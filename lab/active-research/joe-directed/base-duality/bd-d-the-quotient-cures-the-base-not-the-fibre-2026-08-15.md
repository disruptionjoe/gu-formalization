---
artifact_type: exploration
status: exploration
doc_type: reduction-result-and-no-go
created: 2026-08-15
work_item: BD-D
channel: base_duality
route: REDUCE__COMPUTE_THE_DESCENDED_PAIRING_ON_THE_PHYSICAL_QUOTIENT
base_revision: 7db85977
ledger_base: lab/process/conditional-physics-ledger-v0.258.json
ledger_edit: none -- versionless delta, for the canonical owner to disposition
target_claim: "BD-D-2026-08-15-WRONG-STAGE -- the brief's constraint-solver
  hypothesis, in its own words: `positivity is being demanded at the wrong
  stage ... the object that actually governs stability is the reduced pairing
  Z^T H Z on the constraint null space ... and its signature is not determined
  by the ambient signature`; together with the restriction BD-A section 9 H5
  conceded verbatim, `Your positivity theorem assumes the physical quotient is
  ker(c) (x) ad ... a genuine BV physical quotient with ghosts, or a non-split
  subspace -- is not covered`; and the positivity subclause of LA-11's proposed
  `LT-GR6b` revival_trigger, `positive on the physical quotient`. All three are
  INTERNAL CHANNEL claims about repository objects and about a method
  hypothesis. NO GU source claim is targeted, attacked or defended."
target_claim_verdict: "SPLIT VERDICT, AND THE SPLIT IS THE RESULT -- the
  wrong-stage hypothesis is CONFIRMED for the BASE factor and REFUTED for the
  FIBRE factor, exactly. Confirmed: BD-A's ambient negative part `3 n_kappa +
  p_kappa` is a wrong-stage artifact; on the free linearised Yang--Mills symbol
  quotient the negative part is `2 n_kappa`, so the whole `p_kappa` term -- the
  entire contribution of the Lorentzian base -- is removed, and what the
  quotient removes is a NEUTRAL `(91,91)` pair. Refuted: `2 n_kappa` vanishes
  iff `n_kappa = 0`, so the reduced form is definite iff the fibre form is,
  and BD-A's joint-unsatisfiability verdict survives the reduction verbatim. A
  NO-GO is added that BD-A did not have: because every gauge-equivariant
  subquotient of `Lambda^1 (x) ad` is `U (x) ad`, and a tensor product is
  definite iff both factors are, NO equivariant reduction whatsoever can remove
  an indefinite fibre form. BD-A H5's conceded restriction is therefore
  narrowed for the bare module. The `LT-GR6b` positivity subclause is priced
  only conditionally: for this comparator quotient it is one condition on one
  factor, `n_kappa = 0` at a named subscript. GU has no derived Gauss law,
  interacting BRST/BV complex or physical quotient to which that condition can
  yet be transported."
canon_verdict_change: none
priority_change: none
steering_effect: unchanged
canonical_effect: pending_integration
title: "BD-D: the free Yang--Mills symbol quotient cures the BASE and cannot touch the FIBRE.
  The comparator symbol cohomology of `Lambda^1 (x) ad P` on `X^4` is the
  null screen `(k^perp/<k>) (x) ad`, dimension `2 dim g` = 182, and its
  descended pairing has exact inertia `(98,84)` at the source trace form and
  `(182,0)` at a compact one -- so the reduction removes the base half of BD-A's
  obstruction entirely and leaves the fibre half untouched. A NO-GO follows:
  every gauge-equivariant subquotient is `U (x) ad`, a tensor product is
  definite iff both factors are, hence no equivariant subquotient of this bare
  module can rescue definiteness from an indefinite fibre form. The calculation
  does not decide positivity of GU's unconstructed physical quotient; it shows
  that a Cartan involution gives a positive Krein majorant on this comparator
  quotient and that its price there falls from two involutions to one."
rows_touched_structurally: [RA-A4, RA-A5, RA-B6, RA-D4, RA-E4, RA-E6, RA-G1, RA-G4, LT-SM4, LT-SM6]
rows_advanced: 0
rows_proposed: []
free_object_delta: 0
free_object_delta_note: "No GU-owned object is removed. In the imported free
  Yang--Mills symbol complex, the null screen makes a separate base Cartan
  involution unnecessary and leaves one fibre involution. That is a conditional
  comparator price, not a construction of GU's Gauss law, interacting BRST/BV
  complex, physical quotient or maximal-compact selector."
grade: "EXACT integer / fractions.Fraction arithmetic. so(p,q) matrix bases
  built in-file and Jacobi-verified; the Cartan involution built as `-X^T` and
  verified entrywise, for closure, for `theta^2 = 1` and for the automorphism
  identity; every inertia by exact rational symmetric congruence on an
  explicitly assembled Gram matrix, never by eigenvalue and never by the tensor
  signature law (which is separately certified against direct congruence on 225
  cases); the 364-, 273- and 182-dimensional Grams all diagonalized directly;
  ranks and nullspaces over Q by fraction-free elimination; `dim End_g(g)`
  computed as an exact commutant nullspace; no numpy, no float constructed
  anywhere; `assert_no_float` sweeps the whole result dict. 95/95 checks, exit
  0, via tests/channel-swings/joe_directed_bdd_the_quotient_cures_the_base_not_the_fibre.py
  run from the repository root under `_local/cas-venv`. Certificate splits as 61
  [E] exact results, 16 [C] controls that must fire, and 18 [R] reproductions of
  BD-A / BD-B / VG-V2 / K77 facts, all reproduced BEFORE being used. CONTRARY
  CONTROLS included and firing in BOTH directions: a KKT system whose reduced
  Hessian IS positive definite (so the machinery detects genuine cures), a KKT
  system whose reduced Hessian is still indefinite, the GU case itself where the
  reduction provably fails to cure, a spacelike slice that stays indefinite at a
  compact fibre form, a `(7,7)` base where the screen quotient is neutral for
  ANY fibre form, and a NON-equivariant subspace that IS definite at the source
  group -- so the equivariance hypothesis is shown load-bearing rather than
  assumed. FAILURE PATH EXERCISED: sixteen planted false facts (reduced_sig,
  reduced_dim, compact_cure, descent, radical, tensor, hamiltonian, krein,
  ambient_one, nonequi, endg, hessian, spacelike, screen_rule, neutral,
  artifact_drift) each drive exit 1 through `--selftest`. NOT: a ledger edit, a
  verdict change, a physics derivation, a coefficient, a selection principle, a
  claim that GU's action is owned, a claim that GU has a Gauss law, a claim that
  the interacting BRST charge exists, or any domain, boundedness, Fredholm or
  Hilbert-space statement."
disposition: FREE_LINEARIZED_YANG_MILLS_SYMBOL_QUOTIENT_CONSTRUCTED__NOT_GU_PHYSICAL_QUOTIENT__NULL_SCREEN_TIMES_ad_DIM_2_dim_g_EQUALS_182__DESCENDED_INERTIA_98_84_AT_THE_SOURCE_TRACE_FORM_AND_182_0_AT_A_COMPACT_ONE__COMPARATOR_REMOVES_A_NEUTRAL_91_91_PAIR__EQUIVARIANT_SUBQUOTIENT_THEOREM_PRESERVES_AN_INDEFINITE_FIBRE_FORM_ON_THE_BARE_MODULE__NO_CLAIM_FOR_ENLARGED_GHOST_BV_COMPLEXES_OR_INTERACTING_DYNAMICS__OBSERVED_SECTOR_POSITIVITY_SOURCE_OPEN__ONE_INVOLUTION_KREIN_MAJORANT_ON_THIS_COMPARATOR__ZERO_GU_OBJECTS_REMOVED__ZERO_ROWS_ADVANCE
depends_on:
  - lab/active-research/joe-directed/base-duality/bd-a-the-base-duality-is-the-observation-and-positivity-is-the-obstruction-2026-08-15.md
  - lab/active-research/joe-directed/base-duality/bd-b-obstruction-is-fibre-independent-and-evades-only-at-translation-depth-one-2026-08-15.md
  - lab/active-research/joe-directed/base-duality/bd-c-met-x-is-an-argument-not-a-background-2026-08-15.md
  - lab/active-research/joe-directed/ownership-theorem/ot1-the-ownership-predicate-and-the-pairing-obstruction-2026-08-15.md
  - lab/active-research/joe-directed/ledger-advancement/la11-b9stat-is-a-base-duality-row-and-four-rows-name-it-as-a-subclause-2026-08-15.md
  - lab/methods/source-native-comparator-routing.md
  - explorations/positivity-exit-criteria-design-packet-2026-08-11.md
  - explorations/rb1-source-repo-current-musical-2026-07-30.md
  - explorations/big-swing-2026-07-06/VG-V2-fourth-seat-gauge-sector.md
  - explorations/big-swing-2026-07-03/AUDIT-noncompact-compact-reduction-EXTERNAL.md
  - explorations/conditional-build/selected-k77-total-upsilon-null-screen-2026-08-07.md
  - explorations/conditional-build/k77-global-even-bv-null-green-domain-2026-08-05.md
  - explorations/observable-algebra-commutant-trichotomy-2026-08-03.md
  - explorations/W173-brst-cohomology-mirror-sector-2026-07-14.md
  - explorations/no-selector-for-the-base-sign-2026-08-08.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/channel-swings/joe_directed_bdd_the_quotient_cures_the_base_not_the_fibre.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`

> [!CAUTION]
> **CORRECTION IV-20260815 — source semantics and quotient scope.** The original
> version repeatedly shortened the object below to “the physical quotient” and
> treated BD-C as proving that the source disavows physical positivity. Both
> readings are withdrawn. The 182-dimensional object is the ghost-number-zero
> **symbol cohomology of an imported free, linearised Yang--Mills complex**. GU
> has no derived Gauss law, interacting BRST/BV complex, analytic domain or
> physical quotient here. Separately, the source affirms an indefinite ambient
> Killing form but leaves observed-sector positivity open/unsupplied. The exact
> inertias and the bare-module equivariant-subquotient theorem survive with
> those scopes.

**Why that classification, and why it is not `SOURCE_NATIVE_ROUTE` as BD-A and
BD-B declared.** The *module* is source-native: `Λ¹ ⊗ ad P` over the observed
`X⁴`, the source's `𝒢 = Γ(Ad P)`, the source's `𝒲 = 𝒢 ⋉ Ω¹(ad P)`, the
chimeric frame algebra of the source's own signature chain. But to *construct*
the comparator quotient this artifact imports something the source does not own: a
**Yang–Mills constraint symbol**, from which the Gauss law and the
characteristic variety follow. GU's action is the open object; a Gauss law is
not a source datum, and no artifact in this repository has derived one. That
import is a conventional comparator, so this file sits on the boundary and
declares it.

The routing method's bridge burden item 4 — *"the quotient, boundary and
analytic domain if physical modes are claimed"* — is exactly what is at stake,
and it is **not discharged for GU**. Section 6 survives as a theorem about
equivariant subquotients of the bare module: the comparator import fixes the
dimension `(182)` and base inertia `(2,0)`, while the theorem fixes what such a
bare-module subquotient can do to an indefinite fibre form. It does not cover
an enlarged ghost/antifield complex, an interacting differential, a non-split
derived quotient or an analytic physical domain.

---

# BD-D — the free Yang--Mills symbol quotient cures the base and cannot touch the fibre

## Verdict first, unsoftened

**The hypothesis is half right, and the half that is right does not help.**

The brief's constraint-solver lens says positivity is being demanded at the
wrong stage, and that the reduced object on the constraint null space may be
definite where the ambient is not. I computed the reduced object. Three
results, in decreasing order of how much they move.

**1. The base half of BD-A's obstruction is a wrong-stage artifact in the free
Yang--Mills symbol comparator, exactly.** BD-A's ambient negative part is
`3 n_κ + p_κ`. On `P_k^{YM,sym}`, the symbol cohomology defined in §2, it is
`2 n_κ`. The entire `p_κ` term — the whole contribution
of the Lorentzian base signature, the thing that made BD-A's theorem hold *for
any nonzero fibre form* — is **gone**. And what the quotient removes is not
some arbitrary block: it is a **neutral `(91, 91)` pair**, the same neutral pair
for every fibre form, because the removed base directions span a hyperbolic
plane. That is the Gupta–Bleuler quartet mechanism, and it is the exact reason
the hypothesis was worth testing.

**2. The fibre half is untouched, and no bare-module equivariant subquotient can
touch it.** `2 n_κ`
vanishes iff `n_κ = 0`. So BD-A's headline — equivariance at the source group
and positivity are jointly unsatisfiable — **survives the reduction verbatim**,
with the arithmetic changed and the verdict unchanged. And it survives for a
structural reason BD-A did not have: because `ad` is absolutely irreducible,
every `Γ(Ad P)`-equivariant subquotient of `Λ¹ ⊗ ad P` is `U ⊗ ad` for a
subquotient `U ⊆ Λ¹`, so the descended form is always `(N|_U) ⊗ κ`, and a
tensor product of nonzero symmetric forms is definite **iff both factors are**.
**No equivariant subquotient of the bare module can remove an indefinite fibre
form.** This closes the escape within that category. It does not classify an
enlarged ghost/antifield complex, a non-split derived cohomology, or interacting
dynamics.

**3. This comparator admits a one-involution Krein majorant; GU's physical
positivity remains open.** On `P_k^{YM,sym}` the Krein condition is satisfied
with a certificate: `J = 1_screen ⊗ θ`, `J² = 1`, `−B(·, J·)` of inertia `(182, 0)`.
That is *one* Cartan involution. On the ambient the same certificate needs
*two*, `(364, 0)` at `P_base ⊗ θ`, and the fibre involution alone leaves the
ambient indefinite. **So the comparator quotient's contribution is not a GU
positivity result — it is that it halves the involution count in this model.**
The mechanism itself is
`GEOMETER-VS-PHYSICS-OBJECTS.md`'s settled KEEP-AND-GRADE row and BD-A's own
Lens Q2, and **no novelty is claimed for it**.

| the trigger's clause, after BD-A and after BD-D | BD-A's verdict | BD-D's verdict |
|---|---|---|
| a source-owned base duality on `X⁴` | SUPPLIED (`ℷ`) | unchanged |
| ... **global** | line field, `chi(X^4) = 0` for closed `X⁴` | unchanged — still needed, to have a Lorentzian base at all |
| composed with an `Ad`-invariant fibre form | SUPPLIED (trace form) | unchanged |
| into a `Γ(Ad P)`-equivariant pairing on `Λ¹ ⊗ ad P` | CONSTRUCTED, inertia `(189,175)` | unchanged |
| ... **positive on the physical quotient** | BLOCKED; needs **two** Cartan involutions | **CONDITIONAL COMPARATOR PRICE:** on `P_k^{YM,sym}` definiteness is `n_κ = 0`; the base involution is not needed. Transport to GU's physical quotient is unproved. |
| — | — | **Krein-majorant certificate on the comparator only:** `−B(·,J·) = (182,0)` |

---

## 0. PREFLIGHT — six specialist lenses, run inline

Standing rule: N lenses means N sections written here, never N subagents.

### Lens P1 — target triage: is this still the right target after BD-A, BD-B and BD-C?

**Yes, and the target moved twice in one day, which is the thing to notice.**

- **BD-A** proved the ambient no-go and then, in §9 **H5**, conceded the exact
  restriction that defines this route, verbatim: *"Your positivity theorem
  assumes the physical quotient is `ker(c) ⊗ ad`. Conceded as a restriction. I
  computed the trichotomy for a **codimension-1** quotient by a covector. A
  quotient that is not of that form — a genuine BV physical quotient with
  ghosts, or a non-split subspace — is not covered."* A conceded restriction in
  the strongest artifact of the wave is the highest-value target available; it
  is the one place where the wave's own author said the result might not hold.
- **BD-B** proved the fibre subscript **inert** for the rank bound and reduced
  the whole verdict to one integer, the translation depth. That is a *rank
  increase* for this route, because it predicts — before any computation — that
  a base-side reduction will not move the fibre-side answer. BD-D's §6 is that
  prediction made exact for *inertia* rather than for *rank*, and BD-B is
  credited for the mechanism, not re-derived.
- **BD-C**, as corrected by `CORRECTION IV-20260815`, establishes ambient
  Killing-form indefiniteness and maximal-compact experimental shielding. It
  does **not** establish that the source disavows positivity on an observed
  physical quotient. The latter remains source-open/unsupplied. BD-D therefore
  prices a comparator realization of that demand; it does not replace or close
  the GU physicalization debt.
- **What moved in the ranking, stated plainly.** Before today: "build the base
  duality." After BD-A: "decide the composite." After BD-A's H5: **"price the
  demand on a named reduced object, while preserving the missing bridge to
  GU."** The ambient sweep is finished; the free Yang--Mills symbol quotient
  was one controlled place the answer could differ. It removes the base
  contribution but does not supply GU's quotient.

### Lens P2 — constrained optimization / KKT and reduced Hessians: what does the analogy actually import?

The lens the brief supplies, taken seriously and then tested rather than
assumed. In a KKT/saddle-point system

```text
  [ H   A^T ] [ x ]     the ambient block is indefinite BY CONSTRUCTION,
  [ A   0   ] [ y ]     and stability is governed by  Z^T H Z,  Z = null(A).
```

The analogy imports two things. **The first is correct and is why this route
exists:** the ambient signature genuinely does not determine the reduced
signature, and a repository that swept only the ambient has not answered the
question. **The second is a type error, and finding it is part of this route's
output.** In a *gauge field theory* the constraint null space **is** the
Hessian kernel at the characteristic covectors — that is what gauge invariance
*means* at the symbol level — so `Z^T H Z ≡ 0` identically on the physical
quotient (`[E]`, §8). The KKT object the brief names is **vacuous here**. What
survives is the *other* matrix: `Z^T B Z`, the descended **pairing**, which is
the state-space metric, not a Hessian. **That relabelling is not pedantry: it
is what makes the answer a Krein question rather than a stability question,**
and it is the bridge from the brief's lens to this repository's settled
vocabulary.

**Prediction written before computing:** the base factor will improve and the
fibre factor will not, because nothing in a gauge quotient acts on `ad`. Both
halves confirmed.

### Lens P3 — Krein and indefinite-inner-product spaces: what is the right question?

A Krein space is a pair `(K, B)` with `B` nondegenerate and indefinite,
equipped with a **fundamental symmetry** `J`: `J² = 1`, `J` is `B`-selfadjoint,
and `B_J(x,y) := B(x, Jy)` (up to sign) is definite. Positivity of `B` is a
*special case* — `J = 1`. So "is `B` positive?" and "does `B` admit a `J`?" are
different questions, and this program has already settled that GU's answer
lives on the second (`GEOMETER-VS-PHYSICS-OBJECTS.md`, ghost-clearance row:
*"KEEP-AND-GRADE the ghost via the Krein form `[P,S]=0` ... an indefinite-metric
(PT/Krein) consistency, NOT a positive Hilbert space"*).

The lens's instruction to the computation: **do not report only the inertia of
`B̄`. Report the inertia of `B̄_J` as well, and report how many involutions `J`
costs on each space.** §9 does. The lower involution count improves this
comparator construction; it is not a GU advance without the missing bridge.

The lens also fences: `F = ∅` on the 1664-dimensional kinematic carrier
(`observable-algebra-commutant-trichotomy-2026-08-03.md`) is a statement about
a **different object**, and this artifact's `J` on a 182-dimensional adjoint
quotient neither contradicts it nor is licensed by it. The repository keeps
those apart deliberately; so does this file.

### Lens P4 — BRST/BV cohomology and gauge fixing: what comparator is computed here?

For a gauge one-form the physical sector is `H⁰` of the BRST complex at ghost
number zero, which at the linearised/symbol level is

```text
   H^0(k)  =  ker(symbol of the field equation)  /  im(symbol of d_A)
           =  ker H(k) / <k>            tensored with  ad.
```

That is the **free Yang--Mills symbol object**. Its dimension is `0` off the
light cone and `2 dim 𝔤` on it, which is the standard two-polarization count.
It is not a derivation of GU's physical sector. The lens's warnings, all
respected below:

1. **The interacting BRST charge does not exist in this repository.** Register
   row `M-H17` step (i) records it as unbuilt, and `W173` has only the free
   bicomplex. Everything here is at the **free/linearised** level, and the
   artifact says so wherever it matters.
2. **`H⁰` for `Ω¹(ad P)` has never been computed here.** `M-H17` steps
   (iii)–(iv) record exactly that, and the positivity-exit design packet's
   criterion **PC-3** — *"inertia of the descended form on gh-0 cohomology"* —
   is specified there and **never run**. This artifact runs PC-3 for one
   sector. It does not run it for the sector `M-H17` actually tracks, which is
   the RS/`ker Γ` carrier.
3. **The descended form must be checked to descend.** It is not automatic. §2
   checks it and the control fires where it fails.

### Lens P5 — symplectic reduction: is the "quotient" the right kind of object?

Marsden–Weinstein: `J^{-1}(0)/G`, constraint surface modulo gauge, with the
form descending iff the gauge directions lie in the kernel of the restricted
form. The lens supplies the exact well-definedness condition used in §2 and one
correction to how the brief framed the target:

> A gauge quotient **alone** does not carry a form. `⟨k⟩ ⊗ ad` is not in the
> radical of `B` on all of `Λ¹ ⊗ ad`, so `(Λ¹/⟨k⟩) ⊗ ad` has no descended
> pairing at all. The constraint is not an optional extra that improves the
> answer — **without it there is no answer.** (`[C]`, fires.)

And it supplies the second, independent construction: the **Hamiltonian/ADM**
route, timelike foliation plus Coulomb transverse plane, which is a genuinely
different reduction (it needs a chosen timelike `n`; the covariant route does
not). §4 runs it and it agrees exactly. Two reductions agreeing is the only
real defense against the hostile charge in §10.

### Lens P6 — grep-before-novelty: what already exists, credited and not re-claimed

The brief records eight false novelty claims in this channel. A concept-level
sweep was run before a line of the construction, across `explorations/`,
`lab/`, `canon/`, `papers/`, `tests/`, `NEXT-STEPS.md`,
`DERIVATION-PROGRESS.md`, `RESEARCH-STATUS.md` and `CURRENT-STATE.yaml`. It
found prior art for **most** of what this artifact uses. Nothing below is
claimed as new.

| object | owner, date | relation to BD-D |
|---|---|---|
| *"Positivity is neither used nor available"* on the identical musical map | `RB1` §5, 2026-07-30 | **the source-side answer to the brief's question, sixteen days before the row that demanded positivity.** BD-D only computes the number that makes it exact |
| ghost clearance is **KEEP-AND-GRADE** via a Krein form `[P,S]=0`, `P` a Cartan involution, *"NOT a positive Hilbert space"* | `GEOMETER-VS-PHYSICS-OBJECTS.md` | **this is the mechanism.** BD-D claims no novelty for it; §9 only computes its certificate on the quotient |
| *"the row should demand a Krein structure, not positivity ... a nondegenerate pairing plus a fundamental symmetry `J` with `J² = 1` and `B(·,J·)` definite"* | **BD-A Lens Q2**, 2026-08-15, hours earlier | **BD-A already reached the conclusion.** BD-D supplies the exact `(182,0)` certificate and the involution count; the conclusion is BD-A's |
| `B_θ(X,Y) = −B(X, θY)` positive definite, min eigenvalue `+24`; *"ghost parity IS the restricted Cartan involution"* | `VG-V2` (`big-swing-2026-07-06`), 2026-07-06 | the fibre half of `J`, machine-checked with eight firing controls. Reproduced here exactly, over `ℚ`, not re-derived |
| positivity forces compactness; the Cartan involution is `REDUCTION_EXTERNAL` | `W208`, `W219`, `AUDIT-noncompact-compact-reduction-EXTERNAL` | the price of `n_κ = 0`. Already on the books; BD-D does not re-price it |
| the fibre subscript is **inert**; the verdict is a function of one integer | **BD-B**, 2026-08-15 | the same mechanism, for **rank**. §6 is the **inertia** analogue and credits BD-B for the shape of the argument |
| ambient inertias `(49,42)`, `(24,21)`, `(189,175)`, `(273,91)`, `(93,87)`, `(135,45)`; the tensor signature law; the timelike/spacelike/null trichotomy; the pencil facts | **BD-A**, 2026-08-15 | all reproduced `[R]` before use. **Not one number of BD-A's is moved** |
| Killing signature of `so(9,5)` = `(45,46)` | `VG-V2`; reproduced at `BD-B` | reproduced `[R]` |
| an **ambient K77 null screen** of rank 12 and signature **`(6,6)`**, explicitly fenced from *"the separately constructed four-dimensional `10 -> 6 -> 2` physical null quotient"* | `selected-k77-total-upsilon-null-screen-2026-08-07` | **this is the null-screen construction, on `Y¹⁴`.** BD-D reproduces its `(6,6)` as `[R]` from its own base-screen rule, and §3b uses it for the contrary result that the base cure is Lorentzian-specific |
| the exact null dimension filtration **`10 -> 6 -> 2`** with *"explicit plus/cross physical representatives after harmonic constraint and residual gauge"* | `k77-global-even-bv-null-green-domain-2026-08-05` | **the constraint/gauge null quotient mechanism is theirs, in the metric sector.** Its own L7 line records *"no ... positivity ... claim"* and its held-open list still names *"a physical positive cohomology"*, so the **signature** was never computed — there or anywhere |
| the `(d−2)·dim S` physical-mode count | `oq-rk1-rs-rank-first-principles-2026-06-23` (Rarita–Schwinger) | the counting mechanism is theirs. BD-D applies it to a gauge one-form, where it gives `2 dim 𝔤` |
| Gupta–Bleuler as the **normality precedent** for `F = ∅` on a covariant carrier | `observable-algebra-commutant-trichotomy-2026-08-03`, and five other files | the *reading* is theirs and it is exactly right; BD-D supplies the computation it predicted |
| criterion **PC-3**, *"inertia of the descended form on gh-0 cohomology is `(n₊,0,0)`"*, and a checker spec returning *"the descended Gram on H⁰, and its inertia"* | `positivity-exit-criteria-design-packet-2026-08-11` | **BD-D executes PC-3** for the ordinary-gauge `Ω¹(ad P)` sector. The packet is the specification; this is one instance of it, not the packet's own target sector |
| `M-H17` steps (iii)–(iv): *"`H⁰(Q)` genuinely computed (W207 does not)"*, *"nondegenerate descended pairing"* | `improvement-register-2026-08-03:350` | the gap this artifact fills for one sector, and does not fill for the RS/`ker Γ` sector the row tracks |
| no convention-independent structure selects the base sign | `no-selector-for-the-base-sign-2026-08-08` | why every statement here is about **definiteness**, never about which block is *positive* |

**The narrow novelty claim, and it is all of it:** (i) the exact inertia of the
**descended** pairing on the free Yang--Mills symbol quotient — `(98,84)` at
the source trace form, `(182,0)` at a compact one, `(90,92)` at `so(9,5)`,
`(48,42)`/`(90,0)` at `so(6,4)` — a number that exists nowhere in this
repository for any sector; (ii) that the removed complement is a **neutral
`(91,91)` pair**, the same for every fibre form; (iii) the **no-go**: every
gauge-equivariant subquotient is `U ⊗ ad`, hence no equivariant reduction can
cure an indefinite fibre form, with `so(3,1)` computed as the exact case where
the universality hypothesis fails; (iv) that the base cure is
**Lorentzian-specific** and fails on a `(7,7)` base for **any** fibre form;
(v) that the Krein price falls from two involutions to one on the quotient.
Nothing else.

---

## 1. THE COMPUTATION — 95/95, exit 0, zero floats, failure path exercised

`tests/channel-swings/joe_directed_bdd_the_quotient_cures_the_base_not_the_fibre.py`,
from the repository root under `_local/cas-venv`.

```text
CERTIFICATE: 95/95 checks pass; no load-bearing float (swept).
split  [C] 16  [E] 61  [R] 18
```

Prior results are reproduced **before** being used (`[R]`), from matrices built
in-file, nothing quoted:

```text
BD-A   so(7,7) trace form (49,42);  so(6,4) (24,21)
BD-B   so(9,5) trace form (45,46);  dim so(7,7) = dim so(9,5) = 91, so(6,4) = 45
BD-A   ambient 364 composite (189, 175) and (273, 91) by DIRECT congruence
BD-A   ambient 180 at so(6,4): (93, 87) and (135, 45)
BD-A   ker(c) (x) ad: DEFINITE / INDEFINITE / DEGENERATE for timelike /
       spacelike / null c
BD-A   the tensor signature law, agreeing with direct congruence on 225 cases
BD-A   pencil: definite B forces a real 2x2 spectrum on 729 exact cases;
       indefinite B admits lambda^2 + 1
VG-V2  kappa_theta = -kappa(., theta .) is positive definite: (91,0), (45,0)
K77    a null screen in a (7,7) base has rank 12 and inertia (6,6)
```

**Failure path**, sixteen planted mutations, each must drive exit 1:

```text
_local/cas-venv/bin/python tests/channel-swings/joe_directed_bdd_the_quotient_cures_the_base_not_the_fibre.py --selftest

  mutation reduced_sig      exit 1  OK   (the reduced 182 form is (99,83))
  mutation reduced_dim      exit 1  OK   (the physical quotient has dim 273)
  mutation compact_cure     exit 1  OK   (a compact fibre form leaves it indefinite)
  mutation descent          exit 1  OK   (the pairing descends for timelike k too)
  mutation radical          exit 1  OK   (the radical is not the gauge line)
  mutation tensor           exit 1  OK   (some A(x)B is definite with an indefinite factor)
  mutation hamiltonian      exit 1  OK   (the Hamiltonian route disagrees)
  mutation krein            exit 1  OK   (the Krein form on the quotient is indefinite)
  mutation ambient_one      exit 1  OK   (the fibre involution alone definitises the ambient)
  mutation nonequi          exit 1  OK   (the non-equivariant subspace is indefinite too)
  mutation endg             exit 1  OK   (so(3,1) has dim End_g(g) = 1)
  mutation hessian          exit 1  OK   (Z^T H Z is nonzero on the physical quotient)
  mutation spacelike        exit 1  OK   (the spacelike slice is definite at a compact form)
  mutation screen_rule      exit 1  OK   (a (7,7) null screen is definite)
  mutation neutral          exit 1  OK   (the removed pair is not neutral)
  mutation artifact_drift   exit 1  OK   (a headline number vanished from this file)

FAILURE-PATH SELFTEST: PASS (16/16 mutations drove exit 1)
```

**Two honest limits on the failure path, inherited from BD-A and restated
rather than left to be found.** (i) The mechanism is an environment variable
selecting planted assertions inside the same file, each run as a fresh
subprocess — the effect is a mutated copy, but it is not literally a separate
file. (ii) Every mutation asserts the exact **negation** of a headline fact
against the value the unmutated run actually computed, so a firing mutation
certifies the computed value; but **sixteen mutations cover sixteen headline
facts, not all 95 checks.** The 2304-case tensor sweep, the 225-case law
certification, the `dim End_𝔤(𝔤)` commutant solves and the lift-independence
family are covered only by their own internal controls.

---

## 2. THE FREE YANG--MILLS SYMBOL QUOTIENT, NAMED PRECISELY, AND ITS DIMENSION

> **Definition (BD-D).** Fix `x ∈ X⁴`, a nonzero covector `k ∈ T*_xX⁴`, and the
> free gauge symbol
>
> ```text
>   H(k)  =  <k,k>_N * N  -  (Nk)(Nk)^T          on Lambda^1,
> ```
>
> the quadratic form of `|k ∧ a|²`. Define the comparator symbol cohomology
>
> ```text
>   P_k^{YM,sym}  =  ( ker H(k) / im(symbol of d_A) )  (x)  ad P_x
>                 =  ( k^perp / <k> )  (x)  ad P_x   [ only when <k,k> = 0 ]
> ```
>
> i.e. the ghost-number-zero symbol cohomology of the **imported free,
> linearised Yang--Mills complex** at `k`, tensored with the adjoint. It is not
> GU's derived physical quotient.

Everything in that definition is computed, not asserted:

```text
                       dim ker H(k)    im(d_A)    gh-0 quotient
  k timelike                1             1             0
  k spacelike               1             1             0
  k null                    3             1             2
```

and the gauge direction lies in `ker H(k)` for **every** `k` (`[E]`, with a
control: a non-gauge-invariant symbol does not annihilate `⟨k⟩`). So:

> **`P_k^{YM,sym}` is nonzero only on the light cone**, where it is the
> **null screen** `k^⊥/⟨k⟩` tensored with `ad`. Its dimension is
>
> ```text
>   2 dim 𝔤  =  182   at dim 𝔤 = 91 (so(7,7), so(9,5))
>   2 dim 𝔤  =   90   at dim 𝔤 = 45 (so(6,4))
> ```
>
> against `364` and `180` ambient, and `273`/`135` on the constraint surface.
> `182 < 273 < 364` (`[E]`).

**Descent is not automatic and is checked.** The form `B` descends to `P_k` iff
the gauge subspace is `B`-orthogonal to the constraint surface. Computed:

```text
  k null      <k,k> = 0  and  k in k^perp   ->  DESCENDS
  k timelike  <k,k> = -1                    ->  DOES NOT DESCEND   [C] fires
  gauge quotient with NO constraint          ->  DOES NOT DESCEND   [C] fires
```

and the radical of `B` restricted to the constraint surface `k^⊥ ⊗ ad` is
**exactly** the gauge subspace, of dimension exactly `dim 𝔤 = 91` (`[E]`). That
is the well-definedness certificate: the quotient removes the radical and
nothing else.

```text
  k^perp (x) ad   at the source trace form   :   (98, 84, 91)      dim 273
                             nullity  91  =  dim g  =  the gauge orbit
```

**This is one comparator realization of the object `LT-GR6b`'s trigger names;
it is not the source-derived object.** BD-A
computed `ker(c) ⊗ ad` at dimension `273` — the *constraint surface*, or
equivalently a codimension-1 gauge slice — and said so in H5. `P_k` is one
further quotient down.

---

## 3. THE REDUCED SIGNATURE — exact, by rational congruence

Direct symmetric congruence on the explicitly assembled `182 × 182` descended
Gram `Zᵀ B Z`, where `Z` is an explicit lift of `k^⊥/⟨k⟩` tensored with the
identity on `ad`. **Never** the tensor signature law, which is certified
separately against direct congruence on 225 cases.

```text
fibre algebra        dim g   kappa       AMBIENT (4 dim g)   REDUCED (2 dim g)
so(7,7)  trace         91   (49, 42)     364  (189, 175)     182  ( 98,  84)
so(7,7)  K-reduced     91   (91,  0)     364  (273,  91)     182  (182,   0)
so(9,5)  trace         91   (45, 46)     364  (181, 183)     182  ( 90,  92)
so(9,5)  K-reduced     91   (91,  0)          --             182  (182,   0)
so(6,4)  trace         45   (24, 21)     180  ( 93,  87)      90  ( 48,  42)
so(6,4)  K-reduced     45   (45,  0)     180  (135,  45)      90  ( 90,   0)
```

Every reduced form has **zero nullity** (`[E]`): descent killed exactly the
radical.

**The arithmetic, which is the whole result.**

```text
  AMBIENT   negative part  =  3 n_kappa + p_kappa        (BD-A)
  REDUCED   negative part  =  2 n_kappa                  (BD-D)
```

Swept over all 35 nonzero fibre inertias with each part at most 5 (`[E]`):
the ambient negative part is **never** zero; the reduced negative part is zero
**iff** `n_κ = 0`. The difference `3n + p − 2n = n + p = dim 𝔤` is exact and
identical in every case.

### 3.1 What the quotient removes is a NEUTRAL pair

The complement of the screen in `Λ¹` is spanned by `k` and a second null
covector `m` with `⟨k,m⟩ ≠ 0` — a **hyperbolic plane**, inertia `(1,1)`, and
`B`-orthogonal to the screen (`[E]`). Therefore:

```text
  removed = span(k,m) (x) ad  :  (91, 91)   at the SOURCE trace form
                                 (91, 91)   at a COMPACT form
  ambient = reduced (+) removed, exactly:
      (189,175) = ( 98, 84) + (91,91)
      (273, 91) = (182,  0) + (91,91)
```

The removed block is neutral **for every fibre form**, because `(1,1) ⊗ κ` has
inertia `(p_κ + n_κ, n_κ + p_κ) = (dim 𝔤, dim 𝔤)` whatever `κ` is. **That is
why the base contribution cancels: the timelike and longitudinal directions
form a null pair and drop out together.** It is the Gupta–Bleuler quartet, and
this repository has been carrying the *reading* since 2026-08-03
(`observable-algebra-commutant-trichotomy`, *"the normal covariant
indefinite-metric situation ... yet unitary on the physical quotient"*) without
the number.

### 3.2 The reduction is well-posed: lift- and covector-independence

A quotient's signature must not depend on how it is lifted. Certified (`[E]`):

```text
  three different complements of <k> inside k^perp   ->  (98, 84) each
  three further null covectors, incl. (3,4,0,5)      ->  dim 2 and (98, 84) each
```

### 3.3 The base cure is LORENTZIAN-SPECIFIC — and fails on `Y¹⁴`

The screen construction obeys an exact rule, computed for six signatures
(`[E]`):

```text
  base inertia (p,q)   ->   null screen inertia (p-1, q-1),   dim p+q-2

  (3,1) -> (2,0)   DEFINITE        (1,3) -> (0,2)   DEFINITE
  (5,1) -> (4,0)   DEFINITE        (6,4) -> (5,3)   INDEFINITE
  (9,5) -> (8,4)   INDEFINITE      (7,7) -> (6,6)   INDEFINITE  [R: K77 2026-08-07]
```

So **the screen is definite iff the base signature is Lorentzian**, i.e. iff
`min(p,q) = 1`. The `(7,7)` row reproduces
`selected-k77-total-upsilon-null-screen-2026-08-07`'s rank-12 `(6,6)` ambient
screen exactly.

**Consequence, and it is a contrary result in the base direction (`[C]`
fires).** On a `(7,7)` base — the K77 chimeric ambient — the screen quotient is
`(6,6) ⊗ κ`, of inertia

```text
  (6 p_kappa + 6 n_kappa,  6 n_kappa + 6 p_kappa)  =  (546, 546)   NEUTRAL,
```

for **any** `κ`, including a compact one. **On `Y¹⁴` no fibre involution can
help; the base half alone is fatal.** The base cure this artifact reports
exists *because the observation has already happened* and produced a
four-dimensional Lorentzian base. That is a computational corroboration of
BD-C's finding that `MET(X)` is an argument of the source's own action — the
observation is what makes the question askable — and it is not a claim that
BD-C's argument depends on it.

---

## 4. THE HAMILTONIAN ROUTE — a second, independent reduction, same answer

The covariant route needs a null covector and no choice of time. The
Hamiltonian route needs the opposite: a timelike `n` (a foliation), the spatial
slice `n^⊥`, a spatial momentum `q`, and the Coulomb transverse plane
`{a ∈ n^⊥ : ⟨q,a⟩ = 0}`. Different data, different construction.

```text
  spatial slice n^perp             dim 3, inertia (3,0)        DEFINITE
  Coulomb transverse plane         dim 2, inertia (2,0)        DEFINITE
  reduced pairing, source form     (98, 84)     -- identical to section 3
  reduced pairing, compact form    (182, 0)     -- identical to section 3
```

Run for three different spatial momenta `q` (`[E]`). **Both reductions land on
the same inertia.** This is the answer to the hostile charge in §10: the
verdict is not an artifact of picking the convenient quotient, because the two
standard quotients of gauge theory — one covariant and time-free, one
Hamiltonian and time-dependent — agree.

---

## 5. ROBUSTNESS SWEEP — six candidate bare-module reductions

Each candidate is an explicit subquotient `U` of `Λ¹`; the descended form on
`U ⊗ ad` is computed by direct congruence on the ambient Gram.

```text
candidate                          dim U  base       dim   source kappa   compact kappa
ambient Lambda^1 (x) ad              4   (3,1)       364   (189, 175)     (273,  91)
constraint surface only (null k)     3   (2,0,1)     273   ( 98, 84, 91)  (182, 0, 91)
YM SYMBOL QUOTIENT (null screen)     2   (2,0)       182   ( 98,  84)     (182,   0)
timelike slice (BD-A's object)       3   (3,0)       273   (147, 126)     (273,   0)
spacelike slice                      3   (2,1)       273   (140, 133)     (182,  91)
massive (Proca) 3-plane              3   (3,0)       273   (147, 126)     (273,   0)
```

Three things to read off, all `[E]` except where marked:

1. **No candidate is definite at the source trace form.** Every one has both a
   positive and a negative part. The sweep is over the quotients, and the
   answer does not move.
2. **Every reduced form factorises**: its positive part is exactly
   `p_U p_κ + n_U n_κ`. That is not assumed; it is checked for each candidate,
   and it is the empirical face of §6's theorem.
3. **`[C]` fires:** the *spacelike* slice is indefinite `(182, 91)` even at a
   **compact** fibre form. So the machinery is not rigged to say "definite
   whenever `κ` is compact" — a bad base subquotient still fails.

---

## 6. THE BARE-MODULE THEOREM — no equivariant subquotient cures an indefinite fibre form

> **Theorem (BD-D).** Let `𝔤` be a real Lie algebra with `End_𝔤(𝔤) = ℝ` (the
> adjoint absolutely irreducible), let `Λ¹` be `d`-dimensional with a
> nondegenerate symmetric `N`, and let `κ` be `Ad`-invariant and nonzero on
> `𝔤`. Then:
>
> 1. Every `𝔤`-submodule of `Λ¹ ⊗ 𝔤` is `U ⊗ 𝔤` for a unique `U ⊆ Λ¹`; hence
>    every equivariant subquotient is `(U/U') ⊗ 𝔤` and its descended form,
>    where defined, is `(N|_{U/U'}) ⊗ κ`.
> 2. A tensor product of nonzero symmetric forms is **definite iff both factors
>    are definite**.
>
> **Therefore, if `κ` is indefinite, no `Γ(Ad P)`-equivariant subquotient of
> the bare module `Λ¹ ⊗ ad P` carries a definite descended form.** This theorem
> does not classify an enlarged ghost/antifield complex, a differential mixing
> extra representations, an interacting BV cohomology, or an analytic domain.

**Part 2, exhaustively.** Over all `(p_A,n_A,p_B,n_B)` with each part at most
6 and both factors nonzero — **2304 cases, zero exceptions** (`[E]`). The law
`sig(A ⊗ B) = (p_Ap_B + n_An_B, p_An_B + n_Ap_B)` is itself certified against
direct congruence on 225 cases first.

**Part 1, and its hypothesis, computed rather than cited.** `Λ¹ ⊗ 𝔤 ≅ 𝔤^{⊕d}`
as a `𝔤`-module with multiplicity space `Λ¹`, so submodules correspond to
subspaces of `Λ¹` **exactly when** `End_𝔤(𝔤) = ℝ`. Exact commutant nullspaces
over `ℚ`:

```text
  dim End_g(g):   so(3) 1    so(2,1) 1    so(3,2) 1    so(4,1) 1    so(5) 1
                  so(3,1) 2  so(2,2) 2                            <- [C] CONTRARY

  dim Comm_g(Lambda^1 (x) g) = d^2 * dim End_g(g), verified exactly:
                  so(2,1), d=2  ->  4      so(2,1), d=4  ->  16
                  so(3,1), d=2  ->  8      (= 4 * 2, not 4)
```

**The contrary case is `so(3,1)`, and it is instructive rather than
embarrassing.** `so(3,1) ≅ sl(2,ℂ)_ℝ` is a complex Lie algebra viewed as real,
so `End_𝔤(𝔤) = ℂ` and there are submodules of `Λ¹ ⊗ 𝔤` that are **not** of the
form `U ⊗ 𝔤`. The universality clause genuinely fails there. **This does not
touch the load-bearing conclusion**, because the gauge-theoretic subquotients
used above — `⟨k⟩ ⊗ ad` and `k^⊥ ⊗ ad` — are of the form `U ⊗ ad` **by
construction**, being built from base data alone. Part 1 upgrades the result
from "these quotients" to "all equivariant subquotients of this bare module";
it supplies no theorem about GU's unconstructed derived physical quotient.

**For the GU-scale algebras the hypothesis is asserted with a named
dependency, not computed.** `dim End_𝔤(𝔤)` at `dim 𝔤 = 91` is an 8281-unknown
commutant solve and is not run here. What *is* computed: the trace forms are
nondegenerate (nullity 0, so `𝔤` is semisimple by Cartan's criterion), and
`dim so(7,7) = dim so(9,5) = 91` and `dim so(6,4) = 45` are **odd**, so none of
them carries a complex structure and none can have `End_𝔤(𝔤) = ℂ` globally
(`[E]`). The remaining step — that `so(n,ℂ)` is simple for `n ≥ 5`, `n ≠ 4`,
hence these real forms are absolutely simple — is a **standard fact cited, not
certified in this probe**. It is stated here rather than buried, because a
reader who rejects it still keeps the whole load-bearing result.

### 6.1 Equivariance is the load-bearing hypothesis, and here is the witness

The theorem is not vacuous and the hypothesis is not decoration. Take the
Cartan split `so(7,7) = 𝔨(42) ⊕ 𝔭(49)`, on which `κ` is negative and positive
definite respectively (`[E]`: `dim 𝔭 = 49`, `κ|_𝔭 = (49,0)`). Then

```text
  screen (x) p    has dimension 98  and inertia  (98, 0)    DEFINITE   [C] fires
```

**at the source group, with the source's own indefinite trace form.** So a
definite descended form on a subspace of the comparator quotient *does* exist —
and `𝔭` is **not** `ad`-invariant (`[E]`: `[𝔭,𝔭]` is a nonzero bracket leaving
`𝔭`). **Definiteness is available exactly at the cost of equivariance.** That
is BD-A §5.2's joint-unsatisfiability statement, reproduced one quotient
further down, and it is the sharpest form of what the reduction can and cannot
buy.

---

## 7. WHICH LEDGER ROWS THIS BEARS ON, AND UNDER WHAT CONDITION

BD-A's string rule returns a ten-row **class H**:
`RA-A4`, `RA-A5`, `RA-B6`, `RA-D4`, `RA-E4`, `RA-E6`, `RA-G1`, `RA-G4`,
`LT-SM4`, `LT-SM6`. That census is reproducible, but it does not make BD-D
direct evidence for those rows. Nine rows do not demand positivity at all, and
`RA-D4` demands an interacting positive BRST cohomology with a chiral light
spectrum—an object this free ordinary-gauge symbol computation does not build.

The transportable statement is conditional and narrower:

> If a future GU construction has a physical carrier that is an equivariant
> subquotient of the same bare `Λ¹ ⊗ ad P` module, and if its pairing descends
> from `N ⊗ κ` without ghost/antifield mixing, then an indefinite `κ` cannot
> become definite by the quotient alone. On the particular free Yang--Mills
> symbol quotient, definiteness is exactly `n_κ = 0`.

Those “if” clauses are the bridge. They are not established for any of the ten
ledger rows, so no row acquires `n_κ = 0` as a filed condition from this
artifact.

**Zero rows advance.** No verdict, reason kind, priority, canon,
`CURRENT-STATE` or public posture moves. The sequential ledger is untouched. The
movement available to a canonical owner is a **re-typing**, not an advance:

| object | movement available | condition |
|---|---|---|
| `LT-GR6b`'s positivity subclause | split from base duality and retain as an open physicalization debt; BD-D supplies a conditional comparator certificate, not the GU object | source-open/unsupplied; bridge required |
| the ten class-H rows | no filed movement from BD-D | each row's actual carrier, action, quotient and spectrum must be bridged separately |
| BD-A §5.3's *"two Cartan involutions"* price | falls to one on `P_k^{YM,sym}` only | comparator characteristic variety; no GU owner removed |
| `M-H17` (iii)–(iv) / PC-3 | **executed for one sector** (ordinary gauge `Ω¹(ad P)`, free level) | **not** executed for the RS/`ker Γ` carrier the register row actually tracks, and **not** at the interacting level |

---

## 8. THE KKT OBJECT IS VACUOUS HERE; THE PAIRING IS NOT

The brief names `Zᵀ H Z` as the object that governs stability. Computed
(`[E]`):

```text
  Z^T H Z  =  0   identically on the free symbol quotient.
```

Necessarily so: `Z` spans `ker H(k)`, so `H Z = 0`. **In a gauge field theory
the constraint null space *is* the Hessian kernel** — that is what gauge
invariance means at the symbol level — and the KKT reduced Hessian carries no
information. The content sits entirely in `Zᵀ B Z`, the descended **pairing**,
which is a state-space metric rather than a stability matrix.

That is not a technicality; it is the reason the answer is a **Krein** answer:

```text
  reduced pencil,  descended form INDEFINITE :  det(H - lam B) = -lam^2 - 1
                                                no real root                 [E]
  reduced pencil,  descended form DEFINITE   :  disc = (a-c)^2 + 4b^2 >= 0
                                                real spectrum                [C]
```

reproducing BD-A §7.2 and `W183`/`W178` one quotient further down. Thus
definiteness of the descended form supplies a **uniform real-spectrum
guarantee** for symmetric pencils, while indefiniteness permits—not forces—
complex pairs. No physical mass operator is built here, so this observation
does not directly adjudicate the ten class-H rows.

---

## 9. THE KREIN CERTIFICATE — and the price falls from two involutions to one

The Cartan involution is built, not quoted: `θ(X) = −Xᵀ`, verified to stay in
`so(7,7)`, to satisfy `θ² = 1`, and to be a Lie algebra automorphism (`[E]`).
In the built basis it is **diagonal**, with entries `η_i η_j` — verified
entrywise — giving the split `𝔨(42) ⊕ 𝔭(49)`.

```text
  on P_k^{YM,sym} (dim 182):              J = 1_screen (x) theta
      J^2 = 1,  J is B-selfadjoint,  -B(., J.)  =  (182, 0)     DEFINITE   [E]
      control: J = 1 gives back            B    =  ( 98, 84)    INDEFINITE [C]
      control: a NON-Cartan involution     fails to definitise             [C]

  on the AMBIENT (dim 364):               J = P_base (x) theta
      -B(., J.)  =  (364, 0)   -- but this needs TWO involutions           [E]
      control: the FIBRE involution alone leaves the ambient indefinite    [C]
```

**Reading, with the credit where it belongs.** The Krein mechanism is
`GEOMETER-VS-PHYSICS-OBJECTS.md`'s settled ghost-clearance row and `VG-V2`'s
machine-checked `B_θ > 0`; BD-A's Lens Q2 already concluded that *"the row
should demand a Krein structure, not positivity."* **BD-D claims none of that.**
What BD-D adds is one number and one count: the certificate on
`P_k^{YM,sym}` is `(182,0)`, and that comparator quotient **halves the
involution count**. BD-A §5.3 priced
positivity at two Cartan involutions, one per factor, with the base one free
*given* the observation section and a chosen timelike line. On
`P_k^{YM,sym}` the base involution is not needed — the screen form is definite,
fixed by the comparator's characteristic variety rather than by a separate
timelike-line choice. The Lorentzian metric whose light cone defines the screen
is still the same section, with the same `chi(X^4) = 0` globality condition.
This lowers the price only inside the comparator.

**So the answer to the brief's question 3 is conditional:** a one-involution
Krein majorant exists on the free symbol quotient. Whether GU's actual
physical cohomology exists, inherits this form, and meets the required
positivity/domain conditions remains open.

---

## 10. HOSTILE REVIEW — run on my own result

**H1. "Your comparator quotient is the one that gives a clean answer. You chose
the null screen because `(2,0)` is definite."** *The strongest objection, and
the one the brief flagged.* Four independent answers, in increasing order of
weight.

(a) The null screen is not *chosen*; it is **forced**. Off the light cone the
gh-0 quotient is **zero-dimensional** (`[E]`), so there is no other candidate
carrying anything. (b) The **Hamiltonian route** (§4), which needs a chosen
timelike direction and no null covector — different data, different
construction — lands on the same inertia. (c) The **sweep** (§5) computes six
candidates and **none** is definite at the source form. (d) §6 proves the
bare-module verdict for every equivariant subquotient. **The limitation is not
only equivariance:** GU's eventual cohomology may live in an enlarged
ghost/antifield complex, use a different differential, or carry an analytic
domain not represented by a subquotient of `Λ¹ ⊗ ad P`. Section 6 makes no
claim about those possibilities. Section 6.1 merely shows the definite,
non-invariant witness `screen ⊗ 𝔭` inside the tested module.

**H2. "You imported a Yang–Mills constraint into a theory that has no
action."** **Conceded, named in the classification line, and the reason §6
exists.** GU's action is the open object; there is no source-derived Gauss law
and this repository has never built one. The import fixes the *dimension* (182)
and the *base inertia* (2,0). It does **not** fix the bare-module theorem in §6,
which is independent of the constraint. **A reader who rejects the Yang–Mills
symbol keeps §6 as algebra and loses §§2–5 as a physical candidate.** That is
the honest split; neither half constructs GU's quotient.

**H3. "GU's gauge group is `𝒲 = 𝒢 ⋉ Ω¹(ad P)`, not `𝒢`. You quotiented by the
wrong group."** **Half right, and the half that is right is a real scope
limit.** I quotiented by `𝒢 = Γ(Ad P)`, the source's own gauge group and the
one `LT-GR6b`'s trigger names in the phrase *"`Γ(Ad P)`-equivariant"*. The
translation factor `Ω¹(ad P)` acts on the *affine space of connections*, so on
the tangent module `V` it acts trivially (BD-A verified `ad(v)|_V = 0` from
structure constants); quotienting `V` by the translation orbit would give a
point, which is not a physical quotient in any sense the ledger uses. **BD-B is
the right pointer here:** it proved the whole verdict is a function of the
translation depth `t`, and this artifact sits at the `𝒢`-only subscript. A
route that wants the full `𝒲` should read BD-B's lattice, not this file.

**H4. "`Zᵀ H Z = 0` means you did not compute a reduced Hessian at all, so you
did not test the brief's hypothesis."** **I computed the reduced Hessian and it
is zero; that IS the test result.** The brief's hypothesis was that the reduced
object might be definite where the ambient is not. The reduced *Hessian* is
identically zero — vacuous, not definite — and the object that carries the
content is the reduced *pairing*, which I computed exactly. Reporting that the
named object is vacuous, and naming the one that replaces it, is the answer to
the question, not an evasion of it. **What I do not have:** an interacting or
background-curvature Hessian, where `Zᵀ H Z ≠ 0`. That needs the action.

**H5. "The `(98,84)` is just `2 × (49,42)`. You multiplied by two and wrote
2500 lines."** **Largely conceded, and it is the correct reading of §3.** Once
the base factor is known to reduce to `(2,0)`, the reduced inertia is
arithmetic. What is not arithmetic: that the quotient *descends at all* (§2,
with two firing controls), that the removed block is *neutral* (§3.1), that
**every** equivariant quotient factorises (§6), that the base cure is
*Lorentzian-specific* (§3.3), and that a definite non-equivariant witness
exists at the source group (§6.1). If a reader takes one thing it should be §6,
and §6 is not a multiplication.

**H6. "You claim the base half is cured, but you still need `chi(X^4) = 0` to
have a Lorentzian metric at all, so nothing got cheaper."** **Correct, and
stated in §9 rather than left to be found.** The globality condition is
unchanged and is BD-A's and the 2026-08-08 gate's. What falls is only the
*second* base datum — BD-A §5.3's timelike covector line — which the comparator
characteristic variety supplies. The net change is one comparator choice, not
one GU-owned object or one topological hypothesis.

**H7. "You are executing PC-3, which the design packet said would probably
fail, and reporting a failure as a result."** The packet's own outcome table
types a failing free-level check as **expected and not a program kill**, and
that typing is respected here: the result is `(98,84)` at the source form, and
`(182,0)` at a compact one, with the difference isolated to one named external
datum. **What would be dishonest is reporting `(182,0)` as GU's answer.** It is
not; it is the answer *after* `REDUCTION_EXTERNAL`, which is exactly how BD-A
and the noncompact-reduction audit already price it.

**H8. "The `so(3,1)` contrary case shows your theorem's hypothesis can fail, so
the theorem is weak."** The hypothesis fails for exactly the algebras with a
complex structure, which have **even** real dimension; the GU candidates have
dimension 91 and 45, **odd** (`[E]`). The conclusion for the particular
base-defined subquotients does not use the hypothesis, because those objects
are `U ⊗ ad` by construction. The `so(3,1)` case is in the
certificate because a theorem whose hypothesis is never tested is a theorem
whose hypothesis is decorative.

---

## 11. POSTFLIGHT — five lenses, run inline

The preflight lenses were chosen for *deciding what to compute*. These are
chosen for *what the computed object is*, and four of the five bind objects the
preflight did not touch.

### Lens Q1 — spectral theory of pencils: what does the reduced form actually govern?

The generalized eigenproblem `H φ = λ B φ` has a real spectrum for symmetric
`H` when `B` is definite, and admits complex-conjugate pairs when `B` is not
(`[E]`/`[R]`, §8). So the descended form is not a bookkeeping object: it is the
**definitizability** condition on the physical mass operator. The lens's
refusal: this says nothing about whether GU's spectrum is *real*, because no
`H` has been built. It says that whichever `H` is eventually built, its
reality is controlled by `n_κ`, and by nothing in the base or the quotient.
`W183`'s exceptional-point collision and `W178`'s explicit complex pair are the
same phenomenon; this places it on the reduced object.

### Lens Q2 — numerical linear algebra over exact fields: is the method sound at 364?

Every inertia here is a **Sylvester congruence** with exact rational pivots;
the only decision taken is the *sign* of a pivot, and Sylvester's law makes
inertia a complete congruence invariant. No eigenvalue is computed, no
characteristic polynomial is formed, no float is constructed, and
`assert_no_float` sweeps the entire result dict. The tensor signature law is
**not** used to obtain any reported inertia: it is certified *against* direct
congruence on 225 cases and then used only for the exhaustive 2304-case
definiteness sweep, where the objects are inertias rather than matrices — which
is legitimate exactly because inertia is a complete invariant. Two honest
notes: (i) the restriction `Zᵀ B Z` is computed with sparse lift columns, which
is the same matrix product, not a shortcut around it; (ii) the Krein forms
`−B(·,J·)` use the fact that `J` is **diagonal** in the built basis, which is
verified entrywise before it is used.

### Lens Q3 — BV/BFV: what did the free-level computation NOT reach?

Everything here is **linearised and free**, at a single symbol covector, and
fibrewise. Not reached, stated so no reader takes them: (a) the **interacting**
BRST charge, `M-H17` step (i), unbuilt and blocked on the `Y¹⁴`
connection-curvature 2-form; (b) `H⁰` of an interacting complex, as opposed to
the symbol cohomology of a free one; (c) the **antifield** sectors — this is
gh-0 only, and says nothing about the quartet structure at nonzero ghost
number; (d) any **global** statement — the screen is a bundle over the
projectivized null-cone bundle of `X⁴`, not over `X⁴`, and no global section is
claimed or needed; (e) any **domain, closure, Fredholm, boundedness or
Hilbert-space** statement, which `RB1`'s fence already covers and which applies
unchanged here.

### Lens Q4 — Layer-0 / homonym discipline: how many objects are called "the physical quotient"?

At least four in this repository, and conflating them is the standing risk:
(i) BD-A's `ker(c) ⊗ ad`, a codimension-1 gauge slice, dim 273; (ii) BD-D's
gh-0 cohomology `(k^⊥/⟨k⟩) ⊗ ad`, dim 182; (iii) the metric-sector
`10 → 6 → 2` filtration (`k77-global-even-bv-null-green-domain-2026-08-05`),
a **different sector**, symmetric 2-tensors not one-forms; (iv) the ambient
K77 `(6,6)` rank-12 screen on `Y¹⁴`
(`selected-k77-total-upsilon-null-screen-2026-08-07`), which its own author
fenced from (iii) in writing. **These are four objects, and BD-D computes only
(ii).** Its `(7,7) → (6,6)` row reproduces (iv) and is not a claim about it. The
lens's output: any future artifact citing "the physical quotient" in this
program must say which of the four, and the ledger rows `RA-G1` and `RA-D4`
currently do not.

### Lens Q5 — ledger metrology: which direction does this move the file, and should it be distrusted?

The exact computation narrows a bare-module escape while leaving the GU bridge
open. It neither removes nor adds a GU-owned object.

```text
comparator price    two involutions -> one on P_k^{YM,sym}
bare-module result  an equivariant subquotient cannot cure indefinite kappa
GU debts retained  Lorentz section; fibre selector; action/BRST/BV quotient;
                    analytic positive physical domain
demands ADDED       none
rows advanced       0        `SAME` rows touched  0        free_object_delta   0
```

The involution count follows from the two-line fact that `(1,1) ⊗ κ` is neutral.
Section 6 is the durable algebraic result; the rest remains comparator-scoped.

---

## 12. CLAIM CEILING

**May be claimed, exactly and only:**

- The free linearised Yang--Mills symbol cohomology `P_k^{YM,sym}` of
  `Λ¹ ⊗ ad P` on a Lorentzian `X⁴` is `(k^⊥/⟨k⟩) ⊗ ad` for null `k`, of dimension
  `2 dim 𝔤` = 182 (`so(7,7)`, `so(9,5)`) and 90 (`so(6,4)`); it is
  zero-dimensional off the light cone; the pairing descends to it and not to a
  gauge quotient without a constraint; and the radical it removes is exactly
  the gauge subspace of dimension `dim 𝔤`.
- The exact descended inertias `(98,84)`, `(182,0)`, `(90,92)`, `(48,42)`,
  `(90,0)`, obtained by direct rational congruence, together with
  lift-independence and null-covector-independence.
- That the removed complement is a **neutral** `(dim 𝔤, dim 𝔤)` = `(91,91)`
  block for **every** fibre form, and that ambient = reduced + removed exactly.
- That the reduced negative part is `2 n_κ` where the ambient's is
  `3 n_κ + p_κ`; hence the base contribution is removed exactly and the fibre
  contribution is not.
- The base-screen rule `(p,q) → (p−1,q−1)` and its consequence that the screen
  is definite **iff** the base is Lorentzian; hence that on a `(7,7)` base the
  screen quotient is neutral `(546,546)` for any fibre form. **Novelty is NOT
  claimed for the `(6,6)` ambient screen** — `selected-k77-total-upsilon-null-screen-2026-08-07`.
- That the Hamiltonian/Coulomb reduction reaches the same inertia.
- **The bare-module theorem**: for `End_𝔤(𝔤) = ℝ`, every equivariant subquotient is `U ⊗ 𝔤`
  and a tensor product is definite iff both factors are; hence no equivariant
  reduction can cure an indefinite fibre form. With `so(3,1)` and `so(2,2)` as
  the computed cases where the universality hypothesis fails, and with the
  absolute simplicity of `so(n,ℂ)` for `n ≥ 5, n ≠ 4` flagged as **cited, not
  certified here**.
- That a definite descended form exists on the **non-equivariant** subspace
  `screen ⊗ 𝔭`, inertia `(98,0)`, at the source group.
- That `Zᵀ H Z` vanishes identically on `P_k^{YM,sym}` at the free
  level, so the KKT reduced-Hessian object is vacuous and the descended
  **pairing** is what governs.
- The Krein certificate `−B(·,J·) = (182,0)` with `J = 1_screen ⊗ θ`, and that
  the ambient needs two involutions where the quotient needs one. **Novelty is
  NOT claimed for the Krein mechanism** (`GEOMETER-VS-PHYSICS-OBJECTS.md`,
  `VG-V2`, BD-A Lens Q2) nor for `κ_θ > 0` (`VG-V2`).

**May NOT be claimed, and is not:**

- That GU has a Gauss law, a constraint, an action, or an interacting BRST
  charge. None of these is built anywhere, and the Yang–Mills symbol used here
  is a declared comparator import.
- That `P_k^{YM,sym}` is GU's physical quotient, or that the bare-module theorem
  extends to enlarged ghost/antifield complexes, non-split derived cohomology,
  interacting dynamics or analytic domains.
- That `M-H17` is discharged. Steps (iii)–(iv) are executed for **one sector at
  the free level**; the row tracks the RS/`ker Γ` carrier and the interacting
  charge, neither of which is touched.
- That PC-3 has been run on the packet's own target. It has not.
- That GU's physical spectrum is real, or that any mass matrix exists.
- That `𝔤` is `so(7,7)` rather than `so(9,5)`, `sp(32,32;ℍ)`, or `ad P_H` with
  `H = U(64,64)`. **Both signature horns are carried and both are indefinite**;
  BD-B's retyping of the source's own `Δ1` fibre algebra is not adjudicated
  here and its `U(64,64)` Killing form is degenerate, which this artifact does
  not compute.
- That the base duality, the moving pairing, or the observation reduction is
  advanced. Zero rows advance.
- Any domain, boundedness, Fredholm, Hilbert-space, measure or global-section
  statement.
- That positivity is impossible for GU, or that the source rejects it on the
  observed physical sector. Section 6.1 exhibits a definite non-equivariant
  witness inside the tested module; BD-C now types observed-sector positivity
  as source-open/unsupplied.

**Not laundered:** no grant is converted into a derivation. The one conditional
result — that a compact fibre form gives `(182,0)` — is reported **only** with
its condition, `REDUCTION_EXTERNAL`, in every place it appears. The
Yang–Mills import is named in the classification line, in H2, and in the claim
ceiling, and §6 is written specifically so the verdict survives without it.

---

## 13. REPRODUCE

```bash
cd /path/to/gu-formalization
_local/cas-venv/bin/python tests/channel-swings/joe_directed_bdd_the_quotient_cures_the_base_not_the_fibre.py
_local/cas-venv/bin/python tests/channel-swings/joe_directed_bdd_the_quotient_cures_the_base_not_the_fibre.py --selftest
```

Expected: `CERTIFICATE: 95/95 checks pass; no load-bearing float (swept).`,
exit 0, split `[C] 16  [E] 61  [R] 18`; then
`FAILURE-PATH SELFTEST: PASS (16/16 mutations drove exit 1)`. The probe resolves
this artifact relative to its own location and fails if the headline numbers are
not in it.
