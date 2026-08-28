#!/usr/bin/env python3
"""Coupled guard for IDX-02 eta semantics and scale-covariant rank decisions."""

from __future__ import annotations

import ast
import contextlib
import importlib.util
import io
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
DECIDER = ROOT / "tests/decider/fibered_boundary_reduction_decider.py"
RANK_SOURCES = [
    ROOT / "tests/channel-swings/rb6_target_blind_spectral_grammar_probe.py",
    ROOT / "tests/rs_c2_physical_null_cone_restriction.py",
    ROOT / "tests/rs_bicomplex_physical_nullcone_curvature.py",
    ROOT / "tests/rs_bicomplex_spin95_connection_2form.py",
]


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise AssertionError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def extract_rank_helper(source: str):
    tree = ast.parse(source)
    node = next(
        item
        for item in tree.body
        if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef))
        and item.name == "scale_covariant_rank"
    )
    namespace = {"np": np, "ZERO_THRESHOLD": 1.0e-7}
    exec(compile(ast.Module(body=[node], type_ignores=[]), "<rank-helper>", "exec"), namespace)
    return namespace["scale_covariant_rank"]


def semantic_guard(source: str) -> bool:
    required = (
        'fork_from_reduction = "UNRESOLVED"',
        'eta_form_status="ACTUAL_FAMILY_UNCOMPUTED"',
        'reduction_term="INTEGRAL_AHAT_WEDGE_ETA_TILDE"',
    )
    forbidden = ('eta-form=0', 'fork_from_reduction = "GAUGE"')
    return all(token in source for token in required) and not any(
        token in source for token in forbidden
    )


def main() -> int:
    decider_source = DECIDER.read_text(encoding="utf-8")
    assert semantic_guard(decider_source)

    decider = load_module(DECIDER, "idx02_fibered_boundary_decider")
    with contextlib.redirect_stdout(io.StringIO()):
        result = decider.main()["res"]
    assert result["fork_from_reduction"] == "UNRESOLVED"
    assert result["eta_form_status"] == "ACTUAL_FAMILY_UNCOMPUTED"
    assert result["reduction_term"] == "INTEGRAL_AHAT_WEDGE_ETA_TILDE"
    assert not result["any_computable_three"]

    fixture = np.diag([1.0, 1.0e-8, 0.0])
    scales = (1.0e-12, 1.0, 1.0e12)
    mutation_catches = 0
    for path in RANK_SOURCES:
        source = path.read_text(encoding="utf-8")
        helper = extract_rank_helper(source)
        ranks = [helper(scale * fixture, 1.0e-7) for scale in scales]
        assert ranks == [1, 1, 1], (path, ranks)
        referenced_ranks = [
            helper(scale * fixture, 1.0e-7, scale) for scale in scales
        ]
        assert referenced_ranks == [1, 1, 1], (path, referenced_ranks)
        assert helper(np.zeros((3, 3)), 1.0e-7) == 0
        assert helper(np.diag([1.0, 2.0e-7]), 1.0e-7) == 2

        mutated = source.replace(
            "relative_tolerance * scale", "relative_tolerance", 1
        )
        mutant = extract_rank_helper(mutated)
        mutant_ranks = [mutant(scale * fixture, 1.0e-7) for scale in scales]
        assert len(set(mutant_ranks)) > 1, (path, mutant_ranks)
        mutation_catches += 1

    semantic_mutant = decider_source.replace(
        'fork_from_reduction = "UNRESOLVED"',
        'fork_from_reduction = "GAUGE"',
        1,
    )
    assert not semantic_guard(semantic_mutant)
    mutation_catches += 1

    legacy_ranks = [
        int(np.linalg.matrix_rank(scale * fixture, tol=1.0e-7))
        for scale in scales
    ]
    assert len(set(legacy_ranks)) > 1

    print("PASS: family eta-form output is explicitly uncomputed and fork is unresolved")
    print("PASS: all four rank helpers are invariant across 1e-12..1e12 rescaling")
    print("PASS: zero and near-threshold controls classify consistently")
    print(f"PASS: {mutation_catches}/5 planted semantic/absolute-rank regressions caught")
    print(f"INFO: legacy absolute-tolerance ranks across scales = {legacy_ranks}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
