---
title: "Blockbuster P2: the vacuum cancellation theorem — master defect law, de Donder class discharged to an equation of motion, first nonlinear obstruction located and typed"
status: active_research
doc_type: exploration
created: 2026-07-19
directed_by: "Joe direct chat, 2026-07-19 (blockbuster swing, Pathway 2: lift the P-K2 PARTIAL toward a theorem)"
axiom: lab/process/boundary-adapter-standing-axiom.md
extends:
  - explorations/pk2-gauge-covariance-2026-07-19.md
inputs:
  - explorations/pk2-gauge-covariance-2026-07-19.md
  - tests/channel-swings/pk2_gauge_covariance_probe.py
  - explorations/channel-swing-CH-GR-2026-07-19.md
  - explorations/channel-swing-CH-SRC-2026-07-19.md
  - explorations/channel-swing-CH-COSMO-2026-07-19.md
test: tests/channel-swings/bb_p2_vacuum_theorem_probe.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Blockbuster P2: the vacuum cancellation theorem

Assignment: lift the P-K2 PARTIAL to the strongest currently-provable theorem;
attack the presentation-class debt (DEM-GR-3's shadow demand: can the de Donder
class be DERIVED from the action's own structure?); locate the first nonlinear
obstruction; run a hostile referee pass. Probe:
`tests/channel-swings/bb_p2_vacuum_theorem_probe.py` (exit 0, 27/27 checks; no
floats anywhere). Arithmetic discipline, stated exactly: the LAW legs (master
defect law, GEN1, the compensator/BRST identities) are generic symbolic proofs
on function entries; per-instance sweep quantities are exact rational
arithmetic at the r = 3, 7, 9 points; Group C's order-validation legs (C1a,
C1b, C2a's M^2 leg, C3a, C3b) are exact-arithmetic instance checks at SIX
exact points (radical values kept exact), openly instance-grade, not symbolic
proofs — full symbolic simplification of the second-order Ricci was cut for
runtime and is a mechanical (not mathematical) gap; C2b and the C4
obstruction receipts are exact closed forms / exact rationals.

## 0. Council pass (five lenses, inline; written before execution)

- **Mathematical relativist.** The pk2 result is already theorem-shaped; the
  lift is to state it generically, not per-background. Prove the MASTER DEFECT
  LAW — for ANY symmetric h, `t1 = (1/2)<(dH_sym).bhat> - <Ric.bhat>` — on
  generic function entries, so the vacuum identity becomes its corollary, and
  instantiate on genuinely new backgrounds (a random h where both defect terms
  fire at once; a two-center vacuum with stress interference). Feared trap:
  restating pk2's point-sweeps as if they were generic proofs — the theorem
  must ride only on the function-entry legs.
- **PDE/gauge analyst.** The de Donder hypothesis is the debt. A Stueckelberg
  compensator `phi_a` (`delta phi = xi`) makes `htilde = h - (d phi)_sym`
  gauge-invariant with `H[htilde] = H[h] - box(phi)`; a Nakanishi-Lautrup pair
  then outputs `Htilde_a = 0` as an equation of motion in the Landau limit.
  Feared trap: the compensator secretly IS the nonlocal `1/box` dressing the
  pk2 no-go left unswept — that must be named as the finding (the no-go's
  escape route realized locally by new field content), not hidden.
- **BV/Noether theorist.** The gauge-fixing fermion
  `Psi = <bar_c, H - (alpha/2) b>` generates `<b,H>` plus the ghost kinetic
  term precisely because `s H_a = box(c_a)` — which is literally pk2's n1
  identity. The class-defect object and the BRST structure are one machine.
  Check `s^2 = 0` and the fermion algebra at abelian quadratic grade, flagged
  honestly (no Jacobi content), mirroring CH-SRC's toy conventions. Feared
  trap: claiming "derived" when any gauge admits a fermion — non-arbitrariness
  must come from the Noether leg (the identity's own failure mode IS `H`).
- **Hostile referee.** Three attacks the text must answer in their STRONG
  forms: (1) `Q := t1 - t2` makes the cancellation a tautology; (2) BRST
  gauge-fixing is circular — you fixed the gauge you needed; (3) the
  nonlinear obstruction shows a leading-order accident, and "self-energy as
  matter" is Isaacson-flavored spin with known gauge-dependence pathologies.
  Feared trap: answering the weak forms.
- **Expositor.** The theorem must survive in ONE sentence: *on de Donder
  presentations of Ricci-flat linearized backgrounds, the curvature-locked
  distortion field's canonical stress cancels the trace-free vacuum residual
  exactly with unit coefficient; off the class the defect is exactly the
  constraint defect, and off vacuum it is exactly the Ricci term.* Every
  hypothesis of the full statement must map to a clause of that sentence.
  Feared trap: hypothesis-creep — conventions smuggled in as unstated clauses.

**Chair synthesis (the executed plan).** (1) Prove the master law generically;
new-coverage instances: random-h with both terms firing, two-center vacuum.
(2) Discharge the presentation class: compensator + NL pair + gauge fermion,
with a teeth check (repair a non-harmonic presentation by SOLVING the
compensator EOM; solution space = residual family; c = 1 on every repaired
representative) — and state honestly that the debt is CONVERTED (gauge class
to field content), which is exactly DEM-GR-3's shape. (3) Nonlinear: build
harmonic-coordinate Schwarzschild to O(M^2) from the exact metric, validate
by O(M^2) Ricci-flatness AND the exact harmonic condition, then compute the
O(M^3) obstruction as the master law's two typed terms with
`Ric^lin[h2] = -Ric^(2)[h1]`. (4) Referee pass answering the strong forms.
One probe, one file, no claim-status moves.

## 1. The theorem

**One sentence (expositor-certified).** On de Donder presentations of
Ricci-flat linearized backgrounds, a distortion field locked to curvature with
canonical stress cancels the trace-free vacuum residual exactly with unit
coefficient — and off the presentation class the defect is exactly the
constraint defect, while on matter backgrounds it is exactly the Ricci term.

**Theorem V (linearized vacuum cancellation).** Work on a domain of R^{1,3}
in the gate's frozen weak-field symbol conventions (either X4 sign
convention; the (7,7)-inducing convention is covered by the CH-SIG77 port
receipt, cited not recomputed). For a smooth symmetric 2-tensor `h_ab`
define: the de Donder defect `H_a = d^c h_ca - (1/2) d_a h`; the linearized
Ricci `Ric^lin`; the blocks `hmean_ab = box(h_ab)`,
`bhat_{mu nu, ab} = d_mu d_nu h_ab - (1/4) eta_{mu nu} hmean_ab`;
`t1 = (1/2)<hmean.bhat>`; the canonical quadratic stress
`t2_mn = sum_p eta^pp <bhat_{mp}, bhat_{pn}>`; and the residual `Q = t1 - t2`
(the gate's computed decomposition of the Willmore-type residual,
ch_gr_vev_stress_probe PC4 — the identification of Q with the gate residual
is a cited computation, not a definition made here).

- **(0) Master defect law** (generic; proven on symbolic function entries,
  probe A1b): identically in h, with no hypotheses at all,

  > `Q^TF + [t2]^TF = [t1]^TF = (1/2)[<(dH_sym).bhat>]^TF - [<Ric^lin.bhat>]^TF`.

- **(i) Vacuum cancellation.** Under (H1) `Ric^lin = 0` (gauge-invariant
  vacuum) and (H2) `H_a = 0` (de Donder class), both law terms vanish, so
  `t1 = 0` and `Q^TF + sigma kappa^2 [t2]^TF = (sigma kappa^2 - 1)[t2]^TF`
  for the locked field `theta = kappa bhat`: exact cancellation iff
  `sigma kappa^2 = 1`; `sigma = -1` admits no real kappa (hard Z/2 gate,
  gate A4); the coefficient is RIGID — `c = 1` across the whole class,
  closed under residual gauge, on Schwarzschild, Kerr-drag (gate A6-A8,
  pk2 Tier 1), and now a two-center superposition whose stress carries
  nonzero cross-center interference (probe A3, new background).
- **(ii) Constraint defect law.** Off the class on Ricci-flat backgrounds the
  defect is `(1/2)[<(dH)_sym.bhat>]^TF` exactly; no constant retune exists
  anywhere in the pk2 deformation family (8 non-harmonic members, 2
  backgrounds — coefficient never tracks the gauge).
- **(iii) Matter defect law.** On de Donder presentations of non-vacuum
  backgrounds the defect is `-[<Ric^lin.bhat>]^TF` exactly (K5 remainder =
  the Ricci term, pk2 T2a4); on a fully random h BOTH terms fire at once and
  the law still closes exactly (probe A2 — first such instance in the
  program).
- **(iv) No local covariant substitute.** Every scale-free zero-derivative
  stress locked to the gauge-invariant curvature slot has identically
  vanishing trace-free part on 4D Ricci-flat backgrounds (4D Lanczos
  identity, pk2 T2b) — the theta-lock's de-Donder-presentational character
  is irreducible at that kernel order.
- **(v) Presentation discharge (Theorem V-prime, Section 2).** Adjoin a
  Stueckelberg compensator `phi_a` (`delta phi_a = xi_a`) and a
  Nakanishi-Lautrup pair. Then `htilde = h - (d phi)_sym` is gauge-INVARIANT
  (probe B1), `Htilde_a := H_a[h] - box(phi_a) = H_a[htilde]` is a
  gauge-invariant constraint (B2), and the Landau-limit b-equation of motion
  is exactly `Htilde_a = 0` (B4). Statements (0)-(iii) applied to `htilde`
  are then GAUGE-INVARIANT statements, and (H2) is no longer a hypothesis:
  it is an equation of motion of the enlarged action.

**Proof sketch, by machine-checked leg.**

| leg | status | receipt |
|---|---|---|
| `box h = dH_sym - 2 Ric^lin` (GEN1) | generic symbolic proof | pk2 GEN1; re-verified bb_p2 A1a |
| master law (0) | generic symbolic proof (t1 linear in hmean + GEN1; verified by direct contraction) | bb_p2 A1b |
| `Q` = gate's Willmore-type residual | computed identification | ch_gr_vev_stress_probe PC4 (cited) |
| coefficient rigidity + Z/2 sign gate | computed, background-robust | gate A3-A8; pk2 Tier 1; bb_p2 A3c, B5d |
| both-terms instance (law closes with H != 0 AND Ric != 0) | exact rational, 3 points | bb_p2 A2 |
| pure-gauge deformations preserve Riemann (GEN2) | generic symbolic proof | pk2 GEN2 |
| 4D Lanczos no-go (iv) | symbolic, both backgrounds | pk2 T2b1-T2b6 |
| gauge invariance of htilde; `H[htilde] = H - box(phi)` | generic symbolic proof | bb_p2 B1, B2 |
| `s H_a = box(c_a)`; NL/Landau EOM | generic symbolic proof + algebra | bb_p2 B3, B4 |
| EOM repairs any presentation; kernel = residual family; c = 1 survives | computed | bb_p2 B5a-B5d |

The proof depth is deliberately low — the theorem's force is structural
identification (the residual IS minus the canonical stress of the locked
slot; the two failure modes ARE the constraint defect and the Ricci term),
plus rigidity, the sign gate, and the no-go. Low depth is a feature for a
program whose standing risk is unearned imports: every clause is either a
generic symbolic identity or an exact computation.

## 2. The presentation-class debt: discharged to an equation of motion

This was the swing's decisive question (DEM-GR-3's shadow demand from pk2:
"the source action must either DERIVE the de Donder presentation or own it
as frozen construction data"). Outcome: **the derivation branch lands at toy
grade.** The mechanism, fully exhibited:

1. **Compensator.** `phi_a` with `delta phi_a = xi_a` (the transcript-shaped
   Stueckelberg move CH-SRC's Tier-2 toy already uses). Then
   `htilde = h - (d phi)_sym` is gauge-invariant (B1, generic), and
   `H[htilde] = H[h] - box(phi) =: Htilde` (B2, generic) — the de Donder
   defect acquires a gauge-invariant completion.
2. **Gauge fermion.** With `s h = (d c)_sym`, `s bar_c = b`, `s b = s c = 0`
   (nilpotent termwise), the fermion `Psi = <bar_c, H - (alpha/2) b>_eta`
   generates
   `S_gf = s(Psi) = <b, H>_eta - (alpha/2)<b, b>_eta - <bar_c, box c>_eta`,
   closed (`s S_gf = 0`) precisely because `s H_a = box(c_a)` — which is
   pk2's n1 identity (the constraint defect of a gauge shift IS box of the
   gauge parameter). The identity that measured the theorem's failure off the
   class is the same identity that closes the gauge-fixing algebra (B3).
   Every bracket is the SAME indefinite eta form — SRC-COH-1's one-Krein-form
   rule holds in this sector too.
3. **Landau limit.** The b-equation of motion is
   `Htilde_a - alpha b_a = 0`; as `alpha -> 0`, **`Htilde_a = 0` is an
   equation of motion, not a hypothesis** (B4). In the phi = 0 frame this
   reads `H_a = 0`: the de Donder class is the compensator sector's
   on-shell surface.
4. **Teeth.** Take a genuinely non-harmonic presentation
   `h' = h_Schw + (d xi_bad)_sym`. The compensator EOM `box(phi) = H[h']`
   is solvable with a NONTRIVIAL harmonic kernel part; the repaired
   representative `htilde = h' - (d phi)_sym` is de Donder, differs from the
   base presentation, and the theorem holds on it with the frozen `c = 1`
   (B5a-B5d). The EOM's solution space (particular + harmonic kernel) IS the
   residual family pk2 swept — the rigidity-under-residual-gauge result and
   the compensator's solution ambiguity are the same fact.

**What this upgrades.** The pk2 PARTIAL said: the surviving statement has one
gauge-CLASS hypothesis, and "whoever wants the theorem must own the gauge
class as part of the construction's frozen data." After this swing the class
is not frozen data — it is the Landau-limit EOM of a typed auxiliary sector,
and Theorem V-prime (statements (0)-(iii) applied to the gauge-invariant
`htilde`) has NO gauge hypothesis at all. The 4D Lanczos no-go is not
violated: `htilde` is nonlocal in h alone (integrating out phi produces
exactly the `1/box`-dressed kernels the no-go's honest boundary left
unswept). **The compensator is the LOCAL realization of the no-go's nonlocal
escape route** — new field content, which is what "the missing object is not
symbol-level" predicted from the CH-SRC side.

**Honest accounting — what is derived, what is converted, what is open.**

- DERIVED: `H = 0` as an on-shell statement of an enlarged action; the
  closure of the gauge-fixing algebra from the program's own n1 identity;
  the identification of residual gauge freedom with the EOM's kernel.
- CONVERTED, not annihilated: the hypothesis moved from gauge class to FIELD
  CONTENT (one compensator vector + one NL pair + the specific fermion).
  Choosing Psi is choosing de Donder. Two non-arbitrariness arguments, both
  computed: (a) the Noether leg — de Donder is the class whose OWN defect
  generates the identity's failure term exactly (pk2 n6/n7); fixing to any
  other class G_a = 0 leaves a residual defect NOT generated by G, so the
  cancellation demand itself selects this fermion up to the residual family;
  (b) `s H = box c` makes this the fermion whose ghost sector is the
  program's existing constraint machinery, not an import.
- OPEN: whether GU's actual unwritten `S_IG` CONTAINS this sector is
  DEM-GR-3 proper — unchanged, now sharpened to "must contain a
  Stueckelberg/NL sector with this fermion shape." No-ghost at interacting
  level is not proven (the Landau-limit (b, bar_c, c, phi) quartet is
  expected to decouple by the standard argument at this abelian grade;
  stated, not proven); Krein pricing inherited per SRC-COH-1.

## 3. First nonlinear obstruction: located, computed, typed

Setup: exact harmonic-coordinate Schwarzschild
(`g_00 = -(r-M)/(r+M)`, `g_ij = ((r+M)/(r-M)) n_i n_j +
((r+M)^2/r^2)(delta_ij - n_i n_j)`), series-expanded exactly:
`h1` = the gate's linear background (C0a computes the match), and

> `h2_00 = -2 M^2/r^2`, `h2_ij = M^2 (delta_ij / r^2 + x_i x_j / r^4)`.

Machinery validated end-to-end before use: inverse-metric identity to
O(M^2), order by order (C0b, symbolic); full nonlinear Ricci of
`eta + h1 + h2` vanishes at O(M) AND O(M^2) (exact arithmetic at six exact
points — h2 is the true second-order piece; C1a/C1b); the EXACT
harmonic-coordinate condition `g^{bc} Gamma^a_{bc} = 0` holds at both orders
(C2a; O(M) leg symbolic, O(M^2) leg at the six points). Then:

- **The linear class does not persist verbatim; its second-order defect is
  DETERMINED.** `H[h2]_i = 4 M^2 x_i / r^4 != 0` (C2b, closed form): the
  linear de Donder condition fails on the second-order piece even though the
  exact harmonic class survives. So at second order the constraint defect is
  not new freedom — it is a computable functional of h1, forced by the exact
  gauge class.
- **Second-order vacuum bookkeeping.** `Ric^lin[h2] = -Ric^(2)[h1,h1]`
  (C3b, exact arithmetic at the six points), with `Ric^(2)[h1] != 0` (C3a):
  the second-order piece is sourced by the first-order field's self-energy.
- **The linear theorem is CLEAN at O(M^2)** — `[t1[h1+h2]]^TF` has no M^2
  term (C4a): the vacuum cancellation survives at its own order; the
  obstruction starts strictly at the next order.
- **The first obstruction sits at O(M^3) and is TYPED by the master law**
  (C4b, exact at r = 3, 7, 9 points):

  > `[t1[h1+h2]]^TF |_{M^3} = (1/2)[<(dH[h2])_sym . bhat1>]^TF + [<Ric^(2)[h1,h1] . bhat1>]^TF`

  — a constraint piece (from the determined linear-class defect of h2) plus
  a Ricci piece (gravitational self-energy entering the theorem's own MATTER
  slot). Both pieces fire; the total is nonzero (C4c/C4d). Exact receipts,
  (1,1) component (units of M^3): at (1,2,2), r = 3: constraint `16/6561`,
  Ricci `-24/6561`, total `-8/6561`; at (2,3,6), r = 7: `296/40353607`,
  `-444/40353607`, `-148/40353607`; at (4,4,7), r = 9: `88/129140163`,
  `-132/129140163`, `-44/129140163`. The (0,0) TF component vanishes at all
  three points (static field). OBSERVATION, recorded not claimed generally:
  at every sampled component and point the two pieces are proportional to
  the total in the fixed ratio constraint : Ricci : total = -2 : 3 : 1 —
  if that proportionality is exact on this background, the O(M^3) defect is
  a SINGLE structure seen through two slots, which would make the
  second-order absorption question (below) one coefficient, not two. Left
  as a named check for the follow-up.

**Reading.** The first nonlinear obstruction is not a new structure: it is
the theorem's own two-sided defect law feeding back on itself — the
constraint slot fed by the exact gauge class's second-order defect, the
matter slot fed by `Ric^(2)[h1]`, i.e. **nonlinear gravity self-sources
exactly where the theorem says matter sits.** This is the K5 discriminator's
prediction promoted to a computed identity at second order, and it is the
CORRECT behavior for the no-target-import discipline: a construction whose
vacuum cancellation persisted unmodified at O(M^3) would be cancelling its
own self-energy (Einstein-dynamics-in-disguise territory, per CH-GR K5).

**Named next computation (bounded, not done, not claimed).** Whether an
extended lock `theta = kappa bhat + kappa_2 K_2(bhat, bhat)` (second-order
response kernel, pure-number kappa_2 by the C2 scale law) can absorb the
DETERMINED O(M^3) defect on the exact-harmonic class — and whether the
absorption coefficient is again rigid. If yes, the natural conjecture is:
*on exact-harmonic presentations of exact-vacuum backgrounds, the defect at
every order is given by the same two-term law, absorbable order-by-order
with frozen pure numbers.* That conjecture is the nonlinear theorem; nothing
beyond its first-order evidence is claimed here.

## 4. Referee pass (hostile lens; strong forms, answered or conceded)

**R1 — "The theorem is a tautology: you defined Q = t1 - t2, so
Q + t2 = t1 is arithmetic, and t1 = 0 in harmonic gauge is immediate.
Dressing this as a theorem is inflation."**
Answer: three separable contents survive the deflation. (a) The
identification of `t1 - t2` with the gate's independently-defined
Willmore-type residual is a COMPUTATION (PC4), not a definition — the
residual existed before the split. (b) `t2` being exactly the CANONICAL
quadratic stress of a field locked to `bhat` is the physical claim: a
one-parameter equivariant ansatz lands its stress proportional to the
residual with a hard Z/2 sign gate and a rigid coefficient — rigidity was
falsifiable (12-member sweep, two backgrounds, a two-center superposition
with interference) and survived. (c) The master law's split of the defect
into EXACTLY constraint-defect + Ricci — with nothing left over, generically
— is the two-sided structure that makes the statement falsifiable on matter
backgrounds and at second order (Section 3 confirms it bites). CONCEDED:
the proof depth is low; anyone fluent in linearized gravity can verify GEN1
in an afternoon. The claim is not depth — it is that THIS residual, native
to the GU construction, has THIS exact structure, rigidly.

**R2 — "The de Donder 'derivation' is standard BRST gauge fixing. Any gauge
class has a fermion; you chose the one you needed. Circular."**
Answer: the mechanism is standard (that is a feature: no exotic machinery
was needed); the non-arbitrariness is not. Two computed distinguishers:
(a) de Donder is the unique class among `G_a = 0` candidates whose own
defect generates the identity's failure term — the Noether leg (pk2 n6/n7)
shows the cancellation defect is EXACTLY `(1/2)<(dH_sym).bhat>`, i.e. the
theorem itself selects which constraint the fermion must impose; imposing
any other class leaves an unexplained residual. (b) The fermion's closure
identity `s H = box c` is the same n1 identity that measured the defect —
the gauge-fixing algebra is the program's existing constraint machinery.
CONCEDED, fully: the debt is CONVERTED (gauge class -> field content), not
annihilated; whether GU's actual `S_IG` contains the compensator/NL sector
is DEM-GR-3 and remains open; if it does not, Theorem V stands with (H2) as
frozen construction data, exactly as pk2 left it.

**R3 — "O(M^3) breaks your cancellation, so the 'theorem' is a leading-order
accident. And calling `Ric^(2)` 'matter' is Isaacson-flavored rhetoric —
effective gravitational stress-energy is notoriously gauge/averaging
dependent."**
Answer: the theorem never claimed nonlinear validity; what Section 3 adds is
that the failure at O(M^3) is not amorphous — it is TYPED by the same master
law, with both pieces computed in closed form in a NAMED presentation (exact
harmonic Schwarzschild), no averaging performed and none needed: we make no
claim that `<Ric^(2).bhat1>` is a physical stress-energy, only that it is
the exact value of the defect's Ricci slot in this presentation — a
statement about an identity, not about energy localization. The
gauge-dependence concern is answered structurally, not evaded: the
constraint piece of the O(M^3) defect is DETERMINED by the exact harmonic
class (C2a/C2b), so within the named class there is no averaging freedom to
abuse. CONCEDED: a presentation-independent formulation of the second-order
statement would need the Section 2 compensator machinery extended to second
order, which is not done; and the extended-lock absorption question is open
— if kappa_2 fails to be rigid, the nonlinear story dies at second order
and that would be a real (and reportable) kill.

## 5. Distance to publishable, and odds

**As a standalone mathematical note** ("A rigidity theorem for trace-free
vacuum residuals in linearized gravity: a master defect law, de Donder as an
equation of motion, and a 4D Lanczos no-go"): the theorem, the master law,
the no-go, and the O(M^3) typed obstruction form a closed, self-contained
unit whose every claim is machine-verified. Missing for submission: (a)
standalone motivation of `Q`/`bhat` (available: Willmore functional of graph
embeddings in `Met(X4)`, DeWitt vertical Christoffel — the willmore
reconciliation's frame); (b) literature positioning — the triviality risk is
R1: a referee may locate the master law as a known corollary of Fierz-Pauli
manipulations; the rigidity sweep, the Z/2 gate, the Lanczos no-go, and the
EOM discharge are the defensible novel arrangement; (c) human-checkable
proofs transcribed from the probes (mechanical). Estimate: 2-4 focused
sessions to a submittable draft. Odds at a solid mathematical-GR venue
(CQG / J. Math. Phys. class), stated honestly: **~50-60%** as a short paper
— the mechanism is standard piecewise, the arrangement and rigidity results
are the contribution, and R1 is the live rejection mode.

**As a GU-physics claim**: not publishable, unchanged. The coefficient's
source-side provenance (DEM-GR-1/2) is exactly as open as CH-GR left it;
what moved is DEM-GR-3's gauge-class leg (dischargeable at toy grade via the
Section 2 sector) and the nonlinear story (first obstruction now computed
and typed rather than unknown). The honest grade remains `R0_COND`.

**Proposals for owners (not applied here):**

- pk2's PARTIAL verdict can carry an addendum: the gauge-CLASS hypothesis is
  dischargeable to an EOM (Section 2), making Theorem V-prime fully
  gauge-invariant at the cost of one typed field-content demand; the pk2
  no-go's "nonlocal kernels not swept" boundary is now identified as the
  compensator sector in disguise.
- DEM-GR-3 acquires a computed sub-answer: clause "(derive the de Donder
  presentation as the EOM of a gauge-fixing/compensator sector)" is
  EXHIBITED at toy grade; the demand sharpens to "S_IG must contain a
  Stueckelberg/NL sector with fermion `<bar_c, H - (alpha/2)b>`, one Krein
  form throughout (SRC-COH-1)."
- K5's ledger can note: the matter-slot law is confirmed at second order
  with gravitational self-energy as the source (Section 3) — the two-sided
  discriminator now has a computed nonlinear instance.
- CH-COSMO inherits: the FLRW `t1`-sector story should use the master law
  directly (its defect is `(1/2)<dH_sym.bhat> - <Ric.bhat>` with FLRW's
  nonzero Ricci — no new structure needed).

## 6. Receipts

- Probe: `tests/channel-swings/bb_p2_vacuum_theorem_probe.py`, run
  2026-07-19, exit 0, **27/27 PASS**. Groups: A (master law generic + both-
  terms random instance + two-center vacuum, 7 checks), B (presentation
  discharge, 8 checks), C (nonlinear, 12 checks; O(M^2)-order legs
  point-exact at six exact points, stated openly).
- Key exact objects: `H[h2]_i = 4 M^2 x_i / r^4` (closed form, symbolic);
  `Ric^lin[h2]_00 = 2 M^2 / r^4` (sample closed form); `h2_00 = -2M^2/r^2`,
  `h2_ij = M^2(delta_ij/r^2 + x_i x_j/r^4)`; O(M^3) obstruction (1,1)
  components at r = 3, 7, 9: totals `-8/6561`, `-148/40353607`,
  `-44/129140163` (times M^3), split -2 : 3 : 1 between constraint and
  Ricci pieces (Section 3).
- Cited, not recomputed: gate PC4/A3-A8 (ch_gr_vev_stress_probe), pk2
  GEN1/GEN2/Tier1/T2a/T2b (pk2_gauge_covariance_probe), CH-SIG77 port
  receipt for the (7,7) convention, CH-SRC toy conventions for the
  abelian-grade Grassmann bookkeeping.
- Killed-selector ledger respected: none of the eleven dead routes re-run;
  branches (b)/(c) untouched; C3 untouched; the Lanczos no-go is USED as a
  boundary, not re-litigated.

## 7. Boundary

Conditional construction under the standing axiom, weak-field symbol frame,
`R0_COND` working grade. `claim_status_change: none`; no map, canon,
scorecard, or register file touched; Section 5's items are PROPOSALS for
their owners. The Section 2 discharge is at toy grade (abelian quadratic;
no interacting no-ghost proof; whether `S_IG` contains the sector is
DEM-GR-3, open). Section 3 claims exactly: obstruction located at O(M^3),
typed by the master law, both pieces nonzero in the named exact-harmonic
presentation — no nonlinear theorem is claimed. The coefficient's
source-side provenance (DEM-GR-1/2) is untouched by this swing.
