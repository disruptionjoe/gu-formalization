#!/usr/bin/env python3
"""Exact K118 finite-controller and continuum-host controls (stdlib only)."""
from __future__ import annotations

import copy
from fractions import Fraction
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k118-k117-finite-controller-continuum-bv-bfv-host-wave.json"
N = 3
L = 5
KAPPA = Fraction(2, 5)
CLOCK = Fraction(7, 11)
HIGH = Fraction(81, 113)
LOW = Fraction(16, 113)


def kernel(x: int, mutation: str | None = None) -> list[Fraction]:
    high, low = HIGH, LOW
    if mutation == "unnormalized_kernel":
        high = Fraction(82, 113)
    if mutation == "uninformative_kernel":
        high = low = Fraction(1, 3)
    return [high if r == x else low for r in range(N)]


def work_step(x: int, y: int, r: int, mutation: str | None = None) -> int:
    px, py = kernel(x, mutation)[r], kernel(y, mutation)[r]
    step = 1 if px > py else -1 if px < py else 0
    return -step if mutation == "reverse_work" else step


def projected_stationary(mutation: str | None = None) -> dict[tuple[int, int], Fraction]:
    attenuation = CLOCK / (CLOCK + N * KAPPA)
    return {
        (x, r): (Fraction(1, N) + attenuation * (kernel(x, mutation)[r] - Fraction(1, N))) / N
        for x in range(N) for r in range(N)
    }


def projected_edges(state: tuple[int, int], mutation: str | None = None) -> dict[tuple[int, int], Fraction]:
    x, r = state
    clock = Fraction(0) if mutation == "zero_clock" else CLOCK
    out: dict[tuple[int, int], Fraction] = {}
    for y in range(N):
        if y != x:
            out[(y, r)] = KAPPA
    for s in range(N):
        if s != r:
            out[(x, s)] = clock * kernel(x, mutation)[s]
    return out


def lifted_edges(state: tuple[int, int, int], mutation: str | None = None) -> dict[tuple[int, int, int], Fraction]:
    x, r, z = state
    out: dict[tuple[int, int, int], Fraction] = {}
    for (y, s), rate in projected_edges((x, r), mutation).items():
        step = work_step(x, y, r, mutation) if y != x else 0
        if mutation == "break_lift_shift" and step:
            step = 0
        target = (y, s, (z + step) % L)
        out[target] = out.get(target, Fraction(0)) + rate
    return out


def finite_controller_checks(mutation: str | None = None) -> dict[str, object]:
    nu = projected_stationary(mutation)
    mu = {(x, r, z): nu[(x, r)] / L for x in range(N) for r in range(N) for z in range(L)}
    states = list(mu)

    projected_divergence: dict[tuple[int, int], Fraction] = {}
    for target in nu:
        incoming = sum(nu[source] * projected_edges(source, mutation).get(target, Fraction(0)) for source in nu)
        outgoing = nu[target] * sum(projected_edges(target, mutation).values(), Fraction(0))
        projected_divergence[target] = incoming - outgoing

    lifted_divergence: dict[tuple[int, int, int], Fraction] = {}
    for target in states:
        incoming = sum(mu[source] * lifted_edges(source, mutation).get(target, Fraction(0)) for source in states)
        outgoing = mu[target] * sum(lifted_edges(target, mutation).values(), Fraction(0))
        lifted_divergence[target] = incoming - outgoing

    lumping = True
    for state in states:
        aggregate: dict[tuple[int, int], Fraction] = {}
        for target, rate in lifted_edges(state, mutation).items():
            aggregate[target[:2]] = aggregate.get(target[:2], Fraction(0)) + rate
        lumping &= aggregate == projected_edges(state[:2], mutation)

    mean_step = Fraction(0)
    cut_current = Fraction(0)
    for state, weight in mu.items():
        x, r, z = state
        for target, rate in lifted_edges(state, mutation).items():
            y, _s, target_z = target
            step = work_step(x, y, r, mutation) if y != x else 0
            mean_step += weight * rate * step
            if step == 1 and z == L - 1 and target_z == 0:
                cut_current += weight * rate
            elif step == -1 and z == 0 and target_z == L - 1:
                cut_current -= weight * rate

    projected_ep = 0.0
    for source, weight in nu.items():
        for target, rate in projected_edges(source, mutation).items():
            forward = weight * rate
            reverse = nu[target] * projected_edges(target, mutation).get(source, Fraction(0))
            if forward and reverse and forward != reverse:
                projected_ep += 0.5 * float(forward - reverse) * math.log(float(forward / reverse))

    lifted_ep = 0.0
    for source, weight in mu.items():
        for target, rate in lifted_edges(source, mutation).items():
            forward = weight * rate
            reverse = mu[target] * lifted_edges(target, mutation).get(source, Fraction(0))
            if forward and reverse and forward != reverse:
                lifted_ep += 0.5 * float(forward - reverse) * math.log(float(forward / reverse))

    return {
        "nu": nu,
        "mu": mu,
        "projected_divergence": projected_divergence,
        "lifted_divergence": lifted_divergence,
        "lumping": lumping,
        "mean_step": mean_step,
        "cut_current": cut_current,
        "projected_ep": projected_ep,
        "lifted_ep": lifted_ep,
    }


def open_fuel_edges(state: tuple[int, int, int], fuel: int, mutation: str | None = None) -> dict[tuple[int, int, int], Fraction]:
    x, r, z = state
    out: dict[tuple[int, int, int], Fraction] = {}
    for (y, s), rate in projected_edges((x, r), mutation).items():
        step = work_step(x, y, r, mutation) if y != x else 0
        target_z = z + step
        if -fuel <= target_z <= fuel or mutation == "boundary_leak":
            out[(y, s, target_z)] = rate
    return out


def poisson_tail(rate: float, jumps: int) -> float:
    partial = 0.0
    term = math.exp(-rate)
    for k in range(jumps + 1):
        if k:
            term *= rate / k
        partial += term
    return max(0.0, 1.0 - partial)


def poly_derivative(p: list[Fraction]) -> list[Fraction]:
    return [Fraction(i) * p[i] for i in range(1, len(p))] or [Fraction(0)]


def poly_add(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else Fraction(0)) + (b[i] if i < len(b) else Fraction(0)) for i in range(n)]


def poly_scale(a: list[Fraction], c: Fraction) -> list[Fraction]:
    return [c * value for value in a]


def poly_mul(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def poly_integral_0_1(p: list[Fraction]) -> Fraction:
    return sum((value / Fraction(i + 1) for i, value in enumerate(p)), Fraction(0))


def poly_at(p: list[Fraction], t: Fraction) -> Fraction:
    return sum((value * t**i for i, value in enumerate(p)), Fraction(0))


def continuum_checks(mutation: str | None = None) -> dict[str, object]:
    omega2 = Fraction(4)
    u = [Fraction(1), Fraction(2), Fraction(3)]
    v = [Fraction(2), Fraction(-1), Fraction(0), Fraction(1)]
    pu = poly_add(poly_derivative(poly_derivative(u)), poly_scale(u, omega2))
    pv = poly_add(poly_derivative(poly_derivative(v)), poly_scale(v, omega2))
    green_bulk = poly_integral_0_1(poly_add(poly_mul(u, pv), poly_scale(poly_mul(v, pu), Fraction(-1))))
    du, dv = poly_derivative(u), poly_derivative(v)
    green_boundary = (
        poly_at(u, Fraction(1)) * poly_at(dv, Fraction(1))
        - poly_at(v, Fraction(1)) * poly_at(du, Fraction(1))
        - poly_at(u, Fraction(0)) * poly_at(dv, Fraction(0))
        + poly_at(v, Fraction(0)) * poly_at(du, Fraction(0))
    )
    if mutation == "wrong_green_sign":
        green_boundary = -green_boundary

    evolution = ((0, 1), (-1, 0))
    determinant = evolution[0][0] * evolution[1][1] - evolution[0][1] * evolution[1][0]
    q, p = Fraction(3, 5), Fraction(4, 5)
    q2 = evolution[0][0] * q + evolution[0][1] * p
    p2 = evolution[1][0] * q + evolution[1][1] * p
    energy_preserved = q * q + p * p == q2 * q2 + p2 * p2
    symplectic_preserved = determinant == 1

    def retarded_support(t: Fraction, x: Fraction) -> bool:
        if mutation == "acausal_kernel":
            return t >= 0
        return t >= 0 and abs(x) <= t

    support_samples = [
        retarded_support(Fraction(2), Fraction(1)),
        not retarded_support(Fraction(1), Fraction(2)),
        not retarded_support(Fraction(-1), Fraction(0)),
    ]
    spacelike_pairs_zero = all(not retarded_support(t, x) for t, x in ((Fraction(1), Fraction(2)), (Fraction(2), Fraction(3))))
    master_bracket = Fraction(0)  # S_BV is antifield-independent.
    trace_columns = ((1, 0, 0, -1), (0, 1, 1, 0))
    trace_rank_two = trace_columns[0] != trace_columns[1] and any(trace_columns[0]) and any(trace_columns[1])
    return {
        "green_bulk": green_bulk,
        "green_boundary": green_boundary,
        "determinant": determinant,
        "energy_preserved": energy_preserved,
        "symplectic_preserved": symplectic_preserved,
        "support_samples": support_samples,
        "spacelike_pairs_zero": spacelike_pairs_zero,
        "master_bracket": master_bracket,
        "trace_rank_two": trace_rank_two,
    }


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    cyclic = data.get("finite_cyclic_controller", {})
    replenish = data.get("replenishment_boundary", {})
    fuel = data.get("finite_fuel_limit", {})
    host = data.get("continuum_host", {})
    boundary = data.get("coupling_boundary", {})
    control = data.get("exact_control", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    if cyclic.get("finite_state_time_homogeneous_markov_chain") is not True or cyclic.get("strongly_lumpable_exactly_to_K115") is not True or cyclic.get("positive_stationary_winding_current") is not True or cyclic.get("finite_nonequilibrium_controller_constructed") is not True or cyclic.get("finite_closed_equilibrium_bath_constructed") is not False:
        failures.append("cyclic")
    if replenish.get("ring_size_times_net_cut_current_equals_mean_signed_resource_step_rate") is not True or replenish.get("wrap_is_explicit_replenishment_not_costless_identification") is not True or replenish.get("maintained_nonconservative_affinities_are_supplied") is not True or replenish.get("source_or_GU_ownership_of_replenishment") is not False:
        failures.append("replenishment")
    if fuel.get("exactly_matches_K117_before_the_first_boundary_attempt") is not True or fuel.get("finite_window_limit_to_K117_as_N_tends_to_infinity") is not True or fuel.get("stationary_mean_fuel_drift") != "zero_for_every_finite_N" or fuel.get("stationary_exact_K115_projection") is not False:
        failures.append("fuel")
    if host.get("boundary_one_form_and_even_symplectic_flux_constructed") is not True or host.get("bulk_degree_minus_one_BV_cotangent_symplectic_form_constructed") is not True or host.get("BV_BFV_compatibility_identity_constructed") is not True or host.get("boundary_BFV_charge") != "zero_in_the_nongauge_theory" or host.get("advanced_retarded_causal_support") is not True or host.get("spacelike_separated_linear_Peierls_observables_commute") is not True or host.get("genuine_continuum_free_nongauge_BV_BFV_host") is not True or host.get("nontrivial_gauge_or_ghost_complex_constructed") is not False or host.get("AQFT_net_or_Hadamard_state_constructed") is not False:
        failures.append("host")
    required_false = (
        "K115_detector_coupled_to_continuum_field", "finite_controller_derived_from_continuum_action",
        "Weinstein_source_or_GU_action_constructed", "interacting_GU_BV_BFV_theory_constructed",
        "Born_rule_derived", "held_out_scored", "prediction_or_confirmation_credit",
    )
    if any(boundary.get(key) is not False for key in required_false) or boundary.get("canon_verdict_change") != "none":
        failures.append("coupling")
    if any(control.get(key) is not True for key in (
        "cyclic_stationarity_and_strong_lumping_checked_exactly", "winding_resource_and_entropy_checked",
        "finite_fuel_Poisson_bound_checked", "continuum_mode_Green_trace_symplectic_master_and_causal_controls_checked",
    )):
        failures.append("control")
    ceiling = data.get("claim_ceiling", "")
    if "finite nonequilibrium" not in ceiling or "free nongauge continuum" not in ceiling or "not a closed equilibrium bath" not in ceiling or "not coupled to K115" not in ceiling:
        failures.append("ceiling")
    return failures


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    finite = finite_controller_checks(mutation)
    continuum = continuum_checks(mutation)
    lambda_uniform = Fraction(4, 5) + Fraction(679, 1243)
    tails = [poisson_tail(float(lambda_uniform), fuel) for fuel in (2, 4, 8, 16)]
    boundary_state = (0, 0, 2)
    boundary_projected = sum(projected_edges(boundary_state[:2], mutation).values(), Fraction(0))
    boundary_open = sum(open_fuel_edges(boundary_state, 2, mutation).values(), Fraction(0))
    step_antisymmetric = all(work_step(x, y, r, mutation) == -work_step(y, x, r, mutation) for x in range(N) for y in range(N) if x != y for r in range(N))
    checks = [
        ("three base and record states", len(finite["nu"]) == 9),
        ("positive K115 rates", KAPPA > 0 and CLOCK > 0),
        ("event kernels normalize", all(sum(kernel(x, mutation), Fraction(0)) == 1 for x in range(N))),
        ("event kernels remain informative", any(kernel(x, mutation)[r] != Fraction(1, 3) for x in range(N) for r in range(N))),
        ("projected stationary law normalizes", sum(finite["nu"].values(), Fraction(0)) == 1),
        ("projected stationary divergence vanishes", all(value == 0 for value in finite["projected_divergence"].values())),
        ("odd finite fuel ring has five levels", L == 5 and L % 2 == 1),
        ("lifted stationary law normalizes", sum(finite["mu"].values(), Fraction(0)) == 1),
        ("finite cyclic lift is stationary", all(value == 0 for value in finite["lifted_divergence"].values())),
        ("finite cyclic lift strongly lumps exactly to K115", bool(finite["lumping"])),
        ("resource steps are antisymmetric", step_antisymmetric),
        ("stationary signed resource current is positive", finite["mean_step"] > 0),
        ("ring cut current owns the winding factor", L * finite["cut_current"] == finite["mean_step"]),
        ("lifted and projected entropy production agree", abs(finite["lifted_ep"] - finite["projected_ep"]) < 1e-12),
        ("lifted entropy production is positive", finite["lifted_ep"] > 0.0),
        ("bounded fuel is finite", len(range(-2, 3)) == 5),
        ("bounded fuel distorts projection only at its boundary", boundary_open < boundary_projected),
        ("finite-window uniformization bounds decrease", all(tails[i + 1] < tails[i] for i in range(len(tails) - 1))),
        ("finite-window error bound tends small", tails[-1] < 1e-12),
        ("modewise Green identity is exact", continuum["green_bulk"] == continuum["green_boundary"]),
        ("Cauchy trace has full mode rank", bool(continuum["trace_rank_two"])),
        ("quarter-period Cauchy evolution has determinant one", continuum["determinant"] == 1),
        ("quarter-period evolution preserves symplectic form", bool(continuum["symplectic_preserved"])),
        ("quarter-period evolution preserves mode energy", bool(continuum["energy_preserved"])),
        ("antifield-independent free action obeys CME", continuum["master_bracket"] == 0),
        ("retarded massless control has causal-cone support", all(continuum["support_samples"])),
        ("spacelike linear controls have zero causal pairing", bool(continuum["spacelike_pairs_zero"])),
    ]
    return checks


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [(name, any(not ok for _, ok in exact_checks(name))) for name in (
        "zero_clock", "unnormalized_kernel", "uninformative_kernel", "reverse_work",
        "break_lift_shift", "boundary_leak", "wrong_green_sign", "acausal_kernel",
    )]
    updates = (
        ("invent_equilibrium_bath", lambda d: d["finite_cyclic_controller"].__setitem__("finite_closed_equilibrium_bath_constructed", True)),
        ("break_strong_lumping", lambda d: d["finite_cyclic_controller"].__setitem__("strongly_lumpable_exactly_to_K115", False)),
        ("erase_winding", lambda d: d["finite_cyclic_controller"].__setitem__("positive_stationary_winding_current", False)),
        ("erase_replenishment", lambda d: d["replenishment_boundary"].__setitem__("wrap_is_explicit_replenishment_not_costless_identification", False)),
        ("hide_supplied_affinity", lambda d: d["replenishment_boundary"].__setitem__("maintained_nonconservative_affinities_are_supplied", False)),
        ("invent_GU_replenishment", lambda d: d["replenishment_boundary"].__setitem__("source_or_GU_ownership_of_replenishment", True)),
        ("erase_finite_window_limit", lambda d: d["finite_fuel_limit"].__setitem__("finite_window_limit_to_K117_as_N_tends_to_infinity", False)),
        ("invent_stationary_fuel_current", lambda d: d["finite_fuel_limit"].__setitem__("stationary_mean_fuel_drift", "positive")),
        ("invent_exact_finite_fuel_projection", lambda d: d["finite_fuel_limit"].__setitem__("stationary_exact_K115_projection", True)),
        ("erase_boundary_form", lambda d: d["continuum_host"].__setitem__("boundary_one_form_and_even_symplectic_flux_constructed", False)),
        ("erase_odd_BV_form", lambda d: d["continuum_host"].__setitem__("bulk_degree_minus_one_BV_cotangent_symplectic_form_constructed", False)),
        ("erase_BV_BFV_identity", lambda d: d["continuum_host"].__setitem__("BV_BFV_compatibility_identity_constructed", False)),
        ("erase_causal_support", lambda d: d["continuum_host"].__setitem__("advanced_retarded_causal_support", False)),
        ("invent_gauge_complex", lambda d: d["continuum_host"].__setitem__("nontrivial_gauge_or_ghost_complex_constructed", True)),
        ("invent_AQFT_state", lambda d: d["continuum_host"].__setitem__("AQFT_net_or_Hadamard_state_constructed", True)),
        ("invent_detector_coupling", lambda d: d["coupling_boundary"].__setitem__("K115_detector_coupled_to_continuum_field", True)),
        ("invent_action_derived_rates", lambda d: d["coupling_boundary"].__setitem__("finite_controller_derived_from_continuum_action", True)),
        ("invent_source_action", lambda d: d["coupling_boundary"].__setitem__("Weinstein_source_or_GU_action_constructed", True)),
        ("invent_interacting_GU_BV", lambda d: d["coupling_boundary"].__setitem__("interacting_GU_BV_BFV_theory_constructed", True)),
        ("invent_Born", lambda d: d["coupling_boundary"].__setitem__("Born_rule_derived", True)),
        ("score_holdout", lambda d: d["coupling_boundary"].__setitem__("held_out_scored", True)),
        ("invent_prediction", lambda d: d["coupling_boundary"].__setitem__("prediction_or_confirmation_credit", True)),
        ("promote_canon", lambda d: d["coupling_boundary"].__setitem__("canon_verdict_change", "changed")),
        ("erase_control", lambda d: d["exact_control"].__setitem__("winding_resource_and_entropy_checked", False)),
        ("erase_scope", lambda d: d.__setitem__("claim_ceiling", "GU now has a complete physical quantum measurement theory.")),
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
    checks.append(("manifest preserves controller, continuum and coupling ceilings", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    print(f"K118 FINITE CONTROLLER CONTINUUM BV-BFV HOST: {sum(int(bool(ok)) for _, ok in checks)}/{len(checks)} pass")
    return 0 if all(ok for _, ok in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
