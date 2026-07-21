---
title: "Hostile verify of Prong B: the T^2/dim-2 multiplicity is a COMPACT-COLLAR artifact; on the noncompact fiber the moduli dimension is set by the limit-point/limit-circle classification, which is itself the source-silent D2 datum — S-OBSTRUCTED survives only in a weakened, contingent form"
status: active_research
doc_type: exploration
created: 2026-07-21
verifies: explorations/source-domain-selector-prongB-nogo-2026-07-21.md
inputs:
  - explorations/source-domain-selector-prongB-nogo-2026-07-21.md
  - explorations/source-domain-selector-prongA-extraction-2026-07-21.md
  - explorations/continuum-pencil-graph-domain-certificate-2026-07-20.md
probe: tests/channel-swings/source_domain_selector_prongB_hostile_verify_probe.py (foreground, EXIT 0)
outcome: HV-WEAKEN
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_actions: none
---

# Hostile verify of Prong B: the multiplicity is a compact-collar artifact

Adversarial refutation pass, not confirmation. Default posture: skeptical. The
target is `source-domain-selector-prongB-nogo-2026-07-21.md`, outcome
`B-MULTIPLICITY`, which claims that deck-equivariance + Krein do **not** single
out a domain, that the deck-equivariant Krein-self-adjoint domain moduli is a
2-torus `T^2` (real dim 2) with an irreducible-case floor `U(1)`, and that the
missing boundary selector is therefore **provably external** to current GU
structure (`S-OBSTRUCTED`, "cannot be found inside the present structure").

**Verdict: `HV-WEAKEN`.** The core "an external datum must be imported to pin
the domain" survives — but only in a **weakened, contingent** form. Prong B's
load-bearing quantitative claims (`T^2`, dim 2, the `U(1)` floor, the
"continuum of distinct spectra") are **compact-collar artifacts that do not
transfer** to the true noncompact fiber, and its headline modality — "a
positive-dimensional multiplicity **provably** remains / is **structurally
impossible** to single out" — is **false in the limit-point horn**, which is
the *default* for a non-degenerate Dirac-type end. The honest corrected claim is
stated in §6.

## 0. Where the whole computation lives (the setup flaw)

Prong B computes on a **compact collar** `I=[a,b]` (its §1, its probe). The
certificate it builds on says outright that "the compact collar itself is only
a surrogate for the noncompact fiber" (`continuum-pencil-graph-domain-
certificate-2026-07-20.md:30,220`). On a **compact interval** a regular
first-order `d×d` system has deficiency `(d,d)` **automatically**: every `H^1`
solution is square-integrable on a finite interval, so the boundary-data space
is the full `C^d ⊕ C^d` and the maximal-isotropic set is the full `U(d)`. Prong
B's `U(2)` → `T^2` chain is then just "full `U(d)` ∩ deck-commutant." The
multiplicity is **manufactured by compactness before any GU structure is used.**

Prong B never performs the noncompact transfer. Its §6 "GU is reducible ⇒ dim
≥ 2" argument is about the deck-commutant *inside the collar's automatic `U(d)`*;
it silently assumes the noncompact fiber inherits that full `U(d)` of boundary
freedom. That silent assumption is exactly what the primary attack breaks.

## 1. The primary attack: Weyl limit-point / limit-circle on the noncompact fiber

On the honest noncompact fiber the boundary freedom at each end is **not**
automatic. It is the Weyl deficiency index — the number of `L^2` solutions of
`(A~ − λ)u = 0` for `Im λ ≠ 0` at that end:

- **Limit-point (LP)** at an end (`n = d/2`, "half"): no boundary condition is
  allowed or needed there; that end contributes **no** boundary freedom.
- **Limit-point at BOTH ends** ⇒ the operator is **essentially self-adjoint**
  ⇒ a **unique** domain ⇒ the selector is **derivable**, not external.
- **Limit-circle (LC)** at an end (`n = d`, "full"): the full endpoint freedom
  survives there, and a `U(1)`-or-larger of boundary conditions must be chosen.

For a first-order `A~ = B(s)∂_s + W~(s)`, the LP/LC classification is fixed by
the **asymptotics of `B` and `W~` at the fiber ends** — precisely the datum
Prong A logged as **`D2` SOURCE-SILENT**: "decay / self-adjoint domain at the
fiber ends, fixed independently of `z` and `δ` … Route-1 (no locus)"
(`prongA-extraction-2026-07-21.md:67`). The moduli dimension is a **function of
an unknown**.

### 1.1 Dial-the-asymptotics probe (foreground, EXIT 0)

`tests/channel-swings/source_domain_selector_prongB_hostile_verify_probe.py`
uses the canonical Weyl model `−y'' + q(s)y = λy` on `[1,∞)` at `λ = i` (a
scalar reduction of a first-order Dirac-type system) and counts `L^2` solutions
by the **non-oscillatory WKB-amplitude criterion** `|y_±|^2 = |q−λ|^{-1/2}
exp(±2∫Re√(q−λ))` — the honest asymptotic object that decides `L^2` membership,
with no phase/amplitude drift. Dialing `q = c·s^p`:

| end asymptotics | ∫\|y₊\|² | ∫\|y₋\|² | n | class |
|---|---|---|---|---|
| `q=−s^{1.5}` (p<2) | ∞ (`4.1e15`) | finite (`0.98`) | **1** | LIMIT-POINT |
| `q=−s^{2}` (p=2, borderline) | ∞ (`9.7e3`) | finite (`0.98`) | **1** | LIMIT-POINT |
| `q=−s^{3}` (p>2) | finite (`6.1`) | finite (`0.85`) | **2** | LIMIT-CIRCLE |
| `q=+s^{3}` (confining) | ∞ | finite (`0.22`) | **1** | LIMIT-POINT |

**The deficiency index — hence the moduli-end dimension — changes `1 → 2` as
the end-asymptotics are dialed across `p=2`, same operator family.** A limit-point
end kills a torus factor; a limit-circle end keeps a `U(1)`. Controls in the
same probe:

- **C1 (compact-collar artifact):** on a *fixed* `[1,3]`, both branches are
  finite (`L^2`) for **every** `p` — "n=2 always," blind to LP/LC. This is
  Prong B's `T^2`/`U(1)`-floor regime, and it is asymptotics-independent by
  construction.
- **C2 (non-WKB cross-check):** the confining end integrated as a direct,
  monotone (non-oscillatory) ODE gives fundamental-matrix singular values
  `(4.3e15, 0.47)` at `s=6` — one dominant, one recessive — confirming `n=1`
  independently of WKB.
- **C3 (first-order Dirac tie-in):** for `H = −i σ₂∂_s + m σ₁` with the
  principal coefficient `B=−iσ₂` **invertible**, the constant coefficient at
  `λ=i` has real eigenvalues `±√(1+m²)`, decay rate `≥ |Im λ| = 1` for **all**
  masses. A non-degenerate Dirac end is **robustly limit-point** — you cannot
  dial into LC by changing the mass. Reaching LC requires the **principal
  coefficient `B` to DEGENERATE** at the end (become non-invertible) — i.e. GU's
  wall where `C_0 = q^{1/2} → 0` — which is again a `D2`-class asymptotic fact
  the sources do not fix.

### 1.2 What this does to Prong B's numbers

- **`T^2` / dim 2 does NOT transfer.** It is the deck-commutant torus inside the
  collar's *automatic* `U(d)`. On the noncompact fiber the boundary freedom is
  `Σ_ends (LC freedom)`, capped by the deck-commutant — a number set by the
  source-silent asymptotics, which the toy fixes by fiat (compactness), not by
  GU structure.
- **The default is UNIQUENESS, not multiplicity.** For a non-degenerate,
  complete Dirac-type end the generic behavior is limit-point at both ends
  (the Chernoff / essential-self-adjointness default for first-order symmetric
  systems on complete manifolds). In that horn the domain is **unique** and the
  selector is **derivable** — the exact opposite of "provably external." The
  burden Prong B assumes (multiplicity is the structural default) is **reversed**:
  multiplicity requires a *singular* end (coefficient degeneration / incomplete
  end), and whether GU's fiber has one is the unknown `D2` datum.

## 2. Secondary attack — the `U(1)` floor does not survive noncompactness

Prong B §5 steelmans uniqueness to the irreducible case and finds an unremovable
`U(1)` (the phase `θ` of `T_θ = e^{iθ}S(b)`), concluding a floor `≥ U(1)` "even
in the most favorable case," hence "uniqueness is *structurally impossible*."

This is a **compact-collar theorem**. The phase `θ` is a *boundary-condition*
parameter — it only exists when there is boundary freedom to parametrize (a
graph domain `D_T`). In the **limit-point horn there is no graph domain and no
`θ`**: the operator is essentially self-adjoint, the domain is unique, and there
is nothing to fix. The global `e^{iθ}` that remains is the ordinary `U(1)` gauge
phase of the wavefunction — a symmetry, **not** a choice of domain and **not** a
modulus. So the claim "the floor is always `≥ U(1)`" is false on the noncompact
LP fiber: the floor there is **dim 0**. Prong B's §5 dichotomy table ("in
*neither* column is the moduli a point") is a table of the *collar*, and its
"structurally impossible" is unproven off the collar.

## 3. Secondary attack — toy faithfulness and the unfixed deck representation

Prong B places GU "**firmly** in the reducible column" (§6) to get `dim ≥ 2`,
via "the Krein form is purely cross-chirality with chirality persisting as a
sector label; the commutant contains at least the chirality grading, so the
action is reducible." But the same paragraph concedes: "**Prong A established
the sources do not even fix the deck's fiber representation.**"

That is an internal inconsistency. Reducibility of the deck action on the
boundary fiber is a statement **about the deck's fiber representation** — the
very object Prong A/§6 admits is unfixed. You cannot be "firmly" in a column
selected by data you have just declared source-silent. The `dim ≥ 2` step
therefore rests on **two** unfixed inputs stacked: (a) reducibility of the
(unfixed) deck fiber rep, and (b) limit-circle (unfixed asymptotics). The
`(1,1)` signature is a faithful miniature of the cross-chirality **sign** pattern
`(+96,−96,0)`, but the deck realization `U = σ_z` (a sector *grading*) is a
*choice* the sources do not license as GU's actual deck; a mixing/irreducible
deck rep is not excluded by any cited source.

## 4. Secondary attack — "distinct spectrum ⇒ inequivalent" is muddied off the collar

Prong B §4 certifies physical inequivalence via the closed form
`cosh(λL) = cos((α+β)/2)/cos((α−β)/2) = ρ(α,β)` and a continuum of distinct `ρ`.
This is a **compact-interval (discrete-spectrum)** phenomenon: `cosh(λL) = ρ`
has isolated eigenvalue solutions because `[0,L]` is finite. On the noncompact
fiber:

- As `L → ∞` the spectrum becomes **continuous/banded**; the discrete `cosh = ρ`
  ladder does not survive, so "a continuum of distinct spectra" is not the
  correct object.
- Different self-adjoint (Krein-self-adjoint) extensions of the *same* symmetric
  operator share the **same essential/continuous spectrum**; they can differ
  only in discrete eigenvalues inside gaps. "Distinct spectrum" is therefore a
  much weaker separator than on the collar, and can be *empty* even for genuinely
  different LC extensions.
- In the **LP horn the argument is vacuous** — there is one extension, so no two
  domains to separate.

The inequivalence certificate, like the moduli count, is a collar object.

## 5. Fairness check — what I could NOT establish (why this is not `HV-REFUTE`)

I cannot force the limit-point horn. GU's wall is a genuine coefficient
degeneration (`C_0 = q^{1/2} → 0`, `B` complex on the crossed side —
`certificate §5`), which is exactly the kind of **singular end that can produce
limit-circle** and restore boundary freedom. Because the asymptotic/degeneration
data (`D2`) is source-silent, I can neither prove essential self-adjointness
(which would flatly refute `B-MULTIPLICITY`) nor prove limit-circle (which would
transfer some multiplicity). The outcome is genuinely **undetermined by
currently-known structure** — which is the WEAKEN finding, not a REFUTE.

Caveat carried honestly: the LP/LC theory is cleanest for Hilbert-space
symmetric operators. GU's operator is `J`-symmetric (Krein/indefinite). The
`J`-symmetric limit-point/limit-circle theory (Sims-type) is subtler, but the
two conclusions used here are robust across the Hilbert and Krein settings: (i)
a **compact** interval gives full endpoint freedom regardless of asymptotics,
and (ii) the **noncompact** endpoint freedom is governed by `L^2`-solution
counts that depend on the end-asymptotics. Both are exactly what sink Prong B's
transfer.

## 6. Corrected claim (precise)

Replace Prong B's unconditional "`T^2` (dim 2); the selector is **provably
external**; a positive-dimensional multiplicity **provably** remains; uniqueness
is **structurally impossible**" with:

> **The deck-equivariant Krein-self-adjoint domain moduli on the noncompact
> fiber has dimension `= (Σ over ends of the limit-circle boundary freedom) ∩
> (deck-commutant)`, which is DETERMINED by the end-asymptotics of `B` and `W~`
> — exactly the `D2` datum Prong A found SOURCE-SILENT. Consequently:**
>
> 1. **Prong B's `T^2` (dim 2), its `U(1)` floor, and its "continuum of
>    distinct spectra" are COMPACT-COLLAR ARTIFACTS and do not transfer.**
> 2. **The outcome is CONTINGENT on the source-silent `D2` asymptotic
>    classification, not an unconditional theorem.**
>    - *Limit-circle end(s)* (a genuinely singular end, e.g. real wall
>      degeneration): a positive-dimensional external selector is required —
>      `S-OBSTRUCTED` holds in spirit, but the dimension is set by the (unknown)
>      number of LC ends, **not** "2," and the `U(1)` floor is not guaranteed.
>    - *Limit-point at both ends* (the DEFAULT for a non-degenerate / complete
>      Dirac-type end): the operator is essentially self-adjoint, the domain is
>      **UNIQUE**, and the selector is **DERIVABLE from structure** — a
>      `B-FORCED`-type outcome in which "provably external / structurally
>      impossible to single out" is **FALSE**.
> 3. **What survives:** an external input **must** be imported either way,
>    because the asymptotic classification (`D2`) that decides which horn holds
>    — and hence whether *any* multiplicity exists — is itself source-silent.
>    So "**the physical domain is not pinned by currently-known GU structure**"
>    survives. "**A positive-dimensional multiplicity provably remains / cannot
>    be removed inside the present structure**" does **not**.

Net effect on the localization: `DOMAIN-OBSTRUCTION-SOURCE` stays a real gap,
but the correctly-typed missing datum is the **asymptotic/limit-classification
of the fiber ends (`D2`)** — upstream of Prong B's "boundary phase / holonomy."
The phase selector is needed **only in the limit-circle horn**; in the
limit-point horn the structure selects its own domain. Prong B's upgrade from
"not yet found" to "**cannot** be found inside the present structure" is not
earned — the correct statement is "**cannot be decided** without the source-
silent asymptotic datum, and the default (limit-point) would make it derivable."

## 7. Adjudicated outcome

**`HV-WEAKEN`.** The `S-OBSTRUCTED`-flavored kernel ("the domain is not pinned
by known structure; an import is required") holds because `D2` is silent. But
Prong B **over-claims**: the specific `T^2`/dim-2/`U(1)`-floor is a compact-collar
artifact, the "physically-inequivalent continuum" is a discrete-spectrum
artifact, the "reducible ⇒ dim ≥ 2" step stacks on an unfixed deck rep, and the
modality "provably external / structurally impossible" is **reversed** in the
limit-point horn, which is the generic noncompact default. The honest claim is
the contingent statement of §6.

No claim status, canon verdict, paper status, ledger, or public posture is
moved by this note. I did not edit the Prong B artifact, LANE-STATE,
research-portfolio, NEXT-STEPS, or any claim/canon/verdict/ledger file.

## Boundary

Only this artifact and its probe
(`tests/channel-swings/source_domain_selector_prongB_hostile_verify_probe.py`,
foreground, EXIT 0) were written; GU is otherwise read-only. No commit, no push,
no edit to any claim / canon / verdict / ledger / planning file. No claim status,
canon verdict, or public posture changes.
