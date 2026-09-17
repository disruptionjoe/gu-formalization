#!/usr/bin/env python3
"""Independent K210 squarefree-jet/direct-density replay; no producer import."""
from __future__ import annotations

from copy import deepcopy
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / "lab/process"
DATA = P / "k210-order-six-duffy-chain.json"
SOURCES = {str(k): P / f"k{k}-order-six-{name}.json" for k, name in (
    (185, "duffy-face-tail-wave"), (203, "positive-moment-rule"),
    (208, "cubic-moment-rule"), (209, "cubic-core-geometry"))}
FULL = 15


def multiply(left, right):
    out = {}
    for a, x in left.items():
        for b, y in right.items():
            if a & b == 0:
                out[a | b] = out.get(a | b, F(0)) + x*y
    return out


def direct_pullback(u, indices, polynomial):
    """Expand f(z(u+sum labelled t)) in the squarefree jet ring."""
    one = {0: F(1)}
    sticks = []
    for j, value in enumerate(u):
        x = {0: value}
        x.update({1 << slot: F(1) for slot, index in enumerate(indices)
                  if index == j})
        sticks.append(x)
    z = []
    residual = one
    for stick in sticks:
        z.append(multiply(residual, stick))
        complement = {0: 1-stick[0], **{key: -v for key, v in stick.items() if key}}
        residual = multiply(residual, complement)
    z.append(residual)
    total = F(0)
    for coefficient, factors in polynomial:
        term = one
        for coordinate in factors:
            term = multiply(term, z[coordinate])
        total += coefficient*term.get(FULL, F(0))
    return total


def check(data):
    assert data["input_sha256"] == {
        key: hashlib.sha256(path.read_bytes()).hexdigest()
        for key, path in SOURCES.items()}
    old = json.loads(SOURCES["185"].read_text())
    catalog = old["exact_allocation_certificate"]["allocation_catalog"]
    assert data["term_specific_allocation_count"] == len(catalog) == 1276
    # Derive the stick exponents directly by collecting the fourteen simplex
    # powers and the lower-triangular Jacobian powers, not by the producer's
    # tail-sum helper.
    for record in catalog.values():
        beta = [1-F(x) for x in record["loads"].split(",")]
        assert len(beta) == 14 and sum(beta) == 6 and min(beta) >= F(1, 3)
        powers = []
        for j in range(13):
            u_power = beta[j]-1
            complement_power = sum((beta[k]-1 for k in range(j+1, 14)), F(0)) + 12-j
            powers.append((u_power, complement_power))
        if all(b == F(1, 3) for b in beta):
            assert data["common_stick_exponents_u_then_one_minus_u"] == [
                [str(a), str(b)] for a, b in powers]
    common = [F(x) for x in data["common_beta_parameters"]]
    assert common == [F(1, 3)]*14
    assert data["common_stick_exponents_u_then_one_minus_u"] == [
        [str(F(-2, 3)), str(F(14-j-1, 3)-1)] for j in range(13)]
    assert data["fourth_set_partition_counts_by_outer_derivative_order"] == {
        "1": 1, "2": 7, "3": 6, "4": 1}
    assert data["fourth_mixed_chart_bound"] == (
        "16*(M1+7*M2+6*M3+M4), Mk=sup ||D^k f||_2 on chart image; "
        "conservative |D_B z|_2<=2^|B|")
    assert data["fourth_pure_stick_bound"] == (
        "4*M4 since z is affine in each u_i and ||D_i z||_2<=sqrt(2)")
    u = [F(x) for x in data["rational_test_sticks"]]
    assert u == [F(i+2, 2*i+17) for i in range(13)]
    polynomial = [(F(c), tuple(f)) for c, f in data["rational_test_polynomial"]]
    assert polynomial == [(F(1), (0, 0, 0, 0)), (F(-3), (2, 5)),
                          (F(2), (13, 13)), (F(1), (1, 3, 8))]
    assert len(data["rational_fourth_partial_controls"]) == 5
    for name, answer in data["rational_fourth_partial_controls"].items():
        indices = tuple(map(int, name.split("-")))
        assert len(indices) == 4
        assert direct_pullback(u, indices, polynomial) == F(answer), name
    assert data["unchanged_full_domain_error_rational"] == json.loads(
        SOURCES["208"].read_text())["all_group_absolute_error_ceiling_rational"]


def hostile(data):
    mutants = []
    for field, changed in (
        ("term_specific_allocation_count", 1),
        ("fourth_mixed_chart_bound", "16*M4"),
        ("fourth_set_partition_counts_by_outer_derivative_order", {"4": 1}),
        ("unchanged_full_domain_error_rational", "0"),
    ):
        mutant = deepcopy(data)
        mutant[field] = changed
        mutants.append(mutant)
    mutant = deepcopy(data)
    mutant["common_stick_exponents_u_then_one_minus_u"][0][1] = "0"
    mutants.append(mutant)
    mutant = deepcopy(data)
    mutant["rational_fourth_partial_controls"]["0-1-2-3"] = "0"
    mutants.append(mutant)
    for mutant in mutants:
        try:
            check(mutant)
        except AssertionError:
            continue
        raise AssertionError("hostile change survived")
    return len(mutants)


if __name__ == "__main__":
    data = json.loads(DATA.read_text())
    check(data)
    print(f"[PASS] independent squarefree fourth jets; {hostile(data)} hostile changes caught")
