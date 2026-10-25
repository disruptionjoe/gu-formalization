---
title: "K2071: Confined pointer control with quantified sector and detector error"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional complex Dirac graph, supplied tensor preparation and approximate sector; no source or detector-field realization
scripts:
  - tests/channel-swings/k2071_confined_pointer_control.py
  - tests/channel-swings/k2071_confined_pointer_control_probe.py
---

# K2071: Confined pointer control with quantified sector and detector error

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
result: compact spatial control and finite detector approximating the same positive-sector prepared pointer
carrier: full complex Dirac1408 Hilbert carrier with fixed massive projector P LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: positive L2 norm and imported Born probabilities ON=declared_complex_completion
real_structure: complex completion; source real/dual apparatus compatibility unproved
grading: fixed free energy sign and supplied multiplicity qubit
action_owner: repository-construction -- symmetrized spatial cutoff of the declared pointer
target: quantitative prepared-subspace comparison MAP-TYPE=intertwiner
```

[Verified conditional mathematics.] Compactly supported spatial controls can approximate
K2069's homogeneous speed-one pointer on its SAME preparations, with explicit error
bounds that include a finite detector and every outcome. The cost is a large controlled
region and loss of exact intermediate positive-sector preservation. This supplies an
approximate-sector construction, not a source-selected physical quotient or a local
quantum-field detector model. The finite propagation/truncation argument is standard;
no novelty is asserted.

## 1. Fixed carrier, control and domain

Reuse H0=alpha.D+m beta, m>0, on L2(R3,C4 tensor C352), with
C352=C2 tensor C176 and fixed P=1_(H0>0). K2067 supplies the normalized spatial spinor
phi with s=m and each coordinate second moment <=17/(4m^2). K2069 supplies
Hstar=(2/3)H0+(1/3)D1 Z, duration T=30/m, and preparation
psi=exp(iH0*20/m)phi tensor v for arbitrary internal qubit v. Changing the setting
uses Z_n=n.sigma IN THE CONTROL; no spatially homogeneous preliminary rotation is
required. The preparation is setting-independent, including for entangled qubits.

SC-OP-04 ASSERTS the candidate four-field grammar; SC-OP-05 is UNCERTAIN about rival
southeast maps; SC-META-53 is UNCERTAIN about physical positivity; SC-META-56 DISAVOWS
an odd-action prerequisite. None supplies this complex Hilbert, tensor, Born or
apparatus completion. LT-SM8/GR6b, source register, ledger and canon are unchanged.

Choose smooth chi with 0<=chi<=1, chi=1 on B_(L+T+rho), chi=0 outside
B_(L+T+2rho), rho>0. During the pulse define

    Hchi = H0 + {chi,Hstar-H0}/2.                       (1)

This symmetric ordering is essential. In differential form its principal coefficients
are A_j=(1-chi/3)alpha_j+(chi/3)delta_(j1)Z_n, its mass coefficient is
(1-chi/3)m beta, and it includes -i/2 sum_j partial_j A_j. Omitting this last term
would destroy symmetry. For each unit covector e its principal eigenvalues are
+/-(1-chi/3) +/-(chi/3)e1; thus ||A(e)||<=1 everywhere and their absolute values
are >=1/3. Coefficients are smooth, bounded, with bounded derivatives. The formally
symmetric first-order operator on Cc-infinity is essentially self-adjoint and its
unitary evolution has speed at most1. One can obtain these statements from smooth
symmetric-hyperbolic existence, the energy estimate and the complete Euclidean metric;
Chernoff's theorem is the standard self-adjointness result being used. The pulse
uses its self-adjoint closure, followed by free evolution, not an unspecified
self-adjoint extension. We do not require a positive lower bound on the full carrier.

At a boundary with outward normal e the current is psi* A(e) psi, whose absolute
value is at most the density. Integrating outside an expanding speed-one ball gives
the support bound. The same estimate gives uniqueness in a backward cone. A
piecewise constant time switch at0,T is a product of these unitary groups; it needs
no asserted differentiability in time. Smooth temporal versions require their own
common preparation time integral, as in K2069.

## 2. Exact causal-tube comparison, not derivative perturbation

Let Uchi(t) and Ustar(t) be the two evolutions during the pulse. For ANY initial f
supported in B_L, they agree for0<=t<=T: its support stays inside B_(L+t), where
all coefficients and their derivatives agree, so uniqueness identifies the solutions.
Approximate a nonsmooth truncated f in L2 by smooth compactly supported data to
extend this equality; no H1 property of a sharp cutoff is being assumed.

For normalized psi let eta=||1_(outside B_L)psi||. Decompose into inside and outside
pieces WITHOUT renormalizing. Unitarity on the two outside pieces gives

    ||(Uchi(t)-Ustar(t))psi|| <= 2 eta,   0<=t<=T.      (2)

This holds uniformly on the prepared qubit subspace and with any untouched ancilla,
because the spatial preparation is common. Since Ustar commutes with P and psi lies
in Ran P,

    ||(1-P)Uchi(t)psi||^2 <=4 eta^2.                  (3)

This is a probability bound on this preparation, not a uniform operator bound,
exact P-invariance, an interacting positive Hamiltonian or a bound on negative-energy
expectation. Small probability alone does not control an unbounded energy observable.

The mechanism is not the bounded-local rigidity result of K2062: (1) changes the
principal differential coefficients, and exact sector preservation has been relaxed.
The normalized kinetic trace calibration also changes inside the pulse.

## 3. An explicit radius from the same Gaussian preparation

For the free Dirac evolution, q(t)=|| |x| exp(-itH0)phi || obeys
|q'(t)|<=1, by differentiating the second moment and using
||alpha.x phi||=|| |x|phi ||. Approximation justifies the calculation on the
Schwartz state. Therefore

    q(0 for psi) <= (sqrt(51)/2+20)/m <24/m,
    eta <= q/L <24/(m L).                            (4)

The bound is deliberately conservative. With L=2400/m and rho=1/m one has
eta<=1/100, detector radius L+T=2430/m and control support radius2432/m.
The fixed free mean energy of the initial preparation remains <=2m by K2067.
No claim is made that this enormous sufficient apparatus radius is minimal or that
its external control has a source-derived energy budget.

## 4. Finite detector, no postselection, Bell consequence

Read the sign of x1 only within the detector ball B_(L+T). Assign the outside outcome
the fixed value+1. This is a complete bounded observable, including every no-click
event. For BOTH evolutions, the norm outside the detector ball is at most eta:
the inside initial piece has exact support there and the outside piece has norm eta.
Thus the no-click probability is <=eta^2 at either laboratory.

For two supplied tensor copies with a multiplicity singlet, use the usual four axes.
Each local evolution differs from its homogeneous reference by <=2eta on the entire
prepared subspace. The joint evolved vectors differ by <=4eta by telescoping,
including entanglement. The expectation of any norm-one correlator changes by
<=8eta. Replacing infinite sign readout by the finite detector changes each ideal
correlator by at most2 times the probability that either detector misses, hence
<=4eta^2. Summing the four correlations gives

    S_confined >= 2 sqrt(2)(183/200)^2 -32eta-16eta^2. (5)

At eta=1/100 the right side exceeds2. This is a sufficient prepared-state bound;
no fair-sampling or click-conditioned correlation is used. A simple entirely rational
check uses sqrt(2)>7/5 and proves the stricter lower bound
2*(7/5)*(183/200)^2-32/100-16/10000>2.

Writing c=2*(7/5)*(183/200)^2-2, the sufficient Bell criterion is
eta<sqrt(1+c/16)-1. With eta<=24/(mL), this yields an explicit radius
threshold for this conservative certificate. It is not an optimal detector radius.

The same error budget extends to N supplied factors: joint vector error <=2N eta,
so any norm-one joint observable changes by <=4N eta, and finite detector replacement
adds <=2N eta^2. For unequal radii substitute sum_i eta_i. This useful composition
is a telescoping argument, not a new many-body interaction theorem.

## 5. Spatial separation and the remaining physical bridge

Translate the two preparations, controls and detectors to centers at distance
D>2(L+T+2rho)+T. Their whole control cylinders during[0,T] are spacelike separated
for speed1. For the explicit numbers D>4894/m suffices. The initial states still
have noncompact tails. Tensor-factor commutation and the supplied entangled
preparation give the stated mathematical correlations; they do not derive a local
field algebra, detector-field interaction, source-real observable or preparation
procedure. No claim of experimentally realized spacelike laboratories follows.

This closes the previously unbuilt confined-control/finite-detector approximation
on the declared model. The remaining strong version needs a source-compatible
field/detector algebra or a tighter physical resource and preparation criterion.
Repeating a homogeneous time rescaling or claiming exact sector preservation is not
that successor. Approximate errors can be made arbitrarily small by increasing L;
the construction neither defeats positive-energy localization theorems nor
establishes optimal radii.

## 6. Evidence and review

The written symmetric-hyperbolic, truncation, moment and telescoping proofs carry the
continuous statements. The producer checks exact rational radius, cone, leakage and
Bell resource identities. A separate probe checks rational budgets and finite-vector
truncation and tensor union-bound controls and rejects forged leakage, detector and
Bell margins. These are finite controls, not discretized proofs of the PDE. Prior
1408 graph, Gaussian spinor and ideal readout evidence is hash-pinned reuse. Same-author
checking only; no independent specialist, proof-assistant or novelty certification.

Strongest overclaim: low leakage probability does not restore a lower-bounded sector
Hamiltonian. Strongest contrary case: translating a positive-energy state far outside
the control region defeats uniform approximation. Weakest propagation seam: a finite
matrix test cannot establish continuum finite speed; that is supplied by the stated
symmetric-hyperbolic hypotheses, with the derivative-of-cutoff term retained.

Reference: Paul R. Chernoff, [Essential self-adjointness of powers of generators of
hyperbolic equations](https://www.sciencedirect.com/science/article/pii/0022123673900037),
Journal of Functional Analysis12(1973),401-414. The existing K2067/K2069 notes own the
prepared pointer and localization caveats; their formulas are reused explicitly.
