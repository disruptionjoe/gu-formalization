# /gu-compute

Run a bounded GU computation. Usage: `/gu-compute <problem-label>`

Problem labels: `discrete-series`, `vz-schur`, `codazzi-sp64`, `cpa1-tobs`, or a short description of a new problem.

---

## Step 1 — Identify the problem

Use `$ARGUMENTS` as the problem label. If not provided, ask which of the four open computations to run:

1. **discrete-series** — Does Dirac on GL(4,ℝ)/O(3,1) with fiber spinor S(6,4) = ℂ^{16} have dim_ℍ L²-kernel = 24? Harish-Chandra/Parthasarathy discrete series of GL(4,ℝ). Gates generation count to RESOLVED.
2. **vz-schur** — Compute the Schur complement symbol D_{RS}^{eff} = D_{RS,RS} - D_{RS,1/2}(D_{1/2,1/2})^{-1}D_{1/2,RS} using Spin(9,5) Clifford representation theory. If its principal symbol equals g(ξ,ξ)·Id_{RS}, VZ is evaded at 14D.
3. **codazzi-sp64** — Derive the Codazzi equation for the Sp(64) bundle over the embedded section s(X⁴) ⊂ Y¹⁴. Normal bundle N_s ≅ Sym²T*X⁴. Prerequisite: compute II_s explicitly using moving frames before attempting the full Codazzi derivation.
4. **cpa1-tobs** — Compute the explicit coefficient in Λ ~ ε²/t_obs² from GU Tikhonov regularization and compare to λ_max = 1/t_obs from Time as Finality FR2. Both programs point at t_obs as the natural scale; a coefficient match is the first quantitative cross-program contact.

---

## Step 2 — Pre-loaded mathematical context (read before computing)

This is the established result set. Do not re-derive these; build on them.

**Geometry:**
- Y¹⁴ = Met(X⁴): bundle of Lorentzian metrics on 4-manifold X⁴
- Fiber: GL(4,ℝ)/O(3,1) ≃ RP³ (via polar decomposition + Cartan retract)
- Total signature (9,5): fiber Frobenius (7,3) → trace-reversal → (6,4) fiber; (6,4) + (3,1) base = (9,5)
- w₂(Y¹⁴) = 0 for any orientable X⁴ — RESOLVED. Y¹⁴ is spin without condition on X⁴.

**Algebra:**
- Cl(9,5) ≅ M(64,ℍ) — quaternionic type, (p−q) mod 8 = 4
- Spinor module S = ℍ^{64}, dim_ℝ = 256; chiral halves S± = ℍ^{32}
- Gauge group G = Sp(64) = U(64,ℍ), dim_ℝ sp(64) = 8256
- Sp(64) is anomaly-free: pseudoreal fundamental (J² = −1) → n_L − n_R = 0; π_{15}(Sp) = ℤ → no global Z₂ anomaly
- Nguyen §2 (anomaly pincer) and §3.1 (complexification gap) are both FULLY CLOSED

**Shiab and gauge structure:**
- Shiab Φ: Ω²(Y¹⁴)⊗S → Ω¹(Y¹⁴)⊗S via Φ(α⊗s) = Σₐ eᵃ⊗c(ι_{eₐ}α)·s
- ℍ-linear, Spin(9,5)-equivariant, no complexification required
- τ⁺ homomorphism: G → IG = G ⋉ Ω¹(ad P); g ↦ (g, g⁻¹d_Ag) — purely group-theoretic for any Lie group G
- IG double coset equivariance holds for G = Sp(64)

**Dark energy:**
- Distortion θ = A − Γ (gauge connection minus Levi-Civita)
- D_A*θ = 0 follows from Noether's second theorem for the Yang-Mills action — CLOSED

**Generation count (CONDITIONALLY 3):**
- Fiber spinor S(6,4) = ℂ^{16}; Cl(6,4) ≅ M(16,ℂ)
- Pati-Salam decomp: S(6,4) → (4,2,1) ⊕ (4̄,1,2) under SU(4)×SU(2)_L×SU(2)_R
- SM branching: Q_L + L_L + ū_R + d̄_R + ē_R + ν_R = 16 Weyl fermions = 1 SM generation — CONFIRMED
- D_GU commutes with right-ℍ multiplication → index counts ℍ-lines; 8 ℍ-lines per SM generation
- 2 spin-1/2 generations (from ind_ℍ counting) + 1 RS generation = 3 total — CONDITIONAL on discrete-series computation

**4D reduction (partial):**
- Section s: X⁴ → Y¹⁴ selects Lorentzian metric g_s on X⁴
- s*(θ) = II_s (second fundamental form of embedding) — DERIVED at reconstruction grade
- Spinor branching S(9,5) = S(3,1) ⊗ S(6,4) with correct SM content — VERIFIED
- Gauss equation: s*(R_{ℊ}) = R_{g_s} + II_s·II_s + ... (schematic) — Codazzi correction outstanding
- Willmore energy E[s] = ∫|II_s|² selects critical sections variationally
- Tikhonov regularization scale: Λ ~ ε²/t_obs² (from section selection on compactified X⁴)

**Velo-Zwanziger (OPEN):**
- VZ theorem fires for standalone RS fields minimally coupled to non-trivial gauge groups
- 4D: RS(3,1)⊗S(6,4) carries SM charges → H3 satisfied → VZ fires at 4D
- 14D evasion candidate: RS sector is the Leibniz cross-term in D_GU; D_{RS,1/2} nonzero by construction
- Priority computation: Schur complement symbol D_{RS}^{eff} = D_{RS,RS} - D_{RS,1/2}(D_{1/2,1/2})^{-1}D_{1/2,RS}

**Hidden curvature (CONDITIONALLY RESOLVED):**
- 6-piece SO(1,3) decomposition: W (Weyl) + S₀ (traceless Ricci) + R (scalar) + H^{(1)} + H^{(2)} + H^{(3)}
- H^{(i)} sourced by torsion pieces T^{(1,2,3)} via DT = R∧e; invisible to torsion-free geometry

**Cross-program contact:**
- TaF FR2: λ_max = 1/t_obs (maximum observer rate, absorbed by L2+L4)
- GU Tikhonov: Λ ~ ε²/t_obs² (section selection regularization)
- Both depend on t_obs; coefficient comparison (CPA-1) is the named test

---

## Step 3 — Run the computation

Perform the computation at the best achievable grade:
- **verified**: proof complete, all steps checked
- **reconstruction**: argument is correct, minor details unverified
- **exploration**: approach is right, key steps are sketched

State clearly which grade the output achieves and what the remaining gap is. Include explicit failure conditions — what would make the result false.

---

## Step 4 — Write the exploration file

File path: `explorations/{short-label}-YYYY-MM-DD.md` where YYYY-MM-DD is today's date.

Use this frontmatter:
```yaml
---
title: "<Descriptive title>"
date: YYYY-MM-DD
problem_label: "<matches the label above>"
status: exploration|reconstruction|verified|open
verdict: RESOLVED|CONDITIONALLY_RESOLVED|OPEN|EVADED|GENUINE_OBSTRUCTION
---
```

Then write:
1. **Problem statement** — what is being computed and why it matters
2. **Established context** — which prior results this builds on (cite exploration files)
3. **Computation** — the actual work, step by step
4. **Result** — verdict with explicit failure conditions
5. **Open questions** — what remains; what would change the verdict

---

## Step 5 — Tracking cascade

After writing the exploration file, update three tracking files:

**NEXT-STEPS.md:** Find the relevant row. Update the status tag (e.g. `~~VZ1~~` for resolved, or add a new note under the open item). Keep it a single-row table update — do not restructure the table.

**DERIVATION-PROGRESS.md:** Append a brief log entry at the end:
```
### <Problem label> (YYYY-MM-DD)
Verdict: <RESOLVED|OPEN|...>
<2-3 sentences: what was computed, what the result is, what remains if anything>
File: `explorations/{filename}`
```

**canon/no-go-class-relative-map.md:** Update only if the computation affects a no-go entry (VZ-related, anomaly-related, or a new obstruction/evasion found).

---

## Step 6 — Commit

Stage the exploration file and all updated tracking files together. Commit message format:
```
<Short description of computation and verdict> (YYYY-MM-DD)

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
```

Do not push unless explicitly asked.
