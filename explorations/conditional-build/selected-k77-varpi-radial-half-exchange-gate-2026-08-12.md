---
artifact_type: exact_construction_and_composition_result
created: 2026-08-12
run_id: RUN-20260812-060541-gu-varpi-radial-half-exchange
status: TRACE_RADIAL_VARPI_COMPONENT_CONSTRUCTED_IN_FULL_U64_64_HALF_EXCHANGE_COMPLEMENT__MOVING_SOLDERED_DOUBLET_EXACT__PURE_RADIAL_POTENTIAL_ZERO
target_claim: NONE-NOT-A-KILL
ledger: lab/process/conditional-physics-ledger-v0.197.json
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 varpi radial half-exchange gate

## Result in plain English

The missing radial coefficient can be placed in the existing source-sized
connection without adding a new scalar field. The exact trace-aligned cell is

```text
a_rad(h) = h (q-flat/q^2) tensor gamma(q).
```

The already-built moving soldering receiver sends it to `h q`. Together with
q's three compact orbit directions, h supplies the fourth real component of
the exact `Y=-1/2` weak doublet constructed in v0.196. The complete moving
receiver is equivariant under all twelve SM generators.

This also decides which unitary presentation can carry the cell. `gamma(q)`
is exactly `H_q`-unitary and anticommutes with ambient chirality. It is
therefore a half-exchanging component of the full `U(64,64)` connection and is
absent from the block-diagonal `U(32,32)xU(32,32)` algebra. The two half forms
remain valid restrictions; they are not a complete standalone parent for this
Higgs route.

The component has a nonzero four-direction derivative carrier and its
zero-order Clifford cell maps each ambient Weyl half isomorphically to the
other. But its isolated self-wedge vanishes exactly. At constant q and h the
one-cell connection is flat, so this cell alone cannot generate a Mexican-hat
potential or select a nonzero vacuum. The next action must compose the full
moving doublet/angular bank or other curvature/distortion terms. Physical
Yukawa textures and observed chirality remain unbuilt.

## Layer 0

| object | established role | still distinct from |
|---|---|---|
| q | geometry-owned normalized trace direction | an independent Higgs field |
| h | scalar coefficient of an existing varpi cell | a derived VEV or mass |
| `a_rad(h)` | vertical full-unitary one-form component | the soldered doublet |
| `sigma_q(a_rad)=h q` | moving equivariant weak-doublet output | the full Higgs action |
| `gamma(q)` | ambient-Weyl half exchanger | observed 4D chirality or a Yukawa texture |
| derivative incidence | nonzero kinetic carrier | action sign, normalization or positivity |
| zero self-wedge | isolated radial-cell theorem | the full moving-doublet potential |
| two `(32,32)` restrictions | nondegenerate half forms | a complete block-only connection parent |

## Exact finite theorem

On `V=R^(6,4)`, the rank-ten receiver is `sigma_q(X)=Xq` for
`X in V* tensor V`. Its radial functional has rank one, its q-orthogonal part
has rank nine, and together they recover the full receiver. The canonical
line is `X=h P_q`, with `P_q=q q-flat/q^2`, so `Xq=hq`. The full preimage of a
radial output has dimension 91; the construction chooses the natural
trace-aligned line without claiming uniqueness among arbitrary inputs.

On the actual real K77 Clifford carrier, with `Q=gamma(q)` and
`H_q=i B Q`, exact identities give

```text
Q^2=-1,
Q^dagger H_q + H_q Q=0,
{omega,Q}=0,
rank(P_- Q P_+)=rank(P_+ Q P_-)=64.
```

Thus Q belongs to `u(64,64)` and not to the commuting block algebra
`u(32,32)+u(32,32)`. For every generator A of the exact pre-Higgs SM algebra,

```text
delta(P_q q) = [A,P_q]q + P_q(Aq) = Aq,
```

which certifies the moving soldering output rather than inferring a doublet
from dimensions.

In an adapted frame `a_rad=h theta Q`. The map `dh -> dh wedge theta Q` has
rank four over the observed base directions, while
`theta wedge theta [Q,Q]=0`. This establishes a derivative carrier and the
absence of an isolated algebraic self-potential, nothing stronger.

## Constraint surplus and action boundary

No new function is introduced: h is a component of the already-booked
function-valued `varpi` field. q remains metric-derived. P1/P2/P3 are unused.
The construction consumes no coefficient, selector or quotient.

The action still has to select the component, fix the 20-dimensional J family,
derive a correctly signed and normalized kinetic term, generate a viable
potential from the complete moving bank, select a stationary nonzero
amplitude, keep a massless photon, separate unwanted doublets/triplets, and
place `P0/rho(Phi)/Y_K/Y_C/C` reality on the physical fermion blocks. Until
then the strict surplus of the full Higgs claim is not computable.

## Source and hostile review

`SC-GRP-01` and `SC-GRP-02` confirm the full unitary parent. `SC-FER-03` and
`SC-META-57` assign Higgs/Yukawa functions to connection one-form cells, while
`SC-GEO-58` disavows a separately added fundamental Higgs. The source is
silent on the trace-radial identification and all action consequences.

The hostile review repaired four possible overclaims: carrier admission is not
action selection; the input cell is not the soldered doublet; derivative rank
is not kinetic positivity; and ambient half exchange is not physical
chirality. Its verdict is
`SURVIVES_AFTER_LAYER_REPAIR__FULL_PARENT_COMPONENT_AND_MOVING_SOLDERED_DOUBLET_ONLY__PURE_RADIAL_POTENTIAL_ZERO`.

The new probe passes `50/50`, plus the predecessor's `57/57`, v0.195's
`56/56` and v0.194's `50/50`, with four new firing controls.

## Next gate

Construct the complete moving `U(3,2)` doublet connection bank around this
radial cell. Compute its curvature action, quartic and doublet/triplet mass
matrix; then test a stationary nonzero amplitude, photon kernel and the
`P0/rho/Y_K/Y_C/C` fermion placement. Keep the full-unitary half-exchange
owner and 20-dimensional J-selection burden explicit.

