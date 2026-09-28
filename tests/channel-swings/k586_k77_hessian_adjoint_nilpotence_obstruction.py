#!/usr/bin/env python3
"""K586: test the canonical-adjoint completion of the selected action block."""

from __future__ import annotations

import argparse
import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
K585_PATH = Path(__file__).with_name("k585_k77_action_boundary_coupling_typing.py")
OUTPUT = ROOT / "lab/process/k586-k77-hessian-adjoint-nilpotence-obstruction.json"


def strict(relative: str) -> dict[str, Any]:
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def load_k585():
    spec = importlib.util.spec_from_file_location("k585_for_k586", K585_PATH)
    module = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


def matrix_digest(matrix) -> str:
    entries = [[int(i), int(j), str(v)] for (i, j), v in sorted(matrix.todok().items())]
    return "sha256:" + hashlib.sha256(json.dumps(entries, separators=(",", ":")).encode()).hexdigest()


def build() -> dict[str, Any]:
    typed = strict("lab/process/k585-k77-action-boundary-coupling-typing.json")
    k585 = load_k585()
    block, _ = k585.reconstruct()
    gram = block.T * block
    scalar = gram[0, 0]
    is_scalar_identity = gram == scalar * sp.eye(block.cols)
    payload = {
        "schema_version": "1.0",
        "result_id": "K586-K77-HESSIAN-ADJOINT-NILPOTENCE-OBSTRUCTION",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "gu_comparator_routing": "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.",
        "scope": "Exact nilpotence test for the simplest metric-adjoint two-arrow completion of K585's selected first-action 1470-by-91 Hessian cross. The test is confined to the repository's current Euclidean coordinate pairing and does not claim that a source-selected BV pairing must be this adjoint.",
        "gu_typed_objects": {
            "block": "B: Q^91 epsilon variations -> R^1470 connection-Euler receivers",
            "candidate_adjacent_arrow": "B^T: R^1470 -> Q^91 under the current exact coordinate pairing",
            "tested_composition": "B^T B: Q^91 -> Q^91",
            "MAP-TYPE": "canonical-adjoint completion obstruction",
            "LAYER": "selected first-action Hessian tangent data",
            "CHIRALITY": "N/A",
        },
        "source_and_ledger_context": {
            "source_claims": ["SC-ACT-01", "SC-ACT-02", "SC-ACT-06", "SC-META-53"],
            "source_polarity_effect": "none",
            "physics_rows": ["LT-SM8", "LT-GR6b", "RA-F1", "AC-F1"],
            "ledger": "lab/process/conditional-physics-ledger-v0.263.json",
            "ledger_effect": "none",
            "typed_input": "lab/process/k585-k77-action-boundary-coupling-typing.json",
        },
        "preflight_bookend": {
            "route_comparison": "Test the only coefficient-preserving adjacent map supplied without new action data: the exact transpose under the current pairing.",
            "retrieval_collision_result": "No prior artifact tested B^T B for the selected first-action matrix.",
            "strongest_alternative": "Inventing an unrelated rank-70 projection could force a complex but would not be action-derived.",
        },
        "exact_adjoint_test": {
            "block_shape": [block.rows, block.cols],
            "block_rank": int(block.rank()),
            "gram_shape": [gram.rows, gram.cols],
            "gram_rank": int(gram.rank()),
            "gram_nonzero_entries": len(gram.todok()),
            "gram_is_zero": gram.is_zero_matrix,
            "gram_is_scalar_identity": is_scalar_identity,
            "gram_scalar": str(scalar),
            "gram_trace": str(sp.trace(gram)),
            "gram_sparse_content_digest": matrix_digest(gram),
            "positive_definite_over_reals": bool(gram.is_positive_definite),
            "reverse_composition_shape": [block.rows, block.rows],
            "reverse_composition_rank": int(block.rank()),
            "nilpotence_required_for_two_arrow_complex": True,
            "nilpotence_holds": bool(gram.is_zero_matrix),
        },
        "decision": {
            "canonical_adjoint_completion_rejected": True,
            "reason": "B^T B equals (50/257049) times the 91-dimensional identity and therefore has rank 91 rather than zero.",
            "source_action_rejected": False,
            "all_bv_kt_completions_rejected": False,
            "next_exact_input": "An independently action-owned reduction and adjacent arrow whose composition vanishes; neither arrow may be inferred solely from the Euclidean transpose of B.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Promoting failure of the Euclidean-adjoint completion to failure of every BV/KT completion.",
            "strongest_contrary_construction": "A nontrivial quotient or action-owned reduction L can change the target and kernel before an adjacent arrow is selected.",
            "weakest_reproducibility_seam": "The coordinate pairing is inherited from the selected-action probe; a different source-authenticated pairing would require a new test.",
        },
        "controls": {
            "producer": "tests/channel-swings/k586_k77_hessian_adjoint_nilpotence_obstruction.py",
            "probe": "tests/channel-swings/k586_k77_hessian_adjoint_nilpotence_obstruction_probe.py",
        },
        "claim_ceiling": "The exact Euclidean-transpose completion B followed by B^T is not nilpotent: B^T B is a positive scalar identity. This rejects that specified completion only. It does not reject the selected source action, an action-owned quotient/reduction, a different pairing, or every possible BV/KT complex; it does not move source, ledger, canon, paper, public posture, novelty, prediction, confirmation or a physical GU verdict.",
    }
    validate(payload, typed)
    return payload


def validate(payload: dict[str, Any], typed: dict[str, Any] | None = None) -> None:
    test = payload["exact_adjoint_test"]
    decision = payload["decision"]
    if typed is not None and typed["actual_action_block"]["shape"] != test["block_shape"]:
        raise AssertionError("K585/K586 block mismatch")
    if test["block_shape"] != [1470, 91] or test["block_rank"] != 91:
        raise AssertionError("selected action block changed")
    if test["gram_shape"] != [91, 91] or test["gram_rank"] != 91 or test["gram_nonzero_entries"] != 91:
        raise AssertionError("adjoint composition fingerprint changed")
    if not test["gram_is_scalar_identity"] or test["gram_scalar"] != "50/257049":
        raise AssertionError("exact Gram identity changed")
    if test["gram_is_zero"] or test["nilpotence_holds"] or not test["positive_definite_over_reals"]:
        raise AssertionError("nilpotence disposition changed")
    if not decision["canonical_adjoint_completion_rejected"] or decision["source_action_rejected"] or decision["all_bv_kt_completions_rejected"]:
        raise AssertionError("K586 claim boundary changed")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
