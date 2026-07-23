# Reviewer guide: clone, reproduce, Lean, claim map

*Companion to* `located-not-forced-generation-count-2026-06-29.md`.

This packet gives a referee a clean path from a pinned commit to the paper's
executable evidence and claim-status map. Passing it reproduces repository
evidence; it is not external validation, peer review, or a proof of three
generations.

## 1. Environment and pinned checkout

Requirements:

- Git and a POSIX shell;
- Python 3.10 or newer with `venv`;
- `numpy` and `sympy` for the paper harness;
- [elan](https://github.com/leanprover/elan) for the repository-pinned Lean
  toolchain; and
- network access for the clone, Python installation, and a first Lean cache or
  toolchain fetch, plus several GB of free disk and memory.

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
```

The validator reads `LOAD-BEARING-NUMBERS.json`. It fails on missing referenced
files, missing source or evidence anchors, a changed primary check count,
duplicate or skipped runtime ordinals, invalid independence declarations, or
coverage totals that disagree with the 31 runtime checks. It validates the
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

## 4. Build the Lean surface

After the numerical harness succeeds, run one Lean build at a time:

```sh
lake exe cache get
lake build
lake env lean tests/located-not-forced/H2_FiniteCore.lean
```

`lake exe cache get` may download precompiled artifacts. If network policy
forbids that command, `lake build` may compile dependencies locally and take
substantially longer. A successful `lake build` checks the repository's whole
declared Lean surface. The paper-facing files highlighted by the manifest are:

- `Lean/GUFormalization/LocatedNotForcedLegs.lean`, including the finite
  Krein-intersection nullity statements and the 96/−96 arithmetic;
- `Lean/GUFormalization/R4TwoArena.lean`, including the
  `ZMod 24 ≃ ZMod 8 × ZMod 3` decomposition and typed disjointness;
- `Lean/GUFormalization/LocatedNotForcedFiniteCore.lean`, landed in commit
  `33549a781f3e2a53d1b6bd0707a838be3db59a0b`, which proves exhaustiveness and
  2-primary product/gcd/lcm closure for the encoded bounded finite class-C
  census; and
- `tests/located-not-forced/H2_FiniteCore.lean`, the targeted public-theorem
  smoke certificate executed by the final command above.

Lean checks the formal statements present in those files. It does not certify
the NumPy carrier construction or the manuscript's physical interpretation.
In particular, H2 explicitly does not reconstruct the 192-dimensional carrier
Hom-space classification. Its split-signature sesquilinear row is Krein-space
data, not a positive-Hilbert-space premise, and it does not close the
true-`Y14`/source-action residual.

## 5. Walk the claim map

Review these four artifacts together:

1. `located-not-forced-generation-count-2026-06-29.md`, especially the boxed
   disclaimer and “Status of claims” table;
2. `LOAD-BEARING-NUMBERS.json`, for number-to-source-to-evidence traceability;
3. `review/HQW-LEAD-premise-flag-map-and-gu-dependency-2026-07-14.md`, for the
   premise flags and per-claim GU dependency; and
4. `review/H8-H9-reviewer-packet-2026-07-23.md`, for this release audit and the
   exact independent-versus-same-path inventory.

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
