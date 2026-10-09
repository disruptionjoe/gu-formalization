---
title: "Macroscopic flat-block defect and radial-block rigidity"
status: active_research
document_role: exploration
target_claim: INTERNAL_TARGET__MACROSCOPIC_CORRELATION_DEFECT_AND_RADIAL_CONTROL
created: "2026-10-09"
updated_at: "2026-10-09"
---

# Macroscopic flat-block defect and radial-block rigidity

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
  carrier: stationary_gaussian_smoothed_macroscopic_fourier_translation_orbits
  pairing_or_form: weighted_relative_fisher_form_plus_integrated_wick_square
  real_structure: real_trigonometric_cutoff_coordinates
  grading: macroscopic_fourier_block_and_angular_fourth_tensor
  action_owner: repository_control_not_source_owned
  target_object: leading_negative_defect_with_controlled_fisher_scale
  observed_intertwiner: UNTYPED
```

## Scope and preflight bookend

K1641--K1643 prove that bounded non-Gaussianity in every submacroscopic
independent Fourier block is too small to change the `N^4` coefficient.  The
open endpoint is therefore genuinely collective.  This wave constructs one
explicit macroscopic dependence block whose integrated fourth cumulant is
`-Theta(N^4)`.  It then adds a nondegenerate Gaussian residual, producing a
normalized stationary positive smooth finite-Fisher law with exactly the
K1572 covariance.  The positive score cost is bounded at order `N^4`, so the
problem is reduced from a missing scale to an explicit leading-coefficient
competition.  The bound does not decide the sign of that competition.

The companion control treats one macroscopic block whose standardized law is
orthogonally invariant.  Its negative directional cumulant is suppressed by
the block dimension, even for arbitrary finite radial fourth moment.  Thus
macroscopic dependence alone is not sufficient: the constructed leading
defect uses strong angular anisotropy.

SC-ACT-01/02/06 remain assertions and SC-META-53 remains uncertain.  The
physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED.
K1145/K1150 remain 0/7.  No source, ledger, canon, paper, prediction,
confirmation, or public-posture state moves.

## K1646 — a three-dimensional Rudin--Shapiro flat block

Start with `P_0=Q_0=1`.  At stage `n`, choose a coordinate monomial `z^(v_n)`
whose translate doubles one side of the current rectangular support, cycling
through the three coordinate axes, and set

```text
P_(n+1)=P_n+z^(v_n)Q_n,
Q_(n+1)=P_n-z^(v_n)Q_n.                            (1)
```

The two supports are disjoint, so both new polynomials have `d_n=2^n`
coefficients in `{+1,-1}`.  Pointwise,

```text
|P_n|^2+|Q_n|^2=2d_n.                              (2)
```

The rectangular shift also puts the frequency `2v_n` outside the Fourier
support of `(P_n conjugate(Q_n))^2`.  Therefore, with normalized Haar measure,

```text
T_n=int(|P_n|^4+|Q_n|^4),
T_(n+1)=16d_n^2-2T_n.                              (3)
```

Writing `t_n=T_n/d_n^2`, one gets

```text
t_(n+1)=4-t_n/2,
t_n=8/3-(2/3)(-1/2)^n.                             (4)
```

At least one member `R_n in {P_n,Q_n}` consequently satisfies

```text
int |R_n|^4/d_n^2 <= t_n/2
 =4/3-(1/3)(-1/2)^n <=3/2,       n>=1.             (5)
```

For `n=3r`, the support is the complete cube with side `ell=2^r` and
`d_n=ell^3`.  Multiplication by a monomial moves this cube into any desired
fixed-ratio positive-frequency shell without changing (2)--(5).

## K1647 — stationary macroscopic correlation realizes the leading defect

For each large cutoff `N`, take `ell_N` to be a power of two with
`N/16<=ell_N<=N/8`, use K1646 at `n=3log_2 ell_N`, and translate its frequency
cube into a fixed positive-octant shell inside the cutoff.  Let `d_N=ell_N^3`
and let `R_N` denote the selected polynomial.  For independent uniform
`Y in T^3` and `Theta in [0,2pi)`, define the real field

```text
M_N(x)=sqrt(2) A_N Re[e^(iTheta) R_N(x+Y)],
A_N^2=eta/N.                                       (6)
```

Random translation makes the law stationary and the global phase makes it
centrally symmetric.  At every spatial point,

```text
v_(M,N)=E M_N(x)^2=A_N^2 d_N,
E M_N(x)^4=(3/2)A_N^4 int|R_N|^4.                 (7)
```

Hence its exact integrated fourth cumulant is

```text
D_(M,N)=(3/2)A_N^4[int|R_N|^4-2d_N^2]
        <=-(3/4)A_N^4 d_N^2
        =-Theta(eta^2 N^4).                        (8)
```

This is the first explicit family at K1638's required scale.  In the real
sine/cosine covariance coordinates, each selected frequency pair contributes
the same coordinate variance

```text
delta s_k=omega_k A_N^2=eta omega_k/N.             (9)
```

The macroscopic block is not orthogonally invariant.  Its low `L4/L2` ratio
is a coherent angular property of the entire Fourier cube.

## K1648 — Gaussian smoothing gives finite Fisher and an explicit cost ceiling

Let `s_(N,k)^*` be K1572's exact profiled covariance.  Because the selected
cube stays in a fixed-ratio shell, choose fixed `eta>0` small enough that

```text
delta s_k < s_(N,k)^*                              (10)
```

uniformly for all selected modes and all large `N`.  Let `G_N` be an
independent stationary diagonal Gaussian with covariance

```text
s_(0,k)=s_(N,k)^*-delta s_k  on the selected cube,
s_(0,k)=s_(N,k)^*            off the selected cube,               (11)
```

and put `X_N=M_N+G_N`.  Gaussian convolution makes `Law(X_N)` a normalized
positive smooth finite-Fisher density.  It remains stationary and centrally
symmetric, and its covariance is exactly `S_N^*`.  Thus K1637's Gaussian
displacement is

```text
A_N^(gap)=0,                                       (12)
```

while Gaussian independence preserves the fourth cumulant (8).

Fisher convexity bounds the output score by the average translated-component
score.  Direct one-coordinate Gaussian algebra gives

```text
(1/4)R_(Omega,N)
 <= C_(F,N)
 :=(1/2)sum_(k in K_N)
       omega_k delta s_k/[s_(0,k)s_(N,k)^*].        (13)
```

The factor `1/2` includes both real sine/cosine coordinates and the universal
quarter in K1637.  Fixed-shell bounds and (9)--(11) give

```text
C_(F,N)=O_(g,eta)(N^4).                            (14)
```

Consequently the exact full gap is located by

```text
gD_(M,N)
 <=Q_N[Law(X_N)]-lambda_N^statG
 <=C_(F,N)+gD_(M,N).                               (15)
```

The construction proves the correct negative-defect scale and keeps every
positive price at the same scale.  It does not prove descent: (13) is an
upper ceiling, not the actual posterior-score residual.  The next exact gate
is the leading coefficient of `R_(Omega,N)` for this four-parameter
translation/phase channel, or a sharper coercivity theorem proving that it
dominates (8).

## K1649 — rotation-invariant macroscopic blocks cannot realize the defect

Let `X in R^d` be centered, standardized and orthogonally invariant with
finite fourth moment.  Write `X=RU`, where `U` is uniform on the unit sphere,
`R>=0`, and `E R^2=d`.  For every `u in R^d`,

```text
E<u,X>^4=3 E[R^4]/[d(d+2)] ||u||^4,
kappa_4(<u,X>)
 =3{E[R^4]/[d(d+2)]-1}||u||^4.                    (16)
```

Jensen gives `E R^4>=d^2`, so the negative part satisfies the sharp bound

```text
kappa_4(<u,X>)>=-6||u||^4/(d+2),                  (17)
```

with equality for the fixed-radius sphere.  For one macroscopic Fourier block
with `d_N=Theta(N^3)`, uniformly bounded basis and covariance profile,
`||a_N(x)||^2=O(N^2)`.  Therefore

```text
D_N>=-[6/(d_N+2)]int||a_N(x)||^4 dx=-O(N).         (18)
```

K1637 then gives `Q_N>=lambda_N^statG-O(N)`, and the Gaussian member supplies
the upper bound.  The profiled coefficient is rigid throughout this radial
macroscopic-block class, without any uniform upper bound on the radial fourth
moment beyond finiteness.  This does not control anisotropic macroscopic laws;
K1647 is an explicit such law.

## K1650 — protected integration and hostile bookend

The bridge census is now 365 rows: 286 satisfied, ten conditional, 65
excluded, and four missing.  K1646--K1648 prove that macroscopic Fourier
dependence can realize `D_N=-Theta(N^4)` inside a normalized stationary smooth
finite-Fisher law with exact profiled covariance and `O(N^4)` positive score
ceiling.  This resolves the existence and scale questions but not the sign of
the complete energy gap.  K1649 proves that orthogonal/radial macroscopic
dependence has only `O(N)` possible negative defect, so angular anisotropy is
load-bearing for the construction.

Hostile review rejects treating Rudin--Shapiro flatness as independence,
dropping Gaussian residual positivity, replacing the actual score residual by
its convexity ceiling, inferring descent from a leading negative defect, or
promoting radial rigidity to arbitrary anisotropic macroscopic laws.  It also
rejects transfer to a source-owned action, physical state, prediction or GU
verdict.

The next quantum wake is the exact leading posterior-score residual of the
K1648 translation/phase channel, or a coercivity theorem comparing it with
the explicit defect coefficient.  The independent physical wake remains a
source-owned action/measure/Hamiltonian and domain capable of selecting the
finite-cutoff control.

## Postflight bookend

The first macroscopic endpoint is no longer merely a necessary block size.
A fully explicit angularly coherent stationary law reaches the required
negative `N^4` defect while keeping the positive price finite at `N^4` scale.
The remaining question is a genuine coefficient comparison.  Protected
source, ledger, canon, paper, prediction, confirmation, and public-posture
states are unchanged.
