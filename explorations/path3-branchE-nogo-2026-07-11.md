---
artifact_type: exploration
status: exploration
hypothesis: H6 / H37 / count-arc (Path-3 forcing wave)
branch: "Path-3 wave, Branch E (adversarial no-go: make located-not-forced a THEOREM)"
created: 2026-07-11
title: "Path-3 Branch E no-go: the fermion generation count is LOCATED, NOT FORCED, and this is a class-wide theorem. Residual-freedom theorem -- rank-1 (the SO(3) fixed axis, one generation) is admissible whenever rank-3 (three generations) is, because both are odd-dimensional Z/3-invariant subrepresentations of Lambda^2_+(R^4)=R^3, and no equivariance/reality/self-adjointness/anomaly condition separates them. The '3' the world shows is the DIMENSION (dim Lambda^2_+=3, a forced Z-datum, the ceiling); the REALIZED count is a torsion (mod-3) datum with no canonical integer value (Hom(Z/3,Z)=0). Class-wide across the four rival constructions (index / anomaly-inflow / cobordism / torsion). The minimal condition that WOULD force 3 -- faithfulness/maximality + oddness -- is a naturalness posture, NOT first-principles (a sterile axis is anomaly-free; the mod-3 Dai-Freed arena is empty). The no-go survives the steelman."
grade: "exploration / RIGOROUS THEOREM for the residual-freedom + Hom-vanishing obstruction (elementary exact linear algebra, machine-checked, 17/17 in tests/W59_path3_E_nogo.py); ARGUMENT for the completed class-wideness (rests on the four-construction census being exhaustive of 'first-principles selectors', which is the fork census, not a closed meta-theorem). No canon, RESEARCH-STATUS, CANON, claim-status, verdict, or public posture changed. The count stays OPEN, located-not-forced."
depends_on:
  - tests/wave33/H6_family_puzzle_theorem.py
  - explorations/seven-axis-count-map-L0-L7-2026-07-11.md
  - explorations/sg4-forcing-rubric-complete-2026-07-11.md
  - explorations/path3-generation-count-forcing-wave-design-2026-07-11.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W59_path3_E_nogo.py
---

# Path-3 Branch E — the adversarial no-go: located-not-forced as a theorem

**Role.** Branch E of the blind Path-3 generation-count forcing wave. My job is the **opposite** of
branches A–D. A–D each try to FORCE the count to 3 via a different construction (index / anomaly /
cobordism / torsion). I try to **PROVE the count CANNOT be forced from first principles** — to make
"located, not forced" a **theorem**. I ran the five-persona team inline (below). I did **not**
synthesize across the other blind branches; this is Branch E's kill-attempt only.

A no-go is real, publishable, and GU-independent: it says exactly what NEW physics would be needed to
force the generation number, and it holds of any theory whose count is a rank inside the self-dual
2-forms carrying an order-3 symmetry.

## The construction forks I must cover (per GEOMETER-VS-PHYSICS-OBJECTS.md)

A no-go is only as strong as the constructions it holds in. The fork table's **Generation count** row
is load-bearing: the count is *reachable in the torsion construction* (`Z/3 ⊂ π₃ˢ = Z/24`) but *not in
the integer-index one* (`Hom(Z/3, Z) = 0`). So a **class-wide** no-go must handle the reachable
constructions too — it is not enough to re-run the index-side impossibility. I cover all four rival
constructions of "the count":

| Construction of "the count" | Reaches the 3-primary arena? | How my no-go bites |
|---|---|---|
| **Index / Dirac / Atiyah-Singer** (Z-valued) | **No** (`Hom(Z/3,Z)=0`) | Leg 1 — cannot even reach the arena (repo H6). Located-not-forced trivial. |
| **Anomaly-inflow / signature** (2-group, mod-2/mod-8) | **No** (`gcd(3,2^k)=1`) | Leg 1 — arithmetically blind to the mod-3 count. |
| **Cobordism / Dai-Freed** (GEM `Z/9`, WWY `Z/3`) | **Yes** | Leg 2 — reaches, but hits class-to-integer gap + the {1,3} subrep residual. |
| **3-primary homotopy torsion** (`Z/3` of `π₃ˢ`) | **Yes** | Leg 2 — the construction where forcing is *most* reachable, and where the kill does its real work. |

The single most important fork call: **the "3" that the world exhibits is a DIMENSION, not a
torsion-class value.** `3 = dim Λ²₊(ℝ⁴)` is an honest linear-algebra theorem (self-dual 2-forms on a
4-base are 3-dimensional) — this is the forced **ceiling**. The realized *count* is a torsion (mod-3)
datum living *inside* that ceiling, and a torsion class has no canonical integer value. Conflating the
two is exactly how a "forcing" gets smuggled in.

## The obstruction, in one paragraph

Every first-principles selector meets one of two walls. **Leg 1 (unreachable constructions):** an
integer index or a 2-group anomaly cannot separate a `Z/3` class from zero — `Hom(Z/3, Z) = 0`,
`Hom(Z/3, Z/2ᵏ) = 1` (repo H6). **Leg 2 (reachable constructions):** a 3-primary selector *does*
separate the class, but (2a) it only certifies the class is **nonzero mod 3** — it distinguishes
`{1,2}` from `{0}`; it never returns the **integer** 3, because `Hom(Z/3, Z) = 0` means a torsion class
carries no canonical integer; and (2b) the integer 3 enters only as `dim Λ²₊ = 3`, on which the order-3
symmetry acts as an element of `SO(3)` — a fixed axis (dim 1) ⊕ a rotated plane (dim 2). The count is an
**odd-rank invariant subspace** of this `ℝ³`; the odd-dimensional `Z/3`-invariant subspaces are
**exactly `{1, 3}`** (the fixed axis and the whole space). **Rank-1 (one generation, the SO(3) fixed
axis) is admissible whenever rank-3 (three generations) is** — both are invariant subrepresentations
satisfying every equivariance, reality, and self-adjointness condition, and no such condition can
forbid a subrepresentation while admitting the whole representation. The `{1,3}` degeneracy is
**irreducible**.

## Persona 1 — the rigidity / no-go theorist: the construction

**Setup.** Take the count to be the rank of the chiral generation subspace inside `V = Λ²₊(ℝ⁴) ≅ ℝ³`
(the standard location: `3 = dim Λ²₊`, forced by the 4-base, not imported). The generation symmetry is
the order-3 element; on `ℝ³` any order-3 rotation is conjugate to rotation-by-120°, which I model
exactly as the cyclic coordinate permutation `P: e₁→e₂→e₃→e₁` (an element of `SO(3)`: `P³ = I`,
`PᵀP = I`, `det P = +1`).

**Decomposition.** `V` splits into `Z/3`-isotypic constituents:
- `V₀ = span{(1,1,1)}` — the **trivial** subrep (the rotation axis), `dim 1`, `P v = v`;
- `V₁ = {x+y+z = 0}` — the **faithful** 2-dim real irrep, `dim 2`. In the basis `u₁=(1,-1,0)`,
  `u₂=(0,1,-1)`, `P|V₁ = [[0,-1],[1,-1]]`, char poly `x²+x+1`, discriminant `−3 < 0`: **no real
  eigenvalue**, so `V₁` is **irreducible over ℝ** (it has no proper invariant subspace).

**The residual-freedom theorem.** Because the two constituents each have multiplicity 1 and `V₁` is
irreducible, the `Z/3`-invariant subspaces of `ℝ³` are **exactly** `{0, V₀(1), V₁(2), V(3)}` (the `2²=4`
sub-sums). The count is a **net chirality**, an **odd** datum (prior H37 / wave16-17 leg: even ranks are
vectorlike / net-zero), so the admissible counts are the **odd-dimensional** invariant subspaces:

$$\boxed{\text{admissible counts} = \{\dim V_0,\ \dim V\} = \{1,\ 3\}.}$$

`V₀` (rank 1) is `P`-invariant and reality-closed exactly as `V` (rank 3) is. Any first-principles
selector — an index, an anomaly condition, a bordism class, a torsion action — that is required to be
equivariant, reality-compatible, and self-adjoint admits **both**. **No consistency condition removes
the `{1,3}` degeneracy.** ∎ (for the residual leg)

**The class-to-integer leg.** In the reachable constructions the selector reaches `Z/3` (e.g. Adams
`e_KO(8ν) = 1/3`, order 3; `|Hom(Z/3, Z/3ᵃ)| = 3`), but this only labels the class in `{0,1,2}`. The
integer 3 is **not** the class value — it is `dim Λ²₊`. `Hom(Z/3, Z) = 0`: a torsion class has no
canonical integer, so no reachable selector *reads off* 3 either. Both legs point at the same residual.

## Persona 2 — the math referee: grade, circularity, vacuity

- **Rigorous.** (i) `dim Λ²₊(ℝ⁴) = 3` — exact. (ii) `P ∈ SO(3)` of order 3, the isotypic split, and the
  irreducibility of `V₁` (`disc = −3`) — exact integer/rational arithmetic. (iii) The invariant-subspace
  lattice `{0,1,2,3}` and the odd-rank residual `{1,3}` — exact. (iv) `Hom(Z/3,Z)=0`,
  `Hom(Z/3,Z/2ᵏ)=1` — H6, proven. Together these establish the residual-freedom theorem **rigorously**.
- **Not a theorem (honestly).** The completed *class-wide* claim ("no first-principles selector of ANY
  kind forces 3") rests on the four-construction census being **exhaustive** of first-principles
  selectors. That is the fork census — an argument, not a closed meta-theorem. Grade split: **rigorous
  theorem** for the obstruction mechanism within each named construction; **argument (strong)** for the
  completed class-wideness.
- **Circularity check.** The argument does **not** assume the count is unforced and then conclude it. It
  grants each construction its best case (the torsion route *reaches* the arena — I built the positive
  control) and derives the residual purely from (a) `Hom`-vanishing and (b) the representation theory of
  `SO(3)` on `ℝ³`. No step presupposes the conclusion. Clean.
- **Vacuity check.** Not vacuous: the residual is a *specific, named, finite* freedom (`{1,3}` = the two
  odd `Z/3`-subreps), and I exhibit the concrete rank-1 solution (the fixed axis) and show it survives
  every stated condition. This matches — and sharpens to a clean linear-algebra core — the repo's SG4
  rubric result (the residual is a rigid, finite, discrete choice forced by nothing).

## Persona 3 — the adversary-to-the-adversary: a genuine repair attempt

I tried honestly to **force 3** — to find the minimal extra condition that collapses `{1,3} → 3`, and
to check whether it is first-principles (if it is, my no-go is *not* class-wide).

1. **Faithfulness / maximality.** Demand the count carrier be a **faithful** `Z/3`-representation —
   equivalently, use the **whole** `Λ²₊`, no invariant-subspace truncation. Faithfulness kills the
   trivial axis `V₀` (on which `Z/3` acts trivially), leaving rank ≥ 2; with oddness → **rank 3**. This
   **does force 3.** *Is it first-principles?* **No.** A trivial ("sterile") self-dual direction is not
   an inconsistency — sterile sectors are ubiquitous and anomaly-free (a rank-1 / one-generation
   universe cancels every gauge and mixed anomaly), and the relevant **mod-3 Dai-Freed arena is empty**
   for SM data (repo R2: `Ω^Spin₅(BG_SM) ⊗ Z₍₃₎ = 0`), so **no anomaly forbids the axis**. Faithfulness
   is a naturalness *posture*, not a consistency/anomaly/symmetry *theorem*. **The no-go survives.**
2. **"The count IS the whole self-dual bundle by definition."** This is faithfulness renamed as a
   definition — it *chooses* the answer rather than deriving it. A skeptic identifying the count with an
   invariant *sub*-bundle (the fixed axis) is not refuted by any consistency condition. **Fails.**
3. **A canonical bordism generator pins the integer.** Even if the cobordism group `Z/3` (or GEM's
   `Z/9`) has a distinguished generator, that generator is an **order-3 element** = the class `1`, not
   the integer `3`; calling it "3" still needs the class-to-integer lift `Hom(Z/3,Z)=0` forbids. And a
   canonical generator would give you the count **1**, not 3. **Fails.**
4. **Oddness upgraded to force 3.** Oddness only excludes the even ranks `{0,2}`; it leaves `{1,3}`. It
   cannot by itself pick 3 over 1. **Fails.**

**Verdict of the repair attempt.** The *minimal* condition that forces 3 is **faithfulness/maximality +
oddness**, and it is **natural but not first-principles**: it is exactly the free "use the whole bundle"
input the no-go identifies as the irreducible residual. No repair promotes it to a consistency
requirement. **The no-go is class-wide and survives fair steelmanning.** (Honest caveat: *if* some
construction furnished a genuine anomaly forbidding sterile self-dual directions, faithfulness would
become first-principles *there* and the no-go would fail for that construction. None is known — the
mod-3 arena is empty — so this is the named escape hatch, not an actual escape.)

## Persona 4 — the cross-checker: the concrete SO(3) case

Encoded deterministically in `tests/W59_path3_E_nogo.py` (pure Python, exact `Fraction` arithmetic, no
dependencies, **17/17**, exit 0):

- **B0** `dim Λ²(ℝ⁴)=6 = 3+3`; the count ceiling `dim Λ²₊ = 3` (the '3' as a dimension).
- **B1** `P` is a genuine `SO(3)` order-3 element; fixed axis `V₀ = span{(1,1,1)}` (rank-1 solution);
  invariant plane `V₁ = {x+y+z=0}` (the faithful 2-dim irrep).
- **B2** `P|V₁` char poly `x²+x+1`, `disc = −3 < 0` → `V₁` irreducible; invariant-subspace lattice
  exactly `{0,1,2,3}`; **odd-rank residual = `{1,3}`** (the residual-freedom theorem); the rank-1 axis is
  equivariant **and** reality-closed — admissible whenever rank-3 is.
- **B3** Leg 1: `Hom(Z/3,Z/2ᵏ)=1`, `Hom(Z/3,Z)=0` — index/2-group selectors cannot reach the arena.
- **B4** Leg 2a: reachable selectors *do* separate the class (`e_KO(8ν)=1/3`, `e_KO(16ν)=2/3`, order 3)
  but only certify **nonzero mod 3** `{1,2}`; the class-to-integer gap `Hom(Z/3,Z)=0` blocks reading 3.
- **B5** Steelman: faithful odd invariant subspaces = `{3}` (forcing works) — **but** the mod-3
  Dai-Freed arena is empty and the axis is anomaly-free, so faithfulness is not first-principles.
- **B6** Honesty guards: ceiling forced / realized `{1,3}` not; class-wideness is an argument (census),
  not a meta-theorem.

The concrete rank-1 case is the crux the wave asked me to verify: **the SO(3) fixed axis is a genuine,
equivariant, reality-closed, anomaly-free one-generation solution.** It is real, not a strawman.

## Persona 5 — the synthesizer: the branch verdict

**Graded verdict on the three sub-questions.**

- **Q-force — NO.** No first-principles selector forces 3. The **ceiling** 3 (= `dim Λ²₊`) is forced;
  the **realized** count `{1,3}` is not. *Grade: rigorous* (exact linear algebra + H6).
- **Q-extra — the irreducible residual.** The `{1,3}` degeneracy = the two **odd-dimensional
  `Z/3`-invariant subspaces** of `Λ²₊ = ℝ³` (the fixed axis `V₀`, rank 1; the whole space, rank 3),
  **plus** the class-to-integer gap `Hom(Z/3,Z)=0` in the reachable constructions. No equivariance,
  reality, self-adjointness, oddness, or (empty mod-3) anomaly condition removes it.
- **Q-nogo — YES, CLASS-WIDE.** Across index / anomaly-inflow / cobordism / torsion, via one uniform
  mechanism: **the count is a torsion (mod-3) datum with no canonical integer value, realized as an
  invariant subspace whose odd choices `{1,3}` no consistency condition separates.** *Grade: rigorous
  theorem for the obstruction mechanism; argument for the completed class-wideness (four-construction
  census).*

**Class-wide or construction-specific?** **CLASS-WIDE.** Leg 1 kills the unreachable constructions
(index, 2-group) by `Hom`-vanishing; Leg 2 kills the reachable ones (cobordism, torsion) by the
class-to-integer gap + the `{1,3}` subrep residual. The named escape hatch (a construction furnishing a
genuine anomaly that forbids sterile self-dual directions, thereby making faithfulness first-principles)
is **not realized** — the mod-3 Dai-Freed arena is empty. So no construction currently escapes.

**Minimal condition that WOULD force 3.** **Faithfulness / maximality (+ oddness):** use the whole
`Λ²₊`, admit no invariant-subspace truncation. **Not first-principles** — a sterile axis is anomaly-free
and the mod-3 arena is empty. This is precisely the "other teams' blockbuster" test: if any of A–D can
show faithfulness is a *consistency* requirement in their construction, they force 3 and defeat my
no-go. I found no such argument, and the empty mod-3 arena is positive evidence against one.

**The one assumption the kill rests on.** That "first-principles selector" means a
consistency/anomaly/symmetry/reality condition (not a naturalness posture), and that the count is a
rank inside `Λ²₊` with the order-3 element acting as `SO(3)`. If faithfulness were itself
first-principles (an anomaly forbidding sterile self-dual directions), the residual collapses and the
kill fails — but no such anomaly is known.

**Confidence grade.** *Rigorous theorem* for the residual-freedom obstruction (the `{1,3}` odd-invariant
-subspace computation + `Hom`-vanishing are elementary and machine-checked). *Argument (strong)* for the
completed class-wide claim (rests on the four-construction census being exhaustive). This is the wave's
**"E proves a class-wide no-go"** pre-registered outcome, at the honestly-attainable strength: a rigorous
mechanism plus a strong-but-not-meta-theorem exhaustiveness claim.

## Relation to prior repo results (not a re-run)

- **H6** (`tests/wave33/H6_family_puzzle_theorem.py`) proved the *selector-kind* necessity
  (forcing a 3-primary count needs nonzero 3-Sylow image) and flagged `Hom(Z/3,Z)=0` as an open gate.
  Branch E **uses** H6 for Leg 1 and **closes the gate into a positive no-go** via the `SO(3)`
  residual-freedom theorem — the piece H6 explicitly left open ("does NOT derive the integer 3").
- **Seven-axis map / SG4 rubric** found located-not-forced across selector-side axes and hardened the
  residual to a "rigid finite discrete choice forced by nothing." Branch E supplies the **clean
  linear-algebra core** of why: the residual is literally the two odd `Z/3`-subreps of `Λ²₊`, and the
  forcing bit (faithfulness) is provably not a consistency condition.

## What this does NOT do

No claim that faithfulness is *impossible* to derive — only that it is not derived by any known
first-principles condition and the mod-3 anomaly arena is empty. No `3` imported (the `3` is `dim Λ²₊`,
a theorem; the count residual is `{1,3}`). No change to `CANON.md`, `RESEARCH-STATUS.md`, claim status,
verdicts, or public posture. The generation count stays **OPEN**, now with a rigorous located-not-forced
mechanism and a sharp, decidable demand on anyone who would force it: **exhibit a first-principles
consistency/anomaly condition that forbids the SO(3) fixed axis (the sterile self-dual direction).**
Absent that, the number of generations is irreducible data given these principles.
