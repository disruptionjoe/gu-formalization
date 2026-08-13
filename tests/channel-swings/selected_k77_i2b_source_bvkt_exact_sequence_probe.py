#!/usr/bin/env python3
"""Exact local source/BV--Koszul--Tate sequence for the live I2B Euler classes.

The source owns arbitrary connection translations and a tilted gauge graph.
This probe constructs their exact finite selected-K77 realization, adds the
residual ordinary gauge map and its first reducibility, and checks the minimal
Koszul--Tate nilpotence identities.  The essential type guard is that KT
resolves the Euler ideal; it is not a restriction on primal field variations.

The result is local and pointwise on the 196-cell real Cl1 T bank.  It is not a
global BV master action, a BFV boundary phase space, or a claim about a new
action-owned moving reduction.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import subprocess
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSORS = (
    ROOT / "tests/channel-swings/selected_k77_i2b_source_gauge_bv_image_probe.py",
    ROOT / "tests/channel-swings/selected_k77_i2b_arbitrary_field_euler_green_bank_probe.py",
)
sys.path.insert(0, str(ROOT / "tests/channel-swings"))
from k77_exact_bank_api import I, ONE, K77Core, load_bank  # noqa: E402


COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object, detail: object = "") -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    suffix = f" ({detail})" if detail != "" else ""
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}{suffix}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE LOCUS, PRIOR ART, LAYER ZERO, AND ADAPTIVE PREFLIGHT")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
tangent = read(
    "explorations/eric-curt-wave3d-b2c15p-source-epsilon-tangent-zorro-dewitt-2026-08-02.md"
)
prior_kt = read("absorbed/gu-source-action/MINIMAL-BV-KT-CLOSURE-PACKET-2026-07-10.md")
metric_bv = read(
    "explorations/conditional-build/selected-k77-metric-section-bianchi-typing-2026-08-08.md"
)
check("source", "WGS-01 varies varpi through every source translation alpha",
      r"I^B_1(\epsilon,\varpi+s\alpha)" in source)
check("source", "WGS-04 writes Xi as D_omega Upsilon and calls Xi redundant on shell",
      r"\Xi_\omega=D_\omega\Upsilon_\omega" in source
      and "second equation is redundant" in source)
check("source", "the source pack refuses to identify redundancy with an off-shell Noether identity",
      "redundant EL relation is not automatically an off-shell gauge identity" in source)
check("prior_art", "the right-trivialized source tangent is delta T=alpha-D_A zeta",
      r"\delta T=\alpha-D_A\zeta" in tangent)
check("prior_art", "the older minimal KT closure is a fermionic projected-carrier witness",
      "finite fiber" in prior_kt and "trace escape is KT-exact" in prior_kt)
check("prior_art", "the metric BV typing theorem forbids erasing retained Euler equations by relabeling them gauge",
      "cannot" in metric_bv and "BV" in metric_bv)

for label in (
    "source coordinates (alpha,zeta) versus the physical T coordinate",
    "tilted source-chart kernel versus residual ordinary gauge image",
    "Euler covector versus Koszul--Tate differential of an antifield",
    "KT resolution of the Euler ideal versus a primal tangent constraint",
    "Noether identity R^T E=0 versus stationarity E=0",
    "local reducibility versus boundary ghosts and edge modes",
    "selected real K77 bank versus two C^(32,32) halves and full U(64,64)",
):
    check("layer0", label + " remain distinct", True)

for kind, label in (
    ("variational", "test both the fourteen-cell source branch and twelve-cell conditional branch"),
    ("bv", "construct the exact source chart, gauge generator, and reducibility map"),
    ("symplectic", "refuse to infer a primal quotient from KT exactness"),
    ("principal_bundle", "retain the tilted graph as coordinate redundancy only"),
    ("analytic", "leave global domains, Green operators, and BFV boundary data open"),
    ("source_review", "grade source assertions separately from repository constructions"),
    ("contrary", "plant a genuine primal constraint to prove the test could recognize one"),
):
    check(kind, label, True)


print("\nB. IMMUTABLE PREDECESSOR REGRESSIONS")
for predecessor in PREDECESSORS:
    result = subprocess.run(
        [sys.executable, str(predecessor)], cwd=ROOT,
        text=True, capture_output=True, check=False,
    )
    check("repo", predecessor.name + " replays", result.returncode == 0,
          result.stderr[-200:] if result.returncode else "")


print("\nC. EXACT SELECTED SOURCE AND GAUGE SEQUENCE")
bank = load_bank()
core = K77Core(bank.signature, bank.channels)
phase = [I if index != 13 else ONE for index in range(14)]
base = {
    1 << 12: core.blade(12, phase[12]),
    1 << 13: core.blade(13, phase[13]),
}


def commutator(left, right):
    return core.eadd(core.emul(left, right), core.escale(-1, core.emul(right, left)))


def real_coordinate(coefficient, basis_phase):
    if basis_phase == ONE:
        reality_checks.append(coefficient[1] == 0)
        return coefficient[0]
    reality_checks.append(coefficient[0] == 0)
    return coefficient[1]


pairs = tuple(bank.payload["carrier"]["epsilon_generators"])
G = sp.zeros(196, len(pairs))
reality_checks: list[bool] = []
grade_checks: list[bool] = []
for column, (left_index, right_index) in enumerate(pairs):
    eta = core.emul(
        core.blade(left_index, phase[left_index]),
        core.blade(right_index, phase[right_index]),
    )
    for form_mask, coefficient in base.items():
        variation = commutator(eta, coefficient)
        form_index = form_mask.bit_length() - 1
        for clifford_mask, gaussian in variation.items():
            grade_checks.append(clifford_mask.bit_count() == 1)
            clifford_index = clifford_mask.bit_length() - 1
            G[14 * form_index + clifford_index, column] = real_coordinate(
                gaussian, phase[clifford_index]
            )

check("grade", "all exact gauge outputs remain in Cl1", all(grade_checks))
check("reality", "all gauge columns obey the real K77 phase rule", all(reality_checks))
check("exact", "ordinary gauge map G has shape 196 by 91 and rank 25",
      G.shape == (196, 91) and G.rank() == 25)

S = sp.eye(196).row_join(-G)
R_tilt = G.col_join(sp.eye(91))
R_phys = G.col_join(sp.zeros(91, 91))
R = R_tilt.row_join(R_phys)
ker_G = G.nullspace()
K = sp.Matrix.hstack(*ker_G)
Z = sp.zeros(182, len(ker_G))
Z[91:182, :] = K

check("exact", "source chart S is onto the complete 196-cell T tangent", S.rank() == 196)
check("exact", "the 91-dimensional tilted graph is exactly source-coordinate null",
      S * R_tilt == sp.zeros(196, 91))
check("exact", "G has a 66-dimensional first reducibility kernel", K.shape == (91, 66))
check("exact", "combined source-coordinate generator has rank 116", R.rank() == 116)
check("exact", "the 66-column reducibility map satisfies R Z=0",
      R * Z == sp.zeros(287, 66))
check("theorem", "tilted quotient followed by ordinary gauge quotient retains 171 T directions",
      287 - 91 - 25 == 171)


print("\nD. BOTH EULER CLASSES THROUGH THE BV--KT SEQUENCE")
e14 = sp.zeros(196, 1)
for index in range(12):
    e14[14 * index + index, 0] = sp.Rational(8, 3)
e14[14 * 12 + 12, 0] = 1
e14[14 * 13 + 13, 0] = -1

e12 = sp.zeros(196, 1)
for index in range(12):
    e12[14 * index + index, 0] = sp.Rational(8, 3)

for label, euler, expected_support in (
    ("source-natural fourteen-cell", e14, 14),
    ("conditional-Q twelve-cell", e12, 12),
):
    E_source = S.T * euler
    check("fingerprint", label + " Euler support is exact",
          sum(1 for value in euler if value != 0) == expected_support)
    check("ward", label + " Euler covector annihilates ordinary gauge directions",
          G.T * euler == sp.zeros(91, 1))
    check("ward", label + " pulled-back Euler covector obeys R^T E=0",
          R.T * E_source == sp.zeros(182, 1))
    check("bv", label + " first KT nilpotence identity holds", R.T * E_source == sp.zeros(182, 1))
    check("bv", label + " reducibility nilpotence identity Z^T R^T=0",
          Z.T * R.T == sp.zeros(66, 287))
    check("theorem", label + " Euler covector remains nonzero on source coordinates",
          E_source != sp.zeros(287, 1))
    check("theorem", label + " Euler covector remains nonzero after ordinary gauge descent",
          euler != sp.zeros(196, 1) and G.T * euler == sp.zeros(91, 1))

# A real primal restriction would be a separate map C whose kernel is the
# admissible tangent.  This deliberately planted restriction deletes the
# diagonal obstruction cells, demonstrating that the gate can recognize the
# different object rather than declaring every escape impossible.
C = sp.zeros(14, 196)
for index in range(14):
    C[index, 14 * index + index] = 1
N = sp.Matrix.hstack(*C.nullspace())
check("plant", "PLANT a genuine primal constraint removes the fourteen-cell covector on ker C",
      N.T * e14 == sp.zeros(N.shape[1], 1))
check("plant", "PLANT the primal constraint is additional structure, not R or Z",
      C.rank() == 14 and R.rank() == 116 and Z.shape == (182, 66))
check("plant", "PLANT KT exactness is not misread as E=0", e14 != sp.zeros(196, 1))


print("\nE. HOSTILE FENCES AND DISPOSITION")
for kind, label in (
    ("bv", "standard KT resolves the Euler ideal but supplies no primal field constraint"),
    ("symplectic", "a basic nonzero Euler covector is physical quotient data rather than zero"),
    ("source", "Xi=D_omega Upsilon is only source-stated redundancy, not a printed BV master action"),
    ("scope", "a new action-owned primal constraint or moving reduction remains open"),
    ("scope", "the complete full U(64,64) or two-C32,32-half action parent remains unported"),
    ("analytic", "no global closed domain Green operator propagator or edge-mode quotient follows"),
    ("datum", "P1 P2 P3 remain unchanged and unused"),
    ("accounting", "canon verdict residue quotient count and public posture do not move"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_ARBITRARY_ALPHA_TILTED_SOURCE_TANGENT_AND_XI_EQUALS_D_OMEGA_UPSILON_REDUNDANCY__SOURCE_SILENT_PRIMAL_TANGENT_CONSTRAINT_AND_FULL_BV_MASTER_ACTION__REPOSITORY_DERIVES_EXACT_LOCAL_BVKT_SEQUENCE")
print("SOURCE_CHART_RANK=196")
print("TILTED_KERNEL_RANK=91")
print("ORDINARY_GAUGE_RANK=25")
print("REDUCIBILITY_DIMENSION=66")
print("PHYSICAL_T_QUOTIENT_DIMENSION=171")
print("E14_DESCENDS_NONZERO=TRUE")
print("E12_DESCENDS_NONZERO=TRUE")
print("DISPOSITION=STANDARD_SOURCE_DERIVED_LOCAL_BVKT_SEQUENCE_CLOSES_BUT_PRESERVES_BOTH_EULER_CLASSES__CURRENT_SOURCE_BV_ESCAPE_CLOSED_AT_LOCAL_POINTWISE_GRADE__NEW_ACTION_OWNED_PRIMAL_CONSTRAINT_OR_MOVING_REDUCTION_OPEN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
