---
title: K95 quaternionic compatibility retains charged Lorentz-vector mixing
status: exploration
doc_type: structural-result
created: '2026-11-24'
program_target: X-P1-P2-P3
tier: T2
expected_delta: Complete the previously open quaternionic restriction on horizontal covariant mixing
actual_delta: Twelve-real-dimensional complete block-Lorentz class; axial real-Clifford member has full
  observed support and endogenous covariance
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
class_covered: Horizontal Lorentz-vector, fixed normal-SM-neutral, ambient-odd, K95-sharp-skew, quaternionic-compatible
  endomorphism-valued one-forms
premises:
- 'lab/sources/source-claim-register.yaml SC-GRP-02/03/06, SC-FER-05/07 and SC-CHI-01/04/51/52: source
  full-U parent and effective split, not physical on-shell response'
- 'explorations/conditional-build/ambient-correlated-grading-control-2026-11-24.md: fixed K95 H(3,1)+N(6,4),
  proper block Lorentz, actual C and Krein laws'
- C-compatible connection is an additional conditional restriction; source fullU is larger
source_bridge:
  status: conditional
  reason: Tests an additional reality restriction on source-compatible primitive tensor values, not a
    selected physical fluctuation space or current.
kill_condition: An empty class would constrain this added reality-compatible category only. The computed
  survivor does not establish physical modes, rates, failure of effective decoupling or a source verdict.
---

**Correction, 2026-11-26:** The theorem and probe below use the PLUS/reversion K95 pairing, not the printed source's MINUS/conjugation adjoint. The complete horizontal dimension12R survives in the minus adapter, but its coefficients are real with plus-related conjugate halves and its simple witness is c_H(X), not real c_H(X)omega_H. Preserve the original calculations as plus-comparator evidence. C is a minus-pairing anti-isometry; do not import the Sp label. [Current derivation and exact check](source-adjoint-spinless-placement-2026-11-26.md#horizontal-companion).


program_target: X-P1-P2-P3
tier: T2
expected_delta: Complete the previously open quaternionic restriction on horizontal covariant mixing
actual_delta: Twelve-real-dimensional complete block-Lorentz class; axial real-Clifford member has full observed support and endogenous covariance

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.



# Reality does not eliminate the source-parent mixing tensor

**Result.** Within the declared fixed-splitting class, there are exactly
**12 real parameters**. A particularly simple member is

`alpha(X)=c_H(X) omega_H`,

where `omega_H` is the **real horizontal Clifford volume**, not the complex
chirality `chi_H=i omega_H`. It is quaternionic-compatible, Krein-skew,
ambient-odd, and neutral under the entire normal spin action. Its actual
source NE observation has complex rank128, and rank64 from each ambient
half. Adding the optional K95 reality restriction does not confine these
currents to sterile support or force ambient-sector preservation.

This is a field-type theorem, not an excitation, rate, decoupling failure,
physical family count or source-level falsification. The source declares the
larger full U(64,64) parent; it does not require all its connections to preserve
the quaternionic structure. The theorem tests that stronger restriction
without attributing it to the source.

```gu-typed-objects
result: Complete local reality-compatible vector-tensor class and actual NE support
carrier: K95 full complex Dirac S128 and independent scalar/form fields LAYER=ambient+observed BRIDGE=actual-horizontal-and-gamma-contraction CHIRALITY=S-FULL-DIRAC
pairing: actual indefinite K95 Krein pairing; independent density-dual bars ON=declared_carrier
real_structure: quaternionic C²=-1 commuting with real Clifford vectors; no Majorana fixed space
grading: ambient Omega; chi_H=i omega_H; no physical weak-current identification
action_owner: source-print primitive connection variation, not a selected full action
target: source NE vertex and q=(P_H,Gamma_Y,identity) MAP-TYPE=contraction
```

## 1. Exact class and source custody

Work at a point of the oriented K95 observation split `H(3,1)+N(6,4)` on the
full rank128 complex spinor. Fix the actual normal compact SM reduction.
Reuse the established branching `S=(H_L+H_R) tensor (F+Fbar)`, where F is the
normal16 with Q, d^c, u^c, L, e^c, n^c and Fbar its conjugate. This does not
replace the source's 2+1 provenance by repeated families. The two sterile
lines remain distinguished by normal chirality.

The complete classified space consists of real-linear maps
`alpha:H_real -> End_C(S)` satisfying:

1. Tensor equivariance under connected proper **block** Lorentz on H.
2. Commutation with the fixed normal SM action for every real X.
3. `{alpha(X),Omega}=0`.
4. `alpha(X)^sharp=-alpha(X)` for the K95 pairing.
5. `[alpha(X),C]=0` for the fixed antilinear quaternionic C.

All complex endomorphisms are included, not just a bounded Clifford-degree
ansatz. This is a finite-dimensional local tensor class, not a classification
of all natural differential operators, background functions or dynamics.
Normal one-form components, an altered reduction, K77, Pin/parity, and physical
domain/quotient restrictions are separate. The 12-parameter completeness
statement is for **block Lorentz**. The explicit volume witness below also
passes endogenous graph Lorentz; no blanket endogenous completeness follows.

SC-GRP-02/03/06 and SC-FER-05/07 authenticate the full parent, geometric normal
reduction and correlated representation. SC-CHI-01/04/51/52 concern effective
behavior. Neither exact sector preservation nor the added C-preserving
restriction is inferred from them. Bars remain independent as in eq9.16.

Prior coverage: November13 `source-joint-symmetry-current` classified all
scalar odd intertwiners, leaving a sterile rank8 SM residual. November24
`source-small-vev-current-test` imposed K95 sharp-skew on that scalar class
and exhibited `i c_H(X)` in the larger vector-tensor category. Both left the
quaternionic intersection open. The old `i c_H(X)` is C-odd and does not
establish the present result.

## 2. Completeness and the 12 real parameters

Let `E_j`, j=1,...,12, project onto the normal-chirality-resolved SM
irreducibles: six in F and six in Fbar. Let `bar j` denote the conjugate
irrep in the opposite normal chirality. Each occurs once, including the two
separately labelled sterile lines. Their dimensions are `(6,3,3,2,1,1)` in
each half. Every Lorentz-vector intertwiner in the declared class has the
unique form

`alpha(X)=c_H(X) A`,
`A=sum_j (a_Lj P_L E_j + a_Rj P_R E_j)`.                 (1)

**Completeness.** After complexification, the Lorentz vector occurs once
in each of `Hom(H_L,H_R)` and `Hom(H_R,H_L)`, and not in either diagonal
endomorphism space. Clifford multiplication supplies those two nonzero
intertwiners. Ambient oddness with horizontal oddness requires the remaining
normal map to preserve normal chirality. Schur's lemma gives one scalar per
normal irreducible. It prohibits mixing the two sterile lines here because
they have opposite normal chirality. The complex coefficient space before
sharp/reality conditions has dimension24. No higher Clifford tensor lies
outside this all-End classification.

The actual K95 laws are

`c_H(X)^sharp=c_H(X)`, `P_L^sharp=P_R`, `E_j^sharp=E_j`,
`C P_L C^-1=P_R`, `C E_j C^-1=E_barj`.

The E_j sharp law follows from the compact normal group and its
normal-chirality-preserving nondegenerate pairing, not positive physical
states. Horizontal Clifford multiplication swaps P_L and P_R and commutes
with E_j. Substituting (1) into sharp-skew therefore gives independently

`a_hj + conjugate(a_hj)=0`.                            (2)

Quaternionic compatibility gives

`a_R,barj=conjugate(a_Lj)`.                            (3)

Thus, with arbitrary real t_j,

`A=i sum_j t_j (P_L E_j - P_R E_barj)`.                (4)

The 12 directions are independent: their P_L restrictions have distinct
nonzero supports. Equations (1)–(4) prove necessity and sufficiency. C²=-1
adds no further condition on these complex-linear commuting maps.

## 3. Exact support and actual observation

For each nonzero t_j, A acts nontrivially on `H_L tensor E_j` and
`H_R tensor E_barj`, each of dimension2 dim(E_j). Distinct j have disjoint
supports. Hence

`rank_C A = 4 sum_(j:t_j!=0) dim(E_j)`.                (5)

Each paired support lies in one ambient input half because conjugation flips
both horizontal and normal chirality. There are six parameters in each
ambient input half; each half has maximal rank64. All 12 nonzero gives
rank128, with charged and sterile support. For nonnull X, alpha(X) has the
same rank since c_H(X) is invertible; no such claim is needed for null X.

Let J_H be metric horizontal Clifford insertion, `Gamma_H J_H=4I`. The
source NE primitive variation on the independent scalar is
`delta D_NE[alpha] nu=J_H A nu`, up to stipulated nonzero coefficient e.
The **actual** observation gives

`q delta D_NE[alpha] nu=(J_H A nu,4A nu,0)`              (6)

in `(b,tau,nu)`, or `(J_H A nu,0,0)` in `(b,sigma,nu)` where
`sigma=tau-Gamma_H b`. Equation (6) has exactly rank(A), the same kernel
and charged support. This uses the existing contraction q, not a projection.

Independent barred fields detect a nonzero primitive vertex under the
nondegenerate density pairing. A selected physical current or solution/dual
quotient may remove it; those rows and unsuppressed excitations are not
source-selected by this calculation. Nonzero NE support does not establish
q-closure of every block of the fully fluctuated operator.

## 4. A survivor without selecting a normal complex structure

Take the real oriented horizontal volume

`omega_H=c(e_0)c(e_1)c(e_2)c(e_3)`, `omega_H²=-I`,
`chi_H=i omega_H`, so `omega_H=-i chi_H`.

The fixed quaternionic C commutes with every real factor and thus omega_H.
Reversing four sharp-selfadjoint factors has six inversions, so
`omega_H^sharp=omega_H`. It anticommutes with horizontal c_H(X), commutes
with ambient Omega and commutes with every normal Clifford vector. Therefore

`alpha_*(X)=c_H(X) omega_H`

is C-compatible, K95-sharp-skew and ambient-odd. It commutes with every normal
even Clifford action, including SM, with no extra normal vector, complex
structure, VEV or scalar background selected.

Horizontal volume is proper-Lorentz invariant; alpha_* is a Lorentz-vector
tensor. Every endogenous graph-Lorentz correction acts through normal even
Clifford algebra and also commutes with it. This proves endogenous covariance
of this member, without upgrading the full block-Lorentz classification.

Equation (4) contains it at `t_j=-1` for all j. Directly,

`alpha_*(X)^2=g_H(X,X) I`.

Its observation `(J_H omega_H nu,4omega_H nu,0)` has a left inverse from
the trace slot `(-omega_H/4)`. Rank128 and rank64 per ambient input half
follow exactly. After multiplication, the tensor is a real horizontal
three-Clifford type, distinct from the old C-incompatible imaginary vector.

Spatial parity changes the tensor requirement: omega_H is orientation
sensitive. This is the declared oriented proper Spin setting, not a
Pin-natural theorem.

## 5. What this closes, and what the next test still needs

**Closed implication:** K95 reality, Lorentz covariance and SM neutrality
do not by themselves suppress all ambient-odd primitive currents. The
counterexample also passes endogenous Lorentz. The complete class identifies
exactly why the scalar sterile-rank argument is inapplicable to this tensor.

**Remaining physical burden:** source-owned allowed fluctuations, a
constrained gauge/solution quotient, actual density/readout and propagator,
coupling and domain estimates. The tensor can be absent or suppressed in
that physical support. No measured response follows from a permitted local
coefficient. Full-U alone establishes neither excitation nor suppression.

At fixed geometry a connection variation changes only lower differential
order, leaving the principal symbol unchanged. A verdict based solely on
the principal-symbol/K-class cannot distinguish presence from absence of
this tensor or supply the missing current restriction. This does not assert
that all noncompact Fredholm domains or kernel dimensions survive a
lower-order change.

No source action, potential or operator was built. No source count, ledger
verdict, class-C exclusion, source refutation or positive physical space is
derived. This is a T2 conditional tensor-class result, not a T1 source kill.

## Evidence and acceptance

Baseline `6ef984a3f04b40c98724d7442e6bd2f119a56a21`.

- `source-joint-symmetry-current-2026-11-13.md` Part I §§1–4: reused branching,
  scalar scope and reality burden.
- `source-small-vev-current-test-2026-11-24.md` §§3–7: primitive current and
  prior C-incompatible vector.
- `ambient-correlated-grading-control-2026-11-24.md` §§4,7: actual K95 laws.
- `source-prescription-current-2026-11-13.md`: independent source variations.
- `tests/program-focus/source_reality_mixing_class_probe.py`: 30 exact native K95 controls passed.

The Schur proof supplies completeness. Fixture checks independently test
signs, C laws, coefficient supports, covariance and actual contraction; they
do not replace the class proof. Two independent mathematical/source reviews accepted this conditional class result. No physical or analytic realization is certified.
