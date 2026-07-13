# Global Boundary-Condition Tau Data Packet

Date: 2026-07-13

Status: source-current / derivative data still missing; wall selection remains externally keyed.

## Question

The previous wall/tau packet found nine nonzero tangent selectors:

```text
Z_k : S -> ker Gamma
```

Can current GU-native boundary/tau data force one of them, rather than choosing a wall by an external rule?

## Executable Witness

```text
absorbed/gu-source-action/lib/global_boundary_condition_tau_data.py
absorbed/gu-source-action/tests/test_global_boundary_condition_tau_data.py
```

Run:

```text
python absorbed/gu-source-action/tests/test_global_boundary_condition_tau_data.py
```

## Result

The available finite-fiber wall summaries do not contain a source-action rule that selects one wall. Simple
local scalar summaries are rule-choice dependent:

| Local rule | Selected wall |
|---|---:|
| minimum selector norm | `4` |
| maximum selector norm | `3` |
| minimum projection-dependency norm | `4` |
| maximum raw wall Noether residual | `3` |
| first spacelike wall by bookkeeping order | `0` |

An externally supplied boundary/source current can pick a wall, but only because that current is supplied:

```text
current_2 != 0  ->  wall 2
```

The source action has not declared such a current, boundary condition, derivative tau homomorphism, or
`d_aleph` datum. Therefore the selection remains externally keyed, not GU-forced.

## Current Executable Values

| Quantity | Value |
|---|---:|
| admissible spacelike wall selectors | `9` |
| distinct wall selectors | `9` |
| local scalar-selected wall components | `{0, 3, 4}` |
| externally supplied current can select | `true` |
| boundary current declared by source action | `false` |
| source-forced unique selector | `false` |
| `||Pi_RS M_D - M_D Pi_RS||` | `58.7215080716` |
| `||Gamma M_D Pi_RS||` | `155.3625069682` |

## Interpretation

This is a bounded negative:

- The wall family is productive because it creates nonzero tangent maps.
- Local scalar ranking does not constitute a source action.
- A current-weighted choice is admissible only if an actual source current or global boundary condition is
  supplied by GU data.
- No wall is selected as physical in this packet.

## Declaration

```text
externally_keyed_wall_selection_blocked
```

The next progress point is:

```text
SOURCE-CURRENT-DERIVATIVE-DATA
```

That work should supply actual derivative-level source-current data, such as `d_aleph` or an equivalent
boundary condition, that selects a tangent map without target numerology, fitted holonomy, local scalar
ranking, or a fixed projector absorber.
