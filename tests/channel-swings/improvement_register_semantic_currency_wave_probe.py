#!/usr/bin/env python3
"""Exact custody gate for the M-M5/M-M21/M-M25 semantic-currency wave."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/improvement-register-semantic-currency-wave.json"
REGISTER = ROOT / "lab/process/improvement-register-2026-08-03.md"
M5 = ROOT / "explorations/representation-theory-noncompact/tau-twisted-rs-admissibility-kobayashi-2026-06-23.md"
M21_CHAIN = ROOT / "explorations/channel-swing-CH-SM-2026-07-19.md"
M21_Z3 = ROOT / "explorations/wave15/H38-z3-chiral-selector-2026-07-11.md"
M25 = ROOT / "lab/process/rb7-invariant-inertia-and-commuting-cone-coercivity.json"


def evaluate(manifest: dict, register: str, m5: str, chain: str, z3: str, m25: dict) -> list[tuple[str, bool]]:
    rows = {row["id"]: row for row in manifest.get("records", [])}
    return [
        ("three exact records", set(rows) == {"M-M5", "M-M21", "M-M25"}),
        ("M-M5 executed", rows.get("M-M5", {}).get("result") == "NONCOMPACT_KOBAYASHI_ROUTE_FAILS_AS_STATED"),
        ("M-M5 rank mismatch", "rank(G/H) = 3 != 1 = rank(K/(K cap H))" in m5),
        ("M-M5 nonunitary coefficient", "`tau_RS` is not unitary" in m5),
        ("M-M5 cone survives", "contains R_{\\ge 0}(1,1)" in m5),
        ("M-M21 executed", rows.get("M-M21", {}).get("result") == "CONVENTIONAL_126_ROUTE_LEAVES_Z2_NOT_Z3"),
        ("M-M21 matter parity Z2", "a physical Z/2 output of the chain" in chain),
        ("M-M21 primary separation", "|Hom(Z/2, Z/3)|" in z3 and "PERMITS" in z3),
        ("M-M25 premise shifted", rows.get("M-M25", {}).get("disposition") == "PREMISE_SHIFTED"),
        ("M-M25 trace kernel", m25.get("candidate_gram", {}).get("rank") == 9 and "full-trace line" in m25.get("candidate_gram", {}).get("kernel", "")),
        ("M-M25 coercivity fails", "fails" in m25.get("candidate_gram", {}).get("coercivity_verdict", "")),
        ("register markers current", all(token in register for token in ("M-M5 | **EXECUTED (semantic currency reconciled 2026-08-27)", "M-M21 | **EXECUTED AT THE CONVENTIONAL-COMPARATOR/TYPE CEILING", "M-M25 | **PREMISE SHIFTED (semantic currency reconciled 2026-08-27)"))),
    ]


def load() -> tuple[dict, str, str, str, str, dict]:
    return (
        json.loads(MANIFEST.read_text()), REGISTER.read_text(), M5.read_text(),
        M21_CHAIN.read_text(), M21_Z3.read_text(), json.loads(M25.read_text()),
    )


def selftest(inputs: tuple[dict, str, str, str, str, dict]) -> int:
    mutations = []
    for mutate in (
        lambda x: x[0]["records"].pop(),
        lambda x: x[0]["records"][0].update(result="ROUTE_SURVIVES"),
        lambda x: x.__setitem__(2, x[2].replace("rank(G/H) = 3 != 1 = rank(K/(K cap H))", "rank equality holds")),
        lambda x: x.__setitem__(3, x[3].replace("a physical Z/2 output of the chain", "a physical Z/3 output of the chain")),
        lambda x: x[0]["records"][2].update(disposition="EXECUTED"),
        lambda x: x[5]["candidate_gram"].update(rank=10),
    ):
        trial = [copy.deepcopy(v) for v in inputs]
        mutate(trial)
        mutations.append(any(not ok for _, ok in evaluate(*trial)))
    caught = sum(mutations)
    print(f"semantic-currency mutation controls: {caught}/{len(mutations)} caught")
    return 0 if caught == len(mutations) else 1


def main() -> int:
    inputs = load()
    checks = evaluate(*inputs)
    for name, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if not all(ok for _, ok in checks):
        return 1
    print(f"improvement-register semantic currency: PASS ({len(checks)}/{len(checks)})")
    return selftest(inputs) if "--selftest" in sys.argv else 0


if __name__ == "__main__":
    raise SystemExit(main())
