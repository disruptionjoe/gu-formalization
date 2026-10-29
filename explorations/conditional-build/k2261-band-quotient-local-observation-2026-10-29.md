---
title: "K2261 Local observations of the reflected band quotient"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied model theorem only; no source physicalization or canonical verdict
scripts:
  - tests/channel-swings/k2261_band_quotient_local_observation_probe.py
---

# K2261 Local observations of the reflected band quotient

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2261 Local observations of the reflected band quotient
carrier: K2254 constrained complex1280 L2 fields on R13 and K2258 reflected compact-band quotient LAYER=toy CHIRALITY=N/A
pairing: supplied equivalent positive G norm and ordinary L2 duality ON=declared_carrier
real_structure: complex conjugation and Hilbert adjoint
grading: copy, charge and record labels, not observed physical chirality
action_owner: repository-construction -- supplied conditional operator and apparatus
target: dense local representative classes and obstruction to local linear readout MAP-TYPE=intertwiner
```

## 1. The actual quotient and the unanswered locality question

[K2258](k2258-variable-local-preparation-2026-10-29.md) constructs a positive quotient of the unchanged [K2254 raw candidate](k2254-raw-nonparallel-domain-2026-10-29.md). It does not construct a local physical quotient. Let U_n={1,...,6,10,...,13}, and K be the L2 kernel of

    S(w)=sum_a w_a, T(k)w=sum_a gamma_a k_a w_a.

Its generic fibre has complex dimension1024. In K2258 notation, sigma reflects k1,k10, V=gamma1 gamma10, Rf(xi)=Vf(sigma xi), and Pi=1_B(I+R)/2. B is the compact reflection-invariant pair of small balls around k=±kappa e10,p=0, with lambda>=delta>0. Choose their radii less than kappa/2. Then k10²+k11² is bounded away from zero throughout B. The supplied mathematical quotient Q=K/ker Pi identifies with M=ran Pi, endowed with G=(I+H*H/lambda)/2; G>=I/2 and is uniformly bounded on B. H induces bounded selfadjoint dynamics in that G norm. All of these structures are supplied, not selected by the source or a gauge action.

Question: can a continuous scalar observation of this quotient depend only on a bounded spatial region of an arbitrary constrained representative? Compact representatives alone do not answer this.

## 2. Full local parametrization on the selected band

The single-spinor polynomial P0 of [K2255](k2255-local-constraint-stability-2026-10-29.md) proves existence of compact constrained fields, but has at most128-dimensional image. It cannot prove density across1024 fibre components. We construct a different polynomial P with eight128-spinor inputs, a in U_n\{10,11}.

    r=10, s=11, D=gamma_r k_r-gamma_s k_s,
    d=-(k_r²+k_s²), D²=d I,
    w_a=d v_a                         (a≠r,s),
    M_v=sum_(a≠r,s)(gamma_a k_a-gamma_s k_s)v_a,
    w_r=-D M_v,
    w_s=-d sum_(a≠r,s)v_a-w_r.                 (1)

S=0 directly, while T=Dw_r+d M_v=-D²M_v+d M_v=0. These are identities at every frequency, including d=0. Where d≠0 the image equals the full K fibre: given w∈K, recover v_a=w_a/d; T=0 then uniquely determines w_r since D^-1=D/d, and S determines w_s. P has rank8·128=1024 there. This explicit readback proves surjectivity without numerical rank inference.

P(-i partial) maps arbitrary smooth compactly supported1024-component inputs to smooth compact constrained fields. At k10=kappa, all other normal momenta zero, w10=0, w11=kappa² sum v_a, and w_a=-kappa²v_a on every free copy. This is a full-rank exact control. At generic momenta the sparse Clifford identities test the signs and both constraints.

## 3. Local representatives are dense in the entire quotient

**Theorem.** For every nonempty spatial open O⊂R13,

    closure {Pi P(-i partial)phi : phi∈Cc∞(O;C1024)} = M.       (2)

Closure is in either ordinary L2 or the equivalent G norm. Proof: if f∈M is L2-orthogonal to the displayed set, selfadjointness of Pi implies P(-i partial)*f vanishes distributionally on O. Its Fourier transform is P(xi)*fhat(xi), with compact support B. It is therefore an entire analytic field; analytic uniqueness forces it to vanish everywhere. On B, fhat∈K(xi) and ran P(xi)=K(xi), so P(xi)*fhat=0 forces fhat=0. The orthogonal complement is zero, proving density. This uses the standard compact-Fourier-support analyticity principle; see the [MIT Paley-Wiener-Schwartz statement](https://math.mit.edu/~rbm/Problems4.pdf). No novelty of that principle is claimed.

Density does not assert exact preparation, uniform norm bounds for phi, or physically implementable localized operations. The map Pi is itself nonlocal. In particular, it is not a quantum-field vacuum cyclicity theorem.

## 4. No nonzero continuous local linear observation descends

Let ell be a continuous complex linear functional on Q. If its pullback ell(Pi q) vanishes for all constrained preparations q supported in one nonempty spatial open set O, (2) forces ell=0. Therefore a nonzero ell cannot depend only on representative data in a region whose exterior has a nonempty open set.

**Uniform approximate-locality corollary.** If for all phi supported in one nonempty exterior open O, |ell(Pi P(D)phi)|<=epsilon ||Pi P(D)phi||_G, density and continuity imply ||ell||<=epsilon. Thus a normalized nonzero readout cannot have uniformly small exterior sensitivity measured relative to quotient-state norm. This supplies no uniform preparation-cost bound in the input phi or its derivatives; bounded-input approximate locality remains a different question.

A distributional version handles the constraint annihilator carefully. Suppose a compactly supported distribution h represents ell on every compact smooth constrained q by ell(Pi q)=<h,q>. Ordinary L2 Riesz gives f∈M for ell (equivalent G topology suffices). Testing q=P(D)phi gives

    P(D)*h=P(D)*f.                                   (3)

The left side has compact spatial support, while the right side is entire analytic. Hence both vanish. Fibre surjectivity again gives f=0, and ell=0. This does NOT say h must be zero: a nonzero constraint-annihilating h can represent the zero functional. Ignoring this K-perpendicular ambiguity would overstate the theorem.

**Positive control.** Canonical field evaluation f↦f(x) IS bounded:

    |f(x)| <= (2pi)^(-13/2) sqrt(2|B|) ||f||_G.        (4)

Cauchy-Schwarz in Fourier space and G>=I/2 prove it. Its pullback q↦(Pi q)(x) has nonlocal dependence on q, so it does not contradict (3). Evaluation of the original q is a different map and generally does not descend.

## 5. Followthrough: finite propagation of canonical representative response fails

For a compact preparation q=P(D)phi with Pi q≠0, put f_t=exp(-itH)Pi q. For every finite t, f_t is nonzero (the group is invertible) and compact-band. Each nonzero component is analytic and cannot vanish on a nonempty open set. Thus f_t cannot be supported in any bounded finite-speed expansion of supp(phi). This failure already occurs at t=0 through Pi; it is not evidence of superluminal propagation of an operationally local state.

More sharply, for any nonzero continuous linear readout ell and any fixed t, ell∘exp(-itH) is nonzero and continuous. Applying (2) shows that some phi supported in ANY preassigned nonempty open O changes that readout. There is no exact exterior-insensitivity condition of that representative-based kind, even if O is far away. This is an existence result without a distance-uniform signal amplitude or preparation-cost bound.

The result closes the proposed local-linear-readout interpretation of THIS reflected compact-band quotient. It eliminates attempts to turn its compact representatives into local canonical states by relabeling. Nonlinear/local-algebra observables, unbounded/discontinuous functionals, other quotients, noncompact spectra, changed raw coefficients or a source-derived action/domain require their own constructions; no universal GU locality verdict follows.

## Scientific ceiling and reproduction

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 remains UNCERTAIN on the southeast rival; SC-META-53 remains UNCERTAIN on physical positivity. These supplied constructions do not resolve those source claims. Ledger0.263 and LT-SM8/LT-GR6b/AC-F1 remain unchanged: action ownership, physical quotient and observed-domain bridges remain absent. Preserve full16cells/full20/K-C, native2+1/nonchiral, mirrors/fullII/normaljets, scalar/thermal and cosmology ceilings.

Universal statements are written proofs; finite exact probes test the declared algebra and resource controls, not continuum completeness. Internal independent review is distinct from Lean, external-expert, novelty or remote-CI certification. Run the script listed above, adding `--write` only to regenerate its report.
