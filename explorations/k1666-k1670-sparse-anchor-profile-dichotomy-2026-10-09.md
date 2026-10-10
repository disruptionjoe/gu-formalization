---
title: "Sparse/anchor profile dichotomy"
status: active_research
document_role: exploration
target_claim: INTERNAL_TARGET__SPARSE_ANCHOR_PROFILE_DICHOTOMY
created: "2026-10-09"
updated_at: "2026-10-09"
---

# Sparse/anchor profile dichotomy

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
  grading: sparse_or_anchored_positive_frequency_profile_and_four_parameter_orbit
  action_owner: repository_control_not_source_owned
  target_object: vanishing_floor_profile_leading_descent_and_observability
  observed_intertwiner: UNTYPED
```

## Scope and preflight bookend

K1661--K1664 prove a positive leading gap when every complete-cube profile
entry stays between two fixed positive constants.  This wave removes the
global positive floor in two different directions.  First, it proves that a
profile with subextensive squared-amplitude mass cannot lower the leading
coefficient, without estimating the latent orbit at all.  Second, it proves
that one macroscopic cubical anchor is enough to estimate the four orbit
parameters and recover a positive leading gap even when the profile vanishes
or degenerates away from the anchor.

Retain K1661's complete positive-frequency cube `K_N`, with
`d_N=Theta(N^3)`, `d_N/N^3<=1/512`, known phases `|c_(N,k)|=1`, fixed
`eta>0`, and known nonnegative weights

```text
0<=rho_(N,k)<=rho_+<infinity.                       (1)
```

Define `R_N` and the translation/global-phase orbit field exactly as in
K1661, allowing zero coefficients.  Retain the K1572 matched covariance and
the uniform residual margin

```text
t_(N,k)=eta rho_(N,k)r_(N,k)<=1-epsilon.            (2)
```

The conclusions remain fixed-four-parameter, known-profile, complete-envelope
results.  They do not estimate an unknown modewise profile, treat a latent
dimension growing with `N`, or control non-orbit correlations.

SC-ACT-01/02/06 remain assertions and SC-META-53 remains uncertain.  The
physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED.
K1145/K1150 remain 0/7.  No source, ledger, canon, paper, prediction,
confirmation, or public-posture state moves.

## K1666 — subextensive squared-amplitude mass cannot lower the coefficient

Put

```text
B_N=sum_(k in K_N) rho_(N,k)^2,
L_N=sum_(k in K_N) rho_(N,k).                       (3)
```

K1661 and Cauchy remain valid for nonnegative weights, including zeros:

```text
D_(M,N)>=-(3eta^2/N^2)L_N^2
         >=-(3eta^2d_N/N^2)B_N.                    (4)
```

K1637 gives the exact full gap

```text
Q_N[Law(X_N)]-lambda_N^statG
 =A_N+R_(Omega,N)/4+gD_(M,N),                       (5)
```

with `A_N>=0` and `R_(Omega,N)>=0`.  Therefore

```text
Q_N[Law(X_N)]-lambda_N^statG
 >=-3g eta^2(d_N/N^2)B_N.                          (6)
```

If `B_N=o(N^3)`, the right side is `-o(N^4)`.  Such a profile cannot create a
strict negative order-`N^4` descent and cannot lower the stationary-Gaussian
leading coefficient.  No posterior localization is required.

This is a one-sided coefficient-lowering theorem.  It does not say the full
gap is `o(N^4)`: a coherent trigonometric profile can have a large positive
fourth moment.  It also does not supply a positive `Theta(N^4)` gap.

## K1667 — one macroscopic anchor cube localizes the orbit

Assume there is a complete lattice subcube `Q_N subset K_N` with side lengths
bounded below by `alpha N`, hence `q_N=|Q_N|=Theta(N^3)`, such that

```text
rho_(N,k)>=rho_->0,   k in Q_N.                    (7)
```

No positive lower bound is imposed on `K_N\Q_N`.  On `Q_N`, multiply the
selected complex observation by `conjugate(c_(N,k))` and divide by
`sqrt(rho_(N,k))`.  Equations (1), (2), and (7) give K1653's constant-signal
channel with independent circular noise variances bounded above and below.

Use disjoint adjacent pairs inside the anchor cube.  The three translation
risks are `O(q_N^-1)=O(N^-3)`.  A disjoint anchor subcube then gives global
phase risk `O(N^2/q_N)=O(N^-1)`.  Predicting the full orbit costs only the
global upper bound `rho_+`: zero coefficients need no prediction, and every
nonzero selected mode has `|k|=O(N)`.  The normalized per-mode prediction
risk is `O(N^-1)` across `d_N=Theta(N^3)` modes.

Posterior means minimize the original score-weighted risk.  The residual
margin keeps every score weight `O(N)`, so

```text
M_(F,N)=O_(g,eta,rho_-,rho_+,alpha,epsilon)(N^3),
R_(Omega,N)/4=C_(F,N)-O(N^3).                      (8)
```

The anchor is an observability hypothesis, not a conclusion about every
positive-density support.  A checkerboard, arithmetic, fractal, or otherwise
anchor-free threshold set is not silently replaced by a cube.

## K1668 — anchored degenerating profiles have a positive leading gap

K1663's pointwise inequality includes `t=0` by continuity, so with nonnegative
weights

```text
C_(F,N)>=2eta^2N sum_k rho_(N,k)^2r_(N,k)^3.       (9)
```

Combining (4), (9), and the K1664 small-/large-`g` cube margin gives

```text
C_(F,N)+gD_(M,N)>=eta^2 N B_N m_g,   m_g>0.        (10)
```

The anchor supplies `B_N>=rho_-^2q_N=Theta(N^3)`.  K1667 subtracts only
`O(N^3)`, hence

```text
Q_N[Law(X_N)]-lambda_N^statG
 >=c_(g,eta,rho_-,alpha,epsilon)N^4                (11)
```

for all sufficiently large `N`.  Thus the global lower profile bound in K1664
was stronger than necessary: a fixed macroscopic observable anchor suffices,
even if the remaining amplitudes vanish or tend to zero arbitrarily.

## K1669 — exact geometry of the surviving bounded-profile sector

Under the fixed ceiling `rho_+`, a possible negative order-`N^4` descent must
have `B_N=Omega(N^3)` by K1666.  It therefore cannot have support cardinality
`o(N^3)`, since

```text
B_N<=rho_+^2 |{k:rho_(N,k)>0}|.                    (12)
```

More sharply, on any subsequence with `B_N>=bN^3`, use
`d_N<=c_1N^3` and choose `tau^2=b/(2c_1)`.  Then

```text
B_N<=tau^2d_N+rho_+^2|{k:rho_(N,k)>=tau}|,
|{k:rho_(N,k)>=tau}|>=bN^3/(2rho_+^2).             (13)
```

So every surviving bounded profile has a fixed-threshold set of positive
three-dimensional density.  K1668 removes those threshold sets containing a
macroscopic complete cube.  The remaining known-profile orbit question is
therefore not ordinary sparsity: it is extensive but anchor-free support
geometry, where aliasing or missing adjacent-pair structure may obstruct the
current posterior estimator.  Unknown profiles, growing latent dimension and
non-orbit laws remain separate.

Equation (13) is a necessary survivor classification, not an existence claim,
localization theorem, or coefficient-changing construction.

## K1670 — protected integration and hostile bookend

The bridge census is now 385 rows: 306 satisfied, ten conditional, 65
excluded, and four missing.  K1666 excludes every bounded profile with
subextensive squared-amplitude mass from leading descent.  K1667--K1668 close
profiles possessing one macroscopic positive anchor cube even when they
degenerate elsewhere.  K1669 proves that any remaining bounded candidate must
have an extensive fixed-threshold support while avoiding every such anchor.

Hostile review rejects turning the one-sided K1666 lower bound into a
two-sided `o(N^4)` estimate; dropping known phases or amplitudes, the fixed
four-dimensional orbit, the residual margin, the bounded profile ceiling, or
the complete anchor geometry; inferring that arbitrary positive-density
support contains a macroscopic cube; or extending the result to unknown
profiles, growing latent dimension, non-orbit laws or unrestricted
coercivity.  It also rejects transfer to source-owned or physical sectors.

The next quantum wake is a localization/coercivity theorem or explicit
counterexample for extensive anchor-free known profiles, followed by unknown
profiles, growing latent dimension, non-orbit correlations or unrestricted
Fisher/negative-defect coercivity.  The independent physical wake remains a
source-owned action/measure/Hamiltonian, admissible domain, physical state and
observation tuple.

## Postflight bookend

Vanishing individual amplitudes are not themselves a leading-coefficient
loophole.  Too little total squared-amplitude mass is asymptotically unable to
descend, while one macroscopic observable anchor restores the full positive
gap.  The only bounded known-profile orbit sector left by these arguments is
extensive yet anchor-free.  Protected source, ledger, canon, paper,
prediction, confirmation, and public-posture states are unchanged.
