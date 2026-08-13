#!/usr/bin/env python3
"""M-H9 Tier 0 certificate: the base FS-type indicator flips between horns.

VERDICT on pass: BASE-FS-INDICATOR-FLIPS-BETWEEN-HORNS__FIBRE-UNCHANGED

Register item M-H9 asks for the ten `delta_e` mirror-edge sign invariants that
select among the eleven pairs (58,78) ... (78,58) of
`explorations/shiab-operator/b5-krein-mirror-orbit-reduction-2026-07-25.md`.
Two corrections to that item, both established 2026-08-08:

  (a) M-H9 NAMES THE WRONG MODULE.  The Racah-Speiser machinery in
      tests/shiab_b5_observer_symbol_multiplicity_matrix.py is complexified and
      signature-blind (its own docstring fixes H_C = Spin(4,C) x Spin(10,C)).
      It carries no conjugation, no real structure and no pairing, so it cannot
      emit a Frobenius-Schur indicator, and rerunning it under (7,7) returns
      bit-identical output.  The sign-carrying object is `C_perp = K . J_obs`
      in tests/channel-swings/full20_dewitt_loop_transport_probe.py.

  (b) M-H9 IS ALREADY HALF DONE.  full20_dewitt_loop_transport_probe.py
      (committed 2026-07-30, green) forces all ten `delta_e` EQUAL via
      Gamma-naturality plus the 136 written coefficient intertwiners, so `k` is
      already restricted to {0,10} -- endpoints only.  Both the improvement
      register and the Layer-0 fork registry still describe the residual as
      eleven pairs.

What remains is therefore ONE RELATIVE BIT, and this certificate computes it.

WHY ONLY A RELATIVE BIT.  (9,5) and (7,7) differ only in the base, (3,1) versus
(1,3): the DeWitt fibre form is quadratic in `g`, so it stays (6,4) under
`g -> -g`.  And per
`explorations/dc-h1-orbit-signs-monodromy-check-2026-08-04.md`, under `C -> -C`
the even and breaking subspaces exchange (`d -> 136 - d`, i.e. 58 <-> 78) and
that sign is a nontrivial holonomy class `w != 0` in `H^1(F;Z/2)` with NO GLOBAL
SECTION.  Only the unordered pair is loop-invariant.  So an absolute ordered
claim "(9,5) => (58,78)" is not well posed; the decisive, well-posed quantity is
the RELATIVE sign between the two horns.  This certificate computes that and
asserts nothing absolute.

PREREGISTERED BEFORE RUNNING.  Expected: the two horns give OPPOSITE
`J . conj(J)` signs, since Cl(3,1) = M(4,R) is real type while Cl(1,3) = M(2,H)
is quaternionic; and the (6,4) fibre is unchanged.  A SAME sign on both bases
would falsify the endpoint-flip mechanism.  Independent prior certification of
those real forms: tests/channel-swings/p77_real_index_twin.py (A4, A5).
"""

import importlib.util
import sys

import numpy as np

PROBE = "tests/channel-swings/full20_dewitt_loop_transport_probe.py"

_spec = importlib.util.spec_from_file_location("f20", PROBE)
_f20 = importlib.util.module_from_spec(_spec)
sys.modules["f20"] = _f20
_spec.loader.exec_module(_f20)


def fs_sign(positive: int, negative: int):
    """Return (s, residual, dim) with J . conj(J) = s * I for the commuting real structure."""
    gammas, _eta = _f20.signed_gammas(positive, negative)
    real_structure = _f20.commuting_real_structure(gammas)
    squared = real_structure @ real_structure.conj()
    dim = squared.shape[0]
    for candidate in (+1.0, -1.0):
        residual = _f20.max_abs(squared - candidate * np.eye(dim))
        if residual < 1e-9:
            return int(candidate), float(residual), dim
    return None, float(_f20.max_abs(squared)), dim


def main() -> None:
    print("=" * 78)
    print("M-H9 Tier 0 -- base Frobenius-Schur indicator, relative between horns")
    print("=" * 78)

    print("\nBASE (the only structure that differs between the two horns):")
    base = {}
    for label, (p, q) in {
        "(3,1)  base of the (9,5) horn": (3, 1),
        "(1,3)  base of the (7,7) horn": (1, 3),
    }.items():
        sign, residual, dim = fs_sign(p, q)
        base[(p, q)] = sign
        print(f"  {label}: J.conj(J) = {sign:+d} I   (dim {dim}, residual {residual:.2e})")

    print("\nFIBRE (control -- asserted unchanged across horns):")
    fibre_sign, fibre_residual, fibre_dim = fs_sign(6, 4)
    print(f"  (6,4) DeWitt fibre           : J.conj(J) = {fibre_sign:+d} I"
          f"   (dim {fibre_dim}, residual {fibre_residual:.2e})")

    s31, s13 = base[(3, 1)], base[(1, 3)]
    flips = s31 != s13
    print(f"\nRELATIVE base sign, (3,1) vs (1,3): "
          f"{'OPPOSITE -> endpoint flip' if flips else 'SAME -> no flip; mechanism FALSIFIED'}")

    assert s31 == +1, f"Cl(3,1) must be real type (+1), got {s31}"
    assert s13 == -1, f"Cl(1,3) must be quaternionic type (-1), got {s13}"
    assert fibre_sign == +1, f"Cl(6,4) fibre must be real type (+1), got {fibre_sign}"
    assert flips, "PREREGISTERED MECHANISM FALSIFIED: both bases give the same FS sign"

    print("\nVERDICT: BASE-FS-INDICATOR-FLIPS-BETWEEN-HORNS__FIBRE-UNCHANGED")
    print("\nSCOPE, and it is narrow:")
    print("  * RELATIVE sign only. No absolute (58,78) / (78,58) assignment is made")
    print("    or implied; per dc-h1 that is loop-monodromy dependent.")
    print("  * This is the BASE indicator. Propagating it through the actual")
    print("    C_perp and the 136 written coefficient intertwiners is Tier 1 and")
    print("    is NOT done here.")
    print("  * Tier 1 requires RE-DERIVING mixed_rotation()'s hardcoded")
    print("    timelike_leg = 3 for the (1,3) base -- relabelling it produces an")
    print("    artefact sign rather than a result.")
    print("  * Nothing here settles SIGNATURE-AMBIENT, moves a ledger row, or")
    print("    bears on the generation count.")


if __name__ == "__main__":
    main()
