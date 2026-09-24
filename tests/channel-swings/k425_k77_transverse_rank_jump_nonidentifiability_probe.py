#!/usr/bin/env python3
"""Independent controls and hostile mutations for K425."""

from __future__ import annotations

import copy
import json

from k425_k77_transverse_rank_jump_nonidentifiability import demo


def valid(result: dict) -> bool:
    families = result["rank_jump_completions"]
    return all(
        [
            result["frozen_complex"] == {"map": "A0=[I_70 0_70x21]: R^91 -> R^70", "rank": 70, "kernel_dimension": 21, "cokernel_dimension": 0},
            result["constant_completion"]["rank_everywhere"] == 70,
            len(families) == 8,
            [row["matching_jet_order"] for row in families] == list(range(1, 9)),
            all(row["coefficient"] == f"1-t^{row['matching_jet_order'] + 1}" for row in families),
            all(len(row["base_derivatives_through_matching_order"]) == row["matching_jet_order"] for row in families),
            all(set(row["base_derivatives_through_matching_order"]) <= {0} for row in families),
            all(row["generic_rank"] == 70 for row in families),
            all(row["rank_at_t_equals_1"] == 69 for row in families),
            all(row["kernel_dimension_at_t_equals_1"] == 22 for row in families),
            all(row["cokernel_dimension_at_t_equals_1"] == 1 for row in families),
            all(row["global_polynomial_extra_syzygy"] is False for row in families),
            result["shared_frozen_data"]["arbitrarily_long_finite_transverse_jets_can_match_constant_completion"] is True,
            result["decision"]["k419_frozen_complex_identifies_transverse_rank_behavior"] is False,
            result["decision"]["source_owned_transverse_family_still_required"] is True,
        ]
    )


def main() -> int:
    result = demo()
    assert valid(result)
    mutations = []
    for path, value in [
        (("frozen_complex", "rank"), 69),
        (("constant_completion", "rank_everywhere"), 69),
        (("rank_jump_completions", 0, "coefficient"), "1-t"),
        (("rank_jump_completions", 1, "base_derivatives_through_matching_order"), [0, 1]),
        (("rank_jump_completions", 2, "generic_rank"), 69),
        (("rank_jump_completions", 3, "rank_at_t_equals_1"), 70),
        (("rank_jump_completions", 4, "kernel_dimension_at_t_equals_1"), 21),
        (("rank_jump_completions", 5, "cokernel_dimension_at_t_equals_1"), 0),
        (("rank_jump_completions", 6, "global_polynomial_extra_syzygy"), True),
        (("decision", "k419_frozen_complex_identifies_transverse_rank_behavior"), True),
        (("decision", "source_owned_transverse_family_still_required"), False),
    ]:
        candidate = copy.deepcopy(result)
        target = candidate
        for key in path[:-1]:
            target = target[key]
        target[path[-1]] = value
        mutations.append(candidate)
    rejected = sum(not valid(candidate) for candidate in mutations)
    assert rejected == len(mutations)
    print(json.dumps({"controls_passed": 15, "hostile_mutations_rejected": rejected}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
