---
title: "K472 — K77 Effective Properness Compiler"
status: working_draft_verified
status_axis: operational_state
doc_type: conditional_build
date: "2026-09-25"
classification: INTERNAL_STRUCTURAL_ONLY
direction: observed_to_native
---

# K472 — K77 effective properness compiler

> **GU-COMPARATOR-ROUTING — scope before inference.** This finite compiler is
> not an action selection or physical cohomology result. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

## Decision contract

A future K77 packet must supply complete action-owned coefficients, typed
nilpotent squares, closed-domain preservation, a base deformation retract and
invertible perturbation factors. K471 then transfers the packet to an exact
effective homology complex. Properness is accepted only when that effective
complex is acyclic.

The positive control has effective differential `17/18`, determinant `17/12`
and zero cohomology. Setting `t=1/18` instead makes the effective differential
and determinant zero and leaves cohomology dimensions `(1,1)`. Even the small
packet `a=0,b=c=1/10,t=1/100` has zero effective differential, proving that
coefficient smallness alone does not remove base homology.

## Boundary

No action-owned packet exists. The result is a fail-closed finite certificate
interface, not native K77 properness or physical BV cohomology.

## Reproduction

Run `python3 tests/channel-swings/k472_k77_effective_properness_compiler_probe.py`.
