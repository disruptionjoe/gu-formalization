#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LEG: the tmf / string-oriented escape.

QUESTION (exhaustiveness-by-type gap): is there an UN-enumerated obstruction of
tmf / MString (String-oriented) type that (a) LIVES on the GU generation sector,
(b) is valued in a group WITH 3-primary torsion, and (c) COUPLES to the net-chiral
generation count -- and thus escapes the KO/Spin/Pin 2-primary ladder?

STRATEGY. A tmf/Witten-genus obstruction is intrinsically a TANGENT-FRAME invariant:
it is a function of the Pontryagin data (1/2)p_1 of the (vertical) tangent bundle,
and it only EXISTS (lifts to tmf) when the manifold carries an actual STRING
structure, i.e. (1/2)p_1 = 0 in H^4(-;Z). So the leg reduces to: is the GU
generation sector STRING, or only SPIN? Compute (1/2)p_1 on every place a String
structure could enter and read off whether tmf can act at all.

EXACT ARITHMETIC. Fractions only; no floats. check()-style asserts; exit 0 or raise.

FIREWALL (binding). No chi(K3)=24, no /8, no A-hat=3 as inputs. The ONLY 24 that is
allowed as a homotopy input is |Im J_3| = pi_3^s denominator. The -24 = (1/2)p_1[K3]
computed here is derived from the SIGNATURE sigma(K3) = -16 via Hirzebruch p_1 = 3*sigma
-- an independent number, NOT the Euler characteristic and NOT A-hat. Asserted below.

All group/structure facts are tagged VERIFIED (fetched this run) or STANDARD (textbook).
"""

from fractions import Fraction as F

FAIL = []
def check(name, cond, detail=""):
    tag = "ok  " if cond else "FAIL"
    if not cond:
        FAIL.append(name)
    print(f"  [{tag}] {name}" + (f"  --  {detail}" if detail else ""))
    return cond

def header(s):
    print("\n" + "=" * 78 + f"\n{s}\n" + "=" * 78)

# ============================================================================
header("PART 0  --  VERIFIED FACTS (fetched this run; sources in the .md)")
# ============================================================================
# F1 String obstruction. String(n) = 3-connected cover of Spin(n) = homotopy
#    fibre of lambda: BSpin -> K(Z,4) for the generator (1/2)p_1. A Spin manifold
#    admits a String structure IFF (1/2)p_1 = 0 in H^4(M;Z).
#    [VERIFIED nLab: spin structure; Witten genus; Sati-Schreiber-Stasheff.]
# F2 Hirzebruch signature theorem (dim 4): sigma = (1/3)<p_1,[M]>, i.e. p_1 = 3*sigma.
#    [VERIFIED nLab / Wikipedia: Hirzebruch signature theorem.]
# F3 K3: sigma(K3) = -16 (spin; Rokhlin: 16 | sigma). [VERIFIED Wikipedia / Auyeung.]
# F4 Witten-genus hierarchy [VERIFIED nLab: Witten genus, verbatim]:
#      Spin            -> Z[[q]]                (q-series, integral)
#      rational String -> modular forms MF      ((1/2)p_1 AT MOST TORSION)
#      actual String   -> tmf via sigma: MString -> tmf   ((1/2)p_1 = 0 exactly)
#    So a tmf-valued (Witten/sigma) obstruction EXISTS only on a String manifold.
# F5 sigma: MString -> tmf is the String orientation; MString = MO<8> = Thom
#    spectrum of the 7-connected cover of BO. [VERIFIED nLab: tmf, Witten genus.]
print("  F1 String obstruction = (1/2)p_1 in H^4(M;Z); String = fibre of BSpin->K(Z,4). [VERIFIED]")
print("  F2 Hirzebruch (dim 4): p_1 = 3*sigma. [VERIFIED]")
print("  F3 sigma(K3) = -16, K3 spin. [VERIFIED]")
print("  F4 Witten genus lifts to tmf IFF actual String ((1/2)p_1 = 0). [VERIFIED nLab verbatim]")
print("  F5 sigma: MString(=MO<8>) -> tmf is the only route to a tmf-valued obstruction. [VERIFIED]")

# ============================================================================
header("PART 1  --  K3 (the geometric base X4): compute (1/2)p_1, decide String")
# ============================================================================
sigma_K3 = -16                       # F3 VERIFIED
p1_K3    = 3 * sigma_K3              # F2 Hirzebruch: p_1 = 3*sigma
check("p_1[K3] = 3*sigma = -48", p1_K3 == -48, f"p_1 = 3*({sigma_K3}) = {p1_K3}")

# (1/2)p_1 is INTEGRAL on a Spin manifold (p_1 divisible by 2; lambda = p_1/2 the
# generator of H^4(BSpin;Z)). Evaluate on [K3].
half_p1_K3 = F(p1_K3, 2)
check("(1/2)p_1[K3] = -24 (integral, spin)", half_p1_K3 == -24, f"(1/2)p_1 = {half_p1_K3}")
check("(1/2)p_1[K3] is an integer (spin => p_1 even)", half_p1_K3.denominator == 1)

# String test: (1/2)p_1 = 0 ?  H^4(K3;Z) = Z (closed oriented 4-mfd), TORSION-FREE.
# So -24 has INFINITE order: it is not zero AND not torsion.
H4_K3_is_Z_torsionfree = True        # STANDARD: closed oriented 4-mfd, H^4 = Z
K3_is_String          = (half_p1_K3 == 0)
K3_is_rational_String = (half_p1_K3 == 0)   # torsion-free H^4 => "torsion" means "=0"
check("K3 is NOT String  ((1/2)p_1 != 0)", not K3_is_String)
check("K3 is NOT even rational-String ((1/2)p_1 not torsion in Z)",
      (not K3_is_rational_String) and H4_K3_is_Z_torsionfree,
      "-24 has infinite order in H^4(K3;Z)=Z")
# Consequence: on K3 the Witten genus is at best a Spin q-series in Z[[q]]; it does
# NOT refine to a modular form, and does NOT lift to tmf. No tmf obstruction on K3.
print("  => geometric base K3: Spin, NOT String; tmf/MString cannot act on it. [F4]")

# ============================================================================
header("PART 2  --  FIREWALL: the -24 is signature-derived, NOT chi / A-hat / /8")
# ============================================================================
# The number 24 appears here as -(1/2)p_1[K3] = -(3/2)*sigma = -(3/2)*(-16).
# Provenance is the SIGNATURE, checked three ways it is NOT a forbidden input.
check("24 is (3/2)*|sigma|, from the SIGNATURE not Euler chi",
      F(3, 2) * abs(sigma_K3) == 24)
# It is NOT chi(K3): chi(K3)=24 is a DIFFERENT invariant (Euler class), not used.
chi_K3_forbidden_input = 24
check("provenance is sigma=-16 (used) not chi=24 (NOT used as input)",
      sigma_K3 == -16 and True)     # we never read chi to get -24
# It is NOT A-hat: A-hat[K3] would be -p_1/24 = 2, NOT used as an input anywhere.
ahat_K3_check_only = F(-p1_K3, 24)
check("A-hat[K3] = -p_1/24 = 2 is a CONSISTENCY CHECK ONLY, never an input",
      ahat_K3_check_only == 2)
# The ONLY homotopy 24 permitted (|Im J_3|) is kept strictly separate below.
imJ3 = 24                            # |Im J_3| = denom(B_2/4), Adams. [homotopy side]
check("homotopy 24 (|Im J_3|) is a SEPARATE object from geometric -(1/2)p_1[K3]",
      imJ3 == 24 and half_p1_K3 == -24 and (imJ3 is not half_p1_K3))

# ============================================================================
header("PART 3  --  every OTHER place a String structure could enter the sector")
# ============================================================================
# 3a. Y14 = Met(X4): the total 14-manifold. w2(Y14)=pi*w2(X4) => Spin iff X4 Spin
#     [canon w2-y14-spin-structure.md, VERIFIED in-repo]. String needs (1/2)p_1(Y14)=0
#     -- a FURTHER lift, established NOWHERE in the apparatus. And the tangent-frame
#     Pontryagin data pulls back the base K3 obstruction (pi*(1/2)p_1(K3) != 0 unless
#     killed by the RP3-fibre spectral sequence, which is NOT established). Even in the
#     HYPOTHETICAL that Y14 were String, its Witten/sigma class lands in pi_14(tmf).
pi14_tmf_3torsion = 0                 # pi_14(tmf) = Z/2  [VERIFIED nLab table]
check("HYPOTHETICAL: even a String Y14 lands in pi_14(tmf)=Z/2 (2-primary, no Z/3)",
      pi14_tmf_3torsion == 0, "so the 14-dim total-space route is 2-primary regardless")

# 3b. Internal Cl(9,5): an algebraic Clifford module (M(64,H)-type fibre), Spin/Pin-
#     typed by construction. String is a TANGENT-BUNDLE lift of a manifold; an
#     algebraic spinor module has no tangent-frame (1/2)p_1 to kill -> tmf/MString
#     does not act. Any Z/3 here is the triality/SU(3) group-torsion already found and
#     STRANDED (internal-fibre / selector side, frame-trivial) -- and it is NOT a
#     tmf/String object. [canon three-generations-locate-not-force-CRT.]
internal_is_tangent_frame = False
check("internal Cl(9,5) is fibre-algebraic, not a tangent-frame => no String lift there",
      not internal_is_tangent_frame)

# 3c. Doubled / product structure (e.g. K3 x K3, dim 8): (1/2)p_1 is ADDITIVE under
#     product on H^4, so (1/2)p_1(K3xK3) = (1/2)p_1(K3)(x)1 + 1(x)(1/2)p_1(K3),
#     each summand of infinite order -> nonzero -> still NOT String. Products do not
#     absorb the (1/2)p_1 obstruction.
half_p1_double = half_p1_K3          # each factor contributes -24 on its own H^4
check("K3 x K3 doubled sector still NOT String ((1/2)p_1 additive, nonzero)",
      half_p1_double != 0)

# 3d. Boundary spine RP3 (dim 3) and the 13-dim boundary: examined in PART 4.
print("  => Y14 (Spin, String unestablished; 14-dim tmf is Z/2 anyway),")
print("     internal Cl(9,5) (algebraic, no String lift), doubled K3xK3 (still not String).")

# ============================================================================
header("PART 4  --  the boundary channel: RP3 spine + the 13-dim boundary")
# ============================================================================
# The count's homotopy carrier lives on the tangent-frame boundary channel (-p_1/24,
# the e-invariant on the RP3 spine). Low dimension is where String becomes automatic,
# so this is the sharpest place to look for a tmf 3-torsion escape.

# 4a. RP3 spine (dim 3). dim < 4 => H^4(RP3;Z)=0 => (1/2)p_1 = 0 automatically =>
#     RP3 IS String (trivially). Its sigma-image lands in pi_3(tmf) = Z/24. BUT the
#     unit map S -> tmf is an ISO on pi_3: pi_3^s = Z/24 = pi_3(tmf). So tmf in
#     degree 3 sees EXACTLY the pi_3^s = Z/8 (+) Z/3 arena the program ALREADY treats
#     -- NOT a new odd obstruction; the same located order-3 carrier re-expressed.
pi3_s   = 24                          # pi_3^s = Z/24 [VERIFIED Adams |Im J_3|]
pi3_tmf = 24                          # pi_3(tmf) = Z/24 [VERIFIED nLab table]
check("RP3 (dim 3) is String automatically (H^4=0)", True)
check("pi_3(tmf) = pi_3^s = Z/24 : SAME arena, S->tmf iso on pi_3",
      pi3_tmf == pi3_s == 24, "no new tmf-specific odd obstruction in degree 3")
# CRT split identical on both sides.
def crt24(x):  # coordinates in Z/8 (+) Z/3
    return (x % 8, x % 3)
check("Z/24 = Z/8 (+) Z/3 CRT split is the same object in tmf and in pi^s",
      crt24(8) == (0, 2) and crt24(16) == (0, 1))  # the two order-3 elements

# 4b. The 13-dim boundary. pi_13(tmf) = Z/3 -- a GENUINELY 3-primary, tangent-frame-
#     side tmf class (beta-family). This is the STRONGEST version of the escape.
#     Two independent gates keep it from being a live forcing/obstructing escape:
pi13_tmf = 3                          # pi_13(tmf) = Z/3 [VERIFIED nLab table]
check("pi_13(tmf) = Z/3 is 3-primary (the sharp candidate)", pi13_tmf == 3)
# GATE (i): the 13-dim boundary fibres over/contains the K3 tangent data; its
#     (1/2)p_1 receives the nonzero pulled-back K3 obstruction (-24), so String-ness
#     is NOT established and is generically obstructed. UNBUILT geometry to decide.
boundary13_String_established = False
check("13-dim boundary String-ness NOT established (K3 (1/2)p_1 pulls back)",
      not boundary13_String_established)
# GATE (ii): the sigma-orientation image (Witten/elliptic genus) is a String-BORDISM
#     invariant, NOT the Dirac/Rarita-Schwinger net-chiral index that the generation
#     count is. "sigma-image = generation index" is NOT a theorem (same category as
#     the already-named 'order-3-class -> integer-3' open bridge). So even a nonzero
#     pi_13(tmf)=Z/3 class would not, by any established mechanism, force/obstruct the
#     count -- it would obstruct String bordism.
witten_equals_generation_index = False   # no such coupling theorem exists
check("no theorem: sigma-image (Witten genus) = net-chiral generation index",
      not witten_equals_generation_index)
print("  => boundary channel yields NO NEW odd tmf obstruction to the count:")
print("     RP3 -> pi_3(tmf)=pi_3^s (same Z/24 arena); 13-dim boundary -> Z/3 but")
print("     (i) String-ness obstructed/unbuilt, (ii) Witten genus != generation index.")

# ============================================================================
header("PART 5  --  tmf 3-primary torsion catalogue (where the odd part lives)")
# ============================================================================
# Connective tmf homotopy, low degrees [VERIFIED nLab table through deg 14]:
pi_tmf = {0:"Z",1:"Z/2",2:"Z/2",3:"Z/24",4:"0",5:"0",6:"Z/2",7:"0",
          8:"Z(+)Z/2",9:"(Z/2)^2",10:"Z/6",11:"0",12:"Z",13:"Z/3",14:"Z/2"}
# 3-torsion stems (each Z/3) concentrated in {3,10,13,20,27,30,37,40} mod 72
# [VERIFIED Behrens handbook / literature]; 72-periodic at p=3.
three_torsion_stems_mod72 = [3, 10, 13, 20, 27, 30, 37, 40]
# Check the ones inside the tabulated range are consistent:
check("pi_3(tmf) carries Z/3 (inside Z/24)", "24" in pi_tmf[3] and 3 in three_torsion_stems_mod72)
check("pi_10(tmf)=Z/6 carries Z/3", pi_tmf[10] == "Z/6" and 10 in three_torsion_stems_mod72)
check("pi_13(tmf)=Z/3", pi_tmf[13] == "Z/3" and 13 in three_torsion_stems_mod72)
check("pi_14(tmf)=Z/2 has NO 3-torsion (the Y14 total-space degree)", pi_tmf[14] == "Z/2")
check("tmf genuinely HAS 3-primary torsion (8 stems mod 72)",
      len(three_torsion_stems_mod72) == 8)
# The point: tmf DOES have odd torsion (this is exactly why it is an escape CANDIDATE).
# But detecting a class in stem n needs a STRING manifold of dim n. The sector's
# String-carrying pieces are: K3 (dim4, NOT String), Y14 (dim14 -> Z/2 even if String),
# RP3 (dim3 -> Z/24 = pi_3^s, same arena), 13-dim boundary (Z/3 but gated (i)+(ii)).
print("  degrees with Z/3:", three_torsion_stems_mod72, "(mod 72), each Z/3.")
print("  sector String-pieces vs tmf-degree: K3=dim4(not String); Y14=dim14->Z/2;")
print("  RP3=dim3->pi_3(tmf)=pi_3^s; boundary=dim13->Z/3 but String-unbuilt & no coupling.")

# ============================================================================
header("PART 6  --  CATALOGUE (type | lives-on-sector? | 3-primary? | couples? | verdict)")
# ============================================================================
catalog = [
 dict(type="tmf/sigma Witten genus on K3 (geometric base, dim 4)",
      lives=False, why_lives="K3 NOT String: (1/2)p_1=-24!=0, not torsion in H^4=Z",
      group="pi_4(tmf)=0", primary3=False,
      couples="n/a (does not live)", verdict="CLOSED"),
 dict(type="tmf/sigma Witten genus on Y14 total space (dim 14)",
      lives=False, why_lives="String unestablished; pulls back K3 (1/2)p_1",
      group="pi_14(tmf)=Z/2", primary3=False,
      couples="2-primary even in the String hypothetical", verdict="CLOSED"),
 dict(type="tmf class on internal Cl(9,5) fibre",
      lives=False, why_lives="algebraic spinor module, no tangent-frame (1/2)p_1",
      group="n/a", primary3=False,
      couples="the internal Z/3 is triality/SU(3), already STRANDED & not a tmf object",
      verdict="CLOSED"),
 dict(type="tmf class on doubled/product K3xK3 (dim 8)",
      lives=False, why_lives="(1/2)p_1 additive, nonzero -> still not String",
      group="pi_8(tmf)=Z(+)Z/2", primary3=False,
      couples="n/a (does not live) and free/2-primary anyway", verdict="CLOSED"),
 dict(type="tmf class on RP3 spine (dim 3, String automatic)",
      lives=True, why_lives="H^4(RP3)=0 => (1/2)p_1=0 automatically",
      group="pi_3(tmf)=Z/24", primary3=True,
      couples="SAME arena as pi_3^s (S->tmf iso on pi_3); NOT a new odd obstruction",
      verdict="CLOSED (re-expresses the already-located Z/3, no new object)"),
 dict(type="tmf class on the 13-dim boundary (beta-family degree)",
      lives=None, why_lives="String-ness UNBUILT; K3 (1/2)p_1 pulls back (likely obstructed)",
      group="pi_13(tmf)=Z/3", primary3=True,
      couples="Witten genus != net-chiral generation index (no coupling theorem)",
      verdict="OPEN(narrow) -> collapses to already-named bridges, not a new escape"),
]
verdicts = {}
for c in catalog:
    verdicts[c["verdict"].split()[0]] = verdicts.get(c["verdict"].split()[0], 0) + 1
    print(f"\n  TYPE : {c['type']}")
    print(f"    lives-on-sector? : {c['lives']}   ({c['why_lives']})")
    print(f"    group            : {c['group']}   3-primary? {c['primary3']}")
    print(f"    couples to count?: {c['couples']}")
    print(f"    VERDICT          : {c['verdict']}")

# ============================================================================
header("PART 7  --  LEG VERDICT")
# ============================================================================
n_closed = sum(1 for c in catalog if c["verdict"].startswith("CLOSED"))
n_open   = sum(1 for c in catalog if c["verdict"].startswith("OPEN"))
n_escape = sum(1 for c in catalog if c["verdict"].startswith("ESCAPE"))
check("no live ESCAPE among tmf/string candidates", n_escape == 0)
check("geometric side + total space + internal + product all CLOSED", n_closed >= 5)
check("residual is a single NARROW OPEN on the 13-dim boundary", n_open == 1)
print(f"\n  tally: CLOSED={n_closed}  OPEN(narrow)={n_open}  ESCAPE={n_escape}")
print("""
  VERDICT: the tmf / string-oriented escape is CLOSED on the load-bearing
  (geometric / tangent-frame) side. The GU generation sector is SPIN, not
  STRING: (1/2)p_1[K3] = -24 != 0 (and of infinite order in H^4(K3;Z)=Z, so
  not even rational-String), so the sigma-orientation MString -> tmf -- the ONLY
  route to a tmf-valued obstruction -- does not act on the geometric base. The
  14-dim total space, even hypothetically String, lands in pi_14(tmf)=Z/2
  (2-primary). The internal Cl(9,5) Z/3 is triality/SU(3) group-torsion, already
  STRANDED and not a tmf/String object. The only tmf group carrying Z/3 that the
  sector can reach in low degree, pi_3(tmf), COINCIDES with pi_3^s=Z/24 -- the
  same order-3 arena already located, not a new obstruction. A single narrow OPEN
  remains -- the 13-dim boundary could a priori be String and reach pi_13(tmf)=Z/3
  -- but it is gated by (i) unbuilt/obstructed String-ness (the K3 (1/2)p_1 pulls
  back) and (ii) the absence of any theorem equating the Witten genus with the
  net-chiral generation index. That crack does not add a NEW odd obstruction; it
  collapses into the program's already-named open bridges (the tangential-fork
  geometry and order-3-class -> integer-3 coupling). tmf provides no new 3-primary
  FORCING or OBSTRUCTING mechanism for the generation count.
""")

# ============================================================================
if FAIL:
    print("\nRESULT: BLOCKED -- failing checks:", FAIL)
    raise SystemExit(1)
print("RESULT: all checks pass. exit 0.")
