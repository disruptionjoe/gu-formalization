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
