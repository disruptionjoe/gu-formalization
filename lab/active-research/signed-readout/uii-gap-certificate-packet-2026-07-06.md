---
title: "UII Gap Certificate Packet For Signed-Readout OC1/OC2"
date: 2026-07-06
status: active_research
doc_type: certificate_packet
parent:
  - lab/active-research/signed-readout/theorem-statement-v1-2026-06-23.md
  - explorations/internal-paths-2026-07-03/signed-readout-oc1-oc2.md
validator: tests/function-space-ext/uii_gap_certificate_validator.py
verdict: certificate_interface_only
---

# UII Gap Certificate Packet For Signed-Readout OC1/OC2

## Scope

This packet turns the non-compact signed-readout fence into a concrete certificate interface.
It does not discharge OC1 or OC2 for the actual GU operator, does not change a verdict, and does
not touch canon. It records the exact thing a future target-operator run must supply:

```text
Uniform Invertibility at Infinity (UII):
there are a compact K and delta > 0 such that
||D_t u|| >= delta ||u||
for all u supported outside K, uniformly along the deformation t.
```

The internal-path reduction already states the analytic situation: OC1/OC2 reduce to this
single spectral-gap estimate, with the quaternionic OC2 increment reduced to the algebraic
condition `[D_t, J] = 0`.

## Certificate Interface

A candidate UII certificate must name:

| field | required content |
|---|---|
| target operator | the actual non-compact operator family `D_t`, not a proxy for the desired index |
| model at infinity | the asymptotic operator `D_infty(t)` or equivalent end operator |
| compact cutoff | the compact region `K` outside which the model controls the operator |
| lower bound | a uniform `delta > 0` for every allowed `t` |
| continuity | why the deformation stays in the same self-adjoint Fredholm component |
| OC2 side gate | proof or certificate that `[D_t, J] = 0`, if the KSp/H-linear claim is invoked |

The finite validator in `tests/function-space-ext/uii_gap_certificate_validator.py` checks the
matrix-level shape of such a certificate:

1. the asymptotic spectra have a positive uniform gap,
2. the bounded transform has the predicted gap `delta / sqrt(1 + delta^2)`,
3. the quaternionic commutator residual is small for the OC2 side gate,
4. a zero-gap control fails,
5. a J-breaking control remains spectrally gapped but fails OC2.

## Honest Boundary

Passing the validator on a toy or finite asymptotic model is not a proof for `Y^14`. It is only a
regression guard for the certificate shape. The real upgrade requires identifying the actual
`D_infty` of the target non-compact operator and proving the lower bound analytically or with a
certificate whose hypotheses imply the analytic estimate.

This packet therefore changes the next step from a vague "prove Fredholmness" instruction into a
specific target:

```text
Build the actual asymptotic operator and prove the UII lower bound.
```

## Failure Conditions

- If `0` lies in the essential spectrum at infinity, OC1 fails: the bounded transform is not in
  the Fredholm locus and the integer readout is not protected.
- If the lower bound is not uniform in `t`, the deformation can cross a gap-closing point and the
  index may jump.
- If `[D_t, J] != 0`, the OC2/H-linear lift fails even when OC1/Fredholmness holds.
- If the certificate uses a proxy whose asymptotic operator is not the actual target operator,
  it is evidence about the proxy only.

## Current Result

The validator passes on a constructed uniformly gapped H-linear asymptotic family and rejects
both controls:

```text
python tests/function-space-ext/uii_gap_certificate_validator.py
```

This is a frontstage gate for future signed-readout non-compact work, not a canon promotion and
not a generation-count result.
