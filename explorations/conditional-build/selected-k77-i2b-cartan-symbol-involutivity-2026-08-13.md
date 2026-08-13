---
artifact_type: construction_result
created: 2026-08-13
status: SOURCE_NATURAL_FIXED_GRADE_ENDPOINT_PRINCIPAL_SYMBOL_CARTAN_INVOLUTIVE__NONLINEAR_TORSION_AND_PHYSICAL_BV_OPEN
ledger_rows: [RA-E1, RA-E3, LT-SM6]
target_claim: NONE-NOT-A-KILL
source_return: SOURCE_CONFIRMS_SC_ACT_04_ENDPOINT_GRAMMAR__SOURCE_SILENT_CARTAN_CHARACTERS_AND_NONLINEAR_FORMAL_INTEGRABILITY
canon_verdict_change: none
fork_assumed: none
search_space_dim: "one exact order-two tableau with 196 fields/equations over four observed directions, its complete coordinate flag, first prolongation and one nontrivial rational coframe image"
free_object_delta: 0
scripts:
  - tests/channel-swings/selected_k77_i2b_cartan_symbol_involutivity_probe.py
---

# Source-natural K77 I2B Cartan-symbol involutivity

## Result first

The source-natural fixed-grade endpoint symbol passes Cartan's involutivity
test exactly. This closes the **principal-symbol** part of the endpoint
formal-integrability gate; it does not yet close the nonlinear moving system.

For the exact order-two tableau `g_2` on four observed directions, with 196
field and 196 equation coordinates, a regular coordinate flag gives

```text
restricted symbol ranks:       196, 196, 196, 182, 0
flag-kernel dimensions:       1764, 980, 392, 14, 0
Cartan characters:             784, 588, 378, 14
```

The first prolongation has rank `770` in its `784`-dimensional equation-jet
receiver, hence

```text
dim g_3 = 20*196 - 770 = 3150.
```

Cartan's bound from the characters is also

```text
1*784 + 2*588 + 3*378 + 4*14 = 3150.
```

Equality holds. The characters also predict

```text
dim g_4 = 4956,
```

which exactly reproduces the independently certified second-prolongation
value `35*196 - 1904 = 4956`.

## Why the flag is regular

The three higher-dimensional flag restrictions reach receiver rank `196`, so
they are maximal. On the remaining one-dimensional covector subspace the
corrected exact-form syzygy supplies at least fourteen kernel directions for
every covector, bounding rank by `182`; the chosen line attains `182`. Thus
the tested flag is regular rather than merely convenient.

This uses only the surviving algebraic content of the corrected principal
complex. It does not revive the retracted interpretation of that fourteen-map
as the source gauge map.

## Moving-frame test

A nontrivial rational determinant-one coframe transformation was applied to
the complete quadratic tableau. The transformed system retains

```text
flag ranks:                    196, 196, 196, 182, 0
Cartan characters:             784, 588, 378, 14
first-prolongation rank:       770
```

The old coordinate divergence representatives do **not** stay fixed: all
fourteen fail after the coframe moves. The compatibility *space* transports,
while its coordinate rows change. This is the intended naturality control and
prevents a frozen-row calculation from masquerading as moving geometry.

## What this closes

- the complete fixed-natural, local, source-endpoint principal tableau has a
  regular flag;
- Cartan equality holds at first prolongation;
- the next independently certified prolongation has the predicted dimension;
- a nontrivial exact coframe preserves the characters and equality.

Repeated searches for a new obstruction in higher **linear principal-symbol**
prolongations are therefore no longer the best route at this grade.

## What remains open

The theorem does not say that the complete GU Euler system is involutive.
Still open are:

1. the first nonlinear torsion/compatibility class on the nonempty stationary
   affine jet fibre;
2. derivatives of field-dependent or moving `Q_B`, `H_q`, Shiab, metric,
   section and observation data beyond tensorial coframe transport;
3. the full source-unitary action and the separate `E_act/Q_u` rival;
4. the source/action-owned physical tangent and BV/Koszul--Tate complex;
5. presymplectic/BFV reduction, analytic convergence, a Green domain,
   hyperbolic propagation, positivity, stability and global descent.

The Cartan characters count tableau freedom, not particles, physical modes or
new theory inputs. No residue, quotient, external datum or selector is added.

## Source return

`SC-ACT-04` supports the printed bosonic residual-square grammar and the
connection/covariant-derivative arena. It does not publish these Cartan
characters, their fixed-natural K77 realization, or nonlinear formal
integrability.

```text
SOURCE-CONFIRMS: SC-ACT-04 endpoint residual-square grammar.
REPO-DERIVES:    regular flag, characters, Cartan equality and coframe test.
SOURCE-SILENT:   nonlinear moving-coefficient torsion and physical BV closure.
```

No ledger row, physics verdict, canon claim, residue, quotient, P1/P2/P3 or
public posture changes.

## Specialist and hostile review

- **Spencer/EDS:** exact Cartan equality and the independent `g_4` check close
  principal-symbol involutivity at the declared grade.
- **Differential/principal-bundle geometry:** the coframe test preserves the
  tableau while correctly moving its compatibility representatives.
- **Variational bicomplex:** symbol involutivity leaves nonlinear torsion and
  the complete moving Euler identity open.
- **Symplectic geometry:** no stationary quotient, presymplectic current or
  BFV space follows.
- **Microlocal/hyperbolic and analytic:** no Cauchy theorem, convergent germ,
  domain, propagator or stability follows.
- **Krein/operator:** no positivity or physical-state selection follows.
- **Source criticism:** the calculation is repository-derived under the
  source-owned action grammar.

The three-charge hostile review returns `PASS_WITH_SCOPE_FENCES`.

## Next gate

Compute the first nonlinear moving-coefficient compatibility torsion on the
already-constructed nonempty stationary affine jet fibre. A nonzero class
would be the first genuine nonlinear obstruction; a vanishing or absorbable
class advances toward formal integrability. Keep construction of the physical
tangent/BV graph as a separate parallel gate.
