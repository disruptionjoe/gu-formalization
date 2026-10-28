---
title: "K2185 Scalar-grade-square obstructions and rank-four affine localization"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed normalized Clifford adapter equations, no source or physical quotient verdict
scripts:
  - tests/channel-swings/k2185_clifford_spectral_obstruction_probe.py
---

# K2185 Scalar-grade-square obstructions and rank-four affine localization

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
result: K2185 scalar-grade-square exclusion and rank-four localization
carrier: full real Cl77 S128 vector-spinor plus scalar, W(3,1) and N(4,6) fixed LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: algebraic field-equation evaluation; no physical Hilbert pairing ON=declared_carrier
real_structure: real Clifford representation and independently supplied common reverse row
grading: full Dirac; tangent and normal exterior degrees are bookkeeping
action_owner: repository-construction: simple-contraction coupled operator and its fixed four-dimensional target
target: complete normalized zero-order principal and coefficient intertwiners MAP-TYPE=intertwiner
```

## Result and scope

Every affine-square commuting port satisfying the fixed normalized adapter
conditions must have a rank-four bivector B=(wu)_2, where v=I_N w,
t=Omega_W u and w,u are real normal trivectors. Neither product component
h4 nor h8 may have scalar square. This excludes the entire rank-two and
rank-six strata, not just one coefficient ansatz. Rank zero and rank at least
eight are also impossible. The remaining rank-four class is not constructed
or excluded here, and nonaffine and noncommuting classes remain separate.

These statements bind the same full real Cl77 S128, W(3,1)+N(4,6), supplied
common reverse, simple contraction and normalized adapters as
[K2183](k2183-commuting-trace-descent-2026-10-28.md). SC-OP-04 ASSERTS candidate
four-field grammar, not these adapters. SC-GEO-55 ASSERTS displacement from
gauge-rotated Levi-Civita, not ordinary torsion. Source/full16cell/full20/K-C,
native2+1/chirality, physical quotient, ledger0.263, LT-SM8/LT-GR6b/AC-F1 and
canon do not move. This is conditional internal mathematics, not GU
falsification, a physical existence result or a novelty claim.

## Scalar-square product components are impossible in the affine class

Reuse the necessary conditions of K2179--K2183:

    V=v^2, T=t^2, a=<V>0, c=<T>0, h=vt=h4+h8, U=2h4-6h8,
    F=10V+16T+4a-12c, G=142V+36T+68a-108c,
    [U,v]=[U,t]=0, FG=21U^2, FV+3Uh=0, h^2=VT.

In particular h and U commute. Direct expansion gives

    H4 = FG-84FV+756VT = 1344 h4^2,
    H8 = FG+28FV+84VT  = 1344 h8^2.                 (1)

No individual port is inverted. The only invertibility hypothesis is the
already required pencil P=7v-15t. The coefficients in (1) come from
21(U+6h)^2 and 21(2h-U)^2, respectively.

For an affine pair put V=a+X,T=c+zX,tau(X)=0. K2183 already excludes a=0,
X=0, the proportional class and the repeated-root case. Normalize ratios
r=c/a and X/a, without assuming the sign of a can be rescaled away. Write

    A=35-157z-54z^2, L=285+483z+144z^2,
    C0=49-301r+108r^2, C1=637-133r-72r^2,
    D=84-199r+z(-259+54r), E=A C1-L C0.

Then A is nonzero, X obeys A X^2+D X+C0=0, and E=0.
For an allowed even multiplicity m in {2,4,6,8,10,12,14,16}, define

    R_m(z)=Res_r(E,(32-2m)^2 A C0+m(32-m)D^2).     (2)

These are the previously derived nonzero necessary spectral polynomials.
The faithful full normal32 trace is essential; no positive trace assumption
or restriction to one volume sector is used.

If H4 is scalar, substitute V=1+X,T=r+zX in its polynomial expansion and
reduce X^2 using the quadratic. Since 1,X are independent, its X coefficient
must vanish. Clearing A yields

    J4/8=(2916z^3+18504z^2+37260z+15600)r
            -3465z^3-18151z^2-29015z+2975.

For scalar H8 the same calculation gives

    J8/8=(2916z^3+12456z^2+61956z+42480)r
            -11025z^3-22015z^2-52367z+2975.

The exact elimination polynomials are

    Res_r(E,J4)=37632(z-5)(9z+25)(54z^2+69z-85)
       *(62937z^4+447264z^3+1025270z^2+586000z-325375),
    Res_r(E,J8)=-338688(3z+13)(11z+5)(54z^2+69z-85)
       *(15471z^4-182466z^3-994996z^2-1096718z+153365).

For each of the eight m values, the gcd of each displayed resultant with
R_m over Q[z] is 1. The executable proof computes all sixteen gcds and
checks their exact Bezout identities. Therefore there is no common complex
slope, hence no real affine pair with either scalar h4^2 or scalar h8^2.
A resultant can add candidate roots but cannot remove a genuine common
root; the contradiction is therefore valid without solving for r or dividing
by a coefficient of J4/J8. This is a finite exact algebraic proof supplementing
(1) and the inherited universal trace argument.

## Grade support restricts the bivector rank

Let I_N be the normal volume, I_N^2=-1. It anticommutes with odd normal
elements. Write v=I_N w with w a normal trivector, and t=Omega_W u with
Omega_W^2=-1. Since Omega_W commutes with normal elements,
[v,t]=0 is exactly {w,u}=0. The latter removes grades0 and4 from wu, so

    wu=B+C, B=(wu)_2, C=(wu)_6,
    h=Omega_W I_N(B+C), U=Omega_W I_N(2C-6B).

Signs here use the fixed orientation of K2183. Centrality of U with v,t
implies {2C-6B,w}={2C-6B,u}=0. Also {wu,w}={wu,u}=0, directly from
{w,u}=0. Subtracting gives {B,w}={B,u}=0. In the Clifford product of a
bivector and trivector the anticommutator retains only grades1 and5.
Consequently

    B wedge w = B wedge u = 0,                       (3)

and the grade-one double-contraction terms vanish separately. They cannot
cancel the grade-five terms.

Rank means the rank of the alternating map N* -> N associated with the
bivector, not the signature rank of the induced metric. Let rank B=2r and
choose a linear decomposition N=E direct-sum K with dim E=2r and a Darboux
basis in which B=sum e_i wedge f_i. This uses no metric on E. On degree k
exterior forms over E, L=B wedge and its adjoint contraction Lambda for an
auxiliary positive Euclidean basis satisfy

    Lambda L-L Lambda=(r-k) identity.

If k<r and L alpha=0, taking the auxiliary norm gives
0=||Lambda alpha||^2+(r-k)||alpha||^2, so alpha=0. This auxiliary norm is
only a proof of a finite exterior-algebra identity; it is not a physical
positive pairing on the Clifford module.

Decompose w by its K-degree j. For rank at least eight, each E-degree
3-j is below r, so (3) forces w=u=0. This contradicts invertible P.
For rank six, only j=0 survives: w,u belong to Lambda^3 E. Thus C=w wedge u
is a multiple of the top blade of E. It is decomposable or zero. The ambient
nondegenerate Hodge dual maps a decomposable six-blade to a decomposable
four-blade even when E is metric-degenerate. Hence h4=Omega_W I_N C has
scalar square. This is excluded by the preceding theorem.

For rank two, B is decomposable, so its Hodge dual h8 has scalar square;
this is excluded by the other half of the theorem. Rank zero has h8=0 and
is covered as well. Every surviving affine pair therefore has rank B=4.
The same support argument rank B<=6 applies to all commuting candidates;
the scalar-component exclusions additionally require affine squares.

## Released rank-four reconstruction target

When dim E=4, (3) gives the precise necessary support

    w,u in Lambda^3 E plus (ker[L:Lambda^2 E -> Lambda^4 E] tensor K).

Here dim K=6 and the primitive two-form kernel has dimension5. Thus each
trivector lies in a 34-dimensional space, versus the unrestricted120.
Their top product C lies in Lambda^4 E tensor Lambda^2 K. This is a
support reduction, not a reconstruction: the grade-one contraction equations,
{w,u}=0, B=(wu)_2, the Clifford metric, the affine spectral filters,
centrality, P invertibility and all ten original equations remain necessary.
A general two-form in K need not be decomposable, so this statement does
not silently reintroduce the scalar h4-square hypothesis just excluded.
No positive-signature choice for E or K is assumed.

## Verification and continuation

The probe independently expands (1), both scalar coefficient filters and
resultants, all sixteen Bezout identities, and the wedge-map dimensions. It
also reuses actual real Clifford fixtures to check dual-grade/centrality
transfer and their original ten-row failures. Faults alter algebraic
coefficients, dimensions, grade weights or contractions after a green baseline.
Universal support proofs and finite exact polynomial certificates are
separate evidence kinds. Independent internal review inspects the degenerate
metric case and the absence of individual inverses. This is not Lean or
external-expert certification.

Next compare the rank-four affine reconstruction with a genuinely different
common-bar/mobile source construction and general nonaffine/noncommuting
ports. A candidate must use the actual real metric and pass all original
rows. An arbitrary matrix spectral solution is still not a Clifford solution.
