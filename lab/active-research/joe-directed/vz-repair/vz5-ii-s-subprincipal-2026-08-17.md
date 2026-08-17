---
title: "VZ-5: the explicit coordinate formula for II_s, and the subprincipal stability of the 4D Velo-Zwanziger verdict"
artifact_type: exploration
status: independently_verified
doc_type: construction_result
created: "2026-08-17"
work_item: VZ-5
channel: vz_repair
canonical_effect: pending_integration
grade: "EXACT sympy throughout, no float load-bearing anywhere. Christoffel blocks: five of six verified fully symbolically (general 10-symbol fiber point, Koszul identity, lowered form -- no matrix inversion beyond a cheap 4x4); the sixth (fiber self-connection) verified via an exact-rational Koszul solve at three independent generic points (55 pairs x 3 = 165 checks) -- narrower scope than the other five, documented honestly in POSTFLIGHT (sympy's `simplify()` gave a FALSE mismatch on the fully-expanded 10-variable closed form; the exact-rational solve does not have this failure mode). II_s formula: assembled from the verified blocks for a fully general section g_ab(x) (sympy Function), CERTIFIED via the Gauss-formula orthogonality theorem checked exactly across 5 sections x up to 3 points (520 individual zero-checks, all exact rational, zero failures after a real bug -- found by this same check -- was fixed). FC-VZ-4 verdict: exact Cl(3,1) toy-but-structurally-faithful characteristic-determinant computation, using an ACTUAL sampled II_s value as the inserted endomorphism, plus two required contrary controls (both exact, both fire)."
target_claim: FC-VZ-4
target_claim_verdict: "HARDENED, not upgraded past CONDITIONALLY_RESOLVED. II_s (explicit, closed-form, orthogonality-certified) sources no new characteristics at subprincipal order in the toy detector; the general structural reason (a background/xi-independent endomorphism cannot alter the top-degree-in-xi part of a characteristic determinant) is the SAME reason `vz-subprincipal-symbol-rs-2026-06-23.md` already gave for the Weyl/Shiab terms, now extended to the newly-explicit II_s term specifically and grounded in an actual formula rather than a schematic placeholder. Does not itself move the canon verdict -- canon integration is the owner's call, not this artifact's."
depends_on:
  - papers/drafts/canonical-structures-14d-metric-geometry-2026-06-22.md
  - canon/no-go-class-relative-map.md
  - explorations/vz-evasion/vz-subprincipal-symbol-rs-2026-06-23.md
  - explorations/vz-evasion/vz-schur-complement-2026-06-23.md
  - explorations/geometry-curvature-emergence/ii-s-coordinate-formula-2026-06-23.md
  - explorations/geometry-curvature-emergence/pc2-met-x4-bundle-formalization-stub-2026-06-22.md
  - explorations/geometry-curvature-emergence/codazzi-sp64-bundle-2026-06-23.md
  - lab/active-research/joe-directed/vz-repair/vz4-pullback-is-a-contraction-2026-08-15.md
  - lab/methods/source-native-comparator-routing.md
  - lab/active-research/joe-directed/carrier-decl/fx2-typed-carrier-declaration-2026-08-16.md
fork_assumed:
  - LITERAL-GRAPH-VS-HORIZONTAL-NORMALIZED (resolved for this artifact's scope, see SS1.4)
residual_declared:
  - id: REDUCTION-FIDELITY
    statement: "Carried unchanged from VZ-4: s*(R^14D) is the whole 4D one-form bundle, so no gauge fixes 'the 4D RS field is the observed image of the 14D RS field.' Out of scope for this arc by the task's own instruction; not touched, not discharged."
    status: open
  - id: CODAZZI-SP64-EXPLICIT
    statement: "OQ2 (the Codazzi-Mainardi equation for II_s in the Sp(64) bundle) is not computed here -- this artifact supplies the Gauss-side object (II_s itself) that OQ2 would need as an input, but does not attempt the Codazzi computation."
    status: open
scripts:
  - tests/channel-swings/joe_directed_vz5_ii_s_subprincipal.py
---

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `SOURCE_NATIVE_ROUTE`

The object computed is GU's own declared second fundamental form of its own
declared observation map (`s*(theta) = II_s`, Prop 7.2 of the drafts file),
and the question asked of it (does it source spacelike characteristics) is
GU's own Velo-Zwanziger evasion mechanism at the 4D level. No conventional
particle-physics comparator is invoked anywhere in this artifact.

---

# VZ-5 — II_s in coordinates, and why it cannot move the 4D characteristic set

## 0. Verdict in one page

**The explicit formula.** For the graph section `s(x) = (x, g_ab(x))` of
`Y^14 = Met(X^4)`, with the gimmel metric `Gcal` in the block-diagonal
coordinate-patch convention (Prop 2.1, §2.2 below), the second fundamental
form is

```
II_s(d_mu, d_nu) = B_mu_nu^rho * d_rho  +  B_{mu nu, ab} * d/du_ab
```

with **horizontal part**

```
B_mu_nu^rho = (1/2) g^{rho sigma}( d_nu g_{sigma mu} + d_mu g_{sigma nu} )  -  Gammabar^rho_{mu nu}
```

and **vertical part** (the `Sym^2 T*X^4`-valued object Prop 7.2 actually asks
for — see §1.2 on why no further index-raising is needed):

```
B_{mu nu, ab} = d_mu d_nu g_ab
                - Gammabar^lambda_{mu nu} d_lambda g_ab
                - (1/2)( g_{a(mu} g_{nu)b} - (1/2) g_ab g_{mu nu} )
                - (1/2)( (d_mu g)_{ar} g^{rs} (d_nu g)_{sb} + (d_nu g)_{ar} g^{rs} (d_mu g)_{sb} )
```

where `Gammabar` is the ordinary Christoffel symbol of the **induced** metric
`gbar_{mu nu} = g_{mu nu} + V_g(d_mu g, d_nu g)` (V_g = the trace-reversed
Frobenius pairing, Prop 2.1), *not* of `g` itself.

This is not a new schematic guess. It is the **third** independent arrival at
the same closed form: `ii-s-coordinate-formula-2026-06-23.md` §4 wrote it down
by hand (unverified, "convention choice remains" in its own verdict); this
artifact re-derives it from scratch via the Koszul identity on the ambient
metric and certifies it by an independent theorem (§1.3), not by comparison
to that file. The two match exactly.

**Grade.** EXACT sympy throughout. Five of six ambient Christoffel blocks
verified fully symbolically at a general fiber point; the sixth via an
exact-rational solve at three points (§1.1, §5 — narrower scope, stated
honestly, not hidden). The assembled formula is certified by the
orthogonality theorem across 520 exact checks (§1.3), not merely asserted.
The FC-VZ-4 characteristic computation (§3) is an exact but **toy** Cl(3,1)
model — it does not repeat vz-subprincipal's own 128-dimensional Cl(9,5)
RS-sector computation, and says so.

**FC-VZ-4 verdict.** **No spacelike sourcing found.** A background
(`xi`-independent) endomorphism built from an actual II_s sample cannot
change the leading (degree-4-in-`xi`) part of the RS characteristic
determinant — an exact linear-algebra fact (any factor drawn from the
inserted endomorphism instead of the principal symbol lowers the `xi`-degree
by at least one in the Leibniz expansion), confirmed concretely, not merely
asserted abstractly. This is the **same** structural reason
`vz-subprincipal-symbol-rs-2026-06-23.md` §7 Argument 1 already gave (real
principal type / Hörmander propagation) — this artifact grounds that
argument in an actual II_s number for the first time, and adds the required
contrary control proving the check is not vacuous (§3.3). The 4D leg's
verdict **HARDENS at reconstruction grade**; it does not move to VERIFIED
(that requires the full Cl(9,5) RS Schur-complement computation with II_s
plugged in explicitly — not attempted here — plus resolution of
REDUCTION-FIDELITY, out of scope by this arc's own instruction).

```gu-typed-objects
result:         II_s(d_mu,d_nu), the explicit closed-form second fundamental
                form of the graph section, certified via the Gauss-formula
                orthogonality theorem
carrier:        II_s(d_mu,d_nu) in Sym^2(T*_x X^4), the tautological vertical
                tangent space of Y^14=Met(X^4) LAYER=ambient CHIRALITY=N/A
pairing:        Gauss-formula normal projection (ambient covariant derivative
                minus the induced-metric tangential part) ON=Gcal (the (9,5)
                gimmel metric on Y^14, block-diagonal coordinate-patch
                convention, SS2.2)
real_structure: exact rational/sympy symmetric tensor; no complex or
                quaternionic structure anywhere in this computation
grading:        S^2 T*X^4 (base pair mu,nu) tensor Sym^2 T*X^4 (fiber pair
                a,b) -- matches Prop 7.2's stated codomain exactly
action_owner:   repository-construction (fresh Koszul-identity derivation
                this pass; independently cross-checked against
                ii-s-coordinate-formula-2026-06-23.md SS4 and
                pc2-met-x4-bundle-formalization-stub-2026-06-22.md SS2)
target:         s*(theta), Prop 7.2's reconstruction-grade identification
                s*(theta) = II_s MAP-TYPE=contraction
```

```gu-typed-objects
result:         FC-VZ-4 subprincipal verdict -- a background II_s-sourced
                endomorphism cannot alter the leading characteristic variety
                of the 4D RS operator symbol
carrier:        det(M(xi)+K), a scalar polynomial on T*X^4; M(xi)=xi_mu
                gamma^mu built from exact Cl(3,1) gamma matrices, K a 4x4
                sample of the computed II_s LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing:        characteristic determinant / top-degree-in-xi extraction
                ON=T*X^4 (the 4D cotangent space at a point)
real_structure: exact Gaussian/rational Cl(3,1) representation (4x4 Dirac);
                explicitly NOT the repository's Cl(9,5), S=H^64 carrier
grading:        homogeneous-degree filtration in xi (principal = degree 4,
                subprincipal/background insertion = degree 0)
action_owner:   repository-construction (toy structural model; does NOT
                re-derive vz-subprincipal-symbol-rs-2026-06-23.md's own
                Cl(9,5)/128-dim RS Schur-complement computation)
target:         the 4D RS effective operator's characteristic variety
                {det S_R^4D(xi) = 0} MAP-TYPE=not-a-map
```

## 1. PREFLIGHT — retrieval before the work, and six problem-matched lenses

**Retrieval run before any derivation.** Searched (grep, whole repo, not just
`explorations/vz-evasion/`): `II_s`, `s\*(θ)`, `s\*theta`, `second fundamental
form`, `extrinsic curvature`, `DeWitt supermetric`, `gimmel metric`,
`Ehresmann`, `horizontal distribution`. Found and read in full before writing
any sympy: `explorations/geometry-curvature-emergence/ii-s-coordinate-formula-2026-06-23.md`
(a prior, **unverified**, hand-derived attempt at exactly this coordinate
formula — "CONVENTION_CHOICE_REMAINS"), `ii-s-moving-frames-2026-06-23.md`
(a *different* convention — "horizontal-normalized", giving `II_s^H=0` for
tautological sections — built for a separate cross-program dark-energy
question, not for OQ2/Prop 7.4), `pc2-met-x4-bundle-formalization-stub-2026-06-22.md`
(the gimmel metric's explicit construction, §2), `codazzi-sp64-bundle-2026-06-23.md`
(the abstract Gauss-Codazzi-Ricci system, `B=II_s` schematic, no coordinate
formula), and `vz-subprincipal-symbol-rs-2026-06-23.md` (the subprincipal-symbol
machinery this artifact's FC-VZ-4 argument extends). **This is not a first
discovery of the coordinate-formula question** — it is the third pass, and the
first to (a) verify every Christoffel block against an independent identity
and (b) certify the assembled result against a theorem rather than by
inspection.

**Lens 1 — submanifold geometer.** Predicted: "the second fundamental form of
an embedding" has one standard meaning (ambient `nabla` minus the induced
connection's tangential part), and Prop 7.4's Gauss equation is written as
"the standard result... applied to the embedding" with no normalization
caveat — so the *literal graph* convention, not the *horizontal-normalized*
one ii-s-moving-frames.md uses for a different purpose, must be the one Prop
7.2/7.4 intend. **Confirmed** (§1.4): the horizontal-normalized convention
would need an extra correction term inside the Gauss equation, contradicting
Prop 7.4's plain "standard result" language.

**Lens 2 — symbolic-computation hygienist.** Predicted: a fully general
10-free-symbol closed-form inverse of the DeWitt-type vertical metric will be
computationally intractable (huge rational expressions, `simplify()`
timeouts). **Confirmed, and worse than predicted**: not only did the naive
approach blow up (a single derivative of one entry reached ~450,000
characters), the fully-symbolic Koszul check for the *hardest* block (V-V-V)
produced a **false nonzero residual** from `sympy.simplify()` failing to
recognize a true zero in the fully-expanded 10-variable rational form — caught
only by re-verifying via exact-rational solves at concrete points (§5). Logged
as a real finding, not smoothed over.

**Lens 3 — hyperbolic-PDE / characteristic analyst.** Predicted: since `II_s`
is built purely from the background section `g(x)` (never from the dynamical
RS field or from `xi`), it can only ever enter the 4D operator as a
`xi`-independent (zeroth-order, subprincipal) endomorphism, **regardless of
how many x-derivatives of `g` it contains** — so by the same Hörmander
real-principal-type argument `vz-subprincipal-symbol-rs-2026-06-23.md` §7
already used for the Weyl/Shiab terms, no new characteristics can appear, and
this should hold for *any* well-formed background insertion, not something
special to `II_s`. **Confirmed** (§3.2); the interesting content added here is
the concrete instantiation and the required contrary control, not a new
theorem.

**Lens 4 — drafts-file convention auditor.** Predicted a clash: the drafts
file's own words are "a function of `s` and its first derivatives"
(`papers/drafts/canonical-structures-14d-metric-geometry-2026-06-22.md:398`),
but a graph-type second fundamental form is a textbook **second**-order object
(compare: the second fundamental form of a graph hypersurface `z=f(x)` is
`d^2f`, not `df`). **Confirmed** (§1.5): the explicit formula depends on `g`,
`d g`, **and** `d^2 g`, and this artifact's own derivative-order audit (a
planted-control-guarded test, not a footnote) demonstrates the `d^2g`
dependence is load-bearing, not a removable artifact of one convention
choice.

**Lens 5 — adversarial / hostile reader.** Predicted the single weakest joint
is the coordinate-patch choice itself (`Gcal` block-diagonal in `(x^mu,u_I)`,
no horizontal-vertical shift term) — is this pinned down by the source
material, or is it an interpretive choice that could be hiding sourcing
behind a convenient gauge? **Partially confirmed**: it is not fully pinned in
the drafts file's own text (which never writes the shift term down one way or
the other), but it *is* the convention already used, independently, by both
`pc2-met-x4-bundle-formalization-stub-2026-06-22.md` §2.4 ("Working
assumption for the horizontal piece... this is the tautological assignment")
and `ii-s-coordinate-formula-2026-06-23.md` §1 ("product coordinate gauge") —
this artifact does not introduce a new convention, it reproduces the one
already on record twice. See §4 for the blunt paragraph on what this
buys and does not buy.

**Lens 6 — retrieval / novelty-check.** Predicted `II_s` would appear under
several names across the K77 corpus and a naive derivation would silently
duplicate or contradict prior work. **Confirmed** (this section's own
retrieval log) — and refined into an actual finding: the two prior attempts
(`ii-s-coordinate-formula`, hand-derived, unverified; `ii-s-moving-frames`, a
different convention for a different question) are neither duplicated nor
silently contradicted here; §0 states exactly how this artifact relates to
each.

## 1.1 Coordinate conventions, quoted exactly

From the drafts file (`papers/drafts/canonical-structures-14d-metric-geometry-2026-06-22.md`):

> §2.1: "the fiber over `x` ∈ X⁴ is `π⁻¹(x) = { g_x ∈ Sym²(T_x*X⁴) : g_x` has
> signature `(3,1) }`... an open subset of the 10-dimensional vector space
> Sym²(T_x*X⁴)."

> Prop 2.1: "The fiber Sym²(ℝ^{3,1}*) equipped with the Frobenius inner
> product `⟨A,B⟩_F = tr(g⁻¹A·g⁻¹B)` has signature (7,3). After applying the
> trace-reversal map `Â_{μν} = A_{μν} − ½(tr_g A) g_{μν}`, the inner product on
> the image has signature (6,4)."

> Corollary 2.2: signature`(Y¹⁴) = (6+3, 4+1) = (9,5)`.

> Prop 7.2 (`[reconstruction grade]`): "the pullback `s*(θ)` coincides with
> the second fundamental form of the embedding `s: X⁴ → Y¹⁴`: `s*θ = II_s ∈
> Γ(S²T*X⁴ ⊗ Sym²T*X⁴)`."

> §7.2 (the target of this artifact): "**Explicit formula for II_s:** The
> second fundamental form `II_s ∈ Γ(S²T*X⁴ ⊗ Sym²T*X⁴)` has not been computed
> in coordinates as a function of `s` and its first derivatives."

**§1.4 — why the literal-graph convention, not the horizontal-normalized
one.** Prop 7.4 states the Gauss equation as "a standard result in
Riemannian geometry (Gauss equation for immersed submanifolds) applied to the
embedding" with no caveat. The standard Gauss equation is only valid, without
extra correction terms, for the ordinary (unnormalized) second fundamental
form of an embedded submanifold — exactly the object computed in §2 below.
The alternative convention in `ii-s-moving-frames-2026-06-23.md` (subtracting
an "algebraic slice" reference term, giving `II_s^H=0` for tautological
sections) was built for a *different* purpose — a cross-program dark-energy
Tikhonov-parameter contact (`CPA-1`), not the OQ2/Gauss-Codazzi mainline —
and would require Prop 7.4 to carry an unstated correction. This artifact
therefore uses the literal-graph convention as primary, consistent with both
prior explorations that touch the coordinate formula specifically.

**§1.5 — the derivative-order finding.** The formula in §0 depends on `g`,
`∂g`, **and** `∂²g`. The drafts file's own phrasing ("a function of `s` and
its first derivatives") is not matched literally by the standard mathematical
object it names. This is not a contradiction requiring anyone to be wrong —
"second fundamental form" is, by the ordinary meaning of the term, a
second-order construction (§1 Lens 4) — but it is worth stating plainly
rather than silently building a different, first-derivative-only object to
match the prose. `test_b3_derivative_order_audit` in the probe demonstrates
this concretely: two sections agreeing in `g` and `∂g` at a point but
differing in `∂²g` produce **different** `II_s` at that point.

## 2. The computation

### 2.1 The gimmel metric, in adapted bundle coordinates

Adapted coordinates `(x^μ, u_I)`, `I` indexing the 10 independent components
of a symmetric 4×4 tensor (matching VZ-4's `SYM_PAIRS` convention exactly, so
this artifact composes with VZ-4's without a translation layer). In this
chart, **block-diagonal, no horizontal-vertical shift term**:

```
Gcal_{mu nu}(u) = H_{mu nu}(u)          [the fiber point itself is the (3,1) horizontal metric]
Gcal_{mu,I}(u)  = 0                     [no cross term]
Gcal_{I J}(u)   = V_{IJ}(u)             [trace-reversed Frobenius, Prop 2.1, signature (6,4)]
```

This is not a fresh choice; it reproduces `pc2-met-x4-bundle-formalization-stub-2026-06-22.md`
§2.4's "working assumption for the horizontal piece" and
`ii-s-coordinate-formula-2026-06-23.md` §1's "product coordinate gauge",
independently re-derived rather than copied.

### 2.2 The six Christoffel blocks — each independently verified

Six blocks by (upper index type) × (lower index-pair type ∈ {HH,HV,VV}):

| block | formula | verification | checks |
|---|---:|---|---:|
| `Γ^ρ_{μν}` (H,HH) | `0` | by construction (Gcal has no explicit x-dependence) | — |
| `Γ^{ab}_{μν}` (V,HH) | `-(1/2)( g_{a(μ}g_{ν)b} - (1/2)g_{ab}g_{μν} )` | Koszul, lowered, general symbolic `H` | 100/100 |
| `Γ^ρ_{μ,ab}` (H,HV) | `(1/2) g^{ρσ} δ^{ab}_{σμ}` | Koszul, lowered, general symbolic `H` | 40/40 |
| `Γ^{cd}_{μ,ab}` (V,HV) | `0` | by construction | — |
| `Γ^ρ_{ab,cd}` (H,VV) | `0` | by construction | — |
| `Γ^{ef}_{ab,cd}` (V,VV) | `-(1/2)(k g^{-1} l + l g^{-1} k)` for `k,l` the two symmetric inputs | Koszul, exact-rational **solve** at 3 generic points | 165/165 |

The "by construction" rows follow because `u` is an independent fiber
coordinate in this chart (not tied to any section) — a Koszul RHS built purely
from `∂/∂x^μ` of a function of `u` alone is identically zero (verified
structurally, not by a computation that could hide a sign error).

**The V-V-V block's trace-reversal cancellation.** The naive (un-reversed
Frobenius) connection formula `-(1/2)(k Hinv l + l Hinv k)` turns out to be
**exactly** the connection of the *trace-reversed* metric `V` too — the
trace-correction term cancels in the connection, confirmed by solving the
full 10×10 Koszul linear system exactly at three independent generic
rational points and finding the naive candidate matches to the last digit
every time (165/165, zero residual). This matches a claim already on record
in `pc2-met-x4-bundle-formalization-stub-2026-06-22.md` §2 ("the
trace-reversal term cancels... in the inverse metric") — here it is checked,
not merely asserted.

### 2.3 Assembling II_s and the orthogonality certificate

For `s(x)=(x,g_ab(x))`, `T_μ = ds(∂_μ)`. The ambient covariant derivative
`∇_{T_μ}T_ν` is computed via the standard pullback-connection formula (the
six blocks of §2.2, evaluated at `u=g(x)`, contracted with `T_μ,T_ν`). The
tangential part is fixed by `Γ̄`, the ordinary Christoffel symbol of the
*induced* metric `ḡ_{μν}=g_{μν}+V(∂_μg,∂_νg)` — **not** of `g` itself (a
distinction `ii-s-coordinate-formula-2026-06-23.md` §3 already flagged: "older
4D-reduction notes often write `s*(Gcal)=g`. That is true only after
projecting to the horizontal part... For the literal graph immersion, the
induced metric is `ḡ=g+V_g(∂g,∂g)`.").

```
II_s(∂_μ,∂_ν) := ∇_{T_μ}T_ν  −  Γ̄^ρ_{μν} T_ρ
```

**The certificate.** For *any* embedded submanifold with the ambient
Levi-Civita connection, `II_s` is automatically valued in the normal bundle:
`Gcal(II_s(∂_μ,∂_ν), T_σ) = 0` for every `σ`. This is not an assumption; it is
a theorem (the Gauss formula), and a wrong implementation of any of the
pieces above generically fails it. Checked exactly, rational arithmetic, for
5 sections (flat, and four independently varied non-flat sections spanning
linear/quadratic, single-entry/multi-entry perturbations) × up to 3 points
each (the flat section is x-independent, one point suffices) = 13
(section, point) cases × 10 independent `(μ,ν)` pairs × 4 `σ` = **520 exact
zero-checks, 0 failures** (`test_b1_orthogonality_theorem_all_sections`).

## 3. FC-VZ-4 — does II_s source spacelike characteristics at subprincipal order?

### 3.1 The question, precisely, and the domain check it does NOT need

**PD-ULTRAHYPERBOLIC-DOMAIN discharged by scope, per the frontier's own
note.** `lab/process/path-dependencies.md`'s `PD-ULTRAHYPERBOLIC-DOMAIN`
warns that the **ambient** `Y^14` operator (signature `(9,5)`, five time
directions) has an ill-posed-by-default Cauchy problem, and that no citation
of ordinary (one-time-direction) Lorentzian boundary-value theory may be
assumed for it without supplying a domain explicitly. Nothing in this
artifact is a claim about the ambient operator's domain or well-posedness:
every characteristic-determinant computation in this section is about the
**4D reduced** operator `D_GU^{4D}` on `(X^4, ḡ)`, signature `(3,1)`, a single
time direction, ordinary Lorentzian — exactly the operator
`vz-subprincipal-symbol-rs-2026-06-23.md` itself works with. The 4D
section-level scope of this entire artifact discharges the check by
construction: there is no ultrahyperbolic object anywhere in §3's argument
for the domain check to apply to.

`canon/no-go-class-relative-map.md`'s FC-VZ-4: *"`II_s = s*(θ)` (the extrinsic
curvature of the section embedding) sources an effective first-order term in
`S_R^{4D}` producing spacelike characteristics."* The 4D leg is held at
CONDITIONALLY_RESOLVED specifically because this check was open
(`vz-subprincipal` found no such sourcing for the *other* zero-order terms —
Weyl curvature, Sp(64) gauge curvature, Shiab coupling — "but at
reconstruction grade only, which is exactly why the 4D leg is held at
CONDITIONALLY_RESOLVED rather than VERIFIED").

### 3.2 The structural argument, now grounded in an actual formula

`II_s` is built purely from the background section `g(x)` and its
derivatives — never from the dynamical RS field, never from `ξ`. Any tensor
built this way can only enter the 4D operator `D_GU^{4D}` as a **zeroth-order
endomorphism** (a matrix multiplying the field, not differentiating it),
regardless of how many `x`-derivatives of `g` it contains (§1.5's finding
about `∂²g` is irrelevant to this point — differentiability of the
*background* is not differentiation of the *field*).

For a first-order (Dirac-type) operator with principal symbol `M(ξ)` and a
`ξ`-independent addition `K`, the characteristic determinant `det(M(ξ)+K)` is
a polynomial in `ξ` of degree ≤ N; its **top-degree** (here degree 4) part
comes *only* from choosing `M(ξ)` in every factor of the Leibniz expansion —
any factor drawn from `K` instead lowers the `ξ`-degree of that term by at
least one. So the leading/principal characteristic variety — the only thing
Hörmander's propagation-of-singularities theorem cares about for a
real-principal-type operator — is **unchanged by any bounded background
insertion**, full stop, independent of what `K` actually is.

This is exactly `vz-subprincipal-symbol-rs-2026-06-23.md` §7 Argument 1
(Hörmander real principal type), stated there abstractly for the Weyl/Shiab
terms. What is new here is grounding it in an **actual** `II_s` number:

```
test_c3_zeroth_order_no_new_characteristics:
    K = II_s vertical part, section="richer", point=(1/2,-1/3,2/5,1/7), (μ,ν)=(0,0)
    M(ξ) = ξ_μ γ^μ, exact Cl(3,1) gamma matrices, {γ^μ,γ^ν}=2η^{μν}, η=diag(-1,1,1,1)
    deg_4[det(M(ξ)+K)]  ==  det(M(ξ))  ==  (η·ξ·ξ)²          EXACTLY
```

**Verdict: no spacelike sourcing.** Confirmed with the real computed data,
not a placeholder matrix.

### 3.3 The two required contrary controls

**(i) A section where II_s provably ≠ 0.** The flat Minkowski section
(`g_ab` constant, `∂g=0` identically) still has `II_s ≠ 0`:

```
II_s(∂_0,∂_0) has horizontal part = 0, vertical part = -(1/2)(η_{a(0}η_{0)b} - (1/2)η_ab η_00)
  entry (a,b)=(0,0): -1/4     entries (a,b)=(1,1),(2,2),(3,3): -1/4 each
```

exactly, independently of `x` (this section has no `x`-dependence at all).
This reproduces — independently, and now exactly-certified rather than
hand-derived — `ii-s-coordinate-formula-2026-06-23.md` §6.1's finding
("constant sections are not automatically totally geodesic... it comes from
`∂_{h_ab} Gcal_{μν} ≠ 0`"). `test_b2_contrary_control_flat_section_nonzero`
plants the false claim "flat `II_s` = 0" under `MUT=flat_contrary_control_vacuous`
and confirms it drives a genuine assertion failure, not a vacuous pass.

**(ii) An artificial configuration where spacelike sourcing WOULD occur.** The
argument in §3.2 depends entirely on the inserted term being `ξ`-independent.
To prove the detector can actually tell the difference — not just always
report "safe" — `test_c4` **artificially promotes** a background term
(`K=γ⁰`, chosen minimal and deliberately not claimed to arise from `II_s`) to
first order via `K_bad(ξ) := (n·ξ)·K` for a fixed covector `n=(0,0,0,1)`:

```
at ξ = (0,0,0,1):
  η·ξ·ξ = 1                       (SPACELIKE, exactly)
  det(M(ξ))          = 1          (nonzero: this point is NOT already characteristic)
  det(M(ξ)+K_bad(ξ)) = 0          (EXACTLY zero: a NEW spacelike characteristic)
```

confirmed in fully general closed form too:
`det(M(ξ)+K_bad(ξ)) = (η·ξ'·ξ')²` with `ξ'=(ξ_0+ξ_3,ξ_1,ξ_2,ξ_3)` — literally
the same operator as `M` evaluated at a rescaled covector, whose null cone is
a genuinely different quadric. The mechanism generating the defect (a
covariant-order bookkeeping slip promoting a background term to a derivative
term) is exactly the class of error this whole VZ chain polices — it is the
FC-VZ-4 failure condition **made concrete**, not a strawman.

## 4. Blunt paragraph on the generality of the coordinate patch

**The strongest attack, named against itself.** Is the coordinate patch
(block-diagonal `Gcal`, no horizontal-vertical shift term) general enough to
carry the "no sourcing" conclusion, or does it hide sourcing behind a
convenient gauge? Two honest things are true simultaneously. First, within
this coordinate patch, the *section* `g_ab(x)` is fully general — a
completely arbitrary smooth (here: sympy `Function`) map, verified for five
structurally different sections and confirmed as a genuine 2-jet dependence
(§1.5), so nothing about the section itself is special-cased. Second, the
*ambient chart* is a specific, non-canonical choice: there is no proof in
this artifact, nor in either of the two prior explorations that use the same
convention, that a different Ehresmann connection on `Y^14 → X^4` (a nonzero
horizontal-vertical shift term) would leave the leading FC-VZ-4 conclusion
unchanged. The §3.2 structural argument is, however, largely convention-robust
on its own terms: it depends only on `II_s` being *some* `ξ`-independent
tensor built from the background section (true in any Ehresmann gauge, since
a connection choice changes the *formula* for `II_s` but not its status as a
zeroth-order background insertion into a first-order dynamical operator). What
is *not* convention-robust is the §0 closed-form formula itself and the exact
numbers in §3.3(i) — a different horizontal-vertical shift would change both.
Anyone extending this to a different gauge should re-run §2.3's orthogonality
certificate before trusting the new formula; it is cheap (0.2s per sweep) and
it caught a real bug here (§5).

## 5. POSTFLIGHT — six lenses, after the work

**P1 — verdict-inflation auditor.** Did this artifact overclaim? Checked
against three specific risks: (a) the VVV block is graded "exact-rational
sweep at 3 points", not "fully general symbolic", and §2.2's table says so in
the same row rather than in a footnote; (b) the FC-VZ-4 carrier block
explicitly declares `LAYER=toy` and states in prose it does not re-derive
vz-subprincipal's own Cl(9,5) computation; (c) `target_claim_verdict` says
"HARDENED, not upgraded" and explicitly defers the canon-verdict call to the
integration owner, per this arc's own instruction.

**P2 — under-repair / left-a-defect-standing auditor.** Two things are
knowingly left open, both declared in frontmatter: `REDUCTION-FIDELITY`
(untouched, out of scope by instruction) and `CODAZZI-SP64-EXPLICIT` (this
artifact supplies an input OQ2 would need, not OQ2 itself). A third,
un-declared-until-now item: the `ii-s-moving-frames-2026-06-23.md`
"horizontal-normalized" convention is not reconciled with this artifact's
choice beyond the textual argument in §1.4 — a reader who needs *that*
convention's coordinate formula does not get one here.

**P3 — over-repair auditor.** No file outside the two declared write paths
was touched. No canon, drafts, or other-agent-owned directory was edited
(shared checkout; this pass only wrote its own two paths, no git operations
performed).

**P4 — the bug-and-fix narrator.** The orthogonality certificate is not
decorative. During development, an initial implementation of `∂_λ ḡ_{μν}`
mis-indexed a `sympy.Matrix` — `g2[λ][μ][ν]` (flat single-index access into a
4×4 `Matrix`, silently returning a row-major-flattened entry instead of the
intended `∂_λ∂_μ g_{ν·}`-shaped object) where the correct term was simply
`g1[λ][μ,ν]` (one derivative, not a mis-shaped access into the second-derivative
structure). This produced a **constant**, section-independent residual (exactly
`1/6`) in the orthogonality check for every non-flat test section — the tell
that revealed it was a fixed structural bug rather than an accumulating
numerical one. Diagnosis proceeded by isolating raw `∇_{T_μ}T_ν}` from the
`Γ̄`-subtraction step, ground-truthing individual Christoffel components by an
independent perturbative computation at a concrete point, and finally
hand-verifying the exact RHS the buggy helper should have produced (`10/27`,
confirmed by hand) against what it actually produced (`1/27`). Fixed, re-run:
520/520 exact zero-checks, 0 failures. This is reported at this level of
detail because a reader who trusts "the certificate passed" without knowing a
real bug was caught by it is trusting a claim this artifact can actually back
up, not a hope.

A second, smaller self-correction belongs in the same honest ledger: the
first implementation of the `orthogonality_theorem_disabled` planted control
was itself vacuous (it hardcoded the checked *residual* to `0` instead of
corrupting the *assembly* the residual is supposed to catch breaking, so the
"corrupted" run still exited 0). `--selftest` caught this immediately (that
is what the clean-baseline-first, exit-1-required discipline is for), and it
was fixed to corrupt the `Gammabar` tangential subtraction instead, leaving
the live assertion to catch it. Neither bug survived to the final certificate
in §6, but both are named here rather than quietly rewritten out of the
history.

**P5 — reader-of-the-future.** The one sentence most needed: **II_s is now an
exact, orthogonality-certified closed form, provably nonzero even in flat
spacetime, and provably second-derivative-dependent — any future physical
interpretation of it (dark energy, a stress source, anything Codazzi-side)
must start from *this* formula, not from the schematic `B_{μν,ab}` placeholder
`codazzi-sp64-bundle-2026-06-23.md` used.**

**P6 — blast-radius / dependency auditor.** Direct consumers of a computed
`II_s`: `codazzi-sp64-bundle-2026-06-23.md` (OQ2, still schematic — this
artifact supplies its missing input, does not close it);
`ii-s-coordinate-formula-2026-06-23.md` (now independently confirmed, not
superseded — it is not edited, per the write-only-two-paths rule); canon's
FC-VZ-4 line (target of the verdict, not edited — integration is the owner's
call). Nothing in `lab/active-research/joe-directed/` outside this artifact's
own two files was read as authoritative without checking its own status
field.

## 6. Certificate

```
_local/cas-venv/bin/python tests/channel-swings/joe_directed_vz5_ii_s_subprincipal.py
    -> Ran 13 tests, OK, exit 0     (~32s)

_local/cas-venv/bin/python tests/channel-swings/joe_directed_vz5_ii_s_subprincipal.py --selftest
    -> clean baseline exit 0; 11/11 planted controls each drove exit 1; exit 0
```

One control (`orthogonality_theorem_disabled`) was caught VACUOUS on its
first implementation attempt (it hardcoded the orthogonality *residual* to
`0` instead of corrupting the *computation* the residual checks — the
assertion then trivially passed, exit 0, not the required exit 1) and was
corrected before this artifact was finalized: it now skips the `Gammabar`
tangential-subtraction step in the assembly while leaving the orthogonality
assertion itself untouched, so a genuinely broken assembly is what the still-live
check must catch. This self-correction is reported rather than silently
fixed, per this arc's own discipline about crash-catches and vacuous
controls.

Planted controls, each of which must fire (drive the clean-passing suite to
exit 1):

| control | plants |
|---|---|
| `pullback_is_projection` | VZ-4's own control, rerun on this artifact's independent [R]-reproduction |
| `hhv_block_wrong_sign` | flips the H-H-V Christoffel candidate's sign before the Koszul check |
| `vvv_block_missing_trace_term` | the un-reversed plain-Frobenius connection (drops the cancellation of SS2.2) |
| `orthogonality_theorem_disabled` | skips the Gammabar tangential subtraction in the assembly; the orthogonality assertion must catch it live |
| `flat_contrary_control_vacuous` | asserts the flat-section II_s vanishes (the false "totally geodesic" claim) |
| `derivative_order_claim_wrong` | asserts II_s depends on first derivatives only |
| `zeroth_order_theorem_wrong_degree` | checks degree 3 instead of degree 4 (wrong top-degree slot) |
| `adversarial_control_vacuous` | claims the adversarial control point is timelike, not spacelike |
| `clifford_relation_sign_flip` | flips a sign in the Clifford square, should not match `eta` |
| `quote_drift` | asserts a sentence not present in the drafts file |
| `routing_notice_missing` | asserts this artifact's routing notice is absent |

Exactness: every check above is exact `sympy.Rational`/`Integer`/exact matrix
arithmetic; the only non-exact objects touched anywhere are `sp.I` (exact
Gaussian-integer-style imaginary unit inside the Cl(3,1) gamma matrices,
algebraically exact, not a float) and ordinary symbolic differentiation. No
`float` literal appears in any load-bearing computation.

## 7. Claim ceiling, and every imported assumption

**Ceiling.** Purely kinematic/algebraic: an explicit tensor formula plus a
characteristic-determinant check on a toy carrier. It computes no action, no
propagator, no physical stress-energy, decides no fork among the open
residuals, and does not move a canon verdict or ledger row — `canonical_effect:
pending_integration` throughout.

Imported, each load-bearing somewhere:

1. **`Y¹⁴=Met(X⁴)` with fiber `Sym²(T_x*X⁴)`, signature (9,5) via Prop 2.1's
   trace-reversal** — repository-derived, not re-derived here (re-verified
   only insofar as the Christoffel-block computation reproduces it as a
   structural byproduct).
2. **The block-diagonal coordinate-patch convention for `Gcal`** (no
   horizontal-vertical shift) — declared, not proven canonical; matches two
   independent prior explorations (§1 Lens 5); §4 states plainly what this
   does and does not buy.
3. **The literal-graph (not horizontal-normalized) second-fundamental-form
   convention** — argued from Prop 7.4's own "standard result" language
   (§1.4), not independently forced.
4. **Prop 7.2's identification `s*(θ)=II_s`** — imported at its own stated
   reconstruction grade; not re-derived or re-argued here. This artifact
   computes `II_s`; it does not defend the identification with `s*(θ)`.
5. **`vz-subprincipal-symbol-rs-2026-06-23.md`'s Hörmander real-principal-type
   argument** — imported and reused (§3.2), not re-proven from first
   principles of microlocal analysis; the contribution here is grounding it
   in an actual `II_s` number and adding the required contrary control.
6. **Cl(3,1) toy carrier in §3, not the repository's Cl(9,5)/S=H^64 carrier**
   — declared explicitly (`LAYER=toy` in the typed block); the general
   argument (§3.2) is carrier-independent, but the concrete numbers in §3.3
   are specific to this toy embedding and would need re-deriving in the full
   128-dimensional module to become a repository-carrier-native result.
