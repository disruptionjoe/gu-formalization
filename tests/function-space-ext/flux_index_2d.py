#!/usr/bin/env python3
# WC-FUNCTION-SPACE-EXT decisive swing: the external topological datum carries an ODD chiral count.
#
# 2D magnetic-flux Wilson-Dirac on a torus. By the Aharonov-Casher / Atiyah-Singer index theorem the
# net chiral zero-mode count equals the magnetic flux number Phi. Phi = 1, 3 give ODD counts. This is
# the clean numerical realization of the paper's "external on present evidence -- supplied by a
# net-self-dual chiral background (instanton zero-modes, flux, K3/CY)" mechanism, which the interior
# 1D closed model provably cannot host. The flux background breaks the interior Krein-self-adjoint
# class. The index = Phi is ANY integer: NOT 2-primary-constrained, and NOT a selection of 3.
import numpy as np

NASSERT = 0
def check(c, m):
    global NASSERT
    NASSERT += 1
    assert c, m

s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)


def build_flux_dirac(Lx, Ly, Phi, r=1.0):
    """2D Wilson-Dirac, uniform flux Phi (Landau gauge A_y = 2pi Phi nx/(Lx Ly), x-seam twist).
    D = s1 (x) Tx + s2 (x) Ty + s3 (x) Wilson ; Gamma = s3 (x) I ; K = s1 (x) I."""
    N = Lx * Ly
    def idx(nx, ny):
        return (ny % Ly) * Lx + (nx % Lx)
    Tx = np.zeros((N, N), dtype=complex)     # -i D_x (hermitian)
    Ty = np.zeros((N, N), dtype=complex)     # -i D_y
    Wil = np.zeros((N, N), dtype=complex)    # r/2 * (sum_mu (1 - cos p_mu)) -> lattice Laplacian/2
    two_pi = 2 * np.pi
    for nx in range(Lx):
        for ny in range(Ly):
            a = idx(nx, ny)
            # x hop: phase 0, with x-seam twist exp(-i 2pi Phi ny/Ly) when wrapping Lx-1 -> 0
            phx = np.exp(-1j * two_pi * Phi * ny / Ly) if nx == Lx - 1 else 1.0
            b = idx(nx + 1, ny)
            Tx[a, b] += -0.5j * phx
            Tx[b, a] += 0.5j * np.conj(phx)
            Wil[a, b] += -0.5 * phx
            Wil[b, a] += -0.5 * np.conj(phx)
            Wil[a, a] += 0.5
            Wil[b, b] += 0.5
            # y hop: Landau-gauge phase exp(i 2pi Phi nx/(Lx Ly))
            phy = np.exp(1j * two_pi * Phi * nx / (Lx * Ly))
            c = idx(nx, ny + 1)
            Ty[a, c] += -0.5j * phy
            Ty[c, a] += 0.5j * np.conj(phy)
            Wil[a, c] += -0.5 * phy
            Wil[c, a] += -0.5 * np.conj(phy)
            Wil[a, a] += 0.5
            Wil[c, c] += 0.5
    Tx = 0.5 * (Tx + Tx.conj().T)
    Ty = 0.5 * (Ty + Ty.conj().T)
    Wil = 0.5 * (Wil + Wil.conj().T)
    IN = np.eye(N, dtype=complex)
    D = np.kron(s1, Tx) + np.kron(s2, Ty) + np.kron(s3, r * Wil)
    D = 0.5 * (D + D.conj().T)
    return D, np.kron(s3, IN), np.kron(s1, IN)


def chiral_index(D, Gamma, gap):
    w, V = np.linalg.eigh(D)
    Z = V[:, np.abs(w) < gap]
    if Z.shape[1] == 0:
        return 0, 0, np.sort(np.abs(w))[:6]
    return int(round(np.trace(Z.conj().T @ Gamma @ Z).real)), Z.shape[1], np.sort(np.abs(w))[:6]


print("=" * 88)
print("2D magnetic-flux Wilson-Dirac: net chiral zero-mode count = flux number (Aharonov-Casher)")
print("=" * 88)
Lx = Ly = 16
for Phi in [0, 1, 2, 3]:
    D, G, K = build_flux_dirac(Lx, Ly, Phi)
    krein = np.linalg.norm(D.conj().T @ K - K @ D) / max(np.linalg.norm(D), 1e-30)
    gap = 0.25
    c, kc, low = chiral_index(D, G, gap)
    tag = "even" if c % 2 == 0 else "ODD"
    print("  flux Phi=%d: net chiral index = %+d (%s); %d near-zero modes; lowest|E|=%s; Krein-viol=%.2f"
          % (Phi, c, tag, kc, np.round(low[:4], 3), krein))
    check(abs(c) == Phi, "index = flux number Phi=%d (Aharonov-Casher / Atiyah-Singer)" % Phi)
    if Phi > 0:
        check(krein > 0.05, "the flux background breaks the interior Krein-self-adjoint class")

print()
print("#" * 88)
print("# VERDICT: index = flux number. Phi=1 and Phi=3 give ODD net chiral counts -- the external")
print("#  topological datum (magnetic flux / instanton number) DOES carry an odd chiral count, which")
print("#  the interior/closed sector provably cannot. This decisively realizes the paper's 'external")
print("#  on present evidence' route (instanton/flux/K3), breaks the interior Krein class, is ANY")
print("#  integer -- NOT 2-primary-constrained -- and does NOT single out 3.")
print("#  hard asserts passed: %d" % NASSERT)
print("#" * 88)
