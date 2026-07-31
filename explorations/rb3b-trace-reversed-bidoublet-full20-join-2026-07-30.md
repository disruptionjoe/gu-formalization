---
title: "RB3b trace-relative fixed-Cartan four-component candidate and full-20 lift"
status: active_research
doc_type: construction_result
created: 2026-07-30
lane: "1"
work_item: RB3B-TRACE-REVERSED-BIDOUBLET-FULL20-JOIN
run: lab/process/runs/GUH-20260730T232344Z-rb3b-trace-vertex-grade3/run-plan.md
probe: tests/channel-swings/rb3b_trace_reversed_bidoublet_full20_probe.py
grade: "PASS FIXED-CARTAN FINITE ALGEBRA / OBSERVER-CARTAN REDUCTION UNBUILT. The defining rho_S is canonical. Trace reversal changes the fibre from (7,3) to (6,4), fixes the negative trace line, and fixes native Hodge signs, but does not select the A6+W4 maximal-compact split used by the candidate. The executable DEWITT_FRAME additionally chooses an observer/Cartan reduction: rotations preserve it, all three induced boosts mix its planes, and a finite boost moves its W4 projector. Conditional on that reduction, a right-H/Krein-compatible four-component image and canonical full-20 lift exist. The domain W4 has abstract (1,2,2) shape before fixing t; the fixed-t image is only Spin3-equivariant, not a constructed Spin4 bidoublet. Imposed Hilbert-Schmidt isometry gives |lambda|=1, but lambda signs are coordinate parameterizations of one image and their physical quotient is unresolved. Scalar/Phi/M are coflip-even; pseudoscalar/Phi/M are odd. Each component has 44 supported ordered blocks in the fixed twenty-slot decomposition. Retained mode, physical observer/Cartan origin, full moving covariance, compact/SM reduction, VEV, stabilization, and cosmology remain open."
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# RB3b trace-relative fixed-Cartan candidate and full-20 lift

## Result first

The first “missing factor” reported by RB3 was typed too early. For the
native defining bundle

\[
G=Sp(32,32;\mathbb H),\qquad S=\mathbb H^{64},
\]

the derived representation is already the fibrewise inclusion

\[
\rho_S:\operatorname{ad}P
\hookrightarrow \operatorname{End}_{\mathbb H}(S).
\]

Thus

\[
\rho_S(\Phi_{\rm tr})=\Phi_{\rm tr}
\]

in the native matrix realization. The missing choice is the
source-owned subspace or field value in which
\(\Phi_{\rm tr}=-4v(h_{\rm tr})\) lives.

This swing constructs a small **fixed-Cartan** conditional answer. Trace
reversal makes the metric fibre have signature \((6,4)\) and canonically
fixes its negative trace line. It does not select a maximal-compact vector
split. The executable frame additionally chooses

\[
V_{6,4}=A_6\oplus W_4,
\qquad
W_4\simeq(\mathbf1,\mathbf2,\mathbf2)
\]

under
\(\operatorname{Spin}(6)\times\operatorname{Spin}(4)
\simeq SU(4)\times SU(2)_L\times SU(2)_R\).
The unique metric trace direction is a unit negative line
\(t\in W_4\). Conditional on the chosen observer/Cartan reduction, the two
oriented volume elements and Clifford multiplication construct a
four-component native adjoint image. Native reality makes its relative
coefficient real. Imposing an additional Hilbert--Schmidt isometry condition
fixes its magnitude to

\[
\lambda=\pm1.
\]

The signs are two ordered-domain parameterizations of the same
four-dimensional image, related by an orientation-reversing reflection.
Whether that reflection is a physical branch or a field redefinition is
unresolved. The planted \(\lambda=2\) map has the same image but fails only
the imposed isometric normalization.

No independent \(128\times128\) matrix is fitted to any component.

For either discrete branch, the zero-order spinor operator

\[
M_{\rm tr}(w)=c(\widehat\tau)\Phi_t^\lambda(w)
\]

is right-\(\mathbb H\)-linear and Krein-self-adjoint. Its \(K\)-paired
fermion kernel commutes with the frozen first-four spin factor and is
cross-chirality.
The \(C_+\) complex-bilinear kernel has the required Grassmann-skew
transpose class; \(C_-\) has the opposite class and would require an
additional antisymmetric label for an identical Grassmann field.

The minimal associated full-carrier lift

\[
\widehat M_{\rm tr}
=
M_{\rm tr}\oplus(1_V\otimes M_{\rm tr})
\quad\text{on}\quad
S\oplus(V\otimes S)
\]

is explicit. Resolving it through the repository's twenty orthonormal thin
embeddings gives the same 44 supported ordered source-target block
positions for all four components:

\[
4_{SS}+4_{II}+8_{IR}+8_{RI}+20_{RR}=44.
\]

Every transformed witness reconstructs from those twenty slots to numerical
precision. The associated lift has nonzero coordinate blocks involving
\(X\)-labelled summands. That does not construct \(X\) provenance, retention,
or a physical selector.

This is a fixed-frame candidate source stratum, not a constructed
observer/Cartan reduction, full moving-covariant Pati--Salam multiplet,
complete low-energy Standard Model selector, retained normalizable
four-dimensional mode, VEV, mass spectrum, or cosmological prediction.

## Plain English

The trace reversal Joe flagged changes the answer qualitatively.

Without it, the ten metric-fibre directions have signature \((7,3)\), and
the trace direction is positive. With GU's DeWitt trace reversal, that one
direction changes sign. The fibre becomes \((6,4)\).

But a signature tells us only how many positive and negative directions
there are. It does not choose the particular six-plane and four-plane used
by the formula. The executable frame makes an additional choice equivalent,
on the base, to selecting a timelike observer line. Rotations preserve that
choice; Lorentz boosts move it. This is a real construction obligation and
a plausible type for the still-untyped \(X\)-sector datum, not something
paid for by the existing orientation bit.

The construction uses the trace direction to join the two native places
where a four-component domain occurs in the Clifford adjoint after that
observer/Cartan choice. The trace condition
keeps one component from the first copy and three from the second. Requiring
equal Hilbert--Schmidt normalization fixes the relative magnitude within
that ansatz; this condition is not yet derived from the retained kinetic
term. Native reality makes the coefficient real. The two signs are related
by a reflection of the domain coordinates and do not create a second image
subspace.

So the surviving result is a specific fixed-frame formula producing four
matrices with the right native reality and physical bilinear properties,
together with an explicit full-20 lift. It is not yet a geometric
Pati--Salam bidoublet on the unfixed bundle.

The first remaining gap is now upstream and sharply typed: supply or derive
the moving observer/Cartan reduction and test joint induced-Lorentz
covariance. Only then come the retained normalizable mode, orientation/field-
redefinition quotient, stable nonzero solution, compact reduction, and
target-free Standard Model selector.

## 1. Layer 0: the three trace objects

Let \(g\) be the Lorentzian metric on \(X^4\). The three objects that must
not be identified by their coordinate matrices are

\[
h_{\rm tr}=-\frac14g,
\qquad
\tau(k)=\frac14\operatorname{tr}_g(k),
\qquad
q_\tau=+\frac14g^{-1}.
\]

They obey

\[
G_{\rm DW}(h_{\rm tr},k)=\tau(k),
\qquad
G_{\rm DW}^{-1}(\tau,\tau)=-\frac14.
\]

The plus-signed Lorentzian coordinate matrix \(q_\tau\) is the
Frobenius-coordinate representative of the **DeWitt covector**. It is
indefinite, not positive, and is not the primal tensor \(h_{\rm tr}\).

For the unit-normalized negative trace objects used by the finite Clifford
probe, set

\[
\widehat h_{\rm tr}=2h_{\rm tr}=-\frac12g,
\qquad
\widehat\tau=2\tau,
\qquad
G_{\rm DW}^{-1}(\widehat\tau,\widehat\tau)=-1.
\]

For the raw Frobenius form

\[
G_{\rm F}(h,k)
=\operatorname{tr}(g^{-1}hg^{-1}k),
\]

the same primal trace tensor instead obeys

\[
G_{\rm F}(h_{\rm tr},k)=-\tau(k),
\qquad
G_{\rm F}^{-1}(\tau,\tau)=+\frac14.
\]

Thus a quadratic-only test is powerless: it can hide the musical sign.
The probe requires both the linear Clifford insertion and the inverse-metric
trace norm to distinguish the two geometries.

The raw-Frobenius normalized trace generator belongs to
\(\mathrm{Cl}(7,3)\) and squares \(+1\). It is not represented by merely
negating \(c(\widehat\tau)\) inside the native
\(\mathrm{Cl}(6,4)\), where the trace generator squares \(-1\).

The signature and Hodge consequences are:

| geometry | fibre | total with \((3,1)\) base | \(*^2\) on \(1/13\) | \(*^2\) on \(2/12\) |
| --- | --- | --- | ---: | ---: |
| raw Frobenius comparator | \((7,3)\) | \((10,4)\) | \(-1\) | \(+1\) |
| DeWitt / trace-reversed | \((6,4)\) | \((9,5)\) | \(+1\) | \(-1\) |

The second row is the program-native geometry. The first is retained only as
a hostile control.

## 2. The trace-relative adjoint construction

Trace reversal determines the trace line and the signature class. It does
not canonically determine a representative maximal-compact split. The
executable fixture additionally chooses an observer/Cartan reduction
\(\chi\):

\[
V_{6,4}=A_6^{(\chi)}\oplus W_4^{(\chi)}.
\]

In the actual symmetric-tensor geometry this can be typed by a unit timelike
observer line \(u\) on \(X^4\), with

\[
W_4^{(u)}
=
\mathbb R\,\widehat h_{\rm tr}
\oplus
\left(u^\flat\odot u^\perp\right).
\]

The probe now executes the induced Lorentz action. The trace line is fixed
by all six generators. Spatial rotations preserve the displayed split
exactly, while each of the three boosts has

\[
\|L_{A\leftarrow W}\|
=\|L_{W\leftarrow A}\|
=2.449489743,
\qquad
\|[L,P_W]\|=3.464101615.
\]

A boost of rapidity \(0.37\) moves \(P_W\) by norm \(1.940205721\).
Therefore neither the DeWitt form nor the trace line supplies \(\chi\).
The repository's prior
[`AUDIT-noncompact-compact-reduction-EXTERNAL.md`](big-swing-2026-07-03/AUDIT-noncompact-compact-reduction-EXTERNAL.md)
independently grades the physical noncompact-to-compact reduction as
external. A source action could still dynamically select a moving
reduction, but it has not done so here.

Conditional on \(\chi\), let \(\omega_A,\omega_W\) be the corresponding
oriented Clifford volume elements. Let \(t\in W_4^{(\chi)}\) be the negative
trace direction, normalized by
\(c(t)^2=-1\). Define the anticommuting projection

\[
\mathcal P_t^-(B)
=\frac12\left(B-c(t)Bc(t)^{-1}\right).
\]

For \(w\in W_4^{(\chi)}\) and a real relative coefficient \(\lambda\), define

\[
\boxed{
\Phi_t^\lambda(w)
=
\mathcal P_t^-\!\left[
\omega_Wc(w)+\lambda\,\omega_Ac(w)
\right].
}
\]

The two summands lie in internal Clifford grades three and seven. Both are
native grades of
\(\mathfrak{sp}(32,32;\mathbb H)\). Joint covariance would require
\(\chi,t,w,\omega_A,\omega_W\), and the Clifford plane to move together.
That simultaneous induced-\(\operatorname{Sym}^2\) construction is not yet
executed.

Before fixing \(t\), the chosen domain \(W_4^{(\chi)}\) has abstract
\((\mathbf1,\mathbf2,\mathbf2)\) shape under the selected
\(\operatorname{Spin}(6)\times\operatorname{Spin}(4)\). At fixed nonzero
\(t\), the constructed image is only equivariant under its
\(\operatorname{Spin}(3)\) stabilizer:

\[
W_4\downarrow_{\operatorname{Spin}(3)}
=\mathbf1\oplus\mathbf3.
\]

The projection keeps the \(\mathbf1\) from the
\(\omega_Wc(w)\) copy and the \(\mathbf3\) from the
\(\omega_Ac(w)\) copy. The three selected \(\operatorname{Spin}(4)\)
generators that mix \(t\) with \(t^\perp\) leave this fixed image, so the
fixed-\(t\) four matrices are not yet a \((2,2)\) module. The probe powers
this distinction: all three \(\operatorname{Spin}(3)\) stabilizer
leakages are zero, while each of the three \(\operatorname{Spin}(4)\)
mixing-generator image-span leakages is \(5.656854249\).

In the finite trace fixture, the positive Hilbert--Schmidt comparison form
has pullback Gram matrix

\[
H_0(\Phi_i,\Phi_j)
=\frac1{128}\operatorname{Tr}(\Phi_i^\dagger\Phi_j)
=\operatorname{diag}(1,\lambda^2,\lambda^2,\lambda^2)_{ij}.
\]

Native right-\(\mathbb H\) and Krein-skew reality require real
\(\lambda\). **If** this comparison form is imposed as the retained
isometric-soldering normalization, equal normalization gives

\[
\lambda^2=1.
\]

The planted \(\lambda=2\) branch has a \(1:4:4:4\) ratio in \(H_0\). It is rejected
only as an **isometrically normalized soldering map**, not as a distinct
subspace: every nonzero \(\lambda\) in this ansatz has the same
four-dimensional image. The retained kinetic metric is unbuilt, so this is
an ansatz condition rather than a source-derived physical normalization.
Within this two-copy ansatz there is one projective continuous ratio and one
imposed isometry equation. The two displayed signs are related by the
domain reflection
\(\operatorname{diag}(1,-1,-1,-1)\); their
field-redefinition/orientation quotient is unresolved. This is not yet a global
constraint-surplus calculation for all downstream \(P_0/Y/\)selector
choices.

Multiplication by the four-dimensional chirality element supplies a second
Lorentz-scalar but parity-odd family. It passes the same native \(K/C\)
tests. The corrected coflip separates the two:

| branch | coflip parity of \(\Phi\) | coflip parity of \(M_{\rm tr}\) |
| --- | ---: | ---: |
| scalar / base degree \(0\) | even | even |
| pseudoscalar / base degree \(4\) | odd | odd |

The trace Clifford insertion is itself coflip-even, so it does not change
the parity. Both branches pass the other native finite tests. No source-owned
parity/CP rule selects one, and neither is silently erased.

## 3. Bilinear rather than bare-operator test

Let \(\widehat\tau\) be the unit-normalized negative DeWitt trace covector,
with its orientation fixed by
\(G_{\rm DW}(h_{\rm tr},\cdot)=\tau\). Its Clifford action obeys

\[
c(\widehat\tau)^2=-1,
\qquad
c(\tau)=\frac12c(\widehat\tau)
\]

in the normalized native frame. Set

\[
M_{\rm tr}(w)=c(\widehat\tau)\Phi_t^\lambda(w).
\]

The unit normalization is used for the finite bilinear tests; the factor
\(1/2\) returns in action coefficients. Raw Frobenius reverses the linear
musical sign and changes the trace generator's Clifford square; it is not
the same native matrix with a minus sign. Because

\[
\Phi^\ddagger=-\Phi,
\qquad
\{c(t),\Phi\}=0,
\]

one has

\[
M_{\rm tr}^\ddagger=M_{\rm tr}.
\]

The probe checks this directly on all four \(128\times128\) matrices, along
with

\[
M_{\rm tr}J_{\mathbb H}
=J_{\mathbb H}\overline{M_{\rm tr}}.
\]

Each component has rank \(128\).

The operator \(M_{\rm tr}\) commutes with four-dimensional chirality. That
is not the physical mass test. The Krein pairing anticommutes with
four-dimensional chirality, so

\[
K M_{\rm tr}
\]

is cross-chirality. It is Hermitian and commutes with the frozen first-four
\(\operatorname{Spin}(3,1)\) spin generators. This does not replace the
unbuilt diagonal covariance under the induced Lorentz action on the
\(\operatorname{Sym}^2\) fibre and moving Cartan reduction.

For the two independent charge-conjugation branches, the finite matrices
give

\[
(C_+M_{\rm tr})^T=-C_+M_{\rm tr},
\qquad
(C_-M_{\rm tr})^T=+C_-M_{\rm tr}.
\]

Thus \(C_+\) survives the identical-Grassmann-field bilinear and \(C_-\)
does not. The \(K\) and \(C_+\) statements are separate physical branches;
neither is derived from the other.

This strengthens the existing vertical--Krein channel result by supplying
an explicit fixed-Cartan native gauge-adjoint image. It does not newly claim that a
bare vertical Clifford vector is an ambient \(\Lambda^0(V_{9,5})\).

## 4. Canonical full-carrier lift

The first full-carrier lift needs no new coefficient:

\[
\widehat M_{\rm tr}
=
\begin{pmatrix}
M_{\rm tr}&0\\
0&1_V\otimes M_{\rm tr}
\end{pmatrix}
\quad\text{on}\quad
S\oplus(V\otimes S).
\]

This is an endomorphism of the \(1920\)-complex-dimensional carrier. It need
not preserve \(I=\operatorname{im}\Gamma\) and
\(R=\ker\Gamma\); physical zero-order mixing is precisely recorded by

\[
P_a\widehat M_{\rm tr}P_b,
\qquad a,b\in\{S,I,R\}.
\]

The earlier preregistered phrase “fails \(P_R\) covariance” is corrected
here: moving-frame covariance is required, but commutation with a fixed
\(P_R\) is not. A same-rank operator that fails the simultaneous transport
law remains the hostile control.

Using the repository's twenty orthonormal embeddings, the probe computes
every block
\(B_{\rm target}^\dagger\widehat M_{\rm tr}B_{\rm source}\).
The supported ordered block positions are:

| block | supported ordered positions |
| --- | ---: |
| \(S\to S\) | 4 |
| \(I\to I\) | 4 |
| \(I\to R\) | 8 |
| \(R\to I\) | 8 |
| \(R\to R\) | 20 |
| **total** | **44** |

All four scalar and all four pseudoscalar components have identical support.
The minimum supported block norm is \(0.8081\), while the maximum classified
zero is \(9.675\times10^{-16}\). The \(IR/RI\) reverse positions come from
the same constructed operator; they are not independent couplings.
Reconstruction from the twenty targets has relative residual below numerical
tolerance. The \(P_0\)-sandwiched **support counts** are therefore

\[
P_0=1:44,\qquad
P_S:4,\qquad
P_I:4,\qquad
P_R:20.
\]

These are zero-order ordered block positions in the fixed slot
decomposition, not modes, ranks, constraints, parameters, or the older
first-order principal-symbol count. The corresponding carrier ranks remain
\(1920/128/128/1664\). Nonzero blocks involving \(X\)-labelled summands do
not construct their provenance or physical retention.

For the scalar branch, the corrected Gamma-natural coflip acts on
\(\Phi\), \(M_{\rm tr}\), and \(\widehat M_{\rm tr}\) with even parity.
The pseudoscalar equivalents are odd. The vector factor cancels in
conjugation of \(1_V\otimes M_{\rm tr}\). A pairing-only coflip remains the
planted near-miss because it mixes \(I\) with the low \(R\) copy.

No arbitrary \(Y\) is required for this minimal placement. A nontrivial
\(Y_K\) or \(Y_C\) can still be composed with the lift, but its provenance,
\(X\)-sector rule, reality completion, and free-parameter count must be
charged separately. The identity/minimal branch does not derive flavour
hierarchy.

## 5. Pati--Salam and Standard Model boundary

For a **chosen** maximal-compact reduction, the domain has the abstract
branching

\[
W_4^{(\chi)}=(\mathbf1,\mathbf2,\mathbf2)
\]

under

\[
SU(4)\times SU(2)_L\times SU(2)_R.
\]

This is group-theoretic shape, not a derived physical reduction. The
repository already records that the maximal-compact restriction is external
unless a source dynamics selects it. Moreover, fixing the trace direction
reduces the tested image symmetry to \(\operatorname{Spin}(3)\). The full
\(\operatorname{Spin}(4)\) generators mixing \(t\) with \(t^\perp\) leave
the fixed image span. Thus the current matrices are not yet a constructed
Pati--Salam \((2,2)\) multiplet; that would require the unexecuted joint
moving-\(t,\chi\) covariance.

If one additionally imports the standard Pati--Salam-to-SM branching, then

\[
(\mathbf1,\mathbf2,\mathbf2)
\longrightarrow
(\mathbf1,\mathbf2,+\tfrac12)
\oplus
(\mathbf1,\mathbf2,-\tfrac12).
\]

The probe does not construct hypercharge, identify the selected abstract
\(\operatorname{Spin}(4)\) with the physical gauge factor, or verify the
reality relation after this imported branching.

Layer 0 remains decisive. The repository has a bounded no-go for treating
Pati--Salam host containment as a target-free complete Standard Model
selector. This swing does not derive:

- the global \(G_{\rm SM}/\mathbb Z_6\) quotient;
- absolute hypercharge normalization from the source action;
- a complete physical spectrum and extra-mode decoupling;
- a retained nonzero critical-section projection; or
- a vacuum breaking orbit.

The result is therefore
`FIXED-CARTAN-FOUR-COMPONENT-IMAGE-CONSTRUCTED /
MOVING-PATI-SALAM-AND-COMPLETE-SM-SELECTOR-OPEN`,
not “a source-geometric Higgs or the Standard Model is recovered.”

## 6. One field in the fermion and cosmology legs

Let

\[
\Phi_{\rm tr}(x)=\sum_{i=1}^{4}\phi_i(x)\Phi_i,
\qquad
v_{\rm tr}=\tau\otimes\Phi_{\rm tr}.
\]

The \(\phi_i\) are field coordinates, not four fitted matrices. The same
\(\Phi_{\rm tr}\) enters:

1. the unit-normalized reduced zero-order fermion operator
   \(M_{\rm tr}=c(\widehat\tau)\Phi_{\rm tr}\), with the geometric
   \(1/2\) restored in the action coefficient; and
2. the ambient distortion quadratic already written in N1.

The invariant statement before choosing the adjoint-pairing normalization or
branch is

\[
G_{\rm DW}^{-1}(\tau,\tau)
\kappa(\Phi_{\rm tr},\Phi_{\rm tr})
=-\frac14\kappa(\Phi_{\rm tr},\Phi_{\rm tr}).
\]

For the raw coordinate fixture
\(\kappa_0=\operatorname{ReTr}_S\), the direct matrices give

\[
\kappa_0(\Phi_i,\Phi_j)
=
\begin{cases}
+128\delta_{ij},&\text{scalar branch},\\
-128\delta_{ij},&\text{pseudoscalar branch}.
\end{cases}
\]

The corresponding pointwise products are therefore
\(-32\sum_i\phi_i^2\) and \(+32\sum_i\phi_i^2\), respectively. This
\(\kappa_0\) is distinct from the positive Hilbert--Schmidt comparison form
used to impose the optional isometry condition. The raw-Frobenius geometry
reverses the trace-norm sign, but the physical invariant-pairing
normalization, branch, action coupling, and moving reduction remain charged.
These are ambient pointwise quadratic-sign fixtures, not cosmological
coefficients or predicted tachyonic masses.

The pure decomposable one-form
\(v_{\rm tr}=\tau\otimes\Phi_{\rm tr}\) obeys
\(v_{\rm tr}\wedge v_{\rm tr}=0\). Ambient Yang--Mills therefore does not
generate a local quartic from that one vertical form alone. A stable
nonzero orbit needs mixed vertical modes, background curvature, a
source-action interaction, or another term already generated by the full
Euler system. None is added here by hand.

The ambient-to-section variation also contains

\[
D_s\Phi_{\rm tr}
=-4\left[(D_sv)(h_{\rm tr})+v(D_sh_{\rm tr})\right]
\]

and the variation of \(\tau\), the measure, the horizontal split, and the
retained-mode map. Consequently this result does not yet identify the
ambient trace response with the N3 traceless-Ricci Hessian or predict a
four-dimensional cosmological constant.

## 7. Datum and constraint ledger

The datum ledger changes materially:

- \(t\) is fixed geometrically by the DeWitt trace line;
- \(\chi\), the observer/Cartan reduction selecting
  \(A_6^{(\chi)}\oplus W_4^{(\chi)}\), is **not** fixed by the DeWitt form;
- in the base-induced realization, \(\chi\) can be typed as a unit future
  timelike observer line, locally an
  \(SO^+(3,1)/SO(3)\) field with three continuous components before gauge
  and dynamical equations;
- the four \(\phi_i\) are dynamical field coordinates conditional on
  \(\chi\);
- \(|\lambda|=1\) follows only after imposing the unproved retained-isometry
  condition; and
- the scalar/pseudoscalar parity branch remains unselected.

This is the first concrete type candidate for the previously unknown
\(X\)-sector datum: a moving observer/Cartan reduction. It is **not**
identified with P2 merely because P2 is open, and it is not the P1/P2
\(\mathbb Z_2\) orientation line. Layer 0 must construct an explicit map to
an existing datum or charge \(\chi\) separately. The prior
noncompact-to-maximal-compact audit also prevents treating the physical
compact restriction as free.

The \(\lambda=\pm1\) maps have the same image and are related by a chosen
domain reflection. Until an orientation-sensitive action term or transport
map survives field-redefinition quotienting, they are not counted as two
physical branches and are not mapped to P1/P2.

P3 remains a separate relative-\(KO\) interface. Every fixed-frame
\(\Phi_i\) and \(M_i\) is right-\(\mathbb H\)-linear, so the candidate does
not itself violate P3 compatibility and does not read out an index or count.

Global constraint surplus remains uncomputed until \(\chi\)'s origin and
gauge quotient, the retained-mode map, \(P_0\), any nontrivial \(Y\), the
low-energy selector, kinetic normalization, field redefinitions, and VEV
freedom are frozen. Within the two-copy fixed-frame ansatz only, one
projective continuous ratio faces one **imposed** isometry equation; that is
not yet a physical surplus result.

## 8. Seven-axis register

This is a smooth-bundle construction inside the GU class, not a claimed
escape from a chirality/anomaly no-go.

| candidate | L0 | L1 substrate | L2 observer | L3 pairing | L4 causal order | L5 emergence | L6 loop | L7 positivity | first falsification |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| fixed-Cartan trace candidate | primal trace/covector/coordinate matrix separated; signature distinguished from a chosen Cartan split; fixed-\(t\) image distinguished from moving \((2,2)\) domain | smooth \(Sp(32,32;\mathbb H)\) bundle on \(Y^{14}\), conditional observer/Cartan reduction | section plus unbuilt observer line \(\chi\) and retained vertical mode | fixed-frame native connection; separate \(K\)-sesquilinear and \(C_+\)-bilinear branches | ambient \((9,5)\), observed \((3,1)\) shadow; induced boosts move \(P_W\) | fixed-frame field image, no RG claim | no observer feedback loop | indefinite DeWitt/Krein; Hilbert--Schmidt form used only as a comparator | construct joint \(\chi,t,\omega_A,\omega_W\) covariance; failure kills the geometric bidoublet reading |

The construction preserves the smooth/local assumptions of the standard
representation no-goes. Its physical chirality statement comes from the
already-declared Krein bilinear after four-dimensional reduction, not from
changing an index or generation count.

## 9. What this changes and what comes next

RB3's first-arrow ledger should be corrected from

```text
rho_S(Phi_trace): MISSING
```

to

```text
rho_S: DEFINING INCLUSION, EXECUTED
Phi_trace source subspace/value: FIXED-CARTAN FOUR-COMPONENT CANDIDATE
observer/Cartan reduction chi: REQUIRED / UNBUILT
minimal fixed-frame full-carrier lift: EXECUTED
moving Pati-Salam/retained low-energy selector/Y/VEV: OPEN
```

The next highest-information construction is now:

1. construct or derive the observer/Cartan reduction \(\chi\), or identify
   it with an existing datum by an explicit Layer-0 map; treat it as a
   serious candidate type for P2, not an automatic identification;
2. move \(\chi,t,P_W,\omega_A,\omega_W\), and the Clifford plane together
   under induced base-Lorentz transformations and test whether the full
   four-component family descends; failure kills the geometric bidoublet
   reading but preserves the fixed-frame algebraic image;
3. insert every surviving scalar/pseudoscalar and
   field-redefinition/orientation branch into the existing N1 covariant
   operator rather than adding a duplicate `T10`;
4. build the ambient-to-\(X^4\) retained-mode map and derive its kinetic
   metric, then decide whether the Hilbert--Schmidt isometry condition and
   \(\lambda\) quotient were physically justified;
5. derive the quadratic-plus-mixed-mode potential from the already-written
   action and determine whether any source-owned quartic or curvature term
   stabilizes a nonzero orbit; and
6. only then compute a quotient-aware constraint surplus and confront the
   compact reduction, complete SM selector, flavour, and cosmology legs.

The curvature-current and grade-three source tracks in this run are recorded
separately because they alter different action maps and have different
re-entry points.

## Reproduction and nonclaims

Run:

```bash
python3 tests/channel-swings/rb3b_trace_reversed_bidoublet_full20_probe.py
python3 tests/channel-swings/full20_dewitt_loop_transport_probe.py
python3 tests/channel-swings/rb3_moving_soldering_spinzero_probe.py
```

This result claims no source-owned observer/Cartan reduction, moving
Spin(4) bidoublet, physical compact reduction, retained normalizable mode,
VEV, physical mass, flavour hierarchy, stable potential, complete Standard
Model recovery, stationary solution, nonlinear CME, common global domain,
anomaly cancellation, Fredholm index, generation count, or cosmological
prediction.

## RB4 Layer-0 correction and continuation

Later RB4 work constructs the exact moving base-induced family and
supersedes the stale datum paragraph above.

P2 was already typed before RB3b as the phase/orientation of the canonical
vertical projected Rarita--Schwinger symbol and was subsequently welded
with P1, at finite associated-bundle/first-order grade, into the one flat
orientation line \(L_\sigma\). The continuous observer/Cartan field is not
P2 and was never an unknown X-sector datum.

For a unit timelike \(u\),

\[
W_4(u)=\mathbb Rt\oplus(u^\flat\odot u^\perp)
\]

is exactly negative of rank four, with a positive rank-six complement.
RB4 jointly transports \(P_W,\omega_A,\omega_W\), the Clifford frame, and
the conditional \(\Phi\) family under base Lorentz transformations. Thus
the moving-\(u\) covariance step requested above is now constructed.

That result does not supply the full source-owned reduction. The
three-dimensional observer family is a special subfamily of the
24-dimensional vertical Cartan space. More importantly, the compatible
complex structure suggested by Weinstein's later source language is not
derived from \(u\): a fixed-\(u\) \(SO(3)\) stabilizer motion leaves
\(u,P_W,t\) fixed while moving \(J\). The observer-only map \(u\mapsto J\)
is refuted.

The sharpened remaining object is a compatible complex--Cartan flag

\[
(J,\Theta_\chi;t),
\]

plus a determinant-one/complex-volume condition if the compact
intersection is to be \(S(U(3)\times U(2))\) rather than
\(U(3)\times U(2)\). Its \(\epsilon_{\rm IG}\) ownership, Euler equation,
gauge quotient, stable orbit, and retained physical mode remain unbuilt.
See
[`rb4-observer-cartan-moving-family-2026-07-30.md`](rb4-observer-cartan-moving-family-2026-07-30.md).
