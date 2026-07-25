---
title: "GU twistor-reality reconstruction swing"
status: completed
doc_type: run-plan-and-receipt
run_id: RUN-20260725-025239-gu-formalization-twistor-reality-reconstruction
owner_service_id: RUN-20260725-025239-gu-formalization-twistor-reality-reconstruction
parent_run_id: null
owner_id: gu-formalization
workflow: repo-progress-run
workflow_revision: sha256:09ceebd5cdcb21090c418dd504a529b7bd10a906f5709a709a70f14d9adc918c
mode: execute
lane_id: "1"
starting_revision: 4580fa6e1fa7cadc1b350aa075a0def5ff2613b8
resume_capsule:
  transition: "Switching to Run: gu-formalization — reconstruct Minkowski and Euclidean real forms from one twistor substrate, then test the exact missing GU bridge — Progress — writes limited to GU plus the required workspace memory log."
method_refs: []
---

# GU twistor-reality reconstruction swing

Plan created at: 2026-07-24T21:52:39-05:00

Status: completed

Formal phase: `progress`

CapacityOS Run:
`RUN-20260725-025239-gu-formalization-twistor-reality-reconstruction`

Parent Run: `none`

Target: `gu-formalization`

Workflow: `system-runtime#repo-progress-run`

Workflow source:
`repos/private/system-runtime/runtime/workflows/repo-progress-run.md`

Workflow revision:
`sha256:09ceebd5cdcb21090c418dd504a529b7bd10a906f5709a709a70f14d9adc918c`

Mode: `system-canon#execute`

Starting revision: `4580fa6e1fa7cadc1b350aa075a0def5ff2613b8`

Owner workflow: `none`

Method refs: `[]`

## Objective

Take the next large Lane 1 swing implied by the Woit-principles transfer:
treat Minkowski spacetime as a reconstructed real form of a richer twistor
substrate rather than as the starting object.

Build and adversarially test one integrated reconstruction diamond:

```text
complex twistor/incidence geometry
+ Lorentzian or Euclidean real structure
+ field/bundle data
+ OS reflection and positivity data
-> reconstructed physical spacetime and carrier.
```

The material target is an executable packet that:

1. reconstructs the flat Minkowski chart from the Grassmannian/incidence
   substrate and verifies the determinant/conformal metric relation;
2. constructs the distinct Euclidean quaternionic real form and proves that
   it is not the same operation as Lorentzian reality;
3. supplies a finite OS positivity control with a planted failure;
4. maps every reconstruction input to the actual GU observer, carrier,
   Hodge/Krein, deck, action, and soldering interfaces;
5. returns a precise constructor, obstruction, or source-gap verdict without
   promoting a GU claim.

## Exploration / Resume Capsule

- Transition: `Switching to Run: gu-formalization — reconstruct Minkowski and Euclidean real forms from one twistor substrate, then test the exact missing GU bridge — Progress — writes limited to GU plus the required workspace memory log.`
- Question and current understanding: the previous swing proved the finite
  `Gr(2,C^4)` substrate and OS direction controls separately. Joe observed
  that starting from Minkowski spacetime hides much of what is interesting in
  twistor geometry. The construction should therefore derive Minkowski and
  Euclidean spacetime from common holomorphic data and identify the added
  physical-reality inputs.
- Relevant source pointers:
  `explorations/woit-principles/README.md`;
  `explorations/woit-principles/twistor-grassmannian-kernel-2026-07-24.md`;
  `explorations/woit-principles/woit-os-physical-real-form-gate-2026-07-24.md`;
  `GEOMETER-VS-PHYSICS-OBJECTS.md`;
  current GU carrier, physical-signature, observer, and soldering authorities;
  Woit's 2021, 2023, and 2026 primary sources plus standard twistor references.
- Unresolved questions:
  whether the Lorentzian Hermitian-matrix chart and Euclidean quaternionic
  slice can be encoded in one exact finite diamond; which conjugation acts on
  the twistor line and field cohomology; whether OS positivity is geometric or
  action-dependent; and whether GU supplies any native map into this substrate.
- Selected workflow / owner method refs:
  `system-runtime#repo-progress-run`; no local method experiment.
- Prior not-authorized boundary:
  no claim, canon, verdict, scientific-grade, public-posture, Lane-control, or
  non-GitHub external action.
- Last closed phase:
  `runs/RUN-20260725-021645-gu-formalization-woit-principles.md`.
- Current phase:
  Lane 1 Progress, human-direct, explicitly orchestrated by Joe.
- Next action:
  run independent source-geometry, GU-interface, and computational-design legs,
  converge them into one construction, then implement the exact and numerical
  kernels.
- Blocker / exact wake condition:
  stop on a live writer, authority drift, a real-form formula that cannot be
  sourced or independently checked, a planted control that fails, or a
  conclusion requiring scientific-status movement.
- Revision pins:
  owner `4580fa6e1fa7cadc1b350aa075a0def5ff2613b8`;
  default branch contained in owner with `24/0` owner/default divergence;
  workflow graph
  `09ceebd5cdcb21090c418dd504a529b7bd10a906f5709a709a70f14d9adc918c`.

## Governance References

- `AGENTS.md`
- `RESEARCH-POSTURE.md`
- `GEOMETER-VS-PHYSICS-OBJECTS.md`
- `CONTRIBUTING.md`
- `LANES.yaml`
- `repos/private/nbl-governance-operations/relationships/registry.yaml#NBL-REL-003`
- `repos/private/system-operations/stewards/gu-formalization/README.md`
- `repos/private/system-runtime/runtime/workflows/standard-run-safety-rules.md`

## Construction-Fork Guard

Every leg must name which object it uses and why:

| role | standard twistor/physics object | GU-native fork and required check |
|---|---|---|
| physical state space | positive Hilbert space reconstructed by OS positivity | GU begins with a Krein carrier; do not import positivity or a quotient |
| real form | Lorentzian `SU(2,2)` or Euclidean quaternionic structure on `C^4` | GU's physical `192/384` carrier and deck/orientation data need a typed map |
| spacetime metric | determinant conformal class on `Herm(2)` | distinguish the horizontal-normalized base metric from the gimmel/DeWitt metric; a distorted section's vertical slope can alter the full pullback |
| soldering | incidence/tetrad or Cartan frame data | GU's proposed `pi=spin-lift(grad^gimmel)` remains unforced under H27 |
| chirality | holomorphic twistor/cohomology chirality | one Lorentzian GU Hodge half is `K`-null and conjugation-exchanged |
| gauge data | holomorphic bundles and standard stabilizers | program-native super-IG, real `Spin(6,4)`, complex `Spin(10,C)`, and any compact comparison real form must be related by one declared adapter type, not renamed |

A negative result is accepted only for the construction on which it is proved
and after checking whether the other fork survives.

## Lane Selection

- Owner ID and scope: `gu-formalization | repository`
- Lane: `1`
- Manifest SHA-256:
  `5c535ae8674718dc2f2bfedf21bfe4c04ac9cceafe62bbfe1428e3814da9f083`
- Definition/control revisions: `1 | 1`
- Directed-flow revision: `none`
- Selection basis:
  Joe directly authorized the next big swing after the Woit-principles packet.
  The work attacks whether a richer twistor substrate can construct, rather
  than merely host, GU's missing Lorentzian physical-real-form and soldering
  data. It is adversarial Lane 1 truth testing.
- Context capsule:
  owner authority `AGENTS.md`;
  construction fork `GEOMETER-VS-PHYSICS-OBJECTS.md`;
  posture `RESEARCH-POSTURE.md`;
  active Lane 1 control `LANES.yaml`;
  accepted NBL relationship `NBL-REL-003`;
  source and work references above.
- Effective permission intersection:
  Joe's direct request plus active Lane 1 permits GU-local exploration notes,
  exact and numerical tests, local navigation, a Run receipt, routine
  versioning, and the required workspace memory entry. Deny-wins excludes
  claim/canon/verdict/public-posture movement, hidden conventional defaults,
  cross-owner writes, publication, deployment, and other non-GitHub external
  action.
- Emergency-revocation evidence:
  `repos/private/system-runtime/operations/lane-emergency-revocations.yaml`
  digest
  `8a992d3eb3f61b51ef83aa7cb8f85a1865fd0bf76c1f690429fa200a1c698723`;
  revision `1`, entries `[]`, no matching revocation.

## Formal Hypotheses and Predeclared Outcomes

### `TR-1`: Lorentzian reconstruction

After freezing the off-diagonal signature-`(2,2)` Hermitian form
`H=[[0,I],[I,0]]`, the Hermitian `2 x 2` big cell inside the isotropic
Grassmannian reconstructs a real four-dimensional Minkowski conformal
geometry:

```text
x in Herm(2),  det(x)=x_0^2-x_1^2-x_2^2-x_3^2,
L_x = graph(i x) in Gr(2,C^4).
```

The translation-invariant causal test is
`L_x intersect L_y != 0 iff det(x-y)=0`; the graph chart does not include
conformal infinity.

### `TR-2`: Euclidean reconstruction

A quaternionic antilinear map `J` with `J^2=-1` selects `J`-invariant complex
two-planes, giving the Euclidean `HP^1`/`S^4` real form, while projective
twistor space has no `J`-fixed points.

### `TR-3`: reality structures are load-bearing

Lorentzian and Euclidean reconstruction use inequivalent reality data.
Holomorphic incidence alone does not select either physical signature, a time
orientation, or OS reflection.

### `TR-4`: OS positivity is dynamics-dependent

A finite positive-energy covariance gives a positive reflection Gram matrix;
a signed spectral weight supplies the planted negative control. Reflection
geometry plus an antilinear map alone does not prove positivity. The
load-bearing datum is the Schwinger hierarchy/functional, often established
from an action or measure; full reconstruction also needs the remaining OS
axioms and growth/regularity conditions.

### `TR-5`: GU transfer

The current GU repository either supplies a typed map for every field in the
reconstruction diamond or returns a named missing-interface ledger. A standard
twistor identity cannot stand in for a program-native carrier, action,
Krein-physical quotient, deck lift, or solder map.

Predeclared terminal labels:

- `TWISTOR-REALITY-GU-CONSTRUCTOR`: one typed GU-native reconstruction closes.
- `TWISTOR-REALITY-KERNEL-BUILT-GU-MAP-OPEN`: the standard reconstruction
  diamond closes, but one or more GU-native maps remain open.
- `TWISTOR-REALITY-OS-POSITIVITY-FAIL`: the candidate GU reflection form fails.
- `TWISTOR-REALITY-INCOMPATIBLE`: the required real structures or carrier maps
  are mutually inconsistent under the frozen premises.
- `TWISTOR-REALITY-UNDERDEFINED`: source-owned fields are insufficient even to
  type the candidate.

## Recent Run Collision Check

- Recent run:
  `runs/RUN-20260725-021645-gu-formalization-woit-principles.md`.
- Its receipt is complete and its branch was pushed clean/even at `4580fa6`.
- No other run artifact modified in the last three hours is open.
- The writer-lock path `.git/capacityos-writer.lock` is absent.
- Working tree at selection: clean.
- Collision decision: proceed on the same branch as the explicit successor
  swing, with new files and bounded updates to the prior Woit indexes.

## Expected Writable Surfaces

- `runs/RUN-20260725-025239-gu-formalization-twistor-reality-reconstruction.md`
- `explorations/woit-principles/gu-twistor-reality-reconstruction-2026-07-24.md`
- `explorations/woit-principles/README.md`
- `explorations/README.md`
- `tests/woit-principles/test_twistor_real_slice_reconstruction.py`
- `tests/woit-principles/test_os_reconstruction_kernel.py`
- `tests/woit-principles/README.md`
- `tests/README.md`
- workspace-required `memory/log.md` and, if the result is durable,
  `memory/summary.md`

## Orchestration Plan

Three independent legs may run concurrently after this plan exists:

1. **Source geometry:** derive and source the Lorentzian isotropic-plane,
   Hermitian-matrix, Euclidean quaternionic, and OS reconstruction statements.
2. **GU interface:** map the diamond into current GU-native observer, carrier,
   Hodge/Krein, deck, action, and soldering surfaces; return exact source gaps.
3. **Computational design:** implement the finite real-slice and OS positivity
   controls in the two declared test files, with exact checks where available
   and NumPy only for the numerical spectral stress test.

Root converges the legs, writes the synthesis, runs hostile validation, and
owns all navigation, receipt, staging, commit, and push effects.

## Required Checks

- Every standard reconstruction identity has a primary or standard reference
  and an independent executable control.
- Lorentzian determinant, isotropic graph, null-separation/incidence,
  quaternionic square, invariant/non-invariant-plane, projective-square, and
  no-fixed-twistor checks pass.
- OS positive and negative controls pass under NumPy and expose numerical
  tolerance.
- Existing Woit-principles kernels and H27 remain unchanged and pass.
- GU mapping names source lines and never silently replaces a native object.
- Navigation/count manifests, JSON/YAML parsing, path hygiene, and applicable
  process gates pass.
- `git diff --check` passes.

## Flow Contract

- Pinned workflow graph:
  `system-runtime#repo-progress-run@sha256:09ceebd5cdcb21090c418dd504a529b7bd10a906f5709a709a70f14d9adc918c`
- Required graph attested: pending
- Conditional flows expected:
  `rerank-next-work` and `classify-artifact-disposition`;
  `refresh-lane-state` only if semantic Lane state changes.
- Required-flow exceptions: none anticipated.

## External Action Authorization

- Web reads of primary mathematical sources are evidence only.
- Routine non-force GitHub commit and push are authorized by Joe's direct
  request and repository policy.
- No other external write action is authorized.

## Stop Conditions

- Another writer or overlapping live run appears.
- Lane ownership, control, permission, workflow, or emergency state changes.
- A source-dependent twistor or OS claim cannot be checked against primary or
  standard authority.
- A planted positive or negative control fails.
- The only continuation would silently equate the standard Hilbert, metric,
  real-form, gauge, or soldering object with the GU-native fork.
- The conclusion would require a claim, canon, verdict, scientific-grade,
  public-posture, Lane-control, publication, or non-GitHub external action.

## Execution Notes

The three declared legs ran independently and converged without a
construction-fork collision.

### Source/geometry leg

- Froze the off-diagonal signature-`(2,2)` Hermitian form required by the
  `graph(iX)` convention.
- Corrected the invariant causal test from `det(X)` to `det(X-Y)`.
- Distinguished the Lorentzian Grassmannian involution
  `W -> W^{perp_h}`, Euclidean quaternionic `J`, and OS field reflection
  `Theta`.
- Added the `O(1)+O(1)` normal-bundle/Kodaira-Spencer deformation principle:
  spacetime tangent and conformal null structure are reconstructed from
  twistor-line deformations.
- Separated the Riemannian AHS construction from GU's admitted Lorentzian
  observer metric: a Euclidean real-form constructor or a separately typed
  Lorentzian twistor route is mandatory.
- Recorded that `PN` is a real CR hypersurface, the Hermitian graph is only
  the big cell, and the Euclidean `CP1 -> CP3 -> HP1` fibration is smooth
  rather than holomorphic.

### GU-interface leg

- Located the actual observer section, real four-plane, normal
  `Sym^2(T*X)` bundle, base/vertical/full metric fork, `192/384` physical
  carrier correction, quaternionic conjugation, deck/operator gap,
  super-IG sketch, partial action, conditional solder, and B5 symbol slots.
- Classified direct equalities that are type-incompatible separately from
  adapter maps that remain open and source data that remain underdefined.
- Replaced the untyped “functor” target with the executable
  `GU-TWISTOR-OBSERVER-DOMAIN-FREEZE` and resultant
  `GU-OBSERVER-TWISTOR-ADAPTER`.
- Found no global contradiction. The exact missing geometric map is the
  observer-to-twistor-line/conformal-solder adapter; the exact missing
  physical data are the Schwinger/quotient and deck/operator-line packets.

### Computational leg

- Added an exact Gaussian-rational real-slice kernel with eight controls:
  Pauli determinant, Hermitian-form signature, maximal-isotropic graphs,
  null incidence, `O(1)+O(1)` deformation/null arithmetic, quaternionic
  antilinearity and square, projective no-fixed-point behavior, and
  invariant/non-invariant Euclidean planes.
- Added a NumPy OS kernel with six controls: deterministic positivity,
  quotient-rank dependence under fixed time geometry, sixteen seeded random
  positive spectra, a signed negative control, scale-covariant
  classification, and fixed-reflection comparison.
- Hostile review caught and repaired an absolute tolerance floor that could
  have hidden a negative eigenvalue under small rescaling; matrix rank and
  positive/negative inertia are now typed separately.
- Kept the mandatory GU construction-fork guard in both scripts.

### Integrated result

The standard reconstruction diamond closes, but the fused arrow

```text
twistor geometry -> OS-positive chiral Minkowski GU theory
```

does not. The terminal label is
`TWISTOR-REALITY-KERNEL-BUILT-GU-MAP-OPEN`.

The strongest bounded next target is
`GU-TWISTOR-OBSERVER-DOMAIN-FREEZE`: choose the flat/developable or curved
ASD/almost-complex route, real form, spin/marking data, and naturality domain.
Only then is the resultant `GU-OBSERVER-TWISTOR-ADAPTER` typed. This is a
run-local dependency proposal, not queue movement. It must reconstruct the
complexified observer conformal class plus its real involution before any
carrier, action, deck, or B5 physicalization claim is attempted.

## Validation

- `python3 tests/woit-principles/test_twistor_real_slice_reconstruction.py`:
  pass, `8/8` exact controls.
- `python3 tests/woit-principles/test_os_reconstruction_kernel.py`:
  pass, `6/6` controls under NumPy `2.5.1`; positive quotient ranks `1` and
  `3`, and planted signed witness
  `lambda_min=-4.537e+00` against tolerance `1.032e-12`.
- The three prior Woit-principles kernels pass unchanged:
  Palatini `5/5`, OS/right-handed `8/8`, and Grassmannian `10/10`.
- `python3 tests/wave10/H27_soldering_palatini.py`: pass, `6/6`, unchanged
  verdict `NOT FORCED`.
- `python3 -m py_compile tests/woit-principles/*.py`: pass.
- `LANES.yaml` and `LANE-STATE.yaml`: parse successfully under Ruby/Psych.
- `lab/process/research-portfolio.json`: parses successfully.
- New local index link resolves; explicit new-file path-hygiene scan passes.
- Process gates pass:
  `explorations_readme_surface_map_audit.py`,
  `tests_manifest_count_audit.py`,
  `changed_public_path_hygiene_audit.py`,
  `protected_surface_diff_audit.py`,
  `public_path_hygiene_audit.py`,
  `tests_root_readme_inventory_audit.py`,
  `explorations_top_level_file_boundary_audit.py`,
  `readme_entrypoint_map_audit.py`,
  `reproduction_docs_consistency_audit.py`,
  `research_portfolio_contract_audit.py`, and
  `process_gate_readme_inventory_audit.py`.
- `git diff --check`: pass.

## Next-Work Handoff

Run-local dependency proposal within the Woit/twistor branch:

1. `GU-TWISTOR-OBSERVER-DOMAIN-FREEZE`: select the flat/developable or curved
   ASD/almost-complex route, Lorentzian/Euclidean real form, spin/marking
   data, and admissible observer equivalences. The Riemannian AHS construction
   may be used only after a Euclidean metric/real-form constructor; otherwise
   type a separate Lorentzian twistor route.
2. `GU-OBSERVER-TWISTOR-ADAPTER`: after that freeze, construct `Phi_obs`,
   `tau_x`, the determinant-line scale, and the conformal-match theorem on an
   explicitly conformally-flat/developable marked observer; or construct
   `(Z,{L_x},rho,kappa)` with an antiholomorphic `rho`, a real line family, and
   a marking of the reconstructed real slice onto GU's fixed base `X`.
3. `GU-OS-THETA-ACTION`: wake only when a GU-owned Euclidean
   action/Schwinger packet supplies the reflection lift and field algebra.
4. `GU-TWISTOR-B5-FIELD-TRANSFORM`: after the geometric adapter closes, every
   required `m_ij` is enumerated, and a tangent/cotangent adapter exists, land
   `sigma(D_{1/2})` from the named degree-`1`, weight-`-3` transform
   `P_{-3}:H^1(PT_U,O(-3))->ker D_{1/2}` in a B5 `Hom_H` cell and test
   `J/K/domain/cohomology` compatibility. A GU “twistor symbol” is not
   automatically this Penrose-derived differential.
5. Do not rerun H27. Wake the soldered-variation extraction only if a new
   curvature-linear source action appears or a Kodaira-Spencer-to-`pi`
   adapter is constructed.

Exact wake conditions:

- for the observer-first route, either an oriented spin Euclidean
  metric/real-form constructor plus a decision on the AHS
  ASD/integrability/almost-complex branch, or a separately typed Lorentzian
  spin/CR route;
- for the substrate-first route, a candidate complex threefold with a real
  family of `CP1` curves of normal type `O(1)+O(1)`;
- for OS physicalization, a source-owned Schwinger hierarchy/functional,
  reflection lift, support algebra, and declared Hilbert-versus-Krein target.

The durable portfolio is not reranked:
`B5-INDEPENDENT-RECONSTRUCTION` remains the eligible Lane 1 lead, and the
existing OS-Theta packet remains the recorded Woit-derived follow-up. The
domain freeze is proposed first only within this run because it is executable
while OS is source-blocked; no queue state was changed.

## Receipt

- Phase result: `progressed`.
- Service outcome: `progressed`.
- Completed: `2026-07-24T22:13:19-05:00`.
- Terminal scientific label:
  `TWISTOR-REALITY-KERNEL-BUILT-GU-MAP-OPEN`.
- Required workflow graph: completed and attested.
- Conditional flows invoked:
  `rerank-next-work` and `classify-artifact-disposition`.
- `refresh-lane-state` was not invoked because no lane owner, lead,
  eligibility, or semantic state changed.
- Artifact disposition:
  two executable finite research kernels, one integrated exploration packet,
  bounded index/navigation updates, and this completed run receipt.
- Scientific effects:
  no claim promotion, canon movement, verdict change, scientific-grade
  change, or public-posture change.
- External effects:
  primary-source and transcript reads plus authorized routine GitHub
  versioning still to close the run; no other external action.
- Method refs/effect: `[]` / `null`.
