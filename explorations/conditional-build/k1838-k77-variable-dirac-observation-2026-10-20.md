---
title: "K1838: variable coefficients, fixed differential observation and moving-frame repair"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact conditional compressed PDE interface; no source observation, physical mass selection or curved-domain transfer
---

# A pointwise lift does not automatically lift a variable coefficient

For K1836's fixed first-order observation, every compatible target coefficient
B(t,x) must be spatially constant. Time dependence is allowed. This statement
covers all pointwise lifts, including nonconservative ones, and cannot be
repaired by their invisible coefficient freedom or by adding a zeroth-order
observation while retaining those pointwise lift equations. It is a statement
about this fixed observation, not all local observations: an explicit moving
orthogonal frame gives a spatially varying mass orientation with the required
connection terms and a local observation.

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
result: necessary and sufficient variable-coefficient jet compatibility and exact moving-frame repair
carrier: one corrected compressed real16 module with real4 target; 32 copies for E512 LAYER=toy CHIRALITY=N/A
pairing: fixed positive source H and Euclidean target energy ON=real_smooth_fields
real_structure: real rational matrices, real coefficient fields and orthogonal target frames
grading: differential order only; no physical cohomology grading
action_owner: repository-construction -- conditional compressed evolution and demand-selected Dirac target
target: local differential observation and its full coefficient jets MAP-TYPE=quotient
```

## 1. Source boundary and exact setup

SC-OP-04 ASSERTS a four-field candidate operator; SC-OP-05 remains UNCERTAIN
about the southeast rival. SC-MAS-01 ASSERTS a **stylized** mass R(y)/4 where
curvature is approximately constant; SC-CHI-02 ASSERTS the stylized coupled
Weyl toy. These do not identify K1836's compressed operator or derivative
observation with source observation. The source pack, WGS-05, explicitly
leaves that bundle-map identification open. SC-META-53 remains UNCERTAIN.
No source claim, adherence, physics ledger row, or canon verdict changes.
RA-F1, AC-F1 and LT-SM8 remain NEEDS. This is no adverse verdict against the
source toy and gives no physical mass or observed chirality count.

Use the actual rational matrices A_i, H, T_i, D_i from
[K1836](k1836-k77-differential-dirac-quotient-2026-10-20.md), with d_i=D_i/24.
On smooth real fields on an open spacetime patch, set

```
P=partial_t + sum A_i partial_i + C(t,x),
Q=partial_t + sum d_i partial_i + B(t,x),
O=sum T_i partial_i.
```

A_i,d_i,T_i are fixed. Coefficients C,B are C1, and the initial identities
T(xi)A(xi)=d(xi)T(xi) hold coefficientwise. We study the exact operator
identity O P=Q O, not a sampled or on-shell rank comparison. Smooth compactly
supported fields give the algebraic test domain. Global boundary conditions,
source barred pairing and physical quotient remain separate.

## 2. Complete first-jet compatibility

The product rule gives

```
O P-Q O = sum (T_i C-B T_i) partial_i + sum T_i partial_i C.       (1)
```

Thus the identity is equivalent to

```
T_i C=B T_i for i=1,2,3,
sum T_i partial_i C=0.                                          (2)
```

There is no time derivative of C or B in (1), since O differentiates only
spatially. Differentiating the first equations of (2) rewrites the last as

```
sum (partial_i B) T_i=0.                                        (3)
```

Stack W=(T_1;T_2;T_3), a 12-by16 matrix of rank12 in every coordinate type.
It has the explicit right inverse

```
R=H^-1 W^T (W H^-1 W^T)^-1, W R=I12.
```

Equation (3) is [partial_1 B,partial_2 B,partial_3 B] W=0. Multiplication
by R proves **each partial_i B=0**. Conversely, these three conditions and
the pointwise equations imply (1) vanishes. This is a complete classification
of the variable dependence for the fixed observation, not only a single-mass
example. The derivative map from all48 entries of the three target first
jets to a 4-by16 defect is injective; the certificate checks rank48 directly.
On each connected spatial component B may be any function of time.

## 3. Test the available repairs before broadening the obstruction

**Invisible source coefficients.** K1836 supplies a pointwise lift C0(B).
Every other lift is C=C0(B)+K, with T_i K=0 for each i. Differentiation gives
T_i partial_j K=0 for ALL i,j, so arbitrary varying K cannot cancel (3).
They are nevertheless genuine allowed variable source coefficients when B is
spatially constant. Nonconservatively their pointwise space has dimension64.
For H-skew coefficients the invisible space has dimension6. Put P_N=I-RW;
P_N is the H-orthogonal projection onto N=ker W of dimension4. An H-skew
invisible K obeys P_N K=K=K P_N, hence is precisely a skew endomorphism on N.
All six directions may have arbitrary spacetime-dependent scalar functions.
This supplies a nonconstant positive-energy source family with the same target,
not a claim that the source dynamics itself must be constant.

**Zeroth-order observation correction.** Let O'=O+S(t,x) while retaining
the pointwise lift equations T_i C=B T_i. The first-order defect becomes
S A_i-d_i S. K1836's complete constant-observation system has kernel zero.
This applies pointwise, so S=0 everywhere. Its derivatives then vanish too.
Consequently no such S repairs the gradient defect. If the pointwise lift
conditions are relaxed, the equations instead become

```
T_i C-B T_i+S A_i-d_i S=0,
sum T_i partial_i C+S C-partial_t S-sum d_i partial_i S-B S=0.     (4)
```

These equations admit a complete pointwise first-order parametrization.
For arbitrary B and S define V_i=B T_i+d_i S-S A_i. Then
C=R(V_1;V_2;V_3)+K with W K=0 solves all first-order equations.
The space of triples (C,B,S) therefore has dimension64+16+64=144 at a point.
The last equation of (4) is a genuine remaining differential compatibility
condition, not an additional pointwise rank. The next sections construct two
solutions; we do not claim general nonlinear PDE solvability.

**Time-varying masses.** With B=m1(t)B1+m2(t)B2 from K1836, its pointwise
conservative lifts are permitted. The first-order energy remains conserved
on a torus, or for decaying fields on R3, because B is skew and d_i symmetric.
Squaring the time-dependent target gives

```
psi_tt-Delta psi/576+(m1²+m2²)psi+B_t psi=0.                       (5)
```

The B_t term cannot be omitted. This is not an arbitrary scalar Klein-Gordon
system, nor a selected curvature profile. Spatially varying m1,m2 with this
fixed observation must both be constant spatially by the stronger all-B result.

## 4. Released follow-through: moving-frame local repair

Let J=D1 D2 D3. It is skew, J²=-I, and commutes with every D_i. For ANY
smooth real s(t,x), use the rational orthogonal frame

```
F=(I+s J)(I-s J)^-1.
```

Its inverse exists for all real s, F^T F=I, and F commutes with the spatial
Dirac matrices. Start with one constant mass matrix B*=B1 and a constant
compatible lift C*. Keep P fixed, but set

```
O_F=F O,
B_F=F B* F^-1-(partial_t F)F^-1-sum d_i(partial_i F)F^-1,
Q_F=partial_t+sum d_i partial_i+B_F.                             (6)
```

Direct product-rule substitution proves Q_F F=F Q and O_F P=Q_F O_F.
Thus a first-order local observation with variable leading coefficient works.
The conjugated mass M=F B* F^-1 stays anti-Clifford and M²=-I. Its orientation
varies spatially; its magnitude does not. The remaining terms in (6) are the
necessary connection terms. Leaving them out gives a nonzero defect for,
for example, s=x1+t x1². Every term of B_F is skew: the connection generator
is a scalar multiple of J, which commutes with each symmetric d_i. The target
retains its positive conserved L2 norm on boundary-free/decaying domains.

The connection Gamma_mu=(partial_mu F)F^-1 has pure-frame curvature zero,
with the sign convention

```
partial_mu Gamma_nu-partial_nu Gamma_mu-[Gamma_mu,Gamma_nu]=0.
```

This is an exact counterexample to any overbroad claim that spatially varying
target coefficients or masses are impossible. It does not choose a physical
gauge symmetry, produce a varying mass magnitude, identify R(y)/4, or solve
the curved source problem. The same construction preserves the observation's
nonzero-frequency rank and its original derivative/zero-mode limitations.

## 5. Further repair: keep the leading observation and vary its lower term

There is an exact repair even with the leading T_i fixed, once the pointwise
lift assumption is relaxed. Simultaneously conjugate source and target by the
same positive scalar function exp(f(t,x)). Starting with P0,Q0,O, define

```
P_f=exp(f) P0 exp(-f), Q_f=exp(f) Q0 exp(-f),
O_f=exp(f) O exp(-f)=O-sum T_i partial_i f.
```

All principal coefficients A_i,d_i,T_i remain unchanged. The lower terms are

```
C_f=C0-f_t I16-sum A_i f_i,
B_f=B0-f_t I4-sum d_i f_i,
S_f=-sum T_i f_i.                                              (7)
```

Associativity proves O_f P_f=Q_f O_f. For a direct polynomial control take
C0=B0=0 and f=x1²: C_f=-2x1 A1, B_f=-2x1 d1, S_f=-2x1 T1.
This violates the separate pointwise lift equations but satisfies both full
equations (4), including the derivative of S. It is a nonconstant target
coefficient with a fixed leading local observation, so omitting the hypothesis
of section3 would produce a false no-go.

This scalar conjugation changes the energy pairing to exp(-2f)H on the source
and exp(-2f)I on the target. Their positive weighted energies equal the
original energies exactly under field transport. On a torus a smooth periodic
f gives bounded invertible multiplication and transports the standard domain.
For unbounded f on R3, no unweighted Sobolev equivalence is asserted; use the
transported domain or compactly supported smooth tests. The new potential
contains the identity and spatial Dirac matrices, not a selected anti-Clifford
mass of variable magnitude. Neither this repair nor (6) supplies the source
curvature-to-mass map. The full system (4) remains the next meaningful test
when an actual lower-order source packet is supplied.

## 6. Evidence, review and next condition

```
sage -python tests/channel-swings/k1838_k77_variable_dirac_observation.py
sage -python tests/channel-swings/k1838_k77_variable_dirac_observation_probe.py
```

Exact rational right inverses, all48 gradient ranks, all64 zeroth-correction
unknowns, invisible subspaces and rational moving-frame identities support
the written product-rule proof. The separate probe applies the operators to
polynomial fields and reconstructs independent finite-field rank controls.
Reporting mutations are counted separately. No numerical sampling proves the
continuum statement; (1)-(6) and their hypotheses do.

Hostile review checks the missing time derivative, pointwise lift assumption,
invisible-coefficient derivatives, S versus moving principal observation,
energy-skew versus scalar mass, curvature sign, and zero-frequency recovery.
The obstruction is repaired by changing the observation with its connection,
so it is not a local-observation or source no-go. No unresolved issue in this
stated fixed-observation classification; no separate-agent or external review,
novelty claim or canon promotion.

Next test non-frame solutions of (4), or a genuinely source-owned
moving observation and same-background coefficient packet. A pure-frame phase
rotation cannot supply a nonconstant mass magnitude. Derive that mechanism and
its pairing/domain before attaching a physical curvature or chirality verdict.
