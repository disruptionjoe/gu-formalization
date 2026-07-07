---
artifact_type: exploration
status: exploration
created: 2026-07-06
title: "Big swing R1 (mechanism identity): is Bender-Mannheim PT quantization the SAME Z2 as Turok-Bateman ghost parity? Both structures built independently on the Pais-Uhlenbeck fourth-order oscillator in a truncated two-mode Fock space (N = 12/16/20 per mode, anchors reproduced). HONEST OUTCOME: CONDITIONALLY_SAME, machine-checked. On the PT-unbroken / diagonalizable domain (w1 != w2) the dynamics-derived BM C operator IS the mode-counting TB ghost parity (-1)^{N_g} as an operator identity: 0 sign mismatches in every window, ||C - P_ghost|| = 4.8e-5 at N=20 (converging ~2 decades per +4 in N), probability assignments identical to 5.8e-9. At the equal-frequency Jordan boundary w1 = w2 the two mechanisms FAIL TOGETHER (min Krein norm ~ eps^2.00, ||C|| ~ eps^-2.00, ghost commutator ~ eps^0.94, perturbation-splitting exponent 0.496 vs diagonalizable control 1.000), and a two-line theorem shows NO positivity-compatible ghost parity of any kind exists there -- only the kinematic Krein metric survives (residual 0.0). Priority: Mannheim's C is the canonical DERIVATION of the object Turok's projector Born rule CONSUMES; neither exists without diagonalizable dynamics, which is exactly what GU lacks. Canon's open condition [P_ghost, S] = 0 is thereby SHARPENED to a property of S alone: Krein-diagonalizability with real spectrum on the matter module."
grade: "exploration / THEOREM (toy scope: Pais-Uhlenbeck arena, truncation N <= 20 with convergence shown; the GU transfer remains CONSISTENT_UNCOMPUTED because GU supplies no S). Verdict vocabulary: CONDITIONALLY_SAME. No forbidden target {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8} assumed, inserted, hardcoded, or divided by; the number 3 does not appear. Random-input and wrong-parity controls show the checks have discriminating power (12/28 mismatches for the wrong parity; 30/40 complex eigenvalues for random pseudo-Hermitian input)."
depends_on:
  - canon/ghost-parity-krein-synthesis.md
  - explorations/generation-sector/mannheim-conformal-gravity-source-action-intake-2026-07-06.md
scripts:
  - tests/big-swing/cg_r1_pu_pt_vs_ghost_parity.py
---

# R1: Bender-Mannheim PT quantization vs Turok-Bateman ghost parity — same Z2?

**The swing.** `canon/ghost-parity-krein-synthesis.md` leaves one named open condition: GU's unbuilt
source action must realize the ghost parity as a symmetry of the dynamics, `[P_ghost, S] = 0`. The
Mannheim intake (2026-07-06) put a second candidate mechanism on the table: the Bender-Mannheim (BM)
PT-symmetric quantization of fourth-order dynamics, the original ghost-resolution for conformal
gravity. Route R1 asks the mechanism-identity question head on, in the one arena where BOTH mechanisms
were originally built: the Pais-Uhlenbeck (PU) oscillator,
`L = (1/2)[xddot^2 - (w1^2 + w2^2) xdot^2 + w1^2 w2^2 x^2]`. Is BM's dynamics-derived `C` operator the
same `Z2` as Turok-Bateman's (TB) kinematically-motivated ghost parity, or materially different?

**Honest outcome: CONDITIONALLY_SAME.** They are the identical operator exactly on the PT-unbroken /
diagonalizable domain, and they fail *together* — at the same rate, for the same structural reason — at
the equal-frequency Jordan boundary, where a two-line theorem excludes every positivity-compatible
ghost parity outright. All numbers below are printed by
`tests/big-swing/cg_r1_pu_pt_vs_ghost_parity.py` (run from repo root, exit 0).

---

## Arena and anchor reproduction

The PT-rotated PU Hamiltonian (Bender-Mannheim PRL 100, 110402 (2008) realization; `gamma = 1`,
`z = -i q1` contour rotation of the Ostrogradsky form):

```
H = i p_z y + p_y^2/2 + (w1^2 + w2^2) y^2/2 + (w1^2 w2^2) z^2/2
```

built as an explicitly NON-Hermitian matrix on a two-mode Hermite/Fock basis (basis scales taken from
the exact ground-state Gaussian `exp(-a z^2/2 - b y^2/2 - c z y)`, `a = (w1+w2) w1 w2`, `b = w1+w2`,
`c = -w1 w2`), generic frequencies `w1 = 1.9`, `w2 = 1.1`, truncations `N = 12, 16, 20` per mode.

**Anchor (required): the known two-mode spectrum in the truncated Fock space.**
`E(n1,n2) = w1(n1+1/2) + w2(n2+1/2)`:

- `E0(num) = 1.5000000000` vs exact `(w1+w2)/2 = 1.5`; the low table `(0,1) -> 2.60000000`,
  `(1,0) -> 3.40000000`, `(0,2) -> 3.70000000`, `(1,1) -> 4.50000000` all reproduce.
- max window error converges `8.36e-03 (N=12) -> 2.43e-04 (N=16) -> 7.29e-06 (N=20)`
  (windows `n1+n2 <= 4/5/6`, i.e. 15/21/28 states); `max |Im E| = 4.4e-14` at N=20.

## (a) The Turok-Bateman side (Krein space, ghost parity, projector Born rule)

- **Kinematic Krein metric.** `eta = P_z` (z-parity), defined with no reference to the frequencies.
  Pseudo-Hermiticity is EXACT even at finite truncation: `||H^dag eta - eta H|| = 0.000e+00`.
- **Ghost parity from the ladder algebra, not from eig(H).** The 4x4 Heisenberg mode problem
  `[H, a] = -w a` has eigenvalues `{+/-1.9, +/-1.1}` (printed); the two annihilators kill the ground
  state to `~6e-11`. Their Krein commutators are the measured c-numbers
  `[a_p, a_p^krein] = +0.397776` and `[a_g, a_g^krein] = -0.271564` (window constancy `~2e-6` at N=20)
  — so the ghost mode is MEASURED, not assumed: it is the `w_g = 1.1` mode in this realization. Then
  `N_g = a_g^krein a_g / lambda_g` and `P_ghost = (-1)^{N_g}`. Cross-anchors: the ladder reconstruction
  `||H - (w_p N_p + w_g N_g + E0)||/||H|| = 5.9e-08`; the operator occupation numbers match the
  energy-derived labels exactly (`max |n_g(operator) - n_g(energy)| = 0.0`); commutation
  `||[P_ghost, H]||/||H|| = 1.3e-06` and `||offdiag(N_g in H-eigenbasis)|| = 4.4e-05` at N=20.
- **Projector Born rule.** For random ghost-parity-even (physical) states evolved by the non-Hermitian
  `U = exp(-iHt)`: min probability `+6.7e-04 >= 0`, `max |sum p - 1| = 5.4e-12` (positivity and
  unitarity on the physical sector), and the literal project-evolve-project-trace form agrees with the
  amplitude form to `6.4e-12`.

## (b) The Bender-Mannheim side (C from the dynamics)

From the spectral decomposition of `H` alone: `C = sum_k sign(nu_k) * (K-orthogonal projector k)`,
where `nu_k = v_k^dag eta v_k` are the measured Krein norms of the eigenvectors. At N=20:
`||C^2 - I|| = 4.4e-07`, `||[C, H]||/||H|| = 3.7e-10`, the `eta*C` (CPT) Gram matrix is Hermitian to
`7.9e-11` and positive definite with smallest eigenvalue `0.000060` (equal to `min |nu_k|`, the
distance to Krein degeneracy — small because PT metric operators are genuinely unbounded in the
excitation level: `||C||_2 = 1.12e+04` on the window in the raw Euclidean norm).

## (c) The identity test — the core result

The two constructions use disjoint raw data: BM uses the *signs of eigenvector Krein norms*; TB uses
*ghost-mode occupation parity from the ladder operator*. Measured:

- **Sign pattern:** `#{k : sign(nu_k) != (-1)^{n_g,k}} = 0` of 15/21/28 at N = 12/16/20. The printed
  per-state table shows it explicitly, e.g. `(1,1): nu = -0.0627, n_g = 1`; `(0,2): nu = +0.117,
  n_g = 2`; `(2,1): nu = -0.0138, n_g = 1`.
- **Operator identity:** `||C - P_ghost|| = 6.7e-02 (N=12) -> 1.6e-03 (N=16) -> 4.8e-05 (N=20)`,
  computed in the bi-orthogonal spectral frame (the similarity making the CPT product Euclidean; in the
  raw Euclidean norm the comparison is dominated by the `~1e4` PT-metric unboundedness, which is
  physics, not error). No intertwiner is needed: `C = P_ghost` literally, `U = I`.
- **Probability assignments:** `max |p_TB - p_BM| = 5.8e-09` over random physical states and times.
- **Controls (the checks can fail):** the wrong parity `(-1)^{N_p}` mismatches `12 of 28` states;
  `||C - eta|| = 11501.77`; a random eta-pseudo-Hermitian matrix is PT-broken (`30/40` complex
  eigenvalues, `min |nu| = 2.8e-17` self-null eigenvectors) so the machinery refuses to produce a `C`
  for generic Krein dynamics. The identity is a property of the PU dynamics, not of the test.

Structurally the identity is forced by the measured ladder algebra: each `a_g^krein` application
multiplies a state's Krein norm by the negative c-number `lambda_g`, so norm sign = `(-1)^{n_g}` —
which is exactly BM's `C` eigenvalue. The computation checks this chain end to end, with the ghost
mode itself measured (`lambda_g = -0.271564 < 0 < lambda_p = +0.397776`).

## (d) The degenerate boundary w1 = w2 — adjudicated, and it cuts the other way

The route brief conjectured an asymmetry: `P_ghost` kinematic and surviving, `C` dynamics-derived and
failing. **Measured: the asymmetry is not there.** The canonical mode-number ghost parity is exactly as
dynamics-dependent as `C`, and they degenerate in lockstep (`eps = w1 - w2`, `w0 = 1.5`, N=20, window
`n1+n2 <= 2`):

- `min |nu| ~ eps^2.00` and `||C|| ~ eps^-2.00` (BM side blows up);
- `|lambda_g| ~ eps^0.94` (TB side: `N_g = a_g^krein a_g / lambda_g` blows up at the same boundary);
- the identity holds with 0 mismatches at every `eps` down to 0.05.

At `eps = 0` exactly:

- the 4x4 mode matrix is DEFECTIVE: eigenvalues `+/-1.5` each with algebraic multiplicity 2, geometric
  multiplicity 1 (singular values `[5.48, 5.23, 0.687, 0]`); the two `-w` eigenvectors overlap to
  `1.000000` — the ladder pair coalesces, so the canonical `N_g` does not exist (classical secular
  growth `t e^{iwt}`, quantized);
- the quantum Hamiltonian has a Jordan block: perturbation-splitting exponent `0.496` (Jordan: 1/2)
  vs `1.000` for the diagonalizable `eps = 0.4` control; the two eigenvectors at `E = 2w` are self-null
  (`|nu| = 1.8e-11`), so `C` is undefined;
- the kinematic Krein metric survives untouched: `||H^dag eta - eta H|| = 0.0e+00` at the boundary;
- **two-line nonexistence theorem** (stated and premise-checked in the script): if `P^2 = I`,
  `[P, H] = 0` and `G := eta P` is positive definite, then `G H = H^dag G`, i.e. `H` is Hermitian
  w.r.t. the positive product `G`, hence diagonalizable with real spectrum. The measured Jordan block
  therefore excludes EVERY positivity-compatible ghost parity at `w1 = w2` — kinematically defined or
  not. At the boundary the mechanisms do not merely lose canonicity; no such `Z2` exists.

## Verdict and priority

**CONDITIONALLY_SAME.** One mechanism in two dresses: identical operator on the PT-unbroken /
diagonalizable domain; joint nonexistence off it. On priority, based on what was measured: Mannheim's
move is prior *as a derivation* — `C` is constructed from the dynamics and, whenever the TB symmetry
condition is satisfiable at all, `C` IS the ghost parity (`||C - P_ghost|| -> 0`). Turok's move is
prior *as an interface* — the projector Born rule is the consumer of the `Z2` and is the only part
stateable without dynamics, but kinematics alone leaves the physical/ghost split non-canonical, and
the boundary shows there are dynamics for which no admissible choice exists at all.

## What this settles for the GU program

- **Canon's open condition is sharpened to a property of S alone.** `[P_ghost, S] = 0` with a
  positivity-compatible `P_ghost` is (in the shared toy, by the theorem above) EQUIVALENT to: `S` is
  Krein-diagonalizable with real spectrum (PT-unbroken, no Jordan blocks) on the matter module. If GU's
  eventual source action has that property on the 192-dim self-dual triplet sector, the ghost parity
  does not need to be posited as an extra datum — it is derived (`P_ghost = C`), and the split of the
  96 hyperbolic (generation, mirror) pairs into 3 physical + 3 ghost is canonical. If instead `S` has
  Jordan blocks pairing a generation with its mirror (the `eps = 0` analogue), NO parity choice
  rescues it.
- **Neither mechanism supplies a dynamics-free shortcut.** The Mannheim intake's implicit hope — that
  the BM PT machinery might resolve GU's ghost problem at the kinematic level — is closed: `C` needs
  the very `S` GU has not built, exactly as TB's parity does. The kinematic Krein structure (which GU
  HAS, exactly: signature `(+96, -96, 0)` on the triplet) survives everywhere, including at the
  boundary, but it never selects the physical half by itself. This is the same honest boundary canon
  already states, now with the second mechanism folded into it.
- **A new failure mode is named for the frontier.** The equal-frequency wall means "quadratic-gravity-
  like source action" is NOT automatically enough: the higher-derivative class contains a measure-zero
  but structurally meaningful Jordan locus where positivity is unrescuable. Any future GU source-action
  candidate must be checked against it (in PU language: no degenerate frequencies in the vertical
  spectrum; in Krein language: no nilpotent pairing of a generation to its mirror).

## What this does NOT settle

- Nothing here computes a chiral physical sector from GU-native data; the 192-dim triplet was not
  touched computationally in this route. The generation-count verdict stays OPEN.
- The PU arena is quantum mechanics, not field theory. BM's and TB's field-theoretic extensions (full
  conformal gravity; TB's quadratic-gravity Born rule) are NOT adjudicated here; known critiques of PT
  quantization at the interacting-QFT level are inherited risks (intake stress-test item 3, still
  unchecked against primary sources).
- BM's own claim (PRD 78, 025022) that the equal-frequency theory remains unitary in a weaker,
  Jordan-block sense is not adjudicated; what is proved is narrower and sharp: no positivity-compatible
  ghost-parity `Z2` exists there.
- Whether the measured ghost-mode assignment (`w_g` = lower frequency in this realization) is
  convention-independent was not explored; the identity test never uses the assignment, only the
  measured sign of the Krein commutator.

## Next steps

1. Transfer the dichotomy to the carrier: for candidate GU source-action fragments on the verified
   `Cl(9,5)` triplet sector, test Krein-diagonalizability (the PT-unbroken condition) instead of
   hunting for a `P_ghost` first — this is now the single gate.
2. Check the Jordan locus against GU structure: is there any GU-forced degeneracy (e.g. from the
   `SU(2)+` triplet's equal Casimir) that would force the equal-frequency analogue? A forced Jordan
   pairing would be a clean BLOCKED result for the whole ghost-parity route.
3. Primary-source pass on the Mannheim intake guards (Bender-Mannheim 2008/2008b, PT-QFT critiques),
   per the intake's promotion rule.

**Governance.** Exploration-grade; no canon promotion proposed from this doc alone. The natural canon
edit it motivates (rewriting the open condition `[P_ghost, S] = 0` as the Krein-diagonalizability
dichotomy) is a separate pass that pauses for Joe.
