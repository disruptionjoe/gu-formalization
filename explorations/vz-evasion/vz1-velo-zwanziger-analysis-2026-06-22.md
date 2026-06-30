---
title: "VZ1: Velo-Zwanziger Constraint Analysis for GU Spin-3/2 Sector"
status: OPEN
date: 2026-06-22
---

# VZ1: Velo-Zwanziger Analysis

**Status.** OPEN — the evasion candidate (trivial internal gauge coupling) is structurally
coherent but UNCONFIRMED. Three independent failure modes remain open. This document maps
each precisely.

**Tags.** `[verified]` = established result with named reference. `[reconstruction]` =
inferred from sources with explicit warrant. `[speculation]` = extrapolation with explicit
naming of what would need to hold.

---

## The VZ Theorem: Precise Statement

### Original result

Velo and Zwanziger (1969), Phys. Rev. 186:1337 — preceded by Johnson and Sudarshan
(1961), Ann. Phys. 13:126 — showed that a massive or massless Rarita-Schwinger field
Ψ_μ^α minimally coupled to an external gauge field generically suffers:

**(VZ-a) Acausality.** The characteristic cone of the field equations is not the light
cone. Spacelike surfaces exist on which the Cauchy problem for Ψ_μ^α is ill-posed.
`[verified — Velo-Zwanziger 1969; also Kobayashi-Shamaly 1978 for the Abelian case]`

**(VZ-b) Unitarity loss.** The constraints that enforce the correct spin-3/2 DOF count
(γ^μ Ψ_μ = 0 in flat space, D^μ Ψ_μ = 0 in the gauge-coupled case) become inconsistent
in a nontrivial gauge background. This allows negative-norm propagating modes.
`[verified — standard review: Porrati 1993, hep-th/9304065; Deser-Waldron 2001]`

**(VZ-c) DOF mismatch.** In flat Minkowski space, a free massive spin-3/2 field has
2(2s+1) = 8 physical DOF. A massless spin-3/2 gauge field has 2 physical DOF. Under
minimal coupling to a nontrivial gauge field, the constraint algebra breaks and the DOF
count becomes inconsistent: more or fewer propagating modes than the theory's Hilbert
space can accommodate. `[verified]`

### Precise hypotheses

The VZ theorem requires ALL of the following to hold simultaneously:

**(H1) Rarita-Schwinger field.** Ψ_μ^α is a vector-spinor (spinor with a free Lorentz
vector index). On its own this is necessary but not sufficient for VZ.

**(H2) Minimal coupling.** The covariant derivative is D_μ = ∂_μ + A_μ, where A_μ is
a gauge potential for a group G taking values in a Lie algebra representation ρ(G) acting
on the internal index α of Ψ_μ^α. This means the gauge field couples to the spinorial
part of Ψ_μ^α via a non-Abelian connection.

**(H3) Nontrivial gauge group.** G is nontrivial and the representation ρ acting on the
internal index α of Ψ_μ^α is a non-singlet. Specifically, the curvature F_μν of A_μ
is nonzero: [D_μ, D_ν] = −igF_μν ≠ 0. The failure of causality comes from F_μν terms
in the characteristic matrix of the field equations. If F_μν = 0 (flat gauge background),
VZ does not fire. `[verified — VZ 1969 §3: the "bad" term in the characteristic matrix
is proportional to F_μν]`

**(H4) No local gauge symmetry for Ψ_μ^α itself.** If Ψ_μ^α is a gauge field (not just
a matter field), its local gauge invariance maintains the subsidiary conditions δΨ_μ = D_με
against deformation. Without such a local symmetry for Ψ_μ^α itself, the constraint
algebra is vulnerable. `[verified — Deser-Zumino 1976; de Wit-Freedman 1979]`

**(H5) Background does not satisfy special conditions.** In specific backgrounds (flat
space with no gauge coupling, or maximally symmetric spaces with specific radius), the
VZ pathologies can be absent. But these are fine-tuned; a generic background with
nontrivial F_μν triggers VZ. `[verified — Buchbinder-Kuzenko-Shein 1996]`

### Scope: massless vs. massive, gravity vs. gauge

- **Massive spin-3/2, free (no gauge coupling):** 8 physical DOF, causal propagation.
  VZ does not apply.
- **Massless spin-3/2 as gauge field (gravitino in SUGRA):** 2 physical DOF, causal.
  Local SUSY maintains constraints. VZ does not apply because (H4) is violated.
- **Massive spin-3/2, nontrivial internal gauge coupling:** VZ fires. Ill-posed Cauchy
  problem. (H1)–(H5) all satisfied.
- **Massless spin-3/2, nontrivial internal gauge coupling:** VZ fires.
- **Spin-3/2 coupled to gravity only (no internal gauge group):** This is the case where
  GU's evasion candidate lives. VZ in its original 1969 form does NOT fire, because
  gravitational coupling does not produce an internal-symmetry F_μν. BUT Buchdahl (1962)
  and Aurilia-Umezawa (1969) showed that spin-3/2 in curved spacetime can develop
  consistency problems via the curvature of the gravitational background (Weyl tensor
  contributions). These are not the same as the original VZ obstruction but are in the
  same family.

### The supergravity evasion mechanism

In N=1 supergravity, the gravitino Ψ_μ is a gauge field for local SUSY:
  δΨ_μ = D_μ ε + ...

This local invariance:

1. Removes (H4) — the gravitino IS a gauge field, so the constraint algebra is maintained
   by SUSY Ward identities, not by a Lagrange multiplier.
2. The gravitino couples to the stress tensor (energy-momentum) via the vierbein, NOT
   to an internal gauge group. The coupling is gravitational, not of the A_μ^a T^a type
   that appears in (H2)–(H3).
3. The guardian is local SUSY specifically — it is NOT just any local symmetry. A
   spin-3/2 field with local gauge invariance under a transformation that does not form
   a SUSY algebra could still have problems unless the algebra closes properly.

The key implication for GU: supergravity's protection requires BOTH (i) being a gauge
field under a LOCAL symmetry AND (ii) coupling gravitationally (not to internal gauge
groups). It is not sufficient to satisfy only one of these conditions.

---

## GU's Spin-3/2 Sector

### Structure of the field

From `explorations/generation-sector/generation-count-sm-branching-closure-2026-06-22.md` §4:

GU's spin-3/2 sector arises as the RS(3,1) ⊗ S(6,4) component of the spinor on
Y¹⁴ = Met(X⁴). The mechanism is the Leibniz/product rule for spinors on a direct sum
V ⊕ W:

> S(V ⊕ W) = S(V) ⊗ S(W)

The Dirac-DeRham complex on V ⊕ W produces an extra "product rule" term involving
RS(3,1) = Γ-traceless part of (V ⊗ S(3,1)) on the horizontal factor and S(6,4) on the
vertical (fiber) factor. This is the spin-3/2 "imposter" generation.

Transcript [00:40:27]: "in g u, there's one family of 16 flipped chiral spin three
halves particles."

### Internal quantum numbers

From §4.2 of `generation-count-sm-branching-closure-2026-06-22.md` (`[verified]`):

The SM gauge group SU(3) × SU(2)_L × U(1)_Y acts on S(6,4) only. The RS(3,1) factor
is a Lorentz representation and is a Lorentz scalar from the X⁴ perspective. Therefore:

RS(3,1) ⊗ S(6,4) carries SM quantum numbers:
- Under Pati-Salam SU(4) × SU(2)_L × SU(2)_R: (4̄, 2, 1) ⊕ (4, 1, 2) [flipped = CPT-conjugate]
- Under SU(3) × SU(2)_L × U(1)_Y: 16 Weyl fermions with SM charges (Q̄_L, L̄_L, u_R,
  d_R, e_R, ν̄_R and their CP conjugates in the flipped sense)

These are the SAME SM gauge quantum numbers as a standard generation, only conjugated
("flipped chiral"). The spin-3/2 field IS charged under SU(3), SU(2)_L, and U(1)_Y.

`[verified — SM gauge charges come from S(6,4) branching; the RS Lorentz factor does
not carry SM quantum numbers but does not remove them either; the total RS(3,1) ⊗ S(6,4)
is a non-singlet under the SM gauge group]`

### Two perspectives on the gauge coupling

There are two distinct levels at which one can ask whether the VZ hypothesis (H3) is
satisfied:

**14D perspective (GU's native level):** On Y¹⁴ with gauge group Sp(64) (from
`explorations/anomaly-and-bordism/anomaly-audit-cl95-gauge-group-2026-06-22.md`), the spin-3/2 field
RS(3,1) ⊗ S(6,4) is part of the spinor bundle S = H^{64}. The gauge group Sp(64) acts
on S = H^{64} via the fundamental representation. The question is whether the RS sector
component of S is in a non-singlet of Sp(64).

**4D perspective (after reduction via section s: X⁴ → Y¹⁴):** After pulling back via
the section s, the SM gauge group SU(3) × SU(2)_L × U(1)_Y emerges as a subgroup of
the structure group. At this level, the spin-3/2 field clearly carries non-trivial SM
gauge quantum numbers (see above).

---

## The "No Internal Symmetry Groups" Evasion: Assessment

### Weinstein's claim

Transcript [00:41:48–00:42:09]:

> "Vela Zwanziger says that if you have spin three halves matter that is coupled, to some
> sort of nontrivial acting group, you have to be very careful you acquire tachyons or
> failures of unitarity, causality goes out the window. But... if your model differs by
> having no internal symmetry groups, I have no idea whether it has any kind of a Velo
> Zwanziger problem."

Weinstein is explicitly claiming that GU may evade VZ because GU has "no internal
symmetry groups." This requires interpretation.

### The 14D reading of "no internal symmetry groups"

On Y¹⁴, the gauge group is Sp(64) acting geometrically — it is the structure group of
the spinor bundle, arising from the Clifford algebra Cl(9,5) ≅ M(64,H). In this sense,
Sp(64) is not an "internal" symmetry group in the sense of the Standard Model; it is a
geometric/kinematic structure group.

**Assessment.** If "no internal symmetry groups" means "no Standard-Model-type gauge
group with separate coupling constants specified by hand," then on Y¹⁴ this is true.
But VZ hypothesis (H3) does not require an SM-type gauge group. It requires a connection
A_μ with nonzero curvature F_μν acting on the field's internal index. On Y¹⁴, the
Sp(64) connection DOES have nontrivial curvature: the shiab operator couples the
curvature of the gauge connection to the spinor field. The relevant coupling is:

> D_μ Ψ_ν^α = ∂_μ Ψ_ν^α + (A_μ)^α_{β} Ψ_ν^β

where (A_μ)^α_{β} is the Sp(64) connection in the spinor representation. The curvature
[D_μ, D_ν] = −iF_μν^{Sp(64)} ≠ 0 in general.

So at the 14D level, if one tries to write a standalone Rarita-Schwinger Lagrangian for
the RS sector of the spinor, the Sp(64) gauge field would trigger VZ via hypothesis
(H2)–(H3) even though Sp(64) is "geometric" rather than "internal" in the SM sense.
`[reconstruction — the distinction between "geometric" and "internal" does not appear in
the VZ theorem's hypotheses; the theorem applies to any nontrivial gauge connection]`

### The 4D reading of "no internal symmetry groups"

After reduction to 4D via the section s: X⁴ → Y¹⁴, the SM gauge group SU(3)×SU(2)_L×
U(1)_Y appears as a subgroup of the structure group. The spin-3/2 field carries SM
quantum numbers (non-trivial representation under SM gauge group). At this level, the
field is manifestly not a singlet under the internal gauge group. VZ hypothesis (H3) is
clearly satisfied: the field is charged under SU(3), SU(2), and U(1).

**Verdict on the "no internal symmetry groups" claim at the 4D level:** DOES NOT HOLD.
The spin-3/2 field is NOT a singlet under SU(3) × SU(2)_L × U(1)_Y after reduction.
Weinstein's statement, taken as a claim about the 4D effective theory, is not supported
by the representation theory worked out in the generation-count documents.

### Reconciling the two perspectives

The only coherent reading of Weinstein's evasion claim is:

**(Reading A):** VZ must be assessed at the 14D level (on Y¹⁴), where the theory is
formulated. At this level, the spin-3/2 field is part of a geometric Dirac-DeRham complex
with a Sp(64) geometric structure group — not a "minimally coupled matter field" in the
sense VZ assumes.

**(Reading B):** Even at the 14D level, the RS sector of S = H^{64} IS coupled to the
Sp(64) gauge connection, and that connection has nontrivial curvature. What saves GU at
14D is not the absence of gauge coupling but rather the structure of the Dirac-DeRham
complex: the RS field is not described by a standalone Rarita-Schwinger Lagrangian but is
part of a first-order operator acting on all of S simultaneously.

Reading A is Weinstein's likely intent. Reading B identifies the more precise evasion
mechanism — if it exists.

**The crucial question** is whether VZ applies to a spin-3/2 component of a Dirac-type
operator (acting on the full spinor bundle S simultaneously) or only to a standalone
Rarita-Schwinger field with its own separate Lagrangian. This is the key technical issue
that determines whether GU evades VZ.

---

## Characteristic Analysis

### The standard VZ characteristic analysis

For a Rarita-Schwinger field with Lagrangian L(Ψ_μ, D_ν Ψ_μ), the principal symbol
σ(ξ) of the field operator (at covector ξ ∈ T*M) determines the characteristic cone.
VZ failure = det(σ(ξ)) = 0 for some spacelike ξ, meaning the characteristic cone
intersects the spacelike region.

For the free RS field (no gauge coupling), σ(ξ) is proportional to ξ_μ γ^μ (the Dirac
principal symbol), which is hyperbolic with characteristic cone = light cone. With gauge
coupling A_μ:

> Equations of motion: γ^{μνρ} D_ν Ψ_ρ = 0 (γ-matrix antisymmetrized)
> Constraint: γ^μ Ψ_μ = 0 (Gamma-trace condition)

The commutator [D_μ, D_ν] = −igF_μν in the equation of motion introduces a term
proportional to F_μν γ^ν Ψ_μ in the constraint. This modifies the principal symbol:

> σ(ξ)_{modified} = σ(ξ)_{free} + (g F_μν ξ^ν) terms

For spacelike ξ with |ξ|² < 0, if F_μν ξ^ν ≠ 0, the modified symbol can become
degenerate. This is the VZ mechanism.

### GU's operator: the Dirac-DeRham complex

GU's Dirac operator D_GU acts on the FULL spinor S = H^{64} simultaneously. It is not
a Rarita-Schwinger operator Ψ_μ^α → (equations of motion for spin-3/2). It is:

> D_GU: Γ(Ω^•(Y¹⁴) ⊗ S) → Γ(Ω^•(Y¹⁴) ⊗ S)

composed with the shiab Φ: Ω²(Y¹⁴) ⊗ S → Ω¹(Y¹⁴) ⊗ S that rolls up the complex.

The RS sector is NOT a separate field with its own field equation. It is the component
of S in the Lorentz representation RS(3,1) — a subspace of the total spinor space.

**Principal symbol of D_GU.** The Dirac operator on a Clifford bundle has principal
symbol:

> σ_D(ξ) = c(ξ) (Clifford multiplication by ξ)

This is manifestly hyperbolic: σ_D(ξ)^2 = g(ξ,ξ) · Id, so the characteristic
"equation" det(σ_D(ξ)) = 0 requires g(ξ,ξ) = 0, i.e., ξ is on the light cone.

**The light cone is the characteristic cone of D_GU.** For the full Dirac operator on S,
the characteristic cone is exactly the metric light cone, regardless of the gauge coupling.
This is because the principal symbol of D = c(∇) = c(∂) + lower-order (the gauge
connection contributes only to lower-order terms in the symbol). `[verified — principal
symbol of a Dirac operator; see Lawson-Michelsohn, Spin Geometry, §II.5; Berline-Getzler-
Vergne, Heat Kernels and Dirac Operators, §2.1]`

**Implication.** The Dirac operator D_GU does NOT exhibit VZ acausality at the level of
the full operator. Its characteristic cone is the light cone.

### The subtlety: restriction to the RS sector

When one asks about the propagation of the RS(3,1) ⊗ S(6,4) component specifically,
one is asking about the restriction of D_GU to a subspace of S. This restriction is NOT
the same as a standalone RS field equation.

The RS component mixes with the spin-1/2 components via the action of D_GU. There is no
projection operator P_RS that commutes with D_GU and produces a closed subsystem for
the RS component alone. The shiab operator Φ couples Ω²-valued spinors to Ω¹-valued
spinors, mixing different Lorentz representations.

**Working hypothesis:** GU's RS sector does not propagate independently. It is coupled
into the full Dirac system, which propagates on the light cone. The VZ pathology requires
an independently propagating RS field with its own field equation; GU may not have this.

`[reconstruction — requires explicit proof that (a) the RS component of D_GU's kernel
couples to spin-1/2 components, and (b) there is no closed spin-3/2 subsystem in the
Dirac-DeRham complex. Neither is verified in the existing exploration documents.]`

### What would a standalone GU RS field equation look like?

If GU is to make contact with observed spin-3/2 particles (as a distinct particle type),
it must have a field equation for the RS sector that is approximately decoupled from the
spin-1/2 sector at some energy scale. At that decoupling scale, the RS field equation
would be a Rarita-Schwinger-type equation in a gauge background. At THAT level, the VZ
analysis would apply.

The question deferred: at what scale does the RS sector decouple, and what is the
background gauge field (including SM gauge fields) at that scale?

---

## Verdict

**Status: OPEN (not EVADED, not GENUINE_OBSTRUCTION — the question is not yet
precisely posed at the level GU operates)**

### Summary of findings

**1. At the 14D level (D_GU on Y¹⁴), VZ does not fire directly.**

The Dirac operator D_GU has the light cone as its characteristic cone for the full spinor
system. VZ is a theorem about standalone Rarita-Schwinger fields with their own Lagrangian.
GU's spin-3/2 sector is NOT a standalone RS field; it is a component of the full spinor
on Y¹⁴. In this sense, GU's construction avoids VZ's applicability at the 14D level by
not having the RS sector as an independently propagating field.

`[reconstruction — this is the most favorable reading of GU's evasion; it requires
verification that the RS sector genuinely does not decouple into an independent field]`

**2. At the 4D level (after reduction), VZ is potentially applicable.**

After pulling back via s: X⁴ → Y¹⁴, the spin-3/2 field carries SM quantum numbers and
couples to the SM gauge group. VZ hypothesis (H3) is satisfied at this level. If the RS
sector decouples into an independent 4D field (at any energy scale), VZ applies and the
"no internal symmetry groups" evasion FAILS.

`[reconstruction — the 4D decoupling is not demonstrated in existing exploration
documents; it is contingent on the spectrum of D_GU and the mass scale of the RS
particles]`

**3. Weinstein's "no internal symmetry groups" statement does not hold at the 4D level.**

The spin-3/2 field carries the flipped-chiral Pati-Salam representation (4̄, 2, 1) ⊕
(4, 1, 2) — it IS charged under SU(3), SU(2)_L, and U(1)_Y. The "no internal symmetry
groups" claim can only be sustained if interpreted as a statement about the 14D theory,
where the gauge group is Sp(64) (geometric) rather than SM-type.

`[verified — from generation-count-sm-branching-closure-2026-06-22.md §4.2, the SM
charges are present and non-trivial]`

**4. The Dirac-DeRham structure provides a potential evasion mechanism, but it is not
verified.**

The evasion mechanism, if it exists, is:

> GU's RS sector is not a standalone matter field minimally coupled to a gauge connection.
> It is a component of a first-order differential operator (D_GU) on a Clifford bundle.
> Standalone field equations (and hence VZ analysis) apply only AFTER the RS sector has
> decoupled from the full spinor. Before decoupling, VZ is inapplicable because the RS
> field is not an independent dynamical variable.

This is a non-trivial and potentially correct evasion mechanism, but it requires:

(a) Proof that the RS sector does not decouple from the spin-1/2 sectors at the 14D
level (i.e., no closed RS sub-system exists in D_GU).

(b) Demonstration that after 4D reduction, if RS decouples at some mass scale M_RS,
the effective 4D RS field equation at energies below M_RS is of a type that avoids VZ
(e.g., by having a guardian symmetry emerge from the GU structure).

(c) Identification of the guardian symmetry. The supergravity example shows that a
guardian is necessary when the spin-3/2 field decouples. GU's proposed super-IG
extension (a super-extension of the inhomogeneous gauge group Sp(64) ⋉ Ω¹(ad P)) is
a candidate guardian `[speculation — this is Weinstein's suggested direction at [00:41:48];
the super-IG algebra is not constructed in the existing documents]`.

**5. The gravitational-background VZ problem is a separate concern.**

Even if the SM gauge coupling is removed (the "no internal symmetry groups" scenario),
Buchdahl (1962) and Aurilia-Umezawa (1969) show that spin-3/2 fields in curved spacetime
can develop acausality via the Weyl tensor of the gravitational background. On Y¹⁴ (a
14-dimensional non-compact space with the gimmel metric), the gravitational curvature
effects on the RS sector are unanalyzed. This is a separate open question from the SM
gauge coupling problem, and it would need to be addressed even if the SM coupling problem
were resolved.

`[reconstruction — Buchdahl 1962 and Aurilia-Umezawa 1969 are standard references for
the gravitational VZ problem; their application to Y¹⁴ is not worked out anywhere in
the existing exploration documents]`

### The three open questions

| # | Question | Resolution needed | Current status |
|---|---|---|---|
| OQ1 | Does the RS sector of D_GU decouple into an independent field at any scale? | Spectral analysis of D_GU on Y¹⁴; or proof of non-decoupling | UNRESOLVED |
| OQ2 | If RS decouples at scale M_RS: what is its 4D effective field equation and what guardian symmetry (if any) maintains its constraints? | Explicit 4D effective Lagrangian for the RS sector after Kaluza-Klein-like reduction | UNRESOLVED |
| OQ3 | Does the Weyl tensor of the Y¹⁴ background (gimmel metric) produce gravitational VZ problems for the RS sector, independent of SM gauge coupling? | Compute the characteristic cone of D_GU restricted to the RS sector in the gimmel background; check for spacelike characteristics | UNRESOLVED |

### Failure conditions

VZ becomes a GENUINE_OBSTRUCTION to GU if ANY of the following are demonstrated:

**(F1)** The RS sector of D_GU decouples into an independent 4D field, AND that field has
no guardian symmetry that maintains its subsidiary conditions against SM gauge backgrounds.

**(F2)** The characteristic cone of the RS sector of D_GU in the gimmel metric has
spacelike components (gravitational VZ problem).

**(F3)** The super-IG extension proposed by Weinstein as a guardian does not form a
closed algebra with the RS constraints, i.e., the SUSY-like Ward identities do not
maintain γ^μ Ψ_μ = 0 in the relevant background.

### Evasion confirmation conditions

VZ would be EVADED (confirmed) if ALL of the following are demonstrated:

**(E1)** Proof that the RS sector of D_GU does not decouple from the full spinor system
at the 14D level. This would mean VZ is inapplicable because GU has no standalone RS
field at the 14D level.

OR:

**(E2)** If RS decouples: an explicit guardian symmetry (super-IG or other) that maintains
the subsidiary conditions for the RS sector in the relevant backgrounds, analogous to
SUSY's role for the gravitino.

AND:

**(E3)** Verification that the gravitational-background VZ problem (Weyl tensor effects
on RS propagation in Y¹⁴) does not produce additional acausality.

---

## What This Means for GU

### Honest summary

The "no internal symmetry groups" evasion claim is **not false, but not precisely stated
at the right level of the theory**. The correct statement is:

> At the 14D level, GU does not have a standalone Rarita-Schwinger matter field minimally
> coupled to an external gauge connection. The RS sector is part of a Clifford-Dirac system
> and does not have its own independent field equation. This is the genuine structural
> difference from the VZ setup.

This IS a potentially valid evasion mechanism. It is analogous to (but not the same as)
the SUGRA evasion: in SUGRA, the gravitino avoids VZ by being a gauge field; in GU, the
RS sector may avoid VZ by not being an independent field at all.

However, after 4D reduction (and presumably after some Kaluza-Klein-like mass generation),
the RS sector must produce observable spin-3/2 particles. At that point, an effective 4D
description must exist, and at that effective level, VZ conditions apply. The current
documents do not show that this effective description is protected.

### Implications for the research program

1. **N2 / Dirac-DeRham complex:** The most urgent VZ-related computation is to determine
   whether D_GU's RS sector has a closed sub-system. This is entangled with the shiab
   computation (SC1 task) and the Dirac-DeRham-Einstein complex structure. The RS
   decoupling question is exactly the question of whether the shiab Φ maps the RS sector
   back to itself or mixes it with the spin-1/2 sector.

2. **Guardian symmetry:** If RS decouples, a guardian must be identified. Weinstein's
   super-IG extension is the only candidate currently mentioned. This requires constructing
   the super-IG algebra: a super-extension of the inhomogeneous gauge group IG = Sp(64) ⋉
   Ω¹(ad P) over Y¹⁴. This is non-trivial and currently at speculation grade.

3. **No-go map update:** The VZ entry in `canon/no-go-class-relative-map.md` §2.5 should
   be updated to reflect that the evasion mechanism is more precisely the "Dirac-DeRham
   non-decoupling" rather than "trivial internal coupling." The two are related but distinct:
   non-decoupling at 14D implies trivial internal coupling at 14D (no standalone RS field
   to couple); non-trivial SM coupling appears only after 4D reduction.

4. **Priority relative to other tasks:** VZ1 is a genuine concern but is not currently
   blocking the other open computation tasks (N3, N6). The representation-theory level
   (N5, generation count) is unaffected. The no-go analysis deepens the understanding of
   what the GU construction must deliver at the analytic level.

### Comparison to other no-go families

| no-go family | GU evasion mechanism | evasion status |
|---|---|---|
| Witten 1981 | Y¹⁴ is non-compact (no smooth compact internal manifold) | PLAUSIBLE (not proven) |
| Nielsen-Ninomiya | Not a lattice theory; continuous geometry | NOT APPLICABLE |
| Freed-Hopkins | Anomaly structure via Sp(64); KO-theory index | UNDER ANALYSIS (N2/N5) |
| Distler-Garibaldi | GU not based on E8; no E8 representation theory claim | NOT APPLICABLE in strict DG sense |
| Velo-Zwanziger | Dirac-DeRham non-decoupling at 14D; no standalone RS field | OPEN (mechanism identified, not verified) |

VZ is unique among the no-go families in that: (i) it applies to a specific GU prediction
(the spin-3/2 imposter generation) rather than a structural claim; (ii) it admits a
coherent evasion candidate; (iii) the evasion depends on dynamical (not purely
representation-theoretic) properties of D_GU that are not yet analyzed.

---

## References

- Velo, G., Zwanziger, D. (1969). "Propagation and quantization of Rarita-Schwinger
  waves in an external electromagnetic potential." Phys. Rev. 186:1337.
- Johnson, K., Sudarshan, E.C.G. (1961). "Inconsistency of the local field theory of
  charged spin-3/2 particles." Ann. Phys. 13:126.
- Buchdahl, H.A. (1962). "On the compatibility of relativistic wave equations for
  particles of higher spin in the presence of a gravitational field." Nuovo Cim. 10:96.
- Aurilia, A., Umezawa, H. (1969). "Theory of high-spin fields." Phys. Rev. 182:1682.
- Kobayashi, M., Shamaly, A. (1978). "Minimal electromagnetic coupling for massive
  spin-two fields." Phys. Rev. D 17:2179. (Partial Abelian evasion.)
- de Wit, B., Freedman, D.Z. (1979). "Supergravity and the spin-3/2 field." Phys.
  Rev. D 21:358.
- Deser, S., Zumino, B. (1976). "Consistent supergravity." Phys. Lett. B 62:335.
- Deser, S., Waldron, A. (2001). "Gauge invariances and phases of massive higher spins
  in (A)dS." Phys. Rev. Lett. 87:031601. (Review of VZ conditions and evasions.)
- Berline, N., Getzler, E., Vergne, M. Heat Kernels and Dirac Operators. Springer, 1992.
  §2.1 (Principal symbol of Dirac operator; characteristic cone = light cone).
- Lawson, H.B., Michelsohn, M.L. Spin Geometry. Princeton UP, 1989. §II.5 (symbol of
  Dirac operator).
- Weinstein, E. UCSD April 2025 transcript:
  [00:39:18] (RS product rule; third generation from RS term),
  [00:40:27] (one family of 16 flipped chiral spin-3/2 particles),
  [00:41:48–00:42:09] (Velo-Zwanziger; "no internal symmetry groups" evasion claim).
- `explorations/generation-sector/generation-count-sm-branching-closure-2026-06-22.md` §4 (RS sector
  internal quantum numbers; SM charges from S(6,4)).
- `canon/no-go-class-relative-map.md` §2.5 (existing VZ entry; this document extends it).
- `explorations/anomaly-and-bordism/anomaly-audit-cl95-gauge-group-2026-06-22.md` (Sp(64) gauge group).

---

*Filed: 2026-06-22. VZ1 task output. Status: OPEN. The evasion mechanism (Dirac-DeRham
non-decoupling of RS sector at 14D) is identified and is structurally coherent; it is
not verified. The "trivial internal coupling" evasion claim holds at 14D but fails at
4D. Three open questions (OQ1–OQ3) and three failure conditions (F1–F3) are specified
with explicit resolution criteria.*
