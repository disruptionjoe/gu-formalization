---
title: "K1696--K1700 uniform shape-optimized scalar envelope"
status: active_research
document_role: exploration
claim_verdict: proved_for_named_discrete_seeds_at_small_coupling
target_claim: INTERNAL_TARGET__K1689_SCALAR_CARDINAL_UPPER_ENVELOPE
updated_at: "2026-10-10"
---

# K1696--K1700: uniform rectangular-shape optimization

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
  carrier: centered_axis_aligned_rectangular_cardinal_blocks_in_the_scaled_cutoff
  pairing_or_form: weighted_relative_fisher_form_plus_integrated_wick_square
  real_structure: real_cardinal_coordinates_with_conjugation_symmetric_mode_blocks
  grading: small_coupling_legendre_order_and_rectangular_shape_boundary
  action_owner: repository_trial_functional_not_source_owned
  target_object: fully_shape_optimized_named_seed_scalar_cardinal_envelopes
  observed_intertwiner: UNTYPED
```

## Result and boundary

K1691--K1692 compare the optimized Rademacher and three-point scalar channels
at each fixed K1683 rectangle. The present result closes the missing uniform
shape step. After adjoining degenerate rectangles to the shape space, the two
shape ratios

```text
R_g(C)=ell_g(C)^2/tau_g(C),
S_g(C)=ell_g(C)^3/tau_g(C)^2
```

extend continuously by zero on the degenerate boundary. Their zero-profile
limits `R_0,S_0` are uniform because K1571 gives
`g log(1/kappa_g)->1/(12 pi)`, so the profile correction is smaller than every
power of `g`. In particular the positive maximum

```text
M=max_C R_0(C)
```

is attained only by nondegenerate rectangles. If
`Mset={C:R_0(C)=M}` and `S_*=min_(C in Mset)S_0(C)`, then `S_*>0`.

For either named seed `X`, with K1687 coefficient `c_X`, the completely
shape- and strength-optimized correction satisfies

```text
H_X(g)
 =-6g^2 M+432c_Xg^3S_*+o(g^3).                       (1)
```

Consequently

```text
H_R(g)-H_*(g)=(576/5)S_*g^3+o(g^3)>0                 (2)
```

for all sufficiently small positive `g`. Thus the K1688 three-point seed
strictly lowers the fully rectangular-shape-optimized Rademacher cardinal
envelope, not merely every fixed-shape branch.

The result is still trial-side. It does not solve the finite-strength scalar
infimum over all bounded symmetric seeds, quantify the translation-Haar saving,
cover moving nonrectangular packets or correlated cumulant tensors, prove an
unrestricted lower bound, identify the true coefficient, or construct a
continuum physical state.

## Preflight bookend and route choice

The substantial frontier contained uniform scalar asymptotics, shape-boundary
compactness, the dependent optimized-envelope comparison, finite-strength seed
classification, quantitative Haar saving, correlated tensors and an
unrestricted lower bound. The cheapest route-changing discriminator was the
exact factorization through a seed-only Legendre profile: it shows that all
shape dependence enters through `tau_g` and `ell_g`, so a direct compactness
argument can settle the moving-rectangle issue without solving the maximizing
shape.

The probability lens checked the discrete-channel endpoint coercivity; the
analysis lens checked the singular `kappa_g->0` profile and degenerate boxes;
the additive-combinatorics lens supplied the rectangle-energy scaling; the
variational lens supplied the second-order minimization lemma; and the hostile
lens retained the named-seed, rectangular and small-coupling ceilings. A
finite-strength numerical search was rejected because it would not classify
all seeds. Quantitative Haar saving and correlated tensors require new
inequalities or constructions rather than another use of the same expansion.
No source or physics-ledger row moves.

## K1696: uniform scalar Legendre profile

For a named seed let `u=-kappa_4(X)>0`, put `q=ut^2`, and define

```text
Phi_X(r)=min_(0<=q<u)[j_X(q)-rq].
```

K1691's positivity and noiseless-endpoint divergence are seed-only. Hence one
number `r_0(X)>0` works independently of shape: for `0<=r<=r_0`, the unique
global minimizer is the implicit branch `j_X'(q)=r`. K1687 gives uniformly

```text
Phi_X(r)=-(3/2)r^2+27c_Xr^3+O_X(r^(7/2)).             (3)
```

For every K1683 rectangle,

```text
F_X(C,g)
 =tau_g(C)/4 * Phi_X(4g ell_g(C)/tau_g(C)).           (4)
```

The ratio `ell_g/tau_g` is uniformly bounded on the compactified rectangle
space. Thus the argument of `Phi_X` is `O(g)` uniformly and (3)--(4) give

```text
F_X(C,g)
 =-6g^2R_g(C)+432c_Xg^3S_g(C)+O_X(g^(7/2))           (5)
```

uniformly over every admissible rectangle, including sequences moving with
`g`. This is the uniformity K1691 did not claim.

## K1697: rectangle compactness and nondegeneration

Write the scaled cutoff as `Q=[-1,1]^3` and parameterize centered rectangles by
`C_alpha=prod_i[-alpha_i,alpha_i]`, `0<alpha_i<=1`. Adjoin the faces with one
or more `alpha_i=0`.

At `kappa=0`,

```text
b_0(x)=|x|,             a_0(x)=(2|x|)^(-1/2).
```

The singularity is locally integrable, including the fourth factor
`a_0(x+y-z)` in the additive-energy integral. Rescaling the rectangle and
splitting a small ball about the joint singular set show that
`ell_0/tau_0`, `R_0` and `S_0` extend continuously to the compactified shape
space, with `R_0=S_0=0` on every degenerate face. The same split is uniform
for `kappa>=0`; dominated convergence and K1571's beyond-all-orders
`kappa_g` scale yield

```text
||R_g-R_0||_infinity+||S_g-S_0||_infinity=o(g^m)     (6)
```

for every fixed `m>0` needed below.

Every nondegenerate rectangle has positive `R_0`, so `M=max R_0>0`; boundary
rectangles have value zero. Therefore the maximizer set `Mset` is compact and
lies in the interior. Equation (5), compared with one fixed positive rectangle,
then forces every exact or `o(g^2)`-near minimizer of `F_X` into one common
compact interior neighborhood of `Mset`. Moving optimizing rectangles cannot
collapse a side length or escape the cutoff.

## K1698: second-order optimization over shapes

Use the elementary compact variational lemma: if

```text
f_g(C)=-6g^2R_0(C)+g^3B(C)+o(g^3)
```

uniformly on a compact space, then

```text
inf_C f_g(C)=-6g^2M+g^3 min_(C in Mset)B(C)+o(g^3).  (7)
```

Indeed, any minimizing sequence outside every neighborhood of `Mset` pays a
fixed order-`g^2` loss. Inside shrinking neighborhoods, compactness and
continuity reduce the order-`g^3` choice to the minimum of `B` on `Mset`.

Equations (5)--(6) apply (7) with `B=432c_XS_0`. Both named seeds have
`c_X>0`, so they select the same secondary quantity
`S_*=min_(Mset)S_0`. The interior location of `Mset` makes `S_*>0`, proving
(1). No uniqueness of the best rectangle is required.

## K1699: strict fully optimized seed gap

For the K1688 three-point seed `c_*=1/4`; for Rademacher `c_R=31/60`.
Subtracting their two instances of (1) gives

```text
432(c_R-c_*)S_*g^3+o(g^3)
 =432(4/15)S_*g^3+o(g^3)
 =(576/5)S_*g^3+o(g^3).
```

Because `S_*>0`, the difference is positive for sufficiently small `g`.
Writing

```text
h_g^(X-card-up)=h_g^prof+H_X(g),
```

the conclusion is

```text
h_g^(*-card-up)<h_g^(R-card-up)=h_g^card-up<h_g^prof
```

at small positive coupling. This compares exactly the two named seed families
after optimizing both channel strength and every K1683 rectangular shape. It
does not identify the full `h_g^scalar-card-up` over all seeds.

## K1700: protected integration and next frontier

The bridge census becomes 415 rows: 336 satisfied, ten conditional, 65
excluded and four missing. SC-ACT-01/02/06 remain `ASSERTS`; SC-META-53 remains
`UNCERTAIN`; the standing ledger remains 33 SAME / 22 DIFFERS / 31 NEEDS / 2
OVER-DETERMINED; and K1145/K1150 remain 0/7. No source, ledger, canon, paper,
prediction, confirmation or public verdict moves.

The strongest next coefficient questions are the exact finite-strength scalar
infimum, a quantitative asymptotic lower scale for translation-Haar Fisher
saving, one correlated fourth-cumulant tensor or nonrectangular moving packet,
and an unrestricted lower bound against the widened trial functional.
Compactness, Mosco convergence and `E_N+O(1)` recentering still wait for the
true coefficient and shift. The source-owned action/domain/state/observation
tuple remains separate.

## Postflight hostile review

- **Strongest overclaim:** (2) compares two named scalar seeds over K1683
  rectangles only; it does not solve the all-seed or unrestricted problem.
- **Strongest contrary route:** a nonrectangular moving packet or correlated
  fourth-cumulant tensor may lie below both optimized scalar-product families.
- **Weakest analytic seam:** the compactification uses the locally integrable
  zero-profile kernel and K1571's beyond-all-orders `kappa_g` scale. Without
  that profile rate, the displayed cubic coefficient need not be stable.
- **Weakest physical seam:** these are covariance-matched trial laws. They do
  not supply a source-owned Hamiltonian, positive physical quotient, observed
  state or prediction.

The exact factorization, compactness argument and variational lemma—not the
deterministic controls—carry K1696--K1699.
