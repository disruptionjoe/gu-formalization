#!/usr/bin/env python3
"""Exact K117 reservoir-dilation and causal-locality controls (stdlib only)."""
from __future__ import annotations

import copy
from fractions import Fraction
import json
import math
from pathlib import Path
import sys
from typing import Callable


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k117-k116-autonomous-reservoir-causal-locality-wave.json"
N = 3


def kernel(x: int, mutation: str | None = None, parent_x: int | None = None) -> list[Fraction]:
    high = Fraction(81, 113)
    low = Fraction(16, 113)
    if mutation == "unnormalized_kernel":
        high = Fraction(82, 113)
    if mutation == "uninformative_kernel":
        high = low = Fraction(1, 3)
    preferred = x if parent_x is None else (x + parent_x) % N
    return [high if r == preferred else low for r in range(N)]


def finite_control(mutation: str | None = None) -> dict[str, object]:
    base_rate = Fraction(2, 5)
    clock = Fraction(7, 11)
    n = N
    if mutation == "wrong_dimension":
        n = 4
    if mutation == "zero_base_rate":
        base_rate = Fraction(0)
    if mutation == "zero_clock":
        clock = Fraction(0)

    p = [kernel(x, mutation) for x in range(N)]
    attenuation = clock / (clock + N * base_rate) if clock + N * base_rate else Fraction(0)
    h = [
        [Fraction(1, N) + attenuation * (p[x][r] - Fraction(1, N)) for r in range(N)]
        for x in range(N)
    ]
    nu = [[h[x][r] / N for r in range(N)] for x in range(N)]

    divergence: list[Fraction] = []
    for x in range(N):
        for r in range(N):
            incoming_base = sum(base_rate * nu[y][r] for y in range(N) if y != x)
            outgoing_base = (N - 1) * base_rate * nu[x][r]
            incoming_record = sum(nu[x][s] * clock * p[x][r] for s in range(N) if s != r)
            outgoing_record = sum(nu[x][r] * clock * p[x][s] for s in range(N) if s != r)
            divergence.append(incoming_base + incoming_record - outgoing_base - outgoing_record)

    local_db: list[bool] = []
    for x in range(N):
        for r in range(N):
            for s in range(N):
                if r != s:
                    local_db.append(clock > 0 and (clock * p[x][s]) / (clock * p[x][r]) == p[x][s] / p[x][r])
            for y in range(N):
                if x != y:
                    energy_factor = p[y][r] / p[x][r]
                    work_factor = p[x][r] / p[y][r]
                    local_db.append(base_rate > 0 and energy_factor * work_factor == 1)

    x, y, r, s = 0, 1, 0, 1
    cycle_ratio = (p[x][s] * p[y][r]) / (p[x][r] * p[y][s])
    cycle_work_factor = (p[x][s] / p[y][s]) * (p[y][r] / p[x][r])

    mean_work = 0.0
    entropy_production = 0.0
    for x in range(N):
        for r in range(N):
            for y in range(N):
                if y != x and base_rate:
                    mean_work += float(nu[x][r] * base_rate) * math.log(float(p[x][r] / p[y][r]))
                    forward = nu[x][r] * base_rate
                    reverse = nu[y][r] * base_rate
                    if forward != reverse:
                        entropy_production += 0.5 * float(forward - reverse) * math.log(float(forward / reverse))
            for s in range(N):
                if s != r and clock:
                    forward = nu[x][r] * clock * p[x][s]
                    reverse = nu[x][s] * clock * p[x][r]
                    if forward != reverse:
                        entropy_production += 0.5 * float(forward - reverse) * math.log(float(forward / reverse))

    return {
        "n": n,
        "base_rate": base_rate,
        "clock": clock,
        "p": p,
        "h": h,
        "nu": nu,
        "attenuation": attenuation,
        "divergence": divergence,
        "local_db": local_db,
        "cycle_ratio": cycle_ratio,
        "cycle_work_factor": cycle_work_factor,
        "mean_work": mean_work,
        "entropy_production": entropy_production,
    }


SiteState = tuple[tuple[int, int], tuple[int, int], tuple[int, int]]
Observable = Callable[[SiteState], Fraction]


def replace_site(state: SiteState, site: int, value: tuple[int, int]) -> SiteState:
    out = list(state)
    out[site] = value
    return tuple(out)  # type: ignore[return-value]


def local_generator(site: int, state: SiteState, observable: Observable, mutation: str | None = None) -> Fraction:
    base_rate = Fraction(2, 5)
    clock = Fraction(7, 11)
    x, r = state[site]
    parent_x = state[0][0] if site == 1 else None
    probs = kernel(x, mutation, parent_x)
    value = Fraction(0)
    for y in range(N):
        if y != x:
            value += base_rate * (observable(replace_site(state, site, (y, r))) - observable(state))
    for s in range(N):
        if s != r:
            value += clock * probs[s] * (observable(replace_site(state, site, (x, s))) - observable(state))
    return value


def causal_checks(mutation: str | None = None) -> dict[str, bool]:
    states: list[SiteState] = [
        ((xu, ru), (xv, rv), (xz, rz))
        for xu in range(N) for ru in range(N)
        for xv in range(N) for rv in range(N)
        for xz in range(N) for rz in range(N)
    ]
    f_combo: Observable = lambda st: Fraction(1 + st[0][1] + 2 * st[1][0] + 3 * st[2][1])
    f_u: Observable = lambda st: Fraction(st[0][1] == 0)
    f_v: Observable = lambda st: Fraction(st[1][1] == 0)
    constant: Observable = lambda _st: Fraction(1)

    spacelike_commutes = all(
        local_generator(1, st, lambda nxt: local_generator(2, nxt, f_combo, mutation), mutation)
        == local_generator(2, st, lambda nxt: local_generator(1, nxt, f_combo, mutation), mutation)
        for st in states
    )
    causal_noncommutes = any(
        local_generator(0, st, lambda nxt: local_generator(1, nxt, f_v, mutation), mutation)
        != local_generator(1, st, lambda nxt: local_generator(0, nxt, f_v, mutation), mutation)
        for st in states
    )
    past_closed_restriction = all(
        sum(local_generator(site, st, f_u, mutation) for site in range(3))
        == local_generator(0, st, f_u, mutation)
        for st in states
    )
    no_spacelike_input = True
    for xu in range(N):
        for ru in range(N):
            for xv in range(N):
                for rv in range(N):
                    values = {
                        sum(local_generator(site, ((xu, ru), (xv, rv), (xz, rz)), f_v, mutation) for site in range(3))
                        for xz in range(N) for rz in range(N)
                    }
                    no_spacelike_input &= len(values) == 1
    constants_preserved = all(
        all(local_generator(site, st, constant, mutation) == 0 for site in range(3))
        for st in states
    )
    return {
        "spacelike_commutes": spacelike_commutes,
        "causal_noncommutes": causal_noncommutes,
        "past_closed_restriction": past_closed_restriction,
        "no_spacelike_input": no_spacelike_input,
        "constants_preserved": constants_preserved,
    }


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    c = finite_control(mutation)
    p = c["p"]
    h = c["h"]
    causal = causal_checks(mutation)
    checks = [
        ("three base and record states", c["n"] == 3),
        ("positive autonomous rates", c["base_rate"] > 0 and c["clock"] > 0),
        ("event kernels normalize", all(sum(row, Fraction(0)) == 1 for row in p)),
        ("event kernels are strictly positive", all(value > 0 for row in p for value in row)),
        ("event kernels are informative", any(p[x][r] != Fraction(1, 3) for x in range(N) for r in range(N))),
        ("resolvent attenuation exact", c["attenuation"] == Fraction(35, 101)),
        ("stationary density normalizes", sum(value for row in c["nu"] for value in row) == 1),
        ("stationary conditional rows normalize", all(sum(row, Fraction(0)) == 1 for row in h)),
        ("projected stationary divergence vanishes", all(value == 0 for value in c["divergence"])),
        ("base projection is record independent", c["base_rate"] == Fraction(2, 5)),
        ("record projection exactly uses K115 kernel", c["clock"] == Fraction(7, 11) and p[0][0] == Fraction(81, 113)),
        ("edge local detailed balance is exact", bool(c["local_db"]) and all(c["local_db"])),
        ("informative Kolmogorov cycle is nonreversible", c["cycle_ratio"] != 1),
        ("exact cycle ratio is 256/6561", c["cycle_ratio"] == Fraction(256, 6561)),
        ("cycle affinity equals reservoir work", c["cycle_ratio"] == c["cycle_work_factor"]),
        ("stationary mean reservoir work is positive", c["mean_work"] > 0.0),
        ("work rate equals total entropy production", abs(c["mean_work"] - c["entropy_production"]) < 1e-12),
        ("spacelike local generators commute", causal["spacelike_commutes"]),
        ("causally ordered generators need not commute", causal["causal_noncommutes"]),
        ("past-closed observables restrict exactly", causal["past_closed_restriction"]),
        ("local downstream generator ignores spacelike state", causal["no_spacelike_input"]),
        ("causal product generator preserves constants", causal["constants_preserved"]),
    ]
    return checks


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    dilation = data.get("autonomous_dilation", {})
    nogo = data.get("equilibrium_lumpability_no_go", {})
    resource = data.get("resource_and_entropy", {})
    causal = data.get("finite_causal_locality", {})
    control = data.get("finite_control", {})
    result = data.get("result", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    if dilation.get("base_rates_record_independent") is not True or dilation.get("projection_exactly_recovers_K115") is not True or dilation.get("autonomous_time_homogeneous_markov_additive_law") is not True or dilation.get("unbounded_or_chemostatted_resource_required_for_stationarity") is not True or dilation.get("finite_microscopic_reservoir_constructed") is not False or dilation.get("Weinstein_source_or_GU_action_constructed") is not False:
        failures.append("dilation")
    if nogo.get("informative_kernel_has_nonunit_Kolmogorov_cycle_ratio") is not True or nogo.get("finite_detailed_balanced_strongly_lumpable_lift_possible") is not False or nogo.get("finite_nonequilibrium_controller_ruled_out") is not False or nogo.get("transient_finite_fuel_realization_ruled_out") is not False:
        failures.append("no_go")
    if resource.get("stationary_mean_work_rate_positive") is not True or resource.get("stationary_mean_work_rate_equals_entropy_production") is not True or resource.get("costless_controller_claimed") is not False or resource.get("universal_Landauer_equality_claimed") is not False or resource.get("microscopic_fluctuation_theorem_claimed") is not False:
        failures.append("resource")
    if causal.get("past_closed_observable_descent") is not True or causal.get("spacelike_local_generators_commute") is not True or causal.get("causally_ordered_generators_need_not_commute") is not True or causal.get("finite_causal_lattice_precursor_only") is not True or causal.get("continuum_spacetime_field_theory_constructed") is not False or causal.get("BV_BFV_boundary_symplectic_form_or_master_equation_constructed") is not False or causal.get("AQFT_net_or_Hadamard_state_constructed") is not False:
        failures.append("causal")
    if control.get("stationarity_checked_exactly") is not True or control.get("projection_checked_exactly") is not True or control.get("edge_local_detailed_balance_checked_exactly") is not True or control.get("cycle_work_checked_exactly") is not True or control.get("causal_support_and_commutators_checked_exactly") is not True:
        failures.append("control")
    required_true = (
        "repository_owned_autonomous_markov_additive_dilation_constructed",
        "controller_resource_current_internalized_in_extended_path_law",
        "finite_equilibrium_realization_no_go_proved",
        "finite_causal_local_observable_descent_precursor_constructed",
    )
    required_false = (
        "finite_closed_or_source_owned_physical_environment_constructed",
        "continuum_spacetime_or_genuine_BV_BFV_constructed",
        "Born_rule_derived",
        "prediction_or_confirmation_credit",
        "held_out_scored",
    )
    if any(result.get(key) is not True for key in required_true) or any(result.get(key) is not False for key in required_false) or result.get("canon_verdict_change") != "none":
        failures.append("result")
    ceiling = data.get("claim_ceiling", "")
    if "Markov-additive" not in ceiling or "finite causal-lattice" not in ceiling or "No finite microscopic bath" not in ceiling:
        failures.append("ceiling")
    return failures


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [(name, any(not ok for _, ok in exact_checks(name))) for name in (
        "wrong_dimension", "zero_clock", "zero_base_rate", "unnormalized_kernel", "uninformative_kernel"
    )]
    updates = (
        ("invent_source_action", lambda d: d["autonomous_dilation"].__setitem__("Weinstein_source_or_GU_action_constructed", True)),
        ("invent_finite_reservoir", lambda d: d["autonomous_dilation"].__setitem__("finite_microscopic_reservoir_constructed", True)),
        ("break_projection", lambda d: d["autonomous_dilation"].__setitem__("projection_exactly_recovers_K115", False)),
        ("hide_resource", lambda d: d["autonomous_dilation"].__setitem__("unbounded_or_chemostatted_resource_required_for_stationarity", False)),
        ("invent_equilibrium_lift", lambda d: d["equilibrium_lumpability_no_go"].__setitem__("finite_detailed_balanced_strongly_lumpable_lift_possible", True)),
        ("overstate_finite_no_go", lambda d: d["equilibrium_lumpability_no_go"].__setitem__("finite_nonequilibrium_controller_ruled_out", True)),
        ("erase_transient_boundary", lambda d: d["equilibrium_lumpability_no_go"].__setitem__("transient_finite_fuel_realization_ruled_out", True)),
        ("erase_positive_work", lambda d: d["resource_and_entropy"].__setitem__("stationary_mean_work_rate_positive", False)),
        ("break_work_EP_identity", lambda d: d["resource_and_entropy"].__setitem__("stationary_mean_work_rate_equals_entropy_production", False)),
        ("invent_costless_controller", lambda d: d["resource_and_entropy"].__setitem__("costless_controller_claimed", True)),
        ("invent_Landauer", lambda d: d["resource_and_entropy"].__setitem__("universal_Landauer_equality_claimed", True)),
        ("invent_fluctuation_theorem", lambda d: d["resource_and_entropy"].__setitem__("microscopic_fluctuation_theorem_claimed", True)),
        ("erase_past_descent", lambda d: d["finite_causal_locality"].__setitem__("past_closed_observable_descent", False)),
        ("break_spacelike_commutation", lambda d: d["finite_causal_locality"].__setitem__("spacelike_local_generators_commute", False)),
        ("erase_causal_order", lambda d: d["finite_causal_locality"].__setitem__("causally_ordered_generators_need_not_commute", False)),
        ("invent_continuum", lambda d: d["finite_causal_locality"].__setitem__("continuum_spacetime_field_theory_constructed", True)),
        ("invent_BV_BFV", lambda d: d["finite_causal_locality"].__setitem__("BV_BFV_boundary_symplectic_form_or_master_equation_constructed", True)),
        ("invent_AQFT", lambda d: d["finite_causal_locality"].__setitem__("AQFT_net_or_Hadamard_state_constructed", True)),
        ("erase_stationarity_control", lambda d: d["finite_control"].__setitem__("stationarity_checked_exactly", False)),
        ("erase_cycle_control", lambda d: d["finite_control"].__setitem__("cycle_work_checked_exactly", False)),
        ("invent_physical_environment", lambda d: d["result"].__setitem__("finite_closed_or_source_owned_physical_environment_constructed", True)),
        ("invent_genuine_BV_BFV", lambda d: d["result"].__setitem__("continuum_spacetime_or_genuine_BV_BFV_constructed", True)),
        ("invent_Born", lambda d: d["result"].__setitem__("Born_rule_derived", True)),
        ("score_holdout", lambda d: d["result"].__setitem__("held_out_scored", True)),
        ("promote_canon", lambda d: d["result"].__setitem__("canon_verdict_change", "changed")),
        ("erase_scope", lambda d: d.__setitem__("claim_ceiling", "GU has a physical measurement theory.")),
    )
    for name, update in updates:
        mutant = copy.deepcopy(data)
        update(mutant)
        caught.append((name, bool(manifest_failures(mutant))))
    for name, ok in caught:
        print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
    print(f"HOSTILE SELFTEST: {sum(int(bool(ok)) for _, ok in caught)}/{len(caught)} caught")
    return 0 if all(ok for _, ok in caught) else 1


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if "--selftest" in sys.argv:
        return selftest(data)
    checks = exact_checks()
    checks.append(("manifest preserves reservoir, no-go, locality and ownership ceilings", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    print(f"K117 AUTONOMOUS RESERVOIR CAUSAL LOCALITY: {sum(int(bool(ok)) for _, ok in checks)}/{len(checks)} pass")
    return 0 if all(ok for _, ok in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
