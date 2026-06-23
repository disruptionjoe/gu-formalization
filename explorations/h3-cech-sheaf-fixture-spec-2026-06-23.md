---
title: "H3 Cech Sheaf Fixture Specification"
status: exploration
doc_type: research_note
updated_at: "2026-06-23"
problem_label: "h3-cech-sheaf-fixture-spec"
verdict: OPEN_SPECIFIED_NOT_EXECUTABLE
---

# H3 Cech Sheaf Fixture Specification

## Scope

Task: run the full H3 bridge fixture step as far as possible without updating shared
docs. This note specifies the missing `cech_sheaf_fixture` precisely enough for later
implementation, including:

- C1: the type bridge from TaF finality data to flat `Z/2Z` gauge data on the GU
  observerse.
- C2: an executable fixture contract for the Cech/sheaf test.
- C3: the spacelike-overlap repair needed before the H3 restriction maps are
  geometrically meaningful.

The result is a specification, not a completed execution. The sibling
`temporal-issuance` repo contains only route labels and prose requirements for
`cech_sheaf_fixture`; it does not contain a runnable fixture artifact.

## Inputs Read

GU formalization:

- `explorations/taf-h3-contact-2026-06-23.md`.
- `explorations/n3-h3-cech-holonomy-2026-06-23.md`.
- `explorations/n3-h3-cech-fixture-execution-2026-06-23.md`.
- `NEXT-STEPS.md`, `RESEARCH-STATUS.md`, and `DERIVATION-PROGRESS.md` H3/N3
  references.

Temporal Issuance, read-only:

- `explorations/E014-cetext-witness-obligations-lens-survey.md`.
- `agent-runs/RUN-0036-cetext-witness-obligations.md`.
- `explorations/E015-holonomy-fixture.md`.
- `agent-runs/RUN-0037-holonomy-fixture.md`.
- `agent-governance/NEXT-TRIGGER-PLAN.md`.
- `explorations/E019-online-schema-sys-no-anticipation.md`.
- `agent-runs/RUN-0042-online-schema-sys-no-anticipation.md`.
- `explorations/E024-presheaf-ab-absorber-test.md`.
- `agent-runs/RUN-0044-presheaf-ab-absorber-test.md`.
- `tests/README.md`.

## Current H3 State

T63's H3-independent layer is unchanged:

- the four-context Cech computation over `Z/2Z` is valid;
- the nontrivial class has loop product `-1`;
- the GU spin-observerse holonomy computation has the same `Z/2Z` loop shape.

The identity claim remains blocked. H3 requires more than parallel computations. It
requires the TaF finality presheaf transition function and the GU flat `Z/2Z`
holonomy to be the same object under an explicit bridge.

Current verdict:

```yaml
h3_identity_form: open
h3_without_bridge: structural_analogy_only
blocking_conditions:
  C1: type_bridge_missing
  C2: cech_sheaf_fixture_missing
  C3: spacelike_overlap_unfixed
```

## What Could Be Executed

No temporal-issuance fixture could be run. I executed only read-only discovery:

```yaml
artifact_discovery:
  exact_symbol_search: cech_sheaf_fixture
  related_searches:
    - cech
    - sheaf_fixture
    - fixture
    - test
    - script
  tests_directory: tests/README.md only
  executable_scripts_found: none
  fixture_files_found:
    - explorations/E015-holonomy-fixture.md
    - agent-runs/RUN-0037-holonomy-fixture.md
  cech_sheaf_fixture_found: false
```

The existing executable-adjacent artifacts are prose records. `E015` executes the
holonomy fixture and concludes:

```yaml
bare_ext_s_derives_nontrivial_holonomy: false
transport_enriched_ext_s_has_nontrivial_holonomy: true
next_fixture: cech_sheaf_fixture
```

That result is directly relevant but not itself the Cech/sheaf fixture. It says a
closed extension loop supplies a loop word, not a group element, unless a transport
functor or equivalent transition rule is supplied or independently derived.

## Why Execution Remains Blocked

`cech_sheaf_fixture` is missing at three levels:

```yaml
missing_artifact:
  file: no exploration, test, script, or workflow implementation exists
  command: no CLI/test target exists
  data: no machine-readable cover/section/overlap fixture exists
missing_spec:
  compatibility_predicate: C-typed section compatibility is not defined
  cover_data: two-patch S^1 or CHSH four-cycle data is not encoded
  transition_rule: no source rule derives allowed Z/2Z overlap values
  provenance_guard: no check prevents smuggled preselected cocycles
```

So the result is not "fixture failed." The result is:

```yaml
execution_status: NOT_RUN
reason: fixture artifact and compatibility predicate unavailable
stronger_blocker: OPEN_BLOCKED_ON_FIXTURE_SPECIFICATION
```

## C1: Type-Bridge Requirement

H3 needs a natural bridge between two unlike objects:

```text
TaF side: finality presheaf sections / D1 finality profiles
GU side: flat Z/2Z gauge local trivializations on observer-section images in Y_spin
```

The minimum acceptable type bridge is not a label match. It must be a natural
isomorphism, or an explicitly justified quotient isomorphism, between the Cech data
computed on the TaF side and the flat local-system data computed on the GU side.

### C1 Data

Define:

```yaml
taf_cover:
  base: context cover K
  minimal_source_fixture: two_patch_s1
  t63_target_fixture: chsh_four_cycle

taf_finality_presheaf:
  symbol: F_TaF
  type: Open(K)^op -> Set
  section: C-typed admissible finality profile over a patch
  restriction: profile restriction to an overlap, using only current admissibility data

parity_extractor:
  symbol: q
  type: F_TaF(U) -> Z2Torsor(U)
  requirement: derived from C-typed admissibility, not chosen per cover

gu_flat_system:
  symbol: L_GU
  type: locally constant Z/2Z local system on the observer-section correspondence
  section: local flat trivialization over sigma_alpha(X_alpha)
  transition: locally constant g_alpha_beta in {+1, -1}
```

The bridge object is:

```text
eta_U: q(F_TaF(U)) ~= L_GU(U)
```

with naturality:

```text
eta_V(res^F_{U,V}(s)) = res^L_{U,V}(eta_U(s))
for every V subset U.
```

### C1 Pass Conditions

C1 passes only if all of the following are true:

1. `q` is defined uniformly from TaF admissibility data, not from the desired
   holonomy answer.
2. `q` preserves restrictions on every overlap in the cover.
3. The induced transition values are locally constant `Z/2Z` values, so they define
   a flat local system.
4. The induced Cech 1-cochain on the TaF side is the same transition object used by
   the GU holonomy computation after `eta`, not a separately matched label.
5. If two TaF finality sections differ in admissibility-relevant content but map to
   the same `Z/2Z` value, the note must state whether H3 only needs a quotient
   bridge. Without this quotient declaration, information loss fails C1.

### C1 Failure Conditions

```yaml
C1_TYPE_FAIL:
  - no q from finality profiles to Z/2Z torsors is defined
  - q is chosen from the desired cocycle
  - restriction maps do not commute with q
  - GU data is smooth/continuous while TaF data remains only combinatorial, with no
    discrete subcategory or quotient bridge
  - the bridge identifies values post hoc but not sheaves/local systems
```

## C2: Executable `cech_sheaf_fixture` Contract

The fixture must answer one question:

```text
Does C-typed admissibility independently determine allowed overlap cocycles?
```

It must not merely demonstrate that a nontrivial Cech class exists. `E024` and
`RUN-0044` show that generic no-global-section or Cech witnesses are absorbed by
Abramsky-Brandenburger-style sheaf contextuality. The fixture only survives if the
sheaf or compatibility predicate is determined by the source admissibility rule.

### C2 Minimal Cover

The minimal source-side fixture should use a two-patch cover of `S^1`:

```yaml
cover_id: two_patch_s1
patches: [U0, U1]
overlap_components:
  - I_plus
  - I_minus
group: Z2
values: [+1, -1]
```

This cover computes `H^1(S^1, Z/2Z) = Z/2Z` as follows:

```text
cochain: (g_plus, g_minus), one Z/2Z value on each overlap component
holonomy: g_plus * g_minus
coboundary/trivial class: holonomy = +1
nontrivial class: holonomy = -1
```

The T63 transfer fixture should then use the CHSH four-cycle:

```yaml
cover_id: chsh_four_cycle
contexts: [AB, ABp, ApBp, ApB]
edges:
  - [AB, ABp]
  - [ABp, ApBp]
  - [ApBp, ApB]
  - [ApB, AB]
holonomy: product of four edge transitions
```

### C2 Required Inputs

An implementation must accept a machine-readable fixture:

```yaml
fixture_name: cech_sheaf_fixture
version: 1
cover:
  id: two_patch_s1
  patches: [U0, U1]
  overlap_components: [I_plus, I_minus]
source_system:
  schema_state: S_n
  history: H_n
  admissibility_predicate: A_n
  extension_rule: Ext_S
  no_anticipation: true
sections:
  U0: generated_by_C
  U1: generated_by_C
compatibility_predicate:
  name: C_overlap
  inputs: [patch_i, section_i, patch_j, section_j, overlap_component, H_n, S_n]
  output: allowed_transition_subset_of_Z2
  forbidden_inputs:
    - global_loop_product
    - desired_holonomy
    - future_schema
    - preselected_transition_table_without_C_provenance
```

### C2 Algorithm

For each patch, generate all C-typed local sections:

```text
Sec_C(U_i) = {s | A_n says s is admissible on U_i}
```

For each overlap component, compute:

```text
T_ij^k(s_i, s_j) = C_overlap(s_i, s_j, I_k) subset {+1, -1}
```

Then classify:

```yaml
if any required T_ij^k is empty:
  verdict: NO_COMPATIBLE_LOCAL_SYSTEM

if any required T_ij^k == {+1, -1}:
  verdict: UNDERDETERMINED_TRANSPORT
  meaning: C-admissibility does not force cocycle values

if every required T_ij^k is a singleton:
  induced_cochain: the forced singleton values
  holonomy: product around the loop
  if holonomy == -1:
    verdict: DERIVED_NONTRIVIAL_COCYCLE
  if holonomy == +1:
    verdict: DERIVED_TRIVIAL_COCYCLE

if any transition value is read from input data marked stipulated:
  verdict: STIPULATED_TRANSPORT
```

### C2 Required Output

```yaml
fixture_result:
  cover_id: two_patch_s1
  local_sections:
    U0: [...]
    U1: [...]
  overlap_transition_candidates:
    I_plus: [...]
    I_minus: [...]
  forced_cochain: null_or_values
  holonomy: null_or_plus_minus_1
  coboundary: null_or_boolean
  transition_provenance:
    I_plus: derived_from_C | stipulated | underdetermined
    I_minus: derived_from_C | stipulated | underdetermined
  no_anticipation_check: pass_or_fail
  ab_absorber_check:
    generic_sheaf_only: true_or_false
    C_supplies_compatibility: true_or_false
  verdict: one_of_the_C2_verdicts
```

### C2 Success, Failure, and Transfer

The only result that can advance H3 is:

```yaml
C2_success:
  verdict: DERIVED_NONTRIVIAL_COCYCLE
  transition_provenance: all derived_from_C
  no_anticipation_check: pass
  ab_absorber_check:
    generic_sheaf_only: false
    C_supplies_compatibility: true
```

The most likely results, based on `E015`, are:

```yaml
expected_failures:
  UNDERDETERMINED_TRANSPORT:
    meaning: bare admissibility gives sections but no Z/2Z values
  STIPULATED_TRANSPORT:
    meaning: nontrivial cocycle exists only because transition data was inserted
  DERIVED_TRIVIAL_COCYCLE:
    meaning: admissibility forces identity product only
```

After the two-patch source fixture, the same contract must be rerun on the CHSH
four-cycle. H3 only advances if the CHSH run derives the same transition object
that maps under C1 to the GU flat `Z/2Z` holonomy.

## C3: Spacelike-Overlap Fix

The old H3 wording uses a literal geometric overlap:

```text
sigma_A(X_A) cap sigma_B(X_B)
```

For spacelike-separated observers this intersection may be empty. Then the
restriction map in the dictionary is undefined. The fix is to replace literal
intersection with a correspondence overlap indexed by shared context labels.

### C3 Replacement Object

Let `L` be the context-label category:

```yaml
labels:
  observer_settings: [A, Ap, B, Bp]
  contexts: [AB, ABp, ApB, ApBp]
  edge_relation: contexts share exactly one setting label
```

For two contexts `alpha` and `beta` sharing label `ell`, define the overlap
correspondence:

```text
O_{alpha,beta,ell}
  = sigma_alpha(X_alpha) x_{ell} sigma_beta(X_beta)
```

This is not a spacetime intersection. It is a span:

```text
sigma_alpha(X_alpha) <- O_{alpha,beta,ell} -> sigma_beta(X_beta)
```

whose points are comparison records:

```yaml
comparison_record:
  left_section_point: y_alpha in sigma_alpha(X_alpha)
  right_section_point: y_beta in sigma_beta(X_beta)
  shared_label: ell
  fiber_comparison:
    type: flat_Z2_transporter_or_identification
    source: context-label comparison rule
  no_signal_condition: true
```

The restriction maps in H3 must be pullbacks along this span:

```text
res_alpha_beta = pullback to O_{alpha,beta,ell}, not literal set intersection
```

### C3 Pass Conditions

C3 passes if:

1. every CHSH edge has a nonempty correspondence overlap;
2. the correspondence is label-indexed, not causal signaling between spacelike
   regions;
3. the `Z/2Z` transporter on the correspondence is flat and composable around
   the four-cycle;
4. gauge changes at either endpoint conjugate consistently, which is trivial for
   abelian `Z/2Z` but still must be recorded;
5. the Cech restriction used by C2 and the GU holonomy restriction used by C1
   refer to the same correspondence object.

### C3 Failure Conditions

```yaml
C3_OVERLAP_FAIL:
  - the fixture uses literal spacetime intersection for spacelike-separated
    observers
  - the replacement correspondence is not specified
  - the comparison transporter is stipulated independently of C1/C2
  - the construction allows superluminal information transfer rather than a
    shared-label comparison
```

## Integrated H3 Bridge Fixture

The full fixture should run in this order:

```yaml
step_1_C3_geometry:
  build_context_correspondence_overlaps: required
  fail_if_literal_spacelike_intersection_required: true

step_2_C1_type_bridge:
  build_q_from_TaF_finality_to_Z2: required
  prove_restriction_naturality: required
  fail_if_only_label_matching: true

step_3_C2_source_fixture:
  run_two_patch_s1: required
  classify_transition_provenance: required
  fail_if_transition_values_stipulated: true

step_4_C2_CHSH_transfer:
  run_chsh_four_cycle: required
  compare_induced_cochain_to_GU_holonomy_under_C1_C3: required

step_5_H3_verdict:
  if C1_pass and C2_derived_nontrivial and C3_pass:
    h3: DERIVED_CANDIDATE
  if C1_pass and C2_derived_trivial and C3_pass:
    h3: FAILS_FOR_T63_NONTRIVIAL_IDENTITY
  if C2_stipulated_or_underdetermined:
    h3: STIPULATION_NOT_THEOREM
  if C1_fail_or_C3_fail:
    h3: UNSTATABLE_IN_CURRENT_FORM
```

## Concrete Implementation Skeleton

A later implementation can be a small enumerator. It does not need physics code.
The minimum viable test target is a pure finite computation:

```text
input:  fixture YAML/JSON
output: fixture_result YAML/JSON plus a short markdown report
logic:  enumerate C-typed sections, compute allowed Z/2Z transitions, multiply loop values
```

Suggested test cases:

```yaml
tests:
  bare_sections_no_transition_rule:
    expected: UNDERDETERMINED_TRANSPORT
  stipulated_nontrivial_transition_table:
    expected: STIPULATED_TRANSPORT
  equality_only_compatibility:
    expected: DERIVED_TRIVIAL_COCYCLE
  source_forced_orientation_flip:
    expected: DERIVED_NONTRIVIAL_COCYCLE
    requirement: the flip must be computed from C_overlap, not from a preloaded cocycle
  chsh_transfer_from_two_patch_success:
    expected: H3_DERIVED_CANDIDATE only if C1 and C3 also pass
```

The important implementation discipline is provenance. Every transition value must
carry one of:

```yaml
provenance_labels:
  - derived_from_C
  - stipulated_input
  - underdetermined_by_C
  - forced_identity_by_C
```

Only `derived_from_C` can support H3 as a theorem.

## Verdict

The full H3 bridge fixture cannot be executed from current artifacts. The strongest
result achieved here is a precise fixture contract.

```yaml
verdict: OPEN_SPECIFIED_NOT_EXECUTABLE
h3_status: OPEN
what_advanced:
  - C1 type-bridge is specified as a natural Z/2Z local-system bridge
  - C2 executable fixture contract is specified
  - C3 spacelike-overlap fix is specified as a context-label correspondence span
what_did_not_advance:
  - no derived C-typed compatibility predicate was found
  - no temporal-issuance executable fixture exists
  - no Cech cocycle values were derived from source admissibility
next_required_artifact:
  repo: temporal-issuance
  artifact: executable cech_sheaf_fixture
  minimum_content:
    - machine-readable two-patch S^1 fixture
    - C_overlap compatibility predicate
    - transition provenance checks
    - CHSH four-cycle transfer case
    - C1/C3 bridge checks
```

Until that artifact exists and returns `DERIVED_NONTRIVIAL_COCYCLE` with
`derived_from_C` provenance, T63's identity form remains conditional on H3. Without
that result, the H3 bridge remains a structural analogy or a stipulation, not a
derived theorem.
