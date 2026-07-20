---
title: "Probe P-T3-W229: is GU's actual W229 record-current source law a member of C_0? (blind-checklist membership audit)"
status: active_research
doc_type: exploration
created: 2026-07-19
directed_by: "Joe direct chat, 2026-07-19 (CH-REC probe P-T3-W229, auditor dispatch)"
axiom: lab/process/boundary-adapter-standing-axiom.md
extends: explorations/channel-swing-CH-REC-2026-07-19.md
inputs:
  - explorations/channel-swing-CH-REC-2026-07-19.md
  - tests/channel-swings/ch_rec_coflip_probe.py
  - explorations/channel-swing-CH-SRC-2026-07-19.md
  - tests/channel-swings/ch_src_minimal_action_toy.py
  - lab/process/boundary-adapter-standing-axiom.md
inputs_opened_only_after_checklist_freeze:
  - explorations/W229-close-a2-source-action-znu-completion-2026-07-14.md
  - explorations/W236-gravity-theta-sector-residual-built-action-2026-07-15.md
  - lab/process/recovery-no-go-defense-register.json (W229 entries)
  - explorations/W203-branch3-source-action-fixed-coefficients-2026-07-14.md (cited by W229; the sign ledger)
  - explorations/W230-close-a4-derive-w154-2026-07-14.md (cited by W236; the W154 adjudication and sign pin)
  - explorations/W180-build-matter-connection-bridge-c3-2026-07-14.md (the C3 Noether identity)
  - explorations/W158-promotion-gate-boundary-term-C3-2026-07-14.md (the gate conormal n)
  - tests/W229_source_action_znu_completion.py (the built law's executable form)
runnable:
  - tests/channel-swings/pt3_w229_membership_probe.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# P-T3-W229: C_0 membership audit of the built W229 record law

This is the decisive half of CH-REC gap G3. The CH-SRC toy proved the
EXISTENCE half (a C_0-member action exists: record current = conserved
Noether K-charge, direction = tau, no free sign slot). This audit decides
the MEMBERSHIP half: whether GU's actual W229 record-current source law is
such an action — direction Noether-derived from the orientation-carrying
structure — or smuggles an independent sign posit. By the co-flip probe's
accounting identity, a smuggled sign IS a second Z/2 payload bit: the
verdict settles N <= 4 vs N = 5 for the (9,5) package at this grade.

Audit discipline: the checklist below was written from the CH-REC and
CH-SRC swing documents and their two probe scripts ALONE, before any W229
source material was opened. The W229 sources are applied to the frozen
checklist in Section 3, never the reverse. A repair does not count as
membership (hard rule, Section 1.3).

## 1. BLIND CHECKLIST (frozen before opening any W229 material)

### 1.1 The class C_0, restated as executable membership criteria

From CH-REC section 1.2 and the coflip probe's `Config`/`q_of`/
`record_register` structure, plus the CH-SRC existence proof (checks
Db1-Db3, Da3/SRC-COH-1), C_0 membership of a record law decomposes into
six checkable items:

**M1 — Noether provenance of the current.** The record current J[Psi]
must be (identifiable as) the Noether current of a symmetry of the W229
action itself, conserved by that action's own dynamics (the CH-SRC
witness: the phase-symmetry K-charge, conserved because the dynamics is
K-unitary; Db1).
- PASS: J[Psi] arises from the action's variational structure; its
  conservation/continuity is a consequence, not a stipulation.
- FAIL: J[Psi] is written down as an independent source postulate whose
  form (in particular its overall sign) is chosen rather than derived.

**M2 — Orientation-sourced sign.** The SIGN of the record current on
physical content must be a computed function of the orientation-carrying
structure: sign(J) = eps wherever the sector charge q > 0, with
q = eps<P_eps Psi, P_eps Psi> >= 0 the physical-sector K-norm (probe
`q_of`; CH-SRC Db2: direction = tau on every physical-sector state
because the sign IS the K-norm sign of the tau-sector).
- PASS: the direction is traceable, slot by slot, to the same eps/J
  structure that selects the sector.
- FAIL: the direction traces to a convention (an overall sign fixed by
  hand anywhere in the chain).

**M3 — No free mu slot (exhaustive sign-datum inventory).** Enumerate
EVERY sign or normalization datum appearing in the source law — named in
advance from the CH-REC swing: kappa, Z_U, the screened-Poisson kernel's
Green's-function sign convention, plus any explicit +/-, any measure or
volume-form orientation, any operator-ordering sign. Each inventoried
datum must resolve to exactly one of:
  (a) DERIVED — fixed by a positivity/coherence condition of the
      structure itself (the way real kappa exists iff stress > 0 iff
      tau = +1 in CH-SRC Da2);
  (b) MAGNITUDE — enters only through |.|^2, a norm, or a manifestly
      positive combination (kappa^2, Z_U as a positive normalization);
  (c) RELATIONAL/GAUGE — a covariant relabel that transports every slot
      at once and acts as the identity on the observable pair
      (sector G-sign, record direction), like the probe's Rl or the
      toy's global K-flip.
- PASS: the inventory closes with every datum in (a), (b), or (c).
- FAIL: at least one residual Z/2 remains whose flip reverses the record
  direction while leaving the sector selection fixed. That datum is a mu
  — one underived Z/2 import — and by the probe's split-costs-one result
  it is exactly the fifth payload bit.

**M4 — SRC-COH-1 (one Krein form in every slot).** The same Krein form
must appear in the sector grading, the source bilinear, and every
coupling/stress slot of the W229 action. A relative sign between any two
slots is a hidden mu-import (CH-SRC Da3 control: stress built with -K
while the sector uses +K breaks the alignment).
- PASS: one form throughout, no relative sign anywhere.
- FAIL: any slot carries its own independent form-sign choice.

**M5 — Vacuum rule.** Psi = 0 -> J = 0 -> theta = 0 with no additive
constant and no background sign (the RECOVERY-NOGO-GR-W229-VACUUM
minimized obstruction, cited verbatim in the CH-REC swing). A record law
with a Psi-independent contribution would carry direction not sourced by
physical content and fails M2 automatically.
- PASS: J vanishes identically at Psi = 0.
- FAIL: any Psi-independent term or offset.

**M6 — Sign-inventory diagonality at the action level.** The zero-import
sign operations available on the W229 action must act diagonally on the
pair (sector, direction): orientation-flip co-flips both; covariant
relabels and anchor exchange act as identity or as the relational
both-anchors flip; dynamics reversal is inert (the probe's
time-reversal-inert check — the arrow must live in the record law plus
eps, not in the propagator).
- PASS: no zero-import operation on the built action flips exactly one
  of (sector, direction).
- FAIL: any zero-import split — this is the co-flip kill firing on the
  real construction.

### 1.2 Pre-registered classification rule for the Green's-function sign
(written BEFORE seeing the W229 kernel)

The known subtlety: the screened-Poisson kernel. Canonically
(-Laplacian + m^2) G = delta has G > 0 pointwise; but the CONVENTION
(sign of the delta, sign of the operator, sign absorbed into the
coupling) can be set several ways. Pre-registered classification test:

- **FIELD REDEFINITION (harmless)** iff flipping the kernel sign can be
  absorbed by a simultaneous covariant transport of the other slots
  (coupling, field, form) such that the composite operation acts as the
  IDENTITY on the observable pair (sector G-sign, record direction).
  This is the probe's Rl criterion: a relabel must transport G, J, U,
  Psi together; a transported flip that changes no observable is gauge.
- **PHYSICAL FLIP (mu-import)** iff the kernel sign appears in the
  record-direction chain but NOT in the sector-selection chain (or vice
  versa), so that flipping it reverses the record direction with the
  sector fixed. Equivalently: iff absorbing the flip requires an
  uncompensated sign in exactly one slot, violating SRC-COH-1. This is
  the probe's rejected partial-relabel attack (J -> -J with G fixed) in
  kernel costume.

Executable form: write the direction-determining chain
sign(record increment) = f(eps, kernel sign s_G, coupling signs, form
signs); write the sector-selection chain sigma = g(eps, form signs).
The kernel sign s_G is a field redefinition iff s_G either (i) cancels
out of f entirely (enters through a square/magnitude), or (ii) enters f
and g jointly such that any flip of s_G composable with a relabel leaves
(sigma, dir) fixed. It is a physical flip iff s_G enters f alone,
uncancelled.

### 1.3 Pre-registered verdict semantics

- **MEMBER**: all of M1-M6 pass, with the Green's-function sign
  classified as (i)/(ii) field-redefinition. Consequence: T3 holds on
  W229, H-REC holds at construction grade for the built law, the arrow
  rides free on the orientation bit, and N <= 4 stands.
- **NOT-MEMBER**: any of M1-M6 fails with receipts. The failing datum is
  NAMED (which slot, which file, which line/equation). Consequence: that
  named posit is the fifth payload bit; N = 5 by the accounting
  identity. No softening: "it could be repaired" does not avert the
  verdict.
- **CONDITIONAL**: membership holds if and only if the boundary adapter
  supplies a typed structure that the built law references but does not
  itself construct. Per the standing axiom this is not a stop: the
  dependency is typed precisely (what object, what property, which
  checklist item it discharges) and routed as an adapter demand. The
  verdict then reads MEMBER-GIVEN-(typed demand), and the N-accounting
  inherits the same conditionality already carried by the payload.
- **HARD RULE (no mid-audit repair).** If the built law fails an item,
  the audit records (a) the failure with receipts and, separately,
  (b) the MINIMAL repair as a proposal addressed to the channels. The
  repair is never retro-fitted into the audit; the verdict is rendered
  on W229 as built on 2026-07-14/15, not on any improved variant.

**What passing looks like:** every sign datum in the built source law
lands in DERIVED / MAGNITUDE / RELATIONAL; the record direction is
computed from the orientation with no residue; the kernel sign cancels
or transports.

**What failing looks like:** a single Z/2 choice — however innocently
dressed (a kernel convention, a sign inside Z_U, an orientation of an
integration measure, a "+" chosen where "-" would have served equally)
— that the structure does not force and whose flip would reverse the
record direction alone.

--- CHECKLIST FROZEN. W229 sources opened only below this line. ---

## 2. W229 sources opened (audit trail)

Opened in this order, after the checklist freeze:

1. `explorations/W229-close-a2-source-action-znu-completion-2026-07-14.md` —
   the built law. Parent action `S_parent = int<P_IG, D_A U> -
   1/(2Z_U)<P_IG,P_IG> - V_src - (c_theta/2)<theta,theta> + S_cross + S_bdy`;
   exact Gaussian elimination `P_IG = Z_U D_A U`; field equation
   `(-Z_U D_A* D_A + c_theta eta) theta = J`, `c_theta = 1/kappa`, solution
   `theta = G * J`; connection law `D_A* F_A = theta_eff`; kappa and Z_U as
   the two normalization scales; standing residues named (eta-from-gimmel-area
   magnitude, K_IG narrowing, W154, "the interacting C-operator / Krein
   sign #1 (W203)").
2. `explorations/W236-gravity-theta-sector-residual-built-action-2026-07-15.md`
   — the vacuum rule exercised: `J^a = Re<Psi, K_S e_a Psi>` is a Krein
   bilinear, `J[Psi=0] = 0` at all orders, O invertible for `c_theta > 0`
   (sign "forced by W230 / C-positivity"), theta = 0 in vacuum.
3. Defense register `RECOVERY-NOGO-GR-W229-VACUUM`: W229's fork typed as
   "record-sourced induced-YM branch-3 action with screened-Poisson source
   law... kappa and Z_U still normalization data"; minimized obstruction
   includes the vacuum rule `Psi=0 -> J=0 -> theta=0` verbatim.
4. Cited canon needed to trace the sign chain (all named as W229/W236
   dependencies): W203 (the coefficient/sign ledger and the SGN block), W230
   (the W154 adjudication: COMPLETED-POSIT, coupling sign forced by
   C-positivity, magnitude unbuilt), W180 (the C3 identity), W158 (the
   promotion-gate conormal), and `tests/W229_source_action_znu_completion.py`
   (the executable form: `K_S = e_0 e_1 ... e_8` built from the verified
   Cl(9,5) rep; `J^a = Re<Psi, K_S e_a Psi>`; `theta = kappa eta J`;
   `S_eff = -(kappa/2)<J, eta J>`).

## 3. Audit: checklist applied to the built W229 law, item by item

Probe receipts: `tests/channel-swings/pt3_w229_membership_probe.py`, run
2026-07-19 on the actual Cl(9,5) = M(64,H) objects via `gen_sector_bridge`
(identical anchors to the W229 test), exit 0, headline `6 [E] + 2 [F] = 8`
(setup `[T] = 2` excluded).

### M1 — Noether provenance: PASS

`J^a = Re<Psi, K_S e_a Psi>` is exactly `delta S_D / delta A_a` of the
record-field Dirac term `S_D = Re<Psi, K_S c(A) Psi>` — W180's C3 identity,
machine-checked in W203 (PC3a/PC3b) and re-anchored in the W229 test (PC3:
`S_D(A) = A.J` exact). Conservation is Noether II (`D_A* J = 0`, W180,
cited; flat-background discrete check `d* theta_eff = 0` is W229 NL5). The
current is the gauge Noether current of the action's own matter sector; its
form is not a stipulated source postulate. The current's sign structure is
carried entirely by `K_S` — the orientation-carrying Krein form, so the
Noether symmetry is orientation-graded in exactly the CH-SRC toy's sense
(the K-charge of the sector).

Important scope split, so nothing is oversold: what IS a postulate is the
IDENTIFICATION `theta = J` — that the IG sector is sourced by the record
current at all (W154). W230 proves this is NOT Noether-derivable
(COMPLETED-POSIT: equivalent to the single axiom `c_kin = 0`, marble/wood).
But that is a which-current posit, not a sign posit — W230's own summary:
"the coupling sign forced and its magnitude the standing route-beta
residue." And it sits UPSTREAM of T3: CH-REC's C_0 class definition already
carries the record-sourced shape as its premise ("the W229 lineage"). It is
typed below as dependency D2, not counted as a mu.

### M2 — Orientation-sourced sign: PASS, conditional on D1

The direction chain in the built law:

```
sign(record readout)  =  Krein grade of the record content w.r.t. K_S
                      =  eps   wherever the content is confined to the
                               eps-selected (C-positive) sector.
```

Receipts: on the eps-selected eigenspace of the actual `K_S`, the C_0
charge `q = eps<Psi, K_S Psi>` is strictly positive and the register
direction equals eps for BOTH anchors (probe M2 check, 200 draws per
anchor); W203 SGN3 (reproduced in the probe: `J.eta.J > 0` on 100% of
confined draws) shows the same confinement pins the previously two-sided
eta-readout. No sign enters the chain other than eps.

The condition (D1): "confined to the C-positive sector" is GU's standing
records-postulate (W132/W137), verified here on the KINEMATIC proxy (the
+1 eigenspace of `K_S`); whether the INTERACTING C-operator performs the
grading is W203's open question #1. This is a typed structural dependency
(existence of the grading operator), not a hidden sign: the sign VALUE it
delivers is eps itself, the already-counted payload item 1. The probe's
first [F] control shows D1 has teeth: on generic unconfined Psi the
pairing is two-sided (SGN1 reproduced, range [-7.6e-2, +1.6e-1]) — an
unconfined W229 law has NO definite direction, rather than a wrong one.

### M3 — Sign-datum inventory: PASS (every datum resolves; no residue)

| datum | resolution | receipt |
|---|---|---|
| `kappa` sign | (a) DERIVED — forced positive by C-positivity (given D1); "the one genuine physics datum... gated on question #1" | W203 §4 + SGN3; W230 ("only the sign forced"); W236 (`c_theta = 1/kappa > 0` "sign forced by W230/C-positivity") |
| `kappa` magnitude | (b) MAGNITUDE — normalization (eta-from-gimmel-area, Newton-G-like); not a Z/2 | W203 COEF ledger; W229 FF ledger |
| `Z_U` | (b) MAGNITUDE — the one new free datum is declared and rescale-checked as a SCALE (`ell^2 = Z_U kappa`, NL4); direction-irrelevant: the record chain is Z_U-independent (the ultralocal limit NL2 carries the whole direction structure; J[Psi] never touches Z_U) | W229 §4, NL2/NL4; probe M3 kappa/Z_U checks |
| source coupling `-<theta, J>` | (a) DERIVED — geometry_forced by the C3 identity (`J = delta S_D/delta A`); residual convention is an auxiliary-field redefinition | W203 COEF ledger; probe coupling-flip check (`S_eff` invariant, `J` untouched) |
| `K_S` overall sign (frame-order convention in `e_0...e_8`) | (c) RELATIONAL/PAYLOAD — flipping it exchanges the anchors AND flips the current sign together: the co-flip, i.e. payload item 1's two-anchor freedom, not a second bit | probe M6 co-flip check |
| `eta` scale-sign (Schur gives uniqueness up to scale, sign included) | (a)+(c) — transported jointly with kappa: `(eta, kappa) -> (-eta, -kappa)` is the exact identity on `theta*` and `S_eff`; the physical pin is the product `c_theta > 0`, C-positivity-derived | probe joint-flip check (`|dS_eff| = 0`) |
| Green's-function / kernel sign | NOT AN INDEPENDENT SLOT — computed from `{c_theta > 0, coupling, eta}` (Section 4) | probe coupling-flip check; W229 NL0/NL1 |
| gate conormal `n` (`S_gate = n_a J^a`) | (a) DERIVED — W158 pins `n` as a q=5 (negative-eta) frontier direction whose orientation is set by the confirmed/unconfirmable sidedness, i.e. by WHICH sector is the C-positive (confirmed) one — the same eps assignment; exchanging the anchors drags `n` (co-flip, not a split). The flux is sign-definite on confined content (W158 RISEb: "monotone-in, Krein-graded-out flux is STILL sign-definite") | W158 §1-2 (frontier defined as the edge of `H_C+`), SG3 (Stab(n) invariance), RISEb |
| vacuum offset | ABSENT — `J` is a homogeneous Krein bilinear; no Psi-independent term exists | W229 W154-1; W236 C1 |

The inventory CLOSES. No residual Z/2 remains whose flip reverses the
record direction with the sector fixed. The probe's second [F] control
verifies the accounting identity on the real objects: the ONLY way to
flip direction alone is to insert an explicit `mu = -1` into the register
law — a datum the built action does not contain — and it is flagged as
exactly one underived Z/2 import.

### M4 — SRC-COH-1 (one Krein form): PASS

One so(9,5) Krein structure serves every slot: `K_S = e_0...e_8` on the
spinor slot (Dirac term, record current, gate current — all three use the
same `K_S`), and `eta` on the vector/theta fiber slot, where `eta` is not
an independent choice but the Schur-FORCED equivariant kernel of the SAME
Clifford structure (W203 KER1-3; W229 KER1/KER3: the identical nulldim=1
computation pins the mass kernel AND the gradient pairing `Q_IG` — "no
new fiber freedom"). The spinor-slot anti-self-adjointness (`Sigma^dag K_S
+ K_S Sigma = 0`, PC1b) and the vector-slot anti-self-adjointness
(`T^T eta + eta T = 0`, GAU1) are the same invariance statement in two
representations. The one cross-slot sign (eta's scale-sign against kappa)
is jointly transported and pinned by `c_theta > 0` — no relative-sign slot
anywhere. W203 §4 states the coherence outright: "the sign literally IS
the Krein grade of the record current" — the GR cancellation readout and
the record readout are one Krein readout, which is SRC-COH-1 satisfied on
the built action.

Probe report worth recording: the eta-pairing `J.eta.J` is positive on
BOTH anchors' confined draws (minus-anchor range [+3.4e-2, +3.9e-1]) —
the GR-side healthy sign is anchor-INVARIANT while the record direction
co-flips with the anchor. That matches CH-REC's two-anchor structure
(physical norm positive for both eps values in isolation; the anchor
exchange is relational) and confirms there is no anchor-asymmetric slot
hiding in the GR readout.

### M5 — Vacuum rule: PASS

`J` is a homogeneous Krein bilinear: `J[Psi=0] = 0` identically, no
additive constant, no background sign (W229 W154-1; W236 C1-C3: theta = 0
at ALL orders, structural across the `{kappa, Z_U}` sweep and the
`kappa -> inf` edge). The defense register's minimized obstruction quotes
the rule verbatim (`Psi=0 -> J=0 -> theta=0`). The vacuum carries zero
orientation witness, exactly the CH-REC "one absence seen twice" shape.

### M6 — Sign-inventory diagonality: PASS at audit grade

Zero-import operations available on the built law, and their action on
(sector, direction):

- anchor/frame flip (`K_S -> -K_S`): flips BOTH — co-flip (probe M6).
- joint `(eta, kappa)` flip: identity (probe; exact to 0).
- coupling flip + `theta -> -theta`: identity on the record chain and on
  `S_eff` (probe).
- `kappa`-flip alone: NOT zero-import (it violates the C-positivity
  derivation) — and even executed adversarially it leaves (sector, J,
  direction) fixed, changing only the GR-side response (probe M3): it is
  a GR-slot sign, not a record-direction slot.
- dynamics reversal: the record chain is propagator-independent — `J` is
  a state bilinear and the direction is its Krein grade, not a
  time-stepping artifact; the finite probe's time-reversal-inert check is
  the class-level statement, and nothing in the built law adds a
  propagator-borne sign for it to miss.

No zero-import operation flips exactly one of the pair. The co-flip kill
does not fire on the built law at this grade. (The BV/cohomological-grade
inventory — CH-REC gap G2 — remains open and is not claimed here.)

## 4. The Green's-function sign: classification

Pre-registered rule (Section 1.2) applied. The screened-Poisson law is
`O theta = J` with `O = -Z_U D_A* D_A(eta) + c_theta eta`, solution
`theta = O^{-1} J` (W229 NL0/NL1: O self-adjoint in the eta inner
product, equation solved directly). Classification computation:

**The two chains.** Direction chain: `sign(record readout) = f(eps)` —
the register reads the current `J` (and its gate flux `n.J`), and `J` is
UPSTREAM of the kernel; the kernel determines theta's RESPONSE to `J`,
which feeds the GR/connection side (`theta_eff`, `S_eff`), never the
register. So the kernel sign does not appear in `f` at all. Sector chain:
`sigma = g(eps)` via the `K_S` eigenspace selection — also
kernel-independent.

**No independent slot.** In the built law the kernel's sign is a computed
consequence of three data: the mass-term sign (`c_theta = 1/kappa > 0`,
DERIVED by C-positivity — W203 SGN3, W230, W236), the coupling sign
(DERIVED by the C3 identity; residual convention absorbed by
`theta -> -theta`, probe-verified `S_eff` invariant with `J` untouched),
and the eta normalization (RELATIONAL: `(eta, kappa)` joint flip is the
exact identity, probe-verified). There is no fourth place where a
Green's-function sign convention could be flipped independently. An
attempted standalone kernel flip would have to un-derive one of those
three — i.e., flip a sign in exactly one slot while the sector grading
keeps the original `K_S` — which is precisely the SRC-COH-1 violation
(the CH-SRC Da3 control, the probe's rejected partial-relabel attack in
kernel costume), and it is PAID (one Z/2), not free.

**Classification: FIELD REDEFINITION (case i/ii of the pre-registered
rule) — and strictly, not an independent datum at all.** The kernel sign
never enters the direction chain `f`; every flip route through the data
that DO determine it is either derived (blocked at zero import) or
jointly transported (identity on observables). Flipping it is therefore
orientation-equivalent where absorbable and import-paid where not. It is
NOT a physical flip and NOT a candidate fifth bit.

The one genuine physical sign in the kernel's neighborhood is
`c_theta > 0` (screening vs tachyonic anti-screening — detectable, hence
physical). It is DERIVED, not free; and even adversarially flipped it
changes the theta response, not the record direction (probe M3).

## 5. Verdict

**MEMBER, CONDITIONAL (typed) — no independent sign posit found; N <= 4
stands at this grade.**

The actual W229 record-current source law has the C_0 structure: the
record current is the Noether current of the orientation-graded (K_S-
carrying) symmetry of the built action (M1); its direction is the Krein
grade of confined record content — the transmitted orientation eps and
nothing else (M2); the exhaustive sign inventory closes with every datum
DERIVED, MAGNITUDE, or RELATIONAL — kappa's sign C-positivity-forced,
Z_U a direction-irrelevant magnitude, the coupling C3-forced, the kernel
sign a computed consequence, the frame convention the payload bit itself,
the gate conormal oriented by the same confirmed-sector assignment (M3);
one Krein form serves every slot (M4); the vacuum rule holds identically
(M5); and no zero-import operation on the built law splits (sector,
direction) (M6). The mu slot that would be the fifth payload bit is
demonstrably ABSENT: the only direction-only flip constructible on the
real objects is an explicitly inserted, import-flagged `mu = -1`.

Per the standing axiom, the conditionality is typed, not a stop:

- **D1 (sector confinement / the interacting C-operator).** The
  direction-equals-eps result holds where records are confined to the
  C-positive sector. In-repo this is verified on the kinematic proxy
  (the +1 eigenspace of `K_S`; W203 SGN3, probe-reproduced at 100%);
  whether the INTERACTING C-operator (`[P_ghost, S] = 0`) exists and
  grades the record current positive is W203's question #1, expected
  adapter/interaction-grade structure. Type of the dependency: the
  EXISTENCE of the grading operator, not a sign value — the sign it
  delivers is payload item 1's eps. Failure mode if D1 falls: the built
  law's direction becomes TWO-SIDED (SGN1) — no definite arrow at all,
  H-REC loses its subject — which is a different failure from a smuggled
  fifth bit, and would need its own accounting.
- **D2 (W154 / c_kin = 0).** The record-sourced SHAPE of the law is the
  marble/wood posit, proven necessary and not Noether-derivable (W230,
  COMPLETED-POSIT). It is upstream of T3 (C_0's class definition already
  assumes the record-sourced shape), its SIGN is forced (route-beta /
  C-positivity), and its content is a which-current identification, not
  a Z/2. It does not count against membership; it is the standing
  conditionality CH-REC's accounting already carries.

**Consequence for the (9,5) N-accounting:** T3 HOLDS on the built W229
law at this grade, conditional on D1 (typed above). By CH-REC's
accounting identity the arrow rides the orientation bit at zero extra
import; **no fifth payload bit exists in the built law; N <= 4 stands**,
with exactly the conditionality structure the channels already carry
(D1 = question #1's structural half; D2 = W154). The remaining named
routes to N = 5 are unchanged and now sharper: (i) a zero-import split
appearing at the BV/cohomological grade (CH-REC gap G2 — the inventory
here is action-level, not cohomological); (ii) D1 resolving in a form
that requires a SECOND anchor freedom not identifiable with the
kinematic K_S orientation — that would be a genuine new Z/2 and should
be watched for explicitly when the interacting C-operator is built.

**No repair object is emitted.** The hard rule (Section 1.3) required
separating failure-plus-minimal-repair; there is no failure to repair.
What would DISCHARGE the conditions (channel proposals, not W229
retro-fits, and not part of this audit's verdict): for D1, construct the
interacting C-operator on the built action and verify it grades `J`
positive on records (this is exactly W203's question #1 and CH-REC gap
G4's neighborhood); for D2, the standing eta-from-gimmel-area bridge.

### Raw answer to CH-REC gap G3 (both halves now)

- Existence half (CH-SRC, prior): a C_0-member action exists. DONE.
- Membership half (this audit): GU's actual W229 record law IS such an
  action, conditional on D1/D2 as typed — the direction datum was
  isolated and it is the transmitted orientation, not a convention in
  kappa, Z_U, or the kernel. G3 is discharged at audit grade; what
  remains of it is exactly D1, which is not a T3 question but question
  #1.

## 6. Boundary

Receipts: probe `tests/channel-swings/pt3_w229_membership_probe.py`, run
2026-07-19, exit 0, headline `6 [E] + 2 [F] = 8` (setup `[T] = 2`
excluded), on the actual Cl(9,5) rep (gen_sector_bridge, the W229 test's
own anchors). Document receipts cited inline per item (W229 PC3/NL0-NL5/
W154-1/FF; W203 PC3-PC4/KER/SGN/COEF; W230 sign pin + COMPLETED-POSIT;
W236 C1-C6; W158 SG3/SG5/RISEb; defense register minimized obstruction).

Conditional work under the standing axiom, R0_COND working grade. No
claim status, canon verdict, or public posture moves. No repairs applied
to any W229 artifact; no test or exploration files modified other than
this document (and, if emitted, the single declared probe script). No
external actions.
