---
title: "K2135: Full conserving graph connections and nonflat current transport"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional full graph connection freedom; no raw-class compatibility or source-selected holonomy
scripts:
  - tests/channel-swings/k2135_full_graph_current_connection_probe.py
---

# K2135: Full conserving graph connections and nonflat current transport

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
result: Full conserving graph connections and nonflat current transport
carrier: actual K2132 complex32 graph in core128 with native Cl4 multiplicity8 LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: inherited S=a t+3a W Z restricted to positive h ON=declared_carrier
real_structure: complex operator adjoint
grading: Cl4 spin and multiplicity signs; no observed chirality
action_owner: repository-construction -- chosen inherited-form projection or another explicitly compatible connection
target: all graph connections and selected dynamics MAP-TYPE=intertwiner
```

## 1. The full family and the new question

K2132 gives the complete maximum-dimension conserving graph
Y=(I,A,B,C)^T on the Cl4 multiplicity8 space, tensored with the spin4
identity. A=U(I+B*B-C*C)^(1/2), C*C<I. In these joint (t,Z) bases,
S=a t+3a W Z, a=9/280, W=iC1 C2 C3, and

    h=Y*SY=2a(I-C*C)>0.

All graph maps intertwine Cj and M. W*=W, W²=I, [W,Cj]=0 and {W,M}=0.
This uses the actual K2132 decomposition of the native core, not a new pairing.
The conditional graph family has320 real parameters. We do not solve its
1280-real-dimensional raw spacetime first-jet system. K2129 and K2134's
curve-specific exclusions remain intact.

The new decision is whether inherited-current transport across the WHOLE graph
family can carry genuine curvature, and whether that curvature is forced by
current conservation. The answers are yes and no, respectively. This distinguishes flat scalar-curve transport from the nonflat connections
available on the full graph family.

## 2. Canonical projection connection and its exact freedom

With d the parameter/spacetime exterior derivative define

    P_S=Y h^(-1)Y*S,
    Γ_S=h^(-1)Y*S dY,
    R=(I-P_S)dY=dY-YΓ_S.                              (1)

P_S²=P_S, P_S* S=S P_S and Y*S R=0. No positive ambient metric is assumed;
only the restricted h is positive. Differentiation gives

    dh=Γ_S* h+hΓ_S.                                  (2)

Thus Γ_S is metric compatible. It is uniquely determined by the EXTRA
ambient S-orthogonality rule Y*S(dY-YΓ)=0, not by conservation alone.
Its curvature is

    F_S=dΓ_S+Γ_S∧Γ_S
       =h^(-1)dY* S(I-P_S)∧dY.                       (3)

To prove(3), differentiate h^-1Y*S dY, use
dh=dY*S Y+Y*S dY, and cancel the Y*S dY wedge square against Γ∧Γ.
The uncancelled term is exactly(3). A frame change Y->Yg gives the usual
Γ->g^-1Γg+g^-1dg, h->g*hg, so the construction is a connection, not a
frame-specific array. The graph chart itself already fixes a global frame.

There is also a global FLAT compatible connection on this entire chart:
with r=h^(1/2), Γ_flat=r^-1 dr. It satisfies(2) and Maurer--Cartan gives
F_flat=0. All compatible connections are

    Γ=Γ_flat+r^-1 Ω r,  Ω*=-Ω.                       (4)

This follows by multiplying the homogeneous compatibility equation by r^-1
on both sides. To retain the fixed principal matrices also require
[Ω,Cj]=0. Γ_S meets that requirement because S, Y and dY commute/intertwine
Cj. Γ_S need not commute M; h does commute M, which is the condition used
for the massive current. Conservation is not a connection-selection rule.

## 3. A nonflat slice, missed by both scalar curves

On B=C=0, A=U in U(8), h=2aI. Put θ=U*dU and Λ=(I-3W)/2. Direct compression
of S gives Γ_S=Λθ. Maurer--Cartan dθ=-θ∧θ and W²=I imply

    F_S=(Λ²-Λ)θ∧θ=2θ∧θ.                             (5)

Take X=E12-E21 and Z=E23-E32 in multiplicity8, and
U(x,y)=exp(xX)exp(yZ). Then at the origin

    (F_S)xy=2[X,Z]=2(E13-E31) !=0.

This is an exact non-Abelian two-parameter curvature witness; no numerical
sampling of exponentials is needed. Small-loop parallel transport therefore
has a nonzero area-order term. The sign of that term follows the selected
parallel-transport convention; nonflatness does not depend on it. On the same
slice Γ_flat=0. Scalar one-parameter curves have θ∧θ=0 and cannot decide
this question. No source-forced Berry curvature, observable phase or unique
physical connection is inferred.

## 4. Selected PDE and full-H completion

Let Γ be any connection in(4) commuting with Cj, and take constant real mass μ.
For χ in the spin4 times multiplicity8 carrier use

    [∂t+Σ Cj∂j+Γ0+Σ CjΓj+μM]χ=0.                    (6)

Differentiating ρ=χ*hχ and j_j=χ*hCjχ, using(2), [Γ,Cj]=0 and
hM+M*h=0, proves ∂tρ+Σ∂j j_j=0. A time-varying metric h cannot be discarded;
Γ=0 generally fails this equation. For φ=Yχ the core coefficient is prescribed by

    Acore Y=Y(Γ0+Σ CjΓj+μM)-(∂tY+Σ Cj∂jY).          (7)

On R3, assume smooth graph maps, a uniform lower bound h>=cI>0, bounded Y,
its left inverse, r,r^-1, and bounded first derivatives; require transformed
connection potentials bounded with enough time regularity for a common H1
domain (C1 in time in operator norm suffices). Transforming ψ=rχ turns(6)
into a constant-principal Dirac equation with bounded skew-Hermitian lower
coefficient, hence a selfadjoint Hamiltonian on H1 and a unitary propagator.
Current conservation and finite propagation speed follow; transported selected
spaces inherit them. No claim covers C*C approaching I, unbounded graph maps,
or the full1920 principal Cauchy problem.

Use the actual K2021 H,D0 and K1951 J. Set X=JY and N=D0J AcoreY.
Since J*HD0J=-iS,

    X*HN=-i[h μM+Σ Cμ Dμ],
    Dμ=hΓμ-Y*S∂μY, C0=I.                            (8)

Each Dμ is skew-Hermitian by(2); it commutes Cj. Thus(8) is Hermitian.
For Γ_S all Dμ vanish. With L=(X*X)^-1X*, C0full=X*HN,

    Q=HNL+L*N*H-L*C0full L, K=H Q                   (9)

satisfies HK=K*H and KX=N, using the actual involution H²=I. rank K<=64,
because its range lies in span(N,HL*), each rank at most32. This is the
K2131 interpolation lemma applied to the entire graph with its actual Gram;
no circle-specific scalar Gram is used. The coefficient is changed: it is
NOT an original raw upper-class solution or a southeast-only repair.

## 5. Verification, countercontrols and ceiling

The exact probe reconstructs a Cl4 spin factor, the SAME inherited S, a
nontrivial rational graph, connection and projection, then checks current,
nonflat curvature, flat-current countercontrol and Hermitian interpolation.
Multiplicity3 embeds into8; the full graph and domain quantifiers rely on the
written algebra/proof, independently internally reviewed. Input/equation
faults remove the metric inverse, change the inherited coefficient, drop the
variable-metric connection and omit the extension subtraction. None mutates
an assertion. No complete raw coefficient exhaustion, external review,
proof-assistant verification or novelty is claimed.

SC-OP-04 ASSERTS only candidate operator grammar; SC-OP-05 and SC-META-53
remain UNCERTAIN; SC-META-56 DISAVOWS the odd-action prerequisite. LT-SM8 and
LT-GR6b remain open physical-domain debts. Source, ledger0.263 and canon do
not change. Next test the full raw tangent system or supply an observation/action
reason selecting the changed contraction and connection; mathematical existence
and holonomy alone do not select either.
