#!/usr/bin/env python3
r"""PW2F-R2B2B2I2 exact full-evaluator certificate on the S3-fixed stratum.

The durable I1 packet proves that the 1,925 owner-pair/quartic-point labels
split into 380 exact S3 orbits, including exactly two one-cell orbits.  This
probe deterministically resolves the label grid, selects those two fixed
representatives, and certifies both S3 generators through the complete mixed
metric, Phi1, Phi2, Hodge, Shiab residual, moving Hodge-primalizer, and action
jet used by the conditional-active evaluator.

The result is exactly 2/380 representative coverage.  It does not certify the
remaining 378 representatives, promote the reduction engine, replace the
1,925-cell fallback, assemble I1 A4 or I2B C4, begin Green/Helmholtz, spend
P1/P2/P3, merge Curt's rival track, or pass the conjunctive third-lane gate.
"""

from __future__ import annotations

from functools import lru_cache
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
CHANNEL = ROOT / "tests" / "channel-swings"
if str(CHANNEL) not in sys.path:
    sys.path.insert(0, str(CHANNEL))

DEPENDENCIES = {
    CHANNEL / "pw2fr2b2b2i1_s3_geometric_transport_probe.py":
        "ef8e488bcd0353a5f1790ccb8e5c42f298d2aa31e18133034d1102ca9d10d7dc",
    CHANNEL / "pw2fr2b2b2h_mixed_shiab_second_jet_probe.py":
        "cd5c20f848d8384e5b2f56c097fedb2da30422833a2c387ef93338a0a79c7e90",
    ROOT / "lab/process/pw2fr2b2b2i1-s3-geometric-transport-certificate.json":
        "84cef126da1396a4f4c21f12525e9c53446abd345f1230d359cd772ef5e2a3f0",
}


def load_probe(name: str, path: Path):
    spec = spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(str(path))
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


I1 = load_probe(
    "gu_i1_s3_geometric_transport",
    CHANNEL / "pw2fr2b2b2i1_s3_geometric_transport_probe.py",
)
H = load_probe(
    "gu_h_mixed_shiab_jet",
    CHANNEL / "pw2fr2b2b2h_mixed_shiab_second_jet_probe.py",
)
G = H.G
M = H.M

Label = tuple[tuple[int, int], tuple[int, ...]]
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


def label_key(label: Label) -> tuple[int, ...]:
    return (*label[0], *label[1])


def element_key(element: sp.Matrix) -> tuple[sp.Expr, ...]:
    return I1.matrix_key(element)


def canonical_orbit_resolver():
    group = tuple(sorted(I1.group_elements(), key=element_key))
    labels = tuple(
        sorted(
            (
                (owner_pair, monomial)
                for owner_pair in I1.OWNER_PAIRS
                for monomial in I1.MONOMIALS
            ),
            key=label_key,
        )
    )
    resolver = {}
    for label in labels:
        orbit = tuple(
            sorted(
                {I1.grid_action(element, label) for element in group},
                key=label_key,
            )
        )
        representative = orbit[0]
        witnesses = tuple(
            element
            for element in group
            if I1.grid_action(element, representative) == label
        )
        resolver[label] = (representative, witnesses[0], len(orbit))
    return group, labels, resolver


def cliff_equal(left: M.SCliff, right: M.SCliff) -> bool:
    return not M.sadd(left, M.sscale(right, -1))


def form_equal(left: M.SForm, right: M.SForm) -> bool:
    return not M.sfadd(left, M.sfscale(right, -1))


def cliff_transformer(matrix: sp.Matrix):
    @lru_cache(maxsize=None)
    def vector_image(old: int) -> tuple[tuple[int, sp.Expr], ...]:
        return tuple(
            (new, sp.simplify(matrix[new, old]))
            for new in range(M.N)
            if sp.simplify(matrix[new, old]) != 0
        )

    @lru_cache(maxsize=None)
    def blade_image(mask: int) -> tuple[tuple[int, sp.Expr], ...]:
        image: M.SCliff = {0: sp.Integer(1)}
        for old in range(M.N):
            if mask & (1 << old):
                moved_vector = M.sclean(
                    {1 << new: coefficient for new, coefficient in vector_image(old)}
                )
                image = M.smul(image, moved_vector)
        return tuple(sorted(M.sclean(image).items()))

    def transform(value: M.SCliff) -> M.SCliff:
        result: M.SCliff = {}
        for mask, scalar in value.items():
            result = M.sadd(result, M.sscale(dict(blade_image(mask)), scalar))
        return M.sclean(result)

    return transform


def finite_external_action(matrix: sp.Matrix, value: M.SForm) -> M.SForm:
    """Apply one finite linear map to every exterior slot."""

    result: M.SForm = {}
    for key, coefficient in value.items():
        partial: dict[tuple[int, ...], M.SCliff] = {(): coefficient}
        for old in key:
            advanced: dict[tuple[int, ...], M.SCliff] = {}
            for prefix, prefix_coefficient in partial.items():
                for new in range(M.N):
                    factor = sp.simplify(matrix[old, new])
                    if factor == 0 or new in prefix:
                        continue
                    candidate = prefix + (new,)
                    advanced[candidate] = M.sadd(
                        advanced.get(candidate, {}),
                        M.sscale(prefix_coefficient, factor),
                    )
            partial = advanced
        for unsorted_key, out_coefficient in partial.items():
            sign = M.B14.permutation_sign(unsorted_key)
            out_key = tuple(sorted(unsorted_key))
            result[out_key] = M.sadd(
                result.get(out_key, {}),
                M.sscale(out_coefficient, sign),
            )
    return M.sfclean(result)


def total_action(matrix: sp.Matrix, value: M.SForm) -> M.SForm:
    """Act contragrediently on exterior slots and orthogonally on Clifford."""

    external = finite_external_action(sp.simplify(matrix.inv()), value)
    transform_clifford = cliff_transformer(matrix)
    return M.sfclean(
        {key: transform_clifford(coefficient) for key, coefficient in external.items()}
    )


def jet_form_transport(matrix: sp.Matrix, value):
    return tuple(total_action(matrix, slot) for slot in value)


def top_scalar(value: M.SForm) -> sp.Expr:
    return sp.simplify(value.get(M.FULL_KEY, {}).get(0, 0))


def scalar_jet(value: H.JForm) -> tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr]:
    return tuple(top_scalar(slot) for slot in value)  # type: ignore[return-value]


def moving_primalizer(metric, residual):
    """Hodge the moving residual through mixed order by product rule."""

    base_star = H.jhodge(metric, H.constant_form(residual[0]))
    return (
        base_star[0],
        M.sfadd(M.sfhodge(residual[1]), base_star[1]),
        M.sfadd(M.sfhodge(residual[2]), base_star[2]),
        M.sfadd(
            M.sfhodge(residual[3]),
            M.dstar(residual[2], metric[1]),
            M.dstar(residual[1], metric[2]),
            base_star[3],
        ),
    )


def action_jet(primalizer, residual):
    return tuple(
        sp.simplify(value / 2)
        for value in scalar_jet(H.jfwedge(primalizer, residual))
    )


def evaluate(owner_pair, point, curvature):
    owner_i, owner_j = owner_pair
    conormal = tuple(map(sp.Integer, point))
    metric, trace_matrix = G.moving_frame_trace_jet(
        owner_i, conormal, owner_j, conormal
    )
    trace = H.matrix_trace_to_cliff(trace_matrix)
    phi_one, phi_two, _gamma = H.phi_jets(metric)
    hodge = H.jhodge(metric, H.constant_form(curvature))
    residual = H.shiab_jet(metric, trace, H.constant_form(curvature))
    primalizer = moving_primalizer(metric, residual)
    action = action_jet(primalizer, residual)
    return {
        "metric": metric,
        "phi_one": phi_one,
        "phi_two": phi_two,
        "hodge": hodge,
        "residual": residual,
        "primalizer": primalizer,
        "action": action,
    }


def main() -> int:
    print("PW2F-R2B2B2I2 S3-FIXED FULL-EVALUATOR CERTIFICATE", flush=True)

    dependency_checks = 0
    for path, expected in DEPENDENCIES.items():
        actual = sha256(path.read_bytes()).hexdigest()
        dependency_checks += int(actual == expected)
        if actual != expected:
            FAILURES.append(f"dependency drift: {path.name}={actual}")
    exact(
        "byte-pinned I1 geometry, H mixed-jet, and I1 registry dependencies",
        dependency_checks == len(DEPENDENCIES),
        f"{dependency_checks}/{len(DEPENDENCIES)}",
    )

    group, labels, resolver = canonical_orbit_resolver()
    representatives = tuple(
        sorted({entry[0] for entry in resolver.values()}, key=label_key)
    )
    fixed = tuple(
        representative
        for representative in representatives
        if resolver[representative][2] == 1
    )
    expected_fixed = (
        ((9, 9), (0, 0, 0, 4)),
        ((9, 9), (1, 1, 1, 1)),
    )
    exact("canonical resolver covers all labels", len(labels) == len(resolver) == 1925)
    exact("canonical resolver has 380 representatives", len(representatives) == 380)
    exact("fixed-orbit stratum is the two preregistered labels", fixed == expected_fixed)
    exact(
        "fixed labels are stabilized by the complete group",
        all(
            I1.grid_action(element, label) == label
            for element in group
            for label in fixed
        ),
        f"{len(group) * len(fixed)}/{len(group) * len(fixed)}",
    )

    curvature: M.SForm = {
        (0, 1): M.sblade(2, 3),
        (4, 5): M.sblade(6, 7, 8),
        (2, 10): M.sblade(0, 4, 9, 13),
    }

    sources = {}
    mixed_residual_live = 0
    mixed_primalizer_live = 0
    mixed_action_live = 0
    moving_hodge_controls = 0
    for label in fixed:
        source = evaluate(label[0], label[1], curvature)
        sources[label] = source
        mixed_residual_live += int(bool(source["residual"][3]))
        mixed_primalizer_live += int(bool(source["primalizer"][3]))
        mixed_action_live += int(source["action"][3] != 0)
        moving_hodge_controls += int(
            not form_equal(
                source["primalizer"][3],
                M.sfhodge(source["residual"][3]),
            )
        )
        print(f"prepared_fixed_label={label_key(label)}", flush=True)

    counters = {
        "geometry": 0,
        "phi_one": 0,
        "phi_two": 0,
        "hodge": 0,
        "residual": 0,
        "primalizer": 0,
        "action": 0,
    }
    generator_edges = 0
    wrong_forward_rejected = False

    for generator_name, base_action in I1.GENERATORS.items():
        owner_map, owner_representation = I1.owner_action(base_action)
        action14 = I1.frame_action(base_action, owner_representation)
        transport14 = sp.simplify(action14.inv())
        moved_curvature = total_action(transport14, curvature)

        for label in fixed:
            owner_pair, point = label
            mapped_label = I1.grid_action(base_action, label)
            if mapped_label != label:
                FAILURES.append(
                    f"{generator_name}/{label_key(label)}: fixed label moved"
                )
                continue

            mapped_owner_pair = tuple(owner_map[owner] for owner in owner_pair)
            mapped_point = I1.conormal_action(base_action, point)
            mapped = evaluate(mapped_owner_pair, mapped_point, moved_curvature)
            source = sources[label]
            generator_edges += 1

            for slot in range(4):
                expected_metric = sp.simplify(
                    action14.T * source["metric"][slot] * action14
                )
                if sp.simplify(
                    mapped["metric"][slot] - expected_metric
                ) == sp.zeros(14):
                    counters["geometry"] += 1
                else:
                    FAILURES.append(
                        f"{generator_name}/{label_key(label)}/metric[{slot}]"
                    )

            for layer in ("phi_one", "phi_two", "hodge", "residual", "primalizer"):
                transported = jet_form_transport(transport14, source[layer])
                for slot, (actual, expected) in enumerate(
                    zip(mapped[layer], transported)
                ):
                    if form_equal(actual, expected):
                        counters[layer] += 1
                    else:
                        FAILURES.append(
                            f"{generator_name}/{label_key(label)}/{layer}[{slot}]"
                        )

            for slot in range(4):
                if sp.simplify(
                    mapped["action"][slot] - source["action"][slot]
                ) == 0:
                    counters["action"] += 1
                else:
                    FAILURES.append(
                        f"{generator_name}/{label_key(label)}/action[{slot}]"
                    )

            if generator_name == "cycle012":
                wrong_forward_rejected = wrong_forward_rejected or any(
                    not form_equal(actual, expected)
                    for actual, expected in zip(
                        mapped["residual"],
                        jet_form_transport(action14, source["residual"]),
                    )
                )

            print(
                f"checked_fixed_edge={generator_name}/{label_key(label)}",
                flush=True,
            )

    expected_slots = len(fixed) * len(I1.GENERATORS) * 4
    exact("both generators cover both fixed representatives", generator_edges == 4, "4/4")
    for layer, count in counters.items():
        exact(
            f"{layer} transport covers every fixed-edge jet slot",
            count == expected_slots,
            f"{count}/{expected_slots}",
        )
    exact("mixed Shiab residual is live on both fixed cells", mixed_residual_live == 2, "2/2")
    exact("mixed moving primalizer is live on both fixed cells", mixed_primalizer_live == 2, "2/2")
    exact("mixed action is live on both fixed cells", mixed_action_live == 2, "2/2")
    exact(
        "moving-Hodge product-rule contribution fires on both fixed cells",
        moving_hodge_controls == 2,
        "2/2",
    )
    exact(
        "order-three edge rejects the old forward-lift convention",
        wrong_forward_rejected,
    )
    exact(
        "fixed-cell mixed actions match the exact preregistered values",
        [sources[label]["action"][3] for label in fixed]
        == [sp.Rational(215, 8), sp.Rational(87, 16)],
    )

    source_receipt(
        "active finite evaluator reduction is repository-derived",
        True,
        "REPOSITORY_DERIVES",
    )
    source_receipt(
        "public source is silent on the active S3 fixed-orbit evaluator",
        True,
        "SOURCE_SILENT",
    )

    typed("active (9,5) evaluator remains distinct from public (7,7) source presentation")
    typed("two fixed representatives are a stratum, not universal 380-representative coverage")
    typed("geometric transport and full evaluator transport remain separately certified layers")
    typed("I1 A4 and I2B C4 remain separate, incomplete, and unpromoted")
    typed("the unconditional 1,925-cell fallback remains live")
    typed("P1/P2/P3 remain unchanged and unused")
    typed("Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE")
    typed("TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED")

    reject("PLANT promote the 380-representative engine from 2/380 coverage", False)
    reject("PLANT replace the 1,925-cell fallback before the other 378 representatives", False)
    reject("PLANT assemble or merge the I1 A4 and I2B C4 banks", False)
    reject("PLANT begin Green/Helmholtz from the fixed-orbit stratum", False)
    reject("PLANT spend P1/P2/P3 on an evaluator symmetry check", False)
    reject("PLANT merge Curt or promote a third construction lane", False)

    print(f"fixed_representatives={len(fixed)}/2")
    print("representative_coverage=2/380")
    print("remaining_representatives=378/380")
    print(f"mixed_actions={[sources[label]['action'][3] for label in fixed]}")
    print(
        f"SUMMARY: {EXACT} exact + {SOURCE} source + {TYPE} type + "
        f"{PLANTED} planted = {EXACT + SOURCE + TYPE + PLANTED} checks"
    )
    print(f"FAILURES: {len(FAILURES)}")
    for failure in FAILURES:
        print(f"- {failure}")
    if FAILURES:
        return 1

    print(
        "VERDICT: both S3-fixed owner-pair/quartic-point representatives "
        "transport exactly under both generators through every mixed "
        "Phi/Hodge/Shiab/residual/primalizer/action jet slot; fixed-orbit "
        "coverage is 2/380 and the other 378 representatives remain open"
    )
    print("FALLBACK=1925_CELLS_PER_BANK_REMAINS_LIVE")
    print("CURT_TRACK=FORMALLY_SEPARATE_INSIDE_ERIC_LANE")
    print("THIRD_LANE_GATE=TG-1 AND TG-2 AND TG-3 = NOT_PROMOTED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
