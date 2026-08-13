---
title: "PW2C fixed-Q,g source-root Jacobian, full connection return, and structural Ward/cotangent comparators"
status: active_research
doc_type: construction_result
created: 2026-08-02
branch: agent/null-clifford-omega1-repair
run: private orchestration runtime#meta/runs/historical-investigation/run-plan.md
registries:
  - lab/process/pw2c-literal-source-jacobian-full-k.json
  - lab/process/pw2c-moving-action-ward-bv-registry.json
probes:
  - tests/channel-swings/pw2c_literal_source_jacobian_full_k_probe.py
  - tests/channel-swings/pw2c_moving_action_ward_bv_probe.py
grade: "PW2C SCOPED ACTIVE-GERM CONSTRUCTION PASS. The fixed-Q_Cl,fixed-g left-trivialized Frechet block of (epsilon,varpi)->(epsilon exp u(T),varpi) is derived. Its identity active-grade comparator is exactly block triangular and invertible on every controlled finite mode; an equivariant three-patch h descends and a nonconstant overlap verifies the affine connection law. Derivative loss, off-identity dexp resonance, a hostile scalar interval kernel, same-Hs/tame nonlinear inversion, the transported-Q/metric blocks, public-source bundle, and global atlas remain open. Literal K_full=dexp_-u(D_Bu) equals the direct transformed-connection difference, gives curvature conjugacy, and has its full nonzero-delta-B variation checked. On the controlled linear grade-3/11 Krylov family, same-Delta pairs have equal K_red but different K_full; the two tested Hodge-null branches have vanishing commutator and hence K_red=0 with nonzero K_full=Du. A scalar eight-label dependency comparator realizes the mixed order matrix [[2,3,3],[3,4,4],[3,4,4]], exact one/two/two Green layers, a rank-two top Hessian with the planted Abelian gauge direction as sole null, a nonvacuous off-shell Abelian Ward/Green cancellation, an ordinary canonical cotangent lift, and a finite Abelian BRST comparator. Separately, the actual native trace-adapted moving-Shiab code retains all eight named slots with ten-metric-owner rank 10. The scalar comparator and native coefficient are not one tensor action; the independent hatted-Euler/J_F-adjoint chain, actual Y14 literal-K assembly, nonabelian source Ward, graded BV/BFV, domain, and constraint surplus remain open. P1/P2/P3 remain unchanged and unused; Curt remains separate and no third lane is promoted."
canon_verdict_change: none
---

# PW2C fixed-Q,g source-root Jacobian, full connection return, and structural Ward/cotangent comparators

## Result first

PW2C replaces two structural stand-ins with literal formulas and finds one
important limitation.

For the one-shot active-component source substitution at fixed
`Q_Cl` and fixed metric,

\[
F_{Q,g}(\epsilon,\varpi)
=(\epsilon h(T),\varpi),
\qquad h(T)=e^{u(T)},
\]

write the left-trivialized source tangent as

\[
\xi=\epsilon^{-1}\delta\epsilon,
\qquad \alpha=\delta\varpi.
\]

Then

\[
\widehat\xi
=\operatorname{Ad}_{h^{-1}}\xi
+\operatorname{dexp}_{-u}(\delta u),
\qquad \widehat\alpha=\alpha,
\]

with

\[
\delta u
=U_T(\alpha-D_B\xi).
\]

The fixed-`Q_Cl`, fixed-metric source-root block is therefore

\[
\boxed{
A_T=\operatorname{Ad}_{h^{-1}}
-\operatorname{dexp}_{-u}U_TD_B .}
\]

At the identity active-grade germ, with `u=0` and grade-two `B` preserving the
touched split, grade preservation makes this block triangular. The executable
six-dimensional structural slice has an exact inverse. The imported exact
Alt/star-Alt rank ledger retains `91` grade-two epsilon directions, `728` grade-3/11
directions, a `1274`-dimensional grade-two translation first jet,
alternation rank `364`, and fixed-conormal rank `78`.

That is a real partial source-root result, but not a full Frechet or global
chart theorem. In the Abelian Fourier control,

\[
\det A_n=1-in\lambda,
\qquad |\det A_n|^2=1+n^2\lambda^2,
\]

so every real finite Fourier mode is invertible.  On an interval,

\[
(1-\lambda\partial_x)f=0
\quad\Longrightarrow\quad
f=C e^{x/\lambda},
\]

and the kernel depends on the boundary conditions. This scalar ODE is a
hostile domain comparator, not the same square-zero active-grade germ.
Moreover, because \(T\) contains \(d\epsilon\), the source substitution loses
one epsilon derivative. An unqualified inverse-function theorem on one `H^s`
root space is therefore unavailable. A graded/tame setup, off-identity `dexp`
resonance, the nonlinear implicit inverse, and transported-`Q_Cl`/metric
blocks remain open.

The second literal result is

\[
\boxed{
K_{\rm full}
=h^{-1}D_Bh
=\operatorname{dexp}_{-u}(D_Bu)
=\sum_{n\ge0}\frac{(-1)^n}{(n+1)!}
\operatorname{ad}_u^n(D_Bu).}
\]

An exact noncentral two-coordinate matrix germ verifies both

\[
B+K_{\rm full}=h^{-1}Bh+h^{-1}dh
\]

and

\[
F_{B+K_{\rm full}}=\operatorname{Ad}_{h^{-1}}F_B,
\]

as well as the differentiated formula with a nonzero `delta B` plant

\[
\delta K_{\rm full}
=D_{B+K}\eta
+(\operatorname{Ad}_{h^{-1}}-1)\delta B,
\qquad
\eta=\operatorname{dexp}_{-u}(\delta u).
\]

On the controlled linear grade-3/11 blade family, the Krylov chain closes:

\[
\operatorname{ad}_u^2(Du)=-4\Delta Du,
\qquad
\operatorname{ad}_u^3(Du)=-4\Delta\operatorname{ad}_u(Du),
\]

so

\[
K_{\rm full}
=\frac{\sin(2\sqrt\Delta)}{2\sqrt\Delta}Du
-\frac{1-\cos(2\sqrt\Delta)}{4\Delta}[u,Du]
\]

with the continuous limit at (Delta=0).  This changes the coefficient
picture left by the reduced return:

- `(1,0)` and `(5/3,4/3)` have the same `Delta` and the same `K_red`, but
  different `K_full`;
- `(1,1)` and `(1,-1)` have a separately verified zero commutator, so
  `K_red=0` and `K_full=Du` is nonzero in both controlled branches.

The continuous coefficient of `[u,Du]` tends to `-1/2` at `Delta=0`; thus
`Delta=0` alone does not imply `K_full=Du`.

Thus the earlier Delta-only degeneracy is a property of the grade-two
projection, not of the literal connection displacement.  It does not yet
select `c3:c11`; the full action response has not been assembled.

## Plain English

The previous swing proved that the proposed rotation was legal inside the
active quaternionic/Krein group, but it had not differentiated the actual
source map. PW2C now computes the fixed-owner root block. The controlled
fixed-Q,g structural identity-germ slice is reversible mode by mode. Globally
the source substitution is a differential equation, not an ordinary change
of coordinates: the answer depends on function spaces and boundary
conditions.

The full connection change also contains more information than its projected
connection part.  Two coefficient choices that looked identical after the
grade-two projection become different before projection.  More strikingly,
the two Hodge-null branches do not vanish: only their projected return does.
This reopens the full source action as a possible constraint on the ratio,
without pretending the ratio has already been selected.

The variational panel then proves that a shaped scalar bookkeeping
architecture works. When every named dependency label is retained, the
pulled comparator has the expected mixed derivative orders, Green layers,
gauge null, Ward cancellation, ordinary cotangent lift, and finite Abelian
BRST comparator. The labels are not native operators. The remaining hard
step is no longer “what is the
Jacobian?” or “what is the full connection?”  It is assembling that literal
graph with the actual fourteen-dimensional moving coefficient in one tensor
calculation.

## Layer 0

| object | type | PW2C disposition |
| --- | --- | --- |
| public source bundle | public `U/(7,7)`-presented gauge bundle | not identified with the active component |
| active source component | `P_mix/Sp(32,32;H)` with reduced `Spin0(9,5)` structure | executable local scope |
| source epsilon | group coordinate | not the Clifford reduction |
| `Q_Cl` | Clifford-plane owner | fixed in this Jacobian gate; transported block remains open |
| `F` | first-order field substitution | not itself a gauge symmetry |
| source gauge action | separate tilted/gauge generator | supplies Ward identity when constructed |
| `K_full` | full connection displacement | literal dexp formula constructed |
| `K_red` | grade-two projection | strictly less information; Hodge-null can vanish while `K_full` does not |
| finite-mode inverse | algebraic/microlocal inverse | constructed on the fixed-Q,g structural germ |
| analytic nonlinear inverse | inverse on selected function/domain spaces | open |
| Euler covector | bulk variational owner | constructed in the exact comparator |
| Green current | preboundary concomitant | constructed in the exact comparator |
| Ward identity | off-shell cancellation for a separate symmetry | Abelian comparator pass; actual nonabelian source identity open |
| cotangent lift | ordinary canonical field/covector comparator | finite comparator pass |
| Abelian BRST comparator | `sq=c, sa=Dc, sc=0` | finite nilpotence pass; not a BV action |
| graded BV/BFV/moment map/domain | master-equation, reduced phase-space, and boundary theorem | open |
| P1/P2/P3 | discrete datum ledger | wrong type for the continuous port and unused |

The native metric remains the trace-reversed symmetric fibre with inertia
`(6,4)` and total `(9,5)`.  Raw Frobenius and Curt's `(7,7)` construction are
separate controls, not repairs.

## Three specialist pre-assessments

1. The affine gauge/cohomology lens derived the fixed-Q,g root block `A_T`, warned
   that `dexp` resonance and domain kernels are distinct, required a
   three-patch overlap defect, and predicted derivative loss.
2. The Krein/PDE lens required literal `K_full`, the complete mixed
   `2/3/4` table, exact Green/Helmholtz checks, the gauge symbol before any
   quotient, and separate Krein rank versus symbol rank.
3. The symplectic/reductive lens required an independent hatted-Euler versus
   formal-adjoint chain, transported `Q_Cl` as a separate owner, and restraint
   before any BV or moment-map claim. PW2C closes only the direct pulled scalar
   Euler-Green and ordinary cotangent comparators; the stronger requirements
   remain PW2D.

The shared preregistered expectation was a local finite-germ pass with a
domain/global stop.  That is the result obtained.

## Hostile specialist post-review

The same three lenses initially returned `MUST-FIX`, and the construction was
not promoted until every objection was repaired:

1. The affine/cohomology lens forced fixed-`Q_Cl`, fixed-metric,
   left-trivialized scope; separated the structural slice from its imported
   rank ledger; required a nonconstant affine overlap, off-identity `dexp`
   resonance, a genuine generic `Delta=0` control, and nonzero `delta B`.
2. The Krein/PDE lens forced the interval equation to remain a hostile scalar
   comparator; asserted both exact fibre inertias; separated direct pulled
   Euler-Green from the uncomputed independent `J_F`-adjoint chain; and
   restricted the `2/3/4` and Hessian claims to the scalar comparator.
3. The symplectic/BV lens forced the named factors to remain dependency
   labels, required separately live Ward bulk and preboundary cancellation,
   and replaced the overclaimed BV result with an ordinary cotangent lift and
   explicit finite Abelian BRST comparator while leaving graded BV/CME/BFV
   open.

All three final hostile verdicts are `PASS`. The repaired probes report
`28 exact + 9 type + 4 source + 12 planted = 53 PASS` and
`28 exact + 8 type + 4 source + 12 planted = 52 PASS`; the campaign scaffold
then passes `55 exact + 15 planted = 70`.

## Fixed-Q,g source-root Jacobian and descent

At the identity germ the differential correction sends grade-two source jets
to the odd grade-3/11 tangent while leaving the diagonal grade blocks fixed.
Its off-diagonal operator is square-zero on the controlled split, so the
inverse is exact. This is a structurally faithful fixed-Q,g source-root slice,
not the complete field derivative and not PW2B's unrelated block matrix.

On three patches with transition functions `t_ij`, equivariance requires

\[
h_j=t_{ij}^{-1}h_i t_{ij}.
\]

Then

\[
z_{ij}=h_i t_{ij}h_j^{-1}t_{ij}^{-1}=1,
\]

`K_full` descends tensorially. A separate nonconstant-transition calculation
retains the full inhomogeneous affine law for `B+K_full`. A planted
independently chosen local `h_j` gives a nontrivial
`z_ij`.  Local exponentiation alone is therefore not a descent proof.

When `u` is a global equivariant section, `exp(tu)` connects `h` to the
identity and introduces no new topological datum.  Local logarithm branches,
holonomy, boundary conditions, and the public-active bundle morphism remain
separate global burdens.

## Moving action, orders, and Green identity

The exact differential-substitution comparator uses

\[
T=a-Dq,
\qquad
\widehat q=q+\lambda T,
\qquad
\widehat T=T-\lambda DT.
\]

Its scalar coefficient ledger contains separately ablatable labels shaped
like density, Shiab, Hodge, Krein, lowerer, trace, projector, and curvature
dependencies. These are not native owner formulas. Direct differentiation of
the already-pulled comparator gives an exact Euler-plus-Green identity; an
independent hatted Euler covector followed by `J_F`'s formal adjoint is not yet
computed. The comparator's realized mixed order matrix is

\[
\boxed{
\begin{pmatrix}
2&3&3\\
3&4&4\\
3&4&4
\end{pmatrix}_{(\varpi,\epsilon,g)} .}
\]

The Green depths are one, two, and two. The scalar highest-jet Hessian on its
three top jets has rank two; its sole kernel is the planted Abelian gauge
direction `(1,1,0)`. This is not a native conormal/Krein/right-`H` symbol or a
physical quotient rank.

Separately, the actual trace-adapted native moving-Shiab implementation is
replayed on all ten metric owners.  All eight named slots are live:

1. trace gamma;
2. first `Phi1`;
3. first Hodge;
4. outer `Phi1`;
5. `Phi2`;
6. inner Hodge;
7. middle Hodge;
8. outer Hodge.

Their joint metric response has exact rank `10`.  This is actual native
coefficient evidence.  The scalar differential-substitution comparator
and the native eight-slot coefficient are intentionally not called one
assembled Y14 tensor calculation; that is the next gate.

## Ward, cotangent, and Abelian BRST comparators

For the separate Abelian source-gauge comparator

\[
R_\chi=(\delta q,\delta a,\delta g)
=(\chi,D\chi,0),
\]

one has `delta T=0` and

\[
J_FR_\chi=R_\chi.
\]

The direct density variation vanishes, while the two nonzero Euler owners
obey the off-shell identity

\[
\boxed{E_\epsilon-DE_\varpi=0.}
\]

The preboundary and bulk terms are separately nonzero and obey the explicit
sign-convention identity

\[
\Theta(R_\chi)+E_\varpi\chi=0,
\]

whose derivative cancels the live Ward bulk term. This is a nonvacuous
Abelian shift control, not the actual nonabelian tilted-double-coset Ward
theorem and not a relabeling of `Xi=D_omega Upsilon`.

On each Fourier mode, the cotangent lift

\[
(Q,P)\longmapsto(JQ,J^{-T}P)
\]

preserves the ordinary canonical symplectic form. In the continuum,
integration by parts supplies a nonzero Jacobian Green term. Separately, the
finite Abelian differential `sq=c, sa=Dc, sc=0` has `sT=0` and `s^2=0` on
every tested root and output. These are cotangent and BRST comparators, not a
graded BV action, antibracket, master equation, physical BFV phase space,
boundary moment map, measure Berezinian/anomaly theorem, or closed domain.

## Source collision

**SOURCE-CONFIRMS:** the source roots `(epsilon,varpi)`, homogeneous
distortion, gauge-rotated reference connection, first action, fixed
one-half/one-third completion, displayed `Xi` redundancy, and trace reversal.

**SOURCE-CORRECTS:** a field-dependent source substitution, gauge symmetry,
Ward identity, `Xi` redundancy, BV differential, and global coordinate chart
are different objects.

**SOURCE-SILENT / REPOSITORY-DERIVED:** the grade-3/11 bridge, coefficient
pair, `K_full` versus `K_red` information comparison, fixed-Q,g source-root
Jacobian, transported-Q/metric blocks, public-active bundle morphism, full-
connection resummation, scalar dependency comparator, native moving-
coefficient derivative, off-shell nonabelian Ward/BV/preboundary packet,
measure, and analytic domain.

## Constraint surplus and datum

The full connection now distinguishes pairs that the Delta-only projection
could not distinguish.  That is new information, but not coefficient
selection. The fixed-Q,g root block and comparator Ward identities hold for the entire
coefficient family and therefore are structural constraints, not fitted
equations that can inflate surplus.

Constraint surplus remains `UNCOMPUTED` until the literal `K_full` source
graph and actual Y14 coefficient are assembled and at least one independent
observed equation supplies a response-Jacobian constraint.  P1/P2/P3 remain
unchanged and unused.

## Boundary and next gate

PW2C does not close the transported-Q/metric Frechet blocks, public-source
bundle port, off-identity dexp resonance, tame nonlinear inverse,
boundary/domain choice, global atlas, actual literal-`K_full` times native
eight-slot Y14 coefficient, nonabelian source Ward identity, physical BV/BFV
quotient, observed no-leakage equation, Standard Model/GR recovery,
generation count, quantum theory, or cosmological prediction.

The next highest-information construction is
`PW2D-ACTUAL-Y14-MOVING-COEFFICIENT-AND-SOURCE-WARD-ASSEMBLY`:

1. extend the fixed-Q,g root block through the transported `Q_Cl` and metric
   owners, then insert the literal full-K graph into the reconstructed
   Zorro--DeWitt curvature and all eight native coefficient slots;
2. assemble the complete native mixed principal coefficient and compare it
   with the `2/3/4` germ ledger;
3. derive the actual nonabelian tilted-source Ward and inverse-adjoint Green
   packet, including the explicit `Q_Cl` owner;
4. only if that closes, construct the physical BV/BFV quotient and test the
   selected observation current for no leakage.

PW3 remains blocked.  Curt remains `FORMALLY_SEPARATE_INSIDE_ERIC_LANE`, and
`TG-1 AND TG-2 AND TG-3` remains `NOT_PROMOTED`.
