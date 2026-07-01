---
title: "Compensator Adapter Goal"
date: 2026-06-30
status: complete
claim_grade: bounded_negative
claim_promotion: false
depends_on:
  - EXTERNAL-ADAPTER-STEELMAN-2026-06-27.md
  - ADAPTER-DISCRIMINATOR-GOAL-2026-06-30.md
  - lib/compensator_adapter.py
  - tests/test_compensator_adapter.py
---

# Compensator Adapter Goal

## Goal

Test the steelman version where the missing source action is not an ordinary
metric connection and not arbitrary noise, but a compensating adapter attached
to the actual RS escape block:

```text
E = (I - Pi_RS) M_D Pi_RS
```

The question is:

```text
Can a forced sigma_c shape touch the source-action wall, change the
boundary/index discriminator, and still avoid simply decoupling the RS escape
channel?
```

## Method

The candidates are built only from the verified bridge objects already used by
the repo:

```text
Pi_RS, Q = I - Pi_RS, M_D, E = Q M_D Pi_RS
```

For each candidate `sigma_c`, the test computes:

```text
M_eff = M_D + sigma_c
escape_after = || Q M_eff Pi_RS ||
escape_ratio = escape_after / || Q M_D Pi_RS ||
index signal = sig(Hermitian(G-diagonal(i sigma_c)))
```

The guard is intentionally strict. If a candidate wins by making
`escape_ratio` vanish, it is a decoupling trap, not a source action.

## Candidate Shapes

| candidate | shape | purpose |
|---|---|---|
| `full_escape_cancellation` | `-E - E^dag` | cancellation trap control |
| `half_escape_damping` | `-0.5(E + E^dag)` | partial compensator |
| `quarter_escape_damping` | `-0.25(E + E^dag)` | weak partial compensator |
| `antihermitian_escape_twist` | `i(E - E^dag)` | phase/twist adapter |
| `imaginary_escape_completion` | `i(E + E^dag)` | imaginary completion adapter |

## Results

Run:

```powershell
python -m unittest tests.test_compensator_adapter -v
```

Concrete discriminator table:

| candidate | `sig_delta` | `escape_ratio` | `total_commutator_norm` | status |
|---|---:|---:|---:|---|
| `full_escape_cancellation` | 0 | `7.601e-16` | `37.4411` | `clean_decoupling_trap` |
| `half_escape_damping` | 0 | `5.000e-01` | `39.5344` | `damps_escape_without_index_signal` |
| `quarter_escape_damping` | 0 | `7.500e-01` | `47.8548` | `damps_escape_without_index_signal` |
| `antihermitian_escape_twist` | 0 | `1.414e+00` | `83.0448` | `escape_twist_without_index_signal` |
| `imaginary_escape_completion` | 0 | `1.414e+00` | `83.0448` | `escape_twist_without_index_signal` |

Aggregate verdict:

```text
only_decoupling_or_zero_index_compensators
```

## Plain-English Reading

This pass asks a more geometric question than the first adapter discriminator.
Instead of asking whether a generic non-metric candidate can move the index, it
asks whether the missing object can be shaped like an adapter on the exact
escape channel where the GU wall appears.

The expected failure modes are informative:

- Full cancellation is too easy. It protects the system by shutting off the
  bridge, but that destroys the mechanism we are trying to explain.
- Partial damping may be geometrically meaningful only if it also creates an
  index/source signal. If it only changes a norm, it is bookkeeping, not a
  source action.
- Pure phase/twist shapes are attractive because they preserve the channel
  size, but they still need to create a boundary/index signal or supply a
  carrier law.

## Verdict

This goal does not find a live compensator adapter.

The strongest version of the compensator steelman says: maybe the missing
source object is not a generic non-metric perturbation, but a very specific
shape that attaches to the escape block itself. This test grants that premise
and builds every first-pass shape from `E` and `E^dag`.

The result is negative but useful:

```text
full cancellation protects by deleting the bridge;
partial damping changes only the escape norm;
phase/twist completions preserve or enlarge the escape channel;
none produces a boundary/index signal.
```

So the obvious adapter shapes are not enough. A better candidate must add a
new carrier datum beyond `E` itself: for example a spectral-section choice, a
BV/BRST boundary field, a K-theory class, or a source-current law. Without that
extra datum, the geometry only gives cancellation, damping, or twisting of the
known escape block.

## Not Claimed

This goal does not claim:

- a compensator exists;
- the source action has been derived;
- an external universe adapter has been found;
- cancellation of the RS escape block is a valid solution.
