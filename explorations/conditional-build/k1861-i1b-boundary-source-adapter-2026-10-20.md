---
title: "K1861: global source range and boundary flux for the horizontal I1B metric-row control"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact horizontal equation-dual control; no full native distortion injection or global I1B realization
---

# Conservation, zero modes and null resonance are separate source conditions

The horizontal curvature block held by K129 can be placed on explicit periodic
and bounded domains and its source range determined. On a flat **Euclidean**
four-torus, a symmetric source is in the range precisely when it is
divergence-free and has zero mean. On a flat Lorentzian torus, conservation is
not sufficient at a null Fourier mode: two transverse traceless source
components must also vanish. A polynomial bounded-domain response realizes
K1860's exact scale-flux budget, while a variable pure-volume source fails
the local divergence identity even before the zero-mode test.

**This is an equation-dual quadratic control, not the completed source
adapter.** Its symmetric multiplier `t` is paired with the horizontal
curvature row. Identifying it with a component of native augmented distortion
`T=varpi-B_LC(g)` requires a pairing-preserving dual injection, the full
Clifford/field equations, observation and ambient-domain construction. Those
are not supplied here. The bounded-domain witness solves the metric row;
it does not solve the independent distortion row `Ah+Ct=0`.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: complete flat periodic metric-row source range and exact bounded-domain scale flux
carrier: real symmetric two-tensors on a supplied flat four-dimensional domain LAYER=observed BRIDGE=conditional-horizontal-equation-dual-control CHIRALITY=N/A; injection into full native distortion and global ambient action remains unconstructed
pairing: integral of t^{ab}(Ah)_{ab} using the fixed flat metric and density ON=real_symmetric_tensors
real_structure: real Euclidean control or explicitly separate real Lorentzian control; Fourier coefficients obey conjugate symmetry
grading: horizontal metric row versus equation-dual multiplier; differential order two; no particle grading
action_owner: repository-construction -- horizontal quadratic control using the held K129 curvature block; not a global GU action
target: range of a specified linear metric-row operator and its boundary flux MAP-TYPE=evaluation
```

## 1. Custody and the question actually resolved

[K127](selected-k127-native-i1b-ricci-flat-weyl-tt-closure-gate-2026-08-16.md)
owns local Ricci-flat zero-distortion stationary germs;
[K128](selected-k128-native-i1b-t0-coupled-hessian-and-schur-domain-gate-2026-08-16.md)
owns the coupled Hessian `[[0,A*],[A,C]]`, with zero pure-metric block;
[K129](selected-k129-native-i1b-t0-ac-kernel-and-domain-classification-2026-08-16.md)
identifies its horizontal curvature block with `A=-2G'` in the stated
normalization. [K1860](k1860-i1b-vacuum-zero-mode-2026-10-20.md) proves a
conditional scale compatibility theorem but leaves the global domain and
observed-volume coupling unconstructed.

The new question is whether a concrete domain or a source with its mean
removed suffices to satisfy that **one** metric row. This is consequential
before attempting a full `C` inverse: a failed necessary row cannot be fixed
by choosing that inverse, while a passing row does not establish the rest of
the Hessian equation. It is not a new Einstein-Hilbert term in GU.

The control functional is

```
Q(h,t)=integral t^{ab}(Ah)_{ab} + (1/2)<t,Ct> + <J,h>,
```

with no claim that a chosen `C` is the native one. The first Euler row is
`At+J=0`; flat `A` is formally self-adjoint under this tensor pairing.
The remaining Euler row is not discarded as a source-theory equation.

SC-ACT-01/02 and SC-COS-50/51/54 remain ASSERTS, and SC-META-53 remains
UNCERTAIN. ACT01 owns the full torsion/Shiab action and its one-half and
one-third terms; ACT02's annotated Einstein-like row is not a published
observed-volume matter coupling. COS54 is the registered paraphrase with
its unidentified curvature-field caveat. Source adherence is not validation.
Ledger v0.263 retains 88 active targets and 91 stored records; LT-GR1b's
post-Shiab factorization restriction and LT-GR2c/2d/6b, LT-SM8 are unchanged.

Preflight compared a full ambient `Y=Met(X)` construction, a new Schur
inverse, and direct source-range analysis. The global construction remains
the stronger eventual consumer, but a flat horizontal domain is not its
substitute. Source criticism, variational analysis, Fourier/PDE analysis
and boundary geometry selected the last route because it settles three
independent necessary conditions without fitting `C`. Retrieval checked
K127--129, K1860, the existing global-projector branch and the correction
index: none supplied this complete source range. No novelty is claimed.

## 2. The actual operator and its symbol

Let `eta=diag(1,1,1,1)` or separately `diag(-1,1,1,1)`. Raise indices with
eta, set `tau=eta^{ab}t_ab`, and define `A=-2G'_eta`. For a Fourier
covector k, let `u_b=k^a t_ab`, `s=k^a u_a`, and `q=k^a k_a`. Then

```
(A(k)t)_ab = -q t_ab - k_a k_b tau + k_a u_b + k_b u_a
             + eta_ab(q tau-s).                         (1)
```

Direct contraction proves `k^a(A(k)t)_ab=0`. Gauge tensors
`t_ab=k_a z_b+k_b z_a` lie in the kernel. For q nonzero the kernel is
exactly these four directions, the rank is six, and the range is exactly
the six-dimensional conserved-source subspace. This also follows from the
explicit right inverse below, rather than a rank count alone.

In real space, the trace supplies the scale Green identity

```
2 eta^{ab}(At)_ab = partial_mu j^mu,
j^mu=4(partial_nu t^{mu nu}-partial^mu tau).             (2)
```

The factor two is the scale tangent `delta g=2eta`, not a different
normalization of volume. Equations (1)--(2) are tensor identities for the
declared flat operator; no compactness or source ownership is inferred.

## 3. Complete Euclidean periodic range and a constructive inverse

Take the flat Euclidean torus `(R/2pi Z)^4`. For a distributional symmetric
source J, a distributional periodic solution of `At=-J` exists if and only if

```
integral J=0 componentwise,       partial^a J_ab=0.       (3)
```

Necessity follows from the derivative-only operator and its divergence
identity. For sufficiency set the zero Fourier mode of t to zero and, for
every nonzero integer k, use

```
t_hat_ab(k) = [J_hat_ab(k) - (1/2)eta_ab tr J_hat(k)]/|k|^2.  (4)
```

Conservation gives `k^a t_hat_ab=(1/2)k_b tr t_hat`.
Substitution in (1) yields `At_hat=-J_hat`, proving sufficiency for
distributions as well as smooth fields. The matrix trace reversal in four
dimensions is an orthogonal involution for the Euclidean Frobenius norm.
For the standard inhomogeneous Fourier Sobolev norm, `|k|>=1` therefore gives

```
||t||_{H^{r+2}} <= 2 ||J||_{H^r},                      (5)
```

for every real r. This estimate is a Euclidean elliptic control only.
Solutions differ by arbitrary constant tensors and the gauge kernel at
nonzero modes. Formula (4) chooses a representative, not a physical quotient.

An explicit positive control uses `k=(1,0,0,0)` and
`J=diag(0,1,1,1) cos(x0)`. Equation (4) gives
`t=diag(-3/2,-1/2,-1/2,-1/2) cos(x0)`. It solves the metric row and has zero
mean, without claiming stationarity of the other row.

For a pure volume source `J=(rho(x)/2)eta`, conservation forces
`partial_b rho=0`. On a connected periodic domain rho is constant, and the
zero-mean requirement then forces rho=0. Thus merely subtracting the mean of
a nonconstant scalar source does **not** create an admissible source. Extra
stress components or other equations must account for its divergence. This
does not prohibit a complete covariantly conserved matter stress tensor.

## 4. Lorentzian null resonance: conservation alone fails

Keep real Lorentzian eta and a supplied periodic coordinate domain. This is
an algebraic Fourier control, not a causal spacetime proposal. For nonnull
k, (4) with denominator q still solves the conserved-source row. No elliptic
Sobolev estimate or global causal inverse is transferred.

For nonzero null k, (1) instead has the exact range

```
Range A(k) = { k_a w_b+k_b w_a-eta_ab(k^c w_c) : w in R^4 }.  (6)
```

The inclusion follows by taking `w=u-(tau/2)k` in (1). For the reverse
inclusion choose a null covector l with `k·l=1` and put

```
t_ab=l_a w_b+l_b w_a-(k·w)l_a l_b-(l·w)eta_ab.           (7)
```

Direct substitution yields (6). The map w to (6) is injective: its trace
fixes `k·w`, contraction with l fixes w up to k, and its l,l contraction
fixes that last coefficient. Hence the rank is four. In a null frame with
`k=(1,0,0,1)`, the conserved-source space has dimension six; membership adds
exactly

```
J_11-J_22=0,                 J_12=0.                   (8)
```

Indeed (6) obeys (8); independence of the two transverse traceless
conditions and the dimensions establish the converse on conserved sources.
The source `diag(0,1,-1,0) cos(x0+x3)` is conserved, real and zero mean,
but violates (8). It has no periodic solution to this metric row. The two
missing source directions are an operator-range condition, not a claim of
two physical particles or a source-GU falsification. Nonperiodic secular
responses or different boundary data change the domain question.

## 5. A bounded-domain response pays the exact scale-flux budget

On a coordinate box in either signature set `r2=eta_ab x^a x^b` and

```
t_ab=(r2/24)eta_ab,          J_ab=(1/2)eta_ab.           (9)
```

For `t=f eta`, the real-space operator is
`At=2(partial_a partial_b f-eta_ab Box f)`.
Since `partial_a partial_b r2=2eta_ab` and `Box r2=8`, (9) gives
`At=-eta/2`. Equation (2) gives `j^mu=-x^mu`, so the directed boundary
integral is exactly

```
integral_boundary j = -4 Volume(box).                  (10)
```

Use directed coordinate surface measure, which does not require a unit
normal on a null face. This realizes K1860's required first-row flux and
shows that the periodic obstruction does not prohibit a bulk solution with
boundary flux. It selects neither a boundary action nor a closed Hessian
domain; (9) generally violates periodic or fixed multiplier data. Its
native distortion injection and the coupled row remain unbuilt.

## 6. Hostile review and consequence

The strongest overclaim would be a global source-action solution or a GU
screening verdict. The equation-dual injection, complete adjacent-grade C
row, ambient gimmel geometry, observation map and boundary action are
explicit missing premises. A flat base does not make the full metric-bundle
geometry flat. Indefinite geometry is not replaced by the Euclidean control.

The strongest contrary route is a different boundary ensemble: (9)--(10)
show that it can change the first-row answer. It must still satisfy the full
action. A second contrary route is a conserved non-pure-volume stress:
(3)--(4) construct its Euclidean response. A third is Lorentzian resonance:
(6)--(8) demonstrate why a conservation-only adapter fails.

Exact rational checks cover the symbol, gauge and conservation identities,
nonnull inverse, null range/right inverse, null counterexample, independent
Ricci derivation, polynomial response and flux. Mutation tests start from a
clean baseline and count only failed mathematical assertions. They do not
certify an unconstructed field-theory map. The written Fourier proof owns
the distributional and Sobolev statements; no proof assistant, external
expert acceptance or novelty is claimed.

The next substantive native step is to construct the pairing-preserving
injection into full source distortion and evaluate the complete companion
equation and boundary variation on that same object. If it leaks out of the
horizontal control, enlarge from the actual action rather than fitting a
projector. Repeating a zero-mode test or a conservation-only source repair
cannot discharge that dependency. All ledger, canon and source polarities
remain unchanged.

Reproduce:

```
python3 tests/channel-swings/k1861_i1b_boundary_source_adapter.py
python3 tests/channel-swings/k1861_i1b_boundary_source_adapter_probe.py
```
