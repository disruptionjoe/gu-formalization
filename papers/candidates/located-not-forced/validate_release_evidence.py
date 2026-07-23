#!/usr/bin/env python3
"""Validate the Located, Not Forced release-evidence manifest.

This checks the manifest's structure, file references, source/evidence anchors,
primary-harness check count, and declared coverage arithmetic.  It deliberately
does not execute the numerical evidence; run reproduce_all.py for that.
"""

from __future__ import annotations

import argparse
import ast
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
DEFAULT_MANIFEST = HERE / "LOAD-BEARING-NUMBERS.json"
DEFAULT_REPO_ROOT = HERE.parents[2]
ALLOWED_CLASSIFICATIONS = {
    "independent_derivation",
    "independent_value_only",
    "same_code_path",
    "no_second_path",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--repo-root", type=Path, default=DEFAULT_REPO_ROOT)
    parser.add_argument(
        "--json",
        action="store_true",
        help="emit the result as JSON instead of human-readable text",
    )
    return parser.parse_args()


def resolve_repo_path(repo_root: Path, relative: Any, label: str, errors: list[str]) -> Path | None:
    if not isinstance(relative, str) or not relative:
        errors.append(f"{label}: expected a non-empty repository-relative path")
        return None
    candidate = (repo_root / relative).resolve()
    try:
        candidate.relative_to(repo_root)
    except ValueError:
        errors.append(f"{label}: path escapes repository root: {relative!r}")
        return None
    if not candidate.is_file():
        errors.append(f"{label}: missing file: {relative}")
        return None
    return candidate


def require_tokens(text: str, tokens: Any, label: str, errors: list[str]) -> None:
    if not isinstance(tokens, list) or not tokens:
        errors.append(f"{label}: evidence_tokens/anchors must be a non-empty list")
        return
    for token in tokens:
        if not isinstance(token, str) or not token:
            errors.append(f"{label}: tokens must be non-empty strings")
        elif token not in text:
            errors.append(f"{label}: token not found: {token!r}")


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError("manifest root must be a JSON object")
    return value


def count_check_calls(path: Path, errors: list[str]) -> int:
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except (OSError, SyntaxError) as exc:
        errors.append(f"primary_harness: cannot parse {path}: {exc}")
        return -1
    return sum(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "check"
        for node in ast.walk(tree)
    )


def validate(manifest: dict[str, Any], repo_root: Path) -> tuple[list[str], dict[str, Any]]:
    errors: list[str] = []
    repo_root = repo_root.resolve()

    if manifest.get("schema_version") != 1:
        errors.append("schema_version: expected 1")

    paper_path = resolve_repo_path(repo_root, manifest.get("paper"), "paper", errors)
    paper_text = paper_path.read_text(encoding="utf-8") if paper_path else ""

    claim_map = resolve_repo_path(repo_root, manifest.get("claim_map"), "claim_map", errors)
    lean_surface = manifest.get("lean_surface")
    if not isinstance(lean_surface, list) or not lean_surface:
        errors.append("lean_surface: expected a non-empty list")
    else:
        for index, path in enumerate(lean_surface):
            resolve_repo_path(repo_root, path, f"lean_surface[{index}]", errors)
    lean_reproduction = manifest.get("lean_reproduction")
    if not isinstance(lean_reproduction, dict):
        errors.append("lean_reproduction: expected an object")
    else:
        origin = lean_reproduction.get("h2_origin_commit")
        if (
            not isinstance(origin, str)
            or len(origin) != 40
            or any(character not in "0123456789abcdef" for character in origin)
        ):
            errors.append(
                "lean_reproduction.h2_origin_commit: expected a lowercase 40-character SHA"
            )
        commands = lean_reproduction.get("commands")
        expected_commands = {
            "lake build",
            "lake env lean tests/located-not-forced/H2_FiniteCore.lean",
        }
        if not isinstance(commands, list) or set(commands) != expected_commands:
            errors.append(
                "lean_reproduction.commands: expected the whole-project build and "
                "targeted H2 smoke command"
            )
        if not isinstance(lean_reproduction.get("scope_note"), str) or not lean_reproduction[
            "scope_note"
        ]:
            errors.append("lean_reproduction.scope_note: expected a non-empty string")

    harness = manifest.get("primary_harness")
    if not isinstance(harness, dict):
        errors.append("primary_harness: expected an object")
        harness = {}
    harness_path = resolve_repo_path(
        repo_root, harness.get("path"), "primary_harness.path", errors
    )
    harness_text = harness_path.read_text(encoding="utf-8") if harness_path else ""
    actual_static = count_check_calls(harness_path, errors) if harness_path else -1
    expected_static = harness.get("expected_static_check_calls")
    if actual_static != expected_static:
        errors.append(
            "primary_harness.expected_static_check_calls: "
            f"declared {expected_static!r}, found {actual_static}"
        )

    expansion = harness.get("dynamic_expansion")
    if not isinstance(expansion, dict):
        errors.append("primary_harness.dynamic_expansion: expected an object")
        expansion = {}
    cases = expansion.get("loop_cases")
    calls_per_case = expansion.get("check_calls_per_case")
    static_in_loop = expansion.get("static_calls_in_loop")
    runtime_minus_static = expansion.get("runtime_minus_static")
    if not isinstance(cases, list) or not cases:
        errors.append("primary_harness.dynamic_expansion.loop_cases: expected a non-empty list")
        computed_delta = None
    elif not all(isinstance(value, int) for value in (calls_per_case, static_in_loop)):
        errors.append(
            "primary_harness.dynamic_expansion: check_calls_per_case and "
            "static_calls_in_loop must be integers"
        )
        computed_delta = None
    else:
        computed_delta = len(cases) * calls_per_case - static_in_loop
        if computed_delta != runtime_minus_static:
            errors.append(
                "primary_harness.dynamic_expansion.runtime_minus_static: "
                f"declared {runtime_minus_static!r}, computed {computed_delta}"
            )
    expected_runtime = harness.get("expected_runtime_checks")
    if computed_delta is not None and expected_runtime != actual_static + computed_delta:
        errors.append(
            "primary_harness.expected_runtime_checks: "
            f"declared {expected_runtime!r}, computed {actual_static + computed_delta}"
        )
    function = expansion.get("function")
    if not isinstance(function, str) or f"def {function}(" not in harness_text:
        errors.append(
            f"primary_harness.dynamic_expansion.function: definition not found: {function!r}"
        )

    policies = manifest.get("classification_policy")
    if not isinstance(policies, dict):
        errors.append("classification_policy: expected an object")
    else:
        missing_policies = ALLOWED_CLASSIFICATIONS - set(policies)
        extra_policies = set(policies) - ALLOWED_CLASSIFICATIONS
        if missing_policies:
            errors.append(f"classification_policy: missing {sorted(missing_policies)}")
        if extra_policies:
            errors.append(f"classification_policy: unknown {sorted(extra_policies)}")

    entries = manifest.get("entries")
    if not isinstance(entries, list):
        errors.append("entries: expected a list")
        entries = []

    ids: list[Any] = []
    ordinals: list[Any] = []
    counts: Counter[str] = Counter()
    primary_method_by_entry: dict[str, str] = {}
    for index, entry in enumerate(entries):
        label = f"entries[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{label}: expected an object")
            continue
        entry_id = entry.get("id")
        ordinal = entry.get("runtime_ordinal")
        ids.append(entry_id)
        ordinals.append(ordinal)
        expected_id = f"LBN-{index + 1:03d}"
        if entry_id != expected_id:
            errors.append(f"{label}.id: expected {expected_id!r}, got {entry_id!r}")
        if ordinal != index + 1:
            errors.append(f"{label}.runtime_ordinal: expected {index + 1}, got {ordinal!r}")
        for field in ("public_claim", "expected"):
            if not isinstance(entry.get(field), str) or not entry[field]:
                errors.append(f"{label}.{field}: expected a non-empty string")

        source = entry.get("source")
        if not isinstance(source, dict):
            errors.append(f"{label}.source: expected an object")
        else:
            if not isinstance(source.get("section"), str) or not source["section"]:
                errors.append(f"{label}.source.section: expected a non-empty string")
            require_tokens(paper_text, source.get("anchors"), f"{label}.source", errors)

        primary = entry.get("primary")
        if not isinstance(primary, dict):
            errors.append(f"{label}.primary: expected an object")
            primary = {}
        primary_function = primary.get("function")
        primary_method = primary.get("method_family")
        if not isinstance(primary_function, str) or f"def {primary_function}(" not in harness_text:
            errors.append(
                f"{label}.primary.function: definition not found: {primary_function!r}"
            )
        if not isinstance(primary_method, str) or not primary_method:
            errors.append(f"{label}.primary.method_family: expected a non-empty string")
        else:
            primary_method_by_entry[str(entry_id)] = primary_method
        require_tokens(
            harness_text, primary.get("evidence_tokens"), f"{label}.primary", errors
        )

        secondary = entry.get("secondary")
        if not isinstance(secondary, dict):
            errors.append(f"{label}.secondary: expected an object")
            continue
        classification = secondary.get("classification")
        if classification not in ALLOWED_CLASSIFICATIONS:
            errors.append(
                f"{label}.secondary.classification: unknown value {classification!r}"
            )
            continue
        counts[classification] += 1
        secondary_path_value = secondary.get("path")
        secondary_method = secondary.get("method_family")
        confirms = secondary.get("confirms")

        if classification == "no_second_path":
            if secondary_path_value is not None or secondary_method is not None:
                errors.append(
                    f"{label}.secondary: no_second_path requires null path and method_family"
                )
            if confirms != "none":
                errors.append(f"{label}.secondary.confirms: expected 'none'")
            if secondary.get("evidence_tokens") != []:
                errors.append(
                    f"{label}.secondary.evidence_tokens: expected an empty list"
                )
            continue

        secondary_path = resolve_repo_path(
            repo_root, secondary_path_value, f"{label}.secondary.path", errors
        )
        secondary_text = (
            secondary_path.read_text(encoding="utf-8") if secondary_path else ""
        )
        if secondary_path_value == harness.get("path"):
            errors.append(f"{label}.secondary.path: must differ from primary harness")
        require_tokens(
            secondary_text,
            secondary.get("evidence_tokens"),
            f"{label}.secondary",
            errors,
        )
        if not isinstance(secondary_method, str) or not secondary_method:
            errors.append(f"{label}.secondary.method_family: expected a non-empty string")

        if classification == "independent_derivation":
            if confirms != "full_expectation":
                errors.append(
                    f"{label}.secondary.confirms: independent derivation must confirm full_expectation"
                )
            if secondary_method == primary_method:
                errors.append(
                    f"{label}.secondary.method_family: independent path duplicates primary method"
                )
        elif classification == "independent_value_only":
            if confirms != "numeric_value_only":
                errors.append(
                    f"{label}.secondary.confirms: expected 'numeric_value_only'"
                )
            if secondary_method == primary_method:
                errors.append(
                    f"{label}.secondary.method_family: independent value path duplicates primary method"
                )
            if not isinstance(secondary.get("semantic_dispute"), str) or not secondary[
                "semantic_dispute"
            ]:
                errors.append(
                    f"{label}.secondary.semantic_dispute: required for value-only coverage"
                )
        elif classification == "same_code_path":
            if confirms != "full_expectation":
                errors.append(f"{label}.secondary.confirms: expected 'full_expectation'")
            if secondary_method != primary_method:
                errors.append(
                    f"{label}.secondary.method_family: same-code path must match primary method"
                )
            if not isinstance(secondary.get("shared_implementation"), str) or not secondary[
                "shared_implementation"
            ]:
                errors.append(
                    f"{label}.secondary.shared_implementation: required for same-code path"
                )

    if len(ids) != len(set(ids)):
        errors.append("entries: duplicate ids")
    if len(ordinals) != len(set(ordinals)):
        errors.append("entries: duplicate runtime ordinals")
    if expected_runtime != len(entries):
        errors.append(
            f"entries: found {len(entries)}, primary harness declares {expected_runtime} runtime checks"
        )

    declared = manifest.get("declared_coverage")
    if not isinstance(declared, dict):
        errors.append("declared_coverage: expected an object")
        declared = {}
    if declared.get("total_runtime_checks") != len(entries):
        errors.append(
            "declared_coverage.total_runtime_checks: "
            f"declared {declared.get('total_runtime_checks')!r}, found {len(entries)} entries"
        )
    for classification in sorted(ALLOWED_CLASSIFICATIONS):
        if declared.get(classification) != counts[classification]:
            errors.append(
                f"declared_coverage.{classification}: "
                f"declared {declared.get(classification)!r}, found {counts[classification]}"
            )
    if sum(counts.values()) != len(entries):
        errors.append(
            f"declared_coverage: classifications sum to {sum(counts.values())}, "
            f"not {len(entries)}"
        )

    summary = {
        "status": "PASS" if not errors else "FAIL",
        "manifest": str(manifest.get("title", "")),
        "paper": str(manifest.get("paper", "")),
        "claim_map": str(manifest.get("claim_map", "")) if claim_map else None,
        "static_check_calls": actual_static,
        "runtime_checks": len(entries),
        "coverage": {
            classification: counts[classification]
            for classification in (
                "independent_derivation",
                "independent_value_only",
                "same_code_path",
                "no_second_path",
            )
        },
        "errors": errors,
    }
    return errors, summary


def main() -> int:
    args = parse_args()
    manifest_path = args.manifest.resolve()
    repo_root = args.repo_root.resolve()
    try:
        manifest = load_json(manifest_path)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"FAIL: cannot load manifest: {exc}", file=sys.stderr)
        return 2

    errors, summary = validate(manifest, repo_root)
    if args.json:
        print(json.dumps(summary, indent=2, sort_keys=True))
    elif errors:
        print(f"FAIL: {len(errors)} manifest validation error(s)")
        for error in errors:
            print(f"  - {error}")
    else:
        coverage = summary["coverage"]
        total = summary["runtime_checks"]
        print("PASS: release-evidence manifest is internally consistent")
        print(
            f"  primary harness: {summary['static_check_calls']} static check calls, "
            f"{total} declared runtime checks"
        )
        print(
            "  coverage: "
            f"{coverage['independent_derivation']} full independent; "
            f"{coverage['independent_value_only']} independent value only; "
            f"{coverage['same_code_path']} same-code-path only; "
            f"{coverage['no_second_path']} no second path"
        )
        print(f"  claim map: {summary['claim_map']}")
        print("  note: this validates declarations; run reproduce_all.py to execute evidence")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
