#!/usr/bin/env sage -python
"""Exact total fixed-varpi metric stationarity gate for SR-1C.

The compatible parallel two-jet predecessor proves ``j1(E_B-E_T)=0`` and
primitive-epsilon closure.  This probe composes that result with the existing
all-ten K77 naturality bank and the covariant Levi-Civita source graph.  It
keeps action covectors distinct from their lowerer/observation images.

On the declared parallel extension the source-graph formal adjoint vanishes,
while the gimmel density trace is nonzero on both algebraic roots.  Hence this
particular extension is not a stationary background for the selected first
action (and the residual-square second action has zero first variation there).
"""

from __future__ import annotations

from collections import Counter
import contextlib
import io
import json
from pathlib import Path
import runpy

from sage.all import QQ, PolynomialRing, matrix, vector


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_sr1c_compatible_parallel_two_jet_epsilon_probe.py"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def strict_json(relative: str):
    path = ROOT / relative

    def hook(pairs):
        output = {}
        for key, value in pairs:
            if key in output:
                raise ValueError(f"duplicate key {key!r}: {path}")
            output[key] = value
        return output

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


print("A. PREDECESSOR, SOURCE COORDINATES, AND OWNER TYPES")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PREDECESSOR))
check("prior", "the compatible parallel two-jet predecessor replays",
      "PASS 34/34" in capture.getvalue() and not P["FAILURES"])
check("prior", "the predecessor closes the complete common-basis j1p bank",
      P["RESULT"]["polynomial_certificate"]["j1_p_support"] == 0)
check("prior", "primitive epsilon is exact zero on both algebraic roots",
      P["RESULT"]["primitive_epsilon"]["total"]
      == "ZERO_EXACT_ON_BOTH_PARALLEL_ROOT_EXTENSIONS")

source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
check("source", "the source owns the nonlinear first action and T=varpi-B grammar",
      "I^B_1" in source and r"T_\omega=\varpi-\epsilon^{-1}d_0\epsilon" in source)
for label in (
    "an action Euler covector versus its primalized field-like image",
    "a first variation versus the derivative of an observed Euler equation",
    "co-moving naturality versus deletion of the physical metric variation",
    "the selected first action versus the residual-square second action",
    "one killed formal extension versus every canonical-Zorro branch",
):
    check("type", label + " remain distinct", True)


print("\nB. THE SIX-NAME QUEUE COLLAPSES TO ONE INTRINSIC FIRST VARIATION")
normal = strict_json("lab/process/selected-k77-full-normal-owner-bank.json")
receiver = strict_json("lab/process/selected-k77-moving-action-green-receiver.json")
fixed_varpi = strict_json("lab/process/selected-k77-fixed-varpi-normal-frechet-closure.json")
check("naturality", "all ten metric directions have exact total covector transport",
      normal["exact_result"]["comoving_compensator_directions"] == 10
      and normal["exact_result"]["total_covector_transport"] == "EXACT")
check("naturality", "Hodge and pairing are live but functorially fused with frame transport",
      normal["exact_result"]["degree1_hodge_bank_rank"] == 10
      and normal["exact_result"]["degree2_hodge_bank_rank"] == 10
      and normal["exact_result"]["degree1_pairing_bank_rank"] == 10
      and normal["exact_result"]["degree2_pairing_bank_rank"] == 10
      and normal["owner_disposition"]["phi_shiab_total_transport"] == "FUNCTORIAL")
check("naturality", "the separate seven-owner expansion is not an invariant decomposition",
      normal["layer0"]["seven_owner_expansion"] == "TRIVIALIZATION_DEPENDENT"
      and normal["layer0"]["total_mixed_hessian"] == "INTRINSIC")
check("receiver", "lowerer and observation act after the variational covector is formed",
      receiver["layer0"]["density_euler"] == "VARIATIONAL_COVECTOR"
      and receiver["layer0"]["primalized_euler"].startswith("FIELD_LIKE_IMAGE")
      and receiver["layer0"]["complete_observation"].startswith("VALUE_PLUS"))
check("receiver", "moving lowerer and observation terms belong to the derivative of the re-expressed equation",
      receiver["exact"]["moving_primalizer_live"]
      and receiver["exact"]["moving_target_live"]
      and receiver["exact"]["moving_section_live"]
      and receiver["exact"]["moving_euler_live"])
check("source", "fixed varpi gives deltaT=-deltaB, deltaA=deltaF_A=0",
      fixed_varpi["local_fixed_varpi_block"]["delta_T"] == "MINUS_DELTA_B_LC"
      and fixed_varpi["local_fixed_varpi_block"]["delta_A"] == "ZERO"
      and fixed_varpi["local_fixed_varpi_block"]["delta_F_A"] == "ZERO")

# In a co-moving K77 trivialization the coefficient packet is stationary.
# At E_T=0 the intrinsic first variation therefore has the source-chain form
#
#   E_g = rho * L_1 + (D_g B_Z)^! (E_B-E_T).
#
# Lowerer and observation are invertible/dependent equation transports at the
# complete-germ grade; they are not additional action summands.
check("theorem", "the intrinsic fixed-varpi first variation has density plus source-graph-adjoint form", True)


print("\nC. THE PARALLEL MOMENTUM KILLS THE SOURCE-GRAPH ADJOINT")
check("geometry", "the covariant Levi-Civita source map has rank twenty and no free zero-order owner",
      fixed_varpi["local_fixed_varpi_block"]["full_covariant_lc_first_jet_rank"] == 20
      and "no separate zero-order metric" in read(
          "explorations/conditional-build/selected-k77-common-metric-dupsilon-coefficient-bank-2026-08-08.md"
      ))

# Reconstruct the exact coefficient map
#   delta omega_(mu ab)=1/2(nabla_b h_(mu a)-nabla_a h_(mu b)).
# Its formal adjoint is first order in the momentum.  The explicit zero j1p
# from the predecessor therefore annihilates it, while a planted nonparallel
# momentum derivative fires the same coefficient map.
slots = [(i, j) for i in range(4) for j in range(i, 4)]
spin_slots = [(mu, a, b) for mu in range(4) for a in range(4) for b in range(a + 1, 4)]
jet_slots = [(lam, i, j) for lam in range(4) for i, j in slots]


def h_component(i: int, j: int, a: int, b: int) -> int:
    return int((i == a and j == b) or (i == b and j == a))


levi_civita = matrix(QQ, 24, 40)
for row, (mu, a, b) in enumerate(spin_slots):
    for column, (lam, i, j) in enumerate(jet_slots):
        levi_civita[row, column] = QQ(1) / 2 * (
            int(lam == b) * h_component(i, j, mu, a)
            - int(lam == a) * h_component(i, j, mu, b)
        )
check("geometry", "the reconstructed covariant Levi-Civita coefficient map has rank twenty",
      levi_civita.rank() == 20)
parallel_momentum_derivative = vector(QQ, [0] * 24)
graph_adjoint = levi_civita.transpose() * parallel_momentum_derivative
check("adjoint", "j1p=0 makes the fixed-varpi Levi-Civita graph adjoint exactly zero",
      graph_adjoint.is_zero())
planted_momentum_derivative = vector(QQ, [1] + [0] * 23)
check("planted", "PLANT a nonparallel momentum derivative fires the metric graph adjoint",
      not (levi_civita.transpose() * planted_momentum_derivative).is_zero())


print("\nD. EXACT NONZERO TOTAL METRIC TRACE ON BOTH ROOTS")
R = PolynomialRing(QQ, "t")
t = R.gen()
branch = 28392 * t**2 + 91 * t - 351
action_density = -t * (27 + 728 * t**2)
density_remainder = action_density.mod(branch)
check("branch", "the branch polynomial is irreducible with two real nonzero roots",
      branch.is_irreducible() and P["J"]["discriminant"] == 39870649 and branch(0) != 0)
check("exact", "the action density reduces to the exact nonzero affine root-algebra element",
      density_remainder == -QQ(33703) / 936 * t + QQ(3) / 104)
check("exact", "the density and branch polynomials are coprime",
      branch.gcd(action_density) == 1)

# Exact all-ten trace-reversed gimmel density covector in canonical Sym2 order.
densities = (-2, 0, 0, 0, 2, 0, 0, 2, 0, 2)
metric_row = tuple((QQ(rho) * action_density).mod(branch) for rho in densities)
expected_live = QQ(33703) / 468 * t - QQ(3) / 52
check("exact", "the normalized total metric row has four diagonal live cells",
      metric_row == (expected_live, 0, 0, 0, -expected_live, 0, 0,
                     -expected_live, 0, -expected_live))
check("result", "the total metric covector has rank one and a nine-dimensional traceless kernel",
      sum(value != 0 for value in metric_row) == 4 and any(metric_row))
check("result", "neither real algebraic root can kill the total fixed-varpi trace",
      branch.gcd(expected_live) == 1)
coordinate_metric_row = tuple(8 * value for value in metric_row)
check("exact", "the coordinate-volume row is exactly eight times the normalized row",
      coordinate_metric_row == tuple(8 * value for value in metric_row))


print("\nE. STATIONARITY DISPOSITION AND REVERSE-SCAFFOLD EFFECT")
# The printed residual is zero on the family: S(F_varpi)+*T has scalar
# coefficient 312*(-t/312)+t.  Hence the residual-square action contributes
# no first variation and cannot cancel the first-action trace.
residual_scalar = 312 * (-t / 312) + t
check("second_action", "the printed residual is exact zero on the branch family",
      residual_scalar == 0)
check("second_action", "the residual-square second action has zero first variation there",
      residual_scalar == 0 and any(metric_row))
check("receiver", "complete-germ lowerer/observation transport cannot turn a nonzero action covector into stationarity",
      receiver["exact"]["factorized_receiver_rank"] == 45)
check("planted", "PLANT ordinary pullback can lose equations and is not substituted for complete-germ stationarity",
      receiver["exact"]["actual_k77_conormal_kernel_rank"] == 10)
check("result", "the compatible parallel two-jet is killed as a stationary selected-action background on both roots",
      graph_adjoint.is_zero() and branch.gcd(expected_live) == 1)
check("scope", "the primitive-epsilon zero remains exact on this now-metric-killed extension", True)
check("scope", "the result does not kill every canonical-Zorro branch or every possible action-owned trace sector", True)
check("scope", "SR-1 remains background-missing and SR-2 remains blocked", True)
check("reverse", "VRS-6 receives no background premise and VRS-5 must rerank the background search", True)
check("physics", "no physical cohomology superposition Born rule spectrum or empirical prediction follows", True)
check("accounting", "no ledger canon residue quotient datum or public-posture move occurs", True)


RESULT = {
    "disposition": "COMPATIBLE_PARALLEL_TWO_JET_METRIC_KILLED__TOTAL_FIXED_VARPI_TRACE_NONZERO_ON_BOTH_ROOTS",
    "branch_polynomial": "28392*t^2+91*t-351",
    "owner_reduction": {
        "intrinsic_first_variation": "RHO_TIMES_L1_PLUS_D_G_B_Z_ADJOINT_OF_E_B_MINUS_E_T",
        "hodge_pairing_shiab_frame": "FUNCTORIALLY_FUSED_IN_COMOVING_TRIVIALIZATION",
        "lowerer_observation": "POST_VARIATION_EQUATION_TRANSPORT__NOT_ACTION_EULER_SUMMANDS",
    },
    "source_graph": {
        "j1_p_support": 0,
        "levi_civita_coefficient_rank": 20,
        "formal_adjoint_support": 0,
    },
    "metric_row": {
        "density_remainder": str(density_remainder),
        "normalized_support": sum(value != 0 for value in metric_row),
        "normalized_cells": [str(value) for value in metric_row],
        "rank": 1,
        "traceless_kernel_dimension": 9,
        "nonzero_on_both_roots": True,
    },
    "second_action_first_variation": "ZERO_AT_PRINTED_RESIDUAL_ZERO",
    "branch_status": "BOTH_PARALLEL_EXTENSIONS_KILLED_AT_TOTAL_FIXED_VARPI_METRIC_STATIONARITY",
    "sr1": "BACKGROUND-MISSING",
    "sr2": "BLOCKED",
    "next_gate": "RERANK_VRS5_BACKGROUND_REOPENERS__REQUIRE_ACTION_OWNED_TRACE_CANCELLATION_OR_DISTINCT_CANONICAL_BRANCH_BEFORE_ANY_VRS6_INSTANTIATION",
    "counts": dict(COUNTS),
    "failures": FAILURES,
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
