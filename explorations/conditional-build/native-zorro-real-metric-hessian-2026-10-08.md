---
title: "Pure metric Hessian and real-packet acceleration in curved I1B"
status: active_research
claim_verdict: exact_bulk_hessian_and_nonzero_reduced_acceleration_with_conditional_hamiltonian_consequence
doc_type: native_action_metric_hessian_result
created: 2026-10-08
target_claim: NONE-NOT-A-KILL
bears_on: [SC-ACT-06, SC-META-53]
spec_row: SA-U1
canon_verdict_change: none
receipt: lab/process/native-zorro-real-metric-hessian.json
probe: tests/channel-swings/native_zorro_real_metric_probe.py
---

# The real restriction has a surviving metric-acceleration term

> **Subsequent boundary result:** the
> [boundary-constraint calculation](native-zorro-boundary-constraints-2026-10-08.md)
> extends the bulk identity and derives a rank-five momentum compatibility
> condition for a declared odd-Dirichlet completion. The independent-momentum
> hypothesis below does not hold automatically on that domain. Its completed
> real-sector energy remains open.

**The pure-base Hessian is computable. After the third-time-derivative
compensation and all distortion primary equations, its spatial traceless
metric-acceleration block is nonzero and nondegenerate near an explicit
fibre point, on either stationary coupling branch.** This advances the
[real-packet reduction](native-zorro-real-packet-and-selection-2026-10-08.md)
beyond its previously unspecified pure-base operator. It does not yet
supply a completed physical real-sector Hamiltonian. A precise conditional
Hamiltonian consequence, and the boundary condition still needed to apply
it, appear in section 4.

The action, curved metric bundle, Shiab operator and background are those
of the [stationary construction](native-zorro-stationary-background-2026-10-08.md).
The complete mixed operator is owned by the
[algebraic reduction](native-zorro-algebraic-reduction-2026-10-08.md).
The independently certified imaginary-packet energy theorem remains
unchanged. Classification: `SOURCE_NATIVE_ROUTE` within the same declared
reconstruction; no conventional Yang--Mills or Einstein action is substituted.

```gu-typed-objects
result: exact natural pure-base Hessian and complete distortion-primary acceleration certificate, with a conditional homogeneous Hamiltonian implication
carrier: conjugation-even real Clifford one-forms and base Lorentz-metric variations on a relatively compact metric-fibre patch LAYER=ambient+source-print BRIDGE=declared_canonical_reconstruction CHIRALITY=N/A
pairing: selected trace/Hodge action Hessian; fibre integration retained; spatial Frobenius form only normalizes five test polarizations ON=declared_local_product_patch
real_structure: source anti-involution slice with real grades 1,2,5,6,9,10,13,14; imaginary packet set to zero in this calculation
grading: base derivative order, Clifford parity, time kernel and spatial rotation representations; no raw rank interpreted as a particle count
action_owner: source-action -- selected comm/symi/symi bosonic I1B functional at both certified nonzero coupling branches
target: pure-base operator and real acceleration after distortion primary reduction; physical boundary completion and global evolution not inferred MAP-TYPE=restriction
```

## 1. The natural action reduces to two curvature contractions

Use symmetric fibre coordinates `h`, observing metric `g`, and

```text
D_h(A,B) = tr(h^-1 A h^-1 B) - tr(h^-1 A) tr(h^-1 B)/2,
theta = dh - (Gamma(g)^T h+h Gamma(g)) dx,
G_Y = h_ij dx^i dx^j + D_h(theta,theta).
```

The horizontal coframe change has determinant one. In the ten symmetric
matrix coordinates, `det D_h = -64 (det h)^-5`; hence

```text
mu(h) = sqrt(abs(det G_Y)) = 8 abs(det h)^-2.           (1)
```

In particular, this density is independent of `Gamma(g)` and `g` at fixed
`h`. Let `r=(0,h/2)`, with `G_Y(r,r)=-1`, and put

```text
F_ij = R(g)_ij^T h+h R(g)_ij,
||F||^2 = h^ik h^jl D_h(F_ij,F_kl),
K = (11a+c)/2.
```

Here the norm notation denotes this indefinite contraction. It is not a
positive norm. The trace of `h^-1 F_ij` vanishes because the Levi-Civita
curvature has zero endomorphism trace. The adapted-frame Koszul formula
gives

```text
Scal(G_Y) = -10 + h^ij Ric(g)_ij - ||F||^2/4,
Ric(G_Y)(r,r) = -1/4.                                 (2)
```

For clarity, the quadratic-curvature part can be checked without appealing
to a submersion formula with different hypotheses. In an orthonormal
adapted frame, the curvature-dependent connection correction is

```text
delta_i(j) = F_ij/2,
(delta_i)^k_v = (delta_v)^k_i = -eta_kk eta_vv F_ik^v/2.
```

Its quadratic curvature is `[delta_i,delta_j]-F_ij^v delta_v`.
Contracting gives `-||F||^2/4`, with zero radial Ricci correction.
The probe proves this polynomial identity in all 54 independent
horizontal-two-form/traceless-vertical components. The linear connection
jet contributes `h^ij Ric(g)_ij`, by the predecessor's full off-section
Ricci identity; the third-base-derivative mixed Ricci term has zero scalar
trace. There are no higher curvature powers in the connection metric.
This proves the first identity in (2) in observing normal coordinates,
and covariance supplies general coordinates. Alternatively the radial
identity follows from `nabla r=P_H/4`, `div r=1`, and
`tr((nabla r)^2)=1/4`; `r` is geodesic and its dual one-form is closed.

The natural distortion has grade-one part `a I+(c-a)P_r`.
Pairing it with `S(F_B)=-Einstein(G_Y)` gives

```text
<T_nat,S(F_B)> = K Scal(G_Y)+(c-a) Ric(G_Y)(r,r).       (3)
```

Its grade-two part has no curvature pairing. The mass and cubic
contractions of the natural field are constant. In the first-order
term the only possible curvature correction is proportional to
`gamma_r gamma([delta,P_H])`. Its pairing with each grade-one background
direction vanishes on all 54 independent components, as checked exactly.
The grade-one natural field itself has no curvature-dependent derivative,
because `nabla r=P_H/4` is unchanged. Consequently

```text
I(g,T_nat(g)) = integral mu(h) [C + K h^ij Ric(g)_ij
                                      - K ||F||^2/4] dx dh,          (4)
```

where `C` is independent of `g`. This identity concerns the selected
natural coordinates, not the pure Einstein--Hilbert functional on the base.

## 2. The pure-base Hessian, including its lower-order part

At `g=eta`, let `L_i(u)=delta Gamma_i[u]`, set
`F1_ij=(partial_i L_j-partial_j L_i)^T h
          +h(partial_i L_j-partial_j L_i)`, and define
`Q^ij=integral_V mu(h) h^ij dh`. Base variations have compact support;
the fibre patch is fixed. In (4), the divergence terms in `Ric(g)`
integrate to zero in the base alone. Thus the **Hessian**, twice the
quadratic Taylor coefficient, is

```text
M[u,u] = 2K integral_X Q^ij
          (L^a_ab L^b_ij - L^a_jb L^b_ai) dx
         - K/2 integral_(X x V) mu(h) ||F1(u)||^2 dx dh.              (5)
```

This is the complete pure-base bulk Hessian in these coordinates. Its
orders are two and four; it has no order-zero, one or three term. No
fibre integration by parts was used to obtain it. An independent
coordinate-metric quadratic-jet calculation checks the curvature-square
coefficient at three fibre metrics, timelike and null covectors, and
three polarizations (18 exact controls).

Fixing `V` is significant. A general base diffeomorphism also changes the
fibre coordinates and its boundary. One cannot silently replace `Q^ij`
by `sqrt(abs(det g)) g^ij`, or import the ordinary Einstein constraints.
For example, for homogeneous time dependence and
`Q=diag(Q0,Qs,Qs,Qs)`, the two-derivative density includes
`-(Q0+Qs) dot u00 tr(dot u_sp)/4`, before multiplication by `K`.
The lapse is not automatically an algebraic multiplier in that expression.
The full lifted variation and its boundary domain determine the appropriate
constraint statement.

## 3. Compensate before evaluating the acceleration coefficient

Write `C_R=E^mu nabla_mu+V`, and `A=A3+A2` for the full mixed operator.
For time covector `q=dt` with positive ambient square, the predecessor
constructs a grade-two `y(h,u)` satisfying `A3(q)u=E(q)y(h,u)`.
In homogeneous time-dependent fields put

```text
t_R = t' - y(h,ddot u).                               (6)
```

This is an invertible differential change of variables with `u` unchanged;
its inverse adds the same metric acceleration. It removes the third-time
derivative from the mixed term. The compensator is built from the
transverse, trace-free mixed metric lift, not the unprojected spin connection.
The latter already failed the earlier primary-symbol check.

Let `N` span the real time kernel and `W=N^T V N`. The coefficient of
`ddot u` in its new primary source is

```text
b_N(u) = N^T [A2(u)-D_0 y(u)-V y(u)],                 (7)
```

where `D_0 y=E^mu nabla_mu y` is evaluated with zero coordinate-time
derivative of the coefficient field `y(h,u)`. All connection terms,
including the time-direction connection, remain in `D_0`.
The derivative of `y` in the fibre is essential. Freezing it gives the
wrong operator. Clifford parity implies `y^T A2=0` and
`y^T E^mu nabla_mu y=0`. After recovering every primary variable,
the pure metric acceleration Hessian is therefore

```text
K_acc(u,u) = M4(u,u)+y(u)^T V y(u)-b_N(u)^T W^-1 b_N(u).             (8)
```

This is a coefficient of the **coupled reduced action**. It is not a
frozen-metric sign scan.

An exact fixture is

```text
h0 = diag(4,-1,-1,-1), q=dt, u0=diag(0,0,1,-1).
```

At this point `||F1(u0)||^2=9/8`. Computing the full covariant derivative
of the compensator, including the one-form and endomorphism connections,
gives `N^T(A2-D_0 y)=0` and `N^T V y=0` separately.
Every receiver in every touched quartet block is retained, including
higher Clifford grades. Thus the primary correction in (8) is exactly
zero here. The other contractions are

```text
y^T M_Hodge y = -9/128,
y^T H_a y = 39/32,     y^T H_c y = 3/32,
y^T H_v y = y^T H_w y = 0,
K_acc(u0,u0) = -9/128 [kappa+(8/3)(10a+c)].             (9)
```

The probe checks all five spatial traceless polarizations and all their
cross terms. With `G_ij=tr(u_i u_j)`, their full matrix is

```text
K_acc = -9/256 [kappa+(8/3)(10a+c)] G.                 (10)
```

An independent occupation-state matrix implementation reproduces all
three nonzero compensator Gram matrices. Rational interval arithmetic
on the already isolated stationary root proves

```text
3.083191968 < 1+(8/3)(10 alpha+beta) < 3.083191980,
a=kappa alpha, c=kappa beta.                          (11)
```

These decimal bounds are outward weakenings of the exact rational
interval in the receipt. Reversing `kappa,a,c` changes the sign of (10)
without making it degenerate. Lapse and all three shift polarizations
have zero acceleration source at `h0`; this last pointwise fact is not
used to assert a full lapse/shift constraint theorem.

All forty real primary potentials are invertible near `h0`, by the
predecessor and frame covariance. Hence (8) is smooth there. On a small
enough fibre neighbourhood, its restriction to the fixed five-dimensional
spatial traceless space stays definite. Its fibre integral with the
positive density (1) is consequently nondegenerate. This step uses
continuity of the exact matrix, not an unbounded numerical scan.

## 4. The conditional Hamiltonian consequence and the remaining boundary

Here is a precise consequence, without assigning an unproved physical
domain. Consider the spatially homogeneous quadratic problem, for example
on a flat spatial torus, over a sufficiently small rotation-invariant
fibre neighbourhood of `h0`. Require a boundary/variational completion
that admits these five metric coordinates with independent position and
velocity, permits the change (6) and primary recovery, and leaves the
remaining distortion time form nondegenerate in this sector. Require
also that boundary terms neither change the acceleration matrix (10)
nor impose an additional constraint on its canonical momentum.

Under these explicit hypotheses the homogeneous spatial-traceless block
has energy unbounded in both directions. The proof is short. Spatial
rotation invariance separates its spin-two block from the metric scalar
and vector blocks; scalar lapse and vector shift equations cannot supply
a linear spin-two constraint. All distortion multipliers have already
been recovered. In this block put `Q=dot u`. The reduced Lagrangian has
the form

```text
L = 1/2 s^T Omega dot s + 1/2 dot Q^T A dot Q
        + dot Q^T J(s,u,Q) + L0(s,u,Q),                (12)
```

with `Omega` nondegenerate and `A` the nondegenerate fibre integral of
(8). The `s` momentum constraints are second class with bracket `Omega`.
The `Q` momentum solves uniquely for `dot Q`; it supplies no constraint
on the momentum `P_u`. The Hamiltonian contains `P_u dot u=P_u Q`.
At fixed nonzero `Q`, varying `P_u` gives either energy sign without
bound. The sign of `A`, and therefore the coupling branch, does not
remove this Ostrogradsky mechanism. This is a direct canonical argument,
not an inference from a negative entry in the unreduced Hessian.

The domain hypotheses must not be erased. The original stationary
calculation uses compact interior distortion variations and independent
base variations. Since `u=u(x)`, its compensator `y(h,ddot u)` need not
vanish on the fibre boundary. Consequently compact support of `t_R`
does **not** become compact support of `t'` under (6). Fibre-boundary
conditions and their preservation can restrict the data in (12).
Likewise a fixed fibre boundary need not respect the full base gauge
group. This is the specific unresolved step between the certified bulk
coefficient and an unconditional physical real-packet energy theorem.
The imaginary-packet compact-core theorem did not face this issue
because its metric variation vanishes identically.

There is also a concrete obstruction to a tempting compact-support
completion. Suppose a homogeneous spatial traceless metric perturbation
is accompanied by distortion that vanishes on a fixed open fibre collar
for a time interval. There the distortion equation reduces to
`A3(h) dddot u+A2(h) ddot u=0`. The third-order source has only mixed
horizontal/vertical tensor entries. Its horizontal block is zero. The
second-order source has an injective horizontal block on the five
spatial traceless polarizations: at `h0` its spatial block is
`-ddot u_sp/2`. This rank persists in a sufficiently small neighbourhood.
The horizontal equation therefore forces `ddot u_sp=0`. A compactly
supported-in-time metric perturbation in this class is consequently zero.
The probe checks the zero block and rank exactly. Thus requiring a
permanent distortion-free fibre collar does not give a free propagating
real metric phase space: it excludes these accelerated metric data.
Allowing the forced distortion response at the boundary is a different
completion and must be specified. Compact *test variations* in the
stationary proof did not themselves impose this restriction on all
solutions.

Thus merely discarding the imaginary packet has not established a positive
sector: the real bulk problem now has the explicit obstruction (10) to
a nondegenerate homogeneous completion of the stated kind. A successful
alternative must demonstrate an actual further constraint or admissibility
condition, not assume it. This does not prove that every possible
source-compatible completion, shielding mechanism or background fails.

## 5. Which proposed extrapolations survive the source and algebra checks

The two imaginary witnesses differ in ambient derivative signature, so
that signature explains their opposite Hodge-mass signs in this fixture.
It does not prove background independence. In the independent matrix
engine, take the different real background component `e^0 gamma_1`.
Its unphased cubic Hessian column on `e^0 gamma_0 gamma_4 gamma_10` has two
nonzero time-kernel coordinates, both `-4/3`. Multiplying both imaginary
test directions by `i` reverses that sign and preserves nonvanishing.
Thus the four stationary-background
zero columns are not a tensor identity for arbitrary backgrounds.
This control is not claimed to be another stationary solution. No
background-general energy conclusion follows from it in either direction.

The [source transcript](../../lab/sources/transcripts/toe-weinstein-gu-40-years.md)
discusses ultrahyperbolic signature at 01:16:13, the unresolved spectral
problem and compact shielding at 01:22:30, and Bars at 01:25:01.
Bars' specific `Sp(2,R)` constraint/gauge construction is an example of
additional dynamical structure, not a proof that an arbitrary multiple-time
action has it; see [Bars' primary construction](https://arxiv.org/abs/hep-th/9810025).
Neither the imaginary theorem nor (10) is a test of Weinstein's actual
`Spin(6,4)` shielding proposal.

Fermionic closure is a separate question. The
[rendered source extraction](../../lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md)
records the candidate current in (9.18), including
`bar-nu zeta + bar-zeta nu`, and explicitly independent barred and
unbarred classical fields. It does not fix a unique fermion operator,
adjoint reality condition or completed current domain. For a specified
coupling with the usual nondegenerate matrix-current pairing, there is a
simple obstruction: the central `iI` direction belongs to the discarded
packet, and its variation contains `i bar-nu(zeta)`. Independent spinor
fields can make this bilinear nonzero while setting the other current
terms to zero. Thus this current polynomial does not identically preserve
the real restriction. That conditional algebraic statement does not prove
nonzero current for every fermion solution, select a reality condition,
or prove the same conclusion for every source-admitted coupling. No
family, chirality or particle count is inferred.

Under the [claim-indexed doctrine](../claim-indexed-verdict-doctrine-2026-08-12.md),
the demonstrated energy concern binds the selected I1B reconstruction and
the imaginary compact core. The new real result has the additional
domain qualifications above. Neither result validates a universal
complexification argument or decides GU as a whole. `SC-META-53` remains
`UNCERTAIN`; no canon or hypothesis vote changes. An independent coefficient
implementation is not outside research review.

## 6. Reproduction and next decisive calculation

```bash
uv run --no-project --with sympy==1.14.0 python -B tests/channel-swings/native_zorro_real_metric_probe.py
```

The receipt binds exact checks to their native dependencies. Analytic
identities (4)--(8), continuity and the conditional canonical argument
are proved above; the probe does not certify a global PDE domain.
The next decisive task is to derive and propagate a definite transported
fibre-boundary/metric constraint system and decide whether it admits the
independent spin-two momenta of (12). If it does, the conditional energy
conclusion applies. If it excludes them, identify the actual constraint
and verify its closure and source status. Merely recalculating the
unconstrained Hessian would not settle this remaining question.
