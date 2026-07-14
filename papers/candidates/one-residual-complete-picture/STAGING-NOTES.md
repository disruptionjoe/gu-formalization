# Staging Notes: one-residual-complete-picture

**Candidate:** `one-residual-complete-picture-2026-07-11.md`
**Companion:** `figures/FIGURE-ASSETS.md` is figure-source planning only and should be checked against the
current W127 body before use.

## Scope

This candidate stages the one-residual synthesis paper: a geometry-agnostic framing in which a geometric
framework accommodates the known sectors at honest grade while localizing remaining freedom in one
source-action declaration. GU is the concrete carrier, but the strongest thesis is not "GU is proven" or "all
physics is derived"; it is that the residual choices across gauge-vacuum selection, gravity soldering/scale,
fermion `C2`/generation count, and UV branch behavior are all controlled by the same source-action object.

The current staged body includes the 2026-07-13 three-wave consolidation folded by W127: dark energy is now an
honest hard negative for the DESI CPL / CMB-calibrated distance-model route, the AF branch carries a native
tree-unliftable spin-0 tachyon, and the next closure object is sharpened to the covariant operator on `Y14`
against the 27-row source-action requirements spec.

## Honest grade

**Structural synthesis at honest grade.** The candidate is a paper-level synthesis of locally reproducible
sector checks, conditional theorems, no-go results, and explicit hard negatives. It does not promote any single
sector to a new claim status and does not turn compatibility or reconstruction-grade machinery into a GU
derivation.

Local anchors include:

- `tests/one-residual/forces_maxcompact_independent.py`,
  `tests/legs/forces_maximal_compact_is_sm.py`, `tests/one-residual/sm_pati_salam_stabilizer.py`,
  `tests/one-residual/sm_mirror_anomaly_free.py`, and
  `tests/one-residual/sm_so10_cubic_casimir_and_mirror.py` for the forces/SM existence and anomaly-trace legs.
- `tests/one-residual/qm_krein_unitary_repair.py` for the faithful-model Krein-unitary repair.
- `tests/wave1/` through `tests/wave10/` for the tree-level gravity conditional theorem and the genuine
  soldering-postulate boundary.
- `tests/wave45/H46B_referee_grade_desi_verification.py` and
  `tests/wave46/H46C_theta_star_cmb_calibration.py` for the dark-energy hard-negative update.
- `tests/W119_h59_frg_krein_negative_ratio.py`, `tests/W120_path2_target2_keepgrade_vs_clop.py`,
  `tests/W121_path2_target3_hypothesis_hardening.py`, `tests/W122_spin0_scalaron_auxfield.py`,
  `tests/W123_native_r2_sign_convention_audit.py`, `tests/W124_stageA_sunset_graded_vs_LW_CLOP.py`,
  `tests/W124_stageB_overlap_kite_cuts.py`, `tests/W125_built_candidate_assembly.py`,
  `tests/W125_sac4_subprincipal_built.py`, and `tests/W126_beyond4th_conformal_iisq.py` for the UV/loop,
  scalaron, and first source-action-build sharpening.

## Light staging gate

1. Title matches the theorem-grade core: PASS WITH BOUNDARY. The "one residual" headline is a localization
   thesis about the source-action object, not a derivation of GU or a solved theory.
2. No retracted or downgraded wording leaks in: PASS WITH ACTIVE SUPERSESSION NOTES. The W127 body carries the
   hardening pass, Wave 1-8 gravity update, and 2026-07-13 consolidation blocks that govern older body text.
   Any future line edit must preserve those supersession markers until the whole paper is harmonized.
3. External citations resolve: PENDING. The candidate names DESI/Planck, fourth-order-gravity, Krein/PT,
   source-action, and landscape/vacuum-selection literature, but this cleanup pass did not independently verify
   every bibliographic detail against primary sources.
4. Sharpest open issue acknowledged in-text: PASS. Section 6 names the forced/derived source action and the
   covariant operator on `Y14` as the closure object; the honest-negatives section names the AF-vs-AS fork and
   non-perturbative scalaron escape as the remaining thin escapes.
5. No overlap with another staged candidate: DELINEATED. This synthesis subsumes or cites several narrower
   staged packets as legs, especially `located-not-forced/`, `generation-number-boundary-odd-primary/`,
   `uv-structure-fourth-order-gravity/`, and `keep-and-grade-loop-cost/`. Those packets should not be treated
   as duplicate publications unless Joe decides a publication sequence.

## Open items

1. Harmonize older body sections and figure assets with the governing W127 consolidation so no superseded
   dark-energy, Branch-2A, gravity-scalar, or "four legs cleared" wording survives unmarked.
2. Verify external citations and prior-art deltas before any public posting, especially DESI/Planck,
   fourth-order gravity, Krein/PT, landscape/vacuum-selection, and source-action comparisons.
3. Decide the publication sequence against the narrower staged candidates; this synthesis may be the carrier,
   or it may remain a map that points to more focused papers.
4. Keep the AF-vs-AS branch fork, the non-perturbative scalaron escape, loop-level Krein positivity, and the
   `Y14` covariant-operator build as open until later work closes them.

## Before posting

Do not treat this staging note as a publication, submission, tag/release, DOI, arXiv, Zenodo, public-posture, or
claim-status authorization. On Joe's explicit go, run a dedicated publication-readiness pass over the synthesis
body, figures, references, and overlap plan against the narrower staged candidates.
