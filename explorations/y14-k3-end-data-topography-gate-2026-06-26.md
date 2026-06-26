---
title: "Y14/K3 End-Data Topography Gate"
date: "2026-06-26"
status: exploration
doc_type: topography_gate
verdict: "K3_CONTROL_ONLY; PHYSICAL_GENERATION_COUNT_BLOCKED_ON_RS_PAYLOAD_AND_END_DATA"
owned_path: "explorations/y14-k3-end-data-topography-gate-2026-06-26.md"
optional_executable:
  - "tests/y14_k3_end_data_topography_gate_audit.py"
depends_on:
  - "explorations/remaining-math-topography-ledger-v0-2026-06-26.md"
  - "explorations/y14-k3-index-bridge-theorem-or-nogo-2026-06-24.md"
  - "explorations/y14-k3-bridge-loss-ledger-2026-06-24.md"
  - "explorations/mission-a-generation-count-analytic-machinery-2026-06-24.md"
  - "explorations/oc2-b-parametrix-y14-2026-06-23.md"
  - "explorations/oc2-sobolev-a1-bounded-transform-2026-06-23.md"
  - "explorations/oq3b-literature-verification-2026-06-23.md"
  - "explorations/oq-rk2-aps-fc3-fc4-closure-2026-06-23.md"
  - "explorations/oq-rk2-fc4-k3-holonomy-rank-2026-06-23.md"
  - "explorations/oc1-oc2-aps-closure-2026-06-23.md"
---

# Y14/K3 End-Data Topography Gate

## 1. Verdict

**Verdict: K3 remains a compact control surface. The physical generation-count
route is blocked on the physical RS payload and end-data transport package.**

The terrain classification is confirmed:

```text
primary terrain: noncompact-APS-end + transport-loss
secondary terrain: spectral-phase + noncommutative-trace + provenance-verifier
forbidden shortcut: compact K3 arithmetic used as physical noncompact Y14 index
```

This gate does not promote or demote the generation-count claim. It sharpens the
first exact missing object for the next run.

The compact K3/APS control model does **not currently preserve** the physical
noncompact `Y^14` RS index data. It might preserve that data if a same-operator,
same-symbol, same-H, same-background bridge theorem is supplied, with APS/end
corrections paid. The current files do not yet supply that bridge.

Current decision:

```text
GEN_COUNT: OPEN
K3_CONTROL: CONTROL_ONLY
Y14_UNPROJECTED_FREDHOLM: NO_GO_AS_CURRENT_ROUTE
Y14_PROJECTED_WEIGHTED_FREDHOLM: CONDITIONAL_OPEN
Y14_K3_PHYSICAL_EQUALITY: UNDERDEFINED
NEXT_OBJECT: PhysicalRSKTheoryClassGate_V0
```

## 2. What Changed Relative To Earlier Ledgers

Earlier artifacts already established that raw K3 arithmetic is control-only.
This pass adds a narrower routing decision:

```text
Do not run the bridge map first.
First identify the physical RS K-theory / symbol payload that the bridge would carry.
```

Reason: a unitary `Y^14 -> K3` bridge or APS compactification cannot preserve
physical generation data until the payload is named. The current raw K3 classes
`E_raw=(V+1)F` and `E_BRST_style=(V-1)F` are useful controls, but neither is
proved to be the physical GU RS class.

## 3. End-Data Payload Ledger

| payload stage | current status | what must survive transport | decision |
|---|---|---|---|
| Physical RS complex | underdefined | source-derived gauge-fixed or BRST RS complex, gamma-trace maps, gauge maps, symbol class, H-structure | `OPEN_MISSING_SYMBOL_DATA` |
| K3 RS symbol class | control-only | proof that compact class is the reduction of the same physical `Y^14` class | raw `E_raw`/`E_BRST_style` are controls only |
| Tau/discrete projection | conditional/open | nonempty finite `P_disc`, H-linear, bounded on weighted Sobolev spaces, invariant modulo compact terms | scalar route no-go; tau RS sector unproved |
| Weighted Fredholm closure | conditional/open | compact-remainder parametrix on `W^{1,2}_{H,delta,disc} -> L^2_{H,delta,disc}` | Window 0 `delta > 0` is identified; rank-3 end calculus remains input |
| Bounded transform family | underdefined | norm-continuous `X -> Fred_H(K_H)`, common H-Hilbert model, spectral-section control | pointwise Fredholmness is insufficient |
| Compactification / unitary bridge | underdefined | H-unitary `U` or APS compactification for the same physical operator | no bridge map currently supplied |
| Right-H certificate | partial/local | H-linearity of operator, connection, projectors, ghost maps, boundary maps, and bridge maps | local `Cl(9,5)=M(64,H)` is not enough |
| Background `ch_2(F)` | underdefined | physical value of `k=ch_2(F)[K3]` or proof of independence | flat `k=0` is imported unless derived |
| APS/end correction | corrected but uncomputed | `eta(A_RS^phys)`, `h(A_RS^phys)`, `SF_bridge`, `C_end` for the same operator | cannot ignore end data |
| Generation readout | forbidden until index exists | independent `ind_H(D_RS^phys)`, then compare to 8/16/other | target values are forbidden inputs |

## 4. Source Facts That Survive This Gate

The following are still useful:

1. `Ahat(K3)=2`, `chi(K3)=24`, `sigma(K3)=-16`, and `p1(K3)=-48`
   remain fixed compact topological facts.
2. `Cl(9,5) ~= M(64,H)` remains strong local evidence for a right-H carrier.
3. The compact raw RS formulas remain valid as control arithmetic:

```text
E_raw = (V + 1) tensor F
ind_C(E_raw) = -38 n + 5 k

E_BRST_style = (V - 1) tensor F
ind_C(E_BRST_style) = -42 n + 3 k
```

4. The b-parametrix terrain is partially mapped: indicial roots are known at
   reconstruction grade and Window 0 (`delta > 0`) is the natural L2 Fredholm
   regime for a projected discrete sector.
5. The APS eta symmetry for the flat boundary model has partial support from
   the `Pi_RS` / chirality compatibility argument, but only for the same boundary
   operator.

## 5. Source Facts That Do Not Survive As Physical Generation Evidence

The following may not be used as physical generation-count proof:

1. Raw compact K3 arithmetic without a same-operator bridge.
2. The failed scalar `SL(4,R)/SO_0(3,1)` discrete-series route.
3. The tau-correction / formal-degree route as a literal theorem.
4. Physical degree-of-freedom count treated as an analytic Fredholm index.
5. Reverse-engineered formulas such as `rank_H(E_RS^eff)=b_2^+(K3)+b_0(K3)=4`.
6. Eta cancellations from a boundary operator other than `A_RS^phys`.
7. Complex index values divided by two without a global right-H certificate.
8. A flat `F` or `k=0` branch unless the physical Sp(64) background derives it.

## 6. Terrain Decision Tree

```text
1. Is RS_GU^phys specified from the typed GU operator/action?
   no  -> OPEN_MISSING_SYMBOL_DATA; K3 remains control-only.
   yes -> continue.

2. Is its K3 symbol/K-theory class identified?
   no  -> PHYSICAL_RS_KTHEORY_CLASS_OPEN.
   yes -> continue.

3. Does the class equal raw E_raw, BRST-style E_BRST, or a third class?
   raw/control only -> compare as control, not physical.
   derived physical -> continue.

4. Is there a nonempty bounded tau-discrete projected Y14 sector for the same class?
   no  -> Y14 projected route fails; try APS compactification only.
   yes -> attempt H-unitary discrete-sector bridge.

5. Is there an APS compactification for the same physical boundary operator?
   no  -> UNDERDEFINED_BRIDGE_MAP.
   yes -> compute eta, h, spectral flow, and end correction.

6. Is every bridge map right-H linear and family-continuous?
   no  -> COMPLEX_ONLY_OR_NO_KSP_FAMILY.
   yes -> compute independent ind_H(D_RS^phys).

7. Does the independent result equal 8, 16, or another value?
   8     -> Candidate A comparison is allowed.
   16    -> Candidate B comparison is allowed.
   other -> OTHER_INDEX; generation normalization may fail.
```

## 7. Most Impactful Next Goal

The next standard run should not target another K3 number. It should target:

```text
PhysicalRSKTheoryClassGate_V0
```

Goal shape:

```text
Starting from the typed GU source operator/action and the current compact K3
control formulas, derive or refute the physical RS K-theory/symbol class.
Decide whether the physical class is E_raw, E_BRST_style, or a third class.
No generation-count readout is allowed.
```

Required output fields:

| field | requirement |
|---|---|
| source branch | `D_GU`, `D_roll`, or explicitly branched comparison operator |
| bundles | `E_RS^+`, `E_RS^-`, gamma-trace maps, chirality convention |
| gauge/BRST data | gauge map, gauge-fixing block, ghost complex or proof none is needed |
| symbol class | class in compact K3 K-theory or elliptic-complex language |
| H certificate | which maps preserve right-H structure globally |
| background | `F=s^*S(6,4)`, `rank_C(F)=16`, status of `ch_2(F)` |
| no-target-smuggling | no use of `ind_H(D_RS)=8`, `rank_eff=4`, or three generations |
| decision | `E_RAW_PHYSICAL`, `E_BRST_PHYSICAL`, `THIRD_CLASS`, `NON_ELLIPTIC`, or `OPEN_MISSING_SYMBOL_DATA` |

Why this is the highest-impact gate:

```text
Every bridge, APS correction, weighted Fredholm theorem, and generation readout
depends on the physical RS payload. Without it, the bridge transports a name.
With it, the next run can decide whether to pursue the unitary Y14 bridge,
the APS correction package, or a demotion/no-go for the generation route.
```

## 8. Secondary Next Objects

After `PhysicalRSKTheoryClassGate_V0`, the next object depends on the result.

| if result | next object | purpose |
|---|---|---|
| physical class found | `Y14K3EndDataTransportPacket_V0` | track operator, symbol, H-structure, background, eta, `h`, spectral flow, and end corrections |
| physical class found and noncompact route preferred | `TauDiscreteProjectionTheoremOrNoGo_V0` | prove/refute nonempty bounded `P_disc` for the same physical class |
| physical class found and APS route preferred | `PhysicalRSAPSBoundaryCorrectionPacket_V0` | compute `A_RS^phys`, `eta`, `h`, and boundary/end corrections for the same operator |
| no physical elliptic class | `GenerationCountRouteDemotion_V0` | demote K3/RS generation route to control-only until a new class is supplied |
| class depends on `ch_2(F)` | `BackgroundFCh2Gate_V0` | decide whether `k` is physical, symbolic, zero, or imported |

## 9. Three-Generation Route Alternatives After RS Failure

Add `explorations/three-generation-route-alternatives-after-rs-failure-2026-06-26.md`
to the idea bank for solving three generations. It adds three guarded route objects:

| route object | steelman | guardrail |
|---|---|---|
| `WholeOperatorIndexRoute_V0` | compute `ind_H(D_GU^phys)` directly as a whole-operator Fredholm/APS/KSp object, without isolating an RS `8` first | no use of `ind_H(D_RS)=8`, `16 + 8 = 24`, or compact `chi(K3)=24` as physical evidence |
| `PhysicalTopologyGenerationClass_V0` | find a source-derived characteristic class, K-theory class, intersection number, obstruction class, or family index that forces `3` or `24` topologically | no loose K3 numerology, hidden `3/2` factor, or class detached from the physical GU branch |
| `RSDecompositionValidityAudit_V0` | prove or demote the split `ind_H(D_GU)=ind_H(D_{1/2})+ind_H(D_RS)` as a physical invariant of the coupled GU operator | no block-additivity assumption without source, H-linear, gauge/BRST, Fredholm, and end-data compatibility |

Practical routing:

```text
Run RSDecompositionValidityAudit_V0 as a firewall.
If the split is validated, PhysicalRSKTheoryClassGate_V0 remains first for the RS route.
If the split is underdefined or fails, reroute to WholeOperatorIndexRoute_V0.
Run PhysicalTopologyGenerationClass_V0 only when the topological class is tied to the
physical GU bundle/operator, not merely to a compact control surface.
```

These alternatives do not promote the generation-count claim. They expand the next-bank
options while preserving the current `GEN_COUNT: OPEN` status.

## 10. Claim Impact

| claim | impact of this gate |
|---|---|
| `K3-CONTROL` | unchanged; remains useful compact control arithmetic |
| `RS-SYMBOL` | remains specified/open; physical K-theory class is the immediate blocker |
| `Y14_WEIGHTED_FREDHOLM` | remains conditional; not primary until payload exists |
| `Y14_K3_TRANSPORT` | remains underdefined; bridge cannot be filled before payload |
| `GEN-COUNT` | remains open; no promotion allowed |

## 11. Machine-Readable Summary

```json
{
  "artifact": "Y14_K3_END_DATA_TOPOGRAPHY_GATE",
  "version": "2026-06-26",
  "verdict": "K3_CONTROL_ONLY_PHYSICAL_GENERATION_COUNT_BLOCKED_ON_RS_PAYLOAD_AND_END_DATA",
  "terrain": ["noncompact-aps-end", "transport-loss", "spectral-phase", "noncommutative-trace"],
  "forbidden_shortcut": "compact_K3_arithmetic_as_physical_noncompact_Y14_index",
  "current_decisions": {
    "GEN_COUNT": "OPEN",
    "K3_CONTROL": "CONTROL_ONLY",
    "Y14_UNPROJECTED_FREDHOLM": "NO_GO_AS_CURRENT_ROUTE",
    "Y14_PROJECTED_WEIGHTED_FREDHOLM": "CONDITIONAL_OPEN",
    "Y14_K3_PHYSICAL_EQUALITY": "UNDERDEFINED"
  },
  "first_invariant_to_test": "physical_RS_K_theory_or_symbol_class",
  "next_object": "PhysicalRSKTheoryClassGate_V0",
  "route_alternatives_after_rs_failure": [
    "WholeOperatorIndexRoute_V0",
    "PhysicalTopologyGenerationClass_V0",
    "RSDecompositionValidityAudit_V0"
  ],
  "downstream_objects": [
    "Y14K3EndDataTransportPacket_V0",
    "TauDiscreteProjectionTheoremOrNoGo_V0",
    "PhysicalRSAPSBoundaryCorrectionPacket_V0",
    "GenerationCountRouteDemotion_V0",
    "BackgroundFCh2Gate_V0"
  ],
  "forbidden_inputs": [
    "ind_H(D_RS)=8",
    "ind_H(D_GU)=24",
    "rank_eff=4",
    "rank_eff=8",
    "three_generations",
    "physical_DOF_count_as_analytic_index",
    "reverse_engineered_b2_plus_plus_b0_rank"
  ],
  "kill_conditions": [
    "no_source_derived_RS_GU_phys",
    "no_K3_symbol_class_for_same_physical_operator",
    "empty_or_unbounded_P_disc_for_same_operator",
    "APS_boundary_operator_not_A_RS_phys",
    "eta_h_spectral_flow_or_end_corrections_uncomputed",
    "right_H_structure_not_global",
    "background_ch2_F_imported_or_unfixed",
    "generation_target_used_as_input"
  ],
  "promotion_allowed_now": false
}
```

## 12. Bottom Line

The compact K3 arithmetic is not the problem. It is already useful as control.
The physical generation-count route is blocked because the repo has not yet
named the physical RS K-theory payload that either a noncompact projected
Fredholm theorem or an APS bridge would transport.

The next run should therefore attack `PhysicalRSKTheoryClassGate_V0`, not another
generation readout.
