#!/usr/bin/env python3
"""K491 cancellation-safe K139/K168 form on a Neumann cyclic orbit."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k491-k139-cyclic-tail-kernel-form.json"


class CertificateError(ValueError):
    pass


def q(value: Any) -> Fraction:
    try:
        return value if isinstance(value, Fraction) else Fraction(value)
    except (ValueError, ZeroDivisionError, TypeError) as exc:
        raise CertificateError(f"invalid rational value {value!r}") from exc


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def tail_sums(values: Sequence[Fraction]) -> list[Fraction]:
    result = [Fraction() for _ in values]
    running = Fraction()
    for index in range(len(values) - 1, -1, -1):
        running += values[index]
        result[index] = running
    return result


def compile_cyclic_form(
    *, word_masses: Sequence[Any], shifted_free_diagonal: Sequence[Any],
    regular_core_diagonal: Sequence[Any], shape_diagonal: Sequence[Any],
) -> dict[str, Any]:
    a = list(map(q, word_masses))
    alpha = list(map(q, shifted_free_diagonal))
    w = list(map(q, regular_core_diagonal))
    lam = list(map(q, shape_diagonal))
    if not a or not (len(a) == len(alpha) == len(w) == len(lam)):
        raise CertificateError("four equal nonempty sequences are required")
    if a[0] != 1 or any(value <= 0 for value in a):
        raise CertificateError("the normalized cyclic seed requires a0=1 and positive word masses")
    if alpha[0] + w[0] != 0:
        raise CertificateError("K139 seed cancellation alpha0+w0=0 is required")

    b = tail_sums(a)
    e = tail_sums(w)
    c = tail_sums([lam_i * a_i for lam_i, a_i in zip(lam, a, strict=True)])
    size = len(a)
    metric = [[b[max(i, j)] for j in range(size)] for i in range(size)]
    base = [[e[max(i, j)] + (alpha[i] if i == j else 0) for j in range(size)] for i in range(size)]
    shape = [[c[max(i, j)] for j in range(size)] for i in range(size)]

    projection = b[1] / b[0] if size > 1 else Fraction()
    if size > 1:
        base_cross = base[0][1] - projection * base[0][0]
        shape_cross = shape[0][1] - projection * shape[0][0]
        combined_cross = base_cross + shape_cross
        expected_base = e[1] / b[0]
        expected_shape = sum((lam[n] - lam[0]) * a[n] for n in range(1, size)) / b[0]
        if base_cross != expected_base or shape_cross != expected_shape:
            raise AssertionError("tail-kernel cross reduction failed")
    else:
        base_cross = shape_cross = combined_cross = Fraction()
        expected_base = expected_shape = Fraction()

    return {
        "word_masses": list(map(qstr, a)),
        "tail_masses": list(map(qstr, b)),
        "regular_core_tail_scalars": list(map(qstr, e)),
        "shape_tail_scalars": list(map(qstr, c)),
        "metric_matrix": [[qstr(value) for value in row] for row in metric],
        "base_form_matrix": [[qstr(value) for value in row] for row in base],
        "shape_form_matrix": [[qstr(value) for value in row] for row in shape],
        "corrected_first_tail": f"e1-({qstr(projection)})e0" if size > 1 else "none",
        "base_cross": qstr(base_cross),
        "shape_cross": qstr(shape_cross),
        "combined_cross": qstr(combined_cross),
        "base_cross_identity": "E1/A",
        "shape_cross_identity": "sum_(n>=1)(lambda_n-lambda_0)*a_n/A",
        "combined_cross_identity": "(E1+sum_(n>=1)(lambda_n-lambda_0)*a_n)/A",
        "identities_verified": base_cross == expected_base and shape_cross == expected_shape,
    }


def build() -> dict[str, Any]:
    control = compile_cyclic_form(
        word_masses=[1, Fraction(1, 4), Fraction(1, 16), Fraction(1, 64)],
        shifted_free_diagonal=[256, 3, 5, 7],
        regular_core_diagonal=[-256, -2, Fraction(1, 2), Fraction(-1, 4)],
        shape_diagonal=[-2, 1, -2, 1],
    )
    return {
        "schema_version": "1.0",
        "result_id": "K491-K139-CYCLIC-TAIL-KERNEL-FORM",
        "created": "2026-09-25",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "The fixed K139/K156 form and K168 shape on one K162 zero-bath Neumann cyclic orbit; no noncyclic K162 vector is included.",
        "gu_typed_objects": {
            "result": "native cyclic tail-kernel form reduction MAP-TYPE=form-identity",
            "carrier": "closure span{G^n phi:n>=0} inside one K162 q00 or q10 charge sector",
            "pairing": "physical Gram M=S* S",
            "form": "R_ref=A+S*(W+W_ref)S with W bath-number preserving",
            "target": "K489 corrected first-tail cross and later cyclic-complement assembly",
        },
        "exact_theorem": {
            "metric_entries": "M_ij=B_max(i,j), B_j=sum_(n>=j)a_n",
            "base_entries": "R0_ij=delta_ij*alpha_i+E_max(i,j), E_j=sum_(n>=j)w_n",
            "shape_entries": "DeltaR_ij=C_max(i,j), C_j=sum_(n>=j)lambda_n*a_n",
            "seed_cancellation": "alpha_0+w_0=0",
            "corrected_line": "t=e1-(B1/B0)e0",
            "base_cross": "R0(e0,t)=E1/B0",
            "shape_cross": "DeltaR(e0,t)=sum_(n>=1)(lambda_n-lambda_0)a_n/B0",
            "combined_cross": "R_ref(e0,t)=[sum_(n>=1)w_n+sum_(n>=1)(lambda_n-lambda_0)a_n]/B0",
            "q00_shape_specialization": "+3O/A",
            "q10_shape_specialization": "-3O/A",
        },
        "exact_control": control,
        "decision": {
            "cancellation_safe_base_cross_reduced": True,
            "separate_auxiliary_piece_absolute_values_used": False,
            "native_scalar_tail_numerically_evaluated": False,
            "next_exact_input": "Evaluate or enclose the signed scalar E1=sum_(n>=1)<G^n phi,W_n G^n phi> using the K456 prefix and K176 tail, then retain its sign with K490's shape term.",
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "Exact native tail-kernel and cancellation identity on the K139 Neumann cyclic orbit. The signed base scalar is reduced but not numerically evaluated; no full K162 complement, K473 floor, K152 interval, source, ledger, canon, paper, public or physical conclusion follows.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    payload = build()
    if args.write:
        OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    if args.demo or not args.write:
        print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
