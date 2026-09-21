#!/usr/bin/env python3
"""Independent reverse-allocation replay for K278."""
from __future__ import annotations

from copy import deepcopy
from decimal import Decimal, localcontext
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROCESS = ROOT / "lab/process"


def replay(k184: dict, k185: dict, k218: dict) -> tuple[int, int, int, Decimal]:
    source = {}
    for e in k184["andreief_time_gram_certificate"]["gram_entries"]:
        key = (e["group_id"], e["left"], e["right"])
        assert key not in source
        source[key] = e["coefficient_product"]
    expanded = {}
    term_count = ordered_count = 0
    for e in reversed(k185["complete_face_hypergraph"]["entries"]):
        key = (e["group_id"], e["left"], e["right"])
        assert key not in expanded
        expanded[key] = e["coefficient_product"]
        n = len(e["terms"])
        assert n == e["leibniz_term_count"]
        term_count += n
        ordered_count += n * (1 if e["left"] == e["right"] else 2)
    assert source == expanded
    assert term_count == 1864 == k218["terms"]
    assert ordered_count == 2928 == k218["ordered_terms_after_off_diagonal_doubling"]
    groups = sorted({key[0] for key in source})
    witnesses = k184["localized_interval_witnesses"]["groups"]
    assert groups == sorted(witnesses) and len(groups) == 18
    lowers = [Decimal(witnesses[g]["certified_full_space_norm_squared_lower"])
              for g in reversed(groups)]
    assert all(x > 0 for x in lowers)
    with localcontext() as ctx:
        ctx.prec = 90
        lower = sum(lowers, Decimal(0))
    return len(source), term_count, ordered_count, lower


def main() -> None:
    k184 = json.loads((PROCESS / "k184-order-six-certified-low-rank-wave.json").read_text())
    k185 = json.loads((PROCESS / "k185-order-six-duffy-face-tail-wave.json").read_text())
    k218 = json.loads((PROCESS / "k218-order-six-exact-angular-elimination.json").read_text())
    result = json.loads((PROCESS / "k278-order-six-full-domain-gram-positivity.json").read_text())
    facts = replay(k184, k185, k218)
    assert facts[0:3] == (234, 1864, 2928)
    assert str(facts[3]) == result["theorem"]["strict_lower_witness"]

    rejected = 0
    for kind in range(5):
        a, b, c = deepcopy(k184), deepcopy(k185), deepcopy(k218)
        if kind == 0:
            b["complete_face_hypergraph"]["entries"][0]["left"] += "-mutated"
        elif kind == 1:
            b["complete_face_hypergraph"]["entries"][0]["leibniz_term_count"] += 1
        elif kind == 2:
            a["andreief_time_gram_certificate"]["gram_entries"].pop()
        elif kind == 3:
            first = next(iter(a["localized_interval_witnesses"]["groups"]))
            a["localized_interval_witnesses"]["groups"][first]["certified_full_space_norm_squared_lower"] = "-1E-99"
        else:
            c["terms"] = 1863
        try:
            replay(a, b, c)
        except AssertionError:
            rejected += 1
    assert rejected == 5
    print("[PASS] K278 independent reverse replay; 234/1864/2928 and 18 strict groups; 5/5 hostile")


if __name__ == "__main__":
    main()
