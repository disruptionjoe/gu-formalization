---
artifact_type: exploration
status: exploration
created: 2026-07-11
wave: 17
title: "H40 (Wave 17 / terminal) -- can GU FORCE the source action's field-space declaration? NARROWED, not resolved. The Porrati-Rahman causal window is a genuine STRUCTURAL forcing of the cure requirement (the built C2=155.36 VZ leakage is a real acausality, so consistency demands a cure) -- it collapses the 4-corner field-space residual to the 2 causal cures {A,B}, but does NOT force the final constrain(B)-vs-gauge(A) bit. The field-space declaration is a B-LEANING LEAN, the fermion twin of the gravity soldering being a genuine postulate. The soldering and the gamma-trace are TWO independent declarations of one object (unifiable under one geometric-posture meta-postulate). The count STAYS {1,3} even in the full forced build. The program is one forced build from complete, but the build needs one unbuilt input: the source action's causal-cure term."
grade: "COMPUTED (exact, on the repo's verified Cl(9,5)=M(64,H) rep): the built VZ leakage C2=155.3625 and its degree-1 homogeneity; the ker-Gamma-constrained operator's ZERO leakage (cure B is causal); the even/odd sector split (codim-8165 soldering vs rank-1664 gamma-trace projector) and the leakage's independence of the soldering locus; the order-3 SO(3) eigenstructure on Lambda^2_+ (fixed axis + rotated pair) and the odd Z/3-equivariant ranks {1,3}; the residue trap. ARGUED (structural / evidence tier): that GU's Y14 background makes the leakage genuinely acausal (not a flat-background artifact); that the gauge cure (A) is also causal; the B-lean of the final bit; the geometric-posture unification of the two declarations; the constructibility wall. Reconstruction-tier, internal. No canon promotion; the generation count stays OPEN; SG4 unchanged."
depends_on:
  - tests/wave17/H40_terminal_sourceaction.py
  - explorations/wave16/H39-sourceaction-kclass-2026-07-11.md
  - explorations/wave10/H27-soldering-palatini-2026-07-11.md
  - explorations/wave12/H29-fermion-c2-wall-2026-07-11.md
  - canon/carrier-bit-decision-campaign-RESULTS.md
  - canon/gu-forces-field-space-declaration-RESULTS.md
  - papers/candidates/one-residual-complete-picture/one-residual-complete-picture-2026-07-11.md
scripts:
  - tests/wave17/H40_terminal_sourceaction.py
---

# H40 -- the terminal source-action build: is the field-space declaration FORCED, a LEAN, or a POSTULATE?

Test: `tests/wave17/H40_terminal_sourceaction.py` (deterministic, no randomness, exact; 14/14 PASS,
exit 0, ~3 s).

The whole GU program collapsed onto ONE unbuilt object -- the source action, whose two faces (gravity's
soldering, the generation count's K-class) are each located-not-forced modulo one declaration. Wave 16
(H39) proved they are the SAME object with two coherent faces and named the single remaining freedom:
**which field-space the source action declares** (gamma-trace-constrained / causal window -> carrier B;
full field space + BRST -> carrier A). A FREE choice p-hacks the carrier (the mutual-exclusion
certificate forbids it), so only a FORCED derivation resolves it. H40 is the honest attempt to force it.

The single new lever H40 lands: **the Porrati-Rahman causal window is a genuine STRUCTURAL forcing of
the CURE requirement, not merely a GU commitment** -- and that forcing does real work (it collapses the
field-space residual from 4 corners to 2), but it stops one bit short of the carrier. This is exactly
the gravity story one sector over: a forcing that reaches a clean conditional and no further.

## The four verdicts

### Q1 -- does GU's built structure FORCE the field-space declaration? NARROWED; the declaration is a B-LEANING LEAN [COMPUTED forcing of the cure + ARGUED B-lean of the bit]

The forcing lever is the causal window. The chain, computed on the verified rep:

1. **The built minimal Dirac symbol M_D LEAKS off the constraint surface [COMPUTED].** `C2 =
   ||Gamma M_D Pi_RS|| = 155.3625 != 0`, and since `Gamma Pi_RS = 0` (residual `1.1e-14`) this leak is
   the off-constraint push `||Gamma (Q M_D Pi_RS)|| = 155.3625` -- the Velo-Zwanziger constraint-leakage
   (H29's exact characterization). The VZ acausal-propagation trigger is **present in the built
   structure**, not an add-on.
2. **The leakage is background-dependent and genuinely acausal on GU's Y14 [COMPUTED degree, ARGUED
   physics].** `C2(2 xi)/C2(xi) = 2.0` exactly -- degree-1 in the covector, so the leak is nonzero on
   any nontrivial (curved / sourced) background, which GU's `Y14` structurally is. A massive RS field
   with nonzero VZ leakage propagates acausally (loss of hyperbolicity) -- an **inconsistency**, not a
   cosmetic feature. So a causal cure is **DEMANDED, not permitted**. Requiring causality here is a
   structural consistency condition (the standard the task specified), not an imported target.
3. **Cure B (the ker-Gamma / gamma-trace constraint = the Porrati-Rahman causal window) restores
   causality [COMPUTED].** Constrain the physical operator to preserve `ker Gamma`: the leakage of
   `Pi M_D Pi` is `||Gamma (Pi M_D Pi) Pi|| = 6.3e-14 = 0` exactly (because `Gamma Pi = 0`). The
   gamma-traceless field space **propagates causally**. That IS carrier B's field-space declaration.
4. **The cure FORKS, and the forcing collapses 4 corners to 2 [COMPUTED + ARGUED].** The uncured
   readings are acausal (leak `!= 0`): the bare full-`T_C` carrier (`-40`) and the uncured
   live-inconsistency corner are BOTH killed by the causality forcing. The two surviving corners are the
   two causal cures: constrain to `ker Gamma` (`-> B`) and gauge the constraint (`-> A`, whose local
   fermionic invariance removes the trace mode; causal -- ARGUED). So causality collapses the gu-forces
   4-corner residual `{A, B, bare-40, live-inconsistency}` to the **2 causal cures `{A, B}`**.
5. **But causality does NOT force the final bit [ARGUED].** Both surviving cures are causal, so
   causality cannot pick between them. Cure B (constrain) needs no local fermionic invariance; cure A
   (gauge) needs one -- the graded-IG `eps` sub-slot, which GU-as-stated does not state, and whose
   generic SUGRA form is amputated by GU's "no spacetime SUSY" commitment. The built leakage itself
   evidences an **ungauged-matter** reading (a gauged gravitino would gauge-fix the trace away rather
   than present it as a leakage). So the final bit is **B-leaning**, not forced.

**Verdict: NARROWED.** The causal window is a genuine forcing -- it upgrades causality from the
"GU commitment" H39 called it to a **structural forcing of the cure requirement**, and that forcing
removes two corners (the uncured/inconsistent ones), sharpening the residual from H39's 2-bit fork to a
clean 1-bit constrain-vs-gauge choice. But it does **not** reach the carrier. **The field-space
declaration is a B-LEANING LEAN, not a forcing** -- the fermion twin of the gravity soldering being a
genuine postulate (H27). This is forward motion (the forcing is real and does work) that stops honestly
short of resolution.

### Q2 -- does forcing carrier B ALSO discharge the gravity soldering? TWO independent declarations of one object [COMPUTED distinct + ARGUED unifiable]

- **Distinct objects, distinct sectors [COMPUTED].** The soldering is an **even-sector** (Clifford-even,
  bosonic) codim-8165 pinning of the connection `pi` onto the 91-dim spin-lift image inside the 8256-dim
  `sp(64,H)` (`dim so(14)=91`, `dim sp(64,H)=64(2*64+1)=8256`, codim `8165`; H23). The gamma-trace
  constraint is an **odd-sector** (Clifford-odd, fermionic) rank-1664 `ker Gamma` projector on `Cl(9,5)`.
  Per H29 the even sector is gravity and the odd sector is the fermion/C2 leakage: different Clifford
  parity, different mathematical type (a connection-locus vs a subspace-projector).
- **No implication either way [COMPUTED].** `M_D = kron(I, c(xi))` is built purely from the Clifford
  symbol and carries **no dependence on the soldering locus of `theta`**. So pinning `theta` onto the
  spin-lift (soldering) does not change the gamma-trace leakage, and constraining to `ker Gamma` says
  nothing about pinning `pi`. The two are **logically independent declarations** -- one does not entail
  the other.
- **But unifiable under one meta-postulate [ARGUED].** Both faces are the SAME choice -- the
  **geometric/tautological locus over the gauge-extended locus**. Soldering pins `pi` onto the geometric
  spin-lift reference (vs the free `sp(64,H)` family); carrier B constrains the RS field to the geometric
  gamma-traceless locus (vs the gauge-extended full/BRST space `-> A`). A single meta-declaration -- *the
  source action declares the geometric/tautological field space* -- discharges **both** coherently.

**Verdict: TWO logically-independent declarations of ONE object**, thematically unifiable under a single
geometric-posture meta-postulate. It is NOT a theorem that one implies the other (soldering + carrier-A
is logically available); the conservative count is two postulates, reducible to one under the natural
geometric posture. So the program's terminal object is one source action carrying two declarations that
*want* the same answer, not one declaration doing both jobs.

### Q3 -- if forced to B, does the count PIN to 3, or stay {1,3}? STAYS {1,3} [COMPUTED, trap avoided]

The full forced build: causal window imposed + the derived `Z/3` triplet `192 = 3 x 64` + reality
(`M(64,H)` Kramers) + carrier B's actual index. Computed:

- **Ceiling and carrier [COMPUTED].** `dim Lambda^2_+ = 3` (Hodge-star `+1` eigenspace, derived);
  `ind_B = -38 = 19 sigma/8` with `sigma = -16`; residue `1` (index-changing).
- **The order-3 action on the 3 chiral slots [COMPUTED].** The order-3 subgroup of the self-dual
  `SU(2)+` acts on `Lambda^2_+` (3-dim) as an **SO(3) rotation** with eigenvalues `{1, omega, omega^2}`:
  a **1-dim FIXED axis** (`+1`) plus a **2-dim rotated pair** (`omega, omega^2`). Verified `R^3 = I`,
  eigenvalues `(1, -0.5 +/- 0.866i)`.
- **The realized odd rank stays FREE in {1,3}, and the residue trap forbids certifying 3 [COMPUTED].**
  The real `Z/3`-equivariant invariant subspaces of `Lambda^2_+` have dims `{0,1,2,3}`; the ODD (chiral)
  ones are exactly `{1, 3}` -- the fixed axis (rank 1) and the whole triplet (rank 3). The mod-3 datum
  cannot break the tie: **a net index of exactly 3 has residue `0 mod 3`, which is the FIXED-axis /
  trivial (`j=0`) sector = carrier A's residue.** So no order-3 datum can distinguish "3 generations"
  from "1 generation + phase". `rho_B = (0, 2, 1)` engages the 2 rotated sectors, **not** the fixed axis
  where a genuine net-3 would sit.

**Verdict: STAYS {1,3}.** Even the full forced build does NOT pin the count to 3. The residue trap
actively prevents certification. This is the residual freedom that survives forcing B -- a real result,
reported honestly. Manufacturing "forces 3" here (reading `rho`'s engaged sectors or the ceiling-3 as
"three generations") is precisely the Wave-14/15/16 trap, and it is avoided.

### Q4 -- is H40 CONSTRUCTIBLE now, or does it need an unbuilt input? NOT fully constructible now [COMPUTED ledger + ARGUED wall]

- **All built machinery present [COMPUTED].** The spin-lift / `sp(64,H)` backbone (codim `8165`), the RS
  index backbone (`A=-42, B=-38` from `sigma=-16`), the `Z/3` triplet ceiling (`dim Lambda^2_+ = 3`), and
  the constraint machinery (`C2 = 155.36`) all reproduce.
- **The wall: GU has the TRIGGER, not the CURE [COMPUTED + ARGUED].** The built `M_D` **leaks**
  (`C2 != 0`) -- the VZ trigger is present -- but the causal-**cure** term is NOT in the built action. The
  cure that removes the leakage (Q1c's `Pi M_D Pi`) is imposed **by hand**; the built minimal dynamics
  does not impose it. The cure term (the non-minimal RS coupling that enforces `ker Gamma -> B`, or the
  graded-IG gauging `-> A`) is an **added term** the source action does not yet contain -- exactly the
  "unstated non-minimal couplings" the carrier-bit campaign named.

**Verdict: NOT fully constructible now.** The forced build reaches the causal-window forcing (the `{A,B}`
collapse) with current machinery, but the FINAL bit needs one unbuilt input: **the source action's
causal-cure term**, which by construction must be built so as not to p-hack the carrier. The program is
"one forced build from complete, but the build itself needs X first," and X is named precisely.

## COMPUTED vs ARGUED ledger

- **COMPUTED (exact, on the verified rep or by exact linear algebra):** the built VZ leakage
  `C2 = 155.3625` and its off-constraint identity; the degree-1 homogeneity `C2(2xi)/C2(xi) = 2`; the
  ker-Gamma-constrained operator's ZERO leakage (cure B is causal); the even/odd sector split
  (soldering codim `8165` in `sp(64,H)` dim `8256`; gamma-trace rank `1664`); the leakage's independence
  of the soldering locus (`M_D` is `theta`-locus-free); `dim Lambda^2_+ = 3`; the order-3 SO(3)
  eigenstructure (fixed axis + rotated pair); the odd `Z/3`-equivariant ranks `{1,3}`; the residue trap
  arithmetic; the constructibility anchors.
- **ARGUED (structural / evidence tier, not machine-decided):** that GU's `Y14` background makes the
  leakage a genuine acausality rather than a flat-background artifact (VZ acausality needs a nontrivial
  background, which GU has); that the gauge cure (A) is also causal (the gauge invariance removes the
  trace mode -- standard, not re-derived here); the B-lean of the final constrain-vs-gauge bit (rides
  GU's ungauged-matter posture + the no-stated-fermionic-invariance transcript fact + the built-leakage
  evidence); the geometric-posture unification of the two declarations; that the missing cure term is a
  genuine unbuilt input rather than an in-reach computation.

## Honest limits (do not overclaim)

1. **No carrier is forced.** Q1's forcing reaches the cure requirement and the `{A,B}` collapse, and no
   further. The claim "the source action names B" would still require BUILDING the cure term -- which a
   free build p-hacks. The B-lean is evidence, not a verdict; it is the same B-lean the carrier-bit and
   gu-forces campaigns already measured, now with causality upgraded from a commitment to a forcing.
2. **The causality forcing is a forcing of the CURE, not of the carrier.** Both `{A,B}` cures are causal.
   Reading "causality forces B" would be wrong: it forces "cure the acausality," which A and B both do.
   The forward step is precise and bounded -- two corners removed, one bit remaining.
3. **The Y14-acausality step is ARGUED, not computed end-to-end.** The leakage `C2 != 0` is exact, and
   its degree-1 homogeneity is exact; that this constitutes a genuine VZ acausality on GU's actual
   curved/charged `Y14` (rather than a removable flat-background coordinate artifact) is the standard
   Velo-Zwanziger physics, cited, not re-derived on the full bundle.
4. **Q3 does not produce a 3, and must not.** The order-3 structure narrows to odd/nonzero with a ceiling
   of 3, but the realized rank is free in `{1,3}` and the residue trap forbids certifying 3. The count
   stays genuinely OPEN even after forcing B.
5. **The geometric-posture unification (Q2c) is the strongest interpretive step.** It is a natural,
   coherent reading that one meta-declaration discharges both faces; it is NOT a proof that the soldering
   and the gamma-trace are the same postulate. They are computably independent (Q2a/Q2b).

## RE-RANK signal

**H40: NARROWED (not resolved).** The terminal object is now characterized as sharply as the built
structure allows, and the last freedom is located exactly.

- **Is the field-space declaration FORCED, a LEAN, or a POSTULATE?** **A LEAN (B-leaning).** The causal
  window forces the *cure requirement* (a genuine structural forcing: the built `C2` leakage is a real
  acausality, so consistency demands a cure), which collapses the field-space residual from 4 corners to
  the 2 causal cures `{A, B}`. But the final constrain(B)-vs-gauge(A) bit is a lean, not a forcing --
  both cures are causal. This is the honest fermion twin of the gravity soldering being a genuine
  postulate (H27): a forcing that reaches a clean conditional and no further.
- **Does the count pin to 3 or stay {1,3}?** **STAYS {1,3}.** The full forced build (causal window +
  `Z/3` triplet + reality + equivariance) narrows to odd/nonzero with ceiling 3, but the realized rank
  is free between rank-1 (the `Z/3`-fixed self-dual axis) and rank-3 (the full triplet), and the residue
  trap forbids certifying 3. The generation count remains OPEN.
- **Is the program "one forced build from complete"?** **One forced build from complete, but the build
  needs one unbuilt input.** Current machinery forces the fork to `{A,B}`; the terminal object needs the
  source action's **causal-cure term** (the RS non-minimal coupling that enforces `ker Gamma`, or the
  graded-IG gauging), which is not yet built. So: one forced build away, and the build itself needs X.
- **The single next object.** The **causal-cure term of the source action** -- a GU-internal derivation
  of the RS matter's non-minimal (field-space-defining) coupling, built so as not to p-hack the carrier.
  If that term is forced by GU's structure to be the `ker Gamma` projection, the carrier is B and the
  count face becomes a conditional theorem on a single forced declaration; if it admits the gauging
  alternative, the declaration stays a genuine 1-bit postulate. Either outcome resolves the terminal
  freedom; neither is reachable without building the term.
- **No canon movement, no generation-count movement, no public-posture change.** SG4 unchanged; the
  generation count stays OPEN (located, not forced). The one-residual flagship's framing is unchanged in
  substance and sharpened in one phrase: causality is now a *forcing of the cure requirement* (collapsing
  the field-space residual to `{A,B}`), and the terminal freedom is the causal-cure term, a B-leaning
  1-bit postulate.

---

*Filed 2026-07-11. Wave 17, the terminal source-action swing. Reproducible:
`python tests/wave17/H40_terminal_sourceaction.py` (exit 0, 14/14 PASS). Exploration-grade; not promoted
to canon. Adversarially graded: no forcing was manufactured (the causality forcing is of the cure, not
the carrier), no target imported (the only `3` is `dim Lambda^2_+`; no `24 / 24-8 / 155.36` as a target
-- `155.36` appears only as the built leakage magnitude, never fit to anything), and the count was NOT
p-hacked to 3 (it stays `{1,3}` and the residue trap is made explicit). The honest outcome: the
field-space declaration is a B-leaning LEAN, the terminal object is one unbuilt causal-cure term away,
and the loop caught its own would-be wrong guess (the "order-3 forces 3" temptation) and refused it.*
