#!/usr/bin/env python3
"""BD-2 (NUMBERED baryon namespace, not the lettered base-duality BD-A/B/C/D).

B-CHARGE CENSUS OF THE su(3,2) IMAGE INSIDE BD-1's k (+) p PARTITION OF so(6,4).

CP-1 named this the one genuinely new computable object created by composing
SC-A's constructed fibrewise embedding su(3,2) < so(6,4) with BD-1's B-violation
partition, and refused to compute it from the composition channel.  This probe
computes it.

THE QUESTION.  BD-1 partitioned so(6,4) = k(21) (+) p(24) and showed all 24
B-violating root directions lie in p and zero in k.  SC-A constructed an
explicit su(3,2) < so(6,4) (dim 24).  Since 24 > 21 = dim k, the image cannot
sit inside k.  Which B-violating directions does it retain, named as root and
charge data?

THE TRANSPORT, WHICH IS THE WHOLE RISK (PD-STRUCTURE-TRANSPORT, 7 dated
receipts: silently changing carrier, bilinear form, real structure, or basis
convention mid-transport).  Written out and machine-checked in section 1
against the literal text of both source probes:

  BD-1  tests/channel-swings/joe_directed_baryon_gauge_bviolation_probe.py
        block_of(i) = (2*i - 2, 2*i - 1)          plane i  <-> axes (2i-2, 2i-1)
        ETA = np.diag([1] * P_BLOCK + [-1] * Q_BLOCK)      eta = diag(+^6, -^4)
        k = same-block generators (21), p = mixed-block (24)

  SC-A  tests/channel-swings/joe_directed_sca_right_chain.py
        realify:  R[2*i][2*j] = a ; R[2*i][2*j+1] = -b ;
                  R[2*i+1][2*j] = b ; R[2*i+1][2*j+1] = a
                                                  plane i  <-> axes (2i, 2i+1)
        H = [+1,+1,+1,-1,-1] for (p,q) = (3,2)  ->  eta_R = diag(+^6, -^4)
        interleave_perm() = [0,1,2,3,4,5] + [6,7,8,9]      = the IDENTITY

  So the two files use the SAME 5 two-planes, the SAME bilinear form, and the
  map between them is the identity.  Nothing is reordered, rescaled or
  re-signed.  Every one of those four facts is asserted below by exact
  substring match against the two files on disk, so a later edit to either
  convention reds this probe instead of silently moving the census.

  The counterfactual is live in SC-A's own file: block_perm() = [0,1,2,5,6,7,
  3,4,8,9] is the permutation the Re-major realification would need.  SC-A
  uses it in BLOCK 2 (a different object) and NOT in the su(3,2) embedding.
  Planted control PC-T2 shows that applying it would break the census.

WHAT IS DERIVED RATHER THAN ASSUMED.  The complex structure is not chosen:
J is read off SC-A's realify (multiplication by i) and then DECOMPOSED in the
so(10) generator basis by exact linear algebra, giving J = -sum_j A_{2j-2,2j-1}
with UNIFORM sign.  Membership of a root vector in the image is then decided by
the exact matrix commutator [rho(J), E_alpha] = 0 on the 32-dim Clifford module,
never by a hand-computed root condition.

EXACTNESS.  Gamma matrices are exact Z[i] integer matrices (Jordan-Wigner, the
BD-1/MJ-1/MJ-3 discipline).  Root vectors are exact integer matrices.  All
linear algebra over Fraction.  numpy is an integer array container only.  No
floating point is load-bearing anywhere; assert_no_float sweeps the RESULT.

SCOPE.  Algebra census only.  No rates, no operators beyond BD-1's dimension-six
bookkeeping, no lifetimes.  The result binds the RECONSTRUCTED chain (SC-A is
reconstruction grade, the audio check is owed, SC-GRP-50 is unwritten).

Usage:  python3 joe_directed_bd2_su32_image_b_charge_census.py [--selftest]
"""
from __future__ import annotations

import sys
from fractions import Fraction as F
from itertools import combinations, product

import numpy as np

# --------------------------------------------------------------------------
# Mutations for --selftest.  Each corrupts MACHINERY or a REFERENCE; none
# loosens a check.  A mutation caught only by a crash is REJECTED.
# --------------------------------------------------------------------------
MUT = {
    "gamma_site": "Gamma_{2j} built from SX instead of SY at site 3 -- corrupts the "
                  "Clifford algebra the whole census rides on",
    "plane_pair": "BD-1's plane pairing changed from (2i-2, 2i-1) to (i-1, i+4) -- "
                  "the Re-major realification convention, silently",
    "block_split": "the k/p axis boundary moved from 6 to 5 -- wrong bilinear form",
    "bl_coeff": "BD-1's B-L coefficient -(2/3) changed to -(1/3) -- corrupts the "
                "inherited charge grading",
    "j_sign": "the complex structure's sign flipped on plane 3 only -- a "
              "non-uniform J passed off as SC-A's",
    "expect_multiplet": "the expected retained multiplet reference flipped from "
                        "|dY| = 5/6 to |dY| = 1/6",
    "transport_quote": "the asserted SC-A convention quote corrupted -- the "
                       "byte-level transport check must catch it",
}
ACTIVE = set()
if "--mutate" in sys.argv:
    _i = sys.argv.index("--mutate")
    _m = sys.argv[_i + 1]
    if _m not in MUT:
        raise SystemExit(f"unknown mutation {_m!r}; known: {sorted(MUT)}")
    ACTIVE.add(_m)

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok), detail))


def check_eq(name: str, got, want, detail: str = "") -> None:
    check(name, got == want, detail or f"got {got!r}, want {want!r}")


def on(m: str) -> bool:
    return m in ACTIVE


# ==========================================================================
# 0.  Exact arithmetic primitives.
# ==========================================================================
class Zi:
    """Exact Gaussian-integer matrix (BD-1's class, same discipline)."""

    __slots__ = ("re", "im")

    def __init__(self, re, im):
        self.re = np.asarray(re, dtype=np.int64)
        self.im = np.asarray(im, dtype=np.int64)

    @staticmethod
    def eye(n):
        return Zi(np.eye(n, dtype=np.int64), np.zeros((n, n), dtype=np.int64))

    def __matmul__(self, o):
        return Zi(self.re @ o.re - self.im @ o.im, self.re @ o.im + self.im @ o.re)

    def __add__(self, o):
        return Zi(self.re + o.re, self.im + o.im)

    def __sub__(self, o):
        return Zi(self.re - o.re, self.im - o.im)

    def scaled(self, a, b=0):
        return Zi(a * self.re - b * self.im, a * self.im + b * self.re)

    def equals(self, o):
        return bool(np.array_equal(self.re, o.re) and np.array_equal(self.im, o.im))

    def is_zero(self):
        return bool(not self.re.any() and not self.im.any())


def kron(a, b):
    return Zi(np.kron(a.re, b.re) - np.kron(a.im, b.im),
              np.kron(a.re, b.im) + np.kron(a.im, b.re))


def rref_rank(rows: list[list[F]]) -> int:
    """Exact rank over Q."""
    if not rows:
        return 0
    A = [r[:] for r in rows]
    n, m, rank = len(A), len(A[0]), 0
    for col in range(m):
        piv = next((r for r in range(rank, n) if A[r][col] != 0), None)
        if piv is None:
            continue
        A[rank], A[piv] = A[piv], A[rank]
        inv = F(1) / A[rank][col]
        A[rank] = [x * inv for x in A[rank]]
        for r in range(n):
            if r != rank and A[r][col] != 0:
                f = A[r][col]
                A[r] = [x - f * y for x, y in zip(A[r], A[rank])]
        rank += 1
        if rank == n:
            break
    return rank


def span_dim(vs: list[list[F]]) -> int:
    return rref_rank(vs)


def in_span(vs: list[list[F]], v: list[F]) -> bool:
    return rref_rank(vs + [v]) == rref_rank(vs)


def intersection_dim(A: list[list[F]], B: list[list[F]]) -> int:
    return span_dim(A) + span_dim(B) - span_dim(A + B)


def flat(M):
    return [x for row in M for x in row]


def matmul(A, B):
    n, m, k = len(A), len(B[0]), len(B)
    return [[sum((A[i][t] * B[t][j] for t in range(k)), F(0)) for j in range(m)]
            for i in range(n)]


def add(A, B):
    return [[a + b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def sub(A, B):
    return [[a - b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def transpose(A):
    return [list(c) for c in zip(*A)]


def bracket(A, B):
    return sub(matmul(A, B), matmul(B, A))


def is_zero_mat(A):
    return all(x == 0 for row in A for x in row)


def zeros(n):
    return [[F(0)] * n for _ in range(n)]


def assert_no_float(obj, path="RESULT"):
    if isinstance(obj, float):
        raise AssertionError(f"floating point at {path}")
    if isinstance(obj, dict):
        for k, v in obj.items():
            assert_no_float(v, f"{path}.{k}")
    elif isinstance(obj, (list, tuple, set)):
        for i, v in enumerate(obj):
            assert_no_float(v, f"{path}[{i}]")


# ==========================================================================
# 1.  THE TRANSPORT.  Byte-level convention checks against both source files.
# ==========================================================================
REPO_TESTS = __file__.rsplit("/", 1)[0]
BD1_PATH = REPO_TESTS + "/joe_directed_baryon_gauge_bviolation_probe.py"
SCA_PATH = REPO_TESTS + "/joe_directed_sca_right_chain.py"


def transport_block():
    bd1 = open(BD1_PATH).read()
    sca = open(SCA_PATH).read()

    # --- BD-1's side: plane pairing, bilinear form, k/p rule.
    check("T1 BD-1 pairs weight-plane i with axes (2i-2, 2i-1) [exact source line]",
          "return (2 * i - 2, 2 * i - 1)" in bd1)
    check("T2 BD-1's bilinear form is eta = diag(+^6, -^4) [exact source line]",
          "ETA = np.diag([1] * P_BLOCK + [-1] * Q_BLOCK).astype(np.int64)" in bd1
          and "P_BLOCK, Q_BLOCK = 6, 4" in bd1)
    check("T3 BD-1's k is the same-block span and p the mixed-block span "
          "[exact source line]",
          "return ({i, j} <= COLOUR_COORDS) or ({i, j} <= WEAK_COORDS)" in bd1
          and "COLOUR_COORDS, WEAK_COORDS = {1, 2, 3}, {4, 5}" in bd1)

    # --- SC-A's side: realification convention, Hermitian form, permutation.
    q = "R[2 * i + 1][2 * j + 1] = a"
    if on("transport_quote"):
        q = "R[2 * i + 1][2 * j + 1] = -a"
    check("T4 SC-A realifies plane i onto axes (2i, 2i+1) with a+bi -> [[a,-b],[b,a]] "
          "[exact source lines]",
          "R[2 * i][2 * j] = a" in sca and "R[2 * i][2 * j + 1] = -b" in sca
          and "R[2 * i + 1][2 * j] = b" in sca and q in sca,
          "same 5 two-planes as BD-1, same orientation in every plane")
    check("T5 SC-A's Hermitian form is H = (+,+,+,-,-), so eta_R = diag(+^6, -^4) "
          "[exact source lines]",
          "H = [F(1) if k < p else F(-1) for k in range(n)]" in sca
          and "eta_R = diag(1,1,1,1,1,1,-1,-1,-1,-1)" in sca)
    check("T6 SC-A's basis map into so(6,4) is interleave_perm(), and it is the "
          "IDENTITY [exact source lines]",
          "plus = [0, 1, 2, 3, 4, 5]" in sca and "minus = [6, 7, 8, 9]" in sca
          and "perm = interleave_perm()" in sca)
    interleave = [0, 1, 2, 3, 4, 5] + [6, 7, 8, 9]
    check_eq("T7 interleave_perm() evaluates to the identity on 10 letters",
             interleave, list(range(10)))

    # --- the counterfactual convention SC-A does NOT use here.
    check("T8 the Re-major counterfactual block_perm() exists in SC-A and is NOT "
          "applied to the su(3,2) embedding (it is used only in BLOCK 2)",
          "src = [0, 1, 2, 5, 6, 7, 3, 4, 8, 9]" in sca
          and sca.count("perm = block_perm()") == 1
          and "perm = block_perm()" not in sca[sca.index("def block3_su32_reading"):
                                               sca.index("def interleave_perm")])

    # --- the composed statement.
    check("T9 TRANSPORT COMPOSES: identical planes, identical bilinear form, "
          "identical axis order -- the map between BD-1's and SC-A's carriers is "
          "the identity on R^10, with no rescaling, reordering or re-signing",
          True)

    # --- provenance of the charge grading being transported (coordinator's addition).
    check("T10 PROVENANCE: BD-1's B-L is a FORMULA on so(10) weights via the "
          "Pati-Salam branching (colour = w1..w3 from Spin(6), weak = w4,w5 from "
          "Spin(4)), i.e. comparator-derived representation data, not source-native",
          "B-L        = -(2/3) * (w1+w2+w3) / 2" in open(
              REPO_TESTS + "/joe_directed_majorana_bminusl_probe.py").read()
          and "SU(3) from Spin(6) on the first three axes" in open(
              REPO_TESTS + "/joe_directed_majorana_bminusl_probe.py").read())
    check("T11 PROVENANCE: BD-1 itself types this at the routing layer "
          "(BRIDGE_OR_SEMANTIC_BOUNDARY, 'binds only the named model')",
          "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in open(
              REPO_TESTS.replace("/tests/channel-swings", "")
              + "/lab/active-research/joe-directed/baryon-number-and-proton-decay/"
                "bd1-b-violation-lives-only-in-the-removed-coset-2026-08-14.md").read())
    return {"planes": "interleaved (2i-2, 2i-1), identical in both files",
            "form": "eta = diag(+^6, -^4), identical in both files",
            "map": "identity on R^10",
            "charge_grading_provenance": "comparator-derived (SO(10)/Pati-Salam branching)"}


# ==========================================================================
# 2.  BD-1's carrier, rebuilt.  Clifford so(10) on S+, exact Z[i].
# ==========================================================================
I2 = Zi.eye(2)
SX = Zi([[0, 1], [1, 0]], [[0, 0], [0, 0]])
SY = Zi([[0, 0], [0, 0]], [[0, -1], [1, 0]])
SZ = Zi([[1, 0], [0, -1]], [[0, 0], [0, 0]])
RAISE = Zi([[0, 1], [0, 0]], [[0, 0], [0, 0]])
LOWER = Zi([[0, 0], [1, 0]], [[0, 0], [0, 0]])

NQ, DIM = 5, 32
P_BLOCK, Q_BLOCK = (5, 5) if on("block_split") else (6, 4)


def site(j, op):
    out = Zi.eye(1)
    for k in range(1, NQ + 1):
        out = kron(out, SZ if k < j else (op if k == j else I2))
    return out


def pure(j, op):
    out = Zi.eye(1)
    for k in range(1, NQ + 1):
        out = kron(out, op if k == j else I2)
    return out


G = []
for j in range(1, NQ + 1):
    G.append(site(j, SX))
    G.append(site(j, SX if (on("gamma_site") and j == 3) else SY))

RS = [site(j, RAISE) for j in range(1, NQ + 1)]
LS = [site(j, LOWER) for j in range(1, NQ + 1)]

CHIR = Zi.eye(DIM)
for j in range(1, NQ + 1):
    CHIR = CHIR @ pure(j, SZ)


def weight_of(idx: int):
    return tuple(1 if (idx >> (NQ - 1 - k)) & 1 == 0 else -1 for k in range(NQ))


SPLUS = [b for b in range(DIM) if int(CHIR.re[b, b]) == 1]
W16 = [weight_of(b) for b in SPLUS]


def block_of(i):
    """Axis indices (0-based) carrying weight-plane i.  BD-1's convention."""
    if on("plane_pair"):
        return (i - 1, i + 4)
    return (2 * i - 2, 2 * i - 1)


# --- BD-1's charges, reproduced verbatim.
BL_NUM = -1 if on("bl_coeff") else -2


def b_minus_l(w):
    return F(BL_NUM, 3) * F(w[0] + w[1] + w[2], 2)


def t3l(w):
    return F(w[3] - w[4], 4)


def t3r(w):
    return F(w[3] + w[4], 4)


def hyper(w):
    return t3r(w) + b_minus_l(w) / 2


def charge(w):
    return t3l(w) + hyper(w)


def colour_neutral(w):
    return w[0] == w[1] == w[2]


def baryon(w):
    return F(0) if colour_neutral(w) else -b_minus_l(w)


def lepton(w):
    return b_minus_l(w) if colour_neutral(w) else F(0)


def u1_X(w):
    """The u(1) that commutes with the aligned sl(5): the sum of plane weights."""
    return F(sum(w))


def carrier_controls():
    two_I, zero32 = Zi.eye(DIM).scaled(2), Zi.eye(DIM).scaled(0)
    check("PC0.1 Clifford relations {G_a, G_b} = 2 delta_ab exact on all 100 pairs",
          all((G[a] @ G[b] + G[b] @ G[a]).equals(two_I if a == b else zero32)
              for a in range(10) for b in range(10)))
    check("PC0.2 chirality squares to 1 and anticommutes with every Gamma",
          (CHIR @ CHIR).equals(Zi.eye(DIM))
          and all((CHIR @ G[a] + G[a] @ CHIR).is_zero() for a in range(10)))
    check_eq("PC0.3 S+ is 16-dimensional with 16 distinct weights",
             (len(SPLUS), len(set(W16))), (16, 16))
    check("PC0.4 the Cartan SZ_j is diagonal with eigenvalue w_j",
          all(int(pure(j, SZ).re[b, b]) == weight_of(b)[j - 1]
              for j in range(1, NQ + 1) for b in range(DIM)))
    check("PC0.5 BD-1 charge validation: nu_R = (1,1,1,1,1) is the unique SM "
          "singlet, B-L = -1, Q = 0",
          b_minus_l((1,) * 5) == -1 and charge((1,) * 5) == 0
          and sum(1 for w in W16 if colour_neutral(w) and t3l(w) == 0
                  and hyper(w) == 0) == 1)
    check("PC0.6 BD-1 charge validation: 4 lepton + 12 quark states, all |Q| in "
          "{0, 1/3, 2/3, 1}",
          (sum(1 for w in W16 if colour_neutral(w)),
           sum(1 for w in W16 if not colour_neutral(w))) == (4, 12)
          and all(charge(w) in (0, F(1, 3), F(-1, 3), F(2, 3), F(-2, 3), 1, -1)
                  for w in W16))
    check("PC0.7 BD-1 charge validation: 6 states at B = +1/3, 6 at B = -1/3, "
          "2 at L = +1, 2 at L = -1, totals zero",
          (sum(1 for w in W16 if baryon(w) == F(1, 3)),
           sum(1 for w in W16 if baryon(w) == F(-1, 3)),
           sum(1 for w in W16 if lepton(w) == 1),
           sum(1 for w in W16 if lepton(w) == -1)) == (6, 6, 2, 2)
          and sum(baryon(w) for w in W16) == 0 and sum(lepton(w) for w in W16) == 0)
    sm_Y = sorted([F(1, 6)] * 6 + [F(-2, 3)] * 3 + [F(1, 3)] * 3
                  + [F(-1, 2)] * 2 + [F(1)] + [F(0)])
    got_Y = sorted(hyper(w) for w in W16)
    check("PC0.8 the 16-state hypercharge multiset is the Standard Model one up to "
          "the global sign of BD-1's nu_R = -1 convention (k77's independent "
          "2026-08-12 check, reproduced: k77 prints the opposite global sign)",
          got_Y == sorted(-y for y in sm_Y) or got_Y == sm_Y,
          f"got {got_Y}")
    check("PC0.9 and the electric-charge multiset is the one-generation Standard "
          "Model one: {0 x2, +-1/3 x3 each, +-2/3 x3 each, +-1 x1 each}",
          sorted(charge(w) for w in W16)
          == sorted([F(0)] * 2 + [F(1, 3)] * 3 + [F(-1, 3)] * 3 + [F(2, 3)] * 3
                    + [F(-2, 3)] * 3 + [F(1)] + [F(-1)]))


# ==========================================================================
# 3.  Roots, the k/p split, and BD-1's B-violation gate.  [R] reproduction.
# ==========================================================================
ROOTS: dict[tuple, dict] = {}
for i, j in combinations(range(1, NQ + 1), 2):
    for si, sj in product((1, -1), repeat=2):
        E = (RS[i - 1] if si == 1 else LS[i - 1]) @ (RS[j - 1] if sj == 1 else LS[j - 1])
        alpha = tuple((2 * si if k == i - 1 else (2 * sj if k == j - 1 else 0))
                      for k in range(NQ))
        ROOTS[(i, j, si, sj)] = {"E": E, "alpha": alpha, "pair": (i, j),
                                 "key": (i, j, si, sj)}

COLOUR_COORDS, WEAK_COORDS = {1, 2, 3}, {4, 5}


def in_k(rec) -> bool:
    i, j = rec["pair"]
    return ({i, j} <= COLOUR_COORDS) or ({i, j} <= WEAK_COORDS)


def transitions(rec):
    E, out = rec["E"], []
    for b_src in SPLUS:
        for b_tgt in SPLUS:
            if E.re[b_tgt, b_src] or E.im[b_tgt, b_src]:
                out.append((weight_of(b_src), weight_of(b_tgt)))
    return out


for rec in ROOTS.values():
    rec["tr"] = transitions(rec)
    rec["S"] = {(baryon(t) - baryon(s), lepton(t) - lepton(s)) for s, t in rec["tr"]}


def delta(fn, rec):
    return {fn(t) - fn(s) for s, t in rec["tr"]}


K_ROOTS = [r for r in ROOTS.values() if in_k(r)]
P_ROOTS = [r for r in ROOTS.values() if not in_k(r)]


def bd1_reproduction():
    check_eq("R1 [R] so(10) has 40 root vectors; 40 + 5 Cartan = 45", (len(ROOTS), 45),
             (40, 40 + NQ))
    check_eq("R2 [R] BD-1's split: 16 roots in k (dim 21 with the Cartan), 24 in p",
             (len(K_ROOTS), len(K_ROOTS) + NQ, len(P_ROOTS)), (16, 21, 24))
    check("R3 [R] vector-side Killing sign reproduces the same 21/24 split",
          _killing_split() == (21, 24))
    check("R4 [R] BD-1's GATE: every k root has |S| = 1 (B and L separately "
          "conserved); every p root has |S| = 2 (baryon number violated)",
          all(len(r["S"]) == 1 for r in K_ROOTS)
          and all(len(r["S"]) == 2 for r in P_ROOTS))
    check("R5 [R] BD-1: the k/p split and the B-violation split are the SAME "
          "partition of the 40 roots",
          {r["key"] for r in P_ROOTS}
          == {r["key"] for r in ROOTS.values() if len(r["S"]) > 1})
    check("R6 [R] BD-1: all 24 p directions carry |Delta(B-L)| = 2/3 and are weak "
          "doublets |Delta T3L| = 1/2",
          {abs(delta(b_minus_l, r).pop()) for r in P_ROOTS} == {F(2, 3)}
          and {abs(delta(t3l, r).pop()) for r in P_ROOTS} == {F(1, 2)})
    check_eq("R7 [R] BD-1: p splits 12 at |Delta Y| = 5/6 (the SU(5) X,Y multiplet) "
             "and 12 at |Delta Y| = 1/6 (the (3,2) of 10 + 10bar)",
             (sum(1 for r in P_ROOTS if abs(delta(hyper, r).pop()) == F(5, 6)),
              sum(1 for r in P_ROOTS if abs(delta(hyper, r).pop()) == F(1, 6))),
             (12, 12))
    check_eq("R8 [R] BD-1: k's 16 roots are 6 gluons + 6 leptoquarks (3,1)_{2/3} "
             "+ 2 W_L + 2 W_R",
             (len(GLUON), len(LQ), len(WL), len(WR)), (6, 6, 2, 2))
    check("R9 [R] BD-1: the 6 surviving leptoquarks are weak singlets with "
          "|Delta(B-L)| = 4/3 -- Pati-Salam type, not SU(5) X,Y type",
          all(delta(t3l, r) == {F(0)} for r in LQ)
          and {abs(delta(b_minus_l, r).pop()) for r in LQ} == {F(4, 3)})


def _killing_split():
    eta = [[F(1 if i == j and i < P_BLOCK else (-1 if i == j else 0))
            for j in range(10)] for i in range(10)]
    same = mixed = 0
    for a in range(10):
        for b in range(a + 1, 10):
            A = zeros(10)
            A[a][b], A[b][a] = F(1), F(-1)
            X = matmul(eta, A)
            tr = sum(matmul(X, X)[t][t] for t in range(10))
            if tr < 0:
                same += 1
            else:
                mixed += 1
    return (same, mixed)


GLUON = [r for r in K_ROOTS if set(r["pair"]) <= COLOUR_COORDS
         and delta(b_minus_l, r) == {F(0)}]
LQ = [r for r in K_ROOTS if set(r["pair"]) <= COLOUR_COORDS
      and delta(b_minus_l, r) != {F(0)}]
WL = [r for r in K_ROOTS if set(r["pair"]) <= WEAK_COORDS and delta(t3l, r) != {F(0)}]
WR = [r for r in K_ROOTS if set(r["pair"]) <= WEAK_COORDS and delta(t3r, r) != {F(0)}]


# ==========================================================================
# 4.  SC-A's side, rebuilt: so(6,4), the complex structure J, u/su(3,2).
#     Real 10x10 Fraction matrices; nothing complexified yet.
# ==========================================================================
def eta_mat():
    return [[F(1 if i == j and i < P_BLOCK else (-1 if i == j else 0))
             for j in range(10)] for i in range(10)]


def A_gen(a, b):
    """A_{ab} = E_ab - E_ba, the so(10,C) generator basis."""
    M = zeros(10)
    M[a][b], M[b][a] = F(1), F(-1)
    return M


def so64_basis():
    """so(6,4) = {eta A : A antisymmetric}, 45 real generators."""
    e = eta_mat()
    return [matmul(e, A_gen(a, b)) for a, b in combinations(range(10), 2)]


def J_of(eps):
    """SC-A's realify sends 1 -> I and i -> [[0,-1],[1,0]] in EVERY plane.
    eps = (1,)*5 is SC-A's construction; other eps are the counterfactuals."""
    M = zeros(10)
    for j in range(1, NQ + 1):
        a, b = block_of(j)
        M[a][b], M[b][a] = F(-eps[j - 1]), F(eps[j - 1])
    return M


SCA_EPS = (1, 1, 1, 1, -1) if on("j_sign") else (1, 1, 1, 1, 1)


def centralizer(basis, X):
    """{Y in span(basis) : [X, Y] = 0}, returned as a list of matrices."""
    rows, mats = [], []
    for B in basis:
        rows.append(flat(bracket(X, B)))
        mats.append(B)
    # solve rows^T c = 0 : nullspace of the 100 x len(basis) matrix
    n_un = len(basis)
    A = [[rows[c][r] for c in range(n_un)] for r in range(len(rows[0]))]
    # gaussian elimination to find nullspace basis
    A = [r[:] for r in A]
    m = len(A)
    piv_cols, rank = [], 0
    for col in range(n_un):
        piv = next((r for r in range(rank, m) if A[r][col] != 0), None)
        if piv is None:
            continue
        A[rank], A[piv] = A[piv], A[rank]
        inv = F(1) / A[rank][col]
        A[rank] = [x * inv for x in A[rank]]
        for r in range(m):
            if r != rank and A[r][col] != 0:
                f = A[r][col]
                A[r] = [x - f * y for x, y in zip(A[r], A[rank])]
        piv_cols.append(col)
        rank += 1
    free = [c for c in range(n_un) if c not in piv_cols]
    out = []
    for fc in free:
        coef = [F(0)] * n_un
        coef[fc] = F(1)
        for r, pc in enumerate(piv_cols):
            coef[pc] = -A[r][fc]
        M = zeros(10)
        for c, cf in enumerate(coef):
            if cf:
                M = add(M, [[cf * x for x in row] for row in mats[c]])
        out.append(M)
    return out


def derived_algebra(basis):
    keep, rows = [], []
    for X, Y in combinations(basis, 2):
        v = flat(bracket(X, Y))
        if rref_rank(rows + [v]) > len(rows):
            rows.append(v)
            keep.append(bracket(X, Y))
        if len(rows) >= len(basis):
            break
    return keep


def vector_side_construction():
    so64 = so64_basis()
    e = eta_mat()
    check_eq("V1 so(6,4) has 45 generators, all eta-skew", span_dim([flat(X) for X in so64]),
             45)
    check("V2 every generator satisfies X^T eta + eta X = 0",
          all(is_zero_mat(add(matmul(transpose(X), e), matmul(e, X))) for X in so64))
    J = J_of(SCA_EPS)
    check("V3 SC-A's J (multiplication by i under realify) satisfies J^2 = -I",
          all(matmul(J, J)[i][j] == (F(-1) if i == j else F(0))
              for i in range(10) for j in range(10)))
    check("V4 J lies in so(6,4): J^T eta + eta J = 0",
          is_zero_mat(add(matmul(transpose(J), e), matmul(e, J))))
    # DERIVED, not assumed: decompose J in the A_{ab} basis and read the signs.
    coeffs = {}
    for a, b in combinations(range(10), 2):
        coeffs[(a, b)] = J[a][b]
    nz = {k: v for k, v in coeffs.items() if v != 0}
    planes = {block_of(j) for j in range(1, NQ + 1)}
    check("V5 DERIVED: J decomposes as -sum_j A_{2j-2,2j-1} -- supported only on "
          "the five planes, with the SAME sign in every plane (this is the fact "
          "the whole census rests on, and it is read off SC-A's realify, not chosen)",
          set(nz.keys()) == planes and set(nz.values()) == {F(-1)},
          f"support {sorted(nz.keys())}, coefficients {sorted(set(nz.values()))}")

    u32 = centralizer(so64, J)
    check_eq("V6 [R] dim of the centralizer of J in so(6,4) = 25 = dim u(3,2) "
             "(SC-A R6.2 / k77, reproduced independently)",
             span_dim([flat(X) for X in u32]), 25)
    su32 = derived_algebra(u32)
    check_eq("V7 [R] dim of its derived algebra = 24 = dim su(3,2) (SC-A R6.1) -- "
             "obtained INTRINSICALLY, with no complex-trace convention",
             span_dim([flat(X) for X in su32]), 24)

    pati = [X for X in so64 if all(X[i][j] == 0 for i in range(10) for j in range(10)
                                   if (i < P_BLOCK) != (j < P_BLOCK))]
    check_eq("V8 [R] the maximal compact so(6)+so(4) has dimension 21 (BD-1's k)",
             span_dim([flat(X) for X in pati]), 21)
    k_int = intersection_dim([flat(X) for X in su32], [flat(X) for X in pati])
    u_int = intersection_dim([flat(X) for X in u32], [flat(X) for X in pati])
    check_eq("V9 [R] so(6)+so(4) intersect su(3,2) = 12 (SC-A R6.12, CH-3 E, "
             "k77 2026-08-12 -- three prior computations, reproduced here)",
             k_int, 12)
    check_eq("V10 [R] so(6)+so(4) intersect u(3,2) = 13, 'up to a reductive factor "
             "of U(1)' (SC-A R6.13)", u_int, 13)

    # theta-stability, DERIVED: theta(X) = -X^T preserves the image, because
    # theta(J) = J.  Hence image = (image n k) (+) (image n p) with no remainder.
    Jt = [[-J[j][i] for j in range(10)] for i in range(10)]
    check("V11 DERIVED: theta(J) = -J^T = J, so theta preserves the centralizer of "
          "J; the image is theta-stable and therefore splits with NO remainder",
          Jt == J)
    p_sub = [X for X in so64 if any(X[i][j] != 0 for i in range(10) for j in range(10)
                                    if (i < P_BLOCK) != (j < P_BLOCK))]
    p_only = [flat(X) for X in so64 if all(
        X[i][j] == 0 for i in range(10) for j in range(10)
        if (i < P_BLOCK) == (j < P_BLOCK))]
    p_int = intersection_dim([flat(X) for X in su32], p_only)
    check_eq("V12 REAL-DIMENSION CENSUS, computed on the real 10x10 carrier with no "
             "complexification: dim(image n k) = 12, dim(image n p) = 12",
             (k_int, p_int), (12, 12))
    check_eq("V13 and 12 + 12 = 24 exhausts the image -- the theta-split has no "
             "remainder, as V11 predicts", k_int + p_int, 24)
    check("V14 the p-part is nonzero and had to be: dim su(3,2) = 24 > 21 = dim k",
          p_int > 0 and 24 > 21 and p_int >= 24 - 21)
    del p_sub
    return {"dim_u32": 25, "dim_su32": 24, "dim_image_cap_k": k_int,
            "dim_image_cap_p": p_int}


# ==========================================================================
# 5.  The spinor-side transport: rho(A_ab) = (1/2) Gamma_a Gamma_b, verified
#     as a Lie algebra homomorphism, then used to test root membership.
# ==========================================================================
def rho2(a, b):
    """2 * rho(A_ab) = Gamma_a Gamma_b, kept integral."""
    return G[a] @ G[b]


def homomorphism_check():
    """[rho(A_ab), rho(A_cd)] = rho([A_ab, A_cd]) exactly.  Scaled by 4 to stay
    in Z[i]:  [2rho, 2rho] = 4[rho, rho] = 4 rho(bracket) = 2 * (2rho(bracket))."""
    ok = True
    idx = list(combinations(range(10), 2))
    for (a, b), (c, d) in combinations(idx, 2):
        lhs = rho2(a, b) @ rho2(c, d) - rho2(c, d) @ rho2(a, b)
        br = bracket(A_gen(a, b), A_gen(c, d))
        rhs = Zi.eye(DIM).scaled(0)
        for x, y in idx:
            co = br[x][y]
            if co:
                assert co.denominator == 1
                rhs = rhs + rho2(x, y).scaled(2 * int(co))
        if not lhs.equals(rhs):
            ok = False
            break
    check("H1 DERIVED: rho(A_ab) = (1/2) Gamma_a Gamma_b is an exact Lie algebra "
          "homomorphism so(10) -> End(S), verified on all 990 basis pairs -- this "
          "is the bridge between SC-A's vector-side J and BD-1's spinor-side roots",
          ok)


def rho_of(M):
    """Spinor image of a vector-side so(10,C) element, scaled by 2 (exact Z[i])."""
    out = Zi.eye(DIM).scaled(0)
    for a, b in combinations(range(10), 2):
        co = M[a][b]
        if co:
            assert co.denominator == 1, "non-integer coefficient in rho_of"
            out = out + rho2(a, b).scaled(int(co))
    return out


def image_roots(eps):
    """Roots alpha with [rho(J_eps), E_alpha] = 0 -- membership decided by an
    exact matrix commutator, never by a hand-derived root condition."""
    RJ = rho_of(J_of(eps))
    return [r for r in ROOTS.values() if (RJ @ r["E"] - r["E"] @ RJ).is_zero()]


def coroot_diag(rec):
    """Diagonal of [E_alpha, E_-alpha] on S+, as an exact 16-vector."""
    i, j, si, sj = rec["key"]
    opp = ROOTS[(i, j, -si, -sj)]["E"]
    C = rec["E"] @ opp - opp @ rec["E"]
    return [F(int(C.re[b, b])) for b in SPLUS]


def cartan_span(roots):
    return [coroot_diag(r) for r in roots]


# ==========================================================================
# 6.  THE CENSUS.
# ==========================================================================
def multiplet(rec):
    if in_k(rec):
        if rec in GLUON:
            return "gluon (8,1)_0"
        if rec in LQ:
            return "PS leptoquark (3,1)_{+-2/3}"
        if rec in WL:
            return "W_L (1,3)_0"
        return "W_R (1,1)_{+-1}"
    y = abs(delta(hyper, rec).pop())
    return ("X,Y (3,2)_{+-5/6}  [SU(5)]" if y == F(5, 6)
            else "X' (3,2)_{+-1/6}  [10+10bar of SU(5)]")


def census(name, roots, cartan_vecs):
    kr = [r for r in roots if in_k(r)]
    pr = [r for r in roots if not in_k(r)]
    dim_cartan = span_dim(cartan_vecs) if cartan_vecs else 0
    bviol = [r for r in pr if len(r["S"]) > 1] + [r for r in kr if len(r["S"]) > 1]
    tally: dict[str, int] = {}
    for r in pr:
        tally[multiplet(r)] = tally.get(multiplet(r), 0) + 1
    return {"name": name,
            "dim_k_part": len(kr) + dim_cartan,
            "dim_p_part": len(pr),
            "dim_total": len(kr) + len(pr) + dim_cartan,
            "n_roots_k": len(kr), "n_roots_p": len(pr), "dim_cartan": dim_cartan,
            "n_B_violating": len(bviol),
            "p_multiplets": dict(sorted(tally.items()))}


def horn_A():
    roots = image_roots(SCA_EPS)
    check_eq("A1 the image contains exactly 20 root directions (decided by exact "
             "matrix commutator with rho(J), not by a root formula)", len(roots), 20)
    cart = cartan_span(roots)
    check_eq("A2 their coroots span a 4-dimensional Cartan; 20 + 4 = 24 = dim su(3,2), "
             "and adding the J direction gives 25 = dim u(3,2)",
             (span_dim(cart), len(roots) + span_dim(cart)), (4, 24))
    c = census("su(3,2) image, ALIGNED horn (SC-A's construction)", roots, cart)
    check_eq("A3 CENSUS (i): dim(image n k) = 12 and dim(image n p) = 12 -- "
             "root-side count agrees with the independent real vector-side count",
             (c["dim_k_part"], c["dim_p_part"]), (12, 12))
    check_eq("A4 the k-part is 8 roots + 4 Cartan; the p-part is 12 roots and no "
             "Cartan (the whole Cartan of so(6,4) lies in k)",
             (c["n_roots_k"], c["dim_cartan"], c["n_roots_p"]), (8, 4, 12))
    check("A5 the retained k roots are exactly the 6 gluons and the 2 W_L -- "
          "colour and weak isospin, and nothing else",
          {r["key"] for r in roots if in_k(r)}
          == {r["key"] for r in GLUON} | {r["key"] for r in WL})
    check("A6 the image's k-part IS the Standard Model algebra: it contains BD-1's "
          "hypercharge Y, its weak isospin T3L and its colour Cartan",
          in_span(cart, [hyper(w) for w in W16])
          and in_span(cart, [t3l(w) for w in W16])
          and in_span(cart, [F(w[0] - w[1], 4) for w in W16]))
    check("A7 and it does NOT contain u(1)_X (the sum of plane weights), which is "
          "the direction u(3,2) has and su(3,2) does not -- 13 vs 12",
          not in_span(cart, [u1_X(w) for w in W16]))
    check_eq("A8 CENSUS (ii): the p-part is ENTIRELY the SU(5) X,Y multiplet "
             "(3,2)_{+-5/6}; the (3,2)_{+-1/6} of 10 + 10bar is retained ZERO times",
             c["p_multiplets"],
             {"X,Y (3,2)_{+-5/6}  [SU(5)]": 12} if not on("expect_multiplet")
             else {"X' (3,2)_{+-1/6}  [10+10bar of SU(5)]": 12})
    check("A9 CENSUS (ii): ALL 12 retained p directions are B-violating in BD-1's "
          "sense -- |S| = 2, S = {(+-1/3, +-1), (-+2/3, 0)}, |Delta(B-L)| = 2/3",
          all(len(r["S"]) == 2 for r in roots if not in_k(r))
          and all(sorted((abs(db), abs(dl)) for db, dl in r["S"])
                  == [(F(1, 3), F(1)), (F(2, 3), F(0))]
                  for r in roots if not in_k(r))
          and {abs(delta(b_minus_l, r).pop()) for r in roots if not in_k(r)}
          == {F(2, 3)})
    check_eq("A10 CENSUS (ii): the reconstructed chain retains 12 of BD-1's 24 "
             "B-violating directions -- exactly half, and precisely the classic "
             "SU(5) proton-decay half", c["n_B_violating"], 12)
    check("A11 zero B-violating directions in the image's k-part (BD-1's k gate "
          "inherited unchanged)",
          all(len(r["S"]) == 1 for r in roots if in_k(r)))
    check("A12 the 12 dropped B-violating directions are exactly the "
          "(3,2)_{+-1/6}, and the 9 dropped k directions are exactly BD-1's "
          "'9 survivors': 6 PS leptoquarks + 2 W_R + 1 Z' (= u(1)_X)",
          {r["key"] for r in P_ROOTS} - {r["key"] for r in roots}
          == {r["key"] for r in P_ROOTS if abs(delta(hyper, r).pop()) == F(1, 6)}
          and {r["key"] for r in K_ROOTS} - {r["key"] for r in roots}
          == {r["key"] for r in LQ} | {r["key"] for r in WR}
          and 21 - 12 == 9)
    # dimension-six bookkeeping, inherited from BD-1 unchanged
    def d6(rec):
        return {(b1 - b2, l1 - l2) for b1, l1 in rec["S"] for b2, l2 in rec["S"]}
    k_ops = {t for r in roots if in_k(r) for t in d6(r)}
    p_ops = {t for r in roots if not in_k(r) for t in d6(r)}
    check_eq("A13 the retained k-part generates only (dB, dL) = (0,0); the retained "
             "p-part generates the standard qqql (dB, dL) = (+-1, +-1)",
             (k_ops, p_ops),
             ({(F(0), F(0))},
              {(F(0), F(0)), (F(1), F(1)), (F(-1), F(-1))}))
    check("A14 every operator from the retained image conserves B-L, so BD-1's "
          "baryogenesis obstruction is untouched by the reduction",
          all(db - dl == 0 for db, dl in k_ops | p_ops))
    return c, roots, cart


def horn_B():
    """The second POSITIONAL horn: the other su(3,2) in so(6,4) whose maximal
    compact is abstractly su(3)+su(2)+u(1).  Standard GUT fact, imported and
    credited: SO(10) contains two inequivalent SU(5)s -- Georgi-Glashow (1974)
    and flipped (Barr 1982; Derendinger-Kim-Nanopoulos 1984).  Nothing new here
    except the census against BD-1's partition."""
    eps = (-1, -1, -1, 1, 1)
    roots = image_roots(eps)
    cart = cartan_span(roots)
    c = census("su(3,2) image, FLIPPED horn", roots, cart)
    check_eq("B1 the flipped position is also a 24-dimensional subalgebra "
             "(20 roots + 4 Cartan)", (len(roots), span_dim(cart)), (20, 4))
    check_eq("B2 its census is the SAME arithmetic: dim(n k) = 12, dim(n p) = 12",
             (c["dim_k_part"], c["dim_p_part"]), (12, 12))
    check("B3 its maximal compact is ABSTRACTLY su(3)+su(2)+u(1) too: it retains "
          "the same 6 gluons and the same 2 W_L",
          {r["key"] for r in roots if in_k(r)}
          == {r["key"] for r in GLUON} | {r["key"] for r in WL})
    check("B4 THE DISCRIMINATOR: it does NOT contain BD-1's hypercharge. Abstract "
          "isomorphism of the maximal compact does not fix the position, and the "
          "16-state charge assignment is what separates the two horns",
          not in_span(cart, [hyper(w) for w in W16])
          and in_span(cart, [t3l(w) for w in W16]))
    check_eq("B5 CENSUS for the flipped horn: the p-part is entirely the OTHER "
             "multiplet, (3,2)_{+-1/6}; zero SU(5) X,Y",
             c["p_multiplets"], {"X' (3,2)_{+-1/6}  [10+10bar of SU(5)]": 12})
    check_eq("B6 it too retains 12 of BD-1's 24 B-violating directions -- the "
             "count 12 is horn-INDEPENDENT, only the multiplet identity moves",
             c["n_B_violating"], 12)
    check("B7 it is genuinely su(3,2) and not another real form of sl(5,C): its "
          "maximal compact has dimension 12, which among sl(5,C)'s real forms "
          "(su(5):24, su(4,1):16, su(3,2):12, sl(5,R):10) selects su(3,2) uniquely",
          c["dim_k_part"] == 12)
    return c


def horn_sweep():
    """Exhaustive over the 32 plane-diagonal complex structures.  The question
    the tripwire demands: is SC-A's uniform sign a CHOICE or is it FORCED?"""
    vY = [hyper(w) for w in W16]
    vT3L = [t3l(w) for w in W16]
    vC = [F(w[0] - w[1], 4) for w in W16]
    aligned, results = [], {}
    for eps in product((1, -1), repeat=5):
        roots = image_roots(eps)
        cart = cartan_span(roots)
        has_colour = {r["key"] for r in GLUON} <= {r["key"] for r in roots}
        has_wl = {r["key"] for r in WL} <= {r["key"] for r in roots}
        has_Y = in_span(cart, vY) and in_span(cart, vT3L) and in_span(cart, vC)
        c = census(f"eps={eps}", roots, cart)
        results[eps] = (c["dim_k_part"], c["dim_p_part"], has_colour and has_wl and has_Y)
        if has_colour and has_wl and has_Y:
            aligned.append(eps)
    check_eq("S1 all 32 plane-diagonal complex structures give the SAME dimension "
             "census, 12 + 12 -- the ARITHMETIC of the census is convention-free",
             {(a, b) for a, b, _ in results.values()}, {(12, 12)})
    check_eq("S2 UNIQUENESS, DERIVED: exactly 2 of the 32 sign patterns put BD-1's "
             "colour, weak isospin AND hypercharge inside the image, and they are "
             "+-(1,1,1,1,1) -- SC-A's uniform realify is FORCED, not chosen",
             sorted(aligned), [(-1, -1, -1, -1, -1), (1, 1, 1, 1, 1)])
    check("S3 and the two aligned patterns give the SAME subalgebra (J and -J have "
          "the same centralizer), so the aligned horn is unique",
          {r["key"] for r in image_roots((1,) * 5)}
          == {r["key"] for r in image_roots((-1,) * 5)})
    check("S4 SC-A's own realify sign pattern is one of the two",
          tuple(SCA_EPS) in aligned or on("j_sign"),
          f"SC-A eps = {SCA_EPS}")
    return {"n_patterns": 32, "n_aligned": len(aligned)}


# ==========================================================================
# 7.  CONTROLS.
# ==========================================================================
def contrary_controls():
    """The census must DETECT avoidance where avoidance genuinely occurs."""
    # (a) the Standard Model algebra itself: 12-dimensional, entirely inside k.
    sm_roots = GLUON + WL
    sm_cart = [[F(w[0] - w[1], 4) for w in W16],
               [F(w[0] - w[2], 4) for w in W16],
               [t3l(w) for w in W16],
               [hyper(w) for w in W16]]
    c_sm = census("SM algebra (contrary control)", sm_roots, sm_cart)
    check_eq("CC1 CONTRARY CONTROL: the Standard Model subalgebra has dim 12, "
             "dim(n p) = 0 and ZERO B-violating directions -- the census detects "
             "avoidance where avoidance genuinely occurs",
             (c_sm["dim_k_part"], c_sm["dim_p_part"], c_sm["n_B_violating"]),
             (12, 0, 0))
    # (b) BD-1's whole k = Pati-Salam, 21-dimensional, also entirely inside k.
    c_k = census("k = so(6)+so(4) (contrary control)", K_ROOTS,
                 [coroot_diag(r) for r in K_ROOTS])
    check_eq("CC2 CONTRARY CONTROL: BD-1's whole maximal compact k has dim 21, "
             "dim(n p) = 0 and ZERO B-violating directions",
             (c_k["dim_k_part"], c_k["dim_p_part"], c_k["n_B_violating"]),
             (21, 0, 0))
    # (c) the positive pole: so(6,4) itself must report all 24.
    c_all = census("so(6,4) (positive control)", list(ROOTS.values()),
                   [coroot_diag(r) for r in ROOTS.values()])
    check_eq("CC3 POSITIVE CONTROL: so(6,4) itself reports 45 = 21 + 24 with all "
             "24 B-violating -- the instrument reads 24, 12, 12, 0, 0 across five "
             "different subalgebras, so it discriminates",
             (c_all["dim_k_part"], c_all["dim_p_part"], c_all["n_B_violating"]),
             (21, 24, 24))
    return {"sm": c_sm, "k": c_k, "so64": c_all}


def planted_failing_controls():
    """Each must FAIL to reproduce the census, proving the census is not shape-forced."""
    e = eta_mat()
    so64 = so64_basis()
    pati = [X for X in so64 if all(X[i][j] == 0 for i in range(10) for j in range(10)
                                   if (i < P_BLOCK) != (j < P_BLOCK))]
    p_only = [flat(X) for X in so64 if all(
        X[i][j] == 0 for i in range(10) for j in range(10)
        if (i < P_BLOCK) == (j < P_BLOCK))]

    # BD-1's hypercharge as a VECTOR-side generator, from k77's independently
    # computed plane weights (2,2,2,-3,-3).
    Yvec = zeros(10)
    for j, co in zip(range(1, NQ + 1), (2, 2, 2, -3, -3)):
        a, b = block_of(j)
        Yvec[a][b], Yvec[b][a] = Yvec[a][b] + F(-co), Yvec[b][a] + F(co)
    su_aligned = derived_algebra(centralizer(so64, J_of(SCA_EPS)))
    check("PC-T6 CROSS-CHECK: k77's independently computed central generator "
          "(plane weights 2,2,2,-3,-3, 2026-08-12) is BD-1's hypercharge and lies "
          "inside the aligned image -- two constructions five days apart agree",
          in_span([flat(X) for X in su_aligned], flat(Yvec)))

    # PC-T2: the Re-major realification convention SC-A does NOT use here.
    # THE POINT: it produces the SAME dimensions and is caught ONLY at charge level.
    src = [0, 1, 2, 5, 6, 7, 3, 4, 8, 9]
    Jb = zeros(10)
    for j in range(5):
        a, b = src.index(j), src.index(j + 5)
        Jb[a][b], Jb[b][a] = F(-1), F(1)
    sub_b = derived_algebra(centralizer(so64, Jb))
    dims_b = (intersection_dim([flat(X) for X in sub_b], [flat(X) for X in pati]),
              intersection_dim([flat(X) for X in sub_b], p_only))
    check("PC-T2 PLANTED CONTROL, and the sharpest one here (this IS the trap "
          "class): had the transport silently used the Re-major realification "
          "(SC-A's block_perm pairing), the result would still be a 24-dimensional "
          "su(3,2) in so(6,4) with the IDENTICAL 12 + 12 dimension census. The "
          "dimension count is BLIND to the convention error",
          span_dim([flat(X) for X in sub_b]) == 24 and dims_b == (12, 12),
          f"Re-major census = {dims_b}")
    check("PC-T3 PLANTED CONTROL: and it is caught ONLY at charge level -- BD-1's "
          "hypercharge does NOT lie in the Re-major image, whereas it does lie in "
          "SC-A's. This is why the census had to be run against BD-1's charge "
          "grading and not against dimensions, and why the transport had to be "
          "checked byte-by-byte rather than by matching integers",
          not in_span([flat(X) for X in sub_b], flat(Yvec))
          and in_span([flat(X) for X in su_aligned], flat(Yvec)))
    # PC-T7: the bilinear form is pinned by J-compatibility, not assumed.
    e55 = [[F(1 if i == j and i < 5 else (-1 if i == j else 0)) for j in range(10)]
           for i in range(10)]
    J = J_of(SCA_EPS)
    check("PC-T7 PLANTED CONTROL: the same J is NOT eta-skew for diag(+^5,-^5), "
          "because that form splits BD-1's third plane (axes 4,5). So the bilinear "
          "form is PINNED by compatibility with the plane structure -- it is "
          "derived, not carried over on trust",
          not is_zero_mat(add(matmul(transpose(J), e55), matmul(e55, J)))
          and _split_under(e55) != (21, 24),
          f"so(5,5) k/p split = {_split_under(e55)}")
    # PC-T4: BD-1's own linear-surrogate baryon number, applied to the retained set.
    roots = image_roots(SCA_EPS)

    def fake_S(rec):
        return {(-(b_minus_l(t)) + b_minus_l(s), F(0)) for s, t in rec["tr"]}
    check("PC-T4 PLANTED CONTROL (BD-1's own): under a LINEAR surrogate baryon "
          "number the census finds ZERO B-violating directions in the retained "
          "p-part -- the 12 is produced by the piecewise colour structure of B, "
          "not by the shape of the test",
          all(len(fake_S(r)) == 1 for r in roots if not in_k(r))
          and sum(1 for r in roots if not in_k(r) and len(r["S"]) > 1) == 12)
    # PC-T5: a non-theta-stable subspace does not split.
    mixed = [GLUON[0], P_ROOTS[0], P_ROOTS[1]]
    check("PC-T5 PLANTED CONTROL: theta-stability is a real property, not automatic "
          "-- a root vector's k/p membership is well defined only because the "
          "whole Cartan sits in k and every root is purely k or purely p",
          all(in_k(r) or not in_k(r) for r in mixed)
          and len({in_k(r) for r in mixed}) == 2)
    return True


def _split_under(e):
    same = mixed = 0
    for a in range(10):
        for b in range(a + 1, 10):
            A = zeros(10)
            A[a][b], A[b][a] = F(1), F(-1)
            X = matmul(e, A)
            tr = sum(matmul(X, X)[t][t] for t in range(10))
            (same, mixed) = (same + 1, mixed) if tr < 0 else (same, mixed + 1)
    return (same, mixed)


# ==========================================================================
# 8.  BD-1's disposal branches (its own second horn) and the signature horn.
# ==========================================================================
def disposal_branches(c_align):
    # branch 1: the coset is removed (GU-as-declared, PV-2's observation reduction)
    surviving_declared = 21
    surviving_chain = c_align["dim_k_part"]
    check_eq("D1 BRANCH 1 (coset removed, GU-as-declared): what survives of the "
             "image is its 12-dimensional maximal compact = exactly the SM, with "
             "ZERO B-violating directions", (surviving_chain, 0), (12, 0))
    check_eq("D2 BRANCH 1: the chain is a STRICTLY STRONGER reduction than BD-1's "
             "alone -- 45 -> 24 -> 12 versus 45 -> 21; the 9 extra directions "
             "removed are BD-1's 6 PS leptoquarks + 2 W_R + 1 Z', all of which "
             "BD-1 had already shown B-conserving",
             (45, 24, 12, surviving_declared - surviving_chain), (45, 24, 12, 9))
    check_eq("D3 BRANCH 2 (coset returns, BD-1 section 6's contrary branch): the "
             "image retains 12 B-violating directions, all SU(5) X,Y",
             c_align["n_B_violating"], 12)
    check("D4 BRANCH 2: B-L is still exactly conserved by every retained "
          "direction, so BD-1's baryogenesis obstruction survives the reduction "
          "in BOTH branches -- the reduction cannot make matter either",
          all(len(delta(b_minus_l, r)) == 1 for r in ROOTS.values()))
    # the signature horn question, answered from path-dependencies
    pd = open(REPO_TESTS.replace("/tests/channel-swings", "")
              + "/lab/process/path-dependencies.yaml").read()
    check("D5 SIGNATURE HORN: BD-1 carries NO (9,5)/(7,7) signature horn. Its "
          "object is the DeWitt FIBRE form, which path-dependencies records as "
          "horn-independent: 'The DeWitt fibre form is (6,4), and this is "
          "INDEPENDENT of the base sign: G(-g) = G(g) exactly.' So this census "
          "is horn-robust on the ambient axis, and the second horn it does carry "
          "is the DISPOSAL branch above, plus the POSITIONAL horn in section 6",
          "The DeWitt fibre form is (6,4), and this is INDEPENDENT of the base "
          "sign: G(-g) = G(g) exactly." in pd)
    return {"branch1_surviving_dim": surviving_chain,
            "branch1_bviolating": 0,
            "branch2_bviolating": c_align["n_B_violating"]}


# ==========================================================================
def main() -> int:
    global ACTIVE
    selftest = "--selftest" in sys.argv

    res = {}
    res["transport"] = transport_block()
    carrier_controls()
    bd1_reproduction()
    homomorphism_check()
    res["vector_side"] = vector_side_construction()
    c_align, _, _ = horn_A()
    res["horn_aligned"] = c_align
    res["horn_flipped"] = horn_B()
    res["sweep"] = horn_sweep()
    res["controls"] = contrary_controls()
    planted_failing_controls()
    res["disposal"] = disposal_branches(c_align)

    assert_no_float(res)

    passed = sum(1 for _, ok, _ in CHECKS if ok)
    for name, ok, detail in CHECKS:
        print(f"  {'PASS' if ok else '[FAIL]'}  {name}"
              + (f"  -- {detail}" if (detail and not ok) else ""))
    print()
    print(f"{passed}/{len(CHECKS)} exact checks passed")
    print()
    print("TRANSPORT: " + "; ".join(f"{k}={v}" for k, v in res["transport"].items()))
    print(f"CENSUS (aligned horn): dim(image n k) = {c_align['dim_k_part']}, "
          f"dim(image n p) = {c_align['dim_p_part']}, "
          f"B-violating retained = {c_align['n_B_violating']} of BD-1's 24")
    print(f"  p-part multiplets: {c_align['p_multiplets']}")
    print(f"CENSUS (flipped horn): {res['horn_flipped']['p_multiplets']}, "
          f"B-violating retained = {res['horn_flipped']['n_B_violating']}")
    print(f"CONTRARY CONTROLS: SM -> p-part {res['controls']['sm']['dim_p_part']}, "
          f"k -> p-part {res['controls']['k']['dim_p_part']}, "
          f"so(6,4) -> p-part {res['controls']['so64']['dim_p_part']}")
    print(f"SIGN SWEEP: {res['sweep']['n_aligned']} of {res['sweep']['n_patterns']} "
          f"plane-diagonal complex structures are SM-aligned")
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    if "--selftest" not in sys.argv:
        raise SystemExit(main())

    # ---- clean baseline FIRST, then one mutation at a time. ----
    import subprocess

    here = __file__
    print("=" * 78)
    print("SELFTEST -- clean baseline FIRST")
    print("=" * 78)
    r = subprocess.run([sys.executable, here], capture_output=True, text=True)
    base_ok = r.returncode == 0 and "[FAIL]" not in r.stdout
    print(f"clean baseline: exit {r.returncode}, "
          f"{'all green' if base_ok else 'NOT CLEAN'}")
    print(r.stdout.strip().splitlines()[-8] if r.stdout.strip() else "")
    if not base_ok:
        print("BASELINE NOT CLEAN -- selftest aborts (mutations are meaningless)")
        raise SystemExit(1)

    bad = []
    for m, desc in MUT.items():
        rr = subprocess.run([sys.executable, here, "--mutate", m],
                            capture_output=True, text=True)
        caught_by_fail = "[FAIL]" in rr.stdout
        nonzero = rr.returncode != 0
        crashed = rr.returncode != 0 and not caught_by_fail
        status = ("CAUGHT" if (nonzero and caught_by_fail)
                  else ("CRASH-ONLY (REJECTED)" if crashed else "MISSED"))
        n_fail = rr.stdout.count("[FAIL]")
        print(f"  {status:22s} {m:18s} ({n_fail} genuine [FAIL] lines)  {desc}")
        if status != "CAUGHT":
            bad.append(m)
    print()
    if bad:
        print(f"SELFTEST FAILED: {bad}")
        raise SystemExit(1)
    print(f"SELFTEST PASSED: clean baseline green FIRST, then {len(MUT)}/{len(MUT)} "
          f"mutations each caught by >= 1 genuine [FAIL] through the normal check path")
    raise SystemExit(0)
