---
artifact_type: exploration
status: exploration
created: 2026-07-07
title: "FB-F2 (the Adams e-invariant OBSTRUCTION, the universal-no-go leg finishing RS-S2's native-scope gap): is e_R=1/12 provably WITHOUT an integer index preimage, so 'count = e-invariant' is the same category error as Hom(Z/3,Z)=0 one level up? HONEST OUTCOME: GATED (with a genuine theorem-grade sub-result at KILL strength). PROVEN, machine-explicit: the e-invariant CLASS -- an element of Im J = Z/24 = framed bordism pi_3^s, equivalently a torsion element of Q/Z -- has NO integer preimage under ANY homomorphism (Hom(Z/3,Z)=Hom(Z/24,Z)=Hom(Z/n,Z)=Hom(Q/Z,Z)=0, all enumerated/certified); so 'generation count = e-invariant class' is a CONFIRMED category error, now at the FULL framed-bordism level, strictly containing the paper's Hom(Z/3,Z)=0 base case. The CRT split Z/24=Z/8(+)Z/3 is DERIVED (gcd(8,3)=1 cyclic; non-coprime control gcd(4,6)=2 fails), e_R=1/12 has order 12 in Q/Z, and its Z/3-summand carrier is the class 8 in Z/24 with e-value 1/3 (order 3, NONzero, NOT an integer) -- computed two independent ways (Q/Z primary split of the value 1/12 = 3/4 + 1/3, and CRT projection of the class 2). BUT the obstruction is against TORSION classes ONLY: a DISCRIMINATING obstruction test flags e_R/1/3/Z/24/Z/3/Z/8 and does NOT flag the signature, the Euler number, or the relative APS index (integers-by-construction, same invariant class as the signature) -- the task-mandated control passes, random-integer/random-Q/Z scramble passes. The decisive distinction: 'e_R has no integer PREIMAGE' (no hom Q/Z->Z hits it) is TRUE and theorem-grade; 'no integer index has fractional part e_R' is FALSE -- APS ind = bulk - e_R is an integer BY CONSTRUCTION for every geometry-dependent bulk of the form (integer + e_R), so the residue fixes ind mod 1 ONLY and neither forces 3 nor precludes an integer (located, not forced). The transparent-fiber ind = -1/12 (RS-S4) is the SINGLE bulk=0 instance, not a proof no bulk works. A KILL would require proving no geometry supplies the cancelling bulk -- a source-action GEOMETRY statement that e-invariant TOPOLOGY cannot reach. SIGNAL = GATED; the surviving integer-index route is named exactly: the unbuilt relative/equivariant twisted-Rarita-Schwinger (Dirac) index with nonzero geometry-dependent bulk = Section 9's gate, NOT the e-invariant, NOT obstructed by Hom(-,Z)=0."
grade: "exploration; the OBSTRUCTION sub-result is THEOREM-grade (Hom(Z/3,Z)=Hom(Z/24,Z)=Hom(Z/n,Z)=Hom(Q/Z,Z)=0 enumerated/certified; the Q/Z primary split 1/12 = 3/4 + 1/3 and the CRT class-projection to e-value 1/3 both exact; the CRT split derived from gcd(8,3)=1 with a discriminating non-coprime control). The DISCRIMINATION (torsion flagged, integer indices not) is machine-certified with the task-mandated signature/Euler/relative-APS control PASSING and a random-integer/random-Q/Z scramble PASSING. The route VERDICT is GATED, not KILL: pure e-invariant topology confirms the class-level category error but structurally cannot obstruct the relative index (an integer-by-construction invariant), whose existence-with-prescribed-residue is a general APS fact (enumerated: every integer n realizable via bulk = n + e_R). FROM-MEMORY flags: the Kirby-Melvin p_1=4 framing normalization for e_R (mitigated by the agreeing independent Adams class-2/24 route); |Im J_3| = denom(B_2/4) = 24 (Adams image-of-J / Bernoulli) measured, kept provenance-distinct from chi(K3)=24; the APS index identity ind = bulk - eta_defect (statement standard; its application to GU's actual twisted-RS operator is the unbuilt gate, asserted nowhere as built). TARGET-IMPORT GUARD at maximum strictness: {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8} never assumed, inserted, hardcoded, or divided by; 24 = denom(B_2/4) MEASURED, 24 = 8*3 a CRT fact from gcd(8,3)=1, e_R = 1/12 measured two ways, the order-3 carrier 1/3 computed not recalled; the Euler numbers chi(CP^2)=3 and chi(K3)=24 appear ONLY as discriminating controls (genuine integers that must NOT be flagged), never as answers. Every count stated 'mechanism/carrier M forces c', never 'GU forces c'. Internal tier: computed + self-adversarial (discriminating controls + scramble), not externally replicated or peer-reviewed. Run independently as the F2 leg of the 2026-07-07 swing."
depends_on:
  - papers/candidates/located-not-forced/located-not-forced-generation-count-2026-06-29.md
  - canon/h2-base-index-chirality.md
  - explorations/big-swing-2026-07-07/RS-S4-base-forcing-bismut-cheeger.md
  - explorations/big-swing-2026-07-07/RS-S2-relative-index-nogo.md
scripts:
  - tests/big-swing/fb_f2_adams_einvariant_obstruction.py
---

# FB-F2: the Adams e-invariant obstruction -- the universal no-go leg

**The swing.** The frozen `located-not-forced` paper (Section 9) states the single open bridge as
`order-3-class -> integer-3`, and already makes it algebraically explicit at the prime 3:
`Hom(Z/3, Z) = 0`, so a nonzero class in the `Z/3` summand cannot *be* an integer count. RS-S2 killed
the *native-carrier* transfer (the carrier's own twist is 3-inert, `m^2 == 1 (mod 3)`) but left a
native-scope gap and an external-import escape. RS-S4 pinned the two non-operator bridges and returned
GATED. **Route F2 attacks the universal statement directly**: is the Adams `e`-invariant `e_R = 1/12`,
carried by the image of `J` (`J: pi_3(SO) -> pi_3^s`, `Im J = Z/24` in dim 3), a `Q/Z`-valued
(fractional / torsion) invariant that **structurally has no integer index preimage** -- so identifying it
with an integer generation count is the *same* category error as `Hom(Z/3, Z) = 0`, **one level up** (at
the whole framed-bordism group `Z/24`, and at `Q/Z` itself)?

**Honest outcome: GATED**, carrying a **theorem-grade obstruction sub-result** at KILL strength for the
class-as-count identification. The e-invariant class provably has no integer preimage; but the
obstruction is against *torsion classes only*, and a genuine integer-index route (the relative /
equivariant twisted-RS index, an integer *by construction*) survives untouched. Pure e-invariant
topology cannot reach it.

All numbers below are printed by `tests/big-swing/fb_f2_adams_einvariant_obstruction.py` (run from repo
root, exit 0). Anchors reproduced first: `pi_3^s = Z/24` order `= denom(B_2/4)` (derived, homotopy
provenance), the CRT split `Z/24 = Z/8 (+) Z/3` (derived from `gcd(8,3)=1`), `e_R = 1/12` two ways, the
`L(2;1) = RP^3` reduced eta (`-1/8, +1/8`, 2-adic), the transparent-fiber APS value `-1/12`, and the
`12k` index.

---

## 1. The obstruction, laddered: `Hom(Z/3, Z) = 0` -> `Hom(Z/24, Z) = 0` -> `Hom(Q/Z, Z) = 0`

A homomorphism `phi: Z/n -> Z` is fixed by `phi(1)`, and `n * phi(1) = phi(0) = 0` in `Z` forces
`phi(1) = 0`. Enumerated over candidate `phi(1)`, the only valid homomorphism is `phi = 0`, for
**every** finite `n`:

| group | reading | `Hom(-, Z)` |
| --- | --- | --- |
| `Z/3` | the paper's Section-9 base case | `0` |
| `Z/24` | **one level up**: the whole framed-bordism group `pi_3^s` | `0` |
| `Z/8` | the selector summand | `0` |
| `Z/12` | the order of `e_R` | `0` |

And `Hom(Q/Z, Z) = 0`: every element of `Q/Z` has finite order (verified on a 406-element sample), `Z`
is torsion-free, a homomorphism sends finite-order to finite-order, and `0` is the only finite-order
element of `Z` -- so every `phi: Q/Z -> Z` is `0`.

**Consequence.** The `e`-invariant *class* -- an element of `Im J = Z/24`, equivalently a torsion element
of `Q/Z` -- has **no integer preimage under any homomorphism**. "generation count = `e`-invariant class"
is a **confirmed category error**, now at the full framed-bordism level, strictly containing the paper's
`Hom(Z/3, Z) = 0`. This is the promised "one level up."

---

## 2. The CRT split and the order-3 carrier: the count would live in `Z/3` as `1/3`, never as an integer

`pi_3^s = Z/24` splits, by CRT, into `Z/8 (+) Z/3` -- **derived**, not imported: `gcd(8,3) = 1` makes
`Z/8 (+) Z/3` cyclic of order 24; the discriminating non-coprime control `gcd(4,6) = 2` makes
`Z/4 (+) Z/6` (also order 24) *non*-cyclic, so the split is a genuine computation, not an assertion.

`e_R = 1/12` (from the gravitational framing `p_1/48` with `p_1 = 4` Kirby-Melvin *from-memory*,
cross-checked against the Adams class-`2/24`; the two agree) has **order 12** in `Q/Z` (2-adic valuation
2, 3-adic valuation 1). Its 3-primary content is computed two independent ways, agreeing:

- **`Q/Z` primary split of the value:** `1/12 = 3/4 (2-primary) + 1/3 (3-primary)` mod `Z`.
- **CRT projection of the class:** `e_R` = class `2` in `Z/24`; under `k <-> (k mod 8, k mod 3)` its
  `Z/3`-summand part is the class `8` (order 3), with `e`-value `8/24 = 1/3`.

So the homotopy-theoretic count, *if* it lives anywhere, lives in the `Z/3` summand as the class with
`e`-value **`1/3`** -- order 3, **nonzero**, and **not an integer**. `Hom(Z/3, Z) = 0` forbids the
class-to-count identification. The order-3 carrier is genuinely present and genuinely fractional.

---

## 3. The decisive discrimination: the obstruction flags torsion, **never** an integer index

This is the section that decides KILL vs GATED. The obstruction is against **torsion / `Q/Z`-valued
classes**; it must *not* touch an integer-by-construction index. A discriminating `is_obstructed` test
keys on the invariant **type** (and its arithmetic), never on the numeral:

| invariant | type | flagged? | correct? |
| --- | --- | --- | --- |
| `e_R` in `Q/Z` | torsion (`Q/Z`) | **FLAG** | yes -- no integer preimage |
| order-3 carrier `1/3` | torsion (`Q/Z`) | **FLAG** | yes |
| class 2 in `Im J = Z/24` | torsion (`Z/24`) | **FLAG** | yes |
| `Z/3`, `Z/8` summand classes | torsion | **FLAG** | yes |
| `signature(CP^2) = 1`, `signature(K3) = -16` | integer index | **safe** | yes -- integer by construction |
| `chi(CP^2) = 3`, `chi(K3) = 24`, `chi(S^4) = 2` | integer index | **safe** | yes -- a genuine integer, not torsion |
| **relative APS index** `bulk - eta_defect` | integer index | **safe** | yes -- same class as the signature |

The **task-mandated control passes**: the signature and the Euler number of a closed 4-manifold are
*not* flagged. (Note `chi(CP^2) = 3` and `chi(K3) = 24` are the exact numerals the guard forbids
*importing* -- here they appear only as *controls*, genuine integers the obstruction must leave alone,
never as answers.) A scramble control confirms the test is not blind: 40 random integers are never
flagged; 40 random `Q/Z` classes are all torsion.

**Because the relative APS index is an integer-by-construction invariant (the same invariant *class* as
the signature), the `e`-invariant obstruction structurally cannot reach it.** That is the crux.

---

## 4. Why KILL is not reachable: two different statements, one true and one false

- **(A) "`e_R` has no integer PREIMAGE"** -- no homomorphism `Q/Z -> Z` sends `e_R` to an integer.
  **TRUE**, and theorem-grade (Section 1).
- **(B) "no integer index has fractional part `e_R`"** -- **FALSE.** In the APS identity
  `ind = (bulk A-hat ch) - eta_defect`, `ind` is an integer **by construction**, and the
  geometry-dependent bulk can be any real of the form `(integer + e_R)`. Enumerated: for every
  `n in {-3..3}`, `bulk = n + 1/12` gives `ind = bulk - e_R = n`, an integer. The residue `e_R`
  constrains `ind` **mod 1 only**; it fixes neither *which* integer nor whether one exists. So `e_R`
  neither forces a particular integer (in particular **not 3**) nor precludes an integer -- exactly
  "located, not forced."

Conflating (A) and (B) is the subtle error the route exposes. The transparent-fiber value `ind = -1/12`
(RS-S4) is the **single** `bulk = 0` instance, not a proof that no bulk works. A KILL would require
proving that **no geometry** supplies a bulk making `bulk - 1/12` an integer -- a **source-action
geometry** statement that `e`-invariant **topology** cannot settle. Hence the obstruction does not close
the route.

---

## 5. Verdict, conjecture signal, and the named surviving route

**SIGNAL = GATED.**

- **Proven (theorem-grade sub-result, KILL strength for the class-as-count reading):**
  `Hom(Z/3, Z) = Hom(Z/24, Z) = Hom(Z/n, Z) = Hom(Q/Z, Z) = 0`. The `e`-invariant class (element of
  `Im J = Z/24`, torsion in `Q/Z`) has no integer preimage. The category error is confirmed **one level
  up** from the paper's `Hom(Z/3, Z) = 0`. The order-3 carrier is the class with `e`-value `1/3` in the
  `Z/3` summand -- nonzero, order 3, **not** an integer.
- **But (the discrimination):** the obstruction flags only torsion / `Q/Z` classes. The signature, the
  Euler number, and the relative APS index are integers by construction and escape it (controls pass).
  "`e_R` has no integer preimage" is true; "no integer index has fractional part `e_R`" is false.
- **KILL not reached:** closing the route needs a geometry claim (the unbuilt source-action bulk),
  outside `e`-invariant topology.

**Surviving integer-index route (named exactly).** The **relative / equivariant twisted-Rarita-Schwinger
(Dirac) index** on the framed-bordism carrier -- integer **by construction** (the same invariant class as
the signature), with a **nonzero geometry-dependent bulk** making `ind = bulk - e_R` an integer whose
residue is `e_R`. It is **not** the `e`-invariant and is **not** obstructed by `Hom(-, Z) = 0`. This is
precisely Section 9's gate (the unbuilt source action). The category error is confirmed at the class
level; the conjecture is **GATED**, not killed.

This **finishes RS-S2's native-scope gap universally at the topology level**: not only is the
*native-carrier* transfer 3-inert (RS-S2), the `e`-invariant *itself* -- for **any** framing, any
representative in `Im J` -- provably cannot *be* an integer count. What survives is exactly, and only,
an integer index whose *fractional part* is `e_R`, which is a geometry object, not an `e`-invariant one.
The two-arena picture is thereby made maximally sharp: the carrier arena's class is `Q/Z`-torsion (no
integer preimage, ever), and the only integer home is a relative index living in the free-abelian world
where `Hom` obstructions are silent -- the unbuilt object the paper already names.

---

## Honest gaps carried

1. **From-memory analytic inputs (flagged in-script):** the Kirby-Melvin `p_1 = 4` framing normalization
   for `e_R` (mitigated by the agreeing independent Adams class-`2/24` route); `|Im J_3| = denom(B_2/4)
   = 24` (Adams image-of-`J` / Bernoulli), kept provenance-distinct from `chi(K3) = 24`; and the
   *statement* of the APS index identity `ind = bulk - eta_defect`. Its application to GU's actual
   twisted-RS operator is the unbuilt gate, asserted as built nowhere here.
2. **The GATED verdict is a topology statement, not a geometry one.** F2 proves the class-level category
   error and proves that integer indices escape the obstruction; it does **not** build (or preclude) the
   geometry-dependent bulk. Whether GU's actual `Y14` source action yields an integer whose residue is
   `e_R` -- and whether that integer is 3 -- is the residual open object, unchanged.
3. **`is_obstructed` keys on invariant TYPE.** The discrimination is honest because the type distinction
   (torsion class vs free-abelian index) is exactly the mathematical content of `Hom(torsion, free) = 0`;
   the scramble and the signature/Euler/relative-APS controls certify it is not a fitted verdict. But it
   is a *classification* of invariant types, not a search over all conceivable invariants.
4. **Internal tier only:** computed and self-adversarial (discriminating controls + scramble), not
   externally replicated or peer-reviewed. Run independently as the F2 leg of the 2026-07-07 swing.

## Governance

Exploration-grade; **no edit to the frozen paper.** A promote/kill outcome is a **proposal** for the
paper's Section 9 that pauses for the maintainer. The proposed sharpening: the `Hom(Z/3, Z) = 0`
category error generalizes to the **whole framed-bordism group** -- the `e`-invariant class, for any
framing, has no integer preimage (`Hom(Z/24, Z) = Hom(Q/Z, Z) = 0`), so the class-as-count reading is
dead universally, not just at the prime 3; and the **only** surviving integer home is a
relative/equivariant index whose *fractional part* (not whose class) is `e_R`, which is the unbuilt
source action, structurally invisible to the `e`-invariant obstruction because it is a free-abelian
(integer-by-construction) invariant. The generation-count verdict is unchanged: **OPEN** (located, not
forced; the class-as-count reading now closed at the full framed-bordism level). `conjecture_signal =
GATED`. Any verdict/status flip pauses for Joe.
