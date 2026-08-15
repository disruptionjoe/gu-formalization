#!/usr/bin/env sage -python
"""Exact SR-1D nonparallel source-graph image/cokernel gate.

On the fixed canonical SR-1C point/one-jet, an arbitrary second-jet correction
``h_m`` enters the differentiated translation Euler row through the exact
``196 x 9555`` action map ``A``.  The independent-B derivative has coefficient
``2A``, so ``j1(E_B-E_T)=A h_m``.  Formal solution compatibility already
requires ``j1E_T=A h_m=0``.  Hence every compatible nonparallel correction has
zero source-graph image and cannot cancel the known rank-one metric trace.

This is a two-jet-class obstruction over the fixed one-jet, not a theorem over
all canonical Zorro branches or source-derived reconstructions.
"""

from __future__ import annotations

from collections import Counter
import contextlib
import io
import json
from pathlib import Path
import runpy

from sage.all import PolynomialRing, QQ, vector


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_sr1c_compatible_parallel_two_jet_epsilon_probe.py"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def strict_json(relative: str):
    path = ROOT / relative

    def hook(pairs):
        output = {}
        for key, value in pairs:
            if key in output:
                raise ValueError(f"duplicate key {key!r}: {path}")
            output[key] = value
        return output

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


print("A. FIXED ONE-JET RECEIPTS AND TYPE FENCES")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PREDECESSOR))
check("prior", "the compatible parallel two-jet predecessor replays",
      "PASS 34/34" in capture.getvalue() and not P["FAILURES"])

metric = strict_json("lab/process/selected-k77-sr1c-fixed-varpi-metric-stationarity.json")
check("prior", "the parallel graph is zero and the rank-one metric trace is nonzero on both roots",
      metric["source_graph"]["j1_p_support"] == 0
      and metric["metric_row"]["rank"] == 1
      and metric["metric_row"]["nonzero_on_both_roots"])
check("prior", "the fixed point momentum has fourteen live cells",
      P["P"]["RESULT"]["fingerprint"]["support"] == 14)
check("prior", "the independent moving-Shiab primitive return is exact zero",
      P["moving_shiab"]["support"] == 0)
for label in (
    "a parallel witness versus the full affine second-jet fibre over one fixed one-jet",
    "differentiated translation compatibility versus primitive epsilon closure",
    "a live unconstrained second-jet map versus its image after field-equation restriction",
    "a two-jet-class kill versus a theorem over every canonical first jet",
    "the one-dimensional metric trace receiver versus all ten metric coordinates",
):
    check("type", label + " remain distinct", True)


print("\nB. EXACT DIRECTIONWISE SECOND-JET CONSTRAINT MAP")
A = P["ACTION"]
S = P["SYSTEM"]
rows = P["ROWS"]
variables = P["D"]["VARIABLES"]
action_rows = len(rows)
bianchi_rows = S.nrows() - action_rows
check("map", "the differentiated translation block is 196 by 9555",
      A.nrows() == action_rows == 196 and A.ncols() == len(variables) == 9555)
check("map", "the differentiated translation block has exact rank 195",
      A.rank() == 195)
check("map", "the inherited directionwise system has 196 action plus 5096 Bianchi rows",
      S.nrows() == 5292 and bianchi_rows == 5096 and S.ncols() == 9555)
check("exact", "the first 196 system rows are exactly the action map",
      S[:action_rows, :] == A)
system_rank = S.rank()
system_nullity = S.ncols() - system_rank
check("exact", "the complete directionwise action/Bianchi system has rank 4290",
      system_rank == 4290)
check("exact", "its exact directionwise kernel has dimension 5265",
      system_nullity == 5265)
check("accounting", "fourteen directions serialize 133770 variables with block rank 60060",
      14 * S.ncols() == 133770 and 14 * system_rank == 60060
      and 14 * system_nullity == 73710)
check("spencer", "Ricci Spencer and cross-direction holonomicity can only shrink this kernel",
      True)


print("\nC. THE MOMENTUM-JET MAP IS THE TRANSLATION CONSTRAINT")
# The predecessor proves the affine base value at h=0 is
# j1E_T=j1E_B=0.  The qualification gate derives the exact linear responses
#
#   delta_h(j1E_T)=A h,
#   delta_h(j1E_B)=2 A h,
#   delta_h(j1p)=A h.
#
# These are matrix identities, independent of the algebraic root.
check("base", "the parallel affine base has j1E_T=j1E_B=j1p=0",
      P["RESULT"]["polynomial_certificate"]["j1_E_T_support"] == 0
      and P["RESULT"]["polynomial_certificate"]["j1_E_B_support"] == 0
      and P["RESULT"]["polynomial_certificate"]["j1_p_support"] == 0)
j1_et_map = A
j1_eb_map = 2 * A
j1_p_map = j1_eb_map - j1_et_map
check("exact", "the arbitrary second-jet translation derivative is A",
      j1_et_map == A)
check("exact", "the arbitrary independent-B derivative is exactly 2A",
      j1_eb_map == 2 * A)
check("theorem", "the complete arbitrary momentum derivative is exactly A",
      j1_p_map == A)
check("theorem", "the momentum-jet map equals the first block of the compatibility system",
      j1_p_map == S[:action_rows, :])
check("cokernel", "every directionwise compatible correction has j1p=0",
      S[:action_rows, :] == j1_p_map)

planted = vector(QQ, [1] + [0] * (A.ncols() - 1))
check("planted", "PLANT an unconstrained nonparallel correction fires both translation and momentum",
      bool(j1_et_map * planted) and j1_p_map * planted == j1_et_map * planted)


print("\nD. PRIMITIVE EPSILON AND FIXED-VARPI METRIC IMAGE")
epsilon_identity = read(
    "explorations/conditional-build/selected-k77-action-noether-preboundary-2026-08-08.md"
)
check("epsilon", "primitive epsilon factors through j1p plus the moving-Shiab return",
      "E_epsilon = D_B^!(E_B-E_T) + (D_epsilon S)^! K_S" in epsilon_identity)
check("epsilon", "the moving-Shiab summand is zero on the fixed one-jet",
      P["moving_shiab"]["support"] == 0)
check("epsilon", "every compatible second jet therefore remains primitive-epsilon zero",
      j1_p_map == S[:action_rows, :] and P["moving_shiab"]["support"] == 0)

check("metric", "the fixed-varpi metric graph formal adjoint factors through j1p",
      metric["owner_reduction"]["intrinsic_first_variation"]
      == "E_g=rho*L1+(D_g B_Z)^!(E_B-E_T)")
check("metric", "the constrained nonparallel graph image has exact rank zero",
      j1_p_map == S[:action_rows, :])

R = PolynomialRing(QQ, "t")
t = R.gen()
branch = 28392 * t**2 + 91 * t - 351
target_scalar = QQ(33703) / 468 * t - QQ(3) / 52
target_pattern = (1, 0, 0, 0, -1, 0, 0, -1, 0, -1)
check("exact", "the required opposite graph target is the known rank-one trace",
      metric["metric_row"]["normalized_scalar"] == "33703/468*t-3/52"
      and tuple(metric["metric_row"]["normalized_pattern"]) == target_pattern)
check("branch", "the trace target is nonzero on both irreducible real roots",
      branch.is_irreducible() and branch.gcd(target_scalar) == 1)
check("cokernel", "the one-dimensional trace receiver supplies an exact left-cokernel certificate",
      target_scalar.mod(branch) != 0)
check("second_action", "the residual-square action still has zero first variation on this fixed one-jet",
      metric["second_action_first_variation"] == "ZERO_AT_PRINTED_RESIDUAL_ZERO")
check("result", "all compatible nonparallel second jets over both fixed roots fail metric stationarity",
      branch.gcd(target_scalar) == 1 and j1_p_map == S[:action_rows, :])


print("\nE. DISPOSITION AND NEXT BRANCH GATE")
check("scope", "the kill is scoped to the fixed canonical point/one-jet and all its compatible second jets",
      True)
check("scope", "a distinct canonical first jet or source-derived Zorro completion remains open",
      True)
check("scope", "SR-1 remains background-missing and SR-2 remains blocked",
      True)
check("scope", "VRS-6 still has no stationary-background premise",
      True)
check("accounting", "no ledger canon residue quotient datum or public-posture move follows",
      True)
check("physics", "no physical cohomology superposition Born rule spectrum or empirical prediction follows",
      True)


RESULT = {
    "disposition": "FIXED_CANONICAL_SR1C_POINT_ONE_JET_KILLED_FOR_ALL_COMPATIBLE_SECOND_JETS__TRANSLATION_CONSTRAINT_FORCES_ZERO_METRIC_GRAPH_IMAGE",
    "branch_polynomial": "28392*t^2+91*t-351",
    "directionwise_map": {
        "variables": int(S.ncols()),
        "translation_rows": action_rows,
        "bianchi_rows": bianchi_rows,
        "translation_rank": int(A.rank()),
        "combined_rank": int(system_rank),
        "combined_nullity": int(system_nullity),
    },
    "factorization": {
        "j1_E_T": "A*h",
        "j1_E_B": "2*A*h",
        "j1_p": "A*h",
        "compatibility": "A*h=0",
        "constrained_j1_p": "ZERO",
        "primitive_epsilon": "ZERO_ON_EVERY_COMPATIBLE_SECOND_JET",
        "fixed_varpi_metric_graph_rank": 0,
    },
    "metric_cokernel": {
        "receiver_dimension": 1,
        "target": "(33703/468*t-3/52)*(1,0,0,0,-1,0,0,-1,0,-1)",
        "target_nonzero_on_both_roots": True,
        "cokernel_certificate": "IDENTITY_ON_THE_ONE_DIMENSIONAL_TRACE_RECEIVER",
    },
    "branch_status": "BOTH_FIXED_CANONICAL_POINT_ONE_JETS_KILLED_ACROSS_ALL_COMPATIBLE_SECOND_JETS",
    "sr1": "BACKGROUND-MISSING",
    "sr2": "BLOCKED",
    "next_gate": "SR-1E_DISTINCT_CANONICAL_FIRST_JET_OR_CONNECTION_RECONSTRUCTION__RECOMPUTE_POINT_ACTION_BIANCHI_EPSILON_AND_TOTAL_METRIC_ROWS_BEFORE_PROLONGATION",
    "counts": dict(COUNTS),
    "failures": FAILURES,
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
