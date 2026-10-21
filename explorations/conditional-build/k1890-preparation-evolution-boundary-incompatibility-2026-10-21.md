---
title: "K1890: Preparation support and conservative evolution require different boundaries"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional compressed-system mathematics on the stated slab and domains; no native GU identification or physical boundary selection
scripts:
  - tests/channel-swings/k1890_preparation_evolution_boundary_incompatibility.py
  - tests/channel-swings/k1890_preparation_evolution_boundary_incompatibility_probe.py
---

# K1890: Preparation support and conservative evolution require different boundaries

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
result: exact incompatibility and sharp relaxation of preparation traces for conservative evolution
carrier: conditional real16 source with real4 observation on an interval or fixed tangential Fourier mode LAYER=toy CHIRALITY=N/A
pairing: positive H bulk energy and indefinite normal flux F=H*A1 ON=H1_boundary_trace_domain
real_structure: real local boundary subspaces, complex Fourier fibers with conjugate symmetry
grading: incoming/outgoing characteristic flux, not observed particle chirality
action_owner: repository-construction -- fixed conditional conservative source equations
target: zero-observation-flux preparation domain versus skew-adjoint evolution domain MAP-TYPE=restriction
```

## 1. Scope and the independent question

[K1888](k1888-bounded-support-energy-inverse-2026-10-21.md) carefully calls
its domain a preparation domain. This result determines why it cannot simply
be promoted to conservative source evolution. Work with the constant
compressed source system `partial_t psi+sum A_i partial_i psi+C psi=0`,
where H>0, HA_i is symmetric and HC is skew. Use a normal interval
(-L,L), either alone or at each Fourier momentum of a transversely periodic
slab. C is any fixed admitted H-skew coefficient; its value does not affect
the boundary form. These are finite interval / modewise statements. No
classification of arbitrary tangentially nonlocal boundary operators,
additional boundary degrees of freedom or physical GU walls is asserted.

The actual data are K1832's real16 source with positive H, K1836's
real4 observation, and K1888's flux Gram. SC-OP-04 ASSERTS candidate
four-field grammar; SC-MAS-01 and SC-CHI-02 ASSERTS a stylized curvature-mass
toy. SC-OP-05 and SC-META-53 remain UNCERTAIN. These matrices are a
repository conditional construction, not the source's unconstructed full20
placement/injection/reality/pairing/domain adapter. RA-F1, AC-F1, LT-SM8,
source, physics-ledger and canon verdicts do not change.

## 2. Exact normal flux splitting

For one face normal to coordinate1 define

```
F=H A1, T=T1, N=ker T, V=F^-1 T^T,
alpha=138/25, d1=D1/24.
```

The actual four coordinate types all satisfy

```
T A1=d1 T, T H^-1 T^T=alpha I,
spec(A1)={+1 (6),-1 (6),+1/24 (2),-1/24 (2)},
Q=T F^-1 T^T=24 alpha D1, spec(D1)={+1 (2),-1 (2)}.          (1)
```

Because A1 is H-self-adjoint, the energy boundary form F has inertia(8,8).
The image of V is its orthogonal complement to N: `n^T F V=n^T T^T=0`.
Q is invertible, so this is a direct nondegenerate splitting, and the form
on im V has inertia(2,2). Sylvester inertia subtraction gives

```
dim N=12, inertia(F|N)=(6,6), largest isotropic dimension=6. (2)
```

There is a still simpler constructive check. The +/-1 eigenspaces of A1
have dimensions6 each and are annihilated by T: equation (1) forces
T psi=0 whenever A1 psi=+/-psi, since +/-1 is not an eigenvalue of d1.
Their direct sum is N. Any nonzero +1 vector has positive F flux despite
T psi=0; a -1 vector has negative flux. The producer serializes one of each
in every coordinate type. These are actual source vectors, not dimension
counts on an imported model.

## 3. Zero observation flux is not an energy-conserving boundary

Integration by parts for the source generator G=-A1 d/dx1-C gives

```
<phi,G psi>H+<G phi,psi>H=-[phi^* F psi]_-L^L.              (3)
```

The preparation condition T psi=0 allows every trace in N. Equation (2)
and the explicit witnesses show that (3) does not vanish. Multiplying a
witness by a smooth scalar profile equal1 at one endpoint and0 at the other
produces an actual H1 test with nonzero energy flux. Its source trace obeys
the preparation boundary, so the preparation realization is not even
skew-symmetric as an evolution generator. The source energy derivative is
`d ||psi||H^2/dt=-[psi^*F psi]`, when a smooth solution exists.
This does not invalidate the preparation graph closure or its minimum-energy
inverse, whose boundary form concerns O rather than G.

Adding MORE homogeneous trace constraints while retaining T psi=0 cannot
produce a skew-adjoint finite-interval evolution extension. At a separated
face, a self-orthogonal subspace for a nondegenerate(8,8) form must have
dimension8. Any isotropic subspace inside N has dimension at most6.
There is a deficit of two allowed boundary directions at each face.

Even coupling the two endpoints does not remove this obstruction in the
one-dimensional or fixed-Fourier-mode problem. The full trace form is
`diag(-F,F)` with inertia(16,16); its self-orthogonal subspace has dimension16.
The exact zero-flux trace space N x N has restricted inertia(12,12), so an
isotropic subspace inside it has dimension at most12. Thus no unitary
realization containing the minimal differential operator can have all its
endpoint traces in N x N. Boundary trace surjectivity of H1 and integration
by parts identify the adjoint domain with the form-orthogonal trace space;
this proves the dimension requirement directly.

The elementary boundary-space method is standard; see
[Schubert, Seifert, Voigt and Waurick](https://arxiv.org/abs/1308.2635).
Their abstract/graph context is background, not a substitute for (1)--(3).
No unrestricted infinite-dimensional tangential mixing conclusion is inferred
from these finite-dimensional counts. No claim about dissipative, constrained
subsystem or enlarged-boundary dynamics is needed here.

## 4. Sharp minimum relaxation and an explicit conservative repair

Let L_b be any separated energy-conserving self-orthogonal trace subspace.
Its dimension is8 and `L_b intersect N` is isotropic inside N, hence

```
rank(T|L_b)=8-dim(L_b intersect N)>=2.                     (4)
```

The bound is sharp. Choose H-orthonormal bases P_+,P_- of the six-dimensional
fast eigenspaces A1=+1,-1. Choose H-orthonormal bases S_+,S_- of the
two-dimensional slow eigenspaces A1=+1/24,-1/24. The columns

```
P_+ + P_-,        sqrt(24)(S_+ + S_-)
```

span an8-dimensional isotropic subspace L_b. Cross terms vanish by
H-self-adjointness and distinct eigenvalues. The fast sums have zero T image;
the two slow sums have independent T images because T is injective on each
slow eigenspace and those images lie in complementary +/- eigenspaces of D1.
Thus rank(T|L_b)=2 exactly. More generally independently pair positive and
negative flux-normalized fast and slow bases by arbitrary orthogonal matrices.
This exhibits a family of minimal relaxations, not a unique selected boundary.
The probe constructs the bases from the actual rational matrices using
Cholesky factors, verifies exact cancellation and rank for all four types.

Impose such a subspace separately at each endpoint. The finite-interval
operator has a skew-adjoint realization: the domain is H1 with these trace
constraints; (3) identifies its adjoint trace space, equal to itself.
Tangential Fourier coefficients and constant C add bounded H-skew matrices
to each normal operator, preserving skew-adjointness. The direct sum of these
fiber generators, on its natural square-summable graph domain, supplies a
unitary slab source evolution. This proves existence for the repaired boundary,
not for the old preparation boundary. This alone does not prove that O maps the new domain into a target Dirac
domain; section5 supplies that additional construction in the massless normal case.

For general modewise endpoint coupling the same rank-nullity argument gives
`rank(diag(T,T)|L_total)>=16-12=4`, sharp using the two separated repairs.
The still simpler periodic endpoint condition psi(L)=psi(-L) is conservative,
as (3) cancels; it has rank4 under diag(T,T). It allows ordinary nonzero
observation flux at each face and joins the faces, so it is not support
confinement. Its different topology must not be called a repair preserving
all original assumptions.

## 5. A complete massless normal-mode dynamical repair

The first useful domain successor can be solved without claiming the massive
or tangential problem. Set R=0, C=0, tangential momentum p=0, and use the
same separated reflection at both endpoints from section4. Then S=0 and
`O=T d/dx1`. Let W=T L_b, a two-dimensional target subspace. It is
D1-isotropic, so `D1 W=W-perp` in the Euclidean target pairing.
Use source trace L_b and target trace W-perp at BOTH endpoints.

The source fast characteristic sector lies in ker T and remains invariant.
On the slow sector T is a scaled isometry:
`||T psi||^2=alpha ||psi||H^2`, and its inverse is
`H^-1 T^T/alpha`. This follows from T H^-1 T^T=alpha I and the
H-orthogonal fast/slow decomposition. The source-observed variable f=T psi
therefore solves `f_t=-(D1/24)f'` with f endpoint traces in W.
Its derivative y=f' solves the same target equation. For a smooth invariant
source core, f_t has endpoint traces in W, so
`y=-24D1 f_t` has endpoint traces in W-perp. Thus the derivative observation
has the CORRECT target boundary; imposing W on both f and y would fail.

This core and its closure can be described exactly. Put xi=x1+L and
`k_n=n pi/(2L)`. For a in W, complex standing waves

```
f_n(x1)=cos(k_n xi)a+i sin(k_n xi)D1 a, n in Z,
G f_n=-(i k_n/24)f_n, y_n=f_n', n!=0.                      (5)
```

The two W components extend evenly and the two D1 W components oddly
across each endpoint. Unfolding to a circle of length4L proves completeness
of this Fourier family. Reversing these parities gives the target family,
with the same nonzero frequencies and an additional two constant modes in
W-perp. Differentiation maps every nonzero source mode bijectively to the
matching target mode and kills the two constant source modes in W.
It also kills the full fast sector. The singular values on the nonzero
slow modes are

```
sigma_n=sqrt(alpha)*|n| pi/(2L), n!=0.                      (6)
```

On the closed source observation graph domain (fast L2 arbitrary, slow H1
with traces in W), the target range is exactly

```
Y0={y in L2: integral y dx1 is orthogonal to W-perp},
||minimum_energy_right_inverse||=2L/(pi sqrt(alpha)).       (7)
```

Necessity also follows by integrating y=f': its integral is in W.
For sufficiency take a primitive and choose its integration constant so its
initial trace is in W; the same holds at the far endpoint precisely under
the mean constraint. Removing its constant W component minimizes the norm.
The spectral formula (6) proves boundedness and the sharp inverse norm.
An arbitrary target need not satisfy an endpoint condition to lie in L2;
its evolution generator domain does. Those are different uses of a domain.

The minimum-energy inverse intertwines the unitary source and target groups
on Y0: it pairs equal frequencies in (5), and the bounded inverse extends
that identity from finite mode sums to L2. Likewise the raw derivative
intertwines on its invariant graph domain. The two constant target modes
are unreachable, not a defect that a normalization silently removes.
For a normalized nonzero standing-wave target, exact preparation energy is
`1/(alpha k_n^2)`; a target constant in W-perp has best error equal to its
norm for every source-energy budget. These are explicit dynamical and
accuracy consumers of the repaired boundary.

This is a real construction in the fixed massless normal subsystem, not the
old zero-flux preparation inverse. It supplies no massive or p!=0 boundary
intertwiner. The K1889 preparation surface modes cannot be substituted into
(5)--(7); the operators have different domains and different kernels.

## 6. What remains open

The full massive/tangential problem still requires compatible source and
target evolution domains and proof that O transports an invariant core and
its closure. A conservative source boundary alone is insufficient; section5
shows the required extra calculation in a solvable case. The three-wall box
and arbitrary tangentially mixing nonlocal conditions remain unclassified.
No source-native full-C/injection/pairing map, physical boundary selection,
interacting quotient or all-rotation theorem is supplied.

The preflight's inertia test removed the need for numerical conservation
experiments. Follow-through proves the sharp relaxation, constructs the
massless normal dynamical quotient with its exact lost modes, and rejects
using the preparation bands for repaired evolution. This is a scoped
obstruction plus a tested admissible repair, not an all-boundary exclusion.

## 7. Verification and hostile review

The producer passes40 exact matrix groups and3 input pins. The independent
formulation passes100 exact matrix/construction/endpoint/standing-wave controls and8
reporting/pin checks. It checks H positivity, a complete characteristic basis,
actual invisible flux witnesses and actual isotropic repair bases. After the
clean baseline,4 mathematical faults and1 reporting fault are rejected by
explicit FAIL assertions. No certificate fault is counted as independent
continuum validation; the Green identity, trace-adjoint argument and
construction above carry the operator result.

Inline hostile review found that an unqualified statement about all possible
slab boundaries would be too broad: finite-dimensional inertia alone does not
classify arbitrary tangentially mixing nonlocal conditions. The certificate
and theorem were narrowed to separated local and Fourier-modewise endpoint
conditions before publication. The proof also distinguishes isotropic from
self-orthogonal, the O flux from the source-energy flux, and a whole source
Hilbert-space evolution from an invariant subsystem. The explicit boundary
repair is the contrary construction required before broadening any negative
claim. Final blocking findings: none. Independent-agent, external-specialist,
proof-assistant acceptance and novelty are not claimed.
