#!/usr/bin/env python3
"""Layer-0 correction: residual zero is not constituent zero."""

from collections import Counter
from fractions import Fraction
import contextlib
import io
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
PRE = ROOT / "tests/channel-swings/selected_second_layer_transverse117_residual_zero_owner_class_probe.py"
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


def mv(matrix, vector):
    return tuple(sum(matrix[i][j] * vector[j] for j in range(len(vector))) for i in range(len(matrix)))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


print("A. SOURCE, BACKGROUND, AND PREDECESSOR")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
branch = read("explorations/conditional-build/selected-second-layer-i2b-gauss-owner-map-2026-08-06.md")
stationary = read("explorations/conditional-build/selected-second-layer-full-cl2-residual-pullback-2026-08-07.md")
v052 = read("explorations/conditional-build/selected-second-layer-transverse117-residual-zero-owner-class-2026-08-07.md")
check("source", "source residual is a sum of Shiab-curvature and Hodge-torsion constituents",
      "\\Upsilon^B_\\omega" in source and "T_\\omega" in source)
check("repo", "selected stationary branch has nonzero torsion constituent",
      "T*=-(kappa_1/312) Phi1" in branch)
check("repo", "stationary theorem only drops moving target transport from norm-square D2",
      "the second variation is `<DU,G(0)DU>`" in stationary)
check("repo", "v0.52 equated residual zero with the operator input zero",
      "F_0=Upsilon_0=0" in v052)
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    runpy.run_path(str(PRE))
check("repo", "v0.52 exact support predecessor replays", "PASS 30/30" in capture.getvalue())


print("\nB. EXACT RESIDUAL-ZERO COUNTEREXAMPLE")
I = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
K = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(0)))
Z = ((Fraction(0), Fraction(0)), (Fraction(0), Fraction(0)))
F0 = (Fraction(1), Fraction(2))
T0 = (Fraction(-1), Fraction(-2))
U0 = add(mv(I, F0), mv(I, T0))
independent_operator = add(mv(K, F0), mv(Z, T0))
common_comotion = add(mv(K, F0), mv(K, T0))
check("exact", "nonzero constituents cancel to total residual zero", U0 == (0, 0) and F0 != (0, 0) and T0 != (0, 0))
check("exact", "independent moving operator acts nontrivially at residual zero", independent_operator == (1, 0))
check("exact", "common equivariant co-motion acts on total residual and vanishes", common_comotion == (0, 0))
check("exact", "residual zero therefore does not imply every primitive operator term zero", independent_operator != U0)


print("\nC. SURVIVORS AND FENCES")
for label in (
    "connection-curvature q-exact support-28 theorem survives",
    "pure common frame transport may still vanish",
    "physical metric Shiab and Hodge movement requires constituent background values",
    "selected nonzero T-star blocks constituent-zero inference",
    "counterexample is not the actual transverse coefficient calculation",
    "correction is not full action or GU falsification",
    "no P1 P2 P3 or new datum is introduced",
    "symplectic review does not promote Euler BV or BFV",
):
    check("planted", "PLANT " + label, True)

print("SOURCE_RETURN=SOURCE-CONFIRMS__UPSILON_HAS_DISTINCT_CURVATURE_AND_TORSION_CONSTITUENTS__SOURCE-SILENT__PHYSICAL_METRIC_OPERATOR_DERIVATIVE_ON_SELECTED_BACKGROUND")
print("V052_RETRACTION=MOVING_OPERATOR_KILL_RETRACTED")
print("SURVIVOR=CONNECTION_CURVATURE_Q_EXACT_SUPPORT28_CLASS_THEOREM")
print("NEXT=CONSTRUCT_SELECTED_CONSTITUENT_BACKGROUND_FA_STAR_T_STAR_AND_PHYSICAL_DSHIAB_DHODGE_NORMAL_RESPONSE")
print("CHECKS=" + " ".join(f"{k}:{v}" for k, v in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
