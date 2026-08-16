---
artifact_type: construction_result
created: 2026-08-06
status: RAW_FIXED_VARPI_LC_LC_REPRESENTATIVE_NONZERO__K122_NATIVE_COORDINATE_RETYPE__NOT_NATIVE_C_T_H_H
source_return: SOURCE-CONFIRMS
ledger_rows: [LT-GR1, LT-GR2b, LT-GR5, LT-GR6, LT-SM8]
scripts:
  - tests/channel-swings/selected_cubic_gauge_rotated_lc_ward_owner_probe.py
  - tests/channel-swings/selected_cubic_gauge_rotated_lc_ward_owner_independent.sage
registry: lab/process/selected-cubic-gauge-rotated-lc-ward-owner.json
---

# Selected-cubic gauge-rotated Levi-Civita / Ward owner

## K122 native-coordinate correction — 2026-08-15

The exact `14/3` evaluation below remains valid as an algebraic insertion of
two `DB_LC[H]` connection directions into the fixed-geometry `D3 I_T`
backend. Its old interpretation as the native metric response is superseded.
For the independently owned source/native map

```text
(t,h,v) -> (g=h,varpi=B_LC(h)+t Phi1+v),
T=varpi-B_LC(g),
```

the native metric column has `delta varpi=DB_LC[H]` and hence `delta T=0`;
the same cancellation holds at second order. The `14/3` number is therefore
a fixed-`varpi` partial-coordinate representative (or an independent pair of
connection insertions), not a native `C_t_h_h` coefficient. It must not be
added to the full native cubic. The genuine `h`-containing owners are the
same-`I1B` curvature/covariant-derivative and moving metric/frame/Hodge/Shiab/
pairing/density terms after exact source-coordinate composition. K122 gives
the corrected owner formula and K123 is tasked with their coefficientwise
evaluation.

All claims below that call this value a native or physical metric-induced
interaction are historical and superseded by this correction. The raw
carrier and gauge-rank computations remain exact controls for their typed
partial representative.

## Result first

The source-named Levi-Civita insertion creates a fixed, nonzero mixed
helicity-two value in the raw fixed-geometry augmented-torsion cubic. K122
shows that this is not the native metric column; independently, the raw value
is not a gauge-quotient class.

In symmetric frame, the exact first jet of the Levi-Civita spin connection is

\[
 L_k(h)_{\mu ab}=\frac12(k_bh_{\mu a}-k_ah_{\mu b}).
 \tag{1}
\]

For exact back-to-back massless and massive transverse-traceless shells,

\[
 D^3I_T[\Phi_1,L_p(h_0),L_q(h_m)]
 =\frac{14}{3}(p\!\cdot\!q)(h_0\!:\!h_m)
 =\frac73(\mu^2-M^2)(h_0\!:\!h_m).
 \tag{2}
\]

Equation (2) is nonzero for aligned plus or cross polarizations whenever the
two masses differ. It uses zero new fields, coefficients, selectors or
external data.

Three exact carrier checks then sharply delimit the result:

- the full radial LC–Gauss block is zero on the complete `24 x 100` carriers;
- the radial Hessian against all `1274` K77 `Cl2` connection directions is
  zero, eliminating the second-LC-jet term at this stationary `T`-only
  background; and
- the connection-gauge/gauge bilinear has rank five on its six-dimensional
  symbol block, so the nonzero representative does not descend by itself.

The disposition is therefore
`NONZERO_REPRESENTATIVE_WARD_REQUIRED`. The gauge-rotated Levi-Civita owner
and the co-moving epsilon/Ward/BV completion must be built as one package.
No Q1 pole, transition amplitude, fifth quotient, physical particle or
dark-energy identification is claimed.

## Plain English

The previous swing found that the connection distortion by itself could not
couple an ordinary graviton to the new massive partner. This swing checked
the piece that was deliberately left out: when the metric moves, its
Levi-Civita reference connection moves too.

That raw connection-direction response really is nonzero, with a fixed
coefficient. It remains a useful test of the gauge-rotated Levi-Civita
carrier, but K122 forbids reading it as the native metric coupling.

But a gauge choice can still change part of the answer. The calculation is
therefore a live ingredient, not yet an observable. The efficient next move
is not another isolated Levi-Civita coefficient; it is the exact Ward/
co-moving-epsilon completion that makes the whole answer gauge independent.

## 1. Layer 0

| phrase | object computed here | not identified with |
| --- | --- | --- |
| Levi-Civita response | dependent spin-connection first jet induced by a metric perturbation | independent distortion coordinate |
| gauge-rotated LC owner | source-directed connection-difference contribution inside `T` | full augmented torsion or all moving geometry |
| nonzero representative | bulk trilinear evaluated on chosen TT shell representatives | quotient class or S-matrix element |
| Ward obstruction | rank-five bilinear on connection-gauge symbol directions | proof that no completion exists |
| second-jet zero | vanishing stationary radial Hessian channel for this `T`-only package | global removal of nonlinear LC jets |

This prevents the exact mistake that would make v0.20 and this result appear
inconsistent. The old zero is the independent `q0` distortion entry. The new
nonzero is the metric-induced change of the dependent Levi-Civita reference
connection.

## 2. Source locus and disposition

Weinstein's source material explicitly places the **gauge-rotated
Levi-Civita connection** in the slot conventionally occupied by contorsion and
types augmented torsion as a difference of connections. That is the owner
tested here, so the scoped return is `SOURCE-CONFIRMS`.

The source does not publish equation (2), the rank-five quotient obstruction,
the required compensator, or a BFV/preboundary prescription. Those are
construction results and open burdens, not quotations.

## 3. Divergent preassessment

| lens | demand | disposition |
| --- | --- | --- |
| differential geometry | use the spin-connection LC jet, not a naked Christoffel symbol | enforced by (1) |
| variational PDE | include pullback-chain terms and test whether the second jet is actually needed | radial Hessian vanishes on all 1274 directions |
| representation theory | exhaust the complete LC and Gauss carriers | `24 x 100` block checked |
| exact computation | derive the shell coefficient by two routes | Python and independent Sage agree |
| symplectic/BV | test descent, not only value on one physical representative | gauge/gauge block rank five |
| source criticism | separate owner attribution from coefficient derivation | `SOURCE-CONFIRMS`, scoped |
| epistemic breadth | check whether the prior intrinsic zero typed the same object | it did not |

Preregistered branches included zero, nonzero-and-descending, nonzero-with-Ward
obstruction and second-jet-required. The observed branch is
`NONZERO_REPRESENTATIVE_WARD_REQUIRED`.

## 4. Exact shell calculation

The evaluator inserts (1) into the exact selected K77 augmented-torsion third
derivative. On back-to-back momenta satisfying

\[
 p^2=0,\qquad q^2=-M^2,\qquad (p+q)^2=-\mu^2,
\]

the scalar product is `p.q=(mu^2-M^2)/2`, producing (2). Plus-plus and
cross-cross polarizations agree; plus-cross vanishes. Exact rational tests at
mass pairs `(3,1)`, `(5,3)`, `(7,1)` and `(11,5)` reproduce the symbolic
formula.

These samples are correlated evaluations of one identity, not independent
phenomenological constraints. The information gain is the fixed symbolic
coefficient and its carrier selection, not a fabricated surplus count.

## 5. Carrier exhaustion and jet order

The LC first-jet carrier `H* tensor Lambda2 H` has dimension 24. The symmetric
Gauss carrier has dimension 100. Every entry of the radial LC–Gauss block is
zero. Separately, the radial Hessian paired with every one of the 1274
full-K77 bivector connection directions vanishes.

At a stationary background, the pullback third derivative contains the term
`D2I[D2LC, DLC]`. The complete radial-Hessian zero kills that term for the
current `T`-only radial package. This is a genuine workload reduction, but it
does not remove second jets from direct curvature, moving Hodge/Shiab/pairing,
nonstationary, or preboundary calculations.

The LC–LC radial bilinear is symmetric and has full rank 24, providing a
non-vacuity control: the evaluator does not annihilate the LC carrier.

## 6. Gauge and symplectic obstruction

One-sided bilinear checks between connection-gauge directions and the chosen
TT representative vanish. That is not quotient descent. Exact restriction to
the full six-dimensional Lorentz-gauge symbol block gives rank five for every
tested rational mass pair.

Thus gauge directions are not in the radical of the bulk bilinear. A physical
answer needs the co-moving epsilon terms, direct/moving action owners, and the
Ward/BV/preboundary complex to cancel or absorb this block. Until then there
is no well-defined reduced covariant Hamiltonian class and no fifth quotient
is entered in the ledger.

## 7. Seven-axis audit

| axis | result |
| --- | --- |
| Layer 0 | independent distortion, dependent LC response and reduced observable separated |
| L1 typing | LC jet is an `H* tensor Lambda2 H` spin-connection variation |
| L2 covariance | representative formula built; co-moving epsilon covariance open |
| L3 carrier | complete 24-dimensional LC and 100-dimensional Gauss carriers exhausted |
| L4 variation | exact selected-action D3 and stationary jet-order reduction constructed |
| L5 quotient | fails for the isolated owner: gauge/gauge rank five |
| L6 domain | finite exact shell only; common Green/operator domain open |
| L7 physics | no transition, pole, particle, unitarity or cosmological prediction claimed |

## 8. Constraint-surplus and datum accounting

```text
new fields: 0
new coefficients: 0
new selectors: 0
P1/P2/P3 consumed: 0
new real-form identifications: 0
```

The shell masses are diagnostic variables, not fitted parameters or claimed
predictions.

## 9. What moved and next gate

`LT-GR1`, `LT-GR2b`, `LT-GR5`, `LT-GR6` and `LT-SM8` receive distance-only
migrations. Verdicts, reason kinds, residue and quotient count do not move.
`LT-GR3` remains open.

Next construct the co-moving epsilon/Ward totalization of the rank-five gauge
block while assembling direct curvature/full-`II`/defect D3 and moving
Shiab/Hodge/DeWitt/Krein pairing/observation. Only the resulting reduced
preboundary class may advance to Q1.
