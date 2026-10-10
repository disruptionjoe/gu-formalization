---
title: "Bounded-profile unequal-amplitude orbit rigidity"
status: active_research
document_role: exploration
target_claim: INTERNAL_TARGET__BOUNDED_PROFILE_UNEQUAL_AMPLITUDE_ORBIT_RIGIDITY
created: "2026-10-09"
updated_at: "2026-10-09"
---

# Bounded-profile unequal-amplitude orbit rigidity

> **GU-COMPARATOR-ROUTING:** This artifact studies a repository-owned
> finite-cutoff quartic Hamiltonian. It is not a source-native GU action,
> physical state space, observed carrier, prediction, confirmation, or
> falsification of a registered source claim. Conventional comparator
> conclusions bind only the model stated here.
>
> **Classification:**
> `INTERNAL_TARGET__CONDITIONAL_MATHEMATICAL_CONTROL__NO_SOURCE_VERDICT`

```yaml
gu-typed-objects:
  carrier: gaussian_smoothed_known_profile_complete_cube_translation_phase_orbits
  pairing_or_form: weighted_relative_fisher_form_plus_integrated_wick_square
  real_structure: real_trigonometric_cutoff_coordinates
  grading: macroscopic_positive_frequency_cube_and_four_parameter_orbit
  action_owner: repository_control_not_source_owned
  target_object: bounded_dynamic_range_unequal_amplitude_leading_gap_sign
  observed_intertwiner: UNTYPED
```

## Scope and preflight bookend

K1656--K1659 close every fixed admissible amplitude and every known phase
pattern when all complete-cube coefficients have the same magnitude.  The
first genuinely different amplitude question is whether a deterministic
macroscopic profile can concentrate the negative fourth defect more cheaply
than the Fisher price.  This wave proves that no uniformly positive bounded
profile can do so.  The proof does not require spatial regularity, slow
variation, angular flatness, or a Rudin--Shapiro sign pattern.

Retain K1656's translated positive-frequency cube `K_N`, with
`d_N/N^3<=1/512` and `omega_k/N>=sqrt(3)/4`.  Fix deterministic known phases
`|c_(N,k)|=1` and deterministic known weights

```text
0<rho_-<=rho_(N,k)<=rho_+<infinity.                 (1)
```

For fixed `eta>0`, define

```text
R_N(x)=sum_(k in K_N) sqrt(rho_(N,k)) c_(N,k)e^(ikx),
M_N(x)=sqrt(2eta/N) Re[e^(iTheta)R_N(x+Y)].         (2)
```

Add the diagonal Gaussian residual that matches the exact K1572 covariance.
The declared admissible class has a uniform residual margin

```text
t_(N,k):=eta rho_(N,k)sqrt(omega_k^2+kappa_N)/N
          <=1-epsilon                              (3)
```

for some fixed `epsilon>0` and all selected modes for all sufficiently large
`N`.  This class contains arbitrary unequal bounded positive profiles.  It
does not contain profiles whose lower bound degenerates, sparse supports,
unknown magnitudes or phases, a latent dimension growing with `N`, mixtures
of unrelated orbits, or non-orbit dependence.

SC-ACT-01/02/06 remain assertions and SC-META-53 remains uncertain.  The
physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED.
K1145/K1150 remain 0/7.  No source, ledger, canon, paper, prediction,
confirmation, or public-posture state moves.

## K1661 — weighted fourth-defect floor

Put `S_(rho,N)=sum_k rho_(N,k)` and use normalized Haar measure.  Uniform
translation and global phase give

```text
E M_N(x)^2=(eta/N)S_(rho,N),
E M_N(x)^4=(3eta^2/(2N^2))int|R_N|^4.             (4)
```

Consequently the exact integrated fourth cumulant is

```text
D_(M,N)=(3eta^2/(2N^2))
          [int|R_N|^4-2S_(rho,N)^2]
        >=-(3eta^2/N^2)S_(rho,N)^2.               (5)
```

Only `int|R_N|^4>=0` is used.  Cauchy then converts the potentially coherent
`l1` mass into the same `l2` profile quantity paid by Fisher:

```text
S_(rho,N)^2<=d_N sum_(k in K_N)rho_(N,k)^2.        (6)
```

Thus

```text
gD_(M,N)>=-3g eta^2(d_N/N^2)sum_k rho_(N,k)^2.    (7)
```

This is a lower bound, not an exact defect formula or a flatness claim.

## K1662 — bounded known profiles preserve posterior localization

The complex selected-mode observation has known coefficient
`sqrt(rho_(N,k))c_(N,k)`.  Multiply by `conjugate(c_(N,k))` and divide by
`sqrt(rho_(N,k))`.  Equations (1) and (3), together with fixed-shell K1572
bounds, turn the channel into

```text
W'_k=a exp(i(Theta+k dot Y))+xi'_k,                (8)
```

where `a^2=Theta(eta)>0` and the independent circular noise variances are
uniformly bounded above and below.  K1653's disjoint adjacent-pair estimators
therefore apply without estimating any profile entry.  Translation risk is
`O(d_N^-1)`, global-phase risk is `O(N^2/d_N)=O(N^-1)`, and normalized
per-mode orbit prediction risk is `O(N^-1)`.

Posterior means minimize the original score-weighted quadratic risk.  The
bounded profile and residual margin keep the coordinate score weights at
`O_(g,eta,rho_+,epsilon)(N)`, so

```text
M_(F,N)=O_(g,eta,rho_-,rho_+,epsilon)(N^3),
R_(Omega,N)/4=C_(F,N)-O(N^3).                     (9)
```

The lower bound `rho_->0` is load-bearing for this proof.  A vanishing profile
floor may leave a different effective support or an unbounded normalized
noise variance and remains open.

## K1663 — an `l2` profile-Fisher coercivity inequality

Write

```text
r_(N,k)=sqrt(omega_k^2+kappa_N)/N,
t_(N,k)=eta rho_(N,k)r_(N,k).                     (10)
```

The covariance increment is
`delta s_k=eta rho_(N,k)omega_k/N`, and the exact component term is

```text
C_(F,N)=(N/2)sum_k
 r_(N,k)t_(N,k)/[1-t_(N,k)].                      (11)
```

The pointwise inequality `t/(1-t)>=4t^2` for `0<t<1` gives

```text
C_(F,N)>=2eta^2N sum_k rho_(N,k)^2r_(N,k)^3.      (12)
```

This is the needed coercive pairing: K1661 charges the defect to
`sum rho_k^2`, and (12) pays that same quantity with the profiled frequency
weight.  No equality of coefficient magnitudes or regularity of the profile is
used.  The inequality controls the translated-component Fisher term; K1662 is
still needed to show that fixed-dimensional mixing removes only `O(N^3)`.

## K1664 — every admissible bounded positive profile loses

Combine K1661--K1663 with K1637.  For `0<g<=8sqrt(3)`, the shell radius and
`d_N/N^3<=1/512` give

```text
2r_(N,k)^3-3g d_N/N^3
 >=3sqrt(3)/32-3sqrt(3)/64
 =3sqrt(3)/64.                                    (13)
```

For `g>=8sqrt(3)`, K1658's profile self-consistency bound gives, eventually,
`r_(N,k)^3>=(g/2)^(3/2)`, so

```text
2r_(N,k)^3-3g d_N/N^3
 >=2(g/2)^(3/2)-3g/512>0.                         (14)
```

Therefore

```text
C_(F,N)+gD_(M,N)
 >=eta^2N sum_k rho_(N,k)^2 m_g,                  (15)
```

with `m_g>0`.  Since `rho_k>=rho_->0` and `d_N=Theta(N^3)`, the right side is
`Theta(N^4)`.  K1662 subtracts only `O(N^3)`, hence

```text
Q_N[Law(X_N)]-lambda_N^statG>=c_(g,eta,rho_-,epsilon)N^4        (16)
```

for all sufficiently large `N`.

Thus arbitrary known deterministic unequal amplitudes with uniformly bounded
positive dynamic range cannot change the leading coefficient inside the
declared complete-cube four-parameter orbit class.  The theorem is not a
sparse-profile, unknown-profile, growing-latent, non-orbit, or unrestricted
Fisher/negative-defect coercivity theorem.

## K1665 — protected integration and hostile bookend

The bridge census is now 380 rows: 301 satisfied, ten conditional, 65
excluded, and four missing.  K1661 replaces equal-magnitude defect counting by
a weighted `l1`-to-`l2` bound.  K1662 proves that known bounded profiles retain
the K1653 posterior rate.  K1663 makes the profile Fisher cost coercive in the
same `l2` quantity, and K1664 proves a positive `Theta(N^4)` gap throughout the
admitted class.

Hostile review rejects dropping complete-cube support, known phases and
magnitudes, the fixed four-dimensional orbit, the uniform positive profile
floor and ceiling, the uniform residual margin, the K1572 covariance match,
or fixed `eta`.  It also rejects treating (5) as equality, treating (12) as the
output Fisher without K1662, or transferring the result to sparse,
degenerating, unknown-profile, growing-latent, non-orbit, source-owned, or
physical sectors.

The next quantum wake is a degenerating or sparse amplitude profile, unknown
profile, growing latent dimension or non-orbit macroscopic law, or a genuinely
unrestricted Fisher/negative-defect coercivity theorem.  The independent
physical wake remains a source-owned action/measure/Hamiltonian, admissible
domain, physical state and observation tuple.

## Postflight bookend

Equal coefficient magnitude was not the load-bearing source of K1659's sign.
The real mechanism is the shared `l2` profile scale: Cauchy charges every
bounded unequal-amplitude fourth defect to that scale, and the exact K1572
component Fisher term pays it with a strictly larger cube-uniform coefficient.
What remains open is precisely the loss of bounded-profile observability or of
the fixed orbit architecture.  Protected source, ledger, canon, paper,
prediction, confirmation, and public-posture states are unchanged.
