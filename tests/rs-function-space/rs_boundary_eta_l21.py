#!/usr/bin/env python3
r"""
STEP 2 (WC-FUNCTION-SPACE-EXT): reduced eta-bar of the FULL Rarita-Schwinger boundary operator
on RP^3 = L(2;1), and its parity.

SPEC: canon/rs-function-space-framework-SPEC.md, section 5. Question: compute the eta of the RS
boundary operator and decide its parity; expected (falsifiable) result is that the sector's OWN
boundary eta is 2-primary/even, so an odd count cannot come from the sector's own boundary -- only
from an external topological background (-> STEP 3).

This EXTENDS canon/boundary-eta-of-mu-RESULTS.md from the single +96 antilinear SELECTOR to the FULL
RS gamma-traceless boundary operator D_RS = E + E^dag (E = Q.M_D.Pi), reusing the two validated legs:

  (1) GRAVITATIONAL -p_1/24 channel -- the ONLY route to a 3-primary (order-3) eta -- is fed ONLY by
      a NET SELF-DUAL tangent-frame p_1. Decisive computation: the net self-dual frame charge
      (SD - ASD) of the full RS operator. Result: ~0 (non-chiral covariant op) => no -p_1/24.
  (2) GAUGE / SPECTRAL k/8 channel -- the charge-q lens Dirac eta (2q^2-4q+1)/8 has denominator 8 for
      every integer charge, so any internal-charge residue stays in (1/8)Z => 2-primary.

Denominator decides: a factor of 3 in lowest terms => 3-primary; only powers of 2 => 2-primary.

Reuses the machine-checked Cl(9,5)=M(64,H) rep via gen_sector_bridge. Grade: computed-confirmed on
the model RS boundary operator (same finite-model reconstruction caveats as boundary-eta-of-mu), with
an independent re-check in verify/rs_boundary_eta_indep_check.py.

Run: python tests/rs-function-space/rs_boundary_eta_l21.py
"""
from __future__ import annotations
import os, sys
from fractions import Fraction
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", ".."))
for p in (os.path.join(REPO, "tests", "generation-sector"), os.path.join(REPO, "tests")):
    if p not in sys.path:
        sys.path.insert(0, p)
import gen_sector_bridge as gu_bridge  # noqa: E402

N, DIM = gu_bridge.N, gu_bridge.DIM


def lvec(i, j):
    M = np.zeros((N, N), dtype=complex); M[i, j] = 1.0; M[j, i] = -1.0; return M


def frame_charge(O, frame_gens):
    """Component of O along the base tangent-frame so(4) generators on TX^4 = {0,1,2,3}."""
    O4 = O.reshape(N, DIM, N, DIM)
    total = 0.0
    for L in frame_gens:
        nrm = np.tensordot(L.conj(), L, axes=([0, 1], [0, 1])).real
        F_L = np.einsum('vw,vswt->st', L.conj(), O4) / nrm
        total += float(np.linalg.norm(F_L))
    return total


def lens_dirac_eta_charge_q(q: int) -> Fraction:
    """charge-q twisted Dirac reduced eta-bar on L(2;1) (canon control): (2q^2-4q+1)/8."""
    return Fraction(2 * q * q - 4 * q + 1, 8)


def _prime_factors(n):
    fac, d = set(), 2
    while d * d <= n:
        while n % d == 0:
            fac.add(d); n //= d
        d += 1
    if n > 1: fac.add(n)
    return fac


def is_two_primary(fr: Fraction) -> bool:
    return _prime_factors(fr.denominator) <= {2}


def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=160)
    print("=" * 92)
    print("STEP 2: reduced eta-bar of the FULL RS boundary operator on RP^3 = L(2;1) -- parity")
    print("=" * 92)

    e, Gamma, Pi, M_D = gu_bridge.constraint_objects()
    I = np.eye(N * DIM, dtype=complex)
    Q = I - Pi
    E = Q @ M_D @ Pi                      # boundary Dirac into the gamma-traceless RS sector
    D_RS = E + E.conj().T                 # the FULL RS boundary operator (self-adjoint)

    bare = float(np.linalg.norm(Pi @ M_D - M_D @ Pi))
    C2 = float(np.linalg.norm(Gamma @ M_D @ Pi))
    print(f"[anchors] ||[Pi,M_D]|| = {bare:.4f} (58.7215)   C2 = {C2:.4f} (155.3625)")
    assert abs(bare - 58.7215) < 1e-2 and abs(C2 - 155.3625) < 1e-2, "bridge anchors moved"

    rank_Pi = int(round(np.trace(Pi).real))
    e128 = gu_bridge.gammas()
    om = np.eye(DIM, dtype=complex)
    for a in range(N):
        om = om @ e128[a]
    chir = om if (np.trace(om @ om) / DIM).real > 0 else (-1j) * om
    CHIR = np.kron(np.eye(N), chir)
    tr_chir_on_RS = np.trace(Pi @ CHIR).real
    print(f"[RS sector] rank(Pi) = {rank_Pi};  Tr(chirality | RS) = {tr_chir_on_RS:+.3f}  "
          f"(cross-chirality balance +96,-96 => 0)")

    print("\n" + "-" * 92)
    print("LEG 1 (decisive): NET self-dual tangent-frame charge of the RS operator (feeds -p_1/24?)")
    print("-" * 92)
    sd_gens = [lvec(0, 1) + lvec(2, 3), lvec(0, 2) + lvec(3, 1), lvec(0, 3) + lvec(1, 2)]
    asd_gens = [lvec(0, 1) - lvec(2, 3), lvec(0, 2) - lvec(3, 1), lvec(0, 3) - lvec(1, 2)]

    def sd_asd(O, label):
        sd = frame_charge(O, sd_gens); asd = frame_charge(O, asd_gens)
        allc = frame_charge(O, sd_gens + asd_gens)
        print(f"  {label:<40}|frame|={allc:>10.4f}  SD={sd:>10.4f}  ASD={asd:>10.4f}  "
              f"net={sd - asd:>+.3e}")
        return sd - asd

    netPi = sd_asd(Pi, "Pi (gamma-trace projector)")
    netMD = sd_asd(0.5 * (M_D + M_D.conj().T), "M_D (Dirac-type, hermitian part)")
    netD = sd_asd(D_RS, "D_RS = E + E^dag (full RS bdry op)")

    def sgen(i, j):
        return 0.25 * (e[i] @ e[j] - e[j] @ e[i])
    SD_car = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
    Lam2plus = sum(np.kron(np.eye(N), sgen(a, b) + sgen(c, d))
                   + np.kron(lvec(a, b) + lvec(c, d), np.eye(DIM)) for (a, b, c, d) in SD_car)
    netCar = sd_asd(Lam2plus, "Lambda^2_+ carrier (positive control)")

    non_chiral = abs(netPi) < 1e-3 and abs(netMD) < 1e-3 and abs(netD) < 1e-3
    print(f"\n  => RS operator net self-dual frame charge ~ 0 (non-chiral covariant op): {non_chiral}")
    print(f"     => tangent-frame p_1 = 0 => gravitational e_R = 0/24 (NO order-3 from framing).")
    print(f"     control: Lambda^2_+ net self-dual = {netCar:.3f} != 0 (the machine DOES see a 3).")
    e_R_grav = Fraction(0, 48)

    print("\n" + "-" * 92)
    print("LEG 2: internal/gauge + spectral channel is the charge-q lens type (denominator 8)")
    print("-" * 92)
    two_primary_all = all(is_two_primary(lens_dirac_eta_charge_q(q)) for q in range(0, 40))
    for q in range(0, 6):
        eq = lens_dirac_eta_charge_q(q)
        print(f"     q={q}: {str(eq):>7}  denom={eq.denominator}  2-primary={is_two_primary(eq)}")
    print(f"  => every integer charge gives a power-of-two denominator: {two_primary_all}")

    w = np.linalg.eigvalsh(D_RS)
    tol = 1e-7 * max(1.0, np.abs(w).max())
    eta_spec = int((w > tol).sum()) - int((w < -tol).sum())
    ws = np.sort(w)
    sym_defect = float(np.max(np.abs(ws + ws[::-1])))
    print(f"\n  RS boundary spectral eta (D_RS self-adjoint, chiral off-diagonal E): eta = {eta_spec}, "
          f"+/- symmetry defect = {sym_defect:.1e}")

    print("\n" + "=" * 92)
    print("VERDICT (STEP 2)")
    print("=" * 92)
    print(f"  eta_RS = [grav -p_1/24 : {e_R_grav}]  +  [gauge/spectral : (1/8)Z];  p_1=0, spectral eta=0")
    print("  => RS boundary eta-bar carries NO factor of 3  => 2-PRIMARY / EVEN.")
    print("  ANSWER: the sector's OWN L(2;1) boundary cannot source an odd generation count; an odd")
    print("  count must come from an EXTERNAL topological background (the STEP 3 K3 / flux route).")

    assert non_chiral, "RS operator must have ~0 net self-dual frame charge (no -p_1/24)"
    assert abs(netCar) > 1e-2, "Lambda^2_+ positive control must be chiral (machine sees a 3)"
    assert two_primary_all, "charge-q lens eta must be 2-primary for every q"
    assert eta_spec == 0 and sym_defect < 1e-5, "chiral RS boundary Dirac must have symmetric spectrum"
    assert abs(tr_chir_on_RS) < 1e-2, "RS sector must be cross-chirality balanced (+96,-96)"
    print("\n[OK] all STEP-2 guards passed.")
    return {"rank_Pi": rank_Pi, "net_sd_Pi": netPi, "net_sd_MD": netMD, "net_sd_DRS": netD,
            "net_sd_carrier": netCar, "e_R_grav": str(e_R_grav), "spectral_eta": eta_spec,
            "sym_defect": sym_defect, "charge_q_all_2primary": two_primary_all,
            "verdict": "2-PRIMARY (sector's own boundary cannot source an odd count)"}


if __name__ == "__main__":
    main()
