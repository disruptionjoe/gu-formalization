---
title: "K2258 Variable local preparation and a non-fibrewise quotient"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied model theorem only; no source physicalization or canonical verdict
scripts:
  - tests/channel-swings/k2258_variable_local_preparation_probe.py
---

# K2258 Variable local preparation and a non-fibrewise quotient

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2258 Variable local preparation and a non-fibrewise quotient
carrier: K2254 constrained complex1280 fields on R13 and their closed Hilbert subspaces/quotients LAYER=toy CHIRALITY=N/A
pairing: supplied equivalent positive Hilbert norm and explicit quotient G norm ON=declared_carrier
real_structure: complex conjugation and Hilbert adjoint; raw real structure when stated
grading: copy, reflection and energy-sign labels, not observed physical chirality
action_owner: repository-construction -- unchanged K2254 raw candidate
target: local preparation obstruction and explicit nonlocal positive quotient MAP-TYPE=intertwiner
```


## 1. Question and hypotheses

[K2255](k2255-local-constraint-stability-2026-10-29.md) excludes finite constant-coefficient polynomial filters. It does not justify excluding variable coefficients or non-fibrewise quotients. We test both, using the UNCHANGED [K2254 raw candidate](k2254-raw-nonparallel-domain-2026-10-29.md).

Let K be the closed L2 kernel of S=sum w_a and T=sum gamma_a k_a w_a. On this kernel the actual block diagonal multiplier H satisfies

    H_a=sum_(j=7,8,9) C_j p_j
        +sum_(r in U)(1-2 delta_ar) C_r k_r-i m A,
    H²=lambda I, lambda=|p|²-sum_U eta_r k_r²+m²,
    U={1,...,6,10,...,13}, C_r=gamma0 gamma_r, A=gamma0 J.

The invariant raw reduction, signature and copy labels are those of K2254. No replacement Dirac surrogate is used.

Suppose M is ANY closed subspace of K, not assumed translation invariant. It carries a Hilbert norm with fixed constants c,C>0 satisfying c||u||2<=||u||M<=C||u||2. Suppose a selfadjoint operator A_M on M acts distributionally as H on Dom A_M. These are real hypotheses: an arbitrary indefinite form, degenerate quotient seminorm or discontinuous embedding does not satisfy them.

**Theorem.** Every u in M has Fourier support in {lambda>=0}. Consequently M contains no nonzero compactly supported distributional field. Any finite-order smooth-coefficient differential operator P(x,D) mapping ALL compactly supported smooth inputs to M is identically zero. No fibrewise metric or translation invariance of M is assumed.

## 2. Proof with full two-sided evolution

U(t)=exp(-it A_M) gives ||U(t)u||2<=C/c ||u||2 for every real t. For u in Dom A_M its evolution solves i partial_t u=Hu distributionally. Let chi be a smooth compact Fourier cutoff in {lambda<0}; on its support rho=sqrt(-lambda) is bounded above and away from zero and the smooth algebraic projectors

    Q_+=(I+H/(i rho))/2, Q_-=(I-H/(i rho))/2

are bounded. Multiplication by chi does not need to preserve M. In the ambient L2 space, localizing the distributional equation gives an ODE with bounded coefficient. Uniqueness (or its integral equation) implies

    chi Q_+ uhat(t)=exp(rho t) chi Q_+ uhat(0),
    chi Q_- uhat(t)=exp(-rho t) chi Q_- uhat(0).

Density of Dom A_M, uniform L2 bounds and bounded localized multipliers extend the identities to every u in M for each fixed t. The first identity as t→+infinity and the second as t→-infinity force both localized initial vectors to vanish. A countable cutoff exhaustion of {lambda<0} proves the support assertion. Only the identity H²=lambda on the constrained carrier and two-sided bounded evolution were used.

A compactly supported distribution has an entire Fourier transform. Since {lambda<0} contains a nonempty real open set, analytic uniqueness forces that transform to be zero. This uses the standard [Paley-Wiener-Schwartz principle](https://math.mit.edu/~rbm/Problems4.pdf). A smooth finite-order differential P preserves compact support; hence P phi=0 for every test phi. Arbitrary finite jets of test functions then force every coefficient of P to vanish.

This extends the polynomial-filter obstruction to arbitrary smooth local PREPARATION maps and globally nonlocal equivalent norms. It does not classify every variable-coefficient constraint kernel: such a kernel need not contain the full image of any nonzero differential parametrization. Nor does it exclude a semigroup with only forward boundedness, a non-equivalent norm, boundary geometry, changed raw coefficients or a quotient.

A concrete necessity check: at p=0,k1=5,m=3 the growing/decaying raw eigenvalues are ±4i. The decaying eigenbranch is bounded only forward, so a one-sided argument cannot eliminate it. The finite controls check both projectors and opposite exponent signs; the theorem is the written continuum argument.

## 3. A non-fibrewise global quotient DOES escape the subspace conclusion

Let sigma reflect k1 and k10, leaving other momenta fixed, and V=gamma1 gamma10 on every copy. Real Cl(7,7) gives

    V²=I, V*=V, H(sigma xi)=V H(xi)V,
    T(sigma k)V=V T(k).

Choose an explicit compact sigma-invariant union B of two sufficiently small closed balls around k=±kappa e10,p=0, with kappa>0, k≠0 and lambda>=delta>0. Set Rf(xi)=Vf(sigma xi). It is a real orthogonal involution preserving K. The bounded projection

    Pi=1_B (I+R)/2

is an ordinary-L2 orthogonal projection on K, commutes with H on its maximal multiplier domain, and has compact-frequency range. N=ker Pi is closed. On Dom H, H(N intersect Dom H) is contained in N; no unproved invariance of the unbounded operator DOMAIN is asserted. The quotient K/N identifies with ran Pi, and H induces the bounded operator H Pi: every class has its canonical representative Pi f in Dom H. Thus quotient dynamics is defined on the whole quotient.

On the band put G=(I+H*H/lambda)/2, copywise. H*G=GH follows algebraically from H²=lambda I, and G is positive and uniformly bounded with bounded inverse there. Since lambda is reflection invariant and H intertwines V, R is also G-unitary. The induced quotient operator is selfadjoint in the inherited G norm. It is nonzero: symmetrize a nonzero constrained section supported in one ball. Pi is genuinely non-fibrewise in the original momentum decomposition: it fails to commute with multiplication by a scalar function taking different values on the two balls.

This is an explicit global quotient with positive dynamics, not a BV/gauge quotient or a source-selected observation. It STILL supplies stable band B and G. It therefore neither disproves the subspace theorem nor physicalizes the source.

## 4. Local representatives are not local physical states

K2255 supplies nonzero compact smooth constrained fields q=P0 phi. In position space R reflects the two coordinates and multiplies by V; it preserves compact support and K. Choose phi supported in a ball disjoint from its reflection and set q_even=q+Rq, which is nonzero and compact. Since q_even is entire in Fourier space, it cannot vanish on the nonempty interior of B unless it is zero. Therefore Pi q_even is a nonzero quotient class even though its canonical representative has nonlocal spatial tails.

A compact representative is allowed because quotienting removes information nonlocally. One cannot infer locality of observables, finite propagation, local preparation of the canonical representative or a source-owned physical quotient. The local-preparation branch is closed under the theorem's hypotheses; the global quotient is an actual escape with its additional data and remaining bridges explicit.


## Reproduction and scientific ceiling

Run `python tests/channel-swings/k2258_variable_local_preparation_probe.py`; `--write` refreshes the report. Exact finite controls and genuine changed-input faults supplement the written proofs; sampling does not prove the universal assertions. Independent internal specialists reviewed the actual arguments and probes, including cross-review of the separate results. No Lean, external-expert, novelty or remote-CI certification is claimed.

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 remains UNCERTAIN on the southeast rival; SC-META-53 remains UNCERTAIN on physical positivity. These supplied models do not resolve those source claims. LT-SM8/LT-GR6b/AC-F1 and ledger0.263 remain unchanged because action ownership, physical quotient and observed-domain bridges remain absent. Preserve full16cells/full20/K-C, native2+1/nonchiral, mirrors/fullII/normaljets, scalar/thermal and cosmology ceilings.
