---
artifact_type: exact_construction_and_scope_result
created: 2026-08-10
status: OBSERVED1131_CONDITIONAL__SOURCE_NATIVE_Y14_FIRST_JETS_FORCE_FULL1571__TANGENT915_NOT_FIRST_JET_CLOSED
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
ledger_rows: [LT-GR1, LT-GR2b, LT-GR2c, LT-GR3, LT-GR5, LT-GR6]
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected-K77 complete Euler-jet tangent closure

## Result in plain English

The natural rank-`915` tangent from v0.127 is **not closed under the source
action's first derivative**. It was a correct principal-symbol tangent, but it
did not yet own every derivative jet that the first-order Euler equation can
see.

If derivatives are restricted to the four observed spacetime directions, the
smallest closed selected low-grade tangent has rank

```text
321 + 810 = 1,131.
```

If the source action is read natively on all fourteen directions of `Y^14`,
the ten conormal directions fill the remaining block and force

```text
321 + 1,250 = 1,571,
```

the complete selected low-grade tangent. Ordinary pullback does not itself
erase those conormal jets. The smaller `1,131` horn therefore remains a useful
**conditional observed theory**, but it needs an independently source-owned
conormal constraint or BV differential. The source-native `Y^14` result is the
full `1,571` low-grade tangent.

This is a construction result, not a no-go for GU. It tells the next wave what
object must be ported to the two `U(32,32)` halves and the full `U(64,64)`
parent.

## Layer 0: which Euler object owns the calculation

The source first action and its stated Euler object are

```text
I1^B = <T, *[Shiab(F_B + 1/2 d_B T + 1/3[T,T]) + kappa/2 T]>,
Upsilon = Shiab(F_A) + *T.
```

At fixed epsilon, the connection variation is the first-order operator

```text
D_varpi Upsilon[u] = Shiab(d_A u) + Hodge(u).
```

It is not the pointwise density Hessian and not the Gram Hessian of a
residual-square action. A first-order operator is not generally represented by
a symmetrized pointwise matrix; doing that here erases the live grade-one to
grade-two coupling.

| phrase | object tested here | kept distinct |
|---|---|---|
| Euler linearization | unsymmetrized first-order `D_varpi Upsilon` | pointwise density Hessian; residual-square Gram |
| exterior covector `q` | scalar Clifford coefficient `{oneform: 1}` | a `Phi1` Clifford-vector component |
| observed first jets | `q` in `H*`, four directions | all `q` in `H* + N*`, fourteen directions |
| selected parent | low-grade real-Spin carrier | grade five; two `U(32,32)` halves; full `U(64,64)` |
| observed rank `1,131` | value plus four tangential first jets | a global pullback theorem or BV quotient |

## Exact closure calculation

The v0.127 grade-two extension had the block profile

```text
(160, 180, 60, 184, 10), total 594.
```

Each observed derivative direction adds `54` missing normal symmetric
trace-free directions. The exact rank progression is

```text
594 -> 648 -> 702 -> 756 -> 810.
```

The resulting observed-jet image is

| block | ambient | projection | intersection |
|---|---:|---:|---:|
| `H* tensor (H wedge N)` | 160 | 160 | 160 |
| `H* tensor Lambda2(N)` | 180 | 180 | 180 |
| `N* tensor Lambda2(H)` | 60 | 60 | 60 |
| `N* tensor (H wedge N)` | 400 | 400 | 400 |
| `N* tensor Lambda2(N)` | 450 | 10 | 10 |

Thus the four spacetime jets fill exactly
`H tensor Sym^2_0(N)`, of rank `4*54=216`. The rank-`810` image is invariant
under all `51` generators of `so(1,3)+so(6,4)`.

The ten conormal directions then give the exact cumulative progression

```text
810 -> 899 -> 978 -> 1047 -> 1106 -> 1155 -> 1194 -> 1223
    -> 1242 -> 1250 -> 1250.
```

They fill the remaining `440` directions in
`N* tensor Lambda2(N)`. Hence all fourteen source-native first jets close only
on the complete rank-`1,250` off-slice space.

## Lower-order composition

The zero-order Hodge term has the exact Krein lift identity on all `1,250`
off-slice directions. The background-connection part of `d_A` preserves the
rank-`810` observed image. The already-closed metric and epsilon lower-order
blocks add no further directions: v0.123's epsilon correction is zero on this
slice, and v0.125 already completed the metric block.

The result is therefore not a principal-only accident. It is the complete
selected low-grade value-plus-first-jet result under the two explicitly typed
jet domains.

## Why ordinary observation does not choose `1,131`

The earlier observation-germ result gives a rank-`10` conormal kernel and a
nonzero conormal witness. It shows that pullback forgets normal derivatives; it
does not prove that the upstairs Euler operator is independent of them. A
restriction that sets or identifies those jets is additional structure and
must be derived as a constraint, gauge/BV differential, or domain condition.

No new external datum is introduced. The fourteen jet directions are
derivatives of the existing connection field, not fourteen supplied
parameters.

## Source return

```text
SOURCE-CONFIRMS:
  the first Y14 action, its d_B T term, and a first-order Upsilon equation.

REPO-DERIVES:
  observed-X4 closure at 1,131 and source-native-Y14 low-grade closure at
  1,571, including their exact stabilizer blocks.

SOURCE-SILENT:
  any conormal-jet restriction selecting 1,131, a BV differential that
  removes the conormal block, and the port to grade five or unitary parents.
```

## Efficient inline specialist assessment

1. **Layer-0 semantics — ACTUAL MATH, very high confidence.** The Euler
   Frechet operator, a density Hessian and a residual-square Hessian are three
   different objects; only the first answers this gate.
2. **Prior art — ACTUAL MATH, very high.** v0.123/v0.125 supply completed
   epsilon/metric lower order; v0.126/v0.127 supply the tangent and its natural
   decomposition. This wave composes them without rebuilding them.
3. **Variational bicomplex — ACTUAL MATH, high.** The derivative symbol owns
   the cross-grade map; pointwise symmetrization is not a valid substitute.
4. **PDE/microlocal — ACTUAL MATH, high.** Tangential and conormal covectors
   must be tested separately. Closure depends on the admitted jet domain.
5. **Representation theory — ACTUAL MATH, very high.** Observed jets add the
   full `H tensor Sym^2_0(N)` block; conormal jets complete the last normal
   block. The dimensions and all stabilizer defects are exact.
6. **Symplectic/BV-BFV — ACTUAL MATH, very high.** Forgetting conormal jets
   under pullback is not a coisotropic constraint or BV quotient. No reduction
   is promoted without its differential and presymplectic check.
7. **Krein/operator theory — ACTUAL MATH, high.** The Hodge term lifts exactly,
   but no positive majorant, closed domain, Green inverse or spectrum follows.
8. **Source fidelity — ACTUAL MATH, high.** The source owns a first-order Y14
   equation; it does not state the conormal restriction needed by the observed
   `1,131` horn.
9. **Exact algebra — ACTUAL MATH, very high.** Independent Python rational and
   Sage/FLINT routes reproduce the rank progressions and firing controls.
10. **Hostile adversary — ACTUAL MATH, high.** The strongest surviving attack
    is parent scope: all ranks are selected low-grade real-Spin results, not a
    theorem on either unitary parent or grade five.

## Hostile disposition and fences

Verdict:

```text
CANDIDATE_SURVIVES__OBSERVED1131_CONDITIONAL__FULL_Y14_LOW_GRADE1571_FORCED
```

The rank-`915` tangent is retired only as a **complete first-jet tangent**. It
survives as the correct principal tangent. The rank-`1,131` object is a
conditional observed restriction, not a quotient. The rank-`1,571` object is
the complete selected low-grade source-native Y14 first-jet tangent, not the
full grade-five or unitary-parent theory.

## Progress and next gate

```text
Ledger v0.128 — 82/82 mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue 84; conditional action-parent range 84..86
Scoped quotients 5

headline_delta: none
conditions_closed: 2
  - the selected low-grade derivative-jet closure is decided wholesale
  - the observed and source-native jet domains are separately typed
conditions_opened: 0
remaining_named_conditions: 1
```

Next port the complete source-native low-grade rank-`1,571` Euler operator to
the two `U(32,32)` Weyl halves and the full `U(64,64)` parent, and include the
grade-five support before gauge/ghost/domain work. Keep the conditional
rank-`1,131` horn only if a source-owned conormal constraint or BV differential
is constructed.

Evidence:

- primary exact probe: `74/74 PASS`;
- independent Sage/FLINT: `11/11 PASS`;
- P1/P2/P3 unchanged and unused.
