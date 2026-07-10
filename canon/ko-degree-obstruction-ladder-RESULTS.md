---
title: "The KO-degree obstruction ladder: 'located, not forced' upgraded from EMPIRICAL to PARTIALLY STRUCTURAL. A theorem-grade GU-independent disjointness core (anything valued in a finite 2-group or a torsion-free integer index cannot carry the CRT-disjoint order-3 class) + 5 of 7 enumerated obstructions proven-2-primary-by-KO/Spin/Pin-type from cited primary sources. Two rungs (free integer indices) and the exhaustiveness-by-type premise stay open. Caught and corrected a real canon error: e_R=1/12 is NOT the order-3 element (it is order-12, mixed); the order-3 carrier is 8*nu."
status: staged
doc_type: results
created: 2026-07-10
grade: "COMPUTED / exact (ko_ladder.py 52 asserts exit 0; independent referee 34 asserts exit 0; both re-run in-repo). Adversarially verified: 1 build + hostile math referee + overclaim auditor + completeness critic; NOT REFUTED; overclaim flagged and scoped (below). All 8 load-bearing group facts VERIFIED from primary sources this run (pi_3^s=Z/24 nLab; Im J_3=24 Adams/Wikipedia; e_KO(nu)=1/24 nLab; Omega^Pin+_4=Z/16 Kirby-Taylor CMH 65 (1990); Omega^Pin-_2=Z/8 ABK; Omega^Spin_* 2-primary ABP 1967; KO torsion Z/2 Bott; spinor dim 2^floor(m/2) ABS). Internal tier (caveat (e)) for the GU-facing corollary; the disjointness core is GU-INDEPENDENT theorem-grade. No claim-ledger row moves; the generation count stays OPEN; the FORCE step (order-3-class -> integer 3) stays the single open conjecture."
depends_on:
  - canon/two-primary-lemma.md
  - canon/three-generations-locate-not-force-CRT-RESULTS.md
  - explorations/pin-spin-and-2primary-blindness-2026-07-10.md
scripts:
  - tests/ko-ladder/ko_ladder.py
  - tests/ko-ladder/referee_ko_ladder.py
---

# The KO-degree obstruction ladder

Turns the program's empirical two-primary lemma ("every obstruction we checked is blind to 3") into a
partially structural statement by assigning each obstruction its KO / Spin / Pin type and degree and
showing -- from cited primary sources -- that it lands in a group that cannot carry the odd-torsion
Z/3 where the count lives.

## The theorem-grade core (GU-INDEPENDENT, no longer empirical)

In `pi_3^s = Z/24 = Z/8 (+) Z/3` (Adams: `|Im J_3| = denom(B_2/4) = 24`), the order-3 count carrier
lies in the 3-Sylow `Z/3`, CRT-disjoint from the 2-Sylow `Z/8`. **Blindness lemma (proved two ways):
any invariant valued in a finite 2-group of order `2^k`, or in a torsion-free integer index, cannot
carry the order-3 class -- because `gcd(3, 2^k) = 1` and `Hom(Z/24, Z) = 0`.** This is where "locate,
not force" gets its teeth, and it is unconditional arithmetic.

## The ladder: 5 of 7 rungs proven-2-primary-by-type

| # | obstruction | KO/Spin/Pin type | group | 2-primary? | grade |
|---|---|---|---|---|---|
| 1 | Kramers / quaternionic wall (`J^2=-1`) | antilinear `T^2=-1` mod-2 parity (KSp/Kramers) | Z/2 | yes (mod 2) | **structural** |
| 2 | real/pseudoreal mod-2 index (Witten) | KO mod-2 Dirac index (ABS alpha) | Z/2 | yes (Bott) | **structural** |
| 3 | cross-chirality Krein signature `(+96,-96)` | symmetric-form signature | Z (free) | no torsion | BLOCKED (free integer index) |
| 4 | adjoint Dirac index `4k/12k/24k` | twisted Dirac index (Atiyah-Singer) | Z (free) | no torsion | BLOCKED (24=8*3: the 3 is a Dynkin MULTIPLICAND, never a mod-3 congruence) |
| 5 | Rokhlin mod 16 | `Omega^{Pin+}_4` | Z/16 = Z/2^4 | yes | **structural** (Kirby-Taylor CMH 65) |
| 6 | spinor 2-smoothness | Clifford module rank (ABS) | `2^floor(m/2)` | yes (power of 2) | **structural** |
| 7 | ghost-parity no-go | Z/2 Krein grading | Z/2 | yes | **structural** (net-0 rides rung 3) |

5 structural (1,2,5,6,7), 2 BLOCKED (3,4 -- free integer indices; `Z` carries no torsion, so they miss
the order-3 class too, but their blindness is contingent on the torsion-count reading, not a 2-group
fact). Rung-1 degree label refinement (referee): the Z/2 is the Kramers mod-2 parity, not `KO^{-4}`
torsion (`KO^{-4}=KSp=Z` is free) -- the 2-primary conclusion holds, the "by-KO-degree" attribution is
a mod-2 parity statement.

## Two things the referees caught (both make the result more honest)

**1. Canon error CORRECTED -- `e_R = 1/12` is NOT the order-3 element.** Since `e_KO(generator nu) =
1/24` (nLab, verified), the class `1/12 = 2*nu` has ORDER 12 and CRT coordinates `(2,2)` -- a MIXED
element, nonzero in BOTH `Z/8` and `Z/3`. The genuine order-3 elements of `Z/24` are `{8*nu, 16*nu}`
(`e_KO = 1/3, 2/3`), CRT `(0,2),(0,1)`. The located-in-`Z/3` conclusion is UNAFFECTED (both share the
same `Z/3` component, value 2), but the label "`e_R=1/12` IS the order-3 carrier" is wrong and is
corrected in `two-primary-lemma.md` and `three-generations-locate-not-force-CRT-RESULTS.md`.

**2. Overclaim SCOPED -- "KO is blind to the odd part" is FALSE.** The KO e-invariant `e_KO` is itself
a KO invariant, and it DETECTS the full `Z/24` including the order-3 class (`e_KO(8*nu) = 1/3 != 0`) --
indeed that is HOW `|Im J_3| = 24` with its factor 3 is computed, and where the program LOCATES the
carrier. So blindness is NOT a property of KO-theory writ large; it is a property of the enumerated
obstruction TYPES (finite-2-group bordism invariants + free integer indices). The correct, sharper
reading of "located, not forced": **the count is LOCATED by the KO e-invariant (which sees `Z/3`) and
NOT FORCED by any obstruction (all 2-group torsion or free-integer, which cannot carry `Z/3` as a
constraint).** The e-invariant is the locator; the obstructions are the non-forcers.

## Exhaustiveness update (2026-07-10, `canon/exhaustiveness-by-type-RESULTS.md`): PARTIALLY CLOSED

The exhaustiveness gap below was attacked directly. Three odd-primary escape routes are now shut:
tmf/String (K3 is Spin-not-String, `(1/2)p1=-24` infinite order -> `MString->tmf` never acts); the
internal triality/SU(3)/qutrit Z/3 (PROVABLY stranded -- a Z/3 commuting with the Dirac operator gives
a g-independent net index, so it LABELS generations, never moves the count); and every odd-primary
stable-homotopy object (a DETECTOR, collapsing onto the already-located `pi_3^s`). ONE route stays
open: the geometric equivariant Nikulin carrier-B rho `(0,2,1)/3`. **Honest scope correction it forces:
the 2-primary blindness proven below is for NON-equivariant KO/Spin/Pin invariants; EQUIVARIANT
Spin/KO (G-index, rho) DO reach the odd torsion** -- and that one equivariant object is exactly the
LOCATED carrier / the program's single decider (SG4 + order-3->integer-3). Net: the escape surface is
reduced from "any un-enumerated obstruction" to ONE named channel that coincides with the decider --
the investigation proved the DECIDER IS UNIQUE (nothing routes around SG4), not that a general theorem
holds.

## The open gap (the single load-bearing one): exhaustiveness by type

The result re-types the SEVEN enumerated obstructions; it does NOT prove the enumeration is
exhaustive-by-type. Nothing here rules out an un-listed GU generation-sector obstruction of a
non-KO/Spin/Pin type carrying odd-primary torsion -- concretely, `tmf` has 3-primary torsion in some
degrees, so a `tmf`-type obstruction would escape the argument entirely. The universal reading ("every
GU obstruction is 2-primary") is licensed ONLY under the pin-spin completeness premise ("every GU
generation-sector obstruction IS a KO/Spin/Pin invariant"), which is a reconstruction-grade modeling
assumption, not a checked step. **The arithmetic disjointness is airtight and unconditional; the
universalization over all GU obstructions is BLOCKED.**

## Strongest weakest-defensible sentence

In `pi_3^s = Z/24 = Z/8 (+) Z/3`, each of the seven enumerated GU generation-sector obstructions is
valued either in a finite 2-group (rungs 1,2,5,6,7 -- `Z/2`, `Z/16`, `2^floor(m/2)`, by Bott,
Kirby-Taylor's `Omega^{Pin+}_4 = Z/16`, and ABS) or in a torsion-free integer index (rungs 3,4), and
because `gcd(3,2^k)=1` and `Hom(Z/24, Z)=0`, no such invariant can carry the CRT-disjoint order-3
class -- so the enumerated no-go structurally cannot FORCE an odd generation count; it can only LOCATE
one.

## Grade and what it changes

- The **disjointness core** is GU-independent theorem-grade (no longer empirical).
- The **ladder** is structural at 5/7 rungs (cited group facts), free-integer at 2/7.
- The **universal "no obstruction can be odd-primary"** stays OPEN (exhaustiveness-by-type; `tmf`
  escape).
- The **FORCE step** (`order-3 class -> integer 3`) stays the single open conjecture, untouched.

For the located-not-forced paper: it strengthens the headline from "empirically 2-primary" to
"structurally 2-primary at the enumerated obstructions, over a theorem-grade disjointness core" --
worded to (i) say "enumerated," (ii) name the two free rungs, (iii) cite the group facts, (iv) NOT
claim exhaustiveness, and (v) NOT call KO blind (the e-invariant locates the carrier). No claim-ledger
row moves; the generation count stays OPEN.
