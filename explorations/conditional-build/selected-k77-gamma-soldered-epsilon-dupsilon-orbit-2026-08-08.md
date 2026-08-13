---
artifact_type: conditional_build_result
created: 2026-08-08
status: GAMMA_SOLDERED_EPSILON_PRINCIPAL_ORBIT_EXACT__PHYSICAL_TRANSVERSE_METRIC_K_GREEN_OPEN
source_return: SOURCE-CONFIRMS__EPSILON_GAMMA_FRAME_AND_GAUGE_EQUIVARIANCE_CARRIERS__SOURCE-SILENT__GAMMA_XI_AS_PHYSICAL_DIFFEO_SOLDERING_IDENTITY
ledger: lab/process/conditional-physics-ledger-v0.84.json
canon_verdict_change: none
---

# Selected K77 gamma-soldered epsilon D-Upsilon orbit

## Result in plain English

The missing fourth gauge response has a concrete, zero-parameter candidate
inside geometry the repository had already built.

The obvious epsilon compensator is the ordinary spin/Kosmann lift. Exact K77
calculation shows that it is just the negative of the spin Levi-Civita
connection lift. It has rank three and the identical longitudinal kernel in
timelike, spacelike and null classes. It cannot repair v0.83.

The chimeric Clifford map is different. The existing global construction

```text
gamma_epsilon : C -> ad(P_H)
```

sends an observed covector into a grade-one adjoint element. Choosing the
conditional tangent

```text
eta(xi) = gamma_epsilon(xi-flat)
```

and applying the principal Maurer--Cartan derivative gives
`q tensor gamma_epsilon(xi-flat)`. Its four columns have exact rank four. The
already-proved all-grade raw-residual map is injective, so the corresponding
epsilon residual response also has rank four and is live on the longitudinal
direction missed by source `varpi`.

At a complete residual-zero background, differentiating internal gauge
equivariance fixes the sign of that primitive epsilon response relative to the
connection response. Composing it with the exact source-varpi block produces
a rank-four common-field residual orbit in all three causal classes. The four
metric-orbit values required by `J R=0` are then exact, with no fitted
coefficient, field or external datum.

This removes the **rank obstruction** to the older rank-four metric
diagnostic. It does not prove coefficientwise equality with that diagnostic.
Six transverse physical metric columns, lower-order/nonlinear epsilon terms,
the residual pairing, formal adjoint and Green concomitant remain unbuilt.

## Layer 0

| phrase | object built here | object kept distinct |
| --- | --- | --- |
| source epsilon | H-valued action field | the dependent Clifford map `gamma_epsilon` |
| `gamma_epsilon` | global labelled K77 map `C -> ad(P_H)` | a source-quoted diffeomorphism soldering law |
| Kosmann compensator | grade-two `q wedge xi`, rank three | grade-one `gamma_epsilon(xi-flat)`, rank four |
| `D_epsilon Upsilon` | principal internal-gauge-orbit derivative at `Upsilon*=0` | printed covariant `D_omega Upsilon` |
| complete `J R=0` | exact on the four causal orbit columns | full Frechet identity on all field directions |
| metric response | four Ward-determined orbit values | six transverse physical metric columns |
| rank-four revival | removal of v0.83's fixed-epsilon rank obstruction | identity with the old metric Hessian diagnostic |

The identification `eta=gamma_epsilon(xi-flat)` is the construction. The
source supplies its two endpoint types but does not state the identification.

## Exact construction

For a nonzero observed covector `q`, let

```text
B_q : Lambda2 -> T* tensor Lambda2,       eta |-> q tensor eta
K_q : V -> Lambda2,                      xi |-> (q wedge xi)/2
G_q : V -> T* tensor Cl1,                xi |-> q tensor gamma(xi).
```

On all three causal representatives, exact rational computation gives

```text
B_q K_q = -C_LC,
rank(C_LC)=rank(B_q K_q)=3,
ker(C_LC)=ker(B_q K_q)=span(q-sharp),
rank(G_q)=4.
```

Thus the Kosmann route adds no image. By contrast `G_q` is injective because
`q` is nonzero and the labelled Clifford map is injective. The all-grade
response has rank 1,470 on its 1,470-dimensional `Cl1+Cl2` domain, so it
preserves the four gamma columns. Grade one and grade two are independent,
and the source-varpi plus epsilon response remains rank four for either Ward
sign.

The causal support counts for the epsilon response are

```text
timelike:  14,1,1,1
spacelike: 2,15,2,2
null:      16,3,3,16.
```

The combined source-varpi/epsilon supports are `14,2,2,2`, `15,15,4,4` and
`17,7,7,17`. These are diagnostics of the exact coefficient packets, not
particle counts.

Because the metric diffeomorphism symbol `D` has full column rank four, its
left inverse fixes a unique residual response on `im D` that cancels the
combined source orbit. The complementary projector has rank six. Altering
those six columns changes no orbit Ward check, so they remain physically
unidentified rather than silently fitted.

## Constraint surplus

The global K77 construction already proved:

- grade-one Clifford multiplication is B-skew and lies in `ad(P_H)`;
- the full labelled frame has rank fourteen and preserves Clifford relations;
- `gamma_epsilon` uses the existing source epsilon field; and
- it adds no field, continuous coefficient or discrete datum.

The present construction therefore closes four independent orbit conditions
with zero adjustable local coefficients. That is positive constraint surplus.
The soldering identification itself remains a conditional hypothesis and is
not upgraded to a source derivation.

## Specialist preassessment and hostile review

- **Differential geometry:** the spin/Kosmann and chimeric grade-one lifts are
  inequivalent; only the latter removes the longitudinal kernel.
- **Representation/Clifford geometry:** grade-one B-skew adjoint landing and
  grade-one/grade-two independence are exact.
- **Variational PDE:** only the principal orbit block closes; six transverse
  metric columns and lower-order Frechet terms remain.
- **Symplectic geometry:** `J R=0` is a necessary gauge degeneracy, not a
  reduced presymplectic, coisotropic or BFV theorem.
- **Krein/operator theory:** B-skewness is admissibility, not positivity,
  self-adjointness or a common domain.
- **Complex/path-integral:** no contour, determinant, saddle or measure is
  selected.
- **Source criticism:** source carriers are confirmed; the physical soldering
  identity is source-silent.
- **Repo archaeology:** v0.52's epsilon homonym fence survives; the new route
  uses the separately constructed `gamma_epsilon` rather than relabelling
  source epsilon itself.

## Progress meter

```text
Ledger v0.84 — 82/82 active rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Scoped quotients ranked — 5

headline_delta: none
frontier_conditions_closed: 4
  - Kosmann/spin epsilon route classified exactly as rank-three/no-gain
  - gamma-epsilon principal tangent constructed with rank four
  - longitudinal residual direction proved live
  - four-column common-field principal J R=0 closed without fitting
frontier_conditions_opened: 0
remaining_named_conditions: 2
  - construct six transverse physical D_g Upsilon columns and lower-order D_epsilon terms
  - derive K*, formal adjoint and Green concomitant, then form/test the stationary Gram complex
```

No verdict, residue, quotient, external datum, canon or public posture moves.
P1/P2/P3 remain unused. Curt remains formally separate.

## Verification

- exact K77 main probe: `66/66 PASS`;
- independent Sage/QQ direct-sum certificate: `30/30 PASS`;
- grade-two-only, fitted-compensator, orbit-to-full-metric and physics-promotion
  controls are preregistered to reject.

## Next gate

`CONSTRUCT_COMPLETE_PHYSICAL_DG_UPSILON_SIX_TRANSVERSE_AND_LOWER_ORDER_DEPSILON_BLOCKS__VERIFY_FULL_FRECHET_JR_ZERO__DERIVE_RESIDUAL_K_ADJOINT_AND_GREEN_CONCOMITANT__THEN_FORM_STATIONARY_GRAM_HESSIAN`.
