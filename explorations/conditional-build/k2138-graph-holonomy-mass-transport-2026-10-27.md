---
title: "K2138: Full graph holonomy and mass-parallel transport"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional graph holonomy and alternative connection; no raw operator or GU selection
scripts:
  - tests/channel-swings/k2138_graph_holonomy_mass_transport_probe.py
---

# K2138: Full graph holonomy and mass-parallel transport

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2138: Full graph holonomy and mass-parallel transport
carrier: K2132 complex32 graph in native core128 with spin4 times multiplicity8 LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: inherited positive graph metric h=2a(I-C*C), a=9/280 ON=declared_carrier
real_structure: complex adjoint, fixed unitary M with M squared=-I
grading: W eigenspaces, not observed chirality
action_owner: repository-construction -- conditional inherited-form projection connection and mass conjugation average
target: holonomy on graph parameter manifold, not every spacetime pullback MAP-TYPE=intertwiner
```

## 1. Decision and inherited objects

[K2135](k2135-full-graph-current-connection-2026-10-27.md) proves nonflatness
but does not identify the whole holonomy group. Here the canonical connection
has restricted holonomy **U(8) x U(8)** on the full graph manifold. This permits
independent transport of the two W sectors and prevents a nonzero parallel
mass-type intertwiner over that whole manifold. A new, explicitly chosen
mass-conjugation average has restricted holonomy **diagonal U(8)** and preserves
the fixed mass. Both conserve current. Thus current conservation and even
parallel mass do not select a unique physical connection.

Use the exact K2132/K2135 chart Y=(I,A,B,C)^T, A=U sqrt(I+B*B-C*C), C*C<I,
h=2a(I-C*C), a=9/280. Spin4 is implicit on each multiplicity matrix.
S=a t+3a W Z, W*=W, W²=I, [W,Cj]=0, {W,M}=0,
M*=-M, M²=-I. These are the conditional native core objects, not a
reconstruction of source-owned physical fields. Complex Cl4 is Mat4(C), so its finite-dimensional *-representation is
unitarily equivalent to spin4 tensored with multiplicity. K2132 identifies
the commuting t,Z eigenspaces as four multiplicity8 spaces using the actual
K2120 Clifford relations. This is the native bridge for a unitarily equivalent
Pauli representative, not a numerical basis fit. The fixed-principal commutant
on spin4 times C8 is two multiplicity matrix algebras indexed by W=±1.
No observed chirality identification is made.

Write Γ=h^-1 Y*S dY, P=Yh^-1Y*S. K2135 supplies

    F=h^-1 dY* S(I-P) wedge dY,
    dh=Γ*h+hΓ, [Γ,Cj]=0.                              (1)

The base is the full connected320-real-dimensional graph chart, not necessarily
a physical spacetime. Its basepoint is U=I,B=C=0; h=2aI there.

## 2. Curvature already spans the full principal commutant

At the basepoint a tangent is δY=(0,X,b,c), X*=-X. The first derivatives of
the square root with respect to B and C vanish there. On pure B and pure C
tangents, Γ(v)=0 and PδY=0. In the W=w block the four coefficients of S/a are

    (1+3w, 1-3w, -1+3w, -1-3w).

For arbitrary K in u(8), choose b1=I,b2=K/2, or c1=I,c2=K/2.
Both are actual real tangent pairs in the open chart; b1*b2-b2*b1=K,
and analogously for c. Equation(1) gives

    F_B=(K,-2K),    F_C=(-2K,K),                      (2)

where the ordered pair is W=+1,-1. The coefficient matrix has determinant -3.
Therefore these curvature values linearly span u(8) direct-sum u(8), including
both central directions. This is a complete Lie-algebra spanning argument,
not a random small-matrix witness or a dimension extrapolation.

Small contractible rectangles produce each curvature value in the restricted
holonomy Lie algebra. Conversely every transport preserves h and the fixed
Cj, so based holonomy is contained in U(8)xU(8). The connected restricted
holonomy group consequently equals that full connected group. The full
holonomy is also equal to it, since it has the same upper bound. This is the
standard curvature-to-holonomy principle; see Daniel Freed's
[Lecture 15, Holonomy](https://abel.math.harvard.edu/~dafr/diffgeom.pdf).
The displayed curvature calculation and upper containment are specific to
this graph and supply the applicable hypotheses. No novelty is asserted.

## 3. Mass obstruction is an extra transport demand

A parallel endomorphism at the basepoint must commute with all based holonomy.
A mass-type endomorphism anticommutes with each Cj and therefore exchanges
the inequivalent W sectors. The independent central phase (exp(it)I,I) in
U(8)xU(8) forces every such off-diagonal block to vanish. Hence there is **no
nonzero parallel mass-type endomorphism on the full chart** for Γ, even if
one allows a varying mass field. In particular the fixed native M is not
parallel. This is not a claim that the massive current fails: K2135 requires
hM+M*h=0 for its zero-order term, and not dM+[Γ,M]=0.

A spacetime pullback need not realize full parameter holonomy. Constant,
one-dimensional or specially constrained maps can have smaller holonomy and
admit a parallel mass. Do not transfer the full-chart obstruction to every
spacetime background or to the source operator.

## 4. Explicit mass-parallel repair and its exact holonomy

Because M is constant and unitary and commutes with h, define the involution
τ(A)=M^-1 A M. It swaps W sectors. Set

    Γ_m=(Γ+τ(Γ))/2, D=(Γ-τ(Γ))/2.                    (3)

Metric compatibility is an affine condition, so Γ_m is compatible with h.
It commutes with Cj and M; hence the fixed mass is parallel. Its curvature is

    F_m=(F+τ(F))/2-D wedge D.                         (4)

The quadratic subtraction is essential: averaging curvature is not taking
the curvature of the averaged connection. On B=C=0, θ=U*dU,
Γ=(I-3W)θ/2, so

    Γ_m=θ/2, F_m=-θ wedge θ/4.                        (5)

This is nonflat for noncommuting tangents. At the basepoint pure B or C has
D(v)=0, so(2),(4) give (-K/2,-K/2). Those values span diagonal u(8).
The upper containment now also centralizes M. Thus restricted and full
holonomy of Γ_m are exactly diagonal U(8). This supplies a substantive repair
of the mass-parallel demand while preserving genuine non-Abelian curvature.
It changes the selected connection; it is not a solution of the unchanged
raw upper coefficient class or a southeast-only repair.

Nor is this repair unique. Put r=h^(1/2). Every metric-compatible connection
commuting with Cj and M has

    Γ'=r^-1 dr+r^-1 (I_spin tensor ω) r, ω*=-ω.        (6)

This follows by conjugating its difference from r^-1dr by r and taking the
joint Cl4 commutant. The globally flat choice ω=0 and nonflat Γ_m are
inequivalent countercontrols. In a gauge not keeping M constant, use dM in
the parallel condition; equation(3) is given in the global fixed-M chart and
is covariant under the subgroup preserving M, not arbitrary moving frames
with a silently unchanged mass matrix.

K2135's selected Dirac-domain and rank<=64 common-H extension apply to Γ_m
under exactly its boundedness/uniform-metric hypotheses. Those are reused
results, not new raw compatibility or full1920 wellposedness claims.

## 5. Verification and retained scientific ceiling

The probe builds a unitarily equivalent spin4 Clifford representative and a finite multiplicity
witness, reconstructs S/Y/P and pure B/C curvature, checks the coefficient
span and mass commutant, and tests the curvature subtraction and nonflat
mass-preserving slice. The complete8-dimensional Lie-algebra quantifier is
proved by arbitrary K in(2), not inferred from the finite example. Deliberate
faults alter S's coefficient, the tangent adjoint, the average or the
curvature formula. Independent internal review checks the holonomy transfer
and the full-base/pullback distinction; no external review or proof assistant.

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 and SC-META-53 are
UNCERTAIN, while SC-META-56 DISAVOWS an odd-action prerequisite. No source
claim is falsified. LT-SM8/LT-GR6b, ledger0.263 and canon remain unchanged.
The unresolved next discriminator is actual full-family raw tangent
compatibility or an action/observation reason selecting one of these changed
connections. Holonomy alone supplies neither.
