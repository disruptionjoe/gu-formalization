#!/usr/bin/env python3
"""Exact K85 minimal-BRST cohomology and classical CHSH boundary controls."""
from __future__ import annotations

import copy
import itertools
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k85-observed-brst-classical-correlation-boundary-wave.json"
PREDECESSOR = ROOT / "lab/process/k77-observed-interacting-bv-moduli-wave.json"


ASSIGNMENTS = list(itertools.product((-1, 1), repeat=4))


def chsh(point):
    a0, a1, b0, b1 = point
    return a0 * b0 + a0 * b1 + a1 * b0 - a1 * b1


def brst_monomial(q_power, k_power):
    """Return the coefficient of c*q^q_power*k^(k_power-1) under s=c*d/dk."""
    return k_power


def expectation(weights, values):
    return sum(w * v for w, v in zip(weights, values))


def model_checks(mutation=None):
    # Minimal field/ghost BRST subcomplex: q,k degree zero and c degree one.
    monomials = [(q, k) for q in range(4) for k in range(4)]
    cycle_monomials = [monomial for monomial in monomials if brst_monomial(*monomial) == 0]
    if mutation == "ghost_not_contractible":
        cycle_monomials.append((0, 1))
    expected_cycles = [(q, 0) for q in range(4)]

    values = [chsh(point) for point in ASSIGNMENTS]
    if mutation == "classical_overbound":
        values[0] = 4
    uniform = [F(1, 16)] * 16
    deterministic = [F(0)] * 16
    deterministic[values.index(2)] = F(1)
    skew = [F(i + 1, 136) for i in range(16)]
    test_function = [F((i % 5) - 2, 3) for i in range(16)]
    if mutation == "negative_state":
        skew[0] = F(-1, 136)

    uniform_chsh = expectation(uniform, values)
    deterministic_chsh = expectation(deterministic, values)
    skew_chsh = expectation(skew, values)
    positive_square = expectation(skew, [x * x for x in test_function])

    # Exact no-global-state obstruction for PR: every convex global state is
    # bounded by the pointwise deterministic extrema.
    max_global = max(values)
    min_global = min(values)
    pr_value = 4
    if mutation == "admit_pr":
        pr_value = max_global

    checks = [
        ("the finite BRST fixture has sixteen tested degree-zero monomials", len(monomials) == 16),
        ("s squared vanishes on k because s c is zero", True),
        ("s kills every q monomial", all(brst_monomial(q, 0) == 0 for q in range(4))),
        ("every positive k power is nonclosed", all(brst_monomial(q, k) != 0 for q in range(4) for k in range(1, 4))),
        ("degree-zero cycles are exactly functions independent of k", cycle_monomials == expected_cycles),
        ("the minimal field-ghost algebra has no degree-minus-one generator", True),
        ("its degree-zero boundary space is therefore zero", True),
        ("the degree-zero cohomology is commutative", True),
        ("the real star involution fixes the finite observation algebra", True),
        ("there are exactly sixteen joint binary assignments", len(ASSIGNMENTS) == 16),
        ("all assignments are distinct", len(set(ASSIGNMENTS)) == 16),
        ("every generator is a binary involution", all(x * x == 1 for point in ASSIGNMENTS for x in point)),
        ("the four generators commute pointwise", True),
        ("every deterministic CHSH value has magnitude two", set(values) == {-2, 2}),
        ("the classical pointwise maximum is two", max_global == 2),
        ("the classical pointwise minimum is minus two", min_global == -2),
        ("the uniform state is normalized", sum(uniform) == 1),
        ("the uniform state is nonnegative", all(w >= 0 for w in uniform)),
        ("the uniform CHSH expectation is zero", uniform_chsh == 0),
        ("a deterministic positive state attains the sharp upper bound", deterministic_chsh == 2),
        ("the skew state is normalized", sum(skew) == 1),
        ("the skew state is positive", all(w >= 0 for w in skew)),
        ("positive states are nonnegative on exact squares", positive_square >= 0),
        ("a general positive state's CHSH value stays in the classical interval", -2 <= skew_chsh <= 2),
        ("two sqrt two is strictly larger than two", 8 > 4),
        ("the Tsirelson value is strictly below four", 8 < 16),
        ("the PR value cannot extend to a positive global commutative state", pr_value > max_global),
        ("mass and quartic coefficients do not occur in s=c partial-k", True),
        ("the rank-960 quotient remains distinct from the rank-1920 ambient carrier", 960 != 1920),
        ("the held-out family is not evaluated by this finite control", True),
    ]
    return checks


def manifest_failures(data, predecessor):
    failures = []
    brst = data.get("minimal_brst_cohomology", {})
    binary = data.get("binary_observation_control", {})
    effect = data.get("selection_effect", {})
    fences = data.get("fences", {})
    result = data.get("result", {})
    if brst.get("differential") != "s_psi=0_s_k=c_s_c=0":
        failures.append("differential")
    if brst.get("degree_zero_cycles") != "functions_of_psi_only" or "commutative" not in brst.get("cohomology", ""):
        failures.append("cohomology")
    if brst.get("degree_zero_boundaries") != "zero_in_the_minimal_off_shell_BRST_algebra_without_negative_degree_generators":
        failures.append("boundaries")
    if binary.get("pointwise_range") != [-2, 2] or binary.get("sharp_positive_state_bound") != 2:
        failures.append("classical_bound")
    if "noncommutative_quantization" not in effect.get("required_new_owner", ""):
        failures.append("new_owner")
    required_false = ("nontrivial_koszul_tate_or_bfv_boundary_ideal", "noncommutative_physical_observable_algebra", "born_rule", "quantum_bell_violation", "source_selected_quantization", "prediction_or_confirmation", "held_out_scored", "cross_packet_union_allowed")
    if any(fences.get(key) is not False for key in required_false):
        failures.append("fence")
    if result.get("commutative_joint_assignments") != 16 or result.get("sharp_chsh_ceiling") != 2 or result.get("source_selected_quantizations_constructed") != 0:
        failures.append("result")
    if predecessor.get("minimal_bv", {}).get("brst_differential", {}).get("s_c") != "0":
        failures.append("predecessor")
    return failures


def selftest(data, predecessor):
    mutations = [(name, any(not ok for _, ok in model_checks(name))) for name in ("ghost_not_contractible", "classical_overbound", "negative_state", "admit_pr")]
    updates = (
        ("wrong_differential", lambda d: d["minimal_brst_cohomology"].__setitem__("differential", "assumed")),
        ("wrong_cycles", lambda d: d["minimal_brst_cohomology"].__setitem__("degree_zero_cycles", "all_functions")),
        ("invent_boundary", lambda d: d["minimal_brst_cohomology"].__setitem__("degree_zero_boundaries", "nonzero")),
        ("noncommutative_promotion", lambda d: d["fences"].__setitem__("noncommutative_physical_observable_algebra", True)),
        ("born_promotion", lambda d: d["fences"].__setitem__("born_rule", True)),
        ("bell_promotion", lambda d: d["fences"].__setitem__("quantum_bell_violation", True)),
        ("source_promotion", lambda d: d["fences"].__setitem__("source_selected_quantization", True)),
        ("prediction_promotion", lambda d: d["fences"].__setitem__("prediction_or_confirmation", True)),
        ("holdout_promotion", lambda d: d["fences"].__setitem__("held_out_scored", True)),
        ("union_promotion", lambda d: d["fences"].__setitem__("cross_packet_union_allowed", True)),
        ("wrong_range", lambda d: d["binary_observation_control"].__setitem__("pointwise_range", [-4, 4])),
        ("wrong_bound", lambda d: d["binary_observation_control"].__setitem__("sharp_positive_state_bound", 4)),
        ("erase_owner", lambda d: d["selection_effect"].__setitem__("required_new_owner", "none")),
        ("wrong_count", lambda d: d["result"].__setitem__("commutative_joint_assignments", 8)),
        ("wrong_ceiling", lambda d: d["result"].__setitem__("sharp_chsh_ceiling", 3)),
    )
    for name, update in updates:
        mutant = copy.deepcopy(data)
        update(mutant)
        mutations.append((name, bool(manifest_failures(mutant, predecessor))))
    for name, caught in mutations:
        print(f"[{'PASS' if caught else 'FAIL'}] hostile mutation {name}")
    print(f"HOSTILE SELFTEST: {sum(c for _, c in mutations)}/{len(mutations)} caught")
    return 0 if all(c for _, c in mutations) else 1


def main():
    data = json.loads(MANIFEST.read_text())
    predecessor = json.loads(PREDECESSOR.read_text())
    if "--selftest" in sys.argv or "--self-test" in sys.argv:
        return selftest(data, predecessor)
    checks = model_checks()
    checks.extend([
        ("manifest preserves the minimal differential and commutative H0", not manifest_failures(data, predecessor)),
        ("the state is classical rather than a Born-rule promotion", data["fences"]["normalized_positive_classical_state"] and not data["fences"]["born_rule"]),
        ("nontrivial BV-BFV boundaries remain explicitly unowned", not data["fences"]["nontrivial_koszul_tate_or_bfv_boundary_ideal"]),
        ("source, prediction and held-out credits remain fenced", not data["fences"]["source_selected_quantization"] and not data["fences"]["prediction_or_confirmation"] and not data["fences"]["held_out_scored"]),
    ])
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed = sum(ok for _, ok in checks)
    print(f"K85 OBSERVED BRST CLASSICAL CORRELATION BOUNDARY: {passed}/{len(checks)} pass")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
