---
title: "B5 observer-symbol multiplicity matrix: the complexified 20-slot class closes, native real/Krein data remain open"
status: active_research
doc_type: result
created: 2026-07-24
run_id: GUH-20260725T041401Z-b5-observer-symbol-matrix
lane_id: "1"
work_item: B5-INDEPENDENT-RECONSTRUCTION
code: tests/shiab_b5_observer_symbol_multiplicity_matrix.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# B5 observer-symbol multiplicity matrix

## Result

`B5-COMPLEX-OBSERVER-SYMBOL-MATRIX-COMPLETE`.

The frozen independent-B5 carrier ledger now has a complete complexified
observer-subgroup principal-symbol census:

- 20 explicitly labeled irreducible carrier slots;
- total complex carrier dimension 1920;
- all three `S`, `im Gamma`, and `ker Gamma` provenance copies expanded;
- all eight irreducible summands of the 1536-dimensional extra block `X`
  retained;
- 136 nonzero ordered one-dimensional intertwiner cells;
- 68 transpose pairs from vector self-duality; and
- 68 two-cell mirror-support orbits, with no fixed labeled basis cell.

This is a real closure of Step 0b, but it is not yet the stronger
`B5-SYMBOL-CLASS-COMPLETE` outcome. The current source surfaces do not freeze
the phase-normalized native real/Krein adjoint on every observer summand or
the operator domains and boundary form. Those are now the first residual,
rather than an uncomputed representation matrix.

No differential was selected, no favorable lower-order term was imported,
and no symbol exactness or BV cohomology was claimed.

## Construction fork

The computation uses the program-native observer restriction

```text
H_C = Spin(4,C) x Spin(10,C)
```

of the actual `(9,5)`/Rarita-Schwinger carrier. It does not use the full
`Spin(14,C)` carrier as if observation had not occurred, and it does not
replace GU's Krein arena by a conventional positive-Hilbert physical quotient.

Write the two `Spin(4)` Weyl factors as `L=(2,1)` and `R=(1,2)`, and the two
`Spin(10)` Weyl modules as `F+ = 16` and `F- = 16bar`. Then

```text
E+ = (L x F+) + (R x F-)
E- = (L x F-) + (R x F+).
```

The symbol covector branches as

```text
V_14 = (2,2,1) + (1,1,10).
```

The first summand changes both `Spin(4)` spins through the exact
`2 tensor d = (d+1) + (d-1)` Clebsch-Gordan rule. The second leaves the
`Spin(4)` type fixed and uses exact D5 Racah-Speiser decomposition.

## Exact carrier expansion

The complex D5 identities used by the computation are

```text
10 tensor 16+  = 144+ + 16-
10 tensor 16-  = 144- + 16+
```

and the exact decompositions of `10 tensor 144+/-`, including their
dimension closures. The Rarita-Schwinger remainder therefore expands into:

| slot type | dimension | mirror |
|---|---:|---|
| `(3,2,16+)` | 96 | `(3,2,16-)` |
| `(2,3,16-)` | 96 | `(2,3,16+)` |
| `(2,1,144+)` | 288 | `(2,1,144-)` |
| `(1,2,144-)` | 288 | `(1,2,144+)` |
| `(3,2,16-)` | 96 | `(3,2,16+)` |
| `(2,3,16+)` | 96 | `(2,3,16-)` |
| `(2,1,144-)` | 288 | `(2,1,144+)` |
| `(1,2,144+)` | 288 | `(1,2,144-)` |

These eight slots sum to `1536`. The twelve labeled `E+/-` irreducibles
from the three provenance copies sum to `384`, so the complete ledger is
`1536 + 384 = 1920`, agreeing with

```text
S + im Gamma + ker Gamma = 128 + 128 + 1664.
```

Omitting `X` or identifying the three provenance copies before enumeration
fails this dimension ledger.

## Irreducible-type matrix

Use the abbreviated order

```text
Lp Rm Lm Rp X32p X23m X2Tp X1Tm X32m X23p X2Tm X1Tp
```

where, for example, `Lp=(2,1,16+)`, `Rm=(1,2,16-)`,
`X32p=(3,2,16+)`, and `X2Tp=(2,1,144+)`. The exact type matrix is:

```text
        Lp Rm Lm Rp X32p X23m X2Tp X1Tm X32m X23p X2Tm X1Tp
Lp       0  0  1  1    1    0    1    0    0    0    0    0
Rm       0  0  1  1    0    1    0    1    0    0    0    0
Lm       1  1  0  0    0    0    0    0    1    0    1    0
Rp       1  1  0  0    0    0    0    0    0    1    0    1
X32p     1  0  0  0    0    0    0    0    1    1    0    0
X23m     0  1  0  0    0    0    0    0    1    1    0    0
X2Tp     1  0  0  0    0    0    0    0    0    0    1    1
X1Tm     0  1  0  0    0    0    0    0    0    0    1    1
X32m     0  0  1  0    1    1    0    0    0    0    0    0
X23p     0  0  0  1    1    1    0    0    0    0    0    0
X2Tm     0  0  1  0    0    0    1    1    0    0    0    0
X1Tp     0  0  0  1    0    0    1    1    0    0    0    0
```

Every nonzero entry is exactly one. Pulling this matrix back to the three
separately labeled provenance copies gives the full 20-by-20 matrix and its
136 ordered basis cells. Thus the provenance coefficients are not a scalar
chosen by symmetry: every allowed source/target provenance pair is an
independent coefficient slot until a later native action or adjoint condition
relates it.

## Mirror classification

The explicit normal-chirality coflip used at support grade is

```text
Lp <-> Lm
Rm <-> Rp
X32p <-> X32m
X23m <-> X23p
X2Tp <-> X2Tm
X1Tm <-> X1Tp,
```

preserving the `S`, `im Gamma`, or `ker Gamma` provenance label.

It preserves the entire matrix. No labeled basis cell is fixed; all 136 cells
form 68 two-cell support orbits. For a phase-free linear coflip, each orbit
has one symmetric and one antisymmetric combination. If the physical mirror
is antilinear, the same orbit census instead supplies the conjugacy pairs for
the real fixed space.

What is not yet justified is the phase and adjoint data needed to call those
support combinations native `J`-even or `J`-breaking operator symbols. Current
GU truth says each Lorentzian Hodge half is Krein-null and exchanged by the
fundamental structure; it does not supply the normalized invariant pairing,
coflip phase, Green boundary form, and common operator domain on every one of
the 20 slots. Declaring those from convenience would silently replace the
program-native fork.

## Hostile controls

The executable certificate fails if:

1. `X` is omitted;
2. the three provenance copies are collapsed;
3. the mixed super-IG bracket `beta` is mistyped as a carrier or principal
   symbol;
4. a D5 tensor decomposition fails exact dimension closure;
5. vector self-duality fails matrix symmetry;
6. mirror exchange fails matrix invariance; or
7. any mirror orbit is lost or spuriously fixed.

The certificate contains no lower-order term and therefore cannot repair a
failed symbol by postselection.

## Operational outcome

`CONDITIONAL`.

What changed: the full complexified `m_ij` matrix and its provenance-expanded
mirror-support census are closed.

What did not change: the B5 construction, source-action grade, native/unique
ceiling, claim status, canon, verdict, paper state, and public posture.

First residual:

```text
B5-NATIVE-REAL-KREIN-ADJOINT-FREEZE
```

Freeze the native invariant sesquilinear pairing, coflip phase/antilinearity,
formal-adjoint sign, Green boundary form, and common domain on every irreducible
slot. Then reduce the 136-cell complex class to the admissible real/Krein
coefficient space and send its genuine `J`-even and `J`-breaking classes to
the predeclared mirror and symbol-exactness gates.

This is a within-item continuation, not a durable priority change.
