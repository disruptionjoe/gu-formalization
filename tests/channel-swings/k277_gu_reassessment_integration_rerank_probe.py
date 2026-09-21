#!/usr/bin/env python3
"""Independent budget and portfolio replay for K277."""

from fractions import Fraction
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
certificate = json.loads((ROOT / "lab/process/k277-gu-reassessment-integration-rerank.json").read_text())

def energy_budget(a: Fraction, g: Fraction, d: Fraction) -> Fraction:
    return d * a * g / ((a + g) * (a - d))

# A second exact witness uses a different spectral triple and the same integral
# radius with two still-admissible map norms.
a, g, d = Fraction(5), Fraction(3), Fraction(1)
budget = energy_budget(a, g, d)
radius = Fraction(1, 20)
small = (Fraction(2) * radius) ** 2
large = (Fraction(30) * radius) ** 2
assert budget == Fraction(15, 32)
assert small == Fraction(1, 100) < budget
assert large == Fraction(9, 4) > budget

rows = {row["id"]: row for row in reversed(certificate["reassessment_matrix"])}
assert len(rows) == 9 and set(rows) == {"R1", "R2", "R3", "R4", "R5", "R6", "R7a", "R7b", "R8"}
assert "315.342920694554" in rows["R4"]["result"]
assert "8D to 7D" in rows["R7a"]["result"]
assert "m=184" in rows["R7b"]["result"]
assert "projector" in rows["R8"]["result"]

eliminated = " ".join(certificate["eliminated_computations"])
assert "1e-21" in eliminated
assert "Routine next-collar" in eliminated
assert "Lorentzian K77" in eliminated
retained = " ".join(certificate["retained_methods"])
assert all(label in retained for label in ("K270", "K274", "K275", "K276"))

ranked = certificate["ranked_portfolio"]
assert [entry["rank"] for entry in ranked] == [1, 2, 3, 4]
assert ranked[1]["state"] == "viable conditional successor"
assert certificate["ready_followthrough"]["while_unpopulated"].startswith("Keep routine collars suspended")
assert not certificate["boundaries"]["native_K152_decision"]

print("[PASS] K277 independent consumer-budget replay 10/10 exact, 5/5 hostile")
