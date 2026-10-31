---
title: "K2407 Finite certificates for robust planar recovery"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional channel mathematics; no measured calibration, hardware or native GU verdict
scripts:
  - tests/channel-swings/k2407_finite_minimax_certificates_probe.py
---

# K2407 Finite certificates for robust planar recovery

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `CONVENTIONAL_COMPARATOR`.

```gu-typed-objects
result: K2407
carrier: physical planar clock moment uncertainty and one common CPTP decoder LAYER=toy CHIRALITY=N/A
pairing: declared conditional probability or positive Hilbert channel pairing ON=declared_carrier
real_structure: real probabilities and exact rational or algebraic coefficients
grading: observed records, hidden roles and conditional parameters
action_owner: repository-construction -- K2395/K2398 sign instrument at variable visibility and fixed loss weight
target: finite minimax certificates, physical moment cone and exact robust flagged recovery MAP-TYPE=evaluation
```

## Result and scope

[K2404](k2404-rotation-uncertain-recovery-2026-10-31.md) solves a fixed-trace identity criterion and one variable-trace segment. Here any nonempty compact set U of physical planar axis/visibility laws admits an exact minimax certificate supported on at most seven laws. One fixed decoder works for all laws. A certified physical epsilon-net gives a quantitative approximation guarantee. A genuinely scalene, variable-trace uncertainty fixture has an exact optimizer. The complete flagged problem also has this normalized optimum multiplied by the fixed bad-flag weight w, even when good-flag recovery is optimized.

These are positive-Hilbert qubit-channel results for the supplied sign instrument. They do not construct the source's interacting physical quotient, resolve SC-META-53 UNCERTAIN, or change LT-GR6b, source polarities or the physics ledger. The seven-law theorem is a certificate existence/reduction result, not an algorithm that finds a certified covering oracle for arbitrary described compact sets.

## 1. Exactly physical moments, including variable visibility

Let n be a unit vector in the x,z plane and v∈[0,1]. Define m=E n, Q=E[v nn^T], q=tr Q. A pair(m,Q) is physically realizable exactly when Q>=0, q<=1 and there exists h such that

    [[q,h^T],[h,Q]] >=0,             ||m-h||_2 <=1-q.       (1)

Necessity: split each probability mass into a visible portion v and an invisible portion1-v. The visible submeasure has mass q, first moment h=E[v n] and second moment Q. The remaining submeasure has mass1-q and mean m-h.

Sufficiency: the positive3x3 moment matrix with upper-left entry q and lower-block trace q is a moment matrix of a measure of mass q on the unit circle. For q>0 normalize to q=1. Its compact spectrahedron has rank-one extreme points: at rank r>=2 a symmetric perturbation in its range has dimension r(r+1)/2>=3, exceeding the two scalar affine constraints, so a nonzero two-sided feasible perturbation exists. Rank-one extremes are(1,n)(1,n)^T with ||n||=1. Finite-dimensional convex decomposition gives the measure. At q=0 positivity forces h=Q=0. The residual mean ball is realized by antipodal unit axes with total mass1-q, assigned v=0. Assign v=1 to the visible part. This proves(1), including q=1.

The hidden h cancels from the recovered sign channel, but is essential to certify that(m,Q) comes from a physical instrument. Q>=0 and trace alone are insufficient: m=X,Q=ZZ^T is impossible because q=1 forces h=m and the moment matrix is indefinite.

## 2. Exact finite minimax certificate

For a real CPTP decoder R(r)=t+A r, retain its planar coordinates x=(t_x,t_z,A_xx,A_xz,A_zx,A_zz). Common Kraus-conjugation averaging is admissible for all planar laws simultaneously, as in K2398; it cannot worsen worst error. Write

    B_u=t m^T+A_plane Q, f_u=tr B_u, k_u=B_12-B_21,
    r_u(x)=sqrt((2-f_u)²+k_u²), E_u=(1+r_u)/4.             (2)

The exact diamond formula is K2398's original-sign-channel theorem; this is not a Bell-overlap surrogate. Every recovered bad channel is measure-and-prepare and ||B||_*<=1, hence f<=1 and r>=1. The projected real CPTP set C⊂R^6 is compact convex. Minimize r*=min_C max_U r_u. A maximizer over a convex hull occurs at an extreme law, but U need not itself be convex.

At x*, each active r_u is differentiable because r_u>=1. Set

    a_u=(2-f_u(x*))/r*,       b_u=k_u(x*)/r*,
    ell_u(x)=2a_u-a_u f_u(x)+b_u k_u(x).                  (3)

Then ell_u<=r_u everywhere and equality holds at x*. Convex optimality supplies a convex combination g of active gradients with g·(x-x*)>=0 for all x∈C. The subgradient formula follows directly from the maximum of a compact continuous differentiable family. Caratheodory in R^6 reduces g to at most7 active gradients: if a representation has more than7 points, affine dependence allows changing weights until one vanishes, preserving the sum and g; repeat. Because every active support equals r* at x*, the same weights p_i satisfy

    min_C sum_i p_i ell_i = r*.                           (4)

Thus those at most7 physical laws already force the entire robust optimum. This does not say arbitrary7 sampled laws suffice.

A concrete Choi certificate implements(4). Use unnormalized J>=0 with tr_output J=I_input, ordered output⊗input. For each law/direction form the real symmetric K_i satisfying tr(K_i J)=-a_i f_i+b_i k_i. With Kbar=sum p_i K_i, any symmetric input Y obeying

    Kbar-I_output⊗Y >=0                                  (5)

gives r*>=2 sum p_i a_i+tr Y. A globally feasible decoder J*, radius r_upper, physical laws, unit directions and positive weights whose bound equals r_upper form an exact certificate. Strict feasible J=I4/2 gives attained SDP duality here; alternatively a displayed(5) needs no duality theorem to verify its lower bound. The finite-witness existence proof uses the standard finite-dimensional separating-hyperplane/normal-cone characterization, not a computed rank.

## 3. Arbitrary good-flag recovery cannot improve the fixed-weight optimum

Let the bad-flag probability w∈[0,1] be fixed across U. The two good-sign decoders may initially be arbitrary. The common sign symmetry and real-channel averaging reduce their effective channel to a unital map with planar block G and perpendicular scalar g_y; the bad branch retains one real R. These are common physical mixtures, with no law-dependent choice. Contractivity gives ||G||op<=1 and g_y<=1.

The weighted dual witnesses above have sum p_i b_i=0. To see this, compose the optimal bad decoder with a small output rotation in the plane. With the convention f'=k,k'=-f, differentiation of r gives -2b. The weighted support is minimized over all CPTP maps and this rotation is two-sided feasible, so its derivative vanishes. Also every a_i>0 since f_i<=1.

For any law the complete unital plane is T_i=(1-w)G+wB_i and perpendicular contraction(1-w)g_y. Put C_i=I-T_i and d_y=1-(1-w)g_y. Since ||T_i||op<=1, det C_i>=0: real eigenvalues are at most1 and a complex-conjugate pair gives a positive product. Proper planar singular-value rotations, together with the perpendicular axis, reduce the Choi difference to the Pauli-diagonal case. The Bell-input half trace norm lower bound is at least

    [d_y+||C_i||_*]/4.                                    (6)

Indeed its identity-Pauli coefficient is(d_y+s1+s2)/4>=0 and the other coefficients sum to its negative; the total absolute coefficient sum is at least twice that coefficient. This lower bound does not require triangle inequalities among s1,s2,d_y.

For any2x2 C and a²+b²=1, ||C||_*>=a tr C-b(C12-C21), by duality with the orthogonal matrix [[a,-b],[b,a]]. Apply each witness, take the weighted sum and use(4) and sum p_i b_i=0. Every pair of good/bad decoders has worst normalized complete error at least

    w(1+r*)/4 +(1-w)[1-g_y+abar(2-tr G)]/4 >= w(1+r*)/4.  (7)

Good identity and the optimal bad R attain exactly w(1+r*)/4 by homogeneity of diamond norm. This proves the complete optimum. At w=0 it is zero. A law-dependent loss weight breaks the factorization in(7) and is outside this theorem.

## 4. Certified approximation without a false oracle

For two physical moments define d(u,u')=||m-m'||_2+||Q-Q'||_*. Any CPTP map has ||t||<=1 and ||A_plane||op<=1. Hence ||Delta B||_*<=d. The2x2 identity

    (tr D)²+(D12-D21)²=||D||_F²+2det D <=||D||_*²

and norm Lipschitzness in(2) give |E_R(u)-E_R(u')|<=d/4, uniformly in R. If a finite physical N⊂U is a certified epsilon-net in this metric, then

    E_N <= E_U <= E_N+epsilon/4.                          (8)

An optimizer on N is epsilon/4-optimal for U. Add its actual certificate gap if optimization is approximate. A guessed grid, numerical sampling, compactness alone or a nonphysical moment outer point does not supply the needed covering certificate. Fixed-weight complete errors multiply by w. An independently justified complete-channel half-diamond implementation error zeta adds at most zeta; a moment covering error and device error have different meanings and must be priced separately.

## 5. Exact scalene variable-trace fixture

Take the convex hull of three Q=0 laws with means

    mA=(11/68,27/68),
    mB=(1099/3604,-3237/3604),
    mC=(1/4,3/4),

and a fourth law(mD=X,QD=XX^T). The first three are physical: ||m||<1 and an antipodal axis law realizes each mean with v=0. The fourth has deterministic n=X,v=1. Pairwise squared distances among A,B,C are90/53,9/68,9801/3604, so this triangle is scalene. The fourth endpoint introduces genuinely variable trace.

Use the fixed CPTP decoder R=(Id+4 prepare X)/5, t=(4/5)X,A=I/5. Its actual Choi matrix is positive and trace-preserving. The first three radii in(2) all equal

    r*=3sqrt(10)/5,        E*=(1+3sqrt(10)/5)/4.            (9)

Endpoint D has B=XX^T and radius1, strictly slack. Convexity of the norm gives the global upper bound over the entire four-vertex hull.

The exact weights(pA,pB,pC)=(1/4,53/132,23/66) have weighted mean(1/4,0). Put(a_i,b_i)=((2-(4/5)m_ix),(4/5)m_iz)/r*. Direct rational identities give sum p_i b_i=0, sum p_i a_i=r*/2, and Kbar=0: the coefficients of both t_x,t_z vanish and all Q_i are zero. Taking Y=0 in(5) proves lower radius r* for EVERY decoder. Thus(9) is the exact all-CPTP robust optimum; (7) proves complete optimum wE*. The finite check verifies original sign composition, not just moment declarations. Dropping skew or allowing law-dependent rotations gives a strictly wrong objective at an actual endpoint.

## Verification and continuation

The [probe](../../tests/channel-swings/k2407_finite_minimax_certificates_probe.py) checks actual physical instrument Choi matrices, decoder CP/TP, original sign composition, exact dual cancellation, endpoint radii, moment-cone controls and approximation algebra. Universal moment representation, finite-support existence and flagged lower bound use the written proofs and independent internal review; pass counts do not certify those theorems independently. No external-expert, proof-assistant, hardware, empirical or novelty claim. Actual use requires a physically justified uncertainty set with a certified covering/separation description and complete device/calibration costs. Variable loss and nonplanar laws are distinct successors.
