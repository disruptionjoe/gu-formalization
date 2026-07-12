---
artifact_type: exploration
status: exploration
created: 2026-07-11
wave: 35
title: "Source-action consistency carve (Phase 2 landscape assessment) -- parametrize the candidate GU source action by its finite coefficient data, impose ALL ledger constraints JOINTLY (causality for the first time WITH the rest), and map the allowed region. VERDICT: FAMILY, shape-dimension 1. NOT a forced POINT and NOT EMPTY. Causality (leakage=0) HAS a cure solution and is UNIQUE in the physical cure coordinate (g=1, the full ker-Gamma projection); it closes on BOTH carriers so it does NOT pick A/B. The residual continuous freedom is the gravity |II|^2-vs-|II_0|^2 ratio beta/alpha (bounded to a nonempty band by m2_eff+positivity), plus two free scales (mu_DW, alpha). BINDING = {causality (cure->point), count-selection (bit->B), m2_eff+positivity (bound the shape)}; REDUNDANT = {Krein [P,S]=0 auto-satisfied, soldering even-sector orthogonal}. The joint carve CONFIRMS H40: causality forces the cure, not the carrier. No kill, no forcing."
grade: "COMPUTED (exact, on the repo's verified Cl(9,5)=M(64,H) rep + exact rational/linear algebra): the gravity coefficient count 2 (rank-10 vs rank-1 Hessians on Sym^2(R^4)); the built VZ leakage C2=155.3625 reproduced; the causality carve (minimal cure basis leakage(g)=(1-g)C2 -> unique g=1; extended 3-basis leakage-map rank 1, lstsq residual 1.9e-12 -> nonempty, physical cure a point, 2 leakage-blind directions); Gamma so(9,5)-equivariance residual exactly 0 (cure closes on both carriers); the count-selection residues -42%3=0 / -38%3=1; the m2_eff window [5/6,5/4] nonemptiness; the per-constraint ablation dimension bookkeeping. ARGUED (structural / evidence tier): that a nonzero leakage is a genuine acausality on GU's Y14 (H40, cited not re-derived); the mapping of the m2_eff window to a beta/alpha band and the exclusion of the conformal edge by the Stelle m^2!=0 form; the cure-basis SIZE (a modeling choice standing in for the unbuilt higher-spin construction); the B-lean of the final constrain-vs-gauge bit (unchanged from H39/H40). Reconstruction-tier, internal. No canon promotion; the generation count stays OPEN; SG4 unchanged; GU is NOT killed and NOT forced by this carve."
depends_on:
  - tests/wave35/source_action_carve.py
  - explorations/wave17/H40-terminal-sourceaction-2026-07-11.md
  - tests/wave16/H39_sourceaction_kclass.py
  - tests/wave24/H45_H2_vs_II2_binary.py
  - tests/wave27/H48_self_dual_square_forcing.py
  - tests/wave22/H10_ppn_weak_field.py
scripts:
  - tests/wave35/source_action_carve.py
---

# Wave 35 -- the source-action consistency carve: is the allowed region a POINT, a FAMILY, or EMPTY?

Test: `tests/wave35/source_action_carve.py` (deterministic, no randomness, exact; 15/15 PASS, exit 0).

This is Phase 2 of the source-action landscape assessment, run as a **consistency carve** (bootstrap
style): parametrize the candidate GU source-action operator by its FINITE coefficient data, impose the
whole ledger of known constraints SIMULTANEOUSLY, and map the shape of the allowed region. It is not a
build -- no point is claimed to be "the" answer. The novelty against the priors is that H39/H40/H45/H48
each imposed the constraints one at a time; here **causality (the vanishing-leakage constraint) is
imposed JOINTLY with count-selection, positivity, Krein, the m2_eff window, and soldering for the first
time**, and each is ablated to see which actually binds.

## The parametrization (finite coefficient data)

- **`alpha, beta`** -- the two O(4)-invariant 4-derivative gravity densities. `|II|^2` (full-norm,
  rank-10 on `Sym^2(R^4)`) and `|H|^2` (trace-square, rank-1). H45/H48 establish there are exactly TWO
  such invariants. Candidate points: `beta = 0` (full `|II|^2`, Stelle, H45 lean) and `beta = -1/4 alpha`
  (conformal `|II_0|^2`, pure Bach, H48 uniqueness).
- **`g_cure`** -- the non-minimal RS cure-term strength (interpolates the minimal `M_D` to the ker-Gamma
  projected operator). Minimal structural basis = 1 coefficient; the constrain-vs-gauge choice is the
  discrete A/B bit, not a continuous coordinate.
- **A/B bit** -- the field-space declaration: carrier A (index `-42`) vs carrier B (index `-38`). Discrete.
- **`mu_DW`** -- the scale (free; cancels in dimensionless ratios).

## The four verdicts

### Q1 -- DIMENSION COUNT [COMPUTED]

- **Coefficients:** 4 continuous `{alpha, beta, g_cure, mu_DW}` + 1 discrete A/B bit. The gravity `2` is
  computed as the rank fork (`rank(|II|^2 Hessian)=10`, `rank(|H|^2 Hessian)=1` on `Sym^2(R^4)` -> two
  invariants). The cure `1` is the minimal structural basis (a modeling choice; see honest limits).
- **Equality constraints:** 2 -- causality fixes `g_cure`, and `mu_DW` is pure scale. **Naive region dim
  = 4 - 2 = 2** (the H48 coefficient-minus-constraint count).
- Count-selection fixes the **discrete** bit (not a continuous dim); the m2_eff window and positivity are
  **bounds** (they shrink the extent, not the dimension).

### Q2 -- THE CARVE: does causality have a cure solution? [COMPUTED, on the actual rep]

- **The trigger reproduces:** the built minimal `M_D` leaks, `C2 = ||Gamma M_D Pi_RS|| = 155.3625`,
  `Gamma Pi_RS = 0` (`1.1e-14`), `rank(Pi_RS) = 1664 = ker Gamma`.
- **Minimal cure basis (1 coeff):** with `O(g) = (1-g) M_D + g (Pi M_D Pi)`, the leakage is exactly
  `leakage(g) = (1-g) C2` (the projected term is killed by `Gamma Pi = 0`). Verified: `leak(0)=155.36`,
  `leak(1/2)=77.68`, `leak(1)=6.3e-14`. So **causality HAS a solution and it is UNIQUE: `g=1`, the full
  ker-Gamma projection.** The cure coordinate is fixed to a **POINT**, not a family, not empty.
- **Extended cure basis (3 coeffs):** building the leakage design matrix over
  `{Pi M_D Pi - M_D, Pi M_D Q + Q M_D Pi, Q M_D Q}`, its **rank is 1**, the least-squares residual is
  `1.9e-12` (solvable), and there are **2 leakage-blind directions**. So causality is genuinely ONE linear
  equation with a nonempty solution set; the physical (leakage-relevant) cure content is a point, and the
  extra cure directions are redundant gauge of the parametrization, not physical freedom.
- **Causality closes on BOTH carriers:** `Gamma` is `so(9,5)`-equivariant
  (`||Gamma J_i - sigma_i Gamma|| = 0` exactly), so `ker Gamma` (B) and the full space (A) are both
  cure-compatible submodules. **Causality fixes `g_cure` but is blind to the A/B bit** -- the joint-carve
  restatement of H40's "forces the cure, not the carrier."

### Q3 -- THE VERDICT: FAMILY, shape-dimension 1 [COMPUTED]

- **FIXED:** `g_cure` -> point (causality); A/B bit -> **B** by count-selection (`-42 % 3 = 0`,
  index-preserving, cannot select; `-38 % 3 = 1`, index-changing, selects).
- **BOUNDED (not fixed):** the gravity ratio `beta/alpha` lives in a nonempty band. The m2_eff window
  `[5/6, 5/4]` is nonempty and bounds the Einstein/Weyl ratio; positivity forces `alpha > 0`; the Stelle
  `m^2 != 0` form excludes the conformal edge `beta/alpha = -1/4` (H48) while the full-`|II|^2` lean sits at
  `beta/alpha = 0` (H45). This is the **live H45-vs-H48 tension**, and it is exactly the residual freedom.
- **FREE:** `mu_DW` (scale, H42 magnitude-free) and the overall gravity coupling `alpha > 0`.
- **VERDICT = FAMILY.** The region is NONEMPTY (all constraints jointly satisfiable on carrier B with the
  ker-Gamma cure -> GU is not killed here) and NOT a POINT (the `beta/alpha` ratio is a genuine bounded
  1-parameter freedom). Shape-space dimension **1** (the bounded gravity ratio), plus 2 free scales.

### Q4 -- WHICH CONSTRAINT IS BINDING [COMPUTED ablation]

Dropping each constraint and re-measuring the region:

| constraint | drop it -> | classification |
|---|---|---|
| causality | `g_cure` freed, free-cont `3 -> 4` | **BINDING** (the cure) |
| count-selection | both carriers live, discrete `1 -> 2` | **BINDING** (the A/B bit) |
| m2_eff window | `beta/alpha` unbounds | **BINDING** (bound; dim-preserving) |
| positivity | the degenerate `|H|^2`/`alpha=0` corner opens | **BINDING** (boundary) |
| Krein `[P,S]=0` | no change | **REDUNDANT** (auto-satisfied, 2-primary sign-blind) |
| soldering | no change to the odd-sector cure carve | **REDUNDANT** (even-sector, orthogonal) |

**The headline:** imposing CAUSALITY does **not** collapse the A/B freedom (count-selection does) and does
**not** collapse the soldering freedom (even-sector, orthogonal). The three constraints bind three
different coordinates: causality -> the cure (to a point); count-selection -> the carrier (to B);
soldering -> its own independent even-sector locus. H40's "forces the cure, not the carrier" survives the
joint carve for the first time.

## COMPUTED vs ARGUED ledger

- **COMPUTED (exact):** gravity coefficient count 2 (rank-10 vs rank-1 Hessians); `C2 = 155.3625`
  reproduced; the minimal-basis leakage law `leakage(g) = (1-g) C2` and its unique root `g=1`; the
  extended-basis leakage-map rank 1 with lstsq residual `1.9e-12`; the `Gamma` equivariance residual
  exactly 0 (cure closes on both carriers); count-selection residues `-42%3=0`, `-38%3=1`; the m2_eff
  window nonemptiness; the per-constraint ablation bookkeeping.
- **ARGUED (structural / evidence tier):** that a nonzero leakage is a genuine acausality on GU's `Y14`
  (H40, cited); the mapping of the m2_eff window to a `beta/alpha` band and the exclusion of the conformal
  edge by the Stelle `m^2 != 0` form; the cure-basis SIZE (a modeling choice); the B-lean of the final
  constrain-vs-gauge bit (unchanged from H39/H40).

## Honest limits (what this carve does NOT capture)

1. **The cure-basis size is a modeling choice, not a computed dimension.** The minimal basis (1 coeff)
   gives the cleanest carve -- causality fixes the cure to a point -- and the extended 3-basis confirms the
   leakage map is rank 1 regardless. But the TRUE cure-term space is fixed only by the **full higher-spin
   construction** (the unbuilt Porrati-Rahman / non-minimal RS coupling), which this carve stands in for.
   The result "causality fixes the physical cure coordinate to a point" is robust to the two bases tested;
   it is not a proof over every conceivable non-minimal coupling.
2. **The m2_eff -> beta/alpha map is argued, not derived here.** The window `[5/6,5/4]` (H10/H25) bounds
   the Einstein/Weyl ratio; the precise `beta/alpha` interval and the exclusion of the conformal edge are
   read off the Stelle-form structure, not recomputed on the full bundle in this file.
3. **The FAMILY is a landscape shape, not a physical spectrum.** The residual `beta/alpha` freedom is the
   `|II|^2`-vs-`|II_0|^2` choice (H45 P2), which is gated on the same unbuilt source action. The carve
   locates the freedom; it does not resolve it.
4. **This carve does not import the Phase-1 literature causality bounds.** It uses only the repo's internal
   VZ leakage as the causality condition; external Velo-Zwanziger / Porrati-Rahman causal-window bounds
   from Phase 1 are not injected.
5. **No forcing was manufactured and no kill was evaded.** The region is honestly a FAMILY: nonempty (not a
   kill) and not a point (not a forcing). The only exact "3" is `dim Lambda^2_+`; no target number is fit.

## RE-RANK signal

**The source-action allowed region is a FAMILY (shape-dimension 1), NOT a forced POINT and NOT EMPTY.**

- **Is GU killed?** No. All six ledger constraints are jointly satisfiable on carrier B with the full
  ker-Gamma cure. The region is NONEMPTY -- causality + count-selection + positivity + Krein + m2_eff +
  soldering are mutually consistent. **EMPTY is falsified.**
- **Is the keystone forced?** No. The cure strength and the A/B carrier bit ARE pinned (causality ->
  point; count-selection -> B), but the gravity `|II|^2`-vs-`|II_0|^2` ratio `beta/alpha` is a genuine
  bounded 1-parameter residual, plus two free scales. **POINT (forced up to scale) is falsified.**
- **Which physics binds?** Causality binds the cure (to a point) and ONLY the cure; count-selection binds
  the carrier bit; the m2_eff window and positivity bound the gravity shape; Krein `[P,S]=0` and soldering
  are redundant to this carve. This is the first time causality has been imposed JOINTLY with the rest, and
  the outcome CONFIRMS rather than revises H40: **causality forces the cure, not the carrier.**
- **The single next object is unchanged:** the source action's causal-cure term (the non-minimal RS
  coupling), built so as not to p-hack the carrier. The carve shows that term is fixed to a point by
  causality in every basis tested -- so the residual freedom that a forced build must still settle is the
  gravity `beta/alpha` ratio (the H45 P2 / H48 uniqueness fork), not the cure and not, by causality alone,
  the carrier.
- **No canon movement, no generation-count movement.** SG4 unchanged; the generation count stays OPEN; the
  one-residual framing is unchanged, sharpened in one phrase: the terminal object's allowed region is a
  mapped FAMILY (shape-dim 1), with causality binding only the cure.

---

*Filed 2026-07-11. Wave 35, the source-action consistency carve (Phase 2 landscape). Reproducible:
`python -u tests/wave35/source_action_carve.py` (exit 0, 15/15 PASS). Exploration-grade; not promoted to
canon. Adversarially graded: EMPTY was tested for and falsified (region nonempty), POINT was tested for
and falsified (gravity ratio is a bounded residual), no forcing was manufactured, and the only exact `3`
is `dim Lambda^2_+`. The honest outcome: a FAMILY of shape-dimension 1, causality binding the cure to a
point but not the carrier, GU neither killed nor forced by the joint carve.*
