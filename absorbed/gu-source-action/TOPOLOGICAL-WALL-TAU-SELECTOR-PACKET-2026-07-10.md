# Topological-Wall Tau Selector Packet

Date: 2026-07-10

Status: nonzero wall selectors found, but not forced uniquely by current GU data.

## Question

Can a topology/wall-like global datum force a nonzero tangent selector

```text
Z : S -> ker Gamma
```

so the A-door gauge map becomes

```text
A = Pi_ker(Gamma)d_A + Z
```

without collapsing back to a fixed projector or arbitrary tangent choice?

## Executable Witness

```text
absorbed/gu-source-action/lib/topological_wall_tau_selector.py
absorbed/gu-source-action/tests/test_topological_wall_tau_selector.py
```

Run:

```text
python absorbed/gu-source-action/tests/test_topological_wall_tau_selector.py
```

## Model

This is an analogy-driven GU-native finite-fiber probe.  Inspired by the
topology-forced wall/order-parameter pattern recorded in
`KLEIN-BOTTLE-COSMOLOGY-TOPOLOGICAL-WALL-LENS-2026-07-10.md`, the code tests
spacelike reflection wall involutions on the existing Cl(9,5) vector-spinor
carrier.

For each spacelike component `k = 0..8`, it forms a wall-transformed gauge map,
takes the wall difference, and projects the difference into `ker Gamma`:

```text
Z_k = Pi_ker(Gamma) (Wall_k d_A Wall_k^-1 - d_A)
```

Then it asks whether these `Z_k` are nonzero, Noether-compatible, H-linear,
Krein-compatible, anchor-preserving, and uniquely forced.

## Result

The wall lens can make nonzero tangent selectors:

```text
Gamma Z_k = 0
rank(Z_k) = 128
Z_k != 0
```

for all nine spacelike wall involutions tested.  They also preserve the anchor
numbers:

```text
||Pi_RS M_D - M_D Pi_RS|| = 58.7215080716
||Gamma M_D Pi_RS|| = 155.3625069682
```

Current executable values:

| Quantity | Value |
|---|---:|
| admissible spacelike wall selectors | `9` |
| distinct wall selectors | `9` |
| min pairwise selector distance | `18.7567892470` |
| max pairwise selector distance | `109.0216230191` |
| max `||Gamma Z_k||` | `2.0097183471e-14` |
| max H-linear defect | `5.7964847372e-12` |
| max Krein wall residual | `0.0` |
| min projection dependency norm | `3.0237157841` |
| min selector norm | `10.9021623019` |
| max selector norm | `87.2172984153` |

But the family is underdetermined.  All nine spacelike wall choices are
admissible and distinct.  The current repo does not supply a GU-native global
boundary condition that selects one of them.

Also, the raw wall differences are not themselves Noether-compatible.  Each
candidate still needs projection repair:

```text
Gamma(Wall_k d_A Wall_k^-1 - d_A) != 0
Z_k = Pi_ker(Gamma)(...)
```

So this is not yet an independent source-action carrier.

## Interpretation

Plain English:

- The topology-wall analogy is productive: it creates nonzero tangent maps that
  finite-fiber Noether left invisible.
- Those tangent maps can satisfy the same algebraic gates as the previous
  projected BV/KT closure.
- But the wall choice is still external to the current GU data.
- Without an actual boundary/topology condition, the construction is an
  underdetermined family, not a forced source action.

## Declaration

This is a partial negative:

```text
nonzero_wall_selectors_underdetermined
```

The next progress point is:

```text
GLOBAL-BOUNDARY-CONDITION-TAU-DATA
```

That work should stop varying wall involutions and instead specify a concrete
global boundary condition, source current, or derivative-level `d_aleph` datum
that selects one tangent map without using target numerology, fitted holonomy,
or a fixed projector absorber.
