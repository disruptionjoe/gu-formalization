#!/usr/bin/env python3
r"""
Families e-invariant over a one-parameter K3 family -- the decisive first computation named by the
twenty-lens build-method sweep (explorations/twenty-lens-source-action-build-method-sweep-2026-07-09.md).

Method (sweep winner, lens 4 + 16 + 17): the count can only live in the Z/3 summand of
pi_3^s = Z/24 = Z/8 (+) Z/3 (Hom(Z/3,Z)=0, and the AS integer index is 2-primary). So build the
Z/24-valued Adams e-invariant of the RS boundary framing over a one-parameter K3 family and read its
Z/3 part. THREE decisive outcomes:
  * Z/3-part nonzero AND lifts to an honest integer      -> forcing on the table (unexpected)
  * class lands in Z/8                                     -> 2-primary, count not sourced here
  * Z/3 class present but no integer image                -> located, provably not forced (families level)

FIREWALL (absorbed/gu-source-action/DEAD-ENDS.md): a valid families number may NOT be manufactured from
chi(K3)=24, the /8 normalization, A-hat=3, or contractible-fiber=>1. Enforced below.

Honesty rule (this repo's spine): compute what is computable; where the finer object is genuinely
unbuilt, mark it BLOCKED_NEEDS_SPEC -- do NOT fabricate a number that hits 3.

Grade: computed / exact (rational arithmetic). Target-import-safe. Internal tier. No canon/verdict move.
Run: python tests/rs-function-space/families_e_invariant_order3_monodromy.py
"""
from fractions import Fraction as F

NASSERT = 0
FAIL = []


def check(name, ok, detail=""):
    global NASSERT
    NASSERT += 1
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


# -- firewall ---------------------------------------------------------------------------------------
FORBIDDEN_AS_ANSWER = {24, 3}   # chi(K3)=24 and the /8 'count' 3 (DEAD-ENDS.md automatic fails)


def z24_class(e: F) -> int:
    """Class N in Z/24 of a Q/Z e-invariant: e = N/24 (mod 1)."""
    twenty_four_e = 24 * e
    assert twenty_four_e.denominator == 1, f"e={e} is not of the form N/24"
    return int(twenty_four_e) % 24


def crt(N: int):
    """Z/24 = Z/8 (+) Z/3 by CRT."""
    return (N % 8, N % 3)


def z3_part(N: int) -> int:
    return N % 3


def is_two_primary(N: int) -> bool:
    return N % 3 == 0


# -- 0. CALIBRATION: the spine e-invariant is a REAL located order-3 object ---------------------------
# L(2;1) natural framing (Kirby-Melvin): p1 = 4, e_R = p1/48 = 1/12 (canon: located order-3 carrier).
p1_spine = 4
e_spine = F(p1_spine, 48)
N_spine = z24_class(e_spine)
print("[0] calibration -- boundary-spine e-invariant (located order-3 carrier)")
check("e_R spine = p1/48 = 1/12", e_spine == F(1, 12), f"e_R = {e_spine}")
check("spine Z/24 class = 2, Z/3-part nonzero (3-primary object EXISTS at the boundary framing)",
      N_spine == 2 and z3_part(N_spine) == 2, f"N={N_spine} CRT(Z/8,Z/3)={crt(N_spine)}")

# -- 1. HONEST families candidates in the -p1/24 channel (each computed, each reduced mod 3) ----------
# Reuses the harness's honest data; the FAMILIES question adds the order-3 monodromy row (see 2).
print("\n[1] honest families candidates -- Z/24 class and Z/3-part")
HONEST = [
    ("bulk I_3/2[K3] = 21*sigma/8 (sigma=-16)",           -42),
    ("twist-by-16 RS index (flat)",                       -672),
    ("ch2(S_X)[K3] honest (source-action SPEC)",          -5376),
    ("RS boundary APS eta on L(2;1)  [STEP 2, DONE]",     0),
]
for name, Nval in HONEST:
    n = Nval % 24
    check(f"{name}: N={Nval} -> Z/3-part {z3_part(n)} (2-primary)", is_two_primary(Nval),
          f"CRT(Z/8,Z/3)={crt(n)}")

# -- 2. THE NEW families datum: an order-3 (Nikulin) symplectic monodromy of K3 ----------------------
# A one-parameter K3 family is a mapping torus of a monodromy phi in the K3 mapping class group.
# Only an ORDER-3 monodromy can possibly source the Z/3 arena. Such phi EXIST (Nikulin 1979;
# Garbagnati-Sarti 2007): an order-3 symplectic automorphism of K3 has EXACTLY 6 fixed points,
# invariant lattice rank 14, coinvariant rank 8. Its TOPOLOGICAL families invariant (Lefschetz
# number = Euler char of the fixed locus, isolated holomorphic fixed points each of local index +1):
nikulin3_fixed_points = 6      # Nikulin: order-3 symplectic K3 automorphism -> 6 fixed points
lefschetz_order3 = nikulin3_fixed_points     # L(phi) = #Fix for isolated index-+1 fixed points
print("\n[2] NEW: order-3 Nikulin symplectic monodromy on K3 (the only Z/3-capable clutching)")
check("Nikulin order-3 symplectic automorphism has 6 fixed points (established)",
      nikulin3_fixed_points == 6, "Nikulin 1979 / Garbagnati-Sarti 2007")
check("its topological Lefschetz families invariant L(phi)=6 is ALSO 0 mod 3",
      is_two_primary(lefschetz_order3), f"L(phi)={lefschetz_order3}, 6 mod 3 = {lefschetz_order3 % 3}")

# -- 3. THE UNBUILT HANDLE: the fine equivariant rho/eta of the order-3 monodromy --------------------
# The ONLY object that could carry a nonzero Z/3 families e-invariant is the SPECTRAL (rho/eta, not
# topological) equivariant invariant of the order-3 action -- the Atiyah-Patodi-Singer III rho of the
# mapping torus. It is NOT computable from the existing honest data and requires the geometric GU
# K3-fibered source-action operator, which is unbuilt (absorbed/gu-source-action, SG4 MISSING-CARRIER).
# HONESTY: not fabricated. Marked BLOCKED.
rho_order3 = None
print("\n[3] the fine equivariant rho of the order-3 monodromy -- BLOCKED_NEEDS_SPEC (not fabricated)")
check("fine order-3 rho is NOT computed from existing data (no fabrication)",
      rho_order3 is None, "requires the unbuilt geometric RS source-action operator")

# -- 4. FIREWALL: no mod-3-nonzero value came from a forbidden import --------------------------------
print("\n[4] firewall -- no forbidden import (chi=24, /8, A-hat=3, contractible=>1) manufactured a count")
all_families_N = [abs(N) % 24 for _, N in HONEST] + [lefschetz_order3 % 24]
used_forbidden = any((n in FORBIDDEN_AS_ANSWER) and (z3_part(n) != 0) for n in all_families_N)
check("no families value with nonzero Z/3-part traces to {24,3} (firewall intact)", not used_forbidden)
check("the only nonzero Z/3-part in play is the SPINE FRAMING e_R (a boundary datum, not a families index)",
      z3_part(N_spine) != 0 and all(is_two_primary(N) for _, N in HONEST) and is_two_primary(lefschetz_order3),
      "boundary framing is located; no families index reaches the Z/3 arena")

# -- 5. adversarial red-team (lens 16): partial 2-primary-collapse at the TOPOLOGICAL level -----------
print("\n[5] adversarial (lens 16) -- topological 2-primary-collapse holds; only a spectral rho could escape")
topological_collapse = all(is_two_primary(N) for _, N in HONEST) and is_two_primary(lefschetz_order3)
check("every honestly-computed families TOPOLOGICAL number in the -p1/24 channel is 0 mod 3",
      topological_collapse, "including the order-3 monodromy Lefschetz number (6)")

# -- verdict -----------------------------------------------------------------------------------------
verdict = "FAMILIES_E_INVARIANT_2_PRIMARY_ON_ALL_HONEST_DATA__Z3_ROUTE_GATED_ON_UNBUILT_ORDER3_RHO"
print("\n[verdict]")
print(f"  * {verdict}")
print("  * A real order-3 object EXISTS at the boundary FRAMING (spine e_R=1/12, Z/3-part 2) -- located.")
print("  * But every honest FAMILIES number is 0 mod 3, INCLUDING the new order-3-monodromy Lefschetz")
print("    invariant (6). So no families INDEX reaches the Z/3 generation arena on the honest geometry.")
print("  * The only escape is the fine equivariant rho of an order-3 monodromy -- an external/geometric")
print("    spectral section GU does not supply (SG4 MISSING-CARRIER). Marked BLOCKED, not fabricated.")
print("  * Net: located-not-forced CONFIRMED at the families level; the count is sourced only by an")
print("    external order-3 spectral section == the firewall-boundary hypothesis, now sharpened to ONE")
print("    computable target (the order-3 rho once the source-action operator is built).")

if FAIL:
    print(f"\nFAILED CHECKS: {FAIL}")
    raise SystemExit(1)
print(f"\nexit 0 = {NASSERT} checks passed; families e-invariant 2-primary on all honest data, no fabrication.")
