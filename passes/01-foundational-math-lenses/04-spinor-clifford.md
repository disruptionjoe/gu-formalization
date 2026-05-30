# Persona Pass 04 — Spinor / Clifford Algebra Specialist

## (a) Where my discipline gives clearest leverage

Joe's Question 3 (can fermions arise from pure geometry?) is where Clifford/spin machinery is decisive. Spin geometry is the canonical answer to "how do fermions show up from a metric." Questions 1 and 4 get partial leverage through dimension-counting and signature constraints. Question 2 (gauge group emergence) is mostly outside my reach — that's a holonomy / G-structure question, not a Clifford one. I'll be sharpest on 3, secondarily on 1.

## (b) Strongest first-principles construction

Given a (pseudo-)Riemannian manifold (M^n, g), the Clifford bundle Cℓ(TM, g) is canonically built from the metric. A spin structure is a double cover of the orthonormal frame bundle reducing SO(p,q) → Spin(p,q); it exists iff w_2(TM) = 0. Spinor bundles are then associated bundles S = P_Spin ×_ρ Δ, where Δ is an irrep of Cℓ(p,q). This is the only known way to get fermion fields from geometry alone without postulating them.

For n = 14, complex Clifford: Cℓ(14, ℂ) ≅ M_{128}(ℂ), so the Dirac spinor is 128-complex-dimensional. Even dim → chirality operator γ_* exists, splitting Δ = Δ_+ ⊕ Δ_−, each of complex dim 64. For signature (13,1), real structure analysis (mod-8 Atiyah-Bott-Shapiro table, s − t = 12 ≡ 4 mod 8) gives a quaternionic real structure on Δ — Majorana spinors in the strict sense do **not** exist in (13,1), though pseudo-Majorana / symplectic-Majorana variants do. For (7,7) signature, Majorana-Weyl spinors of real dim 64 exist. The 64-dimensional Weyl spinor is the natural "fermion content" candidate.

## (c) What fails or is forced

- **Chirality is forced but wrong-sized.** A single 14d Weyl spinor carries 64 complex (or 64 real Majorana-Weyl, signature-dependent) components. The Standard Model needs 16 complex Weyl fermions per generation (15 + ν_R). 64 = 4 × 16 invites a "four generations" reading, not three. [speculation] One generation could be projected out by a discrete symmetry, but this is a postulate, not geometry.
- **Mass terms require breaking.** Dirac mass needs a pairing Δ_+ ⊗ Δ_− → trivial; Majorana mass needs Δ_+ ⊗ Δ_+ → trivial. Both exist for appropriate signatures, but in 14d the pairings are large and require a 14d → 4d reduction mechanism (KK-style) that is not supplied by spin geometry alone.
- **Spin structure existence is non-trivial.** w_2(M^14) = 0 is a real topological constraint on the 14-manifold; without specifying M, this is unverifiable.
- **Reduction to 4d Dirac.** Standard KK reduction on a 10-manifold fiber gives a tower of 4d fermions; one must hand-pick a zero-mode sector. The geometry alone does not single out the SM fermion content.

## (d) Named obstructions

1. **Atiyah-Singer / mod-8 Majorana obstruction** — signature (13,1) admits only quaternionic, not Majorana, real structure.
2. **w_2 obstruction** — spin structure existence on the 14-manifold.
3. **Generation-counting mismatch** — 64 vs 3 × 16 = 48 (or 3 × 15 = 45).
4. **Witten-style anomaly** — Spin(n) for n ≥ 7 carries discrete anomalies (e.g., π_4(Spin) torsion) that must cancel in any chiral construction.
5. **No-go from spin-statistics in higher dim** — consistent quantization of half-integer-spin fields in 14d requires Lorentzian signature with one time; (7,7) or (14,0) cannot host a unitary QFT in the standard sense.

## (e) Verdict

Spinor geometry **permits** a 14d fermion bundle and forces chirality, but the natural Weyl-component count (64) does not match Standard Model fermion content (48), Majorana structure fails in (13,1), and the path from a 14d Dirac operator to three 4d generations requires postulates that spin geometry does not supply.
