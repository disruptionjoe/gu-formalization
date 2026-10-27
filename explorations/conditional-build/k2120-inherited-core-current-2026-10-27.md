---
title: "K2120: A maximal positive massive subspace of the inherited core current"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no source selection, physical quotient, GU verdict, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k2120_inherited_core_current_probe.py
---

# K2120: A maximal positive massive subspace of the inherited core current

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
result: neutral inherited forms and a sharp complex32 invariant positive-current construction
carrier: actual K1951 complexified128 core embedded in K2021 full1920 K77 carrier LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: G=Jc transpose H Jc; Hermitian current iF=i Jc transpose H D0 Jc ON=declared_core
real_structure: real Cl(7,7) matrices complexified; selected positive subspace need not be conjugation invariant
grading: ambient Clifford labels separate from current sign and finite CAR parity
action_owner: repository-construction -- fixed K1951 principal and K1967 mass, supplied K2021 duality
target: simultaneous invariant positive-current subspace MAP-TYPE=intertwiner
```

## Result and prior boundary

The actual common pairing in [K2021](k2021-common-degree-dual-operator-2026-10-24.md)
does not restrict to the positive energy that was independently supplied in
[K1951](k1951-coordinated-zero-southeast-principal-2026-10-22.md).
Both its core pairing and Hermitian time current are neutral. Nevertheless,
there is a concrete complex32 subspace, invariant under the three observed
principal generators AND the nonzero normalized K1967 mass, on which the SAME
time current is positive. Complex32 is maximal among constant subspaces invariant
under all four generators. This is a conditional construction and a sharp
classification in a specified finite class, not a selected physical quotient.

[K2022](k2022-degree-dual-dynamics-boundary-2026-10-24.md) already transports
R0/R1, the full Jordan obstruction, the positive128 core, and the full common-form
mass defect. None is recalculated as a new finding. The new question is whether
that core can support positive evolution using the **same inherited current**.
The full1920 massive adjoint defect remains: restriction does not repair it.

## 1. Actual data and exact restriction

Use the full matrices H,D0 of K2021. Reconstruct Jc directly from each stored
K1951 block as `basis * section`, embedded with its stored coordinate list;
concatenate the32 four-column blocks in file order. The three quotient generators
are C1,C2,C3 in that same order. Use the normalized M from
`k1967-paired-raw-coefficient-observation.json`, `scalar.repair[0].M`.
They obey

    Cj*=Cj, {Cj,Ck}=2 delta_jk I,
    M*=-M, M²=-I, {M,Cj}=0.

Define G=Jc^T H Jc and F=Jc^T H D0 Jc. Exact rational reconstruction gives

    G^T=G, G²=(121/2450)² I, tr G=0;
    F^T=-F, [F,Cj]=0,
    spectrum(-F²)={81/4900 (64 times),81/19600 (64 times)}.

Thus G has inertia(64,64); iF is Hermitian with64 positive and64 negative
eigenvalues. The positive magnitudes are9/70 and9/140, each32 times.
Multiplying the conserved skew Green current by i is the declared Hermitian
current convention; G and iF are not interchangeable forms.

Set

    Fe=(F+M^T F M)/2, Fo=(F-M^T F M)/2,
    a=9/280, b=27/280, T=Fe/a, A=Fo/b,
    V=C1 C2 C3, Z=-A V.

The exact identities are

    T^T=-T, T²=-I; Z^T=Z, Z²=I; [T,Z]=0;
    [T,Cj]=[Z,Cj]=[T,M]=[Z,M]=0;
    V^T=-V, V²=-I; F=aT+bVZ;
    tr T=tr Z=tr(TZ)=0.

In particular Fe commutes with M and Fo anticommutes with M. A direct spectral
positive-half selection of iF is exchanged by M; that failure is NOT a universal
positive-subspace obstruction. Mixed subspaces must be tested.

## 2. Explicit repair on the same current

In the stored128 core-coordinate order define

    R e_j=(-1)^(floor(j/64)) e_(j xor4), 0<=j<128.

It is a real symmetric involution commuting with Cj,M,T and anticommuting with Z.
Let t=iT and

    P=(I+t)(I+R)/4.

P is an orthogonal projector of trace/rank32, commutes with every Cj and M, and

    P(iF)P=aP.                                      (1)

Indeed P selects t=+1. Since R anticommutes with Z and commutes with V, the
compression of VZ to the R=+1 eigenspace is zero. This explicitly constructs
the mixed survivor rather than invoking unspecified coefficients or a new bar.
Complex conjugation sends t=+1 to t=-1, so this positive complex subspace is
not asserted to be a real field or a source ambient-half/chiral selection.

There is no unique selector: Rtheta=cos(theta)R+sin(theta)iZR is again a
Hermitian involution with the required commutations. Substitution into P gives
a continuous rank32 family with the same positive current. Selecting one
member is an extra choice, not a derived prediction.

## 3. Why32 is the maximum in this invariant class

The four Hermitian generators C1,C2,C3,iM generate complex Cl4=M4(C), so
C128=C4 tensor C32 with multiplicity32. A subspace invariant under all Cj,M
is reducing, hence C4 tensor L. The commuting Hermitian involutions t=iT and Z
act on the multiplicity space. The four joint (t,z) eigenspaces each have
dimension8 there: their full-carrier traces follow from tr T=tr Z=tr TZ=0.
Also iV has signs +/- each twice in the irreducible C4 factor. Positivity of
the compressed current is therefore equivalent to strict positivity on L of

    (t+3Z)|L and (t-3Z)|L.                            (2)

The sum implies t|L>0. Write v=x+y with t x=x, t y=-y; every nonzero v in L
satisfies ||x||>||y|| and projection L->t+ is injective. If dim L>8, its image
in the16-dimensional t+ space intersects the8-dimensional (t+,Z+) space.
Choose a corresponding nonzero v=x+y with x in that intersection. Cross terms
vanish because t and Z commute; on t- the largest eigenvalue of t-3Z is2.
Thus

    <v,(t-3Z)v> <= -2||x||²+2||y||² <0,

contradicting(2). Therefore dim L<=8, and dim W<=32. P attains it.
This excludes only larger coordinate-independent subspaces jointly invariant
under these fixed four generators with this fixed strictly positive compressed
current. Frequency-dependent constraints, different masses, semidefinite forms,
different pairings and full constraint/BV quotients are outside the theorem.

## 4. Released domain and observable construction

On W=ran P let phi evolve by

    partial_t phi = -sum Cj partial_j phi - mu M phi,
    Hobs = -i sum Cj partial_j - i mu M, mu real constant.

With Fourier derivative ik, Hobs(k)=sum Cj k_j-i mu M is Hermitian and squares
to (|k|²+mu²)I. On R3, multiplication by this symbol is selfadjoint with domain
H1(R3,W); its graph norm is equivalent to the H1 norm. This proves selfadjointness
by Fourier multiplication, not merely formal symmetry. The same statement on a
flat torus follows from its Fourier series. Evolution preserves the positive
current norm a||phi||² and the domain. P is constant, hence no hidden derivative
of a moving projector occurs. A smooth K2021 U=rho^(1/2)C gives the algebraic
lift U^-1 Jc phi with exact derivative cancellation, as already proved in K2022.
For mass, use Lq+mu U^-1 K U: K1967 supplies K Jc=D0 Jc M, so the
same transport extends this restricted massive equation without changing K.
Global bounds, invertibility and geometric descent of U remain extra inputs;
we do not turn a patchwise transport into a global source domain theorem.

One may now explicitly SUPPLY the positive CAR algebra over L2(R3,W), with its
ordinary even subalgebra and the quasifree dynamics induced by Hobs. This is an
actual compatible conditional algebra/domain on a subspace of the native core,
not the prior unconnected finite neutral model. Choosing the CAR functor,
quantum state/sea representation, P, mu, flat observation and global base is
additional construction. No source selection, interacting positivity, physical
cohomology, chirality/generation count or full1920 unitary evolution follows.

## 5. Acceptance and claim boundary

The reproducible probe reconstructs actual rational input matrices, verifies all
identities, rank through projector trace, and genuine corrupted-input controls.
The dimension upper bound and infinite-domain result are written proofs; finite
checks do not certify them. Independent mathematical review is recorded in the
verification index. No external expert or proof-assistant certification is claimed.

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 is UNCERTAIN about the
southeast rival; SC-META-53 is UNCERTAIN about physical positivity; SC-META-56
DISAVOWS an odd-action prerequisite. None changes. LT-SM8/LT-GR6b and ledger0.263
remain unchanged because the conditional positive32 selection is not an
interacting source-selected quotient. The next concrete test is whether actual
observation/gauge/connection or allowed lower coefficients preserve this P (or
its covariantly transported family); a failure must test other maximal survivors,
not declare all source observation impossible.
