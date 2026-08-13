---
title: "Run receipt: the two-Z/2 monodromy question, 5-seat pre-flight -> execution -> 5-seat hostile review. The monodromy Z/2 is TIME REFLECTION not the spinor double cover (Layer-0 homonym, computed); the frame-triviality wall IS evadable but the escape is continuously tunable and therefore NOT an index"
artifact_type: run_receipt
created: 2026-08-09
status: MONODROMY_Z2_IDENTIFIED_AS_pi0_O31_TIME_REFLECTION__SPINOR_DOUBLE_COVER_PROVABLY_INERT__FRAME_TRIVIALITY_WALL_EVADABLE_VIA_CLASS_B_BUT_NET_SD_IS_CONTINUOUSLY_TUNABLE_HENCE_NOT_AN_INDEX__NO_COUNT_MOVED
grade: "EXECUTED. Two existing repository probes re-run on the verified Cl(9,5) = M(64,H) substrate, both
  exit-clean. Run A reproduces its own published verdict. Run B REPRODUCES AN EXISTING CANON CORRECTION and
  is NOT a new discovery -- see Provenance. The one contribution that appears not to be already recorded is
  the QUANTIZATION objection in hostile seat 2. No claim status, canon verdict or posture moves."
method: "5 specialist seats inline (pre-flight) -> execution -> the same 5 seats inline (hostile review),
  per house convention that perspectives run inline. Directed by Joe, direct chat 2026-08-09."
canon_verdict_change: none
follows:
  - explorations/monodromy-two-z2s-same-or-different-2026-08-09.md
  - explorations/dc-h1-orbit-signs-monodromy-check-2026-08-04.md
  - canon/frame-triviality-structural-or-evadable-GU-independent-RESULTS.md
  - canon/single-decider-integer-index-RESULTS.md
probes:
  - tests/dc-h1/dc_h1_orbit_sign_monodromy_probe.py
  - tests/gu-independent/frame_active_antilinear_chiralizer_hunt.py
---

# Run receipt: the two-`Z/2` question

## Environment (reproducibility finding, worth fixing)

`scipy` is a **declared, pinned root dependency** (`requirements.txt`, `requirements.lock` -> `1.18.0`) and
was **absent** from the host interpreter. `pip install` into the Homebrew Python is blocked by PEP 668, and
`--break-system-packages` was **not** used. The investigation was executed in an isolated venv
(`numpy 2.5.1`, `scipy 1.18.0`); the system interpreter was left untouched.

**Consequence for the repo:** `tests/gu-independent/frame_active_antilinear_chiralizer_hunt.py` silently
runs its first section and then dies at part (B) on a bare `ModuleNotFoundError` — i.e. **a partial run
looks like a null result for the escape hunt.** Anyone running it without `scipy` gets baseline
frame-triviality and no escape, which is the opposite of the true verdict. `REPRODUCE.md` should state the
venv requirement, or the script should fail fast on import.

---

## Phase 1 — pre-flight, 5 seats

1. **Clifford algebraist.** `J_quat = id_14 (x) U` is spinor-only *by construction*, so its frame charge is
   `0` **definitionally, not empirically**. A null on the baseline proves nothing; only a dressed operator
   tests anything.
2. **Index theorist.** Demand discreteness up front. A count is an index and an index is quantized. **If the
   frame charge varies continuously with any parameter it is not an index**, regardless of being nonzero.
   Filed as the primary kill.
3. **Layer-0 semanticist.** Four objects wear the letter `C`. And the governing hypothesis note already
   types the coincidence `Z/2 = Z/2` as **the weakest evidence class — number-matching, which may NOT be
   used as an argument.** The investigation must test a mechanism.
4. **Verification engineer.** Reproduce published anchors before trusting any new number. Do not
   `--break-system-packages`.
5. **Adversary.** A null here is uninformative (seat 1). The investigation is only worth doing if it contains a
   steelmanned escape attempt; if every candidate leaks out of the carrier, nothing was tested.

---

## Phase 2 — execution

### Run A — `dc_h1_orbit_sign_monodromy_probe.py` — ALL CHECKS PASSED

> Parallel transport of the coflip `C_perp = K J_obs` around the DeWitt metric-fibre loop — **exactly the
> generator of `pi_1(F) = Z/2`** — returns `C_perp -> -C_perp`; the doubled loop returns `+C_perp`. So the
> sign is a `Z/2` **holonomy class `w != 0` in `H^1(F; Z/2)`**, not a stored value.

and, decisively for the question this investigation was commissioned to answer:

> `chi` is quadratic in the Clifford lift, so it descends to `SO` and is **blind to the double cover**: the
> deck element `-I` of `Spin -> SO` has `chi = +1`. `pi_1(SO(3)) = Z/2` **does not move a single orbit
> sign.** The `Z/2` that DOES act is `pi_0` of the Lorentz stabilizer `O(3,1)` — the `O(1)` **time
> reflection**. It is a **REFLECTION `Z/2`, not a double-cover `Z/2`**. The two share a group order and
> nothing else: **Layer-0 HOMONYM.**

### Run B — `frame_active_antilinear_chiralizer_hunt.py` — ESCAPE FOUND

Anchors reproduced exactly: `bare = 58.7215`, `C2 = 155.3625`, carrier dim `192`, carrier `su(2)_+`
reference NET-SD = `33.941`.

| candidate | `C^2` | net-chiral | carrier leak | **NET-SD** |
|---|---|---|---|---|
| **A:** `J_quat . G` (GU baseline) | −1 | **yes** | `2.56e-13` | **+0.000** |
| **B:** `exp(0.3 . su2_+) . C_GU` | −1 | **yes** | `2.56e-13` | **+5.988** |
| **B:** `exp(0.7 . su2_+) . C_GU` | −1 | **yes** | `2.56e-13` | **+14.789** |
| **B:** `exp(1.2 . su2_+) . C_GU` | −1 | **yes** | `2.56e-13` | **+13.307** |
| C: gamma-soldering | +1 | no | `5.77e-01` | +0.000 |
| D: frame-reflection CPT | +1 | no | `5.77e-01` | +0.000 |
| E: `exp(t Lsd) (x) Uw` | −1 | **no** | `0.28 / 0.49` | +5.424 / +9.520 |
| F: `(exp(t Lsd) (x) U) . G` | −1 | **no** | `0.22 / 0.45` | +3.048 / +7.784 |

**Class B evades the wall.** Antilinear, `C^2 = -1` (CII), chirality-**preserving** (net-chiral capable),
carrier leakage `2.56e-13` — bit-identical to baseline — and NET-SD frame charge nonzero. E and F acquire
frame charge but **lose net-chirality and leak out of the carrier** (`0.22`–`0.49`), so they are not
candidates.

---

## Phase 3 — hostile review, same 5 seats

1. **Clifford algebraist — CONFIRMS.** Class B is clean; leakage matches baseline to 13 digits, so the
   dressing genuinely stays on the carrier. Not an artifact.
2. **Index theorist — KILLS THE PHYSICAL READING.** `+5.988 -> +14.789 -> +13.307` for
   `theta = 0.3, 0.7, 1.2` is **continuous and non-monotone**. A continuously tunable, non-quantized
   quantity **is not an index** and cannot carry a count. You can dial it to any value — which is what an
   imported datum looks like, not a derived one. **The escape is structural, not physical.** The pre-flight
   kill fired.
3. **Layer-0 semanticist — SUPPLIES THE HEADLINE.** Run A settles it: the spinor double cover
   (`pi_1(SO) = Z/2`, the Mobius / `4pi` sign) is **provably inert** — `chi` is quadratic, the deck element
   has `chi = +1`, nothing moves. The acting `Z/2` is **time reflection**. Two `Z/2`'s, same order, no
   relation.
4. **Verification engineer — FLAGS PROVENANCE.** Run B **reproduces an existing canon correction** rather
   than discovering anything: the frame-triviality metatheorem holds on the full 1792-dim space and
   **fails on the 192-dim carrier**, already recorded as correcting canon. This receipt is a
   re-execution.
5. **Adversary — NAMES WHAT WAS NOT TESTED.** The hunt checks structure only: antilinearity, `C^2`,
   chirality, leakage, frame charge. It does **not** test that any Class-B operator commutes with a
   dynamics. **`[P_ghost, S] = 0` is untested**, and it is the condition that actually matters. A structural
   candidate with no dynamics is a construction, not a selector.

---

## What this investigation establishes

1. **The Mobius / double-cover reading of the monodromy is DEAD, by computation.** The `H^1(F;Z/2)` class is
   generated by `pi_0(O(3,1))` time reflection; `pi_1(SO)` is inert. This closes the identification posed in
   `explorations/monodromy-two-z2s-same-or-different-2026-08-09.md` (amended accordingly).
2. **The frame-triviality wall is evadable**, and the "`C = J_quat . G` is the unique chiral projector"
   assertion is falsified in the relevant sense — Class B keeps every property that made the baseline
   net-chiral-capable while acquiring nonzero NET-SD.
3. **The evasion cannot count.** NET-SD is continuously tunable, so the escape yields a dial, not a number.
   This **strengthens** the external-datum conclusion rather than weakening it.
4. **A reproducibility defect**: the escape hunt fails partway without `scipy` and a partial run reads as a
   null.

## What it does NOT establish

- Nothing about the generation count. The standing verdict is *located, not forced*, and it tilts toward
  **one**.
- Not whether the ghost parity is the monodromy class. Run A identifies the *mechanism* of the monodromy;
  it does not identify the ghost parity. But the honest prior has **shifted**: since frame-active
  net-chiral operators exist, frame-triviality no longer automatically separates the two `Z/2`'s.
- `[P_ghost, S] = 0` remains untested for every Class-B candidate (hostile seat 5).

All numbers are `(9,5)` arithmetic on a live but undetermined horn (`SIGNATURE-AMBIENT` is OPEN), and
`J_quat` does not exist on `(7,7)`.
