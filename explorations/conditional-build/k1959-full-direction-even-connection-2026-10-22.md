---
title: "K1959: Full-direction even connections on the fixed positive core"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional fixed raw carrier and connection placements only; no physical GU mass exclusion
scripts:
  - tests/channel-swings/k1959_full_direction_even_connection.py
  - tests/channel-swings/k1959_full_direction_even_connection_probe.py
---

# K1959: All fourteen bivector directions and their tensorial repair

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: exact common-bivector leakage classification with pointwise and mixed-parity consumers
carrier: K1951 conditional real1920 raw system and fixed positive128 core LAYER=toy CHIRALITY=N/A
pairing: inherited positive quotient energy, not the source barred pairing ON=fixed_core
real_structure: real Cl(7,7) matrices and common real coefficient fields
grading: intrinsic Clifford parity, distinct from observed chirality
action_owner: repository-construction -- modified zero-southeast principal operator
target: core-preserving zero-order connection contraction MAP-TYPE=intertwiner
```

## 1. Spinor-only class: exact complete exclusion

Let D_k, J and L be [K1951](k1951-coordinated-zero-southeast-principal-2026-10-22.md)'s
actual raw1920 matrices, positive-core injection and its left inverse, LJ=I128.
For k=0,...,13 and0<=a<b<=13 let

    A_k=D_0^(-1)D_k,
    B_ab=I15 tensor(gamma_a gamma_b),
    V(z)=sum_(k,a<b) z_kab A_k B_ab,
    T(z)=(I-JL)V(z)J.                                  (1)

The real parameter space has14*91=1274 coordinates. Its leakage map T has
rank1274. Thus the only common bivector coefficient preserving this fixed
core is zero. No energy or mass equation is required for this exclusion.
It extends K1953's observed-four-direction result; it is not another test
of those364 coefficients alone.

The raw calculation is essential. K1832's E512 compression is not an
invariant raw restriction. Including normal covectors in this zero-order
CONTRACTION does not assert an invariant fourteen-dimensional PDE on J.
The evolution itself still uses the observed directions0,7,8,9.

## 2. Exact certificate and quantitative residue

The scalar-entry support graph decomposes the1274 columns into42 disjoint
blocks:35 of size24 and7 of size62. For each block the report stores selected
raw scalar positions, the square rational minor and its inverse through the
reconstructible selected rows/columns. Multiplying the serialized inverse
by its reconstructed minor gives identity. These minor sizes sum to1274.

The producer verifies full support separation and exact nullspace equations.
The independent checker assembles signed-bit Clifford matrices separately,
reconstructs the opposite-sided raw time inverse and every selected residual,
and checks that ALL selected off-block entries vanish. Checking only42
unrelated minors without off-block separation would not prove the global rank.
It also checks that the column sets partition the entire parameter space and
that selected row sets are disjoint.

The maximum inverse infinity norm over the blocks is exactly

    K=505487620559/71559153.

Consequently the chosen scalar-entry leakage norm obeys

    ||T_selected(z)||_infinity >= (71559153/505487620559)||z||_infinity. (2)

These are explicit coordinate norms, not an invariant physical mass gap.
The arithmetic certificate proves the full real parameter-space statement;
a finite-field pivot search only discovers minors and is not the proof.

## 3. Mixed grades and varying coefficients

K1957 supplies the separate full196 rank for common grade-one coefficients.
Its parity P=diag(I14,-1) tensor omega preserves the fixed core and commutes
with every A_k. Common grade-one actions are odd and bivector actions even.
The induced parity on the quotient raw1920/core128 therefore splits their
leakage maps. If their sum preserves the core, its odd and even parts each
preserve it. Both rank certificates then force ALL1470 real coefficients
to vanish. This concerns the direct sum of the stated grade-one and bivector
classes, not arbitrary even Clifford grades or independent slot matrices.

Because(1) and its rational left inverse are constant, the implication holds
pointwise, almost everywhere for measurable coefficients, and for coefficient
distributions satisfying the linear invariance equation. On the observed PDE,
a frame change J S(x) inside the SAME fixed image contributes only tangential
terms: each observed A_k preserves range J. Frame derivatives cannot cancel
transverse leakage. Changed image, geometry or raw input placement is a new
object and remains outside this statement.

## 4. Tensorial repair

The spinor-only exclusion does not settle the covector-spinor action. Define

    Q_ab=I15 tensor(gamma_a gamma_b)+V_ab tensor I128,
    (V_ab)_ab=2 eta_a, (V_ab)_ba=-2 eta_b,

with every other vector-slot entry zero, including the auxiliary slot.
Replace B_ab by Q_ab in(1). This is K1953's declared tensorial placement,
now tested in all fourteen contraction directions. It is a changed conditional
placement, not a new source identification.

Its leakage rank is1131, with a143-dimensional parameter kernel. The induced
operators M=L V J span91 dimensions. Thus a nonzero core-preserving potential
DOES exist in this class. Impose the actual equations

    M C_i+C_i M=0 (i=1,2,3),    H M+M^T H=0,              (3)

where C_i and H are the inherited positive principal matrices and energy.
The resulting parameter kernel has dimension52, and its induced operator
image is ZERO. In fact143-91=52 already counts the zero-action parameters,
so every mass/energy solution in this class is a redundant zero action.
No nonzero conservative anticommuting Dirac mass is produced. This does not
say that all1131 leakage constraints are independent mass equations, or that
all143 preserving combinations vanish.

The138 support blocks, rational selected minors and full raw kernel vectors
certify completeness. The independent check tests both the lower rank bound
and VJ=JM for EVERY kernel generator; its separate mass-constraint matrix
checks(3), kernel completeness and zero induced image. These are real exact
parameter-space checks, not random coefficient samples.

### Released spacetime gauge family, with a global domain statement

For the explicit temporal label(k,a,b)=(0,1,2), let R=L Q_12 J. Then

    Q_12 J=J R, R^2=-I, H R+R^T H=0, [R,C_i]=0.          (4)

For any real C1 function phi(t,x), put G=exp(phi R) and

    V_phi=[phi_t I-sum_i phi_(x_i) C_i] R.               (5)

This is an actual tensorial connection contraction: use coefficient phi_t
in direction0 and -phi_(x_i) in observed directions7,8,9, all at bivector12.
The independent test checks A_k Q_12 J=J C_k R, with C_0=I, on each of those
four directions, and the H-skewness of their induced terms. The chain rule
then shows that psi=G chi solves

    partial_t psi=sum_i C_i partial_i psi+V_phi psi

exactly when chi solves the free equation. This is a nonzero spacetime-varying
potential with no scattering or mass gap beyond the chosen local frame.
It makes K1955's generic pure-frame observation explicit for these actual raw
coefficients and generalizes K1953's checked time-only rotation; it is
not a classification of every preserving tensor connection.

On R3 or the flat torus, if the first derivatives of phi are bounded on each
finite time interval and phi is C1, multiplication by G and G^-1 preserves
H1, is H-unitary on L2, and conjugates the free evolution to
G(t) U_free(t-s) G(s)^-1. This gives a strongly continuous energy-preserving
propagator with the stated H1 domain. Higher Sobolev preservation requires
the corresponding bounded higher spatial derivatives; it is not inferred
from C1 alone. For example phi(t,x)=f(t)sin(x1), with f C1, meets the finite-
time bounds. Fixed core and observed-four-direction evolution remain essential.
There is no physical-source gauge equivalence or full14 PDE claim.

## 5. Source scope, hostile review and reproduction

SC-OP-04 ASSERTS a candidate four-field operator grammar. SC-MAS-01 ASSERTS
a STYLIZED approximately constant-curvature mass R/4; SC-MAS-02 ASSERTS the
mass-field gauge-potential role with its in-some-sense hedge; SC-MAS-03 ASSERTS
the three-way linkage. WGS05 has no completed full20 placement, barred maps
or physical observation identifying(1) with that entire mechanism. SC-GEO-55
ASSERTS displacement from gauge-rotated Levi-Civita, not ordinary torsion.
These conditional placements are not a falsification of those source claims.
SC-META-53 remains UNCERTAIN; LT-SM8, LT-GR6b and AC-F1 remain NEEDS.
Source, physics-ledger and canon verdicts are unchanged.

Strongest overclaim: all gauge potentials, physical masses or full14 dynamics
are excluded. Only the frozen finite coefficient classes are classified.
Strongest contrary construction: K1951's broader zero-cell mass lift already
exists and is outside the common spinor-only placement; the tensorial class
is tested explicitly rather than excluded by analogy. Weakest reproduction
seam: full raw invariance and the independence of selected blocks; both are
checked on actual matrices, including off-block entries and kernel images.

The two scripts reproduce the exact rational certificates. The producer's
--part spinor and --part tensor modes serialize separate heavy checks;
default checks both against the report. The separate probe uses signed-bit
Clifford assembly, actual generator/order/omission faults and separate matrix
certificate and metadata faults. Analytic pointwise, parity and PDE statements
use the explicitly stated fixed-image hypotheses. Internal verification is
not external expert acceptance or formal proof-assistant certification.
