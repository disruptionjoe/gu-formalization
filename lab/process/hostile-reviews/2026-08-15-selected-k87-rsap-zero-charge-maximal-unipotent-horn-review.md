---
title: "Hostile review: RSAP zero-charge maximal-unipotent horn"
status: complete
reviewed_artifact: explorations/conditional-build/selected-k87-rsap-zero-charge-maximal-unipotent-horn-2026-08-15.md
created: "2026-08-15"
verdict: PASS_CONSTRUCTED_SHARP_ZERO_HORN__FAILS_ZERO_NEIGHBORHOOD_COVERAGE__GENERAL_RSAP_OPEN
---

# Hostile review

## Linear sharpness disguised as a nonlinear model attack

The carrier is an actual smooth cotangent bundle with its canonical
Hamiltonian `G` action and moment map. Rank `49` follows from the exact
stabilizer at the zero covector, not from planting a tangent-space matrix.

## Wrong stabilizer attack

For split `D7`, the maximal unipotent nilradical has one real dimension for
each of the `42` positive roots. Therefore `G/N` is `49D`, and its zero
cotangent vector has stabilizer exactly `N`. The probe constructs all `91`
ambient matrices, all `42` nilradical matrices, and closes their brackets.

## Moment image overclaim attack

The artifact does not call the moment map surjective. Exact trace pairing
identifies `n^perp=b`, so the image is `Ad(G)b`. This contains a split-regular
submersive locus but not all real Cartan types.

## Singular witness attack

The excluded mixed witness is regular: its Cartan parameters are
`1,2,4,8,16,3i,5i`, and every `D7` root value is nonzero. It matches the
action-owned `(5,2)` type. Its imaginary vector eigenvalues cannot occur in a
real upper-triangular Borel or any real conjugate.

## “It contains zero, so it covers zero locally” attack

Containment of one target point is not neighborhood coverage. Every nonzero
rescaling of the mixed witness stays outside `Ad(G)b` and approaches zero.
Thus no target neighborhood of zero lies in the moment image.

## Universal no-go attack

The spectral obstruction kills the maximal-unipotent cotangent candidate. It
does not classify all `42D` subgroups, all Hamiltonian local normal forms, or
all smooth `98D` symplectic carriers. General RSAP existence stays open.

## Comparator relapse attack

Ordinary Higgs, family-index and net-chirality assumptions have no role in the
homogeneous-space stabilizer or moment-image calculation and remain routed
out.

## Verdict

Accept the constructed bound-saturating zero horn and its exact split-regular
submersion. Reject it as a zero-neighborhood RSAP chart because mixed regular
charges accumulate at zero outside its image. Preserve alternate homogeneous
and nonhomogeneous `98D` constructions as open.
