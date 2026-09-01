#!/usr/bin/env python3
"""Exact quotient/majorant descent controls for the two independent K77 packets."""
from __future__ import annotations

import copy
import json
import pathlib
import sys
from fractions import Fraction


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k77-quotient-majorant-descent-wave.json"
Q = Fraction
Matrix = tuple[tuple[Q, ...], ...]
Vector = tuple[Q, ...]


def zeros(rows: int, cols: int) -> Matrix:
    return tuple(tuple(Q(0) for _ in range(cols)) for _ in range(rows))


def identity(size: int) -> Matrix:
    return tuple(tuple(Q(i == j) for j in range(size)) for i in range(size))


def diagonal(entries: tuple[Q, ...]) -> Matrix:
    return tuple(tuple(entries[i] if i == j else Q(0) for j in range(len(entries)))
                 for i in range(len(entries)))


def transpose(matrix: Matrix) -> Matrix:
    return tuple(tuple(matrix[j][i] for j in range(len(matrix)))
                 for i in range(len(matrix[0])))


def add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(tuple(left[i][j] + right[i][j] for j in range(len(left[0])))
                 for i in range(len(left)))


def mul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(sum((left[i][k] * right[k][j] for k in range(len(right))), Q(0))
              for j in range(len(right[0])))
        for i in range(len(left))
    )


def matvec(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(sum((matrix[i][j] * vector[j] for j in range(len(vector))), Q(0))
                 for i in range(len(matrix)))


def dot(left: Vector, right: Vector) -> Q:
    return sum((x * y for x, y in zip(left, right)), Q(0))


def bilinear(left: Vector, form: Matrix, right: Vector) -> Q:
    return dot(left, matvec(form, right))


def outer(vector: Vector) -> Matrix:
    return tuple(tuple(x * y for y in vector) for x in vector)


def conjugate(matrix: Matrix, state: Matrix) -> Matrix:
    return mul(mul(matrix, state), transpose(matrix))


def trace_product(left: Matrix, right: Matrix) -> Q:
    return sum((left[i][j] * right[j][i]
                for i in range(len(left)) for j in range(len(left))), Q(0))


def standard_symplectic(rank: int) -> Matrix:
    size = 2 * rank
    rows = [[Q(0) for _ in range(size)] for _ in range(size)]
    for index in range(rank):
        rows[index][rank + index] = Q(1)
        rows[rank + index][index] = Q(-1)
    return tuple(tuple(row) for row in rows)


def compatible_complex(rank: int, scale: Q) -> Matrix:
    size = 2 * rank
    rows = [[Q(0) for _ in range(size)] for _ in range(size)]
    for index in range(rank):
        rows[index][rank + index] = -Q(1) / scale
        rows[rank + index][index] = scale
    return tuple(tuple(row) for row in rows)


def symplectic_scaling(rank: int, scale: Q) -> Matrix:
    return diagonal(tuple(scale for _ in range(rank))
                    + tuple(Q(1) / scale for _ in range(rank)))


def is_positive_diagonal(matrix: Matrix) -> bool:
    return all(matrix[i][i] > 0 for i in range(len(matrix))) and all(
        matrix[i][j] == 0 for i in range(len(matrix)) for j in range(len(matrix))
        if i != j
    )


def model_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    causal_ranks = (12, 12, 11)
    if mutation == "erase_null_jump":
        causal_ranks = (12, 12, 12)
    radical_dims = tuple(220 - 2 * rank for rank in causal_ranks)
    reduced_dims = tuple(2 * rank for rank in causal_ranks)

    omega = standard_symplectic(2)
    j_one = compatible_complex(2, Q(1))
    j_four = compatible_complex(2, Q(4))
    if mutation == "unique_majorant":
        j_four = j_one
    g_one = mul(omega, j_one)
    g_four = mul(omega, j_four)
    scaling = symplectic_scaling(2, Q(2))
    sample = (Q(1), Q(-2), Q(3), Q(1))

    projector = diagonal((Q(1), Q(1), Q(0), Q(0)))
    projector_out = add(identity(4), diagonal((Q(-1), Q(-1), Q(0), Q(0))))
    energy = diagonal((Q(1), Q(4), Q(1), Q(4)))
    amplitude = (Q(3, 5), Q(2, 5), Q(0), Q(0))
    if mutation == "leave_incoming_range":
        amplitude = (Q(3, 5), Q(2, 5), Q(1), Q(0))
    energy_norm = bilinear(amplitude, energy, amplitude)
    density = tuple(tuple(value / energy_norm for value in row) for row in outer(amplitude))
    negative_density = tuple(tuple(value / energy_norm for value in row)
                             for row in outer(tuple(-x for x in amplitude)))
    unit = energy
    effect_zero = diagonal((Q(1), Q(0), Q(0), Q(0)))
    effect_one = diagonal((Q(0), Q(4), Q(0), Q(0)))
    phase: Matrix = (
        (Q(0), Q(-2), Q(0), Q(0)),
        (Q(1, 2), Q(0), Q(0), Q(0)),
        (Q(0), Q(0), Q(0), Q(-2)),
        (Q(0), Q(0), Q(1, 2), Q(0)),
    )
    if mutation == "non_energy_phase":
        phase = (
            (Q(0), Q(-1), Q(0), Q(0)),
            (Q(1), Q(0), Q(0), Q(0)),
            (Q(0), Q(0), Q(0), Q(-1)),
            (Q(0), Q(0), Q(1), Q(0)),
        )
    phased = conjugate(phase, density)
    dephased = tuple(
        tuple(Q(0) if i != j and i < 2 and j < 2 else density[i][j]
              for j in range(4))
        for i in range(4)
    )
    witness = (Q(2), Q(-1), Q(3), Q(4))

    checks = [
        ("I1B fixed-stratum Green quotients retain the exact 24/24/22 dimensions",
         reduced_dims == (24, 24, 22)),
        ("I1B radical dimensions retain the exact 196/196/198 null jump",
         radical_dims == (196, 196, 198)),
        ("the reduced Green form is alternating rather than a positive majorant",
         transpose(omega) == tuple(tuple(-entry for entry in row) for row in omega)
         and bilinear(sample, omega, sample) == 0),
        ("two distinct compatible complex structures square to minus identity",
         mul(j_one, j_one) == diagonal(tuple(Q(-1) for _ in range(4)))
         and mul(j_four, j_four) == diagonal(tuple(Q(-1) for _ in range(4)))
         and j_one != j_four),
        ("each supplied compatible complex structure constructs a positive majorant",
         is_positive_diagonal(g_one) and is_positive_diagonal(g_four)),
        ("symplectic covariance does not select either positive majorant",
         mul(mul(transpose(scaling), omega), scaling) == omega
         and mul(mul(transpose(scaling), g_one), scaling) != g_one),
        ("the observed incoming projector is idempotent and distinct from its normal-reversed complement",
         mul(projector, projector) == projector and mul(projector_out, projector_out) == projector_out
         and projector != projector_out),
        ("the observed amplitude lies in the incoming range and has positive principal energy",
         matvec(projector, amplitude) == amplitude and energy_norm > 0),
        ("the chart-local quadratic density identifies opposite amplitudes",
         density == negative_density),
        ("the transported principal energy is a deterministic unit on the normalized density",
         trace_product(unit, density) == 1),
        ("two chart-local effects are nonnegative and sum to the deterministic unit on the incoming range",
         trace_product(effect_zero, density) >= 0
         and trace_product(effect_one, density) >= 0
         and trace_product(effect_zero, density) + trace_product(effect_one, density) == 1),
        ("the energy-orthogonal phase squares to amplitude sign and preserves normalization",
         mul(phase, phase) == diagonal(tuple(Q(-1) for _ in range(4)))
         and mul(mul(transpose(phase), energy), phase) == energy
         and trace_product(unit, phased) == 1),
        ("chart-local dephasing preserves the deterministic unit",
         trace_product(unit, dephased) == 1),
        ("the quadratic density remains positive on an exact hostile witness",
         bilinear(witness, density, witness) == dot(witness, amplitude) ** 2 / energy_norm
         and bilinear(witness, density, witness) >= 0),
    ]
    return checks


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    if data.get("direction") != "observed_to_native":
        failures.append("direction")
    packets = {row.get("id"): row for row in data.get("packet_local_results", [])}
    if set(packets) != {"K77-I1B-MIXED-ORDER", "K77-OBSERVED-INCOMING-PROJECTOR"}:
        failures.append("packet_population")
        return failures
    i1b = packets["K77-I1B-MIXED-ORDER"]
    observed = packets["K77-OBSERVED-INCOMING-PROJECTOR"]
    if i1b.get("quotient_status") != "constructed_on_each_fixed_rank_stratum__not_global_across_null_jump":
        failures.append("i1b_quotient")
    if i1b.get("positive_majorant_status") != "compatible_family_exists__none_selected_by_packet":
        failures.append("i1b_majorant")
    if i1b.get("reduced_dimensions") != [24, 24, 22]:
        failures.append("i1b_dimensions")
    if observed.get("quotient_status") != "incoming_boundary_projection_constructed__physical_gauge_quotient_open":
        failures.append("observed_quotient")
    if observed.get("positive_majorant_status") != "chart_local_restriction_of_transported_positive_principal_energy":
        failures.append("observed_majorant")
    if observed.get("state_unit_effect_status") != "chart_local_conditional_interface_constructed":
        failures.append("observed_interface")
    if observed.get("physical_state_status") != "not_constructed":
        failures.append("physical_state_promotion")
    if data.get("composability", {}).get("cross_packet_union_allowed") is not False:
        failures.append("cross_packet_union")
    result = data.get("result", {})
    if result.get("global_physical_quotients_completed") != 0:
        failures.append("global_quotient_promotion")
    if result.get("gu_native_physical_state_spaces_completed") != 0:
        failures.append("state_promotion")
    if result.get("action_selection") != "none":
        failures.append("action_selection")
    holdout = data.get("holdout_firewall", {})
    if holdout.get("status") != "reserved_unscored" or holdout.get("scored_in_this_result") is not False:
        failures.append("holdout")
    obligations = {row.get("id"): row.get("status") for row in data.get("psx_obligations", [])}
    if set(obligations) != {f"K77-PSX-{index}" for index in range(1, 8)}:
        failures.append("psx_population")
    if obligations.get("K77-PSX-5") != "open_both_packets" or obligations.get("K77-PSX-6") != "open_both_packets":
        failures.append("premature_composite_or_instrument")
    for packet in packets.values():
        for ref in packet.get("evidence_refs", []):
            if not (ROOT / ref).is_file():
                failures.append(f"missing_evidence:{ref}")
    if "No global GU-native" not in data.get("claim_ceiling", ""):
        failures.append("claim_ceiling")
    return failures


def selftest(data: dict) -> int:
    edits = (
        ("reverse_direction", lambda d: d.__setitem__("direction", "native_to_observed")),
        ("promote_i1b_global", lambda d: d["packet_local_results"][0].__setitem__("quotient_status", "global")),
        ("select_i1b_majorant", lambda d: d["packet_local_results"][0].__setitem__("positive_majorant_status", "selected")),
        ("merge_null_stratum", lambda d: d["packet_local_results"][0].__setitem__("reduced_dimensions", [24, 24, 24])),
        ("projection_is_gauge", lambda d: d["packet_local_results"][1].__setitem__("quotient_status", "physical_gauge_quotient")),
        ("promote_observed_state", lambda d: d["packet_local_results"][1].__setitem__("physical_state_status", "constructed")),
        ("cross_packet_union", lambda d: d["composability"].__setitem__("cross_packet_union_allowed", True)),
        ("promote_global_quotient", lambda d: d["result"].__setitem__("global_physical_quotients_completed", 1)),
        ("select_action", lambda d: d["result"].__setitem__("action_selection", "selected")),
        ("score_holdout", lambda d: d["holdout_firewall"].__setitem__("scored_in_this_result", True)),
        ("promote_composite", lambda d: d["psx_obligations"][4].__setitem__("status", "complete")),
    )
    caught: list[tuple[str, bool]] = []
    for name, edit in edits:
        mutated = copy.deepcopy(data)
        edit(mutated)
        caught.append((name, bool(manifest_failures(mutated))))
    for name in ("erase_null_jump", "unique_majorant", "leave_incoming_range", "non_energy_phase"):
        caught.append((name, any(not passed for _, passed in model_checks(name))))
    for name, passed in caught:
        print(f"[{'PASS' if passed else 'FAIL'}] hostile mutation {name}")
    print(f"HOSTILE SELFTEST: {sum(passed for _, passed in caught)}/{len(caught)} caught")
    return 0 if all(passed for _, passed in caught) else 1


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if "--selftest" in sys.argv:
        return selftest(data)
    checks = model_checks()
    failures = manifest_failures(data)
    checks.append(("manifest preserves packet asymmetry, PSX denominator and claim ceiling", not failures))
    failed = 0
    for label, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
        failed += int(not passed)
    print(f"K77 QUOTIENT/MAJORANT DESCENT: {len(checks) - failed}/{len(checks)} pass")
    if failures:
        print("manifest failures:", ", ".join(failures))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
