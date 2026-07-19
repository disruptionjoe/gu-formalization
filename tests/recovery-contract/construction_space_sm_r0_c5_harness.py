#!/usr/bin/env python
"""Reusable construction-space SM R0 harness for C5.

This is P2-SM-R0-HARNESS-C5 from the construction-space exploration map.
It checks candidate quotient/algebra/shadow packets against the frozen SM
Rung 0 sharp list: anomaly cancellation, chirality, three generations,
absolute hypercharge, Higgs, full spectrum, and extra-mode decoupling.

Run: python tests/recovery-contract/construction_space_sm_r0_c5_harness.py
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MAP = ROOT / "lab" / "process" / "construction-space-map.json"
LEDGER = ROOT / "explorations" / "type-ii1-spectral" / "sm-gauge-higgs-finite-control-extraction-ledger-2026-06-24.md"
W222 = ROOT / "explorations" / "W222-falsify-sm-emergence-anomaly-hypercharge-2026-07-14.md"

FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL") + " :: " + name + ((" -- " + detail) if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


def log(message: str = "") -> None:
    print(message, flush=True)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def contains(text: str, needle: str) -> bool:
    return needle.casefold() in text.casefold()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def cell(map_data: dict, cell_id: str) -> dict:
    for entry in map_data["cells"]:
        if entry["id"] == cell_id:
            return entry
    raise AssertionError(f"missing construction-space cell {cell_id}")


SM_ONE_GEN = [
    (+1, 2, 3, F(1, 6)),   # Q_L
    (-1, 1, 3, F(-2, 3)),  # u_c
    (-1, 1, 3, F(1, 3)),   # d_c
    (0, 2, 1, F(-1, 2)),   # L_L
    (0, 1, 1, F(1)),       # e_c
    (0, 1, 1, F(0)),       # nu_c
]


def anomalies(fermions: list[tuple[int, int, int, F]]) -> dict[str, F]:
    u1_cubed = F(0)
    grav = F(0)
    su2 = F(0)
    su3 = F(0)
    for tri, n_weak, n_color, hypercharge in fermions:
        u1_cubed += n_weak * n_color * hypercharge**3
        grav += n_weak * n_color * hypercharge
        if n_weak == 2:
            su2 += n_color * hypercharge
        su3 += n_weak * tri
    return {"U1_cubed": u1_cubed, "grav": grav, "su2": su2, "su3": su3}


def su2_doublet_count(fermions: list[tuple[int, int, int, F]]) -> int:
    return sum(n_color for _tri, n_weak, n_color, _hypercharge in fermions if n_weak == 2)


@dataclass(frozen=True)
class SmR0Candidate:
    candidate_id: str
    fermions: list[tuple[int, int, int, F]]
    source_owned_selector: bool
    target_free: bool
    chirality_produced: bool
    generation_count: int
    generation_source: str
    per_generation_adjustable: bool
    absolute_hypercharge_selected: bool
    physical_higgs_sector: bool
    complete_surviving_spectrum: bool
    extra_mode_decoupling: bool


def sm_r0_failures(candidate: SmR0Candidate) -> list[str]:
    failures: list[str] = []
    anomaly_values = anomalies(candidate.fermions)
    if any(value != 0 for value in anomaly_values.values()) or su2_doublet_count(candidate.fermions) % 2 != 0:
        failures.append("gauge anomaly cancellation")
    if not candidate.chirality_produced:
        failures.append("chirality production")
    if candidate.generation_count != 3 or candidate.generation_source not in {"native", "forced"}:
        failures.append("three native generations")
    if candidate.per_generation_adjustable:
        failures.append("per-generation adjustable structure")
    if not candidate.absolute_hypercharge_selected:
        failures.append("absolute hypercharge normalization")
    if not candidate.physical_higgs_sector:
        failures.append("physical Higgs sector")
    if not candidate.complete_surviving_spectrum:
        failures.append("complete surviving spectrum")
    if not candidate.extra_mode_decoupling:
        failures.append("extra/mirror mode decoupling")
    if not candidate.source_owned_selector or not candidate.target_free:
        failures.append("source-owned target-free selector")
    return failures


def passes_sm_r0(candidate: SmR0Candidate) -> bool:
    return sm_r0_failures(candidate) == []


def main() -> None:
    map_data = load_json(MAP)
    c5 = cell(map_data, "C5-NATIVE-QUOTIENT-SELECTOR")
    ledger = read_text(LEDGER)
    w222 = read_text(W222)

    log("=" * 82)
    log("PC controls - reusable harness accepts and rejects the right shapes")
    log("=" * 82)
    complete_native = SmR0Candidate(
        candidate_id="PC_COMPLETE_NATIVE_THREE_GEN",
        fermions=SM_ONE_GEN * 3,
        source_owned_selector=True,
        target_free=True,
        chirality_produced=True,
        generation_count=3,
        generation_source="native",
        per_generation_adjustable=False,
        absolute_hypercharge_selected=True,
        physical_higgs_sector=True,
        complete_surviving_spectrum=True,
        extra_mode_decoupling=True,
    )
    check("PC1  a complete source-owned three-generation SM packet passes R0", passes_sm_r0(complete_native))

    wrong_hypercharge = SmR0Candidate(
        candidate_id="PC_WRONG_HYPERCHARGE",
        fermions=[(+1, 2, 3, F(1))] + SM_ONE_GEN[1:],
        source_owned_selector=True,
        target_free=True,
        chirality_produced=True,
        generation_count=3,
        generation_source="native",
        per_generation_adjustable=False,
        absolute_hypercharge_selected=False,
        physical_higgs_sector=True,
        complete_surviving_spectrum=True,
        extra_mode_decoupling=True,
    )
    check("PC2  wrong hypercharge/anomalous packet fails R0", not passes_sm_r0(wrong_hypercharge), ", ".join(sm_r0_failures(wrong_hypercharge)))

    vectorlike_host = SmR0Candidate(
        candidate_id="PC_VECTORLIKE_HOST_ONLY",
        fermions=SM_ONE_GEN + [(-tri, nw, nc, -hypercharge) for tri, nw, nc, hypercharge in SM_ONE_GEN],
        source_owned_selector=True,
        target_free=True,
        chirality_produced=False,
        generation_count=1,
        generation_source="imported",
        per_generation_adjustable=True,
        absolute_hypercharge_selected=True,
        physical_higgs_sector=False,
        complete_surviving_spectrum=False,
        extra_mode_decoupling=False,
    )
    check("PC3  anomaly-free vectorlike host still fails the SM R0 list", not passes_sm_r0(vectorlike_host), ", ".join(sm_r0_failures(vectorlike_host)))

    log("")
    log("=" * 82)
    log("C1 - C5 source records")
    log("=" * 82)
    check(
        "C1a  map records the completed P2 C5 SM disposition",
        c5["tracks"]["SM"]["grade"] == "R0_FAIL"
        and c5["tracks"]["SM"]["verification_needed"] is False
        and "construction-space-sm-r0-harness-c5-2026-07-19.md" in c5["tracks"]["SM"]["evidence"]
        and "construction_space_sm_r0_c5_harness.py" in c5["tracks"]["SM"]["evidence"],
    )
    check("C1b  finite algebra selector is absent in the extraction ledger", "No current selector computes this algebra" in ledger)
    check("C1c  SM gauge quotient selector is the first target-level failure", "SM gauge quotient `SU(3) x SU(2) x U(1) / Z_6` | fail" in ledger)
    check("C1d  W222 supplies real relative arithmetic only after granting the chiral shadow", contains(w222, "hypercharges MATCH the SM exactly") and contains(w222, "CONDITIONAL on the 4D shadow"))

    log("")
    log("=" * 82)
    log("C2 - current C5 seed candidate")
    log("=" * 82)
    current_c5_seed = SmR0Candidate(
        candidate_id="C5_CURRENT_PATI_SALAM_HOST_SEED",
        fermions=SM_ONE_GEN,
        source_owned_selector=False,
        target_free=False,
        chirality_produced=False,
        generation_count=1,
        generation_source="relative_branch",
        per_generation_adjustable=False,
        absolute_hypercharge_selected=False,
        physical_higgs_sector=False,
        complete_surviving_spectrum=False,
        extra_mode_decoupling=False,
    )
    current_failures = sm_r0_failures(current_c5_seed)
    current_anomalies = anomalies(current_c5_seed.fermions)
    check("C2a  current C5 seed has ordinary one-generation anomaly cancellation", all(value == 0 for value in current_anomalies.values()) and su2_doublet_count(current_c5_seed.fermions) % 2 == 0)
    check("C2b  current C5 seed fails native three-generation selection", "three native generations" in current_failures)
    check("C2c  current C5 seed fails source-owned target-free selection", "source-owned target-free selector" in current_failures)
    check("C2d  current C5 seed fails Higgs, spectrum, and decoupling constraints", {"physical Higgs sector", "complete surviving spectrum", "extra/mirror mode decoupling"}.issubset(set(current_failures)))
    check("C2e  current C5 seed does not pass SM R0", not passes_sm_r0(current_c5_seed), ", ".join(current_failures))

    log("")
    log("=" * 82)
    log("VERDICT")
    log("=" * 82)
    if not FAIL:
        log("Operational result: P2 harness complete.")
        log("The reusable SM R0 checker accepts a complete source-owned three-generation")
        log("packet and rejects wrong-hypercharge or vectorlike host-only controls. The")
        log("current C5 Pati-Salam/Spin(10) host seed has real relative anomaly and")
        log("hypercharge arithmetic, but fails R0 because it has no source-owned target-free")
        log("selector, no native three-generation mechanism, no physical Higgs sector, no")
        log("complete spectrum theorem, and no extra-mode decoupling.")

    if FAIL:
        log(f"\nRESULT: {len(FAIL)} FAILED")
        for name in FAIL:
            log("  FAIL: " + name)
        raise SystemExit(1)
    log("\nRESULT: ALL PASS")


if __name__ == "__main__":
    main()
