"""
T1a -- kinematic falsification test of the ghost-parity chiralization (the six-axis candidate's own test).

Claim under attack: a ghost parity Z2 could turn the vectorlike self-dual triplet into a net-chiral 3
WITHOUT any dynamics (purely kinematically). The six-axis candidate predicts the KILL via index
conservation: a gauge-equivariant generation-mirror swap is a reality structure, so its physical eigenspace
carries net chirality 0.

RESULT (machine-checked, (9,5) and (7,7)): the Krein form K restricted to the 192-dim triplet is purely
CROSS-chirality -- the same-chirality blocks ||K(+,+)|| and ||K(-,-)|| vanish (~1e-14). Therefore every
maximal positive-definite ("physical") subspace is exactly 50/50 chirality, and its net chirality is 0
(~1e-15). No ghost parity (gauge-equivariant or not) can chiralize the triplet kinematically. The
chirality requires a symmetry-breaking dynamics (the unbuilt source action) or a base-manifold Dirac
index. This pins the central claim's honest boundary: ghost parity is necessary (physical-sector
selection) but not sufficient (chiral selection).
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

SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]

def run(timelike, label):
    e = [(1j * base[a] if a in timelike else base[a]) for a in range(14)]
    spacelike = [a for a in range(14) if a not in timelike]
    Gamma = np.hstack(e)
    Pi = np.eye(N * DIM, dtype=complex) - Gamma.conj().T @ np.linalg.inv(Gamma @ Gamma.conj().T) @ Gamma
    J = [np.kron(I14, sgen(e, a, b) + sgen(e, c, d)) + np.kron(lvec(a, b) + lvec(c, d), I128)
         for (a, b, c, d) in SD]
    w, V = np.linalg.eigh(Pi); W = V[:, w > 0.5]
    Cas = -(J[0] @ J[0] + J[1] @ J[1] + J[2] @ J[2])
    CasK = W.conj().T @ Cas @ W; CasK = 0.5 * (CasK + CasK.conj().T)
    ev, U = np.linalg.eigh(CasK); top = max(round(x.real, 3) for x in ev)
    Wt = W @ U[:, np.abs(ev - top) < 1e-3]

    bS = I128.copy()
    for s in spacelike:
        bS = bS @ e[s]
    if np.linalg.norm(bS.conj().T + bS) < 1e-9:
        bS = 1j * bS
    bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
    etaV = np.diag([(-1.0 if a in timelike else 1.0) for a in range(14)]).astype(complex)
    K = np.kron(etaV, bS)
    om = I128.copy()
    for a in range(14):
        om = om @ e[a]
    om2 = (np.trace(om @ om) / DIM).real
    chir = np.kron(I14, om if om2 > 0 else (-1j) * om)

    Kt = Wt.conj().T @ K @ Wt; Kt = 0.5 * (Kt + Kt.conj().T)
    Ct = Wt.conj().T @ chir @ Wt; Ct = 0.5 * (Ct + Ct.conj().T)
    cev, cU = np.linalg.eigh(Ct); Pp = cU[:, cev > 0.5]; Pm = cU[:, cev < -0.5]
    Kpp = np.linalg.norm(Pp.conj().T @ Kt @ Pp)
    Kmm = np.linalg.norm(Pm.conj().T @ Kt @ Pm)
    kev, kU = np.linalg.eigh(Kt); phys = kU[:, kev > 1e-9]
    net = np.trace(phys.conj().T @ Ct @ phys).real
    print(f"{label}: ||K(+chir,+chir)||={Kpp:.1e}, ||K(-chir,-chir)||={Kmm:.1e}  (K is cross-chirality) ; "
          f"net chirality of K-positive subspace = {net:+.1e}")
    assert Kpp < 1e-9 and Kmm < 1e-9 and abs(net) < 1e-6, (label, Kpp, Kmm, net)

if __name__ == "__main__":
    run({4, 5, 6, 7, 8}, "(9,5)")
    run({4, 5, 6, 7, 8, 9, 10}, "(7,7)")
    print("\nKINEMATIC KILL CONFIRMED: no ghost parity chiralizes the triplet without dynamics. "
          "Chirality requires a symmetry-breaking dynamics or a base-manifold Dirac index.")
