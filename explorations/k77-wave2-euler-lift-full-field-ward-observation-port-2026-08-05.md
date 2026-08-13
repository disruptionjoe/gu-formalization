---
title: "K77 Wave 2: Euler-lift Ward and observation receiver theorem"
status: active_research
doc_type: construction_result
created: 2026-08-05
route_disposition: K77_EULER_LIFT_FULL_FIELD_WARD_DOMAIN_OBSERVATION_PORT
gate_after: K77_OBSERVED_COMPLEX_DETECTS_UPSTAIRS_EULER_SHELL_IFF_NO_LEAKAGE_AND_RECEIVER_FAITHFULNESS
fork_assumed: SIGNATURE-AMBIENT
fork_stack_acknowledged: "The wave continues the source-faithful K77 action-owned object only far enough to test its observation receiver, introduces no signature-dependent selector, and preserves the explicit K95 carrier/primalizer/transition re-port cost."
search_space_dim: "0 selector parameters; obstruction dimension = dim ker(rho_X sharp_X O_E), computed wholesale"
free_object_delta: 0
residue_touched:
  - "K77-W2-OBSERVATION-PORT: T3"
probe: tests/channel-swings/k77_wave2_euler_lift_ward_observation_probe.py
registry: lab/process/k77-wave2-euler-lift-ward-observation-port.json
grade: "Exact finite receiver theorem and two independent false-shell witnesses. Observed nilpotence detects the upstairs action Euler row only modulo the equation-observation and coefficient-representation kernels. No-leakage plus faithfulness on the observed Euler image restores the converse in the exact fixture. The actual Y14 receiver, physical coefficient module, odd BV closure, common analytic domain, and physics remain open."
canon_verdict_change: none
---

# K77 Wave 2 Euler-lift Ward and observation receiver theorem

## Result first

The action-owned two-connection construction survives observation only under
two separate conditions. The observed equation must retain every upstairs
Euler component generated on the physical field image, and the observed
coefficient module must faithfully see the resulting connection difference.

Without both conditions, a nonzero upstairs Euler covector can produce a
four-dimensional shifted operator whose square vanishes. There are two exact,
independent mechanisms:

1. **equation leakage:** a normal Euler component is killed by the
   equation-dual observation map; and
2. **representation blindness:** the observed Euler covector is nonzero, but
   its primalized connection difference lies in the kernel of the observed
   coefficient action.

The whole obstruction is one kernel,

\[
 K_{\rm obs}
 =\ker\!\left(\rho_X\circ\sharp_X\circ O_E\right),
\]

not a list of projection candidates. Observed nilpotence detects the upstairs
Euler row modulo `K_obs`. On the no-leakage image, invertibility of `sharp_X`
and faithfulness of `rho_X` make the restricted composite injective and restore
the predecessor's bidirectional shell theorem.

This moves the vague observation-port debt to a formula-level `T3` receiver
condition. It does not build the actual `Y=Met(X)` receiver or close Wave 2.

## Plain English

Upstairs, the action tells us how far the field is from satisfying its
connection equation, and the previous wave turned that error into the
difference between two connections. Downstairs, an observer can miss that
error in two ways. The projection can throw away the direction containing the
error, or the matter representation can be blind to a connection difference
that survived the projection.

So “the four-dimensional operator squares to zero” is not yet the same as
“the fourteen-dimensional action equation is satisfied.” It becomes the same
only after we prove that the observation map keeps the relevant equation and
that the observed fields faithfully feel its connection difference.

## Binding pre-wave disposition

- `fork_assumed: SIGNATURE-AMBIENT`, K77 horn. The K95 cost is a complete
  carrier, pseudo-musical and transition re-port before transfer.
- `search_space_dim: 0 selector parameters`. All maps are inherited and fixed;
  the task is a kernel/rank theorem, so candidate-by-candidate testing is
  forbidden.
- `free_object_delta: 0`. No field, current, connection, section or datum is
  introduced. The receiver debt is tightened but not yet retired.
- `residue_touched: K77-W2-OBSERVATION-PORT:T3`, upgraded from the opening
  `T2` target because necessary and sufficient finite conditions are now
  explicit.

The open fork stack is acknowledged because the active construction uses the
source-derived K77 real form while the registry retains a separately typed
ambient-signature fork. This wave does not decide that fork.

## Layer 0

| phrase | object here | kept distinct |
|---|---|---|
| upstairs Euler equation | `E_Y(L_F phi)` in the density-dual equation bundle | its observed pullback |
| observed Euler equation | `e_X=O_E e_Y` | a validated physical Standard Model or GR equation |
| observed pair difference | `tau_X=sharp_X e_X` | the full upstairs `tau_E` if the observation loses directions |
| faithful action | injectivity of `rho_X` on the observed `tau_X` image | faithfulness of an unrelated upstairs or pre-quotient module |
| no-leakage | `e_Y in im L_E` on the lifted field image | the local split identity `R_F L_F=1` |
| Ward identity | contraction of every Euler row with the even gauge generator | proof that normal Euler components vanish |
| preboundary quotient | quotient by a proved characteristic kernel | a physical BFV phase space or analytic domain |

No decomposition, rank or kernel dimension is read as a particle or generation
count.

## Source collision before construction

The source receipt is
[`gu-euler-lift-ward-observation-source-reinspection-2026-08-05.md`](../lab/sources/gu-euler-lift-ward-observation-source-reinspection-2026-08-05.md).

| source question | disposition |
|---|---|
| observerse section and four-dimensional pullback | `SOURCE-CONFIRMS` |
| Curt's horizontal/vertical connection decomposition after pullback | `CURT-RECONSTRUCTS / ERIC-GUIDES` |
| equation-dual observation map | `SOURCE-SILENT` |
| Euler no-leakage | `SOURCE-SILENT` |
| physical coefficient module and faithfulness | `SOURCE-SILENT` |
| odd BV differential, common domain, physical phase space | `SOURCE-SILENT OR UNRELEASED` |

The source tells us where to look. It does not license the inference that
pullback preserves the action shell.

## Inline divergent specialist preassessment

Ten lightweight lenses were applied before construction:

1. differential geometry required connection-difference naturality after
   pullback;
2. the variational bicomplex required the equation-dual map rather than only a
   field retraction;
3. gauge/BV geometry separated even Ward naturality from odd master closure;
4. Krein theory retained the indefinite pseudo-musical and rejected a positive
   Riesz reading;
5. homological algebra selected the kernel of the composite detector;
6. representation theory warned that quotienting can destroy faithfulness;
7. hyperbolic PDE separated invariant-image no-leakage from well-posedness;
8. symplectic geometry required a characteristic-kernel proof before quotient;
9. exact-computation engineering demanded both false-shell mechanisms and a
   repaired receiver; and
10. proof-systems review charged summary overreach and defense of the
    superseded claim that no observation machinery exists.

## The receiver theorem

Let `L_F:F_X->F_Y` lift observed fields. Let `L_E:E_X^!->E_Y^!` and
`O_E:E_Y^!->E_X^!` be equation lift and observation maps with

\[
 O_E L_E=1.
\]

For a lifted field define

\[
 e_Y=E_Y(L_F\phi),\qquad e_X=O_Ee_Y,
 \qquad \tau_X=\sharp_Xe_X.
\]

The observed shifted square has southwest detector `rho_X(tau_X)`. Therefore

\[
 \mathcal D_{E,X}^2=0
 \quad\Longrightarrow\quad
 e_Y\in\ker(\rho_X\sharp_XO_E),
\]

with equality of the two conditions on the stated shifted coefficient module.
The unconditional conclusion is a quotient shell, not the upstairs shell.

Now impose:

1. **equation no-leakage** on the observed field image,
   `(1-L_EO_E)e_Y=0`; and
2. **receiver faithfulness**, meaning `rho_X sharp_X` is injective on the
   observed Euler image.

Then `D_{E,X}^2=0` gives `e_X=0`; no-leakage gives
`e_Y=L_Ee_X=0`. Conversely `e_Y=0` still implies the observed square vanishes.
Thus, on that restricted image,

\[
 \mathcal D_{E,X}^2=0
 \quad\Longleftrightarrow\quad
 E_Y(L_F\phi)=0.
\]

The pseudo-musical diagram must also commute,

\[
 O_{\rm conn}\sharp_Y=\sharp_XO_E,
\]

so the observed pair difference is genuinely the observation of the
action-owned upstairs pair. The exact fixture verifies this identity with an
indefinite `sharp_Y`; it uses no positivity argument.

## Exact false-shell witnesses

The rational fixture has a four-dimensional upstairs equation space and a
two-dimensional observed equation space.

| quantity | exact result |
|---|---:|
| equation-observation kernel | dimension 2 |
| blind coefficient detector rank | 1 |
| complete blind detector kernel | dimension 3 |
| additional representation-blind direction | dimension 1 |
| faithful detector rank | 2 |
| faithful detector kernel restricted to no-leakage image | dimension 0 |

One nonzero normal Euler covector is killed by `O_E`. A different nonzero
Euler covector survives `O_E` but is killed by `rho_X sharp_X`. The latter
produces an exactly square-zero observed shifted operator in the blind module;
the faithful module restores the nonzero southwest square block.

The first run caught two implementation errors without changing the theorem:
the faithful restricted detector is invertible rather than literally the
identity in the selected indefinite coordinates, and the connection
difference must be checked in the southwest block of the **square**.

## Even Ward, finite domain, and preboundary boundary

For tangent gauge generators `G_Y L_F=L_F G_X`, duality gives

\[
 \langle e_Y,G_Y\rangle
 =\langle O_Ee_Y,G_X\rangle.
\]

The exact fixture verifies this Ward naturality. It also shows why Ward closure
does not replace no-leakage: a normal Euler covector can pair to zero with
every tangent gauge generator while remaining nonzero.

At finite linear grade, no-leakage is exactly the invariant-image condition

\[
 (1-L_EO_E)E_YL_F=0.
\]

A hostile operator passes observed-equation transport but fails this condition;
the repaired operator preserves the image. This is not an unbounded-operator
domain theorem.

The finite preboundary form pulls back correctly, has a two-dimensional
characteristic kernel and a nondegenerate quotient. The leakage witness lies
in that kernel. That fact does **not** authorize quotienting it as gauge: an
action-derived tangent/BV differential and physical boundary conditions are
still required.

## Constraint and residue accounting

| quantity | value |
|---|---:|
| selector parameters searched | 0 |
| equation-blind fixture directions | 2 |
| additional representation-blind direction | 1 |
| new free coefficients or fields | 0 |
| free object delta | 0 |
| residue | `K77-W2-OBSERVATION-PORT:T3` |

This is not counted as phenomenological constraint surplus. It is a necessary
and sufficient conditional receiver theorem for a construction interface.

## Seven-axis disposition

| layer | status |
|---|---|
| Layer 0 | pass with seven object separations and two blindness mechanisms |
| L1 source | pullback guidance confirmed; receiver theorem silent |
| L2 algebra | complete detection kernel and repaired restricted injection built |
| L3 geometry | finite pseudo-musical observation square built; actual Y14 receiver open |
| L4 variation | actual-Euler action ownership preserved |
| L5 covariance | even Ward contraction ports; odd BV/master closure open |
| L6 analytic | common closed Krein/Green domain and physical BFV phase space open |
| L7 physics | no row moves |

P1/P2/P3 remain unchanged and unused. Curt remains formally separate guidance
inside the Eric lane. `TG-1 AND TG-2 AND TG-3` remains not promoted. Wave 3
stays closed.

## Hostile post-review and next gate

The two-sided review is recorded in
[`2026-08-05-k77-wave2-euler-lift-ward-observation-review.md`](../lab/process/hostile-reviews/2026-08-05-k77-wave2-euler-lift-ward-observation-review.md).
It required the quotient-shell wording, both independent blindness mechanisms,
the finite/model grade on Ward and preboundary, and explicit recognition that
the repo already contains observation machinery.

The next gate is:

```text
K77_ACTUAL_Y14_EULER_RECEIVER_FAITHFUL_MODULE_AND_COMMON_GREEN_DOMAIN
```

It must instantiate the actual equation lift/dual, coefficient module and
moving pseudo-musical on the `Y=Met(X)` atlas, prove no-leakage on the complete
action field image, derive the BV/preboundary quotient, and either construct or
kill one common closed Krein/Green domain. Only then can Wave 3's atomic
particle/equation incidence census be admitted.

## Reproduction

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/k77_wave2_euler_lift_ward_observation_probe.py
```

Focused receipt: `7 source + 29 type + 32 exact + 7 planted = 75/75 PASS`.
