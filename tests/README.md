# tests/

Computational checks for the program's claims. Each file is a standalone audit/gate script (run it directly
with `python`). For a one-step sweep, use `scripts/reproduce_all.py` as the central runner. This manifest is
the map: which directory/group supports which claim.

## Current Eric/Curt campaign gate

- `channel-swings/eric_curt_wave3d_b1_h1_closedness_kill_probe.py` is the
  exact Wave 3D-B1 variable-coefficient analytic gate. It constructs an
  actual W131 `ker Gamma` null vector and a boundary-zero Fourier sequence
  that is `L2`-graph Cauchy while its spacetime `H1` energy diverges. This
  kills the naive `H1` realization but leaves energy/maximal-dissipative and
  nonlinear constraint domains open.
- `channel-swings/eric_curt_wave3d_section_green_domain_probe.py` is the exact
  Wave 3D-A admitted-section gate. It pulls the full 1,664-dimensional W131
  gamma-traceless symbol to a supplied `(3,1)` tangent block, verifies the
  Lorentz characteristic split and native right-`H` structure, and constructs
  a balanced `(832,832)` Green trace. Opposite right-`H` spectral sectors show
  that algebra alone does not select an analytic closed domain.
- `channel-swings/eric_curt_wave3c_y14_atlas_cauchy_domain_probe.py` is the
  exact Wave 3C actual metric-bundle gate. It induces the vertical `Sym^2`
  transition from each base `GL(4)` Jacobian, descends the vertical geometry
  and the split-frame gimmel/section jet, and proves that signature `(9,5)` has neither an
  ordinary hyperbolic direction nor a spacelike codimension-one Cauchy
  hypersurface. Section and ultrahyperbolic/Krein domains remain open.
- `channel-swings/eric_curt_wave3b_cech_domain_quotient_probe.py` is the exact
  rational Wave 3B compatibility gate. It transports the observation/Euler
  packet across three patches, preserves equation-dual and Krein-adjoint
  naturality, checks a finite invariant domain and characteristic quotient,
  and plants a locally split lift that fails overlap descent. It does not
  prove an actual global `Y^14` atlas or analytic closed physical domain.
- `channel-swings/eric_curt_wave3a_observation_dual_leakage_probe.py` is the
  exact rational Wave 3A gate. It separates `R`, `L^vee`, and the indefinite
  pairing adjoint `L^!`, then constructs paired linear and nonlinear ambient
  operators with identical observed equations but different off-image
  leakage. It does not claim a global `Y^14` domain or physical equation.

## Reproducing the lead paper ("Located, Not Forced")

The three files the paper cites for its load-bearing computations live in **`generation-sector/`**:

- `generation-sector/ghost_parity_krein.py` - the carrier's Krein signature is exactly `(+96, -96)` (vectorlike).
- `generation-sector/net_chiral_index_invariant.py` - on the `(96,96)` cross-chirality carrier the net chiral
  index `chi = 0` for every physical subspace, invariant under any linear Krein isometry (Theorem 2).
- `generation-sector/t1a_kinematic_chirality_kill.py` - the kinematic chirality-forcing route is killed.

These three paths are **frozen** (the paper cites them); do not move or rename them.

## Organized subdirectories

| Directory | What it covers |
|---|---|
| `woit-principles/` (5) | exact finite controls for Cartan/Palatini soldering, OS/right-handed transfer, `Gr(2,C^4)` geometry, Lorentzian/Euclidean twistor real slices, and finite OS spectral positivity/failure witnesses |
| `generation-sector/` (27) | the generation-count core: Krein signature, net chiral index, chirality kills (paper-cited; frozen), with a local script map and README inventory gate |
| `hardening-pass/` (2) | staged located-not-forced paper-hardening certificates: OQ-RK1 rank and route-(a) classification, with a local direct/independent script map and README inventory gate |
| `source-action/` (12) | the twisted Rarita-Schwinger / source-action gate work (frozen alongside the paper), with a local script map and README inventory gate |
| `gu-independent/` (11) | the GU-independent class-level structural no-go, with a local script map and README inventory gate |
| `hessian-z3/` (9) | Hessian / Z3 carrier-occupancy checks, with a local script map and README inventory gate |
| `forcing-slot/` (8) | the forcing-slot toy stabilized-source test, with a local script map and README inventory gate |
| `carrier-mass/` (7) | the carrier Dirac-mass capstone, with a local script/output map and README inventory gate |
| `carrier-bit-decision/` (13) | the carrier-bit decision campaign: four analysis legs plus independent referees, with a local script/analysis map and README inventory gate |
| `escape-corners/` (16) | the carrier-bit escape-corners campaign: four analysis legs, corner-open audits, independent referees, and checked-in run logs, with a local script/analysis/log map and README inventory gate |
| `anchored-leads/` (7) | the anchored-leads candidate screens, including an independent Jones-index finite-type recheck, with a local script map and README inventory gate |
| `big-swing/` (48) | adversarial big-swing packets for generation-count, boundary, framed-bordism, mirror-sector, and capability-wall leads, with a local script map and README inventory gate |
| `internal-paths/` (4) | internal follow-up path certificates for OQ-RK1 rank, Y14 bundle index pieces, non-compact signed-readout witnesses, and Sp-family anomaly gates, with a local script map and README inventory gate |
| `symbolic-proofs/` (1) | symbolic structure-level certificates for the core theorem package, with a local script map and README inventory gate |
| `decider/` (4) | the single-decider ("only honest computable integer is one"), with a local certificate map and README inventory gate |
| `chase/` (0) | nested MOVE-1..MOVE-5 chase-to-kill verdict scripts, with a local script map and README inventory gate |
| `boundary-eta/` (3) | the boundary eta-invariant / tangential fork, with a local script map, nested independent denominator checks, and README inventory gate |
| `anomaly/` (1) | frontstage anomaly gate validators, currently the Sp(1) 2-primary Dai-Freed AHSS gate, with a local script map and README inventory gate |
| `sm-boundary/` (1) | SM-shaped boundary anomaly-inflow toy, with a local script map, nested independent algebraic verifier, and README inventory gate |
| `calm-gw-boundary/` (1) | finite CALM/GW boundary gate for Jordan-component axial-charge monotonicity versus scalar/rounded readout failures, with a local script map and README inventory gate |
| `pati-salam/` (1) | reproduction harness for the active-research Pati-Salam chain verification scripts, with a local harness map and README inventory gate |
| `enum-completeness/` (2) | enumeration-completeness certificate for the located-not-forced publication gate, with a local script map and README inventory gate |
| `antilinear-bound/` (3) | antilinear-bound certificate for the located-not-forced publication gate, with a local script map and README inventory gate |
| `function-space-ext/` (9) | WC-FUNCTION-SPACE-EXT probes plus the signed-readout UII certificate-shape validator: finite Galerkin, conditional section theorem + independent checks, APS eta boundary control, and UII gap gate, with a local script map and README inventory gate |
| `rs-function-space/` (5) | RS function-space family-index scaffolds: K3 pushforward, boundary eta, family/characteristic-class generation-arena probes, order-3 rho certificates, and geometric `-38` adjudication certificates, with a local script map and README inventory gate |
| `channel-swings/` (169) | active channel and Lane-1 swing probes, including the native operator/domain/`w1` bridge audit, the Pin+ degree-14 Smith/table gate, the Mannheim--Callias end-admission gate, the quaternionic Fredholm/end-clutching gate, the vertical--Krein source-action/B5 one-bit-weld probe, the three-route full-carrier Bott/vertical/actual-fibre starts, the W177 stationarity plus W131-to-B5 normalized-transport gates, the full-20 coarse observer/BV first-write, its analytic four-primitive formula-support manifest, the native Krein/polarization/curvature closure continuation, the independent thin-embedding rederivation of all 136 observer-complex support cells, the Gamma-natural full-20 DeWitt-loop transport with uniformly central returned mismatch, the finite unified bulk-plus-defect source-action/relative-\(KO\)-datum contract, the actual-`Sym2` native charge-conjugation/Krein four-orbit screen, the Levi--Civita curvature-irrep plus partial open-BV incidence screen, their six-discriminator N3 intersection contract, the N3 term-by-term variational-emission/current-cancellation/dynamical-soldering gate with separate index/causality carry, the ten-persona Vanchurin/GU declared-score contract, the Weinstein primary-source disposition/ordering contract, the Curt-iceberg 30-step/14-cross-cutting source-grade and anti-collapse contract, the paired Curt--Eric 40-axiom/nine-chain bosonic-vs-total-square/Higgs-carrier-fork/Step-13-carrier contract with exact residual-pairing control, the Eric/Curt ten-wave campaign and exact C0 bundle-versus-real-carrier/complexification/lane-promotion gate plus the 22-primitive carrier-port ownership census, Wave 2b quotient/ablation, Wave 3A observation-dual/nonlinear-leakage, Wave 3B finite Cech/domain/quotient, Wave 3C actual-Y14-atlas/Cauchy-domain, Wave 3D-A admitted-section/right-H/Green-trace domain selection, and Wave 3D-B1 variable-coefficient naive-spacetime-H1 closedness-kill gates, the exact rational-matrix Weinstein-guided tilted-cocycle/double-coset displacement/source-Euler transport/Ward shadow with planted wrong-coefficient and object-identity controls, the G3 graph-complete-variation/coupled-Ward/preboundary/minimal-BV correction with isolated-conservation and polarization plants, the G2 selected-field-graph/native-density-dual/slot-symmetrized-Euler correction with cyclic and factorization plants, the G1 first-jet derivative-cocycle/moving-reference/lift/patch/stabilizer/right-H/trace-reversal quotient correction, the post-N3 ten-wave rebase dependency/non-regression contract, the RB1 source/repository required-arrow register, varied-root plus owner ledger, fixed-geometry full-20 graded Green split, native-current-musical, and three-candidate/one-control emission contract, the RB2 classical fixed-geometry antifield-zero five-field bridge/source-endpoint variations and returned `A0` moving-background response, the RB3 native moving-Clifford-plane/\(A_0\)-induced candidate-connection/actual-`Sym2` trace-coordinate/full-20-first-block/homogeneous-discriminator-proxy certificate, the RB1b exact full-Spin same-`Lambda2` parity kill plus separate native grade-admission check and finite quaternionic source-shaped architecture/cyclic-nonimplication certificate, the RB3b trace-reversed fixed-Cartan four-component/native-bilinear/exact-44-supported-block lift plus observer/Cartan and fixed-\(t\) Spin(4)-leak controls, the RB3c typed rectangular vertex/Krein completion/one-matrix-amplitude plus finite-\(SO(3)\) and planted-one-dimensional Green fixtures, the RB1c actual-\((9,5)\) all-algebraic-Riemann/Bianchi closure, deterministic cyclic, and planted polarization-factorization disposition, the RB4 trace-reversed moving-\(u\) Cartan/projector/Clifford/volume/Phi family with frozen-frame controls, separate internal moving-\(t\) branch, compatible-\(J\) existence, the fixed-\(u\) descent obstruction, the RB5 exact Clifford-plane-to-flag stabilizer/lift obstruction plus conditional spectral-projector/polar-derivative/local-unimodularity/gauge-modulus-instability classifier, RB6's target-blind vertical Ricci/trace/curvature-square grammar, finite-resolution `1+9` collapse, action-owned distortion/curvature/section Gram adapters, and W177 stationarity carry, and RB7's full W177 Euler-tensor slot/floor audit plus exact anisotropic homogeneous non-abelian stationary/saddle, trace-reversal, Gram/polar, and base-incidence classification, the ten-lens geometry-first orthodoxy provenance/odds contract with per-specialist nonaggregation controls, the fifteen-row Eric-native physics equation/status/dependency atlas, and the Eric-source-directed five-object closure; source-ledger/scaffold checks remain metadata and logic contracts, while RB1/RB2/RB3/RB4/RB5/RB6/RB7 also execute finite linear-algebra, Hodge-sign, full-gradient finite-difference, affine-chain, homogeneous-conjugation, moving-shape, moving-projector, functional-calculus, right-`H`, and integration-by-parts fixtures |
| `recovery-contract/` (22) | recovery-certification branch-local computational checkpoints, including the construction-space GR R0, SM R0, P3 retro-verification, P4 QM checklist, P5 source-object specification, P6 conditional-interior, lattice schema-freeze, and conservative C1 signature-resolution gates; the GR forced-coefficient residual test; GR no-go history/scope defense gates through Swing 3; cosmological field-type/scalar-truncation and no-go defense gates through Swing 3; Standard Model selector and no-go defense gates through Swing 3; and the QM physical-sector conditional sufficiency gate under the frozen action fingerprint |
| `threads/` (18) | frontier A/B/C/D/E thread audits for the current gravity, dark-energy, and source-action-adjacent gates, with a local script map and README inventory gate |
| `hourly-cycles/` (archived off-tree) | **archived** hourly-automation output; not load-bearing |

## Loose audit scripts at `tests/` root, by sector

These 254 direct root scripts are referenced as provenance from `canon/*-RESULTS.md`, so they are
indexed here in place to keep those reproduction pointers valid. This table covers only direct `tests/*.py`
files; organized families live under their subdirectory READMEs, and governance/process checks moved to
`process_gates/`. The table is guarded by `process_gates/tests_root_readme_inventory_audit.py`.

| Sector | Coverage tokens | Count | Boundary |
|---|---:|---:|---|
| **RS / BV-BRST sector** | `rs_*.py` | 20 | Rarita-Schwinger bicomplex, ghost / Koszul-Tate / BRST structure, `c2` curvature, Clifford projector, and symbol-index certificates. |
| **shiab selector / codifferential** | `shiab_*.py` | 14 | selector complex, gamma-trace, quaternionic H-linearity, seesaw, `Sp(64)`, codiff-obstruction certificates, the complete provenance-expanded B5 observer-symbol matrix, its exact phase-parametric Krein-adjoint/mirror reduction, and the fail-closed five-field native packet ingress contract. |
| **Cycle audits** | `cycle1_*.py`, `cycle2_*.py` | 2 | current root-level cycle gate/certificate audits; other cycle governance gates now live under `process_gates/`. |
| **Generation count & K3** | `gen_*.py`, `sp64_octic_trace_i16.py`, `ahat_genus_y14_i16.py`, `c2_holonomy_*.py` | 6 | generation-count and K3/Y14 provenance certificates retained at the root for stable canon pointers. |
| **Bell / QFT / measurement** | `h3_*.py`, `h3-*.py` | 4 | Pati-Salam CHSH state/correlator, measurement gate, and Cech-sheaf fixture certificates. |
| **Velo-Zwanziger** | `vz_*.py` | 2 | typed-symbol gate and subprincipal `FC-VZ-4` certificates. |
| **GR / cosmology / dark energy** | `theta_flrw_desi_sign.py`, `willmore_el_schwarzschild_order.py` | 2 | root-level cosmology and Willmore-order certificates that remain mathematical tests rather than process gates. |
| **Source / selector / control** | `oq_rk1_*.py` | 2 | OQ-RK1 representation and effective-operator assembly certificates. |
| **Temporal issuance / source-action steelman** | `temporal_issuance_source_action_steelmen_checker.py` | 1 | source-action steelman certificate retained as root test provenance, not a process-gate verdict. |
| **W-series frontier packets** | `W*.py` | 200 | later root-level W-series frontier certificates, including W242's DESI intake and dependency-aware prediction queue, W245's Finster-sea/Krein-domain discriminator, and W246's faithful CFS self-adjointization ordering reversal, kept in place as provenance while subdirectory migration remains separate review work. |
| **Hardening quick-win notes** | `HQW_*.py` | 1 | standalone confirming tests for the 2026-07-14 hardening quick-win lemma notes (shape-blind `c_R`), kept at root as provenance. |
