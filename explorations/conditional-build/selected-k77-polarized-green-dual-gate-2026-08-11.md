---
artifact_type: construction_result_and_scope_narrowing
created: 2026-08-11
ledger_version: "0.171"
result: DIRECT_DUAL_KERNEL_HAS_RANK128_GREEN_RADICALS__PERFECT_DUAL_QUOTIENT_IS_UNOWNED_AND_NAIVE_OBSERVATION_DOES_NOT_DESCEND__V0170_SURVIVES_ONE_SIDED_ONLY
grade: "exact rational fixed-normal real-Cl(7,7) principal Green theorem on the actual dimension-1920 four-field symbol; full moving boson-fermion preboundary form and analytic/BFV domain open"
canon_verdict_change: none
---

# Selected K77 polarized Green-dual gate

## Plain-English result

The v0.170 restriction still works as one-sided evolution data, but it is not
yet a complete action domain.

The source action treats the barred and unbarred fermions as independent. For
the actual normal Green coefficient `A=D_t`, the exact dual of
`N(k) psi_hat(k)=0` is fixed uniquely by

```text
Nsharp = A^(-T) N^T A^T,
(Nsharp)^T A = A N.
```

Putting both independent fields in the natural kernels does not give a
nondegenerate Green pairing. Both sides have exact radical dimension `128`.
The algebraic perfect dual of `ker N` is instead

```text
Vbar / im Nsharp,
```

which has dimension `1792`. But the action has not produced that quotient as
a gauge or BV reduction, and the ordinary observation map is nonzero on all
`128` quotient directions. It therefore does **not** descend. For the purely
observed spatial-frequency sample, the unquotiented dual kernel itself retains
only rank `512` of the rank-`640` naive barred observation; the two mixed
center samples retain `640`.

This is a scoped adverse result for the direct action-domain promotion. It is
not a retraction of the one-sided strict-center evolution ingredient.

## Layer 0

| phrase | exact object | distinct object still open |
| --- | --- | --- |
| one-sided polarization | `ker N(k)` on the unbarred evolution field | nondegenerate domain for the independent action pair |
| Green-adjoint polarization | unique `Nsharp` satisfying `(Nsharp)^T A=A N` | source-selected reality, boundary condition or BV differential |
| dual-kernel domain | `ker Nsharp x ker N` | perfect Green dual; it has rank-128 radicals |
| perfect algebraic dual | `Vbar/im Nsharp` paired with `ker N` | source/action-owned gauge or BV quotient |
| observation descent | a map constant on quotient classes | dimension preservation or nonzero observation before quotient |
| fixed-normal theorem | actual `D_t` principal fermion Green block | full moving boson-fermion preboundary current and analytic domain |

## Exact theorem

On all three admitted strict-center samples:

- `rank N = rank Nsharp = 128`;
- `N^2=(Nsharp)^2=0`;
- both kernel dimensions are `1792`;
- `im Nsharp` is exactly the left annihilator of `ker N` under
  `B(bar,psi)=bar^T A psi`;
- `im N` is the corresponding right radical;
- quotienting the barred carrier by `im Nsharp` gives the perfect algebraic
  dual of `ker N`; and
- the naive barred observation has rank `128` on `im Nsharp`, so it cannot
  descend to that quotient.

The last point matters more than the quotient dimension. The quotient does
not merely remove invisible redundancy; it identifies directions carried by
the observation map.

## Prior-art composition

This is not a wholly new quotient obstruction.

1. B2B/B2C1 already showed that removing the old Jordan defect by a fixed
   quotient can erase the observation carrier.
2. v0.165 built the independent-dual Green comparator and kept a physical
   analytic domain open.
3. v0.167 typed `A` as the actual four-field normal principal symbol.
4. v0.170 built the frequency-dependent `ker N` one-sided restriction while
   explicitly leaving Green compatibility open.

The relative increment is the exact Green-adjoint composition for the current
frequency-dependent polarization: its direct dual-kernel radical, the unique
perfect algebraic dual quotient, and the failure of the present observation
map to descend.

## What survives and what does not

Survives:

- strict-center plus `ker N` removes generalized chains for the unbarred flat
  principal evolution;
- the unbarred restriction retains rank-`640` observation; and
- a full action-derived coisotropic/BFV completion or an operator-changing
  semisimple completion remains logically open.

Does not survive:

- calling the same kernel restriction on barred and unbarred fields a
  nondegenerate selected-action domain;
- promoting `Vbar/im Nsharp` as gauge or BV by algebra alone; or
- using the current naive observation after that quotient.

## Progress meter

```text
Ledger v0.171 — 82/82 target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue: 84 continuous + >=19 function-valued + 9 discrete forks
Tightness: T4x1 T3x3 T2x1 · scoped quotients: 5
Frontier: 1 condition closed · 2 opened · 6 named conditions remain
```

The next gate is a composition, not an invented quotient: compare
`im Nsharp` with the already action-owned small-gauge characteristic image and
boundary moment map, then assemble the full moving boson-fermion preboundary
form. Only an owned coisotropic/BFV identification or a modified observation
can revive the restriction route as an action domain. If neither appears,
prioritize the separate source-admitted wedge-Shiab/nonzero-southeast operator
completion.

Main probe:
`tests/channel-swings/selected_k77_polarized_green_dual_gate_probe.py`.

## Session manifest

| artifact | verify status | owed work |
| --- | --- | --- |
| exact Sage probe | `CONFIRMED` | compose radical with owned gauge/BFV images |
| construction result and v0.171 row migrations | `SCOPED` | full moving preboundary and analytic domain |
| hostile review | `CONFIRMED` | none at current scope |
| source return | `CONFIRMED` | source remains silent on the missing quotient/domain |
| process audit and current pointers | `CONFIRMED` | daily steward may absorb priority signal |

No canon proposal is emitted. The result changes neither verdict nor public
posture.
