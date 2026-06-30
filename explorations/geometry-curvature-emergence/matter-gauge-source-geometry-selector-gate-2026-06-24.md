---
title: "Matter/Gauge Source-Geometry Selector Gate"
date: "2026-06-24"
status: exploration/gate
doc_type: matter_gauge_source_geometry_selector_gate
verdict: "NO_SOURCE_GEOMETRY_SELECTOR_YET; PATI_SALAM_BRANCH_DERIVED; SM_FINITE_CONTROL_NOT_DERIVED"
owned_path: "explorations/geometry-curvature-emergence/matter-gauge-source-geometry-selector-gate-2026-06-24.md"
depends_on:
  - "explorations/cycle-gates-and-audits/primary-gu-interface-contract-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/finite-control-provenance-audit-2026-06-24.md"
  - "explorations/type-ii1-spectral/sm-gauge-higgs-finite-control-extraction-ledger-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/goal-draft-type-ii1-fixed-data-selector-challenge-2026-06-24.md"
  - "explorations/type-ii1-spectral/type-ii1-selector-or-nogo-theorem-2026-06-24.md"
  - "explorations/generation-sector/generation-count-sm-branching-closure-2026-06-22.md"
  - "explorations/generation-sector/y14-k3-bridge-loss-ledger-2026-06-24.md"
  - "canon/type-ii1-spectral-sm-checklist.md"
  - "explorations/cycle-gates-and-audits/live-claim-dag-fault-finality-ledger-2026-06-24.md"
optional_audit:
  - "tests/matter_gauge_source_selector_audit.py"
---

# Matter/Gauge Source-Geometry Selector Gate

## 1. Verdict

**Verdict: no current source-geometry selector derives the full matter/gauge
finite-control package.**

The steelman premise is accepted as a gate condition:

```text
If GU replaces the starting object rather than quantizing GR, then matter and
gauge structure must be selected from the source geometry. It cannot be appended
as QFT matter on a background and cannot be imported from finite Connes data.
```

The present repo state is sharper:

```text
source geometry derives:
  typed GU carrier, ambient Sp(64), Spin(6,4) maximal-compact branch frame,
  Pati-Salam one-generation representation packet.

source geometry derives only relative to a supplied branch:
  Pati-Salam-to-SM charges and hypercharge arithmetic.

source geometry hosts:
  SM Higgs quantum-number slots in the ambient adjoint branch.

current lanes import or fail to derive:
  finite Connes algebra A_F,
  SM gauge quotient SU(3) x SU(2) x U(1) / Z_6,
  absolute hypercharge/gauge lattice,
  physical Higgs scalar and potential,
  full anomaly-safe observer shadow,
  exact generation count.
```

Decision consequence:

```text
The honest claim is:
  GU source geometry supplies a real Pati-Salam representation branch and
  necessary Higgs slots.

The forbidden claim is:
  GU source geometry currently derives the SM gauge group, Higgs sector,
  anomaly-safe matter shadow, or three generations.
```

The first hard failure is conditional on the lane:

| lane | first missing datum | current decision |
|---|---|---|
| finite-algebra lane | `A_F = C + H + M_3(C)` | imported, not derived |
| direct GU gauge lane | `G_SM = SU(3) x SU(2) x U(1) / Z_6` | failed target-free selection |
| Higgs lane | nonzero source projection plus potential | hosted/open |
| generation lane | physical GU RS complex and H-index bridge | open/control-only |

So this gate returns:

```text
MATTER-SHADOW: partial/open.
SM-GAUGE: failed as target-free selector.
HIGGS: hosted/open.
GEN-COUNT: open.
```

## 2. Source-Geometry Matter/Gauge Selector Schema

A source-geometry matter/gauge selector certificate is a typed object, not a
story. It must start from the branch-closed GU interface:

```text
I_GU =
  (fields, variations, gauge group, D_GU, S_GU,
   section map, source law, boundary conditions, reduction functor)
```

and output the observer-facing matter/gauge packet:

```text
Phi_SG_MG(I_GU, s, domains)
  =
  (G_obs, Q_obs, A_fin?, K_matter, Y, H_phys,
   anomaly_shadow, n_gen, provenance, replacement_audit).
```

Here `A_fin?` is optional. If the construction uses finite spectral data, the
finite algebra and finite module must be outputs of the source selector, not
inputs. If the construction bypasses finite Connes data, the alternative
finite-control shadow must still provide the same observer-facing decisions.

### Required Certificate Fields

| field | required content | current state |
|---|---|---|
| `input_independence` | proof that `A_F`, `G_SM`, `Z_6`, `K_SM`, physical Higgs, `n=3`, target index values, and ordinary anomaly-free SM content are not inputs | not supplied |
| `branch_closure` | one source branch with written `D_GU`, `S_GU`, variations, source law, section map, domains, and boundary conditions | not supplied for matter/gauge selector |
| `gauge_quotient` | target-free quotient or stabilizer theorem producing `G_obs`, its Lie algebra, global center kernel, and observer gauge action | failed at `G_SM/Z_6` |
| `finite_algebra_if_used` | derivation of `A_F = C + H + M_3(C)` or explicit proof that no finite algebra is being used | imported in current lanes |
| `pati_salam_reps` | derivation of `Spin(6,4) -> Spin(6) x Spin(4) ~= SU(4) x SU(2)_L x SU(2)_R` and `S(6,4) -> (4,2,1) + (4bar,1,2)` | derived as branch representation |
| `sm_reps` | selected Pati-Salam-to-SM embedding and resulting SM representation packet | derived only relative to supplied embedding |
| `hypercharge` | absolute generator `Y = T_3^R + (B-L)/2`, normalization, charge lattice, and `Z_6` kernel | relative arithmetic only |
| `higgs` | source field map from `theta`, `II_s^H`, connection fluctuation, or another source field to a nonzero physical scalar; light-component selector; potential and EWSB sign | hosted/open |
| `anomaly_shadow` | functorial observer shadow with all surviving modes listed, then perturbative/global/Freed-Hopkins checks | ordinary relative SM shadow passes; full shadow open |
| `generation_count` | noncircular count from physical source operator or fixed selector, with replacement tests for `n=2,4` and no target index insertion | open |
| `branch_robustness` | proof that the selection survives allowed GU branch changes, or precise branch-local scope | absent |
| `rollback` | conditions that demote the claim to hosted/imported/failed | active guards only |

### Output Class Rules

| output class | meaning |
|---|---|
| `derived` | computed from allowed source geometry without using the target as input |
| `derived_relative` | computed after an upstream branch or embedding is supplied; not absolute selection |
| `hosted` | ambient source geometry contains a slot or representation, but no physical selector chooses it |
| `imported` | datum is supplied from finite Connes, SM convention, Pati-Salam breaking, phenomenology, or target index value |
| `failed` | current attempted selector needs a forbidden input or passes the replacement-family test |
| `open` | candidate has a named missing proof object |
| `control_only` | useful arithmetic or executable control that is not physical source evidence |

### Minimal Anti-Smuggling Rule

The selector is void if any of the following appear upstream of selection:

```text
A_F,
G_SM,
Z_6,
K_SM,
physical Higgs doublet,
nonzero Higgs projection,
negative Higgs mass squared,
n = 3,
ind_H(D_RS) = 8,
ind_H(D_GU) = 24,
three generations,
ordinary anomaly-free SM shadow.
```

The source geometry may output these data. It may not consume them as target
labels and then call the result a derivation.

## 3. Current Derived/Hosted/Imported/Failed Ledger

| datum | current class | provenance from read files | why this class | missing proof object |
|---|---|---|---|---|
| Typed GU carrier `Cl(9,5) ~= M_64(H)`, `S = H^64`, ambient `Sp(64)` | derived | primary interface, finite-control audit | This is source carrier data, not an SM target. | downstream selector from carrier to finite-control packet |
| Gauge group of source connection `Sp(64)` | derived | primary interface | It is the vertical principal automorphism structure group of `P -> Y`. | observer gauge quotient theorem |
| Pati-Salam branch frame `Spin(6) x Spin(4) ~= SU(4) x SU(2)_L x SU(2)_R` | derived | SM extraction ledger, generation branching closure | It follows from the maximal compact of `Spin(6,4)`. | physical gauge-selection theorem making this observer gauge data rather than a branching frame |
| One-generation Pati-Salam packet `(4,2,1) + (4bar,1,2)` | derived | generation branching closure, finite-control audit | `S(6,4)=C^16` branches to the standard Pati-Salam one-generation packet. | upstream gauge selector and observer shadow |
| One-generation SM charge packet with `nu_R` | derived_relative | generation branching closure, finite-control audit | The charge packet follows after Pati-Salam-to-SM embedding is supplied. | source-selected embedding and global quotient |
| Hypercharge `Y = T_3^R + (B-L)/2` | derived_relative | generation branching closure, finite-control audit | Standard arithmetic is correct once the Pati-Salam breaking is chosen. | absolute source selector for `U(1)_Y`, normalization, and lattice/kernel |
| Pati-Salam-to-SM breaking | imported/open | finite-control audit, SM extraction ledger | The subgroup chain is standard but not selected by current source geometry. | source field/vacuum/boundary condition with the required stabilizer |
| Finite Connes algebra `A_F = C + H + M_3(C)` | imported | finite-control provenance audit | Current Type II_1 or finite CC lanes start after this algebra is supplied. | target-free finite-control selector computing `A_F` |
| SM gauge quotient `SU(3) x SU(2) x U(1) / Z_6` | failed | finite-control provenance audit, SM extraction ledger | Local branch arithmetic does not derive the global quotient; finite CC recovery imports `A_F`. | gauge quotient/stabilizer theorem deriving the global kernel |
| Central quotient `Z_6` | failed | finite-control provenance audit | It is not fixed by the local Lie algebra branch alone. | lattice/kernel theorem from source geometry |
| Ambient Higgs bidoublet `(1,2,2)` in `adj(Sp(16))` | derived | SM extraction ledger | The Clebsch-Gordan decomposition contains a Pati-Salam bidoublet. | physical source projection and dynamics |
| SM Higgs quantum-number slot `(1,2,+1/2)` | hosted | finite-control audit, SM extraction ledger | The slot exists after relative SM branching, but containment is not selection. | nonzero light-component selector |
| Physical Higgs scalar from `theta` or `II_s^H` | open | finite-control audit, SM extraction ledger | Plausible source maps exist, but no gauge-covariant nonzero projection is proved. | `pr_(1,2,+1/2)(II_s^H)` or equivalent on a specified critical section |
| Higgs potential and electroweak symmetry breaking | open | finite-control audit, SM extraction ledger | Representation theory does not supply mass sign, quartic, or vacuum. | effective-potential computation from written source action |
| Ordinary one-generation perturbative anomaly cancellation | derived_relative | finite-control audit | If the observer shadow is exactly the ordinary SM packet, the standard sums cancel. | source proof that this is exactly the observer shadow |
| Full GU/Type II_1 anomaly shadow | open | finite-control audit, Type II_1 checklist | Extra modes and the Connes-channel image are not fully controlled. | functorial shadow listing every observer-facing mode and anomaly result |
| Type II_1 finite-control host | hosted | Type II_1 checklist, selector-or-nogo theorem | Semifinite/II_1 data may host imported finite CC data. | positive selector, not just host embedding |
| Type II_1 selector for `A_F`, `G_SM`, `T_1`, or `T_3` | failed/open_narrow | selector-or-nogo theorem, fixed-data challenge | Instantiated selectors are host-only or cardinality transport; fixed-data rigidity is open but empty. | fixed-data selector with replacement obstruction |
| `2 + 1` generation representation story | derived_relative/open | generation branching closure | Branching supports two spin-1/2 sectors plus one RS/imposter sector at reconstruction grade. | analytic zero-mode/index theorem and physical RS complex |
| Raw K3 RS arithmetic | control_only | Y14/K3 bridge-loss ledger | Compact formulas are useful controls but not transported physical GU index evidence. | physical `RS_GU^phys`, tau-discrete sector, H-linear bridge, corrections |
| Exact generation count `n_gen = 3` | open | live claim DAG, Y14/K3 bridge-loss ledger | `GEN-COUNT` is explicitly open; target values are forbidden inputs. | independent H-index and noncircular generation readout |

## 4. Relation To Type II_1 Selectors And K3/Generation Bridge

### Type II_1

The Type II_1 lane remains useful only if it is kept split:

```text
TYPEII1-HOST:
  conditional hosting lane for imported finite CC data.

TYPEII1-SELECTOR:
  negative filter for current instantiated selectors;
  positive selector absent.
```

For this matter/gauge gate, Type II_1 data may contribute only in one of two
honest ways:

1. It may host a finite-control packet after declaring every imported datum.
2. It may provide a fixed-data selector theorem that computes at least one of
   `A_F`, `G_SM`, one-generation module `T_1`, or exactly three sectors `T_3`.

The first is not a source-geometry derivation. The second is open but currently
uninstantiated. Trace partitions, `C_n` Fourier idempotents, C3/D4 arms, index-3
examples, and `K_SM tensor C^n` shadows fail because the same proof works for
neighboring counts or imports the finite CC module.

### K3 And Generation Count

The K3 lane is a control, not physical generation evidence:

```text
K3 raw RS index != physical noncompact GU index
```

The bridge-loss ledger identifies the missing payload:

```text
RS_GU^phys =
  (E_RS^+, E_RS^-,
   gauge maps,
   gauge condition or BRST ghost complex,
   sigma_RS^phys,
   H-structure certificate,
   GU source operator/action branch).
```

Without this object, the compact K3 formulas do not select generations from
source geometry. The generation branch currently has two distinct statuses:

| layer | current decision |
|---|---|
| representation branch | Pati-Salam one-generation packet and `2 + 1` story are reconstructed/relative |
| physical index/readout | open; `GEN-COUNT` remains not final |

Thus the source-geometry selector may cite the representation content, but it
may not cite K3 as physical evidence for `n_gen = 3`.

## 5. Claim Certificate Table For MATTER-SHADOW, SM-GAUGE, HIGGS, GEN-COUNT

| claim | current status | proof grade | derived by source geometry | hosted or relative content | imported/failed content | missing proof object | forbidden inputs | citation language |
|---|---|---|---|---|---|---|---|---|
| `MATTER-SHADOW` | partial_open | reconstruction/contract | `S(6,4) -> (4,2,1) + (4bar,1,2)` and relative SM charge packet after selected embedding | Pati-Salam branch frame and one-generation quantum numbers | finite CC module and exact observer shadow are not selected | `Shadow_SG` functor from source geometry to observer-facing chiral content, listing all extra modes and anomaly checks | `K_SM`, ordinary SM shadow, deleting extra modes, Pati-Salam labels treated as final observer state | "Source geometry derives a Pati-Salam one-generation branch and relative SM charge arithmetic; the full observer matter shadow is open." |
| `SM-GAUGE` | failed | negative_filter/reconstruction | source carrier gauge is `Sp(64)` and maximal compact branch gives Pati-Salam frame | local branch data support the standard Pati-Salam calculation | `A_F`, `G_SM`, `Z_6`, and Pati-Salam breaking are not target-free outputs | gauge quotient/stabilizer theorem deriving `SU(3) x SU(2) x U(1) / Z_6` and hypercharge lattice from source data | `A_F`, `G_SM`, `Z_6`, chosen SM subgroup, chosen breaking vacuum | "The SM gauge quotient is not derived; current source geometry reaches Pati-Salam branch data only." |
| `HIGGS` | hosted_open | reconstruction | ambient adjoint branch contains a Pati-Salam bidoublet `(1,2,2)` | SM doublet quantum-number slot exists after relative SM branching | physical scalar, nonzero projection, mass sign, quartic, and EWSB are not derived | gauge-covariant source projection plus effective potential from written `S_GU` | physical Higgs doublet, nonzero projection, negative mass squared, Mexican-hat potential, selected light component | "GU hosts Higgs quantum numbers; Higgs emergence is open until the source projection and potential are computed." |
| `GEN-COUNT` | open | open_none for physical count; reconstruction for representation branch | `S(6,4)` carries one Pati-Salam generation; `2 + 1` story is representation-grade/reconstruction | raw K3 arithmetic and RS branch controls | exact `n_gen=3` and physical H-index are not selected | `RS_GU^phys` plus H-linear Fredholm/bridge/index theorem and noncircular readout | `n=3`, `ind_H(D_RS)=8`, `ind_H(D_GU)=24`, `rank_eff=4/8`, compact K3 raw class as physical index | "Generation count remains open; representation branching is supportive but not a physical source-index proof." |

Rollback conditions:

| claim | rollback or demotion condition |
|---|---|
| `MATTER-SHADOW` | demote to hosted/imported if the shadow functor takes `K_SM` or ordinary SM content as input, or if extra observer-facing modes survive without anomaly control |
| `SM-GAUGE` | remain failed if the quotient theorem consumes `A_F`, `G_SM`, `Z_6`, or a selected SM-breaking field as input |
| `HIGGS` | demote emergence language if the source projection vanishes, is gauge-noncovariant, selects the wrong component, or the potential lacks EWSB |
| `GEN-COUNT` | demote any `n_gen=3` language if the physical index is absent, background-dependent, complex-only, circular, or not equal to the required count under fixed normalization |

## 6. Branch/Selector Robustness Table

| branch or selector | robust output | fragile or missing output | replacement/branch test | current decision |
|---|---|---|---|---|
| GU carrier branch `Cl(9,5), S=H^64, Sp(64)` | carrier and ambient source gauge group | observer gauge quotient and finite-control data | must not infer SM quotient from ambient size or representation convenience | derived carrier only |
| `Spin(6,4)` maximal compact branch | Pati-Salam branch frame and one-generation packet | physical low-energy gauge selection | branch must be selected by source dynamics, not by choosing a useful decomposition | derived branch frame, not final gauge |
| Pati-Salam-to-SM standard embedding | correct relative charges and hypercharge arithmetic | absolute hypercharge, breaking vacuum, `Z_6` | input replacement by other embeddings must be blocked by source data | derived_relative only |
| Direct source gauge quotient selector | would be strongest route if source stabilizer gives `G_SM/Z_6` | no current theorem | compute stabilizer/kernel from source field or boundary data without naming SM target | missing |
| finite algebra from source geometry | would select `A_F` if derived from source data | current lanes attach `A_F` | forbid `C`, `H`, `M_3(C)` as target inputs | imported/failed |
| Type II_1 fixed-data rigidity selector | could select `T_3` or stronger data if fixed and replacement-proof | no instantiated fixed data | run `X_2`, `X_4`, `X_n`; require first obstruction for `n != 3` | open_empty |
| Type II_1 trace, `C_n`, C3/D4 selectors | clean count labels after choosing `n` | no physical generation selection | same proof works for arbitrary `n` or imports `K_SM` | failed |
| imported finite CC host | can reproduce finite CC controls after import | no explanatory selector | replacing `K_SM tensor C^3` by `K_SM tensor C^n` exposes copied count | hosted/imported |
| Higgs ambient-adjoint branch | Pati-Salam bidoublet slot exists | physical scalar and potential | source projection must be nonzero and light-component unique | hosted/open |
| anomaly shadow after ordinary SM packet | ordinary per-generation perturbative sums cancel | full GU/Type II_1 shadow | every extra observer mode must be listed and checked | derived_relative/open |
| raw compact K3 RS control | compact characteristic-class arithmetic | physical noncompact GU generation index | same-operator, same-symbol, same-H bridge with corrections required | control_only |
| source action/operator branch changes | failure of full selector is stable across current branches | future branch may supply selector | branch-local selector must name exact `I_GU` branch and rollback outside it | no robust selector yet |

## 7. Forbidden Shortcuts And Rollback Conditions

### Forbidden Shortcuts

These moves are not allowed in a source-geometry selector proof:

1. Add QFT matter fields to a background and call them source-selected.
2. Import `A_F = C + H + M_3(C)` and call finite-control selection derived.
3. Import `SU(3) x SU(2) x U(1) / Z_6` or the `Z_6` quotient.
4. Choose a Pati-Salam breaking field, vacuum, or boundary condition because it
   gives the SM.
5. Treat `Y = T_3^R + (B-L)/2` as absolute selection before the source selects
   the embedding and charge lattice.
6. Treat ambient Higgs quantum numbers as the physical Higgs scalar.
7. Insert nonzero Higgs projection, negative mass squared, quartic potential, or
   electroweak vacuum by hand.
8. Use ordinary anomaly cancellation to select the matter packet.
9. Delete extra GU/Type II_1 modes without an observer-shadow theorem.
10. Use `n = 3`, C3, index 3, three arms, three projections, `dim H_F=96`, or
    `K_SM tensor C^3` as selector input.
11. Use `ind_H(D_RS)=8`, `ind_H(D_GU)=24`, `rank_eff=4/8`, or "three
    generations" as index input.
12. Promote compact K3 arithmetic to physical noncompact GU evidence without a
    bridge theorem for the same physical operator.
13. Use Type II_1 host embedding as Type II_1 selector evidence.
14. Claim branch robustness without naming the GU branch and variation space.

### Rollback Conditions

Any positive source-geometry matter/gauge claim must roll back if one of these
fires:

| rollback trigger | rollback target |
|---|---|
| selector input contains `A_F`, `G_SM`, `Z_6`, `K_SM`, physical Higgs, or target generation count | demote to imported/hosted |
| nearest replacement family works for `n=2,4` or arbitrary `n` | demote generation selector to cardinality transport |
| source action/operator branch is not written or not the branch used by the selector | demote to branch-local speculation |
| Pati-Salam breaking is assumed rather than selected | demote SM reps and hypercharge to relative derivation |
| Higgs source projection is zero, noncovariant, or dynamically heavy/unstable | demote Higgs to hosted quantum numbers |
| full observer shadow contains uncanceled anomalous modes | demote anomaly compatibility and matter-shadow finality |
| physical RS complex or H-index is missing | keep `GEN-COUNT` open |
| K3 bridge loses symbol, H-linearity, background `ch_2`, or APS/end correction data | keep K3 control-only |

## 8. First Exact Missing Proof Object

The first exact missing proof object is the source-geometry finite-control
selector:

```text
Phi_SG_MG =
  (
    source_branch_id,
    I_GU_branch,
    s: X -> Y,
    P -> Y,
    D_GU,
    S_GU,
    variation_space,
    boundary/domain data,
    allowed_source_fields
  )
  ->
  (
    G_obs,
    quotient_or_stabilizer_map,
    kernel_lattice,
    A_fin_or_bypass_certificate,
    K_matter,
    hypercharge_generator,
    H_phys,
    anomaly_shadow,
    n_gen,
    provenance_ledger,
    replacement_audit
  ).
```

It must include these subcertificates:

```text
NoTargetInput:
  A_F, G_SM, Z_6, K_SM, physical Higgs, n=3, target index values,
  and ordinary anomaly-free SM shadow do not occur in the input data.

GaugeQuotient:
  a source-derived stabilizer or quotient map produces the observer gauge group
  and the global kernel. If the route is Pati-Salam first, the source also
  selects the breaking and the hypercharge lattice.

FiniteControl:
  either A_F is derived as output, or the construction proves that it is not
  using finite Connes data and supplies an alternate observer finite-control
  shadow.

MatterShadow:
  every observer-facing chiral mode is produced by the source map and listed.

Higgs:
  a source field has a nonzero, gauge-covariant physical Higgs projection and a
  computed potential.

Generation:
  the physical source operator has a noncircular index/readout, with replacement
  tests and K3/Y14 bridge data if K3 is used.
```

Without this object, all existing positive matter/gauge statements remain
representation branch, hosting, or control statements.

If the finite-algebra lane is chosen, the first subobject to build is:

```text
Phi_SG_A:
  source geometry -> A_F = C + H + M_3(C)
```

If the finite-algebra lane is bypassed, the first subobject to build is:

```text
Phi_SG_G:
  source geometry -> SU(3) x SU(2) x U(1) / Z_6
```

Either route must be target-free.

## 9. Next Meaningful Proof/Computation Step

The next meaningful step is a narrow gauge-quotient computation, not another
global synthesis.

Recommended work packet:

1. Fix one source branch from `I_GU` and declare its allowed source fields,
   variation space, domains, and boundary data.
2. Define a candidate source selector `Phi_SG_G` using only that branch. The
   candidate may use stabilizers of source fields such as `theta`, `II_s^H`,
   connection holonomy, or boundary/domain data, but it may not name the SM
   group as a target.
3. Compute the stabilizer or quotient and its global kernel. First binary
   question:

   ```text
   Does the computation output SU(3) x SU(2) x U(1) / Z_6 without importing it?
   ```

4. If the answer is no, record the obstruction and keep the matter/gauge claim
   at Pati-Salam branch/host level.
5. If the answer is yes, immediately run:

   ```text
   hypercharge lattice check,
   Pati-Salam-to-SM representation branch,
   anomaly shadow over all surviving modes,
   Higgs projection and effective potential,
   generation-count replacement audit.
   ```

The generation-specific parallel step is also precise:

```text
derive RS_GU^phys from the actual source operator/action, then prove or refute
the H-linear Fredholm/bridge theorem before using K3 or any index readout.
```

Until one of these proof objects exists, the live claim posture should remain:

```text
Matter/gauge source geometry:
  real Pati-Salam branch evidence,
  no full SM finite-control selector.
```

## Machine-Readable Source-Geometry Selector Gate

```json
{
  "artifact": "MATTER_GAUGE_SOURCE_GEOMETRY_SELECTOR_GATE",
  "version": "2026-06-24",
  "verdict": "NO_SOURCE_GEOMETRY_SELECTOR_YET",
  "status_enum": [
    "derived",
    "derived_relative",
    "hosted",
    "imported",
    "failed",
    "open",
    "control_only",
    "open_empty"
  ],
  "required_selector_fields": [
    "input_independence",
    "branch_closure",
    "gauge_quotient",
    "finite_algebra_if_used",
    "pati_salam_reps",
    "sm_reps",
    "hypercharge",
    "higgs",
    "anomaly_shadow",
    "generation_count",
    "branch_robustness",
    "rollback"
  ],
  "forbidden_target_inputs": [
    "A_F",
    "G_SM",
    "Z_6",
    "K_SM",
    "physical_Higgs",
    "n_equals_3",
    "ind_H_D_RS_equals_8",
    "ind_H_D_GU_equals_24",
    "ordinary_anomaly_free_SM_shadow"
  ],
  "ledger": [
    {
      "datum": "GU carrier Cl(9,5), S=H^64, Sp(64)",
      "status": "derived",
      "provenance": ["primary-gu-interface-contract", "finite-control-provenance-audit"],
      "missing_proof_object": "downstream finite-control selector"
    },
    {
      "datum": "Pati-Salam branch frame",
      "status": "derived",
      "provenance": ["generation-count-sm-branching-closure", "sm-gauge-higgs-finite-control-extraction-ledger"],
      "missing_proof_object": "physical gauge-selection theorem"
    },
    {
      "datum": "Pati-Salam one-generation packet",
      "status": "derived",
      "provenance": ["generation-count-sm-branching-closure"],
      "missing_proof_object": "observer shadow and upstream gauge selector"
    },
    {
      "datum": "SM charge packet and hypercharge",
      "status": "derived_relative",
      "provenance": ["generation-count-sm-branching-closure", "finite-control-provenance-audit"],
      "missing_proof_object": "source-selected Pati-Salam-to-SM embedding and lattice"
    },
    {
      "datum": "Finite Connes algebra A_F",
      "status": "imported",
      "provenance": ["finite-control-provenance-audit", "type-ii1-selector-or-nogo-theorem"],
      "missing_proof_object": "Phi_SG_A target-free finite algebra selector"
    },
    {
      "datum": "SM gauge quotient G_SM/Z_6",
      "status": "failed",
      "provenance": ["finite-control-provenance-audit", "sm-gauge-higgs-finite-control-extraction-ledger"],
      "missing_proof_object": "Phi_SG_G source gauge quotient selector"
    },
    {
      "datum": "SM Higgs quantum-number slot",
      "status": "hosted",
      "provenance": ["sm-gauge-higgs-finite-control-extraction-ledger"],
      "missing_proof_object": "nonzero source projection and light-component selector"
    },
    {
      "datum": "Physical Higgs scalar and potential",
      "status": "open",
      "provenance": ["finite-control-provenance-audit", "sm-gauge-higgs-finite-control-extraction-ledger"],
      "missing_proof_object": "gauge-covariant projection plus effective potential"
    },
    {
      "datum": "Full anomaly-safe observer shadow",
      "status": "open",
      "provenance": ["finite-control-provenance-audit", "canon/type-ii1-spectral-sm-checklist"],
      "missing_proof_object": "functorial shadow listing every observer-facing mode"
    },
    {
      "datum": "Exact generation count n_gen=3",
      "status": "open",
      "provenance": ["live-claim-dag-fault-finality-ledger", "y14-k3-bridge-loss-ledger"],
      "missing_proof_object": "RS_GU_phys plus H-linear Fredholm/index bridge"
    },
    {
      "datum": "Raw compact K3 RS arithmetic",
      "status": "control_only",
      "provenance": ["y14-k3-bridge-loss-ledger"],
      "missing_proof_object": "same-operator Y14/K3 bridge certificate"
    },
    {
      "datum": "Type II_1 fixed-data selector",
      "status": "open_empty",
      "provenance": ["goal-draft-type-ii1-fixed-data-selector-challenge", "type-ii1-selector-or-nogo-theorem"],
      "missing_proof_object": "fixed data X and replacement obstruction for n != 3"
    }
  ],
  "claim_certificates": [
    {
      "claim": "MATTER-SHADOW",
      "current_status": "partial_open",
      "proof_grade": "reconstruction_contract",
      "derived_by_source_geometry": ["Pati-Salam branch packet", "relative SM charges after selected embedding"],
      "hosted": ["observer-facing representation slots"],
      "imported_or_failed": ["finite CC module", "full observer shadow"],
      "missing_proof_object": "Shadow_SG functor with all observer-facing modes and anomaly checks",
      "forbidden_inputs": ["K_SM", "ordinary_SM_shadow", "deleted_extra_modes"],
      "rollback_condition": "shadow imports K_SM or leaves extra modes anomalous",
      "citation_language": "Source geometry derives a Pati-Salam branch; full matter shadow is open."
    },
    {
      "claim": "SM-GAUGE",
      "current_status": "failed",
      "proof_grade": "negative_filter_reconstruction",
      "derived_by_source_geometry": ["Sp(64) source gauge", "Pati-Salam branch frame"],
      "hosted": ["standard Pati-Salam calculation"],
      "imported_or_failed": ["A_F", "G_SM", "Z_6", "Pati-Salam breaking"],
      "missing_proof_object": "Phi_SG_G deriving G_SM/Z_6 from source data",
      "forbidden_inputs": ["A_F", "G_SM", "Z_6", "chosen_SM_subgroup"],
      "rollback_condition": "quotient theorem consumes target group or breaking vacuum",
      "citation_language": "SM gauge quotient is not derived; source geometry reaches Pati-Salam branch data."
    },
    {
      "claim": "HIGGS",
      "current_status": "hosted_open",
      "proof_grade": "reconstruction",
      "derived_by_source_geometry": ["ambient Pati-Salam bidoublet slot"],
      "hosted": ["SM Higgs quantum-number slot"],
      "imported_or_failed": ["physical Higgs scalar", "EWSB potential"],
      "missing_proof_object": "nonzero source projection and effective potential from S_GU",
      "forbidden_inputs": ["physical_Higgs", "nonzero_projection", "negative_mass_squared", "Mexican_hat_potential"],
      "rollback_condition": "projection vanishes or potential lacks EWSB",
      "citation_language": "GU hosts Higgs quantum numbers; Higgs emergence is open."
    },
    {
      "claim": "GEN-COUNT",
      "current_status": "open",
      "proof_grade": "open_none_for_physical_count",
      "derived_by_source_geometry": ["S(6,4) one-generation representation branch"],
      "hosted": ["2+1 representation story", "K3 compact control arithmetic"],
      "imported_or_failed": ["exact n_gen=3", "physical H-index"],
      "missing_proof_object": "RS_GU_phys plus H-linear Fredholm/index bridge and replacement audit",
      "forbidden_inputs": ["n_equals_3", "ind_H_D_RS_equals_8", "ind_H_D_GU_equals_24", "rank_eff_4_or_8"],
      "rollback_condition": "physical index absent, circular, background-dependent, complex-only, or incompatible",
      "citation_language": "Generation count remains open; representation branching is supportive but not a physical index proof."
    }
  ],
  "branch_robustness": [
    {
      "branch": "GU carrier",
      "decision": "derived_carrier_only",
      "robust_output": "Cl(9,5), S=H^64, Sp(64)",
      "missing": "observer finite-control selector"
    },
    {
      "branch": "Pati-Salam branching",
      "decision": "derived_branch_frame_not_final_gauge",
      "robust_output": "Spin(6,4) maximal compact and one-generation packet",
      "missing": "source-selected low-energy gauge quotient"
    },
    {
      "branch": "Pati-Salam-to-SM embedding",
      "decision": "derived_relative",
      "robust_output": "charge arithmetic after embedding",
      "missing": "absolute source selector for embedding and Z_6"
    },
    {
      "branch": "Type II_1 current selectors",
      "decision": "failed_or_open_empty",
      "robust_output": "negative filter against cardinality transport",
      "missing": "fixed-data selector and replacement obstruction"
    },
    {
      "branch": "K3 compact control",
      "decision": "control_only",
      "robust_output": "compact characteristic-class arithmetic",
      "missing": "physical RS_GU bridge"
    },
    {
      "branch": "Higgs source projection",
      "decision": "hosted_open",
      "robust_output": "ambient bidoublet slot",
      "missing": "nonzero projection and potential"
    }
  ],
  "first_missing_proof_object": "Phi_SG_MG source-geometry finite-control selector",
  "next_step": "define and compute Phi_SG_G gauge quotient selector for one fixed source branch"
}
```

## Sources Read

- `explorations/cycle-gates-and-audits/primary-gu-interface-contract-2026-06-24.md`
- `explorations/cycle-gates-and-audits/finite-control-provenance-audit-2026-06-24.md`
- `explorations/type-ii1-spectral/sm-gauge-higgs-finite-control-extraction-ledger-2026-06-24.md`
- `explorations/cycle-gates-and-audits/goal-draft-type-ii1-fixed-data-selector-challenge-2026-06-24.md`
- `explorations/type-ii1-spectral/type-ii1-selector-or-nogo-theorem-2026-06-24.md`
- `explorations/generation-sector/generation-count-sm-branching-closure-2026-06-22.md`
- `explorations/generation-sector/y14-k3-bridge-loss-ledger-2026-06-24.md`
- `canon/type-ii1-spectral-sm-checklist.md`
- `explorations/cycle-gates-and-audits/live-claim-dag-fault-finality-ledger-2026-06-24.md`
