#!/usr/bin/env python3
"""Regression probe for the remaining B3 primary-source disposition wave."""

from __future__ import annotations

import copy
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LEDGER = ROOT / "lab/process/conditional-physics-ledger-v0.263.json"
SOURCE_REGISTER = ROOT / "lab/process/fc-admission-wave-and-first-b3-register.json"
PACKETS = {
    "CC": (
        ROOT / "lab/process/b3-cc-observation-scope-disposition.json",
        ROOT / "explorations/conditional-build/b3-cc-observation-scope-disposition-2026-08-23.md",
    ),
    "CP": (
        ROOT / "lab/process/b3-cp-observable-scope-disposition.json",
        ROOT / "explorations/conditional-build/b3-cp-observable-scope-disposition-2026-08-23.md",
    ),
    "NU": (
        ROOT / "lab/process/b3-nu-carrier-scope-disposition.json",
        ROOT / "explorations/conditional-build/b3-nu-carrier-scope-disposition-2026-08-23.md",
    ),
}


def load_inputs() -> dict[str, object]:
    ledger = json.loads(LEDGER.read_text())
    rows = {row["id"]: row for row in ledger["rows"]}
    return {
        "rows": rows,
        "source_register": json.loads(SOURCE_REGISTER.read_text()),
        "packets": {
            key: {"registry": json.loads(reg.read_text()), "result": doc.read_text()}
            for key, (reg, doc) in PACKETS.items()
        },
    }


def collect_failures(inputs: dict[str, object]) -> tuple[int, list[str]]:
    failures: list[str] = []
    checks = 0

    def check(condition: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            failures.append(label)

    rows = inputs["rows"]
    source_register = inputs["source_register"]
    packets = inputs["packets"]
    assert isinstance(rows, dict) and isinstance(source_register, dict)
    assert isinstance(packets, dict)

    cc = packets["CC"]["registry"]
    cp = packets["CP"]["registry"]
    nu = packets["NU"]["registry"]
    assert isinstance(cc, dict) and isinstance(cp, dict) and isinstance(nu, dict)

    check(cc["b3_id"] == "B3-CC-02", "CC id pinned")
    check(cc["ledger_row"] == "LT-GR2d", "CC parent pinned")
    check(cc["status"] == "DISPOSED_NO_LEDGER_MOVEMENT__OBSERVATION_VS_VACUUM_SCOPE",
          "CC disposition pinned")
    cc_sources = {source["id"]: source for source in cc["primary_sources"]}
    for source_id in (
        "RIESS-HIGH-Z-SN-1998",
        "PERLMUTTER-HIGH-Z-SN-1999",
        "PLANCK-COSMO-PARAMETERS-2018",
        "DESI-DR2-II-2025",
    ):
        check(source_id in cc_sources, f"CC source present: {source_id}")
    check("do not measure a microscopic decomposition" in
          cc_sources["RIESS-HIGH-Z-SN-1998"]["ceiling"],
          "CC observed-versus-microscopic ceiling")
    check("vacuum-shift response" in cc["precise_relocation"],
          "CC radiative burden retained")

    check(cp["b3_id"] == "B3-CP-04", "CP id pinned")
    check(cp["ledger_row"] == "LT-SM7", "CP parent pinned")
    check(cp["status"] == "DISPOSED_NO_LEDGER_MOVEMENT__OBSERVABLE_TO_THETA_SCOPE",
          "CP disposition pinned")
    cp_sources = {source["id"]: source for source in cp["primary_sources"]}
    check("PSI-NEUTRON-EDM-2020" in cp_sources, "neutron EDM source present")
    check("LATTICE-QCD-THETA-NEDM-2021" in cp_sources,
          "theta-to-EDM source present")
    check("does not directly measure the QCD theta angle" in
          cp_sources["PSI-NEUTRON-EDM-2020"]["ceiling"],
          "EDM-versus-theta ceiling")
    check("do not claim a reliable precision conversion" in
          cp_sources["LATTICE-QCD-THETA-NEDM-2021"]["ceiling"],
          "hadronic-map uncertainty retained")
    check("physical angle combination" in cp["precise_relocation"],
          "physical CP angle burden retained")

    check(nu["b3_id"] == "B3-NU-05", "NU id pinned")
    check(nu["ledger_row"] == "RA-B6" and nu["linked_row"] == "RA-G3",
          "NU parent and linked row pinned")
    check(nu["status"] == "DISPOSED_NO_LEDGER_MOVEMENT__MULTI_CARRIER_SCOPE",
          "NU disposition pinned")
    nu_sources = {source["id"]: source for source in nu["primary_sources"]}
    for source_id in (
        "T2K-NOVA-JOINT-2025",
        "KATRIN-259-DAY-2024",
        "KAMLAND-ZEN-COMPLETE-2024",
        "DESI-DR2-II-2025",
    ):
        check(source_id in nu_sources, f"NU source present: {source_id}")
    check("do not determine the absolute mass scale" in
          nu_sources["T2K-NOVA-JOINT-2025"]["ceiling"],
          "oscillation ceiling retained")
    check("does not establish Dirac neutrinos" in
          nu_sources["KAMLAND-ZEN-COMPLETE-2024"]["ceiling"],
          "double-beta ceiling retained")
    check("not a model-independent laboratory measurement" in
          nu_sources["DESI-DR2-II-2025"]["ceiling"],
          "cosmological model ceiling retained")
    check("one common operator, reality/charge map" in nu["joint_evaluation_constraint"],
          "joint neutral-sector constraint retained")

    check(rows["LT-GR2d"]["verdict"] == "NEEDS" and
          rows["LT-GR2d"]["reason_kind"] == "MISSING_CONSTRUCTION",
          "LT-GR2d status preserved")
    check("radiative response" in rows["LT-GR2d"]["distance"],
          "LT-GR2d radiative distance preserved")
    check(rows["LT-SM7"]["verdict"] == "NEEDS" and
          rows["LT-SM7"]["reason_kind"] == "REAL_PARAMETER",
          "LT-SM7 status preserved")
    check("r-torus" in rows["LT-SM7"]["distance"], "LT-SM7 angle torus preserved")
    check(rows["RA-B6"]["verdict"] == "DIFFERS" and
          "mass spectrum and mixing map" in rows["RA-B6"]["revival_trigger"],
          "RA-B6 neutrino burden preserved")
    check(rows["RA-G3"]["verdict"] == "NEEDS" and
          "stationary odd-form VEV" in rows["RA-G3"]["revival_trigger"],
          "RA-G3 Majorana-channel burden preserved")

    b3 = source_register["b3_register"]
    dispositions = b3["dispositions"]
    check(set(dispositions) == set(b3["ids"]), "all filed B3 entries disposed")
    check(b3["remaining_entries"] == 0, "no B3 entries pending")
    for packet in (cc, cp, nu):
        entry = dispositions[packet["b3_id"]]
        check(entry["status"] == packet["status"],
              f"source register status matches: {packet['b3_id']}")
    check(source_register["ledger_verdict_change"] == "none",
          "source register ledger ceiling preserved")

    for key, packet in packets.items():
        result = packet["result"]
        assert isinstance(result, str)
        flat = re.sub(r"\s+", " ", result)
        check("GU-COMPARATOR-ROUTING — scope before inference." in flat,
              f"routing notice in {key}")
        check("Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in flat,
              f"routing classification in {key}")
        check("```gu-typed-objects" in flat, f"typed-object block in {key}")
        check("No laundering" in flat, f"claim ceiling in {key}")
        check(packet["registry"]["target_claim"] == "NONE-NOT-A-KILL",
              f"not-a-kill typing in {key}")
        check(packet["registry"]["ledger_verdict_change"] == "none",
              f"no ledger movement in {key}")
    return checks, failures


def main() -> int:
    checks, failures = collect_failures(load_inputs())
    for label in failures:
        print(f"[FAIL] {label}")
    if failures:
        return 1
    print(f"PASS {checks}/{checks}")
    return 0


def selftest() -> int:
    baseline = load_inputs()
    checks, failures = collect_failures(baseline)
    if failures:
        for label in failures:
            print(f"[FAIL] baseline: {label}")
        return 1
    print(f"BASELINE PASS {checks}/{checks}")

    mutations: list[tuple[str, str, dict[str, object]]] = []

    changed = copy.deepcopy(baseline)
    changed["packets"]["CC"]["registry"]["primary_sources"] = \
        changed["packets"]["CC"]["registry"]["primary_sources"][:3]
    mutations.append(("cc-desi-dropped", "CC source present: DESI-DR2-II-2025", changed))

    changed = copy.deepcopy(baseline)
    changed["packets"]["CP"]["registry"]["primary_sources"][0]["ceiling"] = \
        "The experiment directly measures theta."
    mutations.append(("cp-carrier-collapsed", "EDM-versus-theta ceiling", changed))

    changed = copy.deepcopy(baseline)
    changed["packets"]["NU"]["registry"]["primary_sources"][2]["ceiling"] = \
        "The null establishes Dirac neutrinos."
    mutations.append(("nu-reality-overclaim", "double-beta ceiling retained", changed))

    changed = copy.deepcopy(baseline)
    changed["rows"]["LT-SM7"]["verdict"] = "SAME"
    mutations.append(("cp-ledger-laundered", "LT-SM7 status preserved", changed))

    changed = copy.deepcopy(baseline)
    changed["source_register"]["b3_register"]["remaining_entries"] = 1
    mutations.append(("pending-count-stale", "no B3 entries pending", changed))

    changed = copy.deepcopy(baseline)
    changed["packets"]["NU"]["result"] = changed["packets"]["NU"]["result"].replace(
        "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`", "Classification: `SOURCE_NATIVE_ROUTE`", 1)
    mutations.append(("nu-routing-retyped", "routing classification in NU", changed))

    changed = copy.deepcopy(baseline)
    changed["packets"]["CC"]["result"] = changed["packets"]["CC"]["result"].replace(
        "```gu-typed-objects", "```objects", 1)
    mutations.append(("cc-typed-block-dropped", "typed-object block in CC", changed))

    changed = copy.deepcopy(baseline)
    changed["packets"]["NU"]["registry"]["joint_evaluation_constraint"] = \
        "The two rows can be credited separately."
    mutations.append(("nu-joint-constraint-dropped",
                      "joint neutral-sector constraint retained", changed))

    ok = True
    for name, expected, mutated in mutations:
        _, caught = collect_failures(mutated)
        if expected not in caught:
            print(f"[FAIL] mutation {name}: expected {expected!r}, got {caught!r}")
            ok = False
        else:
            print(f"MUTATION CAUGHT {name}: [FAIL] {expected}")
    print("FAILURE-PATH SELFTEST: " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else main())
