#!/usr/bin/env python3
# WC-FUNCTION-SPACE-EXT boundary/APS swing: WHERE an odd chiral count can enter, and where it
# provably cannot. The conditional interior theorem says the cross-chirality Krein-Dirac interior
# has net chiral spectral flow 0 (2-primary / even). The paper concludes the odd generation count
# is "external on present evidence -- supplied by a net-self-dual chiral background (chiral gauge
# couplings, instanton zero-modes, K3/CY compactification)."
#
# This script pins the parity honestly on a CLOSED 1D circle:
#   (1) trivial background -> net chiral count 0 (even);
#   (2) any REAL mass background on the closed circle -> net chiral count EVEN (its domain walls /
#       zeros come in opposite-chirality pairs; a closed 1D manifold cannot host an odd net count);
#   (3) a genuinely chiral (complex, sigma_2-channel) background is what would be needed for an
#       asymmetry, and it BREAKS Krein-self-adjointness (leaves the interior class) -- the necessary
#       condition the interior no-go already identified.
#
# HONEST SCOPE: an actual ODD net count is a TOPOLOGICAL index -- the instanton / magnetic-flux
# number (a 2D+ statement) or an APS boundary eta -- NOT hosted by this 1D closed model, which is
# exactly the point: the interior/closed sector is forced even, and the odd count must come from the
# external topological datum. That external index is ANY integer (odd or even) -- it is NOT
# 2-primary-constrained, and it does NOT single out 3. This CONFIRMS and localizes "external on
# present evidence"; it is not a computation of 3.
import numpy as np

NASSERT = 0
def check(c, m):
    global NASSERT
    NASSERT += 1
    assert c, m

s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)

def build(N, m1, m2, r=1.0):
    IN = np.eye(N, dtype=complex)
    P = np.zeros((N, N), dtype=complex)
    Lap = np.zeros((N, N), dtype=complex)
    for j in range(N):
        P[j, (j + 1) % N] += -0.5j
        P[(j + 1) % N, j] += 0.5j
        Lap[j, j] += 1.0
        Lap[(j + 1) % N, (j + 1) % N] += 1.0
        Lap[j, (j + 1) % N] += -1.0
        Lap[(j + 1) % N, j] += -1.0
    A = P + np.diag(m1.astype(complex)) + (r / 2.0) * Lap
    Bm = np.diag(m2.astype(complex))
    H = 0.5 * ((np.kron(s1, A) + np.kron(s2, Bm)) + (np.kron(s1, A) + np.kron(s2, Bm)).conj().T)
    return H, np.kron(s3, IN), np.kron(s1, IN)

def chiral_count(H, Gamma, gap=0.5):
    w, V = np.linalg.eigh(H)
    Z = V[:, np.abs(w) < gap]
    return (0 if Z.shape[1] == 0 else int(round(np.trace(Z.conj().T @ Gamma @ Z).real))), Z.shape[1]

print("=" * 88)
print("Parity of the chiral count: closed 1D circle is forced EVEN; odd needs external topology")
print("=" * 88)
N = 240
th = np.linspace(0, 2 * np.pi, N, endpoint=False)
_, G0, K0 = build(N, np.zeros(N), np.zeros(N))
check(np.linalg.norm(K0 @ G0 + G0 @ K0) < 1e-9, "cross-chirality premise K Gamma = -Gamma K")

# (1)+(2): trivial and REAL-mass backgrounds on the closed circle -> net count EVEN (0)
for label, m1 in [("trivial", np.zeros(N)),
                  ("real mass, 2 zeros", 3.0 * np.cos(th)),
                  ("real mass, 4 zeros", 3.0 * np.cos(2 * th)),
                  ("real mass, 6 zeros", 2.5 * np.cos(3 * th))]:
    H, G, K = build(N, m1, np.zeros(N))
    c, kc = chiral_count(H, G)
    print("  closed circle, %s: net chiral count = %+d (%s), %d near-zero modes"
          % (label, c, "even" if c % 2 == 0 else "ODD", kc))
    check(c % 2 == 0 and c == 0, "closed 1D + real background: net chiral count is EVEN (0)")

# (3): a genuinely chiral (complex) background breaks Krein-self-adjointness (necessary for asymmetry)
for w in [1, 2, 3]:
    H, G, K = build(N, 3.0 * np.cos(w * th), 3.0 * np.sin(w * th))
    krein = np.linalg.norm(H.conj().T @ K - K @ H) / np.linalg.norm(H)
    print("  complex chiral background (winding %d): Krein-self-adjointness violation = %.2f" % (w, krein))
    check(krein > 0.1, "a chiral (complex) background leaves the interior Krein class")

print()
print("#" * 88)
print("# VERDICT: the closed/interior net chiral count is forced EVEN by the cross-chirality Krein")
print("#  structure -- real backgrounds' domain walls pair off, and a closed 1D manifold hosts no")
print("#  odd net count. A genuinely chiral background breaks Krein-self-adjointness [leaves the")
print("#  interior class]. An actual ODD count is a TOPOLOGICAL index -- instanton/flux number or an")
print("#  APS boundary eta -- external to the interior sector, ANY integer, NOT 2-primary-constrained")
print("#  and NOT a selection of 3. This confirms and localizes the paper's 'external on present")
print("#  evidence' route to the external topological datum; a clean numerical odd-count demo needs")
print("#  a 2D flux / APS setup, which remains the genuine analytic frontier.")
print("#  hard asserts passed: %d" % NASSERT)
print("#" * 88)
