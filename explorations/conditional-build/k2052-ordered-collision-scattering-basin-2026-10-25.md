---
title: "K2052: Ordered collisions and open scattering basins with noncompact tails"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: sufficient causal-overlap criterion and open L2 plus Linfinity scattering neighborhoods; no unrestricted complex large-data theorem
scripts:
  - tests/channel-swings/k2052_ordered_collision_scattering_basin.py
  - tests/channel-swings/k2052_ordered_collision_scattering_basin_probe.py
---

# K2052: Ordered collisions and open scattering basins with noncompact tails

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
result: ordered-overlap continuation, L2 scattering and open noncompact-tail neighborhoods
carrier: two complex commuting fields on the line LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: positive weighted charge and L2 plus Linfinity topology ON=declared_graph
real_structure: ordinary complex conjugation of classical fields
grading: even power, not Grassmann parity
action_owner: repository-construction -- K2050 matched positive-power family
target: classical global evolution and scattering MAP-TYPE=intertwiner
```

[Verified conditional mathematics.] An explicitly ordered overlap criterion proves
future global existence and L2 scattering for arbitrary-phase data, including
arbitrarily large waves already moving apart. It releases an open scattering
neighborhood in L2 intersect Linfinity around EVERY smooth compact reference
solution that exists through its finite collision interval. Perturbations may
have noncompact tails. This removes the fixed-support restriction in K2046
and K2050. It does not settle unrestricted large complex initial data.

## 1. The actual system and a one-sided criterion

Take K2050's positive-coupling even-power family, with integer m>=2 and gamma>0:

    z_v = i conjugate(z) w^(2m),
    w_u = -i gamma z^2 conjugate(w)^(2m-1),
    u=x-t, v=x+t.                                      (1)

The actual sextic is m=2,gamma=1. Initial data are smooth with bounded
spatial derivatives of every order, in L2 intersect Linfinity on R. Put

    a0=|z0|^2, b0=|w0|^2, Q=integral_R b0^m,
    A_k(u)=a0(u) exp(2 k^m integral_u^infinity b0(s)^m ds),
    eta_k=2 gamma (m-1) sup_v [b0(v)^(m-1)
                                     integral_-infinity^v A_k(u) du]. (2)

All quantities are finite. Choose ANY k>1. If

    eta_k < 1-k^(1-m),                                 (3)

the solution exists smoothly for all t>=0, with

    |w(t,x)|^2 <= k b0(x+t),
    |z(t,x)|^2 <= A_k(x-t).                            (4)

For the sextic, k=2 gives A_2=a0 exp(8 integral_u^infinity b0^2)
and the condition 2 sup_v b0(v) integral_-infinity^v A_2 <1/2.
This is sufficient, neither necessary nor claimed sharp. The initial
profiles and causal order are load-bearing; an unweighted small-charge
criterion is not substituted for (3).

### Proof and zeros

For a=|z|^2,b=|w|^2, direct differentiation of (1) gives

    |a_v|<=2ab^m, |b_u|<=2 gamma a b^m.                 (5)

Bootstrap b(u,v)<=k b0(v) on u<=v. Along a fixed-u ray, Gronwall gives

    a(u,v)<=a0(u) exp(2 k^m integral_u^v b0^m)<=A_k(u).

Where b0(v)>0, integrating the reciprocal power along the left-moving ray
from v backwards to u gives

    b(u,v)^(1-m) >= b0(v)^(1-m)
                           -2 gamma(m-1) integral_u^v a(s,v) ds,
    b(u,v)<=b0(v)(1-eta_k)^(-1/(m-1)) < k b0(v).        (6)

This is a strict uniform improvement of the bootstrap. Where b0(v)=0,
w stays zero by local ODE uniqueness; no division at zero occurs. Local
bounded solutions initially admit a uniform ratio bound on all nonzero rays:
the logarithmic derivative of b is bounded by 2 gamma sup(a) sup(b)^(m-1)
in null coordinates. Thus a sequence of tiny b0 values at spatial infinity
does not spoil the open bootstrap argument. The same bounded-coefficient
argument prevents a nonzero ray from reaching zero at finite time.

Equations (4) give finite, time-independent amplitude bounds. Differentiating
the characteristic integral equations yields a linear highest-derivative
inequality on every finite time interval; induct on derivatives. The smooth
local solution therefore continues globally forward. This proof uses no
unproved asymptotic boundary flux or positive lower bound for b0.

## 2. Scattering and explicit tail estimates

Define the outgoing profiles as characteristic limits

    z_out(u)=lim_(v->infinity) z(u,v),
    w_out(v)=lim_(u->-infinity) w(u,v).

They exist absolutely: (1) and (4) give

    |z_v|<=k^m sqrt(A_k(u)) b0(v)^m,
    |w_u|<=gamma k^(m-1/2) A_k(u) b0(v)^(m-1/2).       (7)

Both one-dimensional tail integrals are finite. In particular, for t>=0,

    ||z(t)-z_out(.-t)||_2^2
      <= k^(2m) integral A_k(u) [integral_(u+2t)^infinity b0(v)^m dv]^2 du,
    ||w(t)-w_out(.+t)||_2^2
      <= gamma^2 k^(2m-1) integral b0(v)^(2m-1)
                          [integral_-infinity^(v-2t) A_k(u) du]^2 dv. (8)

Dominated convergence sends both bounds to zero: A_k is integrable,
b0^(2m-1) is integrable, and the inner tails tend to zero pointwise and
are uniformly bounded. This is strong L2 scattering for genuine noncompact
profiles, not exact finite-time separation. No uniform rate is claimed
without information on the initial tails. Weighted charge conservation and
strong L2 convergence identify the total outgoing charge with the initial
charge. Individual component charges need not be conserved.

### Released quantitative scattering rates

Suppose additionally A_k(u)<=C_A(1+|u|)^(-p) and
b0(v)<=C_B(1+|v|)^(-q), with p,q>1. These hypotheses follow, for example,
from the same bound on a0 and b0, multiplying C_A by exp(2k^m Q).
Let M_A=integral A_k and Q=integral b0^m. Splitting the first integral
in (8) at u=-t and the second at v=t gives, for t>=0,

    ||z(t)-z_out(.-t)||_2^2 <= k^(2m) [
       Q^2 C_A/(p-1) (1+t)^(1-p)
       +M_A (C_B^m/(mq-1))^2 (1+t)^(2-2mq)],
    ||w(t)-w_out(.+t)||_2^2 <= gamma^2 k^(2m-1) [
       M_A^2 C_B^(2m-1)/((2m-1)q-1) (1+t)^(1-(2m-1)q)
       +2 C_B^(2m-1)/((2m-1)q-1)
                       (C_A/(p-1))^2 (1+t)^(2-2p)].    (11)

Every exponent is negative. The factors2 in the last term count both
halves of the full-line integral. These are explicit sufficient algebraic
rates; no optimal decay exponent or derivative scattering is asserted.
The same estimates apply to the past after the time/space reflection and
to data at the finite gluing time if their tails satisfy these hypotheses.

## 3. Why large separated waves have an OPEN scattering basin

If z0 is supported strictly to the right of the support of w0, the integral
in (2) vanishes whenever b0(v)>0. Hence eta_k=0 regardless of either wave's
size. Their future motion is free; this is the organizing reference, not a
new derivation of the already known support-transport fact.

The functional eta_k is continuous in the L2 intersect Linfinity topology.
Here is an explicit estimate proving this, rather than relying on drawings
of separated supports. For two data sets label their squared amplitudes
a,b and a*,b*, write A,A* for (2), B*=||b*||_infinity, and
Qmax=max(integral b^m,integral b*^m). Then

    ||A-A*||_1 <= exp(2k^m Qmax)
        [||a-a*||_1+2k^m ||a*||_1 ||b^m-b*^m||_1],
    |eta_k-eta_k*| <= 2gamma(m-1)
        [||b^(m-1)-b*^(m-1)||_infinity ||A||_1
                           +(B*)^(m-1)||A-A*||_1].     (9)

The first estimate uses the mean-value bound for exp on a bounded interval;
the second uses |sup f-sup g|<=sup|f-g|. Squaring maps L2 intersect Linfinity
continuously into L1 intersect Linfinity, and the integer powers are locally
Lipschitz there. Thus all the differences on the right tend to zero.
The strict inequality (3) defines an open set. Every large outgoing separated
pair lies in this set, with genuinely noncompact perturbations allowed.

## 4. Released two-sided neighborhoods of large interacting solutions

Let (z*,w*) be a smooth solution with initial support in [l,r] and existing
on [-T,T], where T>(r-l)/2. Support transport gives outgoing separated waves
at +T. Under the transformation (t,x)->(-t,-x), the waves at -T are also
outgoing separated. This transformation reverses both right-hand-side signs
in (1); estimates (5)--(9) are absolute and unchanged.

On a ball of max component amplitude R the physical-coordinate force is
locally Lipschitz with constant

    L_R=2(2m+1)max(1,gamma) R^(2m).                     (10)

Translations are isometries in L2 and Linfinity. The integral equations,
a first-exit argument and Gronwall therefore make the time +/-T solution
maps locally continuous in their intersection norm. The same estimates apply
to the difference in L2; no small derivative norm is needed for amplitude
control. Smooth bounded derivatives ensure the separate classical existence
and continuation statement. Choose a neighborhood whose images at +T and
reflected -T satisfy (3). Sections1--2 then extend every such perturbation
for all positive and negative times with two-sided strong L2 scattering.

Consequently the set of global scattering data contains an open neighborhood
of every such compact reference. K2046 supplies arbitrary-size phase-locked
sextic references; K2050 supplies them for every m>=2 and gamma>0. The present
argument also applies to any other compact reference known to survive the
finite collision interval. This is a conditional reference theorem, not a
claim that every compact arbitrary-phase reference survives that interval.

For example, adding epsilon times two smooth complex Gaussian tails to any
one of those large references is admitted for sufficiently small epsilon.
The phases need not be constant and the perturbed support need not be compact.
This is a full L2 plus Linfinity neighborhood within the stated smooth class,
not merely a finite-parameter family or a fixed-support subspace.

### Continuity of the outgoing scattering map

On the open set defined by a fixed k in (3), the map from initial data to
(z_out,w_out) is continuous into L2 x L2. To check the nonuniform-time issue,
take a convergent sequence of initial data. Equation(9) gives A_n->A in L1;
also b_n^m and b_n^(2m-1) converge in L1 and all their norms stay bounded.
These convergent L1 families have uniformly small tails outside a sufficiently
large fixed interval. Split the two integrals in (8) outside that interval;
for t larger than its radius, each remaining inner integral lies in an
opposite small tail. Thus the scattering errors tend to zero uniformly along
the sequence. Finite-time solution continuity followed by a three-term
triangle inequality proves continuity of the outgoing profiles. Applying
the same reasoning after the finite-time gluing proves continuity of both
asymptotic profiles in the large-reference neighborhoods. This supplies no
inverse wave operator, differentiability or Lipschitz scattering modulus.

## 5. Checks, limitations and prior work

The producer certifies the density-source modulus identity using symbolic
real-coordinate differentiation and reciprocal-power identities.
A distinct Gaussian-rational probe evaluates the actual complex forces and tests
the reciprocal inequality, exponential Lipschitz bound and ordered-support
positive/negative controls. These finite checks verify their stated algebra
and fixtures. The global bootstrap, topology, derivative continuation and
strong-L2 limit are supplied by the written proof above. No numerical
trajectory is used as an existence certificate. Same-author internal checks
are not independent expert or proof-assistant acceptance.

The criterion is not forced by K2050's conserved data. It can fail on large
crossing data without implying blowup. m=1 is excluded from the reciprocal
power argument. No transverse PDE, quantum S-matrix or source-selected
physical state is inferred. SC-OP-04 ASSERTS the candidate four-field source
operator; SC-OP-05 is UNCERTAIN about its rival; SC-META-53 is UNCERTAIN about
physical positivity; SC-META-56 DISAVOWS an odd-action prerequisite. The
commuting two-field model supplies none of the missing common source dual,
fermionic statistics or observation quotient, and LT-SM8/LT-GR6b do not move.

Closest contextual comparison: the published abstract of [Small Data
Scattering for the One-Dimensional Nonlinear Dirac Equation with Power
Nonlinearity](https://doi.org/10.1080/03605302.2015.1081608) describes a small
weighted-Sobolev neighborhood. The abstract alone supplies no theorem transfer
to (1). Our proof is given directly for this asymmetric massless system;
no novelty or exhaustive prior-art claim is made.

Next: test whether a useful same-system large crossing family satisfies a
stronger causal envelope or admits a new estimate. Failure of (3) is not a
counterexample. The general unrestricted complex problem remains open.
