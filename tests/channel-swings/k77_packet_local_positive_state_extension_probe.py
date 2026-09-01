#!/usr/bin/env python3
"""Exact packet-local obstruction and quadratic-state extension certificate."""
from __future__ import annotations

import copy
import json
import pathlib
import sys
from fractions import Fraction


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k77-packet-local-positive-state-extension-wave.json"
Q = Fraction
Matrix = tuple[tuple[Q, Q], tuple[Q, Q]]


def add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(tuple(left[i][j] + right[i][j] for j in range(2)) for i in range(2))  # type: ignore[return-value]


def mul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(tuple(sum((left[i][k] * right[k][j] for k in range(2)), Q(0))
                       for j in range(2)) for i in range(2))  # type: ignore[return-value]


def transpose(matrix: Matrix) -> Matrix:
    return tuple(tuple(matrix[j][i] for j in range(2)) for i in range(2))  # type: ignore[return-value]


def trace(matrix: Matrix) -> Q:
    return matrix[0][0] + matrix[1][1]


def determinant(matrix: Matrix) -> Q:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def symmetric_psd(matrix: Matrix) -> bool:
    return (matrix[0][1] == matrix[1][0] and matrix[0][0] >= 0
            and matrix[1][1] >= 0 and determinant(matrix) >= 0)


def rank_one(vector: tuple[Q, Q]) -> Matrix:
    x, y = vector
    return ((x * x, x * y), (x * y, y * y))


def conjugate(matrix: Matrix, state: Matrix) -> Matrix:
    return mul(mul(matrix, state), transpose(matrix))


def effect_probability(state: Matrix, effect: Matrix) -> Q:
    return trace(mul(state, effect))


def dephase(state: Matrix, eta: Q) -> Matrix:
    return ((state[0][0], eta * state[0][1]),
            (eta * state[1][0], state[1][1]))


def raw_linear_cone_obstruction() -> bool:
    # A proposed sign-invariant pointed cone containing a nonzero vector fails
    # pointedness immediately because it also contains the vector's negative.
    vector = (Q(2), Q(-3))
    negative = tuple(-entry for entry in vector)
    return vector != (0, 0) and negative != vector and tuple(-entry for entry in negative) == vector


def model_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    vector = (Q(3, 5), Q(4, 5))
    neg_vector = tuple(-entry for entry in vector)
    rho = rank_one(vector)
    rho_neg = rank_one(neg_vector)  # type: ignore[arg-type]
    mixed = ((Q(1, 2), Q(1, 4)), (Q(1, 4), Q(1, 2)))
    if mutation == "negative_state":
        mixed = ((Q(-1, 2), Q(1, 4)), (Q(1, 4), Q(1, 2)))
    identity: Matrix = ((Q(1), Q(0)), (Q(0), Q(1)))
    p0: Matrix = ((Q(1), Q(0)), (Q(0), Q(0)))
    p1: Matrix = ((Q(0), Q(0)), (Q(0), Q(1)))
    rotation: Matrix = ((Q(0), Q(-1)), (Q(1), Q(0)))
    eta = Q(3, 5)
    if mutation == "amplifying_decoherence":
        eta = Q(2)
    phase_state = conjugate(rotation, mixed)
    outcome0 = conjugate(p0, mixed)
    outcome1 = conjugate(p1, mixed)
    nonselective = add(outcome0, outcome1)
    if mutation == "drop_outcome":
        nonselective = outcome0
    checks = [
        ("raw linear sign symmetry obstructs a nontrivial pointed cone", raw_linear_cone_obstruction()),
        ("quadratic lift identifies opposite amplitude representatives", rho == rho_neg),
        ("rank-one lifted state is positive semidefinite", symmetric_psd(rho)),
        ("rank-one lifted state has deterministic unit value one", trace(rho) == 1),
        ("mixed control is positive semidefinite", symmetric_psd(mixed)),
        ("trace order unit normalizes the mixed control", trace(mixed) == 1),
        ("projector effect probabilities are normalized and nonnegative",
         effect_probability(mixed, p0) >= 0 and effect_probability(mixed, p1) >= 0
         and effect_probability(mixed, p0) + effect_probability(mixed, p1) == 1
         and effect_probability(mixed, identity) == 1),
        ("selective instrument branches stay positive",
         symmetric_psd(outcome0) and symmetric_psd(outcome1)),
        ("nonselective instrument preserves trace",
         trace(nonselective) == trace(mixed)),
        ("nonselective instrument equals full dephasing",
         nonselective == dephase(mixed, Q(0))),
        ("quarter-turn phase transport preserves positivity and normalization",
         symmetric_psd(phase_state) and trace(phase_state) == 1),
        ("quarter-turn squared realizes amplitude sign while density is unchanged",
         mul(rotation, rotation) == ((Q(-1), Q(0)), (Q(0), Q(-1)))
         and conjugate(mul(rotation, rotation), rho) == rho),
        ("contractive dephasing preserves positivity and normalization",
         Q(0) <= eta <= Q(1) and symmetric_psd(dephase(mixed, eta))
         and trace(dephase(mixed, eta)) == 1),
        ("dephasing suppresses but does not invent coherence",
         abs(dephase(mixed, eta)[0][1]) <= abs(mixed[0][1])),
    ]
    return checks


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    if data.get("direction") != "observed_to_native":
        failures.append("direction")
    theorem = data.get("formal_selection_obstruction", {})
    if theorem.get("claim") != "sign_invariant_and_pointed_implies_trivial":
        failures.append("formal_claim")
    if theorem.get("scope") != "raw_linear_carrier_or_linear_map_range":
        failures.append("formal_scope")
    if theorem.get("does_not_prove") != "nonexistence_of_all_positive_cones":
        failures.append("formal_ceiling")
    packets = data.get("packet_local_results", [])
    if {row.get("id") for row in packets} != {"K77-I1B-MIXED-ORDER", "K77-OBSERVED-INCOMING-PROJECTOR"}:
        failures.append("packet_population")
    for packet in packets:
        if packet.get("raw_linear_cone_status") != "not_selected_and_not_sufficient":
            failures.append(f"raw_cone_promotion:{packet.get('id')}")
        if packet.get("physical_state_extension_status") != "required_not_constructed":
            failures.append(f"extension_promotion:{packet.get('id')}")
        if not packet.get("owned") or not packet.get("missing") or not packet.get("evidence_refs"):
            failures.append(f"packet_reason:{packet.get('id')}")
        for ref in packet.get("evidence_refs", []):
            if not (ROOT / ref).is_file():
                failures.append(f"evidence:{packet.get('id')}:{ref}")
    extension_ids = {row.get("id") for row in data.get("minimal_packet_local_extension", [])}
    if extension_ids != {f"K77-PSX-{i}" for i in range(1, 8)}:
        failures.append("extension_denominator")
    witness = data.get("quadratic_lift_control", {})
    if witness.get("status") != "exact_carrier_neutral_feasibility_witness":
        failures.append("witness_status")
    if witness.get("attached_to_k77_packet") is not False:
        failures.append("witness_import")
    composition = data.get("composability", {})
    if composition.get("cross_packet_union_allowed") is not False or composition.get("candidate_selected") is not False:
        failures.append("composition_or_selection")
    result = data.get("result", {})
    if result.get("packet_local_physical_state_constructions_completed") != 0:
        failures.append("construction_promotion")
    if result.get("action_selection") != "none" or result.get("prediction_or_confirmation_change") != "none":
        failures.append("result_ceiling")
    holdout = data.get("holdout_firewall", {})
    if holdout.get("status") != "reserved_unscored" or holdout.get("scored_in_this_result") is not False:
        failures.append("holdout")
    if "No GU-native" not in data.get("claim_ceiling", ""):
        failures.append("claim_ceiling")
    return failures


def selftest(data: dict) -> int:
    edits = (
        ("direction", lambda d: d.__setitem__("direction", "native_to_observed")),
        ("claim_scope", lambda d: d["formal_selection_obstruction"].__setitem__("does_not_prove", "no_positive_cone_exists")),
        ("promote_i1b", lambda d: d["packet_local_results"][0].__setitem__("raw_linear_cone_status", "complete")),
        ("promote_projector", lambda d: d["packet_local_results"][1].__setitem__("physical_state_extension_status", "constructed")),
        ("remove_extension", lambda d: d.__setitem__("minimal_packet_local_extension", d["minimal_packet_local_extension"][:-1])),
        ("import_witness", lambda d: d["quadratic_lift_control"].__setitem__("attached_to_k77_packet", True)),
        ("cross_union", lambda d: d["composability"].__setitem__("cross_packet_union_allowed", True)),
        ("select_action", lambda d: d["composability"].__setitem__("candidate_selected", True)),
        ("score_holdout", lambda d: d["holdout_firewall"].__setitem__("scored_in_this_result", True)),
        ("promote_result", lambda d: d["result"].__setitem__("packet_local_physical_state_constructions_completed", 1)),
    )
    mutations: list[tuple[str, bool]] = []
    for name, edit in edits:
        mutated = copy.deepcopy(data)
        edit(mutated)
        mutations.append((name, bool(manifest_failures(mutated))))
    for name in ("negative_state", "drop_outcome", "amplifying_decoherence"):
        mutations.append((name, any(not passed for _, passed in model_checks(name))))
    for name, caught in mutations:
        print(f"[{'PASS' if caught else 'FAIL'}] hostile mutation {name}")
    print(f"HOSTILE SELFTEST: {sum(caught for _, caught in mutations)}/{len(mutations)} caught")
    return 0 if all(caught for _, caught in mutations) else 1


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if "--selftest" in sys.argv:
        return selftest(data)
    checks = model_checks()
    failures = manifest_failures(data)
    checks.append(("manifest preserves packet independence, extension denominator and claim ceiling", not failures))
    failed = 0
    for label, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
        failed += int(not passed)
    print(f"K77 PACKET-LOCAL POSITIVE STATE EXTENSION: {len(checks) - failed}/{len(checks)} pass")
    if failures:
        print("manifest failures:", ", ".join(failures))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
