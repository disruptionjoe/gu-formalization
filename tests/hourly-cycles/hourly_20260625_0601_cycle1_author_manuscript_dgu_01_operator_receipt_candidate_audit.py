from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "explorations" / (
    "hourly-20260625-0601-cycle1-author-manuscript-dgu-01-operator-receipt-candidate.md"
)


class ActualDGU01OperatorReceiptCandidateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = ARTIFACT.read_text(encoding="utf-8")

    def test_core_identity_and_required_target_strings(self):
        self.assertIn("ActualDGU01OperatorReceiptCandidateFromAuthorManuscript_V1", self.text)
        self.assertIn("D_GU^epsilon 0/1", self.text)
        self.assertIn("actual D_GU^epsilon 0/1 action/operator/EL/principal-symbol data", self.text)

    def test_zero_accepted_receipts_and_restart_guard(self):
        self.assertIn("Accepted receipt count: `0`", self.text)
        self.assertIn('"accepted_receipt_count": 0', self.text)
        self.assertIn("No proof restart unless accepted", self.text)
        self.assertIn('"proof_restart_allowed": false', self.text)
        self.assertIn('"no_proof_restart_unless_accepted": true', self.text)

    def test_first_obstruction_is_exact_identity_gap(self):
        obstruction = "identity_to_actual_D_GU_epsilon_0_1_action_operator_or_EL"
        self.assertIn("The first exact obstruction is:", self.text)
        self.assertIn(obstruction, self.text)
        self.assertIn("not the actual D_GU^epsilon 0/1 action", self.text)


if __name__ == "__main__":
    unittest.main()
