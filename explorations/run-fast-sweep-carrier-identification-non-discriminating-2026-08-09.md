---
title: "Fast sweep results: the Casimir = -11.25 identification of the generation carrier is NON-DISCRIMINATING (a random 192-dim subspace passes the same test); the 640/832/192 split is pure so(4) branching with zero Dirac input; 40 SM-NEUTRAL states exist in ker(Gamma); and the alpha_Y error is located"
artifact_type: run_receipt
created: 2026-08-09
status: CARRIER_IDENTIFICATION_CRITERION_HAS_NO_SELECTIVE_POWER__SPLIT_IS_BRANCHING_ARITHMETIC__ASD_MIRROR_INDISTINGUISHABLE_BECAUSE_CRITERION_IS_VACUOUS__40_SM_NEUTRAL_STATES_FOUND__GHOST_PARITY_CARRIER_FRAME_CHARGE_ZERO__ALPHA_Y_ERROR_LOCATED
grade: "EXECUTED. 6 agents, 0 errors, ~668k subagent tokens. Two verifies SCOPED/upheld, ONE verify
  upheld=FALSE (the first outright refutation of a cluster headline this session, and the refuting verifier
  rebuilt the substrate from scratch importing nothing). All arithmetic independently reproduced everywhere;
  the failures were interpretive."
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Fast sweep: results

## 1. THE HEADLINE — the carrier identification cannot discriminate

**The `Casimir = -11.25` / "pure `Spin(10)` `16+16bar`" identification of the 192 carries no selective
information about the carrier.**

- The internal `so(10)` spinor Casimir is **exactly a scalar on the whole 128**: deviation-from-scalar
  `0.00e+00`, value `-11.25 = -n(n-1)/8 = -90/8`.
- The full generator's Casimir is `-11.25` with spread **`0.00e+00` on the entire 512-dim
  (base-4 vector) (x) 128 block**.
- **A RANDOM 192-dim subspace of that block passes the identical test** (spread `1.05e-13`).

So `h1_selfdual_family_kill.py`'s load-bearing assertion
`abs(val.mean()-ref16) < 1e-6 and ptp(val) < 1e-6` is passed by **any** 192-dim subspace of
base (x) spinor. The carrier merely has **zero internal-vector support** (`5.22e-30`). For contrast the
640s have internal-vector weight `0.929` and a mixed spectrum `{-21.25: 576, -11.25: 64}`.

**This does NOT say the 192 is not a `Spin(10)` spinor.** It is one. It says **so is everything else in that
block**, so the test does not single the carrier out. The carrier is **asserted by a criterion with no
discriminating power**, not identified.

**ALREADY IN REPO, unconnected.** `tests/oq_rk1_j_restriction_probe.py:316` already asserts
`"so(10) Casimir on S = 45/4 (spinor is 16-type throughout)"`. The repo has known the enabling fact all
along and never connected it to the carrier identification.

## 2. The 640/832/192 split is branching arithmetic, not Dirac content

Predicted with **zero computation** from `so(4)` branching: `14 = 4+10 -> su(2)_+ : 2x(1/2) + 10x(0)`;
`128 = 4_so(4) (x) 32_int -> 32x(1/2) + 64x(0)`; tensor -> `j=1: 64 copies (192)`, `j=1/2: 448`,
`j=0: 704`; remove one equivariant copy of the 128 -> **64 triplets (192) + 416 doublets (832) + 640
singlets**. Matches the computed split **to the digit**.

Scramble evidence: the 192 **survives complete destruction of all ten internal gammas** (internal Clifford
anticommutator residual `16.35`; `ker` still 1664; split still 640/832/192; `su(2)_+` closure still exact at
`7.43e-16`). So it carries **zero internal/generation Dirac content**. It does *not* survive destruction of
the four base gammas -- but that also destroys `su(2)_+` itself (closure residual `0.73`), so `j=1` stops
being a defined label. That dependence is the question's precondition, not evidence of content.

**Honest limit:** this is NOT the NET-SD-grade null. NET-SD was bit-identical even with all gammas zeroed;
the 192 is not. NET-SD remains the stronger null.

## 3. The ASD mirror is indistinguishable -- because the criterion is vacuous

Joint `(Cas_+, Cas_-)` diagonalization (`||[Cas_+,Cas_-]|| = 1.11e-13`):
`(0,3) -> 640`, `(3,0) -> 640`, `(3,8) -> 192`, `(8,3) -> 192`.

The `(1/2,1)` mirror matches the `(1,1/2)` carrier on **every criterion the repo has ever used**: Casimir
`{-11.25: 192}` single eigenvalue no spread; internal-vector weight `8.49e-30` vs `1.28e-24`; internal
chirality `+96/-96` identical.

**NOT licensed: "there are two generation carriers."** Both pass for the *same forced reason* -- neither has
internal-vector support, so both inherit the block-wide `-11.25` automatically. **The correct reading is that
the criterion fails to discriminate.** This answers the "reconcile the two 192s" action: answered, and
negatively.

## 4. `Spin(10)` content of ker(Gamma) -- and a REFUTED headline

`ker(Gamma)` is exactly two-valued under the `Spin(10)` Casimir:
`(C + 11.25)(C + 21.25) = 0`, residual `6.78e-13` (independent rebuild). **512 states of 16-type, 1152 of
144-type, and not a single `Spin(10)` singlet.**

**The cluster's binary conclusion was REFUTED by its own verifier** (`upheld = false`), who rebuilt the
substrate from scratch importing nothing. The agent claimed "SM-CHARGED... that KILLS the SM-singlet /
dark-sector branch outright." **`Spin(10)`-singlet and SM-singlet are different predicates.** Building the
actual SM subalgebra `su(3)_c + su(2)_L + u(1)_Y` inside `so(10)` (CAR residual `0.0`, 12 generators lifted
with reconstruction residual `< 1e-9`) and counting the joint kernel:

> **SM-NEUTRAL states in `ker(Gamma)` = 40** (smallest nonzero eigenvalue of `sum A^dag A` = `1.0000`, so
> the count is clean). By Casimir: **32 at `-11.25` (16-type), 8 at `-21.25` (144-type).**

**So the dark-sector branch of the 1472 programme is NOT killed. There are 40 SM-neutral states.** New,
computed, and the opposite of what the executing agent reported.

## 5. Section-independence: SUPPORTED

12 substrate builds -- ambient `(14,0)`, `(9,5)`, `(7,7)`, `(13,1)`; alternate timelike index sets; seven
base 4-plane placements; all five base signature allocations. The `Spin(10)` Casimir spectrum and the
`su(2)_+` split are unchanged. **Generation content is a schema property, as claimed.** (Caveat reproduced
by the verifier: the naive real SD spectrum on Lorentzian bases gives a spurious triple; the convention-free
statement is the coarser `384/1280`.)

## 6. Open threads closed

- **H-C1 REFUTED.** The carrier-projected ghost-parity frame charge is **zero**: full-space `K` gives
  `tot = SD = ASD = NET-SD = 0.000000` exactly, structurally. Positive control reproduced
  (`su(2)_+ NET-SD = 33.941125497 = 3*sqrt(128)`). **That thread is closed.**
- **H-C2 SUPPORTED.** `w != 0` is robust. Probe re-run `EXIT=0`, `ALL CHECKS PASSED`,
  `chi(DeWitt loop) = -1`, `chi(doubled) = +1`, `chi(2pi deck element -I) = +1`, K1 control holds.
- **H-C3 SUPPORTED, genuinely new.** The `alpha_Y` error is **located**:
  `tests/wave22/H10_ppn_weak_field.py`, comment line **L82** and two constants at **L84**. Owed correction.

## What this changes

1. **The strongest item in the 25-lens council -- "a generation is an m-value, ACTUAL MATH very high" --
   rests on a non-discriminating criterion.** The carrier may still be the right object; it has not been
   *shown* to be, and the test used to show it cannot distinguish it from a random subspace of the block.
2. **The 1472 dark-sector branch revives** with a concrete number: 40 SM-neutral states.
3. **A new required action:** find a criterion for the carrier that HAS discriminating power. Until then,
   "the 192 is the generation carrier" is an assertion, not a result.
4. Ghost-parity frame charge: closed. `w != 0`: robust. `alpha_Y`: located, fix owed.
