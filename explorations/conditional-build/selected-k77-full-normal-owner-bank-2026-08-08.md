---
artifact_type: build_result_and_scope_correction
created: 2026-08-08
status: K77_TEN_NORMAL_GEOMETRY_BANK_EXACT__SEVEN_OWNER_SPLIT_NOT_CANONICAL__TOTAL_MIXED_HESSIAN_REMAINS_INTRINSIC
channels: [BUILD, COMPOSE, SOURCE, VERIFY]
ledger_rows: [LT-GR1, LT-GR2b, LT-GR3, LT-GR5, LT-GR6]
canon_verdict_change: none
---

# Selected K77 full normal-owner bank

## Result in plain English

The attempt to assemble the full bank found a precise boundary.

The geometric part works. All ten directions in the metric fibre
`Sym2(T*X)` induce exact, linearly independent derivatives of the
trace-reversed DeWitt/gimmel metric. Their combined fourteen-dimensional
metric retains signature `(7,7)`. The density response is only rank one, while
the degree-one and degree-two Krein/Clifford pairing and Hodge derivative banks
each retain rank ten. No metric-normal direction is being silently erased.

The seven-way **owner split** from v0.66 does not transfer canonically. In a
fixed frame the metric coefficient derivative is live in all ten directions.
In the exact co-moving frame the same coefficient derivative vanishes and its
effect moves into the field and target-frame terms. The total covector
derivative agrees exactly in both descriptions.

Therefore the total mixed action Hessian remains the correct intrinsic object,
but “B jet + T jet + density + pairing + left Shiab + right Shiab + Hodge” is a
choice of trivialization, not seven invariant K77 subobjects. The source gives
a full upstairs connection difference and a vertical coefficient restriction;
it does not yet give the vertical first-jet lift that would canonically choose
that split.

This is the preregistered `OWNER_INCOMPLETE` ending. It is not a new external
datum and it does not kill the selected action. It corrects what must be built
before antisymmetrization.

## 1. Layer 0

| phrase | object proved here | object kept distinct |
| --- | --- | --- |
| vertical coefficient | value of the upstairs one-form on a vertical tangent | normal derivative of that coefficient |
| normal geometry bank | ten derivatives of the gimmel, density, pairings and Hodge maps | the full action mixed Hessian |
| owner contribution | a term after choosing a field-bundle trivialization/lift | an invariant subobject of the Hessian |
| gauge-rotated Levi-Civita | the reference connection in the augmented-torsion difference on `Y` | a proved vertical connection on the total field bundle |
| dependent field jet | tangent coordinate of an already-owned ambient field | a new action field, coupling or P1/P2/P3 datum |
| total mixed Hessian | intrinsic second differential of the selected action | its coordinate-dependent seven-term expansion |

The source-compatible vertical coefficient map `(s*,res_s^V)` tells us which
components of an upstairs one-form are retained. It does not tell us how to
compare a coefficient at neighbouring metric-fibre points. That comparison is
the missing lift/trivialization question.

## 2. Source return, including Levi-Civita

The checked source material says:

- augmented torsion is the difference of two connections on `Y`;
- the preferred reference in the contorsion slot is the gauge-rotated
  Levi-Civita connection;
- the full connection decomposes into horizontal and vertical coefficient
  sectors; and
- observation is richer than literal differential-form pullback.

It does not publish a vertical covariant derivative of the B/T field bundle
over all ten metric-normal directions, nor an invariant decomposition of the
selected action's mixed Hessian into the seven v0.66 fixture terms.

```text
SOURCE-CONFIRMS:
  full Y-native connection difference, gauge-rotated Levi-Civita reference,
  vertical coefficient sector and observation obligation.

REPO-DERIVES:
  the exact ten-direction K77 metric/density/pairing/Hodge bank and the
  trivialization-change theorem for the normal Euler split.

SOURCE-SILENT:
  a vertical B/T first-jet lift and a preferred invariant seven-owner split.
```

## 3. Exact ten-direction construction

At the mostly-minus Lorentz point `g=diag(1,-1,-1,-1)`, take the ten symmetric
matrix units `h_a` as the metric-fibre basis. Differentiate the trace-reversed
DeWitt metric

```text
G_V(k,l)=tr(g^-1 k g^-1 l)
         -(1/2)tr(g^-1 k)tr(g^-1 l)
```

in every `h_a`, then form

```text
G_Y = g + G_V,
d_a G_Y = h_a + d_a G_V.
```

Exact arithmetic gives:

```text
inertia(G_V) = (6,4),
inertia(G_Y) = (7,7),
rank span{d_a G_Y} = 10.
```

For `K_a=G_Y^-1 d_aG_Y`, the symmetric-frame compensator
`A_a=-K_a/2` satisfies

```text
d_aG_Y + A_a^T G_Y + G_Y A_a = 0
```

for all ten directions. The density response
`rho_a=(1/2)tr(K_a)` satisfies `rho_a+tr(A_a)=0`. Its bank has rank one;
off-diagonal normals have zero density response but nonzero pairing and Hodge
responses.

On exterior degrees one and two, direct compound-matrix differentiation gives

```text
d_a <,> + R(A_a)^T <,> + <,> R(A_a) = 0,
d_a(*) = * R(A_a^T)_in - R(A_a^T)_out *.
```

Both the pairing-derivative bank and Hodge-derivative bank have rank ten in
both degrees. Thus the geometric coefficient substrate requested by v0.66 is
now genuinely full-K77 rather than a sampled fixture.

## 4. Why the seven-way split is not canonical

Let `x` be a field coefficient and use the quadratic control
`I=(1/2)x^T G_Y x`. In the fixed frame the coefficient contribution to the
normal Euler derivative is `(d_aG_Y)x`, nonzero for every `a`. In the co-moving
frame its coefficient derivative is zero. Exact transport gives

```text
A_a^T G_Y x + (d_aG_Y)x = G_Y(-A_a x).
```

The left side calls the change “target frame + metric coefficient”; the right
side calls the same change “field jet.” The total covector is identical. The
allocation to owners is not.

This counterexample fires on all ten directions. It does not say the v0.66
mixed-Hessian formula was wrong. It says its seven independently live terms
were complete **inside its chosen finite trivialization**, not seven invariant
pieces that can be copied into K77 without specifying a lift.

## 5. Symplectic disposition

The covariant phase-space target is the total field-space differential of the
action. A connection or splitting may be useful for calculation, but a physical
presymplectic class should not depend on an arbitrary one.

The efficient successor is therefore a two-horn test:

1. compute how the complete action-owned Green potential transforms under a
   change of vertical splitting and test whether its antisymmetrization is
   splitting-independent up to an exact/basic term;
2. only if that fails, construct a source- or action-owned vertical covariant
   lift compatible with the gauge-rotated Levi-Civita, Krein pairing, Shiab and
   right-H structure.

This order may remove the missing lift as a coordinate artifact. It also has a
clean kill: a nonbasic splitting defect forces the second horn.

## 6. What moved and what did not

Built:

- all ten real-K77 normal metric derivatives;
- the exact rank-one density subbank;
- exact rank-ten degree-one/two pairing and Hodge banks;
- the co-moving Phi transport; and
- an all-ten-direction proof that the seven-owner split is trivialization-dependent.

Still open:

- a splitting-independent total selected-action mixed Hessian bank, or a
  source/action-owned vertical B/T lift;
- the complete Shiab/action coefficient expansion in that invariant language;
- Green-potential antisymmetrization and basicness;
- common Krein/domain, BV and BFV descent.

No verdict, residue, quotient, P1/P2/P3, canon or public posture moves. Five
ledger distances are corrected because “assemble seven invariant owners” is no
longer the right task.

## 7. Review outcome

- **Symplectic geometry:** prefer the splitting-change/basicness calculation
  before introducing a connection; the reduced two-form should be intrinsic.
- **Differential geometry:** a vertical value map is not a horizontal lift of
  the field bundle's tangent exact sequence.
- **Variational PDE:** the total mixed Hessian survives; only its coordinate
  decomposition is retyped.
- **Krein/operator theory:** exact pairing motion is retained with no positivity
  or common-domain claim.
- **Source criticism:** the gauge-rotated Levi-Civita is relevant but not quoted
  as the missing vertical field-space connection.

Both standing hostile charges fire:

1. **Summary outruns artifact:** v0.66's “seven owner classes complete” is
   narrowed to “complete and live in the chosen rational fixture.”
2. **Artifact defends a superseded object:** the next gate no longer tries to
   preserve that coordinate split; it targets the intrinsic total Hessian.

## 8. Progress meter

```text
Ledger v0.67 — 82/82 active target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped

headline_delta: none
frontier_conditions_closed: 2
  - all ten K77 normal geometric directions are exact
  - the seven-owner split's transformation law is decided
frontier_conditions_opened: 1
  - test splitting independence of the antisymmetrized Green potential
remaining_named_conditions: 3
```

Next:

`GREEN_POTENTIAL_SPLITTING_CHANGE_AND_BASICNESS__IF_NONBASIC_CONSTRUCT_VERTICAL_COVARIANT_LIFT`.

Main probe: `48/48 PASS`. Independent Sage/QQ: `PASS`.
