---
title: "K302 Order-Seven Split-Weighted Peano Jet"
document_role: active_research
operational_state: internal_structural_result
date: "2026-09-22"
claim_ceiling: "Uniform Peano-weighted terminal split jet through y-derivative order two; complete coherent norms and radial composition remain open."
manifest: lab/process/k302-order-seven-split-weighted-peano-jet.json
producer: tests/channel-swings/k302_order_seven_split_weighted_peano_jet.py
probe: tests/channel-swings/k302_order_seven_split_weighted_peano_jet_probe.py
target_claim: INTERNAL_TARGET:K152_COEFFICIENT_COMPLETE_BASE_ACTION_COLUMN
target_claim_verdict: TERMINAL_SPLIT_FACE_WEIGHTED_JET_FINITE__SIX_COMPLETE_NORMS_OPEN
canon_verdict_change: none
---

# K302 Order-Seven Split-Weighted Peano Jet

## GU-COMPARATOR-ROUTING

This is an `INTERNAL_STRUCTURAL_ONLY` result about the repository-supplied
conditional construction. It moves no source, physics-ledger, canon, paper, or
public-posture claim.

```gu-typed-objects
result: analytic Peano-weighted terminal split Bessel jet through derivative order two
carrier: all 24 K288 companion determinants with the terminal (8,8) entry retained LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive Hilbert Gram pairing before coherent signed composition PAIRING-TYPE=hilbert
real_structure: CAR adjoint, momentum reflection, and real Bessel K1 kernel
grading: order seven; y is the last K299 tensor-Peano axis
action_owner: repository construction from K139/K156/K179; no source-selected action or physical state is supplied
target: prove terminal native split-face integrability for the K299 second-derivative route MAP-TYPE=intertwiner
```

## Weighted jet

Put `a=1-u3`, `b=1-z3`, and `z=y*a+(1-y)*b`. With K299's exact Peano
kernel `K(y)=min(y,1-y)^2/2`, standard integer-order Bessel bounds give

```text
B0(x) < 1/x,
B1(x) < 1/4 + 2/x,
B2(x) < 3*x/8 + 6/x,
```

where `Bm` integrates `K(y)` times the absolute `m`th `y` derivative of
`2*K1(x*z)` over the complete `(y,a,b)` cube. The key exact split integrals
are

```text
I0(y) = -log(y)/(1-y) - log(1-y)/y,
K(y) J2(y) -> 1/2 at y=0,1,
K(1/2) J2(1/2) = 4*log(2)-2 < 4/5.
```

Every other companion entry adds nonnegative cumulative-time support, so the
terminal `(8,8)` entry is the worst case. The bound therefore covers all 24
occurrences and repairs the split-face gap in K300 without introducing an
artificial positive floor.

## Boundary

K302 proves only the terminal split-face weighted jet. It does not reinstate
K290's pointwise fourth-order bank or the K291/K293 numerical remainders. The
next gate is still an enclosure of the six complete coherent K299 directional
Peano norms, including all determinants and product rules, followed by their
`q,x` scaling before any K294 gamma join.
