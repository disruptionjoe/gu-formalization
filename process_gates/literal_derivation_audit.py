#!/usr/bin/env python3
"""Literal-derivation gate (register P-H10; eleven-lens audit cert-lens).

The audit found certificates whose every check merely *restates* literals
assigned earlier in the same file — checks that cannot fail without editing
the file, in a certificate that claims to *derive* its verdict
(``pin14_smith_degree_gate.py``: all seven checks restated constants
assigned ten lines above; ``gu-forces/verify_legb_intersection.py`` shared
the pattern). Both were rewritten on 2026-08-03 to derive what they assert;
this gate keeps the pattern from returning. There is NO allowlist: a flagged
certificate must be rewritten to derive what it asserts.

Definition enforced here (deliberately narrow, so genuine derivations —
even pure-Python ones — are never flagged):

* A **check site** is an ``assert`` statement, or a call to a same-file
  check helper — a function whose body asserts / raises / exits, or that
  *records* failures into a module-level accumulator (the ``FAILS.append``
  idiom). An assert that merely couples such an accumulator to the exit
  code (``assert not FAILS``) is the recorder sites' coupler, not an
  independent site, and accumulator names never fold.
* A site is a **restatement** when its condition operands fold to constants
  by *shallow* propagation only: literals, containers of folded values,
  arithmetic/boolean/comparison/subscript/conditional expressions over
  folded values, and module-level names bound to folded expressions on an
  unconditionally-reached path. **No function or method call of any kind
  and no comprehension is folded** — one call is one derivation step, which
  is enough to leave the restatement class.
* A certificate is **flagged** when it has at least one check site and
  every one of its check sites is a restatement: nothing in the file's
  verdict depends on anything beyond re-evaluating its own literals.

This is a process gate about certificate shape; file contents are treated
as data (AST only) and nothing under tests/ is executed.
"""

from __future__ import annotations

import ast
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIR_NAMES = {"__pycache__", ".cache", ".pytest_cache", ".git", "hourly-cycles"}


def tracked_tests_files() -> list[str]:
    proc = subprocess.run(
        ["git", "ls-files", "-z", "--", "tests"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        raise AssertionError(proc.stderr.strip() or "git ls-files failed")
    files = []
    for rel in proc.stdout.split("\0"):
        if not rel or not rel.endswith(".py"):
            continue
        if Path(rel).name == "__init__.py":
            continue
        if any(part in SKIP_DIR_NAMES for part in Path(rel).parts):
            continue
        files.append(Path(rel).as_posix())
    return sorted(files)


def _is_exit_call(node: ast.Call) -> bool:
    fn = node.func
    if (
        isinstance(fn, ast.Attribute)
        and fn.attr in ("exit", "_exit")
        and isinstance(fn.value, ast.Name)
        and fn.value.id in ("sys", "os")
    ):
        return True
    return isinstance(fn, ast.Name) and fn.id in ("exit", "quit")


ACCUMULATOR_METHODS = {"append", "add", "extend", "insert", "update"}


def check_helpers(tree: ast.Module) -> set[str]:
    """Same-file functions that fail or record failure: assert / raise /
    exit, or a mutating method call on a non-local (module-level) name —
    the ``FAILS.append`` recorder idiom."""
    helpers: set[str] = set()
    for node in tree.body:
        if not isinstance(node, ast.FunctionDef):
            continue
        local_names = {a.arg for a in node.args.args}
        for inner in ast.walk(node):
            if isinstance(inner, (ast.Assert, ast.Raise)):
                helpers.add(node.name)
                break
            if isinstance(inner, ast.Call):
                if _is_exit_call(inner):
                    helpers.add(node.name)
                    break
                fn = inner.func
                if (
                    isinstance(fn, ast.Attribute)
                    and fn.attr in ACCUMULATOR_METHODS
                    and isinstance(fn.value, ast.Name)
                    and fn.value.id not in local_names
                ):
                    helpers.add(node.name)
                    break
    return helpers


def accumulator_names(tree: ast.Module) -> set[str]:
    """Names mutated through method calls anywhere in the module. Their
    contents are runtime-dependent, so they never fold, and an assert over
    only such names is a recorder coupler rather than an independent site."""
    names: set[str] = set()
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr in ACCUMULATOR_METHODS
            and isinstance(node.func.value, ast.Name)
        ):
            names.add(node.func.value.id)
    return names


class ShallowFolder:
    """Shallow constant propagation over a module body.

    ``env`` maps a name to True when its current binding folds to a constant
    through literal-only expressions on an unconditionally-reached path.
    Calls, comprehensions, and bindings guarded by non-folded conditions are
    never folded. Conservative toward "derived": anything unrecognized is
    treated as non-foldable, so the gate under-flags rather than over-flags.
    """

    def __init__(self, tree: ast.Module, helpers: set[str], accumulators: set[str]) -> None:
        self.helpers = helpers
        self.accumulators = accumulators
        self.env: dict[str, bool] = {}
        # (lineno, description, is_restatement)
        self.sites: list[tuple[int, str, bool]] = []
        self._walk(tree.body, cond_folded=True)

    # -- statement walk ----------------------------------------------------

    def _walk(self, stmts, cond_folded: bool) -> None:
        for stmt in stmts:
            if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                continue
            elif isinstance(stmt, (ast.Import, ast.ImportFrom)):
                for alias in stmt.names:
                    name = alias.asname or alias.name.split(".")[0]
                    self.env[name] = False
            elif isinstance(stmt, ast.Assign):
                value = self._folds(stmt.value) and cond_folded
                for target in stmt.targets:
                    self._bind(target, value)
            elif isinstance(stmt, ast.AnnAssign) and stmt.value is not None:
                self._bind(stmt.target, self._folds(stmt.value) and cond_folded)
            elif isinstance(stmt, ast.AugAssign):
                if isinstance(stmt.target, ast.Name):
                    self.env[stmt.target.id] = (
                        self.env.get(stmt.target.id, False)
                        and self._folds(stmt.value)
                        and cond_folded
                    )
            elif isinstance(stmt, ast.Assert):
                names = {
                    n.id for n in ast.walk(stmt.test) if isinstance(n, ast.Name)
                }
                if names and names <= self.accumulators:
                    continue  # recorder coupler (assert not FAILS), not a site
                self.sites.append(
                    (stmt.lineno, "assert", self._folds(stmt.test) and cond_folded)
                )
            elif isinstance(stmt, ast.Expr):
                self._expr_stmt(stmt.value, cond_folded)
            elif isinstance(stmt, ast.If):
                branch = cond_folded and self._folds(stmt.test)
                self._walk(stmt.body, branch)
                self._walk(stmt.orelse, branch)
            elif isinstance(stmt, ast.While):
                branch = cond_folded and self._folds(stmt.test)
                self._walk(stmt.body, branch)
                self._walk(stmt.orelse, branch)
            elif isinstance(stmt, ast.For):
                iter_folds = self._folds(stmt.iter)  # calls => False
                self._bind(stmt.target, iter_folds and cond_folded)
                self._walk(stmt.body, cond_folded and iter_folds)
                self._walk(stmt.orelse, cond_folded)
            elif isinstance(stmt, ast.With):
                for item in stmt.items:
                    if item.optional_vars is not None:
                        self._bind(item.optional_vars, False)
                self._walk(stmt.body, cond_folded)
            elif isinstance(stmt, ast.Try):
                self._walk(stmt.body, cond_folded)
                for handler in stmt.handlers:
                    if handler.name:
                        self.env[handler.name] = False
                    self._walk(handler.body, False)
                self._walk(stmt.orelse, cond_folded)
                self._walk(stmt.finalbody, cond_folded)
            # Raise/Pass/Break/Continue/Return/Delete/Global: no binding effect.

    def _expr_stmt(self, value, cond_folded: bool) -> None:
        if not isinstance(value, ast.Call):
            return
        fn = value.func
        if isinstance(fn, ast.Name) and fn.id in self.helpers:
            operands = [
                a for a in value.args
                if not (isinstance(a, ast.Constant) and isinstance(a.value, str))
            ] + [kw.value for kw in value.keywords]
            status = cond_folded and all(self._folds(a) for a in operands)
            self.sites.append((value.lineno, f"{fn.id}(...)", status))

    def _bind(self, target, folded: bool) -> None:
        if isinstance(target, ast.Name):
            self.env[target.id] = folded
        elif isinstance(target, (ast.Tuple, ast.List)):
            for elt in target.elts:
                self._bind(elt, folded)
        elif isinstance(target, ast.Starred):
            self._bind(target.value, folded)
        # subscript/attribute targets mutate a container: taint its base name
        elif isinstance(target, ast.Subscript) and isinstance(target.value, ast.Name):
            self.env[target.value.id] = False
        elif isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name):
            self.env[target.value.id] = False

    # -- expression fold ---------------------------------------------------

    def _folds(self, node) -> bool:
        if node is None:
            return True
        if isinstance(node, ast.Constant):
            return True
        if isinstance(node, ast.Name):
            if node.id in self.accumulators:
                return False  # runtime-mutated: never a restatement operand
            if node.id in self.env:
                return self.env[node.id]
            return node.id in ("True", "False", "None")
        if isinstance(node, (ast.Tuple, ast.List, ast.Set)):
            return all(self._folds(e) for e in node.elts)
        if isinstance(node, ast.Dict):
            return all(self._folds(k) for k in node.keys if k is not None) and \
                all(self._folds(v) for v in node.values)
        if isinstance(node, ast.BinOp):
            return self._folds(node.left) and self._folds(node.right)
        if isinstance(node, ast.UnaryOp):
            return self._folds(node.operand)
        if isinstance(node, ast.BoolOp):
            return all(self._folds(v) for v in node.values)
        if isinstance(node, ast.Compare):
            return self._folds(node.left) and all(self._folds(c) for c in node.comparators)
        if isinstance(node, ast.IfExp):
            return self._folds(node.test) and self._folds(node.body) and \
                self._folds(node.orelse)
        if isinstance(node, ast.Subscript):
            return self._folds(node.value) and self._folds(node.slice)
        if isinstance(node, ast.Slice):
            return all(self._folds(p) for p in (node.lower, node.upper, node.step))
        if isinstance(node, ast.Starred):
            return self._folds(node.value)
        # Calls, comprehensions, attributes, f-strings, lambdas, walrus, ...:
        # at least one genuine computation/lookup step => not a restatement.
        return False


def analyze(source: str, filename: str) -> tuple[int, list[tuple[int, str]]]:
    """Return (check_site_count, restatement_sites) for one certificate."""
    tree = ast.parse(source, filename=filename)
    folder = ShallowFolder(tree, check_helpers(tree), accumulator_names(tree))
    restatements = [(line, desc) for line, desc, folded in folder.sites if folded]
    return len(folder.sites), restatements


def flagged_certificates(files: list[str]) -> dict[str, list[tuple[int, str]]]:
    flagged: dict[str, list[tuple[int, str]]] = {}
    for rel in files:
        try:
            source = (ROOT / rel).read_text(encoding="utf-8")
            count, restatements = analyze(source, rel)
        except SyntaxError:
            continue  # certificate_shape_audit reports unparseable files
        if count >= 1 and len(restatements) == count:
            flagged[rel] = restatements
    return flagged


# Synthetic calibration sources. These keep the gate itself falsifiable: if
# the propagation machinery rots, these tests fail before the tree scan runs.

TAUTOLOGY_EXAMPLE = """\
def check(label, condition, detail):
    print(label, detail)
    if not condition:
        raise AssertionError(label)

target = 14
left = 0
shifted = target - 1
check("endpoints", left == 0, "vanishing")
check("shift", shifted == 13, "degree bookkeeping")
check("residue", shifted % 8 in {0, 1, 3, 4, 5, 7}, "exponent table")
"""

ACCUMULATOR_TAUTOLOGY_EXAMPLE = """\
FAILS = []
def ck(n, c):
    print(("PASS" if c else "FAIL"), n)
    if not c:
        FAILS.append(n)

table = {"A": -42, "B": -38}
ck("gap", table["B"] - table["A"] == 4)
ck("midpoint", -40 == (table["A"] + table["B"]) // 2)
assert not FAILS
"""

RECORDER_WITH_DERIVATION_EXAMPLE = """\
FAILS = []
def ck(n, c):
    print(("PASS" if c else "FAIL"), n)
    if not c:
        FAILS.append(n)

def carrier(cell):
    return "A" if cell == ("full", "present") else "B"

table = {"A": -42, "B": -38}
ck("gap", table["B"] - table["A"] == 4)
ck("carrier map", carrier(("full", "present")) == "A")
assert not FAILS
"""

DERIVED_EXAMPLE = """\
import sympy

def check(label, condition):
    if not condition:
        raise AssertionError(label)

x = sympy.Integer(14)
check("shift", x - 1 == 13)
assert x % 2 == 0
"""

PURE_PYTHON_DERIVATION_EXAMPLE = """\
def check(label, condition):
    if not condition:
        raise AssertionError(label)

def dim(D, deriv):
    return (D - deriv) / 2

D = 4
check("scalar dimension", dim(D, 2) == 1.0)
assert len([x for x in range(D)]) == D
"""


class LiteralDerivationAudit(unittest.TestCase):
    maxDiff = None

    def test_analyzer_flags_the_restatement_shapes(self) -> None:
        count, restatements = analyze(TAUTOLOGY_EXAMPLE, "<tautology>")
        self.assertEqual(3, count)
        self.assertEqual(count, len(restatements))

        # recorder sites are sites; the terminal `assert not FAILS` is their
        # coupler, not a site — the ck calls carry the restatement verdict
        count, restatements = analyze(ACCUMULATOR_TAUTOLOGY_EXAMPLE, "<accumulator>")
        self.assertEqual(2, count)
        self.assertEqual(count, len(restatements))

    def test_analyzer_passes_derivation_shapes(self) -> None:
        count, restatements = analyze(DERIVED_EXAMPLE, "<derived>")
        self.assertEqual(2, count)
        self.assertEqual([], restatements)

        count, restatements = analyze(PURE_PYTHON_DERIVATION_EXAMPLE, "<pure-python>")
        self.assertEqual(2, count)
        self.assertEqual([], restatements)

        # a recorder file where at least one recorded check genuinely
        # computes (one call = one derivation step) is not flagged, even
        # though another of its checks restates the same-file table
        count, restatements = analyze(RECORDER_WITH_DERIVATION_EXAMPLE, "<recorder>")
        self.assertEqual(2, count)
        self.assertEqual(1, len(restatements))

    def test_no_tracked_certificate_is_a_literal_restatement(self) -> None:
        files = tracked_tests_files()
        self.assertGreaterEqual(len(files), 1)
        flagged = flagged_certificates(files)
        detail = {
            rel: [f"line {line}: {desc}" for line, desc in sites]
            for rel, sites in sorted(flagged.items())
        }
        self.assertEqual(
            {},
            detail,
            "certificate(s) whose every check restates same-file literals — "
            "rewrite them to derive what they assert (no allowlist)",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
