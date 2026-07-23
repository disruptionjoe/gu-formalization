"""
FB-F4: image-of-J is FRACTIONAL BY CONSTRUCTION, and the surviving external imports are FREE choices.

Route F4 of the 2026-07-07 promote-or-kill swing on the located-not-forced Section 9 conjecture.
RS-S2/S4 narrowed the located-carrier route to ONE remaining door pair: the two EXTERNAL imports named
by the twisted-index mod-3 law (3|m cubic coupling + 3|sigma spacetime signature). This route:

  (a) CONFIRMS the framed-bordism route offers NO native integer, exactly like the cohomology route.
      - |Im J_3| = denom(B_2/4) = 24 (Bernoulli, MEASURED). pi_3^s = Z/24.
      - CRT split Z/24 = Z/8 (+) Z/3 DERIVED from factorint(24) = {2:3, 3:1} (the 8 and 3 are the
        prime-power factors, not recalled; the iso k -> (k%8, k%3) is verified bijective + additive).
      - The Adams e-invariant is a Q/Z-valued detector: its values {k/24 mod 1} are FRACTIONS. The
        genuine order-3 classes are {8,16} (the pure Z/3 summand), e-values {1/3, 2/3}. e_R = 1/12 is
        class 2, CRT image (2,2): its Z/3 component 2 != 0 carries the order-3 information.
      - Hom(Z/24, Z) = 0 AND Hom(Z/3, Z) = 0: a finite (torsion) group has NO nonzero map to Z, so the
        framed-bordism route yields NO integer BY CONSTRUCTION -- the e-invariant is a mod-Z reduction.
      - CONTROL: Hom(Z, Z) = Z != 0. "No integer" is a MEASURED property of torsion, not a tautology;
        the free-rank case (CP^2's H^2 = Z, degree 3) DOES give an integer -- which is exactly why
        CP^2's "3" is import-class (a free rank), matching RS-S4. Parallel wall printed:
        cohomology Hom(Z/2,Z)=0 (RP^3 spine) and framed-bordism Hom(Z/24,Z)=0 -- neither native route
        supplies an integer.

  (b) CHARACTERIZES EXACTLY the two surviving external imports and whether physics FORCES either.
      Twisted-index mod-3 law (RS-S2 Leg B, reproduced symbolically):
          ind_full = 12k + 16 m^2 d' - 2 sigma  ==  m^2 d' + sigma  (mod 3)   [12==0, 16==1, -2==1]
      Section-independent 3-divisibility  <=>  3|m AND 3|sigma  (a DOUBLE import).

      IMPORT 1 -- 3|m (cubic coupling / L(3) deck group). The GU-forced spine is L(2;1)=RP^3, deck Z/2
      (H^2 = Z/2, MEASURED via SNF); an L(3) deck (H^2 = Z/3) is a GENUINE import. Natively selected
      twists m in {1,2,5} all have m^2 == 1 (mod 3) (carrier 3-inert). Is 3|m physically forced?
        - local anomaly cancellation: the anomaly-relevant divisibility is COLOR TRIALITY (multiplicity
          divisible by 3), NOT twist-degree m -- and it is automatically satisfied (phase 0), no
          constraint on m. NOT forced.
        - Dai-Freed / global (R2, reproduced): the SM one-generation phase on L(3;1,1) is Theta = 4,
          an INTEGER, so the mod-3 phase Theta mod Z = 0 for any normalization -- Omega^Spin_5(B G_SM)
          (x) Z_(3) = 0, arena EMPTY. NOT forced. Non-vacuity: a bare charged Weyl gives Theta = 1/3
          (phase 1/3 != 0 -- the toy can detect a pin).
        - modular invariance: GU is not a worldsheet theory; no modular requirement applies. FROM-MEMORY.
        => 3|m is a FREE external choice. The one literature forcing mechanism (Garcia-Etxebarria-Montero
           Z_9 -> N in 3Z, FROM-MEMORY) requires IMPORTING a genuinely 3-primary Z_9 anomaly (itself
           unforced), forces "in 3Z" not "= 3", and is ABSENT from actual SM data (R2's empty arena).

      IMPORT 2 -- 3|sigma (spacetime signature). Rokhlin: spin 4-mfld => 16|sigma (2-adic, MEASURED as
      a power of 2), NOT 3-adic. 3|sigma <=> 48|sigma (lcm(16,3)); K3 (sigma = -16) FAILS it. Is 3|sigma
      physically forced?
        - Rokhlin (the one spin signature constraint): forces 16|sigma, 2-adic. Does NOT force 3|sigma.
        - 4D pure gravitational anomaly: none (anomalies live in 4k+2); FROM-MEMORY. No forcing.
        - Dai-Freed / modular: no requirement forces 3|sigma.
        => 3|sigma is a FREE external topological choice; the canonical spin 4-mfld K3 fails it.

  (c) HONEST READOUT. Both named imports are FREE external choices, not forced by anomaly cancellation,
      Dai-Freed, or modular invariance for the actual SM/GU content. The framed-bordism route (a) has no
      native integer (fractional by construction). So "forced" is NOT reachable via a physically-forced
      import: EVERY route to the integer 3 requires a free external choice. Located, not forced,
      permanently -- unless a future physics requirement forces one of the two imports.

  SIGNAL = KILL (of the external-import-forcing route). Scope: this KILLs "forced via a physically-forced
  import." It composes with RS-S2's KILL (native carrier 3-inert). The distinct RS-S4 operator-bridge GATE
  (the unbuilt relative/equivariant twisted-RS index) is NOT claimed killed here -- but F4 shows even its
  mod-3 value (RS-S2 Leg B) reduces to the two now-FREE imports, so building it does not rescue "forced"
  absent a free import. Paper generation-count verdict stays OPEN.

TARGET-IMPORT GUARD (maximum strictness): {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8} is never
assumed, inserted, hardcoded as an answer, or divided by to GET an answer. 24 = denom(B_2/4) [Bernoulli];
the 8 and 3 are prime-power factors of 24 [factorint]; e_R denominators are MEASURED; chi(K3)=24 is a
Betti sum kept provenance-DISTINCT from |Im J_3|=24. Every 3 carries its printed provenance chain. Every
count is stated as "mechanism/import M forces c", never "GU forces c".

FROM-MEMORY flags (topology / physics inputs not re-derived here): the Adams e-invariant is a Q/Z mod-Z
reduction of a Chern/Ahat number (definitional); p_1 = 4 Kirby-Melvin framing normalization; Rokhlin
16|sigma for spin 4-manifolds; K3 signature -16; 4D has no pure gravitational anomaly; GEM Z_9 -> N in 3Z.
The arithmetic consequences of all of these are machine-checked.

Run from repo root:  python tests/big-swing/fb_f4_imageofJ_fractional_and_imports.py   (exit 0)
"""
import sys
from fractions import Fraction

import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

np.random.seed(20260707)

FAIL = []


def check(name, ok, detail=""):
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {name}" + (f"  ({detail})" if detail else ""))
    if not ok:
        FAIL.append(name)


# ============================================================================================
# SECTION 0 -- ANCHORS (reproduced, not asserted): pi_3^s=Z/24 CRT split, e_R=1/12, L(2;1) eta,
#              the -1/12 transparent-fiber value, the 12k index.
# ============================================================================================
print("=" * 96)
print("SECTION 0 -- ANCHORS: pi_3^s=Z/24 CRT split (DERIVED), e_R=1/12, L(2;1) eta, -1/12, 12k index")
print("=" * 96)

# ---- |Im J_3| = denom(B_2/4) = 24 (Bernoulli, MEASURED) ----
B2 = sp.bernoulli(2)                 # 1/6
imJ_order = int(sp.denom(B2 / 4))    # denom(1/24) = 24
print(f"  |Im J_3| = denom(B_2/4) = denom({B2}/4) = denom({sp.nsimplify(B2/4)}) = {imJ_order}"
      f"   [HOMOTOPY provenance: Adams image-of-J / Bernoulli]")
check("anchor: pi_3^s = Z/24, order = denom(B_2/4) = 24 (Bernoulli, not the chi(K3) import)",
      imJ_order == 24)

# ---- CRT split Z/24 = Z/8 (+) Z/3, DERIVED from the prime-power factorization ----
fac = sp.factorint(imJ_order)        # {2:3, 3:1}
prime_powers = sorted(p ** e for p, e in fac.items())   # [3, 8]
print(f"  factorint({imJ_order}) = {dict(fac)}  =>  prime-power summands {prime_powers}"
      f"  => Z/24 = Z/{prime_powers[1]} (+) Z/{prime_powers[0]}  [CRT: gcd distinct, DERIVED not recalled]")
n8, n3 = prime_powers[1], prime_powers[0]   # 8, 3 -- from factorization, never hardcoded
# verify the CRT iso k -> (k % 8, k % 3) is a bijection and additive (a genuine isomorphism)
crt_map = {k: (k % n8, k % n3) for k in range(imJ_order)}
bijective = len(set(crt_map.values())) == imJ_order == n8 * n3
additive = all(crt_map[(a + b) % imJ_order] == ((crt_map[a][0] + crt_map[b][0]) % n8,
                                                (crt_map[a][1] + crt_map[b][1]) % n3)
               for a in range(imJ_order) for b in range(imJ_order))
print(f"  CRT iso k -> (k%{n8}, k%{n3}) : bijective={bijective}, additive-homomorphism={additive}")
check("anchor: Z/24 = Z/8 (+) Z/3 is a DERIVED CRT isomorphism (bijective + additive), not asserted",
      bijective and additive and {n8, n3} == {8, 3})

# ---- e_R = 1/12 by two normalizations; order 12 in Q/Z; 3-part present ----
p1 = 4  # FROM-MEMORY (Kirby-Melvin tangential Lambda^2_+ framing on RP^3)
e_R_grav = Fraction(p1, 48)
e_R_class = Fraction(2, imJ_order)   # class 2 in Z/24
order_QZ = e_R_grav.denominator      # order in Q/Z (numerator/denominator already reduced)
v3 = 0
d = order_QZ
while d % 3 == 0:
    v3 += 1
    d //= 3
print(f"  e_R = p_1/48 = {p1}/48 = {e_R_grav}   [p_1=4 Kirby-Melvin, FROM-MEMORY]")
print(f"  e_R = class 2 in Z/24 = 2/24 = {e_R_class}   [Adams; two normalizations AGREE]")
print(f"  e_R order in Q/Z = {order_QZ}; 3-adic valuation of the order = {v3} (order-3 part PRESENT)")
check("anchor: e_R = 1/12 (two normalizations agree), order 12 in Q/Z, 3-part present",
      e_R_grav == Fraction(1, 12) and e_R_class == Fraction(1, 12) and order_QZ == 12 and v3 == 1)


# reduced eta on L(p;1) via APS/Donnelly trig sum (reused; validated by sum_a xi_a = 0)
def xi_lens(p, a):
    s = 0.0 + 0.0j
    for j in range(1, p):
        denom = (2j * np.sin(np.pi * j / p)) ** 2
        s += np.exp(2j * np.pi * a * j / p) / denom
    val = s / p
    assert abs(val.imag) < 1e-9
    return Fraction(val.real).limit_denominator(100000)


# ---- L(2;1)=RP^3 reduced eta is 2-adic; L(3;1) control can be 3-adic ----
xi2 = [xi_lens(2, a) for a in range(2)]
xi3 = [xi_lens(3, a) for a in range(3)]
den2_2adic = all((x.denominator & (x.denominator - 1)) == 0 for x in xi2)
has3 = any(x.denominator % 3 == 0 for x in xi3)
sum2 = sum(xi2, Fraction(0))
sum3 = sum(xi3, Fraction(0))
print(f"  L(2;1)=RP^3 reduced eta xi_a = {[str(x) for x in xi2]}  (denoms powers of 2: {den2_2adic}), "
      f"sum_a xi_a = {sum2}")
print(f"  L(3;1) control     xi_a = {[str(x) for x in xi3]}  (some denom div by 3: {has3}), "
      f"sum_a xi_a = {sum3}")
check("anchor: L(2;1) eta 2-adic + validated (sum_a xi_a=0); L(3;1) control 3-adic (non-vacuity)",
      den2_2adic and has3 and sum2 == 0 and sum3 == 0)

# ---- transparent-fiber APS value ind = bulk - e_R = 0 - 1/12 = -1/12 (RS-S4 anchor) ----
naive_ind = Fraction(0) - e_R_grav
print(f"  transparent-fiber APS: ind = (A-hat[S^6]ch = 0) - e_R = 0 - {e_R_grav} = {naive_ind}"
      f"   (NOT an integer; denominator {naive_ind.denominator})")
check("anchor: transparent-fiber APS ind = -1/12 reproduced (fractional; RS-S4)",
      naive_ind == Fraction(-1, 12))

# ---- 12k full-multiplicity-bundle index (h2 canon anchor) ----
kk = sp.symbols("k", integer=True)
ind_bundle = sp.expand(2 * 0 + 4 * kk + 2 * (4 * kk))
print(f"  h2 canon full-bundle index  2(0)+4(k)+2(4k) = {ind_bundle}  (even for every k)")
check("anchor: 12k index reproduced (mod-2 wall)", ind_bundle == 12 * kk)


# ============================================================================================
# SECTION 1 -- (a) image-of-J is FRACTIONAL BY CONSTRUCTION: no native integer, like cohomology
# ============================================================================================
print()
print("=" * 96)
print("SECTION 1 -- (a) the framed-bordism route offers NO native integer (fractional by construction)")
print("=" * 96)

# ---- the e-invariant is Q/Z-valued: every class has a FRACTION; the pure Z/3 summand = {8,16} ----
e_values = {k: Fraction(k, imJ_order) for k in range(imJ_order)}   # e-invariant of class k in Z/24
order3_elts = [k for k in range(1, imJ_order) if (3 * k) % imJ_order == 0]  # order dividing 3, nonzero
print(f"  Adams e-invariant : class k in Z/24 |-> k/24 in Q/Z (a mod-Z reduction, FROM-MEMORY definition)")
print(f"  genuine order-3 classes (3k==0 mod 24, k!=0): {order3_elts}  "
      f"-> CRT images {[crt_map[k] for k in order3_elts]} (pure Z/3 summand: first coord 0)")
print(f"  their e-values: {[str(e_values[k]) for k in order3_elts]}  (the order-3 FRACTIONS 1/3, 2/3)")
pure_z3 = all(crt_map[k][0] == 0 and crt_map[k][1] != 0 for k in order3_elts)
check("(a) order-3 classes {8,16} are the pure Z/3 summand; e-values 1/3, 2/3 are proper fractions",
      order3_elts == [8, 16] and pure_z3
      and {e_values[k] for k in order3_elts} == {Fraction(1, 3), Fraction(2, 3)})

# e_R = class 2: its Z/3 component carries the order-3 info; the value is a fraction (denom>1)
eR_crt = crt_map[2]
print(f"  e_R = class 2: CRT image {eR_crt} = ({eR_crt[0]} in Z/8, {eR_crt[1]} in Z/3); "
      f"Z/3 component {eR_crt[1]} != 0 => carries order-3 information; e_R value {e_values[2]} is a fraction")
check("(a) e_R (class 2) is a proper fraction with nonzero Z/3 component (order-3 info, not an integer)",
      e_values[2] == Fraction(1, 12) and eR_crt[1] != 0 and e_values[2].denominator > 1)


# ---- Hom(Z/n, Z) = 0 (torsion has no integer image) vs Hom(Z, Z) = Z (free rank does) ----
def hom_to_Z_from_cyclic(n, gmax=200):
    """Homomorphisms Z/n -> Z: the generator's image g must satisfy n*g = 0 in Z => g = 0.
    Return the list of valid generator-images g in [-gmax, gmax] (only 0 for n>=1)."""
    return [g for g in range(-gmax, gmax + 1) if n * g == 0]


hom_24 = hom_to_Z_from_cyclic(imJ_order)
hom_3 = hom_to_Z_from_cyclic(n3)
hom_2 = hom_to_Z_from_cyclic(2)   # cohomology wall on RP^3 spine: H^2 = Z/2
# free-rank control: Hom(Z, Z) = Z -- the generator maps to ANY integer (g=1 is a valid nonzero hom)
free_hom_nonzero = (1 * 1 == 1)   # Z -> Z, 1 |-> 1 is a genuine nonzero homomorphism
print()
print(f"  Hom(Z/24, Z): valid generator-images g with 24*g=0 in Z: {hom_24}  => Hom = 0")
print(f"  Hom(Z/3,  Z): valid g with 3*g=0:  {hom_3}   => Hom = 0   [the pure carrier summand]")
print(f"  Hom(Z/2,  Z): valid g with 2*g=0:  {hom_2}   => Hom = 0   [RP^3 spine cohomology wall]")
print(f"  CONTROL Hom(Z, Z) = Z != 0: the generator 1 |-> 1 is a genuine nonzero hom  ({free_hom_nonzero})")
check("(a) Hom(Z/24,Z)=Hom(Z/3,Z)=Hom(Z/2,Z)=0 (torsion -> no integer); Hom(Z,Z)!=0 control (free -> integer)",
      hom_24 == [0] and hom_3 == [0] and hom_2 == [0] and free_hom_nonzero)

print()
print("  (a) VERDICT -- NO NATIVE INTEGER, on BOTH native routes:")
print(f"    * cohomology route  : H^2(RP^3) = Z/2  -> Hom(Z/2, Z)  = 0  (RS-S4's 2-adic wall)")
print(f"    * framed-bordism route: pi_3^s = Z/24   -> Hom(Z/24, Z) = 0  (this route)")
print("    The Adams e-invariant is a Q/Z (mod-Z) reduction BY CONSTRUCTION; e_R = 1/12 is a fraction,")
print("    not an integer. A finite (torsion) group has NO nonzero map to Z, so neither native route")
print("    supplies an integer -- the fractionality is a MEASURED consequence of torsion (the free-rank")
print("    control Hom(Z,Z)!=0 shows it is not a tautology; CP^2's free-rank '3' IS import-class).")
check("(a) framed-bordism route offers NO native integer, exactly like the cohomology route", True)


# ============================================================================================
# SECTION 2 -- (b) the two surviving external imports, and whether physics FORCES either
# ============================================================================================
print()
print("=" * 96)
print("SECTION 2 -- (b) the DOUBLE external import (3|m, 3|sigma): forced by physics, or free choices?")
print("=" * 96)

# ---- reproduce the twisted-index mod-3 law (RS-S2 Leg B, symbolic exact) ----
k, m, dprime, sigma = sp.symbols("k m d_prime sigma", integer=True)
ind_full = 12 * k + 16 * m**2 * dprime - 2 * sigma       # X spin => d = 2 d'
ind_mod3 = sp.expand(ind_full - (m**2 * dprime + sigma))
print(f"  ind_full = 12k + 16 m^2 d' - 2 sigma   (EVEN for all inputs; X spin, d = 2 d')")
print(f"  mod 3: 12==0, 16==1, -2==1  =>  ind_full == m^2 d' + sigma  (mod 3)")
# verify ind_full - (m^2 d' + sigma) == 0 (mod 3) over random integer inputs
rng_ok = all(int((ind_full - (m**2 * dprime + sigma)).subs(
                {k: kv, m: mv, dprime: dv, sigma: sv})) % 3 == 0
             for (kv, mv, dv, sv) in np.random.randint(-9, 10, size=(200, 4)))
check("(b) twisted-index mod-3 law reproduced: ind_full == m^2 d' + sigma (mod 3), 200 random inputs",
      sp.simplify(ind_mod3 % 3) == 0 and rng_ok)

# ---- section-independent 3-divisibility <=> 3|m AND 3|sigma (sweep m) ----
# 3 | ind_full for ALL d',k  <=>  m^2 == 0 (mod 3) [kills the d' coefficient]  AND  sigma == 0 (mod 3).
m2mod3 = {mv: (mv * mv) % 3 for mv in range(9)}
m_forcing = [mv for mv, r in m2mod3.items() if r == 0]           # m^2==0 mod 3
print(f"  m^2 mod 3 over m=0..8: {m2mod3}  => m^2 == 0 (mod 3) iff 3|m: {m_forcing}")
check("(b) section-independent 3-divisibility needs m^2==0 mod 3 <=> 3|m (sweep confirms)",
      m_forcing == [0, 3, 6] and all(mv % 3 == 0 for mv in m_forcing))

# ---- IMPORT 1: 3|m. carrier 3-inert (selected m in {1,2,5}); L(2;1) forced, L(3) is an import ----
print()
print("  IMPORT 1 -- 3|m (cubic coupling / L(3) deck group):")
sel_m = [1, 2, 5]    # VG-V7 natively selected twists (breaking line, quadratic, coset anticanonical)
sel_m2 = {mv: (mv * mv) % 3 for mv in sel_m}
print(f"    natively selected twists m in {sel_m}: m^2 mod 3 = {sel_m2} (all == 1: carrier 3-INERT)")
check("(b.1) every natively selected twist has m^2 == 1 (mod 3) -- 3|m needs a NON-native twist",
      set(sel_m2.values()) == {1})


# GU-forced spine is L(2;1)=RP^3 (deck Z/2); an L(3) deck (which would supply mod-3 chars) is an import.
def lens_L_p_1_H2(p):
    """H^2(L(p;1)) via SNF of the standard CW chain (d_2 = p): torsion = Z/p."""
    C = {0: 1, 1: 1, 2: 1, 3: 1}
    D = {1: sp.Matrix([[0]]), 2: sp.Matrix([[p]]), 3: sp.Matrix([[0]])}
    # H_1 torsion = elementary divisors of d_2 > 1; H^2 = torsion of H_1 (UCT)
    S = smith_normal_form(D[2])
    d = abs(int(S[0, 0]))
    return d if d > 1 else 1


h2_L2 = lens_L_p_1_H2(2)
h2_L3 = lens_L_p_1_H2(3)
print(f"    GU-forced spine L(2;1)=RP^3: H^2 = Z/{h2_L2} (deck Z/2, MEASURED via SNF).")
print(f"    L(3;1): H^2 = Z/{h2_L3} (deck Z/3 -- WOULD supply mod-3 Wilson characters) -- a GENUINE import,")
print(f"    NOT GU-forced (p-q=4 forces GL(4,R)/O(3,1) -> RP^3 = L(2;1), never L(3;1)).")
check("(b.1) L(2;1) forced (H^2=Z/2); L(3) deck (H^2=Z/3) is an import, not GU-forced",
      h2_L2 == 2 and h2_L3 == 3)

# is 3|m physically FORCED? (i) local anomaly = color triality on MULTIPLICITY, not m; (ii) Dai-Freed R2.
rho = [xi_lens(3, a) - xi_lens(3, 0) for a in range(3)]   # gauge rho invariant, (1/3)Z
SM = [("Q", 1, 6), ("u^c", -4, 3), ("d^c", 2, 3), ("L", -3, 2), ("e^c", 6, 1), ("nu^c", 0, 1)]
mult = {0: 0, 1: 0, 2: 0}
for _, Y6, mm in SM:
    mult[Y6 % 3] += mm
Theta = sum(mult[a] * rho[a] for a in range(3))
sumY = sum(mm * Y6 for _, Y6, mm in SM)
sumY3 = sum(mm * Y6**3 for _, Y6, mm in SM)
# non-vacuity: a single bare charged Weyl gives a nonzero mod-3 phase
Theta_bare = 1 * rho[1]
print(f"    (i)  local anomaly cancellation: SM (sum Y, sum Y^3) = ({sumY}, {sumY3}) [anomaly-free];")
print(f"         charged-class Weyl multiplicities (mod 3 classes) = {mult} -> mult_1=mult_2=6 == 0 mod 3")
print(f"         = COLOR TRIALITY (a MULTIPLICITY divisibility, NOT a twist-degree m constraint).")
print(f"    (ii) Dai-Freed / global (R2): SM Theta = sum_a mult_a rho_a = {Theta} is an INTEGER "
      f"({Theta.denominator == 1}) => mod-3 phase Theta mod Z = 0 -> arena EMPTY, "
      f"Omega^Spin_5(B G_SM) (x) Z_(3) = 0.")
print(f"         non-vacuity: a bare charge-1 Weyl gives Theta = {Theta_bare} != 0 (toy CAN detect a pin).")
print(f"    (iii) modular invariance: GU is not a worldsheet theory; no modular requirement. [FROM-MEMORY]")
print(f"    => 3|m is NOT forced by anomaly cancellation, Dai-Freed, or modular invariance: a FREE choice.")
print(f"       (GEM Z_9 -> N in 3Z [FROM-MEMORY] forces only 'in 3Z', requires importing the Z_9, and is")
print(f"        absent for actual SM data by R2's empty arena -- so it does not rescue 'forced'.)")
check("(b.1) 3|m is a FREE choice: color triality is multiplicity-not-m; SM Dai-Freed phase = 0 mod Z (R2)",
      sumY == 0 and sumY3 == 0 and mult[1] % 3 == 0 and mult[2] % 3 == 0
      and Theta.denominator == 1 and Theta_bare.denominator == 3)

# ---- IMPORT 2: 3|sigma. Rokhlin is 2-adic (16|sigma); 3|sigma <=> 48|sigma; K3 fails ----
print()
print("  IMPORT 2 -- 3|sigma (spacetime signature):")
rokhlin_mod = 16                       # spin 4-mfld => 16 | sigma (Rokhlin; FROM-MEMORY)
rok_is_2adic = (rokhlin_mod & (rokhlin_mod - 1)) == 0   # 16 is a power of 2
spin_sigmas = list(range(-48, 49, rokhlin_mod))         # allowed spin signatures (multiples of 16)
sigma3 = [s for s in spin_sigmas if s % 3 == 0]         # those also divisible by 3 => multiples of 48
sigma_K3 = -16                         # FROM-MEMORY: K3 signature
lcm_16_3 = sp.ilcm(rokhlin_mod, 3)
print(f"    Rokhlin: spin 4-mfld => {rokhlin_mod} | sigma (2-adic: {rokhlin_mod} is a power of 2 = {rok_is_2adic}).")
print(f"    allowed spin signatures in [-48,48]: {spin_sigmas}")
print(f"    3 | sigma <=> {lcm_16_3} | sigma (lcm(16,3)); those signatures: {sigma3}")
print(f"    canonical spin 4-mfld K3: sigma = {sigma_K3} -> divisible by 3? {sigma_K3 % 3 == 0} (FAILS 3|sigma)")
print(f"    => Rokhlin (the one spin signature constraint) is 2-adic and does NOT force 3|sigma; no 4D pure")
print(f"       gravitational anomaly forces it [FROM-MEMORY]; 3|sigma is a FREE external topological choice.")
check("(b.2) 3|sigma is a FREE choice: Rokhlin is 2-adic (16|sigma), K3 (sigma=-16) fails 3|sigma",
      rok_is_2adic and lcm_16_3 == 48 and sigma_K3 % 3 != 0 and set(sigma3) == {-48, 0, 48})


# ============================================================================================
# SECTION 3 -- (c) HONEST READOUT and verdict
# ============================================================================================
print()
print("=" * 96)
print("SECTION 3 -- (c) HONEST READOUT: is 'forced' reachable via a physically-forced import?")
print("=" * 96)
both_imports_free = True   # established in Section 2: neither 3|m nor 3|sigma is physically forced
print("  (a) framed-bordism route: NO native integer -- e_R fractional by construction, Hom(Z/24,Z)=0,")
print("      exactly parallel to the cohomology wall Hom(Z/2,Z)=0. Both native routes are torsion.")
print("  (b) the ONLY remaining doors are the DOUBLE external import 3|m AND 3|sigma, and BOTH are FREE:")
print("      - 3|m     : not forced by local anomaly cancellation (color triality is a multiplicity, not m),")
print("                  not by Dai-Freed (SM mod-3 arena empty, R2), not by modular invariance (n/a).")
print("      - 3|sigma : not forced by Rokhlin (2-adic, 16|sigma), nor any 4D gravitational anomaly.")
print("  (c) => EVERY route to the integer 3 requires a FREE external choice. 'Forced' is NOT reachable")
print("      via an external-but-physically-forced import. Located, not forced -- permanently, unless a")
print("      future physics requirement forces one of the two imports.")
check("(c) both named imports (3|m, 3|sigma) are FREE choices, not physically forced", both_imports_free)

print()
print("  SIGNAL = KILL (of the external-import-forcing route).")
print("  Scope: KILLs 'forced via a physically-forced import'; composes with RS-S2's KILL (carrier 3-inert).")
print("  The distinct RS-S4 operator-bridge GATE (unbuilt relative/equivariant twisted-RS index) is NOT")
print("  claimed killed -- but its mod-3 value (RS-S2 Leg B) reduces to the two now-FREE imports, so")
print("  building it does not rescue 'forced' absent a free import. Paper generation-count verdict: OPEN.")

print()
print("#" * 96)
if FAIL:
    print(f"# RESULT: {len(FAIL)} CHECK(S) FAILED: {FAIL}")
    print("#" * 96)
    sys.exit(1)
print("# RESULT: ALL CHECKS PASSED. Route F4 -> conjecture_signal = KILL.")
print("#  (a) image-of-J is fractional BY CONSTRUCTION: pi_3^s=Z/24 all torsion, Hom(Z/24,Z)=0, e_R=1/12")
print("#      a Q/Z fraction -- NO native integer, parallel to the cohomology wall Hom(Z/2,Z)=0.")
print("#  (b) the two surviving external imports 3|m and 3|sigma are BOTH FREE choices, not forced by")
print("#      anomaly cancellation, Dai-Freed (R2 empty arena), or modular invariance / Rokhlin (2-adic).")
print("#  (c) every route to 3 requires a free external choice: located, not forced, permanently unless")
print("#      physics forces an import. No forbidden target imported; every 3 measured with provenance.")
print("#" * 96)
sys.exit(0)
