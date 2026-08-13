---
title: "Selected K77 four-field zero-order port composition"
status: exact_necessary_condition_result
date: 2026-08-10
run_id: RUN-20260810-090656-gu-k77-four-field-zero-order-port
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 four-field zero-order port composition

## Outcome

The complete four-field equation-9.16 grammar revives a route that the
one-form-only v0.136 calculation could not test. Its ordinary
`Omega0(S) -> Omega1(S)` connection cell has exact rank `128`, while the
preferred-ratio leakage from either `W` or its ASD mirror has rank `64` and is
entirely contained in that port image.

The result is not a universal rescue. Exact quotient arithmetic gives one
projective condition per parent class:

| parent ablation | unique port-compatible ratio | W leak | mirror leak |
|---|---|---:|---:|
| moving Spin, grade 2 | `alpha=beta` | `64` inside rank-`128` port | same |
| two `U(32,32)` halves, grade 6 | `alpha=beta` | `64` inside rank-`128` port | same |
| full-`U(64,64)` odd coset, grade 1 | `alpha=-beta` | `64` inside rank-`128` port | same |

Thus the restricted moving-Spin and two-half horns pass the **necessary**
zero-form cancellation gate. The source-full parent still contains incompatible
even and odd parity requirements, so one common coefficient cannot serve it.

## Layer 0

| object | present status |
|---|---|
| one-form invariance | fails by v0.136 |
| zero-form port image inclusion | passes here, parent-specifically |
| graph subspace invariance | open |
| lower-left adjoint compatibility | open |
| BV/constraint cohomology | open |
| closed Krein/Green domain | open |

The important correction is that failure of a diagonal one-form block does
not imply failure of the complete four-field operator. Conversely, image
inclusion does not construct the graph map or make it physical.

## Prior art and source return

The initial proposal to “build the complete four-field operator” was duplicate.
The August 4 trace-`q` wave had already assembled all sixteen equation-9.16
cells and retained the southeast-zero branch. The novel operation here is the
composition of that existing `Omega0 -> Omega1` cell with the exact v0.136
W/mirror leak witnesses.

- `SOURCE-CONFIRMS`: equation 9.16 contains ordinary zero-form-to-one-form
  connection cells in the four-field grammar.
- `SOURCE-SILENT`: no released source supplies a W graph adapter, selects the
  parent, solves the lower-left condition, constructs BV cohomology, or chooses
  a closed domain.

## Exact theorem

Let `a=(2,-1,0,1,0,...,0)` be the already-declared connection one-form fixture.
For an invertible parent coefficient `T`, the ordinary port has image

```text
im(B_T) = span(a) tensor S.
```

The exact quotient is represented without a fitted projector by

```text
Q(y)_r = a_0 y_r - a_r y_0,  r=1,...,13,
```

whose kernel is exactly the port image. Applying `Q` to the two left/right
trace-`q` leakage coefficients gives rank one over both `GF(1000033)` and
`QQ(i)`. Hence each parent has one and only one projective ratio making the
leakage land in the port. Direct ranks then give `rank(leak)=64`,
`rank(port)=rank([port,leak])=128` for W and mirror in all three parent
ablations. Twelve single-slot broken-port plants fail.

Because multiplication by any invertible parent does not change
`span(a) tensor S`, this theorem does **not** select a parent. It tests the form
geometry of the port; the incompatible coefficient ratios preserve the parent
fork.

## Efficient specialist pre-assessment

1. **Layer-0 semantics — ACTUAL MATH, very high.** Test necessary port inclusion
   separately from graph invariance and BV cohomology.
2. **Prior-art archaeology — ACTUAL MATH, very high.** Reuse the August 4
   sixteen-cell assembly rather than reconstruct it.
3. **Differential geometry — ACTUAL MATH, high.** The port is the line
   `span(a)` in the one-form factor, not a carrier selector.
4. **Representation/Clifford theory — ACTUAL MATH, high.** Keep W, mirror and
   the three parent parity classes exact and separate.
5. **Variational bicomplex — ACTUAL MATH, high.** A graph adapter must still
   satisfy the lower-left equation and the Riccati condition.
6. **Symplectic/BV-BFV — ACTUAL MATH, high.** Image cancellation before
   reduction is not physical cohomology.
7. **Operator/Krein analysis — ACTUAL MATH, high.** No closed domain, spectrum
   or positivity follows from finite image ranks.
8. **Adversarial scope — ACTUAL MATH, very high.** The strongest attack is the
   missing graph equation and the incompatible source-full ratio.
9. **Exact-computation architecture — ACTUAL MATH, high.** Replay the immutable
   predecessor and add only the quotient/port calculation.

## What moves

Closed:

> The exact v0.136 leakage already rules out help from the ordinary zero-form
> cells in the complete equation-9.16 grammar.

Opened sharply:

- construct `G:W -> Omega0(S)` and its mirror analogue on the two restricted
  parent horns;
- solve the lower-left adjoint and nonlinear graph/Riccati conditions; and
- separately retain the source-full even/odd coefficient conflict.

Ledger v0.138 moves six distance/evidence fields only. Coverage, verdicts,
residue, five scoped quotients, P1/P2/P3, canon verdicts and public posture do
not move.

## Next gate

Solve or kill the complete W and mirror graph/Riccati plus lower-left adjoint
condition for the moving-Spin and two-half horns. Only a solution then advances
to moving overlap descent and BV/constraint cohomology. Do not spend a global
domain campaign before that algebraic graph gate.
