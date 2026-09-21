#!/usr/bin/env python3
"""Independent K271 Machin and common-normalization replay."""

from __future__ import annotations

import copy
import hashlib
import json
import re
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k271-tight-common-pi-normalization-reenclosure.json"
SOURCES = {
    "K265": ("lab/process/k265-order-nine-complete-binary-low-high-union.json", "complete_binary_union"),
    "K266": ("lab/process/k266-order-nine-first-fixed-axis-middle-collar.json", "complete_collar"),
    "K267": ("lab/process/k267-order-nine-exchangeable-axis-middle-collar.json", "complete_collar"),
    "K268": ("lab/process/k268-order-nine-two-exchangeable-axis-middle-collar.json", "complete_collar"),
    "K269": ("lab/process/k269-order-nine-three-plus-exchangeable-axis-middle-collar.json", "complete_collar"),
}
BALL = re.compile(r"\[([^ ]+) \+/- ([^\]]+)\]")
C = Fraction(2**8 * 256**6, 120)


def h(value: Fraction) -> str:
    return hashlib.sha256(str(value).encode()).hexdigest()


def ball(text: str) -> tuple[Fraction, Fraction]:
    match = BALL.fullmatch(text)
    assert match is not None
    center, radius = Fraction(match.group(1)), Fraction(match.group(2))
    return center - radius, center + radius


def atan_pair(inverse: int, odd_index: int) -> tuple[Fraction, Fraction]:
    x = Fraction(1, inverse)
    lower = sum(((-1) ** k * x ** (2 * k + 1) / (2 * k + 1) for k in range(odd_index + 1)), Fraction())
    upper = lower + x ** (2 * odd_index + 3) / (2 * odd_index + 3)
    return lower, upper


def metadata_ok(data: dict) -> bool:
    r4 = data.get("reassessment_disposition", {}).get("R4", {})
    boundaries = data.get("boundaries", {})
    return all(
        (
            data.get("classification") == "INTERNAL_STRUCTURAL_ONLY",
            data.get("direction") == "observed_to_native",
            r4.get("state") == "concluded",
            r4.get("new_boxes_compiled") is False,
            boundaries.get("uncomputed_K218_complement_controlled") is False,
            boundaries.get("full_K218_integral_sign") is False,
            boundaries.get("K270_native_consumer_inputs_instantiated") is False,
            boundaries.get("physics_ledger_change") is False,
            boundaries.get("paper_or_public_posture_change") is False,
        )
    )


def main() -> int:
    data = json.loads(MANIFEST.read_text())
    certificate = data["certificate"]
    recorded_pi = certificate["machin_pi"]
    pi_lower, pi_upper = Fraction(recorded_pi["lower"]), Fraction(recorded_pi["upper"])

    # Independent, strictly tighter alternating truncations: indices 51 and 13
    # are odd, so each partial is a lower endpoint and the next term supplies
    # the preceding even upper endpoint.
    a_lower, a_upper = atan_pair(5, 51)
    b_lower, b_upper = atan_pair(239, 13)
    check_lower = 16 * a_lower - 4 * b_upper
    check_upper = 16 * a_upper - 4 * b_lower
    checks = [
        ("metadata", metadata_ok(data)),
        ("pi ordered", 3 < pi_lower < pi_upper < 4),
        ("independent pi nested", pi_lower < check_lower < check_upper < pi_upper),
        ("common member order", certificate["common_sum"]["members"] == list(SOURCES)),
    ]

    raw_lower = Fraction()
    raw_upper = Fraction()
    old_lower = Fraction()
    old_upper = Fraction()
    tighter_factor_lower = C / check_upper**8
    tighter_factor_upper = C / check_lower**8
    for result_id, (relative, key) in SOURCES.items():
        payload = (ROOT / relative).read_bytes()
        source = json.loads(payload)[key]
        rl, _ = ball(source["complete_raw_integral_interval"]["lower"])
        _, ru = ball(source["complete_raw_integral_interval"]["upper"])
        ol, _ = ball(source["normalized_integral_interval"]["lower"])
        _, ou = ball(source["normalized_integral_interval"]["upper"])
        row = certificate["per_result"][result_id]
        checks.extend(
            [
                (f"{result_id} source hash", row["source_sha256"] == hashlib.sha256(payload).hexdigest()),
                (f"{result_id} raw interval hash", row["raw_interval_exact_sha256"] == hashlib.sha256(f"{rl}|{ru}".encode()).hexdigest()),
                (f"{result_id} old width hash", row["published_coarse_width_exact_sha256"] == h(ou - ol)),
            ]
        )
        producer_tight = row["tight_normalized"]
        # The independent narrower pi interval must produce a normalized
        # enclosure inside the producer's recorded exact-hash enclosure.
        producer_lower = rl * (C / pi_upper**8)
        producer_upper = ru * (C / pi_lower**8)
        check_tight_lower = rl * tighter_factor_lower
        check_tight_upper = ru * tighter_factor_upper
        checks.extend(
            [
                (f"{result_id} tight lower hash", producer_tight["lower_exact_sha256"] == h(producer_lower)),
                (f"{result_id} tight upper hash", producer_tight["upper_exact_sha256"] == h(producer_upper)),
                (f"{result_id} independent nested", producer_lower < check_tight_lower < check_tight_upper < producer_upper),
                (f"{result_id} width improves", producer_upper - producer_lower < ou - ol),
            ]
        )
        raw_lower += rl
        raw_upper += ru
        old_lower += ol
        old_upper += ou

    common = certificate["common_sum"]
    common_lower = raw_lower * (C / pi_upper**8)
    common_upper = raw_upper * (C / pi_lower**8)
    checks.extend(
        [
            ("common raw lower", common["raw_symbolic_sum"]["lower_exact_sha256"] == h(raw_lower)),
            ("common raw upper", common["raw_symbolic_sum"]["upper_exact_sha256"] == h(raw_upper)),
            ("common tight lower", common["tight_common_normalized"]["lower_exact_sha256"] == h(common_lower)),
            ("common tight upper", common["tight_common_normalized"]["upper_exact_sha256"] == h(common_upper)),
            ("common width improves", common_upper - common_lower < old_upper - old_lower),
        ]
    )
    failed = [name for name, ok in checks if not ok]
    if failed:
        print(f"FAIL independent K271 replay: {failed}")
        return 1

    mutations = [
        lambda d: d.__setitem__("classification", "PHYSICS_RESULT"),
        lambda d: d["reassessment_disposition"]["R4"].__setitem__("state", "pending"),
        lambda d: d["reassessment_disposition"]["R4"].__setitem__("new_boxes_compiled", True),
        lambda d: d["boundaries"].__setitem__("uncomputed_K218_complement_controlled", True),
        lambda d: d["boundaries"].__setitem__("full_K218_integral_sign", True),
        lambda d: d["boundaries"].__setitem__("K270_native_consumer_inputs_instantiated", True),
        lambda d: d["boundaries"].__setitem__("physics_ledger_change", True),
        lambda d: d["boundaries"].__setitem__("paper_or_public_posture_change", True),
    ]
    caught = 0
    for mutation in mutations:
        trial = copy.deepcopy(data)
        mutation(trial)
        if not metadata_ok(trial):
            caught += 1
    if caught != len(mutations):
        print(f"FAIL hostile metadata caught {caught}/{len(mutations)}")
        return 1
    print(f"PASS independent K271 replay {len(checks)}/{len(checks)}; hostile metadata {caught}/{len(mutations)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
