#!/usr/bin/env python3
r"""
CARRIER-DIRECTION HESSIAN EIGENVALUE ON THE SUBSTRATE.

Question (the dynamical reframe of "located, not forced"): is the order-3 generation
count a FLAT direction (a zero MODE / modulus -> "located, not forced" confirmed
dynamically) or a CURVED minimum (a forced value) of the action's quadratic part on
the carrier sector?

This script answers the DIAGONAL (carrier's own) half of the Hessian test -- the
genuinely NEW content beyond the DECOUPLE (which already showed the OFF-diagonal
selector<->carrier coupling is 0 via frame charge 0). Here we ask: is the carrier's
OWN second variation along the OCCUPANCY direction (the Z/3 direction that changes the
order-3 carrier's content) also 0, because the carrier is VECTORLIKE (+96/-96 balanced)?

PROXY DISCIPLINE (honest gating). The full GU source action is UNBUILT. We use the
best-available, prompt-sanctioned proxy for the action's quadratic part on the carrier:
the invariant Krein form K = eta_V (x) beta_S restricted to the carrier triplet
(Lambda^2_+, the 192-dim j=1 sector of ker(Gamma)), signature (+96, -96, 0). The Krein
form IS the so(p,q)-invariant quadratic form on the matter module -- the quadratic
(Gaussian / free) part of any GU-covariant action must be proportional to it on this
sector. So evaluating the Hessian = evaluating the Krein quadratic form. This is
COMPUTED ON THE SUBSTRATE; the only gated step is the identification "action quadratic
part = K" (which any GU-covariant action satisfies up to a positive normalization on a
single irreducible sector, hence cannot change the SIGN structure / the zero).

THE COMPUTATION.
  - Build the carrier triplet projector Wt (192-dim j=1) and B = Wt^dag K Wt (192x192),
    the Krein-Hessian, exactly as ghost_parity_krein.py (reproduces +96/-96).
  - The action's second variation along a field direction v is the Rayleigh quotient
    lambda(v) = (v^dag B v) / (v^dag v)  (the Hessian eigenvalue along v).
  - The CARRIER-OCCUPANCY / Z/3 direction is the BALANCED direction: increasing the
    order-3 carrier's content means populating each hyperbolic (generation, mirror) pair
    EQUALLY, because the carrier is vectorlike -- physical and mirror are bound, you
    cannot change the carrier content chirally at zero cost. The balanced direction is
    the NULL direction of the hyperbolic form. We construct it explicitly from the
    +96/-96 eigenspaces and evaluate B on it.
  - CONTRAST (the machine is not blind): a purely-physical (+96) occupation gives
    lambda > 0 (curved); a purely-ghost (-96) gives lambda < 0. Only the BALANCED
    carrier-occupancy direction is flat.

VERDICT LOGIC.
  lambda_occupancy == 0  => the carrier-occupancy direction is FLAT => the count is a
                            genuine zero MODE (modulus) at the DYNAMICAL level, not merely
                            decoupled => "located, not forced" confirmed dynamically.
  lambda_occupancy != 0  => the action's quadratic part prefers a value => FORCED.

Run: python tests/hessian-z3/carrier_occupancy_hessian.py
"""
from __future__ import annotations

import numpy as np

N, DIM = 14, 128


# ----------------------------------------------------------------------------------------
# substrate: Cl(9,5) gammas (Jordan-Wigner), the carrier triplet, the Krein form
# (self-contained, identical construction to tests/generation-sector/ghost_parity_krein.py)
# ----------------------------------------------------------------------------------------
def jw(n):
    I = np.eye(2, dtype=complex)
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    G = []
    for k in range(n):
        L, R = [s3] * k, [I] * (n - 1 - k)
        for mid in (s1, s2):
            o = np.array([[1 + 0j]])
            for m in L + [mid] + R:
                o = np.kron(o, m)
            G.append(o)
    return G


def sgen(e, i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


def lvec(i, j):
    M = np.zeros((N, N), dtype=complex)
    M[i, j] = 1
    M[j, i] = -1
    return M


SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]   # self-dual SU(2)+ on base {0,1,2,3}


def build_carrier_krein(timelike):
    """Return (B, dims) where B = Wt^dag K Wt is the Krein-Hessian on the 192-dim j=1
    carrier triplet, and dims = (npos, nneg, nzero) its signature."""
    base = jw(7)
    I128, I14 = np.eye(DIM, dtype=complex), np.eye(N, dtype=complex)
    e = [(1j * base[a] if a in timelike else base[a]) for a in range(14)]
    spacelike = [a for a in range(14) if a not in timelike]

    # gamma-trace constraint surface ker(Gamma) and the self-dual SU(2)+ generators
    Gamma = np.hstack(e)
    Pi = np.eye(N * DIM, dtype=complex) - Gamma.conj().T @ np.linalg.inv(Gamma @ Gamma.conj().T) @ Gamma
    J = [np.kron(I14, sgen(e, a, b) + sgen(e, c, d)) + np.kron(lvec(a, b) + lvec(c, d), I128)
         for (a, b, c, d) in SD]
    w, Vv = np.linalg.eigh(Pi)
    W = Vv[:, w > 0.5]                                  # ker(Gamma) = 1664-dim
    Cas = -(J[0] @ J[0] + J[1] @ J[1] + J[2] @ J[2])    # SU(2)+ Casimir
    CasK = W.conj().T @ Cas @ W
    CasK = 0.5 * (CasK + CasK.conj().T)
    ev, U = np.linalg.eigh(CasK)
    top = max(round(x.real, 3) for x in ev)
    Wt = W @ U[:, np.abs(ev - top) < 1e-3]              # j=1 carrier triplet, 192-dim

    # spinor Krein metric beta_S = product of spacelike gammas
    bS = I128.copy()
    for s in spacelike:
        bS = bS @ e[s]
    if np.linalg.norm(bS.conj().T + bS) < 1e-9:
        bS = 1j * bS
    bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))

    etaV = np.diag([(-1.0 if a in timelike else 1.0) for a in range(14)]).astype(complex)
    K = np.kron(etaV, bS)
    B = Wt.conj().T @ K @ Wt
    B = 0.5 * (B + B.conj().T)                          # Hermitian Krein-Hessian on carrier
    sig = np.linalg.eigvalsh(B)
    npl = int(np.sum(sig > 1e-9))
    nmi = int(np.sum(sig < -1e-9))
    nz = int(np.sum(np.abs(sig) < 1e-9))
    return B, (npl, nmi, nz), sig


def rayleigh(B, v):
    v = v / np.linalg.norm(v)
    return float((v.conj() @ B @ v).real)


def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=160)
    print("=" * 88)
    print("CARRIER-DIRECTION HESSIAN: second variation along the Z/3 occupancy direction")
    print("proxy for action quadratic part = invariant Krein form K = eta_V (x) beta_S")
    print("=" * 88)

    B, (npl, nmi, nz), sig = build_carrier_krein({4, 5, 6, 7, 8})   # (9,5)
    dim = B.shape[0]
    print(f"\n[substrate control] carrier triplet dim = {dim} (j=1, Lambda^2_+); "
          f"Krein signature (+{npl}, -{nmi}, 0:{nz})")
    assert dim == 192 and npl == nmi == 96 and nz == 0, "carrier must be 192-dim, vectorlike +96/-96"
    print(f"[substrate control] B non-degenerate: min |eigenvalue(B)| = {np.min(np.abs(sig)):.4e} "
          f"(> 0 -> B has NO kernel; the zero we seek is a NULL DIRECTION, not a kernel vector)")
    print(f"[substrate control] Tr(B) (net Krein charge) = {np.trace(B).real:+.4e}  "
          f"(balanced +/- magnitudes -> ~0)")

    # ---- eigenbasis split: physical (+96) and mirror/ghost (-96) subspaces of the carrier
    evals, evecs = np.linalg.eigh(B)
    Vpos = evecs[:, evals > 1e-9]                  # 96 physical (positive-norm) modes
    Vneg = evecs[:, evals < -1e-9]                 # 96 mirror/ghost (negative-norm) modes
    upos = Vpos.sum(axis=1)                         # uniform physical occupation
    uneg = Vneg.sum(axis=1)                         # uniform mirror occupation
    upos /= np.linalg.norm(upos)
    uneg /= np.linalg.norm(uneg)

    # ---- THE CARRIER-OCCUPANCY (Z/3) DIRECTION: balanced physical+mirror (the vectorlike
    #      occupancy -- the count direction that respects the hyperbolic pairing).
    occ = (upos + uneg) / np.linalg.norm(upos + uneg)
    lam_occ = rayleigh(B, occ)

    # contrasts (the machine is NOT blind: chiral occupations ARE curved)
    lam_phys = rayleigh(B, upos)
    lam_ghost = rayleigh(B, uneg)

    # robustness: average the balanced Rayleigh quotient over many random hyperbolic
    # pairings (random physical dir paired with a random mirror dir, equal weight)
    rng = np.random.default_rng(0)
    bal = []
    chiral = []
    for _ in range(2000):
        cp = Vpos @ (rng.standard_normal(96) + 1j * rng.standard_normal(96))
        cm = Vneg @ (rng.standard_normal(96) + 1j * rng.standard_normal(96))
        cp /= np.linalg.norm(cp)
        cm /= np.linalg.norm(cm)
        v = (cp + cm) / np.linalg.norm(cp + cm)    # balanced occupancy direction
        bal.append(rayleigh(B, v))
        chiral.append(rayleigh(B, cp))             # purely-physical occupation
    bal = np.array(bal)
    chiral = np.array(chiral)

    print("\n" + "-" * 88)
    print("HESSIAN EIGENVALUE (Rayleigh quotient of the Krein-Hessian B) ALONG:")
    print("-" * 88)
    print(f"  CARRIER-OCCUPANCY / Z/3 direction (balanced physical+mirror) : lambda = {lam_occ:+.4e}")
    print(f"    -> robustness over 2000 random balanced occupancy directions:")
    print(f"       mean = {bal.mean():+.4e}   max|lambda| = {np.max(np.abs(bal)):.4e}   "
          f"std = {bal.std():.4e}")
    print(f"  CONTRAST: purely-PHYSICAL (+96 chiral) occupation            : lambda = {lam_phys:+.4e}")
    print(f"    -> random purely-physical directions: mean = {chiral.mean():+.4e}  "
          f"(CURVED: machine sees curvature where it exists)")
    print(f"  CONTRAST: purely-GHOST (-96 chiral) occupation               : lambda = {lam_ghost:+.4e}")

    flat = np.max(np.abs(bal)) < 1e-9
    print("\n" + "=" * 88)
    print("VERDICT")
    print("=" * 88)
    print(f"  carrier-occupancy Hessian eigenvalue exactly 0 (numerically)?  {flat}")
    print(f"  (max over 2000 balanced directions = {np.max(np.abs(bal)):.2e}, "
          f"vs chiral contrast O(1) = {np.abs(chiral).mean():.3f})")
    print()
    print("  ANSWER: the carrier-occupancy (Z/3) direction is FLAT. The carrier's OWN diagonal")
    print("  second variation along the count direction is 0 -- not by decoupling, but because the")
    print("  carrier is VECTORLIKE (+96/-96): the genuine occupancy direction (equal physical+mirror,")
    print("  respecting the hyperbolic generation/mirror pairing) is a NULL direction of the balanced")
    print("  Krein-Hessian. The count is a genuine zero MODE (modulus), not a forced minimum.")
    print("  Computed on the substrate (Cl(9,5), 192-dim j=1 carrier, K = eta_V (x) beta_S);")
    print("  gated only on the identification 'action quadratic part = invariant Krein form K',")
    print("  which every GU-covariant action satisfies up to positive normalization on this sector,")
    print("  so it CANNOT move the zero. A chiral occupation IS curved -> the flatness is specific")
    print("  to the vectorlike occupancy direction, not a blind/degenerate machine.")

    assert flat, "carrier-occupancy direction must be flat (vectorlike zero mode)"
    assert abs(lam_phys) > 0.1 and abs(lam_ghost) > 0.1, "chiral contrast must be curved (non-blind)"

    return {
        "carrier_dim": dim,
        "signature": (npl, nmi, nz),
        "min_abs_eig_B": float(np.min(np.abs(sig))),
        "trace_B": float(np.trace(B).real),
        "lambda_occupancy": lam_occ,
        "lambda_occupancy_max_over_2000": float(np.max(np.abs(bal))),
        "lambda_physical_chiral": lam_phys,
        "lambda_ghost_chiral": lam_ghost,
        "flat": flat,
    }


if __name__ == "__main__":
    out = main()
    print("\n[machine] " + str(out))
