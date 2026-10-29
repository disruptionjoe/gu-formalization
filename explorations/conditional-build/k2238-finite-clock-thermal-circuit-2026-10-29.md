---
title: "K2238 Finite positive Hamiltonian clock for thermal circuits"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: finite engineered time-independent positive Hamiltonian renewal with supplied fresh Gibbs stock and approximate readout window; no autonomous permanent halt, cyclic apparatus, battery cost, local field apparatus or GU realization
scripts:
  - tests/channel-swings/k2238_finite_clock_thermal_circuit_probe.py
---

# K2238 Finite positive Hamiltonian clock for thermal circuits

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: finite continuous positive autonomous compiler and padded thermal-renewal timing window
carrier: M+1 dimensional positive clock, N bank qubits, N supplied fresh Gibbs ancillas and arbitrary retained reference LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace form ON=declared_carrier
real_structure: ordinary complex adjoint
grading: finite clock position and binary occupation
action_owner: repository-construction -- engineered time-independent programmed Hamiltonian and supplied fresh stock
target: finite renewal channel, programmed bandwidth, timing-error bound and exact-plateau obstruction MAP-TYPE=intertwiner
```

Conditional derivation with independent internal review. Classification INTERNAL_STRUCTURAL_ONLY; target NONE-NOT-A-KILL. Carrier: finite positive clock C^(M+1), finite bank and fresh thermal qubit stock D, arbitrary retained reference F. Pairing: ordinary positive Hilbert trace; real structure: complex adjoint; grading: clock position and qubit occupation. Action owner: repository-supplied time-independent Hamiltonian. No GU source action, physical quotient, locality/transport model, selected clock, thermodynamic optimum, permanent autonomous halt or indefinitely reusable apparatus follows.

## Startup, duplicate and inference audit

Read AGENTS, GEOMETER-VS-PHYSICS-OBJECTS (operative T15/T16/T17), source-native comparator routing, Layer0, current state, research posture, verification/contribution rules, path-dependency index, K2232 and K2235. This is the positive finite apparatus already declared there; it is not the source's indefinite geometric carrier. Nothing moves LT-SM8, source claims, votes or ledger grades. Preserve the standard comparator-routing notice in the final artifact.

K2235 already proves finite exchange renewal, full-exchange exact replacement, fresh-state counts, energy/entropy identities and finite cyclic-sink bounds. Those are reused, not new. K94's observed-autonomous-clock instrument wave already compiles a four-state DISCRETE unitary and explicitly chooses NO continuous Hamiltonian; it closes by an inverse leg. The increment here is an explicit continuous, positive, finite, time-independent Hamiltonian with exact ordered completion, reference-uniform timing-error bounds, padding and an actual thermal consumer. Perfect transfer and Feynman history constructions are established mathematics, not a novelty claim. Primary background: Christandl et al., [Perfect state transfer in quantum spin networks](https://arxiv.org/abs/quant-ph/0309131) (Phys. Rev. Lett.92,187902); the formulas below have direct proofs.

## 1. A positive finite autonomous Hamiltonian

Let D be finite dimensional, H_D>=0 fixed, and let U_1,...,U_L be supplied unitaries commuting with H_D. Add R>=0 identity gates, M=L+R. Define V_0=I, V_k=U_k...U_1 for k<=M, and

 W=sum_(k=0)^M |k><k| tensor V_k,
 a_k=sqrt((k+1)(M-k)),
 A_M=sum_(k=0)^(M-1) a_k (|k+1><k|+|k><k+1|),
 H_P=g M I +g sum_k a_k (|k+1><k| tensor U_(k+1)+h.c.),
 H=I_C tensor H_D+H_P, g>0.                          (1)

H_P is the COMPLETE programmed controller term, including clock-data interactions; its budget is not a bare-clock energy. W is unitary and

 W* H_P W=g(MI+A_M), W*(I tensor H_D)W=I tensor H_D. (2)

To prove the spectrum without a guessed matrix exponential, realize C^(M+1) as the symmetric subspace of M qubits, with |k> the normalized weight-k state. Sum_(r=1)^M X_r has entries a_k and is A_M; its symmetric eigenvalues are -M,-M+2,...,M. Thus H_P has spectrum {0,2g,...,2gM}; H>=0, [H_P,H_D]=0, and its programmed bandwidth is 2gM. All carriers and couplings are finite. This Hamiltonian is engineered, not derived from geometry, and a clock transition can address a distant data pair; no spatial locality is established.

At initial clock |0>, for every input rho_DF,

 <H_P>=gM, Var(H_P)=g^2 M, <H>=<H_D>+gM.            (3)

The first statement follows because off-diagonal clock blocks have zero expectation; A_M^2 at 00 equals M. Cross covariance with H_D is zero. These conserved controller resources are not dissipated switching work. There is no time-dependent H and hence no supplied pulse-work term integral <dot H>dt during the run. Initial apparatus preparation, engineering the interactions, admitting data, observing the endpoint and recycling are additional operations whose costs are not priced.

## 2. Exact autonomous endpoint and arbitrary-reference channel

The M-qubit factorization exp(-igt sum X_r) yields

 alpha_k(t)=sqrt(C(M,k)) cos(gt)^(M-k) [-i sin(gt)]^k,
 |Psi(t)>=exp(-igMt) sum_k alpha_k(t)|k> tensor
                exp(-itH_D)V_k|psi>.                 (4)

For mixed/reference inputs extend linearly or purify. The norm sum is (cos²+sin²)^M=1. At T=pi/(2g), only k=M survives, proving exact final decoupling of the clock:

 rho_CDF(T)=|M><M| tensor (e^-iTH_D V_L tensor I_F)
                  rho_DF(V_L* e^iTH_D tensor I_F).    (5)

Thus no per-gate external switch is needed. Initialization and an elapsed-time endpoint/readout convention remain supplied. Intermediate prefixes are in quantum superposition; this is not an ordered schedule of individually switched collisions or the K2232 Markov semigroup at intermediate times.

Trace the clock at general t. The data/reference channel is exactly

 E_t=sum_k b_k(t) Ad[e^-itH_D V_k],
 b_k=C(M,k) p^k(1-p)^(M-k), p=sin²(gt).              (6)

For k>=L, V_k=V_L. Convexity of half diamond distance gives

 (1/2)||E_t-Ad[e^-itH_D V_L]||_diamond
 <= sum_(k<L)b_k(t).                                (7)

This bound is uniform on all D inputs and arbitrary references, including retained history and arbitrary correlations with the already included fresh stock. To interpret V_L as the desired product-Gibbs replacement, the stock must separately satisfy K2235's independent product-Gibbs input hypothesis. Eq.(7) alone does not create freshness.

## 3. Identity padding gives an explicit timing window

For t=T+delta, define r=sin²(g delta), R=M-L, and J~Bin(M,r). Then

 error <= Pr[J>=R+1]
 =sum_(j=R+1)^M C(M,j)r^j(1-r)^(M-j)
 <= C(M,R+1) r^(R+1)
 <= C(M,R+1)(g delta)^(2R+2).                        (8)

The middle bound follows from 1_{J>=R+1}<=C(J,R+1) and E C(J,R+1)=C(M,R+1)r^(R+1). Cap the bound at1. Without padding it is 1-cos^(2M)(g delta)<=M(g delta)^2. With padding the output error has higher even order. These are sufficient upper bounds, not a universal optimal time-energy law or an exact diamond norm. Clock-discarded output is essential: a joint claim that the clock is itself near |M> has trace distance sqrt(1-(1-r)^M), generally only linear in |delta|. Padding does not improve that clock-return statement.

For fixed total programmed bandwidth B=2gM, T=pi M/B. Peak link coefficient is g sqrt(floor((M+1)^2/4)); bounded link coefficients therefore require correspondingly longer time as M grows. Padding purchases robustness with clock dimension M+1, programmed bandwidth at fixed g, or longer runtime at fixed bandwidth. It is not free.

For a bounded static additive Hamiltonian error V, Duhamel gives half-diamond output error <=|t| ||V|| after scalar parts are removed, added to (8). An independently supplied clock state rho_C with half-trace distance at most epsilon_C from |0><0| contributes <=epsilon_C; equivalently one may assume the WHOLE initial joint state is within epsilon_C of |0><0| tensor rho_DF. A clock marginal-only bound with uncontrolled initial correlations is not this hypothesis. This is a specified-error budget, not a physical calibration certificate.

## 4. Thermal consumer and complete resource count

Take D=B_1...B_N A_1...A_N, each pair with equal gap E_j>=0,

 H_D=sum_j E_j(n_Bj+n_Aj),
 U_j=exp[-i(pi/2)X_j], X_j=|01><10|+|10><01|,
 rho_DF=incoming rho_BF tensor product_j tau_Aj.      (9)

All U_j commute with H_D. Their product implements N full resonant exchanges, so tracing A gives EXACT product-Gibbs replacement of B and decouples it from F, by the K2235 Kraus proof. Free B rotation fixes the diagonal Gibbs target. Eq.(7) therefore compares the output on BF directly to tau_B tensor rho_F; the free rotations of unused/spent A disappear when A is discarded. F is untouched. At T+delta, this complete-reference renewal error is at most(8).

This realizes the K2235 full-exchange renewal autonomously during a finite observation window with N fresh Gibbs qubits, N retained bank qubits, and clock dimension N+R+1. It does not autonomously implement K2229's record gap ramps, unknown intervening detector operations or arbitrary adaptive cycles. It removes the per-collision switching assumption for this renewal stage only. All Gibbs supply, equal gaps, couplings and initial clock localization remain imported.

For N=1701 choose R=8, M=1709, d_C=1710. Then T=pi/(2g), peak link855g, controller bandwidth3418g, initial controller mean1709g and variance1709g². A timing interval |g delta|<=1/1000 gives

 epsilon_clock<=C(1709,9)/10^54 < 4*10^-31.          (10)

The exact rational arithmetic should be checked by the probe; this is a conservative reporting decimal. Resource stock is1701 fresh ancillas per renewal, unchanged from K2235 full exchange. Clock dimension does not replace bath entropy capacity. At exact completion, ancillary mean heat is Q_A=sum E_j(a_j-p_j) and the joint finite-environment entropy identity of K2235 remains valid. No first-cycle reset work can be recycled as a later-cycle bound.

A compact explicit fixture uses N=L=2,R=2,M=4. Clock off-diagonals are (2,sqrt6,sqrt6,2)g; H_P spectrum is(0,2,4,6,8)g. The failure probability is

 epsilon<=4r³-3r⁴, r=sin²(g delta),                   (11)

because completion means k>=2. At r=1/100 this is397/100000000; if |g delta|<=1/100, it is<=4*10^-12. Take Gibbs populations p1=1/4,p2=1/3, represented by gaps beta E1=log3,beta E2=log2; all declared gaps are nonnegative. At T both arbitrary reference-correlated bank cells are replaced by their respective Gibbs states. Exact qubit Kraus/matrix-unit tests can check this without numerical logarithms.

## 5. Strongest failure modes and scope ceiling

1. There is no autonomous permanent halt. At2T=pi/g the clock returns to0 and every prefix gate is undone, up to free H_D evolution and scalar phase. The finite model is reversible and recurrent. Continued evolution returns bank information from spent ancillas. The finite output window/readout remains a resource boundary.
2. The clock is pure and decoupled at completion but is |M>, not the initial |0>. Merely waiting recycles the clock by undoing the data circuit. A separate clock reset without undoing data is not supplied. Resetting after tracing/discarding ancillas is an additional operation.
3. H_P includes nontrivial clock-data interaction. Calling gM bare-clock work, battery consumption or minimal cost is unsupported. Conserved energy budget is not a thermodynamic cost. The positive scalar shift fixes a nonnegative total convention; spectral bandwidth/variance are less shift-dependent resources.
4. The constant interactions are not switched off at the endpoint. Their expectation on the endpoint state is zero but their operator action is nonzero. Exact factorization at one time is not dynamical isolation.
5. Noncommuting U_j,H_D break Eq.(2) and the simple free-factorization/energy account. A thermal unequal-gap mutation must detect this. Extending the compiler to gap ramps needs a clock-dependent energy landscape and a battery or additional resource model, not the present proof.
6. Product Gibbs marginals without full independence are insufficient for replacement. K2235's correlated counterexample remains applicable. The compiled unitary can act on any correlated D input, but its renewal interpretation has the fresh-stock premise.
7. Clock error is for a discarded clock and for the same elapsed-time free evolution. A fixed-time target for general nonstationary data requires a further drift error <=|delta| ||H_D|| modulo scalars; the Gibbs-bank target is stationary and needs none.
8. Mutations of clock coupling weights, gate orientation, positive scalar shift and resonance are four genuine input faults. Joint-clock error, padding resource cost and return at2T are separate unconditional countercontrols, not additional mutation credit.

No theorem here supplies GU action closure, physical-state selection, laboratory implementability, spatial signal propagation, indefinitely renewable reservoir or external-expert/proof-assistant certification. A finite exact probe exercises algebra and rational resource arithmetic; the arbitrary-M, arbitrary-reference and tail statements have the direct proofs above.


## 6. Exact autonomous halting is excluded in this finite channel class

This is a second, broader statement than the explicit2T reversal. Let S and E be finite, let sigma_E be fixed independent input, let H be any time-independent finite Hermitian matrix, and define

 Phi_t(X)=Tr_E[e^-itH (X tensor sigma_E)e^itH].

Every matrix entry of Phi_t is a finite linear combination of exponentials exp[-it(E_a-E_b)], hence is real-analytic on the whole real line (indeed entire after complexification of the scalar parameter). If Phi_t equals a fixed channel Lambda on any nonempty open real interval, each coefficient of Phi_t-Lambda vanishes identically by the analytic identity theorem. Evaluating at0 forces Lambda=Phi_0=id_S. Consequently a fixed nonidentity replacement/reset channel cannot hold exactly over an open interval in ANY such closed finite autonomous model. Correlated final states and an arbitrarily large but finite fixed environment do not change this proof.

The theorem concerns equality as a channel on all inputs, fixed environment and one fixed retained output subsystem. It does not exclude approximate padded windows, exact completion at isolated times, a state-specific stationary output, time-dependent control, an infinite apparatus, changing the output subsystem or a genuine externally performed measurement/extraction. For a target with prescribed free drift one may pass to its specified interaction picture only if that transformation and its analytic time dependence are explicitly included; the stationary Gibbs-replacement target used here is already fixed. The theorem gives no lower bound on approximation error, since the padding construction can make finite windows arbitrarily accurate with growing resources.

The exact probe checks229 finite controls and detects four input/equation mutation families, with three additional unconditional countercontrols. These totals do not certify the universal analytic statements.


## Reproduction and independent review

Independent internal specialist review checked the gauge identity, equal-gap/reference renewal, discarded-clock error, resource accounting and analytic no-plateau proof. Its initialization correction is incorporated: a small clock marginal error alone is insufficient. No blocking mathematical finding remains. Run `python tests/channel-swings/k2238_finite_clock_thermal_circuit_probe.py`; the default repeats finite controls and four actual-input fault tests and rejects stale note/probe/dependency hashes. `--write` refreshes its certificate. Finite controls and reporting arithmetic remain distinct from universal written proofs.
