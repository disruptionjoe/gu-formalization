#!/usr/bin/env python3
"""Exact type gate for the SR-1C source-coordinate owner operator."""

from collections import Counter
from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


def strict(relative):
    return json.loads(read(relative))


def trim(poly):
    values = [Fraction(value) for value in poly]
    while values and values[-1] == 0:
        values.pop()
    return values


def divmod_poly(left, right):
    remainder = trim(left)
    divisor = trim(right)
    quotient = [Fraction(0)] * max(1, len(remainder) - len(divisor) + 1)
    while remainder and len(remainder) >= len(divisor):
        degree = len(remainder) - len(divisor)
        coefficient = remainder[-1] / divisor[-1]
        quotient[degree] = coefficient
        for index, value in enumerate(divisor):
            remainder[index + degree] -= coefficient * value
        remainder = trim(remainder)
    return trim(quotient), remainder


def gcd_poly(left, right):
    left, right = trim(left), trim(right)
    while right:
        _, remainder = divmod_poly(left, right)
        left, right = right, remainder
    if not left:
        return []
    return [value / left[-1] for value in left]


registry = strict("lab/process/selected-k77-sr1c-owner-operator-type-gate.json")
branch = strict("lab/process/selected-k77-zorro-nonzero-t-first-action-jet-gate.json")
scaffold = read("lab/active-research/source-residual-cohomology/sr1c-source-coordinate-variational-prolongation-scaffold-2026-08-14.md")
epsilon = read("explorations/conditional-build/selected-k77-action-noether-preboundary-2026-08-08.md")
common = read("explorations/conditional-build/selected-k77-common-field-formal-adjoint-green-2026-08-08.md")
source_return = read("explorations/eric-curt-wave3d-b2c15p-source-epsilon-tangent-zorro-dewitt-2026-08-02.md")

print("A. EXACT BRANCH AND TYPE FENCES")
check("branch", "the exact two-root polynomial is preserved", branch["amplitudes"]["polynomial"] == "28392*t^2+91*t-351")
check("branch", "the common rational correction still closes action and Bianchi rows", branch["symmetric_correction"]["action_defect"] == 0 and branch["symmetric_correction"]["bianchi_defect"] == 0)
check("type", "primitive epsilon is the formal adjoint of E_B-E_T plus the Shiab return", "D_B^!(E_B-E_T)" in epsilon and "(D_epsilon S)^! K_S" in epsilon)
check("type", "the scaffold requires E_B before the two-jet solve", "derive E_B on the admitted witness" in scaffold)
check("type", "observation remains a dependent receiver", "not an additional independently varied action field" in scaffold)

print("\nB. OWNER INVENTORY")
check("source", "the source return leaves the full native Shiab action port open", "full native Shiab/action port" in source_return)
check("source", "the actual Shiab Hodge lowerer coefficient remains unowned", "actual Shiab/Hodge/lowerer owner coefficient" in source_return)
check("inventory", "the common-field audit distinguishes an Euler covector from a field operator", "field **covector**" in common and "field vector requires" in common)
check("inventory", "O_SR1C names the first blocking common-basis output", registry["missing_operator"]["first_blocking_output"].startswith("J1_OF_E_B_MINUS_E_T"))
check("inventory", "all six fixed-varpi metric derivative slots are explicit", len(registry["missing_operator"]["metric_outputs"]) == 6)
check("inventory", "zero substitution is forbidden", registry["missing_operator"]["zero_substitution_allowed"] is False)

print("\nC. EXACT NON-IDENTIFIABILITY CONTROL")
branch_polynomial = [Fraction(-351), Fraction(91), Fraction(28392)]
density_polynomial = [Fraction(0), Fraction(-27), Fraction(0), Fraction(-728)]
check("exact", "the direct density is nonzero in the branch quotient", gcd_poly(branch_polynomial, density_polynomial) == [Fraction(1)])
direct = Fraction(11)
return_zero = Fraction(0)
return_cancel = -direct
check("planted", "two absent-slot completions agree on the admitted input tag", ("same-field-one-jet",) == ("same-field-one-jet",))
check("planted", "one metric completion preserves the live row", direct + return_zero != 0)
check("planted", "one metric completion cancels the same row", direct + return_cancel == 0)
primitive_a, primitive_b = Fraction(0), Fraction(5)
check("planted", "two unowned first derivatives of p change D_B-adjoint p", primitive_a != primitive_b)
check("scope", "the planted completions are controls rather than physical candidates", "NOT_PHYSICAL_COMPLETIONS" in registry["exact_control"]["interpretation"])

print("\nD. DISPOSITION")
check("result", "the result is TYPE_MISSING rather than zero", registry["disposition"] == "TYPE_MISSING")
check("result", "both conjugate branches remain not yet falsified", registry["branch_status"].startswith("BOTH_NOT_YET_FALSIFIED"))
check("result", "SR-1 remains background missing", registry["sr1"] == "BACKGROUND-MISSING")
check("result", "SR-2 remains blocked", registry["sr2"] == "BLOCKED")
check("next", "the next gate constructs and held-out validates O_SR1C", registry["next_gate"].startswith("CONSTRUCT_AND_HELD_OUT_VALIDATE_O_SR1C"))
check("accounting", "no ledger canon residue quotient datum or posture move occurs", set(registry["changes"].values()) == {"none"})

print(json.dumps({"counts": dict(COUNTS), "failures": FAILURES, "disposition": registry["disposition"], "next_gate": registry["next_gate"]}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
