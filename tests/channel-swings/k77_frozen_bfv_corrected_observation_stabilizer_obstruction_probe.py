#!/usr/bin/env python3
"""Independent rebuild and hostile controls for the K77 stabilizer obstruction."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/k77_frozen_bfv_corrected_observation_stabilizer_obstruction.py"
STORED = ROOT / "lab/process/k77-frozen-bfv-corrected-observation-stabilizer-obstruction.json"

spec = importlib.util.spec_from_file_location("k77_stabilizer_target", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K77 stabilizer producer")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


def main() -> int:
    stored = json.loads(STORED.read_text())
    rebuilt = module.build()
    module.validate_payload(stored)
    rho = (Fraction(5, 2), Fraction(3, 2), Fraction(1, 2))
    spin = (Fraction(1, 2), Fraction(1, 2), Fraction(1, 2))
    spin_casimir = sum((x * (x + 2 * r) for x, r in zip(spin, rho)), Fraction())
    checks = [
        ("byte-content rebuild", stored == rebuilt),
        ("ambient split", 21 + 21 + 49 == 91),
        ("orbit split", 21 + 7 * 7 == 70),
        ("target split", 16 * 8 == 128),
        ("trivial Casimir", module.b3_casimir((Fraction(0),) * 3) == 0),
        ("vector Casimir", module.b3_casimir((Fraction(1), Fraction(0), Fraction(0))) == 6),
        ("spinor Casimir", spin_casimir == Fraction(21, 4)),
        ("spectral separation", {Fraction(0), Fraction(6)}.isdisjoint({spin_casimir})),
        ("Hom rank zero", stored["decision"]["equivariant_hom_rank"] == 0),
        ("quotient route retained", stored["decision"]["quotient_descent_route"].startswith("open")),
        ("Green route retained", stored["decision"]["green_compatible_route"].startswith("open")),
        ("all release controls", all(stored["release_test"].values())),
    ]
    failed = [name for name, ok in checks if not ok]
    if failed:
        raise AssertionError(f"K77 independent controls failed: {failed}")

    mutations = [
        lambda p: p.__setitem__("classification", "PHYSICAL_NO_GO"),
        lambda p: p["orbit_decomposition"].__setitem__("trivial_copies", 20),
        lambda p: p["orbit_decomposition"].__setitem__("vector_copies", 8),
        lambda p: p["orbit_decomposition"].__setitem__("orbit_dimension_replay", 69),
        lambda p: p["target_restriction"].__setitem__("full_real_spinor_dimension", 64),
        lambda p: p["target_restriction"].__setitem__("odd_axis_spinor_copies", 8),
        lambda p: p["target_restriction"].__setitem__("trace_lift_has_trivial_or_vector_summand", True),
        lambda p: p["casimir_certificate"]["eigenvalues"].__setitem__("vector", "21/4"),
        lambda p: p["casimir_certificate"].__setitem__("source_target_spectra_disjoint", False),
        lambda p: p["decision"].__setitem__("equivariant_hom_rank", 1),
        lambda p: p["decision"].__setitem__("nonzero_full_orbit_to_trace_intertwiner_exists", True),
        lambda p: p["decision"].__setitem__("quotient_descent_route", "closed"),
        lambda p: p["decision"].__setitem__("green_compatible_route", "derived"),
        lambda p: p.__setitem__("retained_repairs", []),
        lambda p: p["release_test"].__setitem__("no_source_ledger_canon_paper_public_or_physical_effect", False),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(stored)
        mutate(candidate)
        try:
            module.validate_payload(candidate)
        except AssertionError:
            rejected += 1
    if rejected != len(mutations):
        raise AssertionError(f"hostile rejection failed: {rejected}/{len(mutations)}")
    print(f"K77 stabilizer probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
