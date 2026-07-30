#!/usr/bin/env python3
"""S2 manifest/consistency certificate for support and carrier composition.

This probe continues the nine-block construction written in
``full20_chimeric_bv_first_write_probe.py``.  It computes two deliberately
separated objects:

1. the analytically derived generic complexified observer-irrep support
   manifest of the nine carrier blocks and three gauge blocks; and
2. the raw principal carrier composition ``D_c R_r``.

It does *not* identify ``D_c R_r`` with the action-derived native Noether
defect ``H_c R_r``.  That identification still requires the native
Krein/polarization/Green-domain packet.  It also does not infer a generation
count, a physical quotient, all-covector rank, exactness, or BV closure from
support.

The result reverses the preregistered support expectation: the linked carrier
formulas generically saturate all 136 allowed cells.  The edge lists are exact
analytic inputs checked here against the independent representation ledger;
this file does not independently derive them from all 20 observer projectors.
The information then moves from binary incidence to coefficient-family
on/off links and the three-equation principal carrier locus.
"""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from itertools import combinations
import os
import sys
from typing import Callable, Iterable

import numpy as np


HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))

import shiab_b5_krein_mirror_orbit_reduction as reduction  # noqa: E402
import shiab_b5_native_packet_contract as native_contract  # noqa: E402
import shiab_b5_observer_symbol_multiplicity_matrix as ledger  # noqa: E402


Cell = tuple[str, str]
FAILURES: list[str] = []
TOL = 2.0e-10


def check(label: str, condition: bool, detail: str = "") -> None:
    status = "PASS" if condition else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


def info(message: str) -> None:
    print(f"INFO: {message}")


def rejects(callable_: Callable[[], object]) -> bool:
    try:
        callable_()
    except (AssertionError, KeyError, TypeError, ValueError):
        return True
    return False


def sector(slot_name: str) -> str:
    if slot_name.startswith("S:"):
        return "S"
    if slot_name.startswith("imGamma:"):
        return "I"
    if slot_name.startswith("kerGamma:") or slot_name.startswith("X:"):
        return "R"
    raise ValueError(f"not an observer slot: {slot_name}")


def symbol_parts(
    source: ledger.HType, target: ledger.HType
) -> tuple[int, int]:
    """Return the independent base and Sym^2-fibre branching multiplicities."""
    base_part = int(
        source.d5_weight == target.d5_weight
        and target.left_dim in ledger.su2_vector_targets(source.left_dim)
        and target.right_dim in ledger.su2_vector_targets(source.right_dim)
    )
    fibre_part = int(
        source.left_dim == target.left_dim
        and source.right_dim == target.right_dim
    ) * ledger.vector_tensor_decomposition(source.d5_weight).get(
        target.d5_weight, 0
    )
    return base_part, fibre_part


def cell_parts(cell: Cell) -> tuple[int, int]:
    source, target = cell
    return symbol_parts(
        ledger.TYPES[ledger.SLOT_BY_NAME[source].h_type],
        ledger.TYPES[ledger.SLOT_BY_NAME[target].h_type],
    )


def cells_for_sector_pair(source_sector: str, target_sector: str) -> set[Cell]:
    return {
        cell
        for cell in reduction.nonzero_cells()
        if sector(cell[0]) == source_sector and sector(cell[1]) == target_sector
    }


def names_from_indices(edges: Iterable[tuple[int, int]]) -> set[Cell]:
    """Convert one-based ``target <- source`` ledger indices to cells."""
    return {
        (ledger.SLOTS[source - 1].name, ledger.SLOTS[target - 1].name)
        for target, source in edges
    }


# Exact primitive branching lists.  As below, pairs are one-based
# ``target <- source`` ledger indices.
C_BASE_INDEX_EDGES = (
    (1, 4), (2, 3), (3, 2), (4, 1),
)
C_FIBRE_INDEX_EDGES = (
    (1, 3), (2, 4), (3, 1), (4, 2),
)
T_BASE_INDEX_EDGES = (
    (9, 4), (10, 3), (11, 2), (12, 1),
    (13, 1), (14, 2), (17, 3), (18, 4),
)
T_FIBRE_INDEX_EDGES = (
    (9, 3), (10, 4), (11, 1), (12, 2),
    (15, 1), (16, 2), (19, 3), (20, 4),
)


# Exact branching of Q=P_R c(xi) P_R on observer slots 9--20.  These were
# derived independently from the product decomposition, not filled from the
# 40-cell R->R envelope.
Q_BASE_INDEX_EDGES = (
    (9, 12), (9, 13),
    (10, 11), (10, 14),
    (11, 10), (11, 17),
    (12, 9), (12, 18),
    (13, 9), (13, 18),
    (14, 10), (14, 17),
    (15, 20),
    (16, 19),
    (17, 11), (17, 14),
    (18, 12), (18, 13),
    (19, 16),
    (20, 15),
)

Q_FIBRE_INDEX_EDGES = (
    (9, 11), (9, 15),
    (10, 12), (10, 16),
    (11, 9), (11, 19),
    (12, 10), (12, 20),
    (13, 17),
    (14, 18),
    (15, 9), (15, 19),
    (16, 10), (16, 20),
    (17, 13),
    (18, 14),
    (19, 11), (19, 15),
    (20, 12), (20, 16),
)

Q_BASE_SUPPORT = names_from_indices(Q_BASE_INDEX_EDGES)
Q_FIBRE_SUPPORT = names_from_indices(Q_FIBRE_INDEX_EDGES)
Q_SUPPORT = Q_BASE_SUPPORT | Q_FIBRE_SUPPORT
C_BASE_SUPPORT = names_from_indices(C_BASE_INDEX_EDGES)
C_FIBRE_SUPPORT = names_from_indices(C_FIBRE_INDEX_EDGES)
T_BASE_SUPPORT = names_from_indices(T_BASE_INDEX_EDGES)
T_FIBRE_SUPPORT = names_from_indices(T_FIBRE_INDEX_EDGES)


def shifted_cells(
    cells: set[Cell],
    *,
    source_offset: int = 0,
    target_offset: int = 0,
) -> set[Cell]:
    index = {slot.name: position for position, slot in enumerate(ledger.SLOTS)}
    shifted: set[Cell] = set()
    for source, target in cells:
        source_index = index[source] + source_offset
        target_index = index[target] + target_offset
        if not 0 <= source_index < len(ledger.SLOTS):
            raise ValueError("source shift leaves the frozen slot ledger")
        if not 0 <= target_index < len(ledger.SLOTS):
            raise ValueError("target shift leaves the frozen slot ledger")
        shifted.add(
            (
                ledger.SLOTS[source_index].name,
                ledger.SLOTS[target_index].name,
            )
        )
    return shifted


# The exact Clifford reductions are
#
#   P_I M P_I = -(6/7) j c Gamma,  P_R M P_I = (1/7) T Gamma,
#   P_I M P_R = -2 j delta,        Q = P_R M P_R,
#
# in n=14, with delta=-contraction.  Hence the nine written blocks use four
# primitive symbol families.  Rows are targets; cells are (source,target).
BLOCK_PRIMITIVES = {
    "SS": "c",
    "SI": "cGamma",
    "SR": "delta",
    "IS": "jc",
    "II": "jcGamma",
    "IR": "jdelta",
    "RS": "T",
    "RI": "TGamma",
    "RR": "Q",
}

C_SUPPORT = C_BASE_SUPPORT | C_FIBRE_SUPPORT
T_SUPPORT = T_BASE_SUPPORT | T_FIBRE_SUPPORT
DELTA_SUPPORT = {reduction.transpose(cell) for cell in T_SUPPORT}

BLOCK_BASE_SUPPORT = {
    "SS": C_BASE_SUPPORT,
    "SI": shifted_cells(C_BASE_SUPPORT, source_offset=4),
    "SR": {reduction.transpose(cell) for cell in T_BASE_SUPPORT},
    "IS": shifted_cells(C_BASE_SUPPORT, target_offset=4),
    "II": shifted_cells(C_BASE_SUPPORT, source_offset=4, target_offset=4),
    "IR": shifted_cells(
        {reduction.transpose(cell) for cell in T_BASE_SUPPORT},
        target_offset=4,
    ),
    "RS": T_BASE_SUPPORT,
    "RI": shifted_cells(T_BASE_SUPPORT, source_offset=4),
    "RR": Q_BASE_SUPPORT,
}
BLOCK_FIBRE_SUPPORT = {
    "SS": C_FIBRE_SUPPORT,
    "SI": shifted_cells(C_FIBRE_SUPPORT, source_offset=4),
    "SR": {reduction.transpose(cell) for cell in T_FIBRE_SUPPORT},
    "IS": shifted_cells(C_FIBRE_SUPPORT, target_offset=4),
    "II": shifted_cells(C_FIBRE_SUPPORT, source_offset=4, target_offset=4),
    "IR": shifted_cells(
        {reduction.transpose(cell) for cell in T_FIBRE_SUPPORT},
        target_offset=4,
    ),
    "RS": T_FIBRE_SUPPORT,
    "RI": shifted_cells(T_FIBRE_SUPPORT, source_offset=4),
    "RR": Q_FIBRE_SUPPORT,
}
BLOCK_SUPPORT = {
    name: BLOCK_BASE_SUPPORT[name] | BLOCK_FIBRE_SUPPORT[name]
    for name in BLOCK_PRIMITIVES
}


def support_from_written_formulas(
    formulas: dict[str, str],
    coefficients: dict[str, complex],
) -> set[Cell]:
    """Return generic support only after checking the written formula family."""
    if set(formulas) != set(BLOCK_PRIMITIVES):
        raise ValueError("the exact nine carrier blocks are required")
    if set(coefficients) != set(BLOCK_PRIMITIVES):
        raise ValueError("one coefficient status is required for each block")
    if formulas != BLOCK_PRIMITIVES:
        raise TypeError("a sector envelope is not a formula-level support proof")
    return set().union(
        *(
            BLOCK_SUPPORT[name]
            for name, coefficient in coefficients.items()
            if coefficient != 0
        )
    )


def graph_components(
    names: Iterable[str], cells: Iterable[Cell]
) -> tuple[frozenset[str], ...]:
    adjacency = {name: set() for name in names}
    for source, target in cells:
        adjacency[source].add(target)
        adjacency[target].add(source)
    unseen = set(adjacency)
    components: list[frozenset[str]] = []
    while unseen:
        root = min(unseen)
        component = {root}
        queue = deque((root,))
        unseen.remove(root)
        while queue:
            source = queue.popleft()
            for target in adjacency[source]:
                if target in unseen:
                    unseen.remove(target)
                    component.add(target)
                    queue.append(target)
        components.append(frozenset(component))
    return tuple(sorted(components, key=lambda component: min(component)))


def support_closed_under_transpose_and_mirror(cells: set[Cell]) -> bool:
    return all(
        reduction.transpose(cell) in cells and reduction.mirror(cell) in cells
        for cell in cells
    )


def rational_rank(rows: list[list[Fraction]]) -> int:
    if not rows:
        return 0
    matrix = [[Fraction(value) for value in row] for row in rows]
    pivot_row = 0
    for column in range(len(matrix[0])):
        pivot = next(
            (
                row
                for row in range(pivot_row, len(matrix))
                if matrix[row][column]
            ),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        scale = matrix[pivot_row][column]
        matrix[pivot_row] = [value / scale for value in matrix[pivot_row]]
        for row in range(len(matrix)):
            if row == pivot_row:
                continue
            factor = matrix[row][column]
            if factor:
                matrix[row] = [
                    left - factor * right
                    for left, right in zip(matrix[row], matrix[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return pivot_row


RAW_COEFFICIENTS = (
    "a", "bSI", "bSR", "bIS", "d", "bIR", "bRS", "bRI"
)
GAUGE_COEFFICIENTS = ("rS", "rI", "rR")
FORBIDDEN_SELECTORS = frozenset(
    ("P1", "P2", "P3", "count", "generation", "retract", "endpoint")
)


def raw_principal_composition_coefficients(
    coefficients: dict[str, Fraction],
    gauge: dict[str, Fraction],
    **selectors: object,
) -> tuple[Fraction, Fraction, Fraction]:
    if FORBIDDEN_SELECTORS & selectors.keys():
        raise TypeError("held-out datum/count/retract selectors are forbidden")
    if set(coefficients) != set(RAW_COEFFICIENTS):
        raise ValueError("the exact eight raw carrier coefficients are required")
    if set(gauge) != set(GAUGE_COEFFICIENTS):
        raise ValueError("the exact three gauge coefficients are required")
    if not any(gauge.values()):
        raise ValueError("the vacuous zero raw kernel vector is not a witness")

    c = coefficients
    r = gauge
    return (
        c["a"] * r["rS"]
        + c["bSI"] * r["rI"]
        - Fraction(13, 14) * c["bSR"] * r["rR"],
        c["bIS"] * r["rS"]
        - Fraction(6, 7) * c["d"] * r["rI"]
        + Fraction(13, 7) * c["bIR"] * r["rR"],
        c["bRS"] * r["rS"]
        + Fraction(1, 7) * c["bRI"] * r["rI"]
        + Fraction(6, 7) * r["rR"],
    )


def raw_matrix(coefficients: dict[str, Fraction]) -> tuple[tuple[Fraction, ...], ...]:
    c = coefficients
    return (
        (c["a"], c["bSI"], -Fraction(13, 14) * c["bSR"]),
        (c["bIS"], -Fraction(6, 7) * c["d"], Fraction(13, 7) * c["bIR"]),
        (c["bRS"], Fraction(1, 7) * c["bRI"], Fraction(6, 7)),
    )


def determinant3(matrix: tuple[tuple[Fraction, ...], ...]) -> Fraction:
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


WITNESS_C = {
    "a": Fraction(1),
    "bSI": Fraction(1),
    "bSR": Fraction(28, 13),
    "bIS": Fraction(-1),
    "d": Fraction(1),
    "bIR": Fraction(1),
    "bRS": Fraction(-1),
    "bRI": Fraction(1),
}
WITNESS_R = {"rS": Fraction(1), "rI": Fraction(1), "rR": Fraction(1)}


def principal_jacobian(
    coefficients: dict[str, Fraction],
    gauge: dict[str, Fraction],
) -> list[list[Fraction]]:
    """Jacobian in (eight carrier coefficients, rS, rI, rR)."""
    c = coefficients
    r = gauge
    return [
        [
            r["rS"], r["rI"], -Fraction(13, 14) * r["rR"],
            0, 0, 0, 0, 0,
            c["a"], c["bSI"], -Fraction(13, 14) * c["bSR"],
        ],
        [
            0, 0, 0,
            r["rS"], -Fraction(6, 7) * r["rI"],
            Fraction(13, 7) * r["rR"], 0, 0,
            c["bIS"], -Fraction(6, 7) * c["d"],
            Fraction(13, 7) * c["bIR"],
        ],
        [
            0, 0, 0, 0, 0, 0,
            r["rS"], Fraction(1, 7) * r["rI"],
            c["bRS"], Fraction(1, 7) * c["bRI"], Fraction(6, 7),
        ],
    ]


def require_native_noether_packet(packet: dict[str, object]) -> str:
    missing = tuple(field for field in native_contract.REQUIRED if not packet.get(field))
    if missing:
        raise ValueError("native H_c R_r blocked on: " + ", ".join(missing))
    return "packet-present-but-native-composition-not-evaluated-by-this-raw-probe"


def pauli_clifford(
    metric_signs: tuple[int, ...],
) -> tuple[tuple[np.ndarray, ...], tuple[int, ...]]:
    """Jordan-Wigner Clifford matrices with intrinsic diagonal metric."""
    dimension = len(metric_signs)
    if dimension % 2 or set(metric_signs) - {-1, 1}:
        raise ValueError("an even-dimensional +/-1 signature is required")
    identity = np.eye(2, dtype=complex)
    sigma_x = np.array(((0, 1), (1, 0)), dtype=complex)
    sigma_y = np.array(((0, -1j), (1j, 0)), dtype=complex)
    sigma_z = np.array(((1, 0), (0, -1)), dtype=complex)
    gammas: list[np.ndarray] = []
    for index in range(dimension // 2):
        prefix = [sigma_z] * index
        suffix = [identity] * (dimension // 2 - index - 1)
        for middle in (sigma_x, sigma_y):
            factors = prefix + [middle] + suffix
            matrix = factors[0]
            for factor in factors[1:]:
                matrix = np.kron(matrix, factor)
            gammas.append(matrix)
    signed = tuple(
        gamma if sign == 1 else 1j * gamma
        for gamma, sign in zip(gammas, metric_signs)
    )
    return signed, metric_signs


class CliffordSymbol:
    """Finite Clifford/gamma-trace realization without dense V⊗S projectors."""

    def __init__(
        self,
        metric_signs: tuple[int, ...],
        xi: np.ndarray,
    ) -> None:
        self.n = len(metric_signs)
        self.gamma, self.signs = pauli_clifford(metric_signs)
        self.xi = np.asarray(xi, dtype=complex)
        self.spinor_dimension = self.gamma[0].shape[0]
        self.cxi = sum(
            (
                sign * component * gamma
                for sign, component, gamma in zip(
                    self.signs, self.xi, self.gamma
                )
            ),
            np.zeros_like(self.gamma[0]),
        )
        self.q = sum(
            sign * component * component
            for sign, component in zip(self.signs, self.xi)
        )

    def gamma_trace(self, vector_spinor: np.ndarray) -> np.ndarray:
        return sum(
            (
                sign * gamma @ vector_spinor[index]
                for index, (sign, gamma) in enumerate(
                    zip(self.signs, self.gamma)
                )
            ),
            np.zeros(self.spinor_dimension, dtype=complex),
        )

    def j(self, spinor: np.ndarray) -> np.ndarray:
        return np.stack(
            [gamma @ spinor / self.n for gamma in self.gamma],
            axis=0,
        )

    def p_i(self, vector_spinor: np.ndarray) -> np.ndarray:
        return self.j(self.gamma_trace(vector_spinor))

    def p_r(self, vector_spinor: np.ndarray) -> np.ndarray:
        return vector_spinor - self.p_i(vector_spinor)

    def m(self, vector_spinor: np.ndarray) -> np.ndarray:
        return np.stack(
            [self.cxi @ component for component in vector_spinor],
            axis=0,
        )

    def t(self, spinor: np.ndarray) -> np.ndarray:
        raw = np.stack(
            [component * spinor for component in self.xi],
            axis=0,
        )
        return self.p_r(raw)

    def contraction(self, vector_spinor: np.ndarray) -> np.ndarray:
        return sum(
            (
                sign * component * vector_spinor[index]
                for index, (sign, component) in enumerate(
                    zip(self.signs, self.xi)
                )
            ),
            np.zeros(self.spinor_dimension, dtype=complex),
        )

    def delta(self, vector_spinor: np.ndarray) -> np.ndarray:
        return -self.contraction(vector_spinor)

    def q_block(self, vector_spinor: np.ndarray) -> np.ndarray:
        return self.p_r(self.m(self.p_r(vector_spinor)))


def relative_error(left: np.ndarray, right: np.ndarray) -> float:
    left_array = np.asarray(left, dtype=complex)
    right_array = np.asarray(right, dtype=complex)
    scale = max(
        1.0,
        float(np.linalg.norm(left_array)),
        float(np.linalg.norm(right_array)),
    )
    return float(np.linalg.norm(left_array - right_array)) / scale


def clifford_identity_residuals(
    metric_signs: tuple[int, ...],
    seed: int,
) -> dict[str, float]:
    rng = np.random.default_rng(seed)
    dimension = len(metric_signs)
    xi = rng.normal(size=dimension)
    symbol = CliffordSymbol(metric_signs, xi)
    spinor = (
        rng.normal(size=symbol.spinor_dimension)
        + 1j * rng.normal(size=symbol.spinor_dimension)
    )
    vector_spinor = (
        rng.normal(size=(dimension, symbol.spinor_dimension))
        + 1j * rng.normal(size=(dimension, symbol.spinor_dimension))
    )
    pr_vector = symbol.p_r(vector_spinor)
    trace = symbol.gamma_trace(vector_spinor)

    return {
        "Gamma-j": relative_error(symbol.gamma_trace(symbol.j(spinor)), spinor),
        "PI-M-PI": relative_error(
            symbol.p_i(symbol.m(symbol.p_i(vector_spinor))),
            -float(Fraction(dimension - 2, dimension))
            * symbol.j(symbol.cxi @ trace),
        ),
        "PR-M-j": relative_error(
            symbol.p_r(symbol.m(symbol.j(spinor))),
            float(Fraction(2, dimension)) * symbol.t(spinor),
        ),
        "PR-M-PI": relative_error(
            symbol.p_r(symbol.m(symbol.p_i(vector_spinor))),
            float(Fraction(2, dimension)) * symbol.t(trace),
        ),
        "PI-M-PR": relative_error(
            symbol.p_i(symbol.m(pr_vector)),
            -2 * symbol.j(symbol.delta(pr_vector)),
        ),
        "delta-T": relative_error(
            symbol.delta(symbol.t(spinor)),
            -float(Fraction(dimension - 1, dimension)) * symbol.q * spinor,
        ),
        "Q-T": relative_error(
            symbol.q_block(symbol.t(spinor)),
            float(Fraction(dimension - 2, dimension))
            * symbol.t(symbol.cxi @ spinor),
        ),
        "Q-trace": float(np.linalg.norm(
            symbol.gamma_trace(symbol.q_block(vector_spinor))
        )),
    }


def numeric_raw_composition(
    symbol: CliffordSymbol,
    coefficients: dict[str, Fraction],
    gauge: dict[str, Fraction],
    spinor: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Apply the written block symbols to the written gauge symbol."""
    c = {name: complex(value) for name, value in coefficients.items()}
    r = {name: complex(value) for name, value in gauge.items()}

    gauge_s = r["rS"] * (symbol.cxi @ spinor)
    gauge_i = r["rI"] * symbol.j(symbol.cxi @ spinor)
    gauge_r = r["rR"] * symbol.t(spinor)

    out_s = (
        c["a"] * (symbol.cxi @ gauge_s)
        + c["bSI"] * (symbol.cxi @ symbol.gamma_trace(gauge_i))
        + c["bSR"] * symbol.delta(gauge_r)
    )
    out_i = (
        c["bIS"] * symbol.j(symbol.cxi @ gauge_s)
        + c["d"] * symbol.p_i(symbol.m(symbol.p_i(gauge_i)))
        + c["bIR"] * symbol.p_i(symbol.m(symbol.p_r(gauge_r)))
    )
    out_r = (
        c["bRS"] * symbol.t(gauge_s)
        + c["bRI"] * symbol.p_r(symbol.m(symbol.p_i(gauge_i)))
        + symbol.q_block(gauge_r)
    )
    return out_s, out_i, out_r


def main() -> None:
    print("Full-20 support-manifest and raw carrier-composition certificate")
    print("construction: actual Sym^2 fibre; geometric gamma-traceless RS")
    print(
        "grade: analytic complex H-support manifest for a generic covector "
        "with nonzero base/fibre projections; raw D_c R_r"
    )
    print("not claimed: native H_c R_r, BV closure, quotient, count, or all-xi rank")

    all_names = tuple(slot.name for slot in ledger.SLOTS)
    allowed = reduction.nonzero_cells()
    base_cells = {cell for cell in allowed if cell_parts(cell) == (1, 0)}
    fibre_cells = {cell for cell in allowed if cell_parts(cell) == (0, 1)}

    print("\nA. Independent envelope and exact projected-Q branching")
    check("the independent ledger has 20 labeled slots", len(all_names) == 20)
    check("the independent allowed envelope has 136 ordered cells", len(allowed) == 136)
    check(
        "base and Sym^2-fibre branching split the envelope as 68+68",
        len(base_cells) == len(fibre_cells) == 68
        and base_cells.isdisjoint(fibre_cells)
        and base_cells | fibre_cells == allowed,
    )
    check("Q has 20 explicit base cells", len(Q_BASE_SUPPORT) == 20)
    check("Q has 20 explicit fibre cells", len(Q_FIBRE_SUPPORT) == 20)
    check(
        "the explicit Q lists agree with independent base/fibre branching",
        Q_BASE_SUPPORT <= base_cells and Q_FIBRE_SUPPORT <= fibre_cells,
    )
    check(
        "the explicit Q branching exactly fills the 40-cell R->R envelope",
        Q_SUPPORT == cells_for_sector_pair("R", "R") and len(Q_SUPPORT) == 40,
    )
    base_rank = Fraction(4)
    fibre_rank = Fraction(10)
    q_low_base = (
        fibre_rank * (2 - base_rank) / base_rank - base_rank
    ) / (base_rank + fibre_rank)
    q_low_fibre = (
        -fibre_rank
        + base_rank * (2 - fibre_rank) / fibre_rank
    ) / (base_rank + fibre_rank)
    check(
        "projected-Q low-R base coefficient is exactly -9/14 and nonzero",
        q_low_base == -Fraction(9, 14),
    )
    check(
        "projected-Q low-R fibre coefficient is exactly -33/35 and nonzero",
        q_low_fibre == -Fraction(33, 35),
    )
    check(
        "the analytic low-to-X projection coefficients 2/4 and 2/10 are nonzero",
        Fraction(2, 4) != 0 and Fraction(2, 10) != 0,
    )
    planted_q = set(Q_SUPPORT)
    planted_q.remove(min(planted_q))
    check("deleting one planted Q cell fails exact projected-Q support", planted_q != cells_for_sector_pair("R", "R"))

    print("\nB. Nine carrier blocks collapse to four primitive symbol families")
    block_counts = {name: len(cells) for name, cells in BLOCK_SUPPORT.items()}
    expected_counts = {
        "SS": 8, "SI": 8, "SR": 16,
        "IS": 8, "II": 8, "IR": 16,
        "RS": 16, "RI": 16, "RR": 40,
    }
    check("all nine exact block-support counts agree", block_counts == expected_counts, str(block_counts))
    check(
        "every formula-derived block cell is independently representation-allowed",
        set().union(*BLOCK_SUPPORT.values()) <= allowed,
    )
    formula_base_support = set().union(*BLOCK_BASE_SUPPORT.values())
    formula_fibre_support = set().union(*BLOCK_FIBRE_SUPPORT.values())
    check(
        "the formula-derived base lists independently fill exactly 68 cells",
        formula_base_support == base_cells,
    )
    check(
        "the formula-derived Sym^2-fibre lists independently fill exactly 68 cells",
        formula_fibre_support == fibre_cells,
    )
    check(
        "the written blocks use only c, T, delta, Q up to canonical j/Gamma maps",
        {
            primitive.replace("Gamma", "").replace("j", "")
            for primitive in BLOCK_PRIMITIVES.values()
        }
        == {"c", "T", "delta", "Q"},
    )
    generic_coefficients = {name: 1.0 + 0.1j for name in BLOCK_PRIMITIVES}
    formula_support = support_from_written_formulas(
        dict(BLOCK_PRIMITIVES), generic_coefficients
    )
    check(
        "generic formula support reverses preregistration and saturates all 136 cells",
        formula_support == allowed,
    )
    without_x = {
        cell
        for cell in formula_support
        if not cell[0].startswith("X:") and not cell[1].startswith("X:")
    }
    check(
        "omitting X changes the manifest and fails full-slot coverage",
        len(without_x) < len(formula_support)
        and {
            endpoint
            for cell in without_x
            for endpoint in cell
        }
        != set(all_names),
    )
    def collapse_provenance(name: str) -> str:
        if name.startswith(("S:", "imGamma:", "kerGamma:")):
            return "E:" + name.split(":", 1)[1]
        return name

    collapsed_manifest = {
        (collapse_provenance(source), collapse_provenance(target))
        for source, target in formula_support
    }
    check(
        "collapsing S/imGamma/low-R provenance changes the manifest",
        len(collapsed_manifest) < len(formula_support),
    )
    for block, deletion_count in expected_counts.items():
        one_zero = dict(generic_coefficients)
        one_zero[block] = 0
        reduced_support = support_from_written_formulas(
            dict(BLOCK_PRIMITIVES), one_zero
        )
        check(
            (
                f"planting removal of fixed {block}/Q deletes its linked "
                f"{deletion_count}-cell family"
                if block == "RR"
                else f"zeroing {block} deletes its whole linked "
                f"{deletion_count}-cell family"
            ),
            len(formula_support - reduced_support) == deletion_count
            and reduced_support == formula_support - BLOCK_SUPPORT[block],
        )
    check(
        "all 39 prior transpose/mirror support orbits are occupied",
        len(reduction.joint_orbits(formula_support)) == 39,
    )
    rr_orbits = reduction.joint_orbits(Q_SUPPORT)
    off_core_orbits = [
        orbit
        for orbit in reduction.joint_orbits(formula_support)
        if not orbit <= Q_SUPPORT
    ]
    check("Q owns 13 joint support orbits", len(rr_orbits) == 13)
    check("the written off-core formulas occupy 26 more joint support orbits", len(off_core_orbits) == 26)
    provenance_orbit_census = {
        "SS": len(reduction.joint_orbits(BLOCK_SUPPORT["SS"])),
        "II": len(reduction.joint_orbits(BLOCK_SUPPORT["II"])),
        "RR": len(reduction.joint_orbits(BLOCK_SUPPORT["RR"])),
        "SI": len(reduction.joint_orbits(
            BLOCK_SUPPORT["SI"] | BLOCK_SUPPORT["IS"]
        )),
        "SR": len(reduction.joint_orbits(
            BLOCK_SUPPORT["SR"] | BLOCK_SUPPORT["RS"]
        )),
        "IR": len(reduction.joint_orbits(
            BLOCK_SUPPORT["IR"] | BLOCK_SUPPORT["RI"]
        )),
    }
    check(
        "the provenance-refined joint-orbit census is 3,3,13,4,8,8",
        provenance_orbit_census
        == {"SS": 3, "II": 3, "RR": 13, "SI": 4, "SR": 8, "IR": 8},
        str(provenance_orbit_census),
    )
    info(
        "support evidence grade is analytic derivation plus executable "
        "manifest consistency, not a 20-projector rederivation"
    )

    print("\nC. Connectivity and support-level strata")
    full_components = graph_components(all_names, formula_support)
    base_components = graph_components(all_names, base_cells)
    fibre_components = graph_components(all_names, fibre_cells)
    check("the full generic formula-support graph is connected", len(full_components) == 1)
    check("horizontal-only support has four components", len(base_components) == 4)
    check("vertical-only support has four components", len(fibre_components) == 4)
    check(
        "generic support is closed under transpose and mirror at support level",
        support_closed_under_transpose_and_mirror(formula_support),
    )
    outgoing_degrees = {
        name: sum(source == name for source, _target in formula_support)
        for name in all_names
    }
    incoming_degrees = {
        name: sum(target == name for _source, target in formula_support)
        for name in all_names
    }
    check(
        "every S/I/low-R slot has in/out degree 8",
        all(
            outgoing_degrees[name] == incoming_degrees[name] == 8
            for name in all_names[:12]
        ),
    )
    check(
        "every X slot has in/out degree 5",
        all(
            outgoing_degrees[name] == incoming_degrees[name] == 5
            for name in all_names[12:]
        ),
    )

    paired_families = {
        "SI": ("SI", "IS"),
        "SR": ("SR", "RS"),
        "IR": ("IR", "RI"),
    }
    expected_strata = {
        ("SI", "SR"): (88, 12),
        ("SI", "IR"): (88, 12),
        ("SR", "IR"): (104, 16),
    }
    connected_strata: dict[tuple[str, str], tuple[int, int]] = {}
    for family_pair in combinations(paired_families, 2):
        blocks = ("RR",) + tuple(
            block
            for family in family_pair
            for block in paired_families[family]
        )
        support = set().union(*(BLOCK_SUPPORT[block] for block in blocks))
        extra_orbits = len(reduction.joint_orbits(support)) - len(rr_orbits)
        if len(graph_components(all_names, support)) == 1:
            connected_strata[family_pair] = (len(support), extra_orbits)
    check(
        "exactly the three two-bridge strata connect with fixed Q core",
        connected_strata == expected_strata,
        str(connected_strata),
    )
    for family in paired_families:
        blocks = ("RR",) + paired_families[family]
        support = set().union(*(BLOCK_SUPPORT[block] for block in blocks))
        check(
            f"one paired bridge {family} is insufficient",
            len(graph_components(all_names, support)) > 1,
        )
    all_bridge_blocks = ("RR", "SI", "IS", "SR", "RS", "IR", "RI")
    all_bridge_support = set().union(
        *(BLOCK_SUPPORT[block] for block in all_bridge_blocks)
    )
    check(
        "all three paired bridges give 120 cells and 20 off-core orbits",
        len(all_bridge_support) == 120
        and len(reduction.joint_orbits(all_bridge_support)) - len(rr_orbits) == 20,
    )
    check(
        "adding SS and II gives the full 136-cell formula support",
        all_bridge_support | BLOCK_SUPPORT["SS"] | BLOCK_SUPPORT["II"]
        == formula_support,
    )

    print("\nD. Candidate gauge-map incidence")
    gauge_support = {
        "rS": {
            ("G:" + source.removeprefix("S:"), target)
            for source, target in C_SUPPORT
        },
        "rI": {
            ("G:" + source.removeprefix("S:"), target)
            for source, target in shifted_cells(C_SUPPORT, target_offset=4)
        },
        "rR": {
            ("G:" + source.removeprefix("S:"), target)
            for source, target in T_SUPPORT
        },
    }
    gauge_counts = {name: len(cells) for name, cells in gauge_support.items()}
    generic_gauge_support = set().union(*gauge_support.values())
    gauge_base_support = (
        {
            ("G:" + source.removeprefix("S:"), target)
            for source, target in C_BASE_SUPPORT
        }
        | {
            ("G:" + source.removeprefix("S:"), target)
            for source, target in shifted_cells(
                C_BASE_SUPPORT, target_offset=4
            )
        }
        | {
            ("G:" + source.removeprefix("S:"), target)
            for source, target in T_BASE_SUPPORT
        }
    )
    gauge_fibre_support = (
        {
            ("G:" + source.removeprefix("S:"), target)
            for source, target in C_FIBRE_SUPPORT
        }
        | {
            ("G:" + source.removeprefix("S:"), target)
            for source, target in shifted_cells(
                C_FIBRE_SUPPORT, target_offset=4
            )
        }
        | {
            ("G:" + source.removeprefix("S:"), target)
            for source, target in T_FIBRE_SUPPORT
        }
    )
    check("the three gauge blocks have exact support counts 8+8+16", gauge_counts == {"rS": 8, "rI": 8, "rR": 16})
    check("generic gauge support has 32 cells", len(generic_gauge_support) == 32)
    check(
        "gauge incidence splits as 16 base plus 16 fibre cells",
        len(gauge_base_support) == len(gauge_fibre_support) == 16
        and gauge_base_support.isdisjoint(gauge_fibre_support),
    )
    check(
        "generic gauge support reaches all 20 observer targets",
        {target for _source, target in generic_gauge_support} == set(all_names),
    )
    target_incidence = {
        target: sum(candidate_target == target for _source, candidate_target in generic_gauge_support)
        for target in all_names
    }
    check(
        "slots 1-12 receive two gauge cells while each X slot receives one",
        all(target_incidence[name] == 2 for name in all_names[:12])
        and all(target_incidence[name] == 1 for name in all_names[12:]),
    )
    gauge_names = (
        {source for source, _target in generic_gauge_support}
        | set(all_names)
    )
    check(
        "the gauge-incidence graph alone has two components",
        len(graph_components(gauge_names, generic_gauge_support)) == 2,
    )

    print("\nE. Exact raw principal D_c R_r locus")
    witness_coefficients = raw_principal_composition_coefficients(
        WITNESS_C, WITNESS_R
    )
    check(
        "the all-nonzero rational vector is in the raw principal kernel",
        witness_coefficients == (0, 0, 0),
    )
    check("the witness carrier matrix has determinant zero", determinant3(raw_matrix(WITNESS_C)) == 0)
    check(
        "the witness uses every principal carrier and raw-vector coefficient",
        all(WITNESS_C.values()) and all(WITNESS_R.values()),
    )
    generic_c = {name: Fraction(1) for name in RAW_COEFFICIENTS}
    generic_r = {name: Fraction(1) for name in GAUGE_COEFFICIENTS}
    check(
        "an unfitted all-one point has nonzero raw carrier composition",
        raw_principal_composition_coefficients(generic_c, generic_r)
        != (0, 0, 0),
    )
    perturbed_c = dict(WITNESS_C)
    perturbed_c["bSR"] += Fraction(1, 13)
    check(
        "a planted coefficient perturbation removes the raw kernel vector",
        raw_principal_composition_coefficients(perturbed_c, WITNESS_R)
        != (0, 0, 0),
    )
    check(
        "the vacuous r=0 kernel vector is rejected",
        rejects(
            lambda: raw_principal_composition_coefficients(
                WITNESS_C, {"rS": Fraction(0), "rI": Fraction(0), "rR": Fraction(0)}
            )
        ),
    )
    for selector in sorted(FORBIDDEN_SELECTORS):
        check(
            f"API fence rejects held-out selector {selector}",
            rejects(
                lambda selector=selector: raw_principal_composition_coefficients(
                    WITNESS_C, WITNESS_R, **{selector: object()}
                )
            ),
        )

    jacobian_rank = rational_rank(principal_jacobian(WITNESS_C, WITNESS_R))
    check("the three principal equations have generic witness Jacobian rank 3", jacobian_rank == 3)
    check(
        "the unquotiented joint (c,r) incidence locus is locally complex dimension 8",
        11 - jacobian_rank == 8,
    )
    check(
        "det M(c)=0 is generically a complex-dimension-7 carrier hypersurface",
        determinant3(raw_matrix(generic_c)) != 0,
    )
    check(
        "overall nonzero raw-kernel-vector scaling is explicitly redundant",
        raw_principal_composition_coefficients(
            WITNESS_C,
            {name: 3 * value for name, value in WITNESS_R.items()},
        )
        == (0, 0, 0),
    )

    # mu0*rR*T is one member of the unresolved lower-principal remainder.
    # It is not an independent equation until the other R-valued remainders
    # are decomposed and shown unable to cancel its T component.
    info(
        "mu0*rR*T is recorded only as one unresolved lower-order pressure; "
        "the probe does not impose it as an independent equation"
    )
    check(
        "raw pure-T vector fails against the fixed geometric compressed-Q block",
        raw_principal_composition_coefficients(
            {**WITNESS_C, "bSR": Fraction(0), "bIR": Fraction(0)},
            {"rS": Fraction(0), "rI": Fraction(0), "rR": Fraction(1)},
        )[2]
        == Fraction(6, 7),
    )

    print("\nF. Finite Clifford controls and null-covector trap")
    actual_observer_signs = (
        (1, 1, 1, -1)
        + (1, 1, 1, 1, 1, 1, -1, -1, -1, -1)
    )
    for signs, label in (
        ((1,) * 4, "(4,0)"),
        ((1,) * 8, "(8,0)"),
        ((1,) * 14, "(14,0)"),
        (actual_observer_signs, "(3,1)+(6,4)=(9,5)"),
    ):
        residuals = clifford_identity_residuals(
            signs, 2000 + 10 * len(signs) + signs.count(-1)
        )
        check(
            f"all intrinsic Clifford/projector identities hold in signature {label}",
            max(residuals.values()) < TOL,
            f"max residual {max(residuals.values()):.2e}",
        )

    rng = np.random.default_rng(731)
    for signs, label in (
        ((1,) * 14, "(14,0)"),
        (actual_observer_signs, "(3,1)+(6,4)"),
    ):
        xi = rng.normal(size=14)
        symbol = CliffordSymbol(signs, xi)
        spinor = (
            rng.normal(size=symbol.spinor_dimension)
            + 1j * rng.normal(size=symbol.spinor_dimension)
        )
        numeric_witness = numeric_raw_composition(
            symbol, WITNESS_C, WITNESS_R, spinor
        )
        check(
            f"the exact rational vector is in the finite principal-symbol kernel in {label}",
            max(float(np.linalg.norm(component)) for component in numeric_witness)
            < TOL * max(1.0, float(np.linalg.norm(spinor))),
        )

    null_xi = np.zeros(14)
    null_xi[0] = 1
    null_xi[10] = 1
    null_symbol = CliffordSymbol(actual_observer_signs, null_xi)
    null_spinor = (
        rng.normal(size=null_symbol.spinor_dimension)
        + 1j * rng.normal(size=null_symbol.spinor_dimension)
    )
    null_generic = numeric_raw_composition(
        null_symbol, generic_c, generic_r, null_spinor
    )
    check(
        "the planted base-plus-fibre covector is null in the actual (3,1)+(6,4) split",
        abs(null_symbol.q) < TOL,
    )
    check(
        "null-only sampling erases S/I defects even at a non-closing point",
        max(float(np.linalg.norm(component)) for component in null_generic[:2])
        < TOL * max(1.0, float(np.linalg.norm(null_spinor))),
    )
    check(
        "the same null sample retains a nonzero R readout",
        float(np.linalg.norm(null_generic[2]))
        > TOL * max(1.0, float(np.linalg.norm(null_spinor))),
    )

    print("\nG. Native boundary and transfer scope")
    check(
        "the existing native packet names exactly five unresolved fields",
        len(native_contract.REQUIRED) == 5,
    )
    check(
        "native H_c R_r is refused while that packet is unfrozen",
        rejects(lambda: require_native_noether_packet(native_contract.UNFROZEN)),
    )
    polarized_m33 = lambda h_rr: Fraction(6, 7) * h_rr
    info(
        "conditional polarized bookkeeping uses M33=(6/7)h_RR "
        f"(h_RR=0 gives {polarized_m33(Fraction(0))})"
    )
    symmetric_basis = tuple(
        ("sym", left, right)
        for left in range(4)
        for right in range(left, 4)
    )
    exterior_basis = (
        tuple(("wedge2",) + pair for pair in combinations(range(4), 2))
        + tuple(("wedge3",) + triple for triple in combinations(range(4), 3))
    )
    check(
        "Sym^2 has ten explicit basis pairs including four diagonals",
        len(symmetric_basis) == 10
        and sum(left == right for _tag, left, right in symmetric_basis) == 4,
    )
    check(
        "the exterior comparator has six wedge-2 plus four wedge-3 basis elements and no diagonals",
        len(exterior_basis) == 10
        and sum(item[0] == "wedge2" for item in exterior_basis) == 6
        and sum(item[0] == "wedge3" for item in exterior_basis) == 4,
    )
    check(
        "central GL4 weights obstruct a natural Sym^2 versus wedge2+wedge3 identification",
        (2,) * 10 != (2,) * 6 + (3,) * 4,
    )

    print("\nExact support summary:")
    for block in ("SS", "SI", "SR", "IS", "II", "IR", "RS", "RI", "RR"):
        print(
            f"  {block}: primitive={BLOCK_PRIMITIVES[block]:<7} "
            f"cells={len(BLOCK_SUPPORT[block])}"
        )
    print("  carrier total: 136 = 68 base + 68 Sym^2-fibre")
    print("  gauge total: 32 = 8 c + 8 jc + 16 T")

    print("\nRaw principal equations at n=14:")
    print("  F_S = a rS + bSI rI - (13/14) bSR rR")
    print("  F_I = bIS rS - (6/7) d rI + (13/7) bIR rR")
    print("  F_R = bRS rS + (1/7) bRI rI + (6/7) rR")
    print("  lower unresolved remainder includes mu0 rR T among five other terms")
    print("  det M(c)=0: generic complex carrier hypersurface dimension 7")
    print("  joint (c,r) complex incidence dimension 8 before C* scaling")

    if FAILURES:
        print(f"\nRESULT: FAIL ({len(FAILURES)} failed checks)")
        for failure in FAILURES:
            print(f"  - {failure}")
        raise SystemExit(1)

    print("\nRESULT: FULL20-FORMULA-SUPPORT-SATURATES-136")
    print("RESULT: FOUR-PRIMITIVE-SYMBOL-FAMILIES")
    print("RESULT: RAW-PRINCIPAL-CARRIER-DET-M-LOCUS-NONEMPTY")
    print("RESIDUAL: NATIVE-NOETHER-BLOCKED-BY-FIVE-FIELD-PACKET")
    print("RESIDUAL: NO-NEW-COMPENSATOR-YET-DEMANDED")


if __name__ == "__main__":
    main()
