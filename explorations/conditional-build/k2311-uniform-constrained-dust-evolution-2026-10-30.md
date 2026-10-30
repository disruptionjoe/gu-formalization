---
title: "K2311 Uniform constrained dust evolution"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics only; no native physical acceptance
scripts:
  - tests/channel-swings/k2311_uniform_constrained_dust_evolution_probe.py
---

# K2311 Uniform constrained dust evolution

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
result: K2311
carrier: same fixed healthy four-dimensional designer dust and canonical scalar, mean-zero torus perturbations LAYER=toy CHIRALITY=N/A
pairing: positive weighted Fourier energy norm on the fixed constrained perturbation variables ON=declared_carrier
real_structure: real scalar and metric fields with conjugate Fourier modes
grading: scalar perturbations; no native Clifford identification
action_owner: repository-construction -- K2302 healthy action and K2308 full constrained equations, radiation absent
target: frequency-uniform mixed Sobolev evolution and controlled dust derivative loss MAP-TYPE=evaluation
```

## Fixed action and question

Keep exactly [K2308](k2308-inhomogeneous-constrained-dust-transfer-2026-10-30.md)'s conventional healthy designer action, smooth dust, beta=-1/(sqrt6 M), m=M²>0, d>0, q=k²/a², and no radiation. On any compact smooth background interval with a,d bounded away from zero, including its Einstein-frame H=0 turnaround, the question is spatial evolution rather than another fixed-k estimate. Spatial topology is a supplied flat torus; restrict to nonzero Fourier modes. The zero mode has separate gauge constraints.

Source SC-COS-50/51/54 remains ASSERTS; LT-GR2e remains NEEDS at ledger0.263. No physical initial spectrum or native GU action is supplied. The result below is linear conditional mathematics, not nonlinear stability, decay or caustic avoidance.

## Exact change of variables

Use K2308's Hamiltonian constraint to reconstruct n, and set

    W=chi-2beta m Phi, p=dot W, alpha=u/(2m), c=1+2beta²m.

The original constrained equations give

    Phi'=(-H+beta u)Phi-d v/(2m)+alpha W,
    v'=-c Phi-beta u v-beta W,
    W'=p,
    p'=-qW-3Hp+B W+C Phi+Dv,                        (1)

where

    B=2u²/m+4beta H u-V''+2beta V',
    D=-2ud/m-4beta H d,
    C=(4u+2beta mH)(-H+beta u)
      +2beta m(-V''+3beta H u+2beta V')
      -2V'-2beta d+2beta m(2H'+3H²).

Here H'=-(u²+d)/(2m). No H or2mq-u² division occurs. Define R=qPhi,S=qv and

    r=R+alpha p, s=S-beta p.                         (2)

Then qW cancels from r',s'. For an explicit implementation set

    F=-qW-3Hp+B W+[C(r-alpha p)+D(s+beta p)]/q.

With alpha'=(-3Hu-V'-beta d)/(2m), the full normal form is

    r'=(-3H+beta u)(r-alpha p)-d(s+beta p)/(2m)
           +alpha qW+alpha' p+alpha F,
    s'=-c(r-alpha p)-(2H+beta u)(s+beta p)
           -beta qW-beta F,
    W'=p, p'=F.                                    (3)

The apparent qW terms cancel exactly. Remaining coefficients are bounded background functions or their multiples by1/q. The changes are invertible at every nonzero k. Reconstruct Phi=(r-alpha p)/q, v=(s+beta p)/q, chi=W+2beta mPhi and pi=p+2beta mPhi'. K2308 reconstructs n without an H denominator and propagates its Hamiltonian constraint.

## Uniform estimate and its precise regularity

On the torus q>=q_min>0 throughout a compact interval. Set

    E_k=|r|²+|s|²+|p|²+(1+q)|W|².

In E_k', the terms -2q Re(conj(p)W) and+2q Re(conj(W)p) cancel; q'=-2Hq is bounded by2|H|E_k. All remaining cross terms in (3) are bounded by C_I E_k using2|ab|<=|a|²+|b|² and1/q<=1/q_min. Thus |E_k'|<=C_I E_k with C_I independent of k. Gronwall works in both time directions. Summing (1+|k|²)^s E_k gives a reversible continuous Fourier evolution in the mixed Sobolev space

    Phi,v in H^{s+2}; chi in H^{s+1}; pi,n in H^s,  (4)

with the constraint imposed. This follows by the bounded invertible transformations above and q comparable to |k|². Fourier truncation plus the uniform estimate gives existence/uniqueness and strong continuity. Physical dust velocity grad(v)/a has one extra derivative relative to n. The bound depends on the smooth background interval and q_min, not on k; it does not imply small amplification. It does not extend to arbitrary zero modes or assert a uniform infinite-time estimate.

## Released continuation: why the dust derivative allocation matters

At turnaround t*, take paired real Fourier modes |k|=N with initial Phi=chi=pi=n=0 and v=1/N. K2308's constraint holds exactly at H=0. Initial physical velocity amplitude is1/a*, uniformly bounded. Normalize r,s,W,p by N. Their normalized initial data are (alpha beta d/N²,a*^-2-beta²d/N²,0,beta d/N²), approaching (0,a*^-2,0,0) with O(N^-2) error: p_original=beta d/N and W_original=0; q=N²/a². The only wave forcing from the bounded slow sector is(Cr+Ds)/q=O(N^-2). Explicitly, E_w=|p|²+(1+q)|W|² obeys |E_w'|<=C_I E_w+|(Cr+Ds)/q|², with E_w(t*)=O(N^-4). The wave energy estimate with initial wave energy amplitude O(N^-2) yields |p|+sqrt(1+q)|W|=O(N^-2) for the normalized solution. The slow-sector difference then obeys a bounded-coefficient Gronwall estimate and is O(N^-2). This is uniform on the fixed interval: the full energy first bounds the slow sector independently of N, closing the forcing argument without assuming the limit.

The limiting slow system is

    r'=(-3H+beta u)r-ds/(2m),
    s'=-c r-(2H+beta u)s.

Reconstruction gives n_N/N -> delta=-2m r/d, and

    delta'=s,
    delta''+(2H+beta u)delta'-[c d/(2m)]delta=0,
    delta(t*)=0, delta'(t*)=a*^-2.                  (5)

For the fixed healthy beta, c d/(2m)=2d/(3m)>0. The integrating factor for (5) proves delta,delta'>0 forward from t*. With the inherited normalized fixture bounds |H|<1,|u|<4,|beta|<1/2, |2H+beta u|<4, so

    delta(t*+tau)>=a*^-2(1-exp(-4tau))/4.

At each fixed positive tau in the interval, density amplitude grows like N. Scaling v_N=N^{-(s+1)} provides bounded initial physical H^s velocity with final H^s density growing like N. Therefore equal-H^s density/physical-velocity evolution is not bounded. This is linear derivative loss, not a proof of nonlinear caustics. The mixed space(4) budgets it. Equation(5) is a controlled high-frequency gravitational-attraction limit, rather than a coordinate-dependent frozen-matrix eigenvalue assertion.

## Evidence and remaining physical input

The probe derives both transformations from the original constrained five-field equations, checks exact coefficients, q cancellation, energy cancellation, number reconstruction, limiting density equation and actual initial data. Changed coefficients or shifts must fail these same evaluators. Uniform estimates and Fourier limits use the explicit proof above, not sampled k values.

Next supply physical constrained initial statistics and a windowed observable transfer on this action, or a genuine nonlinear dust construction with its caustic domain. Neither is fixed by linear regularity or by rebranding the Jeans limit as a GU prediction. Source, ledger, canon and empirical verdicts remain unchanged.
