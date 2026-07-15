---
artifact_type: exploration
label: W237
created: 2026-07-15
status: exploration
posture: adversarial; truth-seeking; native-object first; construction-fork explicit; no verdict movement; does NOT decide the W235 record bit
title: "W237 channel-S condensate isotropy: the mirror-only (16bar)^4 SMG condensate is Z2-EVEN (chirality-preserving) but does NOT compactify the arena -- it has no SO(10)-singlet bilinear order parameter (channel B empty, W231), so its adjoint VEV is the singlet/zero level and it breaks 0 of the 4096 non-compact generators. The load-bearing new fact is a STRUCTURAL THEOREM: on a null pair, COMPACTIFY <=> Z2-ODD, because the unique compact-reduction direction is the Cartan involution P = tau1(null) which anticommutes with the grading Z = tau3(null); every Z2-EVEN bilinear is a singlet or a boost. So GU cannot get both natively through a null-pair bilinear: closing A1 dynamically requires the Z2-odd chirality-killer (channel D), and the chirality-safe channel S delivers no compactification. On the chirality-preserving branch (the W235 record reading), A1's dynamical residual is a GENUINE LOCATED FLAW: W224's singlet input-failure stands."
grade: "EXACT for the Z2-parity of channel S (integer charge (-1)^4 = +1, mirror-only) and for the structural theorem COMPACTIFY <=> Z2-ODD (the compactifier P = tau1(null) is Z2-odd; every Z2-even bilinear maps to {singlet, boost} in the definite/Krein basis; verified on the su(2)-triple algebra AND by the so(4,4) Cartan-involution/boost centralizer model: cent(P)=maximal compact, cent(boost) != maximal compact, cent(singlet)=full). STRUCTURAL for the lift 'a symmetric-mass-generation gap has no SO(10)-singlet bilinear order parameter (channel B empty, W231) => its arena adjoint VEV is the singlet/zero level => breaks 0 of the 4096 non-compact generators' (same toy status as W224/W234; inherits W231's machine-verified rep-theory singlet counts). CONDITIONAL on the W235 record bit for channel D's availability; channel S is Z2-even hence allowed on BOTH readings. OPEN for the interacting mirror-sector quartic dynamics, the source action, the physical state space, and the observable algebra. Machine regression: tests/W237_channel_s_condensate_isotropy.py (44/44, exit 0, positive controls first). No canon, RESEARCH-STATUS, verdict, bar(b), H59, or generation-count change; the W235 record bit is FLAGGED not decided."
depends_on:
  - explorations/W234-condensate-vev-isotropy-gate-2026-07-15.md
  - explorations/W235-central-bit-mirror-record-vs-redundancy-2026-07-15.md
  - explorations/W231-close-a3-smg-realization-gu-mirror-2026-07-14.md
  - explorations/W224-native-good-stable-dynamical-vacuum-2026-07-15.md
  - explorations/W219-native-good-stable-stabilizer-input-gate-2026-07-14.md
  - explorations/W228-close-a1-corrected-sign-gu-instance-2026-07-14.md
  - explorations/W216-true-vacuum-spectral-condensate-2026-07-14.md
  - explorations/W173-brst-cohomology-mirror-sector-2026-07-14.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W237_channel_s_condensate_isotropy.py
---

# W237 channel-S condensate isotropy

## Result in one paragraph

The knot resolves to **Z2-EVEN but does NOT compactify**, which makes A1's dynamical residual a
**genuine located flaw** on the chirality-preserving branch. W234 showed the only
compactification-capable condensate GU builds -- the good-branch mirror pairing `Delta = tau1(null)`
-- lands EXACTLY in the `~P` Cartan-involution direction (stabilizer the maximal compact
`Sp(32) x Sp(32)`, breaking the full 4096 non-compact block) but is Z2-ODD, hence W231's channel-D
gen-mirror Dirac direction: chirality-killing. This note asks whether the DIFFERENT condensate --
channel S, the mirror-only `(16bar)^4` SMG operator (W231, two `SO(10)` singlets, keeps the
generation chiral) -- can deliver the same compactification WITHOUT the Z2-odd cost. It cannot, and
the reason is a **structural theorem**, not a contingency. (1) **Z2 parity:** channel S is Z2-EVEN
(`(16bar)^4` carries Z-charge `(-1)^4 = +1` under `Z = tau3(null)`; it is mirror-only, connecting the
`-` sector only to itself, so a conserved `Z2` does NOT forbid it -- unlike channel D). VERIFIED, not
assumed. (2) **Isotropy:** channel S does NOT compactify. A symmetric-mass-generation gap has, by
construction, NO bilinear order parameter, and here that is forced by rep theory: the mirror bilinear
`16bar (x) 16bar` has ZERO `SO(10)` singlets (channel B empty, W231), so the `(16bar)^4` singlets
(from the real `10` and `120`) do NOT factor through a singlet bilinear -- their Hubbard-Stratonovich
auxiliary is a non-singlet `10`/`120` field whose symmetric-gap VEV must be zero (a nonzero one would
break `SO(10)` = channel B). So channel S contributes the ZERO adjoint to `Sp(32,32;H)`: its isotropy
is the FULL arena and it breaks 0 of the 4096 non-compact generators -- the SAME shortfall as W224's
singlet vacuum. The load-bearing NEW fact is why this is unavoidable: on a null pair, the unique
compact-reduction direction is the Cartan involution `P = sigma_3(definite) = tau1(null)`, which
**anticommutes** with the grading `Z = tau3(null)` (`{tau1, tau3} = 0`), so it is Z2-ODD; and every
Z2-EVEN bilinear commutes with `Z`, hence lies in `span{I, tau3(null)}`, which maps to
`{I (singlet), sigma_1 (boost)}` in the definite/Krein basis -- NEITHER of which is the compact
direction. **COMPACTIFY `<=>` Z2-ODD.** Therefore "Z2-even AND compactifies" (GU-gets-both) is
structurally blocked for any null-pair bilinear, and the chirality-safe channel S is confined to the
non-compact/singlet side. Conditional on the W235 record bit: on the record-CONSERVED reading (the
one W235 forces at kinematic grade, protecting chirality), channel D is forbidden and channel S does
not compactify, so **no native condensate delivers A1's dynamical good-stable** -- W224's input-failure
stands, and the dynamical good stable remains kinematic-only (W219/W228). The surviving non-compact
generators are the entire 4096-generator boost block, including the grading boost `Z` itself, whose
survival IS the preservation of chirality. `bar(b)`, `H59`, and the count remain OPEN / unchanged; the
W235 record bit is not decided.

## 1. Construction fork (mandatory)

The load-bearing object is the CHANNEL-S ORDER PARAMETER read as a Lie-algebra direction (or the
absence of one) of the internal arena, and it has the program's recurring Krein/native fork -- with a
twist specific to symmetric mass generation.

- **Standard-physics reading.** Treat the mirror gap as a mass term and look for the bilinear
  condensate `<mirror . mirror>` that Higgses the arena; then default to "some adjoint VEV forms and
  reduces `Sp(32,32;H)` to its maximal compact." This is the W224 physics-reading trap in a new place:
  it silently assumes a bilinear order parameter EXISTS. For channel S it does not.
- **Program-native reading.** Channel S is GU's mirror-only `(16bar)^4` four-fermion SMG operator
  (W231), acting on the Krein-negative half of the 96 hyperbolic null pairs `{u = generation,
  v = mirror}` in `ker(Gamma)` of `Cl(9,5) = M(64,H)` (W173), i.e. on the actual quaternionic fiber of
  `Sp(32,32;H)`. It is IRREDUCIBLY quartic: W231 machine-verified that `16bar (x) 16bar` has ZERO
  `SO(10)` singlets (no symmetric bilinear mirror mass exists -- the `16` is complex), while
  `(16bar)^4` has exactly TWO (from the real subreps `10` and `120`; the complex `126` contributes
  none). So the gap is a genuine four-fermion condensate with NO bilinear order parameter -- the
  defining feature of symmetric mass generation.

**Which side, and why.** The answer lives on the native side and is decisive in a way the physics
reading would miss BOTH directions. Because channel S has no bilinear singlet, it contributes no
adjoint VEV to `Sp(32,32;H)`: its arena isotropy is the FULL group and it breaks nothing. The physics
reading would have manufactured a compactification (the W224 trap) that native rep theory forbids.
Conversely the native reading also exposes the positive half of the knot -- that channel S IS
Z2-even and DOES keep chirality, which a crude "no order parameter, therefore nothing happens" reading
would under-state. Per the fork discipline, the kill is checked in the other construction: in the
bilinear-Higgs reading one would either invent a non-existent singlet mass (false compactification) or
be tempted by the mirror NUMBER operator `N_v = (I - tau3(null))/2` -- but that maps to
`(I - sigma_1)/2` in the definite basis (identity minus a BOOST), so it does not compactify either,
and it is a chemical potential, not a chiral gap. Either native route gives the same answer: channel S
does not reduce the non-compact block.

## 2. Channel-S Z2 parity (goal 1) -- EXACT

The grading is `Z = tau3(null) = diag(+1, -1)`: generation `u` carries `+1`, mirror `v` carries `-1`
(W234; W173's Cartan-involution / ghost-parity `Z2`). The Z-charge of a monomial is the product of the
charges of its legs:

```
channel S  = mirror-only (16bar)^4  ->  Z-charge = (-1)^4 = +1   =>  Z2-EVEN
channel D  = gen-mirror  16 . 16bar ->  Z-charge = (+1)(-1) = -1 =>  Z2-ODD
```

(checks S1a-S1c.) Channel S is Z2-EVEN, confirming the expectation but not assuming it: it is
mirror-only, so it connects the `-` sector ONLY to itself and never links `+` to `-`. A conserved `Z2`
superselection charge (the record reading) therefore does NOT forbid channel S (check S1d) -- in sharp
contrast to channel D, whose Z2-odd gen-mirror bilinear IS forbidden by a conserved `Z2` (W234/W231).
So channel S is an ALLOWED condensate on BOTH readings of the W235 record bit. This is exactly the
property that would let GU keep chirality: the massless chiral generation `u` (Z-charge `+1`) is never
paired away by a mirror-only even operator.

## 3. Channel-S isotropy (goal 2) -- does it compactify?

### 3.1 The structural theorem: COMPACTIFY `<=>` Z2-ODD

This is the load-bearing new result and it makes the whole knot structural rather than a case check.
Work on one null pair, the 2-dim space `span{u, v}`. The traceless bilinear directions are
`tau1(null), tau2(null), tau3(null)`. Under the grading `Z = tau3(null)`:

```
tau3(null)          commutes with Z  ->  Z2-EVEN
tau1(null)          anticommutes     ->  Z2-ODD    ({tau1, tau3} = 0)
tau2(null)          anticommutes     ->  Z2-ODD
```

Now transform to the definite (`beta`-eigen / Krein) basis by the fixed 45-degree hyperbolic rotation
`u = (e_+ + e_-)/sqrt2`, `v = (e_+ - e_-)/sqrt2` (W234, Block B). Under it:

```
tau1(null)  ->  sigma_3(definite) = P = diag(I, -I)   DIAGONAL  = the Cartan involution  (COMPACTIFIES)
tau3(null)  ->  sigma_1(definite)                     OFF-diag  = a BOOST                 (non-compact)
I           ->  I                                     singlet                            (breaks 0)
```

(checks S2, S3a-S3d.) The **unique compact-reduction direction is `P = sigma_3(definite)`** -- the
Cartan involution whose centralizer is the maximal compact `Sp(32) x Sp(32)` (W219/W224/W234). And
`P = tau1(null)` is **Z2-ODD**. Meanwhile every Z2-EVEN bilinear is a combination of `I` and
`tau3(null)`, i.e. `{singlet, boost}` in the Krein basis -- NEITHER of which is `P`. So no Z2-even
bilinear can be the compact-reduction direction:

```
COMPACTIFY  <=>  the direction is P (the Cartan involution)  <=>  Z2-ODD.
```

The theorem is given teeth in a faithful `so(4,4)` centralizer model (checks PC2-PC4, S3e-S3f): the
Cartan involution `P` has centralizer `= so(4)+so(4)` (the maximal compact, breaks the full coset);
the single traceless Z2-even direction (the boost image of `tau3(null)`) has centralizer `!=` the
maximal compact (non-compact directions survive); a singlet has centralizer the full algebra (breaks
0). Only the Z2-odd `P` compactifies. This is the deep reason W234's mutual exclusion cannot be
escaped by switching channels: compactification and Z2-oddness are the SAME statement on a null pair.

### 3.2 Channel S sits on the non-compact / singlet side

Channel S is Z2-even, so by Section 3.1 it cannot BE the compact `P` direction. Stronger: being an
SMG quartic with no bilinear singlet order parameter (W231: `16bar (x) 16bar` has 0 `SO(10)`
singlets), it contributes NO adjoint VEV at all. Its two `SO(10)` singlets live in `(16bar)^4` via the
real `10` and `120`; the Hubbard-Stratonovich auxiliary that would linearize them is a `10`/`120`
tensor field, NOT a singlet and NOT the adjoint `P`. A symmetric gap keeps `<10> = <120> = 0` (a
nonzero value would break `SO(10)` = channel B, the disfavored Eichten-Preskill branch, W231). So the
composite one-body order parameter channel S feeds into `Sp(32,32;H)` is the ZERO adjoint = the
singlet / identity level. Consequently (checks S4a-S4d):

```
channel-S arena isotropy  =  the FULL non-compact Sp(32,32;H)   (dim 8256)
non-compact generators broken  =  0   (of 4096)
```

exactly the W224 shortfall. The one Z2-even mirror bilinear that DOES exist, the mirror number
operator `N_v = (I - tau3(null))/2 -> (I - sigma_1)/2` (identity minus a boost), also fails to
compactify (check S4e) -- and it is a chemical potential, not a chiral gap, so it is not even an SMG
order parameter. Every route confirms the same negative.

### 3.3 Which non-compact generators survive

The entire 4096-generator non-compact coset (`4 * 32 * 32`, the off-diagonal quaternionic block that
mixes the two `Sp(32)` Krein factors) survives (check S5a). In particular the grading direction
`Z = tau3(null) = sigma_1(definite)` is itself a non-compact BOOST, and it MUST survive because
channel S is Z2-even (commutes with `Z`) -- and its survival IS the preservation of chirality (check
S5b). This is the geometric statement of the trade-off: to keep chirality you must keep the grading
boost `Z` unbroken; but leaving `Z` unbroken means leaving the non-compact block that `Z` sits in
unbroken; and to compactify you would have to condense in the direction `P` that anticommutes with
`Z`, i.e. gap along the grading, i.e. kill chirality.

## 4. The knot verdict, and reconciliation (conditional on the W235 record bit)

The four priors close into one coherent picture, decided by the single W235 record bit which this note
does NOT re-decide:

| W235 record bit | channel D (`~P`, Z2-odd) | channel S (`(16bar)^4`, Z2-even) | compactifies? | chirality | A1 dynamical good-stable |
|---|---|---|---|---|---|
| CONSERVED (record; W235 forces at kinematic grade) | FORBIDDEN (Z2-odd) | ALLOWED but breaks 0 | **NO** | KEPT | **NOT delivered -> W224 failure STANDS (genuine located flaw)** |
| BROKEN (redundancy; import-only, W235) | ALLOWED, compactifies `Sp(32)xSp(32)` | ALLOWED but breaks 0 | via D only | KILLED (channel D) | delivered only at the cost of chirality |

(checks D1-D10.) Reconciliation with each prior:

- **W234 (channel D / `~P`).** W234 gave the positive half: channel D lands in `~P` and compactifies,
  but is Z2-odd (chirality-killer). W237 gives the complementary half: the ONLY other candidate,
  channel S, is Z2-even (chirality-safe) but does NOT compactify. The two channels occupy opposite
  corners of the `(Z2-parity) x (compactifies?)` square, and Section 3.1's theorem proves the two
  desirable corners (Z2-even AND compactifies) is EMPTY for null-pair bilinears. W234's mutual
  exclusion is therefore not an accident of channel D -- it is structural, and switching to channel S
  does not escape it.
- **W224 (singlet input-failure).** Channel S delivers the SAME arena isotropy as W224's singlet
  vacuum: full `Sp(32,32;H)`, 0 of 4096 broken. So on the chirality-preserving branch W224's input
  failure STANDS -- now for a sharpened reason: not merely "the built vacuum is a singlet," but "the
  chirality-SAFE condensate is necessarily bilinear-order-parameter-free, hence isotropically a
  singlet." A1's dynamical residual is a genuine located flaw on that branch (check D5).
- **W231 (three-channel rep theory).** W237 takes W231's channel S (the good, chirality-preserving SMG
  channel) and adds the arena-isotropy fact W231 did not compute: Z2-even (chirality kept, as W231
  said) AND isotropically trivial (no compactification). The "favorable class" W231 placed GU in
  (direct symmetric transition, no bilinear) is exactly WHY channel S cannot supply the good stable:
  the very absence of a bilinear order parameter that keeps chirality also means no adjoint VEV to
  reduce the non-compact group.
- **W235 (the record bit).** Stated CONDITIONAL on W235 and NOT re-deciding it. W235 forces the record
  reading at KINEMATIC grade (chirality protected, channel D forbidden) and leaves the DYNAMICAL grade
  hinging on the unbuilt `F_A`/`C2` datum. W237 lives entirely at the level below that decision: it
  shows that GRANTING the favorable (record-conserved) reading, the remaining allowed condensate
  (channel S) still does not deliver A1's dynamical good-stable. So the located flaw is NOT an artifact
  of an unfavorable bit -- it survives on the favorable branch too.

## 5. Verdict

```
CHANNEL-S CONDENSATE ISOTROPY (mirror-only (16bar)^4 SMG condensate on Sp(32,32;H)):
  Z2 parity under Z = tau3(null)   : EVEN   ((-1)^4 = +1; mirror-only; allowed under a conserved Z2)
  arena adjoint order parameter    : NONE at bilinear level (channel B empty, W231) -> zero adjoint
  channel-S isotropy               : the FULL non-compact Sp(32,32;H) (dim 8256)
  non-compact generators broken    : 0  (of 4096)  -> DOES NOT COMPACTIFY
  surviving non-compact block      : all 4096 (4*32*32), incl. the grading boost Z itself
  => Z2-EVEN but does NOT compactify.

STRUCTURAL THEOREM (the load-bearing new fact):
  COMPACTIFY <=> Z2-ODD.  The unique compact-reduction direction is the Cartan involution
  P = sigma_3(definite) = tau1(null), which is Z2-ODD (channel D). Every Z2-EVEN bilinear maps to
  {singlet, boost} in the definite/Krein basis -> none compactifies. "Z2-even AND compactifies"
  (GU-gets-both) is STRUCTURALLY BLOCKED for any null-pair bilinear.

THE KNOT (conditional on the W235 record bit, NOT decided here):
  On the record-CONSERVED branch (chirality protected, W235's kinematic-forced reading), channel D is
  forbidden and channel S does not compactify -> NO native condensate delivers A1's dynamical
  good-stable. W224's singlet input-failure STANDS; the good stable remains KINEMATIC-only (W219/W228);
  A1's dynamical residual is a GENUINE LOCATED FLAW on the chirality-preserving branch.
```

This does not claim GU has no good stable, nor that GU is falsified (unbuilt `!=` false). It is the
narrower, computed result that the chirality-SAFE condensate GU could build (channel S) is
structurally incapable of compactifying the arena, so on the branch where chirality survives, no
native condensate closes A1's dynamical residual -- and the reason is the exact theorem that
compactification requires the Z2-odd direction that only the chirality-KILLING channel D provides.
`bar(b)`, `H59`, and the generation count remain OPEN / unchanged; the W235 record bit is not decided.

## 6. Joe-gated items borne on but NOT moved

- **The W235 record / redundancy bit** (is the Cartan-involution `Z2` a conserved superselection
  charge?): this result is stated CONDITIONAL on it and does NOT decide it. FLAGGED, not moved. W237's
  contribution is to show the located flaw survives even on the FAVORABLE (record-conserved) reading.
- **The W216/W211 Krein-sign branch** (good vs pathological): taken as the good branch for the
  geometry; not fixed here. Logically distinct from the record bit; kept separate.
- **H59 / bar(b)**: unchanged. This SHARPENS what H59 must build: not just "a compactifying
  condensate," but a compactifying condensate that is ALSO Z2-even -- which, by Section 3.1's theorem,
  cannot be a null-pair bilinear at all. No debit added or cleared; a located input-failure that
  survives the favorable branch is a sharpened gap, not a new falsification. FLAGGED, not moved.
- **Generation count / RESEARCH-STATUS / verdicts**: untouched.

## 7. Follow-up this unlocks

The structural theorem (COMPACTIFY `<=>` Z2-ODD for null-pair bilinears) says the good stable cannot
come from ANY Z2-even bilinear condensate. The only remaining routes to a chirality-safe dynamical
good stable are genuinely outside the null-pair-bilinear ansatz: (a) a HIGHER-rank / non-bilinear
order parameter (a fundamental-orbit or tensor VEV) whose stabilizer is compact-image yet Z2-even --
does such an object exist in `Sp(32,32;H)` at all, or does a Cartan-involution-type argument forbid
compact-image Z2-even orbits generally? (the highest-value next computation, and it may turn the
located flaw into a STRUCTURAL no-go); or (b) the arena is reduced by the DYNAMICAL vacuum isotropy /
observable algebra (the W235 / W219 front door) to a smaller group in which the compact-reduction
direction is no longer Z2-odd -- exactly the coincidence-admitting smaller-group escape W228/W235
flag. Both are finite-dimensional and Lean-portable (the operator identity `tau1(null) = P`, the
anticommutator `{tau1, tau3} = 0`, and the centralizer arithmetic are exact); a Lean port of the
theorem "compactify `<=>` Z2-odd on a null pair" is noted as follow-up only (no Lean/Lake run here,
per the machine-wide serialized-build rule; a sibling worker is concurrent).

## 8. Machine receipt

```
python -u tests/W237_channel_s_condensate_isotropy.py
```

44/44 checks passed, exit 0. Positive controls run FIRST and each fires on a real falsifier: the
Z2-parity detector is shown to correctly flag the KNOWN Z2-odd channel-D operator (`tau1`) as ODD and
an even operator as EVEN (so the "channel S is EVEN" verdict is not rubber-stamped); the
compactification detector is shown to see a real compactification (the Cartan involution `P` reduces
to the maximal compact in the `so(4,4)` model) and to correctly reject a boost and a singlet (so the
"channel S does not compactify" verdict has teeth). The actual checks then verify the channel-S Z2
charge `(-1)^4 = +1`, the structural theorem COMPACTIFY `<=>` Z2-ODD, the zero-adjoint isotropy from
the absent bilinear singlet, the full 4096-generator survival including the grading boost, and the
complete knot / record-bit truth table.

## Governance

Exploration grade only. No canon, RESEARCH-STATUS, verdict, bar(b), H59, or generation-count change.
The W235 record bit is flagged and coupled, not decided. No cross-repository identity asserted; the
reservoir Krein sign and the Y14 spectral-section / record datum stay gated temporal-issuance /
time-as-finality objects. bar(b) and H59 remain OPEN. Zero em dashes.
