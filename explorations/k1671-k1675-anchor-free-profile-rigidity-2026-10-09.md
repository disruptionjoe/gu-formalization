---
title: "Anchor-free known-profile orbit rigidity"
status: active_research
document_role: exploration
target_claim: INTERNAL_TARGET__ANCHOR_FREE_KNOWN_PROFILE_ORBIT_RIGIDITY
created: "2026-10-09"
updated_at: "2026-10-09"
---

# Anchor-free known-profile orbit rigidity

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
  carrier: gaussian_smoothed_known_profile_complete_cutoff_translation_phase_orbits
  pairing_or_form: whitened_prediction_loss_plus_weighted_relative_fisher_form_and_integrated_wick_square
  real_structure: real_trigonometric_cutoff_coordinates
  grading: arbitrary_nonnegative_profile_and_four_parameter_orbit
  action_owner: repository_control_not_source_owned
  target_object: anchor_free_posterior_missing_information_and_leading_coefficient
  observed_intertwiner: UNTYPED
```

## Scope and preflight bookend

K1669 leaves one known-profile geometry: an extensive fixed-threshold set that
need not contain adjacent pairs or a macroscopic complete cube.  Classifying
that set combinatorially is unnecessary.  The posterior term asks only for a
good prediction of the latent mean, not a unique recovery of translation and
phase.  A finite net of the complete four-parameter orbit therefore absorbs
checkerboard, sublattice and other aliasing automatically: two aliased
parameters are the same point in prediction loss on the active coefficients.

Retain K1661's complete positive-frequency cutoff `K_N`, with
`d_N=Theta(N^3)`, `|k|<=C_KN`, known phases `|c_(N,k)|=1`, fixed `eta>0`, and
known nonnegative weights.  Retain the K1572 matched covariance and the
uniform residual margin

```text
t_(N,k)=eta rho_(N,k)r_(N,k)<=1-epsilon.            (1)
```

The result is still a fixed four-dimensional known-mean orbit theorem.  It
does not estimate unknown modewise amplitudes or phases, treat latent
dimension growing with `N`, or control non-orbit dependence.

SC-ACT-01/02/06 remain assertions and SC-META-53 remains uncertain.  The
physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED.
K1145/K1150 remain 0/7.  No source, ledger, canon, paper, prediction,
confirmation, or public-posture state moves.

## K1671 — a finite-net oracle predicts the orbit without identifiability

Work first with a deterministic profile satisfying `0<=rho_k<=rho_+`.  In
the real sine/cosine coordinates of K1652, write the selected conditional
channel as

```text
X=m_Z+xi,  Z=(Theta,Y) in T^4,  xi~N(0,S_0),       (2)
```

where the fixed shell and (1) give uniform positive lower and upper bounds on
`S_0`.  The mean coordinates are fixed multiples of
`sqrt(rho_k)c_k exp(i(Theta+k dot Y))`.  Consequently

```text
||m_z-m_z'||_(S_0^-1)^2
 <=C sum_k rho_k[|Delta Theta|^2+N^2|Delta Y|^2]
 <=C[N^3|Delta Theta|^2+N^5|Delta Y|^2].          (3)
```

Take a product net with phase mesh `N^-2` and each translation mesh `N^-3`.
It has at most `C N^11` points, and every orbit mean lies within squared
whitened distance `C/N` of the net.

Let `mhat` be least squares over this finite net.  The elementary Gaussian
finite-model oracle inequality, obtained from the least-squares basic
inequality and a union bound for the centered Gaussian linear forms, gives

```text
E||mhat-m_Z||_(S_0^-1)^2
 <=C[1+log |G_N|+inf_(v in G_N)||v-m_Z||_(S_0^-1)^2]
 =O(log N).                                        (4)
```

The posterior mean minimizes Bayes quadratic prediction risk under the exact
uniform orbit prior, so

```text
E Tr[S_0^-1 Cov(m_Z|X)]=O(log N).                  (5)
```

Neither (4) nor (5) asserts a unique or consistent estimator of `Z`.
Arbitrary stabilizers and aliases are allowed because the loss is on `m_Z`.
No density, adjacency, connectedness or anchor condition is used.

## K1672 — every bounded known profile has subleading missing Fisher

K1652's missing term is the posterior covariance measured by
`Omega S_0^-2`.  On the fixed shell, the largest frequency weight is `O(N)`
and the residual covariance is uniformly nondegenerate.  Hence

```text
M_(F,N)
 =E Tr[Omega S_0^-1 Cov(m_Z|X)S_0^-1]
 <=CN E Tr[S_0^-1 Cov(m_Z|X)]
 =O(N log N).                                      (6)
```

Therefore

```text
R_(Omega,N)/4=C_(F,N)-O(N log N).                 (7)
```

This improves the `O(N^3)` anchor estimator and applies to zero, sparse,
degenerating, checkerboard, arithmetic and arbitrary anchor-free bounded
profiles.  It uses a mathematical finite-net predictor and does not supply a
computationally efficient reconstruction algorithm.  Known coefficients,
fixed latent dimension, fixed shell and the residual margin remain
load-bearing.

## K1673 — coefficient rigidity for every bounded known profile

Put `B_N=sum_k rho_(N,k)^2`.  The K1661 defect floor and K1663 component
Fisher floor, with K1664's small-/large-`g` comparison, hold for nonnegative
weights including zeros and give one fixed `m_g>0` such that

```text
C_(F,N)+gD_(M,N)>=eta^2 m_g N B_N.                (8)
```

K1637, K1672 and `A_N>=0` therefore imply

```text
Q_N[Law(X_N)]-lambda_N^statG
 >=eta^2 m_g N B_N-CN log N
 >=-CN log N.                                      (9)
```

Thus every bounded known nonnegative profile in the declared orbit class is
leading-coefficient rigid:

```text
liminf_(N to infinity)
 [Q_N[Law(X_N)]-lambda_N^statG]/N^4 >=0.           (10)
```

If `B_N/log N -> infinity`, the displayed lower bound is eventually positive;
if `B_N>=bN^3`, it is positive `Theta(N^4)`.  Small profiles need not have a
positive leading gap, but they cannot descend at order `N^4`.  This closes the
K1669 anchor-free survivor without claiming an unrestricted ground-state
coefficient or a theorem for unknown/non-orbit laws.

## K1674 — the residual margin already supplies the profile ceiling

The selected shell has the K1663 lower bound

```text
r_(N,k)>=sqrt(3)/4.                                (11)
```

Combining (1) with nonnegativity gives, mode by mode,

```text
rho_(N,k)<=(1-epsilon)/(eta r_(N,k))
           <=4(1-epsilon)/(eta sqrt(3)).           (12)
```

For fixed `eta` and `epsilon`, this is an `N`-independent profile ceiling.
Accordingly K1671--K1673 do not need a second boundedness assumption beyond
the already-declared uniform residual margin.  This does not cover a margin
that vanishes with `N`, a varying `eta`, an unknown coefficient family, or a
different covariance shell.

## K1675 — protected integration and hostile bookend

The bridge census is now 390 rows: 311 satisfied, ten conditional, 65
excluded, and four missing.  K1671 replaces support geometry by a
prediction-space entropy bound.  K1672 makes posterior missing Fisher only
`O(N log N)` for every bounded known profile, K1673 proves a uniform
`-O(N log N)` full-gap lower bound and leading-coefficient rigidity, and
K1674 derives the needed ceiling from residual admissibility itself.

Hostile review rejects converting prediction risk into unique latent recovery;
dropping known coefficients, fixed four-dimensional orbit, fixed `eta`, fixed
shell or uniform residual margin; transferring the `C N^11` net to a growing
latent dimension without a new entropy calculation; or extending the result
to non-orbit laws, unrestricted Fisher/defect coercivity, source-owned
Hamiltonians or physical states.  It also rejects interpreting (9) as a
positive gap for profiles with `B_N=O(log N)`.

The next quantum wake is an unknown-profile or growing-latent orbit, a
non-orbit macroscopic correlation law, or an unrestricted Fisher/negative-
defect coercivity theorem.  The independent physical wake remains a source-
owned action/measure/Hamiltonian, admissible domain, physical state and
observation tuple.

## Postflight bookend

Anchor-free support geometry is not a loophole in the known-profile orbit
class.  Prediction-space covering quotients all aliases automatically and
leaves only `O(N log N)` posterior missing Fisher, so the K1661/K1663
coercive margin fixes the leading coefficient throughout the admissible
class.  Protected source, ledger, canon, paper, prediction, confirmation, and
public-posture states are unchanged.
