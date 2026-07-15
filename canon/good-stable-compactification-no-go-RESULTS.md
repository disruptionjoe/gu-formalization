---
title: "The Good-Stable Compactification No-Go (canon spine)"
status: canon
doc_type: results
created: 2026-07-15
canon_promoted_at: 2026-07-15
tier: internal
gu_independent: true
verdict: "RESOLVED as a structural no-go for the neutral / adjoint / charged-EXTREMAL order-parameter classes (everything GU natively builds); SCOPED (honestly open) only against exotic NON-extremal charged vectors and against denying Proposition 1. Conditional on the Krein positive-majorant definition (Prop 1) and the W235 record bit."
certificate: "tests/W234, tests/W237, tests/W240, tests/W241, tests/W243 (all exit 0) + independent re-verify tests/W244_reverify_good_stable_nogo.py (40/40, exit 0)"
source_explorations:
  - explorations/W234-condensate-vev-isotropy-gate-2026-07-15.md
  - explorations/W237-channel-s-condensate-isotropy-2026-07-15.md
  - explorations/W240-z2even-compact-image-nogo-2026-07-15.md
  - explorations/W241-dynamical-vacuum-coincidence-escape-2026-07-15.md
  - explorations/W243-charged-corridor-closure-2026-07-15.md
reverified_by: explorations/W244-reverify-good-stable-nogo-2026-07-15.md
frozen_packet: packets/GU-002-good-stable-nogo.md
---

# The Good-Stable Compactification No-Go

**Canon means: safe to cite as the current public spine of the project. It does not mean proved physics.**
This is a GU-INDEPENDENT structural result (canonical claim 6: GU-independent results are co-equal products):
a theorem about Krein good-stables carrying an anticommuting grading boost. It is stated without reference to
`chi(K3)`, or the numbers 24 / 8 / 3, and it does NOT move any verdict. **Internal tier** -- reproduced and
independently re-verified within this process (W244), not yet externally replicated or Lean-ported.

## Canonical statement (scope, assumptions, quantifiers)

Let `G = Sp(32,32;H)` be the internal arena (the non-compact real form whose non-compactness IS the Krein /
indefinite form), with Cartan decomposition `g = k + p`, maximal compact `k = sp(32) + sp(32)` (dim 4160),
and `4096` non-compact generators in `p`. Let `Z = tau3(null) = sigma1(definite)` be the generation / mirror
grading. Adopt "good-stable" in the Krein sense of **Proposition 1** (an admissible invariant positive
majorant `eta.C > 0` exists iff the isotropy has relatively compact image). "Chirality-safe" means the
`Z2`-ODD generation / mirror Dirac mass (channel D) is forbidden as an isotropy invariant, i.e. the discrete
`Z2` grading is unbroken.

> **Theorem (good-stable compactification no-go).** In `Sp(32,32;H)`, a chirality-safe good-stable requires a
> compact-image (Proposition 1) isotropy whose adjoint reducing direction is intrinsically `Z2`-ODD, because
> the grading `Z` is a non-compact non-elliptic boost (`Z in p`, `ad(Z)` real and nonzero, `exp(tZ)`
> unbounded) that no Cartan involution commutes with (Theorem C). Consequently NO neutral, adjoint, or
> charged-EXTREMAL order parameter -- everything GU natively builds -- delivers a chirality-safe good-stable
> interior. The sole surviving escapes are (i) GU-non-native NON-extremal charged vectors and (ii) denying
> Proposition 1 (a boundary / firewall positivity).

### The mechanism to state (robust formulation -- W240(C) / W243)

The canonical, robust reason chirality dies is a fact about the **reducing order parameter itself**, not a
post-hoc property of the residual group:

> Any adjoint order parameter `P'` that reduces `G` to a maximal compact `k' = z_g(P')` must satisfy
> `[P', Z] != 0` (otherwise `Z in cent(P') = k'`, forcing the non-elliptic boost `Z` into a compact
> algebra -- impossible). By Theorem C every such Cartan involution `P'` is `Z2`-ODD. Therefore the
> condensate `P'` pairs generation with mirror and kills chirality directly.

The three rank-independent no-go classes (W240) and the charged-corridor closure (W243) instantiate this:

- **(A) `Z`-neutral order parameters, any rank, any SET.** If `dR(Z) w = 0` then `exp(tZ)` fixes `w`, so the
  non-compact `Z` lies in the common isotropy `intersection_i Stab_G(w_i)` -> non-compact image -> no
  compactification.
- **(B) Adjoint / operator-type order parameters, any rank.** `O` is `Z2`-EVEN iff `[O, Z] = 0` iff
  `Z in cent(O) = Stab_G(O)` -> non-compact. W237's null-pair bilinear theorem
  (`COMPACTIFY <=> Z2`-ODD) is exactly the rank-2 case.
- **(C) The maximal-compact good-stable target.** No Cartan involution commutes with the non-elliptic `Z`
  (Theorem C), so the reducing direction is intrinsically `Z2`-ODD -- the chirality-killing channel-D
  direction.
- **Charged corridor (W243).** For a boost grading `Z in p` the algebra `ad(Z)`-grades as
  `g = g_- + g_0 + g_+`; `g_+`, `g_-` are the nilradicals of the `Z`-parabolic and every nonzero element is
  nilpotent. An EXTREMAL-weight `Z`-charged vector is annihilated by the raising (or lowering) nilradical,
  which therefore lies in its stabilizer; a real subalgebra containing a nonzero nilpotent cannot be compact,
  so the stabilizer always retains a non-compact parabolic. Every native condensate is an extremal tensor
  component, so this closes the one corridor W240 left open, UNCONDITIONALLY for the extremal / native class.

Channel S (`(16bar)^4`, additive `Z`-charge `-4`, all-mirror = the minimal extremal charge) is closed twice
over: it has no `SO(10)`-singlet order parameter at all (W231 / W237, emptiness), and even if it did its
stabilizer would be non-compact by the W243 extremal nilradical theorem (isotropy-level).

## Grade (operative)

Copied from the operative grade language of W240 / W243 and the independent re-verification W244:

- **EXACT** (machine-verified, finite-dimensional facts) for: `Z = tau3(null) = sigma1(definite)` being a
  non-compact non-elliptic generator (`ad(Z)` real, `max|imag| = 1.1e-16`, `max|real| = 2.00`; `exp(tZ)`
  `e^t`-unbounded, not conjugate into `k`); the operator identity `tau1(null) -> P = diag(+1,-1)` under the
  fixed hyperbolic rotation; the per-pair parities (`{P,Z}=0`, `[Z,Z]=0`); the centralizer arithmetic
  (`cent(P)` = maximal compact, `cent(Z)` not); the `ad(Z)` three-grading with nilpotent nilradicals; the
  extremal-weight annihilation; the `SO(2,1)` charged-but-compact-stabilizer non-eigenvector fact; and the
  exact `8256 / 4160 / 4096` arena arithmetic for `Sp(32,32;H)`.
- **STRUCTURAL / rank-independent** for the lift of the faithful finite `so(n,n)` / `u(2,2)` models to the
  genuine `Sp(32,32;H)` arena and for the three no-go classes plus the extremal nilradical theorem. Every
  load-bearing argument uses only the Cartan decomposition `g = k + p`, `Z in p` semisimple, rep-theoretic
  extremal weights, and "a compact real algebra has no nonzero nilpotents (all elements elliptic)" -- none
  depends on the rank or on the division algebra `H`. Verified in `so(3,3)` / `so(4,4)` / `so(5,5)` with a
  matched anticommuting boost (same finite faithful-model status as W216 / W224 / W234 / W237 / W240 / W243).
- **CONDITIONAL** on the Krein positive-majorant definition of good-stable (Proposition 1) and on the W235
  record bit (the whole comparison lives on the favorable, record-conserved / chirality-relevant branch).
- **HONESTLY OPEN** for the non-extremal charged corridor (interior `Z`-eigenvectors and non-eigenvector
  `SO(2,1)`-type timelike vectors), the interacting source action, the physical state space, and the
  observable algebra.

## Escapes / residuals (the honest exits)

The no-go is UNCONDITIONAL for everything GU natively builds but not an unconditional Lie-theory no-go. Two
escapes survive and are listed as the honest residuals:

1. **GU-non-native NON-extremal charged vectors.** A charged vector CAN have a compact stabilizer if it is
   NON-extremal (an interior `Z`-eigenvector, or a non-eigenvector timelike vector as in the `SO(2,1)`
   witness whose stabilizer is `SO(2)`). This class is not closed by the extremal nilradical theorem, and it
   is not how a definite-charge / definite-chirality condensate order parameter is built (those are extremal
   tensor components). If such an object existed AND were GU-native it is exactly what H59 needs; GU does not
   build it.
2. **Deny Proposition 1 (the firewall boundary).** The no-go is conditional on the Krein positive-majorant
   definition. A GU-native non-majorant positivity (a PT / pseudo-Hermitian positivity on a proper subspace,
   or a boundary / firewall positivity that lives on the interface rather than the bulk arena) is a different
   object, out of scope here, and is exactly the canonical Firewall-Boundary Hypothesis
   (`canon/firewall-boundary-hypothesis.md`).

The no-go is additionally CONDITIONAL on the W235 record bit (favorable / record-conserved branch) and rests
on the standing `Cl(9,5) = M(64,H)` rep-canonicity caveat.

### Correction incorporated from the independent re-verification (W244)

W244 re-derived every load-bearing step from an independent setup and returned SURVIVES, with one substantive
imprecision that this canon doc deliberately does NOT canonize: **W241's isotropy-level lemma "good-stable =
compact image `<=>` commutes with the specific `P`" is overstated.** A tilted maximal compact
`k' = g K g^{-1}` is compact-image (elliptic generators) yet does not commute with `P`, so "compact image
`=>` commutes with `P`" is false; read literally it would wrongly close the non-extremal charged corridor that
W240 / W243 correctly keep open. The conclusion of W241 (the coincidence escape is closed) is right; only its
stated mechanism is a frame-dependent overstatement. This doc therefore canonizes the ROBUST W240(C) / W243
order-parameter mechanism instead (the reducing direction `P'` is itself `Z2`-ODD; extremal charged vectors
carry a nilradical). W241 itself carries a dated correction block pointing here and to W244.

## Promotion-Rule criteria (all six addressed)

1. **Clear scope statement.** The theorem, arena (`Sp(32,32;H)`), the good-stable definition (Prop 1), the
   chirality-safe definition, and the quantifier "neutral / adjoint / charged-extremal order parameters" are
   stated above.
2. **Proof or falsification target.** Proof: Theorem C (no Cartan involution commutes with the non-elliptic
   `Z`) plus the extremal-weight nilradical theorem. Falsification target: exhibit a GU-native chirality-safe
   compact-image good-stable, i.e. a native NON-extremal charged VEV with a compact stabilizer, or a working
   non-majorant (deny-Prop-1) good-stable.
3. **Explicit assumptions.** Proposition 1 (Krein positive-majorant definition of good-stable); the W235
   record-conserved branch; the `Cl(9,5) = M(64,H)` rep-canonicity caveat; extremal-only for native
   condensate order parameters.
4. **Known failure modes.** The two escapes above (non-extremal charged corridor; deny Proposition 1), plus
   the finite-model -> full-arena STRUCTURAL lift and the unbuilt source action / state space / observable
   algebra.
5. **No dependency on internal work artifacts.** The next action (attack the two escapes) is fully specified
   by in-repo explorations, tests, and the frozen packet GU-002; no internal work-artifact system is needed.
6. **No stale stronger status after the consistency sweep.** The claim-status-consistency sweep
   (`lab/process/runbooks/claim-status-consistency-quality-workflow.md`) was run across `RESEARCH-STATUS.md`,
   `CANON.md`, the `canon/*` RESULTS docs, and the W-notes; no owner surface asserts a stronger status than
   this scoped structural no-go, and W241's overstated mechanism is marked superseded on its own surface.

## Support (machine)

Internal tier; no Lean / Lake build was run.

| test | result |
|---|---|
| `tests/W234_condensate_vev_isotropy_gate.py` | 35/35, exit 0 (positive controls first) |
| `tests/W237_channel_s_condensate_isotropy.py` | 44/44, exit 0 |
| `tests/W240_z2even_compact_image_nogo.py` | 27/27, exit 0 |
| `tests/W241_dynamical_vacuum_coincidence_escape.py` | 46/46, exit 0 |
| `tests/W243_charged_corridor_closure.py` | 26/26, exit 0 |
| `tests/W244_reverify_good_stable_nogo.py` (independent re-verify) | 40/40, exit 0 |

All positive controls run first and each fires on a real falsifier (the escape detector fires on a planted
chirality-safe + compact-image pair, so the no-go has teeth). W244's regression shares no code with the
originals.

## Scope / what this does NOT do

- **Does NOT move `bar(b)`, H59, or the generation count. Those stay OPEN and Joe-gated.** This is canon =
  public-spine framing (a characterization), not a verdict flip. No debit is added or cleared.
- Does not claim GU has no good stable, nor that GU is falsified (unbuilt is not false). It is the narrower,
  computed result that the chirality-preserving compactification GU would need is structurally blocked for
  every order parameter GU builds, and that the only mathematical escapes are a charged NON-extremal VEV (not
  GU-native) or a non-majorant boundary positivity (a different object).
- Does not decide the W235 record bit; the whole comparison lives on the favorable branch.
- Does not assert any cross-repository identity; the reservoir Krein sign and the `Y14` spectral-section /
  record datum remain gated time-as-finality / temporal-issuance objects.

## Cross-references

- `canon/firewall-boundary-hypothesis.md` -- this no-go is the independent-convergence evidence already
  logged there (bearing on falsification criterion 1); its deny-Proposition-1 escape IS that hypothesis.
- `packets/GU-002-good-stable-nogo.md` (+ `packets/GU-002-good-stable-nogo-v0.2.json`) -- the issued frozen
  packet of this result (source revision pinned; five legs modeled as one dependent proof chain, not
  independent evidence).
- Source explorations W234 / W237 / W240 / W241 / W243; independent re-verification W244.
