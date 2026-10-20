---
title: "K1848: shift-protected static response and its physical limits"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional scalar symmetry and response theorem; no GU or vacuum-energy screening
---

# Static cancellation can be protected, with an explicit price

An ordinary internal symmetry that separates a source and readout into
orthogonal invariant sectors suppresses their **entire** linear response,
not just the constant response. A different construction survives: a
simultaneous constant shift of an external source and a scalar field protects
zero static source-conjugate response, including nonlinear interactions that
respect that shift. The source contact is required by the same symmetry.
Promoting the source to a dynamical field produces a physical massless mode,
not a gauge redundancy. Adding a constant to the potential still shifts the
gravity stress, so this is not a solution of the cosmological constant problem.

This is a demand-derived conditional construction following K1846's exposed
readout tuning. SC-COS-50/51/54 and SC-ACT-01/02 remain ASSERTS;
SC-META-53 remains UNCERTAIN. LT-GR2c/2d/6b and LT-SM8 stay unchanged.
The imported real scalar action has no typed identification with GU's
ad-valued connection, its source intervention, or its observed stress tensor.
No claim of novelty, quantum protection, nonlinear relaxation or external
acceptance is made.

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
result: internal selection-rule silence versus affine-shift static protection, nonlinear identity and dynamical-source cost
carrier: finite real scalar multiplet or bounded positive mass-band Hilbert space on fixed flat spacetime LAYER=toy CHIRALITY=N/A
pairing: positive real kinetic inner product ON=real_scalar_fields
real_structure: real fields, real external source and fixed real vector v
grading: none; internal symmetry representation is not GU grading
action_owner: repository-construction -- local potential U(phi-Jv)
target: same-action source-conjugate response and its zero-frequency limit MAP-TYPE=evaluation
```

## 1. A structural discriminator before another tuned spectrum

Let A be a positive self-adjoint mass operator, with A>=m²>0. Suppose an
orthogonal internal symmetry has an orthogonal sector projector P commuting
with A, and Pc=c, Pd=0. Then for every z>0,

```
<d,(z+A)^-1 c>=0.
```

The resolvent preserves ran(P), which is perpendicular to d. Functional
calculus gives the same zero for retarded wave response. A compact-group
selection rule with invariant source and a readout orthogonal to the
invariant sector is an example. The statement requires the actual operator
and domain to preserve P. It does not classify all symmetries or all
possible identities. It says why this particular repair of K1846's tuned
cross integral cannot protect only DC while leaving a nonzero dynamic signal.
Breaking sector preservation can restore both responses; silently using a
symmetry of the kinetic term alone would not prove the premise.

## 2. Demand-derived repair: a simultaneous affine shift

The downstream demands are a local positive-energy field theory, a same-action
readout, constant-source insensitivity at equilibrium, and a nonzero response
to changing sources. For a finite real multiplet, choose a fixed v and a C²
potential U with a nondegenerate minimum at chi=0 and Hessian A>0. Use

```
S[phi;J]=integral { (1/2) partial_mu phi . partial^mu phi - U(phi-Jv) },
chi=phi-Jv,    O=delta S/delta J=<v,grad U(chi)>.
```

The metric convention makes Box=partial_t²-Delta. The field equation is
`Box phi+grad U(chi)=0`; compact variations and ordinary Cauchy data define
this classical problem. Finite-dimensional smooth potentials give standard
local semilinear solutions; all nonlinear identities below apply on their
interval of existence. Global nonlinear well-posedness is not asserted.

For constant epsilon, `(phi,J)->(phi+epsilon v,J+epsilon)` leaves both
kinetic term and potential invariant. This is a spurionic symmetry when J is
external: it relates source configurations and their corresponding field
solutions, not distinct states at the same fixed source. It is not a gauge
constraint. At each constant J, phi=Jv is a stationary homogeneous solution,
and O=0. Any interaction delta U(chi) with a stationary minimum chi0 instead
gives phi=Jv+chi0 and the same O=0. The minimum need not be at zero; its
location must be independent of J in the shifted coordinate.

The exact local on-shell identity is

```
O=-<v,Box phi>.                                             (1)
```

It follows from the actual Euler equation, not a fitted readout. For quadratic
U=chi.A.chi/2, expanding the action gives

```
c=Av,       h=<v,Av>,
S=kinetic-phi.A.phi/2+J<c,phi>-h J²/2,
O=<c,phi>-hJ,
R(z)=<Av,(z+A)^-1 Av>-<v,Av>
    =-z <v,A(z+A)^-1 v>.                                    (2)
```

Thus R(0)=0 while R(z)<0 for z>0 and v!=0. The coefficient identity also
shows `R(z)/z -> -||v||²` at zero. For the positive mass-band case A is bounded
and boundedly invertible, v is in H, and every displayed expression is a
bounded quadratic form. Zero-past retarded solutions have causal support;
the contact is supported at the source point, not outside its causal future.
For finite fields the same statements are elementary matrix identities.

For a general quadratic potential including the source contact, invariance
under this exact shift forces c=Av and h=v.Av. These follow by setting to
zero the coefficients of phi, J and epsilon in the change of the potential.
Consequently changing A while keeping this symmetry also changes c and h.
That is a constrained perturbation class, not arbitrary coefficient robustness.
For c=Av+epsilon w and unchanged h, the static residual is exactly
`2 epsilon <v,w>+epsilon²<w,A^-1 w>`. A contact change h->h+eta adds -eta.
The symmetry makes the relation an action condition rather than repeated
manual readout tuning; neither positivity nor causality enforces it.

## 3. Nonlinear protection and the remaining relaxation condition

For example take two fields, v=(1,2), and

```
U(chi)=chi1²/2+2chi2²+lambda(chi1²+chi2²)²/4, lambda>=0.
```

Its minimum is unique at zero. Its Hessian is
`diag(1,4)+lambda[||chi||² I+2 chi chi^T]`, strictly positive. The source
couplings of orders one through four and their contacts are all fixed by
substitution chi=phi-Jv. Equation(1) and the full static zero survive every
lambda>=0. Linearizing at the minimum recovers(2) with A=diag(1,4).
This is genuine nonlinear static protection within the stated class, not a
proof of quantum radiative stability: a regulator, measure, counterterms and
boundary conditions preserving the spurionic identity would have to be given.

Static zero is not ordinary late-time zero. Already lambda=0 with finitely
many positive masses has persistent step oscillations, as K1846 proves.
For a bounded continuum A=omega² on H=L2([1,2]), take v=1. The quadratic
protected readout following J0 H(t), on a spatial torus, is

```
O(t)/J0=-integral_1^2 omega² cos(omega t) domega,
|O(t)/J0| <=8/t, t>0.                                      (3)
```

The bound is integration by parts: endpoint sum5 plus integral of2omega=3.
The displaced energy remains `J0² integral omega²/2=7J0²/6`. This executes
protection and late decay together in one linear model. A smooth mass function
m(omega)>0 and spectral density give the same static cancellation, but late
decay additionally requires decay of the pushed-forward oscillatory spectral
measure. For instance a constant mass on a positive-measure subinterval
creates an atom and persistent oscillations. The shift alone does not protect
dephasing, and no interacting-continuum scattering theorem is inferred.

## 4. Released successor: promote the source and count the price

Now give J its own positive kinetic coefficient Z>0. The quadratic potential
matrix on the actual fields (phi,J) is

```
M = [ A       -Av  ]
    [ -v^T A  v^TAv],       K=diag(I,Z).
```

For any (f,j), `(f,j)^T M(f,j)=(f-jv)^T A(f-jv)>=0`.
For n finite fields, M has rank n and exactly one kernel direction (v,1).
Positive K turns this into one physical massless scalar and n positive
mass-squared modes. There is no first-class constraint or gauge quotient.
At low z, eliminating the massive phi produces the exact Euclidean/inertial
Schur kernel

```
K_eff(z)=Zz+v^TAv-v^T A(z+A)^-1 Av
        =z[Z+<v,A(z+A)^-1 v>]
        =z[Z+||v||²]+O(z²).                                (4)
```

It is positive for z>0. The same flat stationary manifold survives smooth
shift-invariant interactions; linearizing at a positive-Hessian minimum gives
one zero direction. Quantum masslessness and global nonlinear behavior are
outside this classical statement. A new potential W(J) changes the symmetry
and the zero-mode conclusion. No dynamical-source calculation was licensed by
K1846's external-source energy alone; the enlarged action is explicitly
supplied here.

## 5. Stress is the decisive nontransfer

Covariantize this scalar action with minimal kinetic terms and metric-independent
U. Its matter stress is
`T_munu=partial_mu phi.partial_nu phi-g_munu[(partial phi)²/2-U]`
(up to the consistently chosen stress-sign convention). The constant vacuum
term is proportional to U(chi0) g_munu. Replacing U by U+C preserves the
entire affine symmetry, Euler equation, Hessian and O. It nevertheless shifts
the stress by C g_munu in this convention. This is an exact counterexample to
inferring vacuum-energy insensitivity from source-conjugate O=0.
For a source with its own kinetic term, the constant vacuum has zero kinetic
energy and the same conclusion. Choosing U(chi0)=0 manually does not protect
it against this permitted constant deformation.

Hence the same-action conditional mechanism solves the stated scalar-response
question, but not LT-GR2d. The gravitational observable and its variational
owner are a distinct obligation. Compare the conserved-source gravitational
amplitudes in [Niedermann and Padilla](https://arxiv.org/abs/1706.04778);
those are not the scalar readout used here, so no evasion of their theorem is
claimed. An actual GU test still needs its intervention, contact, observable,
metric variation and common domain on the native carrier.

## 6. Review and reproduction

Run `sage -python tests/channel-swings/k1848_screening_shift_protection.py`
and `python3 tests/channel-swings/k1848_screening_shift_protection_probe.py`.
Symbolic identities check the full nonlinear shift, readout, Hessian, source
promotion and continuum primitive. A separate Fraction implementation checks
matrix response/Schur identities for many positive rational fixtures, exact
symmetry-breaking residuals and genuine coefficient faults. These finite
checks support, but do not replace, the operator-domain, causal-support and
nonlinear arguments above. Manifest scope mutations are reported separately.

Hostile review tests ordinary internal symmetry versus source transformation,
external versus dynamical J, source contact versus a ghost, DC versus late
response, correlated versus arbitrary perturbations, and O versus stress.
No counterexample remains within the stated algebraic hypotheses; relaxed
hypotheses have explicit counterexamples above. No separate-agent or formal
proof review is claimed. The remaining substantive question is a native
stress/constraint mechanism or an actual nonlinear relaxation theorem, not
another cancellation fixture.
