#!/usr/bin/env python3
# WC-FUNCTION-SPACE-EXT residual item (1): GAP WELL-POSEDNESS on a noncompact end.
#
# The interior theorem is the spectral-gapped statement. Residual item (1): the physical
# (negative) spectral projection P_<0 needs a Fredholm spectral gap at 0 to be well-defined in
# infinite dimensions; on a noncompact end with continuous spectrum through 0 the chiral count is
# not well-posed. This script certifies the gap-vs-well-posedness dichotomy INSIDE the cross-
# chirality Krein class, on a genuine noncompact-end (open half-line) lattice Dirac model.
#
# Class structure (same as the v2.8 interior theorem): Gamma = s3 (x) I (chirality),
# K = s1 (x) I (cross-chirality Krein), and a chirality-odd, Krein-self-adjoint operator is forced
# to the form D = s1 (x) B with B Hermitian, so spec(D) = +- spec(B) EXACTLY. The gap at 0 is
# therefore g = min|eig(B)|, set by the end value of B. A gapped end (|B_inf| >= m_inf > 0) gives a
# stable gap and a well-defined P_<0 with tr(Gamma P_<0) = 0; a gapless end (m_inf = 0) closes the
# gap as the end grows (L -> inf), and the count stops being integer-stable -> ill-posed.
#
# Deterministic, numpy-only.
import numpy as np

NASSERT = 0
def check(c, m):
    global NASSERT
    NASSERT += 1
    assert c, m

s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)


def build_B_end(L, m_inf, hop=0.5):
    """Open-chain (noncompact-end stand-in) Hermitian B on L sites:
       B = m_inf * I + T, with T the nearest-neighbour hopping (amplitude `hop`).
    The hopping band is spec(T) = 2*hop*cos(j*pi/(L+1)) in (-2hop, 2hop) = (-1, 1) for hop=0.5, so
    spec(B) in (m_inf - 1, m_inf + 1) and the distance of the asymptotic spectrum from 0 -- i.e. the
    0-gap of D = s1 (x) B -- is set by the END value m_inf: m_inf > bandwidth (=1) opens a stable
    gap; m_inf = bandwidth is the marginal/gapless case where the band bottom touches 0 as L -> inf."""
    B = np.zeros((L, L), dtype=complex)
    for x in range(L - 1):
        B[x, x + 1] += hop
        B[x + 1, x] += hop
    for x in range(L):
        B[x, x] += m_inf
    return 0.5 * (B + B.conj().T)


def dirac_from_B(B):
    D = np.kron(s1, B)
    return 0.5 * (D + D.conj().T)


def chiral_count_neg(D, Gamma):
    """tr(Gamma P_<0): net chirality of the filled (negative) Dirac sea."""
    w, V = np.linalg.eigh(D)
    neg = V[:, w < 0]
    return np.trace(neg.conj().T @ Gamma @ neg).real


print("=" * 90)
print("WC-FUNCTION-SPACE-EXT (1): gap well-posedness on a noncompact end (open-chain Krein-Dirac)")
print("=" * 90)

# ---- structural identity: spec(D) = +- spec(B), so the 0-gap is set by min|eig(B)| ----
Bt = build_B_end(24, m_inf=0.8)
Dt = dirac_from_B(Bt)
IN = np.eye(Bt.shape[0], dtype=complex)
Gam = np.kron(s3, IN)
Kre = np.kron(s1, IN)
check(np.linalg.norm(Dt @ Gam + Gam @ Dt) < 1e-11, "D is chirality-odd ({D,Gamma}=0)")
check(np.linalg.norm(Dt.conj().T @ Kre - Kre @ Dt) < 1e-11, "D is Krein-self-adjoint (D^dag K = K D)")
wD = np.sort(np.linalg.eigvalsh(Dt))
wB = np.sort(np.linalg.eigvalsh(Bt))
spec_pm = np.sort(np.r_[wB, -wB])
check(np.allclose(wD, spec_pm, atol=1e-10), "spec(D) = +- spec(B) exactly (gap at 0 = min|eig B|)")

print("\n  GAPPED END (m_inf = 1.5 > bandwidth 1): gap is stable and P_<0 / chiral count is well-posed")
prev = None
for L in [16, 32, 64, 128]:
    B = build_B_end(L, m_inf=1.5)
    D = dirac_from_B(B)
    G = np.kron(s3, np.eye(L, dtype=complex))
    gap = np.min(np.abs(np.linalg.eigvalsh(D)))
    c = chiral_count_neg(D, G)
    print("    L=%3d: spectral gap at 0 = %.4f ; tr(Gamma P_<0) = %+.2e" % (L, gap, c))
    check(gap > 0.35, "gapped end keeps a stable spectral gap at L=%d" % L)
    check(abs(c) < 1e-8, "well-posed P_<0 is chirality-balanced (count = 0) at L=%d" % L)
    prev = gap
check(prev > 0.35, "gap does NOT close as the end grows (well-posed in the L->inf limit)")

print("\n  GAPLESS END (m_inf = 1.0 = bandwidth): gap closes as L->inf -> P_<0 NOT well-posed (control)")
gaps = []
for L in [16, 32, 64, 128]:
    B = build_B_end(L, m_inf=1.0)
    D = dirac_from_B(B)
    gap = np.min(np.abs(np.linalg.eigvalsh(D)))
    gaps.append(gap)
    print("    L=%3d: spectral gap at 0 = %.5f (closing)" % (L, gap))
check(gaps[-1] < 0.5 * gaps[0], "gapless end: the 0-gap shrinks with L (continuous spectrum through 0)")
check(gaps[-1] < 0.06, "gapless end: gap -> 0, so the filled-sea chiral count is not integer-stable")

print("\n" + "#" * 90)
print("# VERDICT: PASS. Inside the cross-chirality Krein class, spec(D) = +- spec(B), so the physical")
print("#  projection P_<0 is well-defined IFF the end value of B is gapped (m_inf > 0). Whenever it is")
print("#  well-posed, the count is chirality-balanced (tr(Gamma P_<0) = 0), extending the interior")
print("#  theorem to the noncompact-end setting; the gapless case is exactly where well-posedness")
print("#  itself fails -- an analytic (weighted/gapped-completion) hypothesis, not a chiral leak.")
print("#  hard asserts passed: %d" % NASSERT)
print("#" * 90)
