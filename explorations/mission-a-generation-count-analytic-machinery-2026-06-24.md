---
title: "Mission A Generation-Count Analytic Machinery Reconstruction Attempt"
date: "2026-06-24"
status: exploration
doc_type: mission_a_reconstruction_attempt
verdict: "CONDITIONAL_OPEN_FIRST_COMPUTABLE_OBJECT_IDENTIFIED"
owned_path: "explorations/mission-a-generation-count-analytic-machinery-2026-06-24.md"
optional_executable:
  - "tests/mission_a_generation_count_analytic_machinery_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "explorations/y14-k3-bridge-loss-ledger-2026-06-24.md"
  - "explorations/y14-k3-index-bridge-theorem-or-nogo-2026-06-24.md"
  - "explorations/rs-analytic-rank3-rebuild-or-demotion-2026-06-23.md"
  - "explorations/oq-rk2-aps-fc3-fc4-closure-2026-06-23.md"
  - "explorations/oq-rk2-fc4-k3-holonomy-rank-2026-06-23.md"
  - "tests/rs_k3_symbol_index_formula_audit.py"
  - "tests/y14_k3_bridge_loss_audit.py"
  - "active-research/signed-readout/theorem-statement-v1-2026-06-23.md"
  - "explorations/generation-count-rs-symbol-index-contract-2026-06-24.md"
  - "explorations/generation-count-rs-k3-symbol-index-attempt-2026-06-24.md"
  - "explorations/generation-count-rs-clifford-projector-computation-2026-06-24.md"
---

# Mission A Generation-Count Analytic Machinery Reconstruction Attempt

## 1. Verdict

**Verdict: conditional open, with the first computable branch object identified.**

Under Mission A, assume GU is substantially correct as a working hypothesis. Then the
generation-count route cannot stop at "the RS leg is open." If GU is correct, there must be a
specific analytic object that turns the physical Rarita-Schwinger sector into an H-linear
Fredholm index and transports that same index through the noncompact `Y^14` problem or through
a corrected K3/APS control problem.

The current repository does not yet contain that object. It contains strong partial material:

- exact K3 topological data, including `Ahat(K3)=2`, `chi=24`, `sigma=-16`, and `p1=-48`;
- local quaternionic carrier evidence from `Cl(9,5) ~= M(64,H)`;
- explicit raw `Cl(4,0)` gamma-trace projectors and raw ranks;
- compact K3 control formulas for natural RS symbol classes;
- a useful H-linear Fredholm/KSp readout framework once a real Fredholm family exists;
- a sharp `Y^14 -> K3` loss ledger.

But the branch that would derive a physical RS contribution is still missing the first
load-bearing object:

```text
RS_GU^phys
```

as a typed, source-derived, gauge-fixed or BRST elliptic/Fredholm complex with H-structure,
symbol class, background Chern character, and bridge/correction data. Without it, K3 arithmetic
is a compact control calculation and the noncompact `Y^14` route has no named payload to
transport.

Current decision:

```text
generation count: not derived
three generations: not derived
best branch status: OPEN_MISSING_RS_GU_PHYS_AND_BRIDGE_CERTIFICATE
```

Rollback language: any downstream statement that uses `ind_H(D_RS)=8`, `rank_eff=4`,
`ind_H(D_GU)=24`, or "three generations" as an input must be marked `INVALID_CIRCULAR`.

## 2. If GU Is Correct, What Generation-Count Analytic Object Must Exist

If GU is correct, the required object is not a number. It is an analytic machine:

```text
GCA_GU =
  (source_operator,
   RS_GU^phys,
   D^Y_RS,delta,disc,
   H_Fredholm_family,
   Y14_to_K3_or_APS_bridge,
   background_F_certificate,
   noncircular_readout)
```

with the following minimum contents.

| component | required content | current status |
|---|---|---|
| `source_operator` | exact GU source branch, such as `D_GU`, `D_roll`, or an explicitly branched comparison action; plus the gauge symmetry that produces RS fields | underdefined for the physical RS block |
| `RS_GU^phys` | bundles `E_RS^pm`, gamma-trace maps `G_pm`, projectors `P_pm`, gauge maps, gauge condition or BRST ghosts, principal symbol `sigma_RS^phys(xi)`, and right-H certificate | missing |
| `D^Y_RS,delta,disc` | projected weighted noncompact operator `P_disc e^{delta r} D^Y_RS e^{-delta r} P_disc` on `W^{1,2}_{H,delta,disc} -> L^2_{H,delta,disc}` | conditional open |
| `H_Fredholm_family` | compact-remainder parametrix, finite H-kernel/cokernel, closed range, and norm-continuous bounded transforms into `Fred_H(K_H)` | conditional open |
| `Y14_to_K3_or_APS_bridge` | either an H-unitary discrete-mode reduction `U`, or APS compactification for the same physical operator with `eta`, `h`, spectral-flow, and end corrections | underdefined |
| `background_F_certificate` | `F=s^*S(6,4)`, `rank_C(F)=16`, H-connection preservation, and `k=ch_2(F)[K3]` fixed or carried symbolically | rank known, background `k` open |
| `noncircular_readout` | compare the independently computed `I=ind_H(D_RS^phys)` with 8, 16, or other only after the index is computed | guard active |

Why this object must exist if GU is true:

1. The signed-readout theorem can host an H-linear integer readout, but it does not create the
   Fredholm operator or its index. GU needs the operator-level input.
2. The full unprojected noncompact `Y^14` route is blocked by split signature and continuous
   spectrum in the current files. A projected weighted tau/discrete sector or an APS route must
   exist if a finite index is to be recovered.
3. Compact K3 formulas can become physical only if the same physical symbol/operator is
   transported from `Y^14`, or if the compact problem is explicitly the physical branch with all
   corrections paid.
4. Raw RS ranks such as `416`, `96`, `64`, or `24` are not the analytic index and cannot be
   normalized into the target value.

## 3. Non-Circular Reconstruction Attempt

### 3.1 Source Operator To `RS_GU^phys`

The current compact K3 files give a defensible raw object:

```text
V_+ = T_C^*K3 tensor S_4^+ tensor F
V_- = T_C^*K3 tensor S_4^- tensor F
G_+ : V_+ -> S_4^- tensor F
G_- : V_- -> S_4^+ tensor F
R^+ = ker(G_+)
R^- = ker(G_-)
sigma_raw(xi) = P_- (c(xi) tensor 1_F) P_+
```

The raw finite-dimensional model verifies projector identities and shows a sampled raw
projected symbol is full rank on the raw kernels. This is real progress. It rules out a
simple elementary rank defect as the explanation for the missing RS index.

But it does not yet define the physical GU RS sector. The sample gauge check shows the raw
projected symbol does not kill the projected principal gauge image. Therefore the physical
object must add gauge-fixing or BRST data rather than silently treating the raw kernel as the
physical quotient.

There are three live symbol branches:

| branch | virtual coefficient on K3 | status |
|---|---|---|
| full vector-spinor control | `E_full = V tensor F` | compact control only |
| raw gamma-trace-free RS | `E_raw = (V + 1) tensor F` | computable control, not physical GU |
| BRST/anomaly-style comparison | `E_BRST = (V - 1) tensor F` if two spinor ghost complexes are derived | comparison only until derived from GU |

For `E(q)=(V+q) tensor F`, with `n=rank_C(F)` and `k=ch_2(F)[K3]`,

```text
ind_C(E(q)) = (-40 + 2q)n + (4 + q)k.
```

Thus the current defended compact control formulas are:

```text
E_raw:       ind_C = -38 n + 5 k
E_BRST:      ind_C = -42 n + 3 k
flat F, n=16:
  raw        ind_H = -304, if H-linear
  BRST-style ind_H = -336, if H-linear
```

Those are `OTHER_INDEX` controls. If GU is correct and the RS contribution is small and
positive, the physical `RS_GU^phys` complex is not merely the current raw compact symbol in
the flat branch. It must contain additional source-derived gauge/BRST/end data, or a different
symbol class, with a first-principles reason for the change.

### 3.2 `RS_GU^phys` To Rank, Fredholm Class, And Index

The non-circular route must define:

```text
I_RS = ind_H(D_RS^phys) = dim_H ker(D_RS^phys) - dim_H coker(D_RS^phys)
```

not:

```text
I_RS = physical polarization count
I_RS = Ahat(K3) * selected_rank_eff
I_RS = target value needed for three generations
```

For a compact K3 branch, the computation must produce a K-theory symbol class
`[sigma_RS^phys] in K_c^0(T*K3)` or an elliptic complex class and then evaluate the index.
For a noncompact `Y^14` branch, it must produce:

```text
D^Y_RS,delta,disc :
  W^{1,2}_{H,delta,disc}(Y^14) -> L^2_{H,delta,disc}(Y^14)
```

with:

- nonempty tau-twisted `P_disc`;
- boundedness on the weighted Sobolev scale;
- operator invariance modulo compact controlled terms;
- compact-remainder parametrix;
- finite H-kernel and H-cokernel;
- norm-continuous bounded transform family `X -> Fred_H(K_H)`;
- spectral-flow accounting if thresholds cross.

This is the point where the signed-readout theorem becomes relevant: once such an H-linear
Fredholm family exists, its augmentation gives an integer H-line readout. It does not by
itself identify the RS integer.

### 3.3 `Y^14 -> K3` Transport Or APS Control

The `Y^14 -> K3` route has to transport the same physical operator, not a name.

Two non-circular bridges are viable in theorem shape.

**Unitary discrete-sector bridge**

```text
U : L^2_H(K3,Z) -> P_disc L^2_H(Y^14,S)
U^{-1} P_disc D^Y_RS P_disc U = D^K_RS,phys + compact homotopy
```

with the same right-H structure, symbol class, and background data. If this exists, the
compact K3 physical index can equal the projected noncompact physical index.

**APS bridge**

```text
Ind_Y_RS =
  bulk_K3_like_index
  - (eta(A_RS^phys) + h(A_RS^phys))/2
  + SF_bridge
  + C_end
```

where `A_RS^phys` is the boundary operator for the same projected/gauge-fixed physical RS
complex. Older eta cancellations for different boundary operators are not transport.

Current status:

```text
full unprojected Y^14: no-go as current Fredholm route
projected weighted Y^14: conditional open
raw compact K3: control only
physical compact K3 RS: open missing symbol data
Y14 -> K3 physical equality: conditional theorem, underdefined
```

## 4. Genuine Pieces Versus Fitted Or Control-Only Pieces

| item | classification | how it may be used |
|---|---|---|
| `Ahat(K3)=2`, `chi=24`, `sigma=-16`, `p1=-48` | genuine topological input | fixed K3 arithmetic and sanity checks |
| `Cl(9,5) ~= M(64,H)` local carrier | genuine algebraic input, global certificate still needed | motivates H-linearity, but does not alone justify halving a complex index |
| `rank_C(F)=16`, `rank_H(F)=8` if H-structure is verified | genuine representation input | one internal Pati-Salam packet and spin-1/2 compact contribution control |
| raw `Cl(4,0)` projector identities and raw rank `96_C` | genuine finite matrix computation | sanity check for gamma-trace/projectors, not an index |
| Spin(4) irreducible raw rank `24_H` | genuine raw representation count | not the APS effective rank |
| `E_raw=(V+1)F`, `ind_C=-38n+5k` | genuine compact control formula | may be cited as raw K3 control |
| `E_BRST=(V-1)F`, `ind_C=-42n+3k` | comparison formula | physical only if GU BRST complex derives the two subtractions |
| FC3 `Pi_RS`/chirality compatibility and eta symmetry | reconstruction-grade partial proof | usable only for the same RS boundary operator |
| signed-readout H-linear KSp framework | genuine abstract machinery | applies after the H-linear Fredholm family exists |
| `rank_eff=4`, `(chi+sigma)/2`, `b2_plus+b0` | fitted/rejected in current files | not evidence unless derived from the RS symbol/index class |
| physical RS DOF count giving `8` | kinematic count | not an analytic Fredholm index theorem |
| flat `F`, `k=0` | branch assumption | not physical unless the pulled-back Sp(64) background proves it |
| K3 raw arithmetic as physical GU evidence | control-only, currently forbidden | promote only through same-operator bridge and corrections |

## 5. First Exact Obstruction Or Missing Proof Object

The first exact missing proof object is:

```text
RS_GU^phys =
  (source_operator,
   E_RS^+, E_RS^-,
   G_+, G_-,
   P_+, P_-,
   gauge maps,
   gauge-fixing or BRST complex,
   sigma_RS^phys(xi),
   H-structure certificate,
   background F and ch_2(F),
   boundary data if APS is used)
```

It must state whether it is derived from `D_GU`, `D_roll`, an action principle, or an explicitly
branched comparison operator. It must not be selected by asking which formula gives `8`, `16`,
or `24`.

The first bridge-specific missing proof object is:

```text
P_disc theorem for the same RS_GU^phys:
  nonempty tau-twisted sector,
  H-linear projection,
  weighted Sobolev boundedness,
  compact-remainder parametrix,
  finite H-kernel/cokernel,
  bounded-transform family,
  spectral-flow or APS correction accounting.
```

If `P_disc` is empty, unbounded, or not invariant for `RS_GU^phys`, the noncompact branch fails
and K3 remains a separate control model. If `RS_GU^phys` reduces to the standard compact raw
classes already computed, the flat branch gives `OTHER_INDEX`, not Candidate A.

## 6. Constructive Next Computation

The next computation should be an executable certificate, not another prose rank note.

Proposed artifact:

```text
tests/rs_gu_phys_symbol_bridge_certificate.py
```

or an equivalent CAS notebook with a serialized JSON output:

```json
{
  "certificate": "RS_GU_PHYS_SYMBOL_BRIDGE_CERTIFICATE",
  "source_operator": "D_GU|D_roll|comparison",
  "computed_object": "raw|gauge_fixed|elliptic_complex",
  "target_inputs_seen": [],
  "clifford_projectors": {
    "P_plus_idempotent": true,
    "P_minus_idempotent": true,
    "gamma_trace_annihilated": true
  },
  "gauge_or_brst": {
    "provided": false,
    "ghost_complex": null,
    "symbol_level_exact": false
  },
  "symbol_class": {
    "constructed": false,
    "virtual_coefficient": null,
    "ch0": null,
    "ch2": null
  },
  "h_structure": {
    "right_H_global": false,
    "connection_preserves_H": false
  },
  "background": {
    "rank_C_F": 16,
    "ch2_F": "symbolic_or_integer_required"
  },
  "noncompact_bridge": {
    "P_disc_nonempty": null,
    "weighted_fredholm_parametrix": null,
    "unitary_or_APS_bridge": null,
    "eta_spectral_flow_accounted": null
  },
  "decision": "OPEN_MISSING_SYMBOL_DATA"
}
```

Minimal branch decision engine:

1. If target values are present as inputs, return `INVALID_CIRCULAR`.
2. If `RS_GU^phys` is absent, return `OPEN_MISSING_SYMBOL_DATA`.
3. If the symbol or complex is non-elliptic, return `NON_ELLIPTIC`.
4. If H-structure is absent, return `COMPLEX_ONLY_H_STRUCTURE_MISSING`.
5. If `ch_2(F)` is unspecified and the index depends on it, return
   `OPEN_BACKGROUND_DEPENDENT`.
6. If the compact problem is used without a same-operator bridge from `Y^14`, return
   `K3_CONTROL_ONLY`.
7. Only after all gates close, compute `I=ind_H(D_RS^phys)` and compare:

```text
I = 8   -> Candidate A comparison
I = 16  -> Candidate B comparison
else    -> OTHER_INDEX
```

This computation would decide the branch because it forces the first unknown object into a
machine-readable form: either a physical symbol class exists and can be indexed, or the branch
fails before any generation readout is allowed.

## 7. Claim Certificate Table And Machine-Readable Summary

| claim | current status | proof grade | allowed current citation | rollback condition |
|---|---|---|---|---|
| `SPIN_HALF_K3_CONTROL` | conditional control | compact topological arithmetic plus H/background caveats | K3 spin-1/2 control gives `16` H-lines if `F` is the verified flat H-bundle | rollback if H-connection or background invalidates the flat coefficient |
| `RS_GU_PHYS` | missing | none | the required physical RS complex is specified as the first object to construct | any claim using raw K3 RS as physical GU without derivation is invalid |
| `RS_RAW_K3_CONTROL` | computed control | compact characteristic-class control | `E_raw=(V+1)F`, `ind_C=-38n+5k`; flat branch gives `ind_H=-304` if H-linear | rollback physical use unless same-operator bridge and gauge data close |
| `RS_BRST_STYLE_CONTROL` | comparison only | formula control | `E_BRST=(V-1)F`, `ind_C=-42n+3k` if two ghost complexes are independently derived | rollback if ghost subtraction is selected by target matching |
| `Y14_WEIGHTED_FREDHOLM` | conditional open | theorem-shape only | projected weighted route is live only if nonempty bounded `P_disc` and parametrix exist | no-go if `P_disc=0`, unbounded, or non-Fredholm |
| `Y14_K3_TRANSPORT` | underdefined | bridge theorem shape | K3 may be promoted only by H-unitary same-operator bridge or APS correction theorem | control-only if transport loses operator, H-structure, background, or eta data |
| `GEN_COUNT` | open | no proof | generation count remains an explicit construction target | `INVALID_CIRCULAR` if three generations or `ind_H(D_RS)=8` is used as input |

```json
{
  "artifact": "MISSION_A_GENERATION_COUNT_ANALYTIC_MACHINERY",
  "version": "2026-06-24",
  "verdict": "CONDITIONAL_OPEN_FIRST_COMPUTABLE_OBJECT_IDENTIFIED",
  "mission": "MISSION_A_GU_RECONSTRUCTION",
  "three_generations_derived": false,
  "generation_count_claim_status": "NOT_DERIVED",
  "current_decision": "OPEN_MISSING_RS_GU_PHYS_AND_BRIDGE_CERTIFICATE",
  "promotion_allowed_now": false,
  "first_missing_object": "RS_GU^phys",
  "first_computable_object": {
    "id": "RS_GU_PHYS_SYMBOL_BRIDGE_CERTIFICATE",
    "status": "SPECIFIED_NOT_COMPUTED",
    "would_decide": [
      "physical_symbol_class",
      "H_linear_Fredholm_or_APS_index",
      "Y14_to_K3_transport_validity",
      "Candidate_A_vs_Candidate_B_vs_OTHER_INDEX"
    ]
  },
  "required_objects": [
    "source_operator",
    "RS_GU^phys",
    "non_circular_rank_or_index",
    "H_linear_Fredholm_family",
    "APS_or_unitary_bridge",
    "Y14_to_K3_transport_loss_ledger",
    "background_ch2_F",
    "target_input_rollback"
  ],
  "genuine_current_pieces": [
    "K3_topological_inputs",
    "local_Cl95_H_carrier",
    "raw_Cl40_gamma_trace_projectors",
    "raw_K3_RS_control_formula",
    "BRST_style_comparison_formula",
    "signed_readout_framework_after_Fredholm_input"
  ],
  "control_only_or_underdefined": [
    "raw_compact_K3_as_physical_GU_index",
    "physical_RS_complex",
    "tau_discrete_projection",
    "weighted_Fredholm_parametrix",
    "same_operator_Y14_to_K3_bridge",
    "APS_eta_spectral_flow_for_physical_RS",
    "background_ch2_F"
  ],
  "rejected_inputs": [
    "ind_H(D_RS)=8",
    "rank_eff=4",
    "ind_H(D_GU)=24",
    "three_generations",
    "physical_DOF_count_as_index",
    "b2_plus_plus_b0_as_rank_eff_without_derivation",
    "normalization_chosen_after_target"
  ],
  "branch_decision_rule": {
    "I_equals_8": "CANDIDATE_A_COMPARISON_ONLY_AFTER_INDEPENDENT_INDEX",
    "I_equals_16": "CANDIDATE_B_COMPARISON_ONLY_AFTER_INDEPENDENT_INDEX",
    "I_other": "OTHER_INDEX",
    "bridge_missing": "K3_CONTROL_ONLY_OR_UNDERDEFINED",
    "target_input_seen": "INVALID_CIRCULAR"
  }
}
```
