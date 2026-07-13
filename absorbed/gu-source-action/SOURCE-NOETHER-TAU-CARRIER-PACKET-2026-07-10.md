# Source-Noether/Tau Carrier Packet - Anchor-Scale A-Door

Date: 2026-07-10

Status: finite-fiber tau solve found, independent source carrier still blocked.

## Question

Can the projected BV/Koszul-Tate gauge map

```text
A = Pi_ker(Gamma) d_A
```

be derived from a source-level Noether/tau carrier rather than being assumed as
a projector?

## Executable witness

```text
absorbed/gu-source-action/lib/source_noether_tau_carrier.py
absorbed/gu-source-action/tests/test_source_noether_tau_carrier.py
```

Run:

```text
python absorbed/gu-source-action/tests/test_source_noether_tau_carrier.py
```

## Result

At finite fiber, the tau multiplier exists.  It is the KKT/Schur-complement
solution of the constrained minimization problem:

```text
minimize ||A - d_A||^2
subject to Gamma A = 0
```

The equations give:

```text
lambda = (Gamma Gamma^dagger)^-1 Gamma d_A
A = d_A - Gamma^dagger lambda
  = Pi_ker(Gamma) d_A
```

So the source-Noether/tau attempt does derive the same projected gauge map, but
only as the orthogonal projection solution.

## Current executable values

| Quantity | Value |
|---|---:|
| right-inverse residual | `3.7682219008e-15` |
| KKT stationarity residual | `3.5751939605e-15` |
| `||Gamma A||` | `1.5456840580e-14` |
| `||A - Pi_ker(Gamma)d_A||` | `2.2287571677e-15` |
| tangent perturbation Noether residual | `1.3509639743e-14` |
| tangent perturbation norm | `10.9021623019` |
| `rank(Gamma d_A)` | `128` |
| `rank(lambda)` | `128` |
| `rank(A)` | `128` |
| null `rank(Gamma d_A)` for `e0 + e9` | `64` |
| null `rank(lambda)` for `e0 + e9` | `64` |
| null `rank(A)` for `e0 + e9` | `128` |
| free tangent column dimension | `1664` |
| free tangent map dimension | `212992` |
| `||Pi_RS M_D - M_D Pi_RS||` | `58.7215080716` |
| `||Gamma M_D Pi_RS||` | `155.3625069682` |

## Why this is not yet `S_IG`

The Noether equation only fixes the normal component.  If `Z` is any tangent
map with `Gamma Z = 0`, then

```text
Gamma (A + Z) = 0
```

also holds.  The finite-fiber tau solve selects `Z = 0` because it solves a
minimal-distance projection problem.  That is mathematically clean, but it is
still a projector rule unless a GU source action explains why this is the
physical tangent choice.

Plain English:

- The tau multiplier can force the gamma-trace Noether identity.
- The forced map is exactly the projected map from the BV/KT packet.
- Noether alone leaves a huge tangent ambiguity inside `ker Gamma`.
- The null-direction tau caveat remains visible: the null trace has rank `64`.
- The anchor numbers are unchanged.

## Declaration

This is a partial negative:

```text
tau_schur_projector_only_derivative_tau_blocked
```

The next progress point is:

```text
DERIVATIVE-TAU-HOMOMORPHISM
```

That work should supply derivative-level geometric data, such as the actual
`d_aleph`/tau homomorphism or an equivalent source current, that selects the
tangent part without collapsing back to the fixed orthogonal projector.

External lens added after this packet:
`KLEIN-BOTTLE-COSMOLOGY-TOPOLOGICAL-WALL-LENS-2026-07-10.md`.  It suggests a
topology-forced wall/order-parameter mechanism as an analogy for tangent
selection only; it is not GU evidence and imports no claims.

Update after `TOPOLOGICAL-WALL-TAU-SELECTOR-PACKET-2026-07-10.md`: the wall lens produces nonzero tangent
selectors, but the family is underdetermined. The remaining missing object is a concrete global
boundary-condition/source-current datum that selects one wall/tangent map.
