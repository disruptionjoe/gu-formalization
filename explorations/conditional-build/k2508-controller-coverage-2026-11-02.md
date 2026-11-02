---
title: "K2508 Coherent controller coverage and finite parameter calibration"
status: active_research
doc_type: exploration
created: "2026-11-02"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional supplied-model mathematics; no native GU realization, experimental certification or global stopping optimum"
---

# K2508 Coherent controller coverage and finite parameter calibration

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
result: K2508
carrier: original C108 Q/T verifier with retained memory E and supported subspace E0 LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace or original failure-inclusive probability cost ON=declared_carrier
real_structure: complex adjoint for effects; real probabilities for stopping
grading: original verifier sectors or finite stopping stages
action_owner: repository-construction -- supplied instruments and original probability law
target: coherent-control amplification and constructive uniform parameter coverage MAP-TYPE=evaluation
```

## Result and scope

A finite parameter net plus a trusted effect-continuity model supplies the uniform deployment premise left abstract in K2506. The certificate applies simultaneously to every allowed history-dependent mixture of the declared full-memory maps, including proof-hybrid histories. Basis-state controller tests can also certify coherent use, but coherence requires a sharp dimension penalty unless the controller has a proved block-diagonal effect structure. An explicit unitary saturates that penalty. A finite circuit with trusted generator bounds supplies one concrete continuity model.

These are conditional mathematical results, not measured calibration or a physical GU implementation. SC-META-53 remains UNCERTAIN; LT-SM8/LT-GR6b retain native interacting quotient/domain debts. Ledger0.263, source polarities and physical credit are unchanged. No novelty or external certification is claimed.

K2504 already owns sector positivity and fixed-map-class union bounds; K2430/K2506 own confidence sequences and convex-mixture transfer. Enlarging their carrier is reused reasoning. The new endpoint combines a precise controller contract, sharp coherent counterexamples, a constructive parameter-coverage proof and a priced uniform record guarantee. No assertion that calibration alone establishes the controller contract.

## 1. Full carrier, calibration and the coherent penalty

Let D=H tensor E be the complete retained data/memory carrier, with supported subspace S=H tensor E0, dim S=d=108k. Q,T are the original verifier projectors on H, extended by identity on E. Their positive/negative sector ranks on S are r=(10k,98k,12k,96k). Add a retained controller C=C^G. On C tensor D put Sbar=I_C tensor S and Rbar=I_C tensor R for R=Q,T. Every reused quantum memory, including C, is included; only a fresh fixed decoupled ancilla may be traced out.

For one fixed global CPTP map Xi, test basis-control states |g><g| tensor P_i/r_i for the four wrong-outcome sector settings and |g><g| tensor S/d for leakage. Define their probabilities p_gi and p_gL against Rbar and Sbar. Setting choice is private, and the same Xi is fixed before it. The preparations/readout are trusted on this full carrier; marginal preparations or a setting side channel do not suffice.

Let A=Sbar Xi*(Rbar) Sbar and P=Rbar restricted to Sbar. Then 0<=A<=I. Put D_R=A-P and B=P(I-A)P+(I-P)A(I-P). Direct expansion gives

    B-D_R^2=A-A^2 >=0.                                      (1)

Both diagonal sector blocks of B are positive. For any positive block matrix Z indexed by control g,

    ||Z|| <= sum_g ||Z_gg||.                                (2)

Proof: positivity gives |<x_g,Z_gh x_h>|<=sqrt(<x_g,Z_gg x_g><x_h,Z_hh x_h>); sum and use Cauchy-Schwarz to bound by (sum_g ||Z_gg||)sum_g||x_g||^2. Each positive diagonal block has norm at most its trace. Applying this to the two sectors and to positive leakage yields

    epsilon^2 := max_R ||A-P||^2 <= max_i sum_g r_i p_gi,
    ell := ||Sbar Xi*(I-Sbar) Sbar|| <= sum_g d p_gL.         (3)

If all r_i p_gi<=a^2 and d p_gL<=b, the guaranteed global bounds are epsilon<=min(1,sqrt(G)*a), ell<=min(1,G*b). These are bounds from sector data, not from a characterization of each reduced channel. The following construction makes both factors necessary.

## 2. Exact sharpness and the structural repair

Choose orthogonal original vectors A,B in sectors (Q,T)=(1,0),(0,1). Let u=G^(-1/2)sum_g |g> and P_u=|u><u|. For a rotation R_tau on span(A,B) with sin^2 angle=tau in(0,1], define

    V=P_u tensor R_tau + (I-P_u) tensor I.

This is a unitary on the full carrier, identity on the rest of H/E. Tracing control after a basis-control input produces the data channel (1-1/G)Id+(1/G)Ad_Rtau. In each of the four sector settings, r_i p_gi=tau/G; leakage is zero. Yet input u retains the full rotation and ||V* Rbar V-Rbar||=sqrt(tau). Thus the sqrt(G) factor multiplying the sector-derived allowance sqrt(tau/G) is sharp. The actual reduced-channel operator defect is sqrt(tau)/G, which is a different quantity and may not be substituted for that allowance.

For leakage, rotate only one full supported vector A tensor e0 into A tensor e1, with e0 in E0 and e1 perpendicular to E0, using the same conditional-control unitary; act identically on every other data/memory direction. The maximally mixed support test has p_gL=tau/(Gd), hence d p_gL=tau/G; coherent input u tensor A tensor e0 has leakage tau. This saturates the data-derived G factor. The out-of-support e1 remains in the complete E; silently discarding it would invalidate the test model.

A trusted nondemolition controller avoids this amplification. Suppose every Kraus operator is block diagonal in the same retained control basis,

    K_alpha=sum_g |g><g| tensor K_alpha,g,
    sum_alpha K_alpha,g* K_alpha,g=I.

For every data effect F, Xi*(I_C tensor F)=sum_g |g><g| tensor Phi_g*(F). Hence the full operator norm is exactly the maximum branch norm, even on coherent or reference-entangled inputs. A CPTP control-only channel before or after such a controlled map preserves that bound: before it, its unital adjoint contracts the deviation and fixes I_C tensor R; after it, it fixes the measured effects. It also fixes support Sbar. Compositions of multiple data maps are instead whole gaps and must be calibrated/bounded as such.

Arbitrary state-dependent selection is not covered by naming a branch. Even if every selectable Phi_g is identity, a preceding selection instrument that applies the A/B swap destroys Q with certainty on A. Its disturbance is part of the global gap map and needs calibration. Classical random weights chosen from the past, independent of the current quantum input conditional on that past, give an ordinary convex mixture and are safe. If hidden quantum state controls the selection, include and certify that controller explicitly; do not replace it by a marginal classical mixture.

## 3. One pooled experiment on the global carrier

For target center allowances a>0,b>0 define

    c_i=r_i/a^2 (i=1..4), c_L=d/b,
    W_G=G(2d/a^2+d/b), q_gi=c_i/W_G.

Each shot independently samples the label (g,i) with these probabilities after Xi has been fixed. The pooled wrong bit has mean mu=sum_gi q_gi p_gi. Equation (3) implies

    epsilon^2/a^2+ell/b <= sum_gi c_i p_gi = W_G mu.          (4)

This is K2504 on the larger support, with a basis-control implementation of its maximally mixed sector preparation. It does not require coherent input preparation. At fixed n, zero wrong bits yields mu<=1-beta^(1/n) with failure probability at most beta. K2506 supplies the anytime version, provided the map is fixed within this experiment (its adaptive variant certifies an average, not each deployment map). Known per-label bias is charged by eta_eff=sum q_gi eta_gi, so replace mu by U_n+eta_eff. Uniform bias bounds are supplied, not inferred from no observed failures.

One global map uses one confidence event, not G separate events. For N prespecified center maps, use beta=alpha/N, and union bound only over the N experiments. No conditional confidence on a selected passing transcript is asserted.

For the block-diagonal structural model, per-branch pools of weight W_0=2d/a^2+d/b and NG confidence events at alpha/(NG) give maximum rather than sum bounds. Global pooling and per-branch tests have different passing regions: a sum constraint can fail even when every branch meets its individual allowance. The smaller logarithm of global pooling is not a claim of uniformly better sample efficiency.

## 4. Constructive coverage of a continuous controller family

Let Theta=[0,1]^p in sup distance, p>=1. Before seeing data freeze a finite h-net {theta_j}, N<= (ceil(1/h)+1)^p, and a complete stationary global channel Xi_theta for every parameter. Assume trusted uniform effect bounds

    ||Sbar[Xi_theta*(Rbar)-Xi_theta'*(Rbar)]Sbar||
        <= L_R dist(theta,theta'), R=Q,T,
    ||Sbar[Xi_theta*(I-Sbar)-Xi_theta'*(I-Sbar)]Sbar||
        <= L_L dist(theta,theta').                         (5)

Take L_E=max(L_Q,L_T). On the simultaneous event that all centers have epsilon<=a,ell<=b, every theta has

    epsilon(theta)<=min(1,a+L_E h),
    ell(theta)<=min(1,b+L_L h).                            (6)

This is the triangle inequality and the net covering property. It is a pathwise operator result, uniform on supported states and references. Any history-dependent convex mixture of these global channels obeys the same bounds, with weights chosen even after calibration. No union over parameters, deployment times or histories is needed. The model promises that the history-conditioned maps, including hybrid histories, really belong to this family or its convex hull. An arbitrary changing device or unmodeled controller is not certified.

A sufficient circuit model makes (5) checkable separately from tests. On the full retained carrier and a fresh fixed decoupled ancilla, let

    V_theta=U_L(theta)...U_1(theta),
    U_l(theta)=exp(-i t_l H_l(theta)),
    ||H_l(theta)-H_l(theta')||<=h_l dist(theta,theta'),
    Lambda=sum_l |t_l|h_l.

The bounded Hermitian generator assumptions imply, by the integral Duhamel identity and unitarity, ||U_l(theta)-U_l(theta')||<=|t_l|h_l dist. Telescoping gives ||V_theta-V_theta'||<=Lambda dist. For every purified input the output half-trace distance is at most the vector distance, hence at most this operator norm. Tracing the fresh ancilla contracts it. By effect/trace-distance duality, each Heisenberg effect difference has operator norm at most Lambda dist. Thus L_E=L_L=Lambda suffices, including references and support compression. The factor is Lambda, not the looser 2Lambda obtained from two triangle terms. Unknown calibration/control drift must be added explicitly to (5); finite samples cannot establish trusted generator bounds or stationary behavior.

## 5. Priced complete-record consumer and mesh tradeoff

Fix desired deployment epsilon_D,ell_D>0. Choose h with a=epsilon_D-L_E h>0 and b=ell_D-L_L h>0. At each net point use W_G above and a known uniform eta_eff. With v=1/W_G-eta_eff>0, the prospective sufficient all-zero total count is

    N ceil(log(N/alpha)/[-log(1-v)]),                       (7)

for 0<v<1; the conservative N ceil(log(N/alpha)/v) also suffices. This is sufficient passing-data effort, not a prediction that all shots pass or a universal optimal cost. No shot count cures a nonpositive bias or transfer margin. For h<=min(epsilon_D,ell_D)/(2Lambda),

    W_G <= G(8d/epsilon_D^2+2d/ell_D).

N explicitly retains the parameter-dimension cost; no dimension-free guarantee is claimed.

In the zero-bias case, a useful analytic design balances the covering and precision penalties. Put L=max(L_E/epsilon_D,L_L/ell_D)>0 and h=t/L,0<t<1. With C=(L+2)^p the net bound gives N<=C t^(-p). For A=2d/epsilon_D^2,B=d/ell_D, the geometric weight upper envelope is

    N W_G <= C G f(t),
    f(t)=t^(-p)[A/(1-t)^2+B/(1-t)].                       (8)

Each summand is strictly log-convex; their sum is strictly log-convex and diverges at both endpoints. Its unique minimizer solves

    A[(p+2)t-p]+B(1-t)[(p+1)t-p]=0,                       (9)

and lies strictly between p/(p+2) and p/(p+1). At the first point the A term vanishes and the B term is negative; at the second the reverse is positive. This optimizes only the displayed conservative geometric-weight envelope, not (7)'s logarithm, integer net sizes or an apparatus cost. If L=0, one center suffices and this mesh optimization is unnecessary.

For m original verifier gaps with initial support, original Q/T instruments/flags and full history coverage, use K2500/K2506 with epsilon_j,ell_j from (6). In particular for m=2,

    E <= min(1,1024 epsilon_D+1024 sqrt(epsilon_D ell_D)+ell_D).

If epsilon_D=ell_D=10^-6 then E<=2049/10^6. Ideal acceptance s0>=1/2 and bad-and-accepted mass b0=0 imply actual conditional error <=2049/497951<1/200. The operator coverage theorem now supplies this consumer's history premise under the declared circuit/family model; it does not build that device. General m uses the inherited ordered leakage bound, never a cap-independent inference. Confidence failure alpha is separate from the within-event record/postselection error; report both, or use a union bound for a stated unconditional task.

## Controls, evidence and remaining uncertainty

The probe checks exact finite coherent rotations, block-diagonal effects, controller disturbance, leakage and PSD identities; rational sample/consumer budgets and mesh algebra are separate checks. The full theorems are the written arguments, independently reviewed internally. Finite examples do not certify all circuits or a real apparatus.

Strongest contrary constructions are the coherent rank-one controller, a data-disturbing selector even with identity branches, and a parameter family that agrees at every finite net point but has an uncontrolled interior swap when (5) is omitted. A piecewise family choosing identity at sampled points and swap elsewhere has identical calibration data and arbitrarily bad deployment; it demonstrates the necessity of continuity/model coverage, not impossibility of honest calibration. K2506's shared hidden-bit example remains the reason to include all retained memory.

A practical implementation still owes the full memory dimension/support, trusted joint preparation/readout, stationary circuit model and generator/drift bounds. These assumptions are now explicit, testable modeling inputs rather than an abstract average-to-deployment inference. Sharp total-sample optimality and a useful device-scale realization remain open. Native matter/light and the unrestricted stopping frontier are separate.

[Exact probe](../../tests/channel-swings/k2508_controller_coverage_probe.py), [saved report](../../lab/process/k2508-controller-coverage.json), [K2504 sector theorem](k2504-verifier-sector-calibration-2026-11-02.md), [K2506 transfer and record consumer](k2506-calibration-deployment-transfer-2026-11-02.md).

Positive block norm bounds are established matrix analysis; see [Bourin and Lee, Positive block matrices and numerical ranges](https://www.sciencedirect.com/science/article/pii/S1631073X1730256X). The general block bound used here is proved above; no novelty is claimed for pinching or Duhamel estimates.
