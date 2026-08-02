# tests/

Computational checks for the program's claims. Each file is a standalone audit/gate script (run it directly
with `python`). For a one-step sweep, use `scripts/reproduce_all.py` as the central runner. This manifest is
the map: which directory/group supports which claim.

## Current Eric/Curt campaign gate

- `channel-swings/eric_curt_wave3d_b2c15r3_same_bundle_native_variation_observation_support_probe.py`
  proves an abstract reduced descent theorem through an exact three-patch
  `SL(2) -> Sp(4)` structural comparator, rejects fixed-projector ambient
  covariance in that comparator, and derives the finite split direction from
  the same `B,T` values plus a declared compatible full first jet. It verifies
  a same-`dT` nonconstant-germ plant, exact nonzero action response,
  ten-fibre non-unimodular delta-current normalization, separate LC/Krein
  coefficient-dual descent, and independent no-leakage controls. It also
  records that the actual Zorro--DeWitt fixture
  has live base coefficient derivatives and plants an `A1 Z1` cancellation,
  preventing promotion of the prior `A2 Z0` ranks. Run it with
  `uv run --with sympy --with numpy python`.
- `channel-swings/eric_curt_wave3d_b2c15r2_full_bch_action_gauge_curvature_adjoint_probe.py`
  proves the full linear grade-3/11 BCH connection is `Delta`-only to all
  orders, rejects that extension for an independent nonlinear odd-grade
  completion. It separately verifies projected `K_u` covariance and a generic
  fixed-total-connection split-action comparator without a new coupling; the
  actual derived-`K_u` action substitution remains open. It proves the Zorro
  third-order symbol cancels, checks the live full-`A2 o Z0` Shiab ranks while
  keeping the effective order-two assembly open, verifies the exact
  sequential Green identity, and separates supported Gysin from an
  unbuilt selected equation-dual. Run it with
  `uv run --with sympy --with numpy python`.
- `channel-swings/eric_curt_wave3d_b2c15q_distortion_substitution_native_zorro_shiab_owner_return_probe.py`
  exhaustively proves the quadratic BCH connection jet has
  `c3^2-c11^2` dependence and common-background rank 91, then plants a live
  quartic term that blocks full-connection promotion. It evaluates the actual
  13-leg Zorro--Shiab coefficient and shaped `51/8` response, exposes the new
  `lambda_red` action-placement burden, and keeps physical surplus uncomputed.
  A compact-support gauge plant makes the candidate's Ward burden explicit.
  Separate Green and algebraic-owner comparators, all eight fixed-curvature
  moving slots, local rank-10 metric response, nonlinear rank ceilings, and
  the 4-plus-9 observation bidegree split are exact. Run it with
  `uv run --with sympy --with numpy python`.
- `channel-swings/eric_curt_wave3d_b2c15p_source_epsilon_tangent_zorro_dewitt_probe.py`
  kills the direct source-epsilon/reduction zero-jet bridge, constructs and
  fully equivariance-tests the rank-364 grade-3/11 distortion bridge for every
  nonzero coefficient pair, prices zero-order and differential conditional
  genuine-omega coefficient returns inside the existing varpi equation, and
  constructs exact `G,dG,d2G`, LC, Riemann, and spin-curvature
  jets for the LC-horizontal Zorro connection metric. Its pullback identity,
  product-surrogate plant, 71-leg active reality gate, and diagonal-Spin
  stabilizer calculation are exact. Run it with
  `uv run --with sympy --with numpy python`.
- `channel-swings/eric_curt_wave3d_b2c15o_native_y14_background_stabilizer_probe.py`
  returns the finite first-action equations in fixed-`varpi` source
  coordinates on the literal epsilon-Shiab branch, proves the live metric
  correction and isolated Green companion, and rejects fixed-`A` reuse by its
  exact Helmholtz defect. The equality with equation 9.4's `odot_omega`
  remains open. It builds a trace-reversed-carrier-compatible fixture from a
  realizable four-dimensional curvature two-jet and explicit affine
  `B`/constant-`T` germs, asserts exact support and word identities with an
  independent native matrix comparator, and computes selected diagonal-Spin
  isotropies `51,42,42,36,36` with held-out `28`. These are not full
  Zorro/DeWitt Y14 or ambient action-jet stabilizers. Run it with the
  repository research-compute environment.
- `channel-swings/eric_curt_wave3d_b2c15n_full_owner_euler_moving_atlas_probe.py`
  constructs the full exact noncentral finite first-action owner tuple from
  independent `E_T` and `E_B`, returns `E_B-E_T` through two moving graph
  owners, verifies its Green/Helmholtz identities and mixed order-three pair,
  and certifies held-out total-symbol dispersion and DN principal
  determinants. It
  fail-closes native atlas promotion until the actual `Y14` owner background
  and stabilizer are constructed. Run it with `uv run --with sympy python`.
- `channel-swings/eric_curt_wave3d_b2c15m_moving_shiab_exact_g2_weighted_euler_probe.py`
  proves differentiated native-Shiab covariance in all 91 vertical Spin-frame
  directions plus representative quotient-tangent naturality, constructs its
  exact ten-owner metric derivative in a declared local symmetric Clifford
  gauge with corrected trace-vector and `Phi2` motion, separates moving
  adjoint/nonzero-six-slot-`DM`/residual-zero and off-shell terms, freezes three
  Douglis--Nirenberg order-cap skeletons, and certifies the
  complete positive-plus-trace polynomial rank chart by all maximal minors.
  Run it with `uv run --with sympy --with numpy python`.
- `channel-swings/eric_curt_wave3d_b2c15r_reductive_return_rank_strata_probe.py`
  proves the native gauge-rotated-LC/reductive principal `h` return vanishes,
  constructs the two optional full-Spin return channels as hostile plants,
  executes the named trace/covector rank census, and recomputes the earned
  fixed-Shiab principal direct sum without promoting it to a full Hessian.
- `channel-swings/eric_curt_wave3d_b2c15_full_quotient_primalizer_lc_graph_probe.py`
  executes all six quotient-owner grades against all seven active residual
  grades, certifies assembled quadratic grade preservation while retaining a
  raw ordered off-grade plant, builds the full indefinite residual inverse,
  and derives the actual ten-owner `D_g G_Y` fourteen-dimensional LC graph.
  It computes the bare fixed-Shiab quotient and isolated metric ranks,
  inertias, their grade-orthogonal comparator, and a live two-trace second-jet
  endpoint. It does not claim the full coupled block: the `h`-valued reduction
  return, all-grade moving Shiab, and exact-G2 Euler branch remain open. Run it with
  `uv run --with sympy --with numpy python`.
- `channel-swings/eric_curt_wave3d_b2c14_active_y14_shiab_graph_conormal_probe.py`
  executes the repaired descended owner: `h=Lambda2`, a complete invariant
  grade-three slice of `g/h`, all vertical lift cancellations, and the
  quotient of its residual image by every `T*Y tensor h` LC return. It
  extracts exact non-null rank plus projected null/mixed lower bounds, a scoped
  grade-three Gram comparator, native matrix representation cross-check,
  quotient-owned moving-Shiab/`DM` response, and a nonzero-endpoint scalar
  density control. Run it with `uv run --with sympy python`.
- `channel-swings/eric_curt_wave3d_b2c13_dupsilon_preboundary_probe.py`
  keeps the compressed source residual and exact G2 action Euler covector
  separate, extracts their exact noncentral first-jet symbols, and proves a
  60/144 symbol difference plus a fixed-`A` graph response of `0` versus
  `1/2`. With an explicit first-jet reference graph it derives both moving
  residual-square variations, exact bulk/Green identities, conormal packets,
  and nonzero unequal presymplectic forms using the density-correct
  `R_jet=rho^-1 Rbar_jet`. The finite exact-action comparator has a live
  second-order graph/Ostrogradsky pair; the active `Y14` analogue is open.
  Run it with
  `uv run --with sympy python`.
- `channel-swings/eric_curt_wave3d_b2c12_active_staged_action_probe.py`
  constructs the active trace-reversed `(9,5)` residual lowerer and inverse
  primalizer, returns its full local metric variation, and verifies the
  inverse-map sign in the bosonic residual square. It executes a differential
  formal-adjoint/Green identity with moving pairing, varies the selected
  southeast term in its connection and fermion slots, returns the current
  through the local `B_rot` graph, and rank-tests a held-out current channel.
- `channel-swings/eric_curt_wave3d_b2c10_active_current_full_tuple_hessian_probe.py`
  proves that the repaired southeast `bar_nu nu` connection current survives
  the active trace-reversed `(9,5)` right-`H`, Krein, and `C+` restrictions.
  It constructs a nonzero aligned `T`-linear `M00` witness and forced
  `M10/M01` seeds, rejects a misaligned raw `c(T)L` component, then
  proves that they can transfer but cannot remove the current under a shared
  connection displacement. It executes the observed normal-frame LC spin
  lift, trace-reversed `(6,4)` DeWitt owner transpose, reduction-graph return,
  and an exact graph-owned full-tuple Ward/Hessian comparator. Its preliminary
  symmetrized Green replay shows zero-order `M0` does not select a domain.
- `channel-swings/eric_curt_wave3d_b2c9_offdiagonal_total_current_preboundary_probe.py`
  computes the graph-source Euler covector with full first jets, proves its
  local coadjoint gauge law, and rejects the old zero-jet reconstruction with
  a pure-`dchi` plant. It varies an independent-dual two-connection fermion
  family, derives its currents and formal `T=A-B` owner chain, and predicts a
  candidate extra comparator channel for the nonzero-southeast repair. It also
  checks a generic same-field moving-lowerer response and an additive
  unsymmetrized-fermion plus G3-shaped Green comparator. The active current,
  constrained-real pullback, selected total form, and common domain remain open.
- `channel-swings/eric_curt_wave3d_b2c8_source_forked_two_connection_square_euler_map_probe.py`
  builds finite connection and independent-dual fermion primalizer
  architecture controls, checks the trace-reversed `(9,5)` Hodge signs and
  right-`H` compatibility inherited from the active factors,
  and squares both degree-correct placements of the tentative 2025
  two-connection tokens. It realizes a source-compatible connection-level
  `A=B` role—the source selects neither placement nor that locus—while
  separating it from the nonzero connection Euler owner. It rejects two
  finite residual-alphabet coefficient fits with fixture-local compatibility
  codimension and verifies finite constant-conjugation covariance plus exact
  core/correction orbit decompositions. The local gauge-tangent derivative and
  full graph Hessian remain unexecuted.
- `channel-swings/eric_curt_wave3d_b2c7_two_connection_somatic_obstruction_probe.py`
  verifies the 2021/2025 source fork, projection-to-contraction correction,
  shortened `0 -> 1 -> 13 -> 14` spine, and the distinction between local
  Krein--Hodge Riesz maps and a reduced symplectic sharp. It proves exact
  symmetric `A/B` first-/second-jet cancellation in fundamental and adjoint
  representations, reconstructs the full rational G2 Euler density from all
  twelve variations, and forces the nonzero coefficient-free correction from
  the affine curvature core. A degenerate presymplectic fixture rejects an
  inverse Poisson-anchor claim before BFV reduction.
- `channel-swings/eric_curt_wave3d_b2c6_fermion_boson_euler_factorization_probe.py`
  verifies the repo-derived affine-segment and `AA/BB/AB` transgression identities,
  arbitrary-jet cancellation in the mixed route, the mixed symplectic bracket,
  separate active `C+`/Krein/right-`H` projected-endomorphism space, G3 graph
  return, and corrected Levi-Civita curved compositions on three Ricci
  fixtures. It also proves that, at an admissible bosonic solution carrying
  the verified B2C5 principal symbol, no nonzero finite-order local polynomial
  odd gauge generator exists, with fourteen planted overclaims rejected.
- `channel-swings/eric_curt_wave3d_b2c5_covariant_action_green_ward_probe.py`
  tests the frozen independent-dual emission candidate, coefficient
  Krein/right-`H`, `C+` principal compatibility including an unequal-chiral
  witness, the explicit chiral-boost field equivalence, and the reciprocal
  Dirac gate. It constructs the tied common positive symmetrizer, collides its
  energy spectral half with the frozen action Green form, verifies exact
  Levi-Civita right-composition fixtures, and labels scalar-curvature and
  hand-built jet-slot controls without promoting them to GU remainders.
- `channel-swings/eric_curt_wave3d_b2c4_shiab_family_southeast_completion_probe.py`
  filters the complete active right-`H` contract/wedge Shiab family with
  two-sided/Ward and Krein gates, proves the zero-southeast wedge control is
  still rank-128 Jordan-defective, and verifies normalized plus unequal
  witnesses from the two-parameter reciprocal-`11/12` southeast family give
  exact spatial Clifford evolution, positive right-`H` symmetrizers, and
  unquotiented observation/physical `nu`.
- `channel-swings/eric_curt_wave3d_b2c3_rolled_omega_source_shiab_probe.py`
  transcribes the draft's rolled `Omega1(S)+Omega0(S)` principal shape and
  inserts the repo's canonical Clifford-contraction candidate into the
  source-open Shiab slot. It derives `A(k)=K(k)Gamma-M(k)`, proves the retained
  rank-128 square-zero Jordan image is exactly the two physical null-Dirac
  `d nu` halves, kills an off-shell spinor gauge/BV reading, and verifies the
  positive right-`H`, observer-nontrivial characteristic quotient only as a
  conditional control.
- `channel-swings/eric_curt_wave3d_b2c2_null_clifford_omega1_completion_probe.py`
  freezes `Pi_kerGamma(k tensor c(k))` before a held-out Jordan collision,
  proves its null-root images exactly span the isolated W131 Jordan sector,
  and derives the complete gamma-trace blocks from `1 tensor c(k)`. It then
  verifies positive right-`H` section evolution, Jordan removal, observer
  retention, and twelve planted interpretation failures.
- `channel-swings/eric_curt_wave3d_b2c2_tau_tangent_bv_collision_probe.py`
  is the Wave 3D-B2C2A exact type-and-curvature collision. It verifies the
  nonabelian tau-tangent homomorphism and the nonflat identity
  `[D_0,D_1]xi=[F_01,xi]`, then rejects identifying the ordinary adjoint
  connection BRST complex with the scalar-spinor/vector-spinor W131 complex.
- `channel-swings/eric_curt_wave3d_b2c_projected_gauge_quotient_gate_probe.py`
  is the Wave 3D-B2C1 collision with the previous source/action and external
  datum attempt. The prior rank-128 projected map has only one rank-64
  characteristic-null half at each root; opposite halves equal the Jordan
  image but are not source-selected. The fixed common rank-512 repair is the
  whole observer-section carrier, so its Hermitian quotient makes observation
  fail to descend.
- `channel-swings/eric_curt_wave3d_b2b_positive_symmetrizer_jordan_obstruction_probe.py`
  is the Wave 3D-B2B full-cone gate. On the actual W131 carrier, each tested
  nonzero spatial generator has a nonzero rank-128 square-zero Jordan
  remainder. The generator is not diagonalizable, so no positive simultaneous
  symmetrizer exists; the next question is whether a justified invariant
  constraint/gauge quotient removes the defective chains.
- `channel-swings/eric_curt_wave3d_b2a_native_time_flux_coercivity_probe.py`
  is the Wave 3D-B2A time-slice energy gate. It computes the actual W131 time
  flux spectrum and shows balanced `(832,832)` inertia. Its positive right-`H`
  spectral absolute value fails to symmetrize every spatial evolution matrix,
  killing that canonical energy candidate while leaving the general positive
  symmetrizer and maximal-dissipative search open.
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
| `channel-swings/` (195) | active channel and Lane-1 swing probes, including the native operator/domain/`w1` bridge audit, the Pin+ degree-14 Smith/table gate, the Mannheim--Callias end-admission gate, the quaternionic Fredholm/end-clutching gate, the vertical--Krein source-action/B5 one-bit-weld probe, the three-route full-carrier Bott/vertical/actual-fibre starts, the W177 stationarity plus W131-to-B5 normalized-transport gates, the full-20 coarse observer/BV first-write, its analytic four-primitive formula-support manifest, the native Krein/polarization/curvature closure continuation, the independent thin-embedding rederivation of all 136 observer-complex support cells, the Gamma-natural full-20 DeWitt-loop transport with uniformly central returned mismatch, the finite unified bulk-plus-defect source-action/relative-\(KO\)-datum contract, the actual-`Sym2` native charge-conjugation/Krein four-orbit screen, the Levi--Civita curvature-irrep plus partial open-BV incidence screen, their six-discriminator N3 intersection contract, the N3 term-by-term variational-emission/current-cancellation/dynamical-soldering gate with separate index/causality carry, the ten-persona Vanchurin/GU declared-score contract, the Weinstein primary-source disposition/ordering contract, the Curt-iceberg 30-step/14-cross-cutting source-grade and anti-collapse contract, the paired Curt--Eric 40-axiom/nine-chain bosonic-vs-total-square/Higgs-carrier-fork/Step-13-carrier contract with exact residual-pairing control, the Eric/Curt ten-wave campaign and exact C0 bundle-versus-real-carrier/complexification/lane-promotion gate plus the 22-primitive carrier-port ownership census, Wave 2b quotient/ablation, Wave 3A observation-dual/nonlinear-leakage, Wave 3B finite Cech/domain/quotient, Wave 3C actual-Y14-atlas/Cauchy-domain, Wave 3D-A admitted-section/right-H/Green-trace domain selection, Wave 3D-B1 variable-coefficient naive-spacetime-H1 closedness-kill, Wave 3D-B2A native-time-flux/canonical-majorant coercivity, Wave 3D-B2B full-positive-cone Jordan-obstruction, Wave 3D-B2C1 source-datum/projected-gauge/Jordan-quotient collision, Wave 3D-B2C2A tau-tangent/BV type-and-curvature collision, the parallel null-Clifford/full-Omega1 completion, Wave 3D-B2C3 rolled-source/canonical-Shiab/conditional-quotient, Wave 3D-B2C4 Shiab-family/southeast-completion, Wave 3D-B2C5 action/Green/curved-Ward, Wave 3D-B2C6 two-connection-transgression/local-parent, Wave 3D-B2C7 source-forked common-owner/map-separation, Wave 3D-B2C8 source-forked connection-complex/Euler-discriminator, Wave 3D-B2C9 first-jet Euler/off-diagonal-current/total-preboundary, Wave 3D-B2C10 active-current/LC-owner/full-tuple-Hessian, Wave 3D-B2C11 owner-transfer/two-action/candidate-current-contribution, Wave 3D-B2C12 active moving-residual-primalizer/staged-action/differential-Green, Wave 3D-B2C15M/N/O/P/Q moving-coefficient/source-coordinate/selected-fixture/direct-tangent-distortion-Zorro/substitution-owner gates, the exact rational-matrix Weinstein-guided tilted-cocycle/double-coset displacement/source-Euler transport/Ward shadow with planted wrong-coefficient and object-identity controls, the G3 graph-complete-variation/coupled-Ward/preboundary/minimal-BV correction with isolated-conservation and polarization plants, the G2 selected-field-graph/native-density-dual/slot-symmetrized-Euler correction with cyclic and factorization plants, the G1 first-jet derivative-cocycle/moving-reference/lift/patch/stabilizer/right-H/trace-reversal quotient correction, the post-N3 ten-wave rebase dependency/non-regression contract, the RB1 source/repository required-arrow register, varied-root plus owner ledger, fixed-geometry full-20 graded Green split, native-current-musical, and three-candidate/one-control emission contract, the RB2 classical fixed-geometry antifield-zero five-field bridge/source-endpoint variations and returned `A0` moving-background response, the RB3 native moving-Clifford-plane/\(A_0\)-induced candidate-connection/actual-`Sym2` trace-coordinate/full-20-first-block/homogeneous-discriminator-proxy certificate, the RB1b exact full-Spin same-`Lambda2` parity kill plus separate native grade-admission check and finite quaternionic source-shaped architecture/cyclic-nonimplication certificate, the RB3b trace-reversed fixed-Cartan four-component/native-bilinear/exact-44-supported-block lift plus observer/Cartan and fixed-\(t\) Spin(4)-leak controls, the RB3c typed rectangular vertex/Krein completion/one-matrix-amplitude plus finite-\(SO(3)\) and planted-one-dimensional Green fixtures, the RB1c actual-\((9,5)\) all-algebraic-Riemann/Bianchi closure, deterministic cyclic, and planted polarization-factorization disposition, the RB4 trace-reversed moving-\(u\) Cartan/projector/Clifford/volume/Phi family with frozen-frame controls, separate internal moving-\(t\) branch, compatible-\(J\) existence, the fixed-\(u\) descent obstruction, the RB5 exact Clifford-plane-to-flag stabilizer/lift obstruction plus conditional spectral-projector/polar-derivative/local-unimodularity/gauge-modulus-instability classifier, RB6's target-blind vertical Ricci/trace/curvature-square grammar, finite-resolution `1+9` collapse, action-owned distortion/curvature/section Gram adapters, and W177 stationarity carry, and RB7's full W177 Euler-tensor slot/floor audit plus exact anisotropic homogeneous non-abelian stationary/saddle, trace-reversal, Gram/polar, and base-incidence classification, the ten-lens geometry-first orthodoxy provenance/odds contract with per-specialist nonaggregation controls, the fifteen-row Eric-native physics equation/status/dependency atlas, and the Eric-source-directed five-object closure; source-ledger/scaffold checks remain metadata and logic contracts, while RB1/RB2/RB3/RB4/RB5/RB6/RB7 also execute finite linear-algebra, Hodge-sign, full-gradient finite-difference, affine-chain, homogeneous-conjugation, moving-shape, moving-projector, functional-calculus, right-`H`, and integration-by-parts fixtures |
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
