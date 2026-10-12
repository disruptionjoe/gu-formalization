---
title: "K1701--K1705 universal weak-channel cubic envelope"
status: active_research
document_role: exploration
claim_verdict: proved_for_uniformly_controlled_bounded_symmetric_seeds_at_small_coupling
target_claim: INTERNAL_TARGET__K1689_SCALAR_CARDINAL_UPPER_ENVELOPE
updated_at: "2026-10-12"
---

# K1701--K1705: universal controlled cubic scalar envelope

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```yaml
gu-typed-objects:
  carrier: uniformly_bounded_symmetric_scalar_seeds_on_real_cardinal_packet_coordinates
  pairing_or_form: relative_fisher_form_plus_matched_negative_fourth_cumulant_defect
  real_structure: real_scalar_gaussian_interpolation_and_conjugation_symmetric_mode_blocks
  grading: weak_channel_order_then_rectangular_shape_variational_order
  action_owner: repository_trial_functional_not_source_owned
  target_object: controlled_all_seed_fully_rectangular_shape_optimized_cubic_upper_envelope
  observed_intertwiner: UNTYPED
```

## Result and boundary

K1687 already contains a nonnegative square that was not yet promoted to an
all-seed coefficient theorem. For every fixed bounded symmetric centered
unit-variance seed with `kappa_4(X)=-u<0`, put `q=ut^2`. Then

```text
j_X(q)=q^2/6+c_Xq^3+O_X(q^(7/2)),
c_X=1/4+kappa_6(X)^2/(120u^3)>=1/4.                 (1)
```

Equality holds exactly when `kappa_6(X)=0`. Inside the symmetric three-point
family, the unique equality law with negative fourth cumulant is precisely the
K1688 seed

```text
p_*=(15+sqrt(105))/60,
P(X_*=0)=1-p_*,
P(X_*=+-p_*^(-1/2))=p_*/2.                          (2)
```

The fixed-seed statement alone does not control a seed changing with coupling.
For the compact family `S(B,u_0,u_1)` of such laws with `|X|<=B` and
`u in [u_0,u_1]`, `0<u_0<=u_1<=2`, the Hermite remainder and its derivative
are uniform. A score/Hermite identity gives a global coercive bound away from
the Gaussian endpoint, so the global Legendre branch is also uniform. Hence

```text
Phi_X(r)>=-(3/2)r^2+(27/4)r^3-O_(B,u_0)(r^(7/2)).   (3)
```

If the family contains (2), composing (3) with K1696--K1698 yields the sharp
controlled all-seed rectangular envelope

```text
H_S(g)=-6g^2M+108g^3S_*+o(g^3).                    (4)
```

Thus the K1688 seed is cubic-optimal in this controlled scalar-product class,
including coupling-dependent choices inside the class and moving K1683
rectangles. Equation (4) is not the exact finite-strength scalar infimum. It
does not cover support growing with `g^-1`, fourth defect tending to zero,
nonrectangular moving packets, correlated cumulant tensors, translation-Haar
savings, arbitrary stationary laws, or a lower bound for the unrestricted
energy.

## Preflight bookend and route choice

The substantial frontier contained the universal weak-channel coefficient,
three-point equality classification, uniform moving-seed control, dependent
shape optimization, exact finite-strength MMSE optimization, quantitative
Haar saving and correlated/unrestricted alternatives. The coefficient route
won because K1687 already expresses the first seed-dependent penalty as a
square, so one exact argument settles an infinite controlled class before any
finite-strength search.

The probability lens isolated the matched-defect coefficient. The
real-algebraic lens classified the three-point roots. The analysis lens made
support and defect compactness explicit instead of interchanging an infimum
with a pointwise expansion. The information-theory lens supplied an exact
score moment that keeps the global minimizer near the weak endpoint. The
variational lens composed the uniform statement with K1697's nondegenerate
shape compactness. The hostile lens preserved every nonuniform, finite-
strength, correlated, Haar, unrestricted and physical boundary. No source or
physics-ledger row moves.

## K1701: universal fixed-seed cubic floor

K1687 gives, for one fixed bounded symmetric seed,

```text
j_X(t)
 =(kappa_4^2/6)t^4
  +(kappa_6^2/120-kappa_4^3/4)t^6
  +O_X(t^7).
```

Write `kappa_4=-u`, `u>0`, and `q=ut^2`. The quartic term becomes `q^2/6`.
The sixth-order term becomes

```text
[kappa_6^2/(120u^3)+1/4]q^3.
```

This proves (1). The floor is sharp and equality is equivalent to
`kappa_6=0`; no moment or variational inequality beyond the already-proved
Hermite expansion is being assumed. The `O_X` constant remains seed-
dependent at this stage.

## K1702: equality inside the symmetric three-point family

For

```text
P(X=0)=1-p,
P(X=+-p^(-1/2))=p/2,
```

the even moments are `m_2=1`, `m_4=1/p`, `m_6=1/p^2`, so

```text
kappa_4=1/p-3,
kappa_6=1/p^2-15/p+30.
```

Negative fourth cumulant requires `p>1/3`. With `y=1/p`, cancellation of the
sixth cumulant gives

```text
y^2-15y+30=0,
y=(15+-sqrt(105))/2.
```

Equivalently the two probability roots are

```text
p=(15-sqrt(105))/60,
p=(15+sqrt(105))/60.
```

Only the second exceeds `1/3`. It is (2), with
`u_*=(sqrt(105)-9)/2`. This proves uniqueness only in the symmetric
three-point negative-kurtosis family. Other bounded symmetric distributions
may also have zero sixth cumulant.

## K1703: uniform moving-seed Legendre floor

Fix `B<infinity` and `0<u_0<=u_1<=2`. Let `S(B,u_0,u_1)` be the symmetric
centered unit-variance laws supported in `[-B,B]` with
`u=-kappa_4 in [u_0,u_1]`. Uniform support bounds every moment entering the
Hermite expansion; division by `u` is harmless because `u>=u_0`. Thus (1)
and its first `q` derivative have uniform remainders on this family.

It remains to prevent a distant value of `q` from beating the perturbative
branch. If `Y_t=sqrt(t)X+sqrt(1-t)Z`, write its relative score as
`v(Y_t)=rho_Y(Y_t)+Y_t`. Gaussian integration by parts gives

```text
E[v(Y_t)H_3(Y_t)]
 =E[Y_tH_3(Y_t)-H_3'(Y_t)]
 =E H_4(Y_t)
 =kappa_4(Y_t)
 =-q.                                                (5)
```

Cauchy--Schwarz therefore yields

```text
j_X(q)=E v(Y_t)^2 >= q^2/E H_3(Y_t)^2.              (6)
```

The denominator is uniformly bounded by a finite `C_B`, since the sixth
moment of `sqrt(t)X+sqrt(1-t)Z` is uniformly bounded by `B` and Gaussian
moments. Hence `j_X(q)>=q^2/C_B`. For `q` outside one fixed small
neighborhood of zero, this beats the linear reward `rq` when `r` is small.
Every global minimizer is therefore on the uniform implicit branch
`j_X'(q)=r`.

Solving that branch and substituting back gives

```text
Phi_X(r)
 =min_(0<=q<u)[j_X(q)-rq]
 =-(3/2)r^2+27c_Xr^3+O_(B,u_0)(r^(7/2)).            (7)
```

Equations (1) and (7) prove (3). This closes coupling-dependent escape only
inside the declared compact family.

## K1704: sharp controlled all-seed rectangular envelope

Assume `B>=p_*^(-1/2)` and `0<u_0<=u_*<=u_1`, so (2) belongs to the family.
Define

```text
H_S(g)
 =inf_(X in S(B,u_0,u_1)) inf_C
   [tau_g(C)/4]Phi_X(4g ell_g(C)/tau_g(C)).          (8)
```

K1696 bounds `ell_g/tau_g` uniformly over the compactified rectangle space,
so (3) applies uniformly in both seed and shape. K1697 replaces the moving
shape functions by their zero-profile limits through cubic order and excludes
degenerate rectangles. K1698's compact variational lemma then gives

```text
H_S(g)>=-6g^2M+108g^3S_*+o(g^3).                   (9)
```

Choosing (2) gives the matching upper bound, proving (4). Since the
Rademacher coefficient is `432(31/60)=1116/5`, its envelope remains above
(4) by

```text
(1116/5-108)S_*g^3+o(g^3)
 =(576/5)S_*g^3+o(g^3).
```

The new content is the lower comparison within the controlled scalar seed
class; it is not a lower bound over arbitrary field laws.

## K1705: protected integration and next frontier

The bridge census becomes 420 rows: 341 satisfied, ten conditional, 65
excluded and four missing. SC-ACT-01/02/06 remain `ASSERTS`; SC-META-53
remains `UNCERTAIN`; the standing physics ledger remains 33 SAME / 22 DIFFERS
/ 31 NEEDS / 2 OVER-DETERMINED; and K1145/K1150 remain 0/7. No source,
ledger, canon, paper, prediction, confirmation or public verdict moves.

The strongest next coefficient questions are the exact finite-strength scalar
infimum, coupling-dependent seeds outside every fixed `S(B,u_0,u_1)`, a
quantitative translation-Haar saving, a correlated fourth-cumulant tensor or
nonrectangular moving packet, and an arbitrary-stationary lower bound. The
source-owned action/domain/state/observation tuple remains separate.

## Postflight hostile review

- **Strongest overclaim:** the word “all-seed” is restricted to one fixed
  controlled family `S(B,u_0,u_1)`; no uniformity is proved as `B` diverges or
  `u_0` vanishes with coupling.
- **Strongest contrary route:** a coupling-dependent rare-amplitude seed, a
  nonproduct fourth-cumulant tensor, or translation-Haar score cancellation
  can leave the proved scalar cubic class.
- **Weakest analytic seam:** the global branch uses both the uniform Hermite
  remainder and the score/Hermite coercive bound (5)--(6). Pointwise expansion
  alone would not justify the infimum over moving seeds.
- **Weakest physical seam:** the envelope concerns covariance-matched trial
  laws. It supplies no source-owned Hamiltonian, positive physical quotient,
  observed state, prediction or confirmation.

The Hermite coefficient identity, moment-root classification, score moment
coercivity and compact variational composition—not the executable controls—
carry K1701--K1704.
