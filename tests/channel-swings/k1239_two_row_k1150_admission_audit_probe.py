#!/usr/bin/env python3
"""Hostile mutations for the K1239 admission audit."""

GATES = ("source_action_owner", "causal_algebraic_packet", "common_graph_domain",
         "closed_gauge_range", "uniform_positive_gap", "maximal_generator", "boundary_trace_compatibility")
EXPECTED = {gate: False for gate in GATES}


def accepts(item):
    return item == EXPECTED and sum(item.values()) == 0


mutations = []
for gate in GATES:
    item = dict(EXPECTED); item[gate] = True; mutations.append(item)
item = dict(EXPECTED); item.pop("boundary_trace_compatibility"); mutations.append(item)
assert accepts(EXPECTED)
assert all(not accepts(item) for item in mutations)
print(f"PASS hostile mutations {len(mutations)}/{len(mutations)}")
