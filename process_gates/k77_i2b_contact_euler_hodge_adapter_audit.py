#!/usr/bin/env python3
"""Durability gate for v0.222 contact/Euler Hodge adapter."""

from __future__ import annotations

import json
from pathlib import Path

from conditional_physics_ledger_v03_scope_audit import reaches_historical_snapshot


ROOT = Path(__file__).resolve().parents[1]
required = [
    "explorations/conditional-build/conditional-physics-ledger-v0.222.md",
    "explorations/conditional-build/selected-k77-i2b-contact-euler-hodge-adapter-2026-08-12.md",
    "lab/process/conditional-physics-ledger-v0.222.json",
    "lab/process/hostile-reviews/2026-08-12-selected-k77-i2b-contact-euler-hodge-adapter-review.md",
    "lab/process/selected-k77-i2b-contact-euler-hodge-adapter.json",
    "lab/evidence/predecessor-records/i2b-contact-euler-hodge-adapter.md",
    "lab/sources/selected-k77-i2b-contact-euler-hodge-adapter-source-return-2026-08-12.md",
    "tests/channel-swings/conditional_physics_ledger_v0222_probe.py",
    "tests/channel-swings/selected_k77_i2b_contact_euler_hodge_adapter_probe.py",
]
checks: list[tuple[str, bool, bool]] = []


def strict(relative: str):
    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key} in {relative}")
            out[key] = value
        return out

    return json.loads((ROOT / relative).read_text(), object_pairs_hook=hook)


def check(name: str, condition: object, planted: bool = False) -> None:
    checks.append((name, bool(condition), planted))


for relative in required:
    check(f"exists:{relative}", (ROOT / relative).is_file())

registry = strict(required[4])
ledger = strict(required[2])
prior = strict("lab/process/conditional-physics-ledger-v0.221.json")
report = (ROOT / required[1]).read_text()
review = (ROOT / required[3]).read_text()
source = (ROOT / required[6]).read_text()
contract = (ROOT / "lab/methods/research-evidence-contract-v1.0.md").read_text()
contract_data = strict("lab/methods/research-evidence-contract-v1.0.json")
lanes = (ROOT / "lab/process/RESEARCH-AGENDA.json").read_text()

check("ledger_current", ledger["status"] == "CURRENT_APPEND_ONLY_LEDGER_V0_222")
check("ledger_predecessor", ledger["predecessor"].endswith("v0.221.json"))
check("headline_unchanged", ledger["progress"]["verdict_counts"] == prior["progress"]["verdict_counts"])
check("accounting_unchanged", all(
    ledger["residue"][key] == prior["residue"][key]
    for key in ("continuous_real", "function_valued_at_least", "open_discrete_forks", "quotients_ranked")
))
check("three_migrations", sum(item.get("to_version") == "0.222" for item in ledger["migration_history"]) == 3)
check("migrated_rows", {item["row_id"] for item in ledger["migration_history"] if item.get("to_version") == "0.222"} == {"RA-E1", "RA-E3", "LT-SM6"})
check("fingerprints", registry["structure_fingerprints"] == {
    "contact": "OMEGA1_TENSOR_CL2__DIM16__ACTION_OWNED_CONTACT_TANGENT__POINTWISE",
    "principal_euler_response": "OMEGA13_TENSOR_CL2__BANK196__EULER_ADMISSIBLE_VARIATION__POINTWISE",
    "lower_euler_response": "OMEGA13_TENSOR_CL1__BANK196__EULER_ADMISSIBLE_VARIATION__POINTWISE",
})
check("raw_pairing_zero", registry["shortcut_checks"]["raw_trace_hq_pairing_principal_rank"] == 0 and registry["shortcut_checks"]["raw_trace_hq_pairing_lower_rank"] == 0)
check("active_intersection", registry["hodge_principal_intersection"]["dimension"] == 4 and registry["hodge_principal_intersection"]["carrier"] == "OBSERVER_ACTIVE_QUARTET")
check("source_three_cokernel_one", registry["hodge_principal_intersection"]["trace_hq_source_intersection_dimension"] == 3 and registry["hodge_principal_intersection"]["local_contact_cokernel_intersection_dimension"] == 1)
check("lower_disjoint", registry["hodge_lower_intersection_dimension"] == 0)
check("radial_euler", registry["action_selection"].startswith("E3_RADIAL_EULER_COEFFICIENT_EXACT"))
check("primary_carrier", registry["carrier"]["primary"].startswith("C32_32_PLUS"))
check("h_homonym", "HMINUS_EQUALS_X_OF_SPLUS" in registry["carrier"]["h_homonym"])
check("hostile_three_charges", all(f"Charge {index}" in review for index in (1, 2, 3)))
check("required_lenses", all(word in review for word in ("Layer-0", "Prior art", "Symplectic", "Analytic")))
check("source_silent", "Source-silent" in source and "Q_B" in source)
check(
    "contract_ancestry",
    reaches_historical_snapshot(
        contract_data,
        "lab/process/conditional-physics-ledger-v0.222.json",
    ),
)
check(
    "lanes_live_pointer",
    contract_data["standing_ledger"]["ref"] in lanes,
)
check("no_status_change", registry["claim_status_change"] == registry["canon_verdict_change"] == registry["public_posture_change"] == "NONE")
check("stationary_zero_not_selection", "does not turn that" in report and "direction on at its stationary point" in report, planted=True)
check("no_global_section", "pointwise" in report and "global associated-bundle" in report, planted=True)
check("no_lower_order_hodge", "separate Shiab/Riesz" in report, planted=True)
check("no_new_datum", "P1/P2/P3 remain unchanged and unused" in report, planted=True)

failed = [name for name, passed, _ in checks if not passed]
exact = sum(not planted for _, _, planted in checks)
planted = sum(planted for _, _, planted in checks)
print(f"CHECKS={exact} exact + {planted} planted; failures={len(failed)}")
if failed:
    print("FAILED=" + ",".join(failed))
    raise SystemExit(1)
print("RESULT=PASS: historical v0.222 I2B contact/Euler certificate remains exact beneath the live append-only ledger")
