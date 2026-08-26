#!/usr/bin/env python3
"""Reject numeric assertions that only read back an unchanged typed literal.

P-M6 identified certificate assertions whose apparent evidence value was
assigned as a numeric literal and never moved by computation.  Boolean/event
counters are a different class: a zero initializer is legitimate when later
execution updates it before the assertion.  Irreducible model premises are
also legitimate when they enter through an explicit declared-input call.

This gate uses the AST rather than line numbers.  It fails on an asserted name
when that name's matching numeric literal assignment is its last write in the
file.  Derived expressions, explicit declared-input calls, and subsequently
mutated counters are therefore outside the defect class by construction.
"""

from __future__ import annotations

import ast
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def numeric_literal(node: ast.AST) -> int | float | complex | None:
    if (
        isinstance(node, ast.Constant)
        and isinstance(node.value, (int, float, complex))
        and not isinstance(node.value, bool)
    ):
        return node.value
    if (
        isinstance(node, ast.UnaryOp)
        and isinstance(node.op, (ast.UAdd, ast.USub))
        and isinstance(node.operand, ast.Constant)
        and isinstance(node.operand.value, (int, float, complex))
        and not isinstance(node.operand.value, bool)
    ):
        return +node.operand.value if isinstance(node.op, ast.UAdd) else -node.operand.value
    return None


def target_names(node: ast.AST) -> set[str]:
    return {child.id for child in ast.walk(node) if isinstance(child, ast.Name)}


SCOPE_NODES = (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Lambda)


def nodes_in_scope(scope: ast.AST) -> list[ast.AST]:
    """Return descendants in one lexical scope without entering child scopes."""
    nodes: list[ast.AST] = []
    stack = list(ast.iter_child_nodes(scope))
    while stack:
        node = stack.pop()
        if isinstance(node, SCOPE_NODES):
            continue
        nodes.append(node)
        stack.extend(ast.iter_child_nodes(node))
    return nodes


def scope_literal_only_numeric_assertions(scope: ast.AST) -> set[tuple[str, int | float | complex]]:
    scope_nodes = nodes_in_scope(scope)
    literal_assignments: dict[str, list[tuple[int, int | float | complex]]] = {}
    writes: dict[str, list[int]] = {}

    for node in scope_nodes:
        if isinstance(node, ast.Assign):
            targets = node.targets
            value = node.value
        elif isinstance(node, ast.AnnAssign):
            targets = [node.target]
            value = node.value
        elif isinstance(node, ast.AugAssign):
            for name in target_names(node.target):
                writes.setdefault(name, []).append(node.lineno)
            continue
        elif isinstance(node, (ast.For, ast.AsyncFor)):
            for name in target_names(node.target):
                writes.setdefault(name, []).append(node.lineno)
            continue
        elif isinstance(node, ast.NamedExpr):
            for name in target_names(node.target):
                writes.setdefault(name, []).append(node.lineno)
            continue
        else:
            continue

        literal = numeric_literal(value)
        for target in targets:
            for name in target_names(target):
                writes.setdefault(name, []).append(node.lineno)
                if literal is not None:
                    literal_assignments.setdefault(name, []).append((node.lineno, literal))

    hits: set[tuple[str, int | float | complex]] = set()
    for node in scope_nodes:
        if not isinstance(node, ast.Assert):
            continue
        for comparison in ast.walk(node.test):
            if not (
                isinstance(comparison, ast.Compare)
                and len(comparison.ops) == 1
                and len(comparison.comparators) == 1
            ):
                continue
            pairs = (
                (comparison.left, comparison.comparators[0]),
                (comparison.comparators[0], comparison.left),
            )
            for name_node, literal_node in pairs:
                literal = numeric_literal(literal_node)
                if not isinstance(name_node, ast.Name) or literal is None:
                    continue
                matches = [
                    line
                    for line, assigned in literal_assignments.get(name_node.id, [])
                    if assigned == literal and line < node.lineno
                ]
                if matches and not any(
                    line > max(matches) and line < node.lineno
                    for line in writes.get(name_node.id, [])
                ):
                    hits.add((name_node.id, literal))
    return hits


def literal_only_numeric_assertions(source: str) -> set[tuple[str, int | float | complex]]:
    tree = ast.parse(source)
    hits: set[tuple[str, int | float | complex]] = set()
    for scope in (node for node in ast.walk(tree) if isinstance(node, SCOPE_NODES)):
        hits.update(scope_literal_only_numeric_assertions(scope))
    return hits


def tracked_test_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "tests/*.py", "tests/**/*.py"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return sorted({ROOT / line for line in result.stdout.splitlines() if line})


class DirectNumericAssertionCustody(unittest.TestCase):
    def test_planted_defect_is_detected(self) -> None:
        source = "value = 3\nassert value == 3\n"
        self.assertEqual({("value", 3)}, literal_only_numeric_assertions(source))

    def test_mutated_counter_and_derived_value_are_not_defects(self) -> None:
        source = "count = 0\ncount += 1\nassert count > 0\ndim = len((1, 2, 3))\nassert dim == 3\n"
        self.assertEqual(set(), literal_only_numeric_assertions(source))

    def test_declared_input_call_is_not_presented_as_a_derivation(self) -> None:
        source = (
            "ambient = declared_numeric_input('dimension', 4, 'four-dimensional branch')\n"
            "bound = ambient\nassert bound <= 4\n"
        )
        self.assertEqual(set(), literal_only_numeric_assertions(source))

    def test_same_name_in_child_scope_does_not_mask_module_defect(self) -> None:
        source = (
            "value = 3\nassert value == 3\n"
            "def child():\n    value = 0\n    value += 1\n    return value\n"
        )
        self.assertEqual({("value", 3)}, literal_only_numeric_assertions(source))

    def test_tracked_certificates_have_no_literal_only_numeric_assertions(self) -> None:
        defects: list[str] = []
        for path in tracked_test_files():
            hits = literal_only_numeric_assertions(path.read_text(encoding="utf-8"))
            defects.extend(
                f"{path.relative_to(ROOT)}:{name}={value!r}"
                for name, value in sorted(hits, key=lambda item: (item[0], repr(item[1])))
            )
        self.assertEqual([], defects, "literal-only numeric assertion dependencies:\n  " + "\n  ".join(defects))

    def test_p_m6_sites_carry_native_derivation_or_declared_input(self) -> None:
        expected = {
            "tests/W44_H58_rs_power_counting.py": "declared_numeric_input",
            "tests/W59_path3_E_nogo.py": "num_invariant_subspaces = len(invariant_dims)",
            "tests/channel-swings/source_domain_selector_prongB_probe.py":
                "phys_inequiv_dim_lower_bound = int(rho_slice_is_injective)",
            "tests/decider/fibered_boundary_reduction_decider.py": "1 + (-1) ** 6",
        }
        for relative, witness in expected.items():
            self.assertIn(witness, (ROOT / relative).read_text(encoding="utf-8"), relative)


if __name__ == "__main__":
    unittest.main(verbosity=2)
