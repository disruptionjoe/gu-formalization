#!/usr/bin/env python3
"""SG2 -- price the 3 | sigma external import: is the surviving count-import channel available?

Sequential-goals run 2026-07-09, goal 2.

CONTEXT
-------
The BIG-SWING-RS-INDEX synthesizer (2026-07-07) closes the GU-native construction branch of the
generation count and narrows the single surviving escape from `Hom(Z/3,Z)=0` to a DOUBLE EXTERNAL
IMPORT: a cubic `3 | m` Yukawa coupling AND a spacetime base signature `3 | sigma`, disjoint from
the located carrier `e_R = 1/12`. Next-step #2 of that synthesis asks explicitly: "A route that asks
whether any GU-admissible spacetime carries `3 | sigma` would test whether the import is even
available, not just conceivable."

This certificate PRICES the `3 | sigma` leg. It does not build the source action, does not force
three, and changes no verdict. It answers a bounded topological question with exact arithmetic:
under what conditions can a GU-admissible spacetime base `X^4` carry a signature divisible by 3, and
what does that cost?

WHAT IS COMPUTED (exact number theory + realizability; no target import)
-----------------------------------------------------------------------
1. LATTICE FACT. For a closed smooth SPIN 4-manifold, Rokhlin's theorem forces `16 | sigma`. Then
   `3 | sigma` (spin) <=> `sigma in 16Z cap 3Z = lcm(16,3) Z = 48 Z`. Proven here via gcd/lcm.
2. NON-SPIN realizability. Connected sums `a CP^2 # b (CP^2-bar)` realize EVERY integer signature
   `a - b` (odd intersection form, non-spin). So `3 | sigma` is realizable with `|sigma|` as small
   as 3 (e.g. `# 3 CP^2`). Cost: X^4 non-spin => (canon `w2-y14-spin-structure.md`) Y^14 is NON-spin,
   so the Dirac/RS operator needs a Spin^c or twisted setup -- a real structural cost, not a free win.
3. SPIN realizability. Even unimodular forms have signature in `16Z` (van der Blij / Rokhlin);
   `# k K3` realizes `sigma = -16k`, and `3 | sigma` first occurs at `k = 3` (`sigma = -48`),
   forcing `b2 >= 48` (a "large" spacetime). So on a spin base the import costs `|sigma| >= 48`.
4. DISJOINTNESS witness. The carrier defect `e_R = 1/12 in Q/Z` (order 12, 3-adic valuation 1) is a
   framed-bordism/eta datum on the RP^3 spine; `sigma in Z` is a bulk signature of X^4. The map
   between them (an APS defect) carries NO GU-forced relation: `3 | sigma` and the carrier class are
   independent inputs (fully separated in SG5). Here we only confirm they live in different homes.

VERDICT (this script + SG2 doc): the `3 | sigma` import is AVAILABLE, not obstructed -- so the
located-not-forced count CANNOT be upgraded to "provably not forceable" by killing this channel.
But it is a genuine EXTERNAL boundary datum with a priced cost: free-but-non-spin (Y^14 loses its
spin Dirac operator) OR spin-but-large (`|sigma| >= 48`). This SHARPENS "located, not forced": the
surviving escape is real and external, consistent with the firewall-boundary reading, and it is the
spacetime's signature -- not any GU-native carrier -- that would have to supply the factor 3.

Run from repo root:   python tests/big-swing/sg2_price_sigma_mod3_import.py   (exit 0)
"""
from __future__ import annotations

import sys
from math import gcd


def lcm(a, b):
    return a * b // gcd(a, b)


def realizable_nonspin_signatures(bound=6):
    """a CP^2 # b (CP^2-bar): signature = a - b, odd form (non-spin) for a+b>=1.

    Returns the set of signatures reachable with a+b <= bound, plus the minimal a+b realizing 3|sigma.
    """
    sigs = {}
    for a in range(bound + 1):
        for b in range(bound + 1):
            if a + b == 0:
                continue
            s = a - b
            cost = a + b  # b2 = a+b
            if s not in sigs or cost < sigs[s]:
                sigs[s] = cost
    return sigs


def realizable_spin_signatures(kmax=6):
    """# k K3: signature = -16 k (even unimodular; spin). Returns {sigma: b2-cost}."""
    sigs = {}
    for k in range(1, kmax + 1):
        s = -16 * k
        b2 = 22 * k  # b2(K3) = 22
        sigs[s] = b2
    sigs[0] = 0  # S^2 x S^2 stack / trivial
    return sigs


def main():
    print("=" * 78)
    print("SG2  pricing the 3 | sigma external import (is the surviving count channel available?)")
    print("=" * 78)

    ok = True

    # 1. Lattice fact: 16Z cap 3Z = 48Z
    L = lcm(16, 3)
    print("\n[1] Rokhlin lattice fact (spin base):")
    print(f"    spin  =>  16 | sigma  (Rokhlin, closed smooth spin 4-manifold).")
    print(f"    3 | sigma AND 16 | sigma  <=>  {L} | sigma   (lcm(16,3) = {L}).")
    ok &= (L == 48)
    # sanity: no s in (0,48) divisible by both 16 and 3
    both = [s for s in range(1, 96) if s % 16 == 0 and s % 3 == 0]
    print(f"    signatures in [1,96) divisible by both 16 and 3: {both}  (first = 48)")
    ok &= (both[0] == 48)

    # 2. Non-spin realizability
    print("\n[2] Non-spin realizability (a CP^2 # b CP^2-bar, signature = a-b, non-spin):")
    ns = realizable_nonspin_signatures(bound=6)
    div3_ns = sorted((s, c) for s, c in ns.items() if s != 0 and s % 3 == 0)
    smallest = min((abs(s), c, s) for s, c in ns.items() if s != 0 and s % 3 == 0)
    print(f"    3 | sigma reachable at signatures (sigma, b2-cost): {div3_ns[:6]} ...")
    print(f"    minimal |sigma|: |sigma| = {smallest[0]} at b2 = {smallest[1]}  (# 3 CP^2, sigma=+3).")
    print(f"    COST: X^4 non-spin => Y^14 non-spin (canon w2-y14-spin-structure.md) =>")
    print(f"          the GU Dirac/RS operator needs a Spin^c / twisted setup (structural cost).")
    ok &= (3 in ns and ns[3] == 3)

    # 3. Spin realizability
    print("\n[3] Spin realizability (# k K3, signature = -16k, even/spin):")
    sp = realizable_spin_signatures(kmax=6)
    div3_sp = sorted((s, c) for s, c in sp.items() if s != 0 and s % 3 == 0)
    print(f"    spin signatures divisible by 3 (sigma, b2-cost): {div3_sp[:4]} ...")
    first = min((abs(s), s, c) for s, c in sp.items() if s != 0 and s % 3 == 0)
    print(f"    first occurrence: sigma = {first[1]} at b2 = {first[2]}  (# 3 K3), |sigma| = {first[0]}.")
    print(f"    COST: a spin base carrying 3 | sigma needs |sigma| >= 48, hence b2 >= 48 (large X^4).")
    ok &= (-48 in sp and sp[-48] == 66)

    # 4. Disjointness home-check
    print("\n[4] Disjointness of the two homes (full independence proved in SG5):")
    eR_order = 12
    print(f"    carrier defect e_R = 1/12 in Q/Z: order {eR_order}, 3-adic valuation "
          f"{ _v3(eR_order) } (a framed-bordism/eta class on the RP^3 spine).")
    print(f"    sigma in Z: a bulk signature of X^4 (an integer intersection-form invariant).")
    print(f"    No GU-forced map ties them; 3 | sigma is an INDEPENDENT external boundary datum.")

    # Adjudication
    print("\n" + "-" * 78)
    print("ADJUDICATION")
    print("  The 3 | sigma import is AVAILABLE (not obstructed) on GU-admissible spacetimes:")
    print("    - non-spin base: 3 | sigma free (sigma=3), but Y^14 loses its spin Dirac operator;")
    print("    - spin base:     3 | sigma requires |sigma| >= 48 (# 3 K3), a large spacetime.")
    print("  => located-not-forced CANNOT be upgraded to 'provably not forceable' by killing this")
    print("     channel; the surviving escape is real. It is EXTERNAL (spacetime signature), priced,")
    print("     and disjoint from the located carrier -- consistent with the firewall-boundary reading.")
    print("  => No target imported: 3 enters only as the modulus under test; 48 = lcm(16,3) is derived.")
    print("=" * 78)
    if not ok:
        print("CONTRACT FAILED", file=sys.stderr)
        sys.exit(1)
    print("SG2 CONTRACT OK (exit 0): the 3|sigma import is priced-available; no verdict/canon/posture change.")


def _v3(n):
    v = 0
    while n % 3 == 0:
        n //= 3
        v += 1
    return v


if __name__ == "__main__":
    main()
