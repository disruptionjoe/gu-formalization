# Selected K77 observation-jet Euler/preboundary sufficiency gate

Status: `NULL GRAPH AND ONE CONORMAL PROLONGATION PASS; PAIRED ACTION DUAL/GREEN OWNER OPEN`

## Result in plain English

The v0.61 graph survives the first genuinely characteristic test.  Replacing
the frozen non-null covector by the retained labelled null covector does not
destroy the source response: the exact map still has rank 1,470 and nullity
zero, and all four conditional targets still have unique lifts.

But this does **not** yet produce the physical Euler equation or boundary
phase space.  The current construction controls the raw `Upsilon` response.
The source writes the first variation as the paired object
`(Upsilon,Xi)`, with `Xi=D Upsilon`; the equation-dual observation map,
invariant action pairing and Green current are still absent.  The exact
principal symbol has rank 650, so that missing boundary owner cannot be
discarded as inert bookkeeping.

## Exact construction

On the same predeclared `Omega1(Cl1+Cl2)` source tangent, use the labelled
null covector `q=e0+e1` and keep the reciprocal null leg already owned by the
full labelled reduction.  The full response

```text
R_q(a) = * Shiab(q wedge a + T_* wedge a + a wedge T_*) + a
```

has:

```text
domain                         1470
output support                 6530
output Clifford grades         1,2,5
rank                           1470
nullity                           0
```

The four fixed conditional targets have unique supports `103,84,73,73` and
retain family rank four.  Freezing the old non-null solutions fails all four
null equations.

An independent Sage/FLINT sparse matrix over `QQ`, formed by splitting the
Gaussian-rational coefficients into real and imaginary rows, reproduces null
response rank `1470`, nullity `0` and support `6530`.

Differentiating from `q=e0` in the `e1` direction gives

```text
R_q g' + (* Shiab(e1 wedge g)) = 0.
```

Every right-hand side is in the exact response image.  The unique derivatives
have supports `30,37,29,29`, and all four differentiated equations vanish
coefficientwise.  These first derivatives are not the finite null solutions;
higher moving geometry remains real work.

## The decisive boundary result

The source principal symbol

```text
P_q(a) = * Shiab(q wedge a)
```

has rank `650`, nullity `820`, and output support `3224` on the declared
1,470-dimensional tangent.  Exactly 1,365 basis columns are visible.  The
four graph columns have principal supports `16,25,25,25` and family rank four.
The 105 form columns parallel to `q` are an exact zero-symbol control, while
the first transverse column gives a one-coordinate nonzero witness.

Therefore a boundary/Green term is unavoidable on this graph.  What is not
yet known is the invariant density/Krein pairing that turns this symbol into
the actual action preboundary current, and how the paired `Xi` component and
moving observation receiver contribute.

## Layer 0

| phrase | established here | kept distinct |
| --- | --- | --- |
| raw `Upsilon` graph | exact source response inverse at non-null and labelled-null covectors | the paired first variation `(Upsilon,Xi)` |
| graph prolongation | one exact conormal derivative with fixed target/Hodge/Shiab/background | full moving metric, Hodge, section, epsilon and target derivative |
| boundary symbol | rank-650 principal source map | the invariant Green current |
| preboundary | previously retained unrestricted epsilon flux plus a now-proved live source symbol | a reduced presymplectic or BFV class |
| observation | dependent metric-section receiver | a new action field |
| null screen | full labelled ambient rank-12 screen | the separate 4D `10 -> 6 -> 2` physical quotient |

Source return:

```text
SOURCE-CONFIRMS:
  dI1 is the paired (Upsilon,Xi) first variation and Xi=D Upsilon.

SOURCE-SILENT:
  equation-dual observation map, invariant action/Krein pairing, and Green
  current on the unique graph.
```

## Specialist and hostile review

- **Differential geometry:** the null graph and one conormal prolongation are
  exact; the other moving geometric owners are not inferred.
- **Variational PDE:** raw `Upsilon` is not silently promoted to the complete
  Euler covector.
- **Symplectic geometry:** the rank-650 symbol proves boundary sensitivity,
  but a symbol without the action pairing is not a symplectic current and an
  unreduced current is not a physical transition.
- **Hyperbolic PDE:** this is characteristic-symbol algebra, not a common
  domain or well-posedness theorem.
- **Krein/operator theory:** no positive Euclidean norm is imported.
- **Representation theory:** grades, ranks and the retained null labels remain
  explicit.
- **Source criticism:** source ownership stops at the paired first-variation
  grammar; the equation dual and observation Green map are source-silent.
- **Exact computation:** the retained-representation solver and independent
  Sage/FLINT rank agree; wrong frozen graphs, truncated first prolongations,
  and zero/nonzero symbol controls prevent tautological promotion.

Both hostile charges fire.  The summary would outrun the artifact if it called
the rank-650 principal map a presymplectic current.  The lane would defend a
mistyped object if it demanded Euler descent from raw `Upsilon` alone after
the source itself writes `(Upsilon,Xi)`.

## Progress and next gate

```text
Ledger v0.62 — 82/82 active rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped

headline_delta: none
frontier_conditions_closed: 2
  - exact unique graph at the retained labelled null covector
  - exact first conormal graph derivative with fixed target
frontier_conditions_opened: 1
  - paired Upsilon/Xi action dual and moving-observation Green owner
remaining_named_conditions: 2
  - paired action/equation dual plus moving Hodge/section/target derivatives
  - reduced symplectic/common-domain/BV/BFV descent
```

No verdict, residue, quotient, external datum, canon or public posture moves.
P1/P2/P3 remain unused.  The next gate is:

`PAIRED_UPSILON_XI_ACTION_DUAL_AND_MOVING_HODGE_OBSERVATION_GREEN_IDENTITY`.

The executable probe is the authoritative numerical surface.
