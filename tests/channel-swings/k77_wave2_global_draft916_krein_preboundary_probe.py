#!/usr/bin/env python3
"""Exact K77 Wave-2 draft-9.16/formal-primalizer template gate.

Run with:
  UV_CACHE_DIR=/tmp/gu-k77-d916-uv uv run --with sympy==1.14.0 \
    python tests/channel-swings/k77_wave2_global_draft916_krein_preboundary_probe.py

The probe does not instantiate all sixteen K77 blocks of the draft operator
or claim a physical self-adjoint evolution domain.  It verifies the rendered
four-field source receipt and constructs discriminating exact templates for
the density-dual primalizer, moving-pairing formal adjoint, Green current,
overlap descent, cross-paired action, and a candidate compact-support
variational core.  Actual D916 assembly, closed evolution, observation, and
a chiral-family index remain separate gates.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


def zero_matrix(matrix: sp.Matrix) -> bool:
    return all(sp.simplify(entry) == 0 for entry in matrix)


def equal_matrix(left: sp.Matrix, right: sp.Matrix) -> bool:
    return left.shape == right.shape and zero_matrix(left - right)


print("A. SOURCE RECEIPT AND LAYER-0")
source = (ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md").read_text()
wave2 = (ROOT / "explorations/k77-wave2-dirac-derham-superig-rebase-2026-08-04.md").read_text()
campaign = (ROOT / "lab/process/k77-post-b2-next-eight-wave-campaign.json").read_text()

check("source", "official draft hash and rendered p46 receipt are recorded",
      "3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4" in source
      and "rendered PDF page 46" in source)
check("source", "draft field and barred-field orders are recorded separately",
      "bar-zeta-minus" in source and "zeta-plus" in source and "four distinct fields" in source)
check("source", "all sixteen equation-9.16 blocks are transcribed",
      all(token in source for token in (
          "star-odot-varpi-pp", "star-odot-d0-varpi-pm", "varpi-pp", "d0-varpi-pm",
          "star-odot-d0-varpi-mp", "star-odot-varpi-mm", "d0-varpi-mp", "varpi-mm",
          "minus-bar-varpi-pp-star", "minus-d0-star-bar-varpi-pm-star",
          "minus-d0-star-bar-varpi-mp-star", "minus-bar-varpi-mm-star",
          "southeast-zero")))
check("source", "draft admits a nonzero southeast rival",
      "non-trivial map in the lower right quadrant" in source)
check("source", "source is silent on a global Krein adjoint and physical domain",
      "SOURCE-SILENT" in source and "closed physical evolution domain" in source)
check("source", "later source retains the southeast zero as a prospective seesaw constraint",
      "02:38:12--02:43:30" in source and "prospective" in source)

check("type", "the draft bilinear and a primalized operator realization are different objects", True)
check("type", "barred fields are independent Berezin variables rather than an automatic adjoint theorem", True)
check("type", "a common variational field space is not a closed physical evolution domain", True)
check("type", "three kinematic pieces are not three observed chiral families", True)
check("type", "the real K77 carrier is not the K95 right-quaternionic carrier", True)


print("\nB. K77 HODGE SIGNS AND AN EXACT FINITE PRIMALIZER TEMPLATE")


def hodge_square_sign(p: int, n: int = 14, q: int = 7) -> int:
    """Pseudo-Riemannian Hodge-square sign on p-forms for signature (*,q)."""
    return -1 if (p * (n - p) + q) % 2 else 1


check("exact", "K77 Hodge square is negative on degrees 0 and 14",
      hodge_square_sign(0) == -1 and hodge_square_sign(14) == -1)
check("exact", "K77 Hodge square is positive on degrees 1 and 13",
      hodge_square_sign(1) == 1 and hodge_square_sign(13) == 1)

# Finite coordinate models for flat:E->E! and R=flat^{-1}.  H13 models the
# Omega13<->Omega1 Hodge identification (star^2=+1); H14 models the
# Omega14<->Omega0 identification (star^2=-1).  These are exact templates,
# not the actual 128-spinor, 16-block D916 primalizer.
Bspin = sp.diag(2, 3)
H13 = sp.Matrix([[0, 1], [1, 0]])
H14 = sp.Matrix([[0, 1], [-1, 0]])
flat_1 = Bspin * H13
R_13 = H13 * Bspin.inv()
flat_0 = Bspin * H14
R_14 = -H14 * Bspin.inv()
check("exact", "Omega13-to-Omega1 primalizer inverts the finite degree-one flat map",
      equal_matrix(R_13 * flat_1, sp.eye(2)))
check("exact", "Omega14-to-Omega0 primalizer carries the required minus sign",
      equal_matrix(R_14 * flat_0, sp.eye(2)))
check("type", "D916:E->E! must be primalized as D_pr=R D916 before an endomorphism Krein adjoint is asked for", True)
check("type", "the finite primalizer template does not instantiate the actual K77 density, Hodge, Shiab, or sixteen D916 blocks", True)


print("\nC. EXACT MOVING-PAIRING FORMAL-ADJOINT AND GREEN TEMPLATE")
x = sp.symbols("x", real=True)
mu = 1 + x
K_dom = sp.diag(1, -1)
K_cod = sp.Matrix([[2 + x, 1], [1, -(1 + x)]])
A = sp.Matrix([[1 + x, x], [2, 1 - x]])
C = sp.Matrix([[x, 2], [-1, x**2]])
u = sp.Matrix([1 + 2*x + x**2, 2 - x + x**3])
v = sp.Matrix([3 - x + 2*x**2, 1 + x + x**3])


def D_apply(principal: sp.Matrix, lower: sp.Matrix, field: sp.Matrix) -> sp.Matrix:
    return principal * field.diff(x) + lower * field


def formal_adjoint(
    principal: sp.Matrix,
    lower: sp.Matrix,
    pairing_dom: sp.Matrix,
    pairing_cod: sp.Matrix,
    density: sp.Expr,
    field: sp.Matrix,
) -> sp.Matrix:
    flux = density * principal.T * pairing_cod * field
    return pairing_dom.inv() * (-flux.diff(x) / density + lower.T * pairing_cod * field)


Dv = D_apply(A, C, v)
Dxu = formal_adjoint(A, C, K_dom, K_cod, mu, u)
green_density = sp.expand(
    mu * (u.T * K_cod * Dv)[0] - mu * (Dxu.T * K_dom * v)[0]
)
current = sp.simplify(mu * (u.T * K_cod * A * v)[0])
check("exact", "moving-density/moving-pairing Green identity holds coefficientwise",
      sp.simplify(green_density - sp.diff(current, x)) == 0)
check("exact", "integrated Stokes identity equals the endpoint current exactly",
      sp.simplify(sp.integrate(green_density, (x, 0, 1)) - (current.subs(x, 1) - current.subs(x, 0))) == 0)

# A deliberately incomplete adjoint omits derivatives of density, principal
# coefficient, and codomain pairing.
naive = K_dom.inv() * (-A.T * K_cod * u.diff(x) + C.T * K_cod * u)
naive_defect = sp.simplify(
    mu * (u.T * K_cod * Dv)[0]
    - mu * (naive.T * K_dom * v)[0]
    - sp.diff(current, x)
)
check("planted", "omitting the moving-coefficient correction leaves a live interior defect",
      naive_defect != 0)

# Extract the derivative coefficient of the formal adjoint from independent
# symbolic functions.  This prevents a self-comparison from masquerading as
# a principal-symbol check.
q0 = sp.Function("q0")(x)
q1 = sp.Function("q1")(x)
q = sp.Matrix([q0, q1])
adjoint_on_q = formal_adjoint(A, C, K_dom, K_cod, mu, q)
derivative_coefficient = sp.Matrix([
    [sp.diff(adjoint_on_q[i], sp.diff(q[j], x)) for j in range(2)]
    for i in range(2)
])
expected_adjoint_principal = -K_dom.inv() * A.T * K_cod
check("exact", "formal-adjoint derivative coefficient is extracted independently and has the expected principal symbol",
      equal_matrix(derivative_coefficient, expected_adjoint_principal))
check("type", "this formula applies to a primalized first-order operator; the actual D916 coefficient assembly remains open", True)


print("\nD. EXACT MODEL ASSOCIATED-BUNDLE OVERLAP DESCENT")
K = sp.diag(1, -1)


def boost(t: sp.Expr) -> sp.Matrix:
    return sp.Matrix([
        [(1 + t**2) / (1 - t**2), 2*t / (1 - t**2)],
        [2*t / (1 - t**2), (1 + t**2) / (1 - t**2)],
    ])


def connection_transform(connection: sp.Matrix, h: sp.Matrix) -> sp.Matrix:
    return sp.simplify(h * connection * h.inv() - h.diff(x) * h.inv())


def conn_apply(connection: sp.Matrix, field: sp.Matrix) -> sp.Matrix:
    return field.diff(x) + connection * field


def conn_adjoint(connection: sp.Matrix, field: sp.Matrix) -> sp.Matrix:
    return -field.diff(x) + K * connection.T * K * field


h12 = boost(x / 5)
h23 = boost(x / 7)
h13 = sp.simplify(h23 * h12)
C1 = sp.Matrix([[x, 1 + x], [x**2, -x]])
C2 = connection_transform(C1, h12)
C3_via2 = connection_transform(C2, h23)
C3_direct = connection_transform(C1, h13)
f1 = sp.Matrix([1 + x + x**2, 2 - x])
g1 = sp.Matrix([2 + x**2, 1 - 2*x + x**3])

check("exact", "both nonconstant transitions preserve the split two-dimensional model pairing",
      equal_matrix(h12.T * K * h12, K) and equal_matrix(h23.T * K * h23, K))
check("exact", "three-patch transition cocycle composes exactly", equal_matrix(h13, h23 * h12))
check("exact", "connection transformation descends covariant differentiation",
      equal_matrix(conn_apply(C2, h12 * f1), h12 * conn_apply(C1, f1)))
check("exact", "formal Krein adjoint is natural on the overlap",
      equal_matrix(conn_adjoint(C2, h12 * g1), h12 * conn_adjoint(C1, g1)))
check("exact", "direct and two-step connection descent agree on the third patch",
      equal_matrix(C3_via2, C3_direct))
check("exact", "the Green preboundary current descends on the overlap",
      sp.simplify(((h12 * g1).T * K * (h12 * f1))[0] - (g1.T * K * f1)[0]) == 0)

hostile_C2 = sp.simplify(h12 * C1 * h12.inv())
check("planted", "pure algebraic conjugation without the derivative correction fails descent",
      not equal_matrix(conn_apply(hostile_C2, h12 * f1), h12 * conn_apply(C1, f1)))
check("type", "the rational three-patch model is not the actual rho(epsilon), Y14 atlas, or sixteen-block D916 descent", True)


print("\nE. FINITE ALGEBRAIC K-SKEW COMPARATOR FOR THE SOUTHEAST FORK")
P = sp.Matrix([[0, 1], [1, 0]])
R = sp.diag(P, P)
B0 = sp.Matrix([[2, 3], [5, 7]])
B_cross = P * B0.T * P
A_skew = sp.diag(11, -11)
Z2 = sp.zeros(2)
M0 = A_skew.row_join(B0).col_join((-B_cross).row_join(Z2))
K4 = sp.diag(P, P)

check("exact", "displayed barred minus-plus order is an involutive row permutation",
      equal_matrix(R * R, sp.eye(4)) and not equal_matrix(R, sp.eye(4)))
check("exact", "finite negative cross-adjoint lower-left plus zero southeast admits a K-skew completion",
      equal_matrix(M0.T * K4 + K4 * M0, sp.zeros(4)))
check("type", "the K-skew completion is conditional on the source bar/star realizing the chosen cross adjoint", True)

mass = sp.diag(13, -13)
M_mass = A_skew.row_join(B0).col_join((-B_cross).row_join(mass))
check("exact", "a finite nonzero southeast block can preserve the same K-skew relation",
      equal_matrix(M_mass.T * K4 + K4 * M_mass, sp.zeros(4)))
check("planted", "source preference for southeast zero is not a uniqueness theorem",
      not equal_matrix(M_mass, M0))
bad_mass = sp.eye(2)
M_bad = A_skew.row_join(B0).col_join((-B_cross).row_join(bad_mass))
check("planted", "an arbitrary nonzero southeast block violates the completion relation",
      not equal_matrix(M_bad.T * K4 + K4 * M_bad, sp.zeros(4)))
check("type", "the finite comparator proves only that algebraic K-skewness does not force southeast zero", True)
check("type", "actual form-degree, gauge-equivariant, real-K77 nonzero southeast admissibility remains open", True)


print("\nF. FINITE ACTION/CURRENT/COVARIANCE CONTROLS AND CANDIDATE CORE")
K2 = sp.diag(1, -1)
D = sp.Matrix([[1, 2], [3, 0]])
D_cross = K2 * D.T * K2
H = sp.zeros(2).row_join(D_cross).col_join(D.row_join(sp.zeros(2)))
K_big = sp.diag(K2, K2)
check("exact", "cross-pairing an operator with its Krein adjoint gives a variational Hessian",
      equal_matrix(H.T * K_big, K_big * H))

t = sp.symbols("t")
bar_chi = sp.Matrix([[2, -1]])
chi = sp.Matrix([3, 5])
G = sp.Matrix([[0, 1], [-2, 0]])
action = (bar_chi * (D + t*G) * chi)[0]
current_once = (bar_chi * G * chi)[0]
check("exact", "finite one-insertion connection variation emits its current exactly once",
      sp.diff(action, t) == current_once)

xi = sp.Matrix([[0, 2], [1, 0]])
delta_D = xi * D - D * xi
delta_action = ((-bar_chi * xi) * D * chi + bar_chi * delta_D * chi + bar_chi * D * (xi * chi))[0]
check("exact", "the finite conjugation covariance identity closes with field and operator response",
      sp.simplify(delta_action) == 0)
check("planted", "dropping operator response breaks the Ward identity",
      sp.simplify(((-bar_chi * xi) * D * chi + bar_chi * D * (xi * chi))[0]) != 0)

check("type", "the finite insertion control does not recompute the predecessor's actual JD+JF connection variation", True)
check("type", "the finite conjugation control is not the full moving inhomogeneous/even-IG Ward identity", True)
check("type", "compactly supported smooth boson/fermion variations define a candidate product variational core", True)
check("type", "compact support kills an integrated boundary term while an unrestricted Green current may be retained as preboundary data", True)
check("type", "the actual D916 and bosonic Euler operators have not yet been shown to share this core", True)
check("type", "no graded/Berezin Hessian or Wave-5 physical evolution domain is claimed", True)


print("\nG. OBSERVER/FAMILY FENCE AND PARTIAL DISPOSITION")
check("source", "the predecessor keeps Curt steps 19 through 23 as the detailed construction map",
      "| 19 |" in wave2 and "| 23 |" in wave2)
check("type", "Omega0, a chosen gamma-trace complement s_Gamma(im Gamma) in Omega1, and ker Gamma in Omega1 are three provenance pieces", True)
check("type", "each provenance block containing an E-plus carrier is a separate observer-character claim", True)
check("type", "three observed families require one observed operator/domain and equivariant chiral index 3[16]", True)
check("type", "P3 cannot act before an operator-defined family receiver exists", True)
check("type", "the campaign keeps the physical-domain and generation-count gates downstream", "COUPLED_KREIN_GREEN_BFV_PHYSICAL_DOMAIN" in campaign and "PHYSICAL_FERMION_COMPLEX_CHIRALITY_ANOMALY_COUNT" in campaign)

result = {
    "counts": dict(COUNTS),
    "failures": FAILURES,
    "source_operator": "DRAFT_916_TRANSCRIBED_AS_DENSITY_DUAL_BILINEAR__NOT_UNIQUE_REALIZATION",
    "formal_packet": "HODGE_PRIMALIZER_AND_MOVING_PAIRING_ADJOINT_GREEN_TEMPLATES_EXACT__ACTUAL_D916_ASSEMBLY_OPEN",
    "descent_fixture": "MODEL_OVERLAP_FIXTURE_EXACT__ACTUAL_D916_DESCENT_OPEN",
    "southeast_fork": "ZERO_SOURCE_PREFERRED__FINITE_KSKEW_NONUNIQUENESS_ONLY__ACTUAL_NONZERO_RIVAL_OPEN",
    "wave2_domain": "CANDIDATE_COMPACT_SUPPORT_VARIATIONAL_CORE_TYPED__ACTUAL_COMMON_CORE_AND_PHYSICAL_EVOLUTION_OPEN",
    "family_status": "THREE_KINEMATIC_PROVENANCE_PIECES__OBSERVED_CHIRAL_INDEX_NOT_CLAIMED",
    "gate_status": "PARTIAL__DRAFT916_SOURCE_MATRIX_AND_FORMAL_PRIMALIZER_TEMPLATES_BUILT__ACTUAL_D916_K77_ASSEMBLY_OPEN",
}

print("\nK77 WAVE-2 DRAFT-9.16 FORMAL-TEMPLATE RESULT")
print(json.dumps(result, indent=2, sort_keys=True))
print("\nChecks: " + " + ".join(f"{n} {kind}" for kind, n in COUNTS.items()))
if FAILURES:
    raise SystemExit(f"FAIL: {len(FAILURES)} checks")
print("PASS: the rendered source matrix and discriminating formal templates close at their stated grade; actual blockwise K77 D916 assembly, common core, physical evolution, and observed-family index remain open.")
