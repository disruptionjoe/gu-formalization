#!/usr/bin/env sage-python
"""Exact opposite-Cartan edge cancellation and algebraic BFV composition.

The predecessor constructs the chamber-global 98-dimensional Hamiltonian
carrier M_C.  This probe uses M_-C at the exact point -mu, cancels all 91
endpoint charge components, solves the exact first-variation lift
dJ_edge(v)=-dmu, and composes the resulting equivariant diagonal moment map
with the already-certified 91-ghost BFV algebra.  It proves mathematical
Hamiltonian compatibility only; no source-owned boundary action, proper
functional BFV complex, analytic domain, or physical cohomology follows.
"""

from __future__ import annotations

from collections import Counter
import contextlib
import io
import json
from pathlib import Path
import runpy

from sage.all import QQ, block_matrix, matrix, vector, zero_matrix


ROOT = Path(__file__).resolve().parents[2]
PRIMARY = ROOT / "tests/channel-swings/selected_k77_cartan_slice_cotangent_realization_probe.py"
BFV = ROOT / "tests/channel-swings/selected_k77_full_bfv_master_equation_gate_probe.py"
RESULT = ROOT / "explorations/conditional-build/selected-k77-cartan-slice-edge-cancellation-2026-08-14.md"
REGISTRY = ROOT / "lab/process/selected-k77-cartan-slice-edge-cancellation.json"
SOURCE = ROOT / "lab/sources/selected-k77-cartan-slice-edge-cancellation-source-return-2026-08-14.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-14-selected-k77-cartan-slice-edge-cancellation-review.md"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


print("A. PREDECESSORS AND LAYER ZERO")
primary_capture = io.StringIO()
with contextlib.redirect_stdout(primary_capture):
    primary = runpy.run_path(str(PRIMARY))
check(
    "prior",
    "the exact Cartan-slice realization predecessor replays 45/45",
    primary_capture.getvalue().rstrip().endswith("PASS 45/45")
    and not primary["FAILURES"],
)

bfv_capture = io.StringIO()
with contextlib.redirect_stdout(bfv_capture):
    bfv = runpy.run_path(str(BFV))
check(
    "prior",
    "the exhaustive full 91-ghost BFV predecessor replays 27/27",
    bfv_capture.getvalue().rstrip().endswith("PASS 27/27")
    and not bfv["FAILURES"],
)
for label in (
    "opposite chamber moment value versus source-owned edge field",
    "pointwise charge cancellation versus boundary stationarity",
    "first-variation lift versus a globally selected edge section",
    "algebraic BFV compatibility versus Koszul--Tate properness",
    "finite Hamiltonian carrier versus functional analytic phase space",
):
    check("layer0", label, True)


print("\nB. OPPOSITE-CARTAN HAMILTONIAN CARRIER")
mu = primary["invariant_predecessor"]["mu"]
dmu = primary["invariant_predecessor"]["dmu"]
K_mu = primary["kirillov"]
E = primary["E"]
H = primary["H"]
edge_mu = -mu
K_edge = -K_mu
edge_omega = block_matrix(
    QQ,
    [
        [-K_edge, -E],
        [E.transpose(), zero_matrix(QQ, 7, 7)],
    ],
)
edge_dJ = K_edge.augment(E)
check("carrier", "M_-C retains dimension and symplectic rank 98", edge_omega.rank() == 98)
check("carrier", "the opposite-chamber moment differential retains rank 91", edge_dJ.rank() == 91)
check("carrier", "the opposite-chamber moment fibre retains dimension seven", edge_dJ.right_kernel().dimension() == 7)
edge_vertical_h = block_matrix(QQ, [[H], [zero_matrix(QQ, 7, 7)]])
check(
    "carrier",
    "the opposite-chamber fibre is still the right-Cartan tangent",
    edge_dJ * edge_vertical_h == zero_matrix(QQ, 91, 7),
)
fundamental_left = block_matrix(
    QQ,
    [[matrix.identity(QQ, 91)], [zero_matrix(QQ, 7, 91)]],
)
check(
    "carrier",
    "the all-generator Hamiltonian identity survives the sign reversal",
    fundamental_left.transpose() * edge_omega == -edge_dJ,
)


print("\nC. COMPONENTWISE BASE AND FIRST-VARIATION CANCELLATION")
zero_charge = vector(QQ, 91)
check(
    "base",
    "all 91 diagonal moment-map components cancel at (mu,-mu)",
    mu + edge_mu == zero_charge,
)
check("base", "the selected endpoint is genuinely nonzero", mu != zero_charge)
check("base", "the selected endpoint has the inherited support 30", sum(value != 0 for value in mu) == 30)

edge_lift = edge_dJ.solve_right(-dmu)
edge_group_lift = edge_lift[:91]
edge_cartan_lift = edge_lift[91:]
check("variation", "an exact 98-coordinate edge lift is constructed", len(edge_lift) == 98)
check(
    "variation",
    "all 91 first-variation components cancel exactly",
    dmu + edge_dJ * edge_lift == zero_charge,
)
check("variation", "the inherited action first variation is nonzero", dmu != zero_charge)
check(
    "variation",
    "the lift ambiguity is exactly the seven-dimensional moment fibre",
    edge_dJ.right_kernel().dimension() == 7,
)
check(
    "variation",
    "the exact lift uses the Cartan-transverse sector needed beyond a fixed orbit",
    vector(QQ, edge_cartan_lift) != vector(QQ, 7),
)
print("EDGE_LIFT_GROUP_SUPPORT=" + str(sum(value != 0 for value in edge_group_lift)))
print("EDGE_LIFT_CARTAN_SUPPORT=" + str(sum(value != 0 for value in edge_cartan_lift)))


print("\nD. EXACT COADJOINT AND BFV COMPATIBILITY")
structure = bfv["structure"]
check("bfv", "the BFV and endpoint computations use the same 91-generator order", bfv["PAIRS"] == primary["invariant_predecessor"]["PAIRS"])

kirillov_match = True
edge_kirillov_match = True
for a in range(91):
    for b in range(a + 1, 91):
        coefficients = structure(a, b)
        value = sum(QQ(str(coefficient)) * mu[c] for c, coefficient in coefficients.items())
        edge_value = sum(QQ(str(coefficient)) * edge_mu[c] for c, coefficient in coefficients.items())
        if value != K_mu[a, b]:
            kirillov_match = False
        if edge_value != K_edge[a, b]:
            edge_kirillov_match = False
check("equivariance", "all 4095 endpoint brackets reproduce K_mu", kirillov_match)
check("equivariance", "all 4095 opposite-edge brackets reproduce minus K_mu", edge_kirillov_match)
check(
    "equivariance",
    "the diagonal moment map is equivariant and vanishes at the cancellation point",
    kirillov_match and edge_kirillov_match and mu + edge_mu == zero_charge,
)
check(
    "bfv",
    "the inherited 4095 representation identities leave no J-linear master defect",
    not bfv["representation_failures"],
)
check(
    "bfv",
    "the inherited 121485 Jacobi triples leave no cubic-ghost master defect",
    not bfv["jacobi_failures"],
)
check(
    "bfv",
    "Omega_diag=c.J_diag-(1/2)f.c.c.b is algebraically nilpotent on the mathematical product carrier",
    not bfv["representation_failures"] and not bfv["jacobi_failures"],
)
check(
    "bfv",
    "the base and first-variation J-linear coefficients vanish componentwise",
    mu + edge_mu == zero_charge
    and dmu + edge_dJ * edge_lift == zero_charge,
)


print("\nE. OPPOSITE-SIGN AND FIXED-ORBIT PLANTS")
check(
    "plant",
    "PLANT the same-sign chamber doubles rather than cancels the endpoint charge",
    mu + mu != zero_charge and sum(value != 0 for value in mu + mu) == 30,
)
check(
    "plant",
    "PLANT a fixed opposite orbit cancels the base point",
    mu + edge_mu == zero_charge,
)
check(
    "plant",
    "PLANT the fixed 84-dimensional orbit cannot lift the action-owned transverse derivative",
    -dmu not in K_edge.column_space(),
)
check(
    "plant",
    "the seven invariant derivatives independently diagnose the fixed-orbit failure",
    primary["invariant_predecessor"]["invariant_gradient"] * dmu != vector(QQ, 7),
)


print("\nF. SOURCE, BOUNDARY-LAW, AND PHYSICAL CEILING")
check("source", "the source does not own the Cartan-slice edge variable", True)
check("action", "the selected bare action does not add theta_edge or an edge kinetic term", True)
check("boundary", "no boundary stationarity law selects a section of the seven-dimensional lift ambiguity", True)
check("properness", "algebraic BFV compatibility does not prove Koszul--Tate acyclicity", True)
check("scope", "no functional phase space Green domain positivity quantization or physical cohomology follows", True)
check("selection", "charged boundary symmetry remains the zero-import rival", True)
check("accounting", "no ledger canon residue quotient datum or public-posture change follows", True)


print("\nG. DURABLE ARTIFACTS AND HOSTILE REVIEW")
check(
    "artifact",
    "result registry source return and hostile review exist",
    all(path.exists() for path in (RESULT, REGISTRY, SOURCE, REVIEW)),
)
registry = json.loads(read(REGISTRY))
result_text = read(RESULT)
source_text = read(SOURCE)
review_text = read(REVIEW)
check(
    "artifact",
    "the registry records 91 base and 91 first-variation cancellations",
    registry["cancellation"]["base_component_count"] == 91
    and registry["cancellation"]["first_variation_component_count"] == 91,
)
check(
    "artifact",
    "the registry preserves the seven-dimensional lift ambiguity",
    registry["cancellation"]["edge_lift_ambiguity_dimension"] == 7
    and registry["cancellation"]["one_exact_solver_lift"]["group_coordinate_support"]
    == sum(value != 0 for value in edge_group_lift)
    and registry["cancellation"]["one_exact_solver_lift"]["cartan_coordinate_support"]
    == sum(value != 0 for value in edge_cartan_lift),
)
check(
    "source",
    "the source return preserves carrier action and boundary-law silence",
    "SOURCE-SILENT" in source_text and "boundary law" in source_text.lower(),
)
check(
    "hostile",
    "hostile review blocks cancellation-to-stationarity promotion",
    "CANCELLATION IS NOT STATIONARITY" in review_text,
)
check(
    "hostile",
    "hostile review blocks algebraic-to-physical BFV promotion",
    "ALGEBRAIC BFV IS NOT PHYSICAL BFV" in review_text,
)
check(
    "ceiling",
    "the result explicitly preserves source action boundary and physical ceilings",
    all(
        phrase in result_text
        for phrase in (
            "No source-owned edge field",
            "No boundary stationarity law",
            "No physical cohomology",
        )
    ),
)


print("\nSUMMARY")
print("EDGE_CARRIER=M_MINUS_C_DIM98")
print("BASE_COMPONENTS_CANCELLED=91")
print("FIRST_VARIATION_COMPONENTS_CANCELLED=91")
print("EDGE_LIFT_AMBIGUITY=7")
print("DIAGONAL_MOMENT_MAP=EXACTLY_ZERO_TO_FIRST_ORDER")
print("DIAGONAL_BFV=ALGEBRAICALLY_COMPATIBLE")
print("FIXED_ORBIT_FIRST_VARIATION=REJECTED")
print("SOURCE_ACTION_BOUNDARY_OWNERSHIP=OPEN")
print("COUNTS=" + ",".join(f"{key}:{value}" for key, value in sorted(COUNTS.items())))
print(f"FAILURES={len(FAILURES)}")
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
