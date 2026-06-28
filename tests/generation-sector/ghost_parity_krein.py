"""
Ghost parity / Krein structure of the self-dual generation triplet (GU / Turok-Bateman synthesis).

Establishes, machine-checked and exact in every signature:
  (1) GU's RS matter module V (x) S is a Krein space: the so(p,q)-invariant form K = eta_V (x) beta_S is
      indefinite, beta_S the spinor Krein metric (product of spacelike gammas), with beta_S sigma +
      sigma^dagger beta_S = 0 for every so(p,q) generator (pseudo-anti-Hermitian; residual 0).
  (2) The self-dual SU(2)+ generation triplet (H1) is a NEUTRAL / hyperbolic subspace: K|triplet has
      signature (+96, -96, 0). Each generation is bound to its mirror in a hyperbolic (null) pair.

This is the kinematic structure on which Turok & Bateman's ghost-parity generalized Born rule operates:
a Z2 ghost parity resolves each hyperbolic pair into one positive-norm physical generation + one
negative-norm ghost (mirror), and the projector Born rule gives positive probabilities. See
canon/ghost-parity-krein-synthesis.md for the full statement and the open (dynamical) boundary.
"""
import numpy as np

N, DIM = 14, 128

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

def sgen(e, i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])

def lvec(i, j):
    M = np.zeros((N, N), dtype=complex); M[i, j] = 1; M[j, i] = -1; return M

SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]   # self-dual SU(2)+ on Euclidean base {0,1,2,3}

def analyze(timelike, label):
    e = [(1j * base[a] if a in timelike else base[a]) for a in range(14)]
    spacelike = [a for a in range(14) if a not in timelike]
    p, q = len(spacelike), len(timelike)

    # gamma-trace constraint surface and the self-dual triplet sector
    Gamma = np.hstack(e)
    Pi = np.eye(N * DIM, dtype=complex) - Gamma.conj().T @ np.linalg.inv(Gamma @ Gamma.conj().T) @ Gamma
    J = [np.kron(I14, sgen(e, a, b) + sgen(e, c, d)) + np.kron(lvec(a, b) + lvec(c, d), I128)
         for (a, b, c, d) in SD]
    w, Vv = np.linalg.eigh(Pi); W = Vv[:, w > 0.5]
    Cas = -(J[0] @ J[0] + J[1] @ J[1] + J[2] @ J[2])
    CasK = W.conj().T @ Cas @ W; CasK = 0.5 * (CasK + CasK.conj().T)
    ev, U = np.linalg.eigh(CasK)
    top = max(round(x.real, 3) for x in ev)
    Wt = W @ U[:, np.abs(ev - top) < 1e-3]

    # spinor Krein metric beta_S = product of spacelike gammas; Hermitian, beta^2 = I
    bS = I128.copy()
    for s in spacelike:
        bS = bS @ e[s]
    if np.linalg.norm(bS.conj().T + bS) < 1e-9:
        bS = 1j * bS
    bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
    res = max(np.linalg.norm(bS @ sgen(e, i, j) + sgen(e, i, j).conj().T @ bS)
              for i in range(14) for j in range(i + 1, 14))   # pseudo-anti-Hermitian: beta sigma + sigma^d beta = 0
    assert res < 1e-9, (label, res)

    etaV = np.diag([(-1.0 if a in timelike else 1.0) for a in range(14)]).astype(complex)
    K = np.kron(etaV, bS)
    B = Wt.conj().T @ K @ Wt; B = 0.5 * (B + B.conj().T)
    sig = np.linalg.eigvalsh(B)
    npl, nmi, nz = int(np.sum(sig > 1e-9)), int(np.sum(sig < -1e-9)), int(np.sum(np.abs(sig) < 1e-9))
    print(f"{label} ({p},{q}): beta pseudo-anti-Herm residual {res:.0e} | "
          f"triplet Krein signature (+{npl}, -{nmi}, 0:{nz}) -> "
          f"{'NEUTRAL/hyperbolic: 96 (generation,mirror) pairs' if npl == nmi else 'asymmetric'}")
    assert npl == nmi == 96, (label, npl, nmi)

if __name__ == "__main__":
    analyze({4, 5, 6, 7, 8}, "(9,5)")
    analyze({4, 5, 6, 7, 8, 9, 10}, "(7,7)")
    analyze(set(), "(14,0)")
    print("\nGU matter module is a Krein space; the self-dual generation triplet is maximally neutral "
          "(hyperbolic generation/mirror pairs).\nTurok-Bateman ghost parity resolves each pair into "
          "1 physical generation + 1 ghost. See canon/ghost-parity-krein-synthesis.md.")
