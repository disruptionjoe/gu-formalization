---
title: Actual local solution germs with both energy signs and the corrected scalar-normal operator
status: active_research
doc_type: conditional-build-result
program_target: LB-CLASS
tier: T1
expected_delta: Assemble the actual scalar-normal operator with differential Schur corrections and test an exact full-carrier reduction against the candidate propagation burden.
actual_delta: Exact full-carrier reduction supplies local analytic linearized solutions with either canonical patch-energy sign at both held roots. Separately the corrected frozen spin7 operator has a certified positive high-frequency growth rate. Physical admission and GU falsification remain undetermined.
class_covered: The fixed W2/K95 imaginary-U quadratic connection block at the two certified zero-matter kappa1 backgrounds; scalar trace-profile jets in a named homogeneous time-adapted frame, the complete geometric-spin7 multiplicity space, and full-carrier analytic profiles in an exact triangular-frame reduction.
premises:
- explorations/conditional-build/source-action-full-auxiliary-map-2026-11-26.md
- explorations/conditional-build/source-action-constraint-consistency-2026-11-26.md
- explorations/conditional-build/source-action-graph-domain-2026-11-26.md
- explorations/conditional-build/source-action-homogeneous-analytic-vacuum-2026-11-25.md
- lab/sources/source-claim-register.yaml#SC-ACT-01
- lab/sources/source-claim-register.yaml#SC-META-52
- lab/sources/source-claim-register.yaml#SC-META-53
source_bridge:
  status: conditional
  reason: Source grammar motivates the reconstructed action, but neither W2 nor an unrestricted upstairs Cauchy domain is source-selected. The physical quotient and boundary formulation remain open.
kill_condition: Only a certified actual-coefficient necessary-estimate violation excludes its precisely named candidate-domain class. A frozen spectrum, failed ansatz or numerical solver failure is not a physical ghost or GU exclusion.
---

# Actual local solution germs with both energy signs

program_target: LB-CLASS
tier: T1
expected_delta: Assemble the actual scalar-normal operator with differential Schur corrections and test an exact full-carrier reduction against the candidate propagation burden.
actual_delta: Exact full-carrier reduction supplies local analytic linearized solutions with either canonical patch-energy sign at both held roots. Separately the corrected frozen spin7 operator has a certified positive high-frequency growth rate. Physical admission and GU falsification remain undetermined.

Basis: freshly fetched `c1f3642a5b3c7c9f06871c0e02a74644497c5ec9`.

## Scope and question

The full auxiliary map is already regular at both held roots. Its inverse
eliminates all auxiliary variables, but the reduced evolution contains
**differential compositions**, not just products of frozen matrices. The new
question is what its actual lower coefficients do to the scalar-normal
high-frequency behavior. The principal time/trace pencil and finite constraint
consistency are already settled and are not new tests here.

This document distinguishes a scalar-profile jet calculation from an invariant
lower-dimensional PDE. A profile depending initially on only time and the
normal trace coordinate need not remain in that class under evolution.
The finite matrices in sections1–4 act on geometric SO3 multiplicities, not physical
particle spins, fermion families or the observed weak-chirality grading.

```gu-typed-objects
result: actual full-carrier local linearized solution germs with either canonical patch-energy sign; separate corrected frozen high-frequency growth
carrier: W2 K95 imaginary-U connection forms; full-carrier two-variable profiles and complete geometric-spin7 jets with native N/R splitting LAYER=ambient BRIDGE=physical_admission_unproved CHIRALITY=N/A
pairing: native indefinite trace/form pairing ON=declared_carrier
real_structure: physical imaginary-U coefficients; highest-weight complexification used for exact arithmetic
grading: geometric SO3 representation and differential order; no physical spin or family identification
action_owner: repository-constructed fixed W2 action; autonomous quadratic block at zero matter
target: actual local solution germs and their canonical patch-energy quadratic form; separate scalar-profile reduced operator MAP-TYPE=endomorphism
```

No new action, physical domain, norm, boundary condition, gauge charge or
selection law is introduced. A computational trivialization is a coordinate
choice for the existing operator, not a new physical choice family.

## 1. An explicit frame, rather than omitted derivatives

Let G_tau be the orientation-preserving component of the affine group preserving
the positive ray of the base time covector. Its linear matrices have bottom row
`(0,0,0,lambda)` with lambda>0 and positive spatial-block determinant.
The stabilizer is spatial SO3. Use four translations and the ten complement
matrices

    X_a=A_a+H_a,    (H_a)_{i3}=(H_a)_{3i}=-(A_a)_{3i}, i<3.

These are the native `geometry().adapt` matrices. Use the local section
`s(x,z)=(x,exp(sum_a z^a X_a))` and its transported tangent, cotangent and
endomorphism frames. This explicitly chooses the second frame jet; it is not
silently identified with a different section having the same first jet.

For the left Maurer-Cartan form and h_ba=pr_so3[X_b,X_a],

    exp(-X)d exp(X)=dX-[X,dX]/2+O(z^2),
    alpha_a(p)=0,             e_b alpha_a(p)=-h_ba/2.

The native principal matrices K_a have constant components in the transported
frame. The time symbol is lambda K_3, so its kernel projector P and range
projector R are constant. The invariant background T has constant components,
and therefore so does M=P(I+2N(T,.))P. This is not the assertion that their
coordinate derivatives vanish in an arbitrary chart.

Write the full lower coefficient at p as

    C0=I+2N(T,.)+sum_a K_a rho(Lambda_a),
    Lambda_a=L_a+rho_tangent(H_a).

The first variation of the homogeneous connection coefficient is the isotropy
connection, giving

    e_b C0(p)=-1/2 sum_a K_a rho(h_ba).                 (1)

The full native geometric lower operator is retained and checked against the
original engine; no density or divergence term is discarded by a name change.

### Trace coordinate and physical-time lapse

For y=L^{-T}eta L^{-1}, define

    r=-(1/8)log|det y/det eta|=(1/4)log det L.

This is a group character. Since tr X_4=4 and all other normal generators are
traceless, `e_a r=delta_a4` everywhere. Thus `dr=theta4`, and derivatives of
these phase components vanish exactly. For a scalar-profile coefficient q(r),

    e_b e_a q=delta_a4 delta_b4 q''.

Also e_a(t)=0 for a!=3 and e_3(t)=lambda. The time inverse has the external
factor lambda^-1. On the central trace line L=e^r I, lambda=e^r; **not** on the
whole chart. Shape dependence of lambda is retained. Since PK_3=K_3P=0, the
auxiliary elimination has no time derivative, and its spatial composition does
not differentiate this external factor.

## 2. The actual differential Schur correction

Let G=(K_3|R)^-1 R, and use scalar-profile jets v=q(r) with values in R.
Set

    Y=M^-1 P K_4 R,       Z=M^-1 P C0 R.

The actual primary constraint gives n=-Yq'-Zq. Composing the range equation
before freezing at p yields

    q_t=lambda^-1 (L2 q''+L1 q'+L0 q),
    L2=G K_4 Y,
    L1=-G K_4 R+G K_4 Z+G C0 Y,
    L0=-G C0 R+G C0 Z+Delta0,
    Delta0=G sum_b K_b P M^-1 P (e_b C0)R.             (2)

The display evaluates the full operator on these jets; it does not assert that
the resulting function remains a scalar profile. M and K_4 have constant frame
components, so their derivative terms vanish in this named frame. The
**transverse derivatives of Z do not vanish merely because q depends on r**.
They produce Delta0, the term absent if one first freezes a 36-variable
first-order descriptor and then takes its matrix Schur complement.

## 3. Curvature correction through already-owned responses

The only nonzero h_ba occur for spatial traceless-normal V2 axes
`{5,6,8,9,11}`. Use native spatial rotation generators J_i and
`Cas=-sum_i rho(J_i)^2`. With native metric entries d_b, cotangent covariance
and the trace pairing give

    sum_a h_ba^i K_a=-(d_b/8)[rho(J_i),K_b].

Combining this with (1), on a geometric-spin7 input v,

    (e_b C0)v=(d_b/16)sum_i[J_i,K_b]J_i v
             =(d_b/32)(62-Cas)K_b v.                  (3)

For completeness, the rank2 tensor identity is
`sum_i[J_i,[J_i,K_b]]=-6K_b`. Expanding it and using
`sum_i J_i^2 v=-56v` gives the second equality in (3).
Consequently the target spin5,6,7 coefficients are respectively

    d_b,             5d_b/8,             3d_b/16.

All other b contribute zero to (1). These factors must not be extended to the
normal V1 axes. Applying P and M^-1 in (2) therefore uses only complete,
already-certified N5, N6 and N7 responses. No new auxiliary inverse is needed.
SO3 covariance makes the summed correction preserve the complete spin7
carrier, even though its intermediate terms visit other spins.

## 4. A finite high-frequency discriminator

The complete spin7 multiplicity space has dimension36:20 time-range and16
auxiliary. These correspond to300 and240 real coefficient dimensions after
the15-dimensional SO3 factors; they are not counts of physical states.

Let V=P K_4|R. The owned trace-pencil chains give rank V=10. Choose an
algebraic complement R=K direct_sum C with K=ker V, both dimension10.
The square-zero principal structure implies L2 maps into K and kills K.
The owned non-null graph identity `V G(RK_4R)K=0`, together with
`V G K_4P=0`, implies that the complete L1 in (2) preserves K.

For Fourier parameter k>0 use the sign convention

    L(k)=-k^2 L2+i k L1+L0.

The finite similarity T(k)=diag(k I_K,I_C) gives

    T(k)^-1 L(k)T(k)/k -> H,
    H=[[i L1_KK, -L2_KC], [L0_CK, i L1_CC]].           (4)

Thus the frozen eigenvalues grow at most linearly in k. A certified eigenvalue
of H with strictly positive real part produces a growing branch of this
**frozen** operator, by continuity of polynomial roots. This scaling is an
algebraic calculation, not a newly selected graph norm or physical domain.
Delta0 contributes to L0_CK and cannot be discarded before that test.
Pure imaginary leading eigenvalues establish neither bounded evolution nor
physical shielding; subleading and Jordan behavior may still matter.

### Certified result at both held roots

The exact root-box bounds, including the inherited inverse uncertainty and
the transverse correction, give:

| Root | Enclosure for Re tr(H²), rounded outward |
|---|---|
| A | [0.9710674772, 0.9712811711] |
| B | [0.2915800783, 0.2929824211] |

The native reflection identity gives tr(H)=0 throughout the parameter family.
These facts certify a growing frozen branch without fitting eigenvalue plots.
Indeed, if every eigenvalue had nonpositive real part, their zero sum would
force every real part to vanish; then Re tr(H²) would be nonpositive. The
argument does not require diagonalizability. More quantitatively, for n=20,
writing the real parts as x_j and a=max x_j gives
`sum x_j² <= n(n-1)a²`, while `sum x_j² >= Re tr(H²)`.
Both lower bounds exceed `19/80=20*19*(1/40)²`, hence a>1/40 in the
declared native normalization. This is not a physical instability rate.

The correction Delta0_CK is nonzero at both centers. The certificate records
the naive freeze-first and corrected trace moments separately. Neither the
frozen growth calculation nor this numerical rate is imported into the exact
full-carrier reduction below: the two arguments have different carriers.

## 5. An exact full-carrier reduction, beyond the frozen screen

There is a second route that does not require the frozen20 matrix to describe
an invariant PDE. Let S be the affine subgroup with upper-triangular
4x4 linear matrices with positive diagonal. It acts simply transitively on the patch where the fixed
time covector is timelike. To see this, write

    L=[[B,b],[0,lambda]],
    y^-1=L eta L^T.

The negative bottom-right entry determines lambda>0, the mixed column
fixes b, and the positive spatial Schur complement fixes the positive
upper-triangular factor B. This is the reverse-order Cholesky factorization;
using lower-triangular B gives an equally valid alternative frame. No physical
choice is selected by choosing one of these coordinate descriptions.

Use the left-translated native frame on S. Its connection coefficients,
principal matrices and all59 invariant background components are constant.
For the upper-triangular convention its constant lower operator is

    C0S=C0(p)+K_8 J_01+K_9 J_02+K_11 J_12.              (5)

The rotations act on **both** one-form and endomorphism tensor legs. Native
spatial generators A8,A9,A11 become A8+J01,A9+J02,A11+J12;
the adapted boost generators were already upper triangular. This is the same
owned operator in a different frame. The native control exhibits leakage from geometric-spin7 into spin5/6 under
the added rotation terms, so the preceding20 matrix is not imported here.

For a fixed physical reference slice t=t0 put

    u=(t-t0)/lambda,         r=(1/4)log det L.

The frame derivatives are exactly

    e_a r=delta_a4,
    e_3 u=1,
    e_a u=-c_a u (normal a),
    c_4=1, c_7=-3, all other c_a=0.

The spatial horizontal frame vectors annihilate u and r. Hence the **full
connection-carrier** field q(u,r) is closed under the actual linearized
operator, giving the exact equation

    [K_3-u(K_4-3K_7)] q_u+K_4 q_r+C0S q=0.             (6)

This is a test family of existing fields, not an imposed physical restriction.
Its time covector has native norm

    |du|^2=-1+u^2/8,

so it is non-null and timelike near u=0. The slice u=0 is exactly t=t0.
Neither a global domain nor a boundary condition has been added.

### Genuine analytic solution germs at every fixed frequency

For any fixed real k take q(u,r)=exp(i k r)a_k(u). Equation(6) becomes the
finite-dimensional analytic descriptor ODE

    A(u)a_k'(u)+(i k K_4+C0S)a_k(u)=0,
    A(u)=K_3-u(K_4-3K_7).                               (7)

The owned non-null constant-rank splitting gives analytic local kernel/range
frames. If a=T(u)(v,n), the extra moving-frame term is A(u)T'(u)(v,n).
Its auxiliary row vanishes because P(u)A(u)=0. Also P(u)K_4P(u)=0, so the
auxiliary block has no k dependence. At u=0, the added terms in(5) have zero
NN compression: rotations commute with P0 and P0 K_b P0=0. The auxiliary
block therefore equals the **already-certified full M**, not a new matrix.
It remains invertible on a sufficiently small u-neighborhood by continuity.

Eliminating n leaves an ordinary analytic linear ODE for v, with all moving-
frame terms retained. For each finite k and every initial range amplitude it
has a genuine local analytic solution; reconstructing n solves(7) exactly.
No uniform-in-k estimate or physical lifespan is asserted. Real and imaginary parts with conjugate
Fourier modes give native real coefficient fields, multiplied by physical i.

Thus actual local linearized solution germs exist in this full-carrier test
family. They are not merely formal time jets. The proof does not appeal to an
unjustified Cauchy-Kowalevski theorem for the second-order reduced PDE.
Their full coupled quadratic extension uses the previously owned autonomy of
the imaginary-connection block; it is not a nonlinear solution theorem.

## 6. Both canonical energy signs occur on these solution germs

The owned [normal scalar energy test](../../lab/process/source-action-receiver-strategy.json)
already certifies the principal energy for xi=theta4 and range amplitudes
V=K_3 b_j. Its complete N7 inverse is the actual full-M inverse on those
sources; no other inverse block contributes to this principal column.

| Root | j | Principal coefficient center | Error bound, rounded upward | Sign |
|---|---:|---:|---:|---|
| A | 3 | -165406.051571 | 0.000063 | negative |
| A | 12 | 496468.066840 | 0.000188 | positive |
| B | 3 | 300577.505284 | 0.000155 | positive |
| B | 12 | -931597.489600 | 0.000480 | negative |

The table is explanatory; the exact inherited rational intervals govern
acceptance. It omits the common positive normalization factors from the
quadratic action and realification. These are geometric basis indices, not
particle labels. The relevant imaginary-U sign is the one already fixed in
the owned energy calculation.

Choose one of these amplitudes as the initial range value in(7). At u=0 the
actual auxiliary field is

    n=-M0^-1(i k P0 K_4 V+P0 C0S V).

Its leading term is precisely the old normal derivative response. The frame
change affects only the O(1) part. Therefore the real solution's canonical
quadratic energy, **integrated on a fixed nonempty relatively compact patch with smooth or
piecewise-smooth boundary in the
13-dimensional ambient t=t0 slice**, has a nonzero k² coefficient of the certified sign,
with remainder O(k)+O(1). The native density and lapse contribute positive
weights. The zero non-Hermitian self-pairings checked in the old certificate
justify realification. Their exact-root validity follows from highest weight7
and SO3 equivariance of the exact M inverse, not a floating zero at the
certificate center. Equivalently one may use the positive oscillatory
average on the fixed patch.

The distinction between energy representatives matters. The old reduction
uses spatial integration by parts. On a patch with boundary, the boundary
bilinear has the form v*n and is O(k); the NN spatial symbol is zero. Hence
it cannot overturn a strict k² volume sign. We do **not** silently identify
pointwise densities that differ by a divergence. Both signs follow for
sufficiently large, finite k, with no new fitted coupling or physical norm.

This advances the negative directions from constraint-satisfying data to
**actual local analytic solutions of the linearized candidate equations**.
It does not produce compactly supported propagated fields, normalizable
ambient states, a conserved global Hamiltonian, a physical BRST class,
negative-norm particles, nonlinear runaway or an observed signal. Boundary
flux and the source's physical-state selection remain open.

## 7. Native results and verification

Exact native assembly and controls pass: 300 bracket/covector identities,
180 full-field derivative/Casimir identities, 36 original-engine lower controls,
all666 affine trilinear pairs, all20 source/ladder identities and624 inherited
response-map columns. The triangular-frame check verifies196 affine brackets,
2744 Koszul entries, the u/r characters,36 extra-lower identities and16 NN
zero compressions. It also reproduces all four inherited energy-sign bounds.
Full native operator columns0,5,12 agree at both roots; the N7 form/inverse
bindings match the owned certificates. A frozen growing branch still requires
an actual-coefficient growth/estimate argument before any PDE instability
claim. The local analytic existence and patch-energy theorem is instead
proved directly by(6)–(7).

Final replay and artifact-bound independent acceptance are recorded in the
companion certificate and review. Six checked finite Lean lemmas cover the
moving-frame auxiliary identity, frequency-independent compression, quadratic
sign dominance, the du-norm arithmetic and real-component sign extraction.
Lean does not formalize the native geometry, ODE existence theorem, full
energy proof or spectral trace theorem.

## 8. Three-state and source accounting

- **ESTABLISHED:** the corrected scalar-normal jet operator; positive-real-part
  high-frequency growth of its frozen20 matrix at both held roots; exact
  full-carrier two-variable reduction; actual local analytic linearized
  solution germs with both canonical patch-energy signs.
- **RULED OUT:** the claim that these energy witnesses are necessarily only
  off-shell or formal jets, and positivity of canonical patch energy on the
  unrestricted local analytic candidate-solution class. Geometric-spin7
  closure in the triangular frame is also ruled out by an explicit leak.
- **NOT MODELED / UNDETERMINED:** exponential-frame spin7 scalar-profile closure,
  uniform-frequency or global evolution, physical admissibility, a conserved
  global positive Hamiltonian, physical BRST quotient, negative-norm particles,
  nonlinear runaway, observed coupling and GU falsification.

SC-ACT-01 supplies action grammar, not equality with W2. SC-META-52 leaves the
upstairs boundary/Cauchy treatment open, and SC-META-53 supplies no selected
positive physical quotient. The K95 calculation is not transferred to K77.
Source2+1, independent matter bars, contraction observation, fullU/optionalC,
primary-minus adjoint and geometric/observed/physical gradings remain separate.
LT-GR1, LT-GR6b and LT-SM8 remain NEEDS; no source, physics-ledger, class-C,
canon or paper verdict changes. The candidate choice budget remains10 choice
families against4 obligation bundles, net6, with zero source-selected predictions.
