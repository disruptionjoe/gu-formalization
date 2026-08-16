---
title: "Selected-K124 native I1B principal TT evaluator and Cartan gate"
status: active_research
doc_type: exact_full_k77_carrier_principal_tt_action_evaluator_and_green_gate
created: "2026-08-15"
registry: lab/process/selected-k124-native-i1b-principal-tt-evaluator-and-cartan-gate.json
probe: tests/channel-swings/selected_k124_native_i1b_principal_tt_evaluator_and_cartan_gate_probe.py
grade: "K124 CONSTRUCTS THE FIRST EXECUTABLE O_K123 SLICE ON THE FULL REAL K77 CLIFFORD/EXTERIOR CARRIER. IN THE NATIVE GRAPH DELTA_B=DB_LC[H], DELTA_T_H=0, DIRECT POLARIZATION ON A HOMOGENEOUS RADIAL LEG AND BACK-TO-BACK TT WAVES GIVES C_THH=-12 Q_SQUARED TIMES THE TT DEWITT PAIRING AND C_THV=0 ON ALL 120 CAUSAL-POLARIZATION-NORMAL TESTS. K126 IDENTIFIES THIS AS THE R=0, Q=-P SPECIALIZATION OF THE EXACT COMMON-TRANSVERSE THREE-MOMENTUM POLYNOMIAL AND SHOWS AN ISOLATED D(D2B_LC)=-24 CELL IS CANCELLED BY NATURAL TRANSPORT +24. K124 ALSO REPRODUCES D3_TTT=8736 AND C_TVV=-(56/3)<V,*V>."
target_claim: K123_NEXT_GATE__BUILD_O_K123_AND_COMPUTE_NATIVE_C_THH_C_THV
target_verdict: HOMOGENEOUS_RADIAL_BACK_TO_BACK_PRINCIPAL_TT_SLICE_COMPUTED__C_THH_MINUS_12_Q2_DEWITT__C_THV_ZERO__K126_EXTENDS_TO_COMMON_TRANSVERSE_THREE_MOMENTA__FULL_LOWER_ORDER_CARTAN_OPEN
canon_verdict_change: none
---

# Selected-K124 native I1B principal TT evaluator and Cartan gate

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> first-transgression, K77 Clifford/exterior, spin-Levi-Civita and Cartan/Green
> question. Ordinary Higgs/VEV, family-index, net-chirality, anomaly,
> symmetry-breaking and familiar four-dimensional gauge-model constructions
> do not adjudicate it. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

## Result in plain English

K124 finds that K123's requested evaluator was partly hidden in two already
exact but uncomposed surfaces: the full real `(7,7)` Clifford/exterior action
engine and the symmetric-frame spin-Levi-Civita symbol. Composing them on the
native graph, rather than the fixed-`varpi` graph, produces a definite answer
for the homogeneous-radial, back-to-back local principal TT packet.

For TT metric polarizations `H_1,H_2`, covector `q`, and an independent
normal-valued TT distortion `V`, direct scalar-action polarization gives

```text
C_t_h_h^prin(H1,H2;q) = -12 q^2 <H1,H2>_DW,
C_t_h_v^prin(H,V;q)   = 0.                            (1)
```

The raw unit-polarization values of the first equation are `-24`, `+24`, and
`0` on timelike, spacelike, and null representatives. Plus and cross are
diagonal with the same coefficient. The second equation vanishes in all
`3 causal x 2 metric polarizations x 2 distortion polarizations x 10 normal`
evaluations: `120/120` exact zeros.

The same evaluator independently reproduces

```text
D3_t_t_t = 8736,
C_t_v_v  = -(56/3)<V,*V>.                             (2)
```

Thus the K123 rank-two *evidence* deficit was real, but it was not a physical
two-parameter freedom. Once the existing action factors are composed, the
principal TT slice has one universal kinetic coefficient and one exact mixed
zero.

This is not yet the whole `O_K123`. K126 subsequently proves that equation
(1) is the homogeneous-radial/back-to-back specialization of the complete
common-transverse polynomial `-6(p^2+q^2+3r^2)<DW>`. Its isolated live
`d(D2B_LC)=-24` witness is cancelled by natural transport `+24` in the full
fixed-coordinate packet. The lower-order curved background, representative
selection and global Green/BFV domain also remain open.

## 1. Layer-0 packet

| object | exact meaning here | not identified with |
| --- | --- | --- |
| `I1B` | printed first transgression action | `I_sc`, `I2B`, or `I_II` |
| `H` | one of the two physical TT metric polarizations | an independent connection perturbation |
| `V` | normal-valued TT augmented-torsion direction | the metric-induced LC connection |
| native metric graph | `delta B=DB_LC[H]`, `delta T=0` | fixed-`varpi`, where `delta T=-DB_LC[H]` |
| `O_K123^prin` | full-K77-carrier, local principal TT evaluator | complete nonlinear/global `O_K123` |
| Green current | principal Cartan representative | reduced BFV charge |

The source-native graph is load-bearing. The old `14/3` value inserted an LC
direction into the `T`-only cubic. K124 instead moves the reference connection
inside `F_B` while keeping the native metric leg of `T` exactly zero.

## 2. Common evaluator construction

In the co-moving orthonormal K77 frame, metric, Hodge, Shiab, coefficient
pairing, density and frame transport form one natural packet. Their coordinate
motion is absorbed into the frame, while the genuine geometric metric
derivative remains in the spin-Levi-Civita connection. The principal bulk
normal form of the written action is therefore evaluated directly as

```text
F_B      -> B wedge B,
D_B T    -> B wedge T + T wedge B,
bar F    = B^2 + (1/2)(BT+TB) + (1/3)T^2,
I1B^prin = <T,S(bar F)> + (kappa_1/2)<T,*T>.           (3)
```

The exterior-derivative pieces vanish on K124's back-to-back metric packet
because its total metric momentum is zero. K126 shows that this is not a
general deletion: when the radial leg carries momentum, integration by parts
transfers a live `d(D2B_LC)` term to the radial derivative. It also shows that
the isolated exterior cell is not a complete fixed-chart action cell; omitted
coframe, pairing and tautological transport can cancel it exactly.

The evaluator uses the selected source-displayed `comm/symi/symi` Shiab in
exact Gaussian-rational `Cl(7,7)` arithmetic. It constructs the LC symbol

```text
delta B_(mu ab)
 = (1/2)(q_b H_(mu a)-q_a H_(mu b))                  (4)
```

and evaluates the scalar polynomial by eight-corner polarization. No prior
Hessian coefficient is read and no Ward equation is solved for a coefficient.

## 3. Exact `C_t_h_h`

Let

```text
N_DW(H1,H2)=tr(g^-1 H1 g^-1 H2)
```

on the trace-free TT slice. With the formal derivative-symbol convention
`q^2=g^(mu nu)q_mu q_nu`, the complete two-polarization matrices are

```text
timelike q^2=+1:  A=-24 I_2,
spacelike q^2=-1: A=+24 I_2,
null q^2=0:       A=0,                               (5)
```

because the unit plus and cross tensors both have `N_DW=2`. Equations (1) and
(5) agree exactly. This is a principal-order coefficient polynomial, not a
zero-order mass insertion. In particular its null value is zero because the
symbol is proportional to `q^2`, not because the action coupling is absent.

The result supplies the source-native analogue of K117's missing symbol-order
lesson without importing K117's observed `I_sc` coefficient.

## 4. Exact `C_t_h_v`

For each causal representative, the probe pairs each metric TT polarization
with both TT Gauss polarizations in every one of the ten vertical normals.
Direct polarization of the whole polynomial (3), including `F_B`, `D_B T`,
`T^2` and the mass term, returns

```text
C_t_h_v^prin = 0                                     (6)
```

in all 120 cases. Both same-polarization and crossed-polarization entries
vanish, in positive and negative normal directions. This is not a missing-
storage zero: the evaluator constructs every term first and then obtains zero.

Equation (6) is scoped to the selected two-polarization TT/Gauss packet. It is
not a claim that every unrestricted 1,274-dimensional off-shell mixed tensor
entry vanishes.

## 5. Fixed-metric controls

The same scalar evaluator returns `8736` on three radial directions. On every
selected TT distortion direction it returns

```text
C_t_v_v=-(56/3)N_V.                                  (7)
```

For the unit representatives used in the census, `N_V=-2`, so the raw value
is `112/3`. This independently recovers K122 rather than baking its answers
into the evaluator.

## 6. Principal Cartan/Green packet

With the radial coefficient held constant, the operator with symbol in (1)
is `L_h=-12 Box` in unit DeWitt normalization. One exact principal Green
representative on that slice is

```text
j^mu_A(H1,H2)
 = -12[<H1,nabla^mu H2>_DW-<nabla^mu H1,H2>_DW].     (8)
```

It satisfies

```text
div j_A=<H1,L_h H2>_DW-<L_h H1,H2>_DW.               (9)
```

The principal `h-v` current is zero with (6), and the algebraic `t-v-v` term
has no derivative Green current. Equations (8)--(9) are representatives prior
to boundary conditions. Adding an exact field-space or spacetime differential
can change the Cartan potential without changing the bulk or presymplectic
class. K124 therefore does not promote (8) to a physical charge.

## 7. What closed and what did not

| packet | K124 result |
| --- | --- |
| full 14D real carrier and selected Shiab | executable |
| native metric graph | executable |
| homogeneous-radial/back-to-back TT `C_t_h_h` | exact, `-12 q^2 N_DW` |
| local principal TT bulk `C_t_h_v` | exact zero on complete selected TT packet |
| fixed-metric controls | exact |
| principal Green current | exact representative |
| curved/lower-order action jet | open |
| explicit `D2B_LC` plus exterior-derivative recombination | K126: isolated `-24`, cancelled by natural transport `+24` on the adverse witness |
| full noncyclic Cartan potential and global domain | open |
| unique full two-field pencil and spectrum | not selected |

The strongest hostile concern is that a co-moving normal form might hide a
live coordinate owner. That would be a valid objection to a lower-order or
raw-Cartan claim. It does not change the principal bulk result: natural frame
transport is an invertible coordinate change, while the only differentiated
metric owner at top order is the LC symbol (4). K125 must nevertheless perform
the explicit fixed-chart recombination as an independent checksum.

## 8. Reverse scaffold

```text
R0 target: native radial response of the TT I1B Hessian
R1 complete: source/native graph and full K77 scalar polynomial
R2 complete: fixed-metric controls 8736 and -56/3
R3 complete at K123: rank-two evidence deficit and coordinate-split warning
R4 complete at K124: homogeneous-radial/back-to-back principal TT evaluator
R5 complete at K124: A=-12 q^2 N_DW and B=0 on that slice
R6 K125: generic fixed-chart curvature and coefficient covariance
R7 K126: isolated d(D2LC) is live but cancels in the complete transported witness
R8 K126: common-transverse polynomial -6(p2+q2+3r2)<DW>
R9 K127: local Ricci-flat stationary family and aligned one-scalar one-radial response, not the pure TT Hessian at `T=0`
R10 K127: generic Weyl leakage blocks automatic TT closure
R11 K128: source-global background and metric constraint/domain closure
R12 later: spectral/BFV and 2D-to-98D attachment
```

No ledger, datum, quotient, canon, public posture, particle interpretation,
phenomenology or GU truth-status claim changes. Joe input is not required.

## K125/K126 successor correction — 2026-08-15

K125 closes generic curvature/frame covariance. The explicit
fixed-chart symmetric-frame connection has the required nonzero mixed second
metric jet; restoring `dB` gives exact curvature covariance; and transporting
the pairing plus noncyclic Shiab-like map reproduces the co-moving scalar
without a cyclic-trace assumption. The principal Green current is likewise
frame-covariant. K126 then evaluates the isolated K77 `d(D2B_LC)` action cell
and an independent fixed-coordinate completion. The exterior cell is live at
nonzero radial momentum, but the selected `-24` witness is cancelled by
natural transport `+24`; K125's covariance theorem is vindicated. K124's
coefficient is the `r=0,q=-p` specialization of the exact common-transverse
polynomial `-6(p^2+q^2+3r^2)<DW>`.
K127 later constructs the local Ricci-flat curved family, reduces the aligned
compression to `24 K_perp I_2`, and exposes generic off-TT leakage. K128 owns
source-global background and metric constraint/domain closure before any
unique full pencil or spectrum is claimed.

Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k124_native_i1b_principal_tt_evaluator_and_cartan_gate_probe.py
```
