---
artifact_type: exploration
status: exploration
doc_type: construction_result
created: 2026-08-24
work_item: MP1-SEVEN-FLOOR-SUFFICIENCY
title: "MP1-S7: seven middle-form insertions do not suffice on the invariant carrier"
target_claim: "Internal target MP1-SEVEN-FLOOR-SUFFICIENCY: decide whether MP-1's necessary lower bound of seven middle-form insertions is also sufficient to gap one 896-dimensional one-form corner."
target_claim_verdict: "SEVEN-DOES-NOT-SUFFICE for the certified Spin(14)-equivariant middle-form channel: every finite linear sum stays in the unique trace-to-RS cross-block image and has rank at most 128. This narrows MP-1's generic witness; it is not a no-go for every insertion channel, nonlinear mechanism, action-owned background, or GU."
grade: "EXACT representation and linear algebra at complexified D7: RSC-1's 103/103 Klimyk/Racah certificate is re-run and SHA-pinned; the unique alternating middle-form image has trace-trace multiplicity 0, cross multiplicity 1 and RS-RS multiplicity 0; linearity therefore bounds every finite sum by rank 2*64=128. Exact prime-field compatible witnesses reach 128 individually and jointly, while the prior arbitrary seven-block model reaches 896 only by leaving the invariant image. No action, vacuum, scale, spectrum, count, reality map or physical quotient is constructed."
disposition: SEVEN_DOES_NOT_SUFFICE_ON_THE_UNIQUE_EQUIVARIANT_MIDDLE_FORM_IMAGE__ALL_FINITE_LINEAR_SUMS_REMAIN_TRACE_RS_CROSS_BLOCK_RANK_AT_MOST_128__PRIOR_GENERIC_896_WITNESS_IS_INADMISSIBLE__BLIND_DIAGONAL_ROWS_REMAIN_OPEN
canon_verdict_change: none
row_change: none
registry_change: none
steering_effect: unchanged
canonical_effect: none
scripts:
  - tests/channel-swings/mp1_seven_insertion_sufficiency_probe.py
depends_on:
  - lab/active-research/joe-directed/spectral-transport/mp1-composites-inherit-one-horn-never-both-2026-08-17.md
  - lab/active-research/joe-directed/rs-corner/rsc1-unique-channel-lives-on-the-gamma-trace-2026-08-17.md
  - tests/channel-swings/joe_directed_rsc1_unique_channel_lives_on_the_gamma_trace.py
  - lab/process/upgrade-program-register.yaml
  - lab/methods/source-native-comparator-routing.md
  - lab/methods/gu-base-categories.md
---

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

## Scope

This result binds one representation-theoretic question: can a finite linear
sum of the unique complexified-`D_7` middle-form alternating channel make the
declared one-form corner nondegenerate? It does not test whether an action
switches any insertion on, whether nonlinear terms provide other blocks, or
whether the source-native mechanism produces a physical mass or count.

```gu-typed-objects
result:         the sufficiency adjudication for finite linear sums of the
                unique middle-form alternating-form image: SEVEN-DOES-NOT-
                SUFFICE, and in fact no finite linear sum of that same image
                can exceed rank 128 on the 896-dimensional corner
carrier:        zeta_+ = V_14 tensor S_+ = S_-(64) direct-sum R^(+)(832),
                and its mirror; complexified D_7, identical on both
                SIGNATURE-AMBIENT horns LAYER=ambient
                CHIRALITY=S-FULL-DIRAC
pairing:        the Grassmann-live alternating form ON=zeta in Lambda^2(zeta), with
                trace-trace multiplicity 0, trace-RS multiplicity 1 and
                RS-RS multiplicity 0 for the live middle-form half
real_structure: SOURCE-SILENT and not consumed; the theorem is complexified
                representation arithmetic common to both real-form horns
grading:        Gamma_W/package class as carried by MP-1 and RSC-1; no
                grading transfer or selector is performed
action_owner:   repository-construction for the rank theorem and witnesses;
                source-action/SG4-bit-2 retains whether any insertion is on
target:         MP1-SEVEN-FLOOR-SUFFICIENCY MAP-TYPE=not-a-map
```

# MP1-S7 — the floor is not tight on the invariant image

## Preflight and route choice

The load-bearing objects were frozen before computation:

- `zeta = T direct-sum R`, with `dim T=64`, `dim R=832`;
- the alternating middle-form channel, not an arbitrary skew form;
- the unique equivariant image recorded by RSC-1;
- the maximum licensed conclusion: sufficiency or non-sufficiency for finite
  linear sums of this channel only.

The representation-theory, Layer-0 typing, exact-linear-algebra,
source/comparator-boundary, certificate-vacuity and hostile-overclaim lenses
all proposed routes. The selected route re-runs RSC-1's exact block
decomposition, then uses linearity of the unique image. A broad numerical
`896 x 896` search was rejected as dominated unless the exact image carried a
diagonal block or failed uniqueness. It did neither.

Input currency was checked against the correction registry. The consumed MP-1
and RSC-1 artifacts already carry the current CC-05 subtractive `2+1`, CC-06
VEV-conditional and CC-08 partner-obligation fences. No superseded physical
reading enters this rank question.

## Exact result

RSC-1's independent Klimyk and Racah/Brauer instruments give, on

`zeta = T(64) direct-sum R(832)`, 

the middle-form content of the alternating square as:

| block | multiplicity |
|---|---:|
| `Lambda^2(T)` | 0 |
| `T tensor R` | 1 |
| `Lambda^2(R)` | 0 |

Therefore every admissible form has block shape

`B_phi = [[0, A_phi], [-A_phi^T, 0]]`,

with `A_phi: R -> T`. Hence

`rank(B_phi) = 2 rank(A_phi) <= 2 dim(T) = 128`.

The equivariant map `phi -> B_phi` is linear. For any finite collection,

`sum_i B_phi_i = B_(sum_i phi_i)`,

so the sum remains in the same cross-block image and obeys the same rank-128
ceiling. Seven insertions leave at least `896-128=768` directions unpaired.
The argument does not merely show that a particular seven-tuple failed; it
shows that no finite linear sum in this one invariant channel can gap the
corner.

## Why the predecessor's 896 witness does not transfer

MP-1 correctly labeled its `768/896` ranks as generic/model-grade and said
invariant compatibility was not computed. Its seven rank-128 witnesses use
independent arbitrary skew-form supports. Seven disjoint 128-dimensional
blocks can indeed have rank 896, but such a direct sum necessarily introduces
support outside the one shared `T(64) | R(832)` cross block. It is not in the
unique middle-form equivariant image.

The certificate constructs seven exact full-row-rank `T <- R` maps with
distinct supports. Each associated skew form has rank 128. Their sum still has
map rank 64 and skew rank 128, exactly as the theorem requires. This is the
admissible replacement for the prior generic witness.

## Verdict and consequences

`SEVEN-DOES-NOT-SUFFICE` for the unique middle-form alternating channel. The
statement “seven is a floor” remains arithmetically necessary under the loose
per-form bound, but it is not tight and is not a useful finite sufficiency
threshold on the actual invariant image. The stronger carrier truth is the
common rank-128 ceiling for every finite linear sum.

This is not a no-go for every insertion channel. RSC-1 and DS-1 already name
the live alternatives: the `Lambda^1` and `Lambda^5` diagonal RS blocks (and
their Hodge-dual rows), nonlinear/action-owned terms, or structure outside the
declared middle-form image. Their exact invariant form ranks remain open. No
ledger row, source attribution, prediction, confirmation, claim, canon, paper,
agenda priority or public posture changes.

## Controls and hostile review

The live probe passes the following independent burdens:

- re-runs RSC-1 at `103/103`, with its script SHA pinned;
- pins the `64+832`, unique-cross, trace-zero and RS-zero facts;
- exercises seven exact compatible maps over a prime field;
- reproduces the arbitrary rank-896 witness and proves it has out-of-image
  support;
- catches targeted corruptions of the source SHA, dimensions, each block
  multiplicity, linearity, sum rank, admissibility classification and verdict.

Strongest attacks:

1. **“Rank subadditivity says seven can reach 896.”** Only for unrelated
   rank-128 forms. The equivariant forms share one 64-dimensional codomain and
   are closed under addition, so their sum never acquires seven codomains.
2. **“Multiplicity does not determine rank.”** Correct in general; here the
   conclusion uses only the zero diagonal multiplicities and block dimension.
   It does not claim a generic orbit rank beyond the universal ceiling.
3. **“This kills the gapping mechanism.”** It kills no source claim and no
   full mechanism. It closes one proposed sufficiency route and leaves the
   diagonal, nonlinear and action-owned routes explicit.
4. **“The correction erases MP-1.”** MP-1's parity/composition theorem remains
   untouched. Only its model-grade claim that the loose floor is tight is
   fenced by the exact successor.

## Postflight

The actual effect matches the intended one: one queued sufficiency question is
closed at exact carrier grade, one inadmissible model witness is fenced, and
the next executable scientific condition is sharper. The next gapping gate is
the `DS1-BLINDROW-FORM-RANK` census on the `Lambda^1/Lambda^5` diagonal blocks;
the source-silent reality map remains a separate fork and no convention is
selected here.

Reproduce:

```text
python3 tests/channel-swings/mp1_seven_insertion_sufficiency_probe.py
python3 tests/channel-swings/mp1_seven_insertion_sufficiency_probe.py --selftest
```
