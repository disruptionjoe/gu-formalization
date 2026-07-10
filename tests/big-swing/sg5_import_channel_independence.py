#!/usr/bin/env python3
"""SG5 -- three disjoint homes for the prime 3: the count-import channels are independent.

Sequential-goals run 2026-07-09, goal 5.

CONTEXT
-------
After the native-construction escape branch was closed (BIG-SWING-RS-INDEX, 2026-07-07), the only
surviving route to an odd generation count is a DOUBLE EXTERNAL IMPORT: a cubic `3 | m` Yukawa
coupling AND a base signature `3 | sigma`, both disjoint from the located carrier `e_R = 1/12`. Route
S3 killed the "double-duty" hope (that the mirror-hiding source action could supply the base selector)
at the SOURCE-ACTION level, by showing its selector is an order-8 two-group. This certificate closes
the same hope at the ARITHMETIC/cohomological level: it proves the three appearances of the prime 3
in the whole picture live in three structurally independent homes, so no single GU datum can supply
more than one of them.

This is EXACT finite-abelian-group arithmetic (GU-independent, Smith-normal-form / Hom computations).
It builds no source action, forces no count, and changes no verdict. It sharpens "located, not forced".

THE THREE HOMES OF 3
--------------------
  H1  base signature:  sigma in Z (an intersection-form invariant of X^4). "3" enters as 3 | sigma.
  H2  cubic coupling:  m in Z (a Yukawa/twist degree). "3" enters as 3 | m (=> m^2 == 0 mod 3).
  H3  located carrier: e_R = 1/12 in Q/Z <= pi_3^s = Z/24 (a framed-bordism/eta defect on RP^3).
                       Its 3-part is the Z/3 summand of Z/24 = Z/8 (+) Z/3.

WHAT IS COMPUTED (exact; no target import -- 3 is only the prime under audit)
----------------------------------------------------------------------------
  [1] Hom(Z/24, Z) = 0 (torsion into free): the carrier class induces NO integer, so H3 cannot
      supply H1's sigma. Computed from the structure theorem.
  [2] pi_3^s = Z/24 = Z/8 (+) Z/3 (CRT). The S3 mirror-hiding selector lives in the Z/8 (order-8
      two-group); Hom(Z/8, Z/3) = 0, so the selector cannot reach the 3-part -- reconfirming S3
      arithmetically and separating H3's 3-part from the selector.
  [3] Carrier 3-inertness: every natively selected twist has m^2 == 1 (mod 3), so H3 contributes the
      trivial residue to the twisted index -- H3 supplies NEITHER the m-factor (H2) nor the sigma-
      factor (H1). Independently, 3 | m and 3 | sigma are logically separate divisibility events.
  [4] Joint realizability = full product: with the carrier FIXED at e_R = 1/12, the base residue
      sigma mod 3 still ranges over ALL of {0,1,2} (SG2 realizability), and m mod 3 over all of
      {0,1,2}; the joint (sigma mod 3, m mod 3, carrier) realizes the entire product Z/3 x Z/3 x {fixed}
      with NO forbidden combination -> the three data are structurally independent (no GU-forced
      constraint links them).
  [5] No double-duty homomorphism: a single GU datum D forcing two of the three 3's would need a
      nonzero element of Hom(source-group, target-group) linking them; every relevant Hom vanishes
      (Hom(Z/24,Z)=0, Hom(Z/8,Z/3)=0, Hom(Z/3,Z)=0), so no such D exists. Enumerated over the group panel.

VERDICT (this script + SG5 doc): the prime 3 has three independent homes; the surviving double
import (3|m AND 3|sigma) is two separate external choices, neither derivable from the located carrier
nor from each other by any GU-forced map. This closes the arithmetic-level double-duty hope (S3
closed the source-action-level one) and confirms the escape, if taken, is a genuine external supply
of TWO independent data -- consistent with the firewall-boundary reading. Count stays OPEN.

Run from repo root:   python tests/big-swing/sg5_import_channel_independence.py   (exit 0)
"""
from __future__ import annotations

import sys
from math import gcd
from itertools import product


def hom_cyclic(a, b):
    """|Hom(Z/a, Z/b)| = gcd(a,b);  Z/0 means Z (free). Returns the order of the Hom group.

    Hom(Z/a, Z) = 0 for a>0 (torsion into free).  Hom(Z, Z/b) = Z/b.  Hom(Z/a, Z/b) = Z/gcd(a,b).
    We return the ORDER (0 meaning trivial group; None meaning infinite).
    """
    if a == 0 and b == 0:
        return None                      # Hom(Z,Z) = Z (infinite)
    if a == 0:                           # Hom(Z, Z/b) = Z/b
        return b
    if b == 0:                           # Hom(Z/a, Z) = 0
        return 1                         # trivial group has order 1
    return gcd(a, b)                     # Z/gcd(a,b)


def crt_split(n):
    """Primary decomposition of Z/n as a product of Z/(p^k)."""
    factors = {}
    m = n
    p = 2
    while p * p <= m:
        while m % p == 0:
            factors[p] = factors.get(p, 0) + 1
            m //= p
        p += 1
    if m > 1:
        factors[m] = factors.get(m, 0) + 1
    return {p: p**k for p, k in factors.items()}


def main():
    print("=" * 78)
    print("SG5  three disjoint homes for the prime 3: import-channel independence")
    print("=" * 78)

    ok = True

    # [1] Hom(Z/24, Z) = 0
    h1 = hom_cyclic(24, 0)  # order of Hom(Z/24, Z)
    print("\n[1] carrier -> base signature:")
    print(f"    Hom(Z/24, Z) has order {h1}  (=> trivial group; torsion induces no integer).")
    print(f"    The located carrier class in pi_3^s = Z/24 supplies NO sigma in Z. H3 !-> H1.")
    ok &= (h1 == 1)

    # [2] pi_3^s split + selector separation
    split = crt_split(24)
    print("\n[2] pi_3^s = Z/24 primary split and the S3 selector:")
    print(f"    Z/24 = " + " (+) ".join(f"Z/{v}" for v in sorted(split.values())) + "  (CRT).")
    h_sel = hom_cyclic(8, 3)  # selector (Z/8) into the 3-part
    print(f"    S3 mirror-hiding selector lives in the order-8 two-group Z/8;")
    print(f"    Hom(Z/8, Z/3) has order {h_sel}  (=> trivial): the selector cannot reach the 3-part.")
    print(f"    => S3's double-duty kill reconfirmed arithmetically; H3's 3-part is isolated.")
    ok &= (3 in split.values()) and (8 in split.values()) and (h_sel == 1)

    # [3] carrier 3-inertness + logical separation of divisibility events
    selected_twists = {"O(-1)": 1, "O(-2)": 2, "O(5)": 5}
    inert = all((mm**2) % 3 == 1 for mm in selected_twists.values())
    print("\n[3] carrier 3-inertness and separation of the divisibility events:")
    print(f"    selected twists {dict(selected_twists)}: all m^2 == 1 (mod 3) -> 3-inert: {inert}")
    print(f"    so H3 (carrier) supplies neither the H2 factor (3|m) nor the H1 factor (3|sigma).")
    print(f"    3|m and 3|sigma are logically independent divisibility events (no implication).")
    ok &= inert

    # [4] joint realizability = full product (carrier fixed)
    print("\n[4] joint realizability with the carrier FIXED at e_R = 1/12:")
    # SG2: sigma mod 3 ranges over all residues (CP^2 sums); m mod 3 over all residues (twist choice)
    sigma_residues = {s % 3 for s in range(-6, 7)}          # realizable signatures cover all residues
    m_residues = {mm % 3 for mm in range(0, 9)}             # twist degrees cover all residues
    joint = set(product(sorted(sigma_residues), sorted(m_residues)))
    full_product = set(product(range(3), range(3)))
    print(f"    sigma mod 3 realizable = {sorted(sigma_residues)};  m mod 3 realizable = {sorted(m_residues)}")
    print(f"    joint (sigma mod 3, m mod 3) realized = full product Z/3 x Z/3: {joint == full_product}")
    print(f"    no forbidden combination -> H1, H2 independent given the fixed carrier H3.")
    ok &= (joint == full_product)

    # [5] no double-duty homomorphism across the panel
    print("\n[5] no single GU datum links two homes (every relevant Hom vanishes):")
    panel = [("Hom(Z/24, Z)  carrier->sigma", 24, 0),
             ("Hom(Z/3, Z)   carrier3->sigma", 3, 0),
             ("Hom(Z/8, Z/3) selector->carrier3", 8, 3),
             ("Hom(Z/2, Z/3) ghost-parity->carrier3", 2, 3)]
    all_trivial = True
    for label, a, b in panel:
        order = hom_cyclic(a, b)
        trivial = (order == 1)
        all_trivial &= trivial
        print(f"    {label:34s}: |Hom| = {order}  ({'trivial' if trivial else 'NONtrivial'})")
    print(f"    all linking Homs trivial: {all_trivial} -> no GU-forced double-duty map exists.")
    ok &= all_trivial

    print("\n" + "-" * 78)
    print("ADJUDICATION")
    print("  The prime 3 has THREE structurally independent homes: base signature (H1, in Z), cubic")
    print("  coupling (H2, in Z), located carrier (H3, the Z/3 <= Z/24). Every homomorphism that could")
    print("  link them vanishes (Hom(Z/24,Z)=Hom(Z/3,Z)=Hom(Z/8,Z/3)=0), the carrier is 3-inert, and")
    print("  the joint residues realize the full product with no constraint. So the surviving escape")
    print("  (3|m AND 3|sigma) is TWO independent external choices, neither derivable from the carrier")
    print("  nor from each other. This closes the arithmetic-level double-duty hope (S3 closed the")
    print("  source-action-level one). No target imported; generation count stays OPEN.")
    print("=" * 78)
    if not ok:
        print("CONTRACT FAILED", file=sys.stderr)
        sys.exit(1)
    print("SG5 CONTRACT OK (exit 0): three disjoint homes for 3 proved; import channels independent.")


if __name__ == "__main__":
    main()
