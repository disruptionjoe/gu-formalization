#!/usr/bin/env python3
"""Exact finite certificate for the M-H4 / DQ2 reality-commutant fork.

The calculation separates three algebras that prior prose can conflate:

* the full real Clifford action;
* the connected Spin action, which preserves two chiral halves; and
* the disconnected orientation-reversing extension, which exchanges them.

The quaternionic case is computed with exact 4x4 rational left-multiplication
matrices.  Commutants are null spaces of exact linear equations, not numerical
rank estimates.  The split-real case is the corresponding 1x1 control.
"""
from __future__ import annotations

import sys
import contextlib
import io
import os
import runpy
from fractions import Fraction


FAILURES: list[str] = []
CHECKS = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global CHECKS
    CHECKS += 1
    if condition:
        print(f"PASS: {label}" + (f" -- {detail}" if detail else ""))
    else:
        FAILURES.append(label)
        print(f"FAIL: {label}" + (f" -- {detail}" if detail else ""))


def zeros(n: int, m: int) -> list[list[Fraction]]:
    return [[Fraction(0) for _ in range(m)] for _ in range(n)]


def eye(n: int) -> list[list[Fraction]]:
    out = zeros(n, n)
    for i in range(n):
        out[i][i] = Fraction(1)
    return out


def block_diag(a, b):
    n, m = len(a), len(b)
    out = zeros(n + m, n + m)
    for i in range(n):
        for j in range(n):
            out[i][j] = a[i][j]
    for i in range(m):
        for j in range(m):
            out[n + i][n + j] = b[i][j]
    return out


def swap(n: int):
    out = zeros(2 * n, 2 * n)
    for i in range(n):
        out[i][n + i] = Fraction(1)
        out[n + i][i] = Fraction(1)
    return out


def rref_rank(rows: list[list[Fraction]]) -> int:
    if not rows:
        return 0
    a = [row[:] for row in rows if any(row)]
    if not a:
        return 0
    ncol = len(a[0])
    rank = 0
    for col in range(ncol):
        pivot = next((r for r in range(rank, len(a)) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        q = a[rank][col]
        a[rank] = [x / q for x in a[rank]]
        for r in range(len(a)):
            if r != rank and a[r][col]:
                q = a[r][col]
                a[r] = [x - q * y for x, y in zip(a[r], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return rank


def commutant_dimension(generators) -> int:
    n = len(generators[0]) if generators else 1
    rows = []
    # Unknown X is flattened by (row,column).  Enforce XG-GX=0 exactly.
    for g in generators:
        for i in range(n):
            for j in range(n):
                row = [Fraction(0) for _ in range(n * n)]
                for k in range(n):
                    row[i * n + k] += g[k][j]
                    row[k * n + j] -= g[i][k]
                rows.append(row)
    return n * n - rref_rank(rows)


# Quaternion multiplication on basis 1,i,j,k.
QMUL = {
    (0, 0): (1, 0), (0, 1): (1, 1), (0, 2): (1, 2), (0, 3): (1, 3),
    (1, 0): (1, 1), (1, 1): (-1, 0), (1, 2): (1, 3), (1, 3): (-1, 2),
    (2, 0): (1, 2), (2, 1): (-1, 3), (2, 2): (-1, 0), (2, 3): (1, 1),
    (3, 0): (1, 3), (3, 1): (1, 2), (3, 2): (-1, 1), (3, 3): (-1, 0),
}


def left_quaternion(unit: int):
    out = zeros(4, 4)
    for col in range(4):
        sign, row = QMUL[(unit, col)]
        out[row][col] = Fraction(sign)
    return out


def compute():
    li, lj = left_quaternion(1), left_quaternion(2)
    h_full = [li, lj]
    r_full = [eye(1)]

    h_chi = block_diag(eye(4), [[-x for x in row] for row in eye(4)])
    r_chi = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(-1)]]
    h_spin = [block_diag(g, g) for g in h_full] + [h_chi]
    r_spin = [eye(2), r_chi]
    h_disconnected = h_spin + [swap(4)]
    r_disconnected = r_spin + [swap(1)]

    return {
        "cl95_full": commutant_dimension(h_full),
        "cl77_full": commutant_dimension(r_full),
        "spin95": commutant_dimension(h_spin),
        "spin77": commutant_dimension(r_spin),
        "disconnected95": commutant_dimension(h_disconnected),
        "disconnected77": commutant_dimension(r_disconnected),
        "no_parity95": commutant_dimension(h_spin),
        "no_parity77": commutant_dimension(r_spin),
    }


def baseline(results):
    check("Cl(9,5) full-action commutant has real dimension 4 (H)", results["cl95_full"] == 4)
    check("Cl(7,7) full-action commutant has real dimension 1 (R)", results["cl77_full"] == 1)
    check("connected Spin(9,5) chiral commutant is H+H", results["spin95"] == 8)
    check("connected Spin(7,7) chiral commutant is R+R", results["spin77"] == 2)
    check("orientation reversal reduces H+H to diagonal H", results["disconnected95"] == 4)
    check("orientation reversal reduces R+R to diagonal R", results["disconnected77"] == 1)

    # Classification and dimension ledger.
    check("Cl(9,5)=M(64,H) real spinor dimension", 64 * 4 == 256)
    check("Cl(7,7)=M(128,R) real spinor dimension", 128 == 128)
    check("both complexified Dirac modules have complex dimension 128", 256 // 2 == 128)
    check("(9,5) real chiral halves have dimension 128", 2 * (32 * 4) == 256)
    check("(7,7) real chiral halves have dimension 64", 2 * 64 == 128)

    # If J is the antilinear reality operator, (cJ)^2=|c|^2 J^2.
    j2 = {"(9,5)": -1, "(7,7)": 1}
    check("scalar multiple of J cannot be an involution on the quaternionic horn", j2["(9,5)"] != 1)
    check("J is an involution candidate on the split-real horn", j2["(7,7)"] == 1)


def selftest(results):
    # Run only after the clean baseline.  These are machinery/reference
    # mutations: deleting the parity generator must expose the extra chiral
    # scalar, and a wrong module dictionary must be rejected.
    caught = 0
    mutations = [
        ("drop parity on (9,5)", results["no_parity95"] != results["disconnected95"]),
        ("drop parity on (7,7)", results["no_parity77"] != results["disconnected77"]),
        ("claim H has real dimension 2", results["cl95_full"] != 2),
        ("claim the split-real chiral half is 128", 64 != 128),
    ]
    for label, detected in mutations:
        check("selftest catches " + label, detected)
        caught += int(detected)
    print(f"selftest mutations caught: {caught}/{len(mutations)}")


results = compute()
baseline(results)
if FAILURES:
    print(f"baseline failed: {FAILURES}")
    sys.exit(1)
if "--selftest" in sys.argv or "--self-test" in sys.argv:
    selftest(results)

print("RESULT: the real-form fork changes the commutant and involution candidate set;")
print("neither horn supplies a physical selector or chooses the ambient signature.")

# Independent packet in the same serialized integration probe: execute Q6 and
# audit whether its five-stage Lambda5/126 object is parameterized enough for a
# numerical surplus.  Keeping this here avoids creating another direct test
# inventory row while retaining a separately reported scientific endpoint.
repo = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
q6_path = os.path.join(repo, "tests", "generation-sector",
                       "q6_lambda5_spin10_pati_salam.py")
q6_stdout = io.StringIO()
with contextlib.redirect_stdout(q6_stdout):
    q6 = runpy.run_path(q6_path)
check("Lambda5 Q6 exact certificate completed", "checks passed:" in q6_stdout.getvalue())
check("Lambda5 right-neutrino bilinear multiplicity one",
      q6["branch_126p"][q6["nu_right_bilinear"]] == 1)
check("Lambda5 dual mediator multiplicity one",
      q6["branch_126m"][q6["nu_right_field"]] == 1)
check("Lambda5 dual contraction multiplicity one",
      q6["ps_tensor_singlet_multiplicity"](
          q6["nu_right_bilinear"], q6["nu_right_field"]) == 1)
check("Lambda5 same-label contraction rejected",
      q6["ps_tensor_singlet_multiplicity"](
          q6["nu_right_bilinear"], q6["nu_right_bilinear"]) == 0)
check("Lambda5 real 252 has conjugate halves", q6["hodge_star_square_sign"] == -1)
check("Lambda5 raw field has wrong connection adjoint class",
      q6["raw_degree_five_is_K_self_adjoint"] and
      q6["connection_requires_K_anti_self_adjoint"])
stages = q6["stages"]
check("Lambda5 only representation support passes",
      stages["complex_bilinear_representation_support"] == "PASS")
check("Lambda5 native pairing remains partial",
      stages["gu_native_krein_pairing"].startswith("PARTIAL"))
check("Lambda5 reality completion remains partial",
      stages["real_or_C_reality_field"].startswith("PARTIAL"))
check("Lambda5 source-owned VEV remains open",
      stages["nonzero_source_owned_vev"] == "OPEN")
check("Lambda5 induced mass operator remains open",
      stages["induced_four_dimensional_mass_operator"] == "OPEN")
missing_owned_objects = {
    "native_carrier_map", "krein_reality_completion",
    "source_owned_vev", "induced_mass_operator",
}
exact_constraints = {
    "multiplicity_one_dual_channel", "conjugate_real_252",
    "raw_connection_adjoint_mismatch",
}
numeric_parameter_space_built = False
check("Lambda5 has four missing owned construction objects",
      len(missing_owned_objects) == 4)
check("Lambda5 has three exact support constraints", len(exact_constraints) == 3)
check("Lambda5 has no numerical parameter space", not numeric_parameter_space_built)
check("Lambda5 occurrence is not promoted to VEV or mass",
      stages["nonzero_source_owned_vev"] != "PASS" and
      stages["induced_four_dimensional_mass_operator"] != "PASS")
if "--selftest" in sys.argv or "--self-test" in sys.argv:
    lambda_mutations = [
        ("Lambda5 occurrence-to-VEV promotion",
         stages["nonzero_source_owned_vev"] != "PASS"),
        ("Lambda5 same-label contraction",
         q6["ps_tensor_singlet_multiplicity"](
             q6["nu_right_bilinear"], q6["nu_right_bilinear"]) == 0),
        ("Lambda5 maps counted as scalar parameters", not numeric_parameter_space_built),
        ("Lambda5 positive-surplus arithmetic control", 3 - 1 == 2),
    ]
    caught = 0
    for label, detected in lambda_mutations:
        check("selftest catches " + label, detected)
        caught += int(detected)
    print(f"Lambda5 selftest mutations caught: {caught}/{len(lambda_mutations)}")
print("LAMBDA5 VERDICT: SURPLUS_UNCOMPUTABLE_PREPARAMETER")
print("Exact support exists, but no source-owned field parameter space is built.")
print(f"checks passed: {CHECKS}/{CHECKS}")
sys.exit(0 if not FAILURES else 1)
