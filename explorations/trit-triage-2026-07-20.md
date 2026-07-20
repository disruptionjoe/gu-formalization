---
title: "Trit-interpretation triage -- fast discriminating check on each of the five candidate readings of the Z/3, with per-candidate grades and the LEAD's next swing"
status: active_research
doc_type: triage
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (trit-interpretation triage)"
axiom: lab/process/boundary-adapter-standing-axiom.md
lane: 1
channel: TRIT-INTERPRETATION
provenance_grade: triage (cheapest discriminating check per candidate; asserts nothing beyond the receipts + the frozen Z/6 fact)
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Trit-interpretation triage

Probe: `tests/channel-swings/trit_triage_probe.py` (deterministic, exit 0,
5 [E] + 5 [F] = 10 checks, ~10 s). Spec:
`explorations/trit-interpretation-candidates-2026-07-20.md` (8c7b21b).

## The bound (stated honestly)

The heavy Z/6-forcing certifiers (`conditional_forcing_probe.py`,
`trit_internal_check_probe.py`) each run > 2 min foreground; at triage grade
their frozen receipts (f513fcf, 0314958) are CITED, not re-run. The two LIGHT
load-bearing probes that actually carry the discriminators are imported live
and clean: `n4_two_z3s_probe.py` (the trit character) and
`l1_assembly_probe.py` (the boundary group G). The number-theoretic
discriminators (Olum r^2 mod 3, coprimality, roots of unity) are recomputed
directly. P2C is READ-ONLY and NOT run: its access-layer shape is extracted
structurally from SYNTHESIS.md + `tests/indexed_restriction_diagram.py` and
encoded as constants.

## The five grades (one line of evidence each)

1. **ROLE-ROTATION (Joe's orthodox rescue) -- RIDICULOUS.** The trit's Z/3
   carries NO preferred cycle orientation: the two admissible N4 characters
   differ by exactly complex conjugation (chi_D(a1)=omega, chi_B(a1)=omega^2,
   defect 7e-16 = orientation reversal) and BOTH orderings are admissible, so
   the frozen structure declares no chirality; Olum r^2 = 1 mod 3 for both
   generators makes the count orientation-blind. Symmetric -> folds to mundane
   phase.
2. **{WORLD, ACCESS, STANDPOINT} vs G -- RIDICULOUS (MISMATCH).** G's three
   graded pieces are a Z/2 x Sp(1) structure (coset order exactly 2; antilinear
   part order 4 Kramers; kernel the linear Sp(1)) with NO native Z/3; the 2+1
   linearity coloring (lin, lin, anti) admits no orientation-3 cyclic
   permutation (a 3-cycle is fixed-point-free but automorphisms fix the sole
   antilinear piece). The boundary law is a TWO; the trit is a THREE. As
   stated, a category error.
3. **THREE-PHASE OBSERVER CLOCK -- VIABLE-DATA-BLOCKED.** The only order-3
   element in the frozen family-preserving structure is the commutant scalar
   omega*I, a global phase that fixes every ray (projectively trivial);
   U_h is order 2, the antilinear part order 4. A genuine clock needs a
   three-cyclic signature in mass/mixing data the frozen inventory cannot
   supply. Coherent, not refuted, parked on data (not fabricated).
4. **MUNDANE PHASE / null -- RIDICULOUS (DEFEATED).** Coprimality exact: the
   bit generates only {1,-1} (proper order-2 subgroup), the trit is not any
   power of the bit, |<bit>|*|<trit>| = 6 = |Z/6| (Z/6 = Z/2 x Z/3). The Z/3
   is irreducible to the bit -- "means nothing" is false; the trit is a genuine
   third irreducible datum, exactly the positive fact 2/5 rely on.
5. **ACCESS AS THE IRREDUCIBLE THIRD / P2C -- LEAD (weakened).** P2C's COMPUTED
   indexed diagram is a two-fiber (N/S) cospan into one envelope (arity 2 != 3);
   only P2C's plain-English prose reaches THREE (global / from-here /
   from-here-under-budget = world / accessible-region / standpoint). So the
   arities are compatible in COUNT (3=3) but that triple is a NESTED CHAIN
   (Aut = order 1), while the trit is a cyclic Z/3 (order-3 rotation). Still the
   LEAD: it alone owns a sharp cheap decisive cross-repo test.

## The regrade of Joe's originating idea (truth over deference)

Joe's three-capability-spaces idea, and its orthodox role-rotation rescue
(candidate 1), does **not survive as stated**: the discriminator it was given
-- a preferred cycle orientation encoding whose-frame-reads-whom -- is provably
ABSENT. The canonical Z/3 is conjugation-symmetric (both N4 orderings
admissible) and Olum-blind, so there is no computable direction to rotate.

The honest residue is precise and worth carrying: the trit is an **UNDIRECTED
3-cycle** -- a genuine, coprime, irreducible Z/3 (candidate 4's defeat) with no
chirality (candidate 1's symmetry). An undirected 3-cycle is exactly the shape
a 3-CHAIN takes when it CLOSES into a cycle without acquiring a preferred
direction. Both places the personas expected the triple to live -- G's L1
grading (candidate 2) and P2C's access prose (candidate 5) -- present it as a
CHAIN / NESTING, never a native cycle. So the triage's real finding is unified:
**every structural home for the triple is a nesting; the trit's cyclicity is,
so far, unexplained by any of them.** The one surviving way for a candidate to
win is for the trit's (unoriented) Z/3 to be the cyclic CLOSURE of one of those
3-chains.

## Recommended bigger-swing target for the hourly

Advance **candidate 5** only, with a sharpened, pre-registerable test that
respects the arity finding:

> Is the trit's canonical (unoriented) Z/3 exactly the cyclic CLOSURE of P2C's
> nested 3-question chain {world >= access >= standpoint}? Concretely: does the
> restriction partial order (global -> from-here -> from-here-under-budget)
> admit a natural order-3 identification (a "wrap" sending standpoint back to
> world) that (a) is conjugation-symmetric (matching the trit's lack of
> chirality) and (b) reproduces the trit's cube-root sector structure -- with a
> planted DIRECTED-chain control that must FAIL because it has no undirected
> closure.

This is the pre-registered "bigger swing" the spec flagged; the triage only
verified the arities are count-compatible (3=3) and structure-incompatible
(cycle vs chain), so the swing is NOT green-lit as a match -- it is green-lit as
the one cheap decisive test worth running. Do NOT run the full element-for-
element match inside triage (pre-registered separately).

## Five-lens council (short, inline)

- **Standard-field theorist:** grades stand. The orientation/Olum result (1)
  and the coprimality/CRT result (4) are textbook and airtight; (2) is a clean
  representation-type obstruction. No standard-field move rescues 1 or 2.
- **Program-native (TaF/finality):** endorses parking (3) rather than forcing;
  the observer-clock reading is the only one whose evidence is genuinely
  downstream of uncomputable data, so DATA-BLOCKED is the honest grade, not a
  demotion.
- **Category theorist:** the decisive through-line is arity+automorphism: a
  Z/2 grading, a total-order chain, and a cospan all fail to carry Z/3 for the
  same reason (wrong automorphism group). The LEAD's next test is correctly a
  CLOSURE question, not a match question.
- **Skeptic / kill-attorney:** willing to zero the whole channel -- but the
  coprimality floor (4) is a real positive datum, so the field does not
  collapse to "nothing"; it collapses to "one cyclic-closure question." That is
  a demotion of four candidates, not a channel kill.
- **Philosopher:** the reframe is honest and stronger than the original: the
  trit is a THIRD (irreducible, 4) that is a CYCLE (undirected, 1), and every
  proposed home is a NESTING -- so the open problem is sharpened to "what closes
  the nesting," which is more explanatory than any single surviving candidate.

## Receipts

- `tests/channel-swings/trit_triage_probe.py` -- exit 0; 5 [E] + 5 [F] = 10 all
  pass; ~10 s; HEADLINE carries the five grades.
- Imports clean: `n4_two_z3s_probe.py` (exit 0), `l1_assembly_probe.py`
  (exit 0). Heavy certifiers cited: f513fcf (conditional forcing), 0314958
  (trit-internal K-a), 56304e8 (boundary law).
- P2C read-only extraction: `possibility-to-capability/explorations/
  2026-07-19-indexed-restriction-diagram/SYNTHESIS.md` and
  `tests/indexed_restriction_diagram.py` (arity constants: 2 fibers, 6-rung
  chain, 3 nested prose questions).

## Boundary

Triage of a fixture-grade interpretation problem. Asserts nothing beyond the
cited receipts and the frozen Z/6 fact. No claim/canon/posture movement.
Grades are triage verdicts, not resolutions: candidate 5 (LEAD, weakened) is
the sole advance; 1, 2, 4 are demoted by their discriminators; 3 is parked on
data.
