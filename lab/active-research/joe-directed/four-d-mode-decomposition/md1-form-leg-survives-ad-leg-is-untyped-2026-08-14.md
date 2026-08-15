---
artifact_type: exploration
status: exploration
doc_type: mechanism-scope-gate
created: 2026-08-14
work_item: MD-1
channel: four_d_mode_decomposition
title: "MD-1: the nine non-SM directions are 4D VECTORS on the FORM leg -- the source-declared reduction is a contraction (pullback along the observation section), and it sends every ad-valued one-form on Y14 to exactly one 4D one-form. But on the AD leg the typing is NOT determined: the fibre Sym^2(T*X4) is endogenous, so the physical Lorentz algebra embeds in so(6,4), and NO nonzero subspace of k is Lorentz-invariant -- k's 12+9 split is not a Lorentz-covariant labelling under a soldered ad bundle. PV-1/PV-2/CU-1/MV-1/MV-2 survive the form-leg test and inherit a newly named, undecided fork SOLDERED-AD vs INERT-AD on the ad leg."
grade: "EXACT rational arithmetic (fractions.Fraction) on integer/rational matrices plus exact sympy symbolic differentiation, 67/67, exit 0, no float load-bearing anywhere. Signatures by Sylvester congruence, never by eigenvalues. NINE planted controls that FIRE (A4, A5, B7b, B10, B12, C20, D5, E4, F3b). Independently re-derives four banked canon numbers -- Frobenius (7,3), trace-reversed DeWitt (6,4), horizontal (3,1), total (9,5) -- and four PV-2 numbers -- dim k = 21, dim p = 24, Killing negative-definite on k, positive-definite on p. NOT: an action, a kinetic term, a propagator, a mass, a quantization, a source action, a decision of the SOLDERED-AD fork, or any claim-status movement."
disposition: FORM_LEG_CLEARS_THE_FIVE_GATES__AD_LEG_OPENS_A_NEW_UNDECIDED_LAYER0_FORK__NO_NONZERO_SUBSPACE_OF_K_IS_LORENTZ_INVARIANT
canon_verdict_change: none
steering_effect: unchanged
canonical_effect: pending_integration
fork_declared:
  - id: SOLDERED-AD
    horns:
      - "ad(P_H) is soldered: the chimeric carrier is built functorially from TX, so the physical local Lorentz group is canonically a subgroup of the gauge group and the ad index is NOT Lorentz-inert"
      - "ad(P_H) is inert: P_H is an independent principal bundle and the ad index is an ordinary internal label, Lorentz-inert"
    status: open
    note: "NEW. Named here for the first time. Not decided by this artifact and not decidable from the declared field content."
fork_assumed:
  - CARRIER-SPLIT
  - SECTION-VS-OBSERVERSE
depends_on:
  - lab/active-research/joe-directed/photon-extra-vector-spectrum/pv1-available-orbits-retain-an-extra-massless-vector-2026-08-14.md
  - lab/active-research/joe-directed/photon-extra-vector-spectrum/pv2-observation-cannot-reach-the-extra-vectors-2026-08-14.md
  - lab/active-research/joe-directed/coupling-unification/cu1-left-right-degeneracy-forbids-unification-2026-08-14.md
  - lab/active-research/joe-directed/massless-vector-cosmology/mv1-the-surviving-massless-vectors-meet-the-data-2026-08-14.md
  - lab/active-research/joe-directed/massless-vector-cosmology/mv2-all-four-abelian-mass-routes-closed-2026-08-14.md
  - canon/shiab-existence-cl95.md
  - docs/paper-formalization-candidates.md
  - papers/drafts/Transcript into the impossible.md
  - lab/sources/claim-mining-toe-weinstein-complete-2026-07-31.md
  - explorations/vz-evasion/vz-schur-complement-2026-06-23.md
  - lab/process/perspective-passes/01-foundational-math-lenses/08-higher-dim-kk.md
scripts:
  - tests/channel-swings/joe_directed_mode_decomposition_form_leg_probe.py
---

# MD-1 — the form leg survives, the ad leg is untyped

## The joint being tested

Five of this session's negative results — PV-1, PV-2, CU-1, MV-1, MV-2 — count
"massless gauge bosons" on one shared, **imported** assumption: that GU's
ad-valued fields are conventional Yang-Mills VECTORS on 4D spacetime. MV-1
names the assumption in its own limits section and does not derive it:

> "Everything above presumes the surviving directions are propagating vector
> fields with Yang-Mills kinetic terms and gauge-strength couplings to the
> observed fermions. That is the standard reading of a gauge structure group;
> it is **not derived** in this repository for GU's connection sector, and it is
> load-bearing for every number in §5."
> — `mv1-the-surviving-massless-vectors-meet-the-data-2026-08-14.md`

A connection carries **two** indices, and each has to be typed separately:

| leg | lives in | question |
|---|---|---|
| **FORM** | `T*Y14` (14) | does it descend to a 4D one-form, or to a tower of 4D scalars? |
| **AD** | `Lambda^2` of the 14-dimensional chimeric carrier | is the internal label Lorentz-inert? |

The nine live in `k subset so(6,4) = Lambda^2(10)`, the **internal** block. That
location is verified, not assumed (F1–F3, with control F3b).

## Result — the two legs answer differently

> **FORM LEG: the nine are 4D VECTORS. The source-declared reduction is a
> CONTRACTION, and a contraction sends every ad-valued one-form on `Y14` to
> exactly one 4D one-form.**
>
> **AD LEG: not determined. The fibre is endogenous, so the physical Lorentz
> algebra sits inside `so(6,4)`; and NO nonzero subspace of `k` is
> Lorentz-invariant. Under a soldered ad bundle the `12 + 9` split of `k` is not
> a Lorentz-covariant labelling at all — which would break the SM's twelve
> exactly as hard as the nine.**

## 0. PREFLIGHT — five specialist lenses, each proposing a route

Recorded before computing. Cheapest kill-or-switch and one credible contrary
route are stated for each.

### Lens 1 — Kaluza-Klein / dimensional-reduction specialist

Route proposed: run the standard KK split `A_M -> (A_mu, A_m)`: one 4D vector
plus ten 4D scalars per ad direction, and read the nine as nine vectors plus
ninety scalars. **Rejected before running**, on source grounds: the primary
transcript disavows it in as many words — *"It doesn't — it's not extra
dimensions. **It's not Kaluza Klein.** The space that is four dimensional births
its own 14 dimensional ambient space"* (`Transcript into the impossible.md:29`).
Prior art independently reaches the same block from the geometry side: the
repo's own KK perspective pass concludes *"a 4-to-14 lift via the metric-bundle
is the only first-principles-natural route to '14,' and it is **not a
Kaluza-Klein compactification** … As a KK program it fails at step one:
non-compact internal space"*
(`lab/process/perspective-passes/01-foundational-math-lenses/08-higher-dim-kk.md`).
**Cheapest kill-or-switch:** if the fibre's Lorentz-trivial isotypic component
is 10, KK bookkeeping is at least kinematically consistent; if it is 1, KK is
kinematically wrong regardless of the source's disavowal. **Contrary route:** KK
could still be the right *effective* bookkeeping if the internal group is
declared independent of Lorentz — which is exactly the SOLDERED-AD fork.

### Lens 2 — bundle geometer

Route proposed: do not decompose the form index at all; the only reduction map
the source supplies is *pullback along a section*, `s^*: Omega^1(Y) ->
Omega^1(X)`. `s` is the observation, i.e. a metric `g`. Compute `ds` and its
transpose in explicit coordinates. **This is the route taken.** It also matches
the author-stated Layer-0 correction WG-B06 (`O 01:34:49`): *"The relevant map
is a contraction, not a projection."* **Cheapest kill-or-switch:** if `s^*`
turned out to equal horizontal projection for a general section, projection and
contraction would agree and the distinction would be idle. **Contrary route:**
the ambient theory may be the physics and the pullback merely a readout, in
which case the 4D typing question is the wrong question (`SECTION-VS-OBSERVERSE`,
`status: open`).

### Lens 3 — 4D representation theorist (little group / spin content)

Route proposed: the fibre is `Sym^2(T*_x X4)` — built from the **same** tangent
space as the base. So the local Lorentz group acts on it as `Sym^2` of the
vector rep, i.e. `(1,1) + (0,0)` = 9 + 1, not as ten inert labels. Then
`Lambda^2` of that is `so(6,4)`, and the physical Lorentz algebra embeds in the
ad bundle. Compute the branching and test invariance of `k`. **This is the
decisive route.** **Cheapest kill-or-switch:** if `so(3,1)_endo` were contained
in the maximal compact `k`, then `k` would be Lorentz-invariant and the whole
worry would evaporate in one line. **Contrary route:** `P_H` may be an
independent principal bundle with no canonical soldering, restoring inertness.

### Lens 4 — general relativist

Route proposed: read the whole structure as first-order gravity. If the local
Lorentz group is inside the gauge group, then connection components along the
Lorentz directions are a **spin connection**, and components along a
`Sym^2`-valued direction are **vierbein/graviton-like**, not vector bosons —
the MacDowell-Mansouri pattern. Test: exhibit an explicit Lorentz-invariant
9-dimensional submodule of `so(6,4)` (the `trace ^ traceless` block) and check
whether it is the nine. **Cheapest kill-or-switch:** if that 9 lies inside `k`,
the nine may literally *be* the vierbein-like multiplet and the five gates are
mistyped in a specific, nameable way. **Contrary route:** GU's `epsilon` field,
not the connection, may be the soldering carrier, leaving the connection sector
ordinary.

### Lens 5 — source-fidelity reader

Route proposed: read what the transcript actually declares as the field content
and as the reduction, and refuse to supply either. It declares **both**:

> *"it's super simple in terms of the linearized field content. It's **zero
> forms and one forms valued either in add or in the spinners**, and that's it."*
> (`Transcript into the impossible.md:173`)
>
> *"go to the bundle of metrics, **pull back** spinners, and you'll find that
> you're already in the standard model."* (line 107)
>
> *"There is no grand unification. It's just a **normal bundle** in your ambient
> space. You're picking it up because you're pulling back spinners from the
> space of point wise metrics, and you're confusing the normal bundle as if it
> fell out of the sky."* (line 125)

The third quote is the load-bearing one: it says the internal `10` **is** the
normal bundle of `X4` inside `Y14`, i.e. the endogenous `Sym^2(T*X4)`. That is
an argument for SOLDERED-AD from the author's own mouth. **Cheapest
kill-or-switch:** find a source statement declaring the structure group of
`P_H` independent of the frame bundle — none was found. **Contrary route:** the
quote is about the **spinor** index (`Spin(10)` from pulled-back spinors), not
about the connection's ad index; transferring it is an identification the source
does not make. `WG-SH3` discipline applies: do not attribute manuscript
vocabulary to the episode.

### Lens 6 — honesty auditor

Route proposed: assume the finding will be a fork, not a kill, and pre-commit to
reporting it that way. Pre-registered failure mode: **claiming the five gates are
broken when the same argument breaks the SM's twelve just as hard** — which would
be a reductio against my own reading, not a result against theirs. Also
pre-registered: the parent brief's own framing calls the vertical legs "4D
scalars carrying an internal `Sym^2(T*X4)` index." That phrase is internally
inconsistent — an index in `Sym^2(T*X4)` is by construction *not* Lorentz-inert
— and the probe must test it rather than inherit it. **Cheapest kill-or-switch:**
run the trivial-isotypic-component count on the fibre; 1 versus 10 settles it.

## 1. PRIOR ART — what exists, and what is attributed

| prior result | where | relation to MD-1 |
|---|---|---|
| the assumption itself, **named and undischarged** | MV-1 §"Unstated dynamical assumption" | MD-1 is the first artifact to *test* it. MV-1 gets the naming credit |
| `Y14 = Met(X4)` is **not** a KK compactification; non-compact fibre kills spectrum quantization | perspective pass `08-higher-dim-kk.md` | independently reaches Lens 1's conclusion from geometry. Not re-claimed |
| observation **pullback/restriction**, not a supplied defect action, is the author-guided 4D route | `lab/sources/g3-weinstein-section-pullback-recheck-2026-07-31.md`; `selected-k77-h640-*-2026-08-11.md` (`SOURCE_CONFIRMS_Y14_OPERATOR_AND_OBSERVATION_PULLBACK`) | MD-1 uses exactly this map and adds its explicit coordinate form |
| `s^*` on the `H*/N*` split, and "normal RS components are **KK scalars** not spin-3/2 fields" | `vz-schur-complement-2026-06-23.md` §18.3, graded **VERIFIED**, "No approximation is made"; carried into `canon/no-go-class-relative-map.md:401` and five explorations | **MD-1 finds this is a projection, not the pullback** — see §5, weakest seam |
| a soldering map `j_s: normal bundle -> ad(P_s)` already used in the action spec | `explorations/cycle-gates-and-audits/gu-minimal-action-spec-2026-06-24.md:95,161` | makes the SOLDERED-AD horn concrete rather than hypothetical |
| GU torsion has "the same structural shape as MacDowell-Mansouri / Cartan first-order gravity" | `cb-b-lagrangian-terms-2026-08-05.md:528,1092`; council `science-council:270-277`; and Weinstein names MacDowell-Mansouri himself (`toe-weinstein-gu-40-years.md:426`) | Lens 4's pattern is already in the repo for the **torsion** row; MD-1 applies it to the **ad index of the connection**, which is new |
| `so(6,4) = k(21) + p(24)`, Killing negative on `k`, positive on `p`, SM's 12 inside `k`, nine non-SM survive | PV-2 | independently re-derived here from a completely different starting point (`Sym^2` of a Lorentzian 4-metric rather than an abstract `(6,4)` form). **All four numbers reproduce** |
| Frobenius `(7,3)` -> trace-reversed `(6,4)`; horizontal `(3,1)`; total `(9,5)` | `canon/shiab-existence-cl95.md`, `GEOMETER-VS-PHYSICS-OBJECTS.md` | independently re-derived (A2, A3, A6, A7) |
| `VERTICAL-FROBENIUS-TRACE` is an open Layer-0 fork ("the trace reversal" is a homonym) | `lab/process/layer0-fork-registry.yaml` | MD-1 computes the **vertical Frobenius-fibre** horn only, and shows `lambda` genuinely discriminates (controls A4, A5) |

Nothing above is re-claimed. What is new in MD-1: (i) the explicit coordinate
form of the contraction and its consequence for the form leg; (ii) the
endogenous Lorentz embedding `so(3,1) -> so(6,4)` and the invariance tests on
`k`; (iii) the `SOLDERED-AD` fork.

## 2. THE FORM LEG — the contraction, and what it does

The observation section is `s: X4 -> Y14`, `s(x) = (x, g_{ab}(x))` — the section
*is* the metric. In adapted coordinates,

```text
ds(d_mu) = d_mu + (d_mu g_ab) d/d(g_ab)          rank 4                    (E1)

(s^* omega)_mu = omega_mu + omega_(ab) d_mu g_ab                            (E2)
```

verified symbolically with sympy against a general `g_{ab}(x)`. Three consequences,
all exact:

1. **Every ad-valued one-form on `Y14` descends to exactly one 4D one-form.**
   `s^*` is surjective onto `T*X` (rank 4, F4) and the horizontal leg alone
   already saturates it (`s^* o horizontal-inclusion = id`, F4b). So on the form
   leg the nine are nine 4D **vectors**, `(1/2,1/2)`. **PV-1, PV-2, CU-1, MV-1
   and MV-2 pass the form-leg test.**
2. **The vertical legs are contracted in, not split off.** They enter the *same*
   4D one-form, weighted by `d_mu g_ab`. This is WG-B06 made computational:
   *"the relevant map is a contraction, not a projection."*
3. **The contraction is lossy: `s^*` annihilates a 10-dimensional space of form
   legs** (E3). Those ten do not become 4D scalars; they are simply not read by
   the observation. Whether they reappear as independent 4D fields is a
   *dynamical* question about the action and the section's own equation of
   motion, and is not decided here.

And the disavowed alternative is **worse, not better**: under a KK-style
projection the vertical form leg is not ten 4D scalars. `Sym^2(T*X4)` under the
physical Lorentz group is `9 (symmetric traceless) + 1 (trace)` — its
Lorentz-trivial component is exactly **1**-dimensional (B11), where a genuine
Lorentz-inert KK internal space would give **10** (control B12 fires). So the
projection reading gives, per ad direction, a vector **plus a spin-2-type rank-2
tensor plus one scalar** (F5). The parent brief's framing — "VERTICAL legs (4D
scalars carrying an internal `Sym^2(T*X4)` index)" — is exactly the step this
refutes: an index valued in `Sym^2(T*X4)` cannot be inert, because it is built
from the same tangent space the Lorentz group acts on.

## 3. THE AD LEG — where it actually breaks

The fibre is endogenous, so the physical local Lorentz algebra `so(3,1)_g` acts
on it by `Sym^2` of the vector representation, preserves the Frobenius and
trace-reversed forms (B4, B5), and therefore embeds as a 6-dimensional
subalgebra of `so(6,4)` (C16, C17). That embedding is the entire content of
"endogenous": in a real Kaluza-Klein theory it does not exist.

Then, exactly:

```text
so(3,1)_endo meets BOTH Cartan summands: 3 rotations in k, 3 boosts in p   (C18)
    => so(3,1)_endo is NOT contained in k                                  (C19)

k is NOT invariant under so(3,1)_endo, witness [L_01, K_(0,1)] leaves k    (D1)
p is NOT invariant either                                                  (D2)

the LARGEST Lorentz-invariant subspace contained in k is ZERO              (D3)
the largest Lorentz-invariant subspace contained in p is ZERO              (D4)
the SMALLEST Lorentz-invariant subspace containing k is all of so(6,4)     (D6)
```

D3 is the load-bearing line and it is **basis-independent**: it does not need
PV-2's explicit choice of the nine. Since *no nonzero subspace of `k` is
Lorentz-invariant*, neither the SM's twelve nor the nine non-SM directions is a
Lorentz multiplet under a soldered ad bundle. "Nine 4D massless gauge bosons"
is then not a false statement — it is a **not-well-typed** one.

Non-vacuity is checked in both directions. The test finds invariant subspaces
when they exist (`so(3,1)_endo` itself, dim 6, D5 fires), and a compact
subalgebra alone *does* sit inside `k` (rotations, C20 fires), so C18/C19 are
discriminating rather than automatic.

The Lorentz-module structure of the ad block, exact:

```text
so(6,4)  =  6  (+)  9  (+)  30                       independent, 45 total  (G1,G2)

  6  = so(3,1) itself, R-irreducible (commutant = C, discriminant -4)    (G4,G5)
  9  = trace ^ traceless, R-irreducible (commutant = R)                  (G3,D7,D8)
 30  = the remainder; irreducibility NOT certified here, and NOT load-bearing
```

The `9` is the Lens-4 vierbein-like multiplet, and it is the *only* invariant
9. But only **3** of its 9 directions lie in `k` (D9) — so it is not the nine.
And `21`, `24` and `12` are not sums of `{6, 9, 30}` (G6), consistent with the
direct invariance failures.

## 4. WHAT THIS DOES AND DOES NOT SETTLE

**The five gates survive the test that was actually posed.** The worry was that
the nine might be 4D scalars from a KK tower. They are not: on the form leg they
are vectors, under the map the source declares.

**A different and undischarged problem is now named.** `SOLDERED-AD` vs
`INERT-AD` is not decided by GU's declared field content, and the two horns give
incompatible 4D typings for the *entire* connection sector:

| | ad index | the nine, in 4D | the SM twelve, in 4D |
|---|---|---|---|
| **INERT-AD** | Lorentz-inert internal label | nine vectors — five gates stand as written | twelve vectors |
| **SOLDERED-AD** | acts on by `Sym^2`, via the frame bundle | not a multiplet; typing undefined | **also not a multiplet** |

The right-hand column is why this is a fork and not a kill. SOLDERED-AD does not
selectively damage the nine; it damages the twelve identically. A reading on
which GU cannot type its own Standard Model gauge bosons is a reading on which
GU fails at once, for reasons far upstream of anything PV/CU/MV computed. So the
operative reading must be INERT-AD-with-a-declared-decoupling — and **the
declared content does not supply that declaration.** That is the honest form of
the answer: *the correct decomposition is not determined by the declared
content*, and what would determine it is a statement of how `P_H`'s structure
group relates to the frame bundle of `X4` — equivalently, whether the repo's own
soldering map `j_s` into `ad(P_s)` is a gauge-fixing convenience or a canonical
reduction.

## 5. INLINE HOSTILE REVIEW

**Strongest overclaim in this artifact.** Reading D3 as "the nine are not gauge
bosons." It is not. D3 says: *under SOLDERED-AD*, no nonzero subspace of `k` is
Lorentz-invariant. The fork is undecided, and under the other horn every number
in PV-1/PV-2/CU-1/MV-1/MV-2 stands untouched. Anyone quoting MD-1 as a kill of
those five gates is quoting one horn of a declared open fork as if it were the
result. Claim-indexed verdict doctrine: MD-1's target claim is *"the nine are
conventional 4D Yang-Mills vectors"*, and the verdict is **NOT-DETERMINED**, not
**FALSE**.

**Strongest contrary construction.** `P_H` is a principal bundle over `Y14`,
where "the physical 4D Lorentz group" is not defined at all — GU's own position
is that we are not in a four-dimensional world (*"are we on x four at all? And
the answer to me is absolutely not"*, `Transcript:101`). On that reading the
question MD-1 asks only arises after observation, and observation is a
*gauge-fixing*, so the failure of Lorentz-covariance of the `12+9` labels is a
gauge artifact rather than a physical statement. This is a real defence and MD-1
does not defeat it. It does, however, cost something: it makes every 4D particle
label in the program gauge-dependent, which is a larger bill than the five gates
were paying.

**Second contrary construction (mistyping).** The Lens-5 quote about the normal
bundle is about the **spinor** sector's `Spin(10)`, not the connection's ad
index. Transferring it is an identification the source does not make, and
`GEOMETER-VS-PHYSICS-OBJECTS.md` rule 5 forbids defaulting silently to either
side. MD-1's use of it is therefore evidence *for* SOLDERED-AD being live, not
evidence that it is right.

**Weakest reproducibility seam — and it is not in this artifact.** It is
`explorations/vz-evasion/vz-schur-complement-2026-06-23.md` §18.3, which states:

> "The pullback `s*(psi)` of a section `psi in Omega^1(Y^{14}) tensor S` via the
> section `s: X^4 -> Y^{14}` retains only the horizontal components … The
> pullback functor `s*` sends `psi` to its horizontal part."

graded **VERIFIED**, with "No approximation is made." By E2 that identity holds
**iff `d_mu g_ab = 0`** — the constant-coefficient / flat-section gauge, which
§18 elsewhere admits is the only gauge in which OQ3-V1 was computed. Control E4
fires on exactly this: `s^*` equals horizontal projection when `d_mu g = 0`, and
differs from it otherwise. The dependent sentence — "the normal RS components …
appear as scalar fields on `X^4` (one scalar per normal direction per spinor
component)" — is a KK **projection** statement, and it is doubly exposed: the
map is a contraction (WG-B06), and the normal directions are not Lorentz-inert
anyway (B11 vs control B12). This propagates to `canon/no-go-class-relative-map.md:401`
and five explorations. **MD-1 does not re-decide OQ3-V3** — the spinor sector has
its own index structure and the conclusion may well survive — but the stated
*reason* does not hold for a general section, and the grade "VERIFIED / no
approximation" overstates it. Flagged for the owner of the VZ chain; not
actioned here.

**Reproducibility seam inside MD-1.** The `30` is exhibited but its
`R`-irreducibility is **not** certified (the commutant computation is a
900-variable exact-rational system and was not run). Nothing in the result
depends on it: D3 is computed directly, not read off a lattice. Stated so that
no later reader treats G6 as a complete classification.

## 6. CLAIM CEILING AND EVERY IMPORTED ASSUMPTION

**Ceiling.** Kinematic and representation-theoretic. MD-1 types indices. It
computes no action, no kinetic term, no propagator, no mass, no quantization, no
source action; it decides no fork; it moves no claim, canon entry, grade,
ledger, or current-state surface.

Imported assumptions, each named because each is load-bearing somewhere:

1. **`Y14 = Met(X4)` with fibre `Sym^2(T*_x X4)`.** Repository-derived
   (`canon/shiab-existence-cl95.md`), source-supported, not re-derived here.
2. **`CARRIER-SPLIT` horn: Lorentzian `(3,1) + (6,4)`.** Declared, `status: open`.
   Cost of the other horn is small here: `(7,7)` and `(9,5)` **share the internal
   `Spin(6,4)`**, and every ad-leg result lives in that block. The horizontal
   `(3,1)` enters only A6/A7 and F2's index count.
3. **`VERTICAL-FROBENIUS-TRACE`: the vertical Frobenius-fibre horn,
   `lambda = 1/2`.** Declared; controls A4 and A5 show the parameter genuinely
   discriminates, so this is a choice, not a convention.
4. **The observation section is a metric section `s = g` and the reduction map is
   `s^*`.** Source-confirmed (`g3-weinstein-section-pullback-recheck`,
   `selected-k77-h640-*`), and `SECTION-VS-OBSERVERSE` is `status: open`.
5. **IMPORTED KK-STYLE STEP — declared.** §2's projection reading is used *only*
   to compute what the disavowed map would give, and every claim built on it is
   labelled "PROJECTION reading". It is not used for any conclusion about GU. To
   justify it one would need a declared Lorentz-inert internal space, which
   `Y14 = Met(X4)` is not.
6. **The physical local Lorentz group is `O(3,1)_g` acting on `T X4`, and it acts
   on the fibre by `Sym^2`.** This is forced once (1) is granted; it is the
   functoriality of `Met`. It is *not* an assumption about `P_H` — that is the
   fork.
7. **`SOLDERED-AD` is not assumed either way.** Both horns are reported.
8. **PV-2's identification of the nine as 6 leptoquarks + 2 `W_R` + 1 `Z'`** is
   taken from PV-2 and not re-derived. MD-1's ad-leg result is deliberately
   basis-independent so that it does not depend on this.

**Rule-4 compliance (no count from a multiplicity without an index/grade map).**
MD-1 asserts no new count. The one count it *uses* — the nine — is PV-2's, and
MD-1's conclusion about it is reached without indexing it, via D3 (a statement
about every subspace of `k`).

## 7. NEXT GATE

The decisive next gate is **not** more representation theory. It is a
source-and-formalization question: *does GU declare `P_H` to be soldered?*
Concretely — is the repo's `j_s: N -> ad(P_s)` (`gu-minimal-action-spec-2026-06-24.md:95`)
a canonical reduction of `P_H` along the frame bundle, or a chosen local
trivialization? A source reinspection plus a read of `docs/paper-formalization-candidates.md`
2A against the manuscript's definition of `H` would settle it, and it is cheap.

If SOLDERED-AD: the whole 4D particle-label layer of the program needs retyping,
starting with the SM's twelve, and PV/CU/MV are *superseded by scope*, not
refuted.

If INERT-AD: PV-1, PV-2, CU-1, MV-1 and MV-2 stand exactly as written, MV-1's
named assumption is discharged, and MD-1 reduces to a positive result — the form
leg is a vector, by contraction, and the KK worry is closed.

Selection stays inside this channel. No ledger, canon, current-state or public
surface moves.
