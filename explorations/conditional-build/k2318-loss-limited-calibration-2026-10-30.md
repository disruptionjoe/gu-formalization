---
title: "K2318 Loss limited calibration"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics only; no native physical acceptance
scripts:
  - tests/channel-swings/k2318_loss_limited_calibration_probe.py
---

# K2318 Loss limited calibration

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
result: K2318
carrier: fixed-total-N positive bosonic pilot/reference with arbitrary retained ancilla and independent retained working pump LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert inner product and normalized trace distance ON=declared_carrier
real_structure: complex quantum states with physical conjugation
grading: total excitation sectors and sensing-mode number n
action_owner: repository-construction -- single relative phase query followed by sensing-arm pure loss with protected reference
target: calibration necessity, achievable loss budget and code-confined sensing limitation MAP-TYPE=evaluation
```

## Task and the changed physical input

Keep [K2312](k2312-relational-finite-calibration-2026-10-30.md)'s retained working pump with mu=10^28, baseline error delta0<9.386e-12, a pilot/reference stock N, one sensing query exp(-2i phi n), arbitrary final joint pilot/reference readout, and inverse-phase feedforward. The working pump is independent of the pilot; it is not an extra sensor and cannot be arbitrarily replaced. The target is full retained-working-output trace error at most1e-11 with probability at least.95 uniformly in unknown phase modulo pi.

Add a **specified pure-loss channel** of transmissivity 0<eta<1 on the sensing arm; reference and arbitrary ancilla are protected. The loss environment is inaccessible. Classical number-loss flags may be recorded, but conditioning away failures does not satisfy this all-launch probability target. Loss before or after the single phase query gives the same reduced channel by phase covariance. Multiple queries, in-query recovery or coherent environment access define different tasks.

This removes K2315's passive-preparation restriction: arbitrary entangled fixed-shell inputs are allowed. The following limit therefore also applies to the supplied sine pilot. It is ordinary quantum apparatus mathematics, not a GU prediction, hardware exclusion or novelty claim; source/physics ledger mappings remain unchanged.

## Purification bound and confidence necessity

Purify an arbitrary input, retaining its ancilla. Conditional on sensing occupation n, loss label l is binomial with probability1-eta. Rephase the inaccessible environment in the mathematical purification, obtaining derivative generator, up to an irrelevant sign,

    G=2(n-l/(1-eta)),
    E[G|n]=0, E[G²|n]=4 eta n/(1-eta).              (1)

The environment phase is a proof freedom, not available laboratory control. Integrating the norm speed of this horizontal purification and using trace-distance contraction gives, for any two phases separated by d,

    D(rho_phi,rho_phi+d)
      <=min(1,2|d|sqrt(eta E[n]/(1-eta)))
      <=min(1,2|d|sqrt(eta N/(1-eta))).              (2)

This is a finite-displacement distinguishability bound; no locally unbiased estimator assumption enters. The factor2 comes from exp(-2i phi n).

K2315's actual coherent working-pump marginal and baseline sandwich prove that successful output implies phase error less than e0=1e-25. For two possible phases separated by3e0, those successful estimate sets are disjoint. A uniform.95 estimator would discriminate them with error<=.05, hence D>=.9 by the binary discrimination formula. Consequently

    (1-eta)/eta <=4N(3e0)²/.81.                    (3)

At N=3e27 this is4/(3e21), approximately1.3334e-21. This necessary condition is not a sufficient optimum threshold. It covers arbitrary protected ancillas and final joint measurement, with the stated single-query/no-postselection scope.

The method is an application of established purification bounds for noisy metrology; see [Escher, de Matos Filho and Davidovich (2011)](https://www.nature.com/articles/nphys1958). The particular confidence task and budgets are derived here; no novelty adjudication is made.

## Released constructive bound: exact loss-channel continuity

On the fixed total-N shell, including arbitrary retained ancillary systems,

    sup_rho D((Loss_eta tensor Id)(rho),rho)=1-eta^N. (4)

For pure input, write r=eta^(N/2), z=E[eta^(n/2)], y=E[eta^n]. Every nonzero loss lands in a total-number sector below N, orthogonal to the ideal state. The exact trace norm is

    D=[1-y+sqrt((1+y)²-4z²)]/2.

Put u=z-r>=0 and v=y-r². Since X=eta^(n/2) lies in[r,1], v<= (1+r)u. Therefore

    z²-r²(1+y-r²)=2ru+u²-r²v
       >=r[2-r(1+r)]u+u²>=0,

which proves D<=1-r². The Fock input |N,0> attains equality. Purification handles mixed states and ancillary systems; equivalently use convexity. The fixed total-number hypothesis supplies the orthogonal loss sectors and is essential to this proof.

By Bernoulli, 1-eta<=epsilon/N suffices for disturbance<=epsilon. Extend K2312's ideal finite Fourier instrument to all lower-number sectors with an explicit failure flag. On surviving outcomes it applies the same estimate and therefore prepares the same conditional working output, since the working pump is independent. Total variation of the outcome law is at most epsilon; the ideal good-event probability >=43/45 becomes >=43/45-epsilon. With epsilon=1/200 and

    1-eta <=1/(6e29),

success is still greater than.95 at N=3e27. The ideal good-event conditional working error remains below9.986e-12. This is a sufficient, deliberately conservative architecture; it leaves a large gap from the necessity bound(3).

For a distinct **averaged complete-output** requirement with the actual classical-record marginal, use the same conditional-output argument, not bare contraction to a target whose record law changed. For each surviving record j let c_j be the trace distance of its unchanged conditional working output to the target, so 0<=c_j<=1. Assign failure records their actual cost, at most1; their ideal probability is zero. Total variation at most epsilon changes the expected cost by at most epsilon. Thus(4) adds at most epsilon to the ideal<9.491e-12 bound even with the actual record marginal. Choosing epsilon=5e-13 and 1-eta<=1/(6e39) gives averaged error<9.991e-12. Do not confuse this stronger continuity budget with the confidence budget. Nonzero loss outcomes do not return the full charged stock N: exact replenishment requires a charged reservoir. Flagging failure preserves honest accounting but is not renewal.

## Error correction: precise obstruction and countercontrol

For a code projector P correcting the infinitesimal error set{I,a}, the Knill-Laflamme condition includes P a†a P=cP. Since the phase generator is2n=2a†a, its projected logical Hamiltonian is scalar. Thus ideal continuously confined/recovered-code sensing cannot retain a nontrivial first-order logical phase generator while exactly correcting this loss. This is the elementary form of the Hamiltonian-in-noise-span boundary; broader conditions are treated by [Zhou et al. (2018)](https://www.nature.com/articles/s41467-017-02510-3).

It does **not** say every raw encoded physical state loses phase information. In total shell N=4, let |0L>=(|0,4>+|4,0>)/sqrt2 and |1L>=|2,2>. Then PaP=0 and PnP=2P, but n|0L> has a component outside the code and nonzero variance. This exact countercontrol rules out broadening the projected-code statement into all finite-phase, adaptive or approximate-correction impossibility. Nor does a classical loss count restore the coherent lost environment.

## Verification and remaining discriminator

Exact finite binomial and Kraus controls check(1), complete loss sectors, continuity and code compression; rational bounds reuse the actual working-pump success-radius inequality. Changed encoding, loss variance, discarded loss outcomes and generator compression are tested through real evaluators. Universal channel, confidence and code statements use the written proofs; finite matrices do not certify all N. No hardware, external-expert, novelty, empirical or proof-assistant certification.

Next compare an explicit lossy selective-control/reference/reset architecture with the necessary and sufficient budgets, or a separately priced multi-query/accessible-environment model. The loss-free finite construction remains valid on its original assumptions. Loss now has a quantitative cost rather than an unspecified robustness promise.
