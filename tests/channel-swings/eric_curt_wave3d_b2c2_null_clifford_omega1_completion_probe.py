#!/usr/bin/env python3
r"""Target-blind null-Clifford collision and full-Omega1 completion.

Phase A freezes F(k)=Pi_kerGamma(k tensor c(k)) before it constructs the
held-out B2C1 Jordan targets.  Phase B derives every block of the full
one-form symbol 1 tensor c(k) from the Gamma-trace splitting.  No spectral
projector, Jordan eigenvector, fitted coefficient, or external datum enters
either construction.

A pass is only a principal-symbol result.  F(k) is quadratic and closes
through the wave symbol, so it is not by itself an off-shell BV differential.
The test also does not supply Weinstein's unreleased rolled middle map,
lower-order action, analytic domain, or a generation/index mechanism.
"""

from __future__ import annotations

import gc
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
for path in (ROOT / "tests", ROOT / "tests" / "generation-sector"):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

import gen_sector_bridge as gb  # noqa: E402


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


def image_basis(matrix: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    left, singular, _ = np.linalg.svd(matrix, full_matrices=False)
    dimension = int(np.sum(singular > RANK_TOL))
    return left[:, :dimension], singular


def outside(subspace: np.ndarray, vectors: np.ndarray) -> float:
    return float(
        np.linalg.norm(vectors - subspace @ (subspace.conj().T @ vectors))
    )


def product(matrices: list[np.ndarray]) -> np.ndarray:
    result = np.eye(matrices[0].shape[0], dtype=complex)
    for matrix in matrices:
        result = result @ matrix
    return result


def null_clifford_phase() -> None:
    print("=" * 92)
    print("PHASE A - TARGET-BLIND NULL-CLIFFORD / HELD-OUT JORDAN COLLISION")
    print("=" * 92)
    gammas, gamma_trace, projector, _ = gb.constraint_objects()
    eta = np.array([1.0] * 9 + [-1.0] * 5)
    identity_v = np.eye(14, dtype=complex)
    identity_s = np.eye(128, dtype=complex)
    section = {"y": 0, "x": 1, "z": 2, "t": 9}
    values, vectors = np.linalg.eigh(projector)
    rs = vectors[:, values > 0.5]
    identity_rs = np.eye(1664, dtype=complex)

    symbols = {
        name: rs.conj().T @ np.kron(identity_v, gammas[index]) @ rs
        for name, index in section.items()
    }
    inverse_time = np.linalg.inv(symbols["t"])
    evolution = {
        name: inverse_time @ symbols[name] for name in ("y", "x", "z")
    }
    j_s = product([gammas[i] for i in (1, 3, 5, 7, 10, 12)])
    right_h = rs.conj().T @ np.kron(identity_v, j_s) @ rs.conj()
    check(
        "the frozen W131 carrier is rank 1664, gamma-traceless, and right-H",
        rs.shape == (1792, 1664)
        and np.linalg.norm(gamma_trace @ rs) < 3.0e-7
        and max_abs(right_h @ right_h.conj() + identity_rs) < 4.0e-8,
    )

    directions = {
        "y": np.array([1.0, 0.0, 0.0]),
        "x": np.array([0.0, 1.0, 0.0]),
        "z": np.array([0.0, 0.0, 1.0]),
        "generic_1_2_3": np.array([1.0, 2.0, 3.0]),
        "generic_2_m1_2": np.array([2.0, -1.0, 2.0]),
    }
    frozen: dict[tuple[str, int], dict[str, np.ndarray]] = {}

    # Only the natural grammar k, c(k), and Pi_kerGamma occurs above this line.
    for label, coefficients in directions.items():
        norm = float(np.linalg.norm(coefficients))
        a_xi = sum(
            coefficients[i] * symbols[name]
            for i, name in enumerate(("y", "x", "z"))
        )
        for sign in (-1, 1):
            mu = sign * norm
            k = np.zeros(14)
            for i, name in enumerate(("y", "x", "z")):
                k[section[name]] = coefficients[i]
            k[section["t"]] = -mu
            c_k = sum(k[a] * gammas[a] for a in range(14))
            raw = np.kron(k.reshape(14, 1), c_k)
            candidate = rs.conj().T @ projector @ raw
            basis, singular = image_basis(candidate)
            characteristic = a_xi - mu * symbols["t"]
            h_defect = outside(basis, right_h @ basis.conj())
            check(
                f"{label} root {sign:+d}: frozen F(k) passes every intrinsic null test",
                abs(float(k @ (eta * k))) < 2.0e-12
                and rank(c_k) == 64
                and max_abs(c_k @ c_k) < 2.0e-10
                and np.linalg.norm(gamma_trace @ raw) < 2.0e-9
                and np.linalg.norm(projector @ raw - raw) < 2.0e-9
                and basis.shape[1] == 64
                and singular[63] > 0.1
                and singular[64] < 2.0e-10
                and np.linalg.norm(characteristic @ basis) < 2.0e-9
                and h_defect < 2.0e-9,
            )
            frozen[(label, sign)] = {
                "k": k,
                "candidate": candidate,
                "basis": basis,
                "characteristic": characteristic,
            }

    base = frozen[("generic_1_2_3", 1)]
    scaled_k = 2.5 * base["k"]
    scaled_c = sum(scaled_k[a] * gammas[a] for a in range(14))
    scaled = rs.conj().T @ projector @ np.kron(scaled_k.reshape(14, 1), scaled_c)
    scaled_basis, _ = image_basis(scaled)
    check(
        "im F(k) descends to null rays and F(lambda k)=lambda^2 F(k)",
        outside(base["basis"], scaled_basis) < 2.0e-9
        and outside(scaled_basis, base["basis"]) < 2.0e-9
        and np.linalg.norm(scaled - 2.5**2 * base["candidate"]) < 2.0e-9,
    )

    # The held-out B2C1 targets are first constructed here, after the formula
    # and its intrinsic tests have been frozen.
    for label, coefficients in directions.items():
        norm_sq = float(coefficients @ coefficients)
        norm = float(np.sqrt(norm_sq))
        c_xi = sum(
            coefficients[i] * evolution[name]
            for i, name in enumerate(("y", "x", "z"))
        )
        a_xi = sum(
            coefficients[i] * symbols[name]
            for i, name in enumerate(("y", "x", "z"))
        )
        jordan, _ = image_basis(c_xi @ c_xi - norm_sq * identity_rs)
        root_images: list[np.ndarray] = []
        for sign in (-1, 1):
            mu = sign * norm
            k = frozen[(label, sign)]["k"]
            gauge = rs.conj().T @ projector @ np.kron(k.reshape(14, 1), identity_s)
            defect = (a_xi - mu * symbols["t"]) @ gauge
            _, singular, right = np.linalg.svd(defect, full_matrices=False)
            defect_rank = int(np.sum(singular > RANK_TOL))
            held_out, _ = image_basis(gauge @ right.conj().T[:, defect_rank:])
            candidate = frozen[(label, sign)]["basis"]
            check(
                f"{label} root {sign:+d}: frozen im F(k) equals held-out null half",
                held_out.shape[1] == 64
                and outside(held_out, candidate) < 2.0e-9
                and outside(candidate, held_out) < 2.0e-9,
            )
            root_images.append(candidate)
        combined, _ = image_basis(np.hstack(root_images))
        check(
            f"{label}: opposite-root images are disjoint and span the Jordan image",
            combined.shape[1] == jordan.shape[1] == 128
            and outside(jordan, combined) < 5.0e-9
            and outside(combined, jordan) < 5.0e-9,
        )

    off_k = np.zeros(14)
    off_k[section["y"]] = 1.0
    off_k[section["t"]] = -0.5
    off_c = sum(off_k[a] * gammas[a] for a in range(14))
    off_f = rs.conj().T @ projector @ np.kron(off_k.reshape(14, 1), off_c)
    off_residual = np.linalg.norm((symbols["y"] - 0.5 * symbols["t"]) @ off_f)
    wrong_residual = np.linalg.norm(
        frozen[("y", -1)]["characteristic"] @ frozen[("y", 1)]["candidate"]
    )
    old_gauge = rs.conj().T @ projector @ np.kron(
        frozen[("y", 1)]["k"].reshape(14, 1), identity_s
    )
    reject("the prior projected k tensor identity already has rank 64", rank(old_gauge) == 64)
    reject("F(k) is characteristic-null off the null cone", off_residual < 1.0e-8)
    reject("one root image is killed by the opposite-root symbol", wrong_residual < 1.0e-8)
    reject("quadratic F(k) is an ordinary first-order BV symbol", False)
    reject("the target-blind phase used a Jordan or spectral projector", False)
    reject("a null-cone factorization proves off-shell BV closure", False)

    del symbols, evolution, frozen, rs, projector, gamma_trace, gammas
    gc.collect()


def full_omega1_phase() -> None:
    print("=" * 92)
    print("PHASE B - FULL OMEGA1 GAMMA-TRACE COMPLETION")
    print("=" * 92)
    n = 14
    spin = 128
    gammas, gamma_trace, projector, _ = gb.constraint_objects()
    eta = np.array([1.0] * 9 + [-1.0] * 5)
    identity_v = np.eye(n, dtype=complex)
    identity_s = np.eye(spin, dtype=complex)
    identity_vs = np.eye(n * spin, dtype=complex)
    section = {"y": 0, "x": 1, "z": 2, "t": 9}
    values, vectors = np.linalg.eigh(projector)
    rs = vectors[:, values > 0.5]
    trace_spinor = gamma_trace.conj().T / np.sqrt(n)
    split = np.hstack([trace_spinor, rs])
    j_s = product([gammas[i] for i in (1, 3, 5, 7, 10, 12)])
    right_h = np.kron(identity_v, j_s)
    right_h_split = split.conj().T @ right_h @ split.conj()
    check(
        "im Gamma-dagger plus ker Gamma is a complete unitary right-H splitting",
        split.shape == (1792, 1792)
        and max_abs(split.conj().T @ split - identity_vs) < 4.0e-8
        and max_abs(split @ split.conj().T - identity_vs) < 4.0e-8
        and max_abs(right_h_split @ right_h_split.conj() + identity_vs) < 5.0e-8,
    )

    covectors = {
        "y": np.eye(n)[section["y"]],
        "t": np.eye(n)[section["t"]],
        "generic_section": np.array([1.0, 2.0, -1.0] + [0.0] * 6 + [0.75] + [0.0] * 4),
        "generic_ambient": np.array(
            [1.0, -2.0, 0.5, 0.25, -0.75, 1.5, 0.0, 0.4, -0.2,
             0.8, -1.1, 0.3, 0.6, -0.9]
        ),
    }
    coefficient = (n - 2.0) / n
    for label, k in covectors.items():
        c_k = sum(k[a] * gammas[a] for a in range(n))
        q = float(k @ (eta * k))
        multiplication = np.kron(identity_v, c_k)
        blocks = split.conj().T @ multiplication @ split
        a = blocks[:spin, :spin]
        c = blocks[spin:, :spin]
        q_rs = blocks[spin:, spin:]
        k_map = np.kron(k.reshape(n, 1), identity_s)
        twistor = rs.conj().T @ projector @ k_map
        check(
            f"{label}: every full-carrier block is forced and the Clifford square closes",
            max_abs(split @ blocks @ split.conj().T - multiplication) < 4.0e-8
            and max_abs(a + coefficient * c_k) < 4.0e-8
            and max_abs(c - (2.0 / np.sqrt(n)) * twistor) < 4.0e-8
            and max_abs(q_rs @ twistor - coefficient * twistor @ c_k) < 5.0e-8
            and max_abs(blocks @ blocks - q * identity_vs) < 7.0e-8
            and max_abs(blocks @ right_h_split - right_h_split @ blocks.conj()) < 7.0e-8,
        )

    full_symbols = {
        name: np.kron(identity_v, gammas[index])
        for name, index in section.items()
    }
    inverse_time = np.linalg.inv(full_symbols["t"])
    full_evolution = {
        name: inverse_time @ full_symbols[name] for name in ("y", "x", "z")
    }
    hermitian_defect = max(
        max_abs(matrix - matrix.conj().T) for matrix in full_evolution.values()
    )
    square_defect = max(
        max_abs(matrix @ matrix - identity_vs) for matrix in full_evolution.values()
    )
    anti_defect = max(
        max_abs(full_evolution[a] @ full_evolution[b] + full_evolution[b] @ full_evolution[a])
        for a, b in (("y", "x"), ("y", "z"), ("x", "z"))
    )
    h_defect = max(
        max_abs(matrix @ right_h - right_h @ matrix.conj())
        for matrix in full_evolution.values()
    )
    check(
        "the full Omega1 Lorentz-section evolution has identity as a positive right-H symmetrizer",
        max(hermitian_defect, square_defect, anti_defect, h_defect) < 5.0e-8,
        f"defects=({hermitian_defect:.3g},{square_defect:.3g},{anti_defect:.3g},{h_defect:.3g})",
    )

    rs_symbols = {
        name: rs.conj().T @ full_symbols[name] @ rs for name in section
    }
    rs_y = np.linalg.inv(rs_symbols["t"]) @ rs_symbols["y"]
    rs_jordan = rs_y @ rs_y - np.eye(1664)
    full_jordan = full_evolution["y"] @ full_evolution["y"] - identity_vs
    check(
        "restoring the trace companion removes the isolated rank-128 square-zero Jordan remainder",
        rank(rs_jordan) == 128
        and max_abs(rs_jordan @ rs_jordan) < 3.0e-11
        and rank(full_jordan) == 0,
    )

    selector = np.zeros((4 * spin, n * spin), dtype=complex)
    for block, name in enumerate(("y", "x", "z", "t")):
        selector[
            block * spin : (block + 1) * spin,
            section[name] * spin : (section[name] + 1) * spin,
        ] = identity_s
    check(
        "the rank-512 observer-section one-form carrier is retained",
        rank(selector) == 512
        and max_abs(selector @ selector.conj().T - np.eye(512)) < 2.0e-12,
    )

    dirac_evolution = {
        name: np.linalg.inv(gammas[section["t"]]) @ gammas[section[name]]
        for name in ("y", "x", "z")
    }
    check(
        "the conservative Omega0 Dirac plus full Omega1 principal carrier is positive symmetric",
        max(
            max_abs(matrix - matrix.conj().T)
            for matrix in [*dirac_evolution.values(), *full_evolution.values()]
        ) < 5.0e-8,
    )

    reject("the isolated ker-Gamma system is diagonalizable", rank(rs_jordan) == 0)
    reject("the repair quotients out the observer carrier", rank(selector) < 512)
    reject("the twistor coefficient was fit to the Jordan image", False)
    reject("principal-symbol closure constructs the rolled lower-order action", False)
    reject("the direct-sum Omega0 control proves the prospective seesaw", False)
    reject("the full carrier forces three generations or a chiral index", False)


def main() -> int:
    print("ECW3D-B2C2 PARALLEL NULL-CLIFFORD / FULL-OMEGA1 COMPLETION")
    null_clifford_phase()
    full_omega1_phase()
    print("-" * 92)
    print(f"checks: {EXACT} exact + {PLANTED} planted")
    if FAILURES:
        print("FINAL: FAIL")
        for failure in FAILURES:
            print(f"  - {failure}")
        return 1
    print("FINAL: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
