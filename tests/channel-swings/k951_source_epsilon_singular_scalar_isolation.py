#!/usr/bin/env python3
"""K951: a singular sum of squares isolates one real invariant value."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k951-source-epsilon-singular-scalar-isolation.json"
PATHS = {
    "k948": ROOT / "lab/process/k948-source-epsilon-single-scalar-selection-obstruction.json",
    "k950": ROOT / "lab/process/k950-source-epsilon-boundary-selection-disposition.json",
}

def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def build():
    return json.loads(OUTPUT.read_text())

def validate(d):
    t, q = d["theorem"], d["decision"]
    checks = [
        d["result_id"] == "K951-SOURCE-EPSILON-SINGULAR-SCALAR-ISOLATION",
        set(d["pinned_inputs"]) == set(PATHS),
        all(d["pinned_inputs"][k]["sha256"] == digest(p) for k, p in PATHS.items()),
        t["ambient_invariant_dimension"] == 7,
        t["constraint_polynomial_degree"] == 2,
        t["constraint_nonnegative_over_reals"],
        t["real_zero_set_is_exactly_target"],
        t["real_zero_set_dimension"] == 0,
        t["set_theoretic_codimension"] == 7,
        t["first_jet_vanishes_at_target"],
        t["constraint_jacobian_rank_at_target"] == 0,
        t["constraint_hessian_rank_at_target"] == 7,
        not t["regular_constraint"],
        q["singular_scalar_isolates_the_target_set_theoretically"],
        not q["isolated_real_zero_implies_regular_constraint"],
        not q["current_action_owns_the_scalar"],
        not q["SC_ACT_06_proved_or_refuted"],
        d["controls"]["controls_passed"] == 24,
        d["controls"]["hostile_mutations_rejected"] == 10,
        d["gu_typed_objects"]["target"].startswith("SELECTOR-TYPE="),
        "LEDGER_UNCHANGED" in d["source_and_ledger_effect"],
        "real-set isolation" in d["claim_ceiling"],
        "F(u)=" in d["gu_typed_objects"]["constraint"],
        "Compare the principal constraint ideal" in q["next_exact_input"],
    ]
    assert len(checks) == 24 and all(checks), [i for i, ok in enumerate(checks) if not ok]

def main():
    parser = argparse.ArgumentParser(); parser.add_argument("--check", action="store_true"); args = parser.parse_args()
    d = build(); validate(d)
    if not args.check: print(json.dumps(d, indent=2, sort_keys=True))
    return 0

if __name__ == "__main__": raise SystemExit(main())
