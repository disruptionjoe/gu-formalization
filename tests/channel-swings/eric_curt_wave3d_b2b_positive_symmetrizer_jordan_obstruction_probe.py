#!/usr/bin/env python3
r"""ECW3D-B2B: full positive-symmetrizer cone Jordan obstruction.

On the actual W131 ``ker Gamma`` carrier and the admitted ``(3,1)`` section,
write ``C_j=A_t^{-1}A_j``.  A positive symmetrizer would satisfy
``H C_j=C_j^dagger H``.  Then ``H^(1/2) C_j H^(-1/2)`` would be Hermitian, so
every ``C_j`` would be diagonalizable.

The probe instead finds, for each tested nonzero spatial covector ``xi``,

    N_xi = C(xi)^2 - |xi|^2 I != 0,   rank(N_xi)=128,   N_xi^2=0.

Thus the minimal polynomial has a repeated root and the generator is not
diagonalizable.  This kills every positive simultaneous symmetrizer, hence
also the positive right-H subcone.  It does not decide a justified
constraint/gauge quotient, a changed principal system, pseudodifferential or
anisotropic energies, variable coefficients, or the ambient ultrahyperbolic
boundary problem.
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


def numerical_rank(matrix: np.ndarray) -> tuple[int, float, float]:
    singular = np.linalg.svd(matrix, compute_uv=False)
    rank = int(np.sum(singular > RANK_TOL))
    smallest_nonzero = float(singular[rank - 1]) if rank else 0.0
    largest_zero = float(singular[rank]) if rank < len(singular) else 0.0
    return rank, smallest_nonzero, largest_zero


def unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    out: dict[str, object] = {}
    for key, value in pairs:
        if key in out:
            raise ValueError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


def main() -> int:
    print("=" * 96)
    print("ECW3D-B2B POSITIVE SIMULTANEOUS-SYMMETRIZER JORDAN OBSTRUCTION")
    print("=" * 96)

    gammas, gamma_trace, projector, _ = gb.constraint_objects()
    eta = np.array([1.0] * 9 + [-1.0] * 5)
    identity_v = np.eye(14, dtype=complex)
    identity_vs = np.eye(14 * 128, dtype=complex)

    beta_s = matrix_product(gammas[:9])
    krein_vs = np.kron(np.diag(eta), beta_s)
    j_s = matrix_product([gammas[i] for i in (1, 3, 5, 7, 10, 12)])
    j_vs = np.kron(identity_v, j_s)

    section = {"y": 0, "x": 1, "z": 2, "t": 9}
    check(
        "the frozen section has signature (3,1)",
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
        "ker Gamma is invariant under native right-H",
        np.linalg.norm(projector @ j_vs - j_vs @ projector.conj()) < TOL,
    )

    values, vectors = np.linalg.eigh(projector)
    kernel = vectors[:, values > 0.5]
    identity = np.eye(1664, dtype=complex)
    check(
        "the numerical ker-Gamma basis is orthonormal and complete",
        kernel.shape == (1792, 1664)
        and max_abs(kernel.conj().T @ kernel - identity) < 3.0e-8,
    )

    krein = kernel.conj().T @ krein_vs @ kernel
    right_h = kernel.conj().T @ j_vs @ kernel.conj()
    check(
        "the induced Krein form is nondegenerate",
        np.min(np.abs(np.linalg.eigvalsh(krein))) > 0.5,
    )
    check(
        "the induced antilinear generator remains quaternionic",
        max_abs(right_h @ right_h.conj() + identity) < 4.0e-8,
    )

    symbols = {
        name: kernel.conj().T
        @ np.kron(identity_v, gammas[index])
        @ kernel
        for name, index in section.items()
    }
    check(
        "all four section symbols preserve right-H",
        max(
            max_abs(symbol @ right_h - right_h @ symbol.conj())
            for symbol in symbols.values()
        )
        < TOL,
    )

    a_t = symbols["t"]
    time_singular = np.linalg.svd(a_t, compute_uv=False)
    check(
        "the section time symbol remains noncharacteristic",
        abs(float(time_singular[-1]) - 6.0 / 7.0) < 2.0e-8
        and abs(float(time_singular[0]) - 1.0) < 2.0e-8,
        f"singular range=({time_singular[-1]:.12g},{time_singular[0]:.12g})",
    )

    inverse_time = np.linalg.inv(a_t)
    evolution = {
        name: inverse_time @ symbols[name] for name in ("y", "x", "z")
    }
    check(
        "all three evolution generators preserve right-H",
        max(
            max_abs(matrix @ right_h - right_h @ matrix.conj())
            for matrix in evolution.values()
        )
        < TOL,
    )

    time_flux = krein @ a_t
    check(
        "the native time flux remains Hermitian and right-H compatible",
        max_abs(time_flux - time_flux.conj().T) < TOL
        and max_abs(time_flux @ right_h - right_h @ time_flux.conj()) < TOL,
    )
    check(
        "the native time flux exactly symmetrizes all spatial generators",
        max(
            max_abs(time_flux @ matrix - (time_flux @ matrix).conj().T)
            for matrix in evolution.values()
        )
        < TOL,
    )
    flux_values = np.linalg.eigvalsh(0.5 * (time_flux + time_flux.conj().T))
    check(
        "that exact simultaneous symmetrizer is balanced rather than positive",
        int(np.sum(flux_values > 1.0e-7)) == 832
        and int(np.sum(flux_values < -1.0e-7)) == 832,
    )

    directions = {
        "y": ((1.0, 0.0, 0.0), 1.0),
        "x": ((0.0, 1.0, 0.0), 1.0),
        "z": ((0.0, 0.0, 1.0), 1.0),
        "generic_1_2_3": ((1.0, 2.0, 3.0), 14.0),
    }
    jordan: dict[str, dict[str, float | int]] = {}
    for label, (coefficients, norm_sq) in directions.items():
        c_xi = sum(
            coefficients[index] * evolution[name]
            for index, name in enumerate(("y", "x", "z"))
        )
        nilpotent = c_xi @ c_xi - norm_sq * identity
        nilpotent_sq = nilpotent @ nilpotent
        rank, smallest_nonzero, largest_zero = numerical_rank(nilpotent)
        jordan[label] = {
            "rank": rank,
            "max_abs": max_abs(nilpotent),
            "max_abs_square": max_abs(nilpotent_sq),
            "smallest_nonzero_singular": smallest_nonzero,
            "largest_zero_singular": largest_zero,
        }
        check(
            f"{label} has a nonzero rank-128 quadratic Jordan remainder",
            rank == 128
            and smallest_nonzero > 0.6 * norm_sq
            and largest_zero < 2.0e-10,
            f"rank={rank}, sv+={smallest_nonzero:.12g}, sv0={largest_zero:.12g}",
        )
        check(
            f"{label} Jordan remainder is square-zero",
            max_abs(nilpotent) > 0.1 * norm_sq
            and max_abs(nilpotent_sq) < 2.0e-11,
            f"max|N|={max_abs(nilpotent):.12g}, max|N^2|={max_abs(nilpotent_sq):.12g}",
        )

    c_y = evolution["y"]
    minus_rank, _, _ = numerical_rank(c_y + identity)
    plus_rank, _, _ = numerical_rank(c_y - identity)
    check(
        "both y characteristic roots have geometric multiplicity 768",
        (1664 - minus_rank, 1664 - plus_rank) == (768, 768),
        f"nullities=({1664-minus_rank},{1664-plus_rank})",
    )
    check(
        "the nonzero square-zero remainder is a diagonalizability obstruction",
        jordan["y"]["rank"] == 128
        and jordan["y"]["max_abs_square"] < 2.0e-11,
    )

    registry = json.loads(
        (ROOT / "lab/process/eric-curt-wave3d-b2b-positive-symmetrizer-jordan-obstruction.json").read_text(),
        object_pairs_hook=unique_object,
    )
    campaign = json.loads(
        (ROOT / "lab/process/eric-curt-ten-wave-campaign.json").read_text(),
        object_pairs_hook=unique_object,
    )
    wave3 = next(wave for wave in campaign["waves"] if wave["id"] == "ECW3-G4-OBSERVATION")
    b2b = wave3["result"]["wave3d"]["wave3d_b1"]["wave3d_b2a"]["wave3d_b2b"]

    obstruction = registry["computed_jordan_obstruction"]
    check(
        "the registry kills the full positive cone before imposing right-H",
        obstruction["positive_symmetrizer_cone"]
        == "EMPTY_BY_NONDIAGONALIZABLE_SPATIAL_GENERATOR"
        and obstruction["right_h_positive_subcone"] == "EMPTY_AS_A_SUBCONE",
    )
    check(
        "the registry preserves the exact indefinite simultaneous symmetrizer",
        obstruction["indefinite_symmetrizer"]
        == "NATIVE_TIME_FLUX_EXACT_WITH_BALANCED_832_832_INERTIA",
    )
    check(
        "the decisive result carries source silence and an evidence boundary",
        registry["source_collision"]["disposition"] == "SOURCE-SILENT"
        and not registry["source_collision"]["source_is_mathematical_evidence"],
    )
    check(
        "Layer-0 keeps characteristic roots separate from strong hyperbolicity",
        any(
            row["shared_term"] == "hyperbolic"
            and row["disposition"] == "HOMONYM"
            for row in registry["layer_0_dictionary"]
        ),
    )
    check(
        "record/finality cannot repair the unchanged defective generator",
        registry["record_finality_candidate"]["status"]
        == "KILLED_AS_A_SELECTOR_FOR_THE_UNCHANGED_W131_PRINCIPAL_SYSTEM",
    )
    check(
        "the campaign appends B2B without rewriting B2A",
        b2b["registry"]
        == "lab/process/eric-curt-wave3d-b2b-positive-symmetrizer-jordan-obstruction.json"
        and b2b["status_boundary"] == registry["status_boundary"],
    )
    check(
        "the campaign advances only to the constraint/gauge quotient gate",
        wave3["result"]["active_next_swing"] == registry["next_gate"]
        and b2b["next_gate"] == registry["next_gate"],
    )
    promotion = registry["third_lane_promotion"]
    check(
        "Curt remains formally separate under the conjunctive promotion gate",
        registry["curt_rival"]["status"]
        == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
        and promotion["logic"] == "TG-1 AND TG-2 AND TG-3"
        and promotion["verdict"] == "NOT_PROMOTED",
    )

    reject("real characteristic roots imply diagonalizability", jordan["y"]["rank"] == 0)
    reject("a square-zero remainder must itself vanish", jordan["y"]["max_abs"] < TOL)
    reject("C_y satisfies C_y squared equals identity", jordan["y"]["max_abs"] < TOL)
    reject("rank 128 is numerical threshold noise", jordan["y"]["smallest_nonzero_singular"] < 1.0e-4)
    reject("a positive symmetrizer may retain a nontrivial Jordan block", obstruction["positive_symmetrizer_cone"] == "NONEMPTY")
    reject("right-H compatibility removes the Jordan remainder", obstruction["right_h_positive_subcone"] == "NONEMPTY")
    reject("an indefinite exact symmetrizer is a positive energy", np.all(flux_values > 0.0))
    reject("the unreduced W131 kill automatically kills every constraint quotient", registry["constraint_gauge_quotient"]["status"] == "KILLED")
    reject("an ordering arrow diagonalizes the fixed principal generator", registry["record_finality_candidate"]["status"] == "PASS")
    reject("Weinstein supplied the Jordan computation", registry["source_collision"]["disposition"] == "SOURCE-CONFIRMS")
    reject("the Eric W131 result transports to Curt's real (7,7) carrier", registry["curt_rival"]["common_complexification_suffices"])
    reject("maximal dissipativity is reached despite the energy obstruction", registry["boundary_domain"]["maximal_dissipativity"] == "PASS")
    reject("partial TG-1 evidence promotes Curt", promotion["verdict"] == "PROMOTED")

    print("-" * 96)
    if FAILURES:
        print(f"FAIL: {len(FAILURES)} failed checks: {FAILURES}")
        return 1
    print(f"RESULT: {EXACT} exact + {PLANTED} planted = {EXACT + PLANTED} PASS")
    print("VERDICT: full positive simultaneous-symmetrizer cone killed; constraint/gauge quotient open")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
