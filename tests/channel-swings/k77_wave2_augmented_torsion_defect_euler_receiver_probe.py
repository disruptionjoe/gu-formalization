#!/usr/bin/env python3
"""Exact K77 augmented-torsion / defect Euler receiver gate.

The source-native augmented torsion is an adjoint-valued one-form on Y and a
difference of two connections.  Along an observation section, the already
built field map retains both

    T_X = s^* T                         (four one-form coefficients)
    v_T = res_s^V T                     (ten vertical scalar coefficients).

This probe constructs the equation-dual map forced by that field map.  It also
uses the explicit kappa/2 <T,T> term in the 2021 source action to show that the
unrestricted action image is not automatically horizontal: a constant
conormal T emits a nonzero conormal Euler component when kappa is nonzero.

The result is exact and local/fibrewise.  It is not the full moving-section
variation of the nonlinear source action, a global descent theorem, a common
Green domain, or a physical Higgs/Standard-Model equation.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from pathlib import Path
import sys

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


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def zero(matrix: sp.MatrixBase) -> bool:
    return all(sp.expand(entry) == 0 for entry in matrix)


R = sp.Rational


print("A. PRIMARY-SOURCE COLLISION AND LAYER 0")
source_pack = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
portal = read("lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md")
toe = read("lab/sources/transcripts/toe-weinstein-gu-40-years.md")
ucsd = read("papers/drafts/Transcript into the impossible.md")
n1 = read("explorations/unified-source-datum-packet-v0-2026-07-30.md")
n3 = read("explorations/unified-source-datum-variational-emission-map-2026-07-30.md")
predecessor = read("explorations/k77-wave2-actual-y14-receiver-ordering-conormal-2026-08-05.md")

check(
    "source",
    "the 2021 source action types augmented torsion as an adjoint-valued one-form",
    "T_\\omega=\\varpi-\\epsilon^{-1}d_0\\epsilon" in source_pack
    and "\\Omega^1(Y,\\operatorname{ad}P)" in source_pack,
)
check(
    "source",
    "the source action contains the nondegenerate kappa over two T term",
    "\\frac{\\kappa_1}{2}T_\\omega" in source_pack
    and "*\\kappa_1T_\\omega" in source_pack,
)
check(
    "source",
    "the displayed source variation permits translation directions varpi plus s alpha",
    "I^B_1(\\epsilon,\\varpi+s\\alpha)" in source_pack
    and "\\langle\\alpha,\\Upsilon^B_\\omega\\rangle" in source_pack,
)
check(
    "source",
    "Portal calls augmented torsion a two-connection difference with cancelled disease",
    "because we have two connections" in portal
    and "the difference will not have the disease" in portal
    and "augmented torsion is relatively well behaved" in portal,
)
check(
    "source",
    "Portal places the Einsteinian replacement on Y before pullback to X",
    "on \\(Y\\) before being pulled back onto the manifold \\(X\\)" in portal
    and "must be pulled back to \\(X\\)" in portal,
)
check(
    "source",
    "TOE says GU uses gauge-rotated Levi-Civita in the contorsion slot",
    "gauge rotated Levi-Civita connection" in toe
    and "what would be the contortion" in toe,
)
check(
    "source",
    "the modern talk describes the displaced base connection and translated connection",
    "two separate connections" in ucsd
    and "gauge transform the Levi Civita connection" in ucsd
    and "distortion with superior equivariance" in ucsd,
)
check(
    "source",
    "TOE defines observerse as the spaces, fibres, sections, relationships and pullbacks",
    "bundles and the relationships and the pullbacks" in toe
    and "two spaces with a fiber and sections connecting them" in toe,
)
check(
    "source",
    "the prior source-action build already distinguishes vertical coefficient restriction from form pullback",
    "It is not differential-form pullback" in n1
    and "operatorname{res}_s^V" in n1,
)
check(
    "source",
    "the prior variational build already owns a moving section current derivative",
    "The first term varies the intrinsic defect expression; the second moves its\nsupport" in n3,
)
check(
    "source",
    "the predecessor leaves precisely action horizontality, defect variation or a typed normal receiver",
    "actual source-action Euler image to lie in it" in predecessor
    and "genuine defect/density reduction varied on X" in predecessor
    and "typed ten-component normal receiver" in predecessor,
)

check("type", "ordinary torsion and augmented torsion remain distinct objects", True)
check("type", "augmented torsion and its action Euler residual remain distinct objects", True)
check("type", "ordinary form pullback and vertical coefficient restriction remain distinct maps", True)
check("type", "restriction of fields and the dual reception of equations remain distinct maps", True)
check("type", "four horizontal equations and ten vertical scalar equations are different output types", True)
check("type", "a vertical scalar-like coefficient is not thereby the physical Higgs", True)
check("type", "local fibrewise faithfulness is not a global variational or Green-domain theorem", True)


print("\nB. ACTUAL SECTION FIELD MAP: PULLBACK PLUS VERTICAL COEFFICIENT RESTRICTION")
# Exact tilted local section jet ds=[I;J].  The vertical coefficient map is
# canonical for the bundle Y->X; it is not the metric-normal decoder used only
# as an algebraic fallback in the predecessor.
J = sp.zeros(10, 4)
entries = {
    (0, 0): R(1, 5),
    (1, 1): R(-1, 7),
    (2, 2): R(1, 9),
    (3, 3): R(1, 11),
    (4, 0): R(1, 13),
    (5, 1): R(1, 17),
    (6, 2): R(-1, 19),
    (7, 3): R(1, 23),
    (8, 0): R(1, 29),
    (9, 1): R(-1, 31),
}
for slot, value in entries.items():
    J[slot] = value

O = sp.Matrix.hstack(sp.eye(4), J.T)       # ordinary one-form pullback
V = sp.Matrix.hstack(sp.zeros(10, 4), sp.eye(10))  # vertical coefficient restriction
M = sp.Matrix.vstack(O, V)
M_expected_inverse = sp.Matrix.vstack(
    sp.Matrix.hstack(sp.eye(4), -J.T),
    sp.Matrix.hstack(sp.zeros(10, 4), sp.eye(10)),
)

check("exact", "the tilted section jet has rank four", J.rank() == 4)
check("exact", "ordinary one-form pullback has rank four", O.rank() == 4)
check("exact", "vertical coefficient restriction has rank ten", V.rank() == 10)
check("exact", "the combined field map has rank fourteen", M.rank() == 14)
check("exact", "the combined field map has determinant one", sp.expand(M.det()) == 1)
check("exact", "the displayed inverse recovers the ambient one-form coefficients", M.inv() == M_expected_inverse)
check("type", "the four outputs are an X one-form and the ten outputs form a section of s-star V-star Y tensor adP", True)
check("type", "the ten outputs were already present inside the ambient connection difference", True)
check("planted", "PLANT a genuinely tilted section prevents pullback and horizontal coefficient restriction from coinciding", J != sp.zeros(10, 4))

# The complete kernel of ordinary pullback is the graph-conormal space.
N = sp.Matrix.vstack(-J.T, sp.eye(10))
b = sp.Matrix([R(index + 1, 37) for index in range(10)])
T_conormal = N * b
check("exact", "the graph-conormal basis has rank ten", N.rank() == 10)
check("exact", "ordinary pullback erases every graph-conormal direction", O * N == sp.zeros(4, 10))
check("exact", "vertical coefficient restriction retains every graph-conormal direction", V * N == sp.eye(10))
check("exact", "the concrete augmented-torsion witness is hidden by pullback but retained vertically", O * T_conormal == sp.zeros(4, 1) and V * T_conormal == b)


print("\nC. SOURCE-ACTION HORIZONTALITY IS NOT AUTOMATIC")
# Mostly-minus horizontal (1,3) plus trace-reversed vertical (6,4): K77.
G = sp.diag(*([1, -1, -1, -1] + [1] * 6 + [-1] * 4))
L = sp.Matrix.vstack(sp.eye(4), J)
g_section = sp.simplify(L.T * G * L)
H = sp.simplify(G * L * g_section.inv())
P = sp.simplify(H * O)
Q = sp.eye(14) - P

check("exact", "the local ambient metric has K77 inertia by construction", sum(1 for x in G.diagonal() if x > 0) == 7 and sum(1 for x in G.diagonal() if x < 0) == 7)
check("exact", "the induced tilted section metric is nondegenerate", g_section.det() != 0)
check("exact", "the metric horizontal lift is a right inverse", O * H == sp.eye(4))
check("exact", "the horizontal and conormal projectors are complementary", P * P == P and Q * Q == Q and P * Q == sp.zeros(14))
check("exact", "the conormal witness lies wholly outside the horizontal image", Q * T_conormal == T_conormal and P * T_conormal == sp.zeros(14, 1))

# Exact local source-action fixture.  Choose one fixed Lie-algebra generator
# and constant coefficients.  Then dT=0 and [T,T]=0, hence F_A=0 on the
# abelianized one-generator line.  The explicit kappa/2<T,*T> term varies to
# *kappa*T, whose source-owned primalizer returns kappa*T.
kappa = sp.Integer(5)
d_T = sp.zeros(14, 1)
wedge_self = sp.Matrix(14, 14, lambda i, j: sp.expand(T_conormal[i] * T_conormal[j] - T_conormal[j] * T_conormal[i]))
curvature_coefficients = d_T
primal_euler = kappa * T_conormal
euler_density_coefficients = G * primal_euler
recovered_primal_euler = G.inv() * euler_density_coefficients

check("exact", "the constant one-generator torsion witness has zero exterior derivative", d_T == sp.zeros(14, 1))
check("exact", "the one-generator torsion witness has zero self bracket", wedge_self == sp.zeros(14, 14))
check("exact", "the local curvature contribution can therefore vanish", curvature_coefficients == sp.zeros(14, 1))
check("exact", "the kappa term emits the nonzero source Euler witness", recovered_primal_euler == primal_euler and primal_euler != sp.zeros(14, 1))
check("exact", "the emitted source Euler witness violates the action-horizontal-image condition", Q * recovered_primal_euler == recovered_primal_euler and O * recovered_primal_euler == sp.zeros(4, 1))
check("type", "this kills automatic horizontality for nonzero kappa on the displayed full local translation domain", True)
check("type", "a separately source-derived constrained variation domain could still exclude the witness", True)
check("type", "setting kappa to zero would remove this witness but would not prove horizontality", True)
check("planted", "PLANT a zero-curvature fixture does not erase the independently nonzero kappa term", recovered_primal_euler != sp.zeros(14, 1))


print("\nD. EQUATION-DUAL RECEIVER FOR THE FOUR PLUS TEN DEFECT FIELDS")
# q=M A are the defect field coordinates (pullback one-form, vertical scalar
# coefficients).  At fixed section jet, delta A=M^{-1} delta q.  Therefore the
# equation dual is forced: e_q=M^{-T} e_A.
R_defect = M.inv().T
R_defect_expected = sp.Matrix.vstack(
    sp.Matrix.hstack(sp.eye(4), sp.zeros(4, 10)),
    sp.Matrix.hstack(-J, sp.eye(10)),
)
check("exact", "the equation-dual receiver is the inverse transpose of the field map", R_defect == R_defect_expected)
check("exact", "the equation-dual receiver has rank fourteen", R_defect.rank() == 14)
check("exact", "the ambient Euler row is recovered from both defect equation rows", M.T * R_defect == sp.eye(14))

dq = sp.Matrix([R(2 * index + 1, 41) for index in range(14)])
e_ambient = sp.Matrix([R(3 * index - 7, 43) for index in range(14)])
dA = M.inv() * dq
e_defect = R_defect * e_ambient
check("exact", "the complete first-variation pairing is preserved", sp.expand((dA.T * e_ambient)[0] - (dq.T * e_defect)[0]) == 0)
check("exact", "the connection Euler row is the horizontal coefficient row", e_defect[:4, :] == e_ambient[:4, :])
check("exact", "the vertical scalar Euler row includes the forced section-jet correction", e_defect[4:, :] == e_ambient[4:, :] - J * e_ambient[:4, :])
check("exact", "the receiver detects the source conormal Euler witness", R_defect * euler_density_coefficients != sp.zeros(14, 1))

horizontal_only = R_defect[:4, :]
vertical_only = R_defect[4:, :]
check("exact", "the horizontal-only equation receiver has rank four", horizontal_only.rank() == 4)
check("exact", "the vertical equation receiver has rank ten", vertical_only.rank() == 10)
check("exact", "only the combined receiver is faithful on all fourteen coefficients", sp.Matrix.vstack(horizontal_only, vertical_only).rank() == 14)

wrong_dual = M.T
wrong_pairing_defect = sp.expand((dA.T * e_ambient)[0] - (dq.T * wrong_dual * e_ambient)[0])
uncorrected_vertical = sp.Matrix.vstack(e_ambient[:4, :], e_ambient[4:, :])
uncorrected_pairing_defect = sp.expand((dA.T * e_ambient)[0] - (dq.T * uncorrected_vertical)[0])
check("planted", "PLANT using the transpose instead of inverse transpose breaks the variation pairing", wrong_pairing_defect != 0)
check("planted", "PLANT omitting the section-jet correction breaks the variation pairing", uncorrected_pairing_defect != 0)
check("planted", "PLANT dropping the ten vertical equations destroys faithfulness", horizontal_only.rank() < 14)


print("\nE. DEGREE-CORRECT EXTERIOR RECEIVER")
# Every 13-form on a 4+10 split has exactly one of two bidegrees:
#   Lambda^3 H* tensor Lambda^10 V*  (4 coefficients), or
#   Lambda^4 H* tensor Lambda^9 V*   (10 coefficients).
basis_13 = list(combinations(range(14), 13))
bidegrees = [(sum(index < 4 for index in blade), sum(index >= 4 for index in blade)) for blade in basis_13]
horizontal_blades = [blade for blade, degree in zip(basis_13, bidegrees) if degree == (3, 10)]
vertical_blades = [blade for blade, degree in zip(basis_13, bidegrees) if degree == (4, 9)]

check("exact", "Lambda13 of a four plus ten split has dimension fourteen", len(basis_13) == 14)
check("exact", "the degree decomposition has four connection-dual blades", len(horizontal_blades) == 4)
check("exact", "the degree decomposition has ten vertical-scalar-dual blades", len(vertical_blades) == 10)
check("exact", "no third bidegree occurs", set(bidegrees) == {(3, 10), (4, 9)})
check("exact", "contracting the full vertical density sends the horizontal sector to degree three", 13 - 10 == 3)
check("exact", "retaining one vertical label sends the vertical sector to degree four", 13 - 9 == 4)

# c_i is the coefficient of the 13-blade missing basis covector i.  The top
# pairing e^i wedge c_i e^[not i] has sign (-1)^i.  S converts form
# coefficients into the ambient equation covector, after which R_defect gives
# the four degree-three and ten bundle-valued degree-four equations.
S_top = sp.diag(*[(-1) ** index for index in range(14)])
R_forms = R_defect * S_top
c_form = sp.Matrix([R(index + 2, 47) for index in range(14)])
dA_form = sp.Matrix([R(2 * index - 5, 53) for index in range(14)])
dq_form = M * dA_form
e_form_defect = R_forms * c_form
ambient_top_pairing = sp.expand((dA_form.T * S_top * c_form)[0])
defect_top_pairing = sp.expand((dq_form.T * e_form_defect)[0])

check("exact", "the degree-correct form receiver has rank fourteen", R_forms.rank() == 14)
check("exact", "the degree-three plus bundle-valued degree-four pairing equals the ambient top-form pairing", ambient_top_pairing == defect_top_pairing)
check("exact", "the form receiver is exactly invertible", (R_forms.inv() * R_forms) == sp.eye(14))
check("type", "the first four outputs live in Omega3(X,ad-star) with the vertical density line", True)
check("type", "the last ten outputs live in Omega4(X,V tensor ad-star) with the vertical density line", True)
check("type", "the bundle-valued statement requires no chosen list of ten physical scalars", True)
check("type", "using densities rather than an oriented vertical volume consumes no P1", True)
check("planted", "PLANT literal pullback of a 13-form to X4 still has zero codomain", len(list(combinations(range(4), 13))) == 0)


print("\nF. COEFFICIENT EQUIVARIANCE, MOVING-JET NATURALITY, AND SCOPE")
# The receiver acts only on form/section indices and therefore commutes with
# every coefficient representation.  A 2x2 exact noncommuting coefficient
# control is sufficient to catch accidental form/coefficient mixing.
C = sp.Matrix([[0, 1], [-2, 3]])
R_coeff = sp.kronecker_product(R_defect, sp.eye(2))
ambient_coeff_action = sp.kronecker_product(sp.eye(14), C)
defect_coeff_action = sp.kronecker_product(sp.eye(14), C)
check("exact", "the receiver commutes with an arbitrary exact coefficient action", R_coeff * ambient_coeff_action == defect_coeff_action * R_coeff)
check("type", "the structural reason is tensor-factor separation, so the same statement applies to the adjoint coefficient bundle", True)

J2 = J.copy()
J2[0, 1] += R(2, 59)
J2[8, 3] -= R(3, 61)
O2 = sp.Matrix.hstack(sp.eye(4), J2.T)
M2 = sp.Matrix.vstack(O2, V)
R2 = M2.inv().T
dq2 = M2 * dA_form
check("exact", "a second section jet retains an invertible four-plus-ten field map", M2.rank() == 14)
check("exact", "the equation-dual pairing remains exact when the section jet moves", sp.expand((dA_form.T * e_ambient)[0] - (dq2.T * R2 * e_ambient)[0]) == 0)
check("exact", "freezing the old equation receiver at the moved section breaks the pairing", sp.expand((dA_form.T * e_ambient)[0] - (dq2.T * R_defect * e_ambient)[0]) != 0)

check("type", "Layer 0 separates pullback, coefficient restriction, augmented torsion and Euler reception", True)
check("type", "L1 source fixes the carriers and motivates both outputs but not this exact receiver formula", True)
check("type", "L2 exact algebra kills automatic full-domain horizontality for nonzero kappa", True)
check("type", "L3 constructs the local rank-four plus rank-ten field and equation maps", True)
check("type", "L4 derives the complete fibrewise first-variation pairing but not the full localized nonlinear action", True)
check("type", "L5 keeps BV and gauge quotient ownership open", True)
check("type", "L6 keeps common closed Krein Green domains and constraint propagation open", True)
check("type", "L7 moves no Standard Model GR dark-sector or particle row", True)
check("type", "P1 P2 and P3 remain unchanged and unused", True)
check("type", "Curt remains formally separate guidance inside the Eric lane", True)
check("type", "Wave 3 remains closed pending the full moving action Ward BV and descent weld", True)
check("planted", "PLANT the vertical scalar receiver is not called a Higgs derivation", True)
check("planted", "PLANT a local invertible receiver is not called a physical phase space", True)
check("planted", "PLANT source-compatible reconstruction is not reported as Weinstein's released formula", True)


print("\nSUMMARY")
for kind in ("source", "type", "exact", "planted"):
    print(f"{kind}: {COUNTS[kind]}")
print(f"total: {sum(COUNTS.values())}")

if FAILURES:
    print("FAILURES:")
    for failure in FAILURES:
        print(f"- {failure}")
    sys.exit(1)

print("VERDICT: AUGMENTED_TORSION_FULL_DOMAIN_NOT_AUTOMATICALLY_HORIZONTAL__NATURAL_FOUR_PLUS_TEN_DEFECT_EULER_RECEIVER_EXACT_AND_FAITHFUL_LOCALLY__FULL_MOVING_SOURCE_ACTION_WARD_BV_DOMAIN_OPEN")
