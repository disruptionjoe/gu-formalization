"""
Leg 3 closure (H3): enumerate the su(2) family embeddings in the commutant of the gauge group and compute
the generation (16) multiplicity for each.

Spin(14) > Spin(10) x Spin(4); the commutant of the unification group Spin(10) is so(4) = su(2)+ (+) su(2)-.
Up to conjugacy there are three su(2) subalgebras: self-dual su(2)+, anti-self-dual su(2)-, and the
diagonal/vector su(2) (the so(3) rotation of three base axes). su(3) cannot embed: dim su(3) = 8 > 6 = dim
so(4). Decisive question: does any embedding give an ODD generation multiplicity other than the self-dual
triplet 3?

RESULT (machine-checked): the 16-multiplicity space (dim 16) decomposes as
  self-dual su(2)+      : 2*(j=0) + 4*(j=1/2) + 2*(j=1)   -> odd piece is the TRIPLET (j=1, dim 3)
  anti-self-dual su(2)- : same (parity image)             -> odd piece is the TRIPLET (j=1, dim 3)
  diagonal/vector su(2) : 4*(j=1/2) + 2*(j=3/2)           -> ONLY even (2-smooth); NO odd piece
The odd generation multiplicity is always exactly the triplet (3); never a quintet (5) or higher, and no
su(3) commutes with Spin(10). Honest residual: a family symmetry commuting only with the SM subgroup
(not all of Spin(10)) has a larger commutant in which a horizontal su(3) could live; that case is not
covered here.
"""
import numpy as np
from collections import Counter

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

e = jw(7)
I128, I14 = np.eye(DIM, dtype=complex), np.eye(N, dtype=complex)

def sgen(i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])

def lvec(i, j):
    M = np.zeros((N, N), dtype=complex); M[i, j] = 1; M[j, i] = -1; return M

def gen(i, j):
    return np.kron(I14, sgen(i, j)) + np.kron(lvec(i, j), I128)

Gamma = np.hstack(e)
Pi = np.eye(N * DIM, dtype=complex) - Gamma.conj().T @ np.linalg.inv(Gamma @ Gamma.conj().T) @ Gamma
w, V = np.linalg.eigh(Pi); W = V[:, w > 0.5]

# reference Spin(10) Casimir of the 16/16bar spinor, and the 16-sector projector within ker(Gamma)
ref = np.zeros((DIM, DIM), dtype=complex)
for i in range(4, 14):
    for j in range(i + 1, 14):
        ref += sgen(i, j) @ sgen(i, j)
ref16 = np.linalg.eigvalsh(0.5 * (ref + ref.conj().T)).max().real
Cas10 = np.zeros((N * DIM, N * DIM), dtype=complex)
for i in range(4, 14):
    for j in range(i + 1, 14):
        T = gen(i, j); Cas10 += T @ T
C10 = W.conj().T @ Cas10 @ W; C10 = 0.5 * (C10 + C10.conj().T)
ev10, U10 = np.linalg.eigh(C10)
sec16 = W @ U10[:, np.abs(ev10 - ref16) < 1e-3]

SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
ASD = [(0, 1, 3, 2), (0, 2, 1, 3), (0, 3, 2, 1)]
Jplus = [gen(a, b) + gen(c, d) for (a, b, c, d) in SD]
Jminus = [gen(a, b) + gen(c, d) for (a, b, c, d) in ASD]
Jdiag = [Jplus[k] - Jminus[k] for k in range(3)]   # diagonal closes as J+ - J- (opposite structure constants)

def content(J3):
    c = (np.trace((J3[0] @ J3[1] - J3[1] @ J3[0]).conj().T @ J3[2]) / np.trace(J3[2].conj().T @ J3[2])).real
    Cas = -(J3[0] @ J3[0] + J3[1] @ J3[1] + J3[2] @ J3[2])
    M = sec16.conj().T @ Cas @ sec16; M = 0.5 * (M + M.conj().T)
    ev = np.linalg.eigvalsh(M)
    k = c * c   # Casimir eigenvalue = c^2 * j(j+1)
    spins = Counter()
    for x in ev:
        j = (-1 + np.sqrt(1 + 4 * max(x.real / k, 0))) / 2
        spins[round(j * 2) / 2] += 1
    return c, spins

print(f"16/16bar generation sector dim in ker = {sec16.shape[1]} (= 32 x multiplicity-space dim 16)\n")
for name, J in [("self-dual su(2)+", Jplus), ("anti-self-dual su(2)-", Jminus), ("diagonal/vector su(2)", Jdiag)]:
    c, sp = content(J)
    clean = all(abs(sp[j] / (2 * j + 1) - round(sp[j] / (2 * j + 1))) < 1e-6 for j in sp)
    mult = {float(j): round(sp[j] / (2 * j + 1) / 32, 3) for j in sorted(sp)}     # mult-space irrep counts
    odd = [float(j) for j in sorted(sp) if int(round(2 * j + 1)) % 2 == 1 and j > 0 and sp[j] > 0]
    print(f"{name:22s} [J0,J1]={c:+.1f}J2 (clean su(2): {clean}) | mult-space {{j:count}}: {mult} | odd j: {odd if odd else 'NONE'}")
    assert clean
print("\nsu(3) family symmetry commuting with Spin(10): dim su(3)=8 > dim so(4)=6 => cannot embed.")
print("Conclusion: only self-dual/anti-self-dual su(2) give an odd generation multiplicity, always the "
      "triplet 3; never 5 or higher; no su(3). Leg 3 closed for the commutes-with-Spin(10) case.")
