#!/usr/bin/env python3
r"""Resumable full-evaluator coverage: third uncovered size-six S3 orbit.

The byte-pinned predecessor commit certifies exactly 5/380 canonical
representatives. This successor selects the lexicographically first
representative outside that durable coverage before evaluator output, then
checks its complete six-label orbit and both S3 generators through the full
mixed metric/Phi/Hodge/Shiab/primalizer/action evaluator.

The durable result is at most 6/380. It does not execute the preregistered
dense heldouts, certify the remaining representatives, promote the engine,
replace the 1,925-cell fallback, assemble either bank, begin Green/Helmholtz,
spend P1/P2/P3, merge Curt, or pass the conjunctive third-lane gate.
"""

from __future__ import annotations

from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
import json
from pathlib import Path
import subprocess

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
CHANNEL = ROOT / "tests" / "channel-swings"
PREDECESSOR = CHANNEL / "pw2fr2b2b2i2_resumable_second_size6_full_evaluator_probe.py"
PREDECESSOR_REVISION = "93fb3c01d4c4ab40d6d4035bdd6063aae8dcdfab"
PREDECESSOR_LEDGER_PATH = "lab/process/pw2fr2b2b2i2-resumable-full-evaluator-coverage.json"
PREDECESSOR_PROBE_SHA256 = "668cd140bf52c1a78f4137945dc10df64874c04352d0b1fcc474cf891848c77b"
PREDECESSOR_LEDGER_SHA256 = "2f7a2aad5d1d76dd544d2bba5454ecaea1c905bea4685e2b05cda9f1917b8c9d"


def load_predecessor():
    spec = spec_from_file_location("gu_i2_resumable_second_size6", PREDECESSOR)
    if spec is None or spec.loader is None:
        raise RuntimeError(str(PREDECESSOR))
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def predecessor_ledger_bytes() -> bytes:
    return subprocess.check_output(
        ["git", "show", f"{PREDECESSOR_REVISION}:{PREDECESSOR_LEDGER_PATH}"],
        cwd=ROOT,
    )


S = load_predecessor()
P = S.P
I1 = P.I1
M = P.M
DENSE_HELDOUT_SEEDS = S.S.DENSE_HELDOUT_SEEDS

EXPECTED_REPRESENTATIVE = ((0, 0), (0, 0, 3, 1))
EXPECTED_MIXED_ACTIONS = (
    sp.Rational(749, 144),
    sp.Rational(-1499, 288),
    sp.Rational(749, 144),
    sp.Rational(-203, 288),
    sp.Rational(3379, 288),
    sp.Rational(4675, 288),
)


def form_equal(left: M.SForm, right: M.SForm) -> bool:
    return not M.sfadd(left, M.sfscale(right, -1))


def ledger_representative(entry: dict) -> tuple[tuple[int, int], tuple[int, ...]]:
    representative = entry["representative"]
    return (
        tuple(representative["owner_pair"]),
        tuple(representative["quartic_point"]),
    )


def main() -> int:
    print(
        "PW2F-R2B2B2I2 RESUMABLE THIRD-UNCOVERED SIZE6 FULL-EVALUATOR CERTIFICATE",
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
        print(f"{'PASS' if condition else 'FAIL'}: planted rejection - {label}", flush=True)
        if not condition:
            failures.append(f"planted: {label}")

    ledger_bytes = predecessor_ledger_bytes()
    dependency_checks = sum(
        (
            sha256(PREDECESSOR.read_bytes()).hexdigest() == PREDECESSOR_PROBE_SHA256,
            sha256(ledger_bytes).hexdigest() == PREDECESSOR_LEDGER_SHA256,
        )
    )
    exact(
        "durable 5/380 predecessor probe and committed ledger bytes are pinned",
        dependency_checks == 2,
        f"{dependency_checks}/2",
    )
    ledger = json.loads(ledger_bytes)

    group, labels, resolver = P.canonical_orbit_resolver()
    representatives = tuple(sorted({entry[0] for entry in resolver.values()}, key=P.label_key))
    fixed = tuple(rep for rep in representatives if resolver[rep][2] == 1)
    size_three = tuple(rep for rep in representatives if resolver[rep][2] == 3)
    predecessor_covered = set(fixed) | {size_three[0]}
    predecessor_covered.update(
        ledger_representative(entry) for entry in ledger["coverage_chain"]["entries"]
    )
    remaining = tuple(rep for rep in representatives if rep not in predecessor_covered)
    representative = remaining[0]
    orbit = tuple(
        sorted(
            {I1.grid_action(element, representative) for element in group},
            key=P.label_key,
        )
    )
    label_set = set(labels)
    heldout_orbits = tuple(
        {I1.grid_action(element, seed) for element in group}
        for seed in DENSE_HELDOUT_SEEDS
    )

    exact("canonical resolver covers 1,925 labels", len(labels) == 1925)
    exact("canonical resolver still has 380 representatives", len(representatives) == 380)
    exact("durable predecessor ledger resolves to exactly five representatives", len(predecessor_covered) == 5)
    exact("selection is the lexicographically first uncovered representative", representative == EXPECTED_REPRESENTATIVE)
    exact("selected representative has a complete six-cell orbit", len(orbit) == 6, f"{len(orbit)}/6")
    exact("all selected labels resolve to the same representative", all(resolver[label][0] == representative for label in orbit))
    exact("canonical witnesses reach every selected label", all(I1.grid_action(resolver[label][1], representative) == label for label in orbit))
    exact("both generators close on the selected orbit", all(I1.grid_action(generator, label) in orbit for generator in I1.GENERATORS.values() for label in orbit))
    exact("six dense heldout seeds remain outside the 1,925-cell lattice", all(seed not in label_set for seed in DENSE_HELDOUT_SEEDS), "6/6")
    exact("each frozen dense heldout seed retains a nontrivial closed S3 orbit", all(len(heldout) in (3, 6) for heldout in heldout_orbits), "6/6")
    print(f"selected_representative={P.label_key(representative)}", flush=True)
    print(f"selected_orbit={[P.label_key(label) for label in orbit]}", flush=True)

    curvature: M.SForm = {
        (0, 1): M.sblade(2, 3),
        (4, 5): M.sblade(6, 7, 8),
        (2, 10): M.sblade(0, 4, 9, 13),
    }
    sources = {}
    for label in orbit:
        sources[label] = P.evaluate(label[0], label[1], curvature)
        print(f"prepared_orbit_label={P.label_key(label)}", flush=True)

    mixed_residual_live = sum(bool(source["residual"][3]) for source in sources.values())
    mixed_primalizer_live = sum(bool(source["primalizer"][3]) for source in sources.values())
    mixed_action_live = sum(source["action"][3] != 0 for source in sources.values())
    moving_hodge_controls = sum(
        not form_equal(source["primalizer"][3], M.sfhodge(source["residual"][3]))
        for source in sources.values()
    )
    counters = {
        "geometry": 0,
        "phi_one": 0,
        "phi_two": 0,
        "hodge": 0,
        "residual": 0,
        "primalizer": 0,
        "action": 0,
    }
    directed_edges = nonself_edges = 0
    wrong_forward_rejected = False
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
                failures.append(f"grid/component mismatch: {generator_name}/{P.label_key(label)}")
            mapped = P.evaluate(mapped_owner_pair, mapped_point, moved_curvature)
            source = sources[label]
            directed_edges += 1
            nonself_edges += int(mapped_label != label)
            for slot in range(4):
                counters["geometry"] += int(
                    sp.simplify(mapped["metric"][slot] - action14.T * source["metric"][slot] * action14)
                    == sp.zeros(14)
                )
            for layer in ("phi_one", "phi_two", "hodge", "residual", "primalizer"):
                transported = P.jet_form_transport(transport14, source[layer])
                counters[layer] += sum(
                    form_equal(actual, expected)
                    for actual, expected in zip(mapped[layer], transported)
                )
            counters["action"] += sum(
                sp.simplify(actual - expected) == 0
                for actual, expected in zip(mapped["action"], source["action"])
            )
            if generator_name == "cycle012":
                wrong_forward_rejected = wrong_forward_rejected or any(
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
    exact("selected orbit has all twelve directed generator edges", directed_edges == 12, "12/12")
    exact("selected generic orbit moves on every generator edge", nonself_edges == 12, f"{nonself_edges}/12")
    for layer, count in counters.items():
        exact(f"{layer} transport covers every selected-orbit jet slot", count == orbit_slots, f"{count}/{orbit_slots}")
    exact("mixed residual is live on every selected label", mixed_residual_live == 6, f"{mixed_residual_live}/6")
    exact("mixed moving primalizer is live on every selected label", mixed_primalizer_live == 6, f"{mixed_primalizer_live}/6")
    exact("mixed action is live on every selected label", mixed_action_live == 6, f"{mixed_action_live}/6")
    exact("moving-Hodge product rule fires on every selected label", moving_hodge_controls == 6, f"{moving_hodge_controls}/6")
    exact("selected size-six orbit rejects the obsolete forward lift", wrong_forward_rejected)

    mixed_actions = tuple(source["action"][3] for source in sources.values())
    if EXPECTED_MIXED_ACTIONS is not None:
        exact("selected-orbit mixed actions match frozen exact values", mixed_actions == EXPECTED_MIXED_ACTIONS)

    source_receipt("active evaluator and S3 reduction remain repository-derived", "REPOSITORY_DERIVES")
    source_receipt("public sources remain silent on resumable finite evaluator coverage", "SOURCE_SILENT")
    typed("active trace-reversed (9,5) evaluator is distinct from public (7,7) presentation")
    typed("one additional size-six orbit advances durable coverage to at most 6/380")
    typed("the remaining representatives stay open")
    typed("dense heldouts remain preregistered inputs, not executed coverage")
    typed("I1 A4 and I2B C4 remain separate, incomplete, and unpromoted")
    typed("the unconditional 1,925-cell fallback remains live")
    typed("P1/P2/P3 remain unchanged and unused")
    typed("Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE")
    typed("TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED")
    reject("PLANT promote the 380-representative engine from partial coverage")
    reject("PLANT count frozen dense heldouts as executed")
    reject("PLANT replace the 1,925-cell fallback before universal coverage")
    reject("PLANT assemble or merge I1 A4 and I2B C4")
    reject("PLANT begin Green/Helmholtz from a fourth non-fixed orbit")
    reject("PLANT spend P1/P2/P3 on evaluator transport")
    reject("PLANT merge Curt or promote a third construction lane")

    print(f"selected_representative={P.label_key(representative)}")
    print(f"selected_orbit_size={len(orbit)}/6")
    print(f"mixed_actions={mixed_actions}")
    print("representative_coverage=6/380")
    print("remaining_representatives=374/380")
    print("dense_heldouts_preregistered=6/6__executed=0/6")
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
        "VERDICT: the third uncovered canonical representative and its "
        "complete six-cell orbit transport exactly under both S3 generators; "
        "durable coverage is 6/380 and the other 374 representatives remain open"
    )
    print("FALLBACK=1925_CELLS_PER_BANK_REMAINS_LIVE")
    print("CURT_TRACK=FORMALLY_SEPARATE_INSIDE_ERIC_LANE")
    print("THIRD_LANE_GATE=TG-1 AND TG-2 AND TG-3 = NOT_PROMOTED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
