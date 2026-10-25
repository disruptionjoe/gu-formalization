---
title: "K2031: An exact thermal phase edge and unbounded geometric families"
status: active_research
doc_type: exploration
created: "2026-10-24"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact geometric families and unrestricted21-level phase through its right edge; endpoint minimum dimension and remaining phase diagram open
scripts:
  - tests/channel-swings/k2031_thermal_phase_boundaries.py
  - tests/channel-swings/k2031_thermal_phase_boundaries_probe.py
---

# K2031: An exact thermal phase edge and unbounded geometric families

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
result: unbounded geometric families and unrestricted21-level phase with exact right edge
carrier: fixed four-state bath times finite or countable completed catalyst LAYER=toy CHIRALITY=N/A
pairing: positive bath/catalyst states and marginal half trace distance ON=declared_bath_catalyst
real_structure: complex physical states with nonnegative real diagonal populations
grading: bath energy and resonance components, not fermion grading
action_owner: repository-construction -- exact channel and energy-conserving shell unitaries
target: exact-mean families and all-size fixed-bath phase value and dimensions MAP-TYPE=intertwiner
```

## 1. New result and its exact ceiling

The main result is an unrestricted finite/countable catalyst phase with
F21(E)=(15398019-761157E)/32499160 for1/2<delta<=1 and
13/10<=E<=E*, where E*=8283273393/6147208289 (about1.3474854).
Below E*, its unique optimal diagonal requires21 physical levels. At E*,
a17-level diagonal also attains the optimum, and beats the21-level line
immediately above E*. Thus E* is its **exact right phase edge**. The minimum
dimension at E* and the next optimal phase are not classified. Section9
proves this statement from complete certificates, beyond the geometric-family
search. The route below preserves the physical counterexamples that led to it.

[K2029](k2029-multicomponent-thermal-placement-2026-10-24.md) proves the
unrestricted17-level line F17(E)=(985095-61407E)/2040416 on[7/5,8/5], at
1/2<delta<=1. It does not license extrapolation. Here two **actual physical**
competitors defeat its continuation:

- A21-level family has R21(E)=(20321037-992331E)/42923912 and crosses F17 at
  E_L=11399473059/8486952979 (about1.34318). It is strictly better immediately
  below that crossing, including E=13/10.
- A13-level family has R13(E)=(8885-775E)/17532 and crosses F17 at
  E_H=214602655/126183719 (about1.70072). It is strictly better immediately
  above that crossing, including E=9/5.

Both crossings lie inside both competitors' exact feasibility intervals.
The17-level affine diagonal itself stays feasible on
[115329/89105,14079/7295], about[1.29430,1.92995]. Thus it loses optimality
before either of its own physical faces ends. These are bounds on its possible
unrestricted phase, **not proofs that either crossing is an unrestricted
transition** or that13/21 are necessary dimensions.

A longer-rise competitor below improves even that21-level line. Neither line
is promoted to an unrestricted transition.

The follow-through solves a countably infinite two-integer geometric family
at every exact mean5/4<E<=18/5, without a dimension cutoff. It produces physical
upper bounds for every0<delta<=1. The family includes a countable boundary
member at mean5/4 and return4/9, approached by growing finite constructions.
It then removes the fixed-rise restriction and proves the three-integer family
optimum at11 exact energies, again without a head, rise or tail cutoff.
No optimality or infinite-dimension necessity is claimed for the unrestricted
catalyst problem at that boundary.

## 2. Physical family

Keep bath energies0,1,2,3, probabilities(8,4,2,1)/15, and the channel and return
convention of K2029. For integers h>=1 and m>=0, put populations on consecutive
odd occupied energies1,3,...,2h+2m+5:

    p_i=9^(h-1-i)u,                       0<=i<h,
    p_h=(u+4v)/10,  p_(h+1)=v,
    p_(h+2+k)=(3v/2)9^-k,                 0<=k<=m.     (1)

The full physical spectrum is every integer0,...,2h+2m+6; its dimension is
2h+2m+7. It passes the inherited shell-capacity test, including its unoccupied
completion levels. For

    u>0, v>0,       8/3<=u/v<=36,                     (2)

the shell maximizers have a descending head, two reverse edges at the turn,
and a descending tail. Direct bath-label evaluation leaves positive return
deficits only at the first head population and the peak3v/2. Hence

    R=(9^(h-1)/2)u+(3/4)v.                            (3)

Ties in(2) cause no discontinuity. These are genuine channel-feasible
populations, not optimizer vectors without an implementing spectrum.

## 3. Exact normalization and energy

Set z=9^h, q=9^(-m-1), and

    A=(5z-1)/40,             c=(25z-8h-9)/160,
    B=247/80-27q/16,
    d=247h/40+3923/320-27(8m+8h+29)q/64.

Then normalization is Au+Bv=1 and mean energy is cu+dv=E. Therefore

    D=Ad-Bc>0,  u=(d-BE)/D,  v=(AE-c)/D.              (4)

The inequality D>0 follows because c/A<5/4 while the v-part's mean d/B is
larger: its occupied energies start at2h+1>=3. For E>5/4, v>0. Condition(2)
is exactly

    L_(h,m)=(36c+d)/(36A+B) <= E
      <= U_(h,m)=((8/3)c+d)/((8/3)A+B).               (5)

Substitution into(3) gives an affine line a_(h,m)+b_(h,m)E. Its slope is
negative since its unnormalized slope numerator is -(112z+27)/1440.
The new low/high competitors are(h,m)=(3,4),(1,2); the old17-level line is(2,3).

## 4. Every tail length, not a finite tail sweep

For fixed h and E with AE-c>0, subtract the rational values at m+1 and m.
Their denominators are positive. Elementary expansion shows their difference
has the sign of

    T_h(m)=(896z+216)m-1080hz-112z+513+135z/9^(m+1).  (6)

More precisely, the difference numerator after multiplying both positive
denominators is q(AE-c)T_h(m)/3840. This sign is independent of E. It is strictly increasing in m because

    T_h(m+1)-T_h(m)=896z+216-120z/9^(m+1)>0.

Also T_h(h)<0<T_h(2h+1). For m>h the last term is15/9^(m-h), a noninteger,
whereas all other terms are integers; thus T_h(m) never vanishes there.
For m<=h it is negative. There is a **unique** unconstrained minimum at

    m_h=min{m in[h+1,2h+1]: T_h(m)>0}.                (7)

The first12 values are2,3,4,5,7,8,9,10,11,13,14,15. More tail is not always
better, and a finite search through a fixed maximum m is not the proof.

Feasibility must still be imposed. At fixed E<=18/5, the ratio
r_m=(d-BE)/(AE-c) strictly increases with m: the added tail population has
energy2h+7+2m>E. Thus feasible m form a contiguous interval of integers,
possibly unbounded. Project m_h onto that interval. This gives its exact
minimum; if the interval starts beyond m_h, find its first integer by increasing
m until r_m>=8/3. If it ends before m_h, select its last integer. The comparison
with the explicit limiting ratio proves whether that search terminates.
The algorithm includes a countable-tail endpoint when it is the only feasible
member. It never infers absence from a failed finite search.

## 5. Every head length and the finite exact algorithm

For m tending to infinity, set q=0 in(4). The limiting upper feasible energy is

    U_(h,infty)=5/4+10(29h+40)/(16*9^h+145).           (8)

It strictly decreases to5/4. To check monotonicity, cross-multiply consecutive
terms: the positive numerator is9^h(3712h+4656)-4205. For any fixed E>5/4,
there are therefore only finitely many possible heads: once U_(h,infty)<E,
all larger heads are impossible. Since r_m increases, finite upper endpoints
never exceed(8). No arbitrary support cutoff occurs in this exclusion.

There is at least one feasible member at every energy in this domain. Already
m=2 suffices: writing z=9^h, its endpoints satisfy

    L_(h,2)-5/4=(944h+1615)/(4(243z+118)),
    U_(h,2)-5/4=(1304h+1795)/(4(18z+163)),
    U_(h+1,2)-L_(h,2)
      =(163944hz+491427z+102437)/(4(162z+163)(243z+118))>0.

Both endpoint sequences tend to5/4, their adjacent intervals overlap, and
U_(1,2)=1181/325>18/5. Thus their union covers the stated domain.

The solver enumerates exactly those heads, applies section4's constrained
unique-tail minimum to each, includes every feasible countable-tail limit,
and takes the least return. This proves the optimum **inside family(1)** at
the specified exact mean. It is not a proof about arbitrary spectra, multiple
components, other population patterns, or optimization over all means below E.
Every output nevertheless is a valid physical competitor under upper budget E.
The report contains all candidates and the winning physical spectrum for11
exact energies, including1250001/1000000,13/10,3/2,9/5 and18/5.

## 6. Countable boundary and resource accumulation

The pure infinite descending head

    p_i=8/9^(i+1), occupied energy1+2i, i>=0,

has total mass1, mean5/4 and return4/9. All integer physical levels are retained.
Every energy shell is finite and satisfies the same capacity inequality;
the inherited countable shell-unitary and l1 return construction applies.
This is a normal finite-mean state, not a formal nonnormalizable limit.

Choose a fixed ratio r in(8/3,36), use m=m_h, and normalize(1). As h grows,
its mean E_h approaches5/4 from above, its return tends to4/9, and its dimension
grows. Indeed the numerator of E_h-5/4 before division by rA+B is
[((247-2r)h+336-r)/40]-(27q/8)(m+h+3). Since
q(m+h+3)<=(h+3)/9 and r<=36, it is positive and of order h. The formulas give E_h-5/4 of order h*9^-h. From(6),(7),
m_h/h tends to135/112, so this explicit sequence has

    dimension / log_9(1/(E_h-5/4)) -> 247/56.          (9)

This is a construction's asymptotic resource cost, **not a necessary dimension
law**. Other spectra may be cheaper or have better return. Finite truncated
pure heads provide another control: they have mean below5/4 and return above
4/9, tending to the same countable member. They are not silently identified
with the exact-mean turn family.

## 7. A longer rise defeats the first low-energy extrapolation

The attempted backward support line with slope1/44 for the first21-level
candidate fails: the physical pure head(729,81,9,1)/820 on occupied energies
1,3,5,7 has mean256/205 and return729/1640, below that line based at13/10.
The report preserves the exact population and nine-level completion.

The two-integer family is not the whole physical frontier. At E=13/10,
a17-level population with three descending head atoms, a two-step rise and
one descending tail step has the affine return

    (188379-9297E)/397636.

It is strictly below the first21-level line in section1. The report stores
its complete exact population and integer spectrum; the probe recomputes the
bath-shell return. This is an actual physical counterexample to calling the
first family globally optimal. The all-pattern linear-program discovery was
only a lead; the rational physical witness is the evidence.

Let h>=1, l>=1 and m>=0 now vary independently. Replace the turn/tail in(1) by

    bridge=(u+4v)/10,
    rise=(3/2)^k v,              k=0,...,l,
    tail=(3/2)^l v/9^j,         j=1,...,m.            (10)

The head is unchanged. All occupied energies are consecutive odd integers;
the full integer completion has dimension2h+2l+2m+5. The same ratio range
8/3<=u/v<=36 gives the same physical shell construction. With w=(3/2)^l,
return is Pu+wv/2, P=9^(h-1)/2. A and c remain as in section3, while

    B=25w/8-8/5-9wq/8,
    d=w(200h+200l-75)/32-(16h-32)/5
      -9wq(8h+8l+8m+21)/32,      q=9^(-m-1).        (11)

The normalization/mean equations(4) are unchanged. D>0, and v>0 for E>5/4.
Here l=1 exactly recovers the original family. Finite h,l are unbounded;
the countable-tail endpoint is again included by setting q=0.

For fixed h,l, the difference of consecutive tail returns, after multiplying
D_m D_(m+1), is q w(AE-c) T/2880, where

    T=(640wz+72w-512z)m-360hwz-360lwz+72lw-512lz
      +2200wz+99w-2304z+45qwz.

It increases strictly, since its increment is
640wz+72w-512z-40wzq>0 for w>=3/2,z>=9,q<=1/9.
Its coefficient of m is positive, so its first nonnegative value exists.
This gives the unconstrained minimum, allowing a tied neighboring tail if
T=0. Project it onto the feasible tail interval exactly as in section4.
The ratio increases with m because each added tail atom has energy>E.
The limiting ratio proves termination and determines endpoint feasibility.

## 8. Excluding every omitted head and rise

A feasibility bound alone cannot exclude arbitrarily long rises: a tiny
high-energy population may be feasible. An **objective lower bound** closes
this gap. Normalize the u- and v-parts separately. Their means satisfy

    e_u=c/A<5/4,              e_v=d/B>=2h+1.

More explicitly, e_u=5/4-(2h+1)/(5z-1) and
P/A-4/9=4/(9(5z-1))>0. Also B<25w/8, so the v-part's return per unit mass
w/(2B)>4/25.
If eta is the total mass of the v-part, normalization and exact mean give
eta=(E-e_u)/(e_v-e_u). Therefore every feasible l,m at head h obeys

    R >= L_h(E)=4/9-(64/225) min(1,(E-e_u)/(2h+1-e_u)). (12)

The lower bound increases with h and tends to4/9: e_u increases to5/4,
so the fraction decreases (or remains capped at1). Hence any supplied
physical incumbent below4/9 excludes every sufficiently large head.
The original family supplies such an incumbent at each of the11 reported
energies. This theorem does not assert that this particular incumbent
constructor succeeds below4/9 for every possible energy.

For each retained h, the ratio at m=0 increases strictly with l and tends
to infinity. Increasing l adds a rising atom of energy2h+2l+5>E; its positive
contribution to d-BE grows geometrically. Once this ratio exceeds36, every
larger l is infeasible, because adding any tail only increases the ratio.
This is a finite exact rise exclusion, with no imposed rise cap.

Combining(12), the rise exclusion and the tail theorem gives a terminating
exact search of the entire declared three-integer family whenever a feasible
incumbent below4/9 is supplied. The report records every retained head, the
first excluded rise, each minimized finite/countable tail candidate, the
winning physical witness and the first excluded head. At the11 test energies:

| Exact mean E | Winning (h,l,m) | Completion dimension |
|---|---|---|
| 1250001/1000000 | (9,3,7) | 43 |
| 1251/1000 | (5,2,5) | 29 |
| 63/50 | (4,2,4) | 25 |
| 13/10 | (3,2,3) | 21 |
| 27/20, 3/2, 17/10 | (2,1,3) | 17 |
| 9/5, 2, 3, 18/5 | (1,1,2) | 13 |

These dimensions describe the witnesses, not minimum resource requirements.
The new21 branch is

    R(E)=(15398019-761157E)/32499160,

and its value at13/10 is144085149/324991600. The report also gives its exact
feasibility interval and its crossing with F17. None of these within-family
optima supplies a lower bound for arbitrary population patterns, additional
components, arbitrary spectra or all means below the given upper budget.

## 9. Matching unrestricted theorem on a new low-energy interval

A complete certificate closes the global gap on the specific interval

    13/10 <= E <= E*=8283273393/6147208289,       1/2 < delta <= 1.

For the same bath, channel, upper mean-energy budget and marginal return as
K2029, every finite or countable physical catalyst, with any number of
components, has return at least

    F21(E)=a-cE=(15398019-761157E)/32499160.            (13)

The(h,l,m)=(3,2,3) population attains it. For E<E*, every optimizer has that affine
diagonal, saturates its budget and requires all21 physical levels0,...,20.
Thus21 is the sharp minimum dimension **below the right endpoint**. At E*,
the old17-level diagonal also attains the optimum; its minimum dimension is
not classified here. Extra empty levels,
coherences and implementing unitaries are not claimed unique. This theorem
comes from the all-pattern certificates and placement proof below, not from
the three-integer family search. It does not cover all energies in section8.

### Connected components and an integer tail improvement

Write b=43/2000. The stored exact bank covers every admissible canonical
connected support through occupied energy21 and every edge orientation,
including zero-population faces. As in K2027, epigraph variables express the
positive-part bath return without selecting deficit signs. Two rational duals
per cell prove

    R+b e >= F21(13/10)+b(13/10),      e<=13/10,
    R+c e >= a,                      13/10<=e<=E*,   (14)

or certify the section infeasible. There are616194 connected
duals,9150 all-energy component duals and25 short-placement
certificates. All multipliers and reduced costs are
checked exactly by two implementations; numerical discovery is not acceptance.
The report's compressed JSON is a complete proof object, not a hash-only claim.

Translate a connected component to its canonical minimal position first.
Its occupied energies are integers because all connected gaps are bath
energy differences1,2,3. Translation only reduces its mean. Erase canonical
energies above21 and let q,h be the erased mass and energy. Crucially,
**h>=22q**, not just h>21q. The retained prefix remains in the certified class.
Zero-loss unnormalized erasure, homogeneity and the slope floor b give, at
canonical mean e<=E,

    R >= F21(E)+b(E-e)+b(h-22q)+kappa(E)q,
    kappa(E)=(22-E)b-F21(E)
      >=27618129/16249580000>0.                     (15)

A canonical shift tau contributes at least b*tau to the corresponding slack.
Countable tails use the inherited l1 erasure/return theorem. It would be
incorrect to assert a22q charge after erasing at an arbitrary untranslated
real-energy threshold; canonical translation is the required first step.
At equality there is no tail, translation or energy slack.

### Arbitrarily many physical and occupied components

The separate component bank establishes two all-energy support lines
R+lambda e>=alpha_lambda, for lambda=b,c. It enumerates every canonical support
through14, including those starting at2, and proves15lambda>alpha_lambda.
Erasure above14 therefore extends each line to all lengths and countable
components. Their exact intercepts and margins are in the report.

Use K2029's compulsory-physical-interval argument: the first connected occupied
component starting at1 forces every integer from0 to L, where L=1 for a
singleton and L=s_last+3-d_last otherwise. All other occupied components have
canonical offset at least x0=min(L+1/2,s_last+2). This covers fractional
physical components and disconnected occupied components sharing physical
completion levels; it does not assume every completion was chosen consecutive.

For L>=8, x0>=8. Both other-component support lines strictly exceed the
corresponding line in(14):

    alpha_b+8b-[F21(13/10)+b(13/10)] > 0,
    alpha_c+8c-a > 0.                               (16)

The remaining components have mean at least9. The first component's mean is
therefore at most the total budget. Sum the appropriate backward or main
line exactly as in K2029. Every nonzero mass outside the first component has
a strict positive charge, so equality requires only that component.

For L<8, the report includes every short first-component orientation cell.
Variables q,h,r for the aggregate of all other components obey
h>=(x0+1)q and the two translated support lines above, plus the inherited
R+e/4>=3/4 and R+3e/20>=63/100 lines. Exact duals either prove minimum energy above E* or have
strictly positive margin above a throughout[13/10,E*]. Means below13/10
are included by increasing the relaxed h to the lower endpoint: every
constraint relaxes and return is unchanged. This is a relaxation argument,
not an assertion that the altered aggregate energy is physically realizable.

If the first populated physical component has no occupied level1, its mean
is at least2. Every later physical component has occupied mean greater than
3/2 at delta>1/2. Hence this case cannot meet E<=E*<3/2, including arbitrary
numbers of occupied components within each physical component. These cases
exhaust the finite/countable physical class.

### Equality, resource cost and the scope of the phase claim

For E<E*, every contact cell in the connected certificate is checked by exact
complementary slackness. A strictly negative upper-energy multiplier forces
E=E* at equality, so those endpoint-only contacts are excluded from the
interior uniqueness claim. For every remaining contact, normalization, exact mean, tight inequalities and
zero reduced-cost variables imply the same affine diagonal on
1,3,...,19. The separate checker verifies the homogeneous nullspace implication.
The endpoint populations share shell maximizers and deficit signs, proving
affine attainment over the whole interval. Shared-shell rank forces every
physical integer0,...,20. Together with(15),(16) and the strict short margins,
this proves the claimed unique diagonal and minimum21-level dimension for
E<E*. The separate physical17-level witness at E* proves the endpoint
optimum but does not exhaust all endpoint diagonals.

For a near-optimal protocol below the short-case gap, the same proof bounds
outside-component mass by its return surplus divided by the smaller margin
in(16). For a connected protocol, (15) bounds tail mass by epsilon/kappa_min,
energy slack by epsilon/b, and tail energy by(22/kappa_min+1/b)epsilon.
These bounds do not control the number of negligible empty levels.

The old unrestricted17-level theorem on[7/5,8/5] remains intact. At E*,
F21=F17, and the old17-level population remains strictly physically feasible
on an interval above E*. Since its slope is more negative, it beats F21
immediately to the right. Combined with the global lower bound through E*,
this proves the exact right edge of the21-level phase. Required dimension
is21 just below the edge, while17 suffices at the edge: a drop of at least4.
It does not prove that the17-level population is optimal immediately above
E*. The open interval(E*,7/5), endpoint minimum dimension, the left edge of
this21-level phase and the near5/4 accumulation region remain unresolved.

The spacing boundary is again substantive. At delta=1/2, combine the two
five-level spectra0,...,4 and1/2,...,9/2. With weight(E-6/5)/(3/2) on the
second occupied population, K2029's explicit shell construction has return
57/100-E/10, strictly below(13) over this new interval too. Both endpoint
populations, means, shell capacities and returns are replayed. Thus a strict
right jump at1/2 also occurs here, at least F21(E)-(57/100-E/10); the actual
left optimum and exact jump magnitude remain unproved.

## 10. Verification and research consequence

The exact producer and separate bath-label checker replay all616194 connected,
9150 component and25 short-placement certificates (17 strict bounds and8
minimum-energy exclusions). The23 main-line equality contacts separate into
2 interior contacts and21 additional endpoint-only contacts. Both dual-sign
and normalization corruptions are rejected after a clean certificate baseline.
The producer also checks normalization, actual shell capacity and bath return
for192 finite controls,11 original-family searches,11 unbounded three-integer
family searches, both crossing witnesses and the longer-rise counterexample. The separate checker derives
normalization from geometric sums, reconstructs actual bath-shell maxima,
independently minimizes over the analytically reduced candidate set, and checks
five symbolic identities, including both generalized tail identities. It
evaluates97 original and1514 generalized finite candidates independently.
Actual population, completion, return,
phase-coefficient and tail-coefficient corruptions are rejected only after a
clean baseline. Input hashes are separate provenance checks. Infinite statements
rest on sections3--9, not on the finite number of controls. Same-author internal
verification only; no external specialist, proof-assistant or novelty claim.

The initial21-level guess and its backward line failed actual physical
controls; the longer-rise successor was followed into complete exact duals.
The bank was first discovered on[13/10,4/3], then its exact affine right-hand
sides were evaluated through E*. All cells remain certified there;21 upper
constraints attain their limiting value at E*. Endpoint contacts are kept
separate from interior uniqueness. A feasible rounded dual with a tiny
suboptimal gap was not accepted as a physical counterexample: every discovery
dual was reconstructed exactly before the final bank was admitted.
Strongest overclaim: calling the family minimum a global frontier. The notes,
report and solver preserve that ceiling. Strongest contrary routes: another
head length defeats the inherited17 tail while its populations remain valid,
and a longer rise defeats the first21-level competitor. Weakest transfer seam: counting every unoccupied completion level and
justifying infinite h/l/m exclusion; both are explicit above.

The next unrestricted question is the optimal phase immediately above E*,
the left edge of the21-level phase, or the near5/4 accumulation region.
Section9 supplies the matching all-size, all-component proof for this phase.
The old[7/5,8/5] theorem remains intact. Source register, GU physics ledger,
canon and physical-claim postures do not change.
