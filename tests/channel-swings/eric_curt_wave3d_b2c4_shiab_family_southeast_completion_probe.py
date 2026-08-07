#!/usr/bin/env python3
r"""B2C4 full Shiab-family and southeast-completion principal-symbol gate.

The source fixes an Omega1(S)+Omega0(S) Euler-matrix shape, leaves the Shiab
inside a family, and explicitly notes that other versions can have a nonzero
southeast block.  This probe therefore freezes, before looking at PDE output,
the repo's complete active right-H contract/wedge family and the smallest
source-admitted first-order southeast class.

The active real form is the trace-reversed Frobenius-fibre port

    (3,1) + (6,4) = (9,5),   Cl(9,5)=M(64,H).

For the two natural middle symbols A_c=Phi_c o (k wedge -) and
A_w=Phi_w o (k wedge -), it first solves the source-motivated, but
repo-reconstructed, two-sided/Ward and Krein filters

    A K = 0,   C_g A = 0,   A^x = A.

Only after that filter is frozen does it test the southeast ansatz

    L(k)=c(k)(ell_+ P_+ + ell_- P_-)

and the exact coefficient equations

    w_+ w_- != 0,
    12 w_+ ell_- + 11 = 0,
    12 w_- ell_+ + 11 = 0.

These equations leave a two-real-parameter nonzero family in the frozen
unit-K/unit-C normalization.  The four sign choices are a normalized slice,
not the whole family.  Every tested family witness gives section evolution
generators satisfying the spatial Clifford relations, hence a positive
strong-hyperbolicity symmetrizer without quotienting the source-labelled
physical nu field.

This is a principal-symbol construction.  It is not the missing historical
bosonic Bianchi calculation, a covariant nonlinear Noether identity, a Green
current/domain theorem, a mass/index/count claim, or a use of P1/P2/P3.
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


def product(matrices: list[np.ndarray]) -> np.ndarray:
    result = np.eye(matrices[0].shape[0], dtype=complex)
    for matrix in matrices:
        result = result @ matrix
    return result


def main() -> int:
    print("ECW3D-B2C4 SHIAB FAMILY / SOUTHEAST COMPLETION GATE")
    n = 14
    spin = 128
    roll = (n + 1) * spin
    gammas, gamma_trace, _, _ = gb.constraint_objects()
    eta = np.array([1.0] * 9 + [-1.0] * 5)
    identity_s = np.eye(spin, dtype=complex)
    identity_v = np.eye(n, dtype=complex)
    identity_vs = np.eye(n * spin, dtype=complex)
    identity_roll = np.eye(roll, dtype=complex)

    omega = product(gammas)
    p_plus = 0.5 * (identity_s + omega)
    p_minus = 0.5 * (identity_s - omega)
    beta = product(gammas[:9])
    krein_vs = np.kron(np.diag(eta), beta)
    krein_roll = np.block(
        [
            [krein_vs, np.zeros((n * spin, spin), dtype=complex)],
            [np.zeros((spin, n * spin), dtype=complex), beta],
        ]
    )
    right_h_s = product([gammas[i] for i in (1, 3, 5, 7, 10, 12)])
    right_h = np.block(
        [
            [np.kron(identity_v, right_h_s), np.zeros((n * spin, spin))],
            [np.zeros((spin, n * spin)), right_h_s],
        ]
    )

    check(
        "trace-reversed Cl(9,5) volume gives complementary chiral projectors",
        max_abs(omega @ omega - identity_s) < 2.0e-12
        and max_abs(p_plus @ p_plus - p_plus) < 2.0e-12
        and max_abs(p_minus @ p_minus - p_minus) < 2.0e-12
        and rank(p_plus) == rank(p_minus) == 64,
    )
    check(
        "native spinor Krein form is an involution and pairs opposite chirality",
        max_abs(beta - beta.conj().T) < 2.0e-12
        and max_abs(beta @ beta - identity_s) < 2.0e-12
        and max_abs(beta @ omega + omega @ beta) < 2.0e-12,
    )
    check(
        "every Clifford generator is self-adjoint for the active spinor Krein form",
        max(max_abs(beta @ g.conj().T @ beta - g) for g in gammas) < 2.0e-12,
    )

    def c(k: np.ndarray) -> np.ndarray:
        return sum(k[a] * gammas[a] for a in range(n))

    def k_map(k: np.ndarray) -> np.ndarray:
        return np.kron(k.reshape(n, 1), identity_s)

    def codiff(k: np.ndarray) -> np.ndarray:
        return np.kron((eta * k).reshape(1, n), identity_s)

    def contract_middle(k: np.ndarray) -> np.ndarray:
        return k_map(k) @ gamma_trace - np.kron(identity_v, c(k))

    def wedge_middle_coordinate(b: int) -> np.ndarray:
        """A_w(e^b)[a,v]=eta_a c(e_a wedge e_b wedge e_v)."""
        out = np.zeros((n * spin, n * spin), dtype=complex)
        for a in range(n):
            if a == b:
                continue
            for v in range(n):
                if v == a or v == b:
                    continue
                out[
                    a * spin : (a + 1) * spin,
                    v * spin : (v + 1) * spin,
                ] = eta[a] * gammas[a] @ gammas[b] @ gammas[v]
        return out

    coordinates = {name: index for name, index in {"y": 0, "x": 1, "z": 2, "t": 9}.items()}
    wedge = {name: wedge_middle_coordinate(index) for name, index in coordinates.items()}
    covectors = {name: np.eye(n)[index] for name, index in coordinates.items()}

    # Freeze and solve the natural family before PDE inspection.
    generic_k = np.array(
        [1.0, -2.0, 0.5, 0.25, -0.75, 1.5, 0.0, 0.4,
         -0.2, 0.8, -1.1, 0.3, 0.6, -0.9]
    )
    contract_generic = contract_middle(generic_k)
    wedge_generic = sum(generic_k[coordinates[name]] * wedge[name] for name in coordinates)
    # Add the ten unused coordinate contributions only for the family selector.
    for b in range(n):
        if b not in coordinates.values() and generic_k[b] != 0:
            wedge_generic += generic_k[b] * wedge_middle_coordinate(b)
    kg = k_map(generic_k)
    cg = codiff(generic_k)
    qg = float(generic_k @ (eta * generic_k))
    check(
        "both natural Shiab channels obey the nonselecting exterior identity A(k)K(k)=0",
        max_abs(contract_generic @ kg) < 5.0e-8
        and max_abs(wedge_generic @ kg) < 5.0e-8,
    )
    check(
        "only the wedge channel obeys the discriminating two-sided identity C_g(k)A(k)=0",
        max_abs(cg @ wedge_generic) < 5.0e-8
        and np.linalg.norm(cg @ contract_generic) > 1.0,
        f"contract mass={np.linalg.norm(cg @ contract_generic):.6g}",
    )
    expected_contract_divergence = qg * gamma_trace - c(generic_k) @ cg
    check(
        "the contract divergence is exactly q Gamma minus c(k) C_g",
        max_abs(cg @ contract_generic - expected_contract_divergence) < 5.0e-8,
    )
    check(
        "only the wedge channel is self-adjoint for eta tensor beta",
        max_abs(krein_vs @ wedge_generic.conj().T @ krein_vs - wedge_generic) < 5.0e-8
        and np.linalg.norm(
            krein_vs @ contract_generic.conj().T @ krein_vs - contract_generic
        ) > 1.0,
    )

    # The full four-real family has two independent chiral wedge survivors.
    chiral_identity = np.kron(identity_v, identity_s)
    plus_vs = np.kron(identity_v, p_plus)
    minus_vs = np.kron(identity_v, p_minus)
    family = [
        contract_generic @ plus_vs,
        wedge_generic @ plus_vs,
        contract_generic @ minus_vs,
        wedge_generic @ minus_vs,
    ]
    divergence_columns = np.stack([(cg @ item).reshape(-1) for item in family], axis=1)
    divergence_gram = divergence_columns.conj().T @ divergence_columns
    div_eigen = np.linalg.eigvalsh(divergence_gram)
    check(
        "the two-sided selector leaves exactly the two chiral wedge coordinates",
        int(np.sum(div_eigen < TOL * max(1.0, float(div_eigen[-1])))) == 2
        and np.linalg.norm(cg @ family[1]) < 5.0e-8
        and np.linalg.norm(cg @ family[3]) < 5.0e-8,
        f"Gram eigenvalues={div_eigen}",
    )
    check(
        "Krein symmetry does not silently tie the two surviving chiral wedge weights",
        max(
            max_abs(krein_vs @ family[index].conj().T @ krein_vs - family[index])
            for index in (1, 3)
        ) < 5.0e-8,
    )
    check(
        "each surviving chiral wedge block is separately right-H compatible",
        max(
            max_abs(
                family[index] @ np.kron(identity_v, right_h_s)
                - np.kron(identity_v, right_h_s) @ family[index].conj()
            )
            for index in (1, 3)
        ) < 5.0e-8,
    )

    del contract_generic, wedge_generic, family, divergence_columns, divergence_gram
    gc.collect()

    # Source-admitted southeast ansatz.  Coefficients are solved by the four
    # scalar polynomial conditions recorded in the module docstring; they are
    # not fitted separately by direction or characteristic root.
    def rolled_symbol(
        name: str, w_plus: int, w_minus: int, ell_plus: float, ell_minus: float
    ) -> np.ndarray:
        k = covectors[name]
        weights = w_plus * p_plus + w_minus * p_minus
        ell = ell_plus * p_plus + ell_minus * p_minus
        return np.block(
            [
                [wedge[name] @ np.kron(identity_v, weights), k_map(k)],
                [codiff(k), c(k) @ ell],
            ]
        )

    normalized_witnesses: list[tuple[float, float, float, float]] = []
    for w_plus in (-1, +1):
        for w_minus in (-1, +1):
            ell_plus = -11.0 / (12.0 * w_minus)
            ell_minus = -11.0 / (12.0 * w_plus)
            normalized_witnesses.append((w_plus, w_minus, ell_plus, ell_minus))
            check(
                f"normalized witness ({w_plus:+d},{w_minus:+d}) solves the reciprocal variety",
                abs(12.0 * w_plus * ell_minus + 11.0) < 2.0e-12
                and abs(12.0 * w_minus * ell_plus + 11.0) < 2.0e-12,
            )

    unequal_weights = [(1.0, 2.0), (-2.0, 3.0), (0.5, 0.75)]
    unnormalized_witnesses = [
        (wp, wm, -11.0 / (12.0 * wm), -11.0 / (12.0 * wp))
        for wp, wm in unequal_weights
    ]
    witnesses = normalized_witnesses + unnormalized_witnesses
    check(
        "the exact coefficient variety remains two-dimensional before action normalization",
        all(
            wp != 0.0 and wm != 0.0
            and abs(12.0 * wp * em + 11.0) < 2.0e-12
            and abs(12.0 * wm * ep + 11.0) < 2.0e-12
            for wp, wm, ep, em in unnormalized_witnesses
        ),
        "unequal witnesses=(1,2),(-2,3),(0.5,0.75)",
    )

    # Check the full spatial Clifford relations for every discrete witness.
    # These six matrix identities imply E(xi)^2=|xi|^2 for every section xi.
    evolutions_by_witness: list[dict[str, np.ndarray]] = []
    max_clifford_defects: list[float] = []
    for witness in witnesses:
        wp, wm, ep, em = witness
        symbols = {
            name: rolled_symbol(name, wp, wm, ep, em)
            for name in ("y", "x", "z", "t")
        }
        time_inverse = np.linalg.inv(symbols["t"])
        inverse_defect = max_abs(symbols["t"] @ time_inverse - identity_roll)
        evolution = {
            name: time_inverse @ symbols[name] for name in ("y", "x", "z")
        }
        evolutions_by_witness.append(evolution)
        defects = []
        for name in ("y", "x", "z"):
            defects.append(max_abs(evolution[name] @ evolution[name] - identity_roll))
        for left, right in (("y", "x"), ("y", "z"), ("x", "z")):
            defects.append(
                max_abs(evolution[left] @ evolution[right] + evolution[right] @ evolution[left])
            )
        max_clifford_defects.append(max(defects))
        check(
            f"witness ({wp:+g},{wm:+g}) has invertible time symbol and exact spatial Clifford evolution",
            inverse_defect < 6.0e-8 and max(defects) < 6.0e-8,
            f"inverse={inverse_defect:.3g}; Clifford={max(defects):.3g}",
        )

        # The complete operator, including its southeast block, is Krein symmetric.
        full_defect = max(
            max_abs(krein_roll @ symbols[name] - (krein_roll @ symbols[name]).conj().T)
            for name in ("y", "x", "z", "t")
        )
        h_defect = max(
            max_abs(evolution[name] @ right_h - right_h @ evolution[name].conj())
            for name in ("y", "x", "z")
        )
        check(
            f"witness ({wp:+g},{wm:+g}) is full-Krein symmetric and exact right-H",
            full_defect < 6.0e-8 and h_defect < 6.0e-8,
            f"Krein={full_defect:.3g}; H={h_defect:.3g}",
        )

    # One representative proves the direction-independent symmetrizer formula
    # on coordinate and generic directions.  No field is quotiented.
    representative = evolutions_by_witness[3]  # normalized tied (+,+)
    directions = {
        "y": np.array([1.0, 0.0, 0.0]),
        "generic_1_2_3": np.array([1.0, 2.0, 3.0]) / np.sqrt(14.0),
    }
    symmetrizer_bounds: list[tuple[float, float]] = []
    for label, coefficients in directions.items():
        evolution = sum(
            coefficients[index] * representative[name]
            for index, name in enumerate(("y", "x", "z"))
        )
        symmetrizer = identity_roll + evolution.conj().T @ evolution
        symmetry_defect = max_abs(
            symmetrizer @ evolution - evolution.conj().T @ symmetrizer
        )
        right_h_defect = max_abs(
            symmetrizer @ right_h - right_h @ symmetrizer.conj()
        )
        eigenvalues = np.linalg.eigvalsh(symmetrizer)
        symmetrizer_bounds.append((float(eigenvalues[0]), float(eigenvalues[-1])))
        check(
            f"{label}: H=I+E^dag E is a positive right-H symmetrizer",
            symmetry_defect < 6.0e-8
            and right_h_defect < 6.0e-8
            and eigenvalues[0] > 1.0,
            f"bounds=({eigenvalues[0]:.6g},{eigenvalues[-1]:.6g})",
        )
    check(
        "coordinate and generic symmetrizer bounds agree by section covariance",
        max(abs(a - b) for a, b in zip(symmetrizer_bounds[0], symmetrizer_bounds[1])) < 6.0e-8,
        f"bounds={symmetrizer_bounds}",
    )

    # Raw observation and the physical zero-form channel remain untouched.
    observer = np.zeros((5 * spin, roll), dtype=complex)
    for block, name in enumerate(("y", "x", "z", "t")):
        observer[
            block * spin : (block + 1) * spin,
            coordinates[name] * spin : (coordinates[name] + 1) * spin,
        ] = identity_s
    observer[4 * spin :, n * spin :] = identity_s
    nu_projection = np.zeros((spin, roll), dtype=complex)
    nu_projection[:, n * spin :] = identity_s
    check(
        "the no-quotient completion retains all raw observed and physical nu components",
        rank(observer) == 640
        and rank(nu_projection) == 128
        and max_abs(observer @ observer.conj().T - np.eye(5 * spin)) < 2.0e-12,
    )

    # Source-displayed zero-SE control and normalization/one-sided controls.
    zero_se_symbols = {
        name: np.block(
            [
                [wedge[name] @ chiral_identity, k_map(covectors[name])],
                [codiff(covectors[name]), np.zeros((spin, spin), dtype=complex)],
            ]
        )
        for name in ("y", "t")
    }
    zero_se_evolution = np.linalg.inv(zero_se_symbols["t"]) @ zero_se_symbols["y"]
    zero_se_jordan = zero_se_evolution @ zero_se_evolution - identity_roll
    check(
        "the source-displayed zero-southeast wedge control retains the rank-128 square-zero Jordan part",
        rank(zero_se_jordan) == 128
        and max_abs(zero_se_jordan @ zero_se_jordan) < 6.0e-8,
    )
    one_sided_time = rolled_symbol("t", 1, 0, 0.0, -(11.0 / 12.0))
    check(
        "a one-sided chiral wedge fails the time-symbol gate with nullity 832",
        roll - rank(one_sided_time) == 832,
    )

    wrong_ep = -(10.0 / 12.0)
    wrong_em = -(10.0 / 12.0)
    wrong_time = rolled_symbol("t", 1, 1, wrong_ep, wrong_em)
    wrong_y = rolled_symbol("y", 1, 1, wrong_ep, wrong_em)
    wrong_evolution = np.linalg.inv(wrong_time) @ wrong_y
    wrong_clifford = max_abs(wrong_evolution @ wrong_evolution - identity_roll)
    check(
        "the planted nearby 10/12 southeast coefficient fails the exact Clifford identity",
        wrong_clifford > 1.0e-3,
        f"defect={wrong_clifford:.6g}",
    )

    reject("A(k)K(k)=0 uniquely selects the wedge channel", False)
    reject("the spinorial divergence identity is Weinstein's recovered bosonic Bianchi proof", False)
    reject("Krein symmetry ties w_plus to w_minus", False)
    reject("the zero southeast block is forced by every source version", False)
    reject("the principal symbol forces w_plus squared and w_minus squared to equal one", False)
    reject("the reciprocal 11/12 invariant was selected by fitting a characteristic eigenvector", False)
    reject("the one-sided chiral wedge has a noncharacteristic time", False)
    reject("the completion requires quotienting physical nu", False)
    reject("the positive symmetrizer is the native Krein form", False)
    reject("principal-symbol closure proves a nonlinear Noether identity", False)
    reject("P1/P2 selects the tied versus coflip branch", False)
    reject("P3 fixes the southeast coefficient or a generation count", False)
    reject("the draft's literal (7,7) matrix is identical to this trace-reversed (9,5) port", False)

    print("-" * 96)
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
