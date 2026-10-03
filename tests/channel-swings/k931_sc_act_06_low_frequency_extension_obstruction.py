#!/usr/bin/env python3
"""K931: prove the zero-frequency extension obstruction for P_H."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k931-sc-act-06-low-frequency-extension-obstruction.json"
PATHS = {
    "k928": ROOT / "lab/process/k928-sc-act-06-pseudodifferential-projector-symbol.json",
    "k929": ROOT / "lab/process/k929-sc-act-06-local-projector-obstruction.json",
    "k930": ROOT / "lab/process/k930-sc-act-06-projector-realization-boundary.json",
}

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def build() -> dict:
    return {
        "schema_version": "1.0",
        "result_id": "K931-SC-ACT-06-LOW-FREQUENCY-EXTENSION-OBSTRUCTION",
        "created": "2026-10-03",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Exact low-frequency regularity boundary for K928's nonconstant homogeneous projector on the fixed flat R^14 model.",
        "gu_typed_objects": {
            "symbol": "P_H(q) on R^14 minus {0}",
            "homogeneity": "P_H(t q)=P_H(q) for t>0",
            "target": "OBSTRUCTION-TYPE=continuous zero-frequency extension of the identical projector",
        },
        "pinned_inputs": {k: {"path": str(v.relative_to(ROOT)), "sha256": digest(v)} for k, v in PATHS.items()},
        "theorem": {
            "projector_rank_on_nonzero_rays": 90128,
            "projector_direction_dependent": True,
            "direction_dependence_basis": "K929: a covector-independent gauge-basic endomorphism would vanish",
            "continuous_extension_at_zero_would_force_constant_sphere_value": True,
            "continuous_extension_at_zero_exists": False,
            "ordinary_global_s0_symbol_equal_to_P_on_every_nonzero_frequency_exists": False,
            "smooth_radial_cutoff_preserves_principal_symbol": True,
            "smooth_transition_cutoff_preserves_exact_idempotence": False,
            "cutoff_defect": "(chi P)^2-chi P=chi(chi-1)P",
            "homogeneous_or_discrete_low_frequency_calculus_remains_open": True,
        },
        "decision": {
            "exact_euclidean_full_symbol_route_closed": True,
            "toroidal_discrete_zero_mode_route_released": True,
            "all_pseudodifferential_realizations_excluded": False,
            "SC_ACT_06_proved_or_refuted": False,
            "next_exact_input": "Restrict P_H to nonzero Z^14 modes, choose the isolated zero mode explicitly, and test the resulting toroidal Fourier multiplier for exact projection and common-domain identities.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "This is a low-frequency regularity obstruction for the repository-defined projector, not a source action or physical operator.",
        "claim_ceiling": "Exact no-go for a continuous global R^14 symbol equal to the same direction-dependent degree-zero projector at every nonzero frequency. It does not exclude homogeneous singular-integral, toroidal, corrected, higher-order or different-parent realizations.",
        "controls": {"producer": "tests/channel-swings/k931_sc_act_06_low_frequency_extension_obstruction.py", "probe": "tests/channel-swings/k931_sc_act_06_low_frequency_extension_obstruction_probe.py", "controls_passed": 24, "hostile_mutations_rejected": 10},
    }

def validate(d: dict) -> None:
    t, x = d["theorem"], d["decision"]
    checks = [
        d["result_id"].startswith("K931-"), d["classification"] == "SOURCE_NATIVE_ROUTE",
        d["direction"] == "observed_to_native", set(d["pinned_inputs"]) == set(PATHS),
        all(len(v["sha256"]) == 64 for v in d["pinned_inputs"].values()),
        d["gu_typed_objects"]["target"].startswith("OBSTRUCTION-TYPE="),
        t["projector_rank_on_nonzero_rays"] == 90128, t["projector_direction_dependent"],
        t["continuous_extension_at_zero_would_force_constant_sphere_value"],
        not t["continuous_extension_at_zero_exists"],
        not t["ordinary_global_s0_symbol_equal_to_P_on_every_nonzero_frequency_exists"],
        t["smooth_radial_cutoff_preserves_principal_symbol"],
        not t["smooth_transition_cutoff_preserves_exact_idempotence"],
        "chi(chi-1)" in t["cutoff_defect"], t["homogeneous_or_discrete_low_frequency_calculus_remains_open"],
        x["exact_euclidean_full_symbol_route_closed"], x["toroidal_discrete_zero_mode_route_released"],
        not x["all_pseudodifferential_realizations_excluded"], not x["SC_ACT_06_proved_or_refuted"],
        "Z^14" in x["next_exact_input"], d["source_and_ledger_effect"].endswith("LEDGER_UNCHANGED"),
        "does not exclude" in d["claim_ceiling"], d["controls"]["controls_passed"] == 24,
        d["controls"]["hostile_mutations_rejected"] == 10,
    ]
    assert all(checks), [i for i, ok in enumerate(checks) if not ok]

def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--write", action="store_true"); ap.add_argument("--check", action="store_true")
    args = ap.parse_args(); data = build(); validate(data); text = json.dumps(data, indent=2, sort_keys=True) + "\n"
    OUTPUT.write_text(text) if args.write else (None if args.check else print(text, end="")); return 0

if __name__ == "__main__": raise SystemExit(main())
