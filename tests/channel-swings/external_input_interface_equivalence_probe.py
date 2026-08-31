#!/usr/bin/env python3
"""Exact finite controls for the external-input interface theorem.

The model validates interface bookkeeping and hostile failure paths.  It does
not enumerate GU's physical inputs or establish the proposed exhaustive split.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Hashable, Iterable


ROOT = Path(__file__).resolve().parents[2]
CHECKS: list[str] = []


def check(label: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(label)
    CHECKS.append(label)


Port = Hashable
Code = tuple[str, Hashable]


@dataclass(frozen=True)
class FiniteInterface:
    ports: tuple[Port, ...]
    codes: tuple[Code, ...]
    encode: Callable[[Port], Code]
    decode: Callable[[Code], Port]

    def left_failures(self) -> tuple[Port, ...]:
        return tuple(port for port in self.ports if self.decode(self.encode(port)) != port)

    def right_failures(self) -> tuple[Code, ...]:
        return tuple(code for code in self.codes if self.encode(self.decode(code)) != code)

    def is_exact(self) -> bool:
        return not self.left_failures() and not self.right_failures()


BASE_PORTS = (
    "causal-orientation",
    "reservoir-sign",
    "absolute-scale",
    "count-anchor",
)
BASE_CODES: tuple[Code, ...] = (
    ("TIEBREAKER", "causal-orientation"),
    ("TIEBREAKER", "reservoir-sign"),
    ("SETTING", "absolute-scale"),
    ("SETTING", "count-anchor"),
)
BASE_ENCODE = dict(zip(BASE_PORTS, BASE_CODES, strict=True))
BASE_DECODE = dict(zip(BASE_CODES, BASE_PORTS, strict=True))


def baseline_interface() -> FiniteInterface:
    return FiniteInterface(
        BASE_PORTS,
        BASE_CODES,
        BASE_ENCODE.__getitem__,
        BASE_DECODE.__getitem__,
    )


def run_exactness_controls() -> None:
    baseline = baseline_interface()
    check("EXACT.baseline_left_triangle", baseline.left_failures() == ())
    check("EXACT.baseline_right_triangle", baseline.right_failures() == ())
    check("EXACT.baseline_is_bijection", baseline.is_exact())
    check(
        "EXACT.tags_are_disjoint",
        {code[0] for code in baseline.codes} == {"TIEBREAKER", "SETTING"},
    )


def run_hostile_controls() -> None:
    baseline = baseline_interface()

    # A third kind increases the external carrier without adding a tagged code.
    third_ports = baseline.ports + ("history-update",)
    third_encode = dict(BASE_ENCODE)
    third_encode["history-update"] = BASE_CODES[0]
    planted_third = FiniteInterface(
        third_ports,
        baseline.codes,
        third_encode.__getitem__,
        BASE_DECODE.__getitem__,
    )
    check("HOSTILE.planted_third_type_rejected", not planted_third.is_exact())
    check(
        "HOSTILE.planted_third_witness_is_left_failure",
        planted_third.left_failures() == ("history-update",),
    )

    # Both tagged summands decode to one object: explicit overlap/double count.
    overlap_decode = dict(BASE_DECODE)
    overlap_decode[("SETTING", "absolute-scale")] = "causal-orientation"
    overlap = FiniteInterface(
        baseline.ports,
        baseline.codes,
        BASE_ENCODE.__getitem__,
        overlap_decode.__getitem__,
    )
    check("HOSTILE.overlap_double_count_rejected", not overlap.is_exact())
    check(
        "HOSTILE.overlap_hits_right_triangle",
        ("SETTING", "absolute-scale") in overlap.right_failures(),
    )

    # Equal finite cardinality does not save an encoder that omits one port.
    missing_encode = dict(BASE_ENCODE)
    missing_encode["absolute-scale"] = ("SETTING", "count-anchor")
    missing = FiniteInterface(
        baseline.ports,
        baseline.codes,
        missing_encode.__getitem__,
        BASE_DECODE.__getitem__,
    )
    check("HOSTILE.missing_port_rejected", not missing.is_exact())
    check(
        "HOSTILE.missing_port_witness_is_left_failure",
        "absolute-scale" in missing.left_failures(),
    )

    # Same set cardinality, incompatible automorphism data.
    external_flip = {False: True, True: False}
    code_identity = {False: False, True: True}
    carrier_equiv = {False: False, True: True}
    symmetry_respects = all(
        carrier_equiv[external_flip[value]] == code_identity[carrier_equiv[value]]
        for value in (False, True)
    )
    check("HOSTILE.nontrivial_automorphism_detected", not symmetry_respects)

    # A first-result selector changes when the same solutions are enumerated
    # in the reverse order, exposing solver order as an undeclared input.
    solutions = ("world-a", "world-b", "world-c")
    first = lambda items: items[0]
    check(
        "HOSTILE.hidden_solver_order_detected",
        first(solutions) != first(tuple(reversed(solutions))),
    )


SOURCE_MARKERS = {
    "Lean/GUFormalization/ExternalInputInterface.lean": (
        "exists_exact_decoder_iff_bijective",
        "planted_third_type_control",
        "overlap_double_count_control",
        "missing_port_control",
        "nontrivial_automorphism_control",
        "hidden_solver_order_control",
    ),
    "explorations/external-input-interface-equivalence-2026-08-31.md": (
        "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.",
        "EXHAUSTIVE TWO-TYPE EQUIVALENCE IS NOT ESTABLISHED",
        "No source claim, canon verdict, action owner, prediction or physical input census moves.",
    ),
}


def source_marker_errors(
    markers: dict[str, tuple[str, ...]],
) -> tuple[str, ...]:
    errors: list[str] = []
    for relative, expected in markers.items():
        text = (ROOT / relative).read_text(encoding="utf-8")
        for marker in expected:
            if marker not in text:
                errors.append(f"{relative}: missing {marker}")
    return tuple(errors)


def run_source_controls() -> None:
    check("SOURCE.required_markers_present", source_marker_errors(SOURCE_MARKERS) == ())


def run() -> None:
    run_exactness_controls()
    run_hostile_controls()
    run_source_controls()
    print(f"external-input interface probe: {len(CHECKS)}/{len(CHECKS)} checks passed")
    for label in CHECKS:
        print(f"PASS {label}")


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--selftest",
        action="store_true",
        help="run the exact baseline and all hostile controls",
    )
    parser.parse_args(argv)
    run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
