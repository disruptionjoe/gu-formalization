#!/usr/bin/env python3
"""Pure-integer independent check for the SM-boundary anomaly-inflow toy.

This deliberately does not import or execute ``tests/sm-boundary/anomaly_inflow_toy.py``.
The original certificate combines a lattice flux-index check with a bounded search.
This checker re-verifies the boundary-anomaly conclusion by exact integer algebra:

* local U(1)^2 anomaly cancellation forces the linear external count ``Nhat`` even,
  because q^2 == q (mod 2);
* anomaly-free multiplets still realize nonzero even ``Nhat`` values;
* all residues modulo 3 remain reachable, so the local anomaly condition supplies no
  odd-primary / mod-3 selector.

No target generation number is assumed or fitted.
"""

from __future__ import annotations

import itertools
from typing import Iterable


Species = tuple[int, int]  # (integer charge, chirality sign)
Multiplet = tuple[Species, ...]

NASSERT = 0


def check(condition: bool, message: str) -> None:
    global NASSERT
    NASSERT += 1
    assert condition, message


def coefficients(multiplet: Iterable[Species]) -> tuple[int, int, int]:
    """Return (A_grav, A_gauge, Nhat) for a finite Weyl multiplet."""
    items = tuple(multiplet)
    a_grav = sum(chirality for _, chirality in items)
    a_gauge = sum(chirality * charge * charge for charge, chirality in items)
    nhat = sum(chirality * charge for charge, chirality in items)
    return a_grav, a_gauge, nhat


def is_anomaly_free(multiplet: Iterable[Species]) -> bool:
    a_grav, a_gauge, _ = coefficients(multiplet)
    return a_grav == 0 and a_gauge == 0


def construct_even_nhat(nhat: int) -> Multiplet:
    """Construct an anomaly-free multiplet with the requested even Nhat.

    For nhat = 2m, use two positive-chirality charges 5m,5m and two
    negative-chirality charges m,7m. The square sums match:
    50m^2 = m^2 + 49m^2, while the linear sums differ by 2m.
    Flipping all chiralities flips Nhat.
    """
    check(nhat % 2 == 0, "construction only claims even Nhat values")
    if nhat == 0:
        return ((1, +1), (1, -1))

    m = abs(nhat) // 2
    base: Multiplet = ((5 * m, +1), (5 * m, +1), (m, -1), (7 * m, -1))
    if nhat > 0:
        return base
    return tuple((charge, -chirality) for charge, chirality in base)


def exhaustive_anomaly_free_nhats(max_charge: int, max_size: int) -> set[int]:
    species = [
        (charge, chirality)
        for charge in range(-max_charge, max_charge + 1)
        if charge != 0
        for chirality in (+1, -1)
    ]
    seen: set[int] = set()
    for size in range(2, max_size + 1):
        for combo in itertools.combinations_with_replacement(species, size):
            if is_anomaly_free(combo):
                _, _, nhat = coefficients(combo)
                seen.add(nhat)
    return seen


def main() -> int:
    print("=" * 88)
    print("SM-boundary anomaly-inflow independent algebraic check")
    print("=" * 88)

    print("Part A -- parity identity")
    for charge in range(-40, 41):
        check((charge * charge - charge) % 2 == 0, "q^2 == q (mod 2)")
    print("  verified q^2 == q (mod 2) for integer charges in [-40,40]")

    print()
    print("Part B -- constructive even-count family")
    constructed: dict[int, Multiplet] = {}
    for nhat in range(-18, 20, 2):
        multiplet = construct_even_nhat(nhat)
        a_grav, a_gauge, actual = coefficients(multiplet)
        check(a_grav == 0, f"A_grav vanishes for constructed Nhat={nhat}")
        check(a_gauge == 0, f"A_gauge vanishes for constructed Nhat={nhat}")
        check(actual == nhat, f"constructed multiplet realizes Nhat={nhat}")
        constructed[nhat] = multiplet
    print("  constructed anomaly-free multiplets for every even Nhat in [-18,18]")
    print("  sample Nhat=+6 multiplet:", constructed[6])

    print()
    print("Part C -- bounded independent census")
    seen = exhaustive_anomaly_free_nhats(max_charge=5, max_size=6)
    odd_seen = sorted(value for value in seen if value % 2)
    nonzero_seen = sorted(value for value in seen if value)
    residues_mod_3 = sorted({value % 3 for value in seen})
    print("  anomaly-free Nhat values with |q|<=5 and <=6 Weyl species:")
    print(" ", sorted(seen))
    print("  nonzero values:", nonzero_seen)
    print("  odd values:", odd_seen)
    print("  residues modulo 3:", residues_mod_3)

    check(seen, "bounded anomaly-free census is non-empty")
    check({-4, -2, 0, 2, 4}.issubset(seen), "bounded census realizes small even values")
    check(not odd_seen, "bounded anomaly-free census has no odd Nhat")
    check(nonzero_seen, "local anomaly-freedom does not pin Nhat to zero")
    check(residues_mod_3 == [0, 1, 2], "local anomaly-freedom imposes no mod-3 selector")

    print()
    print("#" * 88)
    print("# VERDICT: independent PASS.")
    print("# Local anomaly cancellation gives a real 2-primary parity constraint on Nhat,")
    print("# but it neither pins the external count nor imposes a mod-3 selector.")
    print(f"# hard asserts passed: {NASSERT}")
    print("#" * 88)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
