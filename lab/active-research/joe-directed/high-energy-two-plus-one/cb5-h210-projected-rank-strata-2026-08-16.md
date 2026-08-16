---
artifact_type: exploration
status: exploration
doc_type: conditional_build_exact_projected_rank_classification
created: 2026-08-16
work_item: CB5-B
channel: high_energy_two_plus_one_prediction
target_claim: SC-GEN-53
title: "CB-5B: H210 four-dimensional trace/RS projected-rank strata, exact counterexamples, and the observation-induced F-carrier ceiling"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
grade: "Basis-free Clifford reduction plus exact QQ, GF(1009), and GF(1013) certificates on both real K77 ambient Weyl halves. H210 is a declared conditional horn. No source action, selector, graph, background, family row, PS reduction, external datum, or physical quotient is derived."
disposition: PROJECTED_RANKS_NOT_FUNCTIONS_OF_RAW_RANK__NEITHER_PROJECTION_VANISHES_OFF_ZERO__BANKED_FULL_FULL_IS_GENERIC_BUT_NOT_UNIVERSAL__KERNEL_INTERSECTION_EXACT__HORIZONTAL_TRACE_IS_OBSERVATION_INDUCED_NOT_UPSTREAM_SOURCE_F
probe: tests/channel-swings/joe_directed_cb5_h210_projected_rank_strata_probe.py
canon_verdict_change: none
depends_on:
  - lab/active-research/joe-directed/high-energy-two-plus-one/he4-path-reprioritization-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb3-h210-literal-pullback-rank-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb4-wave-h210-naturality-reprioritization-2026-08-16.md
  - lab/process/hostile-reviews/2026-08-16-joe-directed-cb4-h210-naturality-review.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb5-h210-source-fq-bridge-2026-08-16.md
  - explorations/conditional-build/selected-k77-local-twistor-bach-detour-composition-gate-2026-08-14.md
  - lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md
  - explorations/draft-fqz-map-decider-2026-08-03.md
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact borders
> Weinstein's source-native `2+1`, imposter, F/Q/Z, Pati--Salam, and
> emergent-chirality proposal. Ordinary family indices, net-chirality
> arguments, scalar-Higgs/VEV models, conventional `SO(10)` mass mechanisms,
> anomaly selectors, and familiar vector-mass routes bind only those named
> comparators. They do not adjudicate this construction without an explicit
> typed bridge. Read `lab/methods/source-native-comparator-routing.md`.
>
> Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

# CB-5B — projected H210 rank strata

## Result first

The banked H210 receiver's full/full fingerprint is **generic but not
universal**. More importantly, neither projected rank is a function of the
raw contracted rank:

```text
rank(A_J) does not determine rank(F_J^tr),
rank(A_J) does not determine rank(Q_J^RS).
```

There are exact rational counterexamples with the same `rank(A_J)=64` on one
real ambient Weyl half but fingerprints

```text
(rank A_J, rank F_J^tr, rank Q_J^RS) = (64,64,64)
                                            and (64,40,56).
```

At the coefficient level, however, both projected constructions are
injective in the weighted observer map `W`: on either ambient half,

```text
F_W^tr = 0  iff W=0,
Q_W^RS = 0  iff W=0.
```

Since `A_W=0 iff W=0`, neither projected map can vanish while the contracted
H210 map is nonzero. What varies is its rank on spinors, governed by the
Clifford incidence of the horizontal and normal directions rather than by
`rank(A_W)` alone.

The exact kernel law is

```text
ker(A_W) = ker(F_W^tr) intersection ker(Q_W^RS).
```

The two projected kernels can be unequal, can both be nonzero, and can have a
nonzero intersection. Their ranks must not be added as family counts.

One source boundary becomes sharper. The upstream H210 tensor is a pure-normal
gamma-traceless **Z-sector** port, so its canonical correlated F projection is
zero. A nonzero `F_J^tr` arises only after literal observation contracts that
normal one-form leg into a horizontal one-form. It is therefore an
observation-induced F-shaped adapter, not proof that the upstream H210 tensor
was the equation-(12.22) F summand and not proof of source-F provenance.

## Conditional-build and source fences

This artifact assumes `H210`. It does not derive or choose the source action,
background, observer graph, section, selector, family row, PS reduction, or
external datum. The following three horns remain independent:

```text
H210-ALIGN = identify M_3/ker(r) with the source F/imposter provenance line;

H210-PSRED = reduce observer-normal overlaps at least to N(PS);

H210-FCORR = the observation-induced correlated lift
             kappa_J Gamma_4 O_J T is the typed realization of the
             equation-(12.22) F reveal for the H210 route.
```

`H210-FCORR` supplies neither the family-line identification of `H210-ALIGN`
nor the moving subgroup data of `H210-PSRED`. None of the three is promoted
from conditional input to an action-owned selection.

The names in this artifact are decorated deliberately:

```text
F_J^tr = four-dimensional horizontal Clifford-trace component,
Q_J^RS = four-dimensional horizontal gamma-traceless component.
```

`F_J^tr` is not silently renamed the source's imposter. `Q_J^RS` is not the
source's entire Q summand. The internal `144` remains the distinct Z-sector
partner, and literal contraction does not restore its free normal covector
index.

## Basis-free classifier

Let `H` have signature `(1,3)`, let `V` have signature `(6,4)`, and absorb the
nonzero H210 Clebsch weights into

```text
W = diag(-2,-2,-2,-2,-2,-2,3,3,3,3) J in Hom(H,V).
```

With the fixed invertible normal volume factor `phi_4`, the contracted map is

```text
A_W(s)_mu = c_V(W_mu) phi_4 s.
```

The useful basis-free mixed Clifford invariant is

```text
C_W = Gamma_4 A_W
    = sum_mu eta_H(mu,mu) c_H(e_mu)c_V(W_mu) phi_4.
```

Because `j_4` is injective,

```text
rank(F_W^tr) = rank(C_W|S_half),
F_W^tr       = (1/4) j_4 C_W,
Q_W^RS       = Pi_4 A_W.
```

Thus the three rank functions are determinantal invariants of three different
polynomial matrix families on `Hom(H,V)`. They are Spin(H)-by-Spin(V)
invariant under co-moving frames, but arbitrary row rank forgets the relative
Clifford incidence carried by `C_W` and `Pi_4 A_W`.

There is also an exact nonvanishing certificate. The coefficient maps

```text
H* tensor V -> Hom(S_half, im(j_4)),
H* tensor V -> Hom(S_half, ker(Gamma_4))
```

are linear maps out of the `40`-dimensional coefficient space. With the H210
volume factor `phi_4` held fixed, one must not invoke irreducibility under the
full normal spin group: `phi_4` is extra tensor data and is not fixed by that
whole group. Instead, the exact rational certificate computes coefficient
rank `40` for both `F^tr` and `Q^RS` on each half over `QQ`; `GF(1009)` and
`GF(1013)` independently replay the same rank. Thus both coefficient maps are
injective in this declared H210 tensor family. This is why projected rank can
drop but cannot fall all the way to zero away from `W=0`.

## Exact normal forms and counterexamples

Write `e_i^2=+1`, `f_j^2=-1` in `V`, and
`h_0^2=+1`, `h_1^2=h_2^2=h_3^2=-1` in `H`. The table reports ranks on either
real ambient K77 Weyl half; the two halves agree exactly in every row.
Parentheses give the prior internal-complex normalization, obtained by
dividing these matrix ranks by four.

| weighted map `W:H->V` | `rank W` | `rank A` | `rank F^tr` | `rank Q^RS` | role |
|---|---:|---:|---:|---:|---|
| `0` | 0 | `0 (0)` | `0 (0)` | `0 (0)` | flat control |
| `W(h_0)=e_0` | 1 | `64 (16)` | `64 (16)` | `64 (16)` | non-null rank-one |
| `W(h_0)=W(h_1)=e_0` | 1 | `64 (16)` | `32 (8)` | `64 (16)` | external-null trace counterexample |
| `W(h_0)=e_0+f_0` | 1 | `32 (8)` | `32 (8)` | `32 (8)` | internal-null rank-one |
| `W(h_0)=W(h_1)=e_0+f_0` | 1 | `32 (8)` | `16 (4)` | `32 (8)` | same raw rank, smaller trace rank |
| `W(h_i)=e_i+f_i`, `i<2` | 2 | `48 (12)` | `32 (8)` | `48 (12)` | CB4 isotropic preview |
| `W(h_i)=e_i+f_i`, `i<3` | 3 | `56 (14)` | `40 (10)` | `56 (14)` | isotropic three-plane |
| `W(h_i)=e_i+f_i`, `i<4` | 4 | `60 (15)` | `40 (10)` | `56 (14)` | maximal isotropic four-plane |
| `W(h_0)=e_0+f_0`, `W(h_1)=e_0-f_0` | 2 | `64 (16)` | `64 (16)` | `64 (16)` | paired-null/non-null-span control |
| `W(h_0)=e_0`, `W(h_i)=f_{i-1}`, `i=1,2,3` | 4 | `64 (16)` | `40 (10)` | `56 (14)` | signature-matched incidence counterexample |
| banked rational receiver | 4 | `64 (16)` | `64 (16)` | `64 (16)` | generic-locus witness |

Two counterexample pairs settle the rank-function question separately:

1. The two internal-null rank-one rows both have `rank(A)=32`, while their
   trace ranks are `32` and `16`.
2. The non-null rank-one row and signature-matched rank-four row both have
   `rank(A)=64`, while their Q ranks are `64` and `56` (and their trace ranks
   are `64` and `40`).

Consequently neither `rank(F^tr)` nor `rank(Q^RS)` factors through
`rank(A)`. Even restricting to the full-`A` stratum does not repair the claim.

## Generic versus special

Every maximal-rank condition is the nonvanishing of at least one matrix minor.
The banked receiver is a rational point at which all three maps have maximal
rank `64`. Therefore

```text
U = {W : rank A_W = rank F_W^tr = rank Q_W^RS = 64}
```

is a nonempty Zariski-open subset of the affine `40`-dimensional space
`Hom(H,V)`. Since that affine space is irreducible, `U` is Zariski dense; over
the reals it also contains an ordinary open neighborhood of the banked point.
So the banked full/full preview is genuinely generic in the declared finite
tensor family.

It is not universal. Null incidence, maximal isotropic incidence, and the
signature-matched embedding give explicit proper determinantal strata. The
signature-matched row is especially adverse: `A` is already injective while
both projected maps have kernels. Genericity therefore cannot be summarized
as “the split preserves rank.”

## Kernels and family exact sequences

The projector decomposition is a direct codomain decomposition. Hence, for
every input spinor `s`,

```text
A_W s=0  iff  F_W^tr s=0 and Q_W^RS s=0,
```

which gives

```text
ker(A_W)=ker(F_W^tr) intersection ker(Q_W^RS).
```

This identity was checked exactly in every row and field by stacking the F/Q
maps and reproducing `rank(A)`.

The kernels need not coincide:

- for `W(h_0)=W(h_1)=e_0+f_0`, their probe-unit dimensions are
  `dim ker A/F/Q = 32/48/32`; the intersection is the nonzero `32`-plane;
- for the signature-matched embedding they are `0/24/8`; both projected
  kernels are nonzero and different, while their intersection is zero;
- at the banked receiver all three intrinsic kernels vanish.

Let `r:M_3->C` be the separately declared nonzero family row and let
`B` stand for `A`, `F^tr`, or `Q^RS`. There is a basis-free exact sequence

```text
0 -> ker(r) tensor S -> ker(r tensor B) -> ker(B) -> 0,
```

so

```text
dim ker(r tensor B) = 2 dim(S) + dim ker(B).
```

No splitting or named family is canonical. In the prior internal-complex
normalization `dim S=16`, the banked family kernels are all `32`; the
signature-matched family kernels are respectively `32`, `38`, and `34` for
`A/F/Q`. Their intersection is the `A` family kernel. These are kernels of
shared-domain maps, not counts of independent families or particles.

## Source F/Q/Z boundary and `Pi_4 != Pi_14`

Equation (12.22)'s source F term lives inside the ambient gamma-traceless
carrier as a correlated horizontal/normal trace pair. With the chirality
correlation suppressed from notation, its pointwise split-canonical lift has
the form

```text
kappa(tau) = ((1/4) j_4 tau, -(1/10) j_10~ tau) in ker(Gamma_14).
```

The second component is not optional: it cancels the horizontal trace in the
ambient gamma trace. The lift has the same domain kernel and rank as `tau`,
because the horizontal `j_4` component is injective.

This pointwise formula has not yet been certified as a full co-moving
horizontal/normal natural transformation. That larger square must also move
the normal complement, normal coframe, graded normal Clifford injection, and
the two-half chirality correlation. CB-5 certifies only the horizontal
`F_J^tr/Q_J^RS` co-moving squares.

By contrast, the upstream H210 tensor has zero horizontal covector component
and is gamma-traceless in its normal covector component. It lies in Z and has

```text
P_F,corr(T_H210)=0.
```

After observation, `tau_J=Gamma_4 A_J` can be nonzero. `F_J^tr` is only the
horizontal component of `kappa(tau_J)`. Completing it by the normal correlated
piece constructs an observation-induced `Z -> F-shaped carrier` adapter. It
does not show that a pre-existing source F component survived, does not
recover the consumed free `144` index, and does not identify a family line
with imposter provenance.

This also preserves the twistor warning:

```text
Pi_4 != Pi_14.
```

The positive embedding of a four-dimensionally gamma-traceless carrier into
ambient `ker Gamma_14`, and the correlated lift above for a trace spinor, do
not identify the projectors or their source-to-target maps.

## Adverse conclusions and claim ceiling

The exact calculation kills four tempting statements:

1. `rank(A)` classifies the projected ranks — false by two rational
   counterexample pairs.
2. A nonzero H210 contraction forces either projected map to vanish — false;
   both coefficient maps are injective.
3. Full `A` rank forces full projected ranks — false at the
   signature-matched embedding.
4. `rank(F)+rank(Q)` counts independent outputs or families — false; at the
   banked receiver it would give `128` although the stacked map still has
   rank `64`.

What survives is formal conditional geometry: the decorated projected ranks
and kernel intersections are intrinsic determinantal data of the co-moving
associated map on admitted overlaps. Nothing here constructs a source action,
vacuum, background, observer graph, section, selector, family row, PS
reduction, physical quotient, luminous half, named family, mass, energy scale,
threshold, domain, positivity, observable, or phenomenology. Both conjugate
ambient halves remain present. The fixed trace-`H_q` adverse horn and full
`d0+varpi` derivative collision remain untouched.

## Certificate

Run:

```text
sage -python \
  tests/channel-swings/joe_directed_cb5_h210_projected_rank_strata_probe.py
```

The certificate uses exact `QQ`, `GF(1009)`, and `GF(1013)` arithmetic. It
checks both ambient Weyl halves, the split and gamma-trace identities, the
normal forms above, the two independent rank counterexamples, coefficient
rank `40` for both projected constructions, simultaneous generic full rank,
kernel intersections, family exact-sequence dimensions, upstream Z
gamma-tracelessness, routing fences, and `Pi_4 != Pi_14`.

## Route consequence

The banked receiver remains a strong generic carrier-fit point, but projected
rank by itself is now exhausted as a discriminator: proper lower strata exist
inside the same full-`A` locus, and no projected rank supplies source
provenance. The next synthesis should carry the exact rank/kernel package and
ask whether `H210-FCORR` is an admitted conditional bridge alongside
`H210-ALIGN` and `H210-PSRED`. It should not spend another wave sampling rank
strata or attempt to manufacture an action, selector, PS reduction, or
external datum.
