---
title: "GU Measurement Channel CHSH Gate"
date: 2026-06-24
status: exploration/provenance-gate
doc_type: gu_measurement_channel_chsh_gate
verdict: OBS_CHSH_PARK_STRONG_ANSATZ_ONLY
depends_on:
  - explorations/all-persona-wall-break-steelman-hegelian-2026-06-24.md
  - explorations/observer-finality-physical-forcing-gate-2026-06-24.md
  - explorations/observer-finality-pati-salam-chsh-fixture-2026-06-24.md
  - explorations/observer-finality-gu-derived-chsh-state-attempt-2026-06-24.md
  - explorations/observer-finality-gu-measurement-postulate-gate-2026-06-24.md
  - explorations/generation-count-sm-branching-closure-2026-06-22.md
  - explorations/sm-gauge-higgs-finite-control-extraction-ledger-2026-06-24.md
  - explorations/live-claim-dag-fault-finality-ledger-2026-06-24.md
executable_context:
  - tests/h3_pati_salam_chsh_correlator.py
  - tests/h3_pati_salam_chsh_candidate_state.py
  - tests/h3_pati_salam_gu_measurement_gate.py
---

# GU Measurement Channel CHSH Gate

## 1. Verdict

Decision for `OBS-CHSH`: **PARK**.

The repo does not currently contain a GU-derived `rho_AB` and does not currently contain
GU-admissible local CHSH observables. It contains:

- a correct formal observer/finality CHSH control layer;
- a Pati-Salam finite proxy with executable Bell and product controls;
- two strong Pati-Salam/CPT-labeled ansatz states that reach `2*sqrt(2)`;
- provenance guards that reject those controls and ansatz states as GU evidence.

The current route therefore remains **ansatz-only** for the physical `OBS-CHSH` claim.
This is not a failure of the Bell fixture. It is a state-preparation/provenance gate:
the missing object is the GU measurement channel

```text
M_GU:
  GU zero modes / two-point data / vacuum state
  -> finite Alice/Bob spaces H_A tensor H_B
  -> rho_AB
  -> GU-admissible local +/-1 observables
  -> CHSH decision
```

The pass/park/fail split is:

| target | decision | reason |
|---|---|---|
| Formal observer/finality controls | Pass as conditional formal machinery | The signed-readout/H3 fixture layer is useful and executable under its hypotheses. |
| Pati-Salam CHSH physical forcing | Park | The GU source state, finite reduction, and measurement postulate are missing. |
| Claim that current repo already derives `rho_AB` | Fail | Current violating states are controls or ansatz states, not GU outputs. |

## 2. Required Measurement-Channel Schema And Input/Output Objects

The minimum acceptable channel is not another Bell state. It is a typed extraction
certificate from GU data to the finite CHSH interface.

```text
M_GU = (GuSource, FiniteReduction, ObservableRule, LocalityRule)
       -> (H_A, H_B, rho_AB, Obs_A, Obs_B, CHSHCertificate)
```

| stage | object | required content | current repo state |
|---|---|---|---|
| 1 | `GuSource` | At least one of `P_ZM`, a basis of `ker(D_GU)` after section pullback, a GU two-point function `G_LR(x_A,x_B)`, a finite covariance `K_AB`, a GU vacuum/local-algebra state `omega`, or an explicit modular/thermal state. Source must name the GU operator, section/vacuum, constraints, and provenance. | Missing for CHSH. The repo has representation and index language, not the finite source state. |
| 2 | `FiniteReduction` | Projectors or local-algebra maps selecting Alice and Bob sectors, a direct-sum-to-tensor-product rule, color/isospin contractions, normalization, and any CPT/left-right symmetry assumption. | Proxy only: `H_A = V_L`, `H_B = V_R` in the fixture. No GU reduction map. |
| 3 | `FiniteInnerProduct` | GU-induced Gram matrices `G_A`, `G_B`, and if needed `G_AB`, plus proof that Hermitian/PSD checks use the correct finite pairing. | Fixture uses the standard finite Hermitian pairing. GU finite Gram data is missing. |
| 4 | `DensityExtraction` | A formula producing `rho_AB in End(H_A tensor H_B)` with `rho_AB >= 0`, `Tr(rho_AB)=1`, and role/provenance `gu_derived` / `gu-derived:<source>`. | Missing. Bell and Pati-Salam/CPT states are inserted as controls or ansatz. |
| 5 | `ObservableRule` | A rule selecting local self-adjoint `+/-1` operators `A,A' in End(H_A)` and `B,B' in End(H_B)` with `gu-admissible:<postulate>` provenance. It must explain why same-party settings may be noncommuting. | Missing. Existing Pauli operators are control observables only. |
| 6 | `LocalityRule` | Alice/Bob local commutation, no postselection/future-setting dependence, and NAC/locality for the same live state and observables. | Matrix commutation is checked in the fixture; GU NAC remains conditional. |
| 7 | `CHSHCertificate` | Compute `Tr(rho_AB S_CHSH)`, where `S_CHSH = A tensor B + A tensor B' + A' tensor B - A' tensor B'`; emit `> 2 + epsilon`, `<= 2`, or invalid provenance. | Existing controls compute correctly; live GU slot is pending. |

Acceptance requires all stages. Representation labels alone do not instantiate `M_GU`.
CPT pairing alone does not instantiate `M_GU`. Generic vacuum-entanglement language alone
does not instantiate `M_GU`.

## 3. What The Repo Currently Supplies Versus Imports

| datum | status | decision-useful reading |
|---|---|---|
| `S(6,4) = C^16` and Pati-Salam split `(4,2,1) + (4bar,1,2)` | Supplied as representation branch | This fixes the carrier labels and dimensions for `V_L` and `V_R`. |
| Pati-Salam maximal compact frame `Spin(6) x Spin(4) ~= SU(4) x SU(2)_L x SU(2)_R` | Supplied/relative | Good branching frame. It is not itself a physical low-energy selector. |
| Pati-Salam-to-SM charge packet | Relative derivation after choosing the Pati-Salam/SM embedding | The charge packet is correct in that frame, but the finite-control ledger keeps full SM selection open. |
| Alice/Bob proxy `H_A = C^4_color tensor C^2_SU(2)_L`, `H_B = C^4_anticolor tensor C^2_SU(2)_R` | Supplied as finite proxy | Useful test harness, not a GU state-preparation map. |
| Control CHSH observables `Z_L`, `X_L`, `(Z_R +/- X_R)/sqrt(2)` | Supplied as executable controls | They verify Bell plumbing. They are not yet GU-admissible measurements. |
| Maximally entangled Bell control and product control | Supplied as controls | Bell control reaches `2*sqrt(2)`; product control stays inside the Bell bound. |
| CPT-paired pure rank-8 Bell state | Imported ansatz | Assumes coherent equal amplitudes over color and SU(2). Not derived. |
| CPT-paired color-mixed SU(2) Bell state | Imported ansatz | Avoids coherent color superposition, but still inserts the SU(2) Bell factor. |
| Generic Pati-Salam/CPT pairing | Partial structural motivation | Pairs labels but does not determine amplitudes, phases, purity, Schmidt spectrum, or correlations. |
| GU zero-mode/two-point/vacuum source for CHSH | Missing | This is the first state-preparation blocker. |
| GU measurement postulate for local noncommuting readouts | Missing | This is the first observable blocker. |
| Locality/NAC for live GU state and settings | Conditional | Existing fixture checks matrix commutation only. Physical NAC is downstream of GU bridge claims. |

Current conclusion:

```yaml
repo_has_gu_derived_rho_ab: false
repo_has_gu_admissible_chsh_observables: false
repo_has_executable_controls: true
repo_has_strong_pati_salam_ansatz_states: true
obs_chsh_decision: PARK
route_status: STRONG_ANSATZ_ONLY
```

## 4. State And Observable Provenance Table

| object | provenance in repo | CHSH status with existing fixture | allowed claim |
|---|---|---:|---|
| `rho_control_phi_8` | `control:maximally-entangled-on-C4xC2-proxy` | `2.828427124746` | Bell plumbing works; not GU evidence. |
| `rho_control_product_00` | `control:product-state-on-C4xC2-proxy` | `1.414213562373` | Separable control stays inside Bell bound. |
| `rho_ansatz_cpt_pure_rank8_phi` | `ansatz:pati-salam-left-right-cpt-pairing+coherent-equal-amplitudes-over-color-and-su2` | `2.828427124746` | Strong ansatz only; rejected by GU gate. |
| `rho_ansatz_cpt_color_mixed_su2_phi` | `ansatz:pati-salam-left-right-cpt-pairing+color-classical-mixture+su2-phi-correlations` | `2.828427124746` | Strongest conservative violating ansatz; still rejected by GU gate. |
| `rho_symmetry_baseline_maximally_mixed` | `symmetry-baseline:pati-salam-representation-only` | `0` for traceless SU(2) controls | Shows representation-only symmetry does not force violation. |
| Future `rho_AB` | must be `role="gu_derived"` and `provenance="gu-derived:<zero-mode-or-two-point-source>"` | unknown | Required to upgrade or fail the physical claim. |
| Existing Pauli SU(2) settings | `control:pati-salam-proxy-su2-factor` | optimal for Bell controls | Good control observables, not a GU measurement postulate. |
| Future local observables `A,A',B,B'` | must begin `gu-admissible:<measurement-postulate-reference>` | unknown | Required to decide physical `OBS-CHSH`. |

The executable guardrail is already right: known controls, symmetry baselines, and ansatz
states must not pass as `gu_derived`.

## 5. Claim Certificate Table For OBS-FORMAL And OBS-CHSH

| claim node | current certificate | live dependencies | forbidden promotion | decision |
|---|---|---|---|---|
| `OBS-FORMAL` | Signed-readout/H3 formal layer is useful as conditional theorem/protocol machinery. It separates record/finality/readout structure and provides executable falsification surfaces. | Signed-readout hypotheses, NAC as formal input, odd-SBP, record graph definitions, local/domain-relative finality discipline. | Treating observer/finality as a physical no-go escape, or treating odd-SBP as physically forced before GU supplies state and measurement data. | **PASS-FORMAL**, with conditional-finality only. |
| `OBS-CHSH` | Pati-Salam finite fixture and candidate-state audits are executable. Controls pass. Strong ansatz states reach Tsirelson but are rejected as GU evidence. | `OBS-FORMAL`, GU-derived `rho_AB`, GU-admissible observables, Pati-Salam left/right split, NAC/local commutativity for live data. | Copying the Bell control into the GU slot, relabeling a Pati-Salam ansatz as a GU state, choosing Pauli settings without a GU measurement postulate, or using generic vacuum entanglement as a finite density matrix. | **PARK**, not pass. |

`OBS-CHSH` can move from `PARK` to `PASS` only if a GU source and measurement rule produce
a valid finite state and admissible settings with `CHSH > 2 + epsilon`. It moves from
`PARK` to `FAIL` for physical forcing if the derived channel is separable, only allows
commuting classical readouts, or gives `CHSH <= 2` for all admissible settings.

## 6. Branch/Measurement Robustness Table

| branch or channel | state source | measurement source | current CHSH behavior | robustness decision |
|---|---|---|---:|---|
| Pure Bell ansatz | Imported equal-amplitude CPT-paired rank-8 Bell vector | Existing Pauli SU(2) controls | `2.828427124746` | Numerically strong, provenance weak. Park as ansatz; fail if promoted as GU. |
| Color-mixed ansatz | Imported classical color mixture plus SU(2) Bell block | Existing Pauli SU(2) controls | `2.828427124746` | More conservative than pure color coherence, but still inserts the needed SU(2) Bell correlation. Park as ansatz. |
| Generic Pati-Salam pairing | Representation branch plus possible CPT label pairing | No derived observable rule | not determined | Not robust. Pairing labels do not fix a density matrix or noncommuting measurements. |
| GU two-point channel | Future `G_LR`, `K_AB`, `omega`, or zero-mode source reduced to `rho_AB` | Future `gu-admissible:` local observables | unknown | Only branch that can upgrade. Pass if it derives violation; fail physical forcing if it derives no violation. |
| Separable-output channel | Future GU-derived state happens to be separable or SU(2)-uncorrelated | Future admissible observables, possibly only commuting charges | `<= 2` for admissible settings | Real negative result. Fail physical `OBS-CHSH`, while preserving formal controls. |

This table is the main measurement robustness result: all currently violating branches are
control/ansatz branches. The only decisive branch is the missing GU source channel, and it
is allowed to return a negative result.

## 7. First Exact Missing Proof Object

The first missing proof object is a **GUStateExtractionCertificate**. It should precede
any claim about admissible CHSH observables because the state-preparation map determines
what Hilbert spaces, Gram conventions, and local algebras the observables act on.

Minimum certificate shape:

```text
GUStateExtractionCertificate:
  source_kind:
    one of {zero_mode_projector, ker_D_GU_basis, two_point_function,
            finite_covariance, vacuum_local_algebra_state, modular_state}
  source_provenance:
    gu-derived:<operator/section/vacuum/reference>
  selected_section_or_vacuum:
    explicit GU section, boundary condition, vacuum, or local-algebra state
  finite_spaces:
    H_A, H_B, basis choices, dimensions, and relation to V_L, V_R
  finite_pairing:
    G_A, G_B, and Hermiticity convention
  reduction_map:
    field/local-algebra data -> End(H_A tensor H_B)
  color_isospin_contraction:
    explicit contraction/trace/projection rules
  cpt_left_right_status:
    preserved, broken, or not used
  output_state:
    rho_AB, role="gu_derived", provenance starts "gu-derived:"
  checks:
    Hermitian with respect to finite pairing,
    positive semidefinite,
    trace one,
    not equal to forbidden control/ansatz by construction
```

The second proof object, immediately downstream, is an
**AdmissibleObservableCertificate**:

```text
AdmissibleObservableCertificate:
  observables:
    A, A' in End(H_A), B, B' in End(H_B)
  provenance:
    gu-admissible:<measurement-postulate-reference>
  checks:
    self-adjoint, +/-1 spectrum, Alice/Bob local commutation,
    same-party noncommutation justified by physical readout,
    no postselection or hidden nonlocal setting dependence
```

Without the first certificate, the repo cannot honestly say it has a GU-derived `rho_AB`.
Without the second, it cannot honestly say the Pauli-like settings are physical GU
measurements.

## 8. Next Meaningful Proof/Computation Step

Do not add another Bell fixture. The meaningful next step is to fill one source lane of
`GUStateExtractionCertificate` end to end.

Best first computation:

1. Choose one source lane, preferably a two-point/covariance lane:

```text
G_LR(x_A,x_B) = <Omega_GU | psi_L(x_A) psi_R_bar(x_B) | Omega_GU>
```

or an equivalent finite covariance `K_AB` from the same GU operator/vacuum data.

2. Project that source to the Pati-Salam finite proxy:

```text
V_L = (4,2,1),     V_R = (4bar,1,2),
H_A = V_L,         H_B = V_R
```

while recording the finite Gram matrix and the direct-sum-to-tensor-product reduction.

3. Produce the actual `rho_AB`, even if it is maximally mixed, separable, partially
entangled, or not Bell-optimal. Record trace, positivity, Schmidt/correlation spectrum,
and color/isospin contraction.

4. Only then derive or reject a measurement postulate for noncommuting local readouts.
If the only admissible measurements are commuting charge projectors, record
`SEPARABLE_OR_NO_VIOLATION` or `NO_ADMISSIBLE_CHSH_SETTINGS`.

5. Run the existing gates rather than weakening them:

```bash
python tests/h3_pati_salam_chsh_correlator.py
python tests/h3_pati_salam_chsh_candidate_state.py
python tests/h3_pati_salam_gu_measurement_gate.py
python tests/h3_pati_salam_gu_measurement_gate.py --require-gu
```

At the current repo state, the first three commands should pass or skip missing GU inputs
as designed, and the `--require-gu` command should fail because the GU state and
observables are still absent. A future upgrade must make `--require-gu` pass by adding
real GU-derived data, not by relaxing provenance checks.

Final gate status:

```yaml
obs_formal: PASS_FORMAL_CONDITIONAL_ONLY
obs_chsh: PARK
current_route: STRONG_ANSATZ_ONLY
first_missing_object: GUStateExtractionCertificate
next_step: compute_GU_two_point_or_covariance_to_finite_rho_AB
```
