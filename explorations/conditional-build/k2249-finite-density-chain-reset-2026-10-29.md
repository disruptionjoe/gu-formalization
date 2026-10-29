---
title: "K2249 Finite-density chain reset, Gibbs mismatch and surviving input memory"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no source selection or physical recovery
scripts:
  - tests/channel-swings/k2249_finite_density_chain_reset_probe.py
---

# K2249 Finite-density chain reset, Gibbs mismatch and surviving input memory

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: Finite-density chain reset, Gibbs mismatch and surviving input memory
carrier: finite-volume XY spin chains and algebraic half-line product state with arbitrary retained reference LAYER=toy CHIRALITY=N/A
pairing: positive finite spin Hilbert norm; infinite thermal state defined algebraically ON=declared_carrier
real_structure: complex conjugation and Hermitian adjoint as specified
grading: spin/fermion excitation number, not families
action_owner: repository-construction -- explicitly supplied models
target: complete endpoint channel, finite-volume approximation and conditional process renewal MAP-TYPE=intertwiner
```

## Question and new input class

[K2246](k2246-autonomous-vacuum-reservoir-2026-10-29.md) constructs a one-input vacuum reservoir. Replace its initial vacuum with a uniform finite-density product state while keeping the SAME nearest-neighbor dynamics. The endpoint channel remains exactly generalized amplitude damping for arbitrary reference. However its fixed state is thermal for onsite number energy, not Gibbs for the coupled Hamiltonian. Reinjecting into the same bath retains an explicitly computable memory term.

This is GU-independent supplied apparatus mathematics. Source register SC-META-53 remains UNCERTAIN and ledger0.263 LT-SM8 is not discharged. No source action, physical quotient, KMS thermalization for the coupled energy, autonomous input extractor or indefinitely reusable device is supplied. K2235's finite fresh-stock and entropy-capacity limits remain. Layer0 distinguishes onsite Gibbs, coupled Gibbs, stationary state, one-input channel and multiround process.

## 1. Exact endpoint channel without a vacuum-Fock density

For M sites indexed0,...,M-1, let h_M=omega I+J adjacency(path_M), J>0, omega>=2J, and H_M=dGamma(h_M), equivalently the open XY spin Hamiltonian. These finite-volume Hamiltonians are positive. Put tau_p=diag(1-p,p), 0<p<1, on each bath site1,...,M-1, independent of the arbitrary target/reference state rho_SF. Choose p=(1+exp(beta omega))^-1 when an onsite inverse temperature beta>0 is wanted.

Use Jordan-Wigner modes c_j with c_0=sigma^-_0. The even number-preserving Hamiltonian gives

    c_0(t)=sum_j u_0j(t)c_j, u(t)=exp(-it h_M),
    a=u_00, r=|a|.

Bath odd means vanish and <c_j* c_k>=p delta_jk for bath indices. Thus <c_0(t)>=a<c_0>, and

    <n_0(t)>=r^2<n_0>+p(1-r^2).

These identities apply with every reference matrix coefficient, or equivalently to all four target matrix units. For rho_SF=[[A,C],[C*,B]], T=A+B, the exact output is

    [[(1-p)T+r^2 D, a* C],
     [a C*, pT-r^2 D]], D=pA-(1-p)B.              (1)

The bath may have finite density even though the vacuum-sector derivation of K2246 no longer applies. Infinite product tau_p is defined by its compatible finite-site marginals; it is not a trace-class state on vacuum Fock space and has infinite total excitation/energy. Local half-line dynamics is the limit of these finite-volume evolutions. The endpoint formula below converges in complete channel norm, which is enough to define this output rigorously. No positive thermal-GNS generator is asserted; an equilibrium Liouvillian is a different object.

## 2. Reference error, spatial boundary and finite resources

Block positivity gives ||C||_1<=1/2, while ||D||_1<=max(p,1-p). Consequently the half-diamond distance from (1) to replacement tau_p tensor the SAME reference marginal is at most

    d(r,p)=min(1,r/2+max(p,1-p)r^2).              (2)

The sine-transform/Bessel calculation of K2246 applies to the one-particle matrix u regardless of bath density:

    a(t)=exp(-i omega t) J_1(2Jt)/(Jt),
    r<=min(1,1/(Jt)).                            (3)

The integral and recurrence are standard [DLMF10.9.2](https://dlmf.nist.gov/10.9.E2) and [DLMF10.6.1](https://dlmf.nist.gov/10.6.E1). This uses the established mathematical kernel, with no novelty claim.

Let b_M(T)=2JT exp(2JT)(2JT)^(M-1)/(M-1)! for M>=2JT+1. K2246's one-particle Duhamel proof gives |a_M-a|<=b_M(T) on0<=t<=T. Applying (1) to two amplitudes, and using ||a_M|^2-|a|^2|<=2|a_M-a|, gives

    half-diamond(Phi_M-Phi_infinity)
      <=|a_M-a|/2+max(p,1-p)||a_M|^2-|a|^2|
      <=(5/2)b_M(T).                            (4)

The vacuum Stinespring bound cannot simply be copied to a thermal many-particle representation. Equation(4) is the corrected channel proof. It also proves the endpoint thermodynamic limit on every finite time interval.

Example: p=1/5, J=1, omega=3, beta=log(4)/3, M=4001. K2246's exact integer estimate b_M(200)<10^-1000 still applies. Throughout100<=t<=200, (2)-(4) give error<=0.00508+(5/2)10^-1000; at t=200 it is<=0.00252+(5/2)10^-1000. This is reference-uniform reset to a MIXED state with excitation1/5, not erasure to the ground state. Finite initial bath energy is omega(M-1)p=2400, since all hopping means initially vanish. No estimate of preparing that state or renewing its stock is supplied.

## 3. Stationarity is not Gibbs for coupled energy

For any finite M, tau_p^tensor M is proportional to exp(-alpha N), alpha=log((1-p)/p). It commutes with every number-preserving hopping Hamiltonian, so it is stationary. For J nonzero and beta>0 it is not exp(-beta H_M)/Z. Already for two sites, the one-excitation Gibbs block is

    exp(-beta omega)[cosh(beta J)I-sinh(beta J)X]/Z,

with nonzero off-diagonal covariance, whereas the product state has zero such covariance. The equality exceptions include J=0 and beta=0. A supplied chemical-potential/number state is not silently a thermal state for the declared energy.

For an independently supplied gauge-invariant bath with covariance Gamma_B (not necessarily product), define v_j=conj(u_0j), j>=1, in the convention (Gamma_B)_jk=<b_k* b_j>. Then the output excitation is

    r^2<n_0>+v* Gamma_B v,                       (5)

with an equivalent transposed convention if Gamma is indexed oppositely. More unambiguously the noise is sum_jk conj(u_0j)u_0k <b_j* b_k>. Bath odd means must vanish and independence from SF is required. Uniform product gives p(1-r^2); an isolated-chain Gibbs input has covariance f_beta(h_B), f_beta(x)=1/(1+exp(beta x)), and need not give the same scalar p. We use the unambiguous sum in reproduction.

The fully coupled infinite equilibrium would instead have endpoint occupation

    q_beta=(2/pi) integral_0^pi sin^2(k)
                 f_beta(omega+2J cos k) dk.

For beta>0, omega>=2J>0, f_beta is strictly convex on positive energies, and the sine measure has mean energy omega and nonzero variance. Jensen gives q_beta>f_beta(omega)=p. This is a concrete thermal-state distinction, not a theorem that a newly decoupled target reaches q_beta after a local quench. Its global equilibrium already has correlations; replacing the endpoint destroys that initial equilibrium.

## 4. Exact surviving memory on the SAME half-line

Take independent DIAGONAL target inputs with first excitation probability q1, second q2. Start from the product bath, evolve for t1, discard endpoint0, independently replace it with the second input, then evolve for t2 on the same chain. Let P=|0><0|, Q=I-P, U(t)=exp(-ith). The first total covariance is pI+(q1-p)P. After evolution and endpoint replacement it becomes

    pI+(q2-p)P+(q1-p)|Q U(t1)0><Q U(t1)0|.

Therefore the second endpoint population is EXACTLY

    p+|a(t2)|^2(q2-p)
      +(q1-p)|a(t1+t2)-a(t2)a(t1)|^2.            (6)

The last term is the stored first input returning from the bath. From (3), its absolute value is at most

    max(p,1-p)[1/(J(t1+t2))+1/(J^2 t1 t2)]^2.    (7)

For Jt1=Jt2=200 and p=1/5, this is at most10201/2000000000=0.0000051005. The second input's residual population term is at most1/50000. This is a two-input population bound only, not an arbitrary-reference multiround process estimate.

The same calculation gives a finite-sequence diagonal-input recurrence. Just after insertion k, let C_k be the covariance. With equal time step U and independent diagonal q_k,

    C_1=pI+(q1-p)P,
    C_(k+1)-pI=(q_(k+1)-p)P+Q U(C_k-pI)U* Q.

Hence the output after step k is

    p+sum_(j=1)^k (q_j-p)|<0|U(QU)^(k-j)|0>|^2. (8)

This is an exact accounting rule for this input class. Section5 bounds the long sequence sum uniformly; adaptive or entangled injections remain outside that theorem. Even the two-site full-exchange control shows why independence cannot be assumed: an initially excited first input is stored in the bath; after discarding/replacing the endpoint, the second full exchange returns excitation with certainty, a replacement error1-p. This control reuses K2235's warning; (6)-(8) are the new same-chain quantitative result.

## 5. Uniform marginal reset for an arbitrarily long diagonal stream

Equation(8) has a useful consequence that does not require pretending the bath is fresh. Define the sampled return amplitudes and first-return amplitudes

    a_n=<0|U^n|0>, a_0=1,
    f_n=<0|U(QU)^(n-1)|0>, n>=1.

For |z|<1 the norm-convergent resolvents give generating functions

    A(z)=sum_(n>=0) a_n z^n=<0|(I-zU)^(-1)|0>,
    F(z)=sum_(n>=1) f_n z^n=1-1/A(z).             (9)

To prove the second equality, decompose U=(P+Q)U at each return: a_n=sum_(j=1)^n f_j a_(n-j). Equivalently use the P/Q block Schur complement of I-zU. For the unit spectral measure of U, A(z) is the average of1/(1-z lambda), |lambda|=1. Its real part exceeds1/2, since Re[1/(1-w)]=(1-Re w)/|1-w|^2>1/2 for |w|<1. Hence A never vanishes in the disk and |1/A|<=2. Consequently

    |F(z)|<=2|A(z)-1|,
    sum_(n>=1)|f_n|^2<=4 sum_(n>=1)|a_n|^2
                        <8/(J tau)^2.            (10)

The coefficient inequality follows by Parseval on each circle |z|=r<1 and monotone convergence as r tends to1. Equation(3) gives |a_n|<=1/(nJtau); the elementary integral comparison sum1/n^2<2 yields the final strict bound. No unproved absolute summability, numerical decay fit or Markov approximation is used. The sharper constant2pi^2/3 is available from sum1/n^2=pi^2/6 but is not needed.

For any number k of independent diagonal target inputs, each q_j in[0,1], combine(8),(10):

    |q_out,k-p|<8 max(p,1-p)/(Jtau)^2,             (11)

or the trivial bound1 when smaller. All full states in this theorem are gauge invariant, so the target marginal is diagonal and its half trace distance to tau_p is exactly |q_out,k-p|. At p=1/5 and Jtau=200 the bound is0.00016 for EVERY round, regardless of the chosen deterministic input probability sequence. This is actual reuse of the same semi-infinite finite-density reservoir, not a fresh-tape replacement.

It remains a MARGINAL theorem: outgoing targets may correlate with one another and the bath. There is no bound here on their joint state, on arbitrary quantum-reference input, on adaptive correlated injection or on input/extraction work and timing. The infinite initial bath is a resource of unbounded total energy and entropy capacity. Finite chains have recurrence and do not inherit the infinite-time estimate merely from a finite-horizon single-use bound. Equation(11) narrows the repeated-input question substantially without closing the complete-process interface below.

### A finite chain and a finite stream horizon

For K rounds let T=Ktau and choose M>=2JT+1. Write a_M,n and f_M,n for its sampled return and first-return coefficients. Equation(4)'s one-particle input gives |a_M,n-a_n|<=b_M(T) for1<=n<=K. Both finite/infinite spectral resolvents satisfy ||1/A||_infinity<=2 in the unit disk. Since

    F_M-F=(A_M-A)/(A_M A),

replace A_M-A by its degree-K truncation: the first K output coefficients do not change. Parseval and the bounded analytic multiplier yield

    ||(f_M-f)_(1:K)||_2<=4 sqrt(K)b_M(T).

The triangle inequality and(10) now prove for every k<=K

    |q_out,M,k-p|
      <=m[sqrt(8)/(Jtau)+4sqrt(K)b_M(Ktau)]^2,
    m=max(p,1-p).                                (12)

This is a finite-resource stream theorem, still for independent diagonal inputs and individual output marginals. It does not silently reuse a one-input bath-freshness assumption.

Example: J=1, tau=200, K=1000, T=200000, M=4000001. Set x=2JT=400000 and n=M-1=10x. The factorial lower bound n!>=(n/e)^n and e<3 give b_M(T)<x[3(3/10)^10]^x<x 10^(-4x)<=10^(-3x)<10^-1000. Also sqrt8<3 and4sqrt1000<128, so the bracket in(12) is below0.015001. At p=1/5, every one of these1000 output marginals lies within0.000181 of tau_p. This deliberately large finite chain has4000000 initial bath spins and onsite mean energy2400000 for omega=3. No claim of efficient hardware, automatic extraction/timing, full joint renewal or all-later-time finite reset is made.

## 6. A sufficient complete-reference process condition

For r<1 the endpoint output algebra depends only on S and one normalized bath CAR mode b=sum_(j>=1)u_0j b_j/sqrt(1-r^2), with the target parity factor retained in c_j. In finite volume a bath-only passive mode rotation isolates b as a qubit factor. The infinite version is the norm limit of the l2 mode coefficients in the CAR algebra. The restricted output map is a two-mode fermionic beam-splitter channel; no access to other bath modes is needed for its endpoint observables.

Let F include ALL retained history. Suppose at entry to round k the actual restricted S,F,b state is within half trace norm delta_k of rho_SF tensor tau_p. Data processing and (2) give output-to-tau_p tensor rho_F error<=delta_k+d(r_k,p). Arbitrary intervening completely positive trace-preserving operations contract trace distance, so a hybrid/induction argument bounds the retained multiround outputs by sum_k(delta_k+d_k), capped at1, whenever those entry conditions hold for the actual process. Including outputs in F is essential.

Neither a correct bath occupation nor a correct single-mode marginal proves delta_k small. Correlations with S/history are part of delta_k. Equations(6)-(8) do not establish this hypothesis for arbitrary inputs. The criterion identifies the exact missing renewal estimate rather than granting independence by relabeling the reused bath as thermal.

## Review and remaining input

The independent review challenged the thermal representation, endpoint phase, finite-chain factor, Gibbs interpretation and bath reuse. Followthrough derived a coupled-equilibrium occupation mismatch, explicit two-injection memory, a general diagonal sequence recurrence, uniform marginal reset for every length of independent diagonal stream, and the correct complete-process freshness condition. Exact finite probes supplement the analytic proof; no physical apparatus, source selection, infinite renewal, external-expert, proof-assistant or remote-CI certification is claimed. A next useful result would prove the relevant-mode/history decorrelation under a specified repeated-input extraction process, or analyze an actual coupled Gibbs bath after the target quench. Repeating one-input GAD algebra does not supply either.

## Reproduction and evidence kinds

Run `python tests/channel-swings/k2249_finite_density_chain_reset_probe.py`. Default execution recomputes exact finite controls and genuine input faults, then checks report/code/note/dependency hashes. `--write` refreshes the report. Universal proofs are written mathematics independently reviewed internally; finite controls do not prove them. No external-expert, novelty or proof-assistant claim.
