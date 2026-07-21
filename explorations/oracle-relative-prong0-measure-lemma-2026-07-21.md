---
title: "Prong 0 (oracle-relative swing): the measure-lemma FAILS at clause (c) and the failure is SHARPER than 'theta external' -- GU DOES own a native measure (the DeWitt (9,5) volume w=sqrt|det G| ds, unique up to scale) but the sign of q is measure-INVARIANT, so no measure touches the sector clause; the GENUINE noncompact ends of F=GL(4,R)/O(3,1) are the diagonal FLAT geodesics (O(3,1) boosts are ISOMETRIES that fix the base metric and leave q invariant -- they are NOT ends, a correction to the loose 'boost directions' phrasing), and the timelike-dominant flats cross into q<0 generically (~8% of random genuine ends, on and off the Weyl slice); at q<0 the Krein form K_S is EXACTLY null on the very spectral halves the section cut is built from (residual 9e-16), so on those ends the operator A~=-iK_uG d_s + W~ is not merely non-self-adjoint, it is NOT CONSTRUCTIBLE from committed structure at all -- the K-definite cut that defines it does not exist. On GAPPED ends the Krein deficiency indices ARE equal (limit-point, theta dissolves there; the Q1a win's surviving-sector lean is conceded). Verdict P0-FAILS-OBSTRUCTED: OPERATOR-END-PENCIL does NOT close from structure; the only rescue is an IMPORTED excision of the timelike-crossing ends, which GU does not own (the P=0/q<0 stratum is the still-open N2 operator-lift gap)."
status: active_research
doc_type: exploration
created: 2026-07-21
prereg: explorations/prereg-oracle-relative-thesis-swing-2026-07-21.md
verifies_lemma_from: explorations/decision-tree-Q1a-hostile-verify-2026-07-21.md
inputs:
  - explorations/prereg-oracle-relative-thesis-swing-2026-07-21.md
  - explorations/decision-tree-Q1a-hostile-verify-2026-07-21.md
  - explorations/decision-tree-Q1a-fiber-end-classification-2026-07-21.md
  - explorations/sector-relative-section-theory-2026-07-20.md
  - explorations/n2-end-family-2026-07-20.md
  - canon/source-action-seiberg-witten-construction.md
  - tests/channel-swings/n2_end_family_probe.py
  - tests/channel-swings/decision_tree_Q1a_hostile_verify_true_end_probe.py
probe: tests/channel-swings/oracle_relative_prong0_measure_lemma_probe.py (foreground, deterministic two-run-identical, EXIT 0)
outcome: P0-FAILS-OBSTRUCTED
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
kill_conditions_declared_before_computation: true
---

# Prong 0 -- the measure-lemma, proved-or-refuted

Adversarial truth-test, maximum skepticism (a `P0-HOLDS` would be a paper, so it
gets no benefit of the doubt; the two prior wins this session were both refuted
for planting). This run attacks the exact reopen lemma the Q1a hostile verify
named, the single lemma that decides whether the pencil theorem
`OPERATOR-END-PENCIL` closes from GU structure (θ=0) or stays open (θ external),
or -- the sharper possibility -- whether the operator has no self-adjoint
realization at all.

## 0. Verdict up front

> **`P0-FAILS-OBSTRUCTED`.** GU **does** own a native measure -- the DeWitt
> (9,5) volume `w(s) = √|det G(s)| ds`, unique up to scale -- so the lemma does
> **not** fail for lack of a measure. It fails at **clause (c)**, and it fails
> **structurally**, in a way no measure can repair:
>
> 1. **The measure is orthogonal to clause (c).** `w(s)` multiplies the positive
>    L² weight; the sector datum `q = P − T` is built from the symbol `D=c(ξ)`
>    and `K_S` **alone**, with no reference to any measure. So the **sign of `q`
>    is measure-invariant**: no positive `w(s)` (native or imported) can move a
>    genuine end from `q<0` to `q>0`, nor un-null an indefinite pairing.
> 2. **Clause (c) is false.** The genuine noncompact ends of `F=GL(4,R)/O(3,1)`
>    are the diagonal **flat** geodesics `exp(sH)·o`, `H∈p` (η-symmetric). The
>    O(3,1) **boosts are isometries** -- they fix the base metric and leave `q`
>    exactly invariant (probe C0: `q≡30.13`), so they are **not ends** (a
>    correction to the prereg's loose "boost directions" phrasing). Among the
>    genuine flat ends, the **timelike-dominant** ones cross into `q<0`
>    (probe C1), and this is **generic**: ~8% of random genuine ends cross,
>    on and off the Weyl slice (probe C2). GU's own end-space is **not**
>    contained in the spacelike-gapped sector.
> 3. **The failure is sharper than "θ external."** At a `q<0` end the Krein form
>    `K_S` is **exactly null** on the spectral halves `E_{±i}(D)` (probe C3,
>    residual `8.9e-16`) -- the n2 K-null little theorem, re-verified. Those
>    halves are **what the K-definite section cut is built from**; where they are
>    null, **no cut exists**, so `K_u = K_S c_s/√P` provides no spectral splitting
>    and the operator `A~ = -iK_uG ∂_s + W~` is **not constructed from committed
>    structure at all** on those ends. This is not "an external datum θ must be
>    imported into a well-posed operator"; it is "the operator itself is ill-posed
>    at the genuine ends without an external datum."
>
> **On the surviving sector the Q1a win is conceded.** On gapped ends the reduced
> J-symmetric end is hyperbolic and the Krein deficiency indices are **equal**
> (probe A2: `n₊=n₋=1`, limit-point); θ dissolves **there**. The obstruction is
> not that the win is wrong on its sector -- it is that GU's genuine end-space is
> **not** its sector.
>
> **Consequently `OPERATOR-END-PENCIL` does NOT close from structure.** The only
> rescue is an **imported excision** of the timelike-crossing ends (or a genuinely
> new "third costume" for the `q<0` stratum). GU does **not** own that excision:
> the `P=0`/`q<0` stratum is the still-open operator-lift gap the sector-relative
> theory named (Sec. 7.1, 7.3). That is the exact external datum, stated once.

## 1. The native-measure search (does GU own `w(s)ds`? -- YES, and it doesn't help)

The lemma's clause (a)/(b) presuppose a measure to define "J-self-adjoint" and
"measure-normalized bounded." The honest first question: is there a GU-native one,
or must it be imported?

**There is, and it is not close to arbitrary.** A J-self-adjoint problem needs two
things a Krein/L² setup separates cleanly: a **positive density** `w(s)` (the L²
measure) and an **indefinite fiber pairing** `J`. GU's frozen (9,5)/Krein
structure supplies **both, canonically**:

- `J = K_S` -- the Krein form, already committed (`K = η_V⊗β_S`, the frozen
  object). Native, not a choice.
- `w(s) = √|det G(s)|` -- the **Riemannian volume density of the DeWitt (9,5)
  form** `G` (equivalently the `GL(4,R)`-invariant measure `|det g|^{−5/2}∏dg` of
  the symmetric space, restricted to the ray). This is the canonical density a
  Dirac operator carries; it is **unique up to a constant scale**. It is **not**
  chosen to make (a)/(b)/(c) come out true.

Probe **N1**: along the conf-up ray `d/ds log|det G| = −16.0` exactly (log-linear),
so `w(s)~e^{−8s}` -- a well-defined native radial density contributing exactly one
fixed scalar **drift** term `−(1/2)(w'/w)B` to the operator gauge. (The sign is a
gauge fact about the conformal frame scaling, `hor~e^{s}`, `vert~e^{−2s}`; nothing
in the verdict turns on it.)

**But the measure is orthogonal to the load-bearing clause.** Probe **N2**: `q(s)`
is `⟨ξ,ξ⟩_{9,5} = P−T`, a function of the **symbol and `K_S` alone**. Explicitly
`q` is negative on the timelike ray (`36.1 → 32.8 → 1.5 → …<0`) and positive on
conf-up, with **no measure anywhere in its definition**. A positive `w(s)`
rescales `∫|ψ|²_{K} w ds`; it cannot change the sign of `q` or turn a `K_S`-null
pairing into a definite one. **Whatever the native measure is, clause (c) is
untouched by it.** This is the pivotal structural observation: the measure
question and the sector question are independent, and only the sector question
carries the obstruction.

*(A measure chosen to force (a)-(c) would be planting. We reject that route
explicitly: the only measure used here is the metric volume, and it is shown to be
irrelevant to (c) precisely so that no measure-choice can be doing hidden work.)*

## 2. The true-end sector analysis (clause (c) -- the crux) with the boost correction

The prereg and HV phrase the genuine ends as "the noncompact isotropy O(3,1) boost
directions." **That phrasing is geometrically off, and correcting it sharpens the
result rather than dodging it.**

**Boosts are isometries; they are not ends.** `O(3,1)` is the **isotropy** of the
base point of `F=GL(4,R)/O(3,1)`: a boost fixes the base metric and acts as an
isometry of the (9,5) form. So along a pure boost the section datum `q` is
**exactly invariant** -- probe **C0**: `q≡30.13` for rapidity `η=0…3`. A boost
generates no degeneration and reaches no boundary; it is not a fiber end.

**The genuine noncompact ends are the diagonal FLAT geodesics** `exp(sH)·o` with
`H∈p` (the η-symmetric complement of `o(3,1)` in `gl(4)`). The diagonal matrices
lie in `p` (η is diagonal), and `exp(s·diag(α))` is unbounded -- these are the
genuine noncompact ends the n2 probe already sampled. Their causal type is a genuine
`Ad(O(3,1))`-invariant: a spacelike-dominant stretch `diag(1,1,1,0)` and a
timelike-dominant stretch `diag(0,0,0,1)` have different eigenvalue multiplicities,
so they are **distinct, non-conjugate** ends -- the timelike ones cannot be rotated
to gapped ones.

**And the timelike-dominant genuine ends cross `q<0`** (probe **C1**):

| genuine flat end `exp(s·diag(α))·o` | `P` | `T` | `q` | sector |
|---|---|---|---|---|
| conf-up `(1,1,1,1)/2` (spacelike-dom.) | `5.6e3` | `36` | `+5.6e3` | gapped |
| shape `(1,1,−1,−1)/2` (traceless) | `2.8e5` | `1.3e5` | `+1.5e5` | gapped |
| **timelike `(0,0,0,1)`** | `39` | `1.5e4` | `−1.5e4` | **crossed** |
| **tl-tilt `(.3,.2,.1,1)`** | `1.1e2` | `1.5e4` | `−1.5e4` | **crossed** |

Note the **absolute** `P` is printed: on the crossed ends `P` stays `>0`, so
`B=-iK_uG` remains non-degenerate (the Q1a win's step (i), `‖B‖=‖B⁻¹‖=1` where
`P>0`, is robust and un-contested). **The failure is not `B` degenerating** -- it
is `q<0`, the K-null sector, upstream of `B`.

**Crossing is generic, not a diagonal-slice artifact** (probe **C2**, addressing
the n2 "null-shear rays not sampled" nonclaim): over 2000 random genuine ends --
half of them conjugated off the Weyl slice by a random `O(3,1)` boost, which keeps
them genuine `p`-directions -- **~8% cross into `q<0`** and 6% fall below the
`ρ=0.36` "floor" the Q1a win read as universal. A positive-measure set of GU's
genuine noncompact ends is outside the spacelike-gapped sector. **Clause (c) is
false.**

**At `q<0` the Krein form degenerates on exactly the halves the cut needs**
(probe **C3**): `K_S D` is Hermitian (residual `0`) and the eigenvectors of `D`
with `Im>0` satisfy `⟨x,K_S x⟩ = 0` to `8.9e-16` -- the halves `E_{±i}(D)` are
**exactly `K_S`-null**. This is the n2 little theorem (imaginary spectrum +
`K_S`-Hermitian symbol ⇒ null halves). The K-definite cut `Q_±` that builds
`K_u`'s spectral splitting **does not exist** there.

## 3. The Krein deficiency indices (clause (a)) -- equal on gapped, ill-posed on crossed

The HV correctly warned that the Hermitian reduction is blind to the genuine
J-symmetric count, and that J-symmetric deficiency indices `(n₊,n₋)` can be
**unequal** (⇒ no J-self-adjoint extension). Probe **A** works the genuine
`J=K_S` structure, with kill-conditioned controls declared before GU's case.

**Controls (A0) -- the counter distinguishes the three outcomes:**

| model | `n₊` | `n₋` | reading |
|---|---|---|---|
| hyperbolic Dirac, real bounded mass | 1 | 1 | **equal → limit-point** |
| oscillatory + fast-decaying measure | 0 | 0 | equal (measure symmetric at `±i`) |
| **`−i d/ds` on `(0,∞)`** (massless, one-sided drift) | **1** | **0** | **UNEQUAL → no self-adjoint extension** |

The `−i d/ds` control is the concrete realization of the HV's "indices can be
unequal": `−i u' = i u ⇒ u=e^{−s}∈L²` (one deficiency solution), `−i u' = −i u ⇒
u=e^{s}∉L²` (none). A first-order half-line end with a one-sided drift and **no
balancing conjugation** lands at `(1,0)` and admits no self-adjoint realization.
The counter is not rigged: it returns equal for the hyperbolic case and unequal
only when the balancing structure is absent.

**GU gapped end (A2): equal indices, limit-point.** On `q>0` the section symbol
`M/√q` is a `K_S`-self-adjoint involution; the reduced Dirac block is hyperbolic
(`B~-iσ_z`, real bounded normalized mass). Probe: `n₊=n₋=1`. **Equal → limit-point
→ θ dissolves on the surviving sector.** The Q1a win's structural lean is conceded
exactly where it lives.

**GU crossed end (A3): the operator is not constructible from committed
structure.** Here maximum-skepticism discipline forbids the move the prior wins
made. I do **not** fabricate a 2×2 crossed model and read an index off it -- that
would plant the answer (as the win planted bounded coefficients). What committed
structure establishes, and only this:

- the `n₊=n₋` guarantee for a J-symmetric operator requires a **J-real conjugation
  on the deficiency spaces**;
- `K_S` is **exactly null** on those halves (C3), so the conjugation's domain
  degenerates and the guarantee is **void**;
- the generic fate of a first-order end that has lost the balancing structure is
  unequal indices -- the `−i d/ds → (1,0)` control exhibits it concretely.

Deciding the **actual** crossed indices requires the **operator lift** -- the open
N2 gap (sector-relative Sec. 7.1: promote `zM(t,s)` to an APS-type boundary
condition for a genuine Dirac operator whose symbol changes Krein type). That is
not fixed by committed grade, and honesty forbids asserting a number. The load-
bearing fact is upstream anyway: on the crossed ends there is **no cut**, so there
is **no J-symmetric operator `A~` to compute indices for** in the first place.

## 4. Both steelmans (mandatory)

**Steelman "the lemma HOLDS" (`P0-HOLDS`).** The strongest case: (i) GU owns a
native measure (Sec. 1 -- true, conceded). (ii) On the surviving spacelike-gapped
sector the indices are equal and the end is limit-point (Sec. 3/A2 -- true,
conceded). (iii) *If* the genuine ends were confined to that sector, θ would
dissolve and the pencil would close. The case rests entirely on (iii): that the
crossing/timelike ends are **not genuine** -- e.g. removable as a measure-zero or
non-physical stratum. **Why it fails:** the crossing set is **not** measure-zero
(C2: ~8% of genuine ends, an open set -- the surviving sector is open, but so is
its complement), and the timelike-dominant ends are **genuine, non-conjugate**
noncompact geodesics (distinct `Ad(O(3,1))` type). Excising them is an act of
**importing** a boundary prescription, not a structural fact -- and the sector
theory explicitly lists that excision as an **open** problem (Sec. 7.3, "the `P=0`
stratum needs either an excision argument or a third costume"). So `P0-HOLDS`
requires an import GU does not own; it collapses to `P0-EXTERNAL` at best, and the
cut-nonexistence (C3) pushes it past that to `OBSTRUCTED`.

**Steelman "the lemma FAILS-OBSTRUCTED".** The strongest case (adopted): clause
(c) is false on a positive-measure set of genuine ends (C1/C2); at those ends the
K-definite cut does not exist (C3), so the defining section datum of `A~` is
absent -- the operator is not merely non-self-adjoint but not constructed; and no
measure can repair a sign of `q` or a null pairing (N2). The residual doubt -- "is
it OBSTRUCTED or merely EXTERNAL?" -- turns on whether excising the timelike ends
is owned. It is not (Sec. 7.3 open). **The honest resolution:** the sharpest true
statement is OBSTRUCTED (operator ill-posed at genuine ends from committed
structure), with the explicit EXTERNAL fallback named: *if* one imports an excision
of the `q≤0` stratum (unowned), the residual gapped-sector operator has equal
indices and limit-point (A2), and θ dissolves on what remains.

## 5. Verdict, and what it does to the bit-budget

- **Outcome: `P0-FAILS-OBSTRUCTED`.** The measure-lemma fails at clause (c). GU
  owns the measure (`√|det G| ds`, unique up to scale) but the measure is
  provably orthogonal to (c); the genuine noncompact ends cross into the `q<0`
  K-null sector generically; and there the operator `A~` is **not constructible
  from committed structure** (the cut that defines it does not exist). This is a
  **sharper** obstruction than "θ external": the operator is ill-posed at the
  genuine ends without an external datum.
- **Does `OPERATOR-END-PENCIL` close from structure?** **No.** It closes only on
  the spacelike-gapped sub-sector, and only after **importing** an excision of the
  timelike-crossing ends -- the still-open N2 operator-lift / `P=0`-stratum gap.
  The Q1a `HV-REFUTE` disposition stands, now with the reopen lemma **decided in
  the refuting direction at clause (c)**: the lemma is not merely unproven, its
  sector clause is false on GU's genuine end-space.
- **Bit-budget consequence (stated, not banked).** θ is not `0` from structure.
  The sharpest reading is not "θ is a continuum of boundary phases" (the
  limit-circle horn) but "the operator has no committed-structure realization at
  the timelike ends" -- so the external datum is not a phase but a **prescription
  for the `q<0` stratum** (excision, or a third-costume regularization of the null
  Krein form). That datum's type -- one discrete excision choice vs a continuum --
  is exactly the open operator-lift question; Prong 0 fixes **that this datum is
  required and external**, not its cardinality. The budget is `σ + τ + θ_ext` with
  `θ_ext` = "the `q<0`-stratum prescription," a genuinely external, currently
  unowned datum.

## 6. What survives / what falls (once, truth-seeking)

- **Survives (keep):** GU owns a native measure `√|det G| ds` (unique up to
  scale). On the spacelike-gapped sector the J-symmetric deficiency indices are
  equal → limit-point → θ dissolves *there* (the Q1a win, correctly scoped). `B`
  non-degeneracy where `P>0` (the one Q1a-HV survivor) is re-confirmed and is
  **not** the failure locus.
- **Falls (do not ship):** "a native measure makes (a)-(c) true" (the measure is
  orthogonal to (c)); "the genuine ends are spacelike-gapped" (timelike-dominant
  flats cross, generically); "θ=0 from structure / the pencil closes" (needs an
  unowned excision import); and the loose "O(3,1) boost directions are the ends"
  (boosts are isometries; the ends are the diagonal flats).

## 7. Boundary

Exploration tier. Only this artifact and its probe
(`tests/channel-swings/oracle_relative_prong0_measure_lemma_probe.py`, foreground,
deterministic two-run-identical, **EXIT 0**) were written. GU otherwise read-only.
No commit, no push. No edit to LANE-STATE, research-portfolio, NEXT-STEPS, the
prereg, the decision tree, the Q1a win or its HV, the sector-relative theory, any
other agent's artifact, or any claim/canon/verdict/ledger file. No claim status,
canon verdict, paper status, or public posture changes; the externality of σ/τ is
untouched. Kill conditions were declared in the probe before GU's case was run
(A0 controls, C0 boost-isometry control, N2 measure-invariance). The verdict is
`P0-FAILS-OBSTRUCTED`: the measure-lemma fails at clause (c), the pencil theorem
does not close from committed structure, and the failure is the sharper
"operator-ill-posed-at-the-genuine-ends" obstruction, with the exact external
datum (the `q<0`-stratum prescription / N2 operator lift) named once.
