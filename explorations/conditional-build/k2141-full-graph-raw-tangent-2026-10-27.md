---
title: "K2141: Complete graph first jets against the raw upper class"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: complete tangent obstruction and bounded-coefficient no-departure through P0; no full-chart rigidity or GU recovery
scripts:
  - tests/channel-swings/k2141_full_graph_raw_tangent_probe.py
---

# K2141: Complete graph first jets against the raw upper class

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
result: full conserving graph first-jet compatibility at P0
carrier: K2132 complex32 graph in native K1951 core128 and K2021 full1920 LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: inherited S=iJ*HD0J and the unchanged common-H raw coefficient class ON=declared_core
real_structure: complex adjoint and real1280 first derivatives
grading: t,Z graph multiplicity; not source ambient-half or observed chirality
action_owner: repository-construction -- K2028 raw common-H class with fixed upper contraction
target: complete P0 tangent leakage and inherited-current compatibility MAP-TYPE=intertwiner
```

## 1. The previously untested question

[K2134](k2134-noncircle-current-transport-2026-10-27.md) excludes the noncircle
scalar first jet at u=0, while K2129 excludes the fixed circle. Neither tests
all320 real graph parameters in
[K2132](k2132-conserving-positive-sector-classification-2026-10-27.md).
This computation tests all1280 real spacetime first derivatives simultaneously
at the named P0 sector, keeping the original common-H raw upper coefficient
class. It drops the ENTIRE lower return, so any obstruction cannot be repaired
by a southeast/lower-only modification within this setup.

The complete shared target obstruction has exact rank1280 and survivor dimension0.
Therefore every first derivative of this320-dimensional graph family vanishes
at P0 if it is to satisfy the original raw upper closure and inherited current.
This is stronger than the two previously excluded scalar curves, even with
arbitrary lower return. It is NOT a theorem of global graph rigidity.

The result binds one tangent space and one coefficient class. Even vanishing
first derivatives at P0 does not prove every smooth selector constant, let
alone a global physical exclusion. No raw-class equivariance over the entire
graph chart is assumed. The changed-upper flat and mass-parallel constructions
of K2135/K2138 remain genuine alternatives under changed assumptions.

## 2. Complete native graph tangent basis

Use the actual native C1,C2,C3,M,t,Z,R,Q matrices of K2132, and

    E=(I+t)(I+Z)/4, Y=(I+R)E, P0=YY*/2.

On E, the joint commutant of C1,C2,C3,iM is Mat8(C). Choose a Hermitian REAL
basis H_alpha, alpha=1..64, with H=EHE. At the graph base U=I,B=C=0, the
coordinates are deltaA=X skew-adjoint, deltaB=b and deltaC=c arbitrary complex
8x8. Therefore the320 real frame derivatives are

    deltaY = R(iH_alpha), QH_alpha, Q(iH_alpha),
             RQH_alpha, RQ(iH_alpha).                              (1)

R,Q,RQ identify the four joint t,Z eigenspaces and commute with Cl4. This
is the full tangent of the conserving graph chart, not a scalar-curve ansatz.
In the native signed-permutation representation, a Pauli tag (f,h) means
entry a*(-1)^popcount(i & h) at column i xor f. The six actual generator tags
are extracted and checked against all128 entries, not guessed from labels.
Their centralizer contains256 tags. Quotient by the four-element t/Z
stabilizer yields64 Hermitian E-compressions. Distinct stabilizer cosets are
Hilbert--Schmidt orthogonal on E; multiplying anti-Hermitian tags by i gives
the Hermitian basis. Thus the quotient enumerates all Mat8 Hermitian directions.

For C0=I, the leakage targets are

    T_alpha,mu=-(I-P0) deltaY_alpha Y* C_mu/2, mu=0..3.             (2)

Since Y*Y=2E, T Y=-(I-P0)deltaY C_mu, the exact differentiated-invariance
condition. Normal projection is injective on the graph tangent at P0.
The four spin factors C_mu are linearly independent under the spin trace,
so the four real spacetime copies have dimension1280. The actual target
construction checks the normal condition and frame evaluation exactly.
No arbitrary raw-class U(8) symmetry is used to reduce the coefficients.

## 3. Why the inherited current equations still apply

Write a=9/280 and W=i C1 C2 C3. At this base Y*SY=2aE. For the skew X
coordinate, Y*S deltaY=a(1-3W)X while Y*deltaY=X. Thus

    Y*S(I-P0)deltaY=-3a W X,

which is skew-adjoint because W commutes with X. The b,c directions give zero
for these compressed cross terms. Every C_mu commutes with W and X. Hence
the Hermitian part of the current cross term from (2) vanishes for ALL320
tangents, not merely the old two curves. The P0 same-current equations of
K2134 can be retained unchanged after normal leakage is imposed. The probe
also checks this skewness directly for every native frame derivative.
This is the transfer argument; a matching matrix size would not suffice.

## 4. Complete raw coefficient system and safe coset reduction

The K2028 bank exhausts16620 REAL coefficients:8388 real and8232 imaginary
common-H basis columns. Its original input digests are verified before reuse;
this computation does not claim to have repeated that earlier completeness proof.
Use K2134's exact J_14 coordinate normalization and all14 upper output blocks.
Require their raw residuals (KJ-D0 J A)P0=0, then impose (2) and the same-current
equations. No complement invariance and no lower-return equation are added.

The projector shifts H={0,1,62,63} partition the128 core XOR shifts into32
cosets. An upper output row a has shift f_raw xor flip((D0 J)_a J_14^-1), so the latter
MUST be removed before computing its coset. Leakage and current rows already
use core coordinates. Failing to make this output-row adjustment was caught
by the producer's row-support assertion before any rank result and repaired.
For each coset, one real and one imaginary raw basis representative are also
recomputed from the ORIGINAL gamma-contraction expression on four output
blocks:256 direct checks, independently of the fast grouped contraction.

Each local system sees512--556 raw columns and72 of the SHARED1280 target
columns. Row-normalize by exact integer gcd and eliminate the raw variables
over Q. Retain each target-only row with its ORIGINAL global target ID, then
stack all local constraints. Assigning independent target coefficients per
coset would test a different problem. The final shared target system is what
decides compatibility.

Exact rational and mod101 ranks agree in every local system; the final
rational and finite-field ranks agree too. The certificate stores local
matrix digests, dimensions and ranks, global target labels and any surviving
kernel vectors. All integer products retain the K2134 prebound and guarded
matrix multiplication; no float-rank or finite-difference verdict is used.

## 5. Reproduction, controls and exact ceiling

Run the adjacent probe with numpy, sympy and python-flint, one worker at a
time; default execution recomputes and compares the stored certificate.
`--write` intentionally creates it. Exact source/target normalization and
original contractions are checked before elimination. Controls change the
Hermitian phase, normal projector, target coefficient, Shiab coefficient or
omega coefficient and must fail actual equations after a green baseline;
a crash is not counted as detection.

All32 local augmented-minus-raw ranks are40; the shared global1280-column
constraint matrix has rank1280 over Q and modulo101. There is no surviving
first-jet kernel. Local raw ranks can be deficient (homogeneous coefficients
may remain), which does not weaken the independent target obstruction.
The exact certificate records each individual rank rather than treating
32 independent local target spaces as the global problem.

## 6. Bounded-coefficient no-departure through P0

The first-jet obstruction has a stronger consequence than a pointwise test.
Let z denote local real graph coordinates with z=0 at P0, distinct from
spacetime coordinates. Assume a C1 selector on a connected open spacetime
domain satisfies the SAME raw upper, leakage and inherited-current equations,
and its finite real raw coefficient vector c is locally bounded. If the
selector equals P0 anywhere, it equals P0 everywhere on that domain.

Here is the native-to-smooth-system bridge. Regard Y as a full-column-rank
map from ran E to C128, and take the inverse of Y*Y on ran E. Equivalently
in native128 coordinates put L=(Y*Y+I-E)^-1 Y*,
P=YL, A=A(c), and N=(I-P)(sum_mu C_mu partial_mu Y)L. The equations are

    (KJ-D0 J A)P=0,
    E_leak=(I-P)AP+N=0,
    C_cur=P(SA+A*S)P=0.

With a0=9/280 replace the last row by

    (C_cur-P S E_leak-E_leak* S P)/a0=0.                       (3)

This is equivalent JOINTLY with leakage, not equality of free-standing
current matrices. It is [sym(P S P A P)-sym(P S N)]/a0. At P0,
P0 S P0=a0 P0 and section3 proves sym(P0 S N)=0 for all1280 graph jets.
Thus (3) is exactly the tested scalar-current row at the base point, up to
fixed coordinate identifications. The native equations now have smooth
finite-dimensional real form F(z)c+T(z)Dz=0, with precisely the certified
base matrices. Projectors and the inverse Y*Y are smooth near this chart.

Choose a full fixed left annihilator L0 with ker L0=im F(0). The rank1280 certificate says
L0 T(0) is injective. Smoothness and a positive smallest singular value give

    ||Dz|| <= C |z| (||c||+||Dz||).

Shrink the chart and absorb the last term; local boundedness of c gives
||Dz||<=C'|z|. Around any spacetime point where z=0, continuity keeps z in
this chart and c bounded on a small convex ball. Gronwall along each radial
segment forces z=0 throughout that ball. The preimage of P0 is therefore
relatively open as well as closed, proving the connected-domain statement.
This proof was separately checked by two internal reviewers.

Boundedness is substantive. The abstract scalar equation z'=cz admits
z=t^2 and c=2/t for t!=0, with any finite c(0), through z(0)=0. Its quotient
tangent is injective at0 but it departs because c is not locally bounded.
This is a hypothesis countercontrol, not a native raw realization. The theorem
does not classify selectors avoiding P0 or singular/unbounded coefficients.

## 7. Scope and next consequence

The result is internal conditional mathematics. It neither supplies an
integrable moving solution on the whole graph, proves full-chart rigidity,
selects a physical positive quotient, nor resolves the full1920 principal
domain. The next raw calculation must use a genuinely different base sector
or prove a structural relation transporting this result while preserving the
raw coefficient class. A changed upper contraction remains a distinct route
requiring source/observation justification. Repeating another scalar curve at
P0 no longer supplies independent information once the complete test closes.
SC-OP-04 ASSERTS candidate operator grammar, SC-OP-05/SC-META-53 remain
UNCERTAIN, and SC-META-56 DISAVOWS an odd-action prerequisite. Source polarity,
LT-SM8/LT-GR6b, ledger0.263 and canon are unchanged; no GU recovery or global
GU falsification follows.
