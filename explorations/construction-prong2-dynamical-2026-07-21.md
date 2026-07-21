---
title: "CONSTRUCTION swing PRONG 2 (DYNAMICAL): POSIT sigma = the self-consistent fixed point of the record-issuance loop Phi (S->I->O->S closure), build the picture, gate at the back. RESULT: the fixed-point count is NEVER UNIQUE -- MULTIPLE (2) in the trivial-holonomy / no-flip closure (sigma free), NONE (0) in the nontrivial-holonomy / flip closure (Godel/diagonal obstruction), and WHICH closure is itself sigma. UNIQUE -- the only count that would overturn static 'can't-supply' -- is STRUCTURALLY IMPOSSIBLE, because Phi's one-loop action is the fixpoint-free holonomy involution alpha (the same alpha that powers the static kill), and a rank-1 Z/2 local system has no unique global section (this IS the TI H^1(finality sheaf) computation: fixed point exists iff holonomy trivial iff H^1 obstruction vanishes; uniqueness never). PUSH/PULL/SELF-CONSTITUTE verdict: SELF-CONSTITUTE FAILS; sigma is PUSHED at the seed (external write) and PULLED thereafter (carried as an alpha-odd, internally-unreadable token via the co-flip weld). The dynamical case does NOT reopen self-supply -- it re-confirms externality, now as a Lawvere fixed-point count rather than a Schur map-blindness. Gated at operator grade on the SAME product-uniformity theorem as the static leg. Planted deterministic-closed control CAUGHT (constant default = alpha-even = zero mutual info with true sigma); teeth (external oracle) fire."
status: active_research
doc_type: exploration
created: 2026-07-21
mode: CONSTRUCTION/posit-declared
prereg: explorations/prereg-construction-swing-posit-sigma-cycle-2026-07-21.md
outcome: DYN-NO-REOPEN (posit-productive for the trichotomy; posit-contradicted for self-supply)
inputs:
  - explorations/prereg-construction-swing-posit-sigma-cycle-2026-07-21.md
  - explorations/shard-cycle-prong2-dynamics-gorard-2026-07-21.md
  - explorations/decision-tree-Q2-sector-bit-forced-free-supplied-2026-07-21.md
  - explorations/decision-tree-Q2-defense-attorney-2026-07-21.md
  - explorations/oracle-relative-externality-substantiveness-HV-2026-07-21.md
  - explorations/boundary-law-operator-lift-2026-07-20.md
  - explorations/diagonal-boundary-unification-2026-07-20.md
  - "READ-ONLY temporal-issuance: DRIVING-HYPOTHESIS-OBSERVER-ISSUANCE.md (H1 finality sheaf), formal/lean/OnlineIssuance/BoundaryInvolution.lean"
runnable:
  - tests/channel-swings/construction_prong2_dynamical_probe.py
probe_exit: 0
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_actions: none
---

# Prong 2 (dynamical): is sigma the fixed point the record-issuance loop settles?

## MODE (binding, read first)

CONSTRUCTION, not derivation. The POSIT is DECLARED and kept labeled throughout;
it is NEVER re-reported as "we derived sigma." The gate is at the BACK: does the
built picture force INDEPENDENT consequences (things not inserted) that VERIFY
against banked facts? A contradiction with a banked fact KILLS the posit.

> **THE DECLARED POSIT (P3).** sigma is CONSTITUTED as the self-consistent FIXED
> POINT of the evolving record-issuance loop `S -> I -> O -> S` -- supplied by the
> dynamics as the loop closes, NOT read from a static state. Record-issuance is a
> dynamical SELF-MAP `Phi` (the loop's one-step closure / one full traversal), and
> sigma is a fixed point of `Phi` (the closure orientation the loop settles on
> self-consistently).

This directly takes up Joe's static-vs-dynamic point: the program's "the inside
can't supply sigma" was proven for STATIC maps / observables / standpoints
(Q2-FREE, the oracle-relative zero-capacity, the boundary-law no-invariant-
valuation). Whether the DYNAMICS can self-constitute sigma was left OPEN (the
Q2 defense-attorney seam; the Lawvere leg-a self-closure). This prong builds the
dynamical picture and counts the fixed points.

Receipt: `tests/channel-swings/construction_prong2_dynamical_probe.py` --
deterministic (double-run byte-identical), pure enumeration, no RNG, no network,
**exit 0**, HEADLINE `11 [E] + 2 [F] = 13 :: FIXED-POINT COUNT never UNIQUE`.

---

## 1. The dynamical model, built faithfully

The carrier is the shard-cycle issuance loop as the prior prong typed it
(`shard-cycle-prong2-dynamics-gorard-2026-07-21.md`): record-issuance = hypergraph
/ string rewriting; the token order is an **acyclic helix** winding forward
forever (each pass mints fresh records at a higher issuance index); the map that
forgets the winding number sends the helix onto the oriented 3-cycle
`S -> I -> O -> S`. I add exactly one datum -- the POSIT's handle -- and nothing
else:

- A token carries `(shard_type, orientation, record_dir, gen_count, issuance_index)`.
- Each rewrite `S->I`, `I->O`, `O->S` mints a **fresh token** (the helix;
  `issuance_index` strictly increases, closure-independent -- the model's global
  arrow).
- The `O->S` seam is the **null stratum** (`q<0`, `K_S` null, ~8% of ends, the
  DeWitt `q=0` genesis seam): the place a fresh record is minted and the
  **closure** is applied. Prong A located two **isospectral closures** there;
  the POSIT inserts sigma as *which* closure the loop takes:
  - **NO-FLIP** closure = **trivial holonomy** `h=0`: orientation and record_dir
    pass through unchanged. Realizes `+K_S`.
  - **FLIP** closure = **nontrivial holonomy** `h=1` = the **K_S-sign involution
    alpha**: orientation and record_dir **co-flip together** (Q3's co-flip weld),
    `gen_count` invariant. Realizes `-K_S`.

`Phi` := the orientation self-map induced by ONE full `S->I->O->S` traversal.
This is a genuine dynamical loop, not an `op` written on `Z/2` by fiat: the probe
runs the rewriting and reads `Phi` off the trajectory.

The POSIT is now DECLARED and located. Everything below is the back-gate.

---

## 2. THE DECISIVE COUNT: how many fixed points does Phi have?

Run the loop (probe [1]):

| closure | holonomy | `Phi` on `{+1,-1}` | fixed points | count |
|---|---|---|---|---|
| NO-FLIP | `h=0` (trivial) | `{+1: +1, -1: -1}` (identity) | `{+1, -1}` | **MULTIPLE (2)** |
| FLIP | `h=1` (= alpha) | `{+1: -1, -1: +1}` (negation) | `{}` | **NONE (0)** |

**The count is NEVER UNIQUE.** And the two counts are not on an equal footing
with a third missing case -- they are *exhaustive*, because on a two-element
orientation fiber the one-loop holonomy is a `Z/2` element and there are only two:
identity (2 fixed points) or the free involution (0 fixed points). **UNIQUE (==1)
is structurally impossible.** This is the whole result, and it is forced, not
inserted.

### 2.1 Why UNIQUE cannot occur -- the same alpha that kills the static case

`Phi` in the FLIP closure IS the fixpoint-free involution `alpha` (the K_S-sign
flip). Its fixpoint-freeness is the exact fact the static boundary-law kill rides
on: `alpha` has a fixed point iff `K_S = -K_S` iff `K_S = 0`, excluded by
Krein-nondegeneracy (`boundary-law-operator-lift`, `no_invariant_valuation`). So
the dynamical regime does **not** escape the static obstruction; it **inherits**
it. A self-map whose one-loop action is a fixpoint-free involution has no fixed
point at all in that sector, and the identity in the other. The dynamics carry
`alpha`'s oddness forward; they do not dissolve it.

### 2.2 The count IS the H^1(finality sheaf) computation (TI bridge)

The orientation is a **rank-1 `Z/2` local system** on the issuance loop; the
one-loop holonomy is `h in Z/2`. A **global section** of that local system is an
orientation consistent around the loop: `v == (-1)^h * v`. Section-counting =
fixed-point-counting (probe [3], matches exactly):

- `h=0`: `v==v`, **2 sections** -- the gluing obstruction **`H^1` VANISHES**
  (third-person well-definedness), and there are two consistent global
  orientations. MULTIPLE.
- `h=1`: `v==-v`, **0 sections** -- **`H^1` is NONZERO**; no consistent global
  orientation exists. NONE.

This is precisely the TI apparatus (`DRIVING-HYPOTHESIS-OBSERVER-ISSUANCE.md`:
"shared reality is the global section of finalized bindings, existing iff `H^1`
of the finality sheaf vanishes"; and the prior prong's exact triple **causal
invariance <=> branches agree <=> `H^1`(finality sheaf)=0**). The construction
adds the sharp corollary: **a rank-1 `Z/2` local system NEVER has a unique global
section** -- `H^1=0` gives `|fiber|=2` sections, `H^1 != 0` gives `0`. So sigma =
the **holonomy/monodromy datum** of the orientation local system around the loop,
which is exactly a degree-1 cohomology class **external to the loop's local
dynamics** -- the very thing self-consistency does not fix. This re-derives, by a
dynamical route, the banked "Krein sign reduces to one external `Z/2` posit."

### 2.3 The steelman for UNIQUE, and why it collapses (defense attorney)

Best case for self-supply: enrich the state, couple orientation to record_dir,
and impose a self-consistency constraint "the arrow after one loop must agree with
the arrow it started with." In the FLIP sector `arrow -> -arrow`, so `arrow ==
-arrow` has NO solution (NONE); in the NO-FLIP sector any arrow works (MULTIPLE) --
the same trichotomy. The coupling cannot rescue uniqueness because the coupling
datum `orientation * record_dir` is a **product of two alpha-odd data = alpha-EVEN**
(probe [2]; this is exactly `Q2-defense-attorney` AL2): it fixes only the RELATIVE
sign, never the ABSOLUTE value. **UNIQUE is robustly absent under the steelman.**

### 2.4 Where it is gated

At **fixture grade** the count is a finite, exact enumeration (probe, exit 0):
theorem-grade for the finite model. Its **operator-grade** lift -- whether `Phi`
is a bounded self-map on the doubled product carrier `A x A` where the closure
map lives -- rides on the SAME open theorem as the static Lawvere leg:
**product-uniformity of the norm-resolvent boundary value**
(`boundary-law-operator-lift` Section 1c). Point-surjectivity bottoms out there;
so does the fixed-point count. Said plainly: the dynamical fixed-point count is
gated at operator grade on exactly the product-uniformity theorem the prereg
flagged, no new gate.

**Fixed-point count: NEVER UNIQUE -- MULTIPLE (h=0) or NONE (h=1), and which is
itself sigma.** The one count that would overturn static "can't-supply" does not
occur.

---

## 3. PUSH vs PULL vs SELF-CONSTITUTE (the model distinguishes all three)

The read/pull-and-comprehend direction is banked-blocked (zero inward capacity,
oracle-relative zero-capacity / prong I Schur). Given the fixed-point count, the
model separates the three ways the bit's VALUE could enter (probe [4]):

- **SELF-CONSTITUTE** (the loop settles the value): requires a fixed point that is
  BOTH **unique** AND **alpha-equivariant** (its value co-varies with the true
  sigma). The fixed-point *structure* is alpha-symmetric in BOTH closures (flip
  maps the fixed-point set to itself: `{+,-}->{-,+}` = same set; `{} -> {}` = same
  set), and the count is never 1. **SELF-CONSTITUTE does NOT fire.**
- **PULL** (opaque token the system can't read): the orientation is **carried** as
  a token in every state, but every internal / third-person read map is **alpha-even**
  (`f(-o)=f(o)`), and **zero** alpha-even maps recover the orientation (probe [4]:
  `even_readers = 0`). The co-flip weld makes the orientation an **alpha-odd
  section** the internal algebra cannot resolve -- an FHE-witness-like opaque token.
  This fires: the loop HOSTS sigma without reading it.
- **PUSH** (environment writes): an external seed sets the orientation, and the
  loop transports it unchanged in the trivial-holonomy sector (probe [4]:
  `+1 -> +1`, `-1 -> -1`). This fires at the seed: the ABSOLUTE value is written
  from outside the loop.

**Verdict: PUSH + PULL, NOT SELF-CONSTITUTE.** The value is PUSHED at the seed
(an external write of the initial orientation / the null-stratum prescription --
"an external prescription is required there") and PULLED thereafter (carried as an
alpha-odd token the internal alpha-even reads cannot comprehend, via the co-flip
weld). The loop **hosts and transports** sigma; it neither reads nor creates it.
This is the dynamical restatement of Q2-FREE's "the first person HOSTS sigma and
FORCES its externality; it does not supply the value" -- now with HOST = the loop's
carrier and the FORCING = the fixpoint-free holonomy.

---

## 4. INDEPENDENT consequences (tagged; verified against banked facts)

Separating what the posit FORCES but did NOT insert (independent) from what merely
restates it. Four candidates, each checked against Q2-FREE, Q3, one-global-arrow,
and the ~8% null stratum.

**IC-1 (INDEPENDENT, VERIFIED) -- the global arrow is the alpha-EVEN issuance
index, distinct from the alpha-odd sigma-welded record direction.** The posit welds
`record_dir` to sigma (co-flip, alpha-odd), so in the flip sector `record_dir`
reverses each loop. But the **issuance_index** climbs monotonically **regardless of
closure** (fresh tokens, higher index -- probe asserts `idx` strictly increases in
both closures). So the construction FORCES two distinct arrows: (i) the global,
monotone, **alpha-even** issuance arrow, and (ii) the sector-dependent, **alpha-odd**
sigma-welded `record_dir`. I did not insert this split; the loop produces it.
Check against **one-global-arrow** (banked): the single global arrow is located in
the alpha-even issuance monotonicity, NOT in the alpha-odd orientation -- so
one-global-arrow is fully COMPATIBLE with a sector-dependent orientation, and the
posit independently REINFORCES it by naming *which* arrow is the global one.
**VERIFIED (no contradiction; reinforces one-global-arrow).**

**IC-2 (INDEPENDENT, VERIFIED) -- a record-RATE / frequency relation.** Records
accumulate at 1 per type-step (3 per loop). In the FLIP sector the orientation is
a genuine period-2 orbit (`Phi = alpha`, no fixed point): its period is **two
loops = six type-steps**, i.e. the orientation's frequency is **half** the loop-
closure frequency, while record accumulation is monotone at full rate. The posit
FORCES: sigma is a `Z/2`-graded, half-frequency decoration on a monotone record
flow -- it cannot beat at the record rate. Check against **one-global-arrow** and
the helix: VERIFIED -- the arrow keeps its full-rate monotonicity; only the
alpha-odd decoration halves. (Independent of anything inserted: I inserted the
closure, not the frequency ratio; the ratio falls out of the 3-step loop vs the
period-2 involution.) **VERIFIED.**

**IC-3 (INDEPENDENT, VERIFIED) -- non-uniqueness <=> the null seam re-frees the
orientation.** The `O->S` seam mints a FRESH token, so NO causal edge is written
across it (prior prong: the null stratum is exactly where no causal direction is
written; "sigma undefined at the null stratum"). This fresh-token seam is what
makes the closure a *re-seeding* rather than a *fixed determination*: the
orientation is re-freed each loop instead of being pinned. So **fixed-point
non-uniqueness and the existence of the null seam are the same fact** -- the seam
is the locus where `Phi`'s determination of sigma is reset. Check against the
banked null stratum (`q<0`, `K_S` null, ~8%, "an external prescription is required
there"): VERIFIED -- the seam is precisely where the external prescription
(PUSH) enters, and that is why the count is never unique. **VERIFIED (qualitative).**
*Honest scope:* the construction forces the qualitative link (non-uniqueness <=>
null seam re-freeing); it does **NOT** force the quantitative `~8%` number -- that
fraction has its own derivation and is not reproduced here. Not inflated to a
numeric prediction.

**IC-4 (RESTATES-adjacent, VERIFIED-weak) -- the three generations are alpha-EVEN
spectators of the flow, not graded pieces of it.** The co-flip leaves `gen_count`
invariant (probe [2]); the closure flow does not act on generations. So the posit
FORCES that the generation structure is an alpha-even spectator of the orientation
dynamics -- the flow cannot read or move it. This is CONSISTENT with Q3 (generation
deck-admissibility is a different `Z/2` on the internal `S^3` fiber, DE-sign-blind)
but it does **NOT** derive the count `{1,3}`. Honest tag: this is closer to a
restatement of the co-flip weld than an independent forcing; it earns VERIFIED only
as a consistency check, and I explicitly do **not** claim "generations fall out of
the flow." **VERIFIED-weak (consistency, not forcing).**

No consequence CONTRADICTS a banked fact. The strong independent yield is IC-1
(the two-arrow split, reinforcing one-global-arrow) and IC-3 (non-uniqueness <=>
null seam); IC-2 is a genuine but mild frequency relation; IC-4 is a consistency
check named honestly as near-restatement.

---

## 5. The planted control (deliberately WRONG posit) -- and the catch

Per the prereg discipline, plant a DELIBERATELY-WRONG posit and confirm the
back-gate CATCHES it: **a DETERMINISTIC, CLOSED dynamics with sigma NOT in the
initial state, claiming to self-supply sigma via a "unique fixed point."**

Model (probe [5]): seed orientation UNSET (symmetric, sigma absent); a
deterministic closed rule drives to a HARDCODED default (`+1`) every step. It DOES
have a unique fixed point (`+1`) -- superficially the UNIQUE case that would
"self-supply." **The gate catches it:** a genuine supplier must be
**alpha-EQUIVARIANT** (its output co-varies with the true world-bit); the closed
deterministic default is **alpha-EVEN / constant** -- it outputs `+1` in the
`sigma=+1` world AND in the `sigma=-1` world, so its **mutual information with the
true sigma is 0 bits**. `supplier_fires = False`. **CAUGHT.**

The reason is the information law the prereg names: deterministic evolution with
sigma absent from the seed is a function of a sigma-free trajectory, hence constant
in sigma (alpha-even), hence -- by the blindness lemma -- cannot output the
alpha-odd sigma. A "unique fixed point" that is a hardcoded default is an external
write **smuggled into the RULE by its author**, not a closed self-supply. So
UNIQUE self-supplies sigma **only if** the fixed point is *also* alpha-equivariant;
uniqueness alone is a disguised PUSH.

**Teeth** (probe [6]): a genuine EXTERNAL oracle (returns the true world-bit,
alpha-equivariant) DOES fire -- `mutual info = 1 bit`, `supplier_fires = True`.
This shows the gate is not vacuous: it registers real supply when it exists -- and
that supply is EXTERNAL (oracle / push), never closed self-supply. The control
fails exactly where it should and the teeth bite exactly where they should, so
"the dynamics do not self-supply sigma" is a real finding about the loop's own
resources, not an artifact of a permissive test.

---

## 6. Verdict: does the dynamical case reopen self-supply?

**No. `DYN-NO-REOPEN`.** The dynamical construction is POSIT-PRODUCTIVE (it forces
the never-unique trichotomy and the two-arrow split, both verified) but
POSIT-CONTRADICTED on its self-supply claim (the loop's fixed-point count is
never unique, so sigma is not constituted by the dynamics). The static-vs-dynamic
gap Joe named is now CLOSED on the construction side, in the same direction as the
static result:

- **Fixed-point count = NEVER UNIQUE.** MULTIPLE (2) in the trivial-holonomy /
  no-flip closure (sigma a free choice among two global sections); NONE (0) in the
  nontrivial-holonomy / flip closure (Godel/diagonal obstruction, no consistent
  global orientation); and WHICH closure is itself sigma. UNIQUE -- the only count
  that would overturn static "can't-supply" and FORCE sigma -- is structurally
  impossible for a rank-1 `Z/2` local system, blocked by the SAME fixpoint-free
  holonomy `alpha` that powers the static kill. Gated at operator grade on the
  same product-uniformity theorem.
- **PUSH + PULL, NOT SELF-CONSTITUTE.** sigma is PUSHED at the seed (external
  prescription at the null-stratum genesis) and PULLED thereafter (carried as an
  alpha-odd, internally-unreadable token via the co-flip weld). The loop hosts and
  transports sigma; it neither reads nor mints it.
- **Independent consequences, all VERIFIED (none contradicts):** IC-1 the global
  arrow is the alpha-even issuance index, distinct from the alpha-odd sigma-welded
  record direction (reinforces one-global-arrow); IC-2 a half-frequency record-rate
  relation on the orientation orbit; IC-3 fixed-point non-uniqueness <=> the null
  seam re-frees the orientation (qualitative, not the ~8% number); IC-4 generations
  are alpha-even spectators of the flow (consistency, near-restatement -- named
  honestly).
- **Planted control CAUGHT; teeth fire.** A deterministic closed default is
  alpha-even (0-bit) and is caught as a non-supplier; a genuine external oracle
  (equivariant, 1-bit) fires -- confirming the gate has discriminating power.

**Net:** the dynamical regime does NOT reopen self-supply. It re-confirms sigma's
externality by a NEW route -- a Lawvere/point-surjectivity **fixed-point count**
(never unique) and a **`Z/2` holonomy / `H^1`(finality sheaf)** reading -- rather
than the static Schur map-blindness. Same conclusion, second independent mechanism.
The one honest residue is operator-grade: the count is theorem-grade at fixture and
rides on the product-uniformity theorem one level up, exactly as the static leg
does -- no new gate, no reopener.

---

## 7. Boundary

Exploration tier; CONSTRUCTION mode, posit declared and kept labeled throughout;
NEVER reported as a derivation of sigma. One new artifact + one foreground probe
(`tests/channel-swings/construction_prong2_dynamical_probe.py`, exit 0,
deterministic, double-run byte-identical, pure enumeration, no RNG, no network).
This document moves nothing: no edits to LANE-STATE, research-portfolio,
NEXT-STEPS, any claim / canon / verdict / ledger / portfolio file, or any other
agent's artifact. GU otherwise read-only where cited; the cross-repos
(temporal-issuance) touched READ-ONLY. No commit / push, no external actions.
`claim_status_change: none`, `canon_verdict_change: none`,
`public_posture_change: none`. The externality of sigma remains the program's
closed premise (p2c-owned per the tri-repo signed-graph); this construction
supplies a second, dynamical mechanism for that externality (the fixpoint-free
holonomy / never-unique fixed-point count), not a defeater of it. The finite
`Z/2` / rewriting-loop probe is a faithful model of the grade-independent
structural facts (fixpoint-freeness of alpha, the co-flip weld's alpha-oddness,
the rank-1 `Z/2` local-system section count, the deterministic-closed blindness);
the operator-grade content it stands on lives in the cited boundary-law / Q2 /
oracle-relative receipts, consumed not re-run.
