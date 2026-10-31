---
title: "K2398 One decoder for an uncertain clock law: exact robust diamond recovery"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional finite-channel mathematics; no calibrated apparatus or native GU verdict
scripts:
  - tests/channel-swings/k2398_uncertain_clock_law_recovery_probe.py
---

# K2398 One decoder for an uncertain clock law: exact robust diamond recovery

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
result: K2398
carrier: K2392 normalized two-loss survivor-sign and clock-qubit instrument, optionally with separately flagged identity branches and untouched reference LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert pairing and worst-law half-diamond distance ON=declared_carrier
real_structure: complex qubit channels and real planar first/second moments
grading: classical survivor sign and good versus two-loss flags
action_owner: repository-construction -- stipulated K2389 QND instrument and a supplied uncertainty set
target: one law-independent CPTP decoder, robust optimization and calibration interface MAP-TYPE=evaluation
```

## Result and the changed question

[K2395](k2395-planar-recovery-closed-form-2026-10-31.md) optimizes recovery for a **known** clock law. Its output polar rotation depends on that law. With one decoder chosen before an unknown law is resolved, Bell-overlap optimization need not minimize diamond error. Here the missing term is explicit, and an actual two-law example has an exactly optimal mixed-state decoder that beats the Bell-optimal pure-state decoder.

For the normalized two-loss instrument, symmetrization still permits one real qubit channel R with Bloch form t+A r on each original sign block, followed by the original output sign flip. Write planar coordinates x,z and

    B=t m^T+nu A_plane M,  f=tr B,  k=B12-B21.

Then its exact half-diamond error is

    e(R;m,M,nu) = [1+sqrt((2-f)^2+k^2)]/4.                 (1)

No law-dependent output rotation is added after choosing R. A finite physical moment polytope therefore gives an exact convex program with a four-by-four positive Choi matrix and one two-dimensional norm constraint per vertex. This is an all-CPTP result on the normalized two-loss instrument. With good flags recovered identically, complete error is w times (1). Allowing arbitrary changes to good-flag recovery is a larger optimization problem; the general formula does not settle that problem. The mirror-law example below separately proves optimality even with that freedom.

These are GU-independent conditional channel results. Imported positive Hilbert quantum mechanics, the QND/loss instrument, law class and calibration access are assumptions. Neither a physical clock law, microscopic bath nor GU physical quotient is supplied. SC-META-53 and LT-GR6b do not change.

## Why the diamond formula holds for a fixed decoder

The original unnormalized sign blocks are

    J_z(rho)=1/4[(tr rho+z m.r)I+nu(m tr rho+z M r).sigma],
    r=(tr rho X,tr rho Z), z=+1,-1.                        (2)

The sign traces depend on rho. The pairing symmetry with P=Y and averaging complex-conjugate Kraus channels used in K2392 are **common to every planar law**. Convexity and unitary/transpose invariance of diamond distance thus permit these averages without increasing worst-law error. The latter is a mixture of physical Kraus-conjugate channels, not an implemented antiunitary. The resulting paired channel is unital, has zero perpendicular input/output row and column, and planar block B above. This argument establishes the all-CPTP reduction; it does not assume the decoder is rank two, unital or optimal for any one law.

Any unital qubit channel with zero perpendicular contraction has

    ||B||_* <= 1,                                         (3)

where * is the nuclear norm (sum of singular values). To see this, perform proper input/output Bloch rotations to diagonalize B. The canonical Pauli channel has two signed contractions and third contraction zero; its four nonnegative Pauli weights require the sum of their absolute values to be at most one.

Let d1,d2 be the singular values of C=I2-B. The full linear part of id-T has singular values d1,d2,1. The nuclear-norm triangle inequality gives d1+d2>=2-||B||_*>=1. Also det C>=0 since ||B||op<=1: real eigenvalues of B are at most one, and a conjugate pair contributes a nonnegative squared modulus to det(I-B). The direct two-by-two identity

    (d1-d2)^2=tr(C^T C)-2det C
               =(B11-B22)^2+(B12+B21)^2
               =tr(B^T B)-2det B <= ||B||_*^2

therefore gives |d1-d2|<=1. These three singular values satisfy every triangle inequality, without relying on a generic numerical norm routine.

Proper singular-value rotations reduce id-T to a Pauli-diagonal, trace-annihilating map with contractions d1,d2,1, all nonnegative. Its Pauli coefficients are

    q0=(d1+d2+1)/4,
    q1=(d1-d2-1)/4, q2=(-d1+d2-1)/4,
    q3=(-d1-d2+1)/4.

The triangle inequalities make q1,q2,q3 nonpositive. The diamond norm is sum|qj|=(d1+d2+1)/2: the triangle upper bound is attained by a Bell input giving orthogonal Pauli outputs. Independent input/output unitaries preserve the norm of the difference map; they are a proof device, not a new physical decoder. Finally

    (d1+d2)^2 = tr(C^T C)+2det C
               =(2-tr B)^2+(B12-B21)^2.                  (4)

Equations (3)--(4) prove (1), including entangled references and singular boundaries. K2395's Bell equality returns exactly when B is symmetric; the common output polar rotation available for a known B cannot generally be chosen separately for each unknown B.

## A finite, exact robust optimization

Fix nu and let U be the convex hull of finitely many **physical** moment pairs (m_j,M_j), with M_j>=0, tr M_j=1 and M_j-m_j m_j^T>=0. Mixtures remain physical by mixing their actual axis laws. Use the output-tensor-input unnormalized Choi convention, J>=0 and tr_out J=I. Restrict to real J after the common averaging above. Extract

    t_i=tr[(sigma_i tensor I)J]/2,
    A_ij=tr[(sigma_i tensor sigma_j^T)J]/2.

An exact program is

    minimize s subject to J real symmetric PSD, tr_out J=I,
       ||(2-tr B_j, (B_j)12-(B_j)21)||_2 <= s for each j.  (5)

The optimal normalized error is (1+s*)/4. For fixed J the norm is convex in the moments, so the maximum over the whole polytope occurs at a vertex (possibly also elsewhere). Compactness gives attainment. The norm epigraph is convex and can equally be represented by a small positive matrix; no nonconvex optimizer-direction search is necessary. A rational feasible Choi matrix and rigorously checked constraints certify an upper bound; lower bounds require a valid conic dual or an analytic argument, not solver status alone. No generic numerical solution of (5) is asserted here.

Replacing the norm by 2-tr B_j is the maximin **Bell** problem. By ordinary compact convex minimax its objective can be related to the least favorable pointwise Bell value, but this does not establish the diamond objective. The example below proves a strict separation.

## Exact unknown-law example: randomization is genuinely better

Consider two possible laws, with a=1/4 and b=3/4:

    law +: probability a at +X, probability b at +Z;
    law -: probability a at +X, probability b at -Z.

Their means are m±=(a,±b), and both have M=diag(a,b). These are actual positive discrete unit-axis laws, not merely guessed moments. Let U include these laws and all their mixtures. Initially take nu=0. The clock is then maximally mixed, so every sign decoder is equivalent to preparing a state after reading the sign. Common P=Y sign symmetry removes the output translation. Conjugation by X exchanges the two laws. Averaging this second symmetry cannot worsen their worst-case error and leaves the prepared Bloch vectors ±c X, |c|<=1. Hence **every** decoder is bounded by the best member of this family; mixed preparation is a valid CPTP operation.

For either endpoint B±=[[ca,±cb],[0,0]]. Equation (1) gives

    4e(c)-1=sqrt(4-4ac+(a^2+b^2)c^2).

Negative c cannot improve the objective. Therefore

    c*=min(1,2a/(a^2+b^2)),
    c*=4/5,    e_rob=(1+3sqrt(10)/5)/4.                  (6)

In contrast the maximin Bell objective is ca, uniquely maximized in this symmetric family at c=1. More generally, attaining the optimal endpoint minimum a requires t_x=1 and t_z=0, hence the pure +X output. Before sign symmetrization, this requires the two prepared Bloch vectors to differ by2 in the X direction, forcing the pure pair +X,-X. Its optimum therefore does not conceal a better nonsymmetric choice. Its actual diamond error is

    e_pure=(1+sqrt(58)/4)/4 > e_rob,                     (7)

while its Bell-complement proxy is (3-a)/4=11/16. The comparison between the radical squares in (7) is exact: 58/16-18/5=1/40>0. No numerical discrimination is needed. The decoder in (6) prepares rho_c=(I+(4/5)X)/2; it can be synthesized by preparing +X or -X with probabilities 9/10 and1/10, then applying the sign-dependent flip. Randomness, reset, sign processing and state preparation remain resource costs.

If the law were known, K2395 at nu=0 would give

    e_known=(3-sqrt(10)/4)/4,

which is strictly lower than (6). Thus both swapping max/min across a decoder choice and dropping the antisymmetric diamond term fail on a physical finite law. The better robust decoder remains entanglement breaking and does not restore erased quantum information.

### Good flags cannot improve this particular optimum

Now take a fixed probability w of the displayed two-loss instrument and a flagged identity channel with weight1-w, identical for both laws. Permit arbitrary CPTP recovery on the good flag as well. The same P and X symmetries make the good-flag channel a Pauli-diagonal channel G with diagonal entries g_x,g_y,g_z<=1, and again force bad-flag preparation ±cX. For complete id-T, the planar matrix is

    C±=[[1-(1-w)g_x-wca, -/+wcb],
        [0,                1-(1-w)g_z]],

and the perpendicular contraction is d_y=1-(1-w)g_y>=w. Both planar diagonal entries are nonnegative and their sum is at least w(2-ca). Its determinant is nonnegative, so

    ||C±||_* >= w sqrt((2-ca)^2+c^2b^2).

The proper-SVD Pauli trace-norm lower bound, without requiring the triangle equalities, gives half-diamond error at least (d_y+||C±||_*)/4. One way to see the bound is to retain the absolute identity Pauli coefficient; the other coefficients sum to its negative. This yields at least w e(c). Good-flag identity together with c* attains w e_rob. Consequently (6) times w is globally optimal over all complete flagged decoders **for this mirror family**. This is not an assertion for arbitrary uncertainty sets.

## Positive visibility: a certified finite continuation

The difference between pointer states with visibilities nu and0 has half trace norm nu/2 for each actual unit axis. The instrument is measure-and-prepare, with orthogonal sign records, so convexity and reference stability give

    half||N_nu-N_0||_diamond <= nu/2.                    (8)

The same bound holds after every fixed decoder, and therefore for the difference of robust optimal values. For the complete model it is w nu/2. This is a channel bound, not the unsupported inference from closeness of optimum Bell values.

The mixed preparation decoder ignores the pointer, so its value (6) stays exactly unchanged for every nu. The identity-pointer decoder has normalized error (3-nu)/4 for every planar law. At nu=1/100 the mixed decoder still strictly beats identity, since 3sqrt(10)/5<2-1/100. The robust optimal value lies in

    e_rob-1/200 <= e_rob(nu=1/100) <= e_rob.             (9)

The Bell-maximin error proxy is at most 11/16 (pure preparation remains feasible), whereas the lower endpoint in (9) is strictly greater than 11/16. The pointwise Bell/diamond transfer therefore fails at strictly positive visibility too. Equation (9) is an exact enclosure, not the exact positive-visibility optimum or its optimal channel.

The smaller gap between the two fixed preparation decoders in (6)--(7) persists exactly, since both ignore the pointer. This does not prove that pure preparation is Bell-optimal when nu>0. To prove all positive-visibility Bell-optimal channels suboptimal in diamond would require an additional optimizer analysis; no such assertion is made.

### A coherent improvement and an exact two-variable reduction

The positive-visibility problem can be pushed beyond the continuity bound. Take the amplitude-damping channel toward +X with

    t=(4/5,0,0),  A=diag(1/5,1/sqrt(5),1/sqrt(5))

in x,y,z order. If H is the Hadamard matrix, its two Kraus operators are

    H diag(1,1/sqrt(5)) H,
    H [[0,2/sqrt(5)],[0,0]] H.

This is a concrete rank-two CPTP map, used on each original sign block before the output sign flip. For either mirror law, f=1/5+nu(1+3sqrt(5))/20 and |k|=3/5. Hence it attains

    E_coh(nu)={1+sqrt([9/5-nu(1+3sqrt(5))/20]^2+9/25)}/4. (9a)

For every0<nu<=1 it strictly improves on the mixed preparation value (6): the positive radial component9/5 is reduced without reaching zero, and the skew component is unchanged. At nu=1/100 this is an exact improved upper endpoint for (9). It is an attained channel value, not the optimal positive-visibility value. Unlike preparation, this decoder uses actual pointer coherence; its reset, rotation and damping synthesis costs must enter (12).

For the mirror family the two symmetries also reduce arbitrary decoders at positive visibility to t=cX and diagonal A=diag(x,y,z). Complete positivity is exactly

    c^2+(y+z)^2 <= (1+x)^2,
    c^2+(y-z)^2 <= (1-x)^2,  |c|<=1-|x|.

The Choi matrix splits into two positive two-by-two blocks, so these conditions include the diagonal inequalities. Signs of c,x,z may be made nonnegative without hurting the objective: c enters the CP conditions squared; changing x to -x while changing y to -y exchanges the two inequalities; changing z,y together negates both combinations. These replacements raise f while leaving k^2 unchanged, and 2-f is positive for every physical B. For fixed c,x the largest allowed z is

    z_max(c,x)=[sqrt((1+x)^2-c^2)+sqrt((1-x)^2-c^2)]/2,
    y=[sqrt((1+x)^2-c^2)-sqrt((1-x)^2-c^2)]/2.

Thus the **exact** normalized robust optimum is obtained by minimizing

    [2-ac-nu(a x+b z_max(c,x))]^2+b^2c^2                 (9b)

over0<=c<=1 and0<=x<=1-c, then taking (1+sqrt(minimum))/4. Equivalently retain variables c,x,y,z and the two CP norm constraints above, plus the objective norm constraint; that is a small convex conic program. The two-variable expression alone is not claimed to be a convex parametrization, and a numerical minimum without certification is not acceptance evidence. The good-flag lower-bound argument also extends to this diagonal mirror family, so its complete optimum multiplies by w even with arbitrary good-flag decoders. No general-uncertainty extension of that statement is made.

At nu=0 this reduces to (6); at nu>=1/2 the pointwise identity-optimality test on the **midpoint** law m=(1/4,0), M=diag(1/4,3/4) proves the identity-pointer decoder is robust optimal. Indeed m^T M^-1 m=1/4, and this midpoint lies in U; identity gives the same error for every member. The remaining interval0<nu<1/2 has the exact conic formulation and witness (9a), but no closed-form optimal value is asserted.

## Calibration without an unpriced timestamp oracle

The clock angle need not be observed directly. On separately prepared calibration inputs rho_j=(I+sigma_j)/2 for j=x,z, measure the survivor sign z and the clock Pauli observable sigma_i with outcome y=±1. Equation (2) gives

    E[z]=m_j,             E[z y]=nu M_ij.                (10)

Use four settings (i,j) in {x,z}^2 with n independent normalized two-loss calibration records per setting. Keep two designated sign means, one for each j, and all four correlation means. Each is a mean of bounded ±1 variables. Regardless of correlations among statistics in one setting, a union bound gives simultaneous error radius

    epsilon_n=sqrt(2 log(12/alpha)/n)

with probability at least1-alpha. Explicitly, a variable in[-1,1] obeys the centered moment-generating bound E exp(t(X-EX))<=exp(t^2/2); independence, Chernoff's inequality and both signs give probability at most2exp(-n epsilon^2/2) for one mean. Summing six such bounds gives the displayed radius. The inputs, measurement axes, i.i.d. calibration law and calibrated visibility are additional operational assumptions. Calibration data must come from the same conditional law as recovery, or a separately justified transfer allowance is required.

For a supplied finite axis alphabet {n_l}, put unknown masses p_l>=0, sum p_l=1, m=sum p_l n_l and M=sum p_l n_l n_l^T. Intersect the simplex with the six confidence slabs from (10). This is a **physical** compact polytope, all of whose vertices correspond to actual laws. Apply (5) to those vertices and freeze its decoder before deployment. On the confidence event its certified upper bound applies to the true law. The recovered guarantee has confidence1-alpha; data-dependent decoder selection does not invalidate it because coverage of the entire confidence set is simultaneous. An empty set is an incompatibility/coverage event, not permission to replace the law by an arbitrary convenient estimate. A predeclared identity-pointer fallback remains available.

For a continuous unknown alphabet the feasible moment set is generally a spectrahedron, not this finite polytope. It requires robust separation or a rigorously controlled approximation; arbitrary vertices of a box need not be physical, and (1) must not be applied to nonchannels. Unknown visibility likewise must be modeled jointly or bounded as a separate instrument error; its product with unknown M is not silently linearized.

The total cost is not merely4n stored records: obtaining n two-loss records per setting has random exposure cost. With fixed i.i.d. two-loss probability w>0 and no extra selection bias, expected exposure count is4n/w. This is an expectation, not a deterministic acquisition-time budget; w=0 supplies no such calibration records and makes the corresponding complete recovery issue irrelevant. Preparation, pointer measurements, discarded outcomes, reset, and law drift must be included in a same-apparatus comparison. No record samples or device rates are fabricated here.

## Robustness and the implementation decision

For a fixed decoder, two physical descriptions give planar difference

    Delta B=t Delta m^T+A_plane Delta(nu M).

The half-diamond distance between the resulting unital zero-perpendicular channels is at most ||Delta B||_*/2, by a singular-value/Pauli decomposition. Trace-distance contraction gives ||A||op<=1 and ||t||<=1, so a convenient bound is

    half||T-T'||_diamond
       <= [||Delta m||_2+||Delta(nu M)||_*]/2.             (11)

Unlike K2392's optimum-value Lipschitz bound, this applies directly to the **same fixed** implemented recovery channel without choosing a fresh polar rotation. It can price confidence-set approximation or a separately supplied moment-transfer allowance. Changes to the underlying sign instrument, losses, good flags or reference accessibility require their own complete channel bound.

If a certified normalized robust bound is E and the complete implementation is within half-diamond eta of the intended complete channel, then the complete error is at most wE+eta. Comparison with the **ideal** identity-pointer baseline is guaranteed when

    eta < w[(3-nu)/4-E].                                (12)

For the mirror fixture with nu=1/100, E=e_rob gives a strictly positive exact margin. Two actual devices require both complete budgets; (12) does not price an unprovided apparatus. Finite training must also fit the available calibration shots and stability interval. These costs can eliminate a formal improvement without changing the theorem.

## Alternatives, verification and continuation

The preflight comparison was between: (a) extending an already solved pointwise planar formula; (b) pricing an actual finite controller, which needs a specified apparatus and rates; and (c) removing exact-law knowledge while keeping one decoder and its reference-aware loss criterion. The third changes a live operational premise and produces an exact counterexample, an optimization procedure and a measurement interface. K2389 already covered the completely unrestricted-law minimax identity-pointer result; the new question is a partially calibrated uncertainty set where the nominal nonunital optimum cannot be retuned to the unknown law. K2392's Bell-value stability bound did not supply the fixed-decoder formula (1).

Robust recovery by convex optimization is established literature; see Kosut, Shabani and Lidar, [Robust Quantum Error Correction via Convex Optimization](https://arxiv.org/abs/quant-ph/0703274), PRL100,020502 (2008). The Choi/diamond-program background is Watrous, [Semidefinite programs for completely bounded norms](https://cs.uwaterloo.ca/~watrous/Papers/SDPforCBnorms.pdf) (2009). We make no general novelty claim for robust quantum recovery or conic programming. The contribution here is the exact supplied-instrument reduction, the explicitly realizable failure of the pointwise transfer, and its finite calibration/resource interface.

The companion probe checks actual positive moment laws, Choi normalization/positivity, original sign-block composition, a Bell trace-norm certificate independently of the radical formula, the mixed versus pure optimum identity, exact positive-visibility margins, calibration expectations and changed-input controls. Universal all-CPTP and confidence claims rest on the written proofs, not finite sample counts. The weakest seam is replacing unknown-law recovery by a different law-dependent polar rotation; the offdiagonal control must detect that change. Independent internal review is required; no proof-assistant, external-expert or hardware certification is implied.

Postflight lenses preserve the distinction between normalized and complete recovery, all-CPTP proofs and fixed-decoder bounds, confidence coverage and data evidence, physical moment vertices and arbitrary boxes, and mathematical gain and complete implementation cost. The next substantive continuation is a supplied calibration record with a declared axis law, known/estimated visibility, transfer bound and same-device costs, or an independently certified positive-visibility solution of (5) that improves on mixed preparation. Neither creates native GU confirmation.
