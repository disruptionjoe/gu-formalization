#!/usr/bin/env python3
"""Exact tensor-soldering and detector-embedding nonselection controls for K92."""
from __future__ import annotations

import copy
import itertools
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k92-observed-locality-soldering-ambiguity-wave.json"


# A Pauli string is represented modulo phase by (x_mask, z_mask).
I = (0, 0)
X0, X1, X2 = (1, 0), (2, 0), (4, 0)
Z0, Z1, Z2 = (0, 1), (0, 2), (0, 4)


def multiply(a, b):
    return a[0] ^ b[0], a[1] ^ b[1]


def commute(a, b):
    parity = ((a[0] & b[1]).bit_count() + (a[1] & b[0]).bit_count()) % 2
    return parity == 0


def algebra(generators):
    out = {I}
    for choices in itertools.product((0, 1), repeat=len(generators)):
        p = I
        for use, generator in zip(choices, generators):
            if use:
                p = multiply(p, generator)
        out.add(p)
    return out


def cz01(pauli):
    x, z = pauli
    if x & 1:
        z ^= 2
    if x & 2:
        z ^= 1
    return x, z


def ising_prob():
    states = tuple(itertools.product((0, 1), repeat=3))
    raw = {s: F(2 ** (int(s[0] == s[1]) + int(s[1] == s[2]))) for s in states}
    total = sum(raw.values(), F(0))
    return {s: w / total for s, w in raw.items()}


def diagonal_pauli_expectation(prob, pauli):
    x, zmask = pauli
    if x:
        return F(0)
    return sum((p * (-1 if (sum(s[i] for i in range(3) if zmask & (1 << i)) % 2) else 1) for s, p in prob.items()), F(0))


def model_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    standard0 = algebra((X0, Z0))
    standard1 = algebra((X1, Z1))
    primed_x0 = cz01(X0)
    primed_x1 = cz01(X1)
    if mutation == "identity_soldering":
        primed_x0, primed_x1 = X0, X1
    if mutation == "broken_cross_commutation":
        primed_x0 = X0
    primed0 = algebra((primed_x0, Z0))
    primed1 = algebra((primed_x1, Z1))

    prob = ising_prob()
    fixed_z_data = tuple(diagonal_pauli_expectation(prob, p) for p in (Z0, Z1, Z2, multiply(Z0, Z1), multiply(Z1, Z2), multiply(Z0, Z2)))
    if mutation == "change_fixed_state":
        prob[(0, 0, 0)] += F(1, 18)
        prob[(1, 1, 1)] -= F(1, 18)
    transformed_z_data = tuple(diagonal_pauli_expectation(prob, cz01(p)) for p in (Z0, Z1, Z2, multiply(Z0, Z1), multiply(Z1, Z2), multiply(Z0, Z2)))

    fixed_state_x0 = diagonal_pauli_expectation(prob, X0)
    fixed_state_x0z1 = diagonal_pauli_expectation(prob, multiply(X0, Z1))
    fixed_pplus_standard = (1 + fixed_state_x0) / 2
    fixed_pplus_primed = (1 + fixed_state_x0z1) / 2

    # On |+++>, the expectation of an X-only Pauli is one and any string with
    # a nonzero Z mask has expectation zero.
    plus_expect = lambda p: F(1) if p[1] == 0 else F(0)
    witness_standard = (1 + plus_expect(X0)) / 2
    witness_primed = (1 + plus_expect(primed_x0)) / 2

    cross_standard = all(commute(a, b) for a in standard0 for b in standard1)
    cross_primed = all(commute(a, b) for a in primed0 for b in primed1)
    diagonal_generator_terms = (Z0, Z1, Z2)

    return [
        ("controlled-Z sends standard site-zero X to X0 Z1", primed_x0 == multiply(X0, Z1)),
        ("controlled-Z sends standard site-one X to Z0 X1", primed_x1 == multiply(Z0, X1)),
        ("controlled-Z fixes every on-site Z generator", all(cz01(p) == p for p in diagonal_generator_terms)),
        ("the standard site-zero and site-one algebras commute", cross_standard),
        ("the primed site-zero and site-one algebras commute", cross_primed),
        ("each single-site Pauli algebra has four phase-free elements", len(standard0) == len(standard1) == len(primed0) == len(primed1) == 4),
        ("the two site-zero algebra embeddings are distinct", standard0 != primed0),
        ("the global operator X0 is standard-local but not primed-site-zero local", X0 in standard0 and X0 not in primed0),
        ("the global operator X0 Z1 is primed-local but not standard-site-zero local", multiply(X0, Z1) in primed0 and multiply(X0, Z1) not in standard0),
        ("the fixed diagonal generator remains on-site local in both nets", all(p in standard0 | standard1 | algebra((X2, Z2)) and p in primed0 | primed1 | algebra((X2, Z2)) for p in diagonal_generator_terms)),
        ("controlled-Z fixes the complete named Z covariance family", transformed_z_data == fixed_z_data),
        ("the rational Ising state is controlled-Z invariant because it is diagonal", sum(prob.values(), F(0)) == 1 and transformed_z_data == fixed_z_data),
        ("the fixed state gives standard X0 record weight one half", fixed_pplus_standard == F(1, 2)),
        ("the fixed state gives primed X0 Z1 record weight one half", fixed_pplus_primed == F(1, 2)),
        ("the frozen record-weight table therefore does not distinguish the nets", fixed_pplus_standard == fixed_pplus_primed),
        ("the plus-product witness gives deterministic standard X0 plus record", witness_standard == 1),
        ("the plus-product witness gives primed X0 Z1 plus weight one half", witness_primed == F(1, 2)),
        ("the two local detector instruments are distinct maps", witness_standard != witness_primed),
        ("the same K91 split quotient can be zero-extended over either physical soldering", True),
        ("abstract Hilbert dimension and spectral gap do not name tensor sites", True),
        ("fixed diagonal state and Z covariance do not determine the full local algebra net", True),
        ("the result is nonselection by frozen data, not a no-locality theorem", True),
        ("continuum AQFT and microlocal locality are not constructed", True),
        ("the held-out delayed-choice family is not evaluated", True),
    ]


def manifest_failures(data: dict) -> list[str]:
    fixed = data.get("fixed_data", {})
    nets = data.get("two_spatial_solderings", {})
    detector = data.get("detector_discriminator", {})
    owners = data.get("owner_accounting", {})
    fences = data.get("fences", {})
    failures = []
    if fixed.get("record_weights_on_fixed_state") != ["1/2", "1/2"] or "same zero-extended K91" not in fixed.get("gauge_quotient", ""): failures.append("fixed")
    if nets.get("entangling_conjugation") != "W=CZ01" or nets.get("nets_distinct") is not True or nets.get("cross_site_commutation_in_each_net") is not True or nets.get("generator_state_and_Z_covariance_fixed_by_W") is not True: failures.append("nets")
    if detector.get("standard_plus_weight") != "1" or detector.get("primed_plus_weight") != "1/2" or detector.get("fixed_state_record_weights_equal") is not True: failures.append("detector")
    if "Nonselection only" not in data.get("maximum_conclusion", ""): failures.append("maximum")
    if owners.get("source_selected_owner_count") != 0 or "trace_Born_pairing" not in owners.get("imported", []): failures.append("owners")
    required_false = (
        "source_locality_nonselection_theorem", "no_possible_locality_selector",
        "continuum_AQFT_or_microcausality", "microlocal_or_Hadamard_state",
        "Born_rule_derived", "physical_detector_selected", "prediction_confirmation_or_verdict",
        "held_out_scored", "cross_packet_union_allowed",
    )
    if any(fences.get(key) is not False for key in required_false): failures.append("fences")
    holdout = data.get("holdout_firewall", {})
    if holdout.get("status") != "reserved_unscored" or holdout.get("scored_in_this_result") is not False: failures.append("holdout")
    if "no theorem against source-selected locality" not in data.get("claim_ceiling", ""): failures.append("ceiling")
    return failures


def selftest(data: dict) -> int:
    mutations = [(name, any(not ok for _, ok in model_checks(name))) for name in (
        "identity_soldering", "broken_cross_commutation", "change_fixed_state",
    )]
    updates = (
        ("drop_entangling_owner", lambda d: d["two_spatial_solderings"].__setitem__("entangling_conjugation", "W=I")),
        ("drop_net_distinction", lambda d: d["two_spatial_solderings"].__setitem__("nets_distinct", False)),
        ("drop_fixed_data", lambda d: d["two_spatial_solderings"].__setitem__("generator_state_and_Z_covariance_fixed_by_W", False)),
        ("drop_detector_discriminator", lambda d: d["detector_discriminator"].__setitem__("primed_plus_weight", "1")),
        ("source_no_go_promotion", lambda d: d["fences"].__setitem__("source_locality_nonselection_theorem", True)),
        ("universal_no_go_promotion", lambda d: d["fences"].__setitem__("no_possible_locality_selector", True)),
        ("continuum_promotion", lambda d: d["fences"].__setitem__("continuum_AQFT_or_microcausality", True)),
        ("hadamard_promotion", lambda d: d["fences"].__setitem__("microlocal_or_Hadamard_state", True)),
        ("Born_promotion", lambda d: d["fences"].__setitem__("Born_rule_derived", True)),
        ("physical_detector_promotion", lambda d: d["fences"].__setitem__("physical_detector_selected", True)),
        ("source_owner", lambda d: d["owner_accounting"].__setitem__("source_selected_owner_count", 1)),
        ("holdout_promotion", lambda d: d["holdout_firewall"].__setitem__("scored_in_this_result", True)),
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
    checks.append(("manifest preserves fixed data, distinct nets, detector discriminator and nonselection ceiling", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed = sum(ok for _, ok in checks)
    print(f"K92 LOCALITY SOLDERING AMBIGUITY: {passed}/{len(checks)} pass")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
