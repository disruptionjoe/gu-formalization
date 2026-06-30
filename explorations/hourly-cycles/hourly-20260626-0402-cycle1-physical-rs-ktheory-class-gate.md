---
title: "Hourly 20260626 0402 Cycle 1 Physical RS K-Theory Class Gate"
date: "2026-06-26"
run_id: "hourly-20260626-0402"
cycle: 1
lane: "PhysicalRSKTheoryClassGate"
doc_type: "frontier_gate"
artifact_id: "PhysicalRSKTheoryClassGate_0402_C1_V1"
verdict: "underdefined_open_missing_symbol_data"
owned_path: "explorations/hourly-20260626-0402-cycle1-physical-rs-ktheory-class-gate.md"
---

# Hourly 20260626 0402 Cycle 1 Physical RS K-Theory Class Gate

## 1. Verdict: underdefined

Verdict: **underdefined / open missing symbol data**.

The repo currently does **not** derive the physical RS K-theory/symbol class as
`E_raw`, `E_BRST_style`, or a third class. It also does not yet prove the physical
RS complex non-elliptic. The strongest defensible decision is:

```text
physical_RS_class_decision = OPEN_MISSING_SYMBOL_DATA
```

The compact K3 controls remain useful:

```text
E_raw        = (V + 1) tensor F
E_BRST_style = (V - 1) tensor F
```

but both are still controls/comparisons until a source-clean physical
gauge-fixed or BRST RS complex is supplied. No generation-count readout is
allowed and no target value is used in this artifact.

## 2. Sources read first

Required sources read first:

| source | use |
|---|---|
| `RESEARCH-POSTURE.md` | Applied Mission A discipline and anti-smuggling guardrails. |
| `process/runbooks/five-lane-frontier-run.md` | Used verdict vocabulary, frontier artifact shape, and no-overlap rules. |
| `explorations/remaining-math-topography-ledger-v0-2026-06-26.md` | Inherited spectral/noncommutative/provenance routing and forbidden shortcuts. |
| `explorations/y14-k3-end-data-topography-gate-2026-06-26.md` | Consumed the handoff naming `PhysicalRSKTheoryClassGate_V0` as the next object. |
| `explorations/y14-k3-index-bridge-theorem-or-nogo-2026-06-24.md` | Consumed the bridge theorem conditions and current underdefined physical index status. |
| `explorations/y14-k3-bridge-loss-ledger-2026-06-24.md` | Preserved K3-control-only discipline and same-operator transport requirements. |
| `explorations/mission-a-generation-count-analytic-machinery-2026-06-24.md` | Consumed `RS_GU^phys` as the first load-bearing missing object. |

Additional targeted sources checked:

| source | use |
|---|---|
| `explorations/gu-typed-operator-action-spine-2026-06-24.md` | Identified `D_roll` as a typed proposal/screen, not proof-grade actual `D_GU`. |
| `explorations/generation-count-rs-k3-symbol-index-attempt-2026-06-24.md` | Checked the compact formulas for `E_raw` and `E_BRST_style`. |
| `explorations/generation-count-rs-symbol-index-contract-2026-06-24.md` | Applied the missing-symbol, non-elliptic, H-structure, and background decision rules. |
| `explorations/generation-count-rs-clifford-projector-computation-2026-06-24.md` | Used the raw projector and gauge-image computation. |
| `explorations/cycle2-physical-rs-projector-effective-operator-certificate-2026-06-24.md` | Applied the missing common physical right-H module/certificate obstruction. |
| `explorations/hourly-20260626-0301-cycle3-dgu-primary-row-transition-closeout.md` | Preserved latest DGU state: actual source operator handle still missing. |
| `explorations/hourly-20260626-0301-cycle3-rs-frame-evidence-transition-closeout.md` | Preserved latest RS state: no typed RS restart from source-frame evidence. |
| `explorations/hourly-20260626-0202-cycle3-dgu-symbol-vz-closeout.md` | Preserved the firewall before symbol work for actual `D_GU`. |

## 3. Specific GU claim/bridge under test

The tested bridge is:

```text
typed GU source/operator
  -> physical RS gauge-fixed or BRST complex RS_GU^phys
  -> K3 K-theory/symbol class
  -> decision among E_raw, E_BRST_style, third class, non-elliptic, or open
```

The exact question is whether the current repo already identifies the physical
RS class as one of:

```text
E_RAW_PHYSICAL
E_BRST_PHYSICAL
THIRD_CLASS
NON_ELLIPTIC
OPEN_MISSING_SYMBOL_DATA
```

Current decision:

```text
OPEN_MISSING_SYMBOL_DATA
```

`D_roll` supplies a typed comparison spine with a coherent 0/1-sector principal
symbol. The current DGU source-intake closeouts still say typed `D_roll` is
screen-only: it may be compared against an accepted actual source operator, but
it is not itself the admitted primary source row or actual `D_GU` operator.

## 4. Terrain classification and forbidden shortcut

Terrain:

```text
primary: spectral-phase + noncommutative-trace + provenance-verifier
secondary: transport-loss + noncompact-APS-end
```

The first invariant to test is not a generation number. It is:

```text
[sigma_RS^phys] in K^0_c(T*K3)
```

or an equivalent source-derived elliptic-complex class with right-H and
background certificates.

Forbidden shortcuts:

1. Treating compact K3 arithmetic as the physical noncompact `Y^14` RS class.
2. Treating `E_raw` as physical because it is the standard raw gamma-trace-free class.
3. Treating `E_BRST_style` as physical because it is familiar from gauge-fixed RS theory.
4. Choosing a ghost subtraction count from a desired downstream readout.
5. Using `ind_H(D_RS)=8`, `ind_H(D_GU)=24`, `rank_eff=4`, `rank_eff=8`, or three generations as inputs.
6. Letting typed `D_roll` occupy the source-operator slot before the actual DGU source row and same-operator witness exist.

## 5. Strongest positive construction attempt

The strongest construction starts from the typed spine and the compact K3
control data.

Typed spine:

```text
D_roll^epsilon(u, psi)
  =
  (
    d_A^* psi,
    d_A u + Phi_2(d_A psi)
  )
  + Z_A^epsilon(u, psi)

sigma_1(D_roll^epsilon)(xi)(u, psi)
  =
  (
    i_xi psi,
    xi tensor u + F_xi psi
  )
```

K3 raw RS control:

```text
V_+ = T_C^*K3 tensor S_4^+ tensor F
V_- = T_C^*K3 tensor S_4^- tensor F

G_+ : V_+ -> S_4^- tensor F
G_- : V_- -> S_4^+ tensor F

R^+ = ker(G_+)
R^- = ker(G_-)

sigma_raw(xi) = P_- (c(xi) tensor 1_F) P_+
```

The compact control computation gives:

```text
E_raw = (V + 1) tensor F
ind_C(E_raw) = -38 n + 5 k
```

The BRST-style comparison says that if two spinor ghost/subtraction complexes
are independently derived from the physical GU gauge fixing, the virtual class
would be:

```text
E_BRST_style = (V - 1) tensor F
ind_C(E_BRST_style) = -42 n + 3 k
```

The positive result is therefore not a physical class decision. It is a narrow
branch table:

| candidate | current status | reason |
|---|---|---|
| `E_raw` | control-only, not physical | The raw gamma-trace-free K3 symbol is computed, but the raw projected symbol does not quotient the projected gauge image. |
| `E_BRST_style` | comparison-only, not physical | The two ghost/subtraction complexes are not derived from GU source/gauge data. |
| third class | possible, unselected | The actual physical quotient/BRST/gauge-fixing data could change the virtual class. |
| non-elliptic | not decidable | The physical complex is not specified, so ellipticity cannot yet be tested. |

This is enough to decide that the repo has not yet selected the physical RS
K-theory payload.

## 6. First exact obstruction or missing proof object

The first missing proof object is:

```text
RS_GU^phys =
  (source_operator_branch,
   accepted_source_operator_handle,
   E_RS^+, E_RS^-,
   G_+, G_-,
   P_+, P_-,
   gauge_symbol,
   gauge_condition or BRST ghost complex,
   sigma_RS^phys(xi),
   ellipticity_or_exactness_certificate,
   H_structure_certificate,
   F = s^*S(6,4),
   ch_2(F)[K3] status)
```

There are two stacked blockers.

First, for an actual `D_GU` branch, the current DGU closeouts still lack:

```text
PrimarySourceDGU01SectorRuleRowInstance_V1.source_row_payload
PrimarySourceDGU01SectorRuleRowInstance_V1.actual_operator_handle
```

Second, even on the typed `D_roll` comparison branch, the RS physical symbol
needs quotient/BRST data:

```text
gauge_condition or BRST ghost complex
symbol-level exactness
ellipticity certificate
K-theory class
right-H preservation
background ch_2(F) policy
```

Without those fields, the ghost/subtraction coefficient is not determined. In
the notation `E(a) = (V + 1 - a) tensor F`, the repo currently knows useful
controls at `a=0` and `a=2`, but it does not derive the physical value of `a`.

## 7. What would change if the hole closed

If `RS_GU^phys` were supplied, the gate would become computable:

1. If its K3 symbol class is `E_raw`, then `E_RAW_PHYSICAL` would be admitted and the raw control formula would become the physical compact class for the same source branch.
2. If its BRST/ghost complex derives exactly the two spinor subtractions, then `E_BRST_PHYSICAL` would be admitted.
3. If its quotient, ghost, or gauge-fixing data produce a different virtual coefficient or a nonstandard elliptic complex, then `THIRD_CLASS` would be admitted.
4. If the source-derived complex is not elliptic and no Fredholm replacement is supplied, then `NON_ELLIPTIC` would be admitted.

Only after that class decision would the bridge and end-data work be meaningful:

```text
physical K3 symbol class
  -> same-operator Y14/K3 or APS transport packet
  -> H-linear/background/end-correction checks
```

This artifact does not run that downstream readout.

## 8. What would falsify or demote the route

The current route should be demoted or killed under the relevant branch if any
of the following occurs:

| failure | effect |
|---|---|
| Actual source `D_GU` has no operator branch equivalent to the typed RS 0/1 sector | `D_roll` remains comparison-only; physical class must be recomputed or route blocks. |
| The source-derived RS gauge/BRST complex is non-elliptic with no Fredholm replacement | Physical K3 symbol route fails as currently stated. |
| The ghost/subtraction complex is selected by target matching rather than source gauge data | Route is invalid by provenance-smuggling. |
| Right-H structure is not preserved by the operator, projectors, ghosts, connection, or bridge maps | Complex-only result; no H-class/readout may be claimed. |
| The class depends on `k = ch_2(F)[K3]` and the physical background does not fix it | Background-dependent open branch. |
| The K3 class cannot be proved same-operator/same-symbol with noncompact `Y^14` or APS data | K3 remains control-only even if the compact physical class is known. |

None of these failures is established here. They are the kill conditions for
the next proof object.

## 9. Next meaningful computation or proof step

The next meaningful object is:

```text
RSGUPhysSymbolPacket_V0
```

Minimum packet:

```json
{
  "source_operator_branch": "actual_D_GU|D_roll_comparison|explicit_comparison",
  "accepted_source_operator_handle": null,
  "typed_domain": null,
  "typed_codomain": null,
  "E_RS_plus": null,
  "E_RS_minus": null,
  "gamma_trace_maps": null,
  "gauge_symbol": null,
  "gauge_condition": null,
  "BRST_complex": null,
  "symbol_class": null,
  "ellipticity_or_exactness": null,
  "right_H_certificate": null,
  "background_F": {
    "rank_C": 16,
    "ch2_K3": "symbolic_or_fixed_by_source_required"
  },
  "decision": "OPEN_MISSING_SYMBOL_DATA"
}
```

For the actual `D_GU` branch, this is downstream of an accepted primary source
row and actual operator handle. For the typed `D_roll` branch, it may proceed
only as a labeled comparison branch unless a source-clean same-operator witness
closes.

## 10. Claim-status consistency result

No claim status changes are made.

This artifact sharpens the existing blocker:

```text
RS_GU^phys / physical RS K-theory class is missing.
```

It does not promote `E_raw`, `E_BRST_style`, a third class, non-ellipticity, or
any generation-count claim. The claim-status consistency workflow is therefore
not triggered.

## 11. JSON Summary

```json
{
  "artifact_id": "PhysicalRSKTheoryClassGate_0402_C1_V1",
  "run_id": "hourly-20260626-0402",
  "cycle": 1,
  "lane": "PhysicalRSKTheoryClassGate",
  "artifact_path": "explorations/hourly-20260626-0402-cycle1-physical-rs-ktheory-class-gate.md",
  "verdict_class": "underdefined_open_missing_symbol_data",
  "target_import_used": false,
  "claim_status_consistency_triggered": false,
  "generation_readout_allowed": false,
  "source_branch": "typed_D_roll_screen_only_actual_D_GU_primary_row_payload_and_operator_handle_missing",
  "physical_rs_class_decision": "OPEN_MISSING_SYMBOL_DATA",
  "e_raw_physical": false,
  "e_brst_physical": false,
  "third_class_possible": true,
  "first_missing_object": "RS_GU^phys_source_clean_gauge_fixed_or_BRST_elliptic_symbol_packet",
  "next_frontier_object": "RSGUPhysSymbolPacket_V0"
}
```
