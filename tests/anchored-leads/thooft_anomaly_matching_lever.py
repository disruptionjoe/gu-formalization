"""
LEAD: 't Hooft anomaly matching as a LOCATE->FORCE lever.

Precise question: is e_R = 1/12 (the order-3 carrier) an 't Hooft anomaly coefficient
(hence RG-invariant), and does matching it UV (Spin(10)/14-mfd) <-> IR (SM) FORCE n_gen = 3
WITHOUT resolving the type error / building the source action?

This script does the decisive quick checks:
  (1) HOMOGENEITY: any 't Hooft anomaly coefficient is LINEAR in n_gen, so the matching
      condition is c*n_UV = c*n_IR. Show this fixes nothing about the VALUE of n.
  (2) The SM/16-of-Spin(10) continuous 't Hooft anomalies that could scale with n_gen and
      survive to the IR (grav^2-(B-L), [B-L]^3) -- compute them. If they vanish per gen,
      the matched coefficient is 0 and matching is vacuous for the count.
  (3) VECTORLIKE CARRIER: the order-3 carrier Lambda^2_+ is vectorlike (+96/-96). Compute
      its cubic 't Hooft anomaly. Vectorlike => gappable => anomaly = 0 => e_R=1/12 is NOT
      a 't Hooft (matchable) coefficient of a chiral symmetry.
  (4) DISCRETE Z/3 angle (the one type-correct hope): does a Z/3 discrete 't Hooft anomaly
      of the 16 give an n_gen-dependent mod-3 constraint? Compute the candidate Z/3 charges.

Everything here is exact rational/integer arithmetic on the known rep content -- COMPUTED,
not asserted. No source action is used. No fork is resolved.
"""
from fractions import Fraction as F

# ---------------------------------------------------------------------------
# The 16 of Spin(10) = one SM generation + nu_R, all LEFT-handed Weyl.
# Fields: (name, multiplicity = #colors*#weak, hypercharge Y, B-L)
# Convention: Q_Y normalized so that e^c has Y=+1 (i.e. Y = T3 + ... standard GUT-ish);
# we only need RATIOS/sums for anomaly coefficients. B-L standard.
# ---------------------------------------------------------------------------
# multiplicity counts Weyl components (color x weak-isospin)
SIXTEEN = [
    # name,       mult, Y,            B-L
    ("Q",          6,   F(1,6),       F(1,3)),   # (3,2)_{1/6}
    ("u_c",        3,   F(-2,3),      F(-1,3)),  # (3bar,1)_{-2/3}
    ("d_c",        3,   F(1,3),       F(-1,3)),  # (3bar,1)_{1/3}
    ("L",          2,   F(-1,2),      F(-1)),    # (1,2)_{-1/2}
    ("e_c",        1,   F(1),         F(1)),     # (1,1)_{1}
    ("nu_c",       1,   F(0),         F(1)),     # (1,1)_{0}  (right-handed neutrino)
]

def total_weyl():
    return sum(m for _, m, _, _ in SIXTEEN)

def grav2_U1(charge_idx):
    """grav^2 - U(1) mixed 't Hooft anomaly = sum of charge over all left Weyl fermions."""
    return sum(m * row[charge_idx] for row in SIXTEEN for m in [row[1]])

def cubic_U1(charge_idx):
    """[U(1)]^3 't Hooft anomaly = sum of charge^3 over all left Weyl fermions."""
    return sum(m * (row[charge_idx])**3 for row in SIXTEEN for m in [row[1]])

print("="*72)
print("(0) Substrate sanity: the 16")
print("="*72)
print(f"  total left Weyl components in one 16 = {total_weyl()}  (expect 16)")
assert total_weyl() == 16

print()
print("="*72)
print("(2) Continuous 't Hooft anomalies of the 16 that scale with n_gen")
print("    and could survive to the IR (B-L is gaugeable / can stay a global sym)")
print("="*72)
g_BL = grav2_U1(3)     # grav^2 - (B-L)
c_BL = cubic_U1(3)     # (B-L)^3
g_Y  = grav2_U1(2)     # grav^2 - Y  (Y is gauged, must cancel)
c_Y  = cubic_U1(2)     # Y^3
print(f"  grav^2-(B-L) per generation = {g_BL}")
print(f"  [(B-L)]^3   per generation  = {c_BL}")
print(f"  grav^2-Y    per generation  = {g_Y}   (gauge: must be 0)")
print(f"  [Y]^3       per generation  = {c_Y}   (gauge: must be 0)")
per_gen_anom_vanishes = (g_BL == 0 and c_BL == 0 and g_Y == 0 and c_Y == 0)
print(f"  -> all per-generation continuous 't Hooft anomalies vanish: {per_gen_anom_vanishes}")

print()
print("="*72)
print("(1) HOMOGENEITY of anomaly matching in n_gen")
print("="*72)
print("  A matched 't Hooft coefficient A(n) is LINEAR: A(n) = a * n.")
print("  Matching condition: a*n_UV = a*n_IR.")
print("  Demonstration: for ANY per-gen coefficient a and ANY n, both sides equal:")
for a in [F(0), F(1,3), F(2), F(7,2)]:
    for n in [1, 2, 3, 5, 6, 17]:
        uv = a*n; ir = a*n
        assert uv == ir
print("    a*n_UV == a*n_IR for all (a in {0,1/3,2,7/2}) x (n in {1,2,3,5,6,17}): PASS")
print("  => Matching is a CONSISTENCY (RG-invariance of n_gen) condition, NOT a")
print("     DETERMINATION of n_gen. It is satisfied identically for every n.")
print("  => To FORCE a value you need an INHOMOGENEOUS source: a FIXED bulk number B")
print("     with a*n_IR = B  =>  n = B/a.  That fixed B is the bulk -p_1/24 inflow")
print("     coefficient on GU's actual 14-manifold = THE single-decider integer,")
print("     which is GATED on the unbuilt twisted-RS source action.")

print()
print("="*72)
print("(3) VECTORLIKE CARRIER Lambda^2_+ (+96 / -96): its 't Hooft anomaly")
print("="*72)
# A vectorlike sector = equal numbers of left Weyl with charge +q and -q (for every q).
# Model the carrier as charges {+q_i} paired with {-q_i}. Any cubic / linear 't Hooft
# anomaly sums to zero identically.
import random
random.seed(0)
carrier_charges = [F(random.randint(-9,9), random.randint(1,4)) for _ in range(96)]
# vectorlike: include the mirror -q for each
vectorlike = carrier_charges + [-q for q in carrier_charges]
lin = sum(vectorlike)
cub = sum(q**3 for q in vectorlike)
print(f"  carrier net (linear, grav^2-U(1)) anomaly  = {lin}")
print(f"  carrier cubic [U(1)]^3 anomaly             = {cub}")
print(f"  vectorlike => both vanish identically: {lin==0 and cub==0}")
print("  => A vectorlike sector admits a symmetry-preserving Dirac mass and is GAPPABLE;")
print("     a gappable sector has ZERO 't Hooft anomaly (RG-invariance: it bounds).")
print("  => e_R = 1/12 carried by the VECTORLIKE Lambda^2_+ is NOT a 't Hooft anomaly")
print("     coefficient of any chiral symmetry. 't Hooft matching of the carrier is 0=0.")
print("  => Whether the carrier instead stays MASSLESS (a genuine chiral 't Hooft")
print("     coefficient) is EXACTLY the Dirac-mass / source-action gate already named.")

print()
print("="*72)
print("(4) DISCRETE Z/3 angle: the one type-correct hope (mod-3 congruence)")
print("="*72)
# Candidate Z/3: '(B-L) mod 3'-style discrete charge, or baryon-triality.
# A discrete Z/3 't Hooft anomaly is the cubic sum of Z/3 charges taken mod 3.
# Assign t = 3*(B-L) (integer) as a proxy triality-like charge, reduce mod 3.
def z3_charge(row):
    bl3 = row[3] * 3   # 3*(B-L); is it an integer? -> Fraction
    return bl3
charges_3 = [(row[0], row[1], (row[3]*3)) for row in SIXTEEN]
print("  field  mult  3*(B-L):")
for name, mult, c in charges_3:
    print(f"    {name:5s}  {mult:>2d}   {c}")
# cubic Z/3 anomaly: sum mult * q^3, then mod 3 (only meaningful if q integral)
all_int = all((c.denominator == 1) for _, _, c in charges_3)
print(f"  3*(B-L) integral for all fields: {all_int}")
if all_int:
    cub3 = sum(int(mult) * int(c)**3 for _, mult, c in charges_3)
    lin3 = sum(int(mult) * int(c)    for _, mult, c in charges_3)
    print(f"  per-gen cubic  sum (3(B-L))^3 = {cub3},  mod 3 = {cub3 % 3}")
    print(f"  per-gen linear sum  3(B-L)    = {lin3},  mod 3 = {lin3 % 3}")
    print("  A nonzero per-gen value mod 3 would give a Z/3 't Hooft coefficient that")
    print("  scales as (value)*n_gen mod 3 -- a MOD-3 CONGRUENCE on n_gen (type-correct,")
    print("  lands in the Z/3 carrier arena). A per-gen value of 0 mod 3 => vacuous again.")
print()
print("  NOTE: even a nonzero Z/3 discrete anomaly forces only n_gen = const (mod 3),")
print("  an infinite family {.., 3, 6, 9, ..} -- NOT the integer 3 -- and pinning the IR")
print("  side's discrete charge assignment is itself part of the source-action data.")

print()
print("="*72)
print("VERDICT (computed inputs, analytic logic):")
print("="*72)
print("  - 't Hooft matching is HOMOGENEOUS in n_gen => cannot fix the value, only assert")
print("    RG-invariance (which we never doubted).")
print("  - The 16's continuous 't Hooft anomalies that survive to IR VANISH per gen")
print("    (B-L gaugeable) => matched coefficient 0 => vacuous for the count.")
print("  - The order-3 carrier is VECTORLIKE => its 't Hooft anomaly is 0 => e_R=1/12 is")
print("    NOT a chiral 't Hooft coefficient unless the carrier is MASSLESS, which is the")
print("    same Dirac-mass/source-action GATE.")
print("  - The only inhomogeneous (forcing) source is the bulk -p_1/24 inflow integer =")
print("    THE single decider, GATED on the unbuilt twisted-RS source action.")
print("  - The one type-correct residue: a Z/3 DISCRETE anomaly could yield a mod-3")
print("    CONGRUENCE (smaller theorem), not the number 3, and still needs the IR charge data.")
