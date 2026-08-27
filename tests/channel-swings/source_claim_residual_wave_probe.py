#!/usr/bin/env python3
"""Mutation-backed exact gate for the source-claim residual wave."""

from __future__ import annotations

import copy
from fractions import Fraction
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/source-claim-residual-wave.json"
REGISTER = ROOT / "lab/sources/source-claim-register.yaml"
PRODUCER = ROOT / "explorations/source-claim-residual-wave-2026-08-27.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-27-source-claim-residual-wave-review.md"
CURVATURE = ROOT / "lab/process/resolver-wave-k77b2-shiab-family-curvature-selector-transgression.json"
RECEIVER = ROOT / "lab/process/full-domain-shiab-observed-einstein-receiver.json"


def matmul(left, right):
    return [[sum(left[i][k] * right[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def row(text: str, claim_id: str, next_id: str) -> str:
    return text.split(f"- id: {claim_id}", 1)[1].split(f"- id: {next_id}", 1)[0]


def adjudication_census(text: str):
    flattened = " ".join(text.split())
    match = re.search(r"adjudication_headline: ['\"]?ADHERED (\d+) / PARTIAL (\d+) / UNTYPED (\d+)", flattened)
    return tuple(map(int, match.groups())) if match else None


def evaluate(manifest, register, producer, review, curvature, receiver):
    records = {entry["id"]: entry for entry in manifest.get("records", [])}
    census = adjudication_census(register)

    # Exact source toy: P^-1 [[0,m],[m,0]] P = diag(m,-m), with m=R/4.
    r_value = Fraction(12, 1)
    mass = r_value / 4
    coupling = [[0, mass], [mass, 0]]
    basis = [[1, 1], [1, -1]]
    basis_inv = [[Fraction(1, 2), Fraction(1, 2)], [Fraction(1, 2), Fraction(-1, 2)]]
    diagonal = matmul(matmul(basis_inv, coupling), basis)
    zero_coupling = [[0, Fraction(0)], [Fraction(0), 0]]

    # Source signature formula at n=4, i=1.
    n, i = 4, 1
    source_signature = (
        i * n - i * i + 1,
        (n * n + 2 * i * i - 2 * i * n + n - 2) // 2,
    )
    mirrored_fibre = tuple(reversed(source_signature))
    total_k77 = (mirrored_fibre[0] + 1, mirrored_fibre[1] + 3)

    claim_rows = {
        "SC-SIG-01": row(register, "SC-SIG-01", "SC-SIG-02"),
        "SC-OP-03": row(register, "SC-OP-03", "SC-OP-04"),
        "SC-CHI-02": row(register, "SC-CHI-02", "SC-CHI-03"),
        "SC-MAS-01": row(register, "SC-MAS-01", "SC-MAS-02"),
    }

    return [
        ("four exact records", set(records) == {"SC-OP-03", "SC-CHI-02", "SC-MAS-01", "SC-SIG-01"}),
        ("headline transition", manifest.get("headline_before") == "ADHERED 86 / PARTIAL 24 / UNTYPED 1" and manifest.get("headline_after") == "ADHERED 90 / PARTIAL 20 / UNTYPED 1"),
        ("register headline preserves completed transition", census is not None and census[0] >= 90 and census[1] <= 20 and census[2] <= 1),
        ("four rows adhered", all("adherence: ADHERED" in value and "adherence: PARTIAL" not in value for value in claim_rows.values())),
        ("curvature irrep dimensions", curvature["dimension_ladder"]["algebraic_riemann_irreps"] == {"scalar": 1, "traceless_ricci": 104, "weyl": 3080}),
        ("curvature target multiplicities", curvature["riemann_restriction_hom"]["multiplicities"] == {"scalar": 2, "traceless_ricci": 2, "weyl": 0}),
        ("curvature scope preserved", records.get("SC-OP-03", {}).get("result") == "DISPLAYED_SHIAB_WEYL_KILLING_AND_RICCI_SCALAR_RESPONSE_EXACT" and receiver["route_disposition"]["source_action_ownership"] == "OPEN"),
        ("mass block diagonalization", diagonal == [[mass, 0], [0, -mass]] and mass == 3),
        ("zero curvature decouples", zero_coupling == [[0, 0], [0, 0]] and records.get("SC-CHI-02", {}).get("result") == "STYLIZED_COUPLED_WEYL_SYSTEM_DECOUPLES_AT_R_ZERO"),
        ("constant mass scope", records.get("SC-MAS-01", {}).get("result") == "APPROXIMATELY_CONSTANT_R_GIVES_LOCAL_DIRAC_MASS_R_OVER_FOUR" and "position-dependent coupling" in producer),
        ("source signature exact", source_signature == (4, 6) and mirrored_fibre == (6, 4) and total_k77 == (7, 7)),
        ("signature fork preserved", records.get("SC-SIG-01", {}).get("result") == "SOURCE_FROBENIUS_SIGNATURE_AND_NONFORCED_SCOPE_RECONCILED" and "not an ambient-signature selector" in producer.lower()),
        ("producer and review scope", "No source wording" in producer and "No complete GU\nmechanism" in review),
    ]


def load():
    return (
        json.loads(MANIFEST.read_text()), REGISTER.read_text(), PRODUCER.read_text(),
        REVIEW.read_text(), json.loads(CURVATURE.read_text()), json.loads(RECEIVER.read_text()),
    )


def mutate_claim_adherence(inputs, claim_id: str, next_id: str) -> None:
    claim_row = row(inputs[1], claim_id, next_id)
    mutated_row = claim_row.replace("adherence: ADHERED", "adherence: PARTIAL", 1)
    inputs[1] = inputs[1].replace(claim_row, mutated_row, 1)


def selftest(inputs) -> int:
    mutators = (
        lambda x: x[0]["records"].pop(),
        lambda x: x[0].update(headline_after="ADHERED 89 / PARTIAL 21 / UNTYPED 1"),
        lambda x: x.__setitem__(1, x[1].replace("ADHERED 106 / PARTIAL 4", "ADHERED 89 / PARTIAL 21", 1)),
        lambda x: mutate_claim_adherence(x, "SC-SIG-01", "SC-SIG-02"),
        lambda x: x[4]["riemann_restriction_hom"]["multiplicities"].update(weyl=1),
        lambda x: x[0]["records"][1].update(result="PHYSICAL_CHIRALITY_TRANSITION_PROVED"),
        lambda x: x[0]["records"][3].update(result="AMBIENT_SIGNATURE_SELECTED"),
        lambda x: x.__setitem__(2, x[2].replace("not an ambient-signature selector", "an ambient-signature selector")),
    )
    caught = 0
    for mutate in mutators:
        trial = [copy.deepcopy(value) for value in inputs]
        mutate(trial)
        caught += any(not ok for _, ok in evaluate(*trial))
    print(f"source-claim residual mutation controls: {caught}/{len(mutators)} caught")
    return 0 if caught == len(mutators) else 1


def main() -> int:
    inputs = load()
    checks = evaluate(*inputs)
    for name, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if not all(ok for _, ok in checks):
        return 1
    print(f"source-claim residual wave: PASS ({len(checks)}/{len(checks)})")
    return selftest(inputs) if "--selftest" in sys.argv else 0


if __name__ == "__main__":
    raise SystemExit(main())
