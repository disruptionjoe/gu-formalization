---
title: "Krein-retained order-3 benchmarks and the actual contraction label"
status: exploration
doc_type: structural-result
created: '2026-11-20'
program_target: P3xglobal_index
tier: T2
expected_delta: Defined graded benchmark residues and actual observation-map identification
actual_delta: Retained ghosts do not select a residue; observed imposter is gamma-trace, not horizontal RS
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: approved construction-scope wording only
---

# Krein-retained order-3 benchmarks and the actual contraction label

> **GU-COMPARATOR-ROUTING — scope before inference.** These named benchmark
> constructions do not decide Weinstein's source-native mechanism without an
> explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md`.
> Classification: `INTERNAL_STRUCTURAL_ONLY`.

program_target: P3xglobal_index
tier: T2
expected_delta: Defined graded benchmark residues and actual observation-map identification
actual_delta: Construction/grade fork and source-label mismatch specified; no class or count verdict

Authority: `joe_direct_chat_2026_11_20_b`. Base
`3b5685a5ba679640dd66accbe1768e6b2a7845d4`. Item2steps2/3, internal grade.
[Packet](../../lab/process/work-packets/native-complex-order3-fork-2026-11-20.md) ·
[Exact evidence](../../lab/process/krein-order3-observation-label.json) ·
[Probe](../../tests/program-focus/krein_order3_label_probe.py) ·
[Independent review](../../lab/process/hostile-reviews/2026-11-20-krein-order3-label-review.md).

```gu-typed-objects
result: Nikulin graded-suspension residues and actual horizontal observation of the contraction kernel
carrier: published K3 elliptic benchmark W_t and separately native14 full spinor RS with horizontal4 normal10 split LAYER=UNTYPED CHIRALITY=S-FULL-DIRAC
pairing: positive elliptic Hilbert benchmark with specified even ghost Krein sign; separate cross-grade balanced double and actual K95 tensor form ON=declared_carrier
real_structure: complex equivariant K classes; native Cl(9,5) quaternionic module used only for exact observation maps
grading: index chirality, ghost sign, cross-grade Krein symmetry and observed physical weak chirality are distinct
action_owner: repository-construction -- benchmark comparison; no source action or stabilized RS action built
target: source kernel label versus actual observed summand, not a family count MAP-TYPE=intertwiner
```

## 1. What is and is not defined

"Keep the ghosts and grade them with a Krein form" does not specify an index
complex. A Krein sign is a pairing; the Fredholm index uses domain/codomain
or chirality grading. The spectral invariant also needs its operator,
suspension, equivariant lift and trace convention. We give fully declared
elliptic benchmarks, not a selected source-native complex. No K3-fibered GU
family, source action or stabilized RS action is constructed.

Use the existing Nikulin benchmark: a closed spin K3 with invariant Ricci-flat
metric, symplectic order3 action, six fixed points, the order3 spin lift, and
periodic circle suspension conventions of the July10 rho record. Its closed
Sobolev elliptic realizations are Fredholm. All added trivial spinor copies
carry the same equivariant lift and trivial additional character.

The published relation for geometric gamma-traceless Q is
`ind Q = integral Ahat(TX)(ch(T_C X)+1)`; it differs from the ghost-subtracted
comparator's `T_C−1`. [Homma–Semmelmann, §3 eq(11), Prop3.1 and Rem3.6](https://arxiv.org/html/1804.10602v1)
was checked directly. The equivariant Q symbol comparison and mod-Z suspension
scope are the existing [adjudication](../../canon/gamma-traceless-38-adjudication-RESULTS.md),
not a new identification of Q with a direct-sum operator.

## 2. Exact retained-ghost fork

Define `E=(S⊗T_C X)⊕S`, `D_E=diag(D_T,D)`, common elliptic Sobolev domain,
and fundamental symmetry `K_g=diag(+1,−1)`. Both summands remain present.
`D_E` is Hilbert-self-adjoint and K_g-self-adjoint. There are at least two
index gradings compatible with these data:

- `G_+=diag(Gamma,Gamma)`: positive chirality supertrace gives class `T_C+1`.
- `G_−=diag(Gamma,−Gamma)`: reversing the retained spinor's index grade gives
  class `T_C−1`. Equivalently this is the K_g-weighted chiral supertrace.

**K_g commutes with both gradings. It is not the native cross-chirality K
of Item1.** This comparison proves only that ghost retention and an
indefinite pairing do not select subtraction versus addition. It is not an
admissibility certificate for the source's actual pairing/operator class.
The plus construction shares B's equivariant index/symbol class in the cited
benchmark; it is not literally the geometric Q operator or bundle.

For a general signed multiplicity t, `W_t=T_C+t·1`, positive copies retain
Gamma and negative copies retain the field with reversed index grade. Then

```
I_t = -40 + 2t
fixed-point twist character c_t = -2 + t
ind_g(D_Wt) = 2c_t = -4 + 2t
Ind_Z3(D_Wt) = (-16+2t)·1 -12·zeta -12·zeta²
rho_k mod Z = -k I_t/3 mod Z = k(1+t)/3 mod Z.
```

These are virtual index multiplicities, not dimensions of a physical particle
space. The equivariant formula follows from the six identical local Dirac
contributions1/3 and `tr(g|T_C)=−2`. The bulk formula follows from
`ch(T_C)=4+p1`, `Ahat=1−p1/24`, `integral p1=3sigma=−48`.

The independent suspension check uses circle eta `e(0)=0`, `e(1/3)=1/3`,
`e(2/3)=−1/3` and sums `m_j[e((j−k)/3)−e(j/3)]`. Its values are
`(0,(4−2t)/3,(−4+2t)/3)`, agreeing modulo integers with the index formula.
Explicitly suspend using `Dcal_G = D_E + G(-i d/dtheta)`, with the
declared equivariant flat-character boundary condition giving shifts
`(j-k)/3`. Its square is `D_E^2 - d^2/dtheta^2`; nonzero fiber eigenmodes
cancel in eta, leaving the graded kernel multiplicities used above.
This is the **graded additive suspension rho with the declared grade**.
Changing G changes this suspended/graded operator prescription; it does not
change the ordinary ungraded eta of an unchanged D_E by relabeling its fields.
Kernel h is separate, not folded into rho. No Z/24 normalization is inferred.

| Declared class | t | Index | Fixed twist character | rho mod Z (k=0,1,2) |
|---|---:|---:|---:|---|
| A / retained spinor with reversed index grade | −1 | −42 | −3 | (0,0,0) |
| B symbol class / retained spinor with same index grade | +1 | −38 | −1 | (0,2,1)/3 |
| bare T_C control | 0 | −40 | −2 | (0,1,2)/3 |
| two same-grade spinors control | +2 | −36 | 0 | (0,0,0) |
| two reversed-grade spinors control | −2 | −44 | −4 | (0,2,1)/3 |

Thus vanishing occurs iff `t≡−1 mod3`; the −3 argument applies to A but not
B. Neither keeping fields nor the word "Krein" fixes t. Nonzero B is prior
knowledge; the reusable delta is the explicit retained-field grading fork
and its exact mechanism, not first discovery of B.

### Cross-grade Krein control

A distinct, more native-shaped structural control is a balanced double of
any such closed odd self-adjoint benchmark Q0:
`D_b=diag(Q0,Q0)`, `G_b=diag(Gamma,−Gamma)`, `K_b=[[0,1],[1,0]]`.
K_b is an equivariant invertible cross-grade symmetry, commutes with D_b and
preserves its actual domains. Both copies remain present. The equivariant
index and the graded suspension rho cancel identically, including every
order3 component. This is **pair cancellation**, not the A twist-character
mechanism. Neither this doubled field content nor its domain symmetry is
asserted to be the source total operator.

More generally the Item1 cross-grade balance would force zero equivariant
index if its domain isomorphism also intertwines the order3 action. No W_t
above admits such an equivariant symmetry: its nontrivial isotypic index
coefficients remain−12 for every t. Even choosing t20 to make ordinary
index0 would leave equivariant imbalance. This exposes an exact extra
hypothesis, rather than transferring the even ghost-Krein example to native K.

## 3. Actual contraction map: the imposter is not horizontal Q

Apply T05/T14 to the source, keeping the two label statements separate:

- SC-GEN-50's tentative spoken kernel label names the **ambient**
  `R_Y=ker Gamma_Y`. It is gamma-traceless upstairs as a bundle definition.
- SC-GEN-03's draft Eq12.22 underbrace names only the mixed spinor term
  `S_H⊗S_N`, the imposter. It is not the entire ambient kernel.
- SC-GEN-52 remains UNCERTAIN; this calculation does not settle its spoken
  second-generation label. The draft and spoken labels are not silently merged.

Use precisely the existing [native observation](native-rs-observed-compatibility-2026-11-11.md):
`V*=H*⊕N*`, dimH4, dimN10, full complex spinor S of dimension128;
`Gamma_Y=Gamma_H+Gamma_N` and literal q keeping horizontal one-form components.
Metric-dual Clifford insertions i_H,i_N obey `Gamma_H i_H=4`,
`Gamma_N i_N=10`. Define the mixed summand injection

```
I(psi) = (10 i_H psi, -4 i_N psi).
Gamma_Y I = 0,    q I = 10 i_H,    Gamma_H q I = 40 Id.
```

Therefore q is injective on this imposter summand and sends it into the
horizontal **gamma-trace** space. It is not the horizontal gamma-traceless
carrier. This is a map calculation, not a dimension-only argument.

Indeed q:R_Y→H*⊗S is onto, since
`r(b)=(b,−i_N Gamma_H b/10)` is a right inverse. Its kernel is the normal
RS summand. The bundle decomposition has dimensions

```
R_Y:1664 = (R_H⊗S_N):384 + (S_H⊗R_N):1152 + imposter:128
observed H*⊗S:512 = horizontal RS cousin:384 + gamma-trace:128.
```

The horizontal RS cousin, not the imposter, is the gamma-traceless summand.
Even it is twisted by S_N; a dimension12 intrinsic Spin4 Q on K3 with index−38
is not automatically this dimension384 bundle with its normal connection.
The source's separate zero-form spinor and couplings remain separate; this
calculation does not identify the whole physical weak-current quotient.

The operator mismatch is sharper than the labels: on the actual canonical
projected-symbol quotient, `Qbar_xi=c(xi)−(2/14)i_H i_xi`, while intrinsic
horizontal Q uses2/4. On `ker Gamma_H`,
`Gamma_H Qbar_xi b=(10/7)i_xi b`, which is nonzero for explicit b.
Thus Qbar does not even preserve the horizontal gamma-traceless subspace in
general. A source-selected coupled completion might behave differently; it
is not identified or built here. Full differential/domain descent remains
an independent obligation.

## 4. Disposition and joint question

**No packet kill.** The defined retained-ghost benchmarks have different
residues; no source-native complex has been uniquely selected. The cross-grade
balanced control vanishes by a different mechanism. The map-level imposter/Q
identification fails on the named observation, while the ambient kernel label
is true upstairs. Neither establishes the two conjuncts needed for a
native packet kill. In particular "all three constructions are2-primary"
would contradict the already-established geometric B result.

No P3 row retype, scientific cell-status change, class-C restriction, source
verdict or prediction credit. Hom(Z/3,Z)=0 remains intact. Item1 gives an
integer cancellation only if its same-grading zero-total and Fredholm/count
premises hold. A new map from such an integer to this particular mod3 datum
would need to be constructed and verified. Integer3 itself reduces to0.

**Next ready:** packet step4, the typed joint X-D1-P3 bridge question; it
must keep integer observable, graded benchmark and observation map distinct.
The existing source/native operator-selection residual is information to
resolve, not an instruction to build a forbidden source action.

## 5. Approved wording and verification

Joe-approved corrections apply to the ten canon files recorded in the evidence
JSON: A-zero/B-nonzero/native-open in their scope notes, plus direct headline,
table and inference corrections where stale universal wording occurred.
Historical calculation values and document acceptance status are retained.
No paper, frozen release or Zenodo text changed. No CANON.md promotion.

The probe independently checks the index-character and circle-spectrum routes,
all integer-t congruences, contrary retained-field gradings, cross-grade
cancellation, and the actual128-dimensional Clifford insertion/observation
identities. No native analytic-domain claim is certified by those finite
checks. Independent specialist review and native postflight gates are
required before acceptance; the linked review records the final disposition.
