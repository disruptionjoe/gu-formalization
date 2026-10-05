---
title: "K1138 constraint-projector inertia certificate"
status: active_research
doc_type: exact_constraint_restriction_inertia_theorem
created: 2026-10-05
claim_ceiling: exact finite-dimensional restriction certificate; no action ownership or physical quotient
manifest: lab/process/k1138-constraint-projector-inertia-certificate.json
probe: tests/channel-swings/k1138_constraint_projector_inertia_certificate_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1138 constraint-projector inertia certificate

> **GU-COMPARATOR-ROUTING — scope before inference.** This theorem sharpens
> the acceptance test for a future source-native I1B constraint. Its projector
> is a certificate, not an action-derived physical reduction. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: exact inertia certificate for Hessian restriction to a constraint kernel
carrier: finite real Hessian carrier with full-row-rank constraint map LAYER=source-print CHIRALITY=N/A
pairing: auxiliary positive coordinate pairing used only to form the orthogonal projector ON=constraint-domain
real_structure: real symmetric Hessian and real constraint matrix
grading: unconstrained field directions versus constraint rows
action_owner: comparator -- certificate evaluates a separately owned map
target: K1135 nonnegative restricted inertia gate MAP-TYPE=evaluation
```

For full-row-rank `Q`, define

```text
P = I - Q* (Q Q*)^{-1} Q.
```

Then `P` is the orthogonal projector onto `ker Q`. If `Z` is any basis matrix
for that kernel, the constrained Hessian is exactly `Z* H Z`. Thus

```text
H|ker Q >= 0  iff  P H P >= 0 on im P  iff  Z* H Z >= 0.
```

Changing kernel basis from `Z` to `ZM` gives the congruent matrix
`M*(Z*HZ)M`, so inertia is invariant. The exact fixture uses
`H=diag(-1,2,3)` and `Q=(1,0,1)`. Its kernel Gram matrix is `diag(2,2)` even
though the unreduced Hessian has one negative direction. Quotienting a radical
after this restriction can remove only zero inertia, not repair a surviving
negative direction. This is a complete algebraic test of a supplied `Q`, not
its action ownership, propagation, common domain or cohomology. The producer
passes `12/12`; the hostile probe rejects `11/11` mutations.
