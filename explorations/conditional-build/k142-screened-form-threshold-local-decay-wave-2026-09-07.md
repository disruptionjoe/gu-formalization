---
title: "K142 screened form, threshold, and local-decay wave"
status: active_research
doc_type: conditional_all_sector_screened_point_fock_form_and_finite_boundary_channel_threshold_decay_result
created: 2026-09-07
date: 2026-09-07
claim_ceiling: exact repository-owned theorem for K141's supplied positive particle/hole control that the massive one-dimensional screened Gauss energy, with its self-energy convention explicit, is form controlled on all sectors by critical one-dimensional relativistic fermionic local exclusion and remains finite across the finite IBC boundary-mode dressing, so its positive or normally ordered version forms a semibounded self-adjoint sum with the common signed point operator; independently, the finite boundary-channel free point density has an inverse-square-root first threshold while full-rank point dressing gives square-root impurity-local onset and compact-energy-cutoff t^-3/2 matrix-element decay after point-spectrum projection; no finite-box screened norm-resolvent limit, global full-Fock HVZ or propagation theorem, Moller/Ruelle completeness, NESS/current, physical extension or screening selector, smooth unreduced parent, Weinstein/source/GU owner, Born derivation, prediction or confirmation follows
manifest: lab/process/k142-screened-form-threshold-local-decay-wave.json
probe: tests/channel-swings/k142_screened_form_threshold_local_decay_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K142 screened form, threshold, and local-decay wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) 126
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> lab/methods/source-native-comparator-routing.md and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: this packet remains on K139--K141's repository-supplied positive
particle/hole point control. It adds one named massive screened Gauss energy to
the common infinite-volume operator as a quadratic-form sum and analyzes the
first threshold only in the finite boundary/Friedrichs channel. It does not
select the polarization, extension, couplings, screening mass or state and it
does not reconstruct a source/GU action.

```gu-typed-objects
result: critical one-dimensional relativistic fermionic exclusion controls the massive screened Gauss form on every Fock sector and the finite IBC boundary modes preserve that form domain; a separate finite boundary-channel calculation changes inverse-square-root free point threshold density into square-root impurity-local onset and compact-cutoff t^-3/2 decay under full-rank dressing
carrier: C9 impurity and C512 Klein module tensored with antisymmetric Fock space over L2(R;C36), decomposed into the finite span of the 36 resolvent-dressed point modes and its regular complement LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: standard positive particle/hole Fock Hilbert pairing and finite-dimensional Hermitian boundary pairing; the screened form is the positive quadratic energy of the repository-supplied charge density against Y_kappa=(-d_x^2+kappa^2)^-1 ON=repository_signed_point_control
real_structure: K140's supplied positive particle/hole real structure and charge-conjugation relation are retained; neither the form estimate nor threshold rank selects them
grading: matrix units are even, Klein/CAR fields are odd, defect monomials are even, fermion number grades the local-exclusion estimate, and point spectrum is projected before the cutoff decay statement
action_owner: repository-construction -- the signed free operator, time orientation, polarization, charges, couplings, W, screening mass kappa, self-energy convention and state are not selected by Weinstein's source or a GU action
target: all-sector screened form sum on K141's common carrier plus finite-boundary-channel first-threshold and local-decay classification MAP-TYPE=intertwiner
```

## Inline preflight bookend

K141 leaves two explicit compatible arcs. The first is the missing 36-species
fermionic estimate behind its crude `N^2` bound. The second asks what spectral
threshold and local decay the already-constructed signed point operator has
before any Moller/Ruelle attempt. They use different instruments: critical
local exclusion and form theory for the first, a finite-matrix Weyl function
and stationary phase for the second.

Object retrieval found the one-dimensional fractional Lieb--Thirring
inequality through the general Sobolev/Lieb--Thirring equivalence of Frank,
Lieb and Seiringer ([arXiv:0909.5449](https://arxiv.org/abs/0909.5449)) and the
fractional/relativistic extension in their earlier work
([arXiv:math/0610593](https://arxiv.org/abs/math/0610593)). The local-exclusion
route and finite internal multiplicity are also explicit in Lundholm and
Solovej ([arXiv:1205.2520](https://arxiv.org/abs/1205.2520)). These are method
anchors, not source/GU ownership. Repository retrieval found no prior
application to K141's screened IBC carrier and no prior point-threshold Weyl
calculation. No canonical correction supersedes the K139--K141 inputs.

The route census covered fractional kinetic inequalities, interval local
exclusion, Yukawa convolution, signed charge and self-energy conventions,
normal ordering, finite boundary-mode CAR algebras, the Bessel-`K_0`
singularity, closed form sums, massive one-dimensional density of states,
matrix Weyl functions, dark channels, threshold resonances, stationary phase,
Cook integrability, HVZ/Ruelle prerequisites and source ownership. A one-body
density-only Hartree estimate is insufficient for correlated states; the
proof therefore uses the many-body local-number form directly. Computation
checks scalings and exact threshold transforms, not the functional-analysis
proof.

## 1. Critical relativistic exclusion removes the `N^2` obstruction

Let `F=36`, let `T=dGamma(|p|)` on the antisymmetric Fock space over
`L2(R;C^F)`, and let `N_I` be the smoothly localized number in an interval of
length `ell`. The one-dimensional order-one fractional Lieb--Thirring/local-
exclusion inequality has the critical form

```text
 sum_I <N_I^2> <= C F (ell <T> + <N>)                 (1)
```

for a bounded-overlap smooth interval partition. The constant depends only on
the fixed partition convention, not on particle number, state or volume. This
is the operator/local-number version required here. The corresponding density
statement `integral rho^2 <= C F <T>` is a consequence, but replacing (1) by a
Hartree expression would not control arbitrary correlated two-particle
density and is not the argument used.

For `ell=kappa^-1`, exponential decay and bounded overlap give

```text
 sum_(i,j) exp(-kappa |x_i-x_j|)
   <= C sum_I N_I^2
   <= C F (kappa^-1 T+N).                             (2)
```

If every particle/hole charge obeys `|q_alpha|<=q_*`, the positive screened
field energy

```text
 E_kappa=1/2 <rho,Y_kappa*rho>,
 Y_kappa(x)=exp(-kappa|x|)/(2 kappa)                  (3)
```

satisfies, as a many-body quadratic form,

```text
 0 <= E_kappa
    <= C F q_*^2 (kappa^-2 T+kappa^-1 N)
    <= C F q_*^2 (kappa^-2+(kappa m)^-1) H_0.         (4)
```

The second inequality also bounds the absolute-charge majorant, so signed
particle/hole charges cause no gap. Equation (4) is uniform over all Fock
sectors and volumes. It is exactly the estimate K141 lacked; the finite species
count and the order-one one-dimensional kinetic energy are load bearing.
Neither bosonic statistics nor an unbounded species multiplicity inherits it.

The convention in (3) includes the diagonal field self-energy
`q_alpha^2 Y_kappa(0)/2=q_alpha^2/(4 kappa)` per particle. Normal ordering
subtracts

```text
 S_kappa=sum_alpha q_alpha^2 N_alpha/(4 kappa),        (5)
```

which is only linear in `N` and therefore `H_0`-form bounded by the mass gap.
Thus the normally ordered form is semibounded even though it is no longer
positive. This convention cannot be left implicit: K141's neutral-pair energy
already used the self-inclusive positive field energy.

## 2. The finite IBC boundary modes do not reopen the form-domain gap

K141's signed point domain is not simply the free form domain. Its boundary
map creates or annihilates the finitely many vectors

```text
 h_(alpha,lambda)(p)=c_alpha/(sqrt(m^2+p^2)+lambda).   (6)
```

They lie in `L2` but at the free `H^(1/2)` endpoint. In position space their
short-distance behavior is logarithmic (the same local class as modified
Bessel `K_0`) and their massive tail decays exponentially. Consequently

```text
 h_alpha^vee in L2(R) intersect L4(R),                 (7)
```

even though the naive half-derivative norm is borderline divergent.

Let `B` be the at-most-36-dimensional span of these one-mode-per-species
boundary vectors. Fermionic occupation of `B` is bounded by `dim B`; its
boundary--boundary screened energy is finite by boundedness of `Y_kappa`, and
its boundary--regular cross energy is bounded by a constant times the regular
particle number. On `B^perp`, (2)--(4) apply unchanged. The finite CAR algebra
and K139's uniformly invertible Neumann boundary chart therefore give

```text
 E_kappa[(1-G_lambda)^-1 phi]
   <= C_(kappa,F,q_*,G) (q_K[phi]+||phi||^2)           (8)
```

on the regular form coordinate `phi`, where `q_K` is K139's shifted positive
regular form. This is the missing boundary-mode step: citing only (4) would
incorrectly assume that the IBC dressing preserved the free half-derivative
domain.

After one finite lower shift, K141's `H_infinity^(pol,W)` has closed form
`q_point` in these coordinates. Equations (4), (7) and (8) imply that

```text
 q_(kappa,W)=q_point+E_kappa                            (9)
```

is a densely defined closed semibounded form on the same dressed form domain.
It therefore defines one self-adjoint all-sector screened Hamiltonian
`H_(kappa,W)`. Replacing `E_kappa` by its normally ordered version from (5)
gives another semibounded self-adjoint form sum on that domain.

This closes existence on the common infinite-volume carrier. It does not prove
norm-resolvent convergence of screened finite-box cutoffs: that stronger
claim needs a uniform Mosco/core comparison for the periodic screened forms
through the singular boundary chart and is not smuggled in from K141's local-
defect norm-resolvent theorem.

## 3. The first point threshold has two different exponents

The independent threshold calculation starts with one massive continuum
channel. With Fourier coefficient `(2 pi)^-1/2`, the free point spectral
density at energy `E>m` is

```text
 nu_0(E)=integral dp/(2 pi) delta(E-sqrt(m^2+p^2))
        =E/(pi sqrt(E^2-m^2))
        ~sqrt(m/2)/(pi sqrt(E-m)).                    (10)
```

Thus a generic free point correlation with a smooth energy cutoff nonzero at
`m` decays as `t^-1/2`, which is not time integrable. The mass gap does not by
itself give Cook decay.

For the scalar Friedrichs/IBC boundary channel, write the renormalized
denominator as

```text
 d(z)=a-z-g^2 M(z),
 Im M(E+i0)=pi nu_0(E).                               (11)
```

The divergent imaginary part dominates every finite `a` and finite
renormalized real part when `g!=0`. Hence the impurity-local spectral density
satisfies

```text
 nu_imp(E)=(1/pi) Im d(E+i0)^-1=O(sqrt(E-m)).          (12)
```

For a finite boundary matrix the same conclusion holds on the range of the
leading endpoint matrix `D`: if `D>0` on the whole boundary space, the inverse
boundary response is `O(sqrt(E-m))` in norm. If `D` has a kernel, dark
components are governed by the finite threshold matrix and may retain an
eigenvalue, resonance or unsuppressed channel. Full-rank response is therefore
a mathematical decay hypothesis here, not the physical selector of `W` that
K140 still lacks.

Let `chi` be smooth, compactly supported in a small interval beginning at the
first threshold, vanish to all orders at its upper endpoint, and let point
spectrum be projected out. Watson's lemma/stationary phase applied to (10) and
(12) gives

```text
 free point matrix element       =O(|t|^-1/2),
 full-rank impurity-local element=O(|t|^-3/2).         (13)
```

The second rate is integrable. It is a finite boundary-channel, compact-energy
matrix-element estimate. It is not a global local-decay norm for
`H_(kappa,W)`: the screened interaction, all many-body thresholds, channel
identification, high-energy resolvent bounds and propagation estimates have
not been controlled.

## 4. Exact consequence for the scattering frontier

K142 opens a narrower route than “the Hamiltonian exists, therefore
scattering exists.” The screened all-sector form is now available, and the
first full-rank impurity channel has the favorable integrable threshold
exponent after removing bound states. But a Moller/Ruelle theorem still needs:

1. an HVZ-type description of every cluster threshold for the number-changing
   screened point Hamiltonian;
2. absence or explicit projection of threshold eigenvalues and resonances in
   every open channel, including dark subspaces;
3. weighted resolvent or propagation estimates uniform across the many-body
   thresholds and at high energy; and
4. asymptotic channel identification and completeness, followed separately by
   a return-to-NESS/current theorem.

The numerical threshold locations depend on the bound spectrum and therefore
on the supplied `W`, couplings and `kappa`. No actual response datum or action
principle selects those values.

## Inline postflight bookend

- **Strongest advance:** the 36-species critical relativistic local-number
  estimate and finite boundary-mode split close a semibounded all-sector
  screened form sum on K141's common carrier.
- **Strongest independent result:** free point density diverges as
  `(E-m)^-1/2`, while full-rank boundary dressing makes the impurity-local
  density vanish as `(E-m)^1/2` and yields compact-cutoff `t^-3/2` decay after
  point-spectrum projection.
- **Strongest boundary:** the form-sum theorem is not a screened finite-box
  norm-resolvent limit, and the decay theorem is not a full-Fock propagation
  or asymptotic-completeness result.
- **Strongest overclaim:** “screening plus a mass gap proves NESS.” Refused.
  Many-body thresholds, dark channels, high-energy bounds and channel
  completeness remain unproved.
- **Strongest contrary route:** rank loss can retain a dark threshold
  eigenvalue/resonance, and removing `kappa` restores K140's long-range
  obstruction. Both are explicit failure modes rather than suppressed cases.
- **Weakest reproducibility seam:** (8) uses the finite one-mode-per-species
  content of K139's boundary map. A boundary construction with infinitely many
  independent singular modes would require a new estimate.

The companion probe checks Yukawa norms and self energy, the critical filling
scaling, boundary-mode logarithmic integrability, the exact density of states,
the two threshold exponents and their exact Laplace-transform decay powers,
plus the manifest claim boundary under baseline-first hostile mutations. No
global HVZ theorem, Moller/Ruelle completeness, interacting NESS, microscopic
current, physical `W` or `kappa`, smooth unreduced connection/BRST parent,
Weinstein/source/GU action, Born rule, held-out score, prediction,
confirmation, canon, paper, release or public-posture move follows.

## Next condition

Prove the uniform Mosco/core convergence of periodic screened forms through
the signed IBC boundary chart, or exhibit the exact failure, to decide whether
K142's screened Hamiltonian is the strong/norm-resolvent thermodynamic limit
of finite boxes rather than only a direct common-carrier form sum.
Independently build an HVZ theorem and threshold-rank census for the complete
36-species number-changing operator; only then attempt weighted propagation,
Moller/Ruelle completeness and return-to-NESS. Physical selection still needs
an actual full-rank response datum or action principle, while source/GU
ownership must independently supply the free operator, time orientation,
polarization, charges, couplings, domain and state.

## Reproduction

```bash
python3 tests/channel-swings/k142_screened_form_threshold_local_decay_probe.py
python3 tests/channel-swings/k142_screened_form_threshold_local_decay_probe.py --selftest
```
