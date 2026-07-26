---
artifact_type: exploration
label: W245
status: "completed typed collision; exact finite certificate 16/16; admissibility boundary only"
created: 2026-07-26
title: "W245 — Finster Dirac-sea baryogenesis versus the GU stable/pathological Krein fork"
grade: "EXACT for the two-by-two spectral and positive-metric obstruction; PRIMARY-SOURCE-ANCHORED for the Finster typing; EXPLORATION/CONDITIONAL for the GU-to-CFS bridge; no baryogenesis rate or causal-action selection"
depends_on:
  - explorations/W186-source-content-reservoir-krein-type-2026-07-14.md
  - explorations/W216-true-vacuum-spectral-condensate-2026-07-14.md
  - lab/deep-research/finster-causal-action-selector-comparator-2026-07-26.md
scripts:
  - tests/W245_finster_baryogenesis_krein_branch_discriminator.py
---

# W245 — Finster baryogenesis versus the GU Krein fork

## Plain-English result

There is a real connection, but it is narrower and cleaner than “the good GU
branch makes matter and the bad branch makes antimatter.”

Finster's baryogenesis mechanism counts changes at the edge of a regularized
Dirac sea. The count is built from a **self-adjoint** regularization operator
and its spectral projectors. GU's W216 good branch has exactly the required
kind of real, Hermitian spectrum. The pathological branch does not: in its
central interval its energies become complex. No positive change of inner
product can turn a complex-spectrum operator into a self-adjoint one.

Therefore:

> If the W216 branch generator is conditionally identified with Finster's
> spectral regularization operator, the Finster sea-rate is well typed on the
> good branch and ceases to be well typed in the pathological core.

That is an **admissibility boundary**, not yet a source-action selector. It
says the pathological branch cannot support this particular unitary
Dirac-sea bookkeeping. It does not show that the CFS causal action dynamically
chooses the good branch, and it does not compute a baryogenesis rate.

## 1. What Finster's mechanism actually uses

The original causal-fermion-system construction describes a regularized
Dirac sea whose microscopic regularization changes in time. A mismatch in the
number of sea states can leave particles or holes. Its simple approximate
rate is

\[
B(t)=-\operatorname{tr}\!\left(
  \widetilde E_{-m}(t)\,\dot{\widetilde A}(t)
\right),
\]

where \(\widetilde A(t)\) is the essentially self-adjoint spectral
regularization operator and \(\widetilde E_{-m}(t)\) is its spectral measure
at the sea edge. The construction uses adiabatic projections to preserve
unitarity.

The later Minkowski-space analysis is an important null control. Under its
stated absolutely-continuous-spectrum assumptions:

- the first-order term vanishes;
- the second-order term is generally nonzero;
- a constant regularizing vector \(u=\partial_t\), normal to the Cauchy
  surface, gives \(\Delta A=0\) and no baryogenesis; and
- the result depends on supplied regularization dynamics, not on a branch
  label by itself.

The conformally-flat extension derives a rate depending on the particle mass
\(m\), conformal factor \(\Omega\), and future-directed timelike regularizing
vector field \(u\). None of these sources derives or identifies GU's Krein
sign.

Primary sources:

- Felix Finster, Maximilian Jokel, and Claudio F. Paganini,
  [A Mechanism of Baryogenesis for Causal Fermion Systems](https://arxiv.org/abs/2111.05556),
  *Classical and Quantum Gravity* 39 (2022) 165005.
- Felix Finster and Marco van den Beld-Serrano,
  [Baryogenesis in Minkowski Spacetime](https://doi.org/10.1016/j.geomphys.2024.105346),
  *Journal of Geometry and Physics* 207 (2025) 105346.
- Felix Finster and Marco van den Beld-Serrano,
  [Baryogenesis in Conformally Flat Spacetimes](https://arxiv.org/abs/2504.17434)
  (2025 preprint).

## 2. The exact GU-side theorem

Use only the matrix specimens already declared in W216, without importing its
larger physical interpretation:

\[
H_+(\xi,\Delta)=
\begin{pmatrix}
\xi & \Delta\\
\Delta & -\xi
\end{pmatrix},
\qquad
H_-(\xi,\Delta)=
\begin{pmatrix}
\xi & \Delta\\
-\Delta & -\xi
\end{pmatrix}.
\]

The good block is Hermitian and has

\[
\operatorname{spec}(H_+)
=\left\{\pm\sqrt{\xi^2+\Delta^2}\right\}.
\]

The pathological block is self-adjoint only in the indefinite Krein metric
\(J=\operatorname{diag}(1,-1)\), and has

\[
\operatorname{spec}(H_-)
=\left\{\pm\sqrt{\xi^2-\Delta^2}\right\}.
\]

### Positive-metric sea-projector obstruction

Let \(\Delta\neq0\). For every \(|\xi|<|\Delta|\), \(H_-\) has nonreal
spectrum. If a positive-definite metric \(G\) satisfied

\[
G H_- = H_-^\dagger G,
\]

then \(G^{1/2}H_-G^{-1/2}\) would be Hermitian and would have real spectrum.
Similarity preserves spectrum, giving a contradiction. Thus no
positive-Hilbert self-adjoint realization exists in the broken interval.

At \(\xi=0\) this is visible without a spectral theorem. Writing

\[
G=\begin{pmatrix}a&c\\c&b\end{pmatrix},
\]

the metric-adjoint equation requires

\[
\Delta(a+b)=2\xi c.
\]

At \(\xi=0\), it forces \(a+b=0\), which is impossible for \(G>0\).

The boundary is sharp. For \(|\xi|>|\Delta|\),

\[
G_\xi=
\begin{pmatrix}
1&\Delta/\xi\\
\Delta/\xi&1
\end{pmatrix}
\]

is positive and makes \(H_-\) quasi-Hermitian. Its determinant
\(1-\Delta^2/\xi^2\) vanishes at the exceptional point. The obstruction is
therefore not “Krein operators can never have a Hilbert description.” It is
that the complete pathological path through the exceptional interval cannot
carry the positive self-adjoint spectral calculus the Finster rate requires.

## 3. What the finite computation learned

`tests/W245_finster_baryogenesis_krein_branch_discriminator.py` passes
`16/16` checks.

It establishes:

1. the good branch has an ordinary negative-energy projection-valued
   projector;
2. a generic Riesz projector in the broken pathological interval is
   idempotent but not an orthogonal Hilbert projector;
3. the positive quasi-Hermitian metric outside the interval becomes singular
   at the exceptional point;
4. a standard two-level spectral-flow control reverses sign under time
   reversal and vanishes for static dynamics; and
5. a complete finite CFS universal measure has a computable causal action,
   while the GU branch payload lacks every field needed to form that
   variational comparison.

The finite spectral-flow control

\[
-\operatorname{tr}(P_-\dot H_+)
=v\,\frac{\xi}{\sqrt{\xi^2+\Delta^2}}
\]

is deliberately classified as an ordinary avoided-crossing absorber. It is
not Finster's continuum rate, whose Minkowski first-order term vanishes under
the stronger field-theoretic assumptions. It carries no baryon charge,
washout, entropy, or cosmological semantics.

## 4. Why this does not yet select the stable branch

The CFS causal action acts on a universal measure \(\rho\) over a supplied
operator space, with a fixed Hilbert space, spin dimension, constraints, and
regularization. W186/W216 supply branch generators and metrics. They do not
supply a common map

\[
H_\pm\longmapsto\rho_\pm
\]

inside one frozen CFS variational problem.

Inventing two measures after seeing which matrix is stable would encode the
desired answer. Until a natural common map is derived, the question

\[
\mathcal S(\rho_+)<\mathcal S(\rho_-)\;?
\]

is an incomplete contract, not an unperformed numerical calculation.

There are consequently three distinct claims:

1. **Admissibility:** the good branch supports the required Hilbert spectral
   calculus; the pathological core does not. **Earned in the finite model.**
2. **Selection:** one common causal action chooses the good branch.
   **Not defined.**
3. **Baryogenesis:** selected regularization dynamics generates the observed
   matter asymmetry. **Not computed and far downstream.**

## 5. Consequence for GU

This collision strengthens the interpretation of W186/W216's “pathological”
label: the complex branch is not merely aesthetically bad. It cannot host the
positive-Hilbert Dirac-sea projector used by a serious candidate physical
rate mechanism.

It does **not** resolve the outstanding Krein-sign selector. The old choice is
not converted into a derived source action. GU claim status, operator status,
canon, generation count, and public posture remain unchanged.

The correct current disposition is:

> **ADMISSIBILITY_ONLY / CAUSAL-ACTION COMPARISON INCOMPLETE / NO
> BARYOGENESIS RATE.**

## 6. Reopen conditions

Do not keep circling this route. Reopen it only if at least one of these
arrives:

1. a GU-derived self-adjoint regularization operator \(A_t\) distinct from,
   but naturally related to, the Krein BdG generator;
2. one target-independent construction of \(\rho_+\) and \(\rho_-\) under
   identical CFS Hilbert space, spin dimension, constraints, regulator,
   matter sector, and boundary data;
3. a proof that the causal action or its Euler--Lagrange equations rank those
   two measures without refitting; or
4. a charge-resolved map from sea-state flux to the GU matter sectors,
   including conversion and washout assumptions.

If none is supplied, further local cosmology or rate fitting cannot answer
the branch-selection question and should not be built.
