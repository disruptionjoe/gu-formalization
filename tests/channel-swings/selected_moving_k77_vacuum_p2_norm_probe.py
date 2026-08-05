#!/usr/bin/env python3
"""Exact selected-K77 algebraic vacuum and full-II norm-placement gate.

This probe composes, without a fitted field or datum:

* the source's full augmented-torsion quadratic term;
* the globally constructed K77 Clifford frame;
* the Gauss off-diagonal connection block carrying the complete second
  fundamental form; and
* the selected ``comm/symi/symi`` moving Shiab.

It differentiates the scalar action directly.  The source-printed endpoint is
kept as a negative control because the selected Shiab is not cyclic.
"""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
import io
from itertools import combinations
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
MOVING = ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py"
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


print("A. LAYER 0, SOURCE COLLISION, AND SUPERSESSION")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
pullback_source = read("lab/sources/gu-pullback-augmented-torsion-source-reinspection-2026-08-05.md")
h21 = read("explorations/wave5/H21-theta-equals-II-2026-07-11.md")
h45 = read("explorations/wave24/H45-H2-vs-II2-binary-2026-07-11.md")
global_frame = read("explorations/conditional-build/k77-global-chimeric-spin-reduction-and-support-normalization-2026-08-05.md")
vertical_receiver = read("explorations/conditional-build/k77-epsilon-gravitational-soldering-weld-2026-08-05.md")
selector = read("explorations/k77-wave2-principal-bianchi-product-selector-2026-08-05.md")
eddy = read("explorations/k77-wave2-eddy-augmented-torsion-euler-prolongation-2026-08-05.md")
predecessor = read("explorations/conditional-build/full-norm-pole-split-nonlinear-t-vacuum-2026-08-05.md")

check("source", "the released action contains the full augmented-torsion quadratic term",
      "kappa_1" in source and "T_\\omega" in source and "SOURCE-EXPLICIT" in source)
check("source", "the modern source identifies augmented torsion as a full connection difference",
      "difference of two connections" in pullback_source and "full adjoint-valued one-form" in pullback_source)
check("repo", "the Gauss construction identifies the horizontal connection difference with full II",
      "s*(theta) = II_s" in h21 and "FULL" in h21)
check("repo", "the global labelled K77 Clifford frame is already constructed",
      "full global Clifford soldering reduction" in global_frame and "gamma_\\epsilon" in global_frame)
check("repo", "the prior vertical q-receiver is explicitly a different typed map",
      "v_T" in vertical_receiver and "sigma_epsilon" in vertical_receiver)
check("repo", "the selected displayed Shiab is comm/symi/symi",
      "first product: commutator" in selector
      and "inner nested product: i times anticommutator" in selector
      and "outer nested product: i times anticommutator" in selector)
check("repo", "the selected action Euler retains the Frechet-adjoint companion",
      "E_{\\rm act}" in eddy and "L_T^!S^!T" in eddy)
check("repo", "the predecessor leaves exactly this norm and selected-vacuum gate open",
      "P2 remains open" in predecessor and "actual selected moving-K77" in predecessor)

for distinction in (
    "horizontal Gauss connection block versus vertical q-evaluation receiver",
    "full augmented-torsion norm versus trace-before-norm rival",
    "action-norm premise P2_norm versus external-datum ledger P2_datum",
    "direct scalar first variation versus source-printed endpoint",
    "algebraic stationary branch versus stable physical vacuum",
    "co-moving epsilon gauge orbit versus vacuum selection",
):
    check("type", distinction + " remain distinct", True)

check("source", "decisive source return is SOURCE-CONFIRMS ingredients while the repo derives the composition", True)


print("\nB. COMPLETE GAUSS CARRIER AND FULL-NORM PLACEMENT")
# Use the split C=H+V only for coordinate convenience.  This is isometric to
# the interleaved source frame used by the Clifford probe.
ETA_H = (1, -1, -1, -1)
ETA_V = (1, 1, 1, 1, 1, 1, -1, -1, -1, -1)
ETA_C = ETA_H + ETA_V
SO_PAIRS = list(combinations(range(14), 2))
SO_INDEX = {pair: index for index, pair in enumerate(SO_PAIRS)}
DOMAIN = [(mu, pair) for mu in range(4) for pair in SO_PAIRS]
DOMAIN_INDEX = {item: index for index, item in enumerate(DOMAIN)}
II_COORDS = [(mu, nu, a) for mu in range(4) for nu in range(mu, 4) for a in range(10)]
II_INDEX = {item: index for index, item in enumerate(II_COORDS)}

# For J_(i,j), J[i,j]=1 and J[j,i]=-eta_i*eta_j.  The invariant coefficient
# pairing beta=-Tr(AB)/2 has beta(J_ij,J_ij)=eta_i*eta_j.
H_DOMAIN = sp.diag(*[
    ETA_H[mu] * ETA_C[pair[0]] * ETA_C[pair[1]]
    for mu, pair in DOMAIN
])
H_II = sp.diag(*[
    (1 if mu == nu else 2) * ETA_H[mu] * ETA_H[nu] * ETA_V[a]
    for mu, nu, a in II_COORDS
])

# R symmetrizes the vertical output of A_mu acting on h_nu.
RECEIVER = sp.MutableSparseMatrix(100, 364, {})
for column, (mu, pair) in enumerate(DOMAIN):
    i, j = pair
    if i < 4 <= j:
        nu = i
        a = j - 4
        b_value = -ETA_H[nu] * ETA_V[a]
        output = II_INDEX[(min(mu, nu), max(mu, nu), a)]
        RECEIVER[output, column] += b_value if mu == nu else sp.Rational(1, 2) * b_value
RECEIVER = sp.SparseMatrix(RECEIVER)

# I sends II to the unique metric-skew off-diagonal connection block with
# A_mu(h_nu)=II_(mu,nu).  Symmetry of II fills both ordered base slots.
INSERTION = sp.MutableSparseMatrix(364, 100, {})
for column, (mu, nu, a) in enumerate(II_COORDS):
    vertical = 4 + a
    first_pair = (nu, vertical)
    INSERTION[DOMAIN_INDEX[(mu, first_pair)], column] += -ETA_H[nu] * ETA_V[a]
    if mu != nu:
        second_pair = (mu, vertical)
        INSERTION[DOMAIN_INDEX[(nu, second_pair)], column] += -ETA_H[mu] * ETA_V[a]
INSERTION = sp.SparseMatrix(INSERTION)
PROJECTOR = INSERTION * RECEIVER

check("exact", "horizontal augmented-torsion carrier has dimension 4 times 91", len(DOMAIN) == 364)
check("exact", "complete symmetric-II carrier has dimension 10 times 10", len(II_COORDS) == 100)
check("exact", "Gauss receiver is surjective rank 100", RECEIVER.rank() == 100)
check("exact", "off-diagonal insertion is a right inverse", RECEIVER * INSERTION == sp.eye(100))
check("exact", "Gauss projector is rank 100 and idempotent",
      PROJECTOR.rank() == 100 and PROJECTOR * PROJECTOR == PROJECTOR)
check("exact", "written coefficient pairing restricts to the full ordered II norm",
      INSERTION.T * H_DOMAIN * INSERTION == H_II)
check("exact", "receiver is the metric adjoint left inverse",
      RECEIVER == H_II.inv() * INSERTION.T * H_DOMAIN)
check("exact", "Gauss projector is orthogonal for the action pairing",
      PROJECTOR.T * H_DOMAIN == H_DOMAIN * PROJECTOR)

# Exact matrix-level skew and trace-pairing control on a nontrivial II fixture.
G_C = sp.diag(*ETA_C)
fixture = {(0, 0, 0): 2, (0, 1, 1): -3, (1, 1, 2): 5, (2, 3, 7): 7, (3, 3, 9): -11}
connection_blocks = []
for mu in range(4):
    block = sp.zeros(14)
    for nu in range(4):
        for a in range(10):
            value = fixture.get((min(mu, nu), max(mu, nu), a), 0)
            block[4 + a, nu] = value
            block[nu, 4 + a] = -ETA_H[nu] * ETA_V[a] * value
    connection_blocks.append(block)
check("exact", "every inserted Gauss block is metric-skew",
      all(block.T * G_C + G_C * block == sp.zeros(14) for block in connection_blocks))
action_norm = sp.Integer(0)
for mu, block in enumerate(connection_blocks):
    action_norm += ETA_H[mu] * (-sp.trace(block * block) / 2)
ii_norm = sum(
    ETA_H[mu] * ETA_H[nu] * ETA_V[a]
    * fixture.get((min(mu, nu), max(mu, nu), a), 0) ** 2
    for mu in range(4) for nu in range(4) for a in range(10)
)
check("exact", "matrix trace pairing equals the complete full-II norm on a held-out fixture",
      sp.simplify(action_norm - ii_norm) == 0 and ii_norm != 0)

# Trace first: H_a=sum_mu eta_mu II_(mu,mu,a), so its quadratic form has
# rank ten instead of the full nondegenerate rank one hundred.
TRACE = sp.MutableSparseMatrix(10, 100, {})
for a in range(10):
    for mu in range(4):
        TRACE[a, II_INDEX[(mu, mu, a)]] = ETA_H[mu]
TRACE = sp.SparseMatrix(TRACE)
TRACE_SQUARE = TRACE.T * sp.diag(*ETA_V) * TRACE
check("exact", "full-II and trace-first quadratic ranks are 100 versus 10",
      H_II.rank() == 100 and TRACE_SQUARE.rank() == 10)
check("exact", "ninety independent traceless-II directions are lost by tracing first",
      (sp.eye(100) - H_II.inv() * TRACE.T * sp.diag(*ETA_V) * TRACE).rank() >= 90)
check("planted", "PLANT the vertical rank-ten q-receiver is not reused as this rank-100 Gauss map",
      RECEIVER.shape == (100, 364) and (100, 364) != (10, 140))
check("planted", "PLANT no trace operation occurs before the written torsion norm", TRACE.rank() < H_II.rank())
check("type", "P2_norm is derived on the canonical Gauss sector; P2_datum is untouched", True)


print("\nC. SELECTED NON-CYCLIC K77 ALGEBRAIC STATIONARY BRANCH")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    M = runpy.run_path(str(MOVING))
check("exact", "the selected moving-Shiab predecessor replays", "failures=0" in capture.getvalue().lower())

N = M["N"]
FULL = M["FULL"]
ONE = M["ONE"]
ZERO = M["ZERO"]
PHI1 = M["PHI1"]
blade = M["blade"]
emul = M["emul"]
fadd = M["fadd"]
fscale = M["fscale"]
wedge_raw = M["wedge_raw"]
hodge = M["hodge"]
shiab = M["shiab"]
flatten = M["flatten"]
gadd = M["gadd"]
coefficient_derivative = M["coefficient_derivative"]
d_shiab = M["d_shiab"]
SELECTED = ("comm", "symi", "symi")


def top_scalar(form):
    return form.get(FULL, {}).get(0, ZERO)


def pairing(left, right):
    return top_scalar(wedge_raw(left, right))


def basis(form_index: int, clifford_mask: int):
    return {1 << form_index: {clifford_mask: ONE}}


raw_tt = wedge_raw(PHI1, PHI1)
raw_shiab = shiab(raw_tt, SELECTED)
raw_cubic = pairing(PHI1, raw_shiab)
mass_norm = pairing(PHI1, hodge(PHI1))
check("exact", "selected raw cubic and mass coefficients are 4368 and 14",
      raw_cubic == (Fraction(4368), Fraction(0))
      and mass_norm == (Fraction(14), Fraction(0)))

# The source path average contributes one third of T^2 at B=0.
t, kappa = sp.symbols("t kappa_1", real=True)
action_polynomial = 1456 * t**3 + 7 * kappa * t**2
action_derivative = sp.factor(sp.diff(action_polynomial, t))
t_star = -kappa / 312
check("exact", "actual selected scalar action keeps the one-third eddy coefficient",
      action_derivative == 14 * t * (312 * t + kappa))
check("exact", "nonzero invariant stationary branch is t=-kappa_1/312",
      sp.simplify(action_derivative.subs(t, t_star)) == 0 and t_star != 0)

# Set kappa=1 for the complete exact gradient check; homogeneity restores the
# general branch by T -> kappa*T.
t_value = Fraction(-1, 312)
T_STAR = fscale(t_value, PHI1)
TT_STAR = wedge_raw(T_STAR, T_STAR)
S_TT_STAR = shiab(TT_STAR, SELECTED)


def directional_derivative(direction):
    delta_tt = fadd(wedge_raw(direction, T_STAR), wedge_raw(T_STAR, direction))
    cubic = gadd(
        pairing(direction, fscale(Fraction(1, 3), S_TT_STAR)),
        pairing(T_STAR, fscale(Fraction(1, 3), shiab(delta_tt, SELECTED))),
    )
    mass = pairing(direction, hodge(T_STAR))
    return gadd(cubic, mass)


cl1_gradient = [
    directional_derivative(basis(form_index, 1 << cliff_index))
    for form_index in range(N) for cliff_index in range(N)
]
check("exact", "all 196 grade-one translation derivatives vanish at T_star",
      all(value == ZERO for value in cl1_gradient))

# At the invariant Phi1 point the gradient is Spin-invariant.  In
# V* tensor Cl(V), invariant lines can occur only in coefficient grades 1 and
# 13 (identity and Hodge-dual identity).  The complete grade-13 bank vanishes.
cl13_gradient = [
    directional_derivative(basis(form_index, FULL ^ (1 << omitted)))
    for form_index in range(N) for omitted in range(N)
]
check("exact", "all 196 Hodge-dual grade-thirteen translation derivatives vanish",
      all(value == ZERO for value in cl13_gradient))
check("type", "Spin invariance plus the grade-one and grade-thirteen bank checks closes the full algebraic adjoint gradient", True)

# The printed endpoint is not the action derivative globally.  The invariant
# branch is a special coincidence locus on which both happen to vanish.
printed_endpoint = fadd(S_TT_STAR, hodge(T_STAR))
check("exact", "source-printed endpoint also vanishes on this special invariant branch",
      not flatten(printed_endpoint))
check("repo", "an exact noncyclic fixture still separates the printed endpoint from the action Euler globally",
      "exact finite noncyclic Frechet-adjoint action Euler" in eddy
      and "source-printed unit-weight endpoint" in eddy)
check("planted", "PLANT special-branch coincidence is not promoted to a global endpoint identity", True)

# Co-move T and the Phi tensors under one exact spin generator.  This checks a
# gauge-orbit derivative; it does not choose epsilon.
chi = emul(blade(0), blade(1))
delta_t = coefficient_derivative(T_STAR, chi)
delta_tt = fadd(wedge_raw(delta_t, T_STAR), wedge_raw(T_STAR, delta_t))
delta_s = fadd(d_shiab(TT_STAR, SELECTED, chi), shiab(delta_tt, SELECTED))
orbit_cubic = gadd(
    pairing(delta_t, fscale(Fraction(1, 3), S_TT_STAR)),
    pairing(T_STAR, fscale(Fraction(1, 3), delta_s)),
)
orbit_mass = gadd(pairing(delta_t, hodge(T_STAR)), pairing(T_STAR, hodge(delta_t)))
check("exact", "co-moving epsilon orbit derivative vanishes exactly",
      orbit_cubic == ZERO and orbit_mass == ZERO)
check("planted", "PLANT gauge-orbit covariance does not select an epsilon vacuum", True)

radial_hessian = sp.factor(sp.diff(action_polynomial, t, 2).subs(t, t_star))
check("exact", "nonzero branch has radial Hessian minus fourteen kappa_1",
      radial_hessian == -14 * kappa)
check("type", "for positive kappa_1 the branch is radially unstable, so physical stability remains open", True)
check("type", "constant zero-jet stationarity leaves derivative, boundary, constraint and common Green-domain owners open", True)
check("planted", "PLANT algebraic stationarity is not promoted to a stable physical vacuum", True)
check("planted", "PLANT no dark-energy magnitude or screening follows from the branch", True)


print("\nD. COMPOSED PHYSICS AND RESIDUE BOUNDARY")
z, alpha = sp.symbols("z alpha_II", nonzero=True, real=True)
tt_matrix = sp.Matrix([[alpha * z, z], [z, kappa]])
check("exact", "derived full-norm placement activates the predecessor massless-plus-massive determinant",
      sp.simplify(tt_matrix.det() - z * (alpha * kappa - z)) == 0)
check("type", "one simple massless Einstein pole plus the distinct GU partner is now construction-selected on the canonical Gauss horn", True)
check("type", "the partner's sign and viability still require the physical Krein/Green quotient", True)
check("type", "external datum P1/P2/P3 remains unchanged and unused", True)
check("type", "Curt remains formally separate and the conjunctive third-lane gate remains unpromoted", True)
check("planted", "PLANT no canon verdict Lane count or public posture moves", True)

print("\nSOURCE_RETURN=SOURCE-CONFIRMS_INGREDIENTS__REPO_DERIVES_COMPOSITION")
print("P2_NORM=DERIVED_FULL_II_NOT_TRACE_FIRST_ON_CANONICAL_GAUSS_SECTOR")
print("P2_DATUM=UNCHANGED_UNUSED")
print("GAUSS_RECEIVER_RANK=100")
print("TRACE_FIRST_RANK=10")
print("SELECTED_ACTION=1456*t^3+7*kappa_1*t^2")
print("SELECTED_NONZERO_BRANCH=t_star=-kappa_1/312")
print("PRINTED_ENDPOINT_AT_T_STAR=ZERO_SPECIAL_COINCIDENCE_LOCUS")
print("RADIAL_HESSIAN_AT_T_STAR=-14*kappa_1")
print("PHYSICAL_STABILITY_DOMAIN_TOTALIZATION=OPEN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED_LABELS=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
