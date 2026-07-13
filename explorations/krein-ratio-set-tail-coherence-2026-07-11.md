---
artifact_type: exploration
status: exploration (SECOND FOLLOW-ON to the W103 tail-quotient steelman; the named first-decisive computation: the Krein-graded Araki-Woods/ITPFI tower + the asymptotic-ratio invariant, and the P2-restoration test at the class level; deterministic test + honest self-critique)
created: 2026-07-13
hypothesis: H61 / H61a (the observer-conjecture Krein-TT critical path) -- post-W103: can the tail slot be made ALGEBRA-INTRINSIC (candidate identity: cond -> inf <=> 0 enters the Krein ratio invariant), and do the per-region TAIL CLASSES cohere on overlaps even though the J's (W98 T6) do not?
conjecture: "the source action IS the observer (CONJECTURE-source-action-is-the-observer-2026-07-11.md)"
title: "T1 = PARTIAL, T2 = CLASSES-COHERE.  (T1) The Krein-graded Araki-Woods tower over the W98 mode data is WELL-DEFINED (metric-as-state ITPFI: every finite mode is a faithful positive state -- adversary (a) answered; the genuinely-Krein SIGNED ratio degenerates to -1 identically, so the classical r_inf of the metric-state tower is the only workable definition, a named fork).  The PHYSICAL tower is intrinsically the hyperfinite TYPE III_1 factor (lam_k = (1-r_k)/(1+r_k) ~ c/k slowly varying, non-summable: dense pair ratios with per-window mass bounded below) -- the AQFT local-algebra type reproduced from the Krein tail data, a nontrivial consistency.  BUT THE CANDIDATE IDENTITY FAILS IN BOTH DIRECTIONS: the marginal O(1/k) coupling gives a Powers III_lam factor (0 IN r_inf) with NO wall (kills <=), and the derivative-growing coupling g = G*k gives cond -> inf (wall) with a TYPE I_inf tower, r_inf = {1} (kills =>).  The wall is fully TRANSVERSE to the classical ratio-set/type invariant (all four cells inhabited, for both '0 in r_inf' and 'III_1').  COROLLARY: W103's rate-independence does NOT survive -- PHYS and DERIV share the Calkin class 2[P] but have DIFFERENT ITPFI types (III_1 vs I_inf); the Calkin class does not determine the intrinsic tail invariant.  WHAT SURVIVES (exact, verified): the REPAIRED identity -- wall <=> the relative modular operator between the metric-state and its GRADING twist is unbounded (per-mode ||Delta_{phi o AdJ, phi}|| = cond(eta(r)) EXACTLY, via eta(-r) = (1-r^2) eta(r)^{-1}; fidelity F = 1-r^2 exactly; Connes cocycle unitary at every real t = the flow half FREE, analytic continuation to t = -i/2 diverges like sqrt(cond) = the conjugation half OBSTRUCTED -- the W103 split in relative-modular language).  So the slot IS intrinsic -- but to the (algebra, state, GRADING, filtration) data, not to the (algebra, state) pair: the classical classification is grading-blind, which is exactly WHY it cannot see the wall.  (T2) TAIL CLASSES COHERE on overlaps: with W98's region-dependent modular weights the operator disagreement ||eta_1^{-1/2} - eta_2^{-1/2}|| DIVERGES in the UV (W98 T6 reproduced) while the metric difference |r^1_k - r^2_k| -> 0 is COMPACT: both regions restrict to the SAME singular class 2[P] with the SAME Krein-null line -- ONE typed slot shared by both observers.  The interface glues; only the God's-eye operator does not.  NOT TRIVIAL (adversary (b) answered by two controls): a ROTATED modular frame has the identical break but non-compact metric difference and DISAGREEING classes; a UV-collapsing weight makes the classes maximally disagree.  Coherence holds because W98's region-dependence is a SCALAR modular weight bounded below (direction fixed by field content) -- two named load-bearing assumptions."
grade: "exploration / model-surrogate grade on the W98 Krein-doublet tower (the repo's own mode data).  HIGH within the model: every per-mode identity (eta(-r) = (1-r^2)eta(r)^{-1}, F = 1-r^2, ||Delta_rel|| = cond, signed ratio = -1, |eta(r1)-eta(r2)| = |r1-r2|) is exact/machine-verified; the two-direction failure of the candidate identity is counter-example-explicit; the coherence result and both controls are computed (tests/W107_krein_ratio_tail_coherence.py, 10/10, numpy-only, exit 0).  MEDIUM-HIGH: the type assignments (III_1 / II_1 / III_lam / I_inf) -- the Araki-Woods criteria used (type I iff summable small-eigenvalue mass; II_1 iff sum(1/2-mu)^2 < inf; Powers; two log-irrational ratios => III_1; r_inf = Connes S-invariant) are standard named literature, but the III_1 assignment for the slowly-varying c/k list is computation + criterion grade, not a verbatim cited theorem.  MEDIUM: the metric-as-state construction fork (the standard machinery fed the program-native metric) -- canonical given W52's unique positive intertwiner, but the identification 'metric = state' is a modelling choice, named.  LOW-MEDIUM: extrapolation beyond the doublet surrogate to the genuine III_1 region algebra.  No canon / RESEARCH-STATUS / CANON / claim-status / verdict / posture change; H61/H61a remain OPEN; W98, W100, W103 stand unchanged."
depends_on:
  - explorations/steelman1-adapter-tail-quotient-2026-07-11.md
  - explorations/break-sectorial-closure-interacting-2026-07-11.md
  - explorations/obj2-sectorial-falsification-theorem-2026-07-11.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
  - tests/W103_steelman1_tail_quotient.py
  - tests/W98_break_sectorial_closure.py
scripts:
  - tests/W107_krein_ratio_tail_coherence.py
external_refs:
  - "H. Araki & E. J. Woods, Publ. RIMS 4 (1968) 51 -- classification of ITPFI factors by the asymptotic ratio set r_inf; the criteria used here: type I iff the small-eigenvalue mass is summable; type II_1 iff sum(1/2 - mu_k)^2 < inf; Powers factors III_lambda from constant ratio; two ratios with irrational log-ratio give III_1; r_inf is computed from eigenvalue-ratio products over tail blocks subject to a mass condition."
  - "R. T. Powers, Ann. of Math. 86 (1967) 138 -- the one-parameter family of type III_lambda factors from constant eigenvalue ratio."
  - "A. Connes, Ann. Sci. ENS 6 (1973) 133 -- the S- and T-invariants; for ITPFI factors S(M) = r_inf(M); 0 in S(M) iff M is type III; III_1 iff S = [0,inf).  Also the Connes cocycle [D psi : D phi]_t and its analytic-continuation characterization of state domination -- the machinery behind the repaired identity."
  - "H. Araki, Publ. RIMS 11 (1976) 809 (relative modular theory); relative modular operators Delta_{psi,phi} for pairs of faithful normal states -- the intrinsic object whose per-mode norm equals the W98 conditioning exactly."
  - "A. Connes & M. Takesaki, flow of weights -- the intrinsic tail data of a type III factor; the frontier frame W103 named.  This swing shows the W98 wall is NOT a function of it (transversality)."
  - "D. Buchholz, C. D'Antoni, K. Fredenhagen -- local algebras are the hyperfinite III_1 factor; the physical tower's intrinsic type matches this (consistency check, Section 2)."
  - "S. Kakutani, Ann. of Math. 49 (1948) 214 (dichotomy for infinite product measures); Araki's quasi-equivalence criterion for product states via per-mode fidelity -- used for the grading-twist disjointness computation (F(phi_k, phi_k o J) = 1 - r_k^2 exactly)."
---

# The Krein ratio set and tail-class coherence: the two named follow-on targets of W103

**Role.** `W103` (steelman 1) showed the `W98` wall factors EXACTLY through the Calkin tail quotient
(`[C] = 2[P]` singular, condition `X` = quotient invertibility, a typed slot on the Krein-null
essentially-complex line) and scoped two decisive next computations: **(1)** replace the
ideal-by-fiat Calkin surrogate by an intrinsic invariant -- build the Krein-graded Araki-Woods/ITPFI
tower over the mode data and compute the Krein analogue of the asymptotic ratio set, testing the
candidate identity `cond -> inf <=> 0 enters the Krein ratio invariant`; **(2)** test whether the
per-region **tail classes** cohere on overlaps even though the per-region `J`'s (`W98` T6) disagree
divergently. This swing does both. Kill-or-learn posture; both adversaries taken seriously:
(a) "the ratio-set machinery needs positive states -- the Krein version may be ill-defined";
(b) "class agreement on overlaps is automatic for compact-difference reasons."

**Answer: T1 = PARTIAL (the candidate identity FAILS both directions; a repaired grading-relative
identity holds exactly), T2 = CLASSES-COHERE (with counter-model-backed content).**
**Artifacts:** this file + `tests/W107_krein_ratio_tail_coherence.py` (10/10, numpy-only, exit 0).
**Not committed. Not a claim-status change.**

---

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md discipline)

| Object | Construction used | Load-bearing here |
|---|---|---|
| **The tower** | **standard-math machinery fed the program-native object**: the ITPFI factor `M = (x)_k (M_2, phi_k)` with per-mode state `phi_k = eta(r_k)/2` -- the W52 unique positive intertwiner, normalized (**the metric AS the state**). Eigenvalue list `((1-r_k)/2, (1+r_k)/2)`; per-mode ratio `lam_k = (1-r_k)/(1+r_k)` = exactly the Krein metric's eigenvalue-ratio data. | The decisive fork of T1. The metric-as-state identification is CANONICAL given W52 (the intertwiner is unique) but it is a modelling choice; the genuinely-Krein signed alternative is computed and shown DEGENERATE (Section 1), so this fork is forced-or-nothing, named not defaulted. |
| **The ratio invariant** | **standard-math** (Araki-Woods `r_inf` = Connes S-invariant; the type criteria of Araki-Woods 1968). | This is exactly what "algebra-intrinsic" means here; using it is the point of the swing. |
| **The wall** | the repo's own `W98` quantity: `cond(C) = sup_k (1+r_k)/(1-r_k)` over the region's modes. | Unchanged from W98/W103; the question is whether it descends to the invariant. It does not (Section 3). |
| **The regions / overlap** | `W98` T6's own setup: shared overlap modes with region-dependent scalar modular weights `w_O1 = 1.0`, `w_O2 = 0.45` rescaling the coupling. | T2 is computed on the exact configuration whose OPERATOR coherence W98 broke -- no substitution. The scalar-weight form (direction fixed) is the named load-bearing assumption (Section 5). |

---

## 1. The tower is well-defined; the signed Krein ratio is degenerate (adversary (a))

Two halves, both computed (`W107` T1):

- **The construction stands.** Every finite mode of every coupling profile has `r_k < 1` strictly
  (the W98/W103 exactness), so every `phi_k` is a **faithful positive state** and the tower is a bona
  fide ITPFI factor. Adversary (a)'s objection -- "the classical construction needs positive states" --
  bites only at `k = inf`, which is not a mode: positivity fails exactly and only where the invariant
  (a tail object) lives. The machinery applies.
- **The genuinely-Krein signed alternative carries no information.** The `J`-selfadjoint object
  `A = J eta(r) = sigma_z - i r sigma_x` satisfies `A^2 = (1 - r^2) I`: eigenvalues `-+sqrt(1-r^2)`,
  **signed ratio identically `-1` at every `r < 1`** (verified to 1e-15). A "signed Krein ratio set"
  is constant; its only invariant content is the exceptional-point collision at `r = 1` -- i.e. the
  conditioning again. So the **only workable Krein ratio set is the classical `r_inf` of the
  metric-as-state tower** -- a named fork, forced by computation rather than defaulted.

---

## 2. The classical type of the tower: the physical coupling lands exactly on III_1

The Araki-Woods eigenvalue list of the physical (`g = const`, non-UV-soft) tower is
`lam_k = (1-r_k)/(1+r_k) ~ c/k` -- **slowly varying** (`k*lam_k` constant to 0.2% over `k = 1e3..1e6`)
and **non-summable** (per-decade partial sums equal and non-vanishing). Consequences (`W107` T2, T3):

- pair ratios `lam_j/lam_k ~ k/j` are **dense in `(0,inf)`** and realized in every far window
  `[N, 16N]` to `< 0.1%` for targets `{0.5, 2, 3.7, 10}`, with the window excitation mass
  `sum mu_k ~ c*ln 16` **bounded below uniformly in `N`** (the `r_inf` mass condition);
- hence `r_inf = [0, inf)`: the physical tower is **the hyperfinite type III_1 factor**.

**This is a genuine positive:** the Krein doublet tail data, fed through the standard machinery,
intrinsically reproduces the AQFT type of a local algebra (Buchholz-D'Antoni-Fredenhagen) -- the
model's UV tail is exactly III_1-generic, consistent with W98's premise that the region is type III_1.

**What the grading does to the classification: nothing -- and that is the finding.** The grading acts
per mode by `eta(r) -> J eta(r) J = eta(-r)`, preserving every eigenvalue list; the graded tower is a
`Z_2`-graded hyperfinite III_1 factor whose classical invariants are **grading-blind**. The wall lives
exactly in the (state, grading) pairing that the classification drops (Section 4).

The other profiles on the same doublet tower (`W107` T3):

| profile | coupling | `lam_k` behavior | classical type | wall (`cond -> inf`)? | `0 in r_inf`? |
|---|---|---|---|---|---|
| PHYS | `g = G` | `~ c/k`, non-summable | **III_1** | **YES** | YES |
| SOFT (condition X) | `g = G/k^2` | `-> 1`, `sum(1/2-mu)^2 < inf` | **II_1** | no | no |
| MARG | `g = G/k` | `-> lam* ~ 0.101` const | **Powers III_lam*** | **no** | **YES** |
| DERIV | `g = G*k` | `~ c/k^2`, **summable** | **I_inf** | **YES** | **no** |
| 2VAL (control) | two ratios, log-irrational | `{a, b}`, dense subgroup | **III_1** | **no** | YES |

---

## 3. The candidate identity FAILS in both directions (Task 1 verdict core)

**`cond -> inf <=> 0 enters the Krein ratio invariant`: FALSE, with explicit counterexamples inside
the model class** (`W107` T4):

- **`<=` killed by MARG:** the marginal `O(1/k)` coupling gives a Powers factor `III_{0.101}` --
  `0 in r_inf` (every type III has it) -- while the conditioning **plateaus** (`~ 9.9`): no wall.
- **`=>` killed by DERIV:** the derivative-vertex growing coupling `g = G*k` (W103's own T4 profile)
  drives `cond ~ k^2 -> inf` (wall) while `mu_k ~ c/k^2` is **summable**: the per-mode states become
  so nearly pure that the tower is **type I_inf**, `r_inf = {1}`, `0 not in r_inf`. The invariant is
  trivial exactly where the wall is worst.
- **Full transversality:** all four cells of (wall) x (`0 in r_inf`) are inhabited -- and all four of
  (wall) x (III_1) too (DERIV: wall without III_1; 2VAL: III_1 at bounded conditioning, no wall). No
  classical (algebra, state) invariant of this family can be equivalent to the wall.

**The mechanism, stated plainly:** the wall is a **sup** statement (does the per-mode degeneracy reach
`r = 1`); the ratio invariant is a **statistics** statement (at what rate, with how much mass). Fast
degeneracy (DERIV) crosses the wall while starving the invariant of mass (type I); bounded degeneracy
with the right ratio statistics (MARG, 2VAL) feeds the invariant without any wall.

**Corollary -- W103's rate-independence does not survive the upgrade** (`W107` T5): PHYS and DERIV
differ by a compact operator (block norms `2.2e-3 -> 2.3e-6`; the same Calkin class `2[P]`, W103 T4
reproduced) yet have **different intrinsic types** (III_1 vs I_inf). The Calkin quotient forgets the
rate; the ITPFI invariant remembers it. "One typed slot for all non-UV-soft couplings" is a property
of the compact-ideal quotient **only** -- the honest cost of going intrinsic.

---

## 4. What survives: the repaired identity (exact) -- the wall is (state, GRADING)-relative

The grading twists the state: `phi o AdJ` has per-mode density `eta(-r)/2`, and
`eta(-r) = (1 - r^2) eta(r)^{-1}` **exactly**. Three exact consequences (`W107` T6, verified to 1e-9
at `r` up to 0.999):

1. **Fidelity:** `F(phi_k, phi_k o J) = 1 - r_k^2` exactly.
2. **Relative modular operator (Araki):** `||Delta_{phi o J, phi}||_k = (1+r_k)/(1-r_k) = cond(eta(r_k))`
   **exactly** -- the W98 wall quantity IS the per-mode norm of a canonical, basis-free,
   representation-independent object of relative modular theory.
3. **Connes cocycle split:** `u_t = eta(-r)^{it} eta(r)^{-it}` is **unitary at every real `t`** (the
   flow half is free, zero cost), while the analytic continuation to `t = -i/2` has per-mode norm
   `sqrt(cond) -> inf` (the conjugation half is obstructed) -- **the W103 flow/conjugation split
   reproduced in relative-modular language**, now attached to intrinsic objects.

**The repaired identity (holds exactly across all five profiles):**

> `cond(C) -> inf  <=>  sup_k ||Delta_{phi o AdJ, phi}||_k = inf`
> (the relative modular data between the metric-state and its grading twist is unbounded over the
> mode filtration; equivalently the cocycle `[D(phi o J) : D phi]` has no bounded continuation to
> `-i/2` uniformly in the modes).

**The honest residual (named, not hidden):** the `sup` is over the **mode filtration**. The
filtration-free candidates all fail to be equivalent: the ratio set is transverse (Section 3); global
state domination `phi o J <= C phi` requires `prod_k cond_k < inf`, which diverges even for Powers
factors at bounded conditioning (too strong); grading-twist **disjointness** (Kakutani/Araki:
quasi-equivalent iff `sum r_k^2 < inf`) is transverse too (MARG is disjoint with no wall -- verified).
So the slot is intrinsic to the **(algebra, state, grading, filtration)** quadruple, not to the
(algebra, state) pair. The filtration-sensitivity is consistent with (and predicted by) W103's CM1:
the tail data is direction/decomposition-sensitive. **The classical classification is grading-blind,
and that is exactly why it cannot see the wall: the obstruction is genuinely a property of the Krein
pairing, invisible to any positive-state invariant.** This sharpens the "typed external slot" reading
(the wall is not reducible to standard state data) while denying it the full algebra-intrinsic upgrade
the candidate identity would have delivered.

---

## 5. Tail-class coherence: the interface glues across observers (Task 2)

**The setup is W98 T6's own:** shared overlap modes, region-dependent scalar modular weights
`w_O1 = 1.0`, `w_O2 = 0.45` rescaling the coupling, so `r^1_k != r^2_k` on the same mode and the
operator-level conjugation data diverges. Computed (`W107` T7):

- **Operator level (W98 reproduced):** `||eta_1^{-1/2} - eta_2^{-1/2}||` on the overlap grows
  `11.0 -> 109.7` from `k = 1e3` to `1e5` -- the per-region `J`-data disagree, divergently.
- **Quotient level (new):** `||eta(r^1_k) - eta(r^2_k)|| = |r^1_k - r^2_k|` **exactly**, and it falls
  `2.7e-3 -> 2.8e-6`: the difference is **compact**. Both region metrics converge to the **same**
  `2P`, and both obstructions die on the **same** Krein-null essentially-complex line `e_null`
  (overlap `1 - 1e-9`). Hence
  > `[C_O1]|_overlap = [C_O2]|_overlap = 2[P]` -- **one singular class, one null line, one typed
  > slot, shared by both observers.**

**The reading:** the firewall's INTERFACE structure (the quotient class, its location, its typed
external requirement) is **observer-coherent**; only the God's-eye conjugation operator is not. This
is the P2-restoration W103 scoped: `P2` broke at the operator level (`W98`), and it is **restored at
the interface level** -- the same one-sided pattern as the flow/conjugation split, now across regions.
Combined with the W103 slot: the two observers do not share a `J`, but they provably need the **same**
external completion.

**Adversary (b) ("agreement is automatic/trivial") -- refuted by two controls:**

- **Control 1, rotation (`W107` T8) -- the discriminating case asked for:** a region whose modular
  frame is **rotated** (`theta_2 = pi/2 + 0.9`) has **identical eigenvalues at every mode** -- the
  same break, the same conditioning divergence, an operator disagreement just as before -- but the
  metric difference stays `>= 0.87` (NOT compact), the tail projections differ by
  `||P - P_theta|| = 0.43`, and the **classes DISAGREE** (distinct null lines). So class coherence is
  a falsifiable property, and the actual model falls on the **cohere** side for an identifiable
  reason: W98's region-dependence enters as a **scalar modular weight** (strength only); the mixing
  **direction** is fixed by the field content (the W52 metric form), not by the region. That
  direction-fixedness is **load-bearing assumption 1** (named; it is the same fixed-direction
  assumption W103's CM1 already isolated).
- **Control 2, weight collapse (`W107` T9):** a modular weight vanishing UV-fast
  (`w_2(k) = 1/(1+k^2)`) makes region 2 UV-soft on the overlap: `[C_O2]` invertible vs
  `[C_O1] = 2[P]` singular -- **maximal class disagreement**. Coherence needs the weights **bounded
  below** -- **load-bearing assumption 2** (named; W98's weights are `O(1)` constants, so the model
  satisfies it).

---

## 6. Verdicts, confidence, path

**T1 VERDICT: PARTIAL.**
- The candidate identity (`cond -> inf <=> 0 in the Krein ratio invariant`) **FAILS in both
  directions** with explicit in-model counterexamples; the wall is fully transverse to the classical
  ratio-set/type invariants. The intended upgrade -- the wall as an invariant of the (algebra,
  grading) pair via the ratio set -- is **dead as posed**.
- What survives is strong and exact: the physical tower is intrinsically the **hyperfinite III_1
  factor** (AQFT-consistent), and the wall equals **the unboundedness of the relative modular data
  between the metric-state and its grading twist** (per-mode norm = cond exactly; flow/conjugation
  split = cocycle-continuation split). The slot is intrinsic to (algebra, state, grading, filtration);
  it is **provably invisible to grading-blind (classical) invariants** -- which sharpens, rather than
  refutes, the "typed external interface" reading, at the cost of keeping the grading and filtration
  as irreducible inputs.

**T2 VERDICT: CLASSES-COHERE.** On W98's own overlap configuration the per-region tail classes,
null lines, and slot types agree exactly while the operator data diverges -- and the two controls
show this is a property with a describable failure mode (rotated frames; collapsing weights), not a
compact-difference tautology. The adapter reading **strengthens**: the interface is
observer-coherent; only the conjugation is observer-relative.

**Confidence.** Per-mode identities and both controls: **HIGH** (exact + machine-verified, 10/10).
Type assignments: **MEDIUM-HIGH** (standard Araki-Woods criteria, computation-grade III_1 density
argument). Metric-as-state fork: **MEDIUM** (canonical given W52, but a modelling identification).
Beyond-surrogate extrapolation: **LOW-MEDIUM**. Overall T1 PARTIAL: **HIGH** (the counterexamples are
explicit); T2 CLASSES-COHERE: **HIGH in-model**, **MEDIUM** as a statement about GU regions (rides on
the two named assumptions).

**Path (scoped, not done):** (i) decide the fixed-direction assumption -- is the mixing direction
forced by the W52 intertwiner construction across regions, or can interacting modular data rotate the
doublet frame region-dependently? (this single question now gates BOTH the W103 CM1 delimitation and
the T2 coherence); (ii) the filtration-free form of the repaired identity -- whether "sup of local
relative-modular norms over a filtration" can be replaced by an invariant of the grading automorphism
alone (e.g. via the flow of weights of the CROSSED PRODUCT by the grading, which is where a
Z_2-action's relative data becomes algebra-intrinsic) -- that is plausibly the correct successor to
the failed candidate identity and is frontier-grade; (iii) the genuine-III_1 version of T2 (the
surrogate's compact ideal again).

## 7. What this does NOT do

No GU claim-status, `CANON.md`, `RESEARCH-STATUS.md`, verdict, or public-posture change; no external
action; literature read-only. The `W98` break, the `W100` IFF, and the `W103` PARTIAL all stand
unchanged; H61/H61a remain **OPEN**. This branch **presents, does not decide** -- it hands the
orchestrator: the well-defined Krein-graded ITPFI tower (adversary (a) answered, signed alternative
degenerate), the III_1 identification of the physical tower, the two-direction failure of the
candidate identity with the transversality table, the rate-dependence corollary against W103 T4, the
exact repaired grading-relative identity with its named filtration residual, the CLASSES-COHERE
result with both non-triviality controls and its two named assumptions, and the scoped path whose
sharpest single question is now the fixed-direction fork. Reproducible:
`tests/W107_krein_ratio_tail_coherence.py` (10/10, exit 0).
