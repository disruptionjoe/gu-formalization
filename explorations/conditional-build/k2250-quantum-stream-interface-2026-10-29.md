---
title: "K2250 Quantum stream reset needs an explicit extraction algebra"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied conditional apparatus mathematics; no source selection or physical recovery
scripts:
  - tests/channel-swings/k2250_quantum_stream_interface_probe.py
---

# K2250 Quantum stream reset needs an explicit extraction algebra

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2250 Quantum stream reset needs an explicit extraction algebra
carrier: finite XY spin chains and separately declared fermionic register circuits with retained reference LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert inner product ON=declared_carrier
real_structure: complex conjugation and Hilbert adjoint
grading: excitation number and explicit tensor or CAR ordering; not physical families
action_owner: repository-construction -- supplied operational models
target: joint output reset, coherent spin counterexample and finite reservoir resources MAP-TYPE=intertwiner
```

## Question and scope

[K2249](k2249-finite-density-chain-reset-2026-10-29.md) proves individual output reset for arbitrary-length independent DIAGONAL streams. It does not assert a full quantum process theorem. Here a coherent spin counterexample prevents the naive extension. A different, explicitly supplied fermionic register apparatus admits a joint-output, arbitrary-reference finite-horizon theorem. The distinction is operational, not notation.

Layer0: a physical spin tensor replacement is not a fermionic mode permutation. Output marginals, joint output channel, and adaptive process are different targets. Both models are GU-independent positive-Hilbert apparatus constructions. SC-META-53 remains UNCERTAIN; LT-SM8/LT-GR6b and ledger0.263 do not change. No native action/domain, physical quotient, autonomously timed extraction, efficient hardware or perpetual finite reservoir is supplied.

## 1. Exact coherent-spin counterexample

Use two spins S,B and the number-preserving XY unitary in order00,01,10,11,

    U = diag(1, [[c,-i s],[-i s,c]], 1), c²+s²=1.

Take bath tau_p=diag(1-p,p), c=3/5, s=4/5 and p=1/5. Insert |+> on S, evolve, discard S, then insert an independent |+> on S and apply the SAME U. Direct partial trace after round1 gives bath occupation

    q_B=c²p+s²/2,
    <sigma^-_B>=-i s(1-2p)/2.

The second output occupation is

    q_out=c²/2+s²(c²p+s²/2)-c s²(1-2p)/2
         =1973/6250.

Extending the diagonal covariance recurrence to these coherent inputs would omit the last term and predict2693/6250. The discrepancy is -72/625. No approximation or bath-refresh assumption is involved. The double-excitation phase of the actual spin unitary is included. The invariant onsite energy phase can be taken to be one in this fixture; it does not affect the distinction.

This does not refute K2249's stated theorem. The trace over an endpoint with coherent reinjection alters Jordan-Wigner strings. Ordinary SWAP and FSWAP obey

    FSWAP|i,j>=(-1)^(ij)|j,i>, SWAP=FSWAP CZ.

Nonadjacent mode permutations also carry intervening parity strings. The covariance recurrence cannot be extended across an ordinary spin replacement by simply reusing single-particle linearity.

## 2. A fully declared fermionic input/output apparatus

Now specify a different model. A reservoir has M-1 modes and each is initially tau_p, independent of K jointly prepared input modes and arbitrary reference F. The first input occupies site0 of an M-site path. Each step evolves the path for tau under h_M=omega I+J adjacency, J>0, omega>=2J. Extract the old endpoint into its retained output register and insert the next input using the second quantization Gamma of the one-particle permutation. This is an FSWAP circuit on a fixed global ordered Fock space; all parity strings are part of the supplied apparatus. At the end, apply the declared fermionic permutation placing all retained output modes first and then take the ordinary partial trace over the other modes.

This finite circuit is a passive number-preserving unitary on K+M-1 modes. Its K-by-K input-to-output one-particle block D is lower triangular:

    D_kj=f_(k-j+1), j<=k; D_kj=0, j>k,
    f_n=<0|U(QU)^(n-1)|0>, U=exp(-i tau h_M), Q=I-|0><0|.

The formula follows by propagating each inserted basis mode: a retained endpoint is removed after each step, so propagation between outputs contains Q. This is not the spin circuit of section1. Input entanglement across rounds and with F is allowed, but all inputs are prepared jointly before execution; adaptive interventions are not included.

## 3. Joint-output theorem from the actual scattering block

For any such passive circuit, with at least K reservoir modes and D a contraction, let sigma_i be D's singular values. The half-diamond distance of its K-output channel from replacement by tau_p^tensor K is bounded by

    epsilon <= min(1, sum_i arcsin(sigma_i))
            <= min(1, (pi/2)||D||_*)
            <= min(1, (pi/2)sqrt(K)||D||_F).       (1)

Here the reference is arbitrary and the trace distance is on ALL K outputs and that reference. The bound is independent of p, including pure-vacuum and maximally mixed endpoints.

Proof. The finite cosine-sine decomposition of the one-particle unitary, with input/bath columns and output/environment rows, produces passive basis rotations and K paired rotations. Each paired rotation has retained-input amplitude sigma_i=cos theta_i,0<=theta_i<=pi/2. Bath basis rotations preserve tau_p^tensor because it is a function of total number. The output basis rotations also preserve the target product tau_p. Replace every paired angle by pi/2, leaving all other basis rotations fixed. This fully transfers K bath modes to the outputs. Its reduced output is exactly tau_p^tensor K independent of input/reference. Fermionic permutation phases do not change this: expand the thermal bath in occupation eigenstates; the remaining input is traced out, and the thermal output is diagonal. Input/reference coherences do not survive a trace over the complete transferred input subsystem.

Second quantization of each paired rotation is generated by a two-mode hopping generator whose norm on its full four-dimensional Fock factor is1. Its difference from the full-transfer unitary has operator norm at most pi/2-theta_i=arcsin sigma_i. A product telescoping bound gives the sum in(1), irrespective of pair tensor conventions. Purify the thermal bath; the resulting isometry difference bounds half trace distance after any partial trace, for arbitrary input/reference. This avoids an unjustified tensor-product generalized-amplitude-damping factorization. Finally arcsin x<=pi x/2 and the nuclear/Frobenius inequality give(1).

## 4. Reusing the half-line renewal estimate

For the half-line, K2249 proves sum_n|f_n|²<8/(Jtau)² by its exact renewal resolvent and Parseval argument. Therefore for every finite K,

    ||D||_F²=sum_(n=1)^K (K-n+1)|f_n|²
             <8K/(Jtau)²,
    epsilon <= min(1, pi sqrt(2) K/(Jtau)),         (2)

with the trivial1 ceiling understood when the expression exceeds1. This is joint-output control, which costs a growing spacing tau as K grows. It is not an all-length uniform joint reset theorem. The half-line thermal state is algebraic, not a trace-class vacuum-Fock density. For the finite-resource conclusion below, D from the half-line is only a comparison matrix of coefficients. No global thermal density or complete-channel thermodynamic-limit theorem is needed.

For a finite chain, K2249's first K coefficients satisfy

    ||(f_M-f)_(1:K)||_2<=4 sqrt(K) b_M(Ktau),
    b_M(T)=2JT exp(2JT)(2JT)^(M-1)/(M-1)!.

Consequently ||D_M-D||_F<=4K b_M(Ktau), and(1) gives directly on the finite circuit

    epsilon_M <= min(1, pi sqrt(2) K/(Jtau)
                      +2pi K^(3/2)b_M(Ktau)).     (3)

This derives the finite-channel bound without using a vacuum-only dilation for a thermal spin chain. M-1>=K is imposed for the cosine-sine bath pairing; it holds in the consumer below.

## 5. Concrete finite consumer and what it buys

Take J=1,omega=3,p=1/5,K=10,tau=10000,T=100000,M=2000001. With x=2JT=200000 and n=M-1=10x, n!>=(n/e)^n and e<3 give

    b_M(T)<x[3(3/10)^10]^x <10^-1000.

Using pi<22/7, sqrt2<10/7 and sqrt10<19/6 yields

    pi sqrt2 K/tau < 11/2450 <0.0045,
    2pi K^(3/2)<200,
    epsilon_M <0.0045+200*10^-1000<0.004501.

Every jointly prepared ten-input state, including entangled inputs with arbitrary retained reference, obeys this joint-output bound for the declared FSWAP apparatus. The two million initial reservoir modes have onsite mean energy omega p(M-1)=1200000; the hopping mean initially vanishes. Input energy, preparation cost, routing strings, timed switching and extraction are additional supplied resources. This is finite and expensive, not an efficient device or autonomous renewal.

## 6. Remaining interface and scientific effect

The original diagonal stream result remains intact. Coherent spin reinjection requires a different history algebra, exposed by a nonzero exact cross term. The explicit fermionic extraction alternative now has a complete finite-horizon output/reference theorem and an actual resource consumer. Neither result grants an adaptive comb estimate: a circuit with history-controlled injections can have different initial independence and routing. A useful next test is a diamond/strategy bound for the actual ordinary-spin process or a locally implementable parity-aware extraction with resource accounting. The phase-reference constraints in K2251 separately show why a number-diagonal bath cannot simply serve as a coherent detector reference. No GU mapping or source verdict moves.

## Reproduction

Run `python tests/channel-swings/k2250_quantum_stream_interface_probe.py`. `--write` refreshes the exact-control report. Default execution recomputes the controls, rejects genuine changed-input faults after a green baseline, and checks note/code/dependency hashes. Finite controls do not certify the universal written proofs. Independent internal review is distinct from external-expert, proof-assistant, novelty or remote-CI certification.
