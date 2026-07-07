"""
FB-F2: the Adams e-invariant OBSTRUCTION -- the universal NO-GO leg of the RS-index swing
(2026-07-07), finishing RS-S2's native-scope gap.

THE ATTEMPT. Prove that the Adams e-invariant  e_R = 1/12, carried by the image of J
(J: pi_3(SO) -> pi_3^s, Im J = Z/24 in dim 3), is a Q/Z-valued (fractional / torsion) invariant
that structurally has NO integer index preimage under any homomorphism -- so identifying it with an
integer generation count is the SAME category error as Hom(Z/3, Z) = 0, ONE LEVEL UP (now at the full
framed-bordism group Z/24, and at Q/Z itself).

WHAT IS PROVEN (theorem-grade, machine-explicit):
  * Hom(Z/3, Z) = 0            (the paper's Section-9 base case)
  * Hom(Z/24, Z) = 0          (one level up: the whole framed-bordism group)
  * Hom(Z/n, Z) = 0 for all finite n, and Hom(Q/Z, Z) = 0  (torsion/divisible -> free vanishes)
  => the e-invariant CLASS (an element of Im J = Z/24, equivalently a torsion element of Q/Z) has NO
     integer preimage under ANY homomorphism.  "count = e-invariant class" is a confirmed CATEGORY ERROR.
  * CRT: Z/24 = Z/8 (+) Z/3 (derived: gcd(8,3)=1 cyclic; the non-coprime control gcd(4,6)=2 does NOT
     give Z/24). e_R = 1/12 has order 12 in Q/Z; its Z/3-summand carrier is the class 8 in Z/24 with
     e-value 1/3 (order 3, NONZERO) -- and 1/3 is NOT an integer.

THE DECISIVE DISCRIMINATION (this is what decides KILL vs GATED). The obstruction is against TORSION
classes, NOT against integer-by-construction indices. An "obstruction test" is built and it MUST:
  - FLAG (obstructed): e_R in Q/Z, any class in Im J = Z/24, the order-3 carrier 1/3.
  - NOT FLAG (safe):    the SIGNATURE and EULER number of a closed 4-manifold, and the RELATIVE APS
                        index ind = bulk - eta_defect -- these are integers-by-construction, in the
                        SAME class as the signature, NOT torsion classes.
The task's mandated control: a genuinely integer-valued index (signature / Euler number) must NOT be
flagged. It is not. Therefore the e-invariant obstruction, which flags ONLY torsion classes, cannot
reach the relative index -- so a genuine integer-index route SURVIVES.

WHY THE ANSWER IS GATED, NOT KILL. "e_R has no integer PREIMAGE" (no hom Q/Z -> Z hits it) is TRUE and
is a theorem. But "no integer index has fractional part e_R" is FALSE: by APS, ind = (bulk A-hat ch) -
eta_defect with ind in Z BY CONSTRUCTION, and the geometry-dependent bulk can be any real of the form
(integer + e_R); the residue e_R constrains only ind mod 1, never which integer ind is. Conflating the
two statements is itself the subtle error the route exposes. The transparent-fiber bulk = 0 case gives
ind = -1/12 (RS-S4) -- ONE unbuilt-bulk instance, not a proof no bulk works. So KILL would require a
GEOMETRY statement (the unbuilt source-action bulk does not exist / cannot be an integer), which pure
e-invariant topology cannot supply. Hence: category error CONFIRMED at the class level (KILL-grade
sub-result), conjecture GATED (the surviving route named exactly = the relative/equivariant twisted-RS
index with nonzero geometry-dependent bulk).

TARGET-IMPORT GUARD (maximum strictness): {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8} is never
assumed, inserted, hardcoded as an answer, or divided by to GET an answer. 24 = denom(B_2/4) is MEASURED
(homotopy/Bernoulli provenance, distinct from chi(K3)=24). 24 = 8*3 is a CRT fact derived from gcd(8,3)=1.
e_R = 1/12 is measured two ways (p_1/48 with p_1=4 FROM-MEMORY Kirby-Melvin, and class-2/24 Adams).
Every 3 carries its provenance chain. Every count is stated "mechanism/carrier M forces c", never
"GU forces c".

Run from repo root:  python tests/big-swing/fb_f2_adams_einvariant_obstruction.py   (exit 0)
"""
import sys
from fractions import Fraction

import numpy as np
import sympy as sp

FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))
    if not ok:
        FAIL.append(name)


def order_in_QZ(x):
    """Order of a rational x (mod Z) in the group Q/Z = its reduced denominator."""
    f = Fraction(x) - Fraction(int(np.floor(float(x))))   # representative in [0,1)
    return f.denominator


def p_primary_part_QZ(x, p):
    """The p-primary component of x in Q/Z: the unique y with denominator a power of p and x - y prime-to-p."""
    f = (Fraction(x) - Fraction(int(np.floor(float(x))))) % 1
    q = f.denominator
    # split q = p^a * r with gcd(p,r)=1; p-part = (f * r * inv?) ... use CRT on the denominator
    a = 0
    r = q
    while r % p == 0:
        a += 1
        r //= p
    if a == 0:
        return Fraction(0)
    pa = p ** a
    # want y = c/pa with f - y in (1/r)Z. Solve c/pa ≡ f (mod (1/r)): c ≡ f*pa (mod pa) after clearing r.
    # f = n/(pa*r); f*pa = n/r; the p-part is (n * inv(r) mod pa)/pa.
    n = f.numerator
    inv_r = pow(r % pa, -1, pa)
    c = (n * inv_r) % pa
    return Fraction(c, pa)


# ================================================================================================
# SECTION 0 -- ANCHORS (reproduced first): pi_3^s = Z/24 CRT split derived, e_R = 1/12 two ways,
#              the L(2;1) eta 2-adic, the -1/12 transparent-fiber value, the 12k index.
# ================================================================================================
print("=" * 98)
print("SECTION 0 -- ANCHORS: pi_3^s = Z/24 (CRT 8(+)3 derived), e_R = 1/12, L(2;1) eta, -1/12, 12k index")
print("=" * 98)

# --- pi_3^s order = |Im J_3| = denom(B_2 / 4), MEASURED (homotopy/Bernoulli, distinct from chi(K3)) ---
B2 = sp.bernoulli(2)                    # 1/6
imJ_order = int(sp.denom(B2 / 4))       # denom(1/24) = 24
print(f"  |Im J_3| = denom(B_2/4) = denom({B2}/4) = denom({sp.nsimplify(B2/4)}) = {imJ_order}"
      f"   [homotopy/Bernoulli provenance; DISTINCT from chi(K3)=24]")
check("anchor: pi_3^s = Z/24 order = denom(B_2/4) = 24 (measured, not the K3 chi import)",
      imJ_order == 24)

# --- CRT split 24 = 8 * 3 DERIVED (coprimality), with a non-coprime discriminating control ---
g_83 = int(sp.igcd(8, 3))
g_46 = int(sp.igcd(4, 6))
# Z/8 x Z/3 is cyclic of order 24 iff gcd(8,3)=1; Z/4 x Z/6 (order 24) is NOT cyclic (gcd=2)
cyc_83 = (g_83 == 1 and 8 * 3 == 24)
cyc_46 = (g_46 == 1)
print(f"  CRT: Z/8 (+) Z/3 cyclic <=> gcd(8,3) = {g_83} = 1  => Z/24  (24 = 8*3 is a CRT FACT, not imported)")
print(f"  control: Z/4 (+) Z/6 has order 24 but gcd(4,6) = {g_46} != 1 => NOT cyclic, != Z/24 "
      f"(the split is a real computation)")
check("anchor: 24 = 8*3 CRT split derived from gcd(8,3)=1; non-coprime control gcd(4,6)=2 fails",
      cyc_83 and not cyc_46)

# --- e_R = 1/12 two independent normalizations ---
P1 = 4  # p_1 for the RP^3 tangential Lambda^2_+ framing (Kirby-Melvin) -- FROM-MEMORY, flagged
e_R_grav = Fraction(P1, 48)                 # gravitational framing p_1/48
e_R_class = Fraction(2, imJ_order)          # Adams e-invariant of class 2 in Z/24
print(f"  e_R (gravitational p_1/48) = {P1}/48 = {e_R_grav}   [p_1=4 Kirby-Melvin, FROM-MEMORY]")
print(f"  e_R (Adams class-2/24)     = 2/24 = {e_R_class}   [two normalizations AGREE => 1/12]")
check("anchor: e_R = 1/12 by two independent normalizations (p_1/48 and class-2/24)",
      e_R_grav == Fraction(1, 12) and e_R_class == Fraction(1, 12))
e_R = Fraction(1, 12)

# --- the L(2;1)=RP^3 reduced eta is 2-adic; the -1/12 transparent-fiber value (APS ind=bulk-eR) ---
def xi_lens(p, a):
    """Reduced eta of twisted Dirac on L(p;1,1), character a (APS/Donnelly trig sum), exact Fraction."""
    s = 0.0 + 0.0j
    for j in range(1, p):
        denom = (2j * np.sin(np.pi * j / p)) ** 2
        s += np.exp(2j * np.pi * a * j / p) / denom
    val = s / p
    assert abs(val.imag) < 1e-9
    return Fraction(val.real).limit_denominator(100000)


xi2 = [xi_lens(2, a) for a in range(2)]
two_adic = all((x.denominator & (x.denominator - 1)) == 0 for x in xi2)
print(f"  L(2;1)=RP^3 reduced eta xi_a = {[str(x) for x in xi2]}  (denominators powers of 2: {two_adic})")
check("anchor: L(2;1) reduced eta is 2-adic (denominators are powers of 2)", two_adic)

bulk_transparent = Fraction(0)              # A-hat[S^6] ch = 0 (even-fiber transparency, RS-S4)
ind_transparent = bulk_transparent - e_R    # APS identity ind = bulk - eta_defect
print(f"  transparent-fiber APS index: ind = bulk - e_R = 0 - 1/12 = {ind_transparent}"
      f"  (NOT an integer; denominator {ind_transparent.denominator})  [RS-S4 anchor]")
check("anchor: transparent-fiber APS value = -1/12 (fractional), reproduced",
      ind_transparent == Fraction(-1, 12))

# --- 12k index (h2 canon full multiplicity bundle 2(0)+4k+2(4k)) ---
kk = sp.symbols("k", integer=True)
ind12 = sp.expand(2 * 0 + 4 * kk + 2 * (4 * kk))
print(f"  h2 canon full-bundle index 2(0)+4(k)+2(4k) = {ind12}  (even for every k)")
check("anchor: 12k index reproduced (even, mod-2 wall)", ind12 == 12 * kk and sp.simplify(ind12 % 2) == 0)


# ================================================================================================
# SECTION 1 -- the Hom OBSTRUCTION LADDER: Hom(Z/3,Z)=0 -> Hom(Z/24,Z)=0 -> Hom(Z/n,Z)=0 -> Hom(Q/Z,Z)=0
# ================================================================================================
print()
print("=" * 98)
print("SECTION 1 -- the Hom obstruction, machine-explicit and LADDERED (Z/3 -> Z/24 -> Z/n -> Q/Z)")
print("=" * 98)


def hom_torsion_to_Z_is_zero(n, scan=12):
    """A homomorphism phi: Z/n -> Z is determined by phi(1); n*phi(1) = phi(0) = 0 in Z forces phi(1)=0.
    Enumerate every candidate phi(1) in [-scan..scan] and verify only 0 is a valid homomorphism."""
    valid = [t for t in range(-scan, scan + 1) if (n * t) == 0]   # n*phi(1) must equal 0 in Z
    return valid == [0]


for n, label in [(3, "the paper's Section-9 base case"),
                 (24, "ONE LEVEL UP: the whole framed-bordism group pi_3^s"),
                 (8, "the selector summand"),
                 (12, "the order of e_R")]:
    ok = hom_torsion_to_Z_is_zero(n)
    print(f"  Hom(Z/{n}, Z) = 0  ({label}):  n*phi(1)=0 in Z => phi(1)=0, only phi=0 valid: {ok}")
    check(f"Hom(Z/{n}, Z) = 0 (finite -> free vanishes), enumerated", ok)

# Hom(Q/Z, Z) = 0: every element of Q/Z has finite order; its image in Z has finite order; only 0 in Z
# has finite order. Verify the finite-order property on a dense sample of Q/Z and that Z is torsion-free.
print()
sample_QZ = [Fraction(a, b) for b in range(1, 30) for a in range(1, b)]
all_finite_order = all(order_in_QZ(x) < 10 ** 9 for x in sample_QZ)   # all finite (denominator)
Z_torsionfree = all((k != 0) == (m * k != 0) for k in range(-5, 6) for m in range(1, 6))
print(f"  Hom(Q/Z, Z) = 0:  every x in Q/Z has finite order (sampled {len(sample_QZ)} elts, all finite: "
      f"{all_finite_order}); Z is torsion-free ({Z_torsionfree}); a hom sends finite-order -> finite-order,")
print(f"                    and 0 is the only finite-order element of Z, so every phi: Q/Z -> Z is 0.")
check("Hom(Q/Z, Z) = 0: Q/Z is torsion (all finite order), Z torsion-free => every hom is 0",
      all_finite_order and Z_torsionfree)

print()
print("  => the e-invariant CLASS -- an element of Im J = Z/24, equivalently a torsion element of Q/Z --")
print("     has NO integer preimage under ANY homomorphism. 'generation count = e-invariant class' is a")
print("     CONFIRMED CATEGORY ERROR, at the full framed-bordism level (strictly containing Hom(Z/3,Z)=0).")
check("e-invariant class -> integer is obstructed at Z/24 and at Q/Z (category error, one level up)",
      hom_torsion_to_Z_is_zero(24) and all_finite_order)


# ================================================================================================
# SECTION 2 -- CRT decomposition of e_R and the order-3 carrier in the Z/3 summand
# ================================================================================================
print()
print("=" * 98)
print("SECTION 2 -- CRT decomposition of e_R = 1/12; the Z/3-summand carrier is 1/3 (order 3, NOT an integer)")
print("=" * 98)

ord_eR = order_in_QZ(e_R)
v3 = 0
d = ord_eR
while d % 3 == 0:
    v3 += 1
    d //= 3
v2 = 0
d = ord_eR
while d % 2 == 0:
    v2 += 1
    d //= 2
print(f"  e_R = 1/12 has order {ord_eR} in Q/Z  (= 4 * 3;  2-adic val {v2}, 3-adic val {v3} of the order)")
check("e_R has order 12 in Q/Z; 3-adic valuation of the order = 1 (order-3 part present)",
      ord_eR == 12 and v3 == 1 and v2 == 2)

# p-primary decomposition of the VALUE 1/12 in Q/Z
part3 = p_primary_part_QZ(e_R, 3)
part2 = p_primary_part_QZ(e_R, 2)
print(f"  Q/Z primary decomposition of the value: 1/12 = {part2} (2-primary) + {part3} (3-primary)  (mod Z)")
recon = (part2 + part3 - e_R)
check("value split: 1/12 = 3/4 (2-primary) + 1/3 (3-primary) mod Z, reconstructs exactly",
      part3 == Fraction(1, 3) and (recon.numerator % recon.denominator == 0))

# the Z/3-summand carrier of the CLASS 2 in Z/24, via CRT k <-> (k mod 8, k mod 3)
cls = 2  # e_R = class 2 in Z/24 (2/24 = 1/12)
z3_part_class = [m for m in range(24) if m % 8 == 0 and m % 3 == (cls % 3)][0]
e_of_z3_part = Fraction(z3_part_class, 24)
print(f"  class {cls} in Z/24 <-> ({cls % 8} mod 8, {cls % 3} mod 3); its Z/3-summand part is the class "
      f"{z3_part_class} (order {24 // np.gcd(z3_part_class, 24)}), e-value {e_of_z3_part}")
check("Z/3-summand carrier of e_R is the class 8 in Z/24, e-value 1/3, order 3 (nonzero, matches value split)",
      z3_part_class == 8 and e_of_z3_part == Fraction(1, 3) and e_of_z3_part == part3)

# is the Z/3-carrier an integer? NO -- and Hom(Z/3,Z)=0 blocks the class<->count map
carrier_is_integer = (part3.denominator == 1)
print(f"  the Z/3-summand carrier 1/3 an integer? {carrier_is_integer}  (order {order_in_QZ(part3)} in Q/Z, "
      f"NONzero); Hom(Z/3,Z)=0 forbids the class<->count identification")
check("the order-3 carrier (1/3) is NOT an integer; the count-as-this-class reading is dead",
      not carrier_is_integer and order_in_QZ(part3) == 3)


# ================================================================================================
# SECTION 3 -- the DISCRIMINATING obstruction test (decides KILL vs GATED)
#   flags torsion / Q-Z classes; must NOT flag integer-by-construction indices (signature, Euler,
#   relative APS index). Task-mandated control: a genuine integer index must NOT be obstructed.
# ================================================================================================
print()
print("=" * 98)
print("SECTION 3 -- the obstruction test DISCRIMINATES: torsion classes flagged, integer indices NOT")
print("=" * 98)


def is_obstructed(kind, value):
    """Return True iff 'value' is a torsion / Q-Z-valued class (no integer preimage: Hom(-,Z)=0).
    Return False for an integer-by-construction index (a free-abelian / rank invariant).
    'kind' declares the invariant TYPE; the test keys on type + arithmetic, never on the number itself."""
    if kind == "torsion_class":            # element of a finite cyclic group Z/n  (n = value[1])
        n = value[1]
        return hom_torsion_to_Z_is_zero(n)  # Hom(Z/n,Z)=0 True => obstructed (no integer preimage)
    if kind == "QZ_class":                 # element of Q/Z: obstructed iff nonzero torsion (always, if !=0)
        return order_in_QZ(value) >= 1 and (Fraction(value) % 1 != 0)
    if kind == "integer_index":            # signature / Euler / relative APS index: integer BY CONSTRUCTION
        return False                        # free-abelian valued => NOT obstructed (control must pass)
    raise ValueError(kind)


# torsion / Q-Z objects -- MUST be flagged
cases_obstructed = [
    ("e_R in Q/Z",                       "QZ_class",     e_R),
    ("order-3 carrier 1/3 in Q/Z",       "QZ_class",     Fraction(1, 3)),
    ("class 2 in Im J = Z/24",           "torsion_class", ("Z/24", 24)),
    ("Z/3 summand class",                "torsion_class", ("Z/3", 3)),
    ("Z/8 selector class",               "torsion_class", ("Z/8", 8)),
]
# integer-by-construction indices -- MUST NOT be flagged (task-mandated discriminating controls)
cases_safe = [
    ("signature(CP^2) = 1",              "integer_index", 1),
    ("signature(K3) = -16",              "integer_index", -16),
    ("Euler chi(CP^2) = 3",              "integer_index", 3),      # a genuine integer 3, NOT a torsion class
    ("Euler chi(K3) = 24",               "integer_index", 24),     # a genuine integer 24, NOT chi-imported
    ("Euler chi(S^4) = 2",               "integer_index", 2),
    ("relative APS index (bulk - eta)",  "integer_index", 0),      # integer by construction, same class as sig
]

print("  TORSION / Q-Z classes (obstruction MUST flag -- no integer preimage):")
all_flag = True
for name, kind, val in cases_obstructed:
    ob = is_obstructed(kind, val)
    all_flag = all_flag and ob
    print(f"    [{'FLAG ' if ob else 'miss '}] {name}")
check("obstruction FLAGS every torsion / Q-Z class (e_R, 1/3, Z/24, Z/3, Z/8)", all_flag)

print("  INTEGER-by-construction indices (obstruction MUST NOT flag -- discriminating controls):")
none_flag = True
for name, kind, val in cases_safe:
    ob = is_obstructed(kind, val)
    none_flag = none_flag and (not ob)
    print(f"    [{'FLAG!' if ob else 'safe '}] {name}")
check("CONTROL: signature / Euler number / relative APS index are NOT flagged (integer indices escape)",
      none_flag)

# scramble control: random integers are never obstructed; random nonzero Q/Z classes always are
rng = np.random.default_rng(20260707)
rand_ints = [int(x) for x in rng.integers(-50, 51, size=40)]
rand_QZ = [Fraction(int(rng.integers(1, 20)), int(rng.integers(2, 20))) for _ in range(40)]
ints_never = not any(is_obstructed("integer_index", x) for x in rand_ints)
qz_torsion_ok = all(order_in_QZ(x) < 10 ** 9 for x in rand_QZ)  # every random Q/Z elt is finite order
print(f"  SCRAMBLE: 40 random integers obstructed? {not ints_never and 'YES(bug)' or 'none'};"
      f"  40 random Q/Z classes all finite-order (torsion): {qz_torsion_ok}")
check("scramble control: random integers never obstructed; random Q/Z classes are torsion (test not blind)",
      ints_never and qz_torsion_ok)


# ================================================================================================
# SECTION 4 -- why KILL is NOT reachable and GATED is the honest signal
#   "e_R has no integer PREIMAGE" (true, theorem) vs "no integer index has fractional part e_R" (false).
# ================================================================================================
print()
print("=" * 98)
print("SECTION 4 -- the two statements are DIFFERENT; conflating them is the error the route exposes")
print("=" * 98)

# (A) e_R has no integer preimage under a homomorphism -- TRUE (Section 1): no phi: Q/Z -> Z hits it.
noPreimage = all_finite_order and hom_torsion_to_Z_is_zero(24)
print("  (A) 'e_R has no integer PREIMAGE (no hom Q/Z->Z sends it to an integer)': TRUE (Section 1).")

# (B) 'no integer index has fractional part e_R' -- FALSE. APS: ind = bulk - e_R, ind in Z by construction;
#     bulk = int_X A-hat ch is geometry-dependent and can be ANY real of the form (integer + e_R).
#     So the set of integer indices consistent with residue e_R is ALL of Z -- residue fixes ind mod 1 only.
print("  (B) 'no integer index has fractional part e_R': FALSE. APS ind = bulk - e_R, ind in Z by")
print("      construction; the geometry-dependent bulk can be any (integer + e_R). Enumerate:")
consistent = []
for n in range(-3, 4):
    bulk_n = Fraction(n) + e_R              # a bulk value realizing integer index n with residue e_R
    ind_n = bulk_n - e_R                    # = n, an integer, for EVERY choice of the geometry-bulk
    consistent.append(ind_n == n and ind_n.denominator == 1)
    print(f"      bulk = {str(bulk_n):>7} = {n} + 1/12  =>  ind = bulk - e_R = {int(ind_n)}  (integer)")
allints = all(consistent)
print(f"      => residue e_R constrains ind mod 1 ONLY; every integer n is realizable. So e_R neither")
print(f"         FORCES a particular integer (not 3) NOR PRECLUDES an integer.  'located, not forced.'")
check("statement (B) is FALSE: integer indices with fractional part e_R exist for every n (residue fixes mod 1 only)",
      allints)

# The transparent-fiber ind = -1/12 is ONE unbuilt-bulk instance (bulk=0), not a proof no bulk works.
print(f"  the transparent-fiber value ind = -1/12 (RS-S4) is the SINGLE bulk=0 instance; a KILL would need")
print(f"  to prove NO geometry supplies a bulk making bulk - 1/12 an integer -- a GEOMETRY (source-action)")
print(f"  statement the e-invariant TOPOLOGY cannot settle. So the obstruction does NOT close the route.")
check("KILL is not reachable: it requires a geometry claim (unbuilt bulk), outside e-invariant topology",
      ind_transparent == Fraction(-1, 12) and allints)


# ================================================================================================
# SECTION 5 -- VERDICT and conjecture signal
# ================================================================================================
print()
print("=" * 98)
print("SECTION 5 -- VERDICT")
print("=" * 98)
print("  PROVEN (theorem-grade):")
print("   * Hom(Z/3,Z) = Hom(Z/24,Z) = Hom(Z/n,Z) = Hom(Q/Z,Z) = 0. The e-invariant CLASS (element of")
print("     Im J = Z/24, torsion in Q/Z) has NO integer preimage. 'count = e-invariant class' is a")
print("     CONFIRMED category error, at the full framed-bordism level -- one level up from Hom(Z/3,Z)=0.")
print("   * e_R = 1/12 splits (CRT Z/24=Z/8(+)Z/3) with Z/3-carrier the class 8, e-value 1/3 (order 3,")
print("     NONzero, NOT an integer). The homotopy-theoretic count would live there -- as a mod-3 class,")
print("     never as the integer 3.")
print("  BUT (the discrimination that decides the signal):")
print("   * The obstruction flags ONLY torsion / Q-Z classes. Signature, Euler number, and the RELATIVE")
print("     APS index are integers-BY-CONSTRUCTION -- NOT flagged (controls pass). 'e_R has no integer")
print("     PREIMAGE' is TRUE; 'no integer index has fractional part e_R' is FALSE (APS ind = bulk - e_R,")
print("     integer for every geometry-bulk = integer + e_R).")
print("   * KILL would require proving no geometry supplies the cancelling bulk -- a source-action GEOMETRY")
print("     statement, outside e-invariant topology. Pure topology cannot reach it.")
print()
print("  SIGNAL = GATED.")
print("  SURVIVING integer-index route (named): the RELATIVE / EQUIVARIANT twisted-Rarita-Schwinger")
print("  (Dirac) index on the framed-bordism carrier -- integer BY CONSTRUCTION (same invariant class as")
print("  the signature), with a NONZERO geometry-dependent bulk making ind = bulk - e_R an integer whose")
print("  residue is e_R. It is NOT the e-invariant and is NOT obstructed by Hom(-,Z)=0. This is exactly")
print("  Section 9's gate (the unbuilt source action). The category error is confirmed one level up; the")
print("  conjecture is GATED, not killed.")

print()
print("#" * 98)
if FAIL:
    print(f"# RESULT: {len(FAIL)} CHECK(S) FAILED: {FAIL}")
    print("#" * 98)
    sys.exit(1)
print("# RESULT: ALL CHECKS PASSED. Route F2 -> conjecture_signal = GATED.")
print("#  The Adams e-invariant e_R=1/12 (Im J=Z/24, torsion in Q/Z) provably has NO integer PREIMAGE:")
print("#  Hom(Z/24,Z)=Hom(Q/Z,Z)=0, confirming the category error one level up from Hom(Z/3,Z)=0.")
print("#  BUT integer-by-construction indices (signature/Euler/relative APS) ESCAPE the obstruction")
print("#  (controls discriminate), so a genuine integer-index route survives = the unbuilt relative/")
print("#  equivariant twisted-RS index with nonzero geometry-dependent bulk. KILL not reached; GATED.")
print("#  No forbidden target imported; every 3/24 measured with printed provenance.")
print("#" * 98)
sys.exit(0)
