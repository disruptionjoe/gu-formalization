#!/usr/bin/env python3
"""K596 rank-one discriminator for future action-owned K444 soldering maps."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k596-k77-rank-one-soldering-discriminator.json"


def strict(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text())


def matmul(a, b):
    return [[sum(Fraction(x) * Fraction(y) for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def sub(a, b):
    return [[Fraction(x) - Fraction(y) for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def frobenius_square(a) -> Fraction:
    return sum(Fraction(x) ** 2 for row in a for x in row)


def rank_2x2(a) -> int:
    if all(Fraction(x) == 0 for row in a for x in row):
        return 0
    return 2 if Fraction(a[0][0]) * Fraction(a[1][1]) - Fraction(a[0][1]) * Fraction(a[1][0]) else 1


def outer(y, x, coefficient):
    return [[Fraction(coefficient) * Fraction(yi) * Fraction(xj) for xj in x] for yi in y]


def square_defect(pi_target, coupling, pi_source):
    return sub(matmul(pi_target, coupling), matmul(coupling, pi_source))


def row(name, coefficient, x, y, expected_square, expected_rank):
    projector = [[1, 0], [0, 0]]
    coupling = outer(y, x, coefficient)
    defect = square_defect(projector, coupling, projector)
    norm_square = frobenius_square(defect)
    rank = rank_2x2(defect)
    assert norm_square == Fraction(expected_square) and rank == expected_rank
    return {
        "name": name,
        "coefficient": str(Fraction(coefficient)),
        "source_vector": list(x),
        "target_vector": list(y),
        "typed_square_defect": [[str(v) for v in r] for r in defect],
        "defect_frobenius_norm_square": str(norm_square),
        "defect_rank": rank,
    }


def build() -> dict:
    k444 = strict("lab/process/k444-k77-degree-changing-boundary-squares.json")
    k594 = strict("lab/process/k594-k77-native-third-jet-carrier-typing.json")
    physical = strict("lab/process/selected-action-physical-soldering-observation-compose.json")
    jets = strict("lab/process/selected-action-second-soldering-observation-jets.json")
    coeffs = k594["selected_action_third_jet"]["serialized_coefficients"]
    c1 = Fraction(coeffs["D3_t_t_t"])
    c2 = Fraction(coeffs["D3_t_v_v_over_native_norm"])
    controls = [
        row("D2 same-half", c1, [1, 0], [1, 0], 0, 0),
        row("D2 cross-half", c1, [1, 0], [0, 1], c1 * c1, 1),
        row("D1 same-half", c2, [0, 1], [0, 1], 0, 0),
        row("D1 cross-half", c2, [1, 0], [0, 1], c2 * c2, 1),
    ]
    assert k444["general_theorem"]["typed_square"] == "Pi_target D = D Pi_source"
    return {
        "schema_version": "1.0",
        "result_id": "K596-K77-RANK-ONE-SOLDERING-DISCRIMINATOR",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "The exact K444 typed-square defect for any future conditional rank-one action-owned coupling between declared corrected-carrier source and target halves, evaluated with two already nonzero K594 scalar coefficients.",
        "gu_typed_objects": {
            "carrier": "declared source and target degree sectors tensored with K441 corrected-carrier halves",
            "projectors": "Pi_source and Pi_target on the declared corrected source and target carriers",
            "conditional_coupling": "C=c |y><x| after an action-owned injection/Riesz/soldering packet supplies x and y",
            "result": "rank-one K444 discriminator MAP-TYPE=typed-square-defect",
            "target": "both K444 arrow types H->Q and Q->M",
        },
        "theorem": {
            "typed_square_defect": "Delta(C)=Pi_target C-C Pi_source",
            "rank_one_formula": "For C=c|y><x|, Delta=c(|Pi_target y><x|-|y><Pi_source x|).",
            "same_half_result": "If Pi_source x=epsilon x and Pi_target y=epsilon y for the same epsilon in {0,1}, Delta=0.",
            "opposite_half_result": "If Pi_source x=epsilon x and Pi_target y=(1-epsilon)y for normalized x,y, Delta has rank one and Hilbert-Schmidt norm |c|.",
            "nonzero_scalar_is_not_a_soldering": True,
            "actual_owned_vectors_required": True,
        },
        "exact_controls": {
            "rows": controls,
            "both_K444_arrow_types_exercised": {r["name"].split()[0] for r in controls} == {"D1", "D2"},
            "same_half_rows_zero": all(r["defect_rank"] == 0 for r in controls if "same-half" in r["name"]),
            "cross_half_rows_rank_one": all(r["defect_rank"] == 1 for r in controls if "cross-half" in r["name"]),
            "nonzero_K594_coefficients_replayed": [str(c1), str(c2)],
        },
        "existing_candidate_audit": {
            "physical_soldering_observation_rank": physical["exact_result"]["observed_soldering_rank"],
            "physical_chain_scope": "local principal observation/metric receiver chain",
            "physical_chain_owns_K441_rank512_carrier": False,
            "second_observation_jets_serialized": bool(jets),
            "second_observation_jets_own_K589_degree_arrows": False,
            "K594_action_Riesz_on_K441_pairing_serialized": k594["type_audit"]["action_Riesz_map_on_K441_pairing_serialized"],
            "existing_candidate_releases_actual_K444_square": False,
        },
        "decision": {
            "conditional_rank_one_discriminator_emitted": True,
            "actual_action_owned_soldering_constructed": False,
            "K590_nonfactorized_square_test_released": False,
            "K590_factorized_completion_retracted": False,
            "selected_source_action_rejected": False,
            "next_exact_input": "Supply one action-owned field-to-corrected-carrier injection/Riesz packet naming source vector x and target vector y for either K589 arrow; then apply Delta(C) immediately and repeat for the other arrow.",
        },
        "source_and_ledger_effect": "none",
        "preflight_bookend": {
            "route_comparison": "Derive the cheapest exact discriminator before constructing any 512-by-512 deformation.",
            "retrieval_collision_result": "Existing physical soldering artifacts own a rank-10 local observation chain, not K441's corrected carrier or K589's degree arrows.",
            "strongest_alternative": "A full action-owned soldering construction remains necessary for an actual square, but its first rank-one component can now be tested without expanding the full matrix.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Treating a nonzero K594 scalar coefficient or the rank-10 physical soldering chain as the missing corrected-carrier map.",
            "strongest_contrary_construction": "The same nonzero scalar gives zero defect for matching halves and rank-one defect for opposite halves; carrier placement, not scalar nonvanishing, decides the square.",
            "weakest_reproducibility_seam": "The discriminator is conditional until an action-owned injection/Riesz packet supplies the actual corrected-carrier vectors.",
        },
        "claim_ceiling": "Exact conditional rank-one K444 discriminator: a matching-half coupling has zero typed-square defect, while an opposite-half normalized coupling has rank-one defect of norm |c|. The nonzero K594 coefficients exercise both outcomes for both arrow types, but no action-owned corrected-carrier coupling is constructed and no K444 square, source, ledger, canon, paper, public, novelty or physical conclusion moves.",
    }


def validate(p: dict) -> None:
    t, c, a, d = p["theorem"], p["exact_controls"], p["existing_candidate_audit"], p["decision"]
    assert t["nonzero_scalar_is_not_a_soldering"] and t["actual_owned_vectors_required"]
    assert c["both_K444_arrow_types_exercised"] and c["same_half_rows_zero"] and c["cross_half_rows_rank_one"]
    assert c["nonzero_K594_coefficients_replayed"] == ["8736", "-56/3"]
    assert a["physical_soldering_observation_rank"] == 10 and not a["physical_chain_owns_K441_rank512_carrier"]
    assert not a["second_observation_jets_own_K589_degree_arrows"] and not a["K594_action_Riesz_on_K441_pairing_serialized"]
    assert d["conditional_rank_one_discriminator_emitted"] and not any(d[k] for k in ("actual_action_owned_soldering_constructed", "K590_nonfactorized_square_test_released", "K590_factorized_completion_retracted", "selected_source_action_rejected"))


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--write", action="store_true"); args = parser.parse_args()
    payload = build(); validate(payload); rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write: OUTPUT.write_text(rendered)
    else: print(rendered, end="")
    return 0


if __name__ == "__main__": raise SystemExit(main())
