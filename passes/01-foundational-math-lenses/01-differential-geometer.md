# Persona Pass 01: Differential Geometer

## (a) Clearest leverage

My discipline gives sharpest leverage on **Question 1**: whether a canonical bundle over a smooth 4-manifold X carries fiber dimension 10, yielding a 14-dimensional total space. This is a bookkeeping question internal to bundle theory, so it is decidable from first principles. I get secondary leverage on Question 2 (gauge group emergence) because structure groups of natural bundles are forced by functoriality. Question 3 (spinors) lives in spin geometry, adjacent. Question 4 (GR/QFT limits) is largely outside pure geometry.

## (b) Strongest first-principles construction

Let X be a smooth oriented 4-manifold. The bundle of symmetric nondegenerate bilinear forms on TX, i.e. the bundle of pointwise pseudo-Riemannian metrics, has fiber GL(4,R)/O(p,q). For Lorentz signature (1,3) the fiber is 10-dimensional: the space Sym^2(R^4) has dimension 10, and the open subset of nondegenerate forms inherits that dimension. Call this bundle Met(X). Its total space E = Met(X) has dimension 4 + 10 = 14. So a 14-dimensional total space over a 4-manifold whose fiber is "all possible metrics at a point" is a real, canonical construction. No choice of metric on X is required to define E; E is the home of the metric-as-section.

On E one gets, canonically:
- a tautological fiberwise metric g_taut at each point of E (the point of E *is* a metric at the basepoint),
- a vertical tangent bundle V ⊂ TE of rank 10 with a natural action of GL(4,R),
- under a choice of Ehresmann connection on Met(X) → X, a horizontal complement H of rank 4.

This is the cleanest 4 → 14 story established geometry supports.

## (c) What fails or is forced

- The "observerse" total space E is not itself a spacetime in any standard sense: it has no canonical Lorentzian metric of its own. Building one requires extra structure (a connection on Met(X), a choice of fiberwise metric on V, a relative sign). Each choice is a non-canonical input. [speculation] One can attempt to build a metric on E using the tautological g_taut horizontally and a GL(4,R)-invariant metric on the symmetric-space fiber vertically, but the relative scale and signature on V are free parameters, not derived.
- The structure group of Met(X) → X is GL(4,R), not the Standard Model gauge group SU(3) × SU(2) × U(1). There is no first-principles map from GL(4,R), or from its frame-bundle cousin, to SU(3) × SU(2) × U(1). The Standard Model group is not a quotient, subgroup, or natural representation of GL(4,R) acting on Sym^2(R^4).
- Spinors require a spin structure on X (a lift of the orthonormal frame bundle through Spin(p,q) → SO(p,q)). They are forced by topology of X, not produced by enlarging dimension. The 14-dimensional E does not contain spinors as sections of any tautological bundle.
- GR limit: on-shell GR is a critical point of Einstein-Hilbert on sections of Met(X), not on E itself. Reproducing GR requires writing an action whose Euler-Lagrange equation, restricted to sections, recovers Einstein's. That is a constraint on the action, not a consequence of the geometry.

## (d) Named first-principles obstructions

1. **Functoriality obstruction.** Natural bundles over X have structure group derived from Diff(X) jets, ultimately GL or its reductions. SU(3) × SU(2) × U(1) is not natural in this sense.
2. **No-go on canonical metric on E.** The total space of a fiber bundle does not inherit a canonical Riemannian or Lorentzian metric from the base; extra data is required.
3. **Spin-structure obstruction.** w_2(X) = 0 is required for spinors; this is a topological condition on X, not a consequence of dim 14.
4. **Representation mismatch.** Standard Model fermion reps (e.g. (3,2)_{1/6}) are not contained in any natural tensor or spinor bundle of GL(4,R) or Spin(1,3).

## (e) Verdict

The 4 → 14 dimensional jump is geometrically real as Met(X), but the Standard Model gauge group, fermion representations, and dynamics are not forced by that construction and must be supplied by hand.
