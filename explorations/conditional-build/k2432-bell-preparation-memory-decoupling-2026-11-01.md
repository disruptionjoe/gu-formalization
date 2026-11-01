---
title: "K2432 Sharp joint-preparation decoupling with returning memory"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional quantum-information mathematics; no measured calibration or native GU recovery
scripts:
  - tests/channel-swings/k2432_bell_preparation_memory_decoupling_probe.py
---

# K2432 Sharp joint-preparation decoupling with returning memory

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
result: K2432
carrier: finite-dimensional joint input/reference and arbitrary finite device memory LAYER=toy CHIRALITY=N/A
pairing: half trace norm on states and half diamond norm on channels ON=declared_carrier
real_structure: full complex positive Hilbert density matrices
grading: input/reference, returning device memory, and chronological use
action_owner: repository-construction -- supplied quantum channel model
target: calibrated tested conditional channels and explicitly uniform deployment processes MAP-TYPE=evaluation
```

## Result

[K2430](k2430-adaptive-decoder-certification-2026-11-01.md) requires an input/reference pair independent of device memory given the past. A trusted bound on **joint Bell infidelity** now supplies a quantitative replacement for that exact premise, even when preparation and device memory are initially correlated. The bound preserves the actual device-memory marginal; replacing it by an arbitrary convenient state would define a different channel.

The sharp bound is

    d(rho_AM, phi_A tensor rho_M) <= f(q),
    q = 1 - <phi|rho_A|phi>,
    f(q) = (q + sqrt(4q - 3q^2))/2,     0 <= q <= 1.       (1)

Here A denotes the complete input/reference pair, phi is a rank-one projector, and d is half trace norm. It is squared-fidelity infidelity; the root-fidelity convention is different. For a freely chosen memory state sigma_M the sharp universal bound is sqrt(q). The two bounds must not be interchanged.

This is conditional quantum information, not a GU probability construction. SC-META-53 remains UNCERTAIN; no source polarity, physics ledger 0.263, empirical result or canon changes. No novelty or external certification is asserted. Pure-state fidelity and the usual gentle-measurement bound are established tools; see [IBM's fidelity and gentle-measurement derivation](https://quantum.cloud.ibm.com/learning/en/courses/general-formulation-of-quantum-information/purifications-and-fidelity/fidelity). The actual-marginal bound below is proved directly.

## 1. Proof with the actual memory marginal

Purify rho_AM to a vector on AME and include E in the memory for this proof. For 0<q<1 write

    |Psi> = sqrt(1-q)|phi>|u> + sqrt(q)|v>,
    (<phi| tensor I)|v> = 0,  ||u||=||v||=1.

The purified memory marginal R obeys R >= (1-q)|u><u|. Define

    Delta = |Psi><Psi| - phi tensor R.

A rank-one positive update of a negative semidefinite matrix has at most one positive eigenvalue. Delta has trace zero, so its half trace norm is that positive eigenvalue lambda (or zero). Its rank-one secular equation is

    1 = <Psi|(lambda + phi tensor R)^(-1)|Psi>
      = q/lambda + (1-q)<u|(lambda+R)^(-1)|u>
      <= q/lambda + (1-q)/(lambda+1-q).

The last step is inverse monotonicity for positive definite matrices. Multiplication by positive denominators gives

    lambda^2 - q lambda - q(1-q) <= 0,

hence lambda<=f(q). Partial trace of E proves (1) for the original mixed state and its actual memory marginal. At q=0 a pure marginal forces a product; at q=1 the trivial distance bound one is attained. The function f is increasing and concave: f''(q)=-2/(4q-3q^2)^(3/2) for 0<q<1, and f' decreases to zero at one.

### Sharpness and the distinct free-memory bound

Take orthonormal phi, phi_perp and memory vectors 0,1:

    |Psi_q> = sqrt(1-q)|phi>|0> + sqrt(q)|phi_perp>|1>.

Relative to phi tensor diag(1-q,q), the nonzero spectrum is

    (q +/- sqrt(4q-3q^2))/2,  -q.

Thus (1) is sharp for every q. For q=9/25 the distance is (9+3sqrt(73))/50, strictly larger than sqrt(q)=3/5 and q.

If memory may instead be selected freely, the normalized phi projection is phi tensor |u><u|, and purification gives distance at most sqrt(q). The fixture also proves sharpness of this free-memory guarantee: a correlated phase twirl preserving Psi_q removes off-diagonal entries of a candidate sigma. For sigma=diag(x,1-x), its distance is the unique positive eigenvalue

    lambda(x) = (1-x + sqrt((1-x)^2+4qx))/2.

It decreases with x on [0,1], and its minimum at x=1 is sqrt(q). Neither this minimizer nor postselection replaces the physical memory in (1).

## 2. Adaptive decoder certification with imperfect correlated preparation

At a predictably selected trial t, let rho_ARM,t be the actual state conditioned on the recorded past, and let V_t be the actual CPTP device operation on input and memory (reference R is untouched). Define the counterfactual reduced channel

    C_t(X) = Tr_M V_t(X tensor rho_M,t),

using the actual conditional memory marginal. If trusted conditional joint Bell infidelity is at most epsilon_t and readout-effect operator error at most eta_t, contractivity of trace distance gives

    |p_observed,t - p_ideal,t| <= f(epsilon_t)+eta_t.    (2)

No separate exact preparation-memory independence premise is needed. Run K2430's stopping-safe test on the actual observed Bernoulli probabilities. On its confidence event, if u_n bounds their average, then the mean ideal support leakage is at most

    b_n = min(1, u_n + (1/n) sum_t [f(epsilon_t)+eta_t]).

The same full complex-channel constants apply to both the average C_t and the average of their distances: C_bad=2(1+sqrt(2)/mu), mu^2>0.0522306, and C_good=2, giving min(1,C sqrt(b_n)). Concavity permits the coarser replacement mean f(epsilon_t)<=f(mean epsilon_t). If the calibration bounds hold only on a simultaneous event of probability 1-beta, total coverage is at least 1-alpha-beta. No independence of those events is required.

The theorem does not infer conditional fidelity from an unconditional preparation average. A rare, predictably identified bad-history event can have error one even if its unconditional frequency is tiny. Neither calibration of the input marginal nor successful postselected preparations certify the joint retained ensemble. All test outcomes and failed preparations must be handled by the declared experiment.

## 3. Executed consumer: the price of the missing preparation premise

For a desired distance tau, a zero-failure branch with budget n and readout allowance eta leaves the preparation-probability allowance

    y = (tau/C)^2 - log(1/alpha)/n - eta.

If y<0, this sufficient certificate cannot pass even with perfect preparation. At y=0 only perfect preparation permits the non-strict distance target. For 0<y<1, a uniform joint infidelity epsilon is sufficient exactly when

    epsilon <= g(y),
    g(y) = (1+y-sqrt(1+2y-3y^2))/2
         = 2y^2/(1+y+sqrt(1+2y-3y^2)).                (3)

The stable second expression avoids cancellation. It is the inverse of f, not a new statistical approximation. As n tends to infinity and eta=0, this certificate requires epsilon of order tau^4/C^4. This is the scaling of this sufficient chain, not a lower bound for every calibration protocol.

The report rigorously encloses g(y) for the existing prospective 0.01-distance budgets: 9,000,000 tests per bad sign and 170,000 good tests, alpha=1/60 per branch. It also tests a larger 20,000,000 bad-branch budget to separate the statistical margin from the preparation floor. With zero readout error, the sufficient infidelity thresholds are approximately 8.37e-16 (bad, 9 million), 8.38e-13 (good, 170,000), and 7.79e-14 (bad, 20 million). The probe uses conservative values below those enclosures. These are proposed experiment requirements, not supplied fidelity, counts or costs. More trials do not remove a systematic floor.

## 4. Executed follow-through: exactly what would compose across uses

For every allowed adaptive tester and every reachable deployment cut, let E include the current input/reference, prior outputs, future inputs and tester memory; M includes all device memory that can return. Suppose, uniformly over those cuts,

    d(rho_EM,t, rho_E,t tensor rho_M,t) <= delta_t,
    d_diamond(C_t,C0,t) <= kappa_t.

Here delta_t and kappa_t are deterministic uniform allowances (or worst-case bounds over the declared histories). The maps C0,t define one reference process independently of the unknown actual state. Then the final accessible distinguishing distance is at most

    min(1, sum_t(delta_t+kappa_t)).                    (4)

Proof: replacing the correlated input by its product of actual marginals changes the next accessible state by at most delta_t. Replacing its reduced channel by C0,t costs at most kappa_t including arbitrary reference E. Tester links are CPTP and contractive; induction telescopes. Uniformity makes this a process guarantee over the declared tester class. A single realized test history does not supply it.

A sufficient physical reset condition is a reset channel within complete distance zeta_t of a fixed memory replacement. Its output is zeta_t-close to rho_E tensor sigma_M, while its actual memory marginal is zeta_t-close to sigma_M; therefore delta_t<=min(1,2zeta_t). Exact reset gives zero. Alternatively, a uniformly nearly pure full returning-memory marginal gives delta_t<=min(1,f(epsilon_memory,t)+sqrt(epsilon_memory,t)): (1) first compares to the fixed pure-memory reference, then the pure-state fidelity bound replaces that reference by the actual marginal. The additional term cannot be dropped. A two-qubit pure Schmidt state with memory infidelity q has distance q(1-q)+sqrt(q(1-q)) from the product of its actual marginals; at q=1/25 this exceeds f(q). Hidden memory outside that certified subsystem invalidates the premise.

K2430 can supply kappa_t only with an additional justified uniform deployment transfer bound, for example kappa_test+gamma_t for the actual deployment marginals. Calibration of fresh Bell tests alone leaves this missing. A shared fair X-error bit and independent fair X-error bits give identical one-use channels but two-use outputs at trace distance 1/2; the probe constructs both exact states. Thus the new preparation theorem does not erase the memory-process distinction.

## Verification and next question

The [probe](../../tests/channel-swings/k2432_bell_preparation_memory_decoupling_probe.py) verifies exact spectra and sharp controls, derivative/inverse identities, rational CPTP fixtures, reset and two-use examples, and Arb preparation-budget bounds. Universal assertions rest on the proofs above, not finite sample agreement. Its [report](../../lab/process/k2432-bell-preparation-memory-decoupling.json) separates algebraic checks, rigorous numerical enclosures and contrary controls.

The physical next step is trusted joint preparation/readout evidence with a declared conditional sampling design, or a uniformly justified reset and deployment-transfer bound. None is supplied here. Further nominal objective decimals or an unconditional channel average cannot replace these inputs.
