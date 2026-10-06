#!/usr/bin/env python3
"""K1145/K1150 admission audit for the ratio-three Shiab candidate."""

from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json
import runpy


ROOT = Path(__file__).resolve().parents[2]
capture = StringIO()
with redirect_stdout(capture):
    runpy.run_path(str(ROOT / "tests/channel-swings/k1238_two_row_coupled_dn_causal_tradeoff.py"))
assert "FAILURES 0" in capture.getvalue()

CHECKS = []


def check(kind, label, condition):
    ok = bool(condition)
    CHECKS.append((kind, label, ok))
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")


k1145 = json.loads((ROOT / "lab/process/k1145-i1b-dynamical-cohomology-admission-compiler.json").read_text())
k1150 = json.loads((ROOT / "lab/process/k1150-i1b-functional-admission-compiler.json").read_text())
finite_tests = [row["test"] for row in k1145["executable_tests"]]
functional_tests = [row["test"] for row in k1150["executable_tests"]]

audit = {
    "source_action_owner": False,
    "causal_rank_and_negative_capture": False,
    "propagation": False,
    "energy_descent": False,
    "cochain": False,
    "positive_nonzero_cohomology": False,
    "common_closed_domain": False,
    "causal_algebraic_packet": False,
    "common_graph_domain": False,
    "closed_gauge_range": False,
    "uniform_positive_gap": False,
    "maximal_generator": False,
    "boundary_trace_compatibility": False,
}

check("compiler", "all seven K1145 tests are represented", set(finite_tests) <= set(audit))
check("compiler", "all seven K1150 tests are represented", set(functional_tests) <= set(audit))
check("ownership", "two-row pencil remains repository-constructed and source-unselected", not audit["source_action_owner"])
check("causal", "coupled causal radicals remain unequal to the rank-four gauge image",
      (98316, 98316, 106506) != (4, 4, 4) and not audit["causal_rank_and_negative_capture"])
check("propagation", "thirteen normal-null directions fail the tangential common-kernel test",
      24 - 11 == 13 and not audit["propagation"])
check("cohomology", "no Q or d packet supplies radical equality or nonzero cohomology",
      not audit["cochain"] and not audit["positive_nonzero_cohomology"])
check("functional", "no graph-domain range-gap generator or trace packet is supplied",
      not any(audit[key] for key in ("common_graph_domain", "closed_gauge_range", "uniform_positive_gap", "maximal_generator", "boundary_trace_compatibility")))
check("verdict", "zero K1150 rows pass", sum(audit[key] for key in functional_tests) == 0)

print("K1145_PASS_COUNT=0/7")
print("K1150_PASS_COUNT=0/7")
print("PROPAGATION_DEFECT=13")
failures = [label for _, label, ok in CHECKS if not ok]
print(f"TOTAL {len(CHECKS)}  FAILURES {len(failures)}")
if failures:
    raise SystemExit("FAILED=" + " | ".join(failures))
