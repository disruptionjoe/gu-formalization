---
artifact_type: exploration
label: W235
created: 2026-07-15
status: exploration
posture: "adversarial, truth-seeking, native-object first; coherence-first; conditional register; RUTHLESS skeptic; grant every unbuilt piece; only a wrong definite output or a forced inconsistency falsifies; bar(b)/H59/count stay OPEN and Joe-gated; win condition is CHARACTERIZATION (force-or-name-the-datum), NOT flipping the verdict"
title: "W235 -- THE central bit (mirror Z2: conserved RECORD or gauge REDUNDANCY), characterized. RESULT: GU's DETERMINED (built) content FORCES the RECORD reading at the KINEMATIC / free-BV level via THREE independent, Y14-INDEPENDENT legs (mirror on ker(Gamma) => not Koszul-Tate-exact; gauge orbit im(d_A) transverse to ker(Gamma) => not ghost-exact, both W173; positivity forces the C-grading UNIQUE, grading-sign moduli = 0, W228/A1). The bit is UNDETERMINED only at the DYNAMICAL / quantization grade, where it hinges on EXACTLY ONE named UNBUILT datum: the GU connection-curvature 2-form F_A on Y14 = Met(X4) that closes the secondary constraint C2 = Gamma.M_D.Pi_RS (norm 155.36, Gamma-independent) as a (generation, mirror) doublet-forming differential. theta := F_A-distinguished-null-plane; theta = 0 (no distinguished section) = RECORD (Z2 operative); theta != 0 = REDUNDANCY (Z2 broken). The bit is NOT symmetric: RECORD is the built default and GU's native cores are spectrally sign-blind (cannot source the pairing), so REDUNDANCY is reachable ONLY by an EXTERNAL import. This SHARPENS W173/W231's 'leans REALIZES' to 'FORCED at kinematic grade; import-only demotion; open only at dynamical grade.' Does NOT resolve bar(b)/H59/count. Test tests/W235_central_bit_mirror_record_vs_redundancy.py 30/30 exit 0, positive controls first."
grade: "STRUCTURAL / EXACT for the finite-dimensional cohomology facts (machine-verified, tests/W235_central_bit_mirror_record_vs_redundancy.py, 30/30, exit 0, positive controls first, pure numpy rank arithmetic, no hardcoded cohomology dimensions): s nilpotent with both legs nonzero; H^0 computed by ranks; the mirror is a NONTRIVIAL class at theta=0 (RECORD) and EXACT at theta!=0 (REDUNDANCY); the three kinematic legs L1 (mirror on ker(Gamma), not KT-exact), L2 (gauge orbit transverse for all magnitudes, not ghost-exact), L3 (V+/V- constituent non-coincidence => grading moduli 0) all Y14-independent; robustness of the free-level verdict under the determined-content knobs (KT normalization beta, Krein-sign flip); the single-locus flip (RECORD exactly at theta=0); the five-object unification map; the guard controls (native core sign-blind => dynamical bit open; delta_pair CAN collapse the mirror so the machinery is not rigged). STRUCTURAL for the lift to GU's genuine M(64,H) RS BV bicomplex (this is a faithful finite toy of the exact structural facts computed in the cited W173 / rs-gu-phys-brst / bv-bicomplex tests; it does NOT recompute the full rep). INHERITED (flagged, not re-derived): W173's transversality machine facts (RS-symbol norms 73.48 / 343.73), C2 = 155.36 Gamma-independent; W228's forced-unique C-grading at the kinematic stabilizer; W231's SO(10) channel discriminant; W216's condensate branch dichotomy; the native-core spectral sign-blindness (big-swing R3, SUSTAINED x2). No canon / RESEARCH-STATUS / claim-status / verdict / posture change; bar(b) and H59 stay OPEN; the count stays {1,3}; no forbidden target {3,8,24,chi(K3),Ahat} assumed or inserted. Zero em dashes."
construction: "Construction fork NAMED per GEOMETER-VS-PHYSICS-OBJECTS.md and load-bearing. PROGRAM-NATIVE where the objects are GU's: the mirror as the Krein-negative half of 96 hyperbolic null pairs in ker(Gamma) of Cl(9,5) = M(64,H) with K = the Cartan involution of so(9,5) (W173); the free BV bicomplex s = s_KT + s_long GU actually built (nilpotent on M(64,H)); the secondary constraint C2 = Gamma.M_D.Pi_RS and the Y14 = Met(X4) connection-curvature 2-form F_A that would close it (W173/W177); the good-stable C-commutant stabilizer SO(9)xSO(5) etc. (W228). STANDARD-FIELD where the machinery binds any construction and is ported/cited: BV/BRST cohomology (Henneaux-Teitelboim, Koszul-Tate resolution, longitudinal differential, H^0 = observables), the Kugo-Ojima quartet / doublet demotion, the Krein-space grading-moduli classification. The record-vs-redundancy answer LIVES ON BOTH sides of the fork and the characterization names which side each level lands on: the KINEMATIC/native side FORCES record; the DYNAMICAL side is decided by one external (boundary/firewall-type) datum GU does not build. The reservoir Krein sign / r* stay GATED TI/TaF finality objects (one-way rule respected; no cross-repo identity asserted)."
depends_on:
  - explorations/W173-brst-cohomology-mirror-sector-2026-07-14.md
  - explorations/W231-close-a3-smg-realization-gu-mirror-2026-07-14.md
  - explorations/W228-close-a1-corrected-sign-gu-instance-2026-07-14.md
  - explorations/W216-true-vacuum-spectral-condensate-2026-07-14.md
  - explorations/W233-close-a6-count-import-characterization-2026-07-14.md
  - explorations/W227-gap-analysis-to-unconditional-2026-07-14.md
  - explorations/W211-krein-sign-godel-independent-five-method-synthesis-2026-07-14.md
  - canon/firewall-boundary-hypothesis.md
  - canon/ghost-parity-krein-synthesis.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W235_central_bit_mirror_record_vs_redundancy.py
cross_repo:
  - "time-as-finality / temporal-issuance: the central bit (records vs redundancy) is the object TaF flagged in T507-T509. W235 characterizes GU's side: GU's determined content forces the RECORD reading at KINEMATIC grade and leaves the DYNAMICAL bit hinging on ONE named GU-owned unbuilt datum (F_A / C2 spectral section). This does NOT touch, fix, or re-litigate the reservoir Krein SIGN, which W211 flagged and W228 corrected to a kinematically-forced object; the DYNAMICAL good-stable stabilizer stays unbuilt (W219). One-way rule respected; no GU claim moves, no TI/TaF claim moves, no identity asserted."
---

# W235 -- THE central bit: is the mirror Z2 grading a conserved RECORD or a redundancy?

Test / characterization certificate: `tests/W235_central_bit_mirror_record_vs_redundancy.py`
(30/30, exit 0, positive controls first). Four personas ran INLINE in one worker (BRST /
BV-cohomology specialist; Krein / grading-moduli specialist; GU-structure / Y14-datum specialist;
ruthless skeptic); no sub-agents. Zero em dashes. This is the North Star swing of Wave 2: the whole
six-lane gap-closure wave (W228-W233) collapsed GU's remaining conditionality onto ONE object, and
this note characterizes that object as sharply as GU's built content allows.

## Result in one paragraph

GU's DETERMINED (built) content **FORCES the RECORD reading at the KINEMATIC / free-BV level**, via
three independent legs that are each **Y14-independent**: (L1) the mirror lies on the constraint
surface `ker(Gamma)`, so it is **not Koszul-Tate-exact**; (L2) GU's gauge orbit `im(d_A)` is
**transverse** to `ker(Gamma)` (RS-symbol norms 73.48 / 343.73 nonzero OUT of the surface, zero IN),
so the mirror is **not ghost-exact** -- both from W173; (L3) positivity **forces the `C`-grading
unique** (grading-sign moduli `= 0`) because the stabilizer's `+` and `-` constituents share no type
(W228 / lane A1). None of L1-L3 uses the Y14 connection-curvature, so at the level GU actually
computes the mirror is **BRST-closed-not-exact -> a RECORD -> the Z2 (Cartan-involution / ghost-parity)
grading OPERATIVE** -- and this is *forced*, not merely leaning. The bit becomes **undetermined only at
the DYNAMICAL / quantization grade**, where it hinges on **exactly one named unbuilt datum**: the GU
connection-curvature 2-form `F_A` on `Y14 = Met(X4)` that would close the secondary constraint
`C2 = Gamma . M_D . Pi_RS` (norm 155.36, `Gamma`-independent) as a `(generation, mirror)`
doublet-forming differential. Writing `theta` for that distinguished-null-plane datum: `theta = 0` (no
distinguished spectral section) `=` RECORD; `theta != 0` (section pairs the mirror) `=` REDUNDANCY. The
bit is **not symmetric**: RECORD is the built default, and GU's native cores are **spectrally
sign-blind** (they commute with the grading, so they cannot source the pairing), so REDUNDANCY is
reachable **only by an external import** of the Y14 / boundary datum. This sharpens W173/W231's "leans
REALIZES" to the graded statement **FORCED at kinematic grade; demotion is import-only; genuinely open
only at dynamical grade**. It does **not** resolve `bar(b)` / `H59` / the generation count, which live
at the dynamical grade and stay OPEN and Joe-gated.

## Construction fork (named, load-bearing)

The object "the mirror sector" has the standard-field BRST construction (a negative-norm state is a
gauge artifact, removed by gauge-fixing / the quartet mechanism -> REDUNDANCY by textbook default) and
the program-native construction (the Krein-negative half of 96 hyperbolic null pairs in `ker(Gamma)` of
`Cl(9,5) = M(64,H)`, graded by the *global* Cartan involution `K` of `so(9,5)` -> candidate RECORD).
The answer **lives on both sides, at different levels**, and the whole point of the characterization is
to say which side each grade lands on:

- **Native / kinematic side -> RECORD, forced.** The free BV bicomplex GU built, plus the forced-unique
  compact `C`-grading, put the mirror in `H^0` and make the grading a *global superselection* label,
  not a *local gauge* redundancy. A global involution grades states into records; only a local gauge
  symmetry produces redundancy. GU's grading is the global one (W173 Persona 2; W228).
- **Standard-field / dynamical side -> decided by one external datum.** The textbook demotion
  (Kugo-Ojima doublet) requires a differential that pairs `(generation, mirror)`. In GU that
  differential is `C2`, and `C2` does not close without `F_A` on `Y14`. That datum is exactly the
  firewall/boundary-type object the program's standing hypothesis predicts (`canon/firewall-boundary-hypothesis.md`).

Defaulting silently to either side is the failure mode. The native side does **not** get to declare
"record, done" (that would flip `bar(b)`); the standard side does **not** get to declare "redundancy by
default" (W173 showed the demotion is not GU-forced). The honest statement is the two-grade split.

## The worked characterization

### 1. The two cohomologies (why "is the free-BV cohomology nontrivial?" has a Y14-independent answer)

There are two BRST cohomologies, and conflating them is what made the bit look either "resolved" or
"free":

- `H^0(s_free)` -- the cohomology of the **free BV bicomplex GU actually built** (`s = s_KT + s_long`,
  nilpotent on `M(64,H)`, W173). This is **determined content**. Its verdict on the mirror is a machine
  fact and it is **nontrivial**.
- `H^0(s_full)` -- the cohomology of the **stabilized** complex including the secondary constraint
  `s_C2`. This is **not built**: `s_C2` needs `F_A` on `Y14`.

W235's computation makes precise that the mirror's class in `H^0(s_free)` is controlled **only** by L1
and L2, both Y14-independent, and is **robust** under every determined-content knob (the test varies
the Koszul-Tate normalization and flips the Krein sign; the mirror stays a nontrivial class every
time). So the answer to goal (1) as posed -- "is the mirror's BRST cohomology nontrivial from GU's
determined content alone, or does nontriviality depend on the unbuilt Y14 datum?" -- is:

> The **free-BV** cohomology nontriviality is forced by determined content and is **Y14-independent**.
> The **physically deciding** (stabilized) cohomology is Y14-dependent, and the dependence enters at a
> **single** place: whether `s_C2` (via `F_A`) makes the mirror exact.

In the model, `s = s_free + theta * delta_pair`, where `delta_pair` is the doublet-forming differential
and `theta` is the `F_A`-distinguished-section datum. `H^0` computed by ranks gives: mirror **survives**
(nontrivial, RECORD) for `theta = 0`, mirror **killed** (exact, REDUNDANCY) for `theta != 0`, and the
RECORD locus is **exactly** `{theta = 0}`. One datum, one flip.

### 2. What in the built content forces RECORD, and how robust it is (goal 2)

Three independent legs, each a determined-content fact and each Y14-independent:

- **L1 (Koszul-Tate).** The mirror is on `ker(Gamma)` (the constraint surface; the generation triplet
  is the 192-dim sector of the 1664-dim `ker Gamma`). Koszul-Tate exactness is off-shell/EOM-triviality;
  the mirror is on-shell, so `mirror not-in im(s_KT)`. Machine: `mirror in ker(Gamma)`, `mirror not
  KT-exact`.
- **L2 (longitudinal / ghost).** GU's own gauge orbit `im(d_A)` is transverse to `ker(Gamma)` (W173's
  decisive GU-specific fact, RS-symbol norms 73.48 and 343.73 nonzero, i.e. the gauge orbit escapes the
  surface). So no in-surface gauge direction reaches the mirror: `mirror not-in im(s_long)`. Machine:
  the transverse direction's projection into `ker(Gamma)` is zero for every magnitude, while its norm
  out of the surface is nonzero.
- **L3 (forced-unique grading, W228).** Positivity (`C^2 = I`, `C` eta-self-adjoint, `eta.C > 0`)
  forces the admissible grading unique because `V+` and `V-` share no stabilizer constituent
  (non-coincidence holds at `SO(9)xSO(5)`, at `SO(3)xSO(6)xSO(4)`, in the `Sp`/`Spin` frames). The
  grading-sign moduli space has dimension `0`. So the grading that labels the mirror is the *unique*
  record grading, not a free `Z/2` -- this is the correction W228 made to W211/W206. Machine:
  `moduli = 0`; a degenerate control (coincident types, diagonal `O(r) < O(r,r)`) gives moduli `> 0`,
  so the detector genuinely sees a continuum where one exists.

**How robust is the lean?** Stronger than W173/W231 stated. W173/W231 called it "leans REALIZES." L1-L2
put the mirror in `H^0(s_free)`; L3 (W228, *not yet folded into the W173 lean*) removes the last
free-bit reading at the kinematic stabilizer. Together they make the record reading **forced at
kinematic grade**. For the redundancy reading to hold, **all three** would have to be overridden by the
one dynamical object: `F_A` would have to (i) supply a distinguished null plane that (ii) closes `C2` as
a differential pairing `(generation, mirror)` into a Kugo-Ojima doublet, (iii) against the global
(not local) character of the Cartan-involution grading. Nothing in the *built* content does any of this,
and the native cores provably cannot (next section). So the robustness is: **record survives every
determined-content perturbation; only an external `F_A` import can demote it.**

### 3. The single named datum, and whether GU constrains it (goal 3)

**The datum, exactly:** the **GU connection-curvature 2-form `F_A` on `Y14 = Met(X4)`** (equivalently,
the spectral section / distinguished null plane) that closes the secondary constraint
`C2 = Gamma . M_D . Pi_RS` (bare norm 155.36, `Gamma`-independent, two-construction-confirmed, W173).
It is the same object that (a) supplies W132's `C`-operator for retention unitarity, (b) selects
W216's good-vs-pathological branch, and (c) sits in the count-import characterization (W177/W233).

- **`theta = 0` (RECORD):** `F_A` does **not** select a distinguished null plane that pairs
  `(generation, mirror)`; `C2` does not close as a doublet-forming differential within `ker(Gamma)`;
  the mirror stays closed-not-exact; the Cartan-involution `Z2` is a conserved superselection grading
  -> **the mirror is a conserved record, `Z2` operative**.
- **`theta != 0` (REDUNDANCY):** `F_A` selects the distinguished spectral section that pairs
  `(generation, mirror)` into a BV doublet/quartet; the mirror becomes `s`-exact; the `Z2` is not
  operative -> **redundancy**.

**Does GU constrain it? PARTIAL, and asymmetrically.** GU does not leave `theta` a free symmetric bit:

1. At the **kinematic** level GU **forces `theta = 0`** (L3 above: the compact stabilizer's grading is
   unique; there is no admissible pairing at kinematic grade).
2. GU's **native cores cannot produce `theta != 0`**: big-swing R3 (SUSTAINED x2) found every GU-native
   core PT-unbroken yet **spectrally sign-blind** (every eigenspace exactly `K`-balanced), and `C` is
   non-unique only at the three-generation degeneracy. A sign-blind core **commutes with the grading**,
   hence is block-diagonal in the `(generation +, mirror -)` split, hence **cannot generate the
   off-diagonal (`K`-odd) pairing** `delta_pair`. The test verifies exactly this: the native core
   commutes with the grading, `delta_pair` is `K`-odd, and therefore the native core cannot source
   `theta`.

So **RECORD is the built default; REDUNDANCY is import-only.** The genuine residual freedom is
**dynamical grade**: the DYNAMICAL good-stable stabilizer (the interacting vacuum isotropy + observable
algebra) is **unbuilt** (W228/W219). Were it a strictly smaller, coincidence-admitting group, a shared
`+/-` type could reappear and free-`theta` with it. That -- and only that -- is why the bit is not
closed. The forcing is **kinematic grade**; the openness is **dynamical grade**; the deciding object is
**one named unbuilt datum**.

### 4. Unification: one bit onto all five objects

`theta` reads simultaneously onto every object the wave collapsed (test Block D prints the map):

| object | `theta = 0` (RECORD) | `theta != 0` (REDUNDANCY) |
|---|---|---|
| `bar(b)` (central grading / loop unitarity) | clears cohomologically | re-posed / engine |
| `H59` good branch (Krein-loop positivity) | GOOD branch | pathological branch |
| A1 dynamical stabilizer (W228) | non-coincident, `C = eta` unique | coincident continuum |
| A3 channel S vs D (W231) | S: mirror-only SMG, chirality KEPT | D: gen-mirror Dirac, chirality LOST |
| W216 condensate spectrum | real, gapped, sensible | complex, opposite-type collision |

The identifications are the ones the priors already established: A3's discriminant *is* whether the
Cartan `Z2` is conserved (W231 Persona 3); W216's branch selector *is* the same operative-`C` bit
(W216 Persona 3); A1's forced-unique grading *is* the kinematic side of this bit (W228). W235's
contribution is to show they are the **same `theta`**, that determined content forces `theta = 0` at
kinematic grade on **all** of them at once, and that the sole locus of dynamical-grade freedom is the
one `C2`/`F_A` closure -- so the caution W231 flagged (GU's own W216 condensate structurally sitting in
the chirality-killing channel D) is an **import-only** danger, not a determined-content outcome:
D/pathological/redundancy is reachable only if the external `F_A` actively demotes the mirror.

### 5. Skeptic pass (why neither "resolved record" nor "free bit" survives)

**Steelman "record, resolved."** L1-L3 all force record and are Y14-independent; the demotion needs an
unbuilt import; isn't that a resolution? **No.** The forcing is **kinematic grade**. `bar(b)` and `H59`
are **dynamical**-grade objects (loop unitarity; the interacting vacuum). W228's own honest caveat: the
dynamical stabilizer is unbuilt, and if it were coincidence-admitting the continuum returns. Declaring
"record" resolved would flip `bar(b)` on a kinematic result -- exactly the guardrail. The test's PC-A
control fires if any step narrows the dynamical `theta` to a singleton from built content; it stays
open.

**Steelman "free symmetric bit" (the old W211 reading).** Both grading signs are admissible, so it is
one undecidable `Z/2`? **No** -- W228 killed this: that was the cone-vs-grading conflation; positivity
forces the grading unique at the kinematic stabilizer. The residual is not a symmetric bit; it is the
asymmetric "record default, import-only demotion, dynamical-grade openness."

**Is this a relabeled punt?** No. It does three things the priors did not: (a) it **upgrades the grade**
of the lean from "leans" (W173/W231) to "forced at kinematic grade" by folding in W228's forced-unique
grading as a third independent leg; (b) it **proves the free-level nontriviality Y14-independent** and
**robust** (the bit depends on exactly one parameter, machine-checked by rank across a family of
determined-content perturbations); (c) it shows the demotion is **import-only** (native cores
sign-blind cannot source the pairing), so RECORD and REDUNDANCY are not symmetric alternatives.

## This does NOT resolve bar(b) / H59

Explicitly, and by design. `bar(b)`, `H59`, and the generation-count verdict are the objects this bit
is ABOUT; they are the **dynamical-grade** reading of `theta`, and they stay **OPEN and Joe-gated**. W235
reports a **characterization**: GU's built content forces the record reading at **kinematic** grade and
names the **single** unbuilt datum (`F_A` on `Y14`, closing `C2`) whose value decides the **dynamical**
grade, together with the asymmetry (record is the default; redundancy is import-only). It does **not**
declare "the mirror IS a record" as a resolved verdict; the dynamical bit is open exactly as far as the
Y14 source-action is unbuilt. No canon / RESEARCH-STATUS / claim-status / verdict / posture change; the
count stays `{1,3}`; no forbidden target `{3,8,24,chi(K3),Ahat}` assumed or inserted; no cross-repo
identity asserted; the reservoir Krein sign / `r*` stay gated TI/TaF finality objects.

## What this changes and what it does not

Changes (exploration-tier, no canon movement):

- Sharpens the central bit from "leans REALIZES" (W173/W231) to **"FORCED at kinematic grade via three
  independent Y14-independent legs; demotion import-only; open only at dynamical grade."**
- Folds W228's forced-unique `C`-grading into the record argument as a **third** leg, and unifies it
  with W173's free-BV computation as the **same** `theta = 0` forcing.
- Isolates the **single** locus of dynamical-grade freedom (`C2`/`F_A` closure) and shows every other
  (determined-content) knob leaves the bit invariant.

Does not change:

- `bar(b)`, `H59`, and the generation count remain **OPEN** and **Joe-gated**. No RESEARCH-STATUS,
  claim-status, verdict, or posture movement.
- Does not build `F_A`, close `C2`, construct the dynamical good-stable stabilizer, or fix the source
  action. The Cartan-involution / `C`-operator identifications are inherited (W173/W132), not re-proved.
- The finite model is a faithful toy of exact structural facts, not the full `M(64,H)` rep (that lives
  in the cited W173 / `rs-gu-phys-brst` / `bv-bicomplex` tests). A Lean port of the two-grade split is a
  follow-up only (no Lean run here, per the machine-wide serialized-build rule).

## Highest-value follow-up

Build the **DYNAMICAL** good-stable stabilizer (the W219 front door): derive the interacting vacuum
isotropy + observable algebra and check whether it is one of the non-coincident groups (record forced at
dynamical grade, `bar(b)` clears) or a coincidence-admitting smaller group (free-`theta` returns). That
is the **one** step that would move the bit from kinematic-forced to dynamical-forced or expose the real
residual, and it is exactly what `bar(b)` / `H59` wait on.

**Artifacts:** this file + `tests/W235_central_bit_mirror_record_vs_redundancy.py` (30/30, exit 0;
positive controls first).

*Filed 2026-07-15 by W235 (North Star swing of Wave 2). Four personas inline in one worker (BRST /
BV-cohomology; Krein / grading-moduli; GU-structure / Y14-datum; ruthless skeptic); no sub-agents.
Reproducible: `python -u tests/W235_central_bit_mirror_record_vs_redundancy.py` (30/30, exit 0).
Exploration grade; characterization not resolution; no canon movement; `bar(b)` / `H59` / the count
OPEN. Zero em dashes.*
