---
title: "Prong B no-go: equivariance + Krein do NOT single out a domain — the boundary selector is a POSITIVE-DIMENSIONAL moduli, so it is PROVABLY EXTERNAL to current GU structure"
status: active_research
doc_type: exploration
created: 2026-07-21
directed_by: "Joe direct chat, 2026-07-21 (SOURCE-DOMAIN-SELECTOR swing, Prong B execution)"
prereg: explorations/prereg-source-domain-selector-swing-2026-07-21.md
inputs:
  - explorations/source-domain-selector-prongA-extraction-2026-07-21.md
  - explorations/continuum-pencil-graph-domain-certificate-2026-07-20.md
  - explorations/continuum-pencil-domain-gate-2026-07-20.md
  - canon/source-action-seiberg-witten-construction.md
portfolio_item: OPERATOR-END-PENCIL (Lane 1) + serves B5-MIDDLE-DIFFERENTIAL + touches CONSTRUCTION-SPACE L7
outcome: B-MULTIPLICITY
probe: tests/channel-swings/source_domain_selector_prongB_probe.py (foreground, EXIT 0)
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_actions: none
kill_conditions_declared_before_computation: true
---

# Prong B no-go: the domain selector is a positive-dimensional moduli

> **CORRECTION BANNER (2026-07-21, hostile verification — original preserved
> below, unedited):** The headline `B-MULTIPLICITY` is **DEMOTED to
> collar-conditional**. Hostile verify
> (`source-domain-selector-prongB-hostile-verify-2026-07-21.md`, HV-WEAKEN,
> probe EXIT 0) found the whole computation lives on a **compact collar**, where
> a first-order `d×d` system has deficiency `(d,d)` and full `U(d)`
> **automatically** — the multiplicity is manufactured by compactness *before
> any GU structure is used*. On the true **noncompact** fiber the moduli
> dimension is set by the **limit-point / limit-circle classification at the
> fiber ends**, which is a function of the end-asymptotics of `B, W~` — i.e.
> exactly the `D2` datum Prong A logged `SOURCE-SILENT`. The **default** for a
> non-degenerate Dirac-type end is **limit-point → essentially self-adjoint →
> UNIQUE domain** (no `θ`, no moduli); multiplicity requires the coefficient to
> **degenerate** at the end. So the specific claims below — `T^2`, dim 2, the
> `U(1)` floor, the "continuum of distinct spectra" — **do not transfer**, and
> the modality "*provably* external / structurally impossible to single out" is
> **false in the limit-point horn**. WHAT SURVIVES: an external datum must still
> be imported *either way*, because the LP/LC classification (`D2`) that decides
> whether any freedom exists is itself source-silent — but the correctly-typed
> missing datum is the **fiber-end limit-classification (D2)**, UPSTREAM of the
> boundary phase, and the phase selector is needed only in the limit-circle
> horn. The `sigma/theta/tau` decision tree's Q1 is re-shaped accordingly.

Adversarial truth-test, not advocacy. Prong A returned **S-SILENT-OPEN**: the
Weinstein primary corpus specifies no construction-grade, `z,δ`-independent
boundary/domain selector. Prong B asks the correctly-framed structural question
and it is **not** "prove no domain exists" — the certificate
(`continuum-pencil-graph-domain-certificate-2026-07-20.md`) already shows *many*
compact-collar Krein-self-adjoint graph domains exist. The honest no-go is a
**non-uniqueness / multiplicity theorem**:

> GU's existing structure alone — the first-order operator
> `A~ = B(s)∂_s + W~(s)` with `B = -i K_u(s) G`, the constant Krein involution
> `J = J* = J^{-1}` / the `(9,5)` form, and the `Z/2` deck action (with the
> implementation sequence `1 → Sp(1)_comm → G → Z/2_deck → 1`) — does **not**
> single out a unique physical maximal-isotropic (Krein-self-adjoint) domain.
> The space of deck-equivariant Krein-self-adjoint domains has **more than one
> physically-inequivalent point**.

**Adjudicated outcome: `B-MULTIPLICITY` (⇒ `S-OBSTRUCTED`).** The missing
boundary selector is *provably external* to current GU structure — a
theorem-grade localization of the gap, not merely an unfound datum.

## 1. Boundary-form setup (the moduli is a Lagrangian Grassmannian)

On a compact collar `I = [a,b]` the first-order expression
`A~ = B(s)∂_s + W~(s)`, `B = -i K_u(s) G`, carries the Green boundary form
(certificate §1)

```
h_b(u(b),v(b)) − h_a(u(a),v(a)),   h_s(x,y) = x* H(s) y,   H(s) = -i B(s)* J = G K_u(s) J,
```

with `H(s)` Hermitian and invertible. Because `S(s)* H(s) S(s) = H(a)` (the
transport of certificate §4), `H(a)` and `H(b)` are congruent, hence share one
signature `(p,q)`, `p+q = d`. On the boundary-data space `C^d ⊕ C^d` the form

```
Ω((u_a,u_b),(v_a,v_b)) = u_b* H(b) u_b − u_a* H(a) u_a
```

has signature `(q,p) ⊕ (p,q) = (d,d)`: it is a **split (neutral) Hermitian
form**. Krein-self-adjoint realizations ↔ **maximal-isotropic (Lagrangian)
subspaces** of `Ω`. For a split Hermitian form of signature `(d,d)` the
Lagrangian Grassmannian is

```
Λ(d,d) ≅ U(d)     (real dimension d²),
```

and the graph-domain chart `D_T = { u : u(b) = T u(a) }` is the dense open cell
where `T* H(b) T = H(a)` (certificate eq. (G)); its solution set is a torsor
over the pseudo-unitary group `U(p,q)`, also real dimension `d²`. The phase
`θ` of `T_θ = e^{iθ} S(b)` is the `U(1)` center of this `U(d)` — **one** of
`d²` unfixed directions, the one Prong A pinned as source-silent.

So *before* any group constraint the domain moduli is `d²`-dimensional. The
whole question is whether the **two** structural constraints GU actually owns —
(i) Krein-self-adjointness w.r.t. `J`, (ii) deck-equivariance — cut this to a
single point.

Constraint (i) is already used: it is what makes the subspace isotropic (it
*defines* `U(d)`, it does not shrink it further). So the entire burden of
uniqueness falls on constraint (ii), deck-equivariance. Everything below is the
honest evaluation of exactly how much (ii) can remove.

## 2. Faithful finite toy (d=2, balanced `(1,1)`, a `Z/2` deck)

Deterministic realization (probe
`tests/channel-swings/source_domain_selector_prongB_probe.py`, foreground,
**EXIT 0**), built to satisfy the frozen algebra rather than assert it:

| object | value | role |
|---|---|---|
| `G` | `σ_z` | involution (plays `G_col`), `G²=I` |
| `K_u` | `σ_x` | Hermitian involution (section-theory `K_u`) |
| `B = -i K_u G` | `-σ_y` | principal coefficient, invertible |
| `J` | `σ_x` | constant Krein involution, `J*=J=J^{-1}` |
| `H = -i B* J` | `σ_z` | endpoint form, Hermitian, **signature `(1,1)`** |

All frozen relations verified numerically: `B = -iK_uG`, `J*=J=J^{-1}`, the
principal Krein symmetry `B*J = -J B`, and `H = -iB*J` Hermitian invertible of
balanced signature `(1,1)` — the cross-chirality pattern of GU's own Krein form
`K = η_V ⊗ β_S`, signature `(+96,−96,0)` (`canon/source-action-...:35`).

The `Z/2` deck is realized by the form-preserving involution `U = σ_z` (`U²=I`,
`U*HU = H`): the chirality/sector **grading**, i.e. a deck that labels sectors
rather than mixing them. Single-collar deck-equivariance of the boundary
condition is `U T U^{-1} = T`, i.e. `[T,U] = 0` (the family condition
`T_{t+1} = U_b T_t U_a^{-1}` with one deck acting equally at both un-exchanged
ends — certificate §4).

## 3. Toy enumeration: the admissible set is a 2-torus (moduli dim = 2)

With `H = σ_z` and deck `U = σ_z`, a graph domain is admissible iff

```
T* σ_z T = σ_z      (Krein-isotropy)      AND      [T, σ_z] = 0   (deck-equivariance).
```

`[T,σ_z]=0` forces `T` diagonal, `T = diag(t_1,t_2)`; isotropy then gives
`|t_1| = |t_2| = 1`. Hence

```
{ admissible deck-equivariant Krein-self-adjoint domains } = { diag(e^{iα}, e^{iβ}) }
                                                           = U(1) × U(1) = T²,
```

a **2-real-dimensional torus** — emphatically not a point. The probe admits all
`24×24 = 576` sampled torus points, and as **controls** it exhibits (a) 200
generic non-diagonal `H`-unitary domains that *exist* (Krein-self-adjoint) but
are correctly **deck-excluded**, and (b) 200 generic non-isotropic matrices
correctly **rejected**. The constraints therefore have discriminating power:
they cut `U(2)` (dim 4) down to `T²` (dim 2) and no further.

**Moduli count: total deck-equivariant Krein-self-adjoint domain moduli = `T²`,
real dimension 2.** (General `d`: the admissible set is the maximal torus of the
commutant of the deck action inside `U(d)` — dimension = number of independent
sectors the deck grades, always `≥ 1`.)

## 4. Physical-inequivalence check (the main adversarial self-check)

Multiplicity of *domains* is worthless if the extra domains are gauge/deck
images of one another. The decisive test: **distinct spectrum ⇒ physically
inequivalent**, because every gauge/deck symmetry is isospectral, so different
spectra rule out *all* symmetry relations at once (including the deck itself).

For `A~ = B ∂_s` (`W~ = 0`) on `[0,L]`, `B = -σ_y`, the eigenvalues of the
realization `A~_T` solve `det(exp(λ B^{-1} L) − T) = 0`. For
`T = diag(e^{iα}, e^{iβ})` this collapses (derived, then verified numerically at
5/5 sample phases) to the closed form

```
cosh(λ L) = cos((α+β)/2) / cos((α−β)/2)  =:  ρ(α,β).
```

The spectrum is fixed by the single real invariant `ρ`. Two observations make
the inequivalence rigorous:

1. **`ρ` sweeps a continuum of distinct values.** Along the slice with the
   relative phase *fixed* at `α−β = 0.6 ≠ 0` (so **not** the global-phase
   `U(1)` center) and the sum varying, `ρ = cos(t)/cos(0.3)` is injective: the
   probe finds 40/40 distinct values. Distinct `ρ` ⇒ distinct spectra ⇒
   pairwise physically inequivalent. The physically-inequivalent sub-moduli is
   therefore **at least 1-dimensional** — a continuum, not a finite gauge
   ambiguity.
2. **The deck cannot be the culprit.** `U = σ_z` *fixes* every diagonal `T`
   (`U T U^{-1} = T`), so the `T²` family is manifestly **not** a single deck
   orbit; the deck relates none of its distinct points. And because the
   discriminator is spectrum, no *other* symmetry (any `M` commuting with `A~`,
   Krein-unitary, deck-commuting) can relate two different-`ρ` domains either.

**Physical-inequivalence verdict: CONFIRMED.** The deck-equivariant
Krein-self-adjoint domains contain a continuum of pairwise physically
inequivalent points; ≥ 2 (indeed ∞-many) survive the gauge/deck quotient. This
is genuine multiplicity, not a symmetry artifact.

## 5. Uniqueness steelman (planted control) — and why it FAILS

Planted claim, steelmanned hard: *"equivariance + Krein force a unique domain."*
The strongest case for uniqueness is to make the implementation group act as
large as possible. Push it to the limit — an **irreducible** action of `G` on
the boundary fiber `C^d`. Then, by Schur, the commutant is `C·I`, and
deck-/group-equivariance forces `T` to commute with *every* generator, so

```
T = c·I   (scalar).
```

This is the best possible collapse. Yet Krein-isotropy of a scalar,
`(c̄c) H = H`, imposes only `|c| = 1`. Hence

```
{ equivariant Krein-self-adjoint domains, irreducible action } = { e^{iθ} I } = U(1),
```

a **1-dimensional circle — still not a point.** The probe confirms it: with
generators `{σ_z, σ_x}` (irreducible, commutant `= C·I`), all 32 sampled phases
give admissible scalar domains, non-unit-modulus scalars are rejected
(`|c|≠1` breaks isotropy), and generic non-scalars are excluded. The residual
`U(1)` is *exactly* the certificate's unfixed phase `θ` in `T_θ = e^{iθ} S(b)`.

**Steelman result: uniqueness fails even in the most favorable case.** The
`U(1)` center is unremovable by isotropy, because scalars are always in the
commutant and isotropy only bounds their modulus. To cut the `U(1)` you must
break the phase — which requires an **external** reference (a boundary
holonomy, a variational/reality condition, or a source-fixed phase): precisely
the datum Prong A found `SOURCE-SILENT`, and precisely what the certificate §4
says "the sources provide no ... reference that fixes."

This yields a sharp dichotomy, independent of the toy:

| implementation-group action on the fiber | deck-equivariant Krein domain moduli |
|---|---|
| **irreducible** (commutant `= C·I`) — best case for uniqueness | `U(1)` (dim 1) — the phase `θ` |
| **reducible** (commutant `⊋ C·I`) — GU's actual cross-chirality/multi-sector case | torus of dim = #sectors `≥ 2` (toy: `T²`) |

In **neither** column is the moduli a point. Uniqueness from equivariance +
Krein alone is *structurally impossible*: the floor is always the `U(1)`
θ-phase, and GU's reducible cross-chirality structure only enlarges it.

## 6. Why GU sits in the reducible column (not the collapsing one)

The `B-FORCED` surprise-win would need GU's structure to (a) act irreducibly and
(b) somehow break the residual `U(1)`. (b) is impossible from equivariance+Krein
(§5), and (a) is not what GU has: the Krein form is *purely cross-chirality*
`(+96,−96,0)` with chirality persisting as a sector label (`E_±` each rank 64,
`canon/source-action-...:30,35`); the commutant contains at least the chirality
grading, so the action is **reducible**. Moreover, Prong A established the
sources do not even fix the deck's fiber representation. So GU is firmly in the
reducible row: moduli dimension `≥ 2` structurally, `= 2` in the faithful toy.

## 7. Adjudicated outcome and what it pins

**`B-MULTIPLICITY` ⇒ `S-OBSTRUCTED`.**

- **Moduli count / dimension.** Deck-equivariant Krein-self-adjoint domains form
  a positive-dimensional family: `T²` (real dim **2**) in the faithful `(1,1)`
  toy; structurally `≥ 1` always (the irreducible-case floor `U(1) = θ`),
  `≥ 2` for GU's reducible cross-chirality structure.
- **Physical inequivalence: CONFIRMED** — a continuum of pairwise distinct
  spectra (invariant `ρ`), with the deck shown to fix rather than relate the
  family. The physically-inequivalent sub-moduli is `≥ 1`-dimensional.
- **Uniqueness steelman: FAILS** — even an irreducible action leaves a `U(1)`
  (the phase `θ`); isotropy cannot bound a scalar's phase, only its modulus.

Therefore the missing boundary selector is **provably external** to current GU
structure. `OPERATOR-END-PENCIL` and `B5-MIDDLE-DIFFERENTIAL` are **conditional
on an imported selector as a theorem, not as an unfinished search**: no
refinement of the operator, the Krein form, or the deck action can single out
the domain, because a positive-dimensional space of physically-inequivalent
admissible domains provably remains. This upgrades `DOMAIN-OBSTRUCTION-SOURCE`
from "not yet found" to "cannot be found inside the present structure."

### The exact external datum (unchanged from Prong A, now theorem-pinned)

A construction-grade, `z`- and `δ`-independent choice that **breaks the residual
`U(1)` phase and (in the reducible case) the inter-sector torus** — a boundary
holonomy / endpoint phase, a variational or reality condition, or a
source-fixed `T` — tying the `(9,5)` Krein form to a single deck-equivariant
Krein-self-adjoint domain. Reopen trigger: any source or first-principles
relation that fixes this phase datum (e.g. a released two-connection on-shell
`D²` with a boundary reality condition).

## 8. Forbidden-shortcut self-audit

- No claim that "no domain exists" — the opposite is proved (a `T²` of them).
- The Hermitian central-difference inverse was **not** treated as a continuum
  Dirichlet resolvent; the toy is a genuine first-order graph realization.
- The Dirichlet-domain exclusion was **not** inflated into a native no-go; the
  no-go here is multiplicity, on the Krein-native lane.
- No gauge/deck-related domains counted as inequivalent — inequivalence is
  certified by *distinct spectra*, and the deck is shown to fix the family.
- Uniqueness was genuinely attempted (steelman, §5) before concluding
  multiplicity; multiplicity was not declared without the physical-inequivalence
  check (§4).
- No claim, canon verdict, paper status, ledger, or public posture moved.

## 9. Handoff

Per the pre-registration, `S-OBSTRUCTED` demotes the shared claim of both papers
to **conditional-forever-without-import** and names the exact missing datum
(§7). Route the missing-datum demand to **P2C** (native-vs-forced owner) as a
frozen packet with §7 as its reopen condition. Both papers should carry the
selector as a typed *import*, counted, never hidden — the honest ceiling is now
a theorem-grade localization, not a null.

## Boundary

Only this artifact and its probe
(`tests/channel-swings/source_domain_selector_prongB_probe.py`, foreground,
EXIT 0) were written; GU is otherwise read-only. No commit, no push, no edit to
LANE-STATE / research-portfolio / NEXT-STEPS or any claim / canon / verdict /
ledger file. No claim status, canon verdict, or public posture changes.
