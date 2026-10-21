---
title: "K1916: Exact bath preparation resources and finite-rate limits"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied conditional models only; no native GU, novelty, total work or formal proof
scripts:
  - tests/channel-swings/k1916_bath_preparation_resource_limits.py
  - tests/channel-swings/k1916_bath_preparation_resource_limits_probe.py
---

# K1916: Exact bath preparation resources and finite-rate limits

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
result: optimal rank-constrained free energy and distance, plus finite-rate cooling and channel-error bounds
carrier: finite bath for supplied extreme rank-k correlation channel LAYER=toy CHIRALITY=N/A
pairing: positive complex Hilbert trace pairing ON=finite_bath_density_matrices
real_structure: ordinary adjoint and positive density operators; native K/C not identified
grading: bath energy levels and system populations only
action_owner: repository-construction -- arbitrary endpoint unitary and explicitly specified preparation dynamics
target: exact support preparation and approximate channel implementation MAP-TYPE=intertwiner
```

## 1. Price the missing preparation, without changing the fixed-bath question

[K1912](k1912-faithful-bath-dephasing-boundary-2026-10-21.md) proves that an
extreme correlation channel C of rank k can be realized with a d-dimensional
product bath in state rho exactly iff k rank(rho)<=d, allowing arbitrary joint
unitaries. This note prices changing the bath preparation. It does NOT solve
the global channel-distance optimum when the original faithful bath state
must remain unchanged.

Let beta>0, H have eigenvalues E1<=...<=Ed, tau=exp(-beta H)/Z, and
s=floor(d/k). If d<k exact realization is impossible even from a pure bath.
Otherwise let Z_s=sum_(i<=s)exp(-beta Ei), p_s=Z_s/Z. Among ALL density
matrices allowing exact realization, including noncommuting preparations,

    min D(rho||tau)=-log p_s,
    min [F_beta(rho)-F_beta(tau)]=-log(p_s)/beta,          (1)
    min (1/2)||rho-tau||_1=1-p_s,                        (2)

where F_beta(rho)=Tr(H rho)-S(rho)/beta. Both minima are attained by

    rho_s=P_s tau P_s/p_s,                               (3)

where P_s selects the s lowest-energy levels (any suitable subspace in a
boundary degeneracy). These are exact state-resource optima. A finite
free-energy difference is not a finite-time or single-shot work protocol.

## 2. Proof and actual realizing bath

For fixed eigenvalues r1>=...>=rd, energy is minimized by aligning them
against increasing Ei. Indeed the diagonal probabilities in the energy
basis are a doubly stochastic mixture of the r_i; the rearrangement
inequality minimizes the resulting linear energy. Entropy is basis invariant.
Rank at most s therefore reduces the free-energy problem to probabilities
on the first s energies, allowing zeros. With q_i=exp(-beta Ei)/Z_s,

    F_beta(r)=-log Z_s/beta+D(r||q)/beta.

Relative entropy is nonnegative, with equality at r=q. Using
F_beta(tau)=-log Z/beta proves(1). This proves the global orientation
optimization; it does not assume rho commutes with H at the start.

For(2), if P is the support of rho, rank P<=s, the two-outcome measurement
(P,I-P) gives trace distance at least1-Tr(P tau)>=1-p_s by the variational
principle for the sum of the largest s eigenvalues. State(3) has excess
positive mass1-p_s on P_s and negative mass of that size off it, giving
equality. The minimizing support is thus the same for both costs.

An exact dilation is supplied by K1912's constructive sufficiency: write
C_jk=<e_k,e_j> in C^k, isometrically embed C^k tensor supp(rho_s) into C^d,
and map psi to e_j tensor psi on that support. Each isometry extends to a
unitary U_j. The support dimension ks<=d is precisely what permits this.
No energy-conservation restriction is placed on the endpoint U_j. Preparation
free energy and interaction/transport/reset costs remain distinct.

For a flat bath H=0, p_s=s/d, so the dimensionless cost is log(d/s), not
zero merely because a mixed support is possible. For k=2 and even d it is
log2; enlarging a flat finite bath does not remove it. For a qubit with gap
Delta and k=2, the optimum is the ground state, with dimensionless cost
log(1+exp(-beta Delta)) and trace distance q=1/(1+exp(beta Delta)).
At beta=0 only the relative-entropy statement is retained, as log(d/s);
we do not divide by zero or assign a finite-temperature free energy there.

## 3. Released approximation construction with the ORIGINAL Gibbs state

Use the same U_j designed for rho_s, but supply tau instead. Since

    tau=p_s rho_s+(1-p_s) tau_tail,

the resulting channel is p_s Phi_C+(1-p_s) Phi_tail. Hence

    half-diamond error <=1-p_s.                         (4)

This is a general constructive upper bound for the unchanged Gibbs bath,
not proof that the bound is globally optimal. It complements K1913's
lower bound for its particular four-mode target. For the qubit, (4) is q;
for a flat large bath it approaches1-1/k. A different channel unitary can
have a smaller error without contradicting the exact-preparation optimum.
The endpoint construction may have arbitrary interaction energy and is not
identified with a thermal operation.

## 4. Static finite cost versus bounded-rate preparation

Now specify a preparation model on the SAME finite bath:

    d rho/dt=-i[H_t,rho]+sum_a(L_a rho L_a* -{L_a*L_a,rho}/2).

Assume coefficients are piecewise continuous with a well-defined propagator
and G_t=sum_a L_a*L_a has finite integrated norm
Gamma(t)=integral_0^t ||G_v||dv. Starting from faithful rho0,

    lambda_min(rho_t)>=lambda_min(rho0) exp(-Gamma(t))>0. (5)

Proof: let K solve K'=(-iH_t-G_t/2)K, K(0)=I. The finite-dimensional
variation-of-constants expansion of the completely positive dynamics has
positive jump terms, so rho_t>=K rho0 K*. For y=Kx,
(d/dt)||y||^2=-<y,G_t y>>=-||G_t||||y||^2. Gronwall gives
sigma_min(K)>=exp(-Gamma/2). This proves(5). Hamiltonian rotations do not
improve this bound; their contribution cancels in the norm derivative.
The inequality depends on a supplied Lindblad representation and integrated
rate; no representation-invariant rate optimum is asserted.

Thus finite Gamma cannot reach the rank-deficient exact minimizer(3), nor
any state realizing an extreme k>1 endpoint exactly. This is a restricted,
explicit dynamical statement, not an exclusion of postselection, a swap
with an already pure ancillary system, singular rates or infinite reservoirs.
A no-jump branch with nonzero weight is the mechanism retaining full rank.

More generally eigenvalue min-max applied to K rho0 K* gives
lambda_i(rho_t)>=exp(-Gamma) lambda_i(rho0) for each decreasingly ordered
eigenvalue. Consequently distance to EVERY rank<=s state obeys

    half trace distance >= exp(-Gamma) sum_(i>s) lambda_i(rho0). (6)

The proof uses the variational support measurement as in(2); it is a
necessary approximation bound, not a claim that one process attains every
spectrum simultaneously. For a qubit initially diag(1-q,q), q<=1/2,
amplitude damping with L=sqrt(gamma)|0><1| gives diag(1-qe^-gamma t,
q e^-gamma t), Gamma=gamma t, and saturates(5)-(6) for s=1. This is an
explicit optimal decay example within the stated integrated-rate bound.

## 5. Released full-channel resource consumer

For K1913's four-mode target define delta=6-4sqrt2 and h=4+sqrt2. Compose
its arbitrary-joint-unitary error bound with(5), after preparation ends:

    epsilon := half-diamond error
       >= d lambda_min(rho0) exp(-Gamma) delta/(16h).    (7)

The endpoint interaction need not preserve populations exactly. If rho0 is
Gibbs of bandwidth Delta at beta, d lambda_min(rho0)>=exp(-beta Delta), so

    epsilon >= exp(-beta Delta-Gamma) delta/(16h).       (8)

If epsilon0<delta/(16h), a necessary combined resource inequality is
beta Delta+Gamma>=log[delta/(16h epsilon0)]. With ||G_t||<=g_max>0 this
gives a preparation-time lower bound whenever its right side exceeds beta
Delta. This is not a total-work bound or sharp channel-distance constant.

For a thermal qubit, amplitude damping followed by the ground-state-designed
unitaries has constructive half-diamond error<=q exp(-gamma t), by the same
mixture argument as(4). Thus this class has matching exponential RATE but
not matching lower/upper channel constants. The finite free-energy endpoint
cost(1) and divergent exact-preparation time are compatible facts.

## 6. Released collective-preparation advantage

Extremality survives tensor products of extreme correlation matrices. If the
rank-one Gram projectors of C span Herm(k), their N-fold tensor products span
Herm(k^N): tensor products of real Hermitian bases give a real Hermitian basis
on the tensor space. This is the usual extremality criterion and proves the
hypothesis needed to apply K1912 to C^(tensor N), whose rank is k^N.

For N uses with a collective bath of dimension d^N, the exact maximum allowed
support rank is s_N=floor((d/k)^N). With a flat initial bath, (1) gives

    minimum relative entropy = log(d^N/s_N).             (9)

If d>k, this equals N log k plus a nonnegative rounding correction that tends
to zero. A separate preparation of each d-dimensional cell instead costs
N log[d/floor(d/k)]. These can differ extensively when d/k is not an integer.
For two rank-two target channels and two flat qutrit cells, d^N=9,k^N=4,
s_N=2. A collective rank-two preparation costs log(9/2), versus log9 for
separately pure cells: an exact log2 saving in dimensionless free energy.
The isometry construction uses only8 of the9 bath dimensions and realizes
both target channels together. This is a global controlled unitary on the
combined bath; it does not impose independent interactions, local preparation,
or fixed per-cell circuitry. Those restrictions can remove the advantage.

For an actual product Gibbs spectrum, replace the flat spectral fraction by
the sum of the largest s_N joint Gibbs eigenvalues. The theorem still gives
the exact preparation resource, but determining that spectral sum is a
separate combinatorial/large-deviation problem. No asymptotic work extraction
or finite-rate reset protocol is inferred. Equation(5) still forbids exact
rank reduction by finite integrated-rate preparation on the combined finite
bath. Thus collective resource compression does not evade the dynamical limit.

## 7. Hostile review, prior art and evidence

Strongest overclaim: work equality, universal third law, exact thermal-channel
optimizer, or bath energy conservation. None is asserted. Strongest contrary
models: pure ancilla swaps and measurement/postselection remove hypotheses;
faithful nonclassical approximants in K1912 remain possible. Degenerate energy
levels do not force a unique minimizer. Weakest seam: a noncommuting support
cannot be priced by simply renormalizing P tau P without optimization; the
rearrangement proof is what closes that seam. No-jump positivity is used on
the density operator, not an unjustified eigenbasis ODE.

The Gibbs variational principle and spectral rearrangement are established
methods, specialized here to K1912's exact support requirement. [Reeb and
Wolf](https://arxiv.org/abs/1306.4352) study Landauer costs with explicit
reservoir assumptions; [Masanes and Oppenheim](https://arxiv.org/abs/1412.3828)
and [Freitas et al.](https://arxiv.org/abs/1911.06377) discuss unattainability
and its resource assumptions. Those results provide context, not a claim
that(1) is a realizable work protocol or(5) their most general theorem.
The proof here is self-contained for the finite regular GKSL model.
Exact controls test sorting, support, mixture, damping and resource constants;
separate probes test matrices and actual corrupted inputs. General statements
rest on the arguments, not enumeration of a few states or manifest checks.


## Source and acceptance boundary

SC-OP-04 ASSERTS candidate four-field operator grammar; SC-MAS-01 and
SC-CHI-02 ASSERT a stylized curvature-mass toy; SC-META-53 remains UNCERTAIN
about indefinite spectra. None selects the positive Hilbert pairing, bath,
scalar drive, observable algebra or physical units here. LT-SM8, LT-GR6b
and AC-F1 remain unchanged. Full20 injection, separate K/C, physical domain
and accessible-algebra identification remain independent construction debts.
No source-register, physics-ledger or canon verdict changes. No GU prediction,
novelty, external expert acceptance or formal proof is claimed. Analytic
arguments carry general scope; exact finite probes test the actual algebra
and countercontrols. Report and dependency-pin checks establish only
consistency and provenance, separately from mathematical-input faults.
