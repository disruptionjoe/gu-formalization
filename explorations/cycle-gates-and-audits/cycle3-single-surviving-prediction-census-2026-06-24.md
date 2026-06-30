---
title: "Cycle 3 Single Surviving Prediction Census"
date: "2026-06-24"
status: exploration/census
doc_type: cycle3_single_surviving_prediction_census
verdict: "NO_CURRENT_CONCRETE_SURVIVING_EMPIRICAL_PREDICTION"
owned_path: "explorations/cycle-gates-and-audits/cycle3-single-surviving-prediction-census-2026-06-24.md"
audit:
  - "tests/cycle3_single_surviving_prediction_census_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "lab/process/runbooks/five-lane-frontier-run.md"
  - "lab/roadmap/objection-triage-register.md"
  - "NEXT-STEPS.md"
  - "explorations/cycle-gates-and-audits/cycle1-generation-rs-rank-direct-gate-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/cycle2-source-forced-s-ig-dyn-action-gate-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/cycle2-source-critical-rank-one-psb-selection-certificate-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/cycle2-qft-physical-field-positive-pairing-seed-2026-06-24.md"
---

# Cycle 3 Single Surviving Prediction Census

## 1. Verdict

**Verdict: no current candidate qualifies as a concrete surviving empirical
prediction.**

The repo has several sharp candidate tests, but every live candidate is still
reconstruction-grade, control-only, source-dependent, or conditional on a
missing proof object. The older `gu-testable-predictions-2026-06-23.md` file
ranked dark-energy EOS and generation count as predictions. Later Cycle 1/2/3
artifacts demote the load-bearing inputs:

- generation count is open because neither `rank_H=4` nor `rank_H=8` is
  source-derived for the physical RS projector;
- dark-energy EOS is open because `xi_eff`, `Z_theta`, and `C_Rtheta` are not
  generated from a source-forced action;
- VZ/causality is a conditional consistency gate, not an empirical prediction;
- anomaly/chirality is only relative or partial until the full observer shadow
  is selected and checked;
- QFT state-space and CHSH remain blocked before a source-derived positive
  state, covariance, density matrix, and admissible observables;
- SM gauge/Higgs extraction currently hosts representation slots but does not
  source-select the SM quotient or physical Higgs field.

So the central substrate-shadow thesis remains **not yet falsifiable by one
surviving prediction**. It becomes falsifiable only when at least one candidate
emits a source-derived value before target comparison and names the observation
or mathematical computation that would refute it.

## 2. Candidate Prediction Inventory

This census treats a "candidate prediction" broadly: a proposed GU-specific
empirical consequence, or a consistency result that must close before any
empirical consequence can be trusted. The current candidates are:

| id | candidate | source basis | current decision |
|---|---|---|---|
| C01 | Dark-energy EOS sign/coupling: generated `xi_eff` deciding whether `w_a` can match DESI/Rubin. | `dark-energy-w-window-mechanism`, `mission-a-lambda-dark-energy-provenance`, `cycle2-source-forced-s-ig-dyn-action-gate`, `flrw-theta-xi-branch-reduction`. | Best next target, but not yet a prediction: coefficients are not source-generated. |
| C02 | Generation count: physical `ind_H(D_RS^phys)` gives total 24, 32, or another value. | `cycle1-generation-rs-rank-direct-gate`, `mission-a-generation-count-analytic-machinery`, `y14-k3-index-bridge`, `y14-k3-bridge-loss-ledger`. | Open: physical RS complex, H-trace, background, and bridge are missing. |
| C03 | SM gauge/Higgs selector: source-critical rank-one `v_PSB` or finite-control map selects the SM quotient and physical Higgs. | `cycle2-source-critical-rank-one-psb-selection-certificate`, `sm-gauge-higgs-finite-control-extraction-ledger`, Type II1 selector filters. | Precise target, not selected. Higgs quantum numbers are hosted, not emerged. |
| C04 | QFT state-space/measurement: GU-derived positive state space and finite `rho_AB` produce or fail CHSH. | `cycle2-qft-physical-field-positive-pairing-seed`, `qft-shadow-extraction-certificate`, `gu-measurement-channel-chsh-gate`. | Blocked before positive state, covariance, and observables. |
| C05 | VZ/causality: actual GU RS operator has no spacelike characteristics after E-block and subprincipal checks. | `cycle1-vz-subprincipal-eblock-proof-gate`, `cycle2-vz-actual-operator-e-block-certificate`, `vz-proof-grade-closure-attempt`. | Conditional typed-spine result; primary-operator and subprincipal gates open. |
| C06 | Anomaly/chirality content: complete observer-facing shadow is anomaly-safe and chiral without imported target SM content. | `anomaly-audit-cl95-gauge-group`, `anomaly-sp64-global-pi15`, `freed-hopkins-xobs-sol-k3-moduli`, `sm-gauge-higgs-finite-control-extraction-ledger`. | Partial consistency result only; full shadow/anomaly finality open. |
| C07 | RS/KK mass scale and mass ratio. | `gu-testable-predictions`, VZ/RS sector notes. | Underdetermined and not near observation; depends on fixed `R_s` and physical RS spectrum. |
| C08 | Cosmological constant/Tikhonov scale `Lambda * t_obs^2`. | `gu-testable-predictions`, CPA/Tikhonov notes. | Order-of-magnitude retrodiction/control, not a precision prediction. |
| C09 | Type II1/subfactor generation selector. | `type-ii1-selector-anti-smuggling-theorem`, `type-ii1-selector-or-nogo-theorem`, `sm-gauge-higgs-finite-control-extraction-ledger`. | Current cardinality-only selectors fail; no positive fixed-data selector yet. |
| C10 | Substrate chirality hooks in Wolfram/stochastic/CA/decidability lanes. | `objection-triage-register`, substrate persona reviews. | Lowest proof grade; most hooks insert chirality or lack an SM invariant. |

## 3. Ranking Criteria

Ranking uses two axes.

**Nearness-to-decidable** means how soon a bounded proof or computation could
decide the candidate without importing the target. A high score requires a
specific missing object, a binary or quantitative pass/fail condition, and a
small enough computation to run in the current repo program.

**Information gain** means how much a decision would change belief in the
central substrate-shadow thesis. A high score either produces a new empirical
consequence, kills a major reconstruction branch, or closes a prerequisite
without which empirical claims are impossible.

Source-dependence is marked as:

- `low`: mostly algebraic or already source-fixed;
- `medium`: one named source object or bridge is missing;
- `high`: several branch/action/shadow choices must be fixed first;
- `target-risk`: the candidate is especially exposed to importing observed
  SM/cosmology data upstream.

## 4. Ranked Table With Nearness, Source-Dependence, And Falsification Condition

| rank | id | candidate | nearness-to-decidable | information gain | source-dependence | falsification condition |
|---:|---|---|---:|---:|---|---|
| 1 | C01 | Dark-energy `xi_eff` sign/coupling and EOS | 4 | 5 | high, target-risk | A source-locked action/reduction generates no scalar theta mode, no `xi_eff`, or `xi_eff >= -0.319`; then the DESI-sign mechanism is absent for the current branch. If it generates `xi_eff < -0.319` before target comparison, the branch becomes observationally testable by `w_0,w_a` fits. |
| 2 | C02 | Physical generation count via `ind_H(D_RS^phys)` | 3 | 5 | high, target-risk | A source-derived physical RS complex and same-operator H-linear bridge returns `I` not equal to 8 or 16, or cannot define `I`; then current 3/4-generation readouts fail or remain unusable. If `I=8`, the three-generation candidate survives; if `I=16`, the four-generation branch survives. |
| 3 | C03 | Source-selected SM gauge/Higgs packet | 3 | 5 | high, target-risk | No source-natural `kappa_R1_PSB`/`pi_PSB` exists, `pi_PSB=0`, selected orbit is generic/higher-rank/line-only, or the finite-control map imports `A_F`, `G_SM`, `K_SM`, or Higgs data. |
| 4 | C04 | QFT positive state-space and finite measurement state | 3 | 5 | high | The physical quotient has negative norm, no positive state space exists, only imported/ansatz states exist, or every GU-admissible CHSH state/settings pair gives `CHSH <= 2`. |
| 5 | C05 | VZ/causality for the actual GU RS operator | 3 | 4 | medium-high | The primary GU operator lacks the typed first-order block, the actual E-block has a non-null kernel, or subprincipal/extrinsic-curvature terms produce spacelike characteristics. |
| 6 | C06 | Full anomaly/chirality-safe observer shadow | 2 | 4 | high | A complete observer-facing mode ledger contains an uncanceled perturbative, mixed, or Dai-Freed global anomaly, or chirality is only inserted by choosing the target SM shadow. |
| 7 | C09 | Type II1/subfactor generation selector | 2 | 4 | high, target-risk | Every proposed selector remains cardinality-only, survives `C_3 -> C_n` replacement, or imports finite Connes data before selection; then it is a host, not a generation prediction. |
| 8 | C07 | RS/KK mass scale and ratio | 2 | 3 | high | After a physical RS spectrum and `R_s` are source-fixed, spin-3/2 states are absent where required or do not have the predicted relation to spin-1/2 partners. Currently this is not accessible. |
| 9 | C08 | `Lambda * t_obs^2` Tikhonov scale | 2 | 2 | high, target-risk | A source derivation of `epsilon_sec`, `t_obs`, and the coefficient gives a value outside the claimed dimensionless window, or target time/scale choices are needed. Currently it is retrodictive. |
| 10 | C10 | Heterodox substrate chirality hooks | 1 | 3 | very high | No substrate lane supplies a specific SM chirality invariant and projection rule, or every toy model obtains chirality by hand-inserting parity breaking. |

The ranking is not a confidence ranking. C02 and C03 may be more central to GU
than C01, but C01 is nearer to a single quantitative decision because the
critical boundary `xi_eff < -0.319` is already exposed. Its missing object is
still serious: a source-forced coefficient packet, not another phenomenological
scan.

## 5. Best Next Single Prediction Candidate

**Best next candidate: C01, the dark-energy `xi_eff` coefficient packet.**

The next single prediction should not be "GU predicts DESI" or "GU predicts
`w_a != -1`." Those phrasings are too loose. The tight candidate is:

```text
SourceForcedThetaFLRWCoefficientPacket
  -> scalar mode status
  -> Z_theta
  -> C_Rtheta
  -> xi_eff = C_Rtheta / Z_theta
  -> post-derivation comparison to w_0,w_a
```

Why this is the best next target:

1. It has a concrete decision boundary: `xi_eff < -0.319` reaches the negative
   `w_a` window; minimal and conformal values do not.
2. It is close to observation, but the source computation can be done before
   observation is consulted, which makes anti-fitting possible.
3. It can fail cleanly. If the source action produces no scalar, no curvature
   coupling, or `xi_eff >= -0.319`, the current dark-energy prediction route is
   demoted or killed.
4. It also tests the central substrate-shadow thesis: does the richer GU source
   geometry generate an observer-shadow coefficient that the smooth FLRW
   comparison can check, or does it merely host a tunable phenomenological term?

The best proof target is therefore not a cosmology fit. It is the source-side
coefficient certificate, with DESI/Rubin windows locked out until after the
branch emits `Z_theta`, `C_Rtheta`, and `xi_eff`.

## 6. What Would Make The Central Substrate-Shadow Thesis Falsifiable

The thesis becomes falsifiable only when the repo can name at least one
source-derived substrate object whose shadow value is fixed before target data.
The minimum contract is:

```text
source-fixed substrate data
  -> typed reduction/projection/shadow functor
  -> one numerical or finite structural output
  -> no target quantity in the input graph
  -> explicit observation or theorem that would refute it
```

For this run, the nearest concrete forms are:

- dark energy: source geometry emits `xi_eff`, and surveys test the resulting
  `w_0,w_a` region;
- generations: source geometry emits physical `ind_H(D_RS^phys)`, and the
  generation readout is 3, 4, or neither without target division;
- gauge/Higgs: source geometry selects `v_PSB` and the exact finite shadow, with
  extra modes and anomalies audited;
- QFT: source geometry emits a positive state/covariance and admissible
  observables, so finite experiments have probabilities rather than labels.

Without one of these source-locked outputs, the substrate-shadow thesis remains
a reconstruction program plus discipline for avoiding no-go overreach, not a
single empirical prediction.

## 7. Next Meaningful Proof Or Computation Step

Run the C01 coefficient packet as a source-side gate:

```text
tests/source_forced_theta_flrw_coefficient_packet.py
```

Required output:

```json
{
  "branch_id": "Branch3_or_named_replacement",
  "source_action_locked_before_targets": true,
  "scalar_theta_mode": "present|absent|underdefined",
  "Z_theta": "number_or_symbolic_expression_or_absent",
  "C_Rtheta": "number_or_symbolic_expression_or_absent",
  "xi_eff": "number_or_symbolic_expression_or_absent",
  "target_inputs_seen": [],
  "decision": "XI_NEGATIVE_WINDOW|XI_NONNEGATIVE_OR_TOO_SMALL|NO_SCALAR|UNDERDEFINED|TARGET_FIT"
}
```

Pass/fail rules:

- `target_inputs_seen` nonempty -> `TARGET_FIT`;
- no source-forced action selector -> `UNDERDEFINED`;
- no scalar mode -> `NO_SCALAR`;
- `Z_theta <= 0` -> QFT/energy positivity failure for this branch;
- generated `xi_eff < -0.319` -> promote C01 to a concrete observational
  prediction candidate, still conditional on the rest of the stress tensor;
- generated `xi_eff >= -0.319` -> current DESI-sign route fails for the branch.

If C01 fails under a properly locked source action, the next frontier target
should be C02, because the physical RS index is the highest-information
generation-count gate.

## 8. Machine-Readable JSON Summary

```json
{
  "artifact": "CYCLE3_SINGLE_SURVIVING_PREDICTION_CENSUS",
  "version": "2026-06-24",
  "verdict": "NO_CURRENT_CONCRETE_SURVIVING_EMPIRICAL_PREDICTION",
  "current_surviving_empirical_prediction_exists": false,
  "all_current_candidates_reconstruction_grade_or_weaker": true,
  "best_next_candidate_id": "C01",
  "best_next_candidate": "SourceForcedThetaFLRWCoefficientPacket",
  "best_next_reason": "It exposes a source-side coefficient boundary xi_eff < -0.319 that can become an observational w0-wa test only after the branch emits coefficients before target comparison.",
  "ranking_criteria": {
    "nearness_to_decidable": "bounded proof or computation can decide the candidate without target import",
    "information_gain": "decision changes the central GU substrate-shadow reconstruction status",
    "source_dependence": ["low", "medium", "high", "target-risk"]
  },
  "candidate_count": 10,
  "ranked_candidates": [
    {
      "rank": 1,
      "id": "C01",
      "name": "Dark-energy xi_eff sign/coupling and EOS",
      "nearness_to_decidable": 4,
      "information_gain": 5,
      "source_dependence": "high,target-risk",
      "current_status": "OPEN_COEFFICIENTS_NOT_SOURCE_GENERATED",
      "qualifies_as_concrete_surviving_prediction": false,
      "falsification_condition": "Source-locked action/reduction generates no scalar mode, no xi_eff, or xi_eff >= -0.319; target leakage upstream also invalidates the prediction route."
    },
    {
      "rank": 2,
      "id": "C02",
      "name": "Physical generation count from ind_H(D_RS^phys)",
      "nearness_to_decidable": 3,
      "information_gain": 5,
      "source_dependence": "high,target-risk",
      "current_status": "OPEN_PHYSICAL_RS_COMPLEX_AND_BRIDGE_MISSING",
      "qualifies_as_concrete_surviving_prediction": false,
      "falsification_condition": "A source-derived physical RS complex and H-linear bridge returns a value other than 8 or 16, cannot define the H-index, or uses target division."
    },
    {
      "rank": 3,
      "id": "C03",
      "name": "SM gauge/Higgs source selector",
      "nearness_to_decidable": 3,
      "information_gain": 5,
      "source_dependence": "high,target-risk",
      "current_status": "SPECIFIED_NOT_SELECTED",
      "qualifies_as_concrete_surviving_prediction": false,
      "falsification_condition": "No source-natural kappa_R1_PSB/pi_PSB exists, selected vector is zero/generic/higher-rank/line-only, or SM/Higgs data are imported upstream."
    },
    {
      "rank": 4,
      "id": "C04",
      "name": "QFT positive state-space and finite measurement state",
      "nearness_to_decidable": 3,
      "information_gain": 5,
      "source_dependence": "high",
      "current_status": "BLOCKED_BEFORE_POSITIVE_STATE_AND_COVARIANCE",
      "qualifies_as_concrete_surviving_prediction": false,
      "falsification_condition": "Physical quotient has negative norm, no positive state/covariance exists, or all GU-admissible CHSH settings give CHSH <= 2."
    },
    {
      "rank": 5,
      "id": "C05",
      "name": "VZ causality for actual GU RS operator",
      "nearness_to_decidable": 3,
      "information_gain": 4,
      "source_dependence": "medium-high",
      "current_status": "CONDITIONAL_TYPED_SPINE_PRIMARY_AND_SUBPRINCIPAL_GATES_OPEN",
      "qualifies_as_concrete_surviving_prediction": false,
      "falsification_condition": "Primary GU operator lacks the typed first-order block, actual E-block is noninvertible off the null cone, or subprincipal terms create spacelike characteristics."
    },
    {
      "rank": 6,
      "id": "C06",
      "name": "Full anomaly/chirality-safe observer shadow",
      "nearness_to_decidable": 2,
      "information_gain": 4,
      "source_dependence": "high",
      "current_status": "PARTIAL_RELATIVE_CONSISTENCY_FULL_SHADOW_OPEN",
      "qualifies_as_concrete_surviving_prediction": false,
      "falsification_condition": "Complete observer-facing mode ledger contains an uncanceled perturbative, mixed, or Dai-Freed global anomaly, or chirality is inserted rather than selected."
    },
    {
      "rank": 7,
      "id": "C09",
      "name": "Type II1/subfactor generation selector",
      "nearness_to_decidable": 2,
      "information_gain": 4,
      "source_dependence": "high,target-risk",
      "current_status": "CARDINALITY_ONLY_SELECTORS_FILTERED_NEGATIVE",
      "qualifies_as_concrete_surviving_prediction": false,
      "falsification_condition": "Selector survives arbitrary C3-to-Cn replacement or imports finite Connes/SM data before selection."
    },
    {
      "rank": 8,
      "id": "C07",
      "name": "RS/KK mass scale and mass ratio",
      "nearness_to_decidable": 2,
      "information_gain": 3,
      "source_dependence": "high",
      "current_status": "UNDERDETERMINED_SPECTRUM_AND_RADIUS_NOT_SOURCE_FIXED",
      "qualifies_as_concrete_surviving_prediction": false,
      "falsification_condition": "After a source-fixed physical RS spectrum and radius, predicted spin-3/2 partners are absent or fail the mass relation."
    },
    {
      "rank": 9,
      "id": "C08",
      "name": "Lambda times t_obs squared Tikhonov scale",
      "nearness_to_decidable": 2,
      "information_gain": 2,
      "source_dependence": "high,target-risk",
      "current_status": "RETRODICTION_OR_CONTROL_NOT_PRECISION_PREDICTION",
      "qualifies_as_concrete_surviving_prediction": false,
      "falsification_condition": "Source derivation gives a different coefficient or the time/error scale must be chosen from the observed Lambda target."
    },
    {
      "rank": 10,
      "id": "C10",
      "name": "Heterodox substrate chirality hooks",
      "nearness_to_decidable": 1,
      "information_gain": 3,
      "source_dependence": "very-high",
      "current_status": "LOW_PROOF_GRADE_HOOK_OR_PARK",
      "qualifies_as_concrete_surviving_prediction": false,
      "falsification_condition": "No specific SM chirality invariant and projection rule is supplied, or parity breaking is hand-inserted in every toy model."
    }
  ],
  "central_thesis_falsifiability_contract": {
    "requires_source_locked_output": true,
    "requires_no_target_inputs": true,
    "requires_shadow_projection": true,
    "requires_explicit_refuting_observation_or_theorem": true,
    "nearest_contract": "source-fixed theta FLRW coefficient packet emits xi_eff before DESI/Rubin comparison"
  },
  "next_meaningful_step": {
    "id": "source_forced_theta_flrw_coefficient_packet",
    "candidate_id": "C01",
    "required_outputs": ["scalar_theta_mode", "Z_theta", "C_Rtheta", "xi_eff", "target_inputs_seen", "decision"],
    "promotion_condition": "xi_eff < -0.319 generated before target comparison",
    "demotion_conditions": ["no_scalar_mode", "xi_eff_absent", "xi_eff >= -0.319", "target_inputs_seen_nonempty"]
  }
}
```
