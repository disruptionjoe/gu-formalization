#!/usr/bin/env python3
"""
WC-FUNCTION-SPACE-EXT APS eta boundary-control probe.

The conditional section-setting theorem in this directory is an interior/closed,
spectral-gapped statement: in the cross-chirality Krein-Dirac class, net chiral spectral
flow is zero. This script models the open APS/noncompact-end residual with a finite
boundary spectrum.

It does not compute the Rarita-Schwinger eta invariant and does not close the work card.
It checks the minimal control:

  * paired/symmetric boundary spectra have eta_0 = 0 and APS half-term 0;
  * paired boundary deformations stay eta-neutral;
  * an external unpaired boundary mode gives a nonzero eta half-term;
  * therefore the interior zero-flow theorem alone cannot decide boundary/end terms.

The next mathematical obligation is to prove that the actual RS boundary/end operator has
the required spectral symmetry, or compute the external eta/family-index contribution.
"""

from __future__ import annotations

import numpy as np


TOL = 1e-12
NASSERT = 0


def check(cond: bool, msg: str) -> None:
    global NASSERT
    NASSERT += 1
    assert cond, msg


def eta_zero_value(spectrum: np.ndarray) -> int:
    """Finite eta at s=0 for a nonzero real spectrum: #positive - #negative."""
    pos = int(np.sum(spectrum > TOL))
    neg = int(np.sum(spectrum < -TOL))
    return pos - neg


def kernel_count(spectrum: np.ndarray) -> int:
    return int(np.sum(np.abs(spectrum) <= TOL))


def aps_half_term(spectrum: np.ndarray) -> float:
    """Model the APS boundary half-term (eta + h) / 2 for a finite spectrum."""
    return 0.5 * (eta_zero_value(spectrum) + kernel_count(spectrum))


def symmetric_boundary(values: np.ndarray) -> np.ndarray:
    values = np.asarray(values, dtype=float)
    check(np.all(values > TOL), "positive representatives required")
    return np.sort(np.r_[-values, values])


def summarize(label: str, spectrum: np.ndarray) -> None:
    print(
        f"  {label}: eta_0={eta_zero_value(spectrum):+d}, "
        f"h={kernel_count(spectrum)}, half-term={aps_half_term(spectrum):+.1f}"
    )


def main() -> None:
    print("=" * 88)
    print("WC-FUNCTION-SPACE-EXT APS eta boundary-control probe")
    print("=" * 88)

    interior_chiral_flow = 0
    print(f"  interior Krein-paired net chiral spectral flow = {interior_chiral_flow:+d}")

    balanced = symmetric_boundary(np.array([0.8, 1.6, 2.5, 4.0]))
    summarize("balanced paired boundary", balanced)
    check(eta_zero_value(balanced) == 0, "paired boundary spectrum has eta_0 = 0")
    check(kernel_count(balanced) == 0, "paired boundary spectrum has no kernel")
    check(aps_half_term(balanced) == 0.0, "paired boundary half-term vanishes")

    paired_deformation = np.sort(np.r_[balanced, [-0.37, 0.37], [-5.2, 5.2]])
    summarize("paired boundary deformation", paired_deformation)
    check(eta_zero_value(paired_deformation) == 0, "paired deformations stay eta-neutral")
    check(aps_half_term(paired_deformation) == 0.0, "paired deformation half-term vanishes")

    external_positive = np.sort(np.r_[balanced, [0.37]])
    summarize("external positive boundary mode", external_positive)
    check(eta_zero_value(external_positive) == 1, "one unpaired positive mode gives eta_0 = +1")
    check(aps_half_term(external_positive) == 0.5, "one unpaired positive mode gives +1/2 half-term")

    external_negative = np.sort(np.r_[balanced, [-0.37]])
    summarize("external negative boundary mode", external_negative)
    check(eta_zero_value(external_negative) == -1, "one unpaired negative mode gives eta_0 = -1")
    check(aps_half_term(external_negative) == -0.5, "one unpaired negative mode gives -1/2 half-term")

    delta_from_right_end = aps_half_term(external_positive) - aps_half_term(balanced)
    print(f"  boundary/end half-term delta from the right end = {delta_from_right_end:+.1f}")
    check(delta_from_right_end == 0.5, "boundary/end term can be nonzero while interior flow is zero")
    check(interior_chiral_flow + delta_from_right_end != 0.0, "interior theorem alone does not settle eta")

    print()
    print("VERDICT: PASS")
    print(
        "  Symmetric or paired boundary spectra keep the modeled APS eta half-term at 0. "
        "An external unpaired boundary mode contributes a nonzero half-term, so the closed/interior "
        "Krein-paired spectral-flow theorem does not by itself close the APS/noncompact-end residual."
    )
    print(
        "  This is an exploration-grade boundary control only: the actual RS boundary/end spectrum "
        "still has to be proved symmetric or computed."
    )
    print(f"  hard asserts passed: {NASSERT}")


if __name__ == "__main__":
    main()
