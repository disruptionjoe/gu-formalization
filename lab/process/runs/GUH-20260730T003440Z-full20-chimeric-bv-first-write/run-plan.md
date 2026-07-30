---
run_id: GUH-20260730T003440Z-full20-chimeric-bv-first-write
status: complete
repository: gu-formalization
workflow: joe-directed-north-star-construction
mode: execute
run_type: progress
lane_id: "1"
work_item: SOURCE-OWNED-CHIMERIC-BV-CAMPAIGN-S1
starting_revision: 3c5d8002302cfd3323d37711a7c15995227541a5
opened_at: 2026-07-30T00:34:40Z
closed_at: 2026-07-30T01:30:11Z
result: S1-SPLIT-VERDICT
claim_status_change: none
canon_change: none
public_posture_change: none
external_action_authorization: github_commit_and_push_only
write_boundary:
  - lab/process/runs/GUH-20260730T003440Z-full20-chimeric-bv-first-write/run-plan.md
  - explorations/full20-chimeric-bv-first-write-2026-07-29.md
  - tests/channel-swings/full20_chimeric_bv_first_write_probe.py
  - explorations/README.md
  - tests/README.md
---

# Swing 1: full 20-slot chimeric/BV first write

## Authorization and purpose

Joe said “Go” immediately after the ratified ten-swing campaign identified S1
as the first executable move. This Run executes **S1 only**: write and
machine-check one complete typed quadratic action/equation sheet on the
20-slot observer carrier, together with a separately enumerated enlarged BV
bundle and explicit maps relating the observer, rolled-complex, W131, and BV
objects.

This Run does not solve coefficients, impose the quadratic master equation,
select a symbol retract, consume P1, compute transport, identify P2/P3, select
a stationary background, or read a mass/count.

## Collision and owner check

The preceding campaign scaffold and reduction/transport packet are complete
at revision `3c5d800`. The completed untracked
`GUH-20260729T131135Z-b5-native-packet-source-audit` is outside this Run's
write boundary and remains untouched.

S1 consumes rather than repeats:

- the exact 20-slot/1920-dimensional/136-cell observer ledger;
- W131's 12-slot/1664-dimensional `ker Gamma` kinetic suboperator;
- the exact four-orbit off-core support lower bound;
- the finite free BV/Koszul--Tate controls;
- the existing source-action term and 27-row ledgers; and
- the five-field native-packet block.

## Layer 0 and construction fork

The Run keeps distinct:

| term | object | S1 relation |
| --- | --- | --- |
| observer carrier | `E_20 = direct sum_i W_i` | exactly 20 labeled field slots; no ghosts or antifields counted here |
| W131 operator | `D_W131` on the 12 `ker Gamma` slots | a declared restriction target, not the full equation |
| carrier kernel | `D_c: E_20 -> E_20` | finite first-order block family containing W131 on `ker Gamma` |
| Euler--Lagrange operator | `H_c: E_20 -> Dens(Y) tensor E_20^vee` | variational, density-dual field equation; not itself a carrier endomorphism or shifted antifield |
| rolled differential | `q_B5` on the unrolled `0 -> 1 -> 13 -> 14` carrier | independent cochain object; a one-copy integer-graded endomorphism of `E_20` is not assumed |
| BV bundle | `F_BV` | enlarged graded bundle containing fields, density-dual antifields, ghosts, and nonminimal sectors |
| BV differential | `Q_BV=(S_BV,-)_BV` | nonlinear/graded Hamiltonian vector field; S1 types but does not transfer nilpotency to `q_B5` |
| physical bilinear | `Re integral <Z,D_c Z>_K` | Krein-paired quadratic kernel, not a mass Hessian |

The primary fork uses actual `TY=TX+Sym^2T*X`,
`Sp(32,32;H)`/Krein, keep-and-grade ghosts, and the geometric
gamma-traceless RS carrier. Exterior-ten, `U(128)`, positive-Hilbert,
ghost-removal, and ghost-subtracted-gravitino replacements are controls only.

## Preregistered expectation, kill, and go

**Expected verdict:**
`FULL20-ACTION-ANSATZ-TYPED; ONE-FILTRATION-DATUM-EXPOSED`.

**Kill:** return `S1-TYPING-KILL` if any observer slot, enlarged-BV sector,
density dual, form/ghost degree, chirality, provenance copy, BV role,
operator direction, inclusion/projection, total rank, or W131 restriction
remains untyped; if `E_20`, `q_B5`, and `Q_BV` collapse; if the observer
four-orbit bound is silently applied to the enlarged BV bundle; or if the
ansatz works only after dropping `X`.

**Go:** a finite source-owned quadratic ansatz family and complete typing
sheet exist. Every coefficient/lower-order choice is marked `canonical`,
`inherited`, or `posit`, and the exact remaining datum blocking a coefficient
solve is named.

## Held-out wall

The following are forbidden as S1 selectors:

- P1 or any DeWitt endpoint phase;
- desired `3E_+` symbol cohomology or a target retract;
- full-packet centrality, domain return, or P2/`C_perp` identification;
- P3, a generation count, or a chiral/Fredholm index;
- a stationary background, Yukawa texture, or mass eigenvalue; and
- the lexicographically first four-orbit support witness.

The initial coefficient family may use only typed GU fields, natural maps,
declared inherited W131 structure, action/BV/Krein requirements visible
before downstream consequences, and explicitly charged finite posits.

## Controls and validation

1. Reproduce the exact 20 slots, complex dimension 1920, and 136 allowed
   observer-symbol cells from the independent ledger.
2. Require all eight `S`/`im Gamma` slots and all eight `X` irreducibles
   arranged in four mirror pairs.
3. Plant and reject omission of `X`, collapse of `S` with `im Gamma`, use of
   `beta` as a principal-symbol slot, and application of the 136-cell bound to
   ghosts/antifields.
4. Check every operator's domain/codomain, degree shift, and linearity.
5. Verify that the W131 restriction covers exactly 12 slots and dimension
   1664, without claiming equality with `E_20` or `q_B5`.
6. Verify that the BV odd symplectic pairing pairs each minimal field/ghost
   with its density-dual antifield and that `K` remains scoped to the observer
   field carrier unless explicitly extended.
7. Compile and run the new probe, run relevant existing census/BV controls,
   and run `git diff --check`.
8. Treat the rolled filtration as an assignment problem, not a noun count:
   normalize only a global shift and any explicitly fixed differential
   degree, compute the grading-constraint rank/nullity for the declared map
   incidence, and report `FILTRATION-NULLITY-k` or
   `FILTRATION-NULLITY-UNCOMPUTABLE`. The expected “one datum” suffix is
   earned only if `k=1`.
9. Plant the Layer-0 alternative exposed by the council: test a single-copy
   integer degree-`+1` endomorphism separately from a `Z/2`-rolled symbol
   operator and from the unrolled `0 -> 1 -> 13 -> 14` cochain carrier.
   A forced `Z/2` coloring is not to be reported as an integer filtration.

No S2 coefficient/support result is authorized by an S1 pass.

## Executed result

The preregistered
`FULL20-ACTION-ANSATZ-TYPED; ONE-FILTRATION-DATUM-EXPOSED`
verdict is **not earned**. The construction returns a split result:

```text
S1-SPLIT-VERDICT
COARSE-RELATIVE-OBSERVER-ANSATZ-WRITTEN
FULL-136-ALLOWED-ENVELOPE-Z2-COLORING-UNIQUE-UP-TO-REVERSAL
WHOLE-BIDIRECTIONAL-136-ENVELOPE-NOT-DEGREE+1-ON-ONE-COPY
FOUR-STAGE-0-1-13-14-CANDIDATE-CARRIER-TYPED; DIFFERENTIAL-UNBUILT
CHOSEN-ONE-STAGE-FIXED-A-BV: COMPLEX-RANK-4608; REAL-RANK-9216
W131-CARRIER-BLOCK-INHERITED
```

The positive construction is a finite nine-block coarse `S/I/R` carrier
ansatz plus a three-block candidate gauge generator. It exposes twelve raw
complex coefficient posits and uses no target count, endpoint phase,
cohomology, P1/P2/P3, or preferred four-orbit witness.

The exact grading result belongs only to the maximal **allowed envelope**.
Its `F_2` incidence matrix has rank 19 and nullity one before fixing the
global reversal, then nullity zero. The complete bidirectional envelope
cannot be homogeneous integer degree `+1` on one copy, but sparse/oriented
proper sub-supports remain open.

The source-shaped four-stage candidate has correctly typed bundles and ranks

```text
S
-> I + R = T*Y tensor S
-> (I + R)^vee_dens = Lambda^13 T*Y tensor S^vee
-> S^vee_dens = Lambda^14 T*Y tensor S^vee

128 -> 1792 -> 1792 -> 128.
```

No differential, square-zero relation, or roll intertwiner has yet been
constructed.

The chosen first-stage fixed-background observer BV ansatz has 64 complex
irreducible coordinates. Its complex-coordinate rank is 4608; the explicit
real Hamiltonian interpretation has underlying real rank 9216. Absolute
minimality/completeness, reducibility, compensators, and the ambient
connection-gauge BV sector remain open.

## Council corrections incorporated

The post-write council caught and corrected:

- double-counting the one-form factor in the first unrolled bundle draft;
- treating Hermitian Krein lowering as complex-linear instead of
  conjugate-linear/real-linear after realification;
- simplifying the W131 equation restriction without the needed
  Krein-orthogonality hypothesis;
- overextending the whole-envelope integer obstruction to sparse one-copy
  differentials;
- reading coarse sector coverage as formula-level irrep support;
- using an unexplained algebraic dagger instead of the intrinsic
  metric/Clifford injection;
- omitting the integral on the physical quadratic density;
- using one uniform antifield shift despite distinct ghost numbers;
- overstating the chosen one-stage BV census as complete/minimal;
- treating a held-out API hash as independent non-fitting evidence; and
- leaving the actual symmetric-ten/exterior-ten fork prose-only.

The final artifact and probe contain the narrowed claims and planted
controls.

## Validation receipt

All commands exited zero:

```text
python3 -m py_compile tests/channel-swings/full20_chimeric_bv_first_write_probe.py
python3 tests/channel-swings/full20_chimeric_bv_first_write_probe.py
python3 tests/shiab_b5_observer_symbol_multiplicity_matrix.py
PYTHONPATH=tests python3 tests/shiab_b5_krein_mirror_orbit_reduction.py
python3 tests/shiab_b5_native_packet_contract.py
python3 absorbed/gu-source-action/tests/test_minimal_bv_kt_closure.py
python3 process_gates/explorations_readme_surface_map_audit.py
python3 process_gates/explorations_top_level_file_boundary_audit.py
python3 process_gates/tests_manifest_count_audit.py
python3 process_gates/changed_public_path_hygiene_audit.py
python3 process_gates/protected_surface_diff_audit.py
git diff --check
```

The unrelated completed untracked native-packet audit remained untouched.

## Continuation

The cheapest next kill/go is formula-level irrep expansion of the nine
carrier maps and three gauge maps. Compute their actual nonzero symbol
support, all-slot incidence, and four-orbit connectivity before deriving a
compensator, native adjoint polarization, Hodge/Krein roll maps, or any
quadratic master-equation solve.
