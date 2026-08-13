---
artifact_type: construction_and_composition_result
created: 2026-08-09
status: ONE_SIDED_EDGE_FRAME_TRIVIAL_BUNDLE_ONLY__RELATIVE_A0_BITORSOR_GLOBALIZES_EVERY_EXISTING_P_H_TOPOLOGICAL_SECTOR__COMMON_DOMAIN_OPEN
channels: [SOURCE, COMPOSE, BUILD, VERIFY]
ledger_rows: [LT-GR1, LT-GR2b, LT-GR2c, LT-GR3, LT-GR5, LT-GR6]
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 relative edge-bitorsor topology

## Result in plain English

The previous boundary edge formula was locally right and globally too narrow.
Writing its local frames as `u_j=u_i g_ij` silently asks the boundary gauge
bundle to be trivial. Such frames exist exactly when the transition cocycle is
a coboundary. Nontrivial boundary bundles therefore make the old configuration
space empty.

The repair uses an object GU already owns. The distinguished connection `A0`
lives on the same principal bundle `P_H`; label a reference copy of its
boundary restriction and let `u` be a relative frame from the physical copy to
that reference copy. Its patch law is

\[
u_j=k_{ij}^{-1}u_i g_{ij}.
\]

This relative edge bundle is nonempty exactly when the two principal bundles
are isomorphic. Choosing the reference as a labelled copy of the already-owned
`P_H|_B` gives the identity section in every existing topological sector. It
does not trivialize `P_H`, choose a new characteristic class or add a physical
datum.

The repaired law preserves the prior construction. The dressed distortion and
momentum now patch adjointly on the reference bundle, their invariant trace is
global, the physical target-gauge action is still exactly removed, and the
local characteristic kernel remains the four-dimensional gauge orbit. Thus
v0.102--v0.114 survive after a scope correction: their one-sided formulas are
the trivial-reference presentation of the relative theorem, not a universal
global frame.

## 1. Layer 0

| phrase | object here | kept distinct from |
| --- | --- | --- |
| active target gauge action | `Theta -> h^-1 Theta h`, `u -> u h` | passive change of atlas |
| passive target transition | target cocycle `g_ij` | gauge motion on one chart |
| passive reference transition | reference cocycle `k_ij` | a second physical gauge field |
| one-sided edge frame | local `u_j=u_i g_ij` | a section available on every bundle |
| relative edge frame | section of `Isom_H(P_target,P_ref)` | global trivialization of either bundle |
| reference copy | the same topological `P_H|_B` carrying `A0`, with a label | new characteristic class or external datum |
| dressed field | `Q=u Theta u^-1` in `ad(P_ref)` | an absolute matrix on a nontrivial bundle |
| topological globality | nonempty smooth edge configuration bundle | Sobolev completion or common Green/Krein domain |

The load-bearing correction is that **active gauge invariance and passive
patching are different tests**. v0.102 correctly passed the first and proved
adjoint patching of the action data, but it did not prove that a one-sided
group-valued `u` exists globally.

## 2. Exact topology theorem

For transition functions satisfying `g_ij g_jk=g_ik`, a one-sided family

\[
u_j=u_i g_{ij}
\]

implies `g_ij=u_i^-1 u_j`. The cocycle is therefore a coboundary. Conversely,
a coboundary supplies such a family. Hence:

> The one-sided edge-frame bundle is nonempty iff `P_H|_B` is trivial.

This is not an exotic corner. On the thirteen-dimensional boundary
`S^2 x S^11 = boundary(D^3 x S^11)`, a `U(1)` clutching class with `c1=1`
blocks the one-sided frame for the unitary parents. On
`S^4 x S^9 = boundary(D^5 x S^9)`, an `SU(2)` bundle with `c2=1`, embedded in
the compact subgroup of the Spin-native parent, does the same. The exact probe
uses the corresponding integer clutching obstruction as a planted nontrivial
sector, not only a trivial matrix fixture.

For two bundles with cocycles `g_ij` and `k_ij`, relative frames obey

\[
u_j=k_{ij}^{-1}u_i g_{ij}.
\]

Sequential patching gives

\[
k_{jk}^{-1}k_{ij}^{-1}u_i g_{ij}g_{jk}
=k_{ik}^{-1}u_i g_{ik}.
\]

Such a section is precisely a principal-bundle isomorphism, so it exists iff
the two bundles are isomorphic. For `P_ref=P_target=P_H|_B`, `u_i=1` patches by
conjugation and is a canonical witness of nonemptiness.

## 3. Dressing and symplectic descent after repair

Let `Theta_j=g_ij^-1 Theta_i g_ij` and similarly for `P`. Define

\[
Q_i=u_i\Theta_i u_i^{-1},\qquad \Pi_i=u_iP_i u_i^{-1}.
\]

Then

\[
Q_j=k_{ij}^{-1}Q_i k_{ij},\qquad
\Pi_j=k_{ij}^{-1}\Pi_i k_{ij}.
\]

Therefore `Tr(Q Pi)`, the trace symplectic potential and the commutator moment
map patch globally. Under an active target gauge transformation, `u -> u h`
and both dressed variables are invariant. Under a reference gauge change they
conjugate together, leaving every invariant scalar unchanged.

The exact noncommuting `GL(2,Q)` fixture passes the relative triple overlap,
both dressed patch laws, target and reference gauge laws, moment-map transport,
rank-eight dressed map, rank-eight pulled two-form and equality of its
four-dimensional kernel with the target `gl(2)` orbit. Setting `k_ij=1`
recovers the prior one-sided formulas exactly. v0.102 and v0.114 replay green.

## 4. Ownership and constraint accounting

The reference label is not a new bundle topology. `A0` is a distinguished
connection on the source-owned `P_H`, so the reference and physical copies
have the same transition class by construction. The edge isomorphism remains
an auxiliary boundary variable whose target-gauge orbit is characteristic.

This does **not** select among the action parents. The construction is
functorial for the selected `Spin(7,7)` parent, the two `U(32,32)` halves or the
full `U(64,64)` parent, provided each uses its own `P_H` and invariant trace.
Those parents and carriers remain distinct.

```text
new physical fields: 0
new independent bundle classes: 0
new continuous coefficients: 0
new discrete selectors: 0
new booked quotients: 0
P1/P2/P3 consumed: 0
```

## 5. Source return

The source supplies the chimeric-spinor principal bundle, the distinguished
`A0` on it, the tilted double action and associated-bundle grammar. It does not
print a boundary edge frame, a bitorsor, a nonemptiness theorem or a BFV
topology.

```text
SOURCE-CONFIRMS:
  P_H ownership, distinguished A0 on P_H, and tilted/associated-bundle grammar.

SOURCE-SILENT:
  one-sided edge triviality, relative edge bitorsor, topology, BFV bundle,
  common Green/Krein domain and physical boundary selection.
```

The relative completion is therefore a source-compatible repository
construction, not an Eric quotation.

## 6. What closes and what remains

Closes:

- the global nonemptiness criterion for the old one-sided edge frame;
- a topology-complete relative edge bundle on every already-owned `P_H`
  sector using the `A0` reference copy;
- noncommuting triple-overlap, dressing, trace and moment-map descent;
- preservation of the prior local symplectic kernel and classical BFV algebra.

Remains:

- one bulk Green/Krein domain preserving the `H7/H-7` physical and `H8/H-8`
  gauge/ghost traces;
- coupled bulk-boundary BV-BFV compatibility on that domain;
- quantum measure/anomaly and physical choice between charged and edge horns;
- action-parent, signature and amplitude selection;
- Einstein/Standard Model/cosmological recovery.

## 7. Evidence and progress

Primary exact probe: `34 exact + 10 planted = 44 PASS`.
Independent Sage/FLINT: `14 exact + 5 planted = 19 PASS`.
v0.102: `55/55 PASS`; v0.114: `49/49 PASS`.

```text
Ledger v0.115 — 82/82 mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue 84; conditional action-parent range 84..86
Scoped quotients 5

headline_delta: none
frontier_conditions_closed: 2
frontier_conditions_opened: 0
remaining_named_conditions: 2
```

Next:

`CONSTRUCT_ONE_COMMON_BULK_GREEN_KREIN_DOMAIN_PRESERVING_H7_HMINUS7_PHYSICAL_AND_H8_HMINUS8_GAUGE_GHOST_TRACES_ON_THE_RELATIVE_EDGE_BITORSOR__THEN_COUPLE_BULK_BV_TO_BOUNDARY_BFV__KEEP_PHYSICAL_HORN_OPEN`.
