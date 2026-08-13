---
artifact_type: exploration
label: "DE certification REDO (Wave A-2 rebase, hostile-review spec): synthetic-injection positive control + the five-map c_kin composition ledger"
created: 2026-08-03
status: exploration
posture: adversarial; truth-seeking; preregistered before computation; no verdict movement
title: "Synthetic-injection unbiasedness control for the theta_star+BAO pipeline, and the explicit W230-to-FLRW composition map with its first unbuildable arrow"
grade: "DETERMINISTIC NUMERICAL + EXACT RATIONAL CERTIFICATE / hostile-review rebase / claim_status_change: none"
canon_verdict_change: none
hostile_review_status: "executes the redo the 2026-08-03 Wave A-2 hostile review requires; its seven absorbed findings are the spec"
verdict_gate: "Pre-deposit, J5-gated. No bar, verdict, canon claim, count, H59, or LANE-STATE entry moves here. C10 and M-H13 gate status update only via the register (reported, not edited). The native record law and the native Z_U remain unbuilt regardless of every outcome below."
kill_conditions_declared_before_computation: true
depends_on:
  - lab/process/hostile-reviews/2026-08-03-wave-a2-cosmology-bridge-review.md
  - lab/process/anchor-council-2026-08-03/seat2-cosmology.md
  - lab/process/CURRENT-RESEARCH-CONTEXT.md
  - explorations/de-pipeline-certification-and-bridge-test-2026-08-03.md
  - explorations/W230-close-a4-derive-w154-2026-07-14.md
  - explorations/W203-branch3-source-action-fixed-coefficients-2026-07-14.md
  - canon/theta-field-flrw-dark-energy-eos.md
  - canon/dark-energy-theta-divergence-free.md
  - tests/wave25/H44_de_backreacted_background.py
  - tests/wave29/H46_de_raw_bao_likelihood.py
  - tests/wave45/H46B_referee_grade_desi_verification.py
  - tests/wave46/H46C_theta_star_cmb_calibration.py
  - tests/de-certification/de12_theta_star_positive_control.py
scripts:
  - tests/de-certification/de12b_synthetic_injection_positive_control.py
  - tests/de-certification/w230_flrw_composition_first_arrow.py
---

# DE certification redo: synthetic injection + the composition-map ledger

This artifact executes the two tasks the 2026-08-03 Wave A-2 hostile review
(`lab/process/hostile-reviews/2026-08-03-wave-a2-cosmology-bridge-review.md`)
left open after absorbing its seven findings:

1. **Finding 5 killed the in-sample DE-12 control.** The reported DESI `w0wa`
   row was selected from the same data, so DE-12 could not certify pipeline
   unbiasedness or C10. The replacement is a SYNTHETIC-INJECTION design: mock
   BAO data vectors from KNOWN truth cosmologies never fitted to DESI, noise
   from the byte-verified 13x13 DR2 covariance, pushed through the identical
   theta_star-calibration + likelihood machinery.
2. **Findings 1-4 leave the FLRW scalar `B` vs W230's connection distortion
   `UNCERTAIN` as the same object** because five maps (observation, pullback,
   projection, normalization, equation) were never composed. Section 3 composes
   them explicitly on paper, states which are defined by existing artifacts,
   and identifies the FIRST arrow that is unbuildable with current objects.
   The review predicts the native `Z_U = |D_A U|^2` contribution is the
   blocker; that prediction is the preregistered hypothesis.

The preregistration below (Section 1) was written BEFORE either script was
written or run. Results are appended after it, unedited above the marker.

## 0. Layer-0 typing (before use; per the standing rule)

| Term | Type | Ruling for THIS artifact |
|---|---|---|
| "positive control" | **REDEFINED HERE (synthetic)** | Truth cosmologies are chosen a priori on a grid, disjoint from every H46B-verified DESI fit row. The DESI DR2 MEAN VECTOR is never used to generate or select anything; only the covariance (the instrument model, not the signal) enters, as the noise law and the chi^2 metric. This answers finding 5's in-sample objection at the signal level. |
| "unbiasedness" | **DEFINED (operational)** | Over noise realizations: the pipeline assigns the injected truth dAIC ~ 0 against itself (no self-exclusion), recovers its amplitude with bias small vs sigma_A, reproduces the noiseless shape gaps in the mean (no shape-statistic bias), and ranks wrong models by their true noncentrality. Nothing more: the control certifies the REDUCED pipeline (fixed early physics, omega_m h^2 fixed, amplitude + amplitude-marginalised shape statistics), not a full posterior analysis. |
| theta / B | **UNCERTAIN (same-object), per the review** | Unchanged. Section 3 is ABOUT this typing; nothing below assumes it. |
| c_kin, L | **PLACEHOLDER / native map UNBUILT** | Unchanged from the review. The exact-rational script certifies criterion-level algebra (the ray condition; the k=0 block typing) on declared fixtures; it does not build the native operator. |
| N(z), record law | **NOT USED** | No record-law object appears in this artifact. M-H13's native construction burden is untouched. |
| "fibre" | **HOMONYM (flagged)** | W230's finite fixture lives on the 14-dim (9,5) FRAME direction space; the FLRW mode B lives on functions over the GL(4,R)/O(3,1) METRIC fibre (rc3 spectrum). These are different objects; Section 3 arrow A3 carries the fence. |

Construction fork (GEOMETER-VS-PHYSICS-OBJECTS.md): Section 2 is entirely
standard-field likelihood statistics wrapped around the wave45/46 machinery
under test; Section 3 is a typing/composition exercise on the program-native
objects, with the standard-field FLRW reduction as the target. Hygiene:
nothing under `tests/channel-swings/pw2*` or `papers/candidates/` is touched;
nothing is committed by this agent; the resolver campaign's files are not
touched.

## 1. PREREGISTRATION (written before computing)

### 1.1 Synthetic-injection control (script: de12b_synthetic_injection_positive_control.py)

**Design.** Truth cosmologies, declared a priori and disjoint from the four
H46B `P1_CPL` DESI fit rows {(-0.42,-1.75), (-0.838,-0.62), (-0.667,-1.09),
(-0.752,-0.86)}:

- T0: LCDM (w0, wa) = (-1, 0)
- T1: (-0.8, -0.5)
- T2: (-1.2, +0.4)
- T3: (-0.7, +0.3)
- T4: (-1.05, -0.9)  (deliberately near-degenerate with other truths at low z,
  to exercise the resolvability floor honestly)

Each truth is generated SELF-CONSISTENTLY with the pipeline's frozen early
physics: at fixed omega_m h^2 = 0.1430, solve theta_star(h) = 1.04110 for h
with a GENERATOR-SIDE integrator numerically independent of the evaluator
(adaptive quadrature per BAO row + Simpson calibration integrals vs the
evaluator's fixed-grid trapezoid), apply the generator's own A3 LCDM ratio
correction, and set the truth amplitude A_T = (c/H0_T)/r_drag. The noiseless
mock mean is the truth's 13-element DESI-ordered BAO vector; noise is drawn
`N(0, C)` with C the byte-verified 13x13 DR2 covariance (Cholesky,
`numpy` default_rng, seed 20260803), NREAL = 400 realizations per truth.
Physics conventions (A1 additive radiation in all fresh-frame rows, A3 ratio
correction, frozen Planck digits) are SHARED generator/evaluator by design:
the control certifies the pipeline against its own declared conventions; the
numerics are independent so the certificate is not circular at the
implementation level. The DESI mean vector is never touched.

Evaluation models per mock: the five truths (each at its OWN theta_star-
calibrated amplitude, computed once, data-independently, by the byte-imported
DE-12 fresh machinery) plus GU (M^2 = 8, f0 = 0.125) through the identical
H46C machinery with the A3 correction (GU rows get the same A1 radiation term
as every other fresh-frame row; deviation from the DE-12 CONTRAST row noted,
shared-systematic-removing).

**Preregistered pass/fail thresholds (hard asserts; exit couples).** Exact
sampling theory under the linear-Gaussian model: chi^2(A_cal) ~ chi2_13
against the own-truth mock; d_self = chi^2(A_cal) - chi^2_marg ~ chi2_1;
chi^2_marg(truth) ~ chi2_12; A*_hat ~ N(A_T, sigma_A^2); for a wrong model M,
E[chi^2_M - chi^2_T] = Delta_TM (the noiseless noncentrality) and
E[chi2_marg_M - chi2_marg_T] = lambda_TM (the noiseless marginalised gap).
Bands are ~4-5 sigma of the NREAL = 400 sampling error.

- **SI-1 (noiseless self-recovery; generator/evaluator independence).** For
  every truth: chi^2 of the evaluator's truth model (at its own calibrated
  amplitude) against the noiseless mock mean < 0.05, and the amplitude gap
  |A_eval - A*_hat(noiseless)| / sigma_A < 0.10.
- **SI-2 (dAIC ~ 0 against itself: no self-exclusion).** For every truth:
  |mean d_self - 1| < 0.35 (4.9 sigma at NREAL = 400); equivalently
  mean dAIC_self = mean d_self - 2 in (-1.35, -0.65), asserted inside (-2, +2)
  (the "~ 0", not-decisive AIC band); and |mean chi^2(A_cal) - 13| < 1.2.
  FAILURE IS LOUD: the pipeline manufactures a spurious exclusion for a truth
  it was handed, and every number in the wave45/46/W129 chain is suspect.
- **SI-3 (amplitude + shape-statistic unbiasedness, per truth).** For every
  truth: |mean A*_hat - A_T| / sigma_A < 0.25 (5 sigma), and
  |mean chi^2_marg - 12| < 1.2.
- **SI-4 (ranking).** For every ordered pair (truth T, model M != T) with
  noiseless Delta_TM >= 2 (the resolvability floor): mean(chi^2_M - chi^2_T)
  > 0 AND |mean - Delta_TM| < max(0.25, 5 SE_emp); the fraction of
  realizations preferring the truth >= 0.60. For pairs with Delta_TM >= 25:
  that fraction >= 0.95. Pairs below the floor are reported, not asserted.
- **SI-5 (shape-gap unbiasedness — the review's requirement (b)).** For every
  ordered pair: |mean(chi2_marg_M - chi2_marg_T) - lambda_TM| <
  max(0.5, 5 SE_emp). The recovered shape statistic must reproduce the
  injected shape gap in the mean, at every injected truth.
- **SI-6 (the exclusion contrast responds to real mismatch).** GU's noiseless
  noncentrality Delta_GU(T) >= 9 for every injected truth, and for truths with
  Delta_GU >= 25 the fraction of realizations ranking GU worse than the truth
  >= 0.95. This certifies that the machinery's large exclusion numbers arise
  from genuine shape/amplitude mismatch on data of KNOWN truth, not from a
  pipeline artifact.

**What a full pass licenses (and what it does not).** PASS of SI-1..SI-6 =
the pipeline-unbiasedness certificate that DE-12 could not supply: the
theta_star+BAO reduced pipeline, applied to data whose truth is known and
whose noise is the byte-verified DR2 covariance, neither excludes injected
truths nor biases the recovered shape statistic, and ranks wrong models by
their true noncentrality. This is the certificate C10 needs (seat4 JP5/JP6).
It does NOT move C10's or M-H13's register status (register-owned; reported
below), does not validate the GU background solver's physics, and does not
touch the native record-law burden.

### 1.2 Composition-map question (script: w230_flrw_composition_first_arrow.py)

**Preregistered hypothesis (H-ARROW, from review finding 2).** Writing the
five maps in composition order — observation, pullback, projection,
normalization, equation — the FIRST arrow not definable from existing
artifacts is the one requiring the native gradient term
`Z_U = |D_A U|^2` (the connection Laplacian `D_A* D_A`), i.e. the
normalization/kinetic-split arrow. Decision procedure: for each arrow, name
the defining artifact or the missing object; the first arrow with a missing
required object is the finding, whether or not it matches the prediction.

**Preregistered cheap computations (exact/certified per P-H29; no FD reads).**
All in exact rational arithmetic (`fractions.Fraction`):

- **[EXACT-8]** lambda_{N,1} = (9/2)^2 - (7/2)^2 = 8 exactly (the repo's M^2
  is a fiber-gradient eigenvalue; rc3/canon lines).
- **[EXACT-K0]** In a properly-typed separable gradient model (base-time
  block ⊗ base-space Fourier sector ⊗ fibre ground mode), the k -> 0
  homogeneous limit annihilates EXACTLY and ONLY the base-spatial sub-block;
  the base-time block and the fibre eigenvalue are exactly k-independent, and
  the separable oscillator identity omega^2 = (c_f/c_b) lambda_1 holds in
  exact rationals. Expected consequence: seat2's k = 0 caveat cannot decide
  the c_kin question; only building Z_U can.
- **[EXACT-RAY]** The review's finding-3 criterion made exact: on a declared
  SPD integer fixture, (i) every L in the proportional family c M preserves
  the target ray with residual EXACTLY zero; (ii) the non-proportional
  planted witness L = M + (Mt)(Mt)^T ALSO preserves it exactly (strictly
  sharper than the review's L = M); (iii) a generic integer perturbation
  breaks it with an exactly nonzero 2x2 minor; (iv) the same holds through
  the full field equation theta(c) = (m^2 M + c L)^{-1} kappa J solved in
  exact rationals. This upgrades the finite-fixture ray criterion from float
  tolerance to certificate grade.

Repo-consistency asserts tie the ledger to artifact text (W203's `Z_U`
NOT-BUILT row; W230's naming of `c_kin L = D_A* D_A`; H44's `B''` equation
string), so silent drift in any cited artifact fails the script.

<!-- RESULTS APPENDED BELOW AFTER THE RUNS; PREREGISTRATION TEXT ABOVE UNEDITED -->

## 2. Results (appended after the runs; preregistration above unedited)

Both scripts exit 0 under pinned `numpy`/`scipy` execution, deterministic
(seed 20260803).  EVERY preregistered threshold held on the first run; no
threshold was adjusted post hoc.

### 2.1 The synthetic-injection control (de12b): PASS, all SI-1..SI-6

Machinery certificates: evaluator LCDM theta* matches H46C to `1.7e-7`
relative; generator and evaluator LCDM calibrations agree to `5e-6` in `h`
(each frame divides out its own A3 systematic); GU calibrates to
`h = 0.63749`, reproducing the stored H46C row.

| truth (w0, wa) | noiseless self chi2 | mean d_self (chi2_1: 1) | mean dAIC_self | mean chi2_marg (chi2_12: 12) | A-bias / sigma_A |
|---|---:|---:|---:|---:|---:|
| T0 LCDM (-1.00, 0.00) | 0.0000 | 0.993 | -1.007 | 11.685 | +0.032 |
| T1 (-0.80, -0.50) | 0.0000 | 1.100 | -0.900 | 11.924 | +0.018 |
| T2 (-1.20, +0.40) | 0.0000 | 1.050 | -0.950 | 12.429 | +0.026 |
| T3 (-0.70, +0.30) | 0.0000 | 0.979 | -1.021 | 11.873 | +0.014 |
| T4 (-1.05, -0.90) | 0.0000 | 0.931 | -1.069 | 12.001 | -0.004 |

- **SI-1**: noiseless self-recovery exact to the displayed precision at every
  truth; amplitude gap <= 0.001 sigma_A (generator/evaluator numerics
  genuinely independent, agreement not circular).
- **SI-2**: no self-exclusion anywhere; `mean d_self` sits on the exact
  chi2_1 expectation at every truth; `dAIC ~ 0` band satisfied.
- **SI-3**: amplitude bias <= 0.032 sigma_A; marginalised shape statistic on
  the chi2_12 expectation at every truth.
- **SI-4**: all 18 above-floor ordered pairs pass all bands; the mean
  recovered separation matches the noiseless noncentrality (e.g. T3<-T4:
  injected 1080.50, recovered 1079.99 +/- 3.21).  The two below-floor pairs
  (T0<->T1, Delta = 1.48) are reported unasserted per preregistration
  (truth preferred in 69-74% of realizations).
- **SI-5** (the review's requirement (b)): all 20 ordered pairs reproduce the
  injected amplitude-marginalised shape gap in the mean, within band; no
  systematic bias in the recovered shape statistic at any injected truth.
- **SI-6**: GU (M^2 = 8, f0 = 0.125) shows noiseless noncentrality 15.0 /
  16.0 / 28.1 / 326.0 / 235.7 against T0..T4 and is ranked worse than the
  truth in >= 96.8% of realizations everywhere (100% where Delta >= 25): the
  machinery's exclusion-scale numbers arise from genuine mismatch on data of
  KNOWN truth.

**Licensed statement.** The theta_star+BAO reduced pipeline, fed data whose
truth is known and whose noise is the byte-verified DR2 covariance, does not
exclude injected truths, does not bias the recovered amplitude or
amplitude-marginalised shape statistic, and ranks wrong models by their true
noncentrality.  This is the pipeline-unbiasedness certificate the hostile
review required in place of DE-12's in-sample reading, and it is the
certificate C10's quantitative hook was waiting on (seat4 JP5/JP6).  Fence:
it certifies the MACHINERY, not the value of the +19.3 gap (a DESI-data
statement, recomputed on-disk as 19.346 by the repaired mh13 script), and it
does not edit C10's or M-H13's register status.

### 2.2 The composition-map script (w230_flrw_composition_first_arrow): PASS 17/17

LED 6/6 (ledger shape + repo-text ties), EXACT-8, K0 5/5, RAY 5/5, all in
exact rational arithmetic (no floats on any decisive claim; P-H29 satisfied
by construction).  Headline exact results:

- `lambda_{N,1} = (9/2)^2 - (7/2)^2 = 8` exactly.
- k -> 0 annihilates EXACTLY and ONLY the base-spatial sub-block of a
  properly-typed separable gradient operator; the base-time block and the
  fibre eigenvalue are exactly k-independent; `omega^2 = (c_f/c_b) lambda_1`
  exactly.
- The ray criterion at certificate grade: the proportional family `c M`
  preserves the target ray exactly; the NON-proportional planted witness
  `L = M + (Mt)(Mt)^T` also preserves it exactly (strictly sharper than the
  review's `L = M`); a generic integer perturbation breaks it with an exactly
  nonzero minor (`-210/89` on the declared fixture); all verified through the
  full field equation solved over Fractions.

## 3. The composition-map ledger (the on-paper attempt)

Target: compose native W230 objects into H44's FLRW equation
`B'' + (3 + H'/H) B' + (M^2/H^2) B = 0` and find the first arrow that cannot
be built with current objects.  Review finding 1 names the five maps.

**A1 OBS (observation / identification of the DE field).**
`theta = pi - eps^{-1} B eps`, the connection distortion of the inhomogeneous
gauge group.  DEFINED: `canon/dark-energy-theta-divergence-free.md` Section 1
(the 2026-06-22 proof); W230 types it Psi-INDEPENDENT ([MISMATCH]).  The W230
finite fixture models its value space as R^14 with the equivariant Krein
kernel `M = Gram`.  Nothing beyond the object's name is needed at this arrow.

**A2 PULL (pullback / cosmological restriction).**
`s: X4 -> Y14 = Met(X)` is the FLRW metric point of GU's arena; the
restriction `s* theta` of the VALUE of theta is well-typed given A1.
DEFINED-CONDITIONAL: no artifact computes it, and nothing obstructs it.  Note
recorded for A4: the ACTION needs the first jet of theta (base and fibre
derivatives), not just the value; that requirement is deferred to the arrow
where its operator lives.

**A3 PROJ (projection to the scalar mode).**
The fibre over each x is `GL(4,R)/O(3,1)`;
`rc3-delta-n-spectrum-gl4r-2026-06-23.md` (reconstruction) supplies the
normal-Laplacian spectrum with ground eigenvalue `lambda_{N,1} = 8/R_s^2`,
and the canon sets `M_KK = 2 sqrt(2) H0` from it.  `B(t) := <theta(s(t)), Y_1>`
with `Y_1` the ground mode.  RECONSTRUCTION-GRADE.  **Layer-0 fence (the
honest content of findings 1-2):** the W230 fixture's 14 directions `e_a`
are FRAME directions of the (9,5) tangent model, NOT functions on the metric
coset; no artifact identifies the two decompositions, so every finite-fixture
number (alignments, block tables) transports to the FLRW mode only through
that unproven identification.

**A4 NORM (normalization / kinetic split).  <- FIRST UNBUILDABLE ARROW.**
To write a reduced action for `B` one must evaluate the native kinetic
quadratic form on the configuration `theta = B(t) Y_1(y)` along `s`.  The
native kinetic form is `Z_U = |D_A U|^2` (W203 Section 5; the connection
Laplacian `D_A* D_A` is W230's `L` referent).  Required outputs: the block
coefficients `(c_b : c_s : c_f)` of `Z_U` along the A2/A3 splitting
(base-time / base-space / fibre), then the normalization `B -> B / sqrt(c_b)`.
W203's coefficient ledger row: `Z_U` **NOT BUILT** (machine-tied, LED3).  No
other artifact carries a native gradient operator for theta.  W230's `c_kin`
collapses this three-way split into ONE scalar on an ultralocal fixture with
no base manifold at all -- which is exactly why finding 2 called it a
placeholder.  The review's prediction is CONFIRMED: the native `Z_U`
contribution is the precise blocker, located at the normalization arrow.

**A5 EQ (equation).**
Given `(c_b, c_s, c_f)` and the geometry-forced source coupling
`<theta, J>` (W203 [COEF]), the Euler-Lagrange equation on FLRW at k = 0 is
`c_b B-ddot + 3 H c_b B-dot + c_f lambda_1 B = kappa (J-projection)`.  H44's
equation is the special normalization `c_b = 1`, `c_f lambda_1 = M^2 = 8`,
source dropped.  DEFINED-CONDITIONAL (mechanical given A4).  Consistency
notes, both absorbed from the review: H44's massless-fibre toy is
`(c_b, c_f) = (1, 0)`, not simultaneous removal (finding 4); and any future
necessity theorem must carry the exact escape variety `L t in span(M t)`,
which now has a certificate-grade NON-proportional member (finding 3,
upgraded by [EXACT-RAY]).

**What the k = 0 computation decides, exactly.**  [EXACT-K0]: homogeneity
annihilates exactly and only `c_s`; both `c_b` (through `B''`) and
`c_f lambda_1 (= M^2)` survive at k = 0.  Seat2's Section 1.4 caveat ("W230's
L is a spatial-gradient stand-in and the FLRW mode is homogeneous, where a
gradient term vanishes regardless") therefore dissolves the tension ONLY
under the additional unproven premise that the native `Z_U` maps purely into
the base-spatial sub-block -- and that premise is precisely arrow-A4 content.
Consequence for seat2 Section 4.1's three-way split: outcome (a) "bridge
fails as stated" is NOT licensed; the correct state is **BLOCKED-ON-A4**.
The question "does c_kin = 0 conflict with the FLRW kinetic term?" is not
decidable with current objects; it becomes decidable exactly when `Z_U`'s
block split is built.  The cheapest decisive move is now precisely named:
build the `(c_b : c_f)` ratio of `Z_U` on the A3 configuration -- not another
fixture.

**Effect on M-H13, stated conditionally.**  If `Z_U` yields `c_b > 0`, the
identity `theta ~ M^{-1} J` fails generically by W230 [NEC], with the exact
escape variety now named (a nonzero-measure-zero variety containing
non-proportional SPD members); if `c_b = 0`, the theta sector loses its FLRW
oscillator (the PIPE rows) and the object M-H13 would refit does not exist.
Either way M-H13 stays gated on A4, not on more fixture work.

## 4. Disposition and report

**Citable from this artifact:**
1. The theta_star+BAO reduced pipeline is UNBIASED on synthetic
   known-truth injections with DR2-covariance noise (DE-12b, exit 0; five
   a-priori truths x 400 realizations; SI-1..SI-6 all preregistered and all
   passed).  This supplies the independent positive control / unbiasedness
   certificate that review finding 5 found missing, i.e. the certificate C10
   needs.
2. The first unbuildable arrow of the W230 -> FLRW composition is A4 NORM:
   the kinetic split `(c_b : c_s : c_f)` of the unbuilt native
   `Z_U = |D_A U|^2` (review finding 2's prediction CONFIRMED, machine-tied
   to W203's ledger row).  The k = 0 escape is exactly typed and cannot
   decide the c_kin question; the ray criterion's iff boundary is
   certificate-grade with a non-proportional exact preserver.

**Not citable / unchanged:** any bridge-failure or M-H13 no-go (the state is
BLOCKED-ON-A4); the native record law; the value +19.3 as anything other than
a DESI-data statement; C10 or M-H13 register status (register-owned).

**REPORT to the register owner (no edits made here):** the M-H13 rider's
item (b) (pipeline positive control) is now discharged by the
synthetic-injection design; item (a) (the W230 c_kin<->FLRW mapping question)
is sharpened from "uncertain tension" to BLOCKED-ON-A4 with the decisive
object named (`Z_U`'s `(c_b : c_f)` block ratio on the A3 configuration).
Register/LANE-STATE updates are the orchestrator's.

No external datum is selected, consumed, or changed by this artifact.  The
DESI DR2 mean vector is never read by the injection control; only the
covariance enters, as noise law and metric.
