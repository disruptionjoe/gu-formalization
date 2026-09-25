---
title: "K468 — K77 Perturbation Contraction Certificate"
status: working_draft_verified
status_axis: operational_state
doc_type: conditional_build
date: "2026-09-25"
classification: INTERNAL_STRUCTURAL_ONLY
direction: observed_to_native
---

# K468 — K77 perturbation contraction certificate

> **GU-COMPARATOR-ROUTING — scope before inference.** This abstract complex
> theorem is not an action selection or a physical cohomology result. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

## Theorem

Let `dh+hd=I`, `h^2=0`, and let `D=d+delta` be a differential. If the relevant
Neumann factor is strictly contractive, for example `||h delta||<1`, then

`h_delta = h(1+delta h)^(-1) = (1+h delta)^(-1)h`

satisfies `D h_delta+h_delta D=I`. The perturbed complex is acyclic. A future
K77 use must additionally prove coefficient completeness, typed squares,
nilpotence and closed-domain preservation required by K464.

The exact two-term control starts from `d=I` and
`delta=diag(1/2,-1/3)`. Its adapted contraction is
`diag(2/3,3/2)`. The strict-boundary control `delta=-I` has norm one,
singular perturbed differential and cohomology dimensions `(2,2)`, so it is
rejected.

## Boundary

No action-owned coefficient packet exists, no native K77 complex is selected,
and no physical BV cohomology or source/ledger/canon/public claim follows.

## Reproduction

Run `python3 tests/channel-swings/k468_k77_perturbation_contraction_certificate_probe.py`.
