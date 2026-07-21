---
title: "Null-stratum measure invariance test: positive sector survives, fixed ~8% fails, concurrency comparison underdefined"
status: active_research
doc_type: exploration
created: 2026-07-21
prereg: explorations/prereg-null-stratum-measure-invariance-swing-2026-07-21.md
portfolio_item: FALSIFICATION-BATTERY
lane: "1"
targets: [T-D1, T-D2, T-D3, H-D1, H-D2]
probe: tests/channel-swings/null_stratum_measure_invariance_probe.py
outcome: FAIL
scientific_grade: deterministic_fixture_recomputation_and_structural_measure_audit
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_actions: none
---

# Null-stratum measure invariance result

## Result up front

> **`FAIL` for the fixed-`~8%` clause.** The committed Prong-0 geometry still
> contains a genuine open `q=P-T<0` / `K_S`-null end sector, but `~8%` is not a
> fixed spectral/geometric invariant at the available grade. It is the output of
> one finite probability law and cutoff on noncompact end directions.
>
> **T-D1 survives qualitatively:** all nine declared full-support ensembles
> returned a strictly positive `q<0` fraction.
>
> **T-D2 returns `D2-SAMPLER-DEPENDENT`:** the fraction ranged from `0.5%` to
> `25.0%`; the original-style isotropic radius-5 row returned `7.5%`, consistent
> with the earlier rounded `8%` but not invariant under declared perturbations.
>
> **T-D3 returns `D3-UNDERDEFINED`:** committed GU inputs contain no independent
> causal-past retraction/concurrency predicate on the same end space and no
> frozen provenance-bearing map supplying one. Defining concurrency as `q<0`
> would plant the desired equality and is rejected.

No claim status, canon verdict, or public posture moves. The result narrows the
battery hypothesis rather than changing governed scientific status.

## Construction and fork discipline

The null set was computed on GU's program-native DeWitt `(9,5)` / Krein genuine
flat-end construction by reusing the committed Prong-0 probe. No standard
Lorentzian probability default replaced that geometry.

The probability law over directions is a separate object. Three full-support
Gaussian direction laws were used before Euclidean normalization:

- timelike-suppressed (`alpha_3` scale `0.35`);
- original-style isotropic (`1.0`); and
- timelike-amplified (`3.0`).

Each was evaluated at finite radii `3`, `5`, and `7`, with the existing optional
off-Weyl `O(3,1)` boost conjugation. The boosts preserve the construction; the
direction laws pressure whether the reported percentage is measure-independent.

## Deterministic result table

| time-direction scale | radius 3 | radius 5 | radius 7 |
|---:|---:|---:|---:|
| `0.35` | `2.8%` | `2.6%` | `0.5%` |
| `1.00` | `10.0%` | `7.5%` | `9.3%` |
| `3.00` | `19.6%` | `25.0%` | `24.8%` |

All covariance laws are positive definite and therefore have full support.
The `24.5` percentage-point spread is far beyond finite-sample tolerance and
changes monotonically in the expected direction when timelike-dominant rays
receive more or less weight.

The qualitative result is stronger than a one-row count: `q<0` occurs for every
declared full-support ensemble. This preserves the existence of a genuine
positive-measure obstruction under such measures, the exact `K_S`-null theorem
on crossed spectral halves, and Prong 0's operator-nonconstruction result.

## Why the native volume does not rescue a percentage

The committed Prong-0 measure `sqrt(abs(det G)) ds` is a native radial density,
not automatically a normalized probability distribution over the noncompact
space of end directions. The probe finds

```text
d/ds log sqrt|det G|  = -8  on the conformal-up ray
d/ds log sqrt|det G|  = +8  on the opposite conformal-down ray
```

Thus opposite genuine rays carry opposite radial volume behavior. Integrating
the native noncompact volume does not yield a finite probability distribution
without an additional cutoff or direction-weight prescription. Such a
prescription may be scientifically legitimate, but it is additional data and
its resulting fraction cannot be billed as a measure-free invariant.

## T-D3 audit

The systems-council constructions propose that the external-datum stratum is
the causally-concurrent/non-orderable stratum. The committed GU sources cited by
the registry provide:

- the `q<0` / `K_S`-null predicate on genuine fiber ends;
- analogies to coin rounds, split-brain configurations, FLP bivalence, and TaF
  causal-past retractions; and
- no GU-native causal-past retraction on the same end space, no independent
  concurrency predicate, and no frozen cross-owner map tying one to the other.

There are therefore not two independently defined sets to measure. Assigning
`concurrent := (q<0)` makes the equality true by definition and fails the
preregistered planted-positive control. H-D2 remains a scaffold-level analogy
with an unmet interface burden; no equality or inequality is computed.

## What changed and what did not

Changed at exploration grade:

- the fixed numeric reading of H-D1 is unsupported; report a positive null
  sector under declared full-support samplers, not a canonical `~8%` invariant;
- T-D2 is resolved `D2-SAMPLER-DEPENDENT`; and
- T-D3 is classified `D3-UNDERDEFINED` pending an independent predicate/map and
  common measure.

Unchanged:

- Prong 0's existence of genuine `q<0` ends;
- exact `K_S` nullity on the crossed spectral halves;
- operator nonconstruction on those ends;
- three-seam outcomes `A-NUMEROLOGY`, `B-FAILS`, and `C-SCAFFOLD`;
- the P2C packet boundary;
- claims, canon, verdicts, portfolio, `NEXT-STEPS`, and public posture.

## Next-Work Handoff

### Within Lane 1

1. `FALSIFICATION-BATTERY`: classify the internal track as largely exhausted
   for now. T-D1/T-D2 are decided here; T-D3 is interface-underdefined; T-E2 and
   T-B3 are completed; T-C2's Cech/one-arrow content was already computed in the
   construction swing and should not be repeated. Reopen on a genuinely distinct
   structural test, an independent concurrency map, or a fired experimental
   falsifier.
2. `OPERATOR-END-PENCIL`: remains blocked on a source-owned noncompact-end /
   operator-lift packet; do not rerun Q1a or the settled Q2.
3. `CONSTRUCTION-SPACE-EXPLORATION`: remains source-gapped at the C1 packet and
   must not infer the seven unresolved axes.

### Cross-lane rerank

1. **Lane 2 — `P-OBS-LEG`**: recommended next lane. Its wake condition is met by
   frozen Prediction Packet 1, and current committed maps name it as the strongest
   independent alternative after the C1 source gap.
2. **Lane 1 — source-gated leaders**: retain the protected purpose, but wait for
   the operator-end/C1 source object or genuinely new battery evidence.
3. **Lane 3 — `PROOF-STABLE-KERNELS`**: normally the hardening leader, but its
   next step starts with a Lean/Lake baseline and was ineligible in this run.

Recommended scheduling switch: **Lane 2 / `P-OBS-LEG`**. This is an advisory
handoff, not a durable portfolio edit. Daily Stewardship should reconcile the
stale `OPERATOR-END-PENCIL` Q2 wording and the battery's now-exhausted internal
list.

## Validation and boundary

`python tests/channel-swings/null_stratum_measure_invariance_probe.py` completed
foreground in under ten seconds with exit `0`. No Lean/Lake, heavy build,
external data, external action, claim/canon/verdict movement, or packet transfer
occurred.
