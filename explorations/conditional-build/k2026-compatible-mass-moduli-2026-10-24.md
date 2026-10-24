---
title: "K2026: Complete compatible mass space, exact gaps and an unprotected wall"
status: active_research
doc_type: exploration
created: "2026-10-24"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed-core conditional linear algebra and smooth-solution dynamics; no source connection, physical quotient, interacting positivity, GU prediction or novelty claim
scripts:
  - tests/channel-swings/k2026_compatible_mass_moduli.py
  - tests/channel-swings/k2026_compatible_mass_moduli_probe.py
---

# K2026: Complete compatible mass space, exact gaps and an unprotected wall

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: complete256-dimensional compatible mass space, normalized gapped circle and wall-gapping counterexample
carrier: K1951 full1920 real raw carrier and its fixed invariant128 observed core LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: full indefinite H and inherited positive core P=8I ON=declared_full_and_core_carriers
real_structure: real matrix coefficients and complex Fourier amplitudes
grading: ambient Clifford halves, independent form degree and supplied core wall involution
action_owner: repository-construction -- fixed principal symbols and freely supplied zeroth-order blocks
target: common formal extension and positive conservative gapped propagation MAP-TYPE=intertwiner
```

## 1. Decision and exact scope

[K2024](k2024-full-odd-connection-compatibility-2026-10-24.md) supplied one
invertible compatible mass with a coarse gap bound. Here the **entire real
linear space** satisfying the same three constraints has dimension256:

    N^T=-N,       {N,C_i}=0 (i=1,2,3),       [N,S]=0.       (1)

The report supplies a disjoint-support exact basis, so this is completeness,
not a parameter count inferred from a few witnesses. A deterministic signed
permutation representative N1 satisfies N1^2=-I: its gap is exactly the
supplied mass magnitude. Within (1), the subspace also anticommuting with N1
has dimension128 and contains a second signed permutation N2 with N2^2=-I.

Consequently cos(theta) N1+sin(theta) N2 connects N1 to -N1 while maintaining
the unit gap and every constraint (1). A sign-changing N1 wall has64 transverse
zero modes, but the allowed N2 perturbation gaps them. Thus sign alone does
not define protected sectors under these declared constraints. Additional
symmetry restrictions could change that conclusion; none is supplied here.

This is a complete mass-space result **for the fixed core and constraints**,
not a classification of all source connections or all physical masses. The
Clifford anticommutation assumption imposes an isotropic dispersion relation;
positive conservation alone does not require it. No mass scale is selected.

## 2. Structural reduction before the complete census

Use the K1951/K1967 injection J, D0 J, symmetric generators C_i, and P=8I;
use the K2021 common indefinite H. They obey

    C_i^T=C_i,  {C_i,C_j}=2 delta_ij I,
    S=J^T H D0 J,  S^T=-S,  [S,C_i]=0.

The K2024 general extension condition is SM symmetric. For a skew N this is
exactly [S,N]=0. Define V=C1 C2 C3 and T=-VS. Direct algebra gives

    V^2=-I,  V^T=-V,  T^T=T,  [T,C_i]=0,
    {N,V}=0,  {N,T}=0.                                  (2)

The exact spectrum of T is +9/70, -9/70, +9/140, -9/140,
each of real multiplicity32. Every compatible N exchanges opposite T
eigenspaces of equal magnitude. An invertible N would be impossible if those
multiplicities were unequal. Here that necessary condition is met, and the
explicit normalized matrices prove sufficiency for this actual object.

The C_i and S are monomial matrices in the frozen coordinates. Each entry of
(1) is therefore either a two-variable rational relation or a forced zero.
Connect related entries of a128 by128 unknown matrix. A consistent component
has exactly one parameter; an inconsistent cycle forces its whole component
to zero. This gives an exhaustive exact certificate on all16384 entries:

| System | Scalar equations | Free components | Forced coordinates |
| --- | ---: | ---: | ---: |
| (1) |81920|256|12544|
| (1) plus {N,N1}=0 |98304|128|14464|

The first system has32 free components of size8 and224 of size16. The second
has16 of size8 and112 of size16. Remaining components are forced. The
producer verifies every basis matrix in the original equations. A separate
checker reconstructs completeness using signed conjugation and transpose
orbits, rather than trusting the producer's counts or its entry relations.
Disjoint supports prove independence. No floating rank decision is used.

## 3. Normalized masses and full formal extensions

In each space, scan the basis in deterministic coordinate order. Select a
basis matrix only if its active rows are disjoint from the previous choices
and its square on them is a negative rational square times identity. Normalize
and sum. Sixteen selected matrices cover all128 coordinates, giving each of
N1 and N2 exactly128 nonzero entries and

    N1^2=N2^2=-I,  {N1,N2}=0.                            (3)

This removes the randomized witness search and the coarse inverse-norm gap
bound for these representatives. It does not invalidate the earlier witness.
More generally, if an N in (1) is invertible, -N^2 is positive definite and
commutes with N,S,C_i. Orthogonal diagonalization defines its positive inverse
square root. Then N(-N^2)^(-1/2) still satisfies (1) and squares to -I.
This is a normalization operation, not a source-selected field redefinition
or a classification of the normalized space's topology.

The report constructs full H-self-adjoint1920 by1920 coefficients K1,K2
using K2024's zero-southeast extension formula. Exact multiplication verifies

    H K_a=K_a^T H,   K_a J=D0 J N_a,   (K_a)_SE=0.       (4)

Linearity gives (4) along the entire circle in (3), not only its five rational
controls. These are freely constructed blocks. No raw common-connection tie
or source-owned coefficient has been established for them. The complete
392-coefficient exclusion of K2024 and the full principal Jordan defect remain.

For the fixed observed subsystem,

    partial_t phi+sum C_i partial_i phi+mu N1 phi=0,

smooth decaying or periodic solutions conserve integral phi^dagger P phi.
The Fourier Hamiltonian C dot xi-i mu N1 is Hermitian and squares to
(|xi|^2+mu^2)I. The gap is exactly |mu|, with units and mu supplied. A linear
combination aN1+bN2 instead gives squared gap a^2+b^2. No claim transfers this
positive subsystem to the full carrier or to a source-derived physical quotient.

## 4. Wall modes and an actual gap-opening perturbation

Let x be the first observed spatial coordinate, m(x)=mu tanh(kappa x), with
mu,kappa>0, and put F=C1 N1. Equations(1),(3) imply

    F^T=F,  F^2=I,  dim ker(F-I)=dim ker(F+I)=64.

The transverse zero equation is partial_x phi=-m(x) F phi. Its square-integrable
solutions are exactly

    phi(x)=cosh(kappa x)^(-mu/kappa) v,   Fv=v.           (5)

The F=-1 solutions grow at both ends. The profile in (5) decays exponentially,
so all64 F=+1 amplitudes and no F=-1 amplitudes are normalizable transversely.
C2 and C3 commute with F and restrict to a massless two-spatial-direction
Clifford system on those amplitudes. This is a conditional interface equation,
not a particle-family or chirality count.

Now add the same allowed, constant epsilon N2. Since [N2,F]=0 and
{N2,C2}={N2,C3}=0, the transverse profile space remains invariant. Its Fourier
Hamiltonian is

    C2 eta2+C3 eta3-i epsilon N2,
    H_wall^2=(eta2^2+eta3^2+epsilon^2) I_wall.            (6)

Thus a nonzero epsilon opens a gap without violating (1), full formal
extendibility, or positive smooth-solution energy conservation. The bulk
pointwise mass square becomes -(m(x)^2+epsilon^2)I. This explicit contrary
construction prevents inferring protected gapless wall states from (5) alone.
It does not classify other imposed symmetries, boundary domains, interactions,
or topological invariants of a different admissible class.

## 5. Evidence and retained boundaries

Producer/replay and a separately implemented same-author checker verify all384
basis directions, completeness, both full extensions, exact gaps, the64-mode
wall restriction and its admissible gapping mass. Five faults change actual
mass, extension, basis or gap data and are rejected. Two input hashes establish
provenance separately. The continuum equations (2)--(6) supply the arguments;
finite controls are not a substitute for them. No external specialist or
proof-assistant certificate is claimed.

Strongest overclaim: a positive, formally extendible subsystem is GU's physical
sector. Its selection is still absent. Strongest contrary construction: N2
removes the apparent wall protection without relaxing the tested constraints.
Weakest reproduction seam: mistaking a sparse witness basis for completeness;
the second orbit proof covers all16384 variables. Source SC-OP-04 ASSERTS only
candidate grammar, OP05 and META53 remain UNCERTAIN, and META56 DISAVOWS an
odd-action prerequisite. LT-SM8/LT-GR6b, source register and canon do not change.
The complete raw tie, physical selector, interacting domain, full20, K/C,
accessibility, mirror/full-II, normal jets,2+1 and observed chirality remain open.
