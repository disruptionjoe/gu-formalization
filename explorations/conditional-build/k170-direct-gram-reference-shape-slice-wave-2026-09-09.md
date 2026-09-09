---
title: "K170 direct Gram and reference-shape slice wave"
status: active_research
doc_type: conditional_native_K139_one_vector_physical_Gram_K168_reference_shape_form_Rayleigh_and_matched_residual_result
created: 2026-09-09
date: 2026-09-09
claim_ceiling: direct native one-vector physical-Gram intervals and K168 reference-shape form, Rayleigh and matched-residual bounds on the K162 zero-bath seeds, using the limiting K139 Neumann series and an outward continuum point-profile integral; the coefficient-complete base R0 action, complete R_ref residual, M-orthogonal complement or flux floor and scalar-center left floor remain absent, so no native K152 interval, physical/source selection, Born derivation, prediction or confirmation follows
manifest: lab/process/k170-direct-gram-reference-shape-slice-wave.json
solver: tests/channel-swings/k170_direct_gram_reference_shape_slice.py
probe: tests/channel-swings/k170_direct_gram_reference_shape_slice_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K170 direct Gram and reference-shape slice wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: this packet stays on the repository-supplied K139--K169 positive
particle/hole signed point control. It evaluates the limiting K139 physical
Gram and the declared K168 trace-zero reference shape on the smallest K162
zero-bath seed lines. It does not evaluate the coefficient-complete K156 base
regular action or select the extension or scalar center physically.

```gu-typed-objects
result: the limiting K139 creation chart raises bath number exactly, so its Neumann words are orthogonal and give direct outward physical-Gram, dressed K168 shape-Rayleigh and matched shape-residual bounds on the K162 vacuum and one-impurity seed lines
carrier: hard-core C3 impurity tensor positive particle/hole antisymmetric Fock space over L2(R;C4), in q=(0,0),(1,0),(0,1), with zero-bath seeds belonging to every K162 dyadic cylinder range LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive physical Fock Hilbert pairing transported to regular coordinates by S=(1-G_256)^-1, M=S* S; the reference-shape residual uses the exact M^-1 dual identity ON=repository_signed_point_control
real_structure: CAR adjoint, momentum conjugation, real point profile and the Hermitian flavor-symmetric W_ref=diag(-2,1,1)
grading: conserved incidence charges q_i=n_i+N_i+-N_i-, hard-core impurity degree, bath-particle number, Neumann word order, K162 level and generalized shape Rayleigh quotient
action_owner: repository-construction -- the extension shape is a conditional reference coordinate; no response datum, Weinstein source or GU action selects its normalization, scalar center, polarization, couplings, domain or state
target: evaluate the native physical Gram and reference-shape slice without substituting a finite chart, then expose exactly which base-action, complete-residual, complement and left-floor fields still block K152 MAP-TYPE=intertwiner
```

## Inline preflight bookend

K169 kills the three-unit base-to-reference transfer but leaves direct
reference-specific K152 certification open below the neutral-cluster cap
`5/2`. Retrieval rechecked K139's limiting creation chart, K153's seed lines,
K156's combined normal-ordered regular representative, K162's dyadic carrier,
K165's `M`-orthogonal complement and K168's reference shape. K154 already
proves that chart/domain data cannot invent the base action, so this wave does
not repeat that insufficiency theorem.

The route census compared compressed finite pullbacks, direct common-carrier
quadrature, Neumann words, Feshbach/Birman--Schwinger complements,
Lehmann--Goerisch fluxes and shape variance. K163 forbids a compressed finite
chart. The limiting Neumann series nevertheless has an exact grading that
releases a genuine native slice before the missing base action: every `G`
creates exactly one bath excitation.

`SC-META-53` remains `UNCERTAIN`; `LT-SM8`, `RA-F1` and `AC-F1` remain
`NEEDS`. The source register and v0.263 physics ledger do not move.

## 1. Particle number diagonalizes the Gram expansion

At the fixed K139 chart,

```text
G=-(H0+256)^-1 C*,             S=(1-G)^-1.             (1)
```

The creation half `C*` creates exactly one positive-polarization bath
particle or hole, while the resolvent preserves bath number. Hence `G^n phi`
lies in bath-number sector `n` for either zero-bath seed. Distinct words are
orthogonal, and therefore

```text
M_phi=<phi,S* S phi>=sum_(n>=0)||G^n phi||^2.          (2)
```

Equation (2) is a limiting common-carrier identity, not a compressed finite-
chart Gram. With K153's `||G||<=q=3/8`, the untouched words from order two
obey the squared tail

```text
sum_(n>=2)||G^n phi||^2 <= q^4/(1-q^2)=81/3520.        (3)
```

This is strictly sharper in type than applying the ordinary Neumann norm tail
to a Gram: orthogonality removes all cross terms.

## 2. The first word is an explicit continuum integral

For one allowed impurity transition, the point profile has norm squared

```text
I=(2 pi)^-1 int_R dp/(sqrt(1+p^2)+256)^2.              (4)
```

Put `a=256` and `d=sqrt(a^2-1)`. The substitution `p=sinh(t)` gives

```text
I=(a d-acosh(a))/(pi d^3).                             (5)
```

The solver bounds (5) outward using only rational square-root intervals, the
positive atanh series for logarithms, and the classical rational enclosure
`333/106 < pi < 355/113`. No sampled momentum grid is used.

The vacuum `Omega` has two allowed first transitions, one to each occupied
impurity flavor, so `||G Omega||^2=2I`. The seed `d_1^*Omega` has only the
flavor-one particle transition, so `||G d_1^*Omega||^2=I`; hard core excludes
simultaneous impurity occupation. The complete signed flavor intertwiner gives
the identical statement for `d_2^*Omega` in `q=(0,1)`.

Combining (2)--(5) gives direct native one-vector intervals for the physical
Gram. They improve the generic K153 operator interval while preserving it.

## 3. The same grading evaluates the dressed reference shape

K168 fixes

```text
W_ref=diag(-2,1,1).                                    (6)
```

Each boundary word toggles between impurity vacuum and one occupied impurity.
Thus even and odd word sectors are also eigenspaces of (6). On the vacuum
seed, the occupied weight is the minority; on a one-impurity seed, the vacuum
weight is the minority. The first-word norm and (3) give an outward interval
for that minority probability `p`.

For the normalized dressed seed the shape Rayleigh quotient is respectively

```text
theta_00=-2+3p_occ,          theta_10=1-3p_vac.        (7)
```

Because (6) has only the two values `-2` and `1`, its matched physical
variance is exact:

```text
||(W_ref-theta) S phi||^2/||S phi||^2=9p(1-p).         (8)
```

By K168's pullback identity, (8) is the squared `M^-1` residual of the
reference-shape contribution. The compiled bound is below one on both seed
lines, substantially sharper than the universal three-unit norm budget.
It is trial specific and is not the complete `R_ref` residual: the base
`R_0` action and its covariance with (6) remain unevaluated.

## 4. Direct-reference release test

This wave closes three native one-vector fields:

1. limiting physical Gram intervals on the `q=(0,0)` and `q=(1,0)` K162 seed
   lines, with signed transport to `q=(0,1)`;
2. the dressed K168 reference-shape form and Rayleigh intervals; and
3. the matched reference-shape residual component.

It does not close:

1. the coefficient-complete combined base action `R_0 phi`;
2. the complete `R_ref` form-dual residual;
3. a positive complete `M`-orthogonal complement or flux floor below
   `E_ref(q)+5/2`; or
4. a native left floor at a physically selected scalar center.

The K156 normal-ordered form exists, but no current artifact serializes its
complete limiting action column on these seeds. K165/K169 provide the correct
complement type and an upper cap, not the required positive lower certificate.
Accordingly K152 remains closed. The neutral-cluster membership still does not identify the first threshold.

## Inline postflight bookend

- **Strongest native advance:** the limiting physical Gram is now evaluated
  directly on the smallest K162 seed lines, rather than bounded only by the
  global chart condition number.
- **Strongest reference advance:** the dressed noncommuting K168 shape has
  trial-specific Rayleigh and matched-residual bounds below its worst-case
  three-unit budget.
- **Strongest contrary fact:** those bounds concern only `W_ref`; without the
  combined base action they cannot be added to an unknown base residual.
- **Strongest overclaim:** “a small shape residual closes K152.” Refused; the
  complete residual and complete complement floor are separate native fields.
- **Weakest reproducibility seam:** using a finite compressed chart would
  reproduce neither (2) nor the limiting action. The solver instead certifies
  the continuum first word and all-word squared tail.

All five compatible mathematical arcs were attempted. The Gram, continuum
integral, seed slices and shape residual closed; the combined-form/complement
successor remains dependency-closed on the missing base action column and
complete flux solve. Physical extension and center selection remain authority-
excluded. No source, ledger, Born, prediction, confirmation, canon, paper,
release or public-posture truth moves.

## Next condition

Evaluate the coefficient-complete combined base action `R_0` on the same
K162 seed and its complete Hilbert/form-dual action column. Combine it with
the K170 Gram and shape bounds, then prove a positive complete `M`-orthogonal
complement or flux floor at a threshold below `E_ref(q)+5/2`. Select the
scalar center separately before asking for the native left floor.

## Reproduction

```bash
python3 tests/channel-swings/k170_direct_gram_reference_shape_slice.py --demo
python3 tests/channel-swings/k170_direct_gram_reference_shape_slice_probe.py
python3 tests/channel-swings/k170_direct_gram_reference_shape_slice_probe.py --selftest
```
