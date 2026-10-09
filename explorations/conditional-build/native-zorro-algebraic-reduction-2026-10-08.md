---
title: "Complete mixed derivative and algebraic distortion reduction on the curved I1B branch"
status: active_research
claim_verdict: exact_formal_bulk_even_sector_elimination
doc_type: coupled_perturbation_derivation
created: 2026-10-08
target_claim: NONE-NOT-A-KILL
bears_on: [SC-ACT-06, SC-META-53]
spec_row: SA-U1
canon_verdict_change: none
receipt: lab/process/native-zorro-algebraic-reduction.json
probe: tests/channel-swings/native_zorro_algebraic_reduction_probe.py
---

# Algebraic reduction at the stationary curved background

**Every even Clifford distortion coefficient can be eliminated algebraically
from the linearized bulk equations at the selected stationary background.**
The coefficient map being inverted has no derivatives. Its invertibility
is certified at the exact algebraic background, so this step requires no
Green function, choice of Fourier inverse or division by a covector norm.

The observing-metric coupling is also now determined at every fibre point:
its third-order term is the predecessor's mixed curvature symbol, its
second-order term is the ambient Einstein covector of the base Ricci
variation, and its lower-order terms vanish. All its Clifford receivers
have grade one. These statements reduce the actual selected equations;
they do not yet give a physical state space or energy theorem.

Use the action, canonical connection metric and stationary algebraic branch
of the [background construction](native-zorro-stationary-background-2026-10-08.md),
with the formal bulk field coordinates of the
[mixed-variation calculation](native-zorro-metric-perturbation-2026-10-08.md).
Classification: `SOURCE_NATIVE_ROUTE`, within that declared reconstruction.
The source brackets and metric realization are still specified choices,
not a claim that the draft uniquely selects them. The
[routing method](../../lab/methods/source-native-comparator-routing.md),
[claim-indexed doctrine](../claim-indexed-verdict-doctrine-2026-08-12.md)
and [status consistency method](../../lab/methods/claim-status-consistency.md)
apply. No source polarity, hypothesis vote or canon status changes.

```gu-typed-objects
result: complete mixed metric derivative and invertible even distortion potential at the selected stationary branch
carrier: base symmetric metric perturbations and ambient Clifford one-forms on the canonical curved metric bundle LAYER=ambient+source-print BRIDGE=declared_canonical_reconstruction CHIRALITY=N/A
pairing: exterior top-degree scalar Clifford trace and induced Hodge form; metric adjoint includes fibre integration ON=declared_local_product_patch
real_structure: source phased anti-involution slice with real grades 1,2 mod 4 and imaginary grades 0,3 mod 4; complexification used only to classify coefficient blocks
grading: Clifford parity and grade, base differential order and coefficient XOR labels; raw coefficient dimensions are not physical state counts
action_owner: source-action -- the selected comm/symi/symi I1B functional, including its actual cubic Hessian and kappa-over-two mass term
target: exact formal bulk elimination and gauge-symbol identities at the specified algebraic stationary background MAP-TYPE=evaluation
```

## 1. Real action and variables

Keep the source's phased real adjoint slice displayed on draft p42. An
intrinsic description uses the conjugate-linear Clifford anti-involution
`J(gamma_a)=-gamma_a`, `J(AB)=J(B)J(A)`. Its anti-fixed subspace is

```text
U = {Z : J(Z)=-Z}
  = i Lambda^0 + Lambda^1 + Lambda^2 + i Lambda^3
    + i Lambda^4 + Lambda^5 + Lambda^6 + ... .           (1)
```

Here all exterior-grade coefficient spaces on the right are real before
the displayed factors of `i`. This algebraic involution is not a positive
Hilbert adjoint. In particular, the word "real" below does not imply a
positive norm. The background uses real grades one and two, so it belongs
to (1) without changing any of its certified coefficients.

If `A,B` belong to `U`, both `[A,B]` and `i{A,B}` belong to `U`.
The Clifford coefficients of `Phi_1` and `Phi_2` also belong to `U`.
Consequently the chosen `comm/symi/symi` Shiab maps `U` coefficients to
`U` coefficients. Hodge acts on exterior indices and has real coefficients.
The spin connection preserves `U`, its curvature is in `U`, and the
coefficients of `T wedge T` are commutators in `U`. Finally,

```text
conjugate(tr(AB)) = tr(J(AB)) = tr(BA) = tr(AB),
```

where `tr` is the scalar Clifford trace. Thus the selected action and its
quadratic variation are real on this slice. This supplies a real
variational problem; it does not supply a positive physical pairing.

Write `g=g_*+u` and `T=T_*(g)+t`, using the predecessor's natural projector
formula with its fixed background coefficients. Split `t=o+e` into odd
and even Clifford grades. This is the full distortion carrier, not a
restriction to the four background coefficients. Epsilon is removed by
the predecessor's exact dressing identity.

There is a further exact linearized decomposition. Ordinary coefficient
conjugation preserves `U`, fixes the background and fixes the selected
action: Shiab contains two factors of `i` in its second term and otherwise
has real coefficients. On the real slice, `I(g,bar T)=I(g,T)`.
Its Hessian therefore has no cross term between the two eigenspaces

```text
R = Lambda^1 + Lambda^2 + Lambda^5 + Lambda^6 + Lambda^9
    + Lambda^10 + Lambda^13 + Lambda^14,
J = i(Lambda^0 + Lambda^3 + Lambda^4 + Lambda^7
      + Lambda^8 + Lambda^11 + Lambda^12).              (1a)
```

The metric is in the plus eigenspace, so the entire `J` packet is a
closed, metric-decoupled linearized distortion sector. After the even
elimination below, its remaining odd grades are `3,7,11`, and its even
grades `0,4,8,12` are recovered algebraically. This is a symmetry of the
actual Hessian, not an assumed truncation by Clifford grade. It does not
claim that `J` alone is a closed nonlinear sector. Nor does it remove its
constraints, supply its observation map or determine an energy sign.

## 2. The complete second-order mixed coefficient

At a point with `Gamma(g_*)=0`, denote a connection first jet by
`N[k][i]^a_j=partial_k Gamma_i^a_j`. First allow the larger linear class

```text
N[k][i]^a_j = N[k][j]^a_i,
tr N[k][i] = tr N[i][k].                                (2)
```

These are torsion-free jets with closed trace. Levi-Civita first jets are
in this class because `tr Gamma=d log sqrt(|det g|)`. Conditions (2) are
also preserved by constant base-coordinate changes.

For an arbitrary fibre point `h`, let `C_i=L_i^T h+h L_i`. The connection
metric variation associated with `L` is
`k_iA=-D_h(C_i,A)`, with its other entries zero. To compute the coefficient
of `N`, the probe differentiates this formula in each fibre direction and
then differentiates the actual curved Christoffel connection. Both inverse
metric derivative terms are retained. The result is

```text
delta Ric_Y = diag(Ric(N), 0_10),
Ric(N)_ij = sum_k (N[k][j]-N[j][k])^k_i.                 (3)
```

The projector and radial terms must be varied too. If `r=(0,h/2)` and
`P_H,P_r` are the natural horizontal and radial projectors, then

```text
delta(nabla P_r)=0,       delta(nabla r)=0,
delta(nabla T_*) = (p-w) gamma(r) gamma(delta(nabla P_H)),
p=-v/8.                                                (4)
```

Off the observing section, `delta(nabla P_H)` need not vanish. Nevertheless
its **full formal first-order Euler response** vanishes. Equation (4)
therefore contributes no second-order mixed covector. The mass and cubic
terms contribute none either: this jet has zero connection value, hence
zero pointwise variation of the metric, natural background field and
algebraic operations. The remaining response is precisely Shiab applied
to the curvature in (3), independently of `a,c,v,w,kappa`.

For completeness, the finite certificate spans the entire class (2),
rather than sampling metric polarizations. There are 160 unconstrained
torsion-free connection first-jet coefficients. The map to `tr N` is onto
the 16-dimensional space of matrices, with right inverse

```text
R(V)[k][i]^a_j = (delta_i^a V_kj + delta_j^a V_ki)/5.
```

Projecting each of the 160 elementary generators by `N -> N-R(tr N)`
spans its 144-dimensional kernel. Adding the ten lifts of symmetric `V`
spans the remaining closed-trace directions. The resulting 170 generators
span a 154-dimensional space. For every generator, the probe checks (3),
the radial identities (4), cancellation in every derivative receiver, and
the signed Shiab covector. Nonzero horizontal-projector variations are
included in these checks.

These calculations are made at `h=eta`. Any Lorentzian `h` is taken there
by a constant `GL(4)` congruence; the connection metric, projectors and
conditions (2) transform naturally. Because the calculation allowed all
jets (2), it did not fix an observing metric value that could obstruct that
transport. Thus the identity holds at every fibre point. Six additional
exact anisotropic and sheared controls check the coordinate implementation
away from `h=eta`.

In an ambient orthonormal frame put
`E=Ric^sharp-tr(Ric^sharp) I/2`, using (3). The Euler covector row on
`e^mu gamma_nu` is `-E^mu_nu`. This is the transposed array relative to
the Riesz endomorphism; the signature signs are not omitted.

## 3. No hidden lower-order metric coupling

At the constant observing metric, the coefficients are independent of
base position. The dependence of the ambient geometry on `g` is through
its Levi-Civita connection. Curvature involves at most third derivatives
of `g`, and the background's covariant derivative at most second
derivatives. Therefore the mixed operator has base order at most three.

A constant variation of `g` does not change its connection, so the
zeroth-order coefficient vanishes. Any first connection jet value
`delta Gamma_i^a_j`, symmetric in `i,j`, can be generated by the second
jet of a base coordinate change with identity first jet. The natural
background Euler field vanishes identically on the fibre patch. Its
variation under this coordinate change is consequently zero. This
proves that the first-order coefficient vanishes as well.

Combining (3)--(4) with the predecessor's third-order result gives

```text
A u = A_3(partial_x)u + A_2(partial_x)u,                (5)
A_0=A_1=0,
A_2 : delta Ric_Y = diag(delta Ric_g,0),
A_3 : delta Ric_Y = Ric_principal(G_Y,k(q,u),Q),
Q=(q,0),
```

followed in both cases by the signed Einstein/grade-one covector map.
Equation (5) specifies the full mixed operator in the fixed background
chart, not just its symbol of highest order. All receivers have grade one.
In particular, even distortion has no direct mixed metric source.

There is a useful exact bulk gauge identity. For a base vector field
`xi`, naturality of `T_*(g)` gives

```text
delta_xi u = Lie_xi g_*,       delta_xi t = Lie_xi t_* = 0.
```

The linearized dressed distortion is therefore invariant under this base
diffeomorphism redundancy. On symbols,
`u=q tensor xi_flat + xi_flat tensor q` has zero base Ricci, and
`L_i=q_i (xi tensor q)` makes its ambient metric lift a pure gauge
curvature symbol. Thus `A(delta_xi g_*)=0` at every fibre point, checked
symbolically for arbitrary `q,xi`. Epsilon redundancy also has zero
dressed distortion. These identify known bulk gauge directions; they do
not define boundary gauge charges or prove that no other degeneracies exist.

## 4. The even potential is invertible

Shiab reverses Clifford parity. Hence the formal derivative term in the
distortion Hessian reverses parity, including the spin connection terms.
The cubic Hessian with the grade-two part of `T_*` reverses parity as
well. The diagonal parity blocks come entirely from the mass and the
grade-one background

```text
T_1 = a gamma((I-P_r).) + c gamma(P_r .).
```

For arbitrary one-form variations `U,V`, the latter Hessian is

```text
H_T1(U,V) = ( <U,S(T_1 wedge V+V wedge T_1)>
             + <V,S(T_1 wedge U+U wedge T_1)>
             + <T_1,S(U wedge V+V wedge U)> )/3.         (6)
```

This is the second derivative of the cubic **action**, not a derivative
of the printed residual. The even potential is
`V_e(U,V)=kappa<U,*V>+H_T1(U,V)`.

In the rational orthonormal frame, index `10` is `r`. For each odd-weight
Clifford mask `lambda`, define the 14 coefficient directions

```text
U_mu = e^mu gamma_(lambda XOR {mu}),       mu=0,...,13. (7)
```

The diagonal tautological forms and `T_1` preserve this XOR label in the
paired Hessian. Thus (7) gives all even coefficients in independent
14-dimensional blocks. The group of complex orthogonal transformations
fixing `r` carries any label to a representative specified only by its
weight and whether it contains `r`: permutations of the other 13 axes,
with factors of `i` when exchanging opposite signatures, suffice. The
formula (6) is tensorial, so determinant nonvanishing transfers between
these representatives. This use of complexification proves an algebraic
identity; it does not change the chosen physical real slice.

There are fourteen representatives: weights `1,3,...,13`, with and without
the radial index. Each block further separates the two Clifford grades
`weight-1` and `weight+1`. Multiplying each grade by the phase in (1)
therefore changes the corresponding real potential block only by an
overall real sign. Its invertibility is unchanged and its coefficients
on the source slice are real.

The probe constructs all fourteen Hessians from (6), factors their exact
determinants, and certifies every factor at the stationary branch. For
example, the weight-one block containing `r` has determinant
in the unphased real Clifford basis

```text
-kappa (44a+12c-3kappa)^12 (528a+40c+3kappa) / 1594323. (8)
```

Across the fourteen determinants there are 39 distinct nonconstant factors.
Every factor is homogeneous in `(a,c,kappa)`. Substitute
`a=kappa alpha(w)` and `c=kappa beta(w)`, using the background's exact
degree-ten algebraic root and positive `kappa`. After extracting its
nonzero power of `kappa`, every factor has a rational interval excluding
zero on

```text
227427945967/10^12 < w < 227427945969/10^12.
```

All determinant formulas, label multiplicities and outward rational
factor bounds are in the [receipt](../../lab/process/native-zorro-algebraic-reduction.json).
The blocks cover `14 * 2^13 = 114688` real coefficient directions.
This is a count of raw one-form/Clifford coordinates, not a count of
particles, propagating polarizations or physical states.

Thus `V_e` has an exact smooth pointwise inverse on the stationary fibre
patch. No covector occurs in its determinant. Its inverse therefore exists
also at the ambient null locus where the predecessor's particular
principal compensator formula required division by `Q^2`.

## 5. What the elimination actually gives

On compact interior test fields, with the action's formal adjoints, the
full distortion Hessian has the form

```text
C = [ V_o   D   ],
    [ D^dag V_e ],                                      (9)
```

where `V_o,V_e` are algebraic and `D` is first order on `Y`. Its derivative
part is the actual formally antisymmetrized Shiab coefficient; its
algebraic off-diagonal part is the cubic Hessian with `T_2`. No lower
connection terms are discarded in defining `D`.

Since `A` has odd grade-one receivers only, the linearized equations are

```text
V_o o + D e + A u = 0,
D^dag o + V_e e = 0,
M u + integral_V A_x^dag o = 0.                         (10)
```

The last equation is on the base: its fibre integration is mandatory
because `g` is a base field. Equation (8) and the other certified
determinants justify the exact substitution

```text
e = -V_e^-1 D^dag o,
(V_o-D V_e^-1 D^dag)o + A u = 0,
M u + integral_V A_x^dag o = 0.                         (11)
```

The odd equation is now second order in ambient derivatives. This is an
equivalence of smooth formal bulk equations, with the even field recovered
by the first formula. At the action level it is completing the square
using an invertible symmetric form; positivity of that form is unnecessary.
It is not an inversion of the full differential Hessian `C`.

This also limits the interpretation of the earlier compensator. Canceling
the highest mixed source with an even perturbation does not satisfy the
even equation in (10): its nonzero algebraic potential must be balanced
by an odd-field response. The compensator alone is not a full physical
mode or a valid reason to discard remaining higher derivatives.

## 6. Verification and remaining physical work

Run the focused exact certificate with

```bash
uv run --no-project --with sympy==1.14.0 python -B tests/channel-swings/native_zorro_algebraic_reduction_probe.py
```

It checks 170 spanning connection jets, six off-section controls, symbolic
base gauge identities, fourteen potential representatives, all 39 nonzero
factor bounds and the principal grade-transition/real-phase identities.
The covariance, real-action and formal-elimination proofs are analytic
arguments above; the script does not formalize functional analysis.

The pure-base Hessian `M`, the constraints of the remaining odd/base
system and their propagation still need to be determined. A physical
domain must also specify time, fibre boundary conditions and observation
reduction. The changes `T=T_*(g)+t` and (11) transport boundary data;
independently imposing new boundary conditions after substitution would
define a different problem. The finite local product-patch variation used
to construct the background does not already provide a closed Hamiltonian
domain or justify unrestricted base diffeomorphisms at its fibre boundary.

The closed `J` packet in (1a) permits a separate constrained-energy
calculation without first solving the metric equation. A nonzero dressed
perturbation in it is not removed by the two bulk redundancies identified
above. Whether it survives all constraints and the actual observation
reduction remains a mathematical question, not a premise of this note.

No energy sign is inferred from the determinant factors or Clifford mass
pairing. SA-U1/H59 remain open and SC-META-53 remains `UNCERTAIN`.
Independent later verification is required before any canon promotion.
