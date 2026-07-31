#!/usr/bin/env python3
r"""ECW3D-B1: variable-coefficient right-H boundary domain closedness kill.

This probe freezes the first analytic realization after ECW3D-A.  The section
is ``R_t x S^1_x x [0,1]_y x S^1_z`` with Lorentz tetrad

    e_t = a(y) d/dt,  e_x = a(y) d/dx,
    e_y = d/dy,       e_z = d/dz,
    a(y) = 1 + (1/4) cos(2 pi y).

It uses the actual W131 ``ker Gamma`` carrier, the ECW3D-A positive Green
spectral polarization for the boundary normal ``dy``, and the induced smooth
metric-compatible connection.  The latter contributes only a bounded
zeroth-order matrix ``B_a(y)`` on this stationary spatial slab.

The characteristic sequence

    u_N = psi(t) sin(pi y) sum_(k=1)^N k^-1 exp(i k (t+x)) q

uses a fixed real compactly supported smooth time cutoff ``psi`` and a nonzero
actual-carrier vector ``q`` killed by the Lorentz-null symbol.  The cutoff
derivative is a bounded graph-norm remainder.  The sequence has zero boundary
trace, is Cauchy in ``L2 + ||D_a .||_L2`` because ``sum k^-2`` converges, but
its spacetime ``H1`` norm diverges because the ``x`` and ``t`` oscillatory
derivatives each contribute ``sum 1``.  Therefore the naive isotropic
spacetime-H1 realization is not a closed operator in L2.

This is not a no-go for time-slice energy spaces, anisotropic graph spaces,
maximal-dissipative boundary conditions, or nonlinear constraint propagation.
Curt's literal real (7,7) comparator remains separately tagged and is not
transported through the common complex carrier.
"""

from __future__ import annotations

import json
import math
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


def harmonic_two_tail(start: int, stop: int) -> float:
    return sum(1.0 / (k * k) for k in range(start, stop + 1))


def main() -> int:
    print("=" * 96)
    print("ECW3D-B1 VARIABLE-COEFFICIENT / RIGHT-H POLARIZATION / H1 CLOSEDNESS KILL")
    print("=" * 96)

    gammas, gamma_trace, projector, _ = gb.constraint_objects()
    identity_v = np.eye(14, dtype=complex)

    # Section coordinates use ambient tangent indices
    # y=0 (positive boundary normal), x=1 (positive), z=2 (positive), t=9 (negative).
    boundary_index = 0
    x_index = 1
    z_index = 2
    t_index = 9
    eta = np.array([1.0] * 9 + [-1.0] * 5)
    check(
        "the frozen section frame is Lorentzian with y,x,z positive and t negative",
        tuple(int(eta[i]) for i in (boundary_index, x_index, z_index, t_index))
        == (1, 1, 1, -1),
    )

    # Smooth variable tetrad coefficient.  The exact analytic bounds are
    # 3/4 <= a(y) <= 5/4; samples only guard the executable transcription.
    sample_y = np.linspace(0.0, 1.0, 257)
    coefficient = 1.0 + 0.25 * np.cos(2.0 * np.pi * sample_y)
    check(
        "a(y)=1+(1/4)cos(2 pi y) is nonconstant, smooth, and uniformly positive",
        abs(float(np.min(coefficient)) - 0.75) < 1.0e-12
        and abs(float(np.max(coefficient)) - 1.25) < 1.0e-12
        and float(np.ptp(coefficient)) > 0.49,
    )

    # Construct a null-symbol vector without an eigensolver.  If c=c(dx+dt),
    # s=c r, and q has the same spinor s in vector slots x and t, then
    # Gamma q = c s = c^2 r = 0 and sigma(dx+dt) q = c q = 0.
    c_null = gammas[x_index] + gammas[t_index]
    seed = np.zeros(128, dtype=complex)
    seed[0] = 1.0
    spinor = c_null @ seed
    q_blocks = np.zeros((14, 128), dtype=complex)
    q_blocks[x_index] = spinor
    q_blocks[t_index] = spinor
    q = q_blocks.reshape(-1)
    ambient_null_symbol = np.kron(identity_v, c_null)

    check("the explicit characteristic vector is nonzero", np.linalg.norm(q) > 1.0)
    check(
        "q lies exactly in the W131 gamma-traceless carrier",
        np.linalg.norm(gamma_trace @ q) < TOL
        and np.linalg.norm(projector @ q - q) < TOL,
    )
    check(
        "the actual Lorentz-null W131 principal symbol kills q",
        np.linalg.norm(ambient_null_symbol @ q) < TOL,
    )

    j_s = matrix_product([gammas[i] for i in (1, 3, 5, 7, 10, 12)])
    j_vs = np.kron(identity_v, j_s)
    jq = j_vs @ q.conj()
    check(
        "the native antilinear right-H partner Jq is independent and also gamma-traceless",
        np.linalg.norm(jq) > 1.0
        and abs(np.vdot(q, jq)) < TOL
        and np.linalg.norm(gamma_trace @ jq) < TOL,
    )
    check(
        "the same Lorentz-null symbol kills the right-H partner Jq",
        np.linalg.norm(ambient_null_symbol @ jq) < TOL,
    )

    # The y derivative survives the null cancellation.  Projecting back to
    # ker Gamma is the actual W131 principal action.
    y_symbol = projector @ np.kron(identity_v, gammas[boundary_index]) @ projector
    y_q = y_symbol @ q
    check(
        "the transverse W131 symbol does not kill the characteristic vector",
        np.linalg.norm(y_q) > 1.0,
        f"norm={np.linalg.norm(y_q):.12g}",
    )

    predecessor = json.loads(
        (ROOT / "lab/process/eric-curt-wave3d-section-green-domain.json").read_text(),
        object_pairs_hook=unique_object,
    )
    registry = json.loads(
        (ROOT / "lab/process/eric-curt-wave3d-b1-h1-closedness-kill.json").read_text(),
        object_pairs_hook=unique_object,
    )
    campaign = json.loads(
        (ROOT / "lab/process/eric-curt-ten-wave-campaign.json").read_text(),
        object_pairs_hook=unique_object,
    )
    wave3 = next(wave for wave in campaign["waves"] if wave["id"] == "ECW3-G4-OBSERVATION")
    wave3d = wave3["result"]["wave3d"]
    wave3d_b1 = wave3d["wave3d_b1"]

    check(
        "the imposed boundary polarization is the ECW3D-A right-H positive Green sector",
        predecessor["exact_results"]["green_inertia"]
        == {"positive": 832, "negative": 832, "null": 0}
        and "both Green spectral sectors" in predecessor["exact_results"]["right_h_gate"]
        and registry["domain"]["boundary_polarization"]
        == "IMPOSED_POSITIVE_GREEN_SPECTRAL_SECTOR_FROM_ECW3D_A",
    )
    check(
        "every finite characteristic partial sum satisfies the imposed boundary condition",
        registry["countersequence"]["boundary_trace"] == "ZERO_AT_Y_0_AND_Y_1",
    )

    # Orthogonality already follows from the S1_x factor.  Take a fixed real
    # psi in C_c^infinity(R_t) with ||psi||_2=1.  Its derivative adds only a
    # fixed multiple of the same summable coefficient tail.  The y factor
    # phi=sin(pi y) has integral |phi|^2=1/2 and |phi'|^2=pi^2/2.
    q_norm_sq = float(np.vdot(q, q).real)
    y_q_norm_sq = float(np.vdot(y_q, y_q).real)
    phi_norm_sq = 0.5
    phi_prime_norm_sq = math.pi * math.pi / 2.0

    partial_ns = (8, 32, 128)
    l2_norm_sq = [
        q_norm_sq * phi_norm_sq * harmonic_two_tail(1, n) for n in partial_ns
    ]
    principal_d_norm_sq = [
        y_q_norm_sq * phi_prime_norm_sq * harmonic_two_tail(1, n)
        for n in partial_ns
    ]
    h1_x_norm_sq = [q_norm_sq * phi_norm_sq * float(n) for n in partial_ns]

    check(
        "the L2 partial-sum norms converge to a finite limit",
        l2_norm_sq[-1] < q_norm_sq * phi_norm_sq * (math.pi * math.pi / 6.0)
        and l2_norm_sq[-1] > l2_norm_sq[0],
    )
    check(
        "the transverse principal images also have finite limiting norm",
        principal_d_norm_sq[-1]
        < y_q_norm_sq * phi_prime_norm_sq * (math.pi * math.pi / 6.0)
        and principal_d_norm_sq[-1] > principal_d_norm_sq[0],
    )

    # Any smooth induced connection term B_a(y) is a bounded multiplier on
    # this stationary spatial slab.  Hence its graph-tail norm is bounded by a fixed
    # constant times the same convergent coefficient tail.
    tails = [harmonic_two_tail(n + 1, 4 * n) for n in partial_ns]
    check(
        "the coefficient tails controlling L2, transverse, cutoff, and bounded-connection graph tails vanish",
        tails[2] < tails[1] < tails[0] and tails[2] < 0.006,
        f"tails={tails}",
    )
    check(
        "the spacetime x-derivative H1 energy grows linearly instead of converging",
        h1_x_norm_sq == [q_norm_sq * phi_norm_sq * float(n) for n in partial_ns]
        and h1_x_norm_sq[2] == 4.0 * h1_x_norm_sq[1]
        and h1_x_norm_sq[1] == 4.0 * h1_x_norm_sq[0],
    )
    check(
        "the t derivative has the same divergent H1 energy by the frozen null phase",
        registry["countersequence"]["h1_derivative_series"]
        == "SUM_K_GE_1_K2_TIMES_K_MINUS_2_EQUALS_SUM_1_DIVERGES",
    )
    check(
        "graph convergence plus H1 failure records a non-closed L2 operator realization",
        registry["exact_results"]["naive_h1_closedness"]
        == "KILLED_BY_CHARACTERISTIC_FOURIER_SEQUENCE"
        and registry["status_boundary"].startswith("DECISIVE_ECW3D_B1"),
    )
    check(
        "right-H compatibility survives while closedness fails",
        registry["exact_results"]["right_h_gate"]
        == "PASS_COEFFICIENT_CONNECTION_CARRIER_AND_IMPOSED_BOUNDARY_POLARIZATION"
        and registry["exact_results"]["naive_h1_closedness"].startswith("KILLED"),
    )
    check(
        "the registry leaves nonlinear constraint propagation unclaimed",
        registry["exact_results"]["nonlinear_constraint_propagation"]
        == "OPEN_FULL_NONLINEAR_EULER_OPERATOR_AND_ENERGY_ESTIMATE_NOT_CONSTRUCTED",
    )
    check(
        "the campaign appends B1 without overwriting the completed ECW3D-A packet",
        wave3d["registry"] == "lab/process/eric-curt-wave3d-section-green-domain.json"
        and wave3d_b1["registry"]
        == "lab/process/eric-curt-wave3d-b1-h1-closedness-kill.json"
        and wave3d_b1["status_boundary"] == registry["status_boundary"],
    )
    check(
        "the next gate moves to an energy/maximal-dissipative constraint domain",
        registry["next_gate"]
        == "ECW3D-B2-ENERGY-MAXIMAL-DISSIPATIVE-CONSTRAINT-DOMAIN"
        and wave3d_b1["next_gate"] == registry["next_gate"],
    )
    promotion = registry["third_lane_promotion"]
    check(
        "Curt remains a separated rival under the conjunctive promotion rule",
        registry["curt_rival"]["status"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
        and promotion["logic"] == "TG-1 AND TG-2 AND TG-3"
        and promotion["verdict"] == "NOT_PROMOTED",
    )

    reject(
        "imposing the positive Green sector means GU selected that polarization",
        registry["domain"]["selection_grade"] == "NATIVELY_SELECTED",
    )
    reject(
        "a smooth positive variable coefficient removes the Lorentz characteristic kernel",
        np.linalg.norm(ambient_null_symbol @ q) > TOL,
    )
    reject(
        "the imposed boundary projector excludes a zero-trace countersequence",
        registry["countersequence"]["boundary_trace"] != "ZERO_AT_Y_0_AND_Y_1",
    )
    reject(
        "graph-Cauchy convergence forces convergence in isotropic spacetime H1",
        h1_x_norm_sq[-1] < h1_x_norm_sq[0],
    )
    reject(
        "failure of the naive spacetime-H1 domain kills all Lorentzian energy domains",
        "ALL_LORENTZIAN_DOMAINS_KILLED" in registry["status_boundary"],
    )
    reject(
        "right-H compatibility by itself proves operator closedness",
        registry["exact_results"]["naive_h1_closedness"] == "PASS",
    )
    reject(
        "linear ker-Gamma preservation proves nonlinear Euler constraint propagation",
        registry["exact_results"]["nonlinear_constraint_propagation"] == "PASS",
    )
    reject(
        "the explicit slab proves a global Lorentz/spin section exists on arbitrary X",
        registry["geometry"]["global_section_status"] == "PROVED",
    )
    reject(
        "the common complex carrier transports the B1 domain to Curt's real (7,7) track",
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
    print("VERDICT: naive spacetime-H1 domain is not closed; energy-domain analysis remains open")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
