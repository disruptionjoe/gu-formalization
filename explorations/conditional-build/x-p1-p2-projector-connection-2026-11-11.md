---
title: Parallel RS projectors retain a real connection one-form
status: exploration
doc_type: structural-result
created: '2026-11-11'
program_target: X-P1-P2
tier: T2
expected_delta: Classify the full K95 projector-compatible connection category and
  its local/global named-arrow transfer.
actual_delta: 'Constrained: a parallel native K95 RS projector permits a real volume-valued
  connection; full named-arrow compatibility and global calibration impose additional
  exact conditions.'
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# Parallel RS projectors retain a real connection one-form

Constrained: a parallel native K95 RS projector permits a real volume-valued connection; full named-arrow compatibility and global calibration impose additional exact conditions.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

program_target: X-P1-P2
tier: T2
expected_delta: Classify the full K95 projector-compatible connection category and its local/global named-arrow transfer.
actual_delta: Constrained: a parallel native K95 RS projector permits a real volume-valued connection; full named-arrow compatibility and global calibration impose additional exact conditions.

```gu-typed-objects
result: full compatible connection and named-arrow transport classification
carrier: native complex128 K95 spinors and V tensor S on a fixed oriented spin manifold LAYER=ambient CHIRALITY=S-FULL-DIRAC
pairing: actual K of signature64plus64; auxiliary positive norm only for exact controls ON=declared_carrier
real_structure: quaternionic J with square minus1; reflected coflip requires parallel positive vector
grading: volume Omega, not physical observed chirality
action_owner: repository-construction -- connection category, no selected action
target: Gamma/j/insertion parallelism and residual-orbit calibration MAP-TYPE=intertwiner
```

## 1. Actual category and prior evidence

Fix an oriented spin pseudo-Riemannian manifold of dimension14 and signature
(9,5), a spin structure, its Levi-Civita spin connection nabla0, and the actual
complex128 spinor bundle S. Reuse K,J,Omega,Gamma,j,P_R from the
[native real-form classification](x-p1-p2-real-clifford-transfer-2026-11-11.md).
K has signature(64,64), J is quaternionic, Omega²=1, J commutes with Omega,
and Omega is K-skew-adjoint. Gamma:V tensor S→S, Gamma j=1 and
P_R=1-j Gamma. K,J,Omega and the original arrows are nabla0-parallel.
The tangent connection is fixed Levi-Civita throughout.

[K1826](k1826-k77-graph-preserving-internal-coefficients-2026-10-20.md)
already owns the even-Clifford commutant argument, not the connection
classification below. [K2248](k2248-indefinite-parallel-localization-2026-10-29.md)
owns indefinite parallel L2/null-pairing constraints on another carrier.
The September1 I1B [connection result](k77-i1b-action-induced-connection-wave-2026-09-01.md)
owns a rank24 quotient connection and its hyperbolic transport; that mechanism
is not claimed as novel. Here the new consumer is the complete native K95
projector-to-full-diagram differential and global transfer.

SC-OP-04 ASSERTS the candidate operator grammar; SC-GEO-55 ASSERTS displacement
from gauge-rotated Levi-Civita, with its source hedge. Neither demands the
parallel-symbol hypothesis below. SC-CHI-01/51 ASSERTS nonchiral-total and
effective-chirality claims; SC-GEN-02/03/54 ASSERTS the separately scoped
2+1/label/extension claims. Independent bars are not identified with K-adjoints.
Ledger0.263 RA-F1, AC-F1 and LT-SM8 remain NEEDS. This is a structural category,
not a chosen action, a proof of class-C membership, or an observed-count map.

## 2. Complete compatible-connection classification

**Theorem.** A complex spinor connection nablaS preserving K and J induces a
parallel P_R on V tensor S if and only if

    nablaS = nabla0 + beta Omega,       beta a real one-form.                 (1)

Write A=nablaS-nabla0. Parallel P_R means
[I tensor A_X,P_R]=0 for every vector X. Compatibility with K,J says A_X lies
in their joint Lie algebra. Exponentiating each A_X gives a one-parameter
family in the previously classified fixed-vector projector stabilizer

    g(a)=a P_+ + a^-1 P_-,             a in R*, P_±=(1±Omega)/2.

Its identity-component Lie algebra is exactly R Omega. Differentiating proves
necessity; Omega commutes with every even Clifford block of P_R and preserves
K,J infinitesimally, proving sufficiency. The coefficient beta is global:
Omega is global and nonzero, and differences of connections are tensors.
This uses the complete prior stabilizer, not a finite candidate search.

Define S_beta by (1), on the fixed underlying S. The gamma-trace quotient
connection on S is S_minus_beta:

    Gamma: V tensor S_beta → S_minus_beta,       j: S_minus_beta → V tensor S_beta.

Indeed Gamma(I tensor Omega)=-Omega Gamma and (I tensor Omega)j=-j Omega.
Thus both arrows are parallel with these opposite connections. If their
spinor source/target connections are instead required to be the SAME nablaS,
their covariant defects are 2 beta Omega Gamma and 2 beta (I tensor Omega)j,
respectively. They vanish iff beta=0. Parallelism of a projector and parallelism
of its named odd arrows are therefore genuinely different conditions.

## 3. Curvature, gauge and global calibration

Since nabla0 Omega=0 and beta wedge beta=0,

    R_beta = R0 + d beta Omega.                                                (2)

Use active gauge convention nabla'=g nabla g^-1. For residual g(a),

    beta' = beta - d log|a|.                                                   (3)

Negative a has locally constant sign and the same differential formula.
Locally beta can be removed iff d beta=0. Globally it can be removed iff beta
is exact. Among residual-flat connections d beta=0, equivalence classes under
this residual gauge group are H¹_dR(M;R). This does not classify the full
Spin/gauge orbit or other spin structures; discrete Z2 twists are not encoded
by a one-form on this fixed bundle. Relative transport around a loop is
exp(-Omega integral beta), so trivial residual holonomy is equivalent to all
periods vanishing; the real exponential has no imaginary period ambiguity.

The residual orbit of calibrated Clifford arrows is

    gamma_t(v)=exp(2t Omega) gamma(v),    t=log|a|.

Their covariant derivative under nabla_beta, including Levi-Civita on V, is
2(dt+beta) Omega gamma_t(v). Hence a global parallel calibration **within this
orbit** exists iff beta is exact; the original arrows are parallel iff beta=0.
The factor2 is a real nonzero weight, so no hidden Z2 period makes a nonexact
beta removable. Arbitrary different Clifford structures are outside this claim.

Three controls separate the conditions. beta=df nonzero has nonparallel
original arrows but admits t=-f. beta=b dtheta on a circle, b≠0, has zero
curvature difference but nontrivial residual holonomy and no single-valued t.
beta=x dy on a plane has d beta=dx wedge dy and no local calibration. These
are connection controls, not source-selected backgrounds or action ansatzes.

## 4. Released full diagram rigidity and coflip consequence

Permit different K,J-compatible connections on one-form spinors zeta and
zero-form spinors nu. When the zeta connection preserves P_R, it is S_beta.
Parallel Gamma/j force the nu connection to be S_minus_beta: Gamma is
surjective, so this quotient connection is unique. Requiring in addition
parallelism of the exterior-insertion symbol

    i_xi: nu → xi tensor nu in V* tensor S_zeta

forces the two spinor connections to coincide. Thus all these named arrows
can be parallel simultaneously only for beta=0. Opposite charges give a
contrary control when insertion is omitted. This is differential rigidity of
the explicitly specified source-ingredient diagram, not a claim that class C
or covariance requires that diagram to be parallel.

A related global consequence can be checked when an extra unit positive vector
v is Levi-Civita-parallel. Let C0=gamma(v)J, the reflected-vector coflip of the
prior note. It obeys C0²=-1, is K-antiunitary and anticommutes with Omega.
For C_t=exp(t Omega)C0, C_t²=-1 and the same antiunitary pairing is preserved.

    nabla_beta C_t = (dt+2 beta) Omega C_t.

Therefore a parallel coflip in THIS orbit exists iff beta is exact. Inert J is
parallel for every beta. Same-square K-antiunitarity and even a parallel RS
projector thus do not make every reflected coflip globally parallel. Without
the parallel v, its own covariant derivative adds another term; there is no
claim that a general curved K95 geometry supplies such a vector.

## 5. Scope, review and reproduction

The result strengthens X-P1-P2 and P2xsymmetry at structural conditional scope.
It removes a pointwise-to-connection shortcut and identifies precisely the
local curvature and global-period requirements left after projector symmetry.
No P1/P2 datum equality, full-C verdict, physical index, positivity or family
count follows. A nonparallel source operator can still be covariant.

The universal proof differentiates an already proved full stabilizer and uses
standard connection/gauge identities. Exact native128 controls, symbolic
connection identities and contrary cases are supporting evidence, not a proof
assistant certificate. Run `python tests/program-focus/x_p1_p2_projector_connection_probe.py`.
The matching [report](../../lab/process/x-p1-p2-projector-connection.json)
is reproducibly checked, including input/code/note hashes. Independent internal
specialist and hostile review passed at this conditional scope; no external-expert
certification or novelty claim is made.
