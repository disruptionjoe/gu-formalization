---
artifact_type: exploration
doc_type: adversarial_verification
status: "hostile verification of explorations/torsion-generation-arena-2026-07-20.md (commit b97b798); independent probe exit 0; verdict NOT-DRY (one material narrative revision, zero computational refutations)"
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (hostile verification: torsion arena)"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
target: explorations/torsion-generation-arena-2026-07-20.md
target_probe: tests/channel-swings/torsion_arena_probe.py
probe: tests/channel-swings/verify_torsion_arena_probe.py
related:
  - explorations/torsion-generation-arena-2026-07-20.md
  - explorations/wave33/H6-family-puzzle-theorem-2026-07-11.md
  - canon/no-go-quaternionic-parity-generation-sector.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
sources:
  - "Adams, J.F., On the groups J(X) IV, Topology 5 (1966): im J in pi_3^s has order den(B_2/4) = 24; cross-checked via nLab 'homotopy groups of spheres' and Wikipedia 'Homotopy groups of spheres' (pi_3^s = Z/24, Rokhlin; im J description Adams 1966 / Quillen 1971)."
  - "Milnor, J., On manifolds homeomorphic to the 7-sphere, Ann. Math. 64 (1956): for the S^3-bundle clutchings f_{h,j}(q) x = q^h x q^j, p_1(xi_{h,j}) = +-2(h-j), e = h+j; cross-checked via Crowley-Escher, A classification of S^3-bundles over S^4 (arXiv:math/0004147) and UT/Chicago expository notes."
  - "Dynkin-index additivity: the map pi_3(SU(2)) -> pi_3(U(N)) induced by a representation is multiplication by the Dynkin index (defining rep of SU(2) = 1); standard instanton-number bookkeeping."
---

# Hostile verification: the torsion generation arena (order-3 class in Z/24)

**Assignment.** Break the most consequential single claim to date: a GU-native class of ORDER
EXACTLY 3 in `Z/24 = pi_3^s`, computed from the commutant twist integer `k = +-64` on the frozen
carrier. Two asserted-but-never-checked errors were caught in other results today; the working
assumption was that this result contains one. Independent probe:
`tests/channel-swings/verify_torsion_arena_probe.py` (exit 0, 111.8 s, deterministic, seeded).

**Method separation from the original (nothing re-used).** Exact Gaussian-integer monomial
arithmetic instead of float norms; character/weight decomposition and Schur-block extraction
instead of Autonne-Takagi; Gauss-Legendre nodes with ANALYTIC derivatives instead of midpoint
quadrature with finite differences; a 4-point Milnor calibration (`p_1 = +-2(h-j)` at
`f_{0,1}, f_{1,0}, f_{1,1}, f_{1,-1}`) instead of the single `|p_1| = 2` point; a THIRD
base-leg choice for R2 plus the chirality-block decomposition; three new falsifier controls.

## Per-claim verdict table

| # | Claim (as staked) | Verdict | Receipt |
|---|---|---|---|
| 1 | `pi_3^s = Z/24 = im J` (Adams); `J(k) = k nu`; `order = 24/gcd(k,24)` | **CONFIRMED** | literature (Toda/Rokhlin; Adams 1966, Quillen 1971; H6 census table); order identity machine-verified for ALL k in 0..23 |
| 2 | `C` antisymmetric-unitary to the bit; R1 twist `k = +-64`; quadrature ratio 64, calibrated at `\|p_1\| = 2` | **CONFIRMED, strengthened** | exact integer arithmetic (antisymmetry, `C conj(C) = -I`, ALL 14 generators commute -- original sampled 4); two Autonne-Takagi-free k routes both give 64 exactly; 4-point Milnor calibration passes |
| 3 | `J(+-64) in {8 nu, 16 nu}`, nonzero, purely 3-primary, order exactly 3 | **CONFIRMED** | exact: `64 mod 24 = 16`, `-64 mod 24 = 8`, both order 3, `(mod 8, mod 3) = (0, nonzero)` |
| 4 | order-3 forced by "Kramers evenness kills Z/8" + "C-04 protects Z/3" (two walls become the mechanism) | **REVISED (material, narrative)** | C-04 leg genuine; Kramers leg MIS-ATTRIBUTED: evenness gives only `v_2 >= 1` (n = 2 gives order 12, n = 4 gives 6); the Z/8 kill is supplied by the frozen irrep H-dimension `64 = 2^6` of `M(64,H)`, a stronger and different fact than the Kramers no-go's evenness |
| 5 | carrier-independence: all five native carriers give order exactly 3 | **CONFIRMED, bounded** | re-factorized exactly (all `64m`, `{2,7,13}`-smooth); NEW control: the geometric-3 carrier `Lambda^2_+ (x) S` (m = 3, `H^192`) gives the ZERO class -- independence is conditional on C-04's rep-vs-geometric fence |
| 6 | R0 and R2 wind zero; metric sector alone cannot reach the arena | **CONFIRMED, strengthened** | R0 = `f_{1,1}` is stably trivial by Milnor's `p_1 = +-2(h-j)` (theory anchor, not just quadrature); R2 re-run on a THIRD disjoint leg choice (11,4,5,6): winding 0; chirality blocks wind exactly -+32 and +32 -- cancellation is representation-forced, not leg-accidental |
| 7 | missing datum = one Sp(1)-torsor identification; MERGES with B.5/Element-1; zero new imports | **REVISED (non-fatal)** | accounting defensible (torsor part merges; framed-reading part rides the existing flagged fork; net-new 0 stands) BUT the "Z/2 shadow already verified" support is rep-weight-blind: the co-flip matches ANY rep containing -1, while the VALUE k = 64 (hence order 3, not 24/12/6) requires the twist to act in the FULL carrier rep (new control: defining rep gives order 24; k = 2 gives 12; k = 4 gives 6) |
| 8 | "count = ORDER of the class" is the only well-typed nontrivial reading; dictionary gate stays OPEN | **REVISED (minor)** | element-3 and residue-3 rejections confirmed; order and subgroup-cardinality coincide (both 3); but the subgroup-INDEX reading (= 8) is well-typed, nontrivial, and unenumerated -- "only" is overstated; gate-OPEN typing verified clean everywhere (no sentence claims 3 families) |

## A. The +-64 provenance (highest-value target): CONFIRMED by two independent routes

**Route #1 -- character/weights (no Autonne-Takagi, no quadrature, exact).** The complexified
commutant family is verified to be a genuine Sp(1) action (homomorphism residual 5.6e-17). Its
maximal-torus weights on the 256-dim complexification, along a GENERIC random torus direction,
are `(+1) x 128, (-1) x 128, (0) x 0` -- so the representation is exactly 128 copies of the
defining rep `V_2`, with NO trivial or higher summands. By Dynkin-index additivity the winding
is `128 x 1 = +-128`; Bott's `c = x2` gives `k = +-64`. This is basis-free: `k` equals the
complex dimension of the carrier over 2, i.e. the H-multiplicity, an invariant of the module --
no normalization or convention in the choice of `C` can move it.

**Route #2 -- Schur-block extraction (Youla-style, not Autonne-Takagi).** An exact spectral
projector pulls a vector from the weight-(+1) space of the ACTUAL 256-dim family; the 2-dim
subspace it generates is verified invariant under the whole Sp(1) action (residual 1.2e-15),
and its restricted winding, quadrature-measured, is -1.0000 exactly. 128 identical blocks
`=> k = +-64`.

**Independent engine + wider calibration.** My quadrature uses Gauss-Legendre nodes and
analytic derivatives (the original: midpoint + finite differences). Control values land exact:
id map +1.00000; 1-quaternion control -2.0000; direct 256-dim ratio 64.000. The Milnor 4-point
calibration -- a control family the original never ran -- passes on all four points including
the NEW `|p_1| = 4` target (`f_{1,-1}`, the ad-Hopf bundle): `f01 = +2.000, f10 = -2.000,
f11 = +0.000, f1m1 = -4.000`, exactly the `p_1 = +-2(h-j)` line. Two independent routes agree
with the original: **the result does not die here. k = +-64 stands.**

## B. The stable-homotopy dictionary audit

The imported chain checks out in the literature: `pi_3^s = Z/24` (Rokhlin; Toda), `im J` is the
whole group with `|im J| = den(B_2/4) = 24` (Adams 1966, completed by Quillen 1971), order
arithmetic trivial and machine-verified. The identification the original actually makes is
honest and is the right one to audit: it does NOT claim the commutant family IS a framing
twist; it computes what the class WOULD be, and names the identification as the demand
(outcome shape ii). The Pontryagin-Thom sentence it imports ("a twist `f : S^3 -> SO(N)`
shifts the framed class by `J([f])`") is standard and correctly scoped; the commutant action
is real-orthogonal on `R^256`, so it is `SO(N)`-valued as required.

**Where the demand does MORE work than the merge sentence admits.** The demanded datum bundles
two separable identifications: (i) the Sp(1)-torsor structure on the S^3 cover (this is the
part that merges with B.5/Element-1, and any torsor identification is degree +-1, so it cannot
change `|k|`); and (ii) the framed reading in which the CARRIER transport acts on the stable
framing. The rep-weight sensitivity control makes (ii) load-bearing for the headline number:
a framing twisted through the defining rep gives order 24, through a `k = 2` rep order 12,
through `k = 4` order 6. Only the full 256-dim carrier rep gives 3. The machine-verified Z/2
shadow cannot distinguish any of these (every candidate rep contains -1), so the co-flip
verification supports the torsor half only -- thinner inductive support than the original's
"the pi_1 shadow of the demand is already a theorem of the fixtures" suggests, though the
demand's own wording ("transporting the frozen carrier... whose induced twist is the commutant
action") does pin (ii). N-accounting verdict: zero-new stands; the strengthening is bigger
than one homotopy level.

## C. The reverse-obstruction argument: the material finding

The arithmetic is impeccable; the ATTRIBUTION is not. The original's Section 2 leg 1 states
"the quaternionic evenness of every native carrier... forces `v_2(multiplicity) >= 3`". False
as a statement about evenness: Kramers/quaternionic evenness supplies `v_2 >= 1`, and the
probe shows H-multiplicity 2 gives order 12, multiplicity 4 gives order 6 -- quaternionic,
Kramers-even, and NOT order 3. The original's own falsifier control (n = 4 -> 6) already
demonstrates this and sits in tension with its own prose. What actually kills the Z/8 part is
`64 = 2^6 | k`, i.e. the frozen irreducible module of `M(64,H)` has H-dimension 64, so every
carrier is `H^{64m}`. Same frozen object (the verified `Cl(9,5) = M(64,H)`), different and
much stronger fact than the evenness that powers the Kramers no-go. The marquee line "the two
established obstructions jointly BECOME the purity mechanism" is therefore half-wrong: the
C-04 leg (3 absent from `{2,7,13}`; verified against the actual C-04 statement, canon line 95,
and re-factorized across all five carriers including `5824 = 2^6 x 7 x 13`) genuinely works in
reverse; the 2-primary leg is powered by the irrep dimension, not by the Kramers wall. The
computed order 3 is untouched; the mechanism NARRATIVE needs one sentence rewritten.

## D. R0/R2 zeroes: genuine, now over-determined

Third disjoint leg choice (11,4,5,6): unitary, deck monodromy `-I` exact, Ad reproduces the
native family, winding -0.0000. The chirality decomposition shows WHY: `omega` commutes with
the whole family, splits 64/64, and the block windings are -32.000 / +32.000 -- exact
both-chirality cancellation, representation-forced. Independently, R0 `= f_{1,1}` is stably
trivial by Milnor's table (`p_1 propto h - j`), so the zero is a theorem, not a measurement
artifact. The original's "TS^4 pattern" sentence is correct as written.

## E. The merge claim: audited in Section B above -- zero-new stands, support graded down one notch.

## F/G. Readings and H6 consistency

The gate is typed OPEN everywhere (frontmatter, Sections 0, 3, 7; no sentence claims three
families as a cardinality). H6's receipt, read in full, permits exactly this: its census row
lists the Adams e-invariant / J-homomorphism as the 3-primary-reaching selector with value
group `Z/24`, and its limits (a) mod-3-not-parity and (b) order-3-class -> integer-3 OPEN are
quoted accurately by the original. One gap in the reading analysis: the subgroup-INDEX reading
(`[Z/24 : <J(k)>] = 8`) is well-typed and nontrivial and was not enumerated; "the only
well-typed nontrivial reading" should be "the only well-typed nontrivial reading among those
with any precedent" -- immaterial while the gate stays open, but the rhetoric overshoots.

## Verdict

**NOT-DRY.** Material list (one item):

- **M1 (claim 4, Section 2 leg 1 and the frontmatter's "the SAME quaternionic evenness that
  powers the Kramers no-go"):** the 2-primary kill is not Kramers evenness working in reverse;
  it is the frozen irrep H-dimension `64 = 2^6`. Evenness alone permits orders 12 and 6. The
  fix is one sentence ("8 | k because every `M(64,H)`-module has H-dimension `64m`"), and
  nothing downstream moves -- but as written the mechanism attribution is an
  asserted-but-never-checked error of exactly the class this pass was hunting.

Non-material notes for the next revision: the Z/2-shadow support for the merged demand is
rep-weight-blind (Section B); carrier-independence is bounded by the C-04 rep/geometric fence
(the m = 3 geometric carrier `H^192` gives the zero class); the reading enumeration misses the
index-8 reading. Everything computational -- `k = +-64` by two independent routes, order
exactly 3, all five carriers, R0 = R2 = 0 structurally, the falsifier controls, the H6 and
literature imports -- **survives hostile re-derivation bit-for-bit.** The conditional result
as typed (exploration, R0_COND, gate OPEN, no canon movement) stands.

**Receipts.** `tests/channel-swings/verify_torsion_arena_probe.py`: 26 checks, ALL PASS,
exit 0, 111.8 s. HEADLINE: k = +-64 CONFIRMED by two Autonne-Takagi-free routes; Milnor
4-point calibration passes; R0/R2 zeroes structural; order-3 arithmetic confirmed; NEW
controls bound the claim (frozen `2^6`, rep-native ledger, full-carrier rep-weight).
