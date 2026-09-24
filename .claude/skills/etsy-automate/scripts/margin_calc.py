#!/usr/bin/env python3
"""Calcule le prix de vente Etsy selon 3 scenarios de marge.

Frais Etsy integres (valeurs 2025, ajustables) :
- Frais de transaction : 6.5% du prix de vente
- Frais de mise en vente : 0.20 USD par fiche
- Frais de traitement paiement : ~4% + 0.30 (varie par pays, defaut FR)

Usage :
  python3 margin_calc.py --cost 2.30 --shipping 0 --market-avg 22
  python3 margin_calc.py --cost 2.30 --shipping 1.50 --market-avg 22 --currency EUR
"""

from __future__ import annotations

import argparse

TRANSACTION_FEE = 0.065
LISTING_FEE = 0.20
PAYMENT_PCT = 0.04
PAYMENT_FIXED = 0.30


def etsy_fees(sale_price: float) -> float:
    return (
        sale_price * TRANSACTION_FEE
        + LISTING_FEE
        + sale_price * PAYMENT_PCT
        + PAYMENT_FIXED
    )


def price_for_margin(cost: float, shipping: float, margin: float) -> float:
    """Trouve le prix de vente pour une marge nette cible.

    marge nette = (prix - cout - shipping - frais_etsy) / prix
    On resout par iteration car les frais dependent du prix.
    """
    price = (cost + shipping) * (1 + margin) + 1.0
    for _ in range(100):
        fees = etsy_fees(price)
        net = price - cost - shipping - fees
        current_margin = net / price if price > 0 else 0
        error = current_margin - margin
        if abs(error) < 0.0001:
            break
        price = price - (current_margin - margin) * price * 0.5
    return round(price, 2)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cost", type=float, required=True, help="Cout AliExpress unitaire.")
    parser.add_argument("--shipping", type=float, default=0.0, help="Cout livraison fournisseur.")
    parser.add_argument("--market-avg", type=float, default=None, help="Prix moyen concurrence Etsy.")
    parser.add_argument("--currency", default="EUR", help="Devise affichee.")
    args = parser.parse_args()

    cur = args.currency
    print(f"\nCALCUL MARGE — cout {args.cost} {cur}, livraison {args.shipping} {cur}\n")
    print(f"{'Marge cible':<14}{'Prix vente':<14}{'Frais Etsy':<14}{'Profit net':<14}")
    print("-" * 56)

    for margin in (0.30, 0.50, 0.70):
        price = price_for_margin(args.cost, args.shipping, margin)
        fees = etsy_fees(price)
        net = price - args.cost - args.shipping - fees
        print(
            f"{int(margin*100):>3}%{'':<10}"
            f"{price:>8.2f} {cur:<4}"
            f"{fees:>8.2f} {cur:<4}"
            f"{net:>8.2f} {cur:<4}"
        )

    if args.market_avg:
        print(f"\nPrix moyen concurrence Etsy : {args.market_avg} {cur}")
        for margin in (0.30, 0.50, 0.70):
            price = price_for_margin(args.cost, args.shipping, margin)
            pos = "sous" if price < args.market_avg else "au-dessus"
            diff = abs(price - args.market_avg)
            print(f"  Marge {int(margin*100)}% -> {price} {cur} ({pos} marche, ecart {diff:.2f})")

    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
