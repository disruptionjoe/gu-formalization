#!/usr/bin/env python3
"""K601 exact symmetry reduction of K179's first nonzero exchange moments."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k601-k500-order-two-moment-symmetry-reduction.json"


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K179 = load("k179_for_k601", "k179_matched_normal_order_coefficient_family.py")
K177 = K179.K177


def signature(impurity: int, letters: list[str]) -> str:
    counts = Counter(letters)
    body = ",".join(f"{label}^{counts[label]}" for label in sorted(counts))
    return f"d={impurity}|{body}"


def input_impurity(seed: int, labels: list[str]) -> int:
    impurity = seed
    for label in labels:
        impurity = K177.advance(impurity, (int(label[0]), label[1]))
    return impurity


def term_row(term: dict) -> dict:
    seed = int(term["seed_impurity"])
    labels = list(term["input_letters"])
    in_impurity = input_impurity(seed, labels)
    in_signature = signature(in_impurity, labels)
    out_signature = term["output_signature"]
    return {
        "contraction_id": term["contraction_id"],
        "seed_impurity": seed,
        "charge": list(K177.charges(seed, ())),
        "input_impurity": in_impurity,
        "input_signature": in_signature,
        "output_impurity": term["output_impurity"],
        "output_signature": out_signature,
        "exact_operator_coefficient": term["exact_operator_coefficient"],
        "cyclic_overlap_allowed": in_signature == out_signature,
        "normalization_prefactor": term["output_kernel_formula"]["normalization_prefactor"],
        "denominator_count": len(term["contracted_resolvent_affine_forms"]["all_term_denominators"]),
        "variable_provenance": term["output_variable_provenance"],
    }


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def control() -> dict:
    n, a, b = Fraction(5), Fraction(3), Fraction(2)
    q00 = b / n - a * a / (n * n)
    q10 = b / n - a * a / (4 * n * n)
    return {
        "n": q(n),
        "a": q(a),
        "b": q(b),
        "cauchy_condition": a * a <= n * b,
        "q00_leakage_square": q(q00),
        "q10_leakage_square": q(q10),
        "q10_minus_q00": q(q10 - q00),
        "q10_lower_from_cauchy": q(Fraction(3, 4) * b / n),
        "q00_nonnegative": q00 >= 0,
        "q10_strictly_positive": q10 > 0,
        "difference_identity_passes": q10 - q00 == Fraction(3, 4) * a * a / (n * n),
        "q10_lower_passes": q10 >= Fraction(3, 4) * b / n,
    }


def build() -> dict:
    terms = [term for term in K179.coefficient_family() if term["order"] == 2]
    rows = [term_row(term) for term in terms]
    by_seed = {str(seed): [row for row in rows if row["seed_impurity"] == seed] for seed in (0, 1, 2)}
    common_prefactors = {row["normalization_prefactor"] for row in rows}
    common_denominator_counts = {row["denominator_count"] for row in rows}
    common_provenance = {tuple(row["variable_provenance"]) for row in rows}
    overlap_counts = {seed: sum(row["cyclic_overlap_allowed"] for row in group) for seed, group in by_seed.items()}
    exact_control = control()
    return {
        "schema_version": "1.0",
        "result_id": "K601-K500-ORDER-TWO-MOMENT-SYMMETRY-REDUCTION",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "classification": "INTERNAL_CONDITIONAL_MATHEMATICS",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "K179's complete first nonzero matched-exchange family at order two on the q00, q10 and charge-conjugate q01 K162 seeds, reduced before quadrature by exact impurity/exterior-sector orthogonality and equal-coupling flavor symmetry.",
        "gu_typed_objects": {
            "carrier": "K162 order-two q00/q10/q01 cyclic path sectors in normalized CAR exterior coordinates",
            "action_vector": "the six K179 order-two matched-exchange output kernels",
            "pairing": "regular Hilbert pairing transported from M=S* S, orthogonal across unequal impurity or exterior species signatures",
            "result": "first-nonzero moment block reduction MAP-TYPE=orthogonal-sector-decomposition",
            "target": "the order-two contribution to K599's N, A_F and B_F moments",
        },
        "K179_replay": {
            "complete_order_two_term_count": len(terms),
            "rows": rows,
            "terms_per_seed": {seed: len(group) for seed, group in by_seed.items()},
            "cyclic_overlap_allowed_per_seed": overlap_counts,
            "common_normalization_prefactor": common_prefactors == {"(2*pi)^(-4/2)"},
            "common_three_resolvent_denominators": common_denominator_counts == {3},
            "common_output_variable_provenance": common_provenance == {(2, 3)},
            "vacuum_coefficients": [row["exact_operator_coefficient"] for row in by_seed["0"]],
            "one_impurity_coefficients": [row["exact_operator_coefficient"] for row in by_seed["1"]],
            "charge_conjugate_coefficients": [row["exact_operator_coefficient"] for row in by_seed["2"]],
        },
        "symmetry_reduction": {
            "common_scalar_integrals": {
                "n": "squared norm of one order-two cyclic path kernel",
                "a": "unsigned overlap of the same-flavor cyclic path with its order-two exchange image",
                "b": "squared norm of one order-two exchange output kernel",
                "constraints": ["n>0", "b>0", "a^2<=n*b"],
            },
            "q00_moments": {"N_2": "2*n", "A_2": "2*a", "B_2": "2*b"},
            "q10_moments": {"N_2": "2*n", "A_2": "-a", "B_2": "2*b"},
            "q01_moments": {"N_2": "2*n", "A_2": "-a", "B_2": "2*b"},
            "q00_leakage_square": "b/n-a^2/n^2",
            "q10_q01_leakage_square": "b/n-a^2/(4*n^2)",
            "q10_minus_q00": "3*a^2/(4*n^2)",
            "q10_strict_lower": "lambda_2(q10)^2>=3*b/(4*n)>0 by Cauchy and nonzero positive exchange kernel",
            "zero_cross_terms_removed": "All cyclic/action overlaps with unequal impurity or exterior signatures, and all action/action products between distinct output signatures.",
        },
        "exact_controls": exact_control,
        "decision": {
            "first_nonzero_exchange_family_reduced": True,
            "six_terms_require_six_independent_quadratures": False,
            "minimum_order_two_scalar_integrals": ["n", "a", "b"],
            "q10_q01_order_two_leakage_strictly_positive": True,
            "numerical_order_two_moments_emitted": False,
            "complete_finite_K456_moments_emitted": False,
            "complete_K500_uniform_leakage_emitted": False,
            "native_noncyclic_floor_emitted": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
            "next_exact_input": "Outwardly enclose the three common order-two integrals n,a,b once, then extend the same impurity/exterior signature reduction to orders three through twelve before applying K599 with K574's sharp tail exactly once.",
        },
        "source_and_ledger_effect": "none",
        "preflight_bookend": {
            "route_comparison": "Delete exact zero Gram products and quotient flavor copies before commissioning continuum quadrature.",
            "retrieval_collision_result": "K179 serializes all six order-two coefficients and sectors but does not reduce their three K599 moments.",
            "strongest_alternative": "Termwise quadrature of six copies is correct but duplicates isometric kernels and obscures the q10 cyclic-overlap deficit.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Treating the symbolic n,a,b reduction or the positive order-two truncation as a complete finite or all-level leakage bound.",
            "strongest_contrary_construction": "Higher orders can enter the same output sectors and interfere, so the complete action vector still requires orders three through twelve plus K574's tail.",
            "weakest_reproducibility_seam": "The scalar integrals are exactly identified but not yet outwardly evaluated.",
        },
        "claim_ceiling": "Exact first-nonzero K179 moment reduction: the six order-two exchange terms collapse by equal-coupling symmetry and impurity/exterior-sector orthogonality to three scalar integrals n,a,b. The q00 moments are (2n,2a,2b), while q10 and q01 are (2n,-a,2b); hence their order-two leakage exceeds q00 by 3a^2/(4n^2) and is at least 3b/(4n)>0. This is a truncation-level structural result, not a numerical K456 moment evaluation or a complete uniform K500 leakage bound; higher-order interference, K574 tail composition, the noncyclic floor, K473, K152 and all source, ledger, canon, paper, public, novelty and physical conclusions remain open.",
    }


def validate(payload: dict) -> None:
    replay = payload["K179_replay"]
    reduction = payload["symmetry_reduction"]
    control_data = payload["exact_controls"]
    decision = payload["decision"]
    assert replay["complete_order_two_term_count"] == 6
    assert replay["terms_per_seed"] == {"0": 2, "1": 2, "2": 2}
    assert replay["cyclic_overlap_allowed_per_seed"] == {"0": 2, "1": 1, "2": 1}
    assert replay["common_normalization_prefactor"] and replay["common_three_resolvent_denominators"] and replay["common_output_variable_provenance"]
    assert replay["vacuum_coefficients"] == ["1", "1"]
    assert replay["one_impurity_coefficients"] == ["-1", "-1"] and replay["charge_conjugate_coefficients"] == ["-1", "-1"]
    assert reduction["q00_leakage_square"] == "b/n-a^2/n^2"
    assert reduction["q10_q01_leakage_square"] == "b/n-a^2/(4*n^2)"
    assert control_data["cauchy_condition"] and control_data["q00_nonnegative"] and control_data["q10_strictly_positive"]
    assert control_data["difference_identity_passes"] and control_data["q10_lower_passes"]
    assert decision["first_nonzero_exchange_family_reduced"] and not decision["six_terms_require_six_independent_quadratures"]
    assert decision["minimum_order_two_scalar_integrals"] == ["n", "a", "b"] and decision["q10_q01_order_two_leakage_strictly_positive"]
    assert not any(decision[key] for key in ("numerical_order_two_moments_emitted", "complete_finite_K456_moments_emitted", "complete_K500_uniform_leakage_emitted", "native_noncyclic_floor_emitted", "K473_released", "native_K152_interval_emitted"))


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
