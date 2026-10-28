---
title: "K2193 Ordered anticommuting Clifford constraints"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: normalized zero-order adapters for the declared fixed-splitting coupled operator; no source or physical quotient claim
scripts:
  - tests/channel-swings/k2193_noncommuting_clifford_constraints_probe.py
---

# K2193 Ordered anticommuting Clifford constraints

> **GU-COMPARATOR-ROUTING: scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: K2193 anticommuting nonscalar-square exclusions and ordered necessary equations
carrier: full real Cl77 S128 vector-spinor plus scalar, W(3,1) and N(4,6) fixed LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: algebraic field-equation evaluation; no physical Hilbert pairing ON=declared_carrier
real_structure: real Clifford representation and independently supplied common reverse row
grading: full Dirac; tangent and normal exterior degrees are bookkeeping
action_owner: repository-construction: simple-contraction coupled operator and its fixed four-dimensional target
target: complete normalized zero-order principal and coefficient intertwiners MAP-TYPE=intertwiner
```

## Result and scope

Within the fixed normalized Clifford-adapter model, anticommuting ports
{v,t}=0 cannot satisfy all ten original lower equations if their squares
are proportional, if either square is nilpotent, or if the normal-grade10
product component vanishes and either square is scalar. The other square
need not be scalar or diagonalizable. An exact ordered necessary equation
also constrains the remaining anticommuting family.

This does not exclude all anticommuting or general noncommuting ports,
and does not prove that the ten equations force commutation. K2191 already
excludes commuting ports; its result is reused. The object is full real Cl77
S128 with W(3,1)+N(4,6), fixed simple contraction, normalized adapters and
supplied common reverse. SC-OP-04 ASSERTS four-field candidate grammar,
not these adapters. SC-GEO-55 ASSERTS rotated-LC displacement, not ordinary
torsion. Source/full16cell/full20/K-C, native2+1/chirality, ledger0.263,
canon, LT-SM8/LT-GR6b/AC-F1 and physical quotient remain unchanged. No GU
falsification, novelty or proof-assistant/external-expert claim.

## 1. Ordered reduction from the original equations

Use [K2171](k2171-mixed-port-euler-filter-2026-10-27.md) and
[K2169](k2169-invertible-pencil-full-descent-2026-10-27.md).
Represent the tangent volume Omega by i in the faithful complex normal
Clifford module of dimension32; real-Cl77 calculations retain Omega itself.
Write t=Omega u, v normal grade7, u normal grade3, h=vt,

    V=v², T=t², a=tau(V), c=tau(T), D=49V+225T=P²,
    P=7v-15t, S=7v+9t, W=P^-1 S.

Anticommutation makes V,T,D commute with both ports. K2169 requires P
invertible, hence D invertible, but no individual-port inverse is assumed.
V,T have normal grades0+4. Product h is reversion-odd, hence normal grades6+10
with the common tangent Omega factor. Let J=h10. For the normal Clifford
contraction K, K(V)=2V+8a, K(T)=2T+8c and K(h)=-2h-8J.

K2171 gives 6 bar(P)Q=A W-B, Q=sum q_j gamma_j, retaining all ten actual
residuals and no extra eta_j in Q. Its ordered expansions are

    A=A0-168h, A0=60V-252T+24a+216c,
    B=B0+264h+144K(h), B0=780V+324T+312a-648c,
    W=(49V-135T+168h)D^-1.

The sign before144K(h) is POSITIVE: bR=(v-3t)(v+3t)=V-9T+6h.
Right multiplication by D, and h²=-VT, give the exact identity

    6 bar(P) Q D=-144[E+Lh-8JD],                 (1)
    E=245V²+1275VT+270T²+(98a-294c)V+(510a-810c)T,
    L=-21V+99T-28a-252c.                         (2)

The E term has tangent degree0; Lh and JD have tangent volume degree4.
These subspaces are independent in the real Clifford algebra. Therefore
all ten zero residuals necessarily imply

    E=0, Lh=8JD.                                (3)

These are contraction filters, never sufficient descent conditions.
Setting V=a,T=c recovers K2171's scalar filter
343a²+1491ac-540c² and its normal-grade6/10 coefficients, independently
checking the ordered signs. Two provisional derivation errors (an omitted
cross term and the wrong sign of K(h)) were caught before acceptance by
independent expansion and comparison with the original operator. They are
not alternative formulas.

## 2. No proportional squares, including nonscalar ones

Assume T=kV, k real. Invertible D implies V invertible and49+225k!=0.
Taking traces gives c=ka. Dividing E=0 by V gives

    A(k)V+B(k)a=0,
    A(k)=245+1275k+270k²,
    B(k)=98+216k-810k².                          (4)

If A(k)!=0, V and T are scalar. The all-scalar class is already excluded
by K2177 (and the anticommuting part by K2171). This includes scalar zero
without falsely inferring a zero port from a zero square.

If A(k)=0, then B(k)!=0: their exact polynomial gcd is1. Equivalently a
common root would be k=-833/4041, at which (A/5)*4041²=-20744640.
Thus a=c=0. Since A(0)!=0 and V is invertible, h²=-kV² is invertible.
Equation(3) reduces to

    (-21+99k)h=8(49+225k)J.                     (5)

If h has nonzero normal-grade6 component, its coefficient forces k=7/33;
(5) then forces J=0 since D is invertible. If that component is zero,
h=J!=0 and k=-59/243. Neither solves A=0:

    (A(7/33)/5)*33²=114912,
    (A(-59/243)/5)*243²=-574560.

This exhausts proportional squares with arbitrary Jordan structure.

## 3. Neither square may be nilpotent

The commuting matrices V,T are simultaneously triangularizable over C;
this is used for diagonal eigenvalues and trace only, not diagonalizability.
If T is nilpotent, c=0 and D invertible forces every V diagonal value r!=0.
E then gives r(245r+98a)=0, so every r=-2a/5. Normalized trace gives
a=-2a/5, hence a=r=0, a contradiction. If V is nilpotent, a=0 and
every T diagonal value s!=0; E gives270s(s-3c)=0. Trace gives c=3c,
again a contradiction. These exclusions include nonzero nilpotent squares.

## 4. No scalar-square branch when J=0

If V=aI, a!=0, the square T may still have Jordan blocks. From Lh=0,
multiplication by h and h²=-aT give LT=0. Thus every eigenvalue of T
is either0 or s0=(49a+252c)/99. The previous section excludes a fully
nilpotent T, so the nonzero spectral fraction p is positive.
If both0 and s0 occur, E at a zero eigenvalue gives c/a=7/6. Taking
normalized trace c=p s0 then gives p=33/98. But in the faithful
32-dimensional normal Clifford module p=m/32 for an integer m, impossible.
If all eigenvalues equal s0, c=s0 and c/a=-49/153. E on the diagonal
becomes the scalar polynomial343a²+1491ac-540c², nonzero at that ratio.
This argument preserves arbitrary Jordan blocks.

If T=cI, c!=0, the possible V eigenvalues are0 and
r0=-(28a+153c)/21. Both types would give a/c=18/17 from E at r=0,
but trace a=p r0 gives a/c=-153p/(21+28p)<0, a contradiction.
If all eigenvalues equal r0, a/c=-153/49, again contradicting the scalar
polynomial. Scalar-zero cases were already excluded as nilpotent.
No J!=0 scalar-square conclusion is inferred from this section.

## 5. A genuine nonscalar fixture and remaining reduction

Let n1,...,n10 be normal orthogonal generators, the first four positive.
Set w=u=n123+n145, v=I_N w and t=Omega u. Direct Clifford products give

    {v,t}=0, [v,t]!=0,
    V=2n2345, T=-V, V²=-4I,
    D=-176V, P^-1=PV/704,
    J=0, E=3040I, Lh=480 Omega I_N.

Thus both squares are nonscalar and the pencil is invertible; the fixture
is not covered by a commuting or scalar-square-only rejection. It fails
the necessary Euler contraction and the original lower residuals. The probe
computes the latter, not merely the derived equations.

For further anticommuting work write v=I_N w. Then [w,u]=0 and
H=wu has normal grades0+4. Put e=tau(H); h=Omega I_N H,
J=Omega I_N e, H²=-VT. Equation(3) becomes

    L H=8eD.                                   (6)

If e!=0, H,L and consequently V,T are invertible. If e=0, LH=0
allows singular sectors; no individual inverse is licensed. The remaining
family requires nonproportional, nonnilpotent squares and the actual all-ten
row reconstruction after these necessary tests. Passing(2),(6) is not a
solution, an existence theorem or an exclusion of that family.

## Verification and continuation

The probe compares(1) with all ten original residuals on sparse real
Clifford fixtures, checks direct A/B expansions and scalar specialization,
proportional exceptional values, trace multiplicity and scalar-stratum
contradictions. Actual product/contraction/sign faults must fail after a
green baseline. The universal arguments are the written algebra and trace
proofs; finite fixture controls are not exhaustive searches over forms.

Compare the genuinely nonproportional anticommuting/general noncommuting
construction with an explicit source-native degree-dependent common R0/R1
reality-density map on the same16 cells and lower return. Mobile geometry,
changed adapters and changed reverse are separate models. No further
commuting, proportional-square or nilpotent-square search is warranted in
this frozen family.
