#!/usr/bin/env python3
r"""ECW3D-B2A: native time-flux and canonical-majorant coercivity gate.

The probe uses the actual W131 ``ker Gamma`` carrier on the admitted ``(3,1)``
section. It tests the native time flux ``E_t=K A_t`` and its canonical spectral
majorant ``H_t=|E_t|``. A positive matrix is an evolution energy only if it
also symmetrizes all spatial evolution matrices ``C_j=A_t^{-1}A_j``.

This is a finite principal-symbol gate. It does not enumerate every positive
right-H symmetrizer, prove a variable-coefficient energy estimate, establish
maximal dissipativity, or propagate the nonlinear Euler constraints.
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


def multiplicities(values: np.ndarray) -> list[tuple[float, int]]:
    groups: list[list[float | int]] = []
    for value in values:
        if not groups or abs(float(value) - float(groups[-1][0])) > 1.0e-7:
            groups.append([float(value), 1])
        else:
            groups[-1][1] = int(groups[-1][1]) + 1
    return [(float(value), int(count)) for value, count in groups]


def unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    out: dict[str, object] = {}
    for key, value in pairs:
        if key in out:
            raise ValueError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


def main() -> int:
    print("=" * 96)
    print("ECW3D-B2A NATIVE TIME FLUX / CANONICAL MAJORANT COERCIVITY GATE")
    print("=" * 96)

    gammas, gamma_trace, projector, _ = gb.constraint_objects()
    eta = np.array([1.0] * 9 + [-1.0] * 5)
    identity_s = np.eye(128, dtype=complex)
    identity_v = np.eye(14, dtype=complex)
    identity_vs = np.eye(14 * 128, dtype=complex)

    beta_s = matrix_product(gammas[:9])
    krein_vs = np.kron(np.diag(eta), beta_s)
    j_s = matrix_product([gammas[i] for i in (1, 3, 5, 7, 10, 12)])
    j_vs = np.kron(identity_v, j_s)

    section = {"y": 0, "x": 1, "z": 2, "t": 9}
    check(
        "the frozen section has three positive spatial directions and one negative time direction",
        tuple(int(eta[section[key]]) for key in ("y", "x", "z", "t"))
        == (1, 1, 1, -1),
    )
    check(
        "the W131 projector has rank 1664 and closes the gamma trace",
        int(round(np.trace(projector).real)) == 1664
        and np.linalg.norm(gamma_trace @ projector) < TOL,
    )
    check(
        "the ambient Krein form is a Hermitian involution",
        max_abs(krein_vs - krein_vs.conj().T) < TOL
        and max_abs(krein_vs @ krein_vs - identity_vs) < TOL,
    )
    check(
        "ker Gamma is invariant under the native right-H structure",
        np.linalg.norm(projector @ j_vs - j_vs @ projector.conj()) < TOL,
    )

    values, vectors = np.linalg.eigh(projector)
    kernel = vectors[:, values > 0.5]
    check(
        "the numerical ker-Gamma basis is orthonormal and complete",
        kernel.shape == (1792, 1664)
        and max_abs(kernel.conj().T @ kernel - np.eye(1664)) < 3.0e-8,
    )

    krein = kernel.conj().T @ krein_vs @ kernel
    right_h = kernel.conj().T @ j_vs @ kernel.conj()
    check(
        "the induced Krein form is nondegenerate",
        np.min(np.abs(np.linalg.eigvalsh(krein))) > 0.5,
    )
    check(
        "the induced antilinear generator remains quaternionic",
        max_abs(right_h @ right_h.conj() + np.eye(1664)) < 4.0e-8,
    )

    symbols = {
        name: kernel.conj().T
        @ np.kron(identity_v, gammas[index])
        @ kernel
        for name, index in section.items()
    }
    check(
        "all four section symbols preserve the native right-H structure",
        max(
            max_abs(symbol @ right_h - right_h @ symbol.conj())
            for symbol in symbols.values()
        )
        < TOL,
    )

    a_t = symbols["t"]
    singular = np.linalg.svd(a_t, compute_uv=False)
    check(
        "the continuous Lorentz time coordinate is noncharacteristic on W131",
        abs(float(singular[-1]) - 6.0 / 7.0) < 2.0e-8
        and abs(float(singular[0]) - 1.0) < 2.0e-8,
        f"singular range=({singular[-1]:.12g},{singular[0]:.12g})",
    )

    time_flux = krein @ a_t
    check(
        "the native time flux is Hermitian",
        max_abs(time_flux - time_flux.conj().T) < TOL,
    )
    time_values, time_vectors = np.linalg.eigh(
        0.5 * (time_flux + time_flux.conj().T)
    )
    time_groups = multiplicities(time_values)
    expected_groups = [(-1.0, 768), (-6.0 / 7.0, 64), (6.0 / 7.0, 64), (1.0, 768)]
    check(
        "the native time-flux spectrum has the computed four exact clusters",
        len(time_groups) == len(expected_groups)
        and all(
            abs(value - expected) < 2.0e-8 and count == expected_count
            for (value, count), (expected, expected_count) in zip(
                time_groups, expected_groups
            )
        ),
        f"groups={time_groups}",
    )
    positive = int(np.sum(time_values > 1.0e-7))
    negative = int(np.sum(time_values < -1.0e-7))
    null = 1664 - positive - negative
    check(
        "the native time flux is nondegenerate but balanced",
        (positive, negative, null) == (832, 832, 0),
    )
    check(
        "balanced inertia kills positive coercivity of the native time flux",
        float(time_values[0]) < -0.85 and float(time_values[-1]) > 0.85,
    )
    check(
        "the native time flux remains right-H compatible",
        max_abs(time_flux @ right_h - right_h @ time_flux.conj()) < TOL,
    )

    theta = time_vectors @ np.diag(np.sign(time_values)) @ time_vectors.conj().T
    majorant = time_vectors @ np.diag(np.abs(time_values)) @ time_vectors.conj().T
    check(
        "the spectral sign is a Hermitian involution",
        max_abs(theta - theta.conj().T) < TOL
        and max_abs(theta @ theta - np.eye(1664)) < TOL,
    )
    check(
        "the spectral sign and absolute-value majorant preserve right-H",
        max_abs(theta @ right_h - right_h @ theta.conj()) < TOL
        and max_abs(majorant @ right_h - right_h @ majorant.conj()) < TOL,
    )
    majorant_values = np.linalg.eigvalsh(0.5 * (majorant + majorant.conj().T))
    majorant_groups = multiplicities(majorant_values)
    check(
        "the canonical spectral majorant is positive definite",
        len(majorant_groups) == 2
        and abs(majorant_groups[0][0] - 6.0 / 7.0) < 2.0e-8
        and majorant_groups[0][1] == 128
        and abs(majorant_groups[1][0] - 1.0) < 2.0e-8
        and majorant_groups[1][1] == 1536,
        f"groups={majorant_groups}",
    )
    check(
        "the spectral factorization reproduces abs(E_t)",
        max_abs(theta @ time_flux - majorant) < TOL,
    )

    inverse_time = np.linalg.inv(a_t)
    evolution = {
        name: inverse_time @ symbols[name] for name in ("y", "x", "z")
    }
    check(
        "all spatial evolution matrices preserve right-H",
        max(
            max_abs(matrix @ right_h - right_h @ matrix.conj())
            for matrix in evolution.values()
        )
        < TOL,
    )
    defects = {
        name: max_abs(majorant @ matrix - (majorant @ matrix).conj().T)
        for name, matrix in evolution.items()
    }
    check(
        "the positive spectral majorant fails to symmetrize y evolution",
        defects["y"] > 0.15,
        f"defect={defects['y']:.12g}",
    )
    check(
        "the positive spectral majorant fails to symmetrize x evolution",
        defects["x"] > 0.15,
        f"defect={defects['x']:.12g}",
    )
    check(
        "the positive spectral majorant fails to symmetrize z evolution",
        defects["z"] > 0.15,
        f"defect={defects['z']:.12g}",
    )

    registry = json.loads(
        (ROOT / "lab/process/eric-curt-wave3d-b2a-native-time-flux-coercivity-kill.json").read_text(),
        object_pairs_hook=unique_object,
    )
    campaign = json.loads(
        (ROOT / "lab/process/eric-curt-ten-wave-campaign.json").read_text(),
        object_pairs_hook=unique_object,
    )
    wave3 = next((wave for wave in campaign["waves"] if wave["id"] == "ECW3-G4-OBSERVATION"), None)
    if wave3 is None:
        print("FAIL: campaign is missing the Wave 3 observation row", flush=True)
        return 1
    b2a = wave3["result"]["wave3d"]["wave3d_b1"]["wave3d_b2a"]
    successor = b2a.get("wave3d_b2b")
    latest_successor = successor.get("wave3d_b2c1") if successor else None
    active_expected = (
        latest_successor["next_gate"]
        if latest_successor
        else successor["next_gate"]
        if successor
        else registry["next_gate"]
    )

    check(
        "the registry records that coercivity fails before maximal dissipativity is reached",
        registry["computed_time_flux"]["native_flux_coercivity"]
        == "KILLED_BALANCED_INDEFINITE"
        and registry["boundary_domain"]["maximal_dissipativity"].startswith(
            "NOT_REACHED"
        ),
    )
    check(
        "the decisive result carries a primary-source collision with an evidence boundary",
        registry["source_collision"]["disposition"] == "SOURCE-SILENT"
        and not registry["source_collision"]["source_is_mathematical_evidence"],
    )
    check(
        "record/finality is retained as an unconsumed candidate control",
        registry["record_finality_candidate"]["status"]
        == "NOT_USED_AS_A_B2A_INPUT__RETAINED_FOR_B2B_TEST"
        and registry["record_finality_candidate"]["tag"] == "JOE_CANDIDATE_CONTROL",
    )
    check(
        "the campaign preserves B2A and advances through its deepest recorded successor",
        b2a["registry"]
        == "lab/process/eric-curt-wave3d-b2a-native-time-flux-coercivity-kill.json"
        and b2a["status_boundary"] == registry["status_boundary"]
        and b2a["next_gate"] == registry["next_gate"]
        and wave3["result"]["active_next_swing"] == active_expected,
    )
    promotion = registry["third_lane_promotion"]
    check(
        "Curt remains a formally separated rival under the conjunctive promotion gate",
        registry["curt_rival"]["status"]
        == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
        and promotion["logic"] == "TG-1 AND TG-2 AND TG-3"
        and promotion["verdict"] == "NOT_PROMOTED",
    )

    reject("noncharacteristic time implies a positive native energy", positive == 1664)
    reject("right-H compatibility makes the native time flux coercive", negative == 0)
    reject("taking abs(E_t) automatically symmetrizes y evolution", defects["y"] < TOL)
    reject("taking abs(E_t) automatically symmetrizes x evolution", defects["x"] < TOL)
    reject("taking abs(E_t) automatically symmetrizes z evolution", defects["z"] < TOL)
    reject(
        "a positive matrix alone proves a symmetric-hyperbolic energy estimate",
        all(defect < TOL for defect in defects.values()),
    )
    reject(
        "failure of the canonical majorant kills every positive symmetrizer",
        "GENERAL_POSITIVE_SYMMETRIZER_KILLED" in registry["status_boundary"],
    )
    reject(
        "the Green sectors are already maximal-dissipative boundary data",
        registry["boundary_domain"]["maximal_dissipativity"] == "PASS",
    )
    reject(
        "Weinstein supplied the computed W131 time-flux spectrum",
        registry["source_collision"]["disposition"] == "SOURCE-CONFIRMS",
    )
    reject(
        "the record/finality proposal is an Eric-sourced datum",
        registry["record_finality_candidate"]["tag"] == "ERIC_REQUIRED",
    )
    reject(
        "the admitted section result solves the full ambient multiple-time problem",
        registry["construction"]["time_function"] == "GLOBAL_Y14_TIME",
    )
    reject(
        "partial TG-1 evidence promotes Curt without TG-2 and TG-3",
        promotion["verdict"] == "PROMOTED",
    )

    print("-" * 96)
    if FAILURES:
        print(f"FAIL: {len(FAILURES)} failed checks: {FAILURES}")
        return 1
    print(f"RESULT: {EXACT} exact + {PLANTED} planted = {EXACT + PLANTED} PASS")
    print("VERDICT: native time flux and abs(E_t) majorant fail; general symmetrizer search remains open")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
