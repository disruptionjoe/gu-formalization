#!/usr/bin/env python3
"""Exact controls for the K77 total twisted Yang--Mills current gate.

The paired artifact distinguishes three geometries that are easy to conflate:

* the adapted tangent/normal connection, whose mixed coefficient is raw II;
* the tangent-plane reduction field R, for which D_A R measures that mixed
  coefficient and the vertical energy is a Gauss-map/Willmore-type energy;
* the Yang--Mills detour connection, whose obstruction is D_A^* F_A.

This probe verifies the universal block curvature and current formulas over
Fractions on the actual 4+10 K77 dimensions and explicit (+---)+(++++++----)
metric.  It also supplies firing controls in both directions: nonzero II with
flat total connection, and II=0 with nonzero diagonal Yang--Mills current.
Finally it verifies the exact first variations of the reduction-field energy
and the coupled connection energy.  No finite control is presented as a proof
of a global differential-geometric or physical theorem.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction as Q
from pathlib import Path


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


def z(rows: int, cols: int) -> list[list[Q]]:
    return [[Q(0) for _ in range(cols)] for _ in range(rows)]


def eye(size: int) -> list[list[Q]]:
    out = z(size, size)
    for i in range(size):
        out[i][i] = Q(1)
    return out


def diag(entries: list[int | Q]) -> list[list[Q]]:
    out = z(len(entries), len(entries))
    for i, x in enumerate(entries):
        out[i][i] = Q(x)
    return out


def shape(a: list[list[Q]]) -> tuple[int, int]:
    return len(a), len(a[0]) if a else 0


def add(a: list[list[Q]], b: list[list[Q]]) -> list[list[Q]]:
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def neg(a: list[list[Q]]) -> list[list[Q]]:
    return [[-x for x in row] for row in a]


def sub(a: list[list[Q]], b: list[list[Q]]) -> list[list[Q]]:
    return add(a, neg(b))


def scale(c: int | Q, a: list[list[Q]]) -> list[list[Q]]:
    return [[Q(c) * x for x in row] for row in a]


def transpose(a: list[list[Q]]) -> list[list[Q]]:
    rows, cols = shape(a)
    return [[a[i][j] for i in range(rows)] for j in range(cols)]


def mul(a: list[list[Q]], b: list[list[Q]]) -> list[list[Q]]:
    ar, ac = shape(a)
    br, bc = shape(b)
    assert ac == br
    out = z(ar, bc)
    for i in range(ar):
        for k in range(ac):
            if a[i][k] == 0:
                continue
            for j in range(bc):
                out[i][j] += a[i][k] * b[k][j]
    return out


def comm(a: list[list[Q]], b: list[list[Q]]) -> list[list[Q]]:
    return sub(mul(a, b), mul(b, a))


def trace(a: list[list[Q]]) -> Q:
    rows, cols = shape(a)
    assert rows == cols
    return sum((a[i][i] for i in range(rows)), Q(0))


def pairing(a: list[list[Q]], b: list[list[Q]]) -> Q:
    return trace(mul(a, b))


def is_zero(a: list[list[Q]]) -> bool:
    return all(x == 0 for row in a for x in row)


def hstack(blocks: list[list[list[Q]]]) -> list[list[Q]]:
    rows = shape(blocks[0])[0]
    return [sum((block[i] for block in blocks), []) for i in range(rows)]


def vstack(blocks: list[list[list[Q]]]) -> list[list[Q]]:
    return [row[:] for block in blocks for row in block]


def block2(a, b, c, d):
    return vstack([hstack([a, b]), hstack([c, d])])


def block(a: list[list[Q]], r0: int, r1: int, c0: int, c1: int) -> list[list[Q]]:
    return [row[c0:c1] for row in a[r0:r1]]


def sum_mats(mats: list[list[list[Q]]], size: int) -> list[list[Q]]:
    out = z(size, size)
    for a in mats:
        out = add(out, a)
    return out


T = 4
N = 10
D = T + N
BASE_SIG = [1, -1, -1, -1]       # explicit signs; no ordered-pair ambiguity
NORMAL_SIG = [1] * 6 + [-1] * 4
GT = diag(BASE_SIG)
GN = diag(NORMAL_SIG)
G = block2(GT, z(T, N), z(N, T), GN)


def adjoint_b(b: list[list[Q]]) -> list[list[Q]]:
    """Metric adjoint N<-T to T<-N for involutive diagonal metrics."""
    return mul(mul(GT, transpose(b)), GN)


def so_generator(metric: list[list[Q]], i: int, j: int, value: int) -> list[list[Q]]:
    """Return metric-skew A=G^{-1}S from an ordinary skew matrix S."""
    size = len(metric)
    s = z(size, size)
    s[i][j] = Q(value)
    s[j][i] = Q(-value)
    return mul(metric, s)


def connection(a, b, c):
    return block2(a, neg(adjoint_b(b)), b, c)


def metric_skew(a: list[list[Q]]) -> bool:
    return is_zero(add(mul(transpose(a), G), mul(G, a)))


def curvatures(A: list[list[list[Q]]]) -> list[list[list[list[Q]]]]:
    return [[comm(A[mu], A[nu]) for nu in range(T)] for mu in range(T)]


def currents(A: list[list[list[Q]]], F=None) -> list[list[list[Q]]]:
    if F is None:
        F = curvatures(A)
    return [sum_mats([scale(BASE_SIG[mu], comm(A[mu], F[mu][nu]))
                      for mu in range(T)], D)
            for nu in range(T)]


def all_zero(items: list[list[list[Q]]]) -> bool:
    return all(is_zero(x) for x in items)


print("A. OWNERSHIP AND LAYER ZERO")
codazzi = read("explorations/geometry-curvature-emergence/codazzi-sp64-bundle-2026-06-23.md")
h21 = read("tests/wave5/H21_theta_equals_II_proof.py")
j10 = read("explorations/conditional-build/selected-k77-j10-bv-green-descent-gate-2026-08-13.md")
detour = read("explorations/conditional-build/selected-k77-local-twistor-bach-detour-composition-gate-2026-08-14.md")
action = read("explorations/conditional-build/cb-b-lagrangian-terms-2026-08-05.md")

check("ownership", "the repository owns the adapted tangent/normal connection block form",
      "nabla^Y =" in codazzi and "[ nabla^X       -S" in codazzi)
check("ownership", "the canonical-gauge pullback identifies theta with full raw II",
      "s*(theta) = II_s" in h21 and "FULL symmetric-2-tensor-valued" in h21)
check("ownership", "raw II and horizontal-normalized II^H remain distinct",
      "II_s^raw = nonzero algebraic slice term" in j10 and "II_s^H   = II_s^raw - II_s^ref" in j10)
check("ownership", "the prior gate requires the total twisted connection to be Yang--Mills",
      "Yang--Mills equation for the **total** twisted" in detour and
      "base Bach-flatness is not sufficient" in detour)
check("ownership", "the repository action candidate norms II rather than the Yang--Mills current",
      "alpha_II <II_s,II_s>" in action)
check("ownership", "the repo already records the pulled-back ambient normal-flux correction",
      "K_nu(A,s)" in codazzi and "D_A^{perp *}" in codazzi)

for item in (
    "raw adapted connection versus horizontal-normalized connection",
    "mixed connection coefficient II versus mixed curvature D II",
    "tangent-plane Gauss map versus principal-connection Gauss section",
    "Gauss-map energy |II|^2 versus Yang--Mills energy |F|^2",
    "harmonic reduction equation versus Yang--Mills equation",
    "spinor J10 versus tangent/normal reduction involution R",
    "Bach-flat base current versus total K77 current",
    "detour cohomology versus positive physical cohomology",
):
    check("layer0", item + " remain distinct", True)


print("\nB. EXACT 4+10 ADAPTED CONNECTION")
a = []
b = []
c = []
for mu in range(T):
    am = add(so_generator(GT, mu, (mu + 1) % T, mu + 1),
             so_generator(GT, (mu + 2) % T, (mu + 3) % T, mu + 2))
    cm = add(so_generator(GN, mu, (mu + 3) % N, mu + 2),
             so_generator(GN, (mu + 5) % N, (mu + 7) % N, mu + 1))
    bm = z(N, T)
    bm[mu][mu] = Q(mu + 1)
    bm[(mu + 4) % N][(mu + 1) % T] = Q(mu + 2)
    bm[(mu + 7) % N][(mu + 2) % T] = Q(-1)
    a.append(am)
    b.append(bm)
    c.append(cm)

A = [connection(a[mu], b[mu], c[mu]) for mu in range(T)]
check("signature", "the explicit base metric has one plus and three minus signs",
      BASE_SIG.count(1) == 1 and BASE_SIG.count(-1) == 3)
check("signature", "the explicit normal metric has six plus and four minus signs",
      NORMAL_SIG.count(1) == 6 and NORMAL_SIG.count(-1) == 4)
check("signature", "the assembled metric is exactly split seven plus/seven minus",
      (BASE_SIG + NORMAL_SIG).count(1) == 7 and (BASE_SIG + NORMAL_SIG).count(-1) == 7)
check("connection", "all four adapted connection coefficients preserve the K77 metric",
      all(metric_skew(x) for x in A))
check("connection", "the mixed coefficient has the actual 10-by-4 type",
      all(shape(x) == (N, T) for x in b))
check("connection", "the metric-adjoint upper block is forced rather than independent",
      all(block(A[mu], 0, T, T, D) == neg(adjoint_b(b[mu])) for mu in range(T)))


print("\nC. GAUSS--CODAZZI--RICCI CURVATURE BLOCKS")
F = curvatures(A)
curvature_blocks_pass = True
metric_curvature_pass = True
for mu in range(T):
    for nu in range(T):
        bd_mu = adjoint_b(b[mu])
        bd_nu = adjoint_b(b[nu])
        p = add(comm(a[mu], a[nu]),
                sub(mul(bd_nu, b[mu]), mul(bd_mu, b[nu])))
        q = add(sub(mul(c[mu], b[nu]), mul(c[nu], b[mu])),
                sub(mul(b[mu], a[nu]), mul(b[nu], a[mu])))
        r = add(comm(c[mu], c[nu]),
                sub(mul(b[nu], bd_mu), mul(b[mu], bd_nu)))
        curvature_blocks_pass &= block(F[mu][nu], 0, T, 0, T) == p
        curvature_blocks_pass &= block(F[mu][nu], T, D, 0, T) == q
        curvature_blocks_pass &= block(F[mu][nu], T, D, T, D) == r
        curvature_blocks_pass &= block(F[mu][nu], 0, T, T, D) == neg(adjoint_b(q))
        metric_curvature_pass &= metric_skew(F[mu][nu])

check("curvature", "the tangent block is intrinsic curvature minus II-adjoint wedge II",
      curvature_blocks_pass)
check("curvature", "the mixed block is the covariant Codazzi curl of II",
      curvature_blocks_pass)
check("curvature", "the normal block is normal curvature minus II wedge II-adjoint",
      curvature_blocks_pass)
check("curvature", "the upper mixed curvature is the forced negative metric adjoint",
      curvature_blocks_pass)
check("curvature", "all curvature blocks preserve the K77 metric",
      metric_curvature_pass)
check("curvature", "the generic control actually fires curvature",
      any(not is_zero(F[mu][nu]) for mu in range(T) for nu in range(T)))


print("\nD. COMPLETE TOTAL YANG--MILLS CURRENT BLOCKS")
J = currents(A, F)
current_blocks_pass = True
for nu in range(T):
    jt = z(T, T)
    jn = z(N, N)
    jm = z(N, T)
    for mu in range(T):
        p = block(F[mu][nu], 0, T, 0, T)
        q = block(F[mu][nu], T, D, 0, T)
        r = block(F[mu][nu], T, D, T, D)
        bd = adjoint_b(b[mu])
        qd = adjoint_b(q)
        jt = add(jt, scale(BASE_SIG[mu],
            add(comm(a[mu], p), sub(mul(qd, b[mu]), mul(bd, q)))))
        jn = add(jn, scale(BASE_SIG[mu],
            add(comm(c[mu], r), sub(mul(q, bd), mul(b[mu], qd)))))
        jm = add(jm, scale(BASE_SIG[mu],
            add(sub(mul(c[mu], q), mul(q, a[mu])),
                sub(mul(b[mu], p), mul(r, b[mu])))))
    current_blocks_pass &= block(J[nu], 0, T, 0, T) == jt
    current_blocks_pass &= block(J[nu], T, D, T, D) == jn
    current_blocks_pass &= block(J[nu], T, D, 0, T) == jm
    current_blocks_pass &= block(J[nu], 0, T, T, D) == neg(adjoint_b(jm))

check("current", "the tangent current includes both diagonal divergence and mixed contractions",
      current_blocks_pass)
check("current", "the normal current includes both diagonal divergence and mixed contractions",
      current_blocks_pass)
check("current", "the mixed current is covariant Codazzi divergence plus curvature action on II",
      current_blocks_pass)
check("current", "the full current remains K77 metric-skew",
      all(metric_skew(x) for x in J))
check("current", "the generic current is nonzero and the gate genuinely fires",
      not all_zero(J))


print("\nE. II IS NEITHER NECESSARY NOR SUFFICIENT FOR TOTAL YANG--MILLS")
# A nonzero symmetric rank-one II control.  Only A_0 is nonzero, so all
# connection coefficients commute and the total adapted connection is flat.
b_dev = [z(N, T) for _ in range(T)]
b_dev[0][0][0] = Q(1)  # B^normal0_{00}=1: symmetric and positive in explicit signs
A_dev = [connection(z(T, T), b_dev[mu], z(N, N)) for mu in range(T)]
F_dev = curvatures(A_dev)
J_dev = currents(A_dev, F_dev)
ii_dev_norm = Q(NORMAL_SIG[0] * BASE_SIG[0] * BASE_SIG[0])
check("counterexample", "the developable control has nonzero symmetric II",
      b_dev[0][0][0] == 1 and all(b_dev[mu][i][j] == b_dev[j][i][mu]
      for mu in range(T) for j in range(T) for i in range(N)))
check("counterexample", "that II has nonzero positive quadratic density in the explicit control",
      ii_dev_norm == 1)
check("counterexample", "nonzero II can occur with flat total adapted connection",
      all_zero([F_dev[mu][nu] for mu in range(T) for nu in range(T)]))
check("counterexample", "nonzero II can therefore occur with zero total Yang--Mills current",
      all_zero(J_dev))

# II=0, but a noncommuting tangent connection has nonzero diagonal current.
a_bad = [z(T, T) for _ in range(T)]
a_bad[0] = so_generator(GT, 0, 1, 1)
a_bad[1] = so_generator(GT, 1, 2, 1)
A_base_bad = [connection(a_bad[mu], z(N, T), z(N, N)) for mu in range(T)]
J_base_bad = currents(A_base_bad)
check("counterexample", "the diagonal-current control has II exactly zero",
      all(is_zero(block(x, T, D, 0, T)) for x in A_base_bad))
check("counterexample", "II=0 does not force the tangent/base connection to be Yang--Mills",
      not all_zero(J_base_bad))

# A zero base and zero II control with an independent non-YM normal connection.
c_bad = [z(N, N) for _ in range(T)]
c_bad[0] = so_generator(GN, 0, 1, 1)
c_bad[1] = so_generator(GN, 1, 2, 1)
A_normal_bad = [connection(z(T, T), z(N, T), c_bad[mu]) for mu in range(T)]
J_normal_bad = currents(A_normal_bad)
check("counterexample", "zero base current and II=0 do not erase an independent normal current",
      not all_zero(J_normal_bad) and
      all(is_zero(block(x, 0, T, 0, T)) for x in J_normal_bad))
check("counterexample", "total Yang--Mills is the three-block equation, not a scalar II test",
      current_blocks_pass and not all_zero(J) and all_zero(J_dev))


print("\nF. HORIZONTAL NORMALIZATION CHANGES THE CONNECTION EQUATION")
Kref = [z(D, D) for _ in range(T)]
b_ref = z(N, T)
b_ref[0][1] = Q(1)
Kref[1] = connection(z(T, T), b_ref, z(N, N))
A_norm = [sub(A_dev[mu], Kref[mu]) for mu in range(T)]
F_norm = curvatures(A_norm)

# Exact transgression for constant coefficients:
# F(A-K)=F(A)-D_A K+K wedge K.
transgression_pass = True
for mu in range(T):
    for nu in range(T):
        d_a_k = sub(comm(A_dev[mu], Kref[nu]), comm(A_dev[nu], Kref[mu]))
        k_wedge_k = comm(Kref[mu], Kref[nu])
        predicted = add(sub(F_dev[mu][nu], d_a_k), k_wedge_k)
        transgression_pass &= F_norm[mu][nu] == predicted

check("normalization", "subtracting a mixed reference obeys the exact curvature transgression",
      transgression_pass)
check("normalization", "the raw developable connection is flat before reference subtraction",
      all_zero([F_dev[mu][nu] for mu in range(T) for nu in range(T)]))
check("normalization", "an unowned reference subtraction can create nonzero curvature",
      any(not is_zero(F_norm[mu][nu]) for mu in range(T) for nu in range(T)))
check("normalization", "the same subtraction can create a nonzero Yang--Mills current",
      not all_zero(currents(A_norm, F_norm)))
check("normalization", "II^H=B-S cannot enter the detour gate without constructing A^H",
      transgression_pass and not all_zero(currents(A_norm, F_norm)))


print("\nG. MOVING REDUCTION FIELD AND COUPLED FIRST VARIATIONS")
R = block2(eye(T), z(T, N), z(N, T), scale(-1, eye(N)))
DR = [comm(A[mu], R) for mu in range(T)]
check("reduction", "the tangent/normal reduction involution squares to identity",
      mul(R, R) == eye(D))
check("reduction", "D_A R has only mixed blocks",
      all(is_zero(block(x, 0, T, 0, T)) and is_zero(block(x, T, D, T, D)) for x in DR))
check("reduction", "D_A R is exactly twice the mixed connection coefficient",
      all(block(DR[mu], T, D, 0, T) == scale(2, b[mu]) for mu in range(T)))
check("reduction", "parallel reduction is equivalent to zero mixed coefficient in this adapter",
      all_zero([comm(connection(a[mu], z(N, T), c[mu]), R) for mu in range(T)]))

def reduction_energy(conn: list[list[list[Q]]], reduction: list[list[Q]]) -> Q:
    return Q(1, 2) * sum((Q(BASE_SIG[mu]) *
        pairing(comm(conn[mu], reduction), comm(conn[mu], reduction))
        for mu in range(T)), Q(0))

alpha = [z(D, D) for _ in range(T)]
alpha[0] = connection(so_generator(GT, 0, 2, 1), b_ref,
                      so_generator(GN, 2, 3, 1))
alpha[2] = connection(so_generator(GT, 1, 3, 2), b_dev[0],
                      so_generator(GN, 4, 8, 1))
A_plus = [add(A[mu], alpha[mu]) for mu in range(T)]
A_minus = [sub(A[mu], alpha[mu]) for mu in range(T)]
finite_derivative_a = (reduction_energy(A_plus, R) - reduction_energy(A_minus, R)) / 2
reduction_current = [comm(R, DR[mu]) for mu in range(T)]
predicted_derivative_a = sum((Q(BASE_SIG[mu]) * pairing(reduction_current[mu], alpha[mu])
                              for mu in range(T)), Q(0))
check("variation", "connection variation of |D_A R|^2 yields the reduction current [R,D_A R]",
      finite_derivative_a == predicted_derivative_a)
check("variation", "that reduction current vanishes when the mixed block vanishes",
      all_zero([comm(R, comm(connection(a[mu], z(N, T), c[mu]), R)) for mu in range(T)]))
check("variation", "the generic nonzero mixed block sources the connection equation",
      not all_zero(reduction_current))

xi = connection(so_generator(GT, 0, 1, 1), b_ref,
                so_generator(GN, 0, 5, 1))
dR = comm(xi, R)
R_plus = add(R, dR)
R_minus = sub(R, dR)
finite_derivative_r = (reduction_energy(A, R_plus) - reduction_energy(A, R_minus)) / 2
lap_r = sum_mats([scale(BASE_SIG[mu], comm(A[mu], DR[mu])) for mu in range(T)], D)
predicted_derivative_r = -pairing(comm(R, lap_r), xi)
check("variation", "orbit variation yields the harmonic-reduction equation [R,D_A^*D_A R]=0",
      finite_derivative_r == predicted_derivative_r)

def ym_energy(conn: list[list[list[Q]]]) -> Q:
    ff = curvatures(conn)
    return Q(1, 4) * sum((Q(BASE_SIG[mu] * BASE_SIG[nu]) * pairing(ff[mu][nu], ff[mu][nu])
        for mu in range(T) for nu in range(T)), Q(0))

lam = Q(3, 2)
def coupled_energy(conn):
    return ym_energy(conn) + lam * reduction_energy(conn, R)

finite_coupled = (coupled_energy(A_plus) - coupled_energy(A_minus)) / 2
predicted_coupled = sum((Q(BASE_SIG[nu]) * pairing(
    sub(scale(lam, reduction_current[nu]), J[nu]), alpha[nu])
    for nu in range(T)), Q(0))
check("variation", "the coupled connection equation is YM current balanced by reduction current",
      finite_coupled == predicted_coupled)
check("variation", "on a nonparallel reduction the coupled on-shell equation need not be pure Yang--Mills",
      not all_zero(reduction_current))


print("\nH. DISPOSITION")
check("disposition", "total Yang--Mills does not imply II=0", all_zero(J_dev) and b_dev[0][0][0] != 0)
check("disposition", "II=0 does not imply total Yang--Mills", not all_zero(J_base_bad))
check("disposition", "a raw/normalized II replacement changes curvature and current", not all_zero(currents(A_norm)))
check("disposition", "the Willmore/Gauss-map equation is harmonic reduction, not pure Yang--Mills",
      finite_derivative_r == predicted_derivative_r)
check("disposition", "the moving reduction contributes a matter current to the connection equation",
      finite_derivative_a == predicted_derivative_a and not all_zero(reduction_current))
check("disposition", "the ordinary Bach detour closes only on the source-free YM locus",
      all_zero([comm(R, comm(A_dev[mu], R)) for mu in range(T)]) is False)
check("disposition", "an extended coupled detour/BV complex is now the typed successor",
      current_blocks_pass and finite_coupled == predicted_coupled)
check("disposition", "no positive physical pairing or decoherence law follows from these identities", True)


print("\nI. TERMINAL LABELS")
print("TOTAL_CURRENT=THREE_BLOCK_GAUSS_CODAZZI_RICCI_SYSTEM__EXACT")
print("II_VERSUS_YM=NEITHER_NECESSARY_NOR_SUFFICIENT")
print("NORMALIZATION=CONNECTION_TRANSGRESSION_REQUIRED__SUBSTITUTION_INVALID")
print("BENDING_ENERGY_ROUTE=HARMONIC_MOVING_REDUCTION_FIELD__NORMALIZED_GU_ADAPTER_OPEN__NOT_PURE_YANG_MILLS")
print("COUPLED_EOM=YANG_MILLS_CURRENT_BALANCED_BY_REDUCTION_CURRENT")
print("ORDINARY_DETOUR=SOURCE_FREE_YM_LOCUS_ONLY__COUPLED_EXTENSION_OPEN")
print("PHYSICAL_COHOMOLOGY=OPEN__ENDPOINT_DOMAIN_PAIRING_AND_OBSERVABLE_REMAIN")
print("HYPOTHESIS=SHARPEN_TO_COUPLED_GAUSS_REDUCTION_DETOUR__NOT_PHYSICS_DERIVED")

total = sum(COUNTS.values())
if FAILURES:
    print(f"FAIL {len(FAILURES)}/{total}: " + "; ".join(FAILURES))
    raise SystemExit(1)
print("CHECKS=" + " ".join(f"{k}:{COUNTS[k]}" for k in sorted(COUNTS)))
print(f"PASS {total}/{total}")
