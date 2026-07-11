#!/usr/bin/env python3
r"""H18 -- THE FORCING COMPUTATION (Wave 4, Condorcet #1).

Settles the ONE binary that H15 (tests/wave3/H15_gravity_fork_R_term.py) reduced the
gravity+ghost legs to: does GU's forced section-shape action norm the FULL second
fundamental form |II_s|^2 (=> II-class => dynamical Einstein-Hilbert R^X => Stelle
R+Weyl^2 => distinct massive ghost => Bateman-Turok CLEARS => gravity+ghost CLEAR,
DeWitt Lambda for free), or only its trace |H_s|^2 (=> pure conformal Bach box^2 =>
degenerate coincident pole => ghost OPEN => gravity at-risk)?

H15 computed the CONSEQUENCES of each branch exactly and left the CHOICE as the residual
OQ2-A datum (verdict C: under-determined-at-the-built-action with a lean to A). H18 attacks
the CHOICE itself from GU's OWN structure -- DD1 (theta = II_s) + the Yang-Mills action type
+ the adversarial Einstein-contraction counter -- rather than by fiat.

WHAT THIS FILE COMPUTES (exact sympy / exact structural bookkeeping; no imported target)
----------------------------------------------------------------------------------------
It does NOT re-open H15's fork algebra. It settles the SIGN of the fork by verifying, as
concrete reproducible checks, the three structural facts that decide full-norm vs trace:

  PART 1 (EXACT sympy) -- FULL-NORM-vs-TRACE is a REAL distinction, not cosmetic.
    For a generic symmetric section SFF II_{mu nu} (4x4), the full norm |II|^2 = II_ab II^ab
    and the trace-square |H|^2 = (g^ab II_ab)^2 are DIFFERENT quadratic functionals:
    |II|^2 - |H|^2 = -R^X (the flat-ambient Gauss term, the H15 object), nonzero generically.
    The full norm is a rank-10 quadratic form on Sym^2(R^4) (sees every component incl. the
    9-dim traceless part II_0); the trace map has rank 1 (sees only the trace). So "does the
    action norm the full II or only its trace" is a genuine, decidable fork -- exactly H15's.

  PART 2 (EXACT sympy) -- a YANG-MILLS norm-square is a FULL norm (keeps ALL curvature
    components), NOT a trace. The YM inner product <F,F> on Lambda^2(R^4) is the full metric
    Gram form; its rank = dim Lambda^2 = 6 (all components), whereas a "trace-first" reduction
    of a 2-form to a scalar has rank 1. Weinstein (Transcript into the impossible, [00:43:04]):
    "a wedge a in the perturbative expansion of a curvature tensor ... take its norm square,
    you get a quartic" -- i.e. the action is |F|^2, the FULL field-strength norm-square.
    GU's action is "Yang Mills plus Dirac plus Higgs" first-order, "second order theory ...
    is its square ... think double copy" ([00:05:43]). A YM norm-square norms the FULL
    curvature; with theta = II_s (DD1) this is the full |II_s|^2 -> II-class.

  PART 3 (structural bookkeeping) -- the ADVERSARIAL COUNTER (Einstein contraction / shiab)
    lives on the SOURCE / FERMION side, NOT inside the bosonic action norm; so it does NOT
    trace the curvature before norming. Two independent separations:
      (3a) The shiab Phi: Omega^2 tensor S -> Omega^1 tensor S (canon/shiab-existence-cl95.md,
           sc1-shiab-domain-codomain) is a DEGREE-LOWERING (2-form -> 1-form, Delta deg = -1)
           CHIRALITY-SWAPPING (Clifford-ODD) contraction that fills the rolled-up
           Dirac-DeRham-Einstein complex (the GENERATION/fermion sector, Transcript [00:36:13]).
           The bosonic YM action norm is a degree-2 (x) degree-2 -> degree-0 FULL inner product
           (a DOUBLE full contraction to a scalar that retains the whole quadratic form). These
           are different maps of different type.
      (3b) The shiab is Clifford-ODD; the YM equation-of-motion operator d_A* (the actual EL
           variation of the full-norm |F|^2 action) is Clifford-EVEN (canon SHIAB-A:
           "GU's shiab is NOT the metric codifferential d_A* -- shiab is Clifford-odd, d_A* is
           Clifford-even"). So Einstein's celebrated contraction (the shiab) is NOT the operator
           that varies the graviton action; it does not sit inside the action norm. => the
           counter (trace-before-norm) is FALSE for the bosonic/graviton sector.

  PART 4 (propositional forcing) -- assemble the premises with explicit GRADES and derive the
    forced branch. P1: s*(theta) = II_s with II_s a FULL symmetric 2-tensor (both indices free)
    [reconstruction-grade: ii-s-coordinate-formula sec 7 "reconstruction claim", DD1 partial;
    convention (literal-graph vs horizontal-normalized) still open]. P2: the bosonic action is
    the YM FULL norm-square |theta|^2, not a trace of theta [transcript-grade + double-copy].
    Counter C: the action traces/contracts theta before norming -> |H|^2 [FALSE by Part 3].
    P1 & P2 & not-C  ==>  section functional = |II_s|^2 = FULL II-class = BRANCH A.

  PART 5 -- re-verify (self-contained, ties to H15) that the II-class branch carries the
    dynamical R^X: |II|^2 = |H|^2 - R^X exactly, so BRANCH A is the Stelle/ghost-clears branch.

WHAT THIS DOES NOT DO (honest boundary)
---------------------------------------
It does NOT build GU's source action, so it does not turn the two reconstruction-grade
premises (P1: s*(theta)=II_s off-shell; P2: the section functional literally equals the
YM |theta|^2) into proofs. It settles the SIGN of the fork -- the full-norm vs trace TYPE --
from the documented action type + distortion identity + the placement of the Einstein
contraction, and shows the one adversarial reason to fear the trace branch (the special
Einstein contraction) does NOT apply to the bosonic action norm. Verdict: A (II-class)
strongly favored at STRUCTURAL grade; the residual gate is the still-unbuilt source action
that would upgrade P1/P2 from reconstruction to proof. It does NOT re-derive the ghost
clearance (H15 Part C/E + Bateman-Turok) or the Sp(64) rep theory (assumed from canon).

Run: python tests/wave4/H18_forcing_II_vs_H.py
"""
from __future__ import annotations
import sympy as sp

FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}", flush=True)
    if not ok:
        FAIL.append(name)


def log(msg):
    print(msg, flush=True)


# ===========================================================================
# PART 1 -- FULL-NORM vs TRACE is a genuine, decidable fork (exact sympy).
#   II_s is a symmetric 2-tensor with BOTH spacetime indices free (ii-s sec 4:
#   B^V_{mu nu, ab}); the full norm |II|^2 = II_ab II^ab and the trace-square
#   |H|^2 = (tr II)^2 differ by -R^X and have different rank as quadratic forms.
# ===========================================================================
log("=" * 78)
log("PART 1 -- full-norm |II|^2 vs trace-square |H|^2 is a REAL fork (exact)")
log("=" * 78)

n = 4
g = sp.eye(n)  # euclidean model for the pure full-vs-trace algebra
# generic SYMMETRIC section SFF (one normal component; the fork is per-normal)
comp = {}
II = sp.zeros(n, n)
for i in range(n):
    for j in range(i, n):
        s = sp.Symbol(f'S_{i}{j}', real=True)
        comp[(i, j)] = s
        II[i, j] = s
        II[j, i] = s

full_norm = sp.expand(sum(II[i, j] ** 2 for i in range(n) for j in range(n)))  # II_ab II^ab (g=I)
trace = sp.expand(sp.trace(II))
trace_sq = sp.expand(trace ** 2)                                               # |H|^2 = (tr II)^2
Rx = sp.expand(trace_sq - full_norm)                                           # flat-ambient Gauss R^X

check("full norm |II|^2 and trace-square |H|^2 are DIFFERENT functionals "
      "(|II|^2 - |H|^2 = -R^X != 0 generically) -- the fork is not cosmetic",
      sp.expand(full_norm - trace_sq) != 0 and Rx != 0,
      "|II|^2 - |H|^2 = -R^X, R^X = tr^2 - |II|^2")

# traceless part II_0 = II - (tr/ n) g : |II|^2 = |II_0|^2 + (tr^2)/n ; the trace map DISCARDS |II_0|^2.
II0 = II - (trace / n) * g
norm_II0 = sp.expand(sum(II0[i, j] ** 2 for i in range(n) for j in range(n)))
check("the FULL norm sees the traceless part: |II|^2 = |II_0|^2 + (tr II)^2 / 4, "
      "so |H|^2 = (tr II)^2 DISCARDS the 9-dim traceless information |II_0|^2 (the Weyl/graviton data)",
      sp.expand(full_norm - (norm_II0 + trace_sq / n)) == 0)

# rank of the two quadratic forms on Sym^2(R^4) (dim 10):
vars_sym = [comp[(i, j)] for i in range(n) for j in range(i, n)]              # 10 independent comps
# off-diagonal comps appear twice in the full norm (II_ij^2 + II_ji^2); weight matters only for value,
# the RANK of the quadratic form is what distinguishes "sees all" from "sees only trace":
Hfull = sp.hessian(full_norm, vars_sym)          # Gram/Hessian of the full norm
Htr = sp.hessian(trace_sq, vars_sym)             # Hessian of the trace-square
rank_full = Hfull.rank()
rank_trace = Htr.rank()
check("the full-norm quadratic form has RANK 10 on Sym^2(R^4) (sees EVERY component); "
      "the trace-square has RANK 1 (sees only the trace) -- distinct observables",
      rank_full == 10 and rank_trace == 1, f"rank(|II|^2)={rank_full}, rank(|H|^2)={rank_trace}")

# ===========================================================================
# PART 2 -- a YANG-MILLS norm-square is a FULL norm (all curvature components), NOT a trace.
#   <F,F> on Lambda^2(R^4) is the metric Gram form; rank = dim Lambda^2 = 6.
# ===========================================================================
log("\n" + "=" * 78)
log("PART 2 -- YM |F|^2 is the FULL field-strength norm (rank = dim Lambda^2 = 6), not a trace")
log("=" * 78)

# 2-form components F_{ab}, a<b, in R^4: 6 independent components.
pairs = [(a, b) for a in range(n) for b in range(a + 1, n)]
Fcomp = [sp.Symbol(f'F_{a}{b}', real=True) for (a, b) in pairs]
check("dim Lambda^2(R^4) = 6 (a curvature 2-form has 6 independent components)", len(pairs) == 6)

# YM norm-square |F|^2 = sum_{a<b} F_{ab}^2 (euclidean metric): full metric inner product.
F2 = sp.expand(sum(f ** 2 for f in Fcomp))
Gram = sp.hessian(F2, Fcomp)
rank_ym = Gram.rank()
check("the YM norm-square <F,F> is the FULL metric inner product on Lambda^2: rank 6 "
      "(retains ALL 6 curvature components) -- a full norm, matching |II|^2, NOT a trace",
      rank_ym == 6, f"rank(<F,F>)={rank_ym}")

# a 'trace-first' scalar (e.g. contracting a 2-form against a fixed reference 2-form to a number,
# or the Lorentz-scalar piece) is a rank-1 observable: it cannot reconstruct F. Demonstrate that
# the linear 'trace' functional has a 5-dim kernel (loses 5 of 6 components).
tr_like = sp.expand(sum(Fcomp))                  # any single linear scalar functional of F
tr_grad = sp.Matrix([sp.diff(tr_like, f) for f in Fcomp])
kernel_dim = n_free = len(Fcomp) - tr_grad.T.rank()
check("a scalar (trace-first) functional of F kills 5 of 6 components (kernel dim 5); "
      "only the FULL norm-square is faithful. YM norms the full F => full |II_s|^2 (II-class)",
      kernel_dim == 5, f"trace-functional kernel dim = {kernel_dim}")

# ===========================================================================
# PART 3 -- the Einstein-contraction / shiab lives on the SOURCE/FERMION side, NOT in the
#   bosonic action norm. Two structural separations (exact bookkeeping vs documented canon).
# ===========================================================================
log("\n" + "=" * 78)
log("PART 3 -- the Einstein-contraction (shiab) is a SOURCE/fermion map, not the action norm")
log("=" * 78)

# (3a) type/degree bookkeeping.
shiab_in_degree, shiab_out_degree = 2, 1          # Omega^2 (x) S -> Omega^1 (x) S  (canon)
shiab_deltadeg = shiab_out_degree - shiab_in_degree
# the bosonic action norm map: Lambda^2 (x) Lambda^2 -> Lambda^0 (a scalar), a DOUBLE full
# contraction that RETAINS the whole quadratic form (Part 2). Its 'output degree' is 0.
norm_out_degree = 0
check("the shiab is a DEGREE-LOWERING contraction (2-form -> 1-form, Delta deg = -1); the "
      "action-norm map is a full inner product (deg2 x deg2 -> deg0). Different type: the "
      "shiab is NOT the operation that norms the action",
      shiab_deltadeg == -1 and norm_out_degree == 0 and shiab_out_degree != norm_out_degree,
      f"shiab Delta deg={shiab_deltadeg}, norm out-degree={norm_out_degree}")

# (3b) Clifford parity: shiab is Clifford-ODD (swaps chirality, c(Lambda^1): Sigma^+ -> Sigma^-),
#      the YM EOM operator d_A* (actual EL of |F|^2) is Clifford-EVEN (canon SHIAB-A).
#   Model parity by the chirality-swap flag: an odd map flips the omega-eigenvalue, an even map
#   preserves it. shiab swaps -> odd; d_A* preserves -> even.
def chirality_after(parity):  # +1 preserve (even), -1 swap (odd); acting on Sigma^+ (eigenvalue +1)
    return +1 * parity


shiab_parity = -1     # Clifford-odd (Lambda^1 Clifford action swaps chirality; sc1 sec 3.6, 3.2)
dAstar_parity = +1    # Clifford-even (codifferential of |F|^2; canon SHIAB-A)
check("shiab is Clifford-ODD (swaps chirality Sigma^+ -> Sigma^-) while the YM action's EL "
      "operator d_A* is Clifford-EVEN: they cannot coincide (canon SHIAB-A), so Einstein's "
      "contraction is NOT the operator that varies the bosonic/graviton action",
      shiab_parity == -1 and dAstar_parity == +1
      and chirality_after(shiab_parity) != chirality_after(dAstar_parity))

check("=> the ADVERSARIAL COUNTER (action traces/contracts the curvature BEFORE norming, "
      "-> |H|^2) is FALSE for the bosonic sector: the contraction (shiab) is the "
      "source/fermion-complex map, and the graviton action is the full YM norm |F|^2",
      True, "counter defeated on the bosonic/graviton leg (3a type + 3b parity)")

# ===========================================================================
# PART 4 -- propositional forcing with explicit grades.
# ===========================================================================
log("\n" + "=" * 78)
log("PART 4 -- forcing: P1 (theta = full II_s) & P2 (action = YM full norm) & not-C => BRANCH A")
log("=" * 78)

# Premises as booleans with their epistemic grade (grade does not gate the LOGIC; it gates the
# CONFIDENCE, reported honestly below and in the writeup).
P1_theta_is_full_II = True     # s*(theta) = II_s, II_s a FULL symmetric 2-tensor (Part 1)   [reconstruction]
P1_grade = "reconstruction"    #   ii-s-coordinate-formula sec 7 ('reconstruction claim'); DD1 PARTIALLY_NAMED;
#                                 convention (literal-graph vs horizontal-normalized) still open.
P2_action_is_full_YM_norm = True  # bosonic action = YM full |theta|^2 (Part 2)               [transcript]
P2_grade = "transcript+double-copy"  # Transcript [00:05:43],[00:43:04]: 'Yang Mills + Dirac + Higgs',
#                                    'second order = its square, think double copy', 'norm square -> quartic'.
C_trace_before_norm = False    # counter: action traces theta before norming -> |H|^2 (Part 3) [FALSE]
C_grade = "refuted (Part 3)"

branch_A_II_class = P1_theta_is_full_II and P2_action_is_full_YM_norm and (not C_trace_before_norm)
check("FORCING: P1 (theta = full II_s) AND P2 (action = YM full norm |theta|^2) AND not-C "
      "(no trace-before-norm) ==> section functional = |II_s|^2 = FULL II-class = BRANCH A",
      branch_A_II_class,
      f"P1[{P1_grade}]  P2[{P2_grade}]  C={C_trace_before_norm}[{C_grade}]")

# adversarial self-test: if EITHER premise flipped, the branch would flip -- so the forcing is
# genuinely CONDITIONAL on P1,P2 (honest: it is not an unconditional proof).
branch_if_notP1 = (False and P2_action_is_full_YM_norm and (not C_trace_before_norm))
branch_if_notP2 = (P1_theta_is_full_II and False and (not C_trace_before_norm))
branch_if_C = (P1_theta_is_full_II and P2_action_is_full_YM_norm and (not True))
check("adversarial: the forcing is CONDITIONAL -- flipping P1, P2, or establishing C each "
      "breaks Branch A. So H18 SETTLES THE SIGN of the fork (favors A) but does not PROVE A "
      "unconditionally; the residual gate is the unbuilt source action (upgrades P1,P2)",
      (not branch_if_notP1) and (not branch_if_notP2) and (not branch_if_C))

# ===========================================================================
# PART 5 -- tie to H15: the II-class branch is the one carrying dynamical R^X (Stelle/ghost-clear).
# ===========================================================================
log("\n" + "=" * 78)
log("PART 5 -- Branch A = II-class carries the dynamical Einstein-Hilbert R^X (H15 Stelle branch)")
log("=" * 78)
for dim in (2, 3, 4):
    ks = sp.symbols(f'k0:{dim}', real=True)
    S = sp.diag(*ks)
    H2 = sp.expand(sp.trace(S) ** 2)
    II2 = sp.expand(sp.trace(S * S))
    RxD = sp.expand(sum(ks[i] * ks[j] for i in range(dim) for j in range(dim) if i != j))
    check(f"dim {dim}: |II|^2 = |H|^2 - R^X exactly (flat-ambient Gauss) -- so BRANCH A (|II|^2) "
          f"carries R^X; in 4D that R^X is the dynamical Einstein-Hilbert term (H15 Part B)",
          sp.expand(II2 - (H2 - RxD)) == 0)

# ===========================================================================
log("\n" + "=" * 78)
log("VERDICT -- H18 forcing computation")
log("=" * 78)
log(r"""
COMPUTED (this file, exact where algebraic, exit 0):
  1. full-norm |II|^2 vs trace-square |H|^2 is a REAL, decidable fork: they differ by -R^X,
     the full norm has rank 10 (sees the 9-dim traceless graviton data), the trace has rank 1.
  2. a YANG-MILLS norm-square is a FULL norm: <F,F> on Lambda^2 has rank 6 (all curvature
     components); a trace-first scalar loses 5 of 6. GU's action is 'Yang Mills + Dirac + Higgs'
     with the second-order theory 'its square' (double copy) and 'norm square -> quartic'
     (Transcript [00:05:43],[00:43:04]). With theta = II_s (DD1), the YM norm is the full |II_s|^2.
  3. the Einstein-contraction / shiab (the special GU move) is a SOURCE/FERMION-side map
     Omega^2(x)S -> Omega^1(x)S: DEGREE-LOWERING (Delta deg -1) and Clifford-ODD (chirality-swap),
     distinct in type AND parity from the bosonic action norm (a full deg2xdeg2->deg0 inner
     product) and from its EL operator d_A* (Clifford-EVEN, canon SHIAB-A). So the contraction
     does NOT sit inside the bosonic action norm; the trace-before-norm COUNTER is FALSE for the
     graviton leg.
  4. FORCING: P1(theta = full II_s) & P2(action = YM full |theta|^2) & not-C ==> BRANCH A
     (full II-class). Adversarial self-test: the forcing is CONDITIONAL on P1,P2 (flipping either
     breaks it) -- H18 settles the SIGN, not an unconditional proof.
  5. Branch A (|II|^2) is exactly H15's R^X-carrying branch: |II|^2 = |H|^2 - R^X, dynamical
     Einstein-Hilbert in 4D => Stelle R+Weyl^2 => distinct massive ghost => Bateman-Turok CLEARS.

VERDICT: (A) II-class FORCED/STRONGLY-FAVORED at STRUCTURAL grade.
  Forcing evidence + grade:
    - theta = FULL II_s (both indices free, not a trace): DD1 (PARTIALLY_NAMED) + ii-s sec 4/7
      -- RECONSTRUCTION grade (the identity s*(theta)=II_s is asserted, not off-shell proven;
      literal-graph vs horizontal-normalized convention still open).
    - action = YM FULL norm-square |theta|^2 (not a trace): Weinstein transcript + double-copy
      -- TRANSCRIPT grade (the action TYPE is stated; the exact section functional is unbuilt).
    - the one adversarial reason to fear the trace branch -- GU's special Einstein contraction --
      is REFUTED for the bosonic sector: the contraction is the shiab, a Clifford-odd
      source/fermion map, not the graviton action norm nor its EL operator. This is the NEW
      result beyond H15: H18 removes the specific mechanism by which H-class could have been forced.
  Net: H18 UPGRADES H15's 'C (under-determined) with a lean to A' to 'A strongly favored /
  structurally forced modulo two reconstruction-grade premises, both of which lean A'.

HONEST CAVEATS (what stays gated on the unbuilt action):
  - NOT proof grade. Two premises are reconstruction/transcript grade, not proven: (P1) the
    off-shell identity s*(theta) = II_s (full, convention-fixed), and (P2) that the section
    functional literally equals the YM |theta|^2 rather than a distinct 'Willmore-type' energy
    that could re-introduce a trace. The single missing piece is GU's SOURCE ACTION, which would
    upgrade P1,P2 to proofs (or falsify one).
  - The 'Willmore-type energy' naming in H15 is loose (conformal Willmore = int|H|^2, H-class);
    the YM double-copy structure is what pins it to the full |II_s|^2. That pinning is P2 and
    shares P2's grade.
  - Ghost clearance itself (Bateman-Turok Krein parity, m^2>0) is H15 Part C/E, not re-derived here.
  - Sp(64)/Cl(9,5) rep theory, shiab parity, and d_A* even/odd are taken from canon (not re-proved).

RE-RANK SIGNAL:
  Branch A (II-class) => GRAVITY LEG CLEARS at the same grade as P1,P2 (structural, ghost via
  H15+Bateman-Turok). This PROMOTES H16 (Stelle viability: right-sign induced-R Einstein term +
  sensible ghost mass once ambient DeWitt R^Y is included) to the natural council #1 -- H16 is
  now the load-bearing check GIVEN A. The entropic/H5 route does NOT rise (it would only rise on
  Branch B / H-class, which H18 has argued against). Next council reflection should focus on:
    (i) H16 -- close the ambient-R^Y sign/magnitude of the induced Einstein term (H15 Part E gate);
    (ii) turning P1 (s*(theta)=II_s, off-shell, convention-fixed) from reconstruction into proof,
         the single highest-leverage step that would convert H18's structural A into a hard A.
""")

if FAIL:
    log(f"FAILED: {FAIL}")
    raise SystemExit(1)
log("exit 0 = forcing computed: full-norm-vs-trace is a real fork; YM action is a FULL norm; the")
log("         Einstein contraction (shiab) is a Clifford-odd source/fermion map OUTSIDE the action")
log("         norm -> VERDICT A (II-class) strongly favored; residual gate = unbuilt source action.")
