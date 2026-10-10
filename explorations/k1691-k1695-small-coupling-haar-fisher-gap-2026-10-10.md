---
title: "K1691--K1695 fixed-shape small-coupling and Haar Fisher gap"
status: active_research
document_role: exploration
claim_verdict: proved_for_fixed_shapes_and_finite_cutoff_translation_averages
target_claim: INTERNAL_TARGET__K1689_SCALAR_CARDINAL_UPPER_ENVELOPE
updated_at: "2026-10-10"
---

# K1691--K1695: optimized small-coupling and exact Haar Fisher saving

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
  carrier: fixed_rectangular_cardinal_block_with_scalar_gaussian_channels
  pairing_or_form: weighted_relative_fisher_form_plus_integrated_wick_square
  real_structure: real_cardinal_coordinates_and_orthogonal_translation_action
  grading: matched_fourth_cumulant_defect_and_small_coupling_order
  action_owner: repository_trial_functional_not_source_owned
  target_object: fixed_shape_optimized_upper_branch_and_haar_fisher_deficit
  observed_intertwiner: UNTYPED
```

## Result and boundary

For every fixed K1683 packet shape `C`, the Rademacher and K1688 three-point
channels each have a unique global minimizing matched-defect branch for all
sufficiently small positive coupling `g`. Their optimized fixed-shape gaps
agree through order `g^2`, but the three-point branch is smaller by

```text
(576/5) g^3 ell_g(C)^3/tau_g(C)^2+O_C(g^(7/2)).
```

This converts K1688's pointwise matched-defect ordering into a global
small-coupling statement for each fixed shape. It does not make the expansion
uniform over moving shapes, prove strict inequality after optimizing over all
`C`, or identify the exact finite-strength scalar optimizer.

Independently, compact translation-Haar averaging has an exact Fisher deficit:
the pre-average Fisher information minus the averaged Fisher information is
the posterior variance of the translated component score. Equality holds
exactly when the density is translation invariant. A non-Gaussian independent
cardinal product with nonzero fourth cumulant is not invariant under a genuine
coordinate-mixing translation, so its finite-cutoff saving is strict. No
order-`N^4` lower bound on that saving is proved.

Scope: fixed K1683 rectangular shapes, the named Rademacher and three-point
discrete scalar seeds near `g=0`, and finite-dimensional cutoff laws under the
orthogonal translation representation. These are repository-derived trial
results, not a source-owned action, physical state, observable or prediction.

## Preflight bookend and route choice

K1686--K1690 leave four coefficient-facing routes: finite-strength scalar
optimization, moving shapes or correlated cumulants, exact Haar saving, and an
unrestricted lower bound. Retrieval found K1606's exact finite-mixture score
variance and K1636's translation-Haar Jensen reduction, but no continuous-Haar
identity or strictness theorem for the K1677 cardinal product. It found K1687's
matched-defect expansion but no optimization of its fixed-shape objective.

The cheapest structural route is therefore twofold. First, discrete-channel
coercivity and the implicit function theorem turn the local expansion into a
global small-coupling optimizer before any finite-`t` numerical search.
Second, conditional variance upgrades Haar convexity to an identity, while a
fourth-cumulant mixing witness decides strictness without a high-dimensional
Fisher calculation. Exact finite-strength seed classification, correlated
tensors and a matching lower bound remain outside this footprint.

The probability/information-geometry lens supplies the score identity; the
asymptotic/variational lens supplies global small-coupling minimization; the
harmonic-analysis lens supplies the compact group action; the cumulant lens
supplies noninvariance; and the hostile lens enforces the fixed-shape,
finite-cutoff claim ceiling. No source or physics ledger row moves.

## K1691: the global fixed-shape small-coupling branch

Fix a K1683 shape `C`, abbreviate

```text
A=tau_g(C)/4>0,       B=g ell_g(C)>0,       r=B/A,
```

and take a bounded symmetric seed with `kappa_4=-u<0`. In the matched-defect
coordinate `q=u t^2`, K1687 gives

```text
j_X(q)=q^2/6+c_Xq^3+O_X(q^(7/2)),
c_X=1/4+kappa_6(X)^2/(120u^3).                         (1)
```

The fixed-shape scalar gap is

```text
F_(X,C,g)(q)=A j_X(q)-Bq=A[j_X(q)-rq],       0<=q<u.   (2)
```

For either named discrete seed, `j_X(q)>0` for `q>0`: equality would make the
Gaussian-smoothed output Gaussian and hence, by Cramer's theorem, make the
seed Gaussian. Moreover `j_X(q)->infinity` as `q` approaches `u`, because the
discrete-channel MMSE decays exponentially while K1686 gives
`j=gamma[1-(1+gamma)mmse]` and `gamma->infinity`. Thus every global minimizer
of (2) tends to zero as `g->0`.

Near zero, `j_X''(0)=1/3>0`, so the implicit function theorem gives the unique
critical branch `j_X'(q_X)=r`; the preceding coercivity makes it the unique
global minimizer for sufficiently small `g`. Substitution into (1) gives

```text
q_X(r)=3r-81c_Xr^2+O_X(r^(5/2)),                       (3)

min_q F_(X,C,g)
 =A[-(3/2)r^2+27c_Xr^3+O_X(r^(7/2))]
 =-6g^2 ell_g(C)^2/tau_g(C)
  +432c_Xg^3 ell_g(C)^3/tau_g(C)^2+O_C,X(g^(7/2)).    (4)
```

The word global in K1691 binds the one-dimensional fixed-shape objective for
one of the two named seeds and sufficiently small `g`; it does not bind the
infimum over shapes or all scalar laws.

## K1692: optimized three-point dominance at fixed shape

For the K1688 three-point seed, `kappa_6=0`, hence `c_*=1/4`. For symmetric
Rademacher, `c_R=31/60`. Formula (4) yields

```text
min F_(R,C,g)
 =-6g^2 ell^2/tau +(1116/5)g^3 ell^3/tau^2+O_C(g^(7/2)),

min F_(*,C,g)
 =-6g^2 ell^2/tau +108g^3 ell^3/tau^2+O_C(g^(7/2)).
```

Therefore

```text
min F_(R,C,g)-min F_(*,C,g)
 =(576/5)g^3 ell_g(C)^3/tau_g(C)^2+O_C(g^(7/2))>0     (5)
```

for every fixed admissible `C` and all sufficiently small positive `g`.
This is the first strict comparison after optimizing the channel strength,
but only shape by shape. If the optimizing shapes move with `g`, the remainder
and the ratio `ell^3/tau^2` need uniform control before (5) can compare the two
fully shape-optimized envelopes.

## K1693: exact compact-mixture Fisher deficit

Let a compact group `G` act orthogonally on a finite-dimensional cutoff space,
preserving the Gaussian reference `mu` and commuting with `Omega>0`. For a
positive normalized finite-Fisher density `rho`, write

```text
rho_a(q)=rho(U_a^(-1)q),        u_a=grad log rho_a,
bar rho(q)=int_G rho_a(q) da.
```

At every point with `bar rho>0`, the posterior law of the latent group element
is

```text
w_q(da)=rho_a(q)da/bar rho(q),
```

and differentiation under the compact integral gives

```text
bar u(q)=grad log bar rho(q)=int_G u_a(q)w_q(da).      (6)
```

The conditional-variance identity then gives the exact deficit

```text
I_Omega(rho|mu)-I_Omega(bar rho|mu)
 =E_(bar rho mu) int_G |u_a-bar u|_Omega^2 w_q(da)
 >=0.                                                  (7)
```

This is the continuous compact-group form of K1606 and sharpens K1636's
Jensen inequality. For positive smooth densities, equality in (7) holds iff
all translated scores agree almost everywhere. Their log-density differences
are then constants; normalization makes the constants zero, so equality holds
iff `rho_a=rho` for Haar-almost every `a`, equivalently iff `rho` is stationary.

## K1694: strict saving for the cardinal product

Consider the pre-Haar K1678/K1689 independent scalar product on a nontrivial
complete cardinal block. Its Gaussian smoothing makes the density positive and
smooth. Each active coordinate has a common nonzero fourth cumulant
`kappa_4(Y_t)=t^2kappa_4(X)`.

Continuous translation acts on the cardinal coordinates by an orthogonal
matrix. For a genuine off-grid translation, at least one row contains two or
more nonzero entries. If that row is `(v_j)`, independence gives the transformed
marginal fourth cumulant

```text
kappa_4' = kappa_4(Y_t) sum_j v_j^4.                  (8)
```

Orthogonality gives `sum_jv_j^2=1`, while genuine mixing gives
`sum_jv_j^4<1`. Because `kappa_4(Y_t) !=0`, (8) differs from the original
marginal cumulant. The pre-Haar product density is therefore not translation
invariant. K1693 now makes the weighted Fisher reduction strictly positive at
every such finite cutoff:

```text
I_Omega(rho|mu)-I_Omega(bar rho|mu)>0.                (9)
```

Translation averaging preserves the covariance and integrated Wick defect,
so (9) strictly improves the finite-cutoff product trial energy relative to
the pre-Haar identity used to define the explicit upper functional. The result
does not bound the saving below by `cN^4`; it may be subleading, and the current
continuum upper coefficient remains an upper bound rather than an equality.

## K1695: protected integration and next frontier

The bridge census becomes 410 rows: 331 satisfied, ten conditional, 65
excluded and four missing. SC-ACT-01/02/06 remain `ASSERTS`; SC-META-53 remains
`UNCERTAIN`; the standing ledger remains 33 SAME / 22 DIFFERS / 31 NEEDS / 2
OVER-DETERMINED; and K1145/K1150 remain 0/7. No source, ledger, canon, paper,
prediction, confirmation or public verdict moves.

The strongest coefficient questions are now: make the fixed-shape expansion
uniform enough to compare shape-optimized envelopes; solve the exact
finite-strength scalar seed problem; determine the asymptotic order of the
strict Haar saving; construct one genuinely correlated fourth-cumulant tensor
or moving packet shape; or prove an unrestricted lower bound against the
widened trial functional. Compactness, Mosco convergence and `E_N+O(1)`
recentering still wait for the true coefficient and shift. The source-owned
action/domain/state/observation tuple remains separate.

## Postflight hostile review

- **Strongest overclaim:** (5) is fixed-shape and small-coupling; its remainder
  is not uniform over `C`, so it does not prove strict inequality between the
  globally shape-optimized envelopes.
- **Strongest contrary route:** a moving shape could make `tau`, `ell` or the
  seed remainder nonuniform, while a correlated cumulant tensor can leave the
  scalar product class entirely.
- **Weakest reproducibility seam:** the finite-cutoff strictness proof requires
  a genuine mixing translation and nonzero fourth cumulant. It does not apply
  to a coordinate permutation, a Gaussian channel, or an already stationary
  density.
- **Inference ceiling:** strict finite-`N` Fisher saving does not determine its
  `N^4` scale, the true coefficient, a minimizer, continuum state or GU
  physics.

The structural derivations, not numerical controls, carry K1691--K1694.
