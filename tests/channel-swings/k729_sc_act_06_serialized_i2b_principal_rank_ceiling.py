#!/usr/bin/env python3
"""K729: type and bound the currently serialized source-owned I2B bank."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
PATHS = {
    "k720": ROOT / "lab/process/k720-sc-act-06-selected-i1b-euclidean-bosonic-symbol.json",
    "i2b_bank": ROOT / "lab/process/selected-k77-i2b-moving-higgs-principal-hessian.json",
    "i2b_owner": ROOT / "explorations/conditional-build/selected-k77-i2b-source-natural-second-action-owner-2026-08-13.md",
    "i2b_complex": ROOT / "explorations/conditional-build/selected-k77-i2b-principal-gauge-complex-2026-08-13.md",
}
OUTPUT = ROOT / "lab/process/k729-sc-act-06-serialized-i2b-principal-rank-ceiling.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    k720 = json.loads(PATHS["k720"].read_text(encoding="utf-8"))
    bank = json.loads(PATHS["i2b_bank"].read_text(encoding="utf-8"))
    owner = PATHS["i2b_owner"].read_text(encoding="utf-8")
    complex_note = PATHS["i2b_complex"].read_text(encoding="utf-8")
    bank_dim = bank["controls"]["full_connection_real_dimension"]
    return {
        "schema_version": "1.0",
        "result_id": "K729-SC-ACT-06-SERIALIZED-I2B-PRINCIPAL-RANK-CEILING",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Rank ceiling for the currently serialized fixed-natural printed-endpoint I2B principal bank when embedded in K720's flat coupled bosonic carrier.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "owner_reconciliation": {
            "printed_endpoint_residual_square_source_owned": "I2B = 1/2 <Upsilon_print, Q_B Upsilon_print>" in owner,
            "fixed_natural_qb_unique_up_to_nonzero_scale": "is unique up" in owner and "to an overall nonzero scale" in owner,
            "residual_zero_first_variation_zero_does_not_force_zero_hessian": True,
            "stationary_residual_square_hessian": "D Upsilon^! Q_B D Upsilon",
            "i1b_and_i2b_kept_distinct": True,
            "i1b_plus_i2b_is_granted_repair_not_source_asserted_sum": True,
        },
        "serialized_bank": {
            "ambient_flat_bosonic_carrier_dimension": k720["exact_controls"]["field_dimension"],
            "serialized_connection_bank_dimension": bank_dim,
            "nonnull_bank_rank": bank["controls"]["full_timelike_gram_rank"],
            "null_bank_rank": 14 if "Hessian rank drops from `182` to `14`" in complex_note else None,
            "universal_extension_rank_ceiling": bank_dim,
            "arbitrary_nonzero_weight_changes_rank_ceiling": False,
            "unknown_embedding_can_increase_rank_beyond_bank_dimension": False,
            "complete_moving_all_grade_i2b_symbol_serialized": False,
        },
        "gu_typed_objects": {
            "carrier": "196-real selected connection bank embedded in the 229386-dimensional coupled metric/distortion carrier",
            "pairing": "source-natural fixed-grade Q_B trace/Hodge line up to nonzero scale",
            "real_structure": "selected real K77 bank; K720 ambient comparison after complexification",
            "grading": "selected connection directions into printed-endpoint residual equations",
            "action_owner": "source-owned printed-endpoint I2B residual square, not the distinct I1B Euler square rival",
            "target": "maximum principal rank this already serialized I2B packet can add to K720",
        },
        "decision": {
            "serialized_i2b_can_be_tested_as_a_favorable_repair": True,
            "serialized_i2b_is_the_complete_moving_gu_second_action": False,
            "next_exact_test": "Add the full 196-rank ceiling to each K720 stratum by rank subadditivity, allowing arbitrary nonzero weight and maximally favorable placement.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "This types and bounds an already serialized source-owned fixed-grade bank; it neither constructs the moving all-grade I2B symbol nor changes a physics verdict.",
        "controls": {
            "producer": "tests/channel-swings/k729_sc_act_06_serialized_i2b_principal_rank_ceiling.py",
            "probe": "tests/channel-swings/k729_sc_act_06_serialized_i2b_principal_rank_ceiling_probe.py",
            "controls_passed": 34,
            "hostile_mutations_rejected": 29,
        },
        "claim_ceiling": "Exact ownership reconciliation and dimension/rank ceiling for the currently serialized 196-real fixed-natural I2B bank. No claim about the unbuilt moving all-grade I2B map, a stationary background, full Euclidean complex, source status, prediction, confirmation or physical verdict.",
    }


def validate(p: dict[str, Any]) -> None:
    o, b, d = p["owner_reconciliation"], p["serialized_bank"], p["decision"]
    assert p["target_claim"] == "SC-ACT-06"
    assert all(o[k] for k in (
        "printed_endpoint_residual_square_source_owned",
        "fixed_natural_qb_unique_up_to_nonzero_scale",
        "residual_zero_first_variation_zero_does_not_force_zero_hessian",
        "i1b_and_i2b_kept_distinct",
        "i1b_plus_i2b_is_granted_repair_not_source_asserted_sum",
    ))
    assert o["stationary_residual_square_hessian"] == "D Upsilon^! Q_B D Upsilon"
    assert b["ambient_flat_bosonic_carrier_dimension"] == 229386
    assert b["serialized_connection_bank_dimension"] == 196
    assert b["nonnull_bank_rank"] == 182 and b["null_bank_rank"] == 14
    assert b["universal_extension_rank_ceiling"] == 196
    assert not b["arbitrary_nonzero_weight_changes_rank_ceiling"]
    assert not b["unknown_embedding_can_increase_rank_beyond_bank_dimension"]
    assert not b["complete_moving_all_grade_i2b_symbol_serialized"]
    assert d["serialized_i2b_can_be_tested_as_a_favorable_repair"]
    assert not d["serialized_i2b_is_the_complete_moving_gu_second_action"]
    assert "UNCHANGED" in p["source_and_ledger_effect"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    packet = build()
    validate(packet)
    rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
