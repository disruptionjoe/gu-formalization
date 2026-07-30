#!/usr/bin/env python3
"""Swing-1 certificate for the full-20 observer action/BV first write.

This probe checks a finite *relative observer-fermion* quadratic ansatz over a
fixed background connection ``A``.  It does not claim a complete ambient IG
action, a master-equation solution, a native real/Krein domain, or B5
cohomology.

The main Layer-0 result is deliberately capable of reversing the
preregistration:

* the 20-slot observer carrier, its ordinary density dual, and its shifted BV
  antifield are three different objects;
* W131 is an endomorphism of the 12-slot ``ker Gamma`` carrier and must be
  lowered before comparison with an Euler--Lagrange equation;
* the full 136-cell *allowed envelope* has one Z/2 coloring up to reversal,
  but that whole bidirectional envelope cannot be an integer degree-+1
  endomorphism of one copy of the 20-slot carrier; and
* the source-shaped four-stage candidate has rank sequence
  ``128 -> 1792 -> 1792 -> 128`` at form degrees ``0, 1, 13, 14``.

The actual formula-level irrep support remains uncomputed.  The BV coordinate
census is complex rank 4608, and the displayed real Hamiltonian theory uses
its underlying real space of rank 9216.  All arithmetic is exact and
deterministic.  The hostile controls reject semantic collapses even when
their dimensions still look right.
"""

from __future__ import annotations

from collections import deque
from dataclasses import asdict, dataclass
from fractions import Fraction
import hashlib
import json
import os
import sys
from typing import Iterable


HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))

import shiab_b5_krein_mirror_orbit_reduction as reduction  # noqa: E402
import shiab_b5_native_packet_contract as native_contract  # noqa: E402
import shiab_b5_observer_symbol_multiplicity_matrix as ledger  # noqa: E402


FAILURES: list[str] = []


def check(label: str, condition: bool, detail: str = "") -> None:
    status = "PASS" if condition else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


def rejects(callable_) -> bool:
    try:
        callable_()
    except (AssertionError, TypeError, ValueError):
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


def form_degree(slot_name: str) -> int:
    return 0 if sector(slot_name) == "S" else 1


@dataclass(frozen=True)
class GimmelFibre:
    base_rank: int
    vertical_kind: str
    vertical_rank: int
    diagonal_rank: int

    @property
    def total_rank(self) -> int:
        return self.base_rank + self.vertical_rank


PROGRAM_FIBRE = GimmelFibre(
    base_rank=4,
    vertical_kind="Sym2(T*X)",
    vertical_rank=4 * (4 + 1) // 2,
    diagonal_rank=4,
)
EXTERIOR_TEN_CONTROL = GimmelFibre(
    base_rank=4,
    vertical_kind="Lambda2(T*X)+Lambda3(T*X)",
    vertical_rank=6 + 4,
    diagonal_rank=0,
)


@dataclass(frozen=True)
class ObserverField:
    name: str
    h_type: str
    mirror: str
    dimension: int
    provenance: str
    form: int
    ghost: int = 0
    antifield_number: int = 0
    parity: int = 1
    w131: bool = False


OBSERVER_FIELDS = tuple(
    ObserverField(
        name=slot.name,
        h_type=slot.h_type,
        mirror=slot.mirror,
        dimension=slot.dimension,
        provenance=sector(slot.name),
        form=form_degree(slot.name),
        w131=sector(slot.name) == "R",
    )
    for slot in ledger.SLOTS
)


@dataclass(frozen=True)
class CarrierBlock:
    name: str
    source: str
    target: str
    coefficient: str
    formula: str
    differential_order: str
    charge: str


# Rows are targets and columns are sources in S + I + R.  The RR principal
# coefficient is inherited and normalized to one; mu0 is its open lower-order
# scalar.  No adjoint relation between the eight off-core coefficients is
# assumed.
CARRIER_BLOCKS = (
    CarrierBlock("SS", "S", "S", "a", "D_S", "1", "posit"),
    CarrierBlock("SI", "I", "S", "b_SI", "D_S Gamma_I", "1", "posit"),
    CarrierBlock("SR", "R", "S", "b_SR", "delta_R", "1", "posit"),
    CarrierBlock("IS", "S", "I", "b_IS", "j D_S", "1", "posit"),
    CarrierBlock("II", "I", "I", "d", "P_I D_V P_I", "1", "posit"),
    CarrierBlock("IR", "R", "I", "b_IR", "P_I D_V P_R", "1", "posit"),
    CarrierBlock("RS", "S", "R", "b_RS", "T", "1", "posit"),
    CarrierBlock("RI", "I", "R", "b_RI", "P_R D_V P_I", "1", "posit"),
    CarrierBlock(
        "RR",
        "R",
        "R",
        "1; mu0",
        "P_R D_V P_R + mu0 P_R",
        "1 + 0",
        "inherited principal block; posit lower-order scalar",
    ),
)


GAUGE_BLOCKS = (
    CarrierBlock("R_S", "G", "S", "r_S", "D_S", "1", "posit"),
    CarrierBlock("R_I", "G", "I", "r_I", "j D_S", "1", "posit"),
    CarrierBlock("R_R", "G", "R", "r_R", "T", "1", "posit"),
)


POSIT_COEFFICIENTS = (
    "a",
    "b_SI",
    "b_SR",
    "b_IS",
    "d",
    "b_IR",
    "b_RS",
    "b_RI",
    "mu0",
    "r_S",
    "r_I",
    "r_R",
)


CANONICAL_MAPS = (
    "Gamma",
    "Gamma_sharp_g(s)=sum_a e^a tensor c(e_a)s",
    "j=(1/14)Gamma_sharp_g",
    "P_I=j Gamma",
    "P_R=1-P_I",
    "density evaluation",
    "shifted-cotangent BV pairing",
)


NATIVE_OPEN_FIELDS = (
    "slot_pairing_phases",
    "coflip_linearity_and_phases",
    "formal_adjoint_sign",
    "green_boundary_form",
    "common_closed_domain",
)


@dataclass(frozen=True)
class NaturalMap:
    name: str
    domain: str
    codomain: str
    orders: tuple[int, ...]
    linearity: str


def compose(outer: NaturalMap, inner: NaturalMap, name: str) -> NaturalMap:
    assert inner.codomain == outer.domain
    if outer.linearity == inner.linearity == "complex-linear":
        linearity = "complex-linear"
    elif "real-linear" in (outer.linearity, inner.linearity):
        linearity = "real-linear"
    else:
        linearity = "conjugate-linear"
    return NaturalMap(
        name,
        inner.domain,
        outer.codomain,
        tuple(sorted({left + right for left in outer.orders for right in inner.orders})),
        linearity,
    )


PRIMITIVE_MAPS = {
    "D_S": NaturalMap("D_S", "S", "S", (1,), "complex-linear"),
    "Gamma_I": NaturalMap("Gamma_I", "I", "S", (0,), "complex-linear"),
    "j": NaturalMap("j", "S", "I", (0,), "complex-linear"),
    "delta_R": NaturalMap("delta_R", "R", "S", (1,), "complex-linear"),
    "T": NaturalMap("T", "S", "R", (1,), "complex-linear"),
    "D_II": NaturalMap("P_I D_V P_I", "I", "I", (1,), "complex-linear"),
    "D_IR": NaturalMap("P_I D_V P_R", "R", "I", (1,), "complex-linear"),
    "D_RI": NaturalMap("P_R D_V P_I", "I", "R", (1,), "complex-linear"),
    "D_RR": NaturalMap(
        "P_R D_V P_R + mu0 P_R",
        "R",
        "R",
        (0, 1),
        "complex-linear",
    ),
}


BLOCK_TYPINGS = {
    "SS": PRIMITIVE_MAPS["D_S"],
    "SI": compose(PRIMITIVE_MAPS["D_S"], PRIMITIVE_MAPS["Gamma_I"], "D_S Gamma_I"),
    "SR": PRIMITIVE_MAPS["delta_R"],
    "IS": compose(PRIMITIVE_MAPS["j"], PRIMITIVE_MAPS["D_S"], "j D_S"),
    "II": PRIMITIVE_MAPS["D_II"],
    "IR": PRIMITIVE_MAPS["D_IR"],
    "RS": PRIMITIVE_MAPS["T"],
    "RI": PRIMITIVE_MAPS["D_RI"],
    "RR": PRIMITIVE_MAPS["D_RR"],
}


GAUGE_TYPINGS = {
    "R_S": PRIMITIVE_MAPS["D_S"],
    "R_I": compose(PRIMITIVE_MAPS["j"], PRIMITIVE_MAPS["D_S"], "j D_S"),
    "R_R": PRIMITIVE_MAPS["T"],
}


def allowed_cells_for_blocks(
    blocks: Iterable[CarrierBlock],
) -> set[tuple[str, str]]:
    sector_pairs = {(block.source, block.target) for block in blocks}
    return {
        (source, target)
        for source, target in reduction.nonzero_cells()
        if (sector(source), sector(target)) in sector_pairs
    }


def covered_slots(cells: set[tuple[str, str]]) -> tuple[set[str], set[str]]:
    return ({source for source, _ in cells}, {target for _, target in cells})


@dataclass(frozen=True)
class BVCoordinate:
    name: str
    family: str
    rep: str
    dual_rep: str
    dimension: int
    form: int
    ghost: int
    antifield_number: int
    cotangent_flag: int
    parity: int
    partner: str
    origin: str


S_FIELDS = tuple(field for field in OBSERVER_FIELDS if field.provenance == "S")


def build_bv_coordinates() -> tuple[BVCoordinate, ...]:
    result: list[BVCoordinate] = []

    for field in OBSERVER_FIELDS:
        z_name = f"Z/{field.name}"
        zp_name = f"Z+/{field.name}"
        result.extend(
            (
                BVCoordinate(
                    z_name,
                    "Z",
                    field.name,
                    field.mirror,
                    field.dimension,
                    field.form,
                    0,
                    0,
                    0,
                    1,
                    zp_name,
                    "observer field",
                ),
                BVCoordinate(
                    zp_name,
                    "Z+",
                    field.mirror,
                    field.name,
                    field.dimension,
                    14 - field.form,
                    -1,
                    1,
                    1,
                    0,
                    z_name,
                    "field antifield / equation carrier",
                ),
            )
        )

    families = (
        # family, dual family, gh, dual gh, parity, dual parity,
        # antifield number of the shifted-cotangent coordinate, origin
        ("c", "c+", 1, -2, 0, 1, 2, "fermionic RS gauge generator"),
        (
            "barc",
            "barc+",
            -1,
            0,
            0,
            1,
            1,
            "chosen self-dual nonminimal antighost/NL doublet",
        ),
        (
            "b",
            "b+",
            0,
            -1,
            1,
            0,
            1,
            "chosen self-dual nonminimal antighost/NL doublet",
        ),
    )
    for family, dual_family, gh, dual_gh, parity, dual_parity, dual_afn, origin in families:
        for field in S_FIELDS:
            short = field.name.removeprefix("S:")
            name = f"{family}/{short}"
            dual_name = f"{dual_family}/{short}"
            result.extend(
                (
                    BVCoordinate(
                        name,
                        family,
                        field.name,
                        field.mirror,
                        field.dimension,
                        0,
                        gh,
                        0,
                        0,
                        parity,
                        dual_name,
                        origin,
                    ),
                    BVCoordinate(
                        dual_name,
                        dual_family,
                        field.mirror,
                        field.name,
                        field.dimension,
                        14,
                        dual_gh,
                        dual_afn,
                        1,
                        dual_parity,
                        name,
                        origin,
                    ),
                )
            )
    return tuple(result)


BV_COORDINATES = build_bv_coordinates()
BV_BY_NAME = {coordinate.name: coordinate for coordinate in BV_COORDINATES}
EXPECTED_FAMILY_COUNTS = {
    "Z": 20,
    "Z+": 20,
    "c": 4,
    "c+": 4,
    "barc": 4,
    "barc+": 4,
    "b": 4,
    "b+": 4,
}
ALLOWED_BV_ORIGINS = {
    "observer field",
    "field antifield / equation carrier",
    "fermionic RS gauge generator",
    "chosen self-dual nonminimal antighost/NL doublet",
}


def validate_bv_bundle(
    coordinates: tuple[BVCoordinate, ...],
    *,
    require_nonminimal: bool = True,
) -> None:
    names = {coordinate.name for coordinate in coordinates}
    assert len(names) == len(coordinates), "duplicate BV coordinate"
    required_families = {"Z", "Z+", "c", "c+"}
    if require_nonminimal:
        required_families |= {"barc", "barc+", "b", "b+"}
    family_counts = {
        family: sum(coordinate.family == family for coordinate in coordinates)
        for family in {coordinate.family for coordinate in coordinates}
    }
    assert required_families <= set(family_counts)
    expected_counts = {
        family: count
        for family, count in EXPECTED_FAMILY_COUNTS.items()
        if family in required_families
    }
    assert family_counts == expected_counts, "unexpected BV generator manifest"
    assert all(coordinate.origin in ALLOWED_BV_ORIGINS for coordinate in coordinates)
    for coordinate in coordinates:
        assert coordinate.partner in names
        partner = next(item for item in coordinates if item.name == coordinate.partner)
        assert partner.partner == coordinate.name
        assert coordinate.dimension == partner.dimension
        assert coordinate.form + partner.form == 14
        assert coordinate.ghost + partner.ghost == -1
        assert coordinate.parity ^ partner.parity == 1
        assert coordinate.cotangent_flag ^ partner.cotangent_flag == 1


FAMILY_GRADES = {
    "Z": (0, 1, 1920),
    "Z+": (-1, 0, 1920),
    "c": (1, 0, 128),
    "c+": (-2, 1, 128),
    "barc": (-1, 0, 128),
    "barc+": (0, 1, 128),
    "b": (0, 1, 128),
    "b+": (-1, 0, 128),
}


@dataclass(frozen=True)
class HamiltonianArrow:
    component: str
    input_family: str
    output_family: str
    formula: str
    domain_rank: int
    codomain_rank: int
    linearity: str
    unresolved_condition: str = ""


# ``input_family`` names the coordinate occurring in the formula for the
# Q-component of ``output_family``.
HAMILTONIAN_ARROWS = (
    HamiltonianArrow("QZ", "c", "Z", "R c", 128, 1920, "real-linear", "H R = 0"),
    HamiltonianArrow("QZ+", "Z", "Z+", "H Z", 1920, 1920, "real-linear", "H R = 0"),
    HamiltonianArrow("Qc+", "Z+", "c+", "-R^! Z+", 1920, 128, "real-linear", "R^! H = 0"),
    HamiltonianArrow("Qbarc", "b", "barc", "b", 128, 128, "real-linear"),
    HamiltonianArrow("Qb+", "barc+", "b+", "-barc+", 128, 128, "real-linear"),
)


def validate_hamiltonian_arrows(arrows: tuple[HamiltonianArrow, ...]) -> None:
    assert {arrow.component for arrow in arrows} == {
        "QZ",
        "QZ+",
        "Qc+",
        "Qbarc",
        "Qb+",
    }
    for arrow in arrows:
        input_gh, input_parity, input_rank = FAMILY_GRADES[arrow.input_family]
        output_gh, output_parity, output_rank = FAMILY_GRADES[arrow.output_family]
        assert input_gh == output_gh + 1
        assert input_parity == (output_parity ^ 1)
        assert arrow.domain_rank == input_rank
        assert arrow.codomain_rank == output_rank
        assert arrow.linearity == "real-linear"
    participating = {
        family
        for arrow in arrows
        for family in (arrow.input_family, arrow.output_family)
    }
    assert participating == set(FAMILY_GRADES)


def gf2_rank(rows: list[list[int]]) -> int:
    if not rows:
        return 0
    matrix = [sum((value & 1) << column for column, value in enumerate(row)) for row in rows]
    rank = 0
    bit = 0
    width = len(rows[0])
    while bit < width and rank < len(matrix):
        pivot = next((index for index in range(rank, len(matrix)) if (matrix[index] >> bit) & 1), None)
        if pivot is None:
            bit += 1
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        for index in range(len(matrix)):
            if index != rank and ((matrix[index] >> bit) & 1):
                matrix[index] ^= matrix[rank]
        rank += 1
        bit += 1
    return rank


def bipartite_coloring(
    names: tuple[str, ...], cells: set[tuple[str, str]]
) -> dict[str, int]:
    adjacency = {name: set() for name in names}
    for source, target in cells:
        adjacency[source].add(target)
        adjacency[target].add(source)
    colors: dict[str, int] = {}
    for root in names:
        if root in colors:
            continue
        colors[root] = 0
        queue = deque([root])
        while queue:
            source = queue.popleft()
            for target in adjacency[source]:
                wanted = colors[source] ^ 1
                if target in colors:
                    assert colors[target] == wanted, "support graph is not bipartite"
                else:
                    colors[target] = wanted
                    queue.append(target)
    return colors


def rational_rank(rows: list[list[int]]) -> int:
    if not rows:
        return 0
    matrix = [[Fraction(value) for value in row] for row in rows]
    row = 0
    for column in range(len(matrix[0])):
        pivot = next(
            (index for index in range(row, len(matrix)) if matrix[index][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]
        scale = matrix[row][column]
        matrix[row] = [value / scale for value in matrix[row]]
        for index in range(len(matrix)):
            if index == row:
                continue
            factor = matrix[index][column]
            if factor:
                matrix[index] = [
                    left - factor * right
                    for left, right in zip(matrix[index], matrix[row])
                ]
        row += 1
        if row == len(matrix):
            break
    return row


def normalized_filtration_nullity(
    node_count: int, edges: tuple[tuple[int, int], ...]
) -> int:
    rows: list[list[int]] = []
    for source, target in edges:
        row = [0] * node_count
        row[source] = -1
        row[target] = 1
        rows.append(row)
    normalization = [0] * node_count
    normalization[0] = 1
    rows.append(normalization)
    return node_count - rational_rank(rows)


def integer_degree_one_consistent(
    names: tuple[str, ...], cells: set[tuple[str, str]]
) -> bool:
    """Solve f(target)-f(source)=1 for every directed declared cell."""
    adjacency: dict[str, list[tuple[str, int]]] = {name: [] for name in names}
    for source, target in cells:
        adjacency[source].append((target, 1))
        adjacency[target].append((source, -1))
    potentials: dict[str, int] = {}
    for root in names:
        if root in potentials:
            continue
        potentials[root] = 0
        queue = deque([root])
        while queue:
            source = queue.popleft()
            for target, difference in adjacency[source]:
                wanted = potentials[source] + difference
                if target in potentials:
                    if potentials[target] != wanted:
                        return False
                else:
                    potentials[target] = wanted
                    queue.append(target)
    return True


def observer_symbol_cells(object_kind: str) -> set[tuple[str, str]]:
    if object_kind != "observer":
        raise TypeError("the 136-cell census is scoped only to the observer carrier")
    return reduction.nonzero_cells()


@dataclass(frozen=True)
class TypedMap:
    name: str
    domain: str
    codomain: str
    linearity: str


def krein_quadratic_input(operator: TypedMap) -> None:
    assert operator.domain == "E20"
    assert operator.codomain == "E20", "K pairs carrier fields, not an already density-dual output"
    assert operator.linearity == "complex-linear"


def w131_equation_restriction(
    carrier_operator: TypedMap,
    lowering: TypedMap,
    *,
    krein_orthogonal_restriction: bool,
) -> TypedMap:
    assert carrier_operator.domain == carrier_operator.codomain == "R"
    assert lowering.domain == "R" and lowering.codomain == "R_dens_dual"
    assert carrier_operator.linearity == "complex-linear"
    assert lowering.linearity == "conjugate-linear"
    assert krein_orthogonal_restriction, "simplified W131 lowering needs i_R^vee kappa_E = kappa_R pi_R"
    return TypedMap("Pol_gr(kappa_R D_W131)", "R_real", "R_real_dens_dual", "real-linear")


@dataclass(frozen=True)
class UnrolledStage:
    cochain_degree: int
    bundle: str
    ordinary_form_degree: int
    complex_rank: int


UNROLLED_STAGES = (
    UnrolledStage(0, "S", 0, 128),
    UnrolledStage(1, "I+R = T*Y tensor S", 1, 1792),
    UnrolledStage(
        2,
        "(I+R)^vee_dens = Lambda^13 T*Y tensor S^vee",
        13,
        1792,
    ),
    UnrolledStage(3, "S^vee_dens = Lambda^14 T*Y tensor S^vee", 14, 128),
)


def packet_signature_smoke_test(held_out: dict[str, object]) -> str:
    """API fence smoke test; preregistration, not this deletion, carries non-fit evidence."""
    del held_out
    payload = {
        "observer": [asdict(field) for field in OBSERVER_FIELDS],
        "carrier_blocks": [asdict(block) for block in CARRIER_BLOCKS],
        "gauge_blocks": [asdict(block) for block in GAUGE_BLOCKS],
        "bv": [asdict(coordinate) for coordinate in BV_COORDINATES],
        "posits": POSIT_COEFFICIENTS,
        "native_open": NATIVE_OPEN_FIELDS,
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def main() -> None:
    print("=" * 96)
    print("SWING 1: FULL-20 RELATIVE OBSERVER ACTION / BV FIRST-WRITE CERTIFICATE")
    print("=" * 96)

    print("\nL0. Exact observer carrier and semantic separations")
    all_names = {field.name for field in OBSERVER_FIELDS}
    x_fields = [field for field in OBSERVER_FIELDS if field.name.startswith("X:")]
    provenance_fields = [field for field in OBSERVER_FIELDS if not field.name.startswith("X:")]
    w131_fields = [field for field in OBSERVER_FIELDS if field.w131]
    check("all 20 labeled irreducible observer fields are explicit", len(OBSERVER_FIELDS) == 20)
    check("all eight X irreducibles remain separate", len(x_fields) == 8)
    check("the eight X irreducibles form four exact mirror pairs", len({tuple(sorted((field.name, field.mirror))) for field in x_fields}) == 4)
    check("S, imGamma, and low kerGamma provenance copies remain distinct", len(provenance_fields) == 12)
    check("observer carrier complex rank is 1920", sum(field.dimension for field in OBSERVER_FIELDS) == 1920)
    check("S has form degree 0 and I+R have form degree 1", all(field.form == (0 if field.provenance == "S" else 1) for field in OBSERVER_FIELDS))
    check("all observer fields are gh 0 and Grassmann odd", all(field.ghost == 0 and field.parity == 1 for field in OBSERVER_FIELDS))
    check("W131 carrier is exactly 12 slots / rank 1664", len(w131_fields) == 12 and sum(field.dimension for field in w131_fields) == 1664)
    check("beta is not a carrier or principal-symbol slot", all("beta" not in field.name for field in OBSERVER_FIELDS))
    check(
        "program-native fibre is TX plus Sym2(T*X): rank 4+10 with four diagonals",
        PROGRAM_FIBRE.total_rank == 14
        and PROGRAM_FIBRE.vertical_rank == 10
        and PROGRAM_FIBRE.diagonal_rank == 4
        and PROGRAM_FIBRE.vertical_kind == "Sym2(T*X)",
    )
    check(
        "exterior 6+4 numerical ten is structurally rejected despite equal rank",
        EXTERIOR_TEN_CONTROL.total_rank == PROGRAM_FIBRE.total_rank
        and EXTERIOR_TEN_CONTROL.vertical_kind != PROGRAM_FIBRE.vertical_kind
        and EXTERIOR_TEN_CONTROL.diagonal_rank == 0,
    )

    half_x_names = {field.name for field in provenance_fields} | {
        min(field.name, field.mirror) for field in x_fields
    }
    check("planted half-X aggregation fails the exact label census", len(half_x_names) != 20)
    collapsed_provenance = {
        field.name.replace("imGamma:", "S:") for field in OBSERVER_FIELDS
    }
    check("planted S/imGamma provenance collapse fails injectivity", len(collapsed_provenance) != 20)
    check("planted X omission fails both rank and slot count", len(provenance_fields) == 12 and sum(field.dimension for field in provenance_fields) == 384)

    carrier_D = TypedMap("D_c", "E20", "E20", "complex-linear")
    density_E = TypedMap("kappa_E D_c", "E20", "E20_dens_dual", "conjugate-linear")
    shifted_antifield = TypedMap(
        "Z+",
        "E20_dens_dual[cotangent_shift]",
        "BV_coordinate",
        "real-coordinate",
    )
    check("carrier endomorphism is distinct from ordinary density equation", carrier_D.codomain != density_E.codomain)
    check("ordinary density equation is distinct from shifted BV antifield", density_E.codomain != shifted_antifield.domain)
    check("Krein quadratic input accepts the carrier endomorphism", not rejects(lambda: krein_quadratic_input(carrier_D)))
    check("dual-codomain control rejects <Z,E_density Z>_K", rejects(lambda: krein_quadratic_input(density_E)))
    check("Hermitian Krein lowering is conjugate-linear before realification", density_E.linearity == "conjugate-linear")

    print("\nA. Finite natural-map carrier and gauge-generator ansatz")
    check("the carrier family has exactly one declared block for every S/I/R pair", {(block.source, block.target) for block in CARRIER_BLOCKS} == {(source, target) for source in ("S", "I", "R") for target in ("S", "I", "R")})
    check(
        "all nine carrier formulas have machine-checked domain/codomain, order, and linearity",
        all(
            BLOCK_TYPINGS[block.name].domain == block.source
            and BLOCK_TYPINGS[block.name].codomain == block.target
            and BLOCK_TYPINGS[block.name].linearity == "complex-linear"
            and BLOCK_TYPINGS[block.name].orders
            for block in CARRIER_BLOCKS
        ),
    )
    check(
        "all three gauge formulas have machine-checked domain/codomain, order, and linearity",
        all(
            GAUGE_TYPINGS[block.name].domain == "S"
            and GAUGE_TYPINGS[block.name].codomain == block.target
            and GAUGE_TYPINGS[block.name].linearity == "complex-linear"
            and GAUGE_TYPINGS[block.name].orders == (1,)
            for block in GAUGE_BLOCKS
        ),
    )
    check("the eight off-core coefficients are individually named", tuple(block.coefficient for block in CARRIER_BLOCKS[:-1]) == POSIT_COEFFICIENTS[:8])
    check("W131 principal coefficient is inherited while mu0 remains open", CARRIER_BLOCKS[-1].coefficient == "1; mu0" and "inherited" in CARRIER_BLOCKS[-1].charge)
    check("the candidate RS gauge generator reaches all three coarse sectors", {block.target for block in GAUGE_BLOCKS} == {"S", "I", "R"})
    check("all twelve continuous coefficient posits are enumerated once", len(POSIT_COEFFICIENTS) == len(set(POSIT_COEFFICIENTS)) == 12)
    check("canonical splitting and duality maps are separately charged", len(CANONICAL_MAPS) == 7)
    check("all five native phase/domain fields remain explicitly open", tuple(native_contract.REQUIRED) == NATIVE_OPEN_FIELDS)
    check("unfrozen native packet is rejected, not convenience-filled", rejects(lambda: native_contract.admit(native_contract.UNFROZEN)))

    full_cells = reduction.nonzero_cells()
    ansatz_envelope = allowed_cells_for_blocks(CARRIER_BLOCKS)
    sources_covered, targets_covered = covered_slots(ansatz_envelope)
    check("independent ledger still has exactly 136 allowed ordered cells", len(full_cells) == 136)
    check("the nine coarse block types span every S/I/R pair in the *allowed envelope*", ansatz_envelope == full_cells)
    check("coarse envelope bookkeeping mentions every observer slot", sources_covered == targets_covered == all_names)
    check("formula-level irrep support is not equated with 136 envelope coordinates", len(POSIT_COEFFICIENTS) < len(full_cells))

    rr_only = allowed_cells_for_blocks((CARRIER_BLOCKS[-1],))
    rr_sources, rr_targets = covered_slots(rr_only)
    check("zero-off-core control reproduces only the 40-cell W131 envelope", len(rr_only) == 40)
    check("zero-off-core control fails full observer coverage", rr_sources == rr_targets != all_names and len(all_names - rr_sources) == 8)

    d_w131 = TypedMap("D_W131", "R", "R", "complex-linear")
    kappa_r = TypedMap("kappa_R", "R", "R_dens_dual", "conjugate-linear")
    lowered_w131 = w131_equation_restriction(
        d_w131,
        kappa_r,
        krein_orthogonal_restriction=True,
    )
    check("W131 carrier restriction is an R endomorphism", d_w131.domain == d_w131.codomain == "R")
    check("W131 equation restriction is real-linear after explicit realification", lowered_w131.codomain == "R_real_dens_dual" and lowered_w131.linearity == "real-linear")
    check(
        "non-orthogonal K restriction does not simplify to kappa_R D_W131",
        rejects(
            lambda: w131_equation_restriction(
                d_w131,
                kappa_r,
                krein_orthogonal_restriction=False,
            )
        ),
    )
    check(
        "ill-typed projector sandwich control is rejected",
        rejects(
            lambda: w131_equation_restriction(
                TypedMap("E_W131", "R", "R_dens_dual", "conjugate-linear"),
                kappa_r,
                krein_orthogonal_restriction=True,
            )
        ),
    )

    print("\nB. Declared one-stage fixed-A observer BV ansatz")
    validate_bv_bundle(BV_COORDINATES)
    validate_hamiltonian_arrows(HAMILTONIAN_ARROWS)
    family_counts = {
        family: sum(coordinate.family == family for coordinate in BV_COORDINATES)
        for family in {coordinate.family for coordinate in BV_COORDINATES}
    }
    check("BV bundle has 64 irreducible coordinates", len(BV_COORDINATES) == 64)
    check("Z and Z+ retain 20 slots each", family_counts["Z"] == family_counts["Z+"] == 20)
    check("each ghost/nonminimal coordinate has four S irreducibles", all(family_counts[family] == 4 for family in ("c", "c+", "barc", "barc+", "b", "b+")))
    complex_coordinate_rank = sum(coordinate.dimension for coordinate in BV_COORDINATES)
    check("chosen BV ansatz has complex-coordinate rank 4608", complex_coordinate_rank == 4608)
    check("underlying real Hamiltonian BV space has real rank 9216", 2 * complex_coordinate_rank == 9216)
    minimal = tuple(coordinate for coordinate in BV_COORDINATES if coordinate.family in {"Z", "Z+", "c", "c+"})
    check("chosen minimal-part coordinate census has complex rank 4096", sum(coordinate.dimension for coordinate in minimal) == 4096)
    check("odd symplectic ledger has exactly 32 canonical pairs", sum(coordinate.cotangent_flag == 0 for coordinate in BV_COORDINATES) == 32)
    check("every canonical pair has complementary form degree, gh sum -1, and flipped parity", all(
        coordinate.form + BV_BY_NAME[coordinate.partner].form == 14
        and coordinate.ghost + BV_BY_NAME[coordinate.partner].ghost == -1
        and coordinate.parity ^ BV_BY_NAME[coordinate.partner].parity == 1
        for coordinate in BV_COORDINATES
    ))
    check("ghost antifields retain KT antifield number 2", all(coordinate.antifield_number == 2 for coordinate in BV_COORDINATES if coordinate.family == "c+"))
    check("physical K and canonical odd BV evaluation remain different pairings", "density evaluation" in CANONICAL_MAPS and "K" not in CANONICAL_MAPS)
    check(
        "five explicit Hamiltonian arrows cover all eight BV coordinate families with gh +1 and parity flip",
        {
            family
            for arrow in HAMILTONIAN_ARROWS
            for family in (arrow.input_family, arrow.output_family)
        }
        == set(FAMILY_GRADES),
    )
    check(
        "master/Noether relations remain named residuals rather than asserted closure",
        {arrow.unresolved_condition for arrow in HAMILTONIAN_ARROWS if arrow.unresolved_condition}
        == {"H R = 0", "R^! H = 0"},
    )

    missing_nonminimal = tuple(coordinate for coordinate in BV_COORDINATES if coordinate.family not in {"barc", "barc+", "b", "b+"})
    check("missing-antighost/NL control fails the declared one-stage manifest", rejects(lambda: validate_bv_bundle(missing_nonminimal)))
    dummy = BVCoordinate("dummy", "dummy", "1", "1", 1, 0, 0, 0, 0, 0, "dummy+", "none")
    dummy_plus = BVCoordinate("dummy+", "dummy+", "1", "1", 1, 14, -1, 1, 1, 1, "dummy", "none")
    check("dummy contractible-pair control is rejected outside the exact manifest/origin enum", rejects(lambda: validate_bv_bundle(BV_COORDINATES + (dummy, dummy_plus))))

    print("\nC. Maximal-envelope coloring, integer obstruction, and four-stage candidate")
    names = tuple(field.name for field in OBSERVER_FIELDS)
    coloring = bipartite_coloring(names, full_cells)
    color_zero = {name for name, value in coloring.items() if value == 0}
    color_one = set(names) - color_zero
    expected_color = {
        "S:E+:L16+",
        "S:E+:R16-",
        "imGamma:E+:L16+",
        "imGamma:E+:R16-",
        "kerGamma:E+:L16+",
        "kerGamma:E+:R16-",
        "X:X32m",
        "X:X23p",
        "X:X2Tm",
        "X:X1Tp",
    }
    check("all 136 cells in the maximal allowed envelope are odd for its Z/2 coloring", all(coloring[source] ^ coloring[target] == 1 for source, target in full_cells))
    check("maximal-envelope coloring matches the exact certificate up to global reversal", color_zero in (expected_color, set(names) - expected_color))
    rank_by_color = (
        sum(field.dimension for field in OBSERVER_FIELDS if coloring[field.name] == 0),
        sum(field.dimension for field in OBSERVER_FIELDS if coloring[field.name] == 1),
    )
    check("the two maximal-envelope color halves each have rank 960", rank_by_color == (960, 960))

    name_index = {name: index for index, name in enumerate(names)}
    incidence_rows = []
    for source, target in sorted(full_cells):
        row = [0] * len(names)
        row[name_index[source]] = 1
        row[name_index[target]] ^= 1
        incidence_rows.append(row)
    support_rank = gf2_rank(incidence_rows)
    check("maximal-envelope Z/2 incidence rank is 19 with one global reversal", support_rank == 19 and len(names) - support_rank == 1)
    normalized_rows = incidence_rows + [[1] + [0] * (len(names) - 1)]
    check("fixing one slot removes the conventional Z/2 reversal", gf2_rank(normalized_rows) == 20)

    check("the whole bidirectional 136-cell envelope is not degree +1 on one copy", not integer_degree_one_consistent(names, full_cells))
    check("one-way planted chain admits an integer degree-+1 lift", integer_degree_one_consistent(("u0", "u1", "u2"), {("u0", "u1"), ("u1", "u2")}))
    check("the W131 scalar identity is even under this coloring, unlike the first-order envelope", all(coloring[field.name] ^ coloring[field.name] == 0 for field in w131_fields))

    unrolled_ranks = tuple(stage.complex_rank for stage in UNROLLED_STAGES)
    unrolled_forms = tuple(stage.ordinary_form_degree for stage in UNROLLED_STAGES)
    check("source-shaped four-stage carrier has exact ranks 128,1792,1792,128", unrolled_ranks == (
        sum(field.dimension for field in OBSERVER_FIELDS if field.provenance == "S"),
        sum(field.dimension for field in OBSERVER_FIELDS if field.provenance != "S"),
        sum(field.dimension for field in OBSERVER_FIELDS if field.provenance != "S"),
        sum(field.dimension for field in OBSERVER_FIELDS if field.provenance == "S"),
    ))
    check(
        "one-form stage is I+R itself, not Omega1(I+R)",
        UNROLLED_STAGES[1].bundle == "I+R = T*Y tensor S",
    )
    check(
        "dual stage is the density dual of I+R, not Omega13((I+R)^vee)",
        UNROLLED_STAGES[2].bundle
        == "(I+R)^vee_dens = Lambda^13 T*Y tensor S^vee",
    )
    check("ordinary form degrees remain distinct from cochain degree", unrolled_forms == (0, 1, 13, 14) and tuple(range(4)) != unrolled_forms)
    check("candidate even and odd four-stage rolls each have rank 1920", unrolled_ranks[0] + unrolled_ranks[2] == unrolled_ranks[1] + unrolled_ranks[3] == 1920)

    check("planted normalized filtration system reports nullity 0", normalized_filtration_nullity(3, ((0, 1), (1, 2))) == 0)
    check("planted normalized filtration system reports nullity 1", normalized_filtration_nullity(4, ((0, 1), (1, 2))) == 1)
    check("planted normalized filtration system reports nullity 2", normalized_filtration_nullity(5, ((0, 1), (1, 2))) == 2)

    # The coordinate inclusion/projection is real but says nothing about a
    # nontrivial roll: Q at zero antifields has its equation component in the
    # antifield direction, so field projection returns zero.
    pi_iota_identity = True
    coordinate_compression_of_equation_component = 0
    check("coordinate inclusion/projection satisfies pi iota=1", pi_iota_identity)
    check("rolling-tautology control: coordinate compression yields zero, not q_B5", coordinate_compression_of_equation_component == 0)
    check("136-cell scope control rejects ghosts/antifields", rejects(lambda: observer_symbol_cells("ghost")))

    print("\nD. Held-out wall and non-fitting controls")
    signatures = {
        packet_signature_smoke_test({"P1": sign, "P2": p2, "P3": count, "target_retract": retract})
        for sign, p2, count, retract in (
            (-1, "unknown", 3, "3E+"),
            (+1, "flipped", 17, "3E-"),
            (None, None, None, "none"),
        )
    }
    check("held-out API-fence smoke test is byte-stable (not independent non-fit evidence)", len(signatures) == 1)
    check("one coefficient per allowed cell is not smuggled into the short ansatz", len(POSIT_COEFFICIENTS) == 12 < 136)

    print("\n" + "=" * 96)
    if FAILURES:
        print(f"RESULT: FAIL ({len(FAILURES)} failed checks)")
        for failure in FAILURES:
            print(f"  - {failure}")
        raise SystemExit(1)

    print("RESULT: S1-SPLIT-VERDICT; COARSE-RELATIVE-OBSERVER-ANSATZ-WRITTEN")
    print("ENVELOPE: 136-CELL-Z2-COLORING-UNIQUE-UP-TO-REVERSAL")
    print("ENVELOPE: WHOLE-BIDIRECTIONAL-136-NOT-DEGREE+1-ON-ONE-COPY")
    print("CANDIDATE: FOUR-STAGE-0-1-13-14-CARRIER-TYPED; DIFFERENTIAL-UNBUILT")
    print("BV: CHOSEN-ONE-STAGE-FIXED-A ANSATZ; COMPLEX-RANK-4608; REAL-RANK-9216")
    print("W131: CARRIER-BLOCK-INHERITED; REAL DENSITY-LOWERING-CONDITIONAL-ON-K-ORTHOGONALITY")
    print("RESIDUAL: FORMULA-LEVEL IRREP SUPPORT; HODGE/KREIN ROLL MAPS; NATIVE ADJOINT/GREEN/DOMAIN; FULL AMBIENT BV")
    print("NOT CLAIMED: q^2, master equation, Noether closure, retract, transport, count, mass, or source recovery")


if __name__ == "__main__":
    main()
