---
title: "Continuum pencil graph-domain certificate: compact realizations exist, but GU does not select one"
status: active_research
doc_type: exploration
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (next orchestration)"
inputs:
  - explorations/continuum-pencil-domain-gate-2026-07-20.md
  - explorations/product-typing-and-resolvent-pencil-swing-2026-07-20.md
  - explorations/sector-relative-section-theory-2026-07-20.md
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_actions: none
---

# Continuum pencil graph-domain certificate

## Result

The corrected first-order differential expression has many legitimate compact-
collar Krein-self-adjoint graph domains. On each such fixed domain, invertibility
of the pencil is decided exactly by a finite-dimensional boundary-monodromy
determinant. A single nonresonant point gives a pole-free neighborhood and the
usual norm-resolvent boundary value there.

This is a conditional analytic construction, not a source construction. The GU
sources currently supply neither the endpoint relation nor its phase, and the
compact collar itself is only a surrogate for the noncompact fiber. The honest
source-level outcome therefore remains `DOMAIN-OBSTRUCTION-SOURCE`; the new
mathematical outcome is `COMPACT-GRAPH-CONDITIONAL`.

## 1. Frozen corrected expression

On a compact interval \(I=[a,b]\), let

\[
  \widetilde A=B(s)\partial_s+\widetilde W(s),
  \qquad B(s)=-iK_u(s)G.
\]

Assume \(J=J^*=J^{-1}\) is constant,
\(B,H\in W^{1,\infty}\), \(B^{-1}\in L^\infty\), and
\(\widetilde W\in L^\infty\). Freeze the full formal \(J\)-symmetry
conditions:

\[
  B^*J=-JB,
  \qquad
  \widetilde W^*J-J\widetilde W=(B^*)'J=-JB',
\]

and the corrected native expression

\[
  \widetilde A=K_uD_{\rm op}-\frac{i}{2}K_u'G.
\]

The Hermitian, invertible endpoint-form matrix is

\[
  H(s):=-iB(s)^*J=GK_u(s)J.
\]

Up to the harmless common factor \(i\), Green's formula carries the boundary
form

\[
  h_b(u(b),v(b))-h_a(u(a),v(a)),
  \qquad h_s(x,y)=x^*H(s)y.
\]

The wall enters only through the bounded zeroth-order pencil coefficient
\(C_0(s)=q(s)^{1/2}\); it does not make \(B\) singular.

## 2. Exact graph-domain theorem

For an invertible matrix \(T\), set

\[
  \mathcal D_T=\{u\in H^1(I;\mathbb C^d):u(b)=Tu(a)\}.
\]

Then the trace graph is maximal isotropic for the Green form exactly when

\[
  T^*H(b)T=H(a).                                      \tag{G}
\]

Indeed, (G) is precisely isotropy of the graph. Its dimension is \(d\), half
the boundary-data dimension, so it is maximal isotropic. Standard first-order
Green-form duality then makes the realization \(\widetilde A_T\)
\(J\)-self-adjoint. The domain \(\mathcal D_T\) is dense in \(L^2\) and
closed in \(H^1\); the realization \(\widetilde A_T\) is closed.
Invertibility of \(B\) with bounded lower-order terms gives equivalence of its
graph norm and the \(H^1\) norm.

Thus the earlier two-ended Dirichlet cokernel is not a no-go for the
Krein-native lane. It shows only that a first-order square system needs one
maximal boundary relation, not two independent full endpoint constraints.

## 3. Exact monodromy gate

For the pencil

\[
  L_z=\widetilde A_T-zC_0,
\]

let \(\Phi_z(s,a)\) be the fundamental matrix of the homogeneous ODE,
normalized by \(\Phi_z(a,a)=I\). Variation of constants gives the exact
criterion

\[
  L_z:\mathcal D_T\to L^2\text{ is bijective}
  \quad\Longleftrightarrow\quad
  \det\bigl(\Phi_z(b,a)-T\bigr)\ne0.                 \tag{M}
\]

The forward implication follows because a kernel vector is exactly an initial
value \(c\) with \((\Phi_z(b,a)-T)c=0\). Conversely, when the boundary matrix
is invertible, variation of constants uniquely chooses the initial value for
every \(L^2\) right-hand side and supplies an \(H^1\) solution.

Because the coefficient depends affinely on \(z\), \(\Phi_z\) and the
determinant in (M) are entire in \(z\). Unless that determinant vanishes
identically, the pole set is discrete. On every compact pole-free set, the
inverse is uniformly bounded.

## 4. Existence is cheap; canonical selection is not

There is always a transport between the endpoint forms. Let \(S(a)=I\) and
solve

\[
  S'=-\frac12H^{-1}H'S.
\]

Direct differentiation gives

\[
  S(s)^*H(s)S(s)=H(a).
\]

Hence every

\[
  T_\theta=e^{i\theta}S(b)
\]

satisfies (G). At any fixed \(z_0\), all but finitely many phases are
nonresonant: \(\det(\Phi_{z_0}(b,a)-e^{i\theta}S(b))\) is a nonzero polynomial
in \(e^{i\theta}\) with nonzero leading coefficient.

This proves existence of a valid nonresonant compact graph domain. It does not
prove that GU chooses one. Selecting \(\theta\) after inspecting the operator
is post-hoc spectral tuning, and the sources provide no boundary holonomy,
variational rule, or external reference that fixes \(T\) before the spectral
question is asked.

For a family indexed by \(t\), deck covariance generally requires endpoint
actions \(U_a,U_b\), endpoint-form covariance, and the typing condition

\[
  T_{t+1}=U_bT_tU_a^{-1}.
\]

Conjugation by one \(U_h\) follows only when the same deck action operates at
both endpoints without exchanging them. This is a family condition, not a
reason to impose \(u(b)=U_hu(a)\) on each unrelated compact collar.

## 5. Inverse-pencil and norm-resolvent consequence

Let \(q\in L^\infty\) be real with zero set of measure zero, and let
\(C_\delta=(q+i\delta)^{1/2}\) use the frozen upper boundary-value branch. On
a compact interval, \(C_\delta\to C_0\) in operator norm as
\(\delta\downarrow0\). Fix \(T\) independently of \(z\) and \(\delta\). If
a compact \(z\)-set is pole-free for

\[
P_0(z)=\widetilde A_T-zC_0,
\]

the resolvent identity and a Neumann estimate first give uniform convergence
of the inverse pencils \(P_\delta(z)^{-1}\to P_0(z)^{-1}\).

To obtain an operator norm-resolvent statement, define

\[
N_\delta=\widetilde A_TC_\delta^{-1},
\qquad \operatorname{Dom}N_\delta=C_\delta\mathcal D_T,
\]

and

\[
N_0(C_0v)=\widetilde A_Tv,
\qquad \operatorname{Dom}N_0=C_0\mathcal D_T.
\]

The measure-zero hypothesis makes \(C_0\) injective with dense range, while
pencil bijectivity makes \(N_0\) closed. The exact factorization

\[
(N_\delta-z)^{-1}=C_\delta P_\delta(z)^{-1}
\]

then gives

\[
  \sup_{z\in\Omega}
  \|(N_\delta-z)^{-1}-(N_0-z)^{-1}\|\longrightarrow0.
\]

This is compact pencil regularity on a pole-free region. It does **not** prove
that the wall is a regular Krein critical point: that classification also
requires \(N_0\) to be \(J\)-self-adjoint/definitizable with controlled
spectral projections, which is not automatic because \(C_0\) is complex on
the crossed side. It also does not establish the requested noncompact,
\(N\)-uniform theorem. That requires a source-owned asymptotic domain and
uniform inverse/graph estimates; limiting absorption is one possible route.

## 6. GEOMETER-versus-PHYSICS fork

| fork | result |
|---|---|
| Native GU: \((9,5)\), Krein keep-and-grade, deck-covariant domain | Conditional graph theorem above; source selector for \(T\) absent |
| Finite-box two-ended Dirichlet | Exactly obstructed by the \(d\)-dimensional adjoint cokernel |
| Conventional positive-Hilbert/APS or scattering domain | Potentially valid, but it is an imported physical boundary choice until matched to the GU source |

## 7. Bounded verdict

- `COMPACT-GRAPH-CONDITIONAL`: proved at the stated first-order ODE grade.
- `DOMAIN-OBSTRUCTION-SOURCE`: still fires for the native GU theorem because no
  source-owned endpoint/asymptotic relation has been identified.
- `COMPACT-PENCIL-REGULAR`: proved on every frozen pole-free compact region
  satisfying the stated hypotheses; not promoted to regular-Krein-critical or
  noncompact theorem status.
- No categorical product clause remains: the product is the direct sum of the
  factor realizations.

No claim, canon verdict, paper status, or public posture changes from this note.
