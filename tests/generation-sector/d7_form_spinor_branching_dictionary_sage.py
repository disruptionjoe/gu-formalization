#!/usr/bin/env sage
"""M-M4 exact D7 form-spinor and D5 Pati--Salam branching dictionary.

Run with Sage from the repository root.  The certificate reconstructs the
committed JSON cache from Weyl characters, verifies every dimension, dual and
Frobenius--Schur field, and replays the independent D7/D5 identities that close
FC-IRR, FC-HW, FC-MULT, OQ1 and OQ-CG-2 at complexified algebraic grade.
"""

from __future__ import annotations

import json
import sys
from math import comb
from pathlib import Path

from sage.all import WeylCharacterRing


ROOT = Path(__file__).resolve().parents[2]
CACHE = ROOT / "lab/process/d7-form-spinor-branching-dictionary.json"
CHECKS = 0


def check(label, condition):
    global CHECKS
    CHECKS += 1
    print("  [{}] {}".format("ok " if condition else "FAIL", label))
    assert condition, label


def labels(weight):
    coroots = weight.parent().simple_coroots()
    return [
        int(weight.inner_product(coroots[index]))
        for index in sorted(coroots.keys())
    ]


def irrep_record(ring, weight, multiplicity):
    irrep = ring(weight)
    dual_terms = list(irrep.dual())
    assert len(dual_terms) == 1 and int(dual_terms[0][1]) == 1
    dynkin = labels(weight)
    dual_dynkin = labels(dual_terms[0][0])
    # For compact Spin(4m+2) (odd D-rank), a non-self-dual irrep has
    # Frobenius--Schur indicator zero, while every self-dual irrep is of real
    # type.  Applying that classification from the exact dual labels avoids
    # expanding the enormous exterior square of every midpoint constituent.
    frobenius_schur = 1 if dynkin == dual_dynkin else 0
    return {
        "dynkin": dynkin,
        "multiplicity": int(multiplicity),
        "dimension": int(irrep.degree()),
        "dual_dynkin": dual_dynkin,
        "frobenius_schur": frobenius_schur,
    }


def character_record(ring, character):
    rows = [irrep_record(ring, weight, multiplicity) for weight, multiplicity in character]
    rows.sort(key=lambda row: (row["dynkin"], row["multiplicity"]))
    return rows


def build_dictionary():
    d7 = WeylCharacterRing("D7", style="coroots")
    vector14 = d7(1, 0, 0, 0, 0, 0, 0)
    spin_plus = d7(0, 0, 0, 0, 0, 0, 1)
    spin_minus = d7(0, 0, 0, 0, 0, 1, 0)
    form_spinor = []
    for chirality, spinor in (("S+", spin_plus), ("S-", spin_minus)):
        for degree in range(8):
            character = vector14.exterior_power(degree) * spinor
            constituents = character_record(d7, character)
            form_spinor.append({
                "chirality": chirality,
                "degree": degree,
                "hodge_partner_degree": 14 - degree,
                "expected_dimension": 64 * comb(14, degree),
                "constituents": constituents,
            })

    d5 = WeylCharacterRing("D5", style="coroots")
    vector10 = d5(1, 0, 0, 0, 0)
    f_plus = d5(0, 0, 0, 0, 1)
    f_minus = d5(0, 0, 0, 1, 0)
    t_plus = d5(1, 0, 0, 0, 1)
    t_minus = d5(1, 0, 0, 1, 0)
    ps = {
        "10x16+": character_record(d5, vector10 * f_plus),
        "10x16-": character_record(d5, vector10 * f_minus),
        "16+x144+": character_record(d5, f_plus * t_plus),
        "16+x144-": character_record(d5, f_plus * t_minus),
        "sym2_16+": character_record(d5, f_plus.symmetric_square()),
        "wedge2_16+": character_record(d5, f_plus.exterior_square()),
        "wedge5_10": character_record(d5, vector10.exterior_power(5)),
    }
    return {
        "schema_version": "1.0",
        "artifact_type": "exact_form_spinor_branching_dictionary",
        "created": "2026-08-26",
        "scope": "complexified D7 exterior-form spinors plus exact D5 Pati-Salam controls",
        "claim_ceiling": "algebraic branching and reality typing only; no real-form, action, selector, count, source or physical-sector selection",
        "d7_form_spinor": form_spinor,
        "d5_pati_salam_controls": ps,
    }


generated = build_dictionary()
if "--dump" in sys.argv:
    print(json.dumps(generated, indent=2, sort_keys=True))
    raise SystemExit(0)

committed = json.loads(CACHE.read_text(encoding="utf-8"))
check("committed cache equals fresh Sage reconstruction", committed == generated)

for row in generated["d7_form_spinor"]:
    actual = sum(item["multiplicity"] * item["dimension"] for item in row["constituents"])
    check("D7 {} degree {} dimension closes".format(row["chirality"], row["degree"]),
          actual == row["expected_dimension"])
    check("D7 {} degree {} multiplicities are positive".format(row["chirality"], row["degree"]),
          all(item["multiplicity"] > 0 for item in row["constituents"]))
    check("D7 {} degree {} FS indicators are typed".format(row["chirality"], row["degree"]),
          all(item["frobenius_schur"] in (-1, 0, 1) for item in row["constituents"]))

d7 = WeylCharacterRing("D7", style="coroots")
v14 = d7(1, 0, 0, 0, 0, 0, 0)
sp = d7(0, 0, 0, 0, 0, 0, 1)
sm = d7(0, 0, 0, 0, 0, 1, 0)
check("FC-IRR/HW: 14 x S+ = S- + 832+", v14 * sp == sm + d7(1, 0, 0, 0, 0, 0, 1))
check("FC-MULT: wedge2(14) x S+ has three multiplicity-one constituents",
      len(list(v14.exterior_power(2) * sp)) == 3
      and all(int(mult) == 1 for _, mult in v14.exterior_power(2) * sp))
check("chirality duality: dual(S+) = S-", sp.dual() == sm)
check("odd-D FS control: vector is real", v14.frobenius_schur_indicator() == 1)
check("odd-D FS control: S+ is complex", sp.frobenius_schur_indicator() == 0)
check("Hodge midpoint dimension closes", int((v14.exterior_power(7) * sp).degree()) == 64 * comb(14, 7))

d5 = WeylCharacterRing("D5", style="coroots")
v10 = d5(1, 0, 0, 0, 0)
fp = d5(0, 0, 0, 0, 1)
fm = d5(0, 0, 0, 1, 0)
tp = d5(1, 0, 0, 0, 1)
tm = d5(1, 0, 0, 1, 0)
check("PS: 10 x 16+ = 16- + 144+", v10 * fp == fm + tp)
check("PS: 10 x 16- = 16+ + 144-", v10 * fm == fp + tm)
check("PS: Sym2(16+) = 10 + 126+",
      fp.symmetric_square() == v10 + d5(0, 0, 0, 0, 2))
check("PS: wedge2(16+) = 120", fp.exterior_square() == d5(0, 0, 1, 0, 0))
check("PS: wedge5(10) = 126+ + 126-",
      v10.exterior_power(5) == d5(0, 0, 0, 0, 2) + d5(0, 0, 0, 2, 0))

print("M-M4 verdict: exact cached D7/D5 branching dictionary reproduced")
print("checks passed:", CHECKS)
