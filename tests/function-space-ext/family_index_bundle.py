#!/usr/bin/env python3
# WC-FUNCTION-SPACE-EXT residual item (3): FAMILY-INDEX / higher-topology term over a parameter
# space (the index bundle), invisible to the single-point 1D interior model.
#
# Structural fact for the class D(t) = s1 (x) B(t) (Gamma = s3 (x) I, K = s1 (x) I): the negative-
# energy bundle of D over the parameter torus is E_-(D) = {upper band of B} (+) {lower band of B}
# (the D-eigenvalue -b_max comes from the upper B-band, +b_min from the lower B-band, each dressed by
# a CONSTANT chirality-off-diagonal vector u_-+ = (1,-+1)/sqrt2). Therefore
#     c1(E_-(D)) = c1(upper band of B) + c1(lower band of B) = 0
# because the Chern numbers of the two bands of any gapped 2-band Hermitian sum to zero. This kills
# the family-index / higher-topology term IDENTICALLY -- while each band is individually nonzero, so
# the test is NON-VACUOUS. Breaking the class (letting the negative bundle keep only one band)
# leaves a nonzero Chern number -- exactly the external topological datum.
#
# Chern numbers by the gauge-invariant Fukui-Hatsugai-Suzuki lattice method. Deterministic, numpy.
import numpy as np

NASSERT = 0
def check(c, m):
    global NASSERT
    NASSERT += 1
    assert c, m

s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)


def qwz_B(kx, ky, m):
    """Qi-Wu-Zhang two-band Chern-insulator Hamiltonian B(k) = d.sigma (Hermitian, traceless)."""
    d = np.array([np.sin(kx), np.sin(ky), m + np.cos(kx) + np.cos(ky)])
    return d[0] * s1 + d[1] * s2 + d[2] * s3


def band_vec(B, which):
    """Normalized eigenvector of the 'lower' or 'upper' band of a 2x2 Hermitian."""
    w, V = np.linalg.eigh(B)
    return V[:, 0] if which == "lower" else V[:, 1]


def chern_fhs(vec_at, Nk):
    """Fukui-Hatsugai-Suzuki lattice Chern number of a single band over the T^2 grid.
       vec_at(i, j) -> normalized band eigenvector at k = 2pi(i,j)/Nk."""
    grid = [[vec_at(i, j) for j in range(Nk)] for i in range(Nk)]
    def U(u, v):
        z = np.vdot(u, v)
        return z / abs(z)
    F_total = 0.0
    for i in range(Nk):
        for j in range(Nk):
            u00 = grid[i][j]
            u10 = grid[(i + 1) % Nk][j]
            u01 = grid[i][(j + 1) % Nk]
            u11 = grid[(i + 1) % Nk][(j + 1) % Nk]
            Ux = U(u00, u10)
            Uy_r = U(u10, u11)
            Ux_t = U(u01, u11)
            Uy = U(u00, u01)
            F = np.log(Ux * Uy_r / Ux_t / Uy)  # principal branch, imaginary
            F_total += F.imag
    return F_total / (2 * np.pi)


print("=" * 90)
print("WC-FUNCTION-SPACE-EXT (3): family-index / index-bundle term vanishes in the class")
print("=" * 90)

m = -1.0   # QWZ topological phase (-2 < m < 0): |lower-band Chern| = 1
Nk = 24

def lower_at(i, j):
    return band_vec(qwz_B(2 * np.pi * i / Nk, 2 * np.pi * j / Nk, m), "lower")
def upper_at(i, j):
    return band_vec(qwz_B(2 * np.pi * i / Nk, 2 * np.pi * j / Nk, m), "upper")

c_lower = chern_fhs(lower_at, Nk)
c_upper = chern_fhs(upper_at, Nk)
print("  QWZ B(k), m=%.1f: c1(lower band) = %+.3f, c1(upper band) = %+.3f" % (m, c_lower, c_upper))
c_lower_i = int(round(c_lower)); c_upper_i = int(round(c_upper))
check(abs(c_lower - c_lower_i) < 1e-6, "lower-band Chern is integer")
check(abs(c_upper - c_upper_i) < 1e-6, "upper-band Chern is integer")
check(c_lower_i != 0, "NON-VACUOUS: the lower band carries a nonzero Chern number")
check(c_upper_i != 0, "NON-VACUOUS: the upper band carries a nonzero Chern number")
check(c_lower_i + c_upper_i == 0, "the two bands' Chern numbers sum to 0 (gapped 2-band identity)")

# c1 of the negative bundle of D = s1 (x) B: it is {upper B band} (+) {lower B band}, so its Chern
# number is the SUM of the two band Cherns = 0. Confirm by building D's negative bundle directly.
def neg_bundle_chern_of_D(Nk):
    """Chern number of the rank-2 negative-energy bundle of D = s1 (x) B over T^2 (FHS, non-abelian
       determinant-line version: track the determinant of overlaps of the 2-frame)."""
    frames = {}
    for i in range(Nk):
        for j in range(Nk):
            B = qwz_B(2 * np.pi * i / Nk, 2 * np.pi * j / Nk, m)
            D = np.kron(s1, B)
            w, V = np.linalg.eigh(D)
            frames[(i, j)] = V[:, :2]  # the two most-negative eigenvectors
    def Udet(F1, F2):
        M = F1.conj().T @ F2
        z = np.linalg.det(M)
        return z / abs(z)
    F_total = 0.0
    for i in range(Nk):
        for j in range(Nk):
            f00 = frames[(i, j)]; f10 = frames[((i + 1) % Nk, j)]
            f01 = frames[(i, (j + 1) % Nk)]; f11 = frames[((i + 1) % Nk, (j + 1) % Nk)]
            F = np.log(Udet(f00, f10) * Udet(f10, f11) / Udet(f01, f11) / Udet(f00, f01))
            F_total += F.imag
    return F_total / (2 * np.pi)

c_D = neg_bundle_chern_of_D(Nk)
print("  negative bundle of D = s1 (x) B: total Chern number = %+.3f" % c_D)
check(abs(c_D - round(c_D)) < 1e-6, "D negative-bundle Chern is integer")
check(int(round(c_D)) == 0, "family chiral index term c1(E_-(D)) = c1(upper)+c1(lower) = 0")

print("\n  CONTROL: if the negative bundle kept only ONE band (out of class), the term is nonzero")
check(c_lower_i != 0, "single-band (out-of-class) negative bundle has Chern = %+d != 0" % c_lower_i)

print("\n" + "#" * 90)
print("# VERDICT: PASS. The family-index / higher-topology term of the class family D = s1 (x) B is")
print("#  c1(E_-(D)) = c1(upper band) + c1(lower band) = 0, identically, because the negative bundle")
print("#  contains BOTH bands of B (chirality-balanced). Each band is individually Chern %+d / %+d"
      % (c_lower_i, c_upper_i))
print("#  (non-vacuous). A nonzero family term needs the negative bundle to keep a single chirality/")
print("#  band -- an out-of-class (external topological) datum. Residual item (3) is discharged.")
print("#  hard asserts passed: %d" % NASSERT)
print("#" * 90)
