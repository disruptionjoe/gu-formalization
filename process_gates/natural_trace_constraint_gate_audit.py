#!/usr/bin/env python3
"""Fail-closed scope audit for the v0.169 natural trace-constraint gate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKS = 0


def strict(relative: str):
    path = ROOT / relative

    def reject_duplicates(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise AssertionError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(), object_pairs_hook=reject_duplicates)


def read(relative: str) -> str:
    return (ROOT / relative).read_text()


def check(label: str, condition: object) -> None:
    global CHECKS
    CHECKS += 1
    assert condition, label
    print(f"PASS {label}")


prior = strict("lab/process/conditional-physics-ledger-v0.168.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.169.json")
result = strict("lab/process/selected-k77-natural-trace-constraint-gate.json")
report = read("explorations/conditional-build/selected-k77-natural-trace-constraint-gate-2026-08-11.md")
review = read("lab/process/hostile-reviews/2026-08-11-selected-k77-natural-trace-constraint-gate-review.md")
source = read("lab/sources/selected-k77-natural-trace-constraint-gate-source-return-2026-08-11.md")
lanes = read("LANES.yaml")
next_steps = read("NEXT-STEPS.md")
status = read("RESEARCH-STATUS.md")
contract = strict("lab/process/functional-channel-operating-contract-v1.0.json")

check("ledger advances exactly once", ledger["schema_version"] == "0.169" and ledger["predecessor"].endswith("v0.168.json"))
check("headline counts unchanged", ledger["progress"]["verdict_counts"] == prior["progress"]["verdict_counts"])
check("coverage remains 82 of 82", ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82)
check("residue remains 84", ledger["residue"]["continuous_real"] == prior["residue"]["continuous_real"] == 84)
check("five scoped quotients remain", ledger["residue"]["quotients_ranked"] == prior["residue"]["quotients_ranked"] == 5)
check("one frontier condition closes", ledger["frontier_delta"]["conditions_closed"] == 1)
check("no new frontier condition opens", ledger["frontier_delta"]["conditions_opened"] == 0)
check("natural family is complete only at zero order", result["natural_family"]["complete_scope"].startswith("Spin-natural zero-order"))
check("unique propagated line is typed", result["propagation"]["unique_projective_line"] == "[a:b]=[2:-1]")
check("constraint equation is exact", result["propagation"]["constraint"] == "C=2 Gamma(zeta)-nu")
check("Jordan image stays in constraint kernel", result["jordan_test"]["image_N_j_inside_kernel_C"] is True)
check("restricted Jordan rank remains 128", result["jordan_test"]["rank_N_j_restricted_to_kernel_C"] == 128)
check("restricted remainder stays square zero", result["jordan_test"]["N_j_square_zero_after_restriction"] is True)
check("zero-order repair is rejected", result["jordan_test"]["repairs_positive_hyperbolicity"] is False)
check("direction-fitted control fires", result["controls"]["direction_fitted_Q_j_would_kill_N_j"] is True and result["controls"]["Q_x_equals_Q_y"] is False)
check("source does not select constraint", result["selection"]["source_selects_constraint"] is False)
check("no BV differential is manufactured", result["selection"]["bv_differential_constructed"] is False)
check("no quotient is manufactured", result["selection"]["quotient_constructed"] is False)
check("P1 P2 P3 remain unused", result["accounting"]["P1_P2_P3"] == "UNCHANGED_UNUSED")
check("six rows migrate", len(ledger["wave_row_dispositions"]) == 6)
check("expected rows migrate", {item["row_id"] for item in ledger["wave_row_dispositions"]} == {"RA-D4", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1"})
check("source return is explicit", ledger["source_return"].startswith("SOURCE_CONFIRMS_PHYSICAL_NU_ZETA"))
check("hostile charge one scopes the theorem", "zero-order spinor-valued" in review)
check("hostile charge two preserves physical versus BV typing", "physical relation" in review and "ghost/BV" in review)
check("hostile charge three retains live routes", "needs-recheck" in review and "nonzero-southeast" in review)
check("source return records silence", "SOURCE-SILENT" in source and "does not state or derive" in source)
check("human report refuses all-constraint overclaim", "does not reach" in report.lower() or "live routes" in report.lower())
check("lanes points at v0.169", "conditional-physics-ledger-v0.169.json" in lanes)
check("contract points at v0.169", contract["standing_ledger"]["ref"].endswith("v0.169.json"))
check("next steps names nonlocal successor", "Craig-Weinstein-style nonlocal" in next_steps)
check("research status carries scoped result", "natural zero-order constraint route is killed" in status)
check("canon and public posture do not move", result["accounting"]["canon_change"] is False and result["accounting"]["public_posture_change"] is False)

print(f"PASS: {CHECKS}/{CHECKS} natural trace-constraint process checks")
