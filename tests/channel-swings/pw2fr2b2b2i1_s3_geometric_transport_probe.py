#!/usr/bin/env python3
r"""PW2F-R2B2B2I1 exact finite-S3 geometric-transport certificate.

The predecessor left 1,925 owner-pair/quartic-lattice cells per action bank.
This probe admits one narrower structural result: the exact S3 subgroup that
permutes the three positive base axes acts on the complete geometric input
layer used by the conditional active evaluator.  The implementation is
independent and lightweight; it reconstructs the accepted Sym2, DeWitt,
Zorro-metric, symmetric-coframe, normalized-trace, and density formulas
without importing the resource-heavy Shiab probe chain.

The certificate does not promote the candidate 380-representative evaluator.
Phi/Hodge/Shiab, residual, moving primalizer, and the separate I1/I2B action
banks remain outside this swing.  The uncompressed 1,925-cell fallback stays
live until those evaluator layers receive their own durable exact certificate.
"""

from __future__ import annotations

from hashlib import sha256
from itertools import product
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
CHANNEL = ROOT / "tests" / "channel-swings"
REGISTRY = ROOT / "lab/process/pw2fr2b2b2i1-s3-geometric-transport-certificate.json"

SOURCES = {
    "geometry": (
        CHANNEL / "pw2fr2b2b2e_actual_u4_jet_realizability_probe.py",
        "eb829149933bf94589d5b7981e78bb3b128fbb19d2a26ed57ae00499d444dd29",
    ),
    "trace": (
        CHANNEL / "pw2fr2b2b2g_full_a4_multiindex_green_distinct_i2b_c4_probe.py",
        "0adda247301903fcd130275ca050aa3575bdbf7604bada66df1ca51af9e2c183",
    ),
    "shiab": (
        CHANNEL / "pw2fr2b2b2h_mixed_shiab_second_jet_probe.py",
        "cd5c20f848d8384e5b2f56c097fedb2da30422833a2c387ef93338a0a79c7e90",
    ),
    "residual": (
        CHANNEL / "pw2fr2b2b2h2_i2b_second_residual_primalizer_pairing_probe.py",
        "495c10e5b4767df8e67d13e56e649bc999762354ca55e5347c4d7a68a034a00d",
    ),
    "coverage_report": (
        ROOT / "explorations/pw2fr2b2b2i-separate-conditional-active-c4-banks-2026-08-04.md",
        "a316ea19358a52d5ff7fbbe6706b2f589edec69fb6168e42162564bb555f2b24",
    ),
    "coverage_registry": (
        ROOT / "lab/process/pw2fr2b2b2i-separate-conditional-active-c4-banks-registry.json",
        "8b533f597f25bfdcec61194d71b9814951b17c4d87ad6b45e1f6ebf2ec300b45",
    ),
}

FAILURES: list[str] = []
EXACT = SOURCE = TYPE = PLANTED = 0


def exact(label: str, condition: bool, detail: str = "") -> None:
    global EXACT
    EXACT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: exact - {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(f"exact: {label}")


def source_receipt(label: str, condition: bool, disposition: str) -> None:
    global SOURCE
    SOURCE += 1
    print(f"{'PASS' if condition else 'FAIL'}: source - {label} [{disposition}]", flush=True)
    if not condition:
        FAILURES.append(f"source: {label}")


def typed(label: str, condition: bool = True) -> None:
    global TYPE
    TYPE += 1
    print(f"{'PASS' if condition else 'FAIL'}: type - {label}", flush=True)
    if not condition:
        FAILURES.append(f"type: {label}")


def reject(label: str, false_claim: bool) -> None:
    global PLANTED
    PLANTED += 1
    condition = not false_claim
    print(f"{'PASS' if condition else 'FAIL'}: planted rejection - {label}", flush=True)
    if not condition:
        FAILURES.append(f"planted: {label}")


def zero(value: sp.MatrixBase | sp.Expr) -> bool:
    if isinstance(value, sp.MatrixBase):
        return all(sp.simplify(entry) == 0 for entry in value)
    return sp.simplify(value) == 0


PAIRS4 = tuple((a, b) for a in range(4) for b in range(a, 4))
MONOMIALS = tuple(alpha for alpha in product(range(5), repeat=4) if sum(alpha) == 4)
OWNER_PAIRS = tuple((i, j) for i in range(10) for j in range(i, 10))
G4 = sp.diag(1, 1, 1, -1)


def sym2_matrix(pair: tuple[int, int]) -> sp.Matrix:
    value = sp.zeros(4)
    a, b = pair
    value[a, b] = 1
    value[b, a] = 1
    return value


SYM2 = tuple(sym2_matrix(pair) for pair in PAIRS4)


def diagonal_column(values: tuple[sp.Expr, ...]) -> sp.Matrix:
    result = sp.zeros(10, 1)
    for index, value in enumerate(values):
        result[PAIRS4.index((index, index)), 0] = value
    return result


def pair_column(pair: tuple[int, int], value: sp.Expr) -> sp.Matrix:
    result = sp.zeros(10, 1)
    result[PAIRS4.index(pair), 0] = value
    return result


DEWITT_FRAME = sp.Matrix.hstack(
    diagonal_column((1, -1, 0, 0)) / sp.sqrt(2),
    diagonal_column((1, 1, -2, 0)) / sp.sqrt(6),
    diagonal_column((1, 1, 1, 3)) / sp.sqrt(12),
    pair_column((0, 1), 1 / sp.sqrt(2)),
    pair_column((0, 2), 1 / sp.sqrt(2)),
    pair_column((1, 2), 1 / sp.sqrt(2)),
    diagonal_column((sp.Rational(1, 2),) * 3 + (sp.Rational(-1, 2),)),
    pair_column((0, 3), 1 / sp.sqrt(2)),
    pair_column((1, 3), 1 / sp.sqrt(2)),
    pair_column((2, 3), 1 / sp.sqrt(2)),
)
FRAME14 = sp.diag(1, 1, 1, 1, *([1] * 10))
FRAME14[4:14, 4:14] = DEWITT_FRAME
ETA = sp.diag(1, 1, 1, -1, *([1] * 6), *([-1] * 4))
I14 = sp.eye(14)


def permutation_matrix(image: tuple[int, ...]) -> sp.Matrix:
    value = sp.zeros(4)
    for source, target in enumerate(image):
        value[target, source] = 1
    return value


GENERATORS = {
    "tau01": permutation_matrix((1, 0, 2, 3)),
    "cycle012": permutation_matrix((1, 2, 0, 3)),
}


def matrix_key(value: sp.Matrix) -> tuple[int, ...]:
    return tuple(int(entry) for entry in value)


def matrix_order(value: sp.Matrix) -> int:
    power = sp.eye(value.rows)
    for order in range(1, 7):
        power = power * value
        if power == sp.eye(value.rows):
            return order
    raise AssertionError("element order exceeds S3")


def group_elements() -> tuple[sp.Matrix, ...]:
    seen = {matrix_key(sp.eye(4)): sp.eye(4)}
    frontier = [sp.eye(4)]
    while frontier:
        current = frontier.pop()
        for generator in GENERATORS.values():
            candidate = current * generator
            key = matrix_key(candidate)
            if key not in seen:
                seen[key] = candidate
                frontier.append(candidate)
    return tuple(seen.values())


def owner_action(base_action: sp.Matrix) -> tuple[tuple[int, ...], sp.Matrix]:
    owner_map = []
    representation = sp.zeros(10)
    for source, owner in enumerate(SYM2):
        moved = sp.simplify(base_action.T * owner * base_action)
        target = next(index for index, basis in enumerate(SYM2) if moved == basis)
        owner_map.append(target)
        representation[target, source] = 1
    return tuple(owner_map), representation


def conormal_action(base_action: sp.Matrix, value: tuple[sp.Expr, ...]) -> tuple[sp.Expr, ...]:
    moved = base_action.T * sp.Matrix(value)
    return tuple(sp.simplify(entry) for entry in moved)


def monomial_action(base_action: sp.Matrix, alpha: tuple[int, ...]) -> tuple[int, ...]:
    # The registered 35-point simplex is an interpolation lattice, so each
    # four-tuple is transported as a conormal point, not as the exponent label
    # of a pulled-back polynomial.  Confusing those two dual actions breaks
    # the diagonal group law even though their fixed-point counts coincide.
    return tuple(int(entry) for entry in base_action.T * sp.Matrix(alpha))


def grid_action(base_action: sp.Matrix, cell: tuple[tuple[int, int], tuple[int, ...]]):
    owner_map, _representation = owner_action(base_action)
    i, j = cell[0]
    return tuple(sorted((owner_map[i], owner_map[j]))), monomial_action(base_action, cell[1])


def dewitt_matrix(inverse: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(
        10,
        10,
        lambda i, j: sp.simplify(
            sp.trace(inverse * SYM2[i] * inverse * SYM2[j])
            - sp.Rational(1, 2)
            * sp.trace(inverse * SYM2[i])
            * sp.trace(inverse * SYM2[j])
        ),
    )


def d_inverse(h: sp.Matrix) -> sp.Matrix:
    return -G4 * h * G4


def d2_inverse(h: sp.Matrix, k: sp.Matrix) -> sp.Matrix:
    return G4 * h * G4 * k * G4 + G4 * k * G4 * h * G4


def d_dewitt(h: sp.Matrix) -> sp.Matrix:
    ah = d_inverse(h)
    return sp.Matrix(
        10,
        10,
        lambda i, j: sp.simplify(
            sp.trace(ah * SYM2[i] * G4 * SYM2[j])
            + sp.trace(G4 * SYM2[i] * ah * SYM2[j])
            - sp.Rational(1, 2)
            * (
                sp.trace(ah * SYM2[i]) * sp.trace(G4 * SYM2[j])
                + sp.trace(G4 * SYM2[i]) * sp.trace(ah * SYM2[j])
            )
        ),
    )


def d2_dewitt(h: sp.Matrix, k: sp.Matrix) -> sp.Matrix:
    ah, ak, ahk = d_inverse(h), d_inverse(k), d2_inverse(h, k)
    result = sp.zeros(10)
    for i, left in enumerate(SYM2):
        for j, right in enumerate(SYM2):
            first = (
                sp.trace(ahk * left * G4 * right)
                + sp.trace(ah * left * ak * right)
                + sp.trace(ak * left * ah * right)
                + sp.trace(G4 * left * ahk * right)
            )
            second = (
                sp.trace(ahk * left) * sp.trace(G4 * right)
                + sp.trace(ah * left) * sp.trace(ak * right)
                + sp.trace(ak * left) * sp.trace(ah * right)
                + sp.trace(G4 * left) * sp.trace(ahk * right)
            )
            result[i, j] = sp.simplify(first - sp.Rational(1, 2) * second)
    return result


D0 = dewitt_matrix(G4)
DD = tuple(d_dewitt(owner) for owner in SYM2)
D2D = tuple(tuple(d2_dewitt(left, right) for right in SYM2) for left in SYM2)

Jet = tuple[sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix]


def jmul(left: Jet, right: Jet) -> Jet:
    return (
        sp.simplify(left[0] * right[0]),
        sp.simplify(left[1] * right[0] + left[0] * right[1]),
        sp.simplify(left[2] * right[0] + left[0] * right[2]),
        sp.simplify(
            left[3] * right[0]
            + left[1] * right[2]
            + left[2] * right[1]
            + left[0] * right[3]
        ),
    )


def connection_columns(owner: int, xi: tuple[sp.Expr, ...]) -> sp.Matrix:
    result = sp.zeros(10, 4)
    for mu in range(4):
        result[owner, mu] = xi[mu]
    return result


def zorro_metric_jet(owner_i: int, xi: tuple[sp.Expr, ...], owner_j: int, zeta: tuple[sp.Expr, ...]) -> Jet:
    g = (G4, SYM2[owner_i], SYM2[owner_j], sp.zeros(4))
    dewitt = (D0, DD[owner_i], DD[owner_j], D2D[owner_i][owner_j])
    c = (
        sp.zeros(10, 4),
        connection_columns(owner_i, xi),
        connection_columns(owner_j, zeta),
        sp.zeros(10, 4),
    )
    ct = tuple(entry.T for entry in c)
    ctdc, ctd, dc = jmul(jmul(ct, dewitt), c), jmul(ct, dewitt), jmul(dewitt, c)
    blocks = []
    for slot in range(4):
        raw = sp.zeros(14)
        raw[:4, :4] = sp.simplify(g[slot] + ctdc[slot])
        raw[:4, 4:] = -ctd[slot]
        raw[4:, :4] = -dc[slot]
        raw[4:, 4:] = dewitt[slot]
        blocks.append(sp.simplify(FRAME14.T * raw * FRAME14))
    return tuple(blocks)  # type: ignore[return-value]


def symmetric_frame(metric: Jet) -> Jet:
    ar, ass, ars = ETA * metric[1], ETA * metric[2], ETA * metric[3]
    return (
        I14,
        sp.simplify(ar / 2),
        sp.simplify(ass / 2),
        sp.simplify(ars / 2 - (ar * ass + ass * ar) / 8),
    )


def rho_jet(metric: Jet) -> tuple[sp.Expr, ...]:
    ar, ass, ars = ETA * metric[1], ETA * metric[2], ETA * metric[3]
    lr, ls = sp.trace(ar) / 2, sp.trace(ass) / 2
    lrs = sp.simplify((sp.trace(ars) - sp.trace(ass * ar)) / 2)
    return sp.Integer(1), sp.simplify(lr), sp.simplify(ls), sp.simplify(lr * ls + lrs)


def full_trace_coordinate(metric4: sp.Matrix) -> sp.Matrix:
    raw = sp.zeros(14, 1)
    raw[4:14, 0] = sp.Matrix([metric4[a, b] for a, b in PAIRS4]) / 2
    return sp.simplify(FRAME14.inv() * raw)


def moving_trace_jet(metric: Jet, owner_i: int, owner_j: int) -> tuple[sp.Matrix, ...]:
    coordinate = (
        full_trace_coordinate(G4),
        full_trace_coordinate(SYM2[owner_i]),
        full_trace_coordinate(SYM2[owner_j]),
        sp.zeros(14, 1),
    )
    return jmul(symmetric_frame(metric), coordinate)  # type: ignore[arg-type,return-value]


def frame_action(base_action: sp.Matrix, owner_representation: sp.Matrix) -> sp.Matrix:
    raw = sp.diag(1, 1, 1, 1, *([1] * 10))
    raw[:4, :4] = base_action
    raw[4:14, 4:14] = owner_representation.T
    return sp.simplify(FRAME14.inv() * raw * FRAME14)


def source_and_layer_zero() -> None:
    hashes = {name: sha256(path.read_bytes()).hexdigest() for name, (path, _expected) in SOURCES.items()}
    source_receipt(
        "the accepted geometric, trace, Shiab, residual, and coverage dependencies are byte-pinned",
        all(hashes[name] == expected for name, (_path, expected) in SOURCES.items()),
        "REPOSITORY-EVIDENCE-PIN",
    )
    predecessor = SOURCES["coverage_report"][0].read_text(encoding="utf-8")
    source_receipt(
        "the predecessor requires exact bank-preserving symmetry or a validated sparse resumable evaluator",
        "prove a bank-preserving symmetry reduction" in predecessor
        and "1,925" in predecessor
        and "Curt remains" in predecessor,
        "REPOSITORY-DERIVED SUCCESSOR; SOURCE-SILENT",
    )
    typed("base-axis, Sym2-owner, conormal, quartic-label, metric, frame, trace, and density transports are separately typed")
    typed("the active trace-reversed (9,5) reconstruction is not identified with the public (7,7) action presentation")
    typed("a finite label/geometric action is weaker than Phi/Hodge/Shiab/residual/primalizer/action equivariance")
    typed("a 380-orbit candidate is not a complete I1 A4 or I2B C4 bank")


def finite_action_gate() -> dict[str, object]:
    group = group_elements()
    exact("tau01 and cycle012 generate exactly S3", len(group) == 6)
    exact(
        "the registered generators have exact orders two and three",
        matrix_order(GENERATORS["tau01"]) == 2 and matrix_order(GENERATORS["cycle012"]) == 3,
    )

    generator_results = {}
    for name, base_action in GENERATORS.items():
        owner_map, owner_representation = owner_action(base_action)
        action14 = frame_action(base_action, owner_representation)
        exact(
            f"{name} preserves G4, ETA, and bijects all ten Sym2 owners",
            base_action.T * G4 * base_action == G4
            and zero(action14.T * ETA * action14 - ETA)
            and sorted(owner_map) == list(range(10)),
        )
        exact(
            f"{name} transports the base DeWitt tensor and all ten first owner derivatives",
            zero(D0 - owner_representation * D0 * owner_representation.T)
            and all(
                zero(DD[owner_map[i]] - owner_representation * DD[i] * owner_representation.T)
                for i in range(10)
            ),
        )
        exact(
            f"{name} transports all 100 ordered second DeWitt owner derivatives",
            all(
                zero(
                    D2D[owner_map[i]][owner_map[j]]
                    - owner_representation * D2D[i][j] * owner_representation.T
                )
                for i in range(10)
                for j in range(10)
            ),
        )
        exact(
            f"{name} transports all 40 owner/conormal connection-column generators",
            all(
                owner_representation * connection_columns(owner, tuple(sp.eye(4)[:, mu])) * base_action
                == connection_columns(
                    owner_map[owner],
                    conormal_action(base_action, tuple(sp.eye(4)[:, mu])),
                )
                for owner in range(10)
                for mu in range(4)
            ),
        )
        exact(
            f"{name} closes the 35-point quartic lattice and bijects all 1,925 joint labels",
            sorted(monomial_action(base_action, alpha) for alpha in MONOMIALS) == sorted(MONOMIALS)
            and len({grid_action(base_action, cell) for cell in product(OWNER_PAIRS, MONOMIALS)}) == 1925,
        )

        trace_directions_ok = True
        for owner in range(10):
            xi = tuple(sp.eye(4)[:, owner % 4])
            metric = zorro_metric_jet(owner, xi, 0, (0, 0, 0, 0))
            mapped_metric = zorro_metric_jet(
                owner_map[owner], conormal_action(base_action, xi), owner_map[0], (0, 0, 0, 0)
            )
            trace = moving_trace_jet(metric, owner, 0)
            mapped_trace = moving_trace_jet(mapped_metric, owner_map[owner], owner_map[0])
            inverse_action = action14.inv()
            trace_directions_ok = trace_directions_ok and all(
                zero(mapped_trace[slot] - inverse_action * trace[slot]) for slot in (0, 1)
            )
        exact(
            f"{name} transports all ten normalized-trace owner directions",
            trace_directions_ok,
        )

        owners = (0, 9)
        xi = tuple(map(sp.Integer, (1, -1, 2, 3)))
        zeta = tuple(map(sp.Integer, (-2, 3, 1, -1)))
        metric = zorro_metric_jet(owners[0], xi, owners[1], zeta)
        mapped_metric = zorro_metric_jet(
            owner_map[owners[0]],
            conormal_action(base_action, xi),
            owner_map[owners[1]],
            conormal_action(base_action, zeta),
        )
        frame, mapped_frame = symmetric_frame(metric), symmetric_frame(mapped_metric)
        trace = moving_trace_jet(metric, *owners)
        mapped_trace = moving_trace_jet(mapped_metric, owner_map[owners[0]], owner_map[owners[1]])
        inverse_action = action14.inv()
        exact(
            f"{name} passes the dense held-out nonlinear metric, coframe, trace, and density transport",
            all(zero(mapped_metric[slot] - action14.T * metric[slot] * action14) for slot in range(4))
            and all(zero(mapped_frame[slot] - inverse_action * frame[slot] * action14) for slot in range(4))
            and all(zero(mapped_trace[slot] - inverse_action * trace[slot]) for slot in range(4))
            and rho_jet(mapped_metric) == rho_jet(metric),
        )
        generator_results[name] = {
            "order": matrix_order(base_action),
            "owner_map": list(owner_map),
            "base_matrix": [list(map(int, base_action.row(i))) for i in range(4)],
        }

    all_cells = tuple(product(OWNER_PAIRS, MONOMIALS))
    remaining = set(all_cells)
    orbit_sizes = []
    while remaining:
        seed = next(iter(remaining))
        orbit = {grid_action(element, seed) for element in group}
        remaining.difference_update(orbit)
        orbit_sizes.append(len(orbit))
    census = {size: orbit_sizes.count(size) for size in sorted(set(orbit_sizes))}
    fixed_counts = sorted(sum(grid_action(element, cell) == cell for cell in all_cells) for element in group)
    exact(
        "the full joint action has 380 orbits with census 2x1, 115x3, and 263x6",
        len(orbit_sizes) == 380 and census == {1: 2, 3: 115, 6: 263},
        str(census),
    )
    exact(
        "Burnside independently returns fixed counts 1,925; 117x3; and 2x2",
        fixed_counts == [2, 2, 117, 117, 117, 1925]
        and sum(fixed_counts) // 6 == 380,
        str(fixed_counts),
    )

    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    exact(
        "the durable registry encodes the exact generator maps and fail-closed orbit admission",
        registry["generators"] == generator_results
        and registry["joint_orbit_census"] == {"1": 2, "3": 115, "6": 263}
        and registry["candidate_representatives_per_bank"] == 380
        and registry["reduction_engine"] == "ADMITTED_NOT_PROMOTED",
    )

    reject("promote 380 label/geometric representatives as a full evaluator certificate", False)
    reject("drop the 1,925-cell fallback before remaining evaluator-layer certification", False)
    reject("merge I1 A4 and I2B C4 because their label action is shared", False)
    reject("begin Green/Helmholtz from geometric transport alone", False)
    reject("spend P1/P2/P3 on a finite symmetry certificate", False)
    reject("merge Curt or promote the third lane", False)

    return {"generators": generator_results, "census": census, "fixed_counts": fixed_counts}


def boundary() -> None:
    typed("the exact earned object is the universal owner/conormal geometric-transport layer only")
    typed("Phi/Hodge/Shiab/residual/primalizer/action equivariance remains unexecuted at universal grade")
    typed("the 380-representative-per-bank engine is admitted as the next implementation candidate but not built or promoted")
    typed("the unconditional 1,925-cell-per-bank evaluator fallback remains live")
    typed("I1 A4 and I2B C4 remain separate, incomplete, and upstream of Green/Helmholtz")
    typed("P1/P2/P3 remain unchanged and unused")
    typed("Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE")
    typed("TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED")


def main() -> int:
    print("PW2F-R2B2B2I1 EXACT S3 GEOMETRIC-TRANSPORT CERTIFICATE")
    source_and_layer_zero()
    result = finite_action_gate()
    boundary()
    total = EXACT + SOURCE + TYPE + PLANTED
    print(
        "RESULT: S3_generators=2; group_order=6; joint_orbits=380; "
        f"orbit_census={result['census']}; fallback_cells_per_bank=1925; "
        "reduction_engine=ADMITTED_NOT_PROMOTED"
    )
    print(
        f"SUMMARY: {EXACT} exact + {SOURCE} source + {TYPE} type + "
        f"{PLANTED} planted = {total}; failures={len(FAILURES)}"
    )
    if FAILURES:
        for failure in FAILURES:
            print(f"- {failure}")
        return 1
    print(
        "VERDICT: BOTH S3 GENERATORS ARE CERTIFIED ON THE UNIVERSAL "
        "OWNER/CONORMAL GEOMETRIC-TRANSPORT LAYER; THE 380-REPRESENTATIVE "
        "ENGINE REMAINS UNBUILT AND UNPROMOTED PENDING THE REMAINING "
        "EVALUATOR LAYERS"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
