---
artifact_type: exploration
status: exploration
created: 2026-07-07
title: "BIG SWING (framed-bordism carrier, 2026-07-07 synthesis) -- PROMOTE-OR-KILL on conjecture D. HONEST OUTCOME: STILL-GATED, dramatically sharpened. The swing attacked the ONE remaining located-not-forced carrier: the framed-bordism object of paper Section 9. Four legs (F1-F4), each with two independent verifier passes folded in (verdicts WIN). RESULT: three of the conjecture's branches are KILLED and the class-as-count category error is CONFIRMED one level up from Hom(Z/3,Z)=0 -- but conjecture D as Section 9 actually states it (the relative/equivariant twisted-RS index) is NOT killed, because that object is integer-BY-CONSTRUCTION and structurally invisible to every e-invariant / homomorphism obstruction deployed. (1) F1 [KILL, both verifiers SUSTAINED]: the twisted Dirac operator BUILT on the GU-forced RP^3=L(2;1) spine with the Lambda^2_+ framing; every GU-admissible flat twist eta is 2-adic (deck group Z/2 coprime to 3), so v_3(APS index) is FIXED at -1 and the Z/3 component is frozen at 2/3 -- never an integer. The L(3;1) deck-Z/3 control DOES integerize, proving the block is the deck-group order 2, not a construction failure. This converts RS-S4's GATED to KILL on the constructive-on-carrier branch. (2) F2 [GATED, both SUSTAINED]: e_R=1/12 provably has NO integer PREIMAGE (Hom(Z/3,Z)=Hom(Z/24,Z)=Hom(Q/Z,Z)=0, enumerated) -- the category error confirmed at the FULL framed-bordism level, strictly containing the paper's base case. BUT 'no integer index has fractional part e_R' is FALSE: a relative APS index bulk - e_R = integer is not precluded; the obstruction flags torsion classes ONLY, and integer-by-construction indices escape it (signature/Euler/relative-APS controls pass). (3) F3 [GATED; one verifier SUSTAINED, one PARTIAL downgrading two component-leg labels from THEOREM to tautological/circular, route verdict intact]: reachability trichotomy -- the Z/3 summand IS reached by the carrier but ONLY as the fraction 1/3; every INTEGER that reaches Z/3 is external (3|m AND 3|sigma) or the unbuilt relative index; NO carrier-native sector-constructible integer has nonzero Z/3 content. (4) F4 [KILL, both SUSTAINED]: the two surviving external imports (3|m cubic coupling, 3|sigma signature) are FREE choices -- not forced by anomaly cancellation, Dai-Freed (SM mod-3 arena empty), or modular invariance -- so 'forced' is reachable only through a free import. ADJUDICATION: no twisted index on the located carrier gives an integer in Z/3 (F1 KILL, F3 KILL sub-finding, RS-S2), and e_R=1/12 is provably without an integer-CLASS preimage (F2). But the object conjecture D actually names -- the relative/equivariant twisted-RS index with nonzero geometry-dependent bulk, whose FRACTIONAL PART (not class) is e_R -- is integer-by-construction, escapes the obstruction (F2), and once built reduces mod 3 to the two free imports (F4). It is still UNBUILT. COUNT VERDICT: STILL-GATED (OPEN); the carrier-enumeration frontier is effectively EXHAUSTED (cohomology Z/2 wall + framed-bordism Z/24 wall both closed; constructive-on-carrier and import-forcing branches killed), leaving not another carrier but a single unbuilt OPERATOR-gate that is a source-action geometry question, not a topology question. This is a PROPOSAL for Section 9 that pauses for the maintainer; the frozen paper is not touched."
grade: "synthesis (exploration). Component grades folded with verifier verdicts winning: F1 = KILL of the constructive-on-carrier branch (both verifier passes SUSTAINED); F2 = GATED with a THEOREM-grade class-as-count obstruction sub-result (both SUSTAINED); F3 = GATED (one SUSTAINED, one PARTIAL that reproduced every number and sustained the GATED route verdict but correctly downgraded two component legs -- the mod-3 reduction leg is a tautology, the p1=4 'two independent normalizations' cross-check is arithmetically circular -- neither load-bearing to GATED); F4 = KILL of the external-import-forcing branch (both SUSTAINED). NET conjecture-D verdict: STILL-GATED, because the two routes that bear on conjecture D AS A WHOLE (F2, F3) return GATED, while the two KILLs (F1, F4) close specific BRANCHES, not the conjecture. The category-error confirmation (Hom(Q/Z,Z)=0, one level up) is theorem-grade and sustained. FROM-MEMORY inputs inherited from the legs and honestly flagged: Kirby-Melvin p1=4 framing normalization (cross-check is circular per F3 PARTIAL, so the exact value e_R=1/12 is from-memory-anchored, though fractionality itself is robust to the class); |Im J_3|=denom(B_2/4)=24 (Bernoulli, machine-derived, provenance-distinct from chi(K3)=24); Rokhlin 16|sigma; K3 sigma=-16; no 4D pure gravitational anomaly; Garcia-Etxebarria-Montero Z_9->3Z; the APS identity ind=bulk-eta_defect (statement standard, application to GU's operator is the unbuilt gate). TARGET-IMPORT GUARD sustained across all four legs at maximum strictness by both verifier lanes: no element of {3,8,24,chi(K3)=24,Ahat=3,rank_H=4,ind_H=8} inserted, hardcoded, or divided-by; every 3 measured with printed provenance. e-INVARIANT / Hom(Z/3,Z)=0 discipline held throughout: e_R kept Q/Z-valued, never identified with an integer; the only integers exhibited (closed AS index; relative APS index) are integer-by-construction and proven 3-inert or import-carried. Internal tier: computed + self-adversarial across four legs and eight verifier passes, not externally replicated or peer-reviewed."
depends_on:
  - papers/candidates/located-not-forced/located-not-forced-generation-count-2026-06-29.md
  - canon/h2-base-index-chirality.md
  - explorations/big-swing-2026-07-07/RS-S4-base-forcing-bismut-cheeger.md
  - explorations/big-swing-2026-07-07/RS-S2-relative-index-nogo.md
  - explorations/big-swing-2026-07-07/FB-F1-twisted-operator-build.md
  - explorations/big-swing-2026-07-07/FB-F2-adams-einvariant-obstruction.md
  - explorations/big-swing-2026-07-07/FB-F3-crt-split-on-carrier.md
  - explorations/big-swing-2026-07-07/FB-F4-imageofJ-fractional-and-imports.md
scripts:
  - tests/big-swing/fb_f1_twisted_operator_build.py
  - tests/big-swing/fb_f2_adams_einvariant_obstruction.py
  - tests/big-swing/fb_f3_crt_split_on_carrier.py
  - tests/big-swing/fb_f4_imageofJ_fractional_and_imports.py
---

# Big swing (framed-bordism carrier): PROMOTE-OR-KILL on conjecture D

**Honest outcome: STILL-GATED, dramatically sharpened.** Three branches of the conjecture are KILLED and
the class-as-count category error is CONFIRMED one level up -- but conjecture D as Section 9 actually
states it survives on a single unbuilt object that is integer-by-construction and structurally invisible
to every obstruction this swing deployed.

---

## The swing

The RS-index swing (2026-07-07) closed the native-construction escape four ways and narrowed the
located-not-forced generation count to **one remaining carrier**: the paper's Section 9 / conjecture-D
**framed-bordism** object. The GU-forced `RP^3 = L(2;1)` spine, with its self-dual `Lambda^2_+` tangential
framing, escapes the 2-adic cohomology wall (`H^2(RP^3; Z) = Z/2`) into **framed bordism**
`pi_3^s = Z/24 = Z/8 (+) Z/3` (CRT). The generation count, *if* homotopy-theoretic, would live in the
`Z/3` summand, read by the Adams `e`-invariant via the image of `J`, with `e_R = 1/12`. RS-S4 computed the
untwisted transparent-fiber APS index `= -1/12` (fractional) and stopped **GATED** because the twisted
operator was never built.

**The decisive question.** Does a twisted-RS/Dirac operator on this framed-bordism carrier give an
**INTEGER** in the `Z/3` summand -- or is `e_R = 1/12` provably **WITHOUT** an integer index preimage (a
confirmed category error, one level up from `Hom(Z/3, Z) = 0`)?

Four legs attacked it, each with two independent verifier passes. **Verdicts win** in what follows.

---

## Per-route summaries (verifier verdicts folded in)

### F1 -- BUILD the twisted operator on the located carrier. Verdict: **KILL** (of the constructive-on-carrier branch). Both verifier passes **SUSTAINED**.

The object RS-S4 left unbuilt is now built. On `L(2;1)` with the self-dual framing, the twisted Dirac
reduced `eta` (APS/Donnelly spectral sum) was computed for **every** GU-admissible flat twist: the deck-group
`Z/2` lines, the flat `SU(2)+` family bundles, and the self-dual `Lambda^2_+` adjoint.

- **Measured result.** Every twist `eta_E` is **2-adic** (`v_3(den) = 0`), because `pi_1(L(2;1)) = Z/2` is
  coprime to 3. The built `xi_a = (-1/8, +1/8)`, sum 0. Hence the twisted APS eta-index
  `I(E) = bulk(0) - (e_R + eta_E)` has **`v_3(I) = -1` fixed for every twist** -- never an integer -- and its
  `Z/3` component is **frozen at `2/3`** across all six enumerated twists. The `Z/2` deck acts only on the
  2-primary sector and cannot manufacture, cancel, or integerize the `Z/3` content of `e_R`.
- **Discriminating control (the mechanism exists, on the wrong carrier).** The identical machinery on
  `L(3;1)` (deck `Z/3`, which GU does **not** force) gives `xi_a = (-2/9, +1/9, +1/9)` (3-adic) and **does**
  integerize: framing `1/3` + twist `2/3` `= 1` in `Z`. The obstruction on `L(2;1)` is precisely the
  **deck-group order 2**, not a failure of construction.
- **Scrambled control.** 2000 random 2-adic twists: zero integerize `-1/12`.

**What both verifiers add.** Angle A (refute the computation) failed to refute: an independent recompute of
the APS/Donnelly `xi` matched, and a brute-force scan of all flat `Z/2` twists `n1 * (1/4)`, `n1` in
`[-1000, 1000]`, gave zero integerizations -- the KILL is *airtight for flat twists* because the ultrametric
`min(-1, >=0) = -1` is sharp (valuations differ, no cancellation). Angle B (import auditor) confirmed no
forbidden target inserted, no category error committed (`e_R` held `Q/Z`-valued; the only integer, the closed
AS index, is proven 3-inert via `m^2 == 1 mod 3`), and the `L(2;1)=Z/2` vs `L(3;1)=Z/3` distinction is
load-bearing. One honest, disclosed scope: the KILL is of **carrier-routed flat** twists; a non-flat bulk
relative index over a 4-manifold `W` with `dW = L(2;1)` could carry 3-adic content, but only from external
`sigma`/`d'` (RS-S2), disjoint from `e_R`.

> **F1 converts RS-S4's GATED to KILL on the exact branch it left open**: no built operator on the located
> carrier can integerize `e_R`, for a structural (deck-order / p-adic) reason.

### F2 -- the Adams e-invariant OBSTRUCTION. Verdict: **GATED**, carrying a **THEOREM-grade** class-as-count sub-result. Both verifier passes **SUSTAINED**.

- **Proven (theorem-grade).** `Hom(Z/3, Z) = Hom(Z/24, Z) = Hom(Z/8, Z) = Hom(Z/12, Z) = Hom(Q/Z, Z) = 0`,
  all enumerated. The `e`-invariant *class* -- an element of `Im J = Z/24`, torsion in `Q/Z` -- has **no
  integer preimage under any homomorphism**. "generation count = `e`-invariant class" is a **confirmed
  category error, one level up** from the paper's `Hom(Z/3, Z) = 0`, strictly containing it. Fractionality is
  *proved not asserted*: `e_R = 1/12` has computed order 12 in `Q/Z` (3-adic valuation of the order = 1), and
  its 3-primary component is `1/3` (order 3, nonzero) by two agreeing computations.
- **Why KILL is not reached (the crux).** Two different statements: **(A)** "`e_R` has no integer PREIMAGE"
  is **TRUE** (theorem). **(B)** "no integer index has fractional part `e_R`" is **FALSE** -- in the APS
  identity `ind = bulk - eta_defect`, `ind` is an integer *by construction* and the bulk can be any
  `n + e_R`, giving `ind = n`. The residue fixes `ind` mod 1 only; it neither forces 3 nor precludes an
  integer. A discriminating `is_obstructed` test flags torsion (`e_R`, `1/3`, `Z/24`, `Z/3`, `Z/8`) and does
  **not** flag the signature, Euler number, or **relative APS index** (integers by construction) -- the
  task-mandated control passes.

**What both verifiers add.** Angle A sustained fractionality and the CRT derivation, and flagged honest
control-hygiene defects that do not touch GATED: F1's RNG is unseeded (a probabilistic sanity control can
flake to exit 1 -- reproducibility note on the sibling leg), F2's scramble control is near-tautological
(`is_obstructed('integer_index', x)` ignores `x`), and the "two independent normalizations" of `e_R` are
both from-memory (agree by construction). Angle B confirmed the category-error discipline is respected: the
route proves the class *cannot* be an integer, and the only surviving integer (the relative index) is
explicitly declared *not* the e-invariant.

> **F2 makes the category error universal at the topology level** -- for any framing, any representative in
> `Im J` -- but proves that an integer-by-construction *relative* index structurally escapes it. The route is
> GATED, and the surviving object is named exactly.

### F3 -- the CRT `Z/8 (+) Z/3` split read on the actual carrier. Verdict: **GATED** (reachability trichotomy). One verifier **SUSTAINED**; one **PARTIAL** (route verdict intact, two component-leg labels downgraded).

Via an explicit, roundtrip-validated CRT iso `Z/24 -> Z/8 x Z/3` (24 factored by sympy, idempotents
`e8 = 9`, `e3 = 16`, bijective over all 24 classes):

| object | `Z/3`-reach | integer? | through the carrier? |
| --- | --- | --- | --- |
| fractional `e`-invariant `e_R = 1/12` | `1/3` (NONZERO) | **no** (`Hom(Z/3,Z)=0`) | yes (the carrier) |
| signed sector index (achirality `{K,chi}=0`) | `0` | yes (`=0`) | trivially |
| unsigned twisted index, native `m` | `d' + sigma` | yes | **no** (`m^2==1` inert; external-carried) |
| carrier-controlled integer `Z/3`-charge | needs `3\|m` AND `3\|sigma` | yes | **no** (double external import) |

The `Z/3` summand **is** reached by the carrier's class `2 -> (2, 2)` -- but **only as the fraction `1/3`**;
no carrier-native sector-constructible **integer** index has nonzero `Z/3` content.

**Verdicts folded (PARTIAL wins on the leg labels).** Both verifier passes reproduced every number and
sustained the **GATED** route verdict and the no-go core (the `Hom(Z/3,Z)=0` triviality and the *proved*
e-invariant fractionality are sound). The PARTIAL pass correctly refuted the **THEOREM-grade labeling** of
two component legs: (i) the "300 random inputs" mod-3 verification is a **tautology** (reducing a fixed
integer linear form mod 3 has zero discriminating power); (ii) the "two normalizations agree" mitigation of
the from-memory `p1=4` is **arithmetically circular** (`Fraction(2,24) == 1/12` is one input against
itself; the independent Adams class-2/24 route is asserted in prose, never run in code), and the signed-index
net-0 is substantially a balanced-grading rank artifact with the real content in `tr(chi)=0`. **None of these
is load-bearing to GATED** -- they downgrade component-leg confidence, not the route verdict.

### F4 -- image-of-J is fractional by construction; are the surviving imports forced? Verdict: **KILL** (of the external-import-forcing branch). Both verifier passes **SUSTAINED**.

- **(a) No native integer.** `pi_3^s = Z/24` is all torsion; the `e`-invariant is a `Q/Z` reduction by
  construction; `Hom(Z/24, Z) = 0` -- the *same* `Hom(-, Z) = 0` wall as the cohomology route
  (`Hom(Z/2, Z) = 0`). A free-rank control `Hom(Z, Z) != 0` shows "no integer" is a **measured consequence of
  torsion**, not a tautology (this is exactly why `CP^2`'s free-rank "3" is import-class while `RP^3`'s
  order-3 is not an integer at all).
- **(b) Both surviving imports are FREE.** `ind_full == m^2 d' + sigma (mod 3)`, so section-independent
  3-divisibility `<=> 3|m AND 3|sigma`. Neither is forced: `3|m` is not forced by color-triality (a
  *multiplicity* condition `mult = 6 == 0 mod 3`, not a twist-degree constraint), nor by Dai-Freed (SM
  `Theta = 4`, integer, so the mod-3 arena `Omega^Spin_5(BG_SM) (x) Z_(3) = 0` is **empty**; non-vacuity: bare
  Weyl gives `1/3`), nor by modular invariance (GU is not a worldsheet theory). `3|sigma` is not forced by
  Rokhlin (2-adic: `16|sigma`; `K3` has `sigma = -16`, failing `3|sigma`) nor any 4D pure gravitational
  anomaly.

**What both verifiers add.** Angle A re-derived every load-bearing arithmetic (Bernoulli order, CRT
factorization, `Hom`-to-`Z`, mod-3 law, SNF `H^2`, SM anomaly/triality) and found only cosmetic hardcoded
`True` summary flags and the soft-provenance note that the exact `1/12` leans on from-memory `p1=4`
(fractionality robust to it). Angle B confirmed the KILL is correctly scoped to "the external-import-forcing
branch, for known SM data + the three named requirements," with an explicit GATED downgrade condition if a
future consistency requirement forces an import.

> **F4 closes the external-forcing escape RS-S2 left named-but-open**: every route to the integer 3 requires a
> *free* external choice. It does **not** claim to kill the RS-S4 operator gate -- only to show that once
> built, that operator's mod-3 value is import-carried by free choices.

---

## The promote-or-kill adjudication

**Does a twisted index on the framed-bordism carrier give an integer in `Z/3`?**

**No -- for every object this swing could construct or enumerate.**

- The **built** twisted operator on the located carrier (F1): every GU-admissible flat twist stays fractional,
  `v_3 = -1`, `Z/3` component frozen at `2/3`. **No integer.** The block is structural (deck group order 2,
  coprime to 3), proven not blind by the `L(3;1)` control that *does* integerize.
- Every **carrier-native sector-constructible integer** index (F3): the signed index is `0` by achirality; the
  unsigned native twisted index's `Z/3` charge is external-carried (`m^2 == 1 mod 3`). **No carrier-routed
  integer reaches `Z/3`.**
- The only integers that reach `Z/3` are **external imports** (`3|m` AND `3|sigma`), and both are **free
  choices** (F4). **Not forced.**

**Is `e_R = 1/12` provably without an integer preimage?**

**Yes -- as a CLASS.** `Hom(Z/3, Z) = Hom(Z/24, Z) = Hom(Q/Z, Z) = 0` (F2). The class-to-count identification
is a **confirmed category error, one level up** from the paper's base case, universal over all framings.

**But the swing's dichotomy is subtly false, and that is the whole result.** F2's decisive distinction: "`e_R`
has no integer PREIMAGE" (TRUE) is **not** the same as "no integer index has fractional part `e_R`" (FALSE).
The object conjecture D *actually names* -- the **relative / equivariant twisted-Rarita-Schwinger index** with
a nonzero geometry-dependent bulk, integer *by construction*, whose **fractional part** (not whose class) is
`e_R` -- is neither "the e-invariant handed an integer" nor is it precluded by "no integer preimage." It lives
in the free-abelian world where `Hom`-obstructions are silent. It is **still unbuilt**, and F4 shows that even
once built, its mod-3 value reduces to the two free imports -- so it forces nothing mod 3 without a free
choice.

**Therefore:**

- The **class-as-count** reading of conjecture D is **KILLED** (category error confirmed one level up -- F2).
- The **constructive-on-located-carrier** route is **KILLED** (F1; RS-S4 GATED -> KILL on that branch).
- The **external-import-forcing** route is **KILLED** (F4; both imports free).
- The **relative-index** reading of conjecture D -- the reading Section 9 itself endorses as the "better
  statement" -- is **NOT killed**. It is **GATED** (F2, F3), on a single unbuilt object outside the reach of
  every obstruction deployed.

**Verdict: STILL-GATED.** No promote (no integer in `Z/3` was exhibited on the carrier); no full kill (the
relative index escapes). Three branches down, one unbuilt operator-gate standing.

---

## What this settles for located-not-forced Section 9 / conjecture D

**Count verdict: STILL-GATED (generation count remains OPEN -- located, not forced).**

The swing does not flip the paper's verdict, and should not. What it *settles*:

1. **The category error is confirmed one level up and made universal.** Section 9 already states
   `Hom(Z/3, Z) = 0`. This swing proves the same obstruction at the *whole* framed-bordism group and at `Q/Z`
   itself (`Hom(Z/24, Z) = Hom(Q/Z, Z) = 0`): the `e`-invariant class, for any framing, has no integer
   preimage. The class-as-count reading is dead universally, not just at the prime 3.

2. **The located carrier is closed as a source of a *forced* or *constructed* integer.** No built twisted
   operator on the GU-forced `L(2;1)` spine integerizes `e_R` (F1); no carrier-native integer index has
   nonzero `Z/3` content (F3); the external-import-forcing escape is free, not forced (F4). The carrier reaches
   `Z/3` genuinely -- but only as the fraction `1/3`.

3. **What survives is exactly, and only, the object Section 9 already names.** The relative / equivariant
   twisted-RS index with nonzero geometry-dependent bulk, integer by construction, whose fractional part is
   `e_R`. This swing did not build it and cannot obstruct it -- it is a **source-action geometry** question,
   structurally invisible to `e`-invariant *topology*.

The paper's Section 9 language ("An integer count ... can only arise from a relative, equivariant, or rank
invariant -- integer-valued by construction yet geometry-dependent -- which is exactly what the unbuilt twisted
Rarita-Schwinger index is") is **corroborated and sharpened** by this swing, not overturned.

---

## Proposed Section 9 edit (PROPOSAL -- pauses for the maintainer; the frozen paper is NOT touched)

Recommended addition to Section 9, after the existing `Hom(Z/3, Z) = 0` sentence. This is a proposal only.

> **Sharpening (2026-07-07 framed-bordism swing).** The class-to-count obstruction is not confined to the
> prime 3: `Hom(Z/24, Z) = Hom(Q/Z, Z) = 0`, so the Adams `e`-invariant carrying the located datum has no
> integer preimage under *any* homomorphism, for *any* framing -- the category error holds one level up, at the
> whole framed-bordism group. Moreover, on the GU-forced `RP^3 = L(2;1)` spine the twisted Dirac operator was
> built explicitly with every admissible flat twist; because the deck group `Z/2` is coprime to 3, every
> twisted APS eta-index remains 3-adically fractional (`v_3 = -1`, `Z/3` component frozen at `2/3`) and no such
> operator integerizes `e_R` -- the mechanism *does* integerize on a deck-`Z/3` carrier `L(3;1)`, which GU does
> not force. The one remaining escape, an off-carrier double external import (`3|m` cubic coupling and
> `3|sigma` signature), is a *free* choice: it is forced neither by anomaly cancellation, nor Dai-Freed (the
> Standard-Model mod-3 anomaly arena is empty), nor modular invariance. **Consequently the open bridge collapses
> onto exactly one object**: the relative / equivariant twisted-Rarita-Schwinger index, integer by construction
> and geometry-dependent, whose *fractional part* (not whose class) is `e_R`. It is invisible to every
> homomorphism / `e`-invariant obstruction above -- it lives in the free-abelian world where those obstructions
> are silent -- and it remains unbuilt on GU's 14-manifold. The verdict is unchanged: **located, not forced.**

This is a candidate paragraph, not an edit. It flips no verdict and no grade. Any change to the frozen paper
awaits the maintainer.

---

## Is the count frontier now exhausted?

**The carrier-enumeration frontier: effectively YES. The operator-gate: NO.** Both, honestly.

The *arenas* where a homotopy-theoretic 3 could hide are now walled on both sides:

- **Cohomology** (`H^2(RP^3; Z) = Z/2`): `Hom(Z/2, Z) = 0`, 2-adic wall. Closed (prior work; RS-S4).
- **Framed bordism** (`pi_3^s = Z/24`, the escape from that wall): the `e`-invariant is fractional by
  construction; the class-as-count reading is dead one level up (F2); the constructive-on-carrier route is
  dead (F1); the import-forcing route is dead (F4). Closed as a source of a forced/constructed integer.

There is **no further carrier to escape into.** The framed-bordism group was the last one the RS-index swing
named, and every branch of it that this swing could reach is now closed. In that precise sense the
**carrier frontier is exhausted**.

What remains is **not another carrier**. It is a single unbuilt **operator**: the relative / equivariant
twisted-RS index with nonzero geometry-dependent bulk. It is integer-by-construction, so it structurally
escapes every topological obstruction deployed here (that is *why* it survives -- F2's crux). It is a
**source-action geometry** question -- does GU's actual (unstabilized) `Y14` matter action supply a bulk making
`bulk - e_R` an integer, and does that integer reduce mod 3 to the located carrier? -- and it cannot be settled
by more `e`-invariant / bordism topology. F4 further shows that even if built, it forces nothing mod 3 without
a free external import.

**Honest bottom line.** The frontier of *places to look* is exhausted; the frontier of *things to build* has
exactly one object left, and it is the same object Section 9 named on day one. This swing did not shrink that
object -- it proved everything *around* it is closed, which is the strongest possible statement short of
building it.

---

## Next steps

1. **The relative-index gate is now isolated, not merely named.** Any future promote/kill must build the
   relative / equivariant twisted-RS index on GU's actual 14-manifold with a proven fibered-boundary reduction
   and an integer extraction with the fork resolved (Section 9's three requirements). This swing shows no
   *cheaper* route exists -- every topological shortcut is closed. Building it is a geometry / source-action
   task, blocked on GU's unstabilized matter action (the draft's own "Caveat Emptor" eq. 10.10).
2. **Control-hygiene cleanups (non-load-bearing, flagged by verifiers).** Seed `fb_f1_*.py`'s RNG (unseeded
   sanity control can flake to exit 1); replace F2/F3's near-tautological scramble controls with
   value-computed discriminators; either run the independent Adams class-2/24 normalization in code or drop the
   "two independent normalizations" claim (F3 PARTIAL showed it is circular). None of these changes any
   verdict.
3. **Provenance hardening.** The exact `e_R = 1/12` still rests on from-memory `p1 = 4` (Kirby-Melvin);
   fractionality is robust to the class, but a first-principles derivation of the framing normalization on the
   GU-forced spine would remove the last from-memory anchor under the located datum.
4. **No further carrier search is warranted.** The carrier frontier is exhausted; effort routes to the
   operator gate or to GU's source action, not to new bordism arenas.

---

## Governance

Exploration-grade synthesis. **No edit to the frozen `located-not-forced` paper.** The Section 9 proposal
above is a candidate paragraph that **pauses for the maintainer (Joe)**; it flips no verdict and no grade. The
generation-count verdict is unchanged: **OPEN (located, not forced)**, now with the carrier's constructive
bridge, the class-as-count reading (one level up), and the external-import-forcing route all specifically
closed, leaving only the unbuilt relative-index operator gate. All four legs and all eight verifier passes are
internal tier: computed and self-adversarial, not externally replicated or peer-reviewed. Any verdict/status
flip pauses for Joe.

---

## Verifier's note (main-loop review, 2026-07-07)

Synthesis of a 13-agent workflow (`wf_1adbd643-951`; 4 build routes, 8 skeptics, 1 synthesis; ~1.31M tokens).
Main-loop review:

- **Re-run from disk (exit 0, conclusions reproduced):** `fb_f1_twisted_operator_build.py` (every admissible
  twist on the GU-forced L(2;1) spine stays 2-adic, v_3=-1, Z/3 frozen at 2/3; the L(3;1) deck-Z/3 control
  integerizes -- proving the block is the deck-group ORDER coprime to 3, not a construction failure) and
  `fb_f4_imageofJ_fractional_and_imports.py` (both external imports 3|m, 3|sigma are free choices, forced by
  no anomaly/Dai-Freed/modular requirement). Both routes carried both verifiers SUSTAINED. F2's obstruction
  arithmetic re-checked: Hom(Z/3,Z)=Hom(Z/24,Z)=Hom(Q/Z,Z)=0 laddered and enumerated; |Im J_3|=24 derived
  from the Bernoulli denominator (1/24), explicitly flagged distinct from chi(K3)=24 -- clean target guard.
- **The honest verdict is STILL-GATED, and the verifiers kept it there correctly.** A KILL into "located,
  provably-not-forceable" was NOT reached, because the e-invariant/Hom obstruction (F2) catches TORSION
  CLASSES only -- integer-by-construction indices (signature, Euler, the relative APS index) provably escape
  it, and the controls discriminate. So the one object Section 9 named on day one -- the relative/equivariant
  twisted-RS index, integer-by-construction with geometry-dependent bulk -- structurally survives every
  obstruction deployed. "No integer index has fractional part e_R" is FALSE; that is exactly why it survives.
- **The decisive frontier finding (main-loop concurrence): the CARRIER-enumeration frontier is EXHAUSTED.**
  Both arenas a homotopy-theoretic 3 could hide in are now walled: cohomology (H^2(RP^3)=Z/2, Hom(Z/2,Z)=0,
  2-adic) and framed bordism (pi_3^s=Z/24, e-invariant fractional by construction, class-as-count dead one
  level up (F2), constructive-on-carrier dead (F1), import-forcing free (F4)). Framed bordism was the LAST
  carrier the RS-index swing named; every branch reachable by this swing is closed. There is no further
  carrier to escape into -- so further topology/carrier swings on the count are futile, and the verifiers
  proved it, not asserted it.
- **What remains is not a carrier but a single unbuilt OBJECT:** the relative/equivariant twisted-RS index,
  a source-action GEOMETRY question, structurally invisible to more e-invariant/bordism topology, blocked on
  GU's own unstabilized matter action (draft eq 10.10, "Caveat Emptor"). BIG-SWING-1 already BLOCKED on
  exactly this. It is not a clean promote-or-kill swing; it is an open-ended construction gated on GU itself.
- **Disposition:** the proposed Section 9 sharpening (both arenas walled; the open bridge collapses onto one
  integer-by-construction object) is sound corroboration the paper's Section 8/9 already anticipate. It is a
  SHARPENING, not a status change; count verdict stays OPEN. Pauses for the maintainer; frozen paper untouched.

**Bottom line (main-loop concurrence):** STILL-GATED -- but this is the strongest possible statement short of
building the last object: everything AROUND the twisted-RS source action is now provably closed. The frontier
of places to LOOK is exhausted; the frontier of things to BUILD has exactly one object left, and it is blocked
on GU's unbuilt matter action. The honest strategic read: further count swings are futile; the next real
progress is publishing located-not-forced (now sharper than ever) and pivoting to the mirror-mechanism paper.
