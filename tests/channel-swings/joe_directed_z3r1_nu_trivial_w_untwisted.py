#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Z3-R1 probe: Stiefel-Whitney classes of nu = R (+) Sym^2(Q*) over the RP^3
spine, and the orientation bit `w` this decides (AR-1 row 6; register M-H5;
design packet D1+D2, `explorations/z3-receptacle-design-packet-2026-08-11.md`).

WHAT THIS COMPUTES (exact, no floats). Wave C rebased
(`explorations/resolver-wave-c-rebased-q5-q6-mh7-2026-08-03.md:255-258`)
types the precondition, unproved there: "one must prove the stated
normal-bundle identification, `w1=w2=w3=0`, and the relevant
rank-at-least-four classification" before the sphere bundle `S(nu)` may be
called noncanonically `RP^3 x S^6`.  Register row M-H5
(`lab/process/improvement-register-2026-08-03.md:155`) prices this
"Verify nu decomposition (half-day); SW/triviality check (hours)".  This
probe proves it:

  PART 1  Universal splitting-principle identity (any rank-3 real bundle Q):
          w(Sym^2 Q) = 1 + (w1(Q)^2 + w2(Q)) + (w1(Q)*w2(Q) + w3(Q)), verified
          as an EXACT multivariate F_2 polynomial identity (3 formal roots),
          not merely checked at one substitution.
  PART 2  H^*(RP^3; F_2) = F_2[a]/(a^4).  Derive w(Q) = (1+a)^{-1} truncated
          = 1+a+a^2+a^3 from gamma (+) Q = V = R^4 (trivial), i.e. from
          w(gamma)*w(Q) = 1.  w1(Q)=a, w2(Q)=a^2, w3(Q)=a^3 -- ALL NONZERO.
  PART 3  Plug PART 2's values into PART 1's closed form: w(Sym^2 Q) = 1
          identically (w1=w2=w3=0) -- METHOD A.
  PART 4  INDEPENDENT cross-check -- METHOD B, disjoint machinery: Sym^2(V)
          = Sym^2(l) (+) (l (x) Q) (+) Sym^2(Q) with Sym^2(V) genuinely
          trivial (V trivial), Sym^2(l) genuinely trivial (any real line
          bundle squared is trivial), and l (x) Q =~ T(RP^3) genuinely
          trivial (RP^3 =~ SO(3) is a Lie group, hence parallelizable) via
          the standard formula w(T RP^n) = (1+a)^{n+1}.  Forces
          w(Sym^2 Q) = 1 without touching METHOD A's splitting-principle
          machinery at all.  Methods A and B are asserted to agree.
  PART 5  Assemble nu = R (+) Sym^2(Q*).  Q* =~ Q as real bundles (any
          Riemannian metric gives an honest, not merely stable, bundle
          isomorphism), so w(nu) = w(Sym^2 Q).  Extract w1(nu), w2(nu),
          w3(nu).  Rank arithmetic: rank(nu) = 1 + 6 = 7 >= dim(RP^3)+1 = 4,
          the "rank-at-least-four" hypothesis Wave C names (Steenrod
          cancellation: rank > dim(base) means stably-trivial implies
          trivial on the nose) -- so nu is not merely SW-trivial but a
          genuinely trivial bundle, S(nu) =~ RP^3 x S^6 as an ACTUAL product.
  PART 6  CONTRARY CONTROLS -- prove the machinery discriminates and the
          vanishing is not a vacuous identity:
            (a) Q itself (rank 3, same base, same code path) has w1=a,
                w2=a^2, w3=a^3, ALL NONZERO;
            (b) a FORMAL rank-3 bundle Q' with w1(Q')=0, w2(Q')=b != 0,
                w3(Q')=0 (b a fresh generator, b^2=0) run through the IDENTICAL
                PART-1 closed form gives w2(Sym^2 Q') = b != 0 -- proving
                Sym^2(-)'s vanishing on RP^3's actual Q is a genuine
                consequence of Q's specific classes (w2=w1^2, w3=w1*w3-shape
                relations forced by the RP^3 ring), not an algebraic
                tautology true of every rank-3 bundle.
  PART 7  REPRODUCED [R] from `tests/dim13/mh7_dim13_link_receptacle_probe.py`
          Part 4 (the mod-3 homology of the 9-dim fiber-link L^9 = S(nu) in
          BOTH orientation branches, via the RP^3 Z[Z/2]-complex tensored
          with F_3 and the certified Serre-SS collapse): re-derived here
          independently (not copy-pasted from its printed output), then the
          orientation bit computed in PARTs 2-5 (w1(nu) = 0) is used to
          SELECT the branch programmatically.  Branch A (untwisted) is
          selected and its Betti sequence is asserted to equal the prior
          probe's own hard-coded certified value
          [1,0,0,1,0,0,1,0,0,1] (H_9(L^9;F_3) = F_3 != 0, mod-3 fundamental
          class exists on the model).
  PART 8  File-level verification: AR-1 row 6 status (LIVE, untouched by any
          of AR-1's three correction banners, unlike rows 5/8); the packet's
          D1 statement verbatim; the CURRENT-STATE.yaml receptacle-count
          fence; the GEOMETER-VS-PHYSICS-OBJECTS.md "unsettled" row;
          SC-GEN-01/SC-GEN-04 disavowal text; and (mid-flight addition) the
          post-08-11 2+1 record (HE-1/CR-B/ST-1) confirming the packet's
          five hinge-count kills (Rung-1 fence, coboundary theorem,
          Euler-degree kill, legb2's (0,0,0), PH-K1 vectorlike) all SURVIVE
          untouched -- HE-1's own subtractive n_g -> n_g-1 mechanism is a
          textually distinct, later, non-overlapping route.

CLAIM CEILING (binding, restated from the brief). This computes a
RECEPTACLE-ADMISSIBILITY bit -- which of the three surviving Z/3 homes for a
generation-count receptacle stays open after the orientation-bit gate -- NOT
a generation count and NOT an occupant of the receptacle.
`CURRENT-STATE.yaml`'s "do not ... infer a generation count" fence is not
touched: no line below outputs, suggests, or is usable as an integer
generation count.  The computation presupposes NEITHER SC-GEN-01 NOR
SC-GEN-04 (both `disavowed-by-source`, `lab/sources/source-claim-register.yaml`):
it is an orientation computation on a normal bundle in the program's boundary
differential topology, with no fermion, family index, or representation of
any gauge/family group anywhere in its construction.  The generation-count
RELATION stays UNSETTLED per `GEOMETER-VS-PHYSICS-OBJECTS.md`
(`Hom(Z/3,Z)=0` blocks direct identification) -- nothing here settles it, and
per the mid-flight addition, a future bridge from this bit to an integer
generation count would face a SECOND, independent obstruction beyond
`Hom(Z/3,Z)=0`: the source's own generation structure is ASYMMETRIC (2+1,
one representation-theoretically distinct spin-3/2 imposter -- HE-1/CR-B),
while a bare cyclic group Z/3 carries no privileged element (Aut(Z/3) = Z/2
transitively permutes its two nonzero elements) -- so a symmetric
Z/3-valued receptacle cannot, by itself, express "two true + one imposter"
without additional structure nobody has built.

Exact integer / F_2 arithmetic throughout.  No float is load-bearing
anywhere (swept).  check()-style asserts; exits nonzero on any failure.
Run from the repository root: `_local/cas-venv/bin/python
tests/channel-swings/joe_directed_z3r1_nu_trivial_w_untwisted.py`.
"""

from __future__ import annotations

import re
import sys

# ---------------------------------------------------------------------------
# Generic truncated F_2[t]/(t^N) ring: length-N coefficient vectors, index i
# is the coefficient of t^i.  Reused for RP^3's H^*(RP^3;F_2)=F_2[a]/(a^4)
# (N=4) and for the formal contrary-control ring F_2[b]/(b^2) (N=2).
# ---------------------------------------------------------------------------


def ring_mul(u, v, mutate=None):
    n = len(u)
    out = [0] * n
    for i, ci in enumerate(u):
        if not ci:
            continue
        for j, cj in enumerate(v):
            if not cj:
                continue
            k = i + j
            if k < n:
                coeff = ci * cj
                if mutate != "no_mod_reduce":
                    coeff %= 2
                out[k] = (out[k] + coeff) % 2 if mutate != "no_mod_reduce" else out[k] + coeff
    return out


def ring_add(u, v):
    return [(x + y) % 2 for x, y in zip(u, v)]


def ring_one(n):
    return [1] + [0] * (n - 1)


def ring_pow(u, k, mutate=None):
    r = ring_one(len(u))
    for _ in range(k):
        r = ring_mul(r, u, mutate=mutate)
    return r


# ---------------------------------------------------------------------------
# Multivariate F_2 polynomial engine: dict {exponent-tuple: coeff mod modn}.
# Used once, universally, for the splitting-principle identity (PART 1).
# ---------------------------------------------------------------------------


def mono_mul(m1, m2):
    return tuple(a + b for a, b in zip(m1, m2))


def padd(p1, p2, modn=2):
    out = dict(p1)
    for m, c in p2.items():
        out[m] = (out.get(m, 0) + c) % modn
    return {m: c for m, c in out.items() if c}


def pmul(p1, p2, modn=2):
    out = {}
    for m1, c1 in p1.items():
        for m2, c2 in p2.items():
            m = mono_mul(m1, m2)
            out[m] = (out.get(m, 0) + c1 * c2) % modn
    return {m: c for m, c in out.items() if c}


def padd_many(ps, modn=2):
    out = {}
    for p in ps:
        out = padd(out, p, modn=modn)
    return out


def pmul_many(ps, modn=2):
    nvars = len(next(iter(ps[0])))
    out = {(0,) * nvars: 1}
    for p in ps:
        out = pmul(out, p, modn=modn)
    return out


def pone(nvars):
    return {(0,) * nvars: 1}


def pvar(i, nvars):
    e = [0] * nvars
    e[i] = 1
    return {tuple(e): 1}


def peq(p1, p2):
    return {m: c for m, c in p1.items() if c} == {m: c for m, c in p2.items() if c}


# ---------------------------------------------------------------------------
# Rank-F_3 linear algebra + Betti numbers -- REPRODUCED [R] verbatim in
# structure from tests/dim13/mh7_dim13_link_receptacle_probe.py Part 4.
# ---------------------------------------------------------------------------


def rank_f3(rows):
    m = [[x % 3 for x in row] for row in rows]
    rank = 0
    n_rows = len(m)
    n_cols = len(m[0]) if n_rows else 0
    piv_row = 0
    for col in range(n_cols):
        sel = next((r for r in range(piv_row, n_rows) if m[r][col] % 3), None)
        if sel is None:
            continue
        m[piv_row], m[sel] = m[sel], m[piv_row]
        inv = 1 if m[piv_row][col] % 3 == 1 else 2
        m[piv_row] = [(inv * x) % 3 for x in m[piv_row]]
        for r in range(n_rows):
            if r != piv_row and m[r][col] % 3:
                f = m[r][col]
                m[r] = [(m[r][c] - f * m[piv_row][c]) % 3 for c in range(n_cols)]
        rank += 1
        piv_row += 1
    return rank


def homology_dims_f3(dims, boundaries):
    top = len(dims) - 1

    def rank_of(k):
        mat = boundaries.get(k)
        if not mat or k < 1 or k > top or dims[k] == 0 or dims[k - 1] == 0:
            return 0
        return rank_f3(mat)

    return [dims[k] - rank_of(k) - rank_of(k + 1) for k in range(top + 1)]


# ---------------------------------------------------------------------------
# Text-verification helpers.
# ---------------------------------------------------------------------------


def normspace(s):
    return re.sub(r"\s+", " ", s)


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


# ===========================================================================
# THE PIPELINE, parameterized by an optional machinery-corruption mutation.
# Returns (results dict, list of (name, passed, detail) tuples).
# ===========================================================================

MUTATIONS = (
    "wrong_w_gamma",
    "wrong_closed_form_w3",
    "wrong_TRP3_power",
    "wrong_rank_Sym2Q",
    "flip_Q_dual_class",
    "wrong_branch_selector",
    "poly_engine_mod3",
    "drop_deg1_universal_check",
    "invert_contrary_control",
    "no_mod_reduce_ring",
)


def run_pipeline(mutate=None):
    checks = []

    def check(name, cond, detail=""):
        checks.append((name, bool(cond), detail))

    # -----------------------------------------------------------------
    # PART 1 -- universal splitting-principle identity, 3 formal roots.
    # -----------------------------------------------------------------
    modn = 3 if mutate == "poly_engine_mod3" else 2
    NV = 3
    one = pone(NV)
    x1, x2, x3 = pvar(0, NV), pvar(1, NV), pvar(2, NV)
    lhs = pmul_many(
        [
            padd_many([one, x1, x2], modn=modn),
            padd_many([one, x1, x3], modn=modn),
            padd_many([one, x2, x3], modn=modn),
        ],
        modn=modn,
    )
    e1 = padd_many([x1, x2, x3], modn=modn)
    e2 = padd_many([pmul(x1, x2, modn=modn), pmul(x1, x3, modn=modn), pmul(x2, x3, modn=modn)], modn=modn)
    e3 = pmul_many([x1, x2, x3], modn=modn)
    rhs = padd_many([one, pmul(e1, e1, modn=modn), e2, pmul(e1, e2, modn=modn), e3], modn=modn)
    check(
        "P1.identity: (1+x1+x2)(1+x1+x3)(1+x2+x3) == 1+(e1^2+e2)+(e1*e2+e3) [F_2 polynomial identity]",
        peq(lhs, rhs),
        f"lhs={lhs} rhs={rhs}",
    )
    deg1_terms = {m: c for m, c in lhs.items() if sum(m) == 1}
    if mutate == "drop_deg1_universal_check":
        # corrupt the EXPECTATION, not the computation: wrongly expect a
        # nonzero degree-1 term.  Must be caught as a mismatch, not a crash.
        check("P1.no_w1_term: w(Sym^2 Q) has zero degree-1 (w1) coefficient identically", deg1_terms != {})
    else:
        check("P1.no_w1_term: w(Sym^2 Q) has zero degree-1 (w1) coefficient identically", deg1_terms == {})

    # -----------------------------------------------------------------
    # PART 2 -- H^*(RP^3;F_2) = F_2[a]/(a^4); derive w(Q) from gamma(+)Q=V.
    # -----------------------------------------------------------------
    N = 4
    A = [0, 1, 0, 0]
    ONE = ring_one(N)
    w_gamma = [1, 0, 1, 0] if mutate == "wrong_w_gamma" else [1, 1, 0, 0]  # correct: w(gamma)=1+a
    w_Q = [1, 1, 1, 1]  # candidate 1+a+a^2+a^3
    prod = ring_mul(w_gamma, w_Q, mutate=("no_mod_reduce" if mutate == "no_mod_reduce_ring" else None))
    check(
        "P2.gamma_Q_trivial: w(gamma)*w(1+a+a^2+a^3) == 1  [gamma (+) Q = V = R^4 trivial]",
        prod == ONE,
        f"w_gamma={w_gamma} product={prod}",
    )
    w1_Q, w2_Q, w3_Q = A, ring_pow(A, 2), ring_pow(A, 3)
    check("P2.w1Q: w1(Q) = a", w1_Q == [0, 1, 0, 0])
    check("P2.w2Q: w2(Q) = a^2", w2_Q == [0, 0, 1, 0])
    check("P2.w3Q: w3(Q) = a^3", w3_Q == [0, 0, 0, 1])

    # -----------------------------------------------------------------
    # PART 3 -- METHOD A: plug PART-2 values into PART-1's closed form.
    # -----------------------------------------------------------------
    e1v, e2v, e3v = w1_Q, w2_Q, w3_Q
    deg2_term = ring_add(ring_mul(e1v, e1v), e2v)
    if mutate == "wrong_closed_form_w3":
        deg3_term = ring_add(ring_mul(e1v, e3v), e2v)  # WRONG: e1*e3 + e2, not e1*e2 + e3
    else:
        deg3_term = ring_add(ring_mul(e1v, e2v), e3v)
    w_Sym2Q_methodA = ring_add(ring_add(ONE, deg2_term), deg3_term)
    check(
        "P3.methodA: w(Sym^2 Q) = 1 + (w1^2+w2) + (w1*w2+w3) evaluates to [1,0,0,0]",
        w_Sym2Q_methodA == ONE,
        f"got {w_Sym2Q_methodA}",
    )

    # -----------------------------------------------------------------
    # PART 4 -- METHOD B: independent cross-check via Sym^2(V) triviality
    # and RP^3 parallelizability (disjoint machinery from METHOD A).
    # -----------------------------------------------------------------
    power = 3 if mutate == "wrong_TRP3_power" else 4  # correct exponent is n+1=4 for RP^3
    w_TRP3 = ring_pow(w_gamma, power)
    check(
        "P4.TRP3_trivial: w(T RP^3) = (1+a)^4 == 1  [RP^3 =~ SO(3), Lie group, parallelizable]",
        w_TRP3 == ONE,
        f"(1+a)^{power} = {w_TRP3}",
    )
    w_Sym2l = ONE  # any real line bundle squared is canonically trivial
    # Solve Sym^2(V) = Sym^2(l) (+) (l(x)Q) (+) Sym^2(Q) genuinely trivial:
    # w(Sym^2 l) * w(l tensor Q) * w(Sym^2 Q) = w(Sym^2 V) = 1.
    # Since w(Sym^2 l)=1 and w(l tensor Q)=w(T RP^3), METHOD B's independent
    # value for w(Sym^2 Q) is forced to satisfy: w_TRP3 * w(Sym^2Q)_B = 1.
    # Solve by trial over the ring (small, N=4): find x with w_TRP3 * x = ONE.
    candidates = [
        [c0, c1, c2, c3]
        for c0 in (0, 1)
        for c1 in (0, 1)
        for c2 in (0, 1)
        for c3 in (0, 1)
    ]
    solutions = [c for c in candidates if ring_mul(w_TRP3, c) == ONE]
    w_Sym2Q_methodB = solutions[0] if len(solutions) == 1 else (solutions[0] if solutions else None)
    check(
        "P4.methodB_unique_solution: w_TRP3 * x = 1 has a UNIQUE solution x in F_2[a]/(a^4)",
        len(solutions) == 1,
        f"solutions={solutions}",
    )
    check(
        "P4.methodB: independent solve gives w(Sym^2 Q) = [1,0,0,0], matching METHOD A",
        w_Sym2Q_methodB == w_Sym2Q_methodA,
        f"methodB={w_Sym2Q_methodB} methodA={w_Sym2Q_methodA}",
    )
    check(
        "P4.SymV_reconstruction: w(Sym^2 l)*w(l(x)Q)*w(Sym^2 Q) == w(Sym^2 V) == 1",
        ring_mul(ring_mul(w_Sym2l, w_TRP3), w_Sym2Q_methodA) == ONE,
    )

    # -----------------------------------------------------------------
    # PART 5 -- assemble nu = R (+) Sym^2(Q*); rank arithmetic.
    # -----------------------------------------------------------------
    if mutate == "flip_Q_dual_class":
        w_QstarSym2 = ring_add(w_Sym2Q_methodA, A)  # WRONG: spuriously add "a"
    else:
        w_QstarSym2 = w_Sym2Q_methodA  # Q* =~ Q as real bundles (metric iso)
    w_nu = w_QstarSym2  # w(R)=1 contributes nothing to the product
    w1_nu, w2_nu, w3_nu = w_nu[1], w_nu[2], w_nu[3]
    check("P5.w1_nu: w1(nu) = 0", w1_nu == 0, f"w(nu)={w_nu}")
    check("P5.w2_nu: w2(nu) = 0", w2_nu == 0, f"w(nu)={w_nu}")
    check("P5.w3_nu: w3(nu) = 0", w3_nu == 0, f"w(nu)={w_nu}")

    rank_l, rank_Q = 1, 3
    rank_Sym2Q = rank_Q * rank_Q if mutate == "wrong_rank_Sym2Q" else rank_Q * (rank_Q + 1) // 2
    rank_nu = 1 + rank_Sym2Q
    check("P5.rank_Sym2Q: rank(Sym^2 Q) = C(3+1,2) = 6", rank_Sym2Q == 6, f"got {rank_Sym2Q}")
    check("P5.rank_nu: rank(nu) = 1 + 6 = 7", rank_nu == 7, f"got {rank_nu}")
    dim_RP3 = 3
    check(
        "P5.rank_at_least_four: rank(nu)=7 >= dim(RP^3)+1=4  [Wave C's cancellation-theorem hypothesis]",
        rank_nu >= dim_RP3 + 1,
    )
    check(
        "P5.SymV_rank_sum: rank(Sym^2 l)+rank(l(x)Q)+rank(Sym^2 Q) = 1+3+6 = 10 = rank Sym^2(R^4)",
        1 + 3 + rank_Sym2Q == 10,
    )

    # -----------------------------------------------------------------
    # PART 6 -- contrary controls: prove the machinery discriminates.
    # -----------------------------------------------------------------
    q_nonzero = (w1_Q != [0] * N) and (w2_Q != [0] * N) and (w3_Q != [0] * N)
    if mutate == "invert_contrary_control":
        check("P6a.contrary_Q: w(Q) is claimed TRIVIAL (deliberately wrong expectation)", not q_nonzero)
    else:
        check("P6a.contrary_Q: w1(Q),w2(Q),w3(Q) all NONZERO (same code path, different bundle)", q_nonzero)

    # Formal contrary bundle Q': rank-3, w1=0, w2=b (b^2=0), w3=0, in F_2[b]/(b^2).
    NB = 2
    ONEB = ring_one(NB)
    B = [0, 1]
    w1_Qp, w2_Qp, w3_Qp = [0, 0], B, [0, 0]
    deg2_Qp = ring_add(ring_mul(w1_Qp, w1_Qp), w2_Qp)  # e1^2+e2 = 0+b = b
    deg3_Qp = ring_add(ring_mul(w1_Qp, w2_Qp), w3_Qp)  # e1*e2+e3 = 0+0 = 0
    w_Sym2Qp = ring_add(ring_add(ONEB, deg2_Qp), deg3_Qp)
    check(
        "P6b.contrary_formal: Sym^2(Q') for a FORMAL Q' with w1=0,w2=b!=0,w3=0 has w2(Sym^2 Q')=b != 0",
        w_Sym2Qp == ring_add(ONEB, B) and w_Sym2Qp != ONEB,
        f"w(Sym^2 Q')={w_Sym2Qp}  -- vanishing on RP^3's actual Q is NOT a vacuous identity",
    )

    # -----------------------------------------------------------------
    # Planted-false facts, checked to be OBSERVED FALSE (not asserted true).
    # -----------------------------------------------------------------
    naive_w1_eq_a = (w1_nu == 1)
    check("PF1.naive_w1_wrong: 'w1(nu) equals w1(Q)=a (nonzero)' is FALSE", naive_w1_eq_a is False)
    rank_eq = (rank_nu == rank_Q)
    check("PF2.rank_collision_wrong: 'rank(nu) equals rank(Q)' is FALSE", rank_eq is False)
    classes_eq = (w_nu == w_Q)
    check("PF3.classes_collision_wrong: 'Sym^2(Q) and Q share the same total SW class' is FALSE", classes_eq is False)
    wrong_power = ring_pow(w_gamma, 3)
    check(
        "PF4.wrong_exponent_wrong: '(1+a)^3 equals (1+a)^4 in this ring' is FALSE",
        wrong_power != w_TRP3,
        f"(1+a)^3={wrong_power} (1+a)^4={w_TRP3}",
    )
    check(
        "PF5.wrong_exponent_nontrivial: the WRONG exponent (1+a)^3 is itself NONTRIVIAL (!=1)",
        wrong_power != ONE,
        f"(1+a)^3={wrong_power}",
    )

    # -----------------------------------------------------------------
    # PART 7 -- reproduce [R] the mh7 probe's Part-4 branch homology, then
    # SELECT the branch using w1(nu) computed above (not hardcoded).
    # -----------------------------------------------------------------
    betti_rp3_triv = homology_dims_f3([1, 1, 1, 1], {1: [[0]], 2: [[2]], 3: [[0]]})
    betti_rp3_sign = homology_dims_f3([1, 1, 1, 1], {1: [[1]], 2: [[0]], 3: [[1]]})
    check(
        "P7.R_rp3_triv: [R] H_*(RP^3;F_3 trivial) Betti = [1,0,0,1]  (reproduced from mh7 probe Part 4)",
        betti_rp3_triv == [1, 0, 0, 1],
    )
    check(
        "P7.R_rp3_sign: [R] H_*(RP^3;F_3 sign-twisted) Betti = [0,0,0,0]  (reproduced)",
        betti_rp3_sign == [0, 0, 0, 0],
    )
    BASE_RANGE = range(0, 4)
    link_A = [0] * 10
    link_B = [0] * 10
    for p in BASE_RANGE:
        link_A[p] += betti_rp3_triv[p]
        link_B[p] += betti_rp3_triv[p]
        link_A[p + 6] += betti_rp3_triv[p]
        link_B[p + 6] += betti_rp3_sign[p]
    check(
        "P7.R_branchA: [R] untwisted branch Betti(L^9;F_3) = [1,0,0,1,0,0,1,0,0,1]  (reproduced)",
        link_A == [1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    )
    check(
        "P7.R_branchB: [R] twisted branch Betti(L^9;F_3) = [1,0,0,1,0,0,0,0,0,0]  (reproduced)",
        link_B == [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    )
    # Orientation-bit branch selection: w1(nu)=0 => trivial local system on
    # H^*(fiber) => UNTWISTED (branch A).  w1(nu)!=0 would select branch B.
    if mutate == "wrong_branch_selector":
        selected_branch = "B" if w1_nu == 0 else "A"  # deliberately inverted rule
    else:
        selected_branch = "A" if w1_nu == 0 else "B"
    selected_betti = link_A if selected_branch == "A" else link_B
    check(
        "P7.branch_selected: w1(nu)=0 selects UNTWISTED branch A (not hardcoded -- computed from PART 5)",
        selected_branch == "A",
        f"w1(nu)={w1_nu} -> branch {selected_branch}",
    )
    check(
        "P7.branch_matches_prior_certificate: selected branch's Betti sequence == mh7 probe's certified value",
        selected_betti == [1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
        f"selected={selected_betti}",
    )
    h9_nonzero = selected_betti[9] != 0
    check(
        "P7.H9_nonzero: H_9(L^9;F_3) != 0 on the selected branch -- mod-3 fundamental class EXISTS on the model",
        h9_nonzero,
    )
    check(
        "PF6.branches_differ: 'branch A and branch B have identical Betti sequences' is FALSE",
        link_A != link_B,
    )

    results = {
        "w_nu": w_nu,
        "w1_nu": w1_nu,
        "w2_nu": w2_nu,
        "w3_nu": w3_nu,
        "rank_nu": rank_nu,
        "selected_branch": selected_branch,
        "selected_betti": selected_betti,
    }
    return results, checks


# ===========================================================================
# PART 8 -- file-level / textual verification (run once, not mutated).
# ===========================================================================


def file_checks():
    checks = []

    def check(name, cond, detail=""):
        checks.append((name, bool(cond), detail))

    packet = "explorations/z3-receptacle-design-packet-2026-08-11.md"
    register = "lab/process/improvement-register-2026-08-03.md"
    current_state = "CURRENT-STATE.yaml"
    geometer = "GEOMETER-VS-PHYSICS-OBJECTS.md"
    source_register = "lab/sources/source-claim-register.yaml"
    wave_c = "explorations/resolver-wave-c-rebased-q5-q6-mh7-2026-08-03.md"
    ar1 = "lab/active-research/joe-directed/archaeology/ar1-dropped-commitments-ledger-2026-08-15.md"
    hinge_panel = "lab/process/hinge-panel-synthesis-2026-08-03.md"
    he1 = "lab/active-research/joe-directed/high-energy-two-plus-one/he1-imposter-separation-invariant-2026-08-14.md"
    crb = "lab/active-research/joe-directed/carrier/crb-carrier-is-four-corners-not-one-weyl-2026-08-15.md"
    st1 = "lab/active-research/joe-directed/seesaw-tradeoff/st1-tradeoff-dissolves-into-sg4-bit-2-2026-08-16.md"

    try:
        packet_t = read(packet)
        register_t = read(register)
        cs_t = read(current_state)
        geo_t = read(geometer)
        src_t = read(source_register)
        wc_t = read(wave_c)
        ar1_t = read(ar1)
        hinge_t = read(hinge_panel)
        he1_t = read(he1)
        crb_t = read(crb)
        st1_t = read(st1)
    except OSError as exc:
        check("P8.files_readable: all cited files open cleanly", False, str(exc))
        return checks

    check("P8.files_readable: all cited files open cleanly", True)

    # --- the packet's own D1 statement, verbatim -------------------------
    check(
        "P8.packet_D1_decomp: packet states 'nu ~ R (+) Sym^2(Q*)' verbatim",
        "nu ~ R (+) Sym^2(Q*)" in packet_t,
    )
    check(
        "P8.packet_D1_rank4: packet cites 'rank-at-least-four' classification requirement",
        "rank-at-least-four" in packet_t,
    )
    check(
        "P8.packet_D2_present: packet's D2 names the orientation bit `w` and both branches",
        "orientation bit `w`" in packet_t and "untwisted" in packet_t and "twisted" in packet_t,
    )

    # --- Wave C's precise unproved precondition ---------------------------
    check(
        "P8.waveC_precondition: Wave C types 'w1=w2=w3=0' as the UNPROVED precondition, verbatim",
        "w1=w2=w3=0" in wc_t and "rank-at-least-four" in wc_t,
    )

    # --- register M-H5 row --------------------------------------------
    check(
        "P8.register_MH5: register row M-H5 prices 'Verify ν decomposition (half-day); SW/triviality check (hours)'",
        "Verify ν decomposition (half-day); SW/triviality check (hours)" in register_t,
    )
    check(
        "P8.register_MH5_object: register M-H5 states the object 'ν ≅ ℝ ⊕ Sym²(Q*)'",
        "ν ≅ ℝ ⊕ Sym²(Q*)" in register_t,
    )

    # --- CURRENT-STATE.yaml fence ---------------------------------------
    check(
        "P8.fence_no_count: CURRENT-STATE.yaml next_condition forbids inferring a generation count",
        "infer a" in normspace(cs_t) and "generation count" in normspace(cs_t)
        and "infer a generation count" in normspace(cs_t),
    )

    # --- GEOMETER-VS-PHYSICS-OBJECTS.md unsettled row --------------------
    check(
        "P8.geometer_unsettled: generation-count relation typed 'unsettled', not settled",
        "The relation is **unsettled**" in geo_t,
    )
    check(
        "P8.geometer_hom: Hom(Z/3,Z)=0 blocks direct additive identification, verbatim",
        "`Hom(Z/3,Z)=0` blocks a direct additive identification" in geo_t,
    )

    # --- SC-GEN-01 / SC-GEN-04 disavowals ---------------------------------
    check("P8.scgen01_id: register carries 'id: SC-GEN-01'", "id: SC-GEN-01" in src_t)
    check(
        "P8.scgen01_text: SC-GEN-01 verbatim disavowal present",
        "we do not believe that nature has simply repeated herself three times" in src_t,
    )
    check("P8.scgen04_id: register carries 'id: SC-GEN-04'", "id: SC-GEN-04" in src_t)
    check(
        "P8.scgen04_text: SC-GEN-04 verbatim disavowal present",
        "it is not a true generation as it has a different representation structure" in src_t,
    )
    # both disavowals graded disavowed-by-source (count occurrences, not just presence)
    check(
        "P8.scgen_disavowed_grade: 'disavowed-by-source' appears (SC-GEN-01/04's core grade)",
        "disavowed-by-source" in src_t,
    )

    # --- AR-1 row 6 status: LIVE, untouched by the three correction banners
    row6_text = "referee the normal-bundle decomposition and compute the orientation bit `w`"
    check("P8.ar1_row6_text: AR-1's historical worklist row 6 names this exact work", row6_text in ar1_t)
    check(
        "P8.ar1_row6_hostile: AR-1's hostile-review sample confirms row 6 LIVE -> LIVE, 'correct'",
        "| `Z/3` orientation bit `w` | LIVE | LIVE | correct |" in ar1_t,
    )
    banners = [
        "**CORRECTION IV-20260815",
        "**CORRECTION AR1-CB-20260816",
        "**CORRECTION AR1-R8-20260816",
    ]
    check(
        "P8.ar1_three_banners: AR-1 carries exactly the three named correction banners",
        all(b in ar1_t for b in banners) and ar1_t.count("**CORRECTION ") == 3,
    )
    check(
        "P8.ar1_row6_untouched: no correction banner issues a 'Row 6 is ...' or 'row 6 is ...' retype",
        "Row 6 is" not in ar1_t and "row 6 is" not in ar1_t,
    )
    check(
        "P8.ar1_rows_5_8_touched: rows 5 and 8 (contrast case) ARE named by corrections, unlike row 6",
        "Row 5 is" in ar1_t and "worklist row 8 is" in ar1_t,
    )
    check(
        "P8.ar1_row7_closed: row 7 (VZ §18.3) is named among the IV-20260815 closed rows, unlike row 6",
        "rows `1`, `2`, `3`, `4`, `7`, and `16`" in ar1_t,
    )

    # --- the packet's five hinge/2+1 kills, and the post-08-11 record ----
    five_kills = (
        "HINGE AS COUNT: dead FIVE ways" in hinge_t
        and "the standing Rung-1 fence" in hinge_t
        and "the coboundary" in hinge_t
        and "theorem (the defect is δR, exact, class zero" in hinge_t
        and "Euler-degree kill (the graded contribution" in hinge_t
        and "legb2's computed (0,0,0)" in hinge_t
        and "phenomenologically PH-K1 (the block" in hinge_t
    )
    check(
        "P8.five_kills_recorded: hinge-panel-synthesis records all five hinge-as-count kills verbatim",
        five_kills,
    )
    check(
        "P8.legb2_origin: hinge-panel-synthesis records legb2's (0,0,0) cross-term result, cited by the packet's kill #4",
        "legb2 had already evaluated the cross-term's index classes" in hinge_t
        and "(0,0,0)" in hinge_t,
    )
    check(
        "P8.legb2_untouched_post0811: legb2 is NOT mentioned anywhere in HE-1, CR-B or ST-1 -- silence, not reuse or supersession",
        "legb2" not in he1_t and "legb2" not in crb_t and "legb2" not in st1_t,
    )
    check(
        "P8.PHK1_reused_by_HE1: HE-1 explicitly corroborates PH-K1-KINEMATIC as a THIRD independent arrival (reused, not superseded)",
        "PH-K1-KINEMATIC` (draft §9) and the Witten-1983" in he1_t,
    )
    check(
        "P8.PHK1_reused_by_CRB: CR-B's own prior-art table lists PH-K1-KINEMATIC as CONFIRMED, unchanged",
        "PH-K1-KINEMATIC`: the `Cl(9,5)` 128 block is kinematically vectorlike" in crb_t
        and "CONFIRMED" in crb_t,
    )
    check(
        "P8.HE1_mechanism_distinct: HE-1's 2+1 mechanism (Pati-Salam 16/144 pairing ladder) is textually distinct from the hinge/RS 4+10 mechanism the five kills target",
        "n_g` chiral families plus one `144` leaves net chirality `n_g - 1`" in he1_t
        and "Rung-1 fence" not in he1_t,
    )
    check(
        "P8.CRB_four_corners: CR-B's four-corner/class result is about ambient field-space declaration, not the hinge/RS split",
        "four corners partition into" in normspace(crb_t) and "class-homogeneous halves" in crb_t,
    )
    check(
        "P8.ST1_channel1_unchanged: ST-1 explicitly states channel 1 (2+1, n_g->n_g-1) is UNCHANGED by its own work",
        "input condition is UNCHANGED" in normspace(st1_t) and "n_g` remains an input" in normspace(st1_t),
    )

    return checks


# ===========================================================================
# Self-test.
# ===========================================================================


def self_test():
    ok = True
    print("SELF-TEST: verifying the CLEAN baseline (mutate=None) passes first...")
    try:
        _results, checks = run_pipeline(mutate=None)
    except Exception as exc:  # noqa: BLE001
        print(f"SELF-TEST: clean baseline CRASHED: {exc!r}")
        print("SELF-TEST FAILED")
        return 1
    fails = [c for c in checks if not c[1]]
    if fails:
        print(f"SELF-TEST: clean baseline does NOT pass ({len(fails)} failing); mutations NOT run")
        print("SELF-TEST FAILED")
        return 1
    print(f"SELF-TEST: clean baseline green ({len(checks)}/{len(checks)}). Running {len(MUTATIONS)} mutations...")

    for mutation in MUTATIONS:
        try:
            _results, checks = run_pipeline(mutate=mutation)
        except Exception as exc:  # noqa: BLE001
            # A crash is explicitly NOT a valid catch: it did not produce a
            # genuine named [FAIL] line, it aborted the run.  Per the brief,
            # crash-catches are rejected -- this mutation FAILS the selftest.
            print(f"SELF-TEST: mutation '{mutation}' CRASHED instead of failing a named check: {exc!r}")
            print(f"SELF-TEST: [CRASH-NOT-CAUGHT] '{mutation}' -- rejected as a non-catch")
            ok = False
            continue
        mfails = [c for c in checks if not c[1]]
        if mfails:
            names = ", ".join(c[0] for c in mfails)
            print(f"SELF-TEST: mutation '{mutation}' correctly caught -- {len(mfails)} [FAIL]: {names}")
        else:
            print(f"SELF-TEST: mutation '{mutation}' NOT caught -- all checks passed despite corruption")
            ok = False

    print("SELF-TEST " + ("GREEN" if ok else "FAILED"))
    return 0 if ok else 1


# ===========================================================================
# Main.
# ===========================================================================


def main():
    if "--selftest" in sys.argv or "--self-test" in sys.argv:
        sys.exit(self_test())

    results, checks = run_pipeline(mutate=None)
    checks += file_checks()

    fail = []
    for name, passed, detail in checks:
        tag = "ok  " if passed else "FAIL"
        print(f"  [{tag}] {name}" + (f"  --  {detail}" if detail else ""))
        if not passed:
            fail.append(name)

    print("\n" + "=" * 78)
    print(f"w(nu) = {results['w_nu']}   =>   w1={results['w1_nu']}  w2={results['w2_nu']}  w3={results['w3_nu']}")
    print(f"rank(nu) = {results['rank_nu']}   selected branch = {results['selected_branch']} (untwisted)"
          if results["selected_branch"] == "A"
          else f"rank(nu) = {results['rank_nu']}   selected branch = {results['selected_branch']} (twisted)")
    print("=" * 78)

    n = len(checks)
    if fail:
        print(f"\n  {len(fail)}/{n} FAILURE(S): {fail}")
    else:
        print(f"\n  CERTIFICATE: {n}/{n} checks pass.  w1(nu)=w2(nu)=w3(nu)=0 (nu genuinely trivial, "
              "rank 7 >= 4); orientation bit w = UNTWISTED (branch A); mod-3 fundamental class "
              "exists on the model.  exit 0")

    assert not fail, f"z3r1 probe failures: {fail}"
    sys.exit(0)


if __name__ == "__main__":
    main()
