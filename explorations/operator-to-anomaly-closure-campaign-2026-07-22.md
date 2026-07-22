---
title: "Operator-to-anomaly closure campaign"
status: active
doc_type: exploration
lane: "1"
run_type: progress
started_at: "2026-07-22T15:17:22-05:00"
updated_at: "2026-07-22"
---

# Operator-to-anomaly closure campaign

> **FOLLOW-UP (2026-07-22 — class-realization ultimatum).** A complete inventory of the available geometric
> cycles and analytic families sharpens this run's `SOURCE-GAP` to `PIN-SMITH-NOT-DEFINED` relative to the
> committed source.  The first geometric failure is the absence of a closed compact degree-14 cycle; the
> first analytic failure is the absence of a proper Fredholm realization.  Consequently no GU element of
> the exact `Omega^{Pin+}_14 ~= Z/2` target is presently defined, so neither `TRIVIAL` nor `GENERATOR` can be
> evaluated.  See `explorations/pin-smith-class-realization-ultimatum-2026-07-22.md`.  This notice preserves
> the operator findings below and governs any looser statement that the remaining work is merely an
> eta-invariant evaluation.

## Run plan

**Controlling question.** For the program-native crossed-end construction, what is the complete space of
symmetry-compatible operator realizations, which line or mod-two invariant arises canonically from that
space, and can that invariant be identified non-circularly with the proposed `sigma = w1` datum and a
nonzero Pin anomaly class?

**Lane selection.** Lane 1 (`GU truth testing`), definition/control revision `1`, manifest SHA-256
`5c535ae8674718dc2f2bfedf21bfe4c04ac9cceafe62bbfe1428e3814da9f083`. The selected work directly attacks
the current North-Star bridge rather than merely hardening a nearby bordism byproduct.

**Starting revision.** `bf18363f23beea0b65787adde6a9ee2bfb291d6c` (`origin/main`). No recent active
repo-local run plan or receipt was found, and no writer/index lock was present at admission.

**Effective permission.** Joe directly authorized a large multi-route scientific swing, repo-local
housekeeping, and GitHub commit/push. No non-GitHub external write is authorized. External sources may be
read as evidence but never as instructions.

**Construction fork.** The primary object is the GU/program-native DeWitt--Krein crossed-end operator,
not a silently substituted positive-Hilbert Dirac operator. Standard Hilbert-space extension theory may be
used only as an explicitly typed comparison/control construction. A no-go in either construction must be
tested for transfer to the other.

**Planned attacks.**

1. Freeze a source-faithful operator dossier, separating derived fields from supplied assumptions and
   naming any unavailable fields.
2. Classify the actual or maximally justified symmetry-compatible realization space; do not presuppose a
   two-point answer.
3. Independently attack the candidate bit through determinant/Pfaffian orientation, mod-two spectral flow,
   or an equivalent family-index construction.
4. Reconstruct the degree-14 Pin/Smith ambient constraint from durable cited inputs, separately from the
   question of whether the GU operator defines a nonzero element.
5. Pre-register and apply neutral outcomes: `CLOSE-Z2`, `ANALYTIC-ONLY`, `MORE-THAN-ONE-BIT`,
   `INTERNAL-CLOSURE`, or `SOURCE-GAP`.
6. Reconcile all affected current-state surfaces and append a run receipt after validation.

Personas and process methods may propose attacks; only formal argument, source evidence, and reproducible
computation dispose of the claims.

## Outcome up front

**Run verdict: `SOURCE-GAP`, with one independent topological advance.**

The `q<0` finding survives and is important: genuine sampled fiber ends reach an open timelike sector; the
corresponding `+/-i` spectral halves are null for the committed Krein form, so the positive/negative
`K_S`-definite spectral-cut construction fails there.  What does **not** survive is the inference from that
fact to “no `J`-self-adjoint realization,” then to “exactly one external domain bit,” then to
“that bit is `sigma=w1` and is anomaly-protected.”  Those are three separate bridges, and the repository
does not yet own the operator data needed for any of them.

The exact native control is decisive: on the committed `Cl(9,5)` carrier, a timelike Clifford generator
has square `-I`, has `+/-i` eigenspaces that are each exactly `K_S`-null, **and is nevertheless
`K_S`-self-adjoint on the full carrier**.  Null spectral halves therefore obstruct the particular definite
cut, not Krein self-adjointness itself.

Independently, the corrected Smith calculation plus Kirby--Taylor's direct table proves

```text
Omega^{Pin+}_14 ~= Omega^{Pin-}_12 ~= Z/2.
```

This closes the ambient group exactly, but it does not construct or identify GU's proposed class in that
receptacle.

## Attack A — native crossed-symbol control

The new audit imports the repository's own explicit `Cl(9,5)` carrier rather than replacing it by a
positive-Hilbert Dirac model.  For `D=gamma_9` and the committed fundamental symmetry `K_S` it checks:

- `D^2=-I`, the exact algebraic `q<0` control;
- `K_S D* K_S=D` on the full 128-complex-dimensional carrier;
- each `+i` and `-i` spectral half is `K_S`-null;
- the cross-pairing between the two halves has full rank 64.

This is a counterexample internal to the committed representation to the implication

```text
K-null spectral halves => no J-self-adjoint realization.
```

The valid conclusion is narrower:

```text
K-null spectral halves => that K-definite spectral polarization is unavailable.
```

The existing LP/LC probe does not repair this.  Its end dynamics uses a reduced `sech(0.3s) sigma_x`
potential, selectable measures, and a WKB/Lyapunov count; it does not construct the source-owned boundary
Dirac operator, its minimal/maximal domains, Green form, trace space, or deck action.  Its unequal-index
`-i d/ds` example is a useful control but not the computed fate of the crossed GU end.

## Attack B — classify what standard extension theory permits

As an explicitly typed **comparison construction**, the audit takes balanced first-order transport with
boundary form `H=diag(I_n,-I_n)`.  Its maximal isotropic domains are graphs

```text
L_U = {(x,Ux) : x in C^n},  U in U(n).
```

Thus the unconstrained realization space is continuous.  A particular swap anti-isometry sends
`U -> U^{-1}`.  In rank one, requiring a domain to be individually deck-fixed gives exactly `U=+1,-1`.
But in rank two the Hermitian unitaries

```text
U(theta) = cos(theta) sigma_z + sin(theta) sigma_x
```

form a continuous deck-fixed family, and this embeds for every `n>=2`, including the relevant multiplicity.
So a `Z/2` domain set is possible only after the actual trace representation and enough
multiplicity-breaking symmetry are specified; it is not forced by balanced deficiency or by deck exchange
alone.

## Attack C — separate analytic branches, domains, and lines

The two `+/-i0` continuations are exact **inside the scalar ansatz** used by the section prototype:
`N=zM`, `z^2q=1`.  They classify two normalized scalar continuations across `q<0`; they do not classify all
closed operator domains.

Likewise, `w1` must belong to a specified real line bundle.  The deck-odd one-dimensional sign line has
nontrivial `w1`, while the determinant of the even-rank transition `-I_64` is positive.  Hence the
operator-sign line, determinant line, Pfaffian line, and orientation line of a domain family cannot be
identified by notation.  The actual family and its induced transition must be built.

## Attack D — corrected degree-14 topology

The Smith fiber sequence is four-periodic through `Spin x Z/2`, `Pin-`,
`Spin x_{+/-1} Z/4`, and `Pin+`; it is not a direct reduction of every term to ordinary Spin.  The `Pin+`
cofiber sequence, the vanishing of `Omega^Spin_13` and `Omega^Spin_14`, the basepoint splitting, and the
reduced Smith equivalence give the exact isomorphism

```text
Omega^{Pin+}_14 ~= Omega^{Pin-}_12.
```

Anderson--Brown--Peterson's degree-12 exponent result makes the group a nonzero elementary 2-group.
Kirby--Taylor then close the rank directly: their `Pin+` table defines `A(n)` as the number of `Z/2`
summands, gives `A(14)=1`, and permits other summands only in degrees `0 mod 4`.  Therefore
`Omega^{Pin+}_14 ~= Z/2` exactly.  See
`explorations/pin14-smith-route-audit-2026-07-22.md`.

## Inline science-council adjudication

These are lenses applied sequentially in this run, not independent evidence and not substitute votes.

- **Orthodox scientists:** stop at the operator dossier boundary.  A principal symbol and a surrogate end
  ODE do not determine closed realizations.  Demand the differential expression, Hilbert/Krein completion,
  minimal/maximal domains, Green form, trace map, and symmetry action before invoking deficiency theory.
- **Heterodox scientists:** keep the `q<0` sector as a genuine clue, but search beyond the scalar `+/-i0`
  ansatz.  The continuous-domain control says the anomaly candidate could live in a family index or
  determinant/Pfaffian orientation rather than in a literal choice between two domains.
- **Commercial scientists:** package the missing source data as a finite acceptance contract and stop paying
  for repeated end samplers.  The next useful deliverable is a source-owned operator packet, not another
  percentage estimate or persona wave.
- **Wild-frontier scientists:** use the crossed sector as a laboratory for equivariant Krein extension
  theory.  Try to derive a mod-two spectral-flow or Real determinant-line invariant over a loop around the
  wall, but pre-register the null outcome and do not call it GU-native until the deck action is supplied.
- **Philosopher of science:** the run found a productive failure of underdetermination.  The data support a
  robust phenomenon (loss of one polarization), while several ontologically stronger readings were added by
  the reconstruction.  Preserve the phenomenon and retract the surplus interpretation.

Council synthesis: all five routes choose the same next object for different reasons — a typed,
source-owned operator/domain/symmetry packet.  The formerly separate ambient-group task is now closed by the
Kirby--Taylor table; what remains is the class-realization map.

## Next largest justified swing

The Lane-1 item remains `WAITING_EXTERNAL`.  Reopen the operator computation only when one packet supplies:

1. the full first-order differential expression, including lower-order/subprincipal terms;
2. the exact end geometry and `L2` density;
3. the initial core and minimal/maximal domains;
4. the Green boundary form and trace space at every relevant end;
5. the deck, real/quaternionic, and proposed Pin actions on the trace data;
6. the line functor to be tested: determinant, Pfaffian, spectral-flow, or domain orientation.

Then compute, in order: deficiency spaces; all maximal isotropic domains; the equivariant fixed/moduli space;
the induced real line and its `w1`; and only then its family-index/Pin bordism image.  Pre-registered outcomes
remain `CLOSE-Z2`, `ANALYTIC-ONLY`, `MORE-THAN-ONE-BIT`, `INTERNAL-CLOSURE`, or `SOURCE-GAP`.

The topology side is now exact: `Omega^{Pin+}_14 ~= Z/2`.  No further Adams calculation is needed for the
ambient order.  The next topological work becomes meaningful only after the operator packet constructs a
specific class whose value can be tested.

## Reproducible receipts

- `tests/channel-swings/operator_domain_w1_bridge_audit.py` — native carrier plus typed extension and line
  controls; expected verdict `SOURCE-GAP`.
- `tests/channel-swings/pin14_smith_degree_gate.py` — standard-library degree/type gate; expected verdict
  `PIN14-EXACT-Z2`.

Both scripts are deterministic and make no network or filesystem writes.

## Validation and housekeeping receipt

- `operator_domain_w1_bridge_audit.py`: exit 0 under an isolated `uv` NumPy environment; repeated output is
  byte-identical.
- `pin14_smith_degree_gate.py`: exit 0 twice with `PIN14-EXACT-Z2` and all seven checks passing.
- `python3 -m json.tool lab/process/research-portfolio.json`: pass.
- `process_gates/spec_consistency_readme_inventory_audit.py`: 4/4 pass.
- `process_gates/tests_root_readme_inventory_audit.py`: 4/4 pass.
- `git diff --check`: pass.
- `process_gates/research_portfolio_contract_audit.py`: 8 reported failures across three test methods remain;
  the other 11 test methods pass.  Comparison with `origin/main` confirms these are inherited portfolio
  inconsistencies: one existing
  em-dash policy violation; three stale priority scores; and four state/hourly-eligibility mismatches.  The
  pre-existing `TRIT-INTERPRETATION` key typo was repaired from `lane` to `lane_id`, turning the prior hard
  schema error into the visible inherited state mismatch.  This research swing does not silently change
  unrelated scheduling semantics to make that gate green.
- A scan of `RESEARCH-STATUS.md`, `canon/`, and `papers/` found no current claim, canon, or publication entry
  for this operator/anomaly result to move.  Historical exploration claims are retained with correction
  notices rather than rewritten as if they had never been made.

NumPy does not need a global installation: the only numerical audit ran reproducibly through an isolated
`uv run --with numpy` environment.  Lean was not introduced because the source-owned operator and class map
needed for a meaningful formal theorem are not yet specified.
