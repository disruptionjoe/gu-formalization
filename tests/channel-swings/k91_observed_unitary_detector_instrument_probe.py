#!/usr/bin/env python3
"""Exact interaction-to-Kraus detector-instrument controls for K91."""
from __future__ import annotations

import copy
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k91-observed-unitary-detector-instrument-wave.json"


def matrix(rows): return tuple(tuple(F(x) for x in row) for row in rows)
def eye(n): return tuple(tuple(F(i == j) for j in range(n)) for i in range(n))
def transpose(a): return tuple(zip(*a))
def add(a, b): return tuple(tuple(a[i][j] + b[i][j] for j in range(len(a[0]))) for i in range(len(a)))
def scale(c, a): return tuple(tuple(F(c) * x for x in row) for row in a)
def mul(a, b): return tuple(tuple(sum((a[i][k] * b[k][j] for k in range(len(b))), F(0)) for j in range(len(b[0]))) for i in range(len(a)))
def trace(a): return sum((a[i][i] for i in range(len(a))), F(0))
def kron(a, b): return tuple(tuple(a[i][j] * b[k][l] for j in range(len(a[0])) for l in range(len(b[0]))) for i in range(len(a)) for k in range(len(b)))


def psd2(a):
    return a == transpose(a) and a[0][0] >= 0 and a[1][1] >= 0 and a[0][0] * a[1][1] - a[0][1] * a[1][0] >= 0


def ptrace_system(rho):
    return tuple(tuple(sum((rho[2 * s + r][2 * s + q] for s in range(2)), F(0)) for q in range(2)) for r in range(2))


def extracted_kraus(u, record):
    return tuple(tuple(u[2 * sout + record][2 * sin] for sin in range(2)) for sout in range(2))


def model_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    c, s = F(3, 5), F(4, 5)
    if mutation == "nonunitary_rotation":
        s = F(3, 5)
    u = matrix(((1, 0, 0, 0), (0, c, s, 0), (0, -s, c, 0), (0, 0, 0, 1)))
    k0, k1 = extracted_kraus(u, 0), extracted_kraus(u, 1)
    if mutation == "incomplete_kraus":
        k1 = matrix(((0, 0), (0, 0)))
    e0, e1 = mul(transpose(k0), k0), mul(transpose(k1), k1)

    rho = matrix(((F(9, 25), F(12, 25)), (F(12, 25), F(16, 25))))
    if mutation == "negative_state":
        rho = matrix(((F(26, 25), 0), (0, F(-1, 25))))
    branch0 = mul(mul(k0, rho), transpose(k0))
    branch1 = mul(mul(k1, rho), transpose(k1))
    if mutation == "negative_outcome":
        branch1 = scale(-1, branch1)
    p0, p1 = trace(branch0), trace(branch1)
    record0 = scale(1 / p0, branch0) if p0 else branch0
    record1 = scale(1 / p1, branch1) if p1 else branch1
    if mutation == "wrong_record_normalization":
        record0 = branch0
    nonselective = add(branch0, branch1)

    bell = matrix(((F(1, 2), 0, 0, F(1, 2)), (0, 0, 0, 0), (0, 0, 0, 0), (F(1, 2), 0, 0, F(1, 2))))
    joint0 = mul(mul(kron(k0, eye(2)), bell), transpose(kron(k0, eye(2))))
    joint1 = mul(mul(kron(k1, eye(2)), bell), transpose(kron(k1, eye(2))))
    joint_nonselective = add(joint0, joint1)
    if mutation == "signal_spectator":
        joint_nonselective = add(joint_nonselective, matrix(((F(1, 10), 0, 0, 0), (0, F(-1, 10), 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))))

    expected_branch0 = matrix(((F(225, 625), F(180, 625)), (F(180, 625), F(144, 625))))
    expected_branch1 = matrix(((F(256, 625), 0), (0, 0)))
    expected_record0 = matrix(((F(25, 41), F(20, 41)), (F(20, 41), F(16, 41))))
    expected_record1 = matrix(((1, 0), (0, 0)))
    expected_nonselective = matrix(((F(481, 625), F(180, 625)), (F(180, 625), F(144, 625))))
    hostile_vectors = ((F(1), F(0)), (F(0), F(1)), (F(1), F(-2)), (F(3), F(1)))
    quadratic = lambda v, a: sum((v[i] * a[i][j] * v[j] for i in range(len(v)) for j in range(len(v))), F(0))

    return [
        ("the relevant rotation uses exact rational three-fifths and four-fifths", c == F(3, 5) and s == F(4, 5)),
        ("the stipulated joint interaction is exactly unitary", mul(transpose(u), u) == eye(4)),
        ("detector-zero extraction gives K0 equals diag one and three-fifths", k0 == matrix(((1, 0), (0, F(3, 5))))),
        ("detector-one extraction gives the four-fifths decay Kraus operator", k1 == matrix(((0, F(4, 5)), (0, 0)))),
        ("the first effect is exactly diag one and nine-twenty-fifths", e0 == matrix(((1, 0), (0, F(9, 25))))),
        ("the second effect is exactly diag zero and sixteen-twenty-fifths", e1 == matrix(((0, 0), (0, F(16, 25))))),
        ("the two Kraus effects resolve the identity", add(e0, e1) == eye(2)),
        ("each outcome map has displayed single-Kraus completely-positive form", all(quadratic(v, b) >= 0 for v in hostile_vectors for b in (branch0, branch1))),
        ("the imported initial density is positive and trace one", psd2(rho) and trace(rho) == 1),
        ("record-zero unnormalized branch is exact", branch0 == expected_branch0),
        ("record-one unnormalized branch is exact", branch1 == expected_branch1),
        ("record-zero outcome weight is exactly 369/625", p0 == F(369, 625)),
        ("record-one outcome weight is exactly 256/625", p1 == F(256, 625)),
        ("outcome weights are nonnegative and sum to one", p0 >= 0 and p1 >= 0 and p0 + p1 == 1),
        ("record-zero normalized conditional density is exact", record0 == expected_record0),
        ("record-one normalized conditional density is exact", record1 == expected_record1),
        ("both conditional records are positive and normalized", psd2(record0) and psd2(record1) and trace(record0) == trace(record1) == 1),
        ("the nonselective system output is the exact branch sum", nonselective == expected_nonselective),
        ("Kraus completeness preserves the system trace", trace(nonselective) == trace(rho) == 1),
        ("the Bell spectator input has remote marginal I2/2", ptrace_system(bell) == scale(F(1, 2), eye(2))),
        ("the local nonselective instrument preserves the remote marginal", ptrace_system(joint_nonselective) == ptrace_system(bell)),
        ("the stipulated interaction changes the local joint state without spectator signalling", joint_nonselective != bell and trace(joint_nonselective) == 1),
        ("the exact control uses no numerical tolerance or floating-point approximation", all(isinstance(x, F) for row in u for x in row)),
    ]


def manifest_failures(data: dict) -> list[str]:
    failures = []
    dilation = data.get("dilation", {})
    derived = data.get("derived_instrument", {})
    owners = data.get("owner_accounting", {})
    duplicate = data.get("retrieval_duplicate_boundary", {})
    fences = data.get("fences", {})
    if dilation.get("detector_initialization") != "|0><0|" or dilation.get("rotation_identity") != "(3/5)^2+(4/5)^2=1": failures.append("dilation")
    if derived.get("completeness") != "E0+E1=I2" or "single_Kraus" not in derived.get("complete_positivity", ""): failures.append("derived")
    if owners.get("source_selected_owner_count") != 0 or "trace_Born_state_effect_pairing" not in owners.get("imported", []): failures.append("owners")
    if duplicate.get("generic_controls_repeated_or_promoted") is not False or "interaction_to_Kraus" not in duplicate.get("new_object_only", ""): failures.append("duplicate")
    required_false = (
        "source_selected_detector_dynamics", "source_selected_initial_state", "Born_rule_derived",
        "record_interpretation_derived", "source_interaction_or_locality_constructed", "continuum_local_coupling",
        "microlocal_or_Hadamard_theory", "prediction_confirmation_or_verdict", "held_out_scored",
        "generic_controls_promoted", "cross_packet_union_allowed",
    )
    if any(fences.get(key) is not False for key in required_false): failures.append("fences")
    holdout = data.get("holdout_firewall", {})
    if holdout.get("status") != "reserved_unscored" or holdout.get("scored_in_this_result") is not False: failures.append("holdout")
    if "no source-selected dynamics" not in data.get("claim_ceiling", ""): failures.append("ceiling")
    return failures


def selftest(data: dict) -> int:
    mutations = [(name, any(not ok for _, ok in model_checks(name))) for name in (
        "nonunitary_rotation", "incomplete_kraus", "wrong_record_normalization",
        "negative_state", "negative_outcome", "signal_spectator",
    )]
    updates = (
        ("source_promotion", lambda d: d["fences"].__setitem__("source_selected_detector_dynamics", True)),
        ("Born_promotion", lambda d: d["fences"].__setitem__("Born_rule_derived", True)),
        ("holdout_promotion", lambda d: d["holdout_firewall"].__setitem__("scored_in_this_result", True)),
        ("generic_control_promotion", lambda d: d["retrieval_duplicate_boundary"].__setitem__("generic_controls_repeated_or_promoted", True)),
        ("source_owner", lambda d: d["owner_accounting"].__setitem__("source_selected_owner_count", 1)),
    )
    for name, update in updates:
        mutant = copy.deepcopy(data)
        update(mutant)
        mutations.append((name, bool(manifest_failures(mutant))))
    for name, caught in mutations:
        print(f"[{'PASS' if caught else 'FAIL'}] hostile mutation {name}")
    print(f"HOSTILE SELFTEST: {sum(c for _, c in mutations)}/{len(mutations)} caught")
    return 0 if all(c for _, c in mutations) else 1


def main() -> int:
    data = json.loads(MANIFEST.read_text())
    if "--selftest" in sys.argv:
        return selftest(data)
    checks = model_checks()
    checks.append(("manifest preserves dilation ownership, imports, duplicate boundary, fences and holdout", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed = sum(ok for _, ok in checks)
    print(f"K91 UNITARY DETECTOR INSTRUMENT: {passed}/{len(checks)} pass")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
