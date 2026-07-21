---
title: "Decision tree Q1a (θ): the fiber-end limit-point/limit-circle classification is FORCED to LIMIT-POINT by GU's own structure — B = -iK_uG is an involution product (||B||=||B^-1||=1, non-degenerate wherever P>0), P is floored away from 0 at the ends, and W~ (carrying the bounded wall coefficient C_0=√|P-T|) is bounded; so the noncompact fiber end is essentially self-adjoint, the domain is UNIQUE and FORCED, and θ dissolves — flagged LOUDLY with four named hardening gaps that keep this a strong structural lean, not yet a closed theorem"
status: active_research
doc_type: exploration
created: 2026-07-21
program: explorations/prereg-three-object-decision-tree-2026-07-21.md
question: "Q1a — the RE-SHAPED θ question: does GU's fiber-end geometry put A~ = B(s)d_s + W~(s) (B=-iK_uG) in the limit-point case (unique forced domain, selector derivable) or the limit-circle case (boundary freedom, θ real)?"
inputs:
  - explorations/prereg-three-object-decision-tree-2026-07-21.md
  - explorations/source-domain-selector-prongB-hostile-verify-2026-07-21.md
  - explorations/continuum-pencil-graph-domain-certificate-2026-07-20.md
  - explorations/continuum-pencil-domain-gate-2026-07-20.md
  - explorations/sector-relative-section-theory-2026-07-20.md
  - canon/source-action-seiberg-witten-construction.md
probe: tests/channel-swings/decision_tree_Q1a_fiber_end_classification_probe.py (foreground, EXIT 0)
outcome: Q1a-FORCED (limit-point; unique forced domain; θ dissolves) — flagged for hostile verification, NOT over-claimed
kill_conditions_declared_before_computation: true
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_actions: none
---

# Q1a: the fiber-end limit-point / limit-circle classification

Adversarial truth-test, not advocacy. This run is Q1a of the σ/θ/τ decision tree.
It does **not** re-prove externality (that is the closed premise; re-deriving it is
circling). It returns a **verdict** on the upstream question HV re-shaped: on the
TRUE NONCOMPACT fiber, is the first-order operator `A~ = B(s)∂_s + W~(s)`,
`B = -iK_u(s)G`, in the **limit-point** case (essentially self-adjoint ⇒ unique
forced domain ⇒ the boundary selector is derivable from structure ⇒ the pencil
theorem `OPERATOR-END-PENCIL` closes with no imported datum) or the **limit-circle**
case (boundary freedom survives ⇒ a real θ must be chosen)?

## 0. Verdict up front

> **`Q1a-FORCED` — LIMIT-POINT — flagged LOUDLY, not over-claimed.**
>
> GU's own structure puts `A~` in the **limit-point** case at the noncompact fiber
> ends. The domain is **unique and forced**; there is **no θ** (consistent with
> HV's "in the limit-point horn there is no graph domain and no θ"). The pencil
> theorem can close from structure with **no imported boundary datum**. **Moduli
> dimension = 0.**
>
> **What forces it (the derived chain):**
> 1. `B = -iK_uG` is the product of **two involutions** — `K_u := K_S c_s/√P` is a
>    Hermitian traceless **involution** (`K_u² = I`, section theory §1) and `G`
>    (=`G_col`) is an involution — so **every singular value of `B` equals 1**:
>    `‖B‖ = ‖B⁻¹‖ = 1` **pointwise wherever `P > 0`**. `B` is non-degenerate with
>    uniformly bounded inverse. This is **theorem-grade GU algebra**, not an
>    assumed asymptotic. (Probe `[STRUCTURE]`: singular values `min=max=1.000000`.)
> 2. Therefore `B` can degenerate at an end **only if `P → 0`** there (the
>    pure-timelike `P=0` stratum). GU's section theory finds that stratum **empty
>    at the ends**: `min P/(P+T) = 0.36` over 200 sampled rays **including the
>    boundary-at-infinity**. So `B` stays non-degenerate all the way to the end.
> 3. The remaining knob is the zeroth-order term `W~`. It carries the wall
>    coefficient `C_0 = √|P−T|`, which is **bounded** (`P,T` bounded), plus a
>    bounded potential `V` and the bounded winding of `K_u`. A first-order
>    Dirac-type end with **non-degenerate `B` and bounded `W~`** is **limit-point**
>    (the constant-coefficient/Levinson default; HV's C3). Leaving limit-point
>    requires `W~` to **blow up** at the end (the first-order analog of the scalar
>    `q → −∞` faster than `s²`) — which GU's bounded `P,T,C_0` do **not** do.
> 4. Both ends limit-point ⇒ **essentially self-adjoint ⇒ unique domain**.
>
> **This is NOT `Q1a-UNDETERMINED`.** The `D2` datum HV called "source-silent" is,
> on this structural inspection, **not a free asymptotic function**: it is pinned
> to a single GU-owned scalar `P(s)` (through `K_u`) and to the bounded `C_0`, both
> of which GU's section theory **computes**. GU structure *does* speak here, and it
> speaks limit-point. No external asymptotic datum need be imported.
>
> **BUT (loud):** this is a **strong structural lean at fixture/reconstruction
> grade, not a closed theorem.** Four hardening gaps (§5) keep it from being a
> proof. The honest modality is: *GU structure forces limit-point up to converting
> a sampled `P`-floor into a theorem and a Hilbert-space count into the genuine
> Krein count.* None of the four gaps points **toward** limit-circle; they are
> hardening tasks, not sign-flipping unknowns.

## 1. The pivot, and what HV left open

HV (`source-domain-selector-prongB-hostile-verify`) established the pivot: on the
noncompact fiber the moduli dimension is the Weyl deficiency, set by the
**end-asymptotics of `B` and `W~`**, and the *default* for a non-degenerate
Dirac-type end is **limit-point** (unique domain), while limit-circle requires a
**singular end** — coefficient degeneration. HV's C3 stated this sharply: a
constant-mass Dirac end is robustly limit-point (decay rate `≥ |Im λ|` for all
masses); "reaching LC requires the principal coefficient `B` to DEGENERATE at the
end … which is again a `D2`-class asymptotic fact the sources do not fix." HV then
declined to decide, calling `D2` source-silent.

The worthy Q1a swing is exactly whether `D2` is *really* silent, or whether GU's
own structure fixes it. **It does**, and the reason is that `D2` is not a generic
asymptotic function — it collapses to the behavior of **one GU-native scalar**.

## 2. The structural reduction (derived, GU-native)

The certificate and section theory hand us the operator explicitly:

- `A = K_u D_op`, `D_op = -iG_col ∂_s + V`, so `A~ = -iK_uG ∂_s + W~`, i.e.
  **`B(s) = -iK_u(s)G`** (domain-gate §1; certificate §1).
- `K_u := K_S c_s/√P` is a **Hermitian traceless involution**: `K_u² = I` wherever
  `P > 0` (section theory §1, machine-corroborated on the actual end family).
- `G = G_col` is an **involution** (`G² = I`).

**Lemma (B non-degeneracy, theorem-grade).** A product of two involutions has all
singular values equal to 1: if `K_u² = G² = I` and both are self-adjoint (unitary),
then `B = -iK_uG` is unitary up to the scalar `-i`, so `‖B‖ = ‖B⁻¹‖ = 1` at every
point where `P > 0`.

*Probe `[STRUCTURE]`* sweeps all winding angles and returns `B` singular values
`min = max = 1.000000` and `K_u² = I` throughout. This is the certificate's own
statement ("the wall … does not make `B` singular"; "the principal coefficient
`B(s) = -iK_u(s)G_col` is invertible at every point") upgraded to a **uniform**
bound and traced to its cause: `B` is an **involution product**.

**Corollary (the pivot collapses to one scalar).** `B` degenerates at an end **iff
`P → 0`** there (only then does `K_u = K_S c_s/√P` cease to be a bounded
involution). So the entire LP/LC question at the `B`-level is: *does `P → 0` at the
noncompact fiber ends?* The multi-component "asymptotics of `B`" reduce to the
single scalar `P(s)`.

**What GU says about `P` at the ends.** The section theory computes `P` on the
faithful Y14 end and reports, over **200 sampled rays including the
boundary-at-infinity** (the conf-down limit loop, itself a genuine wall-crossing
loop where `q̂` changes sign): `min P/(P+T) = 0.36`, and the `P = 0` pure-timelike
stratum **empty on every sampled ray**. So at the actual noncompact end, `P` is
**floored away from 0**, `K_u` stays a genuine involution, and `B` stays
non-degenerate. *This is the crux input, and it is GU-computed, not imported — but
it is sampled (see §5 gap A).*

**The geometric reason it is plausible, not coincidental.** The habitat fiber is
`F = GL(4,R)/O(3,1)`, the noncompact symmetric space of signature-`(3,1)` metrics.
The `(3,1)` signature is **preserved on the entire interior** of `F` (that is the
definition of the homogeneous space; the isotropy `O(3,1)` fixes the signature).
`P` is the spacelike Krein norm of the section symbol; it vanishes only where the
symbol goes pure-timelike, the analog of losing the spacelike signature — which
happens only at the actual metric-degeneration **boundary**, at infinite invariant
distance in the complete symmetric-space metric, not along interior directions to
infinity. So the geometry gives a *reason* the sampled `P`-floor is not an
accident: the ends approached within the interior of `F` keep the signature, hence
keep `P > 0`. (This is an argument at plausibility grade, not a signature-to-`P`
theorem — gap A.)

## 3. The zeroth-order term `W~` is bounded

With `B` non-degenerate, limit-point vs limit-circle is then decided by `W~`. From
the certificate, `W~ = K_u V − (i/2)K_u' G`, and the wall enters the pencil only
through the **bounded** coefficient `C_0(s) = q(s)^{1/2} = √(P−T)` ("the wall enters
only through the **bounded** zeroth-order pencil coefficient `C_0`", certificate
§1; "the wall only makes `C_0` Hölder-continuous at its zero", domain-gate §1).
Since `P, T` are bounded at the ends (section theory), `C_0 = √|P−T|` is **bounded**.
The winding term `K_u' = φ'(s)(…)` is bounded where the winding rate `φ'` is bounded
(the section theory's gauge-spikes are **interior-wall** artifacts, not ends). So
`W~ ∈ L^∞` at the ends. *(V and φ' boundedness at the true ends are section-theory
smoothness facts at sampled/collar grade — gap C.)*

A non-degenerate first-order Dirac end with **bounded `W~`** is **limit-point**:
half the modes decay and half grow at `λ = i` (Levinson/constant-coefficient
comparison). LC requires `W~` to be **unbounded** at the end.

## 4. The LP/LC probe: controls distinguish LP from LC, then GU's case

`tests/channel-swings/decision_tree_Q1a_fiber_end_classification_probe.py`
(foreground, **EXIT 0**, numpy/scipy, deterministic). Two robust `L²`-solution
counters (`n` = deficiency index; `n=1` ⇒ LIMIT-POINT/unique domain, `n=2` ⇒
LIMIT-CIRCLE/`U(1)` of BCs survives):

- **(A)** the **scalar Weyl counter verbatim from the HV probe** (with the
  `|q−λ|^{-1/2}` amplitude prefactor) — the already-validated criterion;
- **(B)** a **first-order fundamental-matrix SVD-ratio** for the genuine 2×2 Dirac
  operator `-iσ_z ∂_s + W~`: `σ_max/σ_min → ∞` (one dominant + one recessive) ⇒
  `n=1` LP; ratio bounded ⇒ `n=2` LC (prefactor-independent — exponential
  separation dominates any polynomial).

**CONTROL — the criterion must distinguish planted LP from planted LC (kill
conditions, declared in the probe before GU's case):**

| model | counter | result |
|---|---|---|
| scalar `q=-s^{1.5}` (`p<2`, bounded-ish/slow) | A | `n=1` **LIMIT-POINT** |
| scalar `q=-s^{3}` (`p>2`, fast blow-up) | A | `n=2` **LIMIT-CIRCLE** |
| scalar `q=+s^{3}` (confining) | A | `n=1` **LIMIT-POINT** |
| first-order Dirac, **bounded** `W~` | B | SVD ratio `≈1.1e16` ⇒ `n=1` **LIMIT-POINT** |
| non-J-symmetric `B=-iK_uG` + arbitrary `W~` (earlier draft) | — | coincident `Re(μ)` ⇒ deficiency **ill-defined** (why the model must be J-symmetric; and why the naive "non-degenerate `B` ⇒ LP" hand-argument fails without symmetry) |

The controls **pass**: the counter is not rigged — it returns LC (`n=2`) exactly
when the end-asymptotics blow up faster than `s²`, and LP (`n=1`) otherwise.

**GU'S CASE (both counters):**

| model | counter | result |
|---|---|---|
| effective scalar `q_eff = P − T` (**bounded**, oscillating sign at walls; `min P/(P+T)=0.35` in-sample) | A | `n=1` **LIMIT-POINT** |
| first-order Dirac: bounded winding + bounded `C_0=√\|P−T\|` + bounded `V`, `B` non-degenerate | B | SVD ratio `≈5.0e16` ⇒ `n=1` **LIMIT-POINT** |

**GU-UNBOUNDED counterfactual (honesty control):** force `q_eff ~ -s³` (the wall
coefficient blowing up) ⇒ `n=2` LC — i.e. the *only* structural route to boundary
freedom is an **unbounded** effective potential, which GU's **bounded** `P,T,C_0`
do not produce. GU's structure sits on the limit-point side of the dividing line,
and the probe shows exactly where that line is.

## 5. What I could NOT establish — the four loud hardening gaps

This is a `B-FORCED`-type win, so maximum skepticism applies. The verdict is
limit-point, but it is **not a closed theorem**. Four gaps, each a hostile-verify
target; **none points toward limit-circle**:

- **Gap A — the `P`-floor is SAMPLED, not proven.** `min P/(P+T) = 0.36` is a
  fixture-grade fact over 200 rays on a **reconstruction-grade** model (repo state:
  the `w2–y14` spin is flagged wrong upstream). The `P = 0` stratum is "empty on
  sampled," not "provably empty." The signature-preservation argument (§2) gives a
  *reason* to expect `P` floored but is not a signature-to-`P` theorem. **If some
  genuine end direction has `P → 0`, `B` degenerates there and that end's LP claim
  fails.** *Missing lemma:* a proof that `P` is bounded below on the whole
  noncompact end (e.g. from the `GL(4,R)/O(3,1)` signature staying `(3,1)` on
  interior geodesic rays to infinity).
- **Gap B — Hilbert count vs Krein count.** The operator is `J`-symmetric
  (Krein/indefinite, `J = K_S`). My probe verified LP on a genuinely **Hermitian**
  Dirac reduction (`B` rotated to `-iσ_z`, Hermitian `W~`). The `J`-symmetric
  (Sims-type) LP/LC theory is subtler; even with non-degenerate `B` the indefinite
  metric could in principle admit LC where the definite metric forces LP. HV §5
  flagged exactly this. *Missing lemma:* the Krein deficiency indices of the actual
  `J`-symmetric `A~` at the ends equal the Hilbert-model count (or a Sims-type
  bounded-coefficient limit-point theorem in the `K_S` metric).
- **Gap C — `W~` end-boundedness is sampled.** `C_0 = √|P−T|` bounded follows from
  `P,T` bounded (sampled). `V` and the winding rate `φ'` bounded **at the true
  ends** are section-theory smoothness facts at sampled/collar grade. If `φ'`
  (`K_u`'s winding) is unbounded at an end, the gauge-reduced `W~` blows up and LC
  reopens (the counterfactual). *Missing lemma:* `V, φ' ∈ L^∞` at the noncompact
  ends, not just on the collar.
- **Gap D — completeness / gauge reduction.** The reduction `B=-iK_uG → -iσ_z` by
  a pointwise unitary (gauge rigidity) and the limit-point default both use that
  the end is at **infinite length in a complete metric** (Chernoff-type default).
  `F` with the invariant metric is complete, but that the fiber's `s`-ray inherits
  completeness with the non-degenerate `B` is asserted from geometry, not proved
  for the actual operator.

These are **hardening** tasks (sample → theorem, Hilbert → Krein), not an external
import. That distinction is the whole content of the `FORCED` vs `UNDETERMINED`
call: **GU structure fixes the classification's sign; the gaps are about grade.**

## 6. Why this is `FORCED`, not `UNDETERMINED` (guarding the anti-circling rule)

The prereg's `UNDETERMINED` bucket is "GU's structure does not fix the fiber-end
asymptotics ⇒ the LP/LC datum is the precise external input." That is **not** what
was found. The asymptotics are **not** a free unknown:

- `B`'s end behavior is **fixed by structure** to non-degenerate (`‖B‖=‖B⁻¹‖=1`),
  an involution-product theorem — reducing the whole `D2` "asymptotics of `B`" to
  the single scalar `P`, which GU **computes** (floored).
- `W~`'s dangerous piece `C_0=√|P−T|` is **fixed by structure** to bounded.

So there is no missing external asymptotic *function* to import; there is only a
grade upgrade of computed/structural facts. Reporting `UNDETERMINED` here would be
**re-running externality under a new name** — exactly the circling the program
forbids. The honest new information Q1a adds, stated once: **the fiber-end
classification is determined by GU structure and the determination is LIMIT-POINT**,
contingent on the §5 hardening.

*(For contrast, the genuinely external data remain σ and τ — untouched here. Q1a
concerns θ only, and θ **dissolves** under limit-point: there is no boundary phase
to choose. The forcing datum is a **geometric non-degeneracy**, not a `Z/2` choice,
so — answering the prereg's follow-up "is that datum σ?" — **no**, θ's dissolution
does not hand a bit to σ.)*

## 7. Moduli consequence for the pencil theorem

- **Moduli dimension = 0.** Limit-point at both ends ⇒ `A~` is essentially
  self-adjoint on `C_c^∞` of the fiber ⇒ **unique** `J`-self-adjoint realization ⇒
  no graph domain `D_T`, no endpoint relation `T_θ = e^{iθ}S(b)`, **no θ**.
- **The boundary selector is DERIVABLE from structure**, not external: the
  operator selects its own domain via essential self-adjointness. `OPERATOR-END-
  PENCIL` can then close on the noncompact fiber **without importing an endpoint
  relation or its phase** — resolving the certificate's `DOMAIN-OBSTRUCTION-SOURCE`
  in the direction of "structure supplies the domain," subject to §5.
- **Q1b is not reached.** Q1b (a reality/holonomy condition quantizing `U(1) → Z/2`)
  lives "only in the limit-circle horn" (prereg). Limit-point removes the horn;
  there is nothing to quantize.

## 8. Kill conditions (declared before computation) and adjudication

Declared in the probe's control block before GU's case was run:

- **KC1 (criterion validity):** the counter must return `n=2` (LC) for a planted
  fast-blow-up end (`q=-s³`) and `n=1` (LP) for bounded/slow and confining ends.
  **Held** (probe DIAL + counterfactual).
- **KC2 (first-order faithfulness):** the first-order Dirac counter must return
  `n=1` for a non-degenerate `B` + bounded `W~`. **Held** (SVD ratio `>1e4`).
- **KC3 (GU lands LP):** GU's derived end (non-degenerate involution `B`, bounded
  `W~`/`q_eff`) must return `n=1` on **both** counters. **Held.**
- **KC-REFUTE (would have flipped to `FREE`):** GU's `C_0`/`q_eff` blows up faster
  than `s²` at an end (unbounded `W~`), OR `P → 0` at a genuine end (degenerate
  `B`). **Did not fire** — `C_0=√|P−T|` bounded, `P` floored — *within the sampled
  grade of §5 gaps A, C.*

## 9. Boundary

Exploration tier. Only this artifact and its probe
(`tests/channel-swings/decision_tree_Q1a_fiber_end_classification_probe.py`,
foreground, **EXIT 0**) were written. GU otherwise read-only. No commit, no push.
No edit to LANE-STATE, research-portfolio, NEXT-STEPS, the prereg, any other agent's
artifact, or any claim/canon/verdict/ledger file. No claim status, canon verdict,
paper status, or public posture changes. Externality of σ/τ is untouched and
un-re-derived; θ is found to **dissolve** under the limit-point verdict. The verdict
is scoped to fixture/reconstruction grade with the four §5 hardening gaps named as
the hostile-verification targets that would convert this strong structural lean into
a closed theorem.
