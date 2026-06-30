---
title: "Mission A Matter/Gauge Selector Construction Attempt"
date: "2026-06-24"
status: "exploration/construction_attempt"
doc_type: "mission_a_matter_gauge_selector_construction_attempt"
verdict: "CANDIDATE_SELECTOR_SCHEMA_SPECIFIED_NOT_INSTANTIATED; STRONGEST_ROUTE_IS_SOURCE_SELECTED_RANK_ONE_PATI_SALAM_BREAKING_STABILIZER"
owned_path: "explorations/geometry-curvature-emergence/mission-a-matter-gauge-selector-construction-2026-06-24.md"
optional_audit:
  - "tests/mission_a_matter_gauge_selector_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "explorations/geometry-curvature-emergence/matter-gauge-source-geometry-selector-gate-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/finite-control-provenance-audit-2026-06-24.md"
  - "explorations/type-ii1-spectral/sm-gauge-higgs-finite-control-extraction-ledger-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/primary-gu-interface-contract-2026-06-24.md"
  - "explorations/firewall-and-two-geometries/source-geometry-not-quantized-gravity-contract-2026-06-24.md"
  - "explorations/geometry-curvature-emergence/stress-energy-shadow-emergence-certificate-2026-06-24.md"
  - "canon/type-ii1-spectral-sm-checklist.md"
---

# Mission A Matter/Gauge Selector Construction Attempt

## 1. Verdict

**Verdict: a target-free selector schema can be specified, and there is one
stronger-than-hosting candidate route. It is not instantiated by the current
repo.**

The new Mission A posture changes the question from:

```text
Where is the missing Standard Model selector?
```

to:

```text
If GU is substantially correct, what source-geometric object could select the
observer matter/gauge/Higgs shadow without importing the target?
```

The strongest candidate I can build from the current source data is:

```text
Phi_SG_MG = critical source data
            -> source-selected scalar/vacuum tensor
            -> source stabilizer and low-mode shadow
            -> observer gauge, matter, Higgs, anomaly, generation certificate.
```

The nontrivial constructive idea is a **rank-one Pati-Salam-breaking stabilizer
route**:

```text
G_PS = SU(4) x SU(2)_L x SU(2)_R

source scalar candidate:
  V_PSB = (10bar, 1, 3) inside the ambient adjoint branch

if source dynamics selects a nonzero decomposable rank-one vector
  v_PSB in V_PSB

then compute
  G_obs := image of Stab_{G_PS}(v_PSB) on the complete observer shadow.
```

The expected identity-component stabilizer has Lie algebra:

```text
su(3) + su(2)_L + u(1)
```

and the hypercharge generator is the stabilizer character, not an input label.
The global quotient, including whether the kernel is `Z_6`, must then be
computed from the action on the full observer shadow.

This route is important because it is not the old finite-Connes import route:
it does not start with `A_F`, `G_SM`, `Z_6`, `K_SM`, a physical Higgs, or
`n = 3`. It starts with a source representation slot already present in the
GU carrier branch and asks whether the source action actually selects a
specific tensor in that slot.

Current decision:

```text
Constructed:
  a target-free selector functor schema;
  a concrete rank-one stabilizer candidate;
  replacement tests that would kill target smuggling.

Not constructed:
  the source-critical theorem selecting v_PSB;
  the source Hessian/gap selecting the low observer shadow;
  the global kernel computation on all surviving modes;
  physical Higgs projection and potential;
  generation-count rigidity.
```

Therefore:

```text
SM matter/gauge/Higgs is not derived.
Pati-Salam branch evidence is real.
The strongest next target is a source-selected v_PSB stabilizer theorem.
```

## 2. If GU Is Correct, What Matter/Gauge Selector Object Must Exist

If GU is correct as a source-geometry program, the required object is not a
finite target table. It is a natural selector:

```text
Phi_SG_MG:
  SG_Source_Crit  ->  Obs_Matter_Gauge_Higgs
```

It must take one fixed source branch and output the observer-facing finite
control data.

Input type:

```text
I_GU^b =
  (fields, variations, source gauge group, D_GU, S_GU,
   section map, source law, boundary/domain data, observer access)
```

with a branch key `b`, a source-critical configuration `c`, and an observer
section `s: X -> Y`.

Output type:

```text
Phi_SG_MG(I_GU^b, c, s) =
  (
    G_obs,
    global_kernel,
    K_matter,
    A_source_fin_or_bypass,
    Y_generator,
    H_scalar_candidates,
    H_phys_certificate,
    V_eff_if_any,
    anomaly_shadow,
    n_gen_certificate,
    provenance_ledger,
    replacement_audit,
    rollback
  ).
```

The selector must satisfy seven conditions.

| condition | required content | why it matters |
|---|---|---|
| source naturality | isomorphic source branches produce isomorphic observer packets | prevents label-dependent selection |
| input independence | forbidden target data do not occur in the domain | prevents hidden imports |
| branch commitment | the source branch, variations, action, and boundary data are fixed before output is inspected | prevents after-the-fact tuning |
| stabilizer or quotient theorem | observer gauge data are computed as a source stabilizer, quotient, or image with explicit kernel | prevents local Lie algebra compatibility from being promoted to global gauge derivation |
| complete shadow | every observer-facing mode is listed before anomaly or Higgs claims are made | prevents deleting extra modes |
| replacement rigidity | neighboring finite controls and `n != 3` replacements fail for a source reason | prevents cardinality transport |
| rollback | failed subcertificates demote to host/import/open rather than being rescued by prose | preserves truth tracking |

In categorical language, `SG_Source_Crit` has:

```text
objects:
  branch-fixed source geometries with critical configurations and observer
  access data.

morphisms:
  source isomorphisms preserving D_GU, S_GU, variation space, boundary/domain
  data, source gauge action, and observer section structure.
```

`Obs_Matter_Gauge_Higgs` has:

```text
objects:
  observer gauge groups with global kernels, complete matter shadows, scalar
  sectors, anomaly certificates, generation certificates, and provenance.

morphisms:
  isomorphisms preserving representations, charges, anomaly data, scalar
  potential data, and provenance tags.
```

The functor may output:

```text
derived
derived_relative
hosted
imported
failed
open
control_only
```

It may not coerce an open or hosted row into a derived row.

## 3. Candidate Selector Domain/Codomain/Functor And Legal Source Data

### 3.1 Legal source data

The candidate may legally consume only source-side objects:

| source datum | legal use |
|---|---|
| `X`, `Y = Met_Lor(X)`, `g_Y`, `s: X -> Y` | observer section and 4D pullback structure |
| `P -> Y`, source gauge group `Sp(64)` | source automorphism/stabilizer computation |
| `S = H^64`, `Cl(9,5) ~= M_64(H)` | source carrier and spinor representation data |
| `Spin(6,4)` and maximal compact branch | representation branching frame, not final observer gauge by itself |
| `D_GU`, its physical low-mode complex, and source Hessian | observer mode extraction, if branch-closed |
| `S_GU`, variation space, source law | criticality and scalar/vacuum selection |
| `theta`, `II_s^H`, connection, curvature, boundary/domain data | source fields whose stabilizers or Hessian modes may select observer data |
| source real/quaternionic/grading/chirality structures | chirality, charge conjugation, and anomaly bookkeeping |
| source-derived spectral gap or discrete projection | low observer shadow, if canonical from source data |

Forbidden upstream inputs:

```text
A_F
G_SM
Z_6
K_SM
physical Higgs doublet
nonzero Higgs projection
negative Higgs mass squared
n = 3
ind_H(D_RS) = 8
ind_H(D_GU) = 24
ordinary anomaly-free SM shadow
target hypercharge table
target Pati-Salam breaking vacuum
```

### 3.2 General selector schema

Define the critical source packet:

```text
C_b = Crit(I_GU^b)
```

For `c in C_b`, define the source-invariant vacuum/scalar packet:

```text
V_src(c) =
  (D_GU^c, Hess_c(S_GU), theta_c, II_s^H(c),
   source boundary/domain data, observer section s).
```

Then define the source automorphism group:

```text
Aut_src(c) =
  automorphisms of I_GU^b preserving V_src(c), boundary/domain data,
  source real/grading structures, and observer access.
```

Define the observer low-mode shadow by a source-canonical projection:

```text
K_obs(c) =
  P_low(c) applied to the physical source field complex.
```

`P_low(c)` is legal only if it is determined by the source operator/Hessian and
boundary data. If the cut is chosen to isolate the Standard Model, the selector
fails.

Define the observer gauge group:

```text
G_obs(c) =
  image(Aut_src(c) -> U(K_obs(c) plus scalar_low(c))).

global_kernel(c) =
  kernel(Aut_src(c) action on all observer-facing modes and scalar couplings).
```

Define the optional source finite algebra:

```text
A_source_fin(c) =
  finite-dimensional algebra of source-generated zero-order endomorphisms of
  K_obs(c) that are local over X, preserve source real/grading structures, and
  satisfy the branch order-one/locality constraints.
```

This algebra is an output, not an input. If it is not finite, not canonical, or
not `C + H + M_3(C)`, the selector reports that result. A direct stabilizer
route may bypass finite Connes data, but then it must still supply the observer
gauge, matter, Higgs, and anomaly shadow without using `A_F`.

Define the scalar/Higgs sector:

```text
Scalar_obs(c) =
  observer-scalar source variations modulo gauge, with representation under
  G_obs(c) and Hessian/potential from S_GU.

H_phys(c) =
  nonzero source-selected light or unstable scalar mode with computed
  gauge representation, couplings, and effective potential.
```

If there is only an ambient representation slot, output `hosted`, not
`H_phys`.

Define the generation certificate:

```text
n_gen_certificate(c) =
  source multiplicity or index theorem for repeated observer matter packets,
  with replacement failures for n = 2, n = 4, and n arbitrary.
```

If this is absent, output `open`.

### 3.3 Strongest concrete candidate: rank-one PSB stabilizer

Current repo evidence supplies a real Pati-Salam branch:

```text
Spin(6,4) maximal compact
  -> Spin(6) x Spin(4)
  ~= SU(4) x SU(2)_L x SU(2)_R.

S(6,4) = C^16
  -> (4,2,1) + (4bar,1,2).
```

It also supplies an ambient adjoint branch containing scalar slots:

```text
adj(sp(16))|_{G_PS}
  contains (1,2,2) and (10bar,1,3)
  among other Pati-Salam representations.
```

The candidate route is:

```text
V_PSB := (10bar,1,3)
       ~= Sym^2(C^4 bar) tensor Sym^2(C^2_R)

Find v_PSB in V_PSB from source dynamics, not by choice.
Require v_PSB to be nonzero, decomposable, and rank-one:
  v_PSB = ell^2 tensor r^2
where ell is a source-selected line in C^4 bar and r is a source-selected line
in C^2_R.
```

Then compute:

```text
G_rank1(c) = Stab_{SU(4) x SU(2)_L x SU(2)_R}(v_PSB).
```

Candidate stabilizer lemma:

```text
For a rank-one decomposable v_PSB in (10bar,1,3), the identity component of
Stab(v_PSB) has Lie algebra su(3) + su(2)_L + u(1).
The u(1) is the character combination that fixes v_PSB.
Under the induced action on
  W = (4,2,1) + (4bar,1,2),
the representation branches to the usual one-generation charge packet with
right-handed neutrino, up to convention and conjugation.
```

This is a genuine construction target because:

1. The object being stabilized is a source representation slot, not `G_SM`.
2. The `u(1)` generator is determined as the stabilizer character, not inserted
   as `Y = T_3^R + (B-L)/2`.
3. The global kernel must be computed from the action on `W` and all surviving
   scalar modes, not named as `Z_6`.
4. If the source action selects a different orbit, the output changes or fails.

The route still has a sharp gap:

```text
The repo has not proved that S_GU, theta, II_s^H, boundary data, or Hessian
select a nonzero rank-one v_PSB in (10bar,1,3).
```

Therefore the rank-one route is a **candidate selector**, not a derivation.

### 3.4 Higgs subselector

After a source-selected `v_PSB` reduces the Pati-Salam branch, the electroweak
scalar candidate is:

```text
V_H := (1,2,2) subset adj(sp(16)).
```

Under the stabilizer, this branches to a pair of observer doublet slots. A
physical Higgs certificate requires:

```text
Higgs_SG(c):
  source scalar projection to V_H is nonzero;
  the mode is gauge-covariant and observer-scalar;
  the Hessian or effective action selects the light/unstable component;
  V_eff is computed from S_GU;
  the sign, quartic, and couplings are outputs.
```

If any item fails, the correct output is:

```text
Higgs quantum numbers hosted; physical Higgs open or failed.
```

### 3.5 Matter and generation subselector

The matter packet is not a target module. It is:

```text
K_matter(c) =
  complete chiral low-mode shadow of D_GU^c under G_obs(c),
  with every extra mode listed.
```

The representation branch supplies one Pati-Salam generation packet as a local
representation fact. It does not supply the number of copies.

Generation count must be:

```text
n_gen(c) =
  a source index, multiplicity, or rigidity theorem for K_matter(c),
  independent of n = 3 and with failed n = 2,4 replacements.
```

Until that theorem exists:

```text
one-generation packet: derived as branch representation;
exact number of generations: open.
```

## 4. Anti-Smuggling Replacement Tests, Including n != 3 And Alternate Finite Controls

The selector is void if it wins by hiding target data in the input. These tests
are part of `Phi_SG_MG`, not post-hoc commentary.

| test | pass condition | failure caught |
|---|---|---|
| NoTargetInput | the input DAG contains no `A_F`, `G_SM`, `Z_6`, `K_SM`, physical Higgs, `n=3`, target index, or ordinary SM shadow | direct import |
| LabelErasure | replacing SM names by anonymous source representation names leaves the construction unchanged | semantic target matching |
| BranchCommitment | `I_GU^b`, variation space, boundary data, and source criticality are fixed before the output is inspected | branch tuning after the target is known |
| StabilizerComputation | `G_obs` is computed as a stabilizer/image/kernel; no target gauge group appears in the theorem statement | local compatibility promoted to derivation |
| GlobalKernel | the central kernel is computed from the action on all observer modes; `Z_6` is not named upstream | global quotient import |
| LowModeGap | `P_low` comes from a source spectral gap or discrete projection; threshold variation is audited | spectral cut chosen to isolate SM |
| CompleteShadow | all low modes are listed before anomaly checks | extra anomalous modes deleted |
| AnomalyNonSelector | anomaly cancellation verifies a completed shadow but does not choose it | ordinary SM anomaly table used as selector |
| HiggsNullTest | zero or noncovariant source projection demotes Higgs to hosted/open | physical Higgs inserted after representation slot |
| PotentialTest | EWSB sign and quartic come from `S_GU`, not from a Mexican-hat ansatz | phenomenological Higgs potential import |
| GenerationReplacement | run `n=2`, `n=4`, and `n` arbitrary controls; a claimed `n=3` selector must give a source obstruction to the replacements | cardinality transport |
| AlternateFiniteControls | compare alternate finite-control packets without treating the desired packet as target | finite CC table import |
| K3Bridge | compact K3 arithmetic is ignored unless the same physical GU operator and H-linear bridge are supplied | compact control promoted to physical index |

### n != 3 replacement audit

Any generation claim must run:

```text
Replace K_matter by K_packet tensor C^2.
Replace K_matter by K_packet tensor C^4.
Replace any C_3, triple-arm, trace-three, or index-three input by C_n or n arms.
Replace target-normalized index values by symbolic index k.
```

The selector passes only if:

```text
the source data force exactly three sectors,
and the neighboring replacements fail for a named source reason.
```

Examples of failures:

| attempted selector | decision |
|---|---|
| equal trace partitions in a diffuse II_1 factor | fails because arbitrary `n` works |
| `C_n` Fourier idempotents | fails because `n` is chosen |
| C3/D4 visible triple | fails unless source data force the object and block neighbors |
| `K_SM tensor C^3` | imports both `K_SM` and the count |
| raw compact K3 index | control only until physical `RS_GU^phys` and bridge exist |

### Alternate finite-control replacement audit

If the route uses an algebraic finite-control object, it must be tested against
alternates:

```text
C + H + M_k(C), k != 3
H_L + H_R + M_4(C)
left-right and Pati-Salam finite controls
flipped or conjugate embeddings
same local Lie algebra with different global center quotient
finite modules with extra vectorlike modes
finite modules missing nu_R
```

The test is not "which alternate resembles the SM." The test is:

```text
Does source geometry compute one packet and obstruct the replacements?
```

If the construction merely embeds or hosts all alternates, it is not a
selector.

## 5. What Current Pati-Salam/Higgs/Type-II1 Evidence Supplies And What It Does Not

| evidence | supplies | does not supply |
|---|---|---|
| GU carrier `Cl(9,5) ~= M_64(H)`, `S = H^64`, `Sp(64)` | source carrier and large gauge automorphism structure | observer finite-control selector |
| maximal compact `Spin(6,4)` branch | Pati-Salam branch frame | physical low-energy gauge group |
| `S(6,4) -> (4,2,1) + (4bar,1,2)` | one Pati-Salam generation representation packet | generation count or complete observer matter shadow |
| standard Pati-Salam charge arithmetic | relative SM charges after a breaking is supplied | source-selected breaking, absolute hypercharge, or global quotient |
| `V_PSB = (10bar,1,3)` ambient slot | a plausible source tensor whose rank-one stabilizer could select SM-like gauge data | proof that source dynamics selects a nonzero rank-one vector in this orbit |
| `(1,2,2)` ambient slot | electroweak Higgs quantum-number host after breaking | physical Higgs projection, lightness, potential, EWSB |
| Type II_1 host pathway | possible host for imported finite CC data and useful no-go filters | positive selector for `A_F`, `G_SM`, `Z_6`, `K_SM`, or `n=3` |
| ordinary anomaly formulas | verification after a complete shadow is output | selector for the shadow |
| K3/RS arithmetic | compact control and target for a future bridge | physical noncompact GU generation index |

The Pati-Salam evidence is stronger than a random compatibility result. It gives
the correct high-level representation arena for a source stabilizer selector.
But it still stops at:

```text
source branch representation evidence
```

not:

```text
observer SM matter derived.
```

The rank-one `V_PSB` candidate is the first route in this lane that looks like
a possible source-geometric mechanism rather than a finite-control import. Its
current status is:

```text
conditional candidate:
  if source dynamics selects v_PSB,
  then compute the stabilizer and kernel.

not current evidence:
  v_PSB is selected by GU.
```

## 6. First Exact Obstruction Or Missing Proof Object

The first exact missing proof object is:

```text
CriticalRankOnePSBSelectionAndStabilizerTheorem
```

Required input:

```text
I_GU^b with written D_GU, S_GU, variation space, source law,
boundary/domain data, observer section s, and source scalar sector.
```

Required output:

```text
1. Source-critical scalar selection:
   S_GU and boundary/domain data select a nonzero rank-one decomposable
   v_PSB in (10bar,1,3), or prove that no such source-selected vector exists.

2. Stabilizer theorem:
   Stab_{G_PS}(v_PSB) has identity-component Lie algebra
   su(3) + su(2)_L + u(1), with the u(1) generator obtained from the
   stabilizer character.

3. Global kernel theorem:
   the action on the complete low observer shadow has a computed kernel.
   If the kernel is `Z_6`, it is output here, not input.

4. Matter branching theorem:
   the complete low-mode shadow branches under the stabilizer, with all extra
   modes listed.

5. Higgs theorem:
   the source scalar sector contains a nonzero gauge-covariant light/unstable
   electroweak scalar mode and a computed effective potential, or reports
   hosted/open.

6. Generation theorem:
   multiplicity is computed from source index/rigidity data and survives the
   `n=2,4,n` replacement audit, or remains open.

7. Anomaly theorem:
   all observer-facing modes pass perturbative/global anomaly checks, or the
   branch fails.
```

Why this obstruction is first:

```text
Without source selection of v_PSB, the stabilizer route is just a clever
choice of Pati-Salam breaking data.

Without the stabilizer/kernel computation, the route remains local branch
arithmetic and cannot derive the global observer gauge group.

Without the complete low-mode shadow, anomaly and generation statements are
not meaningful.
```

The selector branch fails cleanly if:

```text
the selected scalar orbit is generic and has the wrong stabilizer;
v_PSB is zero;
v_PSB is inserted by hand because it gives SM;
the global kernel is not the SM quotient;
extra low modes survive with uncanceled anomaly;
the Higgs projection vanishes or has no EWSB potential;
generation replacement tests work for n != 3.
```

## 7. Constructive Next Computation

The next computation should be narrow and exact:

```text
Compute the rank-one stabilizer and kernel without using SM labels.
```

Concrete packet:

1. Work inside:

   ```text
   G_PS = SU(4) x SU(2)_L x SU(2)_R
   W = (4,2,1) + (4bar,1,2)
   V_PSB = (10bar,1,3)
   V_H = (1,2,2)
   ```

2. Choose anonymous vector spaces:

   ```text
   A = C^4
   B = C^2_L
   C = C^2_R
   V_PSB = Sym^2(A^*) tensor Sym^2(C)
   W = (A tensor B) plus (A^* tensor C)
   ```

   Do not name color, weak isospin, hypercharge, or SM.

3. Compute the identity-component stabilizer of:

   ```text
   v = a_4^* a_4^* tensor c_+ c_+
   ```

   in `SU(A) x SU(B) x SU(C)`.

4. Compute the induced weights of the stabilizer on `W` and `V_H`.

5. Compute the kernel of the stabilizer action on `W plus V_H` and record the
   global quotient.

6. Only after the computation, compare the anonymous output to the standard
   SM quotient and charge packet.

7. Add the source-selection question as a separate theorem:

   ```text
   Does any branch-fixed source action/Hessian select the rank-one orbit in
   V_PSB?
   ```

Possible decisions:

| result | consequence |
|---|---|
| stabilizer is wrong | rank-one route fails as SM gauge selector |
| stabilizer is locally right but kernel wrong | local branch route remains insufficient |
| stabilizer and kernel are right but source does not select `v` | host/ansatz, not derivation |
| source selects `v`, but low-mode shadow has extra anomalous modes | branch fails anomaly shadow |
| source selects `v`, kernel is right, shadow complete, Higgs/generation still open | upgrade SM gauge branch only, not full matter/Higgs |

This computation is valuable either way. It turns a vague "Pati-Salam could
break to the SM" statement into a source-stabilizer theorem with exact failure
conditions.

## 8. Claim Certificate Table And Machine-Readable Summary

| claim | current status | proof grade | constructive content | missing proof object | forbidden inputs | rollback |
|---|---|---|---|---|---|---|
| `PHI_SG_MG` | specified_not_instantiated | construction_schema | target-free functor domain, codomain, legal inputs, replacement tests | `CriticalRankOnePSBSelectionAndStabilizerTheorem` plus low-mode shadow | `A_F`, `G_SM`, `Z_6`, `K_SM`, physical Higgs, `n=3` | any forbidden input demotes to import/host |
| `SM_GAUGE` | conditional_candidate | reconstruction_target | rank-one `V_PSB` stabilizer could compute `su3+su2+u1` and kernel | source-selected `v_PSB` and global kernel computation | preselected SM subgroup, hypercharge, `Z_6` | wrong stabilizer/kernel or target-chosen `v_PSB` fails |
| `MATTER_SHADOW` | partial_open | branch_reconstruction | `W=(4,2,1)+(4bar,1,2)` gives one Pati-Salam packet and relative charge output after stabilizer | complete low-mode shadow and anomaly theorem | `K_SM`, ordinary SM shadow, deleted extra modes | extra anomalous modes or target matter input demotes |
| `HIGGS` | hosted_open | representation_host_plus_candidate | `(1,2,2)` is a legal scalar host after rank-one breaking | nonzero source projection, Hessian lightness, `V_eff` | physical Higgs, nonzero projection, negative mass squared | zero projection or no EWSB demotes to hosted/open |
| `GEN_COUNT` | open | no_physical_count | one-generation packet is a branch representation, not copy count | source index/rigidity theorem with `n=2,4,n` replacement failures | `n=3`, C3, triple arms, target index values | replacement works for other `n` or index absent |
| `A_F_OR_BYPASS` | bypass_open | selector_choice | direct stabilizer route can bypass finite Connes algebra | if used, `A_source_fin` must be output by source data | `A_F=C+H+M_3(C)` as input | finite algebra import demotes to host/import |
| `TYPEII1_SELECTOR` | negative_filter_open_empty | audit_control | useful replacement tests and host/selector separation | fixed-data selector forcing output and blocking alternates | trace split, `C_n`, `K_SM tensor C^3` | arbitrary `n` or imported module fails |

## Machine-Readable Summary

```json
{
  "artifact": "SOURCE_GEOMETRY_MATTER_GAUGE_SELECTOR_CONSTRUCTION_ATTEMPT",
  "version": "2026-06-24",
  "verdict": "CANDIDATE_SELECTOR_SCHEMA_SPECIFIED_NOT_INSTANTIATED",
  "overclaim_guard": "do_not_claim_SM_matter_is_derived",
  "selector": {
    "name": "Phi_SG_MG",
    "type": "SG_Source_Crit_to_Obs_Matter_Gauge_Higgs",
    "status": "specified_not_instantiated",
    "domain": [
      "I_GU_branch",
      "source_critical_configuration",
      "observer_section",
      "D_GU",
      "S_GU",
      "variation_space",
      "source_law",
      "boundary_domain_data",
      "source_gauge_action"
    ],
    "codomain": [
      "G_obs",
      "global_kernel",
      "K_matter",
      "A_source_fin_or_bypass",
      "Y_generator",
      "H_scalar_candidates",
      "H_phys_certificate",
      "V_eff_if_any",
      "anomaly_shadow",
      "n_gen_certificate",
      "provenance_ledger",
      "replacement_audit",
      "rollback"
    ],
    "legal_source_data": [
      "Cl_9_5_carrier",
      "H_64_spinor_bundle",
      "Sp_64_source_gauge_group",
      "Spin_6_4_branch_data",
      "theta",
      "II_s_H",
      "connection_curvature",
      "source_Hessian",
      "source_real_grading_structures",
      "canonical_source_low_mode_projection"
    ],
    "forbidden_target_inputs": [
      "A_F",
      "G_SM",
      "Z_6",
      "K_SM",
      "physical_Higgs",
      "nonzero_Higgs_projection",
      "negative_Higgs_mass_squared",
      "n_equals_3",
      "ind_H_D_RS_equals_8",
      "ind_H_D_GU_equals_24",
      "ordinary_anomaly_free_SM_shadow",
      "target_hypercharge_table",
      "target_Pati_Salam_breaking_vacuum"
    ]
  },
  "candidate_routes": [
    {
      "id": "critical_stabilizer_shadow",
      "status": "general_schema",
      "description": "compute observer gauge and matter data as source stabilizer/image/kernel acting on a complete low-mode shadow"
    },
    {
      "id": "rank_one_psb_stabilizer",
      "status": "strongest_conditional_candidate",
      "source_slot": "V_PSB=(10bar,1,3)",
      "requires": "source_selected_nonzero_decomposable_rank_one_v_PSB",
      "expected_local_output": "su3_plus_su2_L_plus_u1",
      "kernel_status": "must_be_computed_not_imported",
      "source_selection_status": "missing"
    },
    {
      "id": "finite_algebra_shadow",
      "status": "optional_open_or_bypass",
      "rule": "A_source_fin_must_be_output_not_input"
    }
  ],
  "anti_smuggling_tests": [
    "NoTargetInput",
    "LabelErasure",
    "BranchCommitment",
    "StabilizerComputation",
    "GlobalKernel",
    "LowModeGap",
    "CompleteShadow",
    "AnomalyNonSelector",
    "HiggsNullTest",
    "PotentialTest",
    "GenerationReplacement",
    "AlternateFiniteControls",
    "K3Bridge"
  ],
  "replacement_tests": {
    "generation": [
      "n_equals_2",
      "n_equals_4",
      "n_arbitrary",
      "C_n_replacement",
      "symbolic_index_k"
    ],
    "finite_controls": [
      "C_plus_H_plus_M_k_for_k_not_3",
      "H_L_plus_H_R_plus_M_4_C",
      "left_right_finite_control",
      "Pati_Salam_finite_control",
      "alternate_global_center_quotients",
      "extra_vectorlike_modes",
      "missing_nu_R"
    ]
  },
  "current_evidence": {
    "pati_salam_branch": {
      "status": "derived_branch_representation",
      "supplies": "Spin_6_4_maximal_compact_and_one_generation_packet",
      "does_not_supply": "source_selected_low_energy_gauge_group_or_generation_count"
    },
    "higgs_slots": {
      "status": "hosted_open",
      "supplies": "ambient_(1,2,2)_and_rank_one_PSB_candidate_slots",
      "does_not_supply": "physical_Higgs_projection_or_potential"
    },
    "type_ii1": {
      "status": "negative_filter_open_empty",
      "supplies": "host_selector_separation_and_replacement_tests",
      "does_not_supply": "positive_A_F_G_SM_Z_6_K_SM_or_n_3_selector"
    }
  },
  "claim_certificates": [
    {
      "claim": "PHI_SG_MG",
      "status": "specified_not_instantiated",
      "proof_grade": "construction_schema",
      "missing_proof_object": "CriticalRankOnePSBSelectionAndStabilizerTheorem",
      "forbidden_inputs": ["A_F", "G_SM", "Z_6", "K_SM", "physical_Higgs", "n_equals_3"],
      "rollback": "forbidden_input_or_no_source_critical_low_mode_shadow"
    },
    {
      "claim": "SM_GAUGE",
      "status": "conditional_candidate",
      "proof_grade": "reconstruction_target",
      "missing_proof_object": "source_selected_v_PSB_and_global_kernel_computation",
      "forbidden_inputs": ["G_SM", "Z_6", "target_hypercharge_table", "preselected_SM_subgroup"],
      "rollback": "wrong_stabilizer_wrong_kernel_or_target_chosen_v_PSB"
    },
    {
      "claim": "MATTER_SHADOW",
      "status": "partial_open",
      "proof_grade": "branch_reconstruction",
      "missing_proof_object": "complete_low_mode_shadow_and_anomaly_theorem",
      "forbidden_inputs": ["K_SM", "ordinary_SM_shadow", "deleted_extra_modes"],
      "rollback": "extra_anomalous_modes_or_target_matter_input"
    },
    {
      "claim": "HIGGS",
      "status": "hosted_open",
      "proof_grade": "representation_host_plus_candidate",
      "missing_proof_object": "nonzero_source_projection_Hessian_lightness_and_V_eff",
      "forbidden_inputs": ["physical_Higgs", "nonzero_Higgs_projection", "negative_Higgs_mass_squared"],
      "rollback": "zero_projection_noncovariant_projection_or_no_EWSB_potential"
    },
    {
      "claim": "GEN_COUNT",
      "status": "open",
      "proof_grade": "no_physical_count",
      "missing_proof_object": "source_index_or_rigidity_theorem_with_n_replacement_failures",
      "forbidden_inputs": ["n_equals_3", "C3", "triple_arms", "target_index_values"],
      "rollback": "replacement_works_for_other_n_or_index_absent"
    },
    {
      "claim": "A_F_OR_BYPASS",
      "status": "bypass_open",
      "proof_grade": "selector_choice",
      "missing_proof_object": "A_source_fin_output_or_explicit_bypass_certificate",
      "forbidden_inputs": ["A_F", "C_plus_H_plus_M_3_C_as_input"],
      "rollback": "finite_algebra_import_demotes_to_host_import"
    }
  ],
  "first_missing_proof_object": "CriticalRankOnePSBSelectionAndStabilizerTheorem",
  "constructive_next_computation": "compute_stabilizer_kernel_and_branching_for_rank_one_V_PSB_without_SM_labels",
  "current_allowed_citation": "A target-free Phi_SG_MG schema and rank-one stabilizer candidate are specified; the repo has not derived SM matter, the physical Higgs, or three generations."
}
```

## Sources Read

- `RESEARCH-POSTURE.md`
- `process/runbooks/five-lane-frontier-run.md`
- `explorations/geometry-curvature-emergence/matter-gauge-source-geometry-selector-gate-2026-06-24.md`
- `explorations/cycle-gates-and-audits/finite-control-provenance-audit-2026-06-24.md`
- `explorations/type-ii1-spectral/sm-gauge-higgs-finite-control-extraction-ledger-2026-06-24.md`
- `explorations/cycle-gates-and-audits/primary-gu-interface-contract-2026-06-24.md`
- `explorations/firewall-and-two-geometries/source-geometry-not-quantized-gravity-contract-2026-06-24.md`
- `explorations/geometry-curvature-emergence/stress-energy-shadow-emergence-certificate-2026-06-24.md`
- `canon/type-ii1-spectral-sm-checklist.md`
