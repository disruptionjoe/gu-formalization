---
title: "Decision tree Q3 (sigma vs tau): one anchor or two? — VERDICT Q3-TWO-INDEPENDENT. The co-flip Z/2 inside the generation anchor Z/6 (deck-admissibility of the internal-fiber transport) is a DIFFERENT order-2 datum from the sector bit sigma (the Krein orientation K_S): they control different observables, sigma-flip preserves the anchor's deck-parity instead of toggling it, and the on-the-books L1 identification covers the habitat/section decks — NOT the internal generation fiber, which is a third base L1 explicitly cannot unite"
status: active_research
doc_type: exploration
created: 2026-07-21
program: explorations/prereg-three-object-decision-tree-2026-07-21.md
outcome: Q3-TWO-INDEPENDENT
axiom: lab/process/boundary-adapter-standing-axiom.md
inputs:
  - explorations/conditional-forcing-minimal-input-2026-07-20.md
  - explorations/l1-assembly-2026-07-20.md
  - explorations/source-packet-coflip-holonomy-freeze-2026-07-20.md
  - explorations/hardening-h2-lean-coflip-2026-07-19.md
  - explorations/blockbuster-p1-de-sign-covariance-2026-07-19.md
  - explorations/blockbuster-p3-one-bit-dossier-v2-2026-07-19.md
  - explorations/W211-krein-sign-godel-independent-five-method-synthesis-2026-07-14.md
  - explorations/verdict-generations-transport-line-closed-2026-07-20.md
  - explorations/prereg-trit-symmetry-and-fork-2026-07-20.md
runnable:
  - tests/channel-swings/q3_one_anchor_vs_two_probe.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_actions: none
---

# Q3: is the anchor's co-flip Z/2 the same Z/2 as the sector bit sigma?

Adversarial truth-test, not advocacy. The CLOSED PREMISE holds: both sigma and
the anchor co-flip are external — I am not re-litigating that. The single
question is whether they are the SAME external datum (same generator, same
action on the same object) or two order-2 data that merely coincide in being
Z/2. Verdict up front: **Q3-TWO-INDEPENDENT.** The identification is asserted
on the books (conditional-forcing framing banner, leaning on L1) but is NOT
proven at the same-object level; the affirmative independence evidence (three
disjoint observables; a decisive parity check) refutes it at current grade.

Receipt: `tests/channel-swings/q3_one_anchor_vs_two_probe.py` — deterministic,
numpy only, no network, exit 0, HEADLINE `7/7 [E] + 2/2 [F] (setup [T]=1) ALL
PASS`.

---

## 1. Origin trace of each Z/2 (where each one is BORN)

Three objects wear the word "co-flip"/"deck"/"Z/2"; the anti-circling rule
(program rule 3) forbids collapsing them without proving the identification.
Naming them apart is the whole job.

### sigma — the sector bit (the Krein orientation)
- **Object:** the orientation of the Krein form `K_S = e_0...e_8` on the (9,5)
  Clifford spine; the C-operator grading sign (record-count mode Krein-negative
  on the (6,4) DeWitt fiber). Value set `{+K_S, -K_S}`.
- **Type:** a FREE external coin. W211's five-method synthesis: symmetry
  reduction to the maximal-compact stabilizer SO(9)xSO(5) grows the
  invariant-form space from dim 1 to dim 2 (basis `{eta, eta.C}`), *liberating*
  the sign as a free Z/2; "compute harder inside GU" is ruled out by proof. Its
  value is the one external posit, Godel-independent (tri-repo signed-graph).
- **Home:** the habitat / metric fiber `F = GL(4,R)/O(3,1)`, `pi_1(F) = Z/2`;
  and the (9,5) Krein structure.
- **Observable it controls:** the physical sector / **DE sign**,
  `sgn(w_0+1) = eps = tau_theta * sgn(Z_theta)` (blockbuster P1, exact readout
  identity `rho_DE + p_DE = eps * Z * Bdot^2`). Kramers-blind: no GU-native
  operator reads it.

### the co-flip involution (the OPERATION that flips sigma)
- **Object:** the involution `E` / `U_h` that flips `(sigma, record-direction)`
  TOGETHER. This is the one-bit result (CH-REC, CoflipCore.lean:
  `sector(act E c) = -sector c AND dir(act E c) = -dir c`).
- **Type:** DERIVED, not a datum — it is the **holonomy** of the Z/2-twisted
  `K_S`-bundle over the generator loop of `pi_1(F) = Z/2` (source-packet
  co-flip-holonomy freeze; all 45 mixed planes transport `K_S -> -K_S`).
- **Relation to sigma:** it is a symmetry that ACTS ON sigma (flips it). L1
  (commit 56304e8) proves the section-deck, the payload/anchor-exchange deck,
  and this co-flip are ONE class = the `{+-K_S}` double cover = sigma's flip,
  via the algebra identity `U_h = -(e0 e9)(e3 e11)(e4 e12)` (a habitat word,
  odd mixed count) read by one character `sgn_K`. **This co-flip is genuinely
  sigma's own flip.** Note WHAT it flips: sigma and the RECORD direction — both
  in the sector/record sphere. It has nothing to do with the generation count.

### the deck co-flip inside the generation anchor Z/6 (the Q3 subject)
- **Object:** the Z/2 factor of the minimal external input `Z/6 = Z/2 x Z/3`
  (conditional-forcing-minimal-input). Its content is **deck ADMISSIBILITY:**
  the generation transport must satisfy the exact co-flip `q(-v) = -q(v)` on the
  INTERNAL fiber-core double cover `S^3 -> RP^3`, whose deck transformation is
  the antipodal `-I`. It is the CUBE of the order-6 generator; the trit tau is
  the SQUARE.
- **Type:** a **one-sided CONSTRAINT** (the transport must be deck-ODD), NOT a
  free coin. Evidence: the Z/3-alone member `(z1^4, z2)` has "deck parity broken
  at O(1) — inadmissible"; "the bit is independently necessary for
  ADMISSIBILITY." Deck-oddness "pins parity only; it cannot see mod 3."
- **Home:** the INTERNAL fiber `S^3` (unit quaternions) over which the
  generation degree `c` (hence `k = 64c`, hence `order(J(k))`) is computed.
- **Observable it controls:** the **admissibility / parity of the generation
  count** (whether the degree is even/odd on the double cover). Not the DE sign,
  not the Krein orientation.

The origins are pinned. sigma is a free orientation coin on the (9,5) Krein
form / habitat fiber, controlling the DE sign. The anchor's Z/2 is a parity
constraint on the internal `S^3` transport, controlling count-admissibility.
Same generator on the same object? That is the test.

---

## 2. The on-the-books ONE-ANCHOR claim, stated at full strength (steelman)

The strongest honest ONE-ANCHOR story, assembled from the record:

1. conditional-forcing §3: the minimal external `X` is one order-six phase
   reference; "its CUBE is the payload bit (deck admissibility); its SQUARE is
   the trit anchor." So `sigma =? cube(Z/6 gen)`, `tau = square(Z/6 gen)`, one
   `Z/6 = sigma x tau`.
2. conditional-forcing framing banner (commit 3fc76f5): "the cube-relation's
   deck=payload identification ... INDEPENDENTLY CLOSED the same night by L1
   (56304e8: section-Z/2 = payload-Z/2, one class) — so the bit in the anchor
   IS the payload orientation bit."
3. L1: payload-Z/2 = the `{+-K_S}` double cover = sigma (Section 1 above).
4. The bridge exists: conditional-forcing Leg B — flipping sigma composes the
   generation transport with the antipodal `-I` of `S^3`, and the internal
   deck IS that antipodal. So sigma's flip acts on the internal fiber precisely
   AS the internal deck generator. A real coupling, not a coincidence.

Chain: anchor-Z/2 = payload-Z/2 (banner) = sigma (L1). **ONE-ANCHOR.** This is
the "single discrete external Z/6 fixes both the sector and the three
generations" blockbuster form, and it is on the record. I steelmanned it before
trying to break it, per program discipline.

---

## 3. The identification does NOT hold: three refutations

### 3.1 Different observables (the required control)
Plant "sigma = the anchor co-flip"; refute by an object depending on one but
not the other. The probe tabulates three observables and their dependency sets:

| observable | depends on | independent of |
|---|---|---|
| generation COUNT (`3 iff 3 does not divide deg`) | transport degree mod 3 (the trit) | **sigma** — sigma-blind |
| DE SIGN (`sgn(w_0+1) = eps`) | **sigma** (eps) | transport degree, deck-parity |
| ADMISSIBILITY (`transport deck-odd?`) | the anchor deck-Z/2 | **sigma** |

- **The count does NOT depend on sigma.** conditional-forcing X1 Leg B,
  machine-witnessed: "K_S-orientation flip composes the transport with the
  antipodal map of S^3, which has degree +1: the degree is UNCHANGED
  (witnessed: -1 -> -1)... The oriented bit selects nothing." The entire X1
  theorem is "the class is bit-blind." Flipping sigma leaves the generation
  count at 3.
- **The DE sign does NOT depend on the anchor deck-Z/2.** `eps` rides the (9,5)
  Krein orientation; the internal-fiber parity constraint never enters the
  `rho_DE + p_DE` identity.
- sigma and the anchor co-flip control DIFFERENT observables — the method's
  stated signature for TWO-INDEPENDENT.

### 3.2 The decisive parity check (fixing one does NOT force the other)
If sigma and the anchor deck-Z/2 were one datum, flipping sigma would toggle the
deck-parity (odd <-> even), and the 4 combinations would not all be admissible.
They are not one datum:

- sigma-flip = **antipodal precomposition** on `S^3` (Leg B). Probe FACT 1,
  exact (defect 0.0 over 200 draws): if `f` is deck-odd then `g = f o A` is
  ALSO deck-odd; if `f` is deck-even it stays deck-even under `A o .`. Antipodal
  composition PRESERVES deck-parity (and, `deg(A) = +1`, the degree). **sigma-
  flip cannot toggle the deck bit** — the [F] control "sigma-flip flips even to
  odd" would have fired if they were the same Z/2; it did not (defect 0.0).
- The 4-combo `(sigma +/-, deck odd/even)`: admissibility `= (deck == odd)`, a
  function of the deck bit ALONE, INDEPENDENT of sigma. sigma ranges free over
  `{+,-}` inside the admissible (deck-odd) sector; deck-even is dead for BOTH
  sigma values. So fixing sigma does not fix the deck bit (it must be odd for
  both sigma), and fixing the deck bit (odd) does not fix sigma (both pass).
  Neither forces the other = independent.

There is also a KIND mismatch that no identification survives: **sigma is a free
coin** (both values structurally admissible — that is exactly why its value is
an external Godel-independent posit, W211), while **the anchor Z/2 is a one-
sided constraint** (only the odd value is admissible). A free binary and a
one-sided constraint are not the same Z/2 datum.

### 3.3 L1 identifies the wrong pair of decks for this question
L1 is a real result — but it identifies the **section-deck** and the
**payload/holonomy-deck**, BOTH living on the habitat side (the `K_S`-sign
double cover over `F` and the end-family base loop). The generation anchor's
deck is the **internal `S^3 -> RP^3`** double cover — a THIRD base. L1 does not
assemble it: `C_read`'s six objects are entropy / S-matrix / Kramers / m1 /
record / sections — the generation-transport fiber is not among them. And L1's
own honest caveat (Section 1 + Boundary + Sheaf-theorist lens): the two classes
it DOES treat "live over different bases ... the fixture cannot see a global
base uniting the two loop families"; "same class" means only "pullbacks of one
datum along exhibited maps." The framing-banner leap from "L1 closed
section=payload" to "the anchor bit IS the payload bit" silently extends the
identification across a base L1 explicitly could not reach. It is asserted, not
proven — precisely the move rule 3 forbids.

Corroboration from the program's own adversary: the hostile-verify of
conditional-forcing (commit 6eb850d) reads the anchor's deck/payload bit as
**native bookkeeping** (a gate native structure passes), making the minimal
EXTERNAL input ONE TRIT and the Z/2 not external at all. That reading is a
different quarrel (Q3 takes both as external by closed premise), but it points
the same way: nobody has pinned the anchor's Z/2 to sigma at object level; two
readings of the program disagree on what the anchor's Z/2 even is.

---

## 4. Steelman of TWO-INDEPENDENT, and the residual that could revive ONE-ANCHOR

TWO-INDEPENDENT is not free of tension, and honesty requires naming its weak
seam. The genuine coupling of §2.4 is real: sigma-flip DOES act on the internal
fiber as the antipodal, which generates the internal deck. One could argue the
internal deck Z/2 is therefore "the image of sigma." The refutation stands
because being the antipodal ACTION is not being the deck-parity DATUM: the
anchor's Z/2 is the *requirement of oddness under* that antipodal, and sigma-
flip (which is that antipodal) provably preserves oddness rather than being it
(§3.2). An action and the equivariance-constraint under that action are
different Z/2's — the first is degree-neutral and parity-preserving, the second
is the parity itself.

**The one lemma that would revive ONE-ANCHOR** (named once, per rule 2 — a NEW
obstruction, not a re-run of externality): an operator/KR-grade **base-uniting
map** carrying the internal generation fiber `S^3` and the habitat fiber `F`
onto one base under the single character `sgn_K`, such that the anchor's deck-
oddness datum is the pullback of the `K_S`-orientation datum (not merely acted
on by its flip). This is exactly L1's own stated residue — "the operator lift ...
weak point-surjectivity on a genuine function object; the N2/L^2 gate" and the
section-theory §7.4 KR-grade residue "where a global base uniting the two loop
families would live." It does not exist at fixture grade. Until it is built AND
shown to send oddness-constraint to orientation-coin, sigma and the anchor Z/2
are two data. (Even then it would have to overturn §3.1's different-observables
result, which is the harder wall: a base-uniting map that leaves the count
sigma-blind and the DE sign deck-blind has united the fibers without
identifying the data.)

---

## 5. Verdict

**Q3-TWO-INDEPENDENT.** GU needs at least two independent external order-2 data:

- **sigma** — the sector bit: the free `{+-K_S}` Krein orientation coin on the
  (9,5) spine / habitat fiber `F`. **Fixes:** the physical sector and the DE
  sign `sgn(w_0+1) = eps`. Externally posited value (Godel-independent). The
  co-flip involution (holonomy over `F`) is sigma's own flip and co-moves the
  record direction — that pairing (sigma <-> record arrow) is the honest
  one-bit result and is untouched here.
- **the anchor co-flip** — the Z/2 factor of the generation anchor `Z/6`: the
  one-sided deck-ADMISSIBILITY constraint `q(-v) = -q(v)` on the internal fiber
  `S^3 -> RP^3` (the CUBE of the order-6 generator). **Fixes:** the parity/
  admissibility of the generation transport so the trit's mod-3 count is
  well-defined on the double cover. Constraint, not free coin.

They coincide only in being order-2, and are coupled (sigma-flip acts as the
internal antipodal) without being identified. The "single discrete external
`Z/6 = sigma x tau` fixes both the sector and the three generations" framing is
**too tidy**: the honest minimal external ledger for the generation count is
`Z/6 = (deck-admissibility Z/2) x (trit Z/3)`, and the SECTOR bit sigma is a
SEPARATE external Z/2 living on the Krein form, so GU's discrete external input
is at least `sigma_Krein x Z/6_gen` (a `Z/2 x Z/6`, with the two Z/2's distinct)
— unless the §4 base-uniting operator-grade lemma is built and defeats the
different-observables wall.

Scope/caveats (disclosed): fixture grade on the frozen (9,5) H-class, R0_COND,
both habitat pins; the internal-fiber and habitat-fiber models are the ones the
cited probes use; `deg(antipodal S^3) = +1` is cited (Olum / Leg B witness), not
recomputed. No claim / canon / verdict / posture movement.

---

## 6. Boundary

Exploration tier under the standing axiom, R0_COND. One artifact + one probe
written (`tests/channel-swings/q3_one_anchor_vs_two_probe.py`, exit 0). No edits
to LANE-STATE, research-portfolio, NEXT-STEPS, any claim/canon/verdict/ledger
file, or any other agent's artifact; GU otherwise read-only. No commit/push, no
external actions. Externality of sigma and of the anchor Z/2 is taken as the
program's closed premise and is nowhere re-derived; this document resolves only
whether they are the SAME external datum (they are not, at current grade) and
names the single lemma whose construction could revive ONE-ANCHOR.
