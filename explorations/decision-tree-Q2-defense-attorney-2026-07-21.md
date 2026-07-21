---
title: "Q2 DEFENSE ATTORNEY: attacking the exhaustiveness of the Q2-FREE kill -- VERDICT DEFENSE-FAILS. The kill's flagged seam (is there an UNWELDED alpha-odd first-person feature, NOT the record arrow and NOT welded to sigma, that could supply sigma?) is CLOSED. The strongest candidate -- the TaF causal-past RETRACTION pi (pi.pi=pi, oriented, non-invertible), proven STRICTLY MORE GENERAL than the fixpoint-free involution alpha on two axes (orbit-cardinality 2^k>2 and orientation idempotent-vs-bijection) -- does NOT furnish the middle. Its cardinality-generality is alpha-EVEN (extra EXCLUSION, not selection -> Horn 2); its orientation IS the record arrow / the very mechanism that makes sigma external (sigma's value is the FORGOTTEN datum in the up-set the retraction cannot reach -> Horn 1 + confirms the kill). 'Unwelded alpha-odd' is shown to be NOT a third horn: it collapses to a relocated Horn 1 (an unsourced second external coin whose coherence with sigma is a product-of-odds = alpha-even, fixing only the RELATIVE sign, never the absolute value). Attack lines 2 (coherence-supply) and 3 (residual record d.o.f.) also collapse. Q2-FREE is ROBUST; the standpoint-supplied door stays closed at current grade. One residue named once."
status: active_research
doc_type: exploration
created: 2026-07-21
defends_against: "the Q2 kill (explorations/decision-tree-Q2-sector-bit-forced-free-supplied-2026-07-21.md, verdict Q2-FREE, Section 4.2 exhaustive dichotomy + Section 6 HOSTILE-VERIFICATION FLAG)"
program: explorations/prereg-three-object-decision-tree-2026-07-21.md
axiom: lab/process/boundary-adapter-standing-axiom.md
inputs:
  - explorations/decision-tree-Q2-sector-bit-forced-free-supplied-2026-07-21.md
  - explorations/decision-tree-Q3-one-anchor-vs-two-2026-07-21.md
  - explorations/boundary-law-operator-lift-2026-07-20.md
  - explorations/diagonal-boundary-unification-2026-07-20.md
  - "READ-ONLY temporal-issuance: formal/lean/OnlineIssuance/BoundaryInvolution.lean, BoundaryParent.lean"
  - "READ-ONLY time-as-finality: explorations/involution-typing-lemma-2026-07-20.md (T-REFUTE; the causal-past retraction characterization)"
runnable:
  - tests/channel-swings/q2_defense_attorney_probe.py
outcome: DEFENSE-FAILS
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_actions: none
---

# Q2 defense attorney: is the FREE kill's dichotomy really exhaustive?

Adversarial toward the KILL, not toward GU. Program discipline: a single
argument's exhaustiveness must be attacked before a kill is treated as global.
The Q2 kill concluded **Q2-FREE** -- "the first person HOSTS sigma and FORCES
its externality but does NOT supply its value" -- on an EXHAUSTIVE two-horn
dichotomy (kill Section 4.2): a standpoint defined WITH the record arrow
presupposes sigma (Horn 1, Q3's co-flip weld); defined WITHOUT it is the
alpha-even self-encoding structure, blind (Horn 2). The kill flagged its own
seam (Section 6): the dichotomy is exhaustive **only if every first-person
alpha-odd object is welded to sigma** -- i.e. only if there is **no unwelded
alpha-odd first-person feature**. My job: exhibit one, or confirm none exists.

**Verdict up front: DEFENSE-FAILS. The kill holds; Q2-FREE is robust.** I ran
all three attack lines. The strongest -- the TaF causal-past retraction as a
second alpha-odd handle -- does not open a middle: read at its own home, the
retraction is the very mechanism that makes sigma external, and sigma's value is
literally the datum it forgets. I close the flagged seam positively: "unwelded
alpha-odd" is NOT a third horn; it collapses to a relocated Horn 1.

Receipt: `tests/channel-swings/q2_defense_attorney_probe.py` -- deterministic
(double-run byte-identical), numpy-seeded (20260721), no network, exit 0,
HEADLINE `10 [E] + 3 [F] = 13 ALL PASS`.

---

## The seam, stated precisely

alpha is the K_S-sign flip. An object is **alpha-odd** if alpha flips it, and
**alpha-even** if alpha fixes it. The kill's two horns rest on: (Horn 1) the
only exhibited alpha-odd first-person object is the record arrow, and Q3 welds
it to sigma (`r * sigma = +1`, alpha-invariant -- they co-flip as one datum);
(Horn 2) everything else first-person is alpha-even (the excluded-reading /
self-encoding class = the alpha-equivariant class, per diagonal-boundary), and
alpha-even structure cannot mint an alpha-odd value.

The middle the kill says does not exist would be an **unwelded alpha-odd
first-person feature**: alpha-odd (so it evades Horn 2's blindness), and NOT
welded to sigma (so it evades Horn 1's presupposition), which could then FIX
sigma without presupposing it. Three attack lines hunt for it.

---

## Attack line 1 -- a second, independent alpha-odd handle (the retraction)

The named candidate is the **TaF causal-past retraction** `pi`. The cross-repo
receipts type it exactly (temporal-issuance `BoundaryParent.lean`, the `H_taf`
hypothesis: "the TaF mechanism is now known to be a causal-past retraction
`pi . pi = pi`, oriented, non-invertible, not this file's fixpoint-free
involution ... a later typed assembly must keep the retraction and involution
legs distinct"). The involution-typing work (time-as-finality
`involution-typing-lemma-2026-07-20.md`, outcome **T-REFUTE**) proves `pi` is
**strictly more general** than the fixpoint-free involution alpha on two axes:

1. **Orbit-cardinality.** `pi`'s indistinguishability classes have size `2^k`
   (k = number of independent future witnesses); alpha's orbits have size <= 2.
   They coincide only at k=1.
2. **Orientation.** `pi` is an idempotent, non-invertible retraction (it forgets
   the future up-set); alpha is an order-2 bijection. The causal cut is
   antisymmetric/oriented (past accessible, future not); the flip is symmetric.

The kill's seam is exactly: does either axis of extra generality furnish an
unwelded alpha-odd degree of freedom that supplies sigma? The task's own hint:
"the retraction's orientation is alpha-odd-flavored and is NOT obviously the
record arrow." I take each axis at full strength.

### 1a. Axis 2 (orientation) -- steelman, then the collapse

**Steelman (the strongest form of DEFENSE-SUCCEEDS).** An actual located
observer R has a DEFINITE causal-past retraction `pi_R`: it retracts onto R's
real accessible down-set. This is not a choice -- R's past is what it is -- so
`pi_R` is possessed independently of sigma, NON-circularly (you do not choose
sigma to have a past; you have a past by being located). `pi_R` is oriented
(alpha-odd-flavored: a directed arrow of forgetting). Coherence: the record
arrow must agree with the retraction orientation. So `pi_R` fixes the record
arrow, and the record arrow fixes sigma (Q3). sigma is SUPPLIED by the
standpoint's actual causal position -- the elegant observer-supplies-the-bit
result. This is the FLP indexical steelman ("occupying a node constitutes the
indexical"), now carried by the strictly-more-general engine the kill did not
have in front of it. If any door reopens Q2, it is this one.

**The collapse -- and it reinforces the kill.** Read the retraction at its own
home. In TaF, `A*(R)` is the accessible past down-set; the value of the finality
bit lives in the **forgotten future up-set** (`R_self_finality` records exist
only at `{e_E1, e_E2, e_meta}`, structurally absent from `A*(R)` -- the model
raises `ValueError` on every external node). The retraction `pi` retains the
down-set and FORGETS the up-set. So:

- `pi_R` gives R the past CONTENT but not the VALUE sigma -- because sigma's
  value is precisely the datum in the forgotten up-set (probe E: a sigma-reading
  functional does NOT factor through `pi`; `pi` is non-invertible, it forgets
  sigma). The retraction does not merely fail to supply sigma; **it is the
  operation that puts sigma out of reach.** This is the kill's Horn-2 blindness
  strengthened, now on the strictly-more-general engine.
- The retraction's INTRINSIC orientation ("toward the fixed image") is
  alpha-EVEN: it is shared by `pi` (retract onto past) and its alpha-image `pi'`
  (retract onto future) -- both have the toward-image property (probe E). Only
  WHICH image (past vs future) is alpha-odd, and that is a free coin whose
  sigma-VALUE is the forgotten content. So "having a definite retraction
  orientation" splits into an alpha-even part (idempotency's toward-image
  direction -- blind, Horn 2) and an alpha-odd part (which end is forgotten =
  the record/causal arrow -- welded to sigma, Horn 1). No unwelded alpha-odd
  residue is left over.

The involution-typing doc says this in its own voice (its Section 3.2): "the
'orientation datum' of the GU parent is external: TaF's exclusion is ... a
directed forgetting whose forgotten content you cannot reach." The retraction is
the MECHANISM of sigma's externality, not a supplier of its value -- exactly the
kill's Section 6 conclusion ("the inside-ness of the observer forces the
externality of the bit; it does not fill it"). Axis 2 collapses INTO the kill.

### 1b. Axis 1 (orbit-cardinality) -- the extra reach is alpha-even

The retraction excludes a `2^k`-element future cube; the involution only pairs
2 elements. The EXTRA content is HOW MUCH is forgotten (the width of the excluded
antichain), a symmetric, sign-free cardinality fact. Probe (k=2): the functions
the retraction excludes BEYOND the involution are **exactly the non-constant
alpha-EVEN functions of the future** (the involution excludes only the alpha-odd
ones). So the retraction's extra generality is alpha-even content: it lets the
engine EXCLUDE more readings, it does not let it MINT an alpha-odd value.
Exclusion is not selection. This is boundary-law Section 2 verbatim
("reachability-exclusion strictly contains equivariance-exclusion"), and the
containment is precisely the alpha-even part. Axis 1 collapses into Horn 2.

**Attack line 1 result: COLLAPSES.** The retraction -- the strongest candidate
-- provides no unwelded alpha-odd handle. Its cardinality-generality is
alpha-even (Horn 2); its orientation is the record arrow / the externality
mechanism, and sigma's value is its forgotten datum (Horn 1, and a confirmation
of the kill). The retraction reinforces Q2-FREE rather than reopening it.

---

## Attack line 2 -- supply-without-minting (coherence selection)

The kill equates "cannot mint" with "cannot supply." Attack line 2 proposes a
coherence/consistency constraint between two first-person structures admitting
exactly one sigma -- "record-arrow orientation must agree with retraction
orientation => fixes sigma" -- selection by constraint, not construction.

**It collapses on a grade-independent identity.** A coherence constraint between
two alpha-odd data `r`, `rho` is their product/relative sign `c = r * rho`. The
product of two alpha-odd data is **alpha-EVEN** (probe E1:
`alpha(r)*alpha(rho) = (-r)(-rho) = r*rho`). An alpha-even datum fixes only the
RELATIVE orientation (whether `r` and `rho` agree), never the ABSOLUTE value of
either: fixing `c = +1` leaves sigma (= `r` by the Q3 weld) ranging over BOTH
values (probe E2/E3, `{(+,+),(-,-)}` projects to sigma in `{+1,-1}`).

Two exhaustive sub-cases, both dead:

- If `rho` (retraction orientation) IS the record arrow -- which attack line 1
  showed -- then `c = r*rho` is the tautology `sigma*sigma = +1`. It says
  nothing, fixes nothing. This is literally the kill's own probe E2 (the co-flip
  weld invariant): the coherence-supply idea reduces to the weld the kill
  already computed.
- If one insists `rho` is a genuinely INDEPENDENT second alpha-odd coin, then
  `c = +1` fixes `r = rho`, transferring sigma's freedom to `rho` without
  sourcing it. `rho` is then an unsourced external coin -- Q3-TWO-INDEPENDENT
  territory, a second POSIT, not a standpoint-supply. To fix `rho` you
  presuppose `rho`: Horn 1, relocated.

**Attack line 2 result: COLLAPSES.** Any coherence between two alpha-odd data is
alpha-even, hence sigma-absolute-blind. Coherence selects the relative sign
(itself an alpha-even, third-person-available fact); it never supplies the
absolute value. Supply-without-minting is not available.

---

## Attack line 3 -- break the weld (residual alpha-odd d.o.f. in the record)

Q3 welds the record arrow to sigma. Is the weld tight, or is there a residual
alpha-odd d.o.f. in the record structure orthogonal to sigma?

The co-flip involution flips `(sigma, record-direction)` together and leaves the
generation count AND the register history invariant (source-packet Part C: "the
register history is invariant"). So the alpha-odd content of the record
structure is exactly one-dimensional -- the direction -- and it is welded;
everything the co-flip leaves invariant (count, register history) is alpha-even.
There is no residual alpha-odd d.o.f. orthogonal to sigma inside the record
structure. The only candidate for an orthogonal alpha-odd handle is the
retraction orientation, and attack line 1 already sent it to a horn (its
alpha-odd part = the welded direction; its extra generality = alpha-even).

**Attack line 3 result: COLLAPSES.** The weld is tight in the alpha-odd
direction; the record structure carries no unwelded alpha-odd residue.

---

## Teeth (the test can register success when it is real)

The kill would be worthless if the machinery could not fire "supply." Probe
[F] controls:

- **Non-fire (the finding):** no constraint built from the exhibited alpha-odd
  handles `{sigma, r, rho}` pins sigma non-circularly. Even-length products are
  alpha-even (cannot equal alpha-odd sigma); odd-length products are alpha-odd
  but equal sigma only by equating it to another odd handle = circular (Horn 1).
  `supplier_fires = False`.
- **Separation (not rigged):** inject a GENUINE external alpha-odd posit whose
  value is given from outside -- the machinery DOES fire `sigma := d`. But that
  is the external coin of Q2-FREE, not a standpoint-supply. So the non-fire
  above is a real finding about the standpoint's own resources, not an artifact.
- **Retraction separation:** the only sigma-reader is the forgotten up-set
  datum, unreachable to the standpoint's retraction -- so no ACCESSIBLE
  alpha-odd supplier exists.

---

## Verdict

**DEFENSE-FAILS. The Q2 kill holds; Q2-FREE is robust.** No unwelded alpha-odd
first-person feature exists at current grade; no non-circular coherence
selection supplies sigma; the standpoint-supplied door stays closed.

I close the kill's flagged seam positively, and strengthen it: **"unwelded
alpha-odd" is not a genuine third horn.** Any alpha-odd handle a standpoint could
carry is EITHER (i) welded to sigma -> Horn 1 (presupposition), OR (ii) alpha-even
in the relevant part -> Horn 2 (blind), OR (iii) an independent unsourced coin
whose only tie to sigma is a coherence constraint that is a product-of-odds =
alpha-even, fixing the relative sign but not the absolute value -- which relocates
Horn 1 (to fix the coin you presuppose it). The trichotomy is exhaustive because
alpha-parity is a grade-independent Z/2 typing: no new parity option appears at
any grade.

The three attack lines and how each collapsed:

- **AL1 (second alpha-odd handle = the retraction):** COLLAPSES, and reinforces
  the kill. Cardinality-generality is alpha-even (Horn 2); orientation is the
  record arrow / the mechanism of sigma's externality, with sigma's value the
  literal forgotten datum in the up-set the retraction cannot reach (Horn 1 +
  confirmation). The strictly-more-general engine gives MORE exclusion, not more
  selection.
- **AL2 (coherence supply):** COLLAPSES on the grade-independent identity that a
  coherence between two alpha-odd data is alpha-even -- it fixes the relative
  sign only. Reduces to the kill's own probe E2.
- **AL3 (residual record d.o.f.):** COLLAPSES. The record structure's alpha-odd
  content is exactly the welded direction; count and register history are
  alpha-even. No orthogonal alpha-odd residue.

**What remains standpoint-supplied (unchanged from the kill):** the DEMAND that
a definite value exist (symmetry-breaking residual, boundary-law leg b); the
HOST/LOCUS at which the value registers; and -- now sharpened by the retraction
reading -- the retraction is the very act of directed forgetting that FORCES
sigma's externality by placing its value in the unreachable up-set. The first
person forces externality; it does not fill the value.

---

## The one residue (named once)

The identification "retraction orientation = the sigma-welded record arrow" is
made at fixture/structural grade: both are the arrow of record accumulation /
causal accessibility, and TaF's retraction orientation is the accessibility
direction. There is **no operator-grade base-uniting map** joining the TaF
causal-past retraction to GU's K_S-flip involution on one base -- this is Q3's
own missing lemma (the base-uniting operator sending oddness-constraint to
orientation-coin) and the involution-typing doc's residue (the lift where
`A*(R)` retains partial coarse future information). Were that map built, it must
be checked that it sends the retraction orientation to the sigma-welded arrow
(predicted by the parity argument; not machine-verified at operator grade).

This is a **stability check, not a reopener.** The defense's collapse is
grade-independent: alpha-parity is a Z/2 typing, and the trichotomy
(welded-odd / even / unsourced-coin-with-even-coherence) is exhaustive at every
grade. The involution-typing doc already predicts the relevant coincidence "only
gets HARDER" under the partial-future lift. So the residue does not license
DEFENSE-INCONCLUSIVE; it is the single lemma whose construction would let a
future pass CONFIRM (not overturn) the weld at operator grade.

---

## Boundary

Exploration tier under the standing axiom, R0_COND. One new artifact + one probe
(`tests/channel-swings/q2_defense_attorney_probe.py`, exit 0, foreground,
deterministic, double-run byte-identical). This document DEFENDS the killed
hypothesis and finds the defense fails; it moves nothing. No edits to LANE-STATE,
research-portfolio, NEXT-STEPS, any claim/canon/verdict/ledger file, or any other
agent's artifact (including the Q2 kill doc -- the directing agent adds any
banner). GU and the cross-repos (temporal-issuance, time-as-finality) touched
READ-ONLY. No commit/push, no external actions. The externality of sigma remains
the program's closed premise (p2c-owned per the tri-repo signed-graph); this pass
confirms the retraction is the mechanism of that externality, not a defeater of
it. The finite Z/2 / idempotent-toy probe is a faithful model of the structural
facts (product-of-odds is even; the retraction forgets the sigma-bearing up-set;
idempotency's toward-image orientation is alpha-even); the operator-grade and
proof-grade content it stands on lives in the cited Q2 / Q3 / boundary-law /
involution-typing receipts, consumed not re-run.
