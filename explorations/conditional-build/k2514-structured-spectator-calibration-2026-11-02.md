---
title: "K2514 Spectator-complete layered calibration and sharp angular pooling"
status: active_research
doc_type: exploration
created: "2026-11-02"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional finite-Hilbert circuit-class certificate; trusted class membership and gate access; no apparatus or GU certification"
---

# K2514 Spectator-complete layered calibration and sharp angular pooling

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
result: K2514
carrier: original C108 Q/T verifier times retained qutrit with supported memory dimension2 LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace ON=declared_carrier
real_structure: complex adjoint; arbitrary complex U2 block phases
grading: declared common-eigenvector pairs and memory support; global Q/T do not commute
action_owner: repository-construction -- supplied layered gate class and trusted primitive access
target: uniform supported effect and leakage certification from spectator-complete primitive tests MAP-TYPE=evaluation
```

## Result and scope

A declared layered error class can be certified without assuming a small full-carrier operator-norm perturbation. Every possible active spectator plane in that class receives a test. Arbitrary complex phases and noncommuting layers are allowed. A sharp angular composition theorem gives the complete-gap effect bound. An exact minimax pooled design certifies its sum-of-angles condition with fewer zero-count samples than separately certifying each layer. The minimax statement concerns this specified labeled-test/angular-envelope design, not all quantum experiments or the exact final-effect acceptance region.

This extends K2512's one-plane circuit and K2504's generic sector tests; their statistical confidence and complete-record theorems are reused. Source SC-META-53 remains UNCERTAIN, LT-SM8/LT-GR6b retain physical quotient/domain debts, and ledger0.263 is unchanged. Positive Hilbert space, fixed circuit membership, trusted complete preparation/readout and primitive access are premises. No measured apparatus, novelty, external-expert or proof-assistant certification is claimed.

## 1. Class and accessible tests

The original Q,T on H=C108 do **not** globally commute: K2484 retains their nontrivial two-dimensional principal-angle block. For each layer j=1,...,L, specify m_j>=1 mutually orthogonal two-dimensional planes span(a_jk,b_jk), whose endpoints are known common eigenvectors of Q,T and have different eigenvalue pairs. Different layers may use different pairings and need not commute. Choose one R_jk in {Q,T} whose eigenlabels differ. Nothing requires a common eigenbasis on all H.

Let U_j be the direct sum of arbitrary unknown U(2) matrices on those planes and a unitary on the orthogonal complement that commutes with both restricted Q and T. In particular the original noncommuting principal-angle block can be left exactly unchanged. The complement is reducing for both Q,T because each chosen endpoint is their eigenvector. This class promise rules out unknown couplings between listed planes or into the complement; tests below do not establish the promise.

Use K2512's full retained qutrit E, E0=span(e0,e1), S=I_H tensor P_E0. The controlled primitive is

C_j=I_H tensor |0><0| + U_j tensor |1><1| + Z_j tensor |2><2|,

where each Z_j is any unitary: dangerous outside-support behavior is retained. Let B act as identity on e0 and as any unknown U(2) on span(e1,e2), and let W be any memory-only unitary preserving E0 and its complement. The full gap is

V=(I_H tensor W)(I_H tensor B) C_L ... C_1.

No memory reset is inserted between deployment gaps. Calibration can isolate each C_j and B with all other primitives bypassed; their parameters/class must be the same as, or uniformly cover, deployed primitives. Isolation, absence of a setting side channel and gate-composition fidelity are separately trusted access premises. All hidden reusable registers must already be included; this class has no additional retained register.

For each pair prepare a_jk tensor e1 using the full reset/preparation from K2512, apply isolated C_j and read R_jk's opposite eigenlabel. If

p_jk=|<b_jk,U_j a_jk>|^2,

this is exactly the wrong-event probability. A 2 by 2 unitary has equal offdiagonal entry magnitudes. Thus testing one endpoint covers its reverse transfer, including all complex phases. Read only this one chosen projector; there is no unlicensed global joint Q/T measurement. For B, prepare any known H vector tensor e1, apply B, and read I-S. Its mean p_B is exactly |<e2,B e1>|^2.

## 2. Whole-carrier effect and leakage theorem

For a rank-one coordinate projector P on one active plane, direct 2 by 2 multiplication gives

(U* P U-P)^2=p I_2.

If Q or T has equal labels on that plane, its difference is zero. Hence for each R=Q,T,

||U_j* R U_j-R|| <= a_j := max_k sqrt(p_jk),
theta_j := arcsin(a_j) in[0,pi/2].

These are norms on the entire H, not only the prepared state. Complement phases or arbitrary complement unitaries commuting with Q,T cost nothing at this step. They may change later states, but subsequent layers still obey the same full-H bounds.

For projections P,P' of equal rank the maximum principal angle is arcsin||P-P'||. One can see the bound without assuming a simultaneous basis for multiple projections: the CS decomposition of two equal-rank subspaces reduces them into common directions and 2D angle blocks, where the difference has eigenvalues plus/minus sin(theta). The maximal angle obeys the triangle inequality, capped at pi/2. Indeed choose unit nearest vectors successively in the two intermediate subspaces. For unit vectors with nonnegative real overlaps cos(alpha),cos(beta), Cauchy--Schwarz on their components perpendicular to the intermediate vector gives real overlap at least cos(alpha)cos(beta)-sin(alpha)sin(beta)=cos(alpha+beta), when alpha+beta<=pi/2. Taking worst vectors gives the stated subspace bound.

Applying this to the successive conjugates of R yields

|| (U_L ... U_1)* R (U_L ... U_1)-R ||
  <= sin(min(pi/2, sum_j theta_j)).                       (1)

Equivalently apply the triangle inequality to a vector's angle to Ran(R) after each U_j; both forward and reverse subspace gaps are bounded. Unitary conjugation does not change a projection gap. Arbitrary phases and overlapping pairings therefore do not invalidate (1). Aligned same-plane real rotations with nonnegative angles and total at most pi/2 attain equality, so a maximum or root-sum-square replacement is false.

Memory-only B,W commute with Qbar,Tbar. Consequently the full compressed effect equals R on memory0 and (U_L...U_1)* R (U_L...U_1) on memory1. Its norm error obeys (1). Since W preserves S and C_j preserve each memory label,

S V*(I-S)V S=p_B I_H tensor |1><1|,
ell=p_B.                                                 (2)

Thus a sum-of-angles certificate plus p_B<=b supplies epsilon<=sin(A),ell<=b. These operator statements remain true after tensoring any untouched reference and for historywise classical mixtures of covered complete gaps. The original complete-record theorem applies provided every actual and proof-hybrid gap is covered and its other unchanged initial-support/instrument premises hold. Calibration alone never proves temporal coverage. A calibration average over hidden changing gates does not certify each constituent: every deployed conditional primitive must satisfy the stated bounds, or its exact conditional channel must be controlled by another applicable theorem. The convex extension here means mixtures of already covered complete gaps, not an inference from an average marginal test.

## 3. Exact pooled angular-envelope design

Fix 0<A<=pi/4. Define the unique tau>0 by

sum_j arcsin(sqrt(m_j tau))=A.                            (3)

Existence and uniqueness follow from strict monotonicity: at tau=0 the sum is0, while at tau=min_j 1/m_j at least one term reachespi/2>A. Set t_j=arcsin sqrt(m_j tau), and

w_j = [1/sin(2t_j)] / sum_i [m_i/sin(2t_i)].              (4)

Each individual pair in layer j receives probability w_j, so sum_j m_j w_j=1. Let mu_E=sum_jk w_j p_jk be the pooled effect-test wrong mean.

**Theorem.** If sum_j max_k arcsin sqrt(p_jk)>A, then mu_E>tau. Therefore mu_E<=tau certifies the full angle budget, and hence epsilon<=sin(A).

Proof. Put x_j=max_k arcsin sqrt(p_jk). Positivity gives mu_E>=sum_j w_j sin²(x_j). If sum x_j>=A, reduce coordinates to y_j in[0,x_j] with sum y_j=A. Every y_j<=A<=pi/4, where sin²(y) is convex, strictly so away from the endpoint. Its first derivative is sin(2y). At t_j the quantities w_j sin(2t_j) are identical by(4). The supporting-line inequality thus gives

sum_j w_j sin²(y_j) >=sum_j w_j sin²(t_j)
  =tau sum_j m_j w_j=tau.

If sum x_j>A, some coordinate was reduced through a positive interval and sin² is strictly increasing, proving strictness. This proof remains valid when some original x_j exceedpi/4: reduction occurs before using convexity.

**Restricted minimax sharpness.** Consider any fixed positive label probabilities q_jk summing to1. In each layer choose a least-weight plane k_j and set only its p_jk=m_j tau, all others zero. The angle sum is A, while

mu_E=tau sum_j m_j min_k q_jk <=tau.

A common slight increase of the nonzero angles makes the angle sum>A and approaches that boundary mean. Thus no such label distribution has an infimum wrong mean greater than tau over failures of the angular-envelope condition. Design(4) attains tau, exactly. These probabilities are realized by independent U(2) rotations in the declared class. The actual final effect can cancel or be smaller if their planes do not align; that is why this is an angular-envelope minimax theorem, not a universal lower bound for testing final epsilon. For equal multiplicities m, aligned common planes are also physical final-effect sharpness fixtures for the uniform design.

For all m_j=m, symmetry gives t_j=A/L, tau=sin²(A/L)/m, and w_j=1/(Lm). Therefore the effective inverse threshold is

W_E=1/tau=m csc²(A/L).                                  (5)

Separately requiring every layer angle<=A/L and using scalar pooled domination would cost Lm csc²(A/L), a factor L larger. The improvement follows from certifying the sum directly, not from dropping a spectator test or assuming error independence. Unequal m_j have the exact implicit design(3)-(4), not an unproved equal-allocation rule.

## 4. Leakage, confidence, preparation bias and drift

For leakage allowance 0<b<1, mix the effect design and the leakage test with

W=1/tau+1/b,
q_E=(1/tau)/W=b/(b+tau), q_B=(1/b)/W=tau/(b+tau).

The overall wrong mean is mu=q_E mu_E+q_B p_B. If mu<=1/W, then mu_E<=tau and p_B<=b, so the two desired conclusions hold. These outer mixing weights maximize min(q_E tau,q_B b), and that maximum is1/W. This is again the specified pooled certificate, not all experimental strategies.

Use K2504's private-label fresh-reset binomial upper bound U at confidence failure alpha for one frozen collection of primitive maps. Each label selects its declared fixed primitive and input/readout; independent fresh trials then have the displayed pooled Bernoulli mean. Gate selection is a declared control, not a license for the same primitive to behave differently in calibration and deployment. With independently justified weighted preparation/readout probability bias xi_eff, require

U+xi_eff<=1/W.

For G predeclared classes use alpha/G. With zero wrong counts and v=1/W-xi_eff>0, n>=ceil(log(G/alpha)/[-log(1-v)]) suffices. At zero bias this threshold is sharp for the chosen protocol and the rule accepting every all-zero transcript: leakage-only unitaries with p_B down to b from above have wrong mean down to1/W and all-zero probability(1-1/W)^n. This is inherited zero-count logic with a new physically derived effect threshold. Keep label-resolved counts; pooled acceptance is sufficient and may reject maps with a good final effect.

For deployment allow every layer's maximum angle to increase by at most h_j compared with its calibrated center, uniformly over every actual/hybrid history, and let B's leakage angle increase by at most h_B. These are explicit angle-coverage promises, not a trusted full-carrier norm bound. They can arise from a separately justified parameter model; samples at one center do not prove them. Then

epsilon_D<=sin(min(pi/2,A+sum h_j)),
ell_D<=sin²(min(pi/2,arcsin sqrt(b)+h_B)).                 (6)

Arbitrary complex phases, W and commuting-complement unitaries may vary historywise without changing the per-layer angle bounds. Arbitrary coherent control by an additional unmodeled register is excluded, not silently treated as a classical mixture.

### Concrete two-layer, two-plane consumer

Take L=m=2, s=1/4000000, A=2arcsin(s), tau=s²/2=1/32000000000000 and b=1/4000000. The exact A obeys A<pi/4. Set h_1=h_2=1/4000000 and h_B=1/2000. Since sin(A)=2s sqrt(1-s²)<=1/2000000 and sin(A+D)<=sin A+D for D>=0 while A+D<pi/2, equation(6) gives epsilon_D<=10^-6. Also |sin(beta+h_B)|<=|sin beta|+h_B gives sqrt(ell_D)<=1/2000+1/2000=1/1000. Hence ell_D<=10^-6.

W=32,000,004,000,000. At zero bias, G=1, alpha=1/100, log100<5 gives sufficient zero-count n=5W=160,000,020,000,000. This is enormous, not an operational forecast. For the same per-layer rectangular bounds the effect contribution is64,000,000,000,000 rather than32,000,000,000,000. The generic K2512 full-carrier weight with center epsilon allowance1/2000000 and leakage allowance1/4000000 is1,728,000,864,000,000; its class is much broader, so no universal superiority is claimed. Four pair preparations plus one leakage setting cover this specified network, including the active spectator pair.

The reused two-gap complete-record consumer is E_record<=2049/10^6; with ideal acceptance>=1/2 and ideal bad-and-accepted mass0, conditional error<=2049/497951<1/200. Confidence failure is separate. No passing data, calibration success, or actual hardware is asserted.

## 5. Contrary controls and boundary

- A listed spectator rotation is detected on its own endpoint even when K2512's original A/e1 tests pass. Omitting that pair gives zero detection probability and no uniform certificate.
- An unlisted spectator swap, or unknown coupling between listed planes, violates class membership and can pass all supplied tests. The class is a promise, not an inferred physical fact.
- Global Q/T commutation is false; a fixture retains an untouched noncommuting principal-angle block while both per-layer proofs remain valid.
- Two aligned nonzero rotations accumulate coherently. Their full effect exceeds either individual effect and exceeds the root-sum-square bound for small equal angles. No stochastic cancellation is assumed.
- Opposite rotations cancel at the final gap despite nonzero pooled mean. This shows conservatism and prevents claiming that the angle certificate is necessary for a good final effect.
- Certifying isolated gates while allowing a different gate on composition, a setting-dependent device, or unbounded parameter drift is insufficient. These are explicit access/coverage failures.
- Equal endpoint transition probabilities use unitarity. A nonunitary one-way reset can leave the tested endpoint fixed while moving the untested endpoint; it is outside the U(2) class and invalidates a one-endpoint inference.
- A rank-one wrong probability p controls effect norm sqrt(p), not p; complex phases do not remove this coherent defect.

The full proofs establish the stated finite-dimensional class and angular-envelope design. The eight-dimensional data fixture retains a noncommuting principal block at angle parameter9/25; it is structurally faithful, not a numerical replay of the original108-dimensional matrices. The written reducing-subspace argument supplies that full-carrier theorem. Exact probes support complex-block identities, this finite embedding, positive and contrary fixtures, convexity and resource arithmetic; they are not a finite proof of arbitrary experimental behavior. Closest generic context: gate-set verification [Zhu and Zhang](https://arxiv.org/abs/1910.14032) and projection-angle geometry [Neretin](https://arxiv.org/abs/math/0005059). The specialized proofs above stand on their stated hypotheses; these citations do not establish novelty.

Next: obtain independent evidence for the complete circuit class, primitive isolation, preparation/readout and deployment coverage, or replace the class promise with tests controlling cross-plane/nonunitary couplings. The full native GU physical-state bridge remains separate.


[Exact probe](../../tests/channel-swings/k2514_structured_spectator_calibration_probe.py), [saved report](../../lab/process/k2514-structured-spectator-calibration.json), [K2512 implementation](k2512-finite-memory-implementation-2026-11-02.md), [K2504 sector calibration](k2504-verifier-sector-calibration-2026-11-02.md), [K2484 original instruments](k2484-coherent-verifier-instruments-2026-11-01.md).
