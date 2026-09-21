#!/usr/bin/env python3
"""K278: certify strict full-domain positivity by exact Gram reassembly."""
from __future__ import annotations

import argparse
from copy import deepcopy
from decimal import Decimal, localcontext
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROCESS = ROOT / "lab/process"
K184 = PROCESS / "k184-order-six-certified-low-rank-wave.json"
K185 = PROCESS / "k185-order-six-duffy-face-tail-wave.json"
K218 = PROCESS / "k218-order-six-exact-angular-elimination.json"
OUT = PROCESS / "k278-order-six-full-domain-gram-positivity.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def projection(entry: dict) -> tuple:
    return (
        entry["group_id"], entry["left"], entry["right"],
        entry["coefficient_product"],
    )


def validate(k184: dict, k185: dict, k218: dict) -> dict:
    gram = k184["andreief_time_gram_certificate"]["gram_entries"]
    expanded = k185["complete_face_hypergraph"]["entries"]
    witnesses = k184["localized_interval_witnesses"]["groups"]
    assert len(gram) == len(expanded) == 234
    assert [projection(x) for x in gram] == [projection(x) for x in expanded]
    assert all(x["normalization_factorials_cancel"] for x in gram)
    assert all(e["leibniz_term_count"] == len(e["terms"]) for e in expanded)

    leibniz_terms = sum(len(e["terms"]) for e in expanded)
    ordered_terms = sum((2 if e["left"] != e["right"] else 1) * len(e["terms"])
                        for e in expanded)
    groups = sorted({e["group_id"] for e in expanded})
    assert len(groups) == 18
    assert groups == sorted(witnesses)
    assert groups == sorted(k185["groups"])
    assert leibniz_terms == k185["complete_face_hypergraph"]["leibniz_terms"] == 1864
    assert ordered_terms == k218["ordered_terms_after_off_diagonal_doubling"] == 2928
    assert k218["terms"] == 1864
    assert k218["input_sha256"]["k185"] == digest(K185)
    assert k184["release_test"]["all_group_norms_have_positive_local_witnesses"]
    assert k185["release_test"]["all_1864_leibniz_terms_covered"]
    assert k185["exact_allocation_certificate"]["all_denominator_weights_sum_to_one"]
    assert k185["radial_duffy_certificate"]["all_beta_at_least_one_third"]

    lowers = [Decimal(witnesses[g]["certified_full_space_norm_squared_lower"])
              for g in groups]
    assert all(x > 0 for x in lowers)
    with localcontext() as ctx:
        ctx.prec = 90
        lower_sum = sum(lowers, Decimal(0))
    trace_bytes = json.dumps([projection(x) for x in gram], separators=(",", ":")).encode()
    return {
        "groups": groups,
        "gram_entries": len(gram),
        "leibniz_terms": leibniz_terms,
        "ordered_terms": ordered_terms,
        "strict_group_witnesses": len(lowers),
        "sum_of_certified_group_lowers": str(lower_sum),
        "gram_trace_sha256": hashlib.sha256(trace_bytes).hexdigest(),
    }


def generate() -> dict:
    k184 = json.loads(K184.read_text())
    k185 = json.loads(K185.read_text())
    k218 = json.loads(K218.read_text())
    facts = validate(k184, k185, k218)

    hostile = []
    mutations = (
        (k184, k185, k218, lambda a, b, c: b["complete_face_hypergraph"]["entries"].pop()),
        (k184, k185, k218, lambda a, b, c: b["complete_face_hypergraph"]["entries"][0].__setitem__("coefficient_product", -1)),
        (
            k184, k185, k218,
            lambda a, b, c: a["localized_interval_witnesses"]["groups"].pop(
                next(iter(a["localized_interval_witnesses"]["groups"]))
            ),
        ),
        (k184, k185, k218, lambda a, b, c: a["localized_interval_witnesses"]["groups"][next(iter(a["localized_interval_witnesses"]["groups"]))].__setitem__("certified_full_space_norm_squared_lower", "0")),
        (k184, k185, k218, lambda a, b, c: c.__setitem__("ordered_terms_after_off_diagonal_doubling", 2927)),
    )
    for index, (a0, b0, c0, mutate) in enumerate(mutations, 1):
        a, b, c = deepcopy(a0), deepcopy(b0), deepcopy(c0)
        mutate(a, b, c)
        try:
            validate(a, b, c)
        except AssertionError:
            hostile.append(index)
    assert hostile == [1, 2, 3, 4, 5]

    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "target_claim": "INTERNAL_TARGET:K218_FULL_DOMAIN_SIGN",
        "direction": "observed_to_native",
        "input_sha256": {"k184": digest(K184), "k185": digest(K185), "k218": digest(K218)},
        "exact_trace": facts,
        "theorem": {
            "identity": "The complete K218 order-six scalar equals the sum over the eighteen K184 coherent output groups of the corresponding Hilbert-space norm squared.",
            "strictness": "Every group has a certified positive-measure local witness with strictly positive norm-squared lower bound, hence the complete scalar is strictly positive.",
            "equality_chain": [
                "K184 supplies all 234 unique self/cross Gram entries with coherent coefficients and canceled wedge factorials.",
                "K185 preserves every group, left path, right path and coefficient product while exactly expanding the species determinants into 1864 Leibniz terms.",
                "Restoring off-diagonal multiplicity gives exactly 2928 ordered terms.",
                "K185 absolute integrability and K218's exact positive radial/simplex changes of variables preserve the full integral and permit the finite reassembly.",
            ],
            "strict_lower_witness": facts["sum_of_certified_group_lowers"],
            "verdict": "STRICTLY_POSITIVE_BY_EXACT_GRAM_REASSEMBLY",
        },
        "controls": {
            "producer_checks": 16,
            "hostile_mutations_rejected": len(hostile),
            "independent_probe": "tests/channel-swings/k278_order_six_full_domain_gram_positivity_probe.py",
        },
        "consumer_effect": {
            "closed": ["full K218 sign", "sign-only middle-box or collar expansion"],
            "still_open": [
                "decision-grade numerical K218 enclosure",
                "coefficient-complete base action column",
                "complete shifted form-dual residual",
                "order-six-integral-to-residual propagation map norm",
                "native K152 spectral tuple and decision margin",
            ],
            "next_rank_one": "Populate the complete native K152 consumer tuple and action-column-to-residual map; invoke K274/K275 only for the smallest finite cube demanded by an instantiated margin.",
        },
        "source_routing": "SC-ACT-01/02/06 remain ASSERTS; SC-META-53 remains UNCERTAIN; LT-SM8/LT-GR6b/RA-F1/AC-F1 remain NEEDS.",
        "ledger_effect": "none",
        "canon_paper_release_or_public_posture_move": False,
        "physical_or_source_selection": False,
        "claim_ceiling": "Strict sign only. The witness sum is a conservative nonzero certificate, not an accurate complete order-six value, K152 error budget, source-derived action coefficient, physical prediction, or ledger-grade result.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--emit", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.emit:
        print(json.dumps(result, indent=2))
    else:
        assert json.loads(OUT.read_text()) == result
        print("[PASS] K278 exact Gram trace and strict full-domain positivity; 5/5 hostile mutations rejected")
