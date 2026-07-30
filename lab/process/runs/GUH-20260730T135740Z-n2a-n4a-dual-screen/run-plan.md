---
run_id: GUH-20260730T135740Z-n2a-n4a-dual-screen
status: completed
repository: gu-formalization
workflow: joe-directed-n2a-n4a-dual-screen
mode: execute
run_type: progress
lane_id: "1"
work_item: SOURCE-OWNED-CHIMERIC-BV-CAMPAIGN-N2A-N4A
starting_revision: 65c08d814f5d764b7b7be7814d220d843bb60d48
opened_at: 2026-07-30T13:58:06Z
completed_at: 2026-07-30T14:38:04Z
claim_status_change: none
canon_change: none
public_posture_change: none
external_action_authorization: github_commit_and_push_only
write_boundary:
  - lab/process/runs/GUH-20260730T135740Z-n2a-n4a-dual-screen/run-plan.md
  - explorations/actual-sym2-c14-odd-orbit-knockout-2026-07-30.md
  - tests/channel-swings/actual_sym2_c14_orbit_probe.py
  - explorations/full20-curvature-irrep-open-bv-factor-2026-07-30.md
  - tests/channel-swings/full20_curvature_irrep_open_bv_probe.py
  - explorations/n2a-n4a-intersection-handoff-2026-07-30.md
  - tests/channel-swings/n2a_n4a_intersection_probe.py
  - explorations/README.md
  - tests/README.md
---

# N2a/N4a dual algebraic screen of unified packet v0

## Authorization and decision question

Joe said “Go” after Swing N1 wrote and froze the unified source-action and
external-datum packet. This Lane-1 run executes the two preregistered
high-information screens that depend only on N1:

1. **N2a:** construct the charge-conjugation bilinear and screen both
   fermionic bilinear branches on the four frozen actual-
   `Sym2(T*X)` representatives.
2. **N4a:** decompose the physical-`R` Levi--Civita and independent
   IG-curvature maps and determine which corrections are expressible in the
   frozen open-BV grammar.

The need for a source action and external datum is the premise. Neither
workstream may return that premise as its result. Each must add a typed map,
matrix, orbit/stabilizer calculation, quotient/basis calculation, or eliminate
a named candidate stratum.

## Lane selection

- Owner/scope: GU Formalization, unified source-action/datum campaign.
- Lane: `1`, Observerse/GU truth status.
- Manifest digest:
  `a0348a5b7977d32fe927d765fe9cab8315dacc770079d79b14ecfa7f1178c8b7`.
- Manifest/control revision: `3` / Lane-1 control revision `2`.
- Selected work basis: N1's exact handoff names N2a and N4a as the first
  parallel discriminators. N2b and N4b remain blocked on N3 variation.
- Effective permissions: Joe-directed construction and testing inside the
  declared write boundary; GitHub commit/push only as external action.
- Emergency revocation/writer evidence: no writer lock; the sole unrelated
  untracked run is a completed-blocked 2026-07-29 receipt outside scope.

## Frozen parent packet

This run consumes, without modifying:

- construction hash
  `1efdffd34e3ad5358fed16c08cda9ecf681df676e817560bf36b436d79658ffb`;
- the bulk-plus-defect carrier `(Y14,s(X4))`;
- the separate `K`-sesquilinear and
  `C_(epsilon_C,tau_C)`-complex-bilinear branches;
- the four orbit representatives `0`, trace, spacelike traceless, and null;
- the ten insertion families, word length at most three, two-derivative,
  antifield-number-two open-BV grammar;
- the bounded P1/P2 and P3 data families;
- the parameter ledger and held-out wall.

No result may silently substitute another action, topology family, parameter
budget, orbit list, or held-out observable.

## Construction fork

Program-native objects are used for the load-bearing GU construction:

- `Y14 = Met_(3,1)(X4)` with actual symmetric-tensor fibre
  `Sym2(T*X)`, not the exterior `Lambda2 + Lambda3` ten;
- native `Cl(9,5)`, indefinite Krein pairing, `Sp(32,32;H)`, and the
  geometric gamma-traceless physical-`R` projector;
- keep-and-grade BV/ghost structure rather than a positive-Hilbert quotient;
- induced `|II|^2` gravity rather than a freely substituted Weyl-squared
  action.

Standard charge-conjugation algebra, Lorentz stabilizers, curvature
decomposition, and BV antibracket identities are tools applied to those native
objects. They do not replace them. Every no-go or kill must state whether it
holds for the native construction, a standard comparator, or both.

## Layer 0 precondition

The following same-named objects are separated before computation:

| term | construction used here | Layer-0 disposition |
| --- | --- | --- |
| bilinear | `Psi^dagger K M Psi` versus `psi^T C M chi` | **HOMONYM:** sesquilinear and complex-bilinear objects; no verdict transfers without a map |
| vertical insertion | coefficient restriction of `v in Sym2(T*X)` through the N1 reduction interface | **HOMONYM:** neither literal pullback nor an exterior-ten form |
| orbit | four frozen representative strata under named group actions | **HOMONYM:** not an exhaustive Lorentzian Segre/Jordan classification |
| scalar | an explicitly intertwined 4D coefficient/mode | **UNCERTAIN** until the reduction intertwiner is built; a generic vertical tensor is not called a scalar |
| mass | algebraic provenance-block Hessian/pairing matrix | **HOMONYM:** not a normalizable four-dimensional physical mass |
| curvature obstruction | physical-`R` Levi--Civita map plus a separately typed IG map | **HOMONYM:** not one undecomposed “curvature” object |
| BV closure | algebraic expressibility in the frozen possible open-BV grammar | **HOMONYM:** not the classical master equation or a global gauge theory |
| count/index | no object computed in N2a/N4a | **SAME-BOUNDARY:** no decomposition is read as a generation count |

Any load-bearing unmarked homonym kills the affected conclusion. An
`UNCERTAIN` row remains a named downstream task, never an escape.

## Pre-registered expected verdict

```text
N2A-DUAL-BILINEAR-SYMMETRY-TYPED
N2A-FOUR-STRATUM-SCREEN-COMPLETED
N4A-LC/IG-CURVATURE-MAPS-SEPARATED
N4A-FROZEN-GRAMMAR-EXPRESSIBILITY-RANKED
INTERSECTION-EMITS-N3-VARIATION-TARGET
NO-PHYSICAL-MASS-CME-INDEX-OR-COUNT-CLAIM
```

This is an expectation, not a required positive answer. Exact scoped
elimination or `UNRESOLVED-WITH-NAMED-MISSING-MAP` is an admissible result.

## Kill and go conditions

### N2a

Kill a tested bilinear/representative stratum if the constructed transpose and
Grassmann symmetry forces it to vanish, native transport fails, its stabilizer
is mistyped, or a branch-relative algebraic necessary condition fails.

Do not kill on physical mass, normalizability, a stationary vacuum, exhaustive
orbit selection, or a cancellable anomaly: those objects do not yet exist.

Go if at least one nonzero transported branch/stratum survives with its
exchange symmetry, reality type, slot support, algebraic provenance matrix,
and three distinct stabilizer actions stated.

### N4a

Kill a proposed correction word if its source/target types do not compose, it
lies outside the frozen derivative/degree/antifield bounds, it is zero in the
frozen identity quotient, or it conflates the Levi--Civita and IG maps.

Do not claim source-EOM factorization or CME closure before N3 supplies the
Euler ideal and equation-dual maps.

Go if the two curvature maps are explicitly separated and the frozen grammar
is reduced to a typed candidate image/quotient with a rank or a precise
`RANK-DEFERRED` witness naming the missing representation map.

### Intersection

The joint output must name the smallest N3 variation target whose Euler maps
can decide both the surviving N2a hull and the N4a source-EOM factorization.
It may not expand the parent packet to rescue an adverse result.

## Controls

- Reproduce the declared charge-conjugation transpose signs and plant one
  Grassmann-symmetric kernel that must vanish for identical odd fields.
- Compare zero, trace, spacelike-traceless, and null actual-`Sym2`
  representatives against a horizontal vector and the exterior-ten hostile
  comparator.
- Delete the forced normal grading and plant a relative slot phase; both must
  reproduce the known transport failures.
- Keep Lorentz-on-`Sym2`, fibre-frame, and full gauge stabilizers in separate
  columns.
- Reproduce the W177 physical-`R` Levi--Civita fixture only after the native
  `4+10` frame/sign permutation is aligned.
- Plant a nonparallel projector, an LC/IG map concatenation, an ill-typed
  insertion word, an over-depth word, and a Jacobi-sign failure.
- Verify that no tested result mutates the N1 construction hash or reads a
  held-out value.
- Plant a “three blocks therefore three generations” inference and require
  rejection at Layer 0.

## Planned execution

1. Reconstruct N2a and N4a independently against the frozen packet.
2. Implement executable exact/finite controls for each.
3. Hostile-review both outputs and cross-check their intersection.
4. Write the minimal N3 emission/variation target generated by the screens.
5. Run new probes, relevant inherited regressions, manifest/process gates,
   Python compilation, and diff checks.
6. Append the immutable receipt, commit and push only scoped files, and close
   through the scoped repository-session guard.

## Execution receipt

### N2a result

The actual-\(\operatorname{Sym}^2T^*X\) screen constructs both native
charge-conjugation components,

\[
(\varepsilon_C,\tau_C)=(-1,+1),\qquad(+1,-1),
\]

and the separate Krein branch. Both bare
\(C_{\varepsilon_C}\Gamma(\alpha_h)\) kernels are transpose-skew, while
\(K\Gamma(\alpha_h)\) is Hermitian. The zero representative is killed.
Trace, spacelike-traceless, and null representatives are nonzero; only trace
preserves all six generators of the fixed-background Lorentz algebra.

This is a conditional bare-kernel result. The total \(P_0\), \(\rho(\Phi)\),
provenance/reality, full-20 placement, and full-
\(\operatorname{Sp}(32,32;\mathbb H)\) equivariance/stabilizer maps remain
unresolved. No branch is promoted to a mass, stationary interaction, index,
or count.

### N4a result

Under \(\nabla\Gamma=\nabla P_R=0\), the compatible Levi--Civita physical-
\(R\) curvature map is exactly

\[
\mathcal C_{RR}^{LC}
=
\frac12P_R\!\left(\operatorname{Ric}^0_{bd}\gamma^d\right).
\]

The scalar and Weyl irreps are annihilated; traceless Ricci survives with
coefficient \(1/2\). W177 remains nonzero and full rank with corrected norm
\(15.66992510\); the earlier \(21.04321084\) value is superseded as a
raised/lowered-gamma convention mixture without rewriting its provenance.

The constructed \(P_{\rm IG}\) matrix is only a pointwise Spin-compatible
witness. The attempted full-\(\operatorname{Sp}\) interpretation was killed
because a generic \(\operatorname{Sp}(32,32;\mathbb H)\) element need not
preserve the gamma/vector slot or \(P_R\). The frozen open-BV grammar has
1110 word shapes and a 233100 slot-word syntactic ceiling, with 36 typed,
712 rejected, and 362 map-deferred word-shape statuses in the supplied
partial incidence graph. These are not Hom dimensions. Full-
\(\operatorname{Sp}\) IG covariance, exact equivariant Hom rank, EOM
factorization, and CME remain open.

### Joint N3 handoff

The only nonzero fully Lorentz-preserving tested N2a representative is
trace-type, while the N4a LC obstruction is traceless-Ricci-type. Exact trace
and traceless projections reject their direct algebraic identification.
This does not kill a differential/current-mediated coupling through the
section, fermion, second-fundamental-form, IG, or source equations.

The intersection freezes six discriminator outputs in dependency order:

1. the total sesquilinear
   \(P_0^\dagger K\mathfrak c_\rho(v[\Phi])Y_KP_0\) kernel;
2. the separate complex-bilinear
   \(P_0^TC_{\varepsilon,\tau}\mathfrak c_\rho(v[\Phi])Y_CP_0\) kernel;
3. the fermion and vertical-connection Euler maps;
4. the trace/trace-free section Euler map, including variation of \(s_!\);
5. the IG parent Euler maps together with
   \([\nabla_A,\Gamma]\), \([\nabla_A,P_R]\), and soldering equivariance;
6. the physical-\(R\) Noether defect split into LC-Ricci-zero, IG,
   compatibility, and source-equation pieces.

The P3-twisted principal/subprincipal symbol is a separate mandatory
index/causality campaign carry, not a seventh minimal N2b/N4b discriminator
and not an index pushforward. No new source coefficient or external-datum
freedom was introduced.

### Corrections fired

The controls and hostile review changed the work materially:

- the actual vertical covector is the trace-reversed DeWitt musical, not a
  Frobenius identification;
- a bare \(C\Gamma\) transpose sign was prevented from becoming a complete
  odd-field verdict before \(P_0\), gauge, and provenance placement;
- the full gauge stabilizer was expanded beyond
  \(\operatorname{Cent}(\Phi)\) to include the pairing, gamma/soldering,
  restriction, and provenance data;
- the original IG witness was downgraded from full-\(\operatorname{Sp}\) to
  pointwise Spin-compatible grade;
- the physical-field-degree plant was separated from the derivative-cap
  plant;
- the \(K\)-sesquilinear and \(C\)-complex total kernels were split after a
  Layer-0 collapse was caught;
- the missing gamma/projector/soldering compatibility equations were added
  to the N3 handoff; and
- the twisted index input was separated from the six local discriminators
  as a campaign carry.

### Validation

Passed:

- all 73 frozen N1 packet checks;
- the new N2a, N4a, and N2a/N4a intersection probes;
- `full20_native_polarization_probe.py`;
- `full20_dewitt_loop_transport_probe.py`;
- `vertical_krein_weld_probe.py`;
- `source_action_requirements_consistency.py`;
- `W229_source_action_znu_completion.py`;
- `vertical_source_action_reduction_probe.py`;
- `full20_chimeric_bv_first_write_probe.py`;
- `W125_built_candidate_assembly.py`;
- `W125_sac4_subprincipal_built.py`;
- `full20_observer_projector_support_probe.py`;
- Python compilation of all three new probes;
- exploration surface/boundary, test manifest/inventory, research-posture,
  public-path, changed-public-path, entrypoint, portfolio, and protected-
  surface process gates; and
- `git diff --check`.

The hostile review independently stress-checked the LC identity on 12 random
Kulkarni--Nomizu algebraic curvatures with worst residual
\(1.16\times10^{-13}\), then re-audited the corrected handoff and README
summaries.

`process_gates/lab_process_readme_surface_map_audit.py` remains red on the
pre-existing process-surface inventory drift: `runs/` and six already
tracked direct files are absent from its expected set. This run did not
modify that README or gate and does not treat the unrelated failure as
scientific evidence.

No scientific-claim status, canon verdict, or public posture changes in this
run. N2b and N4b now have constructed finite inputs, but neither has been
executed.
