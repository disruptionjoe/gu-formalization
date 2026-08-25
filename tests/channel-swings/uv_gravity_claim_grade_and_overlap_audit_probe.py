#!/usr/bin/env python3
"""Regression gate for the 2026-08-23 UV-gravity candidate hardening result."""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load_bundle() -> dict[str, object]:
    return {
        "registry": json.loads((ROOT / "lab/process/uv-gravity-claim-grade-and-overlap-audit.json").read_text()),
        "paper": (ROOT / "papers/candidates/uv-structure-fourth-order-gravity/uv-structure-fourth-order-gravity-2026-07-11.md").read_text(),
        "staging": (ROOT / "papers/candidates/uv-structure-fourth-order-gravity/STAGING-NOTES.md").read_text(),
        "inventory": (ROOT / "lab/process/paper-hardening-inventory.md").read_text(),
        "agenda": json.loads((ROOT / "lab/process/RESEARCH-AGENDA.json").read_text()),
        "current": (ROOT / "CURRENT-STATE.yaml").read_text(),
        "status": (ROOT / "RESEARCH-STATUS.md").read_text(),
        "next_steps": (ROOT / "NEXT-STEPS.md").read_text(),
    }


def paper_agenda_item(agenda: dict[str, object]) -> dict[str, object]:
    matches = [
        item for item in agenda["work_items"]
        if item["id"] == "PAPER-UV-GRAVITY"
    ]
    require(len(matches) == 1, "agenda must contain exactly one UV-gravity paper row")
    return matches[0]


def validate(bundle: dict[str, object]) -> None:
    registry = bundle["registry"]
    agenda = bundle["agenda"]
    assert isinstance(registry, dict) and isinstance(agenda, dict)

    require(registry["disposition"] == "FAILED_HARDENING_GATE", "wrong disposition")
    require(registry["portfolio_state"] == "PARKED_REQUIRES_RECONSTRUCTION", "wrong portfolio state")
    require(len(registry["claims"]) == 5, "claim matrix must contain five load-bearing claims")
    require({row["id"] for row in registry["claims"]} == {
        "UVG-RS-RENORMALIZABILITY", "UVG-ASYMPTOTIC-FREEDOM", "UVG-PREDICTIVITY",
        "UVG-UNITARITY", "UVG-SCALARON-SIGN",
    }, "claim matrix drift")
    require(len(registry["primary_sources"]) == 5, "primary-source packet drift")
    require(len(registry["reopen_requires"]) == 5, "reopening packet drift")

    paper = str(bundle["paper"])
    for token in ("FAILED_HARDENING_GATE", "PARKED_REQUIRES_RECONSTRUCTION", "historical drafting evidence"):
        require(token in paper, f"paper fence missing {token}")

    require("FAILED_HARDENING_GATE" in str(bundle["staging"]), "staging disposition stale")
    require("PARKED_REQUIRES_RECONSTRUCTION" in str(bundle["inventory"]), "inventory disposition stale")

    paper_item = paper_agenda_item(agenda)
    require(paper_item["state"] == "PARKED_REQUIRES_RECONSTRUCTION", "agenda paper state stale")
    require("heat-kernel" in paper_item["next_swing"], "agenda reopening packet incomplete")

    for key, name in (("current", "current state"), ("status", "research status"), ("next_steps", "next steps")):
        surface = str(bundle[key])
        require("uv-gravity candidate" in surface.lower(), f"{name} missing audit result")
        require("FAILED_HARDENING_GATE" in surface, f"{name} missing exact disposition")

    require(registry["canon_verdict_change"] == "none", "canon ceiling drift")
    require(registry["public_posture_change"] == "none", "public posture drift")


def selftest(bundle: dict[str, object]) -> None:
    mutations = []

    wrong_disposition = copy.deepcopy(bundle)
    wrong_disposition["registry"]["disposition"] = "PASS"
    mutations.append(wrong_disposition)

    missing_claim = copy.deepcopy(bundle)
    missing_claim["registry"]["claims"].pop()
    mutations.append(missing_claim)

    unfenced_paper = copy.deepcopy(bundle)
    unfenced_paper["paper"] = str(unfenced_paper["paper"]).replace("historical drafting evidence", "live claim")
    mutations.append(unfenced_paper)

    stale_agenda = copy.deepcopy(bundle)
    paper_agenda_item(stale_agenda["agenda"])["state"] = "ACTIVE"
    mutations.append(stale_agenda)

    incomplete_reopen = copy.deepcopy(bundle)
    item = paper_agenda_item(incomplete_reopen["agenda"])
    item["next_swing"] = item["next_swing"].replace("heat-kernel", "curvature")
    mutations.append(incomplete_reopen)

    stale_status = copy.deepcopy(bundle)
    stale_status["status"] = str(stale_status["status"]).replace("FAILED_HARDENING_GATE", "UNREVIEWED")
    mutations.append(stale_status)

    for index, mutation in enumerate(mutations, start=1):
        try:
            validate(mutation)
        except AssertionError:
            continue
        raise AssertionError(f"planted regression {index} escaped")


parser = argparse.ArgumentParser()
parser.add_argument("--selftest", action="store_true", help="run six planted regression mutations")
args = parser.parse_args()
bundle = load_bundle()
validate(bundle)
if args.selftest:
    selftest(bundle)
    print("UV gravity claim-grade and overlap audit selftest: PASS (6/6 caught)")
else:
    print("UV gravity claim-grade and overlap audit: PASS")
