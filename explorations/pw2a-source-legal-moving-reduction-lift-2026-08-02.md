---
title: "PW2A abstract co-moving gauge lift and action-extension comparison"
status: active_research
doc_type: construction_result
created: 2026-08-02
branch: agent/null-clifford-omega1-repair
run: private orchestration runtime#meta/runs/historical-investigation/run-plan.md
registry: lab/process/pw2a-source-legal-moving-reduction-lift.json
experiment_registry: lab/process/pw2a-action-extension-experiment-registry.json
probes:
  - tests/channel-swings/pw2a_source_legal_moving_reduction_lift_probe.py
  - tests/channel-swings/pw2a_variational_extension_green_probe.py
grade: "PW2A ABSTRACT LOCAL CO-MOVING GAUGE-LIFT PASS WITH A FORCED COSET-CURVATURE RETURN AND A FIXTURE-SCOPED INDEPENDENT-B VARIATIONAL CONTROL. An exact GL(2) principal-bundle chart proves the co-moving mechanism: B and T move oppositely, their total stays fixed, nonzero-background curvature transforms by conjugation, and a generic linear involution remains covariantly compatible. This is source-shaped but not yet a literal source-H or Y14 lift. PW2's frozen-reduction obstruction survives. The curvature-level compensator is the discarded coset bracket with coefficient one and is not a new datum or connection one-form. At flat linearized grade an h-valued connection repair has H2 obstruction and H1 ambiguity; on curved backgrounds ordinary cohomology is unavailable until a deformation complex exists. A polynomial independent-B fixture verifies live D_BK/D_TK adjoints, an attainable fourth-order Euler term, and both Green layers; a derivative-affine control instead drops to order two. A separate nonvacuous Ward comparator passes, while the root-extension and physical Ward identities remain unevaluated. Literal source-group membership, admitted epsilon variation, nested active reductions, complete action order, BV quotient, and domain remain open. P1/P2/P3 are unchanged and unused; PW3 remains blocked."
canon_verdict_change: none
---

# PW2A abstract co-moving gauge lift

## Result first

PW2A found the highest-information candidate mechanism around PW2's
obstruction without adding a new datum or promoting the
independent-connection rival. The theorem earned here is abstract and
source-shaped; the literal GU source lift remains the PW2B gate.

The failed PW2 move projected a genuine gauge displacement against an old,
fixed reduction and then asked the projected connection to remain in the
source gauge orbit. That is not generally true. The corrected construction
moves the source coordinate and the reduction together:

\[
\epsilon' = \epsilon g_u,
\qquad
J' = g_u^{-1}J_\epsilon g_u,
\qquad
\varpi'=\varpi .
\]

The source definitions then give

\[
B_{\epsilon'}=B_\epsilon+K_{\rm full},
\qquad
K_{\rm full}=g_u^{-1}D_{B_\epsilon}g_u,
\]

\[
T_{\epsilon'}=T_\epsilon-K_{\rm full},
\qquad
B_{\epsilon'}+T_{\epsilon'}=B_\epsilon+T_\epsilon .
\]

In the exact local construction, the moved connection and moved reduction
satisfy

\[
D_{B_{\epsilon'}}J'=0,
\qquad
F_{B_{\epsilon'}}=g_u^{-1}F_{B_\epsilon}g_u .
\]

In an abstract principal bundle, the old-frame coset is not automatically a new field. It is the visible
motion of the reduction in a frame that was incorrectly held fixed. Keeping
that motion restores the bracket term that PW2 lost.

This is an abstract local gauge-lift theorem in a finite \(GL(2)\) chart. It
is not yet a source-coordinate reparametrization, gauge equivalence, or
admissible variation of the written action. Those stronger statements require
the distortion-derived \(g_u=\exp u(T)\) to be source-group-valued, descended,
smooth and domain-preserving, and locally invertible where the field-dependent
map needs an inverse. The source packet also leaves the complete admissible
\((\epsilon,\varpi)\) tangent policy undeclared.

## Plain English

The abstract failure mechanism rotates the connection and then measures it
using the old coordinate frame. PW2A rotates the frame with it.
Once that is done in the structural chart, the full connection obeys the same
gauge-rotation law as Eric's distinguished object, the distortion changes by
the opposite amount, and their total is unchanged. PW2B must prove that the
actual grade-3/11 \(g_u\) implements this mechanism in Eric's source group.

The apparent “missing compensator” is mostly the part of the same rotation
that the frozen frame threw away. At curvature level its size is fixed; there
is no coefficient to tune and no external bit to spend. If we insist on a
new connection that lives entirely in the old reduced algebra, that becomes a
different and harder problem: solve a nonlinear differential equation with
global and boundary choices.

The independent-\(B\) route remains useful as an engineering control. We now
know exactly how its higher-derivative Euler and boundary terms work in a
nontrivial structural model. But it adds an entire connection field and is
not what Eric's written source coordinates presently say.

## Layer 0: three meanings that had been mixed

| object | type | PW2A disposition |
| --- | --- | --- |
| \((\epsilon,\varpi)\) | source root coordinates | source explicit |
| \(B_\epsilon\) | connection derived from \(\epsilon\) | source explicit |
| \(T_\epsilon\) | tensorial difference \(\varpi-(B_\epsilon-\nabla_0)\) | source explicit |
| \(K_{\rm full}=g_u^{-1}D_Bg_u\) | full gauge displacement | abstract theorem; source-admissible candidate conditional on source-group membership and domain |
| \(p_JK_{\rm full}\) | projection against the old reduction | not automatically source-integrable |
| \(J'=g_u^{-1}Jg_u\) | transported generic linear involution in the finite chart | exact abstract construction, not the literal quaternionic or Clifford reduction |
| old-frame \(\Phi\) | discarded coset connection component | derived reduction motion in the co-moving route |
| \(Q_\Phi=\tfrac12[\Phi\wedge\Phi]_{\mathfrak h}\) | curvature two-form return | coefficient forced; not a connection |
| \(c\in\Omega^1(\mathfrak h)\) | proposed connection compensator | new nonlinear PDE/domain problem |
| independent \(B\) | new action field | honest repository extension, not source-selected |
| P1/P2/P3 | orientation/count/KO datum ledger | wrong type for every continuous repair above |

The finite chart uses a **linear** involution \(J_0^2=+1\). It is not PW1's
**antilinear quaternionic** reduction \(J_{\mathbb H}^2=-1\). The
infinitesimal \(U(2,2)/Sp(1,1)\) replay is a mixed-sign control, not a finite
upgrade of the \(GL(2)\) chart.

The actual nested reductions are:

1. \(J_{\mathbb H}\) for
   \(U(64,64)/Sp(32,32;\mathbb H)\); and
2. a Clifford-plane reduction \(Q_{\rm Cl}\), also called the repository
   \(\epsilon_{\rm red}\), for
   \(Sp(32,32;\mathbb H)/Spin_0(9,5)\).

The intended grade-3/11 \(g_u\) lies in the quaternionic \(Sp\), so it should
stabilize \(J_{\mathbb H}\) while moving \(Q_{\rm Cl}\). PW2A has not built
that stage-two transport. This preserves B2C15P/Q's homonym warning: the
source \(\epsilon_H\) and the repository \(\epsilon_{\rm red}(T)\) are not
identified by shared notation.

The geometric carrier remains

\[
\operatorname{Sym}^2T^*X,
\qquad
D_h(k,\ell)
=\operatorname{tr}(h^{-1}kh^{-1}\ell)
-\frac12\operatorname{tr}(h^{-1}k)\operatorname{tr}(h^{-1}\ell),
\]

with fibre inertia \((6,4)\) and total active signature \((9,5)\). Raw
Frobenius gives the wrong \((7,3)\) fibre, and Curt's formally separate
\((7,7)\) carrier is not substituted here.

## Three divergent specialist pre-assessments

The pre-pass changed the order of work before construction.

1. **Reductive connection geometry** recommended composing the existing
   source-shaped \(\epsilon\) composition, separating both nested reductions, and testing the
   curvature conjugacy identity before projecting. It predicted that the
   full route could also lower the apparent derivative order.
2. **Variational bicomplex and PDE** separated two branches: an independent
   old-frame coset field has its own Euler owner, while a transported
   reduction returns all \(J/p_J/\Phi_J\) variation to
   \(E_\epsilon^{\rm tot}\). It required an independent-\(B\) rival to pay
   for its field and both Green layers.
3. **Exact algebra, Spencer, and cohomology** distinguished the algebraic
   curvature return from a connection-level inverse problem. It predicted
   that full Maurer--Cartan cancellation could remove nominal Hessian terms,
   while an \(\mathfrak h\)-only repair would require a right inverse,
   cohomology, holonomy, and boundary data.

All three ranked the co-moving full-lift candidate first, independent \(B\) as a
controlled rival, and a new \(\mathfrak h\)-only compensator last.

## PW2A-A: exact abstract local co-moving gauge lift

The executable chart uses \(GL(2)\), not the literal GU source group:

\[
g(x,y)=(1+xE_{12})(1+yE_{21}),
\qquad
\omega=g^{-1}dg .
\]

Every expression is polynomial and rational. Direct differentiation gives

\[
d\omega+\omega\wedge\omega=0.
\]

With a fixed structural \(\varpi\), define

\[
B'=\omega,
\qquad
T'=\varpi-\omega .
\]

The probe verifies componentwise that \(B'+T'=\varpi\). With
\(J_0=\operatorname{diag}(1,-1)\) and
\(J'=g^{-1}J_0g\), it also verifies

\[
(J')^2=1,
\qquad
dJ'+[B',J']=0 .
\]

Freezing \(J_0\) instead leaves a nonzero covariant derivative. This is why
the abstract co-moving mechanism avoids the fixed-projection failure; it is
not yet a proof that the literal nested GU reductions do so.

The finite \(J_0\) check is a generic moving-reduction mechanism only. It
does not transport \(J_{\mathbb H}\) or \(Q_{\rm Cl}\). The theorem is also
deliberately local. A flat \(U(1)\) connection on a circle
with half-integral holonomy supplies the planted global control: zero
curvature does not imply membership in the trivial global gauge orbit.

## PW2A-B: what the compensator actually is

For a symmetric reductive split
\(\mathfrak g=\mathfrak h\oplus\mathfrak m\), write

\[
\omega=K+\Phi .
\]

The \(\mathfrak h\) curvature equation is

\[
0=F_K+\frac12[\Phi\wedge\Phi]_{\mathfrak h}.
\]

In two-form component convention this is

\[
0=F_{K,xy}+[\Phi_x,\Phi_y]_{\mathfrak h}.
\]

The exact \(2\times2\) chart has

\[
F_{K,xy}=-[E_{12},E_{21}],
\qquad
[\Phi_x,\Phi_y]_{\mathfrak h}=[E_{12},E_{21}] .
\]

Putting an unknown coefficient \(\lambda\) on the second term leaves
\((\lambda-1)[E_{12},E_{21}]\), so \(\lambda=1\) is forced. The exact
\(U(2,2)/Sp(1,1)\) replay gives the same full/projected/completed pattern.

That is useful construction, but it is a curvature identity, not a new
connection. An \(\mathfrak h\)-valued one-form \(c\) intended to make the
old projected connection integrable must instead solve schematically

\[
D_{B+K}c+\frac12[c\wedge c]
=\operatorname{Ad}_{g^{-1}}F_B-F_{B+K}.
\]

At linear flat grade this becomes \(D_Bc=R\) with \(D_B^2=0\). The
obstruction is \([R]\in H^2_{D_B}\) and the solution ambiguity is
\(H^1_{D_B}\), together with global holonomy and boundary data. On a curved
background, \(D_B^2=\operatorname{ad}(F_B)\), so ordinary \(H^1/H^2\)
language is unavailable until a deformation complex is constructed. Any
chosen Green/right inverse and its domain must be owned. No such choice is
supplied by P1/P2/P3 or the source passage.

## PW2A-C: derivative-order correction

Naively differentiating \(K_{\rm full}(j^1T)\) produces second derivatives of
\(T\). In the exact full gauge lift, the differentiated and quadratic
curvature pieces are separately nonzero but cancel:

\[
d(g^{-1}dg)+(g^{-1}dg)\wedge(g^{-1}dg)=0.
\]

More generally the nonzero-background probe verifies

\[
D_BK_{\rm full}+\frac12[K_{\rm full}\wedge K_{\rm full}]
=\operatorname{Ad}_{g^{-1}}F_B-F_B.
\]

This proves an order drop for the **curvature of the abstract full gauge
lift**. It corrects PW2's provisional assumption that every candidate route
must retain the generic \(j^2T\to j^1K\) curvature burden.

It does not yet prove the order of the complete written first action. The
\(T\)-prefactor, \(d_BT\), moving Shiab, Hodge, density, Krein lowerer,
projectors, and nested reduction maps must all be substituted before deciding
whether every Hessian cancels. That literal calculation is the highest-value
next gate.

## PW2A-D: independent-B variational control

The independent-\(B\) route was not dismissed. PW2A constructs an exact
structural action comparator with

\[
\widehat B=B+K,
\qquad
\widehat T=T-K,
\qquad
K=Z_BB+Z_0T+Z_1DT .
\]

Writing

\[
R_K=E_{\widehat B}-E_{\widehat T},
\]

direct differentiation agrees exactly with the pulled owner equations

\[
E_B=E_{\widehat B}+(D_BK)^!R_K,
\qquad
E_T=E_{\widehat T}+(D_TK)^!R_K .
\]

Both \(D_BK\) and \(D_TK\) returns are live in the executable polynomial
fixture. Its second-order scalar density reaches fourth jet and satisfies

\[
E_T=L_T-D(L_{DT})+D^2(L_{D^2T}).
\]

The complete Green current has two live layers,

\[
\Theta_T
=\bigl(L_{DT}-D L_{D^2T}\bigr)\,\delta T
+L_{D^2T}\,D(\delta T).
\]

A derivative-affine control removes the non-source quadratic
\((D\widehat B)^2\) term. It still depends on the second \(T\)-jet, but its
Euler expression drops exactly to order two in this fixture. Fourth order is
therefore **attainable in the polynomial control, not forced for Weinstein's
written derivative-affine action**.

A separate gauge-invariant comparator for \(q=DT+B\) verifies the nonvacuous
coupled identity

\[
-D E_B-E_T=0,
\]

while both summands are nonzero. The structural \(K\) used for the
higher-derivative test is intentionally not passed off as the native
gauge-natural map, so the physical Ward identity remains conditional.

The Ward comparator is separate from the root split action; the root-extension
Ward identity is `NOT_EVALUATED`. The result is a fixture-scoped engineering
certificate for the tested independent-\(B\) grammar. It is not source
selection. An unconstrained independent \(B\)
adds a connection-sized functional field; a constrained parent action would
also add its multiplier, constraint, and BV/domain owners.

## Source collision

- `SOURCE-CONFIRMS`: draft Section 9.1 defines the source coordinates
  \((\epsilon,\varpi)\), the derived \(B_\omega\), the tensorial
  \(T_\omega\), and the fixed \(1/2,1/3\) transgression grammar.
- `SOURCE-CONFIRMS`: TOE `02:19:17--02:20:33` identifies the gauge-rotated
  Levi--Civita object as the GU replacement in the contorsion slot and then
  continues to the tilted double-coset construction.
- `SOURCE-CONFIRMS`: TOE `00:26:28--00:29:16` and the draft require trace
  reversal on the ten-dimensional symmetric fibre.
- `SOURCE-CORRECTS`: the source \(B_\epsilon\) is the full gauge-rotated
  connection, not a frozen-reduction projection \(p_JK\).
- `SOURCE-SILENT`: the exact co-moving \(g_u\) construction, the
  distortion-derived \(g_u\), admitted epsilon-variation policy, nested
  reduction transport, global and literal active-native descent, the
  coefficient-one coset theorem, complete action order drop, an
  \(\mathfrak h\)-only compensator PDE, independent \(B\), the physical
  Ward/BV quotient, and the analytic domain.
- `REPOSITORY-DERIVED`: the abstract \(GL(2)\) co-moving theorem and
  nonzero-background curvature-conjugacy fixture; the coefficient-one coset
  return and its degree distinction; and the warning that
  \(\Xi=D_\omega\Upsilon\) is not silently the complete off-shell Ward
  identity.

The new local theorem is repository-derived mathematics. The transcript
selects the object type; it does not supply this proof.

## Constraint and datum ledger

| route | new continuous freedom | current constraint surplus |
| --- | --- | --- |
| derived co-moving \(g_u\) | no new field if \(u(T)\) is the existing map; existing \(c_3:c_{11}\) remains | uncomputed until literal port and physical quotient |
| forced \(Q_\Phi\) | one temporary scalar \(\lambda\), fixed to one by one independent equation | algebraic surplus \(1-1=0\); \(\lambda\) is identifiable with zero residual freedom, not positive surplus |
| independent connection compensator \(c\) | connection field or right-inverse/domain/zero-mode choices | uncomputed and presently unfavorable |
| independent \(B\) extension | connection-sized field plus possible multiplier/BV sector | uncomputed pending gauge quotient |

P1/P2/P3 remain unchanged and unused. None is a gauge transformation,
moving reduction, connection one-form, Green operator, holonomy trivializer,
or boundary condition.

## Verification

- `pw2a_source_legal_moving_reduction_lift_probe.py` verifies the exact
  abstract composition, fixed total connection, generic moving-involution compatibility,
  full and reductive Maurer--Cartan equations, forced coefficient-one return,
  mixed-sign replay, curvature order drop, holonomy control, trace reversal,
  source collision, and anti-datum plants.
- `pw2a_variational_extension_green_probe.py` verifies the independent-\(B\)
  root/pulled Euler chain with live \(D_BK/D_TK\), attainable fourth-order
  term, derivative-affine order-two control, exact formal adjoint, both Green
  layers, separate nonvacuous Ward comparator, field debit, and native
  nonpromotion. Root-extension Ward remains unevaluated.

No statistical or ML result is used. The fixtures were selected by exact
type discrimination and every verdict is symbolic.

## Hostile post-review

Three independent hostile passes return `PASS` after repairs.

- **Source/reductive geometry** demoted the finite theorem from a literal GU
  source lift to an abstract \(GL(2)\) source-shaped mechanism, separated
  \(J_0\), \(J_{\mathbb H}\), and \(Q_{\rm Cl}\), required the admitted
  epsilon/domain/invertibility gates, and added nonzero-background curvature
  conjugacy.
- **Variational PDE/Ward--Green** made both \(D_BK\) and \(D_TK\) returns
  executable, separated attainable fourth order from the derivative-affine
  order-two control, and kept the separate comparator, root action, and
  physical Ward claims distinct.
- **Cohomology/evidence** restricted ordinary \(H^1/H^2\) to the flat
  deformation complex, corrected the temporary-coefficient surplus to zero,
  separated source receipts from repository mathematics, and reconciled the
  campaign, datum, Curt/TG, and 202-probe inventory surfaces.

Final reruns pass: `27 algebraic exact + 14 type/registry + 3 source receipts
+ 14 planted = 58`, `21 algebraic exact + 10 type/registry + 11 planted =
42`, and `47 exact scaffold + 13 planted = 60`. No must-fix item remains.

## Boundary and next gate

PW2A promotes only the abstract co-moving gauge mechanism at exact local
structural grade. It does not construct the literal \(Y^{14}\) atlas, prove global
\(\epsilon'\), exponentiate the actual grade-3/11 bridge inside the source
real form, identify the result with active \(P_{\rm nat}\), or evaluate every
slot of the written action. It claims no physical Euler equation, BV
quotient, domain, Standard Model recovery, generation count, quantum theory,
dark-energy prediction, or dark-matter prediction.

The next gate is:

> **PW2B — literal source-composed action order drop and native port.** First
> build or obstruct the actual \(g_u=\exp u(T;J,\epsilon)\) in the source real
> form, prove its admitted-domain/descent properties, stabilize
> \(J_{\mathbb H}\), and transport \(Q_{\rm Cl}\). Only then substitute
> \(\epsilon'=\epsilon g_u\) into every written \(B/T/\odot/Hodge/density\)
> action slot and determine the true jet order. Finally derive the complete
> Euler/Green/Ward graph. Promote only if the result descends through the
> active right-\(\mathbb H\), Krein, trace-reversed \((9,5)\) port.

PW3 remains blocked until PW2B closes that gate.
