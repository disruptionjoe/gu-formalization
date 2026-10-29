---
title: "K2259 Microscopic donor renewal and finite waste capacity"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied model theorem only; no source physicalization or canonical verdict
scripts:
  - tests/channel-swings/k2259_microscopic_donor_renewal_probe.py
---

# K2259 Microscopic donor renewal and finite waste capacity

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2259 Microscopic donor renewal and finite waste capacity
carrier: one reused donor qubit, finite fresh thermal collision cells, isolated service outputs and arbitrary tester memory LAYER=toy CHIRALITY=N/A
pairing: positive tensor-product Hilbert structure and quantum trace norm ON=declared_carrier
real_structure: complex conjugation and Hilbert adjoint
grading: nonnegative occupation-number labels, not observed physical chirality
action_owner: repository-construction -- supplied conserving finite apparatus
target: complete adaptive renewal bound, entropy ledger and approximate finite apparatus capacity MAP-TYPE=intertwiner
```


## 1. What is renewed, and what is consumed

[K2256](k2256-causal-fresh-resource-reset-2026-10-29.md) constructs isolated causal reset using a fresh donor per call. Here ONE donor B is reused. Between service contacts it collides with L fresh cells in tau_p=diag(1-p,p),0<p<1. Each spent collision cell is isolated permanently; old outputs are also isolated. Initially B itself is tau_p, independent of the tester T and all future stock. The ideal joint preparation is sigma_T tensor tau_B tensor tau_p^tensor N for N fresh cells; delta is half trace distance of the actual complete preparation from that product. At later renewal blocks B may be arbitrarily correlated with history, while the unused ideal cells remain independent. This complete preparation error is charged once. Timed contacts/routing are explicitly supplied. This is a finite microscopic channel construction, not an infinite bath, autonomous controller, fixed-port transport implementation or resource-free reservoir renewal.

Use the positive, number-conserving two-spin generator G=I-F, F=FSWAP. A collision has U_alpha=exp(-i alpha G). In basis00,01,10,11 it has phases1,e^(-2i alpha) on the even basis states and odd block

    exp(-i alpha) [[cos alpha, i sin alpha],[i sin alpha,cos alpha]].

Direct matrix-unit reduction against a fresh tau_p gives

    q_out=p+cos²(alpha)(q_in-p),
    rho01,out=exp(i alpha) cos(alpha) rho01,in.       (1)

Repeated fresh collisions compose exactly. For possibly different actual pulse areas alpha_l, set a=exp(i sum alpha_l) product cos alpha_l and r=|a|. The L-cell channel has population contraction r² and coherence multiplier a. A common positive onsite drift omega(n_B+n_cell) commutes with G and changes only a known number phase.

For arbitrary donor/history state rho_BF, its reduced renewal channel obeys

    D[(N_L tensor id)(rho_BF),tau_p tensor rho_F]
      <=d_p(r):=r/2+max(p,1-p)r².                   (2)

To prove it, write rho_BF as a positive2-by2 operator block matrix. Its offdiagonal block has trace norm at most1/2. The diagonal difference is r² times diag(-X,X), X=(1-p)rho11-p rho00, whose trace norm is at most max(p,1-p). Half trace norm and triangle inequality give(2). This bound erases correlations with F as well as renewing B's marginal. Fresh future cells and permanently isolated waste are essential to this composition.

The repeated-interaction method is established background; see [Attal and Pautrat](https://arxiv.org/abs/math-ph/0311002). The present calculation is finite and needs no continuous or Markov limit.

## 2. Complete adaptive consumer and finite controls

Perform K service contacts, each nominal full FSWAP, with K-1 renewal blocks. K2256's exact service on a fresh donor is replacement for arbitrary reference. Hybrid each renewal against replacement of B by tau_p while retaining every accessible tester memory; the same causal tester can act between slots. Contractivity gives complete history error

    epsilon<=min(1, delta+(K-1)d_p(r)
         +sum_k d_p(|sin Delta_k|)+sum_j eta_j).      (3)

Here delta is the initial JOINT stock/tester deviation, Delta_k the service pulse area error, eta_j integrated arbitrary full operator perturbation per contact. For unequal renewal blocks replace (K-1)d by their sum. Renewal area inaccuracies enter the actual product r directly. Perturbations use Duhamel at the dilation level. No normalized rare-history error is claimed.

Take p=1/5, K=1000, L=20 and alpha=pi/3 for every renewal collision. Then r=2^-20, d=2^-21+(4/5)2^-40, and999d<0.000477. With delta<=10^-4, zero service area error and total perturbation<=10^-4, error is below0.000677. The cost is19980 fresh renewal cells plus one reused donor,1000 input/output qubits, and20980 sequential contacts. With g(t)=(2alpha/pi)sin²t on0<=t<=pi, each positive pulse has area alpha, peak added norm4alpha/pi and peak derivative norm4alpha/pi. Renewal peaks are4/3, service peaks2; total contact time20980pi. Nominal stock energy is(19981/5)omega and entropy19981 h(1/5); preparation delta permits stock-energy deviation at most19981omega delta. No exact actual entropy is inferred from that error alone.

This consumer is deliberately nonoptimal: a full swap renews exactly with one fresh cell, reproducing the original stock replacement. Twenty partial collisions demonstrate a finite weak-contact mechanism and quantitative correlation removal, not a better resource economy.

## 3. Exact waste and conditional entropy ledger

Let E be one L-cell renewal block initially tau_p^tensor L independent of arbitrary BF. Number conservation gives

    Q_E=omega(1-r²)(q_in-p).

For beta omega=log((1-p)/p), entropy conservation and the Gibbs relative-entropy identity (natural logarithms, entropies in nats) yield

    beta Q_E=S(B|F)_in-S(B|F)_out
                +I(BF:E)_out+D(rho_E,out || tau_p^tensor L).  (4)

The reference/history F is untouched. Indeed Delta S_E=-Delta S_BF+I(BF:E)_out, and beta Q_E=Delta S_E+D. This retains quantum correlations and the actual displaced bath state. For a nonthermal/correlated initial block subtract I(BF:E)_in and D(rho_E,in||tau^L) on the right. Signed heat need not be positive for every donor state. Renewal of B does not restore E or erase information from the closed apparatus.

A concrete changed-resource control makes this visible. At p=1/5, B initially excited and alpha=pi/3, one fresh collision leaves q=2/5, two FRESH collisions leave q=1/4. Reusing the SAME cell for both contacts gives U_alpha²=U_(2alpha) and q=2/5, a discrepancy3/20. At a full swap, repeating the same cell twice returns the original state rather than renewing it. Correct cell marginals also do not imply freshness: stock correlated as(4/5)|00><00|+(1/5)|11><11| exports output correlations even under exact swaps, with two-output distance8/25 from independent thermal replacements.

## 4. Approximate reset still needs a large closed apparatus

K2256's exact Kraus-rank argument has an approximate counterpart. Consider any closed unitary K-input/K-output implementation whose total inaccessible apparatus has dimension d and initial rank r_A<=d, independent of the tester; count all donor, discarded and controller memories. Supply K Bell halves as inputs, with the other halves retained. The actual normalized Choi output has rank at most d r_A. The target is

    Omega=(I_2/2)^tensor K tensor tau_p^tensor K,
    eigenvalue lambda_j=2^-K p^j(1-p)^(K-j),
    multiplicity m_j=2^K binom(K,j).                 (5)

A support projector for the actual state has target mass at most the sum of its d r_A largest eigenvalues. Half trace error at most epsilon therefore requires that mass to be at least1-epsilon. Equivalently d r_A>=R_epsilon, where R_epsilon is the smallest count of largest eigenvalues holding mass1-epsilon. This integer is computed by descending binomial levels (reverse j if p>1/2), including a partial final level. In particular

    d r_A >=(1-epsilon)(2/max(p,1-p))^K,
    d>=sqrt(R_epsilon).                              (6)

At p=1/2, d>=2^K sqrt(1-epsilon). An apparatus of b<K qubits forces epsilon>=3/4, regardless of its internal correlations or reuse schedule. At epsilon=0 and0<p<1, R0=4^K, recovering the exact bound. If initial independence holds only within joint error delta, contractivity replaces epsilon by epsilon+delta in the necessary bound. This is a restricted closed-dilation dimension constraint, not an optimal heat/time cost or a bound for an apparatus with uncounted sinks.

### Finite threshold and asymptotic entropy-rate followthrough

For K=10,p=1/5,epsilon=1/100, exact descending spectral mass gives R_epsilon=617857. The final partially used level is j=5; its included mass is0.9900000256, while617856 eigenvalues hold only0.9899999232. Therefore d r_A>=617857 and integer d>=787 (at least10 qubits for a qubit apparatus). This strengthens the largest-eigenvalue estimate without pretending it constructs an optimal apparatus.

For fixed0<p<1 and one fixed epsilon<1, the exact spectrum also gives a sharp information-rate NECESSITY. Sampling a spectral index with its eigenvalue as probability, J has Binomial(K,p) distribution and

    I_K=-log2 lambda=K[1+h2(p)]
            +(J-Kp)log2((1-p)/p),
    Var(I_K)=K v, v=p(1-p)[log2((1-p)/p)]².

For any a>0, Chebyshev bounds the mass of eigenvalues larger than2^(-K[1+h2(p)-a]) by v/(K a²). Any R indices therefore hold mass at most v/(K a²)+R 2^(-K[1+h2(p)-a]). It follows that

    R_epsilon >= [1-epsilon-v/(K a²)]_+
                         2^(K[1+h2(p)-a]).

Take fixed a, then K large enough that the bracket is positive, then let a decrease to zero. Thus liminf log2(d_K r_A,K)/K>=1+h2(p), and

    liminf log2(d_K)/K >= [1+h2(p)]/2.               (7)

The same holds for error ceilings uniformly bounded below1. At p=1/2 the spectrum is uniform and v=0, so the exact finite formula already applies. At p=1/5 the lower rate is(log2 5-3/5)/2 qubits per call. This is a necessary closed-apparatus rate, not an achievable or thermal optimum; the explicit partial-collision construction uses substantially more stock.

Thus the finite microscopic construction really renews the donor and removes its history correlations, but moves the consumed resource into fresh collision stock and isolated waste. A permanently finite apparatus cannot claim arbitrarily accurate indefinite replacement by recycling labels. The remaining physical problem is supplying or recovering that stock with a declared entropy-export interface and routing/clock model.


## Reproduction and scientific ceiling

Run `python tests/channel-swings/k2259_microscopic_donor_renewal_probe.py`; `--write` refreshes the report. Exact finite controls and genuine changed-input faults supplement the written proofs; sampling does not prove the universal assertions. Independent internal specialists reviewed the actual arguments and probes, including cross-review of the separate results. No Lean, external-expert, novelty or remote-CI certification is claimed.

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 remains UNCERTAIN on the southeast rival; SC-META-53 remains UNCERTAIN on physical positivity. These supplied models do not resolve those source claims. LT-SM8/LT-GR6b/AC-F1 and ledger0.263 remain unchanged because action ownership, physical quotient and observed-domain bridges remain absent. Preserve full16cells/full20/K-C, native2+1/nonchiral, mirrors/fullII/normaljets, scalar/thermal and cosmology ceilings.
