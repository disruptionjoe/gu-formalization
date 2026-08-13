---
artifact_type: exact_construction_and_composition_result
created: 2026-08-12
status: SOURCE_U3_2_PATI_SALAM_INTERSECTION_CONSTRUCTED__SM16_EXACT__FIXED_Q_RETYPE_POST_HIGGS__RADIAL_VARPI_ACTION_OWNER_OPEN
target_claim: NONE-NOT-A-KILL
ledger: lab/process/conditional-physics-ledger-v0.196.json
canon_verdict_change: none
---

# Selected K77 moving-Hq, U(3,2), SM and Higgs-direction gate

## Result in plain English

The source-guided group chain works at exact finite grade, and it changes the
meaning of the preceding dimension-nine result.

Choose an orthogonal complex structure `J` on the real normal `(6,4)` space.
Its centralizer in `SO(6,4)` is `U(3,2)`.  Intersecting that reduction with
the full Pati-Salam maximal compact gives

```text
Spin(6)xSpin(4) intersect SU(3,2)
  = S(U(3)xU(2))
  ~= SU(3)xSU(2)xU(1),             dimension 12.
```

The central `U(1)` has exact `2:−3` triplet/doublet weights.  Restriction to
the positive-chiral 16 of `Spin(10,C)` gives precisely the Standard-Model
hypercharge multiset, including vanishing linear and cubic anomalies.

The trace direction q sits in the negative complex two-plane.  Before q is
fixed, that plane is a complex weak doublet with hypercharge `−1/2`.  Fixing a
nonzero q breaks the exact 12-dimensional algebra to a nine-dimensional
algebra whose derived part has dimension eight and whose center has dimension
one:

```text
SU(3)xSU(2)xU(1)  ->  SU(3)xU(1).
```

So v0.195's dimension-nine intersection was not evidence that the construction
missed the Standard Model.  It is the expected *post-Higgs* stabilizer, reached
only after the 12-dimensional pre-Higgs group has first been constructed.

This is a real advance but not yet a Higgs construction.  The normalized trace
q contributes only the three angular/orbit directions.  One radial coefficient
multiplying q is still needed to restore the fourth real component of the
complex doublet.  The source assigns Higgs-like functions to the ad-valued
one-form `varpi`, making a radial `varpi` coefficient a typed candidate.  The
action has not selected that coefficient or produced its kinetic term,
potential, Yukawa map, vacuum or mass spectrum.

## Layer 0

| object | role established here | still distinct from |
|---|---|---|
| orthogonal `J` on `(6,4)` | defines one `U(3,2)` reduction | a canonical or action-selected reduction |
| moving `H_q` family | transports as q moves | a fixed-q compatible connection |
| `S(U(3)xU(2))` | exact pre-Higgs SM algebra | its post-Higgs q stabilizer |
| trace q | direction in the negative complex doublet | a dynamical radial scalar |
| scalar coefficient `h` in `h q` | missing radial degree of freedom | a selected `varpi` component |
| source `varpi` cell | correct one-form type for Higgs-like functions | derived kinetic/potential/Yukawa physics |
| full `U(64,64)` | source principal connection parent | two `U(32,32)` halves or `U(3,2)` |

`U(3,2)` and `U(32,32)` are deliberately written with commas and never
abbreviated to the same token.

## Exact group and representation result

On `R^(6,4)`, an explicit orthogonal `J` obeys `J^2=-1`.  Exact linear algebra
gives

```text
dim Z_so(6,4)(J)                         = 25 = dim u(3,2),
dim su(3,2)                              = 24,
dim (so(6)+so(4)) intersect u(3,2)       = 13,
dim (so(6)+so(4)) intersect su(3,2)      = 12.
```

The last algebra is `s(u(3)+u(2))`.  Its unique central generator has plane
weights `(2,2,2,−3,−3)`.  The actual chiral-spin eigenvalues are half signed
sums with even parity; dividing by six gives

```text
0;
(+1/3)x3; (-1/2)x2;
(+1/6)x6; (-2/3)x3; +1,
```

the exact 16-state Standard-Model hypercharge multiset.  This calculation
does not merely copy a known list into the result.

For q in the negative complex two-plane:

```text
dim Orbit_U(3,2)(q)                      = 9,
Stab_U(3,2)(q)                           = U(3,1), dim 16,
dim Stab_S(U(3)xU(2))(q)                 = 9,
dim [stab,stab]                          = 8,
dim center(stab)                         = 1.
```

The compact orbit is three-dimensional.  Orbit plus a radial scalar has four
real dimensions and the correct `Y=-1/2` doublet charge.

## What remains conditional

The orthogonal-complex-structure family is a 20-dimensional family,
`45−25=20`.  The source calls for the complex reduction, but neither this
gate nor prior action work selects a particular `J`.  This is an existing
selection burden, not a newly booked datum.

Likewise, the geometry owns q but not a freely varying amplitude.  The next
construction must locate an actual scalar coefficient in the full
`U(64,64)` connection or possible two `U(32,32)` halves, prove that its
observation descent is a color-singlet weak doublet, and derive rather than
insert:

1. covariant kinetic energy;
2. a viable symmetry-breaking potential and stationary nonzero amplitude;
3. Yukawa/minimal-coupling placement on the correct fermion blocks;
4. compatibility with moving `H_q`, the selected source action and its
   presymplectic/BV equations.

No positive energy, closed domain, BV quotient, index, count or cosmological
claim follows from the finite result.  P1/P2/P3 are unused.  No verdict,
residue, quotient, canon or public posture changes.

## Adaptive and hostile review

- **Group/representation — actual math, very high:** exact centralizers,
  intersections, derived/center dimensions and chiral-spin weights.
- **Principal-bundle/Clifford/Krein — actual math, high:** moving q is a
  covariant family; fixed-q invariance is only one adapted reduction.
- **Variational/symplectic — actual math, high:** q is metric-derived and gets
  no invented Euler equation, momentum or BV generator.
- **Analytic — actual math, high:** finite compact branching says nothing about
  energy or domains.
- **Construction versus selection — actual math, very high:** the carrier and
  breaking pattern are constructed; `J`, the radial `varpi` coefficient and
  its action remain unselected.
- **Contrary path — actual math, high:** a distinct `varpi` doublet remains
  live if the trace-radial composition fails.

The probe passes `57/57` new checks plus v0.195's `56/56` and v0.194's
`50/50`; five planted controls fire.

## Next gate

```text
LOCATE_THE_RADIAL_SCALAR_COEFFICIENT_IN_THE_FULL_U64_64_OR_TWO_U32_32_VARPI
CONNECTION__PROVE_ITS_COMPOSITION_WITH_THE_TRACE_Q_NEGATIVE_COMPLEX_LINE
DESCENDS_AS_THE_COLOR_SINGLET_WEAK_DOUBLET__DERIVE_KINETIC_POTENTIAL_YUKAWA
AND_STATIONARY_NONZERO_AMPLITUDE__KEEP_THE_20_DIMENSIONAL_J_SELECTION_BURDEN
VISIBLE_AND_RETAIN_A_DISTINCT_VARPI_BLOCK_AS_THE_NEGATIVE_CONTROL.
```
