---
title: "PW2 full first-jet action graph and source-domain obstruction"
status: active_research
doc_type: construction_result
updated_at: "2026-08-02"
run: "RUN-20260802-152647-gu-formalization-pw2-first-jet-action"
grade: "PW2 EXACT AUTOMATIC-SOURCE-INTEGRABILITY OBSTRUCTION WITH CONDITIONAL FULL-JET/ORDER-TWO CERTIFICATES. Weinstein's written B_omega is epsilon-derived. The repository's projected (B,T)->(B+K,T-K) correction is therefore a source-coordinate reparametrization only if B+K remains in that epsilon gauge orbit. Exact Maurer-Cartan witnesses, including the PW1 U(2,2)/Sp(1,1) reduction, show that a flat full gauge displacement can acquire nonzero curvature after reductive projection, so reductive projection and affine descent do not prove source integrability. The actual native K_u on an admitted Y14 background is not evaluated. The earlier nonzero split response is retained as evidence for an explicit modified repository functional, not promoted as a reparametrization of the stated source action. Separately, PW2 proves that exterior dT does not own dK for a legal pointwise index-mixing comparator, reconciles an exact frozen polynomial graph by symbolic and independent dual-number differentiation, and certifies the complete C2 rank locus; native K_u factorization through Alt and the literal native Y14 coefficient remain open. PW3 is not enabled. P1/P2/P3 remain unchanged and unused."
---

# PW2 full first-jet action graph and source-domain obstruction

## Result in plain English

PW2 found the first obstruction **one step earlier** than the coefficient we
planned to calculate.

The promising repository correction moves a tensorial connection amount
(K) between two slots,

\[
(B,T)\longmapsto(B+K,T-K),
\]

so their sum stays fixed. That is a legal operation if (B) is an independent
connection. In Weinstein's written source coordinates it is not: the draft
defines

\[
B_\omega=\nabla_0+\epsilon^{-1}d_0\epsilon,
\qquad
T_\omega=\varpi-\epsilon^{-1}d_0\epsilon .
\]

Thus (B_\omega+K) must itself come from some new (\epsilon_K). Being a
well-transformed connection is not enough; it must remain in the specific
gauge orbit of the reference connection.

The exact PW2 witness shows why this fails as an automatic inference. A full
Maurer--Cartan displacement can be flat, while its reductive projection has
nonzero curvature because the discarded coset components return through
their bracket. That projected connection cannot be a gauge rotation of a
flat reference. The same return is replayed in PW1's exact
(U(2,2)/Sp(1,1)) finite reduction.

This does **not** kill the geometry. It tells us exactly what the next
construction must do: retain the unprojected gauge displacement and carry its
coset field, construct an integrability compensator, or openly enlarge the
action domain so (B) becomes independent and then rederive all Euler, Ward,
and Green owners. What it kills is calling the existing projected split a
substitution into Weinstein's stated action without one of those steps.

## Layer 0: the source graph and repository graph differ

| object | type | present status |
| --- | --- | --- |
| (\omega=(\epsilon,\varpi,g)) | source root coordinates | source explicit |
| (B_\omega) | gauge-rotated Levi--Civita/reference connection, derived from (\epsilon) | source explicit |
| (T_\omega) | tensorial difference between (\varpi) and the rotated reference | source explicit |
| (K_u) | repository-derived reduced connection difference | conditional same-bundle construction |
| (B_\omega+K_u) | an affine connection | exact abstract descent, but not thereby an (\epsilon_K)-rotation of (B_\omega) |
| (j^1T=(T,\nabla T)) | full Spencer first jet entering pointwise (K) | provisional owner pending native factorization |
| (j^2T\to j^1K) | holonomic prolongation required when curvature differentiates (K(j^1T)) | explicit dependency; native Euler/Green return open |
| (d_BT) | antisymmetric/exterior quotient of (j^1T) | insufficient to determine differentiated (K) |
| (J,p_J,\Phi_J,Dp_J) | moving source/native reduction data | PW1 conditional interface; source silent |
| (I_1^B) | written first-order source action | source explicit |
| (E,\Theta,\mathcal W) | Euler, Green/preboundary, and coupled Ward returns | distinct; physical packet open |

The fibre remains

\[
\operatorname{Sym}^2T^*X,
\qquad
D_h(k,\ell)=\operatorname{tr}(h^{-1}kh^{-1}\ell)
-\frac12\operatorname{tr}(h^{-1}k)\operatorname{tr}(h^{-1}\ell),
\]

with inertia ((6,4)). PW2 does not replace it by raw Frobenius geometry or by
the unrelated (\Lambda^2\oplus\Lambda^3) numerical “ten.”

## Three specialist pre-assessments

The required pre-pass converged on the same ordering from different angles.

1. **Covariant jet/reductive geometry:** use one derived-(J) branch, own the
   full Spencer jet, and prove a source-coordinate lift before varying the
   projected split. Its predicted first obstruction was generic failure of
   projected (K) to lie in the reference gauge orbit.
2. **Variational PDE/Ward--Green:** transpose one frozen root-field graph,
   return all derived-(J) terms to (E_\epsilon), and do not count a physical
   odd Ward identity before the source split and
   (\iota_{\rm odd}:Q_{\rm alg}\to T_\Psi Q_F) exist. Its predicted first
   obstruction was the symmetric (j^1T) owner.
3. **Exact AD/rank/statistics:** compare independent exact derivative engines
   owner by owner, certify generic rank by minors rather than samples, and use
   ML only to schedule exact fixtures. Its predicted stop was the active port
   or full-jet owner, not a missing fitted coefficient.

The source-coordinate gate was therefore run before a native rank claim.

## PW2-A: the projected displacement is not automatically source-integrable

Let a reductive symmetric pair split

\[
\mathfrak g=\mathfrak h\oplus\mathfrak m,
\qquad [\mathfrak m,\mathfrak m]\subset\mathfrak h.
\]

At one point, prescribe the Maurer--Cartan jet

\[
\omega_x=X,\quad \omega_y=Y,\quad
d\omega_{xy}=-[X,Y],
\]

with (X,Y\in\mathfrak m) and ([X,Y]\ne0). The full connection
displacement is flat:

\[
d\omega+[\omega,\omega]=0.
\]

But (K=p_{\mathfrak h}\omega) has (K_x=K_y=0) at the point and

\[
F_K=p_{\mathfrak h}(d\omega)+[p_{\mathfrak h}\omega,
p_{\mathfrak h}\omega]=-[X,Y]\ne0.
\]

So projection has removed exactly the coset bracket that made the full
Maurer--Cartan connection flat. If the reference (B) is flat, (B+K) cannot be
another gauge rotation of (B).

The probe runs this twice:

- in a transparent diagonal/off-diagonal symmetric pair; and
- in PW1's exact mixed-sign (U(2,2)/Sp(1,1)) reduction, using the already
  established coset matrices whose bracket returns nontrivially to the
  quaternionic fixed algebra.

This is a counterexample to the **automatic** source-lift claim. It does not
evaluate the actual native (K_u), prove that an admitted flat reference exists
on the literal (Y^{14}) background, or forbid the modified covariant
functional (I'(\epsilon,\varpi)=I(B+K,T-K)). It changes the burden: a
source-coordinate reparametrization must prove the Maurer--Cartan/integrability
equation on its selected locus; a modified functional must be labelled an
extension and have its Euler, Green, and Ward packet rederived.

The local infinitesimal positive control also passes: an honest
(K=D_B\zeta) tangent at a flat reference has zero linearized curvature. This
is a point-jet control, not a global epsilon-existence or holonomy theorem.
The probe therefore distinguishes a local gauge tangent from a generic
projected connection difference without claiming global descent.

## PW2-B: exterior (dT) does not own a general differentiated (K)

Two affine holonomic germs are constructed with the same value of (T) and the
same exterior derivative

\[
\partial_xT_y-\partial_yT_x=1,
\]

but different symmetric cross derivatives

\[
\partial_xT_y+\partial_yT_x=1\quad\text{and}\quad3.
\]

For a legal pointwise index-mixing comparator

\[
K_x=T_x,\qquad K_y=-T_y,
\]

the differentiated connection return is

\[
dK_{xy}=-(\partial_xT_y+\partial_yT_x),
\]

so the two germs give (-1) and (-3). Therefore (d_BT) does not determine
(dK) for general pointwise index mixing, even on holonomic germs. This makes
the full (j^1T) and its formal-adjoint Green return provisional required
owners. The literal native (K_u) could evade the burden only if its actual
port is proved to factor through the exterior/Alt quotient; that factorization
is `OPEN`, not refuted by this comparator.

The same probe verifies a live moving-projector derivative

\[
\dot p_J(X)=[p_JX,\zeta]-p_J[X,\zeta]\ne0,
\]

and the nonzero coset-curvature return. Freezing (p_J) is not a harmless
coordinate simplification.

## PW2-C: exact derivative and complete order-two certificate

A frozen polynomial dependency graph with (K=Z_0T+Z_1\partial T) is
differentiated two independent ways:

- symbolic component differentiation; and
- an exact `Fraction` dual-number forward-mode implementation.

The action value, full directional derivative, and all six separate
**jet-coordinate partial derivatives** agree exactly. Because the scalar
graph has (K=Z_0T+Z_1\partial T) and (dK) contains
(Z_1\partial^2T), its honest dependency is the holonomic prolongation

\[
j^2T\longrightarrow j^1K.
\]

The AD packet is therefore not an Euler--Lagrange or Green packet. A complete
first variation must integrate the (\delta\partial^2T) term twice, producing
two nested boundary layers before naming the bulk Euler covector. Those steps
remain unassembled. This is an experiment-harness certificate, not an
identification of the scalar graph with the native Shiab action.

For

\[
A=A_2\partial^2+A_1\partial+A_0,
\qquad Z=Z_1\partial+Z_0,
\]

the probe verifies by direct application to an arbitrary two-vector function

\[
C_3=A_2Z_1,
\qquad
C_2=A_2(2\partial Z_1+Z_0)+A_1Z_1,
\]

along with the complete lower coefficients. Its exact family has

\[
C_3=0,
\qquad C_2(r)=\begin{pmatrix}-r&0\\0&0\end{pmatrix}.
\]

Thus the generic rank is one on (D(r)) and zero on the exceptional locus
(V(r)). The certificate is algebraic: the pivot minor is (-r) and every
(2\times2) minor vanishes. At (r=0), the abbreviated (A_2Z_0) block still has
rank one while the complete (C_2) is zero because the
(2A_2\partial Z_1) and (A_1Z_1) terms cancel it. This exactly catches the
shortcut that motivated PW2.

The product-rule identity

\[
\partial(A_2Z_1)=(\partial A_2)Z_1+A_2\partial Z_1=0
\]

also has two individually nonzero terms. It is the finite warning for moving
Hodge, density, Krein lowerer, frame, (p_J), and Shiab coefficients.

## What happened to the earlier nonzero action response?

It remains real evidence, but its type is narrower.

B2C15R3 showed that a declared finite split can change an action without a
new coefficient. PW2 shows that this does not yet make the split a path in the
source field space. The earlier result is therefore reclassified as:

> a nonzero response of a repository extension/conditional independent-(B)
> action, pending a source-coordinate lift.

That is not a retraction of the calculation. It is the Layer-0 correction
needed before calling it Weinstein's action.

## Source collision

- `SOURCE-CONFIRMS`: draft Section 9.1 defines the action on
  (\omega=(\epsilon,\varpi)) and the metric; it gives
  (B_\omega=\nabla_0+\epsilon^{-1}d_0\epsilon),
  (T_\omega=\varpi-\epsilon^{-1}d_0\epsilon), and the fixed
  (1/2,1/3) transgression grammar.
- `SOURCE-CONFIRMS`: the draft and TOE (`00:26:28--00:29:16`) use the
  trace-reversed Frobenius fibre. The 2025 TOE contorsion discussion
  (`02:19:17--02:20:33`) confirms that the gauge-rotated Levi--Civita
  connection is distinguished. The source-lift/no-free-reparametrization
  burden is PW2's inference, not a quotation from that passage.
- `SOURCE-CORRECTS`: a projected connection displacement is not
  automatically a source-coordinate reparametrization merely because the
  unprojected displacement is gauge generated. Affine descent is weaker than
  membership in the reference gauge orbit. This is deliberately narrower
  than declaring a global source variation-domain enumeration: the earlier
  tau-source locator correctly warns that the draft does not lock every
  held-fixed/varied field-space convention.
- `SOURCE-CORRECTS`: (\Xi=D_\omega\Upsilon) is a displayed redundancy target,
  not the missing off-shell coupled Ward identity; Shiab is a contraction,
  not (p_J) or a bundle projection.
- `SOURCE-SILENT`: an integrable projected (K), a compensating coset field,
  an independent-(B) extension of the action, moving (J/\Phi_J/Dp_J), the
  active source/native bundle identification, literal native Alt, and the
  physical odd-field map.

## Verification

- `pw2_full_first_jet_action_graph_probe.py`: exact source-domain,
  (U(2,2)/Sp(1,1)) reductive-return, moving-projector, Spencer-jet, and
  trace-reversal gates.
- `pw2_symbolic_ad_rank_strata_probe.py`: exact symbolic/dual-number
  jet-coordinate agreement, full operator composition, moving-coefficient
  product rule, and generic/exceptional rank certificate. It does not claim
  the twice-integrated Euler/Green packet.
- Every approximate/ML role remains scheduling-only. No selected sample is
  counted as proof or constraint surplus.

## Hostile post-review

Three independent hostile lenses return `PASS` after repairs.

- The source/reductive-geometry lens replaced a Euclidean trace mnemonic with
  the exact Lorentzian ten-dimensional Gram, proving trace-reversed inertia
  ((6,4)) against unreversed ((7,3)); it also required the actual native
  (K_u) and admitted literal (Y^{14}) background to remain `NOT_EVALUATED`.
- The variational lens inserted the (j^2T\to j^1K) prolongation, demoted the
  dual-number packet to jet-coordinate partials, and kept the twice-integrated
  Euler and two Green boundary layers open.
- The provenance/evidence lens reconciled the source variation-domain warning,
  separated TOE's distinguished-reference statement from PW2's inference,
  propagated PW2A across the campaign, and corrected the probe inventory.

Final reruns pass: `38 exact + 7 planted = 45`,
`27 exact + 8 planted = 35`, and the campaign scaffold passes with all PW1/PW2
review receipts and live hostile mutations. No must-fix item remains.

## Boundary and next gate

PW2 returns the smallest exact obstruction allowed by its preregistration:
automatic source integrability is false in the exact reductive comparator.
The actual native (K_u) and an admitted literal (Y^{14}) background remain
`NOT_EVALUATED`, so PW2 does not enable PW3. The physical odd Ward identity
remains `NOT_EVALUABLE`, not failed. P1/P2/P3 are unchanged and unused: none
has the type of an (\epsilon_K) lift, a continuous compensator, a jet owner,
or a bundle isomorphism. Curt remains formally separate inside the Eric lane, and
`TG-1 AND TG-2 AND TG-3` remains `NOT_PROMOTED`.

The next construction gate is:

> **PW2A — source-legal moving-reduction lift.** Compare, without fitting:
> (1) the full unprojected gauge displacement with its coset field retained;
> (2) a derived compensator that restores the Maurer--Cartan equation after
> projection; and (3) an explicitly extended action with independent (B).
> Require source descent, moving (J), trace-reversed native compatibility,
> and complete Euler/Green/Ward ownership. Then rerun the literal native
> full-jet and order-two calculation.

No BV quotient, analytic domain, Standard Model recovery, generation count,
quantum theory, cosmological prediction, or dark-sector claim is made.
