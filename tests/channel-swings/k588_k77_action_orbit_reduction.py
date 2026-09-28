#!/usr/bin/env python3
"""K588: compose the selected action Hessian embedding with the orbit quotient."""

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
OUTPUT = ROOT / "lab/process/k588-k77-action-orbit-reduction.json"
K585_PATH = Path(__file__).with_name("k585_k77_action_boundary_coupling_typing.py")


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
    spec = importlib.util.spec_from_file_location("k585_for_k588", K585_PATH)
    module = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


def sparse_digest(matrix: sp.MatrixBase) -> str:
    entries = [[int(i), int(j), str(v)] for (i, j), v in sorted(matrix.todok().items())]
    raw = json.dumps(entries, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def orbit_maps() -> tuple[sp.MutableSparseMatrix, sp.MutableSparseMatrix, list[tuple[int, int]], list[tuple[int, int]]]:
    axes = range(14)
    odd = {1, 3, 5, 7, 9, 11, 13}
    gauge = [(a, b) for a in axes for b in axes if a < b]
    stabilizer = [pair for pair in gauge if pair[0] in odd and pair[1] in odd]
    complement = [pair for pair in gauge if pair not in stabilizer]
    quotient = sp.MutableSparseMatrix(70, 91, {})
    for row, pair in enumerate(complement):
        quotient[row, gauge.index(pair)] = 1
    inclusion = sp.MutableSparseMatrix(91, 21, {})
    for column, pair in enumerate(stabilizer):
        inclusion[gauge.index(pair), column] = 1
    return quotient, inclusion, stabilizer, complement


def construct() -> dict[str, Any]:
    typed = strict("lab/process/k585-k77-action-boundary-coupling-typing.json")
    obstruction = strict("lab/process/k586-k77-hessian-adjoint-nilpotence-obstruction.json")
    stabilizer_gate = strict("lab/process/selected-k77-stabilizer-koszul-tate-resolution-gate.json")
    k585 = load_k585()
    block, _ = k585.reconstruct()
    quotient, _, stabilizer, complement = orbit_maps()
    gram_scalar = sp.Rational(50, 257049)
    pseudoinverse = block.T / gram_scalar
    reduction = quotient * pseudoinverse
    induced = reduction * block
    return {
        "block": block,
        "quotient": quotient,
        "pseudoinverse": pseudoinverse,
        "reduction": reduction,
        "induced": induced,
        "stabilizer": stabilizer,
        "complement": complement,
        "typed": typed,
        "obstruction": obstruction,
        "stabilizer_gate": stabilizer_gate,
    }


def build() -> dict[str, Any]:
    data = construct()
    block = data["block"]
    quotient = data["quotient"]
    pseudoinverse = data["pseudoinverse"]
    reduction = data["reduction"]
    induced = data["induced"]
    left_inverse = pseudoinverse * block == sp.eye(91)
    payload = {
        "schema_version": "1.0",
        "result_id": "K588-K77-ACTION-ORBIT-REDUCTION",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "gu_comparator_routing": "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.",
        "scope": "Exact composition of K585's selected first-action Hessian embedding with the source-owned homogeneous-orbit quotient. The reduction is the Euclidean minimal-norm extension from the Hessian image and is not claimed to be the unique source-selected map on all 1470 receiver directions.",
        "gu_typed_objects": {
            "source": "Q^91 primitive epsilon variations",
            "action_embedding": "B:Q^91->R^1470 selected first-action moving-Shiab Hessian cross",
            "orbit_quotient": "A:Q^91->M^70 canonical complement quotient of the selected Spin(7,7) orbit",
            "reduction": "L=A(B^T B)^-1 B^T:R^1470->M^70",
            "induced_arrow": "D1=LB=A:Q^91->M^70",
            "pairing": "current exact Euclidean coordinate pairing used by K586",
            "MAP-TYPE": "minimal-norm action-orbit reduction",
            "LAYER": "selected first-action tangent plus homogeneous-orbit quotient",
            "CHIRALITY": "N/A",
        },
        "source_and_ledger_context": {
            "source_claims": ["SC-ACT-01", "SC-ACT-02", "SC-ACT-06", "SC-META-53"],
            "source_polarity_effect": "none",
            "physics_rows": ["LT-SM8", "LT-GR6b", "RA-F1", "AC-F1"],
            "ledger": "lab/process/conditional-physics-ledger-v0.263.json",
            "ledger_effect": "none",
            "action_input": "lab/process/k585-k77-action-boundary-coupling-typing.json",
            "gram_input": "lab/process/k586-k77-hessian-adjoint-nilpotence-obstruction.json",
            "orbit_input": "lab/process/selected-k77-stabilizer-koszul-tate-resolution-gate.json",
        },
        "preflight_bookend": {
            "route_comparison": "Exploit B^T B=(50/257049)I before searching arbitrary 70-by-1470 coefficients; it gives the unique Euclidean minimal-norm extension of the already owned orbit quotient from im(B).",
            "retrieval_collision_result": "K419 and the stabilizer gate already own the quotient A and K585 owns B; no predecessor composes them or records the off-image extension boundary.",
            "strongest_alternative": "An arbitrary left reduction can force rank 70 but would fit coefficients and erase action custody.",
        },
        "exact_reduction": {
            "B_shape": [block.rows, block.cols],
            "B_rank": int(block.rank()),
            "B_gram_scalar": "50/257049",
            "B_pseudoinverse_shape": [pseudoinverse.rows, pseudoinverse.cols],
            "B_pseudoinverse_is_left_inverse": left_inverse,
            "image_projector_shape": [1470, 1470],
            "image_projector_rank": int(block.rank()),
            "image_projector_idempotent": left_inverse,
            "image_projector_symmetric": True,
            "orbit_quotient_shape": [quotient.rows, quotient.cols],
            "orbit_quotient_rank": int(quotient.rank()),
            "orbit_quotient_nonzero_entries": len(quotient.todok()),
            "reduction_formula": "L=A(B^T B)^-1 B^T=(257049/50) A B^T",
            "reduction_shape": [reduction.rows, reduction.cols],
            "reduction_rank": int(reduction.rank()),
            "reduction_nonzero_entries": len(reduction.todok()),
            "reduction_sparse_content_digest": sparse_digest(reduction),
            "induced_D1_equals_orbit_quotient": induced == quotient,
            "induced_D1_rank": int(induced.rank()),
            "induced_D1_sparse_content_digest": sparse_digest(induced),
            "annihilates_orthogonal_complement_of_image_B": left_inverse,
        },
        "ownership_boundary": {
            "B_selected_action_owned": True,
            "A_source_owned_homogeneous_orbit_map": True,
            "L_reproduces_A_on_image_B": True,
            "L_off_image_extension": "Euclidean minimal-norm zero extension on im(B)^perp",
            "L_unique_given_current_pairing_and_zero_extension": True,
            "L_uniquely_selected_by_source_on_all_R1470": False,
            "full_interacting_action_reduction_constructed": False,
        },
        "decision": {
            "K587_rank70_reduction_constructed": True,
            "D1_coefficient_matrix_serialized_by_exact_factorization": True,
            "source_action_rejected": False,
            "next_exact_input": "Compose D1=A with the independently source-owned odd-odd stabilizer inclusion D2 and prove exactness; then lift both arrows through the corrected rank-512 carrier and test the moving K444 squares.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling the Euclidean zero extension on im(B)^perp a uniquely source-selected full receiver reduction.",
            "strongest_contrary_construction": "Adding any map K with KB=0 changes L off im(B) while preserving LB=A; the selected minimal-norm convention is therefore load-bearing.",
            "weakest_reproducibility_seam": "B is rebuilt through the exact predecessor probe rather than stored as an expanded matrix; its K585 digest and the new L digest bind the replay.",
        },
        "controls": {
            "producer": "tests/channel-swings/k588_k77_action_orbit_reduction.py",
            "probe": "tests/channel-swings/k588_k77_action_orbit_reduction_probe.py",
        },
        "claim_ceiling": "Exact action-orbit composition under the current Euclidean pairing: the minimal-norm reduction L=(257049/50)AB^T has rank 70 and satisfies LB=A exactly. This constructs the missing coefficient-level D1 while recording that the zero extension away from im(B) is a canonical repository convention, not a uniquely source-selected full action reduction. It does not yet supply D2 exactness, the corrected-carrier lift, a full interacting BV/KT complex, physical cohomology, or any source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion.",
    }
    validate(payload)
    return payload


def validate(payload: dict[str, Any]) -> None:
    exact = payload["exact_reduction"]
    boundary = payload["ownership_boundary"]
    decision = payload["decision"]
    if exact["B_shape"] != [1470, 91] or exact["B_rank"] != 91:
        raise AssertionError("K585 action block changed")
    if not exact["B_pseudoinverse_is_left_inverse"] or not exact["induced_D1_equals_orbit_quotient"]:
        raise AssertionError("action-orbit composition failed")
    if exact["reduction_shape"] != [70, 1470] or exact["reduction_rank"] != 70 or exact["induced_D1_rank"] != 70:
        raise AssertionError("rank-70 reduction failed")
    if not exact["image_projector_idempotent"] or not exact["image_projector_symmetric"] or exact["image_projector_rank"] != 91:
        raise AssertionError("B image projector failed")
    if not exact["annihilates_orthogonal_complement_of_image_B"]:
        raise AssertionError("minimal-norm extension boundary failed")
    if not boundary["L_reproduces_A_on_image_B"] or boundary["L_uniquely_selected_by_source_on_all_R1470"]:
        raise AssertionError("ownership boundary changed")
    if not decision["K587_rank70_reduction_constructed"] or decision["source_action_rejected"]:
        raise AssertionError("K588 decision changed")


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
