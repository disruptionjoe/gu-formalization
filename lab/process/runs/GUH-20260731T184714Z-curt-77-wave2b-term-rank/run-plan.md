# Run Plan — Curt `(7,7)` source reinspection and Wave 2b term rank

- Run ID: `GUH-20260731T184714Z-curt-77-wave2b-term-rank`
- Date: 2026-07-31
- Branch: `agent/weinstein-guided-source-action`
- Lane: 1 — Observerse/GU truth status
- Campaign wave: `ECW2b-TERM-RANK-ABLATION`
- Status: complete

## Controlling question

What argument does Curt's iceberg transcript actually give for the `(7,7)`
chimeric carrier, and—after using that argument to order the surviving carrier
branches—what is the exact target-blind monomial quotient and ablation rank of
the already-selected G2 first-layer bosonic field graph?

This continues Wave 2. It does not restart at a missing source action and does
not enumerate the later odd or second-residual-square actions owned by Waves 4
and 5.

## Layer-0 precondition

Separate five claims:

1. the trace/traceless decomposition of `Sym2 T*X`;
2. the sign choice on the one-dimensional trace line;
3. the ordered signature of the vertical metric;
4. the metric actually induced on the dual-horizontal summand; and
5. the downstream representation-theoretic reason for selecting a split
   `Spin(7,7)` carrier.

The transcript's stated total is not allowed to repair missing block-sign
typing silently. Conversely, the earlier arithmetic objection is not allowed
to erase the explicit trace-line and representation choices the transcript
does supply.

## Source windows

- `00:39:55`--`00:42:43`: Frobenius, trace/traceless split, trace-line choice,
  `(4,6)`/`(3,7)`, declared total `(7,7)`, and spinor dimension/split.
- `00:44:21`--`00:47:20`: structure-group motivation, raw `(3,7)` statement,
  trace reversal to `(4,6)`, and `U(64,64)` presentation.
- `02:45:30`--`02:59:55`: graduate-student recap of chimeric/Zorro geometry,
  the same signature choice, and the inhomogeneous group handoff.

Source: Curt Jaimungal, *The Geometric Unity Iceberg... Oh Boy*, transcript
mirror linked in the source note. The source remains secondary and explicitly
describes its notes as correction-prone.

## Frozen Wave 2b class

Free/derived G2 fields remain:

```text
A in Conn(P), epsilon_red, g
B=A_LC(epsilon_red,g), T=A-B
S_r: Omega2(ad P) -> Omega13(ad* P)
flat_r: Omega1(ad P) -> Omega13(ad* P)
```

Enumerate local natural fourteen-forms that:

- are gauge and diffeomorphism covariant before observation;
- contain one outer homogeneous one-form `T`;
- contain exactly one `S_r` or `flat_r` pairing;
- contain at most one covariant derivative;
- have at most the cubic distortion order of the written G2 action; and
- contain no particle, gauge-subgroup, Higgs, count, P3, or cosmological
  target label.

This deliberately excludes `F^2`/residual-square terms (Wave 5), odd bilinears
(Wave 4), higher derivatives, pure invariant-polynomial topological terms,
and observation-dependent terms (Wave 3).

## Expected quotient

The expected basis is

```text
M1 = integral T wedge S_r(F_B)
M2 = integral T wedge S_r(D_B T)
M3 = integral T wedge S_r(q(T,T))
M4 = integral T wedge flat_r(T)
```

`F_A=F_B+D_BT+q(T,T)` and `D_A T=D_BT+2q(T,T)` must add no directions.
The expected quotient rank is four. The source slice has coefficients
`lambda*(1,1/2,1/3,kappa_1/2)`.

## Kill and planted controls

The run fails if it:

1. calls the trace choice forced rather than chosen;
2. claims the spoken `(4,6)+(1,3)` closes under one fixed ordered convention;
3. promotes the base-flip comparator to the transcript-preferred branch;
4. imports active Hodge/Krein/right-`H` operators to `(7,7)`;
5. counts `F_A` or `D_A T` as new monomials;
6. calls support-incidence rank a positive physical constraint surplus;
7. admits later odd, residual-square, target-labelled, or observation terms;
8. advances a generation/count claim; or
9. creates a third lane.

## Outputs

- source reasoning note with timestamped disposition;
- exact first-layer term quotient, coefficient ledger, and ablation matrix;
- deterministic exact probe with false-branch and false-surplus plants;
- campaign, crosswalk, roadmap, and index reconciliation.

## Exit

Wave 2b exits when the frozen G2 first-layer term rank and support-ablation rank
are exact, branch ownership is explicit, and the physical-surplus boundary is
named. Wave 3 may then begin the observation/equation-dual/domain construction;
Wave 4 and Wave 5 retain their own later action enumerations.

## Nonclaims

No global source convention, carrier, ported `(7,7)` action, physical equation,
Higgs, gauge group, stationary state, anomaly, count, cosmology, or third lane
is selected.

## Result

- Transcript reinspection makes `R77_VERTICAL_FLIP` source-preferred because
  Curt explicitly chooses the vertical trace-line sign and motivates the split
  `Spin(7,7)` carrier. The dual-horizontal sign/order map remains untyped.
- Six admissible `A/B`-written candidates modulo the curvature and derivative
  identities give a four-dimensional frozen first-layer quotient.
- The source coefficient slice has raw dimension two and projective dimension
  one. Four support ablations have rank four, giving support surplus zero.
- Physical surplus is deferred to observation and the later action layers.
- Wave 3 is released; neither a carrier nor a third lane is selected.

## Validation receipt

- Wave 2b: `33 exact + 9 planted = 42 PASS`.
- Wave 2 port ownership: `31 exact + 8 planted = 39 PASS`.
- Wave 1 carrier: `36 exact + 9 planted = 45 PASS`.
- Curt crosswalk: `45 exact + 16 planted = 61 PASS`.
- paired Curt--Eric graph: `50 exact + 20 planted = 70 PASS`.
- physics equation atlas: `52 exact + 14 planted = 66 PASS`.
- G2, G3, source reinspection, and source-directed closure regressions pass.
- changed JSON parses without duplicate keys; changed Python compiles;
  `git diff --check` passes.
