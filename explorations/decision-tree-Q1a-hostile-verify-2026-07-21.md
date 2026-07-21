---
title: "Hostile verify of the Q1a-FORCED win: the limit-point verdict does NOT close from committed structure — the win's own probe PLANTS the load-bearing premise (bounded P,T,C_0,V,phi'), while the actual GL(4,R)/O(3,1) end-model has those coefficients blowing up EXPONENTIALLY along generic degeneration rays; the 'min P/(P+T)=0.36' floor is the surviving-sector existence floor at finite collar s, not a true-end floor (10% of random rays fall below it and cross into the q<0 K-null sector at s=25, one ray driving rho->0); the one genuinely-forced sub-fact is B=-iK_uG non-degeneracy wherever P>0 (theorem-grade, scale-free), which alone does NOT force LP; the LP/LC answer reduces to the native measure / completeness datum the hourly BLOCKED correctly named, and the Chernoff 'complete Riemannian => LP' default is ILL-TYPED because F=GL(4,R)/O(3,1) has non-compact isotropy O(3,1) and carries no invariant Riemannian metric — BLOCKED confirmed and sharpened"
status: active_research
doc_type: exploration
created: 2026-07-21
verifies: explorations/decision-tree-Q1a-fiber-end-classification-2026-07-21.md
inputs:
  - explorations/decision-tree-Q1a-fiber-end-classification-2026-07-21.md
  - explorations/decision-tree-Q1a-limit-classification-2026-07-21.md
  - explorations/source-domain-selector-prongB-hostile-verify-2026-07-21.md
  - explorations/sector-relative-section-theory-2026-07-20.md
  - explorations/n2-end-family-2026-07-20.md
  - explorations/continuum-pencil-graph-domain-certificate-2026-07-20.md
  - explorations/continuum-pencil-domain-gate-2026-07-20.md
  - tests/channel-swings/n2_end_family_probe.py
  - tests/channel-swings/decision_tree_Q1a_fiber_end_classification_probe.py
probe: tests/channel-swings/decision_tree_Q1a_hostile_verify_true_end_probe.py (foreground, EXIT 0)
outcome: HV-REFUTE
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_actions: none
---

# Hostile verify: does Q1a-FORCED (limit-point) close from committed structure?

Adversarial refutation pass, maximum skepticism (a paper-unblocking `B-FORCED`-type
win). The target is `decision-tree-Q1a-fiber-end-classification-2026-07-21.md`,
outcome **`Q1a-FORCED`** — the claim that GU's own structure puts
`A~ = B(s)∂_s + W~(s)`, `B = -iK_uG`, in the **limit-point** case at the true
noncompact fiber ends, so the domain is unique and forced, θ dissolves, and the
pencil theorem `OPERATOR-END-PENCIL` closes with **no imported datum**.

## 0. Verdict up front

> **`HV-REFUTE`.** The `FORCED` verdict does **not** close from committed GU
> structure. It rests on three legs; **exactly the two load-bearing ones fail at
> the true ends**, and they fail the same way Prong B failed — by substituting a
> bounded surrogate for the true noncompact end asymptotics:
>
> - **Leg (i) — B non-degeneracy (`‖B‖=‖B⁻¹‖=1` wherever `P>0`): SURVIVES,
>   theorem-grade, scale-free.** `B = -iK_uG` is a product of two involutions;
>   its singular values are `1` at any scale wherever `P>0` strictly. This is a
>   genuine sharpening of the record and I do not contest it. **But it does not
>   force limit-point** — the win's own `non-J-symmetric B` control shows
>   non-degenerate `B` alone leaves the deficiency ill-defined.
> - **Leg (ii) — `P` floored at the ends (`min P/(P+T)=0.36`): MISREAD.** That
>   `0.36` is the `P>0` **existence-domain floor on the surviving (conformal
>   blow-up) sector at finite collar `s`** (`n2` §"Sampled", `sector-relative`
>   §5), not a floor over all rays to `s→∞`. On the actual model **10% of random
>   unit rays fall below `0.36` at `s=25`, 10% cross into the `q<0` sector, and a
>   timelike-dominant ray drives `ρ=P/(P+T) → 0`** (probe TEST 2b/3). Where
>   `ρ→0` the symbol is timelike-dominated (`q<0`), which is exactly the
>   cone-crossing / K-null sector where the `n2` model's own theorem says **no
>   K-definite cut exists** — the cut/section apparatus that *defines* `A~` exits
>   its existence domain. (`B` itself stays non-degenerate there because `P>0`
>   strictly; the failure is upstream of `B`.)
> - **Leg (iii) — `W~` bounded (`C_0=√|P−T|`, `V`, `φ'` bounded): FALSE in the
>   physical scale.** Along the actual degeneration rays the covector `ξ(s)`, and
>   with it `P, T, C_0=√|q|, V`, grow/decay **exponentially** (`C_0` slope
>   `+0.5…+1.0` per unit `s`; probe TEST 1). The win's probe planted
>   `P=1+0.2sin`, `T=1+0.5sin`, `φ'=0.24cos` — bounded `O(1)` toys — and then
>   verified "bounded ⇒ LP". That is **circular for gaps A and C**.
>
> The honest reduction: after removing the exponential blow-up (a **non-unitary**
> rescaling, so it changes the L² measure), the LP/LC answer depends on the
> **native measure / completeness** datum — precisely what the hourly's
> `Q1A-END-ASYMPTOTICS-BLOCKED` named as missing. And the win's completeness
> fallback (Chernoff: "complete Riemannian metric ⇒ LP") is **ill-typed**:
> `F = GL(4,R)/O(3,1)` has **non-compact isotropy `O(3,1)`**, so it admits **no
> invariant Riemannian metric** — only a pseudo-Riemannian one — and the
> essential-self-adjointness default does not apply.
>
> **`FORCED` is not earned.** The pencil theorem does **not** close from
> structure with no imported datum. The correct disposition is the hourly's
> **`BLOCKED`, confirmed and sharpened**: the single genuinely-forced sub-fact is
> `B` non-degeneracy; everything above it (the LP/LC classification itself) is
> unfixed by committed structure. This is *not* a claim that limit-circle is the
> answer — it is a claim that the classification is undetermined, exactly as
> BLOCKED found.

## 1. The setup flaw: the win's probe never touches the fiber geometry

`decision_tree_Q1a_fiber_end_classification_probe.py` reduces the LP/LC question
(correctly) to "is `W~` bounded at the ends?" — then answers it with **planted**
coefficients:

```python
Pfun  = lambda s: 1.0 + 0.2*np.sin(0.5*s)      # bounded by fiat
Tfun  = lambda s: 1.0 + 0.5*np.sin(0.7*s + 1)  # bounded by fiat
phip  = lambda s: 0.24*np.cos(0.3*s)           # bounded winding by fiat
C0    = lambda s: np.sqrt(abs(Pfun(s)-Tfun(s)))# bounded because P,T are
```

Every "GU CASE" row feeds these into an LP counter and gets `n=1`. But `P, T, φ'`
here are **sinusoids around 1**, not the section-theory `P = tr(c_s²)/128`,
`T = -tr(c_t²)/128` of the actual end. The probe proves only the tautology *"IF
the end coefficients are bounded THEN LP"* — which no one disputes. It never uses
`F = GL(4,R)/O(3,1)`, the degeneration rays `a(s)=exp(2αs)`, or the frame scaling.
**This is the Prong-B compact-collar trap in a new costume**: Prong B substituted
a compact interval (where every solution is `L²` by fiat); the win substitutes a
bounded coefficient profile (where LP holds by fiat). Both replace the true
noncompact end asymptotics with a surrogate that pre-decides the answer.

## 2. The hostile probe: same questions, actual model

`tests/channel-swings/decision_tree_Q1a_hostile_verify_true_end_probe.py`
(foreground, numpy only, deterministic, **EXIT 0**) rebuilds the faithful `n2`
end-model verbatim — DeWitt `(9,5)` form, closed-form G-orthonormal frame
`F_s`, `D(t,s)=c(ξ(t,s))` with `ξ` the components of the one fixed covector `XI`
in `ρ(R_t)F_s`, ray `a(s)=exp(2αs)` — and asks the win's own structural questions
at **`s` up to 25–30 (true ends)**, not on a bounded collar. `P(s)=Σ_{a<9}ξ_a²`,
`T(s)=Σ_{a≥9}ξ_a²`, `q=P−T`, `ρ=P/(P+T)`, `C_0=√|q|` (all matching the probe's
`qform` and `ETA=[+1]^9⊕[−1]^5`). Base anchor reproduced: `ξ(0,0)=XI`,
`P₀=40.45, T₀=10.32, q₀=30.13`.

### TEST 1 — the physical scale blows up exponentially (refutes leg iii)

| ray `α` | `|ξ|(25)` | `C_0(25)` | slope `log C_0` | slope `log|ξ|` |
|---|---|---|---|---|
| conf-up `(1,1,1,1)` | `1.0e6` | `1.0e6` | `+0.50/s` | `+0.50/s` |
| conf-down `(-1,-1,-1,-1)` | `4.4e11` | `2.9e11` | `+1.00/s` | `+1.00/s` |
| boost `(1,0,0,1)` | `1.7e7` | `1.6e7` | `+0.68/s` | `+0.68/s` (frame degenerates past `s≈24`) |
| timelike `(0,0,0,1)` | `8.0e9` | `8.0e9` | `+0.94/s` | `+0.92/s` (frame degenerates past `s≈24`) |

`C_0=√|q|` and `|ξ|` (hence `V` and `W~=K_uV`) are **exponentially unbounded** on
every named ray. The certificate's standing hypotheses `B,H∈W^{1,∞}`,
`W~∈L^∞`, "`C_0` bounded" (`continuum-pencil-graph-domain-certificate` §1;
`domain-gate` §1) are **not met by the actual end** in the physical scale. Note
also (TEST 1, TEST 4): the boost and timelike rays make the model's **own
closed-form frame degenerate** at finite `s` — an internal signal that the
`s→∞` limit is a genuine coordinate/metric singularity, not a benign collar.

### TEST 2 / 2b — `ρ` is not floored at the true ends (refutes leg ii)

| ray `α` | `ρ(3)` | `ρ(4)` | `ρ(≈25)` | sector at end |
|---|---|---|---|---|
| conf-up | 0.994 | 0.994 | 0.994 | gapped `q>0` |
| conf-down | 0.721 | 0.721 | 0.721 | gapped `q>0` |
| boost | 0.933 | 0.922 | 0.917 | gapped `q>0` |
| **timelike `(0,0,0,1)`** | **0.510** | **0.127** | **0.000** | **CROSSED `q<0`** |

Sweep of 4000 random unit rays (2310 frame-survivors) at `s=25`: **228 (10%) have
`ρ<0.36`**, **240 (10%) land in the `q<0` crossed sector**, minimum
`ρ=0.0000` at `α≈[+0.07,+0.05,−0.02,+1.00]`. The `0.36` figure is thus the
existence-domain floor of the **surviving** conformal-blow-up sector sampled at
finite collar depth — precisely how `n2`/`sector-relative` report it ("`min
P/(P+T)=0.36` over all sampled loops", the `P>0` existence bound) — **not** a
universal true-end floor. The win's §2 upgrade of it to "`P` is floored away from
0 at the ends … over 200 rays incl. the boundary-at-infinity" over-reads the
source: the boundary-at-infinity checks live on the surviving sector; the
crossing/timelike/undecided rays (`53/…/15` of the 200 at sampled depth) are
exactly where the floor is **not** claimed.

### TEST 3 — LP control vs breakdown control

- **LP control (conf-up):** `ρ(25)=0.9936`, `q=+1.0e12>0` — gapped, LP-consistent.
- **Breakdown control (timelike):** `ρ(24)=0.0000`, `q=−6.3e19<0` — the crossed /
  K-null sector. By the `n2` little theorem ("for `q<0` the halves `E_{±i}(D)` are
  exactly `K_S`-null … no K-definite cut exists"), the section datum that *builds*
  `K_u`, `B`, `A~` **does not exist** on this end. The LP verdict is not "false"
  there — it is **undefined**.

### TEST 4 — winding: fair to the win on single-exponent rays

On the conf-up ray the faithful winding `‖dK_u/ds‖ = 4.7e-12` at `s=25` (`K_u`
aligns to the dominant exponent; `φ'→0`). So the win's worry that `φ'` blows up
at the ends is **not** the failure mode along a generic single-exponent ray — I
concede this to the win. But (a) this is the *normalized-direction* winding and
says nothing about the physical-scale blow-up of TEST 1, and (b) on the timelike
and boost rays `K_u` is already undefined at `s=25` (`P→0` numerically — the
pure-timelike stratum the win called "empty" is *approached* at the true end).

### TEST 5 — the rescue is a non-unitary, measure-changing gauge

On conf-up, `d/ds log|ξ| → +0.500` (constant). So the blow-up is
`ξ ~ e^{λ(s)}ξ̂` with `λ(s) ~ α_max·s` linear, and normalizing multiplies the
section by `e^{−λ(s)}`, `|e^{−λ}|≠1` — a **non-unitary similarity** that changes
the L² measure. In the **normalized** measure the coefficients are bounded and
(on the surviving sector) LP-consistent; in the **physical** (fiber-volume)
measure `C_0,V` blow up. Which measure is native — the "native measure and
Krein/Hilbert comparison used for square integrability" — is **item 2 of the
hourly's reopen packet** and is not fixed by committed structure.

## 3. The completeness default is ill-typed (gap D is a type error, not a grade gap)

The win's leg for "limit-point default" and for the gauge reduction
`B=-iK_uG → -iσ_z` (gap D) is: *the end is at infinite length in a complete
metric, so Chernoff-type essential self-adjointness applies.* This presumes a
**complete Riemannian** manifold. But `F = GL(4,R)/O(3,1)` has **non-compact
isotropy** `O(3,1)`: a homogeneous space `G/H` admits a `G`-invariant Riemannian
metric only when the isotropy representation is bounded, i.e. `H` compact. `O(3,1)`
acts on `T_o F = Sym²(R⁴)` unboundedly (boosts), so **there is no invariant
Riemannian metric** on `F` — only the pseudo-Riemannian (indefinite Killing)
metric. On a pseudo-Riemannian manifold the Chernoff/finite-propagation
essential-self-adjointness theorem **does not hold** (the wave operator is not
elliptic; "distance" is not positive-definite; geodesic completeness ≠ metric
completeness). So gap D is not a "sampled → theorem" hardening task — the theorem
the win wants to invoke **is not available for this geometry**. This is
independent of, and compounds, the measure ambiguity of §2/TEST 5.

## 4. Secondary — the Krein count could differ (gap B is live, not cosmetic)

Even granting bounded coefficients on a surviving ray, the win's LP conclusion is
proved on a **Hermitian** reduction (`B` rotated to `-iσ_z`, Hermitian `W~`;
counter B). The genuine object is `J`-symmetric (`J=K_S`, indefinite). Two Krein
facts block the transfer of "n=1 ⇒ unique":

1. **Unequal indices are possible.** For a `J`-symmetric operator the deficiency
   indices `(n_+,n_-)` need not be equal; if `n_+≠n_-` there is **no**
   `J`-self-adjoint extension at all — a third outcome (neither "unique domain"
   nor "`U(1)` of domains") that the Hermitian probe cannot see. The win's own
   "non-J-symmetric `B` ⇒ deficiency ill-defined" control is a warning in this
   direction, not a resolution.
2. **The indefinite metric degenerates exactly on the crossed sectors.** The
   `n2` K-null theorem makes `⟨x,K_S x⟩=0` on the relevant half-spaces for `q<0`
   — precisely the sectors TEST 2b shows are reached at the true ends. Where the
   Krein form is null, Hilbert LP/LC intuition provides no guarantee either way.

So the Sims-type `J`-symmetric LP/LC (or its failure) is genuinely open, as HV §5
and the win's own gap B concede. The win did not close it; it set it aside.

## 5. Reconciliation with the hourly BLOCKED — BLOCKED was right

The hourly (`decision-tree-Q1a-limit-classification-2026-07-21.md`,
`Q1A-END-ASYMPTOTICS-BLOCKED`) refused to derive the classification because "the
committed construction does not specify the end geometry or the asymptotic
coefficients needed to compute the deficiency indices … no GU-native end
asymptotics or completeness theorem is frozen." Its reopen packet asked for (1)
the fiber coordinate/ends, (2) the native measure and Krein/Hilbert comparison,
(3) two-sided bounds for `B, W~` and the fundamental symmetry at each end, (4) a
`J`-symmetry proof on the noncompact geometry, (5) a genuine two-ended deficiency
computation.

**Was BLOCKED right to refuse, or did it miss the involution-product mechanism?**
It was **right**. The involution-product mechanism the win contributes is real,
but it discharges only reopen-item-adjacent fact about `B` (non-degeneracy where
`P>0`) — it is a genuine sharpening, and BLOCKED arguably under-credited it. It
does **not** supply items 2, 3, or 5: the measure is still unfixed (§2/TEST 5),
the true-end bounds on `W~`/`C_0` are **false** as stated (they blow up, TEST 1),
and the `J`-symmetric two-ended count is untouched (§4). The win reached `FORCED`
not by supplying the missing packet but by **planting** bounded coefficients
(item 3 by fiat) and **misreading** the `0.36` sample (item 2/5 by fiat). Strip
the plants and the misread and the hourly's disposition is exactly what remains.

## 6. Precise corrected verdict

Replace the win's

> "GU structure forces limit-point … the pencil theorem can close from structure
> with no imported boundary datum; moduli dimension = 0; θ dissolves"

with:

> **The fiber-end LP/LC classification is NOT fixed by committed GU structure.**
> The only genuinely-forced sub-fact is `B=-iK_uG` non-degeneracy wherever `P>0`
> (`‖B‖=‖B⁻¹‖=1`, an involution-product theorem, scale-free). This alone does
> **not** force limit-point. The classification additionally requires the true-end
> asymptotics of `W~` and the **native measure**, which the committed construction
> does not supply; in the actual `GL(4,R)/O(3,1)` model those coefficients blow up
> exponentially, the `P/(P+T)` floor holds only on the surviving spacelike-gapped
> sector (10% of rays cross into the `q<0` K-null sector at the true ends, where
> the defining cut does not exist), and the Chernoff limit-point default is
> unavailable because `F` carries no invariant Riemannian metric (non-compact
> isotropy `O(3,1)`). Consequently `Q1A-END-ASYMPTOTICS-BLOCKED` **stands**,
> sharpened by the one forced sub-fact. θ does **not** provably dissolve; the
> pencil theorem `OPERATOR-END-PENCIL` does **not** close with no imported datum.

**Does the pencil theorem actually close from structure?** No. It closes only
*conditional on* an imported package: (L) fix the native measure / Krein-Hilbert
comparison making `A~` self-adjoint on the noncompact ray, AND (L′) restrict to
the spacelike-gapped sector (or prove the timelike/crossed rays are not genuine
fiber ends), AND (L″) a Sims-type `J`-symmetric limit-point theorem with equal
Krein deficiency indices for the (measure-normalized) `A~`. If all three are
supplied, the win's structural lean — `B` non-degenerate + normalized `W~`
bounded + winding→0 on the surviving sector — plausibly yields limit-point on
that sector. None of the three is currently frozen. That gap is not "sampled →
theorem"; (L) and the pseudo-Riemannian obstruction to the default are **type/
existence** gaps, and (L″) is genuinely open.

**Exact remaining lemma (if one insists on a single conditional).** *"There is a
GU-owned measure `w(s)ds` on the noncompact fiber ray for which (a) `A~` is
`J`-self-adjoint with equal Krein deficiency indices, (b) the measure-normalized
`W~` and `φ'` are bounded and `K_u` aligns at each end, and (c) every genuine
fiber end lies in the spacelike-gapped sector."* Under this lemma, LP holds and
θ dissolves; without it the classification is undetermined. This reduces the win
to **"LP holds IFF ⟨that measure/sector lemma⟩,"** which is BLOCKED-sharpened,
not FORCED.

## 7. What survives, stated once (truth-seeking, not verdict-scoring)

- **Survives (keep):** `B=-iK_uG` is non-degenerate with `‖B‖=‖B⁻¹‖=1` wherever
  `P>0`, an exact involution-product fact, scale-independent — a real upgrade over
  the certificate's pointwise-invertibility statement, and a legitimate credit the
  hourly BLOCKED under-stated. On the spacelike-gapped surviving sector, in the
  normalized gauge, the end is LP-consistent (winding→0, `ρ` floored, gapped).
- **Falls (do not ship):** "`P,T,C_0,V,W~` bounded at the ends" (exponentially
  false); "`min P/(P+T)=0.36` ⇒ `P` floored at all true ends" (surviving-sector
  finite-collar figure); "limit-point default from a complete metric"
  (pseudo-Riemannian; no invariant Riemannian metric); "the pencil theorem closes
  with no imported datum" (needs the measure/sector/Krein lemma of §6); "moduli
  dimension = 0 / θ dissolves" (contingent on the same lemma).

## 8. Boundary

Exploration tier. Only this artifact and its probe
(`tests/channel-swings/decision_tree_Q1a_hostile_verify_true_end_probe.py`,
foreground, **EXIT 0**) were written. GU otherwise read-only. No commit, no push.
No edit to LANE-STATE, research-portfolio, NEXT-STEPS, the prereg, the Q1a win,
the hourly BLOCKED, any other agent's artifact, or any claim/canon/verdict/ledger
file. No claim status, canon verdict, paper status, or public posture changes.
Externality of σ/τ untouched. The verdict is `HV-REFUTE`: `Q1a-FORCED` does not
close from committed structure; `Q1A-END-ASYMPTOTICS-BLOCKED` is confirmed and
sharpened, with the single forced sub-fact (B non-degeneracy) preserved and the
exact conditional lemma named.
