---
title: "K1991: Tight-cut factorization and an exact central pulse"
status: active_research
doc_type: exploration
created: "2026-10-23"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no source identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k1991_tight_cut_pulse_factorization.py
  - tests/channel-swings/k1991_tight_cut_pulse_factorization_probe.py
---

# K1991: Tight-cut factorization and an exact central pulse

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
result: complete forced-support decomposition, explicit capped central pulse and improved feasible norm certificate
carrier: actual optimal scalar phase and width9 characteristic strip LAYER=toy CHIRALITY=N/A
pairing: Lebesgue marginals and real L2 norm ON=characteristic_strip
real_structure: real bounded measurable controls with amplitude23/100
grading: three row bands and disjoint free column ranges, not source chirality
action_owner: repository-construction -- fixed scalar transport problem
target: regional exact feasibility and whole-pulse norm bound MAP-TYPE=intertwiner
```

## Result and scope

For the ACTUAL optimal phase of [K1974](k1974-scalar-excursion-separation-2026-10-23.md),
the two saturated cuts force the pulse outside three disjoint free regions.
The remaining feasible set is an exact Cartesian product of two reflected
wing problems and one central rectangle problem. This is a continuum
factorization, not a grid approximation.

An explicit capped pulse is constructed on the entire central rectangle,
with both marginals exact. Replacing that region in any existing feasible
pulse gives the certified improved whole-pulse bound

    2.34940177149 < ||v_dagger||^2 < 2.7547213641,
    ||v_dagger - w_1989|| < 0.636648.                    (1)

The lower bound and clipped witness w_1989 are reused from
[K1989](k1989-capped-pulse-dual-certificates-2026-10-23.md).
The old feasible upper was2.8566 and distance bound0.712179. The new upper
uses K1974's existing wing feasibility; it is NOT an explicit formula for the
whole pulse. The central formula is not asserted to minimize its norm.
These are pulse L2 bounds, not Dirichlet phase-energy errors.

## 1. Exact forced support and independent residual problems

Use D={(u,z):-3<=u<=3,u<=z<=u+9}, M=23/100, and K1969's algebraic
root t in(9/20,23/50). Set

    L=3-t, A=3-2t, B=6+2t, W=B-A=3+4t.

Every feasible optimal-phase pulse has column integral0, row integral
2phi(u), and |v|<=M. Equality for the cuts u<=-t and u<=t forces the
minority side of each column to its appropriate amplitude endpoint.
In a column interval [lo,hi], if the cut has length m<=ell/2, v=+M on
the cut; if m>=ell/2, v=-M on its complement. This follows because the
nonnegative pointwise slack integrates to zero. Endpoints have measure zero.

Solving those elementary length inequalities gives EXACTLY these free regions:

    D_L: -3<u<-t,       u<z<A,
    D_C: -t<u<t,        A<z<B,
    D_R: t<u<3,         B<z<u+9.                       (2)

D_R is the image of D_L under (u,z)->(-u,9-z). On the rest of D the values
are forced: +M on left-band rows after A, -M on right-band rows before B,
and on central-band rows -M before A and +M after B. The two cuts never
force opposite signs at the same point. Their free regions have disjoint
row bands AND disjoint column ranges, so modifying one cannot affect another's
residual constraints. Conversely, satisfying all three residual problems and
inserting the forced signs satisfies every original marginal. This proves
product equivalence, not just a necessary restriction. Each factor is nonempty
by restriction of K1974's feasible pulse. The squared norm splits into a
fixed forced contribution plus the three regional norms; the unique global
minimum-norm pulse consists of regional minimum-norm solutions, with reflected
wings by uniqueness. The explicit central candidate below is only an upper witness.

For reproducibility, the full left-wing residual is particularly simple.
Put x=u+3 in[0,L], y=z+3 in[x,2L], and q=v/M. Its exact constraints are

    |q|<=1,
    int_x^(2L) q(x,y)dy = 2phi(x-3)/M -9+2L-x,
    int_0^min(y,L) q(x,y)dx = 0                 (0<y<L),
                              y-L             (L<y<2L). (3)

Equivalently h=(q+1)/2 lies in[0,1] and has column integral y/2 and row
integral phi(x-3)/M+2L-9/2-x. The right wing is its signed reflection.
These equations retain the actual algebraic phase, including the plateau
and outer quadratic piece; replacing it by a test marginal would solve a
different problem. They identify the remaining constructive problem precisely.

## 2. Central marginals and an explicit solution

Write x=u/t in[-1,1]. On the central row band phi(u)=-b u, where
b=1-lambda(1-t)^2/2. The algebraic contact equation proves

    2bt=M(3+2t).                                      (4)

The forced parts of that row contribute2Mu. Therefore the free central
row integral must be -MWx. The residual column integral equals M(z-3)
on[A,3], zero on[3,6], and M(z-6) on[6,B]. Normalize the ramps by

    y=(z-3)/(2t) on[A,3],
    y=(z-6)/(2t) on[6,B].

They cover[-1,0] and[0,1], each with dz=2t dy. Define

    f(a) = (3+4t)a/(3+4ta),  0<=a<=1.

On the central rectangle set v=M q, with

    q(x,z) = -sign(x) f(|x|)                     for3<=z<=6,
    q(x,y) = sign(y)                             if |y|>|x|,
             -sign(x) f(|x|)                     if |y|<|x|. (5)

Values on the dividing lines may be assigned arbitrarily. Since0<=f<=1,
the cap is exact. In a ramp column, the tails |x|>|y| cancel by oddness,
while the inner interval contributes2y. Hence int v du=2tMy, the required
column residual. In a positive-x row, the two outer ramp tails have opposite
sign and equal length, while the inner ramps have total width4tx. Adding
the middle width3 gives

    int_A^B q dz = -(3+4tx)f(x) = -Wx.

Reflection gives the negative-x case. Thus BOTH marginals are exact for
the actual root, with no quadrature residual or limiting feasibility claim.
The formula has jumps and does not contradict the earlier C1 nonattainment.

## 3. Norm, improvement and a useful ceiling

Direct integration of(5) gives

    N_C = 2t M^2 [(3+4t)^2 I(t)+2t],
    I(t)=int_0^1 x^2/(3+4tx) dx
        =1/(8t)-3/(16t^2)+9 log(1+4t/3)/(64t^3).       (6)

For an elementary comparison, take sign(y-x) on both ramps and -x on
the middle. That also has exact marginals. Its norm is M^2(8t^2+2t).
For every0<x<1, (5) transfers equal row mass from the saturated inner ramp
to the unsaturated middle, preserving columns by paired reflection. The
exact squared-norm reduction per normalized positive row is

    4tx (1-x)^2 / (1+4tx/3) >0.                       (7)

Thus(5) is a strict feasible improvement, not an arbitrary replacement.
It is only optimal within this paired transfer family; general central
perturbations have not been exhausted.

The central area is2tW. Retaining ANY feasible wings and replacing its
central region by(5) yields

    ||v||^2 <= U = M^2[54-2tW] + N_C.                 (8)

The remaining cap bound includes all forced regions and both wings. Exact
rational root isolation and a positive atanh series with an explicit tail
bound enclose(6)-(8), giving U<2.7547213641. Substitution in K1989's strong
Fenchel inequality proves(1), even though w_1989 remains marginally infeasible.

A regional lower bound is also available for future optimization. On a full
rectangle, zero-mean row and column functions are orthogonal. The uncapped
additive solution gives

    inf ||v_C||^2 >= M^2[2t+16t^2/3].                 (9)

It need not respect the cap, so(9) is a lower bound rather than another
feasible candidate. Exact central minimum-norm and both explicit wings remain
open. Saturation factorization does not supply a convergence rate for solving
them.

## 4. A concrete wing construction is ruled out, without an all-wing claim

A natural explicit competitor for(3) fills a half-length interval in each
column. In normalized units, for0<k<1/2 choose h_k to be the indicator of

    [k y,(k+1/2)y]                     for0<y<L,
    [k(2L-y),k(2L-y)+y/2]              forL<y<2L.

It respects the triangular domain and has EXACT column mass y/2. Its row
mass has successive slopes

    2/k-1/(k+1/2),  -1/(k+1/2),  -1/(1/2-k),

with breakpoints kL and(k+1/2)L. These slopes decrease, so every such row
profile is concave. The k=0 limit has row mass2(L-x), also concave. Convex
mixtures of these kernels therefore remain concave.

The required wing row mass in(3), however, has second derivative
lambda/M>0 on0<x<1, because there phi(x-3)=x[1-lambda(1-x)/2]. This strict
convexity excludes the entire proposed mixture family. It does not exclude
other interval placements, non-interval columns, or measurable kernels;
feasibility is already proved. The failed construction narrows a concrete
attempt rather than declaring the wing impossible or relabeling a test
marginal as the actual phase.

## 5. Verification and claim boundary

The producer verifies7292 rational identities/cap controls and rational
whole-domain log enclosures. The separate probe proves the contact polynomial
identity and central marginals symbolically, derives an independent alternating-
series norm enclosure, and checks the forced-region geometry on rational
controls. Its7202 mixed symbolic/interval/geometry obligations pass; four
changed denominator, column, upper-bound and distance inputs fail genuine
mathematical assertions after the baseline. Universal support and marginal
claims rely on the proofs above, not the geometry samples or pass counts.

Strongest overclaim: calling the central formula an explicit full or globally
minimum-norm pulse. The wing existence input and open regional minima prevent
that. Strongest contrary case: dividing lines and shrinking strip columns;
all statements use Lebesgue a.e. values and exact column lengths. Weakest
remaining seam: an explicit solution of(3). No new external theorem is needed
for this self-contained construction. Same-author separate implementations
are internal checks, not independent specialist acceptance or formal proof.
SC-META-53 remains UNCERTAIN. Source, physics-ledger and canon verdicts are unchanged.
