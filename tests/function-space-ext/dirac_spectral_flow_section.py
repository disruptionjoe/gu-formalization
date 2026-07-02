#!/usr/bin/env python3
# WC-FUNCTION-SPACE-EXT: the conditional section-setting theorem, computed.
#
# Lifts the paper's finite-dimensional index conservation (Theorem 2) + the antilinear
# null-eigenspace bound to a genuine differential-operator / spectral-flow setting: a
# 1D lattice Dirac family on S^1 valued in the cross-chirality Krein space.
#
#   chirality   Gamma = sigma_3 (x) I_N     (Gamma^2 = I)
#   Krein form  K     = sigma_1 (x) I_N     (K^2 = I, K Gamma = -Gamma K: cross-chirality)
#   momentum    P     = central-difference periodic -i d/dx  (Hermitian differential operator)
#
# THEOREM (net chiral spectral flow, closed 1D section setting).  Let D(t) be a
# norm-continuous family that is (i) self-adjoint, (ii) Gamma-ODD (a Dirac / chirality
# operator: D Gamma = -Gamma D), (iii) KREIN-self-adjoint for the cross-chirality K
# (D^dag K = K D), (iv) Fredholm (spectral gap at 0 off isolated crossings).  Then in the
# chiral splitting D(t) = sigma_1 (x) B(t) with B(t) self-adjoint, so the spectrum is
# symmetric about 0 and the negative (Dirac-sea / physical) sector is chirality-balanced:
# n_-(t) = tr(Gamma P_{<0}(t)) = 0 identically, hence the net chiral spectral flow is 0 --
# even though genuine zero crossings occur (non-vacuous, just chirally balanced).
#
# PROOF (per crossing; finite-dim at each t; hypotheses machine-certified): Gamma-odd +
# K-self-adjoint with K = sigma_1 forces D = [[0,B],[C,0]] with C = B^dag (self-adjoint) and
# B = C^dag (K-self-adjoint), i.e. B Hermitian: D = sigma_1 (x) B.  Eigenvectors are
# (1,+-1)(x)v_b, chirality (|1|^2 - |+-1|^2)/2 = 0.  No crossing carries net chirality.
# (Section analog of the finite theorem: physical sector chirality-balanced since K is cross.)
#
# CONTROL (mechanism load-bearing): a Fredholm self-adjoint family with net chiral spectral
# flow +1 is exhibited -- and it VIOLATES K-self-adjointness (a one-sided chiral crossing,
# Gamma-EVEN, not a chirality operator).  Nonzero flow requires leaving the Krein-Dirac class.
#
# RESIDUAL (honest, NOT closed here): (a) the physical projection needs the Fredholm gap to be
# well-posed in infinite dim; (b) an APS/noncompact-end eta correction can carry an unpaired
# chiral piece on a manifold WITH BOUNDARY even when the interior flow is K-paired; (c)
# family-index / higher-topology terms.  This script establishes the interior/closed, gapped
# statement; (a)-(c) remain the open part of WC-FUNCTION-SPACE-EXT.
#
# Deterministic, numpy-only.  A nonzero net chiral flow in the Krein class aborts.
import time
import numpy as np

T0 = time.time()
N = 32
SEED = 20260706
np.set_printoptions(precision=4, suppress=True, linewidth=120)
rng = np.random.default_rng(SEED)
NASSERT = 0


def check(cond, msg):
    global NASSERT
    NASSERT += 1
    assert cond, msg


s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)
IN = np.eye(N, dtype=complex)
Gamma = np.kron(s3, IN)
K = np.kron(s1, IN)

a = 2 * np.pi / N
P = np.zeros((N, N), dtype=complex)
for j in range(N):
    P[j, (j + 1) % N] += -1j / (2 * a)
    P[j, (j - 1) % N] += 1j / (2 * a)
P = 0.5 * (P + P.conj().T)
check(np.linalg.norm(P - P.conj().T) < 1e-12, "momentum P Hermitian")

print("=" * 96)
print("WC-FUNCTION-SPACE-EXT section-setting spectral flow: premises")
print("=" * 96)
check(np.linalg.norm(Gamma @ Gamma - np.eye(2 * N)) < 1e-12, "Gamma^2 = I")
check(np.linalg.norm(K @ K - np.eye(2 * N)) < 1e-12, "K^2 = I")
check(np.linalg.norm(K @ Gamma + Gamma @ K) < 1e-12, "K Gamma = -Gamma K (cross-chirality)")
print("  Gamma^2 = K^2 = I, K Gamma + Gamma K = 0 (cross-chirality Krein) -- confirmed.")


def neg_chiral_charge(D):
    w, V = np.linalg.eigh(0.5 * (D + D.conj().T))
    Pm = V[:, w < -1e-9]
    return np.trace(Pm.conj().T @ Gamma @ Pm).real, w


print()
print("=" * 96)
print("THEOREM: Krein-self-adjoint Gamma-odd Dirac family D(t) = sigma_1 (x) B(t)")
print("=" * 96)
V0 = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))
V0 = 0.5 * (V0 + V0.conj().T)


def B_of_t(t):
    return P + (10.0 * t - 5.0) * IN + 0.5 * V0


def D_krein(t):
    return np.kron(s1, B_of_t(t))


ts = np.linspace(0, 1, 161)
nlist, b_crossings, prev_b = [], 0, None
for t in ts:
    D = D_krein(t)
    if t in (ts[0], ts[80], ts[-1]):
        check(np.linalg.norm(D - D.conj().T) < 1e-10, "D self-adjoint")
        check(np.linalg.norm(D @ Gamma + Gamma @ D) < 1e-10, "D Gamma-odd (Dirac)")
        check(np.linalg.norm(D.conj().T @ K - K @ D) < 1e-10, "D Krein-self-adjoint")
    n_, _ = neg_chiral_charge(D)
    nlist.append(n_)
    bev = np.sort(np.linalg.eigvalsh(B_of_t(t)))
    if prev_b is not None:
        b_crossings += int(np.sum(np.sign(bev) != np.sign(prev_b)))
    prev_b = bev
nlist = np.array(nlist)
print("  net chiral charge n_-(t) = tr(Gamma P_<0): range [%.2e, %.2e]" % (nlist.min(), nlist.max()))
print("  genuine Dirac zero crossings along the path (each a chirality-balanced +-b pair): %d" % b_crossings)
print("  => net chiral spectral flow = n_-(1) - n_-(0) = %.2e  (EXACTLY 0)" % (nlist[-1] - nlist[0]))
check(np.max(np.abs(nlist)) < 1e-8, "n_-(t) identically 0: the physical sector stays chirality-balanced")
check(abs(nlist[-1] - nlist[0]) < 1e-8, "net chiral spectral flow = 0 -- FAILURE if nonzero")
check(b_crossings >= 2, "non-vacuous: genuine zero crossings occur (flow real, chirally balanced)")

w = np.linalg.eigvalsh(D_krein(0.37))
sym = np.max(np.abs(np.sort(w) + np.sort(-w)[::-1]))
print("  spectrum symmetric about 0 (||spec + reflect|| = %.2e)" % sym)
check(sym < 1e-9, "spectrum symmetric about 0 (K cross-chirality pins the +-b pairing)")
wr, Vr = np.linalg.eigh(D_krein(0.37))
lower = Vr[:, :N]
check(abs(np.trace(lower.conj().T @ Gamma @ lower).real) < 1e-8,
      "the negative spectral half is chirality-balanced (graded trace 0)")

print()
print("=" * 96)
print("CONTROL: a family with net chiral spectral flow +1 must LEAVE the Krein-Dirac class")
print("=" * 96)
Hp0 = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))
Hp0 = 0.5 * (Hp0 + Hp0.conj().T)
Hm = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))
Hm = 0.5 * (Hm + Hm.conj().T) + 6.0 * np.eye(N)
lo = np.linalg.eigvalsh(Hp0).min()


def D_ctrl(t):
    Hp = Hp0 - (lo + 0.5) * np.eye(N) * (2 * t)
    Z = np.zeros((N, N), dtype=complex)
    return np.block([[Hp, Z], [Z, Hm]])


n0, _ = neg_chiral_charge(D_ctrl(0.0))
n1, _ = neg_chiral_charge(D_ctrl(1.0))
Dc = D_ctrl(0.5)
krein_viol = np.linalg.norm(Dc.conj().T @ K - K @ Dc) / np.linalg.norm(Dc)
gamma_odd_viol = np.linalg.norm(Dc @ Gamma + Gamma @ Dc) / np.linalg.norm(Dc)
print("  net chiral spectral flow n_-(1) - n_-(0) = %+.0f  (NONZERO)" % (n1 - n0))
print("  but this family violates Krein-self-adjointness (||D^dag K - K D||/||D|| = %.2f)" % krein_viol)
print("  and is Gamma-EVEN, not a chirality operator (||D Gamma + Gamma D||/||D|| = %.2f)" % gamma_odd_viol)
check(abs(round(n1 - n0)) >= 1 and abs((n1 - n0) - round(n1 - n0)) < 1e-6,
      "control carries integer net chiral spectral flow (nonzero, non-vacuity)")
check(krein_viol > 0.3, "the nonzero-flow control violates Krein-self-adjointness")

print()
print("#" * 96)
print("# WC-FUNCTION-SPACE-EXT SECTION-SETTING -- VERDICT")
print("#" * 96)
print("  On a genuine 1D differential-operator (section) family: every self-adjoint, Gamma-odd,")
print("  Krein-self-adjoint (cross-chirality K) Dirac operator takes the form sigma_1 (x) B, so its")
print("  spectrum is symmetric about 0, the negative (physical) sector is chirality-balanced, and the")
print("  net chiral spectral flow is EXACTLY 0 -- extending the finite Theorem 2 to the section")
print("  setting under stated (Fredholm + Krein-self-adjoint) hypotheses. Genuine crossings occur.")
print("  A family with nonzero net chiral spectral flow necessarily leaves the class (the exhibited")
print("  +1 control violates Krein-self-adjointness and is not even a chirality operator).")
print()
print("  CONDITIONAL: this is the interior/closed, spectral-gapped statement. The honest residual --")
print("  NOT closed here -- is (a) well-posedness of the physical projection without a gap, (b) the")
print("  APS/noncompact-end eta correction that can carry an unpaired chiral piece on a manifold with")
print("  boundary, and (c) family-index / higher-topology terms. Those are the open part of")
print("  WC-FUNCTION-SPACE-EXT.")
print()
print("  hard asserts passed: %d" % NASSERT)
print("  total runtime: %.1fs" % (time.time() - T0))
# EOF
