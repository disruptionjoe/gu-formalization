---
title: "Building the source action: a Seiberg-Witten-shaped functional on the chimeric bundle (H1 keystone)"
status: active
doc_type: construction
created: 2026-06-28
grade: "construction in progress; each claimed property is verified numerically on the Cl(9,5) substrate or graded open. Optimize for truth: land only what computes."
depends_on:
  - docs/NEXT-FRONTIER-HYPOTHESES.md
  - canon/dark-energy-theta-divergence-free.md
  - canon/shiab-existence-cl95.md
  - docs/WHERE-GU-STANDS-AND-THE-MISSING-OBJECT-2026-06-27.md
  - explorations/dark-energy-cosmology/dark-energy-assumption3-variational-2026-06-23.md
---

# Building the source action (H1 keystone)

The program's universal blocker is one unbuilt object: a **stabilized RS / inhomogeneous-gauge (IG) sector
action** `S_IG^susy`. The persona sprint found its template is named in the transcript's first 90 seconds --
the Seiberg-Witten 1994 nonlinearity (self-dual curvature coupled to a spinor bilinear, plus Dirac). This
doc states the construction problem precisely, on the repo's actual objects, with a numerical verification
plan. The honest target is **an explicit candidate action plus a verified accounting of which of its claimed
properties compute** -- not a declaration that GU works.

## The objects we already have (the substrate is real)

- **Spinor module.** `Cl(9,5) = M(64,H)`, built explicitly (`tests/oq_rk1_cl95_explicit_rep.py:46-72`),
  128-dim complex rep with chiral projectors `E_+ = (I+omega)/2`, `E_- = (I-omega)/2`, each rank 64.
- **The self-dual target `Lambda^2_+ = su(2)_+`.** On `V (x) S` the self-dual `SU(2)_+` generators `J[k]`
  are built at `tests/generation-sector/h1_selfdual_family_kill.py:52-54`. Inside the gamma-trace kernel
  `ker(Gamma)` (dim 1664) the Casimir splits states into `j=0` (640 singlets), `j=1/2` (192 / 64 doublets),
  `j=1` (64 triplets). **The 64-state `j=1` triplet IS the self-dual `Lambda^2_+` sector carrying the 16**
  -- this is the image space of the moment map below.
- **The gamma-trace constraint.** `Pi_RS = I - Gamma^dagger (Gamma Gamma^dagger)^{-1} Gamma`,
  `dim ker(Gamma) = tr(Pi_RS) = 1664` (`gen_sector_bridge.py:39-48`).
- **The Krein form.** `K = eta_V (x) beta_S`, signature `(+96,-96,0)` on the triplet, purely cross-chirality
  (`ghost_parity_krein.py:64-82`, `t1a_kinematic_chirality_kill.py:60-82`).
- **The shiab / middle map.** `Phi: Omega^2(Y)(x)S -> Omega^1(Y)(x)S`,
  `Phi(alpha (x) s) = sum_a e^a (x) c(iota_{e_a} alpha) s` (`canon/shiab-existence-cl95.md:46`):
  Clifford-ODD, `Spin(9,5)`-equivariant, non-injective.
- **The obstruction.** The folded operator `D = [[0, Phi],[d_A, 0]]` is NOT elliptic;
  `||[Pi_RS, M_D]|| = 58.72` (Cl(4,0) toy), nonzero -- the constraint surface and the gauge orbit do not
  form a clean quotient. (The "343.73 = d^2 commutator" identification was KILLED; 343.73 is a
  compression-on-gauge norm. What survives: qualitative non-closure + a provably non-unique selector.)
- **The selector family.** `Hom_{Spin(9,5)}(Lambda^2 V (x) S, V (x) S)` has complex dim 2 per
  chirality-flipping block, real-quaternionic dim `>= 8`; two channels (Rarita-Schwinger `W(omega_1+omega_6)`
  dim 832, and Clifford-trace `S^+` dim 64). GU's canon shiab `= (1,0,1,0)` (pure Clifford-trace) is a
  **definitional postulate**, leaving **3 residual real dimensions** of freedom.
- **Dark-energy variational structure (already derived).**
  `E_A = delta S_GU / delta A = 2 D_A^* F_A + 2 theta + (fermionic bilinear)`
  (`explorations/dark-energy-cosmology/dark-energy-assumption3-variational-2026-06-23.md:137`); on-shell `theta = -D_A^* F_A`.
  Assumption 3 (unproved): `theta` IS the gauge-potential sector of `E_A`.

## The candidate action (strawman to be improved by the construct phase)

On the 4-base `X^4` with the chimeric spinor field `Psi` (the GU vector-spinor, a section of
`Omega^1(S) (+) Omega^0(S)`) and the IG connection `A`:

```
S_SW[A, Psi]  =  \int_{X^4}  [  ||F_A||^2                          (a) gauge kinetic
                              +  < Psi , D_A Psi >_K               (b) Dirac/RS term, Krein-paired
                              +  | F_A^+  -  mu(Psi) |^2           (c) the Seiberg-Witten monopole coupling
                              ]
              +  S_compensator[sigma_c]   +  S_VZ-guardian          (d) BV/BRST + Velo-Zwanziger completion
```

with the **load-bearing new object**, the moment map / spinor bilinear

```
mu : S  ->  Lambda^2_+ = su(2)_+ ,     mu(Psi) = projection of (Psi (x) Psi^*_K) onto the j=1 triplet,
```

`F_A^+` the self-dual part of the curvature valued in `su(2)_+`, `D_A` the folded shiab operator, and
`<,>_K` the Krein pairing. The monopole coupling (c) is the Seiberg-Witten nonlinearity; its Euler-Lagrange
equations are the **GU monopole equations**

```
F_A^+ = mu(Psi)        (self-dual curvature = spinor bilinear)
D_A Psi = 0            (Dirac/RS equation on the chimeric bundle).
```

## The three discharges to verify (and the consistency gates)

**(A) Dark energy / Assumption 3.** Vary `S_SW` in `A`. The monopole term (c) contributes a fermionic
bilinear to `E_A` exactly of the form already derived. Claim to test: the SW coupling makes the
`theta`-sector of `E_A` dynamical and sourced by `mu(Psi)`, so `theta = -D_A^* F_A` is realized as a field
equation, and Noether's second theorem then gives `D_A^* theta = 0` **without** hand-imposed projectors.
This is the discharge of Assumption 3.

**(B) Middle-map closure / selection.** On the SW shell `F_A^+ = mu(Psi)`, evaluate the obstruction
`[Pi_RS, M_D]` and the selector freedom. Claim to test: the nonlinearity restricts the admissible shiab to
the subset preserving the on-shell constraint surface, collapsing the 3 residual real dimensions (ideally to
GU's `(1,0,1,0)`), and reducing the qualitative non-closure. (Even partial collapse is a real result.)

**(C) 2+1 matter content.** The equivariant shiab family is chirality-flipping only, so both Majorana blocks
of the folded operator vanish -- the seesaw heavy block must come from outside. Claim to test: the SW
coupling `mu(Psi)` supplies exactly that chirality-preserving (Majorana) block, turning the Dirac-doubled
spectrum into a genuine seesaw `[[0, m],[m^dagger, M]]` and producing the "2 + 1 with an imposter" structure
-- making the asserted `+8` Rarita-Schwinger term in `ind_H = 8*A-hat + 8` a computed object rather than a
heuristic.

**Consistency gates (each can falsify the construction):**
- **BV master equation** `(S,S) = 0` (the compensator `sigma_c` must be the non-equivariant ghost symbol
  that closes `(I-Pi_RS)(M_D+sigma_c)Pi_RS`).
- **Velo-Zwanziger.** The super-IG completion must keep the spin-3/2 sector causal/unitary while
  constraints propagate (necessary-not-sufficient; attach a unitarity ledger).
- **Krein.** The `(+96,-96)` cross-chirality structure must be respected; `mu` must be Krein-compatible.
- **The sign/magnitude adversary.** The "obvious" characteristic-class route gives `-5376`, not `24`
  (`WHERE-GU-STANDS...:70-73`). The construction must explain or repair this, or the index claim is dead on
  arrival.

## Verification plan (numerical on the substrate, then graded)

1. **Foundational object first.** Build `mu : S -> Lambda^2_+` explicitly on `Cl(9,5)` (the `j=1` triplet
   projection of the spinor bilinear) and check it exists and is `su(2)_+`-equivariant. If no equivariant
   `S -> Lambda^2_+` bilinear exists in this signature, the SW route is obstructed at step 1 -- a decisive
   early result either way. (Reuse `h1_selfdual_family_kill.py:52-77`, `ghost_parity_krein.py:64-82`.)
2. **Discharge A** -- recompute `E_A` symbolically/numerically with the monopole term; confirm the
   `theta = -D_A^* F_A` identification and the Noether closure (reuse the derivation at
   `dark-energy-assumption3-variational-2026-06-23.md`).
3. **Discharge B** -- evaluate `[Pi_RS, M_D]` on the SW shell and the selector dimension collapse
   (reuse `gen_sector_bridge.py`, `shiab_codiff_intertwiner_dim.py`, `step4_mkt_vs_dirac_square.py`).
4. **Discharge C** -- check the Majorana block / seesaw structure under the SW coupling
   (reuse `shiab_selector_seesaw_selfadjoint.py`).
5. **Consistency** -- `(S,S)=0`, VZ ledger, Krein compatibility, and the `-5376` sign/magnitude audit.

Every numerical check lands a test under `tests/source-action/`. Each claimed property gets a grade:
`computed-confirmed | computed-refuted | open`. We land only what survives, and we report the refutations as
loudly as the confirmations.

## Honest expectation

The most likely outcome is partial: `mu` exists (the `j=1` triplet is right there), the dark-energy
variational discharge (A) is the strongest candidate to land, and (B)/(C) are harder and may only partially
collapse. A clean failure of any gate is a real result -- it converts "GU's source action is unbuilt" into
"GU's source action, built in its own named template, does/does not do X," which is exactly the truth-seeking
deliverable. Building it could also reveal the count is observer-relative (the 3 residual dims) rather than a
clean integer, dissolving the headline rather than confirming 3. That is an acceptable, even valuable,
outcome.
