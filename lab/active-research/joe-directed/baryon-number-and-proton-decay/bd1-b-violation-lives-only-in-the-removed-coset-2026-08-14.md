---
artifact_type: exploration
status: exploration
doc_type: symmetry-protection-gate
created: 2026-08-14
work_item: BD-1
channel: baryon_number_proton_decay_and_matter_asymmetry
title: "BD-1: every baryon-number-violating direction of so(6,4) lies in the 24-dimensional coset p, and none in the maximal compact k. The observation reduction of PV-2 removes exactly the coset, so GU-as-declared has ZERO gauge-mediated proton decay and no GU-native parameter-free branching ratio to predict. Composing with MJ-5: B-L is exactly conserved by every mechanism GU-as-declared possesses -- gauge exchange, gauge-boson decay, BOTH sphaleron channels (SU(2)_L and the SU(2)_R that PV-2 leaves massless), gauge instantons, and every SM-preserving VEV -- so Sakharov condition 1 fails in the B-L channel and GU-as-declared predicts eta_B = 0. The same missing object, an SM singlet with B-L != 0, blocks the Majorana mass and baryogenesis alike."
grade: "EXACT. Integer Z[i] Clifford construction of so(10) on S+, exact integer root vectors, exact Fraction charges and anomaly coefficients, 86/86, exit 0, with a planted linear-surrogate control proving the gate can fail. NOT: a decay-rate or lifetime computation, a CP-violation or out-of-equilibrium analysis, a statement about spontaneous B-L breaking by a condensate, a quantization argument about the coset, a claim about SG4, or any claim-status movement."
disposition: ALL_24_B_VIOLATING_DIRECTIONS_LIE_IN_THE_REMOVED_COSET__ZERO_SURVIVE_IN_k__PROTON_DECAY_STRUCTURALLY_ABSENT_NOT_MERELY_UNCOMPUTED__B_MINUS_L_EXACT_UNDER_ALL_SIX_DECLARED_MECHANISMS__SAKHAROV_1_FAILS__CONDENSATE_ROUTE_AND_SG4_COMPLETION_UNTOUCHED
canon_verdict_change: none
steering_effect: unchanged
canonical_effect: pending_integration
depends_on:
  - lab/active-research/joe-directed/majorana-126-neutrino/mj2-no-native-126-carrier-2026-08-14.md
  - lab/active-research/joe-directed/majorana-126-neutrino/mj5-b-minus-l-exactly-preserved-2026-08-14.md
  - lab/active-research/joe-directed/photon-extra-vector-spectrum/pv2-observation-cannot-reach-the-extra-vectors-2026-08-14.md
  - explorations/conditional-build/cb-a-representation-content-2026-08-05.md
  - explorations/comparative-tensions-ledger-particle-qm-2026-07-21.md
  - explorations/parsimony-unexplained-joints-ledger-2026-07-21.md
  - lab/process/curt-iceberg-native-crosswalk.json
  - canon/gu-forces-field-space-declaration-RESULTS.md
scripts:
  - tests/channel-swings/joe_directed_baryon_gauge_bviolation_probe.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Its result binds only the
> named model and does not adjudicate Weinstein's source-native mechanism
> without a typed bridge. Read `lab/methods/source-native-comparator-routing.md`
> and follow its source-native pointers. Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

# BD-1 — baryon-number violation lives only in the directions observation removes

## 0. Prior art, swept by mechanism and attributed

Swept before computing, by mechanism rather than label, across `*.md`, `*.py`,
`*.yaml`, `*.json`, `*.lean`, `*.tex`.

**Zero hits, genuinely absent from the repository:** `baryon number violation`,
`baryon-number violation`, `sphaleron`, `B-L violation`, `X boson`,
`neutron oscillation`, `neutron-antineutron`, `qqql`, `gauge boson mediated`.

**Present, and attributed:**

| what exists | where | grade there | relation to BD-1 |
|---|---|---|---|
| GU is **SILENT** on proton decay: "GU commits to no GUT-scale breaking dynamics, so it predicts **no** proton-decay rate — neither refuted (like minimal SU(5)) nor confirmed. A coverage gap, not a win" | `explorations/comparative-tensions-ledger-particle-qm-2026-07-21.md` (row) | comparative ledger verdict | **BD-1 replaces the GROUNDS, keeps the verdict.** Silence is not "we did not compute the dynamics"; it is structural — the mediators are removed exactly by the declared observation mechanism |
| Row **E5**: the `(1,2,±1/2)` sits in the same 10 as `(3,1,−1/3)+(3̄,1,1/3)`; doublet–triplet splitting inherited in full, and *conditionally over-determined* — an exactly `so(10)`-invariant scalar mass would make them degenerate by Schur, "excluded by proton decay by ~13 orders of magnitude" | `explorations/conditional-build/cb-a-representation-content-2026-08-05.md` | conditional-build, named trigger | **Prior art on the SCALAR leptoquark channel.** BD-1 is the disjoint **gauge** channel and does not touch E5. Row E4 there (GU forced to ≥2 Higgs doublets) is used below |
| **CI-X04**: "The SU(3,2) real form is said to avoid classic proton-decay problems of older GUT choices." Directive: *"Require the selected representation, heavy mediators, baryon-number operators, and decay-amplitude calculation."* | `lab/process/curt-iceberg-native-crosswalk.json`, probe `tests/channel-swings/curt_iceberg_native_crosswalk_probe.py` | `CURT_REPORT_OF_AUTHOR_CLAIM` / `UNTESTED_PHENOMENOLOGY` | **BD-1 executes items 1–3 of that directive.** Item 4 is moot: there is no mediator to compute an amplitude for. See §5 for why this is *not* a verification of CI-X04 |
| Source p.30 credits Pati-Salam with not leading "immediately to proton decay like the original SU(5) model" | `lab/sources/source-claim-register.yaml` | newly-extracted, auxiliary | **The source's own remark is exactly what BD-1 computes**, in GU's specific setting. Credit for the physics is Pati–Salam (1974); credit for the remark is the source; BD-1 supplies the exact `so(6,4)` computation |
| Standard GUT statement of `X, Y`-mediated proton decay and the Super-K bound `> 10^34 yr` for `p → e⁺π⁰` | `lab/process/perspective-passes/01-foundational-math-lenses/07-representation-theorist.md` | imported textbook lens | Imported, not native. BD-1 cites it and derives nothing from it |
| **R1 constraint classes (proton decay, n-nbar) "staged"**, named for chain pruning, explicitly not part of the R0 sweep | `explorations/channel-swing-CH-SM-2026-07-19.md`, `lab/process/integration-readiness-scorecard.md` | staged, not computed | BD-1 is the first repository computation in that class |
| Matter–antimatter asymmetry graded **OUT-OF-SCOPE** for GU (row 9) | `explorations/parsimony-unexplained-joints-ledger-2026-07-21.md` | parsimony ledger | **BD-1 proposes a row change** (§7): from an asserted scope statement to a computed structural obstruction. *Not applied here* |
| `S4'` seesaw scale `1.3e16 GeV` → Hyper-K proton decay named as the weakest discriminant on the board, OOM-tier | `explorations/W141-steelman-sweep-observational-2026-07-14.md` | conditional-theorem register | Independent (issuance-declaration conditional). BD-1 does not use or move it |
| Finster Dirac-sea baryogenesis vs the GU Krein fork; 16/16 exact | `explorations/W245-finster-baryogenesis-krein-branch-collision-2026-07-26.md` | admissibility boundary | **Rival-theory mechanism, not GU-native.** Disjoint from BD-1 |
| Boyle–Turok C4: the asymmetry is produced by **standard thermal leptogenesis** from unstable `ν_R`; "nothing program-specific generates the asymmetry" | `lab/sources/claim-mining-boyle-turok-cpt-2026-08-03.md` | claim-mining, corrected | The comparison class for §6's escape E4 |
| "Sakharov" (17 files) | throughout `explorations/` | — | **Homonym.** Every hit is Sakharov/Jacobson *induced gravity*. The Sakharov *baryogenesis conditions* appear nowhere in the repository |
| "leptoquark" (3 files) | `explorations/geometry-curvature-emergence/pc5-higgs-su2l-u1y-gate-2026-06-23.md`; PV-2 and its probe | Pati-Salam bifundamental bookkeeping | PV-2's count of 6 is the direct input to BD-1; pc5 uses the word for `SU(4)` bookkeeping and computes nothing about `B` |

Nothing in BD-1 re-claims any of the above. The genuinely new content is isolated
in §5.

## 1. Preflight — six lenses, each proposing a route

Run inline before computing. Each lens had to name a *route*, not an opinion.

**L1 — GUT proton-decay phenomenologist.** *Route:* do not compute a lifetime.
Lifetimes need a mediator mass and GU declares no GUT scale, so any number is
imported. Compute instead **which so(6,4) directions can mediate `ΔB ≠ 0` at
all**, since that is mass-independent. Sharpest known discriminator in the
class: Pati–Salam leptoquarks (`|B−L| = 4/3`) mediate no proton decay, whereas
`SU(5)` `X,Y` (`|B−L| = 2/3`) do — because `X,Y` couple to a diquark current as
well as a leptoquark current. Test which kind GU keeps.

**L2 — effective-operator / dimension-six specialist.** *Route:* the criterion
is not "does the boson carry `B−L`" but "does the boson admit a **consistent
assignment of `B` and `L` separately**". Formalise as `|S(E)|`, the number of
distinct `(ΔB, ΔL)` pairs a root vector induces on the 16. `|S| = 1` ⟹ `B`,`L`
separately conserved; `|S| ≥ 2` ⟹ `ΔB = ±1` operators exist. Computable exactly
from matrix elements. **This lens supplied the deciding object.**

**L3 — baryogenesis / sphaleron cosmologist.** *Route:* Sakharov 1 is the cheap
kill. Sphalerons preserve `B−L` and destroy `B+L`; MJ-5 already says no
SM-preserving VEV carries `B−L`. So do not test `B` — test whether **anything**
in GU-as-declared can move `η_{B−L}` off zero: gauge exchange, boson decay,
instantons, VEVs. *Flag raised in preflight:* PV-2 leaves `W_R` massless, so
GU-as-declared has a **second** sphaleron channel the SM does not. Compute
`SU(2)_R`'s anomaly coefficients too — it could break the argument.

**L4 — group-theory branching specialist.** *Route:* work with **root vectors**,
never the real `M_ab` basis. A real `M_ab` is a sum of up to four root vectors
and would report spurious multi-valued `(ΔB, ΔL)`. Physical gauge bosons are
definite-weight. Also: the `k/p` block assignment is not a convention —
`dim su(3) = 8 > 6 = dim so(4)`, so colour is *forced* into the compact `so(6)`.

**L5 — experimental-limits specialist.** *Route:* if the surviving leptoquarks
are Pati–Salam type, the live bound is **not** Super-K but `K_L → μe`
(`M ≳ 10^3 TeV`), which is a lepton-flavour bound, not a baryon bound. Ask
whether any *parameter-free ratio* survives. Warned in advance: PS-leptoquark
ratios need the quark–lepton flavour rotation, which the repository grades open
— so expect **no** parameter-free ratio, and say so rather than manufacturing
one.

**L6 — honesty auditor.** *Route:* pre-register the three overclaims available
here. (i) "MJ-5 forbids proton decay" — **false**, dimension-six proton decay is
`B−L` preserving; make the probe assert this against itself. (ii) "GU predicts
no proton decay, a win" — the ledger already grades this a coverage gap; do not
upgrade it. (iii) "GU is falsified by `η_B`" — only if GU-as-declared is claimed
complete, and SG4 is open. Also: any test whose PASS is forced by its own shape
is worthless — plant a control.

### Cheapest kill-or-switch, recorded before computing

> **If any root vector inside `k` has `|S| ≥ 2`, target (b) is dead** — GU-as-declared
> would then have a surviving perturbative `B`-violating channel and the
> baryogenesis obstruction would collapse to a rate question. Cost: one matrix
> scan over 16 roots. Switch in that case: pivot entirely to target (a) and
> compute the surviving-sector branching structure.

### One credible contrary route, recorded before computing

> **The coset may not be gone.** PV-2 is explicit that it shows the 24 `p`
> directions carry the *opposite Killing signature*, **not** that they are
> successfully removed; disposal is a quantization question it declines to
> settle. If `p` returns, the `X,Y` mediators return and target (a) is alive.
> BD-1 must therefore compute the `p` sector too, and must state what survives
> in *both* branches.

## 2. What was computed

`tests/channel-swings/joe_directed_baryon_gauge_bviolation_probe.py`, **86/86,
exit 0**. Exact integer `Z[i]` Clifford construction of `so(10)` on `S+`
(Jordan–Wigner, same discipline as MJ-1/MJ-3), exact **integer** root vectors,
exact `Fraction` charges. Numpy is an integer array container only; no floating
point is load-bearing anywhere.

Conventions are MJ-5's, **re-validated on the 16 before use** (`ν_R` the unique
SM singlet at `B−L = −1`, `Q = 0`; 4 lepton and 12 quark states; charges in
`{0, ±1/3, ±2/3, ±1}`). Separate `B` and `L` are then *forced, not chosen*: a
colour-charged weight carries no lepton number, a colour-neutral weight carries
no baryon number, and `B − L` must reproduce the validated `B−L` on all 16
weights — asserted. The `k/p` split is re-derived twice independently: by the
spinor-side axis-block rule and by the vector-side Killing-form sign exactly as
PV-2 did, and the two are asserted equal.

**The deciding object** (lens L2), for a root vector `E_α`:

```
S(E) = { ( B(mu+alpha) - B(mu),  L(mu+alpha) - L(mu) )  :  <mu+alpha| E |mu> != 0 }
```

over the **actual nonzero matrix elements** on `S+` — not a minuscule-weight
argument. `|S| = 1` means the boson admits definite `(B, L)` and conserves both.
`|S| ≥ 2` means no assignment exists, `B` is genuinely violated, and the
current–current operator carries `ΔB = ±1`.

## 3. Result — the partition

> **`so(6,4)` has 40 root directions. Exactly 24 have `|S| ≥ 2`. All 24 lie in
> `p`. Exactly 0 lie in `k`. The `B`-violation partition and PV-2's `k/p`
> partition are the *same* partition of the 40 roots.**

| directions | count | `S` | mediates proton decay? | reached by the observation reduction? |
|---|---|---|---|---|
| gluons, `W_L`, `W_R` (in `k`) | 10 | `{(0,0)}` | no | no |
| **leptoquarks (in `k`)** | **6** | `{(∓1/3, ±1)}`, `\|Δ(B−L)\| = 4/3` | **no** | **no** |
| **coset `p`** | **24** | `{(±1/3,±1), (∓2/3,0)}`, `\|Δ(B−L)\| = 2/3` | **yes** | **yes** |

The complete list of colour-charged non-SM gauge directions in `so(6,4)`,
certified rather than asserted:

- in `k`, surviving: **`(3,1)_{±2/3}`**, 6 states — weak **singlets**;
- in `p`, removed: **`(3,2)_{±5/6}`**, 12 states (the `SU(5)` `X,Y` multiplet)
  and **`(3,2)_{±1/6}`**, 12 states (the `(3,2)` components of the `10 + 10bar`
  of `SU(5)` inside the 45).

**There is no third mediator anywhere in the algebra.** The structural reason
the split falls where it does is visible in that list and is asserted: every
removed direction is a weak **doublet** (`|ΔT3L| = 1/2`, 24/24), and only a weak
doublet can connect the `SU(2)_L` doublet `q_L` to the `SU(2)_L` singlets
`u^c, d^c` — that connection *is* the diquark current. The surviving leptoquarks
are weak singlets and have no such connection available.

Dimension-six operators from single-boson exchange:

- **`k` exchange generates only `(ΔB, ΔL) = (0,0)`.** The surviving sector
  produces **no** dimension-six baryon-number-violating operator at all.
- `p` exchange generates `(0,0)` and `(±1, ±1)` — the standard `qqql` operators.
- **Every** dimension-six operator from gauge exchange anywhere in `so(10)`,
  `p` included, satisfies `ΔB − ΔL = 0`. Asserted, with a companion assertion
  that `(ΔB, ΔL) = (1,1)` *is* in the `p` set — i.e. the probe asserts against
  the overclaim that MJ-5's `B−L` result forbids proton decay. **It does not.
  Proton decay is `B−L` preserving.**

The mechanism, stated once: `B−L` is **linear** in the weight, so every root has
a single `Δ(B−L)` — asserted on all 40. `B` and `L` separately are **piecewise**
(they depend on whether the weight is colour-neutral), which is the only reason
`B` can be violated at all. Also asserted.

Both of GU's bosonic fields carry the same adjoint index, so the partition
transfers unchanged: neither `ε` (`Ω⁰ ⊗ ad`) nor `$` (`Ω¹ ⊗ ad`) can generate a
`B`-violating operator from a `k` direction, and (recomputed here, 450 weights)
neither contains an SM-singlet direction with `B−L ≠ 0`.

## 4. Result — the baryogenesis obstruction

Non-perturbative violation, from exact anomaly coefficients
`A[G² U(1)_q] = Σ_{16} q(w)·T(w)²`:

| gauge factor | `A[B]` | `A[L]` | `A[B−L]` | `A[B+L]` |
|---|---|---|---|---|
| `SU(2)_L` | `1/2` | `1/2` | **0** | `1` |
| **`SU(2)_R`** (survives per PV-2) | `−1/2` | `−1/2` | **0** | `−1` |
| `SU(3)_c` | `0` | `0` | 0 | 0 |
| `SU(4)_c` | content self-conjugate | — | **0** | — |

Lens L3's flag resolves the *safe* way: the extra sphaleron channel
GU-as-declared retains — because PV-2 leaves `W_R` massless — has `A[B] = A[L]`
as well. **GU-as-declared has two `B+L` washout channels and still zero `B−L`
sources.** The obstruction gets stronger, not weaker.

Composed over every mechanism GU-as-declared possesses, each checked:

| mechanism | can it move `η_{B−L}`? |
|---|---|
| gauge exchange (perturbative) | no — `ΔB − ΔL = 0` on all 40 roots |
| gauge-boson decay | no — `Δ(B−L)` single-valued on all 40 roots |
| sphaleron, `SU(2)_L` | no — `A[B] = A[L]` |
| sphaleron, `SU(2)_R` | no — `A[B] = A[L]` |
| instantons, `SU(3)_c` / `SU(4)_c` | no |
| SM-preserving VEV in declared content | no — MJ-5, re-derived here: profile `[0,0,0,0,0,2]` |

> **`B−L` is exactly conserved in GU-as-declared by every mechanism it has, and
> `B` itself is conserved perturbatively. The only baryon-number violation
> anywhere in the theory is the `B+L` violation of sphalerons, which preserves
> `B−L`.**
>
> **Sakharov condition 1 therefore fails in the `B−L` channel. With
> `η_{B−L} = 0` and sphalerons in equilibrium, `η_B = 0`. GU-as-declared
> predicts zero matter–antimatter asymmetry.**

And the two channels close on the same missing object:

> **The single representation that would repair the `ν_R` Majorana mass
> (MJ-2/MJ-5) and baryogenesis (BD-1) is the same one: an SM singlet with
> `B−L ≠ 0`, which occurs in no `Λ^k(10)` except `k = 5` — the 126.**

## 5. Standard GUT arithmetic vs GU-native content

**Standard, imported, and credited — none of it new here:** Pati–Salam
leptoquarks mediate no proton decay (Pati–Salam 1974); `SU(5)`/`SO(10)` `X,Y`
do, and all dimension-six `B`-violating operators conserve `B−L` (Weinberg 1979;
Wilczek–Zee 1979); sphalerons violate `B+L` and conserve `B−L`
('t Hooft 1976; Kuzmin–Rubakov–Shaposhnikov 1985); minimal `SU(5)` baryogenesis
fails because it produces `B−L = 0`, which sphalerons wash out; leptogenesis
requires `B−L` violation from `ν_R` Majorana masses (Fukugita–Yanagida 1986);
`B = a·(B−L)` in equilibrium with `a > 0` (Harvey–Turner 1990) — **cited, not
computed here**, and the conclusion `η_{B−L} = 0 ⟹ η_B = 0` rests on it.
Row E4 of `cb-a` forces GU to at least two Higgs doublets, which changes `a`
but not its sign.

**GU-native, and the actual deliverable:**

1. The `B`-violation partition of `so(6,4)` **coincides exactly** with PV-2's
   `k/p` partition — 24 and 0, not "mostly". That coincidence is a fact about
   GU's declared observation mechanism, not about `SO(10)`.
2. GU-as-declared's surviving non-SM sector (6 leptoquarks + 2 `W_R` + 1 `Z'`)
   contains **zero** `B`-violating directions, so proton decay is *structurally
   absent*, not merely uncomputed.
3. The `SU(2)_R` sphaleron channel that GU-as-declared uniquely retains still
   has `A[B] = A[L]`.
4. The six-mechanism composition giving `η_B = 0` for GU-as-declared.
5. The identification of one missing representation behind two failed sectors.

**On CI-X04.** Curt reports the author as claiming the real form avoids classic
proton-decay problems. BD-1 exhibits an exact mechanism by which a real-form
reduction does precisely that. This is **not** a verification of CI-X04: the
reported object is `SU(3,2)`, the computed object is `so(6,4)`, and identifying
them would be a Layer-0 error of exactly the kind
`GEOMETER-VS-PHYSICS-OBJECTS.md` exists to prevent. CI-X04 stays
`UNTESTED_PHENOMENOLOGY`. What BD-1 adds is the price tag: in GU-as-declared the
same reduction that removes proton decay also removes the theory's ability to
make matter.

## 6. Hostile review of this swing

**Strongest overclaim available, and refused.** "GU predicts no proton decay —
a prediction minimal `SU(5)` got wrong and GU gets right." Refused. The
comparative ledger already grades this SILENT and calls it a coverage gap, not a
win; a theory that forbids the signal makes no risky prediction. Worse, BD-1
shows the same structure that buys the "success" costs the matter asymmetry.
The honest reading is a **net loss of coverage**, not a win.

**Second overclaim, pre-registered by L6 and asserted against inside the probe.**
"MJ-5 shows `B−L` is exact, therefore proton decay is forbidden." False.
Dimension-six proton decay is `B−L` preserving; the probe asserts
`(ΔB, ΔL) = (1,1) ∈ p_ops` so this mistyping cannot pass unnoticed.

**Strongest contrary construction.** *Undo the observation reduction.* PV-2 is
explicit that it did **not** show the coset is disposed of. If `p` returns:
proton decay returns, target (a) becomes live — **and the baryogenesis
obstruction survives untouched**, because every `p` operator still has
`ΔB − ΔL = 0`. Asserted in the probe. The result is therefore robust to the
largest open question upstream of it. That robustness is the strongest thing
BD-1 has.

**Strongest available mistyping.** Reading `|S(E)| = 1` as "`B` is a symmetry of
`k`". It is not: the leptoquark generator does not commute with `B` as an
operator on the 16. The correct statement is narrower — a **consistent
`(B, L)` charge assignment to the boson exists**, so `B` and `L` are separately
conserved in every process that boson mediates. The obstruction is about
processes, not about a Lie-algebra commutant, and the artifact says so.

**Weakest reproducibility / propagation seam.** The step from "`η_{B−L} = 0`" to
"`η_B = 0`" is **imported** (Harvey–Turner equilibrium). It is not computed here
and its coefficient is not re-derived. If a completion put sphalerons out of
equilibrium at the relevant epoch, or introduced a conserved charge not in the
list, the last step would need redoing. Everything up to and including
"`η_{B−L}` cannot move off zero" is exact and native; the final sentence is not.
Second seam: `A[B] = A[L]` is computed for **one** generation and scales
linearly; three-generation flavour structure is not modelled, and does not need
to be for this conclusion, but the artifact should not be cited for anything
flavour-dependent.

**Non-vacuity.** A planted control is built into the probe: replacing the true
piecewise `B` with a **linear surrogate** (`B := −(B−L)` everywhere) collapses
the result to *zero* `B`-violating directions and destroys the dimension-six
finding. The 24/0 split is produced by the physics, not by the shape of the
test.

## 7. Classification, in target-native vocabulary

| object tested | verdict |
|---|---|
| **Target (a): a GU-native parameter-free proton-decay branching ratio** | **ROUTE KILLED.** Not "hard" — *absent*. The mediators are exactly the 24 coset directions; zero survive. In the contrary branch where the coset returns, the mediators are exactly the textbook `SU(5)` `X,Y` and `SO(10)` `X'` multiplets with textbook ratios and no GU-native content. There is no third mediator in the algebra |
| **Candidate: the 6 surviving leptoquarks as a proton-decay source** | **CANDIDATE KILLED**, exactly. `S = {(∓1/3, ±1)}`, single-valued; `ΔB = 0` from every exchange |
| **Target (b): baryogenesis in GU-as-declared** | **ROUTE KILLED for GU-as-declared.** No mechanism can move `η_{B−L}` off zero. Ceiling below |
| **`ΔB ≠ 0` from `ε` or `$` in the surviving sector** | **CANDIDATE KILLED**; the classification is a property of the adjoint index and transfers |
| **Spontaneous `B−L` breaking by a `⟨νν⟩` condensate** | **NOT-YET-FALSIFIED and live.** The `ν_R ⊗ ν_R` bilinear weight *is* one of the two `Λ⁵` SM singlets with `B−L ≠ 0` — exhibited in the probe, not merely mentioned. MJ-3's nonzero `F[45][126] = −5/32` keeps the four-fermion channel open. **This is the decisive gate** |
| **Disposal of the 24 coset directions** | **TYPE-MISSING.** A quantization question about the physical state space (PV-2's PV-3), not a group-theoretic one. BD-1 computes both branches and does not decide it |
| **CI-X04 (real form avoids proton decay)** | **NOT-YET-FALSIFIED**, unchanged grade. A candidate exact mechanism now exists for a *different* group; identification would be a Layer-0 error |
| **Sakharov conditions 2 (CP) and 3 (out-of-equilibrium)** | **SOURCE-SILENT.** Not tested. Condition 1 fails first, so they are not reached |
| **Proposed ledger row changes** (recorded, **not applied**) | `parsimony-unexplained-joints-ledger` row 9 `matter-antimatter asymmetry`: **OUT-OF-SCOPE → STRUCTURALLY OBSTRUCTED (computed)**. `comparative-tensions-ledger-particle-qm` proton-decay row: verdict **SILENT unchanged**, grounds replaced by the exact structural statement. Both require independent verification before any ledger moves |

## 8. Claim ceiling

This is a statement about **GU-as-declared** — candidate 2B field content, with
`canon/gu-forces-field-space-declaration-RESULTS.md` establishing SG4 as the
open decider. It is **not** a statement about GU-as-completed and **not** a
falsification of GU.

Specifically, BD-1 does **not** establish: that a `⟨νν⟩` condensate is
impossible (spontaneous `B−L` breaking is untouched, exactly as MJ-5 recorded);
that no SG4 completion can declare a field carrying an SM singlet with
`B−L ≠ 0`; that a primordial `B−L` asymmetry cannot be imposed as an initial
condition (nothing here forbids it — it would be an unexplained input, the
parsimony ledger's `BRUTE` grade, and inflation would dilute it); that the
Boyle–Turok-class global CPT-mirror reading is excluded; any decay rate,
lifetime, or cross-section; anything about CP violation or departure from
equilibrium; or that the coset is or is not consistently removable.

What it does establish is exact and narrow: **within the declared field content
and the declared observation mechanism, the set of directions that can violate
baryon number is precisely the set observation removes, and no mechanism present
can produce a `B−L` asymmetry.**

## 9. Next in-channel gate

**BD-2 — the condensate.** Everything above is conditional on the one route MJ-5
kept alive and BD-1 exhibits: a `⟨νν⟩` condensate in the 126 channel breaking
`B−L` spontaneously. If it forms, `B−L` is broken, `ν_R` gets a Majorana mass,
leptogenesis is available, and **both** obstructions lift at once. If it cannot
form, both obstructions are permanent for GU-as-declared and the theory needs
SG4 to declare a new field. It is the same gate for channel 3 and channel 4 —
the two channels have converged on one decision, and BD-2 should be run once,
not twice.

The input is already banked: MJ-3's exact `F[45][126] = −5/32` gives the
four-fermion coefficient in the right pairing channel. What is missing is a
condensation criterion, which is a dynamical question the repository has not yet
typed. That typing, not more representation theory, is the bottleneck.

Selection stays inside this channel. Repository-wide GU priority is unchanged,
the superposition / source-residual workstream is untouched, and no ledger,
canon, or current-state surface moves.
