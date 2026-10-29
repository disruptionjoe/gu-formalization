---
title: "K2231 Spatial-local quadratic control boundary and mediator stability"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: direct local-form boundary, stable star early response and classical causal auxiliary-field repair; no quantum apparatus or complete detector
scripts:
  - tests/channel-swings/k2231_spatial_local_control_boundary_probe.py
---

# K2231 Spatial-local quadratic control boundary and mediator stability

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
result: K2231 local-form discriminator, stable star early response and classical causal auxiliary-field repair
carrier: real massive scalar Cauchy space H1(R^d) direct-sum L2(R^d), with declared auxiliary oscillator or second scalar field LAYER=toy CHIRALITY=N/A
pairing: positive real free-energy form; canonical symplectic pairing ON=declared_carrier
real_structure: real smears and real Cauchy data; complex adjoint only on antecedent quantization
grading: canonical position/momentum and auxiliary oscillator; not chirality
action_owner: repository-construction -- supplied quadratic controls and linear oscillator coupling
target: fixed canonical f-mode generator, full Cauchy energy-form comparison MAP-TYPE=intertwiner
```

## Preflight and reranking

K2228 already proves retained-drift continuum channel approximation when direct
canonical-mode controls are supplied. K2143 already identifies the bilocal
kernel and intraregional signalling; K2145 already supplies a causal-duration
lower bound. Repeating either would be duplicate. K2225 supplies finite-chain
dynamic synthesis and prevents a conclusion that local generators cannot
synthesize a collective final operation. The new question here is narrower:
can *instantaneous local differential quadratic generators* approximate the
fixed canonical generator in its full Cauchy energy-form topology? The answer
is no, with an explicit positive lower bound. A mediated construction is then
tested rather than dismissed: its exact stability threshold and elimination
sign are computed. Neither observation decides dynamic continuum synthesis.

Relevant startup routes are T11 domains, T15 positivity and T16 imported
controls. Layer0 distinguishes algebra-local bounded-region observables,
support-local quadratic densities and causal finite-time channels. They are
three different predicates. This is not a new substrate/chirality candidate
and does not modify any L1--L7 no-go assumption or GU source claim.

## 1. Fixed object and topology

Let m>0, A=-Delta+m² and omega=A^(1/2) on R^d. The real Cauchy carrier is
V=H1(R^d) direct-sum L2(R^d), with

    e((q,p),(q',p'))=<omega q,omega q'>+<p,p'>.

Let real normalized f in C_c^infinity be the *same* canonical smearing as
K2228; freeze its nu>0 (use K2160's selected value if identifying that
instrument). Write Q_f=<f,q>, P_f=<f,p>. The K2228 positive oscillator
plateau has classical quadratic symbol

    k_s(q,p)=1/2 [s nu Q_f²+(s nu)^(-1) P_f²], s>0.

Its symmetric Hessian is

    B_s(z,z')=s nu <f,q><f,q'>+(s nu)^(-1)<f,p><f,p'>.

This is continuous on V, since m>0 and f in L2. Its q and p kernels are
rank-one f(x)f(y). A local differential quadratic form means any continuous
symmetric form L:V x V -> R which on compact smooth tests is a finite sum of
integrals of products of derivatives at the SAME spatial point, with local
coefficients for which those integrals make sense. More generally the proof
needs only support locality: L(u,v)=0 for separated supports. Differential
order may vary between approximants, provided each form is defined on the
same tested carrier. Forms not bounded on V already cannot converge in the
V-form norm considered below.

## 2. Quantitative separation theorem

Choose nonzero real smooth u,v with separated compact supports and
a=<f,u> !=0, b=<f,v> !=0. Such packets exist for every nonzero smooth f: take
two small disjoint balls in an open set where f has a fixed nonzero sign.
For q-only data U=(u,0), V0=(v,0), every local L obeys

    (B_s-L)(U,V0)=s nu a b.

Consequently, with ||D||_e=sup |D(z,w)|/sqrt(e(z,z)e(w,w)),

    ||B_s-L||_e >= s nu |a b|/(||omega u|| ||omega v||) >0.       (1)

For p-only data the independent bound is

    ||B_s-L||_e >= |a b|/(s nu ||u|| ||v||) >0.                  (2)

The supremum may be infinite; that does not weaken either bound. The same
fixed u,v works for every member of a proposed approximation sequence, even
if coefficients or differential order vary. Thus there is no pointwise
bilinear-form convergence on all compact smooth tests, no V-form-norm
convergence, and no distribution-kernel convergence to B_s. The last claim
also follows because distributions supported on the diagonal remain so under
distributional limits; f tensor f has nonzero off-diagonal testing.

Proof: derivatives do not enlarge supports, so every integrand pairing a
derivative of u with one of v vanishes. The target cross pairing is exactly
the product above. Divide by the two fixed energy norms. Polarization gives
the equivalent observable quadratic-form test

    k_s(U+V0)-k_s(U-V0)=2 s nu a b,

where every local quadratic form has difference zero. The factor2 is because
k_s(z)=B_s(z,z)/2. Constant quantum vacuum shifts disappear in polarization.

These are sharp two-packet compression lower bounds: normalize U,V0 in e.
The error compression has fixed off-diagonal entry d=s nu a b/
(||omega u|| ||omega v||). Every symmetric 2x2 matrix with this entry has
operator norm at least |d|; choosing both diagonal errors zero attains it.
This is sharpness of the two-dimensional relaxation, not a global optimal
local approximation theorem.

Adding the same free Hessian e to both target and approximant cancels exactly.
Retaining H therefore does not repair the instantaneous form obstruction.
This is a classical Hessian/Cauchy-form theorem. It does not silently assume
that every local quadratic density has a renormalized self-adjoint Fock
operator, and it does not establish a quantum-H-form-norm obstruction without
a separately proved bridge from that topology to these Cauchy pairings.

## 3. A concrete mediator repair, and its exact price

Introduce real oscillator coordinates (x,y), frequency Omega>0, and real
coupling g. Consider the *whole* classical quadratic Hamiltonian

    H_ext=1/2[||p||²+<q,Aq>+y²+Omega² x²]+g x <f,q>.

Its cross coupling is linear in the field at each x-space location, with a
common oscillator coordinate. Let sigma=<f,A^(-1)f> (finite and positive).
Completion of the field square gives

    <q,Aq>+2g x<f,q>+Omega² x²
    =||omega(q+g x A^(-1)f)||²+(Omega²-g² sigma)x².              (3)

Thus the classical Hamiltonian is nonnegative exactly when

    g² sigma <= Omega².                                      (4)

If the inequality fails, q=-g x A^(-1)f and arbitrarily large |x| give an
unbounded negative direction. At equality there is a flat configuration
direction, not a strictly positive oscillator gap. This argument is valid
on H1 because A^(-1)f lies there. It is also the exact finite oscillator
quantum stability criterion, up to a constant; no general continuum
quantization or ground-state existence is claimed here.

Eliminating x *statically* gives

    H_eff(q,p)=1/2[||p||²+<q,Aq>] -g² Q_f²/(2Omega²).            (5)

This realizes a rank-one *negative* correction to stiffness, constrained by
(4); it does not supply K2228's positive Q_f² plateau. Static minimization is
not an exact time-dependent reduced Hamiltonian: Section4 retains mediator
inertia and memory explicitly. Positive completion

    1/2[y²+Omega²(x+g Q_f/Omega²)²]

adds the term +g² Q_f²/(2Omega²) explicitly. Calling this completion local
would hide exactly the bilocal field counterterm at issue. Likewise scaling
g to Lambda g at fixed Omega eventually violates (4). For nonzero g,
Lambda <= Omega/(|g|sqrt(sigma)); unbounded fast control needs a changed
frequency/counterterm/stiffness/resource assumption, with fresh analysis.

The coupling integral g x integral f(r)q(r)dr has one oscillator coupled
simultaneously to separated field patches. It is a star architecture. Writing
it as an integral does not make the shared oscillator a point-local field.
A genuinely spatially distributed auxiliary field, transport network or
finite propagation proof would change the construction and could supply a
dynamic repair; none is excluded by (1)--(5).

## 4. Exact memory equation and arbitrarily-early star response

The mediator does not become causal merely by satisfying (4). Its classical
Hamilton equations, with the full KG drift retained, are

    q''+Aq+g f x=0,       x''+Omega² x+g Q_f=0.

For initial oscillator data x0,y0 the exact variation-of-constants identity is

    x(t)=x0 cos(Omega t)+y0 sin(Omega t)/Omega
         -g integral_0^t sin(Omega(t-r))/Omega Q_f(r) dr.

Consequently the exact field equation is

    q''(t)+Aq(t)=-g f[x0 cos(Omega t)+y0 sin(Omega t)/Omega]
       +g² f integral_0^t sin(Omega(t-r))/Omega Q_f(r) dr.       (6)

The memory term is rank-one in space and has a retarded time kernel. Retarded
time dependence alone does not provide finite spatial propagation.

Take nonzero g satisfying g² sigma<Omega² and smooth compact f,u,v, with u,v
having separated supports and <f,u><f,v> !=0. Start q(0)=u, p(0)=0,
x(0)=y(0)=0. Then, for the actual coupled solution,

    <v,q(t)>=g² <f,v><f,u> t^4/24+o(t^4),  t ->0.             (7)

Proof and domains: on L2(R^d) direct-sum R define the self-adjoint stiffness

    D=[[A,g f],[g<f,.>,Omega²]],  Dom D=Dom A direct-sum R.

The off-diagonal block is bounded. Under the strict stability hypothesis D
is positive and bounded below by a positive constant: square completion and
bounded invertibility of (q,x)->(q+g x A^(-1)f,x) prove coercivity. The unique
finite-energy solution with the chosen zero velocities is
(q(t),x(t))=cos(t sqrt(D))(u,0). Smooth u,f put (u,0) in Dom D². Spectral
calculus gives the norm expansion

    (q(t),x(t))=(u,0)-t² D(u,0)/2+t^4 D²(u,0)/24+o(t^4).

This follows by dividing the scalar cosine remainder by t^4 lambda²,
using a uniform bounded remainder and dominated convergence against the
Dom D² spectral measure; it does not require analyticity in t. The field
component of D²(u,0) is A²u+g² f<f,u>. Local differential operators A,A²
preserve support, so their pairings with v, as well as <v,u>, vanish. This
proves (7), with a nonzero coefficient. Thus every sufficiently small positive
t has a nonzero response in the separated patch, including times below its
distance from supp u in units of KG propagation speed1.

The zero initial data evolve to zero. Comparing that solution to the chosen
u perturbation gives an exact failure of classical finite propagation for
this stable star model. Amplitudes can be scaled arbitrarily small while
retaining the nonzero coefficient and finite input energy. This is not yet
a quantum recorded-channel error bound, nor a claim about every oscillator
or auxiliary-field apparatus. It identifies the actual instantaneous spatial
reach hidden in one oscillator coupled to several patches. A spatially local
mediator field or transport system is a different model.

The broader distinction between localized measurements and causality is
standard background; see [Fewster--Verch](https://arxiv.org/abs/1810.06512)
and [Sorkin](https://arxiv.org/abs/gr-qc/9302018). No theorem is imported from
their abstracts here: (6)--(7) are self-contained statements about this
specified quadratic model, without a novelty claim.

## 5. A genuinely local classical auxiliary-field repair

Replace the shared oscillator by a real scalar field chi with conjugate pi,
D_aux=-c² Delta+mu², c,mu>0, and F=M_f multiplication by the SAME real smooth
compact function f. This deliberately changes the coupling map: multiplication
by f is not the rank-one functional <f,.>. On two copies of H1 direct-sum L2,
use

    H_loc=1/2[||p||²+<q,Aq>+||pi||²+<chi,D_aux chi>]
          +g<q,F chi>.                                      (8)

The exact positivity condition is the quadratic-form Schur complement

    A-g² F D_aux^(-1) F >=0.                                 (9)

Indeed complete the auxiliary square with
chi+g D_aux^(-1)Fq. This translation is well defined in its energy space
because D_aux>=mu². A sufficient strictly stable regime is

    |g| ||f||_infinity < m mu.                               (10)

The potential is bounded below by the two-variable mass form
m²||q||²+mu²||chi||²-2|g|||f||_infinity||q||||chi|| plus the two nonnegative
gradient energies. Its 2x2 mass matrix is positive definite under (10).
Thus this construction has a positive conserved classical energy and
well-posed linear energy-space evolution, retaining both free drifts.

The equations are a local hyperbolic system:

    q''+Aq+g F chi=0,      chi''+D_aux chi+g F q=0.

They propagate initial-data differences no faster than v_max=max(1,c).
One direct proof uses the free wave Duhamel equations on the two energy
spaces. Free wave propagators have speeds1 and c; bounded multiplication F
does not enlarge support. Every Picard/Duhamel term therefore stays inside
the initial support expanded by v_max t. Standard bounded-perturbation
iteration converges in energy norm on bounded time intervals, which preserves
that support containment. This uses compactly supported initial differences
of BOTH fields. Pre-existing auxiliary data supply an independent forcing;
they cannot be silently set to the future equilibrium of changed q data.

With S_D(t)=D_aux^(-1/2)sin(t sqrt(D_aux)) and free auxiliary solution chi_0(t),
exact elimination gives

    q''+Aq-g² F integral_0^t S_D(t-r) F q(r)dr=-g F chi_0(t).   (11)

The negative memory term is on the LEFT; equivalently the feedback has
positive sign on the right, as in (6). Unlike the shared oscillator kernel,
S_D(t-r) has spatial support at distance at most c(t-r). Thus the memory
equation is compatible with the proved finite propagation. The static
approximation remains a negative correction -g² F D_aux^(-1)F to stiffness;
it must not replace the retarded response in a causal timing argument.

This static correction is also not the desired rank-one f tensor f operator.
For nonzero smooth f it has infinite rank: choose a nonempty open patch where
|f|>=epsilon>0. On the infinite-dimensional space of L2 functions supported
there, <h,F D_aux^(-1)Fh>=||D_aux^(-1/2)Fh||² is strictly positive for every
nonzero h. A finite-rank operator would have a nonzero kernel vector on that
space, a contradiction. Consequently the repair supplies a genuine stable,
classical causal architecture, but neither exact rank-one mode selection nor
the positive K2228 plateau. An approximation to the actual mode, quantum
implementation, record nonlinearity, and full channel error remain substantive
next targets. This is a constructive repair of the star's causal defect,
not a full detector or source-owned GU construction.

## 6. Exact consumer and falsification controls

The accompanying rational probe uses f=(3/5,4/5), A=diag(1,9), nu=s=1.
The q-target Hessian has cross entry12/25; any diagonal local compression has
energy-norm error at least4/25, while the p-only bound is12/25. The target
quadratic polarization is24/25. For the mediator sigma=97/225 and Omega=2:
g=3 is strictly stable with Schur remainder3/25, whereas g=4 has remainder
-652/225 and an explicit negative vector. In the stable g=3 fixture, the
field off-diagonal entry of D² is108/25 and the t^4 coefficient is9/50.
The leading retarded memory expansion independently gives g² t^4/24 times
the two overlaps. A two-site auxiliary-field control uses D_aux=[[5,-1],[-1,5]],
F=diag(3/5,4/5), g=1. Its Schur correction has determinant6/625>0, hence is
not rank one, and its sufficient stability condition is strict. These are finite exact algebraic
controls of the displayed formulas, not a simulation proof of the universal
continuum result. Genuine input faults delete the bilocal target cross term,
inject a cross term into the claimed local comparator, replace A^(-1) by A
in the susceptibility, reverse the actual stationary-minimizer sign, omit the return coupling
in the dynamical block, reverse the retarded memory sign, or collapse the
distributed Schur correction to a rank-one outer product.

## Hostile postflight and next scientific condition

The strongest invalid inference is "all local apparatus approximations are
impossible." This result excludes direct same-carrier local differential
generator/form replacement only. Dynamic products can transport support;
K2225 is an explicit finite-chain counterexample to that overclaim. Strong
resolvent/unitary convergence is not inferred from, or ruled out by, failure
of pointwise form convergence. K2145's already-known causal bounds require
its stated operational causality premise and are not re-proved here.

The second invalid inference is that the mediator solves locality: it trades
a field bilocal kernel for a shared global degree of freedom and needs a
stable resource budget. Equations(6)--(7) additionally prove that this stable
model has arbitrarily-early spatial response, not merely a suggestive coupling
diagram. Neither the static sign nor this dynamics supplies the required
causal positive oscillator plateau. Section5 constructs a positive classical
local-field repair with finite propagation, while proving that its static
correction is infinite-rank and negative. The nonlinear record control theta(n_f) also
remains unsupplied; solving quadratic squeezing alone would not implement the
complete detector. The weakest reproducibility seam is continuum domain and
topology transfer: all claims above are deliberately on the stated Cauchy
form space, with universal proofs separate from finite rational checks.

Useful continuation must construct finite-time transport/mediator dynamics
with the actual f, retained KG drift, appropriate stability and a complete
recorded energy-constrained error estimate. No GU source, physical quotient,
Born, empirical, novelty or external-expert credit follows.

## Reproduction and evidence boundary

The [exact probe](../../tests/channel-swings/k2231_spatial_local_control_boundary_probe.py) checks finite algebra and rational consumers; universal statements rely on the written proofs above. Run the probe with the repository Python environment. Its default run regenerates controls in memory and rejects a stale [certificate](../../lab/process/k2231-spatial-local-control-boundary.json); `--write` refreshes that report. Note, probe and reused dependency hashes bind the report. Each planted fault changes mathematics or a supplied input and must fail an unchanged check after a green baseline. Internal independent review is not external-expert or proof-assistant certification.
