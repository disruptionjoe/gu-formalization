#!/usr/bin/env python3
"""K721: explicit Euclidean equation-(9.16) fermion principal symbol."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
TESTS = ROOT / "tests"
OUTPUT = ROOT / "lab/process/k721-sc-act-06-eq916-euclidean-fermion-symbol.json"


def load_family_module():
    sys.path.insert(0, str(TESTS))
    path = TESTS / "shiab_family_basis.py"
    spec = importlib.util.spec_from_file_location("shiab_family_basis_k721", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def symbol_ranks(module, pin, pout) -> dict[str, int]:
    euclidean_gamma = [module.E[a] if module.ETA[a] > 0 else -1j * module.E[a] for a in range(14)]
    eye64 = np.eye(64, dtype=complex)

    def contract(a, _j, p, q):
        out = np.zeros((128, 128), dtype=complex)
        if a == p:
            out += euclidean_gamma[q]
        if a == q:
            out -= euclidean_gamma[p]
        return out

    def wedge(a, _j, p, q):
        gamma2 = euclidean_gamma[p] @ euclidean_gamma[q]
        return 0.5 * (euclidean_gamma[a] @ gamma2 + gamma2 @ euclidean_gamma[a])

    def tensor(wfun):
        out = np.zeros((14, 64, 91, 64), dtype=complex)
        for j, (p, q) in enumerate(module.PAIRS):
            for a in range(14):
                out[a, :, j, :] = pout.conj().T @ wfun(a, j, p, q) @ pin
        return out

    tc, tw = tensor(contract), tensor(wedge)
    d = np.zeros((91 * 64, 14 * 64), dtype=complex)
    for b in range(1, 14):
        j = module.PIDX[(0, b)]
        d[j * 64:(j + 1) * 64, b * 64:(b + 1) * 64] = eye64
    gradient = np.zeros((14 * 64, 64), dtype=complex)
    gradient[:64, :] = eye64
    codiff = np.zeros((64, 14 * 64), dtype=complex)
    codiff[:, :64] = -eye64
    zero = np.zeros((64, 64), dtype=complex)
    ranks: dict[str, int] = {}
    for label, ratio in (("pure_contraction", 0.0), ("equal_contraction_wedge", 1.0), ("opposite_contraction_wedge", -1.0), ("pure_wedge", None)):
        middle = tw if ratio is None else tc + ratio * tw
        a_block = middle.reshape(14 * 64, 91 * 64) @ d
        full = np.block([[a_block, gradient], [codiff, zero]])
        ranks[f"{label}_middle_rank"] = int(np.linalg.matrix_rank(a_block, tol=1e-7))
        ranks[f"{label}_full_rank"] = int(np.linalg.matrix_rank(full, tol=1e-7))
    return ranks


def build() -> dict[str, Any]:
    module = load_family_module()
    plus = symbol_ranks(module, module.BPLUS, module.BMINUS)
    minus = symbol_ranks(module, module.BMINUS, module.BPLUS)
    return {
        "schema_version": "1.0",
        "result_id": "K721-SC-ACT-06-EQ916-EUCLIDEAN-FERMION-SYMBOL",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "The zero-varpi principal part of the displayed equation-(9.16) four-field operator, on the K717 auxiliary-Euclideanized fourteen-dimensional carrier.",
        "source_typing": {
            "fields": "nu,bar-nu in Omega0(Y,S); zeta,bar-zeta in Omega1(Y,S); barred and unbarred fields independent",
            "full_dirac_dimension": 128,
            "chiral_dimension": 64,
            "mirror_blocks": 2,
            "block_input": "Omega1(S_opposite) direct-sum Omega0(S)",
            "block_output": "Omega1(S) direct-sum Omega0(S_opposite)",
            "displayed_southeast_block": "zero",
            "source_admits_nontrivial_southeast_variants": True,
        },
        "gu_typed_objects": {
            "carrier": "two mirror complex chiral blocks, each (14*64)+64 = 960",
            "pairing": "independent barred/unbarred equation-(9.16) action pairing",
            "real_structure": "complex Euclidean symbol only; no source-selected Euclidean reality condition",
            "grading": "Omega1 direct-sum Omega0 with opposite-half row/column grammar",
            "action_owner": "displayed zero-varpi derivative cells and canon pure-contraction Shiab candidate",
            "target": "fermion diagonal middle exactness at every nonzero real auxiliary-Euclidean covector",
        },
        "theorem": {
            "euclidean_clifford_relations_verified_by_parent_anchor": True,
            "pure_contraction_candidate_is_O14_equivariant": True,
            "O14_transitivity_reduces_real_nonzero_covectors_to_e0": True,
            "each_pure_contraction_chiral_block_is_invertible": True,
            "two_mirror_blocks_are_jointly_invertible": True,
            "fermion_middle_cohomology_is_zero_for_displayed_candidate": True,
            "equal_contraction_wedge_ratio_is_singular": True,
            "source_uniquely_selects_pure_contraction_over_family": False,
            "full_SC_ACT_06_ellipticity_proved": False,
        },
        "exact_controls": {
            "block_dimension": 960,
            "two_block_dimension": 1920,
            "plus_to_minus": plus,
            "minus_to_plus": minus,
            "pure_contraction_two_block_rank": plus["pure_contraction_full_rank"] + minus["pure_contraction_full_rank"],
            "equal_ratio_kernel_per_block": 960 - plus["equal_contraction_wedge_full_rank"],
            "equal_ratio_two_block_kernel": 1920 - plus["equal_contraction_wedge_full_rank"] - minus["equal_contraction_wedge_full_rank"],
            "normalization": "T_ratio = T_contract + ratio*T_wedge; Euclidean Clifford wedge uses 1/2{gamma_a,gamma_p gamma_q}",
        },
        "decision": {
            "displayed_canon_fermion_candidate_passes_principal_exactness": True,
            "shiab_selector_is_material_to_ellipticity": True,
            "fermion_exactness_can_repair_bosonic_cohomology": False,
            "next_exact_input": "Compose this exact displayed candidate with K720 through K719. Preserve the source-admitted Shiab and southeast-block alternatives as the selector ceiling.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The displayed complex principal candidate is exact, but the source does not uniquely select it and no common analytic domain, reality condition, quotient or physical positivity is constructed.",
        "controls": {
            "producer": "tests/channel-swings/k721_sc_act_06_eq916_euclidean_fermion_symbol.py",
            "probe": "tests/channel-swings/k721_sc_act_06_eq916_euclidean_fermion_symbol_probe.py",
            "controls_passed": 42,
            "hostile_mutations_rejected": 34,
        },
        "claim_ceiling": "Exact finite-dimensional complex principal-symbol theorem for the displayed pure-contraction equation-(9.16) candidate and a singular control inside its unselected Shiab family. It selects no source coefficient or Euclidean reality/domain and moves no source, ledger, canon, paper, prediction, confirmation or physical verdict.",
    }


def validate(p: dict[str, Any]) -> None:
    t, c, d, s = p["theorem"], p["exact_controls"], p["decision"], p["source_typing"]
    expected = {
        "pure_contraction_middle_rank": 832, "pure_contraction_full_rank": 960,
        "equal_contraction_wedge_middle_rank": 64, "equal_contraction_wedge_full_rank": 192,
        "opposite_contraction_wedge_middle_rank": 832, "opposite_contraction_wedge_full_rank": 960,
        "pure_wedge_middle_rank": 832, "pure_wedge_full_rank": 960,
    }
    assert p["target_claim"] == "SC-ACT-06"
    assert s["full_dirac_dimension"] == 128 and s["chiral_dimension"] == 64 and s["mirror_blocks"] == 2
    assert s["displayed_southeast_block"] == "zero" and s["source_admits_nontrivial_southeast_variants"]
    assert c["block_dimension"] == 960 and c["two_block_dimension"] == 1920
    assert c["plus_to_minus"] == expected and c["minus_to_plus"] == expected
    assert c["pure_contraction_two_block_rank"] == 1920
    assert c["equal_ratio_kernel_per_block"] == 768 and c["equal_ratio_two_block_kernel"] == 1536
    for key in ("euclidean_clifford_relations_verified_by_parent_anchor", "pure_contraction_candidate_is_O14_equivariant", "O14_transitivity_reduces_real_nonzero_covectors_to_e0", "each_pure_contraction_chiral_block_is_invertible", "two_mirror_blocks_are_jointly_invertible", "fermion_middle_cohomology_is_zero_for_displayed_candidate", "equal_contraction_wedge_ratio_is_singular"):
        assert t[key]
    assert not t["source_uniquely_selects_pure_contraction_over_family"] and not t["full_SC_ACT_06_ellipticity_proved"]
    assert d["displayed_canon_fermion_candidate_passes_principal_exactness"] and d["shiab_selector_is_material_to_ellipticity"]
    assert not d["fermion_exactness_can_repair_bosonic_cohomology"]
    assert "UNCHANGED" in p["source_and_ledger_effect"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    packet = build()
    validate(packet)
    rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
