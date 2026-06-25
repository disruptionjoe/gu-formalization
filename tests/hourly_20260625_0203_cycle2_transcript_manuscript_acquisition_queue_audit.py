import json
import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_PATH = REPO_ROOT / "explorations" / "hourly-20260625-0203-cycle2-transcript-manuscript-acquisition-queue.md"


def load_json_summary():
    text = ARTIFACT_PATH.read_text(encoding="utf-8")
    blocks = re.findall(r"```json\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    if not blocks:
        raise AssertionError("No JSON summary block found")
    return json.loads(blocks[-1])


class TranscriptManuscriptAcquisitionQueueAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.summary = load_json_summary()
        cls.tasks = cls.summary["acquisition_tasks"]
        cls.task_text = json.dumps(cls.tasks, sort_keys=True)

    def test_artifact_identity(self):
        identity = self.summary["artifact_identity"]
        self.assertEqual(self.summary["artifact"], "TranscriptManuscriptAcquisitionQueue_V1")
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0203-cycle2-transcript-manuscript-acquisition-queue.md",
        )
        self.assertEqual(
            identity["companion_audit"],
            "tests/hourly_20260625_0203_cycle2_transcript_manuscript_acquisition_queue_audit.py",
        )

    def test_at_least_five_acquisition_tasks(self):
        self.assertGreaterEqual(len(self.tasks), 5)

    def test_required_acquisition_surfaces_present(self):
        required = self.summary["required_inclusions"]
        self.assertTrue(required["includes_JRE_extraction"])
        self.assertTrue(required["includes_TOE_Keating_modern_transcript_acquisition"])
        self.assertTrue(required["includes_Oxford_Portal_exact_locator_pass"])
        self.assertTrue(required["includes_UCSD_visual_slide_capture"])
        self.assertTrue(required["includes_2021_manuscript_acquisition"])
        self.assertIn("JRE-1453", self.task_text)
        self.assertIn("JRE-1628", self.task_text)
        self.assertIn("TOE-JAIMUNGAL", self.task_text)
        self.assertIn("KEATING-DESI", self.task_text)
        self.assertIn("OXFORD", self.task_text)
        self.assertIn("UCSD", self.task_text)
        self.assertIn("2021-DRAFT-RELEASE", self.task_text)

    def test_tasks_output_receipt_candidates_not_proof_claims(self):
        for task in self.tasks:
            with self.subTest(source_id=task["source_id"]):
                self.assertTrue(task["outputs_receipt_candidates_not_proof_claims"])
                self.assertIn("no proof claim", task["acceptance_output"])

    def test_parallel_safe_guidance_present(self):
        for task in self.tasks:
            with self.subTest(source_id=task["source_id"]):
                self.assertTrue(task["parallel_safe_guidance_present"])
                self.assertIn("Parallel", task["parallelization_guidance"])

    def test_no_claim_promotion(self):
        self.assertTrue(self.summary["not_a_claim_promotion"])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertTrue(self.summary["receipt_policy"]["claim_promotion_forbidden"])
        self.assertFalse(self.summary["receipt_policy"]["promotion_allowed_at_intake"])
        for promoted in self.summary["no_claim_promotions"].values():
            self.assertFalse(promoted)
        forbidden_text = " ".join(self.summary["forbidden_promotions"])
        self.assertIn("family_proof_restart_before_intake_acceptance", forbidden_text)
        self.assertIn("source_contains_required_object_before_acquired_and_checked", forbidden_text)


if __name__ == "__main__":
    unittest.main()
