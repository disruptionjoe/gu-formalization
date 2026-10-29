---
title: "K2255 Local constraints and stability of the fixed raw candidate"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied model theorem only; no source physicalization or canonical verdict
scripts:
  - tests/channel-swings/k2255_local_constraint_stability_probe.py
---

# K2255 Local constraints and stability of the fixed raw candidate

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2255 Local constraints and stability of the fixed raw candidate
carrier: K2254 ten complex128 normal-copy fields on R13 momentum space LAYER=toy CHIRALITY=N/A
pairing: hypothetical positive fibre forms versus the supplied stable-band norm ON=declared_carrier
real_structure: complex conjugation and Hilbert adjoint; raw real Clifford structure where specified
grading: raw copy labels and energy signs, not observed physical chirality
action_owner: repository-construction -- unchanged K2254 raw1920 operator and mass m
target: finite local constraint class, localized initial data and unstable propagation MAP-TYPE=intertwiner
```

## Question and exact inheritance

[K2254](k2254-raw-nonparallel-domain-2026-10-29.md) constructs finite-norm nonparallel solutions of the unchanged specified raw1920 candidate on a compact stable Fourier band. Its constraints

    S(w)=sum_a w_a=0, T(k)w=sum_a gamma_a k_a w_a=0

are ALREADY LOCAL: S is algebraic and T is a constant-coefficient first-order differential equation after inverse Fourier transformation. Referring to the entire construction as nonlocal must not obscure this. The support restriction, spectral sign projection and auxiliary positive norm are the extra nonlocal choices. This note sharpens that distinction and tests replacement of stable support by additional local equations.

Retain K2254's O={0,7,8,9}, U={1,...,6,10,...,13}, eta=(+seven,-seven), real128 Cl(7,7), J=gamma0...gamma13, A=gamma0 J, C_r=gamma0 gamma_r. For a in U,

    H_a=sum_(j=7,8,9) C_j p_j
        +sum_(r in U)(1-2 delta_ar)C_r k_r-i m A,
    H_a²=lambda I, lambda=|p|²-sum_U eta_r k_r²+m².       (1)

The exact raw-block verification and invariant rank1024 bundle K=ker(S,T) off k=0 are inherited from K2254. No alternate Dirac surrogate or changed lower return is introduced.

## 1. Finite local equations cannot select a nonzero positive full-domain sector

Let D(p,k) be ANY finite matrix with complex polynomial entries and1280 columns, containing S,T among its rows. It describes homogeneous linear constant-coefficient finite-order equations on initial data. Polynomial degree need not be homogeneous. Define E(p,k)=ker D(p,k). Assume:

1. E is H-invariant almost everywhere in all R13;
2. the restriction H|E is selfadjoint for a positive-definite fibre inner product almost everywhere;
3. the allowed L2 fields are the full measurable kernel of D, with NO additional Fourier-support or nonlocal subspace restriction.

Then the L2 solution space is zero.

Proof. On the nonempty open set lambda<0, any nonzero u in E would satisfy

    <Hu,Hu>_E=<u,H²u>_E=lambda<u,u>_E<0,

a contradiction. Thus D has full column rank almost everywhere on that open set. At one such point a1280-by1280 minor is nonzero (if D has fewer rows, the assumptions are inconsistent immediately). Its determinant is a nonzero polynomial. A nonzero real-variable polynomial, including a complex polynomial via its absolute square, vanishes on a Lebesgue-null set. Off that set D has full rank, so E=0 almost everywhere globally. Plancherel gives the result. No uniform conditioning of the positive metric is needed for this finite-fibre argument.

This excludes an entire class of local spectral filters, not only extra copies of T. It does not exclude variable-coefficient constraints, boundary/compact domains, non-L2 characteristic distributions, changed raw operators, explicitly nonlocal spectral support, or gauge quotients. An indefinite inherited form is not the positive form in assumption2. A local field equation by itself is not a claim of causal well-posedness.

For a polynomial parametrization w=P(p,k)v with arbitrary compact-frequency L2 input (or input in the polynomial multiplier domain), if its full image is invariant and positive-selfadjoint at every generic frequency, the same unstable-open-set argument makes every entry of P vanish there; polynomial uniqueness gives P identically zero. A further finite-polynomial quotient statement is possible: let Q=ker D/im P with DP=0 and both spaces H-invariant. Require the induced H on the entire fibre quotient to be positive-selfadjoint almost everywhere. On lambda<0 that quotient is zero, so at a good point rank D+rank P=1280. The corresponding nonzero minors imply at least those ranks off a polynomial null set; DP=0 bounds their sum by1280. Thus the quotient is zero almost everywhere globally. This covers ordinary L2 sections of finite polynomial fibre quotients, not arbitrary BV/physical quotients, nonclosed global gauge ranges or singular-support distributions.

## 2. Positive control: local constraints DO admit compactly supported data

The conclusion is not that local S,T have no localized data. Set

    R=gamma1 k1-gamma2 k2, q=k1²+k2²,
    M=gamma3 k3-gamma4 k4,
    w1=-R M v, w2=R M v, w3=q v, w4=-q v,
    all other w=0.                                    (2)

Then S=0 and T=-R²Mv+qMv=0 since R²=qI. This nonzero degree-two polynomial image maps generic smooth compactly supported spinor functions v under P(-i partial) to nonzero smooth compactly supported K-data. It is a concrete repair of any overbroad claim that the LOCAL constraints themselves forbid localization. What fails on the full kernel is positive stable evolution, not initial-data existence.

## 3. Explicit instability, with finite derivative loss also insufficient

At p=0,k1=R>m>=0, other k=0, take w3=v,w4=-v. This is in K, and both occupied copies evolve under

    H=R C1-i m A, H²=-(R²-m²)I=-rho²I.

The projector Q_g=(I+H/(i rho))/2 has rank64 on each full spinor and H Q_g=i rho Q_g. Its nonzero range grows as exp(rho t) under exp(-itH). For R=5,m=3, rho=4 is exact. The complementary projector decays forward and grows backward; choosing only the decaying branch is another nonlocal, non-selfadjoint restriction, not a positive unitary repair.

To avoid using a measure-zero plane wave as an L2 argument, work in a small open ball around k=R e1. Solve the S,T corrections using the invertible R12=gamma1 k1-gamma2 k2, and then apply the smooth full block-diagonal Q_g to the resulting K section. At the center choose v in its growing range, so the corrected projected section stays nonzero in a smaller ball. A compact smooth amplitude there gives an actual Schwartz packet. Choose the ball so rho>=R/2. Normalize in H^(s+d), with fixed real s and finite d>=0. Its H^s norm at time t>0 grows at least c(1+R)^(-d) exp(tR/2). This diverges as R grows. Therefore no bounded same-time map H^(s+d)∩K -> H^s on the full kernel exists for any finite derivative loss. The norm ratio estimate follows because all packet frequencies have magnitude comparable to R; it needs no uniform derivative bounds on the section. Each individual compact-frequency packet still has a perfectly defined finite-time solution.

## 4. Stable support cannot provide compactly supported local excitations

If all13 spatial coordinates of a distributional initial field have compact support, each Fourier component is entire. If its Fourier support is restricted to lambda>=0, it vanishes on the nonempty real open set lambda<0 and therefore vanishes identically. In particular K2254's nonzero compact-band Schwartz states cannot also be compactly supported spatial excitations. This is the ordinary compact-support analyticity consequence of the [Paley-Wiener-Schwartz theorem](https://math.mit.edu/~rbm/Problems4.pdf), not a new theorem or a universal statement about every local theory.

The polynomial rank proof and explicit high-frequency instability settle the finite constant-coefficient local replacement branch. A source-facing successor must change a named premise: variable geometry/constraint, quotient, domain or raw principal operator, then test the same original returns and actual observation. Source silence supplies none of those inputs and excludes none of them.

## Reproduction and scope

Run `python tests/channel-swings/k2255_local_constraint_stability_probe.py`; `--write` refreshes its exact report. Finite exact controls and changed-input faults supplement the written universal proofs, not certify them by sampling. The concrete proof and controls received independent internal specialist review; no Lean, external-expert, novelty or remote-CI certification is claimed.

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 remains UNCERTAIN on the southeast rival; SC-META-53 remains UNCERTAIN on physical positivity. These results concern supplied constructions, not every source-admitted completion. LT-SM8/LT-GR6b/AC-F1 and ledger0.263 remain unchanged. Preserve full16cells/full20/K-C, native2+1/nonchiral, physical quotient and global source-domain debts.
