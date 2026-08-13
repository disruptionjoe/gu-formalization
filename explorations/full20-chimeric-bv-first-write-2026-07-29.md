---
title: "Full-20 chimeric/BV first write: a finite coarse observer ansatz exists, while the whole bidirectional envelope is not a one-copy integer differential"
status: active_research
doc_type: result
created: 2026-07-29
work_item: SOURCE-OWNED-CHIMERIC-BV-CAMPAIGN-S1
code:
  - tests/channel-swings/full20_chimeric_bv_first_write_probe.py
canon_verdict_change: none
---

# Full-20 chimeric/BV first write

## Result

The first construction swing returns:

```text
S1-SPLIT-VERDICT
COARSE-RELATIVE-OBSERVER-ANSATZ-WRITTEN
FULL-136-ALLOWED-ENVELOPE-Z2-COLORING-UNIQUE-UP-TO-REVERSAL
WHOLE-BIDIRECTIONAL-136-ENVELOPE-NOT-DEGREE+1-ON-ONE-COPY
FOUR-STAGE-0-1-13-14-CANDIDATE-CARRIER-TYPED; DIFFERENTIAL-UNBUILT
CHOSEN-ONE-STAGE-FIXED-A-BV: COMPLEX-RANK-4608; REAL-RANK-9216
W131-CARRIER-BLOCK-INHERITED
NATIVE-ADJOINT/ROLL/FORMULA-SUPPORT/FULL-AMBIENT-BV-OPEN
```

There is a genuine positive construction. On the complete 20-slot observer
carrier, a nine-block first-order operator family can be written using only
the spin Dirac operator, gamma splitting, twistor, divergence, projected
vector-spinor Dirac operator, and the inherited W131 block. It has eight
off-core complex coefficients, one open W131 lower-order scalar, and three
candidate gauge-generator coefficients. It is a short natural-map family,
not 136 independently fitted cell coefficients. Every observer slot occurs
in its coarse \(S/I/R\) typing envelope, including all eight `X`
irreducibles. The formulas' actual irrep-level nonzero support has not yet
been computed.

The chosen first-stage observer-sector BV ansatz can also be exactly
enumerated.
Relative to a fixed background connection \(A\), it has 64 irreducible
coordinates and complex rank \(4608\): 20 fields, 20 density-dual
antifields, one four-slot commuting RS ghost and its antifield, and one
four-slot antighost/Nakanishi--Lautrup doublet with antifields. The real
Hamiltonian theory displayed below uses the underlying real space, of rank
\(9216\). Reducibility, compensators, and ambient gauge sectors are not yet
known, so neither absolute BV completeness nor minimality is claimed.

The preregistered filtration expectation does **not** survive Layer 0. The
complete 136-cell **allowed envelope** has a unique \(\mathbb Z_2\) coloring
up to global reversal, with two rank-960 halves. That global reversal is a
convention, not one physical datum. Because every allowed first-order cell
has its transposed cell, the **whole envelope** cannot be an integer
degree-\(+1\) endomorphism of one copy of \(\mathcal E_{20}\). The integer
equation would demand both
\(f_j=f_i+1\) and \(f_i=f_j+1\).

This does not kill a sparse or oriented one-copy differential; its reverse
formal-adjoint cells may belong to \(q^\times\), not \(q\). The source-shaped
candidate arena is instead the four-stage carrier at ordinary form degrees

\[
0\longrightarrow1\longrightarrow13\longrightarrow14
\]

with complex ranks

\[
128\longrightarrow1792\longrightarrow1792\longrightarrow128.
\]

Its even and odd rolls both have rank \(1920\). Identifying those two rolled
halves with normalized copies of the 20-slot observer carrier requires
explicit Hodge/Krein roll maps and their phases. Those maps are the next
construction datum. They are not one scalar, and no four-stage differential
has yet been written.

No master equation, Noether identity, nilpotency, B5 cohomology, transport,
physical index, generation count, mass, stationary background, or native
source recovery follows.

## Plain English

We can now write a serious candidate action around the whole GU fermion
carrier rather than only the Rarita--Schwinger part. It is finite and
inspectable: twelve continuous coefficient choices are exposed, and none is
chosen using the desired chirality, count, endpoint sign, or later
cohomology.

The attempt also found that the campaign had asked one maximal envelope to do
two incompatible jobs. A rolled differential can be odd after folding, but
the full bidirectional 136-cell envelope cannot simultaneously be an
ordinary integer degree-\(+1\) map on one unduplicated 20-slot bundle.
The source-shaped four-stage arena is now typed as a candidate. The missing
information is which oriented support survives and how GU's Hodge and Krein
structures identify the high-form stages with the low-form stages during the
roll.

This is the kind of failure that advances the construction: it replaces
"some filtration datum is missing" with exact bundles, exact ranks, one
maximal-envelope parity, one precisely scoped impossible interpretation, and
two explicit roll maps to build.

## Layer 0: four distinctions that control the swing

### 1. Carrier, equation bundle, and antifield

Write

\[
\mathcal E
=\mathcal E_{20}
=S_0\oplus I_1\oplus R_1,
\qquad
I=\operatorname{im}\Gamma,\quad
R=\ker\Gamma .
\]

Three objects must remain separate:

\[
D_{\mathbf c}:\mathcal E\longrightarrow\mathcal E,
\]

\[
\mathcal E^\vee_{\rm dens}
=\operatorname{Dens}_Y\otimes\mathcal E^\vee,
\qquad
H_{\mathbf c}:\mathcal E_{\mathbb R}\longrightarrow
\mathcal E^\vee_{{\rm dens},\mathbb R},
\]

and the shifted BV coordinate

\[
Z^+\in\mathcal E^\vee_{\rm dens}[-1].
\]

\(D_{\mathbf c}\) is a carrier endomorphism. \(H_{\mathbf c}\) is the
variational equation. \(Z^+\) is an antifield coordinate. A common `!`
notation can hide the shift, so this packet writes it explicitly.

All observer ranks in this packet are complex. The native Krein form is
Hermitian, so its lowering map is conjugate-linear over \(\mathbb C\):

\[
\kappa_{K,\mu}:\mathcal E\longrightarrow
\mathcal E^\vee_{\rm dens}.
\]

The displayed `Re` action and BV form are interpreted on the underlying real
graded space

\[
\mathcal F_{\rm BV,rel,\mathbb R}.
\]

Its real rank is twice the complex-coordinate census. This realification is
a mathematical typing choice, not a selection of GU's still-open native
Lorentzian real structure.

### 2. Physical and BV pairings

The physical quadratic term uses the observer Krein form \(K\). The BV odd
symplectic form uses canonical density evaluation between each coordinate
and its shifted cotangent partner. Extending \(K\) to ghosts is neither
needed nor done. After explicit realification, both Hamiltonian structures
used below are real-bilinear.

### 3. W131 and the Euler equation

W131 is an endomorphism of \(R=\ker\Gamma\):

\[
D_{\rm W131}
=P_R D_VP_R+\mu_0P_R:R\longrightarrow R.
\]

It is not already an equation valued in a density dual. The comparison map is

\[
\kappa_R:R\longrightarrow R^\vee_{\rm dens}
\quad\text{(conjugate-linear over \(\mathbb C\), real-linear after realification)}.
\]

The exact carrier statement is

\[
\pi_R D_{\mathbf c}\iota_R=D_{\rm W131}.
\]

The universally typed equation-level statement is

\[
\iota_R^\vee H_{\mathbf c}\iota_R
=
\mathsf{Pol}_{K,\rm gr}
\left(
\iota_R^\vee\kappa_{K,\mu}D_{\mathbf c}\iota_R
\right).
\]

It simplifies only if the \(R\) restriction is Krein-orthogonal:

\[
\iota_R^\vee\kappa_{K,\mu}=\kappa_R\pi_R.
\]

If that identity holds and

\[
\mathsf{Pol}_{K,\rm gr}
\]

is fixed by the odd-field convention, Krein phases, formal adjoint, and
integration-by-parts sign, then

\[
\iota_R^\vee H_{\mathbf c}\iota_R
=
\mathsf{Pol}_{K,\rm gr}
\left(\kappa_R D_{\rm W131}\right).
\]

This becomes \(\kappa_RD_{\rm W131}\) only on the future
Krein-orthogonal, adjoint, Green/domain stratum where those equalities are
proved. The carrier block is inherited now; the simplified variational
equality remains conditional on the native five-field packet.

### 4. Relative observer BV theory versus full ambient IG BV theory

This packet treats \(A\) as a fixed background argument and writes

\[
S_{\rm rel}^{(2)}[-;A].
\]

That is adequate for the observer-fermion first write. It is not a complete
ambient IG BV action. If \(A\), the metric/soldering data, or the affine
one-form translation are independently varied gauge fields, each needs its
own field, antifield, ghost, reducibility, and nonminimal census. Which
connection symmetries are ordinary gauge redundancies and which belong to
the affine/super extension is a separate semantic fork; no huge untyped
bundle is silently appended here.

## Exact 20-slot observer sheet

All entries are complexified
\(H_{\mathbb C}=\operatorname{Spin}(4,\mathbb C)\times
\operatorname{Spin}(10,\mathbb C)\) representations. They are odd observer
fields of ghost number zero. `dual` records the exact mirror slot appearing
in the density-dual representation.

| # | slot | type label | dim | form | dual/mirror | W131 |
| ---: | --- | --- | ---: | ---: | --- | :---: |
| 1 | `S:E+:L16+` | `(2,1,16+)` | 32 | 0 | `S:E-:L16-` | no |
| 2 | `S:E+:R16-` | `(1,2,16-)` | 32 | 0 | `S:E-:R16+` | no |
| 3 | `S:E-:L16-` | `(2,1,16-)` | 32 | 0 | `S:E+:L16+` | no |
| 4 | `S:E-:R16+` | `(1,2,16+)` | 32 | 0 | `S:E+:R16-` | no |
| 5 | `imGamma:E+:L16+` | `(2,1,16+)` | 32 | 1 | `imGamma:E-:L16-` | no |
| 6 | `imGamma:E+:R16-` | `(1,2,16-)` | 32 | 1 | `imGamma:E-:R16+` | no |
| 7 | `imGamma:E-:L16-` | `(2,1,16-)` | 32 | 1 | `imGamma:E+:L16+` | no |
| 8 | `imGamma:E-:R16+` | `(1,2,16+)` | 32 | 1 | `imGamma:E+:R16-` | no |
| 9 | `kerGamma:E+:L16+` | `(2,1,16+)` | 32 | 1 | `kerGamma:E-:L16-` | yes |
| 10 | `kerGamma:E+:R16-` | `(1,2,16-)` | 32 | 1 | `kerGamma:E-:R16+` | yes |
| 11 | `kerGamma:E-:L16-` | `(2,1,16-)` | 32 | 1 | `kerGamma:E+:L16+` | yes |
| 12 | `kerGamma:E-:R16+` | `(1,2,16+)` | 32 | 1 | `kerGamma:E+:R16-` | yes |
| 13 | `X:X32p` | `(3,2,16+)` | 96 | 1 | `X:X32m` | yes |
| 14 | `X:X23m` | `(2,3,16-)` | 96 | 1 | `X:X23p` | yes |
| 15 | `X:X2Tp` | `(2,1,144+)` | 288 | 1 | `X:X2Tm` | yes |
| 16 | `X:X1Tm` | `(1,2,144-)` | 288 | 1 | `X:X1Tp` | yes |
| 17 | `X:X32m` | `(3,2,16-)` | 96 | 1 | `X:X32p` | yes |
| 18 | `X:X23p` | `(2,3,16+)` | 96 | 1 | `X:X23m` | yes |
| 19 | `X:X2Tm` | `(2,1,144-)` | 288 | 1 | `X:X2Tp` | yes |
| 20 | `X:X1Tp` | `(1,2,144+)` | 288 | 1 | `X:X1Tm` | yes |

The exact closures are

\[
\dim_{\mathbb C}(S,I,R)=(128,128,1664),
\qquad
\dim_{\mathbb C}\mathcal E=1920.
\]

The eight `X` slots are eight irreducibles arranged in four mirror pairs.
They are not four aggregated slots. Their displayed \(16_\pm,144_\pm\)
labels type their \(\operatorname{Spin}(10)\) chirality; no extra `E+` or
`E-` label is invented for them.

## The finite carrier ansatz

Let \(V=T^*Y\) be the actual 14-dimensional gimmel cotangent carrier. On the
program-native branch its vertical ten comes from
\(\operatorname{Sym}^2T^*X\), not
\(\Lambda^2T^*X\oplus\Lambda^3T^*X\).

At complex algebraic grade define

\[
\Gamma^\sharp_g(s)=\sum_a e^a\otimes c(e_a)s,
\qquad
\Gamma\Gamma^\sharp_g=14\,1_S,
\]

\[
j=\frac1{14}\Gamma^\sharp_g:S\longrightarrow I,
\qquad
P_I=j\Gamma,
\qquad
P_R=1-P_I.
\]

This is the intrinsic metric/Clifford splitting. It is not a claim about the
still-open physical Krein formal adjoint.

For a fixed metric-compatible background connection \(A\), set

\[
D_S=c^A\nabla_A^S,
\qquad
D_V=1_V\otimes c^A\nabla_A^{V\otimes S},
\]

\[
T=P_R\nabla_A:S\longrightarrow R,
\qquad
\delta_R=-\operatorname{tr}_g\nabla_A:R\longrightarrow S.
\]

Rows are targets and columns are sources in \(S\oplus I\oplus R\):

\[
\boxed{
D_{\mathbf c}=
\begin{pmatrix}
aD_S
&b_{SI}D_S\Gamma_I
&b_{SR}\delta_R\\
b_{IS}jD_S
&dP_ID_VP_I
&b_{IR}P_ID_VP_R\\
b_{RS}T
&b_{RI}P_RD_VP_I
&P_RD_VP_R+\mu_0P_R
\end{pmatrix}.
}
\]

This formula supplies one natural operator for every coarse
\(S/I/R\) source-target block. Expanding only its **typing envelope**
against the independent representation ledger mentions all nine coarse
sector pairs and therefore the 136 allowed ordered cells. This is
formula-blind envelope bookkeeping, not a support computation. It does not
prove that \(T,\delta_R,P_ID_VP_R,\ldots\) are nonzero on every compatible
irrep, nor that every observer slot has actual action incidence. The
formula-level irrep support and linked coefficient pattern are the next
computation.

The W131 principal block is normalized to one and inherited:

\[
\pi_R D_{\mathbf c}\iota_R
=P_RD_VP_R+\mu_0P_R.
\]

The presence of the lower-order scalar is inherited from W131; its value
\(\mu_0=m^2\) is open and remains a posit. It is not a physical mass
eigenvalue.

## Candidate linear gauge generator

Take one explicitly charged observer-spinor ghost bundle

\[
\mathcal G=\Omega^0(Y,S).
\]

The shortest natural candidate is

\[
R_{\mathbf r}c
=
\left(
r_SD_Sc,\;
r_IjD_Sc,\;
r_RT c
\right)
:
\mathcal G\longrightarrow S\oplus I\oplus R.
\]

This is a finite posit, not a source-derived gauge law. In particular, the
finite-fibre control
\(P_Rd_A\) is not imported as the answer, and no non-equivariant
compensator is selected from a desired four-orbit bridge. Swing 2 must expand
this generator, compute the Noether defect, and let that defect type any
needed compensator.

## The relative quadratic BV ansatz

Let

\[
\kappa_{K,\mu}:\mathcal E\longrightarrow\mathcal E^\vee_{\rm dens}
\]

be the conjugate-linear density/Krein lowering map, still phase-parametric
at native grade.
Define the bilinear kernel

\[
B_{\mathbf c}(Z_1,Z_2)
=\operatorname{ev}
\left(\kappa_{K,\mu}D_{\mathbf c}Z_2,Z_1\right).
\]

The action ansatz is

\[
\boxed{
\begin{aligned}
S_{\rm rel}^{(2)}[-;A]
={}&
\frac12\operatorname{Re}\!\int_Y B_{\mathbf c}(Z,Z)\\
&+\operatorname{Re}\!\int_Y
\operatorname{ev}\left(Z^+,R_{\mathbf r}c\right)\\
&+\operatorname{Re}\!\int_Y
\operatorname{ev}\left(\bar c^+,b\right).
\end{aligned}
}
\]

The first line is a real quadratic **ansatz**. Its variational operator is
the graded polarization

\[
H_{\mathbf c}
=\mathsf{Pol}_{K,\rm gr}
\left(\kappa_{K,\mu}D_{\mathbf c}\right),
\]

not automatically the unsymmetrized
\(\kappa_{K,\mu}D_{\mathbf c}\). This is where composing the Krein pairing
matters. The native pairing phases, formal-adjoint sign, Green form, and
common domain decide the exact relation.

There is no \(c^+\) monomial at this abelianized quadratic grade. A
Faddeev--Popov kinetic term would require a gauge-fixing fermion and a typed
gauge condition, neither of which is supplied in S1.

## Declared one-stage fixed-\(A\) observer BV census

The chosen graded base is

\[
\mathcal E\oplus\mathcal G[1]
\oplus\bar{\mathcal G}[-1]\oplus\bar{\mathcal G}[0],
\]

and the ansatz is its shifted cotangent

\[
\mathcal F_{\rm BV,rel}
=T^*[-1]\!\left(
\mathcal E\oplus\mathcal G[1]
\oplus\bar{\mathcal G}[-1]\oplus\bar{\mathcal G}[0]
\right).
\]

Thus the individual antifield shifts follow their base ghost numbers:
\(Z^+\) has ghost number \(-1\), \(c^+\) has \(-2\),
\(\bar c^+\) has \(0\), and \(b^+\) has \(-1\). The table's `afn`
uses the usual minimal values for \(Z^+,c^+\) and a declared bookkeeping
value one for the two nonminimal shifted-cotangent coordinates. The separate
cotangent flag is zero for base coordinates and one for every \(+\)
coordinate.

| coordinate | bundle | form | gh | afn | parity | irreps | rank |
| --- | --- | ---: | ---: | ---: | --- | ---: | ---: |
| \(Z\) | \(\mathcal E\) | `0/1` | 0 | 0 | odd | 20 | 1920 |
| \(Z^+\) | \(\mathcal E^\vee_{\rm dens}\), ghost shift `-1` | `14/13` | -1 | 1 | even | 20 | 1920 |
| \(c\) | \(\mathcal G\) | 0 | +1 | 0 | even | 4 | 128 |
| \(c^+\) | \(\mathcal G^\vee_{\rm dens}\), ghost shift `-2` | 14 | -2 | 2 | odd | 4 | 128 |
| \(\bar c\) | \(\bar{\mathcal G}\) | 0 | -1 | 0 | even | 4 | 128 |
| \(\bar c^+\) | \(\bar{\mathcal G}^\vee_{\rm dens}\), ghost shift `0` | 14 | 0 | 1 | odd | 4 | 128 |
| \(b\) | \(\bar{\mathcal G}\) | 0 | 0 | 0 | odd | 4 | 128 |
| \(b^+\) | \(\bar{\mathcal G}^\vee_{\rm dens}\), ghost shift `-1` | 14 | -1 | 1 | even | 4 | 128 |

Thus

\[
\operatorname{rk}_{\mathbb C}\mathcal F_{\rm BV,rel}
=2(1920)+6(128)=4608.
\]

On the underlying real Hamiltonian space,

\[
\operatorname{rk}_{\mathbb R}\mathcal F_{\rm BV,rel,\mathbb R}=9216.
\]

The chosen minimal-part census before the nonminimal quartet has complex rank

\[
2(1920)+2(128)=4096.
\]

The commuting parity of \(c\) is deliberate: the candidate gauge parameter
for an odd observer fermion is odd, so its BRST ghost is even. The
nonminimal choice is one self-dual copy
\(\bar{\mathcal G}=\mathcal G\), charged as a posit rather than a hidden
extra family.

Every canonical pair has:

\[
\deg_{\rm form}(u)+\deg_{\rm form}(u^+)=14,
\]

\[
\operatorname{gh}(u)+\operatorname{gh}(u^+)=-1,
\]

and opposite Grassmann parity.

## Odd symplectic form and Hamiltonian vector field

The odd symplectic form is

\[
\omega_{\rm BV}
=\operatorname{Re}\!\int_Y
\left(
\delta Z^+\delta Z
+\delta c^+\delta c
+\delta\bar c^+\delta\bar c
+\delta b^+\delta b
\right),
\]

with the usual Koszul signs and canonical density evaluation.
It is a real odd symplectic form on
\(\mathcal F_{\rm BV,rel,\mathbb R}\).

It defines

\[
Q_{\rm BV}=(S_{\rm rel}^{(2)},-)_{\rm BV}.
\]

Up to the overall sign convention for the antibracket, the typed incidence is

\[
\begin{aligned}
QZ&=R_{\mathbf r}c,&
Qc&=0,&
Q\bar c&=b,&
Qb&=0,\\
QZ^+&=H_{\mathbf c}Z,&
Qc^+&=-R_{\mathbf r}^{!}Z^+,&
Q\bar c^+&=0,&
Qb^+&=-\bar c^+.
\end{aligned}
\]

This gives an explicit family-level Hamiltonian arrow for all eight
coordinate families. Formula-level incidence on every irreducible coordinate
still depends on the uncomputed support of \(R_{\mathbf r}\) and
\(H_{\mathbf c}\). No origin-free dummy pair is added; the one nonminimal
contractible quartet is declared explicitly.

Nilpotency is not automatic. The quadratic master equation asks, among other
graded-transpose relations, for

\[
H_{\mathbf c}R_{\mathbf r}=0,
\qquad
R_{\mathbf r}^{!}H_{\mathbf c}=0.
\]

Those are Swing-3 equations after the native adjoint packet and actual
irrep-level support are frozen.

## The rolled-differential correction

### Exact \(\mathbb Z_2\) coloring of the full allowed envelope

The maximal 136-cell **allowed** graph is connected and bipartite. One of
its two globally reversed colorings is:

\[
\begin{aligned}
\mathcal E_{\bar0}=\{&
\texttt{S:E+:L16+},
\texttt{S:E+:R16-},
\texttt{imGamma:E+:L16+},
\texttt{imGamma:E+:R16-},\\
&
\texttt{kerGamma:E+:L16+},
\texttt{kerGamma:E+:R16-},
\texttt{X:X32m},
\texttt{X:X23p},
\texttt{X:X2Tm},
\texttt{X:X1Tp}
\},
\end{aligned}
\]

with \(\mathcal E_{\bar1}\) its ten-slot complement. Both have complex rank
\(960\), and mirror exchange swaps them.

Over \(\mathbb F_2\), the edge equations

\[
\epsilon_j-\epsilon_i=1
\]

have matrix rank \(19\) and nullity \(1\). Fixing one slot's color removes
that nullity. Therefore the maximal envelope has a unique symbol parity up
to one global reversal. The reversal is a grading convention, not an exposed
physical datum. A smaller actual nonzero support can admit additional
colorings.

This is an observer-symbol statement. Identifying it with the author's
rolled de Rham/BV grading still requires the roll maps below.

### Why the whole bidirectional envelope has no one-copy integer lift

If every cell of the maximal envelope is placed in one integer
degree-\(+1\) endomorphism, every directed cell \(i\to j\) requires

\[
f_j-f_i=1.
\]

The frozen support is symmetric: \(j\to i\) is also present. That requires

\[
f_i-f_j=1,
\]

which is inconsistent. Thus the whole 136-cell bidirectional envelope cannot
be one integer degree-\(+1\) endomorphism of \(\mathcal E_{20}\).
A sparse/oriented proper sub-support remains possible, with transpose cells
allowed to live in \(q^\times\) instead of \(q\).

The W131 split gives a second control. Its first-order principal support is
odd for the maximal-envelope coloring, while its scalar identity term
\(\mu_0P_R\) is even. W131 can be a kinetic Euler block, but the complete
massive W131 operator cannot be renamed a homogeneous \(q_{\rm B5}\).

### Source-shaped four-stage candidate

The source-shaped candidate carrier is

\[
\mathcal U^0=S,
\qquad
U^0=\Gamma(Y,\mathcal U^0)=\Omega^0(Y,S),
\qquad \operatorname{rk}_{\mathbb C}\mathcal U^0=128,
\]

\[
\mathcal U^1=I\oplus R=T^*Y\otimes S,
\qquad
U^1=\Gamma(Y,\mathcal U^1)=\Omega^1(Y,S),
\qquad \operatorname{rk}_{\mathbb C}\mathcal U^1=1792,
\]

\[
\mathcal U^2=(I\oplus R)^\vee_{\rm dens}
\cong\Lambda^{13}T^*Y\otimes S^\vee,
\qquad
U^2=\Gamma(Y,\mathcal U^2),
\qquad \operatorname{rk}_{\mathbb C}\mathcal U^2=1792,
\]

\[
\mathcal U^3=S^\vee_{\rm dens}
\cong\Lambda^{14}T^*Y\otimes S^\vee,
\qquad
U^3=\Gamma(Y,\mathcal U^3),
\qquad \operatorname{rk}_{\mathbb C}\mathcal U^3=128.
\]

A future integer cochain differential would have type

\[
q_U^k:U^k\longrightarrow U^{k+1}.
\]

No such map or square-zero identity is constructed in S1. The candidate
parity fold gives

\[
U^{\rm even}=U^0\oplus U^2,
\qquad
U^{\rm odd}=U^1\oplus U^3,
\]

with complex rank \(1920\) on each side. To rewrite the high-form pieces as
the normalized low-form observer bundles requires at least

\[
\rho_{13}:U^2\longrightarrow I\oplus R,
\qquad
\rho_{14}:U^3\longrightarrow S,
\]

together with their Hodge/Krein phases, real structure, and domain
compatibility. These are not supplied by \(\pi\iota=1\).

Indeed, the coordinate maps

\[
\iota_0:\mathcal E\hookrightarrow\mathcal F_{\rm BV,rel},
\qquad
\pi_0:\mathcal F_{\rm BV,rel}\twoheadrightarrow\mathcal E,
\qquad
\pi_0\iota_0=1
\]

are canonical but vacuous for rolling. At zero antifields,
\(Q_{\rm BV}\) sends the quadratic equation into an antifield direction, so
the naïve field-coordinate compression does not produce a nonzero
\(q_{\rm B5}\). A nontrivial relation

\[
q_{\rm B5}=\pi_{\rm roll}Q_{\rm BV}\iota_{\rm roll}
\]

needs a filtered graph embedding that mixes the low/high and field/antifield
stages. Constructing and intertwining that graph is later work.

## Coefficient and choice ledger

### Canonical at the stated complex/fixed-background grade

- \(\Gamma\), its intrinsic metric/Clifford injection
  \(\Gamma^\sharp_g\), \(j=(1/14)\Gamma^\sharp_g\), \(P_I\), and \(P_R\);
- the natural operator types \(D_S,D_V,T,\delta_R\);
- ordinary density duals and evaluation;
- BV shifts, canonical partner pairings, ghost numbers, and parities;
- the coordinate inclusion/projection; and
- normalization of the contractible
  \(\operatorname{ev}(\bar c^+,b)\) term by field rescaling.

### Inherited

- the exact 20-slot/1920-dimensional observer decomposition;
- the exact 12-slot/1664-dimensional W131 carrier;
- the W131 projected principal block; and
- the existence, but not the physical spectral meaning, of its scalar
  lower-order slot.

### Continuous coefficient posits

\[
\left(
a,b_{SI},b_{SR},b_{IS},d,b_{IR},b_{RS},b_{RI},
\mu_0,r_S,r_I,r_R
\right)\in\mathbb C^{12}
\]

at raw complex grade.

No reality, adjoint, or field-redefinition quotient has yet been imposed, so
this is not a physical parameter count. Constraint surplus is deferred until
those equations and quotient dimensions are computed.

### Additional charged choices/open packets

- the candidate gauge-parameter bundle \(\mathcal G=S\);
- the chosen self-dual nonminimal copy
  \(\bar{\mathcal G}=\mathcal G\);
- the five native fields:
  slot-pairing phases, coflip type/phases, formal-adjoint sign, Green form,
  and common closed domain;
- the roll maps \(\rho_{13},\rho_{14}\) and their compatibility;
- whether \(A\) is fixed background data, an ordinary IG gauge field, or part
  of a larger affine gauge redundancy; and
- any compensator basis generated by the future Noether defect.

## Held-out wall

The coefficient/map manifest was written under the preregistered wall before
any downstream target was evaluated. The executable packet also performs an
API-fence smoke test by perturbing:

- P1 and its endpoint sign;
- P2;
- P3 and target count;
- the desired `3E+` versus `3E-` retract; and
- the later four-orbit witness.

The hash is unchanged because the API rejects those inputs. This is a useful
regression guard, not independent evidence that the human-written manifest
was never target-shaped. The preregistration, source/provenance restriction,
and explicit coefficient inventory carry that evidentiary burden.

## Planted controls

The probe passes the following hostile controls:

| control | required response |
| --- | --- |
| aggregate eight `X` irreps into four mirror-pair labels | fail exact 20-label census |
| identify `S` with `imGamma` | fail provenance injectivity |
| omit `X` | return 12 slots / rank 384, not the carrier |
| put `beta` in the principal carrier | reject |
| use density-valued \(H_{\mathbf c}\) inside a carrier \(K\)-pairing | reject |
| compare W131 endomorphism directly with a density-dual projector sandwich | reject |
| import complex support as native phase/domain data | reject all five fields |
| keep only the W131 block | reproduce the 40-cell coarse envelope but leave eight observer slots unmentioned |
| omit the antighost/NL quartet | fail the declared one-stage manifest |
| add a generator outside the exact family/origin manifest | reject |
| apply the 136-cell census to ghosts/antifields | reject |
| infer rolling from \(\pi_0\iota_0=1\) | compression remains zero |
| force every filtration test to return one | planted normalized systems return 0, 1, and 2 |
| identify ordinary form degree with cochain degree | reject via the `0,1,13,14` versus `0,1,2,3` ledger |
| use the exterior `6+4` numerical ten | fail the symmetric-fibre/diagonal typing control |
| treat Hermitian Krein lowering as complex-linear | reject; realify or use conjugate bundles |
| simplify W131 lowering without Krein-orthogonal restriction | reject |
| change P1/P2/P3/retract target | API-fence smoke hash remains invariant |

## What moved

- A finite coarse \(S/I/R\) natural-map action ansatz is typed on the full
  20-slot carrier.
- W131 is embedded with a type-correct carrier restriction; its simplified
  equation lowering is explicitly conditional on Krein orthogonality and
  the native adjoint packet.
- The declared one-stage fixed-\(A\) observer BV ansatz is exact:
  64 complex irreducible coordinates, complex rank \(4608\), and underlying
  real rank \(9216\).
- Every coefficient and nonminimal choice is individually charged.
- The maximal allowed symbol envelope now has an exact parity certificate:
  rank \(19\), nullity one before global normalization, and nullity zero
  after.
- The whole bidirectional 136-cell envelope is excluded as one homogeneous
  degree-\(+1\) endomorphism; sparse/oriented one-copy supports remain open.
- The source-shaped four-stage candidate carrier is correctly typed with
  exact ranks, while its differential remains unbuilt.
- The next missing datum is no longer an unnamed "filtration": it is an
  explicit Hodge/Krein high-to-low roll packet plus the native adjoint data.

## What did not move

- No coefficient is solved or preferred.
- No actual irrep-level nonzero support graph is claimed.
- The four-orbit connectivity lower bound is not discharged.
- No compensator is selected.
- No master equation, Noether identity, or nilpotency is proved.
- No deformation retract, B5 cohomology, physical index, or family count is
  obtained.
- No P1, P2, or P3 datum is consumed.
- No stationary background or physical mass exists.
- No source-action requirement, canon verdict, or public posture changes.

## Efficient next swing

The campaign should insert one short bridge before attempting the full
coefficient solve:

1. expand the nine carrier maps and three gauge maps representation by
   representation, compute their actual nonzero symbol support, and apply the
   four-orbit/all-slot coverage kill;
2. compute the resulting Noether defect and let it type any non-equivariant
   compensator rather than choosing one from the desired support;
3. derive the Krein-orthogonality and graded variational-polarization
   conditions, then derive or exhaust finite candidates for
   \(\rho_{13}\) and \(\rho_{14}\) with all five native fields symbolic; and
4. decide the ordinary-IG versus affine/full-ambient gauge semantic fork
   before promoting the chosen one-stage census to a full BV claim.

That sequence preserves the construction target while preventing the next
master-equation solve from operating on a mistyped roll or an ambiguous
gauge bundle.
