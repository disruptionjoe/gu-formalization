---
title: "K2063: Exact moving-sector transport and its locality cost"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional massive1408 graph and supplied spectral or CAR criterion only; no GU physical quotient or novelty claim
scripts:
  - tests/channel-swings/k2063_moving_sector_transport.py
  - tests/channel-swings/k2063_moving_sector_transport_probe.py
---

# K2063: Exact moving-sector transport and its locality cost

Classification: `INTERNAL_STRUCTURAL_ONLY`.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

```gu-typed-objects
result: complete bounded tracking correction, locality obstruction and quantitative finite-range and slow-time controls
carrier: complexified real1408 observed graph on R3 or stated three-torus LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: fixed universal positive metric transported to standard L2 ON=declared_observed_graph
real_structure: real Clifford C_j and real skew M with beta=-i M
grading: instantaneous energy signs and separately imported CAR sea, not source fermionic parity
action_owner: repository-construction -- K2058 conditional graph with externally supplied mass and optional correction
target: moving sector and many-particle admissibility for the declared construction MAP-TYPE=intertwiner
```

[Verified conditional mathematics.] A changing positive-energy sector of the existing massive1408 graph can be transported exactly by an explicit bounded correction. Its off-diagonal part is forced and nonlocal. No bounded spatial multiplication potential, nor any translation-invariant finite-order differential correction, can do the same when the mass is changing. The result supplies a concrete repair of one-particle sector leakage with a quantified change of locality assumptions. It does not select a GU physical sector.

This is a specialization and further analysis of established transitionless driving, not a new general principle: [Berry, Transitionless quantum driving, J. Phys. A42 (2009)365303](https://michaelberryphysics.wordpress.com/wp-content/uploads/2013/07/berry415.pdf). The projector proof below accommodates the actual degeneracy without choosing individual eigenvectors. [K2062](k2062-bounded-local-multiplier-rigidity-2026-10-25.md) supplies the bounded-local commutant theorem; [K2058](k2058-universal-positive-dynamics-2026-10-25.md) supplies the graph and positive metric. Their scientific evidence is hash-pinned reuse.

## 1. Frozen object and downstream demand

Let A(p)=sum_j C_j p_j, beta=-iM, with Hermitian Clifford matrices, A^2=r^2 I, beta^2=I, {A,beta}=0, r=|p|. The full fiber dimension is1408. Use the fixed positive metric Pstar from K2058 and its constant isometry to standard L2. On R3 set

    H(t,p)=A(p)+m(t) beta, E(t,p)=sqrt(r^2+m(t)^2),
    P(t,p)=(I+H/E)/2.

On each compact time interval assume real m is C1 and m>=m_*>0. All H(t) have common H1 domain. The two spectral fibers each have dimension704. The demand is exact transport U(t,s)P(s)=P(t)U(t,s) by H+K with bounded Hermitian K(t). This is stronger than positive norm conservation, different from positive expectation of H+K, and different from a source-selected quotient. The extra K changes the dynamics; it is not already part of the original mass pulse.

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 is UNCERTAIN about the southeast alternative; SC-META-53 is UNCERTAIN about physical positivity; SC-META-56 DISAVOWS an odd-action prerequisite. None supplies this sector or correction. LT-SM8/LT-GR6b retain their interacting quotient/domain debts. The reverse-search question is whether an explicitly stated state-preservation demand can coexist with locality on this conditional carrier, not whether GU has recovered that demand.

## 2. Complete bounded correction and sharp norm

Differentiating U*PU gives the necessary and sufficient equation

    [K,P]=i dot(P).

Differentiate P^2=P. Then dot(P) is off-diagonal relative to P and
[[dot(P),P],P]=dot(P). Consequently every bounded Hermitian solution is

    K=K_cd+D, K_cd=i[dot(P),P], D*=D, [D,P]=0.       (1)

Here D may be a general bounded operator; no translation invariance is needed for this classification. The unique off-diagonal part is K_cd. On the actual Clifford symbol,

    dot(P)=dot(m)(r^2 beta-m A)/(2 E^3),
    K_cd=i dot(m) beta A/(2 E^2),
    K_cd^2=dot(m)^2 r^2 I/(4 E^4).                  (2)

Thus on R3

    ||K_cd(t)||=|dot(m)|/(4m),                      (3)

with the symbol maximum at r=m. Any K in(1) has norm at least that of its off-diagonal block, which equals this value. D=0 attains the minimum; uniqueness of the full norm minimizer is NOT asserted. On a torus the maximum is a supremum over its momentum lattice and need not equal(3).

K_cd is bounded, Hermitian and norm-continuous on compact time intervals. For the selected correction D=0, solve the finite-dimensional unitary ODE at each momentum. The resulting Fourier multiplier preserves every Sobolev space because its fiber norm is1; dominated differentiation on H1 gives the Schrödinger equation with common domain. Direct differentiation on H1, followed by density in L2, proves exact transport. The algebraic classification of general bounded D in(1) does not claim that every such D preserves H1. The positive metric commutes with the Clifford algebra, so the same statements hold before its isometry. K_cd(-p)=-conjugate(K_cd(p)); hence the evolution generator preserves the original real-field reality condition. It is a new nonlocal operator, not a local zero-order coefficient in the old compatible generator class.

If m reaches zero with nonzero derivative, the displayed correction has size |dot(m)|/(2r) near p=0 and is unbounded. The present bounded/common-domain theorem does not cover that crossing. This is not an exclusion of all unbounded-domain constructions.

## 3. Why bounded local and polynomial differential repairs fail

Fix a time with m>0 and dot(m)!=0. Suppose K=M_V is a bounded measurable Hermitian matrix multiplier in position space. Translation of [M_V,P]=i dot(P) and subtraction shows that M_(V(.+a)-V) commutes with the fixed massive P. K2062's complete bounded-multiplier theorem makes this difference a constant Clifford-commuting matrix C(a). The cocycle identity gives C(a+b)=C(a)+C(b), while ||C(a)||<=2||V||. In particular C(na)=n C(a) stays bounded, so C(a)=0. Translation invariance of the bounded distribution V makes V constant almost everywhere.

For a constant V, the symbol equation at p=0 gives [V,beta]=0. The limit p=r n, r tending to infinity, gives [V,C.n]=0 for every n. Hence [V,P]=0 for every p, contradicting nonzero dot(P) at r>0. Thus no bounded measurable local multiplication correction can track this moving sector. This is a moving-sector obstruction; it does not claim that all local dynamics or observations are impossible.

Even a translation-invariant finite-order differential correction is impossible. Its matrix symbol K(p) is polynomial, and the required identity is

    (r^2+m^2)[K(p),A(p)+m beta]
       =i dot(m)(r^2 beta-m A(p)).                  (4)

It holds polynomially if it holds at all real p. Restrict to p=(z,0,0), complexify, and evaluate at z=i m. The left side is zero; the right is -i dot(m)m^2(beta+i C1), a nonzero matrix. This contradiction rules out every polynomial order and every matrix coefficient in that translation-invariant class. Variable-coefficient differential operators are not classified here.

## 4. Spatial kernel, finite-range approximation and propagation

Use ordinary convolution normalization for the inverse of -Delta+m^2:

    G_m(x)=exp(-m|x|)/(4pi|x|),
    K_cd psi=(dot(m)/2) beta (C.grad G_m)*psi.        (5)

For x!=0 the matrix kernel norm is

    |dot(m)| exp(-m r)(m r+1)/(8pi r^2).             (6)

This kernel is integrable at the origin and infinity and is nonzero at every nonzero displacement when dot(m)!=0. Formula(5) follows from p_j mapping to -i partial_j and beta A, not from a heuristic range assignment. The full tracking dynamics therefore does not inherit K2058's finite-propagation theorem for local zero-order potentials. For example, convolving a sufficiently concentrated smooth compact bump times a suitable vector gives a nonzero derivative at a separated point; the local differential part vanishes there. Smooth initial data and small-time differentiability then show instantaneous tails. No operational signaling claim follows without an observable and physical interpretation.

Truncate the kernel to |x|<=R, obtaining Hermitian bounded K_R. Young's inequality and the exact radial integral give

    ||K_cd-K_R|| <= |dot(m)| exp(-mR)(R+2/m)/2.     (7)

Let U_R be the evolution of H+K_R. Duhamel and exact transport imply

    ||(I-P(t)) U_R(t,s) P(s)||
       <= integral_s^t |dot(m(u))| exp(-m(u)R)
                              *(R+2/m(u))/2 du.    (8)

The bound is dimension-independent in operator norm; it applies to all704 positive fiber directions simultaneously. It is sufficient, not sharp. A finite-range integral operator still permits repeated spatial jumps, so(8) is NOT a finite propagation-speed theorem.

## 5. Uniform slow-time alternative without adding K

For a concrete alternative keep the original local H and change only the speed of a positive mass profile. Let m=m(s), s in[0,1], be C2, m>=m_*, with m'(0)=m'(1)=0, and run m(t/T) over[0,T]. Rotate each radial Clifford block to h_r=r sigma1+m sigma3. Its instantaneous angle has derivative theta'=-r m'/E^2. In the dynamical-phase basis the off-diagonal coefficient is f=theta_dot/2 and the two amplitudes have norm1.

Integrate the transition integral once by parts with phase derivative2E. The boundary term vanishes by endpoint flatness. With g=f/(2E), the absolute remainder is bounded by integral(|dot(g)|+|g f|). Since r/E<=1, E>=m_*,

    ||(I-P(T)) U_H(T,0) P(0)|| <= C_ad/T,
    C_ad= integral_0^1 [ |m''|/(4m_*^2)
             +3|m| |m'|^2/(4m_*^4)
             +|m'|^2/(8m_*^3) ] ds.               (9)

Use min(1,C_ad/T) if desired. This is uniform over all momenta and multiplicities, unlike a fixed-momentum adiabatic statement. It is an upper bound, not a sharp rate or an exact common-sector theorem. The same estimate applies when initial and final positive masses differ, with the corresponding two projectors. Endpoint flatness, the positive gap and the specified C2 profile are explicit hypotheses.

## 6. Exact finite-mode alternative and its changed locality

There is a concrete resource-limited alternative to the continuum polynomial obstruction. On a torus retain only finitely many momenta |p|<=Lambda, and let S be the finite set of their distinct squared radii. At each m>0 interpolate

    q_m(s)=sum_(a in S) [1/(a+m^2)]
                          *product_(b in S, b!=a) (s-b)/(a-b).

Then K_poly(p)=i dot(m) beta A(p) q_m(r^2)/2 agrees EXACTLY with K_cd on every retained mode. It has a finite-order differential expression of order at most2|S|-1, preserves the same real-field reality, and tracks the sector on this invariant finite-dimensional space. Coefficients depend smoothly on positive m. The proof is interpolation, not an approximate numerical fit.

This is not a local continuum repair: the initial spectral cutoff is itself nonlocal, and the polynomial is not required to track or remain bounded on discarded modes. On the full continuum it is prohibited by section3. Finite-mode restriction makes every many-particle implementation finite-dimensional; K2064 records this resource change rather than attributing it to GU. The example prevents an all-resource extrapolation of the continuum obstruction.

## 7. Review and use

Exact four-dimensional Clifford controls check(1)--(4), with a separate Pauli/vector implementation and symbolic kernel and integration-by-parts coefficients. Written proofs supply general degeneracy, functional domains, measurable-local rigidity, arbitrary polynomial order and uniform norm bounds. Coefficient mutations must fail after a clean baseline. Same-author checking is not independent specialist or proof-assistant certification.

The useful repair is complete at one-particle level: exact tracking requires a nonlocal added term; finite-range and slow local approximations have explicit error budgets. It does not automatically give a fixed many-particle representation. [K2064](k2064-mass-pulse-fock-boundary-2026-10-25.md) tests that independent requirement on this same construction. Remaining work must specify the observed-state criterion and allowable locality/representation changes, or supply a different source-owned bridge; the formulas here do not select those inputs.
