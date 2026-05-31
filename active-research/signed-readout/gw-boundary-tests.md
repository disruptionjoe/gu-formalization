---
title: "03 — Bridge-to-GW Tests for JD-CALM and AC-CALM"
status: active_research
doc_type: synthesis
updated_at: "2026-05-31"
---

# 03 — Bridge-to-GW Tests for JD-CALM and AC-CALM

**artifact:** internal origin artifact
**Status.** Local-only draft. Generated 2026-05-31.
**Predecessor inputs.** `01-jordan-calm-formalization.md`; `02-option-b-metric-cointegration.md`; internal origin artifact `falsification-result.md` (the original GW-bridge failure); 21-persona §1 Lattice QFT theorist + §3 Anomaly theorist + §4 Numerical lattice physicist (GW-side authority).

This document tests whether each framework bridges to Ginsparg-Wilson observables. The two tests are independent. The combined verdict drives `05-verdict.md`.

---

## 1. Test 1 — JD-CALM bridge to GW axial charge

**Setup.** Apply JD-CALM (`01` §2) to the GW axial-charge query `Q_A(I) = Σ_x q_A(x; I)` where `q_A(x; I) = ψ̄_x γ_5 (1 - a R D)_{xx} ψ_x` depends on the gauge field input `I` in an exponentially-decaying neighborhood of `x`.

**Test 1.A — Can `Q_A` be Jordan-decomposed in a way that maps to a distributed protocol?**

Two candidate decompositions (per `01` §3):

- **Local pointwise Jordan:** `q_A(x) = q⁺(x) - q⁻(x)` with `q⁺(x) = max(q_A(x), 0)`, `q⁻(x) = max(-q_A(x), 0)`. The sign classification at each site is a local function of the gauge field in the exponentially-decaying neighborhood. **Maps cleanly to a distributed protocol**: each replica accumulates two non-negative aggregates `Q⁺ = Σ_x q⁺(x)`, `Q⁻ = Σ_x q⁻(x)` and reports `Q⁺ - Q⁻` at readout.
- **Global chirality:** `Q_A = n₊ - n₋` from Atiyah-Singer. The sign of each zero mode's contribution is determined by its *global* chirality eigenvalue, which is *not* a local function. **Does NOT map to a coordination-free distributed protocol**: identifying which mode a given site `x` belongs to requires global wavefunction information.

**Bridge-test outcome on Test 1.A:** **PARTIAL.** The local pointwise Jordan decomposition gives a clean coordination-free protocol *for the signed-real-valued per-site density and its aggregate*. But this aggregate `(Σ q⁺, Σ q⁻)` is *not* the topological-index pair `(n₊, n₋)` — it over-counts (per `01` §3, paragraph 6). The protocol returns the correct *signed sum* `Σ q⁺ - Σ q⁻ = n₊ - n₋ = Q_A` by Atiyah-Singer, but the *individual* components `Σ q⁺` and `Σ q⁻` are larger than `n₊` and `n₋` respectively and have no physical interpretation as separate observables.

This is structurally OK for the bridge: JD-CALM correctly says "you can propagate signed contributions as two non-negative aggregates, and reconstruct the signed total at readout." The bridge claim shifts from "CALM-monotonic = GW-realizable" to **"JD-CALM signed aggregate = GW signed-real-readout"** — which is a tighter, more honest claim that preserves the structural content while dropping the integer-index claim.

**Test 1.B — Does the instanton/anti-instanton sign cancellation (internal origin artifact P3) break JD-CALM?**

Per `01` §5: **NO.** Adding an anti-instanton at distance increases the input set, increases `Q⁻` by ~1 unit (the anti-instanton's contribution to negative-chirality density grows), and `Q⁺` essentially unchanged. The signed difference `Q⁺ - Q⁻` decreases. This is *not* a JD-CALM violation: both `Q⁺` and `Q⁻` grow monotonically; the signed-difference readout is allowed to move in either direction.

**This is the load-bearing structural win of JD-CALM over ε-local CALM.** The internal origin artifact P3 instanton/anti-instanton kill is *exactly* the failure mode JD-CALM is designed to handle. Under JD-CALM, the kill becomes a *feature*, not a bug.

**Test 1.C — Does the truncation-rounding non-linearity (V2's counterexample) break JD-CALM?**

Per `01` §4 case (a): **YES**, if the readout is the integer index produced by rounding. The rounding step `round_ε : ℝ → ℤ` introduces a non-linearity at the readout that JD-CALM does not address — the per-component aggregates `Q⁺_ε`, `Q⁻_ε` are each CALM-monotone, but the rounded difference `round_ε(Q⁺_ε - Q⁻_ε)` is not. JD-CALM does not save the integer-index bridge.

Per `01` §4 case (b): **NO**, if the readout is the signed-real value with explicit ε-bound (i.e., we collapse JD-CALM's readout into AC-CALM's readout). Under this reading, the bridge survives at the approximate level.

**Test 1 net verdict:**

- **Signed-real-valued bridge:** JD-CALM **RECOVERS**. The per-site signed-real density `q_A(x)` and the aggregate `Q_A = Σ q_A(x)` are JD-CALM. The instanton/anti-instanton signed cancellation is correctly classified as a Jordan-aggregate feature. The bridge claim is "GW signed-real axial-charge aggregate is JD-CALM," which is a clean positive result.
- **Integer-index bridge:** JD-CALM **does NOT recover**. The integer-index readout requires either an exact (`r → ∞`) limit (outside CALM) or a rounding step (breaks JD-CALM at readout). The integer-index bridge claim does not survive.

---

## 2. Test 2 — AC-CALM bridge to GW axial charge

**Setup.** Apply AC-CALM (`02` §2) to `Q_A(I)`. The GW kernel's exponential decay (Hernández-Jansen-Lüscher 1999) gives the influence-weight bound that AC-CALM requires. The truncation radius `r` becomes a system-level parameter; the metric-cointegration bound `ε(r) = (C' a / γ) exp(-γ r / a)` gives the explicit consistency tolerance.

**Test 2.A — Does AC-CALM provide a coordination-free distributed protocol for `Q_A`?**

For every fixed `r`, the truncated `Q_A,r` is a bounded-radius CALM query (real-valued aggregate, additive composition, bounded radius). The per-replica computation is coordination-free in the standard CALM sense. **YES — coordination-free protocol exists.**

**Test 2.B — Does AC-CALM bridge to the GW axial charge as a *signed-real-valued aggregate with bounded error*?**

The truncation error bound `|Q_A(x) - Q_A,r(x)| ≤ ε(r)` follows directly from the GW kernel's exponential decay. Two replicas computing `Q_A,r` with the same `r` and same input agree exactly; two replicas computing the full `Q_A` agree up to `2 ε(r)`. **YES — bridge holds at signed-real-valued bounded-error level.**

**Test 2.C — Does AC-CALM bridge to the integer-index readout?**

For sufficiently large `r`, the error `ε(r)` is below `1/2`, so the rounded value `round(Q_A,r)` equals the true integer index with high confidence — *for sufficiently large `r`*. But "sufficiently large `r`" is *configuration-dependent*: a gauge configuration with multiple instantons whose tails interfere may require larger `r` than a single-instanton configuration. AC-CALM does not provide a configuration-independent finite `r` that guarantees integer-index correctness.

Practically: for any *fixed* gauge configuration, there exists a finite `r` that gives integer-index correctness; but the required `r` is unbounded across the class of all gauge configurations. **Bridge to integer-index holds *per-configuration* but not *uniformly*.**

**Test 2.D — Does the instanton/anti-instanton sign cancellation break AC-CALM?**

AC-CALM does not classify the signed sum as "CALM-monotonic in the input-set-growth sense" — it treats `Q_A,r` as a *real-valued query with bounded error*, dodging the signed-aggregate semilattice question. The instanton/anti-instanton signed cancellation produces a real-valued sum that decreases under input growth, which is *not* a violation of AC-CALM as stated (because AC-CALM does not assert input-set monotonicity of the signed value). **Bridge survives — AC-CALM is silent on signed-aggregate monotonicity.**

This is a *weaker* repair than JD-CALM's structural classification: AC-CALM allows the signed-cancellation to occur without flagging it, whereas JD-CALM positively classifies it as a Jordan-aggregate feature. Both bridge survive, but JD-CALM gives a stronger structural justification.

**Test 2 net verdict:**

- **Signed-real-valued bridge with bounded error:** AC-CALM **RECOVERS**. The bridge claim is "GW axial-charge real-valued aggregate at fixed truncation radius `r` is bounded-radius CALM, with cross-replica consistency `2 ε(r)`."
- **Integer-index bridge uniformly across configurations:** AC-CALM **does NOT recover**. Per-configuration correctness holds for large `r`; uniform correctness does not.

---

## 3. Joint comparison and reading on the bridge question

The bridge from CALM to GW has *two distinct readout targets* that ε-local CALM (internal origin artifact) confused into one:

**Readout target 1 — Signed-real-valued aggregate of axial-charge density** (`Q_A = Σ_x q_A(x)` as a real number; the per-site density `q_A(x)` is signed real; the global integral happens to equal an integer by the index theorem but the readout itself is a real number).

- internal origin artifact ε-local CALM: FAILS (signed cancellation + truncation rounding)
- JD-CALM: RECOVERS (signed cancellation classified as Jordan-feature; rounding avoided by signed-real readout)
- AC-CALM: RECOVERS (with explicit ε-bound)
- **Joint:** the bridge **survives at the signed-real readout level** under either framework.

**Readout target 2 — Integer topological invariant** (`Q_A = n₊ - n₋` ∈ ℤ; the readout is a discrete integer index produced by an exact, unbounded computation).

- internal origin artifact ε-local CALM: FAILS (rounding step breaks monotonicity)
- JD-CALM: does NOT recover (rounding step is orthogonal to Jordan split)
- AC-CALM: does NOT recover uniformly (requires `r → ∞`)
- **Joint:** the bridge **does NOT survive at the integer-index readout level** under any of the three frameworks tested.

---

## 4. Connection to the 21-persona meta-assessment's "layer split" insight

The 21-persona assessment §S.2 issue B named "wrong target observable; layer conflation" as a structural issue the validators missed. Specifically: the bridge work *conflated*

- **propagation-layer** (per-site contribution accumulates monotonically) — survives
- **decision-layer** (signed readout flips sign under input growth) — fails
- **anomaly-class** (the topological invariant the system carries) — relocates
- **observable-level** (the specific query `Q_A`) — fails

The JD-CALM and AC-CALM exploration in internal origin artifact *operationalizes* this layer split:

- JD-CALM's `Q⁺, Q⁻` per-component aggregates are the **propagation-layer** objects (each grows monotonically).
- The `Q⁺ - Q⁻` readout is the **decision-layer** object (can decrease).
- AC-CALM's `Q_A,r ± ε(r)` is a **bounded-error decision-layer** object that explicitly carries its scale.
- The integer index `n₊ - n₋` returned by Atiyah-Singer is the **anomaly-class / topological-invariant** object, which lives one layer above what JD-CALM or AC-CALM directly capture.

This is consistent with the 21-persona meta-verdict's recommendation: the surviving bridge is at the *propagation layer*, the failing bridge is at the *integer-topological-invariant decision layer*, and the structural insight is the layer split itself.

`[speculation, this draft's read]` — the internal origin artifact exploration *confirms* the 21-persona meta-verdict's "Option II-Retreat" framing rather than overturning it. The signed-CALM repair gives a tighter, more publishable version of the propagation-layer survival claim (via JD-CALM or AC-CALM as the technical machinery), but does not rescue the integer-index decision-layer claim.

---

## 5. Bridge-test summary table

| Bridge claim | ε-local CALM (internal origin artifact) | JD-CALM (`01`) | AC-CALM (`02`) |
|---|---|---|---|
| Signed-real per-site density `q_A(x)` is locally computable | YES | YES | YES |
| Signed-real aggregate `Q_A = Σ q_A(x)` is propagation-layer CALM | NO (signed semilattice broken) | YES (Jordan-split) | YES (per-r CALM) |
| Signed-real aggregate is decision-layer monotone under input growth | NO | NO (correctly classified as Jordan-feature) | Silent (not asserted) |
| Integer index `n₊ - n₋` is recoverable as CALM readout | NO | NO | Per-config YES, uniform NO |
| Instanton/anti-instanton input growth handled cleanly | NO | YES | YES (silent) |
| Truncation-rounding non-linearity (V2's counterexample) handled | NO | NO at integer readout, YES at signed-real readout | YES (no rounding) |
| Bridge to GW signed-real readout survives | NO | YES | YES |
| Bridge to GW integer-index readout survives | NO | NO | NO uniformly |

**Net combined verdict:** The bridge from a signed-CALM framework to GW survives **at the signed-real-valued readout level** under both JD-CALM and AC-CALM; the bridge **does NOT survive at the integer-index readout level** under any framework tested. JD-CALM gives the strongest *structural classification* of the signed-cancellation phenomenon (positively classifying it as Jordan-aggregate behavior). AC-CALM gives the strongest *practical bound* on cross-replica consistency (explicit `ε(r)`). The strongest combined framework is JD-CALM + AC-CALM applied jointly: per-sign and per-radius parameterized, with bounded-error readout.

---

End of `03-bridge-to-gw-tests.md`.
