"""SM-leg hardening: the two referee-flagged 'NOT ESTABLISHED' sub-claims, now REALLY computed.

(1) so(10) has NO independent cubic Casimir -- the totally-symmetric cubic invariant d^{abc} =
    Tr_16({Sigma_a, Sigma_b} Sigma_c) VANISHES on the 16 (chiral spinor). This is the genuine "umbrella"
    the earlier test only asserted: it is *why* every SM anomaly trace of one generation cancels. Built
    from an explicit Cl(10) gamma construction, so(10) generators Sigma_ab, and the 16 chiral projection.
(2) The mirror is a GENUINE 16bar (not the definitional n_L-n_R=16-16 tautology): the opposite-chirality
    spinor carries so(10) charges that are the negatives of the 16's, so 16 (+) 16bar is a real
    (self-conjugate) vectorlike pair -- every charged state has an opposite-charge mirror partner.

numpy, exact-ish (machine precision). Run: python tests/one-residual/sm_so10_cubic_casimir_and_mirror.py
"""
from __future__ import annotations

import numpy as np

FAIL: list[str] = []
sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2, dtype=complex)


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  '+detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


def kron(*ms):
    out = np.array([[1]], complex)
    for m in ms:
        out = np.kron(out, m)
    return out


def cl10_gammas():
    """10 gamma matrices of Cl(10,0), 32x32, {G_a,G_b}=2 delta_ab, via 5-qubit Jordan-Wigner."""
    G = []
    for j in range(5):  # positions 0..4
        pre = [sz] * j
        for pauli in (sx, sy):
            mats = pre + [pauli] + [I2] * (4 - j)
            G.append(kron(*mats))
    return G  # 10 matrices


def main():
    print("[SM-leg hardening] so(10) cubic Casimir vanishes on the 16 + real 16bar mirror\n")
    G = cl10_gammas()
    # verify Clifford relations
    cl_ok = all(np.allclose(G[a] @ G[b] + G[b] @ G[a], 2 * (a == b) * np.eye(32)) for a in range(10) for b in range(10))
    check("Cl(10) gammas satisfy {G_a,G_b}=2 delta_ab (32x32)", cl_ok)

    # chirality and the 16 chiral block
    chir = G[0]
    for a in range(1, 10):
        chir = chir @ G[a]
    chir = chir * (1j ** 5)  # normalize so chir^2 = I, eigenvalues +-1
    ev, V = np.linalg.eigh(chir)
    plus = V[:, ev > 0]  # 16 columns
    check("chirality operator splits 32 = 16 (+) 16bar", plus.shape[1] == 16, f"dim = {plus.shape[1]}")

    # so(10) generators Sigma_ab = [G_a,G_b]/4, projected to the 16
    P = plus  # 32x16 isometry onto the +chirality 16
    gens = []
    for a in range(10):
        for b in range(a + 1, 10):
            S = (G[a] @ G[b] - G[b] @ G[a]) / 4.0
            gens.append(P.conj().T @ S @ P)  # 16x16
    gens = np.array(gens)  # (45,16,16)
    check("so(10) has 45 generators on the 16", gens.shape == (45, 16, 16))

    # (1) cubic Casimir d^{abc} = Tr({S_a,S_b} S_c); anomaly-safe iff it vanishes for all a,b,c
    anti = gens[:, None] @ gens[None, :] + gens[None, :] @ gens[:, None]   # (45,45,16,16) {S_a,S_b}
    d = np.einsum('cij,abji->abc', gens, anti)                            # (45,45,45)
    maxd = float(np.max(np.abs(d)))
    print(f"  so(10) cubic invariant on the 16: max_abc |Tr({{S_a,S_b}} S_c)| = {maxd:.2e}")
    check("(1) so(10) cubic Casimir VANISHES on the 16 -- no independent cubic invariant (the real umbrella)",
          maxd < 1e-9, "this is WHY every one-generation SM anomaly trace cancels")

    # (2) real 16bar mirror: compare the FULL WEIGHT SYSTEM (all 5 commuting Cartans), not one charge
    # (a single Cartan has a symmetric spectrum and would pass trivially). The 16 weights are
    # (+-1/2)^5 with an even number of minus signs; the 16bar are the negatives (odd number). We read the
    # joint weight vectors by diagonalizing a generic combination of the 5 Cartans and evaluating each.
    minus = V[:, ev < 0]  # the 16bar
    cartans = [1j * (G[2 * j] @ G[2 * j + 1] - G[2 * j + 1] @ G[2 * j]) / 4.0 for j in range(5)]  # Hermitian

    def weight_set(block):
        combo = sum((10.0 ** j) * (block.conj().T @ H @ block) for j, H in enumerate(cartans))
        _, W = np.linalg.eigh(combo)  # simultaneous eigenbasis (Cartans commute)
        weights = []
        for k in range(W.shape[1]):
            v = W[:, k]
            weights.append(tuple(round(float(np.real(v.conj() @ (block.conj().T @ H @ block) @ v)), 3) for H in cartans))
        return sorted(weights)

    w16 = weight_set(plus)
    w16b = weight_set(minus)
    neg_w16 = sorted(tuple(-x for x in wt) for wt in w16)
    mirror_ok = (w16b == neg_w16)
    even_minus = all(sum(1 for x in wt if x < 0) % 2 == 0 for wt in w16)  # 16 = even-parity spinor
    print(f"  16 weights (sample): {w16[:2]} ...  all (+-1/2)^5 even-minus: {even_minus}")
    print(f"  16bar weights == negatives of 16 weights: {mirror_ok}")
    check("(2) the 16bar is the genuine charge-CONJUGATE (full 5-Cartan weight set = negatives of the 16)",
          mirror_ok and even_minus, "16 (+) 16bar is a real vectorlike pair; not the n_L-n_R=16-16 tautology")

    print("\n[verdict]")
    if not FAIL:
        print("  * SM leg hardened: the so(10) cubic Casimir is now COMPUTED to vanish on the 16 (max |d| ~ 0),")
        print("    replacing the asserted 'umbrella' -- this is the real reason one-generation anomalies")
        print("    cancel. And the 16bar mirror is exhibited as the genuine charge-conjugate (its Cartan")
        print("    charges are the negatives of the 16's), replacing the definitional n_L-n_R=16-16 tautology")
        print("    with a real vectorlike-pair computation. Existence grade -> now on firmer, computed footing.")
    if FAIL:
        print(f"\nFAILED: {FAIL}")
        raise SystemExit(1)
    print("\nexit 0 = so(10) cubic Casimir vanishes on the 16; the 16bar is a genuine charge-conjugate mirror.")


if __name__ == "__main__":
    main()
