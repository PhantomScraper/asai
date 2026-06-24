#!/usr/bin/env python3
"""
Revert candidate statuses wrongly updated by scraper (Jun 3-6 2026).

Mirrors the admin UI flow so logs are clean:
  1. GET  /api/people/<id>/        -> verify user still has the wrong status
  2. POST /set-user-status/        -> update the real status (no noisy log row)
  3. POST /api/statuschanges/      -> write audit log with changer + reason

Input CSV (exported from the review SQL), columns:
  user_id,agency_id,first_name,last_name,current_status,revert_to

Usage:
  python3 revert_scraper_status.py revert_list.csv \
      --base-url https://<production-host> \
      --token <ADMIN_API_TOKEN> \
      --changer-id <YOUR_USER_ID> \
      --changer-name "Hien Vuong" \
      --dry-run            # run without --dry-run when ready

Results are appended to revert_results.csv. Safe to re-run: users already
reverted (or fixed manually) are skipped by the verify step.
"""
import argparse
import csv
import sys
import time
from datetime import datetime, timezone

import requests

DEFAULT_REASON = "Revert incorrect status update by scraper (Jun 3-6 2026)"
RESULTS_FILE = "revert_results.csv"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv_file")
    ap.add_argument("--base-url", required=True, help="e.g. https://app.example.com (no trailing slash)")
    ap.add_argument("--token", required=True, help="DRF token of the admin account doing the revert")
    ap.add_argument("--changer-id", type=int, required=True, help="User id of the admin account (shown as changer)")
    ap.add_argument("--changer-name", required=True)
    ap.add_argument("--reason", default=DEFAULT_REASON)
    ap.add_argument("--agency", type=int, help="Only process rows of this agency_id")
    ap.add_argument("--sleep", type=float, default=1.0, help="Seconds between users (rate limit is 180/m per endpoint)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    base = args.base_url.rstrip("/")
    s = requests.Session()
    s.headers.update({
        "Authorization": f"Token {args.token}",
        "Content-Type": "application/json;charset=UTF-8",
    })

    with open(args.csv_file, newline="") as f:
        rows = [r for r in csv.DictReader(f)]
    if args.agency:
        rows = [r for r in rows if int(r["agency_id"]) == args.agency]
    if not rows:
        sys.exit("No rows to process")
    print(f"{len(rows)} users to process{' (DRY RUN)' if args.dry_run else ''}")

    results = []
    counts = {"reverted": 0, "skipped": 0, "error": 0}
    for i, row in enumerate(rows, 1):
        user_id = int(row["user_id"])
        agency_id = int(row["agency_id"])
        full_name = f"{row.get('first_name', '')} {row.get('last_name', '')}".strip()
        wrong_status = row["current_status"]
        revert_to = row["revert_to"]
        label = f"[{i}/{len(rows)}] user {user_id} ({full_name}, agency {agency_id})"

        outcome, detail = process_user(
            s, base, args, user_id, agency_id, full_name, wrong_status, revert_to
        )
        counts[outcome] += 1
        print(f"{label}: {outcome} - {detail}")
        results.append({
            "user_id": user_id,
            "agency_id": agency_id,
            "name": full_name,
            "from_status": wrong_status,
            "to_status": revert_to,
            "outcome": outcome,
            "detail": detail,
            "at": datetime.now(timezone.utc).isoformat(),
        })
        time.sleep(args.sleep)

    if results:
        write_header = not file_has_content(RESULTS_FILE)
        with open(RESULTS_FILE, "a", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(results[0].keys()))
            if write_header:
                w.writeheader()
            w.writerows(results)
    print(f"\nDone. reverted={counts['reverted']} skipped={counts['skipped']} "
          f"error={counts['error']} -> {RESULTS_FILE}")
    if counts["error"]:
        sys.exit(1)


def process_user(s, base, args, user_id, agency_id, full_name, wrong_status, revert_to):
    # 1. Verify the user still has the wrong status
    try:
        r = s.get(f"{base}/api/people/{user_id}/", timeout=30)
        r.raise_for_status()
        current = (r.json() or {}).get("status")
    except Exception as e:
        return "error", f"verify failed: {e}"
    if current != wrong_status:
        return "skipped", f"current status is '{current}', expected '{wrong_status}' (already fixed?)"

    if args.dry_run:
        return "skipped", f"dry-run: would set '{wrong_status}' -> '{revert_to}'"

    # 2. Update the real status (same endpoint the admin UI uses)
    try:
        r = s.post(f"{base}/set-user-status/", json={"id": user_id, "status": revert_to}, timeout=30)
        r.raise_for_status()
        if (r.json() or {}).get("unchanged"):
            return "skipped", f"backend reports status already '{revert_to}'"
    except Exception as e:
        return "error", f"set-user-status failed: {e}"

    # 3. Write the audit log row (changer + reason, like the admin UI does)
    log_body = {
        "user": user_id,
        "name": full_name,
        "status": revert_to,
        "old_status": wrong_status,
        "changer": args.changer_id,
        "changer_name": args.changer_name,
        "is_candidate": True,
        "is_employer": False,
        "reason": args.reason,
        "agency": agency_id,
        "is_unchanged": True,  # skip the status-reminder automation check
    }
    try:
        r = s.post(f"{base}/api/statuschanges/", json=log_body, timeout=30)
        r.raise_for_status()
    except Exception as e:
        # Status WAS updated; only the log row failed - flag loudly for manual log insert
        return "error", f"status updated but statuschanges log failed: {e}"

    return "reverted", f"'{wrong_status}' -> '{revert_to}'"


def file_has_content(path):
    try:
        with open(path) as f:
            return bool(f.readline())
    except FileNotFoundError:
        return False


if __name__ == "__main__":
    main()
