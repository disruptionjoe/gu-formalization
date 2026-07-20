---
title: "PP2 prediction package: matter-parity stable state, conditional on a 126-type rank drop"
status: active_research
doc_type: prediction_package
package_id: PP2
version: "0.1"
package_status: FROZEN_CONDITIONAL_EVENT_CLASS
frozen_at: "2026-07-19T22:45:19-05:00"
owner_item: PRED-CANDIDATE-PACKETS
lane_id: "2"
extends:
  - lab/process/prediction-package-standing-rule.md
  - explorations/channel-swing-CH-SM-2026-07-19.md
  - explorations/blockbuster-p4-generation-doors-2026-07-19.md
  - tests/channel-swings/ch_sm_chain_sweep.py
  - tests/channel-swings/bb_p4_generation_doors_probe.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_action: none
---

# PP2: matter-parity stable state

This freezes candidate packet 2 from the prediction-package standing rule.
It is a conditional event-class packet, not a mass, rate, or discovery claim.
No data, literature limits, or external-facing surfaces were consulted while
freezing it.

## Frozen Prediction

If the source-selected Standard Model rank-drop route is 126-type, and no
later source-action term breaks matter parity, then the branch contains an
exact unbroken matter parity

```text
P_M = (-1)^(3(B-L))
```

and therefore its lightest `P_M = -1` state is exactly stable. A valid
confrontation of this packet must first freeze the branch's mass scale,
couplings, and production channel. Before those are frozen, the packet
predicts only the event-class rule:

- `P_M`-odd states are produced or removed in parity-even combinations.
- A single `P_M`-odd state cannot decay entirely into `P_M`-even Standard
  Model states.
- If a stable `P_M`-odd state lies in an accessible mass window, the branch
  must present either missing-parity final states, stable charged/colored
  relic signatures, or another parity-preserving sink explicitly derived
  from the same frozen source action.

## Condition Chain

1. CH-SM machine-checked the rank-drop lemma: the final rank-reducing step
   to `G_SM` demands a spinorial condensate, `16`- or `126`-type; no tensor
   VEV can substitute.
2. The 126 route preserves matter parity, while a 16 route does not. This
   packet is conditional on the 126 route.
3. Blockbuster P4 checked that matter parity is uniform on the matter `16`
   and even on the tensor VEV menu. Matter parity therefore does not count
   generations, but it is a real `Z/2` selection rule when the 126 route is
   selected.
4. The absolute mass, coupling strength, production rate, and which parity
   odd state is lightest are not fixed here. They remain dynamics-gated.

## Competitor Baseline

The immediate baseline is not "generic dark matter." It is the fork between
two Standard Model rank-drop mechanisms inside the same Spin(10) chain:

- 126-type rank drop: preserves `P_M`; stable lightest `P_M = -1` state.
- 16-type rank drop: breaks `P_M`; no stability rule follows from this
  packet.

This is the same distinction as ordinary SO(10) matter-parity logic, but the
admission evidence here is GU-owned: the CH-SM rank-drop lemma and P4 parity
audit. The packet does not claim supersymmetry, a neutralino, a mass scale, or
a detected anomaly.

## Kill Thresholds

- Formal branch kill: a frozen source-action packet selects the 16 route or
  proves that the 126 route is impossible for the GU construction.
- Symmetry kill: within a frozen 126 branch, a derived allowed operator,
  condensate, boundary condition, or anomaly breaks `P_M`.
- Event-class kill: after a mass/coupling/production packet is frozen, the
  branch requires single production or decay of a `P_M = -1` state into only
  `P_M = +1` states.
- Window kill: after a quantitative window is frozen, every state in that
  window is excluded under the packet's own production and lifetime
  assumptions.

Absence of a current detection does not kill PP2 because the mass scale,
couplings, and accessible window are not frozen.

## Non-Claims

- Not a claim that GU predicts a dark-matter mass.
- Not a claim that the lightest `P_M`-odd state is neutral.
- Not a claim that the 126 route is selected.
- Not a claim that matter parity carries the generation count.
- Not a claim that the mirror-sector packet is frozen; packet 3 remains gated
  on its weld probes.
- Not a claim-status, canon, verdict, public-posture, or external-action
  change.

## Receipts

- `tests/channel-swings/ch_sm_chain_sweep.py`: CH-SM rank-drop lemma and
  matter-parity flag.
- `tests/channel-swings/bb_p4_generation_doors_probe.py`: P4 parity audit,
  including the result that matter parity is scalar on the matter `16` and
  imposes zero equations on the Majorana rank.
- `tests/channel-swings/pp2_matter_parity_packet_check.py`: packet boundary
  and required-field validator for this frozen artifact.

## Next Work

Packet 2 is frozen at conditional event-class grade. The next Lane 2 work is
either packet 3's weld probes or a quantitative follow-up that freezes a
mass/coupling/window for PP2 without using target data to tune it.
