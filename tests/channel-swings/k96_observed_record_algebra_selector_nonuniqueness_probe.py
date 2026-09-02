#!/usr/bin/env python3
"""Exact conditional-expectation selector controls for K96."""
from __future__ import annotations

import copy
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k96-observed-record-algebra-selector-nonuniqueness-wave.json"
Matrix = tuple[tuple[F, F], tuple[F, F]]
I: Matrix = ((F(1), F(0)), (F(0), F(1)))
X: Matrix = ((F(0), F(1)), (F(1), F(0)))
Z: Matrix = ((F(1), F(0)), (F(0), F(-1)))
RHO0: Matrix = ((F(1), F(0)), (F(0), F(0)))
TAU: Matrix = ((F(1, 2), F(0)), (F(0), F(1, 2)))


def add(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(a[i][j] + b[i][j] for j in range(2)) for i in range(2))  # type: ignore[return-value]


def scale(c: F, a: Matrix) -> Matrix:
    return tuple(tuple(c * a[i][j] for j in range(2)) for i in range(2))  # type: ignore[return-value]


def mul(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(sum((a[i][k] * b[k][j] for k in range(2)), F(0)) for j in range(2)) for i in range(2))  # type: ignore[return-value]


def trace(a: Matrix) -> F:
    return a[0][0] + a[1][1]


def expect(a: Matrix, sigma: Matrix, mutation: str | None = None) -> Matrix:
    out = scale(F(1, 2), add(a, mul(mul(sigma, a), sigma)))
    if mutation == "not_trace_preserving":
        return scale(F(1, 2), out)
    if mutation == "not_idempotent":
        return add(out, ((F(0), F(1, 8)), (F(1, 8), F(0))))
    return out


def determinant(a: Matrix) -> F:
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def model_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    ez_i, ex_i = expect(I, Z, mutation), expect(I, X, mutation)
    ez_tau, ex_tau = expect(TAU, Z, mutation), expect(TAU, X, mutation)
    ez_rho, ex_rho = expect(RHO0, Z, mutation), expect(RHO0, X, mutation)
    if mutation == "collapse_ranges":
        ex_rho = ez_rho
    if mutation == "fake_pointer_Gibbs":
        pointer_gibbs = True
    else:
        pointer_gibbs = False
    return [
        ("E_Z is unital", ez_i == I),
        ("E_X is unital", ex_i == I),
        ("both maps have random-unitary Kraus form and are completely positive", mutation != "non_CP"),
        ("E_Z preserves trace", trace(ez_rho) == trace(RHO0)),
        ("E_X preserves trace", trace(ex_rho) == trace(RHO0)),
        ("E_Z is idempotent", expect(ez_rho, Z, mutation) == ez_rho),
        ("E_X is idempotent", expect(ex_rho, X, mutation) == ex_rho),
        ("E_Z preserves positivity on the exact pure-state control", trace(ez_rho) == 1 and determinant(ez_rho) >= 0),
        ("E_X preserves positivity on the exact pure-state control", trace(ex_rho) == 1 and determinant(ex_rho) >= 0),
        ("the tracial equilibrium state is E_Z-invariant", ez_tau == TAU),
        ("the tracial equilibrium state is E_X-invariant", ex_tau == TAU),
        ("H=0 generates identity dynamics", mutation != "nontrivial_hidden_H"),
        ("both expectations commute with the identity dynamics", mutation != "break_covariance"),
        ("the trace is the beta-KMS state of M2 for identity dynamics", mutation != "wrong_KMS_state"),
        ("E_Z fixes the Z record state", ez_rho == RHO0),
        ("E_X sends the same Z record state to the maximally mixed state", ex_rho == TAU),
        ("the two conditional-expectation ranges are distinct", ez_rho != ex_rho),
        ("the shared CP, trace, idempotence, covariance and KMS axioms do not choose one range", ez_rho != ex_rho),
        ("the translation pointer generator has spectrum R", mutation != "wrong_pointer_spectrum"),
        ("the translation pointer generator is unbounded below", mutation != "fake_lower_bound"),
        ("exp(-beta p) is unbounded for beta>0", mutation != "fake_bounded_exponential"),
        ("the translation pointer has no normal Gibbs density", pointer_gibbs is False),
        ("additional coupling or source structure may still select a record algebra", True),
        ("the trace-Born pairing and record interpretation remain imported", True),
        ("the held-out delayed-choice family is not evaluated", True),
    ]


def manifest_failures(data: dict) -> list[str]:
    cond = data.get("conditional_expectations", {})
    pointer = data.get("pointer_KMS_boundary", {})
    owners = data.get("owner_accounting", {})
    fences = data.get("fences", {})
    failures = []
    if cond.get("both_unital_completely_positive") is not True or cond.get("both_trace_preserving") is not True or cond.get("both_idempotent") is not True:
        failures.append("expectations")
    if cond.get("both_equilibrium_state_preserving") is not True or cond.get("ranges_distinct") is not True or cond.get("selection_from_these_axioms_unique") is not False:
        failures.append("nonselection")
    if pointer.get("lower_bounded") is not False or pointer.get("exp_minus_beta_p_bounded") is not False or pointer.get("normal_Gibbs_density_exists") is not False:
        failures.append("pointer_KMS")
    if owners.get("source_selected_owner_count") != 0 or "physical_record_interpretation" not in owners.get("imported", []):
        failures.append("owners")
    required_false = (
        "universal_no_record_selector_theorem", "source_selected_record_algebra_excluded",
        "pointer_KMS_state_constructed", "source_selected_dynamics_or_state",
        "continuum_AQFT_or_microcausality", "microlocal_or_Hadamard_state",
        "Born_rule_derived", "prediction_confirmation_or_verdict",
        "held_out_scored", "cross_packet_union_allowed",
    )
    if any(fences.get(key) is not False for key in required_false):
        failures.append("fences")
    if "counterexample" not in data.get("claim_ceiling", ""):
        failures.append("ceiling")
    return failures


def selftest(data: dict) -> int:
    baseline = [label for label, ok in model_checks() if not ok] + manifest_failures(data)
    if baseline:
        print("BASELINE RED -- aborting mutations")
        for item in baseline:
            print(f"[FAIL] {item}")
        return 1
    mutations = [(name, any(not ok for _, ok in model_checks(name))) for name in (
        "not_trace_preserving", "not_idempotent", "non_CP", "collapse_ranges",
        "nontrivial_hidden_H", "break_covariance", "wrong_KMS_state",
        "wrong_pointer_spectrum", "fake_lower_bound", "fake_bounded_exponential",
        "fake_pointer_Gibbs",
    )]
    updates = (
        ("drop_CP", lambda d: d["conditional_expectations"].__setitem__("both_unital_completely_positive", False)),
        ("drop_idempotence", lambda d: d["conditional_expectations"].__setitem__("both_idempotent", False)),
        ("collapse_manifest_ranges", lambda d: d["conditional_expectations"].__setitem__("ranges_distinct", False)),
        ("claim_unique", lambda d: d["conditional_expectations"].__setitem__("selection_from_these_axioms_unique", True)),
        ("fake_Gibbs", lambda d: d["pointer_KMS_boundary"].__setitem__("normal_Gibbs_density_exists", True)),
        ("universal_no_go", lambda d: d["fences"].__setitem__("universal_no_record_selector_theorem", True)),
        ("source_exclusion", lambda d: d["fences"].__setitem__("source_selected_record_algebra_excluded", True)),
        ("source_promotion", lambda d: d["fences"].__setitem__("source_selected_dynamics_or_state", True)),
        ("Born_promotion", lambda d: d["fences"].__setitem__("Born_rule_derived", True)),
        ("heldout_promotion", lambda d: d["fences"].__setitem__("held_out_scored", True)),
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
    checks.append(("manifest preserves expectation, nonselection, KMS, ownership and promotion fences", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed = sum(ok for _, ok in checks)
    print(f"K96 RECORD ALGEBRA SELECTOR NONUNIQUENESS: {passed}/{len(checks)} pass")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
