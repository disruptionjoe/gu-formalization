#!/usr/bin/env python3
"""K608 analytic rational upper envelopes for K606 diagonal self norms."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k608-k500-diagonal-self-norm-analytic-envelopes.json"


def strict(path: str) -> dict[str, Any]:
    return json.loads((ROOT / path).read_text())


def frac(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def gamma_upper_twice(argument_twice: int) -> Fraction:
    """Rational upper for Gamma(argument_twice/2), using sqrt(pi)<2."""
    if argument_twice % 2 == 0:
        return Fraction(math.factorial(argument_twice // 2 - 1))
    n = (argument_twice - 1) // 2
    return Fraction(2 * math.factorial(2 * n), 4**n * math.factorial(n))


def side_upper(side: list[Any]) -> Fraction:
    kind, rank, contracted = side[0], int(side[1]), {int(i) for i in side[2]}
    assert kind in {"C", "A"}
    assert (kind == "C" and not contracted) or (kind == "A" and len(contracted) == 1)
    assert all(1 <= i < rank for i in contracted)
    alphas = [Fraction(1) if i in contracted else Fraction(1, 2) for i in range(1, rank + 1)]
    beta = Fraction(rank) - sum(alphas)
    assert beta > 0
    denominator = Fraction(1)
    for j in range(2, rank + 1):
        tail = Fraction(rank - j + 1) - sum(alphas[j - 1 :])
        assert tail > 0
        denominator *= tail
    gamma_upper = gamma_upper_twice(2 * beta.numerator // beta.denominator)
    # Exterior Cauchy--Schwarz and Hadamard give one kappa(2s_i) factor per
    # uncontracted coordinate.  x K_1(x)<=1, pi>=3 and 2pi>=6 yield the
    # factors below.  K604's kappa kernel already includes its normalization.
    return (
        Fraction(1, 3 ** (2 * len(contracted)))
        * Fraction(1, 6 ** (rank - len(contracted)))
        * (gamma_upper / (Fraction(16) ** int(2 * beta) * denominator)) ** 2
    )


def build() -> dict[str, Any]:
    k604 = strict("lab/process/k604-k500-determinant-simplex-kernel-atlas.json")
    k606 = strict("lab/process/k606-k500-self-norm-quadrature-compression.json")
    k602 = strict("lab/process/k602-k500-order-two-numerical-moment-enclosure.json")
    rows = {row["id"]: row for row in k604["atlas"]["classes"]}
    endpoint_ids = sorted({rid for closure in k606["closure"]["closure_rows"] for rid in closure[1:3]})
    envelopes = []
    patterns: dict[tuple[str, int, tuple[int, ...]], Fraction] = {}
    counts: Counter[str] = Counter()
    for identifier in endpoint_ids:
        row = rows[identifier]
        assert row["l"] == row["r"]
        assert all(block[0] == block[1] for block in row["b"])
        upper = side_upper(row["l"])
        key = (row["l"][0], int(row["l"][1]), tuple(row["l"][2]))
        patterns[key] = upper
        counts[row["k"]] += 1
        envelopes.append([identifier, upper.numerator, upper.denominator])
    pattern_rows = [
        [kind, rank, list(contracted), upper.numerator, upper.denominator]
        for (kind, rank, contracted), upper in sorted(patterns.items())
    ]
    digest = hashlib.sha256(json.dumps(envelopes, separators=(",", ":")).encode()).hexdigest()
    return {
        "schema_version": "1.0",
        "result_id": "K608-K500-DIAGONAL-SELF-NORM-ANALYTIC-ENVELOPES",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "classification": "INTERNAL_CONDITIONAL_MATHEMATICS",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Rigorous rational upper envelopes for all K606 positive diagonal determinant-simplex self norms without numerical quadrature.",
        "gu_typed_objects": {
            "input": "K606's 291 cyclic and 1,323 action diagonal self-norm descriptors",
            "pairing": "the K604 normalized exterior determinant-simplex Hilbert pairing",
            "result": "analytic diagonal envelope bank MAP-TYPE=outward-rational-majorant",
            "target": "K606 cross-class propagation and K609 finite N/A_F/B_F moment aggregation",
        },
        "analytic_theorem": {
            "determinant_step": "Exterior Cauchy--Schwarz plus Hadamard bounds each species self determinant by the product of its diagonal kappa(2s_i) entries.",
            "bessel_step": "x K_1(x)<=1 gives kappa(2s_i)<=1/(2 pi s_i); each contracted scalar gives kappa(s_c)<=1/(pi s_c).",
            "simplex_step": "The ordered simplex power majorant integrates exactly by sequential beta factors and Gamma(q-sum alpha)/(256^(q-sum alpha)).",
            "rational_outward_constants": "pi>=3, 2pi>=6 and sqrt(pi)<2 replace every remaining transcendental factor outwardly.",
            "normalization_counted_once": "K604's kappa(t)=K_1(t)/pi kernel formula already incorporates the serialized side normalization; no additional (2 pi)^(-q) factor is charged.",
            "within_determinant_interference_preserved_until_majorant": True,
        },
        "envelope_bank": {
            "encoding": "[K606 self-class id,numerator,denominator]",
            "count": len(envelopes),
            "cyclic_count": counts["N"],
            "action_count": counts["B_F"],
            "pattern_encoding": "[side kind,rank,contracted positions,numerator,denominator]",
            "pattern_count": len(pattern_rows),
            "pattern_envelopes": pattern_rows,
            "envelopes": envelopes,
            "digest": digest,
        },
        "exact_controls": {
            "all_K606_endpoints_covered": len(envelopes) == 1614,
            "all_envelopes_strictly_positive": all(n > 0 and d > 0 for _, n, d in envelopes),
            "all_action_contractions_precede_last_simplex_coordinate": all(c[0] < rank for kind, rank, c, _, _ in pattern_rows if kind == "A"),
            "order_two_cyclic_path_upper": frac(side_upper(["C", 2, []])),
            "two_order_two_path_uppers_dominate_K602_N2_upper": 2 * side_upper(["C", 2, []]) >= Fraction(k602["seed_moment_intervals"]["q00"]["N_2"][1]),
        },
        "decision": {
            "outward_diagonal_upper_envelopes_emitted": True,
            "K606_all_self_norms_covered": len(envelopes) == 1614,
            "numerical_diagonal_values_claimed": False,
            "complete_finite_K456_moments_emitted": False,
            "complete_K500_uniform_leakage_emitted": False,
            "native_noncyclic_floor_emitted": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
            "next_exact_input": "Propagate the 1,614 exact rational uppers through K606's closure, retain signed coefficients seedwise, compose K602's order-two intervals and K574's tail once, and test the complete normalized leakage uniformly.",
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "Analytic outward upper envelopes, not quadrature values, for all 1,614 K606 diagonal norms. No noncyclic floor, K473/K152 result, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion moves.",
    }


def validate(payload: dict[str, Any]) -> None:
    bank, control, decision = payload["envelope_bank"], payload["exact_controls"], payload["decision"]
    assert bank["count"] == 1614 and bank["cyclic_count"] == 291 and bank["action_count"] == 1323
    assert len(bank["envelopes"]) == 1614 and len(bank["digest"]) == 64
    assert all(control.values())
    assert decision["outward_diagonal_upper_envelopes_emitted"] and decision["K606_all_self_norms_covered"]
    assert not any(decision[key] for key in (
        "numerical_diagonal_values_claimed", "complete_finite_K456_moments_emitted",
        "complete_K500_uniform_leakage_emitted", "native_noncyclic_floor_emitted",
        "K473_released", "native_K152_interval_emitted",
    ))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build(); validate(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write: OUTPUT.write_text(rendered)
    else: print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
