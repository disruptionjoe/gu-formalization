---
title: "K2445 A random-pair certificate for correlated program blocks"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: "mean unlabelled block marginal under hidden routing; no individual-site or joint-process certificate"
---

# K2445 A random-pair certificate for correlated program blocks

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
result: K2445
carrier: arbitrary joint state on m systems of common finite dimension N LAYER=toy CHIRALITY=N/A
pairing: Hilbert-Schmidt loss, collective variance and trace distance ON=declared_carrier
real_structure: complex Hermitian positive states with explicit classical flag blocks
grading: block membership, ordered pair and private test/use choice
action_owner: repository-construction -- supplied conditional mathematical model
target: finite-block noncancelling certificate without replica factorization MAP-TYPE=evaluation
```

## Result

[K2442](k2442-replicated-process-distance-2026-11-01.md) needs conditional independent replicas or a priced pair defect. A different protocol can instead emit and isolate an entire m-system block before sampling. The systems may be arbitrarily entangled and nonidentical. Uniform pair sampling and uniform unlabelled single-system use certify the mean marginal with an explicit finite-block floor,

    ||rho_bar-sigma||2^2 <= h+(N-1/N)/(m-1), m>=2.            (1)

Here sigma is the fixed target state, rho_bar is the average one-site marginal, Omega2 is the uniformly averaged ordered distinct-pair marginal, and

    h=Tr(H_sigma Omega2),
    H_sigma=Swap-sigma tensor I-I tensor sigma+Tr(sigma^2) I.

This replaces a tensor-factorization premise with trusted whole-block custody, random selection and storage. It does not certify each labelled member. The dimension-only correction is universally sharp when m is a multiple of N. Conditional mathematics only; SC-META-53 remains UNCERTAIN and source/ledger/canon unchanged. Squared-distance testing is established in [Fanizza, Salvia and Giovannetti](https://quantum-journal.org/papers/q-2023-09-11-1105/); the present proof states its own correlated-block premises and claims no novelty.

## 1. Collective variance proof

Choose a Hermitian Hilbert-Schmidt orthonormal basis F_a of N by N matrices. Completeness gives sum_a F_a tensor F_a=Swap and sum_a F_a^2=N I. For J_a=sum_i F_a^(i), positivity of every variance gives

    0<=sum_a Var(J_a)
      =m N+m(m-1)Tr(Swap Omega2)-m^2 Tr(rho_bar^2).

No exchangeability or permutation symmetry is assumed: ordered-pair averaging supplies precisely the cross terms. Rearranging gives the stronger form

    ||rho_bar-sigma||2^2
      <= h+(N-Tr(rho_bar^2))/(m-1).                          (2)

Since Tr(rho_bar^2)>=1/N, equation(1) follows. A known common support of dimension s for every block subsystem and sigma permits s in place of N. Individual ranks or target support alone do not. H_sigma has spectrum in[-2,2]: in an eigenbasis of sigma its diagonal eigenvalues are1-2lambda_i+c and its offdiagonal symmetric/antisymmetric eigenvalues are +/-1-lambda_i-lambda_j+c, c=sum lambda_i^2.

## 2. Sharp floor and contrary constructions

A tensor product of N-site totally antisymmetric singlets, with m divisible by N, has rho_bar=I/N. Every collective traceless generator annihilates it, so the variance sum is zero. Equation(2) and the dimension-only floor are equalities. For N=2,m=4, take singlet12 tensor singlet34 and pure target sigma. The uniform-pair swap mean is0, the observed mean score is0, but ||rho_bar-sigma||2^2=1/2. The floor(2-1/2)/3=1/2 is necessary; zero score alone is not a certificate.

The original instrument controls use sigma±tH from K2442, with H supported in the plus flag and equal numbers of both signs in a product block. Then rho_bar=sigma while each labelled member remains distance2|t| from sigma. Ordered-pair averaging gives h=-4t^2/(m-1), not the independent-replica value. This explicitly excludes a mean of labelled-member distances.

Selection must occur after the entire block has been emitted and isolated. The retained index must be erased/hidden from the consumer, or its controller must be chosen independently of that index. Otherwise a history/index-selected controller may undo the cancellation in rho_bar; fresh private initialization alone does not prevent that. A nonuniform selected pair cannot certify a uniform use marginal without a separately justified sampling correction. Never measure a pair and use its unmeasured siblings under this theorem: measurement can steer them. Entire blocks are assigned either test or use.

## 3. Hidden-route used-index certificate

Before block t, condition on the declared past history. Emit an arbitrary joint block, then secretly choose test T_t with probability pi, U_t=1-T_t. On a test select an ordered distinct pair uniformly and measure H_sigma, obtaining |X_t|<=2 and conditional mean h_t. On use retain a uniformly chosen subsystem and discard the rest, with the index unavailable to the controller. Its predictable reduced state is rho_bar,t.

Put a=(1-pi)/pi, b=max(2a,2), v=4pi a^2+4(1-pi), and

    Z_t=a T_t X_t-U_t h_t, E(Z_t|past)=0,
    |Z_t|<=b, E(Z_t^2|past)<=v.

The centering is h_t, not q_t=||rho_bar,t-sigma||2^2. The latter only satisfies q_t<=h_t+f, f=(N-1/N)/(m-1). With L_n=log(2n(n+1)/alpha), the same time-union Freedman bound as K2442 gives, simultaneously at every n with N_U>0,

    mean_used q_t <= Q_U
       =a sum_test X_t/N_U+f
        +[sqrt(2nv L_n)+2b L_n/3]/N_U.                       (3)

On the stated confidence event the right side is nonnegative. Operational reports may clip it into[0,2]; clipping a negative realization is a convention, not a new guarantee on a failed confidence event. Bounded readout bias eta adds n(1-pi)eta/N_U and changes b to b+(1-pi)eta when centering; the stated second-moment bound requires bounded actual scores. Known variable block sizes add the actual use-index mean of f_t.

Cauchy-Schwarz gives mean_used D(rho_bar,t,sigma)<=min(1,sqrt(N Q_U)/2). The ideal K2444 program consumer consequently has normalized mean success error at most C sqrt(N Q_U)/2, C=D_in^2/d_A1. An average trusted completed-operation allowance kappa adds kappa/q. This normalized consumer requires nonzero actual mean success s; lambda sqrt(N Q_U)/2+kappa<q guarantees it. Beyond that regime only a separately established s>0 permits normalization. The independent preparation/causal-identification costs of K2438 are not removed if one wants to identify the producing device rather than use its actual emitted programs.

History-selected controllers are allowed if chosen before the current block's hidden retained index and initialized independently of the block/device quantum memory. Arbitrary within-batch feedback is allowed. This remains a predictable used-block mean, not a final-transcript conditional state, future-device guarantee, every member's quality, or across-block joint process.

## 4. Released consequence: exploit genuinely classical flags

If the entire emitted joint block is invariant under local flag dephasing at every site, and the target has the same classical flag algebra, use the Hermitian basis of the matrix algebra A=direct_sum_z M_(k_z) instead of all N by N matrices. Completeness becomes a flag-compressed swap and sum_a F_a^2=direct_sum_z k_z I_z. The same variance argument yields

    q_t<=h_t+[sum_z k_z p_(t,z)-Tr(rho_bar,t^2)]/(m-1).

For the original r-slot flagged carrier each block has k_z=4^r and total dimension N=12^r. The safe floor is therefore

    f_flag=(4^r-1/12^r)/(m-1).                              (5)

Classical flag compression leaves the score expectation unchanged on these states and cannot increase its norm. The original instrument family thus earns a smaller certified floor without pretending replicas are independent. The unrestricted singlet example proves universal sharpness of(1); it does not prove sharpness of(5) on causal flagged programs. Diagonal one-site flag marginals alone do not suffice: the joint flag state (|01>+|10>)/sqrt(2) has diagonal one-site marginals but full swap expectation1 and compressed swap expectation0. If joint flag coherences might remain, use the unrestricted theorem or separately price that defect.

## 5. Costs and useful consequence

For one original flagged qubit program N=12, q=1/4, lambda=1/2 and C=2. The pure finite-size contribution to mean resource distance is at most(1/2)sqrt(143/(m-1)); the programmed-output contribution is at most sqrt(143/(m-1)). Even an ideal zero-score unlimited-statistics one-percent output allowance therefore needs m>=1,430,001 under this sufficient bound. With verified classical flags, equation(5) replaces143 by47 and the sufficient zero-statistical-floor block size drops to470,001. These are sufficient dimension-floor costs, not optimal protocol lower bounds.

The exact probe prices the simultaneous statistical and block floors for m=10^8,n=10^12, pi=1/2, N_U=n/2 and zero empirical score, with alpha=.05, using Arb256. These are prospective conditions. Total emitted programs are m*n, and even use blocks discard all but one. The protocol can avoid unproved replica independence, but this simple implementation is expensive. A smaller certified support, better measurement design, state-dependent purity lower bound or block structure may improve it; none is inferred from target rank alone.
[Exact probe](../../tests/channel-swings/k2445_correlated_block_certificate_probe.py), [report](../../lab/process/k2445-correlated-block-certificate.json). Written universal proofs and finite exact controls are distinct evidence. Independent internal review is not proof-assistant or external-expert certification.
