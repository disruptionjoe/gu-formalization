---
title: "Common covariance floors and the BV atomic holonomy obstruction"
status: active_research
document_role: exploration
target_claim: INTERNAL_TARGET__COMMON_FLOOR_COVARIANCE_RIGIDITY_AND_BV_ATOMIC_OBSTRUCTION
created: "2026-10-09"
updated_at: "2026-10-09"
---

# Common covariance floors and the BV atomic holonomy obstruction

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
  carrier: common_profile_floor_label_dependent_gaussian_mixtures_plus_compact_bv_spectral_primitives
  pairing_or_form: weighted_relative_fisher_form_gaussian_channel_information_and_fourier_bv_measure_pairing
  real_structure: real_finite_q_space_and_real_finite_dimensional_harmonic_spectral_values
  grading: gaussian_label_and_location_noise_plus_derivative_measure_atomic_continuous_split
  action_owner: repository_control_not_source_owned
  target_object: coefficient_rigidity_and_atomic_holonomy_l1_obstruction
  observed_intertwiner: UNTYPED
```

## Scope and preflight bookend

K1618 appears to stop at one common covariance, but a broad heterogeneous
Gaussian family has exactly that structure after one convolution split. If
every component covariance dominates one common profiled floor, the excess
covariance is an additional random location inside the common Gaussian
channel. This structural representation is stronger than another pairwise
affinity sum: label entropy and within-label Gaussian capacity replace nominal
component count, separation, and shared eigenvectors.

The independent spectral arc removes K1619's finite-jump restriction. For a
general compact BV primitive, the derivative is a finite measure. Wiener's
theorem detects every atomic part of that measure through a positive long-time
Fourier mean square, which is already enough to force logarithmic divergence
after the primitive's inverse-time factor.

SC-ACT-01/02/06 remain assertions and SC-META-53 remains uncertain. The
physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED.
LT-SM8, LT-GR6b, RA-F1 and AC-F1 do not move. No source, ledger, canon,
paper, prediction, confirmation, or public-posture state moves.

## K1621 — heterogeneous covariance as a common-floor location channel

Let `Z_N` be a discrete label with weights `p_(N,z)`. Suppose

```text
S_(N,z)=S_(N,*)+C_(N,z),   C_(N,z)>=0,                         (1)
```

where `S_(N,*)` is stationary diagonal and lies in a fixed relative K1572
profile band. Let `W_N` be standard Gaussian, let
`G_(N,*)~N(0,S_(N,*))` be independent, and set

```text
M_N=m_(N,Z_N)+C_(N,Z_N)^(1/2)W_N,
X_N=M_N+G_(N,*).                                               (2)
```

Conditionally on `Z_N=z`, (2) is exactly `N(m_(N,z),S_(N,z))`.
Thus the original label-dependent covariance mixture is a continuous
location mixture over one common Gaussian covariance. The excess matrices may
have arbitrary and label-dependent eigenvectors; only the common Loewner floor
is shared.

K1616 therefore gives

```text
Q_N(Law(X_N)) >= lambda_N^prof
  -(Lambda_(N,*)/2) I(M_N;X_N),                               (3)
Lambda_(N,*)=||S_(N,*)^(-1/2)Omega_NS_(N,*)^(-1/2)||_op
            =O_g(N).
```

The common profiled floor is load-bearing. No conclusion follows here for a
family with no such floor or for non-Gaussian component shapes.

## K1622 — entropy plus conditional covariance capacity

Since `X_N` depends on `(Z_N,W_N)` only through `M_N`, the channel Markov
structure and the chain rule give

```text
I(M_N;X_N)=I(Z_N,W_N;X_N)
 <= H(p_N)+I(W_N;X_N|Z_N).                                    (4)
```

For
`A_(N,z)=S_(N,*)^(-1/2)C_(N,z)S_(N,*)^(-1/2)>=0`, the conditional
Gaussian channel is exact:

```text
I(W_N;X_N|Z_N=z)=(1/2)log det(I+A_(N,z)).                      (5)
```

Combining (3)--(5),

```text
Q_N(Law(X_N)) >= lambda_N^prof
 -(Lambda_(N,*)/2)[H(p_N)
 +(1/2)sum_z p_(N,z)log det(I+A_(N,z))].                       (6)
```

Hence an `o(N^3)` entropy-plus-conditional-capacity budget preserves
coefficient `h_g^prof`. Component means may be arbitrarily large and separated:
the discrete label charges their transmitted information through `H(p_N)`.

## K1623 — checkable covariance-excess criteria

For every positive semidefinite `A`,

```text
log det(I+A) <= Tr(A),
log det(I+A) <= rank(A) log(1+||A||_op).                       (7)
```

Consequently each of the following, together with `H(p_N)=o(N^3)`, is
sufficient for coefficient rigidity:

1. `sum_z p_z Tr(A_(N,z))=o(N^3)`;
2. `sum_z p_z rank(A_(N,z))log(1+||A_(N,z)||)=o(N^3)`;
3. in cutoff dimension `d_N=Theta(N^3)`,
   `sup_z||A_(N,z)||_op=o(1)`.

Thus bounded covariance excess on weighted effective rank `o(N^3)` is
harmless even when every label rotates the excess eigenspace. Fixed order-one
excess on a positive fraction of all modes can have order-`N^3` capacity and
is not closed by this argument.

## K1624 — every BV derivative atom obstructs holonomy L1

Let `G` be a compactly supported real scalar or finite-dimensional vector BV
primitive and let `mu=DG` be its finite distributional derivative measure.
Distributional integration by parts gives, for nonzero `t`,

```text
|widehat G(t)|=|widehat mu(t)|/|t|.                            (8)
```

Wiener's theorem for finite measures says

```text
lim_(T->infinity) (1/(2T)) int_(-T)^T |widehat mu(t)|^2 dt
  = sum_a |mu({a})|^2.                                        (9)
```

If `mu` has a nonzero atom, the right side is positive. Since
`|widehat mu|<=||mu||_TV`, (9) implies a positive Cesaro mean for
`|widehat mu|`. Writing `F(T)=int_1^T|widehat mu(t)|dt`, one has
`F(T)>=cT` for all sufficiently large `T`, and partial integration yields

```text
int_1^T |widehat mu(t)|/t dt
 =F(T)/T+int_1^T F(t)/t^2 dt >= c log T-O(1).                  (10)
```

Equations (8)--(10) prove `widehat G` is not in `L1`. K1619's finite
endpoint-jump theorem is the finite-atomic special case. Atom-free `DG` is
necessary, not sufficient: singular-continuous or slowly decaying atom-free
measures need separate Fourier control.

## K1625 — protected integration and hostile bookend

The bridge census is now 340 rows: 261 satisfied, ten conditional, 65
excluded, and four missing. K1621--K1623 close the label-dependent Gaussian
covariance subclass admitting one common profiled Loewner floor and an
`o(N^3)` entropy-plus-conditional-capacity budget. K1624 makes absence of
derivative atoms necessary throughout the compact BV primitive class.

Hostile review rejects removal of the common floor, transfer to non-Gaussian
or nonstationary component laws, interpretation of the sufficient capacity
tests as necessary thresholds, and promotion of atom-free derivative measure
to a sufficient Fourier-decay or nonlinear-flow theorem. None is licensed.

The next quantum wake is control at order-`N^3` conditional capacity or a
genuinely non-Gaussian/nonstationary Fisher-defect theorem. The next PDE wake
is a source-owned atom-free primitive representation with sufficient Fourier
decay and integrable curvature/current/radial remainder. The source-owned
action/measure/Hamiltonian tuple remains a separate gate.

## Postflight bookend

The quantum result changes the prior route: part of label-dependent covariance
heterogeneity needs no new score inequality at all; it is already a K1618
continuous-location channel after the exact common-floor split. The remaining
boundary is information-extensive excess or absence of a profiled floor, not
nominal covariance labels or eigenvector rotation.

The spectral result removes finiteness and interval regularity from the jump
obstruction. It does not construct the atom-free measure or any nonlinear GU
dynamics. Source, ledger, canon, paper, prediction, confirmation, and public
posture remain unchanged.
