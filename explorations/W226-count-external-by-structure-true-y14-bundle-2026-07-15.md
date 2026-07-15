---
artifact_type: exploration
label: W226
created: 2026-07-15
status: exploration
posture: adversarial; truth-seeking; native-object first; no verdict movement
title: "W226 external-by-structure on the TRUE RS Y14 bundle: items (1) gap-well-posedness and (2) APS/end-eta neutrality PORT to the actual Cl(9,5) carrier via standard APS machinery; item (3) family-index c1(E_-) ports its STRUCTURAL reduction only, its numerical value stays BLOCKED on the unbuilt K3-fibered geometry"
grade: "COMPUTED on the machine-verified Cl(9,5)=M(64,H) RS carrier (gen_sector_bridge anchors bare ||[Pi,M_D]||=58.7215, C2=155.3625): ITEM (1) gapped-end => tr(CHIR P_<0)=0 to 7e-16, ITEM (2) true RS boundary spectral eta_0=0 (sym defect 7e-15) + charge-q lens 2-primary + STEP-2 reduced eta-bar 2-primary, ITEM (3) multi-band c1(E_-)=0. SOURCE-AUDIT for the standard-vs-blocked classification of each item. OPEN for the true-Y14 K3 family-index pushforward mod-3 value (a free clutching parameter, unbuilt source-action geometry). Machine regression: tests/W226_count_external_by_structure_true_y14.py (21/21, exit 0). No canon / RESEARCH-STATUS / generation-count verdict change; the count stays OPEN and 3 is NOT derived."
depends_on:
  - canon/function-space-index-conservation-residual-closure-RESULTS.md
  - canon/function-space-index-conservation-RESULTS.md
  - canon/rs-boundary-eta-2primary-RESULTS.md
  - canon/external-by-structure-synthesis-RESULTS.md
  - canon/enum-completeness-class-c-RESULTS.md
  - canon/antilinear-bound-RESULTS.md
  - canon/antilinear-nonkrein-admissibility-RESULTS.md
  - canon/rs-function-space-framework-SPEC.md
  - canon/source-action-family-index-interface-SPEC.md
scripts:
  - tests/W226_count_external_by_structure_true_y14.py
---

# W226 external-by-structure on the true Rarita-Schwinger Y14 bundle

## Result in one paragraph

The last analytic residual on the "external by structure" reading of the generation count is
`model -> true RS Y14 bundle`: the three residual items of the conditional section-setting theorem
were discharged only on faithful low-dimensional stand-ins. Porting them to the ACTUAL Cl(9,5)=M(64,H)
Rarita-Schwinger carrier (via the machine-verified `gen_sector_bridge` rep) splits the residual
cleanly into two items that GENUINELY PORT and one that is genuinely BLOCKED. **Item (1), gap
well-posedness, ports at conditional grade:** the true RS operator inherits the cross-chirality Krein
structure (`Gamma`-odd + Krein-self-adjoint `=> sigma_1 (x) B` fiberwise), so its spectrum is
symmetric about 0 to `7e-15`, and whenever the noncompact end is gapped the physical projection
`P_<0` is well-posed with `tr(CHIR P_<0) = 0` (to `7e-16`) on the actual carrier -- standard
weighted-Sobolev / APS machinery supplies the gap hypothesis, and *given* it the count is 0. **Item
(2), APS/end-eta neutrality, is the strongest and ports essentially fully:** STEP 2
(`canon/rs-boundary-eta-2primary-RESULTS.md`) already computed the ACTUAL RS boundary operator's
reduced eta-bar on the sector's own boundary `RP^3 = L(2;1)` as 2-primary; here the two class
neutralities are reconfirmed on the true operator -- spectral `eta_0 = 0` (chiral off-diagonal `E =>
+/- symmetric spectrum) and the gauge/spectral channel 2-primary `(2q^2-4q+1)/8` -- and a nonzero eta
is shown to require leaving the class (an external unpaired mode, `eta_0 = +/-1`). **Item (3), the
family-index term, ports only its STRUCTURAL reduction:** the `sigma_1 (x) B` mechanism forces
`c1(E_-(D)) = c1(V_+ contribution) + c1(V_- contribution)` (chirality-balanced; verified `=0` on a
6-band multi-dimensional true-carrier-flavored family, and equal to `tr(CHIR P_<0)=0` from item 1), so
a nonzero family CHIRAL count would require a single-chirality negative bundle -- an out-of-class
external datum. **What survives BLOCKED is the numerical value of the true-Y14 K3 family-index
pushforward** `pi_!`: its mod-3 value is a FREE function of the clutching term (SPEC obligations 3-5),
blocked on the unbuilt GU K3-fibered source-action geometry, and is ANY integer. The honest residual
therefore narrows from "the whole true-Y14 computation" to precisely "the value of the K3 family-index
clutching term," items (1)-(2) now being carried on the actual bundle rather than asserted-by-machinery.
**This does NOT derive 3** (the external index realizes `0..7`, odd and even, nothing privileges 3),
and the generation-count verdict stays OPEN.

## Construction fork (mandatory)

The load-bearing object is the **cross-chirality Krein form** `K` on the RS carrier
(`Gamma` = chirality, `K Gamma = -Gamma K`, the `(+96,-96)` split). This is the **program-native
(geometer's) construction** -- the indefinite/Krein object of the GEOMETER-VS-PHYSICS table's
"Signature (9,5) / Ghost clearance" rows -- NOT the standard positive-definite Hilbert Dirac. I use
the native Krein carrier deliberately, and state why: "external by structure" is a claim about THIS
sector's own indefinite form, and the standard positive-definite construction does not even host the
cross-chirality involution (`K Gamma = -Gamma K`) that does all the work here. The count itself is
left OPEN -- I stay on neither side for the verdict. The generation count also sits on the native side
of a SECOND fork (the table's "Generation count" row): it is a torsion `Z/3` datum, and a `Z`-valued
index provably cannot reach it (`Hom(Z/3, Z) = 0`); this is exactly why the family-index VALUE being
free-and-external, rather than a forced integer, is the coherent reading and why deriving `3` from an
index would be the error.

## Worked computation (on the true carrier)

All ported quantities are computed on the actual `Cl(9,5) = M(64,H)` RS carrier via
`gen_sector_bridge.constraint_objects()` (anchors `bare ||[Pi,M_D]|| = 58.7215`, `C2 = 155.3625`
intact; `Tr(chirality | RS) = 0`, the native `(+96,-96)` split). `D_RS = E + E^dag`, `E = Q M_D Pi`.

### Item (1) gap well-posedness -- PORTED (conditional)

| quantity (true carrier) | value | reading |
|---|---|---|
| `spec(D_RS)` symmetry defect | `7.1e-15` | the `sigma_1 (x) B` fiber fact holds on the TRUE operator |
| `tr(CHIR P_<0)` (gapped) | `-6.7e-16` | gapped end `=>` physical count is 0 on the actual carrier |
| physical-sector gap | `3.555 > 0` | well-posed (distance of nonzero spectrum from 0) |
| class-generic gapped draw | `tr = 7.6e-16`, gap `35.2` | model-independent within the class |

**What is standard/portable:** the well-posedness of `P_<0` on a gapped (product/cylindrical)
noncompact end is textbook APS / weighted-Sobolev; and *given* the gap, the cross-chirality structure
(which the true carrier has, and which STEP 2 already used) forces `tr(CHIR P_<0) = 0`. So the
conditional statement "gapped end `=>` count 0" is carried on the actual bundle. **What is blocked:**
whether the *actual* GU noncompact end (the fiber-metric direction of `Y14 = Met(X^4)`) is gapped
depends on the unbuilt end metric; gaplessness is a failure of well-posedness, not a chiral leak.

### Item (2) APS/end-eta neutrality -- PORTED (strongest)

| quantity (true RS boundary operator) | value | reading |
|---|---|---|
| spectral `eta_0(D_RS)` | `0` | chiral off-diagonal `E =>` `+/-`-symmetric spectrum |
| gauge/spectral channel `(2q^2-4q+1)/8` | denom `8`, all `q` | 2-primary for every integer charge |
| 30 random class draws `sigma_1 (x) B` | total eta `0` | class-genericity: every class op is neutral |
| out-of-class unpaired mode | `eta_0 = +/-1` | a nonzero eta is EXTERNAL by structure |

This leverages STEP 2 directly: the ACTUAL RS boundary operator's reduced eta-bar on the sector's own
`RP^3 = L(2;1)` is already computed 2-primary (grav `-p_1/24 : 0` because net self-dual frame charge
`= 0`; gauge/spectral `(1/8)Z`). Item (2) is therefore essentially fully on the true bundle: the only
"model" content left is that STEP 2 covered the sector's OWN boundary; a *different* external end (a K3
flux) can carry a nonzero eta -- but that is external by construction.

### Item (3) family-index `c1(E_-)` -- STRUCTURAL reduction ports; VALUE blocked

| quantity | value | reading |
|---|---|---|
| `c1(E_-(sigma_1 (x) B))`, 6-band family | `0` | multi-dim generalization of the faithful QWZ 2-band |
| reduction to true-carrier balance | `tr(CHIR P_<0) = 0` | `c1(V_+)+c1(V_-)` balanced (item 1) |
| single-chirality (out-of-class) bundle | `c1 = -1 != 0` | the mechanism detects a real chiral leak |
| true-Y14 K3 pushforward mod-3 value | FREE / BLOCKED | any integer; unbuilt source-action geometry |

The `sigma_1 (x) B` mechanism reduces the family CHIRAL term to `c1(V_+ contribution) + c1(V_-
contribution)`, chirality-balanced -- a nonzero family chiral count requires the negative bundle to
keep a SINGLE chirality (out-of-class / external). **That reduction ports** (verified beyond 2 bands,
and identified with the item-1 balance). **What stays blocked** is the numerical value of the true-Y14
K3 family-index pushforward `pi_!`: `canon/rs-function-space-framework-SPEC.md` STEP 3 and
`source-action-family-index-interface-SPEC.md` already localize this to obligations 3-5 (the
`Phi`-homotopy / symbol certificate, the `ch2`/eta clutching term, the `H`-line normalization), all
requiring the unbuilt GU `K3`-fibered source-action geometry. The mod-3 family value is a free function
of the clutching term -- ANY integer -- and the firewall holds: the RS bulk uses `sigma(K3) = -16`
(`21*sigma/8 = -42 == 0 mod 3`), never `chi(K3) = 24` or `24/8 = 3`.

## 3 is NOT derived (explicit)

The external topological index realizes `[0,1,2,3,4,5,6,7]` (Aharonov-Casher / Atiyah-Singer,
`index = flux`), odd and even alike; nothing here privileges `3` over `1, 5, 7`. Item (3)'s blocked
value is precisely the slot where a `3` could only ever be IMPORTED, and the firewall control
(`CTRL1`) fires if any ported quantity is ever computed as `chi(K3)/8`. The interior is even/2-primary
(inherited: enum-completeness class C, antilinear bound, STEP-2 boundary), the only odd-count channel
is external, and its value is unbuilt. **Deriving 3 here would be an error; the port is designed to
make that error trip a control.** The generation-count verdict is Joe-gated and remains OPEN.

## Positive controls (fired FIRST, non-vacuous)

1. `CTRL1` -- fires if the argument ever illegitimately privileges 3: constructs the forbidden
   `chi(K3)/8 = 3` import, confirms the honest bulk uses `sigma`, and checks every ported quantity is
   `chi`-independent (perturbing `chi` does not move it).
2. `CTRL2` -- fires on a real index-nonconservation falsifier: a single-chirality (out-of-class)
   negative bundle gives `c1 = -1 != 0`, so the item-(3) balance check is non-vacuous (the mechanism
   detects a genuine chiral leak).
3. External unpaired-mode control (`ITEM2b`): an odd-dim operator with no chirality involution gives
   `eta_0 = +/-1`, confirming the class-neutrality is not blindness.

## Machine receipt

```
python tests/W226_count_external_by_structure_true_y14.py
```

`21/21` checks passed, exit 0. Positive controls first (CTRL1 firewall-on-3, CTRL2 leak detector),
then the true-carrier ITEM (1)/(2)/(3) checks, then the any-integer guardrail.

## What this narrows (recommendation, not executed)

The honest residual in `canon/function-space-index-conservation-residual-closure-RESULTS.md`
("model -> true RS Y14 bundle ... asserted-by-machinery, not re-derived on Y14") can NARROW: items
(1) and (2) are now carried on the ACTUAL Cl(9,5) RS carrier at computed grade (item 2 leaning on the
already-canon STEP-2 true-operator eta), and item (3)'s structural reduction is on the true carrier
too. The residual shrinks from "the whole true-Y14 computation" to precisely **the numerical value of
the K3 family-index clutching term** (SPEC obligations 3-5, unbuilt geometry). This is a
canon-promotion candidate for the residual-closure RESULTS file (a scope-narrowing of its "What this
does NOT close" section) -- **FLAGGED only, not promoted in this wave.**

## Governance

Exploration grade only. No canon, RESEARCH-STATUS, or generation-count verdict change; the count stays
OPEN (Joe-gated). No paper edit. No git commit/push. Internal tier. `3` is NOT derived.
