---
title: "Blockbuster P1: the DE sign co-variance derived at toy grade; Prediction Packet 1 frozen (internal)"
status: active_research
doc_type: exploration
created: 2026-07-19
directed_by: "Joe direct chat, 2026-07-19 (blockbuster swing, Pathway 1: the falsifiable dark-energy sign prediction)"
axiom: lab/process/boundary-adapter-standing-axiom.md
extends:
  - explorations/channel-swing-CH-COSMO-2026-07-19.md
  - explorations/channel-swing-CH-GR-2026-07-19.md
  - explorations/pk2-gauge-covariance-2026-07-19.md
  - explorations/channel-swing-CH-SRC-2026-07-19.md
inputs:
  - tests/channel-swings/ch_cosmo_magnitude_mode_probe.py
  - tests/channel-swings/ch_gr_vev_stress_probe.py
  - tests/channel-swings/pk2_gauge_covariance_probe.py
  - tests/channel-swings/ch_src_minimal_action_toy.py
  - canon/theta-field-flrw-dark-energy-eos.md
  - explorations/assembly-archaeology-recovered-parameters-2026-07-19.md
  - explorations/channel-swing-CH-REC-2026-07-19.md
  - lab/process/research-portfolio.json
test: tests/channel-swings/bb_p1_sign_covariance_probe.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
packet_status: "PREDICTION PACKET 1 FROZEN (internal, conditional; Section 6). Nothing external."
---

# Blockbuster P1: the DE sign co-variance, and Prediction Packet 1

CH-COSMO Section 3 left `sgn(w_0 + 1)` one condition short of being a readout of
the transmitted Z/2: condition (ii), "a DERIVED, field-redefinition-stable
co-variance between the orientation and the mode's energy sign — without it a
sign is just a coefficient." This swing derives that co-variance at toy/symbol
grade, discharges condition (iii) (the second-sector reference) concretely, and
freezes Prediction Packet 1 (internal). Receipt:
`tests/channel-swings/bb_p1_sign_covariance_probe.py`, exit 0, **22/22 checks**.
Per archaeology item 9, no historical sign value is inherited anywhere: the
probe computes `w` from `p/rho` directly and independently re-derives the
quantities the old bug corrupted (`d ln rho_B/dz|_0 = 4.307` vs the
archaeology's 4.229 — never the hardcoded 3).

## 0. Five-lens council pass (inline; run before the plan was fixed)

**Cosmologist.** Anchor the observable in the expansion history, not in field
variables: `w_DE(z)` is defined from measured `H(z)` after subtracting matter,
so the theory-side task is to tie the sign of `(rho + p)_DE` — the source of
`Hdot` — to the orientation. Trap feared: treating the CPL `w_0` as the
observable itself; it is a fit-basis proxy that can leak near the LCDM limit,
so the primary observable must be the window-averaged `sgn(rho + p)_DE` with
CPL as proxy.

**Effective-action field theorist.** The "sign of a mode" is only meaningful as
the kinetic/Krein signature of the propagating eigenmode; Sylvester's law of
inertia is the theorem that makes it redefinition-stable, and total-derivative
shifts handle derivative redefinitions. Trap feared: the unbuilt `S_IG` doing
silent work — every place the actual action is assumed (one Krein form, Z_theta
> 0, mixing discharge) must be a NAMED condition, not background.

**Causal-inference statistician (severity/pre-registration).** Freeze the
decision rules and the packet template — observable, convention, conditional
chain, competitor baseline, kill thresholds — before any derivation output or
number is quoted; brackets from frozen rows only, quoted last. Trap feared: the
frozen `f0` brackets drifting from "bracket" to "support," and a
non-distinctive sign (shared with all of quintessence) being dressed as a
discriminating prediction.

**GR perturbation theorist.** The chain must ride the computed structures and
nothing else: branch-(a) with `sigma = +1` forced (A4: no real kappa
otherwise), the de Donder class as a named hypothesis (P-K2), FLRW riding the
`t1 = -<Ric.bhat>` sector (K5), the magnitude projector with its one slicing
residue (CH-COSMO A2). Trap feared: inheriting any old DE sign, or letting the
`kappa^2 = 1` target-read provenance gap disappear from the conditions.

**Philosopher of science (prediction vs retrodiction).** `w_0 >= -1` alone is
not distinctive — every standard single-field quintessence says it. What makes
this packet falsifiable-in-a-strong-sense is the RIGIDITY: under the derived
co-variance, a phantom-side reading cannot be reabsorbed by redefinition or
re-fitting; it forces the failure of one of four named structural links (a
computed identity chain), and one of those links (the GR cancellation) is
already frozen. Trap feared: retrodiction-compatibility marketed as
prediction; therefore the packet must state its non-distinctiveness explicitly
and put the novelty where it is — the conditional chain and the joint kill
surface.

**Chair synthesis (the fixed plan).** (1) Freeze the prereg: DERIVED / REFUTED
/ PARTIAL signatures for the co-variance claim, the swept redefinition classes,
and the packet template with no data values. (2) Derive the minimal
C10-consistent quadratic action for the magnitude mode about the
curvature-locked VEV, with the sign structure factored through the Krein norm
of the VEV ray under SRC-COH-1. (3) Prove the readout identity through
`(rho + p)_DE`. (4) Sweep the redefinition classes (Sylvester congruence,
positive-multiple point redefinitions, boundary-term derivative redefinitions,
reality exclusion of `B -> iB`); exhibit the two discrete sign-movers (tau-flip
= co-flip; global K-flip = relational identity). (5) Verify the sign map in the
frozen model shape with a fresh FLRW integration. (6) Score against the prereg;
freeze the packet; quote frozen-row brackets only after the freeze. All inline,
no subagents.

## 1. Pre-registration (frozen before the derivation and before the probe existed)

### 1.1 The claim and the decision rules

**Claim under test (CH-COSMO condition (ii)).** There exists a derived,
field-redefinition-stable co-variance between the transmitted orientation and
the magnitude mode's energy-density sign, such that `sgn(w_0 + 1)` is a
readout of the (relational) orientation and not a free coefficient.

**DERIVED signature.** All three legs land: (a) an exact identity ties the
side of `w = -1` to a single sector-sign datum multiplying the mode's
canonical stress — schematically `(rho + p)_DE = eps * Z * Bdot^2` with
`rho_DE > 0` — so the side is `eps` wherever the mode moves; (b) every
redefinition in the swept classes (real point redefinitions, real linear
mixings of the helicity-0 block, first-order derivative redefinitions)
preserves `sgn(eps_eff)` — kinetic signature is congruence-invariant and
derivative redefinitions shift the action by boundary/EOM terms only; (c) the
only operations that flip the readout side are the tau-flip (which co-flips
the GR cancellation solvability and the record arrow — so it is a different
theory, not a redefinition) and the global Krein flip (which flips the
reference too, leaving the relational readout invariant). If (a)-(c) land, the
co-variance is DERIVED at toy/symbol grade conditional on SRC-COH-1, and the
packet freezes.

**REFUTED signature.** An admissible redefinition inside the swept classes
flips `sgn(w_0 + 1)` while preserving the orientation and the GR identity.
Then the sign is a coefficient, not a readout; the packet does not freeze; the
missing structure must be named.

**PARTIAL signature.** Legs (a)/(b) land but (c) fails — e.g. a third discrete
sign-flipping operation exists that touches neither the orientation nor the
reference. Packet does not freeze; the loophole is recorded without smoothing.

**Swept-class boundary (declared now).** NOT swept: nonlocal field
redefinitions, derivative redefinitions beyond first order, quantum/measure
effects, and any redefinition that changes the reality structure of the field
space (excluded by fiat as not a redefinition of the same real theory). The
packet, if frozen, carries this boundary.

### 1.2 The packet template (no data values; brackets enter only in Section 6)

- **Observable:** the side of `w = -1` — primarily the window-averaged
  `sgn(rho_DE + p_DE)` over the fit window; CPL `sgn(w_0 + 1)` as the
  practical proxy, with basis-leakage named as a systematic.
- **Sign convention:** gate frozen conventions; `w = p/rho`; quintessence side
  (`w_0 + 1 > 0`) = positive `(rho + p)_DE` = orientation aligned with the
  matter-sector anchor.
- **Predicted side:** stated after derivation, from the chain — not from data.
- **Conditional chain:** the named channel-card items (Section 6).
- **Competitor baseline:** LCDM null (orientation-silent) and the phantom
  class; explicit non-distinctiveness vs generic quintessence on the bare
  sign.
- **Kill thresholds:** pre-declared sigma levels on the phantom side, plus the
  standing F1 amplitude tripwire as companion; admissible data =
  H46B-verified likelihood inputs only (DE-AMP rule).

## 2. The minimal C10-consistent action for the magnitude mode

Construction data (all frozen upstream, none new): the branch-(a)
curvature-locked VEV with `kappa^2 = 1`, `sigma = +1` (CH-GR A3-A5; provenance
DEM-GR-1/2 still open — a condition, not background); the de Donder
presentation as a NAMED hypothesis of the identity, not a convenience (P-K2:
the `t2`/stress slot is a de-Donder-class object; on FLRW the mode rides the
`t1 = -<Ric.bhat>` sector per the K2/K5 unification); the canonical quadratic
stress bilinear (DEM-GR-3(i)); the fiber-Frobenius magnitude projector with
its single slicing residue (CH-COSMO A1/A2); and SRC-COH-1 — ONE Krein form in
every slot of the action (sector grading, stress bilinear, record charge; the
CH-SRC coherence constraint whose violation is exactly the Da3 control that
breaks the alignment).

The magnitude mode is `B = delta|theta|` along the VEV ray `vhat`. Any
C10-consistent quadratic completion factors its sign structure through the
Krein norm of that ray, because under SRC-COH-1 the kinetic form and the
stress bilinear contract with the SAME Krein form that grades the sectors:

```
L_B = (tau * Z_theta / 2) * (Bdot^2 - M^2 B^2),      tau = <vhat, vhat>_K,
rho_B = tau * Z_theta * (Bdot^2 + M^2 B^2)/2,
p_B  = tau * Z_theta * (Bdot^2 - M^2 B^2)/2,
```

with `Z_theta > 0` the magnitude normalization C10 must emit (open, named) and
`M^2` in the admissible band {3, 7, 8} (value irrelevant below). The
orientation enters ONCE, as `tau` — this is the entire sign resource of the
sector, which is what makes the co-variance provable rather than plausible.
The branch-(a) VEV sits in the physical Krein sector, so `tau` here is the
same bit whose GR-slot image is `sigma` (probe C1/C2; the CH-SRC Da1/Da2
mechanism). Per the tri-repo Krein-sign result, the bit itself is ONE external
Z/2 posit (Godel-independent, not GU-derivable); what is GU-derivable is the
co-variance — how every sector reads the same posit.

## 3. The readout identity (probe Part A, exact)

With the two-component DE (`Lambda_eff` at `w = -1` exactly, plus the mode)
and `eps = tau * sgn(Z_theta)`:

```
rho_DE + p_DE = eps * Z * Bdot^2         (A1, exact; Lambda contributes zero)
w_DE + 1 = eps * Z * Bdot^2 / rho_DE     (A2)
```

Since the TOTAL `rho_DE` is empirically pinned positive (the frozen two-sided
scale row), the side of `w = -1` is exactly `eps`, pointwise, wherever the
mode moves. Three structural corollaries, all machine-checked:

- **Orientation-silent limit (A3).** `B = 0` gives `w_DE = -1` identically for
  both `eps`: no deviation, no readout — CH-COSMO condition (i) is confirmed
  as observational, not derivable.
- **Mass/band independence (A1).** No `M^2` appears in `rho + p`: the sign
  statement is identical at every admissible band point and in either regime
  (oscillating or slow-roll). The readout does not wait on OQ2.
- **Energy-density sign (A4).** `sgn(rho_B) = eps` too (positive-definite
  bracket), so `sgn(f0) = eps`: the "phantom side" is literally the
  negative-energy reading of the same mode — the Krein flip made kinematic.

## 4. The co-variance: three legs (probe Parts B-D)

**Leg (b) — the redefinition sweep (Part B).** (B1) Sylvester: six random
invertible congruences of an indefinite kinetic Gram (signature (2,1),
standing in for the multi-scalar helicity-0 block including the W78 scalaron)
all preserve the signature — no real linear mixing of the scalar block flips
the DE-carrying eigenmode's kinetic sign. (B2) Point redefinitions
`B -> lam B + mu B^2` multiply the quadratic kinetic coefficient by
`lam^2 > 0`. (B3) The first-order derivative redefinition `B -> C + alpha
Cdot` shifts the quadratic Lagrangian by an EXACT total derivative
`d/dt[(Z/2)(Cdot^2 - M^2 C^2)]` — same equations, same on-shell stress. (B4)
The only sign-flipping rescale is `lam^2 = -1`: no real solution — the
cosmological image of CH-GR A4's "no real kappa" gate. The sweep closes the
declared classes; the observable-side statement is even stronger: `w_DE(z)` is
defined from measured `H(z)`, so it is redefinition-invariant by construction,
and the sweep shows the theory-side attribution cannot drift either.

**Leg (c) — the two discrete sign-movers (Part C).** (C2/C3) The tau-flip:
under SRC-COH-1 the GR cancellation demand reads `tau * kappa^2 = 1`, solvable
over the reals iff `tau = +1`. Enumerating both values: the pair (mode energy
sign, GR-cancellation-alive) takes only the correlated values
`(+, alive)` and `(-, dead)`. **There is no configuration with a phantom-side
mode and a surviving branch-(a) cancellation.** Flipping the readout side by
flipping `tau` is not a redefinition — it kills a computed identity elsewhere
in the same construction (and co-flips the record arrow, per CH-REC). (C4) The
global Krein flip: the readout depends only on the PRODUCT
`tau_theta * tau_ref`; flipping every sector at once (anchor relabel) leaves
it invariant. This discharges CH-COSMO condition (iii) CONCRETELY: the
second-sector reference is the observed matter sector, compared to the theta
sector by gravity itself — both source the same `H(z)` through the Friedmann
equations, so the comparator is not an abstract Krein reference but the
expansion history. What the measurement reads is the relative orientation of
the cosmological sector against the matter anchor, exactly the relational
structure H-REC requires.

**Leg (a) verified in the frozen model shape (Part D).** Fresh RK4 integration
of the mode on an LCDM background from `z = 30` (frozen IC where `H/M ~ 33`),
`w` computed directly from `p/rho` — no inherited sign, no hardcoded
`d ln rho`: for `eps = +1`, `w_DE(0) > -1`, pointwise `w_DE(z) >= -1` on
`[0,2]`, CPL-fit `w_0 + 1 > 0`; for `eps = -1` all three flip; the map
`eps -> sgn(w_0+1)` is the identity at `f0 = 0.005, 0.02, 0.1` (D1-D3) — the
CPL proxy never leaks across `w = -1` for this model shape. Independent
cross-checks against frozen rows: `C_inst = 1.431` and `1 + w_B(0) = 1.438`
(canon Result 2: 1.39, reconstruction grade — 3% off, consistent with IC
detail); `d ln rho_B/dz|_0 = 4.307` against the archaeology's 4.229 — the
bug-corrupted quantity, recovered independently and never used to build
`w(z)`.

## 5. Verdict against the prereg: DERIVED (toy/symbol grade, conditional)

All three legs land; the REFUTED and PARTIAL signatures did not fire; no third
sign-mover was found inside the swept classes. The co-variance — CH-COSMO's
condition (ii) — is **DERIVED at toy/symbol grade**, conditional on exactly
these named items:

1. **SRC-COH-1** (one Krein form in every slot). Axiom-grade: exhibited and
   control-tested in the CH-SRC toy (Da3 shows its violation breaks the
   alignment), not derived from the unbuilt `S_IG`.
2. **`Z_theta > 0` emitted by C10.** Open. If C10 emits `Z_theta < 0`, the
   readout formula stands but the predicted side flips — the packet's
   prediction is stated conditional on `Z_theta > 0` and a sign-emitting C10
   computation would sharpen, not break, the packet.
3. **Scalar-block mixing discharge** (single-mode dominance in the DE window,
   including the W78 scalaron) — CH-COSMO's named closure computation. Without
   it, the DE window could be shared between eigenmodes of both signatures
   and the net side becomes amplitude-dependent.
4. **Branch-(a) realization with `sigma = +1`** (computed identity; de Donder
   class as construction data per P-K2; source-side provenance DEM-GR-1/2
   open).

What is NOT claimed: no continuum `S_IG`, no derivation of the external Z/2's
value (Godel-independent posit; the construction pins its unique VIABLE value,
which is different), no data support, no claim-status movement.

**Consequence: the prediction exists.** Under conditions 1-4 the aligned
orientation is FORCED (`tau = +1` is the only value with the GR cancellation
alive), hence `eps = +1`, hence the deviation — if any exists — must sit on
the quintessence side, pointwise in `z`. A phantom-side reading is not a
parameter surprise; it contradicts the chain.

## 6. PREDICTION PACKET 1 — FROZEN (internal, conditional)

*Frozen in this section in full before any bracket numbers are quoted; the
brackets in PP1-7 are frozen repo rows, cited not re-audited. Internal only:
nothing external, no promotion to any public surface.*

- **PP1-1 Observable.** The side of `w = -1` for the dark-energy background:
  primary — the sign of the window-averaged `(rho_DE + p_DE)` over the
  analysis window (`z <= 2`); proxy — CPL `sgn(w_0 + 1)`, valid only when the
  detected deviation is robust to the `w(z)`-basis choice (basis leakage is a
  named systematic).
- **PP1-2 Sign convention.** Gate frozen conventions, `w = p/rho`;
  quintessence side `w_0 + 1 > 0` <=> `(rho + p)_DE > 0` <=> theta-sector
  orientation ALIGNED with the observed matter-sector anchor (relational
  readout `tau_theta * tau_ref = +1`); both X4 signature conventions covered
  per the CH-SIG77 port receipt.
- **PP1-3 Predicted value.** `w_0 + 1 > 0` and pointwise `w_DE(z) >= -1` for
  all `z` — the mode can NEVER cross to the phantom side, at any redshift, in
  any admissible band point, in either dynamical regime. The LCDM limit
  (`f0 = 0`) is orientation-silent: compatible, not confirming.
- **PP1-4 Conditional chain (channel cards, exact).**
  (i) CH-GR card G3-G7: branch-(a) cancellation identity with `sigma = +1`,
  `kappa^2 = 1`, de Donder class as named hypothesis (P-K2 verdict);
  (ii) CH-SRC SRC-COH-1: one Krein form in every action slot;
  (iii) CH-COSMO construction items 3-4: `Z_theta > 0` and the scalar-block
  mixing discharge (incl. W78 scalaron);
  (iv) CH-COSMO A2: the single boundary slicing datum (nondegenerate
  `d|theta_bar|/dt != 0`);
  (v) H-COSMO itself: the identification of the cosmological scalar channel
  with the magnitude mode.
  The ORIENTATION-READOUT interpretation (a measured sign = the transmitted
  Z/2 against the matter anchor) additionally requires H-REC's co-flip
  identification; the bare sign prediction PP1-3 requires only (i)-(v).
- **PP1-5 Competitor baseline.** LCDM: `w_0 + 1 = 0` exactly (null;
  orientation-silent). Generic single-field quintessence: also predicts
  `w >= -1` — **the bare sign is NOT distinctive**; the distinctive content is
  (a) the rigidity (a phantom reading forces failure of a named link in a
  computed identity chain, not a re-fit), (b) the joint surface with the
  standing F1 amplitude tripwire and the frozen amplitude brackets, and
  (c) the relational interpretation (iv the readout is the co-flip
  consistency test of H-REC). Phantom-class models (`w_0 < -1` or crossing)
  are the discriminated class.
- **PP1-6 Kill thresholds (pre-declared).**
  - **KILL-P1-A:** an admissible dataset (H46B-verified likelihood inputs
    only, per the DE-AMP rule) yields `w_0 + 1 < 0` at >= 2-sigma with the
    deviation attributed to the DE background EOS and robust to the
    `w(z)`-basis choice. Kills the conjunction of PP1-4(i)-(v): at least one
    named link fails (which one is a follow-up computation, not a rescue).
  - **KILL-P1-B (stronger, pointwise):** a >= 3-sigma reconstruction-level
    detection of `w_DE(z) < -1` on ANY sub-window of `z <= 2`. The model
    forbids crossing entirely, so this kills the conjunction (H-COSMO
    identification + aligned chain) even if `w_0` itself sits on the
    quintessence side. This is the live risk direction: the current DESI-CPL
    preferred region implies crossing at moderate `z`; if that ever becomes a
    robust pointwise statement, PP1 dies. The packet is genuinely exposed,
    which is what makes it a prediction.
  - **Companion (existing, unchanged):** DE-F1-TRIPWIRE — 2-sigma exclusion of
    `w_a/(w_0+1) > -3.5` fires the amplitude ceiling (`B_i > 3 M_Pl`).
  - **Non-firing outcomes:** continued LCDM-consistency leaves PP1 untriggered
    (not confirmed — orientation-silent). A quintessence-side detection is
    consistent-with, not proof-of, the chain (severity honesty: many models
    share the side).
- **PP1-7 Brackets (frozen repo rows, quoted after freeze).** Total scale
  pinned two-sided: `rho_DE ~ (2.24 meV)^4 ~ 1e-123 M_Pl^4`, known to < 10%
  (H46C leg) — this is what makes the denominator sign in the readout identity
  empirical, not assumed. Split one-sided: `f0 in [0, 0.027]` canonical BC_1
  (`[0, 0.039]` A_1; `[0, 0.208]` softest S^3 point) — so the predicted
  deviation, if present, lives in `w_0 + 1 = 1.39 f0 in (0, ~0.038]`
  canonical (band-softest to `~0.29`); every DESI-signal-reproducing amplitude
  is already excluded band-wide at `dchi^2 >= +33.5` (W129), i.e. PP1's live
  scope is the surviving LCDM-mimic band. F1 status: tightest 2-sigma edge
  `-2.39` (DESY5) vs kill line `-3.5`, live margin `+1.11` (W226). No new
  data are read; the Lane 2 DE-AMP audit remains the data-facing leg and is
  not re-run here.

**Ledger notes (proposals for owners; not applied).** CH-COSMO A3 (sign
linkage adapter item) can now read "co-variance derived at toy grade; enters
via SRC-COH-1" instead of "enters only if derived." CH-COSMO K4 (sign-link
kill) is now OPERATIONAL as KILL-P1-A/B. PRED-CANDIDATE-PACKETS packet-1
draft requirement (predeclare observable, convention, conditions, competitor,
kill threshold before likelihood work) is MET by this section. The
sign-of-any-detected-deviation flag for the next Lane 2 DE-AMP run doubles as
the first live read of PP1.

## 7. Publishable grade and honest odds

**What would make this publishable-grade.** (1) The C10 action at
construction grade, emitting `Z_theta > 0` and the scalar-block mixing
discharge — without it the "minimal action" of Section 2 is a
structure-forced shape, not a derived Lagrangian; this is the same single
decisive computation CH-COSMO already names. (2) SRC-COH-1 derived as a
property of `S_IG` (or stated as one of its axioms with the mini-rep fixture
as regression), not assumed. (3) Source-side provenance for
`sigma = +1, kappa^2 = 1` (DEM-GR-1/2) — until then the GR anchor of the
co-flip is target-read. (4) A detected `f0 != 0` — without a deviation the
packet is untriggered forever. (5) Severity work: a competitor-separation
analysis showing what, beyond the bare side, distinguishes the chain
(the joint sign + amplitude-ceiling + no-crossing surface is the candidate),
pre-registered against a future dataset generation.

**Honest odds.** That the co-variance derivation as scoped here survives
scrutiny at its own grade: high (~85%) — the legs are elementary and
machine-checked; the exposure is in the framing (SRC-COH-1 as axiom).
That the full chain reaches genuinely publishable
distinctive-prediction grade (conditions 1-3 discharged at construction
grade): low near-term, ~10-20%, gated by the same C10/S_IG bottleneck as
everything else. That PP1 survives its kill tests if the DESI-era crossing
hint consolidates: the packet is genuinely at risk — if the current
preferred CPL region becomes a robust pointwise crossing detection,
KILL-P1-B fires; call it ~60/40 survival on present frozen-row information,
and that exposure is the point. The bare-sign non-distinctiveness is
permanent and stated: the publishable object is the conditional chain and
its kill surface, never the side alone.

## 8. Receipts

- Probe: `tests/channel-swings/bb_p1_sign_covariance_probe.py`, run
  2026-07-19, exit 0, 22/22 PASS. Exact legs in sympy (readout identity,
  redefinition sweep, co-flip enumeration, relational product); numeric leg
  fresh RK4 (`M^2 = 8`, LCDM background, `z = 30` start), seed 20260719 for
  the Sylvester congruences.
- Key numbers: `(rho+p)_DE = eps Z Bdot^2` exact; Sylvester signature (2,1)
  invariant across 6 congruences; O(alpha) redefinition shift = exact total
  derivative; `tau = -1` admits no real kappa (A4 reproduced); co-flip
  enumeration `[(+1, +1, alive), (-1, -1, dead)]`; readout =
  `tau_theta * tau_ref` (global flip invariant); D-leg at
  `f0 = 0.005/0.02/0.1`, both orientations: sign map is the identity, e.g.
  `f0 = 0.02`: `w(0) = -0.9718` / CPL `w_0 = -0.9539` (`eps = +1`) vs
  `w(0) = -1.0293` / CPL `w_0 = -1.0497` (`eps = -1`); cross-checks
  `C_inst = 1.431` (canon 1.39), `d ln rho_B/dz|_0 = 4.307` (archaeology
  4.229; never 3, never used to build `w`).
- Prereg discipline: Sections 0-1 were fixed before the probe script existed;
  the probe echoes the prereg in its header and the verdict (Section 5)
  scores against Section 1.1 without reinterpretation. One numerical repair
  was made after the first run (the z = 0 field values were read from the
  RK4 overshoot point, corrupting the D5 finite difference; fixed to
  interpolate at N = 0 exactly) — a bug fix in the receipt machinery, not a
  criterion change; no prereg rule was touched.
- Killed-selector ledger respected: none of the eleven dead routes re-run;
  branches (b)/(c) not resurrected; no historical DE sign inherited
  (archaeology item 9); the DESI-signal exclusions and F1 edge are cited
  from frozen rows (W129/W226), not recomputed.

## 9. Boundary

Conditional construction under the standing axiom, `R0_COND` working grade.
The co-variance is derived at toy/symbol grade conditional on the four named
links; the external Z/2 remains an external posit (Godel-independent) whose
unique VIABLE value the construction pins — pinning viability is not deriving
the posit. PREDICTION PACKET 1 is INTERNAL: it moves no claim status, no canon
verdict, no scorecard row, no register, no public posture, and routes nothing
externally; the Lane 2 DE-AMP audit remains the only data-facing leg and is
untouched. Frozen rows are cited, never re-audited. The swept-redefinition
boundary (no nonlocal, no higher-derivative, no quantum/measure) travels with
the packet.
