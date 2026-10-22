---
title: "K1926: Quantified approximate catalyst return"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied finite positive Hilbert models; no native GU, novelty, total work or formal proof
scripts:
  - tests/channel-swings/k1926_approximate_catalyst_return_bound.py
  - tests/channel-swings/k1926_approximate_catalyst_return_bound_probe.py
---

# K1926: Quantified approximate catalyst return

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
result: full-channel error versus finite catalyst return and spectral separation
carrier: four-level target and finite thermal-bath plus faithful catalyst LAYER=toy CHIRALITY=N/A
pairing: state-weighted Hilbert-Schmidt norm and normalized Choi trace ON=finite_product_dilation
real_structure: complex adjoint and density-matrix spectral projections
grading: system population labels and state eigenspaces; not energy shells
action_owner: repository-construction -- arbitrary joint unitary, then exact additive conservation for the return consumer
target: necessary error/disturbance bounds with arbitrary population leakage MAP-TYPE=intertwiner
```

## 1. State disturbance replaces an exact catalytic assumption

Use K1924's four-level target and constants
delta=6-4sqrt2, h=4+sqrt2, a=delta/(4h), c0=a/4.
Let Omega be ANY faithful state on a finite environment and U any joint
unitary. Let Phi be its system channel and epsilon=(1/2)||Phi-Phi_C||_diamond.
Define gamma=I4/4 tensor Omega and

    R=D(U gamma U* || gamma).

If Omega has at least two distinct eigenvalues p,q>0, define the dimensionless
RELATIVE spectral separation

    kappa=min_(p!=q) (sqrt(p)-sqrt(q))^2/q > 0.          (1)

Both ordered pairs are included. This is a density-spectrum separation,
not a Hamiltonian energy gap, a smallest eigenvalue or a dimension alone.
Then

    epsilon >= f(R/kappa),
    f(x)=max(a-x,0)^2/(4a).                             (2)

If Omega is scalar there is a single state eigenspace and epsilon>=c0
directly; no division by an empty gap is made. Equation(2) is necessary,
not sharp or sufficient, and may become weak for dense spectra.

## 2. Proof with arbitrary population leakage

Let A_j=U_jj, E the pinching onto Omega's eigenspaces and D_j=E(A_j).
Set ell_j=1-Tr(Omega A_j* A_j),
q_j=||(A_j-D_j)sqrt(Omega)||_F^2, Q=sum q_j/4.
The proof of K1924 uses only that the reference state is scalar on each
pinching block, not that those blocks are energy eigenspaces. Weighted
orthogonality, shellwise polar extension and the K1912 tracial residual give

    sqrt(t)+sqrt(pbar+Q)>=sqrt(a),
    t,pbar<=epsilon, hence epsilon>=f(Q).               (3)

Here t is normalized Choi half trace distance and pbar=sum ell_j/4.
These bounds allow arbitrary population mixing. D_j are contractions; their
polar parts extend to unitaries INSIDE each state eigenspace. No tracial
argument is applied directly to a general nonuniform state.

In a joint eigenbasis of gamma, let g_b be its eigenvalues. Define two
normalized classical distributions on ordered pairs of basis states:

    P_ab=|U_ab|^2 g_b, Q_ab=|U_ab|^2 g_a.

Unitary row/column sums normalize both. Direct expansion gives
D(P||Q)=R. Jensen and -log x>=1-x yield

    R >= -2 log(sum sqrt(P_ab Q_ab))
      >= sum (sqrt(P_ab)-sqrt(Q_ab))^2
       = ||U sqrt(gamma)-sqrt(gamma)U||_F^2.            (4)

Zero matrix entries contribute0; faithfulness avoids unsupported likelihoods.
The diagonal-system terms alone in the last norm are
(1/4)sum_j ||A_j sqrt(Omega)-sqrt(Omega)A_j||_F^2.
Every off-state-eigenspace matrix entry contributes at least kappa times
its Omega-weighted squared magnitude by(1). Thus kappa Q<=R.
Since f is decreasing, (3) proves(2). This argument uses relative entropy
itself, not a twice-weakened Pinsker/square-root estimate.

## 3. Thermal bath and approximate average catalyst return

Take Omega=tau_B tensor sigma_A, with sigma_A faithful, tau_B Gibbs at
beta>0. Require exact additive conservation of H_S+H_B+H_A; H_S is diagonal
in the target basis. Let s',sigma' be the output system/apparatus marginals
for input I4/4. Define

    G_A=beta H_A+log sigma_A,
    r=(1/2)||sigma'-sigma_A||_1,
    W=bandwidth(H_S), Z=largest_eigenvalue(G_A)-smallest_eigenvalue(G_A).

Entropy invariance of U gamma U* and expansion of log gamma give the EXACT
identity, even when [sigma_A,H_A]!=0,

    R=-beta Tr[H_S(s'-I4/4)]-Tr[G_A(sigma'-sigma_A)].    (5)

The system channel is epsilon-close to the unital target, hence
(1/2)||s'-I4/4||_1<=epsilon. The centered-observable trace bound proves

    0<=R<=beta W epsilon+Z r.                           (6)

Combining(2) and(6), for epsilon<c0 necessarily

    beta W epsilon+Z r >= kappa(a-2sqrt(a epsilon)).     (7)

If Z>0 this gives an explicit minimum return disturbance, with negative
right sides replaced by0 after subtracting beta W epsilon. When Z=0 the
equation constrains error/energy alone; no zero division is used. Sigma
thermal at the same beta makes G scalar, consistent with the original
thermal obstruction. Kappa is computed from the WHOLE Omega, not sigma alone.

For exact average return r=0, put nu=beta W/kappa. Solving the quadratic
in sqrt(epsilon/a) gives the positive bound

    epsilon >= a/(1+sqrt(1+nu))^2.                      (8)

When W=0 it is c0. For a genuinely unital realized Phi, Delta E_S=0 and
exact average return implies R=0, so the stronger c0 follows even for W>0.
Return on other inputs or absence of output correlations was not assumed.

## 4. Released exact-return theorem without faithfulness

Suppose sigma_A may be rank deficient, but Phi is UNITAL and sigma'=sigma_A
on input I4/4. Exact conservation fixes the average bath energy. Initially
the entropy is log4+S(tau_B)+S(sigma_A). Finally subadditivity and Gibbs
maximum entropy at that bath energy bound it by the same quantity. Equality
forces the FINAL JOINT state to be exactly gamma: both mutual information
terms vanish and the bath equals tau_B. Therefore U gamma U*=gamma.

On supp(Omega), each system block commutes with Omega, which is faithful
there. Spectral-block polar extensions and (3) with Q=0 give epsilon>=c0.
This includes arbitrary coherent/rank-deficient finite catalysts, arbitrary
population leakage and correlations for OTHER inputs. The exact target is
unital, so it cannot be catalyzed. This specializes established catalytic
factorization restrictions; it is not a novel general classification.
For nonunital approximate channels with nonfaithful sigma, (8) is NOT asserted.

## 5. Countercontrols, scale and scope

For Omega=diag(4/5,1/5), kappa=1/4. A rational qubit rotation with sine4/5
in one of four controlled blocks has Q=4/25, square-root commutator norm
8/125, and R=12 log4/125; these explicitly satisfy kappa Q<=commutator norm<=R.
The first inequality is not equality: the two transition directions have
different relative weights. Rotating a degenerate block has Q=R=0 despite
being a nontrivial matrix. As distinct eigenvalues coalesce, kappa->0;
at exact degeneracy the pinching changes. Do not claim a uniform estimate
from the discontinuous exact-return theorem.

The probes reconstruct actual matrices, noncontrolled mixing, transition
distributions and conservation/entropy identities. Numerical logarithmic
examples are illustrations; exact algebra and the analytic inequalities
carry the theorem. Mathematical input faults (state weighting and logarithm
orientation) are separate from report/digest faults. Faithfulness is needed
for the approximate R/G formula; section4 handles exact rank-deficient return
by a different proof. No minimum-work or approximate extreme-rank theorem,
optimal protocol, unrestricted infinite catalyst or source-native claim.

Prior art: [Lie and Jeong](https://arxiv.org/abs/2104.00300) establishes that
catalytic channels are factorizable; [their earlier work](https://arxiv.org/abs/2010.14795)
relates information leakage and catalytic randomness. The present proof
reuses K1912/K1913/K1924's target witness and supplies explicit state-spectrum
and return-error constants. No novelty or exhaustive literature claim.

## Source and acceptance boundary

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 is UNCERTAIN about
the southeast rival; SC-MAS-01 and SC-CHI-02 ASSERT a stylized mass toy;
SC-META-53 remains UNCERTAIN about indefinite spectra. None selects this
positive Hilbert channel, bath, catalyst, energy or units. LT-SM8, LT-GR6b
and AC-F1 remain unchanged. The same-background full20 paired injection,
separate K/C, domain and accessible algebra remain construction obligations.
No source-register, physics-ledger or canon verdict changes. Analytic proofs
carry universal scope; exact finite controls, numerical illustrations and
report/pin checks are distinguished. No novelty, external expert acceptance,
native GU prediction, infinite-reservoir or formal-proof claim.
