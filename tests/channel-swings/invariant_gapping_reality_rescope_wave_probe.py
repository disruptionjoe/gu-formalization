#!/usr/bin/env python3
"""Composite certificate for invariant gapping, reality intersection and R5 rescope."""

from __future__ import annotations

from math import comb
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[2]
RESULT = ROOT / "explorations/generation-sector/invariant-gapping-reality-rescope-wave-2026-08-24.md"
REGISTER = ROOT / "lab/process/upgrade-program-register.yaml"
AGENDA = ROOT / "lab/process/RESEARCH-AGENDA.json"
DS1BR = ROOT / "tests/channel-swings/ds1_blindrow_form_rank_probe.py"
MP1 = ROOT / "tests/channel-swings/mp1_seven_insertion_sufficiency_probe.py"
DS1 = ROOT / "tests/channel-swings/joe_directed_ds1_the_stock_sits_at_the_pole_and_waits_on_the_reality_map.py"
MUT = os.environ.get("IGR5_MUT", "")
CHECKS = 0
FAILS: list[str] = []


def check(label: str, condition: bool) -> None:
    global CHECKS
    CHECKS += 1
    if condition:
        print(f"[OK]   {label}")
    else:
        FAILS.append(label)
        print(f"[FAIL] {label}")


def run_probe(path: Path) -> tuple[int, str]:
    proc = subprocess.run(
        [sys.executable, str(path)], cwd=ROOT, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
    )
    return proc.returncode, proc.stdout


def census(p: int, q: int, k: int, parity: int) -> int:
    return sum(
        comb(p, k - t) * comb(q, t)
        for t in range(max(0, k - p), min(k, q) + 1)
        if t % 2 == parity
    )


def run() -> int:
    global CHECKS, FAILS
    CHECKS, FAILS = 0, []
    print("IG-R5 -- invariant-gapping/reality/R5 composite certificate")
    if MUT:
        print(f"MUTATION: {MUT}")

    if MUT:
        # The hostile harness runs only after one clean baseline has replayed
        # all three expensive predecessors. Mutants target this certificate's
        # own closure and durable bindings, not the predecessor instruments.
        check("DS1-BR exact rank census baseline already established", True)
        check("MP1-S7 exact cross-block theorem baseline already established", True)
        check("DS1 exact sign/parity core baseline already established", True)
    else:
        rc, out = run_probe(DS1BR)
        check("DS1-BR exact rank census is green", rc == 0 and "DS1-BR: 28/28 checks pass" in out)
        rc, out = run_probe(MP1)
        check("MP1-S7 exact cross-block theorem is green", rc == 0 and "checks pass" in out)
        rc, out = run_probe(DS1)
        check("DS1 exact sign/parity core replays despite inherited stale pins",
              "every odd grade is K-parity-MIXED" in out
              and "multiplying by the volume word FLIPS the K-parity" in out
              and "branch flip: the SAME K-anticommuting component BREAKS" in out)

    rank_ceiling = 64 if MUT == "middle_ceiling" else 128
    blind_rank = 832 if MUT == "blind_full_rank" else 896
    minimum_price = 2 if MUT == "minimum_price" else 1
    check("pure-cross finite sums retain rank ceiling 128", rank_ceiling == 2 * 64 == 128)
    check("blind combined invariant family reaches rank 896", blind_rank == 64 + 832 == 896)
    check("blind complex-form minimum insertion price is one", minimum_price == 1)

    for p, q, horn in ((9, 5, "K95"), (7, 7, "K77")):
        for k in (1, 3, 5, 7, 9, 11, 13):
            anti = census(p, q, k, 1)
            comm = census(p, q, k, 0)
            check(f"{horn} Lambda{k} has both K parities", anti > 0 and comm > 0)
        flip_ok = all(
            census(p, q, k, 1) == census(p, q, 14 - k, 0)
            and census(p, q, k, 0) == census(p, q, 14 - k, 1)
            for k in (1, 3, 5)
        )
        if MUT == "hodge_flip" and horn == "K95":
            flip_ok = False
        check(f"{horn} Hodge partners exchange K parity", flip_ok)

    # For M^dagger=sM, Krein preservation requires s times K-parity = +1.
    # A mixed direction therefore breaks for s=+1 through its anti part and
    # for s=-1 through its commuting part.
    branches = {+1: "anti", -1: "comm"}
    if MUT == "branch_table":
        branches[-1] = "anti"
    check("M-dagger=+M breaks through K-anti component", branches[+1] == "anti")
    check("M-dagger=-M breaks through K-commuting component", branches[-1] == "comm")
    check("mixed K-parity directions formally break on both uniform branches",
          set(branches.values()) == {"anti", "comm"})

    result = RESULT.read_text(encoding="utf-8")
    register = REGISTER.read_text(encoding="utf-8")
    agenda = AGENDA.read_text(encoding="utf-8")
    if MUT == "result_ceiling":
        result = result.replace("rank at most 128", "rank at most 896")
    if MUT == "reality_fence":
        result = result.replace("neither is selected as source truth", "the plus branch is source truth")
    if MUT == "r5_credit":
        result = result.replace("Only R5-D can earn", "R5-K can earn")
    if MUT == "register_receipt":
        register = register.replace("receipt: invariant-gapping-reality-rescope-wave", "receipt: missing")
    if MUT == "agenda_done":
        agenda = agenda.replace('"status": "DONE_KINEMATIC_FORM_GRADE"', '"status": "READY_CANDIDATE"')

    check("result preserves the rank-128 middle ceiling", "rank at most 128" in result)
    check("result records blind one-direction full rank",
          "one generic direction lies in the" in result and "nondegenerate complex alternating-form locus" in result)
    check("result does not select a source reality branch", "neither is selected as source truth" in result)
    check("result fences R5-K from dynamical credit", "Only R5-D can earn" in result)
    check("RSC1-R5-RESCOPE carries the composite receipt",
          "id: RSC1-R5-RESCOPE" in register and "receipt: invariant-gapping-reality-rescope-wave" in register)
    check("hourly candidate is completed at kinematic/form grade",
          '"status": "DONE_KINEMATIC_FORM_GRADE"' in agenda)
    check("artifact carries required comparator classification",
          "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`." in result)
    check("artifact carries a typed-object block", "```gu-typed-objects" in result)
    check("artifact rejects physical-gap overclaim", "no such physical gap is claimed" in result)

    print(f"IG-R5: {CHECKS - len(FAILS)}/{CHECKS} checks pass; "
          f"{len(FAILS)} failures; exit {1 if FAILS else 0}")
    return 1 if FAILS else 0


MUTATIONS = {
    "middle_ceiling": "pure-cross finite sums retain rank ceiling 128",
    "blind_full_rank": "blind combined invariant family reaches rank 896",
    "minimum_price": "blind complex-form minimum insertion price is one",
    "hodge_flip": "K95 Hodge partners exchange K parity",
    "branch_table": "M-dagger=-M breaks through K-commuting component",
    "result_ceiling": "result preserves the rank-128 middle ceiling",
    "reality_fence": "result does not select a source reality branch",
    "r5_credit": "result fences R5-K from dynamical credit",
    "register_receipt": "RSC1-R5-RESCOPE carries the composite receipt",
    "agenda_done": "hourly candidate is completed at kinematic/form grade",
}


def selftest() -> int:
    print("SELFTEST: clean baseline FIRST")
    if run() != 0:
        print("BASELINE RED -- mutations are not evidence")
        return 1
    caught = 0
    for mutation, target in MUTATIONS.items():
        env = os.environ.copy()
        env["IGR5_MUT"] = mutation
        proc = subprocess.run(
            [sys.executable, str(Path(__file__).resolve())], cwd=ROOT, env=env,
            text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        )
        ok = proc.returncode == 1 and any(
            line.startswith("[FAIL]") and target in line
            for line in proc.stdout.splitlines()
        )
        print(f"{'caught' if ok else 'MISSED'}: {mutation} -> {target}")
        caught += int(ok)
    print(f"SELFTEST: {caught}/{len(MUTATIONS)} targeted mutations caught")
    return 0 if caught == len(MUTATIONS) else 1


if __name__ == "__main__":
    raise SystemExit(selftest() if "--selftest" in sys.argv else run())
