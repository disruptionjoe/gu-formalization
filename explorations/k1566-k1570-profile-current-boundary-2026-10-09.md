---
title: "Profiled Gaussian coefficient and differentiated-current boundary"
status: active_research
document_role: exploration
created: "2026-10-09"
updated_at: "2026-10-09"
---

# Profiled Gaussian coefficient and differentiated-current boundary

> **GU-COMPARATOR-ROUTING:** This artifact studies a repository-owned finite-cutoff scalar-field and gauge-PDE control. It is not a source-native GU action, physical state space, observed carrier, prediction, confirmation, or falsification of a registered source claim. Conventional comparator conclusions bind only the model stated here and do not transfer to Weinstein's source-native mechanism without an explicit typed bridge.
>
> **Classification:** `INTERNAL_TARGET__CONDITIONAL_MATHEMATICAL_CONTROL__NO_SOURCE_VERDICT`

```yaml
gu-typed-objects:
  carrier: finite_cutoff_real_scalar_q_space_plus_smooth_lifted_charge_fields
  pairing_or_form: gaussian_q_space_dirichlet_form_and_covariant_graph_energy
  real_structure: real_fourier_coordinates_with_complex_charge_pairing_in_pde_arc
  grading: charge_powers_Q_n
  action_owner: repository_control_not_source_owned
  target_object: stationary_diagonal_variational_coefficient_and_K1413_normal_form
  observed_intertwiner: UNTYPED
```

## Scope

The quantum calculation concerns the normalized three-torus, cube Fourier
cutoff, fixed positive mass and coupling, and the stationary diagonal Gaussian
trial class of K1524. The PDE calculation concerns smooth periodic cutoff
solutions in K1558's temporal-gauge convention. Neither construction is a GU
action, a continuum interacting Hamiltonian, a positive physical quotient, or
an observed prediction.

## 1. Fixed-variance profile minimization

Let `Q=[-1,1]^3`, `r=|x|`, and

\[
c_C={1\over2}\int_Q{dx\over r}.
\]

For a positive continuum squeeze profile `s`, the leading point variance and
free cost are

\[
A[s]={1\over2}\int_Q{s(x)\over r}\,dx,
\qquad
F[s]={1\over4}\int_Q r\{s+s^{-1}-2\}\,dx.
\]

At fixed `0<A<c_C`, strict convexity and one Lagrange multiplier give the
unique minimizer

\[
s_\kappa(x)={r\over\sqrt{r^2+\kappa}},
\qquad
A(\kappa)={1\over2}\int_Q{dx\over\sqrt{r^2+\kappa}}=A.
\]

The map `A(kappa)` decreases continuously from `c_C` to zero. If
`F_*(A)=F[s_(kappa(A))]`, the envelope theorem gives
`F_*'(A)=-kappa(A)/2`. This is a global constrained minimum, not just a
stationary equation, because the free integrand is strictly convex and the
constraint is linear.

Write `D(kappa)=c_C-A(kappa)` and `R(kappa)=kappa/D(kappa)`. Direct
differentiation reduces `R'>0` to positivity of

\[
2\{1-(1+t)^{-1/2}\}-t(1+t)^{-3/2},\qquad t>0,
\]

whose derivative is `3t/[2(1+t)^(5/2)]>0`. Moreover `R(kappa)->0` at
the cube origin because `D(kappa)/kappa->infinity`, while
`R(kappa)->infinity` as `kappa->infinity`.

## 2. Self-consistent coefficient and recovery

After optimizing the constant mean on the active branch, the reduced leading
functional is

\[
J_g(A)=F_*(A)+6gA(2c_C-A).
\]

The complementary branch `A>=c_C` cannot lower the coefficient: K1524's
optimized interaction is at least `6g c_C^2` there and the free cost is
nonnegative. Thus the global stationary diagonal coefficient problem is
contained in the displayed low-variance interval plus the vacuum endpoint.

Its unique interior minimizer is equivalently the unique positive solution of

\[
R(\kappa_g)=24g,
\qquad\text{or}\qquad
\kappa_g=24g\{c_C-A(\kappa_g)\}.
\]

The singular derivative at the cube origin is load-bearing: a positive
solution exists for every `g>0`. Since

\[
J_g'(A)={D(\kappa)\over2}\{24g-R(\kappa)\},
\]

the solution is the unique global minimum and lies strictly below the vacuum
coefficient `6g c_C^2` for every positive coupling.

The finite-cutoff recovery is explicit:

\[
s_{N,k}={\omega_k\over\sqrt{\omega_k^2+\kappa_gN^2}},
\qquad
y_N=\left[3(C_N-V_N)-{m^2\over4g}\right]_+.
\]

Riemann sums give `V_N/N^2->A(kappa_g)`, free cost divided by `N^4`
converging to `F[s_(kappa_g)]`, and the optimized total coefficient
converging to `J_g(A(kappa_g))`. Thus

\[
\limsup_{N\to\infty}{E_N\over N^4}
\le J_g(A(\kappa_g))<6gc_C^2.
\]

This also strictly improves the best uniform-squeeze coefficient: at the same
variance every nonvacuum constant profile has strictly larger free cost, and
the profiled family already beats the vacuum when the uniform family does not.
The result remains a Gaussian upper bound; no unrestricted lower coefficient,
ratio convergence, or bounded-error recentering follows.

## 3. Differentiated lifted current

Set `psi_n=Q^n phi`, `pi_n=D_t psi_n`, and
`j_n^a=e Im<psi_(n+1),D^a psi_n>`. Then

\[
\partial_tj_n^a=e\,\mathrm{Im}\langle\pi_{n+1},D^a\psi_n\rangle
+e\,\mathrm{Im}\langle\psi_{n+1},D^a\pi_n\rangle
+e\,\mathrm{Im}\langle\psi_{n+1},[D_t,D^a]\psi_n\rangle.
\]

The apparently derivative-losing middle term is harmless after covariant
integration by parts on the closed torus:

\[
\int A_a\,\mathrm{Im}\langle\psi_{n+1},D^a\pi_n\rangle
=-\int(\partial^aA_a)\,\mathrm{Im}\langle\psi_{n+1},\pi_n\rangle
-\int A_a\,\mathrm{Im}\langle D^a\psi_{n+1},\pi_n\rangle.
\]

The commutator is algebraic in electric curvature. Consequently K1563's
positive quadratic energy obeys

\[
\left|\int A\cdot\partial_tj_n\right|
\le C_m B_A(t)\sqrt{H_nH_{n+1}},
\]

with `B_A=|e|(||A||_infinity+||div A||_3)+e^2||A||_infinity||E||_infinity`.
There is no spatial derivative loss, but
there is still one charge-tier shift. The correction `M_n=int A dot j_n`
has the same adjacent-tier size.

## 4. Two-radius ceiling

For `a_n(rho)=rho^(2n)/n!` and
`G_rho=sum_n a_n(rho)H_n`, define
`S_sigma=sum_n a_n(sigma)sqrt(H_nH_(n+1))`. If
`0<sigma<rho`, then

\[
S_\sigma\le {1\over2}\left[1+{1\over
\rho^2\{1-(\sigma/\rho)^2\}^2}\right]G_\rho.
\]

This makes the modified energy and its differentiated-current remainder
finite at an inner radius whenever an outer analytic energy is finite. At one
radius no uniform relative bound exists: concentrating `H_n` and
`H_(n+1)` at a large tier makes the cross-term-to-energy ratio grow like
`sqrt(n+1)/rho`. The normal form therefore removes the spatial derivative
loss but does not remove K1450's analytic-radius debt or give a self-contained
global Gronwall estimate.

## Outcome

The profiled Gaussian family removes K1562's positive-coupling vacuum threshold
inside the larger stationary diagonal class and supplies a stronger explicit
unrestricted limsup. Independently, the differentiated-current remainder is
now classified as adjacent-charge rather than spatial-derivative losing, with
an exact nested-radius summation and a same-radius coercivity obstruction.
Protected source claims, the physics ledger, canon, papers, and public posture
do not move.
