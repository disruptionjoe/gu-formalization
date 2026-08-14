---
title: "Conditional Physics Ledger v0.254"
status: research
doc_type: ledger-summary
created: 2026-08-14
---

# Conditional Physics Ledger v0.254

Ledger v0.254 preserves all 82 verdicts and records four distance-only
migrations on `RA-G2`, `LT-SM3`, `AC-F1` and `AC-G1a`.  The v0.253 twistor
carrier result and its `LT-SM8` migration remain unchanged.

The action-owned selected endpoint has a nonzero `so(7,7)^*` charge `mu` with
30 nonzero labelled components.  Exact rational and independent modular
calculation give its Kirillov form

```text
K_mu(X,Y)=mu([X,Y])
```

rank 84.  Its coadjoint stabilizer is seven-dimensional and abelian, so this
is a regular endpoint charge at the tested fixture.

This closes two structural questions.

First, the 90-dimensional hyperplane `ker(mu)` is not a Lie algebra: the
restriction of `K_mu` to it still has rank 84.  Restricting boundary gauge
parameters only by zero individual charge is therefore not a consistent
boundary-gauge rule.

Second, the coadjoint orbit `O_{-mu}` is the minimal homogeneous Hamiltonian
carrier capable of cancelling the present endpoint charge.  It has symplectic
dimension 84, its KKS inclusion moment map cancels `mu` componentwise, and
equivariance proves that any Hamiltonian carrier containing a point mapped to
`-mu` has a group orbit of at least that dimension.

This is a located conditional route, not a source-derived edge theory.  Seven
transverse invariant values distinguish nearby regular coadjoint orbits.  A
single fixed orbit can work globally only if action-owned boundary variations
leave those values fixed.  Otherwise GU needs a larger group/cotangent edge
carrier or must retain the charged-boundary-symmetry horn.  No boundary action,
global edge bundle, analytic domain or physical cohomology is yet constructed.

The non-chiral source target remains explicit.  Nothing in this migration
claims fundamental net chirality or a generation count; the physical burden
remains effective luminous/dark separation in positive reduced cohomology.

```text
Ledger v0.254 — 82/82 target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue: 84 continuous + >=19 function-valued + 9 discrete forks
Tightness: T4x1 T3x3 T2x1 · scoped quotients: 5
Headline delta: none
Frontier closed: naive charge-kernel restriction; minimal fixed-fixture homogeneous cancellation carrier
Frontier opened: seven-invariant locking under action-owned endpoint variations
```

Next: compute the seven independent coadjoint invariants and their first
variations along the owned boundary field directions.  If they are locked,
construct the associated `O_{-mu}` edge bundle and diagonal curved BFV charge.
If any varies, reject the fixed-orbit horn before spending on a global field.
