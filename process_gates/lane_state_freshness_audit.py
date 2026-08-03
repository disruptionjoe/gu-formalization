#!/usr/bin/env python3
"""Process gate: fail when LANE-STATE.yaml's mechanical fields diverge from the
derivable truth beyond the stated tolerance.

Register P-H15 (audit CG-08/F-04 / eleven-lens B14). Enforced checks, with
TOLERANCE_DAYS = 7 (stated staleness tolerance):

  1. Broken pointers: every path token in each lane's evidence_ref /
     movement_ref must exist in the working tree or in git history (any ref).
  2. Staleness: a lane's committed evaluated_at (and the top-level updated_at)
     must not lag the newest commit touching that lane's referenced paths by
     more than TOLERANCE_DAYS. This is the audit's exact failure mode: results
     landed and the lane story never moved.
  3. needs_joe optimism: if the portfolio holds a NEEDS_JOE work_item for a
     lane (or at all) while the committed file says needs_joe: false, FAIL.
     The opposite direction (committed true, derived false) is a permitted
     manual escalation - register Tier-0 items never enter the portfolio -
     and is only reported.
  4. Portfolio freshness: research-portfolio.json's updated_at must be within
     TOLERANCE_DAYS of that file's own newest commit.

Exit 0 on pass, 1 on any failure (fail-closed; this gate contains real
assert/exit paths per the certificate-shape standard, register P-C3).
"""
import datetime as dt
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lab", "automation"))
import derive_lane_state as dls  # noqa: E402

TOLERANCE_DAYS = 7
FAILURES = []


def parse_when(value):
    if value is None:
        return None
    s = str(value)
    try:
        t = dt.datetime.fromisoformat(s)
    except ValueError:
        return None
    if t.tzinfo is None:
        t = t.astimezone()
    return t


def check(cond, msg):
    if cond:
        print("  PASS  %s" % msg)
    else:
        print("  FAIL  %s" % msg)
        FAILURES.append(msg)


def lag_days(committed, derived_iso):
    c, d = parse_when(committed), parse_when(derived_iso)
    if c is None or d is None:
        return None
    return (d - c).total_seconds() / 86400.0


def main():
    print("== lane_state_freshness_audit (tolerance %d days) ==" % TOLERANCE_DAYS)
    d = dls.derive()

    # 1. broken pointers
    state = dls.yaml.safe_load(open(dls.LANE_STATE))
    for lane in state.get("lanes", []):
        for p in dls.ref_paths(lane.get("evidence_ref"), lane.get("movement_ref")):
            present = os.path.exists(os.path.join(dls.REPO, p)) or \
                dls.newest_touch([p])[0] is not None
            check(present, "lane %s pointer resolves: %s" % (lane.get("lane_id"), p))

    # 2. staleness per lane + top
    for ln in d["lanes"]:
        lag = lag_days(ln["committed_evaluated_at"], ln["derived_last_movement"])
        check(lag is not None,
              "lane %s has parseable evaluated_at and derivable movement" % ln["lane_id"])
        if lag is not None:
            check(lag <= TOLERANCE_DAYS,
                  "lane %s evaluated_at lags newest evidence commit by %.1fd (<= %dd)"
                  % (ln["lane_id"], max(lag, 0.0), TOLERANCE_DAYS))
    top_lag = lag_days(d["committed_updated_at"], d["derived_updated_at"])
    check(top_lag is not None and top_lag <= TOLERANCE_DAYS,
          "top updated_at lags newest evidence commit by %s (<= %dd)"
          % ("%.1fd" % max(top_lag, 0.0) if top_lag is not None else "?", TOLERANCE_DAYS))

    # 3. needs_joe optimism (one-directional, documented above)
    check(not (d["derived_needs_joe"] and not d["committed_needs_joe"]),
          "top needs_joe not optimistically false against portfolio NEEDS_JOE")
    for ln in d["lanes"]:
        check(not (ln["derived_needs_joe"] and not ln["committed_needs_joe"]),
              "lane %s needs_joe not optimistically false (portfolio: %s)"
              % (ln["lane_id"], ln["needs_joe_items"] or "none"))
        if ln["committed_needs_joe"] and not ln["derived_needs_joe"]:
            print("  NOTE  lane %s carries a manual needs_joe escalation "
                  "(no portfolio NEEDS_JOE item) - permitted" % ln["lane_id"])

    # 4. portfolio freshness
    pf = json.load(open(dls.PORTFOLIO))
    pf_newest = dls.newest_touch(["lab/process/research-portfolio.json"])[0]
    pf_lag = lag_days(pf.get("updated_at"), pf_newest)
    check(pf_lag is not None and pf_lag <= TOLERANCE_DAYS,
          "portfolio updated_at lags its newest commit by %s (<= %dd)"
          % ("%.1fd" % max(pf_lag, 0.0) if pf_lag is not None else "?", TOLERANCE_DAYS))

    if FAILURES:
        print("RESULT: FAIL (%d)" % len(FAILURES))
        for f in FAILURES:
            print("  - %s" % f)
        sys.exit(1)
    print("RESULT: PASS - committed mechanical fields within tolerance of derived truth")
    sys.exit(0)


if __name__ == "__main__":
    assert TOLERANCE_DAYS > 0
    main()
