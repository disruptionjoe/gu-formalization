---
artifact_type: conditional_build_source_ownership_correction
created: 2026-08-12
status: SOURCE_NORMAL_JET_OPERATOR_OWNED__REAL_FORM_IMAGE_RANK80__COKERNEL_RANK80
canon_verdict_change: none
---

# Selected K77 I2B source-normal-jet reconciliation

## Result

The missing contact from v0.219 is now better typed.  It is not one more
geometric coefficient that the gauge-rotated Levi-Civita construction should
uniquely produce.

The released source already supplies the relevant differential operator.  Its
augmented torsion is the full upstairs one-form `T=A-B`, and the residual
contains the nonzero linear term

```text
kappa * T.
```

On the actual sixteen-dimensional K77 live response, the observation readout
applies Hodge again.  In signature `(7,7)`, Hodge squares to `+1` on these
one-form responses.  That does **not** make the source map an isomorphism,
because `T` is valued in the real Lie algebra `u(64,64)`.  Grade-two Clifford
directions in that real form have real coefficients.  The live response has
eight real and twenty-four imaginary bivector coefficients; after the exact
adapted observer pairing, only eight of its sixteen coordinates are reached.
Ten metric normals give ten independent copies:

```text
J1_normal(T_real-u) -> J1_normal(Upsilon)_live-dual
rank per normal = 8 of 16,
total rank = 80 of 160.
```

Consequently the source supplies a nontrivial off-shell subcontact, but not
every `16 x 10` contact.  The zero preserve completion from v0.219 is
admissible.  Its scalar destroy/create completions lie in the exact rank-80
cokernel and are not produced by the current real source tangent.  A complex
preimage is therefore diagnostic of a real-descent obstruction rather than a
physical source germ.

This is not a physical selection.  It proves that the source action fixes the
**normal-jet operator**, while a field configuration fixes the **value** of
that jet.  The action can select a value only through its coupled equations of
motion, their normal prolongation and a physical state/domain.  The presently
used nonzero `SC-ACT-04` branch is not such a solution: it retains fourteen
nonzero fixed-`H_q` transverse connection derivatives.

## Why this corrects the queue

V0.219 accurately proved non-identifiability from restricted pullback, but its
successor—“construct the unique source-native normal jet from geometry”—did
not absorb v0.66–v0.68:

- v0.66 already separated the intrinsic jet operator from its value on a
  chosen background germ;
- v0.67 built all ten K77 geometric normal directions and showed that the
  seven-owner split depends on trivialization; and
- v0.68 proved the complete cotangent/Green object is splitting-natural, so a
  new vertical connection is not needed merely to repair coordinates.

The present exact rank-80 result completes that composition while exposing a
new typed burden.  The geometry bank is built and the source operator is
known, but half of the live contact is outside its real-form image.  The next
question is not to guess a unique metric coefficient; it is to identify the
cokernel as a representation and test whether the coupled Euler system,
carrier reduction or real-descent data legitimately changes it.

## Layer 0

| object | established here | kept distinct |
| --- | --- | --- |
| source-normal-jet operator | derivative of the released full two-connection residual | one numerical normal jet |
| normal field germ | first jet of `T=A-B` in ten metric-normal directions | new coupling or external datum |
| source-compatible completion | local off-shell germ in the rank-80 real-u image | a complex response or a solution of the coupled field equations |
| `Upsilon` jet | derivative of the residual entering `I2B` | the action-normal Euler mixed Hessian from v0.66 |
| generic observer line | open `A>0` contact stratum | global line, time arrow or physical vacuum |
| source carrier | `C^(32,32)+C^(32,32)` halves inside the source construction | its block subgroup, full `U(64,64)` parent or two independent connections |

The gauge-rotated Levi-Civita connection can own the reference `B` jet while
the independent connection `A` still changes `T=A-B` arbitrarily **inside the
real source algebra**.  Fixing the reference therefore does not select the
difference-field germ, but complex live-response coordinates are not thereby
promoted to admissible connection directions.

## Exact certificate

The probe replays v0.219 and uses its actual sixteen live K77 response forms.
It verifies:

- all sixteen are one-form, Clifford-grade-two responses;
- their adapted observer pairing has rank sixteen;
- Hodge squared is the identity on all sixteen;
- the live response contains eight real and twenty-four imaginary bivector
  coefficients;
- the full real-u same-support bank has exact rank eight in the live dual;
- adapted sharp preserves all eight live Clifford masks, while Clifford trace
  orthogonality excludes all other masks from raising that rank;
- the ten-normal contact map has exact rank `80` inside dimension `160`;
- the `kappa=0` control has rank zero;
- a nonzero source-image direction is attained; and
- the v0.219 zero completion is admissible while its scalar destroy/create
  completions lie outside the real source image.

The main probe passes `46/46`, including four controls/plants.  The result is
exact and finite; no matcher, floating tolerance or fitted contact is used.

## Constraint-surplus and physical meaning

The rank-80 image is not booked as 80 action parameters.  It is local first
derivative data of an existing ambient field.  Its rank-80 complement is also
not booked as external datum: it is presently a real-form cokernel whose
physical meaning is open.  Equations, constraints, gauge, regularity and
boundary or initial conditions may further reduce the image; they do not
automatically fill the cokernel.

For the conditional build, the result is mixed and high-information: the
source has a substantial normal-contact channel, but the particular scalar
motion that v0.219 used to change observer strata is not in that channel.
What remains unproved is whether a genuine solution selected by the full
action reaches `A>0`, whether another source-owned term supplies the missing
module, or whether the cokernel is a durable obstruction.

No datum, residue, quotient, parameter, P1/P2/P3, verdict, canon entry or
public posture changes.

## Required next gate

First identify the exact rank-eight cokernel as a module under the observation
stabilizer and check whether it is the repeated defect module seen elsewhere.
Then derive the coupled normal prolongation of the actual Euler equations on a
genuine stationary background, including both connection fields, moving
geometry and the observation receiver.  Compute the allowed real-source image
after constraints/gauge/domain conditions and test it against

```text
(a0 + q s)^2 + a1^2 + a2^2 + a3^2 = 0.
```

Retain three controls:

1. `kappa=0`, where the torsion-jet image disappears;
2. the unrestricted complex response, which must not be passed off as a real
   source connection;
3. an action-owned reduced tangent, which may remove more response directions;
4. the current nonstationary branch, which must not be passed off as an
   on-shell solution.

Only after the prolonged solution space is known should the program advance
to a global common line, arrow, kinetic/preboundary spectrum or external
fallback.
