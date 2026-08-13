---
title: "Full-20 native-polarization wave: an exact auxiliary complex survives, while actual Sym2 curvature obstructs the physical R gauge"
status: active_research
doc_type: result
created: 2026-07-30
work_item: SOURCE-OWNED-CHIMERIC-BV-CAMPAIGN-S3-NATIVE-POLARIZATION
code:
  - tests/channel-swings/full20_native_polarization_probe.py
  - tests/channel-swings/full20_observer_projector_support_probe.py
canon_verdict_change: none
---

# Full-20 native-polarization and conditional-closure wave

## Result

The large third construction swing returns:

```text
NATIVE-SPINOR-KREIN-FORM-FIXED-UP-TO-SCALE
INDUCED-I/R-PAIRING-ORTHOGONAL
S/I-MULTIPLICITY-GRAM-NOT-FORCED
NINE-BLOCK-FORMAL-EXPRESSION-FAMILY-ADJOINT-CLOSED
ODD-POLARIZED-FULL-SUPPORT-DET-LOCUS-NONEMPTY
OBSERVER-COMPLEX-20-PROJECTOR-SUPPORT-REDERIVED
AUXILIARY-S/I-FORMAL-GAUGE-COMPLEX-EXACT
W177-ACTUAL-SYM2-CURVATURE-OBSTRUCTS-GENUINE-R-GAUGE-CLOSURE
FORMAL-GREEN-PACKET-BUILT/GLOBAL-NATIVE-DOMAIN-OPEN
NO-COMPENSATOR-SELECTED
```

This is simultaneously a construction advance and a useful obstruction.
The program-native spinor Krein form is fixed up to overall scale, the
gamma-trace splitting \(V\otimes S=I\oplus R\) is orthogonal for the induced
form, and every formal adjoint of the nine written blocks stays inside the
nine-block family. Native polarization therefore does **not** demand a
tenth first-order carrier block.

On the Grassmann-odd polarization branch, the adjoint-compatible family
still has a nonempty principal kernel locus with every one of the nine
carrier blocks nonzero and a gauge vector that reaches
\(S\), \(I=\operatorname{im}j\), and \(R=\ker\Gamma\). This proves that the
Krein pairing does not kill the construction at principal-symbol grade.
It is only a feasibility result: after polarization the determinant is one
real equation in eight real carrier parameters, so the raw fit has negative
constraint surplus and is not confirmatory.

The lower-order calculation is more selective. Under the already-owned W131
metric/Clifford-compatible connection assumptions, five apparently
independent remainders collapse exactly to two curvature maps. At the actual
W177 seeded gimmel point, using all ten
\(\operatorname{Sym}^2T^*X\) fibre coordinates, both are nonzero and the
\(S\to R\) curvature map has full column rank \(128\). Consequently the
current nine-block ansatz has no full-support gauge identity with
\(r_R\ne0\) at that background.

That is not a GU no-go. W177 is already known not to be a stationary
background for the conditional ambient Yang--Mills action. The result kills
this background/ansatz combination and generates a precise next demand:
either a source-selected compatible background with the required curvature
condition, or an action-generated curvature/gauge completion.

There is also a genuine positive construction. An exact
\(S\oplus I\) auxiliary gauge complex, with all nine carrier blocks present,
obeys the full formal identity on every compatible background. Layer 0 keeps
the gain honest: its gauge map has \(r_R=0\), so it does not yet gauge the
physical gamma-traceless Rarita--Schwinger field.

## Plain English

The previous swing showed that a very small family of geometric formulas can
touch all 20 field types. This swing asked the harder question: can those
formulas actually come from one indefinite quadratic action and possess a
gauge redundancy?

The answer is now split cleanly:

- **Yes at the action and leading-derivative level.** The indefinite pairing
  works, the reverse blocks close, and there are exact all-nonzero
  coefficient choices with a leading-order gauge direction.
- **Yes for a smaller auxiliary symmetry.** There is an exact symmetry
  mixing the spinor and gamma-image sectors on any compatible curved
  background.
- **Not yet for the physical spin-\(3/2\) sector at W177.** Curvature produces
  a concrete leftover map of full rank. It cannot be wished away by choosing
  the mass coefficient, because the curvature term and the mass bridge have
  different differential order.

This is the kind of negative result that helps a constructive program. It
does not say “the idea is impossible.” It says exactly what the present
action is missing, while banking the part that already works.

## Layer 0

| shared term | object computed here | object not identified with it |
| --- | --- | --- |
| Krein form | an invariant Hermitian form on the 128-spinor and the induced \(g\otimes K\) form on \(V\otimes S\) | a positive-Hilbert norm or a hand-entered phase on each observer slot |
| orthogonality | \(I=\operatorname{im}j\) orthogonal to \(R=\ker\Gamma\) inside \(V\otimes S\) | a proof that the separate \(S\) field must be orthogonal to the isomorphic \(I\) field |
| adjoint | compact-support formal adjoint under the displayed Krein form and Green identity | support transpose or a unique global closed realization |
| polarization | the graded symmetric/antisymmetric part of the quadratic kernel | the raw carrier operator \(D_{\mathbf c}\) |
| principal kernel | a nonzero vector in the coefficient matrix \(M(\mathbf h)\) | a Noether identity, a physical zero mode, cohomology, an index, or a generation count |
| full support | nonzero observer-complex projections in all 136 allowed cells | native phase closure, a domain theorem, or gauge closure |
| curvature obstruction | nonvanishing of the actual lower-order defect at one named local background | a background-independent GU no-go |
| auxiliary gauge complex | the exact \(r_R=0\) formal identity on \(S\oplus I\) | a gauge symmetry of \(R=\ker\Gamma\) |
| Majorana block | a fully typed bilinear, including domain, linearity, group and codomain | every construction carrying the same informal name |

The coarse pairing calculation is `SAME-OBJECT` with the program-native
Krein construction. Transfer to a normalized 20-slot coflip, a noncompact
closed domain, or physical four-dimensional fields remains `UNCERTAIN`.
The two previously juxtaposed `SA-Y8` “Majorana blocks” are `HOMONYM`.

## Construction fork

The result remains on the constructive GU branch:

\[
Y^{14}=\operatorname{Met}(X^4),\qquad
TY=TX\oplus\operatorname{Sym}^2T^*X ,
\]

with the actual ten symmetric metric directions, including the four
diagonal directions. It does not substitute the numerically equal but
structurally different \(\Lambda^2\oplus\Lambda^3\) comparator.

It uses:

- the `Cl(9,5)`/Krein keep-and-grade structure rather than replacing it by a
  positive-Hilbert quotient;
- the geometric gamma-traceless Rarita--Schwinger carrier rather than a
  ghost-subtracted standard gravitino;
- the bilinear action, with the pairing composed into the Hessian; and
- the W177 seeded metric only as a local actual-fibre discriminator, not as
  an assumed vacuum.

Every adverse verdict below is scoped to this construction and its named
background.

## 1. Native pairing and the honest multiplicity freedom

Write the spinor form as

\[
[s,t]_S=s^\dagger Kt,
\qquad
[\psi,\phi]_{VS}
=\psi^\dagger(g\otimes K)\phi .
\]

For the explicit `Cl(9,5)` realization, requiring every real Clifford
generator to be \(K\)-self-adjoint,

\[
\gamma_a^\dagger K=K\gamma_a ,
\]

fixes \(K\) up to one overall real scale. The Schur commutant gives the
uniqueness, and the resulting signature is

\[
\operatorname{sig}(K)=(64,64).
\]

Let

\[
\Gamma:V\otimes S\to S,\qquad
j=\frac1{14}\Gamma^\sharp_g,\qquad
P_I=j\Gamma,\qquad P_R=1-P_I .
\]

Then

\[
\Gamma^\times=\Gamma^\sharp_g,\qquad
j^\times=\frac1{14}\Gamma,\qquad
P_I^\times=P_I,\qquad P_R^\times=P_R .
\]

It follows, rather than being assumed, that

\[
I\perp_K R,\qquad
[js,jt]_{VS}=\frac1{14}[s,t]_S .
\]

The signatures are

\[
I:(64,64),\qquad
R:(832,832),
\]

and the canonical direct-sum form on
\(\mathcal E=S\oplus I\oplus R\) has signature

\[
\mathcal E:(960,960).
\]

The preregistered expectation that all three coarse summands would be forced
orthogonal was too strong. The separate \(S\) field and \(I\cong S\) have
the same Spin representation, so invariance alone permits a multiplicity
Gram matrix. After identifying \(I\) with \(S\) through \(\Gamma\), the most
general coarse form in this class is

\[
G_2=
\begin{pmatrix}
\alpha&\zeta\\
\bar\zeta&\beta/14
\end{pmatrix}
\]

on the \(S/I\) multiplicity space, with a separate nondegenerate \(R\)
factor. The canonical direct-sum choice is \(\zeta=0\); it is available but
not forced.

This correction does not destroy the nine-block construction. An arbitrary
\(2\times2\) block on \(S\oplus I\), the two natural bridges to and from
\(R\), and the \(RR\) block are still closed under the adjoint for every
nondegenerate \(G_2\). Fine observer-slot, coflip, and real-structure phases
remain open.

## 2. Formal adjoints and Green form

On the common compact-support core and in the no-\(i\) display convention,

\[
D_S^\times=-D_S,\qquad
D_V^\times=-D_V,\qquad
T^\times=\delta,\qquad
\delta^\times=T,\qquad
Q^\times=-Q .
\]

The normalized reverse-block identities include

\[
(D_S\Gamma)^\times=-14jD_S,\qquad
(jD_S)^\times=-\frac1{14}D_S\Gamma ,
\]

\[
(P_ID_VP_R)^\times=-P_RD_VP_I .
\]

An identity/mass block is self-adjoint at this algebraic grade. Thus the
formal adjoint of every written block is another one of the nine written
blocks. Polarization generates coefficient equations, not a new primitive
map.

For a region \(\Omega\), the local Green identity is

\[
\int_\Omega
\left([D_{\mathbf c}U,V]-[U,D_{\mathbf c}^{\,\times}V]\right)
=
\int_{\partial\Omega}
[\sigma_{D_{\mathbf c}}(\nu)U,V].
\]

This establishes the formal packet on
\(C_c^\infty(Y;\mathcal E)\). It does not choose a global realization.
On a compact collar, a conditional realization can be specified by a
maximal-isotropic boundary-trace subspace, additionally invariant under the
coflip. No source-owned noncompact asymptotic domain or preferred
maximal-isotropic trace condition is presently available. The fail-closed
five-field native packet therefore remains unadmitted at global-domain
grade.

The physical `-iD` convention is compatible with a self-adjoint kinetic
operator, but the associated action phase and real/Grassmann ordering must
be declared rather than silently inferred.

## 3. Graded polarization

Carry the grading sign explicitly:

\[
H_{\mathbf c}
=\frac12\left(D_{\mathbf c}+\sigma
D_{\mathbf c}^{\,\times}\right),
\qquad
H_{\mathbf c}^{\,\times}=\sigma H_{\mathbf c},
\qquad
\sigma\in\{-1,+1\}.
\]

The ordinary antisymmetric kernel is the candidate that survives on the
diagonal for one realified Grassmann-odd field. That points to
\(\sigma=-1\) once the native reality and ordering convention is fixed.
Independent \(\psi,\bar\psi\) doubling is a different field object, so the
probe preserves both branches rather than using the desired support to pick
one.

For polarized coefficients,

\[
\begin{aligned}
h_{IS}&=-\sigma\,14\,\overline{h_{SI}},\\
h_{RS}&=\sigma\,\overline{h_{SR}},\\
h_{RI}&=-\sigma\,\overline{h_{IR}},
\end{aligned}
\]

while

\[
h_a,h_d,h_q=-\sigma\,\overline{h_a,h_d,h_q},
\qquad
h_\mu=\sigma\,\overline{h_\mu}.
\]

Polarizing the fixed normalized \(RR\) first-order coefficient gives

\[
q=\frac{1-\sigma}{2}.
\]

Therefore:

- on the candidate odd branch \(\sigma=-1\), \(q=1\), the three diagonal
  first-order coefficients are real, and all nine blocks can remain
  nonzero;
- on the \(\sigma=+1\) branch, \(q=0\), so polarization erases the entire
  40-cell \(Q\) support family.

This is a planted discriminator, not a choice made to preserve the answer.
A symmetric ordinary matrix vanishes on a one-field Grassmann-odd diagonal
while an antisymmetric one contributes; the pattern reverses for an even
field.

## 4. The native determinant intersection

Use the normalized \(S/I\) coordinates \(U=(S,\Gamma I)\), and write

\[
\lambda=\frac{13}{14},\qquad \kappa=\frac67.
\]

The principal coefficient matrix retains the previous form

\[
M(\mathbf h)=
\begin{pmatrix}
h_a&h_{SI}&-\lambda h_{SR}\\
h_{IS}&-\kappa h_d&\frac{13}{7}h_{IR}\\
h_{RS}&\frac17h_{RI}&\kappa q
\end{pmatrix}.
\]

For the canonical coefficient metric

\[
G_3=\operatorname{diag}\left(1,\frac1{14},\frac{13}{14}\right),
\]

native polarization gives

\[
M^\dagger G_3=-\sigma G_3M.
\]

Consequently \(\det M\) is real for \(\sigma=-1\) and purely imaginary for
\(\sigma=+1\). In either branch \(\det M=0\) is one real equation, not one
complex equation.

On the candidate odd branch, set

\[
x=h_{SI},\qquad y=h_{SR},\qquad z=h_{IR},
\]

with \(a=h_a\) and \(d=h_d\) real. Then

\[
\det M=
\frac{-a(36d+13|z|^2)+39d|y|^2}{49}
-12|x|^2
-\frac{26}{7}\operatorname{Re}(xz\bar y).
\]

An exact all-nine-block, all-three-gauge-component witness is

\[
\begin{gathered}
a=1,\qquad d=\frac{79}{40},\qquad q=1,\\
h_{SI}=-1,\quad h_{IS}=-14,\quad
h_{SR}=2,\quad h_{RS}=-2,\\
h_{IR}=1,\quad h_{RI}=1,
\end{gathered}
\]

with

\[
r=(29,-140,91).
\]

Indeed,

\[
M=
\begin{pmatrix}
1&-1&-13/7\\
-14&-237/140&13/7\\
-2&1/7&6/7
\end{pmatrix},
\qquad
Mr=0
\]

exactly. A coefficient perturbation destroys that kernel vector, and the
zero vector is rejected.

The canonical odd family has eight real principal parameters. At a regular
point the determinant supplies one real constraint, leaving a
seven-dimensional prequotient locus. Its bare constraint surplus is

\[
1-8=-7.
\]

It is therefore non-confirmatory. Its value is that the independently
derived native pairing and polarization do not make the construction
impossible. Physical rephasing quotients and source-selected coefficients
have not been supplied.

## 5. Five lower remainders collapse to two curvature maps

Assume the W131 conditions: one metric/Clifford-compatible connection,

\[
\nabla\gamma=0,\qquad \nabla P_I=\nabla P_R=0 .
\]

The operator identities

\[
\Gamma D_V=-D_S\Gamma-2\delta,\qquad
\delta j=-\frac1{14}D_S
\]

collapse the five previously spanning remainders to

\[
\boxed{
\begin{aligned}
\mathcal C_S
 &=D_S^2-\nabla^a\nabla_a
   =\frac12\gamma^a\gamma^b\Omega_{ab},\\
\mathcal C_{II}&=0,\\
\mathcal C_{IR}&=-2j\mathcal C_S,\\
\mathcal C_{RI}&=0,\\
\mathcal C_{RR}
 &=P_R\bigl(\gamma^a\Omega_{ab}\bigr).
\end{aligned}}
\]

All five are thus curvature-zero-order. The separately written term

\[
\mu_0r_RT
\]

is first-order. For a genuine \(r_R\ne0\) operator identity, the current
family therefore requires \(\mu_0=0\) before any curvature cancellation,
unless the action generates another first-order lower block. A zero-order
curvature defect cannot cancel a first-order twistor map for all sections.

This is the first hardening demand generated by writing the action rather
than selected in advance.

## 6. Actual symmetric-fibre test at W177

The executable probe evaluates the two curvature maps at the W177 seeded
gimmel point. It uses all ten symmetric metric coordinates and the actual
\((9,5)\) orthonormal frame. Across three finite-difference scales:

| scale | scalar curvature | \(\|\mathcal C_S\|\) | Lichnerowicz defect | \(\|\mathcal C_{RR}\|\) | rank \(\mathcal C_{RR}\) |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 0.75 | \(-9.999998171\) | \(28.28426608\) | \(2.13\times10^{-5}\) | \(21.04320727\) | 128 |
| 1.00 | \(-10.000000618\) | \(28.28427299\) | \(1.29\times10^{-5}\) | \(21.04321084\) | 128 |
| 1.25 | \(-9.999999125\) | \(28.28426877\) | \(7.33\times10^{-6}\) | \(21.04320870\) | 128 |

The convention-sensitive Lichnerowicz control is

\[
\mathcal C_S+\frac{\operatorname{Scal}}4I_{128}\simeq0 .
\]

The \(R\)-valued map remains gamma-traceless,

\[
\|\Gamma\mathcal C_{RR}\|
<4.6\times10^{-15},
\]

and has full column rank \(128\) at every scale.

An earlier in-wave computation produced
\(\operatorname{Scal}\simeq-0.6404\) and
\(\|\mathcal C_{RR}\|\simeq15.8796\). It was voided before disposition:
W177's `orthonormal_frame` returns grouped \((+^9,-^5)\) columns, while the
factorized native gamma list uses interleaved \(4+10\) order. Contracting the
grouped curvature tensor with the interleaved gamma/sign list silently
compared different frame labels. Permuting the frame columns into native
gamma order—or equivalently using a grouped Clifford list—gives the table
above. A planted unpermuted interleaving must reproduce the rejected
numbers, so this convention error remains an executable hostile control.

It follows that the present all-nine-block gauge ansatz cannot have
\(r_R\ne0\) at this background:

- nonzero \(b_{SR}r_R\mathcal C_S\) obstructs the \(S\) equation;
- nonzero \(b_{IR}r_R\mathcal C_{IR}\) obstructs the \(I\) equation; and
- \(r_R\mathcal C_{RR}\) obstructs the \(R\) equation after the independent
  first-order \(\mu_0r_RT\) is set to zero.

The \(\sigma=+1\) polarization does not rescue full support: it removes
\(Q\) before this test.

Scope is essential. W177 is a local seeded gimmel metric and is already
nonstationary for the conditional ambient Yang--Mills action. This is a
background-specific/native-fork obstruction, not a theorem against all GU
backgrounds or all action completions.

## 7. An exact auxiliary gauge complex

The curvature identities also expose a branch that works exactly. On the
candidate odd polarization, take

\[
\begin{gathered}
a=-\frac3{49},\qquad
b_{SI}=\frac3{49},\qquad
b_{IS}=\frac67,\qquad
d=1,\\
b_{SR}=1,\qquad b_{RS}=-1,\qquad
b_{IR}=7,\qquad b_{RI}=7,\qquad q=1,
\end{gathered}
\]

and

\[
r=(1,1,0).
\]

Every carrier block is nonzero and all adjoint relations hold. The three
principal equations vanish exactly. Because
\(\mathcal C_{II}=\mathcal C_{RI}=0\) and every other lower remainder carries
\(r_R\), the full formal identity

\[
D^{(1)}R=0
\]

holds on every metric/Clifford-compatible background.

This is a serious construction: a compact-core auxiliary formal gauge
complex on \(S\oplus I\), not merely a symbol kernel. Contractibility,
cohomology, and nonlinear BV closure have not been proved. It is not the
desired physical closure because \(r_R=0\); the gauge map never transforms
the gamma-traceless \(R\) field.

## 8. Independent all-20 support hardening

The companion probe independently constructs 20 thin observer-complex
embeddings:

- four \(S\) factor-chirality slots;
- four normalized \(\operatorname{im}\Gamma\) slots;
- four low-\(R\) combinations fixed by gamma-tracelessness;
- four \(RS_4\otimes S_{10}\) slots; and
- four \(S_4\otimes RS_{10}\) slots.

It applies the intrinsic \(c,T,\delta,Q\) formulas before importing the
held-out representation ledger. No dense \(1792\times1792\) operator is
formed; the largest thin embedding is \(1792\times288\).

The result reproduces, cell for cell,

\[
68_{\rm base}+68_{\rm fibre}=136
\]

with per-block counts

\[
(8,8,16,8,8,16,16,16,40).
\]

The smallest nonzero projection is \(9.04\times10^{-2}\), the largest
nominal zero is \(1.42\times10^{-16}\), and the separation ratio is
\(6.35\times10^{14}\).

Planted controls for a wrong low-\(R\) sign, omitted \(X\) family,
one-chirality restriction, base-only/fibre-only \(Q\), collapsed provenance,
a deleted cell, an unknown one-character label, and a zero formula all fire.

This upgrades the earlier hand-entered analytic support manifest to an
independent observer-complex coordinate rederivation. It still does not
establish native Krein normalization, DeWitt-loop transport, a domain,
Noether closure, or BV nilpotency.

## 9. `SA-Y8`, `SA-Y1`, and the physical mass channel

The hostile Layer-0 rerun confirms that the existing `SA-Y8` owner's headline
is correct: the apparent contradiction is a homonym.

SHIAB-05 tests the existence of a complex-bilinear map on bare
14-dimensional Weyl spinors,

\[
\psi^TC\chi:S^\pm\otimes S^\pm\to\Lambda^0,
\]

with full Spin(9,5) equivariance, and finds that equivariant scalar channel
absent. The Seiberg--Witten moment map is a
sesquilinear/quadratic construction on a vector-spinor subspace, is only
\(SU(2)_\pm\)-equivariant after reduction, and is valued first in a
two-form/\(\mathfrak{su}(2)\) sector and then in an even endomorphism. Their
domains, linearity, symmetry group, and codomains differ. Neither one by
itself settles the physical four-dimensional Majorana/Yukawa channel.

Likewise, \(Kc(e_{\rm vertical})\) establishes a conditional algebraic
four-dimensional cross-chirality carrier. It does not yet prove an internal
singlet, a gauge-invariant action term, a retained \(X_4\) mode, or a
normalizable coefficient. The strongest current `SA-Y1` statement is:

```text
NO-EXTRA-T10-ALGEBRAICALLY-REQUIRED;
PHYSICAL-CHANNEL-IDENTIFICATION-OPEN
```

The constructive channel now worth writing is the odd-form bilinear

\[
B_v(\psi,\chi)=\psi^TC_{14}\Gamma(v)\chi,
\qquad v\in V_{10},
\]

including its Grassmann transpose symmetry and full 20-slot observer
decomposition. The question is not merely whether a \(10\) occurs in
\(16\otimes16\), but whether GU's supplied vertical mode furnishes and
transports the required datum with adequate covariance, stabilization, and
four-dimensional retention.

## Constraint-surplus account

The wave deliberately separates three different evidential grades:

| construction | constraints versus freedom | evidential reading |
| --- | --- | --- |
| 136-cell support | four linked primitive formulas, not 136 independently fitted amplitudes | strong expressibility/carrier result, not a fit surplus |
| native principal determinant | one real equation in eight real carrier parameters before quotient | feasible but non-confirmatory; surplus \(-7\) |
| exact \(r_R=0\) auxiliary identity | three principal equations plus all lower identities, with adjoint-linked coefficients and no curvature tuning | genuine formal construction, but on the auxiliary rather than physical gauge object |
| W177 \(r_R\ne0\) test | action-generated curvature maps evaluated without selecting a compensator | informative obstruction for this background/ansatz |

The lesson is not that shaped constructions teach nothing. The useful
question is whether independent demands exceed available freedom. This wave
banks the overdetermined exact auxiliary identity, refuses to oversell the
underconstrained determinant fit, and lets the actual action generate the
next physical demand.

## Science-council disposition

The parallel operator, source-action, and hostile branches converge on one
ordered disposition:

1. **Bank the formal source action.** The native Krein adjoints close within
   the nine blocks and the exact \(S\oplus I\) auxiliary complex is real
   progress.
2. **Do not promote the principal kernel.** It is a broad feasibility locus,
   not yet an explanation or gauge theorem.
3. **Keep the W177 obstruction.** It is a valid local counterexample to
   generic full-\(R\) closure and a discriminator for future completions,
   despite W177 not being a vacuum.
4. **Do not select a compensator yet.** First test whether source-selected
   curvature, IG/gauge curvature, or transport supplies the missing map.
5. **Preserve the physical-channel uncertainty.** The Krein vertical bridge
   removes one algebraic obstruction but does not by itself satisfy
   `SA-Y1` or `SA-Y8`.

No claim or canon status changes.

## Highest-information next sequence

The next construction wave should proceed in this order:

1. **Transport the actual 20 thin embeddings around the DeWitt loop.** Use
   the genuine vector/spin lift and the written
   \(\Gamma,j,P_R,D_{\mathbf c}\) intertwiners, then compute endpoint Schur
   scalars. Uniform \(-1\) closes the present P1/P2 weld; relative scalars
   measure the residual external datum. Plant an independent slot-phase
   twist that preserves static support but must fail transport.
2. **Write the vertical odd-form mass bilinear.** Compute
   \(B_v=\psi^TC_{14}\Gamma(v)\chi\) and the sesquilinear
   \(K\Gamma(v)\) comparator across all 20 slots, including Grassmann
   symmetry, internal stabilizer, and four-dimensional retention. This is
   the direct `SA-Y1`/physical-`SA-Y8` decider.
3. **Project the W177 curvature defect by observer slot.** Record the
   support and rank of \(\mathcal C_{RR}\), its zero-order scaling against
   the first-order \(\mu T\), a flat-curvature control, and a deliberately
   nonparallel-projector control.
4. **Search only action-generated absorbers.** Test a stationary/special
   curvature condition, an IG/gauge curvature contribution, or a curvature
   correction forced by the written source action. Do not add a free
   compensator because it cancels W177.
5. **Freeze the global packet only after transport.** Once coflip phases and
   the external datum are typed, construct one common maximal-isotropic or
   noncompact domain and rerun the fail-closed five-field contract.
6. **Only then advance to nonlinear BV closure.** Support saturation,
   principal kernels, and the auxiliary complex are insufficient substitutes
   for the physical \(R\)-sector Noether identity.

This sequence maximizes information gain because the first two steps test
whether GU's geometry actually supplies the datum that the source action
needs. The curvature-completion step is delayed until the construction has
earned its type.

## Scope and nonclaims

This wave does not establish:

- a source-selected global domain or normalized 20-slot coflip;
- a physical \(R\)-sector gauge symmetry;
- a stationary GU vacuum;
- a gauge-invariant or normalizable four-dimensional mass;
- nonlinear Noether closure, BV nilpotency, or a master equation;
- a preferred determinant root or compensator;
- a generation count or chiral-index result; or
- a global confirmation or refutation of Geometric Unity.

It does establish a materially stronger conditional step: the written
source action is formally coherent at native Krein grade, admits an exact
auxiliary gauge complex, and produces a sharply typed curvature obstruction
when asked to gauge the physical \(R\) sector on an actual symmetric-fibre
background.
