---
title: "Decision tree Q2 (sigma): is the sector bit FORCED, FREE, or STANDPOINT-SUPPLIED? -- VERDICT Q2-FREE. The FORCED test fails against W211's proof-grade Godel-independence (positivity/unitarity/record-conservation are all provably sigma-blind; W235's positivity-forces-unique-grading forces the RECORD structure and C-given-B, never the sector value). The record-arrow access is DIFFERENT from sector-reading (a section, not an alpha-even map, so the blindness lemma does not forbid it) -- which is the ONLY way STANDPOINT could survive -- but it then FAILS the hard circularity check on an exhaustive dichotomy: a standpoint defined WITH the arrow presupposes sigma (the co-flip weld makes 'having the record arrow' = 'having-already-chosen sigma' -> reads), and a standpoint defined WITHOUT it is the alpha-even self-encoding (L1) structure, which cannot MINT an alpha-odd value (blindness again -> does not supply). The first person HOSTS sigma and FORCES its externality (inside-ness -> outside-ness); it does not supply sigma's value. The DE sign is a free (discrete, exactly-located, record-welded) parameter"
status: active_research
doc_type: exploration
created: 2026-07-21
program: explorations/prereg-three-object-decision-tree-2026-07-21.md
outcome: Q2-FREE
axiom: lab/process/boundary-adapter-standing-axiom.md
inputs:
  - explorations/prereg-three-object-decision-tree-2026-07-21.md
  - explorations/decision-tree-Q3-one-anchor-vs-two-2026-07-21.md
  - explorations/W211-krein-sign-godel-independent-five-method-synthesis-2026-07-14.md
  - explorations/W235-central-bit-mirror-record-vs-redundancy-2026-07-15.md
  - explorations/blockbuster-p3-one-bit-dossier-v2-2026-07-19.md
  - explorations/source-packet-coflip-holonomy-freeze-2026-07-20.md
  - explorations/CONJECTURE-source-action-is-the-observer-2026-07-11.md
  - explorations/diagonal-boundary-unification-2026-07-20.md
  - explorations/boundary-law-operator-lift-2026-07-20.md
runnable:
  - tests/channel-swings/q2_sector_bit_standpoint_probe.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_actions: none
---

# Q2: is the sector bit sigma FORCED, FREE, or STANDPOINT-SUPPLIED?

Adversarial truth-test, not advocacy. The CLOSED PREMISE holds: sigma is
external -- I do not re-derive that. Q2 asks HOW the Z/2 is fixed: by an
internal necessity (FORCED), as a genuine coin (FREE), or legitimately by
the first-person / excluded-reading structure (STANDPOINT-SUPPLIED).

**Verdict up front: Q2-FREE.** sigma is a genuine free Z/2 coin. The FORCED
test fails against W211 (confirmed, not overturned). STANDPOINT-SUPPLIED
survives the blindness objection (the record-arrow access is genuinely
DIFFERENT from sector-reading) but then FAILS the hard circularity check on
an exhaustive two-horn dichotomy: the first person HOSTS sigma and FORCES its
externality, but it does not SUPPLY sigma's value. The DE sign is a free
parameter -- discrete, exactly located, and welded to the record arrow, but
free.

Receipt: `tests/channel-swings/q2_sector_bit_standpoint_probe.py` --
deterministic, numpy only, no network, exit 0, HEADLINE
`5/5 [E] PASS + 1/1 [F] FIRE -> ALL PASS`.

---

## 1. What sigma is now (from Q3), stated precisely so the test is well-posed

Q3 re-typed sigma exactly and I take that typing as fixed input:

- **sigma = the orientation of the Krein form** `K_S` on the (9,5) spine /
  habitat fiber `F = GL(4,R)/O(3,1)` (`pi_1(F) = Z/2`); the value set is
  `{+K_S, -K_S}`.
- **What sigma fixes:** the physical sector and the **DE sign**
  `sgn(w_0+1) = eps` (blockbuster P1 readout identity).
- **The co-flip weld (Q3's honest one-bit result):** the holonomy involution
  over `F` flips sigma AND the **record arrow** together
  (`sector(act E c) = -sector c AND dir(act E c) = -dir c`), leaving the
  generation count untouched. So **sigma <-> record arrow** are two costumes
  of ONE alpha-odd datum, where `alpha` is the `K_S`-sign flip.

The first person has the record arrow (its own direction of record
accumulation). So it appears to have a handle on sigma. That apparent handle
is the whole crux of the STANDPOINT test in Section 4.

---

## 2. The FORCED test, confronted against W211

FORCED requires a named internal necessity that forbids one value of sigma:
positivity, unitarity, record-conservation, or anomaly cancellation. I test
each and confront the strong prior (W211 Godel-independence).

### 2.1 W211 is proof-grade and it says the opposite of FORCED

W211 is a five-method unanimous result: the C-grading sign is
**Godel-independent** of GU's good-stable structure. Five different notions
of "compute inside GU" -- counterfactual-invariance (R16), Dirac-BRST
cohomology (R9), Lawvere fixed-point (R7), topos internal logic (R12),
Helmholtz variational reconstruction (R1) -- each reproduce the same positive
control (the full group forces the ungraded `eta` by Schur, nulldim 1) and
each find the same reason the sign escapes: **conditioning on the good stable
splits the frame into the two C-blocks under the maximal-compact stabilizer
`SO(9) x SO(5)`, growing the invariant-form space from dim 1 to dim 2, which
LIBERATES the relative-block sign as a free Z/2.** "Compute harder inside GU"
is ruled out by proof, because each method is a different sense of "compute
inside GU" and all five leave the SAME bit free.

That is the anti-FORCED prior at proof grade. To land FORCED I would have to
exhibit a mechanism all five methods missed. I cannot, and the following
shows why each candidate necessity is provably sigma-blind.

### 2.2 Positivity / unitarity are sigma-blind (probe E5; W235 read correctly)

The subtle point is W235, which looks like it might rescue FORCED. W235 (with
W228) sharpens W211: **positivity forces the C-grading UNIQUE** at the
kinematic stabilizer (grading-sign moduli = 0), which killed W211's naive
"free symmetric bit" reading. Does that force sigma? **No -- it forces a
different object.**

- W235 forces that the mirror Z/2 is a **RECORD** (an operative superselection
  grading) rather than a **REDUNDANCY** (a gauge artifact), via three
  Y14-independent legs (KT-not-exact, gauge-transverse, forced-unique
  grading). This forces that there IS a genuine sector structure to choose
  in -- it does not force WHICH sector.
- The "forced-unique grading" fixes `C` **given the anchor `B`**, not `B`
  itself. The dossier's D1 build makes this exact: "anchor flip `B -> -B`
  gives `C -> -C` exactly -- the co-flip at interacting grade," and the
  Z/2-typed choice set is exactly `{(B,C), (-B,-C)}` (P11/P12). Positivity
  picks the grading operator relative to a fixed record labelling; the pair
  `(record labelling, grading)` still has a free overall sign = sigma.
- Probe E5: the graded physical inner product `|eta.C|` is positive-definite
  for **both** sigma sectors (they are mirror images). Unitarity -- a
  positive-definite physical inner product -- admits both. Positivity and
  unitarity are blind to sigma.

So W235 REINFORCES FREE rather than rescuing FORCED: it forces the Z/2 to be
a genuine free coin (a real superselection choice), not a redundancy, while
leaving the value external and Kramers-blind. The source-packet freeze states
the same conclusion independently: no `J_quat`-commuting GU-native operator
reads the sector (Kramers blindness, canon no-go); "the value remains the one
external Z/2 posit."

### 2.3 Record-conservation and anomaly cancellation are sigma-blind

- **Record-conservation:** the record current is conserved in both sectors;
  the co-flip flips the current sign but conservation holds either way
  (source-packet Part C: charge and record current flip sign under the
  holonomy; the register history is invariant). Conservation locates the
  structure, never the sign -- the torsor lens of the diagonal-boundary family
  states it verbatim: "conservation can locate a coset, never a map."
- **Anomaly cancellation:** the one genuinely one-sided constraint in the
  neighborhood is the generation anchor's deck-admissibility Z/2 (`q(-v) =
  -q(v)`), and Q3 PROVED that is NOT sigma -- it is a different order-2 datum
  on the internal `S^3` fiber, controlling count-admissibility, DE-sign-blind.
  So the existence of a one-sided constraint elsewhere does not touch sigma;
  sigma itself is a free coin (both values structurally admissible -- exactly
  W211's liberation).

### 2.4 The one honest residual, and why it cannot land FORCED for sigma

W211 and W235 both name a dynamical-grade opening: the unbuilt `F_A` on
`Y14` closing `C2`. Could a future dynamical stabilizer force sigma? **No,
not the VALUE.** The dynamical `F_A` bit is the RECORD-vs-REDUNDANCY bit
(`theta`), not sigma's value. Its two outcomes are: `theta = 0` -> the Z/2 is
a genuine record (sigma stays a free coin over a real superselection); `theta
!= 0` -> the Z/2 dissolves into a redundancy (sigma becomes a non-object, not
a forced value). Neither outcome forces WHICH sector obtains. Building `F_A`
can confirm sigma is a real free coin, or vacate the question, but it cannot
mint sigma's value -- because the native cores are spectrally sign-blind
(W235 Section 3: they commute with the grading, cannot source the pairing).
So FORCED is robustly dead for sigma's value at every grade the sources
reach.

**FORCED verdict: FAILS.** No positivity / unitarity / record-conservation /
anomaly necessity forbids either value of sigma; W211's Godel-independence is
confirmed and W235's positivity-forcing forces the record STRUCTURE and
`C`-given-`B`, never the sector VALUE.

---

## 3. The same-vs-different-access question (the crux, resolved)

Q3 gives the tension in its sharpest form:

- The first person HAS the record arrow, and sigma <-> record arrow. So the
  first person seems to have a handle on sigma.
- The boundary law (diagonal-boundary / excluded-reading) says the first
  person is EXCLUDED from reading the sector: the excluded-reading class is
  the alpha-EVEN class, sigma is alpha-ODD, and no alpha-even map computes an
  alpha-odd datum (blindness = evenness). The first person is BLIND to sigma.
- Blindness to X is incompatible with SUPPLYING X. If "having the record
  arrow" and "reading the sector" were the SAME access, blindness and
  record-access would contradict, and one must give.

**Resolution: the two accesses are DIFFERENT.** This is decisive and it is
what keeps STANDPOINT alive long enough to face the circularity check.

- **Sector-reading** is an alpha-EVEN MAP `A -> B` applied to determine sigma.
  The boundary-law blindness lemma is a statement about MAPS: every internal
  reading map is alpha-even, sigma is alpha-odd, an even map cannot output an
  odd value. Probe E1: zero even maps recover sigma. **Reading is impossible.**
- **Record-arrow-possession** is a SECTION -- a choice of lift in the Z/2
  torsor, not a function on states. The blindness lemma does not constrain
  lifts (probe E3: every even map is blind to the lift; a section evades a
  maps-only lemma). And the boundary law's OWN second conclusion says exactly
  this: leg (b), the symmetry-breaking residual, is "no alpha-invariant
  valuation exists, so every definite valuation the observer commits to is a
  symmetry-breaking selection." Committing a definite record arrow IS an
  alpha-breaking selection. Reading (an even map) and selecting (an odd lift)
  are the two different legs of the same parent -- they do not contradict.

So the boundary-law exclusion and the record-access do NOT contradict: the
first person is blind to sigma **as a map to read** while being dressed with
sigma **as a lift it has selected**. Different fibration of the same alpha-odd
object: one is `Hom(A, B)` (empty on the even part), the other is a point of
the `B`-torsor (a broken-symmetry section). This is the DIFFERENT-access horn,
and it is the only door through which STANDPOINT-SUPPLIED could walk.

---

## 4. The hard circularity check (STANDPOINT-SUPPLIED, steelmanned then broken)

Different access means the first person could, in principle, SUPPLY sigma via
the record-arrow lift while being BLIND via sector-reading. Now the decisive
question: is possessing that lift SUPPLYING sigma (the standpoint is defined
independently of sigma and then fixes it) or READING it (sigma must already be
fixed for the standpoint to exist -- circular)?

### 4.1 Steelman STANDPOINT-SUPPLIED at full strength

The strongest supply story is the CONJECTURE-source-action addendum's
five-systems architecture: the observer is inside as substance and
consequence, "constitutively outside as the source of exactly one datum the
inside provably cannot mint." The standpoint is defined by L1 (self-encoding
admissibility: the system contains its own describers) -- a record-BEARING
structure, definable WITHOUT specifying which sigma. To be an ACTUAL observer
you must have a definite record arrow (you cannot accumulate records in no
direction), and THAT act of committing an arrow is the symmetry-breaking
selection that fixes sigma. FLP makes it precise: deterministic consensus is
impossible from inside (blindness); the tie-break is an INDEXICAL ("arrival
order at MY node") supplied by occupying a node, not read from the network.
The indexical is not "already chosen"; it is constituted by the standpoint.
On this reading the standpoint is prior to sigma and occupying it CONSTITUTES
sigma -- genuine supply, and the elegant result the whole program points at.

### 4.2 The break: an exhaustive dichotomy, neither horn supplies

The steelman requires two things to BOTH hold: (i) the standpoint is defined
independently of sigma; (ii) occupying it CONSTITUTES (not presupposes) the
choice of sigma. Define the standpoint either WITH or WITHOUT the arrow --
exhaustive, since defining a standpoint must either fix the alpha-odd lift or
not.

- **Horn 1 -- standpoint defined WITH the arrow (presupposes sigma -> READS).**
  By Q3's co-flip weld, the record arrow and sigma are ONE alpha-odd datum
  (probe E2: `r * sigma` is alpha-invariant `= +1`; they flip together, same
  class). So "having the record arrow" IS "having-already-chosen the alpha-odd
  lift" = having-already-chosen sigma. A standpoint DEFINED as "the
  record-arrow-bearing first person" is defined as "having-already-chosen
  sigma" -- it reads sigma off its own definition. This is the circularity the
  check forbids: "a standpoint defined AS having-already-chosen-sigma reads, it
  does not supply." Probe E4: the standpoint's alpha-even content is identical
  across the sigma=+1 and sigma=-1 worlds, so the non-sigma content does not
  determine sigma; whatever sigma the standpoint "has" was put in, not derived.

- **Horn 2 -- standpoint defined WITHOUT the arrow (blind -> cannot MINT).**
  Then the standpoint is exactly the L1 self-encoding structure, which is
  built from the excluded-reading class -- and that class is EXACTLY the
  alpha-even class (diagonal-boundary: "excluded class = the alpha-equivariant
  class"). An alpha-even structure cannot output an alpha-odd value: that is
  the blindness lemma again, now blocking SUPPLY rather than reading (probe E1:
  zero even maps mint sigma). Occupying an alpha-symmetric standpoint cannot
  prefer one alpha-odd value over the other -- nothing in "being a record
  bearer" breaks the `+arrow / -arrow` symmetry. So occupying the standpoint
  does not CONSTITUTE a choice; the choice is an additional datum the
  standpoint does not supply.

The dichotomy is exhaustive and both horns fail supply: define the standpoint
with the arrow and it presupposes sigma (circular read); define it without and
it cannot mint sigma (blind). There is no middle -- any dependence on sigma in
the definition is presupposition; any independence is alpha-even blindness.

### 4.3 What the FLP / indexical steelman actually shows

Examined at its own analogies, the steelman confirms the break. In FLP the
tie-break indexical is supplied by the ENVIRONMENT (message arrival timing);
the node is the LOCUS at which the external datum registers, not its SOURCE.
The sampler draws from EXTERNAL randomness; the forward pass (the observer's
internal, alpha-even structure) computes the full distribution -- all readings
weighted -- and the actualization comes from OUTSIDE the pass. So even the
steelman's own systems put the VALUE outside the standpoint and use the
standpoint only as the HOST/LOCUS. The addendum's own words are decisive:
"the source of exactly one datum the inside provably cannot MINT." Cannot mint
= cannot supply. The standpoint program, stated at full strength, does not
claim the observer supplies sigma's value; it claims the observer is the
inside that the external datum attaches to, and that the observer's inside-ness
is WHY the datum must be external. That cuts for FREE, not for
STANDPOINT-SUPPLIED.

**Circularity check: FAILED (for supply of sigma's value).** The standpoint
reads/hosts sigma; it does not supply it.

---

## 5. Steelman FREE at full strength (before accepting it)

FREE must not win by default; here is its strongest form, and the texture that
makes it non-trivial.

- **Structural admissibility of both values:** W211's five-method liberation
  proves both sigma values are structurally admissible -- the exact content of
  "free coin." A free binary is precisely a value both of whose settings the
  structure permits, which is why its value is an external Godel-independent
  posit.
- **The DE sign is then a free parameter:** `sgn(w_0+1) = eps` rides sigma
  (blockbuster P1); with sigma free, GU's third-person geometry does not fix
  the DE sign. GU is predictively empty at sigma -- the pre-declared FREE
  consequence.
- **But maximally structured emptiness (this is why FREE here is a result, not
  a shrug):** the free coin is (i) DISCRETE (one Z/2, not a continuous
  modulus), (ii) EXACTLY LOCATED (the record-count mode of the (6,4) fiber,
  same location under all five W211 methods, decoupled from the signature by
  W202), (iii) WELDED to the record arrow (Q3), and (iv) its externality is
  FORCED by the observer's inside-ness (the L1 -> diagonal -> L2 dependency:
  "the inside-ness of the observer forces the outside-ness of the bit").

FREE is the honest verdict: a free coin, standpoint-HOSTED and
standpoint-EXTERNALITY-forced, but not standpoint-supplied.

---

## 6. Verdict

**Q2-FREE.** sigma is a genuine free Z/2 coin; the DE sign is a free
(discrete, exactly-located, record-welded) parameter that GU's third-person
geometry does not fix.

- **FORCED: fails.** No positivity / unitarity / record-conservation / anomaly
  necessity forbids either value. W211's proof-grade Godel-independence is
  confirmed; W235's positivity-forcing forces the RECORD structure and
  `C`-given-`B`, never the sector value; the sole one-sided constraint nearby
  (generation deck-admissibility) is a different datum (Q3). Probe E5.
- **STANDPOINT-SUPPLIED: fails the circularity check.** The record-arrow
  access is genuinely DIFFERENT from sector-reading (a section, not an
  alpha-even map, so the blindness lemma does not forbid it) -- the only door
  STANDPOINT could enter. But the door leads to an exhaustive dichotomy that
  both horns fail: define the standpoint WITH the arrow and the co-flip weld
  makes it presuppose sigma (reads, probe E2/E4); define it WITHOUT and it is
  the alpha-even self-encoding structure that cannot mint an alpha-odd value
  (blind, probe E1). The program's own strongest statement agrees ("the source
  of one datum the inside cannot MINT").
- **What IS standpoint-supplied (the legitimate residue, not the verdict):**
  the first person supplies (a) the DEMAND that a definite value exist (the
  symmetry-breaking residual, boundary-law leg b), (b) the HOST/LOCUS at which
  the value registers, and (c) via W235, the fact that the Z/2 is a genuine
  RECORD rather than a redundancy. It does NOT supply the VALUE. The
  inside-ness of the observer FORCES the externality of the bit; it does not
  fill it.

**Resolution of the record-access-vs-sector-blindness tension:** DIFFERENT
access. Sector-reading is an alpha-even map (blindness applies -> the first
person cannot READ sigma); record-arrow-possession is an alpha-odd
symmetry-breaking section (blindness, a maps-only lemma, does not apply -> the
first person can be DRESSED with sigma). No contradiction: they are the two
legs (read / select) of one Lawvere parent. But different access only buys
STANDPOINT a hearing at the circularity check, which it then fails.

**Circularity check: FAILED.** The standpoint reads/hosts sigma; it does not
supply it.

**HOSTILE-VERIFICATION FLAG.** The load-bearing move is the exhaustive
dichotomy in Section 4.2 (WITH-arrow = presuppose; WITHOUT-arrow = blind, no
middle). A hostile reviewer should attack the claim that these two horns are
exhaustive -- specifically whether a standpoint could be defined by structure
that is neither alpha-even nor sigma-presupposing (e.g. an alpha-odd feature
of the observer that is NOT the record arrow and NOT welded to sigma). The
sources give no such feature (every internal reading class is alpha-even,
per diagonal-boundary; the only alpha-odd first-person object exhibited is the
record arrow, which Q3 welds to sigma), so at current grade the dichotomy is
exhaustive -- but this is the exact seam to test. If such an unwelded alpha-odd
first-person feature were exhibited, Horn 2 would reopen and STANDPOINT would
merit a fresh circularity pass.

---

## 7. Boundary

Exploration tier under the standing axiom, R0_COND. One artifact + one probe
(`tests/channel-swings/q2_sector_bit_standpoint_probe.py`, exit 0, foreground,
deterministic). Externality of sigma is taken as the program's closed premise
and nowhere re-derived; Q2 resolves only HOW the Z/2 is fixed (FREE; the
standpoint hosts, does not supply). No edits to LANE-STATE,
research-portfolio, NEXT-STEPS, any claim/canon/verdict/ledger file, or any
other agent's artifact; GU otherwise read-only. No commit/push, no external
actions. No movement of `bar(b)`, `H59`, the count `{1,3}`, or public posture;
the DE sign / sigma value remains the externally posited datum (p2c-owned per
the tri-repo signed-graph result). The finite Z/2 probe is a faithful toy of
the structural facts (even/odd blindness, co-flip weld, positivity blindness);
the operator-grade and proof-grade content it stands on lives in the cited
W211 / W235 / Q3 / boundary-law receipts, consumed not re-run.
