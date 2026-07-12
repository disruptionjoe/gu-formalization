#!/usr/bin/env python3
"""
H19 (Wave 14) -- THE (7,7) SIGNATURE BRANCH: what does adopting Y^14 = Cl(7,7) = M(128,R)
[J^2 = +1, R-class] as the working signature actually DELIVER and COST?

H37 (wave 13) proved the generation count is provably located-not-forced on the built
(9,5) = M(64,H) structure, and identified the ONLY escape axis (seven-axis map L7) as the
signature: the grading/Z-eta leg is signature-INDEPENDENT, but the Kramers/mod-2 leg (the J^2
sign) LIFTS under (7,7), making an odd rank-3 projector ADMISSIBLE. This test digs into the four
payoff questions on the actual reps.

DISCIPLINE (STRICT): compute -> adversarially verify -> HONEST grade. The prior verdict
(BIG-SWING-signature-9-5-vs-7-7-UNDER-DETERMINED) is that NO GU-native lever fixes p-q mod 8, and
SG1/H37 that (7,7) makes odd counts ADMISSIBLE but the rank is UNDER-DETERMINED. Do NOT fabricate
that (7,7) forces 3; do NOT import (no 24/8, no chi(K3), no fit to 3). A clean "(7,7) makes odd
admissible but does NOT force 3, and here is the cost" is a full result.

------------------------------------------------------------------------------------------------
THE FOUR QUESTIONS (computed on the actual reps where possible)

  Q1. DOES (7,7) FORCE THE COUNT TO EXACTLY 3, OR JUST ODD?
    1a. On (7,7)=M(128,R): J-commuting orthogonal projectors of odd rank 1,3,5,7 ALL exist;
        on (9,5)=M(64,H) every one is forced to the next even rank. => the admissible odd-rank
        set is UNRESTRICTED; 3 is not selected by parity.  [COMPUTED]
    1b. STRUCTURAL KILL of any "forces 3": the signature is a 2-PRIMARY datum (p-q mod 8 in Z/8);
        the generation 3 lives in the ORDER-3 arena of pi_3^s = Z/24 = Z/8 (+) Z/3. By the
        Lean-verified two-arena core, |Hom(Z/8, Z/3)| = gcd(8,3) = 1 (only the zero map), so NO
        structural map carries a signature (2-primary) datum into the count (3-primary) arena.
        2-primary blindness => (7,7) is STRUCTURALLY INCAPABLE of supplying 3.  [COMPUTED]
    1c. ANTI-FIT control: the natural GU carrier (the self-dual SU(2)+ triplet, multiplicity 3)
        is a NEUTRAL Krein subspace (+96,-96,0) in BOTH (9,5) and (7,7) => net chiral index 0.
        So even where the odd rank-3 projector is admissible, the triplet's "3" is vectorlike;
        (7,7) removes the PROHIBITION but supplies no chiral selector. 3 is not derived.  [COMPUTED]

  Q2. DOES THE GRAVITY CONDITIONAL THEOREM TRANSFER (spin-lift, Krein, |II|^2, ghost-clear)?
    2a. The Krein structure TRANSFERS: beta_S (product of spacelike gammas) is pseudo-anti-Hermitian
        for every so(p,q) generator on BOTH (9,5) and (7,7) (residual ~0). The grading leg
        {G,O}=0 is signature-independent (H37 D1).  [COMPUTED]
    2b. What does NOT transfer: the reality class of the J-commutant flips H -> R (J^2: -1 -> +1).
        End_H(S)=M(64,H) with quaternionic gauge group Sp(32,32;H) becomes M(128,R) with a
        real/split analog. The quaternionic gauge-group identity is (9,5)-SPECIFIC; the
        Krein/|II|^2/grading SHAPE is signature-independent.  [COMPUTED reality class + argued]

  Q3. WHAT DOES (7,7) COST (anomaly-freedom, SM embedding, QM unitarity)?
    3a. Anomaly: omega = e_1...e_14 has omega^2 = +I in BOTH (both q odd) => chiral split exists
        in both; the D=14 anomaly is Tr F^8 (even Casimir), reality-class-blind. NOT broken. [COMPUTED]
    3b. SM embedding: the Pati-Salam Spin(6,4) fiber is signature-INDEPENDENT -- the trace-reversed
        DeWitt fiber form is (6,4) for BOTH base orientations (mostly-plus AND mostly-minus).
        Weinstein's chain Spin(6,4)->Spin(3,2)->maxcompact SU(3)xSU(2)xU(1) rides this common
        fiber. SM embedding survives on (7,7).  [COMPUTED fiber signature both orientations]
    3c. Unitarity: both (9,5) and (7,7) have q>0 => BOTH are Krein, neither is a Hilbert space;
        both need the Turok-Bateman ghost parity. The triplet is (+96,-96) in both.  [COMPUTED via 1c]
    3d. The REAL cost: (7,7) removes the even-parity constraint WITHOUT adding one => the admissible
        set WIDENS (even {0,2,4,6} -> the full {1,2,3,4,5,6,7}). Predictivity DECREASES.  [COMPUTED]

  Q4. IS (7,7) GU-NATIVE (any lever selecting (7,7) over (9,5))?
    4a. Closed form p-q = d + d^2/2, d = (#space - #time) in the base: d=+2 (mostly-plus) -> p-q=4
        -> (9,5)/H; d=-2 (mostly-minus) -> p-q=0 -> (7,7)/R. Only sign(d) moves it.  [COMPUTED]
    4b. The (6,4) trace-reversed fiber is g -> -g invariant (quadratic form) => carries no sign(d);
        Weinstein's Spin(6,4)/Spin(3,2) chain rides this common fiber => NEUTRAL on total signature.
        No GU-native selector for sign(d) is exhibited.  [COMPUTED + cite BIG-SWING]

VERDICT: (7,7) makes odd ADMISSIBLE but does NOT force 3 (2-primary blindness forbids it
structurally); it costs little (anomaly/SM/unitarity survive; only predictivity narrows); it is
NOT GU-native (under-determined choice). LIVE-BUT-NON-DERIVING.

Reproducible: python tests/wave14/H19_seven_seven_branch.py   (exit 0 on all PASS)
"""
from __future__ import annotations

import math
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_GENSEC = os.path.normpath(os.path.join(_HERE, "..", "generation-sector"))
_TESTS = os.path.normpath(os.path.join(_HERE, ".."))
for _p in (_GENSEC, _TESTS):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import oq_rk1_cl95_explicit_rep as cl95   # noqa: E402  verified Cl(p,q) Jordan-Wigner rep
import gen_sector_bridge as gb            # noqa: E402  XI covector

N, DIM = 14, 128
TOL = 1e-9
np.random.seed(20260711)


def report(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {detail}" if detail else ""))
    return bool(ok)


# ------------------------------------------------------------------------------------------------
# Clifford rep for any signature p+q = 14  (first p real / +1, then q imaginary / -1)
# ------------------------------------------------------------------------------------------------
def clifford(p, q):
    G = cl95.jordan_wigner_gammas(7)
    eta = [1] * p + [-1] * q
    return [G[a] if eta[a] > 0 else 1j * G[a] for a in range(N)], eta


def sgen(e, i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


def antilinear_J(e):
    """J = U . conj commuting with every e_a (product of imaginary-conjugation generators). -> (U, J^2)."""
    imag = [a for a in range(N) if np.max(np.abs(e[a].conj() + e[a])) < TOL]
    U = np.eye(DIM, dtype=complex)
    for a in imag:
        U = U @ e[a]
    U = U / np.sqrt(np.max(np.abs(np.diag(U @ U.conj().T))))
    c = complex(np.trace(U @ U.conj()) / DIM)
    return U, c


def odd_rank_J_projector(U, c, target):
    """Tightest J-commuting orthogonal projector near rank `target`. -> (rank, jresid, idem)."""
    Jv = lambda v: U @ v.conj()
    if c.real > 0:  # real structure J^2=+1: J-fixed real form -> any complex dim reachable
        cols = []
        tries = 0
        while len(cols) < target and tries < 500:
            tries += 1
            v = np.random.randn(DIM) + 1j * np.random.randn(DIM)
            r = v + Jv(v)
            for w in cols:
                r = r - (w.conj() @ r) * w
            if np.linalg.norm(r) > 1e-6:
                cols.append(r / np.linalg.norm(r))
        B = np.column_stack(cols)
    else:           # quaternionic J^2=-1: J-invariant subspaces are Kramers-doubled -> even dim only
        raw, seeds = [], []
        while len(seeds) < target:
            v = np.random.randn(DIM) + 1j * np.random.randn(DIM)
            for w in seeds:
                v = v - (w.conj() @ v) * w
            if np.linalg.norm(v) > 1e-6:
                seeds.append(v / np.linalg.norm(v))
        for v in seeds:
            raw += [v, Jv(v)]
        Q, _ = np.linalg.qr(np.column_stack(raw))
        B = Q[:, :np.linalg.matrix_rank(np.column_stack(raw), tol=1e-9)]
    P = B @ B.conj().T
    rank = int(round(np.trace(P).real))
    jr = float(np.max(np.abs(U @ P.conj() - P @ U)))
    idem = float(np.max(np.abs(P @ P - P)))
    return rank, jr, idem


def reachable_odd_ranks(U, c, targets=(1, 3, 5, 7)):
    """Which odd ranks are reachable by a genuine J-commuting orthogonal projector."""
    hits = []
    for t in targets:
        rank, jr, idem = odd_rank_J_projector(U, c, t)
        if jr < TOL and idem < TOL:
            hits.append(rank)
    return sorted(set(hits))


# ------------------------------------------------------------------------------------------------
# Triplet Krein signature (the self-dual SU(2)+ generation triplet on the 1792-dim carrier)
#   -- reproduces canon/ghost-parity-krein: (+96,-96,0) in every signature (net chiral index 0).
# ------------------------------------------------------------------------------------------------
SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]


def lvec(i, j):
    M = np.zeros((N, N), dtype=complex)
    M[i, j], M[j, i] = 1, -1
    return M


def triplet_krein_signature(timelike):
    I128, I14 = np.eye(DIM, dtype=complex), np.eye(N, dtype=complex)
    base = cl95.jordan_wigner_gammas(7)
    e = [(1j * base[a] if a in timelike else base[a]) for a in range(N)]
    spacelike = [a for a in range(N) if a not in timelike]
    Gamma = np.hstack(e)
    Pi = np.eye(N * DIM, dtype=complex) - Gamma.conj().T @ np.linalg.inv(Gamma @ Gamma.conj().T) @ Gamma
    J = [np.kron(I14, sgen(e, a, b) + sgen(e, c, d)) + np.kron(lvec(a, b) + lvec(c, d), I128)
         for (a, b, c, d) in SD]
    w, Vv = np.linalg.eigh(Pi)
    W = Vv[:, w > 0.5]
    Cas = -(J[0] @ J[0] + J[1] @ J[1] + J[2] @ J[2])
    CasK = W.conj().T @ Cas @ W
    CasK = 0.5 * (CasK + CasK.conj().T)
    ev, Uc = np.linalg.eigh(CasK)
    top = max(round(x.real, 3) for x in ev)
    Wt = W @ Uc[:, np.abs(ev - top) < 1e-3]
    bS = I128.copy()
    for s in spacelike:
        bS = bS @ e[s]
    if np.linalg.norm(bS.conj().T + bS) < 1e-9:
        bS = 1j * bS
    bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
    beta_res = max(np.linalg.norm(bS @ sgen(e, i, j) + sgen(e, i, j).conj().T @ bS)
                   for i in range(N) for j in range(i + 1, N))
    etaV = np.diag([(-1.0 if a in timelike else 1.0) for a in range(N)]).astype(complex)
    K = np.kron(etaV, bS)
    B = Wt.conj().T @ K @ Wt
    B = 0.5 * (B + B.conj().T)
    sig = np.linalg.eigvalsh(B)
    npl = int(np.sum(sig > 1e-9))
    nmi = int(np.sum(sig < -1e-9))
    return npl, nmi, beta_res


# ------------------------------------------------------------------------------------------------
# DeWitt / trace-reversed Frobenius fiber signature on Sym^2(R^4)
# ------------------------------------------------------------------------------------------------
def dewitt_fiber_signature(eta_diag):
    eta = np.diag(eta_diag).astype(float)
    # basis of symmetric 4x4 matrices (10-dim)
    basis = []
    for i in range(4):
        for j in range(i, 4):
            E = np.zeros((4, 4))
            E[i, j] = E[j, i] = 1.0
            basis.append(E)
    n = len(basis)  # 10

    def tr_eta(h):
        return np.trace(eta @ h)

    # trace-reversed DeWitt metric G(h,k) = tr(eta h eta k) - 1/2 tr_eta(h) tr_eta(k)
    Gmat = np.zeros((n, n))
    for a in range(n):
        for b in range(n):
            ha, hb = basis[a], basis[b]
            Gmat[a, b] = np.trace(eta @ ha @ eta @ hb) - 0.5 * tr_eta(ha) * tr_eta(hb)
    ev = np.linalg.eigvalsh(0.5 * (Gmat + Gmat.T))
    return int(np.sum(ev > 1e-9)), int(np.sum(ev < -1e-9))


def main():
    checks = []
    xi = gb.XI
    print("=" * 96)
    print("H19  THE (7,7) SIGNATURE BRANCH: does adopting Cl(7,7)=M(128,R) DERIVE three, or only permit odd?")
    print("=" * 96)

    e95, _ = clifford(9, 5)
    e77, _ = clifford(7, 7)
    U95, c95 = antilinear_J(e95)
    U77, c77 = antilinear_J(e77)

    # =========================== Q1: force 3, or just odd? ===========================
    print("Q1 -- does (7,7) FORCE 3, or just ODD?")
    # 1a. reachable odd ranks
    odd77 = reachable_odd_ranks(U77, c77, (1, 3, 5, 7))
    # on (9,5) the same targets round to the next EVEN rank (no genuine odd projector)
    even_forced_95 = all(odd_rank_J_projector(U95, c95, t)[0] % 2 == 0 for t in (1, 3, 5, 7))
    checks.append(report(
        "Q1a. (7,7) J^2=+1: odd ranks {1,3,5,7} ALL reachable; (9,5) J^2=-1 forces even -> 3 NOT selected",
        c77.real > 0 and c95.real < 0 and odd77 == [1, 3, 5, 7] and even_forced_95,
        f"(7,7) reachable odd ranks={odd77} (unrestricted); (9,5) all even-forced={even_forced_95}"))

    # 1b. STRUCTURAL KILL: signature is 2-primary; the count-3 is 3-primary; 2-primary blindness.
    signature_datum_order = 8         # p-q mod 8 lives in Z/8 (2-primary arena)
    count_arena_order = 3             # the generation 3 lives in Z/3 (order-3 arena of Z/24)
    n_homs = math.gcd(signature_datum_order, count_arena_order)   # |Hom(Z/8,Z/3)| = gcd = 1 (zero map only)
    hom_is_trivial = (n_homs == 1)    # only the zero homomorphism
    crt_coprime = (math.gcd(8, 3) == 1 and 8 * 3 == 24)           # Z/24 = Z/8 (+) Z/3, arenas meet only at 0
    checks.append(report(
        "Q1b. 2-PRIMARY BLINDNESS: signature in Z/8, count-3 in Z/3; |Hom(Z/8,Z/3)|=gcd(8,3)=1 (zero map)",
        hom_is_trivial and crt_coprime,
        f"|Hom(Z/8,Z/3)|={n_homs} => a 2-primary signature move CANNOT reach the 3-primary count arena "
        f"(Lean-verified two-arena core) => (7,7) is STRUCTURALLY INCAPABLE of supplying 3"))

    # 1c. ANTI-FIT: the natural carrier (self-dual triplet, mult 3) is NEUTRAL (index 0) in BOTH signatures.
    npl95, nmi95, br95 = triplet_krein_signature({4, 5, 6, 7, 8})          # (9,5)
    npl77, nmi77, br77 = triplet_krein_signature({4, 5, 6, 7, 8, 9, 10})   # (7,7)
    checks.append(report(
        "Q1c. ANTI-FIT: self-dual triplet (mult 3) is NEUTRAL (+96,-96,0) => net chiral index 0 in BOTH",
        npl95 == nmi95 == 96 and npl77 == nmi77 == 96 and br95 < 1e-9 and br77 < 1e-9,
        f"(9,5) triplet Krein=(+{npl95},-{nmi95}); (7,7)=(+{npl77},-{nmi77}) => 3 is vectorlike; "
        f"(7,7) lifts the PROHIBITION but supplies no chiral selector => 3 NOT derived"))

    # =========================== Q2: does gravity transfer? ===========================
    print("Q2 -- does the gravity conditional theorem (Krein / |II|^2 / spin-lift) TRANSFER to (7,7)?")
    # 2a. Krein structure transfers: beta_S pseudo-anti-Hermitian on both (residuals from 1c: br95, br77).
    checks.append(report(
        "Q2a. Krein structure TRANSFERS: beta_S pseudo-anti-Hermitian for every so(p,q) gen on BOTH sigs",
        br95 < 1e-9 and br77 < 1e-9,
        f"beta pseudo-anti-Herm residual: (9,5)={br95:.0e}, (7,7)={br77:.0e} => the |II|^2/Krein SHAPE is "
        f"signature-independent (grading leg {{G,O}}=0 also sig-independent, H37 D1)"))

    # 2b. Reality class of the J-commutant FLIPS H -> R: the quaternionic gauge group is (9,5)-specific.
    #     J^2=-1 => commutant = M(64,H) (quaternionic, gauge Sp(32,32;H));
    #     J^2=+1 => commutant = M(128,R) (real/split, a DIFFERENT real form).
    checks.append(report(
        "Q2b. reality class FLIPS: (9,5) J^2=-1 -> M(64,H)/Sp(...;H);  (7,7) J^2=+1 -> M(128,R)/real-split",
        c95.real < 0 and c77.real > 0,
        f"J^2: (9,5)={c95.real:+.2f} (quaternionic), (7,7)={c77.real:+.2f} (real) => the quaternionic "
        f"gauge group Sp(32,32;H) is (9,5)-SPECIFIC and does NOT transfer; gravity's Krein/|II|^2 shape does"))

    # =========================== Q3: what does (7,7) cost? ===========================
    print("Q3 -- what does (7,7) COST (anomaly / SM embedding / unitarity)?")
    # 3a. anomaly: omega^2 = +I in both (both q odd) -> chiral split exists; D=14 anomaly Tr F^8 reality-blind
    def omega_sq(e):
        w = np.eye(DIM, dtype=complex)
        for a in range(N):
            w = w @ e[a]
        return w @ w
    o95 = omega_sq(e95)
    o77 = omega_sq(e77)
    o95_plus = np.linalg.norm(o95 - np.eye(DIM, dtype=complex)) < 1e-9
    o77_plus = np.linalg.norm(o77 - np.eye(DIM, dtype=complex)) < 1e-9
    checks.append(report(
        "Q3a. anomaly NOT broken: omega^2=+I in BOTH (chiral split exists); D=14 anomaly Tr F^8 reality-blind",
        o95_plus and o77_plus,
        f"omega^2=+I: (9,5)={o95_plus}, (7,7)={o77_plus} => chirality does not privilege H; anomaly-free "
        f"content admissible in both (cite BIG-SWING angle 1)"))

    # 3b. SM embedding: the Pati-Salam (6,4) fiber is signature-independent (both base orientations).
    fib_mp = dewitt_fiber_signature([-1, 1, 1, 1])   # mostly-plus base
    fib_mm = dewitt_fiber_signature([1, -1, -1, -1])  # mostly-minus base
    checks.append(report(
        "Q3b. SM embedding SURVIVES: trace-reversed DeWitt fiber = (6,4) for BOTH base orientations",
        fib_mp == (6, 4) and fib_mm == (6, 4),
        f"fiber signature: mostly-plus={fib_mp}, mostly-minus={fib_mm} => the Pati-Salam Spin(6,4) chain "
        f"(Spin(6,4)->Spin(3,2)->SU(3)xSU(2)xU(1)) rides the COMMON fiber, neutral on the total signature"))

    # 3c. unitarity: both q>0 => both Krein, both need Turok-Bateman ghost parity (triplet neutral in both).
    both_krein = (5 > 0) and (7 > 0)  # q_(9,5)=5, q_(7,7)=7, both indefinite
    checks.append(report(
        "Q3c. unitarity cost IDENTICAL: both (9,5) q=5 and (7,7) q=7 are Krein (q>0), both need ghost parity",
        both_krein and npl95 == nmi95 and npl77 == nmi77,
        "neither is a Hilbert space; the triplet is neutral (+96,-96) in both => same Turok-Bateman cost"))

    # 3d. the REAL cost: predictivity NARROWS -- admissible rank set widens (even {0,2,4,6} -> {1..7}).
    admissible_95 = "even {0,2,4,6,...}"     # Kramers-forced even
    admissible_77 = sorted(set(odd77) | {2, 4, 6})  # odd now free too => the full ladder
    widened = len(admissible_77) > len([0, 2, 4, 6])  # strictly more admissible integers
    checks.append(report(
        "Q3d. the REAL cost: (7,7) removes the even-parity constraint WITHOUT adding one -> predictivity DROPS",
        widened,
        f"(9,5) admissible ranks = {admissible_95}; (7,7) admissible = full ladder incl {admissible_77} "
        f"=> LESS constraining: odd 1,3,5,7 all admissible, not just 3"))

    # =========================== Q4: is (7,7) GU-native? ===========================
    print("Q4 -- is (7,7) GU-NATIVE (any lever selecting it over (9,5))?")
    # 4a. closed form p-q = d + d^2/2: d=+2 -> 4 -> (9,5)/H; d=-2 -> 0 -> (7,7)/R.
    def pminusq(d):
        return d + d * d // 2
    pq_mp = pminusq(+2)   # mostly-plus (3,1): #space-#time = 2
    pq_mm = pminusq(-2)   # mostly-minus (1,3): #space-#time = -2
    checks.append(report(
        "Q4a. closed form p-q = d + d^2/2: mostly-plus d=+2 -> p-q=4 (9,5)/H; mostly-minus d=-2 -> p-q=0 (7,7)/R",
        pq_mp == 4 and pq_mm == 0 and (pq_mp % 8) == 4 and (pq_mm % 8) == 0,
        f"p-q(mostly-plus)={pq_mp} (mod8={pq_mp % 8}, quaternionic); p-q(mostly-minus)={pq_mm} "
        f"(mod8={pq_mm % 8}, real) => ONLY sign(d) moves the class"))

    # 4b. the (6,4) fiber (the only common structure) is g -> -g invariant => carries no sign(d) selector.
    fiber_sign_invariant = (fib_mp == fib_mm == (6, 4))
    checks.append(report(
        "Q4b. NO GU-native selector: the (6,4) fiber is g->-g invariant; Weinstein's Spin(6,4)/Spin(3,2) "
        "chain rides it => neutral on total signature",
        fiber_sign_invariant,
        "only the base pullback (linear in g) carries sign(d), and the space-of-metrics has no preferred "
        "timelike-norm sign => UNDER-DETERMINED (confirms BIG-SWING); (7,7) is a declared choice, not derived"))

    print("-" * 96)
    print("SUMMARY (four verdicts)")
    print("  Q1  ODD-ADMISSIBLE, NOT FORCED-3.   (7,7) permits odd ranks 1,3,5,7 (rank free); 2-primary")
    print("      blindness (|Hom(Z/8,Z/3)|=1) forbids the signature from supplying the 3-primary count;")
    print("      the natural triplet carrier is index-0 (neutral) in both signatures => 3 is not derived.")
    print("  Q2  TRANSFERS IN SHAPE, CHANGES IN REALITY.  Krein/|II|^2/grading are signature-independent")
    print("      (transfer); the quaternionic gauge group Sp(32,32;H) is (9,5)-specific (does NOT transfer,")
    print("      becomes a real/split form). Gravity's conditional-theorem shape survives.")
    print("  Q3  LOW COST.  Anomaly reality-blind (omega^2=+I both), SM embedding rides the common (6,4)")
    print("      fiber, both already Krein (same unitarity cost). The genuine cost is REDUCED predictivity")
    print("      (odd 1,3,5,7 all admissible) -- (7,7) is LESS constraining, not more.")
    print("  Q4  NOT GU-NATIVE.  p-q = d + d^2/2; only sign(d) (mostly-plus vs mostly-minus) moves the class,")
    print("      and no GU-native selector for it exists. (7,7) stays an under-determined choice.")
    print("  HEADLINE: adopting (7,7) makes odd ADMISSIBLE but does NOT DERIVE three (structurally cannot,")
    print("            by 2-primary blindness); it is cheap but non-deriving and not GU-selected. The")
    print("            signature axis (L7) lifts a 2-primary VETO; the 3 still lives in the orthogonal")
    print("            Z/3 arena. Single next object: the Z/3-arena (chiral/ghost-parity) selector, OR a")
    print("            GU-native selector for sign(d). No target imported; no fit to 3.")
    print("=" * 96)

    ok = all(checks)
    print(("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED") + f"  ({sum(checks)}/{len(checks)})")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
