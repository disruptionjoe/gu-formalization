---
title: "K471 — K77 Effective Homology Transfer"
status: working_draft_verified
status_axis: operational_state
doc_type: conditional_build
date: "2026-09-25"
classification: INTERNAL_STRUCTURAL_ONLY
direction: observed_to_native
---

# K471 — K77 effective homology transfer

> **GU-COMPARATOR-ROUTING — scope before inference.** This abstract complex
> theorem is not an action selection or physical cohomology result. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

## Theorem

Start with a deformation retract `dh+hd=I-ip`, with
`ph=hi=h^2=0`. For a typed perturbation `D=d+delta` satisfying `D^2=0`, if
`1+delta h` and `1+h delta` are invertible, the effective differential is

`d_H'=p(1+delta h)^(-1)delta i`.

The standard adapted inclusion, projection and homotopy give a deformation
retract from the perturbed complex to this effective homology complex. This
extends K468 beyond the acyclic-base special case.

For the exact two-term Schur control with
`a=1/2,b=1/3,c=1/4,t=1`, the contractible pivot is `3/2`, the effective
differential is `17/18`, the adapted maps are rational, and both retract
identities hold exactly.

## Boundary

Smallness is sufficient for invertibility but not necessary. Native use still
requires complete action-owned coefficients, typed nilpotence and closed-domain
preservation. No K77 action or physical cohomology is selected.

## Reproduction

Run `python3 tests/channel-swings/k471_k77_effective_homology_transfer_probe.py`.
