---
artifact_type: exploration
status: exploration
doc_type: conditional_source_representation_bridge
created: 2026-08-16
work_item: CB-5-H210-C
channel: high_energy_two_plus_one_prediction
target_claim: SC-GEN-53
title: "CB-5 source/FQ bridge: the observed four-dimensional trace has a pointwise split-canonical lift into the equation-(12.22) F carrier, but H210 starts in Z and source provenance needs a separate adapter horn"
grade: "SOURCE-EXACT custody plus an exact pointwise trace-sector Clifford audit and semantic mutation certificate. CONDITIONAL on H210. The diagonal lift from a post-contraction four-dimensional trace into the F-shaped summand is proved relative to the declared orthogonal split; its full co-moving horizontal/normal naturality is not yet certified, and its identification with Weinstein's intended reveal mechanism is fenced by H210-FCORR. H210-ALIGN and H210-PSRED remain independent. This probe is not by itself a machine derivation of the full F/Q/Z branching or chirality allocation. No action, background, selector, family-row fit, reduction, physical quotient, external datum, mass, scale, threshold, or observable is constructed."
disposition: HORIZONTAL_TRACE_IS_NOT_EQ1222_F_BY_ITSELF__CANONICAL_CORRELATED_TRACE_PAIR_IS_EXACT__H210_Z_PROJECTION_TO_SOURCE_F_IS_ZERO__OBSERVATION_INDUCES_A_Z_TO_F_CARRIER_ADAPTER__SOURCE_REVEAL_READING_NEEDS_H210_FCORR__H210_ALIGN_REMAINS_INDEPENDENT
canon_verdict_change: none
steering_effect: "In CB-5, report F_J^tr as the horizontal Clifford-trace component. When comparing it with equation (12.22), use the correlated lift kappa_J(tau_J), including its synthesized normal trace partner. A nonzero lifted map passes carrier type only; source-imposter provenance still requires H210-ALIGN, and identifying the observation-induced Z-to-F map with Weinstein's intended pullback reveal requires the separate H210-FCORR horn."
depends_on:
  - lab/methods/source-native-comparator-routing.md
  - lab/sources/source-claim-register.yaml
  - lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md
  - explorations/draft-fqz-map-decider-2026-08-03.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/he4-path-reprioritization-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb3-h210-source-observation-functor-crosswalk-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb4-wave-h210-naturality-reprioritization-2026-08-16.md
  - lab/process/hostile-reviews/2026-08-16-joe-directed-cb4-h210-naturality-review.md
  - explorations/conditional-build/selected-k77-local-twistor-bach-detour-composition-gate-2026-08-14.md
scripts:
  - tests/channel-swings/joe_directed_cb5_h210_source_fq_bridge_probe.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.
>
> Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

# CB-5 H210 source/FQ bridge

## Outcome first

The load-bearing correction is sharper than “the trace is only F-shaped.”
There are three different objects:

```text
F_J^tr       = (1/4) j_4 Gamma_4 O_J T,
F_corr       = the correlated horizontal-plus-normal trace summand in
               ker Gamma_14 occurring in equation (12.22),
Z            = S(TX) tensor RS(N), containing the internal 144 partner.
```

`F_J^tr` is not, by itself, equation-(12.22) F. The latter is not a horizontal
trace block: it is the diagonal kernel of the sum of horizontal and normal
Clifford traces. If

```text
tau_J = Gamma_4 O_J T,
```

then the split Clifford algebra constructs, pointwise and canonically relative
to the declared orthogonal splitting,

```text
kappa_J(tau_J)
  = ( (1/4) j_4 tau_J, -(1/10) j_10~ tau_J )
  in ker Gamma_14.
```

Here `j_10~` includes the ordinary grading sign in the normal Clifford action.
The first component is exactly `F_J^tr`; the second is the uniquely normalized
normal trace partner. Thus the owned algebra can **construct** the correlated
F-shaped pair from the observed trace. It does not recover a normal covector
leg preserved by observation: literal pullback already consumed that leg.

This does not yet certify a full co-moving horizontal/normal natural
transformation: the normal complement, normal coframe, graded normal Clifford
injection, and both-half chirality correlation must also be transported.

The functor order then supplies the decisive boundary. The H210 port is
upstream in

```text
Z = S(TX) tensor RS(N),
```

so its canonical projection to the F summand in the equation-(12.22)
direct-sum branching is exactly zero. A nonzero `tau_J` therefore yields an
**observation-induced map from Z into the F carrier**, not evidence that the
H210 port already had F provenance upstairs.

This gives a clean three-level verdict:

1. `F_J^tr != 0` proves a nonzero four-dimensional trace component.
2. `kappa_J(tau_J) != 0` proves a typed, correlated F-carrier-valued adapter.
3. Calling that adapter Weinstein's intended “imposter revealed under
   pullback” still needs the independent conditional horn

   ```text
   H210-FCORR = the observation-induced correlated lift
                kappa_J Gamma_4 O_J T is the typed realization of the
                equation-(12.22) F reveal for the H210 route.
   ```

`H210-ALIGN` does not discharge this horn. `H210-ALIGN` identifies the selected
family-multiplicity quotient with imposter provenance; `H210-FCORR` identifies
the representation/functor adapter with the source's intended reveal. The
moving-PS cocycle remains the third independent horn `H210-PSRED`.

## 1. Primary-source custody

The source rows and primary extraction support only the following claims.

| source | exact owned content | boundary used here |
|---|---|---|
| `SC-GEN-03`; 2021 draft p.62, eq. (12.22), extraction section 5 | the underbrace “Imposter Third Generation” attaches to the third term `S(TX) tensor S(N)` and nothing else | F is the source-labeled referent; neither Q nor Z gets this label |
| `SC-GEN-05`; draft pp.62–63 and p.65, extraction sections 5–6 | the ambient RS remainder is said to reveal the effective imposter under pullback/decomposition | this is source language, not a supplied natural transformation between associated restriction and literal form pullback |
| `SC-GEN-06`; draft p.53, extraction section 3 | imposter-named rows occur in a table whose printed dimensions sum to 144, while the table host and star notation are unexplained | preserve the ambiguity; do not rename all of Z or the internal 144 as F |
| draft p.52, eq. (11.6), extraction section 2.2 | `F=128`, `Q=384`, `Z=1152` ungraded; Z contains `2 tensor 144` factors | fixes representation shapes and both ambient halves, not family provenance |
| `SC-PRE-52` | a roughly 144-complex-dimensional spin-one-half sector is predicted to combine with the observed third generation at Pati--Salam | the internal 144 is the partner, not the equation-(12.22) imposter referent |
| `SC-GEN-53`, `SC-GEN-57` | two-plus-one representation behavior should differ as energy rises while looking the same at low energy | no scale, observable, threshold, or switch is supplied |
| `SC-CHI-50/54`, `SC-CHI-51/53` | the total theory is non-chiral; effective chiral halves decouple at low curvature and reconnect in the proposed high-curvature regime | carry both conjugate halves; do not substitute a net-chirality index |

The F/Q/Z decider correctly identifies the **isomorphism class** of the third
summand as `S(TX) tensor S(N)`. This artifact refines its embedded realization:
inside `ker Gamma_14`, that spinor module is represented by a correlated pair
of trace-image vector-spinors. The refinement changes no source label.

## 2. Exact direct-sum RS branching

Let `H` and `V` have dimensions `h=4` and `v=10`, and write the restricted
ambient vector-spinor as `(psi_H,psi_V)`. With the grading sign absorbed into
the normal maps,

```text
Gamma_14(psi_H,psi_V) = Gamma_H psi_H + Gamma_V~ psi_V,
Gamma_H j_H = h I,
Gamma_V~ j_V~ = v I.
```

Decompose each vector-spinor factor into gamma-traceless and trace-image
parts. The kernel is

```text
ker Gamma_14 |_Spin(H)xSpin(V)
  = RS(H) tensor S(V)
    direct-sum S(H) tensor RS(V)
    direct-sum F_corr,

F_corr = { ((1/h)j_H s, -(1/v)j_V~ s) : s in S(H) tensor S(V) }.
```

The source names these three summands Q, Z, and F, respectively. Their
ungraded dimensions are `384`, `1152`, and `128`; per ambient half they are
`192`, `576`, and `64`, closing to the printed `832`.

The coefficients `1/4` and `-1/10` are not conventions chosen to fit a name.
They are forced by

```text
Gamma_H ((1/4)j_4 s) = s,
Gamma_V~ (-(1/10)j_10~ s) = -s.
```

A horizontal trace component with zero normal partner has ambient gamma trace
`s` and is outside `ker Gamma_14` whenever `s != 0`. Dimension and the word
“trace” therefore cannot identify `F_J^tr` alone with source F.

## 3. Functor order: why the naive source bridge fails

The owned operations occur in this order:

```text
ambient RS
  -- associated restriction and Q/Z/F direct-sum branching --> Q + Z + F_corr
  -- literal one-form contraction O_J --> H* tensor s^*S
  -- four-dimensional Clifford split --> F_J^tr + Q_J^RS.
```

Projection to `F_corr` belongs to the first stage. `F_J^tr` belongs to the
third. They do not commute on the H210 input.

The H210 tensor has a gamma-traceless normal vector leg, hence is Z-shaped:

```text
T_H210 in S(H) tensor RS(V),
P_Fcorr T_H210 = 0.
```

For a tilted graph, contraction can nevertheless produce

```text
tau_J = Gamma_H O_J T_H210 != 0.
```

The exact probe includes a normal gamma-traceless vector-spinor whose direct
F projection is zero but whose tilted contraction has nonzero horizontal
trace. Therefore

```text
kappa_J tau_J != P_Fcorr T_H210.
```

The left side is a newly composed `Z -> F_corr` adapter; the right side is the
source direct-sum projection and vanishes on this port. Equation (12.22) plus
literal pullback is consequently enough to construct a **carrier-type map**,
but not enough to identify the map with source provenance or with the source's
intended reveal mechanism.

The synthesized normal trace partner is also not the original H210 normal
leg. The former lies in `im(j_V~)`; the latter lies in `ker(Gamma_V~)`. Their
intersection is zero in the Clifford splitting. Observation has not restored
a free observed 144.

## 4. What each named object and horn owns

| item | exact job | cannot supply |
|---|---|---|
| `F_J^tr` | horizontal trace-image component of `O_JT` | ambient gamma-traceless F pair; provenance; family identity |
| `kappa_J tau_J` | pointwise split-canonical correlated pair in the equation-(12.22) F carrier | full co-moving H/V naturality; equality with upstream F projection; source selection; physical observation |
| `Q_J^RS` | 4D gamma-traceless component after contraction | ambient Q identity; Z partner; an independent family count |
| Z/internal 144 | upstream normal-RS partner sector from eq. (11.6) and `SC-PRE-52` | source F label; the correlated normal trace partner |
| `H210-ALIGN` | identify `M_3/ker(r)` with the F/imposter provenance line | construct the F correlated pair or compare the two pullback functors |
| `H210-FCORR` | declare the observation-induced correlated lift to be the source-intended H210 realization of the F reveal | family alignment or moving PS reduction |
| `H210-PSRED` | type the moving PS reduction/normalizer cocycle | F provenance or the source functor bridge |

The three horns are logically independent. In particular, setting
`H210-ALIGN=true` while omitting the normal correlated partner remains a type
error, and constructing `kappa_J` does not source-select the family row.

## 5. Both halves and referent discipline

The calculation is signature-independent at this representation layer and
must be applied to both ambient chirality halves. Per half, F has dimension
`64`; ungraded F has dimension `128`. A single-half result is not a proof of
Weinstein's non-chiral parent mechanism.

Four numerical coincidences remain non-bridges:

- `144-16=128` does not identify the internal-144 residual with F;
- rank `16` of the H210 family row does not name a family;
- simultaneous nonzero ranks of `F_J^tr` and `Q_J^RS` do not add to two
  families; and
- the p.53 imposter-named rows do not rename the whole Z sector.

## 6. Exact kill/survive outcomes

| exact outcome | scoped consequence | what survives |
|---|---|---|
| `tau_J=0` on every intrinsic nonzero H210 stratum | kill H210 as a carrier explanation of the source F appearance | the upstream Z/internal-144 port, source F label, and `SC-PRE-52` remain |
| `tau_J!=0`, but the correlated lift or its co-moving naturality fails | a nonzero local 4D trace survives, but no intrinsic equation-(12.22) F-carrier bridge is earned | H210 observation rank and Z port may remain |
| `tau_J!=0` and `kappa_J tau_J` is co-moving | carrier-type bridge survives: observation induces a nonzero `Z -> F_corr` map | provenance, selection, physical quotient, and energy interpretation remain conditional |
| `P_Fcorr T_H210=0` | kills “H210 was already the source F upstairs” | an observation-induced adapter remains possible and is the only live F route here |
| `H210-ALIGN` absent | no selected family quotient may be called the imposter line | carrier type can still pass |
| `H210-FCORR` absent | do not call the constructed adapter Weinstein's intended reveal mechanism | the exact algebraic `Z -> F_corr` adapter remains |
| either conjugate half deleted | kills compatibility with the source's non-chiral parent in this construction | no standard net-chirality replacement is licensed |

Even the strongest survive row does not move `SC-GEN-53`: the source still
supplies no scale, observable, threshold, physical quotient, or regime switch.

## 7. Certificate and semantic plants

Run:

```text
python3 tests/channel-swings/joe_directed_cb5_h210_source_fq_bridge_probe.py --selftest
```

The exact rational probe checks the direct-sum dimensions, the correlated
kernel embedding and forced coefficients, a horizontal-only counterexample,
the Z-projection/tilted-observation functor-order counterexample, both halves,
the family kernel, source-row custody, and all horn separations. Semantic
plants must fire for horizontal-F promotion, Z/F collapse, dimension-only
identification, recovered-normal-leg language, promoted `H210-ALIGN`, omitted
`H210-FCORR`, collapsed horn roles, deleted conjugate half, and additive family
counting.

## Strict claim ceiling

This artifact proves an exact pointwise representation-level diagonal lift
from the post-contraction four-dimensional trace into the correlated F
carrier of the
restricted ambient RS module. It also proves that the current H210 port starts
in Z and has zero canonical F projection before observation. It does not prove
full co-moving naturality of the complete horizontal/normal lift, that the
source or action selects H210, that the observation-induced adapter is
Weinstein's intended pullback reveal, that a family row has imposter
provenance, that PS descends, or that any physical quotient keeps the map. It
does not derive a luminous sector, mass, scale, threshold, domain, positivity,
observable, phenomenology, or a free observed 144. Canon and public posture do
not move.
