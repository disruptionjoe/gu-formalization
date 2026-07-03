#!/usr/bin/env python3
# INDEPENDENT re-check of STEP 2 (rs_boundary_eta_l21.py): the net self-dual frame charge of the RS
# boundary operator is 0, robust under (a) a rotated SD/ASD frame basis and (b) a random unitary
# fiber similarity; and the RS boundary Dirac signature/eta is 0 via an independent signature count.
# Different angle, different basis, different seed -- must agree with the main script's 2-primary verdict.
from __future__ import annotations
import os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(REPO, "tests", "generation-sector"))
import gen_sector_bridge as gu_bridge  # noqa: E402

N, DIM = gu_bridge.N, gu_bridge.DIM


def lvec(i, j):
    M = np.zeros((N, N), dtype=complex); M[i, j] = 1.0; M[j, i] = -1.0; return M


def frame_charge(O, gens):
    O4 = O.reshape(N, DIM, N, DIM); t = 0.0
    for L in gens:
        nrm = np.tensordot(L.conj(), L, axes=([0, 1], [0, 1])).real
        t += float(np.linalg.norm(np.einsum('vw,vswt->st', L.conj(), O4) / nrm))
    return t


def main():
    e, Gamma, Pi, M_D = gu_bridge.constraint_objects()
    I = np.eye(N * DIM, dtype=complex); Q = I - Pi; E = Q @ M_D @ Pi; D_RS = E + E.conj().T

    base_sd = [lvec(0, 1) + lvec(2, 3), lvec(0, 2) + lvec(3, 1), lvec(0, 3) + lvec(1, 2)]
    base_asd = [lvec(0, 1) - lvec(2, 3), lvec(0, 2) - lvec(3, 1), lvec(0, 3) - lvec(1, 2)]

    # (a) rotated frame basis (SO(3) mixing of the self-dual pairs): net must stay 0
    th = 0.7
    R = np.array([[np.cos(th), -np.sin(th), 0], [np.sin(th), np.cos(th), 0], [0, 0, 1.0]])
    rot_sd = [sum(R[k, m] * base_sd[m] for m in range(3)) for k in range(3)]
    rot_asd = [sum(R[k, m] * base_asd[m] for m in range(3)) for k in range(3)]
    net_rot = frame_charge(D_RS, rot_sd) - frame_charge(D_RS, rot_asd)
    print(f"(a) rotated-basis net self-dual (D_RS):        {net_rot:+.3e}  (expect ~0)")

    # (b) random unitary fiber similarity: net self-dual is a base-frame quantity, invariant
    rng = np.random.default_rng(7)
    X = rng.standard_normal((DIM, DIM)) + 1j * rng.standard_normal((DIM, DIM))
    U, _ = np.linalg.qr(X); Uf = np.kron(np.eye(N), U)
    D_conj = Uf @ D_RS @ Uf.conj().T
    net_conj = frame_charge(D_conj, base_sd) - frame_charge(D_conj, base_asd)
    print(f"(b) fiber-conjugated net self-dual (D_RS):     {net_conj:+.3e}  (expect ~0)")

    # (c) independent signature/eta of D_RS
    wv = np.linalg.eigvalsh(0.5 * (D_RS + D_RS.conj().T))
    sig = int(np.sum(wv > 1e-8)) - int(np.sum(wv < -1e-8))
    print(f"(c) independent signature/eta of D_RS:         {sig}  (expect 0)")

    # (d) positive control still fires under the rotated basis
    def sgen(i, j):
        return 0.25 * (e[i] @ e[j] - e[j] @ e[i])
    Lam = sum(np.kron(np.eye(N), sgen(a, b) + sgen(c, d))
              + np.kron(lvec(a, b) + lvec(c, d), np.eye(DIM))
              for (a, b, c, d) in [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)])
    net_ctrl = frame_charge(Lam, rot_sd) - frame_charge(Lam, rot_asd)
    print(f"(d) rotated-basis net self-dual (control):     {net_ctrl:+.3f}  (expect != 0)")

    assert abs(net_rot) < 1e-6 and abs(net_conj) < 1e-6, "net self-dual must stay 0"
    assert sig == 0, "independent signature must be 0"
    assert abs(net_ctrl) > 1e-2, "control must remain chiral"
    print("\n[OK] independent re-check agrees: RS boundary net self-dual = 0, eta = 0 => 2-primary.")


if __name__ == "__main__":
    main()
