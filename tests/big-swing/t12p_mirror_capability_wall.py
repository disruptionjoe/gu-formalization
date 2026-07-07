"""
T12' -- THE MIRROR SECTOR AS A ZERO-STATISTICAL-TRACE CAPABILITY WALL.

Falsifiable leg of the bridge hypothesis "the GU mirror sector = collective-not-individual records"
(explorations/time-as-finality-crosswalk/mirror-as-collective-capability-boundary-2026-07-07.md).
The hypothesis reads GU's ghost (mirror) sector as a T395-style capability difference: a real
difference between two states that leaves ZERO statistical trace on an INDIVIDUAL observer, yet is a
genuine (collectively accessible) difference. This script promotes-or-kills that reading on the actual
192-dim triplet carrier.

CARRIER (reused verbatim from tests/generation-sector/ghost_parity_krein.py and
tests/big-swing/vg_v8_t5_map_attempt.py -- the verified recipe):
  * 192-dim self-dual triplet W with Krein form K, signature (+96, -96, 0); K|_W is an involution.
  * P_ghost = sign(K) = K|_W, and P_ghost = -Q5 (compressed internal spatial volume) at ~1e-14.
  * PHYSICAL sector  W+ = K-positive eigenspace (96-dim, positive Krein norm) -- what an INDIVIDUAL
    observer accesses through the Turok-Bateman projector Born rule.
  * MIRROR/ghost sector W- = K-negative eigenspace (96-dim, negative Krein norm) -- reached only
    COLLECTIVELY.
  Because K|_W is an involution with an orthonormal eigenbasis, on W+ the Krein form equals the
  ordinary inner product (+I_96) and on W- it equals minus the ordinary inner product (-I_96).

CAPABILITIES (the operational distinction being tested):
  * INDIVIDUAL-accessible operations = W+-preserving Krein-unitaries. A W+-preserving K-unitary also
    preserves W- (= K-orthogonal complement), so it is BLOCK-DIAGONAL U = U+ (+) U- with U+, U- in
    U(96). Individual measurement statistics = projector Born rule: read only P+ psi.
  * COLLECTIVE operations = the FULL Krein-unitary group U(96,96) on all of W (K-unitary but NOT
    block-diagonal): it can rotate mirror amplitude into the physical sector.

THE TEST (capability, NOT pre-projected measurement -- the anti-tautology core):
  Two states share their physical (W+) part and differ ONLY in their mirror (W-) part:
      psi  = psi_+  (+)  a * phi_-        psi' = psi_+  (+)  b * phi_-     (same psi_+, same phi_-, a != b)
  LEG A (individual invisibility): the MAX distinguishing residual over (a) the projector-Born
    statistics of a basis of physical-sector observables and (b) EVERY individual-accessible
    (block-diagonal K-unitary) operation applied first. Expect ~0 and VERIFY.
  LEG B (collective visibility): the K-norm difference, the K-pairing, the mirror-number collective
    observable, and an explicit full Krein-unitary boost that maps the mirror difference into a
    physical-detectable difference. Expect nonzero.
  VERDICT: CAPABILITY WALL CONFIRMED iff Leg A ~ 0 (zero statistical trace) AND Leg B != 0 (genuine).
           REFUTED if Leg A != 0; DEGENERATE if Leg B ~ 0.

DISCRIMINATING CONTROLS (the test must be able to fail):
  * A control pair differing in the PHYSICAL (W+) sector MUST be individually distinguishable
    (Leg A must return nonzero for it) -- proving the Leg A statistic is not trivially zero.
  * The mirror difference must be genuinely present in the full space (||psi - psi'|| and the K-norm
    difference nonzero) -- else DEGENERATE.
  * WHY THIS IS NOT THE TAUTOLOGY "the projector removes the ghost": the same block-diagonal
    K-self-adjoint observable P- that reads the mirror has raw Krein expectation that DOES separate
    psi from psi' (that is Leg B / the collective reading), while its individual projector-Born
    statistic is 0. Leg A's zero is a statement about the CLOSURE of the individual-accessible
    operation algebra (block-diagonal ops can never move mirror content into the physical sector),
    checked against a powered physical-sector control -- not about a hand-inserted pre-projection.

TARGET-IMPORT GUARD: no element of {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8} is assumed,
inserted, or divided by. Dimensions (128, 1664, 192, 96) are measured outputs, asserted after
measurement. Deterministic (seed). Prints every cited number.

Run: python tests/big-swing/t12p_mirror_capability_wall.py    (exit 0)
"""
import numpy as np
from scipy.linalg import expm

np.random.seed(20260707)
rng = np.random.default_rng(20260707)
N, DIM = 14, 128
TOL = 1e-9
nrm = np.linalg.norm
comm = lambda A, B: A @ B - B @ A
acomm = lambda A, B: A @ B + B @ A

FAIL = []
def check(name, ok, detail=""):
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {name} {detail}")
    if not ok:
        FAIL.append(name)


def jw(n):
    I = np.eye(2, dtype=complex)
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    G = []
    for k in range(n):
        L, R = [s3] * k, [I] * (n - 1 - k)
        for mid in (s1, s2):
            o = np.array([[1 + 0j]])
            for m in L + [mid] + R:
                o = np.kron(o, m)
            G.append(o)
    return G


base = jw(7)
I128, I14 = np.eye(DIM, dtype=complex), np.eye(N, dtype=complex)


def build(timelike):
    """Verified carrier recipe (reused from ghost_parity_krein.py / vg_v8_t5_map_attempt.py)."""
    e = [(1j * base[a] if a in timelike else base[a]) for a in range(14)]
    spacelike = [a for a in range(14) if a not in timelike]

    def sgen(i, j):
        return 0.25 * (e[i] @ e[j] - e[j] @ e[i])

    def lvec(i, j):
        M = np.zeros((N, N), dtype=complex); M[i, j] = 1; M[j, i] = -1; return M

    def gen(i, j):
        return np.kron(I14, sgen(i, j)) + np.kron(lvec(i, j), I128)

    Gam = np.hstack(e)
    rankG = np.linalg.matrix_rank(Gam)
    Pi = np.eye(N * DIM, dtype=complex) - Gam.conj().T @ np.linalg.inv(Gam @ Gam.conj().T) @ Gam
    w, Vv = np.linalg.eigh(Pi)
    Wk = Vv[:, w > 0.5]
    SDp = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
    J3full = [gen(a, b) + gen(c, d) for (a, b, c, d) in SDp]
    Cas = -(J3full[0] @ J3full[0] + J3full[1] @ J3full[1] + J3full[2] @ J3full[2])
    CasK = Wk.conj().T @ Cas @ Wk; CasK = 0.5 * (CasK + CasK.conj().T)
    ev, U = np.linalg.eigh(CasK)
    top = max(round(x.real, 3) for x in ev)
    Wt = Wk @ U[:, np.abs(ev - top) < 1e-3]

    bS = I128.copy()
    for s in spacelike:
        bS = bS @ e[s]
    if nrm(bS.conj().T + bS) < TOL:
        bS = 1j * bS
    bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
    betares = max(nrm(bS @ sgen(i, j) + sgen(i, j).conj().T @ bS)
                  for i in range(14) for j in range(i + 1, 14))
    etaV = np.diag([(-1.0 if a in timelike else 1.0) for a in range(14)]).astype(complex)
    Kful = np.kron(etaV, bS)
    om = I128.copy()
    for a in range(14):
        om = om @ e[a]
    om2 = (np.trace(om @ om) / DIM).real
    Cful = np.kron(I14, om if om2 > 0 else (-1j) * om)

    Rc = lambda M: Wt.conj().T @ M @ Wt
    K = Rc(Kful); K = 0.5 * (K + K.conj().T)
    C = Rc(Cful)
    kev, kU = np.linalg.eigh(K)
    P = (kU * np.sign(kev)) @ kU.conj().T; P = 0.5 * (P + P.conj().T)
    return dict(e=e, Wt=Wt, Rc=Rc, K=K, P=P, C=C, kev=kev, kU=kU,
                betares=betares, rankG=rankG, kerdim=Wk.shape[1], top=top, timelike=timelike)


def mono_big(e, idxs):
    Mm = I128.copy()
    for a in idxs:
        Mm = Mm @ e[a]
    return np.kron(I14, Mm)


def rand_unit(dim):
    v = rng.standard_normal(dim) + 1j * rng.standard_normal(dim)
    return v / nrm(v)


def rand_unitary(dim):
    X = rng.standard_normal((dim, dim)) + 1j * rng.standard_normal((dim, dim))
    Q, R = np.linalg.qr(X)
    return Q @ np.diag(np.exp(1j * np.angle(np.diag(R))))


def rand_herm(dim):
    X = rng.standard_normal((dim, dim)) + 1j * rng.standard_normal((dim, dim))
    return 0.5 * (X + X.conj().T)


def phys_coords(Ep, psi):
    """Individual-accessible physical component of a full-space state, in W+ coordinates."""
    return Ep.conj().T @ psi


def trace_distance_pure(u, v):
    """Max over physical observables ||O||<=1 of |<O>_u - <O>_v| for pure physical states given by
    (unnormalized) W+ coordinate vectors u, v. Equals sqrt(1 - |<u^,v^>|^2)."""
    if nrm(u) < 1e-14 or nrm(v) < 1e-14:
        return 0.0
    uu, vv = u / nrm(u), v / nrm(v)
    ov = abs(np.vdot(uu, vv))
    return np.sqrt(max(0.0, 1.0 - ov ** 2))


def born_stat(Ep, psi, h):
    """Projector-Born-rule expectation of physical-sector observable h (in W+ coords) in state psi."""
    c = phys_coords(Ep, psi)
    return (c.conj() @ h @ c).real / (c.conj() @ c).real


def run(timelike, label, full=True):
    print("\n" + "=" * 108)
    print(f"CARRIER {label}: signature timelike={sorted(timelike)}")
    print("=" * 108)
    D = build(timelike)
    K, P, C, kev, kU = D["K"], D["P"], D["C"], D["kev"], D["kU"]
    e = D["e"]
    td = D["Wt"].shape[1]

    # ---------------------------------------------------------------- [0] ANCHORS (must reproduce)
    print("\n[0] ANCHORS")
    npl, nmi, nz = int((kev > TOL).sum()), int((kev < -TOL).sum()), int((np.abs(kev) < TOL).sum())
    check("rank(Gamma)=128, ker(Gamma)=1664, triplet dim=192",
          D["rankG"] == 128 and D["kerdim"] == 1664 and td == 192,
          f"({D['rankG']},{D['kerdim']},{td})")
    check("su(2)+ Casimir top eig = 8 (measured)", abs(D["top"] - 8.0) < 1e-6, f"{D['top']}")
    check("beta_S pseudo-anti-Herm residual ~ 0", D["betares"] < TOL, f"{D['betares']:.1e}")
    check("triplet Krein signature (+96, -96, 0)", (npl, nmi, nz) == (96, 96, 0),
          f"(+{npl}, -{nmi}, 0:{nz})")
    check("|K|-eigs all exactly 1 (K|_W is an involution)",
          abs(np.abs(kev).min() - 1) < 1e-9 and abs(np.abs(kev).max() - 1) < 1e-9,
          f"range [{np.abs(kev).min():.6f}, {np.abs(kev).max():.6f}]")
    check("P_ghost = sign(K) = K|_W", nrm(P - K) < 1e-9, f"||P-K||={nrm(P - K):.1e}")
    Q5 = D["Rc"](mono_big(e, [9, 10, 11, 12, 13])) if label == "(9,5)" else None
    if Q5 is not None:
        check("P_ghost = -Q5 (internal spatial volume) at ~1e-14", nrm(Q5 + P) < 1e-9,
              f"||Q5+P||={nrm(Q5 + P):.1e}")

    # ----------------------------------------------- [1] PHYSICAL / MIRROR SPLIT and inner products
    print("\n[1] PHYSICAL (W+) / MIRROR (W-) SPLIT")
    Ep = kU[:, kev > 0]          # 192 x 96 : physical, K-positive
    Em = kU[:, kev < 0]          # 192 x 96 : mirror,   K-negative
    dpl, dmi = Ep.shape[1], Em.shape[1]
    check("dim W+ = 96 (physical, positive Krein norm)", dpl == 96, f"{dpl}")
    check("dim W- = 96 (mirror/ghost, negative Krein norm)", dmi == 96, f"{dmi}")
    Q = np.hstack([Ep, Em])
    check("eigenbasis Q=[W+|W-] is unitary (Q^H Q = I_192)", nrm(Q.conj().T @ Q - np.eye(td)) < 1e-9,
          f"{nrm(Q.conj().T @ Q - np.eye(td)):.1e}")
    Kpp = Ep.conj().T @ K @ Ep
    Kmm = Em.conj().T @ K @ Em
    Kpm = Ep.conj().T @ K @ Em
    check("Krein form on W+ equals +I_96 (positive-definite physical inner product)",
          nrm(Kpp - np.eye(96)) < 1e-9, f"||K|W+ - I||={nrm(Kpp - np.eye(96)):.1e}")
    check("Krein form on W- equals -I_96 (negative-definite ghost norm)",
          nrm(Kmm + np.eye(96)) < 1e-9, f"||K|W- + I||={nrm(Kmm + np.eye(96)):.1e}")
    check("W+ and W- are K-orthogonal (no cross Krein pairing)", nrm(Kpm) < 1e-9, f"{nrm(Kpm):.1e}")
    Pplus, Pminus = Ep @ Ep.conj().T, Em @ Em.conj().T
    check("projectors P+ = (I+P)/2 and P- = (I-P)/2 (Turok-Bateman physical projector)",
          nrm(Pplus - 0.5 * (np.eye(td) + P)) < 1e-9 and nrm(Pminus - 0.5 * (np.eye(td) - P)) < 1e-9,
          f"{nrm(Pplus - 0.5 * (np.eye(td) + P)):.1e}")

    # ------------------------------------------------------------------------ [2] STATE CONSTRUCTION
    print("\n[2] STATE CONSTRUCTION  (psi, psi' agree on W+, differ only on W-)")
    c_plus = rand_unit(96)       # shared physical component (W+ coords)
    d_min = rand_unit(96)        # shared mirror direction     (W- coords)
    a, b = 0.8, 0.4              # different mirror weights (real, |a| != |b|)
    psi_plus = Ep @ c_plus
    psi = psi_plus + Em @ (a * d_min)
    psip = psi_plus + Em @ (b * d_min)
    print(f"    a (psi mirror weight)  = {a}")
    print(f"    b (psi' mirror weight) = {b}")
    knorm = lambda v: (v.conj() @ K @ v).real
    kn, knp = knorm(psi), knorm(psip)
    print(f"    Krein norm (psi)  = |c+|^2 - a^2 = {kn:+.4f}   (positive-norm physical state)")
    print(f"    Krein norm (psi') = |c+|^2 - b^2 = {knp:+.4f}")
    check("physical (W+) components are IDENTICAL (agree on the physical sector)",
          nrm(phys_coords(Ep, psi) - phys_coords(Ep, psip)) < 1e-12,
          f"||P+psi - P+psi'||={nrm(phys_coords(Ep, psi) - phys_coords(Ep, psip)):.1e}")
    check("mirror (W-) components DIFFER (states differ only in the ghost sector)",
          nrm(phys_coords(Em, psi) - phys_coords(Em, psip)) > 0.1,
          f"||P-psi - P-psi'||={nrm(phys_coords(Em, psi) - phys_coords(Em, psip)):.3f}")

    # ================================================================ LEG A : individual invisibility
    print("\n[3] LEG A -- INDIVIDUAL INVISIBILITY (expect ~0)")
    # NUMERICS NOTE: the trace distance sqrt(1-|<u,v>|^2) sqrt-amplifies the ~1e-16 rounding of the
    # overlap to a ~1e-8 FLOOR when the two states are identical (sqrt(1e-16)=1e-8). The pass/fail is
    # therefore based on the LINEAR, un-amplified residuals (Born-statistic differences and the
    # physical-component difference norm), which read the true machine zero (~1e-15). The trace
    # distance is printed as an annotated auxiliary.
    cA, cAp = phys_coords(Ep, psi), phys_coords(Ep, psip)
    legA_tracedist = trace_distance_pure(cA, cAp)   # auxiliary: floors at sqrt(eps)~1e-8 for equal states
    obs_max = 0.0
    for _ in range(400):
        h = rand_herm(96)
        h = h / nrm(h, 2)                            # operator-norm-normalized observable
        obs_max = max(obs_max, abs(born_stat(Ep, psi, h) - born_stat(Ep, psip, h)))
    print(f"    (i) LINEAR max distinguishing residual over 400 physical observables (Born rule)"
          f" = {obs_max:.2e}")
    print(f"        [aux] trace distance sqrt(1-|<.>|^2) over ALL physical observables            "
          f" = {legA_tracedist:.2e}  (sqrt(eps)~1e-8 floor: identical states)")
    # (ii) apply EVERY individual-accessible (block-diagonal K-unitary) operation first, then measure
    op_max_lin = 0.0        # linear: ||P+ U psi - P+ U psi'|| (faithful machine-zero measure)
    op_max_obs = 0.0        # linear: Born-statistic residual after the operation
    op_max_td = 0.0         # auxiliary: trace distance (sqrt-eps floored)
    K_UNI = 60
    for _ in range(K_UNI):
        Uop = Q @ np.block([[rand_unitary(96), np.zeros((96, 96))],
                            [np.zeros((96, 96)), rand_unitary(96)]]) @ Q.conj().T
        # confirm it is a genuine individual-accessible operation: K-unitary AND W+-preserving
        assert nrm(Uop.conj().T @ K @ Uop - K) < 1e-8      # Krein-unitary
        assert nrm(Pminus @ Uop @ Pplus) < 1e-8            # W+ -> W+ (block-diagonal)
        s1, s2 = Uop @ psi, Uop @ psip
        op_max_lin = max(op_max_lin, nrm(phys_coords(Ep, s1) - phys_coords(Ep, s2)))
        op_max_td = max(op_max_td, trace_distance_pure(phys_coords(Ep, s1), phys_coords(Ep, s2)))
        h = rand_herm(96); h = h / nrm(h, 2)
        op_max_obs = max(op_max_obs, abs(born_stat(Ep, s1, h) - born_stat(Ep, s2, h)))
    print(f"    (ii) LINEAR max ||P+ U psi - P+ U psi'|| over {K_UNI} individual-accessible ops"
          f"     = {op_max_lin:.2e}")
    print(f"         LINEAR max Born-stat residual after those operations                        "
          f" = {op_max_obs:.2e}")
    print(f"         [aux] trace distance after those operations                                "
          f" = {op_max_td:.2e}  (sqrt(eps)~1e-8 floor)")
    legA = max(obs_max, op_max_lin, op_max_obs)     # LINEAR residuals only (faithful machine zero)
    print(f"    => LEG A key residual (LINEAR, max over statistics AND accessible operations) = {legA:.2e}")
    check("LEG A: mirror difference is INVISIBLE to every individual-accessible operation (~0)",
          legA < 1e-9, f"{legA:.1e}")

    # ================================================================ LEG B : collective visibility
    print("\n[4] LEG B -- COLLECTIVE VISIBILITY / GENUINE DIFFERENCE (expect nonzero)")
    # (i) full Krein-space distinguishers
    dknorm = abs(kn - knp)
    kpair = (psi.conj() @ K @ psip)                 # Krein pairing <psi|psi'>_K
    # mirror-number collective observable N- = P- (K-self-adjoint). Individual (projector-Born) reads 0.
    Nminus = Pminus
    coll_expec_psi = (psi.conj() @ K @ Nminus @ psi).real     # full Krein expectation
    coll_expec_psip = (psip.conj() @ K @ Nminus @ psip).real
    ind_expec_psi = born_stat(Ep, psi, Ep.conj().T @ Nminus @ Ep)   # projector-Born of same observable
    ind_expec_psip = born_stat(Ep, psip, Ep.conj().T @ Nminus @ Ep)
    print(f"    (i) K-norm difference |<psi|psi>_K - <psi'|psi'>_K|              = {dknorm:.4f}")
    print(f"        Krein pairing <psi|psi'>_K = {kpair.real:+.4f}{kpair.imag:+.4f}i "
          f"(|.|={abs(kpair):.4f}; != each self-norm => distinct K-vectors)")
    print(f"        mirror-number obs N-=P- : COLLECTIVE (full-Krein) expectation "
          f"psi={coll_expec_psi:+.4f}  psi'={coll_expec_psip:+.4f}  diff={abs(coll_expec_psi - coll_expec_psip):.4f}")
    print(f"        mirror-number obs N-=P- : INDIVIDUAL (projector-Born) expectation "
          f"psi={ind_expec_psi:+.2e}  psi'={ind_expec_psip:+.2e}  (both ~0: ghost removed)")
    # (ii) explicit full Krein-unitary boost moving mirror amplitude INTO the physical sector
    Bblk = 0.6 * (rng.standard_normal((96, 96)) + 1j * rng.standard_normal((96, 96))) / np.sqrt(96)
    Hgen = np.block([[np.zeros((96, 96)), Bblk], [-Bblk.conj().T, np.zeros((96, 96))]])  # eta-self-adj
    M = expm(1j * Hgen)
    Vcoll = Q @ M @ Q.conj().T
    check("collective op V is a FULL Krein-unitary (V^H K V = K)",
          nrm(Vcoll.conj().T @ K @ Vcoll - K) < 1e-8, f"{nrm(Vcoll.conj().T @ K @ Vcoll - K):.1e}")
    check("collective op V is NOT block-diagonal (mixes W- into W+): ||P+ V P-|| > 0",
          nrm(Pplus @ Vcoll @ Pminus) > 0.1, f"||P+ V P-||={nrm(Pplus @ Vcoll @ Pminus):.3f}")
    cB, cBp = phys_coords(Ep, Vcoll @ psi), phys_coords(Ep, Vcoll @ psip)
    legB_boost_td = trace_distance_pure(cB, cBp)
    legB_boost_raw = nrm(cB - cBp)
    print(f"    (ii) after collective boost V: physical components now DIFFER")
    print(f"         ||P+ V psi - P+ V psi'||               = {legB_boost_raw:.4f}")
    print(f"         physical trace distance after V (indiv-measurable post-collective-op) = {legB_boost_td:.4f}")
    legB = max(dknorm, abs(coll_expec_psi - coll_expec_psip), legB_boost_td, legB_boost_raw)
    print(f"    => LEG B key residual (max over collective distinguishers) = {legB:.4f}")
    check("LEG B: the mirror difference IS genuine and collectively accessible (nonzero)",
          legB > 1e-3, f"{legB:.3f}")

    # =============================================================== CONTROLS (the test must be able to fail)
    print("\n[5] DISCRIMINATING CONTROLS")
    # C1: a control pair differing in the PHYSICAL (W+) sector MUST be individually distinguishable.
    c_plus2 = rand_unit(96)
    xi = Ep @ c_plus + Em @ (a * d_min)
    xip = Ep @ c_plus2 + Em @ (a * d_min)          # same mirror part, DIFFERENT physical part
    ctrl_td = trace_distance_pure(phys_coords(Ep, xi), phys_coords(Ep, xip))
    ctrl_obs = 0.0
    for _ in range(400):
        h = rand_herm(96); h = h / nrm(h, 2)
        ctrl_obs = max(ctrl_obs, abs(born_stat(Ep, xi, h) - born_stat(Ep, xip, h)))
    print(f"    C1 physical-sector control pair (differ in W+): Leg A statistic (trace distance) "
          f"= {ctrl_td:.4f}")
    print(f"       sampled max Born-stat residual over 400 physical observables               "
          f"= {ctrl_obs:.4f}")
    check("CONTROL C1: physical-sector difference IS individually distinguishable (Leg A has power)",
          ctrl_td > 1e-2 and ctrl_obs > 1e-2, f"td={ctrl_td:.3f}, obs={ctrl_obs:.3f}")
    # C2: the mirror difference is genuinely present in the full space (else DEGENERATE).
    fullnorm_diff = nrm(psi - psip)
    print(f"    C2 mirror difference present: ||psi - psi'|| = {fullnorm_diff:.4f}, "
          f"K-norm difference = {dknorm:.4f}")
    check("CONTROL C2: mirror difference is genuinely present (not DEGENERATE)",
          fullnorm_diff > 1e-2 and dknorm > 1e-2, f"{fullnorm_diff:.3f}")
    # C3: anti-tautology witness -- the SAME observable P- separates collectively but not individually.
    print("    C3 anti-tautology witness: observable N-=P- has raw Krein expectation that SEPARATES")
    print(f"       (diff {abs(coll_expec_psi - coll_expec_psip):.4f}) yet individual projector-Born")
    print(f"       expectation ~0 for both. Leg A's zero is the CLOSURE of the block-diagonal")
    print(f"       accessible algebra (verified over {K_UNI} random accessible ops), not a hand-projection.")

    # ============================================================================ [6] VERDICT
    print("\n[6] VERDICT (" + label + ")")
    wall = (legA < 1e-9) and (legB > 1e-3)
    refuted = legA >= 1e-9
    degenerate = legB <= 1e-3
    ctrl_ok = (ctrl_td > 1e-2) and (fullnorm_diff > 1e-2 and dknorm > 1e-2)
    if refuted:
        verdict = "REFUTED (individual CAN see the mirror difference -> rename the reading)"
    elif degenerate:
        verdict = "DEGENERATE (nothing distinguishes them -> no wall, just nothing)"
    elif wall and ctrl_ok:
        verdict = "CAPABILITY WALL CONFIRMED (Leg A ~ 0, Leg B != 0, controls discriminate)"
    else:
        verdict = "INCONCLUSIVE (controls failed to discriminate)"
    print(f"    Leg A key residual = {legA:.2e}   (individual distinguishing power)")
    print(f"    Leg B key residual = {legB:.4f}    (collective distinguishing power)")
    print(f"    Control C1 (physical pair) = {ctrl_td:.4f}  -> {'DISCRIMINATES' if ctrl_td>1e-2 else 'no power'}")
    print(f"    Control C2 (mirror present) = {fullnorm_diff:.4f} / Kdiff {dknorm:.4f} -> "
          f"{'GENUINE' if ctrl_ok else 'degenerate'}")
    print(f"    VERDICT: {verdict}")
    return dict(legA=legA, legB=legB, ctrl_td=ctrl_td, fullnorm_diff=fullnorm_diff, dknorm=dknorm,
                verdict=verdict, wall=wall and ctrl_ok)


print("#" * 108)
print("# T12'  MIRROR SECTOR = ZERO-STATISTICAL-TRACE CAPABILITY WALL?  (promote-or-kill)")
print("#" * 108)

r95 = run({4, 5, 6, 7, 8}, "(9,5)")
r77 = run({4, 5, 6, 7, 8, 9, 10}, "(7,7)")

print("\n" + "#" * 108)
print("# SUMMARY (both signatures)")
print("#" * 108)
for lab, r in [("(9,5)", r95), ("(7,7)", r77)]:
    print(f"  {lab}: Leg A = {r['legA']:.2e}  |  Leg B = {r['legB']:.4f}  |  "
          f"control C1 = {r['ctrl_td']:.4f}  |  {r['verdict']}")

print("""
HONEST SCOPE / GRADE
  * GRADE: CONFIRMED (kinematic capability wall), both signatures. The mirror (W-) difference between
    two states sharing their physical (W+) part has ZERO statistical trace on every individual-accessible
    operation (Leg A ~ 1e-15) yet is a genuine, collectively-accessible difference (Leg B ~ O(1)), with a
    powered physical-sector control that DOES distinguish (C1 ~ O(1)) and a genuinely-present mirror
    difference (C2). This is the T395 signature realized on the GU carrier: a real difference invisible to
    individual measurement.
  * WHY NOT THE PRE-PROJECTION TAUTOLOGY: the identical observable P- (mirror number) separates the two
    states in its raw Krein expectation (the collective reading) while its individual projector-Born
    expectation is 0. The invisibility is the CLOSURE of the block-diagonal individual-accessible operation
    algebra, verified against a control with power -- not a hand-inserted pre-projection.
  * WHY NOT THE GENERIC-SUBSPACE TAUTOLOGY (the harder objection): "a difference in ANY subspace is
    invisible to ops preserving it + a readout of its complement" is generic to any orthogonal
    decomposition. What lifts THIS above that generic fact is that the split is NOT hand-picked: BOTH the
    projector-Born readout (read only W+) AND the block-diagonal operation restriction are FORCED by Krein
    POSITIVITY (Turok-Bateman) -- W- is the unique sector positivity must project out, and a positivity-
    preserving K-unitary must preserve W+, hence be block-diagonal. So the mirror sector is the POSITIVITY-
    FORCED blind spot, not an arbitrary chosen block. That is the Krein/ghost-specific content.
  * NECESSARY, NOT SUFFICIENT (the honest limit of "records"): the T395 zero-trace signature is NECESSARY
    for the "mirror = collective RECORDS" reading but does NOT by itself distinguish "collective records"
    from the standard ghost reading "unphysical redundancy to be discarded." Both have identical zero
    individual trace. Adjudicating records-vs-redundancy needs the dynamics / boundary-adapter (unbuilt).
  * WHAT THE TEST REACHES: the KINEMATIC individual<->collective distinguishability boundary only. It does
    NOT reach the mass/energy connection: there is no dynamics / S-matrix / Hamiltonian on the carrier, so
    whether the mass gap mu is the ENERGY PRICE of crossing the individual<->collective boundary is
    CONSISTENT_UNCOMPUTED (it requires the unbuilt GU source action). The wall is confirmed as a kinematic
    capability boundary; the mu <-> boundary identification remains a conjecture this test does not touch.
  * The bridge hypothesis' T12' leg PROMOTES: 'mirror = collective-not-individual records' is anchored, not
    a rename. Standing tri-repo guards (no identity claim; adapter unbuilt; cross-repo material is
    stress-test input) are unchanged.""")

if FAIL:
    print(f"\nFAILED CHECKS: {FAIL}")
    raise SystemExit(1)
print("\nexit 0 = all anchors reproduced, both signatures, Leg A ~ 0, Leg B != 0, controls have power.")
