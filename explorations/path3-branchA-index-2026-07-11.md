---
title: "Path-3 Branch A -- the Atiyah-Singer index / Dirac construction of the generation count: what it FORCES, where it DIES (Hom(Z/3,Z)=0), and whether any torsion-valued index EVADES the death"
status: exploration
doc_type: exploration
created: 2026-07-11
grade: "COMPUTED / exact (tests/W55_path3_A_index.py, all checks exit 0). GU-independent arithmetic core (Hom-vanishing, KO torsion type, e-invariant order) verified from cited census facts; the GU-facing 'built eta is 2-primary' leg is reconstruction-tier (in-repo boundary-eta computations). No claim-ledger / RESEARCH-STATUS / verdict change; the generation count stays OPEN."
branch: "A -- Atiyah-Singer index / Dirac (blind multi-team wave, path 3, 'why three generations?')"
construction_of_count: "TORSION class in pi_3^s = Z/24 = Z/8 (+) Z/3; carrier = 3-Sylow Z/3 (geometer's side of GEOMETER-VS-PHYSICS row 'Generation count')"
scripts:
  - tests/W55_path3_A_index.py
---

# Path-3 Branch A: the index / Dirac route to the generation count

**Blind-wave discipline.** This is one branch of a multi-team wave attacking "why three
generations?" from different constructions of *what the count is*. This branch alone reports;
it does not synthesize across branches. Below, a 5-persona team ran inline (Index Theorist ->
Referee -> Adversary -> Cross-Checker -> Synthesizer) over a single computation.

**Construction of "the count" used (fork discipline, `GEOMETER-VS-PHYSICS-OBJECTS.md`).** The
row *Generation count* records a settled fork: the physics default is *a Z-valued index*
(Dirac / Atiyah-Singer / a signature); the program-native object is *a torsion class in the
3-primary arena* `Z/3 subset pi_3^s = Z/24`. This branch does the honest thing the fork
demands: it takes the count on the **geometer's (torsion) side** -- that is where the prior
program *located* it (Adams `e_KO` reaches it) -- and asks precisely how far the physics-default
**index** can go toward it. The whole branch is the map of that boundary.

---

## 1. INDEX THEORIST -- what the index route forces, and the exact computation

**The forced content ("no net chirality without a boundary").** Net chirality of a Weyl fermion
is the index of a chiral Dirac operator, `ind D = dim ker D_+ - dim ker D_-`, an additive,
`Z`-valued homomorphism out of the K-theory class of the fermion content. As an anomaly-inflow
coefficient it is the statement that a nonzero net chirality on a boundary is the inflow of a
bulk SPT term -- equivalently, on a *closed* even manifold the net chirality is a *characteristic
number* (an integral of the index density), fully forced by topology. That is real forcing: the
integer is pinned. What it pins, on the closed pieces, is **2-primary-locked**:

- Closed spin 4-manifold, `p1 = 3 sigma` (signature theorem, universal):
  - Dirac: `ind D = A-hat = -p1/24`. On K3: `-(-48)/24 = 2`. Integer, in `Z`.
  - Rarita-Schwinger (spin-3/2, AGW density `(ch(TM_C)-1) A-hat`, degree-4 = `7 p1/8`):
    `= 21 sigma/8`. On K3: `-42`.
- **`21 sigma/8 == 0 (mod 3)` for every spin 4-manifold** -- the factor `21 = 3.7` forces it to
  the `Z/3` *identity*. The "3" that appears is the `p1 = 3 sigma` signature multiplicand (and the
  `3 | 24` denominator divisor), **never a mod-3 value the index takes**.

So the index *forces an integer* and *constrains 2-primary + parity data*; it never produces a
nonzero element of order 3.

**Where it dies.** The count carrier is the 3-Sylow `Z/3 subset Z/24`. An integer index is a
homomorphism into `Z` (torsion-free). `Hom(Z/3, Z) = 0`: a finite-order class maps only to a
finite-order element of `Z`, and the only one is `0`. Restricted to the count carrier every
`Z`-valued index is **identically zero**. This is the precise death point -- not a hard
computation that came out unfavourable, but a *type* mismatch: `Z` cannot host order-3 data.

**Torsion-refinement escape probe.** The question the fork actually poses: is there an index
*of a different value type* that reaches `Z/3`? Enumerate the standard refinements:

| index refinement | value group `V` | `Hom(Z/3, V)` | reaches `Z/3`? |
|---|---|---|---|
| Atiyah-Singer / twisted Dirac / signature | `Z` (free) | `0` | **no** (the death) |
| KO^{-n}(pt) real / KO-theoretic index | `Z` or `Z/2` (torsion all 2-primary) | `0` | **no** |
| mod-2^k index (Rokhlin `Z/16`, Witten `Z/2`, ABS `2^m`) | finite 2-group | `0` | **no** |
| mod-k Freed-Melrose index (`Z/k`-manifold) | `Z/k` | `gcd(3,k)` | **yes iff `3|k`** (needs order-3 datum) |
| reduced eta / APS / Adams `e`-invariant | `R/Z = Q/Z` | nonzero | **yes** (`e_KO(8nu)=1/3`, order 3) |

Two refinements genuinely evade the death: the **`R/Z`-valued reduced eta / Adams `e`-invariant**
(`e_KO(nu) = 1/24 => e_KO(8nu) = 1/3`, a real order-3 element -- this is exactly the object that
*located* the carrier), and the **mod-`3k` Freed-Melrose index**. Everything torsion-free or
`KO`/2-group-valued stays blind.

---

## 2. MATH REFEREE -- grading each claim, LOCATES-vs-FORCES, integer-vs-torsion

- **Theorem (unconditional):** `Hom(Z/3, Z) = 0`; hence every additive `Z`-valued index is
  blind to the 3-Sylow. **Grade: proven, GU-independent.** (Matches the H6 family-puzzle theorem
  contrapositive and the KO-ladder disjointness core; reproduced here independently.)
- **Theorem (cited census):** `KO^{-n}(pt)` torsion is all `Z/2` (Bott song `Z, Z/2, Z/2, 0, Z,
  0,0,0`); so `Hom(Z/3, KO-tors) = 0`. **Grade: proven-by-type.**
- **Theorem (cited):** `e_KO(nu) = 1/24` (Adams, nLab), `e_KO(8nu) = 1/3` has order 3. So the
  `R/Z` eta *reaches* `Z/3`. **Grade: proven the class is reachable.** This is a **LOCATES**
  statement, flagged as such -- it separates the class from 0, it does **not** hand back the
  integer 3.
- **Blur flag (integer-vs-torsion), caught:** "the index gives 24, so 3 | 24, so 3 generations"
  is the category error. `24` (or the denominator `24`, or `p1 = 3 sigma`) carries `3` as a
  *factor/multiplicand*; the count needs `3` as a *value of order 3 in `Z/3`*. CRT-disjoint
  requirements: an integer that *equals* `3` is `0 mod 3` (identity, zero order-3 content); an
  integer that is a *unit* mod 3 encodes count `1`. No integer is simultaneously "the number 3"
  and "a `Z/3` generator." (Reproduced in `rs_index_carrier_arena_scan.py`; re-derived here.)
- **Blur flag (LOCATES-vs-FORCES), caught:** even the escaping `R/Z` eta only *locates*. Reading
  the integer `3` off an order-3 class is `Hom(Z/3, Z) = 0` **again** -- the death reappears at
  the class->integer step. So "reaches the arena" must never be reported as "forces 3."

---

## 3. ADVERSARY -- did you smuggle in a torsion index that does not exist for this operator?

Three attacks, each answered honestly:

1. *"The `e`-invariant is your torsion index -- doesn't that force 3?"* No. `e_KO` is a genuine
   `R/Z`-valued spectral invariant (a reduced eta), and it genuinely reaches `Z/3`. But (i) it
   *locates* the class, it does not read off the integer; (ii) its nonzero order-3 *value on the
   actual GU boundary operator* is **not** established -- every in-repo built eta
   (`gen_aps_eta_actual_operator.py` round-`S^3` end -> `eta = 0`; charge-`q` lens
   `(2q^2-4q+1)/8` -> 2-primary for all `q`) comes out `0` or 2-primary. The order-3 value is
   *gated* on the unbuilt twisted RS source action. So the escape is *arithmetically available*
   but *not exhibited* on this operator. No smuggling: I mark it reachable-in-principle,
   not-yet-nonzero-in-fact.
2. *"The mod-3 Freed-Melrose index -- free lunch?"* No. A `Z/k` index needs a `Z/k`-**manifold**
   (a geometric order-`k` datum: a `Z/k`-Bockstein bounding structure, or an order-3 group action
   / lens boundary). That datum is **extra input**, not supplied by the Dirac operator. It is
   partly first-principles (GU's noncompact end genuinely has an `RP^3 = L(2;1)` lens spine -- a
   `Z/2` datum, not `Z/3`), so the *specific* order-3 datum is not native and remains a free
   choice pending a `3|k` structure on the actual end.
3. *"KO / real index -- you dismissed it too fast."* Re-checked: `KO^{-n}(pt)` torsion is `Z/2`
   in every degree it is nonzero. `Hom(Z/3, Z/2) = 0`. The `KO`-theoretic index cannot reach
   `Z/3`. (The `KO` *`e`-invariant* does -- but that is the `R/Z` eta of attack 1, an analytic
   secondary invariant, not a `KO^{-n}` index group element.) Confirmed blind.

**Adversary verdict:** no fabricated operator. The one genuinely reaching invariant (`R/Z` eta)
is real, is the program's known locator, and is honestly gated on the operator side.

---

## 4. CROSS-CHECKER -- independent reproduction of `Hom(Z/3,Z)=0` and a known index

- **`Hom(Z/3, Z) = 0` two independent ways:** (i) `|Hom(Z/n, Z/m)| = gcd(n,m)`, and for the free
  target `Hom(finite, Z) = 0` (a finite-order generator must map to a finite-order integer, i.e.
  `0`); (ii) explicit no-separator -- model an index as `phi: Z/24 -> Z`, `phi(k) = kt`; a hom
  needs `24t = 0` in `Z`, forcing `t = 0`, so `phi(8) = 0` for the order-3 class `c3 = 8`. Both
  in `W55_path3_A_index.py`, both PASS. Matches `H6_family_puzzle_theorem.py` Q3b and the
  KO-ladder disjointness core independently.
- **Known index cross-check (the standard family-index anomaly):** the AGW spin-3/2 anomaly
  density on `K3` gives `RS index = 7 p1 / 8 = -42 = -2.3.7`. The lone factor 3 there is the
  `p1 = 3 sigma` signature coefficient (via `2 chi + 3 sigma = 0` it also equals `-2 chi`
  numerically) -- a *disguised signature/Euler* `3`, `== 0 (mod 3)`, i.e. it lands at the `Z/3`
  identity. The `HP^2` case gives a *unit* (`e_KO`-escape value `1`, count `1`). Reproduced: the
  net-chiral integer index is *always* `0 mod 3` or a unit, **never** an order-3 carrier.
  Consistent with `rs_index_carrier_arena_scan.py`.

Cross-checker: obstruction and known index both reproduce; no discrepancy.

---

## 5. SYNTHESIZER -- graded verdict

**Construction of the count:** torsion class in `pi_3^s = Z/24 = Z/8 (+) Z/3`, carrier = 3-Sylow
`Z/3` (geometer's side of the settled fork). The index is the physics-default object probed
against it.

- **Q-force -- does the index FORCE 3?** **No.** The integer Atiyah-Singer / Dirac index forces
  an *integer* net chirality in `Z` (an anomaly-inflow coefficient) and constrains 2-primary /
  parity data; on closed spin 4-manifolds it is `== 0 mod 3` (`p1 = 3 sigma`), i.e. blind to the
  mod-3 count. It **constrains, does not force**. *(Grade: proven.)*

- **Q-extra -- minimal extra input to pin 3.** To even *reach* the `Z/3` arena the index must be
  **torsion-valued**: the `R/Z`-valued reduced eta / Adams `e`-invariant (`e_KO(8nu) = 1/3`,
  order 3 -- the program's locator), or a mod-`3k` Freed-Melrose index (requires an order-3
  geometric datum: a `Z/k`-manifold structure, `3|k`). But *reaching is not forcing*: (i) reading
  the integer `3` off the order-3 class is `Hom(Z/3, Z) = 0` again (ill-typed, open); (ii) on the
  actual GU boundary operator the eta is computed `0` / 2-primary in every built case, the nonzero
  order-3 value gated on the unbuilt twisted RS source action. **The `R/Z`-eta refinement is a
  first-principles object** (it is the canonical secondary invariant of the same Dirac operator);
  **the order-3 geometric datum a mod-3 index needs is NOT native** to the (`Z/2`-lens) GU end and
  is a free choice as things stand. Net: no minimal extra input *forces* 3; the strongest
  reachable statement is *locate*. *(Grade: reachable proven; forcing open.)*

- **Q-nogo -- can you prove no selector of your kind forces 3?** **Class-wide no-go PROVEN for the
  two sub-classes:** torsion-free integer indices (`Hom(Z/3, Z) = 0` -- Dirac, twisted-Dirac,
  signature, any `Z`-valued net chirality) and `KO^{-n}` indices (`KO` torsion 2-primary). It is
  **not** a no-go over the *whole* index family: the `R/Z`-eta and mod-`3k` refinements genuinely
  evade the death (reach `Z/3`). So the death is a property of the *value type* (torsion-free /
  2-primary), not of "indices" writ large. *(Grade: no-go proven for the Z-valued and KO-valued
  sub-classes; the torsion-valued sub-class is not blocked -- but it only locates.)*

**Whether a torsion-valued index evades `Hom(Z/3,Z)=0`:** **YES** for reduced-eta / Adams
`e`-invariant (`R/Z`) and mod-`3k` Freed-Melrose; **NO** for `KO^{-n}` and every torsion-free
integer index. The evasion buys *location of the class*, not the integer.

**Confidence:** HIGH on the arithmetic core (Hom-vanishing, KO-torsion type, `e`-invariant order
-- exact, cited, exit-0). MEDIUM on the GU-facing "built eta is 2-primary / order-3 is gated" leg
(reconstruction-tier, resting on the in-repo boundary-eta computations and the unbuilt RS source
action).

**Load-bearing assumption:** that the count genuinely *lives* in the 3-primary torsion arena
`Z/3 subset pi_3^s` (the located-not-forced localization). If that localization is wrong -- if the
count is actually an integer-index quantity after all -- this entire branch's "death" dissolves
and the ordinary Dirac index is back in play.

**The one thing that would overturn it:** exhibiting a **specific Dirac-type operator on the
actual GU geometry whose reduced eta / `e`-invariant takes a nonzero order-3 value AND a
first-principles class->integer reduction pinning `3`** -- i.e. building the gated twisted RS
source action and showing its APS eta lands at `1/3` (not `0`, not 2-primary) together with a
canonical order-3-class -> integer-3 map. That would turn "locates" into "forces" and overturn the
Q-force / Q-extra verdicts in one stroke.

---

## Deliverables

- Test: `tests/W55_path3_A_index.py` (encodes the `Hom(Z/3,Z)=0` death + the KO / mod-k / eta
  reachability checks + the closed-manifold 2-primary-lock; exit 0, all PASS).
- This exploration: `explorations/path3-branchA-index-2026-07-11.md`.

No canon / RESEARCH-STATUS / claim-status / verdict change. The generation count stays **OPEN**;
this branch sharpens *where and why* the index route can and cannot reach it.
