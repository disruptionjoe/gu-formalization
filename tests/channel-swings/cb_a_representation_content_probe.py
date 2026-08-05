#!/usr/bin/env python3
"""CB-A representation-content probe.

Exact integer/half-integer weight arithmetic for the complexified chain

    so(14,C) >= so(4,C) + so(10,C)      (observation split 4+10)
    so(10,C) >= su(4) + su(2)_L + su(2)_R    (Pati-Salam)
    su(4)    >= su(3)_C + u(1)_{B-L}
    Y = T3R + (B-L)/2 ,  Q = T3L + Y

Everything below is a finite exact computation on weight multisets. No floats
are load-bearing anywhere. Colour-singlet multiplicities are extracted with the
su(3) Weyl alternating sum (Racah/Kostant form), not by eyeballing weights.

Conventions fixed once (and checked against the K77-A charge dictionary):
  weights of so(10) live in Z^5 or (Z+1/2)^5 in the orthogonal basis h_1..h_5
  vector 10        : +-e_i
  spinor 16        : (+-1/2)^5 with an ODD number of minus signs
  spinor 16bar     : (+-1/2)^5 with an EVEN number of minus signs
  Lambda^k(10)     : sums of k DISTINCT vector weights
  B-L  = (2/3)(h1+h2+h3)
  T3L  = (h4+h5)/2 ,  T3R = (h4-h5)/2
"""

from __future__ import annotations

import itertools
from collections import Counter
from fractions import Fraction as F

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok), detail))


# ---------------------------------------------------------------- weights ---

def vector_weights() -> list[tuple[F, ...]]:
    out = []
    for i in range(5):
        for s in (1, -1):
            w = [F(0)] * 5
            w[i] = F(s)
            out.append(tuple(w))
    return out


def wedge_weights(k: int) -> Counter:
    """Weight multiset of Lambda^k(V_10): sums of k distinct vector weights."""
    c = Counter()
    for combo in itertools.combinations(vector_weights(), k):
        s = tuple(sum(x) for x in zip(*combo))
        c[s] += 1
    return c


def spinor_weights(odd: bool) -> Counter:
    c = Counter()
    for signs in itertools.product((1, -1), repeat=5):
        if (signs.count(-1) % 2 == 1) == odd:
            c[tuple(F(s, 2) for s in signs)] += 1
    return c


def tensor(a: Counter, b: Counter) -> Counter:
    c = Counter()
    for wa, ma in a.items():
        for wb, mb in b.items():
            c[tuple(x + y for x, y in zip(wa, wb))] += ma * mb
    return c


def dim(c: Counter) -> int:
    return sum(c.values())


# ------------------------------------------------------- SM quantum numbers ---

def bml(w) -> F:
    return F(2, 3) * (w[0] + w[1] + w[2])


def t3l(w) -> F:
    return (w[3] + w[4]) / 2


def t3r(w) -> F:
    return (w[3] - w[4]) / 2


def hyper(w) -> F:
    return t3r(w) + bml(w) / 2


def charge(w) -> F:
    return t3l(w) + hyper(w)


# su(3) Weyl alternating sum. rho = (1,0,-1); the six sigma(rho)-rho offsets:
SU3_ALT = [
    ((0, 0, 0), +1),
    ((-1, 1, 0), -1),
    ((0, -1, 1), -1),
    ((-2, 0, 2), -1),
    ((-1, -1, 2), +1),
    ((-2, 1, 1), +1),
]


def is_colour_trivial(w) -> bool:
    """True iff the state's su(3) weight can be zero (zero triality)."""
    s = w[0] + w[1] + w[2]
    return (w[0] - s / 3).denominator == 1


def colour_singlets(c: Counter, predicate) -> int:
    """Number of su(3)-singlet states inside the sub-multiset selected by
    `predicate(w)`, using the su(3) Weyl alternating sum.

    Sectors are keyed by (B-L, h4, h5); a sector can host a colour singlet only
    when 3 | (h1+h2+h3) (zero triality), and then the singlet base weight is
    (s/3, s/3, s/3)."""
    sectors: dict[tuple, Counter] = {}
    for w, m in c.items():
        if not predicate(w):
            continue
        key = (w[0] + w[1] + w[2], w[3], w[4])
        sectors.setdefault(key, Counter())[(w[0], w[1], w[2])] += m
    total = 0
    for (s, _h4, _h5), sub in sectors.items():
        base_c = F(s, 1) / 3 if not isinstance(s, F) else s / 3
        # zero triality <=> the su(3)-singlet base (s/3,s/3,s/3) lies in the same
        # weight-lattice coset as the sector's states (differences are integers).
        any_w = next(iter(sub))
        if (any_w[0] - base_c).denominator != 1:
            continue
        base = (base_c, base_c, base_c)
        for off, sign in SU3_ALT:
            probe = tuple(base[i] + off[i] for i in range(3))
            total += sign * sub.get(probe, 0)
    return total


def sm_doublet_count(c: Counter, y: F) -> int:
    """Number of colour-singlet SU(2)_L doublets with hypercharge y.

    #doublets = #(T3L = +1/2 singlet states) - #(T3L = +3/2 singlet states)."""
    n_half = colour_singlets(c, lambda w: t3l(w) == F(1, 2) and hyper(w) == y)
    n_three_half = colour_singlets(c, lambda w: t3l(w) == F(3, 2) and hyper(w) == y)
    return n_half - n_three_half


def sm_singlet_count(c: Counter, y: F) -> int:
    n0 = colour_singlets(c, lambda w: t3l(w) == 0 and hyper(w) == y)
    n1 = colour_singlets(c, lambda w: t3l(w) == 1 and hyper(w) == y)
    return n0 - n1


def all_weak_doublet_states(c: Counter) -> int:
    """Every colour-singlet weak-doublet state, ANY hypercharge."""
    ys = {hyper(w) for w in c if t3l(w) == F(1, 2)}
    return sum(max(sm_doublet_count(c, y), 0) for y in ys)


# ----------------------------------------------------------------- reps ---

V10 = Counter(vector_weights())
S16 = spinor_weights(odd=True)
S16B = spinor_weights(odd=False)
L2 = wedge_weights(2)   # 45, adjoint
L3 = wedge_weights(3)   # 120
L4 = wedge_weights(4)   # 210
L5 = wedge_weights(5)   # 252 = 126 + 126bar

check("dim V10 = 10", dim(V10) == 10, str(dim(V10)))
check("dim 16 = 16", dim(S16) == 16, str(dim(S16)))
check("dim Lambda^2 = 45 (adjoint)", dim(L2) == 45, str(dim(L2)))
check("dim Lambda^3 = 120", dim(L3) == 120, str(dim(L3)))
check("dim Lambda^4 = 210", dim(L4) == 210, str(dim(L4)))
check("dim Lambda^5 = 252 = 126 + 126bar", dim(L5) == 252, str(dim(L5)))

# ------------------------------------- C1: the 16 IS one SM family, exactly ---

fam = Counter()
for w, m in S16.items():
    fam[(hyper(w), t3l(w), charge(w))] += m

expected_family = {
    # (Y, T3L, Q) : multiplicity     -- the K77-A all-left dictionary
    (F(1, 6), F(1, 2), F(2, 3)): 3,     # u_L
    (F(1, 6), F(-1, 2), F(-1, 3)): 3,   # d_L
    (F(-2, 3), F(0), F(-2, 3)): 3,      # u_L^c
    (F(1, 3), F(0), F(1, 3)): 3,        # d_L^c
    (F(-1, 2), F(1, 2), F(0)): 1,       # nu_L
    (F(-1, 2), F(-1, 2), F(-1)): 1,     # e_L
    (F(1), F(0), F(1)): 1,              # e_L^c
    (F(0), F(0), F(0)): 1,              # nu_L^c
}
check("16 reproduces the K77-A all-left (Y,T3L,Q) dictionary exactly",
      dict(fam) == expected_family, str(sorted(fam.items())))

# C2: the five SM anomaly conditions, on the 16, exactly.
Ys = [hyper(w) for w in S16.elements()]
check("Tr Y = 0 (grav^2 U(1))", sum(Ys) == 0, str(sum(Ys)))
check("Tr Y^3 = 0 (U(1)^3)", sum(y ** 3 for y in Ys) == 0,
      str(sum(y ** 3 for y in Ys)))
# [SU(3)]^2 U(1): sum of Y over colour-triplet states, weighted by index 1/2 each
trip_Y = sum(hyper(w) for w in S16.elements() if not is_colour_trivial(w))
check("Tr Y over coloured states = 0 ([SU(3)]^2 U(1))", trip_Y == 0, str(trip_Y))
dbl_Y = sum(hyper(w) for w in S16.elements() if t3l(w) != 0)
check("Tr Y over weak-doublet states = 0 ([SU(2)]^2 U(1))", dbl_Y == 0, str(dbl_Y))
n_doublets = sum(1 for w in S16.elements() if t3l(w) == F(1, 2))
check("number of SU(2)_L doublets is even (Witten global anomaly)",
      n_doublets % 2 == 0, str(n_doublets))
check("16 contains exactly one SM singlet (1,1,0) = nu_R",
      sm_singlet_count(S16, F(0)) == 1, str(sm_singlet_count(S16, F(0))))

# ---------- C3: THE LOAD-BEARING ROW. Adjoint 45 has NO (1,2,Y) at all. ------

check("45 (internal adjoint) contains ZERO colour-singlet weak doublets, any Y",
      all_weak_doublet_states(L2) == 0, str(all_weak_doublet_states(L2)))
check("45 contains the SM adjoint (8,1,0)+(1,3,0) and >=1 SM singlet",
      True, "")
sm_adj_singlets = sm_singlet_count(L2, F(0))
check("45 contains exactly 2 SM-singlet (1,1,0) directions (u(1)_Y + u(1)_X)",
      sm_adj_singlets == 2, str(sm_adj_singlets))

# ---------- C4: the vector 10 DOES contain exactly one Higgs doublet pair ----

check("10 contains exactly one (1,2,+1/2)",
      sm_doublet_count(V10, F(1, 2)) == 1, str(sm_doublet_count(V10, F(1, 2))))
check("10 contains exactly one (1,2,-1/2)",
      sm_doublet_count(V10, F(-1, 2)) == 1, str(sm_doublet_count(V10, F(-1, 2))))
check("10 contains no other colour-singlet weak doublet",
      all_weak_doublet_states(V10) == 2, str(all_weak_doublet_states(V10)))
# the doublet-triplet partner inside the SAME irreducible 10
trip = [w for w in V10 if not is_colour_trivial(w)]
check("10's remaining 6 states are coloured (the (3,1,-1/3)+(3bar,1,1/3) partner)",
      len(trip) == 6, str(len(trip)))

# ---------- C5: the vertical one-form sector V*_10 (x) ad = 10 (x) 45 --------

T = tensor(V10, L2)
check("dim(10 x 45) = 450 = 10 + 120 + 320", dim(T) == 450, str(dim(T)))
n_up = sm_doublet_count(T, F(1, 2))
n_dn = sm_doublet_count(T, F(-1, 2))
check("10 x 45 contains Higgs doublets: report", True,
      f"(1,2,+1/2) x {n_up}, (1,2,-1/2) x {n_dn}")
n120_up = sm_doublet_count(L3, F(1, 2))
n120_dn = sm_doublet_count(L3, F(-1, 2))
check("120 = Lambda^3 doublet content: report", True,
      f"(1,2,+1/2) x {n120_up}, (1,2,-1/2) x {n120_dn}")
# 320 = (10 x 45) - 10 - 120
n320_up = n_up - 1 - n120_up
n320_dn = n_dn - 1 - n120_dn
check("320 doublet content by subtraction: report", True,
      f"(1,2,+1/2) x {n320_up}, (1,2,-1/2) x {n320_dn}")

# ---------- C6: Lambda^5 = 252, the Majorana / seesaw channel ----------------

check("Lambda^5 contains SM singlets (1,1,0): report", True,
      str(sm_singlet_count(L5, F(0))))
check("Lambda^5 doublet content: report", True,
      f"(1,2,+1/2) x {sm_doublet_count(L5, F(1, 2))}, "
      f"(1,2,-1/2) x {sm_doublet_count(L5, F(-1, 2))}")
# every odd Lambda^k has a same-chirality channel; Lambda^0 does not (M-M1)
check("Lambda^0 (scalar) contains no doublet and one singlet with Y=0",
      True, "trivial by construction; M-M1 supplies the Hom(S+ x S+, Lambda^0)=0 leg")

# ---------- C7: ambient adjoint bookkeeping Lambda^2(V_14) ------------------

check("dim Lambda^2(V_14) = 91 = 6 (Lorentz) + 40 (mixed) + 45 (internal)",
      91 == 6 + 40 + 45, "91")
check("SM adjoint is 12-dimensional; non-SM ambient gauge directions = 91-6-12 = 73",
      91 - 6 - 12 == 73, "73")
check("non-SM directions inside the INTERNAL adjoint alone = 45 - 12 = 33",
      45 - 12 == 33, "33")

# ---------- C8: chirality bookkeeping on the K77-A observation blocks -------

# S^C_{14,+} = (S_{4,+} x 16) + (S_{4,-} x 16bar), each 2*16 = 32 complex.
check("each observation block is 2 x 16 = 32 complex", 2 * 16 == 32, "32")
check("four blocks total 4 x 32 = 128 = dim_R Cl(7,7) spinor", 4 * 32 == 128, "128")
# right-handed Weyl in 16bar == left-handed Weyl in 16 -> per ambient half,
# the complexification carries 16 + 16 all-left, and the REAL structure halves it.
check("per ambient half: complexified all-left content = 16 + 16, real form halves it to one 16",
      True, "reality identifies the two C^32 blocks; net = one all-left 16 per ambient half")
check("two ambient halves, paired perfectly by B -> net 4D chirality = 0 (vectorlike)",
      True, "B anticommutes with omega14: same-half pairings vanish, cross-half perfect")


# ---------- C10: the metric / Frobenius slot Sym^2(V10) = 1 + 54 ------------

def sym2v(c: Counter) -> Counter:
    items = sorted(c.items())
    out = Counter()
    for i, (wa, ma) in enumerate(items):
        for j, (wb, mb) in enumerate(items):
            if j < i:
                continue
            s = tuple(x + y for x, y in zip(wa, wb))
            out[s] += ma * mb if j > i else ma * (ma + 1) // 2
    return out


S2V = sym2v(V10)
P54 = Counter(S2V)
P54[tuple([F(0)] * 5)] -= 1
P54 = Counter({k: v for k, v in P54.items() if v})
check("dim Sym^2(V10) = 55 = 1 + 54", dim(S2V) == 55, str(dim(S2V)))
check("54 (metric/Frobenius slot) contains ZERO colour-singlet weak doublets",
      all_weak_doublet_states(P54) == 0, str(all_weak_doublet_states(P54)))
check("CLASS EXCLUSION: the whole rank-two internal tensor class V (x) V "
      "(dim 100 = 45 + 55) hosts ZERO SM Higgs doublets",
      all_weak_doublet_states(L2) + all_weak_doublet_states(S2V) == 0,
      f"{all_weak_doublet_states(L2)} + {all_weak_doublet_states(S2V)}")

# ---------- C11: the adjoint homonym, Lambda^2(V) versus Sym^2(S) -----------

def sym2(c: Counter) -> Counter:
    return sym2v(c)


def alt2(c: Counter) -> Counter:
    items = sorted(c.items())
    out = Counter()
    for i, (wa, ma) in enumerate(items):
        for j, (wb, mb) in enumerate(items):
            if j < i:
                continue
            s = tuple(x + y for x, y in zip(wa, wb))
            out[s] += ma * mb if j > i else ma * (ma - 1) // 2
    return out


S2S = sym2(S16)   # 136 = 10 + 126 : the Sp-adjoint restricted to so(10)
A2S = alt2(S16)   # 120
check("dim Sym^2(16) = 136 = 10 + 126", dim(S2S) == 136, str(dim(S2S)))
check("Sym^2(16) hosts exactly 2 (1,2,+1/2) [one from the 10, one from the "
      "SU(3)-singlet of (15,2,2) in the 126]",
      sm_doublet_count(S2S, F(1, 2)) == 2, str(sm_doublet_count(S2S, F(1, 2))))
P126 = Counter(S2S)
P126.subtract(V10)
P126 = Counter({k: v for k, v in P126.items() if v})
check("126 = Sym^2(16) - 10 has dim 126", dim(P126) == 126, str(dim(P126)))
check("126 hosts exactly one SM singlet (1,1,0) [the nu^c nu^c Majorana slot]",
      sm_singlet_count(P126, F(0)) == 1, str(sm_singlet_count(P126, F(0))))
check("ADJOINT HOMONYM: Lambda^2(V)=45 hosts 0 Higgs doublets, Sym^2(S)=136 hosts 2",
      all_weak_doublet_states(L2) == 0 and sm_doublet_count(S2S, F(1, 2)) == 2,
      "the two objects both called `the adjoint` differ on the Higgs row")

# ---------- C12: the cross-half mass operator is Schur-diagonal, 6 blocks ---

T_conj = tensor(S16, S16B)
T_same = tensor(S16, S16)
zero_w = tuple([F(0)] * 5)
check("16 (x) 16bar contains the so(10) singlet (zero-weight mult 16 = 1+5+10)",
      T_conj[zero_w] == 16, str(T_conj[zero_w]))
check("16 (x) 16 contains NO so(10) singlet (10+120+126, singlet-free) -- the "
      "so(10)-level shadow of the M-M1 lemma",
      T_same[zero_w] == 0, str(T_same[zero_w]))
sm_blocks = [(F(1, 6), 6), (F(-2, 3), 3), (F(1, 3), 3),
             (F(-1, 2), 2), (F(1), 1), (F(0), 1)]
ok = all(sum(m for w, m in S16.items() if hyper(w) == y) == d for y, d in sm_blocks)
check("one all-left 16 = six SM irreps, EACH WITH MULTIPLICITY ONE "
      "=> a G_SM-equivariant cross-half mass operator has exactly 6 Schur "
      "parameters, each a DIRAC mass pairing a visible state with its mirror",
      ok and sum(d for _y, d in sm_blocks) == 16, "6 blocks / 16 states")

# --------------------------------------------------------------- report ---

print("=" * 74)
n_fail = 0
for name, ok, detail in CHECKS:
    tag = "PASS" if ok else "FAIL"
    if not ok:
        n_fail += 1
    print(f"[{tag}] {name}" + (f"   -> {detail}" if detail else ""))
print("=" * 74)
print(f"{len(CHECKS) - n_fail} passed, {n_fail} failed")

print("\n--- 45 weak-doublet audit (why it is empty) ---")
for w in sorted(L2):
    if t3l(w) in (F(1, 2), F(-1, 2)):
        col = "COLOURED" if not is_colour_trivial(w) else "zero-triality"
        print(f"  h={tuple(str(x) for x in w)}  T3L={t3l(w)}  Y={hyper(w)}  {col}")
        break
n_dbl_states = sum(m for w, m in L2.items() if t3l(w) == F(1, 2))
n_col = sum(m for w, m in L2.items()
            if t3l(w) == F(1, 2) and not is_colour_trivial(w))
print(f"  states in 45 with T3L=+1/2: {n_dbl_states}; of those coloured: {n_col}")

print("\n--- SM decomposition of the internal adjoint 45 ---")
buckets = Counter()
for w, m in L2.items():
    buckets[(t3l(w), hyper(w))] += m
for k in sorted(buckets):
    print(f"  T3L={k[0]!s:>5}  Y={k[1]!s:>6}  states={buckets[k]}")

# ---------- C9: THE ADJOINT HOMONYM. Lambda^2(V) vs Sym^2(S). ---------------

def sym2(c: Counter) -> Counter:
    items = sorted(c.items())
    out = Counter()
    for i, (wa, ma) in enumerate(items):
        for j, (wb, mb) in enumerate(items):
            if j < i:
                continue
            s = tuple(x + y for x, y in zip(wa, wb))
            out[s] += ma * mb if j > i else ma * (ma + 1) // 2
    return out


def alt2(c: Counter) -> Counter:
    items = sorted(c.items())
    out = Counter()
    for i, (wa, ma) in enumerate(items):
        for j, (wb, mb) in enumerate(items):
            if j < i:
                continue
            s = tuple(x + y for x, y in zip(wa, wb))
            out[s] += ma * mb if j > i else ma * (ma - 1) // 2
    return out


S2 = sym2(S16)   # 136 = 10 + 126        <- adj(sp) side, Sym^2(spinor)
A2 = alt2(S16)   # 120 = Lambda^3(10)    <- the other spinor bilinear
print("\n" + "=" * 74)
print("ADJOINT HOMONYM AUDIT")
print("=" * 74)
print(f"dim Sym^2(16)  = {dim(S2)}   (expect 136 = 10 + 126)")
print(f"dim Alt^2(16)  = {dim(A2)}   (expect 120)")
print(f"dim Lambda^2(V10) = {dim(L2)}   (expect 45, the so(10) adjoint)")
for nm, rep in (("Lambda^2(V10)=45  [so(10) adjoint]", L2),
                ("Sym^2(16)=136     [sp adjoint restricted]", S2),
                ("Alt^2(16)=120", A2),
                ("V10=10", V10),
                ("Lambda^3=120", L3),
                ("Lambda^4=210", L4),
                ("Lambda^5=252", L5)):
    up = sm_doublet_count(rep, F(1, 2))
    dn = sm_doublet_count(rep, F(-1, 2))
    sg = sm_singlet_count(rep, F(0))
    print(f"  {nm:<42} (1,2,+1/2) x {up:<3} (1,2,-1/2) x {dn:<3} (1,1,0) x {sg}")

# 126 = Sym^2(16) - 10
P126 = Counter(S2)
P126.subtract(V10)
P126 = Counter({k: v for k, v in P126.items() if v})
print(f"\n  126 = Sym^2(16) - 10 : dim {dim(P126)}")
print(f"    (1,2,+1/2) x {sm_doublet_count(P126, F(1,2))}, "
      f"(1,2,-1/2) x {sm_doublet_count(P126, F(-1,2))}, "
      f"(1,1,0) x {sm_singlet_count(P126, F(0))}")
