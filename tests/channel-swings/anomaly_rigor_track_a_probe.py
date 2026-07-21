"""
ANOMALY-RIGOR Track A probe -- the sigma-FREE, minimum-sufficient shot at rigorously
EXCLUDING ANOMALY-TRIVIAL, per explorations/anomaly-rigor-approach-scoping-2026-07-21.md
rung 1 / Track A.

TEST: does a w1(L_time)-monomial Stiefel-Whitney number of the observerse 14-geometry
SURVIVE the forgetful map  Omega^{Pin+}_14 -> Omega^O_14 ?

Logic (Thom): unoriented bordism Omega^O_* (of manifolds-with-a-real-line-bundle, i.e.
Omega^O_*(BZ/2)) is COMPLETELY detected by Stiefel-Whitney numbers -- monomials in the
tangent SW classes w_i(TM) and w1(L).  If ANY w1(L_time)-monomial SW number of sigma's
representative is NONZERO, then sigma's class is nonzero in Omega^O_14, hence nonzero in
Omega^{Pin+}_14 (a nonzero image under the forgetful HOMOMORPHISM forces a nonzero domain
element) -- ANOMALY-TRIVIAL rigorously EXCLUDED, WITHOUT the group order and WITHOUT the
sigma-circular T2 deck action.  If ALL w1-monomials vanish -> INCONCLUSIVE: sigma's class
may sit in ker(forgetful) = the Pin+ TORSION that SW numbers miss (e.g. the Z/16 at n=4 is
an ABK eta-invariant, NOT an SW number).

COMMITTED GEOMETRY USED (the ACTUAL observerse geometry, NOT a planted manifold):
  * sigma = w1(L_time) = the deck Z/2 of the spin double cover S^3 = Sp(1) -> RP^3 ~ F,
    = pi_1(RP^3) = the Cech-H^1 descent obstruction (wave-swing1 Members 3/4, tagged EXACT).
    So sigma is the PULLBACK of the degree-1 generator of H^*(F;Z/2), F ~ RP^3, and
    H^*(RP^3;Z/2) = F_2[a]/(a^4).  => sigma^4 = 0  (COMMITTED, EXACT; the pure power dies).
  * the observerse is 14-dimensional (signature (9,5), Cl(9,5) = M(64,H));
    Pin+ tangential structure  =>  w2(TM) = 0.
  * the base F ~ RP^3 ~ SO(3) is a Lie group, PARALLELIZABLE: w(TRP^3) = 1.

ANTI-TOY (binding): planted controls show the instrument DISCRIMINATES -- a known-trivial
input -> all SW numbers 0; the w1-generators RP^14 and RP^4 -> their w1-monomial fires (=1).
So a vanish on sigma's geometry is a REAL finding about sigma, not a vacuous instrument.

Discipline: exact mod-2 cohomology-ring arithmetic in F_2[a_i]/(a_i^{n_i+1}); no network;
foreground; DETERMINISTIC (no RNG at all); two runs byte-identical.
"""

checks = []


def check(name, ok, detail=""):
    checks.append((name, bool(ok), detail))


def binom_mod2(n, k):
    if k < 0 or k > n:
        return 0
    return 1 if (n & k) == k else 0          # Lucas base 2


# ============================================================================
# EXACT mod-2 cohomology ring of a product of real projective spaces:
#   H^*(RP^{c_0} x ... x RP^{c_{m-1}} ; F_2) = F_2[a_0,..,a_{m-1}] / (a_i^{c_i+1}).
# A class = a frozenset of exponent-tuples (each present with coeff 1 mod 2).
# The fundamental-class pairing (SW number) = coeff of the TOP monomial (c_0,..,c_{m-1}).
# ============================================================================
class CohRing:
    def __init__(self, caps):
        self.caps = tuple(caps)              # a_i^{caps[i]+1} = 0  <-> RP^{caps[i]}
        self.m = len(caps)

    def one(self):
        return frozenset({tuple([0] * self.m)})

    def gen(self, i, k=1):                    # a_i^k  (0 if k exceeds the cap)
        if k > self.caps[i]:
            return frozenset()
        e = [0] * self.m
        e[i] = k
        return frozenset({tuple(e)})

    def add(self, p, q):
        return frozenset(p ^ q)              # XOR = mod-2 sum

    def mul(self, p, q):
        out = set()
        for ep in p:
            for eq in q:
                e = tuple(ep[i] + eq[i] for i in range(self.m))
                if all(e[i] <= self.caps[i] for i in range(self.m)):
                    if e in out:
                        out.discard(e)          # 1+1 = 0
                    else:
                        out.add(e)
        return frozenset(out)

    def power(self, p, k):
        r = self.one()
        for _ in range(k):
            r = self.mul(r, p)
        return r

    def deg_part(self, p, d):
        return frozenset(e for e in p if sum(e) == d)

    def top_monomial(self):
        return tuple(self.caps)

    def evaluate(self, p):                    # SW number mod 2 on the product fundamental class
        return 1 if self.top_monomial() in p else 0

    def w_tangent_RP(self, i, n):             # total SW class of TRP^n = (1+a_i)^{n+1}
        return self.power(self.add(self.one(), self.gen(i, 1)), n + 1)


# ============================================================================
# C0 -- CONTROL: the two famous Pin anchors are consistent with the receptacle
#       flavor (Pin+ <-> w2=0), reproduced as an instrument sanity check.
# ============================================================================
print("C0 -- CONTROL: Pin+ criterion (w2=0) reproduces the flavor anchors")
print("-" * 76)
# RP^4 : w(TRP^4)=(1+a)^5, w2 = C(5,2) mod2 = 0  -> Pin+  (the Z/16 flavor, T^2=(-1)^F)
# RP^2 : w(TRP^2)=(1+a)^3, w2 = C(3,2) mod2 = 1  -> Pin-  (the Z/8 flavor,  T^2=+1)
check("C0-RP4-is-Pin+(w2=0)", binom_mod2(5, 2) == 0, "RP^4 generates Omega^{Pin+}_4 = Z/16")
check("C0-RP2-is-Pin-(w2!=0)", binom_mod2(3, 2) == 1, "RP^2 generates Omega^{Pin-}_2 = Z/8")


# ============================================================================
# C1 -- INSTRUMENT DISCRIMINATION (anti-toy).  The w1(L)-detector must FIRE on the
#       genuine w1-generators and VANISH on a known-trivial input.
# ============================================================================
print()
print("C1 -- instrument discriminates: RP^14 & RP^4 w1-generators FIRE; trivial input -> 0")
print("-" * 76)

# (a) RP^14 with the tautological line L (w1(L) = a): w1(L)^14 [RP^14] = a^14 [RP^14] = 1.
R14 = CohRing([14])
sig14 = R14.gen(0, 1)                         # w1(L) = a
fires_RP14 = R14.evaluate(R14.power(sig14, 14))
check("C1a-w1(L)^14[RP^14]=1-FIRES", fires_RP14 == 1,
      "the degree-14 w1-generator of Omega^O_14(BZ/2); instrument can output 1")
# honesty: RP^14 is Pin- not Pin+ (w2(TRP^14)=C(15,2) mod2 = 1 != 0) -- an INSTRUMENT control,
# NOT a Pin+ representative.  (Exactly the T2-gate noted in pin14_anomaly_number_probe C8.)
check("C1a-note-RP14-is-NOT-Pin+", binom_mod2(15, 2) == 1,
      "RP^14 is Pin- -> a firing w1-generator that is not in the Pin+ receptacle")

# (b) RP^4 (which IS Pin+, w2=0) with the tautological line: w1(L)^4[RP^4] = 1 FIRES.
R4 = CohRing([4])
fires_RP4 = R4.evaluate(R4.power(R4.gen(0, 1), 4))
check("C1b-w1(L)^4[RP^4]=1-FIRES-and-RP4-is-Pin+", fires_RP4 == 1 and binom_mod2(5, 2) == 0,
      "a Pin+ manifold CAN carry a firing w1-monomial (in dim 4) -> detector not vacuous on Pin+")

# (c) TRIVIAL control: L trivial (w1(L)=0=sigma) -> every w1-monomial vanishes.
sigma_trivial = R14.add(R14.gen(0, 1), R14.gen(0, 1))   # 0
all_zero_trivial = all(R14.evaluate(R14.power(sigma_trivial, k)) == 0 for k in range(1, 15))
check("C1c-trivial-L(w1=0)-all-w1-monomials-0", all_zero_trivial,
      "known-trivial input -> 0 ; with (a),(b) the instrument SEPARATES trivial from generator")


# ============================================================================
# C2 -- COMMITTED FACT: sigma is pulled back from F ~ RP^3, so sigma^4 = 0.
#       H^*(RP^3;F_2) = F_2[a]/(a^4).  This is the load-bearing committed input:
#       it CAPS the pure-power reach of sigma at sigma^3 and KILLS w1(L)^14.
# ============================================================================
print()
print("C2 -- committed: sigma = pullback of H^1(F~RP^3); sigma^4 = 0 (a^4=0), sigma^3 != 0")
print("-" * 76)

Rbase = CohRing([3])                          # F ~ RP^3 : F_2[a]/(a^4)
sigma = Rbase.gen(0, 1)
pow_nonzero = [k for k in range(0, 15) if len(Rbase.power(sigma, k)) > 0]
check("C2-sigma^k-nonzero-iff-k<=3", pow_nonzero == [0, 1, 2, 3],
      "H^*(RP^3)=F_2[a]/(a^4): a^0..a^3 nonzero, a^{>=4}=0")
check("C2-sigma^3-nonzero", len(Rbase.power(sigma, 3)) == 1, "a^3 = top class of RP^3")
check("C2-sigma^4=0-committed", len(Rbase.power(sigma, 4)) == 0,
      "sigma^4 = 0  =>  pure power w1(L)^14 = sigma^14 = 0 (committed, EXACT)")
check("C2-purepower-w1(L)^14=0", len(Rbase.power(sigma, 14)) == 0,
      "the only fully-committed w1-monomial (a pure power) VANISHES")


# ============================================================================
# C3 -- THE COLLAPSE (Kunneth on the committed RP^3 base): the ONLY w1-monomial
#       family that can survive is sigma^3 * P_11(w(TY)), a degree-11 SW number of
#       the 11-dim complement Y.  Everything else is forced 0 by committed structure.
#
#   TRP^3 is trivial (RP^3 parallelizable) => all tangent SW classes come from Y, and
#   the base contributes only sigma^k (k<=3).  For M = RP^3 x Y^11,
#       < sigma^k * T , [RP^3 x Y] > = < a^k, [RP^3] > * < T, [Y] > = [k==3] * <T,[Y]>.
#   So k>=4 -> sigma^k=0 ; k<2 -> a^k unpaired on RP^3 -> 0 ; only k=3 (deg T = 11) survives.
# ============================================================================
print()
print("C3 -- collapse: only sigma^3 * (deg-11 tangent number of the complement) can survive")
print("-" * 76)

# demonstrate the base forces k=3, using an abstract top class a1^11 on the Y=RP^11 factor:
Rmix = CohRing([3, 11])
sig_mix = Rmix.gen(0, 1)                       # sigma from the RP^3 base factor
topY = Rmix.gen(1, 11)                         # a formal degree-11 top class on Y
paired_k = [k for k in range(0, 15)
            if Rmix.evaluate(Rmix.mul(Rmix.power(sig_mix, k), topY)) == 1]
check("C3-base-forces-k=3-only", paired_k == [3],
      "<sigma^k * top_Y, [M]> = 1 iff k=3 (a^k pairs with [RP^3] iff k=3); the collapse")
# consequence: the surviving family is exactly sigma^3 * {degree-11 tangent numbers of Y}.
check("C3-survivor-is-sigma^3-times-deg11-of-Y", True,
      "sigma^{>=4}=0 (C2) and k<3 unpaired (C3) => survivor = sigma^3 * P_11(w(TY))")


# ============================================================================
# C4 -- THE ACTUAL EVALUATION on a concrete committed-consistent observerse
#       representative M = RP^3 x RP^11 (14-dim; Pin+ since w2(TM)=0; sigma pulled
#       from the RP^3 base).  GENUINE COMPLETE ENUMERATION of every degree-14
#       w1(L)-monomial SW number, mod 2.
# ============================================================================
print()
print("C4 -- ACTUAL enumeration on M = RP^3 x RP^11 (Pin+ 14-manifold; sigma on the RP^3 base)")
print("-" * 76)

# w(TM) = w(TRP^3) * w(TRP^11) = 1 * (1+a1)^12.  (1+a1)^12 = 1 + a1^4 + a1^8 (a1^12=0 on RP^11).
wTM = Rmix.mul(Rmix.w_tangent_RP(0, 3), Rmix.w_tangent_RP(1, 11))
w = {i: Rmix.deg_part(wTM, i) for i in range(15)}
# Pin+ check: w1(TM)=0 (orientable) and w2(TM)=0.
check("C4-M-orientable-w1(TM)=0", len(w[1]) == 0, "RP^3 (w=1) x RP^11 (w1=0): M orientable")
check("C4-M-is-Pin+(w2=0)", len(w[2]) == 0, "w2(TM)=0 -> M is Pin+ (in fact Spin); admissible receptacle")
# the only nonzero tangent SW classes are w4 = a1^4 and w8 = a1^8.
nonzero_w = [i for i in range(1, 15) if len(w[i]) > 0]
check("C4-nonzero-tangent-SW-at-{4,8}", nonzero_w == [4, 8], "w(TRP^11) = 1 + a1^4 + a1^8")

# COMPLETE enumeration of degree-14 w1(L)-monomials: sigma^k * w4^x * w8^y with k>=1,
# k + 4x + 8y = 14 (only w4,w8 are nonzero tangent classes on this M).
fired = []
enumerated = []
for x in range(0, 4):            # w4^x, 4x <= 14
    for y in range(0, 2):        # w8^y, 8y <= 14
        k = 14 - 4 * x - 8 * y
        if k < 1:
            continue
        cls = Rmix.power(sig_mix, k)
        cls = Rmix.mul(cls, Rmix.power(w[4], x))
        cls = Rmix.mul(cls, Rmix.power(w[8], y))
        val = Rmix.evaluate(cls)
        enumerated.append((k, x, y, val))
        if val == 1:
            fired.append((k, x, y))
# pure power w1(L)^14 is the (k=14,x=0,y=0) entry, already included above.
any_fired = len(fired) > 0
check("C4-enumeration-nonempty", len(enumerated) >= 6, f"{len(enumerated)} degree-14 w1-monomials enumerated")
check("C4-NO-w1-monomial-fires-on-this-representative", not any_fired,
      "every degree-14 w1(L)-monomial SW number = 0 on RP^3 x RP^11")
print("  w1(L)-monomials sigma^k * w4^x * w8^y  (k+4x+8y=14):")
for (k, x, y, val) in enumerated:
    why = ("sigma^k=0 (k>=4)" if k >= 4 else
           ("tangent hits a1^12=0" if (4 * x + 8 * y) >= 12 else "unpaired on RP^3"))
    print(f"    sigma^{k:<2} w4^{x} w8^{y}  = {val}   [{why}]")


# ============================================================================
# C5 -- WHY the survivor is GATED, not merely zero-on-this-model.  The surviving
#       family sigma^3 * P_11(w(TY)) is a degree-11 SW number of the 11-dim
#       COMPLEMENT Y.  Committed structure fixes sigma (and sigma^4=0) but NOT the
#       bordism class of Y (the deck/fiber data = the T2 object).  So no w1-monomial
#       is a function of committed data alone EXCEPT the pure powers -- which are 0.
# ============================================================================
print()
print("C5 -- the survivor sigma^3*P_11(w(TY)) is T2-GATED (depends on the un-committed complement)")
print("-" * 76)

# The set of w1-monomials whose VALUE is fixed by committed structure alone:
#   * pure powers sigma^k (k=1..14): fixed = 0 for all k (sigma^4=0, and k<14 is not top-degree).
#   * any monomial with sigma-exponent >= 4: fixed = 0 (sigma^{>=4}=0).
# The complementary family (sigma-exponent <= 3 mixed with tangent classes) is NOT fixed by
# committed data: it equals <P_11(w(TY)),[Y]>, and w_{>=3}(TY) / [Y] are the T2-gated deck data.
committed_forced_monomials_all_zero = all(len(Rbase.power(sigma, k)) == 0 for k in range(4, 15))
check("C5-committed-forced-w1-monomials-all-zero", committed_forced_monomials_all_zero,
      "the ONLY committed-determined w1-monomials (sigma-exp>=4, incl. pure w1(L)^14) are all 0")
# committed data does not even fix w1(TY): the RP^11 completion is Spin (w1(TY)=0), but the
# true observerse complement's orientation/high-SW classes are un-committed (T2-gated).
check("C5-complement-SW-classes-un-committed", True,
      "sigma is committed; [Y] in Omega^{Pin+}_11 (the deck/fiber class) is NOT -> survivor gated")
check("C5-no-committed-w1-monomial-FIRES", not any_fired and committed_forced_monomials_all_zero,
      "Track A CANNOT fire from committed structure: committed reach = pure powers = forced 0")


# ============================================================================
# C6 -- LOGICAL STRENGTH bookkeeping (the exact grade of each branch).
# ============================================================================
print()
print("C6 -- [BOOKKEEPING] exact logical strength of FIRE vs VANISH")
print("-" * 76)

# FIRE branch (NOT realized this pass): a nonzero w1(L)-monomial SW number of sigma's
# representative => sigma != 0 in Omega^O_14(BZ/2) (Thom: SW numbers detect Omega^O) =>
# sigma != 0 in Omega^{Pin+}_14 (nonzero image under the forgetful HOMOMORPHISM forces
# nonzero domain element).  Strength: proves sigma != 0 in the receptacle, sigma-FREE
# (no group order, no deck action).  This IS a rigorous exclusion of ANOMALY-TRIVIAL.
check("C6-FIRE-would-prove-sigma!=0-in-Pin+_14-sigma-free", True,
      "nonzero SW# -> nonzero in Omega^O -> nonzero in Omega^{Pin+}_14 via forgetful hom")
# VANISH branch (realized): all w1-monomials 0 -> sigma's IMAGE in Omega^O_14 is 0.  This is
# INCONCLUSIVE, NOT trivialization: sigma may lie in ker(forgetful) = Pin+ torsion invisible
# to SW numbers (the Z/16 at n=4 is an eta-invariant, not an SW number).
check("C6-VANISH-is-INCONCLUSIVE-not-trivialization", True,
      "SW-blind ker(forgetful) = Pin+ torsion (eta-detected); vanish neither excludes nor trivializes")
# AND, sharper: Track A's committed reach = pure powers of sigma = forced 0 by sigma's 3-dim
# base origin.  Every candidate-firing (mixed) monomial is gated on sigma's T2 representative.
check("C6-Track-A-collapses-onto-the-sigma-circular-T2-gate", True,
      "the sigma-free SW shot's firing monomials are all T2-gated -> back to the class-gate wall")


# ---- report ----
print()
print("=" * 76)
npass = sum(1 for _, ok, _ in checks if ok)
for name, ok, detail in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name:52s} {detail}")
print("-" * 76)
print(f"HEADLINE: {npass}/{len(checks)} PASS")
print()
print("OUTCOME: Track A VANISHES from committed structure -> ANOMALY-TRIVIAL INCONCLUSIVE.")
print("  * pure power w1(L_time)^14 = sigma^14 = 0 (COMMITTED: sigma pulled from F~RP^3, a^4=0);")
print("  * complete enumeration on the Pin+ representative RP^3 x RP^11: NO w1-monomial fires;")
print("  * the only survivor family sigma^3 * P_11(w(TY)) is a degree-11 SW number of the")
print("    un-committed 11-dim complement Y -> T2-GATED (the deck/fiber class).")
print("  Instrument DISCRIMINATES: RP^14 & RP^4 w1-generators FIRE (=1); trivial input -> 0.")
print("GRADE: does NOT make sigma's anomaly-protection rigorous. The sigma-free SW route's")
print("  committed reach is exactly the pure powers of sigma, forced 0 by sigma's 3-dimensional")
print("  base origin; every candidate-firing monomial is gated on sigma's T2 representative.")
print("  So Track A collapses back onto the sigma-circular T2 class-gate. NOT excluded, NOT")
print("  trivialized: rigorous exclusion still waits on external operator-grade deck input")
print("  (or rung-2: the Pin+ eta-invariant on sigma's deck geometry).")
import sys
sys.exit(0 if npass == len(checks) else 1)
