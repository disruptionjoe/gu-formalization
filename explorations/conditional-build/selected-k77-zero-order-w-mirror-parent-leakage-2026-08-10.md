---
title: "Selected K77 zero-order W/mirror parent-leakage discriminator"
status: conditional_exact_result
date: 2026-08-10
run_id: RUN-20260810-071020-gu-k77-zero-order-w-mirror-parent-leakage
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 zero-order W/mirror parent-leakage discriminator

## Outcome

The already-built draft-9.16 q-repaired zero-order family does **not** preserve
the proposed 192-dimensional `W` carrier. More strongly, it does not preserve
the 384-dimensional closure obtained by adding the exact ASD mirror. This is an
exact, scoped obstruction for three admitted parent witnesses; it is not a
failure of every possible lower-order operator or every action-selected orbit.

The family is

\[
 Z_{\alpha,\beta}(A)=\alpha\,\gamma(q)A+\beta\,A\gamma(q).
\]

For a moving-Spin grade-2 witness, a non-Spin grade-6 witness that preserves the
two `U(32,32)` halves, and a grade-1 full-`U(64,64)` coset witness, the two
coefficient maps responsible for `W -> mirror` leakage have exact rank two.
The maps responsible for leakage outside `W plus mirror` also have rank two.
Therefore only `alpha=beta=0` eliminates either leakage class for any one of
those witnesses.

This explicitly keeps the user's parent distinction: source-full
`U(64,64)`, two `U(32,32)` halves, and moving Spin are rival ablations, not one
group. They are also not silently identified with the quaternionic physical
gauge group.

## Layer 0

Five objects must remain separate:

1. the source's four-field sixteen-cell draft matrix;
2. the previously built one-projective-parameter q-repaired middle family;
3. invariance of a representation subspace;
4. closure of `W plus mirror`;
5. physical K-definite BV/domain cohomology.

The probe establishes only (3) and (4) for the family in (2) and the stated
witnesses. It does not construct or exclude (5), and it does not certify the
whole source matrix in (1) as a global operator.

## Exact construction and controls

All matrices use the labelled K77 real Clifford carrier. The Lorentz
self-dual/anti-self-dual projectors are assembled over exact Gaussian
rationals inside that fixed real form; complexification is not used to decide
a signature fork.

- `W` and its ASD mirror are disjoint exact rank-192 idempotents.
- Their sum is an exact rank-384 idempotent.
- Each of the three parent witnesses is B-skew.
- The Spin and two-half witnesses commute with ambient `J`; the full-parent
  coset witness anticommutes with `J`.
- Seven projective ratios, including generic planted controls, were checked
  over `GF(1000033)`.
- The decisive ranks were independently reproduced over `Q(i)`.

At the minimal-leakage ratios the exact characteristic-zero fingerprint is the
same for all three witnesses:

| parent witness | preferred ratio | internal `W` rank | `W -> mirror` rank | outside-pair rank |
|---|---:|---:|---:|---:|
| moving Spin, grade 2 | `alpha=beta` | 0 | 64 | 64 |
| two-half, grade 6 | `alpha=beta` | 0 | 64 | 64 |
| source-full coset, grade 1 | `alpha=-beta` | 0 | 64 | 64 |

The mirror has the identical table. Generic ratios raise the leakage ranks,
so the minimum is informative rather than a dimension-only tautology. But it
still does not close either proposed carrier.

## What this kills—and what it does not

If a proposed connection parent ranges freely over its stated algebra, one
admitted leaking direction is enough to kill invariance under that parent.
Accordingly, the existing q-repaired family cannot by itself make `W` (or
`W plus mirror`) an invariant carrier under unrestricted moving Spin, the two
halves, or source-full `U(64,64)`.

It does **not** kill:

- a source/action-derived connection orbit that excludes the leaking
  directions;
- an independent up/over adapter different from this q-repair;
- the complete four-field source operator;
- a BV differential whose cohomology removes leakage;
- a global domain or boundary condition selecting a K-definite physical
  sector.

No physical quotient, cohomology, spectrum, index, particle, generation,
count, or external datum is claimed.

## Source return

- `SOURCE-CONFIRMS`: the zero-order connection port, contraction-plus-star
  grammar, southeast-zero branch, and Einstein-Dirac plus Yang-Mills-Higgs
  two-layer architecture.
- `SOURCE-CORRECTS`: Curt's single-layer Higgs/Yukawa placement is not the
  author's full architecture.
- `SOURCE-SILENT`: the q coefficient, connection-orbit restriction, carrier
  selection, BV completion, and domain.

## Constraint surplus and next gate

There is one projective freedom, but each witness supplies a rank-two cross
leakage system and a rank-two outside-pair leakage system. The invariance demand
is therefore over-constrained within this family: only the forbidden zero
operator solves it.

The next gate is no longer “build the zero-order family”; that work already
existed. It is:

> Derive the connection orbit actually owned by the selected action and test
> whether it excludes both leaking parity classes, or construct the BV/domain
> cohomology before imposing any `W` carrier restriction.

Ledger v0.136 records distance/evidence migrations only. Coverage, verdicts,
residue, five scoped quotients, P1/P2/P3, and public posture do not move.

