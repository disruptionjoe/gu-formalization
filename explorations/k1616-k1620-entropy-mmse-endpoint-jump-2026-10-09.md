---
title: "Information-theoretic Gaussian-mixture rigidity and endpoint-jump obstruction"
status: active_research
document_role: exploration
target_claim: INTERNAL_TARGET__ENTROPY_MMSE_RIGIDITY_AND_ENDPOINT_JUMP_OBSTRUCTION
created: "2026-10-09"
updated_at: "2026-10-09"
---

# Information-theoretic Gaussian-mixture rigidity and endpoint-jump obstruction

> **GU-COMPARATOR-ROUTING:** This artifact studies a repository-owned
> finite-cutoff quartic Hamiltonian and a conditional harmonic spectral model.
> It is not a source-native GU action, physical state space, observed carrier,
> prediction, confirmation, or falsification of a registered source claim.
> Conventional comparator conclusions bind only the models stated here.
>
> **Classification:**
> `INTERNAL_TARGET__CONDITIONAL_MATHEMATICAL_CONTROL__NO_SOURCE_VERDICT`

```yaml
gu-typed-objects:
  carrier: shared_covariance_arbitrary_mode_gaussian_location_mixtures_plus_piecewise_bv_harmonic_spectral_primitives
  pairing_or_form: weighted_relative_fisher_form_gaussian_channel_mmse_and_background_adapted_charge_energy
  real_structure: real_finite_q_space_with_real_flat_harmonic_connection
  grading: gaussian_location_label_and_charge_power_Q_n
  action_owner: repository_control_not_source_owned
  target_object: information_controlled_missing_fisher_energy_and_endpoint_jump_holonomy_tail
  observed_intertwiner: UNTYPED
```

## Scope and preflight bookend

K1612 bounds a heterogeneous Gaussian mixture by summing pairwise affinities.
For equal weights this introduces the Renyi-half count `M_N`, and the bound
becomes inconclusive at `M_N` of order `N^3`. That threshold is not intrinsic
when every component has one common covariance. In the common-covariance
location channel, K1606's missing Fisher information is exactly a weighted
posterior mean-square error. The Gaussian I-MMSE identity controls it by the
mutual information carried through the channel, and a discrete label carries
at most its Shannon entropy. Polynomially many components, including the
critical and supercritical counts left open by K1612, are therefore harmless
in this class.

The independent spectral arc tests K1613's zero-endpoint-trace hypothesis.
A nonzero jump of a compact piecewise regular primitive produces a `t^-1`
finite exponential polynomial. Such a polynomial has positive mean absolute
value unless every jump vanishes, forcing logarithmic divergence of the
holonomy `L1` budget. Derivative jumps remain allowed because they enter one
order later, at `t^-2`.

SC-ACT-01/02/06 remain assertions and SC-META-53 remains uncertain. The
physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED.
LT-SM8, LT-GR6b, RA-F1 and AC-F1 do not move. No source, ledger, canon,
paper, prediction, confirmation, or public-posture state moves.

## K1616 — common-covariance missing information is a Gaussian-channel MMSE

Let `M_N` be any square-integrable random location, let
`G_N ~ N(0,S_N)` be independent, and put `X_N=M_N+G_N`. Every conditional
component is the translated Gaussian `N(M_N,S_N)`. Assume `S_N` is stationary
diagonal and lies in a fixed relative band around the K1572 profile. Define

```text
A_N=S_N^(-1/2)M_N,
B_N=S_N^(-1/2) Omega_N S_N^(-1/2),
Lambda_N=||B_N||_op=max_k omega_k/s_(N,k)=O_g(N).               (1)
```

The component score is `u_M(x)=-S_N^(-1)(x-M)`. Conditional expectation gives
the mixture score, so K1606's missing Fisher term is exactly

```text
D_N=E[(M_N-E[M_N|X_N])^T S_N^(-1)Omega_N S_N^(-1)
      (M_N-E[M_N|X_N])]
   =E[(A_N-E[A_N|A_N+Z_N])^T B_N
      (A_N-E[A_N|A_N+Z_N])],                                  (2)
```

where `Z_N~N(0,I)`. Hence

```text
D_N<=Lambda_N mmse(A_N|A_N+Z_N).                               (3)
```

For `Y_t=sqrt(t)A_N+Z_N`, Gaussian I-MMSE gives

```text
I(A_N;Y_1)=(1/2)int_0^1 mmse(A_N|Y_t)dt.
```

The MMSE is nonincreasing in `t`, so

```text
mmse(A_N|A_N+Z_N)<=2I(A_N;A_N+Z_N)=2I(M_N;X_N).                (4)
```

Combining (2)--(4),

```text
0<=E Q_N(N(M_N,S_N))-Q_N(Law(X_N))
  =D_N/4<=(Lambda_N/2)I(M_N;X_N).                              (5)
```

The equality uses linearity of the quartic potential in the law, exactly as
in K1606. No separation, atom count, discreteness, centeredness, support
diameter, or mean bound is used. The common covariance and Gaussian additive
channel are load-bearing.

## K1617 — Shannon entropy crosses the Renyi-half count boundary

If `M_N=m_(N,Z_N)` for a discrete label with weights `p_(N,i)`, data
processing gives

```text
I(M_N;X_N)<=I(Z_N;X_N)<=H(p_N).                                (6)
```

K1572 bounds every translated stationary diagonal Gaussian component below
by `lambda_N^prof`. Equations (5)--(6) therefore give

```text
lambda_N^prof-(Lambda_N/2)H(p_N)<=Q_N(Law(X_N)),
H(p_N)=o(N^3)  ==>  Q_N(Law(X_N))/N^4>=h_g^prof-o(1).           (7)
```

Since the class contains the profiled Gaussian, its infimum coefficient is
`h_g^prof`. For equal weights, `H(p_N)=log M_N`; thus every
`M_N=exp(o(N^3))` is coefficient-rigid. In particular, polynomial component
counts of any fixed degree cross K1612's `M_N=o(N^3)` pair-sum boundary by a
wide margin. This does not close label-dependent covariance mixtures: there
is then no single Gaussian channel whose posterior MMSE is K1606's missing
component-score variance.

## K1618 — continuous arbitrary-mode location laws

The same argument needs no discrete label. Any square-integrable location law
over one common stationary diagonal covariance obeys (5). Consequently

```text
I(M_N;M_N+G_N)=o(N^3)
  ==> Q_N(Law(M_N+G_N))/N^4>=h_g^prof-o(1).                    (8)
```

This extends K1596's arbitrary zero-mode location law to arbitrary cutoff
modes, under an information condition rather than a zero-mode rank-one
identity. A convenient sufficient condition follows from Gaussian channel
capacity. With `A_N=S_N^(-1/2)M_N`,

```text
I(M_N;X_N)<=1/2 log det(I+Cov(A_N)).                            (9)
```

Therefore `log det(I+Cov(A_N))=o(N^3)` implies the same coefficient rigidity.
The theorem permits continuous, asymmetric, correlated and multimodal
location laws. It does not permit non-Gaussian component shapes, varying
covariances, phases, spatial textures, or nonstationary quantum states.

## K1619 — endpoint jumps force a nonintegrable holonomy tail

Let a real compactly supported primitive `G` be `W^{2,1}` on finitely many
open intervals, with one-sided endpoint values. Merge coincident endpoints
and let `J_r` be the resulting jumps at distinct points `a_r`. Distributional
integration by parts gives

```text
widehat G(t)=-(1/(it))T(t)+O(t^-2),
T(t)=sum_r J_r exp(i t a_r).                                   (10)
```

The remainder is `O(t^-2)` when the intervalwise first derivative has bounded
variation. If any `J_r` is nonzero, linear independence of the distinct
characters makes `T` a nonzero finite exponential polynomial. Its Bohr mean
satisfies

```text
M(|T|)>0.                                                       (11)
```

Indeed, `M(|T|^2)=sum_r |J_r|^2>0`, while boundedness of `T` gives
`M(|T|)>=M(|T|^2)/||T||_infinity>0`. Averaging (10) on dyadic time shells then
yields a fixed positive contribution per logarithmic shell, and hence

```text
int_1^infinity |widehat G(t)|dt=infinity.                       (12)
```

Thus K1613's zero trace is sharp within this finite piecewise-BV class:
first-derivative jumps produce only the allowed `t^-2` measure term, but a
density endpoint jump produces a nonintegrable `t^-1` tail. The theorem says
nothing about generation of the spectral representation by nonlinear GU
dynamics, electric-field `L1`, curvature/current remainders, coercivity, or a
physical domain.

## K1620 — protected integration and hostile bookend

The bridge census is now 335 rows: 256 satisfied, ten conditional, 65
excluded, and four missing. K1616 identifies the common-covariance mixing
gain with a Gaussian-channel posterior MMSE and bounds it by mutual
information. K1617 replaces K1612's Renyi-half count by Shannon entropy for
discrete shared-covariance location mixtures, crossing every polynomial
critical/supercritical count. K1618 extends the result to continuous
arbitrary-mode location laws under an explicit information or covariance-
capacity condition. K1619 proves that nonzero endpoint jumps obstruct the
holonomy `L1` budget in the declared piecewise-BV class.

The hostile quantum check rejects covariance heterogeneity, non-Gaussian
component shapes, phase or nonstationary transfer, and any claim that Shannon
entropy controls the nominally broader K1612 class. The hostile spectral
check rejects cancellation of distinct nonzero jump characters, electric-
field `L1`, and promotion to nonlinear/source-owned dynamics. None is
licensed.

The next quantum wake is a valid information inequality for label-dependent
covariances or genuinely non-Gaussian/nonstationary component laws. The next
PDE wake is a source-owned nonlinear derivation of the atom-free zero-trace
primitive measure and the integrable curvature/current/radial remainder. The
source-owned action/measure/Hamiltonian tuple remains a separate admission
gate.

## Postflight bookend

The quantum route shows that K1612's critical component count is not a
physical coefficient threshold for shared-covariance translations. The
intrinsic quantity is information transmitted through the Gaussian channel,
not nominal component count or its Renyi-half surrogate. The result includes
continuous arbitrary-mode location laws but remains Gaussian and common-
covariance scoped.

The PDE route closes the easiest proposed relaxation of K1613: derivative
jumps are admissible, endpoint jumps are not, unless a different cancellation
mechanism changes the actual spectral object. No source, ledger, canon, paper,
prediction, confirmation, or public-posture state changes.
