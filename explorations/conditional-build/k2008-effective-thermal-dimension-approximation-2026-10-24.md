---
title: "K2008: Effective thermal dimension approximation at fixed spacing"
status: active_research
doc_type: exploration
created: "2026-10-24"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no GU identification, sharp complexity, unrestricted attainment, novelty or external certification
scripts:
  - tests/channel-swings/k2008_effective_thermal_dimension_approximation.py
  - tests/channel-swings/k2008_effective_thermal_dimension_approximation_probe.py
---

# K2008: Effective thermal dimension approximation at fixed spacing

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
result: explicit finite-dimension approximation at every fixed positive spacing and a countable-catalyst equality of infima
carrier: fixed extreme four-state channel, four-level Gibbs bath, nondegenerate catalyst LAYER=toy CHIRALITY=N/A
pairing: worst-input marginal half trace distance with upper initial mean energy ON=independent_initial_registers
real_structure: complex conserving unitaries and real energy populations
grading: actual bath resonance components, not source chirality
action_owner: repository-construction -- unchanged finite thermal model plus explicitly stated countable extension
target: quantitative dimension and spacing resources for the exact channel MAP-TYPE=intertwiner
```

## 1. Result, reuse and the question resolved

Keep precisely K2006's finite thermal model and notation
`F_d(delta,E,t)`. Write `F_infty(delta,E,t)=inf_d F_d(delta,E,t)` for the
infimum over all FINITE dimensions at the same positive minimum spacing.
For every feasible spacing `delta>0`, temperature `0<t<1`, budget `E>1`,
and integer `N>E`,

    0 <= F_(2N+7)(delta,E,t)-F_infty(delta,E,t)
       <= (E-1)/(N-E).                                      (1)

The unrestricted finite-dimensional infimum is thus approximated by an
**attained finite-dimensional optimum** with an explicit dimension bound.
For an error tolerance `epsilon>0`, it suffices to take

    N=ceil(E+(E-1)/epsilon),    d=2N+7.                      (2)

This is a sufficient `O(E/epsilon)` resource bound, not a necessary or sharp
one and not an efficient algorithm claim. At `E=1` every feasible instance
has return `1/2`, attained by the pure three-level construction (feasibility
then forces `delta<=1`). Infeasible
spacing/budget pairs are excluded rather than subtracting infinite values.

The same infimum results if the catalyst is allowed a countably infinite,
nonnegative, nondegenerate pure-point spectrum with ground zero and the
same positive minimum spacing, a normal trace-class initial state of finite
mean energy, and an exact conserving unitary. Section4 proves the extension;
it is not inherited silently from finite-dimensional formulas. There is no
claim that the unrestricted optimum is attained by a finite or infinite
catalyst, and no extension to continuous spectra, accumulation at finite
energy, degenerate levels, correlated inputs or approximate channels.

The result builds on, rather than rediscovers:

- K1943 sections5–6: energy-preserving tail normalization and a quantitative
  cutoff for the UNSPACED convexified hierarchy;
- K1950: the one-sided sharp-return tail inequality;
- K1972/K2006: physical two-component dominance, now preserving spacing;
- K1978/K1996: finite-dimensional positive-spacing attainment and finite
  exact programs.

The new step keeps ACTUAL positive spacing while converting a cutoff into
an explicit bound on physical dimension. It also settles the finite-versus-
countable infimum under the stated discrete-spectrum hypotheses. No collision
limit or free classical flag is used in (1).

## 2. Tail normalization preserves the energy budget and full shells

Start with any finite protocol at budget `E`. Pinch and use the inherited
sharp shell implementation. Its return is

    R(p)=1/2 sum_s (p_s-I_s(p))_+ <=1/2,

with `sum p_s=1`. Every occupied energy is at least one: the lowest occupied
shell requires a lower physical partner, whose resonance distance is a
positive integer, and all physical levels are nonnegative.

Remove occupied populations at energies strictly greater than integer `N>E`.
Let their total mass be `q`, and let `p_low` retain the other populations
WITHOUT renormalization. Since all occupied levels are at least one,

    q <= (E-1)/(N-1) < 1.                                (3)

K1950's one-sided inequality, applied at this actual absolute energy cutoff,
gives

    R(p_low) <= R(p)+q/2.                                (4)

Its proof uses at most one edge crossing from each occupied path prefix to
its discarded suffix, and `L_g<=1`; it applies uniformly in temperature and
to fractionally shifted spectra. Summing over components is legitimate.
Normalize the low populations to `p'=p_low/(1-q)`. Homogeneity and `R<=1/2`
give

    R(p')-R(p) <= q(R(p)+1/2)/(1-q)
                  <=q/(1-q) <=(E-1)/(N-E).               (5)

If `q=0`, simply keep the preparation. If `q>0`, every discarded energy is
greater than `N>E`, hence greater than the original mean. The conditional
mean of the retained population is therefore no greater than the original
mean. Normalization in this particular truncation DOES NOT spend additional
energy. No return or energy repair is hidden in a new component.

Retain every original PHYSICAL energy at most `N+3`, including unoccupied
completion levels and ground zero. For an occupied retained site `s<=N`,
every bath shell it uses has energy `s+b<=N+3`. Every physical catalyst
level `a` in that shell satisfies `a<=s+b<=N+3`. Thus none of its physical
shell positions was removed. Removing high occupied inputs only weakens
the rank inequalities. The sharp shell theorem therefore implements the
same exact full channel on this retained spectrum and support. Deletion
preserves nondegeneracy and minimum spacing. Truncating physical levels at
`N`, instead of `N+3`, would generally destroy a required completion.

## 3. Count the actual physical levels after two-component reduction

Apply K1972/K2006 to the truncated finite protocol. Freeze its actual
component shapes and normalized preparations, then reweight to at most two
populated components without increasing energy or return. Delete entire
zero-weight components and translate the surviving spectrum down to ground
zero. All surviving energies remain in `[0,N+3]`; spacing is unchanged.

Each original surviving connected bath-resonance component lies in one
integer coset. The component containing ground zero lies in the integer
coset and has at most `N+4` levels in this interval. A second component on
a noninteger coset has at most `N+3`. If the second component shares the
integer coset but is separated by a large gap, the ACTUAL nondegenerate
union has at most `N+4`, not two copies of the same integers. Consequently

    physical dimension <=2N+7.                           (6)

This counts unoccupied completion levels. There is no extra ground flag:
the common downward translation restores ground zero inside the surviving
spectrum. One can alternatively reduce before truncation for finite inputs,
but truncating first also applies directly to the countable extension below.

Equations(3)–(6) give a physical approximation to every original protocol.
Apply them to arbitrarily near-optimal finite protocols and take their
optimization error to zero to obtain (1). Finite-dimensional attainment
supplies the attaining upper optimizer; it is not an assertion of
unrestricted attainment. Larger `d` inherit the same upper bound. In
particular, with `N=floor((d-7)/2)>E`,

    F_d-F_infty <=(E-1)/(floor((d-7)/2)-E).               (7)

There is an effective enclosure consequence at rational `delta,E,t`. Choose
`N` by(2), evaluate K1996/K2006's COMPLETE finite program at `d=2N+7`, and
call its rational optimum `u`. Then

    max(0,u-(E-1)/(N-E)) <= F_infty(delta,E,t) <= u.

This gives a finite algorithm for a certified interval of any requested
positive width, including at the spacing thresholds themselves. The chosen
finite-dimensional upper endpoint has a physical witness. The algorithm
may be very expensive; these large programs are not claimed executed here.
Section4 transfers the same enclosure to the enlarged countable class.

## 4. Countably infinite discrete catalysts do not lower the infimum

Here the extension is explicit. Let the catalyst Hilbert space have a
countable energy eigenbasis, with nonnegative nondegenerate energies,
ground zero and minimum gap at least `delta>0`. Initial states are positive
trace-class operators of trace one with finite mean energy. The finite
system and four-level bath are unchanged and initially independent. Exact
conservation means that the bounded unitary commutes with all total-energy
spectral projections, equivalently with every total time translation. A
formal unbounded commutator is not used as a substitute for this condition.

**Trace-class pinching.** The covariance identities in K1933 remain valid
for these bounded unitaries and trace-class states. Let `P_M` project onto
catalyst energies at most `M`. The positive spacing makes this a finite-rank
projection, and `P_M sigma P_M -> sigma` in trace norm. Cesaro time averages
and energy pinching are trace-norm contractions. On each finite-rank
approximation, off-diagonal energy matrix entries average to zero; the
triangle inequality then proves trace-norm convergence of the full Cesaro
average to the diagonal state. The induced system channel and the
worst-input marginal-return functional are uniformly continuous in the
preparation's trace norm by complete-positivity contractivity and the triangle
inequality. Convexity/covariance therefore preserve the exact target and
cannot increase return. Diagonal energy probabilities, hence finite mean,
are unchanged; no continuity of an unbounded energy observable is assumed.

**Shellwise sharp return.** For a fixed bath-plus-catalyst energy there are
at most four catalyst/bath positions, because the bath has four distinct
energies and the catalyst is nondegenerate. The extreme-Gram rank and return
argument of K1943 is therefore finite in each shell. For clarity about
exactness under population restriction, a countable mixture implementing
the exact target can be split into any positive branch and its complement.
The target fixes each pure system basis state, so every positive branch
does too and is a Schur channel. Extremality of the target correlation
matrix then forces each such branch to implement the same target. Thus
restriction and renormalization to retained initial branches preserves the
exact full channel; it does not merely approximate the target.

The sharp shell constructions can be chosen in each finite energy shell.
Their direct sum is a bounded unitary, completed on unused columns and
strongly conserving energy. All return contributions and incoming flows
are nonnegative and summable; the inherited disjoint-bath-label estimate
`sum_edges(x+y)<=1` remains valid by monotone limits. Hence the same sharp
return formula and all-input bound extend by Tonelli/absolute convergence.
The one-sided tail estimate also sums over countably many path prefixes:
each crossing is charged to a distinct discarded endpoint of total mass
at most `q`. Infinite individual occupied paths cause no boundary-at-infinity
term.

**Finite approximation.** Now perform section2's cutoff BEFORE applying
K1972. Positive minimum spacing makes the entire physical window
`[0,N+3]` finite. All retained occupied shells are unchanged, their normalized
mean is no larger, and (5) bounds their return. Only then apply the finite
two-component theorem and count(6). Thus every admissible countable protocol
has a finite physical approximation with the same explicit error.

Every finite protocol belongs to the enlarged finite-or-countable class;
if an exactly infinite carrier is required it can be padded by unoccupied,
sufficiently remote separated levels with conserving unitary completion.
Conversely (1)'s construction approximates every countable protocol. Sending
`N` to infinity proves equality of infima. This does not establish a
finite-dimensional optimizer for a countable optimum.

## 5. Effective joint dimension and spacing resources

Write `R_star(E,t)` for the unrestricted UNSPACED finite-protocol infimum.
K1943 already proves that it is convex, nonincreasing, satisfies
`R_star(1,t)=1/2`, and obeys

    R_star(E,t) >=3/2-E.                                 (8)

These statements imply a useful uniform modulus. Convex secant slopes are
nondecreasing, and (8) bounds every secant from the left endpoint below by
`-1`; consequently every later secant lies between `-1` and zero. Thus
`R_star` is 1-Lipschitz in energy for EVERY `0<t<1`. This is a conservative
bound, not the exact initial slope.

K2006's heavier-component-at-zero construction costs at most `delta/2` in
mean energy, uniformly in finite dimension. Take the unrestricted infimum
in that physical construction and use the pure baseline near `E=1`:

    R_star(E,t) <= F_infty(delta,E,t)
      <=R_star(max(1,E-delta/2),t), 0<delta<=1/2.

Together with the modulus this gives a dimension- and temperature-uniform
return estimate `F_infty-R_star<=delta/2`. Combining with(1),

    0 <= F_d(delta,E,t)-R_star(E,t)
       <=delta/2+(E-1)/(N-E),
    d>=2N+7, integer N>E>1, 0<delta<=1/2.                (9)

For tolerance `epsilon>0`, choose

    delta<=min(1/2,epsilon),
    N=ceil(E+2(E-1)/epsilon), d>=2N+7.

Then the total error is at most `epsilon`, with actual spacing and exact
channel realization. At fixed `E,t`, ANY simultaneous `d->infinity` and
`delta->0+` therefore converges to `R_star`, and both iterated limits agree.
Unlike an abstract joint-limit statement, (9) specifies sufficient finite
resources. It does not identify the optimal scaling, the full positive-
spacing frontier, or a dimension-uniform validity threshold for the exposed
two-ladder formula.

## 6. Verification and closing boundary

The standard-library producer uses exact rational arithmetic. It truncates
actual multi-component spectra, checks shell completion, normalizes their
populations and minimizes component weights by enumerating one- and two-
weight vertices. A separate probe computes return from bath-label shell
maxima and performs null-vector component elimination instead. No producer
mathematics is imported by that probe. Controls include nonzero tails,
zero tails, a deleted original ground component, same-coset separated
components, support exactly at the cutoff, completion above the cutoff,
and several temperatures.

An infinite geometric family gives a further exact consumer. On physical
levels `0,1,2,...`, occupy `2k+1` with population `(1-r)r^k`, `0<r<1`.
Its mean is `(1+r)/(1-r)`, its tail above `N` is
`r^floor((N+1)/2)`, and its sharp return is an elementary geometric sum.
The producer evaluates that sum by the incoming-excess formula; the probe
derives its root and interior coefficients directly from the four bath
labels. Finite-prefix realizations retain the required physical shell
completion and satisfy (1). These examples check the implementation; the
trace-class/shell argument, rather than any finite sample, proves section4.

Full production and a separate full replay pass84 physical cases,18 exact
infinite-family controls and12 effective resource choices. The independent
probe passes125 exact control groups and rejects six mathematical faults
after a green baseline: lost tail normalization, increased mean energy,
missing shell completion, an incorrect two-coset count, an altered infinite
geometric return and an underpaid joint error budget. Five input hashes are
checked separately as provenance, not theorem evidence.

The first producer attempt exposed an exact-arithmetic harness defect at
zero tail mass: an empty Python sum returned integer zero, so dividing it
by two introduced floating arithmetic. Explicit rational zeros repaired the
producer and probe. This is a harness correction, not a counterexample to
the tail inequality or mathematical-fault credit. All reported executions
occur after that correction. Independent internal review checked the
finite/countable transfer and the written resource bounds; no external or
proof-assistant review is claimed.

Reproduce from the repository root:

```text
python tests/channel-swings/k2008_effective_thermal_dimension_approximation.py --write
python tests/channel-swings/k2008_effective_thermal_dimension_approximation.py
python tests/channel-swings/k2008_effective_thermal_dimension_approximation_probe.py
```

The strongest overclaims would be treating (2) as a lower complexity bound,
allowing accumulating spectra in section4, dropping physical completion
levels at `N`, charging coincident tags as actual levels, or treating finite
approximation as exact unrestricted attainment. None follows. The next
discriminating questions are sharper necessary/sufficient dimension rates,
an exact all-dimension positive-spacing frontier, or a genuine new
source-compatible physical construction. Another three-component census,
unqualified infinite-catalyst claim or temperature sample is not that result.

Source, physics-ledger and canon verdicts remain unchanged. These are
conditional internal mathematical results, without proof-assistant,
external expert or novelty certification.
