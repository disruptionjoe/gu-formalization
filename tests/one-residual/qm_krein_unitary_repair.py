#!/usr/bin/env python3
"""
ONE-RESIDUAL, Sec. 2.3 (Quantum structure / unitarity) -- EXISTENCE grade.

CLAIM (re-landed as a reproducible in-repo test):
  On the cross-chirality Krein form K of the 192-dim generation triplet carrier
  (signature (+96, -96, 0); purely cross-chirality relative to a chirality
  involution Gamma_c), a UNITARY REPAIR EXISTS:
    (A) a MAXIMAL positive-definite physical subspace P (dim 96, the maximum a
        signature-(96,96) form admits) whose restricted Krein form is strictly
        positive-definite -- min eigenvalue of P^dag K P > 0; and
    (B) a nontrivial Krein-unitary generator S with  S^dag K S = K.
  Moreover the repair is genuine unitary QM: a Krein-unitary that preserves P
  restricts on P to an ordinary (Hilbert-space) unitary.

WHAT IS AND IS NOT ESTABLISHED.
  This is an EXISTENCE clear: it certifies, by explicit construction and machine
  verification, that the structure the paper asserts (P and S) provably exists on
  a FAITHFUL model of the cross-chirality Krein form -- a Hermitian involution K,
  K^2 = I, signature (96,96), purely cross-chirality (the K_++ and K_-- chirality
  blocks vanish, i.e. the chirality eigenspaces are K-Lagrangian), matching the
  structure certified independently in tests/antilinear-bound/. It is NOT a
  derivation that GU forces this Krein form, and NOT a physics prediction; the
  generalized-Born-rule quantization layer is imported (paper Sec. 2.3, 7).

NON-CIRCULARITY. Nothing is asserted that is not computed. The signature (96,96)
  is READ from the eigenvalues of K (not stamped on it). The cross-chirality
  structure is a CONSEQUENCE of building K from an off-diagonal unitary block, and
  is verified after the fact. P is the actual positive eigenspace (extracted by
  eigendecomposition); its positive-definiteness is measured. S = expm(i H) with H
  independently constructed to be K-self-adjoint; S^dag K S = K is measured, not
  imposed. The seed makes the (arbitrary) unitary coupling reproducible; the result
  does not depend on it (the construction is generic).

Deterministic (seeded). numpy + scipy only. Prints PASS/FAIL; exits 0 iff all pass.
"""

import numpy as np
from scipy.linalg import expm

rng = np.random.default_rng(20260711)
TOL = 1e-10
N = 96              # per-chirality dimension
DIM = 2 * N         # 192-dim generation triplet carrier

_fail = 0
def check(cond, msg):
    global _fail
    print(("  PASS  " if cond else "  FAIL  ") + msg)
    if not cond:
        _fail += 1

def rand_unitary(n):
    """Haar-ish unitary via QR of a complex Gaussian."""
    z = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    q, r = np.linalg.qr(z)
    # fix phases so q is genuinely unitary and deterministic
    ph = np.diag(r) / np.abs(np.diag(r))
    return q * ph.conj()

print("=" * 70)
print("ONE-RESIDUAL 2.3 -- cross-chirality Krein form: unitary repair EXISTS")
print("=" * 70)

# ---------------------------------------------------------------------------
# FAITHFUL MODEL of the cross-chirality Krein form.
# Chirality basis: first N coords = W_+, last N = W_-.  Gamma_c = diag(+I, -I).
# A purely cross-chirality Hermitian form couples ONLY W_+ <-> W_-:
#     K = [[0, A], [A^dag, 0]]  with A in U(N).
# Then K^dag = K, and K^2 = diag(A A^dag, A^dag A) = I  (A unitary) => involution;
# eigenvalues of K are the +/- singular values of A = +/-1 each with mult N
# => signature (96,96).  All of this is VERIFIED below, not assumed.
# ---------------------------------------------------------------------------
A = rand_unitary(N)
K = np.zeros((DIM, DIM), dtype=complex)
K[:N, N:] = A
K[N:, :N] = A.conj().T
Gc = np.diag(np.concatenate([np.ones(N), -np.ones(N)])).astype(complex)

print("\n--- PART A: K is a faithful cross-chirality Krein form ---")
check(np.allclose(K, K.conj().T, atol=TOL), "K is Hermitian (K = K^dag)")
check(np.allclose(K @ K, np.eye(DIM), atol=TOL), "K is an involution (K^2 = I)")

kev = np.linalg.eigvalsh(K)
npos = int((kev > 1e-8).sum()); nneg = int((kev < -1e-8).sum())
nzero = DIM - npos - nneg
print(f"    Krein spectrum: (+{npos}, -{nneg}, {nzero})  [read from eigenvalues]")
check((npos, nneg, nzero) == (96, 96, 0), "signature is EXACTLY (+96, -96, 0)")

# purely cross-chirality: chirality blocks of K vanish
Pp = (np.eye(DIM) + Gc) / 2      # projector onto W_+
Pm = (np.eye(DIM) - Gc) / 2      # projector onto W_-
kpp = np.max(np.abs(Pp @ K @ Pp))
kmm = np.max(np.abs(Pm @ K @ Pm))
print(f"    same-chirality blocks: ||K_++|| = {kpp:.1e}, ||K_--|| = {kmm:.1e}")
check(kpp < TOL and kmm < TOL,
      "K purely cross-chirality (W_+/- are K-Lagrangian)")
check(np.allclose(K @ Gc, -Gc @ K, atol=TOL),
      "K anticommutes with chirality: K Gamma_c = -Gamma_c K")

# a chirality eigenspace is K-null, hence CANNOT be the positive-definite sector:
wplus = np.eye(DIM)[:, :N]                    # basis of W_+
kres_wp = wplus.conj().T @ K @ wplus
check(np.max(np.abs(kres_wp)) < TOL,
      "control: W_+ is K-isotropic (max|+chirality| forbidden as physical space)")

# ---------------------------------------------------------------------------
# PART B: the MAXIMAL positive-definite physical subspace P.
# P = positive eigenspace of K (dim = n_+ = 96 = maximal possible).
# Its columns are K-orthonormal with K-norm +1, so P^dag K P should be +I.
# ---------------------------------------------------------------------------
print("\n--- PART B: maximal positive-definite physical subspace P ---")
w, V = np.linalg.eigh(K)
P = V[:, w > 1e-8]                             # 192 x 96
check(P.shape[1] == 96, "dim P = 96 (maximal for signature (96,96))")

Krestrict = P.conj().T @ K @ P
Krestrict = 0.5 * (Krestrict + Krestrict.conj().T)
min_eig = np.linalg.eigvalsh(Krestrict).min()
print(f"    min eigenvalue of restricted form  P^dag K P  = {min_eig:.6f}")
check(min_eig > 0, "restricted Krein form on P is POSITIVE-DEFINITE (min eig > 0)")
check(np.allclose(Krestrict, np.eye(96), atol=TOL),
      "P^dag K P = I_96 (P is a K-orthonormal physical frame)")

# P genuinely MIXES chirality (it is a 'diagonal' of W_+ and W_-, not either one):
chi_content = P.conj().T @ Gc @ P             # induced chirality on P
offdiag = chi_content - np.diag(np.diag(chi_content))
check(np.max(np.abs(np.diag(chi_content))) < 0.5,
      "P is chirality-balanced (no pure-chirality direction survives)")

# ---------------------------------------------------------------------------
# PART C: a nontrivial Krein-unitary generator S with S^dag K S = K.
# H is K-self-adjoint  <=>  H^dag = K H K  (since K^{-1}=K).  Build such an H
# from an arbitrary matrix X via H = (X + K X^dag K)/2, then S = expm(i H).
# Then S^dag K S = exp(-i H^dag) K exp(i H) = K exp(-i H) exp(i H) = K.
# ---------------------------------------------------------------------------
print("\n--- PART C: nontrivial Krein-unitary generator S (S^dag K S = K) ---")
X = rng.standard_normal((DIM, DIM)) + 1j * rng.standard_normal((DIM, DIM))
H = 0.5 * (X + K @ X.conj().T @ K)
# scale to a moderate rapidity so S is a well-conditioned finite Krein boost
# (a K-self-adjoint H is non-Hermitian, so exp(iH) grows exponentially in ||H||;
#  the K-unitarity IDENTITY is exact regardless of scale -- we keep ||S|| modest
#  purely so the ABSOLUTE residual is a fair measure of it).
H = 0.6 * H / np.linalg.norm(H, 2)
check(np.allclose(H.conj().T, K @ H @ K, atol=TOL),
      "generator H is K-self-adjoint (H^dag = K H K)")

S = expm(1j * H)
resid = np.max(np.abs(S.conj().T @ K @ S - K)) / np.max(np.abs(K))
print(f"    ||S^dag K S - K||_max (rel) = {resid:.2e},  ||S||_2 = {np.linalg.norm(S,2):.3f}")
check(resid < 1e-9, "S is KREIN-UNITARY (S^dag K S = K)")
check(np.max(np.abs(S - np.eye(DIM))) > 1e-2, "S is nontrivial (S != I)")
# genuine non-compact element: an ordinary unitary would have S^dag S = I.
nonunitary = np.max(np.abs(S.conj().T @ S - np.eye(DIM)))
print(f"    ||S^dag S - I||_max = {nonunitary:.2e}  (>0 => genuine Krein boost, not ordinary U)")
check(nonunitary > 1e-2, "S is a genuine U(96,96) element (not merely unitary)")

# ---------------------------------------------------------------------------
# PART D: the REPAIR is unitary QM -- a Krein-unitary preserving P restricts on
# P to an ordinary unitary.  Take H_P block-diagonal in the K-eigenbasis
# (Hermitian block h_+ on P, h_- on P^perp): such H_P is K-self-adjoint AND
# leaves P invariant, so S_P = expm(i H_P) is Krein-unitary and its restriction
# to the K-orthonormal frame P is an ordinary unitary.
# ---------------------------------------------------------------------------
print("\n--- PART D: unitary QM recovered on the physical sector ---")
Pm_space = V[:, w < -1e-8]                     # negative eigenspace, dim 96
Q = np.hstack([P, Pm_space])                   # full K-eigenbasis
hp = rng.standard_normal((96, 96)) + 1j * rng.standard_normal((96, 96))
hp = 0.5 * (hp + hp.conj().T)                  # Hermitian on P
hm = rng.standard_normal((96, 96)) + 1j * rng.standard_normal((96, 96))
hm = 0.5 * (hm + hm.conj().T)                  # Hermitian on P^perp
Hblk = np.zeros((DIM, DIM), dtype=complex)
Hblk[:96, :96] = hp
Hblk[96:, 96:] = hm
H_P = Q @ Hblk @ Q.conj().T                    # back to ambient basis
check(np.allclose(H_P.conj().T, K @ H_P @ K, atol=TOL),
      "P-preserving generator H_P is K-self-adjoint")

S_P = expm(1j * H_P)
check(np.max(np.abs(S_P.conj().T @ K @ S_P - K)) < 1e-9,
      "S_P is Krein-unitary")
# does S_P preserve P?  measure leakage of S_P(P) into P^perp.
leak = np.max(np.abs(Pm_space.conj().T @ K @ (S_P @ P)))
print(f"    leakage of S_P(P) into P^perp = {leak:.2e}")
check(leak < 1e-9, "S_P preserves the physical subspace P")
# restriction of S_P to the K-orthonormal frame P is an ordinary unitary:
u = P.conj().T @ S_P @ P
unit_err = np.max(np.abs(u.conj().T @ u - np.eye(96)))
print(f"    ||u^dag u - I||_max on P = {unit_err:.2e}")
check(unit_err < 1e-9,
      "restriction to P is an ORDINARY unitary => unitary QM recovered")

print("\n" + "=" * 70)
if _fail == 0:
    print("RESULT: PASS -- unitary repair EXISTS on the cross-chirality Krein form.")
    print("  (A) maximal positive-definite physical subspace P (dim 96, min eig 1)")
    print("  (B) nontrivial Krein-unitary generator S (S^dag K S = K)")
    print("  (D) Krein-unitary preserving P restricts to ordinary unitary QM on P")
    print("  GRADE: EXISTENCE (structure provably exists on a faithful model).")
else:
    print(f"RESULT: FAIL -- {_fail} check(s) failed.")
print("=" * 70)

raise SystemExit(0 if _fail == 0 else 1)
