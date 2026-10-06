#!/usr/bin/env python3
"""Hostile mutations for K1171."""
from copy import deepcopy
from k1171_repair_resource_conservation_law import build, validate


def main():
    mutations = [
        ("hypotheses", None, []), ("actual_constraint_rank", None, "c=dim W"),
        ("resource_identity", None, "rank H+c=dim V"), ("ceiling_form", None, "no floor"),
        ("relative_repair_floor", None, "one resource is free"), ("hessian_rank", None, 3),
        ("gauge_rank", None, 3), ("constraint_rank_on_kernel", None, 4),
        ("positive_quotient_dimension", None, 0), ("decision", None, "missing directions disappear"),
        ("scope_boundary", None, "global GU no-go"),
    ]
    caught = 0
    for key, _, value in mutations:
        d = deepcopy(build())
        if key in d["theorem"]: d["theorem"][key] = value
        elif key in d["exact_control"]: d["exact_control"][key] = value
        else: d[key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == 11
    print("K1171 hostile probes: 11/11")


if __name__ == "__main__": main()
