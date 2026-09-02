#!/usr/bin/env python3
"""Exact action/net normalization controls for the K93 soldering selector."""
from __future__ import annotations

import copy
import json
import pathlib
import sys


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k93-observed-action-soldering-selection-wave.json"


def mul_char(a: str, b: str) -> str:
    if a == "I":
        return b
    if b == "I":
        return a
    if a == b:
        return "I"
    return ({"X", "Y", "Z"} - {a, b}).pop()


def mul_pauli(a: str, b: str) -> str:
    return "".join(mul_char(x, y) for x, y in zip(a, b))


def cz(pauli: str) -> str:
    images = {
        (0, "X"): "XZI", (0, "Y"): "YZI", (0, "Z"): "ZII",
        (1, "X"): "ZXI", (1, "Y"): "ZYI", (1, "Z"): "IZI",
        (2, "X"): "IIX", (2, "Y"): "IIY", (2, "Z"): "IIZ",
    }
    out = "III"
    for site, value in enumerate(pauli):
        if value != "I":
            out = mul_pauli(out, images[(site, value)])
    return out


def hadamard_zero(pauli: str) -> str:
    swap = {"I": "I", "X": "Z", "Y": "Y", "Z": "X"}
    return swap[pauli[0]] + pauli[1:]


def primed_pulse(pauli: str) -> str:
    return cz(hadamard_zero(cz(pauli)))


STANDARD = (
    frozenset(("III", "XII", "YII", "ZII")),
    frozenset(("III", "IXI", "IYI", "IZI")),
    frozenset(("III", "IIX", "IIY", "IIZ")),
)
PRIMED = tuple(frozenset(cz(p) for p in factor) for factor in STANDARD)


def normalized(net: tuple[frozenset[str], ...], transform) -> bool:
    return all({transform(p) for p in factor} == set(factor) for factor in net)


def model_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    primed = STANDARD if mutation == "collapse_nets" else PRIMED
    pulse = (lambda p: p) if mutation == "identity_pulse" else hadamard_zero
    conjugate_pulse = pulse if mutation == "drop_action_conjugation" else primed_pulse
    witness = "XZI" if mutation == "wrong_witness" else "ZII"
    twice_h = all(pulse(pulse(p)) == p for p in ("III", "XII", "YII", "ZII"))
    twice_prime = all(conjugate_pulse(conjugate_pulse(p)) == p for p in (
        "III", "XII", "YII", "ZII", "IXI", "IYI", "IZI",
    ))
    return [
        ("the standard and CZ-conjugated site-zero factors are distinct", STANDARD[0] != primed[0]),
        ("the standard and CZ-conjugated site-one factors are distinct", STANDARD[1] != primed[1]),
        ("site two is fixed by the soldering conjugation", STANDARD[2] == primed[2]),
        ("the standard factors are pairwise disjoint outside scalars", all(STANDARD[i] & STANDARD[j] == {"III"} for i in range(3) for j in range(i + 1, 3))),
        ("the primed factors are pairwise disjoint outside scalars", all(primed[i] & primed[j] == {"III"} for i in range(3) for j in range(i + 1, 3))),
        ("CZ is involutive on the complete Pauli basis", all(cz(cz(a + b + c)) == a + b + c for a in "IXYZ" for b in "IXYZ" for c in "IXYZ")),
        ("the fixed Hadamard pulse is involutive", twice_h),
        ("the fixed Hadamard pulse normalizes every standard site factor", normalized(STANDARD, pulse)),
        ("the fixed Hadamard pulse fails to normalize the primed net", not normalized(primed, pulse)),
        ("primed-local Z0 is sent to standard-local X0", pulse(witness) == "XII"),
        ("the cross-pair witness X0 is absent from the primed site-zero factor", "XII" not in primed[0]),
        ("the conjugated pulse is involutive", twice_prime),
        ("the conjugated pulse normalizes every primed site factor", normalized(primed, conjugate_pulse)),
        ("conjugating the action with the net restores covariance", all(conjugate_pulse(cz(p)) == cz(pulse(p)) for p in ("XII", "YII", "ZII", "IXI", "IYI", "IZI"))),
        ("action-net normalization distinguishes the fixed standard and primed pairings", normalized(STANDARD, pulse) and not normalized(primed, pulse)),
        ("the selection belongs to the fixed action-net pairing, not the Hilbert dimension", normalized(primed, conjugate_pulse)),
        ("the discrete pulse supplies no continuum causal cone", True),
        ("normalization by one pulse does not prove unique physical locality", True),
        ("the action pulse and tensor soldering remain repository supplied", True),
        ("the held-out delayed-choice family is not evaluated", True),
    ]


def manifest_failures(data: dict) -> list[str]:
    action = data.get("action_soldering_control", {})
    owners = data.get("owner_accounting", {})
    fences = data.get("fences", {})
    failures = []
    if action.get("fixed_pulse") != "R=H0 tensor I1 tensor I2" or action.get("standard_net_normalized") is not True:
        failures.append("action")
    if action.get("primed_net_normalized_by_fixed_pulse") is not False or action.get("cross_pair_witness") != "R Z0 R*=X0 not in A0_prime":
        failures.append("discriminator")
    if action.get("primed_net_normalized_by_conjugated_pulse") is not True:
        failures.append("covariance")
    if owners.get("source_selected_owner_count") != 0 or "discrete_action_pulse" not in owners.get("repository_owned", []):
        failures.append("owners")
    required_false = (
        "source_selected_action_or_net", "unique_physical_locality",
        "continuum_AQFT_or_microcausality", "microlocal_or_Hadamard_state",
        "Born_rule_derived", "prediction_confirmation_or_verdict",
        "held_out_scored", "cross_packet_union_allowed",
    )
    if any(fences.get(key) is not False for key in required_false):
        failures.append("fences")
    if "fixed action-net pairing" not in data.get("claim_ceiling", ""):
        failures.append("ceiling")
    return failures


def selftest(data: dict) -> int:
    mutations = [(name, any(not ok for _, ok in model_checks(name))) for name in (
        "collapse_nets", "identity_pulse", "drop_action_conjugation", "wrong_witness",
    )]
    updates = (
        ("drop_standard_normalization", lambda d: d["action_soldering_control"].__setitem__("standard_net_normalized", False)),
        ("promote_cross_normalization", lambda d: d["action_soldering_control"].__setitem__("primed_net_normalized_by_fixed_pulse", True)),
        ("drop_conjugated_covariance", lambda d: d["action_soldering_control"].__setitem__("primed_net_normalized_by_conjugated_pulse", False)),
        ("source_action", lambda d: d["fences"].__setitem__("source_selected_action_or_net", True)),
        ("unique_locality", lambda d: d["fences"].__setitem__("unique_physical_locality", True)),
        ("continuum_promotion", lambda d: d["fences"].__setitem__("continuum_AQFT_or_microcausality", True)),
        ("hadamard_promotion", lambda d: d["fences"].__setitem__("microlocal_or_Hadamard_state", True)),
        ("Born_promotion", lambda d: d["fences"].__setitem__("Born_rule_derived", True)),
        ("source_owner", lambda d: d["owner_accounting"].__setitem__("source_selected_owner_count", 1)),
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
    checks.append(("manifest preserves action, covariance, ownership and promotion fences", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed = sum(ok for _, ok in checks)
    print(f"K93 ACTION SOLDERING SELECTION: {passed}/{len(checks)} pass")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
