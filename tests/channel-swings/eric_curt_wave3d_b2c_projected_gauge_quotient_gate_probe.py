#!/usr/bin/env python3
r"""ECW3D-B2C1: collide the prior projected-gauge map with the W131 Jordan sector.

The prior source-Noether/tau attempt derived only the minimum-distance map

    G(k) = Pi_ker(Gamma) (k tensor -).

This probe asks whether that already-built map supplies the source- and
dynamics-compatible quotient required after B2B.  At each characteristic
root, only a rank-64 parameter half of the rank-128 map is annihilated by the
principal symbol.  The two root-dependent halves together identify the
rank-128 Jordan image, but the prior source does not select them as a tangent
BV differential.  The smallest fixed spatially invariant closure of all
coordinate Jordan images has rank 512 and equals the entire projected
observer-section vector-spinor carrier.  Quotienting it repairs the reduced
Clifford generators but makes the observer-section map fail to descend.

Thus the existing projected-gauge quotient candidate is killed.  This does
not kill a future independently source-derived tangent/BV differential,
changed action, pseudodifferential reduction, or nonlinear propagated
constraint.
"""

from __future__ import annotations

import json
from pathlib import Path
import sys

import numpy as np


HERE = Path(__file__).resolve().parent
TESTS = HERE.parent
ROOT = TESTS.parent
GENERATION = TESTS / "generation-sector"
for path in (str(TESTS), str(GENERATION)):
    if path not in sys.path:
        sys.path.insert(0, path)

import gen_sector_bridge as gb  # noqa: E402


TOL = 3.0e-7
RANK_TOL = 1.0e-7
FAILURES: list[str] = []
EXACT = 0
PLANTED = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global EXACT
    EXACT += 1
    status = "PASS" if condition else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(label)


def reject(label: str, false_claim: bool) -> None:
    global PLANTED
    PLANTED += 1
    status = "PASS" if not false_claim else "FAIL"
    print(f"{status}: planted rejection — {label}", flush=True)
    if false_claim:
        FAILURES.append(f"planted: {label}")


def max_abs(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(matrix)))


def matrix_product(matrices: list[np.ndarray]) -> np.ndarray:
    out = np.eye(matrices[0].shape[0], dtype=complex)
    for matrix in matrices:
        out = out @ matrix
    return out


def singular_data(matrix: np.ndarray) -> tuple[int, float, float]:
    singular = np.linalg.svd(matrix, compute_uv=False)
    rank = int(np.sum(singular > RANK_TOL))
    smallest_nonzero = float(singular[rank - 1]) if rank else 0.0
    largest_zero = float(singular[rank]) if rank < len(singular) else 0.0
    return rank, smallest_nonzero, largest_zero


def image_basis(matrix: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    left, singular, _ = np.linalg.svd(matrix, full_matrices=False)
    rank = int(np.sum(singular > RANK_TOL))
    return left[:, :rank], singular


def residual_outside(subspace: np.ndarray, vectors: np.ndarray) -> float:
    return float(np.linalg.norm(vectors - subspace @ (subspace.conj().T @ vectors)))


def unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    out: dict[str, object] = {}
    for key, value in pairs:
        if key in out:
            raise ValueError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


def main() -> int:
    print("=" * 96)
    print("ECW3D-B2C1 PRIOR SOURCE/DATUM PROJECTED-GAUGE QUOTIENT COLLISION")
    print("=" * 96)

    gammas, gamma_trace, projector, _ = gb.constraint_objects()
    identity_v = np.eye(14, dtype=complex)
    identity_s = np.eye(128, dtype=complex)
    section = {"y": 0, "x": 1, "z": 2, "t": 9}

    values, vectors = np.linalg.eigh(projector)
    kernel = vectors[:, values > 0.5]
    identity = np.eye(kernel.shape[1], dtype=complex)
    check(
        "the actual W131 carrier is the rank-1664 gamma-traceless projector",
        kernel.shape == (1792, 1664)
        and np.linalg.norm(gamma_trace @ kernel) < TOL
        and max_abs(kernel.conj().T @ kernel - identity) < 3.0e-8,
    )

    symbols = {
        name: kernel.conj().T
        @ np.kron(identity_v, gammas[index])
        @ kernel
        for name, index in section.items()
    }
    inverse_time = np.linalg.inv(symbols["t"])
    evolution = {
        name: inverse_time @ symbols[name] for name in ("y", "x", "z")
    }

    j_s = matrix_product([gammas[i] for i in (1, 3, 5, 7, 10, 12)])
    j_vs = np.kron(identity_v, j_s)
    right_h = kernel.conj().T @ j_vs @ kernel.conj()
    check(
        "right-H remains quaternionic on the W131 carrier",
        max_abs(right_h @ right_h.conj() + identity) < 4.0e-8,
    )

    directions = {
        "y": (np.array([1.0, 0.0, 0.0]), 1.0),
        "x": (np.array([0.0, 1.0, 0.0]), 1.0),
        "z": (np.array([0.0, 0.0, 1.0]), 1.0),
        "generic_1_2_3": (np.array([1.0, 2.0, 3.0]), 14.0),
    }
    direction_results: dict[str, dict[str, object]] = {}
    jordan_images: dict[str, np.ndarray] = {}

    for label, (coefficients, norm_sq) in directions.items():
        c_xi = sum(
            coefficients[index] * evolution[name]
            for index, name in enumerate(("y", "x", "z"))
        )
        a_xi = sum(
            coefficients[index] * symbols[name]
            for index, name in enumerate(("y", "x", "z"))
        )
        nilpotent = c_xi @ c_xi - norm_sq * identity
        q_n, singular_n = image_basis(nilpotent)
        jordan_images[label] = q_n
        check(
            f"{label} reproduces the nonzero rank-128 square-zero Jordan image",
            q_n.shape[1] == 128
            and singular_n[127] > 0.6 * norm_sq
            and max_abs(nilpotent @ nilpotent) < 3.0e-11 * max(1.0, norm_sq**2),
            f"rank={q_n.shape[1]}, sv+={singular_n[127]:.12g}",
        )

        root_modes: list[np.ndarray] = []
        root_rows: dict[str, object] = {}
        for root_sign in (-1, 1):
            mu = root_sign * np.sqrt(norm_sq)
            covector = np.zeros(14)
            for index, name in enumerate(("y", "x", "z")):
                covector[section[name]] = coefficients[index]
            covector[section["t"]] = -mu
            raw_gauge = np.kron(covector.reshape(14, 1), identity_s)
            gauge = kernel.conj().T @ projector @ raw_gauge
            q_gauge, _ = image_basis(gauge)
            characteristic = a_xi - mu * symbols["t"]
            defect = characteristic @ gauge
            _, singular_d, right_d = np.linalg.svd(defect, full_matrices=False)
            defect_rank = int(np.sum(singular_d > RANK_TOL))
            parameter_null = right_d.conj().T[:, defect_rank:]
            modes, _ = image_basis(gauge @ parameter_null)
            root_modes.append(modes)

            intersection_rank = (
                q_gauge.shape[1]
                + q_n.shape[1]
                - image_basis(np.hstack([q_gauge, q_n]))[0].shape[1]
            )
            invariance_residual = residual_outside(q_gauge, c_xi @ q_gauge)
            characteristic_residual = float(np.linalg.norm(characteristic @ modes))
            root_rows[str(root_sign)] = {
                "gauge_rank": q_gauge.shape[1],
                "characteristic_defect_rank": defect_rank,
                "characteristic_null_half_rank": modes.shape[1],
                "jordan_intersection_rank": intersection_rank,
                "characteristic_null_residual": characteristic_residual,
                "full_gauge_invariance_residual": invariance_residual,
            }
            check(
                f"{label} root {root_sign:+d} projected source map has rank 128 but characteristic defect rank 64",
                q_gauge.shape[1] == 128
                and defect_rank == 64
                and singular_d[63] > 1.0e-2
                and singular_d[64] < 2.0e-10,
                f"ranks=({q_gauge.shape[1]},{defect_rank})",
            )
            check(
                f"{label} root {root_sign:+d} has exactly one rank-64 on-characteristic residual half",
                modes.shape[1] == 64
                and characteristic_residual < 2.0e-10
                and intersection_rank == 64,
                f"residual={characteristic_residual:.12g}, intersection={intersection_rank}",
            )
            check(
                f"{label} root {root_sign:+d} full projected source map is not an invariant characteristic gauge image",
                np.linalg.norm(defect) > 1.0
                and invariance_residual > 1.0,
                f"symbol norm={np.linalg.norm(defect):.12g}, invariance={invariance_residual:.12g}",
            )

        combined_modes, _ = image_basis(np.hstack(root_modes))
        jordan_residual = residual_outside(combined_modes, q_n)
        reverse_residual = residual_outside(q_n, combined_modes)
        check(
            f"{label} two root-dependent residual halves together equal the Jordan image",
            combined_modes.shape[1] == 128
            and jordan_residual < 2.0e-9
            and reverse_residual < 2.0e-9,
            f"rank={combined_modes.shape[1]}, residuals=({jordan_residual:.12g},{reverse_residual:.12g})",
        )
        direction_results[label] = {
            "jordan_rank": q_n.shape[1],
            "root_collision": root_rows,
            "combined_residual_half_rank": combined_modes.shape[1],
            "combined_to_jordan_residual": jordan_residual,
            "jordan_to_combined_residual": reverse_residual,
        }

    coordinate_span, _ = image_basis(
        np.hstack([jordan_images[name] for name in ("y", "x", "z")])
    )
    check(
        "the three coordinate Jordan images span rank 384",
        coordinate_span.shape[1] == 384,
        f"rank={coordinate_span.shape[1]}",
    )
    generic_residual = residual_outside(
        coordinate_span, jordan_images["generic_1_2_3"]
    )
    check(
        "the tested generic Jordan image lies in the coordinate rank-384 span",
        generic_residual < 2.0e-9,
        f"residual={generic_residual:.12g}",
    )

    one_step, _ = image_basis(
        np.hstack(
            [coordinate_span]
            + [evolution[name] @ coordinate_span for name in ("y", "x", "z")]
        )
    )
    closure_residual = max(
        residual_outside(one_step, evolution[name] @ one_step)
        for name in ("y", "x", "z")
    )
    check(
        "the smallest tested common invariant closure has rank 512 and closes in one step",
        one_step.shape[1] == 512 and closure_residual < 2.0e-9,
        f"rank={one_step.shape[1]}, residual={closure_residual:.12g}",
    )

    section_maps: list[np.ndarray] = []
    selector = np.zeros((4 * 128, 14 * 128), dtype=complex)
    for block, name in enumerate(("y", "x", "z", "t")):
        covector = np.zeros(14)
        covector[section[name]] = 1.0
        raw = np.kron(covector.reshape(14, 1), identity_s)
        section_maps.append(kernel.conj().T @ projector @ raw)
        selector[block * 128 : (block + 1) * 128, section[name] * 128 : (section[name] + 1) * 128] = identity_s
    section_carrier, _ = image_basis(np.hstack(section_maps))
    closure_to_section = residual_outside(section_carrier, one_step)
    section_to_closure = residual_outside(one_step, section_carrier)
    check(
        "the rank-512 invariant closure equals the full projected observer-section carrier",
        section_carrier.shape[1] == 512
        and closure_to_section < 2.0e-9
        and section_to_closure < 2.0e-9,
        f"residuals=({closure_to_section:.12g},{section_to_closure:.12g})",
    )

    right_h_residual = residual_outside(
        section_carrier, right_h @ section_carrier.conj()
    )
    check(
        "the fixed rank-512 closure is right-H invariant",
        right_h_residual < 2.0e-9,
        f"residual={right_h_residual:.12g}",
    )

    full_q, _ = np.linalg.qr(section_carrier, mode="complete")
    quotient = full_q[:, 512:]
    reduced = {
        name: quotient.conj().T @ evolution[name] @ quotient
        for name in ("y", "x", "z")
    }
    reduced_identity = np.eye(quotient.shape[1], dtype=complex)
    hermitian_defect = max(max_abs(matrix - matrix.conj().T) for matrix in reduced.values())
    square_defect = max(max_abs(matrix @ matrix - reduced_identity) for matrix in reduced.values())
    anticommutator_defect = max(
        max_abs(reduced[left] @ reduced[right] + reduced[right] @ reduced[left])
        for left, right in (("y", "x"), ("y", "z"), ("x", "z"))
    )
    check(
        "the degenerate fixed quotient repairs the generators to Hermitian Clifford involutions",
        quotient.shape[1] == 1152
        and hermitian_defect < 2.0e-8
        and square_defect < 2.0e-8
        and anticommutator_defect < 2.0e-8,
        f"dim={quotient.shape[1]}, defects=({hermitian_defect:.12g},{square_defect:.12g},{anticommutator_defect:.12g})",
    )

    observation = selector @ kernel
    observed_closure = observation @ section_carrier
    observed_rank, observed_smallest, _ = singular_data(observed_closure)
    check(
        "the observer-section map does not descend through the rank-512 repair quotient",
        observed_rank == 512
        and observed_smallest > 0.5
        and np.linalg.norm(observed_closure) > 20.0,
        f"rank={observed_rank}, sv+={observed_smallest:.12g}, norm={np.linalg.norm(observed_closure):.12g}",
    )

    registry = json.loads(
        (ROOT / "lab/process/eric-curt-wave3d-b2c-projected-gauge-quotient-gate.json").read_text(),
        object_pairs_hook=unique_object,
    )
    campaign = json.loads(
        (ROOT / "lab/process/eric-curt-ten-wave-campaign.json").read_text(),
        object_pairs_hook=unique_object,
    )
    wave3 = next(wave for wave in campaign["waves"] if wave["id"] == "ECW3-G4-OBSERVATION")
    b2b = wave3["result"]["wave3d"]["wave3d_b1"]["wave3d_b2a"]["wave3d_b2b"]
    b2c1 = b2b["wave3d_b2c1"]

    previous = registry["previous_source_action_external_datum_attempt"]
    check(
        "the prior tau solve is retained as a projector-only result with tangent ambiguity",
        previous["source_noether_tau"]["result"] == "TAU_SCHUR_PROJECTOR_ONLY"
        and previous["source_noether_tau"]["free_tangent_map_complex_dimension"] == 212992,
    )
    check(
        "P1/P2 and P3 remain separately typed and are not quotient projectors",
        previous["external_datum"]["P1_P2"] == "ONE_FLAT_REAL_ORIENTATION_LINE"
        and previous["external_datum"]["P3"] == "SEPARATE_RELATIVE_REAL_KO_TWIST"
        and not previous["external_datum"]["supplies_gauge_projector"],
    )
    check(
        "the registry distinguishes the two failed repair forks",
        registry["repair_forks"]["root_dependent_residual_halves"]["verdict"]
        == "OPEN_ONLY_AFTER_INDEPENDENT_SOURCE_DERIVATION"
        and registry["repair_forks"]["fixed_common_quotient"]["verdict"]
        == "KILLED_BY_OBSERVER_SECTION_CARRIER_ERASURE",
    )
    check(
        "the decisive result carries source silence and no source-as-proof upgrade",
        registry["source_collision"]["disposition"] == "SOURCE-SILENT"
        and not registry["source_collision"]["source_is_mathematical_evidence"],
    )
    check(
        "the campaign appends B2C1 and advances only to a source-derived tangent differential",
        b2c1["registry"]
        == "lab/process/eric-curt-wave3d-b2c-projected-gauge-quotient-gate.json"
        and b2c1["status_boundary"] == registry["status_boundary"]
        and b2c1["next_gate"] == registry["next_gate"]
        and wave3["result"]["active_next_swing"] == registry["next_gate"],
    )
    check(
        "record/finality remains a non-input and cannot supply the missing BV differential",
        registry["record_finality_candidate"]["status"]
        == "NOT_AN_INPUT_AND_CANNOT_SUPPLY_A_TANGENT_BV_DIFFERENTIAL",
    )
    promotion = registry["third_lane_promotion"]
    check(
        "Curt remains formally separate under the conjunctive third-lane gate",
        registry["curt_rival"]["status"]
        == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
        and promotion["logic"] == "TG-1 AND TG-2 AND TG-3"
        and promotion["verdict"] == "NOT_PROMOTED",
    )

    y_rows = direction_results["y"]["root_collision"]
    reject("the full projected source map is characteristic-symbol-null", all(row["characteristic_defect_rank"] == 0 for row in y_rows.values()))
    reject("equal rank alone makes the projected source map the Jordan image", all(row["jordan_intersection_rank"] == 128 for row in y_rows.values()))
    reject("one characteristic root supplies the full rank-128 Jordan image", any(row["characteristic_null_half_rank"] == 128 for row in y_rows.values()))
    reject("a root-dependent numerical null half is already a source-derived BV differential", registry["repair_forks"]["root_dependent_residual_halves"]["verdict"] == "BUILT")
    reject("the coordinate rank-384 Jordan span is a common invariant quotient kernel", coordinate_span.shape[1] == 512)
    reject("the fixed invariant repair preserves the observer-section carrier", observed_rank == 0)
    reject("Clifford repair alone makes the fixed quotient physically admissible", registry["repair_forks"]["fixed_common_quotient"]["verdict"] == "PASS")
    reject("the P1/P2 orientation line is a gauge projector", previous["external_datum"]["supplies_gauge_projector"])
    reject("the P3 KO twist is a gauge projector", previous["external_datum"]["supplies_gauge_projector"])
    reject("Noether tangency uniquely fixes the physical tangent map", previous["source_noether_tau"]["free_tangent_map_complex_dimension"] == 0)
    reject("source silence verifies the quotient computation", registry["source_collision"]["source_is_mathematical_evidence"])
    reject("record/finality supplies the missing tangent selector", registry["record_finality_candidate"]["status"] == "PASS")
    reject("the W131 collision transports to Curt's unbuilt real (7,7) carrier", registry["curt_rival"]["common_complexification_suffices"])
    reject("partial TG-1 evidence promotes Curt", promotion["verdict"] == "PROMOTED")

    print("-" * 96)
    if FAILURES:
        print(f"FAIL: {len(FAILURES)} failed checks: {FAILURES}")
        return 1
    print(f"RESULT: {EXACT} exact + {PLANTED} planted = {EXACT + PLANTED} PASS")
    print("VERDICT: existing projected-gauge quotient killed; source-derived tangent/BV differential open")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
