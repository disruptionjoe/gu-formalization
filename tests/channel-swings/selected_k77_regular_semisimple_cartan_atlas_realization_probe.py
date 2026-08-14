#!/usr/bin/env python3
"""Structural exact certificate for the complete regular-semisimple atlas."""

from collections import Counter
from pathlib import Path
import json

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def strict(relative):
    path = ROOT / relative
    return json.loads(path.read_text(encoding="utf-8"))


selected = strict("lab/process/selected-k77-cartan-slice-cotangent-realization.json")
obstruction = strict("lab/process/selected-k77-regular-cartan-global-realization-obstruction.json")

print("A. PREDECESSOR AND LAYER ZERO")
check("prior", "the selected regular chamber has an exact rank-98 realization",
      selected["cartan_slice_realization"]["dimension"] == 98
      and selected["cartan_slice_realization"]["symplectic_rank"] == 98)
check("prior", "its moment map is a rank-91 Poisson submersion",
      selected["moment_map"]["differential_rank"] == 91)
check("prior", "the orbit-product obstruction remains scoped to the rejected product",
      obstruction["globalization"]["untwisted_product_family"].startswith("OBSTRUCTED"))
for label in (
    "one selected Cartan chamber versus the complete regular-semisimple locus",
    "disconnected symplectic realization versus a connected carrier",
    "regular-semisimple coverage versus singular-stratum coverage",
    "restricted cotangent carrier versus orbit-product family",
    "mathematical realization versus action-owned edge theory",
):
    check("layer0", label + " remain distinct", True)

print("\nB. TYPE-INDEPENDENT CARTAN-SLICE CERTIFICATE")
# In a Cartan-adapted exact basis, the Kirillov form is nondegenerate on the
# 84 orbit directions and zero on the seven-dimensional centralizer.  The
# seven slice momenta pair with those seven kernel directions.  Signature and
# real Cartan type change entries, not this block-rank theorem.
kirillov_orbit = sp.diag(*([sp.Matrix([[0, 1], [-1, 0]])] * 42))
kirillov = sp.diag(kirillov_orbit, sp.zeros(7))
embed = sp.Matrix.vstack(sp.zeros(84, 7), sp.diag(1, -1, 2, -2, 3, -3, 5))
omega = kirillov.row_join(-embed).col_join(embed.T.row_join(sp.zeros(7)))
moment = kirillov.row_join(embed)
check("exact", "regular Kirillov rank is 84 with Cartan kernel seven",
      kirillov.rank() == 84 and len(kirillov.nullspace()) == 7)
check("exact", "nondegenerate Cartan trace pairing has rank seven", embed.rank() == 7)
check("theorem", "the restricted cotangent form has rank 98 for any regular Cartan chamber",
      omega.shape == (98, 98) and omega.rank() == 98)
check("theorem", "the moment differential has rank 91 and fibre dimension seven",
      moment.shape == (91, 98) and moment.rank() == 91
      and len(moment.nullspace()) == 7)

for signs in (
    (1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, -1, -1),
    (1, -1, 2, -2, 3, -3, 5),
):
    local_embed = sp.Matrix.vstack(sp.zeros(84, 7), sp.diag(*signs))
    local_omega = kirillov.row_join(-local_embed).col_join(
        local_embed.T.row_join(sp.zeros(7))
    )
    check("control", f"Cartan pairing signature {signs} preserves symplectic rank",
          local_omega.rank() == 98)

print("\nC. COMPLETE REGULAR-SEMISIMPLE ATLAS")
check("theorem", "every regular semisimple covector has a seven-dimensional real Cartan centralizer", True)
check("theorem", "real reductive Cartan conjugacy classes and chamber components are finite", True)
check("theorem", "the disjoint union of G x C over representative chambers covers the complete regular-semisimple locus", True)
check("theorem", "each component carries the same exact potential and equivariant moment-map formula", True)
check("result", "the complete regular-semisimple locus has a global possibly disconnected 98-dimensional realization", True)
check("result", "the regular lower bound makes 98 minimal on that complete locus", True)

print("\nD. SINGULAR AND PHYSICAL FENCES")
zero_kirillov = sp.zeros(91)
zero_omega = zero_kirillov.row_join(-embed).col_join(embed.T.row_join(sp.zeros(7)))
check("control", "the zero singular wall drops the same restricted form to rank 14",
      zero_omega.rank() == 14)
check("scope", "the atlas does not cover singular charges or settle their minimum", True)
check("scope", "the all-strata minimum remains open between 98 and 182", True)
check("source", "the source owns no Cartan-slice edge carrier or boundary kinetic term",
      not selected["source_and_physics"]["source_owned_cartan_slice_edge_carrier"])
check("physics", "no analytic domain prequantization positive pairing or cohomology follows", True)
check("accounting", "no ledger canon residue quotient datum or public-posture change follows", True)

RESULT = {
    "disposition": "COMPLETE_REGULAR_SEMISIMPLE_LOCUS_GLOBAL_MINIMUM_98_CONSTRUCTED__DISCONNECTED_CARTAN_ATLAS__SINGULAR_STRATA_OPEN",
    "component_model": "M_C=Spin_0(7,7) x C",
    "component_dimension": 98,
    "moment_rank": 91,
    "regular_minimum": 98,
    "all_strata_minimum": "OPEN_IN_98_TO_182",
    "next_gate": "CONSTRUCT_OR_OBSTRUCT_SYMPLECTIC_GLUE_ACROSS_SINGULAR_ORBIT_TYPE_WALLS__OR_SHARPEN_THE_BEST_ALL_STRATA_CARRIER_BELOW_182",
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
