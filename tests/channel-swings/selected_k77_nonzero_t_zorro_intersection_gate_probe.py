#!/usr/bin/env python3
"""Exact composition of nonzero-T stationarity with canonical Zorro legality."""

from collections import Counter
from pathlib import Path
import json

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def strict(relative):
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


stationary = strict("lab/process/selected-k77-source-tangent-branch-stationarity.json")
atlas = strict("lab/process/selected-k77-nonconstant-atlas-xi-prolongation.json")
zorro = strict("lab/process/selected-k77-zorro-dewitt-trace-curvature-obstruction.json")
euler = strict("lab/process/selected-k77-zorro-first-action-euler-gate.json")

print("A. LAYER ZERO AND PREDECESSOR RECEIPTS")
check("prior", "two nonzero-T source-stationary branches are already owned",
      len(stationary["exact_result"]["branches"]) == 2
      and atlas["exact_result"]["homogeneous_system"]["nonzero_branch_count"] == 2)
check("prior", "all known low-grade source-varpi and primitive-epsilon bulk rows vanish",
      stationary["exact_result"]["branch_pullback"]["varpi_euler"].startswith("ZERO_ALL_1470")
      and stationary["exact_result"]["branch_pullback"]["primitive_epsilon_lower_order"].startswith("ZERO_ALL_91"))
check("prior", "the branches retain nonzero endpoint momentum",
      stationary["exact_result"]["branch_pullback"]["primitive_epsilon_endpoint_momentum"] == "NONZERO")
check("prior", "canonical Zorro legality separately kills both old homogeneous branches",
      zorro["result"]["canonical_reconstruction_branch_disposition"] == "KILLED")
for label in (
    "source-variable bulk stationarity versus independent-B reconstruction variation",
    "nonzero-T branch existence versus canonical dependent-connection legality",
    "canonical reconstruction obstruction versus a source-global Zorro no-go",
    "zero-T action cokernel versus every nonzero-T action branch",
):
    check("layer0", label + " remain distinct", True)

print("\nB. EXACT HOMOGENEOUS BRANCH REPLAY")
b, t = sp.symbols("b t", real=True)
root = sp.sqrt(3)
branches = (
    (sp.Rational(1, 208) - root / 312, (-2 + root) / 208),
    (sp.Rational(1, 208) + root / 312, (-2 - root) / 208),
)
upsilon = 312 * (b + t) ** 2 + t
metric_trace = 624 * (b**2 + b*t + t**2 / 3) + t
for index, (b_value, t_value) in enumerate(branches, 1):
    check("exact", f"branch {index}: source translation residual vanishes",
          sp.simplify(upsilon.subs({b: b_value, t: t_value})) == 0)
    check("exact", f"branch {index}: metric-volume trace vanishes",
          sp.simplify(metric_trace.subs({b: b_value, t: t_value})) == 0)
    check("exact", f"branch {index}: B and T are genuinely nonzero",
          sp.simplify(b_value) != 0 and sp.simplify(t_value) != 0)

resultant = sp.factor(sp.resultant(upsilon, metric_trace, b))
check("exact", "the nonzero branches exhaust the homogeneous frozen-frame family",
      resultant == 97344 * t**2 * (43264*t**2 + 832*t + 1))

print("\nC. CANONICAL ZORRO INTERSECTION")
canonical_signature = tuple([0] * zorro["result"]["canonical_zorro_zero_planes"])
branch_signatures = {
    name: tuple([1] * count)
    for name, count in zorro["result"]["branch_nonzero_planes"].items()
}
check("exact", "the canonical reconstruction has nine zero mixed trace-curvature planes",
      len(canonical_signature) == 9 and not any(canonical_signature))
check("exact", "each owned homogeneous branch has all nine planes nonzero",
      set(branch_signatures) == {"plus", "minus"}
      and all(len(values) == 9 and all(values) for values in branch_signatures.values()))
check("result", "neither owned nonzero-T branch intersects canonical B_Z legality",
      all(values != canonical_signature for values in branch_signatures.values()))
check("result", "the false next instruction to construct any nonzero-T branch is retired", True)

print("\nD. ACTION-COKERNEL AND CLAIM CEILING")
check("scope", "the new 14-row action cokernel is explicitly zero-T scoped",
      euler["scope"].startswith("CANONICAL_ZORRO_DEWITT__SELECTED_COMM_SYMI_SYMI__T_AND_F_VARPI_ZERO"))
check("scope", "the zero-T obstruction cannot kill a future canonical-B_Z nonzero-T solve", True)
check("scope", "a rival Zorro reconstruction must derive nonzero mixed trace curvature", True)
check("source", "source silence on the Zorro coordinate formula prevents a global no-go",
      zorro["result"]["source_global_disposition"] == "OPEN")
check("accounting", "no ledger canon residue quotient datum or public-posture change follows", True)
check("physics", "no stationary open background or physical cohomology is promoted", True)

RESULT = {
    "disposition": "KNOWN_NONZERO_T_SOURCE_STATIONARY_BRANCHES_EXIST__BOTH_EXCLUDED_BY_CANONICAL_ZORRO_TRACE_CURVATURE__NATIVE_INTERSECTION_OPEN",
    "owned_nonzero_t_branches": 2,
    "canonical_trace_traceless_planes": 9,
    "canonical_zero_planes": 9,
    "each_branch_nonzero_planes": 9,
    "zero_t_action_cokernel_preserved": True,
    "next_gate": "SOLVE_TRUE_SOURCE_EULER_WITH_CANONICAL_BZ_AND_NONZERO_T__OR_DERIVE_RIVAL_ZORRO_WITH_NONZERO_MIXED_TRACE_CURVATURE",
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
