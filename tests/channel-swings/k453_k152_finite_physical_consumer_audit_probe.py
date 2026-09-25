#!/usr/bin/env python3
"""Independent controls and hostile mutations for K453."""

from __future__ import annotations

import copy

from k453_k152_finite_physical_consumer_audit import demo


Q00_ALPHA = "250965891222458484365769689/6272010995430339903744000000"
Q10_ALPHA = "4199762151220437726977241661/150528263890328157689856000000"


def controls(packet):
    rows = packet.get("sectors", [])
    decision = packet.get("decision", {})
    return [
        ("schema", packet.get("schema_version") == "1.0"),
        ("id", packet.get("result_id") == "K453-K152-FINITE-PHYSICAL-CONSUMER-AUDIT"),
        ("classification", packet.get("classification") == "INTERNAL_STRUCTURAL_ONLY"),
        ("direction", packet.get("direction") == "observed_to_native"),
        ("three sectors", len(rows) == 3),
        ("charges", [row.get("charge") for row in rows] == [[0, 0], [1, 0], [0, 1]]),
        ("dimensions", [row.get("one_cell_independent_rebuild", {}).get("dimension") for row in rows] == [8, 7, 7]),
        ("Gram differs", all(row.get("physical_Gram_defect_nonzero") is True for row in rows)),
        ("Gram not shared", all(row.get("physical_Gram_exactly_shared") is False for row in rows)),
        ("Gram plus", all(row.get("physical_Gram_plus_certificate_positive_definite") is True for row in rows)),
        ("Gram minus", all(row.get("physical_Gram_minus_certificate_positive_definite") is True for row in rows)),
        ("exact alpha", [row.get("physical_Gram_relative_defect_radius") for row in rows] == [Q00_ALPHA, Q10_ALPHA, Q10_ALPHA]),
        ("consumer changed", all(row.get("rayleigh_difference") != "0" and row.get("dual_residual_square_difference") != "0" for row in rows)),
        ("finite Temple", all("ground_interval" in row.get("one_cell_independent_rebuild", {}).get("finite_dual_temple_result", {}) for row in rows)),
        ("audit complete", decision.get("complete_finite_consumer_quantities_evaluated") is True),
        ("Gram decision", decision.get("physical_Gram_independent_rebuild_defect_certified") is True),
        ("not limiting restriction", decision.get("finite_controls_are_fixed_limiting_K139_form_restrictions") is False),
        ("no native interval", decision.get("native_K152_interval_emitted") is False),
    ]


def main() -> int:
    packet = demo()
    base = controls(packet)
    mutations = [
        lambda d: d.__setitem__("schema_version", "0"),
        lambda d: d.__setitem__("result_id", "K452"),
        lambda d: d.__setitem__("classification", "PHYSICAL"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d["sectors"].pop(),
        lambda d: d["sectors"][1].__setitem__("charge", [0, 0]),
        lambda d: d["sectors"][0]["one_cell_independent_rebuild"].__setitem__("dimension", 7),
        lambda d: d["sectors"][0].__setitem__("physical_Gram_defect_nonzero", False),
        lambda d: d["sectors"][0].__setitem__("physical_Gram_exactly_shared", True),
        lambda d: d["sectors"][0].__setitem__("physical_Gram_plus_certificate_positive_definite", False),
        lambda d: d["sectors"][0].__setitem__("physical_Gram_minus_certificate_positive_definite", False),
        lambda d: d["sectors"][0].__setitem__("physical_Gram_relative_defect_radius", "0"),
        lambda d: d["sectors"][0].__setitem__("rayleigh_difference", "0"),
        lambda d: d["sectors"][0]["one_cell_independent_rebuild"].__setitem__("finite_dual_temple_result", {"certified": False}),
        lambda d: d["decision"].__setitem__("complete_finite_consumer_quantities_evaluated", False),
        lambda d: d["decision"].__setitem__("physical_Gram_independent_rebuild_defect_certified", False),
        lambda d: d["decision"].__setitem__("finite_controls_are_fixed_limiting_K139_form_restrictions", True),
        lambda d: d["decision"].__setitem__("native_K152_interval_emitted", True),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(packet)
        mutate(candidate)
        if not all(ok for _, ok in controls(candidate)):
            rejected += 1
    print(f"K453 EXACT CONTROL: {sum(ok for _, ok in base)}/{len(base)} pass")
    print(f"K453 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
    return 0 if all(ok for _, ok in base) and rejected == len(mutations) else 1


if __name__ == "__main__":
    raise SystemExit(main())
