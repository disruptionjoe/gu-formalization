---
title: "Exact D7 form-spinor and D5 branching dictionary"
status: active_research
doc_type: construction_result
created: "2026-08-26"
grade: "EXACT COMPLEXIFIED REPRESENTATION-THEORY CERTIFICATE; NO REAL-FORM OR PHYSICAL-SECTOR SELECTION"
target_claim: "M-M4 cached exterior-form/spinor branching, duality and compact reality typing"
canon_verdict_change: none
cache: lab/process/d7-form-spinor-branching-dictionary.json
scripts:
  - tests/generation-sector/d7_form_spinor_branching_dictionary_sage.py
---

# Exact D7 form-spinor and D5 branching dictionary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

`GU-COMPARATOR-ROUTING-CLASSIFICATION: INTERNAL_STRUCTURAL_ONLY`

```gu-typed-objects
result: M-M4 exact D7 form-spinor and D5 branching dictionary
carrier: complexified Spin(14) and Spin(10) representation-ring model LAYER=toy CHIRALITY=S-HALF-OPPOSITE
pairing: Weyl-character inner product ON=complexified-representation-ring
real_structure: compact-representation Frobenius-Schur type per irreducible; no GU real form selected
grading: exterior degree k and D7 half-spin chirality
action_owner: repository-construction
target: irreducible decomposition cache MAP-TYPE=evaluation
```

## Result

M-M4 is executed at its algebraic claim ceiling. One Sage certificate now
reconstructs a canonical JSON dictionary for
`Lambda^k(V_14) tensor S+/-`, for every degree `k=0,...,7`; Hodge partners
cover degrees `14-k`. It also reconstructs the D5 controls used by the
Pati--Salam-facing representation questions.

For each D7 chirality the constituent counts rise from one at degree zero to
eight at the midpoint. All multiplicities are one. The exact dimensions close
to `64 * binomial(14,k)` in every case:

| k | total dimension | irreducible dimensions for either chirality |
|---:|---:|---|
| 0 | 64 | 64 |
| 1 | 896 | 64 + 832 |
| 2 | 5,824 | 64 + 832 + 4,928 |
| 3 | 23,296 | 64 + 832 + 4,928 + 17,472 |
| 4 | 64,064 | previous tower + 40,768 |
| 5 | 128,128 | previous tower + 64,064 |
| 6 | 192,192 | previous tower + a second 64,064 |
| 7 | 219,648 | degree-six tower + 27,456 |

The committed cache records exact Dynkin labels, multiplicities, dimensions,
dual Dynkin labels and Frobenius--Schur type. In odd D rank, non-self-dual
irreducibles are complex (`FS=0`) and self-dual irreducibles are real
(`FS=+1`); the certificate independently checks the vector and half-spin
controls with Sage's native indicator.

The D5 controls reproduce:

- `10 tensor 16+ = 16- + 144+` and its opposite-chirality dual;
- `Sym^2(16+) = 10 + 126+` and `Lambda^2(16+) = 120`;
- `Lambda^5(10) = 126+ + 126-`;
- the two exact `16+ tensor 144+/-` dictionaries, including dual and compact
  reality fields.

Fresh reconstruction equals the committed cache byte-for-object and the
certificate passes `60/60` checks. This consolidates the algebraic inputs
behind `FC-IRR`, `FC-HW`, `FC-MULT`, `OQ1` and `OQ-CG-2`; it does not promote
their source, real-form or physical conclusions.

## Claim ceiling and seams

The cache is a complexified compact representation-ring result. It does not
choose the GU ambient signature, the relevant real form, an action owner, a
Higgs/VEV mechanism, a source-native selector, an ordinary-family count, net
chirality or a physical sector. The D5 identities are controls inside the
same algebraic build, not a bridge from conventional SO(10) particle physics
to Weinstein's source-native mechanism. That is why the artifact is classified
`INTERNAL_STRUCTURAL_ONLY`.

The exact remaining seam is semantic: a future consumer must supply the typed
real-form and action bridge appropriate to its claim before using these
complexified branchings physically. Reproduction requires Sage and the single
script named above; `--dump` emits the canonical cache.

## Input-currency receipt

The live correction registry and the M-M4 register row were checked before
construction. No authorial source semantics are consumed or altered. The
dictionary settles only the exact representation-theory build promised by the
row, leaving source attribution and physical interpretation unchanged.
