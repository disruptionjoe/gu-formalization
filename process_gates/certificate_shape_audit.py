#!/usr/bin/env python3
"""Certificate-shape discovery gate (register P-C3; eleven-lens audit A8).

A certificate is only falsifiable if it has a failure path. The 2026-08-03
audit found 70 tracked certificates with no ``assert``, no ``raise``, and no
exit call: unconditional PASSes in every sweep, contradicting REPRODUCE.md's
"hard asserts ... exits nonzero if anything fails". This gate makes that
shape a discovery-time failure:

1. Every git-tracked ``tests/**.py`` swept by the harness must contain at
   least one of: an ``assert`` statement, a ``raise`` statement, a
   ``sys.exit``/``os._exit`` call, or unittest usage.
2. Library modules are exempt from (1) but are NOT certificates: they must
   be declared in ``scripts/reproduce_all.py``'s ``LIBRARY_MODULES`` and be
   excluded from harness discovery counting, so a module whose checks never
   execute is never counted as a passing certificate (audit A8:
   ``gen_sector_bridge.py``, imported by >100 certs, anchors never executed,
   counted as a pass).
3. The library allowlist is explicit here AND re-derived programmatically on
   every run (named seeds + any tracked tests module imported by >= 3 other
   tracked tests modules). Drift in either direction fails the gate, so the
   allowlist cannot silently grow or rot.

This is a process gate about certificate shape, not a mathematical check.
File contents are treated as data (AST only); nothing under tests/ is
executed by this gate.
"""

from __future__ import annotations

import ast
import importlib.util
import subprocess
import unittest
from pathlib import Path
from types import ModuleType

ROOT = Path(__file__).resolve().parents[1]
TESTS_DIR = ROOT / "tests"
HARNESS = ROOT / "scripts" / "reproduce_all.py"
SKIP_DIR_NAMES = {"__pycache__", ".cache", ".pytest_cache", ".git", "research-cycles"}

# Named library seeds (audit A8 / register P-C3 and P-H8): known shared
# engines that must never be counted as certificates regardless of the
# import-graph census.
NAMED_LIBRARY_SEEDS = frozenset({
    "tests/generation-sector/gen_sector_bridge.py",
    "tests/oq_rk1_cl95_explicit_rep.py",
})

# Import threshold above which a tracked tests module counts as a library.
LIBRARY_IMPORTER_THRESHOLD = 3

# The explicit allowlist. Must equal NAMED_LIBRARY_SEEDS union the modules
# detected programmatically (imported by >= LIBRARY_IMPORTER_THRESHOLD other
# tracked tests modules) — test_allowlist_matches_programmatic_detection
# enforces this, so edits here must be justified by the import graph.
LIBRARY_ALLOWLIST = frozenset({
    "tests/ahat_genus_y14_i16.py",
    "tests/channel-swings/actual_sym2_c14_orbit_probe.py",
    "tests/channel-swings/b5_curved_coflip_green_transport_probe.py",
    "tests/channel-swings/b5_native_rs_bv_hessian_lift_probe.py",
    "tests/channel-swings/full20_dewitt_loop_transport_probe.py",
    "tests/channel-swings/k149_sparse_differential_jet_api.py",
    "tests/channel-swings/k150_moving_selected_shiab_coordinate_adapter.py",
    "tests/channel-swings/k151_moving_distortion_pairing_adapter.py",
    "tests/channel-swings/k152_curved_metric_bridge_adapter.py",
    "tests/channel-swings/k153_null_fivefold_first_lower_adapter.py",
    "tests/channel-swings/k154_null_fivefold_second_lower_adapter.py",
    "tests/channel-swings/p77_real_index_twin.py",
    "tests/channel-swings/k77_exact_bank_api.py",
    "tests/channel-swings/nguyen_c1c2_real_form_probe.py",
    "tests/channel-swings/unified_source_datum_packet_v0_probe.py",
    "tests/channel-swings/uniformity_execution_probe.py",
    "tests/channel-swings/w177_ym_residual_and_mode_closure_probe.py",
    "tests/generation-sector/gen_sector_bridge.py",
    "tests/hessian-z3/criticality_torsion_lambda_epsilon.py",
    "tests/lib/exact_gimmel_derivatives.py",
    "tests/oq_rk1_cl95_explicit_rep.py",
    "tests/rs_bicomplex_gimmel_curvature_physical_nullplane.py",
    "tests/rs_clifford_projector_model.py",
    "tests/shiab_b5_krein_mirror_orbit_reduction.py",
    "tests/shiab_b5_native_packet_contract.py",
    "tests/shiab_b5_observer_symbol_multiplicity_matrix.py",
    "tests/shiab_family_basis.py",
})


def tracked_tests_files() -> list[str]:
    """Repo-relative slash paths of git-tracked certificate-scope tests files."""
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
        parts = Path(rel).parts
        if Path(rel).name == "__init__.py":
            continue
        if any(part in SKIP_DIR_NAMES for part in parts):
            continue
        files.append(Path(rel).as_posix())
    return sorted(files)


def parse(rel: str) -> ast.AST:
    return ast.parse((ROOT / rel).read_text(encoding="utf-8"), filename=rel)


def has_failure_path(tree: ast.AST) -> bool:
    """True iff the module contains an assert, a raise, an exit call, or
    unittest usage — i.e. some path on which it can exit nonzero."""
    for node in ast.walk(tree):
        if isinstance(node, (ast.Assert, ast.Raise)):
            return True
        if isinstance(node, ast.Call):
            fn = node.func
            if (
                isinstance(fn, ast.Attribute)
                and fn.attr in ("exit", "_exit")
                and isinstance(fn.value, ast.Name)
                and fn.value.id in ("sys", "os")
            ):
                return True
            if isinstance(fn, ast.Name) and fn.id in ("exit", "quit"):
                return True
        if isinstance(node, ast.Import):
            if any(alias.name.split(".")[0] == "unittest" for alias in node.names):
                return True
        if isinstance(node, ast.ImportFrom):
            if (node.module or "").split(".")[0] == "unittest":
                return True
    return False


def imported_module_stems(tree: ast.AST) -> set[str]:
    stems: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            stems.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            stems.add(node.module.split(".")[0])
    return stems


def detect_library_modules(files: list[str]) -> tuple[frozenset[str], list[str]]:
    """Return (library modules by import census, ambiguity errors).

    A tracked tests module is a library when >= LIBRARY_IMPORTER_THRESHOLD
    other tracked tests modules import it by stem. Certificates import these
    engines via sys.path manipulation, so stem-level matching is the honest
    resolution; a stem shared by several tracked files that is actually
    imported is ambiguous and must fail loudly rather than guess.
    """
    by_stem: dict[str, list[str]] = {}
    for rel in files:
        by_stem.setdefault(Path(rel).stem, []).append(rel)

    importer_count: dict[str, set[str]] = {}
    for rel in files:
        try:
            stems = imported_module_stems(parse(rel))
        except SyntaxError:
            continue  # reported separately by the shape test
        for stem in stems:
            if stem in by_stem and rel not in by_stem[stem]:
                importer_count.setdefault(stem, set()).add(rel)

    errors: list[str] = []
    detected: set[str] = set()
    for stem, importers in importer_count.items():
        if len(importers) >= LIBRARY_IMPORTER_THRESHOLD:
            candidates = by_stem[stem]
            if len(candidates) > 1:
                errors.append(
                    f"ambiguous library stem {stem!r}: {candidates} — "
                    "resolve by renaming before allowlisting"
                )
            else:
                detected.add(candidates[0])
    return frozenset(detected), errors


def load_harness() -> ModuleType:
    spec = importlib.util.spec_from_file_location("gu_reproduce_all_shape", HARNESS)
    if spec is None or spec.loader is None:
        raise AssertionError(f"could not load {HARNESS}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CertificateShapeAudit(unittest.TestCase):
    maxDiff = None

    def test_allowlist_matches_programmatic_detection(self) -> None:
        files = tracked_tests_files()
        self.assertGreaterEqual(len(files), 1)
        detected, errors = detect_library_modules(files)
        self.assertEqual([], errors)
        expected = frozenset(NAMED_LIBRARY_SEEDS) | detected
        self.assertEqual(
            sorted(expected),
            sorted(LIBRARY_ALLOWLIST),
            "LIBRARY_ALLOWLIST is out of sync with the named seeds + "
            f">= {LIBRARY_IMPORTER_THRESHOLD}-importer census; update the "
            "explicit list to match the import graph",
        )

    def test_harness_declares_the_same_library_modules(self) -> None:
        module = load_harness()
        declared = getattr(module, "LIBRARY_MODULES", None)
        self.assertIsNotNone(
            declared,
            "scripts/reproduce_all.py must declare LIBRARY_MODULES so library "
            "engines are excluded from certificate discovery counting",
        )
        self.assertEqual(sorted(LIBRARY_ALLOWLIST), sorted(declared))

    def test_harness_discovery_excludes_library_modules(self) -> None:
        module = load_harness()
        discovered = {
            Path(path).resolve().relative_to(ROOT).as_posix()
            for path in module.discover([module.TESTS_DIR], tracked_only=True)
        }
        self.assertGreaterEqual(len(discovered), 1)
        counted_libraries = sorted(discovered & set(LIBRARY_ALLOWLIST))
        self.assertEqual(
            [],
            counted_libraries,
            "library modules are being counted as certificates by the harness",
        )

    def test_every_swept_certificate_has_a_failure_path(self) -> None:
        files = tracked_tests_files()
        violations: list[str] = []
        unparseable: list[str] = []
        for rel in files:
            if rel in LIBRARY_ALLOWLIST:
                continue
            try:
                tree = parse(rel)
            except SyntaxError as exc:
                unparseable.append(f"{rel}: {exc}")
                continue
            if not has_failure_path(tree):
                violations.append(rel)
        self.assertEqual([], unparseable)
        self.assertEqual(
            [],
            violations,
            f"{len(violations)} swept certificate(s) have no failure path "
            "(no assert/raise/exit/unittest) — unconditional PASSes",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
