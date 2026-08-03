---
title: "Compact-Image Obstructions for a Hyperbolic Grading in Sp(32,32)"
subtitle: "Neutral, grading-even, and extremal order parameters"
author: "Joseph Hernandez"
affiliation: "Independent Researcher"
date: "2026-08-03"
status: "post-ready release candidate"
version: "1.0.0"
claim_grade: "theorem-grade finite-dimensional core; explicit Sp(32,32) specialization; no physical-stability claim"
license: "CC BY 4.0"
---

# Compact-Image Obstructions for a Hyperbolic Grading in $\operatorname{Sp}(32,32)$

## Neutral, grading-even, and extremal order parameters

**Joseph Hernandez**  
Independent Researcher

## Abstract

Let a connected real reductive group $G$ act faithfully on a finite-dimensional
real vector space $E$, and let $A_Z=\exp(\mathbb R Z)$ be a one-parameter
subgroup. We study whether the stabilizer of a specified order parameter has
relatively compact image in $\operatorname{GL}(E)$, equivalently whether it
preserves a positive-definite inner product on $E$. We prove three elementary
compact-image obstructions. An $A_Z$-invariant vector retains the entire
one-parameter group in its stabilizer. An operator commuting with
$z=d\iota(Z)$ retains the same group in its centralizer. For the extremal leg,
assume that $\operatorname{ad}(Z)$ and $dR(Z)$ are diagonalizable over
$\mathbb R$. If the positive, respectively negative,
$\operatorname{ad}(Z)$-eigenspace sum contains $X_+$, respectively $X_-$, whose
image under $d\iota$ is nonzero nilpotent, then a maximal, respectively
minimal, $Z$-weight vector retains the corresponding unipotent one-parameter
subgroup. Whenever the retained subgroup has unbounded represented image, no
invariant positive-definite inner product exists.

For $G=\operatorname{Sp}(32,32)$ we verify the hypotheses directly in the
defining quaternionic matrix model. The relevant grading has only
$\operatorname{ad}(Z)$-eigenvalues $-2,0,2$; the two nonzero eigenspaces have
real dimension $2080$, are abelian, and consist of square-zero matrices. When
$z^2=1$, conjugation by $z$ separately defines a discrete involution on
$\operatorname{End}_{\mathbb R}(E)$, and a grading-even operator is precisely a
$Z$-commuting operator. We do not identify continuous $A_Z$-invariance of an
arbitrary vector representation with preservation of a discrete grading.

The ingredients are standard compact-group averaging, linear algebra, and
weight raising. The contribution is a self-contained synthesis for one fixed
hyperbolic grading, an explicit quaternionic specialization, and a diagnostic
separation of three commonly conflated notions: continuous neutrality,
discrete operator parity, and extremal weight. The result is finite-dimensional
and algebraic; it does not establish an interacting Hilbert space, a vacuum, a
dynamical condensate, or physical unitarity.

## 1. Result at a glance

The mathematical obstruction has three legs with deliberately separate
hypotheses:

| order parameter | subgroup forced into its stabilizer | compact-image obstruction |
|---|---|---|
| vector fixed by $A_Z$ | $A_Z$ | the tested image of $A_Z$ is unbounded |
| operator $O$ with $[O,d\iota(Z)]=0$ | $A_Z\subset C_G(O)$ | the same unbounded image |
| maximal $Z$-weight vector, with real-diagonalizable $\operatorname{ad}(Z)$ and $dR(Z)$ and nonzero nilpotent $d\iota(X_+)$ | the corresponding positive unipotent one-parameter subgroup | nonconstant polynomial growth in the tested image |
| minimal $Z$-weight vector, with real-diagonalizable $\operatorname{ad}(Z)$ and $dR(Z)$ and nonzero nilpotent $d\iota(X_-)$ | the corresponding negative unipotent one-parameter subgroup | nonconstant polynomial growth in the tested image |

For the displayed $\operatorname{Sp}(32,32)$ grading, all three mechanisms are
visible in exact blocks. The standard compact-reducing involution has
centralizer $\operatorname{Sp}(32)\times\operatorname{Sp}(32)$, but it does not
commute with the grading generator.

The strongest conclusion is:

> On the faithful finite-dimensional module tested here, vectors invariant
> under the unbounded grading flow, operators commuting with its infinitesimal
> generator, and extremal-weight vectors for real-diagonalizable
> $\operatorname{ad}(Z)$ and $dR(Z)$ with the corresponding sign-specific
> witness having nonzero nilpotent $d\iota$-image cannot have relatively compact
> stabilizer image. When the
> generator is involutory on the tested module, the operator statement applies
> in particular to grading-even operators.

Four distinctions are load-bearing.

1. Compactness is asserted for the closure of the **represented image**, not
   for an abstract source group hidden behind a nonfaithful action.
2. $A_Z$-invariance is invariance under a continuous one-parameter subgroup.
   It is not automatically a discrete parity statement.
3. Grading-even is defined for operators only when $z=d\iota(Z)$ supplies an
   involution by conjugation.
4. Preservation of a positive-definite form is a finite-dimensional algebraic
   proxy. It is not a theorem about interacting quantum stability.

## 2. Mathematical setting

### 2.1 Representations and stabilizers

Let $E$ be a finite-dimensional real vector space and let

$$
\iota:G\hookrightarrow\operatorname{GL}(E)
$$

be a faithful finite-dimensional representation of a connected real reductive
group. The underlying real representation is used even when $E$ originates as
a complex or quaternionic module.

All group representations in this paper are finite-dimensional continuous,
hence smooth, real Lie-group representations. Closures, boundedness, and
relative compactness are taken in the usual Euclidean topology of the relevant
real matrix space.

For a vector $w$ in a finite-dimensional representation
$R:G\to\operatorname{GL}(V)$, write

$$
G_w=\{g\in G:R(g)w=w\}.
$$

For a finite family $w_i\in V_i$ in representations $R_i$, its common vector
stabilizer is

$$
G_{\mathbf w}=\{g\in G:R_i(g)w_i=w_i\text{ for every }i\}.
$$

For $O\in\operatorname{End}_{\mathbb R}(E)$ under conjugation, the stabilizer
is the centralizer

$$
C_G(O)=\{g\in G:\iota(g)O=O\iota(g)\}.
$$

All compactness statements below concern the closure of the image under
$\iota$. Faithfulness is stronger than strictly necessary, but it prevents a
noncompact stabilizer direction from disappearing in the module on which
positivity is tested. The proofs require only that the named obstruction
subgroups have unbounded image under $\iota$.

### 2.2 Finite-dimensional invariant majorants

An **invariant positive majorant** for a subgroup $H\leq G$ means, in this
paper, a positive-definite real inner product $h$ on $E$ satisfying

$$
h(\iota(a)x,\iota(a)y)=h(x,y)
\qquad(a\in H).
$$

In finite dimensions every positive-definite norm induces the same vector-space
topology, and every bilinear form $b$ is continuous for that topology. After
rescaling the positive form, one may arrange the conventional domination
inequality

$$
|b(x,y)|^2\leq h(x,x)h(y,y).
$$

In this paper “majorant” means only the invariant positive-definite form
defined above; no infinite-dimensional notion of maximal, admissible, or
topology-defining majorant is intended. Those distinctions are substantive in
general Krein-space theory [Bognár 1974, chs. III--VI].

Suppose additionally that $E$ has a nondegenerate symmetric form $\eta$
preserved by $G$. If $h$ and $\eta$ are both $H$-invariant, define the
invertible $h$-self-adjoint operator $A$ by

$$
\eta(x,y)=h(x,Ay).
$$

To see equivariance explicitly, write $T=\iota(a)$ for $a\in H$. Simultaneous
$h$- and $\eta$-invariance gives

$$
h(x,T^{-1}ATy)=h(Tx,ATy)=\eta(Tx,Ty)=\eta(x,y)=h(x,Ay),
$$

so $T^{-1}AT=A$. Finite-dimensional functional calculus therefore gives

$$
|A|=(A^2)^{1/2},
\qquad C=A|A|^{-1},
\qquad C^2=1,
\qquad \eta(x,Cy)=h(x,|A|y).
$$

The commuting $h$-self-adjoint operators $A$ and $C$ satisfy

$$
\eta(Cx,y)=h(Cx,Ay)=h(x,ACy)=\eta(x,Cy),
$$

so $C$ is $\eta$-self-adjoint, while $AC=|A|$ gives
$\eta(x,Cx)=h(x,|A|x)>0$ for $x\ne0$. Conversely, suppose $C$ is an
$H$-equivariant, $\eta$-self-adjoint involution satisfying
$\eta(x,Cx)>0$ for every $x\ne0$. Then

$$
h_C(x,y)=\eta(x,Cy)
$$

is symmetric because $\eta$ is symmetric and $C$ is $\eta$-self-adjoint,
positive definite by hypothesis, and $H$-invariant because $C$ commutes with
$H$ and $\eta$ is invariant. This states all the conditions used in the
fundamental-symmetry formulation rather than treating positivity of
$\eta(\cdot,C\cdot)$ alone as its definition.

### 2.3 Continuous flow, hyperbolicity, and discrete operator parity

Fix $Z\in\mathfrak g$ and set

$$
A_Z=\exp(\mathbb R Z),
\qquad z=d\iota(Z).
$$

The hypothesis needed for the first two obstruction legs is simply that
$\iota(A_Z)$ is unbounded. A sufficient condition is that $z$ have a nonzero
real eigenvalue: on a corresponding eigenvector, $\exp(tz)$ grows like
$e^{t\lambda}$ in one time direction.

The extremal-weight leg needs a different hypothesis. We call $Z$
**$\operatorname{ad}$-hyperbolic** when $\operatorname{ad}(Z)$ is diagonalizable
over $\mathbb R$. Then

$$
\mathfrak g=\bigoplus_{\alpha\in\mathbb R}\mathfrak g_\alpha,
\qquad
\mathfrak g_\alpha=\{X\in\mathfrak g:[Z,X]=\alpha X\},
$$

and we set

$$
\mathfrak n_+=\bigoplus_{\alpha>0}\mathfrak g_\alpha,
\qquad
\mathfrak n_-=\bigoplus_{\alpha<0}\mathfrak g_\alpha.
$$

These are $\operatorname{ad}(Z)$-eigenspace sums. When $Z$ lies in a chosen
maximal split abelian subspace, they are sums of restricted-root spaces having
the same sign on $Z$ [Helgason 2001, chs. III, VI; Knapp 2002, ch. VI]. A
single nonzero real eigenvalue of $z$ does **not** imply this real
decomposition; the two hypotheses must not be conflated.

For any representation $R$, a vector is **$Z$-neutral** when $dR(Z)w=0$.
Equivalently,

$$
R(\exp tZ)w=\exp(t\,dR(Z))w=w,
$$

so it is fixed by the continuous group $A_Z$.

Only the extremal leg requires a weight decomposition. When $dR(Z)$ is
diagonalizable over $\mathbb R$, write

$$
V=\bigoplus_{\lambda\in\mathbb R}V_\lambda,
\qquad
V_\lambda=\{v:dR(Z)v=\lambda v\}.
$$

A nonzero $w\in V_\lambda$ has maximal, respectively minimal, $Z$-weight when
no weight greater, respectively smaller, than $\lambda$ occurs.

A separate discrete operator grading exists when $z^2=1$ on $E$. In that
case

$$
\sigma_Z(O)=zOz^{-1}=zOz
$$

is an involution on $\operatorname{End}_{\mathbb R}(E)$. An operator is
grading-even when $\sigma_Z(O)=O$, equivalently $[O,z]=0$, and grading-odd when
$\sigma_Z(O)=-O$, equivalently $\{O,z\}=0$. No corresponding order-two action
on an arbitrary vector representation is assumed. In particular, continuous
$A_Z$-neutrality is not called discrete grading invariance unless an additional
representation dictionary proves that identification.

## 3. Compactness and two visible witnesses

**Proposition 1 (invariant positive form versus compact closure).** Let
$H\leq\operatorname{GL}(E)$. An $H$-invariant positive-definite inner product on
$E$ exists if and only if $\overline H$ is compact.

**Proof.** If $h$ is invariant, $H$ lies in the orthogonal group $O(E,h)$,
which is compact in finite dimensions. Hence $\overline H$ is compact.

Conversely, if $\overline H$ is compact, choose any positive-definite inner
product $h_0$ and average it over normalized Haar measure:

$$
h(x,y)=\int_{\overline H}h_0(ax,ay)\,d\mu(a).
$$

The average is positive definite and $\overline H$-invariant. $\square$

This elementary equivalence fixes the exact stability predicate used in the
paper. It requires neither closedness nor reductivity of the original subgroup
$H$.

**Lemma 2 (unbounded one-parameter witnesses).** Suppose $H\leq G$.

1. If $A_Z\subset H$ and $\iota(A_Z)$ is unbounded, then
   $\overline{\iota(H)}$ is not compact.
2. If $H$ contains $\exp(tX)$ for every $t\in\mathbb R$, where
   $d\iota(X)$ is nonzero and nilpotent, then
   $\overline{\iota(H)}$ is not compact.

**Proof.** The first conclusion is immediate. In the second case,
$\exp(t\,d\iota(X))$ is a nonconstant polynomial in $t$, hence unbounded.
$\square$

## 4. Three compact-image obstructions

The four clauses below implement three mechanisms and intentionally do not
share one overstrong hypothesis.

**Theorem 3 (continuous-neutral, commuting-operator, and extremal
obstructions).** Let $G$, $E$, $\iota$, and $Z$ be as above.

1. Assume $\iota(A_Z)$ is unbounded. If every member of a finite family
   $w_i\in V_i$ is $Z$-neutral in its representation $R_i$, then
   $G_{\mathbf w}$ has non-relatively-compact image under $\iota$.
2. Assume $\iota(A_Z)$ is unbounded. If
   $O\in\operatorname{End}_{\mathbb R}(E)$ satisfies $[O,z]=0$, then $C_G(O)$ has
   non-relatively-compact image under $\iota$.
3. Assume $Z$ is $\operatorname{ad}$-hyperbolic, $dR(Z)$ is diagonalizable
   over $\mathbb R$, and $w\ne0$ is a maximal $Z$-weight vector. If
   $\mathfrak n_+$ contains $X_+$ for which $d\iota(X_+)$ is nonzero
   nilpotent, then $G_w$ has non-relatively-compact image under $\iota$.
4. Assume $Z$ is $\operatorname{ad}$-hyperbolic, $dR(Z)$ is diagonalizable
   over $\mathbb R$, and $w\ne0$ is a minimal $Z$-weight vector. If
   $\mathfrak n_-$ contains $X_-$ for which $d\iota(X_-)$ is nonzero
   nilpotent, then $G_w$ has non-relatively-compact image under $\iota$.

Consequently none of these stabilizers preserves a positive-definite inner
product on $E$.

**Proof.**

1. Since $dR_i(Z)w_i=0$,
   $$
   R_i(\exp tZ)w_i=\exp(t\,dR_i(Z))w_i=w_i
   $$
   for every $i$ and $t$. Hence $A_Z\subset G_{\mathbf w}$. Lemma 2 and
   Proposition 1 apply.
2. The commutator condition gives
   $$
   O\exp(tz)=\exp(tz)O.
   $$
   Since $\iota(\exp tZ)=\exp(tz)$, we have
   $A_Z\subset C_G(O)$. Apply Lemma 2 and Proposition 1.
3. Suppose $dR(Z)w=\lambda w$ and $\lambda$ is maximal. For
   $X\in\mathfrak g_\alpha$ with $\alpha>0$,
   $$
   dR(Z)dR(X)w=(\lambda+\alpha)dR(X)w.
   $$
   No weight above $\lambda$ occurs, so $dR(X)w=0$. By linearity,
   $dR(\mathfrak n_+)w=0$, in particular $dR(X_+)w=0$. Therefore
   $$
   R(\exp tX_+)w=\exp(t\,dR(X_+))w=w,
   $$
   and $\exp(\mathbb R X_+)\subset G_w$. Its image under $\iota$ is
   unbounded by Lemma 2. Proposition 1 completes the maximal case.
4. For a minimal weight the same calculation with $\alpha<0$ shows that
   $dR(\mathfrak n_-)w=0$. In particular $X_-$ exponentiates to a subgroup of
   $G_w$ whose represented image is unbounded by Lemma 2. Proposition 1
   completes the minimal case. $\square$

**Remark 4 (vector versus line stabilizers).** A parabolic subgroup generally
stabilizes the extremal line $\mathbb Rw$ rather than the chosen vector. The
proof uses only a positive or negative nilpotent subgroup. Its Lie algebra
annihilates $w$, so exponentiation fixes $w$ pointwise. The vector-stabilizer
claim is therefore stronger than, and not confused with, line stabilization.

**Remark 5 (minimal hypotheses).** Faithfulness can be weakened if the tested
representation still detects the named unbounded subgroup. Likewise, parts
3--4 each require only one represented nonzero nilpotent witness of the
appropriate sign, not algebraicity of every representation or a classification
of every root space.

## 5. Compact-reducing operators and parity

Let $P'\in\operatorname{End}_{\mathbb R}(E)$ be an involution such that
$C_G(P')$ has relatively compact represented image. This is the only property
needed for the next result.

**Corollary 6 (a compact-reducing involution cannot commute with the grading
flow).** If $\iota(A_Z)$ is unbounded, then $[P',z]\ne0$.

**Proof.** If $[P',z]=0$, then $A_Z\subset C_G(P')$, contradicting relative
compactness by Lemma 2. $\square$

In a classical matrix realization, an additional hypothesis is needed before
calling $P'$ a Cartan implementer: conjugation by $P'$ must normalize $G$ (or
its Lie algebra) and implement a Cartan involution there. The compactness
argument itself does not infer this structure from involutivity alone.

Corollary 6 proves non-invariance, not pure oddness. If $z^2=1$, every operator
has the decomposition

$$
P'=P'_{\mathrm{even}}+P'_{\mathrm{odd}},
\qquad
P'_{\mathrm{even}}=\frac12(P'+zP'z),
\qquad
P'_{\mathrm{odd}}=\frac12(P'-zP'z).
$$

The condition $[P',z]\ne0$ says only that the odd component is nonzero. It does
not say that the even component vanishes. Pure oddness follows only from the
additional homogeneous condition $zP'z=-P'$.

## 6. The $\operatorname{Sp}(32,32)$ specialization

### 6.1 Quaternionic matrix model

Let $n\geq1$ and regard $E=\mathbb H^n\oplus\mathbb H^n$ as a right
quaternionic vector space, with quaternionic matrices acting on the left and
$^*$ denoting conjugate transpose. Unless otherwise stated,
$\operatorname{End}(E)$ means $\operatorname{End}_{\mathbb R}(E)$ on the
$8n$-dimensional underlying real space. The calculation below is valid for
every $n\geq1$; the numerical specialization of interest is $n=32$, where
$\dim_{\mathbb R}E=256$. Set

$$
\beta=
\begin{pmatrix}
I_n&0\\
0&-I_n
\end{pmatrix}.
$$

The real Lie group

$$
G=\operatorname{Sp}(n,n)
=\{g\in\operatorname{GL}_{2n}(\mathbb H):g^*\beta g=\beta\}
$$

is a connected real reductive Lie group and acts faithfully on the underlying
real vector space of $E$ [Sedano-Mendoza 2019]. Its Lie algebra is

$$
\mathfrak g=
\left\{
X=
\begin{pmatrix}
A&B\\
B^*&D
\end{pmatrix}
:
A^*=-A,\ D^*=-D
\right\}.
$$

We use the standard notation and real-form convention of
[Sedano-Mendoza 2019]. The maximal compact subgroup is

$$
K=\operatorname{Sp}(n)\times\operatorname{Sp}(n).
$$

Since $\dim_{\mathbb R}\operatorname{Sp}(m)=m(2m+1)$,

$$
\dim G=(2n)(4n+1),
$$

$$
\dim K=2n(2n+1),
\qquad
\dim(G/K)=4n^2.
$$

At $n=32$ these are $8256$, $4160$, and $4096$, respectively.

The group preserves the nondegenerate real symmetric form

$$
\eta(x,y)=\operatorname{Re}(x^*\beta y).
$$

For the compact reducer $P=\beta$ used below,
$h_P(x,y)=\eta(x,Py)=\operatorname{Re}(x^*y)$ is positive definite. Thus the
abstract fundamental-symmetry construction of Section 2.2 and the concrete
quaternionic model use the same positivity predicate.

### 6.2 The grading generator and a compact reducer

Define

$$
z=d\iota(Z)=
\begin{pmatrix}
0&I_n\\
I_n&0
\end{pmatrix}.
$$

Direct multiplication gives

$$
z^*\beta+\beta z=0,
$$

so $z\in\mathfrak{sp}(n,n)$, and $z^2=I$. Moreover,

$$
\exp(tz)=
\begin{pmatrix}
\cosh(t)I_n&\sinh(t)I_n\\
\sinh(t)I_n&\cosh(t)I_n
\end{pmatrix}
$$

has eigenvalues $e^t$ and $e^{-t}$. Thus $\iota(A_Z)$ is unbounded. The
continuous group $A_Z$ and the discrete conjugation involution
$O\mapsto zOz$ are related through the same infinitesimal operator but are not
the same action.

The standard compact-reducing involution is $P=\beta$. It satisfies

$$
P^2=I,
\qquad
Pz=-zP.
$$

An element commuting with $P$ is block diagonal, and intersecting the
block-diagonal group with $g^*\beta g=\beta$ gives

$$
C_G(P)=\operatorname{Sp}(n)\times\operatorname{Sp}(n).
$$

Here conjugation by $P$ normalizes $G$ and implements the standard Cartan
involution. This particular $P$ is genuinely grading-odd. Corollary 6 gives the
reducer-independent statement relative to this fixed $z$: any involution with
relatively compact centralizer fails to be grading-even, although a conjugate
representative need not be purely odd in the fixed frame.

### 6.3 Exact $\operatorname{ad}(Z)$ decomposition

The isotropic basis makes the structure transparent. Let

$$
S=\frac1{\sqrt2}
\begin{pmatrix}
I_n&I_n\\
I_n&-I_n
\end{pmatrix},
\qquad
J=
\begin{pmatrix}
0&I_n\\
I_n&0
\end{pmatrix}.
$$

Then

$$
S^{-1}zS=\begin{pmatrix}I_n&0\\0&-I_n\end{pmatrix},
\qquad
S^*\beta S=J.
$$

Writing $Y=S^{-1}XS=\begin{psmallmatrix}a&b\\c&d\end{psmallmatrix}$, the Lie
condition $Y^*J+JY=0$ is equivalent to

$$
d=-a^*,\qquad b^*=-b,\qquad c^*=-c.
$$

Consequently

$$
\mathfrak g_2=
\left\{\begin{pmatrix}0&b\\0&0\end{pmatrix}:b^*=-b\right\},\quad
\mathfrak g_0=
\left\{\begin{pmatrix}a&0\\0&-a^*\end{pmatrix}:a\in M_n(\mathbb H)\right\}
\cong\mathfrak{gl}(n,\mathbb H),
$$

$$
\mathfrak g_{-2}=
\left\{\begin{pmatrix}0&0\\c&0\end{pmatrix}:c^*=-c\right\}.
$$

This immediately exhibits the nonzero eigenspaces as abelian and square-zero.
It also identifies
$\mathfrak p_Z=\mathfrak g_0\oplus\mathfrak g_2$ as the parabolic stabilizing
the first, isotropic quaternionic $n$-plane, with abelian nilradical
$\mathfrak g_2$: in the $S$-basis, its matrices are exactly the displayed
upper-triangular blocks and hence preserve
$\mathbb H^n\oplus0$, while the lower-left block detects failure to preserve
that plane. Rescaling the grading element by $1/2$ turns the displayed
degrees into $-1,0,1$, so this is a $|1|$-grading rather than a depth-two
$|2|$-grading [Čap and Slovák 2009, chs. 2--3].

Conjugating this decomposition back to the original basis gives the following
blocks and fixes every sign explicitly.

For

$$
X=
\begin{pmatrix}
A&B\\
B^*&D
\end{pmatrix}
\in\mathfrak{sp}(n,n),
$$

one computes

$$
[z,X]=
\begin{pmatrix}
B^*-B&D-A\\
A-D&B-B^*
\end{pmatrix}.
$$

Solving $[z,X]=2X$ gives

$$
X_+(B)=
\begin{pmatrix}
-B&B\\
-B&B
\end{pmatrix},
\qquad B^*=-B.
$$

Solving $[z,X]=-2X$ gives

$$
X_-(B)=
\begin{pmatrix}
B&B\\
-B&-B
\end{pmatrix},
\qquad B^*=-B.
$$

Finally $[z,X]=0$ gives

$$
X_0(A,B)=
\begin{pmatrix}
A&B\\
B&A
\end{pmatrix},
\qquad A^*=-A,\quad B^*=B.
$$

Therefore

$$
\mathfrak{sp}(n,n)=\mathfrak g_{-2}\oplus\mathfrak g_0\oplus\mathfrak g_{2}.
$$

A skew-Hermitian quaternionic $n\times n$ matrix has real dimension

$$
3n+4\binom n2=n(2n+1),
$$

while a Hermitian one has real dimension

$$
n+4\binom n2=n(2n-1).
$$

At $n=32$ this yields

$$
\dim\mathfrak g_{2}=\dim\mathfrak g_{-2}=32(65)=2080,
$$

$$
\dim\mathfrak g_0=32(65)+32(63)=4096,
$$

and $2080+4096+2080=8256$ as required.

The decisive nilpotence is equally explicit. For all skew-Hermitian $B,C$,

$$
X_+(B)X_+(C)=0,
\qquad
X_-(B)X_-(C)=0.
$$

Thus $\mathfrak g_2$ and $\mathfrak g_{-2}$ are nonzero abelian subalgebras
whose elements are square-zero in the defining representation. In particular,

$$
\exp(tX_\pm(B))=I+tX_\pm(B)
$$

is unbounded for $B\ne0$. These eigenspaces are the positive and negative
$\operatorname{ad}(Z)$-eigenspace sums; relative to a maximal split abelian
subspace containing $Z$, they are sums of restricted-root spaces. This block
calculation supplies every sign-specific witness hypothesis used by Theorem
3(3)--(4) without appealing to a toy model or to an unspecified algebraicity
assumption.

**Corollary 7 (the $\operatorname{Sp}(n,n)$ family and the
$\operatorname{Sp}(32,32)$ specialization).** For every $n\geq1$ and the $z$
above, the common stabilizer of any finite family of $A_Z$-invariant vectors in
finite-dimensional smooth representations has non-relatively-compact image
under the defining representation. The same holds for the centralizer of every
grading-even operator on $E$. If $R$ is a finite-dimensional representation
with $dR(Z)$ diagonalizable over $\mathbb R$, the conclusion also holds for
every nonzero maximal or minimal $Z$-weight vector: the explicitly displayed
$X_+$ or $X_-$ supplies the required nonzero nilpotent witness of the
corresponding sign. At $n=32$, the positive and negative witness spaces each
have real dimension $2080$.

## 7. Why the scope conditions are necessary

### 7.1 One real eigenvalue is not full hyperbolicity

In a product of a split group and a compact nonabelian group, a semisimple
element can have a split component and an elliptic component. A faithful direct
sum representation then has a nonzero real eigenvalue and also nonreal
eigenvalues in its complexified spectrum; on the underlying real space the
elliptic part appears in rotation blocks and is not real diagonalizable. Its
one-parameter image is unbounded, so Theorem 3(1) and (2) can still apply, but
a real $\operatorname{ad}(Z)$-eigenspace decomposition for parts (3)--(4) does
not follow. This is why the theorem states the two hypotheses separately.

Nor does $\operatorname{ad}$-hyperbolicity create a nilpotent witness. For
$G=\mathbb R_{>0}$ acting on $E=\mathbb R$ by scalar multiplication,
$\operatorname{ad}(Z)=0$ is real diagonalizable but
$\mathfrak n_+=\mathfrak n_-=0$; the nonzero vector $1$ is both maximal and
minimal and has trivial, hence compact, stabilizer. The sign-specific witness
hypothesis is therefore indispensable.

### 7.2 Not every charged vector has noncompact stabilizer

Theorem 3 does not cover a non-extremal weight vector or a vector that is not a
$Z$-eigenvector. This exclusion is substantive. A timelike vector in the
standard representation of $\operatorname{SO}(2,1)$ has compact stabilizer
$\operatorname{SO}(2)$ but is not an eigenvector of a boost mixing its time and
space coordinates. Thus the stronger slogan “every boost-charged vector has
noncompact stabilizer” is false.

### 7.3 Compact subgroups need not use one preferred frame

Maximal compact subgroups of a connected real reductive group are conjugate,
not identical. A compact subgroup can lie in a tilted conjugate $gKg^{-1}$
without commuting with one preferred Cartan implementer. Neither Theorem 3 nor
Corollary 6 uses the false implication

$$
\text{compact image of }H
\Longrightarrow
\iota(H)\subset C_{\operatorname{GL}(E)}(P)
$$

for a fixed $P$.

## 8. Scope and interpretation boundary

The theorem is entirely a finite-dimensional statement about represented
stabilizers. “Order parameter” means a chosen vector, family of vectors, or
operator on which a stabilizer is taken. It does not assert that the object is
a dynamically formed condensate or a vacuum expectation value.

If a physical model identifies an involutory $z$ with a chirality or mirror
grading, Corollary 7 says that a grading-even operator cannot simultaneously
produce a compact-image centralizer in this defining module. Applying the
vector legs to the same physical grading requires an additional dictionary
identifying the relevant vector representation and its $A_Z$ action. The
paper does not supply or assume such a physical dictionary.

The compact boundary is:

- interacting unitarity or ghost clearance;
- a physical state space, observable algebra, or scattering operator;
- existence or dynamical selection of a vacuum;
- anomaly cancellation, a mass spectrum, or chirality of a field theory;
- compactification of spacetime or extra dimensions;
- completeness of any model-specific order-parameter census;
- a theorem for non-extremal or mixed-weight vectors, nonfaithfully detected
  subgroups, or infinite-dimensional metric operators and domains.

These are not hidden premises of the proof. They are different problems.

## 9. Escape taxonomy and falsifiers

The theorem is diagnostic: a proposed escape should name the hypothesis it
changes.

1. **Bounded flow.** Show that the tested image of $A_Z$ is bounded. This
   defeats parts (1) and (2), but it is false for the displayed
   $\operatorname{Sp}(32,32)$ generator.
2. **Non-invariant vector.** Use a vector not fixed by $A_Z$ and not extremal
   for the $Z$-weight decomposition.
3. **Noncommuting operator.** Use an operator that does not commute with $z$.
   A compact reducer must take this route by Corollary 6.
4. **No represented nilpotent witness.** Exhibit a setting in which the
   relevant positive or negative eigenspace is absent or invisible in the
   majorant-tested representation.
5. **Different positivity predicate.** Replace invariant positive-definite
   inner product on $E$ with a precisely defined physical construction not
   equivalent to compact represented closure.
6. **Infinite-dimensional exit.** Supply domains, closures, topologies, and
   boundedness hypotheses adequate for an infinite-dimensional theorem.

A counterexample to any written implication would falsify the theorem. A model
lying outside one of the quantified classes is a scope exit, not a
counterexample.

## 10. Machine-checked hardening and reproducibility

The written proofs are load-bearing. The repository candidate includes three
paper-specific machine-checking layers:

1. An exact SageMath certificate constructs rational quaternionic matrices and
   checks Lie-algebra membership, the $\pm2$ commutator equations, mutual
   square-zero products, the exact isotropic basis change and triangular block
   forms, nonzero linear truncation witnesses, and all dimension formulas.
   Together with $\exp(tX)=I+tX$ from $X^2=0$, the nonzero witnesses certify
   the stated polynomial growth.
2. A property-based Python certificate generates exact small-rank quaternionic
   matrices, checks the same identities without floating point, and includes
   planted sign and parity mutations that the test suite must reject.
3. A Lean 4 module checks a narrow algebraic kernel: conjugation-fixed versus
   commuting parity for an involutory element, the shifted-eigenvector identity
   behind weight raising, extremal annihilation under an explicit no-higher-
   weight hypothesis, and the square-zero block maps.

The Lean module does **not** formalize Proposition 1, Haar averaging, the full
theory of real reductive groups, quaternionic Lie-group membership, or the
physical interpretation. The Sage and property tests are executable
certificates, not substitutes for the general proof. Exact file paths, commands,
dependency locks, theorem names, expected outputs, and axiom dependencies appear
in `REPRODUCE.md` and `VERIFICATION.md` beside this manuscript. An archival
submission must include the complete versioned evidence tree listed below and
its checksum manifest. If this Markdown file is circulated alone, the machine
checks are unavailable to that reader and should receive no evidentiary weight.

## 11. Prior art, novelty, and use

Every general ingredient is established mathematics:

- invariant inner products can be averaged over compact groups;
- Cartan involutions determine maximal compact subgroups, unique up to
  conjugacy;
- a nonzero real weight makes a one-parameter group unbounded in the tested
  representation;
- extremal-weight directions are annihilated by the appropriate raising or
  lowering algebra;
- a one-parameter subgroup with nonzero nilpotent image is unbounded in the
  tested representation.

Compact averaging and Cartan/restricted-root structure are standard in
[Helgason 2001, chs. III, VI, IX; Knapp 2002, chs. IV, VI].
Indefinite-inner-product terminology is treated in [Bognár 1974, chs.
III--VI]. The $|1|$-graded parabolic interpretation is standard
[Čap and Slovák 2009, chs. 2--3]. Draper and Meulewaeter [2022, §§2--4]
classify inner ideals of finite-dimensional real simple Lie algebras up to
automorphism; the abelian nilradicals displayed here belong to that established
landscape, and no new classification is claimed. Khare [2017] supplies broader
context on standard parabolic subsets, weight-set faces, and associated
stabilizers; the local raising-operator argument used here is proved directly.
Richardson and Slodowy [1990] is contextual literature on real reductive orbits
and minimum vectors, not a source for the compact-image theorem. Quaternionic
symplectic notation and dimensions are consistent with [Sedano-Mendoza 2019].

Accordingly, this paper does not claim a new theorem of general Lie theory. Its
narrow contribution is:

1. a single, assumption-explicit obstruction package separating continuous
   neutrality, discrete operator parity, and extremal weight;
2. a complete block-level verification for the fixed
   $\operatorname{Sp}(32,32)$ grading;
3. correction of three tempting overstatements: one real eigenvalue is not full
   hyperbolicity, compact subgroups need not share one fixed Cartan frame, and
   noncommuting does not imply purely odd;
4. a falsifier and escape taxonomy that makes competing constructions state
   exactly which hypothesis they leave.

The practical use is diagnostic. It prevents compactness, positivity, and
grading preservation from being bundled together by terminology when their
stabilizer consequences are incompatible.

## 12. Conclusion

For a faithful finite-dimensional action, preservation of a positive-definite
inner product is equivalent to compact closure of the represented subgroup.
This makes three stabilizer obstructions immediate once their hypotheses are
typed correctly: $A_Z$-invariant vectors and $Z$-commuting operators retain an
unbounded grading flow. When $\operatorname{ad}(Z)$ and $dR(Z)$ are real
diagonalizable, a maximal (respectively minimal) weight vector retains a
positive (respectively negative) unipotent one-parameter subgroup whenever the
corresponding eigenspace sum contains $X_+$ (respectively $X_-$) with nonzero
nilpotent $d\iota$-image.

In $\operatorname{Sp}(32,32)$ the required noncompact directions are not
inferred from general terminology. They are visible in exact quaternionic
blocks: the grading flow has eigenvalues $e^{\pm t}$, and its positive and
negative $\operatorname{ad}(Z)$ eigenspaces are $2080$-dimensional abelian
spaces of square-zero matrices. A compact-reducing involution therefore cannot
be grading-even in this module.

The result is a scoped compact-image theorem. Its value lies in making three
often conflated obstruction mechanisms, their exact hypotheses, and their
honest exits explicit.

## References

- Bognár, János. *Indefinite Inner Product Spaces*. Ergebnisse der Mathematik
  und ihrer Grenzgebiete, vol. 78. Springer, 1974. See chs. III--VI,
  pp. 58--146.
  [doi:10.1007/978-3-642-65567-8](https://doi.org/10.1007/978-3-642-65567-8).
- Čap, Andreas, and Jan Slovák. *Parabolic Geometries I: Background and
  General Theory*. Mathematical Surveys and Monographs 154. American
  Mathematical Society, 2009. See chs. 2--3.
  [doi:10.1090/surv/154](https://doi.org/10.1090/surv/154).
- Draper, Cristina, and Jeroen Meulewaeter. “Inner Ideals of Real Simple Lie
  Algebras.” *Bulletin of the Malaysian Mathematical Sciences Society* 45
  (2022): 2313--2345. See §§2--4.
  [doi:10.1007/s40840-022-01321-0](https://doi.org/10.1007/s40840-022-01321-0).
- Helgason, Sigurdur. *Differential Geometry, Lie Groups, and Symmetric Spaces*.
  Graduate Studies in Mathematics 34, corrected reprint. American Mathematical
  Society, 2001. See chs. III, VI, and IX.
  [doi:10.1090/gsm/034](https://doi.org/10.1090/gsm/034).
- Khare, Apoorva. “Standard Parabolic Subsets of Highest Weight Modules.”
  *Transactions of the American Mathematical Society* 369 (2017): 2363–2394.
  [doi:10.1090/tran/6710](https://doi.org/10.1090/tran/6710);
  [arXiv:1409.4133](https://arxiv.org/abs/1409.4133).
- Knapp, Anthony W. *Lie Groups: Beyond an Introduction*, 2nd ed. Progress in
  Mathematics 140. Birkhäuser, 2002. See chs. IV and VI. ISBN
  978-0-8176-4259-4.
- Richardson, R. W., and P. J. Slodowy. “Minimum Vectors for Real Reductive
  Algebraic Groups.” *Journal of the London Mathematical Society* 42 (1990):
  409–429.
  [doi:10.1112/jlms/s2-42.3.409](https://doi.org/10.1112/jlms/s2-42.3.409).
- Sedano-Mendoza, Manuel. “Isometric Actions of Quaternionic Symplectic
  Groups.” *Journal of Lie Theory* 29, no. 3 (2019): 755–786.
  [doi:10.5802/jolt.1077](https://doi.org/10.5802/jolt.1077).

## Paper-specific evidence map

Only the following files are evidence for this paper:

- `good-stable-compactification-no-go.md`
- `REPRODUCE.md`
- `VERIFICATION.md`
- `evidence/compact_image_obstructions_exact.py`
- `evidence/compact_image_obstructions_properties.py`
- `evidence/check_lean_receipt.sh`
- `evidence/pyproject.toml`
- `evidence/uv.lock`
- `evidence/checksums.sha256`
- `Lean/GUFormalization/CompactImageObstructions.lean`
- `Lean/GUFormalization/CompactImageObstructionsAxioms.lean`

The wider repository contains exploratory and superseded material that is not
relied upon here.
