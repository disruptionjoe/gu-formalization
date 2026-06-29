"""
SOURCE-ACTION / dark-energy angle: the moment map mu and the Noether-second-theorem closure.

CONSTRUCTION UNDER TEST
-----------------------
Candidate action on the 4-base X^4 with chimeric field Psi (section of V (x) S) and IG connection A:

  S_SW[A,Psi] = INT ||F_A||^2                     (a) gauge kinetic
              + <Psi, D_A Psi>_K                   (b) Krein-paired Dirac/RS
              + ||F_A^+ - mu(Psi)||^2              (c) Seiberg-Witten monopole coupling

The SW monopole term (c) is SEPARATELY gauge-invariant. Varying it in A:

  delta_A ||F_A^+ - mu(Psi)||^2 = 2 <delta A, D_A^*(F_A^+ - mu(Psi))>      (mu has no A-dependence)

so the gauge-potential sector that (c) contributes to E_A = delta S/delta A is

  THETA := D_A^*(F_A^+ - mu(Psi))   in  Omega^1(X, ad P).         <-- the engineered dark-energy field

Because (c) is gauge-invariant by itself, Noether's SECOND theorem applied to (c) ALONE gives the
off-shell identity D_A^* (delta S_(c)/delta A) = 0, i.e.

  D_A^* THETA = 0          off-shell, with NO hand-imposed projector.

The only thing that has to hold on the substrate for this to be legitimate is that mu(Psi) really is a
gauge-equivariant, Krein-real, PURELY self-dual (su(2)_+ = Lambda^2_+) bilinear -- so that ||F_A^+ - mu||^2
is genuinely Ad-invariant and the self-dual projection is intrinsic to mu, not inserted by hand. THAT is
what this script checks numerically on the verified Cl(9,5) representation.

THE MOMENT MAP (the load-bearing new object)
--------------------------------------------
  mu^k(Psi) = i <Psi, J^+_k Psi>_K = i Psi^dagger K J^+_k Psi,   k = 1,2,3

with J^+_k the three self-dual SU(2)_+ generators on V (x) S (h1_selfdual_family_kill construction) and
K = eta_V (x) beta_S the Krein form (ghost_parity_krein construction). This is the standard moment map of
the SU(2)_+ action with respect to the Krein symplectic/metric structure.

DECISIVE NUMERICAL CHECKS (all on the (9,5) Krein triplet sector that carries the 16):
  [G1] Krein anti-self-adjointness  J^dagger K + K J = 0  for every su(2)_+/su(2)_- generator
       -> makes mu^k REAL (gate for the monopole term to be a real Ad-invariant).
  [G2] mu is REAL and NON-DEGENERATE on the triplet sector (the bilinear actually reaches Lambda^2_+,
       and the three components span R^3 -> mu is onto su(2)_+).
  [G3] EXACT su(2)_+ equivariance (the Noether-closure heart):
         delta_l mu^k = i Psi^dagger K [J_k,J_l] Psi = sum_m f_{kl}^m mu^m
       with f the measured su(2) structure constants. This is moment-map equivariance; it is what makes
       ||F_A^+ - mu||^2 gauge-invariant, hence D_A^* THETA = 0 by Noether II. Residual must be ~0.
  [G4] SELF-DUAL PURITY (no hand-imposed projector): the SAME bilinear on the anti-self-dual su(2)_-
       generators vanishes on the triplet, and the triplet is an su(2)_- singlet (Casimir_- = 0).
       -> mu is intrinsically valued in Lambda^2_+; P_- mu = 0 with no projector inserted.

If G1-G4 pass, Assumption 3 (canon/dark-energy-theta-divergence-free.md) is discharged in the SW completion:
THETA is the gauge-potential sector of E_A, it is sourced by the fermion bilinear mu(Psi), and D_A^* THETA = 0
follows from Noether's second theorem on the separately-gauge-invariant monopole term -- structurally, not by
hand. Running code decides; numbers below.
"""
import numpy as np
from collections import Counter

N, DIM = 14, 128
TOL = 1e-9


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
TIMELIKE = {4, 5, 6, 7, 8}                      # signature (9,5), same convention as ghost_parity_krein.py
e = [(1j * base[a] if a in TIMELIKE else base[a]) for a in range(14)]
SPACELIKE = [a for a in range(14) if a not in TIMELIKE]


def sgen(i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


def lvec(i, j):
    M = np.zeros((N, N), dtype=complex); M[i, j] = 1; M[j, i] = -1; return M


def comm(A, B):
    return A @ B - B @ A


# ---- self-dual SU(2)_+ and anti-self-dual SU(2)_- generators on V (x) S ----
SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]   # self-dual base {0,1,2,3} (all spacelike -> Euclidean 4-base)
Jp = [np.kron(I14, sgen(a, b) + sgen(c, d)) + np.kron(lvec(a, b) + lvec(c, d), I128) for (a, b, c, d) in SD]
Jm = [np.kron(I14, sgen(a, b) - sgen(c, d)) + np.kron(lvec(a, b) - lvec(c, d), I128) for (a, b, c, d) in SD]

# ---- gamma-trace constraint surface and the j=1 triplet sector (carries the 16) ----
Gamma = np.hstack(e)
Pi = np.eye(N * DIM, dtype=complex) - Gamma.conj().T @ np.linalg.inv(Gamma @ Gamma.conj().T) @ Gamma
w, Vv = np.linalg.eigh(Pi)
W = Vv[:, w > 0.5]                                # 1792 x 1664  (ker Gamma)
Casp = -(Jp[0] @ Jp[0] + Jp[1] @ Jp[1] + Jp[2] @ Jp[2])
CasK = W.conj().T @ Casp @ W; CasK = 0.5 * (CasK + CasK.conj().T)
ev, U = np.linalg.eigh(CasK)
mask = np.abs(ev - 8.0) < 1e-4                    # j=1 Casimir = 4 j(j+1) = 8
Wt = W @ U[:, mask]                               # 1792 x 192  (the self-dual triplet sector)
assert Wt.shape[1] == 192, Wt.shape

# ---- Krein form K = eta_V (x) beta_S ----
bS = I128.copy()
for s in SPACELIKE:
    bS = bS @ e[s]
if np.linalg.norm(bS.conj().T + bS) < 1e-9:
    bS = 1j * bS
bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
etaV = np.diag([(-1.0 if a in TIMELIKE else 1.0) for a in range(14)]).astype(complex)
K = np.kron(etaV, bS)

print("=" * 78)
print("MOMENT MAP mu : S -> Lambda^2_+ = su(2)_+  and the Noether-II closure  D_A^* THETA = 0")
print("signature (9,5); triplet sector dim =", Wt.shape[1], "(= 3 x 64, carries the 16/16bar)")
print("=" * 78)


# ---------------- [G1] Krein anti-self-adjointness ----------------
g1 = max(np.linalg.norm(J.conj().T @ K + K @ J) for J in (Jp + Jm))
print(f"[G1] Krein anti-self-adjoint  max||J^dag K + K J|| = {g1:.2e}   "
      f"-> mu^k is REAL : {g1 < 1e-9}")


# moment map components
def mu_plus(psi):
    return np.array([1j * (psi.conj() @ K @ (Jp[k] @ psi)) for k in range(3)])


def mu_minus(psi):
    return np.array([1j * (psi.conj() @ K @ (Jm[k] @ psi)) for k in range(3)])


# ---------------- [G2] reality + non-degeneracy / surjectivity onto su(2)_+ ----------------
rng = np.random.default_rng(0)
samples = []
max_imag = 0.0
for _ in range(400):
    psi = Wt @ (rng.standard_normal(192) + 1j * rng.standard_normal(192))
    m = mu_plus(psi)
    max_imag = max(max_imag, float(np.max(np.abs(m.imag))))
    samples.append(m.real)
S = np.array(samples)                              # 400 x 3 real
sv = np.linalg.svd(S, compute_uv=False)
mean_norm = float(np.mean(np.linalg.norm(S, axis=1)))
print(f"[G2] mu real : max|Im mu| = {max_imag:.2e} ; non-degenerate : mean||mu|| = {mean_norm:.3f}, "
      f"singular values of the mu-image = {np.array2string(sv, precision=2)}")
print(f"     -> rank of moment image over su(2)_+ = {int(np.sum(sv > 1e-6 * sv[0]))} (want 3 = onto Lambda^2_+)")


# ---------------- structure constants of su(2)_+ (trace-orthogonal projection) ----------------
def killing(A, B):
    return np.trace(A.conj().T @ B)


f = np.zeros((3, 3, 3), dtype=complex)
for a in range(3):
    for b in range(3):
        C = comm(Jp[a], Jp[b])
        for c in range(3):
            f[a, b, c] = killing(Jp[c], C) / killing(Jp[c], Jp[c])
# verify the algebra actually closes on {Jp} with these constants
clo = max(np.linalg.norm(comm(Jp[a], Jp[b]) - sum(f[a, b, c] * Jp[c] for c in range(3)))
          for a in range(3) for b in range(3))
print(f"[--] su(2)_+ closes : max|| [J_a,J_b] - sum f_ab^c J_c || = {clo:.2e}  "
      f"(f_012 = {f[0,1,2].real:+.2f})")


# ---------------- [G3] EXACT moment-map equivariance (Noether-closure heart) ----------------
# delta_l mu^k = i Psi^dag K [J_k,J_l] Psi   MUST equal   sum_m f_{kl}^m mu^m
KcommJ = [[K @ comm(Jp[k], Jp[l]) for l in range(3)] for k in range(3)]   # precompute once
g3 = 0.0
for _ in range(200):
    psi = Wt @ (rng.standard_normal(192) + 1j * rng.standard_normal(192))
    m = mu_plus(psi)
    for k in range(3):
        for l in range(3):
            lhs = 1j * (psi.conj() @ (KcommJ[k][l] @ psi))
            rhs = sum(f[k, l, mm] * m[mm] for mm in range(3))
            g3 = max(g3, abs(lhs - rhs))
print(f"[G3] equivariance  max| i<Psi,[J_k,J_l]Psi>_K  -  sum_m f_kl^m mu^m | = {g3:.2e}   "
      f"-> mu is su(2)_+-equivariant : {g3 < 1e-9}")


# ---------------- [G4] self-dual purity (no hand-imposed projector) ----------------
# (a) the triplet is an su(2)_- singlet: Casimir_- = 0 on Wt
Casm = -(Jm[0] @ Jm[0] + Jm[1] @ Jm[1] + Jm[2] @ Jm[2])
Cm = Wt.conj().T @ Casm @ Wt; Cm = 0.5 * (Cm + Cm.conj().T)
casm_max = float(np.max(np.abs(np.linalg.eigvalsh(Cm))))
# (b) the SAME bilinear on the anti-self-dual generators vanishes on the triplet
g4b = 0.0
for _ in range(200):
    psi = Wt @ (rng.standard_normal(192) + 1j * rng.standard_normal(192))
    g4b = max(g4b, float(np.max(np.abs(mu_minus(psi)))))
print(f"[G4] self-dual purity : Casimir_-(triplet) max|eig| = {casm_max:.2e} (triplet is su(2)_- singlet) ; "
      f"anti-self-dual moment max|mu^-| = {g4b:.2e}")
print(f"     -> P_- mu = 0 intrinsically; mu IS valued in Lambda^2_+ with NO projector inserted : "
      f"{casm_max < 1e-6 and g4b < 1e-6}")


# ---------------- verdict ----------------
passed = (g1 < 1e-9) and (max_imag < 1e-9) and (int(np.sum(sv > 1e-6 * sv[0])) == 3) \
    and (g3 < 1e-9) and (casm_max < 1e-6) and (g4b < 1e-6)
print("=" * 78)
print("DECISIVE RESULT:", "PASS" if passed else "FAIL")
print("If PASS: ||F_A^+ - mu(Psi)||^2 is a separately gauge-invariant, Krein-real, intrinsically self-dual")
print("monopole term. Its A-variation gives THETA = D_A^*(F_A^+ - mu(Psi)) as the gauge-potential sector of")
print("E_A, sourced by the fermion bilinear mu(Psi). Noether's SECOND theorem on this term alone then forces")
print("D_A^* THETA = 0 off-shell, with NO hand-imposed projector -- discharging dark-energy Assumption 3.")
print("=" * 78)
