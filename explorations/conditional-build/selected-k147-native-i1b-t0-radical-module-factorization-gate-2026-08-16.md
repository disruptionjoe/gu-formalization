---
title: "Selected-K147 native I1B T=0 radical-module factorization gate"
status: active_research
doc_type: exact_differential_module_typing_and_evaluator_materialization_gate
created: "2026-08-16"
registry: lab/process/selected-k147-native-i1b-t0-radical-module-factorization-gate.json
probe: tests/channel-swings/selected_k147_native_i1b_t0_radical_module_factorization_gate_probe.py
grade: "K147 CORRECTS AND DECIDES THE FULL DIFFERENTIAL-MODULE READING OF K146, WITH K148 INDEX-RAISING CORRECTION. FULL PRESERVATION IS EQUIVALENT TO ELL_N S_4=Q ELL_N ON 4455 RADICAL SECTION JETS. K147'S ORIGINAL SPACELIKE -384 WITNESS IS RETRACTED: IT CONTRACTED THE HESSIAN COVECTOR WITHOUT THE NATIVE DEWITT MUSICAL MAP. AFTER RAISING, THE SPACELIKE ROW IS -64 ELL_N AND HAS ZERO RADICAL LEAKAGE. THE BROAD FULL-MODULE FAILURE SURVIVES EXACTLY AT A TIMELIKE DERIVATIVE COVECTOR: THE DEWITT-RAISED ROW [0,0,0,0,-648704,0,0,-648704,0,-648768] LEAKS THE RADICAL VECTOR H_11=1 BY -648704. LOWER TERMS CANNOT REPAIR THIS TOP-ORDER FAILURE. THE FROZEN NULL SYMBOL RETAINS K135'S RANK-ONE OUTER-SQUARE LAW AND THE FROZEN K P^5 K A RESIDUAL IS ZERO. K147 THEREFORE KILLS ONLY THE OVER-STRONG ALL-DERIVATIVE-COVECTOR MODULE ROUTE AND RETURNS THE LIVE QUESTION TO A NULL-MICROLOCAL SYMBOL/TRANSPORT MODULE."
target_claim: K146_NEXT_GATE__SPARSE_COVARIANT_EVALUATOR_AND_ELL_N_S4_H_N_TEST
target_verdict: POINTWISE_FIBRE_TEST_INSUFFICIENT__UNRAISED_SPACELIKE_MINUS384_RETRACTED__EXACT_DEWITT_RAISED_TIMELIKE_ORDER8_LEAK_MINUS648704__FULL_DIFFERENTIAL_MODULE_ROUTE_KILLED__NULL_MICROLOCAL_ROUTE_REMAINS_OPEN
canon_verdict_change: none
---

# Selected-K147 native I1B T=0 radical-module factorization gate

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `SOURCE_NATIVE_ROUTE`.

Scope: K147 binds the repository-selected displayed `comm/symi/symi` local
`I1B` branch, the Ricci-flat `T=0` K127/K138 germs, fixed nonzero `kappa_1`,
and the formal polynomial metric operator `S_4=-A^*R_4A`. The product member
is one explicit source-permitted conditional branch, not a recovered preferred
historical Shiab. This result types and exactly kills the full differential-
module descent test at principal-symbol grade. It does not compute the still-
unserialized curved null-microlocal lower coefficient, establish a quotient
transport operator, or select an inverse, domain,
boundary theory, gauge completion, physical mode, or propagation law.

## Result in plain English

K146 found the right carrier but left one subtle mismatch. `H_n` is a
pointwise nine-dimensional metric hyperplane; `S_4` is a differential
operator. Applying `S_4` to nine constant vectors tests only constant sections.
Derivatives of arbitrary scalar coefficients are additional independent
inputs. Consequently a zero on those nine vectors—or on five representatives
after gauge—would not establish preservation of every `H_n`-valued section.

Let `ell_n:Sym2(T*) -> R` be the surjective radical constraint and
`H_n=ker ell_n`. The exact criterion is

```text
S_4(Gamma H_n) subset Gamma H_n
if and only if
there is a scalar differential operator Q with ell_n S_4 = Q ell_n.       (1)
```

Choose one local complement `e_0` with `ell_n(e_0)=1` and a frame
`e_1,...,e_9` of `H_n`. Equation (1) is equivalent to

```text
ell_n S_4(f e_a)=0 for a=1,...,9 and every scalar f.                       (2)
```

Once those nine operator columns vanish, `Qf=ell_n S_4(f e_0)`.

Because `ord(A)=ord(A^*)=2`, `ord(P)=1`, and `R_4` contains powers through
`P^4`,

```text
ord(S_4) <= 2 + 4 + 2 = 8.                                                (3)
```

There are `binomial(12,4)=495` scalar four-variable jets through order eight.
Thus (2) contains `9*495=4455` independent radical jet generators. The K147
probe constructs all of them exactly and checks the factorization theorem,
recovery of `Q`, and planted passing and failing operators.

The same order audit changes the background control. An inner metric two-jet
can be differentiated six more times by the four `P` factors and outer
`A^*`. On the central Brinkmann line, two transverse derivatives expose the
profiles, leaving a safe requirement through
`a^(6)(0)` and `b^(6)(0)`. Therefore the existing affine profiles
`a_0+a_1u`, `b_0+b_1u` can exhibit one nonzero obstruction, but zeros there
cannot certify a generic identity.

The full 4455-coefficient calculation is nevertheless unnecessary. A
differential factorization must hold first at its highest-order symbol for
every derivative covector `xi`. K135 serializes the exact frozen Hessian
coefficient as a map `Sym2 -> Sym2*`. K148 corrects the musical typing: a
metric endomorphism requires the native DeWitt map `G^-1`. For

```text
n=(1,0,0,1),
xi=(0,1,0,0),
ell_n=[1,0,0,-2,0,0,0,0,0,1],
sigma_8(S_4)(xi)=-A(xi)^T (K C_1(xi))^4 K A(xi),

ell_n^T sigma_8(S_4)(xi)
  =[-64,0,0,-256,0,0,0,0,0,-64].                              (4)
```

The displayed row is the original unraised Hessian-covector contraction. It is
not the typed endomorphism leakage. After raising,

```text
ell_n^T G^-1 sigma_8(S_4)(xi)=-64 ell_n^T,                       (5)
```

so the spacelike `-384` witness is retracted. The correctly raised timelike
control supplies the decisive counterexample:

```text
xi=(1,0,0,0),
ell_n^T G^-1 sigma_8(S_4)(xi)
  =[0,0,0,0,-648704,0,0,-648704,0,-648768],
h_11=1,  ell_n^T h=0,  leakage=-648704.                          (6)
```

Lower-order curved coefficients cannot cancel this order-eight failure.

```text
pointwise or five-representative test:  INSUFFICIENT_FOR_MODULE_DESCENT;
full descent criterion:                 ELL_N_S4_FACTORS_THROUGH_ELL_N;
maximum section-jet order:              8;
radical jet generators:                 4455;
safe Brinkmann profile-jet order:       6;
S_4 G:                                  ZERO_EXACT_BY_A_G_ZERO;
full S_4(Gamma H_n) preservation:       FAIL_EXACT_ORDER8_PRINCIPAL_LEAKAGE;
frozen null K P^5 K A residual:         ZERO_BY_L_N_POWER5;
frozen null Schur radical preservation: PASS_OUTER_SQUARE_LAW;
curved null-microlocal lower transport: NOT_YET_SERIALIZED;
null-microlocal quotient endomorphism:  UNDEFINED_LOWER_TRANSPORT_OPEN.
```

## 0. Layer-0 packet and route selection

| object | carrier or module | K147 role |
| --- | --- | --- |
| `P`, `R_4` | distortion differential operators | sparse Krylov middle |
| `A`, `A^*` | metric/distortion differential bridges | action-owned outer factors |
| `S_4=-A^*R_4A` | metric differential operator, order at most eight | candidate quotient operator |
| `H_n=ker ell_n` | metric rank-nine subbundle | section module to preserve |
| `J^8(H_n)` | 4455-dimensional point jet module | complete finite local certificate |
| `G_n` | rank-four metric gauge image | already annihilated structurally |

The route census rejected three shortcuts: a dense `229376^2` matrix, five
constant quotient representatives, and an affine-profile zero. The cheapest
correct first discriminator is the highest-order divisibility test. It fires
on the existing K135 packet, so curved 4455-jet evaluation is dominated for
the full-module question. A dual form,

```text
ell_n S_4 h = -<A ell_n^sharp, R_4 A h>,                                  (6)
```

may still reduce the later null-microlocal lower calculation, but only when
both copies of `A` and
the moving pairing/formal adjoint come from the same owned local action.

## 1. Why the selected branch is owned but the null-microlocal executable is absent

The selected local mathematical branch is not source-undefined. Earlier work
owns the covariant formal-Euler definition `C=kappa_1 K+E(D_B)`, the moving
connection transformation, transported noncyclic Shiab and pairing, the exact
Cl(7,7) algebra, the K138 Brinkmann neighborhood, and the full-module formal
operator `A` by variation. This licenses a conditional local implementation.
It does not recover the missing source-preferred choice among the eight
permitted Shiab products or create a global `Y^14` background/domain.

What is absent is one executable serialization carrying all of these together
for the lower null-microlocal transport question:

1. ordinary derivative plus one-form Levi-Civita and Clifford-adjoint
   connection on `Omega1(Cl(7,7))`;
2. moving Shiab, Hodge, pairing and density;
3. a mechanically derived variable-coefficient formal Euler adjoint;
4. Leibniz-complete sparse composition through `P^4` and `P^5`;
5. the complete curved bridge `A=D_g[S_g(F_B)]` and its compatible adjoint or
   dual-pairing replacement; and
6. independent `a_0,...,a_6,b_0,...,b_6` profile jets.

Frozen K132/K135 routines provide essential regression controls, not the
missing lower coefficients. Importing their matrix transpose as the curved
formal adjoint would reproduce exactly the error class exposed by K144.

## 2. Restricted residual and causal separation

K145's exact right remainder gives

```text
C R_4 A h = A h + kappa_1^-5 K P^5 K A h.                                (7)
```

Thus global `P^5 != 0` does not decide exactness on `im A`. K147 replays the
complete frozen null packet and obtains

```text
K P(n)^5 K A(n)=0.                                                        (8)
```

The prior power remains nonzero, so this is the exact terminal null
nilpotence, not an empty packet. It is a null principal-symbol result, not a
curved differential identity. The timelike family simultaneously supplies
the nonzero DeWitt-raised order-eight leakage (6). This causal contrast is why the result
returns to a null-microlocal module rather than strengthening the null quotient
into an all-derivative-covector differential submodule.

## 3. Controls and outcome rules

- **Frozen replay:** recover K132's selected coefficient and K135's rank-one
  null Schur law exactly.
- **Connection plants:** omitting either the one-form connection or the
  Clifford-adjoint connection must fire.
- **Adjoint plant:** a plain algebraic transpose must fail an independent
  formal Green/integration-by-parts identity when coefficients move.
- **Jet plant:** a sixth-profile-jet obstruction must disappear on the affine
  specialization and survive in the generic profile ring.
- **Gauge/radical plant:** a map that kills `G_n` but leaks one `H_n` section
  must fail (1).
- **Covariance:** replay at the rationally rotated null covector before a pass.

Equation (6) kills full differential-module descent of this `S_4` on the
conditional local branch. It does not kill the covariant five-class null
geometry or claim that the frozen null symbol leaks: an independent null
covector control has zero order-eight term, consistent with K135. Any future
lower null-microlocal result still cannot be called an inverse, exact Schur
complement, propagator, physical dynamics, positivity, state, or
superposition. Failure to derive the unified lower evaluator from the owned
formulas cannot be repaired by silently choosing omitted terms.

## 4. Reverse scaffold

```text
R0 K138: H_n/G_n is exact finite-frequency null geometry.
R1 K145: R_4 leaves exact P^5 remainders as differential operators.
R2 K146: S_4=-A^*R_4A is the first typed metric polynomial and S_4G=0.
R3 K147: pointwise H_n tests are insufficient for a differential operator.
R4 K147: full descent is ell_n S_4=Q ell_n on 4455 radical jets.
R5 K147/K148 correction: the unraised spacelike -384 witness is retracted;
   the DeWitt-raised timelike symbol violates factorization by -648704.
R6 K147: kill the full differential-module route; preserve the frozen null law.
R7 next route: define the exact null-characteristic symbol/transport module and
   compute only its curved lower coefficient with the unified sparse evaluator.
R8 only after R7 passes: descend the null-microlocal coefficient to the
   five-class quotient and determine its covariance and actual meaning.
```

No K147 result changes canon, a ledger, a source claim, a particle or
phenomenology verdict, a paper, or GU's public posture.

## K148 successor classification

K148 pairs each nonzero null covector with its own `H_n/G_n`, rather than
reusing fixed `n` against arbitrary derivative covectors. The frozen metric
polynomial descends covariantly and induces the zero principal map on the
rank-five null-cone quotient. K147's full-module failure remains exact through
the corrected DeWitt-raised timelike witness; the curved lower transport
remains unserialized and is now the K149 gate.

Reproduce the exact gate:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k147_native_i1b_t0_radical_module_factorization_gate_probe.py
```
