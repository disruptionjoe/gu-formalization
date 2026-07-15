---
artifact_type: exploration
label: W221
created: 2026-07-14
posture: FALSIFICATION wave, NON-NAIVE mode; assume-GU-correct + grant-every-unbuilt-piece; exploration grade; truth-seeking (report either way, do not root); RUTHLESS skeptic; tri-repo gating STRICT
title: "W221 VERDICT: SURVIVES (structure does NOT force an even/2/4 count). Attacking the generation-count = 3 leg NON-NAIVELY: grant every unbuilt piece and ask only whether GU's ACTUAL rep-theory structure FORCES a count INCOMPATIBLE with three. Two bounded objects computed from first principles (weight combinatorics + ABS periodicity), not asserted: (a) the H-line count -- Cl(9,5) = M(64,H) quaternionic, S=H^64, S+=H^32, one generation = 8 H-lines; the spin-1/2 leg gives 2 generations = 16 H-lines, and 3 generations = 24 H-lines is a valid integer H-submodule, so the quaternionic structure does NOT forbid the 2+1 assembly (it constrains H-line counts, not generation counts, to be H-integer). (b) the Rarita-Schwinger branching RS(3,1) (x) S(6,4): S(6,4) = C^16 (Cl(6,4) index 2 => M(16,C)) is the Spin(6,4) Weyl spinor; under the maximal compact Spin(6)xSpin(4) = SU(4)xSU(2)xSU(2) (Pati-Salam) it branches, FORCED by the spinor-tensor split S+(10) = S+(6)(x)S+(4) (+) S-(6)(x)S-(4), into (4,2,1) (+) (4bar,1,2) = 8+8 = 16 Weyl = exactly ONE SM generation. Classified against {16 -> total 3 | 0 -> total 2 | 32 -> total 4}: the content is 16, NOT 0 and NOT 32; the flipped-chiral RS imposter S-(10) is also 16; RS is SM-charge-blind so it contributes +1 generation. Total = 2 + 1 = 3. The PRE-DECLARED FAILURE CONDITION (RS branching = 0 or 32, or H-line forbids 2+1) is NOT met. The residual -- the count VALUE still needs an external Z/3 self-dual import (W201/W218: R_src is K-null/index-conserving/vectorlike) -- is a GAP, i.e. SURVIVES-WITH-A-GAP, explicitly NOT a falsification. Test tests/W221_falsify_generation_count_structure.py 25/25 exit 0, positive controls first."
grade: "EXACT / machine-checkable (25/25, deterministic, tests/W221_falsify_generation_count_structure.py) for the bounded rep-theory facts: the ABS Clifford periodicity types (Cl(9,5) index 4 quaternionic M(64,H); Cl(6,4) index 2 complex M(16,C)); the Weyl-spinor dimensions from weight combinatorics (S+(4)=S-(4)=2, S+(6)=4, S-(6)=4bar, S+(10)=16); the FORCED chirality-correlated branch S+(10) = S+(6)(x)S+(4) (+) S-(6)(x)S-(4) = (4,2,1) (+) (4bar,1,2) with no wrong-chirality leak; the resulting one-S(6,4) internal Weyl content = 16; the flipped-chiral S-(10) = 16; and the trichotomy classification 16 vs {0,32}. STRUCTURAL / RECONSTRUCTION for: the identification of S(6,4) with the GU fiber spinor and of RS(3,1) as the SM-charge-blind Lorentz factor (from generation-count-sm-branching-closure and the Weinstein transcript); the H-line-per-generation = 8 accounting; the physical claim that RS multiplicity in the ZERO-MODE count is exactly 1 (that multiplicity is the located-not-forced external gap, NOT decided here). This wave decides only the bounded question 'does the structure FORCE a count incompatible with three' -- it does NOT compute the count VALUE, build the source action, or move any external datum. No canon / RESEARCH-STATUS / claim-status / verdict / posture change; count stays {1,3}; H59 stays OPEN; bar(b) unchanged."
construction: "program-native where the objects are GU's (Cl(9,5) = M(64,H); the chiral half S+ = H^32; S(6,4) = Spin(6,4) Weyl spinor; the maximal compact Spin(6)xSpin(4) = SU(4)xSU(2)xSU(2) Pati-Salam; the Rarita-Schwinger sector RS(3,1); the 2+1 'imposter generation' assembly). Standard-field where the machinery binds any construction (weight-system combinatorics for Spin(2n) Weyl spinors; ABS Clifford periodicity (p-q) mod 8; the spinor-tensor decomposition S(V+W)=S(V)(x)S(W) with chirality correlation; the SO(10) 16 -> SU(4)xSU(2)xSU(2) branching = Slansky Table 28 / Mohapatra-Pati). Forks named per GEOMETER-VS-PHYSICS-OBJECTS.md; no cross-repo identity asserted; the external Z/3 count import and the reservoir Krein sign remain GATED TI/TaF finality objects (one-way rule respected)."
depends_on:
  - explorations/generation-sector/generation-count-sm-branching-closure-2026-06-22.md
  - explorations/W201-count-external-datum-characterization-2026-07-14.md
  - explorations/W218-lean-Rsrc-unification-check-2026-07-14.md
  - explorations/W177-build-connection-curvature-c2-2026-07-14.md
  - papers/candidates/located-not-forced/located-not-forced-generation-count-2026-06-29.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W221_falsify_generation_count_structure.py
external_refs:
  - "Slansky, Group Theory for Unified Model Building, Phys. Rep. 79 (1981), Table 28 -- Spin(10) 16 -> SU(4)xSU(2)xSU(2) = (4,2,1)+(4bar,1,2)"
  - "Mohapatra-Pati (1975) -- Pati-Salam one-generation content"
  - "Atiyah-Bott-Shapiro, Clifford Modules, Topology 3 (1964) -- (p-q) mod 8 periodicity and quaternionic (KO) index counting H-lines"
cross_repo:
  - "time-as-finality / temporal-issuance: the count VALUE's external Z/3 self-dual import and the reservoir Krein sign are TI/TaF-owned finality objects (q=5 frontier). W221 is entirely GU-side and STRUCTURAL: it shows GU's bounded rep-theory does NOT force a count incompatible with three; it does NOT compute the value, which remains the external gap. No GU claim moves, no TI/TaF claim moves, no identity asserted. One-way rule respected."
---

# W221 -- FALSIFICATION (NON-NAIVE): does GU's structure FORCE a generation count incompatible with three?

**Role and charge.** This is a FALSIFICATION wave in NON-NAIVE mode against ONE leg of Geometric
Unity: the generation **count = 3**. Method (strict): ASSUME GU is CORRECT and GRANT every unbuilt
piece resolving as GU hopes; find where GU is NEVERTHELESS wrong. "Unbuilt / needs-an-external-datum /
undetermined" is a GAP, not a falsification.

The non-naive framing is essential and is inherited from W177 / W201 / W218: the count VALUE is
**located-not-forced**. It needs an external `Z/3` self-dual import (W201 typed it; W218 proved the
twisted-Rarita-Schwinger source operator `R_src` is K-null / index-conserving / **vectorlike**, so it
cannot deliver a count by itself). Therefore "the count needs an external datum" does **NOT** count as
a falsification here. The genuine falsification target is purely STRUCTURAL:

> Does GU's ACTUAL rep-theory structure FORCE a count that is EVEN, or 2, or 4 -- so that GU
> structurally CANNOT accommodate three generations?

## Pre-declared failure condition

Stated BEFORE computing, then tested:

> **GU is FALSIFIED on this leg IFF** either
> - the Rarita-Schwinger branching `RS(3,1) (x) S(6,4)` yields internal Weyl content **0** (=> total 2)
>   or **32** (=> total 4), OR
> - the H-line count structure FORBIDS the `2 + 1 = 3` assembly (forces an even-only generation total).
>
> **GU SURVIVES IFF** the RS branching yields **16** (one SM generation, => total 3) AND the H-line
> structure permits the odd `2 + 1` assembly.
>
> An "external-import-needed" outcome for the count VALUE is **SURVIVES-WITH-A-GAP**, explicitly **NOT**
> a falsification.

## The two bounded objects (computed, not asserted)

Five personas ran inline in this one worker (rep-theorist; Clifford/spinor/quaternionic-structure
specialist; Rarita-Schwinger-sector specialist; Pati-Salam/SO(10) brancher; ruthless skeptic). The
deterministic test `tests/W221_falsify_generation_count_structure.py` is 25/25, exit 0, positive
controls first.

### (a) H-line count -- Cl(9,5) = M(64,H)

Clifford/quaternionic specialist. `(p-q) mod 8 = (9-5) mod 8 = 4` => quaternionic type `M(64,H)`
(ABS periodicity). So `S = H^64`, chiral half `S+ = H^32`. One SM generation = 16 Weyl = 16 complex
= **8 H-lines** (`H = C^2`). The spin-1/2 leg carries two Weyl sectors `S_L, S_R`, each one `S(6,4)`
generation, giving **2 generations = 16 H-lines**.

Falsification pressure: does the quaternionic pairing FORCE the GENERATION total even? No. The
quaternionic structure constrains **H-line counts** to be H-integer, not **generation counts** to be
even. A generation is 8 H-lines (itself even in H-line units), so 3 generations = **24 H-lines** is a
perfectly valid integer H-submodule dimension. The `2 + 1 = 3` assembly (`16 + 8 = 24` H-lines) is
**permitted**. No even-only obstruction. (a) does NOT falsify.

### (b) Rarita-Schwinger branching -- RS(3,1) (x) S(6,4)

Pati-Salam brancher + RS specialist. The fiber spinor: `Cl(6,4)` has `(6-4) mod 8 = 2` => complex type
`M(16,C)`, so `S(6,4) = C^16`, the `Spin(6,4)` Weyl spinor (a real form of the `SO(10,C)` Weyl **16**).
Its maximal compact subgroup is `Spin(6) x Spin(4) = SU(4) x SU(2) x SU(2)` = the Pati-Salam group.

The branch is **FORCED** by the spinor-tensor split with chirality correlation. Split the 5 weight
coordinates of `S+(10)` as `(3 | 2)` for `SO(6) x SO(4)`. "Total number of minus signs even" factors as

```text
even total  <=>  (#minus in first-3 even AND last-2 even)  OR  (#minus in first-3 odd AND last-2 odd)
```

i.e.

```text
S+(10) = S+(6) (x) S+(4)  (+)  S-(6) (x) S-(4)
       = 4 (x) (2,1)      (+)  4bar (x) (1,2)
       = (4, 2, 1)        (+)  (4bar, 1, 2)
```

with the wrong-chirality blocks `(+,-)` and `(-,+)` provably EMPTY (test B2/B3). Dimensions `8 + 8 = 16`.
This is the Slansky Table 28 / Mohapatra-Pati one-generation content: `(4,2,1)` = left-handed quarks +
leptons, `(4bar,1,2)` = right-handed partners (incl. `nu_R`) = exactly **one complete SM generation of
16 Weyl fermions**.

RS specialist: `RS(3,1)` is a pure Lorentz/spacetime representation carrying **no SM gauge charge** (the
SM group acts only on the `S(6,4)` factor). So `RS(3,1) (x) S(6,4)` has the internal Weyl content of ONE
`S(6,4)` -- and its generation multiplicity is `1`, independent of the Lorentz dimension of RS. The
flipped-chiral imposter (`S-(10)`, Weinstein's "one family of 16 flipped chiral spin-3/2 particles") is
**also 16** (test B9), the CPT-conjugate multiplets, same count.

Classified against the falsification trichotomy `{16 -> total 3 | 0 -> total 2 | 32 -> total 4}`: the
content is **16**, NOT 0, NOT 32. (b) does NOT falsify; it yields exactly the located-not-forced
`{1,3}`-compatible one-generation block.

## Verdict

**SURVIVES.** Total `= 2` (spin-1/2 leg) `+ 1` (RS imposter) `= 3`. The pre-declared failure condition is
NOT met on either object: the RS branching is `16` (not `0` or `32`), and the H-line structure permits the
`2 + 1 = 3` assembly (`24` H-lines, integer H-submodule). GU's bounded rep-theory structure is
**consistent with three generations** and does not force an even/2/4 count.

## What SURVIVES does and does NOT mean (the honest caveat)

This is **SURVIVES-WITH-A-GAP**, and the gap is load-bearing but is NOT a falsification:

1. **The count VALUE is still external.** W201/W218 stand: the twisted-RS source operator `R_src` is
   K-null / index-conserving / vectorlike, so it cannot POPULATE the odd count by itself; the `1 vs 3`
   integer is a separate `Z/3` self-dual import. W221 shows only that the structure has a **slot** of the
   right shape (one 16-Weyl block per sector) for a three-generation count to live in -- it does NOT
   compute the multiplicity in `ker(D_GU)` and does NOT claim the RS zero-mode count is actually 1. Per the
   pre-declared rule, that undetermined VALUE is a GAP, not a kill.

2. **What would have falsified.** Had `S(6,4)` branched to `0` net chiral content (e.g. a self-conjugate
   vectorlike 8) or to the full unprojected Dirac `32`, the RS sector would have forced total `2` or `4`
   (both even), structurally excluding three. The negative controls (NC1/NC2/NC3) confirm the test would
   FIRE on such a structure -- so the SURVIVES verdict is discriminating, not vacuous.

3. **The located-not-forced premise is respected.** located-not-forced proves the sector INTERIOR is even
   (2-primary); the odd part is necessarily external. W221 is entirely consistent with that: the interior
   spin-1/2 leg gives the even `2`, and the odd `+1` rides on the RS/external structure. W221 does not
   smuggle the odd count into the interior; it only shows the RS branch does not FORBID the third slot.

## What this does NOT do

No canon / RESEARCH-STATUS / claim-status / verdict / posture change. No source action built, no count
value computed, no external datum moved, no Krein sign computed. `H59` remains OPEN; the count stays
`{1,3}`; `bar(b)` unchanged. No cross-repo identity asserted; the external `Z/3` import and reservoir
Krein sign are TI/TaF-owned (one-way rule respected). The result is exactly the falsification bit
(SURVIVES) plus the two branching numbers, nothing more.

**Note on numbering:** `W220` was free at filing; this note takes `W221` per the assigned label (both
`W220` and `W221` were unused; `W221` chosen as instructed).

**Artifacts:** this file + `tests/W221_falsify_generation_count_structure.py` (25/25, exit 0).

*Filed 2026-07-14. FALSIFICATION wave, NON-NAIVE mode. Assume-GU-correct + grant-every-unbuilt-piece;
exploration grade; truth-seeking (report either way, do not root); RUTHLESS skeptic. Five personas inline
in one worker; no sub-agents. Reproducible: `python -u tests/W221_falsify_generation_count_structure.py`
(25/25, exit 0; positive controls first). No canon movement; count stays {1,3}; H59 remains OPEN.*
