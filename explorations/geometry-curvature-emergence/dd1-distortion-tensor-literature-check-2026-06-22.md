---
title: "DD1 — Distortion Tensor Literature Check"
artifact_type: exploration
status: exploration
updated_at: "2026-06-22"
depends_on:
  - "explorations/cycle-gates-and-audits/weinstein-ucsd-2025-04-analysis-2026-06-22.md"
  - "explorations/dark-energy-cosmology/dark-energy-noether-closure-2026-06-22.md"
  - "explorations/dark-energy-cosmology/dark-energy-divergence-free-proof-2026-06-22.md"
verdict: PARTIALLY_NAMED
---

# DD1 — Distortion Tensor Literature Check

**Status.** Exploration-grade. This document executes the DD1 task from `NEXT-STEPS.md`
and from the UCSD analysis (§5, New Task DD1). No result here is promoted to active_research
or canon without meeting the promotion criteria in `RESEARCH-STATUS.md`.

**Task.** Is the GU distortion θ = ∇ − g·∇_LC (equivalently π − ε⁻¹Bε in the coordinate-free
formulation) a named object in the differential geometry or mathematical gauge theory literature?
Check Hehl et al. (1995), Agricola-Friedrich (2003), and Sharpe (1997). Deliver a verdict:
NAMED (with equivalence statement), PARTIALLY_NAMED (with what is new), or NOVEL.

**Verdict (summary).** PARTIALLY_NAMED. The name "distortion" appears in Hehl et al. (1995)
for a partially overlapping object, and "contorsion" appears in Agricola-Friedrich (2003) for
the torsion-only case. GU's θ is distinct because of its specific gauge-equivariance property
under the full inhomogeneous gauge group IG = G ⋉ Ω¹(ad P), which neither framework provides.
The name "distortion" is apt (Hehl et al. use it) but the GU object is the gauge-equivariant
lift of Hehl et al.'s distortion to the IG-double-coset setting.

---

## §1. GU Distortion θ — Precise Definition

### 1.1 Setting

From the UCSD talk analysis (`weinstein-ucsd-2025-04-analysis-2026-06-22.md`, Claim 3)
and the divergence-free proof (`dark-energy-divergence-free-proof-2026-06-22.md`, §1):

- X⁴ is a smooth oriented 4-manifold.
- Y¹⁴ = Met(X⁴) is the observerse (bundle of pointwise Lorentzian metrics, dim = 14,
  signature (9,5) for the gimmel metric after trace-reversal; see N1 audit).
- P → Y¹⁴ is a principal G-bundle over Y¹⁴, with gauge group G (the structure group of
  the chimeric spinor bundle, identified as Sp(64) or U(128) in physicists' convention).
- ∇_ℵ ∈ Conn(P) is a fixed distinguished base connection (the "aleph connection").
- The gimmel metric ℊ on Y¹⁴ determines a Levi-Civita connection ∇_LC on the frame bundle
  of Y¹⁴.

### 1.2 Schematic form

In the transcript ([00:20:57–00:22:26]), Weinstein states:

> "It should be any connection minus the gauge transformed Levi-Civita...
> the distortion with superior equivariance is intended to replace torsion."

The schematic definition:

```
θ = ∇ − g · ∇_LC
```

where ∇ is a connection on P, ∇_LC is the Levi-Civita connection for the gimmel metric ℊ,
and g · ∇_LC is the gauge-transformed Levi-Civita connection (acting by the gauge element g ∈ G).

### 1.3 Coordinate-free form via the tau-plus homomorphism

From the divergence-free proof (§1.3):

The inhomogeneous gauge group IG = G ⋉ Ω¹(Y, ad P) acts on Conn(P). The tau-plus
homomorphism embeds G diagonally:

```
τ⁺: G → IG,  g ↦ (g, d_{∇_ℵ}(g) · g⁻¹)
```

Given ω = (ε, B) ∈ IG, the distortion is the difference of two connections derived from ω:
- The left-push: ε · ∇_ℵ (gauge-transform the base connection)
- The right-push: ∇_ℵ + B (shift the base connection by the potential B)

Their difference:

```
θ = π − ε⁻¹Bε = π − Ad(ε⁻¹)B
```

where π = ∇ − ε · ∇_ℵ ∈ Ω¹(Y, ad P) is the "naive torsion" (connection minus
gauge-transformed base), and Ad(ε⁻¹)B is the Ad-twisted potential.

### 1.4 The key equivariance property

Under a gauge transformation by h ∈ G acting on the right via τ⁺:

```
θ ↦ Ad(h)⁻¹ · θ
```

This is proved in `dark-energy-divergence-free-proof-2026-06-22.md` §2: the left factor of IG
acts trivially on θ and the right factor acts by Ad. This makes θ a genuine tensor in the
gauge sense — it transforms by the adjoint representation of G under the action of G via τ⁺.

**Contrast with standard torsion.** The standard torsion T = ∇ − ∇_LC is NOT gauge-equivariant
under the full gauge group G: a gauge transformation of ∇ shifts it by a gauge potential term,
but ∇_LC (determined by the metric alone) does not shift by the same term. The difference
T = ∇ − ∇_LC therefore has a residual non-equivariance term. Replacing ∇_LC by its gauge
transform g · ∇_LC cancels this term, producing the equivariant θ.

---

## §2. Hehl, McCrea, Mielke, Neeman (1995) Comparison

### 2.1 Their framework

**Reference.** Hehl, F.W., McCrea, J.D., Mielke, E.W., Neeman, Y., "Metric-affine gauge theory
of gravity: Field equations, Noether identities, world spinors, and breaking of dilation
invariance," Physics Reports 258 (1995), 1–171.

**Setting.** Metric-affine gravity (MAG): a theory on a 4-manifold (the base spacetime X⁴)
with three independent geometric fields:
- The metric g (a pseudo-Riemannian metric on X)
- The coframe e^a (a soldering form / vierbein)
- The connection Γ (a GL(4)-connection on the frame bundle of X; not necessarily torsion-free
  or metric-compatible)

In MAG, the connection Γ may have both torsion (T = de + e ∧ Γ ≠ 0) and non-metricity
(Q = ∇g ≠ 0, where ∇ is taken with respect to Γ).

### 2.2 Hehl et al.'s "distortion" and related objects

Hehl et al. decompose the difference between the MAG connection Γ and the Levi-Civita
connection {Γ} (Christoffel symbols of g) into three parts:

```
Γ = {Γ} + K + N
```

where:
- **Contorsion K**: arises from torsion alone. In components:
  ```
  K^λ_{μν} = (1/2)(T^λ_{μν} + T_{μ}^{λ}_{ν} + T_{ν}^{λ}_{μ})
  ```
  This is the symmetric combination of the torsion tensor components. Satisfies
  K_{λμν} = −K_{μλν} (antisymmetric in first two indices when lowered).
  Reference: Hehl et al. (1995), eq. (2.44)–(2.46).

- **Disformation N**: arises from non-metricity alone. In components:
  ```
  N^λ_{μν} = (1/2)(−Q^λ_{μν} + Q_{μ}^{λ}_{ν} + Q_{ν}^{λ}_{μ})
  ```
  where Q_{λμν} = ∇_λ g_{μν} is the non-metricity tensor.
  Reference: Hehl et al. (1995), eq. (2.47)–(2.48).

- **Distortion D** (their terminology): the full correction term D = K + N. Some authors
  (and Hehl et al. in certain contexts) call D = Γ − {Γ} itself the "distortion," meaning
  the total deviation of Γ from the Levi-Civita connection. The word "distortion" in Hehl
  et al. is sometimes applied to the full D and sometimes to the non-metricity piece N alone;
  the usage is context-dependent in their text.

### 2.3 Is GU's θ the same as Hehl et al.'s distortion?

**Partial match.** At the zeroth-order level (before equivariance is imposed):

- GU's schematic θ = ∇ − g · ∇_LC is structurally similar to Hehl et al.'s Γ − {Γ}.
- Both are the difference of a general connection from the Levi-Civita connection of a metric.
- In the zero-non-metricity limit (∇g = 0, i.e., the GU connection Γ is metric-compatible),
  Hehl et al.'s D reduces to just the contorsion K, which captures the torsion.

**Key differences.**

1. **Bundle level.** Hehl et al. work on the frame bundle of X⁴ (a GL(4)-principal bundle
   over the base spacetime). GU's θ lives on P → Y¹⁴, a principal G-bundle over the
   14-dimensional observerse. The base is different: 4D vs. 14D. This is not a minor
   technical point — the "Levi-Civita connection" in GU's setting is the LC connection of
   the gimmel metric ℊ on Y¹⁴ (signature (9,5)), not the LC connection on X⁴.

2. **Equivariance.** Hehl et al.'s distortion D = Γ − {Γ} is equivariant only under the
   local Lorentz group SO(1,3) (or its frame-bundle version). It is NOT equivariant under
   an infinite-dimensional gauge group G. GU's θ is equivariant under the full inhomogeneous
   gauge group IG acting via τ⁺. This is a structurally different and stronger equivariance.

3. **The gauge-transform of ∇_LC.** In Hehl et al., the Levi-Civita connection is fixed by
   the metric; there is no "gauge-transformed Levi-Civita" concept. In GU, the replacement
   of ∇_LC by g · ∇_LC is the defining move that produces equivariance. Hehl et al. have
   no analog of this because their framework has no action of a gauge group G on ∇_LC.

4. **Physical arena.** Hehl et al.'s distortion is a purely 4D classical geometric object.
   GU's θ is a 14D gauge-theoretic object, with the 4D shadow recovered only after choosing
   a section s: X⁴ → Y¹⁴.

**Verdict on the Hehl et al. comparison.** GU's θ coincides with Hehl et al.'s "distortion"
in name and in rough structural type (difference of a general connection from the LC
connection), but differs in: base dimension (14D vs. 4D), principal bundle (G vs. GL(4)),
and the defining equivariance property. GU's θ is not Hehl et al.'s distortion; it is a
14D, G-equivariant lift of the distortion concept to the observerse setting.

In the zero-non-metricity limit AND after pullback to X⁴ via a section s, GU's θ should
reduce to something related to Hehl et al.'s contorsion K. Whether this reduction holds
precisely requires the section pullback computation (PC2 target, §5 of this file below).

---

## §3. Agricola-Friedrich (2003) Comparison

### 3.1 Their framework

**Reference.** Agricola, I. and Friedrich, T., "On the holonomy of connections with
skew-symmetric torsion," Mathematische Annalen 328 (2004), 711–748. (Also: Agricola, I.
and Friedrich, T., "Torsion and Spinors," in Geometric Analysis and Nonlinear Partial
Differential Equations, Springer, 2003.)

**Setting.** A smooth Riemannian or pseudo-Riemannian manifold (M, g) with a metric connection
∇ = ∇_LC + A where the difference A is a (1,2) tensor, and the torsion T of ∇ is assumed to
be totally skew-symmetric (T_{abc} = −T_{bac} for all permutations; T ∈ Ω³(M)).

**Their interest.** Studying holonomy groups and spinor preservation conditions for connections
with skew-symmetric torsion. This is relevant to string theory (where the H-field = torsion
contributes a skew-symmetric torsion) and to special geometries (G₂, Spin(7), SU(3) with
torsion).

### 3.2 Contorsion in their framework

In Agricola-Friedrich's notation, the difference between ∇ and ∇_LC is written:

```
∇_X Y = ∇^{LC}_X Y + A(X,Y)
```

where A = A(X,Y) is a (0,2)-valued vector field (the difference tensor). For skew-symmetric
torsion T, the tensor A is:

```
A(X,Y,Z) = (1/2) T(X,Y,Z)
```

(where the three-index form is obtained by lowering the first index of A with g). This A
is their version of the **contorsion**: the unique tensor such that the torsion of ∇ is T
and the connection is metric-compatible (∇g = 0).

The contorsion (in the standard sense used more broadly) is defined as:

```
K_{abc} = (1/2)(T_{abc} + T_{bca} + T_{cab})
```

where the indices are raised/lowered with g. In the skew-symmetric torsion case T_{abc} = −T_{bac}
(and all permutations), the contorsion K simplifies and A(X,Y) = (1/2)T(X,Y,·). They are
related by K_{abc} = A_{abc} when T is totally skew.

### 3.3 Is GU's θ their contorsion?

**Partial match only, with a different domain.** Agricola-Friedrich work on a single manifold
(M, g) where the metric g is fixed once and for all. Their contorsion K is the difference
∇ − ∇_LC where ∇_LC is the LC connection of the fixed metric g. There is no gauge group action
on g or on ∇_LC.

GU's θ = ∇ − g · ∇_LC replaces the fixed ∇_LC with its gauge transform g · ∇_LC. In the
notation of Agricola-Friedrich:
- If g ∈ G is the identity element, then g · ∇_LC = ∇_LC, and GU's θ reduces to ∇ − ∇_LC,
  which is their contorsion (for metric-compatible ∇ with skew-symmetric torsion).
- For general g ∈ G, the gauge transform g · ∇_LC is a different connection, and the
  difference ∇ − g · ∇_LC is not a standard contorsion.

**Additional structural difference: the torsion-skewness assumption.** Agricola-Friedrich
require totally skew-symmetric torsion (T ∈ Ω³(M)). GU's θ lives in Ω¹(Y¹⁴, ad P) (ad P-valued
1-forms on the observerse), which has a different algebraic character than the totally
antisymmetric part of Ω¹ ⊗ Ω¹ ⊗ Ω¹. GU does not impose the skewness restriction.

**Equivariance.** Agricola-Friedrich do not formulate any infinite-dimensional gauge-group
equivariance for their contorsion. The contorsion K transforms covariantly under the local
Lorentz group SO(1,3) (or SO(n) for Riemannian), but this is not the same as the full
G-equivariance of GU's θ.

**Verdict on Agricola-Friedrich.** GU's θ in the identity-gauge limit (g = e) and for
metric-compatible ∇ with skew-symmetric torsion on X⁴ reduces to (a pushforward of)
Agricola-Friedrich's contorsion. But the full GU θ is not their contorsion because: (a) the
base is 14D not 4D; (b) the gauge-transform of ∇_LC is GU's defining move and has no analog
in their framework; (c) GU's θ is in Ω¹(ad P), not in the purely geometric Ω¹ ⊗ Ω¹.

---

## §4. Sharpe (1997) Comparison

### 4.1 Sharpe's framework

**Reference.** Sharpe, R.W., Differential Geometry: Cartan's Generalization of Klein's
Erlangen Program, Springer, 1997. (Graduate Texts in Mathematics 166.)

**Setting.** Cartan geometry: a principal bundle P → M with structure group H ⊂ G (a parabolic
or Klein pair), equipped with a Cartan connection ω ∈ Ω¹(P, g) — a g-valued 1-form on the
total space of P that restricts to the Maurer-Cartan form on H-fibers and is G-equivariant.

A Cartan connection encodes both the "rolling" of the model space G/H on M and the connection
on the principal H-bundle. In the case G = Poincare group and H = Lorentz group, a Cartan
connection on P → M is equivalent to a vierbein e and a Lorentz connection ω (the
gravitational first-order formalism).

### 4.2 The curvature and torsion of a Cartan connection

The curvature of a Cartan connection ω is:

```
Ω = dω + (1/2)[ω, ω] ∈ Ω²(P, g)
```

The torsion is the g/h-valued part of Ω (where g/h is the quotient of the Lie algebra of G
by that of H). In the Poincare/Lorentz case, the torsion is:

```
T = de + ω ∧ e
```

where e ∈ Ω¹(P, g/h) is the g/h-component of ω (the "translational" part). This is Cartan's
geometric torsion, encoding the failure of the soldering form to be parallel.

### 4.3 Development of a Cartan connection

The "development" of a Cartan connection is the curve in the model space G/H obtained by
rolling the model space along a curve in M. The development encodes holonomy and is the
Cartan-geometry analog of parallel transport.

The difference tensor ∇ − ∇_LC in the Riemannian case, when viewed as a Cartan connection
datum, relates to the curvature of the Cartan connection on the Poincare bundle. But this
is a correspondence at the level of "curvature of the model space development," not an
identification of θ as a development.

### 4.4 Where GU's θ sits in Sharpe's framework

GU uses the frame bundle F(Y¹⁴) → Y¹⁴ as its principal bundle (the frame bundle of the
14-dimensional observerse with structure group SO(9,5), the spin group of the gimmel metric).
The gimmel metric ℊ determines a canonical Cartan connection on F(Y¹⁴): the Levi-Civita
connection ∇_LC (ℊ), together with the soldering form (the canonical 1-form on the frame
bundle).

GU's θ = ∇ − g · ∇_LC is then the difference between a general connection ∇ (not
determined by ℊ) and the gauge-transformed Levi-Civita connection g · ∇_LC. In Sharpe's
language:
- ∇ is a second Cartan connection on the same bundle, not constrained to be the LC one.
- The torsion of ∇ relative to ∇_LC is T = ∇ − ∇_LC (the standard notion).
- GU's θ = ∇ − g · ∇_LC is the "torsion relative to the gauge-transformed reference."

Sharpe does not define a "torsion relative to a gauge-transformed reference connection"
as a named object. His torsion is always relative to the flat model (the canonical Cartan
connection of G/H). The gauge-transform of the reference is not a construction that appears
in Sharpe's framework because his Klein geometry has a fixed model, not a variable one.

The closest Sharpe concept: the curvature of a Cartan connection measures the failure to be
locally isomorphic to the flat model G/H. If ∇_LC (ℊ) is taken as the "flat model" in the
sense of the Levi-Civita reference, then GU's θ measures the failure of ∇ to equal the
gauge-transformed flat reference. This is a generalization that is not in Sharpe but is
consistent with the spirit of Cartan geometry.

**Verdict on Sharpe.** GU's θ does not appear in Sharpe's framework as a named object.
The nearest is the curvature/torsion of a Cartan connection, but Sharpe does not consider
the gauge-equivariant version where the reference connection is gauge-transformed.
GU's τ⁺ construction (the diagonal embedding of G in IG) is the structural move that
produces the equivariant θ; this has no direct analog in Sharpe's Klein-geometry setting.

---

## §5. Verdict

### 5.1 Summary table

| Framework | Named object | GU θ matches? | What matches | What is new in GU |
|---|---|---|---|---|
| Hehl et al. (1995) | "Distortion" D = Γ − {Γ} | Partial | Same name, same schematic type (connection minus LC) | 14D base, G-bundle over Y¹⁴, G-equivariance under IG via τ⁺ |
| Hehl et al. (1995) | Contorsion K (torsion piece of D) | Partial | θ reduces to K in zero-NM limit on X⁴ | Same as above; equivariance is the key distinction |
| Agricola-Friedrich (2003) | Contorsion K for skew-symmetric torsion | Partial (identity-gauge limit) | θ in g=e limit on X⁴ with metric-compatible ∇ | Gauge-equivariance, 14D base, g · ∇_LC construction |
| Sharpe (1997) | Curvature/torsion of a Cartan connection | Structural analogy only | GU uses Cartan-geometry language of frame bundles | Gauge-equivariant reference: no analog in Sharpe |

**VERDICT: PARTIALLY_NAMED.**

The word "distortion" for the object ∇ − g·∇_LC is appropriate and consistent with Hehl
et al.'s usage. However, GU's θ is NOT the same as any of these three frameworks' named
objects because of its specific gauge-equivariance under the full inhomogeneous gauge group
IG. This equivariance property is the defining innovation.

### 5.2 What is new in GU's θ

The novel feature is the **double-coset equivariance structure**:

1. The reference connection is not fixed but is gauge-transformed: ∇_LC ↦ g · ∇_LC.
2. This makes the difference ∇ − g · ∇_LC equivariant under G acting via τ⁺: G → IG.
3. Standard contorsion and distortion are equivariant only under the local frame group
   (SO(1,3) or SO(p,q)); GU's θ is equivariant under an infinite-dimensional G = Sp(64).
4. This equivariance is what makes θ divergence-free (via Noether's second theorem applied
   to the gauge-invariant Yang-Mills action on Y¹⁴), whereas standard torsion has no such
   automatic divergence-free property.

### 5.3 Proposed formal statement of the partial equivalence

**Claim (exploration-grade).** Let s: X⁴ → Y¹⁴ be a smooth section (a metric on X⁴).
Let ∇ be a metric-compatible connection on the frame bundle of X⁴ with skew-symmetric
torsion T. Then the section pullback s*(θ) ∈ Ω¹(X⁴, ad P|_{X⁴}) is, in the identity-gauge
limit (g = e), equal to the contorsion K of T in the sense of Agricola-Friedrich (after
the identification of ad P|_{X⁴} with the adjoint bundle of the frame group).

This claim is not proved here; it requires the section pullback computation (PC2, see §6).

---

## §6. Implication for PC4 (Torsion-for-Λ)

### 6.1 Are PC4 and the distortion mechanism the same?

The positive-constructions-lane proposal (§Target 3) describes PC4 as using torsion to
replace the cosmological constant Λ. The transcript's specific mechanism (Claims 2 and 3
in the UCSD analysis) is the gauge-equivariant distortion θ — not generic torsion.

These are **distinct but related**:
- PC4 (generic torsion-for-Λ) uses candidates like the Nieh-Yan invariant or the torsion
  trace vector V_μ = T^ν_{μν}. These are classical 4D objects available in any torsionful
  extension of GR (Einstein-Cartan theory, teleparallel gravity).
- GU's θ-mechanism is more specific: θ is gauge-equivariant under IG acting on the 14D
  observerse, and its divergence-free property is automatic from gauge invariance (Noether's
  second theorem), not from metric-compatibility.

### 6.2 Relationship between the two

GU's θ-mechanism and PC4's torsion candidates are related by the section pullback:
if s*(θ) reduces to a torsion-related object on X⁴, then the 14D gauge-equivariant
θ-mechanism is an uplift of a 4D torsion-for-Λ candidate to the observerse setting.

However, the converse is not true: PC4's torsion candidates do NOT automatically have
the 14D gauge-equivariance that makes GU's θ structural (divergence-free without
fine-tuning). The equivariance is the key structural feature that justifies θ as a
dark energy replacement — it is the reason θ is free to respond dynamically (as a field)
while remaining divergence-free, unlike λg_μν.

### 6.3 Operational conclusion

PC4 and the θ-mechanism should NOT be conflated. The correct framing:
- PC4 (torsion-for-Λ): generic Einstein-Cartan / Nieh-Yan candidates for dark energy from
  torsion. These are the independent-motivation cases.
- GU's θ-mechanism: the specific 14D gauge-equivariant distortion from the IG double-coset
  construction. This is the GU-specific proposal and is structurally stronger (automatic
  divergence-freedom from Noether; equivariance under the infinite-dimensional gauge group).

For PC4 to make contact with GU's θ-mechanism, the section pullback s*(θ) must be shown
to coincide with a specific torsion candidate on X⁴. This is the open step that requires
the PC2 pullback computation.

---

## §7. First Action Items

1. **Check the pullback.** Compute s*(θ) for the identity-gauge case (g = e) and confirm
   whether it coincides with the contorsion K in Agricola-Friedrich's sense. This is the
   most direct falsification test of the "partial equivalence" claim in §5.3.

2. **Clarify the 14D → 4D reduction of "distortion" terminology.** The word "distortion"
   for ∇ − g · ∇_LC is well-chosen given Hehl et al.'s usage, but should be used with the
   explicit qualifier "gauge-equivariant distortion" to distinguish it from the 4D MAG
   distortion of Hehl et al.

3. **Check the McDowell-Mansouri literature.** The transcript mentions McDowell-Mansouri
   at [00:23:02] as a precursor that "doesn't work." The McDowell-Mansouri formulation of GR
   as a de Sitter gauge theory uses the full ISO(1,3) gauge group; check whether their
   difference tensor is related to GU's θ or to Hehl et al.'s distortion.

---

*Filed: 2026-06-22. Executes DD1 from `NEXT-STEPS.md` and from Section 5 of
`weinstein-ucsd-2025-04-analysis-2026-06-22.md`. Discipline: exploration-grade; no
results promoted to active_research or canon without meeting `RESEARCH-STATUS.md` criteria.*
