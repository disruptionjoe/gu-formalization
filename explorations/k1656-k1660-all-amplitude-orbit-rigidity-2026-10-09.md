---
title: "All-amplitude rigidity of complete-cube translation/phase orbits"
status: active_research
document_role: exploration
target_claim: INTERNAL_TARGET__ALL_AMPLITUDE_COMPLETE_CUBE_ORBIT_RIGIDITY
created: "2026-10-09"
updated_at: "2026-10-09"
---

# All-amplitude rigidity of complete-cube translation/phase orbits

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
  carrier: gaussian_smoothed_known_phase_complete_cube_translation_phase_orbits
  pairing_or_form: weighted_relative_fisher_form_plus_integrated_wick_square
  real_structure: real_trigonometric_cutoff_coordinates
  grading: macroscopic_positive_frequency_cube_and_four_parameter_orbit
  action_owner: repository_control_not_source_owned
  target_object: all_admissible_amplitude_leading_gap_sign
  observed_intertwiner: UNTYPED
```

## Scope and preflight bookend

K1651--K1654 prove that the Rudin--Shapiro translation/phase orbit pays its
full component Fisher ceiling at leading order and therefore loses for every
sufficiently small fixed amplitude.  The remaining family question is whether
its quadratic negative defect can dominate at a larger admissible amplitude.
This wave closes that question structurally and also removes the special
Rudin--Shapiro signs from the sign theorem.

Fix the translated positive-frequency cube

```text
K_N=b_N+{0,...,ell_N-1}^3,
b_N=(ceil(N/4),ceil(N/4),ceil(N/4)),
N/16<=ell_N<=N/8,     d_N=ell_N^3.                 (1)
```

For all sufficiently large `N`, this cube lies inside the cutoff, every mode
satisfies `omega_k/N>=sqrt(3)/4`, and
`d_N/N^3<=1/512`.  Let `R_N` have arbitrary known unit-modulus coefficients
on this complete cube.  Randomize the associated real field by translation
and global phase exactly as in K1647, use `A_N^2=eta/N`, and add the K1648
Gaussian residual so the total covariance is the exact K1572 profile.

The result is class-scoped.  It proves a positive leading gap for every fixed
`eta>0` for which the residual covariance remains positive.  It does not
control unequal coefficient magnitudes, growing latent dimension, a union or
mixture of unrelated orbits, arbitrary stationary anisotropic laws, or the
unrestricted ground-energy coefficient.

SC-ACT-01/02/06 remain assertions and SC-META-53 remains uncertain.  The
physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED.
K1145/K1150 remain 0/7.  No source, ledger, canon, paper, prediction,
confirmation, or public-posture state moves.

## K1656 — known phases do not obstruct posterior localization

Write the positive-frequency coefficient of the orbit as

```text
Z_k=A_N c_k exp(i(Theta+k dot Y)),   |c_k|=1.       (2)
```

After the K1648 covariance normalization, multiplication by the known
`conjugate(c_k)` turns the observation into

```text
W_k=a_k exp(i(Theta+k dot Y))+xi_k.                 (3)
```

The shell amplitudes and circular Gaussian noise variances are uniformly
bounded above and below.  K1653's disjoint adjacent-pair estimators therefore
apply verbatim: the three translation risks are `O(d_N^-1)`, the residual
global-phase risk is `O(N^2/d_N)=O(N^-1)`, and the normalized per-mode orbit
prediction risk is `O(N^-1)`.  Posterior means minimize quadratic risk, so

```text
M_(F,N)=O_(g,eta,R)(N^3),
R_(Omega,N)/4=C_(F,N)-O_(g,eta,R)(N^3).             (4)
```

The constant may depend on the fixed coefficient pattern through only its
known demodulation convention; no unknown phase is estimated separately.
This is not localization for unknown coefficients, unequal magnitudes,
sparse supports, or a latent dimension growing with `N`.

## K1657 — a universal fourth-defect floor

For normalized Haar measure, put

```text
I_(4,N)=int |R_N|^4 >=0.                            (5)
```

Uniform global phase gives, at every spatial point after translation average,

```text
E M_N(x)^2=A_N^2d_N,
E M_N(x)^4=(3/2)A_N^4 I_(4,N).                     (6)
```

Therefore every deterministic unit-modulus coefficient pattern obeys

```text
D_(M,N)=(3/2)A_N^4[I_(4,N)-2d_N^2]
         >=-3A_N^4d_N^2
         =-3 eta^2 d_N^2/N^2.                     (7)
```

This floor is deliberately pattern-blind.  K1651's Rudin--Shapiro value is
much sharper, but (7) is strong enough to decide the complete class once the
profile Fisher price is used.  Nonnegativity of `I_4` is not probabilistic
independence, flatness, or a lower bound for an arbitrary unequal-amplitude
law.

## K1658 — the profiled Fisher price is quadratic-uniform in amplitude

Let `kappa_N=kappa_(g,N)^+` be K1572's minimizing profile parameter and set

```text
r_(N,k)=sqrt(omega_k^2+kappa_N)/N,
t_(N,k)=eta r_(N,k),
s_(N,k)^*=omega_k/sqrt(omega_k^2+kappa_N).         (8)
```

K1648 residual positivity is exactly `0<t_(N,k)<1` on the selected cube.
Since `delta s_k=eta omega_k/N`, its component Fisher term is

```text
C_(F,N)=(N/2)sum_(k in K_N)
                 eta r_(N,k)^2/[1-eta r_(N,k)].    (9)
```

The elementary identity

```text
t/(1-t)>=4t^2,  0<t<1,
```

is equivalent to `(2t-1)^2>=0`.  It removes the apparent small-amplitude
restriction:

```text
C_(F,N)>=2N eta^2 sum_(k in K_N) r_(N,k)^3.        (10)
```

There are two uniform regimes.  If `0<g<=8sqrt(3)`, (1) and (10) give

```text
C_(F,N)/N^4
 >=2 eta^2(d_N/N^3)(sqrt(3)/4)^3.                 (11)
```

If `g>=8sqrt(3)`, use K1572's continuum parameter `kappa_g`, where

```text
kappa_g=24g D(kappa_g),
D(kappa)=(1/2)int_[-1,1]^3
  [|q|^-1-(|q|^2+kappa)^(-1/2)]dq.                (12)
```

Because `|q|<=sqrt(3)`, rationalizing the integrand gives

```text
D(kappa)>=4kappa/
 [sqrt(3)sqrt(3+kappa)(sqrt(3)+sqrt(3+kappa))].    (13)
```

Equations (12)--(13) imply

```text
kappa_g>=16sqrt(3)g-3>=g.                          (14)
```

K1572's `kappa_N/N^2 -> kappa_g` then makes
`r_(N,k)^3>=(g/2)^(3/2)` for all selected modes and all sufficiently large
`N`.  Thus (10) supplies a leading positive coefficient proportional to
`eta^2` even when `eta` is not small.  The divergence of (9) near residual
covariance loss is retained rather than hidden by a linearized estimate.

## K1659 — every admissible complete-cube orbit loses at leading order

Let `c_N=d_N/N^3<=1/512`.  Combining K1657 with K1637 gives the worst possible
negative leading contribution

```text
gD_(M,N)/N^4>=-3g eta^2 c_N^2.                    (15)
```

For `g<=8sqrt(3)`, the right side of (11) is at least
`2eta^2c_N(3sqrt(3)/64)`, while

```text
3gc_N<=3sqrt(3)/64.                                (16)
```

The Fisher coefficient therefore exceeds the worst defect by a fixed positive
margin.  For `g>=8sqrt(3)`, (10), (14), and K1572 convergence give

```text
C_(F,N)/N^4>=2eta^2c_N(g/2)^(3/2),                (17)
```

whereas (15) is at most `3g eta^2c_N^2`; since `g>1` and
`c_N<=1/512`, (17) again has a fixed positive margin.  Finally K1656 makes the
posterior missing term only `O(N^3)`.  Hence, for every fixed `g>0`, every
fixed admissible `eta>0`, and every known unit-modulus coefficient pattern on
the complete cube,

```text
Q_N[Law(X_N)]-lambda_N^statG >= c_(g,eta)N^4       (18)
```

for all sufficiently large `N`.

This closes every amplitude and angular coefficient pattern inside the
declared four-parameter complete-cube orbit class.  A coefficient-changing
competitor must leave at least one load-bearing hypothesis: equal-magnitude
complete-cube covariance, fixed latent translation/global-phase dimension,
known deterministic pattern, or Gaussian smoothing matched to the K1572
profile.  The theorem is not unrestricted Fisher/negative-defect coercivity.

## K1660 — protected integration and hostile bookend

The bridge census is now 375 rows: 296 satisfied, ten conditional, 65
excluded, and four missing.  K1656 extends leading score saturation to known
unit phases.  K1657 bounds every angular pattern's negative defect.  K1658
uses the exact profile rather than K1654's linear lower bound to control every
admissible amplitude.  K1659 then proves a positive `Theta(N^4)` gap across
the entire declared orbit class.

Hostile review rejects dropping complete-cube support, equal coefficient
magnitudes, known phases, fixed four-dimensional latent orbit, K1572 covariance
matching, fixed positive admissible amplitude, or the explicit shell.  It also
rejects replacing the posterior `O(N^3)` estimate by exact label recovery,
claiming arbitrary anisotropic stationary coercivity, or transferring the
result to a source-owned action, physical state, prediction, or GU verdict.

The next quantum wake is a genuinely different macroscopic law with unequal
mode amplitudes, growing latent dimension or non-orbit correlations, or an
unrestricted Fisher/negative-defect coercivity theorem.  The independent
physical wake remains a source-owned action/measure/Hamiltonian, admissible
domain and observation tuple.

## Postflight bookend

The leading-defect translation/phase mechanism is now closed throughout its
admissible amplitude range and throughout its deterministic equal-magnitude
angular class.  The profile itself supplies the missing large-amplitude
coercivity: near small coupling the shell radius pays the price, and at larger
coupling K1572 self-consistency raises the Fisher weight.  The unrestricted
anisotropic sector remains open, but it can no longer reuse a fixed
four-parameter complete-cube orbit as a coefficient-changing witness.
Protected source, ledger, canon, paper, prediction, confirmation, and
public-posture states are unchanged.
