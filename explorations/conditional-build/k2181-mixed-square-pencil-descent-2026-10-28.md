---
title: "K2181 Proportional-square exclusion and affine square pencils"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed normalized Clifford adapter equations, no source or physical quotient verdict
scripts:
  - tests/channel-swings/k2181_mixed_square_pencil_descent_probe.py
---

# K2181 Proportional-square exclusion and affine square pencils

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
result: K2181 proportional-square exclusion and affine spectral necessary conditions
carrier: full real Cl77 S128 vector-spinor plus scalar, W(3,1) and N(4,6) fixed LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: algebraic field-equation evaluation; no physical Hilbert pairing ON=declared_carrier
real_structure: real Clifford representation and independently supplied common reverse row
grading: full Dirac; tangent and normal exterior degrees are bookkeeping
action_owner: repository-construction: simple-contraction coupled operator and its fixed four-dimensional target
target: complete normalized zero-order principal and coefficient intertwiners MAP-TYPE=intertwiner
```

## Result and scope

No real commuting fixed-adapter normal7/normal3 port with proportional squares
T=zV satisfies the complete normalized descent equations. This includes mixed
product grades and the exceptional slopes at which the usual square polynomial
loses degree. It does not assume individual port invertibility.

The released affine-square case T=c+z(V-a) has a nondegenerate quadratic
constraint, at most two square eigenvalues and a finite integer-multiplicity
filter. These are necessary conditions, not an existence theorem or an
exclusion of every affine pair. An actual mixed, central, nonproportional
affine Clifford fixture passes the structural hypotheses and is rejected by
the full original equations. The distinction is material: centrality alone
does not exclude the remaining mixed class.

The carrier is the same full real Cl77 S128 and fixed W(3,1)+N(4,6) with
supplied common reverse, simple contraction and normalized zero-order adapters.
SC-OP-04 ASSERTS candidate four-field grammar, not these fixed adapters;
SC-GEO-55 ASSERTS displacement from gauge-rotated Levi-Civita, not ordinary
torsion. Source/full16cell/full20/K-C, native2+1/chirality, physical quotient,
ledger0.263, LT-SM8/LT-GR6b/AC-F1 and canon remain unchanged. This is
conditional internal mathematics, not GU falsification or a novelty claim.

## Reused necessary system

Use [K2179](k2179-commuting-nonscalar-descent-2026-10-28.md) and
[K2177](k2177-exceptional-spectrum-descent-2026-10-28.md).
For commuting ports v,t=Omega_W u, write

    V=v², T=t², a=<V>0, c=<T>0, h=vt, U=K(h)=2h4-6h8,
    F=10V+16T+4a-12c, G=142V+36T+68a-108c.

Real tangent splitting precedes the faithful complex32 normal representation.
The original equations imply P=7v-15t invertible,

    Fv+3Ut=0, Gt+7Uv=0,
    [U,v]=[U,t]=0, FG=21U², FV+3Uh=0,
    Q=35V²-157VT-54T²+(14a-42c)V+(-102a+162c)T=0.     (1)

K2177 excludes all real scalar-square pairs. K2179 excludes every commuting
pair with homogeneous h4 or h8, including Jordan and singular cases. Neither
result excludes the general mixed nonscalar case. Trace is normalized full32
trace, never a selected16-dimensional normal-volume sector or a positive form.

## Proportional squares, including exceptional slopes

Suppose T=zV for real z, so c=za. Commuting matrices v,t have a common upper
triangularization. If a diagonal entry of V were zero, both corresponding
port eigenvalues would have square zero; P would have a zero diagonal entry.
Thus V is invertible. This is proved for this subclass, not assumed generally.
Substituting in Q and canceling V yields

    A(z)V+B(z)a I=0,
    A(z)=35-157z-54z², B(z)=14-144z+162z².             (2)

If A is nonzero, V and T are scalar and K2177 applies. If A=0, then B is
nonzero. In fact B+3A=119-615z, while A(119/615)=983136/378225 is nonzero;
the exact resultant Res_z(A,B)=-53089344 is an independent control.
Hence a=c=0. Also z is nonzero because A(0)=35. From h²=zV², h is invertible.
Equation FV+3Uh=0 now gives

    U=-(10+16z)/(3z) h.                               (3)

But K acts with distinct eigenvalues2,-6 on h4,h8. Equality U=k h forces
h homogeneous (or h=0, already impossible). K2179 then excludes this case.
All proportional-square slopes are therefore excluded, even the exceptional
ones and without an unjustified inverse of an individual port.

The result also covers V=0 with arbitrary scalar T through K2177; T=0 is
already in the proportional class. No noncommuting reduction is asserted.

## Affine-square successor

Let X=V-aI and T=cI+zX. This includes a common scalar part plus proportional
traceless square defects, which is strictly wider than proportional squares.
Expanding Q gives

    A X²+D X+C0 I=0,
    D=84a-199c+z(-259a+54c),
    C0=49a²-301ac+108c².                              (4)

The quadratic coefficient A cannot vanish for a surviving candidate. If X=0,
both squares are scalar and K2177 applies. If X is nonscalar and A=0, (4)
requires D=C0=0. If a=0 then C0=108c² implies c=0, making T=zV, already excluded.
If a is nonzero, put r=c/a. Eliminating r from D/a and C0/a² gives

    Res_r(84-199r+z(-259+54r),49-301r+108r²)
      =49(64854z²+227077z-47531).

Its resultant with A is -2212378216925184, so it cannot vanish with A.
Thus A=0 is excluded in every affine case, not only proportional squares.

For A nonzero the minimal polynomial of X divides (4). If the discriminant
D²-4AC0 is nonzero, X is diagonalizable over C with at most two eigenvalues.
If it is zero, trace(X)=0 forces its repeated eigenvalue to be zero, so
D=C0=0 and X²=0; a nonzero nilpotent square defect is NOT excluded by this
argument. Jordan blocks then have size at most2.

In the distinct-root case let m be the algebraic multiplicity of the first
root and32-m that of the second. Trace(X)=0 gives the further exact necessary
condition

    (32-2m)² A C0 + m(32-m)D²=0,   m in{0,...,32}.     (5)

It follows by eliminating the two roots using their sum -D/A and product C0/A.
At m=16 it requires D=0; at m=0 or32 it requires C0=0. A nonscalar X with
only one distinct root cannot occur here, but retaining these endpoint
multiplicities makes the necessary filter safe. Equation(5) is NOT sufficient:
real Clifford grade support, centrality, invertible P and all ten original
rows still apply. No positivity of the eigenvalues is assumed.

## Actual mixed affine countercontrol

Take normal generators n1,...,n10 with the first four positive, and I_N their
ordered volume. Define

    w=n123+n145, v=I_N w, u=2n236+3n456, t=Omega_W u.

Exact Clifford multiplication yields [v,t]=0, a=0,c=5, and
T=5I+6V, with V nonzero nonscalar. Both h4 and h8 are nonzero and commute
with v,t. The pencil P is invertible. Thus a genuinely nonproportional affine
mixed pair passes centrality; it cannot be dismissed by the earlier
homogeneous or proportional theorem. Nevertheless its Q is nonzero and
independently evaluated original descent rows reject it.

The probe additionally checks the proportional pair w=n123+2n145 and
u=n236+2n456, v=I_N w. It has V=T=3I+4n2345, both product grades
nonzero, centrality and invertible P. The new theorem applies beyond the
earlier homogeneous-product exclusion; nine of the ten original rows fail
for each of the two fixtures. These fixture rejections supplement the universal proof, not replace it.
An abstract square-zero2x2 matrix control preserves the unresolved Jordan
possibility of (4): a polynomial condition alone is not Clifford existence.

## Reproduction and claim ceiling

Run `tests/channel-swings/k2181_mixed_square_pencil_descent_probe.py` with
SymPy; `--write` regenerates the dependency-hashed report. Exact polynomial
elimination, all33 integer-multiplicity coefficient identities, actual real
Clifford fixtures, original ten-row transfer and genuine altered-equation
faults are checked after a green baseline. Independent internal review
reconstructs the proof and tests exceptional cases. No proof-assistant or
external-expert acceptance is claimed.

The remaining affine candidates must pass (4),(5) and actual Clifford/original
rows; general nonaffine or noncommuting nonscalar squares require different
reductions. A scalar spectral relaxation is not a solution. Moving geometry,
a changed reverse and native source/common-bar constructions remain distinct
questions. Do not requeue scalar squares, homogeneous commuting products or
proportional commuting squares.
