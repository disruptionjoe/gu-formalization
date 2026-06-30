---
title: "Stress-Energy / Wood Emergence Certificate"
date: "2026-06-24"
status: exploration/certificate
doc_type: stress_energy_shadow_emergence_certificate
verdict: "CERTIFICATE_SPECIFIED_STRESS_ENERGY_SHADOW_NOT_DERIVED"
owned_path: "explorations/geometry-curvature-emergence/stress-energy-shadow-emergence-certificate-2026-06-24.md"
optional_audit:
  - "tests/stress_energy_shadow_emergence_audit.py"
depends_on:
  - "process/runbooks/five-lane-frontier-run.md"
  - "explorations/geometry-curvature-emergence/gr-shadow-recovery-certificate-2026-06-24.md"
  - "explorations/misc/constraint-first-ig-tangent-space-gate-2026-06-24.md"
  - "explorations/geometry-curvature-emergence/exact-schwarzschild-kerr-el-gate-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/gu-action-4d-physics-gate-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/gu-minimal-action-spec-2026-06-24.md"
  - "explorations/misc/gu-closed-loop-action-ig-branch-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/finite-control-provenance-audit-2026-06-24.md"
  - "explorations/geometry-curvature-emergence/matter-gauge-source-geometry-selector-gate-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/live-claim-dag-fault-finality-ledger-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/qft-shadow-extraction-certificate-2026-06-24.md"
  - "explorations/geometry-curvature-emergence/ic4-lagrangian-tmunu-derivation-2026-06-23.md"
---

# Stress-Energy / Wood Emergence Certificate

## 1. Verdict

The certificate is specified, but the repo does not currently derive
observer-facing stress-energy.

Current decision:

```text
STRESS-ENERGY-SHADOW:
  specified_open
  proof_grade: specification
  finality: not_final
  current_status: not_derived

SOURCE-CURRENT:
  branch_dependent
  bare theta source not generally stable across branches

MATTER-SHADOW:
  partial_open
  Pati-Salam branch evidence exists
  full matter/QFT shadow not selected

QFT-SHADOW:
  blocked before state space, state, observables, and anomaly-complete shadow
```

Einstein's marble/wood complaint is the right diagnostic. In ordinary GR, the curvature
term `G_mu_nu` is principled geometry while `T_mu_nu` is a phenomenological
right-hand-side input. The `Lambda g_mu_nu` term is a separate geometric-side patch: it is
not stress-energy wood, but it also does not count as principled marble unless its source
provenance is supplied.
The steelman GU direction is not to claim that the current repo has solved this. It is
to leave open the stronger heterodox possibility that the 4D metric marble and the
matter wood are both observer-facing shadows of a deeper source geometry.

That possibility is not yet certified. The repo has:

- a GR-shadow certificate schema, but no true GR shadow certificate;
- a reconstruction-grade IC4 variational `T_mu_nu` note, but not a branch-closed source
  action with full proof provenance;
- branch analyses showing free beta kills nonzero theta, Branch 2A lacks `Phi`, Branch
  2B corrects the source, and Branch 3 must use total-current language;
- a matter/gauge selector gate showing Pati-Salam branch evidence, but no full SM
  finite-control or physical matter selector;
- a QFT-shadow certificate showing that state space, states, observables, Born
  probabilities, unitarity, spin-statistics, and full anomaly shadow are still owed.

Therefore the honest conclusion is:

```text
T_mu_nu is not yet GU-derived wood.
Lambda_eff is not yet a GU-derived dark-energy replacement.
The certificate below defines what would make it a GU-derived source-current/stress-energy
shadow and what would block hidden matter or hidden Lambda relabeling.
```

## 2. Derived Stress-Energy Versus Imports, Hosts, Ansatze, And Residual Relabeling

### 2.1 Derived stress-energy

`T_mu_nu^shadow` counts as derived only when it is produced by one fixed source branch:

```text
I_GU_branch =
  (D_GU, S_GU, fields, variation_space, source law,
   section map, reduction functor, boundary data, observer regime)
```

and when every term in `T_mu_nu^shadow` has this trace:

```text
source action/operator term
  -> source Euler-Lagrange variation
  -> source current or stress tensor
  -> observer projection along s: X -> Y
  -> conservation from source Noether/Bianchi identity
  -> coupling into the same GR-shadow equation
  -> positivity/unitarity/anomaly/QFT provenance status
```

The observer stress tensor may be written schematically as:

```text
T_mu_nu^shadow =
  T_mu_nu^YM
  + T_mu_nu^DD
  + T_mu_nu^IG_or_theta
  + T_mu_nu^section
  + T_mu_nu^selected_matter
  + T_mu_nu^renormalized_or_quantum
```

but only terms with a complete provenance row may be placed in the `derived` bucket.
The IC4 note is useful because it reconstructs a variational stress tensor from
Yang-Mills, Dirac-DeRham, and distortion terms. Under this certificate, IC4 is not enough
by itself: the action branch, IG variation, nonlinear conservation, positivity, observer
projection, and matter/QFT provenance still have to close in the same branch.

### 2.2 Imported matter

Matter is imported if any observer-facing stress-energy term is supplied from outside
the source geometry:

```text
external SM QFT fields,
finite Connes data A_F or K_SM,
the SM gauge quotient G_SM/Z_6,
phenomenological perfect fluids,
hand-written scalar/Higgs potentials,
ordinary anomaly-free SM shadow taken as input,
or a standard QFT Hilbert/Fock space inserted without source extraction.
```

Imported matter may be used as an explicitly labeled comparison branch. It may not be
counted as GU-derived `T_mu_nu^shadow`.

### 2.3 Hosted matter

Matter is hosted when the source geometry contains a slot, representation, or ambient
field space but no selector chooses the physical observer datum.

Examples from current repo state:

```text
Pati-Salam branch frame: derived branch representation, not final low-energy gauge group.
SM Higgs quantum-number slot: hosted, not physical Higgs emergence.
Type II_1 host lane: conditional host for finite CC data, not selector.
Sp(64) carrier: derived source carrier, not observer matter spectrum by itself.
```

Hosted slots may feed future selectors. They do not produce derived stress-energy until
a physical source projection, dynamics, QFT state/observables, and anomaly-compatible
observer shadow are supplied.

### 2.4 Ansatz matter

Matter is ansatz matter if the fields or stress tensor are chosen because they make a
target metric, target cosmology, or target low-energy sector work:

```text
perfect fluid chosen to fit FLRW,
scalar ansatz chosen to get xi_eff about -0.6,
source current chosen to cancel Schwarzschild/Kerr section residuals,
projector chosen because its conormal contains the desired theta,
Bell state or density matrix copied into a GU slot,
or Higgs potential chosen because it has electroweak symmetry breaking.
```

Ansatz matter can be a diagnostic or control. It is not derived wood.

### 2.5 Residual relabeling

Residual relabeling is the hidden-matter failure mode:

```text
unexplained geometric residual R_mu_nu
  -> moved to the right-hand side
  -> called matter stress-energy
```

Forbidden examples:

- Relabel `Q^TF(B_s)` as matter without a source action variation and positivity proof.
- Relabel Willmore or section residuals as vacuum stress to pass Schwarzschild/Kerr.
- Relabel Branch 2B multiplier currents as bare theta source.
- Relabel Branch 3 `J_IG` as ordinary matter while still citing `D_A^*F_A = theta`.
- Relabel finite-control hosted slots as physical QFT matter.
- Relabel anomaly cancellation of ordinary SM as proof that GU selected the ordinary SM
  shadow.
- Move any uncancelled `R_shadow` term into `T_mu_nu` after the target test is known.
- Move any uncancelled source or section residual into `Lambda_eff` after the cosmology
  target is known.

Anti-smuggling rule:

```text
No term may enter derived T_mu_nu^shadow unless it has:
  1. source action/operator provenance,
  2. variational derivation,
  3. observer projection,
  4. conservation proof,
  5. positivity/unitarity/anomaly status,
  6. branch-local rollback condition.
```

Anything missing one of these remains a residual, host, import, ansatz, or control.

The same rule applies to a cosmological-constant-looking term. A branch may report:

```text
Lambda_eff = 0
Lambda_eff = imported_constant
Lambda_eff = phenomenological_control
Lambda_eff = source_derived_dynamic_term
```

Only the last option can be cited as GU-derived, and only after the branch supplies
`LambdaDarkEnergyProvenanceCertificate(branch)`.

## 3. Required Certificate Pipeline

### 3.1 Source action/operator

Required object:

```text
SourceStressActionCertificate(branch)
```

Minimum input:

```text
X, Y = Met_Lor(X), g_Y
s: X -> Y, g = s^* g_Y
P -> Y, G = Sp(64), A, F_A
eps, beta or U/P, theta
Psi and any source matter fields
D_GU
S_GU[branch]
variation_space[branch]
boundary/vacuum/domain data
source selector or matter/QFT shadow data if ordinary matter is claimed
```

Current status: underdefined. The minimal action spec is a branch specification, not a
closed primary action. IG variation remains blocked.

### 3.2 Variation

The certificate must derive the stress object from variation, not from target matching:

```text
E_s = 0
E_A = 0
E_IG = 0
E_Psi = 0
E_matter = 0, if selected matter exists
```

Then:

```text
T_mu_nu^shadow =
  -2 / sqrt(|g|)
  * delta S_eff_branch / delta g^mu_nu
```

where `S_eff_branch` is obtained by source pullback/projection from `S_GU[branch]`.
The metric `g` must enter as `s^*g_Y`; it must not be introduced as an independent
fundamental Einstein-Hilbert metric sector merely to manufacture a familiar stress tensor.

Current status: reconstruction only. The IC4 note gives a useful variational pattern, but
it is upstream of the current branch-closed action, IG, and QFT-shadow gates.

### 3.3 Source current

The source-current law must be branch-specific:

| branch | admissible source current | current status |
|---|---|---|
| Branch 2A | bare `theta` only if `Phi(eps,beta,s)=0` is A-independent and derived | missing `Phi` |
| Branch 2B | corrected current including `(D_A Phi)^*lambda` | possible, not bare theta |
| Branch 3 | total current `theta_eff = c_theta theta - J_IG + ...` | honest fallback, action unwritten |
| Free beta | `theta = 0`, so nonzero theta source fails | rejected |
| Background/Stueckelberg | spurion/background source may survive | host/thin; Noether cost |

The certificate must identify whether the stress tensor is built from bare `theta`, a
corrected multiplier current, a total IG current, or selected matter/QFT currents.

### 3.4 Observer projection

The observer-facing tensor must be a projection of the source object:

```text
Pi_obs:
  source EL/current/stress data on Y
  -> (g_mu_nu, T_mu_nu^shadow, J_mu^shadow, residuals) on X.
```

Required outputs:

```text
g_mu_nu = s^* g_Y
T_mu_nu^shadow is symmetric in observer indices
J_mu^shadow or gauge current is typed and gauge-covariant
kappa_eff and Lambda_eff are fixed by source normalization
all residual terms are named as R_shadow, not hidden in T_mu_nu or Lambda_eff
```

### 3.5 Conservation

Conservation must be derived:

```text
source gauge/diffeomorphism Noether identity
  + source Bianchi identities
  + branch source law
  -> nabla^mu T_mu_nu^shadow = 0
```

It is not enough to impose `nabla^mu T_mu_nu = 0` as a 4D consistency condition. It is
also not enough to assume a generic identity such as `D_A^*D_A^*F_A = 0`. The conserved
quantity must match the branch:

```text
Branch 2A: conserve bare theta-derived current only after Phi and D_A Phi = 0 are proved.
Branch 2B: conserve the corrected multiplier-inclusive current.
Branch 3: conserve total current theta_eff.
Background: account for omitted spurion variations.
Finite-control/QFT: conserve the stress tensor of the selected observer shadow.
```

Current status: blocked beyond reconstruction/linear checks.

### 3.6 Coupling to GR shadow

The same branch must couple the stress tensor to the GR-shadow equation:

```text
Pi_4D(E_s,E_A,E_IG,E_Psi,E_matter) =
  G_mu_nu[g]
  + Lambda_eff g_mu_nu
  - kappa_eff T_mu_nu^shadow
  - R_mu_nu^shadow
  = 0.
```

For an exact GR shadow in the declared regime:

```text
R_mu_nu^shadow = 0
```

or `R_mu_nu^shadow` must be a named, controlled modified-gravity correction. It cannot be
silently moved into `T_mu_nu^shadow`.

Vacuum test:

```text
Schwarzschild/Kerr vacuum branches require T_mu_nu^shadow = 0
for ordinary matter, except for explicitly declared source-geometric vacuum currents
whose action/current/conservation/positivity provenance is complete.
```

If a branch needs nonzero hidden stress to make a vacuum black hole pass, it fails the
vacuum GR-shadow certificate.

### 3.7 Energy and positivity conditions

The stress tensor must have physical sign/probability status, not merely tensor shape.

Required conditions by lane:

| lane | positivity burden |
|---|---|
| classical gauge/source fields | correct sign kinetic terms, no negative-energy physical modes after gauge reduction |
| `Q^TF(B_s)`/section stress | positivity on physical projected modes; no leakage from negative-signature normal directions |
| spinor/QFT matter | positive Hilbert/Fock or algebraic state space; no negative-norm physical sector |
| quantum/renormalized stress | positive state, renormalization prescription, anomaly/trace terms named |
| effective fluids/scalars | energy conditions or explicit controlled violation named as prediction |

Current status: not closed. IC2/IC4 supply reconstruction-grade positivity/variation
ingredients for some geometric terms, but the full branch-positive observer stress tensor
is not certified.

### 3.8 QFT and matter provenance

The stress tensor of ordinary matter requires a matter/QFT shadow:

```text
source geometry
  -> physical field complex or local algebra
  -> state space
  -> state or density matrix
  -> observables/probabilities
  -> local dynamics/unitarity/spin-statistics
  -> anomaly-compatible observer modes
  -> stress-energy expectation or classical limit.
```

Current status: blocked by the QFT-shadow certificate. Pati-Salam branch representation
evidence is useful, but representation labels are not a QFT state, not a stress tensor,
and not observer matter dynamics.

## 4. Branch Table

| branch | can produce nonzero source? | stress-energy status | hidden-relabeling risk | decision |
|---|---|---|---|---|
| Branch 2A: A-independent constrained IG | Yes, only if derived `Phi(eps,beta,s)=0` makes beta tangent proper and `D_A Phi = 0` | Could preserve bare `D_A^*F_A = theta`; no derived `T_mu_nu^shadow` yet | Inventing `Phi` or projecting residuals into theta after target tests | strongest conservative template, underdefined |
| Branch 2B: A-dependent constrained IG | Yes, with multiplier-corrected source | Stress must include multiplier current if it contributes | Calling corrected current "bare theta"; hiding lambda stress | possible branch, not bare-source canon |
| Branch 3: dynamical IG / total current | Yes, through differential IG dynamics | Stress/current must be built from `S_IG-dyn` and `theta_eff` | Calling `theta_eff` ordinary matter or citing old bare-theta conservation | honest fallback, action unwritten |
| Free beta / bare norm | No; beta variation forces `theta = 0` | Cannot derive nonzero theta stress/source | Claiming nonzero theta anyway; adding matter after collapse | rejected for nonzero wood emergence |
| Background/Stueckelberg | Can host nonzero spurion/background source | Source equation may survive, but dynamical stress derivation is thin | Omitting background variations while claiming full Noether conservation | viable host/spurion branch only |
| Finite-control host/import | Can host representation slots or imported SM/CC matter | Stress-energy is imported/hosted until selector and QFT shadow close | Treating Pati-Salam slots, `A_F`, `K_SM`, or ordinary SM anomaly checks as derived matter | partial host/import, no full matter stress derivation |

Robust conclusion:

```text
No current branch derives observer-facing T_mu_nu.
The only branch-robust negative is that free beta plus the bare theta norm cannot support
nonzero theta stress-energy.
```

## 5. Claim Certificate Table

| claim | current status | proof grade | derived content | forbidden shortcuts | rollback conditions | citation language |
|---|---|---|---|---|---|---|
| `STRESS-ENERGY-SHADOW` | `specified_open` | `specification` | certificate schema only | weak-field pass as exact stress derivation; IC4 reconstruction promoted to branch proof; residual relabeling; imported QFT matter; target-fitted fluids; hidden `R_shadow` moved to `T_mu_nu` | missing branch action; missing variation; missing conservation; positivity failure; hidden matter needed for vacuum tests; QFT shadow absent for ordinary matter | "A stress-energy shadow certificate is specified; current GU does not yet derive observer-facing `T_mu_nu`." |
| `SOURCE-CURRENT` | `branch_dependent_open` | `specification/reconstruction` | branch source-law taxonomy | calling Branch 2B or 3 bare theta; assuming `D_A^*D_A^*F_A=0`; ignoring background Noether cost | Branch 2A `Phi` absent; Branch 3 chosen without `theta_eff`; free beta action used with nonzero theta | "The source current is branch-dependent; bare theta is not generally certified." |
| `LAMBDA-DARK-ENERGY-PATCH` | `open_patch_slot` | `specification` | no source-derived certificate | bare `Lambda`; fitted `xi_eff`; target-tuned dark-energy fluid; hidden residual moved to `Lambda_eff` | coefficient inserted after target data; no generated `Z_theta/C_Rtheta/xi_eff`; conservation or exact-GR compatibility fails | "`Lambda_eff` is a patch/dark-energy slot; current GU does not yet derive it." |
| `ACTION-GR-COUPLING` | `open` | `specification` | GR-shadow coupling schema | using `T_mu_nu` to absorb exact Schwarzschild/Kerr residuals; treating weak-field `O(M/r)` as exact | full EL projection missing; exact black-hole vacuum requires hidden stress; `R_shadow` not controlled | "Stress-energy coupling to a GR shadow remains open with the full action/IG gate." |
| `MATTER-SHADOW` | `partial_open` | `reconstruction/contract` | Pati-Salam branch packet and relative charge arithmetic | importing `A_F`, `G_SM/Z_6`, `K_SM`, physical Higgs, or ordinary SM shadow as source-selected matter | selector takes target data as input; extra modes survive without anomaly control; Higgs projection/potential absent | "Source geometry derives branch representation evidence, not the full observer matter stress tensor." |
| `QFT-STRESS` | `blocked` | `specification` | none beyond certificate schema | representation labels as states; Bell controls as states; Pauli controls as observables; formal path integral without state/positivity | no positive state space; no normalized source-derived state; no admissible observables; nonunitary dynamics; anomaly failure | "Ordinary matter stress-energy requires a QFT shadow, currently blocked before state and observable extraction." |

Forbidden shortcuts:

| shortcut | disposition |
|---|---|
| `Q^TF(B_s)` equals matter by name | forbidden unless action variation, positivity, and conservation are proved |
| residual-to-right-hand-side move | forbidden hidden matter relabeling |
| weak-field compatibility as `T_mu_nu` derivation | insufficient |
| IC4 reconstruction as full branch certificate | useful input, not current closure |
| imported finite Connes/SM/QFT data | import, not derivation |
| hosted representation slot as physical stress | host, not derivation |
| ansatz fluid/scalar/Higgs selected by target fit | control/ansatz, not derivation |
| Branch 2B/3 current called bare theta | branch-language failure |
| free beta with nonzero theta stress | contradiction |
| ordinary anomaly cancellation as full GU anomaly shadow | relative check only |

Rollback conditions:

```text
STRESS-ENERGY-SHADOW rolls back to imported/hosted if any term in T_mu_nu lacks source
action/operator provenance.

STRESS-ENERGY-SHADOW rolls back to residual if the term is introduced only because an
EL projection failed.

SOURCE-CURRENT rolls back from bare-theta language if Branch 2A Phi is absent,
A-dependent, or target-fitted.

SOURCE-CURRENT rolls back to theta_eff language if Branch 3 is chosen.

Vacuum GR-shadow rolls back if Schwarzschild/Kerr need nonzero hidden matter stress.

MATTER-SHADOW rolls back if the selector consumes A_F, G_SM, K_SM, physical Higgs,
n = 3, or ordinary SM content.

QFT-STRESS rolls back if state space, state, observables, positivity, unitarity,
spin-statistics, or anomaly compatibility are missing.
```

## 6. First Exact Missing Proof Object

The first exact missing proof object is:

```text
NoHiddenMatterStressEnergyShadowTheorem(branch)
```

This is the proof object that would prevent hidden matter relabeling.

Required input:

```text
branch_fixed_S_GU
D_GU and physical field complex
variation_space[branch]
source current law[branch]
section map s and observer projection Pi_obs
j_s and II_s^H normalization
finite-control selector or explicit bypass certificate
QFT shadow data if ordinary matter is claimed
boundary/vacuum/domain data
```

Required output:

```text
1. Full source EL tuple:
   E_s = E_A = E_IG = E_Psi = E_matter = 0 where applicable.

2. Term provenance ledger:
   every term in T_mu_nu^shadow maps to exactly one source action/operator/current term,
   with status derived, derived_relative, hosted, imported, ansatz, residual, or control.

3. Variational identity:
   T_mu_nu^shadow = -2/sqrt(|g|) delta S_eff_branch / delta g^mu_nu,
   with g = s^*g_Y and no independent target GR metric sector.

4. Projection identity:
   Pi_4D(EL tuple) =
     G_mu_nu[g] + Lambda_eff g_mu_nu
     - kappa_eff T_mu_nu^shadow
     - R_mu_nu^shadow.

5. Anti-relabeling lemma:
   any tensor not in the provenance ledger remains R_shadow, host/import/ansatz/control,
   or a named modified-gravity correction; it may not be moved into derived T_mu_nu.

6. Conservation theorem:
   source Noether/Bianchi identities imply nabla^mu T_mu_nu^shadow = 0 for the same
   branch and same source current.

7. Positivity/QFT theorem:
   physical source modes have positive energy/state status after gauge reduction, and
   ordinary matter stress is backed by a QFT shadow or explicitly labeled non-QFT.

8. Vacuum null test:
   exact Schwarzschild/Kerr vacuum witnesses pass without nonzero imported or relabeled
   matter stress.
```

Why this object is first:

- A variational `T_mu_nu` without the provenance ledger can still hide residuals.
- A provenance ledger without conservation cannot couple to the Bianchi identity.
- A conserved tensor without positivity/QFT status can be ghost matter or a control.
- A matter/QFT selector without the GR projection can produce matter labels that do not
  source the observer metric.
- Exact vacuum tests are impossible to interpret unless hidden stress is ruled out first.

## 7. Machine-Readable Summary

```json
{
  "artifact": "STRESS_ENERGY_SHADOW_EMERGENCE_CERTIFICATE",
  "version": "2026-06-24",
  "verdict": "CERTIFICATE_SPECIFIED_STRESS_ENERGY_SHADOW_NOT_DERIVED",
  "current_status": "specified_open_not_derived",
  "overclaim_guard": "do_not_claim_T_mu_nu_derived",
  "marble_wood_frame": {
    "einstein_complaint": "GR_has_geometric_marble_left_side_and_phenomenological_wood_T_mu_nu_right_side",
    "gu_steelman": "metric_marble_and_matter_wood_may_both_be_observer_shadows_of_deeper_source_geometry",
    "current_decision": "possibility_open_but_not_certified"
  },
  "classification_statuses": [
    "derived",
    "derived_relative",
    "hosted",
    "imported",
    "ansatz",
    "residual",
    "control",
    "blocked",
    "specified_open"
  ],
  "derived_stress_energy_criteria": [
    "branch_fixed_source_action_or_operator",
    "source_variation_derives_EL_tuple",
    "term_provenance_ledger_for_every_T_mu_nu_component",
    "observer_projection_from_s_star_g_Y",
    "conservation_from_source_Noether_Bianchi",
    "coupling_to_same_GR_shadow_branch",
    "positivity_or_physical_state_status",
    "matter_QFT_provenance_if_ordinary_matter_claimed",
    "no_hidden_residual_relabeling"
  ],
  "distinctions": [
    {
      "class": "derived",
      "definition": "computed_from_fixed_source_branch_with_variation_projection_conservation_positivity_and_QFT_or_field_provenance"
    },
    {
      "class": "imported",
      "definition": "external_SM_QFT_finite_Connes_perfect_fluid_or_phenomenological_input_supplied_before_selection"
    },
    {
      "class": "hosted",
      "definition": "ambient_source_geometry_contains_a_slot_or_representation_without_physical_selector_or_dynamics"
    },
    {
      "class": "ansatz",
      "definition": "field_or_stress_tensor_chosen_to_make_target_metric_cosmology_or_low_energy_sector_work"
    },
    {
      "class": "residual",
      "definition": "unexplained_EL_or_projection_residual_that_must_not_be_called_matter_or_Lambda_eff"
    },
    {
      "class": "control",
      "definition": "useful_arithmetic_or_executable_fixture_not_source_evidence"
    }
  ],
  "pipeline": [
    {
      "id": "SourceStressActionCertificate",
      "status": "blocked",
      "requires": ["D_GU", "S_GU_branch", "fields", "variation_space", "boundary_data", "source_selector_or_bypass"],
      "missing": ["branch_closed_primary_action", "IG_variation_closure"]
    },
    {
      "id": "VariationCertificate",
      "status": "reconstruction_only",
      "requires": ["full_EL_tuple", "S_eff_branch", "T_mu_nu_variation_with_g_equals_s_star_gY"],
      "missing": ["branch_closed_variational_identity"]
    },
    {
      "id": "SourceCurrentCertificate",
      "status": "branch_dependent_open",
      "requires": ["bare_theta_or_corrected_or_theta_eff_declared", "current_from_EL_equation"],
      "missing": ["Branch_2A_Phi_or_S_IG_dyn"]
    },
    {
      "id": "ObserverProjectionCertificate",
      "status": "missing",
      "requires": ["Pi_obs", "s_star_gY", "symmetric_T_mu_nu", "fixed_kappa_eff", "Lambda_eff_status", "residual_ledger"],
      "missing": ["full_projection_identity"]
    },
    {
      "id": "ConservationCertificate",
      "status": "blocked",
      "requires": ["source_Noether_identity", "Bianchi_projection", "nabla_mu_T_mu_nu_zero"],
      "missing": ["branch_specific_conservation_theorem"]
    },
    {
      "id": "GRShadowCouplingCertificate",
      "status": "open",
      "requires": ["same_branch_as_GR_shadow", "R_shadow_zero_or_controlled", "exact_vacuum_tests"],
      "missing": ["ELProjectedGRShadowTheorem", "Schwarzschild_Kerr_no_hidden_matter_witnesses"]
    },
    {
      "id": "EnergyPositivityCertificate",
      "status": "open",
      "requires": ["positive_physical_modes", "no_negative_norm_gauge_survivors", "energy_condition_or_named_violation"],
      "missing": ["full_branch_positivity_after_gauge_reduction"]
    },
    {
      "id": "MatterQFTProvenanceCertificate",
      "status": "blocked",
      "requires": ["matter_selector", "QFT_state_space", "state", "observables", "unitarity", "spin_statistics", "anomaly_shadow"],
      "missing": ["QFTStateSpaceExtractionCertificate", "QFTStateExtractionCertificate", "ObservableAdmissibilityCertificate"]
    }
  ],
  "branches": [
    {
      "key": "branch_2a",
      "label": "A-independent constrained IG",
      "source_current": "bare_theta_if_D_A_Phi_zero",
      "stress_energy_status": "possible_template_not_derived",
      "decision": "strongest_conservative_template_underdefined",
      "rollback": "Phi_missing_A_dependent_or_target_fitted"
    },
    {
      "key": "branch_2b",
      "label": "A-dependent constrained IG",
      "source_current": "theta_corrected_by_multiplier_current",
      "stress_energy_status": "must_include_multiplier_current",
      "decision": "possible_not_bare_theta",
      "rollback": "bare_theta_claim_retained_despite_D_A_Phi_nonzero"
    },
    {
      "key": "branch_3",
      "label": "dynamical IG total current",
      "source_current": "theta_eff",
      "stress_energy_status": "depends_on_written_S_IG_dyn",
      "decision": "honest_fallback_action_unwritten",
      "rollback": "theta_eff_not_used_or_S_IG_dyn_unspecified"
    },
    {
      "key": "free_beta",
      "label": "bare free beta norm",
      "source_current": "theta_equals_zero",
      "stress_energy_status": "fails_nonzero_theta_stress",
      "decision": "rejected",
      "rollback": "none_branch_rejected"
    },
    {
      "key": "background_stueckelberg",
      "label": "background or Stueckelberg IG",
      "source_current": "spurion_theta_possible",
      "stress_energy_status": "host_or_thin_background_not_full_derivation",
      "decision": "viable_host_only",
      "rollback": "Noether_background_variations_unaccounted"
    },
    {
      "key": "finite_control_host_import",
      "label": "finite-control host/import",
      "source_current": "ordinary_matter_only_after_selector_and_QFT_shadow",
      "stress_energy_status": "hosted_imported_not_derived",
      "decision": "partial_Pati_Salam_branch_no_full_matter_stress",
      "rollback": "A_F_G_SM_K_SM_or_ordinary_SM_shadow_used_as_input"
    }
  ],
  "claim_certificates": [
    {
      "id": "STRESS-ENERGY-SHADOW",
      "status": "specified_open",
      "proof_grade": "specification",
      "finality": "not_final",
      "decision": "not_derived",
      "forbidden_shortcuts": ["residual_relabeling", "weak_field_as_stress_derivation", "IC4_as_full_branch_certificate", "imported_QFT_matter_as_derived"],
      "rollback_conditions": ["missing_source_provenance", "missing_variation", "missing_conservation", "hidden_matter_needed", "positivity_failure"]
    },
    {
      "id": "SOURCE-CURRENT",
      "status": "branch_dependent_open",
      "proof_grade": "reconstruction_specification",
      "finality": "not_final",
      "decision": "bare_theta_not_generally_certified",
      "forbidden_shortcuts": ["Branch_2B_called_bare_theta", "Branch_3_called_bare_theta", "free_beta_nonzero_theta"],
      "rollback_conditions": ["Branch_2A_Phi_missing", "Branch_3_without_theta_eff", "free_beta_only_theta_norm"]
    },
    {
      "id": "LAMBDA-DARK-ENERGY-PATCH",
      "status": "open_patch_slot",
      "proof_grade": "specification",
      "finality": "not_final",
      "decision": "not_derived",
      "forbidden_shortcuts": ["bare_Lambda_as_marble", "fitted_xi_eff_as_source", "target_tuned_dark_energy_fluid", "residual_to_Lambda_eff"],
      "rollback_conditions": ["coefficient_inserted_after_target_data", "no_generated_Z_theta_C_Rtheta_xi_eff", "conservation_failure", "exact_GR_compatibility_failure"]
    },
    {
      "id": "MATTER-SHADOW",
      "status": "partial_open",
      "proof_grade": "reconstruction_contract",
      "finality": "not_final",
      "decision": "Pati_Salam_branch_evidence_not_full_matter_stress",
      "forbidden_shortcuts": ["A_F_import", "G_SM_import", "K_SM_import", "physical_Higgs_inserted", "ordinary_SM_shadow_assumed"],
      "rollback_conditions": ["target_data_consumed_by_selector", "extra_anomalous_modes", "Higgs_projection_or_potential_missing"]
    },
    {
      "id": "QFT-STRESS",
      "status": "blocked",
      "proof_grade": "specification",
      "finality": "not_final",
      "decision": "ordinary_matter_stress_needs_QFT_shadow",
      "forbidden_shortcuts": ["representation_labels_as_states", "Bell_control_as_state", "formal_path_integral_without_positivity"],
      "rollback_conditions": ["no_positive_state_space", "no_source_derived_state", "no_admissible_observables", "nonunitary_dynamics", "anomaly_failure"]
    }
  ],
  "forbidden_shortcuts": [
    "hidden_matter_relabeling",
    "residual_to_T_mu_nu",
    "residual_to_Lambda_eff",
    "bare_Lambda_as_marble",
    "fitted_xi_eff_as_source",
    "target_tuned_dark_energy_fluid",
    "Q_TF_B_named_matter_without_variation",
    "Willmore_residual_called_vacuum_stress",
    "weak_field_compatibility_as_T_mu_nu_derivation",
    "IC4_reconstruction_as_full_branch_certificate",
    "imported_SM_QFT_as_GU_derived",
    "hosted_representation_as_physical_matter",
    "ansatz_fluid_or_scalar_as_derivation",
    "Branch_2B_or_3_called_bare_theta",
    "free_beta_nonzero_theta",
    "ordinary_SM_anomaly_as_full_GU_shadow"
  ],
  "first_missing_proof_object": {
    "id": "NoHiddenMatterStressEnergyShadowTheorem",
    "requires": [
      "branch_fixed_S_GU",
      "D_GU_and_physical_field_complex",
      "variation_space",
      "source_current_law",
      "observer_projection",
      "term_provenance_ledger",
      "conservation_theorem",
      "positivity_or_QFT_theorem",
      "vacuum_no_hidden_matter_test"
    ],
    "prevents": ["hidden_matter_relabeling", "import_as_derivation", "host_as_selector", "ansatz_as_proof", "residual_absorption"]
  },
  "next_step": "build_term_provenance_ledger_for_Branch_2A_or_reject_Phi_then_rewrite_to_Branch_3_theta_eff"
}
```

## 8. Next Meaningful Proof/Computation Step

Do one branch-local anti-smuggling packet:

```text
Attempt a Branch 2A term provenance ledger for stress-energy.
```

Minimum packet:

1. Decide whether a source-derived, gauge-covariant, A-independent
   `Phi(eps,beta,s)=0` exists. If no, stop Branch 2A and switch to Branch 3
   total-current language.
2. For the chosen branch, list every candidate term in `T_mu_nu^shadow`:

   ```text
   YM, mixed flux, Dirac-DeRham, Shiab, distortion/section, IG/theta,
   multiplier or total current, Higgs/matter/QFT terms, trace/Lambda terms.
   ```

3. For each term, fill:

   ```text
   source term -> variation -> observer projection -> conservation -> positivity/QFT
   status -> rollback.
   ```

4. Any row without full provenance is marked `residual`, `hosted`, `imported`, `ansatz`,
   or `control`, not `derived`.
5. Replay the exact Schwarzschild/Kerr vacuum gate with the rule:

   ```text
   no nonzero imported, ansatz, hosted, or relabeled matter stress may be used to
   cancel the vacuum section residual.
   ```

6. In parallel, connect to the QFT-shadow next step: ordinary matter stress requires a
   source-derived state space, state, observables, and anomaly-complete observer shadow
   before it can enter `T_mu_nu^shadow` as derived matter.

This is the smallest proof object that would decide whether the right-hand side of
Einstein's equation has stopped being phenomenological wood and become a GU-derived
observer-facing shadow.

## Sources Read

- `process/runbooks/five-lane-frontier-run.md`
- `explorations/geometry-curvature-emergence/gr-shadow-recovery-certificate-2026-06-24.md`
- `explorations/misc/constraint-first-ig-tangent-space-gate-2026-06-24.md`
- `explorations/geometry-curvature-emergence/exact-schwarzschild-kerr-el-gate-2026-06-24.md`
- `explorations/cycle-gates-and-audits/gu-action-4d-physics-gate-2026-06-24.md`
- `explorations/cycle-gates-and-audits/gu-minimal-action-spec-2026-06-24.md`
- `explorations/misc/gu-closed-loop-action-ig-branch-2026-06-24.md`
- `explorations/cycle-gates-and-audits/finite-control-provenance-audit-2026-06-24.md`
- `explorations/geometry-curvature-emergence/matter-gauge-source-geometry-selector-gate-2026-06-24.md`
- `explorations/cycle-gates-and-audits/live-claim-dag-fault-finality-ledger-2026-06-24.md`
- `explorations/cycle-gates-and-audits/qft-shadow-extraction-certificate-2026-06-24.md`
- `explorations/geometry-curvature-emergence/ic4-lagrangian-tmunu-derivation-2026-06-23.md`
