#!/usr/bin/env python3
"""Exact M-M12 functorial/class-map certificate.

The ambient input is the already-derived group Omega^Pin+_14 = Z/2. This
certificate separates the ambient group, a U(1)-valued character, and the
class of a particular GU cycle, which is presently undefined.
"""

from __future__ import annotations

from dataclasses import dataclass, replace

import pin_smith_class_realization_gate as realization


Element = int
Phase = int


@dataclass(frozen=True)
class Receipt:
    ambient_order: int
    character: tuple[Phase, Phase]
    gu_class: Element | None
    claimed_phase: Phase | None


TRIVIAL = (1, 1)
SIGN = (1, -1)


def add(left: Element, right: Element) -> Element:
    return (left + right) % 2


def is_character(values: tuple[Phase, Phase]) -> bool:
    return (
        values[0] == 1
        and all(value in (-1, 1) for value in values)
        and all(
            values[add(left, right)] == values[left] * values[right]
            for left in (0, 1)
            for right in (0, 1)
        )
    )


def phase(values: tuple[Phase, Phase], cycle: Element | None) -> Phase | None:
    return None if cycle is None else values[cycle]


def validate(receipt: Receipt) -> list[str]:
    errors: list[str] = []
    if receipt.ambient_order != 2:
        errors.append("ambient group must remain Z/2")
    if not is_character(receipt.character):
        errors.append("partition-function shadow is not a character")
    if receipt.gu_class not in (None, 0, 1):
        errors.append("GU class is outside the typed Z/2 codomain")
    expected = phase(receipt.character, receipt.gu_class)
    if receipt.claimed_phase != expected:
        errors.append("claimed phase does not follow from character evaluation")
    if receipt.gu_class is None and receipt.claimed_phase is not None:
        errors.append("an undefined class cannot emit an anomaly phase")
    return errors


def check(label: str, condition: bool, failures: list[str]) -> None:
    print(f"{'PASS' if condition else 'FAIL'}: {label}")
    if not condition:
        failures.append(label)


def main() -> int:
    failures: list[str] = []

    check("Z/2 has the trivial character", is_character(TRIVIAL), failures)
    check("Z/2 has the sign character", is_character(SIGN), failures)
    check("the trivial character is +1 on both classes", TRIVIAL == (1, 1), failures)
    check("the sign character detects only the generator", SIGN == (1, -1), failures)
    truth_table = (
        phase(TRIVIAL, 0), phase(TRIVIAL, 1),
        phase(SIGN, 0), phase(SIGN, 1),
    )
    check("the exact character/class truth table is (+1,+1,+1,-1)", truth_table == (1, 1, 1, -1), failures)
    check("undefined GU class returns no phase", phase(SIGN, None) is None, failures)

    native_complete = [candidate.name for candidate in realization.CANDIDATES if candidate.complete()]
    check("no committed GU candidate supplies the complete class-map interface", native_complete == [], failures)
    control = next(candidate for candidate in realization.CANDIDATES if candidate.route == "control")
    check("the external generator control fails only program-native ownership", not control.complete() and control.first_failure == "program_native", failures)

    baseline = Receipt(2, SIGN, None, None)
    check("clean M-M12 receipt validates before mutations", validate(baseline) == [], failures)
    if failures:
        print("BASELINE RED; refusing mutation accounting")
        return 1

    mutations = [
        ("ambient-group/class conflation", replace(baseline, ambient_order=1)),
        ("zero class assigned generator phase", Receipt(2, SIGN, 0, -1)),
        ("undefined class assigned anomaly phase", Receipt(2, SIGN, None, -1)),
        ("trivial character claimed to protect generator", Receipt(2, TRIVIAL, 1, -1)),
    ]
    caught = 0
    for label, mutant in mutations:
        errors = validate(mutant)
        detected = bool(errors)
        check(f"mutation caught: {label}", detected, failures)
        if detected:
            caught += 1
            print(f"  detected by: {errors[0]}")
    check("all four logical conflations are caught", caught == 4, failures)
    if failures:
        return 1

    print("PIN14 INVERTIBLE-FIELD-THEORY CLASS-MAP: 14/14 CHECKS PASS; 4/4 MUTATIONS CAUGHT")
    print("VERDICT: FUNCTORIAL STATEMENT CLOSED; GU CLASS REALIZATION UNDEFINED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
