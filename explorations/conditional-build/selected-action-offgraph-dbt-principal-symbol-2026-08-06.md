---
artifact_type: selected_action_offgraph_dbt_principal_symbol
created: 2026-08-06
status: ADJACENT_GRADE_DBT_EULER_LIVE__CURRENT_34_VARIABLE_TRUNCATION_NOT_ACTION_INVARIANT
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
source_return: SOURCE-CONFIRMS_AND_SOURCE-SILENT
ledger_rows: [LT-GR1, LT-GR2b, LT-GR5, LT-GR6, LT-SM8]
scripts:
  - tests/channel-swings/selected_action_offgraph_dbt_principal_symbol_probe.py
registry: lab/process/selected-action-offgraph-dbt-principal-symbol.json
---

# Selected-action off-graph `d_B T` principal symbol

## Result first

The `d_B T/2` term is not an additional ordinary Hessian block on the current
34-variable metric-plus-horizontal-Lorentz carrier. It is a first-order
parity-changing Euler operator.

On the 24-dimensional horizontal Clifford-grade-two connection bank, the raw
quadratic density coefficient and its formal-adjoint Euler symbol both vanish
exactly for timelike, spacelike and null covectors. This is not because the
selected Shiab image vanishes: on the complete 1,274-dimensional `Cl2`
one-form carrier, 1,183 derivative images are live for each nonnull
representative and all 1,274 are live on the null representative. They are
orthogonal to the same-grade action pairing.

The adjacent-grade block is live. Coupling the complete 196-dimensional
Clifford-grade-one bank to the 24 observed horizontal `Cl2` directions gives
formal-adjoint cross ranks

```text
timelike  12
spacelike 12
null      11
```

The corresponding parity-completed off-diagonal Euler ranks are `24/24/22`.
The grade-thirteen-to-horizontal-`Cl2` block is zero. Therefore the current
34-variable truncation is not invariant under the written first-order action:
an independent horizontal Lorentz-connection perturbation generically emits a
grade-one Euler row. The next construction must include the grade-one
companion and its algebraic Hessian, or construct an observation/constraint
receiver that kills this exact cross-block. It cannot simply add a `d_B T`
rank to the existing 34-by-34 Hessian.

The constant-augmented-torsion graph result remains intact. On that graph
`delta T=0`, so the selected curvature term still gives the exact nonnull
gauge-four and null gauge-four-plus-two tensor split. This wave changes the
off-graph completion burden, not that graph theorem.

## Plain English

The last wave showed that curvature supplies the missing Einstein-like
equations when the independent connection follows the metric-built
Levi-Civita connection. We then asked what happens when the connection is
allowed to move independently.

The derivative-torsion term does not act within the connection sector that we
had been using. Instead it connects that sector to a neighboring kind of
field in the Clifford algebra. Think of it as an off-diagonal coupling: looking
only at either side makes it appear to vanish, while looking at both exposes a
rank-12 first-order bridge. On lightlike momenta its formal-adjoint rank drops
by one.

That is useful adverse information. It says the present conditional build is
one carrier too small for the full source action. The repair is not an
external datum or fitted term. It is to include the already source-allowed
grade-one sector and calculate its own action and observation equations.

## Layer 0

| phrase | exact object | not identified with |
| --- | --- | --- |
| `d_B T` density symbol | `A_k(u,v)=<u,S(k wedge v)>` | its bulk Euler equation |
| formal-adjoint Euler symbol | `(A_k-A_k^T)/2` after integration by parts | raw support or raw rank |
| current 34-variable carrier | metric 10 plus horizontal Lorentz `Cl2` one-forms 24 | full `Omega1(Y,ad P)` |
| same-grade zero | vanishing `Cl2-Cl2`, `Cl1-Cl1` and `Cl13-Cl13` action pairings | vanishing selected Shiab image |
| live off-graph block | `Cl1-Cl2` formal-adjoint cross term | a new field invented for the fit |
| null rank loss | cross rank `11` rather than `12` | a physical particle or quotient |
| constant-torsion graph | `delta T=0` under `(delta g,delta varpi)=(h,Lh)` | full independent-source dynamics |

The source uses a full adjoint-valued one-form. The earlier 34-variable packet
was a scoped observed horizontal Lorentz carrier. Calling it the full source
carrier would be a Layer-0 error.

## Source collision

The 2021 action explicitly contains

\[
 \left\langle T,
 \mathscr S\left(F_B+\frac12d_BT+\frac13[T,T]\right)
 +\frac{\kappa_1}{2}*T\right\rangle
\]

and varies `varpi+s alpha` at fixed `epsilon`. It places no horizontal or
Clifford-grade-two restriction on `alpha`. The source therefore confirms the
coefficient, full upstairs carrier and need to vary the derivative term.

It does not publish the repository-selected `comm/symi/symi` product row, its
formal-adjoint rank, the grade-one/grade-two split, the observation receiver
or a common domain.

```text
SOURCE-CONFIRMS: full adjoint-valued T, coefficient 1/2 and translation variation
SOURCE-SILENT:   selected parity ranks, receiver, domain, BV/BFV and physics
```

## Exact construction

Let `C2_H` be the 24-dimensional horizontal Lorentz bank and `C1` the
196-dimensional bank of one-form coefficients in Clifford grade one. For a
covector `k`, define

\[
 A_k(u,v)=\langle u,\mathscr S_{sel}(k\wedge v)\rangle .
\]

Because the action coefficient is one half and the derivative changes sign
under formal adjoint, the bulk Euler coefficient is

\[
 E_k=\frac12(A_k-A_k^T).                         \tag{1}
\]

Exact real `Cl(7,7)` exterior arithmetic gives:

| block | timelike | spacelike | null |
| --- | ---: | ---: | ---: |
| raw `C2_H-C2_H` | 0 | 0 | 0 |
| Euler `C2_H-C2_H` | 0 | 0 | 0 |
| raw full `Cl2-Cl2` | 0 | 0 | 0 |
| raw `C1-C2_H` | 12 | 12 | 12 |
| Euler `C1-C2_H` | 12 | 12 | 11 |
| Euler `C13-C2_H` | 0 | 0 | 0 |

The first exact nonzero Euler coefficient is the timelike pairing of the
grade-one direction `(form index 1, Clifford index 0)` with horizontal `Cl2`
column zero; its value is `-1`.

The selected Shiab flips Clifford parity. Hence same-grade zeros are a type
selection rule, not absence of the derivative map. This is confirmed by the
live-image counts before pairing.

## Mixed-order consequence

In `(g,T)` coordinates, curvature contributes a second-order metric block,
while (1) is first order and off-diagonal between `Cl1` and `Cl2`. Passing to
`(g,varpi)` uses `delta T=delta varpi-L(k)delta g`; it does not make these
orders homogeneous. A valid total symbol must use a filtered or
Douglis--Nirenberg complex with the grade-one algebraic Hessian included.

The exact Ward protection survives formally because the complete source
gauge tangent lies in the kernel of `delta T`. What is not yet proved is that
the enlarged field equations, observation map and domain close on a common
carrier.

## Mandatory symplectic reading

The raw density and formal-adjoint Euler coefficient differ on the null
orbit: raw cross rank 12 becomes Euler cross rank 11. This is precisely why
the equation must be derived before a boundary or physical interpretation.
The integration-by-parts concomitant is nonzero on the live adjacent-grade
block, but no boundary condition, presymplectic reduction or BFV phase space
has been selected. The null rank loss is an open characteristic/constraint
question, not a fifth quotient.

## Corrected queue

1. Compute the selected algebraic Hessian on the complete grade-one bank and
   its cross terms at `T*=-(1/312)Phi1`.
2. Assemble the filtered metric--`Cl2`--`Cl1` Euler symbol and determine the
   nonnull and null kernels modulo the exact diffeomorphism image.
3. Build the observation receiver for both `s* T` and `res_s^V T`; test
   whether it preserves or removes the rank-12 adjacent-grade block without
   fitting a projector.
4. Establish a common Green/Krein domain, then odd BV and unrestricted BFV.
5. Keep `I2B <-> ||II||^2` separate until its owner map is constructed.

## Ledger v0.35

```text
Ledger v0.35 — 82/82 active target rows mapped (100%)
33 SAME · 19 DIFFERS · 24 NEEDS · 6 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped
```

Five distances move. Verdicts, reason kinds, revival triggers, residue,
quotient count and P1/P2/P3 remain unchanged. The rank-12 block is an equation
coupling among source-allowed fields, not twelve new parameters.

## Seven-axis disposition

- **Layer 0:** density, Euler, boundary current, current 34-variable carrier
  and full adjoint carrier are separated.
- **L1 syntactic:** raw, formal-adjoint and adjacent-grade symbols are explicit.
- **L2 type:** selected Shiab flips Clifford parity; same-grade truncations are
  not closed action carriers.
- **L3 algebraic:** all ranks, live-image counts and the first witness are
  exact on three causal representatives.
- **L4 geometric:** local horizontal and full K77 Clifford banks are explicit;
  global bundle/observation descent remains open.
- **L5 variational/symplectic:** the bulk Euler symbol is derived after
  integration by parts; Green/BV/BFV reduction remains open.
- **L6 analytic:** no common closed domain or hyperbolic completion is claimed.
- **L7 physical:** no Einstein, cosmology, particle, unitarity or Q1 claim is
  promoted.

## Constraint fence

```text
new fields: 0 (grade one was already in the full source carrier)
new coefficients: 0
new selectors: 0
new quotients: 0
P1/P2/P3 consumed: 0
```

Curt remains formally separate inside the Eric lane. No third lane, canon
verdict, claim status or public posture is promoted.
