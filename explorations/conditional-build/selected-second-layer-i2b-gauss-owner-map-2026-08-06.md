---
artifact_type: construction_result
created: 2026-08-06
status: I2B_GAUSS_WRONG_TYPE__PROJECTED_FULL_II_PLUS_TRACE_SQUARE_EXACT__FULL_RESIDUAL_LEAKAGE_LIVE
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
ledger_rows: [LT-GR1, LT-GR2b, LT-GR3, LT-GR5, LT-GR6]
source_return: SOURCE-SILENT
free_object_delta: "zero fields, parameters, data, selectors, quotients or boundary conditions"
scripts:
  - tests/channel-swings/selected_second_layer_i2b_gauss_owner_map_probe.py
registry: lab/process/selected-second-layer-i2b-gauss-owner-map.json
---

# Second-layer I2B / Gauss-owner map

## Outcome

The obvious local identification

```text
I2B = 1/2 <Upsilon_B,G Upsilon_B>  ?=  c ||II||^2
```

does not yet type-check on the full first-action residual target.

At the selected invariant stationary branch `T*=-(kappa_1/312) Phi1`, the
rank-100 canonical Gauss carrier is closed under the **Gauss-projected**
first-action Hessian. Squaring that projected Hessian gives the exact bilinear
form

```text
K_Gauss = kappa_1^2 [
    (15376/13689) <II,II>
  - (448/4563)    <tr II,tr II>
].
```

It is full rank and has native inertia `(54,46)`. Thus even the projected
piece is not a pure scalar multiple of the observer full-`II` norm.

But this is not the full `I2B` pullback. The first-action Hessian sends a Gauss
variation into the orthogonal complement of the Gauss carrier inside the
complete 1,274-dimensional Clifford-grade-two residual bank. One exact
witness is

```text
II_(00)^4  -->  e^5 tensor gamma_4 gamma_5
coefficient = 2/39.
```

The target direction has a vertical one-form index and a normal-normal
Clifford bivector, so it is absent from the rank-100 observed Gauss carrier.
The preregistered ending `I2B_GAUSS_WRONG_TYPE` therefore fires: a projected
component has been constructed, but the full residual-target pullback and its
co-moving epsilon/frame completion remain open.

## Plain English

The second action squares the *whole error signal* produced by the first
action. We asked whether, when the four-dimensional slice bends, that error
signal is just the bending tensor `II` in disguise.

Part of it is. On the bending directions themselves, the square is a fixed
mixture of the full bending and its trace. But bending also excites an
upstairs vertical component that is not visible if we keep only `II`. Squaring
only the visible part would throw that component away. So we have not found an
identity between the two actions; we have found the exact visible block and
the first exact missing block.

This is useful because the remaining construction is no longer the vague
request “map `I2B` to `II`.” It is the concrete 1,274-by-100 residual map,
followed by its moving frame/observation composition.

## Layer 0

| object | constructed here | kept distinct |
| --- | --- | --- |
| first action `I1B` | its stationary Hessian on the selected branch | its Euler residual as a field |
| residual `Upsilon_B` | linearized response to Gauss variations | augmented torsion `T` itself |
| second action `I2B` | norm square architecture | first-action quadratic mass term |
| Gauss projection | rank-100 `II` component of the residual | complete 1,274-dimensional `Cl2` residual |
| observer `I_II` | full-`II` quadratic target | a proved pullback of `I2B` |
| local bilinear | exact fixed-background Hessian square | moving Euler/preboundary/covariant phase space |

## Source return

`SOURCE-SILENT` at the decisive map.

The released material confirms that the second action is the norm square of
the first residual and says the resulting operator has Yang--Mills-like and
zeroth-order Einstein-like pieces. It does not identify that norm with the
observer `||II||^2` functional, give the residual projection, or remove the
vertical complement. The coefficients and leakage witness are repository
constructions, not quotations from Weinstein or Curt.

## 1. Exact carriers and pairings

The complete Clifford-grade-two translation carrier is

```text
V* tensor Lambda^2 V,  dim = 14 * 91 = 1274.
```

The canonical Gauss insertion sends

```text
Sym^2 H* tensor V_normal,  dim = 10 * 10 = 100,
```

into the horizontal mixed `H-normal` connection block. It is an isometry for
the written action pairing and the full ordered-`II` metric. Its orthogonal
complement has rank 1,174.

As a control, the standard wedge and contraction maps on
`V* tensor Lambda^2 V` have exact coisometry constants three and thirteen.
The symmetric Gauss image has zero total-`Lambda^3` component. A tempting
full-Spin scalar-eigenvalue shortcut nevertheless fails for the fixed-epsilon
translation Hessian: its formal vector and hook pieces mix. The probe therefore
computes the complete 100-by-100 Gauss block directly.

## 2. Exact projected second-layer form

At `kappa_1=1`, the Gauss Hessian is symmetric and rank 100. Its relative
square has magnitudes

```text
(100/117)^2 on the ten trace directions,
(124/117)^2 on the ninety traceless directions.
```

Equivalently,

```text
H_Gauss^T G_II^-1 H_Gauss
  = (15376/13689) G_II
    - (448/4563) Trace^T G_normal Trace.
```

Homogeneity restores the overall `kappa_1^2`. This checks every entry, not
one trace and one traceless sample. A planted one-direction matcher would have
missed the trace-square term.

The form remains indefinite: residual squaring uses GU's native indefinite
pairing and is a congruence, not an absolute-value norm. No positive energy or
Hilbert space follows.

## 3. Exact no-closure witness

Let `P_G` be the native-orthogonal rank-100 projector onto the Gauss image.
The probe searches complement representatives in the complete `Cl2` bank and
tests the cross Hessian. It finds

```text
< e^5 tensor gamma_4 gamma_5,
  H_act I_Gauss(II_(00)^4) > = 2/39.
```

The left direction is exactly orthogonal to every Gauss insertion. Therefore

```text
(1-P_G) H_act I_Gauss != 0.
```

Consequently

```text
I_Gauss^! H_act^! G_full^-1 H_act I_Gauss
```

cannot be replaced by the projected expression without computing the omitted
residual response. Other Clifford grades, moving target metric, epsilon/frame
and observation jets remain additional owners; this result does not assert
that `Cl2` is the complete residual support.

## 4. Hostile and symplectic review

The review changed the result twice.

1. A representation shortcut initially treated the fixed-epsilon Hessian as
   scalar on formal full-Spin components. A nonzero vector--hook cross term
   killed that shortcut; the final probe squares the direct 100-by-100 block.
2. The first summary called the fixed combination the full `I2B` pullback.
   The mandatory variational/symplectic check demanded orthogonal-complement
   closure and found the `2/39` leakage witness. The formula is now explicitly
   the Gauss-projected component.

The symplectic lens also refuses to identify a nondegenerate local quadratic
form with a reduced Hamiltonian class. Euler, presymplectic current,
preboundary descent, odd BV and global BFV remain unbuilt.

## 5. Ledger and next gate

Ledger v0.38 keeps `82/82`, verdicts `32/19/25/6`, residue
`84 + >=19 functions + 9 forks`, four scoped quotients and unused P1/P2/P3.
Five rows move by distance only.

The next gate is now smaller and executable:

```text
BUILD_COMPLETE_1274_BY_100_CL2_RESIDUAL_TARGET_PULLBACK;
ADD_ANY_OTHER_GRADE_SUPPORT;
COMOVE_EPSILON_FRAME_AND_OBSERVATION;
THEN DERIVE THE FULL I2B QUADRATIC, CUBIC, EULER, PREBOUNDARY AND HELICITY.
```

Do not build a common global domain until the completed second-layer symbol
actually supplies helicity two.

## Boundaries

No Einstein equation, graviton, Weyl/Bach amplitude, cosmological mechanism,
positive energy, global domain, BV/BFV quotient, coefficient selection,
residue reduction or external datum is claimed. Curt remains formally
separate and no third lane is promoted.
