---
title: "K1863: conserved stress does not repair instantaneous mean screening"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: INTERNAL-CONSERVED-INSTANTANEOUS-MEAN-SCREENING
claim_ceiling: linearized Einstein response to declared signed conserved stresses; no GU or positive-matter realization
---

# Constraint-admissible distant stress changes local curvature

Instantaneously subtracting the spatial mean of a conserved stress tensor
preserves its conservation. It can nevertheless produce nonzero **linearized
curvature** outside the original source's causal future. The example below
satisfies the linearized Einstein equations, harmonic gauge, retarded data,
and the zero total energy/momentum constraints on a flat spatial torus.
Conservation alone therefore does not repair K1842's conditional screening
implementation. The source class consists of signed external stresses;
positive-energy matter and a GU observation map are not constructed.

The complementary construction is a causal, conserved, exactly idempotent
**trace-removal** operator. It removes a whole scalar stress sector, not just
vacuum constants. Eternal constant sources lie outside its declared domain.
Thus exact idempotence alone does not forbid causal tensor projectors, while
this repair supplies no vacuum-screening or positive-action theorem.

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
result: conserved mean-screening curvature witness and causal trace-removal repair
carrier: real symmetric external stresses and linearized four-metrics on flat R times T3 LAYER=toy CHIRALITY=N/A
pairing: flat Lorentz metric of signature minus-plus-plus-plus and normalized spatial integral ON=symmetric_tensors
real_structure: real fields, periodic spatial coordinates and zero-past retarded data
grading: tensor degree only; no GU or fermion grading
action_owner: repository-construction -- linearized Einstein action with conserved projected external stress; repaired retarded operator is a response prescription
target: linearized Riemann, Ricci and Weyl tensors MAP-TYPE=evaluation
```

## 1. Question, source boundary and domain

[K1842](k1842-screening-causal-response-2026-10-20.md) already proves the
scalar distant-response criterion, source/readout repairs and scalar analytic
idempotence obstruction. Its unrestricted scalar interventions are explicitly
not conserved metric stresses. The present question is whether conservation,
gauge constraints and a gauge-invariant readout eliminate its witness. They
do not for the following fully specified linear model. The August10
[projector result](selected-k77-global-projector-amplitude-layer0-2026-08-10.md)
already separates formal constant cancellation from amplitude selection.
Neither result is repeated as new.

SC-ACT-01/02 and SC-COS-50/51/54 remain ASSERTS. The source's I1B,
ad-valued displacement one-form, metric-on-metrics and unspecified observation
are not identified with an imported Einstein action or a spatial-average
operator. SC-COS-54's unspecified curvature field remains unspecified.
LT-GR2c/2d/6b remain NEEDS; LT-GR1b's scoped post-Shiab exclusion is untouched.
No source assertion, physics ledger verdict, canon, positivity or magnitude
claim changes. This construction tests one conditional response mechanism.

Let M=R times T3, eta=diag(-1,1,1,1), and spatial volume V. All tensors are
periodic. Let P=partial_t^2-Delta and Box=-P. Sources are smooth and compact
in time, or, for compositions below, smooth with support bounded below in
time. Retarded inverses on this globally hyperbolic cylinder have zero past
Cauchy data. Define componentwise

```
mean(T_munu)(t)=V^-1 integral_T3 T_munu(t,x) dx,
Q_sp T=T-mean(T),
P bar_h_munu=2 kappa (Q_sp T)_munu,  kappa>0,
h_munu=bar_h_munu-(1/2)eta_munu tr_eta(bar_h).             (1)
```

If partial^mu T_munu=0, then partial_t mean(T_0nu)=0. Zero past therefore
gives mean(T_0nu)=0. Spatial integration and differentiation commute, so
Q_sp T is conserved. The divergence of the retarded bar_h solves a
homogeneous wave equation with zero past data; it vanishes. Consequently
(1) solves the **full** linearized Einstein system G^(1)=kappa Q_sp T,
not just a gauge-fixed wave equation with untested constraints. In particular
the torus's integrated Hamiltonian and momentum constraints are satisfied.
An arbitrary positive localized energy injection would not have this property
and is not substituted for the source below.

The metric source coupling to Q_sp T is invariant under linearized
diffeomorphisms because Q_sp T is conserved. The fixed flat foliation and
its average are additional structure, not a source-selected covariant GU
functional. The classical linearized equations and retarded-gauge construction
are standard; see [Poisson, Pound and Vega, section 19](https://pmc.ncbi.nlm.nih.gov/articles/PMC5255936/).
The explicit source and response proof here require no numerical Green solver.

## 2. A six-component conserved intervention

Choose a nonzero smooth g supported in a small spatial neighborhood W, with
positive spatial mean b. Choose a smooth time bump a supported in (0,e), and
any real symmetric 3 by 3 matrix S. Set chi=a(t)g(x) and

```
T_00=sum_ij S_ij partial_i partial_j chi,
T_0i=T_i0=sum_j S_ij partial_t partial_j chi,
T_ij=S_ij partial_t^2 chi.                                (2)
```

Commuting derivatives gives -partial_t T_0nu+partial_i T_inu=0 in
every component. Every component is supported in (0,e) times W.
The spatial means are

```
mean(T_00)=mean(T_0i)=0,
A_ij(t):=mean(T_ij)=b S_ij a''(t).                         (3)
```

Thus all total Killing energy/momentum charges vanish. T_00 is generally
signed. No dominant energy condition, nonlinear backreaction, autonomous
matter Lagrangian, or physical apparatus that realizes (2) is asserted.
One may scale the entire source arbitrarily small within linear theory.

This distinction is essential. On a compact slice, mean(T_00)=0 together
with T_00>=0 forces T_00=0 pointwise. The dominant energy condition then
forces the whole stress tensor to vanish: the energy flux for the normal
observer has zero time component and must be causal, hence is zero; applying
the same condition to nearby timelike observers forces the spatial stress
components to vanish too. Thus a nonzero source (2) cannot be a standalone
dominant-energy matter stress on this background. Signed variations around
nonzero matter can be meaningful, but introduce a different background and
linearized conservation problem requiring a fresh adapter.

Vanishing Killing charges as additional constraints for sourced linearized
Einstein equations on spatially compact settings are established theory;
see [Hintz (2024), Theorem 1.1](https://link.springer.com/article/10.1007/s11005-024-01841-9).
The explicit source above satisfies them directly. Solving the linearized
equations does not prove integrability into a family of exact nonlinear
Einstein-matter solutions or any positive-matter realization.

Choose an observation neighborhood U a distance d>e from W, and a time
t in (0,e) with a''(t) nonzero. Work before any torus-wrapping causal path
can arrive. The unprojected retarded solution is zero on a neighborhood of
(t,U), by finite propagation. The subtracted homogeneous mean solves an
ordinary second-order equation; since a and a' vanish in the past,

```
bar_h_00=bar_h_0i=0,       bar_h_ij=-2 kappa b S_ij a,
h_00=-kappa b tr(S) a,
h_ij=-2 kappa b [S_ij-(1/2)delta_ij tr(S)] a.              (4)
```

These expressions hold only outside the original source's causal future;
near W the unprojected causal field must also be included. That field supplies
the global compensation, so (4) does not violate the zero spatial mean of
the full projected solution.

## 3. Curvature, not a gauge potential

Use

```
R_abcd^(1)=(h_ad,bc+h_bc,ad-h_ac,bd-h_bd,ac)/2,
Ric_bd=eta^ac R_abcd,     R=eta^bd Ric_bd.
```

On the distant region (4) gives exactly

```
E_ij:=R_0i0j^(1)=kappa[A_ij-(1/2)delta_ij tr(A)],
Ric_00=-(kappa/2)tr(A),
Ric_ij=-kappa[A_ij-(1/2)delta_ij tr(A)],
R=kappa tr(A),
C_0i0j^(1)=(kappa/2)[A_ij-(1/3)delta_ij tr(A)].           (5)
```

The Einstein tensor is G_00=G_0i=0 and G_ij=-kappa A_ij,
as required by the distant effective source Q_sp T=-mean(T).
Linearized Riemann on a flat background is invariant under arbitrary smooth
periodic linearized gauge transformations. Hence the effect cannot be removed
by harmonic-gauge residual freedom. A compactly smeared curvature readout
within a region where a'' has fixed sign is also nonzero; no point-detector
idealization is essential.

The tidal map in (5) is invertible on Sym3:

```
A=(E-I tr(E))/kappa.                                     (6)
```

Thus every nonzero averaged spatial stress in this family is visible to some
tidal component. S=I gives nonzero scalar Ricci curvature but zero electric
Weyl curvature; traceless S gives zero scalar curvature but nonzero electric
Weyl curvature. Either readout alone can miss a sector. The two together
detect the six independent averaged stress components. Conservation has
removed four averaged components, not the six responsible for this effect.

For any conserved zero-past source supported away from a readout's causal
past, the same reasoning gives (5) with its actual A(t). Therefore distant
full-tidal response vanishes precisely when A(t)=0 at the observation time.
For a prescribed class of interventions and all distant observation windows,
this is the corresponding necessary-and-sufficient pointwise criterion.
This does not claim that every nonzero source admits such a window or that
nonlinear gravity obeys the same linear formula.

Two direct repairs remain real, narrower experiments. Requiring every
admissible source to have A(t)=0 makes Q_sp T=T, restoring the unprojected
causal response. Measuring a spatial derivative of curvature annihilates
the homogeneous correction, also restoring that readout's causal response.
The latter readout was already insensitive to homogeneous curvature; it
does not demonstrate screening of an otherwise measurable vacuum effect.

## 4. Executed alternative: a causal tensor projector

Let G_Box be the retarded inverse of Box on smooth past-supported scalar
fields on the same cylinder. Define

```
(Pi f)_munu=eta_munu f-partial_mu partial_nu G_Box f,
tau=tr_eta(T),
Q_ret T=T-(1/3)Pi tau.                                  (7)
```

Here Box G_Box f=f and G_Box Box f=f on this zero-past domain; derivatives
commute with G_Box. Hence divergence(Pi f)=0 and tr(Pi f)=3f.
If T is conserved, Q_ret T is conserved and traceless. Its second application
does nothing because its trace is zero: Q_ret^2=Q_ret. It is causal:
Pi consists of a local term and derivatives of a retarded solution. Composing
with the retarded Einstein wave inverse retains causal support. Ward
constraints again propagate from zero past data. No elliptic spatial inverse
or instantaneous average appears.

The kernel is exactly the scalar improvement sector on this domain. With
D chi=partial_mu partial_nu chi-eta_munu Box chi,

```
Q_ret(D chi)=0;
Q_ret T=0  implies  T=D[-G_Box tau/3].                    (8)
```

This is a materially different operation from Q_sp: it removes local scalar
stress responses as well as their trace, including nonconstant ones. It is
the identity on conserved traceless tensors. At a nonnull covector its
restriction to the six-dimensional conserved symmetric-tensor space has rank
five and a one-dimensional scalar kernel. The differential proof, rather
than dividing by a null Fourier symbol, defines (7) at characteristic data.

This repairs causality and conservation **for trace removal**, not vacuum
screening. Eternal constant vacuum stress is not a past-supported source;
G_Box on it requires additional initial/asymptotic data. It cannot be
silently inserted into (7) as if the zero-past inverse existed on constants.
Moreover the periodic linearized Einstein constraint independently excludes
a nonzero uniform energy density with the stated flat background and data.
An enlarged cosmological problem would need its own background and constraints.

The scalar analytic-transfer idempotence theorem in K1842 is not contradicted:
(7) acts on tensor channels, has a nontrivial invariant kernel/image and
does not interpolate a scalar DC cutoff and a scalar high-frequency identity.
Neither positivity nor an action that produces this retarded projector is
proved. A retarded inverse is generally not formally self-adjoint, so placing
it in a single ordinary quadratic action is not a derivation of (7).

## 5. Verification and remaining scientific obligations

The producer checks generic conserved stress jets, trace reversal, all tensor
curvature components, the full Einstein residual, tidal inversion,
Ricci/Weyl sector controls and the nonnull symbol of (7). The independent
standard-library probe checks derivative-polynomial jets and separately
evaluated rational tensors, including planted sign, trace and projector faults.
Report flags are distinct from mathematical controls. The written support,
uniqueness, domain and gauge arguments establish the continuum claims;
finite checks do not prove causal support or admissibility of physical matter.

```
sage -python tests/channel-swings/k1863_conserved_screening_causality.py
python3 tests/channel-swings/k1863_conserved_screening_causality_probe.py
```

Preflight alternatives were a scalar rerun (already settled), an actual GU
metric adapter (requires independent construction), and conserved linearized
Einstein response. The last isolates the previously untested conservation
premise at low cost. Postflight challenges include forbidden total-energy
injections, gauge-dependent potentials, isotropic Weyl blindness, trace-free
Ricci-scalar blindness, constants outside the retarded domain, and an
unjustified self-adjoint/action claim. None is hidden in the conclusion.

The remaining useful test is a specified source-owned or explicitly conditional
matter/metric observation adapter that determines the admissible stress
tangents and the measured curvature. If its tangent class contains (2),
instantaneous mean subtraction fails this causal criterion. If it excludes
them, the exclusion must come from that model's actual equations or operational
source restrictions. No GU-wide conclusion, physical positive-matter
counterexample, novel theorem or formal proof certification is claimed.
