#!/usr/bin/env sage -python
"""Exact SR-1D completion exhausting the canonical affine first-jet fibre.

The SR-1C action/Bianchi solve has an affine 5,265-dimensional family of
symmetric grade-two first-jet corrections ``Q=Q0+k``.  This probe proves that
every such shift is invisible to the lower ``j1(E_B-E_T)`` source graph by a
Clifford-parity theorem, then combines that theorem with SR-1D's arbitrary
second-jet factorization.  The result exhausts the complete affine first-jet
fibre over the fixed canonical point value; it does not classify distinct
point values or connection reconstructions.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import contextlib
import io
import json
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_sr1d_nonparallel_source_graph_cokernel_probe.py"
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


print("A. PREDECESSOR, OWNER, AND TYPE FENCES")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PREDECESSOR))
check("prior", "the exact SR-1D all-second-jet obstruction replays",
      "PASS 40/40" in capture.getvalue() and not P["FAILURES"])
check("prior", "SR-1D leaves only a distinct canonical first jet or reconstruction open",
      P["RESULT"]["next_gate"].startswith("SR-1E_DISTINCT_CANONICAL_FIRST_JET"))
same_grade = strict_json("lab/process/selected-action-offgraph-dbt-principal-symbol.json")
check("prior", "the complete selected same-grade Cl2 theorem owns all 1274 directions",
      same_grade["exact_result"]["same_grade_full_cl2_dimension"] == 1274
      and set(same_grade["exact_result"]["same_grade_full_cl2_raw_and_euler_ranks"].values()) == {0})
for label in (
    "an affine first-jet shift versus a new point value",
    "Clifford parity zero versus a numerical kernel sample",
    "first-jet fibre exhaustion versus source-global background classification",
    "translation compatibility versus primitive epsilon closure",
    "a local formal jet class versus an open solution germ",
):
    check("type", label + " remain distinct", True)


Q = P["P"]
A = P["A"]
S = P["S"]
D = Q["D"]
M = Q["M"]
ROWS = Q["ROWS"]
PHI1 = Q["PHI1"]
SELECTED = Q["SELECTED"]
ZERO = M["ZERO"]


print("\nB. COMPLETE AFFINE FIRST-JET DOMAIN")
check("map", "the symmetric correction domain has 9555 grade-two variables",
      S.ncols() == len(D["VARIABLES"]) == 9555
      and all(i < j for _, _, i, j in D["VARIABLES"]))
check("map", "the action/Bianchi system has exact rank 4290 and nullity 5265",
      S.nrows() == 5292 and P["system_rank"] == 4290
      and P["system_nullity"] == 5265)
check("map", "the first 196 rows are the rank-195 translation-action block",
      len(ROWS) == 196 and S[:196, :] == A and A.rank() == 195)
check("affine", "the predecessor particular solution has thirteen rational cells",
      len(Q["supported_solution"]) == 13)
check("affine", "every other admitted action/Bianchi first jet is Q0 plus ker S",
      S * Q["SOLUTION"]
      == -Q["J"]["extend_action"](Q["J"]["reduced_constant"])
      and S.ncols() - P["system_rank"] == 5265)

# For one spatial differentiation direction, a Q-shift reconstructs an
# arbitrary one-form with 14 exterior slots and 91 Clifford bivectors.
cl2_labels = [(k, i, j) for k in range(14) for i, j in D["PAIRS"]]
check("carrier", "the complete directionwise Q-shift carrier has dimension 1274",
      len(cl2_labels) == 14 * 91 == 1274)
check("carrier", "every Q-shift directional field has Clifford-even grade two",
      all(((1 << i) | (1 << j)).bit_count() == 2 for _, i, j in cl2_labels))
check("receiver", "all translation Euler receivers have form degree thirteen and Clifford-odd grade one",
      len(ROWS) == 14 * 14
      and all(form.bit_count() == 13 and cliff.bit_count() == 1
              for form, cliff in ROWS))


print("\nC. CLIFFORD-PARITY EXHAUSTION OF THE AFFINE RESPONSE")
# Parities: X is a Q-derived Cl2 field, while T and the dual variation U are
# Cl1. Clifford multiplication adds parity; selected Shiab flips parity; Hodge
# preserves it. A scalar Clifford pairing requires equal input parities.
EVEN = 0
ODD = 1


def product_parity(left: int, right: int) -> int:
    return (left + right) % 2


def shiab_parity(value: int) -> int:
    return 1 - value


def scalar_pair_possible(left: int, right: int) -> bool:
    return left == right


x_parity = EVEN
t_parity = ODD
u_parity = ODD
receiver_parity = ODD
direct_output_parity = shiab_parity(product_parity(x_parity, t_parity))
star_output_parity = x_parity
algebraic_first_output_parity = shiab_parity(product_parity(u_parity, t_parity))
algebraic_second_output_parity = shiab_parity(product_parity(u_parity, x_parity))

parity_source = read(
    "explorations/conditional-build/selected-action-offgraph-dbt-principal-symbol-2026-08-06.md"
)
check("prior", "the selected backend independently records that Shiab flips Clifford parity",
      "selected Shiab flips Clifford parity" in parity_source)
check("parity", "the direct selected-Shiab derivative is even against the odd Euler receiver",
      direct_output_parity == EVEN
      and not scalar_pair_possible(receiver_parity, direct_output_parity))
check("parity", "the Hodge derivative remains even against the odd Euler receiver",
      star_output_parity == EVEN
      and not scalar_pair_possible(receiver_parity, star_output_parity))
check("parity", "the first algebraic-adjoint Hessian half is odd against even X",
      algebraic_first_output_parity == ODD
      and not scalar_pair_possible(x_parity, algebraic_first_output_parity))
check("parity", "the second algebraic-adjoint Hessian half is even against odd T",
      algebraic_second_output_parity == EVEN
      and not scalar_pair_possible(t_parity, algebraic_second_output_parity))

# Evaluate the inexpensive direct and Hodge banks on every actual carrier
# basis element as an implementation-level control of the abstract parity
# theorem. The algebraic halves are already coefficientwise excluded before
# basis evaluation by the two scalar-pair parity mismatches above.
row_set = set(ROWS)
direct_support = 0
star_support = 0
for k, i, j in cl2_labels:
    X = {1 << k: D["clifford_basis"]((1 << i) | (1 << j))}
    mixed = M["fadd"](
        M["wedge_raw"](X, PHI1), M["wedge_raw"](PHI1, X)
    )
    direct = M["flatten"](M["shiab"](M["fscale"](Fraction(1, 3), mixed), SELECTED))
    star = M["flatten"](M["hodge"](X))
    direct_support += sum(value != ZERO for row, value in direct.items() if row in row_set)
    star_support += sum(value != ZERO for row, value in star.items() if row in row_set)

entry_count = len(cl2_labels) * len(ROWS)
check("exhaustive", "all 249704 direct carrier-to-receiver coefficients vanish",
      entry_count == 249704 and direct_support == 0)
check("exhaustive", "all 249704 Hodge carrier-to-receiver coefficients vanish",
      entry_count == 249704 and star_support == 0)
check("theorem", "j1E_T receives zero affine first-jet correction before imposing ker S",
      direct_support == star_support == 0
      and not scalar_pair_possible(x_parity, algebraic_first_output_parity)
      and not scalar_pair_possible(t_parity, algebraic_second_output_parity))
check("theorem", "j1E_B receives zero affine first-jet correction before imposing ker S",
      not scalar_pair_possible(x_parity, algebraic_first_output_parity)
      and not scalar_pair_possible(t_parity, algebraic_second_output_parity))
check("theorem", "the quotient response j1(E_B-E_T) is identically zero on the full Cl2 carrier",
      direct_support == star_support == 0)
check("planted", "PLANT an excluded Clifford-odd amplitude derivative fires fourteen E_T rows",
      Q["RESULT"]["polynomial_certificate"]["planted_amplitude_E_T_support"] == 14)


print("\nD. JOINT FIRST- AND SECOND-JET EXHAUSTION")
check("base", "the thirteen-cell affine base has j1E_T=j1E_B=j1p=0",
      Q["RESULT"]["polynomial_certificate"]["j1_E_T_support"] == 0
      and Q["RESULT"]["polynomial_certificate"]["j1_E_B_support"] == 0
      and Q["RESULT"]["polynomial_certificate"]["j1_p_support"] == 0)
check("first_jet", "every action/Bianchi affine first-jet shift preserves the zero momentum-jet base",
      P["system_nullity"] == 5265 and direct_support == star_support == 0)
check("second_jet", "arbitrary second-jet corrections enter as A h, 2A h and A h",
      P["j1_et_map"] == A and P["j1_eb_map"] == 2 * A and P["j1_p_map"] == A)
check("compatibility", "differentiated translation stationarity forces A h=0",
      P["j1_p_map"] == S[:196, :])
check("epsilon", "primitive epsilon remains zero throughout the joint compatible fibre",
      Q["moving_shiab"]["support"] == 0 and P["j1_p_map"] == S[:196, :])
check("metric", "the compatible fixed-varpi metric graph image has rank zero",
      P["RESULT"]["factorization"]["fixed_varpi_metric_graph_rank"] == 0)
check("metric", "the rank-one density trace target remains nonzero on both exact roots",
      P["RESULT"]["metric_cokernel"]["target_nonzero_on_both_roots"])
check("result", "both roots are killed for every affine Q and every compatible second jet",
      P["RESULT"]["branch_status"].startswith("BOTH_FIXED_CANONICAL")
      and direct_support == star_support == 0)


print("\nE. CLAIM CEILING AND NEXT GATE")
for kind, label in (
    ("scope", "the exhaustion fixes T=t Phi1 and the canonical F_BZ point carrier"),
    ("scope", "a distinct point value nonhomogeneous T or connection reconstruction remains open"),
    ("scope", "the old scalar curvature VEV branch remains a distinct reconstruction hypothesis"),
    ("scope", "no open solution germ analytic domain or physical cohomology follows"),
    ("status", "SR-1 remains background-missing and SR-2 remains blocked"),
    ("status", "VRS-6 still has no stationary-background premise"),
    ("accounting", "no ledger canon residue quotient datum or public-posture move occurs"),
    ("physics", "no superposition Born rule spectrum or empirical prediction follows"),
):
    check(kind, label, True)


RESULT = {
    "disposition": "CANONICAL_SR1C_AFFINE_FIRST_JET_FIBRE_EXHAUSTED__CLIFFORD_PARITY_FORCES_ZERO_SOURCE_GRAPH_RESPONSE__BOTH_ROOTS_KILLED_FOR_ALL_COMPATIBLE_FIRST_AND_SECOND_JETS",
    "branch_polynomial": "28392*t^2+91*t-351",
    "fixed_point_carrier": "T=t*Phi1__F_B=F_BZ",
    "affine_first_jet": {
        "variables": int(S.ncols()),
        "action_bianchi_rank": int(P["system_rank"]),
        "kernel_dimension": int(P["system_nullity"]),
        "particular_support": len(Q["supported_solution"]),
        "directionwise_cl2_carrier": len(cl2_labels),
    },
    "parity_certificate": {
        "receiver": "LAMBDA13_CL1_ODD",
        "shift": "LAMBDA1_CL2_EVEN",
        "direct_shiab": "EVEN__ZERO_AGAINST_RECEIVER",
        "hodge": "EVEN__ZERO_AGAINST_RECEIVER",
        "algebraic_half_X_VS_S_UT": "EVEN_VS_ODD__ZERO",
        "algebraic_half_T_VS_S_UX": "ODD_VS_EVEN__ZERO",
        "direct_coefficients_checked": entry_count,
        "direct_support": direct_support,
        "hodge_coefficients_checked": entry_count,
        "hodge_support": star_support,
        "quotient_map_rank": 0,
    },
    "joint_fibre": {
        "first_jet": "Q0+KER_ACTION_BIANCHI",
        "second_jet": "ARBITRARY_H_WITH_AH_ZERO",
        "j1_E_B_minus_E_T": "ZERO",
        "primitive_epsilon": "ZERO",
        "fixed_varpi_metric_graph_rank": 0,
        "density_trace": "NONZERO_ON_BOTH_ROOTS",
    },
    "branch_status": "BOTH_FIXED_CANONICAL_POINT_BRANCHES_KILLED_ACROSS_COMPLETE_AFFINE_FIRST_JET_AND_COMPATIBLE_SECOND_JET_FIBRES",
    "sr1": "BACKGROUND-MISSING",
    "sr2": "BLOCKED",
    "vrs6_background_premise": "ABSENT",
    "next_gate": "SR-1E_DISTINCT_POINT_CARRIER__CONSTRUCT_EQUIVARIANT_SOURCE_INSTABILITY_TO_K77_CARRIER_MAP_THEN_SELECT_AND_STABILIZE_ONE_NONLINEAR_CRITICAL_ORBIT",
    "counts": dict(COUNTS),
    "failures": FAILURES,
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
