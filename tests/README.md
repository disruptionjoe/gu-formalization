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
| `de-certification/` (6) | Wave-A internal likelihood consistency, proxy shape-inverse witnesses, the finite W230/conditional FLRW mapping fixture, the synthetic-injection pipeline-unbiasedness control (known truths, DR2-covariance noise), and the exact-rational composition-map first-arrow certificate; register status for C10 / M-H13 / native bridge moves only via the register |
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
| `channel-swings/` (179) | active channel and Lane-1 swing probes, including the native operator/domain/`w1` bridge audit, the Pin+ degree-14 Smith/table gate, the Mannheim--Callias end-admission gate, the quaternionic Fredholm/end-clutching gate, the vertical--Krein source-action/B5 one-bit-weld probe, the three-route full-carrier Bott/vertical/actual-fibre starts, the W177 stationarity plus W131-to-B5 normalized-transport gates, the full-20 coarse observer/BV first-write, its analytic four-primitive formula-support manifest, the native Krein/polarization/curvature closure continuation, the independent thin-embedding rederivation of all 136 observer-complex support cells, the Gamma-natural full-20 DeWitt-loop transport with uniformly central returned mismatch, the finite unified bulk-plus-defect source-action/relative-\(KO\)-datum contract, the actual-`Sym2` native charge-conjugation/Krein four-orbit screen, the Levi--Civita curvature-irrep plus partial open-BV incidence screen, their six-discriminator N3 intersection contract, the N3 term-by-term variational-emission/current-cancellation/dynamical-soldering gate with separate index/causality carry, the ten-persona Vanchurin/GU declared-score contract, the Weinstein primary-source disposition/ordering contract, the post-N3 ten-wave rebase dependency/non-regression contract, the RB1 source/repository required-arrow register, varied-root plus owner ledger, fixed-geometry full-20 graded Green split, native-current-musical, and three-candidate/one-control emission contract, the RB2 classical fixed-geometry antifield-zero five-field bridge/source-endpoint variations and returned `A0` moving-background response, the RB3 native moving-Clifford-plane/\(A_0\)-induced candidate-connection/actual-`Sym2` trace-coordinate/full-20-first-block/homogeneous-discriminator-proxy certificate, the RB1b exact full-Spin same-`Lambda2` parity kill plus separate native grade-admission check and finite quaternionic source-shaped architecture/cyclic-nonimplication certificate, the RB3b trace-reversed fixed-Cartan four-component/native-bilinear/exact-44-supported-block lift plus observer/Cartan and fixed-\(t\) Spin(4)-leak controls, the RB3c typed rectangular vertex/Krein completion/one-matrix-amplitude plus finite-\(SO(3)\) and planted-one-dimensional Green fixtures, the RB1c actual-\((9,5)\) all-algebraic-Riemann/Bianchi closure, deterministic cyclic, and planted polarization-factorization disposition, the RB4 trace-reversed moving-\(u\) Cartan/projector/Clifford/volume/Phi family with frozen-frame controls, separate internal moving-\(t\) branch, compatible-\(J\) existence, the fixed-\(u\) descent obstruction, the RB5 exact Clifford-plane-to-flag stabilizer/lift obstruction plus conditional spectral-projector/polar-derivative/local-unimodularity/gauge-modulus-instability classifier, RB6's target-blind vertical Ricci/trace/curvature-square grammar, finite-resolution `1+9` collapse, action-owned distortion/curvature/section Gram adapters, W177 stationarity carry, RB7's full W177 Euler-tensor slot/floor audit plus exact anisotropic homogeneous non-abelian stationary/saddle, trace-reversal, Gram/polar, and base-incidence classification, and Resolver Waves D--K77-Wave2's native port, moving reduction, nonlinear `Met(X)` descent, source-action comparator, normalized-trace candidate-comparison, exact real-spinor branching, atomic target sequence, source-bracket normalization, exact low-grade Shiab/B1 classification, the algebraic-curvature/four-coordinate displayed-family obstruction, the full-domain cyclic-kernel mechanism kill, the action-first no-bridge Euler/current/pseudo-Riesz/even-Ward plus mixed-super-IG boundary, the source-corrected K77 Dirac--de Rham rolled-symbol/super-IG requirement rebase, the rendered draft-9.16/Hodge-primalizer/formal-adjoint model gate, the actual-carrier total-graded D916 rival/source-sign obstruction/corrected weighted super-bracket gate, the source-sign/degree-reality/D7-Hom reconciliation with exact moving-odd-covector repairs, the trace-reversed tautological-q ownership/full-adjoint/current/Ward-selection gate, the complete sixteen-cell trace-q zero-order/reality coefficient-selection gate with Curt/Weinstein source collision, the common two-layer norm-square action/actual-K77 square-span/cancellation-target gate, the exact two-connection/up-back-over direct-adapter gate, the action-derived raw mixed-Hessian/primalizer-dependence target-typing gate, the exact Euler-receiver equation-leakage/representation-blindness kernel theorem, and the source-collided augmented-torsion four-plus-ten field/Euler receiver with a scoped nonzero-`kappa` conormal witness; source-ledger/scaffold checks remain metadata and logic contracts, while RB1/RB2/RB3/RB4/RB5/RB6/RB7 also execute finite linear-algebra, Hodge-sign, full-gradient finite-difference, affine-chain, homogeneous-conjugation, moving-shape, moving-projector, functional-calculus, right-`H`, and integration-by-parts fixtures |
| `recovery-contract/` (22) | recovery-certification branch-local computational checkpoints, including the construction-space GR R0, SM R0, P3 retro-verification, P4 QM checklist, P5 source-object specification, P6 conditional-interior, lattice schema-freeze, and conservative C1 signature-resolution gates; the GR forced-coefficient residual test; GR no-go history/scope defense gates through Swing 3; cosmological field-type/scalar-truncation and no-go defense gates through Swing 3; Standard Model selector and no-go defense gates through Swing 3; and the QM physical-sector conditional sufficiency gate under the frozen action fingerprint |
| `threads/` (18) | frontier A/B/C/D/E thread audits for the current gravity, dark-energy, and source-action-adjacent gates, with a local script map and README inventory gate |
| `hourly-cycles/` (archived off-tree) | **archived** hourly-automation output; not load-bearing |

The latest channel-swing addition is
`k77_wave2_actual_y14_receiver_ordering_probe.py`: an exact local K77
trace-reversal, form-degree, rank-ten conormal, horizontal-right-inverse,
full-receiver, and three-route variational-repair gate.

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

## Resolver Wave J certificate

`channel-swings/resolver_wave_j_descended_source_action_total_euler_ward_probe.py`
tests a pointwise already-composed source-shaped scalar-density across the
Wave-I three-chart transport, an exact rational cyclic coefficient/
transgression comparator for the source `1/2,1/3`, and separate finite Green
and `GL(2)` covariance fixtures. It keeps those distinct from the unbuilt
native Shiab, monolithic B1 Euler, native Ward, preboundary, and domain. A
degree audit retains the live quadratic coefficient in `Omega2` and never
feeds it to the `Omega1` source port. The public-coset pair `i e0`,
`i e45678` returns native grade-six curvature `-2 e045678`, requiring any
reduced construction to retain `R_J(m wedge m)`; it does not select a port
order or prove Euler tangency. Separate Wave-I metric/Theta/density and
Wave-H chosen-J/projector first jets remain auxiliary live-dependency
witnesses, not one source-action derivative. P1/P2/P3 remain unchanged and
unused. Run it with `uv run --with sympy==1.14.0 --with numpy python
tests/channel-swings/resolver_wave_j_descended_source_action_total_euler_ward_probe.py`.

## Resolver Wave K certificate

`channel-swings/resolver_wave_k_conditional_active_shiab_b1_variation_probe.py`
reconstructs the source `(7,7)` and conditional-active `(9,5)` signature
arithmetic, rejects applying Wave-H `R_J` outside its typed public-`u(K)`
domain, and constructs an explicitly repository-derived normalized-trace
fixed active `Omega2 -> Omega13` grade-projected candidate. One monolithic B1
action has live curvature, covariant-derivative, repository `q_wedge`, and
kappa channels; direct and owner variations agree in independent B/T
directions. A nonzero exact candidate-local `q_wedge` mismatch is retained,
while the source `[T,T]` identity remains untested until bracket normalization
and a real `Cl(7,7)` action are built. The probe also carries exact source
receipts for chimeric spinors as matter and VEV/curvature-dependent effective
chirality, one scoped gauge-owner cancellation, one fixed-background port
fixture, and planted type/owner failures. K77 real spinors, atomic particle
crosswalk, source action, decoupling theorem, global domain, physics, and
P1/P2/P3 remain open. Run it with `uv run --with sympy==1.14.0 --with numpy python
tests/channel-swings/resolver_wave_k_conditional_active_shiab_b1_variation_probe.py`.

## Resolver Wave K77-A certificate

`channel-swings/resolver_wave_k77a_real_spinor_atomic_crosswalk_probe.py`
reuses the exact all-real `Cl(7,7)=M128(R)` construction and verifies the
source `(1,3)+(6,4)` observation split, real invariant symmetric and
alternating pairings, four complex rank-32 `2 x 16` observation blocks, and
an independent `D7 -> D2+D5` weight-parity certificate. It checks one
imported D5/Pati--Salam 16's state-by-state atomic charges and local anomaly
sums, the exact K77 gamma image/kernel dimensions plus source
`F/Q/Z=64/192/576` branch arithmetic, and the bare-operator versus
constructed-Gram `KX` incidence table. It validates a 37-row atomic target ledger linking exact
Eric/Curt source locators to typed mechanisms, local/joint status, five kill
scopes, and reconstruction debt. Planted controls reject K95 imports,
permissive source matching, carrier-to-pole promotion, and the stale
left-Clifford/exterior-Spin conflation, fixed-`c(v)` equivariance, or stale
`R128 -> C64` Step-0 story. It does not construct K77 F/Q/Z projectors, the K77 action,
select a VEV, derive effective chirality, count generations, prove a global
domain, or recover any physical particle pole. Run it with `python3
tests/channel-swings/resolver_wave_k77a_real_spinor_atomic_crosswalk_probe.py`.

## Resolver Wave K77-B certificate

`channel-swings/resolver_wave_k77b_source_bracket_displayed_shiab_b1_variation_probe.py`
uses exact `Cl(7,7)`, fourteen-dimensional exterior/Hodge algebra, and the
real `B`-adjoint to resolve the draft's quadratic as `T wedge T`, one half of
the graded self-bracket. It gives two exact counterexamples to the literal
raw-product Shiab's advertised adjoint codomain, checks all eight source-inspired low-grade
nodewise commutator/`i`-symmetric reconstructions for universal adjoint closure, and compares
direct differentiation of one B1 density with its displayed endpoint on two
constant noncommuting fixtures. Six channels are live and fail; two
zero-defect channels are vacuous. A Sage D7 character calculation certifies
two invariant copies each for Phi1 and Phi2, so the full low/high-grade family
remains open. The probe does not select a Shiab or construct derivative/Green,
Euler/Noether/BV/domain, observation descent, effective chirality, or physical
particles. Run it with `uv run --with sympy==1.14.0 python
tests/channel-swings/resolver_wave_k77b_source_bracket_displayed_shiab_b1_variation_probe.py`.

## Resolver Wave K77-B2 certificate

`channel-swings/resolver_wave_k77b2_shiab_family_curvature_selector_transgression_probe.py`
constructs the rank-3,185 algebraic Riemann first-Bianchi kernel, an explicit
pointwise fixed-frame metric-raised spin-curvature injection with a basiswise
inverse and full internal infinitesimal intertwiner, exact scalar/traceless-
Ricci/Weyl fixtures, and the complexified `D7` decomposition `3185=1+104+3080` with
Shiab-target multiplicities `2,2,0`. It evaluates the complete K77-B source-
inspired low/high factorized repair carrier in features `(a,b,ac,ad,bc,bd)`.
Exactly two product patterns meet the ambient fourteen-dimensional Einstein
ratio; exact
mixed-grade and coefficient-volume-dual transgression counterexamples force
both to the zero map. The result kills only the displayed ansatz for the joint
ambient-Einstein/same-action burden. A two-coordinate Riemann-restriction
Einstein family is explicitly constructed pointwise, while its associated-
bundle descent, full-domain extension, executable grammar typing, bounded DAG
enumeration, differential Bianchi/Green, moving fields, observation, and
physics remain open. Run it with `uv run --with sympy==1.14.0 python
tests/channel-swings/resolver_wave_k77b2_shiab_family_curvature_selector_transgression_probe.py`.

## Resolver Wave K77-B3 certificate

`channel-swings/resolver_wave_k77b3_full_domain_cyclic_kernel_obstruction_probe.py`
computes the complete complexified equivariant Hom dimension and the three
real grade-two low/high contraction coordinates, checks those coordinates on
all 91 compact/noncompact infinitesimal generators, and constructs exact
low/high field pairs with vanishing mixed quadratic source but nonzero
algebraic-Riemann self-source. The two witnesses force the ambient-Einstein
low/high endpoint coefficients to zero for any fixed-metric, fixed-epsilon,
zero-order linear full-domain Shiab used as the same unit-weight cubic Euler
endpoint. An independent FLINT route reproduces the scalar, pairing, and
two-thirds defects. This does not kill K77, `(7,7)`, gravity, source actions,
or the fermion carrier; derivative/moving-field actions and lawful
action-derived domains remain open, and Green/domain is not reached. Run it
with `uv run --with sympy==1.14.0 --with python-flint==0.9.0 python
tests/channel-swings/resolver_wave_k77b3_full_domain_cyclic_kernel_obstruction_probe.py`.

## K77 Wave 2 action/current/Riesz/Ward certificate

`channel-swings/k77_wave2_action_current_riesz_superig_ward_probe.py`
constructs an exact rational action-first comparator with a noncyclic moving
Shiab, source `1/2,1/3` transgression coefficients, a fermion `J_D/J_F`
split, and three no-bridge/bridge presentations. It distinguishes the actual
Euler derivative from the advertised endpoint, shows that a regular parent
reduces to the same symmetrized derivative, verifies the indefinite
connection flat/sharp pairing, and derives the complete even local-IG Ward
contraction with compensator and inhomogeneous-connection plants. A real
symplectic moment-map fixture constructs the symmetric mixed rolled bracket
and verifies landing, equivariance, nonzero odd squaring, and two-step Jacobi.
The bracket is partial `TG-1`, not a full odd action or Ward/BV identity;
observation, domain, vacuum, particles, physics, and P1/P2/P3 remain held out.
Run it with `uv run --with sympy==1.14.0 python
tests/channel-swings/k77_wave2_action_current_riesz_superig_ward_probe.py`.

## K77 Wave 2 Dirac--de Rham/super-IG rebase certificate

`channel-swings/k77_wave2_dirac_derham_superig_rebase_probe.py` separates the
ordinary de Rham Dirac, the truncated `0 -> 1 -> 13 -> 14` chain, the rolled
two-by-two seesaw operator, draft equation 9.16, and the unreleased cyclic
two-connection proposal. On the exact real `Cl(7,7)` spinor it builds the
full first-order `Phi(xi wedge -)` symbol including the trace-removal term,
certifies non-null ranks `1920/1920`, and combines a rank-1024 modular minor
with an explicit 896-coordinate null kernel. It checks the off-diagonal
Krein-adjoint pairing, rejects bare middle self-adjointness, supplies a
conditional nonchiral cross-pairing, and proves that the opposite-half mixed
moment map lands in the simultaneous `B/Omega` stabilizer. It does not select
the global draft operator, cyclic complex, domain, physical generations, or
P1/P2/P3. Run it with `python3
tests/channel-swings/k77_wave2_dirac_derham_superig_rebase_probe.py`.

## K77 Wave 2 draft-9.16/primalizer-template certificate

`channel-swings/k77_wave2_global_draft916_krein_preboundary_probe.py`
checks the rendered four-field source receipt, the `(7,7)` Hodge-square signs,
finite exact primalizer inverses for the `13->1` and `14->0` sectors, and the
moving-density/moving-pairing formal-adjoint Green identity. It extracts the
adjoint principal coefficient from independent symbolic functions, verifies
a nonconstant three-patch overlap **model**, and runs finite discriminating
controls for the southeast fork, one-insertion current, and conjugation
covariance. It does not instantiate the actual sixteen K77 D916 blocks,
`rho(epsilon)` descent, a common invariant action core, physical domain,
observed family index, or P1/P2/P3. Run it with `uv run --with sympy==1.14.0
python tests/channel-swings/k77_wave2_global_draft916_krein_preboundary_probe.py`.

## K77 Wave 2 actual-carrier D916 rival/source-sign certificate

`channel-swings/k77_wave2_actual_draft916_blockwise_probe.py` uses the exact
real 128-spinor K77 carrier to build the conditional total-graded rolled
operator, degree-sensitive Hodge/primalizer, a nontrivial frozen K77 adjoint
and current direction, nonconstant moving-Clifford/connection descent, and an
inverse-trace-weighted Spin-equivariant two-step bracket.  It also checks the
identity-grade section-11.2 ambient field signs and proves that no uniform
same-half or cross-half barred-row duality reconciles those signs with the
selected gamma `Phi d` and exterior `d` parities.  The total grading therefore
defines a rival, not a source-identical completion.  Full zero-order
coefficients, multi-index adjoint, shared-core connection/Ward variation,
full-`H` descent, observation, physics, and P1/P2/P3 remain open.  Run it with
`uv run python tests/channel-swings/k77_wave2_actual_draft916_blockwise_probe.py`.

## K77 Wave 2 source-sign/Shiab/degree-reality reconciliation certificate

`channel-swings/k77_wave2_source_sign_shiab_duality_probe.py` combines the
actual real K77 Clifford carrier with an independent Sage 10.9 `D7` character
calculation. It proves same-half middle-map Hom dimension zero and
opposite-half dimension two; distinguishes the killed barred-row-only duality
from the two full row-and-column degree-reality sign solutions; and shows that
both those solutions and an even middle-symbol repair require one additional
odd vector/covector. Exact left/right `gamma(q)` repairs preserve principal
adjacency and moving transition covariance, while fixed-`q`, zero-`q`,
cell-matcher, and total-grading plants discriminate the claim. The current
free-`q` fit has surplus `-14`; source ownership, full adjoint/current/Ward,
full-`H` descent, Wave 3, physics, and P1/P2/P3 use remain open. Run it with
`uv run python tests/channel-swings/k77_wave2_source_sign_shiab_duality_probe.py`.

## K77 Wave 2 trace-q ownership / adjoint / Ward certificate

`channel-swings/k77_wave2_q_receiver_trace_adjoint_ward_probe.py` proves that
the trace-reversed metric bundle supplies the preceding odd receiver as the
tautological normalized vertical trace vector `q=t_g/2`, with exact DeWitt
norm `-1`, base-frame naturality, and chimeric Clifford type. It computes all
`14 x 14` form-index/spinor Krein adjoints, shows left/right exchange and
commutator/anticommutator eigen-combinations, retains nonzero moving-`q`
formal-adjoint terms, and obtains nonzero placement-sensitive `q` and one
actual even spin-connection-direction current. Both placements descend, so
Ward coefficient-selection rank is zero. Free-`q` surplus improves from
`-14` to `-1`; zero-order reality, moving Hodge/pairing/density, full-`H`
descent, domain, Wave 3, physics, and P1/P2/P3 use remain open. Run it with
`python3 tests/channel-swings/k77_wave2_q_receiver_trace_adjoint_ward_probe.py`.

## K77 Wave 2 trace-q coefficient / zero-order reality certificate

`channel-swings/k77_wave2_trace_q_coefficient_zero_order_reality_probe.py`
assembles all sixteen draft-9.16 operator cells around `q=g/2`. It keeps the
four Shiab placements in one uniform projective coefficient family, verifies
both degree-reality sign solutions, and tests the actual full form-index times
spinor Krein adjoint. Native real conjugation has coefficient-selection rank
zero. The source-faithful independent-bar action therefore retains one
projective coefficient with surplus `-1`; the optional Majorana rival instead
has rank two in every tested self/skew system and leaves only the zero pair.
Six planted failures prevent source compression, cellwise retuning, a false
Majorana selector, and lower-order repair of a principal-symbol failure. Run
it with `python3 tests/channel-swings/k77_wave2_trace_q_coefficient_zero_order_reality_probe.py`.

## K77 Wave 2 common two-layer action / coefficient-selection certificate

`channel-swings/k77_wave2_common_two_layer_action_probe.py` constructs the
first-layer action plus residual-norm second layer at formula grade and checks
its `Upsilon+H^!G Upsilon` derivative with an exact quartic finite control. It
proves the source redundancy leaves fixed-coupling selection rank zero on the
first-order locus, while an optional coefficient-modulus rival returns two
different field-dependent roots. On the actual K77 family it computes
middle-arrow cancellation rank two, anticommutator scalarity for a basis of
all covectors, and rank three for the quadratic self-square tensors. Seven
plants reject target-free matching, one-sample fitting, positive-norm
substitution, scalar-middle promotion, and duplicate bridges. Run it with
`python3 tests/channel-swings/k77_wave2_common_two_layer_action_probe.py`.

## K77 Wave 2 up/back/over target certificate

`channel-swings/k77_wave2_up_back_over_target_probe.py` verifies the exact
two-connection square with curvature-difference and connection-difference
obstructions, uniquely discriminates the spoken two-minus sign placement with
a noncommuting fixture, and expands the universal Bose--Fermi block square.
It then evaluates the actual real K77 middle symbol on all basis covectors and
proves that both direct trace-`q` plus/minus path adapters have coefficient
rank two. Eight plants preserve the unreleased source grade, Krein/type fences,
P1/P2/P3 non-use, and no-physics boundary. Run it with
`python3 tests/channel-swings/k77_wave2_up_back_over_target_probe.py`.

## K77 Wave 2 stabilized mixed-Hessian certificate

`channel-swings/k77_wave2_stabilized_mixed_cross_map_probe.py` retypes draft
equation `10.10` as a rectangular deformation-to-Euler complex and constructs
both raw mixed blocks from one exact common action. It checks full Hessian
reciprocity, nonzero K77 one-form response and coefficient sensitivity rank
two on the real `Cl(7,7)` carrier. Exact alternative primalizers change both
up-and-back composites, while planted controls forbid composing density-dual
blocks or identifying the two-connection and Bose--Fermi gradings. Selection
rank remains zero; global primalizers, a comparison functor, full sixteen-cell
closure, physics, Wave 3 and P1/P2/P3 remain open. Run it with `python3
tests/channel-swings/k77_wave2_stabilized_mixed_cross_map_probe.py`.

## K77 Wave 2 moving-primalizer / two-connection comparison certificate

`channel-swings/k77_wave2_mixed_primalizer_comparison_probe.py` constructs the
four-field density/Krein pseudo-musicals on the actual real `Cl(7,7)` carrier
and checks their inverse, moving-inverse and transition-naturality identities.
It distinguishes density from oriented top-form notation, so P1 is not
consumed. A source collision retypes the unreleased two-connection mnemonic
as a fermion-cyclic completion/rival; an exact `0+13 -> 1+14` Hodge rolling
builds one arrow and finds a typed slot/principal-order mismatch with D916.
Eight plants prevent promotion to a full cyclic complex, action owner,
coefficient selection, physics or datum use. Run it with `uv run --with
sympy==1.14.0 python tests/channel-swings/k77_wave2_mixed_primalizer_comparison_probe.py`.

## K77 Wave 2 shifted two-connection / action-shell certificate

`channel-swings/k77_wave2_two_connection_action_owner_probe.py` assigns the
second de Rham summand internal degree one and proves that Eric's four spoken
blocks form one total-odd operator with two nonzero parity restrictions. An
exact matrix-valued exterior-DGA fixture computes the full square and retains
the nonzero mixed `-T wedge F_B` block that a planted scalar fixture erases. A
separate cyclic fixture identifies `1/2,1/3` with path-average curvature,
checks the endpoint-curvature first variation and an indefinite Helmholtz
Hessian, then proves the diagonal complex shell and action critical shell
differ for curved `B`. Twelve plants prevent promotion to an actual K77 Shiab,
domain, physics or datum use. Run it with `uv run --with sympy==1.14.0 python
tests/channel-swings/k77_wave2_two_connection_action_owner_probe.py`.

## K77 Wave 2 Euler-shell dependent-pair certificate

`channel-swings/k77_wave2_euler_shell_two_connection_probe.py` reuses the
indefinite K77 connection pseudo-musical, computes the restricted natural-map
space before selection, and constructs
`A_E=B+sharp_conn(E_T^{B,act})`. Its exact noncommutative exterior-DGA control
keeps both off-shell defects live and proves that the complete shifted square
vanishes iff the translation Euler row vanishes on a faithful coefficient
module. Moving-inverse, homogeneous transition, shared inhomogeneous-term and
curvature controls pass. Nine plants preserve source silence, zero surplus,
indefinite/domain/physics fences and P1/P2/P3 non-use. Run it with
`PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python
tests/channel-swings/k77_wave2_euler_shell_two_connection_probe.py`.

## K77 Wave 2 Euler-lift observation receiver certificate

`channel-swings/k77_wave2_euler_lift_ward_observation_probe.py` computes the
complete fixed detector `rho_X sharp_X O_E` and realizes both independent
false-shell mechanisms exactly: equation leakage and observed-module
blindness. The no-leakage image with a faithful coefficient action has zero
restricted kernel. Even Ward naturality, finite invariant-image and
preboundary quotient controls pass, while seven plants forbid promotion to an
actual `Y14` receiver, odd BV differential, closed domain or physics. Run it
with `PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python
tests/channel-swings/k77_wave2_euler_lift_ward_observation_probe.py`.

## K77 Wave 2 augmented-torsion four-plus-ten receiver certificate

`channel-swings/k77_wave2_augmented_torsion_defect_euler_receiver_probe.py`
collides Weinstein's augmented-torsion and observer-pullback sources with the
existing N1/N3 build. It proves that ordinary pullback plus vertical
coefficient restriction is a rank-fourteen field isomorphism along a supplied
section and that its inverse transpose is the unique equation dual preserving
the full first-variation pairing. It checks the exact degree-thirteen
`4+10` bigrading and emits degree-three connection plus vertical-valued
degree-four equations. A constant one-generator conormal witness shows that
the published nonzero-`kappa` term prevents automatic horizontality on the
displayed full local translation stratum. Nine plants keep the constrained
source-domain, full defect action, Ward/BV descent, common domain, physics and
P1/P2/P3 fences live. Run it with `uv run --with sympy==1.14.0 python
tests/channel-swings/k77_wave2_augmented_torsion_defect_euler_receiver_probe.py`.
