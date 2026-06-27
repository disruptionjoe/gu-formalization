---
title: "Generation-sector audit: the quaternionic-parity no-go and the under-determination of the generation count"
status: canon
doc_type: audit_result
verdict: "CONDITIONALLY_RESOLVED (reconstruction-grade), structural no-go for an odd index; generation count UNDER-DETERMINED"
provenance: "Migrated 2026-06-27 from the child repo gu-source-action (CONSTRUCT-01..07). These are AUDIT results about GU's structure, not construction of the missing object, so they belong here with the reconstruction+audit."
tests: "tests/generation-sector/step1..step11"
updated_at: "2026-06-27"
---

# Generation-sector audit: the quaternionic-parity no-go and under-determination

## Why this is here (provenance)

The campaign CONSTRUCT-01..07 was carried out in the child repo `gu-source-action`, which was spun up
to *construct* GU's missing RS/IG source action. In the event, no source action was built: every step
was the parent's own discipline (compute -> adversarially verify -> land only what survives) applied to
GU's generation sector. So these are **audit findings that map GU's edge**, not construction, and they
are migrated here. The child repo is retained only as the construction sandbox for the still-unbuilt
membrane. All claims below reproduce on this repo's verified Cl(9,5)=M(64,H) representation via
`tests/generation-sector/gen_sector_bridge.py` (anchors: bare ||[Pi_RS,M_D]|| = 58.7215, C2 = 155.3625).

## The headline result (C-07): a quaternionic-parity no-go

**THEOREM (reconstruction-grade, closed-form).** Every operator built from GU's own a-priori building
blocks - the Clifford generators e_a (including the timelike i*G_a), the spin generators sigma_ab, the
vector-index generators M_ij, the constraint projector Pi_RS and its complement Q, the twisted Dirac
symbol M_D, and the full BV/BRST/gauge-fixing/ghost apparatus - **commutes with the quaternionic
structure J_quat** of the spinor module. Equivalently, the GU-native operator algebra is contained in
the J_quat-commutant `M(14,C) (x) M(64,H)`, which is just the standard isomorphism `Cl(9,5) = M(64,H)`:
the real Clifford algebra IS the quaternionic-linear algebra.

By **Kramers' theorem** (a Hermitian operator commuting with an antiunitary J with `J^2 = -1` has
even-dimensional eigenspaces), every GU-native Hermitian carrier therefore has **even signature**.
Reading the generation count as the index of such a carrier, the count is forced **even**:

> **GU's quaternionic structure forces an EVEN generation index. An odd count such as 3 cannot arise
> from GU's own building blocks; reaching an odd index requires importing a non-quaternionic
> (non-Clifford) object.**

Verified in `tests/generation-sector/step11_gu_native_parity_theorem.py` (primitives H-linear to ~1e-11;
algebra closure to ~1e-10; carrier signatures all even) and the BV-sector adversarial control (the full
ghost/gauge-fixing apparatus H-linear to ~2e-10). The odd-index escape is FOREIGN: a rank-3 projector is
not H-linear, and the essential scalar-i needed to leave the algebra is itself J-antilinear (defect ~85).

## The honest qualifier (C-06): under-determination, not impossibility

The parity no-go is for the *literal-index* reading. The honest larger picture, also verified, is that
the count is **under-determined**:

- A generic (non-GU-native) rank-r Hermitian carrier on the constraint surface gives signature exactly
  `r`, so odd indices INCLUDING 3 ARE reachable by SOME a-priori carrier (`step10`). What the rep does
  NOT do is **force** the rank/index: choosing rank 3 is a free choice = the forbidden import.
- Under the alternative reading `count = index/2` (Kramers/Weyl doubling), a GU-native H-linear rank-r
  carrier gives index `2r`, so `count = r` is reachable including 3, but the rank stays FREE.

So the precise standing is: **GU neither forces nor forbids three generations; it under-determines the
count.** The quaternionic structure adds one hard constraint on top (the parity no-go for the literal
reading), but does not by itself supply or forbid the number 3.

## Supporting findings (C-01..C-05)

- **C-01** (`step1..step5`): the BV-to-boundary-Dirac map is built at the operator level
  (`M_KT = N * D_Sigma^2`, rel 8.6e-16); the index half is forced shut, `eta(D_Sigma) = 0`, by an
  anticommuting chiral grading `G = Pi_RS - Q`. New obstruction-theorem: any boundary Dirac whose square
  is the positive Koszul-Tate Hessian inherits that grading, so `eta = 0` -- C2 can never be its APS
  index. This re-derives "C2 is not an index" BY CONSTRUCTION, with the mechanism.
- **C-02/C-03** (`step6`, `step8`): that `eta = 0` wall is SOFT (a grading-breaking term revives a
  nonzero index), but the revived index is canonical-per-connection yet CONNECTION-DEPENDENT (its value
  is set by the connection, not the rep). D_Sigma sits in Altland-Zirnbauer class CII; it is the
  particle-hole symmetry C = J_quat.G that forces eta = 0.
- **C-04** (`step7`): the prime 3 is ABSENT from the rep's native dimension prime-spectrum {2,7,13}
  (128 = 2^7, 14 = 2.7, 1664 = 2^7.13, Spin(9,5) = 91 = 7.13); every degree-0 Dirac-content invariant is
  a non-integer surd/rational (C2/bare = sqrt 7, etc.). Honest caveat: the metric signature 9-5 = 4 is a
  degree-0 integer but a declared structural INPUT, not a derived invariant.
- **C-05** (`step9`): every metric so(9,5) (gauge/spin) connection - including the natural self-dual one
  carrying the geometric "3" of Lambda^2_+ - gives generation index ZERO (they preserve the PHS C). The
  families index over the metric fiber retract RP^3 is 2-torsion (3-free).

## Relation to the prior canon

This sharpens, and is consistent with, the existing audit:
- the OPEN "three generations" status and `ch2(S_X)[K3] = -5376` (not 24) are unchanged; the new content
  is *why* the rep cannot supply 3 and *what* an external object would have to do;
- "C2 is not an index" now has a constructive mechanism (C-01);
- the no-go is class-relative in the six-axis sense (`canon/no-go-class-relative-map.md`): it binds the
  closed-internal-quaternionic class, with the escape axis being a non-quaternionic external object.

## The one remaining frontier (still open, in the child sandbox)

A **canonical external membrane** (the unbuilt S_IG) that either (a) pins the free rank a-priori
(half-index reading) or (b) supplies the non-quaternionic structure (literal-index reading) - WITHOUT
import. The honest prior is against it (the rep gives no preferred rank, and the required object is
foreign to GU's quaternionic algebra), but it is the precise, named, still-uncomputed object the whole
program now reduces to. This is the only genuinely "construction" task and it remains in `gu-source-action`.
