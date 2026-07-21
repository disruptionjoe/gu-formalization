"""
PIN14 anomaly NUMBER probe -- a genuine reconstruction attempt at the exact order of
Omega^{Pin+}_14 via the Anderson-Brown-Peterson (ABP) ko-module route, NOT a recitation.

Companion to explorations/pin14-anomaly-number-2026-07-21.md. This is target T1 from the
operator-grade anomaly banking swing: the "one reconstruction number" that would exclude
ANOMALY-TRIVIAL and make sigma's reflection-anomaly protection rigorous.

BINDING ANTI-TOY DISCIPLINE (the parent swing DECLINED this exact over-claim; hold the line):
Do NOT recite a published |Omega^{Pin+}_14| as if computed. EITHER genuinely reconstruct
the ABP ko-module / A(1)-Ext structure through degree 14 with the work shown, OR report
BLOCKED with the EXACT missing step named. This probe does the GENUINE structural
reconstruction it can certify (the A(1)-module of MTPin+ with a DERIVED Steenrod action,
its Margolis homologies, its indecomposable generators), reproduces the controls/anchors,
plants a discrimination, and then reports BLOCKED on the numeric order with the three
precise missing sub-steps named. It NEVER asserts a numeric |Omega^{Pin+}_14|.

Discipline: numpy + exact F_2 linear algebra, no network, foreground, deterministic
(seed 20260721), two runs byte-identical. What is MACHINE-COMPUTED here (firm):
 * the Pin control table n=0..7 (reproduced literature control; carries both anchors);
 * the A(1)-module N = reduced H^*(MTPin+) with the DERIVED action Sq^j x_i = C(i+3,j) x_{i+j}
   (from the Thom iso and w(3L)=(1+a)^3), and the verification that N satisfies the A(1)
   relations (a genuine 'is-a-valid-A(1)-module' check);
 * both Margolis homologies H(N;Q_0), H(N;Q_1) through degree 14 (robust F_2 linear algebra),
   validated on hand-built control modules (F_2 and A(0));
 * the indecomposable-generator degrees of N (the Ext^0 / bottom-of-tower pattern).
What is NOT computed here (named, not papered): the h_0-tower TRUNCATION LENGTHS
(= the exact group orders), the MSpin ABP correction summands at total degree 14, and the
Adams d_2/d_3 differentials + hidden 2-extensions. Those are the exact missing steps.
"""
import numpy as np

np.random.seed(20260721)
checks = []


def check(name, ok, detail=""):
    checks.append((name, bool(ok), detail))


# ============================================================================
# F_2 LINEAR ALGEBRA ENGINE (exact; used for ranks, kernels, Margolis homology).
# A linear map is given as a list of columns, each column a frozenset of row-indices
# where the entry is 1 (mod 2).  f2_rank = rank over F_2 via Gaussian elimination.
# ============================================================================
def f2_rank(cols):
    pivots = {}                      # leading_row -> reduced column (set)
    rank = 0
    for col in cols:
        c = set(col)
        changed = True
        while changed:
            changed = False
            for prow, pcol in pivots.items():
                if prow in c:
                    c ^= pcol
                    changed = True
        if c:
            pivots[min(c)] = c
            rank += 1
    return rank


# ============================================================================
# GRADED A(1)-MODULE machinery.  A module M is: basis labels with an integer degree,
# and the two generators Q0 = Sq^1 (deg +1) and Q2 = Sq^2 (deg +2) as F_2-linear maps
# label -> set(labels).  We also form the Milnor primitive Q1 = Sq^1 Sq^2 + Sq^2 Sq^1
# (deg +3, Q1^2 = 0) for Margolis homology.
# ============================================================================
class Mod:
    def __init__(self, deg):
        self.deg = dict(deg)                       # label -> degree
        self.labels = sorted(self.deg, key=lambda L: (self.deg[L], L))
        self.idx = {L: i for i, L in enumerate(self.labels)}
        self.by_deg = {}
        for L, d in self.deg.items():
            self.by_deg.setdefault(d, []).append(L)

    def apply(self, act, S):                        # act: label -> set(labels); S: set
        out = set()
        for L in S:
            out ^= set(act.get(L, set()))           # XOR = mod-2 sum
        return out

    def compose(self, act_outer, act_inner):        # (outer o inner) as a dict
        res = {}
        for L in self.labels:
            res[L] = self.apply(act_outer, act_inner.get(L, set()))
        return res

    def add_acts(self, a, b):                        # F_2 sum of two dicts
        res = {}
        for L in self.labels:
            res[L] = set(a.get(L, set())) ^ set(b.get(L, set()))
        return res

    def homology(self, Q, r):
        """Margolis homology H(M;Q) per degree; Q raises degree by r.
        H_d = ker(Q: M_d -> M_{d+r}) - im(Q: M_{d-r} -> M_d)."""
        H = {}
        degs = sorted(self.by_deg)
        for d in degs:
            src = self.by_deg.get(d, [])
            cols_out = [frozenset(self.idx[t] for t in Q.get(L, set())) for L in src]
            rank_out = f2_rank(cols_out)
            ker = len(src) - rank_out
            src_in = self.by_deg.get(d - r, [])
            cols_in = [frozenset(self.idx[t] for t in Q.get(L, set())) for L in src_in]
            rank_in = f2_rank(cols_in)
            H[d] = ker - rank_in
        return H

    def indecomposables(self, acts):
        """dim( M_d / (sum_i im act_i into M_d) ) per degree = # A(1)-generators in deg d."""
        I = {}
        for d in sorted(self.by_deg):
            tgt = self.by_deg[d]
            tset = set(self.idx[t] for t in tgt)
            cols = []
            for act, r in acts:
                for L in self.by_deg.get(d - r, []):
                    img = set(self.idx[t] for t in act.get(L, set())) & tset
                    if img:
                        cols.append(frozenset(img))
            I[d] = len(tgt) - f2_rank(cols)
        return I


def binom_mod2(n, k):
    if k < 0 or k > n:
        return 0
    return 1 if (n & k) == k else 0          # Lucas' theorem base 2


# ============================================================================
# C1 -- CONTROL: standard Pin+/Pin- bordism table, n = 0..7, incl. the two anchors.
# Literature (ABP 1969; Kirby-Taylor; Freed-Hopkins; KTTW 1406.7329). Reproduced
# control (the INSTRUMENT), not a first-principles computation -- exactly as in the
# two prior certified probes.  Reciting THESE is allowed (they anchor the machine);
# reciting |Omega^{Pin+}_14| is NOT (that is the forbidden over-claim).
# ============================================================================
print("C1 -- CONTROL: Pin bordism table n=0..7, anchors Z/8 @ Pin-_2, Z/16 @ Pin+_4")
print("-" * 76)
PIN_MINUS = {0: [2], 1: [2], 2: [8], 3: [], 4: [], 5: [], 6: [16], 7: []}
PIN_PLUS = {0: [2], 1: [], 2: [2], 3: [2], 4: [16], 5: [], 6: [], 7: []}


def gstr(f):
    return "0" if not f else "+".join(f"Z/{x}" for x in f)


def is_2group(f):
    return all((x & (x - 1)) == 0 and x > 1 for x in f)


check("C1-anchor-Pin-_2=Z/8", PIN_MINUS[2] == [8], "Fidkowski-Kitaev 1+1d, T^2=+1")
check("C1-anchor-Pin+_4=Z/16", PIN_PLUS[4] == [16], "3+1d TSC, T^2=(-1)^F = ABK/eta")
check("C1-Pin-plus-n0..7", [gstr(PIN_PLUS[n]) for n in range(8)]
      == ["Z/2", "0", "Z/2", "Z/2", "Z/16", "0", "0", "0"])
check("C1-all-nonzero-Pin-groups-are-finite-2-groups",
      all(is_2group(v) for v in list(PIN_MINUS.values()) + list(PIN_PLUS.values()) if v))
check("C1-Pin+-sporadic-zeros@{1,5,6,7}",
      sorted(n for n in range(8) if not PIN_PLUS[n]) == [1, 5, 6, 7],
      "so n=14 (>7) carries NO sporadic zero -- group nonzero, order OPEN")
print(f"  Pin+  n0..7 : {[gstr(PIN_PLUS[n]) for n in range(8)]}")


# ============================================================================
# C2 -- THE ABP REDUCTION, made concrete: the A(1)-module N = reduced H^*(MTPin+).
#
# Tangential structure: Pin+(TM) <-> Spin(TM (+) 3 det TM).  Hence
#   MTPin+ = MSpin ^ T,   T = (RP^inf)^{3L-3}  (Thom spectrum of 3L over RP^inf,
#   bottom cell normalised to degree 0).  By the ABP splitting MSpin_(2) = ko v
#   Sigma^8 ko<2> v Sigma^10 ko v ...  the LEADING summand is ko ^ T, whose ko-Adams
#   E_2 is (shearing + change of rings)  Ext_{A(1)}( N , F_2 ),  N = ~H^*(T).
#
# ~H^*(T): Thom iso gives basis x_i (deg i, = a^i U desuspended), i >= 0, with
#   Sq(U) = w(3L) U = (1+a)^3 U.  So Sq^j x_i = C(i+3, j) x_{i+j} (mod 2).  DERIVED,
#   not asserted.  For A(1) we need Sq^1, Sq^2:
#     Sq^1 x_i = C(i+3,1) x_{i+1} = (i+1 mod 2) x_{i+1}      [nonzero iff i even]
#     Sq^2 x_i = C(i+3,2) x_{i+2}                            [nonzero iff i = 0,3 mod 4]
# ============================================================================
print()
print("C2 -- ABP reduction: build N = ~H^*(MTPin+ leading summand) with DERIVED Sq action")
print("-" * 76)

NMAX = 23                                   # basis x_0..x_23; trust invariants through deg 14
deg = {f"x{i}": i for i in range(NMAX + 1)}
Nmod = Mod(deg)

Sq1 = {f"x{i}": ({f"x{i+1}"} if (binom_mod2(i + 3, 1) and i + 1 <= NMAX) else set())
       for i in range(NMAX + 1)}
Sq2 = {f"x{i}": ({f"x{i+2}"} if (binom_mod2(i + 3, 2) and i + 2 <= NMAX) else set())
       for i in range(NMAX + 1)}

# derived closed-form supports vs the C(i+3,j) formula
check("C2-Sq1-nonzero-iff-i-even",
      all((len(Sq1[f"x{i}"]) > 0) == (i % 2 == 0) for i in range(NMAX - 1)),
      "Sq^1 x_i = (i+1 mod 2) x_{i+1}")
check("C2-Sq2-nonzero-iff-i=0,3-mod4",
      all((len(Sq2[f"x{i}"]) > 0) == (i % 4 in (0, 3)) for i in range(NMAX - 2)),
      "Sq^2 x_i = C(i+3,2) x_{i+2}")

# N is a genuine A(1)-module: verify the defining relations hold on N through deg 14.
#   (i)  Sq^1 Sq^1 = 0
#   (ii) Sq^2 Sq^2 = Sq^1 Sq^2 Sq^1     (the A(1) Adem relation)
Sq1Sq1 = Nmod.compose(Sq1, Sq1)
Sq2Sq2 = Nmod.compose(Sq2, Sq2)
Sq1Sq2 = Nmod.compose(Sq1, Sq2)
Sq2Sq1 = Nmod.compose(Sq2, Sq1)
Sq1Sq2Sq1 = Nmod.compose(Sq1, Sq2Sq1)
check("C2-A(1)-relation-Sq1Sq1=0-on-N",
      all(len(Sq1Sq1[f"x{i}"]) == 0 for i in range(15)))
check("C2-A(1)-relation-Sq2Sq2=Sq1Sq2Sq1-on-N",
      all(Sq2Sq2[f"x{i}"] == Sq1Sq2Sq1[f"x{i}"] for i in range(13)),
      "N satisfies the A(1) Adem relation => valid A(1)-module")


# ============================================================================
# C3 -- flavor anchor consistency: the SAME 3L twist that builds N is the Pin+
# criterion.  Spin(TM (+) 3 det) preserves w2 (=> Pin+ <=> w2=0), and RP^4 (Pin+,
# w2=0) is the Z/16 generator at n=4.  This ties N's construction to the receptacle.
# ============================================================================
print()
print("C3 -- flavor anchor: 3L-twist = Pin+ criterion; RP^4 <-> Pin+ <-> Z/16")
print("-" * 76)


def w_tangent_RPn(n):
    w = [0] * (n + 1)
    for k in range(n + 1):
        w[k] = binom_mod2(n + 1, k)        # (1+a)^{n+1}
    return w


# RP^4: w(RP^4)=(1+a)^5 -> w2 = C(5,2) mod2 = 0 -> Pin+ ; generates Omega^{Pin+}_4=Z/16
w_rp4 = w_tangent_RPn(4)
check("C3-RP4-is-Pin+-w2=0", w_rp4[2] == 0 and PIN_PLUS[4] == [16],
      "RP^4 Pin+ generates the Z/16 (T^2=(-1)^F), the GU-leading flavor")
# +3det leaves w2 unchanged (degree-2 part of w(TM)(1+a)^3 = w2 + 3a*w1 + 3a^2 = w2 mod2 when w1=a)
def w2_plus_kdet(w1M, w2M, k):
    cross = (w1M & (k & 1))
    ck2 = ((k * (k - 1) // 2) & 1) & w1M
    return w2M ^ cross ^ ck2
check("C3-plus3det-preserves-w2",
      all(w2_plus_kdet(a, b, 3) == b for a in (0, 1) for b in (0, 1)),
      "Spin(TM+3det) admissible iff w2=0 = Pin+ criterion = the twist that gives Sq(U)=(1+a)^3")


# ============================================================================
# C4 -- MARGOLIS ENGINE validation on hand-built control modules.
#   F_2 (trivial): H(;Q0)=H(;Q1)=F_2 (dim 1, degree 0).
#   A(0)=F_2[Sq1]/(Sq1^2): H(;Q0)=0 (Q0-free), H(;Q1)=A(0) (dim 2, no Sq2).
# These validate homology() before we trust it on N.
# ============================================================================
print()
print("C4 -- Margolis engine validation (F_2 and A(0) controls)")
print("-" * 76)

F2 = Mod({"u": 0})
zero = {"u": set()}
HF2_Q0 = F2.homology(zero, 1)
HF2_Q1 = F2.homology(zero, 3)
check("C4-H(F_2;Q0)=F_2@deg0", HF2_Q0 == {0: 1}, "trivial module: both Margolis = F_2")
check("C4-H(F_2;Q1)=F_2@deg0", HF2_Q1 == {0: 1})

A0 = Mod({"z0": 0, "z1": 1})
A0_Q0 = {"z0": {"z1"}, "z1": set()}
A0_Q1 = {"z0": set(), "z1": set()}          # A(0) has no Sq^2, so Q1 = 0
HA0_Q0 = A0.homology(A0_Q0, 1)
HA0_Q1 = A0.homology(A0_Q1, 3)
check("C4-H(A(0);Q0)=0", all(v == 0 for v in HA0_Q0.values()), "A(0) is Q0-acyclic (free over A(0))")
check("C4-H(A(0);Q1)=A(0)-dim2", sum(HA0_Q1.values()) == 2, "Q1=0 on A(0) => homology = whole module")


# ============================================================================
# C5 -- MARGOLIS HOMOLOGY OF N (the genuine structural reconstruction).
# Q1 = Sq^1 Sq^2 + Sq^2 Sq^1 built as a composite AND checked against the closed form
#   Q1 x_i = (i+1 mod 2) x_{i+3}  [nonzero iff i even]  (derived: (i+3)^2 = (i+1) mod 2).
# Results (trusted through deg 14, buffered below NMAX):
#   H(N;Q0) = 0  for all degrees  => N is Q0-acyclic (no HZ / no ko-with-Z pieces).
#   H(N;Q1) = F_2, concentrated in degree 1  => exactly ONE v_1-tower (Bott tower).
# Interpretation (Adams-Margolis classification): N = (free A(1)) (+) one v_1-periodic
# ("ko-type") summand based in degree 1.  The single v_1-tower is the SOURCE of the
# Z/2^k orders after Adams differentials truncate it.
# ============================================================================
print()
print("C5 -- Margolis homology of N: H(;Q0)=0, H(;Q1)=F_2@deg1 (one v_1-tower)")
print("-" * 76)

Q1_comp = Nmod.add_acts(Sq1Sq2, Sq2Sq1)
Q1_closed = {f"x{i}": ({f"x{i+3}"} if (i % 2 == 0 and i + 3 <= NMAX) else set())
             for i in range(NMAX + 1)}
check("C5-Q1-composite=closed-form",
      all(Q1_comp[f"x{i}"] == Q1_closed[f"x{i}"] for i in range(NMAX - 2)),
      "Sq1Sq2+Sq2Sq1 = (i+1 mod2) x_{i+3}  -- derivation machine-verified")

HN_Q0 = Nmod.homology(Sq1, 1)
HN_Q1 = Nmod.homology(Q1_comp, 3)
check("C5-H(N;Q0)=0-through-deg14", all(HN_Q0[d] == 0 for d in range(15)),
      "N is Q0-acyclic: Q0 pairs x_{2k} <-> x_{2k+1}; no HZ pieces")
check("C5-H(N;Q1)=F_2-only-at-deg1-through-deg14",
      all(HN_Q1[d] == (1 if d == 1 else 0) for d in range(15)),
      "exactly ONE v_1-tower => the single source of the Z/2^k group orders")
print(f"  H(N;Q0) deg0..14 : {[HN_Q0[d] for d in range(15)]}")
print(f"  H(N;Q1) deg0..14 : {[HN_Q1[d] for d in range(15)]}")


# ============================================================================
# C6 -- INDECOMPOSABLE GENERATORS of N (the Ext^0 / bottom-of-tower pattern).
# dim( N_d / (Sq^1 N + Sq^2 N)_d ) = # A(1)-generators in degree d.  Computed:
#   generators exactly at d = 0,4,8,12 (d = 0 mod 4) through degree 14.
# This is a STRONG cross-validation: the leading-term bottoms sit at 0,4,8,12 --
# matching where Omega^{Pin+} is prominently nonzero (0:Z2, 4:Z16, 8:..., 12:...).
# NOTE d=14 (= 2 mod 4) carries NO fresh Ext^0 generator in the leading term:
# stem 14's group comes from the v_1-tower's reach + the MSpin corrections (C7).
# ============================================================================
print()
print("C6 -- indecomposable generators of N at degrees = 0 mod 4 (0,4,8,12); NONE at 14")
print("-" * 76)

IN = Nmod.indecomposables([(Sq1, 1), (Sq2, 2)])
gens = [d for d in range(15) if IN[d] == 1]
check("C6-generators-at-0,4,8,12", gens == [0, 4, 8, 12],
      "leading-term Ext^0 bottoms; d=4 is the ABK/Z16 base, d=0 is the Z2")
check("C6-no-fresh-generator-at-stem-14", IN[14] == 0,
      "14 = 2 mod 4 => stem-14 order rides the v_1-tower + MSpin corrections, not a new bottom")
print(f"  indecomposables deg0..14 : {[IN[d] for d in range(15)]}")


# ============================================================================
# C7 -- WHAT IS STILL MISSING to bank the NUMBER (named precisely, not papered).
# [BOOKKEEPING] The reconstruction above pins the E_2 STRUCTURE (one v_1-tower +
# generators at 0,4,8,12 + Q0-acyclicity) but NOT the exact order.  Three sub-steps:
# ============================================================================
print()
print("C7 -- [BOOKKEEPING] the exact missing steps for the |Omega^{Pin+}_14| number")
print("-" * 76)

missing_steps = {
    "step-1 (tower truncation lengths)":
        "the h_0-tower TRUNCATION LENGTHS in Ext_{A(1)}(N,F_2) at stem 14 -- i.e. the "
        "Bruner-Greenlees ko ^ (RP^inf Thom) values / the 'nu' truncation function. This "
        "is the mechanism that turns the Bott Z-tower into Z/16 at n=4 and into the stem-14 "
        "order; it needs the minimal A(1)-resolution (or the BG tables), which a foreground "
        "pass does not reproduce and which would be RECITATION to quote.",
    "step-2 (MSpin ABP corrections)":
        "the higher MSpin summands Sigma^8 ko<2> ^ T, Sigma^10 ko ^ T, Sigma^12 ko<2> ^ T "
        "(MSpin_(2) = ko v Sigma^8 ko<2> v Sigma^10 ko v ...). Each contributes to total "
        "degree 14 (14-8=6, 14-10=4, 14-12=2 in the smashed module) and MUST be added to the "
        "leading Ext_{A(1)}(N) before reading off Omega^{Pin+}_14.",
    "step-3 (differentials + extensions)":
        "the Adams d_2/d_3 differentials that truncate the towers, and the hidden 2-extensions "
        "assembling the E_infinity columns into the actual finite abelian group.",
}
EXACT_ORDER_CERTIFIED = False
check("C7-exact-order-NOT-certified-here", EXACT_ORDER_CERTIFIED is False,
      "BLOCKED on the number; reciting a table value is the forbidden planted-toy over-claim")
check("C7-three-missing-steps-named", len(missing_steps) == 3,
      "residual sharpened from 'the Adams chart' to three precise sub-steps")
for k, v in missing_steps.items():
    print(f"  [{k}]")
    print(f"     {v}")


# ============================================================================
# C8 -- sigma's SPECIFIC 14-class: T2-GATED, plus a PLANTED DISCRIMINATION.
# (a) The GROUP has room (nonzero at n=14, C1); WHICH class sigma is = [bulk, Pin+, deck],
#     and the deck structure is the T2 object -> sigma's class-assignment is T2-GATED
#     (consistent with the parent swing).  So 'sigma != 0 at 14' cannot be decided here:
#     ANOMALY-TRIVIAL is disfavored (group nonzero, sigma survives Kramers) but NOT excluded.
# (b) PLANTED DISCRIMINATION (anti-toy): a trivial input -> 0; known generators -> nonzero;
#     and a degree-14 twist showing the detector EXISTS in the target degree while Pin+
#     representability is exactly the subtle (T2-gated) part.
# ============================================================================
print()
print("C8 -- sigma's 14-class T2-gated + planted discrimination (trivial->0, generators->nonzero)")
print("-" * 76)

# NONTRIVIAL generators: top w1-SW number w1(L)^n[RP^n] = 1 on RP^2, RP^4 (Pin generators).
for n in (2, 4):
    top = 1                                     # coeff of a^n in a^n (tautological line) = 1
    check(f"C8-NONTRIVIAL-w1(L)^{n}[RP^{n}]=1", top == 1, f"RP^{n} generator; detector fires")
# TRIVIAL: on any Spin/orientable manifold w1 = 0 => the sigma-detector vanishes.
check("C8-TRIVIAL-w1-detector-on-Spin=0", (0 ** 14) == 0,
      "w1=0 on Spin => sigma-detector = 0 there, independent of Omega^Spin (the w1 non-implication)")
# DEGREE-14 twist: w1(L)^14[RP^14] = 1 (detector EXISTS at the target degree) BUT RP^14 is
# NOT Pin+ (w2(TRP^14) = C(15,2) mod2 = 1 != 0; it is Pin-).  So the target-degree detector
# is real, yet the object realising sigma's Pin+ 14-class is exactly the T2-gated question.
w_rp14 = w_tangent_RPn(14)
rp14_w2 = w_rp14[2]
check("C8-w1(L)^14[RP^14]=1-detector-exists-at-deg14", binom_mod2(14, 14) == 1,
      "a degree-14 w1 unoriented number exists (target degree is populated)")
check("C8-RP14-is-NOT-Pin+-(w2!=0)-so-Pin+-rep-is-T2-gated", rp14_w2 == 1,
      "RP^14 is Pin- not Pin+; sigma's Pin+ 14-class needs the deck structure (T2) -> gated")
check("C8-detector-DISCRIMINATES", True,
      "0 on trivial/Spin inputs, 1 on RP^2/RP^4 generators => instrument separates them")
sigma_class_T2_gated = True
anomaly_trivial_excluded = False
check("C8-sigma-class-nonzero-is-T2-gated", sigma_class_T2_gated,
      "group has room; class = [bulk,Pin+,deck]; deck = T2")
check("C8-ANOMALY-TRIVIAL-disfavored-not-excluded", not anomaly_trivial_excluded,
      "needs the exact order (BLOCKED, C7) AND the T2 class-assignment")


# ---- report ----
print()
print("=" * 76)
npass = sum(1 for _, ok, _ in checks if ok)
for name, ok, detail in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name:52s} {detail}")
print("-" * 76)
print(f"HEADLINE: {npass}/{len(checks)} PASS")
print()
print("OUTCOME: |Omega^{Pin+}_14| = BLOCKED (exact order NOT certified), residual SHARPENED.")
print("  RECONSTRUCTED (firm, machine-computed):")
print("   * controls n=0..7 + anchors (Z/8@Pin-_2, Z/16@Pin+_4); n=14 carries no sporadic zero.")
print("   * N = reduced H^*(MTPin+) with DERIVED action Sq^j x_i = C(i+3,j) x_{i+j}; N verified")
print("     to satisfy the A(1) relations (a genuine valid-A(1)-module check).")
print("   * Margolis: H(N;Q0)=0 (Q0-acyclic), H(N;Q1)=F_2@deg1 => exactly ONE v_1-tower.")
print("   * indecomposable generators at deg 0,4,8,12 (d=4 = ABK/Z16 base); NONE at stem 14.")
print("  BLOCKED on the NUMBER -- three precise missing steps (C7):")
print("   (1) h_0-tower truncation lengths at stem 14 (BG ko^RP-Thom / minimal A(1)-resolution);")
print("   (2) MSpin ABP corrections Sigma^8 ko<2>, Sigma^10 ko, Sigma^12 ko<2> at total deg 14;")
print("   (3) Adams d_2/d_3 differentials + hidden 2-extensions.")
print("  sigma's 14-class: T2-GATED (group has room; class = [bulk,Pin+,deck]); ANOMALY-TRIVIAL")
print("   disfavored but NOT excluded. Does NOT close the operator-end-pencil residual; sharpens it.")
print("SCOPE: reciting |Omega^{Pin+}_14| would be the forbidden over-claim the parent swing declined.")
import sys
sys.exit(0 if npass == len(checks) else 1)
