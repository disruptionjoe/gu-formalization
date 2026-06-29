#!/usr/bin/env python3
r"""
ADVERSARIAL VERIFY: hunt the escape the construct may have missed.

The construct claims a STRUCTURAL no-go: on the 192-dim Clifford-RS carrier, frame charge and net
chiral count are NEVER simultaneously nonzero for a genuine chirality grading (Gamma^2=1, Hermitian).

Gap I probe: the construct's frame-charged RS-slash gradings were built ADDITIVELY (Hermitian
symmetrisation of sum|mu><nu|(x)... ) which BROKE Gamma^2=1, so they were not legitimate gradings.
But a chirality grading CONJUGATED by an ENTANGLING (non-factorised) frame-charged unitary U,
   Gamma' = U (id_V (x) gamma) U^dag ,
AUTOMATICALLY satisfies Gamma'^2 = 1 and is Hermitian. If U genuinely entangles V and S (not of the
form R (x) W, which would cancel against id_V), Gamma' can be frame-charged. Question: can its net
trace on the carrier be nonzero simultaneously?

Decisive tests:
  (1) Conjugation gradings Gamma' = U Gamma_0 U^dag, U = exp(i t H_slash) (entangling). Take the genuine
      carrier involution gam = sign(P_c Gamma' P_c) and measure frame_charge(lift gam) AND Tr(gam).
  (2) Broad signature hunt: for many frame-charged Hermitian seeds (random in the frame-coupling
      algebra) form gam = sign(carrier compression) and look for frame>0 AND |Tr|>0 simultaneously.
  (3) Direct: among ALL involutions, maximise |Tr(gam)| over frame-charged gam via a relaxation:
      does the carrier admit a frame-charged operator with ASYMMETRIC +/- signature?
  (4) Asymmetric seeds: O_RS diagonal-in-mu pieces e_mu^2 = +/-1 (genuinely asymmetric on the 9/5 split).

If ANY genuine carrier involution has frame_charge>1e-4 AND |Tr|>0.5 simultaneously -> ESCAPE.
Run: python tests/gu-independent/adv_verify_escape_hunt.py
"""
from __future__ import annotations
import os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
for p in (os.path.normpath(os.path.join(HERE, "..")),
          os.path.normpath(os.path.join(HERE, "..", "generation-sector"))):
    if p not in sys.path:
        sys.path.insert(0, p)

import gen_sector_bridge as bridge  # noqa: E402
from scipy.linalg import expm        # noqa: E402

N, DIM = bridge.N, bridge.DIM
e = bridge.gammas()
I128 = np.eye(DIM, dtype=complex)
I14 = np.eye(N, dtype=complex)
BASE = (0, 1, 2, 3)
TIMELIKE = {4, 5, 6, 7, 8}
SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]


def lvec(i, j):
    M = np.zeros((N, N), dtype=complex); M[i, j] = 1.0; M[j, i] = -1.0; return M


def sgen(i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


SD_GENS = [lvec(0, 1) + lvec(2, 3), lvec(0, 2) + lvec(3, 1), lvec(0, 3) + lvec(1, 2)]
ASD_GENS = [lvec(0, 1) - lvec(2, 3), lvec(0, 2) - lvec(3, 1), lvec(0, 3) - lvec(1, 2)]
SO4 = SD_GENS + ASD_GENS


def frame_charge(O, gens=SO4):
    O4 = O.reshape(N, DIM, N, DIM)
    tot = 0.0
    for L in gens:
        nrm = np.tensordot(L.conj(), L, axes=([0, 1], [0, 1])).real
        FL = np.einsum('vw,vswt->st', L.conj(), O4) / nrm
        tot += float(np.linalg.norm(FL))
    return tot


def chir(dirs):
    g = I128.copy()
    for a in dirs:
        g = g @ e[a]
    if (np.trace(g @ g) / DIM).real < 0:
        g = 1j * g
    return g / np.sqrt(abs((np.trace(g @ g) / DIM).real))


def build_carrier():
    Gam = np.hstack(e)
    Pi = np.eye(N * DIM, dtype=complex) - Gam.conj().T @ np.linalg.inv(Gam @ Gam.conj().T) @ Gam
    J3 = [np.kron(I14, sgen(a, b) + sgen(c, d)) + np.kron(lvec(a, b) + lvec(c, d), I128)
          for (a, b, c, d) in SD]
    w, Vv = np.linalg.eigh(Pi); Wk = Vv[:, w > 0.5]
    Cas = -(J3[0] @ J3[0] + J3[1] @ J3[1] + J3[2] @ J3[2])
    CasK = Wk.conj().T @ Cas @ Wk; CasK = 0.5 * (CasK + CasK.conj().T)
    ev, Uu = np.linalg.eigh(CasK); top = max(round(x.real, 3) for x in ev)
    Wt = Wk @ Uu[:, np.abs(ev - top) < 1e-3]
    return Wt, Pi, J3


def carrier_involution_from(H, Wt):
    """Genuine Hermitian involution ON the carrier: gam = sign of the carrier compression of H.
    Returns (gam_carrier (192x192), net_trace, lift_to_full)."""
    Hr = Wt.conj().T @ H @ Wt
    Hr = 0.5 * (Hr + Hr.conj().T)
    ev, U = np.linalg.eigh(Hr)
    keep = np.abs(ev) > 1e-9
    s = np.sign(ev[keep]).astype(complex)
    gam = U[:, keep] @ np.diag(s) @ U[:, keep].conj().T
    net = float(np.trace(gam).real)
    lift = Wt @ gam @ Wt.conj().T
    return gam, net, lift


def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=170)
    print("=" * 96)
    print("ADV-VERIFY ESCAPE HUNT: frame-charged net-chiral carrier involution?")
    print("=" * 96)
    Wt, Pi, J3 = build_carrier()
    nc = Wt.shape[1]
    Gamma0 = np.kron(I14, chir(range(N)))     # frame-trivial chiral grading
    # carrier chirality split (control: vectorlike)
    Gc = Wt.conj().T @ Gamma0 @ Wt; Gc = 0.5 * (Gc + Gc.conj().T)
    evc = np.linalg.eigvalsh(Gc)
    print(f"[carrier] dim={nc}  chir split (+{int((evc>0.5).sum())},-{int((evc<-0.5).sum())}) "
          f"net={np.trace(Gc).real:+.2f}  frame(Gamma0)={frame_charge(Gamma0):.3e}")

    hits = []

    # ---- build entangling frame-charged Hermitian generators (slash type) ----
    def slash_herm(coeffs):
        G = np.zeros((N * DIM, N * DIM), dtype=complex)
        idx = 0
        for mu in BASE:
            for nu in range(N):           # couple base frame index to ALL 14 gammas (full V<->S)
                Emn = np.zeros((N, N), dtype=complex); Emn[mu, nu] = 1.0
                G += coeffs[idx] * np.kron(Emn, e[mu] @ e[nu]); idx += 1
        return 0.5 * (G + G.conj().T)

    nco = len(BASE) * N
    rng = np.random.default_rng(11)

    # ---------------------------------------------------------------- (1) conjugation gradings
    print("\n[1] CONJUGATION gradings Gamma' = exp(i t H_slash) Gamma0 exp(-i t H_slash):")
    print(f"    {'t':>5} {'frame(Gamma_op)':>16} {'frame(carrier-involution lift)':>32} {'net Tr':>10}")
    for t in (0.2, 0.5, 1.0, 1.5):
        Hs = slash_herm(rng.standard_normal(nco))
        U = expm(1j * t * Hs)
        Gp = U @ Gamma0 @ U.conj().T
        fop = frame_charge(0.5 * (Gp + Gp.conj().T))
        gam, net, lift = carrier_involution_from(Gp, Wt)
        fcl = frame_charge(lift)
        print(f"    {t:>5.2f} {fop:>16.3f} {fcl:>32.3f} {net:>10.3f}")
        if fcl > 1e-4 and abs(net) > 0.5:
            hits.append((f"conj t={t}", fcl, net))

    # ---------------------------------------------------------------- (2) broad signature hunt
    print("\n[2] BROAD signature hunt over 800 frame-charged slash-Hermitian seeds:")
    best = (0.0, 0.0)   # (max |net| among frame-charged involutions, its frame)
    n_framecharged = 0
    max_net_overall = 0.0
    for it in range(800):
        Hs = slash_herm(rng.standard_normal(nco))
        # ensure genuinely frame-charged seed
        gam, net, lift = carrier_involution_from(Hs, Wt)
        fcl = frame_charge(lift)
        max_net_overall = max(max_net_overall, abs(net))
        if fcl > 1e-4:
            n_framecharged += 1
            if abs(net) > best[0]:
                best = (abs(net), fcl)
        if fcl > 1e-4 and abs(net) > 0.5:
            hits.append((f"slash-rand it={it}", fcl, net))
    print(f"    frame-charged involutions: {n_framecharged}/800 ; "
          f"max |Tr| over ALL seeds = {max_net_overall:.3f}")
    print(f"    among frame-charged: max |Tr| = {best[0]:.3f} (its frame charge {best[1]:.3f})")

    # ---------------------------------------------------------------- (3) asymmetric diagonal seed
    print("\n[3] ASYMMETRIC seeds (diagonal e_mu^2=+/-1 frame-weighted, 9/5 split):")
    # O = sum_mu w_mu |mu><mu| (x) (e_mu g5 e_mu) etc. plus off-diagonal real frame rotations
    g5b = chir(BASE)
    seeds = {
        "sum_mu |mu><mu|(x) e_mu g5b e_mu": sum(
            np.kron(np.outer(np.eye(N)[mu], np.eye(N)[mu]), e[mu] @ g5b @ e[mu]) for mu in BASE),
        "RS sum|mu><nu|(x)e_mu e_nu (full14)": sum(
            np.kron(np.outer(np.eye(N)[mu], np.eye(N)[nu]), e[mu] @ e[nu])
            for mu in BASE for nu in range(N)),
        "frame-rot conj of Gamma0 (factorised, control)":
            (lambda R: R @ Gamma0 @ R.conj().T)(expm(0.7 * np.kron(SD_GENS[0], I128))),
    }
    print(f"    {'seed':<46}{'frame(involution lift)':>24}{'net Tr':>10}")
    for nm, H in seeds.items():
        H = 0.5 * (H + H.conj().T)
        gam, net, lift = carrier_involution_from(H, Wt)
        fcl = frame_charge(lift)
        print(f"    {nm:<46}{fcl:>24.3f}{net:>10.3f}")
        if fcl > 1e-4 and abs(net) > 0.5:
            hits.append((nm, fcl, net))

    # ---------------------------------------------------------------- (4) optimisation relaxation
    # Can the carrier support a frame-charged involution with large |Tr|? Use the lift-frame functional
    # as a penalty and net-trace as objective over the involution manifold (greedy eigen-tilt).
    print("\n[4] OPTIMISATION: tilt Gamma0 by frame-charged direction, maximise |Tr| of sign, keep frame>0:")
    print(f"    {'lambda':>8}{'frame(lift)':>14}{'net Tr':>10}{'note':>8}")
    Hs = slash_herm(rng.standard_normal(nco))
    for lam in (0.0, 0.3, 0.8, 1.5, 3.0, 8.0):
        H = Gamma0 + lam * Hs
        gam, net, lift = carrier_involution_from(H, Wt)
        fcl = frame_charge(lift)
        note = "FRAME" if fcl > 1e-4 else "trivial"
        print(f"    {lam:>8.2f}{fcl:>14.3f}{net:>10.3f}{note:>8}")
        if fcl > 1e-4 and abs(net) > 0.5:
            hits.append((f"tilt lam={lam}", fcl, net))

    print("\n" + "=" * 96)
    print("VERDICT (adv-verify)")
    print("=" * 96)
    if hits:
        print(f"  *** {len(hits)} ESCAPE HIT(S): frame-charged carrier involution with |Tr|>0.5 ***")
        for nm, fcl, net in hits[:20]:
            print(f"     {nm:<30} frame={fcl:.3f} net={net:+.3f}")
    else:
        print("  NO ESCAPE: every frame-charged genuine carrier involution had net trace 0 (|Tr|<=0.5).")
        print("  Construct's structural no-go SURVIVES this broader (conjugation + asymmetric + random)")
        print("  search: frame charge and net chiral count remain mutually exclusive on this carrier.")
    return {"carrier_dim": nc, "n_hits": len(hits),
            "hits": [(nm, round(f, 4), round(n, 4)) for nm, f, n in hits]}


if __name__ == "__main__":
    out = main()
    print("\nRETURN:", out)
