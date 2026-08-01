#!/usr/bin/env python3
r"""ECW3D-B2C2B: natural super-IG/RS tangent, Noether, and observer gate.

The construction is frozen before target collision.  In the parity-neutral
first-order class built only from a covector k, the metric, Clifford
multiplication, and gamma trace, a scalar-spinor-to-vector-spinor symbol is in
the span of

    K(k) = k tensor 1,             Gamma^dagger c(k).

Gamma-tracelessness leaves the unique projective member

    T(k) = Pi_kerGamma K(k)
         = K(k) - (1/14) Gamma^dagger c(k).

The probe then collides that frozen member with the W131 principal symbol and
the unchanged observation map.  The result is deliberately bounded: it is not
an exhaustive no-go over enlarged field complexes, background soldering,
lower-order transformations, or nonlocal symbols.
"""

from __future__ import annotations

import json
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
for path in (ROOT / "tests", ROOT / "tests" / "generation-sector"):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

import gen_sector_bridge as gb  # noqa: E402


TOL = 8.0e-8
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
    print(f"{status}: planted rejection - {label}", flush=True)
    if false_claim:
        FAILURES.append(f"planted: {label}")


def max_abs(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(matrix)))


def rank(matrix: np.ndarray) -> int:
    return int(np.sum(np.linalg.svd(matrix, compute_uv=False) > RANK_TOL))


def image_basis(matrix: np.ndarray) -> np.ndarray:
    left, singular, _ = np.linalg.svd(matrix, full_matrices=False)
    return left[:, singular > RANK_TOL]


def residual_outside(subspace: np.ndarray, vectors: np.ndarray) -> float:
    return float(
        np.linalg.norm(vectors - subspace @ (subspace.conj().T @ vectors))
    )


def unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    out: dict[str, object] = {}
    for key, value in pairs:
        if key in out:
            raise ValueError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


def main() -> int:
    print("=" * 96)
    print("ECW3D-B2C2B NATURAL SUPER-IG/RS TANGENT, NOETHER, AND OBSERVER GATE")
    print("=" * 96)

    gammas, gamma_trace, projector, _ = gb.constraint_objects()
    identity_s = np.eye(128, dtype=complex)
    identity_v = np.eye(14, dtype=complex)
    identity_vs = np.eye(14 * 128, dtype=complex)
    eta = np.array([1.0] * 9 + [-1.0] * 5)
    section = {"y": 0, "x": 1, "z": 2, "t": 9}

    check(
        "the gamma-trace projector is exact on the active Cl(9,5) carrier",
        max_abs(gamma_trace @ gamma_trace.conj().T - 14.0 * identity_s) < TOL
        and max_abs(projector @ projector - projector) < TOL
        and max_abs(projector - projector.conj().T) < TOL
        and np.linalg.norm(gamma_trace @ projector) < TOL,
    )

    covectors = {
        "y": np.eye(14)[section["y"]],
        "timelike_t": np.eye(14)[section["t"]],
        "generic_section": np.array(
            [1.0, 2.0, -1.0] + [0.0] * 6 + [0.5] + [0.0] * 4
        ),
        "generic_ambient": np.array(
            [1.0, -2.0, 0.5, 0.25, -0.75, 1.5, 0.0, 0.4, -0.2,
             0.8, -1.1, 0.3, 0.6, -0.9]
        ),
    }
    natural_rows: dict[str, dict[str, float | int]] = {}

    # Only the predeclared natural grammar appears before the target collision.
    for label, k in covectors.items():
        c_k = sum(k[a] * gammas[a] for a in range(14))
        k_map = np.kron(k.reshape(14, 1), identity_s)
        trace_companion = gamma_trace.conj().T @ c_k
        constraint = np.column_stack(
            [
                (gamma_trace @ k_map).reshape(-1),
                (gamma_trace @ trace_companion).reshape(-1),
            ]
        )
        twistor = k_map - trace_companion / 14.0
        projected = projector @ k_map
        check(
            f"{label}: gamma-tracelessness leaves one natural projective symbol",
            rank(constraint) == 1
            and np.linalg.norm(gamma_trace @ k_map - c_k) < TOL
            and np.linalg.norm(gamma_trace @ twistor) < TOL
            and np.linalg.norm(twistor - projected) < TOL,
        )
        natural_rows[label] = {
            "raw_coefficient_dimension": 2,
            "gamma_trace_constraint_rank": rank(constraint),
            "surviving_coefficient_dimension": 1,
            "projector_identity_residual": float(np.linalg.norm(twistor - projected)),
        }

    # Target collision begins here, after the class and its unique member froze.
    k_off = covectors["y"]
    c_off = gammas[section["y"]]
    k_map_off = np.kron(k_off.reshape(14, 1), identity_s)
    tangent_off = projector @ k_map_off
    w131_off = projector @ np.kron(identity_v, c_off) @ projector
    noether_off = w131_off @ tangent_off
    intertwiner_off = (12.0 / 14.0) * tangent_off @ c_off
    check(
        "the frozen natural tangent obeys the exact W131 twistor intertwiner",
        np.linalg.norm(noether_off - intertwiner_off) < TOL,
        f"residual={np.linalg.norm(noether_off - intertwiner_off):.3g}",
    )
    check(
        "the unique nonzero natural tangent fails the off-shell Noether identity",
        rank(tangent_off) == 128
        and rank(noether_off) == 128
        and np.linalg.norm(noether_off) > 1.0,
        f"ranks=({rank(tangent_off)},{rank(noether_off)})",
    )

    k_null = np.zeros(14)
    k_null[section["y"]] = 1.0
    k_null[section["t"]] = 1.0
    c_null = sum(k_null[a] * gammas[a] for a in range(14))
    k_map_null = np.kron(k_null.reshape(14, 1), identity_s)
    tangent_null = projector @ k_map_null
    w131_null = projector @ np.kron(identity_v, c_null) @ projector
    noether_null = w131_null @ tangent_null
    _, singular_c, right_c = np.linalg.svd(c_null)
    c_rank = int(np.sum(singular_c > RANK_TOL))
    null_parameters = right_c.conj().T[:, c_rank:]
    characteristic_half = tangent_null @ null_parameters
    check(
        "the null covector has the expected rank-64 Dirac kernel",
        abs(float(k_null @ (eta * k_null))) < TOL
        and max_abs(c_null @ c_null) < TOL
        and c_rank == 64
        and null_parameters.shape[1] == 64,
    )
    check(
        "the full natural tangent remains non-Noether on the characteristic cone",
        rank(tangent_null) == 128
        and rank(noether_null) == 64
        and np.linalg.norm(noether_null) > 1.0,
        f"ranks=({rank(tangent_null)},{rank(noether_null)})",
    )
    check(
        "only the rank-64 on-shell parameter half is characteristic-exact",
        rank(characteristic_half) == 64
        and np.linalg.norm(w131_null @ characteristic_half) < TOL,
        f"rank={rank(characteristic_half)}",
    )

    j_s = gammas[1] @ gammas[3] @ gammas[5] @ gammas[7] @ gammas[10] @ gammas[12]
    right_h_vs = np.kron(identity_v, j_s)
    tangent_image = image_basis(tangent_null)
    h_residual = residual_outside(
        tangent_image, right_h_vs @ tangent_image.conj()
    )
    check(
        "the natural tangent image is right-H invariant",
        h_residual < TOL,
        f"residual={h_residual:.3g}",
    )

    observation = np.zeros((4 * 128, 14 * 128), dtype=complex)
    for block, name in enumerate(("y", "x", "z", "t")):
        source = section[name]
        observation[
            block * 128 : (block + 1) * 128,
            source * 128 : (source + 1) * 128,
        ] = identity_s
    observed_tangent_rank = rank(observation @ tangent_null)
    observed_half_rank = rank(observation @ characteristic_half)
    check(
        "unchanged observation is nonzero on both the full tangent and its characteristic half",
        observed_tangent_rank == 128 and observed_half_rank == 64,
        f"ranks=({observed_tangent_rank},{observed_half_rank})",
    )
    check(
        "the natural image therefore cannot be quotiented while leaving the observed carrier unchanged",
        np.linalg.norm(observation @ tangent_null) > 1.0
        and np.linalg.norm(observation @ characteristic_half) > 1.0,
    )

    registry = json.loads(
        (ROOT / "lab/process/eric-curt-wave3d-b2c2b-super-ig-rs-tangent-noether.json").read_text(),
        object_pairs_hook=unique_object,
    )
    campaign = json.loads(
        (ROOT / "lab/process/eric-curt-ten-wave-campaign.json").read_text(),
        object_pairs_hook=unique_object,
    )
    wave3 = next(
        wave for wave in campaign["waves"] if wave["id"] == "ECW3-G4-OBSERVATION"
    )
    b2c2a = (
        wave3["result"]["wave3d"]["wave3d_b1"]["wave3d_b2a"]
        ["wave3d_b2b"]["wave3d_b2c1"]["wave3d_b2c2a"]
    )
    b2c2b = b2c2a["wave3d_b2c2b"]

    check(
        "the registry bounds the result to the frozen natural first-order class",
        registry["natural_symbol_class"]["raw_coefficient_dimension"] == 2
        and registry["natural_symbol_class"]["gamma_trace_constraint_rank"] == 1
        and registry["natural_symbol_class"]["surviving_projective_candidates"] == 1
        and not registry["scope_boundary"]["exhaustive_over_enlarged_actions"],
    )
    check(
        "the conditional mixed super-IG bracket is not promoted to an RS field action",
        registry["mixed_super_ig_predecessor"]["bracket_target"]
        == "Omega1(sp(S_complex))"
        and registry["mixed_super_ig_predecessor"]["rs_tangent_rule"] == "NOT_SUPPLIED"
        and registry["mixed_super_ig_predecessor"]["ward_or_master_identity"] == "NOT_SUPPLIED",
    )
    check(
        "the decisive source collision is silent and source speech is not mathematical evidence",
        registry["source_collision"]["disposition"] == "SOURCE-SILENT"
        and not registry["source_collision"]["source_is_mathematical_evidence"],
    )
    check(
        "the campaign advances only the guided B2C2B pointer",
        b2c2b["registry"]
        == "lab/process/eric-curt-wave3d-b2c2b-super-ig-rs-tangent-noether.json"
        and b2c2b["status_boundary"] == registry["status_boundary"]
        and wave3["result"]["active_next_swing"] == b2c2b["next_gate"],
    )
    check(
        "P1/P2/P3 remain unused and cannot supply the missing action representation",
        not registry["external_datum"]["P1_P2_P3_used"]
        and not registry["external_datum"]["can_supply_rs_tangent_or_ward_identity"],
    )
    promotion = registry["third_lane_promotion"]
    check(
        "Curt remains formally separate under the conjunctive promotion gate",
        registry["curt_rival"]["status"]
        == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
        and promotion["logic"] == "TG-1 AND TG-2 AND TG-3"
        and promotion["verdict"] == "NOT_PROMOTED",
    )

    reject("two raw coefficients mean two gamma-traceless natural symbols", all(row["surviving_coefficient_dimension"] == 2 for row in natural_rows.values()))
    reject("the unique twistor symbol is an off-shell W131 Noether map", rank(noether_off) == 0)
    reject("null-cone rank loss proves off-shell BV closure", rank(noether_null) == 0)
    reject("the characteristic rank-64 parameter half is a source-selected ghost", registry["characteristic_half"]["source_selected"])
    reject("the mixed super-IG bracket itself maps scalar spinors into ker Gamma", registry["mixed_super_ig_predecessor"]["bracket_target"] == "ker Gamma")
    reject("field content automatically specifies the odd parameter module", registry["mixed_super_ig_predecessor"]["odd_parameter_module_source_fixed"])
    reject("right-H invariance supplies the missing Noether identity", h_residual < TOL and rank(noether_off) == 0)
    reject("unchanged observation descends through the natural quotient", observed_tangent_rank == 0)
    reject("P1/P2 or P3 selects the tangent rule", registry["external_datum"]["can_supply_rs_tangent_or_ward_identity"])
    reject("the bounded natural-class negative kills every enlarged action", registry["scope_boundary"]["exhaustive_over_enlarged_actions"])
    reject("the Eric complex result transports to Curt's literal real (7,7) carrier", registry["curt_rival"]["literal_7_7_port_complete"])
    reject("partial TG-1 evidence promotes Curt", promotion["verdict"] == "PROMOTED")

    print("-" * 96)
    if FAILURES:
        print(f"FAIL: {len(FAILURES)} failed checks: {FAILURES}")
        return 1
    print(f"RESULT: {EXACT} exact + {PLANTED} planted = {EXACT + PLANTED} PASS")
    print("VERDICT: unique natural tangent fails off-shell Noether and unchanged-observer descent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
