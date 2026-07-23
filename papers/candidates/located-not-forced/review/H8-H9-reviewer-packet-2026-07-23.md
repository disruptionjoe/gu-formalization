---
title: "H8-H9 reviewer packet: release evidence and clean-checkout workflow"
status: review-support
doc_type: review
paper: "located-not-forced-generation-count-2026-06-29"
date: "2026-07-23"
scope: "reproducibility and reviewer packaging; no science or claim-grade change"
---

# H8-H9 reviewer packet (2026-07-23)

## Result

H8 is complete at repository-evidence level: all 31 runtime checks now have a
machine-readable source/primary/secondary evidence record and a validator that
rejects missing files, stale evidence anchors, malformed independence classes,
and inconsistent expected counts.

H9 is complete at packet level: `REVIEWER.md` now takes a referee from a pinned
clone through manifest validation, numerical reproduction, the whole-project
Lean build, the targeted H2 Lean certificate, and the existing premise/dependency
claim map. The guide preserves environment and network prerequisites rather
than promising a dependency-free cold build.

This is packaging and audit work only. It does not promote any claim or close an
open mathematical residual.

## Artifacts

- `LOAD-BEARING-NUMBERS.json`: 31-entry machine-readable evidence manifest.
- `validate_release_evidence.py`: standard-library validator.
- `REVIEWER.md`: clone -> declaration -> numbers -> Lean -> claim-map workflow.
- this file: human-readable H8/H9 audit and exact coverage inventory.

The H2 bounded finite core landed at
`33549a781f3e2a53d1b6bd0707a838be3db59a0b`. It is included in the manifest's
Lean surface as:

- `Lean/GUFormalization/LocatedNotForcedFiniteCore.lean`; and
- `tests/located-not-forced/H2_FiniteCore.lean`.

The exact H2 commands are:

```sh
lake build
lake env lean tests/located-not-forced/H2_FiniteCore.lean
```

H2 proves exhaustiveness and power-of-two product/gcd/lcm closure for its
encoded finite class-C model. As its module states, it does not reconstruct the
explicit 192-dimensional carrier census. Its cross-chirality sesquilinear row
is the split/Krein construction, not a positive-Hilbert-space assertion.

## Classification rule

“Independent” requires a different file and a substantively different
derivation or formal proof path. A second script that imports, copies, or
closely repeats the primary implementation is marked `same_code_path`.

The one `independent_value_only` item is deliberately not rounded up: the
second path reproduces `256` as projector arithmetic but reports that the
physical index is zero. It therefore confirms the number, not the primary
index interpretation.

## Exact coverage

| Class | Count | Fraction of 31 |
|---|---:|---:|
| Full independent derivation | 23 | 74.19% |
| Independent arithmetic value only | 1 | 3.23% |
| Same-code-path corroboration only | 6 | 19.35% |
| No second executable/formal path found | 1 | 3.23% |

Full-claim independent coverage is exactly **23/31 (74.19%)**. A
substantively different path reproduces at least the numerical value for
**24/31 (77.42%)**, but the full-claim figure remains 23/31 because LBN-030 is
semantically disputed.

### Item-by-item inventory

| ID | Declared expectation | Coverage | Secondary path |
|---|---|---|---|
| LBN-001 | `M(64,H)` | independent derivation | `tests/chase/MOVE-5/verify/indep_check.py` |
| LBN-002 | `rank(Gamma)=128` | independent derivation | `tests/hardening-pass/verify/oqrk1_indh_rank_indep_check.py` |
| LBN-003 | `1664=2^7*13` | independent derivation | `tests/hardening-pass/verify/oqrk1_indh_rank_indep_check.py` |
| LBN-004 | `640/832/192` | same code path | `tests/generation-sector/h1_selfdual_family_kill.py` |
| LBN-005 | `640/416/64` | same code path | `tests/generation-sector/h1_selfdual_family_kill.py` |
| LBN-006 | triplet dimension `192` | independent derivation | `tests/antilinear-bound/verify/nonkrein_indep_check.py` |
| LBN-007 | Krein signature `(+96,-96,0)` | independent derivation | `tests/antilinear-bound/verify/nonkrein_indep_check.py` |
| LBN-008 | beta residual `<1e-9` | same code path | `tests/generation-sector/ghost_parity_krein.py` |
| LBN-009 | `(9,5)` same-chirality blocks `<1e-9` | independent derivation | `tests/antilinear-bound/verify/nonkrein_indep_check.py` |
| LBN-010 | `(9,5)` net chi `0` | independent derivation | `tests/antilinear-bound/verify/nonkrein_indep_check.py` |
| LBN-011 | `(7,7)` same-chirality blocks `<1e-9` | independent derivation | `tests/antilinear-bound/verify/nonkrein_indep_check.py` |
| LBN-012 | `(7,7)` net chi `0` | independent derivation | `tests/antilinear-bound/verify/nonkrein_indep_check.py` |
| LBN-013 | Euclidean control `abs(chi)=96` | independent derivation | `tests/antilinear-bound/verify/nonkrein_indep_check.py` |
| LBN-014 | admissible antilinear `chi_C=0` | independent formal path | `Lean/GUFormalization/LocatedNotForcedLegs.lean` |
| LBN-015 | self-dual `12k` | same code path | `tests/generation-sector/leg3_family_embedding_enumeration.py` |
| LBN-016 | anti-self-dual `12k` | same code path | `tests/generation-sector/leg3_family_embedding_enumeration.py` |
| LBN-017 | diagonal `24k` | same code path | `tests/generation-sector/leg3_family_embedding_enumeration.py` |
| LBN-018 | Adams/image-of-J order `24` | no second path found | none |
| LBN-019 | `Z/24` primary split `8 x 3` | independent formal path | `Lean/GUFormalization/R4TwoArena.lean` |
| LBN-020 | CRT coprimality/bijection | independent formal path | `Lean/GUFormalization/R4TwoArena.lean` |
| LBN-021 | `Hom(Z/3,Z)=Hom(Z/24,Z)=0` | independent derivation | `tests/big-swing/fb_f4_imageofJ_fractional_and_imports.py` |
| LBN-022 | `e_R=1/12` | independent derivation | `tests/boundary-eta/verify/plus96_eta_denominator_indep_check.py` |
| LBN-023 | order `12`, order-3 part `3` | independent derivation | `tests/big-swing/R4_crt_two_arena.py` |
| LBN-024 | `Tr Y=Tr Q=0` | independent derivation | `tests/decider/adversarial_independent_recheck.py` |
| LBN-025 | electric-charge set | independent derivation | `lab/active-research/verify_clifford_explicit.py` |
| LBN-026 | `16//16=1`, chain-relative | independent derivation | `lab/active-research/verify_clifford_explicit.py` |
| LBN-027 | K3 A-hat value `2` | independent derivation | `tests/decider/adversarial_independent_recheck.py` |
| LBN-028 | RS K3 value `-42` | independent derivation | `tests/forcing-slot/twisted_spin32_index_k3.py` |
| LBN-029 | twist identity `0 mod 3` | independent derivation | `tests/forcing-slot/twisted_spin32_index_k3.py` |
| LBN-030 | `256=2^8`, arithmetic only | independent value only | `tests/forcing-slot/adv_verify_rs_independent.py` |
| LBN-031 | at most two of three properties | independent derivation | `tests/decider/adversarial_independent_recheck.py` |

The JSON manifest is authoritative for methods, source anchors, evidence tokens,
and notes explaining why each path received its class.

## Validator contract

The validator currently checks:

- schema version and required records;
- repository confinement and existence of the paper, claim map, Lean files,
  primary harness, and every secondary evidence file;
- all source anchors and primary/secondary evidence tokens;
- 29 static `check(...)` calls and the declared two-case expansion to 31 runtime
  checks;
- unique sequential `LBN-001` through `LBN-031` identifiers and ordinals;
- class-specific contracts, including different method families for independent
  paths and an explicit shared-implementation note for same-code paths;
- the H2 origin SHA and exact whole-build/targeted-smoke commands; and
- recomputed coverage totals against the declarations.

The validator does not execute numerical evidence or prove that a method-family
description is philosophically independent. The item-level audit supplies that
judgment; `reproduce_all.py` supplies numerical execution.

## Validation record

Observed on 2026-07-23 in the working repository at H2 base commit
`33549a781f3e2a53d1b6bd0707a838be3db59a0b`, with the H8/H9 files present as
uncommitted packet changes:

| Command | Result |
|---|---|
| `python3 papers/candidates/located-not-forced/validate_release_evidence.py` | PASS; 29 static, 31 runtime; 23/1/6/1 |
| `.../research-compute/bin/python papers/candidates/located-not-forced/reproduce_all.py` | exit 0; 31 passed, 0 failed; 22.8 s |
| `lake env lean tests/located-not-forced/H2_FiniteCore.lean` | exit 0; three `#print axioms` reports only `propext`, `Classical.choice`, `Quot.sound` |
| `lake build` | exit 0; 8,645 jobs; existing linter warnings only |

The Python environment used NumPy 2.5.1 and SymPy 1.14.0. These are observed
results, not minimum-version promises.

## Clean-checkout record

A local no-hardlink clone of commit
`33549a781f3e2a53d1b6bd0707a838be3db59a0b` was created at
`/private/tmp/gu-lnf-review-33549a7`. Only the four permitted H8/H9 packet files
were copied into it to simulate their eventual packet commit.

| Clean-checkout command | Result |
|---|---|
| `python3 papers/candidates/located-not-forced/validate_release_evidence.py` | exit 0; PASS; 29 static, 31 runtime; 23/1/6/1 |
| `.../research-compute/bin/python papers/candidates/located-not-forced/reproduce_all.py` | exit 0; 31 passed, 0 failed; 23.1 s |

The clean base harness emitted one NumPy divide-by-zero `RuntimeWarning` in the
non-closing fake-su(2) control and still discriminated and passed. A concurrent
hardening change in the source working tree guards that control, but it was not
part of H2 commit `33549a7` and is outside this lane's write scope.

The clean clone did not contain `.lake/packages`, so Lean was not rerun there
without first exercising networked cache/dependency setup. The same exact H2
commands passed in the source checkout at `33549a7`, as recorded above. This is
therefore a clean-checkout Python/package simulation, not yet a cold-network
Lean replication and not an external review.

The final release record should name the eventual committed H8/H9 packet SHA
and preserve all command exit codes. A cold checkout may need network access
for Python packages, elan, and `lake exe cache get`; absence of that network is
an environment failure, not a theorem failure.

## Binding scope

- A torsion class `Z/3` is not an integer count; the manifest keeps
  `Hom(Z/3,Z)=0` explicit.
- Krein and positive-Hilbert constructions are not conflated.
- LBN-030 remains value-only evidence because the independent script identifies
  the 256 calculation as a projector tautology and reports physical index zero.
- The true-`Y14`/source-action relative-index residual remains open.
- All results here are internal-tier repository reproduction until an external
  reviewer independently executes and assesses them.
