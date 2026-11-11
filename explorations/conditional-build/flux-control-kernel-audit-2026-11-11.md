---
title: "The finite flux control: exact kernel and cutoff audit"
status: exploration
doc_type: structural-result
created: "2026-11-11"
program_target: X-P1-P2-P3
tier: T2
expected_delta: "Adjudicate proposed width evidence and refine its exact applicability."
actual_delta: "Witnesses not certified; useful finite and analytic controls retain their explicit scope."
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# The finite flux control: exact kernel and cutoff audit

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `CONVENTIONAL_COMPARATOR`.

program_target: X-P1-P2-P3
tier: T2
expected_delta: Audit LB-CLASS width witnesses without changing the action class.
actual_delta: Witness evidence qualified; no class, source, ledger or scientific verdict.

**Result.** For the actual finite Wilson matrix in the proposed inclusion
control, nontrivial magnetic holonomy and a positive Wilson coefficient imply
invertibility. Its rounded near-zero chirality magnitude agrees numerically with flux in
the tested windows, but is not an exact graded zero-mode index. A quantitative
energy bound makes that distinction rigorous without a larger numerical census.
This is an audit of a conventional instrument, not a GU or class-C verdict.

```gu-typed-objects
result: flux-control-kernel-audit
carrier: finite complex two-component spinors on connected periodic magnetic graph LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: positive Hermitian inner product ON=declared_carrier
real_structure: complex U1 link phases; no K77/K95 identification
grading: Gamma=sigma3 tensor identity; distinct from modified GW grading
action_owner: repository-construction -- existing finite comparator operator, no new action
target: exact kernel versus window chirality and signed-readout index MAP-TYPE=projection
```

## 1. Actual construction and prior corrections

Read [the original function](../../tests/function-space-ext/flux_index_2d.py),
not its headline. It constructs Hermitian T_x,T_y and the magnetic graph
Laplacian W, then

`D = sigma1 ⊗ T_x + sigma2 ⊗ T_y + r sigma3 ⊗ W`, `Gamma=sigma3⊗I`.

The function `chiral_index` returns
`round(Tr(Gamma P_{|D|<gap}))` with gap=0.25, together with the number of
selected modes. It selects a near-zero spectral window, not ker D. Its checks
use `abs(rounded)==Phi`, so the sign is not certified by the old “index=flux”
wording. The [August10 addendum](../judge-corrected-claims-addendum-2026-08-10.md)
already records the sign, dependence of the second parameter sweep and nonzero
Krein violation at Phi=0. Those are reused warnings, not new accepted canon.

## 2. Exact magnetic-kernel theorem

The exact theorem concerns the mathematical unit-phase construction implemented
by the code. NumPy exponentials and eigensolves are binary64 approximations;
the replay is explicitly numerical, not an interval certificate for those stored
float matrices. The Gaussian-unit fixture uses exact arithmetic separately.

For each oriented edge e=(a,b) with unit phase u_e, the old W obeys

`<x,W x> = (1/2) sum_e |x_a-u_e x_b|²`.

Thus W is positive semidefinite. On a connected graph its kernel consists
exactly of parallel sections. Transporting a nonzero parallel section around a
cycle with holonomy h forces x=h x. If any h≠1, that section vanishes at the
cycle and hence everywhere: **W is positive definite**.

Pauli anticommutation gives the exact identity

`(Gamma D + D Gamma)/2 = r I ⊗ W`.

For Dψ=0, the expectation of the left side vanishes, so r>0 and W>0 imply
ψ=0. Since the finite matrix is square, D is invertible. More strongly,
Cauchy–Schwarz and unitarity of Gamma give

`||Dψ|| ||ψ|| >= Re <ψ,Gamma Dψ> >= r lambda_min(W) ||ψ||²`.

Therefore `sigma_min(D) >= r lambda_min(W)>0`. This proof applies to the actual
magnetic code on any connected finite graph with the stated Pauli/edge form.
For the old L×L uniform links, an elementary plaquette has holonomy
`exp(±2 pi i Phi/L²)`. Hence all old nonzero examples 0<Phi<L², including
Phi=1,2,3 at L=16, have **zero exact kernel** for r>0. Sign convention does not
affect nontriviality. Phi=0 admits parallel W sections and is deliberately
outside the strict argument. Removing r also removes the coercive implication.

## 3. Released quantitative successor: a usable gap bound

Choose a cycle of m distinct edges with holonomy h≠1, root a, and let
`delta=|1-h|`. Let every vertex have a simple path from a of length at most ell.
Put E=<x,W x>. Telescoping edge differences around the cycle and applying
Cauchy–Schwarz gives `delta |x_a| <= sqrt(2mE)`. Along a root-to-v path,
`|x_v| <= |x_a|+sqrt(2ell E)`. Consequently

`||x||² <= 4 N (m/delta² + ell) E`,

so `lambda_min(W) >= [4 N (m/delta²+ell)]^-1`.
Repeated edges would require their multiplicities in this bound; the chosen
plaquette and shortest paths do not repeat edges. Cycle/path overlap does not
invalidate separate upper bounds. Apply the scalar inequality separately to
each spin component. The bound is conservative, not an estimate of the true gap.

For the exact L=4,Phi=4 fixture, link phases are Gaussian units, m=4,
delta²=2, and ell=4. This yields **lambda_min(W)>=1/384** and hence
`sigma_min(D)>=r/384`. The probe verifies W as an exact incidence Gram matrix,
positive rational LDL pivots, and positivity of W−I/384. It separately verifies
that trivializing the links restores the parallel section and that removing
the Wilson term restores the original anticommutation. These are genuine
contrary controls on the hypotheses.

## 4. Why rounding does not repair the observable

A fixed separated window can carry continuously varying noninteger chirality.
Let Gamma=diag(1,-1), eigenvalues (1/8,2), cutoff1/4, and rotate the eigenvectors
by a real orthogonal Q. The low-window chirality is cos(2theta), although the
eigenvalues never move. At Q=I it is1. At the exact rational rotation with first
column (3/5,4/5), it is−7/25, rounded to0. There was no eigenvalue crossing of
zero or the cutoff. A continuous rotation connects the examples.

Thus threshold separation alone does not make rounded chirality a homotopy
invariant integer. For the actual nonzero-flux matrices, selecting a cutoff
below their positive minimum absolute eigenvalue makes the selected window
empty. The old cutoff may remain a useful numerical continuum diagnostic;
convergence and a correct continuum/index transfer would have to be established
separately. No estimate here is uniform in the continuum limit: the conservative
bound may tend to zero as lattice size grows. Finite invertibility therefore
does not contradict continuum zero modes.

The exact equal-rank finite odd-matrix balance versus modified lattice chirality
is already discussed in [W224](../W224-falsify-nielsen-ninomiya-chirality-2026-07-14.md).
We reuse that distinction. A physical Hamiltonian's chirality preservation uses
`[H,Gamma]=0`; a graded Dirac operator's index uses an oddness relation. The
failure of `{D,Gamma}=0` alone is **not** a P1 propagation verdict.

## 5. Alternative integer control, executed at its own scope

The existing [signed-readout result, Part Z](../big-swing-2026-07-03/R3-signed-readout-standalone-theorem.md)
starts from even dimension, Tr Gamma=0, and a Hermitian involution epsilon.
For a=1, `D_GW=I+Gamma epsilon` obeys

`Gamma D_GW+D_GW Gamma=D_GW Gamma D_GW`,
`Gamma_hat=Gamma(I-D_GW)=-epsilon`,
`Q=-Tr(epsilon)/2` in Z.

The probe reuses the theorem on exact data Gamma=diag(1,1,-1,-1),
epsilon=diag(-1,-1,-1,1): D_GW=diag(0,0,2,0), Q=1, and the exact kernel has
chirality2−1=1. A noninvolution replacement breaks the GW identity. This is an
instrument control with engineered data, not an action, a generation-count
selection or evidence that this sign operator is local. Hermitian sign-gap
preservation makes Q constant; the old threshold trace has no such property.

Modern primary work proves a continuum torus index correspondence using a
massive Wilson family's spectral flow/eta invariant at sufficiently small
lattice spacing: [Aoki et al., arXiv:2407.17708v2](https://arxiv.org/abs/2407.17708v2).
Its stated mass, family and continuum-limit premises are different from the
single massless rounded window used here. No particular L=16 correspondence is
inferred from that existence theorem. The continuum flux-index theorem and the
reused GW theorem remain valid comparators; neither establishes class C/P1.

## 6. Reproduction and acceptance ceiling

Run `tests/program-focus/class_width_witness_audit_probe.py` in the scientific
Python environment. It checks exact rational/complex identities and controls,
then loads the unchanged historical builder through its function AST and
reproduces L=16 flux0,1,2,3 with single-thread numerical eigensolves. Only the
latter rows are floating diagnostics. [Saved evidence](../../lab/process/class-width-witness-audit.json)
contains raw traces, rounded values, minimum absolute eigenvalues, window sizes,
exact pivots and the historical source hash. Without `--write`, it verifies the
saved exact data and compares numerical replay with a declared tolerance.

The universal proof is the argument above; its hypothesis transfer receives
independent specialist/hostile review. Finite LDL checks do not certify all
lattices, continuum convergence, Y14 geometry or physical families. No Lean,
canon, source or physics-ledger claim follows. The companion
[width audit](class-width-witness-audit-2026-11-11.md) owns the native consequence.
