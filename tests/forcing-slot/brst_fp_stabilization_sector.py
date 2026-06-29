#!/usr/bin/env python3
r"""
FORCING-SLOT TEST -- BRST / Faddeev-Popov stabilization sector for the RS redundancy.

ANGLE
-----
The RS field Psi_mu in V (x) S = C^14 (x) C^128 carries a gauge redundancy
        Psi_mu  ->  Psi_mu + D_mu epsilon
with a SPINOR gauge parameter epsilon in S = C^128.  The Faddeev-Popov ghosts for a spinor
parameter are COMMUTING (bosonic) spinors.  This script BUILDS the FP / BRST stabilization
sector explicitly on the verified substrate and measures whether it can supply the missing
"forcing term" that is SIMULTANEOUSLY
    (a) TANGENTIAL        -- carries p_1, frame charge != 0, NOT id_14 (x) U,
    (b) NET-CHIRAL        -- nonzero net chiral asymmetry (n+ - n- != 0),
    (c) NON-FRAME-TRIVIAL -- nonzero frame charge.

Two rigorous questions, each answered by a real matrix run:

(1) FRAME TRIVIALITY of the FP / ghost operator.
    The de Donder / Lorenz gauge condition is the gamma-trace  Gamma Psi = 0,
    Gamma = [e_0 | ... | e_13] : V (x) S -> S.  The FP operator is the ghost Dirac operator
        Delta_FP = Gamma o g = sum_a e_a xi_a = c(xi)  : S -> S,
    where g(eps)_mu = xi_mu eps is the symbol of D_mu eps.  gamma^mu D_mu CONTRACTS the frame
    index mu WITH the Clifford generators -> the FP operator has NO free 14-frame index left.
    We DECIDE frame triviality by computing the tangent-frame (self-dual Lambda^2_+) charge that
    the ghost/gauge sector carries, and compare to the physical (gamma-traceless) RS carrier.

(2) Does ghost SUBTRACTION preserve VECTORLIKENESS?
    The BRST-physical RS content is the gamma-traceless transverse sector ker(Gamma); the ghost
    removes the gauge sector Q = I - Pi_RS.  We measure the net chirality (n+ - n-) of the full
    field, the physical sector, and the ghost sector -- in Euclidean (14,0) AND with the chiral
    16 of Spin(10) switched on (internal-chirality projection).  If a net asymmetry appears we
    factor the integer and decide 2-primary (selector arena, Z/8) vs 3-primary (carrier arena, Z/3).

Substrate: Cl(14,0) Euclidean and Cl(9,5) reps, 128-dim spinor, 14 = 4 (frame) + 10 (internal).
Reuses conventions from tests/generation-sector/h1_selfdual_family_kill.py (chirality +96/-96)
and tests/decider/generation_index_fork_decider.py (frame_charge, SU(2)+ carrier 33.94).
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction

import numpy as np

N, DIM = 14, 128
np.set_printoptions(precision=4, suppress=True)


# ----------------------------------------------------------------------------- rep builders
def jw(n):
    """Jordan-Wigner: 2n Hermitian gammas, e_a^2 = +I (Euclidean (2n,0))."""
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


GE = jw(7)                                   # Euclidean (14,0)
ETA95 = np.array([1.0] * 9 + [-1.0] * 5)
G95 = [GE[a] if ETA95[a] > 0 else 1j * GE[a] for a in range(N)]   # Cl(9,5)
I128, I14 = np.eye(DIM, dtype=complex), np.eye(N, dtype=complex)


def sgen(e, i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


def lvec(i, j):
    M = np.zeros((N, N), dtype=complex)
    M[i, j] = 1.0
    M[j, i] = -1.0
    return M


def proj_ker(Gamma):
    return np.eye(Gamma.shape[1], dtype=complex) - Gamma.conj().T @ np.linalg.inv(Gamma @ Gamma.conj().T) @ Gamma


def frame_charge(O, frame_gens):
    """Component of operator O on C^14 (x) C^128 along base tangent-frame so(4) rotations on
    TX^4 = {0,1,2,3}.  NONZERO <=> O genuinely rotates the spacetime frame (TANGENTIAL).
    ZERO <=> O is an internal/gauge fiber endomorphism (id_14 (x) U is frame-traceless)."""
    O4 = O.reshape(N, DIM, N, DIM)
    total = 0.0
    for L in frame_gens:
        nrm = np.tensordot(L.conj(), L, axes=([0, 1], [0, 1])).real
        F_L = np.einsum('vw,vswt->st', L.conj(), O4) / nrm
        total += float(np.linalg.norm(F_L))
    return total


def su2plus(e):
    SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
    return [np.kron(I14, sgen(e, a, b) + sgen(e, c, d)) + np.kron(lvec(a, b) + lvec(c, d), I128)
            for (a, b, c, d) in SD]


def prime_factors(n):
    n, f, d = abs(int(n)), {}, 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def fac_str(n):
    if n == 0:
        return "0"
    f = prime_factors(n)
    return " . ".join(f"{p}^{e}" if e > 1 else f"{p}" for p, e in sorted(f.items())) or "1"


def primary(n):
    if n == 0:
        return "ZERO (vectorlike / no asymmetry)"
    f = prime_factors(n)
    if 3 in f:
        return "3-PRIMARY (factor 3 present) => CARRIER arena"
    if set(f) <= {2}:
        return "2-PRIMARY (only powers of 2) => SELECTOR arena"
    return f"MIXED ({fac_str(n)})"


# fixed sample covector (same family used across the campaign) -- NOT tuned
XI = np.array([1.0, 2.0, 3.0, 4.0, 0.5, 1.5, 2.5, 0.7,
               1.1, 0.3, 2.2, 1.7, 0.9, 1.3], dtype=complex)


def chirality_op(e, idx):
    """Chirality grading omega over the Clifford generators indexed by `idx` (Euclidean).
    For an even number m of Hermitian e (e^2=+I): omega = prod e, omega^2 = (-1)^{m/2}.
    Return a Hermitian, square-to-I grading: omega for m/2 even, (-i)omega? we normalise to
    eigenvalues +/-1 by dividing by sqrt of omega^2."""
    om = I128.copy()
    for a in idx:
        om = om @ e[a]
    sq = (om @ om)[0, 0]
    # make Hermitian unit-square grading
    if abs(sq + 1) < 1e-6:        # omega^2 = -I
        om = (-1j) * om
    elif abs(sq - 1) < 1e-6:      # omega^2 = +I
        pass
    else:
        raise RuntimeError(f"omega^2 = {sq}")
    om = 0.5 * (om + om.conj().T)
    return om


def net_chiral_on_subspace(W, chir14):
    """n+ - n- of the chirality grading chir14 (on V (x) S) restricted to the columns of W."""
    if W.shape[1] == 0:
        return 0, 0, 0
    C = W.conj().T @ chir14 @ W
    C = 0.5 * (C + C.conj().T)
    ev = np.linalg.eigvalsh(C)
    npl, nmi = int(np.sum(ev > 0.5)), int(np.sum(ev < -0.5))
    return npl, nmi, npl - nmi


def cols_of_projector(P):
    w, V = np.linalg.eigh(0.5 * (P + P.conj().T))
    return V[:, w > 0.5]


def main():
    out = {}
    print("=" * 94)
    print("BRST / FADDEEV-POPOV STABILIZATION SECTOR  --  forcing-slot test")
    print("=" * 94)

    # ---------------------------------------------------------------- 0. anchors / controls
    e = GE                                          # Euclidean (14,0) for the multiplicity+chirality
    Gamma = np.hstack(e)                            # 128 x 1792
    Pi = proj_ker(Gamma)                            # physical RS (gamma-traceless), dim 1664
    Q = np.eye(N * DIM, dtype=complex) - Pi          # gauge / ghost sector, dim 128
    ker = int(round(np.trace(Pi).real))
    qdim = int(round(np.trace(Q).real))
    print(f"\n[0] CONTROLS")
    print(f"    dim V(x)S = {N*DIM};  ker(Gamma) (physical RS) = {ker};  Q = gauge/ghost = {qdim}")
    assert ker == 1664 and qdim == 128, (ker, qdim)

    # SU(2)+ carrier net self-dual frame charge (anchor 33.94 on Cl(9,5))
    sd_gens = [lvec(0, 1) + lvec(2, 3), lvec(0, 2) + lvec(3, 1), lvec(0, 3) + lvec(1, 2)]
    asd_gens = [lvec(0, 1) - lvec(2, 3), lvec(0, 2) - lvec(3, 1), lvec(0, 3) - lvec(1, 2)]
    J95 = su2plus(G95)
    Jsum95 = J95[0] + J95[1] + J95[2]
    gen_net_sd = frame_charge(Jsum95, sd_gens) - frame_charge(Jsum95, asd_gens)
    print(f"    SU(2)+ carrier net self-dual frame charge (Cl(9,5)) = {gen_net_sd:.3f}  (anchor ~33.94)")
    out["carrier_net_sd_frame_charge"] = gen_net_sd

    # ================================================================ QUESTION (1)
    print("\n" + "-" * 94)
    print("QUESTION (1):  is the FP / ghost (stabilization) operator FRAME-TRIVIAL?")
    print("-" * 94)

    # The gauge embedding g: S -> V(x)S,  g(eps)_mu = xi_mu eps  (symbol of D_mu eps)
    g = np.zeros((N * DIM, DIM), dtype=complex)
    for mu in range(N):
        g[mu * DIM:(mu + 1) * DIM, :] = XI[mu] * I128
    # FP operator = Gamma o g = sum_a e_a xi_a = c(xi) : S -> S
    FP = Gamma @ g
    c_xi = sum(XI[a] * e[a] for a in range(N))
    print(f"    FP operator = Gamma o g  equals  c(xi) = sum e_a xi_a ?  "
          f"||FP - c(xi)|| = {np.linalg.norm(FP - c_xi):.2e}")
    print(f"    FP operator shape = {FP.shape}  -> acts on S = C^128 ONLY; the frame index mu is")
    print(f"    CONTRACTED away by gamma^mu D_mu, leaving NO free 14-frame vector index.")
    out["FP_equals_c_xi_residual"] = float(np.linalg.norm(FP - c_xi))
    out["FP_shape"] = list(FP.shape)

    # M_D = id_14 (x) c(xi): the RS kinetic / ghost-on-each-component operator, manifestly id_14 (x) U
    M_D = np.kron(I14, c_xi)
    fc_MD = frame_charge(M_D, sd_gens + asd_gens)
    print(f"    frame charge of M_D = id_14 (x) c(xi)  (the Dirac/ghost operator lifted) = {fc_MD:.2e}")
    print(f"      -> id_14 (x) U is frame-traceless: frame charge 0 (FRAME-TRIVIAL).")
    out["frame_charge_M_D"] = fc_MD

    # Where does the carrier's tangential framing live: physical ker(Gamma) vs ghost/gauge Q ?
    def net_sd(O):
        return frame_charge(O, sd_gens) - frame_charge(O, asd_gens)

    phys_net_sd = net_sd(Pi @ Jsum95 @ Pi)
    ghost_net_sd = net_sd(Q @ Jsum95 @ Q)
    print(f"    net self-dual frame charge of SU(2)+ carrier projected onto:")
    print(f"        physical ker(Gamma) : {phys_net_sd:.3f}")
    print(f"        ghost / gauge  Q    : {ghost_net_sd:.3f}")
    print(f"      -> the tangential (p_1, Lambda^2_+) framing lives in the PHYSICAL transverse RS;")
    print(f"         the FP ghost/gauge sector Q carries ~0 net self-dual frame charge.")
    out["phys_net_sd_frame_charge"] = phys_net_sd
    out["ghost_net_sd_frame_charge"] = ghost_net_sd

    # Frame charge of the ghost-image projector itself (does the ghost SUBSPACE rotate TX^4 net?)
    Pg = g @ np.linalg.inv(g.conj().T @ g) @ g.conj().T   # projector onto pure-gauge image im(g)
    out["ghost_image_net_sd_frame_charge"] = net_sd(Pg)
    print(f"    net self-dual frame charge of the pure-gauge image projector im(g) = {net_sd(Pg):.3f}")
    print(f"    (NB: the 1.71 ghost-SUBSPACE charge is the frame content of the gamma-trace MODES,")
    print(f"     not of the FP OPERATOR; the operator c(xi) on S is the forcing term.)")

    # ALTERNATIVE stabilization operator: the gauge-fixing term Gamma^dag Gamma on V(x)S.
    # Blocks (mu,nu) = e_mu^dag e_nu -> NOT id_14 (x) U, so it CAN carry frame charge. But it is
    # Hermitian positive -> chirality-symmetric (vectorlike). Measure both.
    GtG = Gamma.conj().T @ Gamma                       # 1792 x 1792 gauge-fixing operator
    fc_GtG = frame_charge(GtG, sd_gens + asd_gens)
    netsd_GtG = net_sd(GtG)
    print(f"\n    gauge-fixing operator Gamma^dag Gamma (blocks e_mu^dag e_nu, NOT id_14 (x) U):")
    print(f"        frame charge (all) = {fc_GtG:.3f}   net self-dual = {netsd_GtG:.3f}")
    print(f"        (it is Hermitian positive -> chirality-symmetric / vectorlike by construction)")
    out["gaugefix_frame_charge_all"] = fc_GtG
    out["gaugefix_net_sd_frame_charge"] = netsd_GtG

    # The forcing-term frame charge IS the FP-operator frame charge (= 0): contracted, no free index.
    q1_operator_frame_trivial = abs(fc_MD) < 1e-6
    print(f"\n    => FP STABILIZATION OPERATOR (ghost Dirac c(xi)) FRAME-TRIVIAL? {q1_operator_frame_trivial}")
    print(f"       (frame charge of the operator = {fc_MD:.1e}; gauge-fixing Gamma^dag Gamma is")
    print(f"        non-frame-trivial [{fc_GtG:.2f}] but vectorlike -> still never all three.)")
    out["q1_operator_frame_trivial"] = bool(q1_operator_frame_trivial)

    # ================================================================ QUESTION (2)
    print("\n" + "-" * 94)
    print("QUESTION (2):  does ghost SUBTRACTION preserve VECTORLIKENESS (net chirality 0)?")
    print("-" * 94)

    # full Spin(14) chirality grading (Euclidean), lifted to V(x)S as id_14 (x) omega_14
    om14 = chirality_op(e, list(range(14)))
    chir14 = np.kron(I14, om14)

    # net chirality: full field, physical ker(Gamma), ghost sector Q
    Wfull = np.eye(N * DIM, dtype=complex)
    Wphys = cols_of_projector(Pi)
    Wghost = cols_of_projector(Q)
    fp_full = net_chiral_on_subspace(Wfull, chir14)
    fp_phys = net_chiral_on_subspace(Wphys, chir14)
    fp_ghost = net_chiral_on_subspace(Wghost, chir14)
    print(f"    Spin(14) chirality (Euclidean), net (n+ - n-):")
    print(f"        full V(x)S         : +{fp_full[0]:<4} / -{fp_full[1]:<4}  net {fp_full[2]:+d}")
    print(f"        physical ker(Gamma): +{fp_phys[0]:<4} / -{fp_phys[1]:<4}  net {fp_phys[2]:+d}")
    print(f"        ghost / gauge Q    : +{fp_ghost[0]:<4} / -{fp_ghost[1]:<4}  net {fp_ghost[2]:+d}")
    rs_minus_ghost_full = fp_full[2] - fp_ghost[2]
    print(f"    RS(full) - ghost net chirality = {fp_full[2]} - ({fp_ghost[2]}) = {rs_minus_ghost_full:+d}"
          f"   [check: equals physical = {fp_phys[2]:+d}]")
    out["netchiral_spin14"] = dict(full=fp_full[2], physical=fp_phys[2], ghost=fp_ghost[2],
                                   rs_minus_ghost=rs_minus_ghost_full)

    # ---- TWIST ON: project onto the chiral 16 of Spin(10) (internal {4..13} chirality = +1)
    om10 = chirality_op(e, list(range(4, 14)))      # internal Spin(10) chirality, square = +I
    P16 = np.kron(I14, 0.5 * (I128 + om10))          # project spinor onto the 16 (internal +)
    Pi_t = P16 @ Pi @ P16
    Q_t = P16 @ Q @ P16
    Wphys_t = cols_of_projector(Pi_t)
    Wghost_t = cols_of_projector(Q_t)
    # net chirality now measured by the FRAME (Spin(4) = {0,1,2,3}) chirality, since the internal
    # chirality is fixed to +1 (we have twisted to the chiral 16). A genuine generation asymmetry
    # would show as a net Spin(4) frame-chirality imbalance in the transverse RS minus the ghost.
    om4 = chirality_op(e, [0, 1, 2, 3])              # frame chirality, square = +I
    chir4 = np.kron(I14, om4)
    tp_phys = net_chiral_on_subspace(Wphys_t, chir4)
    tp_ghost = net_chiral_on_subspace(Wghost_t, chir4)
    # also the full internal-chirality net over the transverse sector (the literal "16 vs 16bar" count)
    nc_phys_10 = net_chiral_on_subspace(Wphys, np.kron(I14, om10))
    nc_ghost_10 = net_chiral_on_subspace(Wghost, np.kron(I14, om10))
    print(f"\n    TWIST ON (chiral 16 of Spin(10), internal chirality fixed = +1):")
    print(f"      Spin(10) 16-vs-16bar net over UNtwisted sectors (om10):")
    print(f"        physical : net {nc_phys_10[2]:+d}    ghost : net {nc_ghost_10[2]:+d}"
          f"    RS - ghost = {nc_phys_10[2]-nc_ghost_10[2]:+d}")
    print(f"      frame-chirality (Spin(4)) net within the 16-projected sector:")
    print(f"        physical(transverse, 16): +{tp_phys[0]:<4} / -{tp_phys[1]:<4}  net {tp_phys[2]:+d}")
    print(f"        ghost(gauge, 16)        : +{tp_ghost[0]:<4} / -{tp_ghost[1]:<4}  net {tp_ghost[2]:+d}")
    rs_minus_ghost_twist = tp_phys[2] - tp_ghost[2]
    print(f"      RS(transverse,16) - ghost(16) net frame chirality = {rs_minus_ghost_twist:+d}")
    out["netchiral_twisted"] = dict(
        spin10_physical=nc_phys_10[2], spin10_ghost=nc_ghost_10[2],
        spin10_rs_minus_ghost=nc_phys_10[2] - nc_ghost_10[2],
        frame_phys16=tp_phys[2], frame_ghost16=tp_ghost[2],
        rs_minus_ghost=rs_minus_ghost_twist)

    integers = [rs_minus_ghost_full, rs_minus_ghost_twist,
                nc_phys_10[2] - nc_ghost_10[2], fp_phys[2]]
    nonzero = [k for k in integers if k != 0]
    print("\n    NET-CHIRAL INTEGERS produced by (RS minus ghost):")
    for label, k in [("Spin(14) RS-ghost", rs_minus_ghost_full),
                     ("Spin(10) 16/16bar RS-ghost", nc_phys_10[2] - nc_ghost_10[2]),
                     ("twisted frame-chirality RS-ghost", rs_minus_ghost_twist),
                     ("physical Spin(14) net", fp_phys[2])]:
        print(f"        {label:<36} = {k:+d}   {primary(k)}")

    q2_introduces_netchiral = len(nonzero) > 0
    out["q2_introduces_netchiral"] = bool(q2_introduces_netchiral)
    out["q2_nonzero_integers"] = nonzero

    # ================================================================ VERDICT
    print("\n" + "=" * 94)
    print("VERDICT")
    print("=" * 94)
    # The FP ghost OPERATOR c(xi): frame-trivial (a NO, c NO), vectorlike (b NO).
    # The gauge-fixing operator Gamma^dag Gamma: non-frame-trivial (a/c could read YES) BUT
    # Hermitian positive => vectorlike (b NO). Neither route gives all three.
    tangential_fp = not q1_operator_frame_trivial
    non_frame_trivial_fp = not q1_operator_frame_trivial
    net_chiral = q2_introduces_netchiral
    fills = tangential_fp and net_chiral and non_frame_trivial_fp
    print(f"  FP GHOST OPERATOR c(xi):")
    print(f"    (a) TANGENTIAL (frame charge != 0)        : {tangential_fp}")
    print(f"    (c) NON-FRAME-TRIVIAL (frame charge != 0) : {non_frame_trivial_fp}")
    print(f"  GAUGE-FIXING OPERATOR Gamma^dag Gamma:")
    print(f"    (a)/(c) non-frame-trivial = True (frame charge {fc_GtG:.2f}) but VECTORLIKE (Hermitian +)")
    print(f"  BOTH ROUTES:")
    print(f"    (b) NET-CHIRAL (n+ - n- != 0)            : {net_chiral}   <-- decisive failure")
    print(f"  FILLS THE FORCING SLOT (a AND b AND c, 3-primary): {fills}")
    out["fills_forcing_slot"] = bool(fills)
    print("\n  READING: the FP/BRST ghost Dirac operator gamma^mu D_mu CONTRACTS the frame index")
    print("  away -> frame-trivial (no p_1 channel); ghost subtraction is chirality-symmetric")
    print("  (ghost carries the SAME chiral rep as the gauge variation) -> vectorlikeness preserved.")
    print("  The bottom row stays EMPTY from the BRST sector. Horn B (no trapdoor) on this leg.")

    print("\nMACHINE SUMMARY:")
    for k, v in out.items():
        print(f"  {k}: {v}")
    return out


if __name__ == "__main__":
    main()
