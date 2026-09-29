#!/usr/bin/env python3
"""K616 unsplit zero-form rank-one obstruction and covariant persistence."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k616-k77-unsplit-rank-one-transport-obstruction.json"


def strict(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def mm(a, b):
    return [[sum(Fraction(x) * Fraction(y) for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def sub(a, b):
    return [[Fraction(x) - Fraction(y) for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def outer(y, x):
    return [[Fraction(yi) * Fraction(xj) for xj in x] for yi in y]


def rank(a):
    rows = [list(map(Fraction, row)) for row in a]
    m, n = len(rows), len(rows[0])
    i = j = result = 0
    while i < m and j < n:
        pivot = next((k for k in range(i, m) if rows[k][j]), None)
        if pivot is None:
            j += 1
            continue
        rows[i], rows[pivot] = rows[pivot], rows[i]
        p = rows[i][j]
        rows[i] = [x / p for x in rows[i]]
        for k in range(m):
            if k != i and rows[k][j]:
                c = rows[k][j]
                rows[k] = [x - c * y for x, y in zip(rows[k], rows[i])]
        result += 1
        i += 1
        j += 1
    return result


def transpose(a):
    return [list(row) for row in zip(*a)]


def rotation(t: Fraction):
    d = 1 + t * t
    return [[(1 - t * t) / d, -2 * t / d], [2 * t / d, (1 - t * t) / d]]


def block_diag(a, b):
    za = [[Fraction(0) for _ in range(len(b[0]))] for _ in range(len(a))]
    zb = [[Fraction(0) for _ in range(len(a[0]))] for _ in range(len(b))]
    return [ra + rz for ra, rz in zip(a, za)] + [rz + rb for rz, rb in zip(zb, b)]


def toy_packet() -> dict:
    projector = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    x = [1, 2, 3, 5]
    y = [7, 11, 13, 17]
    coupling = outer(y, x)
    defect = sub(mm(projector, coupling), mm(coupling, projector))
    matching = [[coupling[i][j] if (i < 2) == (j < 2) else Fraction(0) for j in range(4)] for i in range(4)]
    matching_defect = sub(mm(projector, matching), mm(matching, projector))
    rows = []
    for t in (Fraction(0), Fraction(1, 3), Fraction(1, 2), Fraction(1)):
        u = block_diag(rotation(t), rotation(t))
        pi_t = mm(mm(u, projector), transpose(u))
        c_t = mm(mm(u, coupling), transpose(u))
        delta_t = sub(mm(pi_t, c_t), mm(c_t, pi_t))
        rows.append({"t": str(t), "transported_defect_rank": rank(delta_t)})
    return {
        "unsplit_defect_rank": rank(defect),
        "matching_half_defect_rank": rank(matching_defect),
        "transport_rows": rows,
    }


def build() -> dict:
    k615 = strict("lab/process/k615-k77-zero-form-stationarity-obstruction.json")
    k596 = strict("lab/process/k596-k77-rank-one-soldering-discriminator.json")
    k598 = strict("lab/process/k598-k77-covariant-rank-one-soldering-interface.json")
    toy = toy_packet()
    assert toy["unsplit_defect_rank"] == 2
    assert toy["matching_half_defect_rank"] == 0
    assert all(row["transported_defect_rank"] == 2 for row in toy["transport_rows"])
    ranks = k615["rank_fingerprint"]
    assert ranks["outgoing_zero_form"] == ranks["incoming_zero_form"] == 128
    assert ranks["outgoing_euler"] == ranks["incoming_euler"] == 128
    assert k596["theorem"]["actual_owned_vectors_required"] is True
    assert k598["theorem"]["fixed_vectors_are_not_covariant"]

    return {
        "schema_version": "1.0",
        "result_id": "K616-K77-UNSPLIT-RANK-ONE-TRANSPORT-OBSTRUCTION",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "The natural rank-one packet C_v=|A J0 v><J0 v| for a nonzero chosen K614 zero-form value in the K438 corrected carrier, tested against K596's corrected-half typed square and K598's orthogonal transport.",
        "gu_comparator_routing": "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.",
        "gu_typed_objects": {
            "carrier": "K438 corrected rank-512 E=E_out direct-sum E_in",
            "chosen_field_value": "x=J0 v for arbitrary nonzero v in the source-owned Omega0 field space; not action-selected and off shell by K615",
            "euler_riesz_candidate": "y=A J0 v represented through the K441 positive pairing",
            "projector": "K439 Pi_c,out with complementary Pi_c,in",
            "coupling": "natural unsplit rank-one C_v=|y><x|",
            "result": "unsplit rank-one typed-square obstruction MAP-TYPE=projector-intertwiner defect",
            "target": "K596 initial packet and K598 covariant transport",
        },
        "input_injectivity": {
            "outgoing_x_rank": ranks["outgoing_zero_form"],
            "incoming_x_rank": ranks["incoming_zero_form"],
            "outgoing_y_rank": ranks["outgoing_euler"],
            "incoming_y_rank": ranks["incoming_euler"],
            "every_nonzero_v_has_all_four_components_nonzero": True,
        },
        "unsplit_defect_theorem": {
            "definition": "Delta(C_v)=Pi_out C_v-C_v Pi_out",
            "decomposition": "Delta=|y_out><x_in|-|y_in><x_out|",
            "support_statement": "the two rank-one terms occupy disjoint outgoing-from-incoming and incoming-from-outgoing blocks",
            "rank_for_every_nonzero_v": 2,
            "natural_unsplit_packet_satisfies_K596": False,
            "zero_value_defect_rank": 0,
        },
        "matching_half_repair": {
            "packet": "C_match=|y_out><x_out|+|y_in><x_in|",
            "typed_square_defect_rank": 0,
            "equals_natural_unsplit_packet": False,
            "omitted_cross_terms": "|y_out><x_in|+|y_in><x_out|",
            "split_is_action_owned": False,
            "conditional_K596_packet_remains_live": True,
        },
        "transport_theorem": {
            "law": "Delta(t)=U(t) Delta(0) U(t)^T under K598 orthogonal transport",
            "rank_preserved": True,
            "rank_at_every_transport_fibre": 2,
            "fixed_unsplit_packet_becomes_valid": False,
            "moving_nonlinear_action_coupling_covered": False,
        },
        "exact_control": toy,
        "decision": {
            "K615_stationarity_obstruction_retracted": False,
            "natural_unsplit_packet_rejected_in_frozen_model": True,
            "matching_half_conditional_interface_retracted": False,
            "matching_half_action_ownership_constructed": False,
            "K596_actual_action_owned_packet_released": False,
            "K598_actual_action_owned_packet_released": False,
            "selected_source_action_rejected": False,
            "next_exact_input": "A moving nonlinear/source-owned odd datum must both solve its own stationary equation and action-own a matching-half corrected-carrier coupling; simply choosing v, using A J0 v, or deleting the cross-half terms does not meet that burden.",
        },
        "source_and_ledger_effect": "none",
        "preflight_bookend": {
            "route_comparison": "Apply K596 directly to the natural unsplit x/y packet before attempting a 512-by-512 deformation or silently projecting away cross terms.",
            "retrieval_collision_result": "K596 proves single rank-one same/opposite-half cases and K598 their transport; no predecessor composes the K614 fact that every nonzero zero-form value has both halves with its action-symbol image.",
            "strongest_alternative": "The matching-half sum passes algebraically, but it differs from the natural unsplit packet and needs a source/action owner for the projection.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling the rank-two defect a rejection of every nonfactorized action coupling or treating the unowned matching-half deletion as a repair.",
            "strongest_contrary_construction": "An action that independently supplies only matching-half components would pass K596 and transport through K598; current action truth does not own that modification.",
            "weakest_reproducibility_seam": "The universal rank-two proof uses K615's cross-characteristic injectivity plus disjoint block support; the explicit rational control is illustrative rather than the proof owner.",
        },
        "claim_ceiling": "Exact obstruction for the natural frozen-model packet generated by a chosen nonzero zero-form value: because both x=J0v and y=AJ0v have nonzero incoming and outgoing components, the unsplit rank-one packet has a K596 typed-square defect equal to two disjoint cross-half rank-one blocks and therefore rank two for every v!=0. K598 transport conjugates and preserves that defect. The matching-half sum has zero defect but is not the natural unsplit packet and is not action-owned. Together with K615, the current zero-form route supplies neither an on-shell nonzero background nor an actual K596/K598 packet. Moving nonlinear or differently owned odd data remain open; no source, ledger, canon, paper, public, novelty, prediction, confirmation, or physical conclusion moves.",
    }


def validate(p: dict) -> None:
    i = p["input_injectivity"]
    u = p["unsplit_defect_theorem"]
    m = p["matching_half_repair"]
    t = p["transport_theorem"]
    d = p["decision"]
    assert i["every_nonzero_v_has_all_four_components_nonzero"]
    assert [i[k] for k in ("outgoing_x_rank", "incoming_x_rank", "outgoing_y_rank", "incoming_y_rank")] == [128, 128, 128, 128]
    assert u["rank_for_every_nonzero_v"] == 2 and not u["natural_unsplit_packet_satisfies_K596"]
    assert m["typed_square_defect_rank"] == 0 and not m["equals_natural_unsplit_packet"] and not m["split_is_action_owned"]
    assert t["rank_preserved"] and t["rank_at_every_transport_fibre"] == 2 and not t["fixed_unsplit_packet_becomes_valid"]
    assert d["natural_unsplit_packet_rejected_in_frozen_model"]
    assert not d["matching_half_action_ownership_constructed"]
    assert not d["K596_actual_action_owned_packet_released"] and not d["K598_actual_action_owned_packet_released"]
    assert not d["selected_source_action_rejected"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
