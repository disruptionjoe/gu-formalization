"""
H1 -- the self-dual SU(2)+ family kill (reviewer R1+R2's decisive attack), reproduced.

Question (from two adversarial reviews of papers/multiplicity-theorem-note-2026-06-28.md):
the paper's sharp claim is "3 divides no GU-native branching multiplicity; a generation count of 3 is
equivalent to importing the prime 3." The kill: the Rarita-Schwinger matter sector is V (x) S; the VECTOR
index V (the 14) carries family branching, and under SO(14) > SO(10) x SU(2)+ the self-dual SU(2)+ -- the
rank-3 Lambda^2_+ adjoint of any 4-manifold, intrinsic GU-forced geometry -- rides on an ODD number
(2 (x) 2 = 3 + 1). Does a multiplicity-3 generation family survive the gamma-trace projection?

RESULT: yes. ker(Gamma) = 640 singlets + 416 doublets + 64 TRIPLETS of SU(2)+; the 64 triplets carry the
pure Spin(10) generation spinor (16/16bar). So a GU-native branching multiplicity = 3 EXISTS; the paper's
sharp thesis is refuted. The triplet is vectorlike in Euclidean (14,0) (96/96 by chirality, net 0), so it
is not yet a net-chiral-3; the chiral question passes to the Lorentzian self-dual analysis (H2).

Signature-independent for the multiplicity question, so we use the simplest rep, Euclidean (14,0).
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

e = jw(7)                                   # 14 Hermitian gammas, e_a^2 = +I; base {0,1,2,3}, internal {4..13}
I128, I14 = np.eye(DIM, dtype=complex), np.eye(N, dtype=complex)

# gamma-trace constraint surface
Gamma = np.hstack(e)
Pi = np.eye(N * DIM, dtype=complex) - Gamma.conj().T @ np.linalg.inv(Gamma @ Gamma.conj().T) @ Gamma
ker = int(round(np.trace(Pi).real))
assert ker == 1664, ker

def sgen(i, j):                              # so(N) spinor generator
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])

def lvec(i, j):                              # so(N) vector generator (Euclidean)
    M = np.zeros((N, N), dtype=complex); M[i, j] = 1; M[j, i] = -1; return M

# self-dual SU(2)+ generators on V (x) S : (01+23),(02+31),(03+12), acting on BOTH vector and spinor
sd = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
J = [np.kron(I14, sgen(a, b) + sgen(c, d)) + np.kron(lvec(a, b) + lvec(c, d), I128) for (a, b, c, d) in sd]

def comm(A, B): return A @ B - B @ A

# (1) verify genuine su(2) and that SU(2)+ preserves ker(Gamma)
c01 = np.trace(comm(J[0], J[1]).conj().T @ J[2]) / np.trace(J[2].conj().T @ J[2])
res = np.linalg.norm(comm(J[0], J[1]) - c01 * J[2]) / np.linalg.norm(J[2])
cpi = max(np.linalg.norm(comm(Jx, Pi)) for Jx in J)
print(f"[1] su(2): [J0,J1] = ({c01.real:+.3f}) J2, residual {res:.1e}; max||[J,Pi]|| = {cpi:.1e}")
assert res < 1e-9 and cpi < 1e-9

# (2) SU(2)+ spin decomposition of ker(Gamma)  (Casimir -(sum J^2) has eigenvalue 4 j(j+1))
w, V = np.linalg.eigh(Pi); W = V[:, w > 0.5]
Cas = -(J[0] @ J[0] + J[1] @ J[1] + J[2] @ J[2])
CasK = W.conj().T @ Cas @ W; CasK = 0.5 * (CasK + CasK.conj().T)
ev, U = np.linalg.eigh(CasK)
from collections import Counter
spins = Counter()
for x in ev:
    j = (-1 + np.sqrt(1 + 4 * max(x.real / 4.0, 0))) / 2
    spins[round(j * 2) / 2] += 1
print("[2] SU(2)+ content of ker(Gamma):", {f"j={k}": v for k, v in sorted(spins.items())},
      "  (640*1 + 416*2 + 64*3 = 1664)")
assert spins[1.0] == 192, spins   # 64 triplets

# (3) the triplet sector carries the pure Spin(10) generation spinor
mask = np.abs(ev - 8.0) < 1e-4                # j=1 Casimir = 8
Wtrip = W @ U[:, mask]
Cas10 = np.zeros((N * DIM, N * DIM), dtype=complex)
for i in range(4, 14):
    for j in range(i + 1, 14):
        T = np.kron(lvec(i, j), I128) + np.kron(I14, sgen(i, j))
        Cas10 += T @ T
C10 = Wtrip.conj().T @ Cas10 @ Wtrip
val = np.linalg.eigvalsh(0.5 * (C10 + C10.conj().T))
ref = np.zeros((DIM, DIM), dtype=complex)
for i in range(4, 14):
    for j in range(i + 1, 14):
        ref += sgen(i, j) @ sgen(i, j)
ref16 = np.linalg.eigvalsh(0.5 * (ref + ref.conj().T)).max().real
print(f"[3] triplet sector (dim {Wtrip.shape[1]}): Spin(10) Casimir = {val.mean().real:.2f} "
      f"(spread {np.ptp(val).real:.1e}); reference 16/16bar = {ref16:.2f} -> PURE GENERATION SPINOR")
assert abs(val.mean().real - ref16) < 1e-6 and np.ptp(val).real < 1e-6

# (4) chirality of the triplet sector (Euclidean (14,0): omega_14^2 = -1, chirality = -i omega_14)
om = I128.copy()
for a in range(14):
    om = om @ e[a]
chir = (-1j) * np.kron(I14, om)
Ct = Wtrip.conj().T @ chir @ Wtrip
ce = np.linalg.eigvalsh(0.5 * (Ct + Ct.conj().T))
nplus, nminus = int(np.sum(ce > 0.5)), int(np.sum(ce < -0.5))
print(f"[4] triplet chirality split: +{nplus} / -{nminus}; NET = {nplus - nminus} "
      f"({(nplus - nminus)//3} net triplets) -> {'VECTORLIKE' if nplus==nminus else 'CHIRAL'} in Euclidean")

print("\nCONCLUSION: GU-native multiplicity-3 generation family EXISTS (self-dual SU(2)+ triplet, pure 16/16bar).")
print("The paper's sharp 'count=3 iff import prime 3' is REFUTED. Vectorlike in Euclidean; chiral question -> H2.")
