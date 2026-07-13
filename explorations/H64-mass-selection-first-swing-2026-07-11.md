---
artifact_type: exploration
status: exploration (5-persona inline team; first-swing kill-or-learn on H64; deterministic machine-checked test)
created: 2026-07-11
hypothesis: H64
title: "H64 -- THE MASS HIERARCHY AS THE OBSERVER'S SELECTION. C2/W72's Schur wall forces the collective doublet mass-degenerate; the masses need family-symmetry BREAKING. H62 firmed VALUE = requires-breaking, so arena/value PREDICTS the masses are observer-selected = FREE. VERDICT: PARTIAL-PATTERN-PREDICTED (weak, arena-level). The degeneracy-lifting breaking is FORCED to be a DOUBLET spurion in Sym^2(Lambda^2_+) (2 unbroken params a,b + 4 breaking params = two Z/3 doublets); the fixed axis (individual/democratic direction) is CANONICAL, and a fixed-axis-preserving spurion leaves a protected DEMOCRATIC mixing column (tribimaximal-like, CONDITIONAL, generic to Z/3). BUT the split magnitude, the SIGN (hierarchy direction = which generation is heavy), and the intra-collective mixing angle are FULLY FREE (a continuum, both signs). No exact mass/ratio is predicted; World A (a geometrically FORCED mass value, which would FALSIFY arena/value) does NOT obtain. => masses FULLY FREE as VALUES; arena/value CONFIRMED and REFINED (the arena now includes a breaking-TYPE texture the observer selects WITHIN), NOT contradicted. Caveat: the texture is GENERIC to a Z/3 family symmetry (Curie/genericity, exactly parallel to H62), not a GU-unique signature."
grade: "COMPUTED / analysis. tests/W76_H64_mass_selection_swing.py (deterministic, no RNG, exit 0, 16/16): encodes the breaking characterization (unbroken circulant spectrum {democratic singlet, degenerate pair}; the Sym^2 decomposition 2 singlets + 2 doublets; the doublet-spurion identity of the breaking; the fixed-axis-preserving-vs-mixing spurion contrast; the free-value sweeps; the World-A absence). Standard: elementary Z/3 rep theory (Schur on the real-irreducible 2, circulant diagonalization, Sym^2 branching 1+2 -> 2 singlets + 2 doublets); no new mathematics. No canon / RESEARCH-STATUS / claim-status / verdict / posture movement; the masses/count stay OPEN, GU stays framework-not-theory."
construction: "program-native (GEOMETER-VS-PHYSICS-OBJECTS): the family symmetry the TORSION-supplied discrete Z/3 acting as an order-3 SO(3) element on Lambda^2_+ = R^3 = 1 (individual, fixed axis) + 2 (collective, real-irreducible). The continuous-SO(3) side of the fork is stated explicitly (Sec 6): it would make the UNBROKEN spectrum fully 3-fold degenerate, adding a first breaking stage SO(3)->Z/3 that separates the individual -- the two-stage cascade -- but does NOT change the FREE-value verdict."
depends_on:
  - explorations/path5-branchC2-capability-enclosures-reframe-2026-07-11.md
  - explorations/H62-arena-value-partition-firmup-2026-07-11.md
  - explorations/path3-branchD-homotopy-torsion-2026-07-11.md
  - explorations/CONJECTURE-source-action-is-the-observer-2026-07-11.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W76_H64_mass_selection_swing.py
  - tests/W72_path5_C2_capability_enclosures.py
  - tests/W73_H62_arena_value_partition.py
---

# H64 -- the mass hierarchy as the observer's selection (first-swing kill-or-learn)

## The sharp question (why it is a real test, not a fishing trip)

C2/W72 hit a WALL: under the unbroken family symmetry the collective doublet of `Lambda^2_+ = 1 (individual,
fixed axis) + 2 (collective, real-irreducible)` is **mass-degenerate** by Schur (`m_2 = m_3`), contradicting the
observed non-degenerate `1+1+1` hierarchy. So the masses require **breaking** the family symmetry. H62 firmed the
arena/value split via the SYMMETRY characterization: **VALUE = requires symmetry-BREAKING.** The masses ARE
values. Arena/value therefore **PREDICTS the masses are observer-SELECTED = FREE** -- not forced by the structure.

This makes H64 a genuine test with three mutually-exclusive outcomes:

- **FULLY-PREDICTED (World A, least likely, most consequential):** if the observer/source-action structure
  predicted the exact masses, that is a forced VALUE -> it **CONTRADICTS arena/value** (H62's falsifier World A)
  -> the model takes damage but you get a mass headline. **Must be checked hard.**
- **FULLY-FREE (arena/value confirmed, no headline):** if the masses are structure-free, arena/value holds; the
  honest, expected deflationary result.
- **PARTIAL-PATTERN (the interesting middle, a genuine LEARN):** the structure predicts a *pattern* of the
  breaking (a texture, a hierarchy direction, a mixing structure, a parameter count) WITHOUT fixing the exact
  values -- the observer selects within a constrained pattern, not arbitrarily.

Construction fork (per `GEOMETER-VS-PHYSICS-OBJECTS.md`): I take the family symmetry program-native as the
**torsion-supplied discrete `Z/3`** (path3-branchD: the torsion supplies only the order-3 element; continuous
`SO(3)` is a strictly stronger added input). Both sides of the fork are carried; Sec 6 shows the verdict is
fork-robust.

Run as a 5-persona inline team (one worker, sequential): (1) FLAVOR / REP-THEORY specialist; (2) MATH REFEREE;
(3) ADVERSARY ("free spurion, no pattern"); (4) CROSS-CHECKER; (5) SYNTHESIZER.

---

## Persona 1 -- FLAVOR / REP-THEORY specialist: characterize the breaking, hunt a partial pattern

### 1a. What actually needs lifting (the breaking's JOB is narrow)

The most general **family-symmetric** (unbroken) mass operator on `Lambda^2_+ = R^3` under the `Z/3` family action
`g:(x,y,z)->(y,z,x)` is a **symmetric circulant** `M = a*I + b*(C + C^T)` (`C = g`). Its spectrum (W76 T1.2):

> eigenvalues `{a+2b (democratic singlet), a-b, a-b (degenerate pair)}`, with the **singlet eigenvector EXACTLY
> the fixed axis `(1,1,1)/sqrt3`** (the INDIVIDUAL / democratic combination).

Two facts drop out, both load-bearing:

1. **The individual is already a mass eigenstate under the unbroken symmetry.** The `1`-vs-`2` (individual-vs-
   collective) gap `= (a+2b) - (a-b) = 3b` exists with **no breaking at all** -- it is the difference of two
   independent Schur scalars. The individual is *not* one of the three flavor states; it is the **democratic
   combination** `(1,1,1)/sqrt3` (a basis subtlety the naive "the 1st generation is the individual" reading
   misses).
2. **Only the collective pair's degeneracy needs lifting.** The breaking's JOB is narrow and specific: split
   `a-b -> a-b +/- eps`. It does not have to *create* the `1+2` split (that is unbroken); it only has to lift the
   `2`.

### 1b. The breaking has a FORCED rep-theoretic TYPE (the partial-pattern seed)

Decompose the 6-dim space of real symmetric operators under the `Z/3` conjugation action `M -> g M g^T` (W76 T2.1):

> `Sym^2(Lambda^2_+) = Sym^2(1 + 2) = ` **2 INVARIANT (singlet) directions** `+` **4 BREAKING directions (= two
> `Z/3` doublets)**.

The 2 invariants are exactly the unbroken masses (`I` and `C+C^T`, i.e. `a,b`); **all splitting lives in the
4 doublet parameters.** The degeneracy-*lifting* piece is specifically the doublet in `Sym^2(collective-2)` --
a spurion `S2 = e1 e1^T - e2 e2^T`, traceless on the collective plane (W76 T2.3). So **"the breaking" is not an
arbitrary operator: it is a spurion transforming in the DOUBLET part of `Sym^2(Lambda^2_+)`.** This is a real
structural constraint (rep theory), and it bounds the parameter count (4 breaking params, not an unbounded free
matrix). **This is the partial pattern: the observer selects the mass-splitting within a rep-theoretically fixed
FORM.**

### 1c. Direction free; a fixed-axis-preserving spurion protects a democratic mixing column (conditional)

Within the collective doublet the spurion **direction is FREE** -- the plane is real-**irreducible**, it has **no
canonical direction** (the same irreducibility that forbids rank-2 enclosures in C2). But the enclosure premise
("the individual is always enclosed" = the fixed axis is canonical) singles out a natural *class* of breakings:
**fixed-axis-preserving** ones. Here the rep theory bites cleanly (W76 T3):

- A `Sym^2(collective)` spurion `S2` **splits the pair AND annihilates the fixed axis** (`S2 v0 = 0`), so `v0`
  stays an eigenvector -- the **democratic direction is PROTECTED**.
- An `(individual (x) collective)` spurion `S1 = v0 e1^T + e1 v0^T` instead **rotates `v0` away** -- no protected
  column.

If **two** mass sectors (e.g. charged leptons and neutrinos, or up and down quarks) both break with (different)
`Sym^2(collective)` spurions, both keep `v0` as an eigenvector -> **one column of the mixing matrix is DEMOCRATIC
`(1,1,1)/sqrt3`** (the tribimaximal "solar" column), with the remaining angles free (W76 T3.3). This is a genuine,
if conditional, **mixing texture**.

**Specialist finding:** a real but WEAK partial pattern -- forced breaking rep-TYPE (doublet spurion), canonical
fixed axis, bounded parameter count, and a CONDITIONAL democratic mixing column. The mass VALUES and the
non-democratic angles are free.

---

## Persona 2 -- MATH REFEREE: structural prediction vs tuned numerology (ruthless)

| claim | grade | forced / asserted |
|---|---|---|
| unbroken family-symmetric mass = symmetric circulant; spectrum `{a+2b, a-b, a-b}` | **theorem** | forced (circulant/Schur) |
| singlet eigenvector = fixed axis `(1,1,1)/sqrt3` (the individual is the democratic combination) | **theorem** | forced |
| `Sym^2(Lambda^2_+)` under `Z/3` = 2 singlets + 2 doublets; splitting lives in the doublets | **theorem** | forced (branching) |
| the degeneracy-lifting breaking is a DOUBLET spurion in `Sym^2(Lambda^2_+)` | **theorem** | forced GIVEN `Z/3` family symmetry |
| a `Sym^2(collective)` spurion preserves the fixed axis; an `(1 (x) 2)` spurion rotates it | **theorem** | forced |
| protected democratic mixing column (tribimaximal "solar" column) | **theorem GIVEN two conditions** | conditional: (i) fixed-axis-preserving breaking in BOTH sectors; (ii) same `Z/3` on both |
| split MAGNITUDE / SIGN (hierarchy direction) / intra-collective ANGLE | **NOT predicted** | free (continuum, both signs -- W76 T4) |
| exact masses or a mass RATIO | **NOT predicted** | free |
| the pattern is a GU-UNIQUE signature | **NO** | it is generic to any `Z/3` family symmetry (Curie/genericity) |

**Referee verdict.** The partial pattern is **real but weak, and it is entirely ARENA-level.** Everything graded
"theorem" is a **symmetry INVARIANT** (a fact about the unbroken structure or the rep-type of the breaking) --
under H62's characterization these are **arena**, not values. Nothing that a numerologist would call a
"prediction" (a mass, a ratio, an angle value) is forced. The one thing that *looks* like a flavor prediction --
the democratic mixing column -- is **conditional** (needs fixed-axis-preserving breaking in both sectors) and
**generic** (it is the standard `Z/3`/`A4` -> tribimaximal mechanism of Harrison-Perkins-Scott / Ma, not novel to
GU). **I reject any reading that this is a mass headline.** I accept it as a genuine, honestly-weak structural
learn: *the observer selects the masses within a rep-theoretically constrained breaking form.*

**Numerology guard (explicit).** I checked the tempting fit -- "the electron is the odd-one-out (207x below the
`mu`-`tau` pair, which are only 17x apart), matching `1 + near-pair`." **This is a fit, not a prediction:** (i) the
"individual" is the democratic combination, not a single generation, so "electron = individual" is a basis
mislabel; (ii) the assignment of which physical generation plays which role is FREE, so any "odd-one-out" can be
arranged; (iii) the observed pair (`mu`,`tau`) is split by a factor 17 -- **not** near-degenerate -- so the
predicted `1 + degenerate-2` texture is **absent** in the data (W76 T4.4). I do **not** count it.

---

## Persona 3 -- ADVERSARY: "the breaking is a free spurion, no pattern is predicted"

> **"You have dressed up a free spurion."** Your `S2` has a free magnitude, a free sign, and (in the plane) a free
> direction. Sweep them and you get any splitting and any mixing angle you like (your own W76 T4.1/T4.2:
> continuum, both signs). That is the DEFINITION of a free parameter. Calling its *rep-type* "a pattern" is
> re-describing the arena you already had (C2's Schur degeneracy), not predicting anything new about the masses.
>
> **"Your one flavor-looking claim is conditional AND borrowed."** The democratic mixing column needs the breaking
> to be fixed-axis-preserving in BOTH sectors -- an assumption, not a theorem -- and it is the textbook `A4`
> tribimaximal mechanism. GU adds nothing; it merely hosts a generic `Z/3` flavor symmetry. By H62's own
> genericity caveat, generic != a GU signature.
>
> **"The predicted texture is falsified by data."** `1 + degenerate-2` is not what nature shows (no near-degenerate
> generation pair). To reach the real spectrum you must break LARGE and free, which erases the texture. So the
> masses carry NO surviving structural constraint -- this is FULLY-FREE, and you are inflating it to PARTIAL to
> manufacture a learn.

The adversary's three strikes all **land partially**: the values are free (conceded, T4); the mixing column is
conditional and generic (conceded); the observed spectrum erases the unbroken texture (conceded, T4.4). What the
adversary does **not** overturn: the **rep-TYPE of the breaking is genuinely forced** (a doublet spurion, not an
arbitrary operator), the **fixed axis is genuinely canonical**, and the **parameter count is genuinely bounded**
(4, not 6). These are structural facts about the *form* of the value-selection, not the values -- so the honest
line is not "FULLY-FREE" but "FULLY-FREE VALUES within a constrained breaking FORM." Presented, weighed by the
synthesizer.

---

## Persona 4 -- CROSS-CHECKER: reproduce the breaking structure and the free-value sweeps independently

1. **Unbroken spectrum** reproduced from the symmetric circulant `a*I + b*(C+C^T)`: `{a+2b, a-b, a-b}`, singlet
   eigenvector `(1,1,1)/sqrt3` (W76 T1.2). Matches the C2/W72 Schur degeneracy from a different construction
   (circulant diagonalization vs Reynolds averaging) -- **independent agreement.**
2. **`Sym^2` decomposition** reproduced by diagonalizing the order-3 conjugation action on the 6-dim symmetric
   space: eigenvalue-1 multiplicity 2 (singlets), complex pairs giving 2 doublets (W76 T2.1). Independent of the
   spurion construction. **Confirms 2+4.**
3. **Fixed-axis protection** cross-checked directly: `S2 v0 = 0` (collective spurion) vs `S1 v0 != scalar*v0`
   ((1 (x) 2) spurion) (W76 T3.1/T3.2). **Confirms the conditional column is real and its condition is real.**
4. **Free-value sweeps** cross-checked: signed pair-split (via the quadratic form `e1^T M2 e1 - e2^T M2 e2`, which
   avoids the sign-collapse of sorting) ranges over a continuum with **both signs** (W76 T4.1); the mixing angle
   ranges over a continuum (W76 T4.2). **Confirms magnitude, sign, and direction are all free.**
5. **World-A absence** cross-checked against the record: C2's "one overturning thing" hunt and H62's adversary
   Counterexample-hunt-1 both searched for a *forced* symmetry-breaking value and found none on the board
   (W76 T4.3). **No forced mass value; arena/value's falsifier does not fire.**

**Cross-check verdict:** the forced structural facts (unbroken spectrum, `Sym^2` = 2+4, doublet-spurion identity,
fixed-axis protection) all reproduce; the free-value claims all reproduce; the claimed pattern is **not a fit**
(it is symmetry-invariant structure), and the values are **genuinely free** (not a hidden tuning). Everything
checks.

---

## Persona 5 -- SYNTHESIZER: verdict, meaning for arena/value and the conjecture

**VERDICT: PARTIAL-PATTERN-PREDICTED (weak, arena-level). Masses/mixings FULLY FREE as VALUES. Arena/value
CONFIRMED and REFINED, NOT contradicted. World A (FULLY-PREDICTED) does NOT obtain.**

**The breaking pattern needed to lift the Schur degeneracy:**
- Under the unbroken `Z/3` the individual (democratic combination) is already a mass eigenstate; **only the
  collective pair needs lifting.**
- The lifting spurion is **FORCED to transform as a DOUBLET in `Sym^2(Lambda^2_+)`** (2 unbroken params `a,b` + 4
  breaking params = two `Z/3` doublets). Its **direction within the collective plane is FREE** (irreducibility ->
  no canonical direction).
- A **fixed-axis-preserving** (`Sym^2(collective)`) spurion protects the democratic direction; an
  `(individual (x) collective)` spurion rotates it. The observer's choice among these is free.

**The partial structural prediction (with grade):**
- **Forced (theorem, given `Z/3` family symmetry):** the breaking's rep-TYPE is a doublet spurion; the fixed axis
  is canonical; the parameter count is bounded (4, not 6). *Grade: theorem-grade, but arena-level (a symmetry
  invariant), not a mass value.*
- **Conditional (theorem given two assumptions) + generic:** a protected **democratic mixing column**
  (tribimaximal-like) if both sectors break fixed-axis-preservingly under the same `Z/3`. *Grade: real but weak --
  conditional, and GENERIC to `Z/3` flavor symmetry (Curie/genericity, exactly parallel to H62), NOT a GU-unique
  signature.*
- **NOT predicted (free values):** the split magnitude, the **hierarchy DIRECTION** (which generation is heavy --
  free, both signs occur), the intra-collective mixing angle, and any exact mass or ratio.

**What it means for arena/value.** This **CONFIRMS and REFINES** H62, it does not damage it:
- The forced structural facts are all **symmetry INVARIANTS** -> under H62's characterization they are **ARENA**,
  not values. So the arena is now seen to include not just the count `{1,3}` and the replicas but also a
  **breaking-TYPE texture** (the rep-type of the value-selecting spurion, the canonical fixed axis).
- The masses/angles are exactly the **VALUES** -- observer-selected by a free choice of spurion magnitude/sign/
  direction, precisely what arena/value predicts.
- **World A does NOT obtain:** no forced mass value exists on the board (re-confirmed). Arena/value's falsifier
  does not fire. Had the structure fixed a mass ratio geometrically, THAT would have been the FULLY-PREDICTED
  outcome damaging H62 -- it did not.

So the observer/source-action reading survives cleanly: **the observer forces the arena (count + replicas +
breaking-TYPE texture) and selects the values (the masses, by choosing the doublet spurion).** The boundary H62
drew is not only intact -- it is *sharper*: the arena reaches into the FORM of the symmetry-breaking, while the
observer's free selection is the spurion's magnitude and direction.

**The load-bearing assumption.** That the family symmetry is the discrete `Z/3` acting on `Lambda^2_+` (program-
native, path3-branchD) and that the mass operator is a family-covariant symmetric operator (a spurion analysis).
The conditional mixing-column result additionally assumes fixed-axis-preserving breaking in both sectors -- a
natural but unforced alignment with the enclosure premise.

**Confidence.** HIGH on the breaking characterization and the free-value verdict (elementary `Z/3` rep theory;
circulant diagonalization, `Sym^2` branching, and the sweeps are exact and reproduced two ways). MEDIUM on the
conditional democratic-column being physically relevant (it is conditional and generic). HIGH on World A being
absent (re-confirms two prior hunts).

**The one overturning thing (for a mass headline).** Exhibit a GU mechanism that **forces** the doublet spurion's
magnitude AND direction from geometry (e.g. a `ker-Gamma` eigenvalue ratio that pins the collective mass-splitting
to a determined value, in a determined direction). That would move the verdict to FULLY-PREDICTED -- a mass
headline, but at the cost of **falsifying arena/value** (World A). C2 and H62 both searched for exactly this and
found the structure supplies neither the breaking magnitude nor its ordering; this swing re-confirms it. Absent
that, the masses are free values and arena/value stands.

---

## Honest scope (what is and isn't established)

- **Established (analysis/computed, `tests/W76_H64_mass_selection_swing.py`, 16/16, exit 0):** the unbroken
  family-symmetric spectrum `{democratic singlet, degenerate pair}` with the singlet eigenvector = the fixed axis;
  `Sym^2(Lambda^2_+)` under `Z/3` = 2 invariant (unbroken) + 4 breaking (two doublets); the degeneracy-lifting
  breaking is a doublet spurion in `Sym^2`; a `Sym^2(collective)` spurion preserves the fixed axis while an
  `(1 (x) 2)` spurion rotates it (conditional protected democratic mixing column); the split magnitude, sign
  (hierarchy direction), and intra-collective angle are all free (continuum, both signs); World A (a forced mass
  value) does not obtain on the board.
- **NOT established:** any exact mass, mass ratio, mixing angle value, or hierarchy direction (all free); that the
  democratic mixing column obtains unconditionally (it is conditional on fixed-axis-preserving breaking in both
  sectors) or that it is GU-unique (it is generic `Z/3` flavor structure); that the observed spectrum realizes the
  `1+2` texture (it does not -- no near-degenerate generation pair; the texture must be broken large and free).
- **No movement:** canon, RESEARCH-STATUS, claim-status, verdicts, posture, the generation count, and the masses
  are all unchanged; the masses/count stay OPEN; the arena/value split stays a MODEL of the outputs; the
  conjecture stays a conjecture; GU stays framework-not-theory. Exploration/analysis grade. No git commit
  (orchestrator verifies).

## Not claimed

Not a mass prediction (the values are free); not a claim that arena/value is falsified (World A does not obtain --
the opposite: arena/value is confirmed and refined); not a claim that the democratic mixing column is forced (it
is conditional) or GU-unique (it is generic `Z/3` flavor structure, Curie/genericity); not a canon/verdict
movement. A graded, reproducible demonstration that the mass-hierarchy's family-symmetry breaking is a **doublet
spurion of a rep-theoretically fixed TYPE** (a weak, arena-level PARTIAL PATTERN the observer selects WITHIN),
while the mass/mixing VALUES themselves remain FULLY FREE -- exactly as arena/value predicts.

## Fork note (SO(3) vs Z/3), carried per GEOMETER-VS-PHYSICS-OBJECTS

If the family symmetry were the **continuous `SO(3) = SU(2)_+`** (the strictly-stronger input path3-branchD flags
as not torsion-supplied), the UNBROKEN spectrum would be fully **3-fold degenerate** (Schur on the irreducible
`3`), and lifting it would proceed as a **two-stage cascade `SO(3) ⊃ Z/3 ⊃ 1`**: stage 1 (`SO(3)->Z/3`) separates
the individual along the canonical fixed axis; stage 2 (`Z/3->1`) splits the collective pair with a free direction.
This *adds* an ordered breaking cascade (a slightly richer arena-level texture) but does **not** change the
FREE-value verdict: each stage's magnitude and (for stage 2) direction remain free, and no mass value is forced.
The verdict is **fork-robust**: PARTIAL-PATTERN (arena-level) on the FORM of the breaking, FULLY-FREE on the
values, arena/value confirmed, on both sides of the fork.
