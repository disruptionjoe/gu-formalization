# VERDICT LEG: the carrier-bit decision table

Companion script: `LEG-4-verdict-bookkeeping.py` (68 exact checks, ALL PASS, exit 0; sympy
rationals + exact roots of unity; 3456-combo decision-function enumeration with machine-asserted
structural invariants). This document is the human-readable table; every number in it is asserted
in the script; every quote is verbatim with source.

**What this leg decides:** under which combinations of the swing's leg outcomes the one-bit fork
(carrier A = ghost-subtracted gravitino complex, `-42 = 21*sigma/8`, order-3 classes `(0,0,0)`
vs carrier B = geometric gamma-traceless RS operator, `-38 = 19*sigma/8`, classes `(0,2,1)/3`
NONZERO) resolves A, resolves B, stays OPEN, or becomes "GU-as-stated is INCONSISTENT" -- and at
what grade, with what exact arithmetic consequences.

**The one-sentence result:** no combination of this swing's legs resolves the bit -- B tilts hard
at GU-commitments + published-theorem grade (G3) while carrier A's mechanism is machine-available
on the full field space -- and the swing's real product is that the bit is now a single well-posed
question ("which field space does the source action declare?") with a four-outcome decision table
wrapped around it, canon untouched.

---

## 1. The grade ladder (authority ordering, encoded and asserted)

| grade | meaning | who can reach it |
|---|---|---|
| G0 | arithmetic/adjudication: both carriers computed; provably cannot decide | already done (canon) |
| G1 | transcript-tier: author's spoken mechanism | already done (exploration 2026-07-10) |
| G2 | GU-commitments: the ledger of what GU-as-stated licenses | D2 |
| G3 | G2 + published-theorem hypothesis-matching + finite-model machine theorems | D1, D3-LEG-2/3/4 |
| G4 | built-action: the stabilized source action's quadratic form (SG4) | **nothing in this swing** |

Canon authority: *"which of the two is the GU generation-arena carrier is an operator-identification
question (SG4) that arithmetic provably cannot decide"* and *"Selection authority moved to SG4"*
(`canon/gamma-traceless-38-adjudication-RESULTS.md:99,87`). Machine-asserted invariant I1: **grade
G4 and canon movement occur iff SG4 is built** -- in all 3456 enumerated combos, no leg outcome of
this swing moves a canon row.

## 2. The decision table

Leg-outcome variables (from the three designs):

- **L1** (D3 LEG-1, exactify `343.73 = (6/7)*||P_-(xi (x) c(xi))||`): PASS_BOTH / PASS_ANCHOR_ONLY / FAIL
- **L2** (D3 LEG-2, Schur rigidity: no equivariant gauging coexists with the definitional
  gamma-trace constraint): PROVEN / WEAKENED / REFUTED
- **L3** (D3 LEG-3, BRST complex on the FULL field space): A42 (rolls to -42) / C44 (rolls to
  -44) / FAIL_EXACT
- **mb_closed** (D1/D3-LEG-4): massless-gauged branch closed for GU-as-stated (Grisaru-Pendleton
  hypotheses verbatim + GU's spacetime-SUSY rejection + DEAD-ENDS anti-decoupling)
- **mv_viable** (D1): massive ungauged-matter branch published-viable (VZ mass hypothesis +
  Deser-Waldron window + Buchdahl/HM Einstein-background condition, K3 inside it)
- **m_forced**: massless + interacting PROVEN forced for GU's 16 -- currently FALSE (transcript:
  "the mass is actually a variable"; capstone: mass ALLOWED)
- **vz_bites**: VZ acausality bites GU's coupled sector with NO published escape -- currently FALSE
  (DW window open; K3 is Einstein)
- **D2**: MATTER_STANDS (spin-3/2 stated matter, four independent ways) / DRAFT_SURPRISE_GAUGED
- **SG4**: UNBUILT / CONSTRAINED_NO_GAUGE / CONSTRAINED_WITH_EQ_GAUGE / FULL_GAUGED

Coherence rule (asserted): **L1 = FAIL degrades L2 to at most WEAKENED** -- the rigidity theorem's
coefficient rides the closed form.

### The named rows

| # | condition | bit | grade | canon moves | the surviving other-side case |
|---|---|---|---|---|---|
| 1 | SG4 UNBUILT + L2 PROVEN + L3 A42 + mb_closed + mv_viable + MATTER_STANDS (**max-B row; current state if D3 legs pass**) | **OPEN, B-tilt** | G3 | no | A-door: graded-IG odd invariance on the full field space (repo-derived SHAPE, unbuilt); eq 10.10 author-disclaimed |
| 2 | as row 1 but D3 legs fail (L1 FAIL / L2 WEAKENED / L3 FAIL_EXACT) | OPEN, B-tilt | **still G3** | no | tilt rides D1+D2, not D3; dichotomy register lost |
| 3 | as row 1 but the VZ mass-hypothesis PARTIAL pressed (mv_viable false) | OPEN, B-tilt | G2 | no | same A-door |
| 4 | L2 REFUTED (equivariant quotient exists) | OPEN | G2-G3 | no | **A strengthened: ghost subtraction adoptable on the STATED field space** |
| 5 | L3 = C44 (roll-up lands on the -44 control) | OPEN | as above | no | A not refuted (published -42 stands); finite-model ghost count needs the half-pairing -- new named object |
| 6 | m_forced TRUE + L2 not PROVEN | A-tilt | G3 | no | consistency pressure: massless+coupled => GP forces the supergravity structure; gauging available => A |
| 7 | m_forced TRUE + L2 PROVEN | **INCONSISTENT** | G3 | no | reopens if the 4d-effective-arena identification fails or the graded-IG door is built |
| 8 | vz_bites TRUE + L2 not PROVEN | A-tilt | G3 | no | the guardian symmetry IS the gauging |
| 9 | vz_bites TRUE + L2 PROVEN | **INCONSISTENT** | G3 | no | reopens via DW window / non-equivariant compensator / characteristic-supported gauging |
| 10 | D2 DRAFT_SURPRISE_GAUGED (primary draft states `delta psi = D eps`) | A-tilt | G2 (G3 with L3 A42) | no | SG4 still formal decider |
| 11 | SG4 = CONSTRAINED_NO_GAUGE | **B** | **G4** | **yes** | none needed -- the decider spoke |
| 12 | SG4 = FULL_GAUGED | **A** | **G4** | **yes** | none needed (if L3 was C44: named finite-model anomaly to reconcile, A still stands on published convention) |
| 13 | SG4 = CONSTRAINED_WITH_EQ_GAUGE + L2 PROVEN | **INCONSISTENT** | G4 | no | escapes the action itself could name: non-equivariant compensator; characteristic-supported gauging (rank-32 null-cone hole) |

Distribution over all 3456 combos (script S5): OPEN 780, A 1476, B 864, INCONSISTENT 336 --
and **every** B-resolution sits at G4 (864/864). The generic no-new-information outcome is OPEN.

### The current-state row (2026-07-10, verified by the script)

> bit = **OPEN** | B-tilt grade = **G3** | canon movement = **none**
> "DICHOTOMY LIVE (conditional on D3): constrained => no equivariant gauging (=> B); full+gauged =>
> BRST exists with index exactly -42 (=> A); bit = which field space SG4 declares."
> Carrier-A residual (always named): SG4 could declare the full vector-spinor field space with a
> graded-IG odd invariance (tau-descended, repo-derived SHAPE `gu_derived`, unbuilt); eq 10.10 is
> author-disclaimed.

## 3. Exact arithmetic consequences of each resolution (script S6, all asserted)

**If B resolves (only at G4):**
- Arena index -> `-38 = 19*sigma/8 = 19*p1/24`; mod-3 residue 1.
- Order-3 classes GO LIVE: `(0,2,1)/3 = 2 x class(Dirac)`; Z/24 arena `(0,8,16)`; eta-level
  `(0, +2/3, -2/3)`; `ind_phi(Q) = -2`; kernel `38 = 2h^{1,1}-2`, equivariantly `(14,12,12)`.
- Exact identity `rho_B = rho_A + 2 rho_Dirac` at every level (class, Z/24, eta -- asserted).
- A's 2-primary verdict is RE-SCOPED (A-only), not extended; the families-level Z/3 route's gate
  object (*"the fine equivariant rho of an order-3 monodromy"*,
  `canon/families-e-invariant-order3-monodromy-RESULTS.md:66-68`) becomes B's COMPUTED rho -- the
  single named escape turns into a live target.
- **Ceiling inside the ceiling:** fiberwise `-38 != 0 mod 3` is NOT a pass of the families
  criterion (probe scoping, adjudication `## What is refuted` block) -- transport needs the unbuilt
  fibered geometry. And the generation COUNT is still not forced: the carrier-mass capstone is
  carrier-independent at its grade (*"decouples to ZERO net chiral generations, not three"*,
  `canon/carrier-dirac-mass-capstone-RESULTS.md:35-36`); the count still needs the selector-side
  chiral projection GU never built. **B gives a live nonzero order-3 class, not three generations.**

**If A resolves (only at G4):**
- Arena index `-42 = 21*sigma/8 = 7*p1/8`; classes `(0,0,0)`; Z/24 `(0,0,0)`; multiplier kill
  `c_A = tr(g|T_C) - 1 = -3 == 0 mod 3` (exact roots of unity, asserted).
- The 2-primary verdict stands exactly as scoped; located-not-forced holds as before.
- The fiber-level Z/3 door CLOSES; the families conclusion *"nothing honest reaches Z/3"* hardens.
- **Named cost A must carry:** transcript [00:39:18] *"plus spinners on v, tensor spinners on w.
  So that's where you get your third generation of matter from"* must be reinterpreted -- the added
  slot becomes a gauge artifact, i.e. GU's stated third-generation mechanism is wrong-as-stated.

**If OPEN (the current state):** canon frozen; all four candidate residues stand, spanning
`(0,1,2,1)` for (A, B, bare, double); *"a zero outcome (carrier A confirmed by SG4) remains fully
live"* (adjudication:145). If L2+L3 pass, the OPEN state is SHARPER: the SG4 question reduces to
one field-space declaration.

**If INCONSISTENT:** no carrier resolves FOR GU; the adjudication table survives carrier-agnostically
(all four indices exact, asserted); the generation-arena program keeps both operators as
mathematics and reports that GU's stated commitments admit no consistent completion at the stated
grade -- with the reopening conditions named in rows 7/9/13.

## 4. The honest ceiling (mandatory)

1. **Even the max-B row is G3, not G4.** The formal decider is the quadratic form of a source
   action whose only candidate is author-disclaimed: *"may contain some inconsistencies until it is
   stabilized. Caveat Emptor"* (eq 10.10, repo-relayed at
   `explorations/vz-evasion/rs-gu-phys-brst-specification-2026-06-26.md:95-97`; receipt verdict
   `QUARANTINED_UNDERDEFINED_ZERO_ACCEPTED_RS_RECEIPTS`, :92-94). The deciding object does not
   exist in GU's own sources.
2. **The A-door is real and GU-native:** the graded-IG odd invariance upstairs -- the repo's own
   BRST spec tags the gravitino SHAPE `eps |-> D_mu eps` as `gu_derived` (:61-63) while everything
   that would make it an actual gauging is a genuine gap. A future stabilization walking through
   that door restores A with no spacetime SUSY in the conventional sense.
3. **The Lorentzian-Riemannian bridge is program semantics, not a fetched theorem:** every
   consistency no-go used is a Lorentzian propagation/quantization statement; the adjudicated
   indices are Riemannian-elliptic on K3. "Lorentzian gauged-vs-matter decides Riemannian
   ghost-subtract-vs-complete bookkeeping" is an SG4-level identification.
4. **The 343.73 fact is neutral-to-A-compatible:** the "= d^2 commutator" identification was
   KILLED in-repo (`canon/source-action-seiberg-witten-construction.md:42-43`); the machine fact
   rules out the easy subtraction *"but does not prove a ghost complex is the unique resolution"*
   (spec :117-121). Citing it as "gauging machine-refuted" would be story-shopping.
5. **Provenance gaps carried:** GP/GPvN and VZ primaries unfetched (abstract/secondary tier); the
   VZ mass hypothesis now rides TWO fetched secondaries (nLab per D1; Bekaert-Boulanger-Sundell
   arXiv:1007.0435 cached this swing: *"pathologies (such as seemingly superluminal propagation) in
   Minkowski spacetime already for massive spin-3/2 fields"*) but stays PARTIAL vs the primary.
   AGW primary paywalled; carrier-A physics attribution rides Bilal eq (11.47) + HS Remark 3.6.
   BBS also confirms the gauging escape is supergravity-shaped: *"the interactions between spin-3/2
   and electromagnetic fields in gauged supergravities are well-known to avoid the Velo-Zwanziger
   problems"* -- which cuts toward A if consistency ever forces an escape.

## 5. Verbatim anchors (single-point sources for the table)

- Adjudication table and fork: `canon/gamma-traceless-38-adjudication-RESULTS.md:51-58` (A: `T_C - 1C`,
  -42, `(0,0,0)`; B: `T_C + 1C`, -38, `(0,2,1)` NONZERO; controls -40/-44; fork `2 ind D = 4`).
- Story-shopping guard: *"treating that smell as a verdict would be story-shopping and stays
  blocked"* (:108-109); *"nothing licenses replacing -42 in canon, and nothing licenses extending
  A's 2-primary verdict to B"* (:124-125).
- Transcript (verified at file lines this session): [00:41:48] L140 *"Vela Zwanziger says that if
  you have spin three halves matter that is coupled..."*; [00:46:02] L158 *"We will never find
  space time Susie... because the mass is actually a variable"*; [00:39:18] L127-128 (the plus-sign
  product rule); [00:40:27] L131 (the flipped-chiral 16).
- PTZ (cached fetched text, re-grepped this session): *"found that it is -19 times larger than"*
  the spin-1/2 anomaly (ptz-rsa.txt:1477); the ghostless -20 +/- 1 bookkeeping (:1410-1413).
- Hack-Makedonski (cached fetched text): *"impossible as all couplings require the background to be
  an Einstein spacetime"* (hack-makedonski.txt:18) -- a background restriction, not a gauging
  requirement; K3 is Einstein.
- DEAD-ENDS firewall: bare `||[Pi_RS, M_D]|| = 58.72` never driven down (nothing in this leg
  computes dynamics at all); `343.73` identification FALSE.

## 6. What this leg blocks and what it hands to SG4

BLOCKED (correctly, forever at this grade): any leg output claiming a carrier VERDICT. The
decision function machine-enforces it: B resolves in exactly zero of the 864 SG4-unbuilt combos
(per-combo assert: every B outcome has SG4 = CONSTRAINED_NO_GAUGE).

HANDED TO SG4, sharpened: one bit = one declaration. `R = ker(Gamma)` definitional and ungauged
=> B (with the arithmetic consequences of section 3 going live). Full vector-spinor field space
with an odd invariance => A (BRST complex machine-available, index -42 by its own arithmetic,
order-3-coherent via `c_A = -3`). Constrained AND equivariantly gauged => inconsistent as declared
(escapes: non-equivariant compensator, characteristic support). Until then: OPEN, B-tilt at G3,
both steelmen intact, canon frozen.
