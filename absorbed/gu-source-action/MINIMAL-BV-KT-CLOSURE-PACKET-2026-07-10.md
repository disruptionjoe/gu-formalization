# Minimal BV/Koszul-Tate Closure Packet - Anchor-Scale A-Door

Date: 2026-07-10

Status: finite-fiber closure witness, not a source-action proof.

## Question

Can the anchor-scale A-door be extended into a minimal BV/Koszul-Tate complex
without moving the bare commutator anchor?

## Executable witness

The executable check is:

```text
absorbed/gu-source-action/lib/minimal_bv_kt_closure.py
absorbed/gu-source-action/tests/test_minimal_bv_kt_closure.py
```

It uses the existing Clifford/gamma-trace carrier from `tests/gu_bridge.py`.

## Result

The finite-fiber bicomplex closes after the scalar-spinor gauge map is
projected into the gamma-traceless vector-spinor carrier:

```text
A = Pi_ker(Gamma) d_A
Gamma A = 0
(Gamma^dagger Gamma) A = 0
A^dagger (Gamma^dagger Gamma) = 0
```

That is the minimal Koszul-Tate closure witness.  It says the A-door is not
immediately killed by the algebraic BV/KT check.

Current executable values:

| Quantity | Value |
|---|---:|
| `||Gamma d_A||` | `80.6136464874` |
| `rank(Gamma d_A)` | `128` |
| `||Gamma Pi_ker(Gamma) d_A||` | `1.5788214595e-14` |
| `rank(Pi_ker(Gamma) d_A)` | `128` |
| KT cross residual | `5.9074089763e-14` |
| KT exact escape residual | `1.1284109399e-14` |
| `||Pi_RS M_D - M_D Pi_RS||` | `58.7215080716` |
| `||Gamma M_D Pi_RS||` | `155.3625069682` |
| `rank Gamma(e0 + e9)` | `64` |

## What failed before the projection

The raw gauge map is still second-class:

```text
Gamma d_A = c(xi)
rank(Gamma d_A) = 128
```

So the raw differential does not satisfy the Noether identity.  The closure
comes only after selecting the projected map.  That selection is not yet
derived from a source action, a derivative-level tau carrier, or a variational
identity.

## Anchor-scale checks preserved

The closure attempt preserves the existing A-door anchors:

```text
||Pi_RS M_D - M_D Pi_RS|| = 58.7215
||Gamma M_D Pi_RS|| = 155.3625
rank Gamma(e0 + e9) = 64
```

The trace escape is KT-exact at finite fiber, but the C2 wall remains.  This is
useful: the packet separates the local BV/KT algebra question from the global
boundary/index question.

## Interpretation

Plain English:

- The smallest BV/Koszul-Tate complex can be made to square to zero on the
  declared full vector-spinor A-door.
- The raw scalar-spinor shift still fails the Noether identity.
- The projection that repairs it is exactly the thing a real source action must
  explain, not something this packet is allowed to assume as physics.
- The anchor-scale numeric obstructions do not disappear.

## Declaration

This is a partial pass:

```text
finite_fiber_closes_source_noether_blocked
```

The next progress point is:

```text
SOURCE-NOETHER-TAU-CARRIER
```

That work should try to derive the projected differential from the source-level
Noether/Koszul-Tate structure, including the derivative-level tau carrier,
instead of hand-selecting `Pi_ker(Gamma) d_A`.

Update after `SOURCE-NOETHER-TAU-CARRIER-PACKET-2026-07-10.md`: the finite-fiber tau solve derives the
projection as a Schur complement, but still leaves tangent freedom unselected. The remaining missing object
is derivative-level tau/`d_aleph` homomorphism data.
