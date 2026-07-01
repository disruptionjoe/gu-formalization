#!/usr/bin/env python3
"""ADVERSARIAL: attack 'J-antilinear carriers give sig IDENTICALLY 0, non-vacuously'.

Independent rebuild of J_quat (own seeds + own method), independent projection,
many samples, plus the twistor-style escapes (multiply by i, use unit k=iJ).
"""
import os, sys
import numpy as np

sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))
from lib import gu_bridge

N, DIM = gu_bridge.N, gu_bridge.DIM
ETA = np.array([1.0]*9 + [-1.0]*5)


def Phi_factory(e128):
    def Phi(U):
        out = np.zeros_like(U)
        for a in range(N):
            out += ETA[a] * (e128[a] @ U @ e128[a].conj())
        return out / N
    return Phi


def quaternionic_J_twirl(e128, seed):
    """Same family as the test but arbitrary seed."""
    Phi = Phi_factory(e128)
    rng = np.random.default_rng(seed)
    U = rng.standard_normal((DIM, DIM)) + 1j*rng.standard_normal((DIM, DIM))
    for _ in range(400):
        U = 0.5*(U + Phi(U))
        U /= np.linalg.norm(U)
    Us, _, Vs = np.linalg.svd(U)
    U = Us @ Vs
    return U / np.sqrt(abs(np.trace(U @ U.conj()) / DIM))


def quaternionic_J_eig(e128):
    """INDEPENDENT METHOD: the +1 eigenspace of the real-linear twirl operator,
    realified, then take an eigenvector with eigenvalue near +1; no random walk."""
    Phi = Phi_factory(e128)
    # Build the 2*DIM^2 real matrix of X -> Phi(X) treating real/imag parts.
    n = DIM*DIM
    # Represent complex matrix as vector; Phi is C-linear, so build complex linear op.
    M = np.zeros((n, n), dtype=complex)
    basis_done = 0
    # Build by columns: apply Phi to each unit matrix E_ij.
    E = np.zeros((DIM, DIM), dtype=complex)
    for i in range(DIM):
        for j in range(DIM):
            E[:] = 0; E[i, j] = 1.0
            col = Phi(E).reshape(-1)
            M[:, i*DIM + j] = col
    w, V = np.linalg.eig(M)
    # pick eigenvector with eigenvalue closest to +1
    idx = np.argsort(-np.real(w))
    for k in idx:
        if abs(w[k] - 1.0) < 1e-6:
            U = V[:, k].reshape(DIM, DIM)
            break
    else:
        U = V[:, idx[0]].reshape(DIM, DIM)
    # polar-project to unitary
    Us, _, Vs = np.linalg.svd(U)
    U = Us @ Vs
    return U / np.sqrt(abs(np.trace(U @ U.conj()) / DIM))


def report_J(U, e128, label):
    # J(x) = U conj(x). J^2 = U conj(U). want U conj(U) = -I.
    UbarU = U @ U.conj()
    j2 = np.linalg.norm(UbarU + np.eye(DIM))            # J^2 = -1 ?
    unit = np.linalg.norm(U.conj().T @ U - np.eye(DIM)) # unitary ?
    comm = max(np.linalg.norm(U @ e128[a] - e128[a] @ U) for a in range(N))
    print(f"  [{label}] ||U conjU + I||={j2:.2e}  ||U*U - I||={unit:.2e}  max||[U,e_a]||={comm:.2e}")
    return j2, unit, comm


def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=170)
    e, Gamma, Pi, M_D = gu_bridge.constraint_objects()
    Q = np.eye(N*DIM, dtype=complex) - Pi
    e128 = gu_bridge.gammas()
    bare = float(np.linalg.norm(Pi @ M_D - M_D @ Pi))
    C2 = float(np.linalg.norm(Gamma @ M_D @ Pi))
    print(f"[anchors] bare={bare:.4f} (58.7215)  C2={C2:.4f} (155.3625)")

    # Build several independent J's
    Js = {}
    for s in (1, 7, 42, 999):
        Js[f"twirl-seed{s}"] = quaternionic_J_twirl(e128, s)
    print("\n=== J_quat self-checks (J^2=-1, unitary, [J,e_a]=0) ===")
    for lab, U in Js.items():
        report_J(U, e128, lab)

    def sig(A, rtol=1e-7):
        ev = np.linalg.eigvalsh(0.5*(A + A.conj().T))
        tol = rtol*np.abs(ev).max()
        return int((ev > tol).sum()) - int((ev < -tol).sum())

    def make_ops(U):
        Uf = np.kron(np.eye(N), U)
        Ufi = np.linalg.inv(Uf)
        Sop  = lambda X: Uf @ X.conj() @ Ufi
        gd   = lambda X: Pi @ X @ Pi + Q @ X @ Q
        herm = lambda X: 0.5*(X + X.conj().T)
        jlin = lambda X: 0.5*(X + Sop(X))
        janti= lambda X: 0.5*(X - Sop(X))
        return Uf, Ufi, Sop, gd, herm, jlin, janti

    # structural: does S preserve Pi (needed for gd to preserve S-eigenspaces)?
    print("\n=== does S preserve the projector Pi (S(Pi)=Pi)? ===")
    for lab, U in Js.items():
        Uf, Ufi, Sop, gd, herm, jlin, janti = make_ops(U)
        spi = np.linalg.norm(Sop(Pi) - Pi)
        print(f"  [{lab}] ||S(Pi) - Pi|| = {spi:.2e}")

    # MAIN ATTACK: many antilinear samples for each J
    print("\n=== ANTILINEAR carriers: antilinearity resid, norm, signature (50 samples each J) ===")
    for lab, U in Js.items():
        Uf, Ufi, Sop, gd, herm, jlin, janti = make_ops(U)
        rng = np.random.default_rng(20260627)
        sigs, nrms, resid = [], [], []
        for _ in range(50):
            R = rng.standard_normal((N*DIM, N*DIM)) + 1j*rng.standard_normal((N*DIM, N*DIM))
            Da = herm(gd(janti(R)))
            sigs.append(sig(Da))
            nrms.append(float(np.linalg.norm(Da)))
            resid.append(float(np.linalg.norm(Sop(Da) + Da)))  # S(Da) = -Da ?
        sigs = np.array(sigs)
        print(f"  [{lab}] sig: min={sigs.min()} max={sigs.max()} #nonzero={int((sigs!=0).sum())}/{len(sigs)} "
              f"| ||D|| mean={np.mean(nrms):.0f} | S(D)=-D resid mean={np.mean(resid):.1e} max={np.max(resid):.1e}")

    # robustness of sig=0 to tolerance (does it 'flow' if we tighten tol?)
    print("\n=== antilinear sig under varying rtol (twirl-seed1) ===")
    U = Js["twirl-seed1"]
    Uf, Ufi, Sop, gd, herm, jlin, janti = make_ops(U)
    rng = np.random.default_rng(5)
    R = rng.standard_normal((N*DIM, N*DIM)) + 1j*rng.standard_normal((N*DIM, N*DIM))
    Da = herm(gd(janti(R)))
    ev = np.linalg.eigvalsh(Da)
    print(f"  spectrum: min={ev.min():.3e} max={ev.max():.3e} |min eig nonzero|={np.min(np.abs(ev)):.2e}")
    for rt in (1e-3, 1e-5, 1e-7, 1e-9, 1e-11):
        print(f"    rtol={rt:.0e} -> sig={sig(Da, rt)}")
    # how symmetric is the spectrum? compare sorted ev vs -reversed
    sym = np.linalg.norm(np.sort(ev) + np.sort(-ev)[::-1]*0 + np.sort(ev)[::-1])  # placeholder
    pos = np.sort(ev[ev>0]); neg = np.sort(-ev[ev<0])
    m = min(len(pos), len(neg))
    pair_resid = np.linalg.norm(pos[:m] - neg[:m]) if m>0 else 0.0
    print(f"  spectrum pairing |+λ vs -λ| resid={pair_resid:.2e}  (#pos={len(pos)} #neg={len(neg)})")

    # TWISTOR ESCAPE 1: multiply an H-linear carrier by complex i
    print("\n=== TWISTOR ESCAPE: i * (H-linear Hermitian carrier) ===")
    U = Js["twirl-seed1"]
    Uf, Ufi, Sop, gd, herm, jlin, janti = make_ops(U)
    rng = np.random.default_rng(11)
    R = rng.standard_normal((N*DIM, N*DIM)) + 1j*rng.standard_normal((N*DIM, N*DIM))
    Dl = herm(gd(jlin(R)))            # H-linear Hermitian carrier
    iDl = 1j*Dl
    print(f"  H-linear Dl: sig={sig(Dl)}  ||Dl||={np.linalg.norm(Dl):.0f}")
    print(f"  i*Dl is Hermitian? ||herm(iDl)-iDl||={np.linalg.norm(herm(iDl)-iDl):.2e} (anti-herm => herm kills it)")
    print(f"  herm(i*Dl): sig={sig(herm(iDl))}  ||herm(iDl)||={np.linalg.norm(herm(iDl)):.2e}")

    # TWISTOR ESCAPE 2: unit k = i*J. Does S_k differ from S?
    print("\n=== TWISTOR ESCAPE: quaternion unit k = i*J (S_k vs S) ===")
    Uk = 1j*U
    Ukf = np.kron(np.eye(N), Uk); Ukfi = np.linalg.inv(Ukf)
    Sk = lambda X: Ukf @ X.conj() @ Ukfi
    rng = np.random.default_rng(13)
    R = rng.standard_normal((N*DIM, N*DIM)) + 1j*rng.standard_normal((N*DIM, N*DIM))
    diff = np.linalg.norm(Sk(R) - Sop(R))
    print(f"  ||S_k(R) - S(R)|| = {diff:.2e}  (if 0, k gives identical antilinear sector)")
    janti_k = lambda X: 0.5*(X - Sk(X))
    Da_k = herm(gd(janti_k(R)))
    print(f"  k-antilinear carrier: sig={sig(Da_k)}  ||D||={np.linalg.norm(Da_k):.0f}")

    # CONTROL: does jlin reach 4Z and mixed reach 2mod4 (sanity that machinery is alive)?
    print("\n=== CONTROL (twirl-seed1): jlin & mixed ===")
    U = Js["twirl-seed1"]
    Uf, Ufi, Sop, gd, herm, jlin, janti = make_ops(U)
    rng = np.random.default_rng(303)
    ls, ms = [], []
    for _ in range(12):
        R = rng.standard_normal((N*DIM, N*DIM)) + 1j*rng.standard_normal((N*DIM, N*DIM))
        ls.append(sig(herm(gd(jlin(R)))))
        ms.append(sig(herm(gd(R))))
    print(f"  jlin sig={sorted(ls)} all4Z={all(x%4==0 for x in ls)}")
    print(f"  mixed sig={sorted(ms)} reaches2mod4={any(x%4==2 for x in ms)}")


if __name__ == "__main__":
    main()
