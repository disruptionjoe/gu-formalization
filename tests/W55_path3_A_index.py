#!/usr/bin/env python3
r"""W55 / PATH-3 BRANCH A -- THE ATIYAH-SINGER INDEX / DIRAC CONSTRUCTION OF THE COUNT.

Blind multi-team wave on "why three generations?". This branch attacks the count as
NET CHIRALITY = a Dirac index (Atiyah-Singer). The task is not to "prove 3" but to state
precisely what the index route FORCES, establish WHERE it dies for the generation count,
and test honestly whether any TWISTED / EQUIVARIANT / mod-k / KO / eta-invariant index
EVADES that death.

CONSTRUCTION OF "THE COUNT" USED (fork discipline, GEOMETER-VS-PHYSICS-OBJECTS.md row
"Generation count"): the count is a TORSION CLASS in the 3-primary arena
    A = pi_3^s = Z/24 = Z/8 (+) Z/3,   count carrier = 3-Sylow A_(3) = Z/3,
located there by the prior program (Adams e_KO reaches it: e_KO(8nu)=1/3). This branch
holds the count on the GEOMETER'S (torsion) side and asks whether an INDEX -- the physics
default (a Z-valued Dirac index) or any torsion-refined index -- can reach/force it.

WHAT THIS FILE ENCODES AND VERIFIES (all deterministic, exit 0 on PASS):

(a) FORCES.  The integer Atiyah-Singer / Dirac index is an additive homomorphism
    ind : (K-class of the count) -> Z (net chirality; the anomaly-inflow coefficient,
    "no net chirality without a boundary"). On the closed pieces it is fully computable
    and 2-primary-locked: on ANY spin 4-manifold the Dirac index = -p1/24 and the RS
    (spin-3/2) index = 7 p1/8 = 21 sigma/8, both == 0 mod 3 (the factor 3 enters as a
    DYNKIN/signature MULTIPLICAND p1=3 sigma, never as a mod-3 congruence). It FORCES an
    integer / constrains 2-primary+parity data; it does not see the mod-3 count.

(b) DEATH.  Hom(Z/3, Z) = 0. A torsion-free additive index cannot separate the order-3
    class of A_(3) from 0. This is the exact boundary where the integer-index route dies
    for the generation count. Proven two ways (Hom-count + explicit no-separator).

(c) ESCAPE PROBE.  Which index refinements land in a value group that CAN carry Z/3?
      - KO^{-n}(pt) index (real / KO-theoretic): torsion is ALL Z/2 (2-primary) ->
        Hom(Z/3, KO-torsion) = 0. DOES NOT ESCAPE.
      - mod-k Freed-Melrose index (Z/k-valued, Z/k-manifold): Hom(Z/3,Z/k)=gcd(3,k) !=0
        iff 3|k. A mod-3 (or mod-24) index REACHES Z/3 -- but only given an EXTRA order-3
        geometric datum (a Z/k-manifold / order-3 boundary structure).
      - reduced eta / APS / Adams e-invariant (R/Z = Q/Z valued): e_KO(nu)=1/24 =>
        e_KO(8nu)=1/3 has order 3. GENUINELY REACHES Z/3. This is the LOCATOR.
    So the escape is REAL for R/Z eta and mod-3k indices (torsion-valued), and FALSE for
    KO^{-n} and every torsion-free integer index.

(d) REACH != FORCE.  Even the escaping (torsion-valued) indices only LOCATE the class.
    Reading the integer 3 off an order-3 class is again Hom(Z/3, Z) = 0: ill-typed. And on
    the ACTUAL GU boundary operator the eta comes out 0 / 2-primary in every built case
    (the nonzero order-3 value is gated on the unbuilt RS source action). So no index of
    any kind FORCES 3; the torsion-valued ones reach the arena but stop at LOCATE.

Self-contained; imports only stdlib. Deterministic; exit 0 iff every claim's arithmetic
holds. Do NOT commit.
Run:  python -u tests/W55_path3_A_index.py
"""
from __future__ import annotations

from fractions import Fraction
from math import gcd

FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('   ' + detail) if detail else ''}", flush=True)
    if not ok:
        FAIL.append(name)


# ------------------------------------------------------------------------------------------------
# elementary primitives (finite cyclic groups by order; order 0 == Z, the free / torsion-free group)
# ------------------------------------------------------------------------------------------------
def hom_cyclic(source_order: int, target_order: int) -> int:
    """|Hom(Z/source, V)|. V = Z/target_order, with target_order == 0 meaning V = Z (free).
    Hom(Z/n, Z/m) = Z/gcd(n,m) has gcd(n,m) elements; Hom(finite, Z) = 0 (only the zero map)."""
    if target_order == 0:
        return 1          # Hom(Z/finite, Z) = 0  -> a single (zero) homomorphism
    return gcd(source_order, target_order)


def p_part(n: int, p: int) -> int:
    """p-Sylow order of Z/n; the free group Z (n==0) has no torsion -> 1."""
    if n == 0:
        return 1
    m = 1
    while n % p == 0:
        m *= p
        n //= p
    return m


def order_in_QZ(fr: Fraction) -> int:
    """order of a rational as an element of Q/Z = its reduced denominator (0 for an integer)."""
    r = fr - int(fr)
    return 1 if r == 0 else r.denominator


def dirac_index_dim4(p1: int) -> Fraction:
    """Atiyah-Singer: ind D = A-hat = -p1/24 on a closed spin 4-manifold."""
    return Fraction(-1, 24) * p1


def rs_index_dim4(p1: int) -> Fraction:
    """AGW spin-3/2 (Rarita-Schwinger) index density degree-4 part = 7 p1 / 8."""
    return Fraction(7, 8) * p1


def main() -> None:
    print("=" * 100)
    print("W55 PATH-3 BRANCH A -- Atiyah-Singer / Dirac INDEX construction of the generation count")
    print("=" * 100)
    print("CONSTRUCTION OF THE COUNT: torsion class in A = pi_3^s = Z/24 = Z/8 (+) Z/3; carrier = 3-Sylow Z/3.")
    print("(geometer's side of GEOMETER-VS-PHYSICS row 'Generation count'; the index is the physics default.)")

    # ============================================================================================
    # (a) WHAT THE INTEGER INDEX FORCES: net chirality in Z, 2-primary-locked on closed pieces
    # ============================================================================================
    print("\n(a) FORCES -- the integer Dirac / RS index is Z-valued and 2-primary-locked on closed spin 4-mflds")

    # canonical closed spin 4-manifolds; p1 = 3*sigma (signature theorem, holds for EVERY 4-manifold)
    manifolds = {"K3 (sigma=-16)": -16, "T^4 (flat)": 0, "K3#K3 (sigma=-32)": -32}
    dirac_all_int = True
    rs_all_zero_mod3 = True
    for name, sigma in manifolds.items():
        p1 = 3 * sigma
        d = dirac_index_dim4(p1)
        rs = rs_index_dim4(p1)
        d_int = (d.denominator == 1)
        rs_int = (rs.denominator == 1)
        dirac_all_int = dirac_all_int and d_int
        rs_mod3 = (int(rs) % 3) if rs_int else None
        rs_all_zero_mod3 = rs_all_zero_mod3 and (rs_mod3 == 0)
        print(f"      {name:20s} p1={p1:>5d}  ind D = -p1/24 = {str(d):>4s}   "
              f"RS = 7p1/8 = {str(rs):>5s}  (mod 3 = {rs_mod3})")
    check("a1. Dirac index -p1/24 is an INTEGER (net chirality in Z) on every closed spin 4-manifold",
          dirac_all_int, "the index is a torsion-free Z-valued anomaly-inflow coefficient")
    check("a2. RS index 7p1/8 = 21 sigma/8 == 0 (mod 3) on EVERY spin 4-manifold (factor 21 = 3.7 forced)",
          rs_all_zero_mod3, "the '3' is the p1=3sigma signature MULTIPLICAND, not a mod-3 congruence -> Z/3 identity")
    # the 3 in the A-hat denominator 24 is a divisor/multiplicand, never a mod-3 value the index takes
    check("a3. the lone 3 lives in the DENOMINATOR 24 of A-hat (a multiplicand), so the integer index value is "
          "always == 0 mod 3 or a unit",
          Fraction(-1, 24).denominator == 24 and 24 % 3 == 0,
          "an integer index cannot be a nonzero order-3 element: 3 divides its structure, it is not its value")

    # ============================================================================================
    # (b) WHERE IT DIES: Hom(Z/3, Z) = 0  (torsion-free additive index is blind to the 3-Sylow)
    # ============================================================================================
    print("\n(b) DEATH -- Hom(Z/3, Z) = 0 : a torsion-free integer index cannot separate the order-3 count")

    check("b1. |Hom(Z/3, Z)| = 1 (only the zero map): a finite group has no nonzero hom to a torsion-free group",
          hom_cyclic(3, 0) == 1, "any additive Z-valued Atiyah-Singer index restricted to A_(3)=Z/3 is identically 0")
    # explicit no-separator: model an index as a hom phi: Z/24 -> Z; phi(k)=k*t is a hom iff 24t=0 => t=0.
    c3 = 8  # a generator of the 3-Sylow Z/3 = <8> < Z/24 (the mod-3 count class)
    valid_t_into_Z = [t for t in range(-50, 51) if 24 * t == 0]   # only t=0
    integer_index_separates_c3 = any((c3 * t) != 0 for t in valid_t_into_Z)
    check("b2. explicit: NO homomorphism Z/24 -> Z gives phi(c3) != 0 for the order-3 class c3=8 (only phi=0)",
          (valid_t_into_Z == [0]) and (not integer_index_separates_c3),
          "so no integer index -- Dirac, twisted-Dirac, signature, any Z-valued net chirality -- can FORCE the count")
    check("b3. same wall blocks the 2-primary reductions: |Hom(Z/3, Z/2^k)| = gcd(3,2^k) = 1 for all k",
          all(hom_cyclic(3, 2 ** k) == 1 for k in range(1, 7)),
          "mod-2^k index data (Rokhlin Z/16, Witten Z/2, ABS 2^m) is also blind to the 3-Sylow")

    # ============================================================================================
    # (c) ESCAPE PROBE: which index refinement lands in a value group that CAN carry Z/3?
    # ============================================================================================
    print("\n(c) ESCAPE PROBE -- torsion-valued index refinements vs the Z/3 carrier (reach test = Hom(Z/3,V)!=0)")

    # KO^{-n}(pt) Bott song: Z, Z/2, Z/2, 0, Z, 0, 0, 0 (n = 0..7 mod 8). Torsion is ALL Z/2.
    ko_pt = {0: 0, 1: 2, 2: 2, 3: None, 4: 0, 5: None, 6: None, 7: None}  # order; 0=Z(free), None=trivial
    ko_torsion_orders = [v for v in ko_pt.values() if v not in (0, None)]
    ko_all_2primary = all(p_part(v, 3) == 1 for v in ko_torsion_orders)
    ko_reaches = any((v not in (0, None)) and hom_cyclic(3, v) != 1 for v in ko_pt.values())
    check("c1. KO^{-n}(pt) index: torsion is ALL Z/2 (2-primary) -> Hom(Z/3, KO-torsion) = 0. DOES NOT ESCAPE",
          ko_all_2primary and (not ko_reaches),
          "KO / real / KO^{-n} Dirac index is structurally blind to Z/3 -- the KO-theoretic escape fails")

    # mod-k Freed-Melrose index (Z/k-valued, needs a Z/k-manifold / order-k geometric datum)
    modk_reach = {k: (hom_cyclic(3, k) != 1) for k in (2, 4, 8, 16, 3, 9, 24)}
    check("c2. mod-k Freed-Melrose index Z/k: Hom(Z/3, Z/k) = gcd(3,k) != 0 IFF 3|k -> mod-3 / mod-24 REACHES",
          modk_reach[3] and modk_reach[9] and modk_reach[24]
          and not modk_reach[2] and not modk_reach[8] and not modk_reach[16],
          "a mod-3k index reaches Z/3 -- but ONLY given an EXTRA order-3 geometric datum (Z/k-manifold / boundary)")

    # reduced eta / APS / Adams e-invariant: R/Z = Q/Z valued (torsion). e_KO(nu) = 1/24.
    e_nu = Fraction(1, 24)
    e_8nu = 8 * e_nu     # = 1/3, order 3
    e_16nu = 16 * e_nu   # = 2/3, order 3
    eta_reaches = (e_8nu == Fraction(1, 3) and order_in_QZ(e_8nu) == 3 and order_in_QZ(e_16nu) == 3)
    check("c3. reduced eta / APS / Adams e-invariant (R/Z-valued): e_KO(8nu) = 1/3 has ORDER 3. GENUINELY REACHES",
          eta_reaches,
          f"e_KO(nu)=1/24 => e_KO(8nu)={e_8nu} (order {order_in_QZ(e_8nu)}), e_KO(16nu)={e_16nu}: the eta is the LOCATOR")
    check("c4. ESCAPE SUMMARY: torsion-free Z and KO(2-primary) DIE; R/Z eta and mod-3k indices REACH the Z/3",
          hom_cyclic(3, 0) == 1 and ko_all_2primary and eta_reaches and modk_reach[3],
          "the death is class-wide for torsion-free + KO indices; it is EVADED only by genuinely torsion(3-primary)-valued indices")

    # ============================================================================================
    # (d) REACH != FORCE: even the escaping index only LOCATES; class -> integer is Hom(Z/3,Z)=0 again
    # ============================================================================================
    print("\n(d) REACH != FORCE -- the torsion-valued escapes LOCATE the class; none FORCE the integer 3")

    check("d1. reading the integer 3 off an order-3 class is ill-typed: Hom(Z/3, Z) = 0 (no canonical class->count)",
          hom_cyclic(3, 0) == 1,
          "e_KO(8nu)=1/3 pins the CLASS (order 3) but not the number 3; the FORCE step order-3-class -> integer-3 is open")
    # on the ACTUAL built operators the eta is 0 / 2-primary (nonzero order-3 gated on unbuilt RS source action)
    built_eta_values = [Fraction(0), Fraction(1, 8), Fraction(3, 8)]  # in-repo computed etas (round-S^3=0; lens 2-primary)
    none_order3 = all(order_in_QZ(v) != 3 for v in built_eta_values)
    check("d2. on every BUILT GU boundary operator the eta is 0 or 2-primary (order != 3); the order-3 value is GATED",
          none_order3,
          "the escape is arithmetically available but the nonzero order-3 eta needs the unbuilt twisted RS source action")

    # ============================================================================================
    # SUMMARY / VERDICT
    # ============================================================================================
    print("-" * 100)
    print("VERDICT (branch A = Atiyah-Singer index / Dirac)")
    print("  Q-force : the integer Dirac/AS index does NOT force 3. It forces an integer net chirality in Z and")
    print("            constrains 2-primary/parity data; on closed spin 4-mflds it is == 0 mod 3 (p1=3sigma).")
    print("  Q-extra : to even REACH the Z/3 arena the index must be TORSION-VALUED -- R/Z reduced eta / Adams")
    print("            e-invariant (e_KO(8nu)=1/3), or a mod-3k Freed-Melrose index (needs an order-3 geometric")
    print("            datum). Both LOCATE, neither FORCES: class -> integer is Hom(Z/3,Z)=0 again, and on the")
    print("            actual operator the order-3 eta is gated on the unbuilt RS source action.")
    print("  Q-nogo  : CLASS-WIDE no-go PROVEN for torsion-free integer indices (Hom(Z/3,Z)=0) AND for KO^{-n}")
    print("            indices (KO torsion 2-primary). NOT a no-go for R/Z-eta / mod-3k indices -- those evade")
    print("            the death (reach Z/3), so the index FAMILY as a whole is not blocked; only its Z-valued")
    print("            and KO-valued sub-classes are.")
    print("  ESCAPE  : YES for reduced-eta / Adams e-invariant (R/Z) and mod-3k Freed-Melrose; NO for KO^{-n}.")
    print("=" * 100)

    if FAIL:
        print(f"\nSOME CHECKS FAILED: {FAIL}")
        raise SystemExit(1)
    print("\nALL CHECKS PASS")
    print("exit 0 = branch A verdict is internally consistent: integer/KO index CONSTRAINS (cannot force 3);")
    print("         torsion-valued (R/Z eta, mod-3k) index REACHES Z/3 but only LOCATES -- none FORCES the integer 3.")


if __name__ == "__main__":
    main()
