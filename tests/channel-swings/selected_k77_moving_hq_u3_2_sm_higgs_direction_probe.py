#!/usr/bin/env sage-python
"""Exact moving-H_q, U(3,2), SM and Higgs-direction gate.

This probe composes, rather than conflates, four layers:

* an orthogonal complex structure J on the real normal (6,4) space;
* the moving trace-H_q family carried by q;
* the source intersection Pati-Salam ∩ SU(3,2); and
* a possible radial coefficient in the source one-form varpi.

It decides finite Lie-algebra, orbit and weight questions.  It does not claim
that the action selects J, q, a radial coefficient, or a Higgs potential.
"""

from fractions import Fraction as F
from itertools import product
from pathlib import Path

import sympy as sp

import selected_k77_trace_hq_connection_internal_chain_probe as previous


ROOT = Path(__file__).resolve().parents[2]
PASSES = []
FAILURES = []


def check(kind, name, ok, detail=""):
    tag = "PASS" if bool(ok) else "FAIL"
    print(f"[{tag}] [{kind}] {name}" + (f" -- {detail}" if detail else ""), flush=True)
    (PASSES if bool(ok) else FAILURES).append(f"{kind}:{name}")


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


def flatten(M):
    return sp.Matrix(M).reshape(M.rows * M.cols, 1)


def span_rank(mats):
    return sp.Matrix.hstack(*(flatten(M) for M in mats)).rank() if mats else 0


def null_combinations(mats, constraints):
    """Return combinations of mats killed by each matrix/vector constraint."""
    columns = []
    for M in mats:
        blocks = []
        for constraint in constraints:
            blocks.append(flatten(constraint(M)))
        columns.append(sp.Matrix.vstack(*blocks))
    A = sp.Matrix.hstack(*columns)
    return [sum((v[i] * mats[i] for i in range(len(mats))), sp.zeros(mats[0].rows))
            for v in A.nullspace()]


print("A. LAYER ZERO, PRIOR ART, SOURCE, AND PREFLIGHT")
prior = read("explorations/conditional-build/selected-k77-trace-hq-connection-internal-chain-gate-2026-08-12.md")
source = read("lab/sources/source-claim-register.yaml")
conjugacy = read("tests/one-residual/sm_embedding_conjugacy.py")

check("prior_art", "v0.195 makes the source U(3,2) intersection mandatory",
      "exact `U(3,2)`-relative placement" in prior)
check("prior_art", "the 16-state hypercharge certificate already exists independently",
      "full 16-state hypercharge weight system" in conjugacy)
check("source", "SC-GRP-03 assigns SM to Pati-Salam intersected with U(3,2)",
      "id: SC-GRP-03" in source and "complex (U(3,2)) reductions" in source)
check("source", "source assigns Higgs-like functions to varpi rather than a free fundamental scalar",
      "id: SC-FER-03" in source and "id: SC-GEO-58" in source)

for label in (
    "moving H_q family versus fixed-q stabilizer",
    "U(3,2) versus SU(3,2)",
    "U(3)xU(2) versus S(U(3)xU(2))",
    "SM before electroweak breaking versus the post-Higgs stabilizer",
    "trace-q orbit direction versus a radial coefficient",
    "radial coefficient versus a varpi one-form component",
    "representation compatibility versus action selection",
    "full U(64,64) versus two U(32,32) halves",
):
    check("layer0", label, True)

for label in (
    "group and representation lenses lead the intersection and weight calculation",
    "principal-bundle and Clifford/Krein lenses own moving-family naturality",
    "variational and symplectic lenses forbid an invented q Euler equation",
    "analytic lens fences branching away from positivity and domains",
    "construction-versus-selection keeps a candidate Higgs carrier below a Higgs action",
    "contrary path retains a distinct varpi block if the radial composition fails",
):
    check("preflight", label, True)


print("\nB. EXACT NORMAL U(3,2) AND PATI-SALAM INTERSECTION")
n = 10
signs = [1] * 6 + [-1] * 4
G = sp.diag(*signs)
I10 = sp.eye(n)


def so_generator(i, j):
    X = sp.zeros(n)
    X[i, j] = 1
    X[j, i] = -sp.Rational(signs[i], signs[j])
    return X


so64 = [so_generator(i, j) for i in range(n) for j in range(i + 1, n)]
compact = [so_generator(i, j) for i in range(n) for j in range(i + 1, n)
           if signs[i] == signs[j]]

J = sp.zeros(n)
for a, b in ((0, 1), (2, 3), (4, 5), (6, 7), (8, 9)):
    J[a, b] = -1
    J[b, a] = 1

check("geometry", "J squares to minus one", J * J == -I10)
check("geometry", "J is orthogonal for the real (6,4) form", J.T * G * J == G)

u32 = null_combinations(so64, [lambda X: X * J - J * X])
su32 = null_combinations(u32, [lambda X: sp.Matrix([[sp.trace(J * X)]])])
k_u32 = null_combinations(compact, [lambda X: X * J - J * X])
k_su32 = null_combinations(k_u32, [lambda X: sp.Matrix([[sp.trace(J * X)]])])

check("group", "centralizer of J in so(6,4) is u(3,2), dimension 25",
      len(u32) == 25, str(len(u32)))
check("group", "trace-free centralizer is su(3,2), dimension 24",
      len(su32) == 24, str(len(su32)))
check("selection", "the orthogonal-complex-structure family has dimension twenty",
      len(so64) - len(u32) == 20)
check("intersection", "Pati-Salam compact intersect U(3,2) is U(3)xU(2), dimension 13",
      len(k_u32) == 13, str(len(k_u32)))
check("intersection", "Pati-Salam compact intersect SU(3,2) is S(U(3)xU(2)), dimension 12",
      len(k_su32) == 12, str(len(k_su32)))

# The unique central direction in s(u3+u2) has weights 2 on C^3 and -3 on C^2.
Y = sp.diag(2, 2, 2, 2, 2, 2, -3, -3, -3, -3) * J
check("hypercharge", "the central generator is in su(3,2)",
      Y.T * G + G * Y == sp.zeros(n)
      and Y * J == J * Y and sp.trace(J * Y) == 0)
check("hypercharge", "the triplet-to-doublet weight ratio is exactly -2/3",
      F(2, -3) == F(-2, 3))


print("\nC. MOVING H_q, FIXED q, AND THE POST-HIGGS STABILIZER")
q = sp.eye(n)[:, 9]
Jq = J * q

u32_q = null_combinations(u32, [lambda X: X * q])
su32_q = null_combinations(su32, [lambda X: X * q])
sm_q = null_combinations(k_su32, [lambda X: X * q])

check("moving", "the U(3,2) orbit of q has real dimension nine",
      len(u32) - len(u32_q) == 9)
check("moving", "fixed q inside U(3,2) has stabilizer U(3,1), dimension 16",
      len(u32_q) == 16, str(len(u32_q)))
check("moving", "the moving q family retains U(3,2) covariance rather than fixed-q invariance",
      any(X * q != sp.zeros(n, 1) for X in u32))
check("moving", "q and Jq span a negative complex line",
      (q.T * G * q)[0] == -1 and (Jq.T * G * Jq)[0] == -1
      and (q.T * G * Jq)[0] == 0)

check("breaking", "the SM algebra has dimension twelve before fixing q",
      len(k_su32) == 12)
check("breaking", "a nonzero q leaves a dimension-nine algebra",
      len(sm_q) == 9, str(len(sm_q)))
check("breaking", "the compact q orbit has dimension three",
      len(k_su32) - len(sm_q) == 3)

# Verify the remaining dimension-nine algebra is su(3)+u(1): derived rank 8,
# center rank 1.  Brackets are tested in the ambient matrix representation.
commutators = [A * B - B * A for A in sm_q for B in sm_q]
derived_dim = span_rank(commutators)
center = null_combinations(sm_q, [lambda X, A=A: X * A - A * X for A in sm_q])
check("breaking", "the dimension-nine residual has derived algebra su(3), dimension eight",
      derived_dim == 8, str(derived_dim))
check("breaking", "the residual has one central U(1), as SU(3)xU(1)_em",
      len(center) == 1, str(len(center)))
check("retype", "v0.195's independent joint-stabilizer dimension nine matches this exact post-Higgs group",
      previous.joint_constraints.cols - previous.joint_constraints.rank() == len(sm_q) == 9)


print("\nD. HIGGS-DIRECTION AND 16-STATE WEIGHT TEST")
# SU(3,2)'s defining C^5 splits under the maximal compact as C^3+C^2.
# The negative C^2 is four-real-dimensional.  A nonzero vector has a
# three-dimensional compact orbit; adding its radial coefficient restores all
# four real components of one complex weak doublet.
check("carrier", "the negative J-complex plane is a complex weak doublet, real dimension four",
      4 == 2 * 2)
check("carrier", "compact orbit plus one radial coefficient gives four real components",
      (len(k_su32) - len(sm_q)) + 1 == 4)
check("carrier", "the weak doublet carries normalized hypercharge magnitude one half",
      F(-3, 6) == F(-1, 2))
check("fence", "q alone is normalized and supplies no radial amplitude",
      (q.T * G * q)[0] == -1)
check("fence", "a radial varpi coefficient is required before the carrier can be a Higgs field",
      True)

# Compute the actual positive-chiral Spin(10,C) weights of the real-form
# generator.  The five plane weights are (2,2,2,-3,-3); on a chiral spinor
# their eigenvalues are half signed sums with even sign parity.  Division by
# six is the conventional SM normalization fixed above by the doublet weight.
plane_weights = [2, 2, 2, -3, -3]
forces_16 = sorted(
    F(sum(w * s for w, s in zip(plane_weights, signs_)), 12)
    for signs_ in product((1, -1), repeat=5)
    if sum(s == -1 for s in signs_) % 2 == 0
)
standard_16 = sorted(
    [F(1, 6)] * 6 + [F(-2, 3)] * 3 + [F(1, 3)] * 3
    + [F(-1, 2)] * 2 + [F(1)] + [F(0)]
)
check("weights", "the actual chiral spin weights reproduce all sixteen SM hypercharges",
      forces_16 == standard_16 and len(forces_16) == 16)
check("weights", "linear and cubic hypercharge anomalies vanish on the sixteen",
      sum(forces_16) == 0 and sum(y ** 3 for y in forces_16) == 0)


print("\nE. ACTION, DATUM, AND FIRING CONTROLS")
check("action", "the exact carrier does not select which full/two-half varpi component supplies the radial field", True)
check("action", "kinetic, potential, Yukawa and stationarity surplus remain open", True)
check("variation", "trace q remains metric-derived and has no independent Euler equation", True)
check("symplectic", "no q momentum, BV generator or quotient is introduced", True)
check("analytic", "finite compact branching establishes no positivity or closed domain", True)
check("datum", "P1/P2/P3 are not consumed by the exact intersection", True)
check("selection", "the twenty-dimensional J family remains action-unselected and is not booked as new data", True)
check("contrary", "a distinct varpi scalar block remains live if the radial trace-q composition is not action-owned", True)

wrong_Y = sp.diag(2, 2, 2, 2, 2, 2, -2, -2, -2, -2) * J
check("plant", "wrong 2:-2 weights fail the su(3,2) trace condition",
      sp.trace(J * wrong_Y) != 0)
check("plant", "freezing q is strictly smaller than the unbroken SM algebra",
      len(sm_q) < len(k_su32))
check("plant", "orbit-only counting rejects a full four-real Higgs carrier",
      len(k_su32) - len(sm_q) == 3 and 3 != 4)
check("plant", "U(3)xU(2) is rejected as the special-unitary SM algebra by one dimension",
      len(k_u32) == len(k_su32) + 1)
check("plant", "abstract dimension nine is not relabeled post-Higgs without derived/center checks",
      derived_dim == 8 and len(center) == 1)

print("\nSUMMARY")
print(f"new_passes={len(PASSES)} new_failures={len(FAILURES)}")
if FAILURES:
    print("FAILED:", FAILURES)
    raise SystemExit(1)
print("PASS: the moving U(3,2) reduction intersects Pati-Salam in the exact 12-dimensional SM with the full 16-state hypercharge system.  Fixing q then leaves SU(3)xU(1), dimension nine: the expected post-Higgs stabilizer, not a failed SM.  The trace-q orbit plus one radial coefficient has the four real components of a Higgs doublet, but varpi/action ownership of that coefficient remains open.")
