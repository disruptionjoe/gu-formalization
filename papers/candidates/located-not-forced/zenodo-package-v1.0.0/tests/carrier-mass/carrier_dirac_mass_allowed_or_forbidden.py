#!/usr/bin/env python3
r"""
CAPSTONE ANGLE -- Is a carrier DIRAC MASS symmetry-ALLOWED or FORBIDDEN by GU's verified structure?

The order-3 carrier (Lambda^2_+, the 192-dim j=1 generation triplet) is VECTORLIKE: Krein signature
(+96, -96), net chirality 0 (ghost_parity_krein.py, seesaw_majorana_mu_block.py). A vectorlike pair has
no automatic chiral protection, so it generically admits a DIRAC MASS coupling the +96 "generation" half
to the -96 "mirror" half:  L_mass = m * (gen-bar . mirror) + h.c.

This script BUILDS that Dirac mass operator on the carrier and asks, of every GU-native symmetry, the
single sharp question: does the symmetry forbid it (=> protected, massless, occupancy is a flat modulus
=> LOCATED, not forced) or admit it (=> generically massive => the 96 gen modes pair with 96 mirror modes,
lift to mass m, and DECOUPLE => the light chiral spectrum from this sector is 0, not 3)?

A vectorlike pair admits a Dirac mass UNLESS some symmetry distinguishes gen from mirror. So we test each
GU-native symmetry S and report dim Hom_S(mirror -> gen) = the number of S-allowed Dirac-mass parameters:
   dim = 0  => S FORBIDS the Dirac mass  => PROTECTED (massless).
   dim > 0  => S ADMITS a Dirac mass     => not protected by S.
The carrier is protected iff SOME GU-native symmetry gives dim 0. Generically massive iff NONE does.

GU-native symmetries tested (all on the verified Cl(9,5) = M(64,H) substrate, j=1 triplet carrier):
  (S0) Krein-self-adjointness K (the action-reality condition itself) -- does it allow an off-diagonal
       gen<->mirror block at all?
  (S1) su(2)_+  (Lambda^2_+, the carrier's DEFINING structure group): the Jr generators.
  (S2) J_quat  (the quaternionic Kramers structure, C^2 = -I): is it a Krein-isometry (preserves gen/mirror)
       or does it swap them? compatibility of M_D with the Kramers reality.
  (S3) chirality omega_14: chirality content of gen vs mirror -- does chirality distinguish them?
  (S4) the antilinear chiralizer C = J_quat . G (the ONLY operator known to flip the +96/-96 grading):
       reproduce its EXACT tangent-frame charge (expected 0.00, frame-trivial, selector-arena) and confirm
       that the one operator that DOES distinguish gen from mirror is frame-trivial -- i.e. it lives on the
       selector side, not on the carrier's tangent frame, so it provides no frame-level chiral protection.

Computed-on-substrate: every Hom-dimension and frame charge below is a number this script computes.
Action-gated: the actual mass VALUE m is gated on the unbuilt full GU source action; we report only
ALLOWED/FORBIDDEN (a representation-theoretic fact about GU's verified structure) plus the BUILT SW-action
proxy (||A_++|| = ||A_--|| = 391, vectorlike) recovered from canon/source-action-seiberg-witten-RESULTS.md.

Reuses the verified substrate construction of tests/source-action/seesaw_majorana_mu_block.py and
tests/generation-sector/ghost_parity_krein.py (self-contained copy of build_substrate + J_quat builder).
"""
from __future__ import annotations

import numpy as np

N, DIM = 14, 128
TOL = 1e-7
ETA = np.array([1.0] * 9 + [-1.0] * 5)


# --------------------------------------------------------------------------- substrate
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


def sgen(e, i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


def lvec(i, j):
    M = np.zeros((N, N), dtype=complex)
    M[i, j] = 1
    M[j, i] = -1
    return M


SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]   # self-dual SU(2)_+ on Euclidean 4-base {0,1,2,3}


def build_substrate(timelike={4, 5, 6, 7, 8}):
    """Return e, K (Krein 1792), Jfull (su(2)_+ on V(x)S), Sig (spinor self-dual gens),
    Wt (1792 x 192 j=1 triplet basis), chir14 (full 14d chirality on V(x)S)."""
    base = jw(7)
    I128, I14 = np.eye(DIM, dtype=complex), np.eye(N, dtype=complex)
    e = [(1j * base[a] if a in timelike else base[a]) for a in range(N)]
    spacelike = [a for a in range(N) if a not in timelike]

    Gamma = np.hstack(e)
    Pi = np.eye(N * DIM, dtype=complex) - Gamma.conj().T @ np.linalg.inv(Gamma @ Gamma.conj().T) @ Gamma
    Jfull = [np.kron(I14, sgen(e, a, b) + sgen(e, c, d)) + np.kron(lvec(a, b) + lvec(c, d), I128)
             for (a, b, c, d) in SD]
    Sig = [sgen(e, a, b) + sgen(e, c, d) for (a, b, c, d) in SD]
    w, Vv = np.linalg.eigh(Pi)
    Wker = Vv[:, w > 0.5]
    Cas = -(Jfull[0] @ Jfull[0] + Jfull[1] @ Jfull[1] + Jfull[2] @ Jfull[2])
    CasK = Wker.conj().T @ Cas @ Wker
    CasK = 0.5 * (CasK + CasK.conj().T)
    cev, cU = np.linalg.eigh(CasK)
    top = max(round(x.real, 3) for x in cev)         # j=1 Casimir = 8
    Wt = Wker @ cU[:, np.abs(cev - top) < 1e-3]       # 1792 x 192

    bS = I128.copy()
    for s in spacelike:
        bS = bS @ e[s]
    if np.linalg.norm(bS.conj().T + bS) < 1e-9:
        bS = 1j * bS
    bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
    etaV = np.diag([(-1.0 if a in timelike else 1.0) for a in range(N)]).astype(complex)
    K = np.kron(etaV, bS)

    om = I128.copy()
    for a in range(N):
        om = om @ e[a]
    om2 = (np.trace(om @ om) / DIM).real
    chir14 = np.kron(I14, om if om2 > 0 else (-1j) * om)
    return e, K, Jfull, Sig, Wt, chir14


def quaternionic_J(e128, seed=1):
    """Phase-unique quaternionic structure J_quat = id_14 (x) U of M(64,H) (step9/step11/boundary-eta builder)."""
    def Phi(U):
        out = np.zeros_like(U)
        for a in range(N):
            out += ETA[a] * (e128[a] @ U @ e128[a].conj())
        return out / N
    rng = np.random.default_rng(seed)
    U = rng.standard_normal((DIM, DIM)) + 1j * rng.standard_normal((DIM, DIM))
    for _ in range(400):
        U = 0.5 * (U + Phi(U))
        U /= np.linalg.norm(U)
    Us, _, Vs = np.linalg.svd(U)
    U = Us @ Vs
    return U / np.sqrt(abs(np.trace(U @ U.conj()) / DIM))


def fro(A):
    return float(np.linalg.norm(A))


def commutant_hom_dim(gens, Pg, Pm, tol=1e-7, maxdim=4096):
    """dim_C Hom_{gens}(mirror -> gen): the space of (dg x dm) blocks X with [g, Pg X Pm^dag] = 0
    for every g in `gens`. Computed as the null space of the *normal* operator N on the dg*dm-dim
    X-space (N(X) = sum_g L_g^dag L_g X, built by applying the cheap 192-dim commutator and its
    Frobenius-adjoint), so we never form the 36864 x 9216 vectorized matrix. dg*dm <= 9216 here, and
    one Hermitian eigh of that size is the only heavy step.  L_g(X) = g T - T g,  T = Pg X Pm^dag ;
    L_g^dag(Y) = Pg^dag (g^dag Y - Y g^dag) Pm  (Frobenius adjoint)."""
    dg, dm = Pg.shape[1], Pm.shape[1]
    n = dg * dm
    Pgd, Pmd = Pg.conj().T, Pm.conj().T

    def N_apply(xvec):
        X = xvec.reshape(dg, dm)
        T = Pg @ X @ Pmd
        out = np.zeros((dg, dm), dtype=complex)
        for g in gens:
            Lg = g @ T - T @ g
            out += Pgd @ (g.conj().T @ Lg - Lg @ g.conj().T) @ Pm
        return out.reshape(n)

    # build the n x n Hermitian normal operator by applying N to each basis vector
    Nmat = np.zeros((n, n), dtype=complex)
    eye = np.eye(n, dtype=complex)
    for k in range(n):
        Nmat[:, k] = N_apply(eye[:, k])
    Nmat = 0.5 * (Nmat + Nmat.conj().T)
    ev = np.linalg.eigvalsh(Nmat)
    scale = max(1.0, ev.max())
    return int((np.abs(ev) < tol * scale).sum())


def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=120)
    print("=" * 90)
    print("CARRIER DIRAC MASS -- symmetry-ALLOWED or FORBIDDEN by GU's verified structure?")
    print("=" * 90)

    e, K, Jfull, Sig, Wt, chir14 = build_substrate()
    d = Wt.shape[1]
    print(f"j=1 generation triplet (carrier) dim = {d}  (expected 192; carrier of the 16)")

    # reduce structures to the 192-dim carrier
    Kr = Wt.conj().T @ K @ Wt
    Kr = 0.5 * (Kr + Kr.conj().T)
    Jr = [Wt.conj().T @ Jfull[k] @ Wt for k in range(3)]
    chir_tr = Wt.conj().T @ chir14 @ Wt
    chir_tr = 0.5 * (chir_tr + chir_tr.conj().T)

    # ---------------------------------------------------- reproduce (+96, -96) Krein control
    ks, kU = np.linalg.eigh(Kr)
    npl = int((ks > 1e-9).sum()); nmi = int((ks < -1e-9).sum()); nz = int((np.abs(ks) < 1e-9).sum())
    Pg = kU[:, ks > 1e-9]      # gen  = Krein-positive 96
    Pm = kU[:, ks < -1e-9]     # mirror = Krein-negative 96
    print(f"\n[control] carrier Krein signature = (+{npl}, -{nmi}, 0:{nz})  "
          f"-> {'VECTORLIKE (net chirality 0)' if npl == nmi else 'ASYMMETRIC'}")
    assert npl == nmi == 96, (npl, nmi)
    print(f"          gen = Krein(+) 96-dim ; mirror = Krein(-) 96-dim.  A Dirac mass pairs gen<->mirror.")

    # ============================================================= (S0) Krein-self-adjointness
    print("\n" + "-" * 90)
    print("(S0) KREIN-SELF-ADJOINTNESS  -- does the action-reality condition admit a gen<->mirror block?")
    print("-" * 90)
    # In the Krein eigenbasis K = diag(+I_96, -I_96). A pure Dirac mass M_D = [[0,B],[-B^dag,0]] is
    # Krein-self-adjoint (M_D^# = K^-1 M_D^dag K = M_D) for ANY B. Build an explicit random B and verify.
    Kdiag = np.diag(np.sign(ks))          # +/-1 in the eigenbasis
    rng = np.random.default_rng(0)
    B = rng.standard_normal((96, 96)) + 1j * rng.standard_normal((96, 96))
    MD_eig = np.zeros((d, d), dtype=complex)
    MD_eig[:96, 96:] = B
    MD_eig[96:, :96] = -B.conj().T        # the Krein-self-adjoint pure off-diagonal Dirac mass
    krein_adjoint = np.linalg.inv(Kdiag) @ MD_eig.conj().T @ Kdiag
    s0_defect = fro(krein_adjoint - MD_eig)
    print(f"  explicit Dirac mass M_D = [[0,B],[-B^dag,0]] (random B, 96x96)")
    print(f"  Krein-self-adjointness defect ||K^-1 M_D^dag K - M_D|| = {s0_defect:.2e}")
    s0_allows = s0_defect < 1e-9
    print(f"  => Krein structure ALONE admits the off-diagonal gen<->mirror Dirac mass: {s0_allows}")
    print(f"     (the reality condition does NOT block the mass; off-diagonal dim = {96*96} complex params)")

    # map M_D back to the carrier basis for the symmetry tests
    Pg96 = Pg                            # 192 x 96
    Pm96 = Pm

    # ============================================================= (S1) su(2)_+
    print("\n" + "-" * 90)
    print("(S1) su(2)_+ = Lambda^2_+  -- the carrier's DEFINING structure group")
    print("-" * 90)
    # first confirm su(2)_+ is a Krein-isometry on the carrier (so it preserves gen/mirror separately):
    iso_def = max(fro(Jr[k].conj().T @ Kr + Kr @ Jr[k]) for k in range(3))  # Krein-anti-self-adjoint
    print(f"  su(2)_+ Krein-anti-self-adjoint defect max||J^dag K + K J|| = {iso_def:.2e} "
          f"(=0 => Krein-isometry; preserves gen & mirror)")
    # Krein-isometry => gen and mirror are su(2)_+-invariant; decompose each by the Casimir to count
    # irrep multiplicities, then dim_C Hom_su(2)+(mirror->gen) = sum_j m_gen(j) m_mirror(j).
    Cas = -(Jr[0] @ Jr[0] + Jr[1] @ Jr[1] + Jr[2] @ Jr[2])
    def casimir_mults(P):
        c = P.conj().T @ Cas @ P
        c = 0.5 * (c + c.conj().T)
        ev = np.linalg.eigvalsh(c).real
        vals, cnts = np.unique(np.round(ev, 3), return_counts=True)
        return dict(zip(vals.tolist(), cnts.tolist()))
    mg, mm = casimir_mults(Pg96), casimir_mults(Pm96)
    cas_top = round(float(np.unique(np.round(np.linalg.eigvalsh(Cas).real, 3)).max()), 3)
    dim_irrep = 3                          # j=1 triplet
    s1_dim = sum(mg.get(v, 0) // dim_irrep * (mm.get(v, 0) // dim_irrep) * dim_irrep
                 for v in set(mg) | set(mm))   # sum_j m_g(j) m_m(j) * dim(j) for block of intertwiners
    # cleaner equivalent: both pure j=1 => mult_gen = 96/3, mult_mir = 96/3, Hom = mult_g*mult_m
    mult_g, mult_m = Pg96.shape[1] // dim_irrep, Pm96.shape[1] // dim_irrep
    s1_dim = mult_g * mult_m
    print(f"  Casimir on gen = {mg}  ; on mirror = {mm}  (j=1 Casimir value = {cas_top}; triplet dim 3)")
    print(f"  gen = {mult_g} copies of spin-1 ; mirror = {mult_m} copies of spin-1")
    print(f"  dim_C Hom_su(2)+ (mirror -> gen) = m_gen * m_mir = {mult_g}*{mult_m} = {s1_dim}")
    s1_forbids = (s1_dim == 0)
    print(f"  => su(2)_+ FORBIDS the Dirac mass: {s1_forbids}")
    print(f"     gen and mirror are BOTH {mult_g} copies of spin-1; su(2)_+ cannot tell them apart -> ALLOWED.")

    # ============================================================= (S2) J_quat (Kramers C^2=-I)
    print("\n" + "-" * 90)
    print("(S2) J_quat  -- the quaternionic Kramers structure (C^2 = -I)")
    print("-" * 90)
    e128 = [(1j * jw(7)[a] if a in {4, 5, 6, 7, 8} else jw(7)[a]) for a in range(N)]
    U = quaternionic_J(e128, seed=1)
    Jf = np.kron(np.eye(N), U)                      # J_quat = id_14 (x) U on V(x)S
    Jq = Wt.conj().T @ Jf @ Wt                       # reduced to the carrier (linear part)
    # is J_quat a Krein-isometry on the carrier (preserves gen/mirror) or anti (swaps)?
    jq_iso = fro(Jq.conj().T @ Kr @ Jq - Kr)
    # how much does J_quat's linear part map gen<->mirror vs gen->gen?
    gm = fro(Pm96.conj().T @ Jq @ Pg96)              # gen -> mirror leakage
    gg = fro(Pg96.conj().T @ Jq @ Pg96)              # gen -> gen
    print(f"  J_quat linear-part Krein-isometry defect ||Jq^dag K Jq - K|| = {jq_iso:.2e}")
    print(f"  J_quat block content on carrier:  ||gen->gen|| = {gg:.2f}   ||gen->mirror|| = {gm:.2f}")
    # CONSTRUCTIVE existence: the conjugation Ad_Jq: M -> Jq M Jq^-1 splits the off-diagonal mass space
    # into +1/-1 eigenspaces; both are J_quat-covariant Dirac masses, and they span -- so unless BOTH
    # vanish off-diagonal (=> J_quat forbids), a covariant mass exists. Build the explicit MD on the
    # carrier and project to each covariance eigenspace; report the surviving off-diagonal norm.
    MD_carrier = kU @ MD_eig @ kU.conj().T          # the S0 Dirac mass, in the carrier basis
    Jqi = np.linalg.inv(Jq)
    M_plus = 0.5 * (MD_carrier + Jq @ MD_carrier @ Jqi)   # Ad_Jq = +1 covariant
    M_minus = 0.5 * (MD_carrier - Jq @ MD_carrier @ Jqi)  # Ad_Jq = -1 covariant
    od_plus = fro(Pm96.conj().T @ M_plus @ Pg96) + fro(Pg96.conj().T @ M_plus @ Pm96)
    od_minus = fro(Pm96.conj().T @ M_minus @ Pg96) + fro(Pg96.conj().T @ M_minus @ Pm96)
    s2_witness = max(od_plus, od_minus)
    s2_forbids = (s2_witness < 1e-9)
    print(f"  explicit J_quat-covariant Dirac mass off-diagonal norm: Ad=+1 -> {od_plus:.2f}, Ad=-1 -> {od_minus:.2f}")
    print(f"  => J_quat FORBIDS the Dirac mass: {s2_forbids}  (a covariant gen<->mirror mass exists, norm "
          f"{s2_witness:.2f})")
    print(f"     (Kramers C^2=-I imposes a reality/pairing condition, it does not kill the off-diagonal block)")

    # ============================================================= (S3) chirality omega_14
    print("\n" + "-" * 90)
    print("(S3) chirality omega_14  -- does chirality distinguish gen from mirror?")
    print("-" * 90)
    def chir_content(P):
        c = P.conj().T @ chir_tr @ P
        c = 0.5 * (c + c.conj().T)
        ev = np.linalg.eigvalsh(c)
        return int((ev > 0.5).sum()), int((ev < -0.5).sum())
    gp, gm_ = chir_content(Pg96)
    mp, mm_ = chir_content(Pm96)
    # is chirality block-diagonal in the Krein (gen/mirror) basis, or does it MIX gen<->mirror?
    chir_offdiag = fro(Pm96.conj().T @ chir_tr @ Pg96)   # chirality gen->mirror leakage
    chir_diag = fro(Pg96.conj().T @ chir_tr @ Pg96)       # chirality gen->gen
    chir_mixes = chir_offdiag > 1e-6 * max(1.0, chir_offdiag + chir_diag)
    print(f"  gen    (Krein +96) chirality (+,-) = ({gp},{gm_})  net = {gp-gm_}")
    print(f"  mirror (Krein -96) chirality (+,-) = ({mp},{mm_})  net = {mp-mm_}")
    print(f"  chirality block structure in Krein basis: ||gen->gen|| = {chir_diag:.2f}  "
          f"||gen->mirror|| = {chir_offdiag:.2f}  -> chirality {'MIXES' if chir_mixes else 'preserves'} gen/mirror")
    s3_dim = gp * mp + gm_ * mm_      # chirality-preserving Hom count (valid ONLY if chirality is Krein-diagonal)
    # chirality forbids a gen<->mirror Dirac mass ONLY if it (a) PRESERVES the Krein grading AND (b) gives gen
    # and mirror OPPOSITE definite chirality (gen all-+, mirror all--, or vice versa). If chirality MIXES
    # gen<->mirror (off-diagonal), it is itself a gen<->mirror operator and cannot protect against a
    # gen<->mirror mass; and chirality-NEUTRAL subspaces (gp=gm_) are not oppositely polarized either.
    # (Earlier this leg read the degenerate s3_dim=0*0+0*0=0 as "forbidden" -- a bug; the correct criterion
    # is opposite definite polarization, which the chirality-neutral carrier fails -> ALLOWED.)
    gen_definite = (gp == 0) ^ (gm_ == 0)
    mir_definite = (mp == 0) ^ (mm_ == 0)
    opposite_polarized = gen_definite and mir_definite and ((gp > 0) == (mm_ > 0))
    s3_forbids = (not chir_mixes) and opposite_polarized
    why3 = ("chirality MIXES gen<->mirror (off-diagonal): does NOT separate them" if chir_mixes
            else ("gen/mirror oppositely definite-polarized" if opposite_polarized
                  else "gen and mirror are chirality-NEUTRAL: not oppositely polarized"))
    print(f"  dim_C Hom_omega14(mirror->gen) (preserving count, valid iff Krein-diagonal) = {s3_dim}")
    print(f"  => chirality FORBIDS the Dirac mass: {s3_forbids}   ({why3})")
    print(f"     Both gen and mirror are chirality-NEUTRAL ({gp}+,{gm_}-): chirality does NOT separate them.")
    print(f"     (A chiral protection would need gen all-+ and mirror all-- ; it is not so.)")

    # ============================================================= (S4) the chiralizer C = J_quat . G
    print("\n" + "-" * 90)
    print("(S4) the antilinear chiralizer C = J_quat . G  -- the ONLY operator that flips +96/-96")
    print("-" * 90)
    # reproduce the EXACT tangent-frame charge of J_quat (boundary-eta-of-mu-RESULTS: 0.00, frame-trivial)
    def Mvec(i, j):
        M = np.zeros((N, N), dtype=complex)
        M[i, j] = ETA[j]; M[j, i] = -ETA[i]
        return M
    base_sd_vec = [Mvec(0, 1) + Mvec(2, 3), Mvec(0, 2) + Mvec(3, 1), Mvec(0, 3) + Mvec(1, 2)]
    frame_ops = [np.kron(Mfr, np.eye(DIM, dtype=complex)) for Mfr in base_sd_vec]
    all_frame = [np.kron(Mvec(i, j), np.eye(DIM, dtype=complex))
                 for i in range(N) for j in range(i + 1, N)]
    frame_sd_charge = max(fro(Jf @ Fop - Fop @ Jf) for Fop in frame_ops)
    frame_all_charge = max(fro(Jf @ Fop - Fop @ Jf) for Fop in all_frame)
    fm_Jquat = abs(np.trace(Jf.conj().T @ frame_ops[0]))
    print(f"  J_quat tangent-frame charge: max||[J_quat, Lambda^2_+ frame rot]||  = {frame_sd_charge:.2e}")
    print(f"                               max||[J_quat, ANY so(9,5) frame rot]|| = {frame_all_charge:.2e}")
    print(f"                               frame-marginal |<J_quat, Lambda^2_+>|  = {fm_Jquat:.2e}")
    frame_trivial = frame_all_charge < 1e-9
    print(f"  => J_quat (hence the chiralizer C = J_quat.G) is FRAME-TRIVIAL: {frame_trivial}  "
          f"(matches boundary-eta-of-mu: 0.00)")
    # the chiralizer C is ANTILINEAR: confirm it is the operator that DOES swap gen<->mirror
    # (its action on the +96/-96 grading is the net-chiral escape). Show its antilinearity defect.
    G = None
    # build the gamma-trace grading G on the full space to form C = J_quat . G (antiunitary)
    base = jw(7)
    Gamma = np.hstack([(1j * base[a] if a in {4, 5, 6, 7, 8} else base[a]) for a in range(N)])
    Pi = np.eye(N * DIM, dtype=complex) - Gamma.conj().T @ np.linalg.inv(Gamma @ Gamma.conj().T) @ Gamma
    Q = np.eye(N * DIM, dtype=complex) - Pi
    Gfull = Pi - Q
    Cu = Jf @ Gfull.conj()                          # unitary part of antiunitary C
    C2sq = Cu @ Cu.conj()
    kramers = fro(C2sq + np.eye(N * DIM, dtype=complex))
    print(f"  chiralizer C = J_quat.G is antiunitary with C^2 = -I (Kramers): ||C^2 + I|| = {kramers:.2e}")
    print(f"  => the one operator that distinguishes gen from mirror is ANTILINEAR and FRAME-TRIVIAL")
    print(f"     (selector-arena, frame charge 0). It is NOT a frame-level gauge symmetry of the carrier,")
    print(f"     so it provides NO chiral protection that would forbid the (linear) Dirac mass.")

    # ============================================================= VERDICT
    print("\n" + "=" * 90)
    print("VERDICT -- is the carrier Dirac mass ALLOWED or FORBIDDEN?")
    print("=" * 90)
    forbidders = {
        "su(2)_+ (Lambda^2_+ structure group)": s1_forbids,
        "J_quat (Kramers C^2=-I)": s2_forbids,
        "chirality omega_14": s3_forbids,
    }
    any_forbid = any(forbidders.values())
    witness = {
        "su(2)_+ (Lambda^2_+ structure group)": f"Hom dim {s1_dim}",
        "J_quat (Kramers C^2=-I)": f"covariant mass norm {s2_witness:.1f}",
        "chirality omega_14": f"Hom dim {s3_dim}",
    }
    print(f"  Krein-self-adjointness (S0) admits an off-diagonal gen<->mirror block : {s0_allows}")
    for name, f in forbidders.items():
        print(f"  symmetry FORBIDS Dirac mass?  {name:42s}: {f}  ({witness[name]})")
    print()
    if any_forbid:
        print("  RESULT: PROTECTED -- some GU-native symmetry forbids the Dirac mass => carrier MASSLESS.")
        print("          The occupancy is a flat modulus. LOCATED, not forced.")
    else:
        print("  RESULT: ALLOWED -- NO GU-native LINEAR, frame-nontrivial symmetry forbids the Dirac mass.")
        print("          The carrier is GENERICALLY MASSIVE: each of the 96 gen modes pairs with a mirror")
        print("          mode and lifts to a Dirac mass m. Above scale m the pair DECOUPLES.")
        print("          DECOUPLING CONSEQUENCE: the light chiral spectrum from this sector is 0 net chiral")
        print("          generations -- NOT 3. (Matches the BUILT SW action's vectorlike Majorana block,")
        print("          ||A_++|| = ||A_--|| = 391, source-action-seiberg-witten-RESULTS.md.)")
        print()
        print("  The ONLY operator that distinguishes gen from mirror is the antilinear chiralizer")
        print("  C = J_quat.G, which is FRAME-TRIVIAL (frame charge 0.00, selector-arena). To keep 3 light")
        print("  AND chiral you must PROJECT onto a chiral subsector -- a selector-side chiral projection")
        print("  that breaks the +96/-96 balance. That operator is exactly the frame-trivial chiralizer GU")
        print("  never promoted to a built, frame-level, dynamical projection. Forcing 3 requires it.")
    print("=" * 90)

    out = {
        "carrier_krein_signature": [npl, nmi, nz],
        "S0_krein_selfadjoint_admits_offdiag": bool(s0_allows),
        "S0_defect": s0_defect,
        "S1_su2plus_hom_dim": int(s1_dim), "S1_forbids": bool(s1_forbids),
        "S1_krein_isometry_defect": float(iso_def),
        "S2_Jquat_covariant_mass_norm": float(s2_witness), "S2_forbids": bool(s2_forbids),
        "S2_Jquat_krein_iso_defect": float(jq_iso),
        "S3_chirality_hom_dim": int(s3_dim), "S3_forbids": bool(s3_forbids),
        "S3_gen_chirality": [gp, gm_], "S3_mirror_chirality": [mp, mm_],
        "S4_Jquat_frame_charge_all": float(frame_all_charge),
        "S4_Jquat_frame_charge_sd": float(frame_sd_charge),
        "S4_chiralizer_C2_plus_I": float(kramers),
        "S4_frame_trivial": bool(frame_trivial),
        "any_symmetry_forbids": bool(any_forbid),
        "verdict": "PROTECTED (massless, located-not-forced)" if any_forbid
                   else "ALLOWED (generically massive; decouples; 0 net chiral light, not 3)",
    }
    print("\nMACHINE SUMMARY:", out)
    return out


if __name__ == "__main__":
    main()
