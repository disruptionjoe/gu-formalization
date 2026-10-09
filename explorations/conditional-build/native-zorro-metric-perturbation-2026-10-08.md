---
title: "The observing-metric response and a leading distortion compensator"
status: active_research
claim_verdict: exact_mixed_variation_and_principal_compensation
doc_type: coupled_perturbation_derivation
created: 2026-10-08
target_claim: NONE-NOT-A-KILL
bears_on: [SC-ACT-06, SC-META-53]
spec_row: SA-U1
canon_verdict_change: none
receipt: lab/process/native-zorro-metric-perturbation.json
probe: tests/channel-swings/native_zorro_metric_perturbation_probe.py
---

# Metric response on the stationary curved branch

The observing metric couples to distortion through **third base derivatives
away from the observing section**. That highest-order term vanishes on
the section. The next, second-order section response is precisely the
ambient Clifford covector obtained from the linearized base Ricci tensor.
These are derivatives of the same selected action and geometry as the
[stationary-background construction](native-zorro-stationary-background-2026-10-08.md).

An observed null transverse-traceless metric polarization gives a useful
test. Its base Ricci variation vanishes, while the off-section cubic
response is nonzero. An explicit grade-two distortion perturbation cancels
that leading response in every Clifford receiver. Thus the purely metric
lift does not intertwine the observed Ricci equation with the ambient
equation, but this failure does not exclude a coupled perturbation. The
compensator has not yet been extended to a solution of the lower-order
equations or to a physical domain.

Classification: `SOURCE_NATIVE_ROUTE`. This differentiates the specified
GU-inspired action; it does not replace it by a conventional metric or
Yang–Mills action. The [routing method](../../lab/methods/source-native-comparator-routing.md)
and claim-indexed doctrine apply. SA-U1/H59 remain open and SC-META-53
remains `UNCERTAIN`; no source polarity or canon grade changes.

```gu-typed-objects
result: mixed metric-to-distortion derivative, observing-section jet and leading compensator
carrier: base symmetric metric perturbation u(x) and ambient real Clifford one-form t(x,h) at the selected stationary curved background LAYER=ambient+source-print BRIDGE=declared_canonical_reconstruction CHIRALITY=N/A
pairing: ambient exterior top-degree scalar Clifford trace and Hodge pairing; fibre-integrated formal adjoint for the base variable ON=declared_local_product_patch
real_structure: real metric and Clifford coefficients; complex Fourier notation only complexifies real linear equations
grading: base derivative order and Clifford grade; no identification of symbol kernel with gauge
action_owner: source-action -- same selected comm/symi/symi I1B, differentiated before observation
target: evaluation of actual mixed Euler coefficients and principal compensation, without a physical reduction MAP-TYPE=evaluation
```

## 1. Variables and exact quadratic structure

Keep the source distinction on draft p44: the observing metric `g` lives
on `X`, while epsilon and the translation/distortion fields live on `Y`.
Dressing removes epsilon from the bulk functional exactly, as proved by
the predecessor. Use local field coordinates

```text
g = g_* + u,
T = T_*(g) + t,
```

where `T_*(g)` is the predecessor's intrinsic radial/projector formula,
with its fixed algebraic coefficients. This is an invertible change of
field coordinates; it does not restrict `t` to that four-coefficient
background family. It depends on the first jet of `g` through the
horizontal splitting. The stationary point is `(u,t)=(0,0)`.

These are formal bulk field coordinates. Any chosen fibre boundary data
must be transported under this differential reparametrization: fixing the
original `T` on a boundary does not mean independently fixing `t` when
`g` varies. No independent Dirichlet conditions on the new variables or
closed physical boundary problem are being asserted.

The formal quadratic Euler system has the structure

```text
C t + A u = 0                      on X x V,
M u + integral_V A_x^dagger t = 0  on X.                 (1)
```

Here `V` is the fixed relatively compact fibre patch of the local action.
`A=D_g E_T(g,T_*(g))` and `C=D_T E_T` are actual derivatives of that
functional. `M` is its pure-base second variation in these field
coordinates. Equation (1) identifies the variational owners; it is not
a claim that all coefficients of `A` and `M` have been evaluated.

**The metric equation is fibre-integrated.** Since the varied metric is
`u(x)`, the same `u` occurs at every `h`. Integration by parts in `x`
therefore produces the fibre integral in (1), with the induced density.
It does not impose one separate metric equation at every fibre point.
Replacing that integral by a section value or by pointwise equations would
change the variational problem. Fibre boundaries and completion of the
formal adjoint still require a domain. Epsilon dressing alone removes
no nonzero dressed distortion fluctuation; a physical diffeomorphism
quotient also needs boundary conditions and the full coupled equations.

For clarity, the exact distortion bilinear form is already explicit.
For a compactly supported receiver `U`, its derivative part is

```text
(1/2) sum_s { <U,S(e^s wedge nabla_s t)>
              - <nabla_s t,S(e^s wedge U)> },
```

and its algebraic part is the Hodge mass plus the cubic Hessian

```text
kappa <U,*t>
+ (1/3) <U,S(t wedge T_* + T_* wedge t)>
+ (1/3) <t,S(U wedge T_* + T_* wedge U)>
+ (1/3) <T_*,S(U wedge t + t wedge U)> .                 (2)
```

In particular, the highest derivative `E(q)` of `C` is unchanged by
the nonzero background, while its lower-order part is not. The calculation
below uses (2)'s actual skew formal derivative, not the printed residual.

## 2. Lifting an observing-metric variation

At the constant base metric `g_*=eta=diag(1,-1,-1,-1)`, replace one base
derivative by a covector `q`. For a symmetric polarization `u`, define

```text
L_i^a_j(q,u) = eta^ab (q_i u_bj + q_j u_bi - q_b u_ij)/2,
C_i(h) = L_i^T h + h L_i.
```

The leading variation of the canonical ambient metric has only mixed
horizontal/vertical entries:

```text
k_iA(q,u;h) = -D_h(C_i(h), A),
k_ij = k_AB = 0.                                        (3)
```

For an exponential bookkeeping variable `z`, the metric perturbation is
`z k exp(z q.x)`. Two further base derivatives in the curvature yield
the `z^3` response. With `Q=(q,0)` and all raised indices taken using
`G_Y`, its Ricci coefficient is

```text
R^(3)_ab = (Q_a Q^c k_bc + Q_b Q^c k_ac
            - Q^2 k_ab - Q_a Q_b tr_G(k))/2.             (4)
```

The trace is zero because (3) is mixed. Applying the selected Shiab to
the spin curvature gives the corresponding Euler covector. Variations of
the operator, mass, cubic term and first-order distortion term have lower
base order. The first-jet change of field coordinates `T_*(g)` also cannot
change this third-order coefficient. Thus (4) determines the actual
highest mixed derivative of the source action.

At `h=eta`, metric compatibility gives `C_i=q_i u`. Consequently
`k=-(Q tensor W + W tensor Q)` for a vertical covector `W`. This is a
pure metric gauge symbol for the ambient curvature, so the entire cubic
curvature coefficient vanishes there. This is a cancellation of a
coefficient at the section, not permission to omit it over the fibre.

## 3. The next section coefficient

To isolate second derivatives, set `delta g=(q.x)^2 u/2` at `x=0`.
Its value and first jet vanish. The probe differentiates the actual
curved metric's Christoffel formula, including both differentiated inverse
metric terms. At `h=eta` it obtains

```text
delta Ric_Y = diag(delta Ric_g, 0_10).                   (5)
```

It also verifies that the covariant derivatives of the moving natural
projectors and unit radial vector have zero variation in this jet. Thus
the derivative term in (2) evaluated on `T_*(g)` adds no second-jet
response at the section. The cubic and mass terms are algebraic and
their values do not vary in this jet. The mixed coefficient is exactly
the selected Shiab applied to the curvature variation in (5).

Varying the observing section itself adds the derivative of the background
Euler field in the displaced fibre direction. That term is zero because
the background Euler field vanishes on the entire patch. Thus evaluating
this linearized response at `h=eta` also gives the moving-section response.

Care is needed with the pairing. Put
`E^nu_mu=(Ric^sharp-Scal/2 I)^nu_mu` in the ambient orthonormal frame.
The Riesz endomorphism is `-E`; the Euler **covector row** at
`e^mu gamma_nu` is `-E^mu_nu`. The extra Hodge/Clifford metric signs
transpose the metric-self-adjoint endomorphism. The probe tests off-diagonal
polarizations as well as diagonal ones; these two arrays cannot be
identified by ignoring the signature.

All ten symmetric polarizations are checked on each of the timelike,
spacelike and null base-covector orbits. Linearity in `u`, quadratic
homogeneity in `q` and Lorentz covariance extend (5) and the section
coefficient to arbitrary real base covectors. Polynomiality extends the
identity to complex Fourier covectors. This still gives a section
coefficient, not a closed physical perturbation operator.

## 4. A null-wave test and its missing normal response

Choose the observed null polarization

```text
q=(1,1,0,0),        u=diag(0,0,1,-1).
```

It satisfies `q^2_eta=0`, `q^i u_ij=0`, `tr_eta u=0` and
`delta Ric_g(q,u)=0`. It is not a base diffeomorphism polarization:
`(q tensor xi + xi tensor q)_22=0` for every `xi`, whereas `u_22=1`.
This is an exact test of the native metric map using the familiar
transverse-traceless tensor, not an imported assertion that it is already
a GU physical graviton.

Along the fibre path `h=diag(1+rho,-1,-1,-1)`, `rho>-1`, formula (4)
has exactly the following nonzero entries and their symmetric partners:

```text
R^(3)_(2,02) = -rho^2/[2(1+rho)^2],
R^(3)_(3,03) = +rho^2/[2(1+rho)^2].                      (6)
```

The labels `02,03` here are symmetric metric-fibre coordinate directions,
not Clifford grades. Both the section value and the first derivative
along this fibre path vanish, but the second normal derivative is
nonzero. Thus the cubic response is invisible to these particular
observational data. No statement about every first normal derivative is
inferred from this one path.

At `rho=3`, the probe uses a rational orthonormal frame and independently
computes curvature from Christoffel coefficients, then applies the actual
Shiab. Eight nonzero grade-one rows remain. They are recorded in the
[exact receipt](../../lab/process/native-zorro-metric-perturbation.json).
Since a null Ricci polarization has this nonzero response, the full
mixed operator cannot factor solely through the observed linearized
Ricci operator under the pure natural-metric lift. This is an operator
intertwining obstruction, not a statement about the final coupled mode.

## 5. A geometric leading compensator

The principal cancellation has a covariant construction wherever the
ambient horizontal covector is non-null. Write `d_b=Q^a k_ab`. Because
`k` is mixed and `Q` is horizontal, `tr_G k=0` and `Q^b d_b=0`. Therefore

```text
k_perp = k - (Q tensor d + d tensor Q)/Q^2
```

is transverse and tracefree, and has the same curvature symbol as `k`.
In an orthonormal frame its symmetric-frame spin Levi-Civita variation is

```text
y_i = sum_(a<b) eta_a eta_b
      (Q_b (k_perp)_ai - Q_a (k_perp)_ib) gamma_a gamma_b / 4.
```

The selected operator satisfies `E(Q)y=S(Q wedge y)` on this transverse
tracefree carrier. The probe evaluates both sides on the complete
90-dimensional transverse tracefree symmetric-metric basis at `Q=e^0`.
Equivariance and homogeneity give every positive-norm covector. Substituting
the rational transverse tracefree projector into the identity and clearing
denominators then gives a polynomial identity: vanishing on that open set
extends it to every non-null `Q`. This is an analytic extension argument
for exact coefficient identities, not a physical-state completeness claim.

Thus the leading curvature forcing has a natural distortion compensator
where `Q^2 != 0`. The projection is essential: the unprojected spin
connection variation has four extra Euler rows in the explicit test below.
Those rows come from the formal adjoint and are absent from the raw
curvature contraction. This retains the failed unprojected construction
as an exact control.

The division by `Q^2` is a real limit on this construction. It is not an
inverse on the null locus, a global fibre domain, or a license to remove
null modes. Regularity across the characteristic fibre locus remains a
separate obligation.

### A sparse rational representative

In that same rational frame at `rho=3`, `q_frame=(1/2,1,0,...,0)`.
Write a coefficient as `(form_index, Clifford_mask)`. The grade-two
one-form `y` has these eight nonzero coefficients:

| Component | Coefficient |
| --- | --- |
| `(0,260)` | `9/32` |
| `(2,257)` | `-9/32` |
| `(0,520)` | `-9/32` |
| `(3,513)` | `9/32` |
| `(0,4100)` | `-27/32` |
| `(2,4097)` | `27/32` |
| `(0,8200)` | `27/32` |
| `(3,8193)` | `-27/32` |

Using the actual first-order Euler coefficient from (2), direct exact
evaluation against **all** possible receivers gives

```text
E(q) y = A_3(q) u.                                      (7)
```

Therefore `t=-z^2 y exp(z q.x)` cancels the metric source at order `z^3`
in the first equation of (1). The identity is a frozen coefficient
statement at the declared fibre point, not an integrable fibre profile or
a complete mode. The order-three metric source covector has grade one,
so it also annihilates this grade-two `y`. In particular the formally
highest cross contribution to the second equation of (1) vanishes by
Clifford parity. This does not evaluate its remaining metric or distortion
terms, boundary terms, or constraints.

Four base-diffeomorphism polarizations are exact controls: their cubic
response vanishes at the off-section point. Analytically their lifted
connection has `L_i=q_i L`, so (3) is a pure ambient gauge symbol for
every fibre metric. The nonzero response in (6) is therefore not an
artifact of confusing a pure base gauge polarization with the chosen
transverse-traceless one. Conversely (7) is the concrete reason that (6)
cannot be promoted to an exclusion of that coupled polarization.

## 6. Evidence and remaining work

The probe passes 19 grouped exact checks, including the 30 complete
second-jet polarization calculations and 90 transverse tracefree metric
controls. It verifies (3)--(7), the moving field jets, the signed covector,
the geometric compensation identity and all receiver rows of the sparse
compensator. No finite-difference or small-residual conclusion is used.

```bash
uv run --no-project --with sympy==1.14.0 python -B tests/channel-swings/native_zorro_metric_perturbation_probe.py
```

The next step is to compute the off-section second-order coupling and
the pure-base Hessian `M`, then solve the lower-order distortion and
fibre-integrated metric equations on a common domain. A completion of
`y(h)` must also control normal derivatives and boundary conditions.
Only that coupled system can identify propagating constraints, gauge
classes and a physical energy form. No conserved positive physical
pairing or semibounded Hamiltonian has been constructed here.
