---
title: "Selected-K77 CBRS-1AA covariant odd-momentum operator obstruction"
status: active_research
doc_type: exact_equivariant_operator_and_variational_owner_admission_obstruction
created: "2026-08-22"
registry: lab/process/selected-k77-cbrs1aa-covariant-odd-momentum-operator-obstruction.json
probe: tests/channel-swings/selected_k77_cbrs1aa_covariant_odd_momentum_operator_obstruction_probe.py
grade: "EXACT RECONSTRUCTION-GRADE CLASSIFICATION OF THE SMALLEST SPIN-COVARIANT ZERO/FIRST-ORDER ODD-AUXILIARY ACTION CLASS; ITS RAW BF ENDPOINT MAP IS NONZERO, BUT ITS PURE FORM IS A MULTIPLIER/FIELD-REDEFINITION AND ITS GENUINE-FIELD FORM HAS AN UNSUPPLIED COUPLING; NOT A NO-GO FOR A SOURCE-NORMALIZED NON-EULER ODD OWNER"
target_claim: NONE-NOT-A-KILL
source_return: SOURCE_CONFIRMS_PRIMITIVE_EPSILON_B_T_AND_SELECTED_ACTION_GRAMMAR__REPOSITORY_DERIVES_THE_EQUIVARIANT_HOM_BF_VARIATION_AND_FIELD_REDEFINITION_OBSTRUCTION__SOURCE_SILENT_ON_THE_AUXILIARY_AND_ITS_COUPLING
canon_verdict_change: none
---

# Selected-K77 CBRS-1AA covariant odd-momentum operator obstruction

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`

```gu-typed-objects
result: CBRS-1AA exact operator-space and variational admission obstruction for the smallest covariant odd-auxiliary primitive-momentum class
carrier: real Spin(9,5) W_odd=Lambda1(V) direct-sum Lambda3(V), V=R(9,5), together with the existing primitive bivector epsilon in Lambda2(V) LAYER=toy CHIRALITY=N/A
pairing: selected real Clifford scalar-trace pairings on Lambda1, Lambda2 and Lambda3, with Hodge formal adjoints ON=pre_density_covariant_operator_class
real_structure: real Cl(9,5) exterior-grade modules; all auxiliary fields are Grassmann-even and W_odd is Clifford-odd
grading: d_B alpha and delta_B beta lie in Clifford-even Lambda2 while the B/T connection variation of their epsilon pairing is Clifford-odd in Lambda1 direct-sum Lambda3
action_owner: repository-construction
target: target-blind admission of a nonredundant odd B/T endpoint momentum owner with coefficient field equation and Hilbert map fixed before solving MAP-TYPE=evaluation
```

## Result first

The smallest covariant first-order class has a real endpoint map, but not an
independently owned action coefficient.

Write

```text
V=R^(9,5),
W_odd=Lambda^1 V direct-sum Lambda^3 V,
Xi=alpha+beta,
alpha in Lambda^1 V, beta in Lambda^3 V,
epsilon in Lambda^2 V.
```

The complete relevant first-order intertwiner space is

```text
Hom_Spin(V tensor W_odd, Lambda^2 V)
  = R[d_B:Lambda1->Lambda2]
    direct-sum R[delta_B:Lambda3->Lambda2].
```

Both basis maps are nonzero. They give the general smallest BF-like density

```text
L_BF(c1,c3)
  = c1 <epsilon,d_B alpha>_2
    +c3 <epsilon,delta_B beta>_2.
```

Modulo a boundary term the second summand is
`c3 <d_B epsilon,beta>_3`. Varying the connection in either summand gives a
nonzero Grassmann-even, Clifford-odd current in the same grade-one/grade-three
endpoint receiver as the CBRS-1U momentum. CBRS-1Z's quadratic-current parity
obstruction therefore does **not** extend to this mixed even/odd BF class.

The class still fails target-blind admission. Full Spin equivariance permits
independent `c1,c3`. The Hodge--de Rham/Clifford-Dirac projection selects the
relative ray `c1=c3`, but neither the released source nor the selected K77
action owns its overall `c`. With no independent quadratic normalization the
coefficient is absorbable by rescaling `Xi`, and `Xi` is a multiplier imposing
equations on `epsilon`. With the CBRS-1Z one-half quadratic auxiliary action,
the field scale is fixed and `c` becomes a new dimensionless coupling. Choosing
it after evaluating `M0` is the forbidden fit.

There is a second, equivalent view. Mixing `P_2 D_B Xi` into an existing
`Lambda2` B/T variable can produce the BF cross term inside the full field redefinition

```text
T' = T + c P_2 D_B Xi.
```

Expanding a matching quadratic `T` control yields the cross term together with
the required `c^2` auxiliary term. Substituting `T'` throughout the complete
action changes only field coordinates and also carries every induced
nonquadratic term; keeping only the cross term instead makes `Xi` a multiplier;
adding an independent kinetic normalization leaves `c` as a new parameter.
Thus the raw endpoint-variation map has dimension two, its canonical relative
ray has dimension one, and the nonredundant target-blind owner quotient has
dimension zero at current source ownership.

## Complete bounded local operator ledger

The census is polynomial degree at most two in `Xi`, zero or one total
covariant derivative for BF terms, and at most one derivative on each field
for the already-admitted quadratic first-jet controls. It uses no evaluated
`M0`, selected frame, boundary law or extra spurion.

| class | invariant dimension | disposition |
| --- | ---: | --- |
| `Hom_Spin(W_odd,R)` | 0 | no algebraic linear scalar |
| `Hom_Spin(W_odd,W_odd)` | 2 | independent grade projectors |
| `Hom_Spin(V tensor W_odd,R)` | 1 | `delta alpha`; total divergence |
| `Hom_Spin(V tensor W_odd,W_odd)` | 0 | no one-derivative odd-to-odd natural endomorphism |
| zero-order symmetric quadratic forms on `W_odd` | 2 | grade-one and grade-three masses/pairings |
| one-derivative quadratic scalars on `W_odd` | 0 | no odd-only BF term |
| symmetric quadratic first-jet forms on `V tensor W_odd` | 7 | three per grade plus one shared-Lambda2 cross term; quadratic-current class already bounded by CBRS-1Z |
| `Hom_Spin(V tensor W_odd,Lambda2)` | 2 | the nonzero `d alpha` and `delta beta` BF basis |

For `n=14`, the decompositions that fix the table are

```text
V tensor Lambda1 = Lambda0 + Lambda2 + Sym2_0,
14*14 = 1+91+104 = 196,

V tensor Lambda3 = Lambda2 + Lambda4 + Hook_(2,1,1),
14*364 = 91+1001+4004 = 5096.
```

The shared `Lambda2` occurs once in each summand. It supplies the two BF maps
and the single cross term among the seven symmetric quadratic first-jet
pairings. No component search is needed to discover another map.

## Field equations and endpoint variation

For the pure first-order density, formal adjunction gives

```text
E_alpha   = c1 delta_B epsilon,
E_beta    = c3 d_B epsilon,
E_epsilon = c1 d_B alpha+c3 delta_B beta.
```

Signs are fixed by the selected Hodge/form-adjoint convention; the displayed
choice is the convention used in the registry and probe. If the fixed
quadratic auxiliary operator is `K=K1 direct-sum K3`, the first two rows become

```text
K1 alpha+c1 delta_B epsilon=0,
K3 beta +c3 d_B epsilon=0.
```

Variation of `B/T` through `D_B` defines the odd current by

```text
<delta B,J_BF>
 = c1 <epsilon,P2((delta B) alpha)>
  +c3 <epsilon,P2((delta B) beta)>.
```

Exact exterior-basis witnesses make both summands nonzero. This current is a
valid contrary control to a blanket parity kill. It does not select `c1,c3`,
solve the complete Euler system or prove alignment with the evaluated `M0`.

## Hilbert variation

The BF action owns a Hilbert map; it is not stress-free. In the integrated-by-
parts representative

```text
L_BF=c1 <epsilon,d_B alpha>_2+c3 <d_B epsilon,beta>_3,
```

the cross-form stress tensors are

```text
H1_mu_nu
 = c1 [g_mu_nu <epsilon,d_B alpha>_2
       -2 epsilon_(mu|rho| (d_B alpha)_nu)^rho],

H3_mu_nu
 = c3 [g_mu_nu <d_B epsilon,beta>_3
       -(d_B epsilon)_(mu|rho sigma| beta_nu)^(rho sigma)].
```

They are symmetric, and their fourteen-dimensional traces are respectively
`10 c1 <epsilon,d_B alpha>` and `8 c3 <d_B epsilon,beta>`, as required by the
general cross-`p`-form identity `tr H=(n-2p)L`. Boundary representatives differ
only by the corresponding Hilbert improvement term.

For the genuinely normalized quadratic horn, eliminating `Xi` instead gives
an Euler-squared effective action. On each grade,

```text
L_p=(s_p/2) k_p Xi_p^2+s_p c_p Xi_p M_p
  -> Xi_p=-(c_p/k_p)M_p,
L_eff,p=-(s_p/2)(c_p^2/k_p)M_p^2,
```

where the Clifford-trace signs are `s_1=+1`, `s_3=-1`. In the general
Spin-equivariant class only the two field-rescaling invariants
`lambda_p=c_p^2/k_p` survive. Imposing both the selected Clifford-trace
quadratic ray and the canonical Hodge--de Rham ray identifies them with one
still-unsupplied overall `c^2`. Its Hilbert tensor is exactly

```text
H_eff=-2/sqrt(|g|) delta_g
      integral sqrt(|g|) [-(1/2)<M,lambda M>],
```

including metric dependence of the pairing and `M`. It vanishes on the old
endpoint equation `M=0`; it is an Euler-operator deformation, not an
independent pre-density owner.

## Exact classification and controls

| object | exact result | consequence |
| --- | --- | --- |
| raw first-order map | dimension two | parity does not kill the BF class |
| canonical Dirac ray | `d alpha+delta beta` | fixes relative map, not overall coupling |
| pure BF horn | multiplier / field-coordinate rewrite | not a new primitive owner |
| normalized-field horn | two invariant `c_p^2/k_p` coefficients | new unsupplied coupling data |
| endpoint current | nonzero, Clifford odd | correct raw target grade |
| Hilbert map | nonzero cross-form stress | must be retained in any later solve |
| nonredundant target-blind quotient | dimension zero | current class not admitted |

Positive controls remain. A source-owned term could fix the coupling and make
the mixed BF ray nonredundant. A genuinely new odd spurion or action variable
could supply a map that does not factor through an existing Euler owner. A
source-derived second sigma invariant remains a separate resurrection trigger.
None is present in this class.

## Hostile return and claim ceiling

- **Parity contrary route:** the even `epsilon` times odd `Xi` BF term really
  does generate an odd current. The result does not repeat the false blanket
  parity kill.
- **Representation contrary route:** the raw Hom space is two-dimensional,
  not zero and not one. The Dirac ray is an additional naturality choice.
- **Coefficient overclaim:** canonical `d+delta` fixes a relative ray only.
  Its overall coupling is not fixed by writing the operator canonically.
- **Multiplier overclaim:** absorbing `c` by rescaling an otherwise
  unnormalized `Xi` does not derive a coupling; it proves that `Xi` is acting
  as a multiplier.
- **Field-redefinition overclaim:** expanding `T+cP2DXi` may display exactly
  the desired cross term, but only the full substitution through every action
  term is the old action in new coordinates; an isolated cross term is new and
  remains unowned.
- **Stress shortcut:** integration by parts moves the derivative and changes
  the representative by an improvement; it does not erase the Hilbert map.
- **Source overclaim:** the source supplies primitive epsilon and action
  grammar, not this auxiliary, its BF term or its coefficient.

This is an exact reconstruction-grade admission obstruction to the smallest
zero/first-order mixed BF auxiliary class at current ownership. It is not a
universal no-go for source-normalized odd owners and changes no vacuum,
spectrum, ledger, canon, source ownership, residue, prediction or public
posture.

## Reverse-scaffold consequence

Continue with `CBRS-1AB`: audit the only surviving admission horn against the
selected K77 action itself. Require a source/action-owned normalization that
fixes the canonical Hodge--de Rham BF coefficient and proves the term is not a
`B/T` field redefinition or multiplier. If no such independent owner exists,
close the odd-auxiliary route until new source evidence and return only to a
source-derived second sigma invariant or another materially distinct action
class. Do not fit `c` to `M0`, add a boundary/sector, or advance to `CBRS-2`.

Reproduce with:

```bash
sage -python \
  tests/channel-swings/selected_k77_cbrs1aa_covariant_odd_momentum_operator_obstruction_probe.py
```

The exact probe passes after native propagation.
