---
title: "G1 global tilted packet: derivative cocycle, moving reference, and quotient level"
status: active_research
doc_type: specification
created: 2026-07-31
branch: agent/weinstein-guided-source-action
run: archived private execution record
probe: tests/channel-swings/g1_derivative_cocycle_moving_reference_probe.py
grade: "CONDITIONAL GLOBAL CONSTRUCTION SPECIFICATION. The derivative cocycle, tilted algebra, local-lift descent, patch covariance, moving-reference conjugation, trace-reversed Spin compatibility, right-H structure, and fixed-fibre action-groupoid quotient are exact. Existence/selection of a global LC-equipped reduction on an arbitrary G-bundle and equivalence with Conn(P)/G are not claimed."
---

# G1 global tilted moving-reference packet

## 1. Layer-0 object dictionary

The two symbols previously both called `epsilon` are different objects:

| symbol | type | role |
| --- | --- | --- |
| `g` | `Gau(P)` | a gauge transformation; it has a first jet `dg` |
| `epsilon_red` | `Gamma(P/H)` plus the required LC-equipped reduction structure | a moving Clifford/Spin reduction |
| `u_i` | local lift of `epsilon_red` | defined only modulo `u_i -> u_i h_i`, `h_i:U_i->H` |
| `A_LC(epsilon_red)` | `Conn(P)` | connection induced by the native LC `H`-connection |
| `Gamma_epsilon^A0` | `Conn(P)` | reductive rival induced from a supplied transforming `G`-connection `A0` |
| `q_A(g)` | `Omega^1(Y,ad P)` | derivative affine cocycle relative to a connection `A` |
| `Theta_A` | `Omega^1(Y,ad P)` | left-tilted-invariant/right-adjoint distortion coordinate |

The source `epsilon`, the reduction `epsilon_red`, and P1/P2/P3 are not
identified. `A_LC(epsilon_red)=Gamma_epsilon^A0` is also not automatic.

## 2. Convention and derivative cocycle

Let

```text
G = Sp(32,32;H)
H = Spin_0(9,5) subset G
calG = Gau(P)
V = Omega^1(Y,ad P).
```

Use the left gauge convention

\[
 g\boldsymbol\cdot A
 =\operatorname{Ad}_gA-(dg)g^{-1}.
\]

Then

\[
 q_A(g):=A-g\boldsymbol\cdot A
 =A-\operatorname{Ad}_gA+(dg)g^{-1}
\]

obeys

\[
q_A(gh)=q_A(g)+\operatorname{Ad}_gq_A(h).
\]

Its infinitesimal first-order symbol is nonzero. For `g=exp(t xi)`,

\[
\left.\frac d{dt}\right|_0q_A(e^{t\xi})
=D_A\xi
\]

in this convention. The sign becomes `-D_A xi` in the inverse/right-action
convention. This sign fork has no mathematical content once the convention is
declared.

The E0 object

\[
c_0(g)=A-\operatorname{Ad}_gA
\]

is only the zero-jet summand. If `g(y0)=1` and `dg(y0)!=0`, then
`c0(g)(y0)=0` while `q_A(g)(y0)=dg(y0)`. Hence no pointwise adjoint-module
coboundary can replace the connection cocycle.

## 3. Tilted subgroup and distortion

Equip `IG=calG semidirect V` with

\[
(g,a)(h,b)=(gh,a+\operatorname{Ad}_g b).
\]

For every fixed connection `A`,

\[
\tau_A(g)=(g,q_A(g))
\]

is a homomorphism. Define

\[
\Theta_A(g,a)
=\operatorname{Ad}_{g^{-1}}\bigl(a-q_A(g)\bigr).
\]

Then

\[
\Theta_A\bigl(\tau_A(k)(g,a)\bigr)=\Theta_A(g,a),
\]

\[
\Theta_A\bigl((g,a)\tau_A(h)\bigr)
=\operatorname{Ad}_{h^{-1}}\Theta_A(g,a).
\]

These identities need the 1-cocycle law, not cocycle triviality. The E0
finite lemma therefore survives after its global interpretation is corrected.

## 4. Moving native Levi--Civita reference

Let `Q_Spin(Y,G_DW)` be the Spin bundle of the native trace-reversed metric,
whose vertical fibre is `(6,4)` and whose total signature is `(9,5)`. On the
induced bundle

\[
P_{\rm nat}=Q_{\rm Spin}(Y,G_{\rm DW})\times_HG,
\]

the Levi--Civita spin connection `omega_LC` extends to a `G`-connection. A
moving LC-equipped reduction is locally represented by `u_i`. Put

\[
A_{{\rm LC},i}(\epsilon_{\rm red})
=u_i\omega_{{\rm LC},i}u_i^{-1}-(du_i)u_i^{-1}.
\]

Under a change of reduction lift,

\[
u_i\mapsto u_i h_i,
\qquad
\omega_{{\rm LC},i}\mapsto
h_i^{-1}\omega_{{\rm LC},i}h_i+h_i^{-1}dh_i,
\]

the displayed `G`-connection is unchanged. Under a gauge transformation `k`,

\[
u_i\mapsto k_i u_i,
\qquad
A_{\rm LC}(k\epsilon_{\rm red})
=k\boldsymbol\cdot A_{\rm LC}(\epsilon_{\rm red}).
\]

Thus the construction is local-lift independent and gauge equivariant. It is
global on the orbit/groupoid of LC-equipped reductions isomorphic to the
native Spin reduction. An arbitrary `G`-bundle need not admit such an
`H`-reduction; a different topological component is not silently free.

Because `omega_LC` lies in the moving `spin(9,5)` algebra, it preserves the
moving Clifford soldering and the trace-reversed metric. Because `G` and its
Lie algebra act on the left of the quaternionic spinor module, the resulting
connection commutes with right quaternionic multiplication. No preferred
complex unit is inserted.

## 5. Reductive `A0` rival and exact compatibility equation

For a reductive splitting `g=h+m` and a supplied connection `A0`, define

\[
B_i=u_i^{-1}A_{0,i}u_i+u_i^{-1}du_i,
\qquad
\omega_i^{A_0}=\operatorname{pr}_{h}B_i,
\]

\[
\Gamma_{\epsilon,i}^{A_0}
=u_i\omega_i^{A_0}u_i^{-1}-(du_i)u_i^{-1}.
\]

This also descends under `u_i->u_i h_i`, provided the reductive projection is
`Ad_H`-equivariant. It is gauge covariant only when `A0` transforms as a
connection. Treating `A0` as inert fails the exact patch test.

The two branches agree exactly iff

\[
\operatorname{pr}_{h}
\bigl(u_i^{-1}A_{0,i}u_i+u_i^{-1}du_i\bigr)
=\omega_{{\rm LC},i}.
\]

This is the missing Layer-0 map. It may be imposed as a graph constraint or
derived from later Euler equations; it cannot be hidden in the word
“gauge-rotated Levi--Civita.”

## 6. Moving family and patch law

For `A_epsilon=A_LC(epsilon_red)` or the compatible reductive rival, define

\[
q_\epsilon(g)=q_{A_\epsilon}(g),\qquad
\tau_\epsilon=\tau_{A_\epsilon}.
\]

If `k` moves the reduction and reference, then

\[
q_{k\epsilon}(kgk^{-1})
=\operatorname{Ad}_k q_\epsilon(g).
\]

Consequently the automorphism

\[
C_k(g,a)=(kgk^{-1},\operatorname{Ad}_k a)
\]

sends `tau_epsilon(calG)` to `tau_{k epsilon}(calG)` and

\[
\Theta_{k\epsilon}(C_k\omega)
=\operatorname{Ad}_k\Theta_\epsilon(\omega).
\]

These are also the overlap laws when `k` is a bundle transition function.
The moving construction is therefore a conjugate family of tilted subgroups,
or equivalently a subgroupoid over the reduction field. It is not one fixed
subgroup unless the reference is frozen.

## 7. Exact quotient level and stabilizers

At fixed `A`, left multiplication by `tau_A(g^{-1})` sends every
`omega=(g,a)` to

\[
(1,\Theta_A(\omega)).
\]

The remaining right tilted action is the adjoint action. Therefore the fixed-
reference double-action groupoid is equivalent to

\[
[V/\mathcal G]_{\rm Ad}.
\]

The stabilizer of `omega` under the two-sided tilted action is isomorphic to
the adjoint stabilizer of `Theta_A(omega)`; the left factor is uniquely
determined by the right factor.

This is not automatically `[Conn(P)/calG]`. With `A` held fixed, a connection
`C=A+T` transforms by

\[
T\mapsto\operatorname{Ad}_gT-q_A(g),
\]

which is affine rather than adjoint. If the reference moves simultaneously,
`T=C-A_epsilon` does transform adjointly, but the configuration is then the
pair `(epsilon_red,T)`. Its natural quotient is

\[
[\mathcal E_{\rm ref}\times V/\mathcal G],
\]

not the connection quotient with `epsilon_red` erased. An equivalence to
`Conn(P)/calG` needs an additional equivariant, stabilizer-preserving,
essentially unique reference owner.

## 8. Field policy passed to G2

G2 must choose one of these policies before varying an action:

| policy | `A_ref` | `epsilon_red` | debit |
| --- | --- | --- | --- |
| native LC graph | graph-constrained composite `A_LC(epsilon_red,g_DW)` | varied or boundary-supplied | global reduction sector and its boundary/domain owner |
| reductive `A0` graph | composite `Gamma_epsilon^A0` | varied | full transforming `A0` plus compatibility with native LC if that name is used |
| independent reference | free connection | free/optional | an additional continuous field; loses the claimed economy unless action selects it |

The recommended G2 default is the native LC graph, with the reductive `A0`
branch retained as a hostile comparator. Variation of `epsilon_red` must then
include the first-derivative chain rule and its boundary term.

## 9. Seven-axis impact and datum ledger

G1 changes no L1--L7 class. It remains a smooth principal-bundle construction
with the native Krein signature. The observer/domain axis remains open for G4.

- P1: unchanged.
- P2: unchanged; the reduction/domain orientation is not identified with it.
- P3: unchanged and unused.
- New continuous datum: none locally on the native induced bundle.
- Possible global debit: reduction topological component or boundary
  selection if the action does not own it.
- Surplus: `UNCOMPUTABLE`; the exact identities are structural dependencies,
  not independent phenomenological constraints.

## 10. G1 completion boundary

G1 constructs the derivative/global field grammar needed by G2. It does not
construct the source action, declare the complete variation domain, prove a
Noether identity, identify N1's independent `U`, select a reduction sector,
or establish `Conn(P)/calG` equivalence. It makes each of those statements a
typed downstream question.
