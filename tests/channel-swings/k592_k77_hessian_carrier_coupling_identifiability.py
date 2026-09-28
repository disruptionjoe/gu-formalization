#!/usr/bin/env python3
"""K592 exact third-jet requirement for nonfactorized carrier coupling."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k592-k77-hessian-carrier-coupling-identifiability.json"


def subtract(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [[a - b for a, b in zip(lrow, rrow)] for lrow, rrow in zip(left, right)]


def multiply(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [[sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))] for i in range(len(left))]


def matrix_rows(matrix: list[list[int]]) -> list[list[str]]:
    return [[str(value) for value in row] for row in matrix]


def rank_2x2(matrix: list[list[int]]) -> int:
    if all(value == 0 for row in matrix for value in row):
        return 0
    return 2 if matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0] != 0 else 1


def build() -> dict:
    projector = [[1, 0], [0, 0]]
    compatible = [[2, 0], [0, 3]]
    hostile = [[0, 1], [1, 0]]

    def action_text(coupling: list[list[int]]) -> str:
        a, b, c = coupling[0][0], coupling[0][1], coupling[1][1]
        terms = ["x^2/2", "z_out^2/2", "z_in^2/2"]
        if a:
            terms.append(f"{a}*x*z_out^2/2")
        if b:
            terms.append(f"{b}*x*z_out*z_in")
        if c:
            terms.append(f"{c}*x*z_in^2/2")
        return "+".join(terms)

    def data(coupling: list[list[int]]) -> dict:
        hessian = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        third_jet = coupling
        defect = subtract(multiply(projector, third_jet), multiply(third_jet, projector))
        return {
            "action": action_text(coupling),
            "background_hessian": matrix_rows(hessian),
            "carrier_third_jet": matrix_rows(third_jet),
            "typed_square_defect": matrix_rows(defect),
            "typed_square_defect_rank": rank_2x2(defect),
        }

    zero = data([[0, 0], [0, 0]])
    good = data(compatible)
    bad = data(hostile)
    common_hessian = zero["background_hessian"] == good["background_hessian"] == bad["background_hessian"]
    distinct_third_jets = len({tuple(map(tuple, row["carrier_third_jet"])) for row in (zero, good, bad)}) == 3
    if not common_hessian or not distinct_third_jets:
        raise AssertionError("third-jet control failed")
    if good["typed_square_defect_rank"] != 0 or bad["typed_square_defect_rank"] != 2:
        raise AssertionError("projector controls failed")

    k585 = json.loads((ROOT / "lab/process/k585-k77-action-boundary-coupling-typing.json").read_text())
    k588 = json.loads((ROOT / "lab/process/k588-k77-action-orbit-reduction.json").read_text())
    k590 = json.loads((ROOT / "lab/process/k590-k77-corrected-carrier-completion-squares.json").read_text())
    selected = {
        "hessian_block_shape": k588["exact_reduction"]["B_shape"],
        "hessian_block_rank": k588["exact_reduction"]["B_rank"],
        "hessian_gram_scalar": k588["exact_reduction"]["B_gram_scalar"],
        "factorized_carrier_rank": k590["factorized_completion"]["carrier_rank"],
        "actual_nonfactorized_third_action_jet_serialized": False,
        "first_action_block_reused": k585["result_id"],
    }

    return {
        "schema_version": "1.0",
        "result_id": "K592-K77-HESSIAN-CARRIER-COUPLING-IDENTIFIABILITY",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Identifiability of the first field-dependent, nonfactorized corrected-carrier coupling from K585/K588's selected stationary action Hessian data.",
        "gu_comparator_routing": "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.",
        "gu_typed_objects": {
            "carrier": "K441 corrected moving rank-512 boundary carrier, represented in the exact control by one outgoing and one incoming line",
            "pairing": "real symmetric action Hessian pairing at the selected stationary background",
            "real_structure": "real polynomial control; the selected K77 real form remains unchanged",
            "grading": "base field x versus corrected-carrier trace halves",
            "action_owner": "K585/K588 own the selected second action derivative only; a third action derivative is not serialized",
            "result": "action-jet ownership boundary MAP-TYPE=variational-identifiability",
            "target": "first nonfactorized carrier dependence of the K590 degree-changing arrows",
        },
        "selected_native_inputs": selected,
        "theorem": {
            "background": "For S_T(x,z)=x^2/2+<z,z>/2+x<z,Tz>/2 at (0,0), the Hessian is diag(1,I) for every real symmetric T.",
            "third_jet": "d_x d_z^2 S_T(0,0)=T.",
            "identifiability": "The stationary Hessian does not determine the first field-dependence of its carrier block; that dependence is a third action jet.",
            "typed_square": "For the fixed boundary projector Pi, the first carrier coupling obeys the linearized K444 square exactly when [Pi,T]=0.",
            "full_rank_transfer": "On K441's 64+64 slow trace pair, the hostile exchange has commutator rank 128 while a block-diagonal third jet has rank-zero defect.",
        },
        "exact_controls": {
            "all_actions_share_background_hessian": common_hessian,
            "all_three_third_jets_distinct": distinct_third_jets,
            "zero_control": zero,
            "compatible_control": good,
            "hostile_exchange_control": bad,
            "hostile_exchange_actual_commutator_rank": 128,
        },
        "decision": {
            "K585_K588_hessian_determines_nonfactorized_carrier_coupling": False,
            "third_action_jet_is_necessary_input": True,
            "actual_selected_third_action_jet_tested": False,
            "K590_factorized_completion_retracted": False,
            "source_action_rejected": False,
            "next_exact_input": "Serialize the selected first action's third Frechet derivative at the same stationary background on the K441 corrected carrier, restrict it to the K589 degree sectors, and test both linearized K444 squares before nilpotence and properness.",
        },
        "source_and_ledger_context": {
            "source_claims": ["SC-ACT-01", "SC-ACT-02", "SC-ACT-06", "SC-META-53"],
            "physics_rows": ["LT-SM8", "LT-GR6b", "RA-F1", "AC-F1"],
            "ledger": "lab/process/conditional-physics-ledger-v0.263.json",
            "source_polarity_effect": "none",
            "ledger_effect": "none",
        },
        "preflight_bookend": {
            "route_comparison": "Test variational identifiability before expanding any 46,592-dimensional nonfactorized arrow; the action Hessian and the first variation of that Hessian are different jets.",
            "retrieval_collision_result": "K443--K446 classify arbitrary compatible controls and K590 instantiates the factorized Hessian-owned complex, but no predecessor proves that the selected Hessian cannot own the missing carrier dependence.",
            "strongest_alternative": "Directly differentiate the complete selected action a third time; this is the positive successor once its carrier and stationary background are fixed.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Saying the selected action has no nonfactorized coupling, rather than that its serialized Hessian does not determine one.",
            "strongest_contrary_construction": "A selected nonzero third action jet could choose the compatible control and close the squares, or the hostile control and fail them, without changing K585's Hessian.",
            "weakest_reproducibility_seam": "The exact control proves jet-level non-identifiability on a minimal trace pair; applying it to the selected action requires serializing that action's actual third derivative.",
        },
        "claim_ceiling": "Exact variational identifiability boundary: K585/K588's selected stationary Hessian fixes the linear action-orbit block but cannot determine the first nonfactorized corrected-carrier dependence, which is a third action jet. Exact symmetric cubic controls share the same Hessian while giving either zero or rank-128 linearized boundary-square defect. This does not show that the selected action lacks such a jet, does not choose either control, and does not construct the nonlinear BV/KT complex or move source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusions.",
    }


def validate(payload: dict) -> None:
    selected = payload["selected_native_inputs"]
    controls = payload["exact_controls"]
    decision = payload["decision"]
    if selected["hessian_block_shape"] != [1470, 91] or selected["hessian_block_rank"] != 91:
        raise AssertionError("selected Hessian typing changed")
    if selected["hessian_gram_scalar"] != "50/257049" or selected["factorized_carrier_rank"] != 512:
        raise AssertionError("selected Hessian/carrier data changed")
    if not controls["all_actions_share_background_hessian"] or not controls["all_three_third_jets_distinct"]:
        raise AssertionError("identifiability controls failed")
    if controls["compatible_control"]["typed_square_defect_rank"] != 0 or controls["hostile_exchange_control"]["typed_square_defect_rank"] != 2:
        raise AssertionError("typed-square controls failed")
    if controls["hostile_exchange_actual_commutator_rank"] != 128:
        raise AssertionError("actual rank transfer changed")
    if decision["K585_K588_hessian_determines_nonfactorized_carrier_coupling"] or not decision["third_action_jet_is_necessary_input"]:
        raise AssertionError("decision boundary changed")
    if decision["actual_selected_third_action_jet_tested"] or decision["source_action_rejected"]:
        raise AssertionError("K592 overclaimed selected-action effect")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
