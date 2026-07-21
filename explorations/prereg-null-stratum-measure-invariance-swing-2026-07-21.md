---
title: "Preregistration: null-stratum measure invariance and concurrency comparison"
status: preregistered
doc_type: exploration
created: 2026-07-21
portfolio_item: FALSIFICATION-BATTERY
lane: "1"
targets: [T-D1, T-D2, T-D3, H-D1, H-D2]
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_actions: none
---

# Null-stratum measure invariance swing

## Decision question

Is the reported `~8%` `q=P-T<0` end fraction a fixed spectral/geometric
invariant, rather than a fraction induced by one finite sampling measure? If a
fixed external-datum-stratum measure exists, does committed GU structure also
supply an independently defined causally-concurrent/non-orderable stratum whose
measure can be compared without circular identification?

## Construction fork

- Null sector: use GU's program-native DeWitt `(9,5)` / Krein end geometry and
  the committed genuine-flat-end construction from Prong 0. Do not replace it
  with a standard Lorentzian probability model.
- Concurrency: require an independently defined GU-native causal-past
  retraction or a frozen provenance-bearing cross-owner map. Do not define
  concurrency as `q<0` and then count the resulting equality as evidence.

## Load-bearing inputs

- `explorations/oracle-relative-prong0-measure-lemma-2026-07-21.md`
- `tests/channel-swings/oracle_relative_prong0_measure_lemma_probe.py`
- `explorations/hypothesis-and-test-registry-from-councils-2026-07-21.md`
- `explorations/council-committed-constructions-systems-2026-07-21.md`
- `explorations/construction-prong3-verify-2026-07-21.md`

## Predeclared tests and outcomes

### T-D2: fraction invariance

Recompute the `q<0` fraction on the same committed end construction under:

1. the original isotropic Euclidean-sphere direction sampler;
2. timelike-suppressed and timelike-amplified full-support direction samplers;
3. multiple finite end radii; and
4. the existing optional off-Weyl boost conjugation.

- `D2-INVARIANT`: fractions agree within deterministic Monte Carlo tolerance
  across the declared samplers and radii, and a normalized native measure
  explains why.
- `D2-SAMPLER-DEPENDENT`: fractions move materially with sampler or cutoff, or
  the native noncompact volume supplies no normalized probability measure.
- `D2-UNDERPOWERED`: the probe cannot distinguish the outcomes.

The test concerns the number, not the already-banked existence of genuine
`q<0` ends or the exact `K_S`-null result on their spectral halves.

### T-D1: zero-percent control

Verify that at least one declared full-support ensemble returns a reproducible
strictly positive `q<0` fraction. A zero result across every declared ensemble
would fire T-D1. A positive fraction does not by itself establish a canonical
percentage.

### T-D3: concurrency comparison

Audit the committed inputs for a GU-native causal-past retraction or an explicit
map carrying a frozen external concurrency predicate onto the same end space.

- `D3-COMPARABLE`: an independent predicate and common normalized measure exist;
  compute both fractions.
- `D3-DIFFERENT`: the independent fractions differ; H-D2 is falsified at the
  available grade.
- `D3-UNDERDEFINED`: no independent predicate/map/common measure exists.

An equality obtained only by defining the concurrency set as the null set is a
planted positive control and must be rejected.

## Owned outputs

- `tests/channel-swings/null_stratum_measure_invariance_probe.py`
- `explorations/null-stratum-measure-invariance-2026-07-21.md`

## Boundary

No Lean/Lake, external data, claim or canon status, P2C packet, portfolio,
`NEXT-STEPS`, public posture, or external action moves in this swing.
