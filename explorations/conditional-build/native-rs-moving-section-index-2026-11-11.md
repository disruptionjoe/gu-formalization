---
title: Native RS moving-section and grading-dependent index transfer
status: exploration
doc_type: structural-result
created: '2026-11-11'
program_target: X-P2-P3
tier: T2
expected_delta: Test simultaneous observation, propagation, pairing and graded-index
  requirements on actual canonical structural symbols
actual_delta: 'Constrained: native projected symbol quotient and exact limits; no
  full-C or source verdict'
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# Native RS moving-section and grading-dependent index transfer

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Its result binds only the
> named model and does not adjudicate Weinstein's source-native mechanism
> without a typed bridge. Read `lab/methods/source-native-comparator-routing.md`
> and follow its source-native pointers. Classification: `INTERNAL_STRUCTURAL_ONLY`.

program_target: X-P2-P3
tier: T2
expected_delta: Actual simultaneous structural compatibility
actual_delta: Conditional native-symbol and domain constraints; no class decision

```gu-typed-objects
result: Native RS moving-section and grading-dependent index transfer
carrier: nondegenerate native4+10 split; separate closed positive spin4 comparison with rank10 normal spinors LAYER=UNTYPED CHIRALITY=S-FULL-DIRAC
pairing: metric-compatible native tensor form; positive elliptic comparison explicitly separate ON=declared_carrier
real_structure: actual quaternionic K95 where named; separate complex positive elliptic comparison
grading: ambient volume, coherent horizontal lift and observed weak grading are distinct
action_owner: repository-construction -- canonical projected symbol and stated arrow span; not selected source action
target: simultaneous actual observation and declared evolution or index transfer MAP-TYPE=intertwiner
```

## 1. Prior work and precise new seam

The Aug30 source-native observation-sector result proves ambient gamma kernel
observes outside the horizontal gamma kernel. Nov11 BET provenance classifies
minimum augmented observations. Neither tests the tangential **projected RS
principal symbol on R itself**; K2236's full scalar/vector raw evolution is a
different operator. Today's local-boundary-symbol result proves ambient raw RS
symbol homotopy and n+1 coefficient for ambient chirality. We reuse that proof
rather than pretend RS is Dirac type.

The new seam is the exact symbol short sequence

  0 -> normal gamma kernel -> ambient gamma kernel -> observed one-forms -> 0,

including the actual descended symbol and its grading-dependent index classes.
The literal map is never replaced by a projection onto horizontal RS states.

## 2. Exact symbol descent

Let V*=H*⊕N* be a nondegenerate orthogonal split, dim h,n, and let S be a
Clifford module, c(v)c(w)+c(w)c(v)=2g(v,w). Let Γ_Y:V*⊗S -> S be gamma trace,
j_Y=γ/m its metric-normalized right inverse and Π=I-j_Y Γ_Y. Set R=ker Γ_Y.
The literal observation q:R -> B=H*⊗S forgets normal one-form slots.
It is onto: b lifts to (b,-j_N Γ_H b). Its kernel K=ker Γ_N⊂N*⊗S.

For horizontal covector ξ let Cξ act by c(ξ) on each spinor slot. On R,

 Γ_Y Cξ v=2 ιξ v,
 Qξv=Π Cξv=Cξv-(2/m)γ ιξv.

For z∈K, its horizontal slots and ιξz vanish. Therefore Qξz=Cξz, and
Γ_N Cξz=-CξΓ_Nz=0. Thus K is symbol-invariant and qQξ=Bξq with

 Bξ b_a=c(ξ)b_a-(2/m)γ_a ιξb,     a horizontal.

This is an actual native principal-symbol quotient. It is stronger than mere
surjectivity of carrier observation but does not yet include lower-order
connection terms, moving-section derivatives, analytic domains or physical
state selection.

## 3. Complete non-null inverse and homotopy

For k=g^-1(ξ,ξ)≠0, Cξ^-1=Cξ/k. Write U=γ_H:S -> H*⊗S, V=ιξ. Then

 V Cξ^-1 U=I_S.

For α=2t/m define Bξ(t)=Cξ-αUV, 0≤t≤1. The exact inverse is

 Bξ(t)^-1=Cξ^-1 + [α/(1-α)] Cξ^-1 U V Cξ^-1.

The determinant lemma gives

 det Bξ(t)=(1-2t/m)^s det Cξ,   s=dim S,

on a full-Dirac module. For m>2 the whole path is invertible at every non-null
ξ. This proves a symbol homotopy to Cξ on the observed one-form bundle. On
half-spin maps use the same composition inverse between the appropriate
opposite chiralities rather than an untyped square determinant.

For native Lorentzian H, null ξ remain characteristic. The determinant
identity extends as a polynomial identity, so this does not prove ellipticity
or supply a Fredholm operator. In a separately declared positive elliptic
transfer, every ξ≠0 is non-null and the homotopy defines a K-symbol identity.
The factor is m=14 (1-t/7); replacing it by h=4 gives the WRONG descended
operator even though it happens to retain ellipticity in a positive control.

## 4. Ambient grading and its exact K-symbol sequence

Assume a global oriented spin split in the positive elliptic transfer category,
S=S_H ⊗ S_N. Let χ_H,χ_N denote the two even-dimensional complex chiralities;
ambient χ_Y=χ_Hχ_N (up to the fixed common orientation convention). On a
four-dimensional base let D_H be the chiral spin Dirac symbol and put
Δ_N=[S_N^+]-[S_N^-] in complex K^0(X).

The observed B symbol has ambient-graded class

 [B]_χY=[H_C][D_H]Δ_N.

The hidden normal gamma kernel has
 [R_N^+]-[R_N^-]=([N_C]+1)Δ_N,
because Γ_N maps N_C⊗S_N^± onto S_N^∓. Therefore

 [K]_χY=([N_C]+1)[D_H]Δ_N,
 [R]_χY=([H_C]+[N_C]+1)[D_H]Δ_N,
 [R]_χY=[K]_χY+[B]_χY.

The last identity can be proved directly from the invariant exact symbol
sequence: choose a bundle splitting, write its symbol triangularly, and scale
the off-diagonal block to zero. All diagonal blocks remain invertible on the
punctured positive cotangent bundle. It agrees with the independently owned
ambient RS n+1 symbol rule. No ghost subtraction has been inserted.

## 5. Horizontal chirality requires a nontrivial lift on R

Naive slotwise χ_H does NOT preserve R: it anticommutes with horizontal gamma
trace but commutes with normal gamma trace. For Γ_H b+Γ_Nv=0, generally
Γ_Y χ_H(b,v)=χ_H(-Γ_Hb+Γ_Nv)≠0.

Nevertheless χ_H grades the observed B symbol. To lift it coherently to R,
let r=+I on H* and -I on N*, and put

 G=r⊗χ_H.

Then Γ_Y G=-χ_H Γ_Y and G j_Y=-j_Y χ_H, so G commutes with Π, preserves R,
and anticommutes with Qξ. Literal q satisfies qG=χ_Hq, while on the hidden
kernel G restricts to **minus** χ_H. Consequently the coherent G-graded
classes are

 [B]_χH=[H_C][D_H][S_N],
 [K]_G=-([N_C]-1)[D_H][S_N],
 [R]_G=([H_C]-[N_C]+1)[D_H][S_N].

Here [S_N]=[S_N^+]+[S_N^-] and the ungraded normal exact sequence gives
[R_N]=([N_C]-1)[S_N]. The hidden minus sign is essential. Adding same-sign
horizontal indices of hidden and observed pieces would be an invalid grading
transfer. G is a constructed lift within this symbol category, NOT a selected
source physical grading or a proved symmetry of every lower-order term.
Its domain and connection preservation must still be checked.

Thus the same literal observed carrier and symbol support two mathematically
different grading conventions with different index classes. Calling both
'four-dimensional chirality' or identifying either with observed weak chirality
without the current/action/quotient map would erase the key source distinction.

## 6. Closed-four-manifold index consumers (explicitly conditional)

Assume X is CLOSED oriented spin four-dimensional, the positive elliptic
transfer is globally defined, and no boundary or noncompact end correction is
present. These assumptions are not native Lorentzian Y14 APS-end data. The
usual twisted Dirac index pairing is ∫_X Â(TX) ch(W). Reference for the standard
framework: Gilkey, The Atiyah-Singer Index Theorem, chapter5,
https://www.maths.ed.ac.uk/~v1ranick/papers/gilkey3.pdf . The following coefficients
are derived from spin weights, not quoted or inferred from dimensions alone.

For oriented rank10 spin N with formal roots x1,...,x5,

 ch(S_N^+)-ch(S_N^-)=product_j (exp(xj/2)-exp(-xj/2)).

Its lowest cohomological degree is10, exceeding dimX=4. Hence the integer
ambient-graded indices of observed, hidden and total symbols above are all0.
This does not assert their K classes vanish integrally, and does not settle
one-sided weak currents, which can occur with index0.

In the horizontal case use
 ch(S_N)=32+4 p1(N) through degree4,
 ch(H_C)=4+p1(TX),    Â(TX)=1-p1(TX)/24.
Thus

 ind(B)_χH=∫[(80/3)p1(TX)+16p1(N)].

For the metric-section normal bundle N≅Sym² T*X, the root calculation gives
p1(N)=6p1(TX). Indeed the nonzero complexified Sym² weights are ±2x1,±2x2,
±x1±x2, with two zero weights; one-half the sum of their squares is
6(x1²+x2²). Using ∫p1(TX)=3 signature(X),

 ind(B)_χH=368 signature(X).

The hidden **G-graded** index is -1188 signature(X), and total is
-820 signature(X), so exact additivity gives -820=-1188+368. These integers
are index-pairing results of the declared closed positive transfer, not
native family predictions. Arbitrary APS/end data can add corrections and the
native Lorentzian symbol is not elliptic; neither is silently removed. No
identification of P3 with either index has been supplied.

The difference from zero to these multiples comes from an actual grading
change with a nontrivial lift, NOT from multiplying a whole operator by a
nonzero scalar phase. P2 scalar phase on this fixed realization preserves both
chosen index classes. A purported P2-to-P3 change needs a genuinely different
grading/domain/end operation rather than renaming the sign.

## 7. Exact moving-section lower-order test

The exact symbol quotient survives pointwise on a nondegenerate split, but a
moving section creates lower-order off-diagonal leakage. For ambient LC/Clifford
connection and tangential projected operator Q, hidden z in ker Γ_N has

 (qQz)_a=sum_r[-sum_i γ^i II_ia^r+(2/m)γ_a H^r] z_r.

To vanish on all kerΓ_N, each horizontal coefficient family L_a^r must factor
as M_a γ_r. For at least two normal directions, L_a^r γ_r^-1 lies in distinct
bivector subspaces H∧span(n_r); their intersection is0. The grade2 Clifford
representation is injective in the present dimensions, including half-spin.
Thus II_ia^r=(2/m)g_ia H^r. Tracing gives(1-2h/m)H=0, so for h4,m14 the quotient
requires II=0. At m=2h the algebra permits umbilic II. No spin-connection term
within a normal vector slot leaks into a horizontal vector slot; the displayed
LC vector-connection contribution is the whole leakage in this category.

Independent non-LC fields or zero-order coupled blocks may cancel it. Their
possibility is not excluded by the LC test. Native SC-GEO-55 specifically keeps
displacement from gauge-rotated LC in play. The proper joint requirement is:
actual observation-compatible lower-order completion and grading/domain must
precede transferring the closed positive index calculation to a native count.

## Exact controls for root to serialize

1. Symbol identities in supplied Clifford fixture, h4/n10/m14: ΓQ=0,
qQ=Bq, K invariant; inverse residual zero at rational nonnull ξ.
2. Determinant/homotopy formula through rank-one block factorization, rather
than constructing large symbolic determinants.
3. A gamma-trace-free vector whose slotwise χ_H leaves R (e.g. horizontal
trace compensated by normal insertion), contrasted with G preserving R.
4. qG=χ_Hq and G|K=-χ_H exact.
5. Formal characteristic-class coefficient arithmetic using rational numbers,
with ambient super-spin character having no degree≤4 term.
6. Same-symbol/phase invariance retained, and a null horizontal covector giving
singular symbol: positive ellipticity must not be transported back to K95.
7. Root's moving-II test: pure trace at m14 still leaks, nonzero tracefreeII
leaks, II0 passes; criticalm=2h umbilic passes as a contrary universal control.

### Expanded spin-weight and index arithmetic

The 32 weights of the full complex Spin(10) module are all
w_ε=(ε1 x1+...+ε5 x5)/2, εj∈{±1}. Their sum is0. In
sum_ε exp(w_ε), the degree4 term is(1/2)sum_ε w_ε². Cross terms cancel by
independent sign reversal, and each xj² occurs32/4 times before multiplying
1/2. Thus ch(S_N)=32+4sum_j xj²=32+4p1(N).

For hidden ungraded R_N=(N_C−1)S_N, ch(N_C−1)=9+p1(N), so
Â ch(R_N) has degree4 68p1(N)−12p1(TX). The coherent total grading G puts a
minus sign on this hidden block; with p1(N)=6p1(TX) its index is
−(408−12)*3 signature(X)=−1188 signature(X).
Observed degree4 is (32−128/24)p1(TX)+16p1(N)
=(80/3+96)p1(TX)=(368/3)p1(TX), giving368 signature(X).
Total virtual twist H_C−N_C+1 has rank−5 and degree4 p1(TX)−p1(N), so
Â ch(H_C−N_C+1)ch(S_N) has degree4
(32+160/24)p1(TX)−52p1(N)
=(116/3−312)p1(TX)=−(820/3)p1(TX), giving−820 signature(X).

## Released structural repair: a split-preserving metric connection

Let V=s*TY carry its nondegenerate H⊕N metric split along the observation
section, with orthogonal projectors P=P_H and Q=P_N=I−P. Starting from the
ambient LC pullback connection ∇, define a connection along X by

 ∇ad_X u=P ∇_X(Pu)+Q ∇_X(Qu).

The derivative acts on Pu/Qu, including the moving projectors. This is a
covariant definition, not a framewise deletion without transformation law.
It preserves both subbundles and the same metric. With A=∇ad−∇,

 A_X=[P,∇_X P]=(2P−I)∇_X P.

Since P is metric-selfadjoint and ∇ is metric, ∇P is selfadjoint; its commutator
with P is metric-skew. In a split frame, A is precisely minus the off-diagonal
connection blocks. Thus this correction compensates the II leakage without
making the original embedded section totally geodesic.

Use the induced spin lift, characterized without index-sign ambiguity by
[Δ_X,c(v)]=c(A_Xv), where Δ_X is the change of spin connection, and use
∇ad on the one-form slot as well. The resulting tensor connection preserves
Γ_Y, the split, R, and K=kerΓ_N in normal slots. It also preserves the split
volume/chirality operators and the constructed G=r⊗χ_H. Therefore the actual
tangential projected first-order expression

 Qad=sum_i Π_R c(e^i) ∇ad_i

preserves hidden K and descends through literal observation along arbitrary
original II. Its difference from Q is zero-order IN THE FERMION variable;
its observed principal symbol is still Bξ. A global graded analytic domain
remains an additional requirement. The isolated Jordan defect in its frozen
principal time-evolution pencil is unchanged; this connection repair cannot
supply strong hyperbolicity to that unrestricted isolated system.

Curvature changes by R^ad=R+d_∇A+A∧A. Along the section, the horizontal block
of the original LC projection is the induced LC connection on X; do not call
its tangential torsion nonzero merely because the full connection differs.
An extension away from the section is extra data and may have ambient torsion.
In any case the source's SC-GEO-55 displacement from gauge-rotated LC is not
identified with ordinary torsion.

Claim limits: this is a structural connection comparison on s*TY along X,
not a source-selected connection, not a globally constructed Y14 end, and not
an inhabited class-C action/BV witness. Extending the connection, respecting
the actual source/gauge grammar, and maintaining the action's jet-order and
variational requirements need separate proofs. 'Zero order in the fermion'
does not mean zero derivative order in background/section fields. The result
shows that the LC-only observation obstruction is repairable in a larger
metric-connection category; it does not choose that repair physically.

## Released companion repair and its SAME index consumer

This is an independently recognizable structural symbol, not a newly guessed
action: the full vector-spinor Clifford symbol Cξ on A decomposed as
A=R⊕j_Y S. In coordinates (r,ψ), where Γ_Y(r+j_Yψ)=ψ, its blocks are

 Mξ = [[Qξ, (2/m) Uξ], [2 Vξ, ((2−m)/m)cξ]],
 Uξ=Π_R(ξ⊗I), Vξ=ιξ.

Indeed Π C j_Y=(2/m)Π ξ, Γ C|R=2ιξ, Γ C j_Y=((2−m)/m)cξ.
The exact identities

 Q²=kI−(4/m)UV, QU=βUc, VQ=βcV, VU=δkI,
 β=(m−2)/m, δ=(m−1)/m,

show more generally that [[aQ,eU],[gV,t c]] squares to a²kI when
eg=4a²/m and t=−aβ. This is sufficient and does not claim the entire
strong-hyperbolicity classification. The explicit a=1,e=2/m,g=2,t=(2−m)/m
case is exactly the full Clifford decomposition above.

After quotienting the SAME hidden K, replace observed coordinates (b,ψ) by
(w,ψ)=(b+γ_Hψ/m,ψ). The symbol becomes

 [[cξ,0],[2ιξ,−cξ]],

and its square is kI. The isolated Jordan obstruction is therefore not stable
under this particular coupled principal completion. A positive analytic
symmetrizer can be induced from the fixed Euclidean quotient of the parent
slotwise Dirac evolution; this is distinct from the native K95 action pairing.

Crucial grading: ψ here is the ambient gamma TRACE coordinate, not an arbitrary
source scalar with equal dimension. In the ambient grading it has opposite
spinor chirality. Under the coherent G lift it has grading −χ_H. Therefore the
augmented observed symbol classes are

 ambient:   ([H_C]−1)[D_H]Δ_N,
 horizontal coherent G: ([H_C]−1)[D_H][S_N].

In the SAME closed positive spin comparison with N=Sym²T*X, the first integer
index is0. The second equals300 signature(X): the scalar full-normal-spin
Dirac twist contributes

 ∫[4p1(N)−(32/24)p1(TX)]=(68/3)∫p1(TX)=68 signature(X),

and the opposite scalar grading subtracts it from observed368 signature(X).
Thus repairing the isolated propagation defect by this recognized companion
completion does not erase the grading/count burden. The change368→300 is due
to adding a specifically graded companion symbol, not a phase or an inferred
family. It supplies no source ν identification, native end correction,
physical count, or class-C action/BV witness.

The scalar grading is forced by the decomposition map, not chosen to obtain
an index: Γ_Y G=-χ_H Γ_Y and G j_Y=-j_Yχ_H imply that the coordinate
ψ=Γ_Y a transforms as −χ_Hψ. Similarly Γ_Yχ_Y=-χ_YΓ_Y forces opposite ambient
spinor grading on ψ. In observed coordinates (b,ψ) the horizontal grading is
diag(χ_H,−χ_H); the change w=b+γ_Hψ/m preserves that typed grading because
χ_Hγ_H=-γ_Hχ_H. Hence the two displayed symbol matrices are graded-conjugate.

The virtual factor [H_C]−1 has virtual rank3 on X4. This is NOT three physical
generations: its Chern character includes p1(TX), it remains tensored with the
full rank32 normal spinor bundle, and its integer index is300 signature(X) in
this comparison. Its rank is representation bookkeeping, not P3. A source
independent scalar ν acquires none of this identification merely by sharing
S's dimension or by permitting a pairing-compatible coefficient completion.

The full-Clifford companion uses the inherited trace form K/m (m=14), not K. Its offdiagonal coefficients2/m and2 are adjoints with that weight; a scalar normalization moves the weight and coefficients together. No source action pairing is silently changed.

## Evidence and acceptance boundary

Universal proofs are distinct from finite exact controls in
[the probe](../../tests/program-focus/native_rs_joint_compatibility_probe.py)
and [report](../../lab/process/native-rs-joint-compatibility.json).
Independent internal specialist cross-review applies; this is not external
certification or a Lean/full-class decision. The source register, class C,
physics ledger0.263 RA-F1/AC-F1/LT-SM8 and canon remain unchanged. Matrix18/18
coverage remains conditional; the joint class-C intersection remains open.
