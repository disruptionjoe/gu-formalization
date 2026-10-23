---
title: "K1985: Exact coupled symmetric second jets"
status: active_research
doc_type: exploration
created: "2026-10-23"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no source identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k1985_symmetric_second_jet_compatibility.py
  - tests/channel-swings/k1985_symmetric_second_jet_compatibility_probe.py
---

# K1985: Exact coupled symmetric second jets

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
result: mixed second derivatives extend both stored positive first jets, with a certified positive Taylor neighborhood
carrier: fixed raw1920 section and real128 core in14 flat coordinates LAYER=toy CHIRALITY=N/A
pairing: real symmetric matrix field Q ON=raw_spinor_and_vector_spinor
real_structure: fixed real Cl(7,7) coefficients, not an identified source bar
grading: coordinate derivatives and Clifford volume, not observed chirality
action_owner: repository-construction -- unchanged raw lower-return equation
target: local second-order compatibility MAP-TYPE=intertwiner
```

## Result and exact scope

Both identity-value first jets from [K1979](k1979-multicoordinate-symmetric-pairing-2026-10-23.md)
admit exact, symmetric, mutually compatible second derivatives. This resolves
the coupled second-order question left open by [K1982](k1982-positive-pairing-flux-obstruction-2026-10-23.md).
It does not construct a local solution of the full differential equation.
All coefficients, the raw core and the two mass signs remain fixed.

Write the equation as

    sum_k eta_k (partial_k Q) J_k = R_s(Q),
    R_s(Q)=sum_k eta_k Omega_k^T Q J_k - s Q T,
    eta_k=+1 for k<7 and -1 otherwise; s=+1 or -1.

At the origin Q=I and partial_k Q=H_k are K1979's actual stored jets.
The new unknowns S_kl must satisfy BOTH S_kl=S_lk and S_kl^T=S_kl, and

    sum_l eta_l S_kl J_l = R_s(H_k), for every k.       (1)

The linked JSON gives450 nonzero independent entries per sign, encoded by
(k,l,i,j,value), with k<=l and i<=j. Reflection in each index pair reconstructs
the complete tensor; omitted entries are zero. These exact rational entries
satisfy(1) in the full128-by128 matrices. They are not separate first-order
solutions that happen to share labels.

## Sparse reduction, without importing a Clifford shortcut

The actual J_k are signed weighted permutation matrices, but their squares
are not scalar and J0,J1 do not anticommute. A usual Clifford square would be
a wrong operator here. Instead each symmetric second-derivative entry affects
at most four equation entries. The exact bipartite incidence graph splits the
229376 scalar equations into128 blocks of896 rows and64 blocks of1792 rows.
The actual right sides are supported in just TWO896-row blocks.

Sparse rational elimination on these1792 rows and8064 columns has row rank1792.
Thus the selected blocks are onto. Solving them and setting all other
components to zero gives the stored tensor. The code verifies block closure;
no equation outside those blocks receives a hidden contribution. This is a
rank statement about the two selected blocks, not the rank of the whole
prolonged symbol and not formal integrability at arbitrary order.

The separate probe reconstructs J,Omega,T from the earlier raw implementation
and directly contracts every mixed-derivative equation. It does not import
the new elimination or its graph partition to accept the witness.

## Released consumers: positive Taylor field and exact remaining defect

Define the symmetric polynomial

    Q2(x)=I+sum_k x_k H_k+(1/2)sum_kl x_k x_l S_kl.

For the matrix maximum-row-sum norm put

    A=sum_k ||H_k||,
    B=(1/2)sum_k ||S_kk||+sum_(k<l)||S_kl||,
    r=1/[4(1+A+B)].

The report supplies rational A,B,r for each sign. If max|x_k|<=r, then
||Q2-I||<=rA+r^2 B<1/2. Symmetry therefore gives Q2>=I/2 on the whole cube,
not merely at sampled points. Equations(1) and the known zeroth-order equation
cancel every constant and linear PDE coefficient. The exact residual is

    sum eta_k (partial_k Q2) J_k-R_s(Q2)
       =-(1/2)sum_kl x_k x_l R_s(S_kl).                (2)

It is nonzero as a polynomial. Its norm is bounded by C max|x_k|^2, with
C reported from the same half-diagonal/full-off-diagonal sum of ||R_s(S_kl)||.
A rational-point check independently verifies(2); the coefficient identity
establishes the universal statement.

The two first-symbol cokernel witnesses Z also obey
<Z,R_s(S_kl)>=0 for all105 symmetric coordinate pairs, both signs:420 exact
necessary second-differentiated value conditions. This clears that cheap
third-order prerequisite. It does not provide mutually compatible third
jets, an all-order growth estimate, convergence, or a genuine positive field.
The global bounded/periodic PSD exclusion in K1982 remains valid.

## Verification and boundary

Producer: exact component partition, elimination and full equations for both
signs. Independent probe:454 raw equation/value/Taylor obligations and four
genuine coefficient, mass-sign, mixed-entry and radius faults after a green
baseline. The norm estimates are analytic; the rational point is a control.
Both implementations were run by one author, without external verification.

Strongest overclaim would turn a positive Taylor polynomial into a solution;
(2) explicitly prevents it. A different first jet can have different higher
compatibility. The next substantial question is a structural all-order/local
existence argument or an actual higher obstruction, rather than treating
finite-order survival as a physical pairing. SC-OP-04 ASSERTS candidate grammar;
SC-OP-05 and SC-META-53 remain UNCERTAIN. SC-MAS-01/02 ASSERT scoped stylized
mass claims; none selects this Q. SC-META-56 DISAVOWS the extra odd-action
prerequisite. LT-SM8/LT-GR6b/RA-F1/AC-F1, source and canon do not change.
