---
title: "Channel swing CH-SRC: the minimal source-action toy runs; B.1-B.4 exhibited; one orientation datum serves two of the three converging sign demands"
status: active_research
doc_type: exploration
created: 2026-07-19
directed_by: "Joe direct chat, 2026-07-19 (channel deep-research swings; CH-SRC = lagging integrator, research-portfolio.json channel_structure.ch_src_contract)"
axiom: lab/process/boundary-adapter-standing-axiom.md
extends: explorations/five-leg-swing-2026-07-19.md
inputs:
  - docs/WHERE-GU-STANDS-AND-THE-MISSING-OBJECT-2026-06-27.md
  - explorations/assembly-archaeology-recovered-parameters-2026-07-19.md
  - explorations/channel-swing-CH-GR-2026-07-19.md
  - explorations/channel-swing-CH-REC-2026-07-19.md
  - explorations/channel-swing-CH-QM-2026-07-19.md
  - explorations/channel-swing-CH-COSMO-2026-07-19.md
  - lab/process/source-object-interface-contract.md
  - lab/process/integration-readiness-scorecard.md
  - explorations/firewall-and-two-geometries/source-action-necessary-conditions-and-causality-2026-06-27.md
  - explorations/anomaly-and-bordism/nonequivariant-ghost-construction-2026-06-27.md
  - explorations/anomaly-and-bordism/bv-bicomplex-and-c2-obstruction-2026-06-27.md
  - canon/no-go-quaternionic-parity-generation-sector.md
  - tests/rs_bicomplex_spin95_connection_2form.py
pending_inputs:
  - "explorations/channel-swing-CH-SM-2026-07-19.md (sibling still running at write time; ledger rows marked PENDING)"
cross_repo_reads_cited_as_evidence:
  - "time-as-finality (read-only, Joe-authorized): tests/T507..T510 admission/ledger gates + explorations/ghost-parity-physicality-push-2026-07-07.md (record reading priced at Krein-retention + self-normalized observer; BRST record-admission shape)"
  - "temporal-issuance (read-only, Joe-authorized): memory/steward-memory-summary.md + E179/E180 (GU kinematic Krein sign trends forced-internal; out-of-band sign reading killed/inadmissible)"
tests: tests/channel-swings/ch_src_minimal_action_toy.py
ledger: lab/process/source-action-build-ledger.md
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Channel swing CH-SRC: the minimal source-action toy

> **2026-07-21 payload correction (`P-RANK-FOLD`):** the conditional fold
> mentioned below has now failed by sector separation. The native value
> `3 = dim Lambda^2_+` remains derived, but the mirror-selection and
> `SU(2)-`-collapse map cannot be encoded by the finite Spin(10) chain datum.
> Treat older `N = 4 iff fold / N = 5 if not` language as the historical open
> branch, not current slot typing. Current evidence requires the chain and
> generation-physicalization selectors to remain distinct; this correction
> does not adjudicate the global count of unrelated slots.

CH-SRC's standing role: attempt the minimal source-action skeleton (spec
B.1-B.4) and maintain the build-parameter ledger that integrates what every
other channel has frozen. Both deliverables exist as of this swing:

1. **The minimal toy is BUILT and RUNS**
   (`tests/channel-swings/ch_src_minimal_action_toy.py`, exit 0, headline
   `24 [E] + 7 [F] = 31`, setup `[T] = 4` excluded). All four spec mechanisms
   B.1-B.4 are exhibited in a finite model that structurally mirrors the
   verified real-rep machinery, and the model is honestly obstructed at
   exactly the place the real program is (the C2 analog persists — the B.5
   global data are not symbol-level suppliable).
2. **The build ledger is STOOD UP**
   (`lab/process/source-action-build-ledger.md`): every frozen demand from
   CH-GR, CH-QM, CH-COSMO, CH-REC and the 2026-06-27 archaeology is a typed
   build constraint; CH-SM rows are PENDING (its swing had not landed when
   this ran).

Headline on the three converging sign demands: **in the toy, ONE orientation
datum simultaneously (a) forces the GR cancellation sign sigma = +1 and
(b) Noether-derives the record-law direction — but (c) it provably CANNOT be
non-quaternionic**, corroborating CH-QM's (9,5) theorem at mini scale down to
the same Kramers mechanism and the same real-class ((7,7)-type) escape. The
one-bit economy holds for Krein sector + GR sign + arrow; generations remain
a separate payload decision, exactly as CH-QM's D-QM-NEG demands.

All of this is conditional construction under the standing axiom. No claim
status, canon verdict, or public posture moves.

## 1. The toy: design

Scope honestly declared up front: the win condition is a finite model
exhibiting the spec MECHANISMS, not a Y14 realization. The model is the
verified bicomplex test (`tests/rs_bicomplex_spin95_connection_2form.py`) at
1/112 scale, upgraded from a complex to an actual BV **action**:

- **Mini-rep:** `Cl(1,3) = M(2,H)` on `S = C^4` — deliberately the smallest
  QUATERNIONIC-class real Clifford algebra (`p - q = 6 mod 8 -> H`), so the
  (9,5) = M(64,H) parity structure survives miniaturization. Vector-spinor
  `V (x) S` (dim 16), gamma-trace constraint `Gamma = hstack(e_a)`, gauge map
  `d_A = vstack(xi_a I)`, Dirac symbol `M_D = I (x) c(xi)`, Krein form
  `beta = e_0` on the fiber; `xi` fixed non-null.
- **Compensator:** an a-priori NAMED non-equivariant carrier
  `sigma_c(W) = 0.8 * Sigma_01` (a fixed boost element; adjoint defect 0.80),
  fixed before any check and never tuned. Dressed constraint
  `B_W = Gamma (I (x) e^{sigma_c})`, Koszul-Tate Hessian `M_KT = B_W^+ B_W`,
  forced generator `A_W = Pi_ker(B_W) d_A`.
- **The action, two tiers:**
  - Tier 1 (projected generator):
    `S_1 = (1/2) psi^+ M_KT psi + psi* A_W c`.
  - Tier 2 (compensator FIELD, raw inherited gauge symmetry):
    `S_2 = (1/2)|B_W psi - phi|^2 + psi*(d_A c) + phi*(B_W d_A c)` —
    the raw `d_A` is restored as a symmetry by the Stueckelberg-type
    compensator `phi` with transmitted transformation
    `delta phi = B_W d_A c`.
- BV convention: fields realified; the antibracket is the naive graded sum,
  valid at this abelian quadratic grade (Koszul signs cancel pairwise for
  these monomials) — stated in the docstring.

## 2. Results: the spec sheet B.1-B.4, check by check

| spec item | toy result | receipt |
|---|---|---|
| **B.1** `(S,S) = 0` | EXHIBITED both tiers: Tier-1 operator-exact (`\|M_KT A_W\| = 8.6e-16`); Tier-2 exact at 20 random field configurations (`max \|(S,S)\| = 2.8e-14`) | B1a, B1b |
| **B.2** Noether identity FORCES `delta_2 . d_RS,-1 = 0` | EXHIBITED: the constraint identity `B_W A_W = 0` and the gauge-invariance condition `M_KT A_W = 0` are the SAME equation (`M_KT A' = B_W^+ (B_W A')`, `B_W^+` injective); under 5 random off-surface perturbations of the generator both defects fail TOGETHER, sandwiched by the singular values of `B_W`; the raw generator fails both (control `\|B_W d_A\| = 6.15`) | B2a, B2b, B2c |
| **B.3** non-equivariant compensator present AND necessary | PARTIAL-STRONG: present (adjoint defect 0.80); necessary at master-equation level — dropping the compensator's transformation breaks `(S,S) = 0` (control fires at 0.094); the equivariant-family IMPOSSIBILITY is inherited from the real-rep theorems (SHIAB-04/GHOST-01), NOT re-proven here — see Section 4 for what the mini-rep does and does not show | B3, B3a, B3b |
| **B.4** physical sector cohomological, not decoupled | EXHIBITED: quotient closed-not-exact with dim `12 - 4 = 8 > 0`; dressed escape `= 3.62 != 0` (no invariant-subspace reading); the full decoupling "fix" is constructed and achieves `[Pi, M_D + s_trap] = 1.3e-15` — exhibited AS the disqualified VZ trap; full bicomplex `s^2 = 1.2e-15` with non-vacuous leg ranks (4/4) and raw control breaking closure at 20.11 | C1, C2, C3, C4, C5, C6 |

**B.1-B.4: all four mechanisms pass.** Named gaps, so nothing is oversold:
the Tier-2 compensator is a Stueckelberg FIELD restoring the raw symmetry
(the action-level realization of "the identity is transmitted, not the bare
differential"); the antighost/Koszul-Tate leg is realized at complex level
(as in the verified test), not yet with its own antighost field in the
action; and the toy contains no metric sector, so DEM-GR-3(iii) (no linear
theta-metric vacuum coupling) is not modeled.

## 3. The three converging sign demands: one datum, tested

The orientation datum `tau in {+1,-1}` enters as the Krein-sector choice
(projectors `(1 +- tau*beta)/2` — the canonical ghost-parity orientation in
miniature).

**(a) GR cancellation sign (CH-GR K1 demand) — TESTED, POSITIVE.**
The physical K-Gram is positive-definite iff `tau = +1` (Da1), and the
canonical quadratic stress of a field locked to the tau-sector carries sign
= tau, so a real locking coefficient kappa (the `sigma kappa^2 = 1` demand)
exists iff `tau = +1` (Da2: stress `+10.03` vs `-13.28`). Both demands read
the SAME number — the K-norm sign of the tau-sector. **K1 lands positive at
toy grade**: the Krein orientation that yields the positive physical sector
IS the one that delivers `sigma = +1`, PROVIDED the action uses one Krein
form throughout. The control (Da3) shows the caveat is load-bearing: a
relative sign between the sector grading and the stress contraction breaks
the alignment — that relative sign is the GR-level image of CH-REC's
mu-import. Registered on the ledger as a NEW coherence constraint,
**SRC-COH-1**: one Krein form in every slot of the action (sector grading,
stress bilinear, record charge), no relative sign anywhere.

**(b) Record-law direction (CH-REC T3) — TESTED, POSITIVE (existence leg).**
In the toy action the record current is the Noether K-charge of the phase
symmetry; the dynamics is K-unitary so the charge is conserved (3.9e-16);
on every physical-sector state its sign equals tau (Db2) — the record
direction is DERIVED, with no free `mu` slot: the action's only sign
resources are the tau-flip (flips sector AND direction — the co-flip) and
the global K-flip (anchor relabel, a relational identity), both diagonal
(Db3). So **an action of the C_0 class with Noether-derived record sign
EXISTS** — CH-REC's T3 is satisfiable, at toy grade. This discharges the
existence half of CH-REC's gap G3; the decisive half (whether GU's actual
W229 record law is such an action) remains open and is NOT claimed.

Cross-repo pricing honored (read-only evidence, Joe-authorized): the toy's
record construction has exactly the shape time-as-finality's admission gates
(T508-T510) demand of any record packet — predeclared nilpotent `s` with a
non-nilpotent control, physical class closed-not-exact, dynamics and readout
descending through the quotient, ledger conserved (the Noether K-charge) —
AND it lives in the corner TaF's ghost-parity push priced at two non-default
assumptions: Krein-retention quantization plus a sector-normalized
(projector-Born) reading of the record charge. That pricing is inherited,
not evaded; it is now recorded on the ledger's T3 row. Independently,
temporal-issuance's steward memory carries the standing correction that the
GU kinematic Krein sign trends forced-INTERNAL (out-of-band sign readings
inadmissible) — which is what SRC-COH-1 enforces at the action level.

**(c) Non-quaternionicity (archaeology item 6) — TESTED, NEGATIVE, as
CH-QM proved.** The mini-rep reproduces the entire parity structure: the
antilinear intertwiner solved from `C conj(e_a) = e_a C` gives
`C conj(C) = -I` exactly (quaternionic class, Dc1); J preserves the Krein
sign and commutes with the orientation projector (defects ~1e-15, Dc2) — an
anticommuting orientation is impossible for the same reason as in (9,5);
every J-commuting Hermitian carrier is Kramers-doubled (even index, Dc3)
and the rank-1 odd carrier is flagged as an import (J-defect 1.414, Dc4);
and the real-class fork `Cl(2,2) = M(4,R)` gives `C' conj(C') = +I` — the
Kramers wall dissolves exactly as in the (7,7) contingency (Dc5).

**Net on the sign questions: 2 + 1.** One orientation datum genuinely serves
Krein positivity + GR cancellation sign + record direction (three demands,
one bit, coherence condition SRC-COH-1). It provably does NOT serve
generations — that demand is a separate payload decision on CH-SM's card
(rank pin / larger-typed item / (7,7) fork), per D-QM-NEG. All three
questions were tested; none was left unanswered.

## 4. The C2 scale law and the honest edge

**Scale law: PASS.** `C2(2xi)/C2(xi) = 2.000000000000` exactly, bare AND
dressed with the (scale-free) compensator (E1). The discriminator works: a
compensator kernel carrying an internal scale (`W/(1 + L^2 Q(xi))`) breaks
the exact law (ratio 2.0454, E2) — CH-GR's K3 kill is executable against any
future candidate `S_IG` at the compensator level, not just the VEV level.

**The honest edge (the C7 finding, plus a mini-rep rigidity result).** The
C2 analog (`B M_D Pi_ker(B)`, constraint-independent part) persists at full
norm under EVERY carrier tried: bare 8.30, dressed 8.38, residual equal to
the norm (fully constraint-independent — same signature as the real rep's
155.36). Sharper: in the mini-rep the dressed obstruction `[Pi_B, M_D]` is
EXACTLY invariant (to 6 decimals) under the entire equivariant (gamma5)
sweep, and non-equivariant carriers move it only UPWARD (5.8686 -> up to
6.1804, never below bare). Two honest readings, both recorded:

- The mini-rep corroborates the program's central negative at its own scale:
  **no symbol-level datum closes the obstruction** — closure needs the B.5
  global objects (the Y14 connection-curvature), which no finite symbol toy
  can supply. The toy is obstructed at exactly the same frontier as the real
  construction, which is what a faithful miniature should do.
- The BENDING phenomenon (58.72 -> 32.80 in the real rep) does NOT
  miniaturize: the mini-rep is too rigid to exhibit it. The equivariant
  family is exactly inert here (only leaving it moves the number at all —
  directionally consistent with GHOST-01 — but no carrier improves it). So
  B.3's necessity claim rests on the real-rep proofs, and this toy
  contributes presence + master-equation-level necessity, not an
  independent impossibility proof.

**Obstruction accounting (pre-registered endings):** no computed CONFLICT
was found between any two frozen channel constraints — every frozen demand
on the ledger is simultaneously realized or consistently pending in the toy.
The one thing the toy cannot do (close C2) is the one thing the spec already
assigns to the B.5 global data. The build is *narrowed and unobstructed*,
not finished.

## 5. What this does to the N-accounting

- **N = 3 core confirmed at toy grade** for the non-generation sectors:
  one Z/2 orientation (carrying Krein sector + GR sign + record arrow,
  J_quat-commuting by type, coherence via SRC-COH-1), one absolute scale
  (CH-COSMO's empirically pinned item), one finite subgroup datum (CH-SM).
  The CH-GR branch item stays deleted (forced by computation); kappa^2 = 1
  is a known pure number awaiting provenance, not a payload item.
- **Generations set the N = 4 vs N = 5 boundary**, and the toy sharpens
  nothing there beyond corroborating the wall: N = 4 iff the rank pin folds
  into CH-SM's finite datum (or the construction migrates to the real
  class); N = 5 if CH-SM's swing shows it cannot fold.
- **Two named +1 triggers remain:** T3 failing on the actual W229 record law
  (CH-REC's accounting identity — the toy shows the good case is
  realizable, not that GU realizes it), and the CH-SM fold failing.
- Evidence state after this swing: **N <= 4 conditional on (T3 on W229) and
  (the CH-SM fold), with the N = 3 reading dead for the full package** (it
  would require the orientation to carry generations, killed by the parity
  theorem and mini-corroborated here).

## 6. Proposed scorecard note (proposal only; scorecard not edited here)

CH-SRC has no scorecard row (it is the integrator, not a leg). Proposed
contract-status line for the portfolio owner: the ch_src_contract's freeze
condition ("skeleton exists at toy grade OR obstructed by a named computed
conflict") is MET on the first branch — the skeleton exists at toy grade
with receipts; the card can freeze once CH-SM's rows land in the ledger and
the K2 (gauge covariance) verdict from CH-GR's predeclared next computation
is known.

## 7. Inline persona passes (three, inline only)

**BV/BRST theorist.** The two-tier presentation is the right honesty split:
Tier 1's identity `M_KT A' = B_W^+ (B_W A')` is the genuine content of
"Noether forces the constraint" at quadratic-abelian grade — one equation,
two names — while Tier 2 is what "transmit the identity, not the
differential" means as an action: the compensator field's transformation law
IS the transmitted datum. Warning accepted and recorded: at this grade the
gauge algebra is abelian and field-independent, so `(S,S) = 0` carries no
higher-order Jacobi content; the real `S_IG` must survive the non-abelian
completion, and nothing here tests that.

**Constructive field theorist.** The toy's most useful negative is the
rigidity result: a model whose obstruction cannot be moved by ANY symbol
datum is the cleanest possible finite statement of "the missing object is
global." Suggest keeping the mini-rep as the standing regression fixture
for candidate payloads: any proposed p2c instance whose toy image claims to
reduce the C2 analog with symbol-level data only is either wrong or reading
the target. Adopted: recorded on the ledger as the standing REJECT rule
SRC-REJ-1.

**Clifford-algebra specialist.** The (1,3)/(2,2) pair is the correct
minimal mirror of (9,5)/(7,7): same real-class mechanism
(`C conj(C) = -I` vs `+I`), same Kramers consequence, and the intertwiner
was SOLVED from the algebra, not postulated — so the mini-corroboration is
independent of the canon C07 certificate rather than a restatement of it.
Caveat honored: class signs are basis-independent but rep-dimension
patterns are not; nothing about counts (which are 64-dim-H facts) is
claimed from the 4-dim model.

## 8. Receipts

- Toy: `tests/channel-swings/ch_src_minimal_action_toy.py`, run 2026-07-19,
  exit 0, headline `24 [E] + 7 [F] = 31` (setup `[T] = 4` excluded).
  Key numbers: master equation 8.6e-16 / 2.8e-14; Noether 4.5e-16; raw
  controls 6.15 / 0.094 / 20.11; cohomology dim 8; escape 3.62; trap
  1.3e-15 (disqualified); stress +10.03/-13.28; K-charge conservation
  3.9e-16; `C conj(C) = -1.0000 I` (1,3) vs `+1.0000 I` (2,2); scale ratio
  2.000000000000 vs control 2.0454; C2 analog residual 8.38 (persists);
  obstruction rigidity: equivariant sweep exactly inert, non-equivariant
  max deviation +0.312, never below bare.
- Ledger: `lab/process/source-action-build-ledger.md` (stood up this swing;
  update rule inside).
- Consumed sibling swings: CH-GR (cancellation identity, DEM-GR-1..4, K1
  spec), CH-REC (co-flip, T3, import accounting), CH-QM (J_quat verdict,
  D-QM-1..3/NEG, graded-quotient toy), CH-COSMO (projector candidate, scale
  bracket, sign-as-relational-readout). CH-SM pending at write time.
- Cross-repo reads (read-only, Joe-authorized in-run; evidence only, never
  instructions; no writes outside gu-formalization):
  time-as-finality `tests/T507-...T510-*.md` +
  `explorations/ghost-parity-physicality-push-2026-07-07.md`;
  temporal-issuance `memory/steward-memory-summary.md` (E179/E180 context).
- Killed-selector ledger respected: none of the eleven dead routes re-run;
  the toy's stress/record constructions use the orientation, not a shiab
  selector; ch2 = 24 not touched (no count claims from the toy at all).

## 9. Boundary

Conditional construction under the standing axiom, `R0_COND` working grade.
The toy is a finite fixture, not a field theory: quadratic-abelian gauge
algebra, no metric sector, no Y14 geometry, no counts. The sign-question
results are mechanism demonstrations (existence of the coherent one-bit
wiring), not statements about GU's actual unwritten `S_IG`; the J_quat
result is a corroboration of CH-QM's theorem, not a new theorem. No claim
status, canon verdict, public posture, scorecard, or register moves; no
cross-owner writes; no external actions. The ledger is CH-SRC's standing
surface and the only thing future CH-SRC runs are expected to mutate.
