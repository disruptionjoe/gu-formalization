---
title: "K2212 Minimal massive connection algebra and exact gap threshold"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional common-return connection classification and constant-background spectrum; no source gauge or physical action selection
scripts:
  - tests/channel-swings/k2212_mass_connection_algebra_probe.py
---

# K2212 Minimal massive connection algebra and exact gap threshold

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
result: minimal ten-dimensional mass connection algebra, full140-to40-to30 coefficient classification and exact constant spectral gap
carrier: real128 Cl77 spinor and supplied raw V1152 sector, observed O={0,7,8,9} LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: positive Euclidean reduced current; distinct ambient trace-Hq ON=declared_carrier
real_structure: real Clifford coefficients, complex Fourier Hilbert completion
grading: grade2 tangent bivectors and grade13 mass generators; not a family or physical chirality count
action_owner: repository-construction -- unchanged common raw lower return and supplied observed principal part
target: conditional invariant evolution and connection curvature MAP-TYPE=intertwiner
```

## Result and scope

The positive massive coefficient of [K2206](k2206-changed-raw-mass-construction-2026-10-28.md)
and tangent Spin algebra generate a ten-dimensional real Lie algebra isomorphic
to so(2,3). It preserves every fixed normal trace-Hq form. For all fourteen
connection components valued in THIS algebra, preservation of the supplied
V1152 forces every normal component to vanish. The remaining40 coefficients
have induced image15 and kernel25; the positive-current subset has dimension30
and image5. Its entire induced zero-order term is

    N=m P0+Q(c+b dot C),   m,c,b_j real.                 (1)

On the constant-coefficient full-space H1 domain the Hermitian Hamiltonian has

    spectrum=(-infinity,-g] union [g,infinity),
    g=max(|m|-|b|,0).                                  (2)

This exact threshold strengthens K2209's massless no-gap result. It is not a
source-selected gauge algebra, coupled interacting action, observed physical
quotient, or theorem about variable-background gaps. The whole140-dimensional
class differs from K2209's full1274-dimensional Spin class; neither contains
the other. No source or ledger grade changes.

## 1. Minimal Lie closure and trace compatibility

Use eta=(+1 seven,-1 seven), O={0,7,8,9}, normal complement U,
J=gamma0...gamma13, Q=gamma0 gamma7 gamma8 gamma9, and Cj=gamma0 gamma_j.
Set B_ab=gamma_a gamma_b for a<b in O and P_a=gamma_a J. Then J²=1 and

    [B_ab,P_c]=2(eta_b delta_bc P_a-eta_a delta_ac P_b),
    [P_a,P_b]=-2 B_ab  (a!=b).                         (3)

Together with the ordinary bivector bracket these close the ten independent
blades. In particular [B_0j,P0]=-2P_j, proving minimality from tangent Spin
and the one mass coefficient P0. The extra generator has the positive metric
sign in the bivector presentation, giving signature(2,3). This identifies a
Lie algebra only; it does not construct a Cartan geometry or gauge action.
Each generator has B-adjoint X*=-X and commutes with every gamma_r, r in U.
Hence X* gamma(q)+gamma(q)X=0 for every normal q, the same trace-Hq test as
K2206/K2209. This test remains distinct from the source fermion action pairing.

The algebra is also the ENTIRE B-skew real normal commutant. Faithful
Cl(7,7)=End(R128) lets us test every Clifford blade. Commuting with all ten
normal generators permits even blades with no normals (tangent grades0,2,4),
or odd blades containing all normals (grades11,13), a16-dimensional space.
The B-adjoint sign (-1)^(d(d+1)/2) retains only grades2 and13, dimension6+4.
This maximality separately assumes normal commutation and B-skewness; it does
not classify every trace-Hq-compatible matrix without those assumptions.

## 2. Entire common-return class and current

Let Omega_k be arbitrary in this algebra for k=0,...,13 and keep the original
raw D_k, observed principal derivatives and bottom return of K2209. Its
normalized bottom row annihilates every sum-zero normal tuple iff
Omega_r gamma_r is independent of r in U. For each r the possible supports
are grade3 blades containing exactly that normal index (from B_ab), and
grade12 blades missing exactly that normal index and one tangent index
(from P_a). For distinct normal r these supports are disjoint. Their common
intersection is zero, so all Omega_r=0. No assumption of zero normal
connection was used.

Each remaining Omega_k commutes with normal gammas. Direct substitution in
all fifteen original raw rows preserves V and yields nine identical equations

    partial_t u+sum_j Cj partial_j u+N u=0,
    N=gamma0 sum_(k in O) gamma_k Omega_k.              (4)

The probe checks original-row differences on a basis of every sum-zero tuple,
including auxiliary and observed leakage rows. It never fits a lower adjoint.

The tangent-bivector part of(4) has the inherited8-dimensional even image,
with four independent symmetric transpose directions and four skew directions
Q,QC7,QC8,QC9. Write the odd part Omega_k=sum_a e_ka P_a. Then

    N_odd=(e00-e77-e88-e99)P0
           +sum_j(e0j-ej0)Pj
           +sum_(j<l)(ejl-elj) gamma0 gamma_j gamma_l J. (5)

The six displayed off-diagonal generators are symmetric under ordinary real
transpose, whereas P0 is skew. Thus current conservation is precisely e=e^T
on this part. Its10 symmetric coefficient coordinates produce one mass,
m=eta-trace(e); the nine tracefree coordinates are invisible to(4).
The even and odd Clifford supports are disjoint. The full map consequently
has rank15, kernel40-15=25; its symmetric defect has rank10, leaving30
current-compatible coefficients with image5 as in(1).

For smooth real coefficients in this current-compatible class,
partial_t|u|²+sum_j partial_j(u† Cj u)=0. The principal current has unit
speed because C(n)²=I for unit n. Bounded time-independent potentials retain
the self-adjoint H1 domain, and bounded operator-norm-continuous time-dependent
potentials have the inherited unitary Volterra propagator. No unbounded
potential or ambient14D domain theorem is inferred.

## 3. Exact spectrum of every constant conservative image

Put S=-iQ and M=-iP0 after complexification. Then S²=M²=I,
[S,Cj]=0, {M,S}={M,Cj}=0. The Hamiltonian is

    H(p)=p dot C+S(c+b dot C)+mM.                       (6)

When b=0, squaring gives energies of magnitude
sqrt((|p| plus/minus c)²+m²), so the spectrum avoids(-|m|,|m|).
Adding S b dot C has operator norm |b|; the resolvent Neumann-series bound
therefore excludes |E|<|m|-|b| when |b|<|m|.

For the converse, take p=r n with n parallel b (any unit n if b=0), r real.
T=S C(n) commutes with H and has both eigenvalues tau=+1,-1: an invertible
C(v) with v perpendicular n exchanges them. On each T sector,

    H_tau=tau |b|+(r+tau c) C(n)+mM,
    E_tau,plus/minus=tau |b| plus/minus sqrt((r+tau c)²+m²). (7)

The invertible C(n)M preserves each T sector and anticommutes with its
centered Hamiltonian (r+tau c)C(n)+mM, so both branches actually occur
(the zero degenerate case is immediate).
As r ranges over R, these rays fill exactly the complement of(-g,g); for
|b|>=|m| they fill all R. Localized Fourier wave packets turn the matrix
values into spectral points. Combined with the resolvent bound this proves(2),
not merely a sufficient small-potential estimate. The case m=0 recovers
K2209, and c can shift crossing momenta without changing the gap size.
At |b|=|m| a zero mode occurs at r=-tau c; above threshold the crossings have
r=-tau c plus/minus sqrt(|b|²-m²).

## 4. Curvature and covariance countercontrols

For Omega=omega+E, E=sum_a e^a P_a, its curvature is

    F=domega+omega wedge omega
      -2 sum_(a<b) e^a wedge e^b B_ab
      +dE+omega wedge E+E wedge omega.                 (8)

For constant Omega0=mP0 alone the connection is flat but(4) is massive.
For Omega0=P0 and Omega7=P7, the eta trace is zero and N=0, yet
F07=[P0,P7]=-2B07 is nonzero. Thus identical reduced evolution need not
mean identical connection curvature; reduced mass is not a curvature invariant.
A time-dependent transformation exp(-tmP0) can remove the flat connection,
but [P0,Cj]!=0 rotates the frozen principal matrices. Full algebra-valued
connection transformations therefore do not supply gauge covariance of the
fixed raw operator. A source-owned moving principal/observation/action bridge
remains necessary before interpreting this as a physical gauge theory.

## Evidence and remaining work

Exact sparse controls prove the finite bracket, normal-support intersection,
raw transfer, the separate original bottom-return identity off V, ranks, positive-current class, actual spectral identities and
zero-mode counterexamples. Genuine mutations reverse the curvature sign,
reverse the order of the common raw coefficient, or corrupt the squared mass.
Universal proofs above establish class completeness and the continuum spectrum;
finite examples alone do not. No external-expert, proof-assistant or novelty
claim is made. Existing so(3,2) support-incidence work concerns a different
object; K2206 supplies the mass axis but not this full connection/current/gap
classification.

SC-OP-04 ASSERTS only candidate four-field grammar; SC-META-53 is UNCERTAIN
about unbounded spectra; SC-META-56 DISAVOWS a required odd-action premise.
Neither trace-Hq compatibility nor the present Clifford closure selects their
source physical realization. Useful successors must construct the moving
principal/observation or action bridge, or test a specified variable potential;
another constant-gap computation inside(1) is now redundant.
