---
artifact_type: construction_result
created: 2026-08-08
status: SMALL_GAUGE_BASIC__BOUNDARY_CHARGE_LIVE
source_return: SOURCE-SILENT__PHYSICAL_BOUNDARY_GAUGE_CLASS__REPO-DERIVES__SMALL_GAUGE_BASIC_WITH_BOUNDARY_MOMENT_MAP
ledger_rows: [LT-GR1, LT-GR2b, LT-GR3, LT-GR5, LT-GR6]
scripts:
  - tests/channel-swings/selected_k77_contact_presymplectic_gauge_basicness_probe.py
  - tests/channel-swings/selected_k77_contact_presymplectic_gauge_basicness_independent.sage
registry: lab/process/selected-k77-contact-presymplectic-gauge-basicness.json
---

# Selected K77 contact-presymplectic gauge basicness

## Result first

The derivative-bearing part of the selected K77 construction now has an exact
local gauge/symplectic disposition.

The actual flat null-orbit spin-Levi-Civita symbol has rank ten. An exact
action-current witness produces nonzero contact coefficients in all ten
metric slots, and the complete first-jet observation/equation dual preserves
the rank-ten block. When augmented torsion is typed as the two-connection
difference

\[
T=A-B_{LC}(g),
\]

diagonal motion of `A` and `B_LC(g)` cancels exactly. Freezing the reference
connection instead produces a rank-ten Ward defect. This is why the pairing of
the two connections is structural rather than optional bookkeeping.

The resulting contact action has exact left and right off-shell Ward
identities. Its presymplectic form is Lie invariant and horizontal for
compact-support/Dirichlet gauge. It is **not** horizontal for unrestricted
boundary gauge: the contraction is the field-space derivative of a nonzero
boundary moment map. All ten K77 normal coefficient directions carry a
nonzero instance of that charge.

Therefore the fired ending is:

```text
SMALL_GAUGE_BASIC__BOUNDARY_CHARGE_LIVE
```

This is not a bulk inconsistency. It says the next object is the physical
boundary gauge class: either an action/source-selected boundary domain, or an
owned edge-mode extension. A transformation with live surface charge cannot
simply be quotiented as gauge.

## Layer 0

| shared phrase | exact object tested | not identified with |
| --- | --- | --- |
| contact transformation | derivative-bearing map `T=A-B_LC(g)` with total-derivative boundary owner | v0.68's point-frame field-coordinate change |
| gauge motion | simultaneous/diagonal motion of both connections in the source-owned difference | moving `A` while freezing `B_LC` |
| invariant current | zero Lie derivative under fixed gauge parameters | horizontal/basic current |
| small gauge | compact-support or boundary-vanishing parameter | boundary transformation with live surface charge |
| boundary charge | moment map whose field derivative is `-i_R Omega` | bulk Ward defect or already-reduced observable algebra |
| presymplectic form | local field-space two-form before characteristic/boundary quotient | BFV phase space, polarization or common analytic domain |

The load-bearing distinction is invariance versus horizontality. Basicness
requires both. The unrestricted current passes the first and fails the second
by an exact, interpretable charge.

## Source return

The primary-source packet confirms three ingredients:

1. augmented torsion is a difference of two connections;
2. the gauge-rotated Levi-Civita connection occupies the contorsion/reference
   slot; and
3. observation is richer than naive differential-form pullback.

The checked source does not select the physical boundary gauge class, an edge
extension, a polarization, or a common BFV/Krein domain. The decisive return
is therefore:

```text
SOURCE-SILENT__PHYSICAL_BOUNDARY_GAUGE_CLASS__
REPO-DERIVES__SMALL_GAUGE_BASIC_WITH_BOUNDARY_MOMENT_MAP
```

Source silence neither derives nor refutes the construction.

## Exact Levi-Civita and observation block

For null covector `k=(1,0,0,1)`, the linearized Levi-Civita symbol is

\[
(D_g\Gamma[h])^\rho{}_{\mu\nu}
=\frac12\eta^{\rho\sigma}
\left(k_\mu h_{\nu\sigma}+k_\nu h_{\mu\sigma}
-k_\sigma h_{\mu\nu}\right).
\]

On the ten symmetric metric directions its `64 x 10` matrix has rank ten.
The exact current used in the probe yields ten nonzero formal-adjoint metric
coefficients. Tensoring with the already-built complete observation receiver
preserves rank ten and lifts back exactly. The tangential-only receiver keeps
its conormal kernel and fails as a substitute.

Writing the contact map as

\[
C=(-L\; I), \qquad R_{diag}=\binom{I}{L},
\]

gives `C R_diag=0`. The planted frozen-reference generator instead has
`rank(C R_frozen)=10`.

## Exact contact Ward complex

The finite difference complex is a coefficient-independent certificate of
the derivative and boundary algebra. With

\[
D=\begin{pmatrix}-1&1&0&0\\0&-1&1&0\\0&0&-1&1\end{pmatrix},
\qquad T=a-Dg,
\]

and nondegenerate indefinite `K=diag(-1,2,3)`, the quadratic contact Hessian is

\[
H=\begin{pmatrix}D^T K D&-D^T K\\-KD&K\end{pmatrix},
\qquad R=\binom{I}{D}.
\]

Exact arithmetic gives

\[
HR=0=R^T H,
\]

`rank(H)=3`, and the four gauge columns of `R` exhaust its nullity. Moving
only `g` while freezing the connection fails the planted Ward control.

## Presymplectic contraction and boundary moment map

For `p=KT`, discrete integration by parts gives

\[
\delta I
=\langle p,\delta a-D\delta g\rangle
=\text{bulk Euler}
+p_0\delta g_0-p_2\delta g_3.
\]

The last two terms are the contact preboundary potential. Its field-space
exterior derivative obeys, for a fixed boundary gauge parameter,

\[
\iota_{R_\xi}\Omega=-\delta Q_\xi,
\qquad
Q_\xi=p_0\xi_0-p_2\xi_3.
\]

If `xi_0=xi_3=0`, the contraction vanishes: small gauge is a characteristic
direction. For unrestricted endpoint parameters the charge is nonzero. The
constant exact two-form remains Lie invariant in both cases, demonstrating
why invariance alone is insufficient.

The ten nonzero K77 cotangent normal weights from v0.68 multiply this identity
without changing it. Every normal direction has a live unrestricted charge
and vanishes on the small-gauge subspace.

## What changed

The contact-owner question and small-gauge basicness question close at local
principal grade. The physical boundary quotient becomes sharper:

- no new vertical B/T lift is needed;
- no bulk diagonal-gauge Ward defect survives;
- unrestricted boundary transformations cannot yet be quotiented;
- the source/action must select a boundary domain, or an edge-mode extension
  must be built and charged to the construction.

Five ledger distances move. Verdicts, residue, quotients and P1/P2/P3 do not.

```text
Ledger v0.69 — 82/82 active target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped
headline_delta: none
frontier_conditions_closed: 2
frontier_conditions_opened: 1
remaining_named_conditions: 2
```

## Seven-axis disposition

- **Layer 0:** point/contact, one-/two-connection, invariant/basic and
  small-/boundary-gauge objects are separated.
- **L1 syntactic:** Levi-Civita, observation, contact and boundary owners are
  explicit.
- **L2 type:** the two connection slots and ten metric slots remain distinct.
- **L3 algebraic:** Ward, contraction, moment-map and planted controls are
  exact over rationals; Sage independently replays them.
- **L4 geometric:** local flat Lorentz observation symbol plus K77 normal
  coefficient bank; full nonlinear ambient descent remains open.
- **L5 variational:** the contact Green/presymplectic owner and small-gauge
  kernel close; physical boundary reduction remains open.
- **L6 analytic:** no boundary domain, polarization or common operator domain
  is selected.
- **L7 physical:** no BFV charge algebra, positive state space, Einstein,
  Standard Model, cosmology or unitarity result is claimed.

## Constraint fence

```text
new fields: 0
new coefficients: 0
new selectors: 0
new quotients: 0
boundary condition selected: no
edge mode added: no
P1/P2/P3 consumed: 0
```

Curt remains formally separate inside the Eric lane. No third lane, claim
status, canon verdict or public posture is promoted.

## Next gate

Construct or source-select the physical boundary gauge domain, or construct an
edge-mode extension and its moment map. Then test the reduced presymplectic
class before choosing polarization or opening the common Krein/Green domain.
