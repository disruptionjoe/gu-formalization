#!/usr/bin/env python3
"""Derive the mechanical LANE-STATE fields and diff them against the committed file.

Register P-H15 (audit CG-08/F-04 / eleven-lens B14): LANE-STATE.yaml is
hand-written and its mechanical fields go stale in the optimistic direction.
This script derives, per lane:

  * last_movement_derived / movement_ref_derived - the newest commit (searched
    across ALL local refs, because live campaigns run on agent/* branches)
    touching any path named in the lane's evidence_ref or movement_ref.
    Untracked-but-present paths (receipt-only runs) fall back to file mtime.
  * needs_joe_derived - True iff lab/process/research-portfolio.json holds any
    work_item in state NEEDS_JOE for that lane (top level: any lane at all).
    NOTE the deliberate asymmetry documented in the gate: a committed
    needs_joe:true with derived false is a permitted manual escalation
    (e.g. a register Tier-0 item that never enters the portfolio); the
    dangerous direction is committed false while derived true.
  * work_status_suggested - heuristic only, never authoritative:
    evidence commit <= STALE_DAYS old -> "moving", else "stale/waiting".
  * updated_at_derived (top level) - the max of the per-lane derived times.

It prints a field-by-field diff against the committed LANE-STATE.yaml and
always exits 0; enforcement lives in
process_gates/lane_state_freshness_audit.py.
"""
import datetime as dt
import json
import os
import subprocess
import sys

import yaml

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LANE_STATE = os.path.join(REPO, "LANE-STATE.yaml")
PORTFOLIO = os.path.join(REPO, "lab", "process", "research-portfolio.json")
STALE_DAYS = 7


def ref_paths(*fields):
    """Split 'a.md; b.md#anchor' style refs into repo-relative path tokens."""
    out = []
    for field in fields:
        for tok in str(field or "").replace("\n", " ").split(";"):
            tok = tok.strip().split("#")[0].strip()
            if tok and "/" in tok and " " not in tok and "@" not in tok:
                out.append(tok)
    return out


def newest_touch(paths):
    """(iso_time, describing_ref) of the newest commit across all refs touching
    any path; mtime fallback for untracked-but-present paths."""
    best = (None, None)
    for p in paths:
        r = subprocess.run(
            ["git", "log", "-1", "--all", "--format=%cI|%h|%s", "--", p],
            cwd=REPO, capture_output=True, text=True)
        line = r.stdout.strip()
        if line:
            iso, sha, subj = line.split("|", 2)
            cand = (iso, "%s %s (%s)" % (sha, subj, p))
        elif os.path.exists(os.path.join(REPO, p)):
            m = dt.datetime.fromtimestamp(
                os.path.getmtime(os.path.join(REPO, p))).astimezone()
            cand = (m.isoformat(timespec="seconds"), "uncommitted mtime (%s)" % p)
        else:
            cand = (None, "MISSING (%s)" % p)
        if cand[0] and (best[0] is None or cand[0] > best[0]):
            best = cand
        elif cand[0] is None and best[0] is None:
            best = cand
    return best


def derive():
    state = yaml.safe_load(open(LANE_STATE))
    portfolio = json.load(open(PORTFOLIO))
    needs = {}
    for w in portfolio.get("work_items", []):
        if str(w.get("state", "")).upper() == "NEEDS_JOE":
            needs.setdefault(str(w.get("lane_id")), []).append(w["id"])
    now = dt.datetime.now().astimezone()
    lanes, top_newest = [], None
    for lane in state.get("lanes", []):
        paths = ref_paths(lane.get("evidence_ref"), lane.get("movement_ref"))
        iso, ref = newest_touch(paths)
        if iso and (top_newest is None or iso > top_newest):
            top_newest = iso
        status = None
        if iso:
            age = (now - dt.datetime.fromisoformat(iso)).days
            status = "moving" if age <= STALE_DAYS else "stale/waiting (%dd)" % age
        lanes.append({
            "lane_id": str(lane.get("lane_id")),
            "committed_evaluated_at": lane.get("evaluated_at"),
            "derived_last_movement": iso,
            "derived_movement_ref": ref,
            "committed_needs_joe": lane.get("needs_joe"),
            "derived_needs_joe": bool(needs.get(str(lane.get("lane_id")))),
            "needs_joe_items": needs.get(str(lane.get("lane_id")), []),
            "committed_work_status": lane.get("work_status"),
            "suggested_work_status": status,
        })
    return {
        "committed_updated_at": state.get("updated_at"),
        "derived_updated_at": top_newest,
        "committed_needs_joe": state.get("needs_joe"),
        "derived_needs_joe": bool(needs),
        "lanes": lanes,
    }


def main():
    d = derive()
    print("== derive_lane_state: committed vs derived (mechanical fields) ==")
    print("top updated_at : committed=%s derived=%s" % (
        d["committed_updated_at"], d["derived_updated_at"]))
    print("top needs_joe  : committed=%s derived(portfolio)=%s" % (
        d["committed_needs_joe"], d["derived_needs_joe"]))
    for ln in d["lanes"]:
        print("-- lane %s" % ln["lane_id"])
        print("   evaluated_at=%s | newest evidence commit=%s" % (
            ln["committed_evaluated_at"], ln["derived_last_movement"]))
        print("   derived movement_ref: %s" % ln["derived_movement_ref"])
        flag = "" if ln["committed_needs_joe"] == ln["derived_needs_joe"] else \
            "  [DIVERGES%s]" % ("" if ln["committed_needs_joe"] else " - OPTIMISTIC")
        print("   needs_joe committed=%s derived=%s%s" % (
            ln["committed_needs_joe"], ln["derived_needs_joe"], flag))
        print("   work_status committed=%s suggested=%s" % (
            ln["committed_work_status"], ln["suggested_work_status"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
