---
title: "Hardening H3: the 192-dim triplet lift — the graded quotient and the C-operator on the actual structure (gaps G-B1 + the D1 lift)"
status: active_research
doc_type: exploration
created: 2026-07-19
directed_by: "Joe direct chat, 2026-07-19 (hardening swings)"
axiom: lab/process/boundary-adapter-standing-axiom.md
extends:
  - explorations/channel-swing-CH-QM-2026-07-19.md
  - explorations/d1-coperator-build-2026-07-19.md
inputs:
  - explorations/channel-swing-CH-SRC-2026-07-19.md
  - canon/ghost-parity-krein-synthesis.md
  - tests/generation-sector/ghost_parity_krein.py
  - tests/generation-sector/gen_sector_bridge.py
  - tests/channel-swings/ch_qm_graded_quotient_toy.py
  - tests/channel-swings/d1_coperator_build_probe.py
  - explorations/big-swing-2026-07-06/R3-pt-phase-classification-gu-cores.md
runnable:
  - tests/channel-swings/h3_triplet_lift_probe.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Hardening H3: the 192-dim triplet lift

The CH-QM graded-quotient toy and the D1 C-operator build both ran on a
9-dim miniature and both declared the same lift path: do it on the ACTUAL
192-dim self-dual generation triplet. This swing executes that lift.
Receipts: `tests/channel-swings/h3_triplet_lift_probe.py`, run 2026-07-19,
exit 0, headline `21 [E] + 2 [F] = 23` (setup `[T] = 7` excluded), 21s wall
time, float64 with exact structural anchors (many certificates land at
literal `0.0e+00`; every residual ceiling printed).

**Headline (the honest one): the mechanism survives scale unchanged — and
the one thing that does NOT survive is the toy's silence about the gap.**
At 192 dims the pair gap `delta` cannot be inserted by hand and forgotten:
the native dynamics is provably exactly scalar (Casimir residual `0.0e+00`;
R3 sign-blind), so the gap is imported openly as a TYPED conditional
(chi-odd, boost-non-equivariant — a stand-in for the unbuilt `S_IG`/B.5
global data), and the whole battery downstream is conditional on that one
declared import. The lift's value is that the mechanism survives scale;
nothing here becomes unconditional.

## 0. Five-lens council (inline, before execution)

**Representation theorist.** Approach: build the triplet from the verified
Cl(9,5) = M(64,H) rep exactly as `ghost_parity_krein.py` does — kernel of
the gamma-trace, SU(2)+ Casimir top eigenspace, K = eta_V (x) beta_S
restricted — reuse, don't reinvent; then chirality-split and SVD the
cross-pairing to get the K-canonical 96-pair frame. Trap feared: confusing
compressed so(9,5) generators with triplet-PRESERVING ones — only the
internal generators (indices >= 4, disjoint from the self-dual base
{0,1,2,3}) preserve the triplet; equivariance statements must use those, with
leak checks. (Also: the reused SU(2)+ generators carry a factor-2
normalization, so the triplet Casimir is 4j(j+1) = 8, not 2 — caught at run
time, spectrum 8/3/0 = triplet/doublet/singlet.)

**Constraint/BV theorist.** Approach: the battery fixture must be the toy's
structure with the REAL pair sector: gauge hyperbolic block + the 192-dim
triplet in its pair frame, causality coupling on, the transmitted object the
action-level Noether row `delta_2 = K(n_sigma*, H .)`, quotient
`ker delta_2 / im d_{RS,-1}`. Trap feared: the interaction dressing — a
"parity-even" `V_pe` is parity-even RELATIVE TO the imported grading, so it
silently presupposes the import; this must be stated, not hidden (in the
9-dim toy this circularity was invisible because the toy also hand-inserted
the gap).

**Krein operator theorist.** Approach: the D1 recipe is dimension-agnostic;
run it verbatim. At the native point the single eigengroup's Krein Gram has
signature (+96,-96): the recipe MUST abort loudly (K-indefinite), and the
continuum must be exhibited constructively — including independent PER-PAIR
boosts, not just the global one, because at scale the admissible set is the
symmetric space U(96,96)/(U(96)xU(96)), dimension 2*96^2 = 18432. Trap
feared: letting numpy's arbitrary eigenbasis at the degeneracy manufacture a
"determined" C; and sector collision — the dressing amplitude must be capped
below half the gap (spectral norm) or the two graded sectors can collide and
fake a K-indefinite group off-degeneracy.

**Numerical engineer.** Approach: 192 dims is COMPUTABLE — insist on the
actual object, no proxies. Exact structural anchors exist and must be used:
`Gamma Gamma^dag = 14 I` exactly (each gamma unitary), so `Pi_RS` is exact;
gamma entries are exact `+/-1, +/-i`; the Casimir-scalar and co-flip checks
should land at machine zero. Budget: the 1792-dim work (Casimir products,
kernel SVD, dressed C2) is seconds-to-minutes; do the compensator sector at
FULL 1792-dim scale, not a miniature. Trap feared: tolerance theater —
print residual ceilings, and where a certificate is exact-by-algebra
(e.g. `{chi, G_gap} = 0` in the frame) say so and report the frame-fidelity
residual separately.

**Skeptical auditor.** Approach: guard the conditionality ledger. The toy's
`delta` was a fixture parameter; at scale it is THE missing object — if the
lift quietly ships a gapped Hamiltonian and reports "battery passes," it has
assumed `S_IG` without saying so. Demand: (i) the native (delta = 0) point
run FIRST as the unconditional statement (recipe aborts, continuum exists);
(ii) the import declared with a type (what algebraic properties force it
outside the native family); (iii) success criteria taken from the prior
swings' own cards (six-certificate battery, wrong-orientation cohomological
failure, D1's "determined off-degeneracy / continuum at the degenerate
point / datum exactly one Z/2"), not redefined. Trap feared: the lift
"confirming" the toy by importing more than one datum — count the imports.

**Chair synthesis (fixes to the plan).** (1) Run the native point first;
the gap enters only afterwards, as the typed import, and everything
downstream is labeled conditional on it. (2) Type the import doubly:
chi-oddness (exact anticommutation with the triplet chirality — R3 says
chi-odd content has no GU-native carrier) and non-equivariance (commutator
defect against triplet-preserving internal boosts, with the compact
rotation as control). (3) Cap `V_pe` at spectral norm 0.15 < delta = 0.2 so
sectors cannot collide. (4) Compensator sector at full 1792 dims via the
dressed-constraint C2 scale law (the archaeology item 8 weld check), with
the scale-carrying kernel control made strong enough to actually vary
(kernel scale relative to `|xi_0|^2`); what cannot be built at scale
(compensator field tier, antighost leg, non-abelian master equation) is
typed as gaps G-COMP-1..3, per the standing axiom. (5) Reuse the toy's
Part-A register verbatim for Q4 — the storage argument is
dimension-independent; re-run it, don't re-derive it. Execute.

## 1. The triplet, built (chair item: reuse) — PART 0, all [T] PASS

From the verified rep (`gen_sector_bridge` anchors reproduced: bare
commutator 58.7215, C2 = 155.3625):

| structure | result | residual |
|---|---|---|
| `Gamma Gamma^dag = 14 I` | exact — `Pi_RS` is an exact structural anchor | `0.0e+00` |
| SU(2)+ Casimir top eigenspace on `ker(Gamma)` | dim 192, Casimir 8 (= 4j(j+1), j = 1), spectral gap 5 to the doublet | exact to 1e-9 |
| `K` restricted to the triplet | signature (+96, -96); **every eigenvalue exactly +/-1** | — |
| chirality `chi` | preserves the triplet, splits 96/96, each half TOTALLY K-null, `{K, chi} = 0` | all ~1e-14 |
| cross-pairing of the null halves | full rank; **all 96 singular values exactly 1.0000** — the pairing is not merely nondegenerate, it is exactly unitary in the chirality-split orthonormal frames | frame residual `||B - swap|| = 4.0e-14` |
| `J_quat` (canon C07 convention) | preserves the 192-dim triplet AND the canonical 96-dim physical sector | leaks 7.2e-14 / 5.1e-14 |
| Q4 register (toy Part A) | re-run verbatim: loop-coherent, locally unreadable, full loop reads the bit | PASS |

New structural finding (not in canon at this sharpness): the pairing
singular values are all exactly 1 — `K|triplet` is exactly the swap in the
chirality-split orthonormal bases, with no pair-dependent weights. The
K-canonical pair frame therefore exists with NO rescaling freedom beyond
the per-pair hyperbolic boosts that the D1 continuum already counts. And
the CH-QM A4 typing (the orientation is J_quat-commuting) now holds at the
actual 192-dim sector, not only at the 128-dim carrier level.

## 2. The six-certificate battery at 192 dims (gap G-B1) — PARTS 1-2

Fixture: 194-dim = gauge hyperbolic block (g, s) + the full triplet in its
pair frame (the ACTUAL numerical `B_t`, not an idealized stand-in). Pair
dynamics `mu I + delta G_gap + V_pe` (delta = 0.2 the typed import, Section
3; `V_pe` parity-even K-Hermitian dressing, spectral norm 0.15 < delta),
causality coupling c = 0.35, `sigma* = +1` baked into the action side,
transmitted row `delta_2 = K(n_sigma*, H .)`.

**RIGHT orientation — all six pass on the real form:**

| certificate | result at 192 dims |
|---|---|
| Q1 closure | `|delta_2 . d_(-1)| = 0.0e+00` exact |
| Q1 quotient | im d in ker; all 96+96 representatives in the constraint surface, K-orthogonal to the orbit (max residual `0.0e+00`) |
| Q6 | 96-dim physical Gram positive-definite, eigenvalues all 1.000000 |
| Q5 | descended H Hermitian, defect 2.8e-16 (coupling AND dressing on) |
| Q3 | Born positive, sum-1 drift 4.4e-16 over t in {0.5, 2, 7} |
| Q2 | K-Hermitian parity-even observable restricts Hermitian, defect 3.5e-14 |
| Q4 | storage-level certificate inherited (register re-run; dimension-independent) |

**WRONG orientation — fails cohomologically, same mode as the toy:**

| check | result |
|---|---|
| Noether closure | NON-closure = 0.7000 = gamma exactly (primary, cohomological) |
| quotient | ill-formed: dist(im d, ker delta_2) = 1.0000 |
| repair 1 (brute grading) | **96 negative-norm survivors** (one per hyperbolic pair, all exactly -1) |
| repair 2 (delete negatives) | zombie `n_+` in the constraint surface, Hilbert norm growth 2.0138 -> 4.0552 = `e^{gamma t}` exact, regenerated from kept ghosts (feed = c = 0.350) |
| repair 3 (retune) | numerically restores closure; structurally blocked (loop-coherent storage, Part A — scale-independent) |

CH-QM's Q1 gap ("lift from the 9-dim toy to the 192-dim triplet") is
discharged at this grade: the conditional construction exists and runs on
the actual structure, both orientations, with the wrong-orientation failure
in exactly the predicted mode.

## 3. D1 at scale: the C-operator on the actual triplet — PART 3

**(i) The unconditional statement first (native point).** The so(9,5)
Casimir on the verified spinor is EXACTLY a scalar (residual `0.0e+00`,
lambda = -22.75) — native Casimir-type pair dynamics is `mu I`, exactly
degenerate, trivially diagonalizable (geometric mult 192; NOT Jordan). The
recipe ABORTS: the single 192-dim eigengroup is K-INDEFINITE with signature
(+96, -96) — dynamics does not determine C on the actual triplet. The
continuum is exhibited constructively: global AND independent per-pair
hyperbolic boosts of the kinematic C are all admissible (K-isometries,
`C_s^2 = I`, `[C_s, H] = 0`, `B.C_s > 0`), with `||C_s - C_kin||` up to
50.15. The admissible set is the symmetric space U(96,96)/(U(96)xU(96)) of
maximal K-positive subspaces: **dimension 2*96^2 = 18432 real parameters,
versus 18 in the 9-dim toy. Non-uniqueness GROWS with scale; it does not
heal.** (Exactly what the external-bit result requires; had determination
appeared at scale, that result would have broken.)

**(ii) The typed conditional import.** `G_gap = delta *` (pair swap),
declared openly as the stand-in for the S_IG/B.5 datum, with two computed
type facts:

- **chi-ODD**: `{chi, G_gap} = 0` exactly (algebraic zero in the frame;
  frame fidelity 3.4e-14). R3 proved chi-odd content has no GU-native
  carrier — the import demand is forced, not chosen.
- **Non-equivariant along the non-compact directions**: against
  triplet-preserving internal so(9,5) generators (leaks ~4e-14), the
  commutant defect is `[G_gap, X] = 0.000` for the compact rotation (4,5)
  but `13.856` for BOTH boosts (8,9) and (5,11). The non-equivariance of
  the gap is purely a signature phenomenon — the compact directions are
  compatible with the grading, the boosts are not. This sharpens D-QM-3/B.3
  at scale: what the adapter must transmit is non-invariant specifically
  under the non-compact half.

**(iii) Conditional determination.** With the import on (+ dressing): all
192 eigenvalues real in 192 K-definite groups; `C^2 = I` (4.3e-12),
`[C, H] = 0` (5.0e-14), `G = B.C` Hermitian positive (min eigenvalue
1.000) — the interacting V-metric exists on the actual triplet,
conditionally. The determined C EQUALS the kinematic K-grading
(`||C - C_kin|| = 4.3e-12`): the audit's watched second anchor freedom does
not appear at 192 dims either. Stability 4.0e-06 under an O(1e-6)
pseudo-Hermitian perturbation; `-C` inadmissible; anchor co-flip
`B -> -B => C -> -C` EXACT (`0.0e+00`). Within the Z/2-typed payload family
the choice set is exactly `{(B, C), (-B, -C)}`: **the undetermined datum is
one Z/2 at full scale — determined off-degeneracy, continuum at the
degenerate point, datum exactly one Z/2**, which is the D1 recipe's whole
required shape. Armed control: the continuum COLLAPSES when the gap is on
(`[C_s, H]` defects 5.07 / 16.79) — determination is exactly the
gapped-pair phenomenon, at scale as in the toy.

## 4. The compensator sector at full 1792-dim scale — PART 4

Feasible at FULL scale, and done there:

- **Carrier**: `sigma_c = 0.8 Sigma_(0,9)` (fixed non-compact boost),
  non-equivariant (max `||[sigma_c, Sigma_ab]|| = 4.525`) — passes the K3
  equivariance tripwire. The equivariant alternative is dead by structure:
  the Cl(9,5) commutant is H (canon C07, M(64,H)), so an equivariant
  carrier is a quaternionic scalar and drops out of the constraint dressing
  entirely — the GHOST-01 image at full scale.
- **Dressed C2**: 179.1952 vs bare 155.3625 — the obstruction PERSISTS and
  moves UPWARD under the non-equivariant dressing, matching CH-SRC's
  mini-rep rigidity finding at the real scale. The compensator dresses; it
  does not close. The missing object is still the B.5 global data.
- **Scale law**: `C2(2xi)/C2(xi) = 2.000000000000` exact for the
  scale-free compensator (archaeology item 8 weld check, now at 1792 dims);
  [F] control: a kernel carrying an internal scale
  (`L^2 = 0.25/|xi_0|^2`) breaks it to 1.889475 — CH-GR's K3 kill is
  executable against future `S_IG` candidates on the actual structure.

Typed gaps (recorded, not stops, per the standing axiom):

- **G-COMP-1**: the compensator FIELD tier (Stueckelberg action with
  transmitted transformation law) exists only at CH-SRC's 16-dim mini-rep;
  not built at 1792.
- **G-COMP-2**: the antighost/Koszul-Tate leg as an action field: complex
  level only, at every scale.
- **G-COMP-3**: the non-abelian master equation: no fixture at any scale
  tests it.

## 5. What the lift changed vs the toy (the honest ledger)

Survived scale unchanged: the entire mechanism — closure/non-closure,
quotient well-/ill-formedness, positive physical Gram, state-preserving
descent, Born rule, observable restriction, cohomological wrong-bit
failure with all three repair branches, recipe abort at the degeneracy,
conditional determination, co-flip, one-Z/2 accounting, C2 scale law.
Several certificates got SHARPER at scale (exact 0.0e+00 where the toy had
1e-15). What did NOT survive, i.e. the headline differences:

1. **The gap's provenance.** The toy hand-inserted `delta = 0.2` as fixture
   furniture. At scale that move is unavailable: the native dynamics is
   provably exactly scalar, so the gap is a declared import with a computed
   type (chi-odd, boost-non-equivariant). The toy's battery looked
   unconditional-modulo-orientation; the lifted battery is visibly
   conditional on exactly one import. This is a change in what the result
   MEANS, surfaced by scale.
2. **The dressing's circularity.** `V_pe`'s parity-evenness is defined
   relative to the imported grading — the interaction dressing presupposes
   the import. Invisible in the toy, explicit now.
3. **The transverse mode has no scale analog.** All 192 triplet dimensions
   are paired; nothing in the triplet is natively K-positive outside the
   graded selection. The toy's transverse mode was fixture furniture, and
   the Born/observable certificates run fine without it.
4. **Non-uniqueness grows with scale**: 18 -> 18432 continuum dimensions at
   the degenerate point. The external-datum need is more acute at scale,
   not less.
5. **New structural facts**: the cross-pairing is exactly unitary (all 96
   singular values = 1) — no pair-dependent weights anywhere in
   `K|triplet`; the gap import's non-equivariance is confined to the
   non-compact directions (compact rotation defect exactly 0, boosts
   13.856); `J_quat` preserves the canonical physical sector at 192 dims
   (A4 typing lifted).

## 6. Remaining gaps

- The import is a stand-in: nothing here builds `S_IG` or the B.5 global
  data; the K-definite gap's PROVENANCE is still the program's central
  missing object (unchanged in direction, sharpened in type: chi-odd,
  boost-non-equivariant, one Z/2 riding on top).
- G-COMP-1..3 (Section 4).
- The record-drive/PT-threshold finding (D1 build, named finding) was not
  re-examined at 192 dims; the battery here runs undriven. A lifted drive
  study would put a quantitative PT-unbrokenness bound on the 96-pair
  register.
- The CH-REC co-flip hook is not lifted (their swing, their call).
- Q4 remains a storage-level certificate (the P4 gap — no QFT-shadow
  microcausality object — is untouched by scale).

## Boundary

Conditional construction under the standing axiom (`R0_COND` working
grade) throughout. The 194-dim battery fixture is a finite model whose
PAIR SECTOR is the actual triplet with its actual Krein form; the gauge
block, coupling, and dressing remain typed fixture structure; no field
theory, no Y14 geometry, no counts. The gap import stands in for the
unbuilt `S_IG`/B.5 and everything downstream of it is conditional; the
native-point results (Casimir scalar, recipe abort, continuum) are the
unconditional core. No claim status, canon verdict, scorecard, register,
or public posture moves; no external actions; files touched: this document
and the probe script only.
