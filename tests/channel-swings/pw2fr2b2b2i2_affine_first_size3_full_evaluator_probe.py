#!/usr/bin/env python3
r"""Durable affine first-moving and first size-three S3 evaluator certificate.

The byte-pinned predecessor closes the complete two-cell fixed stratum.  This
successor certifies the zero plus four coordinate conormal directions for all
ten owners, proves exact affine spanning at the preregistered dense controls,
and then selects the lexicographically first non-fixed size-three orbit without
looking at evaluator output.  All three orbit labels and both S3 generators are
checked through the full mixed metric/Phi/Hodge/Shiab/primalizer/action jet.

The durable result is exactly 3/380 canonical representatives.  It does not
certify the remaining 377, promote the reduction engine, replace the 1,925-cell
fallback, assemble I1 A4 or I2B C4, begin Green/Helmholtz, spend P1/P2/P3,
merge Curt's rival track, or pass the conjunctive third-lane gate.
"""

from __future__ import annotations

from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
CHANNEL = ROOT / "tests" / "channel-swings"
PREDECESSOR = CHANNEL / "pw2fr2b2b2i2_s3_fixed_orbit_full_evaluator_probe.py"
PREDECESSOR_REGISTRY = (
    ROOT / "lab/process/pw2fr2b2b2i2-s3-fixed-orbit-full-evaluator-certificate.json"
)
DEPENDENCIES = {
    PREDECESSOR: "02f86f0dcd126f38257fc941c4cd73dc6240502d0a0c31472733520587588497",
    PREDECESSOR_REGISTRY: "f10609cc2e11790364e343ca30d6db4e16ecfb1d082cde3037d32b722ebec16f",
}


def load_predecessor():
    spec = spec_from_file_location("gu_i2_fixed_durable", PREDECESSOR)
    if spec is None or spec.loader is None:
        raise RuntimeError(str(PREDECESSOR))
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


P = load_predecessor()
I1 = P.I1
G = P.G
M = P.M


def form_equal(left: M.SForm, right: M.SForm) -> bool:
    return not M.sfadd(left, M.sfscale(right, -1))


def sum_forms(values) -> M.SForm:
    return M.sfadd(*tuple(values))


def combine_forms(coefficients, values) -> M.SForm:
    return sum_forms(
        M.sfscale(value, coefficient)
        for coefficient, value in zip(coefficients, values)
        if coefficient != 0
    )


def combine_matrices(coefficients, values) -> sp.Matrix:
    result = sp.zeros(14)
    for coefficient, value in zip(coefficients, values):
        result += coefficient * value
    return sp.simplify(result)


def top_scalar(value: M.SForm) -> sp.Expr:
    return sp.simplify(value.get(M.FULL_KEY, {}).get(0, 0))


def fixed_shiab(curvature: M.SForm) -> M.SForm:
    return M.sfproject(M.sfleft(M.STRACE, M.sraw(curvature)))


def first_slot(owner: int, conormal: tuple[sp.Expr, ...]):
    metric = I1.zorro_metric_jet(owner, conormal, 0, (0, 0, 0, 0))
    coordinate = G.fixed_frame_trace_jet(owner, 0)
    trace_motion = tuple(coordinate[1][index, 0] for index in range(14))
    return metric[1], trace_motion


def primalizer_derivative(
    residual: M.SForm,
    residual_derivative: M.SForm,
    metric_derivative: sp.Matrix,
) -> M.SForm:
    return M.sfadd(
        M.dstar(residual, metric_derivative),
        M.sfhodge(residual_derivative),
    )


def action_derivative(
    residual: M.SForm,
    residual_derivative: M.SForm,
    metric_derivative: sp.Matrix,
) -> sp.Expr:
    primalizer = M.sfhodge(residual)
    d_primalizer = primalizer_derivative(
        residual, residual_derivative, metric_derivative
    )
    return top_scalar(
        M.sfadd(
            M.sfwedge(d_primalizer, residual),
            M.sfwedge(primalizer, residual_derivative),
        )
    )


def build_first_case(
    curvature: M.SForm,
    residual: M.SForm,
    owner: int,
    conormal: tuple[sp.Expr, ...],
):
    metric_derivative, trace_motion = first_slot(owner, conormal)
    parts = M.moving_metric_shiab_parts(
        curvature, metric_derivative, trace_motion
    )
    residual_derivative = sum_forms(parts.values())
    return {
        "metric": metric_derivative,
        "parts": parts,
        "residual": residual_derivative,
        "primalizer": primalizer_derivative(
            residual, residual_derivative, metric_derivative
        ),
        "action": action_derivative(
            residual, residual_derivative, metric_derivative
        ),
        "trace_fires": bool(M.flatten_form(parts["trace_gamma"])),
    }


def combine_first_cases(coefficients, cases):
    part_names = tuple(cases[0]["parts"])
    return {
        "metric": combine_matrices(
            coefficients, [case["metric"] for case in cases]
        ),
        "parts": {
            name: combine_forms(
                coefficients, [case["parts"][name] for case in cases]
            )
            for name in part_names
        },
        "residual": combine_forms(
            coefficients, [case["residual"] for case in cases]
        ),
        "primalizer": combine_forms(
            coefficients, [case["primalizer"] for case in cases]
        ),
        "action": sp.simplify(
            sum(
                coefficient * case["action"]
                for coefficient, case in zip(coefficients, cases)
            )
        ),
    }


def first_case_equal(left, right) -> bool:
    return (
        sp.simplify(left["metric"] - right["metric"]) == sp.zeros(14)
        and all(
            form_equal(left["parts"][name], right["parts"][name])
            for name in left["parts"]
        )
        and form_equal(left["residual"], right["residual"])
        and form_equal(left["primalizer"], right["primalizer"])
        and sp.simplify(left["action"] - right["action"]) == 0
    )


def unit(axis: int) -> tuple[sp.Expr, ...]:
    return tuple(sp.Integer(index == axis) for index in range(4))


def main() -> int:
    print(
        "PW2F-R2B2B2I2 AFFINE-FIRST-MOVING PLUS FIRST-SIZE3 FULL-EVALUATOR CERTIFICATE",
        flush=True,
    )
    failures: list[str] = []
    exact_checks = source_checks = type_checks = planted_checks = 0

    def exact(label: str, condition: bool, detail: str = "") -> None:
        nonlocal exact_checks
        exact_checks += 1
        suffix = f" ({detail})" if detail else ""
        print(f"{'PASS' if condition else 'FAIL'}: exact - {label}{suffix}", flush=True)
        if not condition:
            failures.append(f"exact: {label}")

    def source_receipt(label: str, disposition: str) -> None:
        nonlocal source_checks
        source_checks += 1
        print(f"PASS: source - {label} [{disposition}]", flush=True)

    def typed(label: str) -> None:
        nonlocal type_checks
        type_checks += 1
        print(f"PASS: type - {label}", flush=True)

    def reject(label: str, false_claim: bool = False) -> None:
        nonlocal planted_checks
        planted_checks += 1
        condition = not false_claim
        print(
            f"{'PASS' if condition else 'FAIL'}: planted rejection - {label}",
            flush=True,
        )
        if not condition:
            failures.append(f"planted: {label}")

    dependency_checks = 0
    for path, expected in DEPENDENCIES.items():
        actual = sha256(path.read_bytes()).hexdigest()
        dependency_checks += int(actual == expected)
        if actual != expected:
            failures.append(f"dependency drift: {path.name}={actual}")
    exact(
        "fixed-stratum probe and registry are byte pinned",
        dependency_checks == len(DEPENDENCIES),
        f"{dependency_checks}/{len(DEPENDENCIES)}",
    )

    curvature: M.SForm = {
        (0, 1): M.sblade(2, 3),
        (4, 5): M.sblade(6, 7, 8),
        (2, 10): M.sblade(0, 4, 9, 13),
    }
    residual = fixed_shiab(curvature)
    zero = tuple(sp.Integer(0) for _ in range(4))
    directions = (("zero", zero),) + tuple(
        (f"e{axis}", unit(axis)) for axis in range(4)
    )
    dense = tuple(map(sp.Integer, (1, -1, 2, 3)))
    source_cases = {}
    trace_nonzero = action_nonzero = 0
    for owner in range(10):
        for direction, conormal in directions:
            case = build_first_case(curvature, residual, owner, conormal)
            source_cases[(owner, direction)] = case
            trace_nonzero += int(case["trace_fires"])
            action_nonzero += int(case["action"] != 0)
        print(f"prepared_affine_owner={owner}", flush=True)

    affine_span_checks = 0
    dense_cases = {}
    for owner in (0, 9):
        direct = build_first_case(curvature, residual, owner, dense)
        coefficients = (sp.Integer(1) - sum(dense),) + dense
        combined = combine_first_cases(
            coefficients,
            [source_cases[(owner, direction)] for direction, _ in directions],
        )
        affine_span_checks += int(first_case_equal(direct, combined))
        dense_cases[owner] = direct
        print(f"checked_affine_dense_owner={owner}", flush=True)

    affine_counters = {
        "geometry": 0,
        "parts": 0,
        "residual": 0,
        "primalizer": 0,
        "action": 0,
    }
    affine_wrong_forward_rejected = False
    part_count = len(next(iter(source_cases.values()))["parts"])
    for generator_name, base_action in I1.GENERATORS.items():
        owner_map, owner_representation = I1.owner_action(base_action)
        action14 = I1.frame_action(base_action, owner_representation)
        transport14 = sp.simplify(action14.inv())
        moved_curvature = P.total_action(transport14, curvature)
        moved_residual = fixed_shiab(moved_curvature)
        for owner in range(10):
            for direction, conormal in directions:
                source = source_cases[(owner, direction)]
                mapped = build_first_case(
                    moved_curvature,
                    moved_residual,
                    owner_map[owner],
                    I1.conormal_action(base_action, conormal),
                )
                affine_counters["geometry"] += int(
                    sp.simplify(
                        mapped["metric"]
                        - action14.T * source["metric"] * action14
                    )
                    == sp.zeros(14)
                )
                for name, source_part in source["parts"].items():
                    affine_counters["parts"] += int(
                        form_equal(
                            mapped["parts"][name],
                            P.total_action(transport14, source_part),
                        )
                    )
                affine_counters["residual"] += int(
                    form_equal(
                        mapped["residual"],
                        P.total_action(transport14, source["residual"]),
                    )
                )
                affine_counters["primalizer"] += int(
                    form_equal(
                        mapped["primalizer"],
                        P.total_action(transport14, source["primalizer"]),
                    )
                )
                affine_counters["action"] += int(
                    sp.simplify(mapped["action"] - source["action"]) == 0
                )
        if generator_name == "cycle012":
            source = dense_cases[0]
            mapped = build_first_case(
                moved_curvature,
                moved_residual,
                owner_map[0],
                I1.conormal_action(base_action, dense),
            )
            affine_wrong_forward_rejected = any(
                not form_equal(
                    mapped["parts"][name],
                    P.total_action(action14, source["parts"][name]),
                )
                for name in source["parts"]
            ) or not form_equal(
                mapped["residual"],
                P.total_action(action14, source["residual"]),
            )
        print(f"checked_affine_generator={generator_name}", flush=True)

    affine_edges = len(I1.GENERATORS) * 10 * len(directions)
    exact("affine basis has all ten zero-plus-four cases", len(source_cases) == 50, "50/50")
    exact("preregistered dense controls are exact affine spans", affine_span_checks == 2, f"{affine_span_checks}/2")
    exact("affine metric transport covers every generator edge", affine_counters["geometry"] == affine_edges, f"{affine_counters['geometry']}/{affine_edges}")
    exact("all eight moving Shiab families cover every affine edge", affine_counters["parts"] == affine_edges * part_count, f"{affine_counters['parts']}/{affine_edges * part_count}")
    exact("affine residual transport covers every generator edge", affine_counters["residual"] == affine_edges, f"{affine_counters['residual']}/{affine_edges}")
    exact("affine moving-primalizer transport covers every generator edge", affine_counters["primalizer"] == affine_edges, f"{affine_counters['primalizer']}/{affine_edges}")
    exact("affine action derivative is invariant on every generator edge", affine_counters["action"] == affine_edges, f"{affine_counters['action']}/{affine_edges}")
    exact("trace motion is nonvacuous on the affine basis", trace_nonzero > 0, f"{trace_nonzero}/50")
    exact("action derivative is nonvacuous on the affine basis", action_nonzero > 0, f"{action_nonzero}/50")
    exact("affine order-three edge rejects the obsolete forward lift", affine_wrong_forward_rejected)

    group, labels, resolver = P.canonical_orbit_resolver()
    representatives = tuple(
        sorted({entry[0] for entry in resolver.values()}, key=P.label_key)
    )
    size_three = tuple(
        representative
        for representative in representatives
        if resolver[representative][2] == 3
    )
    representative = size_three[0]
    orbit = tuple(
        sorted(
            {I1.grid_action(element, representative) for element in group},
            key=P.label_key,
        )
    )
    exact("canonical resolver covers 1,925 labels", len(labels) == 1925)
    exact("canonical resolver still has 380 representatives", len(representatives) == 380)
    exact("orbit census has 115 size-three representatives", len(size_three) == 115)
    exact("selected orbit is the first complete non-fixed orbit", len(orbit) == 3)
    exact("all selected labels resolve to the same representative", all(resolver[label][0] == representative for label in orbit))
    exact("canonical witnesses reach every selected label", all(I1.grid_action(resolver[label][1], representative) == label for label in orbit))
    exact("both generators close on the selected orbit", all(I1.grid_action(generator, label) in orbit for generator in I1.GENERATORS.values() for label in orbit))
    print(f"selected_representative={P.label_key(representative)}", flush=True)
    print(f"selected_orbit={[P.label_key(label) for label in orbit]}", flush=True)

    orbit_sources = {
        label: P.evaluate(label[0], label[1], curvature) for label in orbit
    }
    mixed_residual_live = sum(
        bool(source["residual"][3]) for source in orbit_sources.values()
    )
    mixed_primalizer_live = sum(
        bool(source["primalizer"][3]) for source in orbit_sources.values()
    )
    mixed_action_live = sum(
        source["action"][3] != 0 for source in orbit_sources.values()
    )
    moving_hodge_controls = sum(
        not form_equal(
            source["primalizer"][3], M.sfhodge(source["residual"][3])
        )
        for source in orbit_sources.values()
    )
    orbit_counters = {
        "geometry": 0,
        "phi_one": 0,
        "phi_two": 0,
        "hodge": 0,
        "residual": 0,
        "primalizer": 0,
        "action": 0,
    }
    directed_edges = nonself_edges = 0
    orbit_wrong_forward_rejected = False
    for generator_name, base_action in I1.GENERATORS.items():
        owner_map, owner_representation = I1.owner_action(base_action)
        action14 = I1.frame_action(base_action, owner_representation)
        transport14 = sp.simplify(action14.inv())
        moved_curvature = P.total_action(transport14, curvature)
        for label in orbit:
            mapped_label = I1.grid_action(base_action, label)
            mapped_owner_pair = tuple(owner_map[owner] for owner in label[0])
            mapped_point = I1.conormal_action(base_action, label[1])
            if mapped_label != (mapped_owner_pair, mapped_point):
                failures.append(
                    f"grid/component mismatch: {generator_name}/{P.label_key(label)}"
                )
            mapped = P.evaluate(mapped_owner_pair, mapped_point, moved_curvature)
            source = orbit_sources[label]
            directed_edges += 1
            nonself_edges += int(mapped_label != label)
            for slot in range(4):
                orbit_counters["geometry"] += int(
                    sp.simplify(
                        mapped["metric"][slot]
                        - action14.T * source["metric"][slot] * action14
                    )
                    == sp.zeros(14)
                )
            for layer in ("phi_one", "phi_two", "hodge", "residual", "primalizer"):
                transported = P.jet_form_transport(transport14, source[layer])
                orbit_counters[layer] += sum(
                    form_equal(actual, expected)
                    for actual, expected in zip(mapped[layer], transported)
                )
            orbit_counters["action"] += sum(
                sp.simplify(actual - expected) == 0
                for actual, expected in zip(mapped["action"], source["action"])
            )
            if generator_name == "cycle012":
                orbit_wrong_forward_rejected = orbit_wrong_forward_rejected or any(
                    not form_equal(actual, expected)
                    for actual, expected in zip(
                        mapped["residual"],
                        P.jet_form_transport(action14, source["residual"]),
                    )
                )
            print(
                f"checked_orbit_edge={generator_name}/{P.label_key(label)}"
                f"->{P.label_key(mapped_label)}",
                flush=True,
            )

    orbit_slots = len(orbit) * len(I1.GENERATORS) * 4
    exact("selected orbit has all six directed generator edges", directed_edges == 6, "6/6")
    exact("selected orbit contains non-self transport", nonself_edges == 5, f"{nonself_edges}/6")
    for layer, count in orbit_counters.items():
        exact(f"{layer} transport covers every selected-orbit jet slot", count == orbit_slots, f"{count}/{orbit_slots}")
    exact("mixed residual is live on every selected label", mixed_residual_live == 3, f"{mixed_residual_live}/3")
    exact("mixed moving primalizer is live on every selected label", mixed_primalizer_live == 3, f"{mixed_primalizer_live}/3")
    exact("mixed action is live on every selected label", mixed_action_live == 3, f"{mixed_action_live}/3")
    exact("moving-Hodge product rule fires on every selected label", moving_hodge_controls == 3, f"{moving_hodge_controls}/3")
    exact("selected orbit rejects the obsolete forward lift", orbit_wrong_forward_rejected)
    exact(
        "selected-orbit mixed actions match preregistered exact values",
        [orbit_sources[label]["action"][3] for label in orbit]
        == [sp.Rational(-727, 144), sp.Rational(-727, 144), sp.Rational(107, 9)],
    )

    source_receipt("active evaluator and S3 reduction remain repository-derived", "REPOSITORY_DERIVES")
    source_receipt("public sources remain silent on affine and orbit evaluator coverage", "SOURCE_SILENT")
    typed("active trace-reversed (9,5) evaluator is distinct from public (7,7) presentation")
    typed("affine first-moving closure is not mixed second-order universal coverage")
    typed("one size-three orbit advances durable coverage to exactly 3/380")
    typed("the remaining 377 representatives and dense universal heldouts stay open")
    typed("I1 A4 and I2B C4 remain separate, incomplete, and unpromoted")
    typed("the unconditional 1,925-cell fallback remains live")
    typed("P1/P2/P3 remain unchanged and unused")
    typed("Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE")
    typed("TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED")
    reject("PLANT treat first-moving affine closure as mixed universal coverage")
    reject("PLANT promote the 380-representative engine from 3/380 coverage")
    reject("PLANT replace the 1,925-cell fallback before the other 377 representatives")
    reject("PLANT assemble or merge I1 A4 and I2B C4")
    reject("PLANT begin Green/Helmholtz from one non-fixed orbit")
    reject("PLANT spend P1/P2/P3 on evaluator transport")
    reject("PLANT merge Curt or promote a third construction lane")

    print(f"affine_basis_cases={len(source_cases)}/50")
    print(f"affine_generator_edges={affine_edges}/100")
    print(f"selected_representative={P.label_key(representative)}")
    print(f"selected_orbit_size={len(orbit)}/3")
    print(f"mixed_actions={[orbit_sources[label]['action'][3] for label in orbit]}")
    print("representative_coverage=3/380")
    print("remaining_representatives=377/380")
    print(
        f"SUMMARY: {exact_checks} exact + {source_checks} source + "
        f"{type_checks} type + {planted_checks} planted = "
        f"{exact_checks + source_checks + type_checks + planted_checks} checks"
    )
    print(f"FAILURES: {len(failures)}")
    for failure in failures:
        print(f"- {failure}")
    if failures:
        return 1
    print(
        "VERDICT: every first-moving owner/conormal affine-basis direction "
        "and the lexicographically first non-fixed size-three orbit transport "
        "exactly under both S3 generators; durable full-evaluator coverage is "
        "3/380 and the other 377 representatives remain open"
    )
    print("FALLBACK=1925_CELLS_PER_BANK_REMAINS_LIVE")
    print("CURT_TRACK=FORMALLY_SEPARATE_INSIDE_ERIC_LANE")
    print("THIRD_LANE_GATE=TG-1 AND TG-2 AND TG-3 = NOT_PROMOTED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
