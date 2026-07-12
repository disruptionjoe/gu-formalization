---
artifact_type: exploration
status: exploration
hypothesis: "Path-3 wave-2 (decisive): is SU(2)_+ a FORCED continuous gauge symmetry of the generation space?"
branch: "Path-3 wave-2 -- the single cross-shared swing settling discrete-Z/3 vs continuous-SU(2)_+"
created: 2026-07-11
title: "Path-3 wave-2: SU(2)_+ is GAUGED (spin connection) but gauging does NOT force the generation multiplet to be the adjoint Lambda^2_+. The forcing to rank 3 is CONDITIONAL on C1 (the generation bundle is an SU(2)_+-equivariant subspace of the adjoint, under the CONTINUOUS group) -- and C1 is not supplied by the framework: matter reps are free (Rep(SU(2)) has every dimension; the singlet is admissible), the sterile SU(2)_+-singlet sector survives gauging (anomaly-free, mod-3 Dai-Freed arena empty), and the frame SU(2)_+ acts on SPIN not FLAVOR. Under C1, Schur forces 3 (theorem). Verdict: NOT-FORCED / CONDITIONAL-ON-C1 with C1 unsupplied; the class-wide no-go stands; the count stays {1,3} = {singlet, adjoint}. The one native crack is GU's super-IG guardian ({Q,Q} ~ spin connection), an unestablished conjecture."
grade: "exploration / THEOREM for the two load-bearing math facts (Schur-forces-3-under-C1; gauging-never-forces-adjoint-matter -- elementary rep theory, machine-checked 14/14 in tests/W60_path3_wave2_su2plus.py); ARGUMENT for 'the framework does not supply C1' (rests on the generation-selection origin being torsion/internal rather than frame-covariant, which GU has not settled). No canon, RESEARCH-STATUS, CANON, claim-status, verdict, or public posture changed. The count stays OPEN, located-not-forced."
depends_on:
  - explorations/path3-branchD-homotopy-torsion-2026-07-11.md
  - explorations/path3-branchE-nogo-2026-07-11.md
  - tests/W58_path3_D_homotopy_torsion.py
  - tests/W59_path3_E_nogo.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
  - AGENTS.md
scripts:
  - tests/W60_path3_wave2_su2plus.py
---

# Path-3 wave-2 -- is SU(2)_+ a FORCED continuous gauge symmetry of the generation space?

**Role.** The five-branch blind wave (A-E) reduced "why three generations?" to a single fork. Branches
D and E, independently, named the **one** escape hatch from the class-wide no-go: promote the discrete
order-3 element (`Z/3 subset pi_3^s = Z/24`) to the **continuous** self-dual frame group
`SU(2)_+ = SO(3)`. Under the connected group `Lambda^2_+(R^4) = R^3` is irreducible, so any generation
content that is an `SU(2)_+`-equivariant subspace of the adjoint is forced to rank `3`. This swing is
**cross-shared** (not blind): I was handed D's and E's results and must settle whether that escape hatch
is a genuine first-principles forcing or a stronger assumption than the framework supplies.

## Construction used (fork discipline, per GEOMETER-VS-PHYSICS-OBJECTS.md)

I use the **gauged-chiral-frame** construction of both load-bearing objects, and I name where the
internal-global alternative would change the answer.

- **`SU(2)_+`** = the self-dual half of the local frame-rotation group `Spin(4) = SU(2)_+ x SU(2)_-`,
  gauged by the **spin connection**. This is standard 4D physics: local Lorentz **is** gauged. So
  `SU(2)_+` is a genuine *continuous, gauged* symmetry -- this part is not in doubt, and it is exactly
  what makes the escape hatch tempting ("the continuous group is handed to you for free").
- **"The generation space"** = a representation of that `SU(2)_+` *related to* `Lambda^2_+ = su(2)_+ =`
  the adjoint. The decisive ambiguity is **which** representation: the whole adjoint (rank 3), a
  sub-rep, or an external singlet (rank 1). The internal-global alternative -- a **new** internal
  `SU(2)` that is *not* the frame group -- is even weaker (a new gauged internal symmetry is not
  forced at all), so it cannot rescue the forcing; I note it and set it aside.

This is the fork the geometer-vs-physics table flags in the **Generation count** row (the count is a
3-primary *torsion* datum, not a `Z`-index) and the **graded/guardian** row (`{Q,Q} ~ Omega^1(ad) =`
spin connection). Both rows are load-bearing below.

## The anchor, reproduced independently

`dim Lambda^2(R^4) = C(4,2) = 6`, splitting under Hodge `*` (`*^2 = +1`) into self-dual `(+)`
anti-self-dual, each **dim 3**. Independently `Lambda^2_+ = su(2)_+`, the self-dual `so(4)` summand, and
`dim su(2) = 3 = 2j+1` at `j = 1` (the adjoint / spin-1 / vector irrep). So `3 = dim Lambda^2_+ =`
`dim adjoint SU(2)_+` -- the "3" is the **dimension of the adjoint of the self-dual frame group**,
derived from the 4-dimensionality of the base, not imported. This is the forced **ceiling** (agreeing
with D's 2a and E's B0).

## The crux, in one paragraph

`SU(2)_+` being gauged is **true and continuous**, but **gauging a group never forces its matter into
the adjoint**. `Rep(SU(2))` contains an irrep of every dimension `1, 2, 3, 4, ...`; the adjoint
(dim 3) is one choice and the **trivial (singlet)** rep (dim 1, sterile) is equally admissible. So "the
spin connection gauges `SU(2)_+`" does **not** make the generation multiplet `Lambda^2_+`. The **only**
thing that forces rank 3 is **Schur's lemma applied to the irreducible adjoint** -- and that bites only
**if** the generation carrier is already a nonzero `SU(2)_+`-equivariant *subspace of the adjoint*. That
"if" (call it **C1**) is precisely faithfulness/maximality in geometric clothing: the answer as a
premise. The framework does not supply it.

---

## Derivation 1 (representation-theoretic): gauging does not force adjoint matter; Schur is the forcing-IF

**Claim (specialist).** Under the *continuous* `SU(2)_+`, `Lambda^2_+ = R^3` is the vector rep, which
is **absolutely irreducible** (`End_{SU(2)_+}(R^3) = R`). By **Schur's lemma**, every
`SU(2)_+`-equivariant endomorphism of `R^3` is a scalar `lambda * Id`; hence every equivariant subspace
(and every equivariant-operator kernel/image) is `{0}` or all of `R^3`. The intermediate
`Z/3`-invariant subspaces -- the rank-1 fixed axis `V_0` and the rank-2 rotated plane `V_1` -- are
**not** `SU(2)_+`-invariant. So a nonzero equivariant subspace of the adjoint is **forced** to be all
of it: **rank 3.** *This is a genuine theorem.*

**Concrete verification (W60 D1c).** The `g`-fixed axis `(1,1,1)` is fixed by the order-3 element but
**moved** by a second `SO(3)` generator `h` (rotation by 90 deg about `x`). The pair `<g,h>` has **no
common invariant line** (0 real common eigen-directions), so the connected group acts on `R^3` with no
invariant line -- the intermediate `{1,2}` subspaces literally **dissolve**. This is exactly what
"promote `Z/3 -> SO(3)`" does to the *subspaces of `Lambda^2_+`*.

**Adversary.** *"Stop right there. Schur forces 3 only for a subspace **of the adjoint**. But gauging
`SU(2)_+` does not put the generations in the adjoint -- matter reps are free. `Rep(SU(2))` has an irrep
of every dimension; a generation sector can be a **trivial `SU(2)_+` singlet** (rank 1), a fundamental
(dim 2), or the adjoint (dim 3). QCD gauges `SU(3)_c` and does **not** force quarks into the octet;
leptons are color singlets. You have not forced the generations to be `Lambda^2_+`; you assumed it."*

**This attack stands.** The specialist's Schur theorem is real but **conditional**: it forces 3 only
**given C1** = *the generation multiplet is a nonzero `SU(2)_+`-equivariant subspace of the adjoint
`Lambda^2_+`, under the continuous group*. Gauging alone does not supply C1 (W60 D1a, D1d): the matter
rep is free, so `SU(2)_+`-gauging is compatible with rank 1 (singlet), 2, 3, ... . **D1 verdict:
FORCING IS CONDITIONAL ON C1.**

There is also a physical reason C1 is not automatic. The frame `SU(2)_+` acts on **spin** space (it is
the self-dual half of the *Lorentz* group). The three generations are three copies of the **same**
Lorentz/spin content, distinguished by an **internal, Lorentz-scalar** family label. A Lorentz-scalar
family index is, under the *frame* `SU(2)_+`, a **singlet** -- the frame group acts *trivially* on
flavor. To make the family multiplet transform in the *adjoint* of the frame `SU(2)_+` you must
identify an **internal** structure with a **spacetime** (Lorentz) one -- precisely the move
Coleman-Mandula forbids for ordinary symmetries. So the "continuous group handed to you for free" (the
frame rotation) is, generically, the **wrong group** to act on the generation count: on flavor it acts
trivially unless C1 is imposed by hand.

## Derivation 2 (consistency / anomaly): the sterile singlet survives gauging

**Claim (specialist).** Take the generation sector to be the sterile case D1's adversary named: a
**trivial `SU(2)_+` singlet** (rank 1). Does gauging the continuous `SU(2)_+` obstruct it?

- The singlet is a legitimate `SU(2)_+` module; the gauged group acts **trivially** (non-effectively)
  on it. Nothing in gauge theory forces `SU(2)_+` to act *effectively* or *irreducibly* on matter
  (W60 D2a).
- The sterile sector is **anomaly-free**: a one-generation (rank-1) content cancels every gauge and
  mixed anomaly, and the relevant **mod-3 Dai-Freed arena is empty** (repo R2:
  `Omega^Spin_5(BG_SM) (x) Z_(3) = 0`). No local or global anomaly forbids the axis (W60 D2b). This is
  E's B5b, reproduced under the *continuous* group.

**Adversary.** *"But under the connected `SU(2)_+` the fixed axis `V_0` is not even a subspace of
`Lambda^2_+` -- you (D1c) just proved it dissolves. So the rank-1 solution is gone!"*

**Rebuttal (the honest relocation).** Promoting `Z/3 -> SO(3)` removes `V_0` **as a subspace of the
adjoint**, but it does **not** forbid the rank-1 solution -- it **relocates** it. The one-generation
content persists as an `SU(2)_+` **singlet external to the adjoint** (an abstract trivial module, not a
line inside `R^3`). A singlet is a perfectly good matter rep, anomaly-free, consistent with the
continuous gauged group (W60 D2c). So the sterile rank-1 axis is **admissible either way**: as a
`Z/3`-subrep of `Lambda^2_+` under the discrete group, or as an external `SU(2)_+` singlet under the
continuous group. **It is not first-principles-forbidden.**

**D2 verdict: the sterile rank-1 sector survives gauging `SU(2)_+`. NOT FORCED.**

## The two derivations agree

- **D1 (rep theory):** matter reps are free; the singlet is admissible; Schur forces 3 only under C1.
- **D2 (consistency):** the sterile singlet survives gauging, anomaly-free, mod-3 arena empty; the
  rank-1 solution is relocated, not forbidden.

Both say: **gauging `SU(2)_+` does not force the generation multiplet to be the adjoint.** The odd
`SU(2)_+` options for a chiral generation sector are exactly `{1 (singlet), 3 (adjoint)}` -- the dim-2
fundamental is excluded by oddness / net-chirality (prior H37 leg). So the two independent routes
reproduce **exactly** D's and E's `{1,3}` menu, now stated in `SU(2)_+` representation language:
**`{1,3} = {singlet, adjoint}`.** The count is **not forced to 3.**

---

## The conditional, stated exactly

**Under C1, the count is forced to 3 -- and that part is a theorem.** C1 =

> *the generation bundle is a nonzero `SU(2)_+`-equivariant subspace of (equivalently, the kernel/image
> of an `SU(2)_+`-equivariant operator on) the adjoint bundle `Lambda^2_+`, with `SU(2)_+` the*
> **continuous** *gauged frame group.*

Given C1, Schur forbids any intermediate rank and matter-present forbids `{0}`, so `dim = 3` (W60 C1a).
This is the genuine content the escape hatch points at -- and it is genuinely first-principles **given
C1**.

**The framework does not supply C1** (W60 C1b):
1. The **torsion construction that reaches the count** (`Z/3 subset pi_3^s`, branch D) supplies only
   the **discrete** order-3 element, not the connected group -- the selection is `Z/3`-equivariant, not
   `SU(2)_+`-equivariant. `SO(3)` strictly contains `<g>`.
2. A **family/generation index is Lorentz-scalar (internal)**; the frame `SU(2)_+` acts on **spin**.
   On flavor space it acts trivially unless an internal structure is identified with the Lorentz group
   by hand.
3. **Gauging permits singlet matter.** Nothing makes the action effective/irreducible on the
   generation multiplet.

So C1 is **faithfulness/maximality in geometric clothing** -- "use the whole adjoint, no truncation" --
which E already isolated as a *naturalness posture*, not a consistency theorem. **The escape hatch is a
CONDITIONAL masquerading as a FORCING.**

## The one native crack (named, not closed)

There is exactly one place C1 could become first-principles *inside GU*: the **super-IG guardian**. The
geometer-vs-physics table (graded row) records that GU's graded symmetry has
`{Q,Q} ~ Omega^1(ad) = the spin connection` -- an internal-graded object tied to the frame geometry, a
structure that *does* mix internal and frame data in a way ordinary (Coleman-Mandula) reasoning would
forbid. **If** super-IG makes the family bundle **frame-covariant** (adjoint-valued,
`SU(2)_+`-equivariant), then C1 holds natively and rank 3 is forced (W60 C1c). But this is an
**unestablished conjecture** about GU's native graded structure, not a theorem -- and it is the sharp,
decidable follow-up the whole investigation now reduces to:

> **Does GU's super-IG guardian make the generation bundle an `SU(2)_+`-equivariant (adjoint-valued)
> object under the continuous frame group?** If yes -> C1 -> the count is forced to 3 (blockbuster). If
> no -> the count stays `{1,3}` and the class-wide no-go is final.

I did **not** find an argument that it does; the super-IG structure ties the *graded* bracket to the
spin connection, which is about the *guardian/gravitino* sector, not shown to make the *generation
family* bundle adjoint-valued. So the crack survives as an open question, not a forcing.

---

## Graded verdict

| Question | Verdict | Grade |
|---|---|---|
| **Is `SU(2)_+` gauged?** | **YES** -- it is the self-dual half of the local Lorentz group, gauged by the spin connection. Continuous, genuine. | THEOREM (standard 4D physics) |
| **Does gauging `SU(2)_+` force the generation multiplet to be the adjoint `Lambda^2_+` (=> count 3)?** | **NO.** Gauging never forces adjoint matter (`Rep(SU(2))` has every dimension; the singlet is admissible). The sterile `SU(2)_+`-singlet sector survives gauging (anomaly-free; mod-3 arena empty). | THEOREM (rep theory + consistency) |
| **Under C1 (generation bundle = nonzero `SU(2)_+`-equivariant subspace of the adjoint) is 3 forced?** | **YES** -- Schur: the irreducible adjoint has no intermediate equivariant subspace; nonzero => all 3. | THEOREM (Schur) |
| **Does the framework supply C1?** | **NO.** The reaching (torsion) construction supplies only discrete `Z/3`; the frame `SU(2)_+` acts on spin not flavor; gauging permits singlet matter. C1 = faithfulness/maximality = answer-as-premise. | ARGUMENT (strong) |
| **Is the sterile rank-1 axis first-principles-forbidden once `SU(2)_+` is properly gauged?** | **NO.** It is relocated (from a `Z/3`-subspace of the adjoint to an external `SU(2)_+` singlet), not forbidden -- and it is anomaly-free. | THEOREM (rep theory) + ARGUMENT (empty mod-3 arena) |
| **Overall** | **NOT-FORCED / CONDITIONAL-ON-C1 with C1 unsupplied.** `SU(2)_+` is gauged, but that pins the *ceiling/menu*, not the *value*; the count stays `{1,3} = {singlet, adjoint}`; the class-wide no-go is **final** unless GU's super-IG is shown to make the family bundle frame-equivariant (the one open crack). | see rows |

**Two-derivation agreement:** YES. D1 (rep theory: free matter rep, Schur only under C1) and D2
(consistency: sterile singlet survives gauging, anomaly-free) both conclude **NOT forced** absent C1,
and both reproduce the `{1,3} = {singlet, adjoint}` menu.

**Sterile rank-1 axis:** **admissible**, not first-principles-forbidden -- relocated to an external
`SU(2)_+` singlet under the continuous group; anomaly-free; mod-3 arena empty.

**Load-bearing assumption (for FORCING):** **C1** -- *the generation multiplet is the `SU(2)_+`
adjoint bundle `Lambda^2_+` (equivariant under the continuous frame group, nonzero)*, not a sub-rep and
not an external singlet. Not supplied by the framework. Everything hinges on C1.

**Confidence:** **HIGH** on the two theorems (gauging-does-not-force-adjoint-matter; Schur-forces-3-under-C1
-- elementary, machine-checked). **MEDIUM-HIGH** on "the framework does not supply C1": it rests on the
generation-selection origin being torsion/internal rather than frame-covariant, which GU has **not**
settled -- the super-IG graded row leaves a genuine (unexploited) crack. If a future result shows
super-IG makes the family bundle adjoint-valued, this flips to FORCED.

## What this does and does not change

Honest outcome, as pre-registered by the brief as the most likely one: **`SU(2)_+` being gauged does
not by itself force the generation multiplet to be `Lambda^2_+`; the sterile sub-rep/singlet stays
consistent; the count remains `{1,3}` and the class-wide no-go is the final word** -- *conditional on
C1 not being independently established*. The potential blockbuster (the multiplet forced to be
`Lambda^2_+`) is **not** delivered here: the only route to it, C1, is faithfulness/maximality in
geometric clothing unless GU's super-IG supplies it, which is unproven. No `3` was smuggled: the forced
`3` is `dim Lambda^2_+` (the ceiling); the realized count residual is `{1,3}`.

No change to `CANON.md`, `RESEARCH-STATUS.md`, claim status, verdicts, or public posture. The
generation count stays **OPEN**, located-not-forced, now with a sharpened demand on anyone who would
force it: **exhibit the first-principles reason the generation bundle is `SU(2)_+`-equivariant
adjoint-valued (C1) -- e.g. show GU's super-IG guardian makes the family bundle frame-covariant.**
Absent that, the number of generations is irreducible data given these principles.
