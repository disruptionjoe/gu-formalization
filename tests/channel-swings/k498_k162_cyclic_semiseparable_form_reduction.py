#!/usr/bin/env python3
"""K498 exact same-form matrix on the exhaustive K492 cyclic contrasts."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k498-k162-cyclic-semiseparable-form-reduction.json"
ROUTING = (
    "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional "
    "particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net "
    "chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass "
    "route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism "
    "without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its "
    "source-native pointers before reusing this result."
)


class CertificateError(ValueError):
    pass


def q(value: Any) -> Fraction:
    try:
        return value if isinstance(value, Fraction) else Fraction(value)
    except (TypeError, ValueError, ZeroDivisionError) as exc:
        raise CertificateError(f"invalid rational {value!r}") from exc


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def tails(values: Sequence[Fraction]) -> list[Fraction]:
    result = [Fraction() for _ in values]
    running = Fraction()
    for index in range(len(values) - 1, -1, -1):
        running += values[index]
        result[index] = running
    return result


def matmul(left, right):
    return [
        [sum((left[i][k] * right[k][j] for k in range(len(right))), Fraction()) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def compile_reduction(
    *, word_masses: Sequence[Any], shifted_free_diagonal: Sequence[Any],
    regular_core_diagonal: Sequence[Any], shape_diagonal: Sequence[Any],
) -> dict[str, Any]:
    a = list(map(q, word_masses))
    alpha = list(map(q, shifted_free_diagonal))
    w = list(map(q, regular_core_diagonal))
    lam = list(map(q, shape_diagonal))
    size = len(a)
    if size < 2 or not (size == len(alpha) == len(w) == len(lam)):
        raise CertificateError("four equal sequences of length at least two are required")
    if a[0] != 1 or any(value <= 0 for value in a):
        raise CertificateError("positive normalized word masses are required")
    if alpha[0] + w[0] != 0:
        raise CertificateError("the K491 seed cancellation alpha0+w0=0 is required")

    b = tails(a)
    f = [w_i + lam_i * a_i for w_i, lam_i, a_i in zip(w, lam, a, strict=True)]
    F = tails(f)
    metric = [[b[max(i, j)] for j in range(size)] for i in range(size)]
    form = [[F[max(i, j)] + (alpha[i] if i == j else 0) for j in range(size)] for i in range(size)]

    # Columns are K492's u_j=e_(j-1)-(B_(j-1)/B_j)e_j, j=1,...,N.
    columns = [[Fraction() for _ in range(size - 1)] for _ in range(size)]
    ratios = [Fraction()]
    for j in range(1, size):
        ratio = b[j - 1] / b[j]
        ratios.append(ratio)
        columns[j - 1][j - 1] = 1
        columns[j][j - 1] = -ratio
    transformed_metric = matmul(transpose(columns), matmul(metric, columns))
    transformed_form = matmul(transpose(columns), matmul(form, columns))

    predicted = [[Fraction() for _ in range(size - 1)] for _ in range(size - 1)]
    diagonal_norms = []
    semiseparable_left = []
    semiseparable_right = []
    for j in range(1, size):
        rj = ratios[j]
        diagonal_norms.append(a[j - 1] * b[j - 1] / b[j])
        semiseparable_left.append(1 - rj)
        semiseparable_right.append(F[j - 1] - rj * F[j])
        predicted[j - 1][j - 1] = (
            alpha[j - 1] + rj * rj * alpha[j] + f[j - 1] + (rj - 1) ** 2 * F[j]
        )
        for k in range(j + 1, size):
            rk = ratios[k]
            value = (1 - rj) * (F[k - 1] - rk * F[k])
            if k == j + 1:
                value -= rj * alpha[j]
            predicted[j - 1][k - 1] = value
            predicted[k - 1][j - 1] = value

    expected_metric = [
        [diagonal_norms[i] if i == j else Fraction() for j in range(size - 1)]
        for i in range(size - 1)
    ]
    if transformed_metric != expected_metric:
        raise AssertionError("K492 metric diagonalization failed")
    if transformed_form != predicted:
        raise AssertionError("semiseparable form formula failed")

    return {
        "word_masses": list(map(qstr, a)),
        "metric_tail_masses": list(map(qstr, b)),
        "combined_physical_level_scalars": list(map(qstr, f)),
        "combined_tail_scalars": list(map(qstr, F)),
        "contrast_ratios": list(map(qstr, ratios[1:])),
        "contrast_M_norms": list(map(qstr, diagonal_norms)),
        "semiseparable_left": list(map(qstr, semiseparable_left)),
        "semiseparable_right": list(map(qstr, semiseparable_right)),
        "transformed_metric": [[qstr(value) for value in row] for row in transformed_metric],
        "transformed_form": [[qstr(value) for value in row] for row in transformed_form],
        "formula_matches_dense_congruence": True,
        "dense_entry_count": (size - 1) ** 2,
        "scalar_sequence_count": 4 * size,
    }


def build() -> dict[str, Any]:
    control = compile_reduction(
        word_masses=[1, Fraction(1, 4), Fraction(1, 16), Fraction(1, 64)],
        shifted_free_diagonal=[256, 3, 5, 7],
        regular_core_diagonal=[-256, -2, Fraction(1, 2), Fraction(-1, 4)],
        shape_diagonal=[-2, 1, -2, 1],
    )
    return {
        "schema_version": "1.0",
        "result_id": "K498-K162-CYCLIC-SEMISEPARABLE-FORM-REDUCTION",
        "created": "2026-09-25",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "gu_comparator_routing": ROUTING,
        "scope": "The fixed K491 same form restricted to K492's exhaustive cyclic M-orthogonal contrast basis; noncyclic K162 states are excluded.",
        "gu_typed_objects": {
            "result": "cyclic semiseparable congruence MAP-TYPE=form-reduction",
            "carrier": "K139 Neumann cyclic closure inside one K162 charge sector",
            "pairing": "physical positive Gram M=S* S",
            "form": "R_ref with K491 diagonal-plus-max-tail entries",
            "real_structure": "CAR adjoint on the fixed q00 or q10 charge sector",
            "grading": "bath-particle number and fixed charge",
            "action_owner": "repository-supplied conditional operator; no source/GU action selection",
            "target": "complete cyclic-complement floor prerequisite for K494/K473",
        },
        "theorem": {
            "contrast_basis": "u_j=e_(j-1)-r_j e_j with r_j=B_(j-1)/B_j",
            "metric_diagonal": "M(u_j,u_k)=delta_jk a_(j-1)B_(j-1)/B_j",
            "combined_level_scalar": "f_n=w_n+lambda_n a_n",
            "combined_tail": "F_j=sum_(n>=j)f_n",
            "diagonal_entry": "alpha_(j-1)+r_j^2 alpha_j+f_(j-1)+(r_j-1)^2 F_j",
            "offdiagonal_entry": "(1-r_j)(F_(k-1)-r_k F_k)-1_(k=j+1) r_j alpha_j for j<k",
            "structure": "symmetric rank-one semiseparable tail plus one nearest-neighbor correction",
            "consequence": "the cyclic form needs scalar sequences and tail control, not an independently assembled dense cyclic Gram",
        },
        "exact_control": control,
        "decision": {
            "K492_basis_composed_with_K491_form": True,
            "dense_cyclic_Gram_required": False,
            "native_infinite_cyclic_floor_emitted": False,
            "next_exact_input": "Supply outward native alpha_n, combined f_n and infinite-tail controls, then apply K499's rational positivity test to expanding prefixes with a certified tail floor.",
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "Exact cyclic-form reduction only. No native infinite cyclic floor, noncyclic floor, K473 beta, K152 interval, source, ledger, canon, paper, public or physical conclusion follows.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    if args.write:
        OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    else:
        print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
