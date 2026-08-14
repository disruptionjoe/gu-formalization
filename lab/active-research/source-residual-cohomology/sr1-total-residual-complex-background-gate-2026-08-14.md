---
title: "SR-1 total-residual complex and background gate"
status: active_research
doc_type: exact_conditional_composition_and_background_audit
created: "2026-08-14"
lane_id: SRC-RES-COH-01
swing_id: SR-1
source_claims: [SC-ACT-01, SC-ACT-04, SC-ACT-05, SC-ACT-06]
ledger_rows: [LT-SM8]
probe: tests/channel-swings/source_residual_cohomology_sr1_total_residual_complex_background_probe.py
claim_grade: "EXACT CONDITIONAL EQUIVARIANCE THEOREM AND EXACT FINITE CONTROL; FULL GU BACKGROUND MISSING"
disposition: BACKGROUND-MISSING
canon_verdict_change: none
---

# SR-1 total-residual complex and background gate

## Result first

`SR-1` returns

```text
BACKGROUND-MISSING
```

The latest canonical-Zorro nonzero-`T` candidate advances through exact
action/Bianchi field one-jet grade, but it does not yet change that
disposition. Primitive epsilon contains `D_B^!(E_B-E_T)` and therefore needs
at least a compatible field two-jet; total fixed-`varpi` metric stationarity
also needs the moving Shiab/Hodge/frame/volume/observation derivative bank.
Exact same-one-jet controls give different values for both downstream rows,
so missing higher-order data cannot be filled with zero and neither algebraic
branch is yet admitted or killed as a complete background.

The algebraic composition is not the obstruction. For any equivariant total
residual, differentiating equivariance gives

```text
L_Upsilon(Phi) K_Phi(eta) = rho_*(eta) Upsilon(Phi).
```

Consequently,

```text
Upsilon(Phi_*)=0  =>  L_Upsilon(Phi_*) K_Phi_*=0.
```

The repository already contains exact selected bosonic realizations of this
identity on internal and four-dimensional diffeomorphism orbits. It also owns
a local selected internal gauge map of rank `25` with `66` first
reducibilities.

What it does **not** contain is one complete action-owned field configuration
`Phi_*` on which the typed total boson--fermion residual is assembled and
vanishes, all action Euler equations are stationary, and the full gauge map
acts on the same carrier. Source claim `SC-ACT-06` asserts a rich solution
moduli and deformation complex; it does not exhibit or prove such a
background. The selected nontrivial K77 branch used by the current Hessian
work has nonzero Krein-null residual and is not stationary on the full
`196`-cell connection bank.

Therefore the conditional chain theorem is exact, but it cannot yet be
instantiated as the requested GU complex. `SR-2` is blocked at its premise.

## Exact conditional theorem

Let the action-owned field space be `F`, the total residual carrier be `E`,
and a gauge group `G` act on both. Write

```text
Upsilon : F -> E,
K_Phi : Lie(G) -> T_Phi F.
```

If the total residual is equivariant,

```text
Upsilon(g.Phi)=rho(g)Upsilon(Phi),
```

then differentiation at the identity gives

```text
D Upsilon|_Phi (K_Phi eta)=rho_*(eta)Upsilon(Phi).       (1)
```

Equation (1) is an off-shell covariance identity. Its right composition is a
differential only after selecting a residual-zero background. It cannot be
made zero by dropping field blocks, freezing moving coefficients or declaring
the right-hand side absent.

At `Upsilon(Phi_*)=0`, define

```text
L_Upsilon=D Upsilon|_{Phi_*}.
```

Then equation (1) gives the exact complex condition

```text
L_Upsilon K_Phi_*=0.                                    (2)
```

This proves the implication, not the existence of `Phi_*`, a global complex,
ellipticity, exactness, a quotient, or positive physical cohomology.

## Exact nonvacuous control

The executable control uses two integer `2 x 2` matrices as fields,

```text
U(A1,A2)=[A1,A2],
K_eta(Ai)=[eta,Ai].
```

The Jacobi/derivation identity gives

```text
D U(K_eta A1,K_eta A2)=[eta,U].
```

On a nonzero commuting diagonal pair, `U=0` while both gauge-field responses
are nonzero. Their two contributions cancel exactly, so `L_U K=0` is
nonvacuous. Freezing either field response leaves a nonzero defect. On a
noncommuting pair the same composition is nonzero and equals `[eta,U]`,
showing that covariance is not off-shell nilpotence.

This is a generic exact control for (1)--(2), not a GU background.

## Repository candidate audit

| candidate | exact/source status | failing requirement |
|---|---|---|
| source `Upsilon=0` moduli | author-stated in `SC-ACT-06`; Euclidean ellipticity/moduli untested | no explicit solution or complete action-owned field tuple |
| selected fixed-`H_q` radial critical branch | exact restricted critical branch | `Upsilon!=0` (Krein-null) and nonstationary on the full `196` bank |
| stationary two-layer factorization packet | exact generic theorem plus finite fixtures | assumes `Upsilon*=0`; does not construct the selected GU background |
| source-native physical Ward closure | exact selected K77 four-column bosonic composition | conditional on `Upsilon*=0`; not the total boson--fermion carrier |
| source gauge/BV--KT packet | exact local rank-25 image and 66 reducibilities | records gauge redundancy while both tested Euler covectors remain nonzero |
| full-carrier fermion residual packet | exact fixed-fixture finite operator results | does not supply a coupled bosonic stationary background or total residual complex |
| trivial flat-zero ansatz | possible generic gauge-theory control | not shown to be a legal global `Y=Met(X)` GU geometry with all owner equations |

The final row is deliberately not promoted. Setting formal coefficients to
zero is not a constructed Observerse solution unless the metric, soldering,
two connections, curvature, torsion, fermions, observation section, domain
and all action equations are simultaneously legal.

## Map inventory

```text
owned exactly at selected local grades:
  G_internal : R^91 -> T_selected, rank 25, ker dimension 66
  K_diff     : R^4  -> T_metric+connection+epsilon
  L_Upsilon_B K_diff = 0 conditionally at Upsilon_B*=0
  local BV/KT reducibility for G_internal

not yet one owned map:
  K_total : gauge parameters -> T_(gimel,epsilon,varpi,nu,zeta,...)
  L_total : T_total -> E_B direct-sum E_F
  L_total K_total on a constructed Phi_*
```

The rank-25 internal block and rank-four diffeomorphism block must not be
silently direct-summed: their overlap, semidirect bracket, fermion action,
metric/section entries, reducibility and boundary conditions are not yet one
action-owned complex.

## Disposition and next construction

`SR-1` closes two tempting but invalid shortcuts:

- treating the conditional identity (2) as proof that a GU background exists;
- using the nonzero-residual restricted critical branch as though it were the
  stationary residual-zero shell required by `SR-2`.

The lane remains active, but `SR-2` does not start. The next construction is
`SR-1B`:

```text
construct one complete source/action-owned Phi_*;
verify Upsilon_B(Phi_*)+Upsilon_F(Phi_*)=0 componentwise;
verify every independent action Euler row at Phi_*;
assemble K_total and L_total on that same carrier;
then replay L_total K_total=0 and determine reducibility.
```

The cheapest honest candidate is a nonzero-fermion saddle or a complete
moving-background jet already allowed by the released grammar. A trivial
zero ansatz may be used only after its legality as an Observerse geometry and
its complete owner equations are proved.

No quantum state space, superposition mechanism, physical cohomology,
ellipticity, positivity, decoherence law or empirical prediction follows.

## 2026-08-14 native-connection curvature-jet refinement

The later exact native-legality gate retires the underspecified pointwise
curvature-orbit discriminator.  If `B=B(epsilon)`, the labelled curvature and
all covariant curvature jets must be gauge transports of the distinguished
Zorro connection.  The frozen `b Phi1` ansatz already has a nonzero first jet,
and the two exact branches have distinct `b^4` curvature invariants.  One fixed
labelled orbit cannot realize both at one `Y` point, but either branch could
still match a different moving-`Y` jet.

The source-facing Zorro construction is presently a sketch without an explicit
induced-`Y` connection formula.  `SR-1B` therefore begins by constructing that
connection and comparing its labelled curvature one-jet branchwise.  This
sharpens `BACKGROUND-MISSING`; it does not close it or start `SR-2`.

## 2026-08-14 canonical Zorro/DeWitt curvature disposition

The repository already contained a canonical reconstruction of the sketched
connection: the B2C15P Levi-Civita-horizontal connection metric.  Its
pure-vertical DeWitt curvature is base-sign invariant, so it ports exactly from
the old `(9,5)` convention to the authorial K77 horn.  The normalized metric
trace is a flat fibre factor: all nine labelled trace--traceless curvature
planes vanish.  Both nonzero `b Phi1` branches have nonzero Clifford curvature
on those same nine planes.  Hence neither branch can be a gauge transform of
the distinguished connection in this canonical reconstruction.

This dissolves the labelled first-jet comparison only for those two candidates
and that reconstruction.  The source does not print or uniquely select the
connection-metric formula, so the abstract native-background question remains
`BACKGROUND-MISSING`; `SR-2` remains blocked.  The corrected `SR-1B` target is
now a residual-first solve with canonical `B_Z` held dependent and
`T=varpi-B_Z`, `varpi` allowed to move nonhomogeneously.  A rival Zorro
completion may substitute only after deriving nonzero mixed trace curvature or
changing the connection owner explicitly.

## 2026-08-14 residual-first point-jet refinement

Holding the canonical dependent `B_Z` fixed does **not** create a pointwise
algebraic obstruction. The independent source connection can be chosen at any
point so that

```text
varpi_y=(B_Z)_y,   T_y=0,   F_varpi(y)=0,
```

by using its free antisymmetric first jet to cancel the connection-value
commutator. Therefore `Upsilon_B(y)=0` for every linear Shiab, with no inverse
or surjectivity assumption and no external datum.

Curvature returns at the next order rather than disappearing:

```text
Alt(DT)_y=-F_BZ(y),
D Upsilon_B=Shiab(D_varpi F_varpi)+Hodge(DT).
```

Thus `BACKGROUND-MISSING` survives at neighborhood/stationary-background
grade, but its first honest obstruction is now the actual selected-K77
`j^2 varpi -> j^1 Upsilon_B` image with Bianchi and symmetric-second-jet
compatibility. A flat-`varpi` patch cannot extend the construction when `B_Z`
is curved: residual zero would force `T=0`, hence `varpi=B_Z` and the
contradictory equality `F_varpi=F_BZ`. This point-jet theorem neither starts
`SR-2` nor changes a ledger or canon verdict.

## 2026-08-14 differentiated-Shiab/Spencer refinement

The actual selected `comm/symi/symi` Hodge--Shiab map is an exact
`1274 x 1274` signed-permutation isomorphism,

```text
F_ij^k |-> -2 eta_i eta_j eta_k T_k^ij,
```

with `637` positive and `637` negative columns.  On the canonical
Levi-Civita Zorro/DeWitt curvature module, the unique inverse of the forced
target obeys differential Bianchi by Riemann pair exchange and first Bianchi.
The explicit Spencer right inverse

```text
B_(ri);j^k=(C_(r;ij)^k+C_(i;rj)^k)/3
```

is symmetric in the derivative indices and reconstructs all `214` supported
curvature-derivative cells from `323` supported second-jet cells with zero
residual, Bianchi or holonomicity defect.  The selected first-prolongation
target is therefore admitted; no free symmetric `DT` correction is needed.

`SR-1` nevertheless stays `BACKGROUND-MISSING`.  At `T=0`, coefficient-only
density/Hodge/Shiab/pairing variations vanish, the source observation remains
a dependent receiver, and the selected fixed boundary kills preboundary
flux.  What remains type-missing is the bulk action-owned `E_B-E_T` row and
the primitive-epsilon metric/observation formal-adjoint chain on this live
`DT` jet.  Residual zero does not imply that dependent-connection Euler row;
the exact control `L=t b'` has `E_t=b'=0` but `E_b=-t'` nonzero.  The narrowed
`SR-1B` must compute that row before any Spencer tower, stationary background, `SR-2`
or physical-cohomology claim can begin.

## 2026-08-14 true first-action Euler disposition

The selected noncyclic transgression action supplies an earlier obstruction
than the dependent metric/observation chain. Its translation Euler covector is

```text
E_T=S(barF)+L_T^!S^!T+*kappa T,
```

not the separately printed residual. On the pure antisymmetric representative
of the canonical point/two-jet, the direct term has 14 live grade-one cells;
the exact formal-adjoint `DT` companion occupies nine with ratio `1/7`, and
the total remains nonzero on all 14 cells.

The contrary affine family was exhausted. All `9,555` grade-two corrections
`Q_(r;k)^ij=Q_(k;r)^ij` were assembled. An exact 14-supported left-cokernel
covector annihilates every action column and evaluates to one on the forced
target. It uses zero differential-Bianchi rows, so relaxing or re-solving the
Spencer constraint cannot repair the action equation.

Therefore the canonical Zorro/DeWitt, selected `comm/symi/symi`,
`T=F_varpi=0` residual-first family is excluded at stationary first-action
two-jet grade. The prior printed-residual and second-jet theorems remain exact,
but no longer constitute a candidate stationary background. Primitive epsilon
and metric/observation rows are downstream on this family because the
independent bulk translation row already fails.

`SR-1` remains `BACKGROUND-MISSING`, rather than becoming a global no-go. The
next admissible candidate must be genuinely distinct: a nonzero-`T` branch, or
an explicitly derived different connection-grade/Zorro reconstruction with
new typed jet columns. `SR-2` remains blocked.

## 2026-08-14 nonzero-T/Zorro intersection refinement

The repository already owns the two exact nonzero-`T` homogeneous branches

```text
t_+ = (-2+sqrt(3))/208,  b_+ = 1/208-sqrt(3)/312,
t_- = (-2-sqrt(3))/208,  b_- = 1/208+sqrt(3)/312.
```

They solve the known local source-variable bulk Euler equations, including
all 1,470 low-grade `varpi` directions and 91 selected primitive-epsilon bulk
directions. Therefore “construct any nonzero-`T` candidate” is no longer the
correct next gate.

Both branches use the homogeneous connection `B=b Phi1`. Each is nonzero on
all nine labelled mixed trace-curvature planes, while the canonical
Zorro/DeWitt connection is zero on all nine. Neither branch intersects the
canonical dependent-connection locus. This is an empty intersection for the
currently owned homogeneous family, not a source-global background no-go.

The corrected `SR-1C` construction is a canonical-`B_Z` nonzero-`T`
source/action Euler solve, or a derived rival Zorro reconstruction with
nonzero mixed trace curvature. The one-dimensional action cokernel remains
exact, has fourteen-cell support, and is zero-`T` scoped. `SR-1` remains
`BACKGROUND-MISSING`; `SR-2` remains blocked.

## 2026-08-14 canonical-Zorro nonzero-T action/Bianchi refinement

The corrected `SR-1C` construction now exists at local formal-jet grade. Set

```text
C=Phi1 wedge Phi1,
T=t Phi1,
DT=-F_BZ+(-t/312-t^2)C+Q,
```

with `Q` symmetric in its derivative indices. The printed endpoint residual
vanishes because `S(C)=312 Hodge(Phi1)`. The true action Euler projects onto
the sole symmetric-`DT` cokernel as

```text
28392t^2+91t-351.
```

This polynomial has two real nonzero roots. At either root, one rational
thirteen-cell `Q` kills all 196 action rows and all 5,096 inherited Bianchi
rows exactly. Thus the canonical-Zorro nonzero-`T` action/Bianchi jet is
`NOT-YET-FALSIFIED`; the zero-`T` obstruction and the exclusion of both old
homogeneous branches remain exact.

This does not close `SR-1`. The action density
`-t(27+728t^2)` is nonzero on both roots, so a direct volume partial remains
live. Because only `E_T` has closed, that partial cannot be promoted to the
total fixed-`varpi` metric Euler. The next construction, now named `SR-1C`,
must derive `E_B`, construct the minimal compatible field two-jet required by
`D_B^!(E_B-E_T)`, and evaluate the moving-Shiab primitive-epsilon term plus
the complete fixed-`varpi` metric/Hodge/frame/volume graph on this exact
witness. Observation is a dependent receiver and is checked after the
underlying source rows, not added as an independent Euler row. Only after
those rows close does the complete formal-integrability tower begin. A formal
tower, local germ, total boson--fermion carrier and legal global background
remain separate burdens before `SR-2` can unblock. See
[`sr1c-source-coordinate-variational-prolongation-scaffold-2026-08-14.md`](sr1c-source-coordinate-variational-prolongation-scaffold-2026-08-14.md).
