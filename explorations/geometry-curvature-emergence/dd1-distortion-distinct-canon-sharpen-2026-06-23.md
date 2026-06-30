---
title: "DD1 — Distortion vs Torsion: IG-Equivariance Does Not Collapse Under Change of Frame"
date: 2026-06-23
problem_label: "dd1-distortion-distinct-canon-sharpen"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# DD1 — Distortion vs Torsion: The IG-Equivariance Is Frame-Stable

**Status.** Reconstruction grade. This sharpens the prior DD1 literature check
(`explorations/geometry-curvature-emergence/dd1-distortion-tensor-literature-check-2026-06-22.md`, PARTIALLY_NAMED) by
converting the loose claim "GU's θ is distinguished by IG-equivariance" into a precise,
testable cohomological statement, and by discharging the named failure condition: *does the
IG-equivariance collapse to a known torsion notion under a change of frame?* No result is
promoted to active_research or canon without meeting `RESEARCH-STATUS.md` criteria.

**Task.** Sharpen the distinction between two objects on the same data:

- **Torsion / contorsion** `T(∇) = ∇ − ∇_LC` — the classical difference tensor (Hehl
  contorsion, Agricola-Friedrich A, Cartan torsion-relative-to-LC).
- **Distortion** `D(∇, g) = ∇ − g·∇_LC` — the GU object, where `g·∇_LC` is the
  *gauge-transformed* Levi-Civita connection.

The prior file claimed these differ by IG-equivariance. The remaining danger, named in the
task: **if the IG-equivariance of D is just T written in a rotated frame, the novelty claim
collapses.** This file proves it does not — the obstruction to that collapse is a nonzero
group-cohomology class.

---

## §1. Precise definitions and the transformation laws

### 1.1 The two difference operators

Fix a principal `G`-bundle `P → Y¹⁴` (`G = Sp(64)`), a fixed reference (Levi-Civita)
connection `∇_LC ∈ Conn(P)` determined by the gimmel metric `ℊ`, and a variable connection
`∇ ∈ Conn(P)`. Both differences live in `Ω¹(Y¹⁴, ad P)`:

```
T(∇)       :=  ∇ − ∇_LC                       (torsion / contorsion)
D(∇, g)    :=  ∇ − g·∇_LC,   g ∈ G            (distortion)
```

where `g·∇_LC = Ad(g)∇_LC − (d_{∇_LC} g)·g⁻¹` is the gauge transform of `∇_LC` by a gauge
element `g ∈ G` (the gauge group `G = Γ(Ad P)`). The pair `(∇, g)` is exactly the data of an
inhomogeneous-gauge-group element acting on the reference, as set up in
`dark-energy-divergence-free-proof-2026-06-22.md` §1: with `ω = (ε, B) ∈ IG`, one has
`g = ε`, `∇ = ∇_LC + B`, and `D = π − Ad(ε⁻¹)B` with `π = ∇ − ε·∇_LC`.

### 1.2 The gauge transformation laws — the entire distinction lives here

Let `h ∈ G` act. The action on connections is `∇ ↦ h·∇`, and we must specify how the
*reference* and the *gauge label* `g` transform. There are two structurally different
references, and this is the whole point.

**(A) Torsion law.** Under `h`, `∇ ↦ h·∇` while `∇_LC` is a *fixed* connection that also
transforms as a connection, `∇_LC ↦ h·∇_LC`. Compute the difference of two transformed
connections:

```
T(h·∇) = h·∇ − ∇_LC                                    [∇_LC held fixed, NOT transformed]
       = Ad(h)(∇ − ∇_LC) + Ad(h)∇_LC − (d_{∇_LC}h)h⁻¹ − ∇_LC
       = Ad(h)·T(∇)  +  [Ad(h)∇_LC − ∇_LC − (d_{∇_LC}h)h⁻¹]
       = Ad(h)·T(∇)  −  D_{∇_LC} h · h⁻¹          (Maurer–Cartan defect)
```

The bracket is the covariant Maurer–Cartan 1-form `μ(h) := −(D_{∇_LC} h)·h⁻¹ ∈ Ω¹(Y, ad P)`.
So:

```
   T(h·∇) = Ad(h)·T(∇) + μ(h),     μ(h) = −(D_{∇_LC}h)·h⁻¹ ≠ 0  in general.   (T-LAW)
```

This is an **affine / inhomogeneous** transformation. `T` is *not* a tensor under `G`: the
inhomogeneous term `μ(h)` is the standard connection-difference anomaly.

**(B) Distortion law.** Under `h`, transform `∇ ↦ h·∇` AND drag the gauge label
`g ↦ hg` (this is the IG/τ⁺ rule: the reference `g·∇_LC` is carried along by the same `h`).
Then `g·∇_LC ↦ (hg)·∇_LC = h·(g·∇_LC)`, and the *same* Maurer–Cartan defect appears in
both terms and cancels:

```
D(h·∇, hg) = h·∇ − (hg)·∇_LC
           = [Ad(h)∇ − (d g')g'⁻¹]_{g'=h} − [Ad(h)(g·∇_LC) − (d h)h⁻¹]
           = Ad(h)·(∇ − g·∇_LC)
           = Ad(h)·D(∇, g).                                                  (D-LAW)
```

This is a **linear / homogeneous (tensorial)** transformation. `D` IS a tensor under `G`
acting via `τ⁺` (it transforms in the adjoint representation, matching Prop. 2.1 of the
divergence-free proof: the τ⁺-left factor cancels, the relevant factor acts by `Ad`).

### 1.3 The distinction, stated exactly

The single mathematical fact separating the two objects is:

> **(T-LAW) carries a nonzero inhomogeneous cocycle `μ(h)`; (D-LAW) does not.**

`T` is an affine object (a "connection-difference" that fails to be a tensor by the
Maurer–Cartan term). `D` is a genuine `ad P`-valued tensor. This is not a cosmetic
relabeling: it is the difference between a non-equivariant and an equivariant section. The
remaining question — the failure condition — is whether a change of frame can *remove*
`μ(h)` and thereby identify `D` with some `T` in a new frame.

---

## §2. The failure condition, made precise

The task's falsifier: *"if the IG-equivariance collapses to a known torsion notion under a
change of frame, the novelty claim fails."* We must define "change of frame" and "collapse"
sharply enough to test.

**Definition (change of frame).** A change of frame is a gauge transformation `k ∈ G`
(equivalently a new local trivialization of `P`, or a new choice of reference connection
`∇_LC ↦ k·∇_LC`). A "collapse" would be the existence of a *single, ∇-independent*
`k ∈ G` such that, in the `k`-frame, the distortion `D(∇, g)` equals a standard
torsion `T̃(∇) = ∇ − ∇̃_LC` for some fixed reference `∇̃_LC`, *for all `∇`*, with `T̃`
transforming by (T-LAW) — i.e. such that the IG-tensoriality of `D` is revealed to be the
ordinary affine non-tensoriality of `T̃` seen from a tilted frame.

**Reformulation as a cohomological question.** Define the maps `G → Ω¹(Y, ad P)`:

```
α: h ↦  μ(h) = −(D_{∇_LC}h)·h⁻¹        (the torsion cocycle)
β: h ↦  0                               (the distortion cocycle)
```

Each is a **1-cocycle** of `G` acting on the `G`-module `M = Ω¹(Y, ad P)` (action `Ad`),
because both `T` and `D` are sections that transform by `(value) ↦ Ad(h)(value) + cocycle(h)`,
and the cocycle condition

```
c(h₁h₂) = Ad(h₁)c(h₂) + c(h₁)              (CO)
```

is exactly the consistency of iterated transformations. One checks `α` satisfies (CO):
`μ(h₁h₂) = −(D_{∇_LC}(h₁h₂))(h₁h₂)⁻¹ = Ad(h₁)μ(h₂) + μ(h₁)` by the Leibniz/Maurer–Cartan
identity for `D_{∇_LC}`. And `β ≡ 0` trivially satisfies (CO).

A "change of frame by `k`" shifts a transformation law by a **coboundary**: replacing the
reference value by `(value) − ζ` with a fixed `ζ ∈ M` sends the cocycle `c(h) ↦ c(h) +
(Ad(h)ζ − ζ)`. The map `h ↦ Ad(h)ζ − ζ` is the 1-coboundary `∂ζ`.

> **Collapse ⟺ `[α] = [β]` in `H¹(G; M)`**, i.e. `α` and `β=0` differ by a coboundary
> `∂ζ` for a single fixed `ζ ∈ Ω¹(Y, ad P)` independent of `∇`. Equivalently: `α = ∂ζ`,
> i.e. `α` is a **coboundary** and hence `[α] = 0 ∈ H¹(G; M)`.

So the entire novelty claim reduces to one statement:

> **NOVELTY ⟺ `[α] ≠ 0` in `H¹(G; Ω¹(Y, ad P))`** (the torsion cocycle is
> not a coboundary; no single frame change trivializes it).

This is the load-bearing computation. If `[α] = 0`, the failure condition fires and the
novelty collapses. If `[α] ≠ 0`, the IG-equivariance is frame-stable and genuinely new.

---

## §3. The torsion cocycle `α` is not a coboundary: `[α] ≠ 0`

We prove `[α] ≠ 0` by exhibiting an obstruction that a coboundary cannot carry. Three
independent arguments; each suffices, and they are mutually consistent.

### 3.1 Curvature obstruction (the decisive one)

A coboundary `∂ζ(h) = Ad(h)ζ − ζ` is generated by a *fixed* `ζ ∈ Ω¹(Y, ad P)` (a single
1-form, no derivatives of `h`). The torsion cocycle `α(h) = −(D_{∇_LC}h)·h⁻¹` is the
Maurer–Cartan form pulled back through `∇_LC`; it depends on the *derivative* `D_{∇_LC}h`,
not on `h` pointwise. The two are distinguished by an invariant: take the covariant
exterior derivative `D_{∇_LC}` and read the curvature.

Compute `D_{∇_LC} α(h)` using the structure equation `D_{∇_LC}((D_{∇_LC}h)h⁻¹) =
F_{∇_LC} − Ad(h)F_{∇_LC} + ((D_{∇_LC}h)h⁻¹) ∧ ((D_{∇_LC}h)h⁻¹)`. The curvature-difference
piece is the salient invariant:

```
the α-cocycle "sees" the reference curvature F_{∇_LC}: its covariant derivative
contains the term  (Ad(h) − 1)F_{∇_LC}.
```

A coboundary `∂ζ(h) = (Ad(h) − 1)ζ` has covariant derivative `D_{∇_LC}∂ζ(h) =
(Ad(h)−1)D_{∇_LC}ζ − (D_{∇_LC}Ad(h))ζ`; the `(Ad(h)−1)`-weighted piece is `(Ad(h)−1)D_{∇_LC}ζ`,
controlled entirely by the *exact* 2-form `D_{∇_LC}ζ`. For `α = ∂ζ` to hold we would need

```
(Ad(h) − 1) F_{∇_LC} = (Ad(h) − 1) D_{∇_LC}ζ   for all h ∈ G
  ⟹  (Ad(h) − 1)(F_{∇_LC} − D_{∇_LC}ζ) = 0      for all h ∈ G
  ⟹  F_{∇_LC} − D_{∇_LC}ζ ∈ (Ω²(Y) ⊗ ad P)^{Ad(G)},
```

the pointwise `Ad(G)`-invariant subspace of the fibre. **Fixed-point step (made explicit).**
At each point `y ∈ Y`, the fibre is `Λ²T*_yY ⊗ (ad P)_y` and `Ad(G)` acts only on the second
tensor factor `(ad P)_y ≅ sp(64)`. A vector `v ∈ sp(64)` satisfies `Ad(h)v = v` for *all*
`h` in the connected group `G` iff `[ξ, v] = 0` for all `ξ ∈ sp(64)` (differentiate `Ad(exp tξ)v
= v` at `t = 0`; connectedness makes the infinitesimal condition equivalent to the global one),
i.e. iff `v ∈ Z(sp(64))`. So `(ad P)_y^{Ad(G)} = Z(sp(64)) ⊗ 1`, hence
`(Ω²⊗ad P)^{Ad(G)} = Ω²(Y) ⊗ Z(sp(64))`. Therefore

```
α = ∂ζ  ⟹  F_{∇_LC} = D_{∇_LC}ζ + (Z(sp(64))-valued 2-form).
```

For `G = Sp(64)` the algebra `sp(64) = sp(128,ℝ)`-type is **simple**, so `Z(sp(64)) = 0`
(the centre of `sp(2n)` vanishes for every `n ≥ 1`; equivalently the fundamental
representation is irreducible and faithful, so by Schur the only `Ad`-fixed vectors are `0`).
Hence `α = ∂ζ` would force `F_{∇_LC} = D_{∇_LC}ζ`, i.e. the reference curvature would be
`D_{∇_LC}`-*exact*. But `F_{∇_LC}` is `D_{∇_LC}`-*closed by the Bianchi identity*
`D_{∇_LC}F_{∇_LC} = 0` and generically *not exact* (its de Rham / Chern–Weil class
`[tr F_{∇_LC}^k] ∈ H^{2k}(Y¹⁴)` is generically nonzero — e.g. the second Chern / first
Pontryagin / instanton number of `P`). A `D_{∇_LC}`-exact 2-form has vanishing Chern–Weil
class, so the equality is impossible whenever `[F_{∇_LC}] ≠ 0`.

> **Conclusion.** `α = ∂ζ` ⟹ `[F_{∇_LC}]` is trivial in equivariant cohomology. Whenever
> the reference connection has nonzero characteristic class (generic `P`, and in particular
> any GU background with nonzero gauge instanton number, which is exactly the curvature-rich
> regime where the dark-energy θ is supposed to "come roaring out"), `[α] ≠ 0`.

This is the crux: **the torsion cocycle is cohomologically pinned to the curvature of the
reference connection.** A coboundary (one fixed `ζ`) is flat data; it cannot manufacture a
nonzero characteristic class. So no single change of frame trivializes `α`.

### 3.2 Locality / jet-order obstruction (independent, frame-free, and *fully rigorous*)

`α(h) = −(D_{∇_LC}h)h⁻¹` is a *first-order differential operator* in `h` (it depends on the
1-jet of `h`). A coboundary `∂ζ(h) = Ad(h)ζ − ζ` is a *zeroth-order* (pointwise algebraic)
operator in `h` (it depends only on the 0-jet `h(y)` and a fixed `ζ`). A first-order
operator cannot equal a zeroth-order operator unless its first-order part vanishes
identically. The first-order (symbol) part of `α` is `h ↦ −dh·h⁻¹` (the naive
Maurer–Cartan form), which is nonzero for any non-constant `h`. Therefore `α` is never a
coboundary, on any manifold `Y` admitting non-constant gauge transformations
(`dim Y = 14 > 0`, `G = Sp(64)` nonabelian connected). This argument is independent of the
choice of reference and of any frame — it is a statement about differential order that no
change of frame (itself a zeroth-order regauging plus a fixed reference shift) can alter.

**Infinitesimal form (this leg is verified, not reconstruction).** Restrict the cocycle
relation (CO) to the identity component and linearize at `h = e`. Writing `h = exp(tξ)`,
`ξ ∈ Lie(G) = Ω⁰(Y, ad P)`, the derivative `c'(ξ) := (d/dt)|_0 c(exp tξ)` of any group
1-cocycle is a **Lie-algebra 1-cocycle** of `Lie(G)` valued in the module `M = Ω¹(Y, ad P)`:
`c'([ξ,η]) = ξ·c'(η) − η·c'(ξ)` (the linearization of (CO)), and a group coboundary `∂ζ`
linearizes to the Lie-algebra coboundary `(∂ζ)'(ξ) = ξ·ζ = [ξ, ζ]` (action of `Lie(G)` on
`M` by the pointwise bracket). Compute the two linearizations:

```
α'(ξ) = −D_{∇_LC} ξ        (first order: the covariant differential of ξ)
(∂ζ)'(ξ) = [ξ, ζ]          (zeroth order: pointwise algebraic in ξ)
```

These cannot be equal for all `ξ`: pick `ξ` constant in a chart with `dξ ≠ 0` impossible — so
instead pick any `ξ` with `ξ(y₀) = 0` but `(D_{∇_LC}ξ)(y₀) ≠ 0` (always possible since
`dim Y = 14 > 0`). Then `(∂ζ)'(ξ)(y₀) = [0, ζ(y₀)] = 0` while `α'(ξ)(y₀) = −(D_{∇_LC}ξ)(y₀)
≠ 0`. Hence `α' ≠ (∂ζ)'` for every fixed `ζ`, so `[α'] ≠ 0` in `H¹(Lie(G); M)` already at the
infinitesimal/local level. Because the *restriction-to-infinitesimal* map sends group
coboundaries to Lie-algebra coboundaries, `[α'] ≠ 0 ⟹ [α] ≠ 0`. This step requires no
curvature input, no global topology, and no choice of frame — it is an exact statement about
the differential order (1 vs 0) of the two operators, decided pointwise at a single `y₀`. It
is the rigorous backbone underneath the curvature interpretation of §3.1.

### 3.3 Holonomy / global obstruction (independent)

Integrate `α` around a loop. The torsion cocycle's path-ordered integral is the holonomy of
`∇_LC` relative to `∇`; on a loop `γ ⊂ Y` enclosing nonzero `∇_LC`-flux, the holonomy
`Hol_γ(∇_LC) ∈ Sp(64)` is nontrivial. A coboundary integrates to a *pure gauge*
(trivial holonomy) contribution: `∫_γ ∂ζ = ∮_γ (Ad(h)−1)ζ`, which is exact and contributes
no net holonomy. Nontrivial reference holonomy ⟹ `[α] ≠ 0`. (This is the integrated form
of §3.1.)

### 3.4 Synthesis

All three arguments converge: `[α] ≠ 0` because the torsion cocycle encodes the *curvature*
`F_{∇_LC}` (3.1, global form 3.3) and is *first differential order* in `h` (3.2), whereas a
frame-change coboundary is flat, exact, and zeroth-order. Therefore the failure condition
**does not fire**: there is no change of frame `k ∈ G` that turns `D` into a standard
torsion `T̃`.

The three legs have different epistemic weights, which matters for the verdict:

- **§3.2 (jet-order / infinitesimal) is verified** and is the minimal sufficient argument:
  `[α'] ≠ 0 ∈ H¹(Lie(G); Ω¹(Y, ad P))` by an exact differential-order count, decided at one
  point, with no curvature, topology, or frame input. It alone proves `[α] ≠ 0` and hence
  proves non-collapse. *This is the leg that closes the named failure condition.*
- **§3.1 (curvature-pinning) is reconstruction-grade** and supplies the *interpretation*:
  the obstruction is the Chern–Weil class `[F_{∇_LC}]`, which ties non-collapse to exactly the
  curvature-rich regime where θ is physically invoked. It is the most informative leg.
- **§3.3 (holonomy) is the global integral** of §3.1 and is a consistency cross-check.

Because §3.2 already settles the binary question (`collapse` vs `no-collapse`) rigorously, the
*named failure condition is discharged at verified grade*; the residual reconstruction-grade
status of the file is about the finer **structure** of the class `[α]` (its identification with
the universal curvature class and the precise `H¹_{cont}(G; ·)` computation), not about whether
it is nonzero. This separation is reflected in the verdict reasoning of §6.

---

## §4. Why this is exactly the novelty vs Hehl / Agricola-Friedrich / Sharpe

The prior literature check established that all three frameworks define a difference tensor
`∇ − ∇_LC` and study its representation content. The sharpening here pins down *what they do
not have*, in one line each, using §1–§3.

| Framework | Their object | Its transformation law | Why it is `T`, not `D` |
|---|---|---|---|
| Hehl et al. (1995), distortion/contorsion `K, N` | `Γ − {Γ}` on the `GL(4)`-frame bundle of `X⁴` | covariant under the *finite-dimensional* structure group `GL(4)`/`SO(1,3)` only; affine (T-LAW) under any *infinite-dimensional* internal gauge group | They never gauge `{Γ}`; there is no `g·∇_LC`. Their `K` is `α`-type (carries the Maurer–Cartan defect under any would-be internal gauging). |
| Agricola-Friedrich (2003), contorsion `A` for skew torsion | `∇ − ∇_LC` on a *fixed* `(M,g)` | covariant under `O(n)` frame rotations; the metric `g` is fixed, so there is no gauge orbit of references | Same: `∇_LC` is rigid; `[α]` is never quotiented out; the object is `T`. |
| Sharpe (1997), Cartan torsion | `g/h`-part of `Ω = dω + ½[ω,ω]`, relative to the *flat model* `G/H` | equivariant under the *fixed Klein structure group* `H`; the model is rigid (single `G/H`) | The reference is the flat model, never gauge-transformed. No `g·(model)`; the construction has no IG. |

In every case the reference connection (or model) is **rigid**, so the relevant
transformation law is (T-LAW) and the object carries the nonzero class `[α]`. GU's move is
precisely to *gauge the reference* (`∇_LC ↦ g·∇_LC`) via the τ⁺ homomorphism, which by
(D-LAW) sets the cocycle to `β ≡ 0`. The content of §3 is that this is not achievable by a
frame change inside any of the three classical frameworks: `[α] ≠ 0`, so passing from `α` to
`0` is a genuine change of cohomology class, not a coboundary.

**One-sentence canonical statement of the novelty.**

> GU's distortion `D` is the unique representative in the IG-orbit of the difference tensor
> whose `G`-transformation cocycle is the coboundary-completed (zero) class; classical
> torsion/contorsion is the representative carrying the curvature-pinned class
> `[α] = [−(D_{∇_LC}·)·(·)⁻¹] ≠ 0 ∈ H¹(G; Ω¹(Y, ad P))`. The two are equal as set-theoretic
> *values* at any fixed `(∇, g=e)` but are inequivalent as *equivariant sections*; no frame
> change identifies them because `[α] ≠ 0`.

This both (a) justifies keeping the name "distortion" (Hehl's term, apt for the value) and
(b) isolates the new structure (the IG-coboundary completion / equivariance), with a precise
falsifier attached.

---

## §5. Consistency with the established `HC1` decomposition (no contradiction)

`HC1` (`hc1-hidden-curvature-components-2026-06-22.md`, open-Q1 resolved 2026-06-23) found
that `θ = D` decomposes into the **same** `SO(1,3)` irreducibles `T^{(1,2,3)}` as standard
torsion after section pullback to `X⁴`, with only the *coupling coefficients* and field
equations changed. This is fully consistent with §3, and the consistency is informative:

- **`SO(1,3)` is finite-dimensional and local (pointwise).** The irreducible-type
  decomposition is a statement about the *value* `D|_y ∈ ad P_y ⊗ T*_y` as an `SO(1,3)`-module
  at each point. Values of `D` and `T` live in the same module, so they share irreducible
  types. (This is the `g = e` agreement noted in §4's last sentence.)
- **`H¹(G; ·)` is about the infinite-dimensional gauge group `G` and is global/derivative.**
  The class `[α]` is invisible to the pointwise `SO(1,3)`-type decomposition; it lives in the
  *transformation law*, not in the *value*. HC1 explicitly says IG-equivariance "changes
  coupling coefficients and field equations but not irreducible types" — which is exactly the
  prediction of §3: the novelty is in the cocycle/equivariance layer, not in the
  representation-type layer.

So there is no tension: `D` and `T` have identical `SO(1,3)`-type content (HC1) and
inequivalent `G`-equivariance class (this file). These are orthogonal invariants. The novelty
claim was never that `D` decomposes into new tensor types; it is that `D` is the
frame-stable, IG-tensorial completion, and §3 proves that completion is non-coboundary.

---

## §6. Result and verdict

**Verdict: CONDITIONALLY_RESOLVED (reconstruction grade).**

**What is established.** The distinction between distortion `D = ∇ − g·∇_LC` and torsion
`T = ∇ − ∇_LC` is exactly the difference between the trivial cocycle `β ≡ 0` (D-LAW,
tensorial) and the curvature-pinned cocycle `α(h) = −(D_{∇_LC}h)h⁻¹` (T-LAW, affine) in
`H¹(G; Ω¹(Y, ad P))`. The named failure condition — *IG-equivariance collapses to a known
torsion notion under a change of frame* — is shown **not to fire**, because a frame change is
a coboundary and `[α] ≠ 0` by three obstructions of differing strength:
(i) the **verified** jet-order obstruction (§3.2): `α'(ξ) = −D_{∇_LC}ξ` is first
differential-order in `ξ` while a coboundary `[ξ, ζ]` is zeroth-order, so `[α'] ≠ 0 ∈
H¹(Lie(G); Ω¹(Y, ad P))` by a pointwise argument requiring no curvature, topology, or frame —
this alone discharges the failure condition; (ii) the **reconstruction-grade** curvature
obstruction (§3.1): `α` is cohomologically pinned to the reference curvature `F_{∇_LC}`, whose
characteristic class is generically nonzero and which a flat coboundary cannot carry
(`Z(sp(64)) = 0` makes the central escape unavailable) — this supplies the physical
interpretation; (iii) the holonomy obstruction (§3.3), the global integral of (ii). The
binary non-collapse result rests on (i) alone; (ii)–(iii) identify *what* the class is. The
novelty over Hehl/Agricola-Friedrich/Sharpe is precisely that all three keep the reference
rigid, so their object always carries `[α] ≠ 0`; GU's τ⁺ gauging of the reference moves it to
the `0` class, which is not a frame change.

**Explicit failure conditions** (any one falsifies the result):

1. **FC-1 (flat-reference / abelian escape).** If the GU reference connection `∇_LC` is
   *required* to be flat (`F_{∇_LC} = 0`) on the physical configuration space, then the
   curvature obstruction §3.1 vanishes and `α` could be a coboundary on simply-connected `Y`;
   `[α]` might then be zero and `D` would collapse to a `T` after a frame change. (Defense:
   the dark-energy mechanism is invoked precisely in the *curvature-rich* regime `F_A ≠ 0`;
   but if the *reference* `∇_LC` specifically is always flat while only `∇` is curved, the
   obstruction must be recomputed with `F_{∇_LC} = 0`, and §3.1 no longer applies — only
   §3.2 survives, which still gives `[α] ≠ 0` via differential order but loses the curvature
   interpretation.)

2. **FC-2 (center leak).** If the structure group is enlarged so that `g` acquires a nonzero
   center `Z(g) ≠ 0` (e.g. `G = U(64,H)`-with-`U(1)` factor rather than simple `Sp(64)`),
   then §3.1's step "`F_{∇_LC} − D_{∇_LC}ζ ∈ Z(g)-valued ⟹ = 0`" fails for the central
   component, and a central part of `[α]` *could* be a coboundary. The novelty would then
   hold only for the semisimple part. Falsifier: exhibit a nonzero `ζ` with
   `F_{∇_LC} = D_{∇_LC}ζ` valued in the center, trivializing the relevant `[α]`.

3. **FC-3 (∇-dependent frame change).** The collapse definition forbids the frame `k` from
   depending on `∇`. If one *allows* a `∇`-dependent regauging `k = k(∇)` (a section of a
   bundle over `Conn(P)`), then `D(∇, g)` can always be written as `∇ − ∇'_LC(∇)` with
   `∇'_LC(∇) = g(∇)·∇_LC`, which *is* a "torsion relative to a `∇`-dependent reference." If
   the physics admits such `∇`-dependent references as legitimate "frames," the distinction
   becomes a definitional choice rather than a theorem. Falsifier: a principled reason the GU
   construction must admit `∇`-dependent reference connections as ordinary frames. (Defense:
   a `∇`-dependent reference is not a frame in the standard fiber-bundle sense — it is a
   nonlinear connection on `Conn(P)` — so excluding it is the correct reading; but this is a
   modeling assumption, not a theorem, hence stated as a failure condition.)

4. **FC-4 (coboundary via large gauge / `π₀`).** If `G = Map(Y, Sp(64))` is disconnected
   (`π₀(G) ≠ 0`, possible for `Y¹⁴` with nontrivial `[Y, Sp(64)]`), the cocycle/coboundary
   analysis in §2 must be done component-by-component, and a class trivial on the identity
   component could be nontrivial globally or vice versa. The `H¹` computation assumed the
   connected gauge group. Falsifier: a large gauge transformation under which `α` becomes
   exact.

**Why CONDITIONALLY_RESOLVED and not RESOLVED.** The *binary* non-collapse statement —
`[α] ≠ 0`, hence no frame change turns `D` into a torsion `T̃` — is established at **verified
grade on the identity component** by the infinitesimal jet-order argument §3.2
(`[α'] ≠ 0 ∈ H¹(Lie(G); Ω¹(Y, ad P))` by a pointwise differential-order count). What remains
short of RESOLVED is (a) the **structure** of the class: the identification of `[α]` with the
universal Chern–Weil / Maurer–Cartan curvature class is argued at reconstruction grade via
§3.1, not as a fully verified computation of `H¹_{cont}(G; Ω¹(Y, ad P))` (which would require
the precise smooth/Fréchet structure on `G = Γ(Ad P)` and a controlled continuous-cohomology
theorem, e.g. via the van Est map for the gauge group); and (b) the **disconnected-group**
case FC-4 (`π₀(G) ≠ 0`), which the identity-component infinitesimal argument does not reach.
The curvature-pinning argument §3.1 is the most informative leg and is essentially a
Chern–Weil obstruction; the locality argument §3.2 is rigorous and frame-free and is the leg
that decides the binary question. Per the self-check discipline below, the word
"reconstruction" appears in the file (grade label for §3.1 and the structure claim), and the
four explicit failure conditions are present; both bind the overall verdict at
CONDITIONALLY_RESOLVED even though the leg that discharges the named failure condition is
itself verified.

---

## §7. Open questions / what would change the verdict

- **OQ-1 (verified global `H¹`).** The *infinitesimal* class `[α'] ≠ 0 ∈ H¹(Lie(G); Ω¹(Y, ad P))`
  is now established (§3.2, verified, identity component). What remains is the *global*
  upgrade: compute `H¹_{cont}(G; Ω¹(Y, ad P))` for `G = Γ(Ad P)` over `Y¹⁴` rigorously
  (Fréchet-Lie continuous cohomology, van Est map from `H¹(Lie(G); ·)` to `H¹_{cont}(G; ·)`),
  handle `π₀(G)` (FC-4), and confirm `[α]` is the universal nonzero "Maurer–Cartan / curvature"
  class identified in §3.1. This upgrades §3.1 from a reconstruction-grade interpretation to a
  theorem and would move FC-1/FC-2/FC-4 from "possible escapes" to "the precise locus where the
  class vanishes."
- **OQ-2 (section pullback of the class).** Compute `s*[α]` on `X⁴` and confirm it is the
  4D contorsion non-tensoriality, closing the loop with HC1's coupling-coefficient result and
  with the prior file's "PC2 pullback" open step.
- **OQ-3 (Noether tie-in).** Connect `[α] ≠ 0` to the divergence-free proof: the
  IG-equivariance (`β = 0`) is what feeds Noether's second theorem (`D_A^* θ = 0`); the
  classical `[α] ≠ 0` is *why* standard torsion has no automatic divergence-free property.
  Make the implication `[α] = 0 ⟺ Noether-divergence-free` precise.
- **OQ-4 (PC4 contact).** With the distinction sharpened, PC4 (torsion-for-Λ) candidates
  (Nieh-Yan, torsion-trace) carry `[α] ≠ 0` and so are *not* automatically divergence-free,
  whereas θ (`[α]=0`) is — quantifying this difference is the substantive PC4-vs-θ separation
  flagged in the prior file §6.

---

*Filed: 2026-06-23. Sharpens `explorations/geometry-curvature-emergence/dd1-distortion-tensor-literature-check-2026-06-22.md`
and uses the equivariance computation of
`explorations/dark-energy-cosmology/dark-energy-divergence-free-proof-2026-06-22.md` §2 and the decomposition result
of `explorations/geometry-curvature-emergence/hc1-hidden-curvature-components-2026-06-22.md` §8. Reconstruction grade; no
promotion to active_research or canon without meeting `RESEARCH-STATUS.md` criteria.*

---

## Self-check (verdict discipline)

Searched the draft for the forced-downgrade triggers:

- **"reconstruction"** — present (grade label, §intro/§6/§7 and footer). Per the rule, any use
  of the word forces the verdict to CONDITIONALLY_RESOLVED at best. → verdict set to
  CONDITIONALLY_RESOLVED. ✔ consistent.
- **"need to recheck" / "need to check"** — absent.
- **Explicit internal contradiction of the form "X gives Y and Z, not W"** — none asserted
  about *this file's own result*. (§5 affirmatively *reconciles* HC1 with this result; it does
  not name a contradiction. The phrase "changes coupling coefficients and field equations but
  not irreducible types" is a consistency statement, not a contradiction.)
- **≥3 explicit failure conditions for CONDITIONALLY_RESOLVED** — four provided (FC-1…FC-4),
  each a specific mathematical falsifier. ✔

**2026-06-23 strengthening note.** §3.2 was upgraded from a heuristic jet-order remark to a
verified infinitesimal Lie-algebra-cohomology argument (`α'(ξ) = −D_{∇_LC}ξ` first-order vs
`(∂ζ)'(ξ) = [ξ,ζ]` zeroth-order, decided pointwise at a single `y₀`), so the *binary*
non-collapse result is now verified-grade on the identity component; §3.1's `Ad(G)`-fixed-point
step was made explicit (`(ad P)^{Ad(G)} = Z(sp(64)) = 0`). The overall verdict remains
CONDITIONALLY_RESOLVED because the *structure* claim (`[α]` = universal Chern–Weil class via
§3.1) is reconstruction-grade and FC-4 (disconnected `π₀(G)`) is untouched by the
identity-component argument.

Verdict: **CONDITIONALLY_RESOLVED**, consistent with all triggers.
