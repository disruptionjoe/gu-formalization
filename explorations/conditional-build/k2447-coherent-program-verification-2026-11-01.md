---
title: "K2447 Coherent references for mixed program verification"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: "conditional coherent-reference certificate; no free upgrade of measured instruments or native GU identification"
---

# K2447 Coherent references for mixed program verification

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
result: K2447
carrier: original normalized flagged qubit Choi states with nine-dimensional coherent environment LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace and trace distance ON=declared_carrier
real_structure: complex Hermitian positive states and real probabilities
grading: coherent environment, recorded flags, ordered slots and private route
action_owner: repository-construction -- supplied conditional mathematical model
target: pure extension witness and original instrument access boundary MAP-TYPE=evaluation
```

## Result and changed premise

A trusted coherent reference permits verification of the original mixed program sigma without K2445's random-block floor. Fix a pure target P=|Psi><Psi| on S tensor E with Tr_E P=sigma. For any actual joint state rho, including one entangled with an inaccessible memory,

    e=1-Tr(P rho),     D(Tr_E rho,sigma)<=sqrt(e).            (1)

One joint program is sufficient per test/use round. This changes the resource interface: the original measured instrument does not by itself expose a purification. K2445 remains valid when only recorded programs and whole correlated blocks are available. This is established quantum state verification specialized to the exact original instruments, not a novelty claim. The pure-state measurement framework is described by [Wang and Hayashi](https://www.nature.com/articles/s41534-019-0226-z). SC-META-53 remains UNCERTAIN; positive Hilbert programs are conditional mathematics, not a derived GU physical quotient. Source, physics ledger0.263 and canon stay unchanged.

To prove(1), decompose rho into pure states. Pure-state trace distance to P is sqrt(1-overlap); convexity and concavity of square root give D(rho,P)<=sqrt(e). Partial trace is contractive. On use discard E and dephase S's classical flags. That fixed channel leaves sigma invariant and cannot increase the distance. Never pass E or correlated environment data to the downstream controller.

## 1. Explicit coherent original instrument

Use the two original laws in K2419/K2439, with w in(0,1), mean vector m=(m_x,m_z), ell=||m||, n=m/ell and visibility v=1/2. For s,h,z in{-1,+1}, let a_s=(1+s ell)/2, b_h=(1+h v)/2, and |h;n_s> the h eigenvector of n_s dot(X,Z), n_s=s n. Define nine Kraus operators

    K_g=sqrt(1-w) I,
    K_(z,s,h)=sqrt(w a_s b_h) |h;n_s><z;n_s|.               (2)

The good Kraus has accessible flag g; the other eight have accessible flag z and a distinct environment label(z,s,h). The isometry V=sum_a |flag(a)> tensor K_a tensor |a> obeys V*V=I: summing h gives a normalized output, summing z gives I, and summing s gives one. The purified Choi vector is

    |Psi>=(I_R tensor V)|Phi_RA>,   dim(S)=12, dim(E)=9.     (3)

Tracing E gives exactly K2439's three original Choi blocks, including the plus/minus conditional probabilities and v=1/2 output visibility. The nine S-side Kraus Choi vectors are orthogonal. Their squared norms are

    lambda_g=1-w,   lambda_(z,s,h)=w a_s b_h/2.             (4)

All nine weights are positive for both original laws. Thus sigma has rank9 and E dimension9 is minimal for a pure extension. For r independent target slots the target is |Psi> tensor-power r. Testing each slot projector and accepting iff every slot passes implements exactly its rank-one product projector, even for an arbitrarily correlated actual r-slot state. This does not make actual slots independent. A generic nonproduct target requires its own verifier.

A finite joint ideal implementation is the Householder reflection U=I-2|v0><v0|, v0=(|0>-|Psi>)/sqrt(2-2<Psi|0>), in the declared real basis. It maps |0> to |Psi>; applying U* and testing zero implements P. The probe checks this action, but a dense finite matrix is not a hardware compiler.

### Released construction: two settings with one-way reference readout

The original rank9 target also has an explicit verifier requiring no joint E/S entangling gate. Write its Schmidt form |Psi>=sum_i sqrt(lambda_i)|u_i>_S|i>_E, with i=0,...,s-1, s=9. The u_i are the normalized original Kraus Choi vectors. Choose between two tests with equal probabilities:

1. Measure E in its declared basis; for outcome i, accept iff S passes |u_i><u_i|. The acceptance effect is P_Z=sum_i |u_i,i><u_i,i|.
2. Measure E in the Fourier basis |f_k>=s^(-1/2)sum_i omega^(ik)|i>, omega=exp(2pi i/s); for outcome k, accept iff S passes |v_k><v_k|, v_k=sum_i sqrt(lambda_i)omega^(-ik)u_i. The effect is P_F=sum_k |v_k,f_k><v_k,f_k|.

Both are projections. Finite Fourier orthogonality gives, in Schmidt coordinates,

    (P_F)_(i,a;j,b)=sqrt(lambda_i lambda_j)
                     1{a-i=b-j mod s}.

Equivalently P_F=sum_c |Psi_c><Psi_c| with Psi_c=sum_i sqrt(lambda_i)|u_i,i+c>. These s vectors are orthonormal; P_Z kills each c!=0 and fixes Psi_0=Psi. Therefore P_Z P_F=P_F P_Z=P. The randomized verifier Omega=(P_Z+P_F)/2 has unique eigenvalue1 at Psi and all other eigenvalues in{1/2,0}; for s>=2, its gap is exactly nu=1/2. Outside supp(sigma) tensor E both tests reject. This is a universal exact argument, with the two actual rank9 banks and Fourier residue identity checked separately. It does not rely on an untested matrix eigensolver.

The first setting uses a classical reference basis. The second requires coherent superpositions across the original flags on S. Thus ordinary measured flags still cannot implement this interface for free. Communication E-to-S is confined to test rounds; use rounds discard E without disclosing its outcome to the controller. State-dependent single-register projections, phase conventions, random settings, storage and their aggregate effect error beta require trusted implementation. The construction provides two equally randomized setting families and nine reference outcomes with E-to-S feedforward, not measured gate times or an operational device. Locality here means only across E|S: a conditional S projection can require entangled operations among its reference, output and coherent flag components. Reversing the unknown producer is not independent trusted verification.

## 2. Measured records fail the stronger test without spoiling the program

Full environment dephasing leaves Tr_E rho=sigma but its acceptance is sum lambda_a^2=Tr(sigma^2). Dephasing only the accessible flag similarly leaves sigma unchanged but gives acceptance (1-w)^2+w^2/2. Exact original values are:

| law | full environment dephasing | flag dephasing |
| --- | --- | --- |
| first | 50434873/216320000 | 6787/20000 |
| second | 347981/1730560 | 1819/5408 |

These are strongly rejected coherent resources that nevertheless implement the correct reduced program. Hence the certificate is sufficient, not necessary. A changed environment purification gauge can also reduce acceptance without changing sigma. Fixing one gauge is an explicit verification premise.

There is no general nondisturbing free upgrade. Let a channel Lambda from a support H to H tensor E satisfy Tr_E Lambda=id_H on every state in that support. Its Choi marginal is the pure maximally entangled state. Every positive extension of a pure marginal factors, so J_Lambda=Phi tensor tau_E, and Lambda(rho)=rho tensor tau_E. It cannot turn a mixed sigma into a pure extension. A reset/replacement channel can prepare a passing resource, but then it certifies that newly prepared resource, not the original device. This no-go requires identity on the whole support; it does not exclude a target-specific replacement or a disturbing operation on a restricted family.

A simpler one-copy zero-failure limitation is exact: W>=0 and Tr(W sigma)=0 imply W^(1/2)sigma^(1/2)=0, hence W annihilates supp(sigma). Such a witness sees none of the original causal alternatives sigma +/- tH, H=Z_R tensor Y_B in the plus block, t=1/100000. Their positive-support minimum eigenvalues exceed t, Tr_B H=0, and D(sigma +/- tH,sigma)=2t. Every joint extension of either alternative must have e>=4t^2 by(1). Signed multi-setting tomography is not excluded; neither is a positive score with a nonzero target baseline. The theorem rules out a free nonnegative zero-baseline witness that resolves internal mixed-state variation.

## 3. Spectral gap and downstream use

A trusted acceptance effect Omega with Omega|Psi>=|Psi> and

    0<=Omega<=P+(1-nu)(I-P),    0<nu<=1,

has failure probability p>=nu e. If actual readout effect differs by operator norm at most beta_t, then e_t<=(p_actual,t+beta_t)/nu. The calibration bound must hold for the same conditional resource before routing; an average over all rounds cannot silently replace an actual-use allowance. Rank-one target uniqueness matters: a degenerate accepted subspace cannot certify a specific vector or mixed state.

For local target-slot verifiers with gaps nu_j, their accept-all product has gap min_j nu_j. It need not lose the product of gaps: every non-target joint eigenvector has at least one rejected slot. The witness has a unique target eigenvector and can be used on correlated inputs. Both ideal and imperfect local implementations still require trusted access to their full coherent slot registers.

[K2448](k2448-binary-hidden-route-certificate-2026-11-01.md) bounds the mean pre-route conditional failure probabilities on actual use indices. Combining its bound B_U with calibration gives mean-used e<=Q_U=min(1,(B_U+mean_used beta)/nu) and mean resource distance<=sqrt(Q_U). For the K2444 heralded controller,

    epsilon=sqrt(Q_U),  theta=lambda epsilon+kappa,
    D(normalized mean success, same-history ideal mean)
       <=min(1,theta/q),                                   (5)

with q=D_in^(-2), lambda=1/d_A1. Require actual mean success>0; theta<q guarantees it. kappa bounds the completed trusted operation's mean error, including storage and controller errors; it is not multiplied by lambda. History-selected controllers with fresh private initialization independent of the current resource are allowed, and within-batch feedback is retained. This is not a final-transcript state, an across-round joint process, future-device claim or the mean of individually normalized successful outputs.

## 4. Decision and remaining inputs

This removes the dimension/block-size floor under a stronger coherent-access premise and removes a proposed nondisturbing shortcut for obtaining that premise. The original product target permits slot-local verification, while K2448 supplies the non-iid statistics. Actual coherent custody, trusted verifier compilation/calibration, storage and success records remain missing. No experiment is reported. If only measured records are accessible, retain K2445 or the full tomography interface instead of treating a failed purification test as evidence that the reduced instrument is wrong.

[Exact probe](../../tests/channel-swings/k2447_coherent_program_verification_probe.py), [report](../../lab/process/k2447-coherent-program-verification.json). Written universal arguments, finite exact controls and prospective numerical budgets are separate evidence. Internal independent review is not external-expert or proof-assistant certification.
