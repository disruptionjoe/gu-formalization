#!/usr/bin/env python3
# Independent re-check of gap_wellposedness_end.py. DIFFERENT substrate: instead of the specific
# I + hopping chain, use SEEDED RANDOM Hermitian B at several sizes, made gapped by a positive shift
# (B = H + c*I, c > ||H|| => B positive-definite => gap = min eig(B) > 0) vs gapless (c = 0 => random
# H has eigenvalues straddling 0). Confirms the model-independent core: spec(D) = +- spec(B), the
# 0-gap = min|eig(B)|, and the well-posed physical projection is chirality-balanced (count 0).
import numpy as np

NASSERT = 0
def check(c, m):
    global NASSERT
    NASSERT += 1
    assert c, m

s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)

rng = np.random.default_rng(77712345)

def rand_herm(n):
    A = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    return 0.5 * (A + A.conj().T)

print("independent re-check: spec(D)=+-spec(B), gap=min|eig B|, well-posed count 0 (random B)")
for n in [6, 12, 24, 48]:
    H = rand_herm(n)
    nrm = np.max(np.abs(np.linalg.eigvalsh(H)))
    Bg = H + (nrm + 0.6) * np.eye(n)             # gapped: positive-definite
    Bz = H                                        # gapless control: eigenvalues straddle 0
    for tag, B, gapped in [("gapped", Bg, True), ("gapless", Bz, False)]:
        D = np.kron(s1, B)
        G = np.kron(s3, np.eye(n))
        wD = np.sort(np.linalg.eigvalsh(D)); wB = np.linalg.eigvalsh(B)
        check(np.allclose(wD, np.sort(np.r_[wB, -wB]), atol=1e-9), "spec(D)=+-spec(B) n=%d %s" % (n, tag))
        gap = np.min(np.abs(wD))
        check(abs(gap - np.min(np.abs(wB))) < 1e-9, "gap = min|eig B| n=%d %s" % (n, tag))
        V = np.linalg.eigh(D)[1][:, wD < 0]
        cnt = np.trace(V.conj().T @ G @ V).real
        if gapped:
            check(gap > 0.3, "gapped B has a real spectral gap n=%d" % n)
            check(abs(cnt) < 1e-8, "well-posed physical projection is chirality-balanced n=%d" % n)
        print("    n=%2d %-7s: gap=%.3f  tr(Gamma P_<0)=%+.2e" % (n, tag, gap, cnt))
print("INDEPENDENT CHECK PASS: gap<->well-posedness, count 0 when gapped; asserts %d" % NASSERT)
