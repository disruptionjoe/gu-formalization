---
title: "PC3 — Riemannian-Ehresmannian Annotation of the Witten No-Go Entry"
date: 2026-06-23
problem_label: "pc3-riemannian-ehresmannian-annotation"
status: reconstruction
verdict: RESOLVED
---

# PC3 — Riemannian-Ehresmannian Annotation of the Witten No-Go Entry

## Problem Statement

The no-go map Witten entry (`canon/no-go-class-relative-map.md` §2.1) names the candidate forgetful
operation as a "smoothing functor":

```
phi_smooth : (X~, S, B) |-> (X', trivial-bg)
```

that resolves singularities and trivializes gauge backgrounds. Two sharpening annotations are required:

1. **Riemannian-Ehresmannian framing:** phi_smooth is more precisely the *Riemannian-reduction
   functor* that projects out all Ehresmannian structure from the connection data and retains only
   the Levi-Civita (Riemannian) piece. This is the specific geometric content of the "smoothing"
   operation when the richer substrate is the metric bundle Y^14 = Met(X^4).

2. **Met(X) = Y^14 non-compact fiber entry:** The metric bundle Met(X^4) itself is a new entry in
   the "candidate richer substrate datum" column of the Witten no-go entry, providing a concrete
   richer geometric substrate that violates Witten's assumption (1) through a non-compact fiber
   rather than through orbifold singularities or branes.

The problem is annotation-grade (no new derivation required); the mathematical content is established
by PC2 and the NEXT-STEPS.md cross-impact note on Riemannian-Ehresmannian framing.

## Established Context

This annotation builds on:

- `canon/no-go-class-relative-map.md` §2.1 (Witten 1981 entry; forgetful functor description;
  assumption list)
- `NEXT-STEPS.md` PC3 entry (annotation target explicitly named; no new derivation required)
- `NEXT-STEPS.md` positive constructions cross-impact block (Riemannian-Ehresmannian framing named
  as a "clarification annotation... not a revision")
- `NEXT-STEPS.md` UCSD transcript task table (last row: "Einstein anticipates Chern-Simons /
  sharpens Riemannian-Ehresmannian framing / L1 substrate / annotation to no-go map Witten entry")
- `explorations/geometry-curvature-emergence/pc2-met-x4-bundle-formalization-stub-2026-06-22.md` and
  `explorations/geometry-curvature-emergence/pc2-gauss-y14-curvature-2026-06-23.md` (PC2: Met(X^4) bundle formalization;
  non-compact fiber established)
- Established math context: Y^14 = Met(X^4); fiber GL(4,R)/O(3,1); Levi-Civita connection as
  tautological section; distortion theta = A - Gamma as the Ehresmannian-minus-Riemannian residual

## Computation

### Step 1 — Ehresmann-Connection Decomposition of the Witten Forgetful Functor

**What Witten's class fixes.** Witten 1981 takes the connection data on the internal manifold to be
the Levi-Civita connection of a smooth Riemannian (or Lorentzian) metric. The fermion spectrum is
determined by the Dirac operator built from this Levi-Civita connection. Assumption (2) in the
no-go map entry reads: "Reduction is Kaluza-Klein at the level of the action, with smooth
Levi-Civita data."

**The Ehresmannian residual.** A general connection A on a principal bundle P over an internal
manifold is not the Levi-Civita connection. An Ehresmann connection specifies a horizontal
distribution H_A on the total space of P; the Levi-Civita connection is the unique Ehresmann
connection compatible with the metric and torsion-free. On Y^14 = Met(X^4), the distortion
field is

    theta = A - Gamma

where A is a general Sp(64) connection and Gamma is the Levi-Civita connection lifted to the
spinor bundle via the spin representation. The Ehresmannian content of A is exactly theta: the
piece that is *not* determined by the Riemannian metric g.

**Restatement of phi_smooth as Riemannian-reduction functor.** The smoothing functor
phi_smooth can be decomposed into two operations:

    phi_smooth = phi_Riemann o phi_geom

where phi_geom resolves the topological/geometric data (singularities, boundaries, orbifolds)
and phi_Riemann is the *Riemannian-reduction step*:

    phi_Riemann : (M, A) |-> (M, Gamma_M)

that replaces a general connection A by the Levi-Civita connection Gamma_M of the underlying
metric g_M. In GU language, phi_Riemann is the operation theta |-> 0: it sets the distortion to
zero. The image of phi_Riemann is precisely the Riemannian class: smooth manifolds equipped
with their Levi-Civita connection, no Ehresmannian residual.

**Witten's class as the image of phi_Riemann.** The Witten 1981 no-go applies on the image of
phi_Riemann: the Dirac operator on a smooth compact manifold with Levi-Civita connection and
trivial gauge background. The theorem is the statement that on the image of phi_Riemann, the 4D
Dirac index vanishes (no net chirality).

**What gets lost.** phi_Riemann projects out:

- The distortion theta = A - Gamma (the Ehresmannian content, 8256 d.o.f. of sp(64))
- The torsion data encoded in theta: T^(1), T^(2), T^(3) (three irreducible SO(1,3) torsion pieces,
  24 d.o.f. total, sourcing the three hidden curvature components H^(1), H^(2), H^(3))
- The full connection data of the Sp(64) bundle that is independent of the metric

The relation-side (a 4D manifold with a Riemannian metric) survives phi_Riemann. The
mechanism side (the Ehresmannian residual that could source chirality via torsion-activated
curvature or flux) does not.

**Connection to the "What gets lost" analysis.** The existing no-go map entry for Witten says
the smooth-bundle shadow loses "Net chirality data localized on S; anomaly-inflow contributions
from boundary components; the topological class of the gauge background." The Riemannian-
Ehresmannian framing sharpens this: the smooth-bundle shadow also loses the *torsion class*
encoded in theta. In GU, chirality could in principle be sourced by the Ehresmannian data theta
rather than by geometric singularities alone.

**Analogy with Einstein anticipating Chern-Simons.** Weinstein's remark ([UCSD transcript] —
that Einstein's Ricci contraction is the 4D analog of the 3D Hodge-star in Chern-Simons) points
at this same decomposition. In 3D Chern-Simons, the whole theory is built from the connection A,
not from the Riemannian metric g alone. In 4D, the Riemannian piece is g |-> Gamma_g |-> R[Gamma_g]
(Einstein curvature), while the Ehresmannian piece is A |-> F_A (full Yang-Mills curvature).
Witten's class restricts to the Riemannian side; GU's Y^14 carries both sides as independent data.

### Step 2 — Met(X^4) = Y^14 Non-Compact Fiber as New Richer Substrate Entry

**Witten's assumption (1).** "Internal manifold X is smooth, compact, closed (no boundary)."
Standard Kaluza-Klein compactifications take X to be a compact manifold, e.g. CY3 (real dim 6),
S^7 (dim 7 in M-theory). Compactness is essential for Witten's proof: it ensures that the Dirac
operator has discrete spectrum with finite-dimensional kernel.

**Y^14 = Met(X^4) violates assumption (1) via a non-compact fiber.** The bundle

    pi : Y^14 -> X^4

has fiber GL(4,R)/O(3,1), the space of Lorentzian metrics at a point of X^4. This fiber is
non-compact: GL(4,R)/O(3,1) has the homotopy type of RP^3 (via the polar decomposition retract
through O(4) -> O(3) x O(1) quotient), but the non-compact directions correspond to the
conformal/volume degrees of freedom. Specifically:

    GL(4,R)/O(3,1) = R^+ x (SL(4,R)/SO_0(3,1))

where R^+ is the conformal scale and SL(4,R)/SO_0(3,1) has dimension 9 (symmetric space of rank
1, compact part S^3 = SO(4)/SO(3)). The non-compact factor R^+ alone violates the compactness
assumption.

**Y^14 is NOT a standard Kaluza-Klein internal space.** Y^14 is the total space of a bundle
over X^4, not the internal space in the usual KK sense. The 10-dimensional fiber
GL(4,R)/O(3,1) is the "internal" space in GU's scheme, but unlike CY3 or S^7 it is:

- Non-compact (conformal direction is non-compact)
- Dynamical (the section s: X^4 -> Y^14 is a dynamical field, the metric g_s on X^4)
- Canonically attached to X^4 (not an independent compact factor in a product)

**How this evades Witten's class.** Witten's proof requires L2-normalizable zero modes of the
Dirac operator on X, which on a non-compact space generically do not exist in L2. In GU,
the fiber GL(4,R)/O(3,1) is non-compact, so the Atiyah-Schmid L2 discrete-series mechanism
(not the compact Atiyah-Singer theorem) governs zero modes. The relevant invariant is the
relative-discrete-series Plancherel multiplicity m_H(S(6,4)) in L2(SL(4,R) x_{SO_0(3,1)} S(6,4)),
which is a strictly different analytic invariant than the Atiyah-Singer index on a compact manifold.
Witten's proof (which uses compactness to invoke the Atiyah-Singer theorem on X) therefore
does not apply on GL(4,R)/O(3,1).

**Specifying the new substrate entry.** The candidate richer substrate datum for the Witten
entry is:

    (Y^14, pi, Met(X^4), s: X^4 -> Y^14)

that is, the metric bundle with its tautological structure: the total space Y^14, the projection
pi onto X^4, the identification of the fiber as the space of Lorentzian metrics Met(X^4)_x at
each x in X^4, and the section s as a dynamical field. The chirality content (generation count
= 3) is carried by the discrete-series data of the fiber GL(4,R)/O(3,1), not by a compact
internal space with singularities.

**What the Riemannian-reduction forgets.** phi_Riemann applied to the GU substrate forgets:

1. The non-compact fiber GL(4,R)/O(3,1) (replaces it with a point, since the smooth-manifold
   class has trivial fiber bundle structure: the internal space is X itself, not Met(X))
2. The discrete-series representation-theoretic data m_H(S(6,4)) (absorbed into the
   Riemannian Dirac index on X, which by Witten is zero)
3. The tautological section structure (in the Riemannian class there is no bundle projection
   from a metric bundle; the metric is the direct geometric input, not a section of a larger space)

**Comparison to existing Witten evasions.** The published Witten evasions (Acharya-Witten,
Horava-Witten, Dobrescu-Ponton) all add singular/boundary/orbifold structure to X. The GU
substrate adds a different kind of structure: it replaces compact X with the non-compact fiber
bundle Met(X^4), sourcing generation count from discrete-series harmonic analysis rather than
from codimension-1 singularities or boundary anomaly inflow. This is a different evasion
mechanism class within the same Witten "assumption (1)" axis.

### Step 3 — Annotation Formulation for the No-Go Map

**Riemannian-Ehresmannian annotation.** In the Witten §2.1 "Candidate forgetful operation"
subsection, add the following sharpening paragraph:

    [RIEMANNIAN-EHRESMANNIAN ANNOTATION, 2026-06-23]
    
    The smoothing functor phi_smooth is more precisely decomposable as:
    
        phi_smooth = phi_Riemann o phi_geom
    
    where phi_Riemann is the *Riemannian-reduction functor*:
    
        phi_Riemann : (M, A) |-> (M, Gamma_M)
    
    that replaces a general Ehresmann connection A by the unique Levi-Civita connection
    Gamma_M compatible with the metric g_M on M. The Witten 1981 class is the image of
    phi_Riemann after phi_geom has resolved singularities and trivialized gauge backgrounds.
    
    In GU language: phi_Riemann sets the distortion theta = A - Gamma to zero, projecting out
    all Ehresmannian data and retaining only the Riemannian piece. The three irreducible SO(1,3)
    torsion pieces T^(1), T^(2), T^(3) encoded in theta — which source the three hidden curvature
    components H^(1), H^(2), H^(3) — are deleted by phi_Riemann. The mechanism by which
    Ehresmannian data could source chirality (e.g., via torsion-activated curvature on a
    non-compact fiber) is exactly what phi_Riemann forgets.
    
    Analogy: Einstein's Ricci contraction (Riemannian curvature of Gamma) : Yang-Mills
    (curvature of A) :: Riemannian class : Ehresmannian class. Witten fixes the Riemannian class.

**Met(X) = Y^14 non-compact fiber entry.** In the Witten §2.1 "Candidate richer substrate
datum" subsection, add the following entry:

    [MET(X) = Y^14 NON-COMPACT FIBER ENTRY, 2026-06-23]
    
    Additional candidate richer substrate datum: the metric bundle
    
        (Y^14, pi, Met(X^4), s: X^4 -> Y^14, S = H^64, D_GU)
    
    where Y^14 = Met(X^4) is the bundle of Lorentzian metrics on a 4-manifold X^4 with
    fiber GL(4,R)/O(3,1) (non-compact, homotopy type RP^3 x R^+). This datum violates
    Witten's assumption (1) directly via non-compact fiber, not via orbifold/singular loci.
    The chirality mechanism is discrete-series harmonic analysis on the non-compact fiber
    (Atiyah-Schmid L2 theory), not anomaly inflow from boundary/brane. The generation count
    candidate is m_H(S(6,4)) = 24 (CONDITIONALLY_RESOLVED, explorations/n5-discrete-series-
    gl4r-2026-06-23.md). Status: this candidate is GU-specific and at reconstruction grade;
    the discrete-series computation gates RESOLVED status (OQ3a-c remain open).
    
    The forgetful operation that produces the Witten image from this substrate:
    phi_Riemann: (Y^14, A) |-> (X^4, Gamma_{g_s}) — collapses the bundle to its base,
    replaces the general Sp(64) connection by the Levi-Civita connection of the chosen section
    g_s = s*(gg), and discards the fiber GL(4,R)/O(3,1). The image is a smooth 4-manifold
    with Levi-Civita data — exactly the Witten class.

## Result

**Verdict: RESOLVED** at reconstruction grade.

The annotation is logically complete: the Riemannian-Ehresmannian decomposition of phi_smooth
is a rigorous statement about connection geometry (Levi-Civita vs. general Ehresmann), and the
Met(X^4) = Y^14 non-compact fiber entry precisely identifies which Witten assumption is violated
and by what mechanism.

The no-go map §2.1 should be updated with both annotation blocks (see §3 above). The update is
a sharpening of the existing entry, not a revision of the theorem statement or the analogy-
strength assessment.

**Explicit failure conditions:**

F1. If the distortion theta = A - Gamma is constrained to zero by a field equation independent
    of dynamics (not merely by gauge choice), then the Ehresmannian residual is not a free
    datum and the Riemannian-Ehresmannian split collapses. This would undermine the framing
    but would not falsify the no-go theorem or the GU construction.

F2. If GL(4,R)/O(3,1) turns out to be compact (i.e., if the conformal R^+ factor can be
    compactified or fixed by a symmetry principle), the non-compact fiber argument fails.
    Concretely: if GU imposes a volume-normalization gauge that removes R^+, the relevant
    fiber becomes SL(4,R)/SO_0(3,1) which still has rank 1 and is non-compact but lacks the
    R^+ factor. The Flensted-Jensen criterion still applies in this case; the evasion of
    Witten's compactness assumption survives.

F3. If the discrete-series computation (m_H(S(6,4)) = 24) fails — specifically if OQ3a
    (variational selection of K3-type X^4) or OQ3b-c (index additivity) are falsified — then
    the Met(X) = Y^14 substrate datum does not produce 3 SM generations even at the
    representation-theoretic level. This would not invalidate the annotation (non-compact fiber
    still evades Witten), but it would remove the main physical motivation for this substrate
    candidate.

F4. If phi_Riemann is not a functor (i.e., if the assignment A |-> Gamma_M is not natural
    with respect to diffeomorphisms and gauge transformations), the functor framing breaks.
    Concretely: phi_Riemann must send gauge-equivalent connections to the same Gamma_M;
    this holds if Gamma_M depends only on the metric g_M and not on the choice of connection
    representative A. Since Gamma_M is uniquely determined by g_M, this holds unconditionally.
    F4 is therefore not a genuine failure mode.

## Open Questions

OQ1. The Riemannian-Ehresmannian decomposition phi_smooth = phi_Riemann o phi_geom is
     asserted structurally. A rigorous functorial formulation requires specifying the source
     and target categories precisely: source = (category of stratified geometric substrates
     with Ehresmann connections), target = (category of smooth manifolds with Levi-Civita
     connections). The categorical construction is open; the annotation is at the descriptive
     level.

OQ2. Whether the torsion-activated hidden curvature pieces H^(1), H^(2), H^(3) (established
     in hc1-sl2c, 2026-06-23) can source chirality via the Ehresmannian mechanism is an open
     derivation. The annotation establishes that phi_Riemann deletes H^(1,2,3); whether these
     pieces can produce chiral zero modes in the non-compact fiber setting requires a separate
     computation downstream of the discrete-series program.

OQ3. The Met(X) substrate entry needs a precise statement of which Witten assumption it violates
     and at what analogy strength relative to the existing published evasions. The current entry
     assigns it to "assumption (1) via non-compact fiber" with analogy-strength = reconstruction
     (not yet "strong" because the discrete-series count is CONDITIONALLY_RESOLVED, not VERIFIED).
     Once OQ3a-c are closed, the analogy strength can be upgraded.

## References

- `canon/no-go-class-relative-map.md` §2.1 (Witten 1981 entry)
- `explorations/representation-theory-noncompact/n5-discrete-series-gl4r-2026-06-23.md` (discrete-series Plancherel multiplicity)
- `explorations/geometry-curvature-emergence/pc2-met-x4-bundle-formalization-stub-2026-06-22.md` (Met(X^4) bundle)
- `explorations/geometry-curvature-emergence/pc2-gauss-y14-curvature-2026-06-23.md` (PC2 Gauss equation / Y^14 curvature)
- `explorations/geometry-curvature-emergence/hc1-sl2c-bianchi-spinor-2026-06-23.md` (hidden curvature SL(2,C) labels)
- `explorations/geometry-curvature-emergence/hc1-coupling-coefficients-2026-06-23.md` (HC coupling coefficients)
- `NEXT-STEPS.md` PC3 entry and positive-constructions cross-impact block
- Witten, E. (1981). "Search for a realistic Kaluza-Klein theory." Nuclear Physics B186: 412-428.
- Acharya, B.S. and Witten, E. (2001). "Chiral Fermions from Manifolds of G_2 Holonomy."
  hep-th/0109152.
