#!/usr/bin/env python3
"""CH-QM graded-quotient toy + the decisive J_quat probe (channel swing 2026-07-19).

Runs under the boundary-adapter standing axiom (adapter assumed as axiom
A_boundary; the received datum is the transmitted global Z/2 orientation).
Machine-checks:

PART A  p2c-style Z/2 register: the orientation is stored loop-coherently on a
        Z/2 gauge loop -- locally unreadable (every proper-subset marginal is
        identical across the two holonomy sectors), readable only by the full
        loop product. This is the Q4-support / local-inertness certificate and
        the structural (not procedural) non-retuning condition.

PART B  finite Krein graded quotient driven by the received bit:
        (a) RIGHT orientation: the Noether identity closes
            (delta_2 . d_{RS,-1} = 0), the quotient physical sector is
            positive-definite, dynamics is state-preserving, toy Born rule is
            positive and normalized                       [Q1 Q2 Q3 Q5 Q6]
        (b) WRONG orientation: the PRIMARY failure is cohomological --
            delta_2 . d_{RS,-1} != 0, the complex does not close, the quotient
            is ill-formed (im d not inside ker delta_2). Every repair branch
            then fails a named certificate:
              brute grading      -> surviving negative-norm physical states (Q6)
              delete-negatives   -> an unremovable null "zombie" gauge mode
                                    with e^{gamma t} growth, regenerated from
                                    the kept graded ghosts (Q5/Q3; the
                                    Velo-Zwanziger-analog: deletion is not
                                    dynamics-invariant)
              retune delta_2     -> restores closure numerically, but requires
                                    rewriting the transmitted action-level
                                    identity; blocked structurally because the
                                    bit is loop-coherent (Part A), so it cannot
                                    be retuned target-locally.
        This realizes spec items B.2 (Noether-forced d_{RS,-1}), B.4
        (cohomological realization; clean decoupling fails) in finite form.

PART C  the decisive J_quat probe (joint CH-QM/CH-SM):
        C0 single-pair CONTROL: a quaternionic J that ANTIcommutes with the
           Krein Gram flips the Krein sign -- the structure a
           parity-discharging (non-quaternionic) orientation would require.
        C1 Kramers-doubled pairs: with [B, J] = 0 the ghost parity P commutes
           with J, both canonical orientations are J-invariant, the physical
           sector inherits a quaternionic structure, and every J-commutant
           Hermitian carrier on it has EVEN signature (Kramers persists INSIDE
           the physical sector); odd-signature carriers have J-defect > 0.
        C2 real Cl(9,5) = M(64,H): with C = e1 e3 e5 e7 e10 e12 (canon
           convention), J^2 = -1, every e_a commutes with J bit-exactly, and
           the Krein Gram beta_S = e0..e8 (Hermitian, no i-factor) commutes
           with J bit-exactly => J_quat PRESERVES the Krein sign
           K(Jx,Jx) = K(x,x) => an ANTIcommuting fundamental symmetry is
           IMPOSSIBLE in (9,5), and the canonical ghost-parity orientation
           (= K on the triplet, synthesis V2) is J-commuting.
        C3 (7,7) contrast: the analogous C' has J'^2 = +1 (real class) -- the
           Kramers wall dissolves, confirming the canon signature caveat.

PART D  CH-REC hook: a record register logging raw sector-occupation traces
        for both orientations. RAW DATA ONLY -- the co-flip ANALYSIS belongs
        to CH-REC's agent (five-leg swing, H-REC first falsification test).

Receipts: canon/no-go-quaternionic-parity-generation-sector.md (J_quat,
Kramers wall, per-generator-exact certificate);
canon/ghost-parity-krein-synthesis.md (hyperbolic pairs; V2: K = ghost parity
on the triplet); docs/WHERE-GU-STANDS-AND-THE-MISSING-OBJECT-2026-06-27.md
B.2-B.4; explorations/assembly-archaeology-recovered-parameters-2026-07-19.md;
lab/process/boundary-adapter-standing-axiom.md.

Run: python tests/channel-swings/ch_qm_graded_quotient_toy.py   (exit 0 = pass)
"""
from itertools import combinations, product as iproduct

import numpy as np

TOL = 1e-10
RESULTS = {}


def K(B, x, y):
    """Krein form K(x,y) = x^dagger B y (antilinear in the first slot)."""
    return complex(np.conj(x) @ B @ y)


# ----------------------------------------------------------------------------
# PART A -- p2c-style Z/2 register: loop-coherent, locally unreadable
# ----------------------------------------------------------------------------

def part_A():
    L = 6

    def flip(cfg, i):                       # gauge move at vertex i: flip both incident edges
        c = list(cfg)
        c[(i - 1) % L] *= -1
        c[i] *= -1
        return tuple(c)

    def orbit(seed):
        seen, frontier = {seed}, [seed]
        while frontier:
            nxt = []
            for c in frontier:
                for i in range(L):
                    f = flip(c, i)
                    if f not in seen:
                        seen.add(f)
                        nxt.append(f)
            frontier = nxt
        return seen

    plus = orbit(tuple([1] * L))            # holonomy +1 sector
    minus = orbit(tuple([-1] + [1] * (L - 1)))  # holonomy -1 sector
    assert len(plus) == 32 and len(minus) == 32 and not (plus & minus)
    assert all(np.prod(c) == 1 for c in plus) and all(np.prod(c) == -1 for c in minus)

    # local unreadability: every PROPER subset's marginal multiset is identical
    unreadable = True
    for k in range(1, L):
        for S in combinations(range(L), k):
            m_plus = sorted(tuple(c[j] for j in S) for c in plus)
            m_minus = sorted(tuple(c[j] for j in S) for c in minus)
            if m_plus != m_minus:
                unreadable = False
    # the FULL loop reads the bit
    full_reads = (sorted(plus) != sorted(minus))

    print("PART A  p2c-style Z/2 register (loop of 6 edges, vertex-flip gauge)")
    print(f"  orbits: two holonomy sectors of size 32/32 (all 64 configs)      PASS")
    print(f"  every proper-subset marginal identical across sectors (Q4/inert) {'PASS' if unreadable else 'FAIL'}")
    print(f"  full loop product reads the bit                                  {'PASS' if full_reads else 'FAIL'}")
    assert unreadable and full_reads
    RESULTS["A_locally_inert"] = unreadable
    return plus, minus


# ----------------------------------------------------------------------------
# PART B -- Krein graded quotient with Noether-forced differential
# ----------------------------------------------------------------------------
# Basis (dim 9): 0:t (transverse, K=+1) | 1:g 2:s (hyperbolic gauge block)
#                | 3,4,5: u_i  6,7,8: v_i  (three generation/mirror pairs)

DIM = 9
OMEGA, GAMMA, MU, DELTA, CPL = 1.0, 0.7, 1.3, 0.2, 0.35
SIGMA_STAR = +1                              # the orientation baked into the ACTION


def basis_vec(i):
    v = np.zeros(DIM, dtype=complex)
    v[i] = 1.0
    return v


def build_B():
    B = np.zeros((DIM, DIM), dtype=complex)
    B[0, 0] = 1.0
    B[1, 2] = B[2, 1] = 1.0                  # K(g,s) = 1
    for i in range(3):
        B[3 + i, 6 + i] = B[6 + i, 3 + i] = 1.0   # K(u_i, v_i) = 1
    return B


def n_vec(sigma):
    """Null gauge direction n_sigma = (g + i*sigma*s)/sqrt(2)."""
    return (basis_vec(1) + 1j * sigma * basis_vec(2)) / np.sqrt(2)


def w_vec(i, sign):
    """Graded pair mode (u_i + sign*v_i)/sqrt(2); K-norm = sign."""
    return (basis_vec(3 + i) + sign * basis_vec(6 + i)) / np.sqrt(2)


def build_H(B, extra=None):
    """Source-side dynamics with sigma_star baked in (pseudo-Hermitian: B H = H^dag B)."""
    H = np.zeros((DIM, DIM), dtype=complex)
    H[0, 0] = OMEGA                                          # transverse
    npv, nmv = n_vec(SIGMA_STAR), n_vec(-SIGMA_STAR)
    S = np.column_stack([npv[1:3], nmv[1:3]])                # gauge block: eigenvalues +/- i*gamma
    H[1:3, 1:3] = S @ np.diag([1j * GAMMA, -1j * GAMMA]) @ np.linalg.inv(S)
    for i in range(3):                                       # pairs: mu*I + delta*swap  ([H,P]=0)
        H[3 + i, 3 + i] = H[6 + i, 6 + i] = MU
        H[3 + i, 6 + i] = H[6 + i, 3 + i] = DELTA
    # causality-style coupling: pair mode w_1(+) leaks into the sigma_star null
    # direction (pseudo-Hermitian by construction; absorbed by the quotient
    # exactly when the received bit is right)
    w1 = w_vec(0, +1)
    M = CPL * (np.outer(npv, np.conj(B @ w1)) + np.outer(w1, np.conj(B @ npv)))
    H = H + M
    if extra is not None:
        H = H + extra
    assert np.linalg.norm(B @ H - H.conj().T @ B) < TOL, "H must be pseudo-Hermitian"
    return H


def delta2_row(B, H):
    """Transmitted action-level Noether map: delta_2(psi) = K(n_{sigma_star}, H psi)."""
    return np.conj(n_vec(SIGMA_STAR)) @ B @ H                # 1 x DIM row


def kernel(row):
    _, sv, Vh = np.linalg.svd(row.reshape(1, -1))
    return Vh.conj().T[:, 1:]                                # DIM-1 null directions


def part_B():
    B = build_B()
    H = build_H(B)
    d2 = delta2_row(B, H)

    print("\nPART B  Krein graded quotient, Noether-forced differential")
    sig_B = np.linalg.eigvalsh(B)
    print(f"  Krein signature of the module: (+{int((sig_B > 0).sum())}, -{int((sig_B < 0).sum())})  [indefinite]")

    # ---- (a) RIGHT orientation ----
    sigma = SIGMA_STAR
    closure_right = abs(d2 @ n_vec(sigma))
    print(f"  [right bit] Noether closure |delta_2 . d_(-1)| = {closure_right:.2e}  "
          f"{'PASS (closes)' if closure_right < TOL else 'FAIL'}")
    assert closure_right < TOL

    # quotient: ker(delta_2) / im(d_(-1));  physical grading by ghost parity
    ker = kernel(d2)
    n_s = n_vec(sigma)
    # im d inside ker delta_2:
    in_ker = np.linalg.norm(n_s - ker @ (ker.conj().T @ n_s))
    assert in_ker < TOL, "gauge orbit must lie in the constraint surface (right bit)"
    phys_basis = [basis_vec(0)] + [w_vec(i, sigma) for i in range(3)]
    ghost_basis = [w_vec(i, -sigma) for i in range(3)]
    # all representatives lie in ker delta_2 and are K-orthogonal to im d:
    for b in phys_basis + ghost_basis:
        assert abs(d2 @ b) < TOL and abs(K(B, n_s, b)) < TOL
    G_phys = np.array([[K(B, a, b) for b in phys_basis] for a in phys_basis])
    ev_phys = np.linalg.eigvalsh(0.5 * (G_phys + G_phys.conj().T))
    print(f"  [right bit] physical-sector Gram eigenvalues: {np.round(ev_phys.real, 6)}  "
          f"{'PASS (positive-definite, Q1/Q6)' if ev_phys.min() > TOL else 'FAIL'}")
    assert ev_phys.min() > TOL

    # descended dynamics on the quotient: Hermitian wrt the positive Gram -> Q5
    Hq = np.array([[K(B, a, H @ b) for b in phys_basis] for a in phys_basis])
    herm_defect = np.linalg.norm(Hq - Hq.conj().T)
    print(f"  [right bit] descended H Hermitian on physical sector: defect = {herm_defect:.2e}  "
          f"{'PASS (state-preserving, Q5)' if herm_defect < 1e-9 else 'FAIL'}")
    assert herm_defect < 1e-9
    # explicit evolution check + toy Born rule (positivity + normalization) -> Q3
    rng = np.random.default_rng(7)
    psi = rng.standard_normal(4) + 1j * rng.standard_normal(4)
    psi /= np.linalg.norm(psi)
    evals, V = np.linalg.eigh(0.5 * (Hq + Hq.conj().T))
    drift = 0.0
    for t in (0.5, 2.0, 7.0):
        Ut = V @ np.diag(np.exp(-1j * evals * t)) @ V.conj().T
        p = np.abs(Ut @ psi) ** 2
        drift = max(drift, abs(p.sum() - 1.0))
        assert p.min() >= -1e-12
    print(f"  [right bit] Born probabilities positive, sum-1 drift = {drift:.2e}   "
          f"{'PASS (Q3)' if drift < 1e-9 else 'FAIL'}")
    assert drift < 1e-9
    # admissible observables restrict Hermitian (Q2 toy): any K-Hermitian,
    # parity-even operator has Hermitian physical restriction
    A = rng.standard_normal((DIM, DIM))
    P_par = np.zeros((DIM, DIM)); P_par[0, 0] = 1.0
    for i in range(3):
        P_par[3 + i, 6 + i] = P_par[6 + i, 3 + i] = 1.0
    A = A + P_par @ A @ P_par                                # parity-even part (real)
    A = 0.5 * (A + np.linalg.inv(B.real) @ A.T @ B.real)     # K-Hermitian part
    A_phys = np.array([[K(B, a, A @ b) for b in phys_basis] for a in phys_basis])
    obs_defect = np.linalg.norm(A_phys - A_phys.conj().T)
    print(f"  [right bit] K-Hermitian parity-even observable restricts Hermitian: "
          f"defect = {obs_defect:.2e}  {'PASS (Q2)' if obs_defect < 1e-9 else 'FAIL'}")
    assert obs_defect < 1e-9
    RESULTS["B_right_bit"] = "Q1 Q2 Q3 Q5 Q6 toy certificates PASS"

    # ---- (b) WRONG orientation ----
    sigma = -SIGMA_STAR
    n_w = n_vec(sigma)
    closure_wrong = abs(d2 @ n_w)
    print(f"  [wrong bit] Noether closure |delta_2 . d_(-1)| = {closure_wrong:.4f}  "
          f"{'PASS (NON-CLOSURE: cohomological failure, = gamma)' if closure_wrong > 0.1 else 'FAIL'}")
    assert abs(closure_wrong - GAMMA) < 1e-9
    # im d NOT inside ker delta_2 -> the complex is not a complex; quotient ill-formed
    in_ker_w = np.linalg.norm(n_w - ker @ (ker.conj().T @ n_w))
    print(f"  [wrong bit] dist(im d_(-1), ker delta_2) = {in_ker_w:.4f}  "
          f"{'PASS (quotient ill-formed)' if in_ker_w > 0.1 else 'FAIL'}")
    assert in_ker_w > 0.1

    # repair branch 1: brute grading anyway -> negative-norm physical survivors (Q6 fail)
    bad_phys = [basis_vec(0)] + [w_vec(i, sigma) for i in range(3)]
    G_bad = np.array([[K(B, a, b) for b in bad_phys] for a in bad_phys])
    ev_bad = np.linalg.eigvalsh(0.5 * (G_bad + G_bad.conj().T))
    n_neg = int((ev_bad < -TOL).sum())
    print(f"  [wrong bit] repair 1 (brute grading): physical Gram eigenvalues "
          f"{np.round(ev_bad.real, 6)} -> {n_neg} NEGATIVE-NORM SURVIVORS "
          f"{'PASS (Q6 visibly fails)' if n_neg == 3 else 'FAIL'}")
    assert n_neg == 3

    # repair branch 2: delete the negatives -> the null zombie n_+ stays
    # (im d = n_- cannot remove it), grows as e^{gamma t}, and is regenerated
    # from the kept graded ghosts through the causality coupling
    n_zombie = n_vec(SIGMA_STAR)             # still in ker delta_2, NOT quotientable now
    z_in_ker = abs(d2 @ n_zombie)
    growth = []
    evH, VH = np.linalg.eig(H)
    VHi = np.linalg.inv(VH)
    for t in (1.0, 2.0):
        Ut = VH @ np.diag(np.exp(-1j * evH * t)) @ VHi
        growth.append(np.linalg.norm(Ut @ n_zombie))
    w1 = w_vec(0, +1)                        # a KEPT graded ghost in the wrong-bit labeling
    feed = abs(K(B, n_vec(-SIGMA_STAR), H @ w1))             # amplitude H moves w1 -> n_+ direction
    print(f"  [wrong bit] repair 2 (delete negatives): zombie n_+ in constraint surface "
          f"(|delta_2 n_+| = {z_in_ker:.1e}), Hilbert norm growth "
          f"{growth[0]:.3f} -> {growth[1]:.3f} (e^gt: {np.exp(GAMMA):.3f} -> {np.exp(2*GAMMA):.3f})")
    ok_growth = abs(growth[0] - np.exp(GAMMA)) < 1e-6 and abs(growth[1] - np.exp(2 * GAMMA)) < 1e-6
    print(f"              zombie fed by kept ghost sector: |K(n_-, H w_1)| = {feed:.3f} "
          f"{'PASS (regeneration; deletion not invariant -- VZ analog; Q5/Q3 fail)' if (ok_growth and feed > 0.1) else 'FAIL'}")
    assert ok_growth and feed > 0.1

    # repair branch 3: retune delta_2 to the wrong bit -> closure restored
    # numerically, but this rewrites the TRANSMITTED action-level identity.
    d2_retuned = np.conj(n_vec(sigma)) @ B @ H
    closure_retuned = abs(d2_retuned @ n_w)
    print(f"  [wrong bit] repair 3 (retune delta_2): closure after retune = {closure_retuned:.1e} "
          f"-- 'works', BUT requires rewriting the transmitted Noether identity;")
    print("              blocked structurally: the bit is loop-coherent (Part A), so no local")
    print("              operation on the target side can retune it (non-retuning is structural).")
    assert closure_retuned < TOL
    RESULTS["B_wrong_bit"] = ("non-closure = gamma (cohomological, primary); brute grading -> 3 negative-norm "
                              "survivors; deletion -> zombie e^{gamma t} + regeneration; retune blocked by storage")


# ----------------------------------------------------------------------------
# PART C -- the decisive J_quat probe
# ----------------------------------------------------------------------------

def antilinear_conj_op(Cm, A):
    """For J = Cm . conj:  J A J^{-1} = Cm conj(A) Cm^{-1} (linear)."""
    return Cm @ np.conj(A) @ np.linalg.inv(Cm)


def part_C0():
    """Single-pair CONTROL: a quaternionic J that ANTIcommutes with the Gram."""
    B2 = np.array([[0, 1], [1, 0]], dtype=complex)           # hyperbolic pair (u,v)
    Cm = np.array([[0, 1], [-1, 0]], dtype=complex)          # i*sigma_2, real, Cm^2 = -I
    anti = np.linalg.norm(antilinear_conj_op(Cm, B2) + B2)
    rng = np.random.default_rng(3)
    x = rng.standard_normal(2) + 1j * rng.standard_normal(2)
    Jx = Cm @ np.conj(x)
    flip = abs(K(B2, Jx, Jx) + K(B2, x, x))
    print("\nPART C  the decisive J_quat probe")
    print(f"  C0 control (single pair): J anticommutes with Gram (defect {anti:.1e}) "
          f"=> K(Jx,Jx) = -K(x,x) (residual {flip:.1e})")
    print("     -> THIS is the structure a Krein-sign-discharging (non-quaternionic)")
    print("        orientation would require: J exchanges the two halves, and the bit")
    print("        breaks the J-symmetry. C2 tests whether Cl(9,5) is in this class.")
    assert anti < TOL and flip < TOL


def part_C1():
    """Kramers-doubled pairs: [B,J]=0 -> Kramers persists INSIDE the physical sector."""
    # 4 pairs (u_i, v_i), i=1..4; J maps pair-doublets (1,2) and (3,4) quaternionically.
    n_pairs = 4
    dim = 2 * n_pairs                                        # order: u1 v1 u2 v2 u3 v3 u4 v4
    B = np.zeros((dim, dim), dtype=complex)
    P = np.zeros((dim, dim), dtype=complex)                  # ghost parity: u <-> v
    for i in range(n_pairs):
        B[2 * i, 2 * i + 1] = B[2 * i + 1, 2 * i] = 1.0
        P[2 * i, 2 * i + 1] = P[2 * i + 1, 2 * i] = 1.0
    Cm = np.zeros((dim, dim), dtype=complex)
    for (a, b) in [(0, 1), (2, 3)]:                          # pair-doublet blocks
        # u_a -> u_b, v_a -> v_b ; u_b -> -u_a, v_b -> -v_a   (Cm^2 = -I, real)
        Cm[2 * b, 2 * a] = Cm[2 * b + 1, 2 * a + 1] = 1.0
        Cm[2 * a, 2 * b] = Cm[2 * a + 1, 2 * b + 1] = -1.0
    assert np.linalg.norm(Cm @ np.conj(Cm) + np.eye(dim)) < TOL          # J^2 = -1
    cB = np.linalg.norm(antilinear_conj_op(Cm, B) - B)
    cP = np.linalg.norm(antilinear_conj_op(Cm, P) - P)
    print(f"  C1 Kramers-doubled pairs: [B,J] defect = {cB:.1e}, [P,J] defect = {cP:.1e} (both commute)")
    assert cB < TOL and cP < TOL

    # physical sector (canonical orientation +): span{(u_i + v_i)/sqrt2}
    W = np.zeros((dim, n_pairs), dtype=complex)
    for i in range(n_pairs):
        W[2 * i, i] = W[2 * i + 1, i] = 1 / np.sqrt(2)
    # J-invariance of the physical sector + induced quaternionic structure
    JW = Cm @ np.conj(W)                                     # J acts columnwise (basis real)
    proj_out = np.linalg.norm(JW - W @ (W.conj().T @ JW))
    Cp = W.conj().T @ Cm @ np.conj(W)                        # induced Cm on the sector
    j2 = np.linalg.norm(Cp @ np.conj(Cp) + np.eye(n_pairs))
    print(f"  C1 physical sector J-invariant (leak {proj_out:.1e}); induced J^2 = -1 (residual {j2:.1e})")
    assert proj_out < TOL and j2 < TOL

    # J-commutant Hermitian carriers on the physical sector: Kramers-degenerate
    # spectra, hence EVEN signature (shifts included to spread the signatures)
    rng = np.random.default_rng(11)
    sigs, degenerate = [], True
    for shift in (0.0, 0.0, 0.0, 1.2, -1.2, 2.5):
        A = rng.standard_normal((n_pairs, n_pairs)) + 1j * rng.standard_normal((n_pairs, n_pairs))
        A = 0.5 * (A + A.conj().T) + shift * np.eye(n_pairs)
        A = 0.5 * (A + antilinear_conj_op(Cp, A))            # project onto J-commutant
        A = 0.5 * (A + A.conj().T)
        ev = np.linalg.eigvalsh(A)
        degenerate &= all(abs(ev[2 * i] - ev[2 * i + 1]) < 1e-9 for i in range(n_pairs // 2))
        sigs.append(int((ev > 1e-9).sum()) - int((ev < -1e-9).sum()))
    all_even = all(s % 2 == 0 for s in sigs) and degenerate
    # foreign carrier: rank-1 projector -> odd signature, J-defect > 0
    P1 = np.zeros((n_pairs, n_pairs), dtype=complex); P1[0, 0] = 1.0
    d_for = np.linalg.norm(antilinear_conj_op(Cp, P1) - P1)
    print(f"  C1 J-commutant carrier signatures {sorted(sigs)} -> all EVEN, spectra doubly "
          f"degenerate? {all_even}   (Kramers INSIDE the physical sector)")
    print(f"  C1 foreign odd carrier (rank-1): signature 1, J-defect = {d_for:.2f} (> 0: an import)")
    assert all_even and d_for > 0.5


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


def part_C2():
    """Real Cl(9,5) = M(64,H): the Krein Gram COMMUTES with J_quat -> no anticommuting
    fundamental symmetry; the canonical ghost-parity orientation is J-commuting."""
    G = jw_gammas(7)
    e = [G[a] if a < 9 else 1j * G[a] for a in range(14)]    # signature (9,5)
    C = e[1] @ e[3] @ e[5] @ e[7] @ e[10] @ e[12]            # canon convention (C07 exact cert)
    d128 = 128
    j2 = np.linalg.norm(C @ np.conj(C) + np.eye(d128))
    gen_defect = max(np.linalg.norm(e[a] @ C - C @ np.conj(e[a])) for a in range(14))
    betaS = np.eye(d128, dtype=complex)
    for a in range(9):
        betaS = betaS @ e[a]                                 # product of the 9 spacelike gammas
    herm = np.linalg.norm(betaS - betaS.conj().T)            # Hermitian WITHOUT i-factor
    b2 = np.linalg.norm(betaS @ betaS - np.eye(d128))
    gram_defect = np.linalg.norm(betaS @ C - C @ np.conj(betaS))
    print(f"  C2 Cl(9,5): J^2 = -1 (residual {j2:.1e}); all 14 e_a J-commute (max defect {gen_defect:.1e})")
    print(f"  C2 Krein Gram beta_S = e0..e8: Hermitian (defect {herm:.1e}), beta^2 = I (defect {b2:.1e}),")
    print(f"     [beta_S, J_quat] defect = {gram_defect:.1e}  -> the Gram COMMUTES with J_quat")
    assert j2 < TOL and gen_defect < TOL and herm < TOL and b2 < TOL and gram_defect < TOL
    # => J_quat preserves the Krein sign
    rng = np.random.default_rng(5)
    worst = 0.0
    for _ in range(8):
        x = rng.standard_normal(d128) + 1j * rng.standard_normal(d128)
        Jx = C @ np.conj(x)
        worst = max(worst, abs(K(betaS, Jx, Jx) - K(betaS, x, x)))
    print(f"  C2 sign preservation: max |K(Jx,Jx) - K(x,x)| = {worst:.1e}")
    print("     THEOREM: J_K J = -J J_K would force J(H_+) subset H_- ; but J preserves the")
    print("     Krein sign, so an ANTIcommuting fundamental symmetry is IMPOSSIBLE in (9,5).")
    # canonical orientation projectors Pi_+- = (1 +- beta_S)/2 commute with J
    Pp = 0.5 * (np.eye(d128) + betaS)
    ori_defect = np.linalg.norm(Pp @ C - C @ np.conj(Pp))
    print(f"  C2 canonical orientation projector (1+beta_S)/2: J-commutation defect = {ori_defect:.1e}")
    print("     -> both canonical orientations are J_quat-INVARIANT; each half inherits a")
    print("        quaternionic structure; Kramers persists inside the selected sector.")
    assert worst < 1e-9 and ori_defect < TOL


def part_C3():
    """(7,7) contrast: the analogous conjugation squares to +1 -- real class, wall dissolves."""
    G = jw_gammas(7)
    T = {4, 5, 6, 7, 8, 9, 10}                               # repo (7,7) timelike convention
    e = [1j * G[a] if a in T else G[a] for a in range(14)]
    # factors: generators with conj(e_a) = -e_a  (imag spacelike + even-index timelike)
    factors = [1, 3, 4, 6, 8, 10, 11, 13]
    C = np.eye(128, dtype=complex)
    for a in factors:
        C = C @ e[a]
    gen_defect = max(np.linalg.norm(e[a] @ C - C @ np.conj(e[a])) for a in range(14))
    j2p = np.linalg.norm(C @ np.conj(C) - np.eye(128))       # J'^2 = +1 ?
    print(f"  C3 Cl(7,7) contrast: all e_a J'-commute (max defect {gen_defect:.1e}); "
          f"J'^2 = +1 (residual {j2p:.1e})")
    print("     -> REAL class: no Kramers pairing; the parity wall is (9,5)/H-class-specific,")
    print("        exactly the canon signature caveat.")
    assert gen_defect < TOL and j2p < TOL


# ----------------------------------------------------------------------------
# PART D -- CH-REC record-register hook (raw traces only; no conclusion here)
# ----------------------------------------------------------------------------

def part_D():
    B = build_B()
    # sigma-INDEPENDENT weak drive t <-> u_1 (part of the transmitted action)
    lam = 0.15
    t_v, q1 = basis_vec(0), basis_vec(3)
    D = lam * (np.outer(t_v, np.conj(B @ q1)) + np.outer(q1, np.conj(B @ t_v)))
    H = build_H(B, extra=D)
    evH, VH = np.linalg.eig(H)
    VHi = np.linalg.inv(VH)
    traces = {}
    for sigma in (+1, -1):
        w1, m1 = w_vec(0, sigma), w_vec(0, -sigma)           # graded physical / ghost modes (pair 1)
        occ = []
        for t in np.linspace(0.0, 4.0, 9):
            Ut = VH @ np.diag(np.exp(-1j * evH * t)) @ VHi
            psi = Ut @ t_v
            occ.append((round(t, 2), round(abs(K(B, w1, psi)) ** 2, 6), round(abs(K(B, m1, psi)) ** 2, 6)))
        # register = time-integrated (physical - ghost) occupation difference
        reg = float(np.trapezoid([a[1] - a[2] for a in occ], [a[0] for a in occ]))
        traces[sigma] = {"occ_(t,phys,ghost)": occ, "register_integral": round(reg, 6)}
    print("\nPART D  CH-REC hook: record-register raw traces (drive t -> pair 1, sigma-independent)")
    for sigma in (+1, -1):
        print(f"  sigma = {sigma:+d}: register integral = {traces[sigma]['register_integral']:+.6f}")
    print("  NOTE: raw data only. Whether this constitutes the H-REC co-flip (orientation flip")
    print("  flips physical selection AND record direction together, always) is CH-REC's call.")
    RESULTS["D_ch_rec_hook"] = traces


# ----------------------------------------------------------------------------

def main():
    np.set_printoptions(precision=5, suppress=True, linewidth=140)
    part_A()
    part_B()
    part_C0()
    part_C1()
    part_C2()
    part_C3()
    part_D()
    print("\n=== VERDICT ===")
    print("Toy: right orientation -> all six toy certificates PASS; wrong orientation -> the")
    print("failure is COHOMOLOGICAL (Noether non-closure), with negative-norm survivors and an")
    print("unremovable regenerating zombie as symptoms; retuning is blocked by loop-coherent storage.")
    print("J_quat: the transmitted Z/2 orientation CANNOT anticommute with J_quat in Cl(9,5)")
    print("(the Krein Gram commutes with J_quat, so J_quat preserves the Krein sign), and the")
    print("canonical ghost-parity orientation COMMUTES with J_quat. One payload bit therefore")
    print("fixes the Krein sign but does NOT discharge the quaternionic-parity no-go:")
    print("generations require the rank-pin route, a fifth (larger-type) payload item, or the")
    print("(7,7) signature escape (C3). ALL CONDITIONAL under the standing axiom; no claim moves.")
    return RESULTS


if __name__ == "__main__":
    main()
