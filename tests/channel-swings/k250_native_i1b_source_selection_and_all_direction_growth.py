#!/usr/bin/env python3
"""K250: source-selection closure and all-direction first-layer I1B growth."""
from __future__ import annotations

import argparse
from contextlib import redirect_stdout
from fractions import Fraction as Q
from hashlib import sha256
from io import StringIO
import json
from pathlib import Path
import re
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
BACKEND = ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py"
K236 = ROOT / "lab/process/k236-native-i1b-invariant-mixed-grade-symbol.json"
K249 = ROOT / "lab/process/k249-native-i1b-common-principal-hull.json"
SOURCE_REGISTER = ROOT / "lab/sources/source-claim-register.yaml"
SOURCE_EXTRACTION = ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md"
OUT = ROOT / "lab/process/k250-native-i1b-source-selection-and-all-direction-growth.json"
CHANNELS = ("comm", "symi", "symi")


def claim_block(text: str, claim_id: str) -> str:
    match = re.search(
        rf"(?ms)^- id: {re.escape(claim_id)}\n.*?(?=^- id: |\Z)", text
    )
    assert match is not None
    return match.group(0)


def calculate() -> dict[str, object]:
    register = SOURCE_REGISTER.read_text()
    extraction = SOURCE_EXTRACTION.read_text()
    op04 = claim_block(register, "SC-OP-04")
    op05 = claim_block(register, "SC-OP-05")
    assert "polarity: ASSERTS" in op04
    assert "begin with operators" in op04
    assert "polarity: UNCERTAIN" in op05
    assert "non-trivial lower-right" in op05 or "non-trivial map" in op05
    assert 'can **"begin\nwith operators like"** equation 9.16' in extraction
    assert extraction.count("southeast-zero") == 5  # ledger four plus prose control
    assert '**"non-trivial map in the lower right quadrant"**' in extraction
    assert "neither source supplies a uniqueness theorem" in extraction

    with redirect_stdout(StringIO()) as log:
        m = runpy.run_path(str(BACKEND))
    assert "FAILURES=0" in log.getvalue()
    one, zero, full = m["ONE"], m["ZERO"], m["FULL"]

    def direction(mu: int, blade: int):
        return {1 << mu: {blade: one}}

    def ordered(left, right, principal: int):
        image = m["shiab"](
            m["wedge_raw"](direction(principal, 0), right), CHANNELS
        )
        return m["wedge_raw"](left, image).get(full, {}).get(0, zero)

    odd = direction(0, 1 << 1)
    witnesses = []
    for principal in range(1, 14):
        blade = (1 << 0) | (1 << principal)
        output = direction(1, blade)
        forward = ordered(output, odd, principal)
        reverse = ordered(odd, output, principal)
        euler = (forward[0] - reverse[0]) / 2
        label = blade ^ (1 << 1)
        assert forward == (Q(-2), Q()) and reverse == zero and euler == -1
        witnesses.append(
            {
                "principal_direction": principal,
                "output": f"dx1 tensor gamma0{principal}",
                "output_label": label,
                "ordered_forward_reverse": [str(forward[0]), str(reverse[0])],
                "euler_coefficient": str(euler),
                "outside_k249_carrier": label not in range(4),
            }
        )

    assert witnesses[0]["output_label"] == 1
    outside = [row["output_label"] for row in witnesses[1:]]
    assert len(outside) == len(set(outside)) == 12
    assert all(label not in range(4) for label in outside)

    # Basis coordinates are (one-form leg, Clifford blade).  The common hull
    # must contain o, N0(o)=-E and all thirteen Np(o), p=1..13.
    odd_key = (0, 1 << 1)
    spoke_keys = [(j, (1 << 1) | (1 << j)) for j in range(2, 14)]
    witness_keys = [(1, (1 << 0) | (1 << p)) for p in range(1, 14)]
    keys = [odd_key, *spoke_keys, *witness_keys]
    lookup = {key: i for i, key in enumerate(keys)}
    assert len(lookup) == len(keys)
    vectors = [sp.zeros(len(keys), 1) for _ in range(15)]
    vectors[0][lookup[odd_key]] = 1
    for key in spoke_keys:
        vectors[1][lookup[key]] = 1
    for index, key in enumerate(witness_keys, start=2):
        vectors[index][lookup[key]] = 1
    rank = sp.Matrix.hstack(*vectors).rank()
    assert rank == 15

    return {
        "schema_version": "1.0",
        "classification": "SOURCE_NATIVE_ROUTE__LOCAL_SELECTED_SYMBOL_ONLY",
        "input_sha256": {
            "backend": sha256(BACKEND.read_bytes()).hexdigest(),
            "k236": sha256(K236.read_bytes()).hexdigest(),
            "k249": sha256(K249.read_bytes()).hexdigest(),
            "source_register": sha256(SOURCE_REGISTER.read_bytes()).hexdigest(),
            "source_extraction": sha256(SOURCE_EXTRACTION.read_bytes()).hexdigest(),
        },
        "source_selection": {
            "claims": [
                {"id": "SC-OP-04", "polarity": "ASSERTS", "effect": "displayed_candidate_grammar"},
                {"id": "SC-OP-05", "polarity": "UNCERTAIN", "effect": "nonzero_southeast_rival_admitted_without_selection"},
            ],
            "displayed_candidate": "draft equation 9.16 with four southeast zeros",
            "rival": "source-admitted unspecified non-trivial southeast map",
            "decision": "current source corpus does not select a unique full fermion operator",
            "missing": [
                "unique Shiab/operator version",
                "barred-field reality and global grading",
                "density and operative adjoint",
                "lower-order invariant bundle",
                "common stationary closed domain",
            ],
        },
        "principal_symbol": {
            "object": "selected comm/symi/symi I1B formal Euler symbol on the flat Ricci-flat T=0 zero-fermion germ",
            "seed": "o=dx0 tensor gamma1",
            "witnesses": witnesses,
            "outside_labels_p2_through_p13": outside,
            "forced_vectors": "o, E=-N0(o), and Np(o) for p=1..13",
            "forced_vector_rank": rank,
            "common_invariant_hull_dimension_lower_bound": rank,
            "theorem": "Every common invariant hull for all fourteen selected principal directions that contains o has dimension at least 15; twelve independent first-layer outputs already lie outside K249's natural 56-vector label-0/1/2/3 carrier.",
        },
        "interpretation": "K249's dx2 escape is one member of a uniform p=2..13 family, not an exceptional direction. The source-selection dependency is closed negatively for the current corpus: subsequent larger-hull work is conditional on a named candidate unless new source evidence selects an operator.",
        "source_routing": "SC-OP-04 ASSERTS and SC-OP-05 UNCERTAIN are jointly preserved; SC-ACT-01/02 ASSERTS, SC-META-53 UNCERTAIN and LT-GR6b/LT-SM8 NEEDS do not move.",
        "claim_ceiling": "Exact source underdetermination from the current registered corpus and an exact 15-dimensional lower bound for one selected local principal-symbol family. No complete all-direction hull, source-selected full operator, lower-order/common domain, quotient, spectrum, positivity, ledger/canon/public change, or K218 cancellation theorem.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = calculate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K250 source-selection closure and 15D all-direction hull lower bound")
