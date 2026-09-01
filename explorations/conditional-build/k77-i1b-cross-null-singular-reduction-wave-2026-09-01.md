---
title: "K77 I1B cross-null singular-reduction wave"
status: active_research
doc_type: reverse_scaffold_i1b_cross_null_singular_reduction_result
date: 2026-09-01
claim_ceiling: exact rank-changing Green normal form for the native I1B 24-to-22 quotient jump, with an unavoidable logarithmic pole for any compatible ordinary connection and exact nonselection of the tangential holonomy coefficient; no smooth cross-null quotient bundle, source-owned coupled Hessian, physical reduction, prediction, confirmation, or verdict
manifest: lab/process/k77-i1b-cross-null-singular-reduction-wave.json
probe: tests/channel-swings/k77_i1b_cross_null_singular_reduction_probe.py
---

# K77 I1B cross-null singular-reduction wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`

```gu-typed-objects
result: native-rank I1B presymplectic normal form whose compatible ordinary connection has an unavoidable logarithmic pole at the 24-to-22 quotient jump
carrier: real rank-220 I1B fibre with constant rank-196 radical plus a rank-24 transverse block away from u=0; two transverse modes join the radical at u=0 LAYER=conditional CHIRALITY=N/A
pairing: varying Green form J_u=J_22 direct_sum uJ_2 on the transverse rank-24 block ON=native_rank_changing_normal_form
real_structure: real presymplectic carrier on the two punctured strata and null interface
grading: radical-to-presymplectic-quotient sequence with variable quotient rank; not a constant-rank BV-BFV bundle
action_owner: rank data are native to the I1B packet; the normal-form connection is repository-derived and not a source-owned coupled Hessian
target: connection-compatibility trace identity, logarithmic residue, transport collapse and holonomy-coefficient nonselection MAP-TYPE=obstruction
```

## Native rank jump in one exact normal form

Let the rank-220 I1B fibre contain its constant rank-196 radical `K`. On a
transverse rank-24 complement, use a coordinate `u` normal to the null stratum
and write

```text
J_u = J_22 direct_sum u J_2,                           (1)
J_2 = [[0,1],[-1,0]].
```

For `u != 0`, (1) has rank 24, so the full radical has rank 196 and the Green
quotient rank is 24. At `u=0`, the last Darboux pair becomes radical: the full
radical has rank 198 and the quotient rank is 22. This realizes the exact
native timelike/null ranks without pretending that they form one constant-rank
quotient bundle.

## Every compatible ordinary connection is singular

For a connection coefficient `A_u` on the transverse block, compatibility
with the varying Green form is

```text
partial_u J_u + A_u^T J_u + J_u A_u = 0.             (2)
```

Restrict (2) to the degenerating two-plane and call the resulting matrix
`B_u`. For every two-by-two matrix,

```text
B_u^T J_2 + J_2 B_u = tr(B_u) J_2.
```

Equation (2) therefore forces

```text
1 + u tr(B_u) = 0,
tr(B_u) = -1/u.                                       (3)
```

No bounded, continuous or smooth ordinary connection can satisfy (3) across
`u=0`. This is stronger than the prior dimension count: it identifies the
exact singularity that any compatible punctured-stratum representative must
carry.

The trace residue `res(u B_u)=-1` is forced. The symmetric logarithmic
representative is

```text
B_u = -(1/(2u)) I_2.                                  (4)
```

It has matrix residue `-I_2/2`; other representatives may add trace-free
singular terms. Parallel transport for this symmetric representative scales
the degenerating pair by

```text
q(u1) = sqrt(|u1/u0|) q(u0).                          (5)
```

The pair collapses as `u1 -> 0`; inverse transport diverges. Equation (5) is a
singular reduction on the punctured strata, not an isomorphism through the
null interface. At `u=0` the two modes join the radical and the honest quotient
has rank 22.

## The singular reduction does not select `log(2)` versus `log(3)`

On either punctured side, append the predecessor's tangential symplectic
connection

```text
A_y = log(r) x H,       r>1,
```

with `H` blockwise `diag(1,-1)`. It is compatible with every `J_u`, commutes
with the scalar singular residue on the degenerating pair, and produces the
same fixed-stratum rectangle holonomy family

```text
Hol_r = diag(r^-1 I12, r I12).
```

Both `r=2` and `r=3` satisfy the identical normal compatibility equation and
carry the same forced trace residue; both also admit the symmetric
representative (4). The cross-null trace singularity is universal for this
normal form but independent of the tangential coefficient. It therefore does
not distinguish the two predecessor actions.

The exact certificate passes `19/19`; its hostile selftest catches `14/14`
mutations. It verifies the rank jump, the full two-by-two trace identity,
compatibility of (4), transport scaling, symplectic tangential controls and the
coefficient-nonselection fence.

## Scope and next condition

This is a repository-derived local normal-form theorem using native I1B rank
data. It is not a source theorem that every possible derived, stratified or
sheaf-valued reduction must have this form. It excludes an ordinary smooth
constant-rank Green quotient and bounded compatible connection across the
stated transverse rank jump. A logarithmic/filtered/derived replacement may
still exist, but must declare its category, matching data, domain and action
owner.

The next I1B selector must therefore come from a source-owned coupled Hessian
term that fixes the tangential coefficient, or from additional singular
matching/boundary data whose compatibility equation couples the trace residue
or trace-free singular data to `r`. Merely requiring Green compatibility,
ordinary transport on each stratum, the forced trace residue `-1`, or the
symmetric `-I_2/2` representative leaves the complete `r>1` family
nonselected.
