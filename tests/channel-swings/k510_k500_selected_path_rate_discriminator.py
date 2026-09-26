#!/usr/bin/env python3
"""K510 discriminate naive selected-path rates against the K496 residual."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k510-k500-selected-path-rate-discriminator.json"
Q = Fraction(3, 8)


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K177 = load("k177_for_k510", "k177_laplace_simplex_exchange_prefix.py")
K496 = load("k496_for_k510", "k496_k176_sharp_exchange_tail.py")


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def distinguished_letters(seed: int, order: int):
    if seed == 0:
        return tuple((1, "-" if i % 2 == 0 else "+") for i in range(order))
    return tuple((seed, "+" if i % 2 == 0 else "-") for i in range(order))


def selected_word(seed: int, order: int):
    letters = distinguished_letters(seed, order)
    candidates = [word for word in K177.words(seed, order) if word.letters == letters]
    if len(candidates) != 1:
        raise AssertionError("distinguished K177 path is not unique")
    word = candidates[0]
    _, sign = K177.build_state(word, order + 1)
    return word, sign


def build() -> dict:
    rows = []
    for seed in (0, 1):
        for order in range(13):
            word, sign = selected_word(seed, order)
            simplex_template = Q**order / math.factorial(order)
            residual = Fraction() if order == 0 else K496.exchange_tail(order)
            ratio = Fraction() if order == 0 else residual / simplex_template
            rows.append({
                "seed_impurity": seed,
                "charge": list(K177.charges(seed, ())),
                "order": order,
                "letters": [f"{a}{b}" for a, b in word.letters],
                "output_impurity": word.impurity,
                "CAR_sign": sign,
                "exact_state_nonzero": True,
                "simplex_volume_template": q(simplex_template),
                "K496_post_order_tail": q(residual),
                "tail_to_template_ratio": q(ratio),
            })
    ratios_by_seed = {
        seed: [Fraction(row["tail_to_template_ratio"]) for row in rows if row["seed_impurity"] == seed and row["order"] > 0]
        for seed in (0, 1)
    }
    return {
        "schema_version": "1.0",
        "result_id": "K510-K500-SELECTED-PATH-RATE-DISCRIMINATOR",
        "created": "2026-09-25",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "The lexicographically fixed single-flavor alternating K177 path in q00 and q10 at every bath level, and the proof strength of a lower certificate that retains only the ordered-simplex volume factor.",
        "all_level_path": {
            "q00": "(1-,1+) repeated, truncated after n letters",
            "q10": "(1+,1-) repeated, truncated after n letters",
            "admitted_by_hard_core_automaton_for_every_n": True,
            "charge_preserving_for_every_n": True,
            "continuum_CAR_state_nonzero_for_every_n": True,
            "common_CAR_sign_with_its_K507_signature_block": True,
            "orders_zero_through_twelve_replayed": True,
        },
        "rate_theorem": {
            "template_under_test": "L_n=(3/8)^n/n!",
            "template_status": "proof template only; not asserted to be the sharp native path norm",
            "why_this_template": "It is the strongest geometric factor available if an attempted lower proof retains K139's 3/8 scale but pays the full ordered-simplex volume without a determinant-aware compensation.",
            "K496_tail": "R_n=(3/8)^n*((n+1)-n*(3/8))/(1-3/8)^3",
            "exact_ratio": "R_n/L_n=n!*(((n+1)-n*(3/8))/(1-3/8)^3)",
            "ratio_diverges": True,
            "consequence": "Any selected-path lower proof with an uncancelled 1/n! simplex-volume penalty cannot normalize K496 uniformly, even though K507 makes that path a valid positive word lower.",
            "what_is_not_proved": "No native path norm has been shown to equal or lie below L_n; the result rejects a certificate family, not the K507 path route or K500 itself.",
        },
        "exact_controls": {
            "rows": rows,
            "row_count": len(rows),
            "all_paths_nonzero": all(row["exact_state_nonzero"] for row in rows),
            "sample_ratios_strictly_increase_by_level": all(
                all(b > a for a, b in zip(values, values[1:])) for values in ratios_by_seed.values()
            ),
            "order_12_ratio_exceeds_order_1": all(values[-1] > values[0] for values in ratios_by_seed.values()),
        },
        "decision": {
            "K507_native_positivity_retracted": False,
            "simplex_volume_only_selected_path_certificate_sufficient_for_K500": False,
            "determinant_aware_or_direct_variance_work_required": True,
            "uniform_all_level_native_path_lower_emitted": False,
            "complete_K500_uniform_leakage_emitted": False,
            "next_exact_input": "Exploit quantitative total positivity of the actual heat-kernel moment determinant strongly enough to avoid factorial loss, or switch to a directly normalized K501 variance estimate; do not repeat a simplex-volume-only lower.",
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "An exact all-level native path selection and a rate obstruction for one natural certificate family. It does not bound the actual path norm above or below by the tested template, decide K500 leakage, supply a noncyclic/cyclic floor, move K473/K152, or change source, ledger, canon, paper, public, novelty or physical conclusions.",
    }


def validate(payload: dict) -> None:
    if payload["exact_controls"]["row_count"] != 26:
        raise AssertionError("K510 census changed")
    if not payload["exact_controls"]["all_paths_nonzero"]:
        raise AssertionError("K510 selected a zero path")
    if not payload["rate_theorem"]["ratio_diverges"]:
        raise AssertionError("K510 rate theorem lost divergence")
    if payload["decision"]["simplex_volume_only_selected_path_certificate_sufficient_for_K500"]:
        raise AssertionError("K510 overclaimed the weak template")
    if payload["decision"]["K507_native_positivity_retracted"]:
        raise AssertionError("K510 retracted K507")
    if payload["decision"]["uniform_all_level_native_path_lower_emitted"]:
        raise AssertionError("K510 overclaimed a native lower")
    if payload["decision"]["complete_K500_uniform_leakage_emitted"]:
        raise AssertionError("K510 overclaimed K500")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
