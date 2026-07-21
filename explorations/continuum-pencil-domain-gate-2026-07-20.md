---
title: "Continuum pencil domain gate: two-ended Dirichlet is an exact cokernel obstruction, so the next theorem must freeze a Krein-compatible Lagrangian boundary condition"
status: active_research
doc_type: exploration
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (premium operator-end exact theorem swing)"
inputs:
  - explorations/operator-grade-end-2026-07-20.md
  - explorations/product-typing-and-resolvent-pencil-swing-2026-07-20.md
  - explorations/sector-relative-section-theory-2026-07-20.md
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_actions: none
---

# Continuum pencil domain gate

## Bottom line

The continuum theorem cannot use the two-ended Dirichlet domain named by the
finite-difference probe. On a compact collar, the first-order pencil on

\[
  \mathcal D_{DD}=H^1_0((a,b);\mathbb C^d)
\]

is injective but has a $d$-dimensional adjoint kernel, hence range of
codimension $d$, for every $z$. It is never bijective. This fires the
predeclared outcome **DOMAIN-OBSTRUCTION-DD** before any wall estimate is
attempted.

This is not a no-go for the native Krein section theorem. It removes the
ordinary two-ended Dirichlet truncation as a continuum domain and identifies
the exact next datum: a closed, deck-compatible, Krein-self-adjoint
Lagrangian boundary condition (periodic/deck-twisted, APS-type, or another
explicit maximal isotropic trace relation).

## 1. The exact first-order pencil

On the $P>0$ collar used by the existing construction, write

\[
  D_{\rm op}=-iG_{\rm col}\partial_s+V(s),\qquad
  A=K_u(s)D_{\rm op},\qquad C_0=q(s)^{1/2}.
\]

Here $G_{\rm col}$ is an involution and $K_u(s)$ is the section-theory's
Hermitian involution. Thus the principal coefficient

\[
  B(s)=-iK_u(s)G_{\rm col}
\]

is invertible at every point. For fixed $z$, the continuum pencil is the
regular first-order square system

\[
  P_0(z)u=B(s)u'+W_z(s)u,
  \qquad W_z(s)=K_u(s)V(s)-zC_0(s).
\]

The wall only makes $C_0$ Holder-continuous at its zero. It does not destroy
the invertibility of the principal coefficient, so it does not affect the
domain argument below.

## 2. Exact obstruction for two-ended Dirichlet

Let $L_z=P_0(z):H^1_0((a,b);\mathbb C^d)\to L^2$. The homogeneous equation
$L_zu=0$ is a regular first-order ODE. The initial condition $u(a)=0$
forces $u=0$, so $L_z$ is injective. Variation of constants with the same
zero initial trace gives the standard estimate
$\|u\|_{H^1}\leq C_z\|L_zu\|_{L^2}$, so the range is closed.

Integration by parts shows why surjectivity fails. Because every
$u\in H^1_0$ has zero trace at both ends, the boundary form vanishes against
every $v\in H^1$. Consequently the adjoint has the maximal domain

\[
  \mathcal D(L_z^*)=H^1((a,b);\mathbb C^d),
\]

with no endpoint condition. Its homogeneous equation $L_z^*v=0$ is another
regular first-order system. Every choice of $v(a)\in\mathbb C^d$ has a
unique solution on the compact interval, giving

\[
  \dim\ker L_z^*=d.
\]

Therefore

\[
  (\operatorname{Ran}L_z)^\perp=\ker L_z^*,\qquad
  \operatorname{codim}\operatorname{Ran}L_z=d.
\]

In particular, $P_0(z)^{-1}$ does not exist on the two-ended Dirichlet
domain for any common $z$-region. The same argument is independent of the
choice of $q+i0$ branch and applies before the proposed uniform estimate.

## 3. Why the finite matrix looked invertible

The probe uses the Hermitian central-difference matrix obtained by setting
ghost values to zero outside the sampled interior nodes. That finite square
matrix can be invertible after addition of the potential. It is not a
graph-convergent realization of the continuum derivative with domain
$H^1_0$: the latter is symmetric but not self-adjoint and carries the exact
adjoint cokernel above. The finite inverse therefore cannot certify the
continuum Dirichlet pencil. This is a boundary-domain artifact in addition to
the already recorded wall-on-node artifact.

## 4. GEOMETER-versus-PHYSICS fork

| fork | domain choice | result |
|---|---|---|
| Native keep-and-grade Krein geometry | a maximal isotropic/Lagrangian trace relation for the collar boundary form, required also to respect the deck action | still open; this is the applicable route to a Krein-self-adjoint pencil |
| Ordinary finite-box physics surrogate | zero trace at both collar ends | exactly obstructed: injective, codimension-$d$ range |
| Periodic or deck-twisted end model | $u(b)=Uu(a)$ with $U$ preserving the boundary/Krein form | viable candidate, but invertibility and compatibility are not yet proved |

The negative result lives on the second row. It must not be promoted into a
kill of the first row.

## 5. Frontier movement and next handoff

The operator program has moved from an unspecified domain condition to a
sharp exclusion and a finite-dimensional boundary datum. The next premium
swing should:

1. compute the Green boundary form of $K_uD_{\rm op}$ exactly;
2. freeze one deck-compatible maximal isotropic trace relation, with no
   post-hoc tuning in $z$ or $\delta$;
3. prove closedness and Krein self-adjointness on that domain; and
4. only then test $P_0(z)$ for a common $z$-region, stopping on an adjoint
   solution or boundary monodromy eigenvalue.

No claim, canon verdict, public posture, or paper status changes here. The
result is an exact domain triage for the remaining operator theorem.
