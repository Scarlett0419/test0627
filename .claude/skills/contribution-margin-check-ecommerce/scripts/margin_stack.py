#!/usr/bin/env python3
"""Build the contribution margin stack per SKU from a CSV export.

Used by: contribution-margin-check-ecommerce

Why this exists: the margin skill multiplies and subtracts across six or seven
cost lines for every SKU in the catalog. A language model doing that by eye is
guessing, and a margin number that is quietly wrong is worse than no number,
because the owner will act on it. This does the arithmetic exactly and leaves
the judgement to the skill.

Input: one CSV with a row per SKU. Column names are matched case-insensitively
and several common export spellings are accepted (see COLUMNS). Missing cost
columns are not invented: they are reported as missing and excluded from the
stack, and every affected SKU is flagged so the skill can mark the finding as
an assumption rather than a measurement.

  sku, units, revenue          required
  discounts                    optional, either sign accepted, magnitude is subtracted
  returns                      optional, either sign accepted, magnitude is subtracted
  cogs_unit or cogs_total      optional
  shipping_cost                optional, what the carrier charged you
  shipping_charged             optional, what the customer paid you
  packaging_cost               optional
  ad_spend                     optional, spend attributed to this SKU

Fee rates are passed as flags because they are usually a rate, not a column:
  --payment-fee-pct 2.9 --payment-fee-fixed 0.30 --platform-fee-pct 2.0

usage:
  python3 scripts/margin_stack.py products.csv --payment-fee-pct 2.9
  python3 scripts/margin_stack.py products.csv --json

exit 0 = ran, 2 = could not run (missing file or required columns).
"""
import argparse
import csv
import json
import sys

COLUMNS = {
    "sku": ["sku", "variant sku", "product sku", "id", "product id", "handle"],
    "name": ["name", "title", "product title", "product name"],
    "units": ["units", "quantity", "qty", "units sold", "net quantity", "items sold"],
    "revenue": ["revenue", "net sales", "gross sales", "total sales", "sales"],
    "discounts": ["discounts", "discount", "total discounts", "discount amount"],
    "returns": ["returns", "refunds", "returned value", "refund amount"],
    "cogs_unit": ["cogs unit", "cogs_unit", "unit cost", "cost per item", "cost per unit", "landed cost"],
    "cogs_total": ["cogs", "cogs total", "cogs_total", "total cost", "cost of goods"],
    "shipping_cost": ["shipping cost", "shipping_cost", "fulfilment cost", "fulfillment cost", "carrier cost"],
    "shipping_charged": ["shipping charged", "shipping_charged", "shipping revenue", "shipping collected"],
    "packaging_cost": ["packaging", "packaging cost", "packaging_cost"],
    "ad_spend": ["ad spend", "ad_spend", "spend", "marketing cost", "amount spent"],
    "orders": ["orders", "order count", "orders count", "number of orders"],
}


def norm(s):
    return " ".join(str(s or "").strip().lower().replace("_", " ").split())


def build_map(header):
    seen = {norm(h): h for h in header}
    out = {}
    for key, aliases in COLUMNS.items():
        for alias in aliases:
            if alias in seen:
                out[key] = seen[alias]
                break
    return out


def num(row, colmap, key):
    col = colmap.get(key)
    if not col:
        return None
    raw = row.get(col)
    if raw is None:
        return None
    s = str(raw).strip()
    if s == "" or s.lower() in ("n/a", "na", "none", "-"):
        return None
    neg = s.startswith("(") and s.endswith(")")
    for ch in "()$£€ ,%":
        s = s.replace(ch, "")
    s = s.replace(" ", "")
    try:
        v = float(s)
    except ValueError:
        return None
    return -v if neg else v


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv_path")
    ap.add_argument("--payment-fee-pct", type=float, default=0.0)
    ap.add_argument("--payment-fee-fixed", type=float, default=0.0,
                    help="per-ORDER fixed fee. Needs an orders column, or pass "
                         "--units-per-order so it is not charged once per unit")
    ap.add_argument("--units-per-order", type=float, default=None,
                    help="average units per order, used to convert the fixed fee "
                         "when the export has no orders column")
    ap.add_argument("--platform-fee-pct", type=float, default=0.0)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    try:
        with open(args.csv_path, newline="", encoding="utf-8-sig") as fh:
            rows = list(csv.DictReader(fh))
    except OSError as exc:
        print("could not read %s: %s" % (args.csv_path, exc), file=sys.stderr)
        return 2

    if not rows:
        print("no rows in %s" % args.csv_path, file=sys.stderr)
        return 2

    colmap = build_map(rows[0].keys())
    missing_required = [k for k in ("sku", "units", "revenue") if k not in colmap]
    if missing_required:
        print("missing required columns: %s" % ", ".join(missing_required), file=sys.stderr)
        print("columns found: %s" % ", ".join(rows[0].keys()), file=sys.stderr)
        return 2

    # cogs counts as present if EITHER a unit cost or a total cost column exists
    optional = ["discounts", "returns", "shipping_cost", "packaging_cost", "ad_spend"]
    absent = [k for k in optional if k not in colmap]
    if "cogs_unit" not in colmap and "cogs_total" not in colmap:
        absent.insert(0, "cogs")

    out = []
    incomplete = 0
    negative_outflows = False
    for row in rows:
        sku = row.get(colmap["sku"], "")
        if not str(sku).strip():
            continue
        units = num(row, colmap, "units") or 0.0
        revenue = num(row, colmap, "revenue") or 0.0
        # Discounts and returns are money leaving the business. Exports disagree
        # about the sign: some write 120, some write -120, some write (120).
        # Taking the magnitude means both conventions subtract. Trusting the
        # sign would silently ADD a negative discount back to revenue and
        # inflate every margin below it.
        discounts_raw = num(row, colmap, "discounts") or 0.0
        returns_raw = num(row, colmap, "returns") or 0.0
        if discounts_raw < 0 or returns_raw < 0:
            negative_outflows = True
        discounts = abs(discounts_raw)
        returns = abs(returns_raw)

        cogs = num(row, colmap, "cogs_total")
        if cogs is None:
            unit = num(row, colmap, "cogs_unit")
            cogs = unit * units if unit is not None else None

        orders_col_value = num(row, colmap, "orders")
        ship_cost = num(row, colmap, "shipping_cost")
        ship_charged = num(row, colmap, "shipping_charged") or 0.0
        packaging = num(row, colmap, "packaging_cost")
        ad_spend = num(row, colmap, "ad_spend")

        net_revenue = revenue - discounts - returns + ship_charged
        # A fixed transaction fee is charged once per ORDER, not once per unit.
        # Multiplying it by units overstates the fee on every multi-unit basket
        # and understates the margin of exactly the products people buy in twos.
        if orders_col_value is not None and orders_col_value > 0:
            fee_units = orders_col_value
        elif args.units_per_order:
            fee_units = units / args.units_per_order
        else:
            fee_units = units
        payment_fee = net_revenue * (args.payment_fee_pct / 100.0) + args.payment_fee_fixed * fee_units
        platform_fee = net_revenue * (args.platform_fee_pct / 100.0)

        assumed = []
        for label, value in (("cogs", cogs), ("shipping_cost", ship_cost),
                             ("packaging", packaging), ("ad_spend", ad_spend)):
            if value is None:
                assumed.append(label)
        if assumed:
            incomplete += 1

        cm2 = (net_revenue - (cogs or 0.0) - payment_fee - platform_fee
               - (ship_cost or 0.0) - (packaging or 0.0))
        cm3 = cm2 - (ad_spend or 0.0)
        # A margin percentage computed on a stack that is missing COGS is not a
        # margin, it is an artefact. Withhold the derived figures rather than
        # printing a clean number and hoping the caveat column gets read.
        stack_incomplete = "cogs" in assumed
        cm2_pct = None if stack_incomplete else ((cm2 / net_revenue * 100.0) if net_revenue else None)
        # breakeven ROAS = revenue needed per unit of ad spend to cover variable cost
        breakeven_roas = None if stack_incomplete else ((net_revenue / cm2) if cm2 > 0 else None)

        out.append({
            "sku": str(sku).strip(),
            "name": row.get(colmap.get("name", ""), "") if colmap.get("name") else "",
            "units": round(units, 2),
            "net_revenue": round(net_revenue, 2),
            "cm2": round(cm2, 2),
            "cm2_pct": round(cm2_pct, 1) if cm2_pct is not None else None,
            "cm3": round(cm3, 2),
            "breakeven_roas": round(breakeven_roas, 2) if breakeven_roas else None,
            "missing_cost_lines": assumed,
            "derived_figures_withheld": stack_incomplete,
        })

    out.sort(key=lambda r: r["cm2"])

    negative_before_ads = [r for r in out if r["cm2"] < 0]
    negative_after_ads = [r for r in out if r["cm2"] >= 0 and r["cm3"] < 0]

    summary = {
        "skus": len(out),
        "skus_with_missing_cost_lines": incomplete,
        "cost_columns_absent_from_export": absent,
        "negative_outflow_values_normalised": negative_outflows,
        "total_cm2": round(sum(r["cm2"] for r in out), 2),
        "total_cm3": round(sum(r["cm3"] for r in out), 2),
        "negative_before_ad_spend": len(negative_before_ads),
        "negative_only_after_ad_spend": len(negative_after_ads),
    }

    if args.json:
        print(json.dumps({"summary": summary, "skus": out}, indent=2))
        return 0

    print("SKUs: %d   CM2 total: %.2f   CM3 total: %.2f"
          % (summary["skus"], summary["total_cm2"], summary["total_cm3"]))
    if any(r["derived_figures_withheld"] for r in out):
        print("NOTE: margin %% and breakeven ROAS are withheld where COGS was absent. "
              "A percentage computed without product cost is not a margin.")
    if not colmap.get("orders") and args.payment_fee_fixed and not args.units_per_order:
        print("NOTE: no orders column and no --units-per-order, so the fixed "
              "transaction fee was charged once per UNIT. On multi-unit baskets "
              "that overstates fees and understates margin.")
    if negative_outflows:
        print("NOTE: discount/return values were negative in the export; "
              "magnitudes used so they subtract rather than add.")
    if absent:
        print("MISSING COST COLUMNS (excluded from the stack, findings are assumptions): %s"
              % ", ".join(absent))
    print("negative before ad spend: %d   negative only after ad spend: %d"
          % (summary["negative_before_ad_spend"], summary["negative_only_after_ad_spend"]))
    print()
    print("%-22s %8s %12s %10s %8s %12s  %s"
          % ("sku", "units", "net_revenue", "cm2", "cm2_%", "breakeven", "missing"))
    for r in out[:40]:
        print("%-22s %8.0f %12.2f %10.2f %8s %12s  %s"
              % (r["sku"], r["units"], r["net_revenue"], r["cm2"],
                 "-" if r["cm2_pct"] is None else "%.1f" % r["cm2_pct"],
                 "-" if r["breakeven_roas"] is None else "%.2f" % r["breakeven_roas"],
                 ",".join(r["missing_cost_lines"]) or "-"))
    if len(out) > 40:
        print("... %d more rows, use --json for the full set" % (len(out) - 40))
    return 0


if __name__ == "__main__":
    sys.exit(main())
