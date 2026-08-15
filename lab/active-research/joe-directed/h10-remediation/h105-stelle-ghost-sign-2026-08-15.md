---
artifact_type: exploration
status: exploration
doc_type: falsifier-remediation-gate
created: 2026-08-15
work_item: H10-5
channel: h10_remediation
route: REMEDIATE__THE_ONLY_SOLAR_SYSTEM_FALSIFIER
base_revision: not-read (no git commands run in this channel)
target_claim: "INTERNAL targets (the source-claim register carries NO entry for PPN, Cassini, Stelle or solar-system tests -- verified by absence sweep, control C10 -- so this remediation is correctly typed against REPOSITORY claims, not against a registered source claim). T1: the repo-wide 'the Yukawa strength alpha_Y = 1/3, forced, vDVZ trace factor' (path4-wave2-alphaW L133; track2-conditional-numbers L111/L193; tests/W61 L233; tests/W66 L125). T2: H10's 'gamma - 1 = -(2/3) e^{-m2 r}'. T3: H10 Q2a's 'gamma(m2 r -> 0) = 1/2 anchors the linearization, so a linearization error would have shown up here'. T4: H10 Q4's 'GATED-ON-mu_DW, effectively PASSES (not falsified)'. T5: H10 Q1b's 'the massive spin-2 flips sign between the temporal and spatial potentials'. SCOPE: every verdict below binds the tree-level Stelle-clear model H10 names (R^X + Weyl^2 + Lambda, no R^2), conditional on the soldering postulate and on H15/H25's identification of GU's TT operator as box(box+m2^2). It does NOT bind Weinstein's full construction."
target_claim_verdict: "T1 REFUTED in magnitude AND sign: alpha_Y = -4/3, REPULSIVE, not +1/3 attractive -- magnitude x4, and a ghost as the fourth-order operator requires. T2 SIGN REFUTED, MAGNITUDE UPHELD: gamma - 1 = +(2/3)e^{-m2 r}; GU predicts gamma > 1, not gamma < 1, and the leading magnitude is unchanged. T3 REFUTED as an anchor: 1/2 is the massive-mode-only value, is also the Brans-Dicke omega=0 value, and is exactly what the WRONG assignment produces -- a check that could not fail. Replaced by the discriminating Einstein-Weyl endpoint gamma(m2 r -> 0) = -1. T4 UPHELD, NUMERICALLY UNCHANGED: GU still clears Cassini; mu_DW floor 1.485e-17 eV, cleared by 44.9 decades at natural mu_DW ~ M_Pl. T5 REFUTED: both potentials are repulsive; they differ in MAGNITUDE 4/3 vs 2/3, not in sign. HEADLINE: the banner's physics VERIFIED independently from structure, and the verdict did NOT move -- because Cassini bounds |gamma-1| two-sided and the leading magnitude is degenerate between the wrong and the corrected assignment (floors differ by 5.6e-6 relative). A bar whose verdict is invariant under a x4 sign-flipping error in its own central input is WEAK, and that is a statement about the test, not about GU."
canon_verdict_change: none
priority_change: none
steering_effect: unchanged
canonical_effect: pending_integration
title: "H10-5: the 2026-08-09 banner is RIGHT and now DERIVED, not transcribed -- the massive spin-2 is a GHOST with alpha_Y = -4/3 REPULSIVE (not +1/3 attractive), gamma - 1 flips to +(2/3)e^{-m2 r}, and GU STILL CLEARS Cassini by 44.9 decades with the floor moving by 5.6e-6 relative, because Cassini is two-sided and the |gamma-1| magnitude is degenerate between the two assignments -- a THIRD non-discriminating check beyond the two the banner named, and the one the verdict actually rides on"
grade: "REMEDIATION with independent re-derivation. The banner's assignment was NOT taken on trust: the coefficients are derived from trace reversal in D dimensions, tracelessness of the spin-2 projector, static-source saturation, and the residue structure of box(box+m2^2) -- no literature number is an input -- and only then compared to the five citations, which agree. Exact sympy Rational throughout sections D/E; floats confined to section O, declared in FLOAT_INPUTS, and read by no exact claim. 48/48 checks via tests/channel-swings/joe_directed_h105_stelle_ghost_sign.py under _local/cas-venv from the repository root; split [D] 13 derivation, [E] 8 exact PPN, [R] 5 reproductions asserted before use, [O] 7 observational, [C] 15 controls. FAILURE PATH EXERCISED: 14 planted false facts each drive exit 1, and the clean run exits 0. TWO CONTRARY CONTROLS, both firing: an internal GU configuration at mu_DW = 1e-18 eV that violates the bar by ~4.4e4x, and the external Brans-Dicke omega=100 comparator at 426x. The target file tests/wave22/H10_ppn_weak_field.py now runs 28/28 exit 0, up from exit 1 behind a known-defect guard. NOT: a re-linearization of GU's |II|^2 action with matter sources (SA-G9 stays open), a computed PPN beta (still argued structurally), a derivation of mu_DW, a loop-level statement, a canon or ledger edit, or a claim that GU is consistent."
disposition: BANNER_PHYSICS_INDEPENDENTLY_CONFIRMED__COEFFICIENTS_CORRECTED_AND_UPGRADED_FROM_ARGUED_TO_COMPUTED__GUARD_REMOVED__VERDICT_UNCHANGED_BECAUSE_THE_BAR_IS_DEGENERATE_UNDER_ITS_OWN_ERROR__FALSIFIER_RESTORED_BUT_RANKED_DOWN
rows_proposed: []
rows_advanced: 0
free_object_delta: 0
depends_on:
  - tests/wave22/H10_ppn_weak_field.py
  - explorations/wave22/H10-ppn-weak-field-2026-07-11.md
  - lab/methods/source-native-comparator-routing.md
  - lab/sources/source-claim-register.yaml
  - lab/active-research/joe-directed/archaeology/ar1-dropped-commitments-ledger-2026-08-15.md
  - explorations/track2-conditional-numbers-2026-07-13.md
scripts:
  - tests/channel-swings/joe_directed_h105_stelle_ghost_sign.py
---

# H10-5 — restoring the repository's only solar-system falsifier

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.
> Classification: `CONVENTIONAL_COMPARATOR`.

**Why that classification.** The comparator here is four-derivative (Stelle) quadratic gravity: its
linearized point-mass potential, its spin-2 ghost, and the PPN parameters `gamma, beta` confronted
with Cassini and LLR. Every coefficient computed below binds *that named model*. It becomes a
statement about GU only through the repository's own prior identification (H15/H25) that GU's
tree-level TT graviton operator **is** `box(box + m2^2)` with `m2^2 = m^2_eff mu_DW^2`. This
artifact **consumes** that identification and does not adjudicate it. Nothing here is evidence for
or against Weinstein's source-native construction without that bridge, and the bridge is not mine.

---

## The assignment

`tests/wave22/H10_ppn_weak_field.py` is the repository's **only** Cassini/LLR bar. Its own
2026-08-09 banner recorded that its Yukawa assignment was wrong — spin-2 coefficient `-4/3`, not
`+1/3` — and left the constants unedited because the fix "changes behaviour and propagates". The
file had also been made unparseable by that same banner (prepended as a second module docstring,
pushing `from __future__ import annotations` off the front); the parse was repaired earlier today,
and the file was then gated behind a known-defect guard rather than shipped with a verdict computed
from an assignment its own header disavowed.

My job: verify the banner's physics **independently**, apply the remediation, recompute the verdict,
and remove the guard only if the work is genuinely complete.

---

## PREFLIGHT — five specialist lenses, run inline before any edit

**1. Quadratic-gravity linearisation.** The object is `R + Weyl^2` with no `R^2`. The TT operator is
fourth-order, `box(box + m2^2)`. Partial fractions give `1/(k^2(k^2+m2^2)) = (1/m2^2)[1/k^2 -
1/(k^2+m2^2)]`: two poles, opposite-sign residues. The relative minus sign **is** the ghost, and it
is available from the operator alone. Anything claiming an attractive massive spin-2 Yukawa in this
theory is claiming the massive pole has the same-sign residue as the massless one, which contradicts
the operator. *Prediction before computing: the banner's REPULSIVE claim will verify.*

**2. PPN formalism.** `gamma = Psi/Phi` requires **both** potentials. A build that only tracks the
temporal potential cannot get `gamma` right, and cannot notice that the temporal and spatial Yukawa
coefficients differ. *Watch for: an assignment that assumes the two coefficients are equal and
opposite.* (They are not: `4/3` and `2/3`, same sign.)

**3. Projector algebra.** Two different numbers both equal `1/3` in D=4 and are easy to swap: the
spin-2 projector's own `theta theta` trace coefficient `-1/(D-1)`, and the Fierz-Pauli numerator
trace coefficient `1/(D-1)`. The *potential* coefficient is neither — it is the **ratio**
`(1 - 1/(D-1))/(1 - 1/(D-2))`. *This is precisely where the banner says the error occurred, and it
is checkable without any external fetch.*

**4. Solar-system observational bounds.** Cassini's `|gamma - 1| < 2.3e-5` is a **two-sided** bound
on an absolute value. *Therefore a pure sign flip in the prediction cannot, by itself, change the
verdict.* Flagged before computing, and it turned out to be the whole story.

**5. Unit and convention hygiene.** Signature `(-,+,+,+)` vs `(+,-,-,-)` flips intermediate signs.
The banner cites Giacchini with the opposite signature to Lu et al. and reports the same answer. My
derivation fixes the convention once, at the source saturation step, and never changes it.

**6. Adversarial reading of my own arithmetic.** A remediation that "fixes" a file to match a
comment is the same failure mode as the original transcription. *Rule adopted before starting: the
banner's numbers are an* output *to be compared against, never an* input. If my derivation had
disagreed with the banner, the finding would have been that the banner is wrong.

**Retrieval before the work.** No prior remediation attempt exists (`lab/.../h10-remediation/` did
not exist). The diagnosis is recorded as settled in `explorations/SESSION-INDEX-2026-08-09.md` and
as owed in `lab/process/exploration-absorption-priorities-2026-08-10.md` and
`ar1-dropped-commitments-ledger-2026-08-15.md` row 3. The `4/3`, `vDVZ` and `alpha_Y` searches also
turned up the propagation set — six files beyond the two the banner named. That is a finding in
itself and is reported below.

---

## The derivation — no literature number is an input

Four structural steps, all exact.

**Step 1 — the two trace coefficients, both derived.**

- *Massless*, from **trace reversal** in D dimensions. Harmonic gauge gives
  `box hbar_{mn} ~ T_{mn}` with `hbar_{mn} = h_{mn} - (1/2) eta_{mn} h`. Tracing:
  `hbar = h(1 - D/2)`, so `h = -2 hbar/(D-2)`, and inverting,
  `h_{mn} = hbar_{mn} - (1/(D-2)) eta_{mn} hbar`. The `1/(D-2) = 1/2` is forced.
- *Massive*, from **tracelessness** of the spin-2 projector. `P^(2) = (1/2)(th th + th th) + a th th`
  has first-pair trace `(1 + a(D-1)) th`, so `a = -1/(D-1) = -1/3`.

This second number, `-1/3`, is the correct intermediate the 2026-07-11 build mis-slotted.

**Step 2 — saturate on a static point mass.** Signature `(-,+,+,+)`, `T_{00} = M`,
`T = eta^{00}T_{00} = -M`. Both `T.T'` and `T T'` collapse to `M M'`. Temporal weights:
`1 - 1/2 = 1/2` massless, `1 - 1/3 = 2/3` massive. Spatial weights: `1/2` and `1/3`.

```
temporal ratio  (1 - 1/3)/(1 - 1/2) = 4/3     <- the van Dam-Veltman-Zakharov enhancement
spatial  ratio  (1/3)/(1/2)         = 2/3
massive sector alone: Psi/Phi = (1/3)/(2/3) = 1/2   <- the genuine vDVZ / Fierz-Pauli value
massless sector alone: Psi/Phi = 1                  <- GR
```

**Step 3 — the sign, from the operator.** `1/(k^2(k^2+m2^2))` has residue ratio `-1` between the
massive and massless poles. Which pole is the ghost is fixed by requiring the *massless* residue to
give **attraction** (Newton); the other then has no freedom left. The massive spin-2 is a ghost and
its Yukawa is **repulsive**.

**Step 4 — assemble.**

```
Phi(r) (g_00) = -(GM/r)[1 - (4/3) e^{-m2 r}]        REPULSIVE Yukawa, magnitude 4/3
Psi(r) (g_ij) = -(GM/r)[1 - (2/3) e^{-m2 r}]        REPULSIVE Yukawa, magnitude 2/3
V_full(r)     = -(GM/r)[1 - (4/3)e^{-m2 r} + (1/3)e^{-m0 r}]
```

The scalaron `+1/3` follows independently from Stelle's `r -> 0` finiteness of the *full* theory,
`1 - 4/3 + c0 = 0`, given the spin-2 term. (That sum rule is symmetric under the swap, so it never
discriminated on its own — it is used here only to fix the scalar *after* the spin-2 is settled.)

### The banner verifies, on both legs

- Normalising Lu–Perkins–Pope–**Stelle** Eq. (4.7a) to a unit Newtonian term gives
  `(1/3)(e^{-m0 r} - 4 e^{-m2 r} + 3)`, which equals the derived bracket **exactly** (control R3).
- The banner's stated *trap* potential, `psi = -(GM/r)[1 - (2/3)e^{-m2 r} - (1/3)e^{-m0 r}]`, is
  reproduced independently: the spatial spin-2 coefficient `2/3` from Step 2, and the spatial scalar
  `-1/3` forced by the Brans–Dicke `omega = 0` endpoint `gamma = 1/2`. Both same sign, as warned.

**Verdict on the banner: CONFIRMED, independently, with zero external fetch.** Had it disagreed I
would be reporting the banner as wrong; it does not.

### The trap, not repeated

The banner warns that a stray `1/3` on the spin-2 term may come from misreading the spatial
potential. Control C5 substitutes the spatial pair `(2/3, -1/3)` into the temporal slot: it
reproduces **neither** the correct temporal bracket **nor** the old wrong assignment. Misreading
`psi` does not rescue `+1/3`. *(This control failed on its first draft because I used one symbol
for both exponentials, silently setting `m0 = m2` and collapsing the trap bracket onto the true one.
The fixed control keeps them distinct and asserts the collapse only under explicit substitution.)*

---

## The recomputed verdict

```
gamma(r) = (1 - (2/3)e^{-m2 r}) / (1 - (4/3)e^{-m2 r})
gamma - 1 = +(2/3) e^{-m2 r} + O(e^{-2 m2 r})        POSITIVE  (was -(2/3): sign refuted)
gamma(m2 r -> oo) = 1                                 GR recovered
gamma(m2 r -> 0)  = -1                                Einstein-Weyl  (the WRONG assignment gives +1/2)
short-range Phi bracket -> 1 - 4/3 = -1/3             gravity REPULSIVE below the Yukawa range
```

Cassini `|(2/3)u/(1 - (4/3)u)| < 2.3e-5` with `u = e^{-m2 r}` gives `m2 r > 10.2746`, hence at 1 AU
`m2 > 1.355e-17 eV`, and with `m2 = sqrt(m^2_eff) mu_DW` at the conservative `m^2_eff = 5/6`:

| quantity | corrected | previously published | moved? |
|---|---|---|---|
| `alpha_Y` (temporal Yukawa strength) | **`-4/3`, repulsive** | `+1/3`, attractive | **x4 and sign** |
| `gamma - 1` leading | **`+(2/3)e^{-m2 r}`** | `-(2/3)e^{-m2 r}` | **sign only** |
| `m2 r` floor | `10.274597` | `10.274540` | `5.6e-6` relative |
| `mu_DW` floor | `1.485e-17 eV` | `~1.5e-17 eV` | no |
| clearance at `mu_DW ~ M_Pl` | `44.9 decades` | `~45 decades` | no |
| **verdict** | **GATED-ON-mu_DW, effectively PASSES** | same | **no** |

### GU still clears the bar — and the reason it does is the finding

**GU passes Cassini/LLR, by 44.9 orders of magnitude.** No falsification. I went looking for one and
it is not there, and I am not going to manufacture it: Cassini bounds `|gamma - 1|`, two-sided, and
the leading **magnitude** `(2/3)e^{-m2 r}` is **identical** under the wrong and the corrected
assignment. Only the sign differs. So a `x4`, sign-flipping error in this bar's central input moved
its published floor by **parts per million** and moved its verdict **not at all**.

The 2026-08-09 banner named two checks that fail to discriminate (the `r->0` sum rule, and the
`gamma = 1/2` endpoint). **This is a third, and it is the one the verdict actually rides on.** The
banner's own sentence — "that sign is the entire observational content here" — is exactly right, and
its corollary is that at Cassini precision *that content is currently unmeasurable*.

On the sign itself: Bertotti et al. measured `gamma - 1 = (2.1 +/- 2.3)e-5`, a positive central
value consistent with zero at `0.91 sigma`. The correction moves GU's predicted deviation onto the
same side as the central value. **The statistical significance of that is zero.** Recorded so that
nobody, in either direction, reads more into the sign flip than a null measurement supports.

---

## Hostile review, inline

**"You fixed a file to match a comment — the same failure mode you are remediating."** Rejected, and
this was guarded structurally: the banner's numbers enter only as comparison targets in section
`[R]`, after section `[D]` has produced the coefficients. If `[D]` is deleted, `[R]` has nothing to
compare against and the run fails.

**"Your derivation asserts the massless `1/(D-2)`."** *This landed.* First draft derived the massive
`-1/(D-1)` from tracelessness but asserted `1/(D-2)`. Fixed: it is now derived from trace reversal
(`h = -2 hbar/(D-2)`), so both numbers entering the vDVZ ratio are derived and the ratio rests on no
transcription. Checks `Q1-D1b` / `D2a`.

**"Is the sub-leading term degenerate too?"** No — `+8/9 u^2` corrected vs `+2/9 u^2` wrong. At
`u ~ 3.45e-5` that is `~1e-9` against a bound of `2.3e-5`. The degeneracy claim is made at the
precision that matters, and the `5.6e-6` figure comes from an **exact solve** of the full rational
`gamma`, not from the truncated series (check `Q3a2` runs both routes and requires agreement).

**"`beta` is not recomputed."** Correct, and now stated as an honest limit in both files. `beta -> 1`
is an *argued structural* statement (the nonlinear correction is also `O(e^{-m2 r})`), true under
either assignment, and Cassini `gamma` is the binding bar. It is the weakest link in Q2.

**"The pass is vacuous — the bar never fails anything."** It did not, and that was a real defect.
Two contrary controls are now in the bar itself: an internal GU configuration at `mu_DW = 1e-18 eV`
giving `|gamma-1| = 1.0` (`~4.4e4x` the bound, **FALSIFIED**), and the external Brans–Dicke
`omega = 100` comparator at `9.8e-3` (`426x`, **FALSIFIED**, reproducing the repo's W220 control).

**"Scope creep — is this a claim about GU?"** Bounded explicitly: the tree-level Stelle-clear model
H10 names, conditional on the soldering postulate and H15/H25's operator identification. Not
Weinstein's full construction. The matter coupling is still imported; `SA-G9` stays open.

---

## POSTFLIGHT — five lenses on the finished work

**1. Did the verdict change, and was I honest about it?** No, and yes. A no-change outcome after a
`x4` sign-flipping correction is a surprising result and the temptation is to dress it as either a
vindication or a catastrophe. It is neither: it is a measurement of *this bar's* discriminating
power. Both edited files now say so in their own verdict blocks.

**2. Exactness discipline.** Sections `[D]`/`[E]` are sympy `Rational`/symbolic throughout. Floats
appear only in `[O]`, are enumerated in `FLOAT_INPUTS`, and no exact assertion reads one. The two
threshold routes (exact solve vs leading-order) agree to `5e-5` in `m2 r`.

**3. Failure path.** 14 planted false facts, each forcing exit 1; the clean run exits 0. The plants
cover every load-bearing number: both trace coefficients, the projector trace, the ghost sign, both
enhancements, the `gamma-1` sign, the discriminating endpoint, the degeneracy, the `mu_DW` floor,
the contrary control's non-vacuity, and the anti-drift hooks into both edited files.

**4. Anti-drift.** The probe **executes** `H10_ppn_weak_field.py` and reads its actual stdout and
exit code, rather than grepping for a literal. This caught my own bad check: I had grepped for a
hardcoded `sp.Rational(-4, 3)`, which fails against a remediated file that *derives* the constant.
The record and the certificate cannot now diverge.

**5. Blast radius honesty.** The banner named two files. The wrong coefficient is live in **six
more**, all outside this channel's write scope, all still wrong, all enumerated below. I did not
touch them and I am not reporting the correction as complete.

**6. What this does NOT establish.** That GU's gravity is right; that `mu_DW ~ M_Pl`; that the
massive mode is harmless (BAR 1, loop-level unitarity, is untouched — and the mode kept is the
*ghost*); or that the matter coupling is derived (`SA-G9`).

---

## Guard: removed, and why that was allowable

The known-defect guard is **removed**. The condition it named is discharged: the constants carry
`-4/3` / `-2/3` / `+1/3`; every dependent comment and derivation site the banner listed is edited;
the exploration note is edited; and the assignment is no longer transcribed at all — Q1 derives it.
Removing the guard on the strength of the banner's citations alone, without the derivation, would
have repeated the original mistake in the opposite direction.

`tests/wave22/H10_ppn_weak_field.py` now runs **28/28, exit 0** (from exit 1 behind the guard, and
`SyntaxError` before that).

---

## Owed, and deliberately not done here

`alpha_Y = 1/3` is live in six files outside this channel's write scope:

| file | sites |
|---|---|
| `explorations/track2-conditional-numbers-2026-07-13.md` | L111, L119, L193, L196, L227 |
| `explorations/path4-branchA-eos-gravity-correlation-2026-07-11.md` | L37, L70, L72, L167 |
| `explorations/path4-wave2-alphaW-parameter-free-2026-07-11.md` | L52, L112, L115, L133, L221 |
| `tests/W61_path4_A_eos_gravity.py` | L36, L233-236 |
| `tests/W66_path4_wave2_alphaW.py` | L118, L125-129, L174 |
| `tests/W138_issuance_kill_battery.py` | L147 |

All six still exit 0 with the wrong coefficient, which is the propagation failure this repository's
`correction_propagation_audit` gate exists to catch. **Direction of the error there:** the corrected
Yukawa is 4x stronger and repulsive, so the sub-mm exclusion that `track2` already reports as the
*binding* channel (~14 orders tighter than Cassini) gets **stronger**, and the already-falsified H36
point stays falsified a fortiori. No verdict in those files flips in GU's favour. That is why
deferring is safe — not why dropping it would be.

**Also owed, in another channel:** `ar1-dropped-commitments-ledger-2026-08-15.md` row 3 recorded this
defect and asserts, as evidence, that H10 fails to compile and carries an un-actioned
`REMEDIATION OWED` block. Both assertions are now false *because the work is done*. Its owner should
close that row. The compile assertion was already red before this channel opened (the parse repair
predates it); the `REMEDIATION OWED` assertion went red as a direct result of this remediation.

---

## Certificate

```
tests/channel-swings/joe_directed_h105_stelle_ghost_sign.py     48/48   exit 0
  split  [D] 13 derivation   [E] 8 exact PPN   [R] 5 reproductions
         [O] 7 observational [C] 15 controls
  --selftest    14 planted false facts each -> exit 1;  clean run -> exit 0
  exact: sympy Rational in [D]/[E];  floats confined to [O], declared, non-load-bearing

tests/wave22/H10_ppn_weak_field.py                              28/28   exit 0
  (was: exit 1 behind a known-defect guard; before that, SyntaxError)

DERIVED, no literature input
  Phi = -(GM/r)[1 - (4/3)e^{-m2 r}]        Psi = -(GM/r)[1 - (2/3)e^{-m2 r}]
  gamma - 1 = +(2/3)e^{-m2 r}              gamma(m2 r -> 0) = -1,  gamma(m2 r -> oo) = 1
  alpha_Y = -4/3 REPULSIVE
BANNER CONFIRMED  (R3: LPPS Eq 4.7a bracket == derived bracket, exactly)

CASSINI            m2 r > 10.2746   mu_DW floor 1.485e-17 eV   clearance 44.9 decades
VERDICT            GATED-ON-mu_DW, effectively PASSES -- GU CLEARS the bar
DEGENERACY         corrected vs wrong floors differ by 5.6e-6 relative

CONTRARY CONTROLS  (both fire)
  A  internal: mu_DW = 1e-18 eV -> |gamma-1| = 1.003, ~4.4e4x the Cassini bound  FALSIFIED
     same machinery passes mu_DW = 1e-15 eV, so the discrimination is live, not an artifact
  B  external: Brans-Dicke omega=100 -> gamma = 101/102, |gamma-1| = 9.8e-3, 426x  FALSIFIED
     reproduces the repo's own W220 negative control
```

---

## Can the falsifier be trusted now? — blunt

Its arithmetic, yes. Its authority as a falsifier, much less than its framing claims.

The physics is now derived rather than copied, both trace coefficients are forced rather than
asserted, the ghost sign falls out of the operator the repo already computed, the derivation
reproduces the literature it used to merely quote, two contrary controls fire, and the false anchor
that let a `x4` sign error survive four weeks has been replaced by an endpoint that actually
separates the two hypotheses. On those axes it is in better shape than it has ever been, and the
guard came off honestly.

But the thing worth carrying out of this remediation is uncomfortable. This bar's headline number —
the `mu_DW` floor, cleared by 45 decades — is **degenerate between the correct physics and physics
that is wrong by a factor of four and in sign**. It moved by 5.6 parts per million. The file was
dead for six days and no RED list caught it; when it was alive it was computing a confident
non-falsification from an assignment its own header disavowed; and had it kept running with the
wrong constants forever, its published verdict would have been indistinguishable from the right
one. A test with that property is not a falsifier in any load-bearing sense — it is a consistency
check that GU's massive mode is heavy, which the repo already knew from BAR 2 and which the sub-mm
channel constrains ~14 orders more tightly. Ranking it as "a cheap falsifier" overstates it, and
both edited files now say so in their own re-rank blocks.

The one genuinely new observational statement is the sign: GU-given-the-bridge predicts
`gamma > 1`, where the repo has been saying `gamma < 1` since July. That is real content, it is
currently unmeasurable, and it is now recorded correctly in the two files inside this channel's
scope — and still recorded *incorrectly* in six files outside it.
