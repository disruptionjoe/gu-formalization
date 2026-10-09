---
title: "Heterogeneous Gaussian mixtures and atom-free spectral dispersion"
status: active_research
document_role: exploration
target_claim: INTERNAL_TARGET__HETEROGENEOUS_MIXTURE_STABILITY_AND_SPECTRAL_DISPERSION
created: "2026-10-09"
updated_at: "2026-10-09"
---

# Heterogeneous Gaussian mixtures and atom-free spectral dispersion

> **GU-COMPARATOR-ROUTING:** This artifact studies a repository-owned
> finite-cutoff quartic Hamiltonian and a conditional spectral model for the
> harmonic gauge sector. It is not a source-native GU action, physical state
> space, observed carrier, prediction, confirmation, or falsification of a
> registered source claim. Conventional comparator conclusions bind only the
> models stated here.
>
> **Classification:**
> `INTERNAL_TARGET__CONDITIONAL_MATHEMATICAL_CONTROL__NO_SOURCE_VERDICT`

```yaml
gu-typed-objects:
  carrier: translated_heterogeneous_gaussian_mixtures_plus_harmonic_spectral_sector
  pairing_or_form: weighted_relative_fisher_form_quartic_schrodinger_form_and_charge_analytic_energy
  real_structure: real_finite_q_space_with_real_harmonic_connection
  grading: gaussian_component_law_and_charge_power_Q_n
  action_owner: repository_control_not_source_owned
  target_object: precision_jensen_gap_and_atom_free_holonomy_budget
  observed_intertwiner: UNTYPED
```

## Scope and preflight bookend

The quantum route crosses both restrictions isolated by K1597: components may
have different covariances and their means may point in arbitrary cutoff-mode
directions. The exact quantity left between Fisher convexity and the K1533
moment extremal is a precision Jensen gap. That gap can be order `N^4` under
order-one heterogeneity, so the unrestricted coefficient is still open. A
shrinking relative Loewner band around the K1572 profile, however, makes the
gap `o(N^4)` and proves a genuinely larger coefficient-rigid class.

The PDE route states the stronger hypothesis demanded by K1599 rather than
calling removal of `k=0` dispersive. Pure-point spectral mass is excluded at
the level of the harmonic electric field. Three integrations by parts for an
atom-free `W^{3,1}` spectral density give integrable electric field and, with
zero asymptotic holonomy, integrable connection amplitude. K1598 and K1573 can
then be composed with an explicitly integrable remainder budget. This is a
conditional spectral theorem, not a nonlinear scattering construction.

SC-ACT-01/02/06 remain assertions and SC-META-53 remains uncertain. The
physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED. No
source, ledger, canon, paper, prediction, confirmation or public-posture state
moves.

## K1601 — heterogeneous translated-Gaussian Fisher sandwich

Let `mu=N(0,I)`, let `Omega` be positive, and let `pi` index positive
covariances `S_z` and means `m_z`. Define

```text
nu=int N(m_z,S_z) pi(dz),
alpha=E m_z,  C=Cov(m_z),  T=E S_z+C.                            (1)
```

Fisher convexity and the exact Gaussian formula give

```text
I_Omega(nu|mu)
 <=U:=E[m_z^T Omega m_z
          +Tr Omega(S_z+S_z^(-1)-2I)].                           (2)
```

The mixture has mean `alpha` and covariance `T`, so K1533 gives

```text
I_Omega(nu|mu)
 >=L:=alpha^T Omega alpha+Tr Omega(T+T^(-1)-2I).                  (3)
```

The mean-covariance terms cancel exactly because
`E[m_z^T Omega m_z]-alpha^T Omega alpha=Tr(Omega C)` and
`Tr Omega(E S_z-T)=-Tr(Omega C)`. Hence

```text
0<=U-L=Delta
 :=Tr Omega(E S_z^(-1)-T^(-1)).                                  (4)
```

Nonnegativity follows from operator convexity of inversion and
`T>=E S_z`. Equation (4) is valid without common covariance, common mean,
commutation, finite support, symmetry, or zero-mode localization. It is a
sandwich width, not the exact Fisher information of the mixture.

## K1602 — perturbative heterogeneous-mixture coefficient stability

Let `S_N^*` be K1572's larger-root profile. Restrict the components to the
stationary diagonal Gaussian class and assume, for `0<=epsilon_N<1`,

```text
(1-epsilon_N)S_N^* <= S_z <= (1+epsilon_N)S_N^*,
C <= eta_N S_N^*.                                                (5)
```

No commutation is needed for the following Loewner bounds:

```text
E S_z^(-1) <= (1-epsilon_N)^(-1)(S_N^*)^(-1),
T^(-1) >= (1+epsilon_N+eta_N)^(-1)(S_N^*)^(-1).                  (6)
```

Therefore

```text
Delta <= d_N Tr[Omega(S_N^*)^(-1)],
d_N=(1-epsilon_N)^(-1)-(1+epsilon_N+eta_N)^(-1).                 (7)
```

For the K1572 profile,
`omega_k/s_(N,k)=sqrt(omega_k^2+kappa_(g,N)^+)`; the cutoff has
`Theta(N^3)` modes with `omega_k` and `sqrt(kappa_(g,N)^+)` of order at most
`N`. Thus the trace in (7) is `O_g(N^4)`. K1572 bounds every component
energy below by `lambda_N^prof`, while linearity of the potential and
`q_0=I_Omega/4` give

```text
Q_N(nu)>=lambda_N^prof-Delta/4.                                  (8)
```

The class contains the profile itself. If `epsilon_N+eta_N->0`, then
`d_N->0`, and

```text
inf Q_N(nu)/N^4 -> h_g^prof.                                    (9)
```

This proves coefficient stability for a shrinking relative band of genuinely
heterogeneous covariances and arbitrary-mode translations. Fixed order-one
heterogeneity, spatial textures, phases, non-Gaussian components and
nonstationary laws remain open; (7) explicitly shows why the present argument
can lose order `N^4` there.

## K1603 — exact atomic-resonance exclusion

Let the harmonic electric field have a finite-dimensional pure-point part and
an absolutely continuous part,

```text
E_h(t)=sum_j(b_j e^(i lambda_j t)+conj)
      +int_0^infty[e^(it omega)F_+(omega)
                   +e^(-it omega)F_-(omega)]domega.              (10)
```

Any nonzero finite trigonometric polynomial has positive mean absolute value,
so its time `L1` norm diverges. K1589 and K1599 are one-frequency instances.
The exact nondispersive exclusion is therefore

```text
P_pp E_h=0.                                                       (11)
```

Assume additionally that `F_+` and `F_-` lie in `W^{3,1}`, are supported
away from zero, and their values and first two derivatives vanish at every
support endpoint. Three integrations by parts give, for `t>=1`,

```text
|E_h(t)|<=t^(-3)B_3,
B_3=||F_+'''||_1+||F_-'''||_1.                                  (12)
```

With `B_0=||F_+||_1+||F_-||_1`,

```text
int_0^infty |E_h|dt <= B_0+B_3/2.                               (13)
```

If the asymptotic harmonic holonomy is fixed to zero and
`a(t)=int_t^infty E_h(s)ds`, then

```text
int_0^infty |a(t)|dt
 <=int_0^infty t|E_h(t)|dt <=B_0/2+B_3,                          (14)
```

and `||a||_infty<=B_0+B_3/2`. The endpoint conditions are sufficient, not
necessary. The theorem excludes the full declared pure-point sector and
controls this atom-free spectral class; it does not derive the spectral
representation from the nonlinear Maxwell--matter equations.

## K1604 — conditional bare-energy and analytic-radius budget

Set

```text
B_E=B_0+B_3/2,  B_a=B_0/2+B_3.                                  (15)
```

K1603 gives `int|a|<=B_a`, `||a||_infty<=B_E`, and hence
`int|a|^2<=B_E B_a`. K1598 therefore yields

```text
E_0(t)<=E_0(0)
 exp(2|e|B_a+(e^2/m)B_E B_a).                                   (16)
```

This closes the exact `D'` and `M'` normal-form expenditure in the declared
spectral class. Let `R(t)>=0` collect the separately estimated curvature,
oscillatory-Maxwell, current, radial and other hierarchy coefficients, with
`B_R=int R<infinity`. If the K1573 moving-radius inequality holds with
effective coefficient

```text
B_A(t)<=|e||a(t)|+R(t),                                          (17)
```

then the choice `-rho'=C_m B_A/4` gives

```text
rho_infty>=rho_0-(C_m/4)(|e|B_a+B_R).                            (18)
```

Thus the explicit budget

```text
(C_m/4)(|e|B_a+B_R)<rho_0                                      (19)
```

preserves a positive limiting analytic radius. Equations (16)--(19) are a
conditional closure theorem, not a proof that the nonlinear GU/source system
has the spectral representation, the remainder bound, global coercivity, a
physical quotient, or a source-owned Hamiltonian.

## K1605 — protected integration and hostile bookend

The bridge census is now 320 rows: 241 satisfied, ten conditional, 65 excluded
and four missing. K1601 identifies the exact general Gaussian-mixture sandwich
width. K1602 closes the shrinking relative heterogeneous band, not order-one
heterogeneity or unrestricted states. K1603 excludes the declared atomic
resonant sector and proves an atom-free spectral decay theorem, but assumes the
spectral representation and endpoint regularity. K1604 composes an explicit
positive-radius budget while leaving the nonlinear/source-owned inputs open.

The hostile quantum check mutates the relative band into fixed order-one
heterogeneity, drops K1572 component admissibility, or calls a Fisher sandwich
an exact mixture formula. The hostile PDE check restores a spectral atom,
drops endpoint conditions or zero asymptotic holonomy, or promotes conditional
coefficients to a nonlinear source-owned flow. None of those transfers is
licensed.

The next quantum wake is a cutoff-uniform bound for order-one precision
heterogeneity or a genuinely non-Gaussian/nonstationary Fisher-defect theorem.
The next PDE wake is to derive K1603's atom-free spectral measure and K1604's
integrable remainder from one source-owned nonlinear action/domain, or to find
a cancellation requiring weaker decay. The source-owned
action/measure/Hamiltonian tuple remains a separate admission gate.
