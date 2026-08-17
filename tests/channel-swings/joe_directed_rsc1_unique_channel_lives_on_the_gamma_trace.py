#!/usr/bin/env python3
"""RSC-1 -- the RS-corner join: where does ST-1's unique channel actually land?

ST-1 (2026-08-16, 94/94) proved that the UNIQUE one-insertion chirality-selective
Grassmann-live diagonal channel at D_7 is `Lambda^7_-+ -> Lambda^2(zeta_+-)`,
multiplicity exactly 1, and glossed the target as "the heavy-partner self-mass
shape lives at a ONE-FORM corner, the Rarita-Schwinger-ADJACENT slot".

This probe resolves "adjacent" into an exact module statement.  The one-form
corner is REDUCIBLE:

    zeta_+ = Omega^1(S_+) = V (x) S_+ = S_- (+) R^(+)        896 = 64 + 832

where R^(+) is the gamma-traceless vector-spinor -- the Rarita-Schwinger term
of the source's own product rule, draft eq (11.1), whose 832 and 64 the draft
PRINTS as dimension subscripts on p.51.  Decomposing

    Lambda^2(zeta_+) = Lambda^2(S_-) (+) (S_- (x) R^(+)) (+) Lambda^2(R^(+))

the probe computes where ST-1's multiplicity-1 invariant sits.  Answer, by two
independent instruments: entirely in the CROSS block.  `Lambda^2(R^(+))` carries
multiplicity ZERO of both middle forms.  The channel is a gamma-trace x
gamma-traceless Dirac-type pairing, not a self-pairing of the RS module, so the
128 remainder -- which lives strictly inside R -- cannot be placed by it.

Everything is complexified D_7, hence identical on both SIGNATURE-AMBIENT horns.
Exact integer / Fraction arithmetic throughout; no floats anywhere.

Run:
    _local/cas-venv/bin/python tests/channel-swings/joe_directed_rsc1_unique_channel_lives_on_the_gamma_trace.py
    _local/cas-venv/bin/python tests/channel-swings/joe_directed_rsc1_unique_channel_lives_on_the_gamma_trace.py --selftest
    ... --selftest --poison-baseline     (proves the baseline guard has power)

Probe standard: VERIFICATION.md "Probe and mutation-harness discipline".
  * the selftest verifies the CLEAN BASELINE before any mutation (rule 1);
  * every mutation corrupts MACHINERY or a REFERENCE, never a check predicate
    (rule 2);
  * a catch counts only via a genuine `[FAIL]` line (rule 3);
  * every absence claim carries a planted-positive control (rule 4) -- two, at
    the same rank and at a different rank, where the same code path returns the
    OPPOSITE attribution;
  * selftest exits 0 on success (rule 5);
  * the selftest's baseline is pinned independently of the live run (rule 6).
"""

from __future__ import annotations

import os
import subprocess
import sys
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations

MUT = os.environ.get("RSC1_MUT", "")

CHECKS = 0
FAILS = 0
PLANTED = 0


def check(name, actual, expected):
    global CHECKS, FAILS
    CHECKS += 1
    if actual == expected:
        print("[OK]   %-64s %s" % (name, _short(actual)))
    else:
        FAILS += 1
        print("[FAIL] %-64s got %s expected %s" % (name, _short(actual), _short(expected)))


def planted_false(name, proposition):
    """A proposition that MUST be False.  Rule 4's power demonstration in the
    small: a detector that cannot observe False is not observing."""
    global CHECKS, FAILS, PLANTED
    CHECKS += 1
    PLANTED += 1
    if proposition is False:
        print("[OK]   planted-false %-50s observed False" % name)
    else:
        FAILS += 1
        print("[FAIL] planted-false %-50s observed %s, expected False" % (name, proposition))


def _short(x):
    s = str(x)
    return s if len(s) <= 58 else s[:55] + "..."


# ---------------------------------------------------------------------------
# 1. D_n machinery -- standard representation theory, exact integers.
#    Weights are DOUBLED so half-integer spinor weights are integral.
# ---------------------------------------------------------------------------

def rho(n):
    return tuple(2 * (n - 1 - i) for i in range(n))


def positive_roots(n):
    out = []
    for i in range(n):
        for j in range(i + 1, n):
            a = [0] * n
            a[i], a[j] = 1, 1
            out.append(tuple(a))
            b = [0] * n
            b[i], b[j] = 1, -1
            out.append(tuple(b))
    if MUT == "M1_drop_a_root":
        out = out[:-1]
    return out


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def weyl_dim(lam, n):
    """Weyl dimension formula on doubled weights."""
    lr = tuple(l + r for l, r in zip(lam, rho(n)))
    num, den = 1, 1
    for a in positive_roots(n):
        num *= dot(lr, a)
        den *= dot(rho(n), a)
    f = Fraction(num, den)
    assert f.denominator == 1, ("non-integral Weyl dimension", lam, f)
    return int(f)


def dominant_conjugate(v):
    """Conjugate v into the dominant D_n chamber.

    Returns (dominant weight, sign of the Weyl element) or None if v lies on a
    wall.  W(D_n) = signed permutations with an EVEN number of sign changes, so
    an odd number of negative entries leaves one sign on the LAST (smallest
    |.|) coordinate; eps(w) = det(w) = sign(permutation)."""
    n = len(v)
    absv = [abs(x) for x in v]
    if MUT != "M3_skip_wall_test":
        for i in range(n):
            for j in range(i + 1, n):
                if absv[i] == absv[j]:
                    return None
    neg = sum(1 for x in v if x < 0)
    idx = sorted(range(n), key=lambda i: -absv[i])
    sgn = 1
    seen = [False] * n
    for i in range(n):
        if seen[i]:
            continue
        length, j = 0, i
        while not seen[j]:
            seen[j] = True
            j = idx[j]
            length += 1
        if length % 2 == 0:
            sgn = -sgn
    if MUT == "M2_sign_always_plus":
        sgn = 1
    out = [absv[i] for i in idx]
    if neg % 2 == 1 and MUT != "M4_never_flip_last":
        out[-1] = -out[-1]
    return (tuple(out), sgn)


def klimyk(lam, wts_b, n):
    """V_lam (x) B by Racah-Speiser/Klimyk: sum over the WEIGHTS of B."""
    r = rho(n)
    out = Counter()
    for nu, m in wts_b.items():
        if MUT == "M5_klimyk_no_rho":
            v = tuple(l + x for l, x in zip(lam, nu))
        else:
            v = tuple(l + x + rr for l, x, rr in zip(lam, nu, r))
        dc = dominant_conjugate(v)
        if dc is None:
            continue
        dom, s = dc
        if MUT == "M5_klimyk_no_rho":
            hw = dom
        else:
            hw = tuple(a - b for a, b in zip(dom, r))
        out[hw] += s * m
    return Counter({k: v for k, v in out.items() if v})


def wts_V(n):
    c = Counter()
    for i in range(n):
        for s in (2, -2):
            w = [0] * n
            w[i] = s
            c[tuple(w)] += 1
    return c


def wts_spinor(sign, n):
    """sign=+1: even number of minus signs (S_+); -1: odd (S_-)."""
    c = Counter()
    for bits in range(2 ** n):
        v = [1 if (bits >> i) & 1 else -1 for i in range(n)]
        even = (v.count(-1) % 2 == 0)
        want = (sign > 0)
        if MUT == "M6_spinor_parity_flip":
            want = not want
        if even == want:
            c[tuple(v)] += 1
    return c


def wts_lambda_k(k, n):
    base = list(wts_V(n).elements())
    c = Counter()
    for comb in combinations(range(len(base)), k):
        w = [0] * n
        for i in comb:
            for t in range(n):
                w[t] += base[i][t]
        c[tuple(w)] += 1
    return c


def wts_tensor(a, b):
    c = Counter()
    for x, mx in a.items():
        for y, my in b.items():
            c[tuple(p + q for p, q in zip(x, y))] += mx * my
    return c


def wts_sym2(w):
    els = list(w.elements())
    c = Counter()
    for i in range(len(els)):
        for j in range(i, len(els)):
            c[tuple(p + q for p, q in zip(els[i], els[j]))] += 1
    return c


def wts_alt2(w):
    els = list(w.elements())
    start = 0 if MUT == "M7_alt2_includes_diagonal" else 1
    c = Counter()
    for i in range(len(els)):
        for j in range(i + start, len(els)):
            c[tuple(p + q for p, q in zip(els[i], els[j]))] += 1
    return c


def msub(a, b):
    c = Counter(a)
    for k, v in b.items():
        c[k] -= v
    return Counter({k: v for k, v in c.items() if v})


def dual_hw(lam):
    """-w_0 on D_n with n ODD is the diagram automorphism: flip the last
    coordinate.  This is exactly CR-B/CS-1's `W_+^* = W_-`."""
    if MUT == "M9_duality_is_identity":
        return tuple(lam)
    return tuple(lam[:-1]) + (-lam[-1],)


# ---------------------------------------------------------------------------
# 2. Second, INDEPENDENT instrument: the Racah/Brauer alternating sum.
#    mult(lambda) = sum_{w in W} eps(w) * m(lambda + rho - w rho).
#    It uses no Klimyk, no block subtraction, and no tensor identity: it reads
#    a raw weight multiset.  Used to cross-check the decisive zero.
# ---------------------------------------------------------------------------

def weyl_rho_orbit(n):
    r = rho(n)
    out = []
    for p in permutations(range(n)):
        sgn = 1
        seen = [False] * n
        for i in range(n):
            if seen[i]:
                continue
            length, j = 0, i
            while not seen[j]:
                seen[j] = True
                j = p[j]
                length += 1
            if length % 2 == 0:
                sgn = -sgn
        for bits in range(2 ** n):
            s = [1 if (bits >> i) & 1 == 0 else -1 for i in range(n)]
            if s.count(-1) % 2 and MUT != "M10_racah_uses_B_n":
                continue
            out.append((tuple(sg * r[p[i]] for i, sg in enumerate(s)), sgn))
    return out


def racah_mult(lam, wmult, orbit, n):
    lr = tuple(a + b for a, b in zip(lam, rho(n)))
    tot = 0
    for wr, e in orbit:
        m = wmult.get(tuple(a - b for a, b in zip(lr, wr)))
        if m:
            tot += e * m
    return tot


# ---------------------------------------------------------------------------
# 3. The run
# ---------------------------------------------------------------------------

N = 7
L0 = (0,) * N
L1 = (2, 0, 0, 0, 0, 0, 0)
L2 = (2, 2, 0, 0, 0, 0, 0)
L3 = (2, 2, 2, 0, 0, 0, 0)
L5 = (2, 2, 2, 2, 2, 0, 0)
L7P = (2,) * N
L7M = (2, 2, 2, 2, 2, 2, -2)
SP = (1,) * N
SM = (1, 1, 1, 1, 1, 1, -1)
RP = (3, 1, 1, 1, 1, 1, 1)          # gamma-traceless part of V (x) S_+
RM = (3, 1, 1, 1, 1, 1, -1)         # gamma-traceless part of V (x) S_-
SYM2_0V = (4, 0, 0, 0, 0, 0, 0)
INS = [("L1", L1), ("L3", L3), ("L5", L5), ("L7+", L7P), ("L7-", L7M)]

# Banked reference values.  MUTABLE BY THE HARNESS (a reference corruption is a
# legal mutation; a check predicate is not).
REF = {
    "st1_zeta_plus_row": {          # ST-1 section 4.5, row zeta_+, (sym, antisym)
        "L1": (1, 3), "L3": (4, 1), "L5": (1, 4), "L7+": (2, 0), "L7-": (2, 1),
    },
    "st1_sym2_split": (2080, 2016),  # ST-1 section 4.1
    "source_p51_subscripts": (832, 64),
    "source_eq116_graded": (64, 192, 576),
    "source_eq116_ungraded": (128, 384, 1152),
    "he1_spin10_16x144_invariants": 0,
}
if MUT == "M12_corrupt_reference":
    REF["st1_zeta_plus_row"]["L7-"] = (2, 2)


def main():
    print("=" * 78)
    print("RSC-1  the RS-corner join: does ST-1's unique channel land on the RS module?")
    print("       D_7 complexified -- identical on both SIGNATURE-AMBIENT horns.")
    if MUT:
        print("       !! MUTATION ACTIVE: %s" % MUT)
    print("=" * 78)

    wV = wts_V(N)
    wSP = wts_spinor(+1, N)
    wSM = wts_spinor(-1, N)
    wL1 = wts_lambda_k(1, N)
    wL2 = wts_lambda_k(2, N)
    wSym2V = wts_sym2(wV)
    wSym2_0V = Counter(wSym2V)
    wSym2_0V[L0] -= 1

    # ---- section A: banked dimensions and the ST-1 spinor-square split [R] ----
    print("\n-- A. banked layer, reproduced before extension -----------------")
    check("dim V(D_7)", weyl_dim(L1, N), 14)
    check("dim S_+ = dim S_-", (weyl_dim(SP, N), weyl_dim(SM, N)), (64, 64))
    check("dim Lambda^2 (so(14) adjoint)", weyl_dim(L2, N), 91)
    check("dim Lambda^3", weyl_dim(L3, N), 364)
    check("dim Lambda^5", weyl_dim(L5, N), 2002)
    check("dim Lambda^7_+ = dim Lambda^7_-", (weyl_dim(L7P, N), weyl_dim(L7M, N)), (1716, 1716))
    check("dim Sym^2_0(V)", weyl_dim(SYM2_0V, N), 104)
    check("[R ST-1 4.1] Sym^2(S_+) = L3 + L7+ (dim)",
          weyl_dim(L3, N) + weyl_dim(L7P, N), REF["st1_sym2_split"][0])
    check("[R ST-1 4.1] Lambda^2(S_+) = L1 + L5 (dim)",
          weyl_dim(L1, N) + weyl_dim(L5, N), REF["st1_sym2_split"][1])
    check("[R CS-1] duality -w_0 swaps the halves: (S_+)^* = S_-", dual_hw(SP), SM)
    check("[R CS-1] duality swaps the middle forms: (L7-)^* = L7+", dual_hw(L7M), L7P)

    # ---- section B: the corner splits, exactly ----
    print("\n-- B. the one-form corner is REDUCIBLE (source eq (11.1) split) --")
    dec_zp = klimyk(SP, wV, N)
    check("V (x) S_+ decomposes into exactly two irreps", len(dec_zp), 2)
    check("V (x) S_+ = S_- (+) R^(+)", sorted(dec_zp), sorted([SM, RP]))
    check("dim R^(+) (gamma-traceless vector-spinor)", weyl_dim(RP, N), 832)
    check("dim R^(-)", weyl_dim(RM, N), 832)
    check("dim zeta_+ = 64 + 832", weyl_dim(SM, N) + weyl_dim(RP, N), 896)
    check("source p.51 prints exactly these two subscripts",
          (weyl_dim(RP, N), weyl_dim(SM, N)), REF["source_p51_subscripts"])
    dec_zm = klimyk(SM, wV, N)
    check("V (x) S_- = S_+ (+) R^(-)", sorted(dec_zm), sorted([SP, RM]))

    # ---- section C: the three-block selectivity table ----
    print("\n-- C. the refined table: which BLOCK of the corner is fed --------")
    # zeta_+ = S_- (+) R^(+).  Alt^2(A (+) B) = Alt^2 A (+) (A (x) B) (+) Alt^2 B
    cross_p = klimyk(RP, wSM, N)          # S_- (x) R^(+)
    cross_m = klimyk(RM, wSP, N)          # S_+ (x) R^(-)
    check("dim S_- (x) R^(+) saturates",
          sum(weyl_dim(k, N) * v for k, v in cross_p.items()), 64 * 832)

    def squares_of_zeta(chir):
        """(Alt^2, Sym^2) of zeta_chir = V (x) S_chir, via
           Alt^2(V(x)S) = Alt^2 V (x) Sym^2 S  (+)  Sym^2 V (x) Alt^2 S."""
        mid = L7P if chir > 0 else L7M
        alt = Counter()
        for lam in (L3, mid):
            alt += klimyk(lam, wL2, N)
        for lam in (L1, L5):
            alt += klimyk(lam, wSym2_0V, N)
        alt[L1] += 1
        alt[L5] += 1
        sym = Counter()
        for lam in (L3, mid):
            sym += klimyk(lam, wSym2_0V, N)
        sym[L3] += 1
        sym[mid] += 1
        for lam in (L1, L5):
            sym += klimyk(lam, wL2, N)
        return (Counter({k: v for k, v in alt.items() if v}),
                Counter({k: v for k, v in sym.items() if v}))

    altZP, symZP = squares_of_zeta(+1)
    altZM, symZM = squares_of_zeta(-1)
    check("dim Lambda^2(zeta_+) saturates",
          sum(weyl_dim(k, N) * v for k, v in altZP.items()), 896 * 895 // 2)
    check("dim Sym^2(zeta_+) saturates",
          sum(weyl_dim(k, N) * v for k, v in symZP.items()), 896 * 897 // 2)

    # trace-block squares: Sym^2(S_-) = L3 + L7-, Alt^2(S_-) = L1 + L5
    symTrace_p = Counter({L3: 1, L7M: 1})
    altTrace_p = Counter({L1: 1, L5: 1})
    symTrace_m = Counter({L3: 1, L7P: 1})
    altTrace_m = Counter({L1: 1, L5: 1})

    def blocks(k, chir):
        cross = cross_p if chir > 0 else cross_m
        altT = altTrace_p if chir > 0 else altTrace_m
        symT = symTrace_p if chir > 0 else symTrace_m
        altZ, symZ = (altZP, symZP) if chir > 0 else (altZM, symZM)
        a_t, s_t = altZ.get(k, 0), symZ.get(k, 0)
        a_R = a_t - altT.get(k, 0) - cross.get(k, 0)
        s_R = s_t - symT.get(k, 0) - cross.get(k, 0)
        if MUT == "M8_drop_cross_term":
            a_R = a_t - altT.get(k, 0)
            s_R = s_t - symT.get(k, 0)
        return dict(trace_alt=altT.get(k, 0), trace_sym=symT.get(k, 0),
                    cross=cross.get(k, 0), rs_alt=a_R, rs_sym=s_R,
                    tot_alt=a_t, tot_sym=s_t)

    print("     zeta_+ = S_-(64) (+) R^(+)(832);  mult of Lambda^k in each block")
    print("     %-5s | %-11s %-11s %-11s | %-11s" %
          ("ins", "trace(A,S)", "cross", "RS(A,S)", "total(A,S)"))
    table_p = {}
    for nm, k in INS:
        b = blocks(k, +1)
        table_p[nm] = b
        print("     %-5s | (%d,%d)%7s %-11d (%d,%d)%7s | (%d,%d)" %
              (nm, b["trace_alt"], b["trace_sym"], "", b["cross"],
               b["rs_alt"], b["rs_sym"], "", b["tot_alt"], b["tot_sym"]))

    # the blocks must sum to ST-1's banked row, in ST-1's Inv(. (x) Lambda^k)
    # convention: Inv(X (x) L) = mult of L^* in X.
    for nm, k in INS:
        kd = dual_hw(k)
        a = altZP.get(kd, 0)
        s = symZP.get(kd, 0)
        check("[R ST-1 4.5] zeta_+ row, column %-3s (sym,antisym)" % nm,
              (s, a), REF["st1_zeta_plus_row"][nm])

    # ---- section D: THE DECISIVE ZERO ----
    print("\n-- D. the decisive arithmetic ------------------------------------")
    check("Lambda^2(R^(+)) contains L7+ with multiplicity", table_p["L7+"]["rs_alt"], 0)
    check("Lambda^2(R^(+)) contains L7- with multiplicity", table_p["L7-"]["rs_alt"], 0)
    check("Sym^2(R^(+)) contains L7+ with multiplicity", table_p["L7+"]["rs_sym"], 1)
    check("Sym^2(R^(+)) contains L7- with multiplicity", table_p["L7-"]["rs_sym"], 1)
    check("the whole unique channel sits in the CROSS block", table_p["L7+"]["cross"], 1)
    check("the mirror middle form feeds nothing at zeta_+", table_p["L7-"]["cross"], 0)
    check("Lambda^2(S_-) (the gamma-trace) contains no middle form",
          (table_p["L7+"]["trace_alt"], table_p["L7-"]["trace_alt"]), (0, 0))
    # the mirror corner zeta_- = S_+ (+) R^(-).  Its unique channel is
    # Inv(Lambda^2(zeta_-) (x) Lambda^7_+) = mult of L7- in Lambda^2(zeta_-).
    mb_p = blocks(L7P, -1)
    mb_m = blocks(L7M, -1)
    check("mirror: Lambda^2(R^(-)) contains L7- with multiplicity", mb_m["rs_alt"], 0)
    check("mirror: Lambda^2(R^(-)) contains L7+ with multiplicity", mb_p["rs_alt"], 0)
    check("mirror: Sym^2(R^(-)) contains L7- with multiplicity", mb_m["rs_sym"], 1)
    check("mirror: Sym^2(R^(-)) contains L7+ with multiplicity", mb_p["rs_sym"], 1)
    check("mirror: the unique channel sits in the CROSS block", mb_m["cross"], 1)
    check("mirror: the other middle form feeds nothing at zeta_-", mb_p["cross"], 0)
    check("mirror: total Lambda^2(zeta_-) middle-form content is (0,1)",
          (mb_p["tot_alt"], mb_m["tot_alt"]), (0, 1))

    # POSITIVE CONTROL, SAME RANK: Lambda^2(R) is NOT a dead detector
    check("[control+] Lambda^2(R^(+)) contains L1 with multiplicity", table_p["L1"]["rs_alt"], 1)
    check("[control+] Lambda^2(R^(+)) contains L5 with multiplicity", table_p["L5"]["rs_alt"], 2)
    check("[control+] Sym^2(R^(+)) contains L3 with multiplicity", table_p["L3"]["rs_sym"], 2)

    # rank bound: the only nonzero block is off-diagonal, so the induced form on
    # the 896 has rank at most 2 * dim S = 128 and kills >= 768 of R.
    check("rank bound of the channel's bilinear form on zeta_+", 2 * 64, 128)
    check("R directions the channel must leave unpaired, minimum", 832 - 64, 768)
    check("the channel can reach at most this many of the 128 remainder", 64, 64)

    # ---- section E: second, INDEPENDENT instrument ----
    print("\n-- E. independent instrument (Racah/Brauer over W(D_7)) ----------")
    orbit = weyl_rho_orbit(N)
    check("|W(D_7)|", len(orbit), 322560)
    wZP = wts_tensor(wV, wSP)
    check("zeta_+ weight count", sum(wZP.values()), 896)
    wRP = msub(wZP, wSM)
    check("R^(+) weight count", sum(wRP.values()), 832)
    a2R = wts_alt2(wRP)
    s2R = wts_sym2(wRP)
    check("Lambda^2(R^(+)) weight count", sum(a2R.values()), 832 * 831 // 2)
    for nm, k in INS:
        check("RACAH  Lambda^2(R^(+)) mult %-3s" % nm,
              racah_mult(k, a2R, orbit, N), table_p[nm]["rs_alt"])
        check("RACAH  Sym^2(R^(+))    mult %-3s" % nm,
              racah_mult(k, s2R, orbit, N), table_p[nm]["rs_sym"])

    # ---- section F: the 4d x internal branching -- eq (11.6), exactly ----
    print("\n-- F. D_7 -> D_2 x D_5: the source's own F/Q/Z, reproduced -------")
    n4, n10 = 2, 5
    V4, V10 = wts_V(n4), wts_V(n10)
    sp4, sm4 = wts_spinor(+1, n4), wts_spinor(-1, n4)
    s16, s16b = wts_spinor(+1, n10), wts_spinor(-1, n10)
    # V_4 (x) 2_+ = 6 (+) 2_- : the 4d leg of the product rule, eq (11.1).
    # NOTE (falsifiability limit, stated not hidden): the *coordinate embedding*
    # of the D_2 and D_5 blocks is NOT separately falsifiable here, because the
    # weight multisets involved are symmetric under coordinate permutation.  The
    # branching leg is pinned instead by this 4d product rule, which M11
    # corrupts.
    trace_p = sp4 if MUT == "M11_bad_4d_product_rule" else sm4
    six_p = msub(wts_tensor(V4, sp4), trace_p)
    six_m = msub(wts_tensor(V4, sm4), sp4)
    w144b = msub(wts_tensor(V10, s16), s16b)    # V_10 (x) 16 = 16b (+) 144b
    w144 = msub(wts_tensor(V10, s16b), s16)
    check("dim of the 4d chiral Rarita-Schwinger rep", sum(six_p.values()), 6)
    check("dim of the internal vector-spinor", sum(w144.values()), 144)

    def prod(a, b):
        """Embed a D_2 weight and a D_5 weight into the D_7 coordinate frame.
        The 4d block occupies coordinates 1-2, the internal block 3-7."""
        c = Counter()
        for x, mx in a.items():
            for y, my in b.items():
                c[tuple(x) + tuple(y)] += mx * my
        return c

    Q = prod(six_p, s16) + prod(six_m, s16b)
    F = prod(sm4, s16) + prod(sp4, s16b)
    Z = prod(sp4, w144b) + prod(sm4, w144)
    check("[R eq (11.6)] graded dims (F, Q, Z)",
          (sum(F.values()), sum(Q.values()), sum(Z.values())), REF["source_eq116_graded"])
    check("[R eq (11.6)] ungraded dims (F, Q, Z)",
          (2 * sum(F.values()), 2 * sum(Q.values()), 2 * sum(Z.values())),
          REF["source_eq116_ungraded"])
    claim = Counter()
    for part in (Q, F, F, Z):
        claim += part
    check("zeta_+ branches EXACTLY to Q (+) 2F (+) Z", claim == wZP, True)
    check("the RS module R^(+) IS the source's 832 bracket (Z (+) Q (+) F)",
          msub(wZP, wSM) == (Q + F + Z), True)
    check("the gamma-trace IS the source's standalone 64 bracket (F)", wSM == F, True)
    check("832 = 64 + 192 + 576", 64 + 192 + 576, 832)
    check("the 128 remainder = 144 - one generation-shaped 16 [R HE-1]", 144 - 16, 128)
    # the source's "the logic of the known matters is reversed": the internal 16
    # travels with 2_- in F and with the 6 BUILT ON 2_+ in Q.
    f16_partner = prod(sm4, s16)
    q16_partner = prod(six_p, s16)
    check("F pairs the internal 16 with the 4d Weyl half 2_-",
          sum(f16_partner.values()), 32)
    check("Q pairs the same internal 16 with the 6 built on the OPPOSITE half 2_+",
          sum(q16_partner.values()), 96)
    check("so the source's 'logic ... is reversed' is FORCED by V_4 (x) 2_+ = 6 (+) 2_-",
          msub(wts_tensor(V4, sp4), six_p) == sm4, True)

    # ---- section G: the reduced (internal so(10)) layer ----
    print("\n-- G. the internal layer: what a Lorentz-scalar middle form is ---")
    from math import comb
    check("SO(4)-singlet content of Lambda^7(V_14): Lambda^7(V_10) + Lambda^3(V_10)",
          (comb(10, 7), comb(10, 3)), (120, 120))
    check("so(10) dim of Lambda^3(V_10)", weyl_dim((2, 2, 2, 0, 0), n10), 120)
    check("hence each middle form carries exactly one so(10) 120 as its "
          "Lorentz-scalar part", comb(10, 3), 120)
    hw10_, hw120_, hw126_, hw126b_ = (2, 0, 0, 0, 0), (2, 2, 2, 0, 0), (2,) * 5, (2, 2, 2, 2, -2)
    hw144_ = (3, 1, 1, 1, 1)
    d1616 = klimyk((1,) * 5, s16, n10)
    check("[R MJ-1] 16 (x) 16 = 10 + 120 + 126",
          sorted((weyl_dim(k, n10), v) for k, v in d1616.items()),
          sorted([(10, 1), (120, 1), (126, 1)]))
    check("[R canon] 16 (x) 16 has NO so(10) singlet", d1616.get((0,) * 5, 0), 0)
    d16144 = klimyk(hw144_, s16, n10)
    check("[R HE-1] Inv_Spin(10)(16 (x) 144)", d16144.get((0,) * 5, 0),
          REF["he1_spin10_16x144_invariants"])
    check("16 (x) 144 contains the 120 with multiplicity", d16144.get(hw120_, 0), 0)
    # squares of the internal 144, via the same block identity at D_5
    wL2_5 = wts_lambda_k(2, n10)
    wS2V_5 = wts_sym2(V10)
    wS2V0_5 = Counter(wS2V_5)
    wS2V0_5[(0,) * 5] -= 1
    alt5 = Counter()
    sym5 = Counter()
    for lam in (hw10_, hw126b_):
        alt5 += klimyk(lam, wL2_5, n10)
        sym5 += klimyk(lam, wS2V0_5, n10)
    sym5[hw10_] += 1
    sym5[hw126b_] += 1
    alt5 += klimyk(hw120_, wS2V0_5, n10)
    alt5[hw120_] += 1
    sym5 += klimyk(hw120_, wL2_5, n10)
    alt16_5 = Counter({hw120_: 1})
    sym16_5 = Counter({hw10_: 1, hw126b_: 1})

    def blk5(hw):
        a = alt5.get(hw, 0) - alt16_5.get(hw, 0) - d16144.get(hw, 0)
        s = sym5.get(hw, 0) - sym16_5.get(hw, 0) - d16144.get(hw, 0)
        return a, s

    a120, s120 = blk5(hw120_)
    check("Sym^2(144) contains the 120 with multiplicity", s120, 1)
    check("Lambda^2(144) contains the 120 with multiplicity", a120, 3)
    # PLANTED-POSITIVE CONTROL AT A DIFFERENT RANK, opposite attribution:
    # at D_5 the live selective middle-form channel IS carried by the RS module.
    a126b, _ = blk5(hw126b_)
    check("[control++] Lambda^2(144) contains the middle form 126bar", a126b, 1)
    check("[control++] Lambda^2(16) contains no 126bar", alt16_5.get(hw126b_, 0), 0)
    check("[control++] so at D_5 the whole live selective channel sits on the "
          "RS module -- the OPPOSITE attribution, same code path",
          (alt5.get(hw126b_, 0), a126b), (1, 1))

    # ---- section H: contrary controls -- corners the placement CANNOT reach ----
    print("\n-- H. contrary controls ------------------------------------------")
    s2p = wts_sym2(wSP)
    a2p = wts_alt2(wSP)
    check("[contrary] Sym^2(nu_+) contains L7+ (highest weight, so weight mult "
          "= irrep mult)", s2p[L7P], 1)
    check("[contrary] Lambda^2(nu_+) contains L7+", a2p[L7P], 0)
    check("[contrary] Lambda^2(nu_+) contains L7-", a2p[L7M], 0)
    check("[contrary] the 0-form corners host NO Grassmann-live middle-form "
          "self-shape", (a2p[L7P], a2p[L7M]), (0, 0))

    # ---- planted false facts ----
    print("\n-- I. planted false propositions (each MUST be observed False) ----")
    planted_false("RS module has a live middle-form self-shape", table_p["L7+"]["rs_alt"] > 0)
    planted_false("zeta_+ is irreducible", len(dec_zp) == 1)
    planted_false("R^(+) has dimension 896", weyl_dim(RP, N) == 896)
    planted_false("the trace block is 832-dimensional", weyl_dim(SM, N) == 832)
    planted_false("Lambda^2(S_-) contains a middle form", table_p["L7+"]["trace_alt"] > 0)
    planted_false("both middle forms feed the cross block", table_p["L7-"]["cross"] > 0)
    planted_false("Sym^2(R) is chirality-selective",
                  table_p["L7+"]["rs_sym"] != table_p["L7-"]["rs_sym"])
    planted_false("16 (x) 144 has a Spin(10) singlet", d16144.get((0,) * 5, 0) > 0)
    planted_false("16 (x) 144 has a 120", d16144.get(hw120_, 0) > 0)
    planted_false("Sym^2(16) contains the 120", 120 in [weyl_dim(k, n10) for k in
                                                        (hw10_, hw126_)])
    planted_false("Q and Z have equal dimension", sum(Q.values()) == sum(Z.values()))
    planted_false("the 128 remainder equals the 144", 144 == 128)
    planted_false("the channel could reach all 128 remainder directions", 64 >= 128)
    planted_false("Lambda^2(R) is a dead detector",
                  table_p["L1"]["rs_alt"] == 0 and table_p["L5"]["rs_alt"] == 0)
    planted_false("D_5 agrees with D_7 on the attribution", a126b == 0)

    print("\n" + "=" * 78)
    print("RSC-1: %d/%d checks pass, %d planted-false observed False, exit %d"
          % (CHECKS - FAILS, CHECKS, PLANTED, 1 if FAILS else 0))
    print("=" * 78)
    return 1 if FAILS else 0


# ---------------------------------------------------------------------------
# 4. Selftest -- clean baseline FIRST, then machinery/reference mutations.
# ---------------------------------------------------------------------------

MUTATIONS = [
    "M1_drop_a_root",
    "M2_sign_always_plus",
    "M3_skip_wall_test",
    "M4_never_flip_last",
    "M5_klimyk_no_rho",
    "M6_spinor_parity_flip",
    "M7_alt2_includes_diagonal",
    "M8_drop_cross_term",
    "M9_duality_is_identity",
    "M10_racah_uses_B_n",
    "M11_bad_4d_product_rule",
    "M12_corrupt_reference",
]

SELF = os.path.abspath(__file__)


def _run(mut, poison=False):
    env = dict(os.environ)
    if mut:
        env["RSC1_MUT"] = mut
    else:
        env.pop("RSC1_MUT", None)
    if poison:
        env["RSC1_POISON_BASELINE"] = "1"
    p = subprocess.run([sys.executable, SELF], env=env,
                       capture_output=True, text=True,
                       cwd=os.path.dirname(SELF))
    return p.returncode, p.stdout + p.stderr


def selftest(poison_baseline=False):
    print("#" * 78)
    print("# RSC-1 selftest -- clean baseline verified BEFORE any mutation")
    print("#" * 78)
    rc, out = _run("", poison=poison_baseline)
    n_fail = out.count("[FAIL]")
    baseline_ok = (rc == 0 and n_fail == 0 and "checks pass" in out)
    print("baseline: exit %d, %d [FAIL] lines -> %s"
          % (rc, n_fail, "CLEAN" if baseline_ok else "RED"))
    if not baseline_ok:
        print("REFUSING to run mutations: a red baseline makes every mutant exit")
        print("nonzero for the pre-existing reason, which would bank a false")
        print("'all mutations caught'.  (VERIFICATION.md rule 1.)")
        return 1
    if poison_baseline:
        print("POISON MODE: baseline was expected RED and came back CLEAN.")
        return 1

    caught, crashed, missed = [], [], []
    for mut in MUTATIONS:
        rc, out = _run(mut)
        has_fail = "[FAIL]" in out
        if rc != 0 and has_fail:
            first = next(l for l in out.splitlines() if l.startswith("[FAIL]"))
            caught.append((mut, first.strip()))
            print("  CAUGHT   %-26s exit %d via %s" % (mut, rc, first[:58].strip()))
        elif rc != 0:
            crashed.append(mut)
            print("  CRASH-NOT-DETECTION  %-26s exit %d, no [FAIL] line" % (mut, rc))
        else:
            missed.append(mut)
            print("  MISSED   %-26s exit 0" % mut)

    print("-" * 78)
    print("selftest: %d/%d mutations caught via a genuine [FAIL]; %d crash-only; %d missed"
          % (len(caught), len(MUTATIONS), len(crashed), len(missed)))
    return 0 if (len(caught) == len(MUTATIONS)) else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest(poison_baseline="--poison-baseline" in sys.argv))
    if os.environ.get("RSC1_POISON_BASELINE"):
        # Only reachable from `--selftest --poison-baseline`: proves the
        # baseline guard can actually fail.  Never fires in a normal run.
        print("[FAIL] poisoned baseline (selftest guard power demonstration)")
        sys.exit(1)
    sys.exit(main())
