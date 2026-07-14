---
artifact_type: exploration
label: W173
status: exploration (W173 / BRST-COHOMOLOGY of the mirror sector; 5-persona inline team; one deterministic test 27/27 exit 0; the cross-repo bridge computation of the bit TaF flagged in T507-T509)
created: 2026-07-14
branch: "Team W173 (BRST-cohomology): is GU's graded-ghost / mirror sector BRST-EXACT (gauge redundancy -> NOT-operative -> engine) or BRST-COHOMOLOGY-NONTRIVIAL (physical record -> Krein grading OPERATIVE)?"
title: "W173 VERDICT: QUANTIZATION-DEPENDENT-<Y14 connection-curvature 2-form / secondary constraint C2>. In the FREE BV bicomplex GU actually determines (built, nilpotent s^2=0 on Cl(9,5)=M(64,H)), the mirror is BRST-cohomology-NONTRIVIAL: it lies ON the constraint surface ker(Gamma) so it is NOT Koszul-Tate-exact, and GU's own gauge orbit im(d_A) is TRANSVERSE to ker(Gamma) (machine fact, RS-symbol norms 73.48 / 343.73 != 0) so within ker(Gamma) it is NOT ghost-exact -> closed-not-exact -> a RECORD -> Krein grading OPERATIVE. This REVERSES TaF's redundancy default at the level GU actually computes. The ONLY object that could demote the mirror to BRST-EXACT (redundancy) is a differential pairing (generation,mirror) into a BV doublet/quartet -- exactly the BRST-invariance of the dynamics M_D (secondary constraint C2 = 155.36, Gamma-independent) which does NOT close without the UNBUILT Y14 connection-curvature 2-form that selects a distinguished null plane / spectral section. That spectral section is the SAME external datum the C-operator provides for W132 retention unitarity: one geometric object governs both records-vs-redundancy and the unitarity price. GU's native cores cannot supply it (big-swing R3: PT-unbroken yet spectrally sign-blind; C non-unique at the 3-generation degeneracy), so the redundancy demotion requires importing the firewall/boundary datum -- which is the program's standing external-source thesis. Effect on bar(b): NOT cleared and NOT simply re-posed -- RELOCATED onto the Y14-curvature / C-operator question, jointly with the generation-count boundary datum."
grade: "EXACT for the finite-dimensional cohomology facts (null-pair signature; closed-not-exact in the free complex; the demotion-by-pairing; W132 expansion identity A^dag A = P+ + B^dag B), machine-verified 27/27 to 1e-6..1e-12. STRUCTURAL for the lift to GU's genuine RS BV bicomplex (the toy reproduces the qualitative machine facts of rs-gu-phys-brst-specification sec 3 and bv-bicomplex-and-c2-obstruction: gauge-orbit transversality, Koszul-Tate-exact-not-ghost-exact escape, C2 as the sole demotion channel; it does NOT recompute the M(64,H) rep here -- that is in the cited tests). ARGUED for the identification of the C2-closing spectral section with W132's C-operator (both are a distinguished-null-plane / positive-metric choice; a proof of identity is not attempted). NO canon / claim-status / verdict / posture change. No cross-repo identity claim. Whether the mirror is a record stays OPEN exactly as far as the Y14 source-action is unbuilt."
depends_on:
  - canon/ghost-parity-krein-synthesis.md
  - explorations/vz-evasion/rs-gu-phys-brst-specification-2026-06-26.md
  - explorations/anomaly-and-bordism/bv-bicomplex-and-c2-obstruction-2026-06-27.md
  - explorations/W132-graded-optical-theorem-physical-subspace-2026-07-14.md
  - explorations/big-swing-2026-07-06/BIG-SWING-CONFORMAL-CLASS-BLOCKED.md
  - explorations/big-swing-2026-07-06/VG-V1-condensate-ghost-parity-scan.md
  - explorations/cross-repo-survey-taf-ti-2026-07-11.md
scripts:
  - tests/W173_brst_cohomology_mirror_sector.py
external_refs:
  - "Bateman & Turok, Escape from Ostrogradsky via Hidden Ghost Parity, arXiv:2607.00096 -- Krein-space quantization, ghost parity, generalized Born rule (the RECORD family)"
  - "Kugo & Ojima, Local covariant operator formalism of non-abelian gauge theories, PTP Suppl 66 (1979) -- quartet mechanism: BRST-exact (doublet) states leave the cohomology; physical subspace positive-definite (the REDUNDANCY family)"
  - "Henneaux & Teitelboim, Quantization of Gauge Systems, Princeton 1992 -- BV/BRST, Koszul-Tate resolution, longitudinal differential, H^0(s) = observables"
  - "Distler & Garibaldi, There is no Theory of Everything inside E8, CMP 298 (2010) -- the vectorlike/mirror obstruction whose positivity assumption the Krein reading drops"
cross_repo:
  - "time-as-finality: T507 (records-vs-redundancy double gate), T508 (BRST-cohomology record-admission gate), T509 (BRST-observable-compatibility gate); explorations/ghost-parity-physicality-push-2026-07-07.md -- the gate this computes GU's side of. One-way rule respected: no GU claim moves, no TaF claim moves, no identity claimed."
---

# W173 -- BRST cohomology of GU's mirror (ghost) sector

**Role and framing.** The time-as-finality repo narrowed its `records vs redundancy`
discriminator (governed tests T507-T509;
`explorations/ghost-parity-physicality-push-2026-07-07.md`) to ONE crisp gate, and the
2026-07-13 cross-repo survey confirmed it is the residual:

> **is the mirror / ghost sector BRST-EXACT** (a first-class-constraint gauge artifact
> -> quotient -> REDUNDANCY -> ghost unphysical -> positive-definite restriction ->
> Krein grading NOT operative) **or BRST-COHOMOLOGY-NONTRIVIAL** (a genuine physical
> dof -> retain -> candidate RECORD -> Krein grading OPERATIVE)?

TaF's push leaned toward BRST-exact / redundancy ("two special bets, default is
redundancy") but recorded the decision as **fixed by the constraint / gauge structure
of the dynamics -- a named piece GU owns and can compute**, not by the full source
action. This wave computes GU's side. It makes no cross-repo identity claim; it computes
what TaF explicitly flagged as GU-owned (the tri-repo division of labor puts boundary
content and its exact mathematics on the GU side). Five personas ran inline;
deterministic test `tests/W173_brst_cohomology_mirror_sector.py`, 27/27, exit 0.

## 0. The one object, and the three constructions of "the mirror sector"

THE OBJECT: is the Krein grading OPERATIVE -- is the ghost a physical RECORD (`bar(b)`
clears) or gauge REDUNDANCY (tachyon physical / engine, `bar(b)` re-posed)?

| Construction of "the mirror sector" | BRST reading | Handling |
|---|---|---|
| (i) The **free BV bicomplex** GU has BUILT (`s = s_KT + s_long`, `s^2 = 0` on Cl(9,5), verified 1.18e-12) | compute `H^0(s)`; is the mirror closed-not-exact? | **the object GU actually determines** -- computed below (Part B) |
| (ii) The **stabilized / gauge-fixed** complex with the dynamics M_D | is the mirror removed by the secondary constraint C2? | **UNBUILT** -- needs the Y14 connection-curvature; the demotion channel (Part C) |
| (iii) The **C-metric / Krein-retention** quantization | is the ghost a positive-probability out-state under `eta_+ = eta C`? | conditional on the C-operator (W132; non-local, non-unique) -- Part D |

The verdict is stated per construction; that fork IS the result.

## 1. Persona 1 -- BRST/cohomology specialist: the free-complex computation

**The BRST operator GU has.** `bv-bicomplex-and-c2-obstruction-2026-06-27.md` constructs,
on the explicit `Cl(9,5) = M(64,H)` rep, the full BV differential `s = s_KT + s_long`:
the Koszul-Tate leg `s_KT` (antighost, resolves the stationary/constraint surface) and
the longitudinal leg `s_long` (ghost, along gauge orbits). Verified nilpotent:
`||s^2|| = 1.18e-12`, both legs nontrivial (`rank M_KT = rank A_W = 128`), Noether
identity `||B_W A_W|| = 1.7e-13`. So GU **does** determine a genuine, nilpotent free BRST
complex -- `Q` is not fabricated.

**Where the mirror sits.** From `canon/ghost-parity-krein-synthesis.md` (fact 3): the
generation-carrying triplet is a **totally null / neutral Krein subspace**, signature
exactly `(+96, -96, 0)`, each chirality half TOTALLY NULL; the form is purely the
cross-pairing between a generation and its mirror. So each of the 96 `(generation,
mirror)` pairs is a hyperbolic null pair `{u, v}`, `<u,v> != 0`, and the mirror is the
Krein-negative combination. The whole triplet sits INSIDE `ker(Gamma)` (the gamma-trace
irreducibility constraint; the triplet is the 192-dim sector of the 1664-dim `ker Gamma`).

**Is the mirror `s`-exact?** Two ways to be exact; both fail:

- **Koszul-Tate-exact?** NO. `s_KT`-exact directions are the EOM/off-shell directions
  that vanish on the stationary surface (Koszul-Tate is a resolution: `H_k(s_KT) = 0` for
  `k>0`, `H_0` = functions on the constraint surface). The mirror lies ON `ker(Gamma)`
  (the constraint surface), so it is not an off-shell / EOM-trivial direction. It is not
  in `im(s_KT)`.
- **Ghost-exact (pure gauge)?** NO, and this is the decisive GU-specific machine fact.
  `rs-gu-phys-brst-specification-2026-06-26.md` sec 3 computes, in BOTH the `Cl(4,0)` toy
  and the `Cl(9,5)` anchor, that the pure-gauge image `im(d_A)` is **TRANSVERSE to**
  `ker(Gamma)`: the RS symbol on the projected gauge image has norm **73.48** and
  **343.73** respectively, `!= 0` -- the gauge orbit ESCAPES the constraint surface. So
  within `ker(Gamma)` the gauge differential does not reach the mirror: `im(d_A)` points
  OUT of the surface the mirror lives on. The mirror is not `s_long`-exact.

**Is the mirror `s`-closed?** YES: it is on the constraint surface and no gauge direction
inside the surface moves it (the surviving null half is gauge-inert; the escape is the
COMPLEMENT of the pair, resolved by Koszul-Tate -- see below).

**Conclusion (Part B of the test, B0-B8, all PASS).** In the free BV bicomplex GU
actually determines, the mirror is **BRST-CLOSED but NEITHER Koszul-Tate-exact NOR
ghost-exact** -> it survives in `H^0(s)` -> **BRST-COHOMOLOGY-NONTRIVIAL -> a RECORD ->
Krein grading OPERATIVE.**

**Consistency with the bicomplex's own refined statement.** `bv-bicomplex` reports the
gauge ESCAPE is genuinely `s`-exact via the Koszul-Tate leg (`||(I - P) escape|| =
1e-13`) but NOT ghost-exact (`45.37`). The test reproduces exactly this (B6/B7): the
transversality (the escape) is a Koszul-Tate (co-exact) direction, i.e. it is the
OFF-SHELL complement of the pair that KT resolves -- NOT the on-shell mirror. This is
what makes the free complex close (`s^2 = 0`) WHILE leaving the on-shell mirror in
cohomology. The two facts are not in tension: KT kills the escape, not the mirror.

## 2. Persona 2 -- Krein/PT specialist: Krein-retention vs BRST-quotient, the ghost-parity Z2 (reusing W132)

The `records vs redundancy` fork is exactly the **Kugo-Ojima quartet** question. In a
standard first-class gauge theory the ghost/antighost form a BRST **doublet**; with a
partner the pair is a **quartet** that is `s`-exact and LEAVES the cohomology, so `H^0(s)`
is positive-definite -- REDUNDANCY. For GU's mirror to be redundancy, the ghost parity
`Z2` (the `generation <-> mirror` swap, `u <-> v`) would have to be REALIZED as a BRST
doublet: `s`(antighost) `~` mirror. The test's Part C is precisely this positive control
for the EXACT case: adding a doublet differential `delta` with `delta(w) = m` makes the
mirror exact and collapses `H^0` to the positive-norm state (C1-C4, PASS).

But GU's actual `s_long` does NOT pair `(generation, mirror)` within the constraint
surface (Part 1: `im(d_A)` transverse). And there is a structural reason the surviving
grading is a physical, not a gauge, grading: the synthesis update (V2, SUSTAINED x2)
established that **the Krein form `K` implements the Cartan involution of `so(9,5)`
(residual 0.0e+00) and equals the ghost parity on the triplet.** The Cartan involution is
a GLOBAL automorphism defining the non-compact real form -- not a local gauge
transformation. A global involution grades states into superselection labels (records),
whereas only a LOCAL gauge symmetry produces redundancy. So the `Z2` that grades the
mirror is, in GU, of the record type at kinematic grade -- the local-gauge-redundancy
route is the obstructed one.

**W132 binding (Part D, D1-D3, PASS).** Retention is NOT free. W132's exact identity
`A^dag A = P_+ + B^dag B` (reproduced here to 1e-6 on a constructed `eta`-pseudo-unitary
`S` with the ghost sector coupled, `B != 0`) shows the physical-subspace map is an
EXPANSION: keep-and-grade has NO physical-subspace unitarity resource except the
C-operator. So even the RECORD verdict carries W132's price: the record is only a
consistent positive-probability out-state under the non-local, degeneracy-non-unique
C-metric. Records-vs-redundancy and the unitarity price are the same object seen twice.

## 3. Persona 3 -- GU-structure specialist: does the (9,5) q=5 / soldering FORCE retention or quotient?

The task's subtlety (3): does a GU-structural datum pick the quantization?

- **(9,5) q=5 indefiniteness.** The internal form is genuinely indefinite (q=5 timelike;
  the Krein form exists ONLY because `G` is taken NON-COMPACT, per the A0 audit -- a
  scope-exit from Distler-Garibaldi's DG-A3). This is NECESSARY for the null pairing (a
  compact `G` / Hilbert space has no ghost at all: test D4/D5, PASS -- the effect vanishes
  under a positive-definite metric). But indefiniteness alone is NOT sufficient for
  retention: standard BRST starts indefinite and lands positive-definite. It sets up the
  null pair; it does not decide the cohomology.
- **Soldering.** The soldering identifies `K` with the Cartan involution (Part 2), a
  GLOBAL structure -> it leans RECORD, not quotient. It does not force the local-gauge
  quotient.
- **The Koszul-Tate leg** cannot reach on-shell states, so it forces nothing on the
  mirror (Part 1).

So no GU datum FORCES the quotient. The only quotient-forcing object is the secondary
constraint **C2 = `Gamma . M_D . Pi_RS`** (bare norm **155.36**, `Gamma`-INDEPENDENT,
two-construction-confirmed) -- the **BRST-invariance of the dynamics M_D**. C2 does NOT
close on the symbol algebra `(xi, M_D, Gamma)`; by two independent proofs (flat holonomy
insufficient; intrinsic KSp class cannot break the 5-fold null-pair symmetry) it needs an
EXTERNAL datum: the **GU connection-curvature 2-form on Y14 = Met(X4), selecting one
distinguished null plane (a spectral section).** That distinguished null plane is exactly
the choice that would pair `(generation, mirror)` into a BV doublet (quotient/redundancy)
or not (retention/record). It is the SAME kind of object as W132's C-operator (a
positive-metric / distinguished-subspace choice). GU's native cores cannot supply it:
big-swing R3 (SUSTAINED x2) found every GU-native core PT-unbroken yet **spectrally
sign-blind** (every eigenspace exactly K-balanced), and C exists but is **non-unique at
the spectral degeneracies** that ARE the three-generation regime. So GU's own dynamics
does not force the pairing; the demotion to redundancy requires importing the Y14 /
boundary datum -- which is the program's standing external-source thesis.

## 4. Persona 4 -- symbolic engineer: the test, controls, exit code

`tests/W173_brst_cohomology_mirror_sector.py`, 27/27, exit 0. Positive controls in BOTH
directions, per mandate:

- **Known nontrivial cohomology (record):** Part B builds the free complex where the
  mirror is closed-not-exact -> nontrivial (B5). Reproduces the two GU machine facts
  qualitatively: gauge-orbit transversality to `ker Gamma` (B1, toy of 73.48/343.73) and
  Koszul-Tate-exact-not-ghost-exact escape (B6/B7, toy of 1e-13 / 45.37).
- **Known BRST-exact ghost (redundancy):** Part C adds the doublet-pairing `delta` (a
  Kugo-Ojima quartet) -> mirror becomes exact, `H^0` positive-definite (C1-C4).
- **Negative controls:** positive-definite metric has NO ghost (D4/D5 -- the effect
  tracks the Krein indefiniteness, not a basis); Krein-sign flip swaps physical/ghost
  labels but leaves the free-complex nontrivial verdict INVARIANT (D6/D7 -- exactness is
  a property of `im(d_A)`, `im(s_KT)`, not of the metric sign).
- **W132 cross-check:** the expansion identity `A^dag A = P_+ + B^dag B` verified to 1e-6
  (D1-D3), binding the retention branch to its C-operator price.

The test is faithful (the null-pair, the transversality, the KT resolution, the doublet
demotion are all real linear algebra, not asserted); it is a TOY of the `M(64,H)` rep,
whose full computation lives in the cited `rs_bicomplex_spin95_connection_2form.py` and
`rs_gu_phys_brst_specification.py`. No number was reverse-engineered to a target; `q`
(the ghost count) is left free exactly as the BRST-spec leaves it.

## 5. Persona 5 -- adversarial skeptic: steelman BRST-EXACT / redundancy (TaF's default)

**The steelman, at full strength.** (a) A negative-norm state is, by textbook default
(Gupta-Bleuler, Kugo-Ojima), a GAUGE ARTIFACT; GU's mirror is negative-norm, so
presumptively gauge. (b) "Nontrivial in the FREE complex" is EXPECTED even for a genuine
gauge artifact BEFORE gauge-fixing and before imposing the secondary constraint -- the
whole point of the BV machinery (the KT leg, the C2 constraint) is to REMOVE such states;
so Part B is not evidence of a record, it is the generic starting point. (c) The KT leg
ALREADY resolved the gauge escape as `s`-exact -- the machinery is demonstrably designed
to kill these directions; extend it with the dynamics and the mirror likely goes too. (d)
TaF's push was honest and it leaned AGAINST the record: two compounding non-default bets
(Krein-retention AND self-normalized observer) are needed for "hidden record"; the
default corner is redundancy.

**Answer (why EXACT is also not certified).** Objection (b) is CORRECT and is exactly why
the verdict is QUANTIZATION-DEPENDENT, not "NONTRIVIAL, done." But the skeptic cannot
claim EXACT either: (i) the sole demotion channel -- the C2 secondary constraint that
would pair the mirror away -- does NOT close without the UNBUILT Y14 curvature, and by
two independent proofs cannot be built on the symbol algebra alone; (ii) GU's grading
`Z2` is the GLOBAL Cartan involution, and only a LOCAL gauge symmetry yields redundancy;
(iii) GU's native dynamics is spectrally sign-blind and gives a non-unique C at the
3-generation degeneracy, so it does not FORCE the pairing. The redundancy default is
therefore an assumption about the unbuilt action IMPORTED from textbook lore, not a
GU-forced computation -- symmetric to the record reading being unforced. The honest
statement: GU's determined content leans NONTRIVIAL (record); the demotion to redundancy
is possible but requires the external Y14 datum GU does not have. Neither is certified;
the default is not GU-forced.

## 6. Verdict

**QUANTIZATION-DEPENDENT -- deciding datum: the GU connection-curvature 2-form on Y14
(the secondary constraint C2 / the stabilized RS-IG source action), which fixes whether
`(generation, mirror)` is a BRST doublet.**

With the structural lean made explicit and honest:

- **At every level GU actually determines** (the built, nilpotent free BV bicomplex), the
  mirror is **BRST-COHOMOLOGY-NONTRIVIAL -> a RECORD -> Krein grading OPERATIVE.** This
  REVERSES TaF's redundancy default at the computed level: the mirror is on the constraint
  surface (not KT-exact) and GU's own gauge orbit is transverse to that surface (not
  ghost-exact).
- **The demotion to BRST-EXACT (redundancy) is not GU-forced.** It requires the UNBUILT
  Y14 curvature to close C2 AND pair the mirror into a BV doublet; GU's native cores
  cannot supply it (spectrally sign-blind; C non-unique at the 3-gen degeneracy).
- **Retention is not free** (W132): the record is a consistent positive-probability
  out-state only under the C-metric, which is non-local (W54) and non-unique at the
  degeneracy. The spectral section that closes C2 IS the C-operator W132 needs -- one
  external geometric datum governs both records-vs-redundancy and the unitarity price.

**Does GU force retention or quotient?** Neither, from native content. GU sets up the null
pair (forced by q=5 non-compactness) and grades it by the global Cartan `Z2` (leaning
record), but the quotient-forcing object (C2 / Y14 curvature / spectral section) is
external and unbuilt. The redundancy reading requires importing the SAME boundary datum
that supplies the chirality / generation count -- so `records vs redundancy` is decided at
the boundary, not inside GU. This is the program's external-source thesis, now sharpened
onto one object.

**Effect on `bar(b)`.** `bar(b)` is **NOT cleared and NOT simply re-posed -- it is
RELOCATED**, jointly with the generation-count boundary datum, onto the Y14-curvature /
C-operator question. If the Y14 curvature exists and pairs the mirror: BRST-EXACT ->
redundancy -> `bar(b)` re-posed (engine). If it does not: BRST-nontrivial -> record ->
`bar(b)` clears cohomologically, but its unitarity reading re-poses the C-operator
uniqueness question. Both branches route through one unbuilt geometric object.

**How it bears on TaF's T507-T509.** TaF's T508 asked a future packet to predeclare a
nilpotent `Q`, prove the mirror `Q`-closed, and decide exactness by membership in
`im(Q)`. GU's side answers, at the free-complex level TaF said GU owns: the nilpotent `Q`
EXISTS (the built BV `s`, `s^2 = 0` on `M(64,H)`); the mirror IS `Q`-closed and is NOT in
`im(Q)` (transverse gauge orbit + on-shell) -> the free-complex class is NONTRIVIAL,
which is the T508 "admit as review material" branch, and it REVERSES the sign of T507's
default lean (TaF leaned redundancy; GU's determined content leans record). T509's point
-- that full-Krein recovery does not descend through the quotient and W+ readout is not
exact-invariant -- is consistent: the record survives only under the C-metric / spectral
section, exactly W132's non-local C-operator. The tri-repo bit is thus computed on the GU
side WITHOUT moving any claim or asserting identity: the residual gate is one GU-owned
geometric object (Y14 curvature = spectral section = C-operator), and it is unbuilt.

## 7. What this does NOT do

No canon change; no claim / RESEARCH-STATUS / verdict / posture change; the ghost being a
record stays OPEN exactly as far as the Y14 source-action is unbuilt. No cross-repo
identity claim (the one-way rule is respected: TaF material is stress-test input; no GU
claim is cited as TaF evidence or vice versa). No recomputation of the `M(64,H)` BV
bicomplex here (that is the cited tests); no construction of `S_IG`, no generation count,
no closure of C2. The Cartan-involution / C-operator identification is ARGUED, not proved.
The test is a faithful finite toy of exact structural facts, not the full rep.

**Artifacts:** this file + `tests/W173_brst_cohomology_mirror_sector.py` (27/27, exit 0).
