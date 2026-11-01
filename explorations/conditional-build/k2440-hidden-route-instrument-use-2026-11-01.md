---
title: "K2440 Hidden routing from instrument tests to heralded use"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: average predictable used program states only; heralded fixed independent inputs, no product-process or future-device guarantee
---

# K2440 Hidden routing from instrument tests to heralded use

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
result: K2440
carrier: original three classical flag blocks on a complex qubit reference and qubit output LAYER=toy CHIRALITY=N/A
pairing: normalized Choi trace norm and half diamond distance ON=declared_carrier
real_structure: complex positive Hermitian states and completely positive maps
grading: classical flag blocks and pre-emission conditional history
action_owner: repository-construction -- imported finite quantum operations
target: hidden randomized test/use transfer and heralded channel programming MAP-TYPE=evaluation
```

## Result

A concrete protocol can certify **use-round conditional averages** despite arbitrary drift: make the same emitted resource eligible for either route on each round, then secretly choose whether to test or use it. The test data bound the average of the pre-round conditional states at the actual used indices. Bell postselection turns those states into a heralded implementation of the target recorded instrument on a fixed independent input. For a qubit the ideal success probability is1/4; failures and a trusted Bell-measurement error are priced explicitly.

This is a changed operational architecture, not a claim that old calibration records establish future reliability. Ordinary signed averages still cannot certify mean distance, adaptive input sequences or the full correlated multi-use process. The theorem does not condition past states on the entire eventual transcript or promise behavior conditional on passing the test. It is a simultaneous-confidence statement about predictable conditional averages.

[Choi-state gate programming](https://arxiv.org/abs/1912.05418) and [Freedman's martingale inequality](https://tropp.caltech.edu/papers/Tro11-Freedmans-Inequality.pdf) are established tools; no novelty is claimed. SC-META-53 remains UNCERTAIN, ledger0.263/source/canon unchanged. No measured device, native GU instrument, physical quotient or source-action identification is supplied.

## 1. Experiment and exact quantifiers

Fix a target normalized flagged Choi state sigma for one finite-dimensional input channel; retain the original three flags. Before each round t, condition on the complete declared classical history H_(t-1). The device may carry arbitrary quantum memory and depend on all past data. Under the same preparation/emission protocol it produces a normalized flag-block resource rho_t on R,B, with inaccessible device memory traced out. rho_t denotes the conditional reduced state before seeing the current output or routing result.

Only **after** emission and isolation from the device, draw a fresh private coin T_t with P(test)=pi, 0<pi<1; U_t=1-T_t. It is independent of the pre-round history, resource and device. Test rounds read the same Pauli axes as K2439, independently chosen after emission. Use rounds apply a specified trusted Bell-program operation. Future device behavior may depend on earlier test/use results; nothing is iid. The current output, including its flag, is not used to choose the routing probability. Any leak, loss or extra flag must be modeled on the fixed complete carrier.

For fixed Pauli coefficient j put c_tj=Tr(O_j rho_t), with |c_tj|<=1. On a test round the importance-weighted readout W_tj obeys

    E(W_tj | H_(t-1),test)=c_tj,
    |W_tj|<=w_j,  E(W_tj^2 | H_(t-1),test)<=w_j,              (1)

where w_j=1,3,9 for zero, one, two nonidentity factors. Every identity/flag coefficient is retained. A trusted measurement bias |E W-c|<=eta_tj is handled below.

At any n define N_U=sum_t U_t. For N_U>0 the quantity certified is

    rho_U=(1/N_U)sum_(t<=n) U_t rho_t.                         (2)

This random matrix is positive and normalized along each trajectory. It averages the states conditioned on their own **earlier** histories. It is not a physical unmeasured reservoir conditioned on the full record, the state of a uniformly sampled stored register after measurements elsewhere, or the joint state of all used systems. Quantum steering makes those different objects.

## 2. Direct test-to-use martingale

Use test counts without dividing by the random number of tests:

    hat c_U,j=(1-pi)/(pi N_U) sum_t T_t W_tj,
    Z_tj=(1-pi)/pi T_t W_tj - U_t c_tj.                       (3)

Each increment has conditional mean zero. Because test/use are disjoint,

    |Z_tj|<=b_j=max((1-pi)w_j/pi,1),
    E(Z_tj^2 | H_(t-1))<=v_j=(1-pi)^2 w_j/pi+(1-pi).          (4)

Thus a scalar Freedman bound, unioned over M=48 coefficients and every n>=1, gives simultaneously with probability>=1-alpha:

    |hat c_U,j-Tr(O_j rho_U)| <= r_j(n),
    r_j(n)=[sqrt(2n v_j L_n)+2b_j L_n/3]/N_U,
    L_n=log(2 M n(n+1)/alpha).                                (5)

The union uses sum_n1/[n(n+1)]=1, so stopping can be chosen from the observed record. N_U=0 yields no certificate, never a division. Bounds are valid for every realized positive N_U; no separate binomial approximation is used. A confidence event for the whole run need not hold with the same probability after conditioning on a data-dependent pass event.

If (1) has bias eta_tj bounded by a pre-round trusted eta_j, use r_j+n(1-pi)eta_j/N_U. To see this, subtract the predictable mean (1-pi)bias_tj from Z. Freedman's increment constant then increases conservatively to b_j+(1-pi)eta_j; the variance bound v_j still bounds conditional variance of the raw increment, because the implemented sparse estimator still obeys E(W^2|past,test)<=w_j and |c_tj|<=1. Uniform settings, bounded readout signs and the original importance weights guarantee that second-moment bound even with biased signs; a general biased estimator must supply it separately. The report prices this correction. Alternatively a simultaneous realized bias bound on sum_t(1-pi)|bias_tj| may be used. Do not simply add eta once when estimating a randomly normalized used subset.

Set e_zab=|hat c_U,zab-c_target,zab|+the applicable radius. K2438's full complex Pauli inverse proves

    D(rho_U,sigma) <= epsilon=(1/2)sum_z ||e_z||_2.             (6)

No support, TP-marginal or ideal-Bell assumption on rho_U is needed for(6). All48 moments are read from the same nine-setting experiment. The 29/44 constrained reconstructions require their additional assumptions and are not substituted here.

### Executed allocation consequence

For a fixed total emission budget and typical N_U near n(1-pi), the leading variance factor in(5) is w/pi+1/(1-pi). It is minimized at pi=sqrt(w)/(1+sqrt(w)), because

    w/pi+1/(1-pi)-(sqrt(w)+1)^2
      = [sqrt(w)(1-pi)-pi]^2/[pi(1-pi)] >=0.

For the worst Pauli weight9 this gives pi=3/4 and leading factor16 instead of20 at pi=1/2. It also halves ideal successful uses per emission, from1/8 to1/16. This is a variance-versus-throughput choice, not a universal experimental optimum. The exact theorem still uses realized N_U and the linear confidence term; the typical-count substitution is only an allocation guide. Choose pi before the experiment. A post-hoc best allocation or adaptive policy needs its own valid weighting/coverage calculation.

## 3. Heralded programming of the actual used resources

Let input S have dimension d and rho on R,B, dim R=d. Prepare the **same fixed** input state xi_SE freshly on each use, with private reference E, conditionally independent of the resource and device memory. It may be entangled with E. Apply the Bell projection Phi_SR and keep B,E and original flags on success. Include a classical failure outcome to make the whole operation CPTP.

For the normalized Choi state J(Lambda)=(id_R tensor Lambda)(Phi_RA), direct basis contraction gives

    T_xi[J(Lambda)]=(Lambda tensor id_E)(xi)/d^2.              (7)

There is no input transpose in this convention: the two Bell contractions cancel it. For every TP flagged Lambda, success q=1/d^2 is input-independent **after summing all original flags**. An individual flag need not have an input-independent success probability. For arbitrary actual rho with an incorrect R marginal the success may depend on xi; this is why errors must be bounded before normalization.

Since T_xi is the same linear map for every used index, the average predictable subnormalized success output is T_xi(rho_U). Denote its trace by s. By completed-instrument contraction applied to(6),

    |s-q|<=epsilon,
    D(T_xi(rho_U)/s, (Lambda_target tensor id_E)(xi))
        <=epsilon/s <=epsilon/(q-epsilon),   epsilon<q.       (8)

Proof: write A=T_xi(rho_U), B=q Lambda_target(xi). The failure block has trace difference q-s. Contractivity gives ||A-B||_1+|s-q|<=2epsilon. Since
||A/s-B/q||_1 <= [||A-B||_1+|s-q|]/s,
(8) follows. It is the normalization of the mean subnormalized success output, correctly weighted by success probabilities, not the unweighted mean of normalized branches.

A uniform or selected-use-average trusted completed-operation half-diamond error kappa adds to epsilon in(8). This includes Bell projection, storage, private input preparation and readout imperfections when they fit that stated operation norm. Resource preparation error is already visible in rho_U; **no separate ideal-Bell preparation bound is needed for this actual program-output theorem**. Inferring the original device channel from rho_U is a different task and still requires K2432/K2438's joint resource/memory transfer. No free native identification follows from program behavior.

For a desired normalized error tau, it suffices that

    epsilon+kappa <= tau q/(1+tau).                           (9)

The rate is a real cost: at pi=1/2 and d=2, the ideal expected successful uses are one eighth of total emitted resources. No retries on an unknown consumed input are promised. The operation requires trusted entangled resources/measurement, storage, input isolation and a hidden classical choice; these are explicit added capabilities, not a free guarantee for ordinary direct device use. Expected success is not a pathwise count guarantee. Here s is an average conditional success probability, not the realized success fraction; (8) is neither the final-transcript conditional harvested state nor the mean of individually normalized outputs.

## 4. Counterexamples and finite consumer

- Reveal the routing before emission: a device outputs the target on tests and a different full-support instrument on use. All test estimates can look perfect while use is wrong. The zero-mean identity(3) fails.
- Test on Bell inputs but directly use unrelated data inputs under a distinguishable interface: the device may discriminate the preparations. Hidden late routing must apply to the same emitted program, not only to a secret classical label.
- The target mixed channel may be the average of two different channels at distance1/2. Choosing input/tester based on the branch reveals their errors even when the average channel matches. This also occurs at each original instrument: perturb one full-rank bad Choi block by plus/minus t Z tensor Y, with t=1/100000. Both instruments retain CP/TP and every flag effect, their complete mean equals the original target, but alternating input |0>,|1> gives the same nonzero output-error direction. No mean-distance or arbitrary adaptive-input guarantee follows.
- Accept every Bell result with Pauli correction after an arbitrary noncovariant channel: an amplitude-damping control fails. Only the named Bell outcome in(7) is accepted; other corrections need a separately proved covariance.
- Correlate data with the emitted program or device: knowing marginal rho_U is insufficient. The private input/reference independence condition is essential.
- Let success probabilities vary: normalize the averaged subchannels as in(8); an average of normalized outputs uses different weights and can differ substantially.

The report reconstructs the original two instruments and verifies(7) on a complete complex matrix-unit basis, checks a noncovariant channel and literal input-dependent failure, and exactly enumerates the randomized estimator's first two moments. A prospective n=4 billion, pi=1/2, N_U=2 billion example with empirical residual and readout error1e-6 and kappa1e-5 is evaluated by Arb256. The resulting normalized average output allowance is below0.015017, with average conditional success at least0.246301. It supplies a conditional allowance, not actual counts, a sample-size optimum, hardware cost or a future guarantee. Its extra heralding cost and success-normalization amplification are displayed.

## Verification and next condition

[Probe](../../tests/channel-swings/k2440_hidden_route_instrument_use_probe.py) and [report](../../lab/process/k2440-hidden-route-instrument-use.json) distinguish exact finite contractions/controls from rigorous prospective arithmetic and the universal written martingale proof. Independent specialist review checks causal information, ensemble conditioning and success weighting. Internal review is not external-expert or proof-assistant certification.

```sh
python tests/channel-swings/k2440_hidden_route_instrument_use_probe.py --check
```

Actual application needs the declared secret-late-routing hardware and trusted Bell-operation/readout bounds, together with a real complete record. General adaptive useful computation or a joint multi-use guarantee needs a full temporal tester or a stronger noncancellation certificate; it is not supplied by this retrospective conditional-average theorem. The formal hook analytic inverse remains a separate open mathematical route.
