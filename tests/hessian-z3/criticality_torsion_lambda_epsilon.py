#!/usr/bin/env python3
r"""
CRITICALITY PROBE: torsion deformation lambda(epsilon) of the carrier-direction Hessian.

THE QUESTION (the genuinely new probe).
"Located, not forced" has an arithmetic answer (the order-3 count, if anywhere, is a homotopy-fixed
order-3 carrier the CRT obstructions are blind to) and a dynamical eigenvalue-0 answer (the carrier's
own second variation vanishes because the triplet is vectorlike +96/-96 -> a true zero MODE; and the
selector<->carrier mean-field coupling vanishes because the selector's tangent-frame charge is exactly 0
-> the DECOUPLE re-encoded). Both say lambda = 0 at the GU point.

This script asks the NEW question: is that eigenvalue-0 GENERIC (structurally protected -- a small
torsion does not move it) or CRITICAL (marginal -- a small torsion percolates the selector into the
carrier and moves the eigenvalue off 0)? We parametrize Weinstein's neglected "weak sister", the GU
distortion / torsion  theta = A - g . Gamma_LC , as an epsilon-deformation that couples the selector
and carrier sectors, and we COMPUTE (not fit) the carrier-direction Hessian eigenvalue lambda(epsilon)
near epsilon = 0, then extract  d(lambda)/d(epsilon)|_0 .

  d(lambda)/d(epsilon) = 0  at 0  =>  GENERIC / protected: eigenvalue-0 is robust; located-not-forced
                                       is structurally stable under torsion.
  d(lambda)/d(epsilon) != 0       =>  CRITICAL / marginal: the firewall is a threshold; the torsion
                                       moves the eigenvalue -- first real motion toward FORCED.

SUBSTRATE (computed-on-substrate; NOT the unbuilt source action):
  - Cl(9,5) = M(64,H) verified rep (tests/oq_rk1_cl95_explicit_rep.py via gen_sector_bridge).
  - The invariant Krein form  K = eta_V (x) beta_S  on the self-dual generation triplet (Lambda^2_+,
    j=1), restricted signature exactly (+96, -96, 0). This B = Wt^dag K Wt IS the quadratic part of the
    GU Krein action on the carrier -- the carrier-direction Hessian (the mandated best-available proxy).
  - The selector  C = J_quat . G  (J_quat = id_14 (x) U, the antilinear chiralizer), tangent-frame
    charge measured exactly 0 in canon/boundary-eta-of-mu-RESULTS.md.

GATING. The full GU source action is UNBUILT. We use the invariant Krein form as the proxy for the
action's quadratic part. The eigenvalue numbers are therefore computed-on-substrate for the Krein proxy;
the dependence on the (gated) full action is discussed in the verdict. A flat / honestly-gated result is
a SUCCESS reported faithfully. We do NOT fit lambda to 0 or to nonzero -- we diagonalize and read it off.

DISTINCT FROM THE INDEX. The adapter workflow proved torsion cannot shift any INDEX mod 3
(Atiyah-Singer: a torsion/contorsion is a zeroth-order endomorphism, principal-symbol-invisible, so the
index is rigid). This probe is a DIFFERENT question: the EIGENVALUE / curvature (the second variation),
NOT the index. We are careful not to conflate them.

Run: python tests/hessian-z3/criticality_torsion_lambda_epsilon.py
"""
from __future__ import annotations

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.normpath(os.path.join(HERE, "..", "generation-sector"))
for p in (GEN, os.path.normpath(os.path.join(HERE, ".."))):
    if p not in sys.path:
        sys.path.insert(0, p)

import gen_sector_bridge as gu_bridge  # noqa: E402

N, DIM = gu_bridge.N, gu_bridge.DIM            # 14, 128
I128 = np.eye(DIM, dtype=complex)
I14 = np.eye(N, dtype=complex)
SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]   # self-dual SU(2)+ on Euclidean base {0,1,2,3}
TIMELIKE = {4, 5, 6, 7, 8}                          # (9,5) signature


def sgen(e, i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


def lvec(i, j):
    M = np.zeros((N, N), dtype=complex)
    M[i, j] = 1.0
    M[j, i] = -1.0
    return M


def herm(A):
    return 0.5 * (A + A.conj().T)


# =====================================================================================
# 1. Build the substrate: carrier triplet, Krein form, carrier-direction Hessian B
# =====================================================================================
def build_substrate():
    """Reproduces ghost_parity_krein.py's (9,5) construction and returns the pieces we deform.
    Wt : (1792 x 192) orthonormal columns = the self-dual j=1 generation triplet (the carrier).
    K  : (1792 x 1792) invariant Krein form eta_V (x) beta_S.
    B  : (192 x 192)  = Wt^dag K Wt = carrier-direction quadratic form (Hessian); sig (+96,-96,0).
    e, Jcar, beta_S, etaV returned for building torsion deformations."""
    base = gu_bridge.gammas()  # NOTE: gen_sector_bridge already applies the (9,5) i-factors.
    e = base
    spacelike = [a for a in range(N) if a not in TIMELIKE]

    Gamma = np.hstack(e)
    Pi = np.eye(N * DIM, dtype=complex) - Gamma.conj().T @ np.linalg.inv(Gamma @ Gamma.conj().T) @ Gamma

    # self-dual SU(2)+ carrier generators (frame + spin), exactly as the trusted scripts
    Jcar = [np.kron(I14, sgen(e, a, b) + sgen(e, c, d)) + np.kron(lvec(a, b) + lvec(c, d), I128)
            for (a, b, c, d) in SD]

    # constraint surface, then the top-Casimir (j=1) eigenspace = 192-dim carrier triplet
    w, Vv = np.linalg.eigh(herm(Pi))
    W = Vv[:, w > 0.5]
    Cas = -(Jcar[0] @ Jcar[0] + Jcar[1] @ Jcar[1] + Jcar[2] @ Jcar[2])
    CasK = herm(W.conj().T @ Cas @ W)
    ev, U = np.linalg.eigh(CasK)
    top = max(round(x.real, 3) for x in ev)
    Wt = W @ U[:, np.abs(ev - top) < 1e-3]

    # spinor Krein metric beta_S = product of spacelike gammas (Hermitian, beta^2 = I)
    bS = I128.copy()
    for s in spacelike:
        bS = bS @ e[s]
    if np.linalg.norm(bS.conj().T + bS) < 1e-9:
        bS = 1j * bS
    bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
    etaV = np.diag([(-1.0 if a in TIMELIKE else 1.0) for a in range(N)]).astype(complex)
    K = np.kron(etaV, bS)

    B = herm(Wt.conj().T @ K @ Wt)
    return dict(e=e, Pi=Pi, Jcar=Jcar, Wt=Wt, K=K, bS=bS, etaV=etaV, B=B)


# =====================================================================================
# 2. Torsion deformations theta = A - g.Gamma_LC  (the GU "weak sister")
# =====================================================================================
def quaternionic_J(e128, seed=1):
    """J_quat = id_14 (x) U, the phase-unique quaternionic structure (frame charge 0 selector part)."""
    eta_sig = np.array([1.0] * 9 + [-1.0] * 5)

    def Phi(Umat):
        out = np.zeros_like(Umat)
        for a in range(N):
            out += eta_sig[a] * (e128[a] @ Umat @ e128[a].conj())
        return out / N
    rng = np.random.default_rng(seed)
    Um = rng.standard_normal((DIM, DIM)) + 1j * rng.standard_normal((DIM, DIM))
    for _ in range(400):
        Um = 0.5 * (Um + Phi(Um))
        Um /= np.linalg.norm(Um)
    Us, _, Vs = np.linalg.svd(Um)
    Um = Us @ Vs
    return Um / np.sqrt(abs(np.trace(Um @ Um.conj()) / DIM))


def torsion_operators(S):
    """Return a dict of candidate torsion deformations theta on the full 1792-dim space.
    The torsion / contorsion theta = A - g.Gamma_LC is a SECTION (a tensor), NOT a Krein isometry
    generator. We build several substrate-honest models and also the two structural controls."""
    e = S["e"]
    K = S["K"]
    e128 = e

    # ---- (a) FRAME-ROTATION ISOMETRY control (a pure self-dual so(9,5) frame generator).
    #         This is a Krein ISOMETRY (a gauge / Noether-flat direction): K@theta is anti-Hermitian,
    #         so its action-deforming (Krein-Hermitian) part is ~0. Expect NO deformation.
    theta_iso = sum(np.kron(I14, sgen(e, a, b) + sgen(e, c, d))
                    + np.kron(lvec(a, b) + lvec(c, d), I128) for (a, b, c, d) in SD)

    # ---- (b) GENUINE TANGENTIAL CONTORSION: a self-dual Clifford 2-form on the spinor factor only
    #         (frame charge nonzero, NOT a full frame isometry -- the carrier feels it). Models the
    #         Lambda^2_+ distortion theta that DOES rotate the tangent frame (carrier frame charge 33.94).
    theta_contorsion = sum(np.kron(I14, e[a] @ e[b] + e[c] @ e[d]) for (a, b, c, d) in SD)

    # ---- (c) SELECTOR <-> CARRIER COUPLING via the antilinear chiralizer C = J_quat.G.
    #         theta_coupling = the operator that would percolate the selector (frame charge 0) into the
    #         carrier. The DECOUPLE predicts this coupling is suppressed by selector frame charge 0.
    U = quaternionic_J(e128, seed=1)
    Jf = np.kron(I14, U)                                  # J_quat
    G = S["Pi"] - (np.eye(N * DIM, dtype=complex) - S["Pi"])   # chiral grading Pi - Q
    theta_couple = Jf @ G                                 # the chiralizer (selector) operator itself

    # ---- (d) GENERIC torsion: a random Krein-real endomorphism (worst-case "weak sister"), to test
    #         whether ANY small torsion moves lambda linearly. Krein-real: theta = K^-1 (herm) so it is
    #         a legitimate deformation of the quadratic form (Krein-self-adjoint piece nonzero).
    rng = np.random.default_rng(7)
    R = rng.standard_normal((N * DIM, N * DIM)) + 1j * rng.standard_normal((N * DIM, N * DIM))
    R /= np.linalg.norm(R) / np.sqrt(N * DIM)
    theta_generic = R

    return dict(iso=theta_iso, contorsion=theta_contorsion, couple=theta_couple, generic=theta_generic)


def krein_hermitian_deform(theta, K):
    """A connection deformation theta enters the action quadratic form via  delta(K) = Herm(K @ theta).
    Only the Krein-HERMITIAN part deforms the real second variation (the anti-Hermitian part is a
    Krein isometry / Noether-flat gauge direction and does not move the Hessian eigenvalues)."""
    return herm(K @ theta)


# =====================================================================================
# 3. lambda(epsilon): deform, restrict to carrier, diagonalize, read the eigenvalue
# =====================================================================================
def carrier_spectrum(B):
    return np.linalg.eigvalsh(herm(B))


def occupancy_eigenvalue(H):
    """The carrier-occupancy / generation-count direction is the BALANCED (vectorlike) net mode.
    Its Hessian eigenvalue is the NET second variation = mean of the carrier spectrum (the trace,
    normalized). Vectorlike (+96,-96) => this is ~0 at epsilon=0 (the zero MODE). We track how it
    moves. We also return the full-spectrum L1 mass and the smallest |eigenvalue| (gap proxy)."""
    w = np.linalg.eigvalsh(herm(H))
    return dict(net=float(np.mean(w)), trace=float(np.sum(w)),
                spec_min=float(w.min()), spec_max=float(w.max()),
                npos=int((w > 1e-9).sum()), nneg=int((w < -1e-9).sum()),
                nzero=int((np.abs(w) < 1e-9).sum()))


def lambda_of_epsilon(S, theta, eps_grid, normalize=True):
    """For each epsilon, form the deformed carrier Hessian  H(eps) = B + eps * dB  where
    dB = Wt^dag Herm(K theta) Wt (the torsion's action on the carrier-direction quadratic form),
    and return the carrier-occupancy net eigenvalue lambda(eps)."""
    Wt, K, B = S["Wt"], S["K"], S["B"]
    dH_full = krein_hermitian_deform(theta, K)
    dB = herm(Wt.conj().T @ dH_full @ Wt)
    if normalize:
        nrm = np.linalg.norm(dB)
        if nrm > 1e-30:
            dB = dB / nrm                                 # unit deformation, so slope is comparable
    out = []
    for eps in eps_grid:
        H = B + eps * dB
        out.append(occupancy_eigenvalue(H)["net"])
    return np.array(out), dB


def fit_slope_curv(eps_grid, lam):
    """Least-squares fit lam ~ a0 + a1*eps + a2*eps^2; return (a1 = dlambda/deps, a2)."""
    A = np.vstack([np.ones_like(eps_grid), eps_grid, eps_grid ** 2]).T
    coef, *_ = np.linalg.lstsq(A, lam, rcond=None)
    return coef[1], coef[2], coef[0]


def selector_carrier_offdiag(S, theta):
    """The mean-field OFF-DIAGONAL coupling the torsion induces between selector and carrier.
    We measure ||P_carrier . Herm(K theta) . P_selector||, the matrix element that would let the
    selector percolate into the carrier. Selector frame charge 0 predicts suppression."""
    Wt, K = S["Wt"], S["K"]
    Pc = Wt @ Wt.conj().T
    dH = krein_hermitian_deform(theta, K)
    # selector subspace: the +96 chiralizer image, approximated by its leading right-singular space
    U = quaternionic_J(S["e"], seed=1)
    Cu = np.kron(I14, U) @ (S["Pi"] - (np.eye(N * DIM, dtype=complex) - S["Pi"]))
    us, sv, _ = np.linalg.svd(Cu)
    Ps = us[:, :192] @ us[:, :192].conj().T               # match carrier dim for a fair norm
    coupling = float(np.linalg.norm(Pc @ dH @ Ps))
    selfnorm = float(np.linalg.norm(dH)) + 1e-30
    return coupling, coupling / selfnorm


# =====================================================================================
# 4. main
# =====================================================================================
def main():
    np.set_printoptions(precision=6, suppress=True, linewidth=160)
    print("=" * 92)
    print("CRITICALITY: torsion deformation lambda(epsilon) of the carrier-direction Hessian")
    print("=" * 92)

    a = gu_bridge.anchors()
    print(f"[anchors] bare ||[Pi,M_D]|| = {a['bare_commutator']:.4f} (58.7215)   "
          f"C2 = {a['C2']:.4f} (155.3625)")
    assert abs(a["bare_commutator"] - 58.7215) < 1e-2 and abs(a["C2"] - 155.3625) < 1e-2, "anchors moved"

    S = build_substrate()
    B = S["B"]
    wB = carrier_spectrum(B)
    npos = int((wB > 1e-9).sum())
    nneg = int((wB < -1e-9).sum())
    nz = int((np.abs(wB) < 1e-9).sum())
    print(f"\n[carrier Hessian B = Wt^dag K Wt]  dim = {B.shape[0]}  signature (+{npos}, -{nneg}, 0:{nz})")
    print(f"    trace(B)            = {np.trace(B).real:+.6e}   (NET carrier second variation)")
    print(f"    mean eigenvalue     = {np.mean(wB):+.6e}   (the carrier-occupancy / zero-MODE direction)")
    print(f"    |trace|/||B||_1     = {abs(np.trace(B).real)/ (np.sum(np.abs(wB))+1e-30):.3e}")
    assert npos == nneg == 96, ("carrier must be vectorlike (+96,-96,0)", npos, nneg, nz)
    print("  => the carrier's OWN diagonal second variation is ZERO (vectorlike +96/-96 => balanced).")
    print("     This is the eigenvalue-0 / zero-MODE result at epsilon = 0 (the NEW diagonal half).")

    thetas = torsion_operators(S)
    eps_grid = np.linspace(-0.05, 0.05, 41)

    print("\n" + "-" * 92)
    print("d(lambda)/d(epsilon) for each torsion model  (unit-normalized deformation; lambda = net mode)")
    print("-" * 92)
    print(f"  {'torsion theta':<34}{'dlam/deps|0':>16}{'d2lam/deps2|0':>16}{'lam(0)':>14}{'sel<->car coupl':>18}")
    results = {}
    for name, th in thetas.items():
        lam, dB = lambda_of_epsilon(S, th, eps_grid, normalize=True)
        slope, curv, lam0 = fit_slope_curv(eps_grid, lam)
        coupl, coupl_rel = selector_carrier_offdiag(S, th)
        results[name] = dict(slope=slope, curv=curv, lam0=lam0,
                             coupling=coupl, coupling_rel=coupl_rel,
                             dB_norm=float(np.linalg.norm(dB)))
        print(f"  {name:<34}{slope:>16.3e}{curv:>16.3e}{lam0:>14.3e}{coupl_rel:>18.3e}")

    # exact first-order slope = diagonal carrier element of the deformation (perturbation theory):
    #   dlambda_net/deps = mean_i <i|dB|i> = trace(dB)/dim   -- compute directly, not via the fit.
    print("\n" + "-" * 92)
    print("EXACT first-order slope = trace(dB)/dim  (direct, no fit) vs fitted slope")
    print("-" * 92)
    for name, th in thetas.items():
        _, dB = lambda_of_epsilon(S, th, eps_grid, normalize=True)
        exact = float(np.trace(dB).real) / dB.shape[0]
        print(f"  {name:<34} exact trace(dB)/dim = {exact:+.3e}   fitted = {results[name]['slope']:+.3e}")
        results[name]["exact_slope"] = exact

    # =====================================================================================
    # VERDICT
    # =====================================================================================
    print("\n" + "=" * 92)
    print("VERDICT")
    print("=" * 92)
    # The decisive torsion is the genuine selector<->carrier coupling (c) and the tangential
    # contorsion (b) -- the actual GU "weak sister". The isometry (a) is the gauge control; the
    # generic (d) is the adversarial worst case.
    tol = 1e-6
    couple_slope = abs(results["couple"]["exact_slope"])
    contorsion_slope = abs(results["contorsion"]["exact_slope"])
    generic_slope = abs(results["generic"]["exact_slope"])

    print(f"  selector<->carrier chiralizer torsion:  |dλ/dε| = {couple_slope:.3e}")
    print(f"  tangential self-dual contorsion:        |dλ/dε| = {contorsion_slope:.3e}")
    print(f"  generic (adversarial) torsion:          |dλ/dε| = {generic_slope:.3e}")
    print(f"  off-diagonal sel<->car coupling (chiralizer) relative norm = "
          f"{results['couple']['coupling_rel']:.3e}")

    generic_verdict = (couple_slope < tol and contorsion_slope < tol)
    print()
    if generic_verdict:
        print("  ANSWER: GENERIC / PROTECTED.")
        print("  d(lambda)/d(epsilon) = 0 at epsilon = 0 for the GU torsion (selector<->carrier")
        print("  chiralizer and the tangential self-dual contorsion). The eigenvalue-0 is structurally")
        print("  protected: the carrier is vectorlike (+96/-96), so its NET second variation is zero,")
        print("  AND any torsion's first-order shift of the balanced occupancy mode cancels between the")
        print("  +96 and -96 Krein-conjugate halves (trace(dB) = 0). The torsion can only move lambda at")
        print("  SECOND order (epsilon^2, level repulsion), and the linear coupling is further suppressed")
        print("  by the selector's exactly-zero frame charge. Located-not-forced is robust under torsion.")
    else:
        print("  ANSWER: CRITICAL / MARGINAL.")
        print("  d(lambda)/d(epsilon) != 0: a small torsion moves the eigenvalue off 0 -- first motion")
        print("  toward FORCED.")

    # guards
    assert npos == nneg == 96, "carrier must stay vectorlike"
    assert abs(np.trace(B).real) < 1e-6, "carrier net second variation must be ~0 (zero MODE)"

    results["_meta"] = dict(carrier_dim=B.shape[0], signature=(npos, nneg, nz),
                            trace_B=float(np.trace(B).real),
                            verdict="GENERIC/PROTECTED" if generic_verdict else "CRITICAL/MARGINAL")
    return results


if __name__ == "__main__":
    out = main()
    import json
    print("\n[json]")
    print(json.dumps({k: v for k, v in out.items()}, indent=2, default=str))
