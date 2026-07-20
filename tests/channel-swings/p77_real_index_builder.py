#!/usr/bin/env python3
"""P-77-REAL-INDEX (W1 builder): the (7,7) real-index generation arithmetic.

Companion to explorations/p77-real-index-W1-builder-2026-07-19.md, whose
Sections 1-2 (pre-registered interpretations FORCED-3 / FREE-INTEGER /
REAL-CLASS-BLOCKS-3, and the convention-DOF enumeration D1-D9) were
committed BEFORE this script was written or run.

Signature purity (K6): every computation below is performed IN (7,7)
(timelike T = {4..10}, the repo convention, matching
tests/channel-swings/ch_sig77_port_probe.py). All (9,5) facts are CITED
from receipts (canon C-01..C-07; tests/generation-sector/step5, step6,
step10/11; DERIVATION-PROGRESS generation-count-rank3-resolution), never
recomputed here.

PART 0  Exact-arithmetic class certificate (bit-exact where the matrices
        are integer/i-integer): Cl(7,7) relations; J' = (prod of 8 gammas)
        . conj commutes with every generator and J'^2 = +1; the real form
        R^128 inside C^128 has real dimension 128 (the (7,7) module is the
        HALF-size real module: 128 real dims vs the cited (9,5) H^64 = 256
        real dims); class invariance under a relabeled timelike set (D2).

PART A  Convention rigidity (D3-D5): Gram fork facts exact (bS J'-odd, bT
        J'-even, both Grams' overall signs immaterial); the J'-phase family
        all squares to +1 (D5); Weyl typing: omega^2 = +1, J' preserves
        both 64-dim Weyl halves and restricts to a real structure on EACH
        (Cl0(7,7) is R(+)R type: both halves real, rank_R 64).

PART B  The bulk divisor (ABS/KO arithmetic, p-q = 0 mod 8 = KO side):
        (B2) fiber Cl(6,4) module theory with explicit 32-dim gammas: the
        commuting conjugation solved by subset search, J_f^2 = +1 (real
        Dirac class), omega_int^2 = -1 so the antiunitary EXCHANGES the two
        Weyl 16s: no real form on a single 16; the minimal real block is
        16(+)16bar = 32 real dimensions. Per-generation unit REBUILT:
          (9,5) cited: 16 Weyl = C^16 = H^8   -> divisor 8 H-lines
          (7,7) computed: 16 Weyl pairs with 16bar -> divisor 32 R-lines
        SAME 32 real dimensions per generation in both classes: the unit
        conversion (24/8 = 48/16 = 96/32 = 3) is bookkeeping, not forcing.
        (B3) What WAS forcing in (9,5) -- H-linearity => even complex index
        (Kramers factor 2) -- DIES: a J'-real (commuting) Hermitian carrier
        on the (7,7) constraint surface reaches signature 1 (rank-1, odd)
        and an odd-dimensional kernel (dim ker = 1); reachable-signature
        divisor = 1. KO^0(pt) = Z: plain integer, no forced divisibility;
        the newly available Z/2 (kernel parity mod 2, KO^{-1}/KO^{-2}
        shadow) is exhibited. So the naive expectation "divisor 8 was
        quaternionic rank" is REFINED, not confirmed as stated: the forced
        part of the (9,5) arithmetic was only the factor 2; the /8 was unit
        conversion and survives as /32-real.

PART C  THE CENTER OF GRAVITY -- boundary/eta in (7,7). Build the (7,7)
        D_Sigma = E + E^dag on the RS constraint surface (E = Q M_D Pi):
        (C1) the chiral grading G = Pi - Q anticommutes with D_Sigma, so
        the BARE eta is 0 EXACTLY -- this half of the (9,5) C-01 mechanism
        is signature-blind and PORTS. (C2) What does NOT port is the
        symmetry class: in (7,7), T' = J'_RS has T'^2 = +1 and
        C' = J'_RS . G has C'^2 = +1: Altland-Zirnbauer class BDI (cited
        contrast: (9,5) is CII with T^2 = C^2 = -1, step6). (C3) Grading-
        breaking flow, mirroring step6 with J'-real admissible breakers:
        eta(D + t*Delta) is revived; WITHOUT Kramers the flow quantum is 2
        (simple crossings), not 4 (Kramers pairs) -- values eta = 2 mod 4,
        impossible in (9,5), are looked for; and the value is BREAKER-
        DEPENDENT (connection-dependent, the C-03 reading), hence NOT
        forced. If forced-3 exists it would have to come from here; the
        computation shows the boundary supplies REACHABILITY of odd counts
        (via half-quantum + odd kernels), not the value 3.

PART D  Ghost/compensator sector: the canonical Krein Gram K = eta_V (x) bS
        ANTICOMMUTES with J'_RS (exact), while the entire GU-native
        apparatus (e_a, sigma_ab, Pi, M_D, G) is J'-REAL: the grading is
        J'-odd, the machinery J'-even. Consequences computed: (D2) a
        J'-real, K-commuting Hermitian carrier has EQUAL signature on the
        two ghost-parity sectors (J' exchanges them), so its TOTAL
        signature is even -- a factor-2 that returns, but only for the
        total-space reading under the canonical Gram; (D3) the PER-SECTOR
        (physical) count parity is FREE under BOTH Grams (odd per-sector
        carriers constructed under bS and, J'-real, under bT). The parity
        freedom of the physical sector is Gram-robust; the total-even fact
        is Gram-DEPENDENT and therefore (by the pre-registered rigidity
        rule) cannot serve as a REAL-CLASS-BLOCKS-3 wall.

No claim-status, canon, scorecard, map, or public-posture movement.
Exit 0 iff all checks pass.

Run: python tests/channel-swings/p77_real_index_builder.py
"""

import numpy as np

TOL = 1e-9
CHECKS = []
REPORT = {}


def check(name, cond, detail=""):
    CHECKS.append((name, bool(cond)))
    tag = "PASS" if cond else "FAIL"
    print(f"[{tag}] {name}" + (f"  --  {detail}" if detail else ""), flush=True)


def maxabs(A):
    return float(np.abs(A).max())


# ===========================================================================
# shared construction ((7,7) repo convention, identical to the port probe)
# ===========================================================================

N, DIM = 14, 128
TIMELIKE_77 = {4, 5, 6, 7, 8, 9, 10}
JPRIME_FACTORS = [1, 3, 4, 6, 8, 10, 11, 13]


def jw_gammas(n):
    I2 = np.eye(2, dtype=complex)
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    G = []
    for k in range(n):
        L, R = [s3] * k, [I2] * (n - 1 - k)
        for mid in (s1, s2):
            o = np.array([[1 + 0j]])
            for m in L + [mid] + R:
                o = np.kron(o, m)
            G.append(o)
    return G


base = jw_gammas(7)
e = [(1j * base[a] if a in TIMELIKE_77 else base[a]) for a in range(N)]
eta = np.array([(-1.0 if a in TIMELIKE_77 else 1.0) for a in range(N)])
spacelike = [a for a in range(N) if a not in TIMELIKE_77]
timelike = sorted(TIMELIKE_77)

Cp = np.eye(DIM, dtype=complex)
for a in JPRIME_FACTORS:
    Cp = Cp @ e[a]
Cp_inv = np.conj(Cp)          # from Cp conj(Cp) = I (checked in 0b)


def jconj(A, Cm=None, Cm_inv=None):
    """Antiunitary conjugation J A J^{-1} for J = Cm . conj."""
    Cm = Cp if Cm is None else Cm
    Cm_inv = Cp_inv if Cm_inv is None else Cm_inv
    return Cm @ np.conj(A) @ Cm_inv


def sgen(i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


def hsig(A, return_counts=False):
    ev = np.linalg.eigvalsh(0.5 * (A + A.conj().T))
    tol = 1e-7 * (np.abs(ev).max() + 1e-30)
    npos = int((ev > tol).sum())
    nneg = int((ev < -tol).sum())
    nzero = int((np.abs(ev) <= tol).sum())
    if return_counts:
        return npos - nneg, npos, nneg, nzero
    return npos - nneg


# ===========================================================================
# PART 0 -- exact class certificate + bookkeeping + D2 spot check
# ===========================================================================

def part0():
    print("=" * 78)
    print("PART 0 -- exact Cl(7,7) class certificate and real-dimension bookkeeping")
    print("=" * 78)

    r = max(maxabs(e[a] @ e[b] + e[b] @ e[a] - (2 * eta[a] if a == b else 0) * np.eye(DIM))
            for a in range(N) for b in range(N))
    check("0a  Cl(7,7) relations {e_a,e_b} = 2 eta_ab BIT-EXACT (max entry residual 0)",
          r == 0.0, f"max residual {r:.1e}")

    gen_defect = max(maxabs(e[a] @ Cp - Cp @ np.conj(e[a])) for a in range(N))
    j2 = maxabs(Cp @ np.conj(Cp) - np.eye(DIM))
    check("0b  J' commutes with all 14 generators BIT-EXACT and J'^2 = +1 exact "
          "(real class M(128,R))", gen_defect == 0.0 and j2 == 0.0,
          f"gen defect {gen_defect:.1e}, J'^2-I {j2:.1e}")

    # real form dimension: J' v = Cp conj(v); as a real-linear map on R^256 it is
    # M = [[A, B], [B, -A]] with Cp = A + iB; M^2 = I; dim fix = 128 + tr(A).
    A_, B_ = np.real(Cp), np.imag(Cp)
    Mreal = np.block([[A_, B_], [B_, -A_]])
    m2 = maxabs(Mreal @ Mreal - np.eye(2 * DIM))
    dim_fix = 0.5 * (2 * DIM + np.trace(Mreal))
    check("0c  BOOKKEEPING: the (7,7) irreducible real module is R^128 -- the J'-fixed "
          "real form inside C^128 has real dimension 128 (cited contrast, not "
          "recomputed: Cl(9,5) module is H^64 = 256 real dims; same complex 128, "
          "HALF the real content)",
          m2 < 1e-12 and abs(dim_fix - 128) < 1e-9,
          f"M^2-I {m2:.1e}, dim_R(fixed) = {dim_fix:.1f}")
    REPORT["real_dims"] = {"(7,7)": 128, "(9,5) cited": 256}

    # D2 spot check: relabeled timelike set {0..6} -- averaging construction, J^2 sign.
    e_alt = [(1j * base[a] if a < 7 else base[a]) for a in range(N)]
    eta_alt = np.array([(-1.0 if a < 7 else 1.0) for a in range(N)])

    def Phi(U):
        out = np.zeros_like(U)
        for a in range(N):
            out += eta_alt[a] * (e_alt[a] @ U @ e_alt[a].conj())
        return out / N

    rng = np.random.default_rng(1)
    U = rng.standard_normal((DIM, DIM)) + 1j * rng.standard_normal((DIM, DIM))
    for _ in range(300):
        U = 0.5 * (U + Phi(U))
        U /= np.linalg.norm(U)
    Us, _, Vs = np.linalg.svd(U)
    U = Us @ Vs
    lam = (np.trace(U @ U.conj()) / DIM).real
    check("0d  D2 rigidity: relabeled timelike set {0..6} gives the SAME class "
          "(commuting antiunitary with J^2 = +1)", lam > 0.5, f"J^2 = {lam:+.3f}")


# ===========================================================================
# PART A -- convention rigidity: Gram fork, phase family, Weyl typing
# ===========================================================================

def partA():
    print()
    print("=" * 78)
    print("PART A -- convention DOFs D3/D4/D5 and the Weyl real structure")
    print("=" * 78)

    P7s = np.eye(DIM, dtype=complex)
    for a in spacelike:
        P7s = P7s @ e[a]
    bS = 1j * P7s
    bT = np.eye(DIM, dtype=complex)
    for a in timelike:
        bT = bT @ e[a]

    hS = maxabs(bS - bS.conj().T)
    sS = maxabs(bS @ bS - np.eye(DIM))
    aS = maxabs(jconj(bS) + bS)
    hT = maxabs(bT - bT.conj().T)
    sT = maxabs(bT @ bT - np.eye(DIM))
    cT = maxabs(jconj(bT) - bT)
    check("A1  Gram fork facts EXACT: bS Hermitian, bS^2 = I, J'-ODD (anticommutes); "
          "bT Hermitian, bT^2 = I, J'-EVEN (commutes). Overall signs +-bS/+-bT only "
          "relabel the sectors (D4)",
          hS == 0.0 and sS == 0.0 and aS == 0.0 and hT == 0.0 and sT == 0.0 and cT == 0.0,
          f"residuals bS ({hS:.0e},{sS:.0e},{aS:.0e}) bT ({hT:.0e},{sT:.0e},{cT:.0e})")

    ph_ok = True
    for th in (0.7, 2.1):
        Cth = np.exp(1j * th) * Cp
        ph_ok = ph_ok and maxabs(Cth @ np.conj(Cth) - np.eye(DIM)) < 1e-12
    check("A2  D5 rigidity: the J'-phase family (e^{i theta} U).conj all square to +1 "
          "-- the real class does not depend on the phase convention", ph_ok)

    omega = np.eye(DIM, dtype=complex)
    for a in range(N):
        omega = omega @ e[a]
    om2 = maxabs(omega @ omega - np.eye(DIM))
    om_h = maxabs(omega - omega.conj().T)
    om_j = maxabs(jconj(omega) - omega)
    Pp = 0.5 * (np.eye(DIM) + omega)
    pres = maxabs(jconj(Pp) - Pp)
    # restrict J' to a Weyl half and verify it is a real structure there (C_half conj(C_half)=I)
    wv, Wv = np.linalg.eigh(0.5 * (omega + omega.conj().T))
    Whalf = Wv[:, wv > 0.5]                      # 64-dim +1 Weyl half
    C_half = Whalf.conj().T @ Cp @ np.conj(Whalf)
    half_real = maxabs(C_half @ np.conj(C_half) - np.eye(Whalf.shape[1]))
    check("A3  Weyl typing: omega^2 = +1, omega Hermitian, J' preserves both Weyl "
          "halves and RESTRICTS to a real structure on each (J'|half squared = +1): "
          "both 64-dim halves are REAL, rank_R 64 each (Cl0(7,7) of R(+)R type)",
          om2 == 0.0 and om_h == 0.0 and om_j == 0.0 and pres == 0.0 and half_real < 1e-10,
          f"omega^2-I {om2:.0e}, [omega,J'] {om_j:.0e}, half-real residual {half_real:.1e}")
    return bS, bT


# ===========================================================================
# PART B -- the bulk divisor: fiber module theory + no forced divisibility
# ===========================================================================

def partB(Pi, CpRS):
    print()
    print("=" * 78)
    print("PART B -- bulk divisor: Cl(6,4) fiber unit + KO-side forced divisibility")
    print("=" * 78)

    # ---- B2: fiber Cl(6,4), explicit 32-dim gammas ----------------------------------
    nf, DF = 10, 32
    fbase = jw_gammas(5)
    f_timelike = {6, 7, 8, 9}                      # fiber (6,4): 6 space + 4 time
    ef = [(1j * fbase[a] if a in f_timelike else fbase[a]) for a in range(nf)]
    ef_eta = np.array([(-1.0 if a in f_timelike else 1.0) for a in range(nf)])
    rf = max(maxabs(ef[a] @ ef[b] + ef[b] @ ef[a] - (2 * ef_eta[a] if a == b else 0) * np.eye(DF))
             for a in range(nf) for b in range(nf))
    check("B2a fiber Cl(6,4) relations exact (32-dim explicit gammas)", rf == 0.0,
          f"max residual {rf:.1e}")

    # subset search for the COMMUTING conjugation Jf = P.conj (try P and iP)
    found = None
    for mask in range(1 << nf):
        P = np.eye(DF, dtype=complex)
        for a in range(nf):
            if mask >> a & 1:
                P = P @ ef[a]
        for scal, name in ((1.0, ""), (1j, "i*")):
            Pc = scal * P
            if all(maxabs(Pc @ np.conj(ef[a]) - ef[a] @ Pc) == 0.0 for a in range(nf)):
                found = (mask, name, Pc)
                break
        if found:
            break
    check("B2b fiber commuting conjugation SOLVED by subset search (not postulated)",
          found is not None,
          f"P = {found[1]}prod(e_a, a in {sorted(a for a in range(nf) if found[0] >> a & 1)})"
          if found else "none")
    Pf = found[2]
    lam_f = (Pf @ np.conj(Pf))[0, 0].real
    diag_f = maxabs(Pf @ np.conj(Pf) - lam_f * np.eye(DF))
    check("B2c fiber Jf^2 = +1: the Cl(6,4) DIRAC module C^32 is REAL class "
          "(p - q = 2 mod 8)", diag_f == 0.0 and abs(lam_f - 1.0) < 1e-12,
          f"Jf^2 = {lam_f:+.1f}")

    om_f = np.eye(DF, dtype=complex)
    for a in range(nf):
        om_f = om_f @ ef[a]
    omf2 = (om_f @ om_f)[0, 0].real
    omf2_res = maxabs(om_f @ om_f - omf2 * np.eye(DF))
    # omega^2 = -1: Weyl halves are the +-i eigenspaces; Jf must EXCHANGE them
    Wp = 0.5 * (np.eye(DF) - 1j * om_f)           # +i eigenprojector
    Wm = 0.5 * (np.eye(DF) + 1j * om_f)
    exch = maxabs(Pf @ np.conj(Wp) @ np.conj(Pf) - Wm)
    check("B2d fiber omega_int^2 = -1 and Jf EXCHANGES the Weyl 16s: NO real form on "
          "a single Weyl 16; the minimal real block is 16(+)16bar = 32 REAL dims. "
          "PER-GENERATION UNIT (7,7) = 32 R-lines  [(9,5) cited: C^16 = H^8 = 8 "
          "H-lines = the SAME 32 real dims]",
          omf2_res == 0.0 and abs(omf2 + 1.0) < 1e-12 and exch == 0.0,
          f"omega_int^2 = {omf2:+.1f}, exchange residual {exch:.1e}")
    REPORT["unit"] = {"(9,5) cited": "8 H-lines (= 32 R)", "(7,7)": "32 R-lines"}

    # ---- B3: forced divisibility on the (7,7) side: NONE ------------------------------
    w, V = np.linalg.eigh(Pi)
    W = V[:, w > 0.5]

    def jfix(v):
        u = v + CpRS @ np.conj(v)
        if np.linalg.norm(u) < 1e-8:
            u = 1j * (v - CpRS @ np.conj(v))
        return u / np.linalg.norm(u)

    v1 = jfix(W[:, 0])
    P1 = np.outer(v1, np.conj(v1))
    jdef = maxabs(jconj(P1, np.kron(np.eye(N), Cp), np.kron(np.eye(N), Cp_inv)) - P1)
    inker = maxabs(Pi @ P1 - P1)
    s1 = hsig(P1)
    check("B3a NO forced divisibility: a rank-1 J'-real Hermitian carrier ON the "
          "constraint surface has signature 1 (ODD; reachable-signature divisor = 1). "
          "[(9,5) cited: H-linearity forces EVEN signature, canon C-07]",
          jdef < 1e-9 and inker < 1e-9 and s1 == 1,
          f"J'-defect {jdef:.1e}, kernel residual {inker:.1e}, signature {s1}")

    # odd kernel (the KO Z/2 shadow): 5 J'-fixed surface vectors, spectrum (0,1,1,-1,-1)
    vs = []
    idx = 0
    while len(vs) < 5 and idx < W.shape[1]:
        u = jfix(W[:, idx])
        for f in vs:
            u = u - (np.conj(f) @ u) * f
        nu = np.linalg.norm(u)
        if nu > 1e-8:
            vs.append(u / nu)
        idx += 1
    U5 = np.column_stack(vs)
    Ablk = U5 @ np.diag([0.0, 1.0, 1.0, -1.0, -1.0]).astype(complex) @ U5.conj().T
    jdefA = maxabs(jconj(Ablk, np.kron(np.eye(N), Cp), np.kron(np.eye(N), Cp_inv)) - Ablk)
    evA = np.linalg.eigvalsh(Ablk)
    n_unit = int((np.abs(np.abs(evA) - 1.0) < 1e-9).sum())
    # kernel ON the 5-dim block: 1 zero mode among the 5 block eigenvalues
    check("B3b ODD KERNEL allowed: a J'-real Hermitian block with dim ker = 1 on its "
          "5-dim carrier space (the KO Z/2 kernel-parity invariant is LIVE in the "
          "real class). [(9,5) cited: Kramers forces even-dimensional kernels]",
          jdefA < 1e-9 and n_unit == 4,
          f"J'-defect {jdefA:.1e}, block spectrum has 4 unit modes + 1 zero mode")

    print()
    print("  --- B4 the rebuilt packaging (bookkeeping table) ---")
    print("  (9,5) CITED : ind_H = 24 = 16 + 8; ind_C = 48; ind_R = 96;")
    print("                unit = 8 H-lines/gen; count = 24/8 = 48/16 = 96/32 = 3;")
    print("                FORCED part: ind_C even (Kramers factor 2); the /8 is unit")
    print("                conversion, physical-count grade on the RS leg (GEN-01).")
    print("  (7,7)       : KO^0(pt) = Z; forced divisibility: NONE (B3a);")
    print("                unit = 32 R-lines/gen (B2d, = the same 32 real dims);")
    print("                count = ind_R/32 with ind_R a FREE plain integer:")
    print("                3 is reachable (ind_R = 96) and NOT forced; the (9,5)")
    print("                Candidate A/B rank ambiguity (D9) ports verbatim, and no")
    print("                (7,7) computation supplies the value of ind_R.")


# ===========================================================================
# PART C -- the center of gravity: boundary/eta in (7,7)
# ===========================================================================

XI = np.array([1, 2, 3, 4, 0.5, 1.5, 2.5, 0.7, 1.1, 0.3, 2.2, 1.7, 0.9, 1.3], dtype=complex)


def partC(Pi, Q, G, CpRS, CpRS_inv):
    print()
    print("=" * 78)
    print("PART C -- boundary/eta: bare eta = 0 ports; the CII protection does NOT")
    print("=" * 78)

    M_D = np.kron(np.eye(N), sum(XI[a] * e[a] for a in range(N)))
    E = Q @ M_D @ Pi
    D = E + E.conj().T

    anti = maxabs(G @ D + D @ G)
    ev = np.linalg.eigvalsh(D)
    tol = 1e-7 * np.abs(ev).max()
    npos, nneg = int((ev > tol).sum()), int((ev < -tol).sum())
    nzero = int((np.abs(ev) <= tol).sum())
    check("C1  BARE eta(D_Sigma) = 0 in (7,7), forced by the chiral grading "
          "G = Pi - Q ({G, D} = 0): THIS half of the (9,5) C-01 mechanism is "
          "signature-blind and PORTS. If the question is the bare operator, eta is "
          "computably zero here too -- said plainly",
          anti < 1e-9 and npos == nneg,
          f"{{G,D}} {anti:.1e}; #pos={npos} #neg={nneg} #zero={nzero}; eta={npos-nneg}")

    TD = maxabs(CpRS @ np.conj(D) @ CpRS_inv - D)
    Cu = CpRS @ np.conj(G)
    C2v = (np.trace(Cu @ np.conj(Cu)) / (N * DIM)).real
    CD = maxabs(Cu @ np.conj(D) @ np.linalg.inv(Cu) + D)
    check("C2  Altland-Zirnbauer class of the (7,7) D_Sigma: T' = J'_RS with "
          "T'^2 = +1, [T', D] = 0; S = G chiral; C' = J'_RS.G with C'^2 = +1, "
          "{C', D} = 0  =>  class BDI. [(9,5) cited: class CII, T^2 = C^2 = -1 -- "
          "the particle-hole symmetry WAS J_quat.G; that protection is GONE]",
          TD < 1e-8 and abs(C2v - 1.0) < 1e-9 and CD < 1e-8,
          f"[T',D] {TD:.1e}; C'^2 = {C2v:+.4f}; {{C',D}} {CD:.1e}")

    # ---- C3: grading-breaking flow with J'-real admissible breakers -------------------
    def gdiag(X):
        return Pi @ X @ Pi + Q @ X @ Q

    def herm(X):
        return 0.5 * (X + X.conj().T)

    def jreal(X):
        return 0.5 * (X + CpRS @ np.conj(X) @ CpRS_inv)

    Delta_nat = gdiag(herm(M_D))
    nrm = np.linalg.norm(Delta_nat)
    rng = np.random.default_rng(7)
    breakers = [("natural diag M_D", Delta_nat)]
    for k in range(3):
        R = rng.standard_normal((N * DIM, N * DIM)) + 1j * rng.standard_normal((N * DIM, N * DIM))
        Dl = herm(gdiag(jreal(R)))
        breakers.append((f"generic J'-real #{k + 1}", Dl / np.linalg.norm(Dl) * nrm))

    spin_gen = np.kron(np.eye(N), sgen(0, 1))
    ts = np.linspace(0.0, 2.0, 9)
    all_etas = {}
    print("\n  eta(D + t*Delta) over t in [0, 2] (9 points), J'-real admissible breakers:")
    for name, Dl in breakers:
        gbreak = float(np.linalg.norm(G @ Dl + Dl @ G))
        jlin = maxabs(CpRS @ np.conj(Dl) @ CpRS_inv - Dl)
        noneq = float(np.linalg.norm(spin_gen @ Dl - Dl @ spin_gen))
        etas, zeros = [], []
        for t in ts:
            s, npv, nnv, nz = hsig(D + t * Dl, return_counts=True)
            etas.append(s)
            zeros.append(nz)
        all_etas[name] = etas
        print(f"    [{name}] {{G,Delta}}={gbreak:.1f}(breaks)  J'-defect={jlin:.1e}(real)  "
              f"[spin,Delta]={noneq:.1f}(non-eqv)")
        print(f"      eta: {etas}   #zero: {zeros}")

    flat = [x for name in all_etas if name != "natural diag M_D" for x in all_etas[name]]
    generic_flows = any(x != 0 for x in flat)
    all_even = all(x % 2 == 0 for x in flat)
    natural_zero = all(x == 0 for x in all_etas["natural diag M_D"])
    half_quantum = any(x % 4 != 0 for x in flat)
    values = sorted(set(flat))
    check("C3a eta is REVIVED by generic J'-real grading-breakers (the (9,5) soft-wall "
          "GO ports); the natural M_D-diagonal breaker stays special",
          generic_flows, f"natural stays 0: {natural_zero}; generic values seen: {values}")
    check("C3b flow parity: all eta values even (dimension parity: eta = dim - 2k when "
          "ker is trivial) -- evenness of FULL-SPACE eta is arithmetic, not Kramers",
          all_even, f"values {values}")
    check("C3c THE HALVED QUANTUM: eta values NOT divisible by 4 occur -- impossible in "
          "(9,5), where Kramers doubling makes every crossing a pair (cited step6: "
          "flow in steps of 4, values +-4). In (7,7) crossings are simple: the "
          "boundary spectral-flow quantum is 2, and with the D6 half-index reading "
          "count = eta/2 this makes ODD counts (including 3) REACHABLE from the "
          "boundary -- reachable, not pinned",
          half_quantum, f"values mod 4: {sorted(set(x % 4 for x in flat))}")

    names = [n for n in all_etas if n != "natural diag M_D"]
    breaker_dep = any(all_etas[a][i] != all_etas[b][i]
                      for i in range(len(ts)) for a in names for b in names if a < b)
    check("C3d VALUE NOT FORCED: different admissible breakers give different eta at "
          "the same coupling -- the revived index is connection-dependent (the C-03 "
          "reading ports). The boundary supplies REACHABILITY of odd, not the value 3",
          breaker_dep)
    REPORT["eta_values"] = {k: v for k, v in all_etas.items()}
    return D


# ===========================================================================
# PART D -- ghost/compensator sector vs the real structure
# ===========================================================================

def partD(bS, bT, Pi, G, CpRS, CpRS_inv):
    print()
    print("=" * 78)
    print("PART D -- ghost sector: J'-odd grading, J'-even machinery, and the count")
    print("=" * 78)

    etaV = np.diag(eta).astype(complex)
    K = np.kron(etaV, bS)
    kh = maxabs(K - K.conj().T)
    k2 = maxabs(K @ K - np.eye(N * DIM))
    kanti = maxabs(CpRS @ np.conj(K) @ CpRS_inv + K)
    check("D1  canonical ghost/Krein Gram K = eta_V (x) bS: Hermitian, K^2 = I, and "
          "ANTICOMMUTES with J'_RS BIT-EXACT -- the grading is J'-ODD",
          kh == 0.0 and k2 == 0.0 and kanti == 0.0,
          f"herm {kh:.0e}, sq {k2:.0e}, {{K,J'}} {kanti:.0e}")

    # the GU-native machinery is J'-EVEN (J'-real): generators, spin, Pi, M_D, G
    M_D = np.kron(np.eye(N), sum(XI[a] * e[a] for a in range(N)))
    prims = [np.kron(np.eye(N), e[a]) for a in (0, 4, 13)] + \
            [np.kron(np.eye(N), sgen(0, 1)), np.kron(np.eye(N), sgen(4, 9)), Pi, M_D, G]
    prim_defect = max(maxabs(CpRS @ np.conj(P) @ CpRS_inv - P) for P in prims)
    check("D2  the GU-native apparatus (e_a, sigma_ab, Pi, M_D, G) is J'-REAL "
          "(commutes with J'_RS): machinery J'-even, canonical grading J'-odd -- the "
          "CH-SRC interaction, stated precisely",
          prim_defect < 1e-8, f"max apparatus J'-defect {prim_defect:.1e}")

    wK, VK = np.linalg.eigh(0.5 * (K + K.conj().T))
    Sp = VK[:, wK > 0.5]                     # + ghost-parity sector (896)
    Sm = VK[:, wK < -0.5]
    Pplus = 0.5 * (np.eye(N * DIM) + K)
    Pminus = np.eye(N * DIM) - Pplus
    rng = np.random.default_rng(3)
    v = Pplus @ (rng.standard_normal(N * DIM) + 1j * rng.standard_normal(N * DIM))
    v /= np.linalg.norm(v)
    A0 = np.outer(v, np.conj(v))                             # rank-1 in the + sector, sig 1
    A = A0 + CpRS @ np.conj(A0) @ CpRS_inv                   # J'-real symmetrization; K-commuting
    jdA = maxabs(CpRS @ np.conj(A) @ CpRS_inv - A)
    kcA = maxabs(K @ A - A @ K)
    sp = hsig(Pplus @ A @ Pplus)
    sm = hsig(Pminus @ A @ Pminus)
    check("D3  canonical Gram, J'-real + K-commuting carrier (rank-1 physical seed + "
          "its forced J'-image): J' EXCHANGES the sectors, so the per-sector "
          "signatures are EQUAL and NONZERO (1 and 1) and the TOTAL is even -- a "
          "factor 2 RETURNS, but only for the total-space reading",
          jdA < 1e-9 and kcA < 1e-9 and sp == sm == 1 and (sp + sm) % 2 == 0,
          f"J'-defect {jdA:.1e}, [K,A] {kcA:.1e}, sig(+) = {sp}, sig(-) = {sm}, total = {sp + sm}")

    # per-sector parity is FREE: rank-3 carrier inside the + sector (K-commuting)
    V3 = Sp[:, :3]
    A3 = V3 @ V3.conj().T
    s3p = hsig(Sp.conj().T @ A3 @ Sp)
    s3m = hsig(Sm.conj().T @ A3 @ Sm)
    check("D4  canonical Gram, PER-SECTOR parity FREE: a K-commuting rank-3 carrier "
          "supported in the + sector has per-sector signature 3 (odd). The physical "
          "(one-sector) count carries no parity wall",
          s3p == 3 and s3m == 0, f"sig(+) = {s3p}, sig(-) = {s3m}")

    # chirality-twisted Gram: K_T commutes with J'; sectors J'-invariant; a J'-REAL
    # odd carrier exists INSIDE a sector
    KT = np.kron(etaV, bT)
    ktcomm = maxabs(CpRS @ np.conj(KT) @ CpRS_inv - KT)
    wT, VT = np.linalg.eigh(0.5 * (KT + KT.conj().T))
    SpT = VT[:, wT > 0.5]
    vs = []
    idx = 0
    while len(vs) < 3 and idx < SpT.shape[1]:
        v = SpT[:, idx]
        u = v + CpRS @ np.conj(v)
        if np.linalg.norm(u) < 1e-8:
            u = 1j * (v - CpRS @ np.conj(v))
        for f in vs:
            u = u - (np.conj(f) @ u) * f
        nu = np.linalg.norm(u)
        if nu > 1e-8:
            vs.append(u / nu)
        idx += 1
    U3 = np.column_stack(vs)
    A3T = U3 @ U3.conj().T
    jd = maxabs(CpRS @ np.conj(A3T) @ CpRS_inv - A3T)
    insec = maxabs(KT @ A3T - A3T @ KT)
    s3T = hsig(A3T)
    check("D5  chirality-twisted Gram (GRAM-PIN-77 other branch): K_T is J'-EVEN, "
          "sectors J'-invariant, and a J'-REAL rank-3 carrier with ODD signature 3 "
          "lives INSIDE one sector: no parity wall under this Gram either. "
          "=> per-sector parity freedom is GRAM-ROBUST; the D3 total-even fact is "
          "Gram-DEPENDENT, hence (pre-registered rule) NOT a blocks-3 wall",
          ktcomm == 0.0 and jd < 1e-9 and insec < 1e-9 and s3T == 3,
          f"[K_T,J'] {ktcomm:.0e}; carrier J'-defect {jd:.1e}, in-sector {insec:.1e}, sig {s3T}")


def main():
    part0()
    bS, bT = partA()

    Gamma = np.hstack(e)
    gg = maxabs(Gamma @ Gamma.conj().T - N * np.eye(DIM))
    Pi = np.eye(N * DIM, dtype=complex) - Gamma.conj().T @ Gamma / N
    check("S   Gamma Gamma^dag = 14 I exact => Pi = I - Gamma^dag Gamma / 14 "
          "(constraint projector, closed form)", gg == 0.0, f"residual {gg:.1e}")
    Q = np.eye(N * DIM, dtype=complex) - Pi
    G = Pi - Q
    CpRS = np.kron(np.eye(N), Cp)
    CpRS_inv = np.kron(np.eye(N), Cp_inv)

    partB(Pi, CpRS)
    partC(Pi, Q, G, CpRS, CpRS_inv)
    partD(bS, bT, Pi, G, CpRS, CpRS_inv)

    n_fail = sum(1 for _, ok in CHECKS if not ok)
    print()
    print(f"{len(CHECKS) - n_fail}/{len(CHECKS)} checks passed.")
    print("SUMMARY: (7,7) real class certified exactly (R^128, half the real content "
          "of the cited (9,5) H^64); per-generation unit rebuilt = 32 R-lines (the "
          "SAME 32 real dims as (9,5)'s 8 H-lines) -- the /8 was unit conversion, "
          "only the Kramers factor 2 was forced and it DIES: rank-1 odd carriers, "
          "odd kernels, KO^0 = Z with no forced divisibility. Boundary/eta: bare "
          "eta = 0 PORTS (chiral grading, signature-blind); the symmetry class drops "
          "CII -> BDI, the flow quantum halves 4 -> 2 (values 2 mod 4 observed, "
          "impossible in (9,5)), and the revived value is breaker/connection-"
          "dependent: odd counts REACHABLE from the boundary, value 3 NOT pinned. "
          "Ghost sector: canonical grading J'-odd vs J'-even machinery; total-space "
          "even-ness returns for J'-real K-commuting carriers but is Gram-dependent; "
          "per-sector parity freedom is Gram-robust. Pre-registered ending: "
          "FREE-INTEGER. No claim-status movement.")
    if n_fail:
        raise SystemExit(f"{n_fail} check(s) FAILED")
    raise SystemExit(0)


if __name__ == "__main__":
    main()
