---
artifact_type: conditional_construction_and_composition_result
created: 2026-08-10
status: CONDITIONAL_TOPOLOGICAL_MAGNITUDE_SELECTOR_EXISTS__CURRENT_P3_DIAGONAL_UNBUILT__SIGN_REMAINS_DISCRETE
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
source_return: SOURCE_SILENT_CHARACTERISTIC_MATCH_AMPLITUDE_QUANTIZATION_AND_SIGN_MAP
ledger_rows: [LT-GR1, LT-GR2b, LT-GR2c, LT-GR2d, LT-GR6]
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 P3 characteristic-class amplitude selector

## Result in plain English

There is a mathematically clean way the external datum **could** select the
remaining VEV magnitude without supplying an arbitrary real number.

The source-Euler equations leave a curvature family

```text
F_B = f(t) Omega,       f(t)=t^2/3,
u(t)=-t/312-4t^2/3.
```

If this is a genuine global source connection on the framed four-cycle already
specified by P3, its normalized characteristic number is fixed by bundle
topology. For a quadratic invariant polynomial,

\[
  k_B=\frac1{8\pi^2}\int_{\Sigma_4}P(F_B\wedge F_B)
      = C_B\,\frac{t^4}{9}.
\]

When `k_B` and the nonzero pairing `C_B` are fixed, this equation removes the
one continuous amplitude and leaves at most the two signs of `t`. In that
conditional horn, topology chooses the magnitude and a separate orientation
bit could choose the sign. No continuous fit parameter is required.

But the present P3 datum does **not yet do this**. It is an auxiliary
`KO`/BPST twist of the operator. The repository has not built a diagonal map
that makes its characteristic class the characteristic class of the varied
source connection `B`. Nor has it proved that the native moving curvature
shape has `C_B != 0`, or that P1's loop orientation is the sign of `t`.

So this wave establishes a viable conditional construction route and its
precise missing maps. It does not claim that GU presently predicts the VEV,
the cosmological constant, or dark energy.

## Layer 0

| phrase | object here | kept distinct from |
| --- | --- | --- |
| P3 curvature | fixed BPST/anti-BPST connection on the auxiliary `H_n` twist | curvature of the varied source connection `B` |
| characteristic datum | integral class on the framed four-cycle | a fitted real amplitude |
| local family coefficient | `f=t^2/3` in the invariant source jet | a globally realized Chern--Weil number |
| normalization `C_B` | pairing fixed by invariant polynomial, representation, cycle and curvature shape | a tunable real normalizer |
| magnitude | `|t|` fixed by an even characteristic equation | sign of `t` |
| P1 | flat orientation line on the DeWitt loop | an established sign map for this VEV |
| topological selection | finite allowed values on a global connection sector | physical units or observed dark-energy density |

The load-bearing statement is therefore conditional:

> If the P3 class is carried by the source connection on its existing framed
> cycle, and the native characteristic pairing is fixed and nonzero, then the
> remaining continuous VEV amplitude is discretized.

## Exact theorem

For any degree-`m` invariant polynomial and compact oriented `2m`-cycle,

\[
  F_t=(t^2/3)\Omega
  \quad\Longrightarrow\quad
  \langle P(F_t),[\Sigma_{2m}]\rangle
  = C_m\,t^{2m}/3^m.
\]

Thus a fixed nonzero integral characteristic value makes the nonzero real
solution set finite. On the four-cycle (`m=2`) it gives

\[
  t^4=9k_B/C_B.
\]

- `k_B/C_B>0`: two real values `+|t|` and `-|t|`;
- `k_B=0` with `C_B != 0`: only `t=0`;
- `k_B/C_B<0`: no real solution.

The exact source Jacobian has rank two. Adding the fixed characteristic
equation raises it to rank three at every nonzero root. If `C_B` is instead a
free real, then `C_B=9k_B/t^4`; the freedom has merely moved. The sign cannot
be extracted from an even characteristic class.

The same conclusion applies parent-by-parent with the correct invariant
polynomial: Pontryagin normalization for a Spin parent and Chern normalization
for unitary parents. It does not select among the moving-Spin field domain,
the two `U(32,32)` halves, and full `U(64,64)`.

## Relation to prior art

This is not a new use of topology in the repository. Two earlier results are
being composed:

- the P3 packet already supplies `n in {-1,0,+1}`, a framed normal four-cycle,
  and `p1(H_n)=-2n u`;
- the external-flux canon result already proves that an integral external
  topology can carry information unavailable to the interior.

The new delta is narrowly typed: the characteristic class is tested as a
possible **magnitude selector for the v0.142 curvature family**, and the test
shows both why it can work and why the current auxiliary P3 twist does not yet
own that selection.

## External datum and constraint surplus

The efficient construction candidate is:

1. use the existing framed four-cycle `Sigma_4`;
2. embed the P3 `SU(2)`/BPST sector into the chosen source-connection parent,
   or otherwise build an action-owned equality of characteristic classes;
3. compute the native fixed pairing `C_B` rather than fitting it;
4. impose the resulting integral sector on the global field domain;
5. only if separately established, use the P1 orientation line to choose the
   sign of `t`.

If steps 1--4 use no free continuous normalization, one topological equation
removes one continuous amplitude: positive continuous constraint surplus.
The remaining sign is a discrete fork. If step 3 introduces a free real, the
surplus falls back to zero and the route is only a relabeling of the problem.

P1/P2/P3 are not reassigned by this result. P3 reuse and the P1 sign map remain
candidate interfaces until the ownership maps exist.

## Kill conditions

- the source connection and auxiliary P3 twist admit no action-owned diagonal
  characteristic map;
- the relevant native pairing `C_B` vanishes on the framed cycle;
- the normalization or embedding carries a free continuous coefficient;
- the global source family cannot be realized on the chosen topological
  sector;
- the selected nonzero amplitude breaks another mapped physics row;
- P1 has no same-object map to the amplitude sign (this kills only sign
  completion, not magnitude discretization).

## Specialist and hostile return

- **Chern--Weil/topology:** the scaling and finite-root theorem are exact;
  integrality belongs to the global connection sector, not the local jet.
- **Representation theory:** invariant-polynomial normalization and embedding
  index must be computed separately for Spin, two-half and full-unitary
  parents.
- **Variational geometry:** the sector must constrain the varied field domain
  or action. Appending an equality after solving is not dynamics.
- **Symplectic/BV--BFV:** a topological sector is not a gauge quotient or
  polarization. The coupled domain still has to preserve it.
- **Krein/operator theory:** discreteness does not imply positivity,
  self-adjointness or a common Green domain.
- **Source criticism:** Weinstein supplies no characteristic matching or sign
  map. Both are repository constructions.
- **Constraint accounting:** a fixed integer is categorically cheaper than a
  free real only if the pairing normalization is actually owned.

Hostile verdict:

```text
SURVIVES_AS_CONDITIONAL_CONSTRUCTION
CURRENT_P3_DOES_NOT_YET_SELECT_T
NO_CANON_OR_DATUM_ASSIGNMENT
```

## Progress and next gate

```text
Ledger v0.144 — 82/82 mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue 84; conditional parent range 84..86
Scoped quotients 5

headline_delta: none
frontier_conditions_closed: 1
frontier_conditions_opened: 1
remaining_named_conditions: 3
```

Closed: an external selector need not be a supplied real; a fixed nonzero
characteristic class can discretize the amplitude. Opened: the source-
connection/P3 diagonal and native nonzero pairing are now one explicit gate.

Next compute the source connection's characteristic pairing on the existing
framed four-cycle for each retained parent. Kill the route if it is zero,
unowned, or continuously normalized. If it survives, test the P1 sign map and
then carry the selected sector into the common Green/Krein and BV--BFV domain.

Primary exact certificate: `40/40 PASS` before manifest integration.
