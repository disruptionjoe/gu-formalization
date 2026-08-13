---
artifact_type: source_return
created: 2026-08-12
run_id: RUN-20260812-030756-gu-two-half-hermitian-witt-map
status: SOURCE_CONFIRMS_FULL_PARENT_TWO_HALF_EXPOSITION_AND_VARPI_ASSIGNMENT__SOURCE_SILENT_ON_HQ_Q_SELECTION_AND_PHYSICAL_BLOCK
---

# Source return: full unitary parent and two Weyl halves

## Question

Do the checked sources establish that the full `U(64,64)` connection is two
`U(32,32)` halves, and do they supply the Hermitian form or reduction that
makes that statement precise?

## Return

The source-claim register and the previously checked primary/expository
extracts support three distinct statements:

- `SC-GRP-01/SC-GRP-02` (`SOURCE-ASSERTS`): the authorial construction uses a
  full `U(64,64)` principal arena.
- Curt's iceberg exposition (`SOURCE-EXPOSITOR-STATES`): the two complex Weyl
  halves are each described as `C^(32,32)`.
- `SC-FER-03` (`SOURCE-ASSERTS`): components of the connection one-form
  `varpi` host gauge, Higgs-like, CKM and Yukawa functions.
- `SC-FER-05` (`SOURCE-DISPLAYS`): equation 12.20 carries two `2x16` terms per
  complex ambient half.

The checked material does **not** print `H_q=iB gamma(q)`, choose a normalized
non-null line, derive block `U(32,32)xU(32,32)` as the operative action parent,
or identify the equation-9.16 `+/-` labels with ambient `omega` chirality. The
fermionic extraction explicitly says those labels are displayed without a
definition of the plus/minus grading. It also does not identify a specific
diagonal or exchange block as the observed Higgs or Yukawa channel.

## Disposition

```text
SOURCE-CONFIRMS:
  full U(64,64) authorial arena;
  two C^(32,32) Weyl halves in Curt's exposition;
  varpi assignment to gauge/Higgs-like/CKM/Yukawa functions;
  two 2x16 terms per complex ambient half.

SOURCE-SILENT:
  H_q=iB gamma(q);
  selection or global ownership of q;
  operative full-versus-block action parent;
  equation-9.16 plus/minus equals omega;
  physical Higgs/Yukawa block identification.

REPO-DERIVES:
  exact conditional Witt compatibility between the full (64,64) form and
  two nondegenerate (32,32) Weyl-half restrictions after q is supplied.
```

The source therefore motivates the target but does not discharge the new
reduction datum or physical identification.
