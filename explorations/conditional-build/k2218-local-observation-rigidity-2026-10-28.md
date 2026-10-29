---
title: "K2218 Local observation rigidity and exact leakage"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: complete local multiplier intertwiners for the supplied scalar coefficient class; no source-selected observation
scripts:
  - tests/channel-swings/k2218_local_observation_rigidity_probe.py
---

# K2218 Local observation rigidity and exact leakage

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
result: K2218 Local observation rigidity and exact leakage
carrier: fixed common-return V1152 real spinor sector complexified over R3 LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: positive reduced L2 form ON=declared_carrier
real_structure: ordinary conjugation in real Cl77 basis; real and complex commutants separate
grading: inherited full Dirac; no physical chirality or family count
action_owner: repository-construction -- supplied conditional operator
target: local bounded multiplier intertwiner algebra MAP-TYPE=intertwiner
```

## Complete variable-coefficient classification

Retain [K2212](k2212-mass-connection-algebra-2026-10-28.md)'s positive sector
V_R=R1152 and its operator on L2(R3;C1152), domain H1:

    H=-i sum Cj partial_j+c(x)S+m(x)M+S b(x).C,
    M=-iA1, S=-iQ, Q=-C1 C2 C3.

The five coefficients are bounded real measurable. The spatial Cj are real
symmetric Clifford involutions; A1 is real skew, squares to -I and
anticommutes with each Cj. No mass sign or gap assumption is needed here.

Every bounded measurable matrix multiplier T satisfying H(T psi)=T(H psi)
in distributions for all compactly supported smooth psi is constant almost
everywhere and commutes with C1,C2,C3. If m is nonzero on a set of positive
measure, it also commutes with M. Conversely all such constant matrices
intertwine H, preserve H1 and commute with its self-adjoint dynamics.

Modulate a test field by exp(ik xj) and compare coefficients of k: [Cj,T]=0.
Thus [T,S]=[T,SCj]=0 and the remaining distributional equation is

    -i sum Cj partial_j T + m[M,T]=0.                 (1)

The three commuting involutions Ad(Cj) act on matrix distributions. The
three derivative terms have characters (+,--),(-,+,-),(-,-,+); the mass
term has character (-,-,-). Character projections separate (1), giving
partial_j T=0 and m[M,T]=0. Connectedness makes T constant. A nonzero mass
set then kills the constant mass commutator. This avoids presuming H1
preservation for an arbitrary measurable multiplier.

## Exact real and complex algebra, including copy mixing

The independent real4 model C1=X tensor I, C2=Z tensor X,
C3=Z tensor Z, A1=Z tensor J uses X=[[0,1],[1,0]], Z=diag(1,-1),
J=[[0,1],[-1,0]]. Its16 words span Mat4(R), establishing the faithful
Cl(3,1) algebra. The actual1152-dimensional module has288 irreducible copies.
This includes arbitrary mixing among all nine inherited128 copies.

| mass class | local algebra | orthogonal projector ranks |
| --- | --- | --- |
| nonzero on positive measure, real | Mat288(R) | real4r |
| nonzero on positive measure, complex | Mat288(C) | complex4r |
| zero almost everywhere, real | Mat288(C) as real algebra | real4r |
| zero almost everywhere, complex | Mat288(C) plus Mat288(C) | complex2(r_plus+r_minus) |

Ranks r,r_plus,r_minus range0..288. In the massless complex case S has two
576-dimensional eigenspaces; ordinary conjugation exchanges them and a real
projector has equal sign-sector ranks. The faithful128 Clifford census gives
2048 real commutant dimensions without mass and1024 with mass; multiplying
by81 accounts for all copy mixing. Algebra classification, not sampled
projectors, proves the complete rank list.

## Quantitative leakage and energy consequence

For T in W1,2_loc with exact [T,Cj]=0, let R be the left side of (1).
Distinct character spaces are orthogonal for the Frobenius inner product:

    ||R||F²=sum ||partial_j T||F²+m²||[M,T]||F².     (2)

No spatial variation can cancel mass leakage. If |m|>=m_star>0, then
E(T)=(T+MTM)/2 belongs to the mass commutant and

    ||T-E(T)||F=||[M,T]||F/2 <= ||R||F/(2m_star).

E need not preserve idempotence: for P=(I+S)/2 it gives I/2. Approximate
principal commutation is outside (2).

Every nonzero local orthogonal invariant sector has energy unbounded in both
directions. Its constant projector commutes with the Cj; C2 exchanges the
C1 plus/minus eigenspaces in its range. A normalized compact bump times one
such vector, modulated by exp(ikx1), has expectation plus or minus k plus
a bounded O(1) term. Hence the restricted self-adjoint operator has no upper
or lower spectral bound. Such a projector cannot select positive energy.
This does not forbid position effects, nonconserved measurements, nonlocal
spectral projectors or a different physical observation map.

## Genuine changed-class escape

On a Clifford4 factor with two multiplicity copies take the real flavor
rotation U(x1)=exp(x1 A), A=[[0,-1],[1,0]], and P0=I4 tensor diag(1,0).
Then U commutes with the principal matrices and mass, but

    H_U=U H U†=H+i C1 A,
    P(x1)=U P0 U†

is nonconstant and intertwines H_U. The added coefficient is Hermitian and
its evolution generator is real. Without that connection, the derivative
residual is nonzero. The probe verifies both cases at a rational rotation
and its exact first jet; the displayed identity proves all x1. This is a
conservative observation/operator pair with the same principal symbol,
inside a broadened multiplicity-connection class. It is not realized by fiat
in K2212's scalar five-image raw connection class. For generic static frames
use [K2215](k2215-variable-mass-gap-2026-10-28.md)'s entire derivative correction.

## Evidence, prior boundary and remaining physics

K2062 already supplies a related local-commutant argument for a free
positive-energy projector on a different1408 carrier; no new generic locality
principle is claimed. Here the full variable common-return operator,
measurable multiplier classification, rank algebra, residual coercivity and
broader-class escape are the result. Exact finite controls support the written
distributional and continuum arguments; they are not a proof assistant.

SC-OP-04 ASSERTS candidate grammar; SC-OP-05 UNCERTAIN rival and SC-META-53
UNCERTAIN spectral handling remain intact. LT-SM3/LT-SM8/LT-GR6b and ledger0.263
are unchanged. This does not identify a source observation, interacting
positive physical quotient, family or chirality count. Next substantive work
is a typed source-admissible observation/operator beyond this local scalar
class or an actual physical nonlocal domain; the constructed flavor term is
an explicit changed assumption requiring its own raw-return test.
