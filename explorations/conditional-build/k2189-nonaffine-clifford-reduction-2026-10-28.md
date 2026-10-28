---
title: "K2189 Nilpotent exclusion and six-plane reduction for commuting Clifford ports"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed normalized Clifford adapter equations, no source or physical quotient verdict
scripts:
  - tests/channel-swings/k2189_nonaffine_clifford_reduction_probe.py
---

# K2189 Nilpotent exclusion and six-plane reduction

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
result: K2189 nilpotent exclusion and nonaffine six-plane reduction
carrier: full real Cl77 S128 vector-spinor plus scalar, W(3,1) and N(4,6) fixed LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: algebraic field-equation evaluation; no physical Hilbert pairing ON=declared_carrier
real_structure: real Clifford representation and independently supplied common reverse row
grading: full Dirac; tangent and normal exterior degrees are bookkeeping
action_owner: repository-construction: simple-contraction coupled operator and its fixed four-dimensional target
target: complete normalized zero-order principal and coefficient intertwiners MAP-TYPE=intertwiner
```

## Result and scope

Neither product component h4 nor h8 can be nilpotent in ANY commuting
solution of the fixed normalized adapter equations. No affine-square premise
is needed. For rank-four metric-nondegenerate bivector support, actual
Clifford multiplication further forces the six-form product C to be a
nonzero nondegenerate decomposable blade. Both trivectors then live on one
nondegenerate six-plane. The rank-six support stratum has the same six-plane
property. Each of the two h4 spectral sectors separately reproduces the
scalar square traces a,c, a stronger constraint than their global average.

These are necessary reductions, not an exclusion or construction of all
nonaffine commuting ports. In particular scalar NONZERO h4 squared is not
excluded here: the scalar-square theorem of K2185 requires affine squares.
K2187 already excludes every affine-dependent pair and is not rerun.
Rank-two and degenerate rank-four survivors require separate treatment;
noncommuting ports do not inherit this commutative proof.

The model is unchanged: full real Cl77 S128, W(3,1)+N(4,6), simple
contraction, supplied common reverse and normalized adapters. SC-OP-04
ASSERTS candidate four-field grammar, not these adapters; SC-GEO-55 ASSERTS
displacement from gauge-rotated Levi-Civita, not ordinary torsion.
No source/full16cell/full20/K-C, physical quotient, native2+1/chirality,
LT-SM8/LT-GR6b/AC-F1, ledger0.263 or canon verdict changes. This is
conditional internal mathematics with no novelty or physical claim.

## 1. Nilpotent components cannot evade diagonal trace closure

Reuse [K2179](k2179-commuting-nonscalar-descent-2026-10-28.md):

    V=v^2, T=t^2, a=tau(V), c=tau(T), h=vt=h4+h8,
    U=2h4-6h8, F=10V+16T+4a-12c, G=142V+36T+68a-108c,
    Fv+3Ut=0, Gt+7Uv=0, P=7v-15t invertible.

Reversion already proves [U,v]=[U,t]=0; hence all of v,t,U,h4,h8 commute.
After the real tangent split, use the faithful complex normal32
representation, whose normalized trace tau is scalar extraction. A finite
commuting family has a common upper-triangular flag: a common eigenvector
exists by restriction to successive invariant eigenspaces, then induction
applies on the quotient. This does not assume diagonalizability.

If h4 is nilpotent, its diagonal vanishes, so U=8h4-6h has diagonal -6h.
If h8 is nilpotent, U=2h-8h8 has diagonal 2h. At each diagonal position
write lambda,mu for v,t, and r=lambda^2,s=mu^2. The exact same scalar
systems as K2179 follow, with k=-6 or2 respectively:

    [10r+(16+3k)s+4a-12c]lambda=0,
    [(142+7k)r+36s+68a-108c]mu=0.

Invertibility of P excludes lambda=mu=0. The pure-v, pure-t and mixed
square pairs are therefore the K2179 table. If m,n are their first two
integer multiplicities and 32-m-n is the third, trace consistency has
2x2 determinant

    k=2:  (32mn+329m-2935n+32480)/30720,
    k=-6: (mn-30m-132n+2304)/960.

Neither numerator vanishes for integers m,n>=0,m+n<=32. For k=2,
reduction modulo32 forces m+n=0 or32; the latter leaves a quadratic with
nonsquare discriminant4*2569. For k=-6, a zero requires
(132-m)(30-n)=23*72; no divisor of1656 lies in[100,132]. These arithmetic
arguments are inherited; the new transfer is that only DIAGONAL vanishing
of the component was necessary. It forces a=c=0, then every diagonal
lambda=mu=0, contrary to P invertible. A nonzero nilpotent component does
not evade this argument. Neither individual port was inverted and no
positive spectrum was used.

## 2. Immediate rank and null-support consequences

Write v=I_N w, t=Omega_W u for normal trivectors w,u. Then {w,u}=0,
wu=B+C, B=(wu)_2 and C=w wedge u. Put J=Omega_W I_N, J^2=1, so
h8=JB, h4=JC. J commutes with even normal elements. Centrality gives
{B,w}={B,u}=0 and B wedge w=B wedge u=0. The exterior support theorem
of K2185 bounds rank B by6.

- Rank0 is excluded since h8=0.
- Rank2 has decomposable B, hence scalar B^2. If it vanishes, h8 is
  nilpotent, so every surviving rank2 support is metric-nondegenerate.
- Rank6 confines w,u to Lambda^3 E for E=supp B. Thus C is a top six-blade.
  It must be nonzero and C^2 nonzero by section1, which makes E
  metric-nondegenerate.
- Rank4 has B^2=b+D, D=B wedge B a nonzero top four-blade. If E is
  degenerate then D^2=0. When b=0, h8^4=B^4=0, again excluded. The
  degenerate rank4 stratum with b!=0 remains open.

A null-support countercontrol in the probe has nonzero B,D with
B^2=D and D^2=0. It exists as exterior/Clifford data and is rejected as a
solution by the theorem; it is not falsely identified with zero.

## 3. Rank-four nondegenerate support forces a simple complement

Let E=supp B be nondegenerate of dimension4, K=E-perp, D=B wedge B,
D^2=d!=0. K2187's support and centrality arguments, which did not require
affine squares, give

    w,u in Lambda^2 E tensor K, C=D H, H in Lambda^2 K.

Indeed [B^2,w]=[D,w]=0 removes the Lambda^3 E term because D is
invertible and anticommutes with it. The same applies to u.

Complexify the nondegenerate E Clifford algebra. Its even algebra is
Mat2(C) plus Mat2(C): the usual two commuting Pauli-matrix triples give
a faithful four-dimensional module for this eight-dimensional algebra. D acts as plus/minus
δ times identity, δ^2=d, and E-bivectors have trace zero in each block.
B^2=b+D therefore acts as b+δ or b-δ. At least one is nonzero.
In that block diagonalize B as diag(β,-β), β!=0. Its two eigenvalues
are distinct. The relations {B,w}={B,u}=0 then give

    w=[[0,A],[A',0]], u=[[0,L],[L',0]],

where the entries are complex K-vectors, since the original coefficients
were E-bivectors times K-vectors. Even E elements commute with K, so this
matrix multiplication is the ordinary one with Clifford-valued entries.
The first diagonal entry of wu=B+D H is

    A L'=β+δ H.

Its K-grade2 part is δH=A wedge L'. Thus H wedge H=0. The Pluecker
criterion for a bivector says it is decomposable or zero: an alternating
matrix with all four-index Pfaffians zero has rank at most2. Since H is
real, its real Pluecker equations vanish too. Hence H^2 is scalar and
C^2=d H^2 is scalar. Section1 makes it NONZERO, so H is a nonzero
nondegenerate simple bivector. This proof includes the exceptional case
where the other chiral block of B has square zero.

## 4. Released common six-plane reduction

Let F=supp H be its nondegenerate two-plane. Split K=F orthogonal-direct-sum
K'. Then C=D H is a nonzero top blade of L=E orthogonal-direct-sum F,
a nondegenerate six-plane. Centrality also gives {C,w}={C,u}=0.
Within w in Lambda^2E tensor K, the Lambda^2E tensor F terms
anticommute with C, while the Lambda^2E tensor K' terms commute with C.
The latter anticommutator is twice their product with the invertible C,
so they vanish. Therefore

    w,u in Lambda^2E tensor F, dim(L)=6.

Together with rank6 in section2, both these strata reduce to actual
trivectors on a nondegenerate six-plane. The rank4 subspace has dimension
6*2=12 for each trivector before its two B-contraction constraints, rather
than arbitrary normal trivectors. This is an exact reduction inside the
original ten-dimensional normal space, not permission to replace the
ambient source carrier or drop its spectator Clifford multiplicity.

## 5. Independent sector trace constraints

For rank4, w^2,u^2 have grades in
R plus Lambda^4E plus (Lambda^2E tensor Lambda^2K). For rank6 they
lie in R plus Lambda^4L. In both cases h4=J C is, after fixing
Omega_W=i, a pure four-blade on the orthogonal complement of the
six-plane. Grade orthogonality gives

    tau(h4)=tau(h4 V)=tau(h4 T)=tau(h4 h8)=0.

Since h4^2=q^2!=0, choose either complex square root q and set
e_plus/minus=(1 plus/minus h4/q)/2. Both have faithful32 rank16.
The sector normalized traces tau_plus/minus(Z)=2tau(e_plus/minus Z)
therefore satisfy

    tau_plus/minus(V)=a, tau_plus/minus(T)=c,
    tau_plus/minus(h8)=0, tau_plus/minus(h)=plus/minus q.

There is no positivity inference when q is imaginary. These are necessary
constraints on the same a,c, not independently refitted sectors.
The existing genuine K2187 nonaffine fixture satisfies these geometric
conditions, has invertible pencil and nevertheless fails all ten original
rows. The probe rechecks it against those original equations to expose the
remaining algebraic gap. Scalar nonzero h4 squared is compatible with this
structural fixture; K2185's affine-only exclusion cannot be reused here.

## 6. Released faithful four-dimensional square algebra

On either proved six-plane L, V=w^2 and T=-u^2 lie in Cl(L)^even and
are independent of the orthogonal four-plane volume J_R=I_(L-perp).
The ambient faithful normal32 representation restricts to four copies of
the faithful complex Cl(L) representation of dimension8. In that8-space,
fix either J_R eigenvalue. P=7J_R I_L w-15i u is odd with respect to
L-volume, invertible, and commutes with V,T. Its two off-diagonal4x4
blocks are invertible and simultaneously intertwine the two chiral blocks
of V and T. Consequently the full32 square-algebra representation is eight
copies of the same4-dimensional representation, and

    tau32(f(V,T))=tr4(f(V_plus,T_plus))/4

for every polynomial f. This is a derived trace reduction, retaining the
ambient definitions of a,c. Every joint generalized square multiplicity is
therefore divisible by8, and there are at most4 distinct joint eigenvalue
pairs. Jordan radicals can remain: neither algebra dimension at most4 nor
at least3 distinct joint eigenvalues follows from nonaffine squares.
Individual odd ports and the real conjugation cannot be restricted to
one chiral4-space; they exchange blocks. The original equations need both.

## 7. Exact six-plus-one original-row consumer

Dimension reduction must not erase the four orthogonal normal rows. Even
though w,u lie on L, v=I_N w has four orthogonal volume legs, so their
derivatives do not vanish. The following consumer keeps all ten rows while
using the smaller algebra. Choose an oriented orthonormal splitting N=L+R,
dim L=6, dim R=4, I_N=J_R I_L. Work in Cl(L)_C[J_R] with
J_R^2=epsilon_R, retaining BOTH eigenvalues of J_R. The tangent volume is
represented by i only after the original real tangent split. Define

    v=J_R I_L w, t=i u, z=v+t, R0=v+3t, P=7v-15t,
    C_a=-eta_a P^(-1) d_a R0, a in L,
    A0=-P^(-1)v,
    S_L=sum_(b in L) bar(C_b)d_b bar(R0),
    S=S_L+4bar(A0)v.

Here d_a is the same right Clifford contraction as the original port map,
and bar is the inherited real tangent conjugation (i changes sign).
For r in R the original adapter is C_r=eta_r A0 gamma_r. The six original
L rows are exactly

    q_a=4t C_a-eta_a d_a z+7bar(C_a)z+2S C_a
        +eta_a sum_(b in L) bar(C_b)[d_b z,gamma_a]
        +8eta_a bar(A0)d_a v.

The four other original rows are q_r=eta_r Q_R gamma_r, with

    Q_R=4t A0-v+7bar(A0)bar(z)+2S A0
        +2sum_(b in L) bar(C_b)d_b v+6bar(A0)v.

Thus all ten rows vanish if and only if these six q_a and Q_R vanish,
with P invertible. This formula even applies to arbitrary six-plane
trivectors before imposing commutation or the centrality filters.
To derive it, move an R generator through each coefficient by

    gamma_r X=theta(X)gamma_r,

where theta flips J_R and every L-odd element. In particular theta(z)=bar(z)
and theta(d_a z)=-d_a bar(z). Substitute C_r into K2169's full row formula.
The four R terms in S each equal bar(A0)v. For q_a their commutator
contribution totals8eta_a bar(A0)d_a v. For q_r its three distinct R
indices supply6bar(A0)v; its self commutator is zero. The L commutators
supply twice the displayed L sum. This derivation preserves multiplication
order; it does not commute arbitrary adapters.

Exact controls independently reconstruct all ten original rows for a
genuine central nonaffine fixture and an arbitrary noncentral six-plane
fixture. They check this consumer in mixed signatures and both tangent
conjugation terms; planted omission of an orthogonal-row contribution
fails. The structural central fixture still has ten nonzero rows. A
future six-plane search can use seven smaller-algebra equations without
mistaking six retained equations alone for full descent.

## Verification and continuation

The universal arguments above are distinct from finite exact controls.
The probe checks the diagonal transfer, inherited integer trace census,
nonzero nilpotent geometry, chiral block and six-plane grade identities,
sector traces and original-row rejection. Faults alter actual weights,
trace dimension, Gram sign or blade product; baseline must pass first.
Independent internal review challenges the proof transfer and real/null
cases. No proof-assistant, external-expert or remote-CI certification.

Next solve the reduced nonaffine scalar-nonzero product-square equations
on their actual six-plane, retaining full32 multiplicities, centrality,
invertible pencil and all ten original rows. Rank2 and degenerate rank4
with b!=0 remain separate, as do noncommuting and common-bar/mobile native
constructions. This removes unnecessary ten-dimensional coefficient search
for the proved strata; it does not exhaust the full commuting problem.
