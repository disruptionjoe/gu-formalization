#!/usr/bin/env python3
"""Audit the GU research-portfolio and hourly/steward orchestration contract.

This is a process and routing gate. It checks that the machine-readable portfolio,
human front door, runbooks, collision policy, and Lean guard agree. It does not
validate any mathematical or physical claim.
"""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PORTFOLIO = ROOT / "lab" / "process" / "research-portfolio.json"
NEXT_STEPS = ROOT / "NEXT-STEPS.md"
DAILY_RUNBOOK = (
    ROOT / "lab" / "process" / "runbooks" / "daily-research-portfolio-stewardship.md"
)
HOURLY_RUNBOOK = (
    ROOT / "lab" / "process" / "runbooks" / "meaningful-hourly-progress-swing.md"
)
LEAN_RUNBOOK = ROOT / "lab" / "process" / "runbooks" / "lean-verification-run.md"
LEAN_LEDGER = ROOT / "lab" / "process" / "lean-verification-lane-LEDGER.md"
LEAN_GUARD = ROOT / "lab" / "automation" / "check-lean.ps1"
PAPER_INVENTORY = ROOT / "lab" / "process" / "paper-hardening-inventory.md"
PAPER_SEED_RUNBOOK = (
    ROOT / "lab" / "process" / "runbooks" / "draft-factory-paper-seed-handoff.md"
)
RECOVERY_MATRIX = ROOT / "lab" / "process" / "recovery-certification-matrix.json"
RECOVERY_ASSESSMENT = (
    ROOT / "lab" / "process" / "recovery-certification-assessment-2026-07-15.md"
)
NO_GO_DEFENSE_PROTOCOL = (
    ROOT / "lab" / "process" / "recovery-no-go-defense-protocol.md"
)
NO_GO_DEFENSE_REGISTER = (
    ROOT / "lab" / "process" / "recovery-no-go-defense-register.json"
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class ResearchPortfolioContractAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.portfolio = json.loads(read(PORTFOLIO))
        cls.lanes = cls.portfolio["lane_catalog"]
        cls.lane_by_id = {lane["id"]: lane for lane in cls.lanes}
        cls.work_items = cls.portfolio["work_items"]
        cls.top_by_id = {item["id"]: item for item in cls.work_items}
        cls.by_id = dict(cls.top_by_id)
        for item in cls.work_items:
            for internal in item.get("internal_work_items", []):
                if internal["id"] in cls.by_id:
                    raise AssertionError(f"duplicate work-item id: {internal['id']}")
                cls.by_id[internal["id"]] = internal
        cls.next_steps = read(NEXT_STEPS)
        cls.current_frontdoor = cls.next_steps.split(
            "[SUPERSEDED as the hourly queue by the steward-maintained portfolio above",
            1,
        )[0]

    def test_ids_are_unique_and_dependencies_resolve(self) -> None:
        lane_ids = [lane["id"] for lane in self.lanes]
        self.assertEqual(len(lane_ids), len(set(lane_ids)))
        ids = [item["id"] for item in self.work_items]
        ids.extend(
            internal["id"]
            for item in self.work_items
            for internal in item.get("internal_work_items", [])
        )
        self.assertEqual(len(ids), len(set(ids)))
        for item_id, item in self.by_id.items():
            with self.subTest(work_item=item_id):
                missing = [dep for dep in item.get("depends_on", []) if dep not in self.by_id]
                self.assertEqual([], missing)

    def test_states_and_hourly_eligibility_are_consistent(self) -> None:
        allowed = set(self.portfolio["operational_states"])
        ineligible = {
            "WAITING_EXTERNAL",
            "GATED_P2C",
            "GATED_NEW_STRUCTURE",
            "GATED_FIXED_QUANTITY",
            "MONITOR",
            "PARKED",
            "RESOLVED_NO_GO",
            "PAPER_READY",
            "NEEDS_JOE",
        }
        for item in self.work_items:
            with self.subTest(work_item=item["id"]):
                self.assertIn(item["state"], allowed)
                if item["state"] in ineligible:
                    self.assertFalse(item["hourly_eligible"])

    def test_three_progress_lanes_and_lane_a_stewardship(self) -> None:
        contract = self.portfolio["selection_contract"]
        self.assertEqual({"1", "2", "3", "A"}, set(self.lane_by_id))
        self.assertEqual(["1", "2", "3"], contract["progress_lane_ids"])
        self.assertEqual(["A"], contract["administrative_lane_ids"])
        self.assertEqual("1", contract["protected_north_star_lane_id"])
        self.assertEqual("A", contract["standard_stewardship_lane_id"])
        self.assertEqual(1, contract["max_concurrent_progress_runs"])
        self.assertTrue(contract["lane_one_is_protected_from_difficulty_demotion"])
        self.assertEqual("protected_north_star", self.lane_by_id["1"]["purpose_priority"])
        self.assertEqual("administrative", self.lane_by_id["A"]["lane_type"])
        self.assertFalse(self.lane_by_id["A"]["hourly_eligible"])
        self.assertIn("Lane A never enters", contract["end_of_run_rerank_rule"])
        self.assertIn("purpose, not an automatic", contract["scheduling_rule"])
        self.assertIn("actual falsification", contract["north_star_rule"])
        self.assertEqual(
            "DEP-NATIVE-SOURCE-DATUM", contract["deepest_open_dependency_work_item_id"]
        )
        self.assertEqual(
            {"1", "2", "3", "A"},
            {item["lane_id"] for item in self.work_items},
        )
        for lane in self.lanes:
            self.assertIn(lane["current_top_work_item_id"], self.top_by_id)
            self.assertEqual(
                lane["id"], self.top_by_id[lane["current_top_work_item_id"]]["lane_id"]
            )
        self.assertIn("transferred", contract["deepest_open_problem_posture"])

    def test_priority_scores_match_declared_formula(self) -> None:
        scored_items = [item for item in self.by_id.values() if "score" in item]
        for item in scored_items:
            score = item["score"]
            expected = (
                2 * score["impact"]
                + 2 * score["information_gain"]
                + score["readiness"]
                + score["distinctiveness"]
                + score["time_sensitivity"]
                - score["effort"]
                - score["wall_risk"]
                - score["duplication_risk"]
            )
            with self.subTest(work_item=item["id"]):
                self.assertEqual(expected, item["priority_score"])
                self.assertTrue(all(1 <= value <= 5 for value in score.values()))

    def test_scientific_scope_constraints_are_not_flattened(self) -> None:
        mirror = self.by_id["MIRROR-NATIVE-ROUTE"]
        physical_c = self.by_id["PHYSICAL-C-BOUNDARY"]
        physical_c_conditional = self.by_id["PHYSICAL-C-CONDITIONAL"]
        source_datum = self.by_id["DEP-NATIVE-SOURCE-DATUM"]
        f1 = self.by_id["DE-F1-TRIPWIRE"]

        self.assertEqual("RESOLVED_NO_GO", mirror["state"])
        self.assertIn("everything GU natively builds", mirror["current_authority"])
        self.assertIn("GU-non-native", mirror["next_swing"])
        self.assertEqual("GATED_P2C", physical_c["state"])
        self.assertIn("closed-interior", physical_c["current_authority"])
        self.assertEqual(
            {"DEP-NATIVE-SOURCE-DATUM", "DEP-PROP1", "DEP-W235-RECORD"},
            set(physical_c["depends_on"]),
        )
        self.assertEqual("READY", physical_c_conditional["state"])
        self.assertIn("explicit adapter assumption", physical_c_conditional["title"])
        self.assertIn("not a GU construction", physical_c_conditional["construction_fork"])
        self.assertEqual("GATED_P2C", source_datum["state"])
        self.assertIn("deepest unresolved GU-native dependency", source_datum["current_authority"])
        self.assertIn("+1.11", f1["current_authority"])
        self.assertIn("+0.032", f1["current_authority"])
        self.assertIn("not the firing margin", f1["current_authority"])
        self.assertIn("never a positive GU prediction", f1["forbidden_shortcut"])
        self.assertIn("W226-harden-de-tripwire", f1["evidence_source"])

    def test_recovery_certification_is_one_adaptive_lane(self) -> None:
        recovery = self.by_id["RECOVERY-CERTIFICATION"]
        rerank = recovery["internal_rerank_contract"]
        items = recovery["internal_work_items"]

        self.assertEqual("1", recovery["lane_id"])
        self.assertEqual("ACTIVE", recovery["state"])
        self.assertTrue(recovery["hourly_eligible"])
        self.assertTrue(rerank["one_workstream_not_sublanes"])
        self.assertTrue(rerank["rerank_after_every_swing"])
        self.assertIn("Next-Work Handoff", rerank["handoff_rule"])
        self.assertEqual(
            "lab/process/recovery-certification-matrix.json",
            recovery["assessment_source"],
        )
        self.assertTrue(RECOVERY_MATRIX.is_file())
        self.assertTrue(RECOVERY_ASSESSMENT.is_file())
        self.assertIn("possibility-to-capability", recovery["owner"])
        self.assertIn("Subgroup containment", recovery["forbidden_shortcut"])
        self.assertEqual(
            {
                "NO-GO-SCOPE-CHALLENGE",
                "RECOVERY-CONTRACT",
                "SM-CONSISTENT-SECTOR",
                "GR-DYNAMICAL-BENCHMARKS",
                "QM-PHYSICAL-SECTOR",
                "COSMO-PERTURBATIONS",
                "ADAPTER-RETURN-CERTIFICATION",
            },
            {item["id"] for item in items},
        )
        self.assertEqual("NO-GO-SCOPE-CHALLENGE", items[0]["id"])
        self.assertEqual("READY", items[0]["state"])

        item_ids = {item["id"] for item in items}
        for item in items:
            score = item["score"]
            expected = (
                2 * score["impact"]
                + 2 * score["information_gain"]
                + score["readiness"]
                + score["distinctiveness"]
                + score["time_sensitivity"]
                - score["effort"]
                - score["wall_risk"]
                - score["duplication_risk"]
            )
            with self.subTest(internal_work_item=item["id"]):
                self.assertEqual(expected, item["priority_score"])
                self.assertTrue(set(item["depends_on"]).issubset(item_ids))

        flavor = self.by_id["PRED-FLAVOR-RANK"]
        normalization = self.by_id["PRED-NORM-RANK"]
        flavor_obs = self.by_id["PRED-FLAVOR-OBS"]
        fixed = self.by_id["FIXED-NATIVE-QUANTITY"]
        blind = self.by_id["BLIND-QUANTITATIVE-CONFRONTATION"]
        self.assertEqual("RESOLVED_NO_GO", flavor["state"])
        self.assertEqual("RESOLVED_NO_GO", normalization["state"])
        self.assertEqual("RESOLVED_NO_GO", flavor_obs["state"])
        self.assertEqual("2", fixed["lane_id"])
        self.assertEqual("2", blind["lane_id"])
        self.assertIn("two free dimensionless ratios", flavor["current_authority"])
        self.assertIn("no GU-native absolute scale", normalization["current_authority"])

    def test_branch_no_go_defense_and_conditional_unitarity_are_executable(self) -> None:
        recovery = self.by_id["RECOVERY-CERTIFICATION"]
        defense = recovery["no_go_defense_contract"]
        items = {item["id"]: item for item in recovery["internal_work_items"]}
        register = json.loads(read(NO_GO_DEFENSE_REGISTER))
        protocol = read(NO_GO_DEFENSE_PROTOCOL)

        self.assertTrue(NO_GO_DEFENSE_PROTOCOL.is_file())
        self.assertTrue(NO_GO_DEFENSE_REGISTER.is_file())
        self.assertTrue(defense["history_audit_before_defense"])
        self.assertFalse(defense["history_audit_counts_as_swing"])
        self.assertEqual(3, defense["minimum_broad_swings_per_no_go"])
        self.assertIn("explains more", defense["legitimate_reframe_rule"])
        self.assertEqual(3, register["minimum_broad_swings_per_no_go"])
        self.assertTrue(register["history_audit_required_before_swing_1"])
        self.assertFalse(register["history_audit_counts_as_broad_swing"])
        self.assertEqual("QM-PHYSICAL-SECTOR", register["interleave_after_swing_1_round"])
        six_axis = register["six_axis_consideration"]
        self.assertIn("Layer 0", six_axis["current_form"])
        self.assertEqual(7, len(six_axis["axes"]))
        self.assertIn("first falsification test", six_axis["escape_admission_rule"])
        self.assertIn("UNDERDEFINED", six_axis["underdefinition_rule"])
        self.assertEqual(
            {
                "RECOVERY-NOGO-GR-W229-VACUUM",
                "RECOVERY-NOGO-COSMO-SCALAR",
                "RECOVERY-NOGO-SM-SELECTOR",
            },
            {target["id"] for target in register["targets"]},
        )
        for target in register["targets"]:
            with self.subTest(no_go_target=target["id"]):
                audit = target["history_audit"]
                swing1_or_later_states = {
                    "SWING_2_READY",
                    "SWING_3_READY",
                    "BOUNDED_NO_GO",
                    "CLASS_EXHAUSTED",
                    "REFRAMED_SURVIVOR",
                    "MORE_CONSTRUCTION_SPACE",
                }
                swing2_or_later_states = {
                    "SWING_3_READY",
                    "BOUNDED_NO_GO",
                    "CLASS_EXHAUSTED",
                    "REFRAMED_SURVIVOR",
                    "MORE_CONSTRUCTION_SPACE",
                }
                swing3_complete_states = {
                    "BOUNDED_NO_GO",
                    "CLASS_EXHAUSTED",
                    "REFRAMED_SURVIVOR",
                    "MORE_CONSTRUCTION_SPACE",
                }
                if audit["state"] == "PENDING":
                    self.assertEqual("HISTORY_AUDIT_READY", target["challenge_state"])
                    continue

                self.assertIn(
                    target["challenge_state"],
                    swing1_or_later_states | {"INTEGRITY_CONFLICT"},
                )
                self.assertIn(
                    audit["result"],
                    {"NO_PRIOR_CLEARANCE_FOUND", "INTEGRITY_CONFLICT"},
                )
                self.assertIsInstance(audit["prior_encounters"], list)
                self.assertIsInstance(audit["search_receipt"], dict)

                if target["challenge_state"] in swing1_or_later_states:
                    self.assertTrue(target["completed_swings"])
                    self.assertTrue(
                        any(
                            swing["history_audit_consumed"]
                            and swing["result"]
                            in {
                                "SCOPE_CONFIRMED",
                                "CLASS_RELATIVE",
                                "UNDERDEFINED",
                                "INVALID_NO_GO",
                            }
                            for swing in target["completed_swings"]
                        )
                    )
                if target["challenge_state"] in swing2_or_later_states:
                    self.assertTrue(
                        any(
                            swing.get("swing_1_scope_consumed") is True
                            and swing["result"]
                            in {
                                "NO_SURVIVOR",
                                "SURVIVOR_CANDIDATE",
                                "NEW_DEPENDENCY",
                                "INVALID_ESCAPE",
                            }
                            for swing in target["completed_swings"]
                        )
                    )
                if target["challenge_state"] in swing3_complete_states:
                    self.assertTrue(
                        any(
                            swing.get("swing_2_consumed") is True
                            and swing["result"]
                            in {
                                "CLASS_EXHAUSTED",
                                "BOUNDED_NO_GO",
                                "REFRAMED_SURVIVOR",
                                "MORE_CONSTRUCTION_SPACE",
                            }
                            for swing in target["completed_swings"]
                        )
                    )
        self.assertIn("Mandatory history audit", protocol)
        self.assertIn("Minimum three-swing sequence", protocol)
        self.assertIn("does not count as one of the three", protocol)
        self.assertIn("INTEGRITY_CONFLICT", protocol)
        self.assertIn("Six-axis consideration", protocol)
        self.assertIn("Layer 0 semantic alignment plus L1 through L7", protocol)

        challenge = items["NO-GO-SCOPE-CHALLENGE"]
        self.assertEqual("READY", challenge["state"])
        self.assertIn("HISTORY_AUDIT_READY", challenge["next_swing"])
        self.assertEqual("QM-PHYSICAL-SECTOR", challenge["interleave_after_swing_1_round"])

        quantum = items["QM-PHYSICAL-SECTOR"]
        self.assertIn("supplied boundary adapter", quantum["title"])
        self.assertIn("Does the same frozen GU construction", quantum["conditional_input_question"])
        self.assertIn("CONDITIONAL_COMPLETE", quantum["next_swing"])

    def test_id_namespace_ends_automatic_w_collisions(self) -> None:
        policy = self.portfolio["run_id_policy"]
        self.assertIn("must not allocate a new W number", policy["w_series"])
        self.assertTrue(policy["hourly_pattern"].startswith("GUH-"))
        self.assertTrue(policy["daily_steward_pattern"].startswith("GUS-"))
        self.assertTrue(policy["direct_progress_pattern"].startswith("GUD-"))

    def test_frontdoor_matches_the_portfolio(self) -> None:
        required = (
            "THREE PROGRESS LANES PLUS STEWARDSHIP",
            "Lane 1, GU truth testing",
            "Lane 2, prediction extraction and computation",
            "Lane 3, result hardening and publication readiness",
            "Lane A, Stewardship",
            "Lane 1 always retains the North-Star purpose",
            "rerank-next-work",
            "RECOVERY-CERTIFICATION",
            "NO-GO-SCOPE-CHALLENGE",
            "RECOVERY-CONTRACT",
            "PRED-FLAVOR-RANK",
            "PRED-NORM-RANK",
            "DEP-NATIVE-SOURCE-DATUM",
            "PROOF-STABLE-KERNELS",
            "DE-AMP-DIAGNOSTIC",
            "DE-F1-TRIPWIRE",
            "two-sigma edge margin is `+1.11`",
            "W226-harden-de-tripwire-squeeze-data-2026-07-14.md",
            "GU-002 packages that result",
            "Proposition 1",
            "W235 record bit",
            "`bar(b)` and `H59` remain OPEN",
            "minimum three broad swings",
            "integrity conflict",
            "CONDITIONAL_COMPLETE",
            "no longer allocate W numbers",
        )
        missing = [phrase for phrase in required if phrase not in self.current_frontdoor]
        self.assertEqual([], missing)

    def test_runbooks_and_shared_surface_firewall_exist(self) -> None:
        daily = read(DAILY_RUNBOOK)
        hourly = read(HOURLY_RUNBOOK)
        self.assertIn("valid scientific or dependency signal", daily)
        self.assertIn("is the only routine writer", daily)
        self.assertIn("Lane 1 is GU truth testing", daily)
        self.assertIn("rank Lanes 1 through 3", daily)
        self.assertIn("Lane A", daily)
        self.assertIn("does not mutate or authoritatively reprioritize the portfolio", hourly)
        self.assertIn("Adaptive lane reranking", hourly)
        self.assertIn("Next-Work Handoff", hourly)
        self.assertIn("defines an `assessment_source`", hourly)
        self.assertIn("Within each numbered lane", hourly)
        self.assertIn("Re-rank those three lane leaders", hourly)
        self.assertIn("Exclude Lane A", hourly)
        self.assertIn("Hourly runs do not edit", hourly)
        self.assertIn("Never use `git add -A`", hourly)
        self.assertIn("one meaningful research delta", hourly)
        self.assertIn("paper_seed_proposal", hourly)
        self.assertIn("implicitly equates fit quality", daily)
        self.assertIn("No-go admission and defense", hourly)
        self.assertIn("INTEGRITY_CONFLICT", hourly)
        self.assertIn("history audit does not count", hourly)
        self.assertIn("three-swing defense sequence", daily)

    def test_lean_is_lane_three_method_and_serialized(self) -> None:
        lean_runbook = read(LEAN_RUNBOOK)
        lean_ledger = read(LEAN_LEDGER)
        lean_guard = read(LEAN_GUARD)
        self.assertIn("Lane 3 convergent-hardening", lean_runbook)
        self.assertIn("research-portfolio.json", lean_ledger)
        self.assertIn("Lean queue inside Lane 3", lean_ledger)
        self.assertIn("THEOREM H", lean_ledger)
        self.assertIn("L0 BASELINE", lean_ledger)
        self.assertIn("L1 R4 INTEGRATION", lean_ledger)
        self.assertIn("host-local", lean_guard)
        self.assertIn("FileShare]::None", lean_guard)
        self.assertIn("lake build -j1", lean_guard)

    def test_paper_ceiling_is_recorded_without_external_action(self) -> None:
        inventory = read(PAPER_INVENTORY)
        self.assertIn("READY FOR ZENODO", inventory)
        self.assertIn("arXiv-ready", inventory)
        self.assertIn("NEEDS_JOE", inventory)
        self.assertIn("stop routine polishing", inventory)
        self.assertIn("External review and publication are Joe-gated", inventory)

    def test_draft_factory_seed_seam_is_explicit(self) -> None:
        seam = self.portfolio["publication_seed_seam"]
        daily = read(DAILY_RUNBOOK)
        inventory = read(PAPER_INVENTORY)
        handoff = read(PAPER_SEED_RUNBOOK)

        self.assertEqual("drafting-factory", seam["seed_owner"])
        self.assertIn("immediately", seam["discovery_rule"])
        self.assertIn("not a command", seam["return_rule"])
        self.assertIn("Drafting Factory seam", daily)
        self.assertIn("paper-shaped opportunity", inventory)
        self.assertIn("capacity-backed", inventory)
        self.assertIn("Status: proposed", handoff)
        self.assertIn("Drafting Factory owns", handoff)

    def test_new_orchestration_files_use_no_em_dash(self) -> None:
        files = (
            PORTFOLIO,
            DAILY_RUNBOOK,
            HOURLY_RUNBOOK,
            LEAN_RUNBOOK,
            PAPER_INVENTORY,
            PAPER_SEED_RUNBOOK,
            RECOVERY_MATRIX,
            RECOVERY_ASSESSMENT,
            NO_GO_DEFENSE_PROTOCOL,
            NO_GO_DEFENSE_REGISTER,
        )
        offenders = [path.relative_to(ROOT).as_posix() for path in files if "\u2014" in read(path)]
        self.assertEqual([], offenders)


if __name__ == "__main__":
    unittest.main(verbosity=2)
