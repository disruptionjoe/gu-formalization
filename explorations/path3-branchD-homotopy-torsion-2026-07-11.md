# Path 3 / Branch D -- the 3-primary homotopy-torsion construction of the generation count

**Status:** BLIND branch of the "why three generations?" wave. Reconstruction-grade; the pure math is
theorem-grade, the physical admissibility mappings are argued. Durable in-repo; not committed by this run.
**Test:** `tests/W58_path3_D_homotopy_torsion.py` (14/14 PASS, exit 0, deterministic).
**Construction fork used (per `GEOMETER-VS-PHYSICS-OBJECTS.md`):** the *generation-count* row -- the count as a
**torsion class in the 3-primary arena** `Z/3 subset pi_3^s = Z/24`, NOT a Z-valued index. Branch D is the
*reachable* construction (nonzero 3-Sylow image, H6), so it is where forcing is possible if anywhere; it is
tested hardest here.

---

## 1. Construction of "the count" (stated precisely, fork-disciplined)

The count = the **realized real rank** of the Z/3-equivariant self-dual family space

>  `V  <=  Lambda^2_+(R^4) ~= R^3`,

where:
- `Lambda^2_+(R^4)` = self-dual 2-forms on the 4-base, `dim = 3` (the ceiling);
- the acting `Z/3` = the 3-Sylow summand of stable homotopy `pi_3^s = Z/24`, realized geometrically as an
  order-3 element of `SO(3) = SU(2)+` (the self-dual frame-rotation / self-dual gauge algebra), acting on
  `Lambda^2_+ = adjoint su(2)+`.

"Forcing" = the structure admits a **unique** realized rank. "Bounding" = the structure caps the rank (ceiling)
but admits more than one value.

This is deliberately the geometer's side of the fork: a Z-index cannot reach a Z/3 class (`Hom(Z/3, Z) = 0`,
H6), so the standard-physics index construction is provably blind to this count. Branch D asks whether the
*native* torsion construction, being reachable, can go further and FORCE.

---

## 2. The two anchor facts, reproduced independently

### 2a. `3 = dim Lambda^2_+(R^4)` (the ceiling)
Hodge star `*` on `Lambda^2(R^4)` (Euclidean) satisfies `*^2 = +1`; the `+1` (self-dual) eigenspace has
`dim = 3` (computed exactly: `||*^2 - I|| = 0`, signature `(3,3)` on `Lambda^2`). Independently,
`Lambda^2_+ ~= su(2)+`, the self-dual summand of `so(4) = su(2)+ (+) su(2)-`, and `dim su(2) = 3`. The "3" is
**derived from the 4-dimensionality of the base**, not imported. (No 24, no 24-8, no fit.)

### 2b. `Z/3 subset pi_3^s = Z/24` (the arena), three ways
1. **Image of J / Bernoulli.** `pi_3^s = im J = Z/24`; the order is the denominator of `B_2/(4) = (1/6)/4 =
   1/24`, i.e. `24 = 2^3 * 3`. 3-Sylow `= Z/3`.
2. **von Staudt-Clausen.** `denom(B_2) = prod{ p : (p-1) | 2 } = 2 * 3 = 6`; the prime **3 enters because
   `(3-1) | 2`**. This is the arithmetic origin of the Z/3.
3. **Adams alpha-family.** The first 3-torsion element `alpha_1` (image of J) sits in stable stem
   `2p - 3 = 3` for `p = 3`, and generates the `Z/3 subset pi_3^s`.

H6 reachability, restated: `Hom(Z/3, Z) = 0` (a Z-index is blind), but the order-3 element has 3-part `= 3`
(reachable). Branch D lives on the reachable side.

---

## 3. The order-3 action on `Lambda^2_+ = R^3` (the whole ballgame)

An order-3 element of `SO(3)` is a rotation by `2pi/3` about a fixed axis. An exact, integer model is the
cyclic coordinate permutation `g : (x,y,z) -> (y,z,x)`: `g^3 = I`, `det g = +1`, orthogonal, rotation by
`2pi/3` about the fixed axis `(1,1,1)`. Its eigenvalues are `{1, omega, omega^2}` (`omega = e^{2pi i/3}`):

- a **1-dim fixed axis** `V0` (eigenvalue 1, the trivial rep), and
- a **2-dim rotated pair** `V1` (the `omega, omega^2` conjugate pair, real-irreducible -- a genuine
  120-degree rotation has no invariant line in its plane).

So `R^3 = V0 (+) V1` as a real Z/3-representation: `trivial (+) standard`. The full-space **character is
`tr(g) = 1 + 2 cos(2pi/3) = 0`** -- this single fact drives the residue trap below.

---

## 4. The force-vs-bound analysis (5 personas, inline)

### Persona 1 -- stable-homotopy / torsion theorist: the invariant-subspace structure
The realized family space `V` must be a **real Z/3-invariant subspace** of `R^3`. Because `R^3 = V0 (+) V1`
with `V1` real-irreducible, the invariant subspaces are exactly the sub-sums:
`{0}, V0, V1, R^3` -- dims **`{0, 1, 2, 3}`** (computed in the test from the real-irreducible block
structure `[1, 2]`). The ceiling `dim Lambda^2_+ = 3` is saturated only by `V = R^3`; the fixed axis alone is
`V = V0`, rank 1.

**Oddness refinement.** Over C, `R^3 (x) C = C_1 (+) C_omega (+) C_{omega^2}`. A real (conjugation-stable)
subspace has **odd** real dim **iff** it contains the fixed line `C_1`. Hence the odd invariant ranks are
`{1, 3}`:
- rank 1 = `V0` = the **Z/3-neutral** family only (the SO(3) rotation axis);
- rank 3 = `V0 (+) V1` = neutral family **plus** the `omega/omega^2` **charged pair**.

So the located-not-forced `{1,3}` is exactly: *do you or do you not realize the charged pair on top of the
neutral fixed axis?*

### Persona 2 -- math referee: grade each claim
- `dim Lambda^2_+ = 3`; `R^3 = trivial (+) standard` under Z/3; invariant dims `{0,1,2,3}`; odd `= {1,3}`;
  `tr(g) = 0`; `R^3` irreducible under connected SO(3): **all THEOREM-grade** (elementary rep theory,
  reproduced exactly).
- "the count = realized rank of `V <= Lambda^2_+`" and "matter present => rank > 0" and "the family multiplet
  is the adjoint of the self-dual gauge SU(2)+": **ARGUED** (physical admissibility, not theorems).
- **BOUNDS vs FORCES flag:** the Z/3 action FIXES the ceiling (3) and, with oddness, the menu `{1,3}` -- these
  are bounds/menus. It does **not** single out a value. Any claim that Z/3 "forces 3" is a BOUND masquerading
  as a FORCING.

### Persona 3 -- adversary: attack the forcing claim
> "You want rank 3 = all of `Lambda^2_+`. But the fixed axis `V0` is a perfectly good Z/3-invariant subspace:
> nothing in the order-3 action forbids the realized content from being **exactly** the neutral fixed axis
> (rank 1). Did you assume the whole self-dual bundle is realized? That's the ceiling, i.e. the answer, smuggled
> as a premise. And if instead you demand the Z/3 act *irreducibly* (fixed-point-free) to look principled, you
> get `V1`, **rank 2** -- the wrong count. So your two 'natural' selectors give 1 (fixed axis) or 2
> (irreducible), never 3. Where does 3 come from that isn't 'realize everything'?"

This attack **stands**. The test's F6 confirms irreducibility mis-selects 2. The fixed axis survives every
order-3 condition.

### Persona 4 -- cross-checker: the residue trap, independently
Any selector that is a **class function** of the order-3 element `g` (a character, a mod-3 residue, an
equivariant/mod-3 index) evaluates the same on rank 3 as on the trivial sector:
- `tr(g | R^3) = 0` (the full-space character vanishes);
- a **net count of 3 has residue `3 = 0 (mod 3)`** -- *identical to the residue of the trivial/fixed-axis
  (rank-1) sector*.

So no order-3 class function can distinguish "3 generations" from "0 mod 3 / the neutral sector." This is the
same collision the repo's H39/H40 flagged (`net index 3 == 0 mod 3 == carrier-A residue`), reproduced here from
scratch on the bare `SO(3)` character. It is a genuine, class-wide obstruction to **certifying** 3 with any
order-3 datum.

### Persona 5 -- synthesizer: the verdict
The Z/3 torsion action **bounds** the count (ceiling `dim Lambda^2_+ = 3`; menu `{1,3}` with oddness) and
**cannot force** 3 over 1: the fixed axis is invariant and residue-indistinguishable. The only thing that turns
the bound into a forcing is **promoting the discrete order-3 element to the full connected group**:

> Under the **connected `SO(3) = SU(2)+`**, `R^3` is **irreducible**, so the only invariant subspaces are
> `{0, R^3}`. With matter present (rank `> 0`), this **FORCES rank 3.**

But `SO(3)` strictly contains `<g>`; the homotopy-torsion construction supplies only the `Z/3`. The forcing
therefore lives in a **different construction** (SU(2)+ as a continuous gauge symmetry), an added geometric
input beyond branch D's datum.

---

## 5. Graded verdict on {Q-force, Q-extra, Q-nogo}

| Question | Verdict | Grade |
|---|---|---|
| **Q-force** | **BOUNDS, does not FORCE.** Ceiling `dim Lambda^2_+ = 3`; Z/3-invariance gives `{0,1,2,3}`, oddness gives `{1,3}`; the rank-1 fixed axis stays admissible. The SO(3) order-3 action is a *bound*, not a *forcing*. | THEOREM (math core) |
| **Q-extra** | Minimal input to pin 3 = **promote the order-3 element to the full connected `SO(3)=SU(2)+`** (equivalently: the family multiplet is the *entire adjoint* of the self-dual gauge SU(2)+, i.e. realize all of `Lambda^2_+`). First-principles **iff** `SU(2)+` is a genuine continuous gauge symmetry -- but that is **strictly stronger** than the torsion datum, so **relative to branch D's construction it is a free/added choice, not forced.** | ARGUED |
| **Q-nogo** | **YES, class-wide** for order-3-equivariant selectors: (i) both `{1,3}` are Z/3-invariant, so invariance can't separate them; (ii) `3 = 0 (mod 3) =` trivial-sector residue and `tr(g)=0`, so **no order-3 class function certifies 3.** | THEOREM (given the construction) |

**The count-construction used:** torsion class in the 3-primary arena (`Z/3 subset pi_3^s = Z/24`,
`3 = dim Lambda^2_+`), acting as `SO(3)` on `Lambda^2_+ = R^3`.

**Does the Z/3 action FORCE rank 3 or only BOUND it?** Only **BOUND** (ceiling 3, realized `{1,3}`, rank-1
fixed axis admissible).

**Minimal extra input to pin 3 and its status:** the promotion `Z/3 -> connected SO(3)=SU(2)+`
(equivalently, realize the whole self-dual bundle / the full su(2)+ adjoint). First-principles *only if*
`SU(2)+` is an established continuous gauge symmetry; as an input to the *torsion* construction it is a free
add-on, because the torsion supplies just the order-3 element.

**Load-bearing assumption:** that "the count" = realized rank of a Z/3-invariant `V <= Lambda^2_+`, with the
acting group being exactly the discrete `Z/3` the torsion supplies (not more).

**The one overturning thing:** if `SU(2)+` is established as a *forced continuous* gauge symmetry of the
theory (its adjoint = `Lambda^2_+`, forced by the 4-base self-duality) rather than merely its order-3 subgroup,
then `SO(3)`-irreducibility of `R^3` forces rank 3 cleanly and branch D upgrades **BOUNDS -> FORCES**. Then the
generation number would be `3 = dim adjoint SU(2)+ = dim Lambda^2_+(R^4)`, first-principles. The entire verdict
hinges on **discrete order-3 vs continuous SO(3)** -- and the homotopy-torsion construction, by itself, gives
only the discrete one.

**Confidence:** HIGH on the located-not-forced (BOUNDS) result and the class-wide order-3 no-go (elementary,
reproduced exactly). MEDIUM on the Q-extra characterization being *the* minimal input (the SO(3) promotion is
the cleanest; a chirality/index-changing carrier declaration -- the repo's SG4/H39 route -- is an alternative
extra input living in a different arena).

---

## 6. Relation to prior in-repo results (independent reproduction, then beyond)

Reproduced independently: `3 = dim Lambda^2_+` (H38 Q1c), the `Z/3 subset pi_3^s = Z/24` arena (H6/H38), the
order-3 `SO(3)` action with fixed axis + rotated pair, and the residue collision `3 = 0 mod 3` = trivial
sector (H39/H40 Q3). **Beyond prior art**, branch D isolates the *exact* minimal extra input that would force
3 -- the **discrete-to-continuous promotion `Z/3 -> SO(3)`** -- and proves it is strictly stronger than the
torsion datum, sharpening "located-not-forced" into a precise statement of *what new structure* forcing would
require: not another discrete/torsion refinement (all of which hit the residue trap) but the full connected
self-dual gauge group. This is the honest located-not-forced result feeding the wave's no-go leg (E), with a
single named escape hatch (a forced continuous SU(2)+) for the forcing leg.
