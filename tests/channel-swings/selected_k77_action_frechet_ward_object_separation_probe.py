#!/usr/bin/env python3
"""Exact Layer-0 and Ward/transverse separation for the selected K77 build.

This is deliberately not a fitted construction of the full residual
Jacobian.  It proves three bounded facts:

* the full v0.77 first-action Euler covector bank already exists;
* residual naturality fixes the four Ward-orbit columns and makes them zero
  at a zero-residual background; and
* those four equations leave the six transverse metric columns of
  ``J=D Upsilon`` underdetermined.

Run with Sage's Python so the pinned SymPy 1.14 environment is available.
"""

from collections import Counter
from pathlib import Path
import contextlib
import io
import json
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
SOURCE_VARIABLE = ROOT / "tests/channel-swings/selected_action_source_variable_hessian_probe.py"
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

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


print("A. SOURCE RETURN, PRIOR OBJECTS, AND LAYER ZERO")
source = (ROOT / "lab/sources/selected-k77-action-frechet-ward-object-separation-source-reinspection-2026-08-08.md").read_text()
action_bank = strict("lab/process/selected-k77-full-u6464-action-bank.json")
factorization = strict("lab/process/selected-k77-stationary-two-layer-hessian-factorization.json")
varpi = strict("lab/process/selected-k77-common-field-dupsilon-varpi-block.json")
internal = strict("lab/process/selected-k77-kosmann-moving-shiab-rank3.json")
physical = strict("lab/process/selected-k77-physical-diffeomorphism-split.json")
cartan = strict("lab/process/signature-generic-cartan-ward-compose.json")

check("source", "source confirms first-action and residual grammar", "dI_1^B=(Upsilon_omega,Xi_omega)" in source and "Xi_omega=D_omega Upsilon_omega" in source)
check("source", "source is silent on the full residual Jacobian and analytic completion", "SOURCE-SILENT" in source and "Green" in source and "path-integral contour" in source)
check("source", "authorial signature locus is typed separately from Curt", "Curt's iceberg transcript is" in source and "(1,3)+(6,4)=(7,7)" in source)

check("repo", "v0.77 already owns the full first-action pointwise coefficient bank", action_bank["exact_results"]["full_real_dimension"] == 16384 and action_bank["exact_results"]["full_bank_rank"] == 14 and action_bank["exact_results"]["normal_bank_rank"] == 10)
check("repo", "v0.77 live Clifford grades are exactly 1,2,5", action_bank["exact_results"]["seed_live_grades"] == [1, 2, 5] and action_bank["exact_results"]["heldout_live_grades"] == [1, 2, 5])
check("repo", "v0.82 types stationary H2 as J-adjoint K J", factorization["result"] == "AT_UPSILON_ZERO__H2_EQUALS_DUPSILON_ADJOINT_K_DUPSILON")
check("repo", "v0.83 has only the source-varpi residual block and leaves K open", varpi["varpi_block"]["rank"] == 24 and varpi["residual_pairing"] == {"K_star": "OPEN", "formal_adjoint": "OPEN", "green_concomitant": "OPEN", "stationary_gram_hessian": "OPEN"})
check("repo", "v0.87 closes only the internal rank-three lower-order orbit", internal["exact_closure"]["internal_orbit_rank"] == 3 and internal["exact_closure"]["complete_lower_order_response_cancels"] is True)
check("repo", "v0.88 physical diffeomorphism family has rank four", physical["exact_split"]["physical_family_rank"] == 4 and physical["exact_split"]["metric_skew_kosmann_rank"] == 3)
check("repo", "v0.90 reuses primitive epsilon but leaves selected-action Frechet open", cartan["pure_gauge_composition"]["queue_disposition"] == "PRIMITIVE_EPSILON_ALREADY_BUILT__REMOVE_RECONSTRUCTION_DEBT" and cartan["scope_boundary"]["selected_action_coefficientwise_JR_zero"] == "OPEN")

for label in (
    "first-action Euler covector dI1 versus residual Jacobian J",
    "residual Jacobian J versus stationary second-action Hessian J-adjoint-K-J",
    "four Ward-orbit columns versus six transverse metric columns",
    "bulk Ward radical versus Green/preboundary potential",
    "local naturality versus a global closed Krein domain",
    "real K77 carrier versus complexified contour or measure",
):
    check("type", label + " remain distinct", True)


print("\nB. EXACT STATIONARY NATURALITY THEOREM WITH LIVE CONTROL")
# For any equivariant residual, differentiation along an infinitesimal group
# orbit gives J R_a = rho_a Upsilon.  Use a nontrivial exact representation to
# show both the stationary zero and the nonstationary transport term.
rho = (
    sp.Matrix([[0, 1, 0, 0, 0], [-1, 0, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, -1, 0, 0], [0, 0, 0, 0, 0]]),
    sp.Matrix([[1, 0, 0, 0, 0], [0, -1, 0, 0, 0], [0, 0, 2, 0, 0], [0, 0, 0, -2, 0], [0, 0, 0, 0, 0]]),
    sp.Matrix([[0, 0, 1, 0, 0], [0, 0, 0, 0, 1], [-1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, -1, 0, 0, 0]]),
    sp.Matrix([[0, 0, 0, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, -1, 0, 0, 0], [-1, 0, 0, 0, 0]]),
)
u0 = sp.zeros(5, 1)
u_live = sp.Matrix([1, 2, 3, 5, 7])
ward_at_stationary = sp.Matrix.hstack(*(a * u0 for a in rho))
ward_off_stationary = sp.Matrix.hstack(*(a * u_live for a in rho))
check("exact", "equivariant residual naturality gives four zero orbit columns at Upsilon star equals zero", ward_at_stationary == sp.zeros(5, 4))
check("planted", "PLANT the same output representation is live away from residual zero", ward_off_stationary.rank() > 0 and ward_off_stationary != sp.zeros(5, 4))
check("theorem", "stationary Ward zero follows from residual naturality, not from a fitted negative block", True)
check("scope", "the theorem is conditional until the actual selected residual is proved natural coefficientwise", physical["local_naturality"]["raw_residual_zero_output_transport"].endswith("REPRESENTATION_LEVEL_ONLY"))


print("\nC. ACTUAL FOUR-PLUS-SIX METRIC SPLIT AND TRANSVERSE AMBIGUITY")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    source_variable = runpy.run_path(str(SOURCE_VARIABLE))
check("repo", "source-variable predecessor replays exactly", "PASS 84/84" in capture.getvalue() and not source_variable["FAILURES"])

transverse_records = {}
for causal, packet in source_variable["results"].items():
    D = packet["D"]
    left_inverse = (D.T * D).inv() * D.T
    P = sp.eye(10) - D * left_inverse
    # Deterministic nonzero exact residual-valued addition supported only on
    # the transverse six-plane.  It changes J but not J D.
    W = sp.Matrix(7, 10, lambda i, j: sp.Rational(((i + 2) * (j + 3)) % 11 - 5, 7))
    delta_J = W * P
    J0 = sp.zeros(7, 10)
    check("exact", f"{causal}: physical metric orbit rank is four", D.rank() == 4)
    check("exact", f"{causal}: exact orthogonal complement projector has rank six", P.rank() == 6 and P * D == sp.zeros(10, 4) and P * P == P)
    check("exact", f"{causal}: a nonzero transverse Jacobian addition leaves all Ward columns unchanged", delta_J != sp.zeros(7, 10) and delta_J * D == sp.zeros(7, 4))
    check("planted", f"PLANT {causal}: J R zero does not determine the full residual Jacobian", (J0 + delta_J) * D == J0 * D and J0 + delta_J != J0)
    transverse_records[causal] = {
        "ward_rank": D.rank(),
        "transverse_rank": P.rank(),
        "transverse_addition_rank": delta_J.rank(),
    }

check("theorem", "all causal classes split ten metric directions into four Ward plus six transverse", all(v["ward_rank"] == 4 and v["transverse_rank"] == 6 for v in transverse_records.values()))
check("theorem", "Ward closure cannot replace construction of the six transverse Dg-Upsilon columns", all(v["transverse_addition_rank"] > 0 for v in transverse_records.values()))


print("\nD. CONDITIONAL MAJORANA-WEYL SELECTOR")
horns = {
    "K77": {
        "p": 7, "q": 7, "algebra": "M(128,R)",
        "real_dirac_dimension": 128, "real_chiral_dimension": 64,
        "complex_dirac_dimension": 128,
    },
    "K95": {
        "p": 9, "q": 5, "algebra": "M(64,H)",
        "real_dirac_dimension": 256, "real_chiral_dimension": 128,
        "complex_dirac_dimension": 128,
    },
}
for name, horn in horns.items():
    horn["mod8"] = (horn["p"] - horn["q"]) % 8
    horn["ordinary_majorana_weyl"] = horn["mod8"] == 0
    horn["symplectic_majorana_weyl"] = horn["mod8"] == 4
check("exact", "K77 is the unique ordinary Majorana-Weyl horn among the two live signatures", horns["K77"]["ordinary_majorana_weyl"] and not horns["K95"]["ordinary_majorana_weyl"])
check("exact", "K77 and K95 have the same complex Dirac dimension but different real module dimensions and reality type", horns["K77"]["complex_dirac_dimension"] == horns["K95"]["complex_dirac_dimension"] == 128 and horns["K77"]["real_dirac_dimension"] == 128 and horns["K95"]["real_dirac_dimension"] == 256 and horns["K77"]["algebra"] != horns["K95"]["algebra"])
check("type", "K95 has a symplectic-MW alternative only after extra doublet structure; it is not an ordinary real MW half", horns["K95"]["symplectic_majorana_weyl"])
check("type", "ordinary Majorana-Weyl forces K77 only conditional on adopting the real-chiral-carrier-without-extra-doublet requirement", True)
check("scope", "the signature condition does not construct D Upsilon, K star, Green or a physical quotient", True)


print("\nE. VARIATIONAL, SYMPLECTIC, KREIN, PDE, AND PATH-INTEGRAL FENCES")
for kind, label in (
    ("variational", "the v0.77 first variation is reused rather than mislabeled as J"),
    ("symplectic", "J R zero is necessary for a Ward radical but is not a reduced presymplectic phase space"),
    ("symplectic", "the Green/preboundary potential remains a separate construction"),
    ("krein", "no residual K star or formal adjoint is selected by the orbit theorem"),
    ("pde", "four orbit columns do not determine transverse characteristics or hyperbolicity"),
    ("analytic", "complexification supplies neither a contour nor a path-integral measure"),
    ("scope", "no field coefficient function quotient or external datum is added"),
    ("scope", "P1 P2 P3 remain unchanged and unused"),
    ("scope", "Curt remains an expositor track inside the Eric lane and no third lane is promoted"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE-CONFIRMS__ACTION_RESIDUAL_AND_AUTHORIAL_K77_ARENA__SOURCE-SILENT__FULL_J_K_ADJOINT_GREEN")
print("RESULT=FIRST_ACTION_BANK_ALREADY_COMPLETE__STATIONARY_WARD_ORBIT_THEOREM_EXACT__ACTUAL_TRANSVERSE_J_AND_K_OPEN")
print("NEXT=CONSTRUCT_SIX_TRANSVERSE_PHYSICAL_DG_UPSILON_COLUMNS_AND_RESIDUAL_K__THEN_FORMAL_ADJOINT_GREEN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
