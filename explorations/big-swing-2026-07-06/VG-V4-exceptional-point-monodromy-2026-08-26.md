---
title: "VG-V4 exceptional-point monodromy versus ghost parity"
status: active_research
doc_type: exploration_result
created: "2026-08-26"
grade: "EXACT FINITE TOY CERTIFICATE; NO GU TRANSFER OR PHYSICAL VERDICT"
target_claim: "M-S3 exceptional-point monodromy swaps the two low Pais-Uhlenbeck branches but is not the diagonal ghost-parity operator"
canon_verdict_change: none
scripts:
  - tests/big-swing/vg_v4_exceptional_point_monodromy.py
---

# VG-V4 exceptional-point monodromy versus ghost parity

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
result: M-S3 EP monodromy exchanges opposite-Krein branches but is not diagonal ghost parity
carrier: Pais-Uhlenbeck n=1 two-branch eigenspace LAYER=toy CHIRALITY=N/A
pairing: biorthogonal continuation plus Krein form ON=PU-n1-eigenspace
real_structure: complex delta-loop family with real positive basepoint
grading: measured opposite Krein-sign ghost grading
action_owner: comparator
target: endpoint branch transport versus ghost parity MAP-TYPE=evaluation
```

## Result

The specialist-panel hypothesis contained one strong observation and one weak
identification. The equal-frequency Pais-Uhlenbeck point is a second-order
exceptional point, and a loop around it does have `Z/2` branch monodromy. But
the induced transport is not Turok--Bateman ghost parity.

The certificate works in the existing fixed oscillator basis and uses the
analytic loop coordinate `delta = epsilon^2`. For truncations `N=10,12` and
radii `0.04,0.09`, it biorthogonally tracks the same two low branches over one
and two complete loops. All `38/38` checks pass:

- one loop returns the Hamiltonian to its starting matrix and swaps the two
  continuously tracked branches;
- two loops restore the branch identities;
- the two basepoint branches have opposite measured Krein signs;
- in that measured ghost grading, the one-loop swap anticommutes with parity;
- the endpoint transport matches the swap to residuals between
  `3.50e-14` and `8.31e-14`, while it fails the diagonal-parity comparison;
- pair conditioning remains finite, with the largest reported condition
  number `5.792`.

Thus both objects generate an abstract `Z/2`, but they act differently. Ghost
parity is diagonal and labels the two branches; exceptional-point monodromy is
off-diagonal and exchanges those labels. The useful corrected statement is:
encircling the exceptional point conjugates/exchanges the ghost labels. It
does not construct the ghost-parity operator.

## Scope and seams

This is an exact finite-dimensional toy result in the Pais-Uhlenbeck fixture.
It does not supply a GU source action, a field-theory transport, a physical
Hilbert-space selector, an S-matrix, a prediction or a canon verdict. No
standard-particle comparator is used in the inference, hence
`INTERNAL_STRUCTURAL_ONLY`.

The result is contrary to the literal M-S3 identification but preserves its
valuable loop question. Reproduction is the standalone script named in the
front matter. The principal transfer seam is unchanged: a GU-native action and
typed bridge would be required before any corresponding spectral monodromy
could be defined on the source-native carrier.

## Input-currency receipt

The local July/August Pais-Uhlenbeck artifacts and their current correction
registry were checked before execution. This certificate consumes only the
existing toy spectral fixture and makes no authorial-source attribution, so no
source correction changes the measured conclusion.
