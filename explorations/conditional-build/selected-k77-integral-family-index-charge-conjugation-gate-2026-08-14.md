---
artifact_type: exact_conditional_integral_family_index_result
created: 2026-08-14
status: TEN_DIMENSIONAL_SPIN_FAMILY_IS_CONJUGATE_ODD_IN_INTEGRAL_COMPLEX_K_THEORY__GU_FAMILY_OPERATOR_LINE_DOMAIN_AND_PHYSICAL_DESCENT_UNBUILT
ledger_rows: [RA-G2, LT-SM3, AC-F1, AC-G1a]
canon_verdict_change: none
---

# Selected K77 integral family-index charge-conjugation gate

## Result first

The predecessor's rational identity lifts to integral complex K-theory. Let

```text
pi:Y -> X
```

be a **conditional** proper Riemannian spin family with compact fibres of
dimension `2m`, let `D_v^+` be its chiral vertical spin Dirac family, and let
`L` be a complex line on `Y`. Fibrewise charge conjugation gives an anti-linear
bundle map

```text
C:S^+ tensor L -> S^epsilon tensor L^-1,
epsilon = + for m even, - for m odd,
```

intertwining the chiral Fredholm families. Consequently

```text
Ind(D_v tensor L^-1) = (-1)^m conjugate(Ind(D_v tensor L))
```

in **integral** `K^0(X)`. In ten vertical dimensions `m=5`, so

```text
Ind(D_v tensor L^-1) = -conjugate(Ind(D_v tensor L)).
```

This is torsion-sensitive: it is an identity of analytic index classes, not
an inference from rational Chern characters. It removes the integral-lift
ambiguity in the conditional theorem.

It does not construct the conditional objects. GU still owns no proper 10D
spin fibration, vertical Dirac family, compact/Fredholm domain, nontrivial
selected line or flux, observation pushforward, BFV quotient, positive
physical cohomology or vacuum. The canonical Spin-induced determinant line
remains trivial. An integral virtual class is not a particle, generation or
luminous/mirror count.

## Analytic proof

For a continuous family of elliptic chiral Dirac operators, the analytic
index is the stable virtual kernel/cokernel class

```text
Ind(D_L^+) = [ker D_L^+] - [coker D_L^+]
            = [ker D_L^+] - [ker D_L^-]
```

in `K^0(X)`. This notation is understood after the usual finite-dimensional
stabilization when kernel dimensions jump.

Complex conjugation of the line sends `L` to `bar(L)=L^-1`. For the complex
half-spin representations of `Spin(2m)`, conjugation preserves half-spin
chirality when `m` is even and exchanges it when `m` is odd. The charge-
conjugation intertwiner commutes with the metric spin connection and carries
the twisted Dirac family to the conjugate twisted family.

- If `m` is even, conjugated kernel and cokernel keep their order, giving
  `Ind(L^-1)=conjugate(Ind(L))`.
- If `m` is odd, they exchange, giving
  `Ind(L^-1)=-conjugate(Ind(L))`.

The statement is stable under continuous variation over `X`, so it is an
identity of integral family-index classes. Applying the Chern character
recovers the predecessor law

```text
ch_j Ind(L^-1) = (-1)^(m+j) ch_j Ind(L).
```

No rational injectivity argument is used, so torsion is included.

## Layer 0

| Object | Decided here | Not decided |
| --- | --- | --- |
| analytic family index | integral `K^0(X)` parity | existence in GU |
| charge conjugation | half-spin exchange in 10D | physical W/mirror map |
| line conjugate | `bar L = L^-1` | a supplied nontrivial GU line |
| virtual kernel/cokernel | exact sign exchange | particle multiplicity |
| torsion | included in the K-class identity | value of an unbuilt class |
| KO/KR refinement | not claimed | extra real structure on `L` and family |
| Fredholm family | theorem input | source-owned compact/domain realization |
| physical descent | not implied | observation, gauge/BFV and positivity |

The Riemannian compact vertical family is a conditional mathematical object.
It is not silently substituted for the ambient ultrahyperbolic GU operator.

## Broad route-changing lens census

- **Spin representation theory — selected:** chirality exchange decides the
  sign before any characteristic-class expansion.
- **Analytic family theory — selected:** conjugating the Fredholm family sees
  integral torsion that the rational Chern character cannot see.
- **K-theory — exact:** stable kernel/cokernel exchange is an equality in
  complex `K^0`, including nontrivial torsion classes.
- **KO/KR theory — restrained:** an arbitrary complex twist need not carry a
  compatible real structure, so no real refinement is promoted.
- **Characteristic classes — control:** applying `ch` reproduces every degree
  sign in the predecessor theorem.
- **PDE/domain — ownership stop:** compact elliptic vertical fibres and a
  continuous Fredholm family are assumptions, not current GU outputs.
- **Gauge/BFV — ownership stop:** the theorem neither supplies a line/flux nor
  proves survival through observation or gauge reduction.
- **Source criticism — high:** the source supplies a non-chiral total arena,
  not the family pushforward used here.
- **Philosophy of science — strict ceiling:** strengthening a conditional
  theorem does not increase evidence that its antecedent is physically real.

## Controls and hostile boundary

The strongest overclaim is that an integral index makes the route physical.
It does not: integrality closes a mathematical ambiguity inside a conditional
construction and supplies none of its antecedent objects.

The adjacent-dimension controls fire. In 8D and 12D, `m` is even, charge
conjugation preserves chirality and the index is conjugate-even. In 10D and
14D, `m` is odd, it exchanges chirality and the index is conjugate-odd.

The strongest torsion control is a nonzero formal torsion class `t` with
zero rational Chern character. The predecessor proof cannot distinguish `t`
from zero, whereas analytic conjugation transports `t` and reverses its
virtual sign in odd `m`. This is exactly why the new proof is stronger.

The weakest seam is existence and ownership, not integrality. No current
source object realizes the compact proper family or its closed physical
domain. Failure there kills the physical reading without weakening the
integral theorem.

## Progress and next gate

```text
Ledger v0.248 — 82/82 target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue: 84 continuous + >=19 function-valued + 9 discrete forks
Tightness: T4x1 T3x3 T2x1 · scoped quotients: 5
Headline delta: none
```

The integral-lift gate is closed. The next family-index burden begins earlier:
construct the actual proper ten-dimensional spin family, source-owned vertical
operator and Fredholm domain, and a nontrivial line sector that is supplied
rather than chosen. Then test observation and BV/BFV descent. If ownership or
Fredholm closure fails, use the independently action-owned asymmetric-boundary
or domain route. No verdict, residue, datum, quotient, generation count,
canon claim or public posture changes.
