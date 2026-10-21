"""Scrub Vanguard leads against Do Not Call files.

Usage: python3 scrub.py leads.csv registry_dir/ area_codes_downloaded.txt [internal_dnc.txt]
registry_dir: the area-code files downloaded from telemarketing.donotcall.gov (any text format;
every 10-digit number found is treated as a do-not-call number).
area_codes_downloaded.txt: one area code per line, exactly the ones you downloaded. Leads in any other
area code are NOT marked clean; they go to leads_not_checked.csv.
Writes leads_clean.csv (OK to dial), leads_removed.csv (on a list) and leads_not_checked.csv.
"""
import csv, datetime, glob, os, re, sys

leads_path, reg_dir = sys.argv[1], sys.argv[2]
covered = {l.strip() for l in open(sys.argv[3]) if l.strip()}
internal = sys.argv[4] if len(sys.argv) > 4 else None
dnc = set()
for path in glob.glob(os.path.join(reg_dir, "**", "*"), recursive=True):
    if os.path.isfile(path):
        with open(path, errors="ignore") as fh:
            for line in fh:
                d = re.sub(r"\D", "", line)
                if len(d) == 11 and d[0] == "1":
                    d = d[1:]
                if len(d) == 10:
                    dnc.add(d)
internal_set = set()
if internal:
    for line in open(internal, errors="ignore"):
        d = re.sub(r"\D", "", line)[-10:]
        if len(d) == 10:
            internal_set.add(d)
rows = list(csv.DictReader(open(leads_path)))
today = datetime.date.today().isoformat()
clean, removed, unchecked = [], [], []
for r in rows:
    d = re.sub(r"\D", "", r["phone_e164"])[-10:]
    if d in internal_set:
        removed.append({**r, "reason": "internal do-not-call"})
    elif d[:3] not in covered:
        unchecked.append({**r, "reason": "area code not downloaded"})
    elif d in dnc:
        removed.append({**r, "reason": "national registry"})
    else:
        clean.append({**r, "dnc_scrub_date": today})
for name, data, extra in (("leads_clean.csv", clean, "dnc_scrub_date"), ("leads_removed.csv", removed, "reason"),
                          ("leads_not_checked.csv", unchecked, "reason")):
    with open(name, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()) + [extra])
        w.writeheader()
        w.writerows(data)
print(f"{len(dnc):,} registry numbers loaded | leads: {len(rows)} | OK to dial: {len(clean)} | removed: {len(removed)} | not checked: {len(unchecked)}")
