# Actual-\(\operatorname{Sym}^2\), \(C_{14}\), odd-kernel, and orbit knockout

**Date:** 2026-07-30
**Run:** N2a only
**Frozen N1 executable construction hash:**
`1efdffd34e3ad5358fed16c08cda9ecf681df676e817560bf36b436d79658ffb`
**Executable certificate:**
`tests/channel-swings/actual_sym2_c14_orbit_probe.py`

## Result first

N2a does not knock out the \(C\)-complex branch. It constructs two explicit
native charge-conjugation components on the repo's \(128\)-complex-dimensional
\(\operatorname{Cl}(9,5)\) module:

\[
(\varepsilon_C,\tau_C)=(-1,+1),
\qquad
(\varepsilon_C,\tau_C)=(+1,-1).
\]

Here “native” means the signed-Jordan--Wigner representative of the same
\(\operatorname{Cl}(9,5)\) algebra. The probe verifies similarity covariance,
but it does not construct the still-missing intertwiner placing these matrices
on every factorized \(4+10\), full-\(20\) carrier slot.

For both components and every real vertical covector \(\alpha\),

\[
\bigl(C_{\varepsilon_C}\Gamma(\alpha)\bigr)^T
=-C_{\varepsilon_C}\Gamma(\alpha).
\]

That is a result about the **bare spinor kernel**. It is not yet the
Grassmann verdict for the N1 action. The latter belongs to the total restricted
spinor-times-gauge-times-provenance kernel

\[
\mathcal M_C
\sim
P_0^T
\left[
  C_{\varepsilon_C}\Gamma(\alpha_h)
  \otimes \rho(\Phi)
  \otimes Y_C
\right]
P_0,
\]

with the displayed tensor factorization only schematic until the actual
placement maps are supplied. \(P_0\), \(\rho(\Phi)\), and the relevant
provenance contraction are not explicit matrices in the frozen packet.
Consequently:

- the two \(C\)-components **survive the native spinor-algebra knockout**;
- identical-odd-field survival of the complete N1 term is
  **typed unresolved**;
- neither a survival nor a cancellation may be inferred from
  \(C\Gamma(\alpha_h)\) alone.

The separate \(K\)-sesquilinear branch also survives its bare algebraic screen:
\(K\Gamma(\alpha_h)\) is Hermitian for all four representatives and is nonzero
for all three nonzero ones. No result is transferred between the \(K\) and
\(C\) branches because N1 supplies no \(\mathcal R_{KC}\).

The actual-\(\operatorname{Sym}^2\) geometric screen discriminates:

| representative | chosen normalization | \(\operatorname{tr}_g h\) | \(G_{\rm DW}(h,h)\) | \(\operatorname{rank}\Gamma(\alpha_h)\) | fixed \(SO(3,1)\) stabilizer dim. | \(SO(6,4)\) vector stabilizer dim. |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| zero | \(0\) | \(0\) | \(0\) | \(0\) | \(6\) | \(45\) |
| trace | \(-g/4\) | \(-1\) | \(-1/4\) | \(128\) | \(6\) | \(36\) |
| spacelike traceless | \(\operatorname{diag}(1,-1,0,0)/\sqrt2\) | \(0\) | \(+1\) | \(128\) | \(1\) | \(36\) |
| null | \(h_{\rm sp}-g/2\) | \(-2\) | \(0\) | \(64\) | \(1\) | \(36\) |

The null insertion is nonzero, square-zero, and rank \(64\). Thus
“DeWitt-null” is not “absent.”

Only zero and trace preserve the full fixed-background Lorentz group under the
actual \(\operatorname{Sym}^2\) action. Spacelike-traceless and null preserve a
one-dimensional subgroup for the representatives chosen here. This does not
break covariance of the **dynamical** \(h\)-contracted term: the probe
constructs the induced

\[
\mathfrak{so}(3,1)\longrightarrow\mathfrak{so}(6,4)
\longrightarrow\operatorname{End}(S_{\mathbb C})
\]

lift and verifies infinitesimal covariance for every generator and all four
representatives. It says only that freezing a non-invariant \(h\) reduces the
background stabilizer.

No mass, stationary point, physical gauge group, exhaustive orbit
classification, anomaly, index, or count follows.

## 1. Layer-0 object ledger

This screen runs Layer 0 before its algebra. The following objects are kept
distinct.

| word at risk | object used here | object not identified with it |
| --- | --- | --- |
| vertical datum | \(h\in\operatorname{Sym}^2T^*X\) followed by its DeWitt musical \(\alpha_h\in(\operatorname{Sym}^2T^*X)^*\) | Frobenius identification of \(h\) with a covector; an exterior \(6+4\) ten |
| Clifford insertion | \(\Gamma(\alpha_h)\) on the native \(128\)-component spinor factor | the complete \(\mathfrak c_\rho(v_s)\) on the restricted \(E_{20}\) carrier |
| complex odd kernel | \(C\Gamma(\alpha_h)\) | \(P_0^T[C\Gamma(\alpha_h)\otimes\rho(\Phi)\otimes Y_C]P_0\) |
| \(K\) kernel | \(\psi^\dagger K\Gamma(\alpha_h)Y_K\psi\) | the \(C\)-complex bilinear \(\psi^TC\Gamma(\alpha_h)Y_C\psi\) |
| covariance | simultaneous transformation of \(h\), the spinor, and the insertion | invariance after a particular \(h\) is held fixed |
| scalar | invariant trace direction under Lorentz-on-\(\operatorname{Sym}^2\) | a component of the observer-fork \((1,10)\) scalar multiplet |
| support | complexified first-order observer-symbol cell | nonzero zero-order matrix element of \(\mathfrak c_\rho(v_s)\) |
| rank/count | matrix rank of one Clifford insertion | chiral index, generations, retained modes, or physical states |
| orbit screen | four preregistered representatives | exhaustive Lorentzian Segre/Jordan classification |

The construction and the tests below all refer to the left-hand objects.

## 2. Frozen input and fork discipline

The test invokes the N1 hash emitter and refuses to proceed silently against a
different construction. The ordinary Markdown file hash is not substituted for
the executable construction hash.

The native column of this investigation is:

- the actual metric fibre
  \(\operatorname{Sym}^2T^*X\);
- the signed-Jordan--Wigner \(128\times128\)
  \(\operatorname{Cl}(9,5)\) representation already used by the repo;
- the indefinite Spin-invariant Krein matrix \(K\);
- the geometric Lorentz action on \(\operatorname{Sym}^2T^*X\);
- the native gauge typing \(Sp(32,32;\mathbb H)\).

The following remain comparators and do not receive native conclusions:

- \(\Lambda^2T^*X\oplus\Lambda^3T^*X\), the exterior “ten”;
- a \(U(128)\) gauge reading;
- a positive-definite Hilbert replacement for \(K\);
- a ghost-subtracted Rarita--Schwinger carrier.

The \(R\)-curvature question is not used in N2a. Where \(R\) is mentioned by
neighbouring work, its geometric typing remains native and a physics
reinterpretation requires a separate Layer-0 map.

Every disposition below is fork-scoped.

## 3. The required DeWitt musical

At a reference Lorentz metric

\[
\eta=\operatorname{diag}(1,1,1,-1),
\]

the DeWitt form used in the probe is

\[
G_{\rm DW}(h,k)
=
\operatorname{tr}(\eta h\,\eta k)
-\frac12
\operatorname{tr}(\eta h)
\operatorname{tr}(\eta k).
\]

The Clifford input is the covector

\[
\alpha_h(k)=G_{\rm DW}(h,k).
\]

If that covector is displayed using the ordinary Frobenius pairing
\(\alpha_h(k)=\operatorname{tr}(q_h^Tk)\), its matrix is

\[
q_h
=
\eta h\eta
-\frac12\operatorname{tr}(\eta h)\eta.
\]

That trace reversal is essential. Feeding \(h\) itself into the covector slot
is a different map.

The probe builds an explicit DeWitt-orthonormal frame
\(\{f_i\}_{i=1}^{10}\) with signature

\[
\eta_{10}=\operatorname{diag}(+1^6,-1^4)
\]

and uses the dual-frame coefficients

\[
\alpha_i=G_{\rm DW}(h,f_i),
\qquad
\Gamma(\alpha_h)=\sum_{i=1}^{10}\alpha_i\gamma_i^\perp .
\]

It verifies

\[
\Gamma(\alpha_h)^2
=G_{\rm DW}(h,h)\mathbf1_{128}.
\]

The trace normalization is chosen to meet N1 exactly:

\[
h_{\rm tr}=-\frac14g,
\qquad
G_{\rm DW}(h_{\rm tr},k)
=\frac14\operatorname{tr}_g(k)
=\tau_g(k).
\]

Thus the geometric trace vector is the DeWitt inverse of N1's trace covector;
it is not merely a matrix with nonzero trace.

### Hostile wrong-musical control

For both the trace and null representatives, the probe plants a generic
symmetric \(k\) and checks

\[
\operatorname{tr}(q_h^Tk)=G_{\rm DW}(h,k)
\]

while

\[
\operatorname{tr}(h^Tk)\ne G_{\rm DW}(h,k).
\]

The control would fail if the calculation silently reverted to Frobenius
identification.

## 4. Explicit native \(C\)-solutions

Let \(e_0,\ldots,e_{13}\) be the repo's signed-Jordan--Wigner generators in
their native order, with nine positive and five negative squares. In this
basis,

\[
e_a^T=(-1)^ae_a.
\]

There are seven transpose-symmetric and seven transpose-skew generators. Define

\[
P_{\rm skew}=e_1e_3e_5e_7e_9e_{11}e_{13},
\qquad
P_{\rm sym}=e_0e_2e_4e_6e_8e_{10}e_{12},
\]

and

\[
C_-=P_{\rm skew}^{-1},
\qquad
C_+=P_{\rm sym}^{-1}.
\]

Direct \(128\times128\) evaluation gives

\[
\begin{array}{c|cc}
 & \varepsilon_C & \tau_C\\
\hline
C_- & -1 & +1\\
C_+ & +1 & -1
\end{array}
\]

in N1's convention

\[
C\gamma_aC^{-1}=\varepsilon_C\gamma_a^T,
\qquad
C^T=\tau_CC.
\]

For a one-form Clifford insertion,

\[
\bigl(C\Gamma(\alpha)\bigr)^T
=\varepsilon_C\tau_C\,C\Gamma(\alpha).
\]

Both constructed components have
\(\varepsilon_C\tau_C=-1\), so both bare kernels are skew.

### Similarity-covariance control

This result is not an artefact of the displayed Jordan--Wigner coordinates.
For a deterministic non-unitary similarity \(S\), the probe transforms

\[
\gamma'_a=S\gamma_aS^{-1},
\qquad
C'=S^{-T}CS^{-1},
\qquad
K'=S^{-\dagger}KS^{-1}.
\]

It then rechecks:

\[
C'\gamma'_aC'^{-1}
=\varepsilon_C(\gamma'_a)^T,
\qquad
(C')^T=\tau_CC',
\]

and the congruences

\[
C'\Gamma'(\alpha)
=S^{-T}[C\Gamma(\alpha)]S^{-1},
\]

\[
K'\Gamma'(\alpha)
=S^{-\dagger}[K\Gamma(\alpha)]S^{-1}.
\]

All pass.

## 5. Grassmann exchange: what is computed and what is not

For odd fields and an ordinary complex matrix \(M\),

\[
B_M(\chi,\psi)=\chi^TM\psi
\quad\Longrightarrow\quad
B_M(\chi,\psi)=-B_{M^T}(\psi,\chi).
\]

Therefore:

- \(M^T=-M\) makes the exchange symmetric and permits an identical-field
  diagonal;
- \(M^T=+M\) makes the exchange antisymmetric and kills an identical-field
  diagonal.

The constructed bare spinor factor
\(A=C\Gamma(\alpha_h)\) is skew. If a factorizable remaining
gauge/provenance kernel is \(B\), then

\[
\frac12\left[A\otimes B-(A\otimes B)^T\right]
=A\otimes\frac{B+B^T}{2}.
\]

Only the transpose-symmetric part of the remaining factor contributes to the
identical-odd-field diagonal. The probe includes three hostile controls:

1. a symmetric planted gauge/provenance factor leaves the total kernel skew
   and nonzero;
2. a skew planted factor makes the total kernel symmetric and cancels the
   identical-field diagonal;
3. a planted one-dimensional \(P_0\) restriction annihilates an otherwise
   surviving skew form.

All three pass. This is why the bare \(C\Gamma\) sign cannot decide the N1
term.

### N2a disposition of the \(C\)-branch

**CONSTRUCTED**

- two nonempty components of
  \(\mathcal C_{\varepsilon_C,\tau_C}\);
- bare spinor exchange sign for both;
- representative-dependent Clifford rank;
- covariance under native spinor-basis similarity.

**UNRESOLVED-NEEDS-TOTAL-KERNEL**

- the explicit \(P_0\) embedding/restriction on the defect fermion;
- matrices for the relevant \(\rho(\Phi_\alpha)\);
- the actual transpose/reality condition on \(Y_C\);
- ordering and placement of these factors on \(E_{20}\);
- the reality-completion map in the chosen \(C\)-component.

No \(C\)-component is killed before those maps exist.

## 6. The separate \(K\)-sesquilinear branch

The native Krein matrix is

\[
K=\prod_{\gamma_a^2=+1}\gamma_a .
\]

The probe verifies

\[
K^\dagger=K,
\qquad
\Sigma^\dagger K+K\Sigma=0
\]

for all \(91\) native \(\mathfrak{spin}(9,5)\) generators.

For every real \(\alpha_h\) in the four-representative screen,

\[
[K\Gamma(\alpha_h)]^\dagger
=K\Gamma(\alpha_h).
\]

The matrix ranks are the Clifford ranks in the result table. This establishes
a nonzero bare sesquilinear channel for trace, spacelike-traceless, and null.
It does not establish that the full

\[
P_0^\dagger
[K\Gamma(\alpha_h)\otimes\rho(\Phi)\otimes Y_K]
P_0
\]

is nonzero, gauge invariant, or selected by a stationary solution.

The transpose calculation in Section 5 does not transfer to this branch:
\(\psi^\dagger H\psi\) is sesquilinear, while \(\psi^TM\psi\) is complex
bilinear. No \(\mathcal R_{KC}\) has been constructed.

## 7. Four actual-\(\operatorname{Sym}^2\) representatives

The representatives are a preregistered screen, not a classification.

### 7.1 Zero

\[
h_0=0,
\qquad
\alpha_{h_0}=0,
\qquad
\Gamma(\alpha_{h_0})=0.
\]

This kills the bare vertical insertion in both bilinear branches. It does not
kill the rest of the source action.

Stabilizers:

- Lorentz-on-\(\operatorname{Sym}^2\): all of \(SO(3,1)\), dimension \(6\);
- fibre-frame: all of \(SO(6,4)\), dimension \(45\);
- full gauge: all of the native gauge group as far as this zero insertion is
  concerned.

### 7.2 Trace

\[
h_{\rm tr}=-\frac14\eta,
\qquad
G_{\rm DW}(h_{\rm tr},h_{\rm tr})=-\frac14.
\]

This is the DeWitt inverse of the N1 functional \(\tau_g\).
\(\Gamma(\alpha_{h_{\rm tr}})\) is invertible of rank \(128\).

Stabilizers:

- Lorentz-on-\(\operatorname{Sym}^2\): all of \(SO(3,1)\), dimension \(6\);
- fibre-frame: the negative-vector stabilizer \(SO(6,3)\), dimension \(36\);
- full gauge: unresolved without \(\Phi_{\rm tr}\) and \(\rho\).

### 7.3 Spacelike traceless

\[
h_{\rm sp}
=\frac1{\sqrt2}\operatorname{diag}(1,-1,0,0),
\qquad
G_{\rm DW}(h_{\rm sp},h_{\rm sp})=+1.
\]

\(\Gamma(\alpha_{h_{\rm sp}})\) is invertible of rank \(128\).

Stabilizers:

- Lorentz-on-\(\operatorname{Sym}^2\): dimension \(1\), an
  \(\mathfrak{so}(1,1)\)-type stabilizer for this diagonal representative;
- fibre-frame: the positive-vector stabilizer \(SO(5,4)\), dimension \(36\);
- full gauge: unresolved.

### 7.4 Null

\[
h_{\rm null}=h_{\rm sp}-\frac12\eta,
\qquad
G_{\rm DW}(h_{\rm null},h_{\rm null})=0.
\]

Nevertheless,

\[
\Gamma(\alpha_{h_{\rm null}})\ne0,
\qquad
\Gamma(\alpha_{h_{\rm null}})^2=0,
\qquad
\operatorname{rank}\Gamma(\alpha_{h_{\rm null}})=64.
\]

Stabilizers:

- Lorentz-on-\(\operatorname{Sym}^2\): dimension \(1\), again
  \(\mathfrak{so}(1,1)\)-type for this chosen representative;
- fibre-frame fixed-null-vector stabilizer:
  \(SO(5,3)\ltimes\mathbb R^8\), dimension \(36\);
- full gauge: unresolved.

The dimension-\(36\) group fixes the null **vector**. The null-line stabilizer
would include one additional dilation and has dimension \(37\); it is not the
object reported here.

## 8. Dynamic covariance versus fixed-background invariance

For \(X\in\mathfrak{so}(3,1)\), the actual symmetric tensor varies as

\[
\delta_Xh=X^Th+hX.
\]

In the DeWitt frame this gives a computed matrix

\[
R_X\in\mathfrak{so}(6,4).
\]

The probe constructs its spin lift

\[
\widehat R_X
=
\sum_{a<b}(R_X)_{ab}\eta_a
\frac14[\gamma_a^\perp,\gamma_b^\perp]
\]

and verifies

\[
[\widehat R_X,\Gamma(\alpha_h)]
=\Gamma(\alpha_{\delta_Xh})
\]

for all six Lorentz generators and all four representatives. It also verifies

\[
\widehat R_X^\dagger K+K\widehat R_X=0,
\qquad
\widehat R_X^TC+C\widehat R_X=0
\]

for both \(C\)-components.

These identities make the fully transformed \(h\)-contracted bare bilinears
covariant. If \(h\) is frozen, the \(\delta_Xh\) term is omitted. Invariance
then holds only for the stabilizer of that particular \(h\). The numerical
stabilizer dimensions \(6,6,1,1\) and the direct fixed-kernel commutator test
agree.

### Observer-scalar comparator

The repo's factorized observer calculation branches the vertical vector as
\((1,10)\) under
\(\operatorname{Spin}(3,1)\times\operatorname{Spin}(6,4)\). In that comparator,
each vertical component is a four-dimensional Lorentz-scalar multiplet.

The actual-\(\operatorname{Sym}^2\) calculation instead lets the geometric
Lorentz group act on the metric fibre. Under that action, only the trace
direction is a nonzero full-Lorentz fixed vector.

These are different group actions on a numerical ten. N2a records the fork; it
does not use one to refute the other.

## 9. Three stabilizer questions, not one

The screen returns three separately typed answers.

### 9.1 Lorentz-on-\(\operatorname{Sym}^2\)

Computed exactly from

\[
X^T\eta+\eta X=0,
\qquad
X^Th+hX=0.
\]

Dimensions are \(6,6,1,1\).

### 9.2 Abstract fibre-frame \(SO(6,4)\)

Computed from the fixed-vector equation in the DeWitt-orthonormal frame.
Dimensions are \(45,36,36,36\), with group types listed in Section 7.

This is larger than the image of geometric Lorentz-on-\(\operatorname{Sym}^2\).
It must not be reported as the spacetime stabilizer.

### 9.3 Full native gauge stabilizer

For the zero insertion, the full native gauge group stabilizes the zero
operator.

For a decomposable nonzero datum
\(\alpha_h\otimes\Phi\), one necessary factor that can presently be written is
the formal centralizer

\[
\operatorname{Stab}_{\rm gauge}(\Phi)
=
\left\{
u\in Sp(32,32;\mathbb H):
\rho(\operatorname{Ad}_u\Phi)
=
\rho(\Phi)
\right\},
\]

or infinitesimally

\[
\left\{
\xi\in\mathfrak{sp}(32,32;\mathbb H):
[\rho(\xi),\rho(\Phi)]=0
\right\}.
\]

For a multi-component \(v_s=\sum_\alpha\nu^\alpha\otimes\Phi_\alpha\), this
becomes the corresponding joint centralizer, subject also to any allowed
mixing of the covector components. It is still not the full stabilizer of the
N1 bilinear. That object must additionally preserve or equivariantly
transform the charge form \(C\), the gamma/soldering map, \(P_0\), and the
provenance kernel \(Y_C\) (or the separate \(K,Y_K\) data on the
sesquilinear branch).

N1 does not supply explicit \(\Phi_\alpha\) or \(\rho(\Phi_\alpha)\) matrices
for these representatives. No nonzero full-gauge stabilizer identity or
dimension is computed. In particular, this investigation does not substitute
\(U(128)\) for \(Sp(32,32;\mathbb H)\).

## 10. Corrected \(20\)-slot support and provenance

The independently owned observer-symbol ledger has:

\[
E_{20}=S\oplus\operatorname{im}\Gamma\oplus\ker\Gamma,
\]

with:

- \(20\) explicitly named irreducible slots;
- total complex dimension \(1920\);
- three separately retained four-slot provenance families
  \(S,\operatorname{im}\Gamma,\ker\Gamma_{\rm low}\);
- eight \(X\)-sector slots;
- \(136\) nonzero ordered principal-symbol cells;
- \(68\) horizontal and \(68\) vertical cells.

N2a rechecks those exact numbers and the two important transport controls.

### 10.1 Missing \(N\) hostile control

On the \(\operatorname{im}\Gamma/\ker\Gamma_{\rm low}\) multiplicity plane, the
pairing-only vector coflip induces

\[
\begin{pmatrix}
-3/7 & 2\sqrt{10}/7\\
2\sqrt{10}/7 & 3/7
\end{pmatrix},
\]

so it mixes the two provenance classes. Including the normal grading

\[
N=+1\quad\text{on }TX,
\qquad
N=-1\quad\text{on }\operatorname{Sym}^2T^*X
\]

returns the identity on this plane. The control therefore rejects a
pairing-only transport and retains the corrected \(N\eta\) transport.

### 10.2 Relative-phase hostile control

The static support and mirror-involution matcher admits an independently
flipped mirror pair. The same flip violates \(28\) of the \(136\) nonzero
coefficient equations. Exhausting the \(2^{10}\) mirror-pair sign assignments
leaves exactly two assignments, differing only by one global sign.

### 10.3 What the \(136\) cells do not supply

Those cells classify first-order complexified observer-symbol support. N1's
\(\mathfrak c_\rho(v_s)\) is a zero-order Clifford/gauge insertion. The frozen
packet does not give an explicit matrix lift

\[
\operatorname{End}(S_{\mathbb C})
\longrightarrow
\operatorname{End}(E_{20}),
\]

together with \(P_0\), \(\rho(\Phi)\), and the provenance matrix placement.

Therefore the \(68\) vertical symbol cells are not promoted to \(68\) nonzero
N2a bilinear amplitudes. The representative-specific zero-order \(20\)-slot
matrix remains
**UNRESOLVED-NEEDS-PLACEMENT-MAP**.

This is not a failure of the corrected support ledger. It is the distinction
between a principal symbol and a zero-order action kernel.

## 11. Hostile comparators

### 11.1 Horizontal one-form

For a planted horizontal gamma, both \(C_-\gamma_\parallel\) and
\(C_+\gamma_\parallel\) are also transpose-skew. Yet
\(K\gamma_\parallel\) fails the test for an individual observer-Lorentz scalar.

Thus the \(C\)-transpose sign knows nothing by itself about vertical scalarity.

### 11.2 Exterior ten

Under a central \(GL(4)\) scaling by \(\lambda\),
\(\operatorname{Sym}^2V^*\) has one quadratic weight, while

\[
\Lambda^2V^*\oplus\Lambda^3V^*
\]

contains six quadratic-weight and four cubic-weight directions, up to the
common covariant/contravariant sign convention. For \(\lambda=2\), the exact
intertwining equation forces every map from the actual symmetric ten to the
exterior ten to have rank at most \(6\). No invertible \(GL(4)\)-equivariant
identification exists.

The equal dimensions do not identify the fibres.

### 11.3 Positive Hilbert, \(U(128)\), and ghost subtraction

None is inserted into the executable calculation. They are named hostile forks:

- replacing \(K\) by a positive identity pairing would change the bilinear
  object;
- replacing \(Sp(32,32;\mathbb H)\) by \(U(128)\) would change the full-gauge
  stabilizer problem;
- quotienting or subtracting Rarita--Schwinger sectors would change the frozen
  \(20\)-slot carrier and its support ledger.

No native verdict is allowed to depend on any of these substitutions.

## 12. Knockout ledger

| candidate or inference | disposition | exact reason |
| --- | --- | --- |
| \(C_-\) component \((-1,+1)\) | **SURVIVES bare native algebra** | explicit invertible \(128\times128\) solution; \(C_-\Gamma(\alpha)\) skew |
| \(C_+\) component \((+1,-1)\) | **SURVIVES bare native algebra** | explicit invertible \(128\times128\) solution; \(C_+\Gamma(\alpha)\) skew |
| total \(C\)-branch identical-odd survival | **UNRESOLVED** | needs total \(P_0\times\rho(\Phi)\times Y_C\) kernel and reality completion |
| \(K\)-sesquilinear bare channel | **SURVIVES bare native algebra for nonzero reps** | \(K\Gamma(\alpha_h)\) Hermitian and nonzero |
| \(K\leftrightarrow C\) transfer | **NOT ADMITTED** | no \(\mathcal R_{KC}\) |
| zero representative as vertical coupling | **KILLED at bare insertion** | \(\Gamma(0)=0\) |
| trace representative | **SURVIVES N2a screen** | invertible rank \(128\), full Lorentz fixed |
| spacelike-traceless representative | **SURVIVES covariance; fails full fixed-background Lorentz invariance** | rank \(128\), fixed stabilizer dimension \(1\) |
| null representative | **SURVIVES covariance; fails full fixed-background Lorentz invariance** | nonzero rank-\(64\) nilpotent, fixed stabilizer dimension \(1\) |
| nonzero full-gauge stabilizer claim | **UNRESOLVED** | \(\Phi_\alpha\) and \(\rho\) matrices absent |
| \(68\) vertical symbol cells \(\Rightarrow68\) nonzero bilinear entries | **REJECTED inference** | first-order support is not zero-order placement |
| exterior ten as actual metric ten | **KILLED as natural \(GL(4)\) identification** | central-weight test bounds intertwiner rank by \(6\) |
| pairing-only coflip | **KILLED on corrected full-20 transport fork** | mixes \(\operatorname{im}\Gamma\) and low-\(\ker\Gamma\) |
| independent mirror-pair phase | **KILLED on written coefficient transport** | violates \(28/136\) coefficient equations |
| any generation/index/count result | **OUT OF TYPE** | insertion rank and provenance blocks are not those counts |

“Survives” here means only that the stated finite algebraic necessary condition
did not kill the candidate. It is not “selected,” “stationary,” “physical,” or
“massive.”

## 13. Executable controls

Run:

```bash
python3 tests/channel-swings/actual_sym2_c14_orbit_probe.py
```

The passing certificate checks:

1. the frozen N1 executable construction hash;
2. the native \(128\times128\) \(\operatorname{Cl}(9,5)\) relations;
3. the \((3,1)+(6,4)\) relabeling without a basis substitution;
4. seven transpose-symmetric and seven transpose-skew generators;
5. both explicit \(C\)-components and their \((\varepsilon_C,\tau_C)\) signs;
6. native \(K\) Hermiticity and all \(91\) Spin-invariance equations;
7. the actual-\(\operatorname{Sym}^2\) DeWitt frame and signature;
8. the trace vector as the inverse DeWitt musical of \(\tau_g\);
9. square, rank, and nonzero-null nilpotence for all four representatives;
10. bare \(C\)-kernel skewness and bare \(K\)-kernel Hermiticity;
11. hostile rejection of the Frobenius musical;
12. the induced Lorentz-on-\(\operatorname{Sym}^2\) lift into
    \(\mathfrak{so}(6,4)\);
13. dynamical contraction covariance and fixed-background breaking;
14. non-unitary similarity covariance;
15. symmetric, skew, and \(P_0\)-annihilated planted total Grassmann kernels;
16. the corrected \(20\)-slot, \(1920\)-dimension, \(68+68\) support ledger;
17. missing-\(N\) and independent-relative-phase hostile controls;
18. the exterior-ten central-weight obstruction;
19. the horizontal non-scalar comparator.

The current run exits zero with all controls passed.

## 14. What N2a now demands

The highest-information next construction is not another spinor-sign probe. It
is the smallest explicit total-kernel packet that supplies:

1. \(P_0\) as an actual matrix or basis map on the defect carrier;
2. one frozen nonzero \(\Phi\) representative for each geometric stratum;
3. \(\rho(\Phi)\) in the native \(Sp(32,32;\mathbb H)\)-typed representation;
4. the placement of \(\Gamma(\alpha_h)\rho(\Phi)\) on the corrected
   \(E_{20}\) provenance slots;
5. the admissible transpose/reality subspace of \(Y_C\) and Hermiticity/reality
   subspace of \(Y_K\);
6. the \(C\)-branch reality completion;
7. the full-kernel \(Sp(32,32;\mathbb H)\)-equivariance/stabilizer equations,
   including the gamma/soldering and \(P_0\) actions;
8. only then, the restricted total-kernel rank and Grassmann diagonal.

That packet has constraint surplus: it must simultaneously respect the native
Clifford signs, DeWitt musical, corrected \(N\eta\) transport, \(136\) written
coefficient equations, gauge typing, and defect restriction. A successful fit
would therefore teach something. Until it is written, declaring either
bilinear dead or physically realized would answer the wrong Layer-0 question.

## 15. Explicit nonclaims

This file makes no claim about:

- an Euler--Lagrange solution or stationary background;
- a physical mass, mass hierarchy, or normalizable Hessian mode;
- positivity, unitarity, or a physical probability interpretation;
- anomaly cancellation or inflow;
- a Fredholm/chiral index;
- generation or particle count;
- exhaustive \(\operatorname{Sym}^2\) orbit classification;
- the physical low-energy gauge group;
- a \(K\)-to-\(C\) equivalence;
- a zero-order \(20\)-slot amplitude table;
- N2b, which remains downstream of N3.

The result is a conditional construction step: the native spinor and geometric
pieces now exist explicitly, and the remaining uncertainty has been localized
to named total-kernel maps rather than hidden behind a generic “Yukawa”
label.
