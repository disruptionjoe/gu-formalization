---
title: "Real I1B boundary constraints and the limit of the free-momentum argument"
status: active_research
claim_verdict: universal_bulk_acceleration_identity_and_rank_five_boundary_compatibility_constraint
doc_type: native_action_boundary_constraint_result
created: 2026-10-08
target_claim: NONE-NOT-A-KILL
bears_on: [SC-ACT-06, SC-META-53]
spec_row: SA-U1
canon_verdict_change: none
receipt: lab/process/native-zorro-boundary-constraints.json
probe: tests/channel-swings/native_zorro_boundary_constraint_probe.py
---

# The boundary qualification is an actual constraint problem

> **2026-10-09 successor:** the
> [real compact-core energy theorem](native-zorro-real-energy-2026-10-09.md)
> constructs two-sided energy families in a reflection character with zero
> full metric force and all-order formal boundary compatibility. The
> rank-five momentum restriction below is unchanged. The new route avoids
> its free-momentum hypothesis; a closed physical evolution domain remains
> unconstructed.

**The real bulk acceleration identity extends throughout the positive-time
patch. But a legitimate odd-Dirichlet boundary completion imposes five
independent compatibility conditions on the metric momenta at fixed
distortion data. The free-momentum Hamiltonian argument cannot simply be
applied to this completion.** This does not establish positive energy;
it identifies the constraint that an unconditional negative-energy proof
would have to solve rather than assume absent.

This result follows the [metric Hessian](native-zorro-real-metric-hessian-2026-10-08.md),
the [real primary reduction](native-zorro-real-packet-and-selection-2026-10-08.md),
and the [imaginary energy theorem](native-zorro-constrained-energy-2026-10-08.md).
It keeps the selected curved comm/symi/symi bosonic I1B realization and its
two stationary coupling branches. The boundary completion below is declared
here; it is not selected by the source draft. Classification:
`SOURCE_NATIVE_ROUTE` within that reconstruction.

```gu-typed-objects
result: universal homogeneous primary cancellation and explicit polarized boundary compatibility chain, including a rank-five obstruction to unrestricted metric momentum variation
carrier: real Clifford one-forms and homogeneous base-metric perturbations on a small metric-fibre patch LAYER=ambient+source-print BRIDGE=declared_canonical_reconstruction CHIRALITY=N/A
pairing: selected action trace/Hodge density, raw first-order Green form, and reduced bulk symplectic form ON=declared_local_product_patch_with_stated_boundary_polarization
real_structure: coefficient-conjugation fixed source slice; odd grades 1,5,9,13 and even grades 2,6,10,14
grading: Clifford parity, homogeneous connection jets, derivative order and five spatial traceless metric polarizations; no rank interpreted as a particle count
action_owner: source-action -- selected I1B bulk functional; explicitly declared polarization boundary term, without source uniqueness or admission credit
target: applicability of the real homogeneous free-momentum energy argument and selected-realization evidence for LT-SM8 and LT-GR6b MAP-TYPE=restriction
```

## 1. The pointwise calculation is a complete tensor identity

At a point put the fibre metric in the standard Lorentz frame and align
the positive ambient time covector with `dt`. The flat observing metric
need not then be the same matrix as the fibre metric. Its homogeneous
Levi-Civita variation is contained in the space

```text
C_i^a_j = C_j^a_i,       tr C_i = 0 for i=1,2,3.       (1)
```

There are 40 torsion-free coefficients and three independent trace
conditions, hence dimension 37. Indeed `tr delta Gamma_i` is proportional
to `q_i` for a homogeneous metric jet. Conversely we need only that the
actual jets are contained in (1), not that every member is realized by
the same observing metric. These are coefficient tensors at a fixed
background; the calculation does not declare an independent affine
connection to be a new physical field.

Both `A2-D0 y` and each potential column applied to `y` are linear in
these coefficients. The probe constructs a complete exact basis of (1),
computes every covariant fibre derivative of `y`, and projects onto every
touched real primary block. It proves

```text
N^T(A2-D0 y)=0,      N^T M_Hodge y=N^T H_a y
                  =N^T H_c y=N^T H_v y=N^T H_w y=0.   (2)
```

Here `D0` includes the time-direction connection even though coefficient
fields have zero coordinate-time derivative. Linearity, constant base
coordinate covariance and nonzero rescaling of the time covector extend
(2) to every actual homogeneous metric jet and every fibre point in the
positive-time patch. The natural background is independent of the value
of a constant observing metric when its connection is zero, so aligning
the fibre frame does not silently identify the two metrics.

The complete 37-by-37 polarized Gram identities are

```text
y^T M_Hodge y = -||F1||^2/16,
y^T H_a y = -(52/3) y^T M_Hodge y,
y^T H_c y = -(4/3) y^T M_Hodge y,
y^T H_v y = y^T H_w y = 0.                            (3)
```

The curvature Gram has rank 27; all 1,369 entries are checked. These
identities therefore include cross terms and are not an inference from
diagonal tests. After `t=t'-y(h,ddot u)`, **no homogeneous metric
acceleration remains in any real distortion primary equation**, and

```text
K_acc(u,u) = -[kappa+(8/3)(10a+c)] ||F1(u)||^2/16.     (4)
```

This is a general coefficient identity on the stated patch of the same
background, not an extension to arbitrary stationary backgrounds. The
predecessor's five-dimensional definite block near
`h0=diag(4,-1,-1,-1)` and both coupling branches follow immediately.

## 2. The action's boundary form is not its skew bulk coefficient

Write the real distortion as `T=O+E`, with odd and even Clifford parity.
Let `K^mu` denote the raw derivative coefficient in
`<T,S(D_B T)>`, so the derivative density is
`T^T K^mu nabla_mu T/2`. Its bulk Euler coefficient is

```text
E^mu = (K^mu-(K^mu)^T)/2.                             (5)
```

Clifford parity makes the diagonal blocks `K_OO` and `K_EE` zero.
It does not make `K` skew. For the conormal in direction 4, the independent
matrix engine gives, with `o=e^0 gamma_0`, `e=e^0 gamma_0 gamma_4`,

```text
K(o,e)=0,       K(e,o)=-2,       E(o,e)=1.             (6)
```

Thus replacing the original boundary form by `T^T E(n) delta T/2`
would drop a real boundary variation. The raw first-order boundary
one-form is `T^T K(n) delta T/2`. Here `n` means the oriented conormal
density in Stokes' formula; no unit normal at a null boundary point is
assumed.

A concrete polarization completion is obtained by adding

```text
B_pol = -1/2 integral_boundary O^T K_OE(n) E.          (7)
```

Integration by parts changes the cross derivative density to
`E^T E_EO^mu nabla_mu O`. The Clifford tensors and trace/Hodge pairing
are parallel for the reference spin connection. There is then no
derivative of the even field, and the remaining distortion boundary
one-form is

```text
Theta_pol = E^T E_EO(n) delta O.                      (8)
```

Choose the odd natural perturbation `o=O-O_nat(g)` to vanish at the
fibre boundary, while the even perturbation is free. Metric variations
are still base fields; their induced `delta O_nat(g)` contribution must
be included in the fibre-integrated metric equation. It is not an
independent arbitrary boundary metric variation. The natural boundary
term depends on `g` through its first jet, so it changes lower-order
metric terms, not the fourth-order bulk matrix (4).

This is a definite variational polarization of the bulk action. It is
additional boundary data, not an assertion that the printed source chose
it or that the associated evolution is well posed. The background's
metric first variation still integrates to zero for compact base tests:
its boundary coefficients are base-translation invariant and contain
base derivatives of the variation. No new stationary source claim follows.

Because `y` has even grade, the change `t=t'-y ddot u` leaves `o=0`
unchanged. **Invariance of the boundary condition under this change is
not invariance under time evolution.**

## 3. The transported compatibility equations

Use the primary reduction from the real-packet owner. By (2), its
homogeneous reconstruction after compensation is

```text
t' = R s,       R = iota - N W^-1 F.                  (9)
```

It contains spatial/fibre derivatives of `s` but no metric acceleration.
The nondegenerate quotient time form and bulk equation have the shape

```text
Omega dot s + L s + J a = 0,       a=ddot u,
Tcal=-Omega^-1 L,       Ucal=-Omega^-1 J,
Bcal s = (P_odd R s)|_boundary = 0.                   (10)
```

These are operator definitions from the exact action and its actual
primary inverse, not invented boundary operators. All coefficients are
time independent at the stationary background. A smooth solution must
satisfy the entire compatibility chain, starting with

```text
C0: Bcal s = 0,
C1: Bcal(Tcal s+Ucal a) = 0,
C2: Bcal(Tcal^2 s+Tcal Ucal a+Ucal j) = 0,  j=dddot u. (11)
```

Higher equations follow by differentiating, including the metric
equation when replacing higher metric derivatives. They are not supplied
merely by the pointwise inverse of `W`.

The nontrivial metric part has rank five. At `s=0`, the even equation of
the original compensated system reads

```text
E_EO(dt) dot o = V_EE y a.                            (12)
```

On the five spatial traceless polarizations at `h0`,

```text
y^T V_EE y = -(9/256) delta G,
delta = kappa-(52a+4c)/3,
-0.401 < delta/kappa < -0.399,                        (13)
```

where `G` is the positive Frobenius Gram. Thus `V_EE y` is injective on
these five polarizations, on either coupling branch, and remains so on
a small fibre neighbourhood. Equation (12) proves that
`Bcal Ucal` has rank five there: if the odd boundary velocity vanished,
its left side would vanish, contradicting (13) for nonzero `a`.
This conclusion uses the full even equation, not just a contraction
mistaken for that equation.

In particular, the data `s=0`, `a!=0` pass every bulk distortion primary
equation but fail `C1`. At `s=0`, `a=0`, one has `dot s=0`; differentiating
(12) shows that a nonzero `j` fails `C2`. The scalar/shift metric blocks
cannot repair this rank-five spin-two failure in a rotation-invariant
fibre patch. The condition arises at the boundary in the same spin-two
sector, not from identifying these tensors with scalar gauge data.

## 4. What this does to the metric momentum

Let `A` be the nondegenerate fibre integral of (4), and put `Q=dot u`.
The acceleration momentum has leading part
`P_Q=A a+J^dag s`. Consequently, at fixed lower-order data,

```text
delta P_u = -A delta j.                              (14)
```

Lower-order terms and the polarization boundary term give affine shifts;
they do not change this derivative with respect to `j`. Substituting
(14) in `C2` gives a rank-five condition on `P_u` at fixed distortion
jets. Therefore the predecessor's operation of holding `s,u,Q,P_Q`
fixed while varying `P_u` arbitrarily **does not stay in this boundary
compatibility domain**. In the zero-distortion family it is explicitly
forbidden by (12)--(14).

This establishes neither semiboundedness nor a successful real-sector
repair. Boundary jets of `s` can themselves vary, and the coupled
Hamiltonian after imposing (11), its higher compatibility conditions,
and a closed evolution domain has not been computed. Those jets may
permit a different unbounded-energy family. A claim of positive energy
would be just as premature as declaring the real escape eliminated.

The earlier conditional Ostrogradsky theorem remains true under its
stated free-momentum hypotheses. The calculation here shows precisely
why those hypotheses are substantive, and why a natural polarization
does not discharge them automatically. The permanent distortion-free
collar obstruction of the predecessor is also preserved; compact test
variations do not by themselves define either completed solution space.

## 5. The bounded endpoint and standing-ledger meaning

The full selected realization already has the unconditional **classical
quadratic compact-core** obstruction in its imaginary packet. The real
restriction is an additional bosonic field selection. The current source
does not supply the common boundary/initial-value domain and propagated
constraint system that would select its physical Hamiltonian. The
specific odd-Dirichlet completion above has the explicit compatibility
constraints (11); it is not justified to drop them and call the remaining
free Hamiltonian the physical one.

Accordingly this road supplies a bounded native-action obstruction,
complete local primary and metric coefficients, and a derived boundary
constraint target. It supplies neither a universal GU no-go nor an
unconditional real-sector kill. Further physical closure requires one
selected domain and its propagated coupled energy, not another bulk
signature scan. No source action-root candidate is admitted by this work.

For `LT-SM8`, the result concerns classical quadratic energy in a
selected bosonic realization. `INHERITANCE_BRIDGE` is a different
statement about a pairing descending to the physical BV/BRST quotient,
including the carrier the row actually tracks. The bridge is not proved
by the two energy signs. Record native-action selected-realization
evidence **bearing on** that condition, with no discharge of it.
For `LT-GR6b`, record the bulk and boundary calculations against its
ghost-free observed Euler demand, retaining the missing observed quotient
and domain. Both rows remain `NEEDS`.

The observation-descent theorem has an independent elementary core:
if `O(x)=O(y)` and `H(x)!=H(y)`, no function `h` obeys `H=h composed with O`.
The imaginary compact families supply this collision for every readout
factoring through the smooth observing-section germ. It is an obstruction
to that proposed observation interface. It does not exclude every closed
internal completion or require an external firewall. Record it as a
bounded observation relevant to firewall criterion 1; leave its verdict
`OPEN` and its reconstruction-choice alternative live.

Applying the claim-indexed doctrine, source ownership, `SC-META-53`,
canon, hypothesis votes, forward-certification stage completion and
prediction/confirmation credit do not change. “First computation” is not
used as a priority claim; “partial stage-relevant evidence” is distinct
from a completed physical-state stage.

## Reproduction

```bash
uv run --no-project --with sympy==1.14.0 python -B tests/channel-swings/native_zorro_boundary_constraint_probe.py
```

The exact finite certificates prove the universal coefficient identities,
raw Green-form control and rank-five factors. The polarization and
compatibility-chain arguments are analytic above. The probe does not
prove existence, propagation or positivity of a completed physical
initial-boundary-value problem. An independent implementation of a
coefficient is not outside review of this boundary argument.
