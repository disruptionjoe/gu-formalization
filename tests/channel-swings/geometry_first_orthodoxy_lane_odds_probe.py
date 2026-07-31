#!/usr/bin/env python3
"""Contract checks for the ten-lens geometry-first orthodoxy audit."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "lab/process/geometry-first-orthodoxy-ten-lens-council.json"

exact_checks = 0
planted_checks = 0


def exact(name: str, condition: bool) -> None:
    global exact_checks
    if not condition:
        raise AssertionError(name)
    exact_checks += 1


def planted(name: str, false_claim: bool) -> None:
    global planted_checks
    if false_claim:
        raise AssertionError(f"planted false claim passed: {name}")
    planted_checks += 1


def main() -> None:
    data = json.loads(CERT.read_text())
    lenses = data["lens_odds"]
    audit = {row["id"]: row for row in data["assumption_audit"]}

    exact("same ten specialist lenses retained", len(lenses) == 10 and {row["id"] for row in lenses} == set(range(1, 11)))
    exact("every forced lane comparison sums to 100", all(row["guided"] + row["control"] == 100 for row in lenses))
    exact("aggregate odds are explicitly refused", data["odds_reporting_policy"]["aggregate"] == "NOT_REPORTED_BY_USER_DIRECTION")
    exact("each specialist retains a reason", all(row["reason"] for row in lenses))
    exact("dimension-14 result is separated from supplied starting data", {row["id"]: row["class"] for row in data["four_to_fourteen_boundary"]}["Y14_DIMENSION"] == "FORCED_FROM_METRIC_BUNDLE" and {row["id"]: row["class"] for row in data["four_to_fourteen_boundary"]}["GAUGE_ARENA"] == "SECTORAL_OR_FIELD_ARENA_INPUT")
    exact("explicit Yang-Mills is classified as inserted", audit["N1_YANG_MILLS"]["class"] == "ORTHODOX_TEMPLATE_INSERTION")
    exact("Yukawa and flavor matrices are classified as inserted", audit["N1_YUKAWA_FLAVOR"]["class"] == "ORTHODOX_TEMPLATE_INSERTION")
    exact("SW defect is classified as inserted", audit["N1_SW_DEFECT"]["class"] == "ORTHODOX_TEMPLATE_INSERTION")
    exact("G3 Euler Noether boundary packet is action-derived", audit["G3_EULER_NOETHER_BOUNDARY"]["class"] == "ACTION_DERIVED_CONSEQUENCE")
    exact("SM and cosmology remain downstream tests", audit["SM_DIAGNOSTICS"]["class"] == audit["COSMO_DIAGNOSTICS"]["class"] == "DOWNSTREAM_HOSTILE_TEST")
    exact("in-sample template agreement has zero confirmation weight", all(audit[key]["evidence_weight_for_SM_fit"] == 0 for key in ("N1_YANG_MILLS", "N1_DIRAC_RS", "N1_SW_DEFECT", "N1_YUKAWA_FLAVOR", "BARE_LAMBDA")))
    exact("ablation and target-blind enumeration are both required", any("ablate" in test for test in data["decisive_tests"]) and any("target-blind" in test for test in data["decisive_tests"]))
    exact("next swing does not displace G4", "does not replace" in data["next_swing"]["relationship"])

    planted("four dimensions alone force the gauge arena", {row["id"]: row["class"] for row in data["four_to_fourteen_boundary"]}["GAUGE_ARENA"] == "FORCED_FROM_METRIC_BUNDLE")
    planted("an inserted Yang-Mills term is an emitted result", audit["N1_YANG_MILLS"]["class"] == "ACTION_DERIVED_CONSEQUENCE")
    planted("free Yukawa matrices provide held-out SM confirmation", audit["N1_YUKAWA_FLAVOR"]["evidence_weight_for_SM_fit"] > 0)
    planted("lane odds are probabilities that GU is true", not data["odds_scope"]["not_probability_of"])
    planted("ten heterogeneous specialist odds may be collapsed", data["odds_reporting_policy"]["aggregate"] != "NOT_REPORTED_BY_USER_DIRECTION")
    planted("G3.5 may select its natural basis using PP3 labels", "PP3 labels allowed" in data["next_swing"]["output"])

    print(
        "GEOMETRY-FIRST-ORTHODOXY-LANE-ODDS: "
        f"{exact_checks} exact checks + {planted_checks} planted failures = "
        f"{exact_checks + planted_checks} PASS"
    )
    print("RESULT: ten separate guided/control odds are retained with no aggregate")
    print("RESULT: dimension-14 emergence is separated from gauge, action, SM, and datum inputs")
    print("RESULT: G3.5 target-blind enumeration plus N1 ablation precedes downstream scoring")
    print("BOUNDARY: no probability that GU is true, lane success, SM emergence, or cosmological emission")


if __name__ == "__main__":
    main()
