---
title: The B5 end needs more than a boundary polarization for a Fredholm index
status: exploration
doc_type: structural-result
created: '2026-11-11'
program_target: P3xdomain_boundary
tier: T2
expected_delta: Resolve the full graph-domain Fredholm feasibility of the existing
  B5 end, including scalar weights and the reduced gauge complex.
actual_delta: 'Constrained: the actual flat B5 fold has escaping approximate null
  sequences for every fixed exponential weight and scalar mass; boundary polarization
  alone cannot supply Fredholmness, and the massless gauge quotient retains the sequence.'
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# The B5 end needs more than a boundary polarization for a Fredholm index

Constrained: the actual flat B5 fold has escaping approximate null sequences for every fixed exponential weight and scalar mass; boundary polarization alone cannot supply Fredholmness, and the massless gauge quotient retains the sequence.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

program_target: P3xdomain_boundary
tier: T2
expected_delta: Resolve the full graph-domain Fredholm feasibility of the existing B5 end, including scalar weights and the reduced gauge complex.
actual_delta: Constrained: the actual flat B5 fold has escaping approximate null sequences for every fixed exponential weight and scalar mass; boundary polarization alone cannot supply Fredholmness, and the massless gauge quotient retains the sequence.

```gu-typed-objects
result: full graph-domain Fredholm feasibility and strict reduced-complex transfer
carrier: complex1920 folded B5 sections over flat half-cylinder with periodic spin structure LAYER=ambient CHIRALITY=S-FULL-DIRAC
pairing: auxiliary positive weighted L2 graph norms; native Krein form kept separate ON=declared_carrier
real_structure: complexified native9plus5 Clifford module; no coflip-real physical quotient asserted
grading: ghost0 versus vector-spinor1 and strict linear complex; not observed chirality
action_owner: repository-construction -- existing strict B5 expression; scalar shifts analytic controls only
target: compact-core sequences and induced Hilbert quotient operator MAP-TYPE=quotient
```

## 1. Existing object, exact new question

The [B5 minimal-domain result](../b5-flat-product-minimal-domain-2026-08-20.md)
constructs a closed realization on [0,infinity) times T13 with periodic spin
structure, metric diag(9plus,5minus), normal dr=e0, and auxiliary positive L2
topology. Its formal pairing stays Krein. The
[marked BRST class](../b5-domain-compatible-brst-cohomology-2026-08-21.md)
proves extension-sensitive cohomology at a particular decaying mode. Neither
asserts Fredholmness. We test that missing premise on this actual existing
operator, not on an elliptic replacement or the actual global Met(X) end.

Generic ultrahyperbolicity was already established in the
[Y14 Cauchy/domain audit](../eric-curt-wave3c-y14-atlas-cauchy-domain-2026-07-31.md).
It is reused, not counted as a new result. Here a normalized sequence in the
**full graph domain** proves non-Fredholmness for every closed realization
containing the compact-interior core, even after scalar exponential weights
and constant scalar lower-order shifts. Thus this is stronger than failure of
an H1 elliptic estimate or a statement that an APS theorem is unavailable.
No action is constructed. The scalar shifts below are analytic countercontrols,
not source-selected action coefficients or an allowed flat B5 mass branch.

SC-OP-04 ASSERTS candidate operator grammar and SC-CHI-01/51 ASSERTS
nonchiral-total/effective-chirality obligations; none identifies the existing
strict B5 reconstruction with the source nonlinear action. SC-GEN-02/03/54
ASSERTS the separately scoped2+1/label/graded-extension claims. RA-F1, AC-F1
and LT-SM8 remain NEEDS in ledger0.263. No class-C exclusion, source verdict,
physical Hilbert realization, family-count conclusion or canon change follows.

## 2. A general graph-domain criterion

Let T be any densely defined closed operator between Hilbert spaces. If u_n are
in its domain, ||u_n||=1, u_n converges weakly to0, and ||T u_n||→0, then T is
not Fredholm. If it were, its finite-dimensional kernel projection P would
satisfy ||P u_n||→0 and closed range would give

    ||(1-P)u_n|| <= C ||T u_n||,

a contradiction. The estimate follows by the bounded inverse theorem on the
closed graph domain restricted to ker(T)-orthogonal vectors. Selfadjointness,
normality and a particular boundary trace are not assumptions.

Consequently a sequence of compact-interior smooth sections works for EVERY
closed realization of the same expression that contains that core. A boundary
polarization at r=0 cannot remove such a sequence. Boundary realizations that
exclude the compact core or impose nonlocal bulk constraints are different
categories, not covered by the conclusion.

## 3. Native folded symbol and exact transverse identity

Use gamma_a gamma_b+gamma_b gamma_a=2 eta_a delta_ab and gamma^c=eta_c gamma_c.
Write xi^a for RAISED complex symbol components. For xi, the exact native symbol on S plus (V* tensor S) is

    B(xi) = [[0,Avee(xi)],[A(xi),K(xi)]],
    A_a=eta_a xi^a,  Avee_c=xi^c,
    K_ac=sum_b xi^b gamma_[a gamma_b gamma^c].
    D=sum_a eta_a B(e_a) partial/partial y_a, with y0=r.

The triple is the fully antisymmetric Clifford product; it vanishes on repeated
indices and agrees with the ordered product on distinct indices. These are the
actual functions in the retained B5 probe, not a Dirac substitution.

Put l^sharp=e4+e9. Its lowered Fourier covector is k=e^4-e^9; both are
nonzero, integral and null. Fix delta in R
and mu in C. For a positive integer N let

    xi_N = -delta e0 + i N l^sharp,        q(xi_N)=delta²,
    c_N = sum_a xi_N^a gamma_a.

Take ghost component0, vector components

    v_N,1=gamma2(c_N+mu)s,     v_N,2=gamma1(c_N+mu)s,

and all other components0. Choose a fixed spinor s with c(l^sharp)s≠0, possible
because the faithful complex128 Clifford module has c(l^sharp)≠0.
Gamma v_N=0 and Avee(xi_N)v_N=0: the former uses
(gamma1 gamma2+gamma2 gamma1)=0; the latter uses xi^1=xi^2=0.
On this transverse trace-free vector, the triple identity gives K(xi_N)v_N=c_N v_N.
Since c_N anticommutes with gamma1,gamma2 and c_N²=delta²,

    (B(xi_N)+mu I)v_N
      = (mu²-delta²) w,  w_field1=gamma2 s, w_field2=gamma1 s,
      w_ghost=w_field0=all other fields=0.                  (1)

Both gamma1 and gamma2 are invertible. Hence ||v_N|| >= cN-C for constants
c>0,C depending only on fixed s,delta,mu, and normalized residual in (1) is
O(1/N). At mu²=delta² it vanishes identically; this resonance is not needed.
The probe verifies (1) as an exact polynomial Clifford identity in N,delta,mu,
plus independent native-matrix nonzero/growth and contrary controls.

## 4. Weight, cutoffs and all boundary realizations

Let H_delta have norm ||exp(delta r)u||_L2. The map T_delta u=exp(delta r)u
is unitary from this weighted Hilbert space to unweighted L2; it is generally
NOT a boundedly invertible map on the same unweighted L2 space. It conjugates
D+mu I to D-delta B(e0)+mu I.

Choose chi in C_c^infinity((0,1)) with L2 norm1, L_N=N, and R_N→infinity.
In unweighted coordinates set

    u_N(r,y)=L_N^-1/2 chi((r-R_N)/L_N)
             exp(iN(y4-y9)) v_N/||v_N||,

with Haar-normalized torus measure. Then ||u_N||=1, its support escapes, and

    ||(D-delta B(e0)+mu I)u_N||
       <= C1/N + ||B(e0)|| ||chi'||/L_N  →0.                       (2)

Support escaping proves weak convergence to0 by the L2 tail bound (distinct
Fourier modes also give orthogonality). Each u_N is smooth and compactly
supported away from r=0, hence is in every admitted closed extension. The
criterion proves non-Fredholmness for every delta,mu and all such boundary
realizations. This includes the minimal and closed polarized B5 domains.

For ONE fixed closed extension of D_delta containing the core, all scalar
shifts have that same domain and are closed. The proof applies to every shift,
so its Fredholm essential spectrum, defined as the set of lambda for which
D_delta-lambda is not Fredholm, is the entire complex plane. Its ordinary
resolvent is therefore empty too. This is a nonnormal unbounded-operator
statement, not a calculation of physical energies or boundary-adapted spectra.

The simpler zero tangential mode already gives an O(1/L) singular sequence for
the strict unweighted massless operator. It is insufficient for the weighted
conclusion: the scalar comparison partial_r+mu with domain H1_0(R+) IS
boundedly invertible for real mu>0, with inverse

    u(r)=integral_0^r exp(-mu(r-s)) f(s) ds,       ||u||<=||f||/mu.

Thus ordinary mass-gap intuition works in that scalar category. The new B5
conclusion depends on its actual high tangential null modes and nonnormal
symbol behavior; it is not a general claim that weights or masses never help.

## 5. Released asymptotic perturbation consequence

The result persists for smooth coefficients of the EXPANDED first-order expression tending uniformly on
the torus to the constant B5 coefficients, and zero-order term tending to mu I.
After the same weight conjugation, choose R_N far enough out that ALL principal
and zero-order differences have norm at most N^-2 throughout r>=R_N.
On the normalized u_N, tangential derivatives have norm O(N), the radial
cutoff derivative O(1/N), and there are finitely many coefficients. Thus the
additional residual is O(1/N); (2) still tends to0. No convergence rate or
relative-compactness assertion is needed. In divergence form, coefficient
derivatives are included in the zero-order convergence hypothesis. Uniform decay of a bounded potential
alone is the special case of unchanged principal coefficients.

This is a theorem for ends with these specified asymptotics and a periodic
null lattice. Neither the source nor class C has supplied those asymptotics for
Met(X). Arbitrary nondecaying matrix potentials, altered leading symbols,
nonperiodic ends, different weights or genuine bulk constraints are outside
this argument. They require a different test, not automatic success.

## 6. Released massless gauge quotient

Set mu=0. Conjugate the whole constant-coefficient complex by T_delta:
S --A_delta--> V* tensor S --K_delta--> (V* tensor S)^vee --Avee_delta--> S^vee.
The derivatives shifted by -delta commute, so K_delta A_delta=0 and
Avee_delta K_delta=0 still hold. Assume closed stage domains that form this
complex and contain the compact-interior cores; this includes the strict
unweighted constructions at their stated grade.

Let G=closure(im A_delta). Closedness and the complex identity imply
G subset ker K_delta subset Dom K_delta. The orthogonal projection Q onto
vector slots1,2 and ALL Fourier modes {N k:N integer} annihilates the entire
distributional gauge range: those modes have no derivative in directions1,2.
It therefore annihilates G. Our field vectors obey Q u_N=u_N, so their distance
to G is exactly1. K_delta descends to a closed operator on the Hilbert quotient
H1/G: identify its domain with Dom K_delta intersect G-perp and use that
subtracting a G element preserves both domain and image. The same normalized
weakly null sequence has K_delta residual→0. Thus the induced operator is
non-Fredholm as well. The conclusion remains if its target is restricted to
a closed compatible subspace with the inherited norm.

The sequence forces infinite-dimensional kernel OR nonclosed range; it does
not determine which, compute total cohomology, or determine the cokernel. It is also
not a positive physical quotient. Scalar mu≠0 or arbitrary potentials need
not preserve the complex, so the quotient statement is not extended to them.

## 7. Cross-result consequence: a non-scalar compatible connection

The [connection classification](x-p1-p2-projector-connection-2026-11-11.md)
releases a concrete non-scalar test, without inventing an action. Its entire
constant-radial subclass is nabla_b=partial+b dr Omega, b real, on the flat
K95 spinor bundle. Applying this connection to every folded spinor slot gives
the analytic differential expression

    D_b=D+b B(e0) Omega_fold.

This is ordinary covariantization of the existing expression, not a claim of
variational/BV closure or a newly guessed action. K,J and P_R are parallel;
the original Gamma/j are not parallel when b≠0. In particular the original
strict gauge complex is not assumed to survive this replacement.

Let H=b gamma0 Omega. Then H commutes with gamma1,gamma2,c(l^sharp),
anticommutes with gamma0, and H²=-b². Replace c_N+mu by c_N+H+mu in v_N.
The same gamma trace and divergence vanish. Acting on these transverse fields,
B(e0) Omega_fold equals gamma0 Omega, and

    (B(xi_N)+b B(e0)Omega_fold+mu I)v_N = w_N,
    w_field1=gamma2 R s, w_field2=gamma1 R s,
    R=(mu²-delta²-b²) I + 2 b delta Omega + 2 b mu gamma0 Omega,

with zero ghost/field0/other components. This follows from
(-c_N+H+mu)(c_N+H+mu) and [H,c_N]=2 b delta Omega.
R is independent of N, whereas ||v_N|| still grows linearly. Thus every fixed
constant b, every exponential weight and every scalar shift retains the
non-Fredholm sequence, and fixed-domain spectrum is again all C. The uniform
asymptotic theorem also applies with this limiting zero-order matrix, by the
same error estimate and the modified sequence.

**Whole smooth radial category.** The same conclusion holds for ANY smooth
real beta=b(r)dr, even when b is unbounded. On an escaping compact interval
I_j of length L_j→infinity set B_j=sup_Ij |b| and B'_j=sup_Ij |b'|, both finite.
Use the same v_N(r) with H(r)=b(r)gamma0 Omega. Its pointwise algebraic residual
is R(r) above. Differentiation adds B(e0) partial_r v_N(r), bounded by a fixed
constant times B'_j. The leading term of v_N is still the same N-dependent
nonzero constant spinor; its other terms are bounded by C(1+B_j). Thus for
N sufficiently larger than 1+B_j, its norm on I_j is uniformly between cN
and CN. Normalize the cutoff section by its actual global L2 norm. The result
obeys

    ||(D_b-delta B(e0)+mu)u_j||
       <= C/L_j + C(1+B_j²+B'_j)/N_j.

The constants depend on fixed Clifford matrices, s,delta,mu and cutoff, not j.
Choose an integer N_j at least j times a sufficiently large constant times
(1+B_j²+B'_j), and L_j=j. Then the residual tends to0 and supports escape.
Every section remains in the compact core. This proves non-Fredholmness for
every scalar shift on every closed extension of the entire smooth-radial
category, without imposing asymptotic constancy, a bound on b, or a rate for b'.
It supplies no b-deformed gauge-complex or source-action theorem.

Although beta=b dr is exact, its eliminating residual gauge exp((integral b dr) Omega)
is generally unbounded on the auxiliary unweighted L2 space. It also transports
the named Clifford arrows. We therefore use the direct sequence, never an
invalid bounded-conjugacy assertion. This is a useful composition of two
structural categories, not a common source-action identification. Arbitrary
nonradial/nondecaying matrix potentials remain outside the theorem, and no
massive or b-deformed gauge-quotient claim is made.

## 8. Effect, contrary cases and verification

P3xdomain_boundary and X-P2-P3 gain an exact analytic constraint: a closed
polarized domain or an unchanged local symbol phase does not provide a
Fredholm index on this existing B5 end. Its compact-core obstruction survives
all boundary choices, fixed exponential weights/scalar shifts, the entire smooth-radial compatible
connection category, the stated
asymptotic perturbations, and the strict massless gauge quotient. This neither
refutes nor supplies an inhabited subclass of C and changes no matrix cell to
empty or decided_for_C. The useful new input would change the actual asymptotic
operator/geometry or constrain its bulk domain with a justified physical map.

The universal functional-analytic proof is separate from exact polynomial
symbol checks and finite controls. No finite eigenvalue cutoff proves (2).
The [report](../../lab/process/p3-essential-end-domain.json) distinguishes them.
Run `python tests/program-focus/p3_essential_end_domain_probe.py`.
Independent internal specialist and hostile review check the universal transfer;
no external-expert, Lean, physical or novelty certification is claimed.
