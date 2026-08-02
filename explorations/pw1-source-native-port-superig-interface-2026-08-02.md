---
title: "PW1 source/native port and mixed super-IG action interface"
status: active_research
doc_type: construction_result
updated_at: "2026-08-02"
run: "RUN-20260802-142051-gu-formalization-pw1-port-interface"
grade: "PW1 CONDITIONAL CONSTRUCTION PASS / PW2 ENABLED WITH THREE EXACT KILLS. The active native bundle extends canonically to the mixed-sign complex source bundle. A general source bundle first needs a moving quaternionic reduction J and then a separate compatible identification of that reduction with active P_nat; there is no canonical retraction or full real-form equivalence. Fixed projection is killed because coset fields return quadratically to native curvature. The full-unitary mixed Omega0+Omega1 bracket closes through the real-bilinear Krein square; the complex-bilinear symplectic comparator is killed by central iI. The forced one-half affine representation acts only on the algebraic odd coordinate; the physical-field map and written-action Ward identity remain open. P1/P2/P3 remain unchanged and unused."
---

# PW1 source/native port and mixed super-IG interface

## Result in plain English

The Eric-guided and independent-native constructions can meet, but not by
declaring their bundles equal and projecting one connection into the other.
The honest meeting interface has two stages: a **moving quaternionic
reduction** (J), followed by an isomorphism from that reduced bundle to the
already-active native bundle with its trace-reversed Clifford/soldering data.

Starting from the native
(Sp(32,32;\mathbb H)) bundle, extension to the mixed-sign complex
(U(64,64)) bundle is canonical. Starting in the other direction, a general
source bundle acquires some (Sp(32,32;\mathbb H)) reduction only if it admits
a compatible field (J). It becomes the active (P_{\rm nat}) only after the
second bundle/Spin/DeWitt/Clifford/soldering gate. The pointwise (J)-coset is
8128-dimensional; it is not P1, P2, or P3. The source (\epsilon) can locally
lift (J), so this remains a construction opportunity, not a request for a
new external datum.

The same swing also builds one exact meaning of Weinstein's “square root of
connections” language. On the full unitary source algebra, spinor-valued zero-
and one-forms admit a nonzero symmetric **real-bilinear Krein** bracket whose
value is a connection translation, and the algebraic affine action closes
only with coefficient (1/2). The tempting complex-bilinear symplectic route
works only on the centerless comparator: central (iI) kills it for
(U(64,64)). This is a real algebraic success. It does **not** yet identify
the algebraic odd coordinate with the physical field or prove that the GU action is
invariant under those transformations; PW2 must vary the complete action and
all its moving coefficients before that Ward identity can be evaluated.

## Layer 0: the objects are different

| Phrase | Object used here |
| --- | --- |
| source carrier | mixed-sign complex Krein (U(64,64)) bundle |
| native carrier | right-(\mathbb H), Krein (Sp(32,32;\mathbb H)) reduction |
| complexification | shared (M(128,\mathbb C)) container, not a real identification |
| real-form port stage 1 | a compatible moving (J)-field defining some (H)-reduction (P_H\subset P_{\rm src}) |
| active-native port stage 2 | an (H)-bundle isomorphism (P_H\simeq P_{\rm nat}) compatible with (Q\), trace-reversed DeWitt Clifford data, soldering, and transitions |
| algebraic odd generator | element of the underlying-real (S_{\mathbb R}\oplus(T^*Y\otimes S_{\mathbb R})) for the full-unitary bracket |
| physical odd field | the separately typed (\Omega^0(S_H)\oplus\Omega^1(S_H)) field |
| odd bracket closure | a Lie-superalgebra statement |
| Ward identity | a statement about the complete action, Euler covectors, and boundary current |
| datum | a priced residual choice, not a missing reduction, jet, or compensator |

The fibre metric throughout the native branch is the already-earned
trace-reversed Frobenius/DeWitt form. Nothing in PW1 replaces it with a raw
positive Frobenius product or with the exterior (6+4) “ten.”

## PW1-A — the actual port

Let

\[
G=U(64,64),\qquad H=Sp(32,32;\mathbb H),\qquad
J=C\circ\mathrm{conj},\quad J^2=-1.
\]

The native group is the fixed group (H=G^J). A native bundle therefore has
the canonical complex extension

\[
P_{\mathrm{mix}}=P_{\mathrm{nat}}\times_HG.
\]

The reverse operation is not a projection. Its first stage is an (H)-reduction
of an arbitrary source bundle (P_{\rm src}), equivalently

\[
J\in\Gamma(P_{\rm src}\times_GG/H).
\]

In the repository's passive overlap convention, the antilinear operator and
its linear coefficient transform differently:

\[
J_j=g_{ij}^{-1}J_i g_{ij},\qquad
C_j=g_{ij}^{-1}C_i\overline{g_{ij}}.
\]

The finite probe checks the coefficient law on three exact patches. It also
checks a source-legal central direction (iI) which fails fixed-(J) descent.
Globally, the lift from (BU(64)\times BU(64)) to
(BSp(32)\times BSp(32)) remains open. Vanishing of the odd Chern classes
(c_1,c_3,c_5,c_7) on both Krein-sign subbundles is a necessary screen on
(Y^{14}), not a sufficiency theorem. Even if it succeeds, the second stage
must identify (P_H) with
(P_{\rm nat}=Q\times_{Spin_0(9,5)}Sp(32,32;\mathbb H)) and preserve the
trace-reversed DeWitt Clifford representation, soldering, and transition
class. That actual-native gate remains open.

The source epsilon supplies a promising local construction:

\[
J_\epsilon=\epsilon^{-1}\circ J_0\circ\epsilon,
\qquad C_\epsilon=\epsilon^{-1}C_0\overline\epsilon.
\]

Here epsilon modulo (H) is a local lift of the reduction. This relates the
source epsilon to the repository's moving reduction; it does not identify the
two fields or prove that a global epsilon exists.

### Why fixed projection fails

Once the first-stage (J) reduction exists,

\[
\mathfrak u(64,64)=\mathfrak{sp}(32,32;\mathbb H)\oplus\mathfrak m_J,
\qquad p_J=\frac{1+\sigma_J}{2}.
\]

This is a reductive symmetric pair, not a quotient Lie algebra:

\[
[\mathfrak m_J,\mathfrak m_J]\subset\mathfrak h
\quad\text{and is generically nonzero.}
\]

Consequently a source connection must be written

\[
A=A_H+\Phi_J,\qquad
\Phi_J=\frac12(D_AJ)J^{-1},
\]

Using the convention
(F_A=dA+\tfrac12[A\wedge A]), its curvature splits as

\[
p_JF_A=F_{A_H}+\frac12[\Phi_J\wedge\Phi_J],\qquad
(1-p_J)F_A=D_{A_H}\Phi_J.
\]

The exact (U(2,2)/Sp(1,1)) witness has two coset matrices (X,Y) with
(p_JX=p_JY=0) but (p_J[X,Y]=[X,Y]\ne0). Thus the projected connection is
zero while the projected source curvature is nonzero. This kills the naive
action port. PW2 must carry (\Phi_J,D_{A_H}\Phi_J,[\Phi_J,\Phi_J]), or derive
the sector (D_AJ=0) from the action.

The moving projector contributes its own first-jet owner:

\[
\delta[p_JX]
=p_J(\delta X)+[\zeta,p_JX]-p_J[\zeta,X].
\]

Composing it with the moving spin projection sharpens the native B2C15P map to

\[
u(T;J,\epsilon)
=c_3\operatorname{Alt}(\operatorname{pr}^{J,\epsilon}_{\rm spin}T)
+c_{11}*\operatorname{Alt}(\operatorname{pr}^{J,\epsilon}_{\rm spin}T).
\]

The already-earned nonzero-pair rank remains (364), with kernel (910) and
full coset cokernel (7801). Symmetry still does not select (c_3:c_{11}).

### Exact real-form dispositions

- The positive (U(128)) fork cannot directly preserve the active noncompact
  group: an exact (Sp(1,1)) boost has real nonzero spectrum, incompatible
  with positive-definite skew-adjointness.
- Literal (Cl(7,7)) reality has (R^2=+1), whereas native quaternionic
  reality has (J^2=-1). A nonzero real-structure intertwiner would imply
  (T=-T).
- Both carriers complexify to (M(128,\mathbb C)), but this transports none of
  the reality, right-(\mathbb H), connection, action, or domain data.
- A reduced block route survives: the two metrics share
  (Spin(3,1)\times_{\mathbb Z_2}Spin(6,4)), dimension (51), and the vertical
  complex Wick map exactly relates the block metrics. Their full real ranks
  (7) and (5) remain different.

## PW1-B — square roots of connections, stated exactly

For the full unitary source algebra, write the algebraic odd carrier on the
underlying real spinor space as

\[
Q_{\rm alg}=S_{\mathbb R}\oplus(T^*Y\otimes S_{\mathbb R}),
\]

and keep it distinct from the physical field carrier

\[
Q_F=\Omega^1(S_H)\oplus\Omega^0(S_H).
\]

The complex symplectic comparator is

\[
\mu_\Omega(u,v)w=\Omega(u,w)v+\Omega(v,w)u.
\]

It lands in (\mathfrak{sp}(S,\Omega)), but it is not equivariant for the
full unitary source center: for (Z=iI), the adjoint action on the target is
zero while
(\mu_\Omega(Zu,v)+\mu_\Omega(u,Zv)=2i\mu_\Omega(u,v)\ne0).

The honest full-(U(K)) channel instead uses the real-bilinear Krein square

\[
M_K(u,v)=i\left(uv^\dagger K+vu^\dagger K\right)\in\mathfrak u(K)
\]

and the mixed bracket

\[
\beta_K((u,\psi),(v,\chi))(X)
=M_K(u,\chi(X))+M_K(v,\psi(X)).
\]

The probe verifies on the complete exact (\mathfrak u(2,2)) basis, including
its center, that (\beta_K) is symmetric, nonzero, real-bilinear,
Krein-skew-valued, and equivariant. It separately records the central kill of
the complex comparator.
It defines the source two-step superalgebra

\[
(\mathfrak u(K)\ltimes N_{\rm src})\oplus\Pi Q_{\rm alg},\qquad
[q,r]=(0,\beta_K(q,r)),\quad [N_{\rm src},Q]=0,
\]

with \(N_{\rm src}=\Omega^1(\operatorname{ad}P_{\rm src})\). After the first
reduction, \(N_H=p_JN_{\rm src}=\Omega^1(\operatorname{ad}P_H)\). Its affine realization acts on an
algebraic odd coordinate (\theta\in\Pi Q_{\rm alg}):

\[
R_q\theta=q,\qquad R_qA=\frac12\beta_K(q,\theta).
\]

The factor (1/2) is forced exactly by
([R_q,R_r]_+=R_{\beta_K(q,r)}); a planted (1/3) fails. The probe checks this
over the complete finite odd basis. It does not yet act on physical (\Psi):
that requires a constructed
(\iota_{\rm odd}:Q_{\rm alg}\to T_\Psi Q_F).

Because (\beta_K) is already Krein-skew, the first-stage conditional native
bracket is (\beta_H=p_J\beta_K). The probe finds it nonzero, Krein-skew,
(J)-linear, and equivariant under the complete fixed
(\mathfrak{sp}(1,1)) basis. Calling it the active native bracket still
requires the second (P_H\simeq P_{\rm nat}) stage. Variations must include
(Dp_J); omitting it would repeat PW1-A's fixed-projector error.

### The Ward boundary

If \(J\) is an independent field, the complete identity must include
\(\langle E_J,\mu_J\rangle\). If \(J=J_\epsilon\) is derived, the
\(D_\epsilon J,Dp_J\), and \(\Phi_J(A,J)\) returns must instead flow through
\(E_\epsilon\). The final owner is therefore a cases term, not both terms at
once:

\[
\mathcal W_q=
\langle E_A,\mu_A\rangle
+\langle E_g,\mu_g\rangle
+\langle E_\Psi,R_\Psi q\rangle
+\langle E_{\bar\Psi},R_{\bar\Psi}q\rangle
+\begin{cases}
\langle E_\epsilon^{\rm dir},\mu_\epsilon\rangle
+\langle E_J,\mu_J\rangle,&J\text{ independent},\\
\langle E_\epsilon^{\rm tot},\mu_\epsilon\rangle,&J=J_\epsilon,
\end{cases}
+d(\Theta_q-B_q),
\]

In the derived case, (E_\epsilon^{\rm tot}) means the direct epsilon Euler
covector plus the formal-adjoint chain returns through
(D_\epsilon J,Dp_J), and (D_\epsilon\Phi_J(A,J_\epsilon)). It is not a
second summand.

An exact independent-Euler **logical counterexample** makes one algebraic
owner contraction nonzero. It is not a Ward computation. Its meaning is
narrow but decisive: odd-algebra closure does not make an arbitrary action
invariant for free. The actual source-action verdict is `NOT_EVALUABLE`, not
“failed,” until PW2 supplies the full action graph, physical
(\iota_{\rm odd}), moving (J), (\Phi_J), every Euler owner, and the
boundary return.

## PW1-C — exact selector algorithm scaffold

PW1 adds a deterministic experiment-selection **algorithm scaffold**, not a
typed mathematical oracle or trained model. The candidate registry records
imported dispositions from named evidence. The current four response columns
are explicitly synthetic axes—`type`, `curvature`, `bracket`, and `affine`—not
responses of the six scientific candidates.

The selector greedily maximizes exact rational rank over those four axes and
uses stable tie-breaking. Its controls are visible `RESERVED_CONTROL` fixtures,
not sealed qualification data. A future prospective bank must be created only
after a freeze receipt binds the candidate/schema, discovery selection,
evaluation code, thresholds, and content digests. Rational reconstruction is
a future policy, not implemented here. No ML baseline is justified until PW2
provides the legal action graph and actual response-producing oracle.

## Source collision

- `SOURCE-CONFIRMS`: TOE `01:41:12–01:42:56` describes odd fields whose
  brackets return gauge-potential/connection translations. UCSD `00:46:02`
  and `00:49:16` place the relevant fields in spinor-valued zero- and
  one-forms. Portal material separates zeta/nu and the connection roles.
- `SOURCE-CORRECTS`: “square root of connections” fixes the algebraic target;
  it does not state an operator square, choose the bilinear channel, supply a
  Ward identity, or define a BV differential.
- `REPOSITORY-CONSTRUCTS`: the real-Krein bracket, the moving-(J) reduction
  interface, and the coset-curvature correction.
- `SOURCE-SILENT`: global (Y^{14}) reduction, its identification with active
  (P_{\rm nat}), the (J/\Phi_J) action, physical odd-field map, native
  Ward/BV closure, and the grade-3/11 coefficient ratio.

## Verification

- `pw1_source_native_real_form_superig_probe.py`: `61 exact + 6 planted = 67 PASS`.
- `pw1_typed_experiment_selection_probe.py`: `26 exact + 11 planted = 37 PASS`.
- B2C15P's exact native `Alt+*Alt` rank result is carried, not recomputed or
  promoted into a complete port.

## Post-construction hostile review protocol

Every major wave, including PW1, requires divergent specialist
pre-assessment and hostile specialist post-review. The post-review must attack
at least Layer 0, source attribution, real-form/descent, variational/Green/Ward
ownership, and test leakage. A wave is not complete until objections are either
repaired and rerun or recorded as a scoped open boundary.

PW1's three hostile lenses all return `PASS` after repairs. They forced the
two-stage active-native port, the central-(iI) complex-bracket kill and
real-Krein replacement, the complete underlying-real finite basis, mutually
exclusive (J/\epsilon) Ward ownership, the physical/algebraic odd-carrier
split, and the selector-scaffold demotion. No must-fix item remains.

## Nonclaims and next gate

P1/P2/P3 are unchanged and unused. PW1 is a conditional pass that enables
PW2; it is not an unconditional global-port completion. Curt remains formally separate inside the
Eric lane; `TG-1 AND TG-2 AND TG-3` remains `NOT_PROMOTED`. PW1 claims no global
reduction, written-action Ward identity, BV quotient, analytic domain,
Standard Model recovery, generation count, quantum theory, or cosmological
prediction.

PW2 is now the single rendezvous:

> construct the complete moving-(J), (\Phi_J), full-(j^1T),
> trace-reversed `Alt/K`, connection, curvature, Shiab, action, Euler, Green,
> Ward, and effective-order-two graph; then test whether the earlier nonzero
> response survives without an unowned coefficient.
