---
title: "K2039: Sharp first-order spacing law and a finite thermal counterexample"
status: active_research
doc_type: exploration
created: "2026-10-24"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: sharp uniform first-order spacing law and finite counterexamples; exact positive-spacing optimum and second-order coefficient remain open
scripts:
  - tests/channel-swings/k2039_thermal_component_undercut.py
  - tests/channel-swings/k2039_thermal_component_undercut_probe.py
---

# K2039: Sharp first-order spacing law and a finite thermal counterexample

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
result: sharp uniform first-order spacing law, an explicit dimension-independent lower bound and finite counterexamples
carrier: four-state bath times a finite positive-spacing catalyst LAYER=toy CHIRALITY=N/A
pairing: positive populations and worst-input marginal half trace distance ON=declared_bath_catalyst
real_structure: complex physical states with real nonnegative diagonal populations
grading: bath shells and resonance components, not fermionic grading
action_owner: repository-construction -- inherited energy-conserving shell channel
target: feasible return frontier and resource witnesses MAP-TYPE=intertwiner
```

The main result is the sharp first-order spacing law in Section7: the
unrestricted return frontier equals K1952's chord plus an explicitly determined
linear penalty in delta, with a uniform O(delta^2) remainder. The proof uses
finite polyhedral stability and two physically separated components. The same
construction gives a finite counterexample to the later countable odd-tail
candidate.

## 1. A finite catalyst beats the proposed infinite-tail endpoint

[Verified conditional mathematics.] Keep the bath energies0,1,2,3 and
populations(8,4,2,1)/15, the shell-channel class and the nonnegative physical
energy convention of K2037. Write delta for the minimum allowed separation of
physical catalyst levels. The countable odd-tail point

    E_inf=415/172, R_inf=12/43

is **not** the unrestricted optimum whenever0<delta<315/724. A finite22-level
construction already gives smaller return at exactly this energy. In
particular, at delta=1/4 its return is

    R=17783631/63725398,
    R_inf-R=201/63725398>0.

This resolves the optimality question for that candidate on this spacing
range; it does not determine the actual optimum. For delta>=315/724 this
particular comparison supplies no improvement. K2037's proved phases through
E0=1575/653 remain intact. The endpoint is an inherited repository construction,
not a GU source claim, and no physics, source or canon verdict changes.

## 2. The odd-tail recurrence is genuinely feasible

For integer m>=0 take odd inputs1,3,...,2m+3 with unnormalized weights

    w1=1, w_(3+2j)=(3/2)9^(-j), 0<=j<=m.

Set q=9^(-(m+1)). Their normalization and unnormalized mean are exactly

    Z_m=(43-27q)/16,
    H_m=(415-27(8m+21)q)/64.

Hence E_m=H_m/Z_m and R_m=3/(4Z_m). Complete the physical spectrum with every
integer0,...,2m+4. This is feasible at every0<delta<=1.

The edge flow from an input of mass p to its next odd neighbor of mass p'
is(3p-12p')/15. At the first edge p3=3p1/2, so incoming mass exactly fills
p1. At every following edge the ratio is9, so incoming mass exactly fills
the next population. Only p3 has positive deficit, giving R=p3/2.

The two adjacent normalized endpoints m and m+1 share these edge orientations.
Their interpolation preserves p1=2p3/3 and every old tail ratio. At the new
last input its mass is at most one ninth of its predecessor, so its deficit
is nonpositive throughout. The actual return is therefore affine on the
entire interpolation, with feasible line

    R=C_m(2m+5-E),
    C_m=48/(344m+445+27*9^(-(m+1))),
    E_m<=E<=E_(m+1).

This is a constructive recurrence, not an optimality theorem. The first new
segment beyond K2037 is

    R=729(11-E)/22432,
    1575/653<=E<=28361/11755.

Its physical completion has13 levels in the interior. The geometric series
also recovers E_inf and R_inf. Absolute summability justifies the inherited
countable-return passage; the new counterexample itself is entirely finite.

## 3. Restore convex mixing by separating the resonance components

K2037's failed same-ladder chord joined two diagonals on odd inputs1,3,5,7,9:

    A=(486,729,81,9,1)/1306,
    (E_A,R_A)=(1575/653,729/2612),

    B=(36,54,81,9,1)/181,
    (E_B,R_B)=(675/181,81/362).

Each has the physical integer completion0,...,10. Keep A's completion fixed
and translate B's entire completion by delta. For0<delta<=1/2 the union has22
levels and consecutive gaps delta and1-delta, so its minimum gap is delta.
The two ladders have distinct fractional residues modulo1; integer bath
energies cannot create a shared shell between them. Thus mixing with mass t
on B and1-t on A gives the **actual** return and physical mean

    E_delta(t)=E_A+t(E_B+delta-E_A),
    R_delta(t)=R_A+t(R_B-R_A), 0<=t<=1.

The shift costs t*delta in energy. Omitting this cost or merging the ladders
would be invalid. Shell capacities and bath-label maxima are checked directly
on the full rational spectrum by the independent probe.

For C=729/22432, direct subtraction gives

    C(11-E_delta(t))-R_delta(t)
      =t*C*(628/1629-delta).

Consequently every0<delta<628/1629 strictly undercuts the next connected
odd-tail line immediately to the right of E_A, and throughout its interval.
This threshold is sharp **for this A/B comparison**; it is not a universal
phase boundary. At equality the two lines agree. Above it this mixture lies
above that next line.

At E_inf take t=(E_inf-E_A)/(E_B+delta-E_A). The competing return is below
R_inf exactly when

    delta<315/724.

For delta=1/4 this gives t=17195/31862699 and the exact witness in Section1.
All ten input populations are positive and all22 completion levels are
present. This is an upper resource bound; no sharp minimum dimension is
claimed.

More generally, for endpoint m>=4 the sharp threshold for this comparison is

    delta_m=(R_A-R_B)(E_m-E_A)/(R_A-R_m)-(E_B-E_A).

These thresholds strictly increase from628/1629 to315/724. To see this
without extrapolation, write H_m-H_3 and Z_m-Z_3 as the weighted sum and mass
of added inputs11,13,...,2m+3. Their ratio is their strictly increasing mean,
which converges to11+2/8=45/4. The displayed threshold is a positive affine
function of that ratio. Thus for every delta<315/724 some finite odd-tail
endpoint is also beaten. For delta between the two thresholds the first new
segment can survive this comparison even though later endpoints fail it.

## 4. Recover K1952's chord with two components and a uniform rate

K1952 already proved this chord as the unrestricted finite infimum when no
fixed positive spacing is imposed, with endpoint attainment, interior
nonattainment and finite epsilon approximations using three components.
That result must not be relabeled a new optimum. K2037 independently supplies
the same global lower line for finite/countable spectra:

    L(E)=1053/2768-(2907/69200)E.

Its two contact points are exactly A and B. Set C_L=2907/69200. For any
E in[E_A,E_B] choose t=(E-E_A)/(E_B+delta-E_A) in the separated construction.
Combining its exact return with that inherited global lower bound yields

    0 <= F_delta(E)-L(E)
      <= C_L*delta*(E-E_A)/(E_B+delta-E_A)
      <= C_L*delta,                 0<delta<=1/2.

Here F_delta is the unrestricted finite/countable infimum at budget E. Thus

    lim_(delta down to0) F_delta(E)=L(E)

uniformly on the whole interval[1575/653,675/181]. The22-level physical
construction is sufficient for this uniform approximation; its dimension
does not grow as delta decreases. This recovers the inherited chord with a simpler two-component construction
and an explicit uniform error bound in the prescribed spacing. It does not assert that L is attained
for positive delta or that either A/B mixture is optimal at fixed delta.

## 5. Every fixed positive spacing has a strictly positive interior gap

For the same finite/countable model and every0<delta<=1,

    F_delta(E)>L(E),       E_A<E<E_B.

All these budgets are feasible: A's integer completion has spacing1 and
mean E_A<=E. Moreover, for every delta_min>0 with delta_min<=1 and every
E_A<a<=b<E_B, the gap has a positive minimum on the closed rectangle

    delta_min<=delta<=1, a<=E<=b.

This statement is uniform over unrestricted finite/countable dimension.
This is an alternative inherited attainment proof. Section6 directly proves
an explicit lower bound without using attainment, and Section7 supplies the
sharp uniform first-order spacing law.
The endpoint exclusion is essential: A and B attain the line at their own
energies for delta<=1. The theorem here does not address delta>1.

The proof transfers existing theorems rather than relying on fixed-dimension
compactness. K2010 proves that every feasible positive-spacing finite-budget
infimum is attained by an actual finite or countably infinite catalyst of
this model, and proves joint lower semicontinuity in spacing and budget.
Its hypotheses include nonnegative pure-point nondegenerate energies, ground0,
minimum spacing delta>0, a normal finite-mean preparation, exact spectral-
projection conservation and the fixed faithful bath. All are unchanged here.

If a countable protocol equaled L(E), the K2037 unnormalized erasure proof
for this line would force equality in every nonnegative charge:

    R-L(E)>=C_L(E-e)+C_L sum_i m_i d_i
        +C_L sum_i(h_i-10q_i)+(549/13840) sum_i q_i.

Here e is actual mean, d_i is each component's nonnegative canonical offset,
and q_i,h_i are its mass and canonical energy above9. In particular e=E,
all populated offsets vanish and all occupied tails vanish. Every occupied
physical level is therefore at most9. Retaining all physical levels through12
preserves every occupied shell and its channel construction. Positive spacing
makes this completion finite, giving a finite protocol with the same return
and mean. K1952's exact finite equality-face classification excludes such an
interior equality protocol: only A or B can attain the chord. Thus no
countable protocol can equal L(E).

The unrestricted attainment theorem now gives strict inequality for the
**infimum**. Merely excluding equality protocols, or citing K1978's
fixed-dimension compactness, would not suffice. Finally, the gap is lower
semicontinuous by K2010 and the continuity of L; a positive lower
semicontinuous function on the displayed compact feasible rectangle has a
strictly positive minimum. This argument extends K2010's earlier exposed-line
strictness consumer to the present K1952/K2037 chord; it does not reprove the
underlying compactness theorem or claim fixed-budget finite attainment.

## 6. Polyhedral stability gives an explicit lower bound

Set C=C_L, A=1053/2768 and Delta=E_B-E_A=155700/118193. The complete
cutoff-nine bank inherited from K2037 has183 edge-orientation cells and3137
vertex records. Direct exact evaluation gives

    gamma=min{R(v)+C e(v)-A : positive vertex defect}=9/5017000.

The only zero-defect diagonals are A and B. No edge-orientation cell contains
both: their edge from3 to5 has opposite signs. **Return is not affine on an
entire edge-orientation cell.** Subdivide each such cell by all deficit-sign
hyperplanes and choose the closed chamber containing the actual population.
Return is affine there, and every chamber vertex belongs to the complete
stored arrangement bank. The bank check thus justifies convex decomposition
inside a genuine affine chamber, never across incompatible signs.

Apply the K2037 erasure argument to each component, retaining its original
canonical prefix through9 without recanonicalizing it. Decompose each retained
population homogeneously into vertices of its affine chamber. Let alpha and
beta be total mass assigned to zero vertices A and B; let z be total mass on
positive-defect vertices, q erased tail mass, h erased canonical tail energy,
v=h-10q, D the actual offset-weighted mass and ell the unused energy budget.
All are nonnegative, v>=0, and

    alpha+beta+z+q=1,
    E=alpha E_A+beta E_B+e_bad+h+D+ell,
    0<=e_bad<=9z,
    G:=R-L(E)>=gamma z+kappa q+C(v+D+ell),
    kappa=10C-A=549/13840.

The last inequality preserves the unnormalized mass and high-energy tail
charge. For countably many components these identities and inequalities pass
by nonnegative summation; finite mean controls h and D. No truncation of the
physical dimension or assumption that small tail mass has small energy is
used.

Subtracting E_A or E from the energy identity gives

    beta >= (E-E_A-K_A G)/Delta,
    alpha >= (E_B-E-K_B G)/Delta,

where the explicit sufficient constants are

    K_A=max((9-E_A)/gamma,(10-E_A)/kappa,1/C),
    K_B=E_B/gamma,
    K=max(K_A,K_B)=2398126000/653.

For the second inequality it suffices that e_bad>=0 and E_B<10; negative
terms from v,D,ell may be discarded. These constants are intentionally loose.

Every component carrying positive zero-vertex mass has actual occupied
energy1+d, where d>=0 is its original canonical offset. A component can carry
only one endpoint type, because its chamber has at most one zero vertex.
The roots of distinct such components are distinct physical levels, hence
their offsets are separated by at least delta. At most one such component
has offset in[0,delta); all others pay at least delta. If that exceptional
component has A contact mass, all B contact mass pays at least delta, and
conversely; if none is exceptional, both types pay. Original component
labels and offsets are preserved throughout, including in the vertex
decomposition: the vertex pieces are not separately recanonicalized. The component's actual mass is at least its contact mass.
Therefore, including the case that one type is absent,

    D>=delta min(alpha,beta).

Consequently, with d(E)=min(E-E_A,E_B-E),

    G>=C delta min(alpha,beta)
      >=(C delta/Delta)(d(E)-K G),

which rearranges to the explicit unrestricted lower bound

    F_delta(E)-L(E)
      >= C delta d(E)/(Delta+C delta K),
      0<delta<=1, E_A<=E<=E_B.                         (10)

This proof does not infer a rate from compactness. It derives it from the
finite positive-defect margin, the preserved first-moment tail charge and
physical spacing between roots. In particular it already gives a uniform
Omega(delta) lower bound on every compact interior energy interval.

## 7. Swap the shifted endpoint to obtain the sharp leading coefficient

Shifting B while leaving A at its canonical position gives

    F_delta(E)-L(E)<=C delta (E-E_A)/(Delta+delta).

For the other half of the interval, leave B canonical and shift A upward by
delta. The B mass is now t=(E-E_A-delta)/(Delta-delta), and the exact return gap
is

    C delta (E_B-E)/(Delta-delta),
    E_A+delta<=E<=E_B.

Both constructions have the same22-level physical spectrum. On the lower
half E-E_A<=Delta/2 choose the first; on the upper half choose the second.
Since Delta>1 and0<delta<=1/2, the second choice is always feasible on that
upper half. At the endpoints the unused component may be omitted.

Combine these upper bounds with(10). Uniformly for E in the **entire closed
interval**[E_A,E_B],

    F_delta(E)=L(E)+a(E)delta+O(delta^2),
    a(E)=C min(E-E_A,E_B-E)/Delta,
    delta down to0.                                   (11)

One explicit sufficient uniform remainder constant for0<delta<=1/2 is

    |F_delta(E)-L(E)-a(E)delta|<=M delta^2,
    M=max(C^2 K/(2 Delta), C/(2(Delta-1/2))).

Indeed(10) lies at most C^2 K delta^2/(2 Delta) below a(E)delta. The first
upper construction lies below a(E)delta on its half, while the second lies
at most C delta^2/[2(Delta-delta)] above it. This proves the sharp first-order
coefficient, including zero coefficient and exact equality at the endpoints.
It does not identify an exact optimizer for positive delta, a sharp uniform
remainder, or the second-order coefficient. The large sufficient K and M are
proof constants, not estimates of actual optimal performance.

## 8. Checks, limits, and the next question

The exact producer checks13 finite tail endpoints, adjacent interpolation
controls, closed moments, thresholds and the rational22-level witness. The
independent probe reconstructs the return from individual bath-label maxima,
checks physical shell capacities and spacing, tests15 separated mixtures,
checks the exact uniform squeeze identity at nine rational controls,
recomputes all3137 cutoff-nine vertex values from physical bath-label maxima,
and checks20 swapped-placement/first-order remainder controls.
The all-m and all-interpolation claims rely on the algebra above, not a finite
sample count. Provenance hashes pin K2010, K1952 and the inherited shell/erasure evidence;
those hashes do not newly certify the predecessor theorems.

Actual faults cover population normalization, a missing completion level,
an invalid minimum-spacing demand, return corruption, and replacing the
separated mixture by a same-ladder convex combination. An inflated stability margin is rejected by the actual prior endpoint
(349/145,81/290). A spacing overreach control gives at delta=1/2 and E_inf

    R_delta-R_inf=141/147779992>0,

so the strict undercut is not extended beyond its proved range. These are
internal exact computations and independent implementations, not external
review, proof-assistant certification or an external novelty claim.

The exact zero-spacing frontier was already settled by K1952; its present
spacing-sensitive consumer is now explicit. The next
substantial question is the exact positive-spacing frontier or second-order
correction above E_A: can a lower certificate match a separated construction,
or does a changed shape/component improve its next-order cost? The wide-spacing connected recurrence
still has unproved optimality. This result removes the all-spacing odd-tail
optimality conjecture and the need to extend that false global certificate.
It does not replace the separate near5/4 accumulation problem, determine an
entire phase diagram, or certify any GU mechanism.
