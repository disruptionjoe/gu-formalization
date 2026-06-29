"""Synthesis adjudication: does the SW shell (j=1 triplet) REDUCE or INCREASE the
gamma-trace obstruction ||Q M_D P||?  Resolves verify_B (uncaptured 'expectation')
vs critique (claimed measured refutation: shell ~1.44x WORSE).

Off-shell: P = Pi_RS (full 1664-dim constraint surface).
On-shell : P = P_trip (192-dim j=1 SW carrier).
Reports Frobenius leakage, per-mode RMS (||.||_F / sqrt(rank P)), and escape
fraction ||Q M_D P||_F / ||M_D P||_F for each.  Self-contained: reuses the verified
(9,5) constraint objects from gen_sector_bridge and the self-dual su(2)+ J generators.
"""
import os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.normpath(os.path.join(HERE, "..", "generation-sector"))
for p in (GEN, os.path.normpath(os.path.join(HERE, ".."))):
    if p not in sys.path:
        sys.path.insert(0, p)

import gen_sector_bridge as gsb

N, DIM = gsb.N, gsb.DIM
e, Gamma, Pi_RS, M_D = gsb.constraint_objects()
I128, I14 = np.eye(DIM, dtype=complex), np.eye(N, dtype=complex)

# Q = I - Pi_RS  (projector onto image of Gamma^dag = off-constraint-surface)
Q = np.eye(N * DIM, dtype=complex) - Pi_RS

# anchors (sanity)
bare = np.linalg.norm(Pi_RS @ M_D - M_D @ Pi_RS)
c2 = np.linalg.norm(Gamma @ M_D @ Pi_RS)
print(f"anchors: bare ||[Pi_RS,M_D]|| = {bare:.4f}  (expect 58.7215)")
print(f"         C2 = ||Gamma M_D Pi_RS|| = {c2:.4f}  (expect 155.3625)")
print(f"         C2/sqrt(N) = {c2/np.sqrt(N):.4f}  (the 41.52 off-shell floor)")

# self-dual su(2)+ generators on V (x) S, same gammas (base {0,1,2,3} are spacelike here)
def sgen(i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])
def lvec(i, j):
    M = np.zeros((N, N), dtype=complex); M[i, j] = 1; M[j, i] = -1; return M
sd = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
J = [np.kron(I14, sgen(a, b) + sgen(c, d)) + np.kron(lvec(a, b) + lvec(c, d), I128)
     for (a, b, c, d) in sd]
cpi = max(np.linalg.norm(J[k] @ Pi_RS - Pi_RS @ J[k]) for k in range(3))
print(f"self-dual J preserves ker(Gamma): max||[J,Pi_RS]|| = {cpi:.2e}")

# Casimir decomposition inside ker(Gamma); extract j=1 (Casimir = 8) triplet projector
w, V = np.linalg.eigh(Pi_RS); W = V[:, w > 0.5]
Cas = -(J[0] @ J[0] + J[1] @ J[1] + J[2] @ J[2])
CasK = W.conj().T @ Cas @ W; CasK = 0.5 * (CasK + CasK.conj().T)
ev, U = np.linalg.eigh(CasK)
mask = np.abs(ev - 8.0) < 1e-3
Wtrip = W @ U[:, mask]
P_trip = Wtrip @ Wtrip.conj().T
print(f"j=1 triplet carrier dim = {Wtrip.shape[1]} (expect 192)")

def leakage(P, name):
    QMDP = Q @ M_D @ P
    MDP = M_D @ P
    fro = np.linalg.norm(QMDP)
    rank = int(round(np.trace(P).real))
    rms = fro / np.sqrt(rank)
    escape = fro / np.linalg.norm(MDP)
    print(f"\n[{name}]  rank(P)={rank}")
    print(f"   ||Q M_D P||_F      = {fro:.4f}")
    print(f"   per-mode RMS       = {rms:.4f}")
    print(f"   escape fraction    = {escape:.4f}")
    return rms, escape

print("\n=== OBSTRUCTION LEAKAGE: off-shell vs on-shell (SW j=1 carrier) ===")
rms_off, esc_off = leakage(Pi_RS, "OFF-SHELL  P=Pi_RS (1664)")
rms_on, esc_on = leakage(P_trip, "ON-SHELL   P=P_trip (192, SW carrier)")

print("\n=== VERDICT ===")
print(f"per-mode RMS ratio  on/off = {rms_on/rms_off:.3f}")
print(f"escape frac  ratio  on/off = {esc_on/esc_off:.3f}")
better = rms_on < rms_off and esc_on < esc_off
print(f"SW shell REDUCES obstruction per mode? {better}")
print("-> if ratio > 1 on both, the SW shell is strictly WORSE (B1 refuted, not just no-help).")
