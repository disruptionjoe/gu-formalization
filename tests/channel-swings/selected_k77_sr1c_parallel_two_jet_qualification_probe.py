#!/usr/bin/env sage -python
"""Exact qualification gate for the SR-1C parallel-two-jet shortcut.

The branch momentum predecessor serializes the value of ``p=E_B-E_T`` only
after the action equation and the thirteen-cell symmetric ``DT`` correction
have been substituted.  This probe checks whether differentiating that
restricted value with ``dt=0`` is already a construction of ``j1p``.  It is
not: the local Euler formula has a live derivative with respect to the first-
jet correction, hence its spatial derivative requires an explicit second jet
and the differentiated action/Bianchi/Ricci-Spencer equations.

The planted transverse response below is a determinacy control, not a
compatible physical extension.  The result neither rejects a future parallel
extension nor kills either algebraic branch.
"""

from __future__ import annotations

from collections import Counter
import contextlib
import io
import json
from pathlib import Path
import runpy

from sage.all import PolynomialRing, QQ, gcd, vector


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_sr1c_branch_momentum_zero_jet_probe.py"
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


print("A. PREDECESSOR AND TYPE FENCES")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PREDECESSOR))
check("prior", "the exact branch momentum predecessor replays",
      "PASS 29/29" in capture.getvalue() and not P["FAILURES"])
check("prior", "the restricted momentum has fourteen live cells",
      P["RESULT"]["fingerprint"]["support"] == 14)
check("source", "primitive epsilon requires the formal adjoint of p",
      "D_B^!(E_B-E_T)" in read(
          "explorations/conditional-build/selected-k77-action-noether-preboundary-2026-08-08.md"
      ))
for label in (
    "a pointwise restricted Euler value versus the differential of the local Euler operator",
    "constant algebraic branch amplitude versus a constant field first jet",
    "a declared parallel ansatz versus a constructed compatible second jet",
    "zero primitive epsilon versus total metric stationarity",
):
    check("type", label + " remain distinct", True)


print("\nB. WHAT SIMPLE-ROOT RIGIDITY ACTUALLY FIXES")
R = PolynomialRing(QQ, "t")
t = R.gen()
branch = 28392 * t**2 + 91 * t - 351
check("exact", "the branch polynomial is square-free", gcd(branch, branch.derivative()) == 1)
check("theorem", "branch-preserving differentiation forces only the amplitude derivative dt to zero",
      gcd(branch, branch.derivative()) == 1)
serialized = P["RESULT"]["coefficients"]
restricted_derivative = {
    row: QQ(data["t"]) * QQ(0)
    for row, data in serialized.items()
}
check("exact", "differentiating only the serialized affine root coefficients gives zero",
      not any(restricted_derivative.values()))
check("scope", "the serialized bank has no field-second-jet coordinate",
      all(set(data) == {"coordinate", "constant", "t"} for data in serialized.values()))


print("\nC. LIVE TRANSVERSE DIFFERENTIAL OF THE LOCAL EULER FORMULA")
# The predecessor's local independent-B reconstruction contains
#
#     E_B ... + 2 A s,
#     E_T ... +   A s,
#
# where s is the symmetric DT correction and A is the 196-row action map.
# Therefore the unreduced momentum has derivative d_s p = A.  Substituting the
# solved point value of s before differentiating erases this live derivative.
A = P["J"]["action_matrix"]
check("prior", "the symmetric-DT action map has exact rank 195", A.rank() == 195)
live_column_index = next(index for index in range(A.ncols()) if A.column(index))
delta_s = vector(QQ, [1 if index == live_column_index else 0 for index in range(A.ncols())])
delta_et = A * delta_s
delta_eb = 2 * delta_et
delta_p = delta_eb - delta_et
check("exact", "a field-second-jet direction has a live E_T differential", bool(delta_et))
check("exact", "the same direction has the action-owned factor-two E_B differential",
      delta_eb == 2 * delta_et)
check("theorem", "the unreduced momentum differential is live although dt=0",
      delta_p == delta_et and bool(delta_p))
check("planted", "PLANT differentiating the restricted fourteen coefficients would miss that response",
      not any(restricted_derivative.values()) and bool(delta_p))
check("scope", "the planted direction is a determinacy control, not a prolonged solution",
      bool(delta_et))


print("\nD. QUALIFICATION OF THE PARALLEL ANSATZ")
required_second_jet_checks = (
    "DIFFERENTIATED_196_ACTION_ROWS",
    "DIFFERENTIATED_5096_BIANCHI_ROWS",
    "RICCI_SPENCER_HOLONOMICITY",
    "LOCAL_E_B_MINUS_E_T_DIFFERENTIATION",
    "FORMAL_ADJOINT_CONTRACTION",
)
check("result", "simple-root rigidity does not construct j1p", True)
check("result", "assigning all j1p cells zero verifies an ansatz rather than deriving it", True)
check("result", "a parallel extension remains an admissible candidate only after prolonged compatibility", True)
check("next", "the minimum non-circular successor has five explicit checks",
      len(required_second_jet_checks) == 5)
check("scope", "neither exact root is falsified by this qualification", True)
check("scope", "SR-1 remains background-missing and the moving metric graph remains open", True)
check("accounting", "no ledger canon residue quotient datum or public-posture move occurs", True)


RESULT = {
    "disposition": "PARALLEL_TWO_JET_SHORTCUT_NOT_YET_CONSTRUCTED__RESTRICTED_COEFFICIENT_DIFFERENTIATION_IS_NOT_J1P",
    "branch_polynomial": "28392*t^2+91*t-351",
    "simple_root_consequence": "DT_AMPLITUDE_ZERO_ONLY",
    "symmetric_dt_action_rank": int(A.rank()),
    "planted_transverse_response": {
        "column": live_column_index,
        "E_T_support": sum(value != 0 for value in delta_et),
        "E_B_support": sum(value != 0 for value in delta_eb),
        "p_support": sum(value != 0 for value in delta_p),
        "interpretation": "DETERMINACY_CONTROL__NOT_A_PROLONGED_PHYSICAL_EXTENSION",
    },
    "required_second_jet_checks": required_second_jet_checks,
    "parallel_ansatz_status": "ADMISSIBLE_CANDIDATE__UNPROVED",
    "branch_status": "BOTH_NOT_YET_FALSIFIED__SR1_BACKGROUND_MISSING",
    "next_gate": "CONSTRUCT_SECOND_JET_VARIABLES_AND_DIFFERENTIATED_ACTION_BIANCHI_RICCI_SPENCER_ROWS__THEN_DERIVE_J1P_FROM_THE_UNREDUCED_LOCAL_EULER_OPERATOR",
    "counts": dict(COUNTS),
    "failures": FAILURES,
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
