---
title: "Location-mixture rigidity and transverse nonzero-mode cancellation"
status: active_research
document_role: exploration
target_claim: INTERNAL_TARGET__LOCATION_MIXTURE_RIGIDITY_AND_TRANSVERSE_MODE_CANCELLATION
created: "2026-10-09"
updated_at: "2026-10-09"
---

# Location-mixture rigidity and transverse nonzero-mode cancellation

> **GU-COMPARATOR-ROUTING:** This artifact studies a repository-owned
> finite-cutoff quartic Hamiltonian and an opposite-charge torus
> gauge--matter control. It is not a source-native GU action, physical state
> space, observed carrier, prediction, confirmation, or falsification of a
> registered source claim. Conventional comparator conclusions bind only the
> models stated here.
>
> **Classification:**
> `INTERNAL_TARGET__CONDITIONAL_MATHEMATICAL_CONTROL__NO_SOURCE_VERDICT`

```yaml
gu-typed-objects:
  carrier: profiled_zero_mode_location_mixtures_plus_transverse_opposite_charge_torus_modes
  pairing_or_form: weighted_relative_fisher_form_quartic_schrodinger_form_and_bare_fourier_energy
  real_structure: real_finite_q_space_with_oppositely_charged_complex_scalar_pair
  grading: gaussian_location_law_and_charge_power_Q_n
  action_owner: repository_control_not_source_owned
  target_object: common_covariance_mixture_coefficient_and_nonzero_mode_holonomy_work
  observed_intertwiner: UNTYPED
```

## Scope and preflight bookend

The quantum route asks whether K1591 was special to a two-atom symmetric cat.
Keep the exact K1572 profiled covariance `S_N`, but replace its two locations
by an arbitrary probability law on the constant zero-mode coordinate. Fisher
convexity and K1533 depend only on that law's mean and variance, so the full
mixing benefit is again an exact rank-one inverse gap. K1572 then supplies a
componentwise lower bound. This is a global theorem for an infinite-dimensional
class of mixing laws, not for heterogeneous covariances, spatial textures or
nonstationary phases.

The PDE route does not assume equal same-mode amplitudes. It decomposes the
opposite-charge work into total intensity and momentum imbalance and identifies
the exact boundary correction whose corrected energy is the `a`-independent
bare Fourier energy. A nonzero lattice momentum perpendicular to the rotating
holonomy plane then gives an exact periodic control. It shows that excluding
only the homogeneous matter mode does not produce dispersion.

SC-ACT-01/02/06 remain assertions and SC-META-53 remains uncertain. The
physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED. No
source, ledger, canon, paper, prediction, confirmation or public-posture state
moves.

## K1596 — arbitrary location-mixture Fisher sandwich

Let `mu=N(0,I)`, let `Omega` be positive, let `S` be K1572's profiled diagonal
covariance, and let `e_0` be its constant zero-mode eigenvector. For an
arbitrary probability law `pi` on `A` with finite second moment, set

```text
nu_pi=int N(A e_0,S) pi(dA),   alpha=E A,   v=Var(A).              (1)
```

Fisher convexity and the exact Gaussian formula give

```text
I_Omega(nu_pi|mu)
 <= U:=E[A^2] omega_0+Tr[Omega(S+S^(-1)-2I)].                     (2)
```

The mixture has mean `alpha e_0` and covariance
`T=S+v e_0 e_0^T`. K1533 gives

```text
I_Omega(nu_pi|mu)
 >= L:=alpha^2 omega_0+Tr[Omega(T+T^(-1)-2I)].                    (3)
```

Because `E[A^2]=alpha^2+v`, the linear variance terms cancel. The exact width
is

```text
U-L=Tr[Omega(S^(-1)-T^(-1))]
    =omega_0 v/[s_(N,0)(s_(N,0)+v)]
    <=omega_0/s_(N,0)
    =sqrt(omega_0^2+kappa_(g,N)^+)=Theta_g(N).                    (4)
```

No atom count, symmetry, separation or overlap asymptotic enters (4). The law
may be continuous, asymmetric or arbitrarily multimodal. The common profiled
covariance and zero-mode-only location support are load-bearing.

## K1597 — the complete common-covariance location-mixture class

Let `E_N(A,S_N)` be the Rayleigh quotient of the positive stationary diagonal
Gaussian `N(Ae_0,S_N)`. Linearity of every potential expectation under mixing
and the wavefunction identity `q_0=I_Omega/4` give

```text
Q_N(pi)=E_pi E_N(A,S_N)-(U-I_Omega(nu_pi|mu))/4.                  (5)
```

K1572 proves that its larger-root profiled Gaussian is the finite-cutoff global
minimum over the stationary diagonal Gaussian class. Hence each component
satisfies `E_N(A,S_N)>=lambda_N^prof`. Combining this with (4),

```text
Q_N(pi)>=lambda_N^prof
          -(1/4)sqrt(omega_0^2+kappa_(g,N)^+).                    (6)
```

The class contains K1591's symmetric profiled cat, whose quotient is at most
`lambda_N^prof`, so its infimum obeys

```text
lambda_N^prof-O_g(N) <= inf_pi Q_N(pi) <= lambda_N^prof,
inf_pi Q_N(pi)/N^4 -> h_g^prof.                                  (7)
```

Thus every finite-second-moment zero-mode location mixture over the common
profiled covariance has the same class-infimum coefficient. Arbitrarily many
modes in location space and arbitrarily negative fourth-cumulant defects inside
this class cannot lower the `N^4` coefficient. This does not cover mixtures of
different covariances, non-zero-mode translations, spatial sign textures,
phases or nonstationary laws; K1587's `Theta_g(N^(5/2))` descent remains outside
the theorem.

## K1598 — unequal-mode bare-energy normal form

For charges `+e` and `-e`, write

```text
w_(+,k)=|phi_(+,k)|^2,  w_(-,k)=|phi_(-,k)|^2,
M=sum_k(w_(+,k)+w_(-,k)),
D=sum_k k(w_(+,k)-w_(-,k)).                                      (8)
```

Summing K1593's signed species identities without imposing equality gives

```text
H_a'=-e dot(a) dot D+e^2 dot(a) dot a M.                          (9)
```

Expanding the covariant frequencies shows

```text
H_a=E_0-e a dot D+(e^2/2)|a|^2 M,                                (10)
E_0=(1/2)sum_(sigma,k)[|dot phi_(sigma,k)|^2
                       +(m^2+|k|^2)|phi_(sigma,k)|^2].
```

Therefore the exact normal form

```text
E_0=H_a+e a dot D-(e^2/2)|a|^2M,
E_0'=e a dot D'-(e^2/2)|a|^2M'                                  (11)
```

contains no `dot a`. For `m>0`, Cauchy gives

```text
|D'|<=2E_0,   |M'|<=2E_0/m,
|E_0'|<=[2|e||a|+(e^2/m)|a|^2]E_0.                               (12)
```

The correction is exact and same-tier: it removes harmonic-electric total
variation and spatial derivative loss. Equation (12) still spends holonomy
amplitude and by itself gives no global integrability, scattering or positive
limiting analytic radius. Curvature, oscillatory Maxwell, current and nonlinear
remainders also remain outside this linear harmonic calculation.

## K1599 — a transverse nonzero-mode periodic family

Work on a three-torus. Choose a nonzero lattice vector `k` and a two-plane
orthogonal to it. Let

```text
a(t)=A(cos(Omega t),sin(Omega t),0),
phi_+(t,x)=phi_-(t,x)=R exp(i omega t) exp(i k dot x),             (13)
Omega=sqrt(2)eR,
omega=sqrt(m^2+|k|^2+e^2A^2),
```

after coordinates put `k` along the third axis. Then `k dot a(t)=0`, so both
charged covariant frequencies equal the same constant
`m^2+|k|^2+e^2A^2`. The opposite Gauss densities cancel. Their spatial currents
have equal momentum parts with opposite charges and add to
`-2e^2R^2a`, so the harmonic Maxwell equation is
`a''+2e^2R^2a=0`. Equations (13) are therefore an exact coupled periodic
solution with no homogeneous matter mode.

The same-`k` amplitudes are equal for all time, `D=0`, and `M=2R^2` is
constant. K1598 gives constant `E_0`; K1593 gives constant `H_a`. Meanwhile
the harmonic electric magnitude is `A Omega>0`, so total variation still
diverges linearly. Excluding only `k=0` is insufficient. Any dispersive route
must exclude or control the entire nondispersive transverse single-mode sector,
or the analytic hierarchy must exploit its exact cancellation. This one family
does not exclude small-data scattering under stronger localization, spectral,
nonresonance or radiation hypotheses.

## K1600 — protected integration and hostile bookend

The bridge census is now 315 rows: 236 satisfied, ten conditional, 65 excluded
and four missing. K1596--K1597 close all zero-mode location mixtures over one
common profiled covariance, not arbitrary negative-defect laws. K1598 removes
`dot a` from the exact unequal-mode linear normal form, but its same-tier bound
still spends `|a|+|a|^2`. K1599 proves that homogeneous-mode exclusion alone
does not create dispersion, without rejecting stronger dispersive hypotheses.

The hostile quantum check mutates the common covariance, zero-mode support,
finite-second-moment hypothesis and K1572 componentwise minimum. The hostile
PDE check mutates the signs in (10)--(11), drops transversality, or promotes
one periodic family to a universal no-go. None of those transfers is licensed.

The next quantum wake is covariance heterogeneity, non-zero-mode translation,
spatial texture or a global nonlinear Fisher/defect theorem. The next PDE wake
is an exact hypothesis that excludes every nondispersive resonant sector, or a
normal form controlling `D'`, `M'`, curvature, current, radial and oscillatory
remainders without spending a nonintegrable coefficient. The source-owned
action/measure/Hamiltonian tuple remains a separate admission gate.
