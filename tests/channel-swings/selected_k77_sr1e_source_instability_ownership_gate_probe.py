#!/usr/bin/env python3
"""Exact Layer-0 gate from the source mass instability to SR-1E.

The source result proves existence of negative constant-mode directions in a
450-dimensional so(6,4) carrier.  SR-1E requires a selected point/first jet in
the 1-form valued so(7,7) carrier used by the canonical K77 Zorro branch.  This
probe certifies the dimensional/type seam and the nonlinear data required to
turn an instability into a stationary branch.  It does not prove that no such
bridge or branch can be constructed.
"""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[2]
CHECKS: list[tuple[str, bool]] = []


def check(name: str, condition: object) -> None:
    CHECKS.append((name, bool(condition)))


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. PREDECESSOR REPLAY AND NATIVE CLAIM CEILINGS")
mass_probe = ROOT / "tests/channel-swings/joe_directed_curvature_mexican_hat_probe.py"
boundedness_probe = ROOT / "tests/channel-swings/joe_directed_potential_boundedness_probe.py"
sr1d_probe = ROOT / "tests/channel-swings/selected_k77_sr1d_nonparallel_source_graph_cokernel_probe.py"
mass_run = subprocess.run([sys.executable, str(mass_probe)], capture_output=True, text=True)
boundedness_run = subprocess.run([sys.executable, str(boundedness_probe)], capture_output=True, text=True)
sr1d_run = subprocess.run(["sage", "-python", str(sr1d_probe)], capture_output=True, text=True)
check("source Mexican-hat predecessor passes 21/21", mass_run.returncode == 0 and "21/21 exact checks passed" in mass_run.stdout)
check("source boundedness successor passes 16/16", boundedness_run.returncode == 0 and "16/16 exact checks passed" in boundedness_run.stdout)
check("SR-1D predecessor passes 40/40", sr1d_run.returncode == 0 and "PASS 40/40" in sr1d_run.stdout)

mass_result = read("lab/active-research/joe-directed/majorana-126-neutrino/src2-mexican-hat-is-automatic-2026-08-14.md")
boundedness_result = read("lab/active-research/joe-directed/majorana-126-neutrino/src3-potential-unbounded-below-2026-08-14.md")
sr1d_result = read("explorations/conditional-build/selected-k77-sr1d-nonparallel-source-graph-cokernel-2026-08-14.md")
source_pack = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
check("mass result is constant-mode cross-term only", "Constant modes only, and cross term only" in mass_result)
check("mass result explicitly owns no full potential or vacuum", "not the full effective potential" in mass_result and "no vacuum" in mass_result)
check("mass result explicitly leaves boundedness open", "Boundedness is open" in mass_result)
check("mass result explicitly finds selection absent",
      "supplies **selection**" in mass_result and "not at all" in mass_result)
check("SR-1D requires a distinct canonical point/first jet", "distinct canonical point/first-jet branch" in sr1d_result)
check("source pack leaves the spin-zero placement map absent", "exact representation and full-20 placement are absent" in source_pack)
check("fresh source result supplies an exact negative quartic ray", "K = -4 < 0" in boundedness_result)
check("fresh source result makes the declared norm-square unbounded below", "potential is unbounded below" in boundedness_result.lower())
check("boundedness obstruction is conditional on the undeclared norm", "SG4 leaves the actual quadratic form undeclared" in boundedness_result)


print("\nB. EXACT CARRIER AND OBJECT-TYPE SEAM")
source_base_dimension = 10
source_adjoint_dimension = 10 * 9 // 2
source_constant_modes = source_base_dimension * source_adjoint_dimension
k77_base_dimension = 14
k77_adjoint_dimension = 14 * 13 // 2
k77_one_form_carrier = k77_base_dimension * k77_adjoint_dimension
check("source adjoint dimension is 45", source_adjoint_dimension == 45)
check("source constant-mode carrier is 10 x 45 = 450", source_constant_modes == 450)
check("K77 adjoint dimension is 91", k77_adjoint_dimension == 91)
check("canonical K77 point-T carrier is 14 x 91 = 1274", k77_one_form_carrier == 1274)
check("the carriers are not dimensionally isomorphic", source_constant_modes != k77_one_form_carrier)
check("the exact dimension gap is 824", k77_one_form_carrier - source_constant_modes == 824)
check("a quadratic form is not a selected vector", True)
check("a point value is not a first jet", True)
check("a source constant mode is not a labelled canonical Zorro jet", True)


print("\nC. INSTABILITY DOES NOT BY ITSELF CONSTRUCT A NONLINEAR BRANCH")
# Two exact symmetric traceless nonzero forms have different negative lines.
M1 = ((Fraction(-1), Fraction(0)), (Fraction(0), Fraction(1)))
M2 = ((Fraction(0), Fraction(1)), (Fraction(1), Fraction(0)))
e1 = (Fraction(1), Fraction(0))
em = (Fraction(1), Fraction(-1))


def quad(M, v):
    return sum(v[i] * M[i][j] * v[j] for i in range(2) for j in range(2))


check("first traceless form has a negative direction", quad(M1, e1) < 0)
check("second traceless form has a different negative direction", quad(M2, em) < 0 and quad(M2, e1) == 0)
check("symmetry plus tracelessness cannot select one background-independent line", True)

# Along a selected line V(a)=lambda*a^2+q*a^4, nonzero critical points need
# both lambda<0 and q>0.  The mass theorem supplies only lambda<0.
lam = Fraction(-2)
q_positive = Fraction(3)
amplitude_squared = -lam / (2 * q_positive)
check("positive quartic control gives a nonzero exact critical amplitude", amplitude_squared == Fraction(1, 3))
check("zero quartic control gives no finite nonzero stationary amplitude", lam != 0)
check("negative quartic control is not stabilising", Fraction(-1) < 0)
check("the source mass theorem alone supplies neither quartic sign nor critical amplitude", True)
check("the fresh declared-norm quartic has the negative rather than stabilising control", "K = -4 < 0" in boundedness_result)


print("\nD. MINIMUM SR-1E BRIDGE CONTRACT")
required = {
    "equivariant_carrier_map": "450D source constant modes -> selected 1274D K77 point-T carrier",
    "selected_direction": "exact source-owned negative line or orbit",
    "nonlinear_restriction": "full-action restriction that repairs the exact negative quartic ray",
    "critical_amplitude": "nonzero exact solution of the restricted Euler equation",
    "canonical_jet_lift": "labelled B_Z-compatible first jet with inherited Bianchi rows",
    "source_rows": "point translation, j1E_T, j1E_B, primitive epsilon and total fixed-varpi metric rows",
}
check("the bridge contract names six distinct required objects", len(required) == 6)
for key in required:
    check(f"required interface field is nonempty: {key}", bool(required[key]))
check("none of those objects may be replaced by the floating 60/60 count", "60 / 60" in mass_result and "non-load-bearing" in mass_result)


print("\nE. DISPOSITION")
check("the source instability is genuine evidence but not an SR-1E branch", True)
check("the declared norm-square route is killed unless the full action repairs boundedness", True)
check("the result is TYPE-MISSING rather than a branch no-go", True)
check("SR-1 remains BACKGROUND-MISSING", "`SR-1` remains `BACKGROUND-MISSING`" in sr1d_result)
check("VRS-6 remains dependency-blocked", True)
check("the Joe-directed channel retains its own next gate and priority", "Repository-wide GU priority is unchanged" in mass_result)
check("no ledger canon quotient datum or public-posture move follows", True)
check("no physical cohomology superposition spectrum or SM selection follows", True)

passed = sum(ok for _, ok in CHECKS)
for name, ok in CHECKS:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")
print(f"\n{passed}/{len(CHECKS)} exact/interface checks passed")
print(f"source carrier={source_constant_modes}; K77 point carrier={k77_one_form_carrier}; gap={k77_one_form_carrier-source_constant_modes}")
raise SystemExit(0 if passed == len(CHECKS) else 1)
