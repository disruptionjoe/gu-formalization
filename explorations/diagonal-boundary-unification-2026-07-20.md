---
title: "Diagonal-boundary unification swing: re-typing the class-relative no-gos as the third-person/first-person boundary -- the Lawvere no-closure parent (H62/H63) FACTORS into a diagonal leg (L1, a) and an involution leg (L2, b), and the 2026-07-20 blindness family instantiates the INVOLUTION LEG with exhibited structure maps (Kramers: derivable-instance with the (9,5)/(7,7) dissolution as the fixed-point control; selection rule, transparency/ghost/parity, operator-grade pairing: leg-(b) instances; record-sector protection: derivable at generalized group; universal-null: analogous, mechanism-match / conclusion-type mismatch) -- the planted dimension-counting no-go (C-04, prime 3) is correctly REJECTED by the instantiation certificate; cross-repo: TI holds the DIAGONAL leg (Lean-derived), TaF holds the composite first/third-person CONCLUSION, GU holds the involution leg -- three repos, three legs of one candidate theorem; unified boundary conjecture stated with first missing lemma = L1 (Branch B)"
status: active_research
doc_type: exploration
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (diagonal re-typing of the class-relative no-gos)"
claim: none
canon: none
posture: none
inputs:
  - explorations/CONJECTURE-source-action-is-the-observer-2026-07-11.md
  - explorations/path5-branchD-lawvere-no-closure-2026-07-11.md
  - explorations/H63-lawvere-payoff-first-swing-2026-07-11.md
  - explorations/H62-arena-value-partition-firmup-2026-07-11.md
  - explorations/W208-decisive-bit-lawvere-fixed-point-2026-07-14.md
  - canon/no-go-quaternionic-parity-generation-sector.md
  - explorations/araki-scale-route-2026-07-20.md
  - explorations/smatrix-sector-face-2026-07-20.md
  - explorations/operator-grade-end-2026-07-20.md
  - explorations/m1-third-reading-2026-07-20.md
  - explorations/torsor-k-sequence-2026-07-20.md
  - "READ-ONLY time-as-finality: CLAIM-LEDGER.md (T19/T92 rows), tests/T92-accessible-witness-gap-restriction.md, open-problems/first-person-finality-complexity-separation.md"
  - "READ-ONLY temporal-issuance: agent-runs/RUN-0050-expressiveness-threshold-fixture.md, agent-runs/RUN-0080-online-issuance-minimal-constructive-witness.md, agent-governance/NEXT-TRIGGER-PLAN.md (E117/E120/G1-G3 region)"
runnable:
  - tests/channel-swings/diagonal_boundary_probe.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_action: none
---

# Are the class-relative no-gos one Godelian diagonal, in the good way?

Joe's proposal, verbatim intent: the program's class-relative no-gos should
perhaps be re-typed not as boundaries of technique but as THE boundary
between third-person and first-person interpretation -- a Godelian diagonal
"in the good way." This swing tests that proposal with per-instance grading
and a planted non-instance the test must reject.

Receipt: `tests/channel-swings/diagonal_boundary_probe.py` -- deterministic
(double-run byte-identical), numpy only, seeded 20260720, exit 0 --
HEADLINE `15 [E] + 4 [F] = 19 (setup [T] = 4 excluded) ALL PASS`.

**Verdict up front.** There is one theorem-shape here, but it FACTORS, and
the honest finding is the factorization: the parent (the Lawvere no-closure
/ arena-value theorem, H62/H63) has two hypothesis legs and two conclusion
legs, and today's blindness family instantiates the INVOLUTION leg (L2 =>
conclusion (b)) with exhibited, machine-checked structure maps -- while the
DIAGONAL leg (L1 => conclusion (a)) is exhibited only in W208 GU-side, in
TI (Lean-derived), and in TaF (statement-level). The re-typing survives as
a CONJECTURE with enumerated proven instances and a named first missing
lemma; it is not yet a theorem, and one family member (universal-null) is
honestly only analogous. The planted dimension-counting no-go is correctly
rejected by the instantiation certificate (fails 2 of 5 criteria, machine
grade), so the test has teeth.

## 1. The parent shape, exact from the receipts (not paraphrased)

From `path5-branchD` (W70, machine-checked skeleton) and `H63` (W75, the
symmetry-breaking re-statement), the target theorem verbatim in structure:

> Let `(A, gamma, J, F)` be the region's graded admissibility structure:
> `A` the observer's admissibility space; `gamma : A -> B = {+,-}` the
> Krein-norm grading; `F` the firewall = the partition surface of `gamma`;
> `J` the antilinear Krein modular conjugation with `J^2 = 1`;
> `alpha : B -> B` the grading-flip `J` induces across `F`. Assume:
> - **L1 (self-encoding admissibility).** The structure is a category with
>   finite products and a diagonal `Delta : A -> A x A`; admissibility
>   predicates are exactly the maps `A -> B`; a firewall-closure is a
>   weakly point-surjective `T : A x A -> B` (the observer internally
>   representing every admissibility predicate).
> - **L2 (fixpoint-free label involution).** `alpha` is fixpoint-free (the
>   swap): `J^2 = 1`, the firewall nontrivial, no fixed boundary grade.
>
> Then: **(a) no closure** [needs L1 + L2] -- no `T` is point-surjective;
> the diagonal predicate `d = alpha . T . Delta` is unrepresented for every
> `T`; and **(b) symmetry-breaking residual** [needs L2 ALONE] -- no
> `alpha`-invariant valuation `p : A -> B` exists, so every definite
> valuation the observer commits to is a symmetry-breaking selection: the
> orientation datum is external.

Two receipts fix the reading discipline. First, H63's own grading: the
diagonal ALONE forces only a generic residual; the symmetry-breaking
character rides entirely on L2. Second -- load-bearing for this swing --
**conclusion (b) is proven from L2 without any diagonal** (W75 PART B, an
exhaustive fixed-point count). So the parent already factors in its own
receipts: a DIAGONAL leg (L1+L2 => (a)) and an INVOLUTION leg (L2 => (b)).
The mission's proposed statement ("any system with self-encoding
admissibility + a fixpoint-free involution on labels admits no internal
map computing the involution's orientation") is the CONJUNCTION; the exact
parent delivers its two halves from different hypothesis sets.

The orientation form of leg (b), which is what the instance test below
uses, is the equivariance-blindness lemma (probe T4, generic finite form):
if every map in the internal reading class is alpha-EVEN (invariant) and
the target datum is alpha-ODD (it flips), then no internal map computes
the datum; and supplying it is an alpha-breaking external selection. W208
already stamped this GU-side with the Godel signature made precise: the
grading sign is TRUE in the good model and FALSE in the pathological model
of the SAME self-consistency theory -- Godel-INDEPENDENT, "a fixpoint-free
-swap residual" -- with the self-consistency loop as the diagonal.

## 2. The instantiation certificate (the test with teeth)

A candidate no-go IS an instance of the involution leg iff all five hold,
each machine-exhibitable:

- **C1** the involution `alpha` is exhibited as an explicit structure map;
- **C2** `alpha` is fixpoint-free in the relevant sense (no fixed label /
  no fixed ray / free action);
- **C3** the EXCLUDED reading class is alpha-equivariant (even), checked
  on the fixture;
- **C4** the excluded DATUM is alpha-odd (evenness = blindness);
- **C5** supplying the external datum removes the obstruction (the
  exclusion is class-relative, not absolute).

FULL instance additionally requires the diagonal (L1): a self-referential
evaluation structure in which the no-go is the unrepresented diagonal.
DERIVABLE = instance of the involution leg plus named extra structure.
ANALOGOUS = shares mechanism or conclusion flavor, fails a criterion --
named exactly where.

## 3. The per-instance table (the family, graded one at a time)

| No-go | alpha (C1) | fixpoint-free (C2) | excluded class even (C3) | datum odd (C4) | external cure (C5) | diagonal (L1) | **GRADE** |
|---|---|---|---|---|---|---|---|
| Kramers/quaternionic parity (canon) | the Kramers pairing `v -> J_quat v`, `J^2 = -1` antiunitary | YES on rays: `<v, Jv> = 0` identically (probe E2) | J-commuting Hermitians: all-even multiplicities (E3; canon: per-generator exact) | odd signature/index is exactly what the pairing inverts (E4) | non-J import reaches rank 3 (E5; canon C-06) | absent | **DERIVABLE** (involution-leg instance + Kramers' theorem as the named transfer lemma) |
| Even/odd selection rule (Araki) | cut-swap involutions `w`, `V = c_m c_tau`: `w K_S w = -K_S`, machine-exact | YES: flips the sector label, no fixed label (E7) | every Araki-form/positive functional swap-symmetric; deck-odd part identically 0 (E8) | the datum IS the relative sign K_S-vs-cut; `k_sigma` flips (E9) | K_S-linear reference term reads it, ~ eps (E10; Araki step 5) | absent | **INSTANCE (leg b)** -- the cleanest one; "entropy is K_S-even; the sector is K_S-odd" is the lemma verbatim |
| Transparency + ghost-conjugation + parity-transfer (S-matrix) | `V = sigma2 x omega` (commutes with dynamics, anticommutes with currents); `W = I x omega` (parity transfer) | YES: V pairs every ghost channel with an opposite-grading partner | S contains no K_S at all: `(S, eps) -> (S, -eps)`; every functional of S even (E12); traced odds exactly 0 (E13) | per-channel graded content nonzero and flips (E14) | graded PREPARATION = the external orientation datum (E15); "dynamics consumes the orientation; it cannot produce it" | absent | **INSTANCE (leg b)**, doubly: two independent involutions, and parity transfer converts the bit into the same single Z/2 posit |
| Operator-grade blindness (unnamed pairing involution) | ghost-Kramers `S_VJ = (sigma2 x omega J_quat) . conj`; beyond it, the exact spectral-pairing identity | YES (antiunitary pairing; V "sufficient, never necessary") | blindness survives ALL named symmetries via the pairing identity of graded scattering | same sector datum as above | same orientation slot (B-GAUGE: classification stays Z/2) | absent | **INSTANCE (leg b)** -- and the strongest evidence the obstruction is the PAIRING itself, not any one symmetry operator |
| Record-sector protection (torsor K-sequence) | `Sp(1)_comm` action; kernels `K_S e_a` H-self-adjoint (two exact identities, 0.0 on 14 legs) | free torsor action (generalizes fixpoint-free Z/2 to a free G-action) | record current Sp(1)-INVARIANT; every one-insertion contraction blind; "conservation can locate a coset, never a map" | a torsor POINT (the map) is exactly what invariants cannot select | non-H-self-adjoint kernels respond at O(0.1); import >= 1 priced | absent | **DERIVABLE** (involution leg with Z/2 generalized to Sp(1); the coset/point gap is the residual-selection statement at group grade) |
| Universal-null lemma (m1) | conjugation swap of the complex pair `u_+ <-> u_-` | YES off the real axis | conserved pairings forced off-diagonal: each member SELF-NULL, cross-pairing carries the sign | FAILS: the excluded property is POSITIVITY of a conserved pairing, not an alpha-odd orientation output | no external Z/2 restores a positive pairing; the cure is a different accounting (both-modes), not a datum | absent | **ANALOGOUS** -- mechanism-level match (fixpoint-free pair swap kills the definite class), conclusion-type mismatch (no label object whose orientation is the excluded output). It is the SUPPLY LINE: it forces the indefiniteness that makes the sector label two-sided |
| PLANT: C-04 prime-3 dimension count | none exists | -- | -- | FAILS: `dim mod 3` is invariant under EVERY involution (F2) | FAILS: no 2^a label refinement reaches divisibility by 3 (F3) | -- | **REJECTED (non-instance)** -- correctly, by the certificate |

Count: 3 INSTANCE (leg b) + 2 DERIVABLE + 1 ANALOGOUS + plant rejected.
A majority of the family instantiates.

Two structural bonuses the table surfaces, both receipts-grade:

1. **The dissolution control is physical.** The parent predicts: give
   alpha a fixed point and the obstruction dissolves (W70: alpha = id).
   The canon Kramers no-go has EXACTLY this contingency: it holds for the
   `(9,5)`/H-class (`J^2 = -1`, fixpoint-free on rays) and DISSOLVES in
   the `(7,7)` real class (`J^2 = +1`, fixed rays exist). Probe E6 checks
   the miniature. The family's one named reopener is the parent's own
   fixed-point dial -- strong evidence of instantiation, not analogy.
2. **The "exactly" clause has a computed precedent.** The conjecture's
   sharpest clause (excluded class = EXACTLY the class computable without
   the orientation datum) is not aspirational: W105 computed the set
   equality {quantities needing J} == {two-sided ex-ante}, and the Araki
   lemma is if-and-only-if-shaped (even = blind; K_S-linear = reader).

## 4. The cross-repo faces (TaF and TI, read-only)

**TaF (T19/T92).** Exact statement shape from the ledger: on a finite
7-node T1 graph, `FIRST-PERSON-FINALITY(A*(R)) = NO` while
`THIRD-PERSON-FINALITY(G) = YES`; EXTERNAL decidable in O(|G|); INTERNAL
not in the image of ANY A*(R)-local computation ("stronger than
undecidability"); the gap is a CAUSAL-BOUNDARY obstruction (R's
self-finality witnesses sit strictly after R's observation horizon; no
increase in R's computational power bridges it). T60+T19: closure is
structurally guaranteed, but knowledge-of-closure is not self-certifiable.
T92: the gap object `G(U) = A(U) - F(U)` has conditional finite
restriction closure (a typed gap presheaf), explicitly NOT a complexity
separation and NOT a consciousness claim.

Instance test: the self-encoding leg is PRESENT at statement level (the
excluded predicate is R's verdict about R's own finality -- a genuine
diagonal; TaF's own open-problems file names the Godel lens). The
conclusion shape matches the parent's composite exactly: one
self-referential bit computable from outside, excluded for the inside
class, class-relatively (relative to A*(R)-access). What FAILS the
certificate: no fixpoint-free involution is exhibited anywhere in the TaF
receipts -- the exclusion mechanism is witness PLACEMENT (causal horizon),
not equivariance under a flip, and TaF itself insists the gap is "not a
computational undecidability." **Grade: ANALOGOUS-toward-DERIVABLE**
(diagonal leg + conclusion shape present; involution leg absent). The
missing lemma on this face is precise: exhibit an involution on the
finality label whose even/equivariant maps are exactly the
A*(R)-computable ones. If that lemma holds, T19 is a full instance; if it
provably fails, the parent has two genuinely different exclusion engines
and the unification is only leg-deep.

**TI (expressiveness threshold / E117 / RUN-0080).** The threshold is,
verbatim: "self-encoding admissibility + diagonal productive escape + no
hidden completed oracle." These are the parent's L1 + the diagonal leg,
carried as EXPLICIT named hypotheses (E117/E120 keep "diagonal
productivity and self-encoding admissibility as visible hypotheses"), and
then partially DERIVED: G1 derives diagonal productivity hypothesis-free
from `EnumeratorPresent` (`diagName_not_mem`, Lean), G2 derives
self-encoding admissibility for the concrete predicate. RUN-0080's
minimal witness class is "local constructive context + self-encoding
admissibility + diagonal/productive successor + no internally formed
future oracle." **Grade: INSTANCE OF THE HYPOTHESIS PACKAGE + conclusion
(a)** -- TI has machine-derived the DIAGONAL leg (the productive escape
from any admissible pre-committed enumeration IS the unrepresented
diagonal predicate), at theorem-prover grade, which GU's family lacks.
What TI lacks is the involution leg: no Z/2 label object, no orientation
datum; its conclusion is issuance/creation, not blindness.

**The cross-repo picture, honestly stated.** The three repos hold the
three legs of one candidate theorem, each a different two-thirds:

| Repo | L1 / diagonal (leg a) | L2 / involution (leg b) | composite conclusion |
|---|---|---|---|
| GU | W208 only (self-consistency loop); L1 = Branch B, OPEN | PROVEN, machine-exact, across 5 of 6 family members | conjectured (H63: WITHIN-REACH modulo L1) |
| TaF | present at statement level (self-finality predicate) | ABSENT (causal mechanism instead) | EXHIBITED on finite fixtures (T19/T92) |
| TI | DERIVED (Lean, G1/G2) | absent (no label object) | (a) only: productive escape |

So the unification statement is cross-repo REAL at the shape level --
but as a partition of one theorem's legs, not as three proofs of one
theorem. That is the honest form of "a Godelian diagonal in the good
way": the diagonal is proven where the physics is absent (TI), the
physics is proven where the diagonal is absent (GU family), and the
composite gap is exhibited where neither engine is formalized (TaF).

## 5. The re-typing verdict (conjecture, with its proven instances)

A majority of the blindness family instantiates the involution leg, so
the unified statement is warranted as a CONJECTURE:

> **CONJECTURE (the diagonal boundary).** The class-relative no-gos mark
> the third-person/first-person boundary: for each no-go there is an
> exhibited involution (or free group action) `alpha` on a label/value
> object such that (i) the excluded reading class is exactly the
> alpha-equivariant class -- the class computable WITHOUT the external
> orientation datum (the third-person-available readings); (ii) every
> surviving reading class is alpha-odd and CONSUMES the datum (the
> first-person selection); (iii) the obstruction dissolves exactly when
> alpha acquires a fixed point. The family is one theorem: leg (b) of
> the Lawvere no-closure parent, instantiated per sector; and the full
> parent (with L1) types the whole family as the observer's
> no-self-closure boundary.
>
> **Already-proven instances (leg b):** the Araki even/odd selection
> rule; the transparency + ghost-conjugation + parity-transfer triple;
> the operator-grade spectral-pairing blindness; Kramers/quaternionic
> parity (via Kramers' theorem, with the (9,5)/(7,7) contingency as the
> fixed-point dial); record-sector protection (at Sp(1)-generalized
> grade); W208's Godel-independence of the grading sign (with the
> diagonal). **Near-miss enumerated:** the universal-null lemma
> (mechanism-match, conclusion-type mismatch -- the supply line, not an
> instance). **Control:** the C-04 prime-3 dimension count is NOT an
> instance and the certificate rejects it.
>
> **First missing lemma: L1 (Branch B).** Assemble the per-no-go reading
> classes into one category with finite products and a diagonal in which
> "closure" is weak point-surjectivity -- the `{F_tau} <-> Sect` map's
> job, unchanged since Branch D named it. Until L1 lands, the family is
> a proven bundle of leg-(b) instances plus one full instance (W208),
> and "boundary between third- and first-person interpretation" is a
> TYPING, not a theorem. Second missing lemma (cross-repo face): the
> involution-typing of TaF's causal-horizon mechanism (Section 4).

What the conjecture does NOT claim: GU-uniqueness (H62's Curie/genericity
caveat carries verbatim); any movement of bar-b, H59, or any verdict; any
statement that the no-gos are "solved" by the re-typing -- the re-typing
changes what kind of boundary they are, not whether they bind.

## 6. Council pass (inline, five lenses)

- **Categorical logician (Lawvere/diagonal fidelity; attack sloppy
  instantiations):** the discipline held where it usually breaks: leg (b)
  does not need the diagonal, and no family member except W208 was
  credited with one. The blindness results are instances of the
  fixed-point-count Proposition (W75 B) + the equivariance-blindness
  lemma (probe T4), NOT of Lawvere's theorem proper; calling them
  "Lawvere instances" without L1 would be the sloppy move, and the doc
  types them as involution-leg instances instead. One genuine subtlety:
  Kramers' fixpoint-freeness lives on RAYS (projective, from J^2 = -1),
  the Araki/S-matrix ones on LABELS, the torsor one on a GROUP ACTION --
  three different "fixpoint-free" senses. The certificate's C2 names the
  sense per instance; a future L1 category must reconcile them (this is
  a real obligation, recorded, not waved).
- **Krein analyst (the involution identifications):** the identifications
  are the receipts' own: w and V are machine-exact swap involutions
  (Araki step 3); V = sigma2 x omega and W = I x omega are exhibited with
  0.0 defects; S_VJ extends to antiunitary grade; the Sp(1) invariance is
  two exact identities. The one identification made HERE and not in the
  sources: reading the Kramers pairing as the alpha of the parent -- it
  is defensible (projective fixpoint-freeness is exactly what J^2 = -1
  buys, and the (7,7) dissolution tracks the fixed-point dial) but it is
  this swing's contribution and should be attacked at L1 time. The
  universal-null grading as ANALOGOUS is correct: positivity is not an
  orientation datum; do not let the unification absorb it.
- **TaF-native theorist (T19/T92 fidelity):** the extraction is faithful:
  FIRST-PERSON-FINALITY(A*(R)) = NO vs THIRD-PERSON-FINALITY(G) = YES,
  causal-boundary mechanism, "stronger than undecidability," T92's
  conditional restriction closure -- all quoted, none upgraded. The
  proposed shared typing does NOT touch C1's weakened status and must
  not: the mailbox draft proposes a lemma target (involution-typing of
  the horizon mechanism), not a re-reading of TaF claims. Flag honored:
  TaF explicitly denies the gap is computational undecidability; the
  draft therefore proposes the involution as a QUESTION, not as the
  hidden truth of T19.
- **TI-native theorist (self-encoding/diagonal-productivity fidelity):**
  correctly stated: TI's threshold is the hypothesis side of the parent,
  and G1/G2 are derivations, not assumptions, as of the E120/E121 swing
  (strict c.e. tier still OPEN, correctly not claimed). The one-way
  discipline holds: nothing here imports GU's involution into TI's
  issuance chain; the draft note proposes only the typing "your diagonal
  productivity = leg (a) of the same parent," which TI already half-says
  by keeping the hypotheses visible per E117.
- **Adversarial referee (the whole exercise as retro-fitted grand
  narrative; answered in writing):** (i) Charge: any three math-adjacent
  repos will share Godel flavor; this is numerology of shapes. Answer:
  the planted control is the answer in writing -- the certificate
  REJECTED a genuine repo no-go (C-04) on machine-checked criteria (F2,
  F3), so the test does not pass everything; and the correspondences are
  exhibited structure maps with exact defects, not adjectives. (ii)
  Charge: leg (b) alone is trivial -- "invariant functionals can't read
  what the symmetry flips" is a one-line fact dressed as physics. Answer:
  conceded as mathematics, denied as typing: the CONTENT per instance is
  that the native/internal class IS the even class (transparency: a
  K_S-free construction exists and is complete scattering data -- false
  in the static theory; Kramers: the ENTIRE GU-native algebra is
  J-commuting, per-generator exact). That equality is computed per
  sector, and it is exactly the "exactly" clause of the conjecture. (iii)
  Charge: W208 already said all this; today adds nothing. Answer: W208
  typed ONE bit (the grading sign) as the Lawvere residual; today's
  result is that five further no-gos instantiate the same leg with their
  own involutions, one resists (universal-null), and the family-level
  typing has a named missing lemma -- that is a family theorem-candidate,
  not a restatement. (iv) Charge: the mailbox drafts are cross-repo claim
  movement by the back door. Answer: they are appendices, not sent, and
  propose lemma TARGETS in each repo's own vocabulary; no identity is
  asserted (tri-repo gating strict, one-way rule respected).

## 7. Receipts

- Probe: `tests/channel-swings/diagonal_boundary_probe.py` -- HEADLINE
  `15 [E] + 4 [F] = 19 (setup [T] = 4 excluded) ALL PASS`, exit 0,
  deterministic (double-run byte-identical), numpy only, seeded 20260720.
  [T] setup reproduces W70 PART A (diagonal escapes every T under swap,
  |A| <= 3 exhaustive; dissolves under id), W75 PART B (0 invariant
  valuations under swap), and the generic equivariance-blindness lemma.
  [E] the three finite/matrix-grade instantiation maps exhibited as
  explicit structure maps: Kramers (J^2 = -1, <v,Jv> = 0 at 1.6e-16,
  all-even multiplicities, rank-3 external cure, J'^2 = +1 dissolution
  control), selection rule (w K w = -K exact, even battery blind at
  3.3e-16, k-datum flips exactly, eps-tilted reference reads at 2e-3),
  transparency (unitary wall toy, [V,T] = 0 and {V,eps} = 0 exact,
  traced graded 0 at machine zero, per-channel 0.996, graded preparation
  reads). [F] the plant: C-04 reproduced, rejected at C4 (F2) and C5
  (F3), teeth check F4.
- Parent receipts: W70/W75 (exhaustive skeleton + fixed-point count);
  H63 verdict block (the two-lemma reduction, the honest ceiling); the
  CONJECTURE file's retraction section (the abstract theorem SURVIVED
  unconditionally, needing only the fixpoint-free J^2 = 1 label
  involution) and W105's set equality; W208 (the Godel signature,
  RESIDUAL-BIT-STANDS, PC1).
- Family receipts: canon C-07 + signature caveat + C-06 + C-04; Araki
  Q3 steps 1-6 + defense-attorney reframe; S-matrix Sections 3-4 +
  Section 5 twist/value distinction; operator-grade title block (Q-C
  C-BLIND STRENGTHENED TWICE); torsor Section 1 identities (i)/(ii) +
  representation-theorist council note; m1 title block (universal-null).
- Cross-repo receipts (read-only): TaF CLAIM-LEDGER T19 block
  (FIRST-PERSON = NO / THIRD-PERSON = YES, O(|G|), causal-boundary),
  T92 test spec, open-problems complexity-separation file; TI RUN-0050
  threshold definition + candidate table, RUN-0080 minimal witness
  class, NEXT-TRIGGER-PLAN E117/E120/G1-G3 entries.

## 8. Boundary

Exploration tier; claim/canon/posture: none; no external actions; no
commits; no edits to any existing file; TaF and TI touched read-only;
nothing written outside gu-formalization. Toy/matrix grade for all probe
fixtures (the probe checks the INSTANTIATION MAPS on miniatures, not the
original theorems -- those have their own receipts, cited not re-run,
except W70/W75 whose exhaustive skeleton is re-reproduced in-probe).
Named residues: (i) L1 remains the gate it has been since Branch D --
nothing here advances it; (ii) the three senses of fixpoint-free (label /
ray / free action) are certified per-instance but not yet unified in one
category; (iii) the TaF involution-typing lemma is proposed, not begun;
(iv) the universal-null lemma is deliberately left OUTSIDE the conjecture
-- if a future pass finds its positivity-exclusion is secretly an
orientation-exclusion, that is an upgrade path, not a present claim; (v)
the mailbox notes below are DRAFTS, appendices only, not sent, not
placed in system/mailboxes/.

## Appendix A. DRAFT (not sent) -- mailbox note to the TaF steward

Subject: proposed shared typing for the T19/T92 first/third-person gap
(awareness only; no claim movement requested).

GU-side result, 2026-07-20: GU's class-relative no-gos (Kramers parity,
the sector-blindness family) machine-instantiate leg (b) of the Lawvere
no-closure parent -- excluded class = the involution-equivariant
(third-person-computable-without-the-datum) readings; surviving readers
consume an external orientation datum. T19's shape
(FIRST-PERSON-FINALITY(A*(R)) = NO vs THIRD-PERSON-FINALITY(G) = YES,
exclusion relative to A*(R)-access, external witness exists) matches the
parent's composite conclusion, and T19's self-finality predicate is a
genuine diagonal. What TaF does not have in its receipts is the
involution: your mechanism is causal witness placement, and T19
explicitly is not undecidability. Proposed lemma target, in your
vocabulary, at your discretion: does there exist an involution on the
finality label object whose equivariant maps are exactly the
A*(R)-computable functionals (so that the causal horizon IS the
fixpoint-free flip, and T19 becomes a full instance)? Either answer is
informative: YES unifies the exclusion engines; NO proves the parent has
two genuinely distinct engines. No C1 movement proposed; T92's
restriction-closure result is untouched either way. Receipts:
gu-formalization explorations/diagonal-boundary-unification-2026-07-20.md
+ tests/channel-swings/diagonal_boundary_probe.py.

## Appendix B. DRAFT (not sent) -- mailbox note to the TI steward

Subject: proposed shared typing for the expressiveness threshold
(awareness only; no claim movement requested).

GU-side result, 2026-07-20: your threshold triple (self-encoding
admissibility + diagonal productive escape + no hidden completed oracle)
is, structure-for-structure, the hypothesis package of GU's Lawvere
no-closure parent (H63 L1 + the diagonal leg), and your G1/G2 Lean
derivations (diagName_not_mem from EnumeratorPresent; concrete AdmDef
self-encoding) are the only theorem-prover-grade proof of that leg
anywhere in the tri-repo system. GU has the complementary leg: the
fixpoint-free label involution and the machine-exact blindness family
(every internal reading class is involution-even; the orientation datum
is external). Proposed typing, at your discretion: register (as a note,
not a claim) that TI's diagonal productivity = leg (a) and GU's
sector-blindness family = leg (b) of one parent shape, so that a future
L1-grade unification has both legs pre-located. No TI claim movement
proposed; the strict c.e. tier stays open as you have it; one-way rule
respected (no GU physics imported into the issuance chain). Receipts: as
in Appendix A.
