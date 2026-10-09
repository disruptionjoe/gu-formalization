---
title: "A two-sided constraint-compatible energy obstruction on the stationary curved I1B branches"
status: active_research
claim_verdict: conditional_two_sided_constraint_reduced_energy_obstruction
doc_type: native_action_constrained_hamiltonian_derivation
created: 2026-10-08
target_claim: NONE-NOT-A-KILL
bears_on: [SC-ACT-06, SC-META-53]
spec_row: SA-U1
canon_verdict_change: none
receipt: lab/process/native-zorro-constrained-energy.json
probe: tests/channel-swings/native_zorro_constrained_energy_probe.py
---

# Constrained energy on the selected curved branch

**The quadratic Hamiltonian is unbounded above and below on a smooth, compactly
supported, constraint-compatible phase core of the selected stationary
curved I1B reconstruction, for either certified sign of the coupling.**
The construction uses the source phased real
slice, solves the primary constraints and removes their nondynamical
variables. Its remaining time form is nondegenerate. The negative-energy
fields are therefore not artifacts of leaving multipliers unconstrained.

There are both section-visible and section-invisible negative-energy
families. The first survives the native section evaluation. The second
proves that identifying all fields with equal section pullback does not
make the Hamiltonian descend to that quotient. Thus section evaluation
alone does not repair the energy obstruction.

This is a result about one explicitly selected action realization, a pair of
real stationary branches with opposite coupling signs, and a phase core.
It does not establish a no-go for every source
completion, action choice, background or additionally selected physical
subspace. In particular it does not turn Nguyen–Polya's group-only argument
into a GU theorem. No independent later verification or canon promotion is
claimed. SA-U1/H59 remain open and SC-META-53 remains `UNCERTAIN`.

**Same-day strengthening:** the initial note exhibited only the vertical
negative-energy family for `kappa>0`. The spatial companion below gives the
opposite sign. The mirror branch and the two witnesses now exclude a repair
by reversing this coupling or the overall action sign. A separate occupation-
state matrix calculation checks their Clifford coefficients independently of
the original sparse engine. This is an independent implementation, not an
independent later research review or a quantum spectral theorem.

The action and background are exactly those of the
[stationary construction](native-zorro-stationary-background-2026-10-08.md).
The [algebraic reduction](native-zorro-algebraic-reduction-2026-10-08.md)
establishes the real slice, the complete mixed metric operator and the
closed imaginary-grade packet used here. Classification:
`SOURCE_NATIVE_ROUTE` within that declared reconstruction. The
[routing method](../../lab/methods/source-native-comparator-routing.md),
[claim-indexed verdict doctrine](../claim-indexed-verdict-doctrine-2026-08-12.md)
and [status consistency method](../../lab/methods/claim-status-consistency.md)
govern the scope of the conclusion.

```gu-typed-objects
result: solved primary constraints, nondegenerate time form, quadratic energy unbounded in both directions on either coupling branch, and section-quotient obstruction on a specified compact phase core
carrier: imaginary-grade dressed Clifford one-form perturbations on the canonical curved metric bundle at the certified stationary branch LAYER=ambient+source-print BRIDGE=declared_canonical_reconstruction CHIRALITY=N/A
pairing: actual source-action time presymplectic form and quadratic Noether Hamiltonian; no replacement by a positive Clifford trace ON=constraint_reduced_compact_phase_core
real_structure: t=i psi with real psi of Clifford grades 0,3,4,7,8,11,12, inside the source phased anti-involution slice
grading: Clifford phase packet, primary time kernel and its complement; coefficient ranks are not particle counts
action_owner: source-action -- the selected comm/symi/symi I1B functional and its full differentiated cubic Hessian, at the certified real roots kappa=plus-or-minus sqrt(kappa_squared)
target: failure of semibounded energy and of Hamiltonian descent under bare section evaluation on the stated core MAP-TYPE=evaluation
```

## 1. A closed native packet and a stated time

Set the observing metric to `g_*=eta`, with time `t=x^0`. Let `V` be a
sufficiently small relatively compact fibre neighbourhood of `h=eta`
on which the ambient covector `q=dt` has positive square. Work on
`I_t x R^3 x V`, where `I_t` is an open time interval. The coefficients of
the curved stationary background are independent of `t` and of base
position. The metric is nevertheless curved and has signature `(7,7)`.

Use the dressed variable and natural field coordinates
`T=T_*(g)+delta T`. Coefficient conjugation splits the full linearized
equations into two independent packets. This note uses

```text
delta T = i psi,
psi in Omega^1(Lambda^0 + Lambda^3 + Lambda^4 + Lambda^7
              + Lambda^8 + Lambda^11 + Lambda^12),      (1)
```

with real coefficients. The metric perturbation is zero. This is a closed
linearized sector of the actual Hessian, so the other distortion and
metric equations have zero linear source from (1). It is not a nonlinear
truncation. Its source real structure is retained: dropping the factor
of `i` would reverse its action and energy.

Let `E(xi)` denote the real, skew, formally antisymmetrized first-order
coefficient obtained by varying the actual action. The Clifford trace,
Hodge operator and tautological tensors are parallel for the ambient
Levi-Civita connection, hence `nabla E=0`. In the unphased real coefficient
basis the distortion Euler operator is

```text
C_R = E^mu nabla_mu + V_R,
V_R = kappa M + a H_a + c H_c + v H_v + w H_w.           (2)
```

The four `H` matrices are full cubic action Hessians with the four
intrinsic background fields. No printed-residual derivative replaces them.
On (1) both quadratic blocks have the opposite overall sign:
`I_2[i psi]=-I_2[psi]`. The equations are still `C_R psi=0`.

The initial phase core below consists of smooth fields of compact support
in `Sigma=R^3 x V`. All integrations by parts used here have zero boundary
term on that core. The result concerns the quadratic action relative to
the stationary background; it requires no integral of the constant
background density over all of space or the full noncompact metric fibre.

## 2. A geometric primary-kernel lemma

Put `K(q)=ker E(q)`. On the positive-norm covector locus its rank is
constant: orthogonal covariance transports `E(q)` to a positive multiple
of `E(e^0)`. This statement concerns the first-order coefficient, which
has full ambient orthogonal covariance; it does not assume that the
background potential has that larger symmetry.

Choose a smooth local kernel frame `N(q)`, so `E(q)N(q)=0`. Differentiation
with respect to covector components, followed by multiplication by `N^T`,
gives

```text
N^T E^A N = 0,
N^T (E^A N_,B + E^B N_,A) = 0.                        (3)
```

The second identity follows by differentiating `E(q)N(q)=0` twice;
the term `N^T E(q) N_,AB` is zero. Since `q=dt` and the connection is
torsion-free, `nabla_A q_B` is symmetric. Contracting it with (3), in a
normal frame at the point, proves

```text
N^T E^mu nabla_mu N = 0.                               (4)
```

A different choice of kernel frame contributes only a derivative within
`K`, which vanishes by the first identity in (3). Thus (4) is intrinsic.
It is important that `q` is an exact time covector: an arbitrary
nonintegrable distribution is not being substituted for time.

Choose any smooth complement `S` of `K(q)`, and write
`psi=s+N z`, with `s` a section of `S`. A convenient auxiliary positive
coordinate metric can choose this complement; it is not a proposed
physical inner product. Equations (3)--(4) imply that the kernel rows of
the full equation are

```text
W z + N^T C_R s = 0,
W = N^T V_R N.                                        (5)
```

There are no derivatives of `z` in (5), and no time derivatives of `s`:
`N^T E(dt)=0`. Curved connection and frame terms in `C_R s` are retained.
In particular, no uncomputed geometric correction is added to `W`.

## 3. Exact invertibility of the primary potential

The same rational orthonormal frame as the predecessors has time index
`0`, radial index `10`, three horizontal spatial axes and nine vertical
traceless axes. Each coefficient has XOR label
`lambda=(exterior one-form mask) XOR (Clifford mask)`.

The time derivative toggles index `0`; the grade-two background potential
toggles index `10`; the mass and grade-one potential preserve the label.
Consequently each orbit of four labels

```text
lambda, lambda XOR {0}, lambda XOR {10},
lambda XOR {0,10}                                     (6)
```

is closed for the time coefficient and algebraic potential. Select the
imaginary grades (1) inside this orbit and compute its complete time
kernel. The background stabilizer fixing time and `r` acts separately on
the three horizontal spatial and nine vertical traceless directions.
Complex orthogonal signed permutations reduce all the orbits to forty
representatives, labelled by counts `0<=n_H<=3`, `0<=n_V<=9`.
Their multiplicities are `binomial(3,n_H) binomial(9,n_V)`.

As in the predecessor, complexification is used only to transfer
determinant nonvanishing between coefficient blocks. It does not change
the selected real fields. The common factor `i` on (1) reverses the
potential's sign and leaves its invertibility unchanged.

The probe computes every kernel and every entry of `W` directly from the
mass pairing and cubic Hessian. To certify the determinants, write
`a=kappa alpha(w)`, `c=kappa beta(w)` and use the previously isolated
degree-ten algebraic root for `w`, with `kappa>0`. Multiplying the even
kernel vectors by `kappa`, then dividing the entire potential matrix by
`kappa`, puts its entries in `Q(w)`:

```text
odd/odd:   M + alpha H_a + beta H_c,
even/even: kappa^2 (M + alpha H_a + beta H_c),
odd/even:  v H_v + w H_w.                              (7)
```

All forty determinants are nonzero **in that exact number field**.
No rounded background values or numerical rank tolerances enter the
certificate. The [receipt](../../lab/process/native-zorro-constrained-energy.json)
records the minimal polynomial, root interval, all multiplicities and
digests of the reduced determinant coefficients. The producer rebuilds
the matrices and exact field calculations without a coefficient bank.

### The opposite coupling branch

The background equations are also solved by
`(a,c,kappa)->(-a,-c,-kappa)`, with `v,w` unchanged. The first three
equations are invariant; the last two reverse sign. Thus their common zero
set is preserved. The epsilon and observing-metric stationarity arguments
apply to either sign. This changes the coupling parameter and the grade-one
background together; it is not an identification of two backgrounds at the
same fixed value of that parameter.

Let `P` be Clifford parity on the homogeneous primary-kernel basis. The
mass and grade-one-background matrices preserve parity; the grade-two
background matrices reverse it. Consequently the primary potentials obey

```text
W_minus = -P W_plus P,        P^2=1.
```

The probe verifies these coefficient identities in all forty classes.
They prove invertibility on the mirror branch and interchange its positive
and negative inertias without a numerical scan. Equivalently, the scaled
number-field calculation (7) depends only on `kappa^2` and works for either
nonzero square root.

Thus `W` has a smooth pointwise inverse throughout the chosen time/fibre
patch. Equation (5) gives the exact local recovery rule

```text
z = -W^-1 N^T C_R s.                                  (8)
```

Every smooth compactly supported `s` supplies constraint-compatible data;
(8) preserves compact support and uses spatial derivatives only. The time
form restricted to `S` is nondegenerate, because `K` is exactly its
kernel. After (8), the remaining equations determine the time derivative
of `s`, with no remaining multiplier equations or gauge null directions
inside this packet. This is the usual algebraic conclusion of the
first-order constraint reduction, not an inference from a symbol kernel
alone. It does not assert a well-posed global Cauchy evolution.

The two known source redundancies do not remove these variables: epsilon
redundancy fixes the dressed distortion, and linearized base
diffeomorphisms have `delta t=0` in the natural coordinates. The other
linearized packet cannot add a constraint to this one because the Hessian
is block diagonal under coefficient conjugation.

## 4. The actual reduced Hamiltonian

Use a stationary local frame. In the unphased real variables write
`C_R=E^0 partial_t+C_sp`, retaining all connection terms in `C_sp`.
The imaginary slice has the autonomous quadratic Lagrangian

```text
L_J = -psi^T E^0 partial_t psi/2 - psi^T C_sp psi/2,
```

up to the compact-support divergence already included in the formal
adjoint calculation. Its Noether Hamiltonian is therefore
`H_J=integral psi^T C_sp psi/2`. Define `f=N^T C_sp s`. Completing the
square using the actual constraint (8) gives

```text
H_red[s] = integral_Sigma (s^T C_sp s - f^T W^-1 f)/2.  (9)
```

The density is the positive coordinate density induced by the ambient
volume form. The time presymplectic form restricts to the nondegenerate
bilinear form associated with `-E^0|_S`. It is not a positive Hilbert
pairing. On any smooth solution for which the boundary flux vanishes,
autonomy gives conservation of (9). The unboundedness argument below
already holds on its compact phase core and does not assume a global
solution or a self-adjoint completion.

Take a unit positive vertical traceless covector `zeta=e^4`, and let the
free real field direction be

```text
s_0=e^10 1.                                          (10)
```

It is a genuine dynamical direction: it is transverse to the primary
kernel, and `E^0 s_0` is nonzero. In the probe's basis
`s_0^T E^0(E^0 s_0)=-48`, so it has a nonzero time symplectic partner.

For the spatial derivative along `zeta`, the complete primary source is
particularly simple. In the target orbit `(n_H,n_V)=(0,1)`, one kernel
direction is

```text
n_0=e^0 gamma_0 gamma_4 gamma_10,
N^T E(zeta)s_0 = 2 e_last,
W e_last = kappa e_last.                              (11)
```

Every background cubic column in the last identity is exactly zero,
and the mass column is exactly the unit column. XOR routing excludes
additional primary receivers outside that target orbit. Thus (11)
uses the full primary potential, not a truncated inverse. The induced
auxiliary term is `-(2/kappa)n_0 partial_zeta psi_0`.

For a free scalar amplitude in (10), the second term of (9) has principal
spatial energy

```text
-(2/kappa) (partial_zeta psi_0)^2.                     (12)
```

The first term of (9) has only one spatial derivative. The sign in (12)
comes after solving the constraints on the source imaginary slice; it
is not the sign of an unreduced Clifford trace. Stabilizer covariance
extends (12) to any positive vertical traceless covector, with the
factor `|zeta|^2` for an unnormalized covector.

A direct sign check is useful. The relevant imaginary-slice spatial
Lagrangian terms are `-2 z partial_zeta psi_0-kappa z^2/2`.
Substituting the exact constraint `z=-2 partial_zeta psi_0/kappa`
gives `+2(partial_zeta psi_0)^2/kappa` in the Lagrangian and hence
the negative of that expression in the Hamiltonian, as in (12).

### An exact spatial companion and an independent matrix realization

Repeat the complete primary projection for the horizontal spatial axis
`e^1` at `h=eta`, keeping the same free direction `s_0`. The receiving
class is `(n_H,n_V)=(1,0)`. Its distinguished vector is
`n_1=e^0 gamma_0 gamma_1 gamma_10`, and the exact identities are

```text
N^T E(e^1)s_0 = 2 e_last,
W e_last = -kappa e_last,
H_red,principal = +(2/kappa)(partial_1 psi_0)^2.        (12a)
```

Here `e_last` names the distinguished coordinate, independent of the
implementation's basis ordering. Every cubic column again vanishes and
the Hodge mass column is now minus the unit column. Thus the two derivative
directions have opposite reduced-energy signs for either nonzero `kappa`.

The [independent matrix probe](../../tests/channel-swings/native_zorro_matrix_energy_probe.py)
imports neither `K77Core` nor a coefficient bank. It represents fourteen
gamma matrices on the 128 occupation states of seven fermionic modes:
positive generators are creation plus annihilation, negative generators
creation minus annihilation. It checks every Clifford relation on all
128 states and uses the normalized matrix trace. For `p<q`, the selected
Shiab contraction expands directly to

```text
Tr[e^mu C wedge S(e^p wedge e^q D)]
 = eta_p eta_q (delta_mu,p tr(C[gamma_q,D])
              -delta_mu,q tr(C[gamma_p,D])
              -(eta_mu/2) tr(C{gamma_mu,{gamma_p gamma_q,D}})).
```

The last sign includes both `*vol=-1` and the two factors of `i` in the
symmetrized channels. Antisymmetrizing the first-order action, differentiating
all three slots of the cubic term, and computing the two complete primary
kernel blocks reproduces sources `2`, masses `+1,-1`, four zero cubic
columns each, and the time symplectic coefficient `-48`. Scalar trace
selection proves the XOR receiver completeness: a nonempty Clifford blade
anticommutes with some invertible gamma matrix and therefore has zero trace.
This coefficient verification is separate from the analytic domain argument.

## 5. A rigorous compact-support unboundedness family

Choose a smooth degree-zero fibre coordinate `y(h)` with
`y(eta)=0`, `dy|_eta=e^4` and `r(y)=0`. Such a coordinate can be given
explicitly: if `ell` is the linear fibre covector `e^4` at `eta`, then
`ell(eta)=0`; put `y(h)=ell(h)/h_00`. On a small enough `V`, `h_00>0`,
`dy` is vertical traceless and `|dy|^2>0`. These are open conditions.

Let `chi(x^1,x^2,x^3,h)` be a nonzero real smooth compactly supported
cutoff in this patch. Use the smooth radial coframe direction (10) and
free amplitudes

```text
psi_0,n = chi sin(n y),
psi_n = s_0 psi_0,n + N z_n,
z_n = -W^-1 N^T C_sp(s_0 psi_0,n).                     (13)
```

All constraints are satisfied exactly, not just to leading frequency.
All fields and their recovered auxiliaries have compact support. The
coefficients of the reduction and their needed derivatives are bounded
on this fixed support. Equations (9)--(12) give

```text
H_red[psi_n]
 = -(2 n^2/kappa) integral |dy|^2 chi^2 cos^2(ny) dmu
   + R_n,
|R_n| <= C_1 n + C_0.                                 (14)
```

The constants are finite sup-norm/integral bounds on the fixed smooth
coefficients and cutoff. The terms included in `R_n` have at most one
derivative of the oscillatory amplitude. Since `dy` is nowhere zero on
the support, integration by parts using a smooth vector field with
`X(y)=1` gives
`integral a cos(2ny)=O(1/n)` for `a=|dy|^2 chi^2 dmu`.
Consequently

```text
H_red[psi_n] = -(n^2/kappa) integral |dy|^2 chi^2 dmu + O(n),
```

and the strictly positive integral makes the energy tend to minus
infinity. This is an analytic bound with exact coefficient (12), not a
finite-difference null test or a numerical spectral extrapolation.

Any Hamiltonian completion that contains this compact constraint-reduced
core and agrees with its quadratic form is therefore not semibounded.
A conserved positive pairing together with bounded-below classical energy cannot
be obtained on such a completion. This does not, by itself, exclude a
positive conserved norm with an unbounded Hamiltonian, or an additional
source-owned restriction that excludes the exhibited core.

For the companion family use `psi_0,n=chi sin(n x^1)`. The coefficient
in (12a) is nonzero at `h=eta`; smoothness of the exact constraint inverse
preserves its sign on a sufficiently small fibre neighbourhood. Choose
the complement to contain the smooth radial direction there. Exact recovery
by (8), bounded lower-order coefficients on the fixed compact support, and
integration by parts in `x^1` give

```text
H_red[psi_n] = +c n^2 + O(n),   c>0,   for kappa>0.
```

The vertical family gives the negative sign. For `kappa<0` the two signs
exchange. Thus both divergences occur on each branch, and an overall
reversal of the action sign also only exchanges them. These are values of
the classical quadratic Hamiltonian on phase data. No Hilbert normalization,
quantized operator spectrum, well-posed global evolution or nonlinear
runaway is inferred from this statement.

## 6. Section visibility and failure of bare observation descent

The native section is `j_*(x)=(x,eta)`. On the smooth phase core the
pullback `j_*^*(delta T)` is well-defined. It is not identified with a
completed quantum state map.

For `kappa>0`, first choose `chi` nonzero on the section. Because `y(eta)=0`, the free
field and all lower-order amplitude terms vanish there, while its normal
derivative is `n chi e^4`. The exact constraint recovery (11) gives

```text
j_*^*(delta T_n)
 = -(2 i n/kappa) chi(x,eta) dx^0 gamma_0 gamma_4 gamma_10.
                                                               (15)
```

This nonzero observed component is in the allowed source grade-three
slice. Thus the visible negative-energy family is not discarded merely
by restricting exterior one-form indices to the observing section.

For `kappa<0`, use the spatial family with `chi` nonzero where `x^1=0`
on the section. On that slice its amplitude vanishes and the exact
auxiliary pullback is `(2 i n/kappa) chi dx^0 gamma_0 gamma_1 gamma_10`,
which is nonzero. The spatial family has negative energy on this branch.

Next choose the cutoff with fibre support disjoint from `h=eta`, still
inside the same positive patch. Locality of (8) implies that the full
constraint-compatible field, including its auxiliary components, vanishes
near the section. Its pullback is exactly zero, but the appropriate
vertical or spatial family still gives negative energy on either branch.
The zero field has the same pullback and zero energy.
Therefore the Hamiltonian is not constant on the fibres of the observation
map and **does not descend through the quotient by its kernel**.

These invisible fields are not presymplectic gauge null directions: the
time form after (8) is nondegenerate. A further dynamical selection or a
different, source-justified observation reduction would have to be
specified and checked; bare section evaluation supplies neither.

## 7. Validation and precise conclusion

Run

```bash
uv run --no-project --with sympy==1.14.0 python -B tests/channel-swings/native_zorro_constrained_energy_probe.py
uv run --no-project --with sympy==1.14.0 python -B tests/channel-swings/native_zorro_matrix_energy_probe.py
```

The main probe passes seventeen grouped checks: it reconstructs forty
complete primary-potential classes, certifies their determinants in the
stationary number field, proves the mirror congruence and checks both
energy witnesses. The separate matrix probe passes twelve grouped checks
of the independently realized coefficient inputs. The geometric kernel
lemma and the compact-support bounds are
the analytic arguments above, not claims of a formalized PDE theorem.

| Object or inference | Result at this scope |
| --- | --- |
| Primary constraints in the closed imaginary packet | Solved algebraically with a smooth pointwise inverse |
| Remaining time form | Nondegenerate on the stated smooth compact phase core |
| Quadratic Noether energy on that core | Unbounded in both directions on either coupling branch, by two exact constraint-compatible families |
| Native section evaluation | Has a visible negative-energy family; its kernel also contains negative-energy nongauge fields |
| Hamiltonian on the bare section quotient | Does not descend |
| Conserved positive norm alone, global evolution or a selected quantum completion | Not established or excluded by this energy argument alone |
| All GU action choices, backgrounds or further physical selections | Not covered; no universal source-claim verdict |

The result supplies a concrete surviving obstruction for the specified
reconstruction and domain class. It supersedes attempts to decide this
branch from an unconstrained mass sign, from the earlier flat-background
growing mode, or from a principal metric compensator alone. Those
calculations retain their separate scopes and correction history.
