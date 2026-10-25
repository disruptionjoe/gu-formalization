---
title: "K2068: Exact finite-tail population family and its minimizing length"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: explicit two-deficit odd-ladder thermal family; no unrestricted optimum or minimal physical dimension
scripts:
  - tests/channel-swings/k2068_thermal_population_construction.py
  - tests/channel-swings/k2068_thermal_population_construction_probe.py
---

# K2068: Exact finite-tail population family and its minimizing length

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
result: exact population family, all-integer tail-length minimizer and finite physical witness
carrier: four-state bath and finite nondegenerate integer catalyst spectrum LAYER=toy CHIRALITY=N/A
pairing: classical diagonal marginal return ON=declared_thermal_population_model
real_structure: nonnegative rational populations
grading: energy and support gaps, not source parity
action_owner: repository-construction -- K1935 model and K2059 two-deficit population
target: energy-constrained thermal return of one explicit family MAP-TYPE=intertwiner
```

[Verified conditional mathematics.] A 41-level finite physical catalyst, with 20 occupied
odd levels, improves K2059's countable upper witness at E=5/2:

    F_delta(5/2) <= 335946011010129/1206372108151072,
    old upper - new upper = 6939/289516035863067618208
                         approximately 2.396758431468003e-17,
    1/2 < delta <=1.

K2066's lower bound549971760412002337513926417/1976871225373814177206100780 is unchanged.
This tiny upper improvement does NOT materially close the remaining global gap.
The substantive result is an exact all-integer family optimization: N=20 occupied
levels is the unique minimizing tail length for every 249/100<=E<=251/100 in the
specified two-deficit family. The countable invisible tail is slightly worse. This
neither optimizes all populations on that support nor proves minimal dimension or
the unrestricted thermal optimum. It is GU-independent mathematics; source register,
physics ledger, canon and prior statuses remain unchanged.

## 1. Reuse and the new construction question

[K2059](k2059-energy-aware-thermal-tail-2026-10-25.md) already constructs a ten-occupied-
level two-deficit population and its infinite 1/9 tail. [K2066](k2066-thermal-terminal-response-2026-10-25.md)
strengthens the lower certificate. Neither proves that infinitely extending an
invisible tail is best after mass and energy are rebalanced. The question here is
which finite truncation minimizes actual return under BOTH constraints in that
explicit family. Standard linear algebra and finite numerical search are not new
physical mechanisms or evidence of unrestricted optimality.

The numerical reconnaissance first reproduced the existing witness. A 24-level
mixed-integer floating solve reported a much larger gain, but its tiny populations
and near-zero deficits did not survive exact reconstruction. The exact raw bath return of the displayed decimal population is
0.2784771049283266, versus its reported0.2784759258431873; the population
also misses exact normalization. That candidate was not accepted. Exact formulas below resolve the much smaller true family effect,
which ordinary displayed decimal precision conceals. No solver-optimality statement
is used in the result.

## 2. One exact family and its physical realization

Use the same bath(8,4,2,1)/15. Let the first ten occupied energies be1,3,...,19 and
fix adjacent dominance bits

    (0,1,1,1,0,0,0,0,1).

A1 bit means the lower-energy population supplies the larger shell input; equivalently
p_(i+1)<=p_i/4. A0 bit means the reverse. Let T have boundary diagonals T_00=2/5 and
T_99=1/10. Each1 edge adds1/10 in rows i,i+1 of column i; each0 edge adds2/5 in
rows i,i+1 of column i+1. These are the occupied-site returns after the same balanced
shell mixing as K2059, not an arbitrary transition model. Set M=I-T and

    B=M^(-1) [e1,e8],  p_(0:9)=B (x,y)^T.

For integer N>=10 append p_i=p_9*9^(-(i-9)), i=10,...,N-1. Every appended deficit is
zero, while the two retained nonzero deficits are x and y. Thus the actual
unnormalized return is x+y, provided populations and dominance inequalities hold.
The boundary contribution at a finite last point is exactly the same 1/10 diagonal
that it had before an invisible1 edge was appended; no fictitious zero-cost root is
introduced. The full physical spectrum is0,1,...,2N, not only the N occupied levels.

For each shell, put its heavier input into a balanced two-output block whose outputs
include the occupied sites; put a lighter second input into the remaining two sites.
There are at most two occupied inputs and four available sites in their shared shell;
boundary single-input shells have at least two. These disjoint 2x2 unitary blocks conserve
energy and trace, and direct bath-label summation gives total-variation return x+y.
All physical gaps are1, so the witness is admissible throughout1/2<delta<=1. Empty
physical levels remain part of the apparatus and its resource count.

## 3. Close mass and energy exactly

Put r=9^(-(N-10)). The omitted part of the infinite tail has mass r*p9/8 and energy
r*(8N+5)*p9/32. Thus the two linear equations for x,y are obtained from the infinite
family by subtracting this rank-one moment correction. Solving gives

    D = 34824 N r - 20223 r - 41518097,
    x = 81(-60 E r+11452 E+120 N r+75 r-170683)/D,
    y = -432(1451 E-3499)/D,
    f_N(E)=x+y
          =135(-36 E r+2228 E+72 N r+45 r-91213)/D.       (1)

The manifest contains the exact 10x2 matrix B and released N20 affine populations.
For N>=10, Nr<=10 and D<0. Feasibility on249/100<=E<=251/100 is proved uniformly,
not extrapolated from a finite list of N: let h=(N-10)r. Then0<=r<=1 and
0<=h<=1/9; the latter follows since k/9^k decreases for integers k>=1. After
multiplying each population, x,y and dominance inequality by -D>0, its numerator
is affine separately in E,r,h. The 168 exact corner checks in the producer are
nonnegative at E=249/100,251/100, r=0,1 and h=0,1/9. Multiaffine interpolation
therefore proves all these inequalities on the larger containing box. Appended
populations have positive 1/9 ratios and satisfy their 1/4 dominance conditions.
Mass and energy are exact by construction. This proves a continuum-in-E and
all-integer-N family, rather than merely sampled feasibility.

## 4. Unique finite optimum over every tail length

Substituting(N+1,r/9) into(1) gives the exact difference

    f_(N+1)-f_N =
      4320 r (1451 E-3499)(4456 N+9r-88985)
      /[(11608 N r+4867r-124554291)
        (34824 N r-20223r-41518097)].                    (2)

Both denominator factors are negative for N>=10 by Nr<=10. Also1451E-3499>0
throughout the displayed feasible interval. For 10<=N<=19,
4456N+9r-88985 <=4456*19+9-88985<0. For N>=20 the same expression is positive
already after discarding9r. Thus f_N strictly decreases through N20 and strictly
increases thereafter. Its countable limit is K2059's line

    f_infinity(E)=135(91213-2228 E)/41518097.

This proves unique N=20 optimality in the declared family, including comparison
with the countable limit. It does not rule out another orientation, more deficit
sites, another support or another thermal operation.

The whole N20 affine population remains feasible on the larger exact interval

    11836234695567/4865270085667 <= E
        <= 991560367479/368093049355.

The producer derives both endpoints from all exact affine population and dominance
inequalities. The all-N minimizing-length statement is only asserted on the smaller
uniformly feasible interval. At E5/2 this supplies the41-level upper bound above;
41 is a sufficient dimension, never a minimum claim.

## 5. Consequence for finite/countable and numerical reasoning

The invisible-tail identity holds at fixed unnormalized prefix, but comparing
normalized states at fixed energy requires rebalancing x and y. Equation(2) proves
that more invisible tail can eventually worsen return. The effect is exponentially
small but exact. The finite witness removes any need for a countably infinite
catalyst to attain this improved upper number. It does not make the global frontier
near-exact or justify repeated decimal refinement as the next priority.

The difference from the countable limit is explicit by(1); r times a linear function
of N bounds its numerator, and the denominators stay bounded away from zero. Hence
f_N-f_infinity=O(N*9^(-(N-10))) uniformly on any bounded feasible E interval. This is
a constructive dimension/error relation for this family, not a universal rate for
all thermal catalysts. Every bound and feasible affine population is reproducible
with rational arithmetic, without the mixed-integer scout.

## 6. Checks and hostile limits

The producer derives both moment formulas, f_N and its exact difference, checks 168
corner inequalities, derives the extended N20 interval and proves the all-N sign
threshold by exact integer inequalities. A separate implementation checks 117 exact
population/moment/return/physical-shell/affine obligations, with 3 real faults detected.
The bath-label replay reconstructs actual energy-conserving outputs rather than
trusting the matrix's deficit interpretation. Hashes pin prior model and lower-bound
inputs; no large inherited bank is regenerated or counted as a new proof.

Same-author mathematical review checks the principal risks: two deficit sites are
an ansatz, an infinite tail is not a dimension certificate, floating zero deficits
are not exact, and occupied levels are not the physical spectrum. No independent
specialist, proof-assistant or novelty certification is claimed. The remaining
substantial thermal route is a joint-terminal lower certificate or a genuinely
different feasible population family; extending this now-optimized tail again is
not that route. Source-to-physics control constraints, nonlattice phase estimates
and exact continuum wings remain independent contenders.
