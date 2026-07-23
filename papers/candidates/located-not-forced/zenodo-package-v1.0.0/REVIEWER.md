# Reviewer guide: clone, reproduce, Lean, claim ledger

*Companion to* `located-not-forced-generation-count-2026-06-29.md`.

This packet gives a referee a clean path from a pinned commit to the paper's
executable evidence and current claim ledger. Passing it reproduces repository
evidence; it is not external validation, peer review, or a proof of three
generations. External review is welcome but is not a prerequisite for a Zenodo
deposit; it becomes a prerequisite only for describing the work as externally
validated.

## 1. Environment and pinned checkout

Requirements:

- Git and a POSIX shell;
- Python with `venv` (the pinned review run records the exact tested version;
  no broader minimum-version claim is made);
- `numpy` and `sympy` for the paper harness;
- [elan](https://github.com/leanprover/elan) for the repository-pinned Lean
  toolchain; and
- network access for the clone, Python installation, and a first Lean cache or
  toolchain fetch, plus several GB of free disk and memory.

The v2.15 internal release run used Python 3.14.6, NumPy 2.5.1, and SymPy
1.14.0. Those are tested-environment facts, not a promise that every newer or
older combination is supported.

The wider test tree also uses packages in `requirements.txt`, including SciPy.
They are not required for the one-file paper harness.

Obtain the exact review commit from the release record, editor, or review
packet and substitute it below. Do not review a moving branch tip.

```sh
export REVIEW_SHA='<exact 40-character commit supplied for review>'
git clone https://github.com/disruptionjoe/gu-formalization.git
cd gu-formalization
git switch --detach "$REVIEW_SHA"
test "$(git rev-parse HEAD)" = "$REVIEW_SHA"

python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install numpy sympy
```

The repository's `lean-toolchain` and `lake-manifest.json` pin the Lean
environment. Do not run `lake update`: that changes the dependency graph being
reviewed.

## 2. Validate the evidence declaration

Run:

```sh
python papers/candidates/located-not-forced/validate_release_evidence.py
```

Expected result:

```text
PASS: release-evidence manifest is internally consistent
  primary harness: 29 static check calls, 31 declared runtime checks
  coverage: 23 full independent; 1 independent value only; 6 same-code-path only; 1 no second path
  claim ledger: papers/candidates/located-not-forced/CLAIM-AND-PREMISE-LEDGER.json
  historical claim map: papers/candidates/located-not-forced/review/HQW-LEAD-premise-flag-map-and-gu-dependency-2026-07-14.md
```

The validator reads `LOAD-BEARING-NUMBERS.json` and the current
`CLAIM-AND-PREMISE-LEDGER.json`. It fails on missing referenced files, missing
source or evidence anchors, a changed primary check count, duplicate or skipped
runtime ordinals, invalid independence declarations, coverage totals that
disagree with the 31 runtime checks, unknown premise dependencies, invalid
claim grades/codomains, or known superseded formulations. It validates the
release declaration; it does not execute the numerical checks.

The manifest is the machine-readable map from every runtime check to:

- the public claim and expected value;
- an anchor in the paper;
- the primary function in `reproduce_all.py`; and
- a second derivation, a disclosed shared-code rerun, or an explicit evidence
  gap.

## 3. Execute all paper-level checks

Run:

```sh
python papers/candidates/located-not-forced/reproduce_all.py
```

Expected result is exit code 0 and:

```text
load-bearing checks: 31 passed, 0 failed  (total 31)
ALL LOAD-BEARING NUMBERS REPRODUCE. Exit 0.
```

Each check prints the paper value next to the computed value. Controls use
wrong or scrambled inputs and must discriminate. Runtime is normally a few
minutes and depends on BLAS and hardware. The harness is deterministic and
does not import the test tree.

The 31 runtime results come from 29 static `check(...)` call sites: two call
sites in `check_theorem2` execute for both `(9,5)` and `(7,7)`.

## 4. Build the paper-facing Lean surface

After the numerical harness succeeds, run the targeted paper-facing checks one
at a time:

```sh
lake exe cache get
lake -Kjobs=1 build +GUFormalization.LocatedNotForcedFiniteCore
lake env lean Lean/GUFormalization/LocatedNotForcedLegs.lean
lake env lean tests/located-not-forced/H2_FiniteCore.lean
lake env lean tests/located-not-forced/V15_CodomainSeparatedFiniteCore.lean
lake env lean tests/located-not-forced/V15_KreinTransversality.lean
```

`lake exe cache get` may download precompiled artifacts. If network policy
forbids that command, the first targeted build may compile dependencies locally
and take substantially longer. These commands check the paper-facing surface;
they do not imply that every unrelated module in the repository was rebuilt.
The files highlighted by the manifest are:

- `Lean/GUFormalization/LocatedNotForcedLegs.lean`, including the finite
  Krein-intersection nullity statements and the 96/−96 arithmetic;
- `Lean/GUFormalization/R4TwoArena.lean`, including the
  `ZMod 24 ≃ ZMod 8 × ZMod 3` decomposition and typed disjointness;
- `Lean/GUFormalization/LocatedNotForcedFiniteCore.lean`, landed in commit
  `33549a781f3e2a53d1b6bd0707a838be3db59a0b`, which proves exhaustiveness and
  now types finite torsion, integer equality/divisibility, representation
  dimensions, and diagnostics separately while preserving the historical
  finite-census origin; and
- `tests/located-not-forced/H2_FiniteCore.lean`, the targeted public-theorem
  smoke certificate;
- `tests/located-not-forced/V15_CodomainSeparatedFiniteCore.lean`, the typed
  codomain and CRT-input boundary certificate; and
- `tests/located-not-forced/V15_KreinTransversality.lean`, the complex
  Hermitian finite transversality certificate.

Lean checks the formal statements present in those files. It does not certify
the NumPy carrier construction or the manuscript's physical interpretation.
In particular, H2 explicitly does not reconstruct the 192-dimensional carrier
Hom-space classification. Its split-signature sesquilinear row is Krein-space
data, not a positive-Hilbert-space premise, and it does not close the
true-`Y14`/source-action residual.

## 5. Run the physical-signature and framing discriminators

Using the same Python environment:

```sh
python tests/lorentzian-transfer/physical_signature_transfer_audit.py
python tests/boundary-eta/v15_framing_convention_sensitivity.py
```

Expected terminal receipts are:

```text
AUDIT PASS: 53/53 checks
VERDICT: PASS_WITH_DECLARED_GU_TANGENTIAL_IDENTIFICATION_PREMISE
```

The first command distinguishes the compact `192/(96,96)/(2,2,2,2,0)`
packet from one physical Lorentzian Hodge half and its conjugation-stable
closure. The second enumerates both signs, CRT projections, and
factor/object sensitivities for the framed cycle. Neither constructs the true
`Y14` source action.

## 6. Walk the current claim ledger

Review these four artifacts together:

1. `located-not-forced-generation-count-2026-06-29.md`, especially the front
   disclaimer and “Status of claims” table;
2. `LOAD-BEARING-NUMBERS.json`, for number-to-source-to-evidence traceability;
3. `CLAIM-AND-PREMISE-LEDGER.json`, for stable current claim IDs, codomains,
   premises, evidence roles, GU dependency, evidence paths, and scope exits;
4. `review/V15-2-cfin-cinv-lifting-audit-2026-07-23.md`,
   `review/V15-4-carrier-faithfulness-packet-2026-07-23.md`, and
   `review/V15-5-framing-convention-sensitivity-2026-07-23.md`, for the
   current theorem-domain, carrier-transfer, and framing boundaries.

The July 14 `HQW-LEAD` map remains in `review/` as historical evidence. It is
not the current release authority. The H8-H9 packet likewise records the
v2.14 release-evidence inventory; where it conflicts with the current ledger
or v2.15 packets, the current artifacts govern.

The machine-readable view is also available with:

```sh
python papers/candidates/located-not-forced/validate_release_evidence.py --json
```

## Coverage and interpretation

The manifest classifies all 31 runtime checks, without promoting same-code
reruns to independent evidence:

| Coverage class | Checks | Meaning |
|---|---:|---|
| Full independent derivation | 23 | A different file and substantively different derivation confirms the full expectation |
| Independent value only | 1 | A different derivation reproduces 256 and confirms that it is a projector trace, not a physical index |
| Same-code-path corroboration only | 6 | A second file shares or closely copies the primary recipe |
| No second executable/formal path found | 1 | The order-24 Adams/image-of-J derivation is present only in the primary harness |

Thus 23/31 (74.19%) have full independent derivations. Including the
value-only arithmetic cross-check gives 24/31 (77.42%) with a substantively
different executable path for at least the stated number. It does not raise
the full-claim figure above 23/31.

The critical scope rules are:

- `Z/3` is torsion, not an integer generation count:
  `Hom(Z/3,Z)=0`;
- the indefinite Krein construction and a positive Hilbert-space construction
  are different objects and are not interchangeable;
- the independently reproduced `256` is a projector trace whose second path
  reports physical index zero, so it is value-only evidence; and
- the true-`Y14`/source-action relative-index residual remains open.

## Failure triage

- Validator failure: use the reported entry and token to find a stale source,
  function, or evidence declaration. Do not merely update an expected number
  to make it pass.
- Numerical `[FAIL]`: retain the complete output, Python version, platform,
  NumPy/SymPy versions, and reviewed commit.
- Lean failure before project compilation: record elan, network/cache, and
  toolchain diagnostics separately from theorem failures.
- Paper/evidence disagreement: treat the paper's status table and open
  residual as binding; a successful computation does not by itself upgrade a
  claim.

For a review report, record `git rev-parse HEAD`, all command exit codes, and
whether execution occurred in a genuinely fresh checkout.
