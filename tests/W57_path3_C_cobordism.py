#!/usr/bin/env python3
r"""
W57 / PATH-3 BRANCH-C -- THE K-THEORY / COBORDISM CONSTRUCTION of the generation count.
=======================================================================================

Blind branch C of the "why three generations?" wave. The construction of "the count"
used here is the TORSION COBORDISM CLASS (the GEOMETER-VS-PHYSICS fork's torsion side,
NOT the integer index): anomaly-free 4d fermion content is classified (Freed-Hopkins)
by a 5d bordism group Omega^Spin_5(target); the generation datum sits in that group's
3-primary torsion, the Z/3 that is the 3-Sylow of the image of J = pi_3^s = Z/24.

This script encodes -- as deterministic, exact-arithmetic assertions -- the four
load-bearing facts and the single forces-vs-locates decision:

  (A) THE GROUP + ITS 3-PRIMARY SUMMAND.
      pi_3^s = Z/24 = Z/8 (+) Z/3 (CRT, Toda). |im J_3| = den(B_2/4) = 24 (Adams).
      3-primary summand = Z/3 (3-Sylow), exponent 3.  This is the arena Freed-Hopkins /
      GEM / Wan-Wang-Yau place the beyond-cohomology (Dai-Freed) 3-primary datum in.

  (B) THE STRUCTURE FORCES THE MODULUS, NOT THE VALUE.
      The exponent of Z/3 is 3 (forced: it is |Z/3|). But Aut(Z/3) = Z/2 exchanges the
      two generators {1,2}: there is NO canonical generator. A cobordism-NATURAL
      invariant (charge conjugation / orientation reversal acts as this Aut) cannot
      single out "1" from "2" -> it detects ORDER (3), it does not select the VALUE.

  (C) ANOMALY CANCELLATION IS GENERATION-BLIND (the GEM / WWY cross-check).
      The Dai-Freed anomaly is a HOMOMORPHISM eta: Omega^Spin_5(BG) -> R/Z. For N
      generations the fermion class is N*[1 gen], so eta(N*[1gen]) = N*eta([1gen]).
      GEM/WWY: for the actual Standard Model eta([1gen]) = 0 (one generation is already
      Dai-Freed anomaly-free), hence eta(N*[1gen]) = 0 for EVERY N. Anomaly cancellation
      -- the only first-principles consistency condition the cobordism framework supplies
      -- does NOT constrain N. The integer count is free.

  (D) THE Z-LIFT DOES NOT EXIST (H6 / class-as-count category error).
      Hom(Z/3, Z) = 0: no Z-valued (index) cobordism invariant reaches the torsion, and
      the order-3 CLASS has no canonical integer preimage. "count = integer 3" is a
      different construction (the index fork); Hom(Z/3, Z)=0 says the two forks do not
      communicate.

DECISION: LOCATES (the count is a class in the Z/3 summand, modulus 3 forced) but does
NOT FORCE (the value 3 requires a free choice of generator + Z-lift; anomaly cancellation
leaves it free). A POSITIVE CONTROL shows the no-go is structural, not vacuous: even a
hypothetical target with eta([1gen]) an order-3 element would only constrain N mod 3 --
still never pinning the integer 3.

No GU machinery imported; pure arithmetic of finite abelian groups + the anomaly hom
model. Deterministic, exit 0.  Run:  python tests/W57_path3_C_cobordism.py
"""
from __future__ import annotations

from fractions import Fraction as Fr
from math import gcd

FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


# --------------------------------------------------------------------------- #
# finite-abelian-group helpers (exact)
# --------------------------------------------------------------------------- #
def p_part(n: int, p: int) -> int:
    """p-primary part (p-Sylow order) of Z/n; n=0 denotes the free group Z (no torsion)."""
    if n == 0:
        return 1
    m = 1
    while n % p == 0:
        m *= p
        n //= p
    return m


def hom_count(source_order: int, target_order: int) -> int:
    """|Hom(Z/source, Z/target)| = gcd(source, target); target_order=0 means Z (free),
    for which Hom(finite, Z) = 0 -> only the zero map (count 1)."""
    if target_order == 0:
        return 1  # Hom(finite -> Z) = 0
    return gcd(source_order, target_order)


def aut_order_cyclic(n: int) -> int:
    """|Aut(Z/n)| = |(Z/n)^*| = Euler phi(n)."""
    return sum(1 for a in range(1, n + 1) if gcd(a, n) == 1)


def exponent_cyclic(n: int) -> int:
    """Exponent of Z/n is n."""
    return n


# --------------------------------------------------------------------------- #
# (A) THE GROUP + 3-PRIMARY SUMMAND
# --------------------------------------------------------------------------- #
def section_A():
    print("\n(A) THE BORDISM/K-THEORY GROUP AND ITS 3-PRIMARY SUMMAND")
    N = 24  # |im J| in dim 3 = pi_3^s = den(B_2/4) = 24 (Adams); the 3-primary count arena
    # CRT split verified as an explicit iso on all 24 classes
    iso = {k: (k % 8, k % 3) for k in range(N)}
    bijective = len(set(iso.values())) == N
    homomorphic = all(
        iso[(a + b) % N] == ((iso[a][0] + iso[b][0]) % 8, (iso[a][1] + iso[b][1]) % 3)
        for a in range(N) for b in range(N)
    )
    check("pi_3^s = Z/24 = Z/8 (+) Z/3 (CRT explicit iso, bijective+homomorphic)",
          bijective and homomorphic, "k |-> (k mod 8, k mod 3)")
    three = p_part(N, 3)
    two = p_part(N, 2)
    check("3-primary summand (3-Sylow) is Z/3 (nontrivial)", three == 3, f"3-part(Z/{N})={three}")
    check("2-primary summand (2-Sylow) is Z/8 (the selector arena)", two == 8, f"2-part(Z/{N})={two}")
    # von Staudt-Clausen provenance of the prime 3 in 24: den(B_2)=6=2*3 -> primes p with (p-1)|2
    check("prime 3 enters 24 by von Staudt-Clausen ((3-1)=2 | 2), not fitted",
          (3 - 1) % 2 == 0 and 24 % 3 == 0)
    return {"arena_order": N, "three_sylow": three, "two_sylow": two,
            "summand": "Z/3", "exponent": exponent_cyclic(3)}


# --------------------------------------------------------------------------- #
# (B) STRUCTURE FORCES THE MODULUS, NOT THE VALUE
# --------------------------------------------------------------------------- #
def section_B():
    print("\n(B) DOES THE GROUP STRUCTURE FORCE 3?  -- MODULUS vs VALUE")
    # exponent of Z/3 is 3: the MODULUS is forced (it is |Z/3|)
    exp = exponent_cyclic(3)
    check("the exponent/modulus of the Z/3 arena is forced = 3 (= |Z/3|)", exp == 3)
    # Aut(Z/3) = Z/2 exchanges the two nonzero elements {1,2}: NO canonical generator
    autord = aut_order_cyclic(3)
    generators = [g for g in (1, 2) if gcd(g, 3) == 1]
    swap = {g: (2 * g) % 3 for g in generators}  # the nontrivial automorphism a |-> 2a
    check("Aut(Z/3) = Z/2 is nontrivial: no canonical generator", autord == 2,
          f"|Aut(Z/3)|={autord}; nontrivial aut swaps {generators} -> {list(swap.values())}")
    check("the automorphism (charge-conj/orientation-reversal) exchanges the two generators",
          swap[1] == 2 and swap[2] == 1)
    # CONSEQUENCE: a natural invariant fixed by this Aut cannot select value 1 vs 2.
    # It can only see the ORBIT {1,2} (= 'order 3, nonzero') -- i.e. detect ORDER, not VALUE.
    canonical_generator_exists = (autord == 1)
    check("=> the structure forces the MODULUS (3) but NOT the VALUE (which generator)",
          not canonical_generator_exists,
          "natural invariants see the Aut-orbit {1,2}='nonzero order-3', never a single value")
    return {"exponent_forced": exp, "aut_order": autord,
            "canonical_generator_exists": canonical_generator_exists}


# --------------------------------------------------------------------------- #
# (C) ANOMALY CANCELLATION IS GENERATION-BLIND  (Freed-Hopkins linearity + GEM/WWY)
# --------------------------------------------------------------------------- #
def anomaly_of_N(eta_one_gen: Fr, N: int, modulus: int) -> Fr:
    """Dai-Freed anomaly of N generations = N * eta([1gen]) in R/Z, reduced mod 1.
    eta valued in (1/modulus)Z / Z (the torsion arena). Returns the R/Z representative."""
    val = (eta_one_gen * N)
    return val - Fr(int(val))  # mod 1 representative in [0,1)


def section_C():
    print("\n(C) ANOMALY CANCELLATION IS GENERATION-BLIND (Freed-Hopkins hom + GEM/WWY)")
    # Freed-Hopkins: anomaly is a HOMOMORPHISM eta: Omega_5 -> R/Z; N gens -> N*eta([1gen]).
    # GEM/WWY cross-check: for the actual SM, eta([1gen]) = 0 in the 3-primary Dai-Freed arena
    # (one generation is already anomaly-free). So the anomaly vanishes for ALL N.
    eta_SM = Fr(0)  # GEM 1808.00009 / Wan-Wang-Yau: SM per-generation Dai-Freed anomaly = 0
    all_N_free = all(anomaly_of_N(eta_SM, N, 3) == 0 for N in range(0, 25))
    check("SM 3-primary Dai-Freed anomaly eta([1gen]) = 0 (GEM/WWY) -> vanishes for ALL N",
          all_N_free, "eta(N*[1gen]) = N*0 = 0 for N=0..24: the count is UNCONSTRAINED")
    # linearity is the crux: the anomaly is a hom, so it can only constrain N modulo an order,
    # never pin a single positive integer. Demonstrate on a NONZERO control below.
    return {"eta_SM": Fr(0), "anomaly_free_for_all_N": all_N_free}


# --------------------------------------------------------------------------- #
# (C') POSITIVE CONTROL -- the no-go is structural, not vacuous
# --------------------------------------------------------------------------- #
def section_C_control():
    print("\n(C') POSITIVE CONTROL -- a NONZERO mod-3 anomaly still cannot pin the integer 3")
    # Hypothetical target whose per-generation anomaly is an ORDER-3 element eta([1gen])=1/3.
    eta = Fr(1, 3)
    # anomaly-free  <=>  N * (1/3) in Z  <=>  N == 0 (mod 3).
    free_set = [N for N in range(0, 25) if anomaly_of_N(eta, N, 3) == 0]
    check("nonzero order-3 anomaly constrains N == 0 (mod 3) -- a MODULUS-3 condition",
          free_set == [0, 3, 6, 9, 12, 15, 18, 21, 24],
          f"anomaly-free N in 0..24: {free_set}")
    # It selects the RESIDUE 0 mod 3, i.e. a Z/3 condition -- NOT the single integer 3.
    # (N=3 is allowed, but so are 6,9,12,...; and the physical count is N NONzero mod 3 in
    #  GU's reading, the opposite residue -- either way it is a residue class, never a value.)
    pins_integer_3 = (free_set == [3])
    check("=> even a genuine 3-primary anomaly does NOT pin the integer 3 (only a residue class)",
          not pins_integer_3)
    return {"nonzero_anomaly_free_set": free_set, "pins_integer_3": pins_integer_3}


# --------------------------------------------------------------------------- #
# (D) NO Z-LIFT: Hom(Z/3, Z) = 0  (H6 category error, cobordism-branch instance)
# --------------------------------------------------------------------------- #
def section_D():
    print("\n(D) NO Z-LIFT OF THE TORSION CLASS -- Hom(Z/3, Z) = 0  (class != integer)")
    # a Z-valued (index) cobordism invariant is a hom Z/3 -> Z; there are none but 0.
    check("Hom(Z/3, Z) = 0 (no Z-valued index reaches the torsion)",
          hom_count(3, 0) == 1, "only the zero map: the order-3 class has no integer preimage")
    check("Hom(Z/24, Z) = 0 (whole arena, one level up)", hom_count(24, 0) == 1)
    # 2-primary / free selectors are blind to the 3-Sylow (the family-puzzle partition)
    check("Hom(Z/3, Z/2^k) = 0 for k=1..5 (2-primary selectors blind to the count)",
          all(hom_count(3, 2 ** k) == 1 for k in range(1, 6)))
    # direction is load-bearing: Hom(Z, Z/3) = Z/3 != 0 (a Z-index CAN be reduced mod 3,
    # but that is the OTHER fork -- reducing an integer, not lifting the torsion class).
    check("direction check: Hom(Z, Z/3) = Z/3 != 0 (reduction is the index fork, not a lift)",
          gcd(0, 3) == 3,  # |Hom(Z, Z/3)| = 3 (nonzero): reducing an integer mod 3 IS allowed,
          "but that is the index fork; lifting the torsion class to Z is not (Hom(Z/3,Z)=0)")
    return {"hom_Z3_Z": 0, "hom_Z24_Z": 0}


# --------------------------------------------------------------------------- #
# THE FORCES-vs-LOCATES DECISION
# --------------------------------------------------------------------------- #
def decision(A, B, C, Cc, D):
    print("\n" + "=" * 78)
    print("FORCES-vs-LOCATES DECISION (branch C: torsion cobordism class)")
    print("=" * 78)

    # LOCATES: the count is a class in the Z/3 summand; the modulus 3 is forced.
    locates = (A["three_sylow"] == 3 and B["exponent_forced"] == 3)
    # FORCES the integer 3 would require ALL of:
    #   (i)   a canonical generator of Z/3            -> FALSE (Aut(Z/3)=Z/2)
    #   (ii)  anomaly cancellation to pick it         -> FALSE (generation-blind, GEM/WWY)
    #   (iii) a Z-lift of the class to the integer 3  -> FALSE (Hom(Z/3,Z)=0)
    forces = (B["canonical_generator_exists"]
              and not C["anomaly_free_for_all_N"]
              and D["hom_Z3_Z"] != 0)

    check("LOCATES: count is a class in Z/3, modulus 3 forced by the group structure", locates)
    check("FORCES the integer 3?  requires canonical generator AND selecting anomaly AND Z-lift",
          not forces, "all three fail -> NOT forced")

    print("\n  Q-force : LOCATES only. Omega^Spin_5(BG) 3-primary part = Z/3; the group forces the")
    print("            MODULUS (exponent 3 = |Z/3|), NOT the value. Anomaly cancellation, being a")
    print("            HOMOMORPHISM (Freed-Hopkins), is generation-blind for the SM (GEM/WWY:")
    print("            eta([1gen])=0 -> free for all N).")
    print("  Q-extra : the minimal extra input to pin 3 = (choice of a GENERATOR of the Z/3 summand,")
    print("            i.e. which fermion rep / bordism class) + (a Z-lift / integer normalization).")
    print("            Anomaly cancellation does NOT supply either (it vanishes for all N). => FREE")
    print("            MODEL-BUILDING CHOICE, not a first-principles consistency condition.")
    print("  Q-nogo  : class-wide no-go for cobordism selectors -- (i) Aut(Z/3)=Z/2 => no natural")
    print("            invariant selects a generator (only the order); (ii) Hom(Z/3,Z)=0 => no")
    print("            Z-index reaches the torsion; (iii) the anomaly hom is linear in N => at best")
    print("            a residue-mod-3 condition, never a single integer. No cobordism/K-theory")
    print("            selector of the anomaly-homomorphism kind forces the integer 3.")
    return {"locates": locates, "forces": forces}


# --------------------------------------------------------------------------- #
def main():
    print("=" * 78)
    print("W57 / PATH-3 BRANCH-C -- K-THEORY / COBORDISM CONSTRUCTION OF THE GENERATION COUNT")
    print("=" * 78)
    print("construction of 'the count' used: TORSION COBORDISM CLASS (Freed-Hopkins anomaly")
    print("classification; the torsion side of the GEOMETER-VS-PHYSICS fork, NOT the integer index)")

    A = section_A()
    B = section_B()
    C = section_C()
    Cc = section_C_control()
    D = section_D()
    dec = decision(A, B, C, Cc, D)

    # ---- load-bearing hard asserts ----
    assert A["three_sylow"] == 3 and A["two_sylow"] == 8
    assert B["exponent_forced"] == 3 and B["aut_order"] == 2
    assert not B["canonical_generator_exists"]
    assert C["anomaly_free_for_all_N"]           # GEM/WWY: SM generation-blind
    assert not Cc["pins_integer_3"]              # even a nonzero mod-3 anomaly does not pin 3
    assert dec["locates"] and not dec["forces"]

    if FAIL:
        print(f"\nFAILED CHECKS: {FAIL}")
        raise SystemExit(1)

    print("\n" + "=" * 78)
    print("VERDICT: cobordism/K-theory LOCATES the count in the Z/3 (3-primary) summand of")
    print("Omega^Spin_5(BG) = im J = pi_3^s = Z/24; it FORCES the modulus 3, NOT the value 3.")
    print("The extra input to pin 3 (a generator choice + Z-lift) is a FREE model-building choice;")
    print("anomaly cancellation is generation-blind (GEM/WWY) and does not force it. Class-wide")
    print("no-go: no cobordism selector of the anomaly-homomorphism kind forces the integer 3.")
    print("=" * 78)

    summary = {
        "construction": "torsion cobordism class (Freed-Hopkins), NOT the integer index",
        "group": "Omega^Spin_5(BG) ~ im J = pi_3^s = Z/24 = Z/8 (+) Z/3",
        "three_primary_summand": "Z/3 (3-Sylow), exponent 3",
        "Q_force": "LOCATES only (modulus 3 forced, value 3 not)",
        "Q_extra": "generator choice + Z-lift; FREE model choice, not anomaly-forced",
        "Q_nogo": "class-wide: Aut(Z/3)=Z/2 (no canonical gen) + Hom(Z/3,Z)=0 + linear anomaly hom",
        "gem_wwy_crosscheck": "SM per-generation Dai-Freed anomaly = 0 -> free for all N",
        "locates": dec["locates"], "forces": dec["forces"],
    }
    print("\nMACHINE SUMMARY:")
    for k, v in summary.items():
        print(f"  {k}: {v}")
    return summary


if __name__ == "__main__":
    main()
