# tests/

Computational checks for the program's claims. Each file is a standalone audit/gate script (run it directly
with `python`). For a one-step sweep, use `scripts/reproduce_all.py` as the central runner. This manifest is
the map: which directory/group supports which claim.

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
| `generation-sector/` (34) | the generation-count core: Krein signature, net chiral index, chirality kills, Wave-A Reading-A kinematic grading, Wave-B hinge-symbol leakage, Wave-C exact Spin(10)/Lambda5/Pati-Salam channels, and Wave-D exact exterior/Sage native-connection placement certificates (paper-cited surface; frozen paths remain frozen), with a local script map and README inventory gate |
| `observable-algebra/` (5) | finite compression-algebra commutant/trichotomy probes plus exact Wave-B compact-isotypic, Sage character, and neutrality certificates; kinematic carrier evidence only, not a physical observable-algebra, quotient, or signature-selection theorem |
| `de-certification/` (5) | Wave-A internal likelihood consistency, proxy shape-inverse witnesses, the finite W230/conditional FLRW mapping fixture, the synthetic-injection pipeline-unbiasedness control (known truths, DR2-covariance noise), and the exact-rational composition-map first-arrow certificate; register status for C10 / M-H13 / native bridge moves only via the register |
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
| `boundary-eta/` (4) | the boundary eta-invariant / tangential fork, with a local script map, nested independent denominator checks, and README inventory gate |
| `anomaly/` (1) | frontstage anomaly gate validators, currently the Sp(1) 2-primary Dai-Freed AHSS gate, with a local script map and README inventory gate |
| `sm-boundary/` (1) | SM-shaped boundary anomaly-inflow toy, with a local script map, nested independent algebraic verifier, and README inventory gate |
| `calm-gw-boundary/` (1) | finite CALM/GW boundary gate for Jordan-component axial-charge monotonicity versus scalar/rounded readout failures, with a local script map and README inventory gate |
| `pati-salam/` (1) | reproduction harness for the active-research Pati-Salam chain verification scripts, with a local harness map and README inventory gate |
| `enum-completeness/` (2) | enumeration-completeness certificate for the located-not-forced publication gate, with a local script map and README inventory gate |
| `antilinear-bound/` (3) | antilinear-bound certificate for the located-not-forced publication gate, with a local script map and README inventory gate |
| `function-space-ext/` (9) | WC-FUNCTION-SPACE-EXT probes plus the signed-readout UII certificate-shape validator: finite Galerkin, conditional section theorem + independent checks, APS eta boundary control, and UII gap gate, with a local script map and README inventory gate |
| `rs-function-space/` (5) | RS function-space family-index scaffolds: K3 pushforward, boundary eta, family/characteristic-class generation-arena probes, order-3 rho certificates, and geometric `-38` adjudication certificates, with a local script map and README inventory gate |
| `channel-swings/` (157) | active channel and Lane-1 swing probes, including the native operator/domain/`w1` bridge audit, the Pin+ degree-14 Smith/table gate, the Mannheim--Callias end-admission gate, the quaternionic Fredholm/end-clutching gate, the vertical--Krein source-action/B5 one-bit-weld probe, the three-route full-carrier Bott/vertical/actual-fibre starts, the W177 stationarity plus W131-to-B5 normalized-transport gates, the full-20 coarse observer/BV first-write, its analytic four-primitive formula-support manifest, the native Krein/polarization/curvature closure continuation, the independent thin-embedding rederivation of all 136 observer-complex support cells, the Gamma-natural full-20 DeWitt-loop transport with uniformly central returned mismatch, the finite unified bulk-plus-defect source-action/relative-\(KO\)-datum contract, the actual-`Sym2` native charge-conjugation/Krein four-orbit screen, the Levi--Civita curvature-irrep plus partial open-BV incidence screen, their six-discriminator N3 intersection contract, the N3 term-by-term variational-emission/current-cancellation/dynamical-soldering gate with separate index/causality carry, the ten-persona Vanchurin/GU declared-score contract, the Weinstein primary-source disposition/ordering contract, the post-N3 ten-wave rebase dependency/non-regression contract, the RB1 source/repository required-arrow register, varied-root plus owner ledger, fixed-geometry full-20 graded Green split, native-current-musical, and three-candidate/one-control emission contract, the RB2 classical fixed-geometry antifield-zero five-field bridge/source-endpoint variations and returned `A0` moving-background response, the RB3 native moving-Clifford-plane/\(A_0\)-induced candidate-connection/actual-`Sym2` trace-coordinate/full-20-first-block/homogeneous-discriminator-proxy certificate, the RB1b exact full-Spin same-`Lambda2` parity kill plus separate native grade-admission check and finite quaternionic source-shaped architecture/cyclic-nonimplication certificate, the RB3b trace-reversed fixed-Cartan four-component/native-bilinear/exact-44-supported-block lift plus observer/Cartan and fixed-\(t\) Spin(4)-leak controls, the RB3c typed rectangular vertex/Krein completion/one-matrix-amplitude plus finite-\(SO(3)\) and planted-one-dimensional Green fixtures, the RB1c actual-\((9,5)\) all-algebraic-Riemann/Bianchi closure, deterministic cyclic, and planted polarization-factorization disposition, the RB4 trace-reversed moving-\(u\) Cartan/projector/Clifford/volume/Phi family with frozen-frame controls, separate internal moving-\(t\) branch, compatible-\(J\) existence, the fixed-\(u\) descent obstruction, the RB5 exact Clifford-plane-to-flag stabilizer/lift obstruction plus conditional spectral-projector/polar-derivative/local-unimodularity/gauge-modulus-instability classifier, RB6's target-blind vertical Ricci/trace/curvature-square grammar, finite-resolution `1+9` collapse, action-owned distortion/curvature/section Gram adapters, W177 stationarity carry, RB7's full W177 Euler-tensor slot/floor audit plus exact anisotropic homogeneous non-abelian stationary/saddle, trace-reversal, Gram/polar, and base-incidence classification, Resolver Wave D's native grade-six-to-real-252 K/right-H/C/full-20 placement fork, Resolver Wave E's native moving real-252/conditional source-kappa interface/representative half-weight fork, Resolver Wave F's fixed grade-six exterior `Pext`, signed-permutation transport/derivative schema, exact downstream direct-selection classifier, auxiliary price, and `chi=0` basepoint audit, Resolver Wave G's generic-native number-operator `q6`, D7 five-intertwiner census, fixed-pairing rank-252 composite, non-Spin full-`Sp` mover, and exact tilted-source group-law certificate, Resolver Wave H's typed chosen-`J` moving reduction, combined `Psrc(T_omega)`, and projector-first-jet fixture, and Resolver Wave I's nonlinear `Met(X)`/Theta reconstruction, raw-`C*` dual law, and Riesz-ported rank-252 associated-projector fixture; source-ledger/scaffold checks remain metadata and logic contracts, while RB1/RB2/RB3/RB4/RB5/RB6/RB7 also execute finite linear-algebra, Hodge-sign, full-gradient finite-difference, affine-chain, homogeneous-conjugation, moving-shape, moving-projector, functional-calculus, right-`H`, and integration-by-parts fixtures |
| `recovery-contract/` (22) | recovery-certification branch-local computational checkpoints, including the construction-space GR R0, SM R0, P3 retro-verification, P4 QM checklist, P5 source-object specification, P6 conditional-interior, lattice schema-freeze, and conservative C1 signature-resolution gates; the GR forced-coefficient residual test; GR no-go history/scope defense gates through Swing 3; cosmological field-type/scalar-truncation and no-go defense gates through Swing 3; Standard Model selector and no-go defense gates through Swing 3; and the QM physical-sector conditional sufficiency gate under the frozen action fingerprint |
| `threads/` (18) | frontier A/B/C/D/E thread audits for the current gravity, dark-energy, and source-action-adjacent gates, with a local script map and README inventory gate |
| `hourly-cycles/` (archived off-tree) | **archived** hourly-automation output; not load-bearing |

## Loose audit scripts at `tests/` root, by sector

These 255 direct root scripts are referenced as provenance from `canon/*-RESULTS.md`, so they are
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
| **Source / selector / control** | `oq_rk1_*.py` | 3 | OQ-RK1 representation, J-restriction, and effective-operator assembly certificates. |
| **Temporal issuance / source-action steelman** | `temporal_issuance_source_action_steelmen_checker.py` | 1 | source-action steelman certificate retained as root test provenance, not a process-gate verdict. |
| **W-series frontier packets** | `W*.py` | 200 | later root-level W-series frontier certificates, including W242's DESI intake and dependency-aware prediction queue, W245's Finster-sea/Krein-domain discriminator, and W246's faithful CFS self-adjointization ordering reversal, kept in place as provenance while subdirectory migration remains separate review work. |
| **Hardening quick-win notes** | `HQW_*.py` | 1 | standalone confirming tests for the 2026-07-14 hardening quick-win lemma notes (shape-blind `c_R`), kept at root as provenance. |

## Resolver Wave B certificates

`generation-sector/q3_imposter_symbol_invariance.py` separates the internal
hinge projector from external P3 and proves the raw RS symbol leaks at first
order. `observable-algebra/dq3_signature_free_neutrality.py` gives the exact
constraint-restricted neutrality lemma, while
`observable-algebra/dq1_compact_isotypic_data.py` computes the compact
`Spin(9)xSpin(5)` branching and residual dimension on finite kinematic
`ker Gamma`; `observable-algebra/dq1_compact_isotypic_sage.py` independently
checks the B4/B2 character decompositions through Sage without adding Sage to
the ordinary Python harness. These are pre-deposit certificates and do not construct the
physical quotient or move a scientific verdict.

## Resolver Wave C certificates

`generation-sector/q5_spin10_vector_spinor_product.py` derives all four typed
`16x144` products and separates the bare tensor from the conditional
complex-linear dualized Hom factor;
`generation-sector/q5_spin10_vector_spinor_product_sage.py` independently checks
the D5/D7 characters with Sage 10.9. The Q6 script derives the internal
`Lambda5/126` Pati--Salam channel, rejects raw real Lambda5 as an Sp connection
generator by K-adjoint class, and records the unbuilt admissible placement,
reality, VEV, and mass stages. `located-not-forced/mh7_dim13_restatement.py`
checks the purely 3-primary coefficient ledger and the external-product-framing
zero control without claiming the actual radial boundary, framing, class, or
integer P3.

## Resolver Wave D certificates

`generation-sector/q7_native_126_connection_placement.py` proves the exact
signed exterior-algebra ranks and pure-five/pure-seven projectors for
`V10* tensor Lambda6(V10*)`; its Sage companion independently checks the D5/D7
characters and the abstract grade-ten comparator multiplicity. The channel-swing probe
exhausts the actual native grade-four through grade-seven K/right-H/C classes,
tests the trace-reversed written contraction, and separates the useful
one-form comparator's desired 144 component plus paired 16-dimensional
companions from the still-unbuilt full-20 source placement.

## Resolver Wave E certificate

`channel-swings/resolver_wave_e_source_owned_moving_252_full20_probe.py`
builds the native full-14 `4+5=9` carrier and signed exterior adjoint,
rationally reconstructs one-simple-blade horizontal/vertical support
polynomials, and separates the source-silent unweighted reconstruction from a
source-silent representative half-weight candidate. It constructs diagonal
K/C/right-`H` reciprocal and coarse `P0` controls, tests three-frame
constant-conjugation moving-projector covariance, and separately verifies the
displayed source kappa term with a coupled affine-action Ward/Green comparator.
It leaves the source-to-active port, representation-wide half-weight, full
`G2/Y/P0`, total moving Shiab/fermion/bridge Euler residual, stationary VEV,
mass, quotient, analytic domain, and observation no-leakage open.

## Resolver Wave F certificate

`channel-swings/resolver_wave_f_source_port_action_ownership_probe.py`
constructs `Pext^0=j5(1/9)pi_V5 delta` on an already grade-six exterior
carrier, checks all 252 image blades and one off-image input, and reuses the
exhaustive native grade-six/grade-five K/right-`H` matrices. Constant
signed-permutation fixtures test two-leg split transport, composition, one
split-preserving lift, a split-moving control, and one differentiated
projector identity; they do not instantiate the source
`U_(Theta,epsilon)`. An independent Sage calculation certifies two complex
support branches and four real exterior maps after Hodge-star twists, with
`[a:b]` only the star-even subansatz. The probe separates the forced `1/9`
exterior normalization from the one-simple-blade source-silent
`lambda=1/2` placement, shows the displayed kappa term does not directly
select that ratio, prices an isolated algebraic auxiliary, and rejects
arbitrary vectorlike `chi=0` as a canonical physical KO basepoint. `q6`,
public native-`Sp` reduction, tilted `epsilon_src` descent, actual `Theta_Z`
overlaps, total active/transverse Euler closure, VEV, mass, quotient, domain,
no-leakage, and P1/P2/P3 remain open.

## Resolver Wave G certificate

`channel-swings/resolver_wave_g_q6_native_tilted_source_port_probe.py`
exhausts all 16,384 Clifford blades and all 8,256 native adjoint blades to
construct the coefficientwise grade-six projector as a number-operator
polynomial. It independently invokes Sage for the `D7` coefficient and
one-form Hom multiplicities, exposing the grade-ten near-miss. It composes
the fixed-pairing-self-adjoint `1/9` exterior port, tests all 252 image blades,
and checks exact ranks. A square-zero grade-three native mover proves frozen
`q6` is not full-`Sp` equivariant while the conjugated moving family is. Exact
noncommuting rational first jets prove a chosen-`A0=0` left tilted
cancellation, right adjoint covariance, `tau` homomorphism, and semidirect
associativity fixture. A separate `GL(2)` frame surrogate is explicitly not a
Clifford/`Theta_Z` frame, and the combined `Psrc(T_omega)` is untested. The probe does not
construct the public/native reduction, actual `Theta_Z` overlaps, global
Riesz map, source variation domain, total Euler, domain, no-leakage, VEV,
mass, index, count, or P1/P2/P3 coupling.

## Resolver Wave H certificate

`channel-swings/resolver_wave_h_public_native_combined_port_probe.py`
constructs a chosen local right-`H` Reynolds fixed-locus map on an explicitly
phase-typed real public Krein algebra. It checks `Fix(rho_J) intersect u(K) =
sp(K,J)`, rejects arbitrary complex-Clifford inputs, checks the `16384 ->
8256` dimensions with numerical 128-by-128 K/right-`H` controls and independent
Sage arithmetic, and plants its failure as a complex-domain or Lie-algebra
homomorphism. It composes the chosen reduction
with `q6`, the complete rank-252 exterior projector, and Chevalley
reinclusion. A mixed public `T_omega` is then passed through the same moving
projector under both tilted actions, including a public K-unitary mover
outside native `Sp`; frozen reduction fails while moving `J` repairs local
family covariance into `sp(K,J_h)`. Exact symbolic differentiation verifies
the moving-projector formula and differentiated idempotence. The live `-4`
chain term belongs only to an auxiliary quadratic fixture, not the displayed
source action or an Euler covector. The probe does not source or globalize
`J`, derive the stipulated paired-frame law, construct actual
`Met(X)`/`Theta_Z` overlaps, vary `I1B+IF`, or close density/Krein domain,
Euler/Ward/Green, observation no-leakage, VEV, mass, index, count, or
P1/P2/P3 coupling. Run it with `uv run --with sympy==1.14.0 --with numpy
python tests/channel-swings/resolver_wave_h_public_native_combined_port_probe.py`
so its symbolic dependency is explicit.

## Resolver Wave I certificate

`channel-swings/resolver_wave_i_actual_metx_zorro_theta_descent_probe.py`
constructs two integrable nonlinear coordinate shears and an independently
written composite on a local three-chart `Met(X)` fixture. It verifies the
full 14-dimensional first-jet chain rule, exact Christoffel/Hessian
cancellation, and `Theta_recon DPhi=L Theta_recon` on all three overlaps and
their triple. Two Lorentz-fibre fixtures verify the trace-reversed chosen-
`(9,5)` gimmel metric, metric-determinant law, and absolute-density law. At
one rational triple-overlap point, a Lorentz boost and noncommuting rotation
give a coherent Spin lift; a sign flip is a planted inconsistency, not a
global obstruction. The boost exposes the raw `C*` source law `O^-T` versus
the raised projector law `O`. Explicit `sharp_eta` and `flat_eta` construct
`Psrc_raw=flat Psrc_raised sharp`; the incorrect vector law fails, while all
252 selected image basis vectors and representative kernel sectors
intertwine. The probe keeps the chosen `(9,5)` branch separate from live
rival `(7,7)`, chosen `J` separate from source ownership, observer `Gamma`
separate from uncertain Levi-Civita-derived `A0`, and rank 252 separate from
the untouched A9F rank-128 hinge. It does not globalize Theta/Spin, assemble
both tilted connections on the charts, vary the source action, or close
Euler/Ward/Green/domain/no-leakage. Run it with `uv run --with
sympy==1.14.0 --with numpy python
tests/channel-swings/resolver_wave_i_actual_metx_zorro_theta_descent_probe.py`.
