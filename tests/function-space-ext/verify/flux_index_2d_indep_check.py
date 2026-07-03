#!/usr/bin/env python3
# Independent re-check of flux_index_2d.py: net chiral index = magnetic flux number, across
# DIFFERENT lattice sizes and higher fluxes (including odd 1,3,5). Confirms the Aharonov-Casher /
# Atiyah-Singer index = flux is robust, not a size/gap artifact. Deterministic, numpy-only.
import numpy as np

NASSERT = 0
def check(c, m):
    global NASSERT
    NASSERT += 1
    assert c, m

s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)


def build(Lx, Ly, Phi, r=1.0):
    N = Lx * Ly
    def ix(nx, ny):
        return (ny % Ly) * Lx + (nx % Lx)
    Tx = np.zeros((N, N), complex); Ty = np.zeros((N, N), complex); W = np.zeros((N, N), complex)
    tp = 2 * np.pi
    for nx in range(Lx):
        for ny in range(Ly):
            a = ix(nx, ny)
            phx = np.exp(-1j * tp * Phi * ny / Ly) if nx == Lx - 1 else 1.0
            b = ix(nx + 1, ny)
            Tx[a, b] += -0.5j * phx; Tx[b, a] += 0.5j * np.conj(phx)
            W[a, b] += -0.5 * phx; W[b, a] += -0.5 * np.conj(phx); W[a, a] += 0.5; W[b, b] += 0.5
            phy = np.exp(1j * tp * Phi * nx / (Lx * Ly))
            c = ix(nx, ny + 1)
            Ty[a, c] += -0.5j * phy; Ty[c, a] += 0.5j * np.conj(phy)
            W[a, c] += -0.5 * phy; W[c, a] += -0.5 * np.conj(phy); W[a, a] += 0.5; W[c, c] += 0.5
    Tx = 0.5 * (Tx + Tx.conj().T); Ty = 0.5 * (Ty + Ty.conj().T); W = 0.5 * (W + W.conj().T)
    D = np.kron(s1, Tx) + np.kron(s2, Ty) + np.kron(s3, r * W)
    return 0.5 * (D + D.conj().T), np.kron(s3, np.eye(N))


print("independent re-check: net chiral index = flux across sizes 20, 24 and flux up to 6")
for L, Phi in [(20, 0), (20, 1), (20, 2), (20, 4), (20, 5), (24, 3), (24, 6)]:
    D, G = build(L, L, Phi)
    w, V = np.linalg.eigh(D)
    Z = V[:, np.abs(w) < 0.2]
    c = int(round(np.trace(Z.conj().T @ G @ Z).real)) if Z.shape[1] else 0
    print("  L=%d flux=%d: index=%+d (%s)" % (L, Phi, c, "ODD" if c % 2 else "even"))
    check(abs(c) == Phi, "index = flux for L=%d Phi=%d" % (L, Phi))
print("INDEPENDENT CHECK PASS: index = flux (incl. odd 1,3,5); asserts %d" % NASSERT)
