---
title: Compact shielding is not preserved by the unchanged geometric reference
status: exploration
doc_type: structural-result
created: '2026-11-27'
program_target: BET-MASS-GAP
tier: T1
expected_delta: Decide preservation of positive compact reductions by the actual metric-fibre and observed-normal reference connections
actual_delta: Native vertical LC admits no positive parallel metric; section-normal LC does exactly when base holonomy is precompact, hence locally only for flat Ricci-flat four-bases
class_covered: Every source-guided tautological Lorentz-metric bundle with native trace reversal one half; unchanged fibre LC, projected normal connection along its same-metric section, and sufficiently small C1 spin-connection displacements where stated
premises:
- source-chimeric-trace-compatibility-2026-11-13.md section1 binds the source geometry chain and marks the coordinate completion reconstructed
- ricci-flat-ambient-source-jets-2026-11-27.md section2 owns the fibre and normal connection formulas
- printed-endpoint-analytic-branch-2026-11-27.md section3 supplies the actual printed small-h branch, not W2
- lab/sources/source-claim-register.yaml SC-META-53 remains UNCERTAIN and SC-GEO-55 admits independent displacement
source_bridge:
  status: conditional
  reason: The source proposes compact shielding but does not require a positive finite-fibre form parallel for the reference connection; independent displacement, moving reduction and physical quotient remain distinct
kill_condition: A nonzero real curvature eigenvalue excludes every positive parallel form for the specified connection; failure of native geometry or connection identification invalidates that transfer, not GU
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
internal_target: INTERNAL-UNCHANGED-REFERENCE-PARALLEL-COMPACT-SHIELDING
internal_target_verdict: scoped geometric exclusion; no bet-wide kill or source verdict
canon_verdict_change: none
---

# Compact shielding is not preserved by the unchanged reference

program_target: BET-MASS-GAP
tier: T1
expected_delta: Resolve exact compact preservation for the source-guided reference.
actual_delta: Vertical LC has a real curvature eigenvalue; section-normal LC has the exact base-holonomy criterion.

**Existence of a compact reduction does not imply preservation by a connection.**
In the existing source-guided Lorentz-metric bundle, no positive metric is
parallel along an open metric-fibre patch. On a Ricci-flat four-dimensional
observed section, its projected normal connection has a positive parallel
metric locally exactly when the base is flat. A related full-spinor obstruction
persists on the actual printed small-inverse-coupling branch.

These are finite-fibre transport results, not physical ghost or quantum-gap
verdicts. The ordinary Dirac countercontrol in §6 is mandatory for interpretation.

> **GU-COMPARATOR-ROUTING — scope before inference.** Classification:
> `INTERNAL_STRUCTURAL_ONLY`. Compact groups, positive Yang–Mills theories,
> normal geometric transport and a physical GU quotient are different objects.
> Follow [source-native routing](../../lab/methods/source-native-comparator-routing.md).
> No conventional Higgs, repeated-family, projection or positive-Hilbert
> premise is imported into the source's nonchiral2+1 mechanism.

```gu-typed-objects
result: reference-connection compact preservation
carrier: vertical N=Sym2(T*X) and its observed normal pullback LAYER=ambient+observed BRIDGE=same-metric-section-normal-connection CHIRALITY=N/A
pairing: native trace-reversed form K of signature6,4 versus arbitrary positive auxiliary q ON=normal_bundle
real_structure: real tensor geometry; K95 and explicitly flipped K77 ports separately checked; spin extension uses coherent Clifford compatibility
grading: geometric horizontal/normal split, not physical chirality
action_owner: repository-construction -- source-guided LC reference, no new action or selected physical connection
target: parallel compact reduction and curvature compatibility MAP-TYPE=restriction
```

## 1. Source custody and reuse

Basis: `410ad2167d2dd706a7c686a16c587804ff93d050`. This is lane-C evidence;
no scientific matrix cell or physics-ledger row absorbs it.

SC-GRP-03 (draft p29eq4.6) asserts simultaneous compact and U(3,2) normal
reductions. SC-META-53 (TOE2025 01:22:30, transcript366) explicitly leaves
handling indefinite unbounded spectra unknown and proposes compact shielding.
It does not assert LC parallelism. SC-GEO-55 (TOE02:18:44, transcript594–598)
keeps independent displacement from gauge-rotated LC. That freedom survives.

[Source geometry](source-chimeric-trace-compatibility-2026-11-13.md) §1
pins draft §§3.1–3.4, pp17–22/eqs3.7–3.17; §4/eqs3.39–3.42,4.4–4.6;
§6 pp35–36; §11 p50/eq11.4. We fix its existing connection-dependent
chimeric-to-TY identification and source-guided coordinate metric

    G_g=y(dx,dx)+K_y(theta_g,theta_g),
    theta_g=dy-C(Gamma_g)y dx,
    K_y(U,V)=tr(y^-1 U y^-1 V)-tr(y^-1 U)tr(y^-1 V)/2.

The source does not uniquely select this coordinate completion.

Already consumed: K713–716's abstract positive-reduction availability and
nonselection; K1354's split invariant-kinetic-form obstruction; K1356–1360's
supplied compact principal-series control; absolute normal-reduction existence;
the stationary flat-T3 MG1 Hessian theorem; and W2 small-h spinor commutants.
The new discriminator is preservation by the **actual reference connection**,
including vertical transport for every base and the distinct printed branch.

## 2. Native vertical curvature

For constant symmetric coordinate fields, the fibre LC connection is

    F_y(U,V)=-(U y^-1 V+V y^-1 U)/2.                    (1)

Differentiate K using D_U y^-1=-y^-1 U y^-1. The two F terms reproduce the
derivative of both trace terms; F is symmetric, hence torsion-free. The
four-dimensional native K is nondegenerate, so uniqueness proves(1).
Trace reversal has not been replaced by a positive comparator.

The fibres are totally geodesic for G_g. Horizontal parallel transport preserves
K, so the horizontal Koszul component of nabla_U V vanishes. Thus intrinsic
fibre curvature agrees with ambient curvature on three vertical arguments.
The [owned full Koszul formulas](ricci-flat-ambient-source-jets-2026-11-27.md)
§2 authenticate this for every smooth base g.

For R(U,V)=nabla_U nabla_V-nabla_V nabla_U-nabla_[U,V], differentiation gives

    R_y(U,V)W=-(1/4)y[[A,B],C],
    A=y^-1 U, B=y^-1 V, C=y^-1 W.                      (2)

The left y converts the endomorphism back to a symmetric covariant tensor.
The earlier engineering calculation owns this formula on a positive plane;
the mixed-sign plane gives the new preservation obstruction.

At y=diag(-1,1,1,1), embed these two-by-two blocks, zero elsewhere:

    A=diag(1,-1), B=[[0,1],[-1,0]], C=A+B,
    U=yA, V=yB, W=yC=[[-1,-1],[-1,-1]].

U,V,W are symmetric and W is nonzero. With J=[[0,1],[1,0]],
[A,B]=2J and [J,C]=-2C, hence

    R(U,V)W=W.                                        (3)

Congruence transports this witness to every Lorentz y. On all ten symmetric
components the eigenvalues are ±1 (multiplicity1 each), ±1/2 (multiplicity2
each), and0 (multiplicity4). W is K-null, consistent with indefinite skewness.
The block sits in the full rank-ten bundle; the degenerate standalone
base-dimension2 trace-reversal problem is not used.

If any smooth positive q were parallel on a neighborhood, curvature skewness
would give

    0=q(RW,W)+q(W,RW)=2q(W,W)>0.                       (4)

This excludes every moving or fixed positive form, including all parallel
Cartan involutions Theta with q=K(-,Theta -)>0. It fails locally at every
fibre point, independently of base curvature or topology. The statement concerns
vertical transport on an open subset of Y, not the pullback to X alone.

For y→-y and unchanged covariant U,V,W, the signs in(2) cancel and K is
unchanged. Exact controls cover both this same-input flip and the corresponding
adapted witnesses. No physical Krein/adjoint or Clifford-phase transfer follows.

**Positive control:** on the fibre of positive-definite y, the same connection
preserves q_y(U,V)=tr(y^-1 U y^-1 V)>0, although trace-reversed K still has a
negative radial direction. Thus indefinite K alone does not imply(4); actual
Lorentz-fibre curvature is essential.

## 3. Full spin connection, epsilon and small displacements

Let B be the coherent spin-LC lift on an open Y-domain. Clifford compatibility
and injectivity of the full Clifford-vector map c give

    [F_B(U,V),c(W)]=c(R(U,V)W)=c(W).                   (5)

A positive parallel Hermitian form on the full spinor bundle would induce one
on End(S) by the Hilbert–Schmidt construction. Then ad(F_B(U,V)) would be
skew-Hermitian, contradicting its real eigenvalue1 on the nonzero c(W).
Null W does not imply c(W)=0. This is a full-spinor statement, not an
individual-half-spinor or physical-subspace theorem.

Pure epsilon gauge dressing conjugates curvature and transports parallel
forms bijectively. It cannot repair(5). Independent displacement A=B+T
changes the connection, with curvature

    F_(B+T)=F_B+D_B T+T wedge T.                       (6)

Finite-dimensional spectral continuity keeps an eigenvalue of ad(F_(B+T))
near1, off the imaginary axis, for sufficiently small C1 T at the tested
point. Such connections still admit no positive parallel full-spinor form.
The perturbed connection need not remain Clifford-compatible: the argument
uses curvature continuity, not a new Clifford identity for A. No uniform
conditioning bound on hypothetical positive forms is required. No numerical
radius is claimed.

The [actual printed analytic branch](printed-endpoint-analytic-branch-2026-11-27.md)
§3 has T(h)=O(h) in every compact C^m seminorm with this held LC reference.
It is therefore covered for sufficiently small h=1/kappa. This supplies the
new printed-equation bridge without importing the already-separated W2
Euler locus. It does not settle kappa=1, large displacements or physical norms.
Nor does vertical curvature alone prove this for a spin connection pulled back
only to X, where vertical directions are unavailable.

## 4. Section-normal connection: the exact criterion

Along s_g(x)=(x,g_x), N=Sym²T*X. The projected normal connection is Sym²
of downstairs LC: in an LC-normal frame the vertical component of nabla^Y_X U
is the ordinary derivative of U; covariance gives the tensor connection.
The full ambient derivative additionally has the nonzero horizontal shape
term. These connections are not identified.

On a connected time-oriented base, the normal connection has a positive
parallel metric iff full base LC holonomy has compact closure, iff a parallel
timelike vector exists. The local version uses restricted holonomy on a
simply connected patch.

**Proof of the Sym² step.** A positive parallel q on Sym²V* gives an invariant
quartic f(alpha)=q(alpha⊗alpha,alpha⊗alpha)>0 for alpha≠0. On an auxiliary
Euclidean unit sphere it has positive lower and finite upper bounds.
Homogeneity and invariance therefore uniformly bound every holonomy matrix
and its inverse on V*. The closure in the Lorentz group is compact.
Average a future timelike vector over this compact group; convexity of the
future cone gives a nonzero invariant timelike vector. Parallel transport
extends it globally. Conversely a parallel unit timelike u gives the positive
parallel flip metric g_R=g+2u-flat⊗u-flat and its induced positive Sym²
metric. Since K is also parallel, polar decomposition yields a parallel
compatible Cartan reduction. This covers arbitrary positive q, not only a
preselected Cartan ansatz.

The compact-holonomy/timelike-vector equivalence is prior art:
[Gutiérrez–Müller, Theorem2](https://arxiv.org/abs/1502.05289).
Without time orientation the global invariant object can be only a timelike
line. The local conclusion remains valid.

If Ric(g)=0 in dimension4, parallel timelike u gives a local product
-dt²+h3. Then Ric(h3)=0, and in dimension3 Ricci determines Riemann, so g
is locally flat. Conversely, a simply connected flat patch has trivial
holonomy and admits positive parallel normal metrics. Therefore

    Ricci-flat Lorentz4: local normal compact preservation iff local flatness.

Nonflat Schwarzschild/Kerr patches fail this condition by the Ricci-flat theorem.
The exact probe checks the normalized Sym² boost mechanism, not metric-specific
Schwarzschild curvature derivatives. Global flatness alone is
insufficient when discrete holonomy is noncompact. Curved non-Ricci-flat
ultrastatic products are positive controls; nonzero curvature alone is not
being excluded. Indefinite parallel complex/U(3,2) reductions without positive
compact preservation are also outside this theorem.

## 5. Changed-connection control and physical ceiling

For a supplied K-orthogonal Cartan involution Theta, the standard correction

    D'=D+(1/2)Theta(DTheta)

satisfies D'Theta=0 and remains K-compatible, using Theta(DTheta)=-(DTheta)Theta.
It is a changed connection, not a gauge conjugation. This control exposes the
fixed-reference premise; no such source solution or selector is adopted.
Independent varpi, moving nonparallel reductions, on-shell currents, physical
state restrictions and physical quotients remain possible mechanisms requiring
their own preservation and positivity proofs. No new choice family is added.

## 6. Mandatory ordinary-Dirac countercontrol

A Lorentz boost has real eigenvalues and its finite-dimensional spin
representation preserves no positive Hermitian form. On curved backgrounds
with boost holonomy, no positive parallel spinor fibre form exists. Nevertheless
ordinary Dirac theory has a positive Cauchy density obtained by contracting its
conserved current with a future hypersurface normal; on its usual admitted
solution/domain this gives a positive physical norm. That normal-dependent
form need not be parallel. Flat Minkowski has trivial holonomy and constant
positive parallel forms, although those forms are not invariant under all
Lorentz boosts.

Thus the excluded property is **finite-fibre parallel positive shielding**,
not a necessary condition for every unitary QFT or a ghost-free physical
quotient. SC-META-53 does not identify its proposed shielding with the excluded
property. No Hamiltonian sign, physical spectral gap or normalizable-mode
conclusion follows.

## 7. Verification and effect

The [exact probe](../../tests/program-focus/bet_mass_gap_reference_holonomy_probe.py)
checks109 identities: raw fibre connection derivatives, metric compatibility,
all ten symmetric curvature components, both signature ports and same-input
flip, native14D Nomizu seam, positive-fibre and rotation controls, trace
flatness, Sym²/Dirac boost controls and coherent conjugation. The controls
calibrate the written geometric proof, not a quantum or global PDE diagnostic.

[ReferenceHolonomy.lean](../../Lean/GUFormalization/ReferenceHolonomy.lean)
checks the real-eigenvalue/positive-norm contradiction, its inner-product
version and a real-part margin. Connection geometry, holonomy, product
splitting and spectral continuity remain written proofs. The module compiled
without placeholders; no full Lean or external-expert certification is claimed.
No world-novelty claim is made; the underlying compact-holonomy criterion is
standard literature.

| State | Result |
|---|---|
| ESTABLISHED | Vertical reference curvature obstructs all parallel positive forms; section-normal positivity has the exact base-holonomy criterion; the full-spinor obstruction persists on the actual small-h printed branch. |
| RULED OUT | Unchanged-reference parallel compact shielding in the declared geometric classes and sufficiently small full-spinor displacements on open Y-domains. |
| NOT MODELED / UNDETERMINED | Source-selected shielding, physical Hilbert quotient/current, interacting Hamiltonian, quantum gap, kappa1 and full source/GU* viability. |

Weakest physical link: the source does not require the excluded parallelism.
Class-C representativeness and physical export are not established. Source,
canon, physics-ledger and matrix verdicts remain unchanged. Lane-C retention
precedes any warranted lane-B absorption. Choicebudget10/4/net6/0 predictions
is unchanged; no new action or physical mechanism is selected.
