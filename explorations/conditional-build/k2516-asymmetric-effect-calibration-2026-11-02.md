---
title: "K2516 Sharp asymmetric effect calibration and optimal sector pooling"
status: active_research
doc_type: exploration
created: "2026-11-02"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional finite-dimensional effect and trusted calibration theorem; no hardware or GU certification"
---

# K2516 Sharp asymmetric effect calibration and optimal sector pooling

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
result: K2516
carrier: full retained finite Hilbert carrier with supported subspace S and original C108 Q/T verifier LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace ON=declared_carrier
real_structure: complex adjoint; real rational matrix controls
grading: projection sectors and retained-memory support
action_owner: repository-construction -- supplied CPTP storage and trusted preparation/readout
target: sharp supported effect bound and optimal two-sector wrong-event pooling MAP-TYPE=evaluation
```

## Result and scope

K2504 already handles arbitrary full-memory completely positive trace-preserving (CPTP) maps, including cross-plane and nonunitary errors. Repeating that coverage would add nothing. The new result is the exact worst-case effect error from **unequal** sector wrong-trace caps, followed by an optimal randomized two-sector test for a fixed accuracy. It improves the previous symmetric square-root bound and its dimension weight without a layered-unitary or spectator-plane promise.

The two-sector minimax theorem is for this specified labeled wrong-event design and arbitrary effects. The outer Q/T/leakage composition is sufficient, not asserted jointly minimax over channels or all quantum experiments. Complete retained memory, trusted inputs/readouts, fresh calibration trials and worst-history deployment coverage remain premises. The result is independent positive-Hilbert mathematics: SC-META-53 remains UNCERTAIN, LT-SM8/LT-GR6b retain their native quotient/domain debts, and source polarities, ledger0.263, canon and physical credit remain unchanged. No measured apparatus, novelty, external-expert or proof-assistant certification is claimed.

## 1. Exact two-sector operator law

Let 0<=A<=I, let R be a nontrivial orthogonal projection, and put

    E=R(I-A)R, G=(I-R)A(I-R), D=A-R.
    a=min(1,Tr E), b=min(1,Tr G).

More generally any caps 0<=a,b<=1 on ||E||,||G|| suffice. Define

    f(a,b)=(|a-b|+sqrt((a-b)^2+4 min(a,b)))/2.          (1)

Then ||D||<=f(a,b), and this is the best possible bound given just these caps, in every pair of nonzero sector dimensions.

**Proof.** Compress A to the span of normalized components of an arbitrary vector in Ran R and Ker R. It has the form

    [[1-e,c],[conj(c),g]], 0<=e<=a, 0<=g<=b,
    |c|^2<=min((1-e)g,e(1-g)),                         (2)

by positivity of A and I-A. Its difference from diag(1,0) has norm at most f(e,g): if e>=g, use |c|²<=g(1-e) in the exact two-by-two eigenvalues; if g>=e, use the other determinant bound. The Rayleigh quotient of D on the original vector is the same compressed quotient, so supremizing proves the claim once f is nondecreasing in both variables.

On a>=b, f is the nonnegative root of f²-(a-b)f-b=0, lies in[0,1], and implicit differentiation gives f_a=f/(2f-a+b)>=0 and f_b=(1-f)/(2f-a+b)>=0 wherever the denominator is positive. Extend by continuity at zero and across a=b; symmetry covers the other half. This proves the monotonicity without assuming the effect blocks commute.

For a>=b, the two-by-two effect

    A_*=[[1-a,sqrt(b(1-a))],[sqrt(b(1-a)),b]]           (3)

has determinant0 and eigenvalues0,1-a+b in[0,1]. Its defect norm is exactly f(a,b). For b>=a use offdiagonal sqrt(a(1-b)); I-A_* then has determinant0. Extend by the perfect projection on all other coordinates. Sector traces equal the caps exactly. These are actual channel effects: the measure/prepare channel with probabilities Tr(A_* rho),Tr((I-A_*)rho) and orthogonal output states in the two R sectors is CPTP and has Phi*(R)=A_*. Thus sharpness is not an arbitrary Hermitian-matrix fiction.

At a=b=t the law is sqrt(t), attained by a coherent rotation. At b=0 it is a, attained by a one-way nonunitary error. Hence a linear bound in both errors fails, while using sqrt(max(a,b)) loses the asymmetric information. Neither a full-channel norm bound nor a simultaneous Q/T eigenbasis is used.

## 2. Nonlinear acceptance and exact optimal pooling

Fix 0<epsilon<=1/2. Squaring (1) on either half-plane gives the equivalence

    f(a,b)<=epsilon
      iff min(a,b)+epsilon |a-b|<=epsilon².            (4)

The right side already implies |a-b|<=epsilon, making the squaring legitimate. The acceptance set is the union of two triangles; its frontier has vertices (epsilon,0),(epsilon²,epsilon²),(0,epsilon). Requiring both a,b<=epsilon² keeps only an unnecessarily small square.

Let r<=s be the two sector ranks; label the smaller-rank sector first regardless of whether it is R or I-R. Its wrong means are p_r,p_s, with raw wrong traces x=r p_r,y=s p_s. Set

    D_e=r(1-epsilon)+s epsilon,
    q_r=r(1-epsilon)/D_e, q_s=s epsilon/D_e,
    mu=q_r p_r+q_s p_s,
    tau=epsilon²/D_e.                                 (5)

If mu<=tau, then (1-epsilon)x+epsilon y<=epsilon². For clipped a=min(1,x),b=min(1,y),

    min(a,b)+epsilon|a-b| <=(1-epsilon)a+epsilon b
                           <=D_e mu,

because epsilon<=1/2. Therefore (4) certifies ||A-R||<=epsilon. Equivalently every bad effect has mu>tau. This gate is sufficient and can reject an effect which is itself within tolerance.

**Exact minimax within the labeled design.** For arbitrary smaller-sector probability q, consider the sharp effects with caps (epsilon²,epsilon²) and (0,epsilon), approached from outside the acceptable region. Their infimum wrong means are

    epsilon²(q/r+(1-q)/s),  epsilon(1-q)/s.             (6)

They are realized by (3), including coherent rotation and a one-way reset. The first expression increases with q (or is constant if r=s), while the second decreases. They intersect at q=q_r in(5), with common value tau. If q<=q_r the first gives an upper bound tau on the worst-failure infimum; if q>=q_r the second does. Design(5) attains tau by the preceding theorem. The third frontier vertex has mean epsilon(1-epsilon)/D_e>=tau and cannot lower the value. At r=s the design remains optimal, though need not be unique. Equality cases use limits of strict failures; passing at equality is not falsely counted as failure.

The new effective weight is W_R=1/tau=r/epsilon²+(s-r)/epsilon. The symmetric K2504 pooling assigns (r+s)/epsilon² to this one projection. For small epsilon the new leading coefficient is the smaller sector rank. This is a single-effect test-design theorem, not a bound on all conceivable experiments.

## 3. Original verifier, leakage and finite confidence

Use K2504's full retained H/E carrier, S=I_H tensor P_E0, k=dim E0 and d=108k. The compressed A_R=S Phi*(R)S is an effect on S for every complete-carrier CPTP Phi; it need not preserve S, be unitary, or commute with Q/T. The supported ranks are Q:10k/98k and T:12k/96k. Apply (5) to each separately; Q and T need not commute. Leakage L=S Phi*(I-S)S is positive with ||L||<=d p_L from uniform S/d input.

Mix the two optimal projection protocols and the leakage protocol with outer probabilities W_Q/W,W_T/W,W_L/W, where

    W_Q=10k/epsilon²+88k/epsilon,
    W_T=12k/epsilon²+84k/epsilon,
    W_L=108k/ell, W=W_Q+W_T+W_L.

If the pooled wrong mean mu<=1/W, positivity gives mu_R<=1/W_R and p_L<=ell/d, so both effect errors are <=epsilon and leakage<=ell. This retains exactly five mixed input/readout distributions. It does not identify the channel or certify its disturbance outside the named effects. The simultaneous compatibility of worst Q and T effects is not used to claim a globally optimal outer allocation.

Reuse K2504's exact one-sided binomial upper limit U for one frozen map and alpha/G for G predeclared map classes. Private labels, identical deployed/calibrated maps, independent fresh-reset trials and complete retained memory are explicit assumptions. For weighted preparation/readout probability bias xi_eff, the sufficient confidence gate is

    U+xi_eff<=1/W.                                    (7)

It holds simultaneously at confidence at least1-alpha by the union bound. With zero wrong counts and v=1/W-xi_eff>0, n>=ceil(log(G/alpha)/[-log(1-v)]) suffices. At zero bias, n=ceil(W log(G/alpha)) is a conservative sufficient count. Positive systematic slack is necessary for this protocol; collecting more shots does not cure an unbounded bias. Nonzero counts use the exact upper limit, and fixed-n inference does not permit unlicensed optional stopping.

Each actual and proof-hybrid deployment gap must use a covered full-memory map, or a separately justified convex mixture of covered maps. Calibration of one average channel does not establish such history coverage. Untouched-reference scope follows from the operator theorem. No new primitive-isolation or layered-membership promise is required, but complete input preparation and readout are still trusted.

## 4. Released full-record resource consumer

For the same k=2 retained-memory support used in K2514, choose epsilon=ell=10^-6, G=1, alpha=1/100, zero bias and zero wrong counts. Then

    W=44/epsilon²+344/epsilon+216/ell
     =44,000,560,000,000,
    n=5W=220,002,800,000,000                           (8)

suffices since log100<5. The old generic same-carrier K2504 weight is 432/epsilon²+216/ell=432,000,216,000,000. Its corresponding sufficient sample count is more than9.8 times(8). This compares specified conservative sufficient designs under passing-data assumptions, not actual experiment time or an information-theoretic optimum over all experiments. The structured K2514 design can be cheaper under its narrower promises; it is not superseded.

For two covered gaps, the reused K2500 complete-record theorem gives

    E_record<=512(2*10^-6)+1024 sqrt(10^-6*10^-6)+10^-6
             =2049/10^6.

If ideal acceptance>=1/2 and ideal bad-and-accepted mass0, conditional error<=2049/497951<1/200. Statistical confidence failure is separate. This is a hypothetical certified consumer, not passing hardware data.

## 5. Contrary constructions and evidence boundary

Coherent a=b errors refute a linear wrong-count bound; one-way resets refute a one-endpoint test outside a unitary class. A hidden rotated vector inside a high-rank sector exposes the required trace/rank factor. Complex offdiagonal phase changes do not alter the sharp norm. Removing either A>=0 or I-A>=0 destroys (2). Sector-label changes without changing ranks/weights can invalidate (5). Preparation bias, calibration/deployment side channels and correlated hidden memory are not removed by sharp statistics.

The exact probe checks scalar characteristic identities, rational sharp effects and their PSD minors, actual measure/prepare Kraus completeness, complex and higher-rank embeddings, boundary tests, label minimax identities and resources. Universal results rest on the compression/monotonicity and decision-boundary proofs above, not a count of finite samples. Independent internal review challenges these proofs and probe evidence. The predecessor confidence and complete-record theorems are reused rather than rerun. The general context of gate verification is [Zhu and Zhang](https://arxiv.org/abs/1910.14032); that paper is not a novelty certificate for this specialized result.

Next: independently justified preparation/readout and history coverage, or jointly optimal Q/T/leakage designs retaining their actual noncommuting geometry. The single-effect minimax result does not settle that joint problem.

[Exact probe](../../tests/channel-swings/k2516_asymmetric_effect_calibration_probe.py), [saved report](../../lab/process/k2516-asymmetric-effect-calibration.json), [K2504](k2504-verifier-sector-calibration-2026-11-02.md), [K2514](k2514-structured-spectator-calibration-2026-11-02.md).
