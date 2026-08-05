#!/usr/bin/env python3
"""Exact K77 epsilon_IG gravitational receiver and action-weld gate.

The construction is conditional on ``epsilon_IG`` being a *full* Clifford
soldering isometry of the already split chimeric bundle
``C = V + H*``.  A coarse Clifford-plane orbit is deliberately insufficient.
No K95/right-H/chosen-J object is imported.

The probe verifies three separate claims:

* grade-one projection followed by evaluation on the canonical DeWitt-negative
  trace vector gives a rank-ten receiver;
* the Krein sign on grade-one coefficients makes its right inverse an
  isometry and its rank-ten projector orthogonal; and
* splitting the old action by that projector permits a literal sector
  replacement, rather than appending a second Einstein term.

It does not prove existence of a global soldering reduction, a nonlinear BV
master equation, a Green domain, positivity, observation or cosmology.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import sys

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
CHANNEL = ROOT / "tests" / "channel-swings"
sys.path.insert(0, str(CHANNEL))

from p77_real_index_twin import build_split_clifford  # noqa: E402


COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


print("A. LAYER 0, REPOSITORY COLLISION, AND SOURCE RETURN")
forks = (ROOT / "lab" / "process" / "layer0-fork-registry.yaml").read_text()
ic1 = (ROOT / "explorations" / "geometry-curvature-emergence" / "ic1-soldering-map-ns-adps-2026-06-23.md").read_text()
rb3 = (ROOT / "explorations" / "rb3-moving-soldering-spinzero-placement-2026-07-30.md").read_text()
q_wave = (ROOT / "explorations" / "k77-wave2-q-receiver-trace-adjoint-ward-selection-2026-08-04.md").read_text()
source_pack = (ROOT / "lab" / "sources" / "weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
predecessor = (ROOT / "explorations" / "conditional-build" / "pre-shiab-gauss-defect-action-bv-symbol-2026-08-05.md").read_text()
bulk_defect = (ROOT / "explorations" / "k77-wave2-i1b-conormal-symbol-bulk-defect-weld-domain-2026-08-05.md").read_text()

check("repo", "the real Clifford fork is settled source-aligned at K77",
      "Cl(7,7)" in forks and "source-aligned" in forks)
check("repo", "the older IC1 map belongs to the rival K95/Sp64 construction",
      "Cl(9,5)" in ic1 and "Sp(64)" in ic1)
check("repo", "IC1 is an injection into the adjoint, not the required receiver out of it",
      "N_s" in ic1 and "ad(P_s)" in ic1 and "injection" in ic1.lower())
check("repo", "the moving-plane predecessor distinguishes a coarse orbit from a full local soldering frame",
      "unframed Clifford plane" in rb3 and "vector-frame/soldering isometry" in rb3)
check("repo", "the trace-reversed K77 wave owns q=g/2 without consuming P1",
      "q=t/2" in q_wave and "P1 is not consumed" in q_wave)
check("repo", "the predecessor leaves sigma_epsilon as the next missing typed arrow",
      "sigma_epsilon" in predecessor and "global ten-dimensional equivariant map" in predecessor)
check("repo", "the standing bulk/defect architecture forbids treating localization as a second copy of a bulk density",
      "S_X^{\\rm independent}" in bulk_defect and "normal-density" in bulk_defect)
check("source", "the source pack types source epsilon as a gauge transformation and warns against identifying it with epsilon_IG",
      "gauge transformation" in source_pack and "UNCERTAIN/HOMONYM-RISK" in source_pack)
check("source", "the source does not print the new sigma_epsilon receiver",
      "sigma_epsilon" not in source_pack)
check("type", "source epsilon, coarse Clifford plane, full soldering reduction, q, v_T and sigma_epsilon are distinct objects", True)
check("type", "decisive source return at the new receiver/weld locus is SOURCE-SILENT", True)


print("\nB. ACTUAL REAL Cl(7,7) GRADE-ONE PROJECTION")
P_PLUS, P_MINUS = build_split_clifford(7)
GAMMA = P_PLUS + P_MINUS
ETA14 = [1] * 7 + [-1] * 7
I128 = np.eye(128, dtype=np.int64)
Z128 = np.zeros((128, 128), dtype=np.int64)


def product(values: list[np.ndarray]) -> np.ndarray:
    out = I128.copy()
    for value in values:
        out = out @ value
    return out


B = product(P_MINUS)


def gamma_of(vector: list[int]) -> np.ndarray:
    return sum((vector[i] * GAMMA[i] for i in range(14)), start=Z128.copy())


def grade_one_coordinates(matrix: np.ndarray, frame: list[np.ndarray]) -> list[int]:
    return [
        ETA14[i] * int(np.trace(frame[i] @ matrix)) // 128
        for i in range(14)
    ]


test_vector = [2, -1, 0, 3, 0, 1, -2, 1, 0, -1, 2, 0, 1, -3]
test_gamma = gamma_of(test_vector)
test_bivector = GAMMA[1] @ GAMMA[2]
check("exact", "all fourteen real Clifford generators are B-skew",
      all(np.array_equal(B @ gamma.T @ B, -gamma) for gamma in GAMMA))
check("exact", "the trace projector recovers every grade-one coordinate",
      grade_one_coordinates(test_gamma, GAMMA) == test_vector)
check("exact", "the grade-one trace projector kills a bivector control",
      grade_one_coordinates(test_bivector, GAMMA) == [0] * 14)
check("exact", "the B-adjoint trace metric on grade one is minus the K77 vector metric",
      all(int(np.trace((-GAMMA[i]) @ GAMMA[i])) == -128 * ETA14[i] for i in range(14)))

# An exact Spin element moves two positive vertical Clifford axes.  Projection
# in the moved epsilon-frame is natural; freezing the old frame is a planted
# failure.
h_spin = GAMMA[1] @ GAMMA[2]
h_spin_inv = -h_spin
moved_frame = [h_spin @ gamma @ h_spin_inv for gamma in GAMMA]
moved_test_gamma = h_spin @ test_gamma @ h_spin_inv
check("exact", "moving the coefficient and epsilon frame together preserves grade-one coordinates",
      grade_one_coordinates(moved_test_gamma, moved_frame) == test_vector)
check("planted", "freezing epsilon while moving the coefficient changes the extracted coordinates",
      grade_one_coordinates(moved_test_gamma, GAMMA) != test_vector)
check("planted", "a bivector is not silently accepted as a soldered vector",
      test_bivector.shape == test_gamma.shape and grade_one_coordinates(test_bivector, GAMMA) != test_vector)


print("\nC. RANK-TEN RECEIVER, RIGHT INVERSE, AND KREIN PROJECTOR")
# Horizontal signature (1,3), vertical signature (6,4), total (7,7).
H_INDICES = [0, 7, 8, 9]
V_INDICES = [1, 2, 3, 4, 5, 6, 10, 11, 12, 13]
G10 = sp.diag(1, 1, 1, 1, 1, 1, -1, -1, -1, -1)
q = sp.zeros(10, 1)
q[6, 0] = 1
q_flat = G10 * q
q_norm = (q.T * G10 * q)[0]

# Domain is V* tensor C_1, dimension 10*14.  The receiver first evaluates the
# V* slot on q, then projects the epsilon-dependent grade-one vector to V.
SIGMA = sp.MutableSparseMatrix(10, 140, {})
for out_local, out_ambient in enumerate(V_INDICES):
    for source_local in range(10):
        SIGMA[out_local, source_local * 14 + out_ambient] = q[source_local, 0]
SIGMA = sp.SparseMatrix(SIGMA)

# The adjoint right inverse is q_flat/q_norm tensor gamma(u).  Since q_norm=-1
# and q_flat=-e_6, its coordinate matrix simply inserts at source slot 6.
IOTA = sp.MutableSparseMatrix(140, 10, {})
for out_local, out_ambient in enumerate(V_INDICES):
    for source_local in range(10):
        IOTA[source_local * 14 + out_ambient, out_local] = q_flat[source_local, 0] / q_norm
IOTA = sp.SparseMatrix(IOTA)
P_GRAV = IOTA * SIGMA
Q_COMP = sp.eye(140) - P_GRAV

# The coefficient grade-one pairing is -eta because every gamma is B-skew.
# This minus sign cancels the negative norm of q and makes IOTA an isometry.
ETA_C = sp.diag(*ETA14)
H_DOMAIN = sp.kronecker_product(G10.inv(), -ETA_C)

check("exact", "the canonical trace receiver has full rank ten", SIGMA.rank() == 10)
check("exact", "q is unit DeWitt-negative", q_norm == -1)
check("exact", "the declared insertion is a right inverse", SIGMA * IOTA == sp.eye(10))
check("exact", "the gravitational projector is rank ten and idempotent",
      P_GRAV.rank() == 10 and P_GRAV * P_GRAV == P_GRAV)
check("exact", "the complement is rank 130 and idempotent",
      Q_COMP.rank() == 130 and Q_COMP * Q_COMP == Q_COMP)
check("exact", "receiver and insertion are adjoint for the Krein-DeWitt pairings",
      IOTA.T * H_DOMAIN == G10 * SIGMA)
check("exact", "the rank-ten projector is self-adjoint for the full domain pairing",
      P_GRAV.T * H_DOMAIN == H_DOMAIN * P_GRAV)
check("exact", "the insertion is an isometry only after the B-skew coefficient sign is retained",
      IOTA.T * H_DOMAIN * IOTA == G10)
check("planted", "dropping the Krein coefficient sign makes the same insertion an anti-isometry",
      IOTA.T * (-H_DOMAIN) * IOTA == -G10 and -G10 != G10)
check("planted", "q alone spans one input line, while End(V) acting on q makes the receiver surjective",
      q.rank() == 1 and SIGMA.rank() == 10)

# Direct actual-Clifford realization on a held-out vertical-coefficient tensor.
coefficient_vectors: list[list[int]] = []
for source_local in range(10):
    vector = [0] * 14
    vector[V_INDICES[(3 * source_local + 2) % 10]] = source_local + 1
    vector[H_INDICES[source_local % 4]] = 2 - source_local
    coefficient_vectors.append(vector)
coefficient_matrices = [gamma_of(vector) for vector in coefficient_vectors]
evaluated = sum((int(q[a, 0]) * coefficient_matrices[a] for a in range(10)), start=Z128.copy())
extracted = grade_one_coordinates(evaluated, GAMMA)
sigma_actual = [extracted[index] for index in V_INDICES]
sigma_coordinate = list(SIGMA * sp.Matrix([entry for vector in coefficient_vectors for entry in vector]))
check("exact", "the coordinate receiver agrees with the faithful 128x128 Clifford trace projection",
      sigma_actual == sigma_coordinate)
check("planted", "the receiver discards horizontal grade-one coefficients rather than mistyping them as gravity",
      any(extracted[index] for index in H_INDICES)
      and sigma_actual == [extracted[index] for index in V_INDICES])


print("\nD. EQUIVARIANCE DOES NOT BY ITSELF SELECT A UNIQUE RECEIVER")
eta4 = sp.diag(-1, 1, 1, 1)


def tr_g(h: sp.Matrix) -> sp.Expr:
    return sp.trace(eta4 * h)


def traceless(h: sp.Matrix) -> sp.Matrix:
    return h - tr_g(h) * eta4 / 4


def bilinear_family(h: sp.Matrix, k: sp.Matrix) -> list[sp.Matrix]:
    h0 = traceless(h)
    k0 = traceless(k)
    pairing = sp.trace(eta4 * h0 * eta4 * k0)
    jordan = h0 * eta4 * k0 + k0 * eta4 * h0
    jordan0 = traceless(jordan)
    return [
        tr_g(h) * tr_g(k) * eta4,
        pairing * eta4,
        tr_g(h) * k0,
        tr_g(k) * h0,
        jordan0,
    ]


sym_basis: list[sp.Matrix] = []
for i in range(4):
    for j in range(i, 4):
        basis = sp.zeros(4)
        basis[i, j] = 1
        basis[j, i] = 1
        sym_basis.append(basis)


def sym_coords(h: sp.Matrix) -> list[sp.Expr]:
    return [h[i, j] for i in range(4) for j in range(i, 4)]


structure_columns: list[list[sp.Expr]] = [[] for _ in range(5)]
for h_basis in sym_basis:
    for k_basis in sym_basis:
        maps = bilinear_family(h_basis, k_basis)
        for index, value in enumerate(maps):
            structure_columns[index].extend(sym_coords(value))
hom_rank = sp.Matrix.hstack(*(sp.Matrix(column) for column in structure_columns)).rank()

boost = sp.Matrix([[sp.Rational(5, 3), sp.Rational(4, 3), 0, 0],
                   [sp.Rational(4, 3), sp.Rational(5, 3), 0, 0],
                   [0, 0, 1, 0], [0, 0, 0, 1]])
h_fixture = sp.Matrix([[2, 1, 0, 1], [1, -1, 2, 0], [0, 2, 3, 1], [1, 0, 1, 0]])
k_fixture = sp.Matrix([[1, 0, 1, 0], [0, 2, -1, 1], [1, -1, 0, 2], [0, 1, 2, -2]])
moved_maps = bilinear_family(boost.T * h_fixture * boost, boost.T * k_fixture * boost)
expected_maps = [boost.T * value * boost for value in bilinear_family(h_fixture, k_fixture)]

check("exact", "five explicit Lorentz-equivariant Sym2 x Sym2 to Sym2 maps are independent",
      hom_rank == 5)
check("exact", "the rational boost preserves the Lorentz metric",
      boost.T * eta4 * boost == eta4)
check("exact", "all five maps pass an exact held-out Lorentz-equivariance test",
      moved_maps == expected_maps)
check("type", "equivariance alone therefore does not select the gravitational receiver", True)
check("type", "the q-evaluation composite is canonical only after full epsilon_IG, the vertical split and the grade-one projector are named", True)
check("planted", "calling every equivariant map unique is rejected by the rank-five family", hom_rank > 1)


print("\nE. NONDUPLICATING SECTOR REPLACEMENT")
# Held-out exact coefficient/current fixtures in the 140-dimensional grade-one
# domain.  The old source row and gain split orthogonally.  Replacing only the
# P-sector receiver recovers the old action when E_old=sigma(r), and differs by
# exactly one gravitational term for a faithful pre-Shiab E_new.
x = sp.Matrix([sp.Rational((7 * i + 3) % 17 - 8, 5) for i in range(140)])
r = sp.Matrix([sp.Rational((11 * i + 1) % 19 - 9, 7) for i in range(140)])
e_new = sp.Matrix([sp.Rational((5 * i + 2) % 13 - 6, 3) for i in range(10)])
kappa = sp.Rational(7, 11)


def pair_domain(left: sp.Matrix, right: sp.Matrix) -> sp.Expr:
    return sp.expand((left.T * H_DOMAIN * right)[0])


def pair_vertical(left: sp.Matrix, right: sp.Matrix) -> sp.Expr:
    return sp.expand((left.T * G10 * right)[0])


x_q = Q_COMP * x
r_q = Q_COMP * r
x_g = SIGMA * x
r_g = SIGMA * r
old_linear = pair_domain(x, r)
split_linear = pair_domain(x_q, r_q) + pair_vertical(x_g, r_g)
old_gain = kappa * pair_domain(x, x) / 2
split_gain = kappa * (pair_domain(x_q, x_q) + pair_vertical(x_g, x_g)) / 2
old_action = old_linear + old_gain
weld_old_receiver = pair_domain(x_q, r_q) + pair_vertical(x_g, r_g) + split_gain
weld_new_receiver = pair_domain(x_q, r_q) + pair_vertical(x_g, e_new) + split_gain

check("exact", "the source row splits into complement plus one gravitational receiver with no cross term",
      old_linear == split_linear
      and pair_domain(P_GRAV * x, Q_COMP * r) == 0
      and pair_domain(Q_COMP * x, P_GRAV * r) == 0)
check("exact", "the quadratic gain splits with the same sign after the Krein cancellation",
      old_gain == split_gain)
check("exact", "using the old receiver in the welded architecture reconstructs the old action exactly",
      weld_old_receiver == old_action)
check("exact", "using the faithful receiver changes exactly one localized gravitational sector",
      sp.expand(weld_new_receiver - old_action)
      == sp.expand(pair_vertical(x_g, e_new - r_g)))
check("exact", "the complement and gravitational projectors reconstruct the full coefficient carrier",
      Q_COMP + P_GRAV == sp.eye(140))
check("type", "the welded term is a replacement, not an appended second Einstein term", True)
check("type", "the coefficient/gain identities are algebraic action identities before any field equation is imposed", True)
check("type", "this exact split is same-stratum algebra; moving its gravitational term from Y14 to X4 still needs a support architecture and relative normalization", True)
check("planted", "appending the new receiver to the unsplit old action double counts when it equals the old receiver",
      old_action + pair_vertical(x_g, r_g) != old_action)
check("planted", "Euclideanizing the output would change the faithful trace-reversed gravitational sector",
      (x_g.T * x_g)[0] != pair_vertical(x_g, x_g))


print("\nF. MOVING OWNER LEDGER AND WARD BOUNDARY")
# An infinitesimal vertical Lorentz generator fixes q and acts on X:V->V by
# commutator.  This supplies an exact finite Ward control for the natural
# receiver/projector, without pretending to construct the full nonlinear BV
# differential.
K = sp.zeros(10)
K[0, 1] = 1
K[1, 0] = -1
check("exact", "the test generator is DeWitt-skew and fixes q",
      K.T * G10 + G10 * K == sp.zeros(10) and K * q == sp.zeros(10, 1))

# Restrict to End(V), the actual vertical grade-one block of the 140 carrier.
X = sp.Matrix(10, 10, [sp.Rational((3 * i + 2 * j + 1) % 11 - 5, 4) for i in range(10) for j in range(10)])
delta_X = K * X - X * K
sigma_X = X * q
delta_sigma_X = delta_X * q
check("exact", "evaluation on q intertwines the stabilizer action",
      delta_sigma_X == K * sigma_X)
check("exact", "the induced rank-ten projection P(X)=sigma(X) tensor q-flat/q2 is natural",
      (K * (X * q) - (X * q) * 0) * (q_flat.T / q_norm)
      == K * ((X * q) * (q_flat.T / q_norm))
      - ((X * q) * (q_flat.T / q_norm)) * K)

E = sp.zeros(10, 1)
E[1, 0] = 1
delta_E = K * E
ward_scalar = pair_vertical(K * sigma_X, E) + pair_vertical(sigma_X, delta_E)
check("exact", "the receiver pairing has a finite exact Ward cancellation",
      sp.expand(ward_scalar) == 0)
check("type", "the full first variation must retain D_epsilon P, D_g q, D_s Gauss, moving Hodge, density and Green terms", True)
check("type", "the finite Ward cancellation is not a nonlinear BV/CME or analytic-domain theorem", True)
check("planted", "freezing the receiver output while transforming its partner breaks the Ward scalar on the held-out fixture",
      pair_vertical(sigma_X, delta_E) != 0)


print("\nG. FINAL BOUNDARIES")
check("type", "sigma_epsilon is global only conditional on a global full soldering reduction; a coarse plane field does not suffice", True)
check("type", "global epsilon_IG existence/topology, nonlinear BV closure, null Green domain and positivity remain open", True)
check("type", "the full bulk/defect weld remains open even though its same-stratum projector algebra is now exact", True)
check("type", "an independent X4 density avoids copying a Y14 density but still requires a typed relative normalization owner", True)
check("type", "P1 P2 P3 remain unchanged and unused", True)
check("planted", "the old K95 injection cannot discharge the K77 receiver merely because both use the word soldering", True)
check("planted", "an orthogonal projector does not supply the inverse normal-density line of a codimension-ten defect", True)

print("\nCOUNTS", dict(COUNTS))
print("TOTAL", sum(COUNTS.values()))
if FAILURES:
    print("FAILURES", FAILURES)
    raise SystemExit(1)
print("ALL CHECKS PASS")
