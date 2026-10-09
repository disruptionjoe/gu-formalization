---
title: "Profiled cat rigidity and angular-holonomy cancellation"
status: active_research
document_role: exploration
target_claim: INTERNAL_TARGET__NEGATIVE_DEFECT_CAT_AND_ANGULAR_HOLONOMY_CANCELLATION
created: "2026-10-09"
updated_at: "2026-10-09"
---

# Profiled cat rigidity and angular-holonomy cancellation

> **GU-COMPARATOR-ROUTING:** This artifact studies a repository-owned
> finite-cutoff quartic Hamiltonian and an opposite-charge periodic
> gauge--matter control. It is not a source-native GU action, physical state
> space, observed carrier, prediction, confirmation, or falsification of a
> registered source claim. Conventional comparator conclusions bind only the
> models stated here.
>
> **Classification:**
> `INTERNAL_TARGET__CONDITIONAL_MATHEMATICAL_CONTROL__NO_SOURCE_VERDICT`

```yaml
gu-typed-objects:
  carrier: symmetric_profiled_gaussian_mixture_plus_equal_mode_opposite_charge_periodic_sector
  pairing_or_form: weighted_relative_fisher_form_quartic_schrodinger_form_and_harmonic_adapted_energy
  real_structure: real_finite_q_space_with_oppositely_charged_complex_scalar_pair
  grading: gaussian_mixture_component_and_charge_power_Q_n
  action_owner: repository_control_not_source_owned
  target_object: leading_negative_defect_cat_effect_and_angular_holonomy_work
  observed_intertwiner: UNTYPED
```

## Scope and preflight bookend

The quantum route switches away from a third local residual refinement. The
strongest explicit global negative-defect challenger already present in the
repository is the symmetric two-well mixture. Here its two components are the
sign-reflected K1572 profiled Gaussians. Fisher convexity gives an upper bound;
K1533 applied to the mixture covariance gives the matching lower sandwich.
The resulting rank-one gap decides whether this concrete `-Theta(N^4)` defect
changes the leading coefficient.

The PDE route keeps K1589's exact two-species homogeneous orbit but does not
ask energy to make `int|dot a|` finite. It retains the sign of the harmonic
work and tests the equal-mode opposite-charge symmetry before taking absolute
values. This isolates angular motion of the holonomy from radial motion of its
amplitude.

SC-ACT-01/02/06 remain assertions and SC-META-53 remains uncertain. The
physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED. No
source, ledger, canon, paper, prediction, confirmation or public-posture state
moves.

## K1591 — exact Fisher sandwich for the symmetric profiled cat

Use the real covariance coordinates of K1533. Let `mu=N(0,I)`, let `Omega`
be the positive free-frequency matrix, and let

```text
nu_+=N(m,S),  nu_-=N(-m,S),  nu_cat=(nu_++nu_-)/2,                 (1)
```

where `S` is positive and `m` is the constant zero-mode mean vector. Write
`I_Omega` for weighted relative Fisher information. Convexity of Fisher
information under mixing and the exact Gaussian formula give

```text
I_Omega(nu_cat|mu)
 <= U:=m^T Omega m+Tr[Omega(S+S^(-1)-2I)].                         (2)
```

The cat has mean zero and covariance

```text
T=S+mm^T.                                                         (3)
```

K1533's all-density fixed-moment extremality therefore gives

```text
I_Omega(nu_cat|mu)
 >= L:=Tr[Omega(T+T^(-1)-2I)].                                    (4)
```

The linear covariance and mean terms cancel between (2) and (4). The
Sherman--Morrison identity yields the exact sandwich width

```text
U-L=Tr[Omega(S^(-1)-T^(-1))]
   =[m^T S^(-1)Omega S^(-1)m]/[1+m^T S^(-1)m].                    (5)
```

For K1572's stationary diagonal profile, `m` is the zero-mode eigenvector.
If its `S` and `Omega` eigenvalues there are `s_(N,0)` and `omega_0`, then

```text
0<=U-I_Omega(nu_cat|mu)
 <=omega_0 |m|^2/[s_(N,0)(s_(N,0)+|m|^2)]
 <=omega_0/s_(N,0)
 =sqrt(omega_0^2+kappa_(g,N)^+)=Theta_g(N).                        (6)
```

Since the positive cat wavefunction has `q_0=I_Omega/4`, mixing can save at
most order `N` of free energy relative to either profiled component. No
separation or overlap asymptotic is needed.

## K1592 — a leading negative defect does not move this coefficient

At each spatial point a component has law `N(plus_or_minus h_N,v_N)`. The
mixture has mean zero, variance `v_N+h_N^2`, and fourth central moment

```text
h_N^4+6h_N^2v_N+3v_N^2.
```

Its defect relative to its moment-matched Gaussian is therefore

```text
[h_N^4+6h_N^2v_N+3v_N^2]-3(v_N+h_N^2)^2=-2h_N^4
 =-Theta_g(N^4).                                                   (7)
```

This is a genuinely nonperturbative negative-defect family outside K1577's
nonnegative-defect class. Nevertheless the Wick polynomial is even and
expectation is linear in the law, so the cat interaction equals the
interaction of either sign-reflected profiled Gaussian exactly. If
`lambda_N^prof` is K1572's component energy and `Q_N^cat` the cat Rayleigh
quotient, (6) gives

```text
lambda_N^prof-(1/4)sqrt(omega_0^2+kappa_(g,N)^+)
 <=Q_N^cat<=lambda_N^prof.                                        (8)
```

Consequently

```text
Q_N^cat/N^4 -> h_g^prof.                                          (9)
```

The symmetric profiled cat cannot change the leading coefficient. More
sharply, its possible gain is only `O_g(N)`, so it cannot account for
K1587's `Theta_g(N^(5/2))` residual Ritz descent. The latter requires a
higher-chaos or more spatially structured deformation. Equation (9) is not an
unrestricted coefficient theorem: asymmetric, multimodal, nonstationary and
spatial sign-texture laws remain outside this calculation.

## K1593 — opposite charges cancel angular holonomy work

For a prescribed differentiable harmonic connection `a(t)`, a species of
charge `q` has Fourier energy

```text
H_q=(1/2)sum_k [|dot phi_(q,k)|^2
                +(m^2+|k-q a|^2)|phi_(q,k)|^2],                   (10)
```

and its equation gives the exact work identity

```text
H_q'=-q dot(a) dot sum_k (k-q a)|phi_(q,k)|^2.                    (11)
```

Take charges `+e` and `-e`. On any interval where their same-`k` amplitudes
are paired,

```text
|phi_(+,k)|^2=|phi_(-,k)|^2=:w_k,                                 (12)
```

the momentum-linear terms cancel before absolute values:

```text
H_+'+H_-'
 =2e^2 dot(a) dot a sum_k w_k
 =e^2 d(|a|^2)/dt sum_k w_k.                                     (13)
```

Thus angular holonomy motion is exactly invisible to the paired adapted
energy whenever `|a|` is constant, even if `int|dot a|` diverges. Only radial
amplitude variation remains in (13). The same-mode condition is load-bearing
and need not be preserved for general nonzero Fourier data; the homogeneous
`k=0` equal-species sector is invariant and supplies the exact control.

## K1594 — the periodic orbit preserves every charge-analytic tier

K1589 has only the homogeneous `k=0` modes, equal species amplitudes,
constant `|a|=A`, and constant scalar amplitude `R`. It therefore satisfies
(12)--(13) for all time and has

```text
H_+(t)+H_-(t)=constant                                              (14)
```

despite `|dot a|=A Omega>0`. The global charge generator acts on the two
species with eigenvalues of equal absolute value. Applying any power `Q^n`
multiplies the paired matter energies by the same even factor on both species,
so (13) holds at every charge tier. Every convergent positive charge-analytic
sum of these adapted tier energies is constant on the orbit.

This closes the interpretation left open by K1589: the orbit disproves an
energy-only proof of `dot a in L1_t`, but it is not an obstruction to every
cancellation-based positive-radius mechanism. On the orbit itself the signed
opposite-charge/angular cancellation removes the entire infinite-variation
cost. A global theorem still needs control of unequal-mode imbalance,
nonconstant `|a|`, oscillatory Maxwell modes, currents, radial terms and
nonlinear continuation.

## K1595 — protected integration and hostile bookend

The bridge census is now 310 rows: 231 satisfied, ten conditional, 65 excluded
and four missing. K1591--K1592 exclude one explicit global negative-defect
family from changing the profiled `N^4` coefficient, but do not determine the
unrestricted coefficient. K1593--K1594 exhibit an exact cancellation that
survives infinite angular holonomy variation, but do not prove a global
positive-radius flow.

The hostile quantum check requires a symmetric mixture of the two
sign-reflected K1572 profiled components, their common covariance and the
zero-mode rank-one update. It forbids transfer to arbitrary negative-defect
states. The hostile PDE check requires equal same-mode amplitudes of charges
`+e` and `-e`; it forbids replacing that condition by neutrality alone or
claiming cancellation of radial and nonhomogeneous remainders.

The next quantum wake is a different nonperturbative family or a global
nonlinear Fisher/negative-defect theorem capable of deciding the unrestricted
coefficient. The next PDE wake is a stable cancellation/normal form for
unequal nonzero modes plus the curvature/current/radial remainder, or a
dispersive hypothesis excluding the nondecaying sector. The source-owned
action/measure/Hamiltonian tuple remains a separate admission gate.
