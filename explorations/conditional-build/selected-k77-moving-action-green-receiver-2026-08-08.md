---
artifact_type: build_result
created: 2026-08-08
status: MOVING_COMPLETE_GERM_ACTION_GREEN_EXACT__SOURCE_NATIVE_NORMAL_JET_OPEN
channels: [BUILD, COMPOSE, SOURCE, VERIFY]
ledger_rows: [LT-GR1, LT-GR2b, LT-GR3, LT-GR5, LT-GR6]
canon_verdict_change: none
---

# Selected K77 moving action-Green receiver

## Result in plain English

The moving observation machinery now transports the action's Euler equations
without dropping a term—but only when observation means the **complete
value-plus-first-jet germ**, not ordinary four-dimensional pullback.

For the density Euler covector `E`, indefinite lowerer `K`, inverse
primalizer `R=K^{-1}`, complete section-germ map `M`, and moving target map
`Z`, the observed field-like equation is

```text
j = Z M R E.
```

Its derivative has four separately live terms:

```text
delta j = (delta Z) M R E
        + Z (delta M) R E
        - Z M R (delta K) R E
        + Z M R (delta E).                              (1)
```

An exact theorem tensored with all nine directions of the v0.64 noncyclic
action fixture verifies (1). Freezing the target, section, primalizer or Euler
factor fails independently. The degree-fourteen epsilon companion obeys the
corresponding moving inverse-density formula.

The action-density Green identity also closes with nonzero boundary flux. Its
adjoint bulk needs the derivative of the lowerer, the moving section inverse,
and the Euler image. Freezing either geometric factor fails.

This is real progress but not yet the physical four-dimensional equation.
Ordinary pullback still has the established rank-ten K77 conormal kernel. The
lossless complete germ carries dependent normal-jet equation data, and the
selected action's source-native normal first Euler jet has not yet been
computed. That jet is now the sharp remaining construction before the Green
potential can be honestly antisymmetrized.

## 1. Layer 0

| phrase | object here | kept distinct |
| --- | --- | --- |
| Euler owner | density-valued variational covector | its primalized field-like image |
| complete observation germ | value, tangential jet and dependent normal jet | ordinary section pullback |
| equation dual | inverse-transpose transport preserving first variation | a new action field or counterterm |
| Green owner | one preboundary potential with nonzero flux | antisymmetrized presymplectic current |
| lossless transport | invertible germ-level change of variables | physical quotient or global bulk-shell faithfulness |

The distinction matters. Primalize-then-restrict has rank four on the actual
`4+10` graph section and loses the ten conormal directions. Retaining the full
germ is lossless, but those ten components must be supplied by the ambient
Euler operator's normal jet; they are not additional particles and are not an
external datum.

## 2. Source return

The source supports observation by a metric section and corrects the naive
reading that observation is merely direct pullback. It does not print the
normal first jet of the selected action Euler operator or the complete moving
equation-dual Green formula.

```text
SOURCE-CORRECTS:
  observation is richer than naive direct pullback.

REPO-DERIVES:
  the universal moving complete-germ equation-dual and Green identities.

SOURCE-SILENT:
  the coefficientwise source-native normal Euler jet needed by the selected
  action on the admitted K77 section.
```

## 3. Exact certificate

The certificate composes three already verified ingredients rather than
rebuilding them: the v0.64 action companion, the K77 moving indefinite
primalizer, and complete observation-germ duality. Its new calculation uses a
nontrivial `2+3` graph germ and tensors the universal form identity with all
nine exact action-coefficient directions.

- the indefinite lowerer is invertible but not positive definite;
- `delta R=-R(delta K)R` holds exactly;
- observed lowerer and primalizer are mutual inverses;
- the complete equation dual preserves the first variation;
- the full tensor receiver has rank `45`;
- all four terms in (1) are nonzero and forced;
- the degree-fourteen inverse-density response is forced;
- the moving Green identity has nonzero flux;
- frozen-lowerer and frozen-section Green plants fail;
- tangential pullback retains the exact conormal kernel.

Independent Sage and python-flint checks reproduce rank `5`, determinant
`2772`, and the moving inverse identity on the rational indefinite lowerer.

Main probe: `42/42 PASS`, including the immutable v0.64 chain replay.

## 4. Symplectic review

The Green boundary owner is a field-space one-form. Antisymmetrizing it before
the source-native normal jet exists would silently choose an ambient extension
of the action Euler operator. That would manufacture the missing object in the
composition layer. The correct order is:

1. compute the selected action's normal first Euler jet;
2. insert it into the complete-germ receiver;
3. antisymmetrize the resulting action-owned Green potential;
4. test basicness, polarization and common-domain descent.

No BFV class, charge or physical phase space is claimed here.

## 5. Seven-axis disposition

- **Layer 0:** density/primalized equations, complete germ/direct pullback, and
  Green/presymplectic/BFV objects are separated.
- **L1 syntactic:** source pullback language and the repository correction are
  located.
- **L2 type:** degree `13<->1` and `14<->0` primalizers and inverse-transpose
  equation transport close.
- **L3 algebraic:** the universal moving derivative and Green identities pass
  exactly with firing omissions.
- **L4 geometric:** complete local germ transport is exact; the actual
  source-native normal Euler jet is open.
- **L5 variational:** first variation and Green potential are exact;
  antisymmetrized second variation is open.
- **L6 analytic:** no common closed, hyperbolic or Krein-self-adjoint domain is
  inferred.
- **L7 physical:** no Einstein, Standard Model, spectrum or cosmology claim.

## 6. Ledger v0.65

```text
Ledger v0.65 — 82/82 active target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped

headline_delta: none
frontier_conditions_closed: 4
frontier_conditions_opened: 1
remaining_named_conditions: 2
```

Five rows migrate in distance, evidence and mapping grade only. P1/P2/P3,
verdicts, residue, quotients, canon and public posture stay frozen.

Next:

`SOURCE_NATIVE_NORMAL_JET_OF_ACTION_EULER__THEN_ANTISYMMETRIZE_COMPLETE_GREEN_POTENTIAL`.
