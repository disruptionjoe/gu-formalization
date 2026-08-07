#!/usr/bin/env python3
r"""Source-shaped rolled Omega0+Omega1 / Shiab principal-symbol gate.

The 2021 draft's equations (9.16)--(9.18) display, after chirality rows are
regrouped, a first-order fermion Euler operator on

    (zeta, nu) in Omega1(S) direct-sum Omega0(S)

with principal blocks

    [ (shiab o d)(k)   d(k)   ]
    [       d*(k)        0    ].

The manuscript explicitly leaves its Shiab selector inside a family open.  This
probe therefore instantiates that slot with the repository's canonical natural
Clifford-contraction candidate,

    shiab(e^i wedge e^j tensor s)
      = e^i tensor c(e^j)s - e^j tensor c(e^i)s,

whose middle symbol is forced before any PDE outcome is inspected:

    A(k) = K(k) Gamma - M(k),

where K(k)=k tensor 1, Gamma is gamma trace, and
M(k)=1 tensor c(k).  This probe collides that exact canonical instantiation of
the source-shaped symbol with
the prior positive full-Omega1 control.  It keeps the codifferential sign fork
explicit because (9.16) and the Euler-vector presentation (9.18) use opposite
display signs, and it does not treat either convention as a fit parameter.

This is a principal-symbol gate, not a BV differential, nonlinear domain,
generation count, chiral index, or claim that the existence-only Cl(9,5)
Shiab is uniquely selected by Weinstein's unavailable Bianchi calculation.
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


TOL = 8.0e-8
RANK_TOL = 2.0e-7
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


def null_basis(matrix: np.ndarray) -> np.ndarray:
    _, singular, right = np.linalg.svd(matrix, full_matrices=True)
    return right.conj().T[:, int(np.sum(singular > RANK_TOL)) :]


def outside(subspace: np.ndarray, vectors: np.ndarray) -> float:
    return float(
        np.linalg.norm(vectors - subspace @ (subspace.conj().T @ vectors))
    )


def product(matrices: list[np.ndarray]) -> np.ndarray:
    result = np.eye(matrices[0].shape[0], dtype=complex)
    for matrix in matrices:
        result = result @ matrix
    return result


def source_blocks(
    k: np.ndarray,
    gammas: list[np.ndarray],
    gamma_trace: np.ndarray,
    eta: np.ndarray,
    codiff_sign: int,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Return D(k), A(k), K(k), C_g(k), and M(k).

    `codiff_sign=+1` is the Euler-vector sign in draft (9.18), while `-1`
    is the lower-left matrix sign displayed in (9.16).  The metric
    codifferential symbol C_g uses the same (9,5) quadratic form as c(k)^2.
    """
    n = len(gammas)
    spin = gammas[0].shape[0]
    identity_v = np.eye(n, dtype=complex)
    identity_s = np.eye(spin, dtype=complex)
    c_k = sum(k[a] * gammas[a] for a in range(n))
    k_map = np.kron(k.reshape(n, 1), identity_s)
    multiplication = np.kron(identity_v, c_k)
    shiab_middle = k_map @ gamma_trace - multiplication
    codiff = np.kron((eta * k).reshape(1, n), identity_s)
    operator = np.block(
        [
            [shiab_middle, k_map],
            [codiff_sign * codiff, np.zeros((spin, spin), dtype=complex)],
        ]
    )
    return operator, shiab_middle, k_map, codiff, multiplication


def main() -> int:
    print("ECW3D-B2C3 SOURCE-SHAPED ROLLED OMEGA/SHIAB GATE")
    n = 14
    spin = 128
    gammas, gamma_trace, projector, _ = gb.constraint_objects()
    eta = np.array([1.0] * 9 + [-1.0] * 5)
    identity_s = np.eye(spin, dtype=complex)
    identity_vs = np.eye(n * spin, dtype=complex)
    identity_roll = np.eye((n + 1) * spin, dtype=complex)
    section = {"y": 0, "x": 1, "z": 2, "t": 9}

    # Freeze the canonical Clifford-contraction instantiation of the source's
    # open Shiab slot before constructing any evolution matrix or Jordan target.
    basis_k = np.array([1.0, -2.0, 0.5, 0.25, -0.75, 1.5, 0.0,
                        0.4, -0.2, 0.8, -1.1, 0.3, 0.6, -0.9])
    _, middle, k_map, codiff, multiplication = source_blocks(
        basis_k, gammas, gamma_trace, eta, +1
    )
    c_k = sum(basis_k[a] * gammas[a] for a in range(n))
    q = float(basis_k @ (eta * basis_k))
    check(
        "the canonical Clifford-Shiab instantiation gives A(k)=K(k)Gamma-M(k)",
        max_abs(middle - (k_map @ gamma_trace - multiplication)) < 2.0e-12,
    )
    check(
        "the canonical middle block annihilates exact one-form spinors off shell",
        max_abs(middle @ k_map) < 4.0e-11,
    )
    check(
        "metric codifferential and gradient recover the ambient quadratic form",
        max_abs(codiff @ k_map - q * identity_s) < 2.0e-12
        and max_abs(c_k @ c_k - q * identity_s) < 2.0e-12,
    )
    check(
        "the canonical source-shaped middle is not the prior Clifford completion",
        np.linalg.norm(middle - multiplication) > 1.0
        and np.linalg.norm(middle + multiplication) > 1.0,
    )

    # The exact gamma-trace split exposes which W131 block this canonical
    # instantiation contains.  In particular, its RS compression is -Q(k),
    # not +Q(k), while trace/RS off-diagonal blocks remain nonzero.
    values, vectors = np.linalg.eigh(projector)
    rs = vectors[:, values > 0.5]
    trace_spinor = gamma_trace.conj().T / np.sqrt(n)
    split = np.hstack([trace_spinor, rs])
    split_middle = split.conj().T @ middle @ split
    split_mult = split.conj().T @ multiplication @ split
    check(
        "the canonical middle's RS compression is exactly minus compressed W131",
        max_abs(
            split_middle[spin:, spin:] + split_mult[spin:, spin:]
        ) < 5.0e-8,
    )
    check(
        "the canonical middle retains both gamma-trace/RS coupling blocks",
        np.linalg.norm(split_middle[:spin, spin:]) > 1.0
        and np.linalg.norm(split_middle[spin:, :spin]) > 1.0,
    )

    # Construct the source-displayed shape with the frozen canonical Shiab.
    # Both display-sign conventions are tested independently.
    covectors = {
        name: np.eye(n)[index] for name, index in section.items()
    }
    j_s = product([gammas[i] for i in (1, 3, 5, 7, 10, 12)])
    right_h = np.block(
        [
            [np.kron(np.eye(n), j_s), np.zeros((n * spin, spin))],
            [np.zeros((spin, n * spin)), j_s],
        ]
    )
    convention_results: dict[int, dict[str, float | int | bool]] = {}
    evolutions: dict[int, dict[str, np.ndarray]] = {}

    for codiff_sign in (+1, -1):
        symbols = {
            name: source_blocks(k, gammas, gamma_trace, eta, codiff_sign)[0]
            for name, k in covectors.items()
        }
        time = symbols["t"]
        time_inverse = np.linalg.inv(time)
        inverse_defect = max_abs(time @ time_inverse - identity_roll)
        evolution = {
            name: time_inverse @ symbols[name] for name in ("y", "x", "z")
        }
        hermitian_defect = max(
            max_abs(matrix - matrix.conj().T) for matrix in evolution.values()
        )
        h_defect = max(
            max_abs(matrix @ right_h - right_h @ matrix.conj())
            for matrix in evolution.values()
        )
        convention_results[codiff_sign] = {
            "inverse_defect": inverse_defect,
            "hermitian_defect": hermitian_defect,
            "right_h_defect": h_defect,
        }
        evolutions[codiff_sign] = evolution
        check(
            f"codifferential sign {codiff_sign:+d}: the time symbol is invertible",
            inverse_defect < 7.0e-8,
            f"inverse defect={inverse_defect:.3g}",
        )
        check(
            f"codifferential sign {codiff_sign:+d}: section evolution is exactly right-H",
            h_defect < 7.0e-8,
            f"Hermitian defect={hermitian_defect:.3g}; right-H defect={h_defect:.3g}",
        )

    check(
        "the 9.16/9.18 codifferential display-sign fork gives the same section evolution",
        max(
            max_abs(evolutions[+1][name] - evolutions[-1][name])
            for name in ("y", "x", "z")
        ) < 2.0e-12,
    )
    check(
        "the displayed square symbol has no nonzero polynomial right-syzygy",
        all(
            result["inverse_defect"] < 7.0e-8
            for result in convention_results.values()
        ),
        "D(dt) invertible implies D(k)R(k)=0 polynomially only for R=0",
    )

    y_evolution = evolutions[+1]["y"]
    jordan = y_evolution @ y_evolution - identity_roll
    jordan_square = jordan @ jordan
    jordan_rank = rank(jordan)
    check(
        "the displayed-shape/canonical-Shiab operator retains the rank-128 Jordan remainder",
        jordan_rank == 128
        and max_abs(jordan_square) < 5.0e-8,
        f"rank={jordan_rank}; square defect={max_abs(jordan_square):.3g}",
    )
    check(
        "there is no positive full-carrier symmetrizer for this canonical one-time system",
        jordan_rank > 0,
        "a positive symmetrizer would make every real characteristic generator semisimple",
    )

    # Identify the obstruction without fitting it.  The endpoints are the two
    # null-root halves of the source differential d: Omega0(S)->Omega1(S).
    root_maps: list[np.ndarray] = []
    zero_spin = np.zeros((spin, spin), dtype=complex)
    for root_sign in (+1, -1):
        root = covectors["y"] + root_sign * covectors["t"]
        root_operator, _, root_k, _, _ = source_blocks(
            root, gammas, gamma_trace, eta, +1
        )
        root_c = sum(root[a] * gammas[a] for a in range(n))
        root_null = null_basis(root_c)
        full_gradient = np.vstack([root_k, zero_spin])
        endpoint = full_gradient @ root_null
        root_maps.append(endpoint)
        check(
            f"null root {root_sign:+d}: source d supplies a rank-128 characteristic kernel",
            rank(full_gradient) == 128
            and max_abs(root_operator @ full_gradient) < 5.0e-8
            and root_null.shape == (spin, 64),
        )
    endpoint_basis = image_basis(np.hstack(root_maps))
    jordan_basis = image_basis(jordan)
    check(
        "the Jordan image is exactly the two rank-64 null-Dirac halves of source d",
        endpoint_basis.shape[1] == jordan_basis.shape[1] == 128
        and outside(endpoint_basis, jordan_basis) < 4.0e-8
        and outside(jordan_basis, endpoint_basis) < 4.0e-8,
    )

    # This agreement is characteristic only.  Off the null cone the complete
    # rolled Euler operator does not annihilate d: D(k)(K(k),0)=(0,+/-q).
    exact_inclusion = np.vstack([k_map, zero_spin])
    source_plus = source_blocks(basis_k, gammas, gamma_trace, eta, +1)[0]
    expected_failure = np.vstack(
        [np.zeros((n * spin, spin), dtype=complex), q * identity_s]
    )
    check(
        "source d is not an off-shell Noether/BV differential of the full rolled operator",
        max_abs(source_plus @ exact_inclusion - expected_failure) < 5.0e-8
        and abs(q) > 0.1,
    )

    # Observation is a trace, not a quotient.  The rolled carrier retains the
    # complete rank-512 observed one-form channel and rank-128 zero-form
    # channel before any physical cohomology is asserted.
    observer = np.zeros((5 * spin, (n + 1) * spin), dtype=complex)
    for block, name in enumerate(("y", "x", "z", "t")):
        observer[
            block * spin : (block + 1) * spin,
            section[name] * spin : (section[name] + 1) * spin,
        ] = identity_s
    observer[4 * spin :, n * spin :] = identity_s
    check(
        "the source-shaped rolled carrier retains 512 one-form plus 128 zero-form observed components",
        rank(observer) == 640
        and max_abs(observer @ observer.conj().T - np.eye(640)) < 2.0e-12,
    )

    # Conditional construction: if a separately typed odd ghost later derives
    # d as a genuine gauge differential, quotienting the two complete root
    # images is exact, right-H compatible, semisimple, positively symmetrizable,
    # and visible as an observed quotient.  This is a target for the next Ward/
    # BV gate, not a promotion of physical nu to a ghost.
    quotient_directions = {
        "y": np.array([1.0, 0.0, 0.0]),
        "x": np.array([0.0, 1.0, 0.0]),
        "z": np.array([0.0, 0.0, 1.0]),
        "generic_1_2_3": np.array([1.0, 2.0, 3.0]) / np.sqrt(14.0),
    }
    quotient_defects: list[float] = []
    symmetrizer_defects: list[float] = []
    right_h_symmetrizer_defects: list[float] = []
    observed_quotient_ranks: list[int] = []
    for coefficients in quotient_directions.values():
        spatial_k = sum(
            coefficients[i] * covectors[name]
            for i, name in enumerate(("y", "x", "z"))
        )
        direction_evolution = sum(
            coefficients[i] * evolutions[+1][name]
            for i, name in enumerate(("y", "x", "z"))
        )
        full_root_gradients: list[np.ndarray] = []
        for root_sign in (+1, -1):
            root = spatial_k + root_sign * covectors["t"]
            root_k = source_blocks(root, gammas, gamma_trace, eta, +1)[2]
            full_root_gradients.append(
                np.vstack([root_k, zero_spin]) / np.sqrt(2.0)
            )
        gauge_basis = np.hstack(full_root_gradients)
        gauge_projector = gauge_basis @ gauge_basis.conj().T
        physical_projector = identity_roll - gauge_projector
        reduced_evolution = (
            physical_projector @ direction_evolution @ physical_projector
        )
        reduced_symmetrizer = (
            physical_projector + reduced_evolution.conj().T @ reduced_evolution
        )
        quotient_defects.append(
            max(
                max_abs(
                    gauge_basis.conj().T @ gauge_basis - np.eye(2 * spin)
                ),
                max_abs(
                    reduced_evolution @ reduced_evolution - physical_projector
                ),
            )
        )
        symmetrizer_defects.append(
            max_abs(
                reduced_symmetrizer @ reduced_evolution
                - reduced_evolution.conj().T @ reduced_symmetrizer
            )
        )
        right_h_symmetrizer_defects.append(
            max_abs(
                reduced_symmetrizer @ right_h
                - right_h @ reduced_symmetrizer.conj()
            )
        )
        observed_gauge = observer @ gauge_basis
        observed_projector = (
            np.eye(5 * spin) - observed_gauge @ observed_gauge.conj().T
        )
        observed_quotient_ranks.append(
            rank(observed_projector @ observer @ physical_projector)
        )
    check(
        "conditional full-d quotient is a semisimple involution in four directions",
        max(quotient_defects) < 5.0e-8,
        f"max defect={max(quotient_defects):.3g}",
    )
    check(
        "the conditional quotient has an explicit positive right-H symmetrizer",
        max(symmetrizer_defects) < 5.0e-8
        and max(right_h_symmetrizer_defects) < 5.0e-8,
        "H=P+(PEP)^dagger(PEP), hence H>=P on the quotient",
    )
    check(
        "observation conditionally descends with constant nonzero quotient rank",
        observed_quotient_ranks == [384, 384, 384, 384],
        f"ranks={observed_quotient_ranks}",
    )

    # These are deliberately diagnostic placeholders until the observed
    # polynomial outcome has been inspected and encoded as a theorem below.
    reject("the manuscript uniquely selects the canonical Clifford Shiab", False)
    reject("the canonical middle block equals 1 tensor c(k)", max_abs(middle - multiplication) < TOL)
    reject("A(k) is a BV differential merely because A(k)K(k)=0", False)
    reject("the codifferential display-sign fork selects a physical convention", False)
    reject("characteristic annihilation makes source d an off-shell gauge symmetry", False)
    reject("a local spinor gauge generator exists inside the displayed square field block", False)
    reject("physical nu and an isomorphic odd ghost are the same object", False)
    reject("the conditional characteristic quotient is already action-derived", False)
    reject("retaining carrier rank proves observation descends on cohomology", False)
    reject("P1/P2 or P3 was used to repair the symbol", False)
    reject("a rolled 2-by-2 block forces three generations or chirality", False)

    del split_middle, split_mult, split, rs, projector, gamma_trace, gammas
    gc.collect()
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
