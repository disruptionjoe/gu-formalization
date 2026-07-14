---
artifact_type: exploration
status: exploration (W134; 5-persona inline team; one deterministic test; closes W124 Stage C)
created: 2026-07-14
hypothesis: H59
branch: "Path-2 wave-5 (Team H70 / W134): W124 Stage C -- attach the spin-2 tensor numerators to the two-loop scalar-core cut results; upgrade the ARGUED positivity/parity claim to COMPUTED"
title: "W134 VERDICT: PARITY-SURVIVES-COMPUTED. On the cut every massive spin-2 line carries the on-shell projector P2(k), which equals the uniformly (+1)-weighted polarization sum exactly; the cut numerator is a positive semidefinite form for EVERY vertex (min eigenvalue 0 within 1e-15, min nonzero eigenvalue exactly 1) pointwise across the Stage-A phase space at s = 5, 6, 8, 12; the longitudinal 1/M^2 and 1/M^4 growth is positive growth (max eigenvalue 1.5 -> 17, minimum pinned at zero); the internal Krein twist is EXCLUDED (Schur: trivial commutant; the eta-twisted sum is not a covariant tensor), so the Krein sign rides the overall residue and the (-1)^{n_ghost} parity map lifts intact from the scalar core to spin-2"
grade: "COMPUTED (machine-checked exact identities: transversality, tracelessness, positive orthonormality, P2 = sum eps eps to 3e-14; Schur commutant dimension 1 exact to 1e-10 singular values) and COMPUTED-AT-POINTS (eigenvalue scans over 280-point phase-space grids per s value, both m = 0.3 and the m -> 0 CLOP normalization; positive control C1 massless graviton, negative control C2 flipped-norm longitudinal detectable and growing); ARGUED where marked (the lift of the CLOP-band arithmetic to tensor numerators via Schwarz pairing of the a_+/a_- line numerators; the vertex tensors are arbitrary rather than derived from the Stelle action). Test: W134 14/14 exit 0. NO canon / RESEARCH-STATUS / claim-status / verdict / posture change. H59 remains OPEN."
depends_on:
  - explorations/path2-wave4-target2-two-loop-overlap-selfenergy-2026-07-13.md
  - papers/candidates/keep-and-grade-loop-cost/keep-and-grade-loop-cost-2026-07-11.md
  - tests/W124_stageA_sunset_graded_vs_LW_CLOP.py
  - tests/W124_stageB_overlap_kite_cuts.py
  - tests/W48_H59_krein_loop_positivity_gate.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W134_stageC_tensor_numerators.py
external_refs:
  - "Stelle, Renormalization of higher-derivative quantum gravity, PRD 16 (1977) 953 -- the fourth-order propagator and its massive spin-2 pole"
  - "van Dam & Veltman, NPB 22 (1970) 397; Zakharov, JETP Lett. 12 (1970) 312 -- the longitudinal/vDVZ structure of the massive spin-2 propagator, the named failure mode hunted here"
  - "'t Hooft & Veltman, Diagrammar, CERN 73-9 -- cutting equations put cut lines exactly on-shell with pole-residue numerators"
---

# Path-2 Wave-5 (W134) -- Stage C: spin-2 tensor numerators on the two-loop cuts

**Role.** W124 computed the two-loop graded-vs-Lee-Wick cut structure (sunset at the mixed
threshold, kite overlap) with SCALAR internal lines and left Stage C open with an ARGUED-only
claim: tensor numerators cannot flip the `(-1)^{n_ghost}` cut parity. This wave computes that
claim. Five personas ran inline, sequentially (tensor-loop engineer, higher-derivative-gravity
propagator specialist, Krein specialist, numerical engineer, adversarial skeptic); their
outputs are folded into the sections below. Deterministic test:
`tests/W134_stageC_tensor_numerators.py` (14/14, exit 0). Units `M = 1`, normal mass
`m = 0.3` (and the `m -> 0` CLOP normalization where the threshold is exactly `4M^2`).

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md discipline)

| Object | Constructions in play | Handling |
|---|---|---|
| **The cut numerator** | (i) covariant on-shell projector `P2(k)`; (ii) explicit polarization sum `sum_a eps_a eps_a` | proven EQUAL on-shell to machine precision (E2); this equality IS the positivity mechanism |
| **The internal little-group metric** | (i) uniform `+delta` with the Krein sign overall; (ii) internal `eta` on the 5 polarization labels | IDENTIFIED, not defaulted: (ii) is excluded by Schur irreducibility (F1) and by direct covariance failure (F2); the repo's grading (W54 / keep-and-grade Result 3) carries its signature on frequency shells, uniform across the multiplet (F3) |
| **The vertex** | arbitrary complex tensor (vertex-independent statement) vs the specific Stelle vertices | arbitrary: the positivity claim quantifies over ALL vertices, so no vertex derivation is needed for the SIGN claim (magnitudes would need the real vertices) |
| **Positivity language** | Krein-graded optical theorem only | W48 gate discipline unchanged: nothing here is loop positivity; the odd-cut leak SURVIVES tensor numerators (P1) |

## 1. The projector algebra (personas 1 + 2)

On a Cutkosky cut every line is exactly on-shell and contributes its pole-residue numerator.
For the Stelle TT propagator `1/(p^2 (p^2 - m2^2))` the massive-pole residue is
`-(1/m2^2) P2(k)`: the minus sign is the Krein sign and rides the OVERALL residue; the repo's
`m2_eff` band (`m2^2 = m2_eff mu_DW^2`, `m2_eff in [5/6, 5/4]`, H25) is a positive overall
normalization that cannot affect any sign statement. The projector, all indices upper,
`eta = diag(1,-1,-1,-1)`:

    P2^{mn,rs}(k) = 1/2 (th^{mr} th^{ns} + th^{ms} th^{nr}) - 1/3 th^{mn} th^{rs},
    th^{mn}(k)    = k^m k^n / M^2 - eta^{mn}.

Note the projector decomposition of the fourth-order propagator uses `k^m k^n / k^2`; at the
pole `k^2 = M^2` the two agree, so the on-shell cut numerator is unambiguous even though the
off-shell contact terms differ.

**The exact identities (COMPUTED, machine-checked at rest and at boosted momenta up to
`|k| = 3.9 M`):**

- E1: the five massive spin-2 polarization tensors (rest-frame symmetric traceless spatial
  basis, boosted) are transverse (`k_m eps^{mn} = 0`), traceless, and orthonormal with
  POSITIVE norms under the metric contraction: `eps_a . eps_b = +delta_ab` (Gram deviation
  `< 1.2e-14`). The positive norm is the load-bearing fact: for a massive particle both
  tensor indices are carried by spatial vectors in the rest frame, and the two `(-1)`s from
  the mostly-plus-time metric square away.
- E2: **on-shell completeness**: `P2(k) = sum_a eps_a eps_a` with UNIFORM `+1` weights, to
  `2.8e-14`, longitudinal `1/M^2` and `1/M^4` pieces included. The covariant projector IS
  the uniformly-weighted polarization sum; positivity of the cut numerator is then automatic
  for any vertex `V`: `V* P2 V = sum_a |eps_a . V|^2 >= 0`.
- E3: the delta-weighted sum is polarization-basis independent (`7e-15` under a random SO(3)
  basis rotation): it is a genuine covariant tensor, as a propagator numerator must be.

## 2. The Krein-twist fork (persona 3)

Could the graded ghost's polarization sum carry the Krein metric INTERNALLY -- `eta` on the
little-group indices, some polarizations positive-norm and some negative -- rather than an
overall `-1`? This is the construction fork named in the task; it is identified and settled,
not defaulted:

- **F1 (Schur, COMPUTED).** The SO(3) little group acts irreducibly on the 5-dimensional
  spin-2 polarization space: the commutant of two generic Wigner rotations is computed to be
  exactly 1-dimensional (stacked-Sylvester nullspace, singular-value threshold `1e-10`).
  Any rotation-invariant internal metric is therefore a multiple of the identity: `+-delta`
  only. A nontrivial internal `eta` is forbidden for ANY massive spin-2 line, graded or not.
- **F2 (direct exclusion, COMPUTED).** The eta-twisted sum with weights `(+,+,+,-,-)` is
  polarization-basis DEPENDENT: under the same SO(3) basis rotation it shifts by `23.3`
  (Frobenius max-entry) while the delta-weighted sum shifts by `7e-15`. The twisted sum is
  not a tensor and cannot be any propagator numerator. The internal-eta branch is EXCLUDED,
  not merely disfavored.
- **F3 (repo-construction identification).** The keep-and-grade grading carries its Krein
  signature `(+,-,-,+)` on the FREQUENCY shells `(omega_1 pm, omega_2 pm)` (Result 3 of the
  keep-and-grade candidate; `tests/W54`): the sign separates the ghost oscillator from the
  graviton oscillator and is uniform across each little-group multiplet. The repo's own
  construction sits on the allowed branch.

**Fork resolution: ghost line = (positive `delta` internal metric) x (overall `-1` Krein
residue sign).** Both branches were computed; the eta branch fails covariance (F2) and Schur
(F1), so there is no surviving construction on which the parity map could break by an
internal twist.

## 3. The positivity scans and the longitudinal hunt (personas 4 + 5)

The sesquilinear form `Q_k(T) = T*_{mn} P2^{mn,rs}(k) T_{rs}` over ALL complex tensors `T`
(16-dimensional; rank of `P2` is 5) was scanned across full grids of the Stage-A two-ghost
cut phase space (10 pair-mass values x 7 angles x 2 azimuths = 140 points, 280 cut lines per
`s`), at `s = 5, 6, 8, 12` in units `M = 1`, in both normalizations (`m = 0.3`, where `s = 5`
is below the `(2M+m)^2 = 5.29` threshold and the cut is exactly empty, and `m -> 0`, the CLOP
normalization with threshold exactly `4M^2`):

| s | m | cut lines | max `\|k\|` | min eigenvalue | min NONZERO eigenvalue | max eigenvalue |
|---|---|---|---|---|---|---|
| 5.0 | 0 | 280 | 0.497 | `-7.8e-16` | 1.0000 | 1.82 |
| 6.0 | 0 | 280 | 0.704 | `-8.8e-16` | 1.0000 | 2.97 |
| 8.0 | 0 | 280 | 0.996 | `-1.7e-15` | 1.0000 | 6.28 |
| 12.0 | 0 | 280 | 1.411 | `-5.9e-15` | 1.0000 | 16.86 |
| 5.0 | 0.3 | -- | -- | empty (below threshold, exact) | -- | -- |
| 6.0 | 0.3 | 280 | 0.417 | `-5.1e-16` | 1.0000 | 1.54 |
| 8.0 | 0.3 | 280 | 0.817 | `-8.7e-16` | 1.0000 | 3.96 |
| 12.0 | 0.3 | 280 | 1.287 | `-3.2e-15` | 1.0000 | 12.74 |

- **S1: no indefiniteness anywhere.** At every sampled point the spectrum is 5 positive
  eigenvalues and 11 zeros; the worst minimum across all scans is `-5.9e-15` (numerical
  zero). COMPUTED-AT-POINTS across the grids.
- **S2: the longitudinal growth is positive growth (the skeptic's verdict).** The
  `k k / M^2` pieces DO grow on the phase space: the maximum eigenvalue rises from 1.5 to 17
  across the scanned window, and would grow without bound at larger `s`. But the growth is
  confined to the positive eigenvalues; the minimum never leaves zero. The mechanism is
  exact, not accidental: ON-SHELL the projector equals `sum eps eps` (E2), a manifestly
  positive object, so no amount of longitudinal growth can push an eigenvalue negative. The
  vDVZ/contact-term structure lives in the OFF-shell continuation (where `th` is indefinite),
  which cuts never sample. The naive positivity argument fails only off-shell, and cuts are
  never off-shell.
- **S3: both lines together.** The product form `P2(k1) x P2(k2)` on the full 256-dimensional
  vertex space is positive semidefinite at the sampled points (min eigenvalue `-2.5e-14` at
  `s = 12` against a max of 113).
- **S4: vertex-independence, two routes.** For random complex vertex tensors, the
  polarization sum `sum_ab |eps_a(k1) eps_b(k2) . V|^2` equals the projector-chain
  contraction `V* (P2 x P2) V` to `1e-8` relative, and is nonnegative: the cut integrand is
  `|M|^2`-like for EVERY vertex, derivative vertices included. Derivative vertices change
  MAGNITUDES (they grow with `s`, W55's proxy) but enter the sign structure only through
  `V`, over which the statement quantifies.
- **C1 (positive control):** the massless graviton's two helicity tensors give the standard
  positive cut form (eigenvalues exactly `{1, 1, 0, ...}`).
- **C2 (negative control):** deliberately flipping the longitudinal polarization's norm to
  `-1` produces a detectable negative eigenvalue that GROWS with `|k|` (`-2.8` at `s = 6`,
  `-14.8` at `s = 12`): the detector is sensitive to exactly the longitudinal failure mode,
  and the true projector does not show it. This is also what an internal Krein twist WOULD
  have done had the fork gone the other way: the eta branch fails covariance before it ever
  reaches the cut, but if forced it would produce indefiniteness concentrated in the
  longitudinal sector and growing with energy.

## 4. Parity assembly and verdict

With `N >= 0` the cut integrand is `N x (-1)^{n_ghost} x dPhi`:

- even two-ghost cut (Stage A sunset): `(+1) x N > 0` -- the graded positive cut of W124 G1
  survives tensor numerators;
- odd one-ghost cut (Stage A one-ghost sunset K2; Stage B kite ghost cuts B3): `(-1) x N < 0`
  -- the W48 leak equally survives tensor numerators (assembled numerically at a
  representative point, P1: `N = 36.83`, even cut `+36.83`, odd cut `-36.83`).

**VERDICT: PARITY-SURVIVES-COMPUTED.** The `(-1)^{n_ghost}` cut-parity structure of the
scalar core lifts intact to spin-2 tensor numerators: tensor numerators multiply every cut by
a positive (vertex-dependent) form factor and cannot flip any sign. What this does to W124's
conclusions: Stage C closes in the direction W124 section 3 argued; every Stage A / Stage B
sign statement (graded even-cut positivity, odd-cut leak, disjoint-loci map, the CLOP
endpoints-as-family-answers reading, the state-space integer arithmetic K1) now holds at
spin-2 tensor level, not just scalar-toy level. The magnitudes (and hence UV behavior,
resonance-window width in physical couplings) are NOT computed here; they need the real
Stelle vertices. The one remaining ARGUED step on the W124 ledger for the LW side is
unchanged (the finite-width LW boundary value by Euclidean continuation), plus one new named
ARGUED step: the lift of the CLOP-band arithmetic itself to tensor numerators uses Schwarz
pairing (conjugating the `a_+` line maps its complex-mass projector numerator to the `a_-`
line's, so the mixed-bubble reality of W124 L1 survives real tensor structures); this was
not recomputed as a loop integral.

## 5. What this does NOT do

No full tensor two-loop integration (not needed for the sign claim, which quantifies over
vertices). No derivation of the Stelle cubic vertices; magnitudes and UV growth are out of
scope. No recomputation of the CLOP band with tensor numerators (ARGUED via Schwarz pairing,
named above). No statement inside the resonance window (W124 R1/R2 guard unchanged). No
claim that keep-and-grade loop positivity holds: the odd-cut leak is CONFIRMED to survive
tensor numerators, which if anything hardens the W48 gate. No canon / RESEARCH-STATUS /
claim-status / verdict / posture change. **H59 remains OPEN.**

**Artifacts:** this file + `tests/W134_stageC_tensor_numerators.py` (14/14, exit 0) + an
appended Stage-C status update in
`papers/candidates/keep-and-grade-loop-cost/keep-and-grade-loop-cost-2026-07-11.md`
(append-only, prior text unchanged).
