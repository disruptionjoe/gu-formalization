# Where GU stands, and the one missing object

**Date:** 2026-06-27. **Status:** capstone summary of the 2026-06-24..27 campaign. **Verdict:** GU's
reconstruction is mapped to its computational edge. It does NOT close on the existing material; it is missing
ONE precisely-specified object (the RS/IG **source action**), and the obvious ways to supply or sidestep it
have been computed and fail. This document is both the honest summary and the **spec sheet** for that object.

> Plain-English bottom line: We pushed Geometric Unity to its limit and proved, with machine-checked
> computations, that it does not finish on its own. We cornered the gap down to one missing rulebook, pinned
> exactly what that rulebook must do, and showed the existing material cannot supply it — the natural
> calculation for "three generations" gives a big messy number (-5376), not the clean 24 the story needs. GU
> is not disproven; it is precisely, honestly mapped as INCOMPLETE.

---

## A. What is honestly established (survived adversarial verification)

These are computed and re-checked, but the overall theory remains reconstruction-grade and OPEN.

- **The strongest old canon claim was WRONG and is corrected (W2-01).** The "Y14 is always spin" claim was
  found mathematically false; the truth is **Y14 is spin iff X4 (spacetime) is spin** — so X4-spin is a hard
  precondition, not automatic.
- **The shiab operator exists** as a natural real Clifford contraction in the corrected signature
  Cl(9,5)=M(64,H) — *existence only*, not uniqueness, not the selector.
- **The shiab is NOT unique and NOT the codifferential.** Equivariance leaves a multi-dimensional family;
  GU's written formula `(1,0,1,0)` is a postulate, not derived. The "which map is GU's" selector is a real
  open gap.
- **The gravitational anomaly density is computed exactly:**
  `[A-hat(TY14)]_16 = (381 p1^4 - 904 p1^2 p2 + 208 p2^2 + 512 p1 p3 - 192 p4)/464486400`, verified three
  independent ways.
- **The local anomaly does NOT Green-Schwarz factorize** (conditional negative; robust via the gravitational
  channel as long as the chiral counts differ).
- **The dark-energy sign was being computed from a bug** (a hard-coded 3 vs the real 4.229); both prior
  numbers were wrong; the data-facing sign stays OPEN.
- **The RS BV bicomplex is BUILT and verified** (s^2 = 0, non-vacuous; the "escape" is resolved via the
  Koszul-Tate/antighost leg). A real piece of machinery, machine-checked.
- **The final obstruction C2 is isolated** (= the BRST-invariance of the dynamics), and proven to be
  **global** (no local curvature/holonomy reduces it; ~94% global) AND proven to be **NOT an index** (it is a
  scale-dependent symbol-norm: `C2(2xi)/C2(xi) = 2` exactly, non-integer).
- **The honest global numbers:** `ch2(S_X)[K3] = -5376` (not 24) and `APS eta = 0` for the available operator.

A strong STRUCTURAL finding (flagged, not a theorem): the obstruction appears to be **causality-required** —
the clean "no-ghost" stabilization would decouple the RS sector and reinstate Velo-Zwanziger acausality, so
the ghost is mandatory. This unifies the RS-BRST gap with the VZ no-go, pending an independent
VZ-characteristic check.

## B. The one missing object — the SPEC SHEET (the RS/IG source action)

Everything downstream (shiab selector, generation count, dark-energy structure, anomaly closure) is gated on
ONE object GU never writes: the **stabilized RS/IG source action**. The campaign pinned its required
properties precisely enough to attempt a build:

1. **A BV action satisfying the classical master equation** `(S,S) = 0` (its own internal consistency).
2. **Its gauge-invariance FORCES the physical constraint via a Noether identity** (`delta_2 . d_RS,-1 = 0`) —
   rather than imposing the constraint by hand.
3. **It supplies a NON-EQUIVARIANT compensator** (a ghost `sigma_c` outside the Spin(9,5) symmetry family) —
   proven necessary: every equivariant attempt provably cannot close.
4. **It realizes the constraint COHOMOLOGICALLY** (the full BV bicomplex, both ghost and Koszul-Tate legs),
   NOT as a clean decoupled subspace — because a clean decoupling would be acausal (the VZ connection).
5. **It supplies three GLOBAL objects** the existing data does not:
   (i) a valid **families pushforward** / index over the non-convex metric fiber `GL(4,R)/O(3,1)`;
   (ii) the **global boundary holonomy / spectral section** of the non-compact Y14 end;
   (iii) a **BV-to-boundary-Dirac map** tying the dynamics to an actual index.
6. **It must make the matter number come out right WITHOUT importing it.** This is the sharp warning: even if
   1-5 are met, the most natural characteristic-class computation on the existing data gives **-5376, not 24**.
   So existence of the source action is necessary but NOT obviously sufficient for "three generations."

## C. The honest conditional — and what was TESTED and KILLED

**The conditional (stated honestly):** *IF* a source action exists with properties B.1-B.5, *THEN* the RS
sector stabilizes and the generation count becomes a well-posed index question — *BUT* B.6 shows even that
does not guarantee the answer is 3; the obvious route gives the wrong number. So the "if this existed, it
would all connect" feeling is a real, precisely-specified target, not a near-certainty.

**What was tested and FAILED** (so this package never oversells — these are the dead ends, with receipts):
- shiab = the codifferential — FALSE (Clifford parity).
- the obstruction = a specific commutator number (343.73) — FALSE (different object).
- selectors: gamma-trace (excludes canon), seesaw self-adjointness (vacuous/even), folded-complex closure
  (unsatisfiable), PO1 "forgetful=kernel" (identical kernels), conditional-expectation (vacuous for a trace),
  Kostant cubic Dirac (re-hits the equal-rank wall) — ALL fail.
- the record-issuance / boundary idea = a shiab selector — NO (it lands on the index, not the selector).
- the source action = "the observer's slice" = ONE global object with the index — **FORCED ANALOGY**
  (C2 is not even an index; no computable handle links them; the apparent link was a generic projection
  artifact).
- ch2 = 24 — NO (it is -5376; the lone "24" was a disguised chi-import, rejected).

Every one of these was caught by computation, several after looking very convincing in words — including one
the integrator (this author) briefly believed and had to retract. That track record is the reason the
surviving items in Section A can be trusted.

## D. What it would take, and where it goes

Closing GU from here is **not** more computation on the existing data — that frontier is exhausted. It
requires **new physics**: actually constructing the object in Section B (even Weinstein only sketched a
candidate and disclaimed it, "Caveat Emptor"). That is open-ended theoretical construction with a real chance
of going nowhere — a different kind of work from this repo's honest-reconstruction-and-audit mission.

**Recommendation:** treat THIS repo as the finished, trustworthy reconstruction + audit (the map of the edge
+ this spec sheet), and pursue the construction of the missing object as a SEPARATE research program (a new
repo) that depends on this one's spec. Keeping them separate preserves the hygiene that makes this repo
worth citing.

## Pointers (the receipts)

- Full chronological record: `DERIVATION-PROGRESS.md` — entries W2-01, SHIAB-01..06, ANOMALY-03/04,
  DARK-ENERGY-03, RFAIL-03, VZ-FCVZ4, RS-BRST, SOURCE-01..04, GHOST-01, BICOMPLEX-01, TRACK-2.
- Key syntheses: `explorations/source-action-necessary-conditions-and-causality-2026-06-27.md` (the spec's
  origin), `nonequivariant-ghost-construction-2026-06-27.md`, `bv-bicomplex-and-c2-obstruction-2026-06-27.md`,
  `c2-is-global-y14-end-data-2026-06-27.md` (with its SOURCE-04 correction banner),
  `topological-edge-c2-not-an-index-2026-06-27.md`.
- Key machine-checked tests: `tests/rs_bicomplex_spin95_connection_2form.py` (the bicomplex),
  `tests/c2_holonomy_global_obstruction.py` (C2 is global), `tests/gen_ch2_sx_from_codazzi.py` (ch2 = -5376),
  `tests/ahat_genus_y14_i16.py` (the anomaly density), `tests/shiab_family_basis.py` (the equivariant family).
- The open topological route: `active-research/topological-generation-count-families-k3-chi-gate-2026-06-26.md`.

---

## E. Update (2026-06-27): the generation-sector audit deepened (migrated from gu-source-action)

The follow-on campaign CONSTRUCT-01..07 (run in the child repo `gu-source-action`, migrated back here as
audit because it never reached construction) sharpens Part B's generation question into a precise
structural statement. Full write-up + reproducible tests:
`canon/no-go-quaternionic-parity-generation-sector.md` and `tests/generation-sector/step1..step11`.

- **The count is UNDER-DETERMINED, not impossible.** A generic rank-r carrier on the constraint surface
  gives index r (so 3 is reachable), but the rep does not FORCE the rank/index; choosing it is the
  forbidden import. GU neither predicts nor forbids three generations from its existing material.
- **A new quaternionic-parity no-go (the headline).** Every GU-native operator (the whole real Clifford
  algebra Cl(9,5)=M(64,H), including the BV/ghost/gauge-fixing apparatus) commutes with the quaternionic
  structure J_quat, so by Kramers every GU-native Hermitian carrier has an EVEN index. Hence, reading the
  count as the index, **GU's own building blocks cannot produce an odd count such as 3** -- an odd index
  requires importing a non-quaternionic (non-Clifford) object. Closed-form, not sampling.
- **C2 is not an index, now with a mechanism** (CONSTRUCT-01): any boundary Dirac whose square is the
  positive Koszul-Tate Hessian inherits an anticommuting chiral grading, forcing eta = 0.
- **The missing object is more sharply specified.** The source action S_IG must either pin the free rank
  a-priori (half-index reading) or supply the non-quaternionic structure (literal-index reading), without
  import. The honest prior remains against it; it is the one genuine construction task, retained in the
  `gu-source-action` sandbox.

Net effect on the verdict: no movement toward 3 (if anything the parity no-go hardens the literal-index
reading), but the search space collapses to a single named, forced, still-uncomputed object, and the
campaign's most defensible single claim is now the quaternionic-parity no-go.
