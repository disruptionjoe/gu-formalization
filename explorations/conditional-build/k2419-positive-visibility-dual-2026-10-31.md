---
title: "K2419 A narrow all-channel recovery bracket"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU or empirical verdict
scripts:
  - tests/channel-swings/k2419_positive_visibility_dual_probe.py
---

# K2419 A narrow all-channel recovery bracket

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
result: K2419
carrier: flagged positive-Hilbert qubit instrument with two original visibility-half axis laws LAYER=toy CHIRALITY=N/A
pairing: complete channel half-diamond distance ON=declared_instrument
real_structure: exact rational physical channels and Choi duals
grading: good/bad flags and signs; planar and perpendicular Bloch blocks
action_owner: repository-construction -- K2398/K2410 original instrument
target: unrestricted shared CPTP recovery bracket MAP-TYPE=evaluation
```

## Result

For the SAME two positive-visibility endpoint instruments in [K2416](k2416-positive-visibility-recovery-2026-10-31.md), the best shared good/bad CPTP recovery satisfies

    1786296137/4000100000 < E* < 447/1000.

The bracket width is1748563/4000100000, approximately0.000437129822 and strictly below0.000438. It also applies to the convex hull of the complete endpoint instruments. This narrows the prior lower bound above0.4 and upper bound below0.487. It does not prove exact optimality.

These are conditional positive-Hilbert channel results. SC-META-53 remains UNCERTAIN. No GU physical quotient, device implementation, calibrated clock law, ledger change or external novelty claim follows.

## 1. Original instrument and unrestricted symmetry

Retain the actual means m1=(125/338,150/169), m2=(49/250,−84/125), loss weights w1=73/100,w2=37/52, axis lengths25/26 and 7/10. Each physical law uses opposite unit axes u=±m/||m|| with probabilities(1±||m||)/2 and visibility1/2, so Q=uuᵀ/2.

The original sign instrument obeys J_z(AdY rho)=J_−z(rho), including its nonzero mean output. Simultaneous sign/input/output averaging pairs the decoders as R_−=AdY composed with R_+. Averaging the Kraus-conjugated channels removes perpendicular/planar mixing and translation perpendicular to the plane. These common physical mixtures work for both endpoint laws and cannot increase worst-case convex channel error. Thus arbitrary shared CPTP controllers reduce without loss to the affine planar bad map t+Ar and good planar block G with perpendicular multiplier g.

The composed bad block is B_i=t m_iᵀ+A Q_i. With C_i=I−(1−w_i)G−w_iB_i and d_i=1−(1−w_i)g, retain the complete norm

    E_i=max(d_i+L_i,L_i+H_i,2d_i)/4,
    L_i²=(tr C_i)²+(C12−C21)²,
    H_i²=(C11−C22)²+(C12+C21)².

The derivation and exact Bell-block convention are inherited from K2410; the new probe independently composes the original sign maps and verifies these blocks for the upper witnesses.

## 2. A physical all-CPTP dual

Choose weights p_i≥0 summing to1 and F_i=[[c_i,s_i],[-s_i,c_i]] with c_i²+s_i²≤1. Define

    c0=1+2 sum p_i c_i, h=sum p_i(1−w_i),
    S=sum p_i(1−w_i)F_i, r²=S00²+S01²,
    v=sum p_i w_i F_i m_i, M=sum p_i w_i F_i Q_i.

From L_i≥<F_i,C_i>, g≤1 and ||G||op≤1,

    4 max E_i ≥ c0−h−2r−sup_bad[v·t+<M,A>].

The good support bound is ||S||*=2r. Crucially, keep the bad channel's complete positivity coupling instead of independently relaxing t and A.

For output-first unnormalized Choi J, let sigma=(X,Z) and

    H=[sum v_a sigma_a⊗I + sum M_ab sigma_a⊗sigma_bᵀ]/2.

Then Tr(HJ)=v·t+<M,A>. Any Hermitian Z_d with I⊗Z_d−H positive semidefinite bounds this by Tr Z_d because J≥0 and Tr_out J=I. This is a direct weak-duality proof, requiring no claim of numerical convergence or attainment.

The exact certificate uses p=(263,237)/500, half-angle tangents−1/21 and 1/19 for F1,F2, and

    Z_d=(1851/10000)I+(37/1000)X+(59/1000)Z.

All15 original rational principal minors of I⊗Z_d−H are positive. Also c0=2990077/1000025, h=45297/162500 and r²=6250334491593/81252031250000<(1387/5000)². Substitution gives the strict rational lower bound displayed above. The full exact certificate and minors are in the saved report. Search suggested constants; exact inequalities establish the result.

## 3. Two original physical upper witnesses

First, identity recovery on the good flag and positive sign, with Y correction on the negative sign, gives t=0,A=G=I,g=1. Then L=3w/2,H=w/2,d=w, so E=5w/8 and the maximum is exactly73/160=0.45625. This already beats the prior0.487 upper witness. It does not contradict K2416's fixed-translation scalar comparison, which imposed t=(4/5,0).

Follow-through improves this with a rational physical extremal channel. Define C(z)=(1−z²)/(1+z²), S(z)=2z/(1+z²), and R(z)=[[C,S],[-S,C]]. Set

    a=C(187/1000), a_s=S(187/1000),
    b=C(29/48), b_s=S(29/48),
    e=(C(1/186),S(1/186)), R=R(−1/31), G=R(1/272),
    t=a_s b_s R e, A=R[aI+(ab−a)eeᵀ].

The bad perpendicular multiplier is b and good multiplier is1. The unrotated canonical channel has translation a_s b_s along its first axis and multipliers(ab,b,a). Its two Choi blocks obey(1±ab)²−(a_s b_s)²=(a±b)² with nonnegative diagonals; rotations are physical qubit unitaries. The probe also checks the actual rotated Choi matrix directly.

Composing these decoders with the actual original sign instrument gives H_i²<w_i²<L_i² and L_i²<(4·447/1000−w_i)² for BOTH endpoints. Thus the complete errors are below0.447; approximate values0.4469597700644 and 0.4469837897963 are orientation only, not the certificate. Convexity extends this one shared controller to complete-instrument mixtures. Do not average conditional moments without the loss weights.

## 4. Follow-through: one good unitary always suffices

This structural result applies to any uncertainty family of the stated physical planar sign instruments, with loss weights0≤w≤1, while keeping one shared controller. It removes general good-CPTP optimization from the successor problem.

The composed bad block has the actual representation B=E[(t+vAn)nᵀ]. Each t+vAn is the decoded Bloch vector of the physical pointer state vn, hence has norm≤1; ||n||=1. The nuclear-norm triangle inequality therefore gives ||B||*≤1. Consequently |tr B|≤1 and the anticonformal length H(B)≤1, even for nonsymmetric B.

For arbitrary symmetry-averaged good G,g, write its conformal projection P=[[a,b],[-b,a]], a²+b²≤1. Replacing G by P and g by 1 is a physical mixture of Y-axis rotations. It preserves L and lowers d to w. Its H=wH(B)≤w, while tr C=2−2(1−w)a−w tr B≥w, so L≥w. Its complete error is therefore exactly(w+L)/4, no larger than the old error.

Now fix b and increase a to a'=sqrt(1−b²). This is one proper Y-axis unitary on the right semicircle. Write X=2−2(1−w)a−w tr B. Its new value is X'=X−2(1−w)(a'−a), with X≥X'≥w≥0. The skew component is unchanged, so L'≤L without division by 1−w. At w=0 this includes the good-only case; at w=1 it is equality because the good channel is irrelevant. Thus the SAME unitary weakly improves every law at once. This proof uses actual physical moment laws and the flagged identity good sector; arbitrary independently specified m,Q or arbitrary instruments need not obey it.

CPTP controller sets are compact, and the supremum of continuous endpoint errors is lower semicontinuous. Hence an optimum exists even for an arbitrary nonempty family, and at least one minimizing controller has a good unitary of this form. This does not imply uniqueness, a bad-unitary optimum, an exact angle, or a solved joint minimax problem. The unrestricted search now needs only one good angle plus the physically coupled bad Choi matrix.

## Verification and remaining question

Original decoder/instrument/full-channel CP and trace preservation, Pauli composition, Bell blocks, all 15 dual principal minors, symbolic Choi-support normalization and all rational radius inequalities pass. Controls reject an invalid dual and unphysical translation-plus-identity channel. Independent quantum-channel review checks unrestricted symmetry and the same-instrument scope. The exact arithmetic corrected a preliminary rounding claim: the width is under 438 millionths, not437.

The next substantial question is an exact joint primal/dual optimum after the proved good-unitary reduction, or a stability/robustness theorem that changes an implemented-error decision. Another rounded controller alone would only tighten this already narrow conditional bracket. Any physical deployment still owes actual apparatus and clock calibration with a full-channel error budget.

Certificate: [exact report](../../lab/process/k2419-positive-visibility-dual.json); [reproducible probe](../../tests/channel-swings/k2419_positive_visibility_dual_probe.py).
