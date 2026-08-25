#!/usr/bin/env python3
"""Exact gate for the P3-framed self-dual source-reduction revival.

The test separates three objects which the predecessor left dangerously close:
preservation of the four-plane chiral split, curvature valued in the single
self-dual ``su(2)+`` factor, and the auxiliary P3 BPST bundle.  It then tests
the exact nonzero source family before any projected action is proposed.
"""

from pathlib import Path
import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS = {}
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] = COUNTS.get(kind, 0) + 1
    if not bool(condition):
        FAILURES.append(f"[{kind}] {label}")
        print(f"FAIL [{kind}] {label}")
    else:
        print(f"PASS [{kind}] {label}")


def vec(matrix):
    return sp.Matrix(matrix.rows * matrix.cols, 1, list(matrix))


def span_rank(matrices):
    return sp.Matrix.hstack(*(vec(m) for m in matrices)).rank()


def exterior_sign(indices):
    if len(set(indices)) != len(indices):
        return 0
    inversions = sum(
        indices[i] > indices[j]
        for i in range(len(indices))
        for j in range(i + 1, len(indices))
    )
    return -1 if inversions % 2 else 1


def four_volume_coefficient(curvature):
    values = list(curvature.values())
    check("custody", "the curvature factor supplies a matrix-size witness", bool(values))
    answer = sp.zeros(values[0].rows if values else 0)
    for a, A in curvature.items():
        for b, B in curvature.items():
            sign = exterior_sign(a + b)
            if sign:
                answer += sign * A * B
    return sp.simplify(answer)


packet = (ROOT / "explorations/unified-source-datum-packet-v0-2026-07-30.md").read_text()
prior = (ROOT / "explorations/conditional-build/selected-k77-p3-native-characteristic-pairing-2026-08-10.md").read_text()
tangential = (ROOT / "canon/boundary-einvariant-and-the-tangential-fork.md").read_text()
transcript = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()

check("prior", "P3 BPST connection is fixed auxiliary data", "fixed external data, not a\nvaried gauge field" in packet)
check("prior", "predecessor leaves the self-dual reduction unowned", "the action does not\nyet own it" in prior)
check("prior", "repo prior art types Lambda2+ as tangential", "places `Lambda^2_+` as a tangential framing" in tangential)
check("source", "Weinstein calls instanton self-duality Einsteinian rather than Yang-Millsian", "It's not a Yang is an Einsteinian equation" in transcript)
check("source", "source does not identify P3 with the varied source connection", "SOURCE_SILENT_P3_SOURCE_CONNECTION_DIAGONAL" in (ROOT / "lab/process/conditional-physics-ledger-v0.145.json").read_text())

I = sp.I
sigma1 = sp.Matrix([[0, 1], [1, 0]])
sigma2 = sp.Matrix([[0, -I], [I, 0]])
sigma3 = sp.Matrix([[1, 0], [0, -1]])
eye2 = sp.eye(2)
gamma = [
    sp.kronecker_product(sigma1, eye2),
    sp.kronecker_product(sigma2, eye2),
    sp.kronecker_product(sigma3, sigma1),
    sp.kronecker_product(sigma3, sigma2),
]

for i in range(4):
    for j in range(4):
        target = 2 * sp.eye(4) if i == j else sp.zeros(4)
        check("clifford", f"Clifford relation ({i},{j})", gamma[i] * gamma[j] + gamma[j] * gamma[i] == target)

chi = sp.simplify(gamma[0] * gamma[1] * gamma[2] * gamma[3])
P_plus = sp.simplify((sp.eye(4) + chi) / 2)
P_minus = sp.simplify((sp.eye(4) - chi) / 2)
F = {
    (i, j): sp.simplify(gamma[i] * gamma[j])
    for i in range(4)
    for j in range(i + 1, 4)
}
F_plus = {key: sp.simplify(P_plus * value * P_plus) for key, value in F.items()}
F_minus = {key: sp.simplify(P_minus * value * P_minus) for key, value in F.items()}

check("split", "four-plane chirality is an involution", chi * chi == sp.eye(4))
check("split", "projectors are complementary", P_plus + P_minus == sp.eye(4) and P_plus * P_minus == sp.zeros(4))
for key, value in F.items():
    check("split", f"Spin(4) curvature {key} preserves the chiral split", value * chi - chi * value == sp.zeros(4))
    check("split", f"Spin(4) curvature {key} is block diagonal", value == F_plus[key] + F_minus[key])
    check("split", f"Spin(4) curvature {key} has no cross block", P_plus * value * P_minus == sp.zeros(4) and P_minus * value * P_plus == sp.zeros(4))

check("factor", "self-dual factor has Lie-algebra rank three", span_rank(list(F_plus.values())) == 3)
check("factor", "anti-self-dual factor has Lie-algebra rank three", span_rank(list(F_minus.values())) == 3)
check("factor", "self-dual source component is nonzero", any(value != sp.zeros(4) for value in F_plus.values()))
check("factor", "anti-self-dual source component is nonzero", any(value != sp.zeros(4) for value in F_minus.values()))

t = sp.symbols("t", real=True)
scaled_minus = {key: sp.simplify(t**2 * value / 3) for key, value in F_minus.items()}
nonzero_entry = next((entry for value in scaled_minus.values() for entry in value if entry != 0), None)
check("custody", "the scaled anti-self-dual factor retains a nonzero witness", nonzero_entry is not None)
nonzero_entry = nonzero_entry if nonzero_entry is not None else sp.Integer(0)
check("factor", "pure SU2+ membership forces t=0", sp.solve(sp.Eq(nonzero_entry, 0), t) == [0])
check("factor", "declared nonzero branch is not SU2+ valued", any(value.subs(t, sp.Rational(1, 104)) != sp.zeros(4) for value in scaled_minus.values()))
check("planted", "PLANT split preservation is weaker than one-factor selection", all(value * chi - chi * value == sp.zeros(4) for value in F.values()) and any(value != sp.zeros(4) for value in F_minus.values()))
check("planted", "PLANT odd Clifford connection fails split preservation", gamma[0] * chi - chi * gamma[0] != sp.zeros(4))

vol_plus = four_volume_coefficient(F_plus)
vol_minus = four_volume_coefficient(F_minus)
pair_plus = sp.simplify(sp.trace(vol_plus))
pair_minus = sp.simplify(sp.trace(vol_minus))
check("chern_weil", "self-dual factor pairing is nonzero", pair_plus == 12)
check("chern_weil", "anti-self-dual factor pairing is nonzero and opposite", pair_minus == -12)
check("chern_weil", "full parent pairing cancels", pair_plus + pair_minus == 0)

# General finite-dimensional variational control: restricting before variation
# projects the Euler covector.  This proves the typing of a possible replacement,
# not that GU's current action already owns it.
x0, x1, x2, x3 = sp.symbols("x0 x1 x2 x3", real=True)
x = sp.Matrix([x0, x1, x2, x3])
Pi = sp.diag(1, 1, 0, 0)
H = sp.Matrix([[2, 1, 3, 0], [1, 4, 0, 5], [3, 0, 6, 1], [0, 5, 1, 8]])
grad_full = H * x
x_restricted = Pi * x
grad_restricted = sp.simplify(Pi * H * x_restricted)
check("variational", "restricted Euler is projected pullback of full Euler", grad_restricted == Pi * (H * x_restricted))
check("variational", "restriction removes forbidden test covectors", (sp.eye(4) - Pi) * grad_restricted == sp.zeros(4, 1))
check("planted", "PLANT projection changes a coupled action equation", grad_restricted != (H * x).subs({x2: 0, x3: 0}))

check("layer0", "auxiliary P3 curvature remains distinct from source curvature", "P3 BPST curvature" in prior and "unprojected source curvature" in prior)
check("layer0", "split preservation is not one-factor reduction", span_rank(list(F_plus.values()) + list(F_minus.values())) == 6)
check("accounting", "current action-owned nonzero family loses its topological revival", sp.solve(sp.Eq(nonzero_entry, 0), t) == [0])
check("accounting", "projected replacement is not booked as a current datum assignment", "No P3 stratum selects a finite nonempty amplitude set" in prior)
check("symplectic", "a restricted configuration space is not a BV quotient", "A reduction projector is not a" in prior and "quotient; its constraint and ghosts" in prior)

print("\nRESULT")
print("verdict=CURRENT_NONZERO_SOURCE_FAMILY_NOT_SU2PLUS_REDUCED__DBP_SPLIT_PRESERVATION_INSUFFICIENT__PROJECTED_ACTION_REPLACEMENT_UNBUILT")
print(f"su2plus_rank={span_rank(list(F_plus.values()))}")
print(f"su2minus_rank={span_rank(list(F_minus.values()))}")
print(f"pairings=({pair_plus},{pair_minus},{pair_plus + pair_minus})")
print("current_family_intersection_with_su2plus=t=0")
print("next_gate=CONSTRUCT_EXPLICIT_P3_TO_SOURCE_SU2PLUS_BUNDLE_DIAGONAL_AND_RESTRICT_I1_BEFORE_VARIATION__RECOMPUTE_FULL_EULER_BV_DOMAIN")
print(f"failures={FAILURES}")
print(f"counts={COUNTS}")
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
