#!/usr/bin/env python3
# Independent re-check of aps_end_eta_class_symmetry.py. DIFFERENT seed, DIFFERENT B distribution
# (integer-valued GOE-like real-symmetric AND complex-Hermitian with a large scale), larger sizes,
# and an INDEPENDENT symmetry witness: for D = s1 (x) B every eigenvalue lambda has partner
# -lambda, so (i) trace(D) = 0 exactly, (ii) trace(D^(2k+1)) = 0 for all k (odd moments vanish),
# and (iii) eta_0 = 0. Odd-moment vanishing is a basis-free witness of spectral symmetry that does
# not go through diagonalization sorting.
import numpy as np

NASSERT = 0
def check(c, m):
    global NASSERT
    NASSERT += 1
    assert c, m

s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)
TOL = 1e-10
rng = np.random.default_rng(555_909)

def eta0(spec):
    return int(np.sum(spec > TOL)) - int(np.sum(spec < -TOL))

print("independent re-check: class boundary operator is spectrally symmetric => eta_0 = 0")
maxodd = 0.0
for n in [4, 7, 11, 20, 33]:
    # complex Hermitian, larger scale, plus an integer-valued real-symmetric variant
    A = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    Bc = 2.5 * (0.5 * (A + A.conj().T)) + 1.7 * np.eye(n)
    R = rng.integers(-3, 4, size=(n, n)).astype(float)
    Br = (R + R.T) + 5.0 * np.eye(n)
    for tag, B in [("cplx", Bc), ("intR", Br.astype(complex))]:
        D = np.kron(s1, B)
        # odd-moment witnesses of symmetry (basis-free)
        for k in (1, 3, 5):
            odd = abs(np.trace(np.linalg.matrix_power(D, k)))
            maxodd = max(maxodd, odd)
            check(odd < 1e-7 * max(1.0, np.linalg.norm(D) ** k), "odd moment %d ~ 0 (n=%d %s)" % (k, n, tag))
        spec = np.linalg.eigvalsh(D)
        check(eta0(spec) == 0, "class eta_0 = 0 (n=%d %s)" % (n, tag))
        check(abs(np.sum(spec)) < 1e-8, "sum of spectrum = 0 (n=%d %s)" % (n, tag))
print("  max |odd moment| across all draws = %.1e" % maxodd)
print("INDEPENDENT CHECK PASS: class boundary eta_0 = 0 by odd-moment + eta witnesses; asserts %d" % NASSERT)
