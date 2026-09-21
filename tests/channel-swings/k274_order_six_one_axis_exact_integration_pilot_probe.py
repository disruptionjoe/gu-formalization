#!/usr/bin/env python3
"""Independent direct-quadrature replay and hostile controls for K274."""
from __future__ import annotations

from fractions import Fraction as Q
import json
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[2]
PROCESS = ROOT / "lab/process"
SOURCE = PROCESS / "k185-order-six-duffy-face-tail-wave.json"
RECORD = PROCESS / "k274-order-six-one-axis-exact-integration-pilot.json"
AXIS = 1
GENERIC_C = (Q(5, 4), Q(0), Q(17, 8), Q(9, 8), Q(13, 8), Q(21, 8), Q(25, 8), Q(29, 8))


def independent_terms(source: dict):
    catalog = source["exact_allocation_certificate"]["allocation_catalog"]
    for entry in reversed(source["complete_face_hypergraph"]["entries"]):
        outer = entry["coefficient_product"] * (2 if entry["left"] != entry["right"] else 1)
        for term in reversed(entry["terms"]):
            masks = tuple(int(value, 16) for value in
                          catalog[term["allocation_id"]]["support_masks_hex"].split(","))
            yield outer * term["leibniz_sign"], masks


def prepared_rows(items: list, coshes: tuple[Q, ...]):
    rows = []
    for weight, masks in items:
        participating = []
        prefactor = Q(weight)
        for load_index in reversed(range(14)):
            base = Q(256) + sum((coshes[j] for j in reversed(range(8))
                                 if j != AXIS and masks[j] & (1 << load_index)), Q(0))
            if masks[AXIS] & (1 << load_index): participating.append(base)
            else: prefactor /= base
        rows.append((mp.mpf(prefactor.numerator) / prefactor.denominator,
                     tuple(mp.mpf(value.numerator) / value.denominator for value in participating)))
    measure = mp.mpf(1)
    for axis, value in enumerate(coshes):
        if axis != AXIS: measure *= mp.mpf(value.numerator) / value.denominator
    return rows, measure


def direct_integrand(t, rows, measure, *, omit_measure: bool = False):
    c = mp.cosh(t)
    total = mp.mpf(0)
    for prefactor, loads in rows:
        denominator = mp.mpf(1)
        for load in loads: denominator *= load + c
        total += prefactor / denominator
    return total if omit_measure else measure * c * total


def integrate(function, upper=100):
    cuts = [value for value in (0, 1, 2, 4, 8, 16, 32, 64) if value < upper] + [upper]
    return mp.quad(function, cuts)


def midpoint(value: str):
    return mp.mpf(value.split()[0].lstrip("["))


def main() -> None:
    mp.mp.dps = 90
    source = json.loads(SOURCE.read_text())
    record = json.loads(RECORD.read_text())
    items = list(independent_terms(source))
    assert len(items) == 1864
    rows, measure = prepared_rows(items, GENERIC_C)
    value = integrate(lambda t: direct_integrand(t, rows, measure))
    expected = midpoint(record["controls"]["generic_integrated_value_without_common_constant_or_pi8"])
    assert abs(value - expected) < mp.mpf("1e-80")

    exact_checks = 0
    assert [sum(masks[axis].bit_count() for _, masks in items) for axis in range(8)] == record["selection"]["all_axis_participating_load_totals"]; exact_checks += 1
    assert record["controls"]["generic_stats"]["exact_polynomial_reconstructions"] == len(items); exact_checks += 1
    assert abs(value - expected) < mp.mpf("1e-80"); exact_checks += 1
    assert record["controls"]["native_load_separation"]["strict_support_chains"] == len(items); exact_checks += 1

    repeated = lambda t: mp.cosh(t) / ((mp.mpf(257) + mp.cosh(t)) ** 2
                                       * (mp.mpf(258) + mp.cosh(t)))
    repeated_value = integrate(repeated)
    repeated_expected = midpoint(record["controls"]["artificial_confluent_control"]["integrated_value"])
    assert abs(repeated_value - repeated_expected) < mp.mpf("1e-80"); exact_checks += 1

    hostile_checks = 0
    truncated = integrate(lambda t: direct_integrand(t, rows, measure), upper=8)
    assert abs(truncated - value) > mp.mpf("1e-40"); hostile_checks += 1
    wrong_measure = integrate(lambda t: direct_integrand(t, rows, measure, omit_measure=True))
    assert abs(wrong_measure - value) > mp.mpf("1e-34"); hostile_checks += 1
    assert any(order == "2" for order in ["2"] if record["controls"]["artificial_confluent_control"]["contains_second_order_pole"]); hostile_checks += 1

    print(f"[PASS] K274 independent direct replay {exact_checks}/5 exact, {hostile_checks}/3 hostile")


if __name__ == "__main__":
    main()
