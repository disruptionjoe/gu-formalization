---
title: "K2147: Moving raw kernels and generic graph rigidity"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no source selection, apparatus construction or GU recovery
scripts:
  - tests/channel-swings/k2147_moving_raw_kernel_prolongation_probe.py
---

# K2147: Moving raw kernels and generic graph rigidity

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
result: Moving raw kernels and generic graph rigidity
carrier: K2132 complex32 graph in fixed K77 core128, real1280 joint jets LAYER=toy CHIRALITY=N/A
pairing: inherited S and original common-H raw coefficient class ON=declared_carrier
real_structure: real coefficients and complex adjoint as stated
grading: graph t/Z multiplicity, not observed chirality
action_owner: repository-construction -- explicit conditional object below
target: analytic rank obstruction on the conserving graph manifold MAP-TYPE=intertwiner
```

## 1. The moving-kernel question changes the conclusion

[K2144](k2144-raw-neighborhood-rank-budget-2026-10-27.md) proves exactly13 FIXED
universal homogeneous coefficients and isolates three extra P0 directions. It
explicitly leaves open whether those extra vectors can rotate with the graph.
Here their first prolongation is tested modulo the ENTIRE available raw image,
and also modulo the jointly available raw-plus-target image. Both obstruction
ranks are three. This establishes more than failure of fixed transport:

- every sufficiently small nonzero point of the native hyperbola has exactly13
  homogeneous coefficients and ZERO compatible joint1280 first jets;
- the zero-jet locus contains an OPEN DENSE subset of the entire connected
 320-real-dimensional conserving positive graph manifold;
- any nonconstant C1 solution of these pointwise equations on a connected
  spacetime domain must remain in a proper analytic exceptional set.

This does not prove that the exceptional set has no moving solutions. It is not
full-family rigidity, a source-operator no-go, a physical positive quotient or GU
falsification. The fixed conditional K77/common-H raw class and upper contraction
are unchanged; lower-return constraints remain absent.

## 2. Actual derivative and its quotient, not the bare residual

Use [K2141](k2141-full-graph-raw-tangent-2026-10-27.md)'s real equations

    F(z)c+T(z)v=0, c in R16620, v in R1280.                       (1)

At P0 their ranks are rank F0=16604 and rank[F0,T0]=17884. Their16-dimensional
raw kernel splits into the universal13 and K2144's explicit three extras e_j.
The augmented kernel consists of the SAME raw kernel with v=0, because K2141
excludes every nonzero target combination. Original coefficient labels are kept.

Along the native hyperbola Y(u)=(I+cosh(u)R+sinh(u)Q)E,

    Y0=(I+R)E, Y'0=QE,
    P'0=(QE Y0*+Y0 E Q)/2.                                    (2)

For each fixed extra vector reconstruct its native core action A and all14 upper
residuals U_a. The derivative column D_j=F'(0)e_j has blocks

    U_a P',
    -P' A P+(I-P)A P',
    P'(A+A*)P+P(A+A*)P'.                                      (3)

The last expression is the scalar-current homogeneous row in original coordinates.
The native modified-current row of K2141 is equivalent JOINTLY with leakage.
Along this hyperbola PSP=(9/280)sech²(u)P, so its HOMOGENEOUS current coefficient
is sech²(u) times (3)'s underlying current row. The scalar prefactor has zero
derivative at0. The full augmented target-current term generally remains present
away from0: it is not discarded. It vanishes at0 by K2141, and its derivative
does not enter [F,T]'(e_j,0)=F'e_j. This distinction makes the prolongation valid.

A rotating homogeneous lift c(u)=e+u c1+... must satisfy F0 c1+F'0 e=0.
Consequently D must be tested modulo im F0. K2144's bare noncircle residual rank
cannot answer that question. To test the full jet system the relevant quotient
is instead modulo im[F0,T0]. Neither coefficient corrections nor shared target
corrections may be omitted.

## 3. Exact finite certificate on complete affected cosets

Differentiate the ORIGINAL row-scaled K2141 matrix using exact integer projector
numerators. A separate sparse-matrix implementation of (3) checks every derivative
column, including all row scales, independent of the array product-rule code.
The actual derivative support occupies exactly normalized XOR cosets64 and78;
upper-output row shifts are removed exactly as in K2141. Every raw column in each
affected coset is included, not just the old556 columns in coset64. Targets keep
their shared global IDs among all1280. Exact rational and mod101 ranks agree:

| coset | raw columns | selected target columns | rank F | rank[F,T] | rank[F,D] | rank[F,T,D] |
|---|---:|---:|---:|---:|---:|---:|
|64|556|72|549|589|549|589|
|78|520|72|519|559|522|562|

The two complete blocks total1076 raw columns. After raw elimination and stacking
with SHARED target IDs, the affected target rank is80 and target-plus-D rank83.
Already the coset78 block proves all three D columns independent modulo its raw
and target columns. Therefore they are independent modulo the GLOBAL images too:
a global dependence would restrict to a forbidden dependence in that block.
The three-column size supplies the matching upper bound. No independence between
local target copies is assumed, and no complete32-coset replay is claimed.

Thus globally

    rank[F0,D]=16607,
    rank[F0,T0,D]=17887.                                      (4)

These append-D ranks are derivative certificates at0, not values of the undifferentiated
matrix at0. The stored report includes the actual three derivative columns, primitive
row digests, exact/modular block ranks and pinned dependencies. K2141/K2028 complete
raw/tangent bases and base ranks are reused; their premises and digests are retained.
Actual fault controls alter a base coefficient, omit a product-rule term and break the
projector derivative identity; all fail mathematical checks after the clean baseline.

## 4. Analytic Schur argument consumes the derivative certificate

Let M(u) be either F(u) or [F(u),T(u)], analytic near0. Fix complements to its
kernel and image at0, and choose an invertible rank-r0 block. Block Gaussian
elimination is analytic for small u and leaves a Schur block S(u) that vanishes
at0. Its derivative is exactly the map from ker M0 to coker M0 induced by M'0.
Equation(4) says that this derivative has rank3 on the three extra directions;
the universal13 directions are identically in ker M(u). Select a3x3 minor of
S'(0) with nonzero determinant. The corresponding minor of S(u) is
u³(det minor(S'(0))+O(u)), nonzero for every sufficiently small u!=0.

The universal13 provide upper bounds16607 for F and17887 for [F,T], so the
lower bounds from this minor attain both maxima there. In particular

    dim{v:T(u)v in im F(u)}=1280+16607-17887=0.                 (5)

This settles the moving-kernel question on the punctured hyperbola and all graph
points in an open full-rank neighborhood of each such point. It supplies neither
a numerical radius nor a full-sector finite-u matrix rank certificate. Those
claims are not inferred from decimal sampling.

## 5. Released analytic continuation: generic rigidity of the whole graph family

K2132's entire strictly positive conserving maximum-sector manifold is

    M=U(8) x Mat8(C) x {C:C*C<I},
    graph map A=U sqrt(I+B*B-C*C).                              (6)

It is connected and real analytic. Use the global right-invariant frame generated by iH,
with H a Hermitian basis of Mat8(C), on U(8), ordinary real and imaginary B,C directions, and four spacetime
copies to frame the joint1280 tangent variables. This is a global analytic
FRAME on a manifold, not a claim of one global Euclidean coordinate chart.
The positive matrix square root is analytic on positive-definite inputs, as
is L=(Y*Y+I-E)^-1Y*, and all finite native residual rows are analytic. Thus
[F,T] is a globally analytic finite matrix in this frame. A change from K2141's
local coordinates is an invertible target-column map and does not change rank.

By section4 there is a point with maximal rank17887. Choose one such nonzero
maximal minor as an analytic function on M. On a connected real-analytic
manifold a nonzero analytic function cannot vanish on an open subset: local
power-series uniqueness propagates along overlapping charts. Its nonzero set
is open dense. More invariantly the deficient-rank locus is the common zero
set of ALL maximal minors, a proper closed analytic determinantal set E_bad.
On M minus E_bad, rank[F,T]=17887; since rank F<=16607 and there are only1280
target columns, rank F must equal16607, proving zero compatible jets there.

This generic result does not identify E_bad, its dimension, its components, or
whether any component supports a moving selector. P0 itself has augmented
rank17884, so it lies in E_bad despite its separate zero-jet certificate. A
nonempty exceptional set is NOT evidence of a surviving solution, and generic
zero jets are NOT proof of complete rigidity.

There is a useful exact consequence requiring no coefficient boundedness beyond
pointwise finite equations. If a C1 solution z(x) on a connected open spacetime
domain hits z* outside E_bad, continuity gives a neighborhood mapping outside
E_bad, where every derivative of z is zero. Thus z=z* locally. The preimage
of z* is closed by continuity and open by repeating this argument at every
point of the preimage; connectedness makes the solution constant. Therefore
any NONCONSTANT solution stays entirely inside E_bad. This does not replace
K2144's path-integrability requirement for no-departure at the exceptional P0.
The next targeted construction is the exceptional-locus compatibility/integrability
problem, not another generic-sector sweep.

## Acceptance and source boundary

This is conditional internally reviewed mathematics: exact finite elimination,
analytic Schur/identity proofs and pointwise-to-C1 transfer are distinguished.
No proof assistant, external-expert certification, remote CI or novelty claim.
SC-OP-04 candidate operator grammar, SC-OP-05/META53 uncertainty and META56 odd-action
boundary remain unchanged. LT-SM8/LT-GR6b, ledger0.263, source register and canon
receive no verdict move. Changed upper contractions remain distinct permitted
research branches, not repairs attributed to the fixed raw class.
