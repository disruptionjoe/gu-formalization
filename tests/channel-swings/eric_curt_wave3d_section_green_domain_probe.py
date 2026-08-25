#!/usr/bin/env python3
r"""ECW3D-A: admitted-section RS symbol, right-H Green trace, and domain-selection gate.

This probe takes one explicitly admitted flat Lorentz/spin section of the
actual metric bundle used by ECW3C.  In an adapted orthonormal frame its
tangent directions are three positive gimmel directions and one negative
direction.  The calculation pulls the already-verified W131 Cl(9,5)
Rarita--Schwinger symbol to that (3,1) block and constructs the boundary
Green matrix on ``ker Gamma``.

The result is deliberately algebraic.  It tests characteristic, Krein, and
right-H compatibility and whether the trace algebra itself selects a boundary
sector.  It does not prove existence of such a section on arbitrary X, a
Sobolev trace theorem for variable nonlinear coefficients, closedness or
self-adjointness of a differential realization, constraint propagation for
the full Euler packet, a propagator, BFV reduction, or any physical equation.
Curt's literal real (7,7) comparator is not transported through the common
complex algebra and remains a separately tagged rival.
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


TOL = 2.0e-8
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


def max_abs(value: np.ndarray) -> float:
    return float(np.max(np.abs(value)))


def matrix_product(matrices: list[np.ndarray]) -> np.ndarray:
    out = np.eye(matrices[0].shape[0], dtype=complex)
    for matrix in matrices:
        out = out @ matrix
    return out


def unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    out: dict[str, object] = {}
    for key, value in pairs:
        if key in out:
            raise ValueError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


def main() -> int:
    print("=" * 96)
    print("ECW3D-A ADMITTED-SECTION / RIGHT-H GREEN TRACE / DOMAIN-SELECTION GATE")
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

    check(
        "the W131 projector is rank 1664 and closes the ambient gamma trace",
        int(round(np.trace(projector).real)) == 1664
        and np.linalg.norm(gamma_trace @ projector) < TOL,
    )
    check(
        "the ambient Krein form is Hermitian and nondegenerate",
        max_abs(krein_vs - krein_vs.conj().T) < TOL
        and max_abs(krein_vs @ krein_vs - identity_vs) < TOL,
    )
    check(
        "the native antilinear quaternionic generator squares to minus one",
        max_abs(j_s @ j_s.conj() + identity_s) < TOL,
    )
    check(
        "ker Gamma is invariant under the native right-H structure",
        np.linalg.norm(projector @ j_vs - j_vs @ projector.conj()) < 2.0e-7,
    )

    # An admitted flat section in an adapted gimmel frame.  The positive
    # tangent directions are 0,1,2 and the negative/time direction is 9.
    section_indices = (0, 1, 2, 9)
    section_signature = tuple(int(eta[i]) for i in section_indices)
    check(
        "the admitted section tangent block has Lorentz signature (3,1)",
        section_signature == (1, 1, 1, -1),
        f"signature={section_signature}",
    )
    check(
        "the pulled-back Clifford generators close Cl(3,1) exactly",
        max(
            max_abs(
                gammas[left] @ gammas[right]
                + gammas[right] @ gammas[left]
                - (
                    2.0 * eta[left] * identity_s
                    if left == right
                    else np.zeros_like(identity_s)
                )
            )
            for left in section_indices
            for right in section_indices
        )
        < TOL,
    )

    # Use an orthonormal basis of ker Gamma exactly as W131 does.  The only
    # tolerance-bearing step is the Hermitian eigensolver for the already
    # exact orthogonal projector.
    values, vectors = np.linalg.eigh(projector)
    kernel = vectors[:, values > 0.5]
    check(
        "the numerical ker-Gamma basis is orthonormal and complete",
        kernel.shape == (1792, 1664)
        and max_abs(kernel.conj().T @ kernel - np.eye(1664)) < 2.0e-8
        and np.linalg.norm(projector @ kernel - kernel) < 2.0e-7,
    )

    krein_kernel = kernel.conj().T @ krein_vs @ kernel
    j_kernel = kernel.conj().T @ j_vs @ kernel.conj()
    check(
        "the induced right-H structure remains quaternionic on ker Gamma",
        max_abs(j_kernel @ j_kernel.conj() + np.eye(1664)) < 3.0e-8,
    )
    check(
        "the induced Krein form is nondegenerate on ker Gamma",
        np.min(np.abs(np.linalg.eigvalsh(krein_kernel))) > 0.5,
    )

    def cxi(components: tuple[float, float, float, float]) -> np.ndarray:
        return sum(
            components[position] * gammas[index]
            for position, index in enumerate(section_indices)
        )

    def restricted_symbol(components: tuple[float, float, float, float]) -> np.ndarray:
        return kernel.conj().T @ np.kron(identity_v, cxi(components)) @ kernel

    spacelike = restricted_symbol((1.0, 0.0, 0.0, 0.0))
    timelike = restricted_symbol((0.0, 0.0, 0.0, 1.0))
    null = restricted_symbol((1.0, 0.0, 0.0, 1.0))
    generic = restricted_symbol((2.0, -1.0, 0.5, 0.25))
    doubled = restricted_symbol((4.0, -2.0, 1.0, 0.5))

    check(
        "the section-pulled symbol is exactly first-order linear",
        max_abs(doubled - 2.0 * generic) < 2.0e-8,
    )
    check(
        "spacelike and timelike section covectors are noncharacteristic",
        np.linalg.svd(spacelike, compute_uv=False)[-1] > 1.0e-3
        and np.linalg.svd(timelike, compute_uv=False)[-1] > 1.0e-3,
    )
    check(
        "a Lorentz-null section covector is characteristic",
        np.linalg.svd(null, compute_uv=False)[-1] < 1.0e-8,
    )
    check(
        "the pulled-back symbol is right-H linear on ker Gamma",
        max(
            max_abs(symbol @ j_kernel - j_kernel @ symbol.conj())
            for symbol in (spacelike, timelike, generic)
        )
        < 3.0e-7,
    )

    # Green trace for a timelike boundary whose outward conormal is the first
    # spacelike section covector.  K D is the formal divergence pairing.
    green = krein_kernel @ spacelike
    hermitian_defect = max_abs(green - green.conj().T)
    green_eigenvalues, green_vectors = np.linalg.eigh(
        0.5 * (green + green.conj().T)
    )
    positive = green_vectors[:, green_eigenvalues > 1.0e-7]
    negative = green_vectors[:, green_eigenvalues < -1.0e-7]
    nullity = 1664 - positive.shape[1] - negative.shape[1]
    check(
        "the section Green trace matrix is Hermitian",
        hermitian_defect < 3.0e-7,
        f"defect={hermitian_defect:.2e}",
    )
    check(
        "the Green trace is nondegenerate and balanced",
        positive.shape[1] == 832
        and negative.shape[1] == 832
        and nullity == 0,
        f"inertia=({positive.shape[1]},{negative.shape[1]},{nullity})",
    )

    # Determine whether the anti-linear right-H action preserves the two
    # spectral sectors.  If both do, the exact algebra admits two opposite
    # maximal definite trace choices and therefore does not select one.
    p_plus = positive @ positive.conj().T
    p_minus = negative @ negative.conj().T
    plus_j_defect = np.linalg.norm(p_plus @ j_kernel - j_kernel @ p_plus.conj())
    minus_j_defect = np.linalg.norm(p_minus @ j_kernel - j_kernel @ p_minus.conj())
    check(
        "both opposite Green spectral sectors are right-H invariant",
        plus_j_defect < 2.0e-6 and minus_j_defect < 2.0e-6,
        f"defects=({plus_j_defect:.2e},{minus_j_defect:.2e})",
    )
    check(
        "the two right-H trace sectors are distinct and exhaust the boundary data",
        np.linalg.norm(p_plus @ p_minus) < 2.0e-6
        and max_abs(p_plus + p_minus - np.eye(1664)) < 2.0e-6,
    )
    check(
        "the Green flux signs of the two admissible algebraic sectors are opposite",
        np.min(np.linalg.eigvalsh(positive.conj().T @ green @ positive)) > 1.0e-7
        and np.max(np.linalg.eigvalsh(negative.conj().T @ green @ negative)) < -1.0e-7,
    )

    registry = json.loads(
        (ROOT / "lab/process/eric-curt-wave3d-section-green-domain.json").read_text(),
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
    wave3d = wave3["result"]["wave3d"]
    check(
        "the machine registry records the computed section and Green inertias",
        registry["construction"]["section_signature"] == [3, 1]
        and registry["construction"]["ambient_gamma_trace_kernel_complex_rank"] == 1664
        and registry["exact_results"]["green_inertia"]
        == {"positive": 832, "negative": 832, "null": 0},
    )
    check(
        "the registry keeps analytic closedness and physical surplus open",
        "ANALYTIC_CLOSEDNESS_OPEN" in registry["status_boundary"]
        and registry["constraint_parameter_surplus"]["physical_surplus"] == "UNCOMPUTABLE",
    )
    check(
        "the campaign records ECW3D-A without overwriting completed ECW3C",
        wave3d["registry"] == "lab/process/eric-curt-wave3d-section-green-domain.json"
        and wave3d["status_boundary"] == registry["status_boundary"]
        and wave3["result"]["wave3c"]["registry"]
        == "lab/process/eric-curt-wave3c-y14-atlas-cauchy-domain.json",
    )
    check(
        "the next gate is variable-coefficient closed-domain analysis",
        registry["next_gate"] == "ECW3D-B-VARIABLE-COEFFICIENT-RIGHT-H-CLOSED-DOMAIN"
        and wave3d["next_gate"] == registry["next_gate"],
    )
    promotion = registry["third_lane_promotion"]
    check(
        "Curt remains a separated rival under the conjunctive promotion rule",
        registry["curt_rival"]["status"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
        and promotion["logic"] == "TG-1 AND TG-2 AND TG-3"
        and promotion["verdict"] == "NOT_PROMOTED",
    )
    check(
        "the completed-wave live pointer retains the broader ECW3D compatibility gate",
        wave3["result"]["current_next_swing"]
        == "ECW3D-SECTION-PULLBACK-RIGHT-H-GREEN-DOMAIN",
    )

    hostile_vector = np.zeros(1664, dtype=complex)
    hostile_vector[0] = 1.0
    hostile_projector = np.outer(hostile_vector, hostile_vector.conj())
    hostile_right_h_defect = np.linalg.norm(
        hostile_projector @ j_kernel
        - j_kernel @ hostile_projector.conj()
    )

    # These are the load-bearing honesty plants.  Each false claim is tied to
    # a computed or registry-backed contrary witness, not a constant flag.
    reject(
        "an admitted flat section proves a Lorentz/spin section exists on arbitrary X",
        "arbitrary X" in registry["construction"]["object"],
    )
    reject(
        "section hyperbolicity resurrects full-ambient (9,5) hyperbolicity",
        registry["construction"]["ambient_signature"] == [3, 1],
    )
    reject(
        "a nondegenerate Green matrix is already a closed operator domain",
        "ANALYTIC_CLOSEDNESS_OPEN" not in registry["status_boundary"],
    )
    reject(
        "the exact trace algebra uniquely selects the positive sector",
        positive.shape[1] == 1664,
    )
    reject(
        "the exact trace algebra uniquely selects the negative sector",
        negative.shape[1] == 1664,
    )
    reject(
        "right-H coefficient compatibility makes every trace subspace right-H invariant",
        hostile_right_h_defect < 2.0e-6,
    )
    reject(
        "principal-symbol closure proves nonlinear Euler constraint propagation",
        "FULL_EINSTEIN_DIRAC_ACTION_OPEN"
        not in registry["non_regression"]["odd_matter"],
    )
    reject(
        "a formal boundary pairing constructs the physical BFV quotient",
        "BFV_OPEN" not in registry["non_regression"]["quantum_domain"],
    )
    reject(
        "the common complex algebra transports Curt's real (7,7) domain",
        registry["curt_rival"]["common_complexification_suffices"],
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
    print("VERDICT: section principal/Green algebra closes; analytic domain selection remains extra data")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
