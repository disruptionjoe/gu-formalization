---
artifact_type: conditional_build_composition_result
created: 2026-08-12
run_id: RUN-20260812-151325-gu-i2b-nonlinear-receiver-composition
status: NONLINEAR_PRODUCT_RECEIVER_EXACT__ARBITRARY_FIELD_I2B_EULER_PREBOUNDARY_COEFFICIENTS_OPEN
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 I2B nonlinear receiver composition

## Result

The nonlinear receiver requested by v0.210 did not require another epsilon
field.  Its two factors had already been built separately:

1. the finite observation section owns the eta-self-adjoint graph projector
   `P_J`, with complement `Q_J=1-P_J`; and
2. the selected real I2B first variation owns the residual-space primalizer
   `P_+`, with complement `P_-=1-P_+`.

Their exact product gives four complementary sectors on a residual-valued
upstairs equation:

```text
P_J tensor P_+    observed / real-fixed
P_J tensor P_-    observed / anti-fixed
Q_J tensor P_+    metric-normal / real-fixed
Q_J tensor P_-    metric-normal / anti-fixed.
```

For the actual dimensions their ranks are

```text
784 + 784 + 1960 + 1960 = 5488 = 14 x 392.
```

They are pairwise complementary idempotents and sum to the identity.  Thus the
receiver is lossless before any physical quotient.  Ordinary four-dimensional
pullback still has rank four and a ten-dimensional conormal kernel; an exact
nonzero witness erased by pullback is retained by `Q_J`.

This closes the receiver burden.  It does **not** close the I2B Euler equation:
the remaining arbitrary-field coefficients must still be differentiated from
the action and inserted into the receiver before its Green potential can be
antisymmetrized at this branch.

## Nonlinear moving composition

The exact finite section is

```text
L_J=(I,J)^T,
G_J=L_J^T eta L_J,
P_J=L_J G_J^-1 L_J^T eta.
```

On the admitted rational graph, `G_J` is nondegenerate with inertia `(1,3)`,
and `P_J/Q_J` have ranks `4/10`.  The four q-row derivatives from v0.210 give
four independent `dot P_J` satisfying the differentiated idempotency and
eta-adjoint identities.

For every sector `E_ab=P_a tensor P_b`, simultaneous motion is

```text
dot E_ab = dot P_a tensor P_b + P_a tensor dot P_b.
```

All four q-row directions pass exact reconstruction and differentiated-sector
identities.  Freezing either the observation factor or the residual
primalizer changes the answer in every direction.  A genuinely mixed
fractional K77 graph transition and a moving residual transition conjugate the
product receiver exactly.

The v0.210 radial result remains correctly typed: its residual derivative is
nonzero in four base-jet directions while its local action derivative is zero
by grade orthogonality.  A lossless receiver preserves that zero equation
value; it does not manufacture a force or erase the metric-normal coordinate.

## Layer 0

| phrase | object closed here | kept distinct |
| --- | --- | --- |
| observation reduction | finite graph projector `P_J` | a preferred adapted or Spin frame |
| real Euler primalizer | residual projector `P_+` | the nonlinear residual itself |
| complete receiver | tangent/normal times fixed/anti-fixed direct sum | ordinary pullback |
| lossless transport | identity decomposition before reduction | a physical gauge quotient |
| source epsilon | dependent conjugated Clifford frame in Weinstein's grammar | repository `P_J` or `P_+` |
| Euler owner | arbitrary-field derivative of the selected I2B action | the receiver accepting its output |
| preboundary | action-owned Green one-form and its antisymmetrization | this algebraic product split |

The product lives at the natural type of an `E`-valued one-form/Euler image on
the `14`-dimensional observerse.  It does not identify the two factors or turn
one into an external datum.

## Source return

Weinstein's source corrects naive direct pullback and owns the section,
epsilon-conjugated frame, gauge-rotated Levi-Civita and two-connection arena.
It does not print the exact graph projector, product receiver or current I2B
arbitrary-field Euler bank.

```text
SOURCE-CORRECTS: observation is richer than literal pullback.
SOURCE-CONFIRMS: section/epsilon/Levi-Civita/two-connection grammar.
REPO-DERIVES: exact product receiver and moving product rule.
SOURCE-SILENT: product formula and remaining I2B Euler/preboundary bank.
```

The source `C^(32,32)+C^(32,32)` carrier split, derived block-preserving
`U(32,32)xU(32,32)`, full `U(64,64)` parent and independent connections remain
four separately typed objects.

## Specialist and hostile review

- **Principal-bundle geometry:** the projector and reduced connection already
  own stabilizer overlap; no preferred frame is selected.
- **Variational bicomplex:** a receiver is not the Euler coefficient map.  The
  latter must still come from differentiating the selected action.
- **Clifford/Krein:** `P_+` is action-adjoint at the fixed-real first-variation
  layer.  No positivity or nonlinear replacement of the residual is inferred.
- **Symplectic geometry:** lossless reception precedes the action-owned Green
  potential, antisymmetrization, basicness and BFV reduction.
- **Analytic/PDE:** there is no common closed domain, spectrum, propagator,
  evolution or stability theorem.
- **Source criticism:** the exact product is repository-derived; source epsilon
  remains distinct and its finer physical identification is open.
- **Contrary review:** the four sectors are not claimed to be four physical
  fields.  They are a bookkeeping-free direct-sum decomposition of one
  residual-valued equation bundle.

The hostile review scopes the `5488` rank statement as a tensor-rank theorem
composed from exact `14=4+10` and `392=196+196` predecessors, rather than a
fresh materialization of a `5488 x 5488` matrix.  It also rejects the stronger
claim that the receiver selects the physical observation section or settles
source epsilon.

## Progress and next gate

```text
Ledger v0.211 — 82/82 target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue: 84 continuous + >=19 function-valued + 9 discrete forks
Tightness: T4x1 T3x3 T2x1 · scoped quotients: 5
Headline delta: none
Frontier: 1 named condition closed · 0 opened · 1 remains
```

No field, parameter, selector, quotient or external datum is added.
P1/P2/P3 remain unchanged and unused.

Next assemble the remaining arbitrary-field I2B Euler coefficients—including
the moving connection, trace/Hodge/Shiab, section and field terms—inside this
receiver, then form the action-owned Green potential and its presymplectic
preboundary class.  Do not reopen the nonlinear receiver or invent another
epsilon field.

Main exact probe: `54/54 PASS`.
