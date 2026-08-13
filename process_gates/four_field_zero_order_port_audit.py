#!/usr/bin/env python3
"""Durability audit for ledger v0.138 four-field zero-order port result."""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def strict(relative: str):
    path = ROOT / relative

    def hook(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate key {key!r}: {path}")
            result[key] = value
        return result

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


old = strict("lab/process/conditional-physics-ledger-v0.137.json")
new = strict("lab/process/conditional-physics-ledger-v0.138.json")
result = strict("lab/process/selected-k77-four-field-zero-order-port.json")
contract = strict("lab/process/functional-channel-operating-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-k77-four-field-zero-order-port-2026-08-10.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-10-selected-k77-four-field-zero-order-port-review.md").read_text()
routing = "\n".join((ROOT / name).read_text() for name in (
    "LANES.yaml", "NEXT-STEPS.md", "RESEARCH-STATUS.md", "lab/process/README.md",
    "lab/process/agent-context-pack.md", "lab/process/exploration-absorption-priorities-2026-08-10.md",
))

check("ledger", "v0.138 is append-only from v0.137",
      new["predecessor"].endswith("v0.137.json")
      and [row["id"] for row in new["rows"]] == [row["id"] for row in old["rows"]])
check("ledger", "headline counts remain unchanged",
      new["progress"]["verdict_counts"] == old["progress"]["verdict_counts"]
      and new["progress"]["mapped"] == old["progress"]["mapped"] == 82)
check("ledger", "frontier closes one condition and exposes two graph horns",
      new["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 1,
                                "conditions_opened": 2, "remaining_named_conditions": 2})
check("ledger", "six exact migration edges were appended",
      [(m["row_id"], m["from_version"], m["to_version"]) for m in new["migrations"][-6:]]
      == [(row, "0.137", "0.138") for row in ("RA-D2", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1")])
check("ledger", "six moved rows cite the four-field port result",
      all(row["evidence"] == "selected-k77-four-field-zero-order-port-2026-08-10.md"
          for row in new["rows"] if row["id"] in {"RA-D2", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1"}))

parents = result["exact_results"]["parents"]
check("exact", "moving Spin and two-half parents require alpha=beta",
      parents["moving_spin_grade2"]["preferred_ratio"] == "alpha=beta"
      and parents["two_u32_32_halves_grade6"]["preferred_ratio"] == "alpha=beta")
check("exact", "full-U odd coset requires alpha=-beta",
      parents["source_full_u64_64_odd_coset_grade1"]["preferred_ratio"] == "alpha=-beta")
check("exact", "every parent has rank-64 leak inside rank-128 port",
      all(parent["leak_rank_each"] == 64
          and parent["port_rank_each"] == parent["joined_rank_each"] == 128
          for parent in parents.values()))
check("exact", "every form-quotient coefficient system has rank one",
      all(parent["quotient_coefficient_rank_each"] == 1 for parent in parents.values()))
check("exact", "finite and Gaussian-rational fields plus twelve plants are recorded",
      result["exact_results"]["fields"] == ["GF(1000033)", "QQ(i)"]
      and result["exact_results"]["single_slot_plants_rejected"] == 12)
check("theorem", "source-full common ratio is rejected",
      result["exact_results"]["common_ratio_for_even_and_odd_parent_classes"] is False)

check("layer0", "inclusion, graph, BV and domain stay split",
      result["layer0"] == {
          "one_form_invariance": "V0_136_FAILS",
          "zero_form_port_image_inclusion": "DECIDED_HERE",
          "graph_invariance": "OPEN_DISTINCT",
          "bv_cohomology": "OPEN_DISTINCT",
          "analytic_domain": "OPEN_DISTINCT",
      })
check("scope", "graph and lower-left conditions remain open",
      "construction of a graph map G from W or mirror to Omega0(S)" in result["scope"]["not_closed"]
      and "lower-left adjoint compatibility and the nonlinear graph Riccati identity" in result["scope"]["not_closed"])
check("source", "source confirmation and silence are separate",
      set(result["source_return"]) == {"SOURCE-CONFIRMS", "SOURCE-SILENT"})
check("hostile", "three charges and dissent are explicit",
      all(token in review for token in ("Charge 1", "Charge 2", "Charge 3", "Dissent")))
check("symplectic", "review refuses port-to-BV inflation",
      "reduction is not physical cohomology" in report
      and "no reduced phase-space class" in review)
check("analytic", "review refuses rank-to-domain inflation",
      "No closed domain, spectrum" in report and "no domain, spectrum" in review)
check("variational", "graph Riccati and lower-left duties are explicit",
      "graph/Riccati" in report and "lower-left" in review)

check("routing", "contract and front doors point to v0.138",
      contract["standing_ledger"]["ref"].endswith("v0.138.json")
      and "ledger v0.138" in routing)
check("routing", "next gate is graph-Riccati plus lower-left",
      "graph-Riccati" in routing and "lower-left" in routing)
check("accounting", "no verdict residue quotient datum or P1/P2/P3 moves",
      all(result["accounting"][key] is False for key in (
          "verdict_change", "residue_change", "quotient_change", "datum_change", "p1_p2_p3_change"
      )))
check("accounting", "residue forks and quotients are unchanged",
      new["residue"] == old["residue"])

print("COUNTS " + " ".join(f"{kind}={count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    for failure in FAILURES:
        print(f"FAIL: {failure}")
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
