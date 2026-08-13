---
artifact_type: exact_conditional_construction_and_constraint_surplus_result
created: 2026-08-10
status: MINIMAL_EXTERNAL_N_R_COUPLING_CONDITIONALLY_SELECTS_AMPLITUDE_AND_PRESERVES_SMALL_GAUGE__CURRENT_MULTIROW_SURPLUS_NONPOSITIVE__DERIVED_PAIRING_OR_TYPED_INDEX_BRIDGE_REQUIRED
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
source_return: SOURCE_CONFIRMS_DISTINGUISHED_A0_AND_CHERN_SIMONS_LIKE_ACTION_GRAMMAR__SOURCE_SILENT_EXTERNAL_N_R_COUPLING_CHIRAL_REDUCTION_REALITY_P3_BRIDGE_AND_SURPLUS
ledger_rows: [LT-GR1, LT-GR2b, LT-GR2c, LT-GR2d, LT-GR3, LT-GR6]
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 external relative datum coupling and surplus

## Result in plain English

There is a real conditional path, but the present two-coordinate version does
not yet teach us enough.

On an observed three-boundary `Sigma`, pull the source connection back and
project it to one Lorentzian chiral factor,

```text
a_plus = pi_plus(s*B),       a0_plus = pi_plus(s*A0).
```

For the two real invariant pairings on `sl(2,C)_R`, use one projective chart

```text
B_r = B_Re + r B_Im.
```

Choose a boundary component `g_n` of winding `n in Z` and add the minimal
relative term to the already selected first action,

```text
I_cond[n,r] = I_G2 + k CS_Br(a_plus,a0_plus;g_n).
```

Here `k` is the normalized action level, not the sector label `n`. For fixed
`n` and `r`, a nonzero reduced characteristic coefficient `C(r)` gives

```text
C(r) t^4 = 9 n.
```

That equation can select a finite magnitude for the remaining stationary
amplitude `t`, leaving the even sign fork. It is therefore a legitimate
conditional fit: the route is not geometrically impossible, and the
topological term does not disturb the already-built local bulk Euler equations.

But `r` is still free. In an affine chart `C(r)=c_Re+r c_Im`, every chosen
nonzero `t` can be accommodated by

```text
r = (9 n/t^4 - c_Re)/c_Im.
```

The strict parameter-rank count is therefore one independent characteristic
equation against two supplied datum coordinates `(n,r)`, giving surplus `-1`.
Even under the most favorable row-level count—crediting both conditional
magnitude selection and small-gauge/BFV compatibility—the surplus is `0`, not
positive. The unowned choice of chiral horn would make it worse if charged.

So the minimal candidate **fits conditionally but does not yet confirm the
construction**. It becomes informative if the selected action/reality
conditions derive `r`, or if a genuinely typed relative-index map makes the
same `n` close P3 without relabelling it. Until one of those happens, do not
restrict and vary the bulk action on this sector.

## Layer 0

| phrase | object here | kept distinct from |
| --- | --- | --- |
| boundary component `n` | winding of `g_n` in `pi_3(SL(2,C))=Z` | Chern--Simons level `k`, P3 or generation count |
| level `k` | coefficient whose integral normalization makes the exponentiated action large-gauge compatible | which component `n` is occupied |
| pairing ratio `r` | point of the projectivized two-real-dimensional invariant-pairing cone | overall action scale or a derived reality condition |
| chiral projection | `pi_plus s*` on the observed Lorentzian connection | ambient `P_H`, normal P3 support or a full-parent trace |
| relative term | observed-boundary/preboundary functional | a new local fourteen-dimensional bulk Euler density |
| characteristic equation | global sector condition on the stationary family | a pointwise source Euler equation |
| P3 | realized right-`H`/relative-`KO` count interface | an integer with the same printed symbol |

The two most tempting mistakes are to call `n` the action level and to call it
P3. Both erase the very maps this gate is testing.

## Action and variation

For a closed observed boundary, invariant-pairing and Bianchi identities give

```text
delta CS_Br(a) = 2 integral_Sigma B_r(delta a wedge F_a),
delta_xi CS_Br = 2 integral_Sigma d B_r(xi,F_a) = 0
```

for small gauge transformations. This preserves the existing small-gauge
basicness result. Large transformations remain component-labelled and charged;
the normalized exponentiated phase is compatible with every integer `n`, so it
does not select `n=1` or any other component.

The added term is topological in the relative connection sector. Its interior
bulk Euler derivative vanishes after the characteristic sector is fixed, while
its preboundary potential and boundary conditions change. That is why the
symplectic/BV--BFV review is mandatory and why “no local Euler change” is not
“no physical effect.”

The construction is naturally attached to the source's first-transgression
parent. It does not prove that the residual-square parent generates the same
boundary term, and therefore does not settle `LT-GR3`.

## Exact constraint-surplus calculation

Use the exact nonzero reduced fixture

```text
c_Re=12, c_Im=6, n=2, r=1, C(r)=18.
```

Then `C(r)t^4=9n` has real roots `t=+1,-1`. Holding `n` fixed while allowing
`r` to vary fits every tested nonzero rational amplitude exactly. The relaxed
datum Jacobian is

```text
D_(n,r) [C(r)t^4-9n] = (-9, c_Im t^4),
```

which has rank one. Thus:

```text
strict rank surplus       = 1 constraint - 2 datum coordinates = -1
favorable row surplus     = 2 closed conditions - 2 coordinates = 0
unowned chiral horn cost  = at least one additional discrete choice
```

The favorable second condition is small-gauge/BFV compatibility. Large-gauge
integrality is not counted again: it is the same transgression datum, and an
integral level makes the phase compatible for every integer component rather
than selecting one. P3 contributes no condition because no same-object map
exists. The current full-parent quadratic pairing remains exactly zero; the
nonzero coefficient exists only after the explicitly charged chiral reduction.

## Efficient specialist pre-assessment

1. **Chern--Weil geometry — ACTUAL MATH, very high.** A fixed relative sector can discretize the stationary amplitude, but sector and level must remain separate.
2. **Principal-bundle geometry — ACTUAL MATH, high.** The observed chiral pullback is a construction; ambient `A0` does not perform it automatically.
3. **Complex Chern--Simons theory — ACTUAL MATH, high.** Integral level compatibility does not choose the occupied winding component, and the second real coupling remains continuous.
4. **Variational bicomplex — ACTUAL MATH, high.** The term is bulk-topological but preboundary-active; it cannot be booked as a new local Euler equation.
5. **Symplectic/BV--BFV — ACTUAL MATH, very high.** Small gauge remains basic while large boundary transformations remain charged; selecting a sector is a boundary condition, not a quotient.
6. **Constraint-rank geometry — ACTUAL MATH, very high.** The sole discriminating equation has rank one against two datum coordinates; automatic consequences cannot be counted repeatedly.
7. **Krein/operator theory — ACTUAL MATH, medium.** No pairing reality, positive majorant or common closed domain is derived by the integer sector.
8. **Cosmology — ACTUAL MATH, medium.** The magnitude becomes conditional on `(n,r)` but physical units, observed stress and radiative stability remain open.
9. **Index/KO theory — ACTUAL MATH, high.** Boundary winding is not the realized count/index datum P3 without an index/transgression bridge.
10. **Source criticism — ACTUAL MATH, high.** The source supplies compatible ingredients but is silent on this term, its datum and the surplus result.

## Constraint disposition

| target | result | counts toward current surplus? |
| --- | --- | ---: |
| conditional stationary magnitude | finite for fixed nonzero compatible `(n,r)` | yes, one |
| small-gauge/BFV basicness | preserved for the invariant relative term | favorable count: one |
| large-gauge sector selection | phase compatibility holds for every integer component | no |
| observed chirality | projection inserted but horn not derived | no |
| P3/count interface | no same-object map | no |
| local Einstein/VEV Euler | unchanged by the topological term | preservation only, not a new equation |
| observed Hilbert stress and common domain | unbuilt | no |

The honest surplus interval is therefore `[-1,0]`. It never reaches the
strictly positive threshold required to advance this two-coordinate candidate.

## Mailbox composition

The computational-spec proposal is **incorporated narrowly**: its insistence
on a compiled constraint battery and the first-action/residual-square purpose
fork sharpen this count. Its claimed 12-duty contract is not imported or
treated as GU truth without independent verification. The Krein poised-screen
proposal is **deferred** until a fermionic quadratic candidate is in scope; it
does not alter this topological boundary calculation.

## Progress and next gate

```text
Ledger v0.152 — 82/82 mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue 84; conditional parent range remains 84..86
Scoped quotients 5

headline_delta: none
frontier_conditions_closed: 2
frontier_conditions_opened: 1
remaining_named_conditions: 2
```

Closed: the minimal action coupling exists and its current surplus is not
positive. Opened: derive the pairing ratio/chiral horn or construct an actual
relative-index-to-P3 bridge. The next efficient work is to attack those two
independently, then rerun surplus before any restricted Euler, stress or common
domain campaign.

No residue, quotient, P1/P2/P3 assignment, canon verdict or public posture
moves. Exact probe: `52 exact + 7 planted = 59 PASS`.
