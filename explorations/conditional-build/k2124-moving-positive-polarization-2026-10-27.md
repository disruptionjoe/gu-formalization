---
title: "K2124: Moving positive sectors, exact leakage and holonomy"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no source selection, physical GU quotient, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k2124_moving_positive_polarization_probe.py
---

# K2124: Moving positive sectors, exact leakage and holonomy

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
result: conditional exact construction with explicit domain and inference limits
carrier: K2120 complex128 with its actual maximal positive32 family LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: the unchanged inherited S=iF, with Ptheta S Ptheta=9 Ptheta/280 ON=declared_carrier
real_structure: complex Hilbert adjoint; no source-selected physical reality
grading: Clifford labels, current sign and CAR parity are separate
action_owner: repository-construction -- fixed K2028 image first; explicitly enlarged Z connection second
target: conditional dynamics and operational compatibility MAP-TYPE=intertwiner
```

## Result

The constant survivors of [K2123](k2123-same-current-potential-dynamics-2026-10-27.md)
cannot be turned into a freely varying full32 subbundle using K2028's frozen
whole128-preserving raw coefficient class. The leakage has exact squared
Hilbert-Schmidt norm8(theta_t²+|grad theta|²). There is a concrete compatible
connection repair preserving the SAME current, but its nontrivial part is
outside that class. This separates a scoped obstruction from a universal
observation or positivity claim. A flat global example has nontrivial boundary
holonomy, which the local repair does not erase.

## 1. Full-bundle leakage, including null gradients

Let Utheta=exp(i theta Z/2), Ptheta=Utheta P0 Utheta*, theta smooth real.
The original K2120 identities give [Z,F]=[Z,Cj]=[Z,M]=0 and Ptheta Z Ptheta=0.
Differentiating Ptheta and applying it on the right yields

    L=(partial_t Ptheta+Cj partial_j Ptheta)Ptheta
      =(i/2)Z(theta_t I+Cj theta_j)Ptheta.                       (1)

For a section phi=Ptheta phi, (1) is precisely the off-bundle part of the
spacetime derivative. The mass and K2028 potential commute with Ptheta,
so they cannot cancel it. Invariance for arbitrary compact initial data in
the entire32-dimensional fibre requires L=0 pointwise, not just Lphi=0
for one selected solution.

Set B=theta_t I+Cj theta_j. Clifford relations give
B²=(theta_t²+|grad theta|²)I+2theta_t Cj theta_j.
Since M commutes with Ptheta and anticommutes with Cj, tr(Ptheta Cj)=0.
Thus

    ||L||_HS²=(1/4)tr(Ptheta B²)
             =8(theta_t²+|grad theta|²).                        (2)

This is a positive Euclidean sum, despite the Lorentzian-looking derivative.
Even a nonzero null gradient cannot preserve the full32 bundle. Some smaller
kernels at characteristic gradients may survive; (2) does not exclude them.
On a connected patch the entire frozen image works iff theta is constant.
The conclusion exhausts ONLY the K2028 whole128-preserving/conservative class.
Raw coefficients preserving only32 while leaking from its128 complement were
not classified there and remain an especially concrete next alternative.

## 2. Explicit changed-class repair and time term

Supply

    Gamma_mu=i a_mu I-(i/2)theta_mu Z.

It is anti-Hermitian and S-compatible: Gamma_mu* S+S Gamma_mu=0.
It obeys partial_mu Ptheta+[Gamma_mu,Ptheta]=0 and

    E_Gamma=partial_t+Gamma_0+Cj(partial_j+Gamma_j)+mu M
           =Utheta E_a Utheta*.                                 (3)

These equalities also prove the full32 propagated-bundle result. The new
coefficient -(i/2)Z(theta_t I+C.grad theta) is trace-orthogonal to
 i span_R{I,C1,C2,C3}. Exact original matrices give
tr(A Z B)=0 for all A,B in {I,C1,C2,C3}; its Hilbert-Schmidt norm squared is
32(theta_t²+|grad theta|²). It is nonzero outside the old image whenever
dtheta is nonzero. This statement does not forbid a DIFFERENT raw class
or transformed full construction; it rules out silently calling the repair
an element of the already frozen class.

For static theta with bounded derivatives, Utheta is a unitary H1 multiplier
and Htheta=Utheta H_a Utheta* is selfadjoint on Utheta H1 (equal to H1 as an
ambient function space, with range in the moving bundle). For time-dependent
theta one must include

    Htheta(t)=Utheta H_a(t) Utheta* - theta_t Z/2.                 (4)

The propagator is Utheta(t) U_a(t,s) Utheta(s)*, with the regularity conditions
of K2123 and bounded first spatial/time derivatives for the multiplier.
Omitting the last term in (4) is an actual wrong equation, not a gauge choice.
The scalar curvature is i da; the Z term is pure gauge locally. This gives
curved examples by combining the repair with K2123's bounded nonflat a.

## 3. A global domain consequence: flat is not globally removable

On a circle of length L take theta(x)=2pi n x/L, n integer, and a=0.
Ptheta is periodic, whereas Utheta(x+L)=(-1)^n Utheta(x). The connection
Gamma_x=-i pi n Z/L is flat, with parallel holonomy(-1)^n I.
Periodic physical sections phi correspond to transformed sections
psi=Utheta*phi with psi(L)=(-1)^n psi(0). For the one-spatial-direction massive
equation (other momenta zero), therefore,

    p_k=2pi(k+n/2)/L,
    energies=+/-sqrt(mu²+p_k²).                                  (5)

This is a boundary-condition shift, not dynamically generated mass. The
bundle itself is trivial: Vtheta=Utheta exp(-i theta/2) is periodic, supplies
a periodic frame of the selected bundle, and leaves residual scalar
connection -i dtheta/2. Adding a scalar a changes holonomy to
(-1)^n exp(-i integral a). Setting the local curvature to zero does not
justify discarding the holonomy or choosing periodic transformed boundary data.

## Prior and strongest contrary route

K2028 already proves smooth lifts, and K2034 constructs a changed positive
form with supplied curved connections. The new statements concern the SAME
K2120 inherited current, exact full32 varying-selector leakage and a specified
changed-class repair/global domain. The strongest contrary route is a raw
coefficient preserving only the selected32; it is not covered by this result.
Full1920 Jordan and mass defects remain. Constant family choice, complex
rather than real positive sector, and source selection remain explicit imports.


## Source and acceptance boundary

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 and SC-META-53 are
UNCERTAIN; SC-META-56 DISAVOWS an odd-action prerequisite. Their polarity and
adherence remain unchanged. LT-SM8/LT-GR6b and ledger0.263 remain unchanged:
these conditional constructions are neither source-selected interacting physical
quotients nor recovered GU physics. Native2+1, total/observed chirality,
full20, K/C, mirror/full-II and normal jets remain distinct debts.

Exact finite probes and genuine input faults test the displayed identities.
Universal domain, causal and global claims rest on the written arguments and
independent internal specialist review, not the finite checks. No external
expert, proof-assistant or novelty certification is claimed.
