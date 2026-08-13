#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C3-prime probe: exact commutant of spin(1,3) x spin(6,4) inside M(128,R)
on the certified Cl(7,7) gamma bank, plus the induced complex/Krein layer.

Brief v1.1 launch, v1.2 mid-run corrections applied (five-lens rule; step-4
per-half-Hermitian mis-specification dropped; C3a/C3b/C3c successor
structure; independent-replication framing against the hourly gate result).

ANTI-REDO: the gamma construction, eta convention, index conventions, and the
exact sign-consistent-orbit nullspace solver are IMPORTED from the certified
C1/C2 probe (tests/channel-swings/nguyen_c1c2_real_form_probe.py, filed
2026-08-12, 42/42 PASS).  No new gamma basis is invented.  The repo is
treated READ-ONLY: sys.dont_write_bytecode is set BEFORE import so no
__pycache__ is written into the repo tree.

Pins (recorded, not fetched at runtime): spec section = "Integration
correction -- the split layer" at the end of
explorations/nguyen-c1c2-real-form-certificates-2026-08-12.md, first present
at HEAD c789e75b; tree read at HEAD 0e299cf5 (hourly commits
29286b1f preregistration + 0e299cf5 split-layer gate landed mid-run).

Block assignment (stated with rationale; the probe's eta ordering makes the
(1,3) block NON-CONTIGUOUS and this is handled explicitly):
  eta = diag(+1 x7, -1 x7); gammas 0..6 square +1, gammas 7..13 square -1
  (certified C1 convention).  Eq (12.19) types the split TX^{1,3} (+)
  N^{6,4}_gimel (SC-CHI-03 locus; s11 extraction :249-250), so the base
  block needs signature (1,3) = one square-+1 generator and three square--1
  generators, and the normal block needs (6,4) = six square-+1 and four
  square--1.  Canonical assignment: BASE = (0, 7, 8, 9) (first plus gamma,
  first three minus gammas), NORMAL = (1,2,3,4,5,6,10,11,12,13) (remaining
  six plus, four minus).  Any other admissible assignment differs by an
  orthogonal relabeling inside the plus and minus blocks, implemented by
  Pin(7,7) conjugation, so the commutant dimension/type is
  assignment-independent; control ALT-ASSIGNMENT verifies this with a
  second, disjointly chosen assignment.

Deterministic: no randomness anywhere in this file.  Exit code = number of
FAILed checks.  All arithmetic exact (integers; Fractions for the Hermitian
LDL*; Gaussian rationals as pairs of Fractions).
"""

import sys
from fractions import Fraction

sys.dont_write_bytecode = True  # repo is READ-ONLY: no __pycache__ there

import importlib.util

REPO = "/Users/joe/Brain/CapacityOS/repos/public/gu-formalization"
PROBE_PATH = REPO + "/tests/channel-swings/nguyen_c1c2_real_form_probe.py"
_spec = importlib.util.spec_from_file_location("nguyen_c1c2_real_form_probe",
                                               PROBE_PATH)
P = importlib.util.module_from_spec(_spec)
sys.modules["nguyen_c1c2_real_form_probe"] = P
_spec.loader.exec_module(P)

PASSES = []
FAILURES = []


def check(name, ok, detail=""):
    tag = "PASS" if ok else "FAIL"
    print("[%s] %s%s" % (tag, name, (" -- " + detail) if detail else ""),
          flush=True)
    (PASSES if ok else FAILURES).append(name)
    return ok


# --------------------------------------------------------------------------
# Small helpers adapted from the certified probe's main() closures (they are
# defined inside main() there and are not importable; adapted verbatim in
# behavior, same conventions).
# --------------------------------------------------------------------------

def apply_sp(B, v):
    out = {}
    for j, a in v.items():
        out[B.perm[j]] = out.get(B.perm[j], 0) + B.sign[j] * a
    return {k: v2 for k, v2 in out.items() if v2 != 0}


def dot(u, v):
    return sum(a * v.get(i, 0) for i, a in u.items())


def gram(Vr, Vc, B):
    Bc = [apply_sp(B, v) for v in Vc]
    return [[dot(u, w) for w in Bc] for u in Vr]


def eigsplit(omega, n):
    """Exact +1/-1 eigenbasis of an involutive signed perm (probe's method)."""
    plus_basis = []
    minus_basis = []
    seen = [False] * n
    for a in range(n):
        if seen[a]:
            continue
        b, s = omega.perm[a], omega.sign[a]
        if b == a:
            seen[a] = True
            (plus_basis if s == 1 else minus_basis).append({a: 1})
        else:
            seen[a] = True
            seen[b] = True
            plus_basis.append({a: 1, b: s})
            minus_basis.append({a: 1, b: -s})
    return plus_basis, minus_basis


def restrict(sig, basis, lookup):
    """Restrict a signed perm commuting with omega to an eigenbasis span
    (probe's method, adapted)."""
    n_half = len(basis)
    perm = [None] * n_half
    sign = [0] * n_half
    for col, v in enumerate(basis):
        img = apply_sp(sig, v)
        key = tuple(sorted(img.keys()))
        hit = lookup.get(key)
        if hit is None:
            return None
        row, w = hit
        ratio = None
        for i, a in w.items():
            r = img.get(i, 0) // a if img.get(i, 0) % a == 0 else None
            if r is None or (ratio is not None and r != ratio):
                return None
            ratio = r
        if ratio not in (1, -1):
            return None
        if any(img.get(i, 0) != ratio * a for i, a in w.items()) or \
           len(img) != len(w):
            return None
        perm[col] = row
        sign[col] = ratio
    if any(p is None for p in perm) or len(set(perm)) != n_half:
        return None
    return P.SP(tuple(perm), tuple(sign))


def commutes(a, b):
    return a.mul(b).eq(b.mul(a))


def product(gammas, indices):
    out = P.SP.identity(gammas[0].n)
    for i in indices:
        out = out.mul(gammas[i])
    return out


def block_bivectors(gammas, indices):
    idx = list(indices)
    return [gammas[i].mul(gammas[j])
            for a, i in enumerate(idx) for j in idx[a + 1:]]


# --------------------------------------------------------------------------
# Exact Gaussian-rational Hermitian LDL* (full symmetric pivoting).
# Complex numbers are (Fraction re, Fraction im) pairs.
# --------------------------------------------------------------------------

F0 = Fraction(0)


def gq(re, im=0):
    return (Fraction(re), Fraction(im))


def gq_add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def gq_sub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def gq_mul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def gq_conj(x):
    return (x[0], -x[1])


def gq_div_real(x, d):
    return (x[0] / d, x[1] / d)


def gq_is_zero(x):
    return x[0] == 0 and x[1] == 0


def hermitian_signature(H):
    """Exact signature (pos, neg, zero) of a Hermitian Gaussian-rational
    matrix by congruence diagonalization with full symmetric pivoting."""
    n = len(H)
    H = [row[:] for row in H]
    pos = neg = zero = 0
    for k in range(n):
        if gq_is_zero(H[k][k]):
            m = next((i for i in range(k + 1, n)
                      if not gq_is_zero(H[i][i])), None)
            if m is not None:
                for j in range(n):
                    H[k][j], H[m][j] = H[m][j], H[k][j]
                for i in range(n):
                    H[i][k], H[i][m] = H[i][m], H[i][k]
            else:
                pq = next(((p, q) for p in range(k, n)
                           for q in range(p + 1, n)
                           if not gq_is_zero(H[p][q])), None)
                if pq is None:
                    zero += n - k
                    break
                p, q = pq
                if p != k:
                    for j in range(n):
                        H[k][j], H[p][j] = H[p][j], H[k][j]
                    for i in range(n):
                        H[i][k], H[i][p] = H[i][p], H[i][k]
                    # q stays > k; if q == k impossible since q > p >= k
                c = H[k][q]
                # basis change u_k := u_k + c u_q (rows), then conj on cols
                for j in range(n):
                    H[k][j] = gq_add(H[k][j], gq_mul(c, H[q][j]))
                cc = gq_conj(c)
                for i in range(n):
                    H[i][k] = gq_add(H[i][k], gq_mul(cc, H[i][q]))
        d = H[k][k]
        assert d[1] == 0, "Hermitian diagonal must be real"
        if d[0] == 0:
            zero += 1
            continue
        if d[0] > 0:
            pos += 1
        else:
            neg += 1
        dr = d[0]
        col_k = [H[i][k] for i in range(n)]
        row_k = [H[k][j] for j in range(n)]
        for i in range(k + 1, n):
            if gq_is_zero(col_k[i]):
                continue
            f = gq_div_real(col_k[i], dr)
            for j in range(k + 1, n):
                H[i][j] = gq_sub(H[i][j], gq_mul(f, row_k[j]))
            H[i][k] = gq(0)
            H[k][i] = gq(0)
    return pos, neg, zero


# ==========================================================================
# MAIN
# ==========================================================================

def main():
    print("=" * 78)
    print("C3-prime probe -- split-layer commutant, exact integer arithmetic")
    print("gammas/solver: imported from certified nguyen_c1c2_real_form_probe")
    print("spec pin: c789e75b (correction section); tree read at 0e299cf5")
    print("=" * 78)

    N = 128
    gammas, eta = P.build_cl77()
    IdN = P.SP.identity(N)

    # ---- ground the imported construction (anti-redo, re-verified) ----
    bad = []
    for i in range(14):
        if gammas[i].mul(gammas[i]).is_identity_times() != eta[i]:
            bad.append(("sq", i))
        for j in range(i + 1, 14):
            if not P.sum_is_zero(gammas[i].mul(gammas[j]),
                                 gammas[j].mul(gammas[i])):
                bad.append(("anti", i, j))
    check("C3P-GROUND-CLIFFORD: imported certified Cl(7,7) bank re-verified "
          "(105 anticommutators + 14 squares, eta=(7,7))", not bad,
          "violations=%s" % (bad[:3] if bad else "none"))

    # ---- block assignment ----
    BASE = (0, 7, 8, 9)
    NORMAL = (1, 2, 3, 4, 5, 6, 10, 11, 12, 13)
    sig_base = sorted(eta[i] for i in BASE)
    sig_normal = sorted(eta[i] for i in NORMAL)
    check("C3P-BLOCK-ASSIGNMENT: BASE=(0,7,8,9) has eta multiset (1,3), "
          "NORMAL=(1..6,10..13) has (6,4); disjoint, exhaustive; "
          "non-contiguity of the (1,3) block under the certified plus-first "
          "eta ordering handled by explicit index lists",
          sig_base == [-1, -1, -1, 1] and
          sig_normal == [-1] * 4 + [1] * 6 and
          sorted(BASE + NORMAL) == list(range(14)))

    # ---- generators of spin(1,3) x spin(6,4) ----
    sig_split = block_bivectors(gammas, BASE) + block_bivectors(gammas, NORMAL)
    check("C3P-GENERATOR-COUNT: 6 base bivectors + 45 normal bivectors = %d "
          "(expect 51; no mixed base-normal products)" % len(sig_split),
          len(sig_split) == 51 and
          len(block_bivectors(gammas, BASE)) == 6)

    # ---- the split commutant (COMPLETE nullspace, certified solver) ----
    dim_split, bas_split = P.commutant(sig_split, N)
    check("C3P-SPLIT-COMMUTANT-DIM: dim_R End_{spin(1,3)+spin(6,4)}(R^128) "
          "= %d (expect 4; refutation branch: 1 would have restored the "
          "ambient-only typing at full strength)" % dim_split,
          dim_split == 4)

    # ---- basis, relations, algebra type ----
    omega = product(gammas, range(14))
    J4 = product(gammas, BASE)      # base-block volume, degree 4
    J10 = product(gammas, NORMAL)   # normal-block volume, degree 10
    sq4 = J4.mul(J4).is_identity_times()
    sq10 = J10.mul(J10).is_identity_times()
    sqom = omega.mul(omega).is_identity_times()
    s_prod = J4.mul(J10).proportional_sign(omega)
    comm_pairs = (commutes(J4, J10) and commutes(J4, omega) and
                  commutes(J10, omega))
    span_ok = (dim_split == 4 and
               P.in_span(bas_split, IdN, N) and
               P.in_span(bas_split, omega, N) and
               P.in_span(bas_split, J4, N) and
               P.in_span(bas_split, J10, N))
    check("C3P-COMMUTANT-BASIS: commutant = span{1, J4, J10, omega} with "
          "J4 = gamma_0 gamma_7 gamma_8 gamma_9 (base volume), J10 = "
          "normal volume (all four verified in the computed span; dim 4 => "
          "equality)", span_ok)
    check("C3P-COMMUTANT-RELATIONS: J4^2 = %+d*I (expect -1), J10^2 = %+d*I "
          "(expect -1), omega^2 = %+d*I (expect +1), J4*J10 = %+d*omega "
          "(expect +1), all pairs commute: %s => commutative algebra "
          "C (x)_R C = C (+) C; central idempotents (1 +- omega)/2; center "
          "= whole algebra" % (sq4, sq10, sqom, s_prod, comm_pairs),
          sq4 == -1 and sq10 == -1 and sqom == 1 and s_prod == 1 and
          comm_pairs)
    check("C3P-REPLICATION-COMPARE: hourly gate reports span{1,J4,J10,omega}, "
          "J4^2=J10^2=-1, J4J10=J10J4=omega, omega^2=+1, C+C "
          "(selected-k77-split-layer-commutant-action-parent-gate-2026-08-12"
          ".md; RUN-20260812-020740): this run's independent driver "
          "reproduces dimension, generators, relations EXACTLY",
          span_ok and sq4 == -1 and sq10 == -1 and sqom == 1 and
          s_prod == 1 and comm_pairs)

    # ---- equivariance of both complex units ----
    eq4 = all(commutes(J4, s) for s in sig_split)
    eq10 = all(commutes(J10, s) for s in sig_split)
    check("C3P-J-EQUIVARIANCE: [J4, all 51 generators] = 0: %s; "
          "[J10, all 51 generators] = 0: %s (exact)" % (eq4, eq10),
          eq4 and eq10)

    # ---- B re-certification and B-compatibility classes ----
    dB, bB = P.bilinear_space(gammas, N, [-1] * 14)
    Bm = P.sparse_to_sp(bB[0], N) if dB == 1 else None
    if Bm is not None and Bm.sign[0] == -1:
        Bm = Bm.neg()
    symB = Bm.transpose().proportional_sign(Bm) if Bm else None
    sqB = Bm.mul(Bm).is_identity_times() if Bm else None
    trB = Bm.trace() if Bm else None
    check("C3P-B-RECERT: eps=-1 invariant bilinear dim %d (expect 1), "
          "B^T=%+d*B, B^2=%+d*I, tr=%d => signature (64,64) (re-certifies "
          "C1 row 4)" % (dB, symB, sqB, trB),
          dB == 1 and symB == 1 and sqB == 1 and trB == 0)

    def b_class(w):
        return w.transpose().mul(Bm).proportional_sign(Bm.mul(w))

    chi_I, chi_om = b_class(IdN), b_class(omega)
    chi_J4, chi_J10 = b_class(J4), b_class(J10)
    check("C3P-B-CLASSES: chi(1)=%+d, chi(omega)=%+d, chi(J4)=%+d, "
          "chi(J10)=%+d (expect +1,-1,+1,-1): B-skew slice of the "
          "commutant = span{omega, J10}; with the relations above the "
          "B-compatible complex structures (J^2=-I and J^T B J = B) are "
          "EXACTLY +-J10 (case arithmetic in the results draft)"
          % (chi_I, chi_om, chi_J4, chi_J10),
          (chi_I, chi_om, chi_J4, chi_J10) == (1, -1, 1, -1))
    J = J10
    jbj = J.transpose().mul(Bm).mul(J)
    check("C3P-J-B-COMPAT: J10^T B J10 = B exactly (J10 is a B-orthogonal "
          "complex structure; the Krein-compatible unit)", jbj.eq(Bm))

    # ---- ambient chirality halves ----
    plus_basis, minus_basis = eigsplit(omega, N)
    lookup_p = {tuple(sorted(v.keys())): (i, v)
                for i, v in enumerate(plus_basis)}
    lookup_m = {tuple(sorted(v.keys())): (i, v)
                for i, v in enumerate(minus_basis)}
    check("C3P-CHIRALITY-SPLIT: omega eigensplit (%d,%d) (expect (64,64))"
          % (len(plus_basis), len(minus_basis)),
          len(plus_basis) == 64 and len(minus_basis) == 64)

    okc = commutes(J, omega) and commutes(J4, omega)
    Jp = restrict(J, plus_basis, lookup_p)
    Jm = restrict(J, minus_basis, lookup_m)
    J4p = restrict(J4, plus_basis, lookup_p)
    J4m = restrict(J4, minus_basis, lookup_m)
    ok_restr = all(x is not None for x in (Jp, Jm, J4p, J4m))
    sqp = Jp.mul(Jp).is_identity_times() if Jp else None
    sqm = Jm.mul(Jm).is_identity_times() if Jm else None
    rel_p = Jp.proportional_sign(J4p) if ok_restr else None
    rel_m = Jm.proportional_sign(J4m) if ok_restr else None
    check("C3P-J-HALVES: [J,omega]=0: %s => J PRESERVES each ambient half "
          "(does not swap); restrictions are exact signed perms: %s; "
          "J|S+^2 = %+d*I, J|S-^2 = %+d*I (expect -1,-1) => each real-64 "
          "half carries complex-32 structure; J10|S+ = %+d*J4|S+, "
          "J10|S- = %+d*J4|S- (expect -1,+1 from J4*J10=omega)"
          % (okc, ok_restr, sqp, sqm, rel_p, rel_m),
          okc and ok_restr and sqp == -1 and sqm == -1 and
          rel_p == -1 and rel_m == 1)

    # ---- per-half split commutants ----
    sig_p = [restrict(s, plus_basis, lookup_p) for s in sig_split]
    sig_m = [restrict(s, minus_basis, lookup_m) for s in sig_split]
    ok_sig_restr = all(s is not None for s in sig_p + sig_m)
    dim_hp = dim_hm = None
    span_hp = span_hm = False
    if ok_sig_restr:
        dim_hp, bas_hp = P.commutant(sig_p, 64)
        dim_hm, bas_hm = P.commutant(sig_m, 64)
        Id64 = P.SP.identity(64)
        span_hp = (dim_hp == 2 and P.in_span(bas_hp, Id64, 64) and
                   P.in_span(bas_hp, Jp, 64))
        span_hm = (dim_hm == 2 and P.in_span(bas_hm, Id64, 64) and
                   P.in_span(bas_hm, Jm, 64))
    check("C3P-HALF-COMMUTANTS-SPLIT: dim End_split(S+) = %s, "
          "dim End_split(S-) = %s (expect 2,2 = span{1, J|half} = C each; "
          "ambient-Spin certified values were 1,1: REAL there, COMPLEX "
          "here -- the layer contrast, exact)" % (dim_hp, dim_hm),
          ok_sig_restr and span_hp and span_hm)

    # ---- split-invariant bilinears: full and blocks ----
    dim_bil, bas_bil = P.spin_bilinear_space(sig_split, N)
    dpp = P.mixed_block_bilinear_space(sig_p, sig_p, 64, 64)
    dmm = P.mixed_block_bilinear_space(sig_m, sig_m, 64, 64)
    dpm = P.mixed_block_bilinear_space(sig_p, sig_m, 64, 64)
    dmp = P.mixed_block_bilinear_space(sig_m, sig_p, 64, 64)
    check("C3P-SPLIT-BILINEARS: dim Hom_split(S x S, R) = %d (expect 4 = "
          "commutant o B); blocks pp/mm/pm/mp = %d/%d/%d/%d (expect "
          "0/0/2/2: even at the split layer NO same-half invariant real "
          "bilinear exists; cross-pairing doubles from the ambient 1/1)"
          % (dim_bil, dpp, dmm, dpm, dmp),
          dim_bil == 4 and (dpp, dmm, dpm, dmp) == (0, 0, 2, 2))

    # ---- Hermitian form on the TOTAL (S, J10): h = B(.,.) + i B(., J.) ----
    BJ = Bm.mul(J)
    reps = [i for i in range(N) if i < J.perm[i]]
    ok_pairs = (len(reps) == 64 and
                all(J.perm[J.perm[i]] == i for i in range(N)))

    def b_entry(sp, a, b):
        return sp.sign[b] if sp.perm[b] == a else 0

    H = [[gq(b_entry(Bm, reps[k], reps[l]), b_entry(BJ, reps[k], reps[l]))
          for l in range(64)] for k in range(64)]
    herm_ok = all(H[i][j] == gq_conj(H[j][i])
                  for i in range(64) for j in range(64))
    pos, neg, zero = hermitian_signature(H)
    check("C3P-HERMITIAN-TOTAL: J-pair coordinate basis ok: %s; Gram of "
          "h(x,y)=B(x,y)+i*B(x,Jy) on (S,J10)=C^64 is Hermitian: %s; exact "
          "LDL* signature = (%d,%d) with %d zero pivots (expect (32,32), 0: "
          "ONE Krein space C^(32,32) on the TOTAL spinor module)"
          % (ok_pairs, herm_ok, pos, neg, zero),
          ok_pairs and herm_ok and (pos, neg, zero) == (32, 32, 0))

    # ---- Krein presentation of the halves (NOT a failure; v1.2 scope) ----
    zpp_B = all(v == 0 for row in gram(plus_basis, plus_basis, Bm)
                for v in row)
    zmm_B = all(v == 0 for row in gram(minus_basis, minus_basis, Bm)
                for v in row)
    zpp_BJ = all(v == 0 for row in gram(plus_basis, plus_basis, BJ)
                 for v in row)
    zmm_BJ = all(v == 0 for row in gram(minus_basis, minus_basis, BJ)
                 for v in row)
    det_cross = P.bareiss_det(gram(plus_basis, minus_basis, Bm))
    check("C3P-KREIN-HALVES: h(S+,S+) = 0: %s, h(S-,S-) = 0: %s (both the "
          "B block and the B(.,J.) block vanish identically); real cross "
          "block det = %d != 0 (re-certifies C1 row 6) => the two ambient "
          "halves are MAXIMAL h-NEUTRAL (isotropic) complex-32 subspaces "
          "of C^(32,32), cross-paired; per-half restriction of h is the "
          "zero form BY C1's isotropy certificate, not a native-J failure "
          "(v1.2 correction: the fence's per-half C^(32,32) lives on the "
          "complexified halves, C3b)"
          % (zpp_B and zpp_BJ, zmm_B and zmm_BJ, det_cross),
          zpp_B and zmm_B and zpp_BJ and zmm_BJ and det_cross != 0)

    # ---- C3b-partial: conjugate 32+32 branching of each complexified half --
    trJp, trJm = Jp.trace(), Jm.trace()
    eqp = all(commutes(Jp, s) for s in sig_p)
    eqm = all(commutes(Jm, s) for s in sig_m)
    check("C3P-C3B-PARTIAL: J|half is a REAL operator with square -I and "
          "tr(J|S+) = %d, tr(J|S-) = %d (expect 0,0) => (S+- (x) C) = "
          "E_{+i} (+) E_{-i}, complex-conjugate pair, dim_C 32 each "
          "(tr P_{+-i} = (64 -+ i*tr J)/2 = 32 exactly); [J|half, all 51 "
          "restricted generators] = 0: %s/%s => both eigenspaces are "
          "complex-32 SUBREPRESENTATIONS exchanged by conjugation "
          "(the conjugate 32+32 branching of each complexified Weyl half, "
          "certified; the (2-+ x 16+)(+)(2+- x 16-) LABEL identification "
          "and the Hermitian (32,32) on that object remain owed = C3b)"
          % (trJp, trJm, eqp, eqm),
          trJp == 0 and trJm == 0 and eqp and eqm)

    # ---- CONTROLS ----
    dim_full, bas_full = P.commutant(gammas, N)
    idf = P.sparse_to_sp(bas_full[0], N) if dim_full == 1 else None
    check("C3P-CONTROL-FULL-CLIFFORD-14: commutant of all 14 gammas: dim %d "
          "(expect 1, basis Identity; re-certifies C2 row 11)"
          % dim_full,
          dim_full == 1 and idf is not None and
          abs(idf.is_identity_times() or 0) == 1)

    sig_all = [gammas[i].mul(gammas[j]) for i in range(14)
               for j in range(i + 1, 14)]
    dim_91, bas_91 = P.commutant(sig_all, N)
    span_91 = (dim_91 == 2 and P.in_span(bas_91, IdN, N) and
               P.in_span(bas_91, omega, N))
    check("C3P-CONTROL-FULL-SPIN-91: commutant of all 91 degree-2 words: "
          "dim %d = span{1, omega} (certified C2 row 12 value 2; the "
          "launch brief's control-(a) 'expect 1' conflates C2's 14-gamma "
          "row with its 91-word row -- certified numbers preserved); "
          "omega^2=+1 => still NO J there; enlargement chain 1 -> 2 -> 4 "
          "is the restriction effect, exact" % dim_91,
          span_91)

    BASE_W = (0, 1, 7, 8)
    NORMAL_W = (2, 3, 4, 5, 6, 9, 10, 11, 12, 13)
    sig_wrong = (block_bivectors(gammas, BASE_W) +
                 block_bivectors(gammas, NORMAL_W))
    dim_w, bas_w = P.commutant(sig_wrong, N)
    u_w = product(gammas, BASE_W)
    v_w = product(gammas, NORMAL_W)
    squ = u_w.mul(u_w).is_identity_times()
    sqv = v_w.mul(v_w).is_identity_times()
    s_w = u_w.mul(v_w).proportional_sign(omega)
    span_w = (dim_w == 4 and P.in_span(bas_w, IdN, N) and
              P.in_span(bas_w, omega, N) and P.in_span(bas_w, u_w, N) and
              P.in_span(bas_w, v_w, N))
    comm_w = commutes(u_w, v_w) and commutes(u_w, omega) and \
        commutes(v_w, omega)
    check("C3P-CONTROL-WRONG-SPLIT-(2,2)x(5,5): commutant dim %d (SAME "
          "dimension 4: span{1, u, v, omega}, u,v the block volumes, "
          "u*v=%+d*omega) BUT u^2 = %+d*I, v^2 = %+d*I (expect +1,+1), "
          "commutative: %s => Klein-four group algebra = R^4, NO complex "
          "structure (identity coefficient of any square is a sum of four "
          "real squares, never -1): dimension alone does NOT discriminate; "
          "the C-vs-R^4 TYPE tracks the source's (1,3)+(6,4) signature "
          "split exactly (blocks with p-q = -2 and +2, both in the "
          "complex-type classes p-q = +-2 mod 8; the control's blocks have "
          "p-q = 0, the real-split class)" % (dim_w, s_w, squ, sqv, comm_w),
          span_w and squ == 1 and sqv == 1 and comm_w)

    sig_broken = list(sig_split)
    s0 = sig_broken[0]
    flip = list(s0.sign)
    flip[0] = -flip[0]
    sig_broken[0] = P.SP(s0.perm, tuple(flip))
    dim_b, _ = P.commutant(sig_broken, N)
    check("C3P-CONTROL-BROKEN-GENERATOR: one sign flipped in generator 0: "
          "commutant dim %d != 4 (answer must change; planted negative)"
          % dim_b, dim_b != 4)

    BASE_A = (3, 9, 11, 13)
    NORMAL_A = tuple(i for i in range(14) if i not in BASE_A)
    sig_alt = (block_bivectors(gammas, BASE_A) +
               block_bivectors(gammas, NORMAL_A))
    dim_a, bas_a = P.commutant(sig_alt, N)
    u_a = product(gammas, BASE_A)
    sqa = u_a.mul(u_a).is_identity_times()
    check("C3P-CONTROL-ALT-ASSIGNMENT: second admissible (1,3) choice "
          "BASE=(3,9,11,13): commutant dim %d (expect 4), base volume "
          "squares %+d*I (expect -1) => the certificate is "
          "assignment-independent (adversarial-lens control)"
          % (dim_a, sqa),
          dim_a == 4 and sqa == -1)

    # ---- summary ----
    print("=" * 78)
    print("C3-PRIME CERTIFIED SUMMARY (exact):")
    print("  split commutant dim 4 = span{1, J4, J10, omega}; J4^2=J10^2=-1,")
    print("  J4J10=omega, omega^2=+1 => C (+) C; replicates hourly gate "
          "exactly.")
    print("  Equivariant J exists; B-compatible ones are exactly +-J10.")
    print("  J preserves both ambient halves; each real-64 half = "
          "complex-32.")
    print("  Per-half split commutants 2/2 (C each; ambient values were "
          "1/1).")
    print("  Split bilinears 4 total, blocks 0/0/2/2.")
    print("  h = B + iB(.,J10 .): Hermitian, signature (32,32) on "
          "(S,J10)=C^64;")
    print("  ambient halves are maximal neutral (isotropic), cross-paired "
          "(Krein).")
    print("  C3b-partial: conjugate equivariant 32+32 branching per "
          "complexified half.")
    print("  Controls: 14-gamma dim 1; 91-word dim 2 {1,omega}; wrong split "
          "(2,2)x(5,5)")
    print("  dim 4 but R^4 (no J); broken generator changes answer; alt "
          "assignment dim 4.")
    print("=" * 78)
    print("checks passed: %d, failed: %d" % (len(PASSES), len(FAILURES)))
    if FAILURES:
        print("FAILED:", FAILURES)
    return len(FAILURES)


if __name__ == "__main__":
    sys.exit(main())
