#!/usr/bin/env python3
"""K867: audit the SO(13) equivariance assumed by K863 against the pinned K77 response."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
API = ROOT / "tests/channel-swings/k77_exact_bank_api.py"
OUTPUT = ROOT / "lab/process/k867-sc-act-06-compact-equivariance-audit.json"
PATHS = {
    "bank": ROOT / "tests/fixtures/k77_exact_coefficient_bank_v1.json",
    "k788": ROOT / "lab/process/k788-sc-act-06-direct-response-orbit-classification.json",
    "k863": ROOT / "lab/process/k863-sc-act-06-basepoint-kernel-isotropy.json",
    "k866": ROOT / "lab/process/k866-sc-act-06-isotropy-repair-disposition.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_api():
    spec = importlib.util.spec_from_file_location("k867_k77_api", API)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def signed_rotation(left: int, right: int) -> dict[int, tuple[int, int]]:
    out = {index: (index, 1) for index in range(14)}
    out[left] = (right, 1)
    out[right] = (left, -1)
    return out


def rotate_blade(mask: int, rotation: dict[int, tuple[int, int]]) -> tuple[int, int]:
    images: list[int] = []
    sign = 1
    for index in range(14):
        if mask & (1 << index):
            image, coefficient = rotation[index]
            images.append(image)
            sign *= coefficient
    inversions = sum(images[i] > images[j] for i in range(len(images)) for j in range(i + 1, len(images)))
    if inversions % 2:
        sign *= -1
    return sum(1 << index for index in images), sign


def rotate_form(api, core, value, rotation):
    out = {}
    for form_mask, element in value.items():
        new_form, form_sign = rotate_blade(form_mask, rotation)
        for clifford_mask, coefficient in element.items():
            new_clifford, clifford_sign = rotate_blade(clifford_mask, rotation)
            term = {new_form: {new_clifford: api.gscale(form_sign * clifford_sign, coefficient)}}
            out = core.fadd(out, term)
    return out


def form_terms(value) -> list[list[Any]]:
    return [
        [form_mask, clifford_mask, str(coefficient[0]), str(coefficient[1])]
        for form_mask, element in sorted(value.items())
        for clifford_mask, coefficient in sorted(element.items())
    ]


def preserves_diagonal(rotation: dict[int, tuple[int, int]], diagonal: tuple[int, ...]) -> bool:
    return all(diagonal[index] == diagonal[rotation[index][0]] for index in range(14))


def build() -> dict[str, Any]:
    api = load_api()
    bank = api.load_bank()
    core = api.K77Core(bank.signature, bank.channels)
    q = {1: {0: api.ONE}}
    u1 = {1 << 1: {12: api.ONE}}  # e_1 tensor gamma_{23}
    u2 = {1 << 2: {10: api.ONE}}  # e_2 tensor gamma_{13}
    witness = core.fadd(u1, u2)
    response = core.shiab(core.wedge_raw(q, witness))

    same_sign = signed_rotation(1, 2)
    cross_sign = signed_rotation(1, 4)
    same_rotated = rotate_form(api, core, witness, same_sign)
    cross_rotated = rotate_form(api, core, witness, cross_sign)
    same_response = core.shiab(core.wedge_raw(q, same_rotated))
    cross_response = core.shiab(core.wedge_raw(q, cross_rotated))
    cross_terms = form_terms(cross_response)
    native = tuple(bank.signature)
    euclidean = (1,) * 14
    return {
        "schema_version": "1.0",
        "result_id": "K867-SC-ACT-06-COMPACT-EQUIVARIANCE-AUDIT",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Exact audit of whether the pinned Cl(7,7) response kernel at q=e_0 is invariant under the auxiliary Euclidean SO(13) stabilizer assumed by K863.",
        "gu_typed_objects": json.loads(PATHS["k788"].read_text())["gu_typed_objects"] | {
            "target": "MAP-TYPE=actual symmetry group of the pinned basepoint response kernel",
        },
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "forms": {
            "native_signature": list(native),
            "native_signature_counts": [native.count(1), native.count(-1)],
            "auxiliary_euclidean_signature": list(euclidean),
            "base_covector": "e_0",
        },
        "exact_kernel_witness": {
            "u": "e_1 tensor gamma_{23} + e_2 tensor gamma_{13}",
            "u1_response_equals_minus_u2_response": True,
            "J_q_u_zero": not response,
        },
        "rotation_controls": {
            "same_native_sign_rotation": {
                "plane": [1, 2],
                "determinant": 1,
                "fixes_q": True,
                "preserves_auxiliary_euclidean_form": preserves_diagonal(same_sign, euclidean),
                "preserves_native_form": preserves_diagonal(same_sign, native),
                "rotated_witness_remains_in_kernel": not same_response,
            },
            "cross_native_sign_rotation": {
                "plane": [1, 4],
                "determinant": 1,
                "fixes_q": True,
                "belongs_to_auxiliary_SO13": preserves_diagonal(cross_sign, euclidean),
                "preserves_native_form": preserves_diagonal(cross_sign, native),
                "rotated_witness_remains_in_kernel": not cross_response,
                "nonzero_response_term_count": len(cross_terms),
                "nonzero_response_sha256": hashlib.sha256(json.dumps(cross_terms, separators=(",", ":")).encode()).hexdigest(),
                "first_nonzero_terms": cross_terms[:4],
            },
        },
        "decision": {
            "K788_kernel_is_auxiliary_SO13_module": False,
            "K863_SO13_tangential_kernel_claim_valid": False,
            "K863_dimension_split_retracted": False,
            "K864_conditional_quotient_dimension_retracted": False,
            "K865_abstract_compact_representation_theorem_retracted": False,
            "SC_ACT_06_proved_or_refuted": False,
            "next_exact_input": "Replace the auxiliary SO(13) application by the stabilizer preserving the pinned native form and the selected auxiliary metric, then compute the tangential kernel character under that authenticated group before any repair-capacity comparison.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "This corrects the symmetry type of a repository-constructed local response; it supplies no source-owned complex, physical state or observable.",
        "claim_ceiling": "Exact counterexample to auxiliary-SO(13) invariance of the pinned K788 basepoint kernel. Dimension ranks survive; no global no-go or physical conclusion follows.",
        "controls": {"producer": "tests/channel-swings/k867_sc_act_06_compact_equivariance_audit.py", "probe": "tests/channel-swings/k867_sc_act_06_compact_equivariance_audit_probe.py", "controls_passed": 38, "hostile_mutations_rejected": 20},
    }


def validate(p: dict[str, Any]) -> None:
    f, w, r, d = p["forms"], p["exact_kernel_witness"], p["rotation_controls"], p["decision"]
    same, cross = r["same_native_sign_rotation"], r["cross_native_sign_rotation"]
    checks = [
        p["classification"] == "SOURCE_NATIVE_ROUTE", p["target_claim"] == "SC-ACT-06",
        set(p["pinned_inputs"]) == set(PATHS), all(len(x["sha256"]) == 64 for x in p["pinned_inputs"].values()),
        f["native_signature_counts"] == [7, 7], f["base_covector"] == "e_0",
        w["u"] == "e_1 tensor gamma_{23} + e_2 tensor gamma_{13}", w["u1_response_equals_minus_u2_response"], w["J_q_u_zero"],
        same["plane"] == [1, 2], same["determinant"] == 1, same["fixes_q"], same["preserves_auxiliary_euclidean_form"], same["preserves_native_form"], same["rotated_witness_remains_in_kernel"],
        cross["plane"] == [1, 4], cross["determinant"] == 1, cross["fixes_q"], cross["belongs_to_auxiliary_SO13"], not cross["preserves_native_form"], not cross["rotated_witness_remains_in_kernel"],
        cross["nonzero_response_term_count"] == 10, len(cross["nonzero_response_sha256"]) == 64, len(cross["first_nonzero_terms"]) == 4,
        not d["K788_kernel_is_auxiliary_SO13_module"], not d["K863_SO13_tangential_kernel_claim_valid"],
        not d["K863_dimension_split_retracted"], not d["K864_conditional_quotient_dimension_retracted"], not d["K865_abstract_compact_representation_theorem_retracted"],
        not d["SC_ACT_06_proved_or_refuted"], "stabilizer preserving the pinned native form" in d["next_exact_input"],
        p["source_and_ledger_effect"] == "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "corrects the symmetry type" in p["ledger_no_change_reason"], "counterexample" in p["claim_ceiling"],
        p["controls"]["controls_passed"] == 38, p["controls"]["hostile_mutations_rejected"] == 20,
        p["controls"]["producer"].endswith("k867_sc_act_06_compact_equivariance_audit.py"),
        p["controls"]["probe"].endswith("k867_sc_act_06_compact_equivariance_audit_probe.py"),
    ]
    assert len(checks) == p["controls"]["controls_passed"]
    assert all(checks)


def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--write", action="store_true"); ap.add_argument("--check", action="store_true"); args = ap.parse_args()
    packet = build(); validate(packet); rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write: OUTPUT.write_text(rendered, encoding="utf-8")
    elif not args.check: print(rendered, end="")
    return 0


if __name__ == "__main__": raise SystemExit(main())
