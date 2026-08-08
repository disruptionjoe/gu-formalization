# tests/

Computational checks for the program's claims. Each file is a standalone audit/gate script (run it directly
with `python`). For a one-step sweep, use `scripts/reproduce_all.py` as the central runner. This manifest is
the map: which directory/group supports which claim.

## Current Eric/Curt campaign gate

- `channel-swings/selected_k77_total_upsilon_null_screen_probe.py` assembles
  the complete parity-graded source tangent, proves exact full linearized
  superconnection Bianchi closure, constructs the labelled ambient rank-12
  `(6,6)` null screen, and proves that the source-required `kappa_1 T` term
  leaves a rank-four total raw-`Upsilon` defect outside the curvature-only
  grade-two fit. Run it with
  `uv run --with numpy --with sympy==1.14.0 python`.
- `channel-swings/conditional_physics_ledger_v060_probe.py` verifies the
  append-only five-row distance/mapping migration and frozen verdicts,
  residue, quotients and external datum.

- `channel-swings/selected_k77_full_reduction_quotient_reconciliation_probe.py`
  composes the source-owned global labelled Clifford reduction with the v0.58
  graph, proves central-stabilizer basicness of the paired object, preserves
  the horizontal-plane forgetful failure, and closes the invariant-replacement
  horn by exact Spencer/target-span arithmetic. Run it with
  `uv run --with numpy --with sympy==1.14.0 python`.
- `channel-swings/conditional_physics_ledger_v059_probe.py` verifies the
  append-only five-row distance/mapping migration and frozen verdicts,
  residue, quotients and external datum.

- `channel-swings/selected_k77_source_graph_basicness_probe.py` transports the
  corrected four-column K77 lift through an exact full-frame three-patch
  cocycle, then computes rank-four horizontal and normal stabilizer defects,
  the three-dimensional invariant Hom span, and failed quotient basicness.
- `channel-swings/conditional_physics_ledger_v058_probe.py` verifies the
  append-only five-row distance/mapping migration and frozen verdicts,
  residue, quotients and external datum.

- `channel-swings/selected_k77_cartan_spencer_signature_correction_probe.py`
  rebuilds the full raw-target, selected-Shiab, Koszul and fixed-epsilon
  source-`varpi` chain on settled K77 `(7,7)`, supersedes every old `(9,5)`
  coefficient packet, and proves that the pointwise rank-four/support theorem
  survives exactly.
- `channel-swings/conditional_physics_ledger_v057_probe.py` verifies the
  append-only five-row provenance/mapping migration and frozen verdicts,
  residue, quotients and external datum.

- `channel-swings/selected_source_varpi_cartan_composition_probe.py` types the
  fixed-epsilon source tangent as `delta B=0`, `delta T=delta A=alpha`, composes
  its endpoint response with the four exact Koszul preimages, and reconstructs
  all transverse 117 pointwise with supports `57,34,34,34`, rank four and zero
  coefficient freedom at fixed nonzero background.
- `channel-swings/conditional_physics_ledger_v056_probe.py` verifies the
  append-only five-row distance migration and frozen verdicts, residue,
  quotients and external datum.

- `channel-swings/selected_nonzero_background_cartan_spencer_owner_probe.py`
  proves the nonzero-background unrestricted Cartan/Spencer connection map is
  an exact rank-1,274 isomorphism, reconstructs all transverse 117 coefficients
  with rank-four Koszul preimages, and proves the Levi-Civita torsion-free
  subclass remains q-exact with zero transverse intersection.
- `channel-swings/conditional_physics_ledger_v055_probe.py` verifies the
  append-only five-row distance migration and frozen verdicts, residue,
  quotients and external datum.

- `channel-swings/selected_invariant_constituent_operator_naturality_probe.py`
  constructs exact selected `F_A*,T*`, checks their nonzero coefficientwise
  cancellation and proves the invariant branch-tangent natural operator packet
  is zero while fixed-coordinate Hodge/target transport controls stay live.
- `channel-swings/conditional_physics_ledger_v054_probe.py` verifies the
  append-only five-row distance migration and frozen verdicts, residue,
  quotients and external datum.

- `channel-swings/selected_second_layer_residual_constituent_operator_correction_probe.py`
  preserves the q-exact connection-class theorem and separates zero total
  residual/common co-motion from a live independent constituent-operator
  derivative with an exact counterexample.
- `channel-swings/conditional_physics_ledger_v053_probe.py` verifies the
  append-only five-row distance migration and frozen verdicts, residue,
  quotients and external datum.

- `channel-swings/conditional_physics_ledger_v052_probe.py` freezes verdicts,
  residue and quotients while migrating exactly five row distances to the
  residual-zero owner-class retype.
- `channel-swings/selected_second_layer_transverse117_residual_zero_owner_class_probe.py`
  proves the whole connection-curvature principal class remains q-exact,
  checks moving-operator vanishing at zero residual and plants a live nonzero-
  background control.

- `channel-swings/conditional_physics_ledger_v051_probe.py` freezes all
  verdicts and residue while migrating exactly five row distances to the
  fixed-B partial-owner result.
- `channel-swings/selected_second_layer_translation_curvature_principal_owner_probe.py`
  proves the fixed-`B` `q wedge delta T` image owns support 28 and not the
  transverse support 117, retains ranks four and four, and excludes
  `T wedge T` as an odd first-order principal enlargement.
- `channel-swings/conditional_physics_ledger_v050_probe.py` preserves all
  predecessor rows, supersedes only stale `AC-G1`, appends `AC-G1a` as the
  settled-horn missing construction, verifies active counts `32/19/26/5`, and
  freezes residue, quotient and P1/P2/P3 boundaries.
- `channel-swings/selected_second_layer_gcr_exterior_degree_owner_retype_probe.py`
  exhausts all 8,281 classical `Cl2` curvature columns, proves their selected-
  Shiab outputs occupy only Clifford grades one and five with zero grade-two
  target entries, preserves the exact rank-1,274 `Cl1 -> Cl2` isomorphism and
  excludes the single-`q` adapter by its rank-thirteen image and the four
  seven-component `q`-direction witnesses.
- `channel-swings/conditional_physics_ledger_v049_probe.py` freezes headline
  counts and residue, migrates exactly five rows to the odd-source owner gate
  and forbids datum, quotient, canon or posture inflation.
- `channel-swings/selected_second_layer_nonnull_koszul_gcr_split_probe.py`
  replays v0.47, constructs the canonical non-null connection part, measures
  the rank-four transverse completion burden, verifies exact selected-Shiab
  recombination and plants a null-screen dependence control.
- `channel-swings/conditional_physics_ledger_v048_probe.py` freezes headline
  counts and residue, migrates exactly five rows and forbids datum, quotient,
  canon or posture inflation.
- `channel-swings/selected_second_layer_shiab_inverse_bianchi_completion_probe.py`
  proves the full selected Hodge-Shiab map is an exact rank-1,274 isomorphism,
  reconstructs the four unique split preimages and proves every principal
  Bianchi wedge map has rank fourteen. It rejects only the standalone split-
  jet identification and leaves total GCR completion open.
- `channel-swings/conditional_physics_ledger_v047_probe.py` freezes headline
  counts and residue, migrates exactly five rows and forbids datum, quotient,
  canon or posture inflation.

- `channel-swings/selected_second_layer_normal_jet_carrier_compatibility_probe.py`
  proves that the v0.42 background-subtracted Hessian is not the Gram of a
  residual difference, while the raw rank-four graph-orbit corrections all lie
  in the exact rank-1190 source-native mixed-normal carrier. It leaves the
  actual prolonged field jet and any background-subtraction owner open.
- `channel-swings/conditional_physics_ledger_v046_probe.py` freezes headline
  counts and residue, migrates exactly five rows, and enforces the owner-map
  correction without datum, quotient, canon or posture inflation.

- `channel-swings/pw2fr2b2b2i2_resumable_third_size6_full_evaluator_probe.py`
  byte-pins the committed `5/380` predecessor ledger, selects the first
  remaining canonical key before evaluator output, and certifies owners
  `(0,0)` at quartic point `(0,0,3,1)`. Its complete six-cell orbit passes all
  twelve non-self generator edges and `48/48` slots per evaluator layer, with
  exact mixed actions `749/144`, `-1499/288`, `749/144`, `-203/288`,
  `3379/288`, and `4675/288`. Durable coverage is `6/380`; dense heldouts
  remain `0/6` executed, the other 374 representatives stay open, and the
  1,925-cell fallback remains live. Run it with
  `uv run --with sympy==1.14.0 --with numpy==2.5.1 python`.
- `channel-swings/pw2fr2b2b2i2_resumable_second_size6_full_evaluator_probe.py`
  byte-pins the committed `4/380` predecessor ledger, selects the first
  remaining canonical key before evaluator output, and certifies owners
  `(0,0)` at quartic point `(0,0,2,2)`. Its complete six-cell orbit passes all
  twelve non-self generator edges and `48/48` slots per evaluator layer, with
  exact mixed actions `-31/144`, `-697/144`, `-31/144`, `-409/144`, `871/72`,
  and `1015/72`. Durable coverage is `5/380`; dense heldouts remain `0/6`
  executed, the other 375 representatives stay open, and the 1,925-cell
  fallback remains live. Run it with
  `uv run --with sympy==1.14.0 --with numpy==2.5.1 python`.
- `channel-swings/pw2fr2b2b2i2_resumable_first_size6_full_evaluator_probe.py`
  creates the append-only exact coverage chain and certifies the
  lexicographically first representative outside the durable `3/380`
  predecessor. Its six-cell orbit passes all twelve non-self generator edges
  and `48/48` slots per evaluator layer, with exact mixed actions `-523/144`,
  `-1379/288`, `-523/144`, `-1235/288`, `3499/288`, and `3643/288`.
  Durable coverage is `4/380`; six dense heldout inputs are preregistered but
  unexecuted, the other 376 representatives remain open, and the 1,925-cell
  fallback stays live. Run it with
  `uv run --with sympy==1.14.0 --with numpy==2.5.1 python`.
- `channel-swings/pw2fr2b2b2i2_affine_first_size3_full_evaluator_probe.py`
  certifies all ten owners at the zero plus four coordinate conormal
  directions with exact affine spanning under both S3 generators, then
  certifies the lexicographically first non-fixed size-three orbit through the
  full mixed evaluator. The affine layer passes 100/100 generator edges and
  800/800 moving-family checks; the selected orbit passes 24/24 slots per
  layer with exact actions `-727/144`, `-727/144`, and `107/9`. Durable
  coverage is exactly `3/380`; the other 377 representatives remain open.
  Run it with `uv run --with sympy==1.14.0 --with numpy python`.
- `channel-swings/pw2fr2b2b2i2_s3_fixed_orbit_full_evaluator_probe.py`
  certifies the complete mixed geometry, Phi1/Phi2, Hodge, Shiab residual,
  moving-primalizer, and action evaluator on both one-cell S3 orbits under
  both generators. Every layer passes `16/16` slots, exact mixed actions are
  `215/8` and `87/16`, and nonvacuous moving-Hodge/wrong-lift controls fire.
  Coverage is exactly `2/380`; the other 378 representatives and dense
  universal held-outs remain open, and the 1,925-cell fallback stays live.
  Run it with `uv run --with sympy==1.14.0 --with numpy python`.
- `channel-swings/pw2fr2b2b2i1_s3_geometric_transport_probe.py` certifies both
  exact S3 generators on the universal owner/conormal geometric layer, including
  all 1,925 joint labels, the `{1:2,3:115,6:263}` orbit census, independent
  Burnside count `380`, and dense nonlinear held-outs. It does not promote the
  380-representative evaluator: Phi/Hodge/Shiab, residual, moving-primalizer,
  and action transport remain open, and the 1,925-cell fallback stays live.
- `channel-swings/pw2fr2b2b2i_separate_conditional_active_c4_banks_probe.py`
  byte-pins the accepted quartic-basis, bank-grade precedent, H/H2/H3, and H4
  evidence; proves the `55` owner-pair, `35` monomial, and `1,925` cell-per-bank
  requirements; and audits the accepted H/H2 coverage as one shared pair at
  one setting. It retains their parameterized constructors while failing
  complete-bank promotion closed. It uses the standard library only.
- `channel-swings/pw2fr2b2b2h4_source_active_real_form_scope_exit_probe.py`
  verifies the exact `(7,7)` versus `(9,5)` inertia, real-reality,
  Clifford-module, common-complexification, and group/coset boundaries, then
  audits the pinned source/PW1/H3 records for the two-stage global port data.
  It earns a source-attribution evidence-scope exit while keeping the
  independent moving-J construction open and admitting only separate
  conditional-active C4 banks downstream. Run it with
  `uv run --with sympy==1.14.0 python`.
- `channel-swings/pw2fr2b2b2h3_source_epsilon_curvature_orbit_graph_probe.py`
  verifies exact connection-level gauge curvature through a live mixed source
  slot, rejects omission of `epsilon^-1 d epsilon`, and constructs the formal
  active Spin(9,5) curvature/trace/Phi/Shiab orbit through `(1,r,s,rs)`. The
  moved residual equals transport, both partial routes are live, and the full
  residual norm stays `(981/64,0,0,0)`. It closes only the conditional local
  orbit, not the global real-form bundle port or either C4 bank. Run it with
  `uv run --with sympy==1.14.0 python`.
- `channel-swings/pw2fr2b2b2h2_i2b_second_residual_primalizer_pairing_probe.py`
  constructs the conditional active residual, Hodge primalizer, and symmetric
  pairing second jet on the accepted nonlinear coframe. It recovers the
  full-carrier norm `981/64`, matches both accepted first Hodge slots, and
  reassembles mixed action `-103/256` from all five off-shell `I2B` Hessian
  families with frozen/omitted/positive-Hilbert plants. It closes only the
  scoped fixed-background dependency, not the global curvature graph or C4
  banks. Run it with `uv run --with sympy==1.14.0 python`.
- `channel-swings/pw2fr2b2b2h_mixed_shiab_second_jet_probe.py` constructs the
  exact sparse bivariate normalized-trace/Phi/Hodge/Shiab operator jet, checks
  all 196 Clifford relations, both accepted first-order constructors, Hodge
  square, owner swap, curvature linearity, and frozen-trace/omitted-cross
  plants. It closes only the scoped operator dependency, not either complete
  C4 bank. Run it with `uv run --with sympy==1.14.0 python`.
- `channel-swings/pw2fr2b2b2f_i1_transgression_projective_kappa_probe.py`
  constructs the written transgression in the conditional active canonical
  coframe, matches an independent curvature-path integral and direct
  full-polynomial raw-density derivative, proves a degree-five ceiling, and
  compares two exact quartic density rows projectively. The result is a
  frozen-Shiab raw-density comparator, not a Green/Helmholtz-reduced Euler
  operator. Run it with `uv run --with sympy==1.14.0 python`.
- `channel-swings/pw2fr2b2b2e_actual_u4_jet_realizability_probe.py`
  builds the conditional active nonlinear two-wave Zorro metric and corrected
  symmetric coframe, checks all ten principal owner tangents, independently
  differentiates the quadratic-distortion action, and proves by universal
  max-degree propagation that every non-normal route stops at C3 while the
  normal route reaches C4. Three off-diagonal independent-conormal held-outs
  confirm `U4=0`. Run it with `uv run --with sympy python`.
- `channel-swings/pw2fr2b2b2d_kappa_c4_identifiability_probe.py`
  reconstructs the complete corrected-source-tangent normal `kappa1`
  `J*H*J` quartic subbank over all 35 conormal monomials, checks three dense
  held-outs, independent formal adjoints, a direct mixed action derivative,
  and a live native-ray Green concomitant. Its two relaxed `U4` completions
  are algebraic constraint-ledger witnesses, not realized geometric jets;
  R2B2B2E owns the conditional principal `U4` verdict. Run it with
  `uv run --with sympy==1.14.0 python`.
- `channel-swings/pw2fr2b2b2c_i2b_offshell_c5_ceiling_probe.py`
  expands the complete five-family off-shell residual-square Hessian, checks
  every family on a live exact control, and combines symbolic observed-base
  `J3=0` with all fourteen second-Frechet ceilings. It proves every admitted
  route stops at order four or below, while planted `J3`, `D2E`, and moving-
  primalizer controls restore C5/C6. It is an order ceiling, not a C4 bank.
  Run it with `uv run --with sympy --with numpy python`.
- `channel-swings/pw2fr2b2b2b_source_residual_leading_symbol_probe.py`
  derives the conditional fixed-`(epsilon,varpi)` active ten-owner tangent,
  ports thirteen residual coordinates into the full carrier, and proves the
  observed-base pre-Shiab incidence, `I1` C5, and residual-zero normal `I2B`
  C6/C5 cancellations with a live non-LC plant. Run it with
  `uv run --with sympy python`.
- `channel-swings/pw2fr2b2b2a_native_coefficient_action_split_probe.py`
  extracts one exact contracted active moving-Shiab coefficient, enumerates
  the complete ordered finite density/Krein/lowerer/pairing product rule, and
  differentiates finite `I1` and `I2B` Hessians separately with frozen,
  reordered, off-shell, and residual-zero controls. The five slot matrices
  are ownership/order fixtures, not actual induced-`Y14` tensors. Run it with
  `uv run --with sympy --with numpy python`.
- `channel-swings/pw2fr2b2b1_source_comoving_second_graph_probe.py` builds an
  exact finite source `q/Gamma` split and one repository-derived co-moving
  `h/theta1/Bhat2` graph. It verifies affine split identities, curvature
  conjugacy, an independently assembled live `Bhat2`, frozen/commuting
  controls, and direct versus two-term pullback Hessian agreement. It does not
  compute the native C5/C4 or either `I1`/`I2B` Hessian. Run it with
  `uv run --with sympy python`.
- `channel-swings/pw2fr2b2b1_primary_source_collision_probe.py` re-pins the
  primary-source corpus, keeps source epsilon separate from repository h,
  and records the finite second graph as repository-derived. Run it with
  `python3`.
- `channel-swings/pw2fr2b2a_second_frechet_c4_graph_probe.py` reconstructs
  the exact rank-35 partial fixed-total-connection quartic comparator and its
  live moving-Shiab and `NONE/ANY/UNIQUE(kappa)` controls. It deliberately
  blocks complete-C4 promotion until the source `q/Gamma` tangent split,
  co-moving second graph, and five coefficient slots are built. Run it with
  `uv run --with sympy python`.
- `channel-swings/pw2fr2b2a_primary_source_collision_probe.py` pins the
  source corpus and rendered draft receipt, records the global-section
  disagreement, modern trace reversal, contorsion-slot claim, and source
  silence on the repository second graph. Run it with `python3`.
- `channel-swings/pw2fr2b1_section_jvp_source_coordinate_probe.py` corrects
  the literal fixed-`varpi` source tangent, verifies the unified
  section/Zorro JVP and curved pullback controls, proves first-JVP data
  insufficient for an off-shell pulled Hessian, and constructs the exact
  rank-35 quartic reconstruction and global-`kappa1` proportionality gate. It
  is a prerequisite, not the complete actual-`Y14` C4. Run it with
  `uv run --with sympy python`.
- `channel-swings/pw2fr2b1_primary_source_collision_probe.py` pins the
  source/control artifacts and separates source-confirmed connection/Zorro
  grammar from repository-derived tangent/Hessian results and source silence
  on the complete C4. Run it with `python3`.
- `channel-swings/pw2fr2_total_swervature_kappa_probe.py` derives a noncyclic
  directional Euler-covector remainder and hence an eddy candidate from the pinned action,
  rejects one universal constant `kappa1` across two exact finite background
  families, and checks two-layer plus linearized Green identities. It leaves
  the constrained actual-`Y14` exceptional locus open. Run it with
  `uv run --with sympy python`.
- `channel-swings/pw2fr2_total_swervature_source_probe.py` pins the draft and
  Portal source claims while keeping the written action transgression, the
  repository eddy candidate, and Portal's unspecified eddy distinct. Run it with
  `python3`.
- `channel-swings/pw2fr_complete_derived_k_c3_probe.py` restores the omitted
  derivative-bearing `Z1` metric graph, composes the highest derived-`K`
  incidence, executes the structural `C6` comparator, proves scoped
  all-base-conormal `C5` cancellation, and isolates a live principal-`Z1`
  `kappa1` distortion-norm `C4` contribution. Run it with
  `uv run --with sympy python`.
- `channel-swings/pw2fr_primary_source_collision_probe.py` replays hashed
  source artifacts and keeps fixed source `epsilon`, an independently varied
  source `epsilon`, and repository-derived `h` separate. Run it with `python3`.
- `channel-swings/pw2fr_flint_rank_crosscheck.py` independently certifies the
  non-null rank-ten/nonzero-determinant and null rank-zero contribution over
  exact FLINT rationals. It reuses the primary geometric matrices and is an
  arithmetic-backend check, not an independent geometry. Run it with
  `uv run --with sympy --with python-flint python`.
- `channel-swings/pw2fr_sage_principal_helmholtz_crosscheck.sage` is an
  independent structural `C6/C5/C4` polynomial comparator. It does not
  assemble the native action.
- `channel-swings/pw2f_native_top_order_metric_composition_probe.py` composes
  the induced-Y14 Levi-Civita alternation subroute and selected fixed
  curvature panel, then preserves the hostile correction: a live omitted
  derived-K summand on 129 columns and non-skew vertical/mixed C3
  contributions. It also tests the separate raw moving-Shiab bank and the
  conditional ten-owner affine-second-jet Euler/Green theorem. Complete native
  top order remains open. Run it with `uv run --with sympy python`.
- `channel-swings/pw2f_metric_diffeomorphism_ward_probe.py` derives an exact
  natural-lift diffeomorphism Noether identity/current with a live metric owner
  and keeps the internal Ward separate. Run it with
  `uv run --with sympy python`.
- `channel-swings/pw2f_primary_source_collision_probe.py` verifies strict JSON,
  author-PDF custody, source-file and exact locator-slice hashes, scoped
  absence-search hashes/queries, typed objects, and anti-collapse plants. Run
  it with `python3`.
- `channel-swings/pw2f_sage_jet_helmholtz_crosscheck.sage` and
  `channel-swings/pw2f_flint_exact_rank_crosscheck.py` independently check the
  structural affine-second-jet/Green theorem and selected rank-seven/rank-ten
  certificates in SageMath and python-flint/Arb; neither assembles the native
  action.
- `channel-swings/pw2e_finite_native_shiab_descent_probe.py` checks the exact
  finite active grade-3/11 Shiab on elliptic, hyperbolic, and Hodge-null
  branches; full-basis invariant rank-8256 projector; three-patch coefficient,
  tensorial-`K`, and affine-`B+K` descent; and the transported-only pairing and
  representation-covector boundary. Run it with
  `uv run --with sympy --with numpy python`.
- `channel-swings/pw2e_mixed_metric_frechet_native_ward_probe.py` checks the
  structural fixed-varpi adjoint/Green chain, all eight actual moving-Shiab
  metric slots, rank ten across ten owners, the induced-Y14 LC graph, an exact
  top-order cancellation, and the conditional fourth-jet sufficiency test.
  Run it with `uv run --with sympy --with numpy python`.
- `channel-swings/pw2d_native_transported_shiab_action_probe.py` checks the
  repaired Q-family tangent identity, independently zero transported-grade-
  projector response, all-thirteen-leg `ker Alt` split, literal full-K and
  complete `kappa1/2` bosonic distortion-norm action jet, Delta-only quadratic response, separate
  eight-slot/ten-owner coefficient bank, native `(6,4)/(9,5)` signature, and
  explicit PW2E boundaries. Run it with
  `uv run --with sympy --with numpy python`.
- `channel-swings/pw2d_right_tilted_ward_green_probe.py` checks the derivative
  cocycle, left/right tilted distinction, structural nonabelian Ward identity,
  literal `B+K` covariance, generic old-root `(DF)^!` tuple, independent raw
  pulled-action integration, separate graph Green layer, and total endpoint.
  It is a local `GL(2)` comparator, not the native all-owner Ward. Run it with
  `uv run --with sympy python`.
- `channel-swings/pw2c_literal_source_jacobian_full_k_probe.py` checks the
  fixed-Q,g active-germ source-root Frechet block, finite-mode versus hostile
  scalar interval/domain and `dexp`-resonance distinctions, three-patch group
  plus nonconstant affine descent, literal `K_full` and nonzero-`delta B` variation,
  curvature conjugacy, and equal-Delta/Hodge-null discrimination. Run it with
  `uv run --with sympy python`.
- `channel-swings/pw2c_moving_action_ward_bv_probe.py` checks a scalar
  dependency comparator's pulled Euler/Green identity, mixed `2/3/4` order
  ledger, `1/2/2` Green depths, scalar gauge-null Hessian, nonvacuous Abelian
  Ward/preboundary identity, ordinary cotangent and finite Abelian BRST
  comparators, and the separate native eight-slot moving-Shiab
  replay. Run it with `uv run --with sympy python`.
- `channel-swings/pw2b_literal_native_source_port_probe.py` checks active
  grade-3/11 right-`H`/Krein/`C+` membership, moving-projector identities,
  direct Hodge-null projector motion, `K_full`/`K_red` separation, the
  structural-only tangent comparator, trace reversal, source-bundle fork,
  and datum/Curt/TG controls. Run it with `uv run --with sympy python`.
- `channel-swings/pw2b_source_composed_action_order_probe.py` checks the exact
  minus-one-sixth transgression normal form, compatible pointwise
  curvature-orbit `dK`, identity-Shiab varying-varpi order-two attainability,
  one- and two-layer Green identities, and the open literal
  derived-K/moving-Shiab/Ward/BV/domain boundary. Run it with
  `uv run --with sympy python`.
- `channel-swings/pw2a_source_legal_moving_reduction_lift_probe.py` separates
  algebraic, type/registry, source-receipt, and planted counts while checking
  the abstract co-moving `GL(2)` mechanism, fixed total connection,
  nonzero-background curvature conjugacy, full/projected/completed
  Maurer--Cartan fork, forced coefficient-one coset return, infinitesimal
  mixed-sign replay, holonomy control, trace-reversed fibre, nested-reduction
  boundary, and datum/nonpromotion plants. Run it with
  `uv run --with sympy python`.
- `channel-swings/pw2a_variational_extension_green_probe.py` checks the
  independent-`B` polynomial comparator's live `D_BK/D_TK` adjoints,
  attainable fourth-order term, derivative-affine order-two control, both
  Green layers, separate nonvacuous Ward comparator, field debit, and
  literal-native boundary. Run it with `uv run --with sympy python`.
- `channel-swings/pw2_full_first_jet_action_graph_probe.py` checks the exact
  source-coordinate obstruction for a projected Maurer--Cartan displacement,
  including the finite `U(2,2)/Sp(1,1)` return, a positive gauge-tangent
  control, live moving-projector derivative, two same-`dT` holonomic germs
  with different `dK`, and the trace-reversed symmetric fibre. Run it with
  `uv run --no-project --no-cache --with sympy -- python`.
- `channel-swings/pw2_symbolic_ad_rank_strata_probe.py` reconciles a frozen
  full-jet polynomial graph under exact symbolic and independent `Fraction`
  dual-number differentiation; verifies the complete differential-operator
  composition; and certifies generic rank one with exceptional locus `V(r)`,
  while planting an `A2 Z0` false positive and missing-term controls. It is a
  structural harness, not a native Shiab coefficient. Run it with
  `uv run --no-project --no-cache --with sympy -- python`.
- `channel-swings/pw1_source_native_real_form_superig_probe.py` checks the
  exact `U(2,2)/Sp(1,1)` reduction model, symmetric-pair bracket laws,
  coset-curvature return, three-patch moving-`J` descent, projector derivative,
  positive-unitary and reality forks, reduced complex Wick comparator,
  full-unitary real-Krein mixed bracket, central complex-channel kill, forced
  one-half algebraic affine representation, independent-Euler logical
  boundary, and carried native `Alt` result. Run it with
  `uv run --with sympy python`.
- `channel-swings/pw1_typed_experiment_selection_probe.py` validates the
  fail-closed candidate/fixture schema, four synthetic response axes, exact
  rational rank-gain selector, content-derived duplicate rejection, visible
  reserved-control separation, frozen selection, exact-replay policy, and
  hostile mutation bank. It is an algorithm scaffold, not a typed oracle. Run
  it with `python`.
- `channel-swings/post_b2c15r3_multidisciplinary_council_scaffold_probe.py`
  validates the post-B2C15R3 council registry: at least ten specialist lenses,
  exactly ten engineering personas, exactly ten dependency-ordered waves,
  explicit information-gain questions and kill routes, Layer-0/lane/datum
  guards, an exact-ending ML pipeline, the PW1/PW2 frontier, and the mandatory
  divergent-pre/hostile-post specialist protocol. It includes live planted
  mutations for false execution, missing personas/waves, forward
  dependencies, absent kill tests, ML-verdict substitution, datum smuggling,
  and nonconjunctive Curt promotion. Run it with `python`.
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

- `channel-swings/eric_curt_wave3d_b2c2b_super_ig_rs_tangent_noether_probe.py`
  is the Wave 3D-B2C2B natural tangent/Noether/observer gate. In the frozen
  metric/Clifford-only first-order class, gamma-tracelessness leaves the unique
  twistor symbol. Its W131 composition fails off shell, and unchanged
  observation sees both its full image and characteristic-exact half. An
  enlarged mixed-carrier super-IG action and Ward identity remain open.
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
| `generation-sector/` (34) | the generation-count core: Krein signature, net chiral index, chirality kills, Wave-A Reading-A kinematic grading, Wave-B hinge-symbol leakage, Wave-C exact Spin(10)/Lambda5/Pati-Salam channels, and Wave-D exact exterior/Sage native-connection placement certificates (paper-cited surface; frozen paths remain frozen), with a local script map and README inventory gate |
| `observable-algebra/` (5) | finite compression-algebra commutant/trichotomy probes plus exact Wave-B compact-isotypic, Sage character, and neutrality certificates; kinematic carrier evidence only, not a physical observable-algebra, quotient, or signature-selection theorem |
| `de-certification/` (6) | Wave-A internal likelihood consistency, proxy shape-inverse witnesses, the finite W230/conditional FLRW mapping fixture, the synthetic-injection pipeline-unbiasedness control (known truths, DR2-covariance noise), and the exact-rational composition-map first-arrow certificate; register status for C10 / M-H13 / native bridge moves only via the register |
| `hardening-pass/` (2) | staged located-not-forced paper-hardening certificates: OQ-RK1 rank and route-(a) classification, with a local direct/independent script map and README inventory gate |
| `source-action/` (12) | the twisted Rarita-Schwinger / source-action gate work (frozen alongside the paper), with a local script map and README inventory gate |
| `gu-independent/` (11) | the GU-independent class-level structural no-go, with a local script map and README inventory gate |
| `hessian-z3/` (9) | Hessian / Z3 carrier-occupancy checks, with a local script map and README inventory gate |
| `forcing-slot/` (8) | the forcing-slot toy stabilized-source test, with a local script map and README inventory gate |
| `carrier-mass/` (8) | the carrier Dirac-mass capstone plus the trace-`q` chiralizer admission screen, with a local script/output map and README inventory gate |
| `carrier-bit-decision/` (13) | the carrier-bit decision campaign: four analysis legs plus independent referees, with a local script/analysis map and README inventory gate |
| `escape-corners/` (16) | the carrier-bit escape-corners campaign: four analysis legs, corner-open audits, independent referees, and checked-in run logs, with a local script/analysis/log map and README inventory gate |
| `anchored-leads/` (7) | the anchored-leads candidate screens, including an independent Jones-index finite-type recheck, with a local script map and README inventory gate |
| `big-swing/` (48) | adversarial big-swing packets for generation-count, boundary, framed-bordism, mirror-sector, and capability-wall leads, with a local script map and README inventory gate |
| `internal-paths/` (4) | internal follow-up path certificates for OQ-RK1 rank, Y14 bundle index pieces, non-compact signed-readout witnesses, and Sp-family anomaly gates, with a local script map and README inventory gate |
| `symbolic-proofs/` (1) | symbolic structure-level certificates for the core theorem package, with a local script map and README inventory gate |
| `decider/` (4) | the single-decider ("only honest computable integer is one"), with a local certificate map and README inventory gate |
| `chase/` (0) | nested MOVE-1..MOVE-5 chase-to-kill verdict scripts, with a local script map and README inventory gate |
| `boundary-eta/` (4) | the boundary eta-invariant / tangential fork, with a local script map, nested independent denominator checks, and README inventory gate |
| `anomaly/` (2) | frontstage anomaly gate validators: the Sp(1) 2-primary Dai-Freed AHSS gate and the conditional-build anomaly-rank probe, with a local script map and README inventory gate |
| `sm-boundary/` (1) | SM-shaped boundary anomaly-inflow toy, with a local script map, nested independent algebraic verifier, and README inventory gate |
| `calm-gw-boundary/` (1) | finite CALM/GW boundary gate for Jordan-component axial-charge monotonicity versus scalar/rounded readout failures, with a local script map and README inventory gate |
| `pati-salam/` (1) | reproduction harness for the active-research Pati-Salam chain verification scripts, with a local harness map and README inventory gate |
| `enum-completeness/` (2) | enumeration-completeness certificate for the located-not-forced publication gate, with a local script map and README inventory gate |
| `antilinear-bound/` (3) | antilinear-bound certificate for the located-not-forced publication gate, with a local script map and README inventory gate |
| `function-space-ext/` (9) | WC-FUNCTION-SPACE-EXT probes plus the signed-readout UII certificate-shape validator: finite Galerkin, conditional section theorem + independent checks, APS eta boundary control, and UII gap gate, with a local script map and README inventory gate |
| `rs-function-space/` (5) | RS function-space family-index scaffolds: K3 pushforward, boundary eta, family/characteristic-class generation-arena probes, order-3 rho certificates, and geometric `-38` adjudication certificates, with a local script map and README inventory gate |
| `channel-swings/` (423 Python + 35 Sage) | active channel and Lane-1 swing probes; the current count includes the K77 minimal edge-mode reduction probe, its independent Sage/QQ replay, and ledger-v0.70 integrity gate. The detailed historical inventory remains represented by the files and per-wave entries above. |
| `recovery-contract/` (22) | recovery-certification branch-local computational checkpoints, including the construction-space GR R0, SM R0, P3 retro-verification, P4 QM checklist, P5 source-object specification, P6 conditional-interior, lattice schema-freeze, and conservative C1 signature-resolution gates; the GR forced-coefficient residual test; GR no-go history/scope defense gates through Swing 3; cosmological field-type/scalar-truncation and no-go defense gates through Swing 3; Standard Model selector and no-go defense gates through Swing 3; and the QM physical-sector conditional sufficiency gate under the frozen action fingerprint |
| `threads/` (18) | frontier A/B/C/D/E thread audits for the current gravity, dark-energy, and source-action-adjacent gates, with a local script map and README inventory gate |
| `hourly-cycles/` (archived off-tree) | **archived** hourly-automation output; not load-bearing |

The latest channel-swing additions are
`selected_k77_coupled_all_grade_upsilon_graph_probe.py` and
`conditional_physics_ledger_v061_probe.py`. They prove the full response has
domain/rank `1470`, output support `4330`, nullity zero, and four unique
conditional all-grade lifts while keeping target derivation, Euler,
preboundary, symplectic, common-domain, odd BV and BFV work open.

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

## K77 Wave 2 moving-defect localization certificate

`channel-swings/k77_wave2_full_source_action_defect_localization_probe.py`
constructs the scalar-coefficient/induced-density localization on an exact
moving graph. It independently checks patch descent across a normal-coordinate
orientation reversal, the field Euler monopole plus graph-mixed normal dipole,
the support-plus-density section-shape derivative, and complete-owner even
gauge/diffeomorphism Ward descent. A source-shaped first-order witness separates
equal zero/tangential jets with unequal normal jets, while fourteen plants
forbid promotion to the actual moving K77 Shiab symbol, a selected
bulk/defect weld, odd super-IG BV, a common domain or physics. Run it with
`PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python
tests/channel-swings/k77_wave2_full_source_action_defect_localization_probe.py`.
## K77 Wave 2 moving-Shiab / epsilon-Ward / Green-domain certificate

`channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py`
implements exact Gaussian-rational real `Cl(7,7)` exterior/Hodge arithmetic,
enumerates all eight source-permitted coefficient product triples, and reports
support, selected-slice rank and full grade-one rank separately. It verifies
the moving-Phi derivative by exact dual numbers, the primitive epsilon chain,
complete off-shell homogeneous even Ward owner cancellation, and the
Dirichlet versus preboundary Green identity at the `H10 -> H9` trace grade.
Nine plants prevent selector, support/rank, owner, domain, datum and physics
promotion. Run it with `uv run --with sympy==1.14.0 python
tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py`.

## K77 Wave 2 principal-Bianchi product-selector certificate

`channel-swings/k77_wave2_principal_bianchi_product_selector_probe.py`
constructs the complete rank-91 algebraic-Riemann differential-Bianchi
principal carrier for positive, negative and null `Spin(7,7)` covectors and
tests all eight fixed displayed product assignments. Bianchi has defect rank
one and leaves four rows; the nonvacuity gate rejects three zero Riemann maps,
selecting `comm/symi/symi`. The selected map is exactly `-2` times the ambient
fourteen-dimensional Einstein contraction and kills Weyl. A separate Sage
file rebuilds the exact Clifford/exterior calculation without importing the
Python implementation. Six plants forbid zero-map, sample-jet, continuous-
uniqueness, full-functor, physics and datum promotion. Run:
`uv run --with sympy==1.14.0 python
tests/channel-swings/k77_wave2_principal_bianchi_product_selector_probe.py`
and `sage
tests/channel-swings/k77_wave2_principal_bianchi_product_selector_independent.sage`.

## K77 Wave 2 eddy / augmented-torsion Euler prolongation certificate

`channel-swings/k77_wave2_eddy_augmented_torsion_euler_prolongation_probe.py`
reconstructs the source's `1/2,1/3` path-average curvature, replays the K77-B3
printed-endpoint obstruction, and builds the action-owned Fréchet-adjoint
Euler formula. It keeps the printed endpoint as a rival and computes its
degree-14 rank 13 on complete rank-182 grade-one generic-adjoint carriers,
while the Riemann subcarrier remains closed. It does not transfer that rank to
the action Euler and retains the raw northeast block without assigning it to
stress-energy. Independent Sage rebuilds only the printed-rival Clifford ranks
and identity-Shiab transgression coefficients. Run:
`PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python
tests/channel-swings/k77_wave2_eddy_augmented_torsion_euler_prolongation_probe.py`
and `sage
tests/channel-swings/k77_wave2_eddy_augmented_torsion_euler_prolongation_independent.sage`.

## K77 Wave 2 action degree-14 / northeast certificate

`channel-swings/k77_wave2_action_owned_degree14_northeast_probe.py`
constructs the exact formal adjoint of the selected `comm/symi/symi` Shiab on
all `8,281` tested `Omega2 tensor Cl2` inputs, with rank `1,197` split into
`Cl1/Cl5` ranks `196/1,001`. It types the full even Noether totalization,
proves the raw northeast map rank-`8,281` injective, and kills direct
`J_D+J_F` ownership. The minimal pure-trace degree-three candidates collapse
all positive, negative and null rank-91 Riemann banks to ranks `0/1` and erase
traceless Ricci. Independent Sage certifies raw injectivity, the three orbit
banks, and a Gaussian-rational adjoint slice without importing the Python
probe. Run:
`uv run --cache-dir /private/tmp/gu-k77-action-uv-cache --with sympy==1.14.0
python tests/channel-swings/k77_wave2_action_owned_degree14_northeast_probe.py`
and `sage
tests/channel-swings/k77_wave2_action_owned_degree14_northeast_independent.sage`.

## Dynamic cosmological-sector constraint-rank and ledger certificates

`channel-swings/dynamic_cosmological_sector_constraint_rank_probe.sage`
separates an independent equality of two field values from a definition, a
Ward/Bianchi-dependent copy, a relation with a free gain and an unscreened
vacuum-energy shift. It also gives an exact spatially-flat de Sitter witness
with nonzero four-dimensional curvature. It passes 21 exact/type/planted
checks without claiming a native action-parameter reduction.

`channel-swings/conditional_physics_ledger_v03_probe.py` freezes ledger v0.2,
recomputes the 82-row active denominator and checks the five-way `LT-GR2`
split, source return, current-build collision, Weinberg horn typing and both
hostile-review charges. Run:

```sh
sage tests/channel-swings/dynamic_cosmological_sector_constraint_rank_probe.sage
python3 tests/channel-swings/conditional_physics_ledger_v03_probe.py
```

## Source-native curvature/VEV Euler-rank and ledger v0.4 certificates

`channel-swings/source_native_curvature_vev_euler_rank_probe.py` types the
source distortion as the action's two-connection difference, varies `B` and
`T` independently, and computes the complete homogeneous value ranks. It
separates ambient curvature covariation rank 105 from total `T`-Euler rank 196
and its 91 `T`-only rows, retains the rank-10 observed post-Shiab kernel
obstruction without using it circularly against the complete moving geometry,
marks native BV quotient rank undefined, and shows an independent vacuum shift
is tracked rather than screened. Nine plants prevent ambient/observed,
rank/support, action/density, BV and magnitude promotions. Independent Sage
rebuilds the QQ ranks and scalar ambient-kernel witness.

`channel-swings/conditional_physics_ledger_v04_probe.py` freezes v0.3,
recomputes the unchanged denominator and verdict counts, checks only
`LT-GR2b/c/d` migrated, validates the new
`PROVEN_UNABLE_BY_CURRENT_ACTION` kind, and enforces the circularity, quotient
and hostile-review fences. Run:

```sh
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/source_native_curvature_vev_euler_rank_probe.py
DOT_SAGE=/private/tmp/gu-source-native-sage \
  /Applications/SageMath-10-9.app/Contents/Frameworks/Sage.framework/Versions/Current/venv/bin/sage \
  tests/channel-swings/source_native_curvature_vev_euler_rank_independent.sage
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/conditional_physics_ledger_v04_probe.py
```

## Pre-Shiab defect-action/BV symbol and ledger v0.5 certificates

`channel-swings/pre_shiab_gauss_defect_action_bv_symbol_probe.py` proves the
scoped current-`I1B` `T=0` ownership obstruction, selects the unique
five-coefficient Einstein line through Ward/Bianchi constraints, retains the
trace-reversed `(6,4)` pairing, and constructs the exact non-null
`4 -> 20 -> 20 -> 4` even-BV symbol complex. Zero-gain and null controls keep
the accidental and characteristic kernels visible. The independent Sage/QQ
script rebuilds the same ranks and identities.

`channel-swings/conditional_physics_ledger_v05_probe.py` freezes v0.4,
requires only `LT-GR2c` to migrate, preserves all verdict and global-residue
counts, and permits one ranked conditional local quotient without promoting
the missing global soldering map, nonlinear weld or null domain. Run:

```sh
uv run --with sympy==1.14.0 python \
  tests/channel-swings/pre_shiab_gauss_defect_action_bv_symbol_probe.py
DOT_SAGE=/private/tmp/gu-pre-shiab-bv-sage \
  /Applications/SageMath-10-9.app/Contents/Frameworks/Sage.framework/Versions/Current/venv/bin/sage \
  tests/channel-swings/pre_shiab_gauss_defect_action_bv_symbol_independent.sage
python3 tests/channel-swings/conditional_physics_ledger_v05_probe.py
```

## K77 epsilon gravitational receiver, same-stratum weld and ledger v0.6

`channel-swings/k77_epsilon_gravitational_soldering_weld_probe.py` uses the
faithful real 128-dimensional K77 Clifford representation to construct the
moving grade-one receiver, exact rank-ten right inverse/projector and
Krein-DeWitt action split. It separately proves that five Lorentz-equivariant
`Sym2 x Sym2 -> Sym2` maps survive, so equivariance is not uniqueness, and
keeps bulk/defect support plus nonlinear BV open. The independent Sage/QQ
script reconstructs the receiver, projector, action identities and five-map
lower bound. The v0.6 ledger probe preserves v0.5 byte-for-byte and moves only
`LT-GR2c`. Run:

```sh
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/k77_epsilon_gravitational_soldering_weld_probe.py
DOT_SAGE=/private/tmp/gu-k77-epsilon-weld-sage \
  /Applications/SageMath-10-9.app/Contents/Frameworks/Sage.framework/Versions/Current/venv/bin/sage \
  tests/channel-swings/k77_epsilon_gravitational_soldering_weld_independent.sage
python3 tests/channel-swings/conditional_physics_ledger_v06_probe.py
```

## K77 global chimeric spin reduction, support horn and ledger v0.7

`channel-swings/k77_global_chimeric_spin_reduction_probe.py` checks the K77
characteristic classes, induced spin lift, real/Krein Clifford carrier, global
full labelled `gamma_epsilon` frame, inherited rank-ten receiver and the
profile-free bulk-plus-independent-`X` support horn. It fences the unresolved
`lambda_def` alias and nonlinear/null-domain work. The independent Sage script
rebuilds the characteristic-class, signature and rank checks. The v0.7 ledger
probe freezes v0.6 byte-for-byte and moves only `LT-GR2c`. Run:

```sh
uv run --with numpy --with sympy python \
  tests/channel-swings/k77_global_chimeric_spin_reduction_probe.py
sage tests/channel-swings/k77_global_chimeric_spin_reduction_independent.sage
python3 tests/channel-swings/conditional_physics_ledger_v07_probe.py
```

## K77 formal homogeneous-gauge BV, null quotient, defect Green domain and ledger v0.8

`channel-swings/k77_global_even_bv_null_green_domain_probe.py` composes the
global frame, moving Shiab, primitive epsilon and full homogeneous Ward owner;
checks the formal minimal homogeneous-gauge CME hypotheses on a nonabelian
control; and proves the null `10 -> 6 -> 2` constraint/gauge quotient with
explicit plus/cross representatives. It fences the Green result to the flat
globally hyperbolic defect (or a separately proved normally-hyperbolic curved
completion), charges `lambda_def` as the 84th prequotient real and leaves the
global coupled `Y14` domain open. The independent Sage/QQ script reconstructs
the null and Lie-algebra results. The v0.8 ledger probe freezes v0.7 and moves
only `LT-GR2c`. Run:

```sh
sage -python tests/channel-swings/k77_global_even_bv_null_green_domain_probe.py
sage tests/channel-swings/k77_global_even_bv_null_green_domain_independent.sage
python3 tests/channel-swings/conditional_physics_ledger_v08_probe.py
```

## K77 moving observation, ambient-domain obstruction and ledger v0.9

`channel-swings/k77_moving_observation_y14_domain_obstruction_probe.py`
constructs the complete first-jet moving-section map and equation dual, proves
section-germ no-leakage, kills value-only and finite-jet global-shell
promotion, computes the `(6,7)`, `(7,6)` and `(6,6,1)` induced hypersurface
inertias, and types the conditional observed curvature/distortion equation.
The independent Sage/QQ script rebuilds the jet inverse and signature result.
The v0.9 ledger probe freezes v0.8, migrates exactly four distances and
preserves coverage, verdict counts, residue, plus/cross and all no-promotion
fences. Run:

```sh
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/k77_moving_observation_y14_domain_obstruction_probe.py
DOT_SAGE=/private/tmp/gu-k77-observation-y14-sage \
  /Applications/SageMath-10-9.app/Contents/Frameworks/Sage.framework/Versions/Current/venv/bin/sage \
  tests/channel-swings/k77_moving_observation_y14_domain_obstruction_independent.sage
python3 tests/channel-swings/conditional_physics_ledger_v09_probe.py
```

## Action-owned stress, observed propagator and ledger v0.10

`channel-swings/observed_upback_stress_normal_constraint_vacuum_probe.py`
proves the general radial reconstruction of Hilbert stress from the common
action's existing mixed return block, checks an exact Krein-Dirac plane wave,
replays the flat observed null quotient and computes the repaired TT field
matrix. Its determinant is `-z^2`, so the metric response is double-pole even
though plus/cross survive. The quadratic-vacuum fixture has inertia `(6,4)`
and tracks independent shifts; it explicitly leaves the existing full
nonlinear `T`-cubic vacuum open. The independent Sage/QQ script rebuilds the
linear algebra, and the v0.10 ledger probe freezes v0.9 and requires exactly
five scoped migrations. Run:

```sh
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/observed_upback_stress_normal_constraint_vacuum_probe.py
DOT_SAGE=/private/tmp/gu-observed-upback-sage \
  /Applications/SageMath-10-9.app/Contents/Frameworks/Sage.framework/Versions/Current/venv/bin/sage \
  tests/channel-swings/observed_upback_stress_normal_constraint_vacuum_independent.sage
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/conditional_physics_ledger_v010_probe.py
```

## Full-norm pole split, nonlinear cyclic control and ledger v0.11

`channel-swings/full_norm_pole_split_nonlinear_t_vacuum_probe.py` composes the
existing Gauss-induced full-`|II|^2` horn with the action-owned mixed gravity
placement. The exact TT response has determinant
`z*(alpha_II*kappa_1-z)`, hence one simple massless Einstein pole and one
distinct simple massive GU partner; setting `alpha_II=0` restores the
predecessor's coincident double pole. The same probe solves the full finite
noncommutative cyclic transgression, finding two genuinely nonlinear real
stationary branches and proving both are nondegenerate saddles. The Sage/AA
control independently reconstructs the factorization, root count, resultants
and Hessian inertia. The v0.11 ledger probe freezes v0.10, migrates exactly
seven distances, leaves P2 source-silent, and does not identify the cyclic
control with the selected moving-K77 vacuum. Run:

```sh
env UV_CACHE_DIR=/tmp/gu-uv-cache uv run --with sympy==1.14.0 python \
  tests/channel-swings/full_norm_pole_split_nonlinear_t_vacuum_probe.py
sage tests/channel-swings/full_norm_pole_split_nonlinear_t_vacuum_independent.sage
python3 tests/channel-swings/conditional_physics_ledger_v011_probe.py
```

## Selected K77 algebraic branch, canonical Gauss full-II norm and ledger v0.12

`channel-swings/selected_moving_k77_vacuum_p2_norm_probe.py` constructs the
correct horizontal Gauss receiver from `Sym2(H*) tensor V` into the
off-diagonal `so(H plus V)` connection block. It proves rank 100, exact
right-inverse and action-orthogonal projector identities, full-II quadratic
rank 100 versus trace-first rank ten, and zero new fields/data/fitted
coefficients. The same packet differentiates the selected non-cyclic K77
scalar action directly, including the one-third eddy, and verifies the exact
nonzero algebraic branch `t=-kappa_1/312`, all 392 invariant translation
directions, the moving-epsilon orbit and radial Hessian `-14*kappa_1`. The
Sage control independently rebuilds both Clifford/exterior arithmetic and the
Gauss linear algebra. The v0.12 ledger probe freezes v0.11, migrates exactly
seven rows, moves `LT-GR1` to `SAME/DERIVED_CONDITIONAL`, retires one fork and
keeps physical stability, totalization/current closure, common domain and
external `P2_datum` open. Run:

```sh
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_moving_k77_vacuum_p2_norm_probe.py
DOT_SAGE=/private/tmp/gu-selected-k77-vacuum-p2-sage \
  /Applications/SageMath-10-9.app/Contents/Frameworks/Sage.framework/Versions/Current/venv/bin/sage \
  tests/channel-swings/selected_moving_k77_vacuum_p2_norm_independent.sage
python3 tests/channel-swings/conditional_physics_ledger_v012_probe.py
```

## Selected-branch Gauss Hessian, totalization/current and ledger v0.13

`channel-swings/selected_branch_linearized_totalization_domain_probe.py`
differentiates the selected action on the actual gravitational Gauss carrier.
It obtains trace/traceless coefficients `100*kappa_1/117` and
`124*kappa_1/117`, types the direct-plus-soldered one-action chain, constructs
the common coupled observed defect Krein/Green domain and records exact
opposite residues for the massless pole and GU partner. The independent Sage
route rebuilds the Clifford-one and Gauss spectra without importing the Python
probe. The v0.13 ledger probe freezes v0.12 and migrates exactly seven rows
while physical BV cohomology, ambient `Y14` domain, full metric/coframe
soldering and two-field curvature/VEV cosmology remain open. Run:

```sh
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_branch_linearized_totalization_domain_probe.py
DOT_SAGE=/private/tmp/gu-selected-branch-totalization-sage \
  /Applications/SageMath-10-9.app/Contents/Frameworks/Sage.framework/Versions/Current/venv/bin/sage \
  tests/channel-swings/selected_branch_linearized_totalization_domain_independent.sage
python3 tests/channel-swings/conditional_physics_ledger_v013_probe.py
```

## Selected-branch metric soldering, even BV, Krein grade and ledger v0.14

`channel-swings/selected_branch_bv_tt_curvature_vev_flrw_probe.py` computes
the gauge-rotated Levi-Civita metric derivative modulo connection gauge on all
three covector orbit types, the massive TT quotient lower bound, the canonical
finite spectral Krein majorant, and the local curvature/VEV parameter and
vacuum-shift responses. The independent Sage route rebuilds the three core
linear-algebra and scalar formulas over exact arithmetic. The v0.14 ledger
probe freezes v0.13 and migrates exactly eight rows while retaining the full
nonlinear ambient, odd super-IG, loop/UV and ambient/global cosmology fences.
Run:

```sh
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_branch_bv_tt_curvature_vev_flrw_probe.py
DOT_SAGE=/private/tmp/gu-selected-branch-bv-flrw-sage \
  /Applications/SageMath-10-9.app/Contents/Frameworks/Sage.framework/Versions/Current/venv/bin/sage \
  tests/channel-swings/selected_branch_bv_tt_curvature_vev_flrw_independent.sage
python3 tests/channel-swings/conditional_physics_ledger_v014_probe.py
```
## First-interaction Krein, global zero mode and ledger v0.15

`channel-swings/first_interaction_krein_global_zero_mode_probe.py` rechecks
the exact free TT involution, expands the action-owned `theta h^2` vertex in
its mass-parity eigenbasis and proves that neither scalar sign preserves all
monomials. It then proves the constant-mode theorem for finite local
derivative polynomials and constructs the unique normalized invariant
rank-one projector on a finite connected transitive control, whose complement
screens independent constant shifts. Ten plants catch term truncation,
unnormalized/non-self-adjoint averages, disconnected zero modes, tracking-
as-screening and P2/source overclaims. The independent Sage route rebuilds the
parity and projector algebra exactly. The v0.15 ledger probe freezes v0.14 and
migrates exactly six rows while preserving counts and residue. Run:

```sh
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/first_interaction_krein_global_zero_mode_probe.py
DOT_SAGE=/private/tmp/gu-interaction-zero-mode-sage \
  /Applications/SageMath-10-9.app/Contents/Frameworks/Sage.framework/Versions/Current/venv/bin/sage \
  tests/channel-swings/first_interaction_krein_global_zero_mode_independent.sage
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/conditional_physics_ledger_v015_probe.py
```

## First perturbative background C and ledger v0.16

`channel-swings/first_perturbative_background_c_operator_probe.py` derives
the fixed-background Hessian of the first owned cubic, constructs the exact
free-connected positive spectral fundamental symmetry and verifies the
rank-four unique first correction. It classifies generic Jordan walls, a
complex-spectrum interval, a disconnected real branch with opposite positive
orientation and a scalar nonselection collision. Twelve plants enforce its
fixed-background/two-field scope. The independent Sage route reconstructs the
algebra and v0.16 freezes v0.15 while migrating exactly four rows. Run:

```sh
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/first_perturbative_background_c_operator_probe.py
DOT_SAGE=/private/tmp/gu-first-background-c-sage \
  /Applications/SageMath-10-9.app/Contents/Frameworks/Sage.framework/Versions/Current/venv/bin/sage \
  tests/channel-swings/first_perturbative_background_c_operator_independent.sage
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/conditional_physics_ledger_v016_probe.py
```

## Selected-cubic QFT threshold, numerator gate and ledger v0.17

`channel-swings/selected_cubic_qft_threshold_numerator_probe.py` computes the
complete three-field cubic Hessian, both scalar-parity monomial banks, the
selected scalar/TT mass ratio and the exact heavier-to-lighter-plus-massless
shells. Its numerator-divisibility control forbids booking a Q1 pole from a
denominator zero alone. Thirteen plants catch term omission, discrete-to-
continuum import, scalar/spin-two conflation, soft-boundary overclaim and
state-space promotion. The symplectic hostile check additionally rejects an
unreduced cubic density as a physical transition until it descends through the
presymplectic quotient. Sage reconstructs the algebra independently; v0.17
freezes v0.16 and migrates exactly four rows. Run:

```sh
uv run --cache-dir /private/tmp/gu-selected-cubic-qft-uv-cache \
  --with sympy==1.14.0 python \
  tests/channel-swings/selected_cubic_qft_threshold_numerator_probe.py
sage tests/channel-swings/selected_cubic_qft_threshold_numerator_independent.sage
python3 tests/channel-swings/conditional_physics_ledger_v017_probe.py
```

## Selected-cubic reduced numerator, completion fork and ledger v0.18

`channel-swings/selected_cubic_reduced_numerator_probe.py` reconstructs the
full free `(h,v)` pencil, its massless/massive external legs and Krein norms.
It proves the compact-core `theta-q0-q0` bulk numerator is shell-zero and
exhibits exact `hh`-only and full-pencil field-redefinition completions that
share the inherited constant-background `hh` block but give nonzero and zero
mixed shell classes. A symplectic comparator separates a nonzero Hamiltonian
vector field from an EOM-exact zero while keeping the unrestricted
preboundary/BFV phase space open. Sage independently reconstructs the fork;
v0.18 preserves the denominator/counts/residue and migrates four rows. Run:

```sh
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_cubic_reduced_numerator_probe.py
DOT_SAGE=/private/tmp/gu-selected-cubic-reduced-numerator-sage \
  /Applications/SageMath-10-9.app/Contents/Frameworks/Sage.framework/Versions/Current/venv/bin/sage \
  tests/channel-swings/selected_cubic_reduced_numerator_independent.sage
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/conditional_physics_ledger_v018_probe.py
```

## Selected-action grade-one Schur, observation and ledger v0.36

`channel-swings/selected_action_grade1_dbt_schur_observation_probe.py`
constructs the complete 196-dimensional grade-one invariant Hessian and
inverse, the corrected curvature-plus-`d_B T` source cross, its Ward-exact
Schur form and horizontal/vertical observation ranks. The default exact run
is analytic; `--exhaustive` additionally checks all `196^2` selected-Hessian
entries. The independent Sage audit factors the timelike, spacelike and null
quotient pencils and checks the N1/N2 algebraic kernels. The ledger probe
freezes v0.35, migrates exactly five rows and requires the `LT-GR1` verdict
retraction without residue, quotient or datum promotion. Run:

```sh
uv run --cache-dir /private/tmp/gu-grade1-schur-uv-cache \
  --with-requirements requirements.txt python -B \
  tests/channel-swings/selected_action_grade1_dbt_schur_observation_probe.py
sage -python tests/channel-swings/selected_action_grade1_dbt_schur_observation_independent.sage
python3 tests/channel-swings/conditional_physics_ledger_v036_probe.py
```

## Selected-action N2 little-group, Green flux and ledger v0.37

`channel-swings/selected_action_n2_null_little_group_green_probe.sage`
reconstructs the completed null source symbol through a low-memory exact path,
descends the transverse rotation through the N2 gauge quotient and proves that
the two extra modes have helicity `±1`, not `±2`. It also differentiates the
mixed-order Schur pencil with exact degree-four Lagrange weights and verifies a
rank-two definite gauge-descending local principal Green flux. The ledger
probe freezes v0.36, migrates exactly six distances and makes the distinct
second-layer I2B/observer-full-II owner map primary without changing verdicts,
residue, quotients or external datum. Run:

```sh
sage -python tests/channel-swings/selected_action_n2_null_little_group_green_probe.sage
python3 tests/channel-swings/conditional_physics_ledger_v037_probe.py
```

## Selected second-layer I2B/Gauss owner map and ledger v0.38

`channel-swings/selected_second_layer_i2b_gauss_owner_map_probe.py` constructs
the exact Gauss insertion into the complete `Cl2` residual carrier, computes
the rank-100 projected quadratic form and inertia, and exhibits an exact
`2/39` leakage into an orthogonal vertical/normal-bivector direction. The
ledger probe freezes v0.37 and migrates exactly five distances while keeping
all headline counts and external data fixed. Run:

```sh
uv run --with sympy==1.14.0 python tests/channel-swings/selected_second_layer_i2b_gauss_owner_map_probe.py
python3 tests/channel-swings/conditional_physics_ledger_v038_probe.py
```

## Selected second-layer full-Cl2 pullback and ledger v0.39

`channel-swings/selected_second_layer_full_cl2_residual_pullback_probe.py`
derives the sparse stabilizer-block formula, exhaustively checks all
`1,274 x 100` coefficients, computes the full-II plus trace-square Gram form
and verifies stationary co-moving cancellation. The ledger probe freezes
v0.38 and migrates exactly five distances without changing headline counts.

```sh
uv run --with sympy==1.14.0 python tests/channel-swings/selected_second_layer_full_cl2_residual_pullback_probe.py
python3 tests/channel-swings/conditional_physics_ledger_v039_probe.py
```

## Selected second-layer TT Euler, preboundary, helicity and ledger v0.40

`channel-swings/selected_second_layer_tt_euler_preboundary_helicity_probe.py`
composes the complete selected-`Cl2` coefficients with the exact Gauss/TT
normalization, derives the non-fitted fourth-order Euler polynomial and Green
identity, and proves the massless plus/cross quotient has compact null-rotation
polynomial `x^2+4`; the massive TT plane is only axial weight two until its
full `SO(3)` type is constructed. The ledger probe freezes v0.39, migrates exactly four row
distances and retains all headline counts, four scoped quotients and unused
P1/P2/P3.

```sh
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_second_layer_tt_euler_preboundary_helicity_probe.py
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/conditional_physics_ledger_v040_probe.py
```

## Selected second-layer off-TT scalar/Ward owner and ledger v0.42

`channel-swings/selected_second_layer_offtt_scalar_ward_owner_probe.py`
constructs the exact metric-to-full-II tangent, reproduces the selected TT
polynomial, and proves the isolated metric block has Ward-defect rank four and
no full characteristic root at the restricted scalar candidate. The ledger
probe freezes v0.41, migrates exactly five distances/priorities, preserves all
headline counts and requires the full co-moving action owner.

```sh
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_second_layer_offtt_scalar_ward_owner_probe.py
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/conditional_physics_ledger_v042_probe.py
```

## Selected second-layer massive SO3 closure and ledger v0.41

`channel-swings/selected_second_layer_massive_so3_closure_probe.py` constructs
the exact massive rest-frame diffeomorphism quotient, closes the axial
plus/cross plane under all three spatial rotations, proves the resulting
five-dimensional carrier has spin-two Casimir `-6`, and isolates the one
spin-zero complement. Two exact covariant Hessians agree on the complete
spin-two carrier and disagree on the scalar pole, proving the TT-to-scalar
identifiability boundary. The ledger probe freezes v0.40, migrates exactly
five distances/priorities and retains all headline counts, four scoped
quotients and unused P1/P2/P3.

```sh
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_second_layer_massive_so3_closure_probe.py
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/conditional_physics_ledger_v041_probe.py
```

## Selected second-layer D Upsilon gauge-orbit weld and ledger v0.43

`channel-swings/selected_second_layer_dupsilon_gauge_orbit_weld_probe.py`
replays the independent rank-four metric Ward load and source-native
connection diffeomorphism orbit, proves the forced response rank and constructs
the unique diagnostic weld on that orbit. It plants failures against treating
that weld as the actual action derivative or extending uniqueness to the other
twelve connection directions. The ledger probe migrates exactly five rows
without changing headline counts, residue, four scoped quotients or P1/P2/P3.

```sh
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_second_layer_dupsilon_gauge_orbit_weld_probe.py
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/conditional_physics_ledger_v043_probe.py
```

## Selected second-layer actual source-lift rank mismatch and ledger v0.44

`channel-swings/selected_second_layer_actual_source_lift_rank_mismatch_probe.py`
replays the v0.43 proxy and the source-native `(g,varpi)` lift, proves that the
actual independent connection component has rank three with time-direction
kernel, and verifies the rank-four metric Ward load is nonzero there. It kills
only connection-only cancellation at the current principal grade. The ledger
probe migrates exactly five rows without changing headline counts, residue,
four scoped quotients or P1/P2/P3.

```sh
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_second_layer_actual_source_lift_rank_mismatch_probe.py
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/conditional_physics_ledger_v044_probe.py
```

## Selected second-layer observation-owner retype and ledger v0.45

`channel-swings/selected_second_layer_observation_owner_retype_probe.py`
composes the v0.44 rank mismatch with the exact observation theorem. It proves
that metric and graph-section motion share one rank-four tangent, that an
invertible observation receiver preserves the Ward rank, and that a dependent
moving-section normal-jet term remains live but is not identifiable from the
on-section full-`II` pullback. The ledger probe migrates exactly five rows
without changing headline counts, residue, four scoped quotients or P1/P2/P3.

```sh
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_second_layer_observation_owner_retype_probe.py
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/conditional_physics_ledger_v045_probe.py
```

## Selected second-layer normal-jet carrier compatibility and ledger v0.46

`channel-swings/selected_second_layer_normal_jet_carrier_compatibility_probe.py`
rejects the background-subtracted residual-Gram identification and proves all
four raw graph-orbit corrections are expressible in the exact source-native
mixed-normal carrier. The ledger probe migrates exactly five rows while
freezing headline counts, residue, four scoped quotients and P1/P2/P3.

```sh
UV_CACHE_DIR=/private/tmp/gu-uv-cache uv run --with sympy==1.14.0 python \
  tests/channel-swings/selected_second_layer_normal_jet_carrier_compatibility_probe.py
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/conditional_physics_ledger_v046_probe.py
```

## Selected second-layer Shiab inverse/Bianchi completion and ledger v0.47

`channel-swings/selected_second_layer_shiab_inverse_bianchi_completion_probe.py`
constructs the full selected Hodge-Shiab map, proves exact rank 1,274, solves
the four correction preimages uniquely and proves all four principal
`q wedge F` maps have rank fourteen. The ledger probe migrates exactly five
rows while freezing headline counts, residue, four scoped quotients and
P1/P2/P3.

```sh
UV_CACHE_DIR=/private/tmp/gu-uv-cache uv run --with sympy==1.14.0 python \
  tests/channel-swings/selected_second_layer_shiab_inverse_bianchi_completion_probe.py
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/conditional_physics_ledger_v047_probe.py
```

## K77 labelled-null observation-jet Euler/preboundary sufficiency and ledger v0.62

`channel-swings/selected_k77_observation_jet_euler_preboundary_sufficiency_probe.py`
recomputes the exact full response at the retained labelled null covector,
constructs one conormal graph derivative and measures the rank-650 source
principal symbol without promoting it to a Green or symplectic current. The
ledger probe migrates exactly five rows while freezing verdicts, residue, four
scoped quotients and P1/P2/P3.

```sh
uv run --with sympy==1.14.0 --with numpy python \
  tests/channel-swings/selected_k77_observation_jet_euler_preboundary_sufficiency_probe.py
python3 tests/channel-swings/conditional_physics_ledger_v062_probe.py
```

## K77 paired Upsilon/Xi, formal Green owner and ledger v0.63

`channel-swings/selected_k77_paired_upsilon_xi_green_probe.py` corrects the
graph target to a primalized degree-one form, restores the source
degree-thirteen density before applying `D`, verifies printed Xi supports
`16,15,11,11` and rank-zero dependence after total closure, and supplies an
exact formal covariant Green comparator. The ledger probe migrates five rows
without moving verdicts, residue, quotients or P1/P2/P3.

```sh
uv run --with sympy==1.14.0 --with numpy python -u \
  tests/channel-swings/selected_k77_paired_upsilon_xi_green_probe.py
python3 tests/channel-swings/conditional_physics_ledger_v063_probe.py
```

## K77 action-owned degree-fourteen companion and ledger v0.64

`channel-swings/selected_k77_action_owned_degree14_companion_probe.py`
differentiates every connection entry in an exact noncyclic action fixture,
derives `D_B^!(E_B-E_T)+(D_epsilon S)^!K_S`, and rejects deleting either
Euler owner, moving Shiab, or substituting naive `D_A E_T`. The ledger probe
migrates five rows without moving verdicts, residue, quotients or P1/P2/P3.

```sh
uv run --with sympy==1.14.0 --with numpy python -u \
  tests/channel-swings/selected_k77_action_owned_degree14_companion_probe.py
python3 tests/channel-swings/conditional_physics_ledger_v064_probe.py
```

## K77 moving action-Green receiver and ledger v0.65

`channel-swings/selected_k77_moving_action_green_receiver_probe.py` tensors
the exact action coefficient fixture with the moving indefinite primalizer and
complete observation germ. It verifies the four-term moving derivative,
degree-fourteen inverse-density response and nonzero-flux Green identity, with
firing frozen-factor controls and retained ordinary-pullback conormal loss.
The ledger probe migrates five rows without moving verdicts, residue, quotients
or P1/P2/P3.

```sh
uv run --with sympy==1.14.0 --with numpy python -u \
  tests/channel-swings/selected_k77_moving_action_green_receiver_probe.py
python3 tests/channel-swings/conditional_physics_ledger_v065_probe.py
```

## K77 selected-action normal Euler mixed Hessian and ledger v0.66

`channel-swings/selected_k77_source_native_normal_euler_jet_probe.py`
derives the normal connection/epsilon Euler packet as the mixed action Hessian
on every exact field direction. Seven moving owner classes are independently
live and exhaustive; the printed residual normal jet is rejected as a
substitute, and the explicit packet inserts losslessly into the complete
germ. The independent Sage/QQ replay reproduces the normal matrices and owner
sum. The ledger probe migrates five rows without moving verdicts, residue,
quotients or P1/P2/P3.

```sh
uv run --with sympy==1.14.0 --with numpy --with scipy python -u \
  tests/channel-swings/selected_k77_source_native_normal_euler_jet_probe.py
sage tests/channel-swings/selected_k77_source_native_normal_euler_jet_independent.sage
python3 tests/channel-swings/conditional_physics_ledger_v066_probe.py
```

## K77 full normal geometry and owner-split correction ledger v0.67

`channel-swings/selected_k77_full_normal_owner_bank_probe.py` constructs all
ten trace-reversed DeWitt/gimmel normal derivatives, their density, pairing and
Hodge banks, and proves exact fixed-frame/co-moving-frame transport of the
total covector. The firing counterexample shows that the seven v0.66 owner
buckets are trivialization-dependent even though the total mixed Hessian is
intrinsic. The independent Sage/QQ replay verifies signature, ranks and
transport. The ledger probe migrates five distances without moving verdicts,
residue, quotients or P1/P2/P3.

```sh
uv run --with sympy==1.14.0 --with numpy==2.3.2 python -u \
  tests/channel-swings/selected_k77_full_normal_owner_bank_probe.py
sage tests/channel-swings/selected_k77_full_normal_owner_bank_independent.sage
python3 tests/channel-swings/conditional_physics_ledger_v067_probe.py
```

## K77 Green-potential point-splitting basicness ledger v0.68

`channel-swings/selected_k77_green_potential_splitting_basicness_probe.py`
proves exact nonlinear cotangent naturality of the complete Green potential,
exact transport of its field-space exterior derivative, and a three-splitting
cocycle. All ten actual K77 normal directions have nonzero induced normal/base
momentum corrections. The firing partial-potential control shows why freezing
those momenta gives a real defect. The result therefore retires a vertical
B/T lift only for point-trivialization descent; derivative-dependent contact
transformations, physical gauge basicness, polarization, common domain and
BV/BFV remain open. The independent Sage/QQ replay verifies the cotangent and
symplectic identities. The ledger probe migrates five distances without
moving verdicts, residue, quotients or P1/P2/P3.

```sh
uv run --with sympy==1.14.0 --with numpy==2.3.2 python -u \
  tests/channel-swings/selected_k77_green_potential_splitting_basicness_probe.py
sage tests/channel-swings/selected_k77_green_potential_splitting_basicness_independent.sage
python3 tests/channel-swings/conditional_physics_ledger_v068_probe.py
```

## K77 contact-presymplectic gauge basicness ledger v0.69

`channel-swings/selected_k77_contact_presymplectic_gauge_basicness_probe.py`
assembles the actual rank-ten Levi-Civita contact block and complete
observation dual, proves diagonal two-connection Ward closure, and separates
small/Dirichlet gauge from charged boundary symmetry. The presymplectic form
is invariant and horizontal for small gauge; unrestricted contraction is the
field-space derivative of a nonzero moment map in all ten K77 normal
directions. The independent Sage/QQ replay verifies the contact, Ward and
boundary-charge identities. The ledger probe migrates five distances without
moving verdicts, residue, quotients or P1/P2/P3.

```sh
uv run --with sympy==1.14.0 python -u \
  tests/channel-swings/selected_k77_contact_presymplectic_gauge_basicness_probe.py
sage tests/channel-swings/selected_k77_contact_presymplectic_gauge_basicness_independent.sage
python3 tests/channel-swings/conditional_physics_ledger_v069_probe.py
```

## K77 minimal edge-mode reduction ledger v0.70

`channel-swings/selected_k77_minimal_edge_mode_reduction_probe.py` proves that
an ordinary scalar boundary counterterm cannot change the presymplectic form,
types the unselected Dirichlet and zero-charge horns, and constructs the unique
two-cell edge extension. Across all ten nonzero K77 normal weights its extended
dimension/rank/kernel are `60/40/20`; the conditional quotient has
dimension/rank `40/40`. The independent Sage/QQ route checks coefficients,
kernel, ranks and counterterm control. The ledger gate adds one scoped quotient
without moving verdicts, global residue or P1/P2/P3.

```sh
uv run --with sympy==1.14.0 --with numpy python -u \
  tests/channel-swings/selected_k77_minimal_edge_mode_reduction_probe.py
sage tests/channel-swings/selected_k77_minimal_edge_mode_reduction_independent.sage
python3 tests/channel-swings/conditional_physics_ledger_v070_probe.py
```
