---
title: "K2128: Contact-limit channel convergence and logarithmic energy cost"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional empty-Fock model; no source selection, stable massive QFT, GU recovery, novelty or external certification
scripts:
  - tests/channel-swings/k2128_contact_limit_energy_cost_probe.py
---

# K2128: Contact-limit channel convergence and logarithmic energy cost

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
result: conditional exact dynamics and quantitative limits
carrier: empty Fock over counterpropagating L2 line species R,L0,L1 LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert Fock metric and spatial graded local von Neumann factors ON=declared_carrier
real_structure: complex adjoint; no GU-selected reality
grading: CAR parity; propagation direction is not physical chirality
action_owner: repository-construction -- smooth pairwise unitary conjugacy of free transport
target: full recorded instrument, locality and free-energy compatibility MAP-TYPE=intertwiner
```

## Result and scope

For the same [K2127](k2127-smooth-collision-locality-2026-10-27.md) family,
U_e(t) converges strongly to the sharp K2125 propagator. It has an explicit
O(sqrt(epsilon)) error on each fixed smooth finite code with a fixed probe,
but generally no operator-norm convergence. For a fixed midcollision packet
with a nonzero crossing trace and theta not in2pi Z, its positive free-energy
proxy diverges logarithmically as epsilon decreases. Exact completed records
and small channel error cannot supply a uniform budget for an unbounded
energy observable. This does not repair the unbounded-below generator.

## 1. Strong and finite-code convergence

F(r/epsilon) tends to 1{r>0} almost everywhere. The modulus-one multipliers
therefore converge strongly on each sector by dominated convergence; the
Fock direct sum follows by truncating its particle-number tail. Multiplication
by the fixed translation preserves this argument for each t.

For a quantitative bound, take orthonormal R modes f_1,...,f_d, arbitrary
code/reference input, one fixed normalized smooth probe g in |+>, and empty
spectators. Put

    M = min(d ||g||_infinity^2, ||sum_j |f_j|^2||_infinity).

The R one-particle density is bounded by the code projector density, and
its integral is at most d. For each relative slab |x-y-a|<epsilon, its
expected number of active R/L1 pairs is at most epsilon M: length2epsilon
and the active rail probability1/2. The event probability of any such pair
is no larger than its expected count. This is an operator bound uniform on
the code, not an independence assumption about its particles or reference.

At initial coordinates the smooth and sharp phases can differ only in the
union of two slabs centered at a=0 and a=-2vt. Outside those slabs both F
values equal their sharp steps. The pointwise difference of phases has
modulus at most2. Thus for the code preparation isometry V,

    ||(U_e(t)-U_sharp(t)) V|| <= min(sqrt2, sqrt(8 epsilon M)).   (1)

If initial separation excludes the first slab, the second bound improves
to min(sqrt2,2sqrt(epsilon M)). The sqrt2 cap uses that the L0 branch is
identical and has weight1/2. The standard isometry estimate follows directly
by comparing purifications and trace distance; after any SAME output
recording channel the half-diamond error is at most min(1,the RHS). Nothing
here is uniform over varying codes, concentration, particle number or probes.
Full crossing with margins can improve this bound to exactly zero (K2127).

## 2. Failure of operator-norm convergence

Fix t>0 and theta!=0. Use normalized one-R/one-L1 packets with initial relative
coordinate near epsilon u, width o(epsilon), fixed transverse packet and
u in(-1,1) away from0. At final coordinates both profiles are1, so the limiting
multiplier difference has modulus

    |exp[i theta(F(u)-1{u>0})]-1|.                             (2)

A nontrivial continuous transition supplies a u making this positive.
These epsilon-dependent concentrated inputs prove failure of operator-norm
convergence. For symmetric F and theta=pi the supremum lower limit is at
least sqrt2 by u approaching0 from below. When theta=2pi k!=0, the sharp
interaction is free but a nontrivial smooth transition still winds through
nontrivial phases; it does not become a uniformly free family. Fixed-code
convergence is compatible with this counterexample because its inputs vary.

## 3. Logarithmic intermediate free energy

In one R/one L1 put r=x-y,s=(x+y)/2. Then H0=-2iv partial_r. Choose fixed
smooth compact incoming data in r<0 separated from the initial interface; at a fixed
midcollision time let the translated amplitude a(r,s) have nonzero a(0,s)
on a set of positive measure, and support away from the second phase interface.
For all sufficiently small epsilon the state is

    u_e(r,s)=exp[-i theta F(r/epsilon)] a(r,s).                 (3)

If theta is not in2pi Z, there are positive constants c,C,epsilon0 depending
on this fixed data, profile, phase and velocity such that

    c log(1/epsilon)-C <= <u_e,|H0|u_e>
                        <= C(1+log(1/epsilon)), 0<e<epsilon0. (4)

These are form expectations. Each is finite for fixed epsilon; no coefficient
or constant independent of the frozen packet is asserted.

The fractional-Sobolev background is standard; see [Di Nezza, Palatucci and
Valdinoci](https://arxiv.org/abs/1104.4345). The estimates here are written out
for this specific family and carry no novelty claim.

For completeness, the Fourier fractional-seminorm identity identifies
<u,|p_r|u> with a positive universal constant times
integral ds dr dh |u(r+h,s)-u(r,s)|^2/h^2. It follows by Plancherel and
integrating |exp(iph)-1|^2/h^2, then scaling h by |p|.
For the lower bound choose a compact transverse subset where |a(0,s)|>=a0>0.
Continuity makes the phase jump across r=-x and r=y bounded below for
x,y small and positive outside the layer, since |exp(-i theta)-1|>0.
Integrate x in[2epsilon,delta/2], y in[x,2x]. This gives a positive
multiple of integral dx/x, minus a bounded endpoint error.

For the upper bound, write the translation difference of(3) as the sum of
the smooth amplitude difference and its phase difference. Compact support
and bounded a, its first derivatives, and F' give

    ||u_e(.+h,.)-u_e||^2 <= C h^2/epsilon,  0<|h|<=epsilon,
                           C |h|,          epsilon<|h|<=1,
                           C,              |h|>1.            (5)

The first estimate uses ||partial_r u_e||_2^2<=C/epsilon; the second uses
the O(|h|+epsilon) measure of the transition-crossing strip and the smooth
amplitude bound; the third uses normalization. Integrating (5)/h^2 gives
(4). This proof uses the actual regulator scale rather than a fixed grid.

The positive free proxy Epos=v(|p_x|+|p_y|) has the same order because

    Epos=2v max(|p_r|,|p_s|/2),
    2v|p_r| <= Epos <= 2v|p_r|+v|p_s|.

The phase is independent of s and the transverse form expectation stays
bounded by smoothness of a. Hence (4) transfers to Epos. It is not an
interacting conserved energy or a controller-work definition.

### Countercontrols and follow-through

If a vanishes near the crossing slice, no logarithmic lower bound follows.
If theta is an integer multiple of2pi, the limiting phase jump vanishes;
the nontrivial layer can retain bounded nonzero energy, but (4)'s lower
bound is not licensed. In fact its phase difference is supported only in
a width-O(epsilon) layer, giving O(1) fractional energy by the same three
ranges with the middle increment bounded by C epsilon+C h^2.
A discontinuous profile is the sharp model and has infinite intermediate
energy, not the regulated finite value. A spatial finite-range error is
also not an ultraviolet energy budget.

For data satisfying the lower-bound hypotheses, any uniform budget Emax
on this free-energy proxy, in 0<epsilon<epsilon0, requires epsilon >= exp[-(Emax+C)/c]. Conversely
the finite-code estimate requires epsilon <= delta^2/(8M) to GUARANTEE an
error at most delta by this particular bound. The second condition is
sufficient, not necessary; exact final crossing has zero error at finite
epsilon, so these inequalities do not prove a universal detector-error
lower bound. They expose the resource assumptions of taking a contact
limit at intermediate times. A different stable causal field interaction
remains a distinct construction problem.

## Source and acceptance boundary

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 and SC-META-53 remain
UNCERTAIN; SC-META-56 DISAVOWS an odd-action prerequisite. This supplied model
changes none of those source polarities, ledger0.263, LT-SM8/LT-GR6b or canon.
Finite exact controls check equations and witnesses. Infinite-dimensional domains,
local-algebra statements and analytic bounds rest on the written arguments and
independent internal review, not finite certificates or external certification.
