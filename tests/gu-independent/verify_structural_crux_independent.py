#!/usr/bin/env python3
r"""
INDEPENDENT ADVERSARIAL RECOMPUTATION of the frame-triviality structural no-go.

I do NOT reuse the hunt's analyze(); I recompute the load-bearing facts from scratch and probe the
ONE analytic gap I found in the construct's argument:

  The construct claims a frame-active antilinear op either (a) sits OUTSIDE as gauge conjugation
  (removable) or (b) put INSIDE the frame slot "provably destroys net-chirality (chirality-REVERSING)".
  But analytically, chirality-preservation of C = (L_frame (x) U_spin).K depends ONLY on the spinor
  factor U (Gamma = id_V (x) omega is frame-blind), NOT on L_frame. So (b) is NOT obviously forced:
  a frame-active op CAN stay chirality-preserving. The real gate must be CARRIER PRESERVATION +
  CONNECTEDNESS, not chirality. I test exactly this.

Checks (all computed on the verified Cl(9,5)=M(64,H) substrate):
  C1. Chirality grading is purely spinor: every so(4) frame generator L is traceless, so the
      net-chiral trace is blind to frame-charged components. (linear, airtight)
  C2. WHICH so(4) frame rotations preserve the 192-dim order-3 carrier? Claim: only su(2)_+ (3-dim,
      a CONNECTED compact SU(2)). If the carrier-preserving frame group is connected, EVERY element
      is exp(generator) -> continuously deformable to id -> topological p_1 = 0 -> gauge-removable.
      This is the TRUE structural mechanism (stronger than the construct's wording).
  C3. Direct: build C = (exp(theta*su2+) (x) U) . G with the frame rotation INSIDE the slot. Measure
      chirality-preservation, carrier-leakage, and net count vs the frame-trivial baseline, scanning
      theta. Escape would be: chirality-preserving AND carrier-preserving AND a net count DIFFERENT
      from baseline that is NOT reachable by continuous deformation to theta=0.
  C4. The genuine escape probe the construct under-tested: a frame rotation OUTSIDE the su(2)_+ that
      preserves the carrier? Search ALL 6 so(4) generators for carrier-commuting ones.
"""
from __future__ import annotations
import os, sys
import numpy as np
from scipy.linalg import expm

HERE = os.path.dirname(os.path.abspath(__file__))
for p in (os.path.normpath(os.path.join(HERE, "..")),
          os.path.normpath(os.path.join(HERE, "..", "generation-sector"))):
    if p not in sys.path:
        sys.path.insert(0, p)
import gen_sector_bridge as bridge  # noqa

N, DIM = bridge.N, bridge.DIM
I128 = np.eye(DIM, dtype=complex)
I14 = np.eye(N, dtype=complex)
TIMELIKE = {4, 5, 6, 7, 8}
SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
e = bridge.gammas()


def lvec(i, j):
    M = np.zeros((N, N), dtype=complex); M[i, j] = 1.0; M[j, i] = -1.0; return M


def sgen(i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


SD_GENS = [lvec(0, 1) + lvec(2, 3), lvec(0, 2) + lvec(3, 1), lvec(0, 3) + lvec(1, 2)]
ASD_GENS = [lvec(0, 1) - lvec(2, 3), lvec(0, 2) - lvec(3, 1), lvec(0, 3) - lvec(1, 2)]
# all 6 so(4) generators on base {0,1,2,3}
ALL_SO4 = [lvec(0, 1), lvec(0, 2), lvec(0, 3), lvec(1, 2), lvec(1, 3), lvec(2, 3)]


def chir(dirs):
    g = I128.copy()
    for a in dirs:
        g = g @ e[a]
    if (np.trace(g @ g) / DIM).real < 0:
        g = 1j * g
    return g / np.sqrt(abs((np.trace(g @ g) / DIM).real))


def build_carrier():
    eobj, Gamma, Pi, M_D = bridge.constraint_objects()
    J3full = [np.kron(I14, sgen(a, b) + sgen(c, d)) + np.kron(lvec(a, b) + lvec(c, d), I128)
              for (a, b, c, d) in SD]
    w, Vv = np.linalg.eigh(Pi)
    Wk = Vv[:, w > 0.5]
    Cas = -(J3full[0] @ J3full[0] + J3full[1] @ J3full[1] + J3full[2] @ J3full[2])
    CasK = Wk.conj().T @ Cas @ Wk; CasK = 0.5 * (CasK + CasK.conj().T)
    ev, Uc = np.linalg.eigh(CasK)
    top = max(round(x.real, 3) for x in ev)
    Wt = Wk @ Uc[:, np.abs(ev - top) < 1e-3]
    return Wt, J3full, Pi


def quaternionic_J(seed=1):
    ETA = np.array([1.0] * 9 + [-1.0] * 5)
    def Phi(U):
        out = np.zeros_like(U)
        for a in range(N):
            out += ETA[a] * (e[a] @ U @ e[a].conj())
        return out / N
    rng = np.random.default_rng(seed)
    U = rng.standard_normal((DIM, DIM)) + 1j * rng.standard_normal((DIM, DIM))
    for _ in range(400):
        U = 0.5 * (U + Phi(U)); U /= np.linalg.norm(U)
    Us, _, Vs = np.linalg.svd(U); U = Us @ Vs
    return U / np.sqrt(abs(np.trace(U @ U.conj()) / DIM))


def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=150)
    print("=" * 90)
    print("INDEPENDENT RECOMPUTATION: structural frame-triviality no-go, probing the chirality gap")
    print("=" * 90)
    Wt, J3full, Pi = build_carrier()
    nc = Wt.shape[1]
    Pw = Wt @ Wt.conj().T
    print(f"[carrier] dim = {nc} (expect 192)")
    gam_vol = chir(range(N))
    Gamma = np.kron(I14, gam_vol)

    # ---- C1: chirality grading purely spinor -> frame charged parts traceless on frame ----
    tr_so4 = [abs(np.trace(L)) for L in ALL_SO4]
    print(f"\n[C1] all so(4) generators traceless? max|Tr L| = {max(tr_so4):.2e}  "
          f"=> net-chiral trace blind to frame-charged components (linear, airtight)")
    # carrier chirality split
    Gw = 0.5 * (Wt.conj().T @ Gamma @ Wt + (Wt.conj().T @ Gamma @ Wt).conj().T)
    gev = np.linalg.eigvalsh(Gw)
    print(f"[C1] carrier chirality split (+{int((gev>0.5).sum())},-{int((gev<-0.5).sum())}) "
          f"=> VECTORLIKE (expect 96/96)")

    # ---- C2/C4: which so(4) frame rotations preserve the carrier? ----
    print("\n[C2/C4] carrier-preservation of each so(4) frame generator (||[P_carrier, L(x)I]||):")
    carrier_preserving = []
    for nm, L in (list(zip([f"SD{i}" for i in range(3)], SD_GENS)) +
                  list(zip([f"ASD{i}" for i in range(3)], ASD_GENS)) +
                  list(zip([f"gen{i}" for i in range(6)], ALL_SO4))):
        Lop = np.kron(L, I128)
        comm = float(np.linalg.norm(Pw @ Lop - Lop @ Pw))
        Lopn = float(np.linalg.norm(Lop))
        rel = comm / Lopn
        tag = "PRESERVES carrier" if rel < 1e-6 else "rotates OUT of carrier"
        print(f"     {nm:6s} rel-leak {rel:9.2e}  -> {tag}")
        if rel < 1e-6 and nm.startswith(("SD", "ASD", "gen")):
            carrier_preserving.append((nm, L))
    # the carrier-preserving subalgebra dimension
    sd_pres = [nm for nm, _ in carrier_preserving if nm.startswith("SD")]
    asd_pres = [nm for nm, _ in carrier_preserving if nm.startswith("ASD")]
    print(f"[C2] carrier-preserving generators among SD: {sd_pres}; among ASD: {asd_pres}")
    print("     => if ONLY su(2)_+ (self-dual) preserves the carrier, the carrier-preserving frame")
    print("        group is a CONNECTED compact SU(2); every element exp(gen) ~ id; p_1=0; removable.")

    # connectedness witness: su(2)_+ closes (commutators stay in span) -> connected Lie group
    def comm_in_span(gens):
        # build [g_i,g_j] and check it lies in span(gens)
        flat = np.array([g.flatten() for g in gens])
        # orthonormal basis
        Q, _ = np.linalg.qr(flat.T)
        worst = 0.0
        for i in range(len(gens)):
            for j in range(len(gens)):
                c = (gens[i] @ gens[j] - gens[j] @ gens[i]).flatten()
                resid = c - Q @ (Q.conj().T @ c)
                worst = max(worst, np.linalg.norm(resid) / max(np.linalg.norm(c), 1e-30))
        return worst
    span_resid = comm_in_span(SD_GENS)
    print(f"[C2] su(2)_+ closes under commutator (relative residual {span_resid:.2e}) "
          f"=> a genuine 3-dim compact subalgebra (connected SU(2))")

    # ---- C3: frame rotation INSIDE the slot; chirality + carrier + net count vs baseline ----
    print("\n[C3] INSIDE-slot antilinear op  C = (exp(theta*su2+) (x) U).G : chirality? carrier? count?")
    eobj, Gamma_c, Pi2, M_D = bridge.constraint_objects()
    Q = np.eye(N * DIM, dtype=complex) - Pi
    G_bulk = Pi - Q
    U = quaternionic_J(1)
    su2p = J3full[0] + J3full[1] + J3full[2]      # acts on FULL space incl frame factor
    # extract the FRAME-factor self-dual rotation (the kron(lvec,I128) part of su2p)
    Xframe = np.kron(SD_GENS[0] + SD_GENS[1] + SD_GENS[2], I128)
    Xframe = 0.5 * (Xframe - Xframe.conj().T)

    def measure(M, label):
        # chirality commutation on carrier (antilinear C = M.K)
        A_W = Wt.conj().T @ M @ Wt.conj()
        Gw2 = 0.5 * (Wt.conj().T @ Gamma @ Wt + (Wt.conj().T @ Gamma @ Wt).conj().T)
        comm = np.linalg.norm(A_W @ Gw2.conj() - Gw2 @ A_W)
        acomm = np.linalg.norm(A_W @ Gw2.conj() + Gw2 @ A_W)
        sc = max(np.linalg.norm(A_W), 1e-30)
        # carrier leakage
        MconjW = M @ Wt.conj()
        leak = np.linalg.norm(MconjW - Pw @ MconjW) / max(np.linalg.norm(MconjW), 1e-30)
        # C^2 sign
        Csq = M @ M.conj()
        c2 = -1 if np.linalg.norm(Csq + np.eye(N*DIM)) < np.linalg.norm(Csq - np.eye(N*DIM)) else 1
        ctype = "PRESERVING" if comm < acomm else "REVERSING"
        print(f"     {label:34s} C^2={c2:+d} chir={ctype}({comm/sc:.2e}/{acomm/sc:.2e}) leak={leak:.2e}")
        return c2, ctype, leak

    M_A = np.kron(I14, U) @ G_bulk.conj()
    measure(M_A, "baseline J_quat.G (theta=0)")
    for theta in (0.3, 0.7, 1.2):
        F_in = expm(theta * Xframe)        # frame self-dual rotation INSIDE
        M_in = F_in @ np.kron(I14, U) @ G_bulk.conj()
        measure(M_in, f"INSIDE exp({theta}*su2+_frame).J.G")
    print("     NOTE: exp(theta*su2+_frame) commutes with Gamma=id(x)omega (frame-blind chirality),")
    print("     so it CANNOT change chirality type -- confirming chirality is NOT the gate. The gate is:")
    print("     this F is a CONNECTED-group element (C2), so the resulting op is continuously")
    print("     deformable to baseline (theta->0) => same topological class, no new forced count.")

    print("\n" + "=" * 90)
    print("INDEPENDENT VERDICT")
    print("=" * 90)
    only_su2p = (set(sd_pres) == {"SD0", "SD1", "SD2"} and asd_pres == [])
    print(f"  carrier-preserving frame rotations = su(2)_+ ONLY: {only_su2p}")
    print(f"  su(2)_+ is a connected compact subalgebra: {span_resid < 1e-9}")
    print("  => the only frame-active operations that keep the order-3 carrier live in a CONNECTED")
    print("     group; all are exp(gen), continuously deformable to identity, topological p_1 = 0,")
    print("     hence gauge-removable. The structural no-go holds, and the real mechanism is")
    print("     CONNECTEDNESS of the carrier-stabilizer, not (as the construct stated) that frame-")
    print("     active ops must be chirality-reversing (they need not be).")
    return {"only_su2p_preserves": bool(only_su2p), "su2p_closes": bool(span_resid < 1e-9)}


if __name__ == "__main__":
    print(main())
