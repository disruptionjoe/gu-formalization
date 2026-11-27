"""Read-only progress projection: freshness is file custody, never a verdict."""
from copy import deepcopy
import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import yaml

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("research_context", ROOT / "scripts/research_context.py")
context = importlib.util.module_from_spec(spec)
spec.loader.exec_module(context)


class ProgressMap(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / "evidence.md").write_text("held evidence\n")
        (self.root / "one-cell.md").write_text("distinct owner\n")
        cell = {"attributed_status": "conditional owner status", "closed": "named scope only",
                "open": "physical transfer", "shared_missing_ref": "evidence.md#shared",
                "cheapest_next": "declared suggestion", "evidence_refs": ["evidence.md#result"]}
        self.data = {"schema_version": "1.0", "basis_revision": "a" * 40,
                     "scope": "test linked view", "assumptions_ref": "evidence.md#shared",
                     "dependencies": [{"ref": name, "sha256": hashlib.sha256((self.root / name).read_bytes()).hexdigest()}
                                      for name in ("evidence.md", "one-cell.md")],
                     "pillars": [{"id": name, "cells": {layer: deepcopy(cell) for layer in context.PROGRESS_LAYERS}}
                                 for name in context.PROGRESS_PILLARS]}
        self.data["pillars"][0]["cells"]["source"]["evidence_refs"].append("one-cell.md#proof")

    def project(self, data=None):
        return context.progress_projection(self.data if data is None else data, root=self.root, revision="b" * 40)

    def cells(self, view):
        return [c for p in view["pillars"] for c in p["cells"].values()]

    def test_eighteen_attributed_cells_not_scientific_verification(self):
        view = self.project()
        self.assertEqual(len(self.cells(view)), 18)
        self.assertTrue(all(c["freshness"] == "hash_current" for c in self.cells(view)))
        self.assertEqual(view["basis_revision"], "a" * 40)
        self.assertEqual(view["checked_out_revision"], "b" * 40)
        self.assertTrue(all(c["attributed_status"] == "conditional owner status" for c in self.cells(view)))
        self.assertIn("not scientific applicability", view["ceiling"])

    def test_changed_dependency_invalidates_only_linked_cells(self):
        (self.root / "one-cell.md").write_text("changed conclusion\n")
        view = self.project()
        self.assertEqual(view["freshness"], "needs_recheck")
        stale = [c for c in self.cells(view) if c["freshness"] == "needs_recheck"]
        self.assertEqual(len(stale), 1)
        self.assertEqual(stale[0]["recheck_refs"], ["one-cell.md#proof"])

    def test_unused_stale_pin_flags_map_without_changing_cells(self):
        self.data["pillars"][0]["cells"]["source"]["evidence_refs"].remove("one-cell.md#proof")
        (self.root / "one-cell.md").write_text("changed but unlinked\n")
        view = self.project()
        self.assertEqual(view["freshness"], "needs_recheck")
        self.assertTrue(all(c["freshness"] == "hash_current" for c in self.cells(view)))

    def test_missing_or_unreadable_dependency_is_not_current(self):
        (self.root / "evidence.md").unlink()
        self.assertTrue(all(c["freshness"] == "needs_recheck" for c in self.cells(self.project())))
        (self.root / "evidence.md").mkdir()
        self.assertEqual(self.project()["freshness"], "needs_recheck")

    def test_unpinned_and_malformed_hash_require_recheck(self):
        for mutate in (lambda d: d["dependencies"].pop(),
                       lambda d: d["dependencies"][1].pop("sha256"),
                       lambda d: d["dependencies"][1].update(sha256="not-a-hash")):
            data = deepcopy(self.data)
            mutate(data)
            self.assertEqual(self.project(data)["pillars"][0]["cells"]["source"]["freshness"], "needs_recheck")

    def test_complete_distinct_pillars_and_layers_required(self):
        mutations = [lambda d: d["pillars"].pop(),
                     lambda d: d["pillars"][1].update(id=d["pillars"][0]["id"]),
                     lambda d: d["pillars"][0]["cells"].pop("class"),
                     lambda d: d["pillars"][0]["cells"].update(extra={}),
                     lambda d: d["pillars"][0]["cells"]["source"].update(evidence_refs=[])]
        for mutate in mutations:
            data = deepcopy(self.data)
            mutate(data)
            with self.assertRaises(ValueError):
                self.project(data)

    def test_reference_escape_is_rejected_before_dependency_read(self):
        for ref in ("../outside.md", "/tmp/outside.md", "a/../../outside.md", "file://outside", "a\\outside"):
            for field in ("evidence", "dependency"):
                data = deepcopy(self.data)
                if field == "evidence":
                    data["pillars"][0]["cells"]["source"]["evidence_refs"] = [ref]
                else:
                    data["dependencies"][0]["ref"] = ref
                with self.subTest(ref=ref, field=field), self.assertRaises(ValueError):
                    self.project(data)

    def test_symlink_escape_is_rejected(self):
        with tempfile.TemporaryDirectory() as outside:
            external = Path(outside) / "secret.md"
            external.write_text("outside\n")
            (self.root / "escape.md").symlink_to(external)
            self.data["pillars"][0]["cells"]["source"]["evidence_refs"] = ["escape.md#ignored"]
            with self.assertRaises(ValueError):
                self.project()

    def test_cli_read_only_without_loading_unrelated_state_or_executing_verifiers(self):
        path = self.root / context.PROGRESS_MAP
        path.parent.mkdir(parents=True)
        path.write_text(json.dumps(self.data))
        before = {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        output = io.StringIO()
        head = subprocess.CompletedProcess([], 0, stdout="b" * 40 + "\n", stderr="")
        with patch.object(context, "ROOT", self.root), patch.object(context.subprocess, "run", return_value=head) as run, contextlib.redirect_stdout(output):
            self.assertEqual(context.main(["--progress-map"]), 0)
        run.assert_called_once_with(["git", "rev-parse", "HEAD"], cwd=self.root, text=True, capture_output=True, check=False)
        after = {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(before, after)
        parsed = yaml.safe_load(output.getvalue().split("```yaml\n")[1].split("```", 1)[0])
        self.assertEqual(parsed["progress_map"]["freshness"], "hash_current")

    def test_existing_reuse_cli_still_available_and_flags_are_exclusive(self):
        index = self.root / context.REUSE_INDEX
        index.parent.mkdir(parents=True)
        index.write_text(json.dumps({"schema_version": "1.0", "coverage": "fixture", "entries": []}))
        with patch.object(context, "ROOT", self.root), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(context.main(["--reuse", "missing"]), 0)
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            context.main(["--progress-map", "--claim", "SC-ACT-01"])

    def test_actual_map_schema_and_all_reference_paths(self):
        data = json.loads((ROOT / context.PROGRESS_MAP).read_text())
        view = context.progress_projection(data, root=ROOT)
        self.assertEqual(len(self.cells(view)), 18)
        # Owner files may change during integration: that must remain a recheck,
        # never a test that silently rewrites pins to make the view appear fresh.
        self.assertTrue(all(c["freshness"] in ("hash_current", "needs_recheck") for c in self.cells(view)))
        self.assertTrue(all(c["evidence_refs"] for c in self.cells(view)))


if __name__ == "__main__":
    unittest.main()
