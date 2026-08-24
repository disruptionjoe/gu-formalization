---
artifact_type: exploration
status: exploration
doc_type: construction_result
created: 2026-08-24
work_item: DS1-BLINDROW-FORM-RANK
title: "DS1-BR: the blind rows admit full-rank invariant forms"
target_claim: "Internal target C-DS1-GAP(blind): compute the invariant alternating-form ranks on the 896-dimensional one-form corner for the Lambda1/Lambda5 rows and their Hodge-dual Lambda13/Lambda9 directions."
target_claim_verdict: "BLIND-ROWS-ADMIT-FULL-RANK-FORMS at complexified representation/form grade: the trace, cross and RS channel ranks are 64, 128 and 832, and one shared generic Lambda1 or Lambda5 direction with diagonal channels included yields rank 896. This closes DS1's missing form-rank census but is not a physical mass-gap certificate: the real adjoint, action coefficient, selected direction, kinetic operator, domain and spectrum remain unbuilt."
grade: "EXACT complexified D7 representation and finite-field linear algebra. Highest-weight kernels have dimensions 3 for Lambda1 and 4 for Lambda5, matching RSC1's trace/cross/RS multiplicities 1/1/1 and 1/1/2. The gamma-trace projector splits every form exactly. One common 70-orbit insertion direction gives pure-channel ranks 64/128/832 (and a second 832 RS channel for Lambda5) and combined rank 896 over each of the independent primes 1000003 and 1000033. Nonzero determinant modulo a prime proves the determinant polynomial is nonzero over Q/C. No real structure, action, vacuum, selector, mass, spectrum, count or physical quotient is constructed."
disposition: BLIND_ROWS_ADMIT_FULL_RANK_INVARIANT_ALTERNATING_FORMS_AT_COMPLEXIFIED_KINEMATIC_GRADE__O2_RANK_128_CEILING_IS_PURE_CROSS_ONLY__REAL_ACTION_AND_PHYSICAL_GAP_REMAIN_OPEN
canon_verdict_change: none
row_change: none
registry_change: none
steering_effect: unchanged
canonical_effect: none
scripts:
  - tests/channel-swings/ds1_blindrow_form_rank_probe.py
depends_on:
  - lab/active-research/joe-directed/grading-bridge/ds1-the-stock-sits-at-the-pole-and-waits-on-the-reality-map-2026-08-17.md
  - lab/active-research/joe-directed/rs-corner/rsc1-unique-channel-lives-on-the-gamma-trace-2026-08-17.md
  - explorations/generation-sector/mp1-seven-insertion-sufficiency-2026-08-24.md
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

This result binds the complexified invariant alternating-form question on the
declared one-form corner. It decides whether DS1's “blind” `Lambda1/Lambda5`
rows retain the pure-cross rank ceiling that killed middle-form sufficiency.
It does not decide whether a source-native action selects or realizes one of
the nondegenerate forms.

```gu-typed-objects
result:         the DS1 blind-row invariant-form census: BLIND-ROWS-ADMIT-
                FULL-RANK-FORMS at complexified representation/form grade
carrier:        zeta_+ = V_14 tensor S_+ = T(64) direct-sum R^(+)(832),
                and its mirror; complexified D_7 common to both
                SIGNATURE-AMBIENT horns LAYER=ambient
                CHIRALITY=S-FULL-DIRAC
pairing:        Grassmann-live alternating forms ON=zeta in Lambda^2(zeta),
                split into gamma-trace, trace-RS and RS-RS channels
real_structure: SOURCE-SILENT and not consumed; C-DS1-REALITY remains open
grading:        Gamma_W/package class from DS1; no grading transfer or
                physical selector is performed
action_owner:   repository-construction for the rank theorem and witnesses;
                source-action retains coefficients and selected directions
target:         C-DS1-GAP(blind) MAP-TYPE=not-a-map
```

# DS1-BR — the diagonal channels remove the pure-cross ceiling

## Preflight and route choice

The load-bearing objects were fixed before computation:

- `zeta = V_14 tensor S_+ = T(64) direct-sum R(832)`;
- the alternating invariant images of `Lambda1` and `Lambda5`, not arbitrary
  skew matrices;
- RSC1's exact block multiplicities; and
- the maximum licensed conclusion: existence and genericity of nondegenerate
  complexified forms, not a real action-owned physical gap.

Representation-theory, Layer-0 typing, exact Clifford/linear-algebra,
source/comparator-boundary, certificate-vacuity and hostile-overclaim lenses
were applied. Three routes were compared. Inferring rank from multiplicity was
rejected because multiplicity locates channels but does not determine their
rank. A floating `896 x 896` census was rejected as a final certificate. The
selected route constructs highest-weight intertwiners exactly, splits them by
the gamma-trace projector, and evaluates one common generic insertion direction
over two finite fields.

The switch condition was failure to reproduce RSC1's block multiplicities,
failure of the exact projector split, or disagreement between primes. None
fired.

## Exact construction

Use the Fock model `S_+ = Lambda^even U` for the complex `D_7` half-spinor and
`V = U direct-sum U*`. The Chevalley raising operators act on
`zeta = V tensor S_+` and hence on `Lambda^2(zeta)`. Solving the highest-weight
equations gives:

| insertion | highest-weight variables | kernel dimension | RSC1 block split |
|---|---:|---:|---|
| `Lambda1` | 1104 | 3 | trace 1, cross 1, RS 1 |
| `Lambda5` | 141 | 4 | trace 1, cross 1, RS 2 |

The Clifford contraction `C: V tensor S_+ -> S_-` and its adjoint algebraic
injection `J: S_- -> V tensor S_+` obey `C J = 7 I`. Thus
`Q = J C / 7` is the exact gamma-trace projector and `1-Q` the Rarita--
Schwinger projector. Every computed alternating form splits with zero residual
as

`Q B Q^T + Q B (1-Q)^T + (1-Q) B Q^T + (1-Q) B (1-Q)^T`.

This recovers the multiplicities independently rather than taking their labels
on trust.

## Rank census

For each insertion module, one common direction is built as the same linear
combination of 70 lower-unipotent orbit points in every channel. Channel
coefficients are then combined only after that common direction is fixed. All
ranks are exact modular Gaussian-elimination ranks and agree over both
`p=1,000,003` and `p=1,000,033`:

| insertion | trace block | cross block | RS block(s) | combined form |
|---|---:|---:|---:|---:|
| `Lambda1` | 64 | 128 | 832 | **896** |
| `Lambda5` | 64 | 128 | 832, 832 | **896** |

The same result transfers at invariant-module grade to the Hodge-dual rows
`Lambda13 ~= Lambda1` and `Lambda9 ~= Lambda5`. Their operator directions are
still distinct, and DS1's K-parity flip under the ambient volume word remains
binding.

Because the combined determinant is nonzero modulo two good primes, the
integer/rational determinant polynomial is not identically zero. Therefore a
nondegenerate form exists over `Q` and `C`, and nondegeneracy is Zariski-open:
the full rank is generic inside the certified combined invariant family. This
is stronger than a random numerical witness and weaker than a real physical
mass construction, exactly as required.

## Verdict and consequences

`BLIND-ROWS-ADMIT-FULL-RANK-FORMS` at complexified representation/form grade.
RSC1's rank-128 ceiling is a theorem about pure trace--RS cross-block shapes.
It does not extend to the all-three-block `Lambda1/Lambda5` rows. Their
diagonal trace and RS channels can compose with the cross channel to give a
nondegenerate alternating form on all 896 directions from one generic
insertion direction.

This closes only `C-DS1-GAP(blind)`. It is not a physical mass-gap certificate.
The result does not supply:

- the global Hodge/Krein/reality adjoint (`C-DS1-REALITY`);
- action-owned coefficients or the direction selected by a vacuum
  (`C-DS1-COMPONENT`);
- the self-adjoint realization of negative-square components;
- a kinetic operator, Fredholm domain, both-sides wall profile or spectrum; or
- a source-native action, physical quotient, observed mass or count.

The exact next scientific gate is now the common reality-map owner. At form
grade the blind rows are no longer the gapping obstruction; at physical grade
their admissibility is still undefined until the real adjoint and action make
the form operative.

## Hostile review

**Strongest overclaim.** “Full rank 896” can be misread as a massive physical
spectrum. It is only the rank of a complexified alternating form. No kinetic
operator, real self-adjointness, action coefficient, vacuum selection or pole
spectrum is present.

**Strongest contrary construction.** The middle-form channel remains pure
cross and rank at most 128 under every finite linear sum. The new result does
not weaken MP1-S7; it proves that a different invariant module with diagonal
channels behaves differently.

**Weakest reproducibility seam.** The highest-weight basis and orbit witness
are modular constructions. The seam is bounded by two independent primes, the
exact `CJ=7I` projector identity, zero split residuals, reproduction of RSC1's
`1/1/1` and `1/1/2` multiplicities, and a baseline-first mutation harness.

## Reproduction

```bash
python3 tests/channel-swings/ds1_blindrow_form_rank_probe.py
python3 tests/channel-swings/ds1_blindrow_form_rank_probe.py --selftest
```

Expected live result: `DS1-BR: 28/28 checks pass`.

Expected hostile result: `SELFTEST: 9/9 targeted mutations caught`.
