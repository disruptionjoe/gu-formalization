---
title: "K2045: Third and fourth exact thermal spacing phases"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: unrestricted finite/countable thermal model on the declared energy and spacing intervals; no GU or novelty claim
scripts:
  - tests/channel-swings/k2045_third_thermal_spacing_phase.py
  - tests/channel-swings/k2045_third_thermal_spacing_phase_probe.py
---

# K2045: Third and fourth exact thermal spacing phases

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
result: two further exact spacing phases, sharp physical boundaries and minimum resources
carrier: four-state bath times finite/countable pure-point catalyst LAYER=toy CHIRALITY=N/A
pairing: positive populations and worst-input marginal half trace distance ON=declared_bath_catalyst
real_structure: complex states with nonnegative real diagonal populations
grading: exact energy shells and connected occupied components
action_owner: repository-construction -- inherited energy-conserving shell channels
target: unrestricted optimum and physical-level necessity MAP-TYPE=intertwiner
```

[Verified conditional mathematics.] The nine-level Q competitor of
[K2043](k2043-chamber-offset-frontier-2026-10-25.md) belongs to a third exact
phase, which lasts through delta=628/1629. A fourth exact phase then lasts
through delta=2/5. Both boundaries have actual physical competitors beyond
them. These are unrestricted finite/countable results on the full energy
interval [1575/653,675/181], not optima of a fixed dimension search.

The result reuses the odd-tail T competitor and its threshold already found
in [K2039](k2039-thermal-component-undercut-2026-10-24.md). What is new is the
whole-domain optimum, the phase between the earlier boundaries and that
threshold, the next phase, and their necessary resource counts. It does not
claim to have discovered the T family or threshold again.

## 1. Endpoints, lines and exact formulas

Keep bath energies0,1,2,3 with populations(8,4,2,1)/15; nonnegative physical
catalyst levels with minimum spacing delta; the inherited exact shell channel;
and mean-energy budget E. Let each named pair below be (energy,return):

    A=(1575/653,729/2612), B=(675/181,81/362),
    D=(349/145,81/290), Q=(37/10,9/40),
    T=(28361/11755,6561/23510), C=(19/8,9/32).

A,B,D,Q have K2043's populations. T has populations
(4374,6561,729,81,9,1)/11755 on1,3,5,7,9,11 and completion0,...,12.
C has(3/8,9/16,1/16) on1,3,5 and completion0,...,6.
For points P,R define l(P,R;E) as their affine interpolating line. A shifted
point P_delta has the same return and energy EP+delta. Define

    fA = l(A,B_delta;E), fDQ = l(D_delta,Q;E),
    fQB = l(Q,B;E), fAT = l(A,T;E), fTB = l(T,B_delta;E).

On EA<=E<=EB the exact optimum is

    F_delta(E)=min(fA,max(fDQ,fQB))
                       for 2/145 <= delta <= 628/1629;      (1)
    F_delta(E)=min(max(fAT,fTB),max(fDQ,fQB))
                       for 628/1629 <= delta <= 2/5.        (2)

All lines here use the SAME delta, bath and channel. The maxima are essential:
using a single minimum of all lines would incorrectly extend a physical
segment beyond its available endpoint. This is a union of competing convex
piecewise-linear profiles, not one unrestricted convex hull.

In(1), fA wins from EA to its unique crossing with fDQ; fDQ then wins until
EQ=37/10; fQB wins from EQ to EB. In(2), fAT wins on[EA,ET], then fTB until
its unique crossing with fDQ, followed by fDQ and fQB. All segment lengths are
positive at strict spacings. A crossing between lines a1-s1 E and a2-s2 E is
(a2-a1)/(s2-s1); this gives an exact rational expression if desired.

## 2. Physical attainability and its domain

The fA branch uses low A and shifted B; fTB uses low T and shifted B; fDQ
uses low Q and shifted D. Their masses are determined by mean E. Their actual
spectra are the union of the two consecutive completions at offsets0 and delta.
Since0<delta<=2/5<1/2, the smallest union gap is delta; distinct fractional
residues cannot share a bath shell. The return and energy therefore add with
the same masses, including the shifted component's energy cost.

The fAT branch is a SINGLE component formed by interpolating the A and T
population diagonals after padding A with a zero at11. The fQB branch similarly
interpolates Q and B after padding Q with a zero at9. Direct bath-label maxima
have a common maximizing label at both endpoints of each segment, and the
clipped deficits have compatible signs there. Their affine dependence then
proves the same return formula over the ENTIRE population segment. Endpoint
sampling alone would not establish this fact.

The lines that are actually selected have nonnegative masses. For each spacing
interval, cleared endpoint inequalities show that the left line is at most RD
at ED+delta and is strictly above RQ at EQ; fDQ has the steeper negative slope.
Thus the crossing is between ED+delta and EQ. The A-to-T branch in(2) lies below
fDQ on its whole interval by its endpoint inequalities. Above EQ, fQB stays
below the left branch through EB. These are affine-cleared inequalities over
closed spacing intervals, verified at their endpoints, not a numerical grid.

## 3. Complete cutoff-eleven certificate

The cutoff-nine proof first gave a merely sufficient upper bound305/1629,
where its zero-return tail line touched energy10. That was NOT a physical
transition. The present calculation expands the same exact arrangement
construction through occupied energy11. It enumerates53 canonical supports,
671 edge-orientation cells,626412 hyperplane bases and20975 vertex records.
The complete cutoff-nine subbank agrees exactly with the inherited3137 rows.

Canonical supports have first root max(1,3-first_gap), gaps1,2,3 and adjacent
gaps summing at least4; an isolated root is1. Edge comparisons determine which
incoming bath contribution is maximal. Within one such cell, return is a sum
of positive parts of affine deficits and is therefore piecewise affine after
subdivision by deficit-zero planes. Coordinate, edge and deficit hyperplanes,
intersected with sum(p)=1, contain every vertex of that subdivision. Enumerating
all n-1 hyperplane bases and retaining nonnegative points satisfying the edge
orientation gives a complete finite set, including degenerate vertices.

For(1), every low cell is assigned at least one valid line from EACH pair
(A,DQ) and(A,QB). For(2), each low cell receives one from EACH of
(AT,DQ),(AT,QB),(TB,DQ),(TB,QB). A line is valid for a low cell when every
vertex there lies on or above it. Every line also supports ALL vertices of a
high component after adding delta to its energy, and satisfies f(12)<0.
The assignments remain fixed over their entire closed spacing interval.
After multiplying by the positive line denominator, every tested difference
is affine in delta, including shifted components. Endpoint checks therefore
certify the whole interval. The exact assignments and all vertices are saved
in the linked JSON; the producer independently regenerates them.

By [K2043](k2043-chamber-offset-frontier-2026-10-25.md)'s forced-ground proof,
at most one occupied component has original offset d_i<delta. This includes
first-gap1/root2 components; ignoring their forced unoccupied ground would be
wrong. All other components pay at least delta. The exceptional component has
one actual edge-orientation cell, so each pair supplies a valid global line
bound after the tail transfer below. Consequently

    R >= min(fA,fDQ) and R >= min(fA,fQB),

which combine exactly to(1)'s lower bound. The four pairwise bounds similarly
combine through the distributive identity

    max_{i,j} min(L_i,R_j) = min(max_i L_i,max_j R_j)

to give(2). If every component is high, every individual line is available.
No component is allowed to select different population chambers for different
parts of a fictitious mixture. This is why the cell assignments matter.

## 4. Tail, translation and countable transfer

Erase occupied canonical levels above11 without renormalizing. Write a valid
line as f(e)=a-s e with s>0, component mass m, erased mass q, erased canonical
energy h>=12q, original offset d_i and required offset ell=0 or delta.
The inherited zero-loss return-erasure result and the finite certificate give

    R_component >= a*m-s*e_actual
       +(12s-a+s*ell)*q+s*(h-12q)+s*m*(d_i-ell).          (3)

Every correction is nonnegative; the first is strictly positive when q>0.
Original offsets are retained. Summing gives R>=f(E), including the positive
unused-budget correction s*(E-total_actual_mean). Normality and finite mean
justify countable sums; all correction terms are nonnegative, and the inherited
erasure return is l1-continuous. Small tail mass is never substituted for a
bound on tail energy. Thus the finite certificates apply to arbitrary finite
or countable catalysts in this model, and the realizations in section2 attain
the resulting lower bound.

## 5. Equality and minimum physical levels

For spacings STRICTLY inside the third or fourth interval, positive tail and
offset margins remove tails, higher offsets and unused budget. The full
certificate enumerates all persistent zero vertices. For the competing lines:

- fA: low A and high B only.
- fTB: low T and high B only.
- fDQ: low Q and high D only.
- fAT: low A,T only and no high vertex.
- fQB: low C,Q,B vertices and no high vertex.

An equality population lies in a compatible subdivision face spanned by those
vertices. This is not permission to mix incompatible C,Q,B cells. The explicit
Q/B segment is feasible. For E>EQ, every equality decomposition needs a positive
B vertex because C and Q have energy at most EQ. Therefore every such diagonal
has all five odd occupied levels and needs its full eleven-level completion.
At EQ, Q supplies a nine-level optimum. Below EQ on the fDQ-winning branch,
only low Q/high D are possible, requiring nine plus nine distinct-residue
levels. The same reasoning gives the following sharp minima:

| Strict-spacing regime | Energy region | Minimum physical levels |
|---|---|---:|
| Third | EA<E<left/right switch | 22 |
| Third | switch<=E<EQ | 18 |
| Fourth | EA<E<=ET | 13 |
| Fourth | ET<E<left/right switch | 24 |
| Fourth | switch<=E<EQ | 18 |
| Both | E=EQ | 9 |
| Both | EQ<E<=EB | 11 |
| Both | E=EA | 11 |

At a left/right switch both branches attain; the smaller dimension is18.
For each positive odd diagonal, adjacent populated inputs force all four
outgoing levels of their shared bath shell, hence the entire consecutive
completion. Distinct fractional residues cannot merge these required levels.
The checker removes every completion level for A,B,D,Q,T individually and
finds a shell-capacity violation. The written equality argument, not merely
those tests, excludes a different smaller optimizer. Full equality and minimum
dimensions at the CRITICAL spacing values are left open; the optimum formulas
remain proved there. This table makes no claim about all optimizing unitaries
or coherences.

## 6. Sharp boundaries and next branch

At delta=628/1629, the original low-A/high-B line passes through T. Immediately
above, the physical unshifted T diagonal lies below the old third-phase formula
at ET; the other branch is strictly higher there. This is the already-known
odd-tail competitor, now matched to an unrestricted optimal phase boundary.
The fourth phase retains the connected A/T segment and shifts the A/B branch
to T/B. No extra numerical digits or additional isolated endpoints were needed.

At delta=2/5, shifted C lies on the D_delta-to-Q line. For every sufficiently
close larger spacing its chord to low Q improves that line. At E=7/2, the
right branch is strictly below the left branch and both channels are feasible,
so the improvement is an actual counterexample to the whole fourth-phase
formula. The checker executes both boundary witnesses at critical delta+10^-6.
The first attempt at E=16/5 did NOT beat the competing left branch; it was
rejected. A negative line coefficient alone would not have proved a transition.

This gives the next concrete candidate: low Q mixed with shifted C, requiring
sixteen levels, together with the existing piecewise left profile. Its full
optimality beyond2/5 is not asserted here; additional low contacts, including
67/19, and offset packing near1/2 must be checked before extending the formula.

## 7. Verification and limits

The producer uses exact integer cofactors for all626412 bases. The separate
checker reconstructs supports, edge/deficit planes from bath weights and uses
fraction-free row elimination to independently recover every cell's complete
vertex set. It also recomputes every return by direct bath-label maxima,
checks whole-interval supports,64 physical mixture/segment controls, both
boundary rivals, two full-segment common-cell proofs and53 necessary completion
removals. Four actual faults overextend each phase, corrupt T's return and
change a rival mass. Clean baselines must precede their rejection.

The independent implementations are same-author internal verification. The
finite enumeration is new; inherited canonical reduction, forced-ground packing
and zero-loss erasure are reused at pinned hashes and with explicit transfers.
The whole-domain and resource conclusions rely on sections2--5. Neither a
pass count nor a sampled catalyst is an unrestricted proof. No external review,
proof-assistant acceptance, novelty, source-register change, physics-ledger
movement or canon promotion is claimed.
