---
title: "K2253 Complete detector instruments with a finite reusable phase reference"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional finite-resource apparatus theorem; no source selection or physical recovery
scripts:
  - tests/channel-swings/k2253_full_instrument_reference_reuse_probe.py
---

# K2253 Complete detector instruments with a finite reusable phase reference

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2253 Complete detector instruments with a finite reusable phase reference
carrier: finite-mode bosonic Fock system, finite charge reference and neutral instrument ancillas LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert inner product ON=declared_carrier
real_structure: complex conjugation and Hilbert adjoint
grading: physical total oscillator number and neutral record labels; not families
action_owner: repository-construction -- supplied conserving shell unitaries
target: complete recorded field instrument and joint reference restoration MAP-TYPE=intertwiner
```

## Question and distinction from prior results

[K2251](k2251-detector-phase-reference-2026-10-29.md) approximates binary record statistics with a finite phase reference, explicitly leaving field backaction and reuse open. Here the target is the full recorded field instrument, including any external quantum reference, and the apparatus reference is retained in the error comparison. The new ingredient is an output-energy bound plus a finite isometry completion; positivity of compressed effects alone cannot prove this result.

The target is a supplied finite-mode oscillator instrument with Stinespring isometry V and total number N. Its finite-dimensional outcome record is dephased after V; an additional environment may be discarded. Write G=N+1. Assume the actual instrument has the quadratic-form bound

    V* (G tensor I) V <= C G, C finite.                 (1)

This is an assumption to establish on the chosen target, not a property of every effect. All fresh dilation/environment ancillas below carry ZERO charge, with explicitly allowed finite degeneracy. The controllable unitary conserves system-plus-reference number. It need not be local, efficiently synthesized, autonomously timed or subject to a specified control alphabet.

[K2241](k2241-local-mode-detector-network-2026-10-29.md) gives (1) for its detector by Gaussian collection, number-diagonal controlled rotation and Gaussian readout. For the actual two-mode b=(5/3)a1+(4/3)a2*, select E=1_(b*b=0) and the recorded Lüders instrument with Kraus E,I-E. The squeeze has exp(|t|)=3, so collection and inverse readout each bound G by9G; number-diagonal measurement preserves its expectation in collected coordinates. Thus C=81 is a valid conservative constant. It is not asserted optimal.

The conserved quantity is physical total NUMBER. Exact conservation of a nonuniform Hamiltonian does not follow; it requires another spectral lift. A positive one-particle energy gap h_min converts an input energy budget E to B<=E/h_min.

This is conditional apparatus mathematics on a positive Hilbert space. Source SC-META-53 remains UNCERTAIN; LT-SM8/LT-GR6b and ledger0.263 are unchanged. No source action, physical quotient, native2+1 or chirality result follows. General phase-reference ideas are established background, including [Åberg's catalytic-coherence model](https://arxiv.org/abs/1304.1060); this finite joint-error statement is not a novelty or exact-catalysis claim. Sine-shift estimates are reused from K2240/K2251.

## 1. A finite isometry that retains the target backaction

For integer cutoffs Q>=0 and R>=Q, let P_Q=1_(N<=Q), P_R=1_(N<=R). Their ranks for m modes are binomial(m+Q,m) and binomial(m+R,m). Define

    A=(P_R tensor I)V P_Q,
    D=(P_Q-A*A)^(1/2).

Even if the original environment is infinite, choose bases of P_Q and of output P_R times the finite record. Expanding A on those bases gives at most d_Q*d_R*d_record environment vectors. Their span E_fin is finite and contains the range of A; implement that neutral environment and use its isometric embedding into the original environment only for comparison. Finite outcome alone would not justify a finite environment.

Add orthogonal success/failure flags. Put a neutral copy of the P_Q input space in the failure environment and define on P_Q

    W psi = A psi tensor |success>
          + |vacuum,record0> tensor D psi tensor |failure>.     (2)

The initial and unused ancilla spaces can be enlarged by finite neutral dimensions. W*W=A*A+D²=P_Q, so W is an isometry. Its output field charge is at most R. Compare with V psi tensor success. Its removed high-charge success vector is orthogonal to the new failure vector, and

    ||W psi - V psi tensor success||²
      =2||(I-P_R) V psi||².                            (3)

Equation (3) is valid with any external reference by tensoring all maps with its identity. It preserves the low-output amplitudes, including record coherences prior to dephasing; it is not an effect-only compression or a polar factor with a potentially singular inverse.

For an arbitrary normalized input/reference state with Tr(N rho)<=B, apply (3) to the subnormalized low-input purification. Since P_Q commutes with G and the high-output G is at least R+2,

    output error <= sqrt(2C(B+1)/(R+2)).                (4)

The trace-distance convention throughout is one half the trace norm. The pure-state estimate || |u><u|-|v><v| ||_1/2 <= ||u-v|| for vectors of norm at most1 and contractivity under discarding/dephasing give (4). Input truncation affects both channels; the gentle-projection bound gives the combined contribution

    2sqrt(B/(Q+1)).                                    (5)

No energy expectation convergence is inferred from trace distance alone.

## 2. Physical finite-reference realization, including end shells

Let L>=2 and take a reference with integer charges0,...,H, where

    H=R+L-1+Q.

Prepare the shifted sine packet beta supported on charges R,...,R+L-1:

    beta_(R+j)=sqrt(2/(L+1)) sin((j+1)pi/(L+1)), 0<=j<L.

In each total-charge shell t with R<=t<=H, define the map on the subspace of low-input states with a fixed initialized neutral ancilla by copying W's amplitudes:

    |n,alpha> |t-n> |anc0>
      -> sum_(m,beta,e) W_(m,beta,e;n,alpha)
                          |m,beta> |t-m> |e>.          (6)

All reference levels in (6) exist: input n<=Q<=R, output m<=R, and t is in [R,H]. Orthogonality follows from W*W=I, including degenerate system charges. Complete this partial isometry to a unitary separately inside each finite total-charge shell, using the same enlarged neutral ancillary space on both sides. On unused sectors choose an arbitrary unitary, and outside the finite system/reference workspace use identity. This defines a genuine charge-conserving unitary on the whole system with finite charged apparatus. Every low-input component of the chosen reference lies in the good shells. End-shell padding, not periodic wraparound, is essential.

For the comparison only, embed beta in l2(Z) and use bilateral translations S. The lifted isometry factors as input-controlled translation S^n, W on the finite system, then output-controlled translation S^(-m). Orthogonality of charge eigenspaces (and their full degeneracies) gives

    ||lift(W)(psi tensor beta) - W psi tensor beta||
      <= max_(n<=Q)||S^n beta-beta||
         +max_(m<=R)||S^m beta-beta||
      <= (Q+R) delta_L,
    delta_L=2sin(pi/(2(L+1))) <= pi/(L+1).             (7)

These shifts prove an estimate; they are not an infinite physical battery. The actual apparatus is the finite shell unitary (6). Incomplete shells have already been handled by unitary completion, not by truncating a translation and pretending it is unitary.

Combining (4),(5),(7), tracing only the new environment and dephasing the record, the actual output on FIELD + RECORD + arbitrary external reference + retained charge reference differs from the ideal full instrument output tensored with the ORIGINAL pure beta by at most

    epsilon(B;Q,R,L) <= min(1,
       2sqrt(B/(Q+1)) + sqrt(2C(B+1)/(R+2))
       +(Q+R)pi/(L+1)).                               (8)

Thus this is simultaneous field-backaction accuracy, record accuracy and approximate reference restoration/decorrelation. It is stronger than K2251's binary-effect theorem and weaker than exact restoration. Finite neutral workspace, arbitrary block synthesis, precision and control time remain supplied resources.

## 3. Correlated finite reuse and adaptive controllers

Use the same charge reference for K calls, with fresh neutral ancillas each time. Allow arbitrary CPTP controllers between calls acting on accessible system, records and retained memory, but not on the apparatus reference. Assume the IDEAL comparison process presents mean number at most B to every detector call, averaged over its records. Apply the same controllers in both processes. In a hybrid expansion insert the physical-versus-ideal comparison on a state whose past calls are ideal. The reference there is beta and independent, and all history/memory is part of the arbitrary external reference covered by (8). Subsequent physical channels contract trace distance even when they create correlations. Therefore

    epsilon_K <= min(1, K epsilon(B;Q,R,L)).             (9)

Real intermediate states need not be independent of the battery and need not obey a separately assumed real-history energy bound. This is precisely why a marginal-fidelity argument would be insufficient and why beta is kept in the one-call comparison. The ideal-input mean-number hypothesis is substantive; an adaptive controller that injects unbounded energy is outside it. Conditioning on a rare outcome can magnify normalized error, so (9) is an averaged joint-process statement, not a uniform postselected-history guarantee. Controllers themselves can import energy/coherence; their resource cost is not hidden in (8).

## 4. An explicit finite consumer

For the actual E Lüders instrument choose B=1,C=81,K=10 and

    Q+1=16000000, R+2=5184000000, L+1=100000000000000.

Then R>=Q and the first two terms in (8) are exactly1/2000 and1/4000. Using pi<22/7, its last term is less than0.000164. Hence epsilon<0.000914 and the complete ten-call adaptive bound is less than0.00914. The reference maximum charge is H=100005199999995 and its mean charge is50005183999997, from H=R+L-1+Q and R+(L-1)/2. These enormous but finite values are an existence/resource accounting result, not a practical or optimal detector. The number of system cutoff states and neutral workspace are finite; exact matrix synthesis remains assumed.

## 5. Exact restoration is still excluded for this charge source

For vacuum input, K2251 gives E|00>=(3/5)|Omega_b>, and the normalized squeezed vacuum has mean total number32/9. The nonselective Lüders output is E rho E+(I-E)rho(I-E). Since N|00>=0, its mean charge is

    2 <00|E N E|00> = 2*(9/25)*(32/9) =64/25.          (10)

A finite reference, neutral fresh ancillas and exact total-number conservation cannot produce this target and exactly restore even the reference marginal on vacuum: conservation would require a strictly positive increase of the field number with no decrease elsewhere. Correlations do not evade this expectation identity. Approximate trace restoration in (8) is consistent because a tiny change in a large reference can carry finite charge. This does not exclude an apparatus with another charged resource, and it does not imply an energy-error bound from (8).

A bounded witness makes this incompatibility quantitative without assuming continuity of unbounded energy. For integer J>=1 put F_J=min(N,2J). The target vacuum output has probability162/625*(16/25)^j at N=2j for j>=1, and probability337/625 at zero, so

    mu_J=Tr(F_J rho_target)=64/25*[1-(16/25)^J].

Let epsilon_S bound the actual field trace-distance error and delta_B the reference marginal restoration error, with reference spectrum0,...,H. Conservation, positivity and bounded-observable trace duality give

    H delta_B >= max(0, mu_J-2J epsilon_S).             (11)

Indeed the field's actual mean N is the reference's mean loss and is at least its expectation of F_J; field closeness loses at most2J epsilon_S, and reference closeness bounds the mean loss by H delta_B. If a single joint error epsilon bounds both marginals, then epsilon>=mu_J/(H+2J). Already J=1 gives epsilon>=(576/625)/(H+2). This lower bound is not asserted to match the constructive upper bound.

A separate countercontrol isolates the backaction gap: measuring E and preparing physical vacuum has exactly the target records, but on Omega_b its field output is4/5 away from the target Lüders output. Matching record statistics cannot certify (8).

## Scope, review and reproduction

This construction follows the effect-only result into a full instrument and finite correlated reuse, without equating classical records with field backaction or finite reuse with perpetual catalysis. Remaining questions are restricted local synthesis, quantitatively economical reference replenishment, actual controller costs and an infinite-mode/continuum energy-domain bridge.

Run `python tests/channel-swings/k2253_full_instrument_reference_reuse_probe.py`; `--write` refreshes its report. Exact small controls test a genuine charge-changing isometry, degenerate charge sectors, failure completion, shell orthogonality, translation orientation and reference coherence. Universal Hilbert-space and adaptive hybrid arguments are written proofs reviewed independently, not inferred from finite checks. No proof-assistant, external-expert, remote-CI or novelty certification is claimed.
