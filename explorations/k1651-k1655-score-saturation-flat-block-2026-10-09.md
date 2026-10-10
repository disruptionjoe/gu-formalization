---
title: "Posterior-score saturation and the small-amplitude flat-block sign"
status: active_research
document_role: exploration
target_claim: INTERNAL_TARGET__TRANSLATION_PHASE_SCORE_SATURATION_AND_SIGN
created: "2026-10-09"
updated_at: "2026-10-09"
---

# Posterior-score saturation and the small-amplitude flat-block sign

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
  carrier: gaussian_smoothed_rudin_shapiro_translation_phase_orbits
  pairing_or_form: weighted_relative_fisher_form_plus_integrated_wick_square
  real_structure: real_trigonometric_cutoff_coordinates
  grading: macroscopic_fourier_cube_and_four_parameter_orbit
  action_owner: repository_control_not_source_owned
  target_object: leading_posterior_score_residual_and_small_amplitude_gap_sign
  observed_intertwiner: UNTYPED
```

## Scope and preflight bookend

K1646--K1648 leave one exact competition: the macroscopic translation/phase
orbit has a leading negative fourth cumulant, while Fisher convexity supplies
only a leading positive ceiling.  This wave resolves that competition for the
small-amplitude K1648 family.  It first sharpens the individual
Rudin--Shapiro fourth moment.  Independently, it rewrites the continuous
equal-covariance Gaussian channel by conditional variance and proves that the
four latent orbit parameters are consistently recoverable from the complete
Fourier cube.  The posterior missing-information term is then one power of
`N` below the component ceiling.

The conclusion is family-scoped.  The positive term is linear in the fixed
amplitude parameter `eta`, whereas the negative defect is quadratic.  Thus
every sufficiently small admissible fixed `eta` gives a positive leading gap,
not descent.  Larger amplitudes, another angular orbit, and unrestricted
stationary anisotropic laws remain open.

This extends K1606's finite-mixture score identity to the present continuous
equal-covariance channel; it does not rediscover or replace K1606.  The
correction registry contains no matching posterior-score, Rudin--Shapiro, or
macroscopic-correlation correction.  SC-ACT-01/02/06 remain assertions and
SC-META-53 remains uncertain.  The physics ledger stays 33 SAME / 22 DIFFERS
/ 31 NEEDS / 2 OVER-DETERMINED.  K1145/K1150 remain 0/7.  No source, ledger,
canon, paper, prediction, confirmation, or public-posture state moves.

## K1651 — exact individual Rudin--Shapiro fourth moments

Retain K1646's recursion

```text
P_(n+1)=P_n+z^(v_n)Q_n,
Q_(n+1)=P_n-z^(v_n)Q_n,                            (1)
```

with disjoint old and shifted supports, `d_n=2^n`, and pointwise
`|P_n|^2+|Q_n|^2=2d_n`.  Put `a=z^(v_n)`.  The difference of the two new
fourth powers is

```text
|P_(n+1)|^4-|Q_(n+1)|^4
 =16d_n Re[a Q_n conjugate(P_n)].                  (2)
```

The integral on the right is zero: it is the inner product of `P_n` with the
disjoint translate `aQ_n`.  Therefore the two individual fourth moments are
equal at every stage `n>=1`.  Combining this with K1646's exact sum recurrence
gives, for either `R_n=P_n` or `Q_n`,

```text
int |R_n|^4
 =d_n^2[4/3-(1/3)(-1/2)^n].                       (3)
```

For the cubic stages `n=3r`, K1647's real translation/phase field therefore
has the exact integrated fourth cumulant

```text
D_(M,N)
 =-[1+(1/2)(-1/8)^r] A_N^4 d_N^2.                 (4)
```

The coefficient tends to `-1`; no member selection or `3/2` ceiling is needed.
Equation (4) is still only the negative term in K1637's complete gap.

## K1652 — continuous Gaussian-channel missing information

Work in finite-dimensional real coordinates with reference `mu=N(0,I)` and
positive diagonal weight `Omega`.  Let a latent variable `Z` have any
probability law, let `m_Z` be centered with covariance `Delta`, and condition
on `Z` by

```text
X=m_Z+epsilon,   epsilon~N(0,S_0),
S_*=S_0+Delta,                                      (5)
```

where `S_0`, `S_*`, `Delta`, and `Omega` commute and `S_0>0`.  If `u_Z` is
the component relative score, `u` the output relative score, and `u_*` the
score of the moment-matched Gaussian `N(0,S_*)`, then

```text
u_Z-u_*=S_0^(-1)m_Z+(S_*^(-1)-S_0^(-1))X,
u-u_*=E[u_Z-u_* | X].                              (6)
```

Conditional Pythagoras and a one-line covariance calculation give the exact
identity

```text
R_Omega
 :=E|u-u_*|_Omega^2
 =Tr[Omega Delta S_0^(-1)S_*^(-1)]
  -E Tr[Omega S_0^(-1)Cov(m_Z|X)S_0^(-1)].         (7)
```

The first term is the component Fisher ceiling; the second is exactly the
posterior missing information.  This is the continuous equal-covariance
specialization of K1606's score-variance mechanism.  In K1648's real
sine/cosine convention, including its universal quarter,

```text
R_(Omega,N)/4=C_(F,N)-M_(F,N),   0<=M_(F,N)<=C_(F,N). (8)
```

## K1653 — the translation/phase posterior term is subleading

After multiplying by the known Rudin--Shapiro signs and normalizing each
selected positive-frequency coefficient, the K1648 observation has the form

```text
W_k=a exp(i(Theta+k dot Y))+xi_k,   k in K_N,       (9)
```

where `K_N` is a complete cube of `d_N=Theta(N^3)` lattice modes,
`a^2=Theta(eta)>0`, and the independent circular Gaussian noise variances are
bounded above and below uniformly on the fixed-ratio shell.

Partition fixed positive-density subsets of the cube into disjoint adjacent
mode pairs.  For each coordinate direction `j`, the average of

```text
conjugate(W_k) W_(k+e_j)                            (10)
```

has expectation `a^2 exp(iY_j)` and mean-square fluctuation `O(d_N^-1)`.
A bad-event split around half the nonzero mean therefore gives a phase
estimator with

```text
E|exp(i Yhat_j)-exp(iY_j)|^2=O(d_N^-1).             (11)
```

Use a disjoint residual subcube to estimate `Theta` after demodulation.  Since
`|k|=O(N)`, (11) gives

```text
E|exp(i Thetahat)-exp(iTheta)|^2=O(N^2/d_N)=O(N^-1).
                                                               (12)
```

The plug-in orbit predictor consequently has normalized per-mode mean-square
error `O(N^-1)`.  The posterior mean is the minimum quadratic-risk predictor,
so summing over `Theta(N^3)` modes and multiplying by the largest score weight
`O(N)` gives

```text
M_(F,N)=O_(g,eta)(N^3).                            (13)
```

Combining (8) and (13),

```text
C_(F,N)-O_(g,eta)(N^3)
 <=R_(Omega,N)/4<=C_(F,N).                         (14)
```

Thus K1648's convexity ceiling is its exact leading posterior-score residual.
The result uses the complete cubical coefficient support, known signs,
fixed positive amplitude, and fixed-shell residual-noise bounds.  It is not a
general macroscopic-block coercivity theorem.

## K1654 — sufficiently small fixed amplitude loses at leading order

Let the selected shell satisfy `a_0N<=omega_k<=a_1N` and
`c_0N^3<=d_N<=c_1N^3`.  K1572's profiled factors obey `0<s_(N,k)^*<=1`, and
K1648 sets

```text
delta s_k=eta omega_k/N,
s_(0,k)=s_(N,k)^*-delta s_k>0.                     (15)
```

Hence its exact component ceiling has the uniform lower bound

```text
C_(F,N)
 =(1/2)sum_(k in K_N)
   omega_k delta s_k/[s_(0,k)s_(N,k)^*]
 >=(eta/(2N))sum_(k in K_N)omega_k^2
 >=(a_0^2 c_0/2) eta N^4.                         (16)
```

K1651 and `d_N<=c_1N^3` give

```text
gD_(M,N)>=-(3/2)g c_1^2 eta^2 N^4.                (17)
```

Choose one fixed positive `eta` below both K1648's covariance-positivity
threshold and `a_0^2c_0/(6gc_1^2)`.  Equations (14), (16), and (17) then imply

```text
Q_N[Law(X_N)]-lambda_N^statG >= c_(g,eta)N^4       (18)
```

for all sufficiently large cubic stages, with `c_(g,eta)>0`.  The explicit
small-amplitude macroscopic flat-block family therefore raises the energy at
leading order.  Its negative defect is real, but the asymptotically saturated
component-score payment is linear in `eta` and dominates the quadratic gain.

This does not classify every admissible larger `eta`, another correlated
angular law, or the unrestricted ground-energy coefficient.  It supplies no
bounded-error recentering, compactness, Mosco result, source-owned Hamiltonian,
physical state, observation, prediction, or GU verdict.

## K1655 — protected integration and hostile bookend

The bridge census is now 370 rows: 291 satisfied, ten conditional, 65
excluded, and four missing.  K1651 sharpens the flat-block defect to an exact
coefficient.  K1652--K1653 prove that the K1648 posterior-score residual
saturates its component Fisher ceiling at order `N^4`, with only `O(N^3)`
missing information.  K1654 then proves a positive `Theta(N^4)` gap for every
sufficiently small fixed admissible amplitude.

Hostile review rejects presenting K1606's finite-mixture identity as new,
dropping the complete-cube or fixed-positive-amplitude hypotheses, reversing
the conditional-variance sign, replacing posterior concentration by exact
label recovery, extending the small-amplitude result to all amplitudes, or
promoting this family theorem to unrestricted coercivity.  It also rejects
transfer to a source-owned action, physical state, prediction or GU verdict.

The next quantum wake is a larger-amplitude translation/phase coefficient
test or a genuinely different anisotropic macroscopic family, followed by
unrestricted Fisher/negative-defect coercivity if a structural inequality is
available.  The independent physical wake remains a source-owned
action/measure/Hamiltonian and admissible domain.

## Postflight bookend

The first explicit leading-defect family is now classified in the regime in
which its Gaussian residual is chosen safely small: its posterior label is
learnable from the macroscopic cube, so mixing does not cancel the leading
component Fisher payment, and the full leading gap is positive.  The result
eliminates this small-amplitude orbit as a coefficient-changing witness while
preserving larger-amplitude and different-anisotropy routes.  Protected
source, ledger, canon, paper, prediction, confirmation, and public-posture
states are unchanged.
