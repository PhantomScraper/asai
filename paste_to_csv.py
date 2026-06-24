#!/usr/bin/env python3
"""
Convert pasted psql table output into revert_list.csv for revert_scraper_status.py.

Expected pasted columns (the per-agency review query):
  user_id | full_name | current_status | revert_to | wrong_changed_at

Usage:
  1. Paste psql output (header/dashes/"(N rows)" lines are fine) into a text file, e.g. agency_969.txt
  2. python3 paste_to_csv.py agency_969.txt --agency 969
  Rows are appended to revert_list.csv (header written once). Duplicate user_ids are skipped.
"""
import argparse
import csv
import os
import re
import sys

OUT_FILE = "revert_list.csv"
FIELDS = ["user_id", "agency_id", "first_name", "last_name", "current_status", "revert_to"]


def parse_line(line):
    parts = [p.strip() for p in line.split("|")]
    if len(parts) < 4 or not re.fullmatch(r"\d+", parts[0]):
        return None
    user_id, full_name, current_status, revert_to = parts[0], parts[1], parts[2], parts[3]
    name_parts = full_name.split()
    first_name = name_parts[0] if name_parts else ""
    last_name = " ".join(name_parts[1:])
    return {
        "user_id": user_id,
        "first_name": first_name,
        "last_name": last_name,
        "current_status": current_status,
        "revert_to": revert_to,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input_file", help="Text file containing pasted psql output")
    ap.add_argument("--agency", type=int, required=True, help="agency_id for these rows")
    args = ap.parse_args()

    existing_ids = set()
    if os.path.exists(OUT_FILE):
        with open(OUT_FILE, newline="") as f:
            for row in csv.DictReader(f):
                existing_ids.add(row["user_id"])

    rows, dupes = [], 0
    with open(args.input_file) as f:
        for line in f:
            parsed = parse_line(line)
            if not parsed:
                continue
            if parsed["user_id"] in existing_ids:
                dupes += 1
                continue
            parsed["agency_id"] = str(args.agency)
            existing_ids.add(parsed["user_id"])
            rows.append(parsed)

    if not rows and not dupes:
        sys.exit(f"No data rows found in {args.input_file} - check the pasted format")

    write_header = not os.path.exists(OUT_FILE) or os.path.getsize(OUT_FILE) == 0
    with open(OUT_FILE, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        if write_header:
            w.writeheader()
        w.writerows(rows)

    msg = f"Added {len(rows)} users (agency {args.agency}) to {OUT_FILE}"
    if dupes:
        msg += f", skipped {dupes} already-present user_ids"
    print(msg)


if __name__ == "__main__":
    main()
