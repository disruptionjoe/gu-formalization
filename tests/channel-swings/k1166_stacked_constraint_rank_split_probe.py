#!/usr/bin/env python3
"""Hostile mutations for K1166."""
from copy import deepcopy
from k1166_stacked_constraint_rank_split import build, validate


def main():
    mutations = [
        ("hypotheses", None, []), ("exact_split", None, "rank adds automatically"),
        ("overlap_defect", None, "delta<0"), ("radical_capture_necessity", None, "rank may vanish"),
        ("target_ceiling", None, "unbounded"), ("q_rank", None, 3),
        ("ell_rank", None, 2), ("stacked_rank", None, 5),
        ("overlap_defect_value", None, 0), ("required", None, 4),
        ("decision", None, "all rows independent"), ("scope", None, "global no-go"),
    ]
    caught = 0
    for key, _, value in mutations:
        d = deepcopy(build())
        if key in d["theorem"]: d["theorem"][key] = value
        elif key == "overlap_defect_value": d["exact_control"]["overlap_defect"] = value
        elif key == "required": d["exact_control"]["required_radical_capture_rank"] = value
        elif key in d["exact_control"]: d["exact_control"][key] = value
        elif key == "scope": d["scope_boundary"] = value
        else: d[key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == 12
    print("K1166 hostile probes: 12/12")


if __name__ == "__main__": main()
