#!/usr/bin/env python3
"""Validate lab/process/path-dependencies.yaml and regenerate its mermaid view.

WHY THIS FILE EXISTS.  layer0-fork-registry.yaml records WHAT the forks and
homonyms are.  It does not record the causal chain that makes a given check
worth doing, so an agent meeting "check whether this is on (9,5)" or "is this
parity spectral or kinematic?" sees an arbitrary rule instead of a consequence.
Rules without their chain get skipped or cargo-culted.  path-dependencies.yaml
carries the chain; this gate keeps it honest.

WHAT IS ENFORCED.
  * schema: every chain has id, headline, trigger, naive, chain, check, traps,
    invalidates_if, related.
  * RECEIPTS RESOLVE.  Every receipt path must exist. This is the load-bearing
    check -- a chain whose receipts have rotted is worse than no chain, because
    it reads as verified.
  * TRAPS ARE DATED AND REAL.  Every trap carries a date and a cost. The file's
    own rule is that a trap is recorded only once it has ACTUALLY happened;
    speculative pitfalls belong in the improvement register.
  * grades come from a fixed vocabulary.
  * related ids resolve to real chains.

WHAT IS NOT ENFORCED, stated so nobody reads more into a green run.  This gate
cannot check that a chain's reasoning is correct, only that it is well-formed
and that its receipts exist. A chain can be green and wrong.

REGENERATION.  Run with --write to rewrite lab/process/path-dependencies.md
from the YAML. The markdown is GENERATED; edit the YAML, never the markdown.
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "lab/process/path-dependencies.yaml"
RENDERED = ROOT / "lab/process/path-dependencies.md"

REQUIRED = ("id", "headline", "trigger", "naive", "chain", "check",
            "traps", "invalidates_if", "related")
GRADES = {"EXACT", "THEOREM", "AUTHOR-STATED", "CONDITIONAL", "OPEN"}
CHAIN_CAP = 8  # overbuild protection; see test_chain_count_is_capped


def load() -> dict:
    return yaml.safe_load(SOURCE.read_text(encoding="utf-8"))


def render(doc: dict) -> str:
    out: list[str] = []
    out.append("<!-- GENERATED from lab/process/path-dependencies.yaml by")
    out.append("     process_gates/path_dependency_audit.py --write.")
    out.append("     Edit the YAML, never this file. -->")
    out.append("")
    out.append("# Path dependencies")
    out.append("")
    out.append("Why a strange-looking check exists. Each chain ends in a **check**;")
    out.append("each **trap** is a mistake that actually happened, with its date.")
    out.append("")
    out.append("```mermaid")
    out.append("graph TD")
    for chain in doc["chains"]:
        cid = chain["id"].replace("-", "_")
        out.append(f'  {cid}["{chain["id"]}"]')
        for i, step in enumerate(chain["chain"]):
            node = f"{cid}_s{i}"
            fact = step["fact"].replace('"', "'")
            if len(fact) > 78:
                fact = fact[:75] + "..."
            out.append(f'  {node}["{step["grade"]}: {fact}"]')
            out.append(f"  {cid} --> {node}" if i == 0
                       else f"  {cid}_s{i-1} --> {node}")
        last = f"{cid}_s{len(chain['chain']) - 1}"
        chk = chain["check"].strip().replace('"', "'").split(".")[0]
        if len(chk) > 78:
            chk = chk[:75] + "..."
        out.append(f'  {cid}_chk{{"CHECK: {chk}"}}')
        out.append(f"  {last} --> {cid}_chk")
        for t, trap in enumerate(chain["traps"]):
            out.append(f'  {cid}_t{t}("TRAP {trap["date"]}")')
            out.append(f"  {cid}_chk -.-> {cid}_t{t}")
    for chain in doc["chains"]:
        for rel in chain.get("related") or []:
            out.append(f'  {chain["id"].replace("-", "_")} '
                       f'=== {rel.replace("-", "_")}')
    out.append("```")
    out.append("")
    for chain in doc["chains"]:
        out.append(f"## {chain['id']}")
        out.append("")
        out.append(f"**{chain['headline'].strip()}**")
        out.append("")
        out.append(f"- **Trigger:** {chain['trigger'].strip()}")
        out.append(f"- **Naive reading:** {chain['naive'].strip()}")
        out.append("")
        out.append("| # | grade | fact | receipt |")
        out.append("|---|---|---|---|")
        for i, step in enumerate(chain["chain"], 1):
            out.append(f"| {i} | `{step['grade']}` | {step['fact']} "
                       f"| `{step['receipt']}` |")
        out.append("")
        out.append(f"**CHECK.** {chain['check'].strip()}")
        out.append("")
        out.append("**Traps that actually happened:**")
        out.append("")
        for trap in chain["traps"]:
            out.append(f"- **{trap['date']}** — {trap['what'].strip()}")
            out.append(f"  - *Cost:* {trap['cost'].strip()}")
            out.append(f"  - *Receipt:* `{trap['receipt']}`")
        out.append("")
        out.append(f"**Invalidates if:** {chain['invalidates_if'].strip()}")
        out.append("")
    return "\n".join(out) + "\n"


class PathDependencyAudit(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.doc = load()
        cls.chains = cls.doc["chains"]
        cls.ids = {c["id"] for c in cls.chains}

    def test_chain_count_is_capped(self) -> None:
        """The overbuild protection, and the only one that has ever worked.

        This repository has 272 files in process_gates/ and about three are
        named as run every wave. Growth was free, so it happened. A hard cap
        forces the question 'is this chain more valuable than the weakest
        current one?', which nobody asks otherwise.
        """
        print(f"\n[cap] {len(self.chains)}/{CHAIN_CAP} chains")
        self.assertLessEqual(
            len(self.chains), CHAIN_CAP,
            f"path-dependencies.yaml is capped at {CHAIN_CAP} chains. "
            "Adding another requires RETIRING one -- that is the point of the "
            "cap. Do not raise it without a council; the 272-gate directory is "
            "what happens when growth is free.")
        if len(self.chains) == CHAIN_CAP:
            print("      AT CAP -- the next chain must replace one, not extend.")

    def test_schema_is_complete(self) -> None:
        print(f"\n[schema] {len(self.chains)} chains")
        for chain in self.chains:
            for field in REQUIRED:
                self.assertIn(field, chain,
                              f"{chain.get('id', '?')} missing '{field}'")
            print(f"    {chain['id']}: {len(chain['chain'])} steps, "
                  f"{len(chain['traps'])} traps")

    def test_every_receipt_resolves(self) -> None:
        """The load-bearing check. A chain with rotted receipts reads as
        verified while being unverifiable."""
        missing: list[str] = []
        total = 0
        for chain in self.chains:
            receipts = [s["receipt"] for s in chain["chain"]]
            receipts += [t["receipt"] for t in chain["traps"]]
            for rec in receipts:
                total += 1
                if not (ROOT / rec).exists():
                    missing.append(f"{chain['id']}: {rec}")
        print(f"\n[receipts] {total} checked")
        for m in missing:
            print(f"    MISSING  {m}")
        self.assertEqual([], missing,
                         "a path-dependency chain cites a receipt that does not "
                         "exist; fix the path or remove the step")
        print("    all resolve")

    def test_grades_are_from_the_vocabulary(self) -> None:
        for chain in self.chains:
            for step in chain["chain"]:
                self.assertIn(step["grade"], GRADES,
                              f"{chain['id']}: unknown grade {step['grade']!r}")

    def test_traps_are_dated_and_costed(self) -> None:
        """The file's own rule: a trap is recorded only once it has actually
        happened. Undated entries are speculation and belong in the register."""
        count = 0
        for chain in self.chains:
            self.assertTrue(chain["traps"],
                            f"{chain['id']} has no traps -- a chain with no "
                            "recorded failure has not earned its place here")
            for trap in chain["traps"]:
                for field in ("date", "what", "cost", "receipt"):
                    self.assertIn(field, trap, f"{chain['id']}: trap missing {field}")
                self.assertRegex(str(trap["date"]), r"^\d{4}-\d{2}-\d{2}$",
                                 f"{chain['id']}: trap date must be ISO")
                count += 1
        print(f"\n[traps] {count} recorded, all dated and costed")

    def test_related_ids_resolve(self) -> None:
        for chain in self.chains:
            for rel in chain.get("related") or []:
                self.assertIn(rel, self.ids,
                              f"{chain['id']} relates to unknown chain {rel}")

    def test_rendered_markdown_is_current(self) -> None:
        expected = render(self.doc)
        if not RENDERED.exists():
            self.fail(f"{RENDERED.relative_to(ROOT)} missing -- run with --write")
        actual = RENDERED.read_text(encoding="utf-8")
        self.assertEqual(expected, actual,
                         "the rendered markdown is stale; regenerate with "
                         "`python process_gates/path_dependency_audit.py --write`")
        print("\n[render] markdown view is current")


if __name__ == "__main__":
    if "--write" in sys.argv:
        RENDERED.write_text(render(load()), encoding="utf-8")
        print(f"wrote {RENDERED.relative_to(ROOT)}")
    else:
        unittest.main(verbosity=2)
