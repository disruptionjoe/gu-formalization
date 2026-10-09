---
title: "Profiled residual Ritz scale and harmonic-electric periodic obstruction"
status: active_research
document_role: exploration
target_claim: INTERNAL_TARGET__PROFILED_RESIDUAL_SCALE_AND_HARMONIC_ELECTRIC_INTEGRABILITY
created: "2026-10-09"
updated_at: "2026-10-09"
---

# Profiled residual Ritz scale and harmonic-electric periodic obstruction

> **GU-COMPARATOR-ROUTING:** This artifact studies a repository-owned
> finite-cutoff quartic Hamiltonian and a charge-neutral two-species periodic
> Maxwell--Klein--Gordon sector. It is not a source-native GU action, physical
> state space, observed carrier, prediction, confirmation, or falsification of
> a registered source claim. Conventional comparator conclusions bind only the
> models stated here.
>
> **Classification:**
> `INTERNAL_TARGET__CONDITIONAL_MATHEMATICAL_CONTROL__NO_SOURCE_VERDICT`

```yaml
gu-typed-objects:
  carrier: finite_cutoff_translation_invariant_wavefunctions_plus_charge_neutral_periodic_gauge_matter_sector
  pairing_or_form: quartic_schrodinger_form_gaussian_chaos_pairing_and_reduced_maxwell_matter_energy
  real_structure: real_finite_q_space_with_oppositely_charged_complex_scalar_pair
  grading: gaussian_chaos_degree_and_charge_sign
  action_owner: repository_control_not_source_owned
  target_object: profiled_residual_ritz_scale_and_energy_only_harmonic_integrability
  observed_intertwiner: UNTYPED
```

## Scope and preflight bookend

The quantum arc retains the finite cube cutoff, positive mass, fixed positive
coupling and K1572 larger-root stationary diagonal Gaussian. K1581 proves only
that its residual is nonzero. The new question is quantitative: what are the
cutoff scales of the off-diagonal residual norm and the second Ritz diagonal,
and what do they decide about the leading coefficient and bounded-error
recentering?

The PDE arc tests the weakest proposed route from K1584 to an integrable
holonomy budget. It asks whether positive conserved coupled energy and Gauss
neutrality can force the harmonic electric field into `L1_t`. A homogeneous
periodic orbit is enough to reject that implication without rejecting
dispersive or cancellation-based routes.

SC-ACT-01/02/06 remain assertions and SC-META-53 remains uncertain. The
physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED. No
source, ledger, canon, paper, prediction, confirmation or public-posture state
moves.

## K1586 — exact third/fourth profiled residual

Let `G_N` be K1572's larger-root Gaussian minimizer and write

```text
phi=h_N+eta,  E_G eta=0,
Gamma_N(x-y)=E_G[eta(x)eta(y)],  v_N=Gamma_N(0).       (1)
```

The interaction expansion relative to `Gamma_N` is

```text
:phi^4:_(C_N)
 = :eta^4:_(Gamma_N)+4h_N:eta^3:_(Gamma_N)
   +6(h_N^2+v_N-C_N):eta^2:_(Gamma_N)
   +4h_N(h_N^2+3v_N-3C_N)eta + constant.              (2)
```

The logarithmic quotient of the free oscillator acting on a Gaussian is
affine-quadratic. K1572 varies `h_N` and every stationary diagonal covariance
coordinate at an interior minimum. Its Euler equations therefore cancel the
constant, first and second Gaussian-chaos projections of
`(H_N-lambda_N)G_N/G_N`. What survives is exactly

```text
R_N=g int_T3 [:eta(x)^4:_(Gamma_N)
              +4h_N:eta(x)^3:_(Gamma_N)] dx,
(H_N-lambda_N)G_N=R_NG_N.                             (3)
```

Different Gaussian chaoses are orthogonal. Wick's rule gives

```text
sigma_N^2=||R_NG_N||^2
 =g^2[96h_N^2 int_T3 Gamma_N(z)^3 dz
      +24 int_T3 Gamma_N(z)^4 dz].                    (4)
```

The covariance has positive Fourier coefficients, so the displayed
convolution sums are nonnegative and the fourth term is strictly positive.
This refines K1581's degree argument into an exact residual formula.

## K1587 — the Ritz drop is `Theta_g(N^(5/2))`

Write

```text
Gamma_N(z)=sum_(|k|_infty<=N) a_(N,k)e^(ik.z),
a_(N,k)=[2 sqrt(omega_k^2+kappa_(g,N)^+)]^(-1).       (5)
```

K1572 gives `kappa_(g,N)^+/N^2->kappa_g>0` and
`h_N^2=Theta_g(N^2)`. Hence `a_(N,k)=O_g(N^-1)` on the
whole cutoff box and `a_(N,k)>=c_gN^-1` on any fixed positive-volume interior
subbox. Positive convolution counting then yields

```text
int Gamma_N^3=Theta_g(N^3),
int Gamma_N^4=Theta_g(N^5).                            (6)
```

Indeed, a three-fold zero-sum convolution has two freely chosen lattice modes,
`Theta(N^6)` interior choices and three factors `Theta(N^-1)`; the four-fold
sum has three freely chosen modes, `Theta(N^9)` choices and four such factors.
The full cutoff boxes give the matching upper counts. Equations (4)--(6) imply

```text
sigma_N=Theta_g(N^(5/2)).                              (7)
```

For `u_N=R_NG_N/sigma_N`, set

```text
delta_N=<u_N,(H_N-lambda_N)u_N>.                      (8)
```

The Gaussian ground-state transform splits (8) into a polynomial Dirichlet
part and `E_G(R_N^3)/sigma_N^2`. The former is `O_g(N)` because `R_N` lives in
chaoses three and four and every cutoff one-particle oscillator frequency is
`O_g(N)`. Nelson hypercontractivity on degree at most four gives

```text
|E_G R_N^3|/sigma_N^2
 <= ||R_N||_3^3/sigma_N^2 <= C sigma_N.               (9)
```

Thus `|delta_N|<=C_g sigma_N`. The exact lower Ritz eigenvalue is
`lambda_N-Delta_N`, where

```text
Delta_N=[sqrt(delta_N^2+4sigma_N^2)-delta_N]/2.        (10)
```

Equations (7), (9) and (10) give

```text
Delta_N=Theta_g(N^(5/2)).                              (11)
```

The strict descent is therefore uniform and divergent, but still
`o(N^4)`. It cannot by itself decide whether the unrestricted leading
coefficient equals or lies below `h_g^prof`.

## K1588 — profiled-Gaussian bounded-error recentering is false

Let `lambda_N^prof` be the exact K1572 stationary diagonal Gaussian minimum
and `E_N` the unrestricted translation-invariant bottom. The Ritz vector is
translation invariant, so (11) gives

```text
lambda_N^prof-E_N >= c_g N^(5/2)                      (12)
```

eventually. Consequently, for every
`a_N=lambda_N^prof+o(N^(5/2))`, including every bounded perturbation of the
profiled Gaussian energy,

```text
inf spec(H_N-a_N) -> -infinity.                       (13)
```

This answers one bounded-error question sharply: the profiled Gaussian value
cannot recenter the unrestricted theory to `O(1)`. It does not identify the
unknown true `E_N`, decide whether recentering by `E_N+O(1)` has compactness or
Mosco limits, or change the leading coefficient. K1577 remains exact on its
nonnegative-defect class; by K1582 the descending direction exits that class.

## K1589 — conserved energy does not make harmonic electric variation finite

Consider the homogeneous torus sector of Maxwell--Klein--Gordon with two
equal-mass complex scalars of charges `+e` and `-e`. With symmetric
half-normalization, temporal gauge reduces the equations to

```text
phi_sigma''+(m^2+e^2|a|^2)phi_sigma=0,
a''+e^2(|phi_+|^2+|phi_-|^2)a=0.                     (14)
```

The Gauss density is

```text
rho=e Im(conj(phi_+)phi_+')
    -e Im(conj(phi_-)phi_-').                         (15)
```

For arbitrary `A,R>0`, define

```text
Omega=sqrt(2)eR,  omega=sqrt(m^2+e^2A^2),
a(t)=A(cos(Omega t),sin(Omega t),0),
phi_+(t)=phi_-(t)=R exp(i omega t).                   (16)
```

The amplitudes `|a|`, `|phi_+|` and `|phi_-|` are constant. Substitution in
(14) proves the equations exactly, while (15) vanishes because the phases and
amplitudes agree and the charges are opposite. The two spatial currents add
and supply the centripetal Maxwell force.

The reduced Hamiltonian is finite and constant. But

```text
E_bar=-a',  |E_bar|=A Omega>0,
int_0^T |E_bar(t)|dt=A Omega T -> infinity.           (17)
```

Thus energy conservation, Gauss neutrality and a genuine coupled Maxwell
current do not imply K1584's `L1_t` harmonic-electric hypothesis. A global
positive-radius theorem must instead exploit dispersion or scattering,
exclude the homogeneous charged sector, add damping, or find a normal-form
or spacetime cancellation that does not pay total variation. The construction
does not exclude those routes and does not claim failure for every
one-species constrained model.

## K1590 — protected integration and hostile bookend

The bridge census is now 305 rows: 226 satisfied, ten conditional, 65 excluded
and four missing. K1586--K1588 quantify a divergent but subleading
profiled-Gaussian descent and exclude only that Gaussian's bounded-error
recentering. They do not determine the unrestricted `N^4` coefficient or the
true-ground shift. K1589 excludes only an energy-only generic route to
harmonic-electric integrability; dispersive and cancelling closures remain.

The hostile quantum check requires the larger-root interior profiled Gaussian,
fixed positive coupling, positive covariance coefficients, the exact chaos
cancellation, and the `o(N^4)` ceiling. The hostile PDE check requires two
oppositely charged species, equal amplitudes and phases, constant circular
holonomy amplitude and Gauss cancellation; it forbids promotion to a universal
one-species no-go.

The next quantum wake is a global nonlinear Fisher/negative-defect lower bound
or a construction changing the unrestricted `N^4` coefficient, followed by
true-ground `E_N+O(1)` compactness. The next PDE wake is a dispersive estimate
excluding the periodic homogeneous obstruction or a cancellation-based
hierarchy whose radius budget does not spend `int|E_bar|`. The source-owned
action/measure/Hamiltonian tuple remains a separate admission gate.
