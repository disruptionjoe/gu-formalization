---
title: "K1816--K1820 full-Fisher slab-three leafwise calibration wave"
status: active_research
doc_type: exploration
updated_at: "2026-10-19"
---

# K1816--K1820: complete boundary closure; interior uniqueness remains open

## October 19 structural completion

K1819 now closes **all 114 exposed atomic faces and all 114 vertices of
the slab-three retained union**. K1804's earlier 122/122 census describes
the union across both slabs two and three; it was incorrectly carried as a
slab-three-only obligation. The original atlas remains valid in its own scope.
The complete corrected K1818 bank still has nine gradient exclusions and
43 method-indeterminate leaves. Its incomplete Bernstein replacement is not
used here. Complete stationary uniqueness and global optimality remain open.

Classification: `INTERNAL_STRUCTURAL_ONLY`. This result is independent scalar
variational mathematics and conveys no source-owned physical state, observable,
prediction, confirmation or unrestricted-infimum claim.

```gu-typed-objects
result: K1819 compact-support value transfer and finite-closed-cover boundary theorem
carrier: real scalar functions of observation y and rational parameter rectangles (t,z); LAYER=toy; CHIRALITY=N/A
pairing: integral rho_theta(y) f(y) g(y) dy ON=real scalar functions in L2(rho_theta)
real_structure: ordinary real conjugation
grading: N/A
action_owner: repository-construction
target: full Fisher objective J(theta) and boundary of retained slab-three union; MAP-TYPE=not-a-map
```

### Compact support removes the tail obligation for this lower witness

Use the same positive density and score as the existing producers:
`rho=G D/(sqrt(v) sqrt(2 pi))`, `s=sqrt(t) R/(v D)`, and
`J=integral_R rho s^2`. Here `G,D,R,v` are exactly the K1807/K1816
mixture quantities, with no change of measure or compact renormalization.
On every certified parameter box, `0<t<1`, `0<z<1` and
`2t^2>1/1024` keep the mixture chart positive and nonsingular.

Let `C=[-11,11]` and `H=1_C h0`, where `h0` is the fixed K1787 score.
Then the already-certified compact quantities are exactly
`A_C=<s,H>_rho` and `B_C=<H,H>_rho`. Cauchy gives
`J B_C >= A_C^2`. The certified `A_C>0` implies `B_C>0`, so the
26 strict compact cross margins `A_C^2-T B_C>0` imply `J>T` on
the entire closed parameter boxes, including their faces and vertices.
The threshold is `T=7958932265249/50000000000000000000`.

No derivative or integration by parts of `H` occurs, so its jumps at the
window endpoints cause no distributional boundary term. This does **not**
certify the different untruncated `h0` witness's whole-line cross margin.
K1808's untruncated tail result remains valid; it is unnecessary for this
support-truncated lower witness. No new quadrature is used.

### Finite closed pruning removes the remaining boundary calculations

Let `D` be K1771's original closed slab-three rectangle:

```text
t in [887855469/17179869184, 4059652289/68719476736]
z in [17/32, 37/64].
```

K1791 and K1796 use finite bisections into closed rectangles. Let `P` be
the union of their strictly pruned boxes and `R` the final retained union.
Their accepted complete partition certificates give `D=P union R`; every
point of `P` satisfies `J>T0`, where
`T0=31835729061/200000000000000000` and
`T0-T=1/50000000000000000000>0`.

For `p` on the boundary of `R` and in the interior of `D`, choose points
of `D` outside `R` approaching `p`. They lie in `P`. A finite union of
closed boxes is closed, so `p` lies in `P` and inherits its strict lower
bound. This uses the finite closed partition, not a continuity inference
that a positive value off a boundary must remain strictly positive there.

Exact Fraction geometry reconstructs 114 exposed faces and 114 vertices
from K1816's 78 boxes. Direct positive-box inheritance covers 45 faces
and 47 vertices. The other 69 faces (including endpoints) and 67 vertices
are strictly inside `D`, hence covered by the lemma. All 13 faces and
14 vertices on the original domain boundary have direct witnesses from
leaves 0--12. No stationary exclusion is used to claim boundary values.

The K1819 artifact records every face/vertex, direct witness identity or
closed-cover proof, exact threshold slack and the linked partition digests.
This composes accepted K1791/K1796 certificates; their costly numerical
predicates and K1816 quadrature were not independently recomputed.

### Verification and scope review

An independent read-only review checked the density/score scaling, the
unrenormalized measure, the Cauchy hypotheses, all 78 checkpoint hashes,
positive chart, exact threshold difference and boundary geometry. Exact
finite-measure controls check signed scores and compact support; a cancellation
control distinguishes the untruncated witness. Hostile mutations reject wrong
thresholds, windows, anchors, partition links, missing terminal cells and
unsupported outer-domain closure. K1819's producer passes 15 controls, its
probe passes 18 controls, and K1820's producer/probe pass 11/3 controls.
These are composition, geometry and mutation checks, not fresh quadrature.

Publication status: coherent provisional checkpoint of the ongoing wave.
The boundary composition and its checks are complete; final wave acceptance
also requires the native `RESEARCH-STATUS.md` promotion rollup. That file is
outside this wave's frozen write scope, so the rollup remains an explicit
next-admission obligation. The current status, roadmap and verification
surfaces are reconciled here; no canon or global-optimizer promotion occurs.

| Claim | Prior result | Current result | Load-bearing evidence |
| --- | --- | --- | --- |
| K1819 exposed slab-three boundary | unclosed, with two-slab census carried forward | all 114 faces and 114 vertices excluded at T | K1771, K1791, K1796, K1816 and the two arguments above |
| K1820 global optimizer | unproved | unproved; interior stationary uniqueness remains | K1787 local certificate and incomplete interior cover |

The older account below is retained as **historical through October 16**.
Its open-boundary wording is superseded by this section. This is an
active-research result, not canon promotion.

## Historical result through October 16

K1816 now contains the complete atomic, digest-checked fixed K1787-score bank
on all 78 exact K1796 slab-three leaves. The selected uniform configuration is
parameter order eight, observation order fourteen and 88 rational observation
cells of half-width `1/4`. It proves strict compact margins on exactly 26
leaves: `0--12` and `65--77`. The contiguous block `13--64` is
method-indeterminate, with zero counterexample flags. The worst uniform lower
endpoint occurs on leaf 53 at `-9.2561445289e-25`.

The completed bank changes the route. Raising leaf 53 to observation order
sixteen improves its lower endpoint to `-4.1152250086e-25` but does not close
it. Exact t-only, z-only, depth-two, depth-three and targeted t-by-z scouts
drive the enclosure toward zero while remaining indeterminate. At the exact
rational lower-t/mid-z point, however, the same fixed witness has a strictly
positive margin `8.2260790157e-29`. Thus the negative box endpoints are still
certificate-method limits, not counterexamples, but the vanishingly small
point margin makes deeper value subdivision computationally dominated.

K1818's first full-objective gradient bank exposed a remainder-domain defect
during hostile review. The Taylor polynomial is centered at K1787, but the
degree-eight derivative enclosure was evaluated only on each target leaf. For
every leaf outside the anchor, Taylor's intermediate point can lie on the
segment between the anchor and leaf, so the derivative enclosure must cover
the complete anchor-to-leaf hull. The ten apparent stationary exclusions are
therefore withdrawn before downstream use. They do not change K1816's value
bank or K1787's local stationary certificate.

The corrected producer uses configuration-distinct checkpoints and the exact
axis-aligned hull of K1787's anchor with each target leaf. The complete replay
rigorously excludes leaves `27`, `28`, `39--42`, `52`, `53`, and `64` by at
least one whole-line gradient component. The other 43 candidates remain
method-indeterminate, including leaf 50 containing K1787's named stationary
box; retention is not evidence of another stationary point. K1804's 122
exposed atomic faces and 122 exposed vertices remain open. Stationary
uniqueness, global optimality, unrestricted scope and source-owned physics
remain withheld.

## Exact gradient replay and current continuation

```bash
UV_CACHE_DIR=/private/tmp/uv-cache-gu-science uv run --offline --with python-flint==0.9.0 --with sympy==1.14.0 python tests/channel-swings/k1818_full_fisher_slab_three_stationary_cover.py --resume-bank --summary
```

The command reuses only corrected anchor-hull checkpoints; the invalidated
leaf-only files have distinct names and are ineligible. Leaf-centered
reexpansion or a complete interval-Newton/Krawczyk cover is now required on the
43 retained leaves. Exposed-boundary closure is now supplied above. Complete
interior stationary uniqueness and protected global admission remain downstream.
