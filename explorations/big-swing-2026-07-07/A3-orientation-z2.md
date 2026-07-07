---
artifact_type: exploration
status: exploration
created: 2026-07-07
title: "AS-A3 (alignment swing, route A3): THE ORIENTATION Z2 IS DISCHARGED — V8's residual discrete import ('WHICH half of each hyperbolic pair is physical') is a labeling redundancy of the Krein axioms, not physical data, at kinematic grade. Mechanism is a LOCK: P_ghost = K|_W identically (3.7e-14), so the orientation flip and the Krein-sign flip are ONE Z2, not two — the V8 identity Q5 = −P is orientation-COVARIANT (both sides flip together under frame reversal). A two-line theorem excludes any K-preserving flipper (U†KU = K and UPU⁻¹ = −P force U†U = −I); the flip is implemented instead by a GU-NATIVE norm-reversing intertwiner: chi, the Clifford 14-volume — unitary involution, preserves W, commutes with all 91 so(9,5) gauge generators (5.2e-14), both family su(2)± actions, and J_quat, and maps (K, P, Q5, Pi_mirror) → (−K, −P, −Q5, Pi_generation). The sign of K is fixed by NO axiom (−beta_S passes the full battery at the identical 0.0e+00; Ad(−K) = Ad(K) exactly, so V2's Cartan seat theta is sign-blind: the Z2 is ker(Ad: {±K} → theta)). No K-invariant native observable distinguishes W₊ from W₋ (battery max 2.6e-14 vs random-control splits 0.085–0.137). And the flip exchanges the gap target AND the physical label simultaneously: Pi_mirror = (I − K|_W)/2 as an operator identity (9.2e-16), so in EVERY orientation the condensate gaps the K-negative (ghost) half and leaves the K-positive (physical) half exactly massless. Sharp conclusion: the theory does not owe 'which half' — the question has no orientation-invariant content; the invariant prediction is 'the ghost half gaps.' V8's invoice shrinks from three items to two: any residual physical sign lives inside the ALIGNMENT hypothesis, not as a separate import."
grade: "THEOREM (kinematic scope: the 192-dim triplet sector of the (9,5) carrier with (7,7) cross-check of every headline identity; the no-K-preserving-flipper statement is an exact two-line algebraic theorem plus an exhaustive verification over all 1024 internal Clifford monomials (flip ⟺ K-reversal ⟺ odd timelike count, perfect correlation, zero exceptions); the sign-unfixedness of K is verified against the full axiom battery in both signatures; the observable scan is exhaustive over the listed battery + V1's enumerated native algebra (cited), NOT over family-tensor directions (35 × 256 dims), non-monomial combinations, or position-dependent operators; no dynamics — a built S could in principle anchor the sign only by coupling to a norm-anchored external sector, which nothing in GU currently supplies). Anchors reproduced first: rank(Gamma) = 128, ker = 1664, triplet 192, Krein (+96, −96, 0), beta_S residual 0.0e+00, |K|-eigs exactly 1, Q5 = −P at 3.7e-14. Target-import guard clean: no element of {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8} assumed, inserted, or divided by; all counts (128, 1664, 192, 96, 512, 1024) are measured outputs. Controls with discriminating power: random P-even K-self-adjoint elements split the sectors at 0.085–0.137 while the native battery sits at 2.6e-14; a random exchange involution breaks family intertwining at 32.4 vs chi's 8.6e-14; random K-unitaries preserve every Krein norm and never flip P (min ‖UPU⁻¹+P‖ = 27.8). Turok–Bateman Born-rule covariance under the joint flip is argued from canon's prose formula and FLAGGED, not source-audited."
depends_on:
  - explorations/big-swing-2026-07-06/VG-V8-t5-map-attempt.md
  - explorations/big-swing-2026-07-06/VG-V2-fourth-seat-gauge-sector.md
  - explorations/big-swing-2026-07-06/VG-V1-condensate-ghost-parity-scan.md
  - canon/ghost-parity-krein-synthesis.md
  - canon/swing-ghost-parity-no-chiral-selection.md
  - explorations/big-swing-2026-07-06/BIG-SWING-CONFORMAL-CLASS-BLOCKED.md
scripts:
  - tests/big-swing/as_a3_orientation_z2.py
---

# AS-A3: the orientation Z2 — convention or physical modulus?

**Route A3 of the 2026-07-07 alignment swing.** V8 constructed the mirror-hiding condensate
direction at kinematic grade and priced its invoice at three items: (i) one orientation Z2 —
WHICH half of each hyperbolic pair is physical; (ii) the alignment (why the condensate lands on
`Pi_mirror`); (iii) the Yukawa/derivative typing caveat. This route attacks item (i): is that Z2
fixed by structure GU already carries, or a genuine modulus?

**Outcome: neither — it is a labeling redundancy. Item (i) is DISCHARGED at kinematic grade,
and its ghost of physicality is absorbed into item (ii).**

Script: `tests/big-swing/as_a3_orientation_z2.py` (exit 0; every number below is printed by
it). Carrier machinery reused verbatim from `tests/big-swing/vg_v8_t5_map_attempt.py`.

## 0. Anchors (reproduced before any claim)

(9,5) carrier, timelike = {4..8}: rank(Gamma) = 128, dim ker = 1664, triplet dim 192, beta_S
pseudo-anti-Hermiticity 0.0e+00, triplet Krein signature (+96, −96, 0), |K|-eigenvalues on `W`
all exactly 1.000, V8 identity `Q5 = −P_ghost` at 3.7e-14. The (7,7) block reproduces its own
anchors (rank 128, ker 1664, triplet 192, Krein (+96, −96)) and every headline identity below.

## 1. The lock: the orientation flip and the Krein-sign flip are ONE Z2

The route's question presupposes two independent data: the orientation sign of `Q5` and the
physical/ghost assignment. The first measured fact collapses them:

> **P_ghost = K|_W identically** (‖P − K‖ = 3.7e-14; (7,7): 3.9e-14), hence **Q5 = −K|_W**
> (1.8e-15). The orientation of the internal spacelike frame and the sign of the Krein form
> are the SAME datum on the triplet sector. They cannot be moved independently.

Covariance check (mechanism-level, machine-verified): reversing the internal spacelike frame
orientation (e13 → −e13) negates `beta_S` (it contains e13 once) and negates the ordered
product `Q5` — so `(K, P, Q5) → (−K, −P, −Q5)` **together**, and the V8 identity `Q5' = −P'`
holds with the same relative sign (3.7e-14). The identity is orientation-covariant; only the
joint sign is free. The flipped convention has the identical signature multiset (+96, −96).

**Two-line theorem (no K-preserving flipper).** Suppose linear invertible `U` satisfies
`U†KU = K` and `UPU⁻¹ = −P`. Using `P = K` on `W`:
`K = U†KU = U†(−UKU⁻¹)U = −(U†U)K`, so `U†U = −I` — impossible (`U†U ⪰ 0`). Antilinear maps
preserving Krein norms preserve the positive cone, so they cannot swap `W₊ ↔ W₋` either
(V8: `J_quat` indeed FIXES `K`, `P`, `chi`, `Q5`). Numeric witness: random K-unitaries preserve
the Krein form at 1.1e-14, never flip `P` (min ‖UPU⁻¹ + P‖ = 27.8 over draws), and transport
`W₊` states to K-norm exactly +1.000000. **Any transformation relating the two orientations
must reverse Krein norms.**

## 2. Test (i): the native intertwiner exists, and it is chi

The two orientations ARE related by structure GU already carries — printed with residuals:

| property of chi (compressed Clifford 14-volume) | residual (9,5) |
|---|---|
| preserves `W` | 1.0e-13 |
| unitary involution, tr = 0 | 5.3e-14 / 6.7e-15 |
| **flips the orientation: chi Q5 chi = −Q5** | 5.2e-14 |
| **reverses the Krein form: chi K chi = −K** | 5.2e-14 |
| commutes with ALL 91 compressed so(9,5) gauge generators | 5.2e-14 |
| commutes with both family actions su(2)± | 8.6e-14 |
| fixed by J_quat (V8, cited) | 1.3e-13 |
| maps `Pi_mirror → Pi_generation` | 3.7e-14 |

Same in (7,7) (flip 1.0e-13, K-reversal 5.6e-14). A second native flipper for the record:
`c(e4)` (any internal timelike Clifford vector) flips `Q5` and reverses `K` (1.3e-13, 5.2e-14).
Exhaustively (Section 5): 512 of the 1024 internal monomials flip, all 512 reverse `K`, and
**zero** flip while preserving `K` — the theorem's fingerprint, with the grammar
*flip ⟺ odd number of timelike factors* (the Spin(10) grading `chi_int`, with 5, is a flipper —
this is V8's `{chi_int, P} = 0` finding re-derived as an orientation statement).

**Is chi-conjugation a gauge equivalence?** It reverses Krein norms, so the question reduces to:
is the overall sign of `K` itself native data? Machine answer: **no axiom fixes it.** `−beta_S`
is Hermitian, squares to I, and passes pseudo-anti-Hermiticity over all 91 generators at the
identical 0.0e+00 (both signatures). And the V2 connection the route asked for:

> **Ad(−K) = Ad(K) exactly (0.0e+00): V2's fourth seat theta — the Cartan involution that K
> implements — is sign-blind.** `B_theta(X,Y) = −B(X, theta Y)` uses theta alone; the maximal
> compact chain, the positivity certificate, every Cartan-relative datum sees only the
> projectivization of K. **The Z2 is precisely ker(Ad: {±K} → theta) — it lives BELOW theta,
> and nothing theta-relative can determine it.**

So: native intertwiner exists (chi), it commutes with the entire gauge + family + quaternionic
apparatus, and the one structure it negates (the K-sign) is itself unfixed by every axiom the
repo's Krein quantization states. **The two orientations are gauge-equivalent: one Z2, pure
bookkeeping.**

## 3. Test (ii): no K-invariant observable distinguishes the halves

Battery on `W₊` vs `W₋` (sorted spectra of K-self-adjoint, P-commuting native operators):

| observable | max\|spec₊ − spec₋\| |
|---|---|
| su(2)+ Cartan / generic / Casimir | 8.9e-15 / 2.6e-14 / 1.4e-14 |
| su(2)− Cartan / Casimir | 3.3e-15 / 5.8e-15 |
| so(5)_s / so(5)_t spinor Casimirs | 3.6e-15 / 7.5e-15 |
| internal compact 2-form i·e9e10, even 4-form e9..e12 | 3.1e-15 / 3.1e-15 |
| fiber scale etaV\|_W | 2.0e-15 |

Controls with power: random P-even K-self-adjoint elements split the sectors at
**0.085 / 0.137 / 0.085** — the coincidence is forced by chi intertwining, not generic; and a
random exchange involution fails to intertwine the family action at **32.4** (vs chi's
8.6e-14) — chi's status as a structure-preserving exchange is special, not automatic.

The **sole** discriminator found: `Q5` itself (spec₊ = {−1}×96, spec₋ = {+1}×96) — but `Q5`
carries the orientation and co-flips with it. Every distinguishing native object traces back to
a sign that is part of the choice, never a fixed external marker. (V8's base-leg kill closes
the one route to an external marker: no base-geometric operator reaches `W`.)

## 4. Test (iii): the flip exchanges the gap target — and the physical label, simultaneously

`chi Pi_mirror chi = Pi_generation` (3.7e-14): yes, under orientation flip the condensate
channel retargets to gap the OTHER half — the route's feared "gapping the wrong half." But the
lock makes this exactly compensating, via the operator identity (9.2e-16):

> **Pi_mirror = (I − K|_W)/2 — the projector onto the K-NEGATIVE half — in every orientation.**

Machine check in both conventions (orientation A as built; orientation B = (−K, −Q5)): the
condensate channel `phi·Pi_mirror` at phi = 1 leaves the K-positive (physical) half massless at
≤ 2.1e-15 (×96) and gaps the K-negative (ghost) half at exactly 1.000 (×96) — **both times**.
The gap target and the physical label are two readings of the same operator `K|_W`; the flip
moves them together and the invariant statement survives:

> **The condensate gaps the ghost (K-negative) half and leaves the physical (K-positive) half
> exactly massless — in every orientation. "Which half" names a basis label, not an
> observable.**

## 5. The exhaustive monomial scan

All 1024 internal Clifford monomials classified (conjugation action on `Q5`; Krein character
`m†Km = ±K`): **1024 scanned, 512 flip, 512 reverse K, overlap 512, exceptions 0.** Perfect
correlation, as the lock forces (flipping `Q5` = flipping `K|_W` is one condition, not two).
Grammar verified: flip ⟺ ODD number of timelike factors.

## 6. The sharp conclusion, and what it does to V8's invoice

The route's pre-registered branch fires in its strongest form: the two orientations are
native-equivalent AND the flip exchanges the gap target — but the refined conclusion is sharper
than "an empirical input, not a derivation":

1. **The theory does not owe an answer to "which half is physical."** At kinematic grade the
   question has no orientation-invariant content — asking it is like asking which square root
   of −1 is "really" i. The invariant prediction is: **a gapped half exists, and it is the
   ghost (K-negative) half.** That statement is orientation-free, machine-checked in both
   conventions and both signatures.
2. **V8's invoice shrinks from three items to two.** Item (i) — the orientation Z2 — is a
   convention locked to the K-sign convention, which no axiom fixes and no Cartan-relative
   datum (V2's theta) can see. What SURVIVES as physical is exactly item (ii), the alignment
   hypothesis, now statable orientation-free: **the condensate direction must be
   (I − K|_W)/2 — the condensate couples to the Krein form itself.** Even the residual coupling
   sign is absorbed: `M = mu·I − phi·q·K|_W`, and phi → −phi flips q for any even potential
   (Mannheim's conformal potential is even in phi — from memory, flagged; primary-source status
   is VG-SA territory).
3. **Canon connection.** Canon's "the physical/ghost assignment is not canonical without
   dynamics" is refined: the assignment is not canonical AND NEED NOT BE — the two assignments
   are gauge-equivalent under a native intertwiner, and every physical statement the frontier
   currently makes (mirrors gapped, generations light, positivity intact) is invariant under
   the exchange. What dynamics must still supply is not the sign but the direction: alignment.

## 7. Honest gaps

1. **Kinematic only.** No S exists. A built dynamics could anchor the K-sign only by coupling
   `W` to an external norm-anchored sector; nothing in GU currently supplies one (the base leg
   is dead — V8), but this is an absence, not a proof of impossibility. If T3'-grade dynamics
   ever couples the triplet to a sector with a fixed positive-definite metric, the Z2 could
   become physical through that coupling. Flagged as the one reopening route.
2. **Exhaustiveness limits.** The intertwiner/observable scans cover: all 1024 internal
   Clifford monomials, the listed K-invariant battery, V1's enumerated native algebra (cited),
   chi, `c(e4)`-type vectors, J_quat (cited from V8). NOT covered: family-tensor directions
   (35 × 256 dims of E⁻), non-monomial combinations beyond those scanned, position-dependent
   operators on an actual Y14. A family-tensor object with a canonical sign that distinguishes
   the halves would reopen the question; none is known to be native (V8: those cells are import
   territory anyway).
3. **Turok–Bateman Born-rule covariance is argued, not source-audited.** Canon's prose formula
   (project onto physical subspace, evolve, project, trace) references K only through the
   physical projector and pseudo-Hermiticity — under the joint flip `(K, Pi_phys) → (−K,
   Pi_ghost)` every ingredient co-flips and the probabilities map to themselves. If the
   primary T–B construction anchors the sign somewhere the canon prose does not record (e.g., a
   fixed choice at the initial condition), that would be initial-condition DATA — one global
   binary choice — not theory structure; still, this is from canon-prose, flagged, and a
   primary-source audit belongs to the VG-SC lane.
4. **The choice of "positive norm = physical" is itself part of the convention pair.** The
   discharge theorem says the JOINT flip is unobservable; it does not (and cannot) derive the
   convention that physical states have positive norm — that is Turok–Bateman's postulate,
   imported by canon as the quantization rule, and it is sign-covariant rather than
   sign-fixing.
5. **(14,0) not run.** The lock `P = K|_W` was verified in (9,5) and (7,7); the Riemannian
   block (where V8's grammar predicts the ghost parity coincides with the 16/16bar grading)
   was not rerun here.
6. **Nothing here touches alignment, chirality, or the count.** The physical sector remains
   96 = 3 × 2 × 16, chi-trace-achiral (canon fence intact); this route removes an import from
   the invoice but adds no dynamics and selects no 3.
