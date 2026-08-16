#!/usr/bin/env python3
"""Integration audit for the 2026-08-15 Claude session.

This probe checks scope, artifact governance and the visible correction layer.
It deliberately does not recompute the scientific probes it inventories; the
session-scoped validation run executes those entry points separately.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[2]
SESSION_ID = "session_015qsiNaasV9Pabea3Cf9K64"
SESSION_TRAILER = (
    "Claude-Session: https://claude.ai/code/" + SESSION_ID
)
TERMINAL_COMMIT = "fb854a13c0b3d956c83c1e06648c201a988fc785"
CORRECTION_TOKEN = "CORRECTION IV-20260815"
MUTATION = os.environ.get("GU_SESSION_INTEGRATION_MUTATION", "")

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, condition: bool, detail: str) -> None:
    CHECKS.append((name, bool(condition), detail))


def git(*args: str) -> str:
    proc = subprocess.run(
        ["git", *args], cwd=ROOT, text=True, capture_output=True, check=False
    )
    if proc.returncode:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip())
    return proc.stdout


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return ""
    end = text.find("\n---\n", 4)
    return text[4:end] if end >= 0 else ""


def session_commits() -> list[str]:
    out = git(
        "log",
        "--all",
        "--since=2026-08-15 00:00",
        "--grep=" + SESSION_ID,
        "--format=%H",
    )
    return [line for line in out.splitlines() if line]


def session_added_artifacts(commits: list[str]) -> list[str]:
    paths: set[str] = set()
    for commit in commits:
        out = git(
            "diff-tree",
            "--no-commit-id",
            "--name-only",
            "--diff-filter=A",
            "-r",
            commit,
        )
        for path in out.splitlines():
            if (
                path.startswith("lab/active-research/joe-directed/")
                and path.endswith(".md")
                and not path.endswith("/README.md")
            ):
                paths.add(path)
    return sorted(paths)


def main() -> int:
    CHECKS.clear()
    commits = session_commits()
    expected_count = 38 if MUTATION == "commit_count" else 39
    check(
        "scope.commit_count",
        len(commits) == expected_count,
        f"got {len(commits)}, expected {expected_count}",
    )
    check(
        "scope.terminal_commit",
        TERMINAL_COMMIT in commits,
        f"terminal {TERMINAL_COMMIT[:8]} absent",
    )

    for commit in commits:
        body = git("show", "-s", "--format=%B", commit)
        check(
            "scope.exact_trailer." + commit[:8],
            SESSION_TRAILER in body,
            "session trailer absent from commit body",
        )

    artifacts = session_added_artifacts(commits)
    check(
        "governance.session_artifact_count",
        len(artifacts) == 35,
        f"got {len(artifacts)}, expected 35 non-index markdown artifacts",
    )
    missing_effect = [
        path
        for path in artifacts
        if "canonical_effect:" not in frontmatter(read(path))
    ]
    check(
        "governance.canonical_effect_explicit",
        not missing_effect,
        "missing=" + repr(missing_effect),
    )

    special_effects = {
        "lab/active-research/joe-directed/archaeology/ar3-rediscovery-rate-2026-08-15.md": "none",
        "lab/active-research/joe-directed/archaeology/ar4-c3c-genericity-control-2026-08-15.md": "none",
        "lab/active-research/joe-directed/base-duality/bd-reg-routing-backlog-disposition-2026-08-15.md": "none",
        "lab/active-research/joe-directed/vz-repair/vz4-pullback-is-a-contraction-2026-08-15.md": "narrow_canon_correction_integrated_after_independent_second_verification",
    }
    if MUTATION == "metadata_ar3":
        special_effects[next(iter(special_effects))] = "pending_integration"
    for path, value in special_effects.items():
        check(
            "governance.effect." + Path(path).stem,
            f"canonical_effect: {value}" in frontmatter(read(path)),
            f"expected canonical_effect {value}",
        )

    corrected = [
        "lab/active-research/joe-directed/base-duality/bd-c-met-x-is-an-argument-not-a-background-2026-08-15.md",
        "lab/active-research/joe-directed/base-duality/bd-d-the-quotient-cures-the-base-not-the-fibre-2026-08-15.md",
        "lab/active-research/joe-directed/base-duality/bd-disposition-packet-2026-08-15.md",
        "lab/active-research/joe-directed/indefiniteness-typing/itc-positivity-rows-are-five-not-ten-2026-08-15.md",
        "lab/active-research/joe-directed/carrier/crb-carrier-is-four-corners-not-one-weyl-2026-08-15.md",
        "lab/active-research/joe-directed/high-energy-two-plus-one/he2-real-form-does-not-pair-144-with-144bar-2026-08-15.md",
        "lab/active-research/joe-directed/source-chain/sca-right-chain-2026-08-15.md",
    ]
    wanted_token = CORRECTION_TOKEN + ("-MUTATED" if MUTATION == "marker" else "")
    for path in corrected:
        check(
            "coherence.correction_marker." + Path(path).stem,
            wanted_token in read(path),
            f"{wanted_token!r} absent",
        )

    register = json.loads(read("lab/process/source-native-comparator-routing-registry.json"))
    integration_path = (
        "lab/active-research/joe-directed/integration-review/"
        "session-015qsi-coherence-integration-repair-2026-08-15.md"
    )
    rows = {
        row["path"]: row["classification"] for row in register["artifacts"]
    }
    expected_classification = (
        "SOURCE_NATIVE_ROUTE"
        if MUTATION == "routing"
        else "BRIDGE_OR_SEMANTIC_BOUNDARY"
    )
    check(
        "governance.integration_record_registered",
        rows.get(integration_path) == expected_classification,
        f"got {rows.get(integration_path)!r}, expected {expected_classification!r}",
    )

    register_claims = read("lab/sources/source-claim-register.yaml")
    check(
        "source.one_weyl_layer_retained",
        "id: SC-GEN-55" in register_claims
        and "ONE Weyl spinor -> one generation coexists" in register_claims,
        "SC-GEN-55 or its layer distinction is absent",
    )
    check(
        "source.vz_unknown_retained",
        "id: SC-PRE-56" in register_claims
        and "Whether the spin-3/2 sector has a Velo-Zwanziger pathology is unknown"
        in register_claims,
        "SC-PRE-56 uncertainty is absent",
    )

    failed = [(name, detail) for name, ok, detail in CHECKS if not ok]
    for name, detail in failed:
        print(f"FAIL {name}: {detail}")
    print(f"CERTIFICATE: {len(CHECKS) - len(failed)}/{len(CHECKS)} checks pass.")
    return 1 if failed else 0


def selftest() -> int:
    baseline = main()
    if baseline != 0:
        print("SELFTEST FAILED: clean baseline is red; mutations are not interpretable.")
        return 1

    failures: list[str] = []
    for mutation in ("commit_count", "metadata_ar3", "marker", "routing"):
        env = dict(os.environ, GU_SESSION_INTEGRATION_MUTATION=mutation)
        proc = subprocess.run(
            [sys.executable, __file__],
            cwd=ROOT,
            env=env,
            text=True,
            capture_output=True,
            check=False,
        )
        caught = proc.returncode == 1
        print(f"mutation {mutation:16s} exit {proc.returncode} {'CAUGHT' if caught else 'MISSED'}")
        if not caught:
            failures.append(mutation)
    if failures:
        print("SELFTEST FAILED: " + ", ".join(failures))
        return 1
    print("SELFTEST PASSED: clean baseline plus 4/4 caught mutations.")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else main())
