---
artifact_type: exploration
status: exploration (5-persona inline team; analysis + computed grade)
created: 2026-07-11
title: "Path-3 Branch B (blind wave): the anomaly-inflow / boundary-localization construction of the generation count. Verdict: inflow LOCATES & QUANTIZES the count (to Z, via winding/Chern/level) but does NOT FORCE it; its only forced constraint is 2-primary parity; by Hom(Z/3,Z)=0 the standard inflow invariant provably cannot reach the 3-primary count. Q-extra = the bulk data (the free input). Class-wide no-go for the physics-side inflow invariant; a torsion-refined (Dai-Freed / bordism) inflow invariant is the only inflow object that could reach 3-primary, and its forcing is the OPEN global question."
grade: "COMPUTED / analysis. tests/W56_path3_B_anomaly_inflow.py (exit 0, 10/10 checks, deterministic, no RNG). Standard physics (Nielsen-Ninomiya doubling; Jackiw-Rebbi/Kaplan domain-wall winding; Callan-Harvey local inflow parity; theta-level quantization) plus two elementary number-theoretic obstructions (Hom(Z/3,Z)=0, Hom(Z/3,Z/2)=0). No canon / RESEARCH-STATUS / claim-status / verdict movement; the generation count stays OPEN."
construction_of_the_count: "net chirality of fermions localized on a defect/boundary, fixed by anomaly inflow from a bulk topological term (Callan-Harvey; Kaplan domain-wall; Jackiw-Rebbi; Nielsen-Ninomiya closed-side no-go). Boundary invariant = domain-wall winding / bulk Chern number / bulk theta-level."
depends_on:
  - GEOMETER-VS-PHYSICS-OBJECTS.md
  - explorations/no-net-chirality-without-a-boundary-2026-07-10.md
  - explorations/nielsen-ninomiya-domain-wall-records-as-rows-2026-07-10.md
  - explorations/anomaly-and-bordism/sm-as-boundary-cobordism-frontier-2026-07-03.md
  - explorations/path3-generation-count-forcing-wave-design-2026-07-11.md
scripts:
  - tests/W56_path3_B_anomaly_inflow.py
---

# Path-3 Branch B: does anomaly inflow FORCE the generation count?

Blind branch B of the "why three generations?" wave. This branch attacks the count as a
**boundary-localized** quantity set by **anomaly inflow** from a higher-dimensional bulk. The five
personas run inline, sequentially, in one context. I reproduced the repo's prior
`no-net-chirality-without-a-boundary` and `sm-as-boundary-cobordism-frontier` logic independently
before building on it; where I lean on those results I re-derived their load-bearing step in the test.

**Fork discipline (required by `GEOMETER-VS-PHYSICS-OBJECTS.md`).** The count has two rival
constructions: the *physics* one (an **integer index** -- a Chern number, a winding, a Dirac index)
and the *geometer's* one (a **torsion class** in the 3-primary arena `Z/3 subset pi_3^s = Z/24`,
where `Hom(Z/3,Z)=0` makes a Z-index provably unable to reach it). Anomaly inflow, in its standard
(Callan-Harvey / Kaplan) form, produces an invariant on the **physics side** -- an integer degree /
Chern / level. I state this explicitly because it is the whole story: the branch's boundary invariant
is a physics-side integer, and that is exactly why it locates but cannot force the geometer-side count.

---

## Persona 1 -- the ANOMALY-INFLOW THEORIST: the bulk term and the boundary invariant

**The inflow setup.** Take a bulk topological term whose boundary variation reproduces the boundary
fermion anomaly. The canonical choices, all one mechanism:

- **Bulk theta-term (4d):** `S_bulk = (k/8pi^2) integral Tr F^F`. By descent `d(CS_3) = Tr F^F`, a
  gauge variation localizes on the boundary as precisely the consumed/produced chiral anomaly
  (Callan-Harvey 1985). The coefficient `k` (equivalently `theta`, with `theta ~ theta+2pi`) is
  **quantized to Z** by large-gauge invariance.
- **Mass domain wall (Kaplan 1992; Jackiw-Rebbi 1976):** a complex mass `m(x)=m1(x)+i m2(x)` that
  winds around 0 across the wall binds `|w|` net chiral zero modes, where `w` is the **winding
  number** (degree of the map `boundary-sphere -> vacuum manifold`).
- **Callan-Harvey axion string / Chern insulator:** the localized net chirality equals the **bulk
  Chern / instanton number**.

**The boundary invariant that counts the localized chiral modes** is, in every case, the same kind of
object: a **Z-valued integer** -- a winding, a Chern number, or a level. That identification is the
load-bearing input, and it is checked three ways in the test:
- `[1]` **Closed side (Nielsen-Ninomiya):** on a compact BZ, net chirality `= 0` (fermion doubling).
  A boundary is *necessary* for any nonzero count; the continuum/open control gives net `+1`.
- `[2]` **Inflow escape + quantization:** a single wall carries net chirality `= w`; computed for
  `w = 1,2,3 -> counts 1,2,3`. The count is quantized to Z, but its **value is the chosen winding**.
- `[3]` **Level quantization:** `exp(i 2pi k)=1` selects `k in Z`; every integer level is admissible.

## Persona 2 -- the MATH REFEREE: grade each claim, LOCATES vs FORCES

| claim | grade | LOCATES or FORCES |
|---|---|---|
| Net chirality = 0 on a closed structure (NN / Theorem 2) | **theorem** (standard; finite-dim Krein version rigorous) | constrains the *closed* count to 0 |
| A boundary carries net chirality = bulk invariant (bulk-boundary correspondence) | **theorem** (standard) | LOCATES the count at the boundary |
| The boundary invariant is Z-valued (winding/Chern/level) | **theorem** (standard) | quantizes to Z; **does not force a value** |
| The *value* equals the winding/level we chose | **theorem, but the choice is free** | this is the LOCATES-not-FORCES line, made explicit |
| Anomaly-free `=>` net count even (2-primary) | **theorem** (`q^2 == q mod 2`; basis-free) | forces PARITY only, in the wrong arena |
| `Hom(Z/3,Z)=0`, `Hom(Z/3,Z/2)=0` | **theorem** (elementary) | the integer/parity invariant CANNOT reach the 3-primary count |

**Referee flag.** Every "forcing" the branch can muster is a forcing of *integrality* or of *parity*.
Neither is a forcing of a **value**, and neither lives in the **3-primary** arena where the count
lives. The distinction "integer index (`Z` / 2-primary) vs torsion class (3-primary)" is exactly the
place a careless argument would blur; it is not blurred here.

## Persona 3 -- the ADVERSARY: "you chose the answer"

The pre-registered trap: *the bulk topological term / the domain-wall target topology is itself the
free input that secretly chooses the count.* The adversary is **correct**, and the test makes the
concession explicit rather than hiding it:
- To get count 3 you pick winding `w=3` (a degree-3 profile) `[2]`, or level `k=3` `[3]`, or a
  domain-wall target whose relevant homotopy group supplies a 3. Each of these is a **free choice of
  bulk data**; none is selected by any inflow consistency condition. Choosing 3 **assumes the answer**.
- The only genuinely *forced* datum -- parity (anomaly-freedom forces even) -- is not merely
  non-3-selecting; it is in the **2-primary** arena, coprime to the 3-primary count (`[4]`,`[5]`). So
  inflow does not even push *toward* an odd count; if anything its one forced constraint is *even*.

The adversary's attack therefore **succeeds against forcing** and the branch concedes: inflow
**quantizes given a choice**; the choice is Q-extra.

## Persona 4 -- the CROSS-CHECKER: reproduce a known inflow result and check parity

Two independent reproductions, both in the test, both deterministic:
1. **Nielsen-Ninomiya doubling** (the closed-side no-go): naive 1d lattice fermion `E(k)=sin k` has
   zeros at `k=0` (`+1`) and `k=pi` (`-1`), **net 0** -- reproduced from scratch (midpoint grid,
   circular wrap). Matches the repo's `nn_domain_wall_records_as_rows.py` result independently.
2. **Callan-Harvey local-inflow parity** (reproducing `sm-as-boundary-cobordism-frontier-2026-07-03`
   from a clean enumeration): over all 4-Weyl anomaly-free multiplets (`A_grav=sum eps=0`,
   `A_gauge=sum eps q^2=0`), the achievable net count `Nhat=sum eps q` is **always even**, and **all
   three residues mod 3 are reachable**. The parity is proved basis-free: `q^2-q=q(q-1)` is even, so
   `A_gauge == Nhat (mod 2)`. **Independently confirms** the prior result: local inflow constrains the
   count entirely within the 2-primary arena and is blind to mod-3.

**Parity check verdict:** the inflow-forced structure is 2-primary. This is the concrete, computed
form of the `GEOMETER-VS-PHYSICS` note that "odd (mod-2) != the count (mod-3)": inflow's forcing is
even worse than "odd" -- it is *parity*, coprime to the count.

## Persona 5 -- the SYNTHESIZER: verdict

**Construction of the count used:** net chirality of defect/boundary-localized fermions, fixed by
anomaly inflow from a bulk topological term (Callan-Harvey / Kaplan / Jackiw-Rebbi, with the NN
closed-side no-go). **Boundary invariant:** the domain-wall winding / bulk Chern number / bulk level
-- a **Z-valued integer** (physics-side construction).

- **Q-force -- CONSTRAINS, does not FORCE.** Inflow forces (i) a boundary to *exist* for any nonzero
  count (NN), (ii) the count to be **Z-quantized** (winding/Chern/level integrality), and (iii) under
  anomaly-freedom, **even parity** (2-primary). It forces **no value** and, in particular, does not
  force 3, or odd, or 3-primary. It **locates and quantizes**; it does not force.
- **Q-extra -- the BULK DATA, a free choice.** The minimal extra input that pins 3 is the bulk
  topological datum: the level `k=3`, the winding `w=3`, or a domain-wall target whose relevant
  homotopy supplies a 3. This is a **free choice, not a first-principles consistency condition** --
  exactly the pre-registered trap. (The one first-principles condition inflow *does* impose --
  anomaly-freedom -- lands in the 2-primary arena and cannot select the count.)
- **Q-nogo -- YES, class-wide, for the standard (physics-side) inflow invariant.** Its boundary
  invariant is Z-valued (Chern/winding/level) or mod-2 (parity). By `Hom(Z/3,Z)=0` and
  `Hom(Z/3,Z/2)=0`, **no such invariant can force the 3-primary count.** This is the H6 obstruction
  restated on the boundary side, and it is class-wide over all integer/parity inflow selectors.

**The fork caveat (where the no-go stops).** The no-go is derived in the **physics** construction of
the inflow invariant (an integer index). It does **not** transfer to a **torsion-refined** inflow
invariant -- a **Dai-Freed eta-invariant** / an `Omega^Spin_*` (or framed `Omega^fr_3 = pi_3^s =
Z/24`) **bordism** class -- which lives in a group *with* 3-torsion (`Z/24 >= Z/3`). That is the
**only inflow-type object that could reach the 3-primary arena**, and it is the geometer's side. The
local inflow computed here is provably blind to it (`[4]`,`[5]`). Whether the torsion-refined inflow
invariant **forces the value 3** is the **OPEN global bordism / Dai-Freed question** -- and even if a
Z/3 *class* were forced, the `order-3-class -> integer-3` bridge (the number of generations *as an
integer*) is separately open (per `no-net-chirality-without-a-boundary`). This branch does not close
either; it sharply localizes both.

**Confidence.** HIGH on Q-force (constrains-not-forces) and the class-wide Q-nogo for the physics-side
invariant -- these are theorems (`Hom(Z/3,Z)=0` and the parity identity are elementary and computed).
MEDIUM-HIGH that the torsion-refined route is the *only* inflow escape (it is the standard
Dai-Freed/bordism refinement; I did not exhaust exotic bulk constructions).

**Load-bearing assumption.** That the boundary invariant of *standard* anomaly inflow is a Z-valued
integer (winding/Chern/level). This is the physics-side identification; it is what the whole no-go
rests on, and it is exactly the fork the geometer's torsion refinement would step around.

**The one overturning thing.** Exhibit an inflow construction whose boundary invariant is
**intrinsically 3-primary and forced** -- i.e. a bulk term whose *consistency* (not a free level/
winding choice) requires the boundary defect to carry a class of order 3, with the value pinned. The
natural candidate is a Dai-Freed / `Omega^{Spin-G}_5` anomaly whose vanishing *forces* a Z/3 boundary
piece per the actual gauge/bordism data -- if such a construction pins 3 without importing it, Q-force
flips. Absent that, inflow quantizes-given-a-choice.

---

## Honest scope (what is and isn't established)

- **Established (theorem/computed):** the closed-side no-go (NN); inflow locates the count at a
  boundary and quantizes it to Z; the *value* is a free winding/level; anomaly-freedom forces only
  2-primary parity; and `Hom(Z/3,Z)=Hom(Z/3,Z/2)=0` makes the standard inflow invariant unable to
  reach the 3-primary count. All in `tests/W56_path3_B_anomaly_inflow.py` (exit 0, 10/10, no RNG).
- **NOT established:** that inflow forces 3 (it does not); that the torsion-refined inflow invariant
  forces 3 (open); the `order-3-class -> integer-3` bridge (open). No claim that any construction
  *produces* the physical count 3.
- **No movement:** canon, RESEARCH-STATUS, claim-status, verdicts, and the generation count are all
  unchanged; the count stays OPEN. Exploration/analysis grade.

## Not claimed

Not a derivation of three (or any) generations; not a proof that a torsion-refined inflow invariant
cannot force 3 (only that the *integer/parity* invariant cannot); not a metric. A graded, reproducible
demonstration that anomaly inflow **locates and quantizes** the count on the physics side but does not
force it, with the exact free input (the bulk data) and the exact fork (physics-integer vs
geometer-torsion inflow invariant) named.
