# /gu-status

Report the current state of the GU formalization project. Read NEXT-STEPS.md and DERIVATION-PROGRESS.md, then emit a short oriented summary in this format:

---

## GU Formalization Status

**Nguyen Objections**
- §3.1 complexification gap: CLOSED (Cl(9,5) quaternionic → ℍ-linear shiab, no complexification needed)
- §2 anomaly pincer: CLOSED (Sp(64) pseudoreal → anomaly-free; IG dimension matching resolved via group-theoretic τ⁺)

**Resolved**
List items from NEXT-STEPS.md marked ~~strikethrough~~ or RESOLVED. One line each: `- N1 Signature: (9,5) confirmed`.

**Conditionally Resolved** (have remaining analytic conditions)
- N5 Generation count: CONDITIONALLY 3 — representation theory confirmed; discrete-series computation for GL(4,ℝ)/O(3,1) remains
- Anything else from NEXT-STEPS.md with CONDITIONALLY_RESOLVED status

**Open** (no resolution yet)
List items that are open with their specific blocking computation. Be precise:
- VZ1 Velo-Zwanziger: OPEN — Schur complement symbol D_{RS}^{eff} is the decisive computation
- Codazzi/Sp(64): OPEN — needed to derive full Einstein equations from 4D reduction
- CPA-1 cross-program coefficient: OPEN — compare Λ ~ ε²/t_obs² to TaF FR2 λ_max = 1/t_obs
- Any others from NEXT-STEPS.md

**Paper version**
State which version of `papers/what-geometric-unity-needs-to-do-next-*.md` is current (check for the highest v-number or status: draft).

**Recommended next computation**
Name one specific bounded computation to run next, with a one-sentence reason. Default order: discrete-series > vz-schur > codazzi-sp64 > cpa1-tobs.

---

Keep the whole output under 40 lines. No headers beyond the ones above. No tables. Plain bullet points only.
