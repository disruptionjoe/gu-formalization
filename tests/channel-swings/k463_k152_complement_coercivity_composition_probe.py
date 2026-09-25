#!/usr/bin/env python3
"""Independent controls and hostile mutations for K463."""

from __future__ import annotations

import argparse
import copy
import json
from fractions import Fraction
from pathlib import Path

from k463_k152_complement_coercivity_composition import CertificateError, compose_rank_one_and_coercivity, demo


ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k463-k152-complement-coercivity-composition.json"
NARRATIVE = ROOT / "explorations/conditional-build/k463-k152-complement-coercivity-composition-2026-09-25.md"


def controls(packet: dict) -> list[tuple[str, bool]]:
    theorem = packet.get("theorem", {})
    control = packet.get("exact_positive_control", {})
    certificate = control.get("certificate", {})
    outward = packet.get("outward_nonsquare_control", {})
    outward_certificate = outward.get("certificate", {})
    boundary = packet.get("substitution_boundary", {})
    readiness = packet.get("current_native_readiness", {})
    decision = packet.get("decision", {})
    artifact = json.loads(ARTIFACT.read_text(encoding="utf-8"))
    narrative = NARRATIVE.read_text(encoding="utf-8")
    return [
        ("schema", packet.get("schema_version") == "1.0"),
        ("id", packet.get("result_id") == "K463-K152-COMPLEMENT-COERCIVITY-COMPOSITION"),
        ("classification", packet.get("classification") == "INTERNAL_STRUCTURAL_ONLY"),
        ("direction", packet.get("direction") == "observed_to_native"),
        ("M geometry", "M-Hilbert" in theorem.get("geometry", "")),
        ("strict premise", theorem.get("premises", [None])[0] == "rho<b<beta"),
        ("rank theorem", "rank 1_" in theorem.get("count", "")),
        ("floor formula", "sqrt" in theorem.get("global_floor", "")),
        ("nonidentity M", control.get("physical_metric", [])[0] == ["1", "1", "0"]),
        ("exact block", control.get("block_form_in_M_orthonormal_coordinates", [])[0] == ["-2", "3/2", "0"]),
        ("full inertia", control.get("full_pencil_inertia_at_b") == [1, 0, 2]),
        ("exact spectrum", control.get("exact_generalized_spectrum") == ["-5/2", "5/2", "3"]),
        ("count one", certificate.get("spectral_count_strictly_below_b") == 1),
        ("strict order", certificate.get("strict_order") == "rho < b < beta"),
        ("discriminant", certificate.get("discriminant") == "25"),
        ("floor exact", certificate.get("global_lower_floor_outward_interval") == ["-5/2", "-5/2"]),
        ("coercive", certificate.get("shifted_coercivity_lower") == "1/2"),
        ("nonsquare outward", outward.get("discriminant_is_nonsquare") is True and outward_certificate.get("discriminant") == "13"),
        ("sqrt outward width", Fraction(outward_certificate.get("sqrt_discriminant_outward_interval", ["0", "0"])[1]) - Fraction(outward_certificate.get("sqrt_discriminant_outward_interval", ["0", "0"])[0]) == Fraction(1, 65536)),
        ("floor outward ordered", Fraction(outward_certificate.get("global_lower_floor_outward_interval", ["0", "0"])[0]) < Fraction(outward_certificate.get("global_lower_floor_outward_interval", ["0", "0"])[1])),
        ("outward coercive", Fraction(outward_certificate.get("shifted_coercivity_lower", "0")) > 0),
        ("same form", certificate.get("same_fixed_limiting_form") is True),
        ("complete Q", certificate.get("complete_charge_sector_complement") is True),
        ("not native", control.get("control_is_native_K162_packet") is False),
        ("HVZ fenced", boundary.get("K169_HVZ_threshold_member_is_complete_Q_floor") is False),
        ("finite fenced", boundary.get("K447_K453_independent_finite_rebuild_is_same_limiting_form") is False),
        ("column fenced", boundary.get("K456_K457_trial_column_or_residual_determines_Q_floor") is False),
        ("native refs missing", len(readiness.get("missing_native_references", [])) == 5),
        ("no native count", readiness.get("native_rank_one_below_b_certificate_emitted") is False),
        ("no native coercivity", readiness.get("native_center_zero_coercivity_emitted") is False),
        ("K461 open", readiness.get("K461_relative_readiness_complete") is False),
        ("theorem complete", decision.get("composition_theorem_complete") is True),
        ("constants open", decision.get("native_constants_evaluated") is False),
        ("artifact agrees", artifact.get("result_id") == packet.get("result_id") and artifact.get("current_native_readiness") == readiness),
        ("narrative boundary", all(token in narrative for token in ("K169", "finite independent rebuild", "native constants", "remain open", "M-orthogonal"))),
    ]


def input_rejections() -> list[tuple[str, bool]]:
    base = dict(
        trial_rayleigh=-2,
        count_threshold=0,
        complete_complement_floor=2,
        cross_action_norm_upper="3/2",
        coercive_shift=3,
        fixed_limiting_form_ref="R",
        physical_metric_ref="M",
        trial_line_ref="u",
        complete_m_complement_ref="Q",
        cross_action_column_ref="ell",
        same_fixed_limiting_form=True,
        complete_charge_sector_complement=True,
    )
    cases = [
        ("rho reaches b", {"trial_rayleigh": 0}),
        ("b reaches beta", {"count_threshold": 2}),
        ("negative eta", {"cross_action_norm_upper": -1}),
        ("shift too small", {"coercive_shift": 2}),
        ("finite rebuild", {"same_fixed_limiting_form": False}),
        ("incomplete Q", {"complete_charge_sector_complement": False}),
        ("missing form", {"fixed_limiting_form_ref": None}),
        ("missing metric", {"physical_metric_ref": None}),
        ("missing trial", {"trial_line_ref": None}),
        ("missing Q proof", {"complete_m_complement_ref": None}),
        ("missing cross proof", {"cross_action_column_ref": None}),
    ]
    caught = []
    for name, update in cases:
        kwargs = dict(base)
        kwargs.update(update)
        try:
            compose_rank_one_and_coercivity(**kwargs)
        except CertificateError:
            caught.append((name, True))
        else:
            caught.append((name, False))
    return caught


def hostile_selftest(packet: dict) -> tuple[int, int]:
    mutations = [
        lambda d: d.__setitem__("schema_version", "0"),
        lambda d: d.__setitem__("result_id", "K462"),
        lambda d: d.__setitem__("classification", "PHYSICAL"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d["theorem"].__setitem__("geometry", "free Hilbert"),
        lambda d: d["theorem"].__setitem__("premises", ["rho<=b"]),
        lambda d: d["theorem"].__setitem__("count", "unknown"),
        lambda d: d["theorem"].__setitem__("global_floor", "none"),
        lambda d: d["exact_positive_control"].__setitem__("full_pencil_inertia_at_b", [2, 0, 1]),
        lambda d: d["exact_positive_control"].__setitem__("exact_generalized_spectrum", ["-2", "2", "3"]),
        lambda d: d["exact_positive_control"]["certificate"].__setitem__("spectral_count_strictly_below_b", 2),
        lambda d: d["exact_positive_control"]["certificate"].__setitem__("global_lower_floor_outward_interval", ["-3", "-2"]),
        lambda d: d["exact_positive_control"]["certificate"].__setitem__("shifted_coercivity_lower", "0"),
        lambda d: d["outward_nonsquare_control"].__setitem__("discriminant_is_nonsquare", False),
        lambda d: d["exact_positive_control"]["certificate"].__setitem__("same_fixed_limiting_form", False),
        lambda d: d["exact_positive_control"]["certificate"].__setitem__("complete_charge_sector_complement", False),
        lambda d: d["exact_positive_control"].__setitem__("control_is_native_K162_packet", True),
        lambda d: d["substitution_boundary"].__setitem__("K169_HVZ_threshold_member_is_complete_Q_floor", True),
        lambda d: d["substitution_boundary"].__setitem__("K447_K453_independent_finite_rebuild_is_same_limiting_form", True),
        lambda d: d["substitution_boundary"].__setitem__("K456_K457_trial_column_or_residual_determines_Q_floor", True),
        lambda d: d["current_native_readiness"].__setitem__("missing_native_references", []),
        lambda d: d["current_native_readiness"].__setitem__("native_rank_one_below_b_certificate_emitted", True),
        lambda d: d["current_native_readiness"].__setitem__("native_center_zero_coercivity_emitted", True),
        lambda d: d["current_native_readiness"].__setitem__("K461_relative_readiness_complete", True),
        lambda d: d["decision"].__setitem__("native_constants_evaluated", True),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(packet)
        mutate(candidate)
        if not all(ok for _, ok in controls(candidate)):
            rejected += 1
    return rejected, len(mutations)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    packet = demo()
    checks = controls(packet)
    rejections = input_rejections()
    print(f"K463 EXACT CONTROL: {sum(ok for _, ok in checks)}/{len(checks)} pass")
    print(f"K463 INPUT REJECTIONS: {sum(ok for _, ok in rejections)}/{len(rejections)} caught")
    if args.selftest:
        rejected, total = hostile_selftest(packet)
        print(f"K463 HOSTILE MUTATIONS: {rejected}/{total} rejected")
    else:
        rejected = total = 0
    return 0 if all(ok for _, ok in checks + rejections) and (not args.selftest or rejected == total) else 1


if __name__ == "__main__":
    raise SystemExit(main())
