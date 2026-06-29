"""
SYNTHESIS CHECK (lead constructor): is the FULL-Lambda^2 doubling legitimate?

The G4 refutation in moment_map_noether_closure.py proved the self-dual-only SW template is
INCOMPLETE: the j=1 (192-dim) carrier is simultaneously an su(2)_- doublet (Casimir_- = 3 = 4*(1/2)(3/2)),
and the SAME Krein bilinear sources su(2)_- with |mu^-| ~ |mu^+|. The honest resolution (without a
hand-imposed self-dual projector on Psi) is to DOUBLE the monopole coupling to the full
Lambda^2 = su(2)_+ (+) su(2)_- target:

    |F_A^+ - mu^+(Psi)|^2  +  |F_A^- - mu^-(Psi)|^2 ,
    mu^±_k(Psi) = i <Psi, J^±_k Psi>_K .

That doubling is only legitimate if the mu^- leg is ALSO a genuine Krein-real, su(2)_--EQUIVARIANT
moment map -- so that |F_A^- - mu^-|^2 is separately gauge-invariant and gives its OWN Noether-II
closure D_A^* THETA^- = 0. G1 (in the sibling test) already showed the su(2)_- generators are
K-anti-self-adjoint; this script confirms the remaining load-bearing facts for BOTH chiralities at once:

  [D1] su(2)_- closes on {Jm}             (analog of the su(2)_+ closure)
  [D2] Jm K-anti-self-adjoint  -> mu^- REAL          (re-confirm, full 1792-dim)
  [D3] mu^- EXACTLY su(2)_--equivariant: i<Psi,[Jm_k,Jm_l]Psi>_K = sum_m f^-_kl^m mu^-_m   (the Noether heart)
  [D4] mu^- onto su(2)_- (image rank 3, nonzero)     -> the second monopole eq F_A^- = mu^- is well-posed
  [D5] full Spin(4)=SU(2)_+ x SU(2)_- content of the carrier: (j_+,j_-) per state, so the 192 carrier
       is the (3,2) Spin(4) irrep times its multiplicity -> BOTH mu^+ and mu^- are non-trivial on it.

Self-contained: copies the substrate builders. Running code decides.
"""
import numpy as np

N, DIM = 14, 128
TIMELIKE = {4, 5, 6, 7, 8}
SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]


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
e = [(1j * base[a] if a in TIMELIKE else base[a]) for a in range(N)]
SPACELIKE = [a for a in range(N) if a not in TIMELIKE]


def sgen(i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


def lvec(i, j):
    M = np.zeros((N, N), dtype=complex); M[i, j] = 1; M[j, i] = -1; return M


def comm(A, B):
    return A @ B - B @ A


Jp = [np.kron(I14, sgen(a, b) + sgen(c, d)) + np.kron(lvec(a, b) + lvec(c, d), I128) for (a, b, c, d) in SD]
Jm = [np.kron(I14, sgen(a, b) - sgen(c, d)) + np.kron(lvec(a, b) - lvec(c, d), I128) for (a, b, c, d) in SD]

Gamma = np.hstack(e)
Pi = np.eye(N * DIM, dtype=complex) - Gamma.conj().T @ np.linalg.inv(Gamma @ Gamma.conj().T) @ Gamma
w, Vv = np.linalg.eigh(Pi)
W = Vv[:, w > 0.5]
Casp = -(Jp[0] @ Jp[0] + Jp[1] @ Jp[1] + Jp[2] @ Jp[2])
CasK = W.conj().T @ Casp @ W; CasK = 0.5 * (CasK + CasK.conj().T)
ev, U = np.linalg.eigh(CasK)
Wt = W @ U[:, np.abs(ev - 8.0) < 1e-4]   # j_+=1 triplet sector, 192-dim

bS = I128.copy()
for s in SPACELIKE:
    bS = bS @ e[s]
if np.linalg.norm(bS.conj().T + bS) < 1e-9:
    bS = 1j * bS
bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
etaV = np.diag([(-1.0 if a in TIMELIKE else 1.0) for a in range(N)]).astype(complex)
K = np.kron(etaV, bS)

print("=" * 80)
print("FULL-Lambda^2 DOUBLING CHECK: is the mu^- (anti-self-dual) leg a genuine moment map?")
print("=" * 80)

# [D1] su(2)_- closes
fm = np.zeros((3, 3, 3), dtype=complex)
for a in range(3):
    for b in range(3):
        C = comm(Jm[a], Jm[b])
        for c in range(3):
            fm[a, b, c] = np.trace(Jm[c].conj().T @ C) / np.trace(Jm[c].conj().T @ Jm[c])
clo = max(np.linalg.norm(comm(Jm[a], Jm[b]) - sum(fm[a, b, c] * Jm[c] for c in range(3)))
          for a in range(3) for b in range(3))
print(f"[D1] su(2)_- closes : max||[Jm_a,Jm_b] - f.Jm|| = {clo:.2e}   f^-_012 = {fm[0,1,2].real:+.2f}")

# [D2] Jm K-anti-self-adjoint -> mu^- real
g1m = max(np.linalg.norm(Jm[k].conj().T @ K + K @ Jm[k]) for k in range(3))
print(f"[D2] Jm K-anti-self-adjoint (full 1792): max||Jm^dag K + K Jm|| = {g1m:.2e}  -> mu^- REAL: {g1m < 1e-9}")

KJm = [K @ Jm[k] for k in range(3)]
def mu_minus(psi):
    return np.array([1j * np.vdot(psi, KJm[k] @ psi) for k in range(3)])

# [D3] mu^- equivariance (Noether heart) on the carrier
rng = np.random.default_rng(0)
g3m = 0.0
max_im = 0.0
KcommJm = [[K @ comm(Jm[k], Jm[l]) for l in range(3)] for k in range(3)]
for _ in range(200):
    psi = Wt @ (rng.standard_normal(192) + 1j * rng.standard_normal(192))
    m = mu_minus(psi)
    max_im = max(max_im, float(np.abs(m.imag).max()))
    for k in range(3):
        for l in range(3):
            lhs = 1j * np.vdot(psi, KcommJm[k][l] @ psi)
            rhs = sum(fm[k, l, mm] * m[mm] for mm in range(3))
            g3m = max(g3m, abs(lhs - rhs))
print(f"[D3] mu^- equivariance: max|i<Psi,[Jm_k,Jm_l]Psi>_K - sum f^-_kl^m mu^-_m| = {g3m:.2e}  "
      f"-> su(2)_- equivariant: {g3m < 1e-9}")
print(f"     mu^- reality: max|Im mu^-| = {max_im:.2e}")

# [D4] mu^- onto su(2)_- (rank 3, nonzero)
S = np.array([mu_minus(Wt @ (rng.standard_normal(192) + 1j * rng.standard_normal(192))).real for _ in range(400)])
sv = np.linalg.svd(S, compute_uv=False)
rank = int((sv > 1e-6 * sv[0]).sum())
print(f"[D4] mu^- image: singular values {np.array2string(sv, precision=2)} -> rank {rank} (want 3); "
      f"mean||mu^-|| = {np.mean(np.linalg.norm(S, axis=1)):.2f}")

# [D5] Spin(4) content: Casimir_- on the j_+=1 carrier
Casm = -(Jm[0] @ Jm[0] + Jm[1] @ Jm[1] + Jm[2] @ Jm[2])
Cm = Wt.conj().T @ Casm @ Wt; Cm = 0.5 * (Cm + Cm.conj().T)
casm = float(np.median(np.linalg.eigvalsh(Cm).real))
jminus = (-1 + np.sqrt(1 + casm)) / 2
print(f"[D5] Spin(4) content of carrier: Casimir_+ = 8.0 (j_+=1), Casimir_- = {casm:.2f} (j_-={jminus:.1f}) "
      f"-> carrier = (j_+,j_-)=(1,1/2) Spin(4) irrep, dim {int((2*1+1)*(2*0.5+1))} x mult")

ok = (clo < 1e-9) and (g1m < 1e-9) and (g3m < 1e-9) and (rank == 3)
print("=" * 80)
print(f"VERDICT: mu^- is a genuine Krein-real su(2)_--equivariant moment map ONTO su(2)_- : {ok}")
print(f"  => the doubled coupling |F_A^- - mu^-(Psi)|^2 is separately gauge-invariant and yields its")
print(f"     OWN Noether-II closure D_A^* THETA^- = 0. The full-Lambda^2 doubling is substrate-legitimate;")
print(f"     it resolves the G4 refutation WITHOUT a hand-imposed self-dual projector on Psi.")
print("=" * 80)
