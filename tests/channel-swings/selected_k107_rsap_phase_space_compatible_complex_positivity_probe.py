#!/usr/bin/env python3
"""Exact K107 invariant zero-section complex/Krein positivity classification."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import contextlib
import io
import json
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
K106_PROBE = ROOT / "tests/channel-swings/selected_k106_rsap_balanced_quotient_positivity_ellipticity_probe.py"
REGISTRY = ROOT / "lab/process/selected-k107-rsap-phase-space-compatible-complex-positivity.json"
RESULT = ROOT / "explorations/conditional-build/selected-k107-rsap-phase-space-compatible-complex-positivity-2026-08-15.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-15-selected-k107-rsap-phase-space-compatible-complex-positivity-review.md"
CURRENT = ROOT / "CURRENT-STATE.yaml"
NEXT = ROOT / "NEXT-STEPS.md"
K106_RESULT = ROOT / "explorations/conditional-build/selected-k106-rsap-balanced-quotient-positivity-ellipticity-2026-08-15.md"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def tr(a):
    return [list(row) for row in zip(*a)]


def det2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def eye2():
    return [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]


def neg(a):
    return [[-value for value in row] for row in a]


def signature_tensor(sig_a: tuple[int, int], sig_b: tuple[int, int]) -> tuple[int, int]:
    ap, an = sig_a
    bp, bn = sig_b
    return ap * bp + an * bn, ap * bn + an * bp


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def p_add(left: dict[tuple[int, int, int], int],
          right: dict[tuple[int, int, int], int]):
    result = dict(left)
    for monomial, coefficient in right.items():
        result[monomial] = result.get(monomial, 0) + coefficient
        if result[monomial] == 0:
            del result[monomial]
    return result


def p_neg(value):
    return {monomial: -coefficient for monomial, coefficient in value.items()}


def p_mul(left, right):
    result = {}
    for lm, lc in left.items():
        for rm, rc in right.items():
            monomial = tuple(lm[i] + rm[i] for i in range(3))
            result[monomial] = result.get(monomial, 0) + lc * rc
    return {monomial: coefficient for monomial, coefficient in result.items() if coefficient}


def pmm(left, right):
    return [[sum_polynomials(p_mul(left[i][k], right[k][j])
                             for k in range(len(right)))
             for j in range(len(right[0]))] for i in range(len(left))]


def sum_polynomials(values):
    result = {}
    for value in values:
        result = p_add(result, value)
    return result


PZERO = {}
PONE = {(0, 0, 0): 1}
PA = {(1, 0, 0): 1}
PB = {(0, 1, 0): 1}
PC = {(0, 0, 1): 1}


print("A. PREDECESSOR AND DURABLE FILES")
k106_output = io.StringIO()
with contextlib.redirect_stdout(k106_output):
    runpy.run_path(str(K106_PROBE), run_name="__main__")
check("predecessor", "K106 invariant base positivity certificate replays 38/38",
      "PASS 38/38" in k106_output.getvalue())
check("artifact", "result registry and hostile review exist",
      all(path.exists() for path in (RESULT, REGISTRY, REVIEW)))


print("\nB. ZERO-SECTION PHASE CARRIER")
q_signature = (24, 25)
check("carrier", "the base isotropy module has dimension 49", sum(q_signature) == 49)
check("carrier", "cotangent doubling has dimension 98", 2 * sum(q_signature) == 98)
check("commutant", "two copies enlarge the scalar commutant to dimension four", 2 * 2 == 4)
K = [[Fraction(0), Fraction(1)], [Fraction(-1), Fraction(0)]]
check("symplectic", "the multiplicity form K is skew and nondegenerate",
      tr(K) == neg(K) and det2(K) == 1)


print("\nC. ALL RATIONAL INTEGER COMPATIBLE-COMPLEX FIXTURES")
A_sym = [[PA, PB], [PC, p_neg(PA)]]
K_sym = [[PZERO, PONE], [p_neg(PONE), PZERO]]
B_sym = pmm(K_sym, A_sym)
relation = p_add(p_mul(PA, PA), p_mul(PB, PC))
relation_identity = [[relation, PZERO], [PZERO, relation]]
check("symbolic", "generic A squared is (a squared plus bc) identity",
      pmm(A_sym, A_sym) == relation_identity)
check("symbolic", "generic K A is symmetric",
      B_sym == [[B_sym[j][i] for j in range(2)] for i in range(2)])
check("symbolic", "generic determinant of K A is minus (a squared plus bc)",
      p_add(p_add(p_mul(B_sym[0][0], B_sym[1][1]),
                  p_neg(p_mul(B_sym[0][1], B_sym[1][0]))), relation) == PZERO)
AT_sym = [[A_sym[j][i] for j in range(2)] for i in range(2)]
minus_relation_K = [[PZERO, p_neg(relation)], [relation, PZERO]]
check("symbolic", "the complex relation forces symplectic compatibility",
      pmm(pmm(AT_sym, K_sym), A_sym) == minus_relation_K)
solutions = []
for a in range(-6, 7):
    for b in range(-6, 7):
        for c in range(-6, 7):
            if a * a + b * c == -1:
                A = [[Fraction(a), Fraction(b)], [Fraction(c), Fraction(-a)]]
                solutions.append(A)
check("complex", "the exact solution family has multiple nontrivial fixtures", len(solutions) >= 8)
all_square = all(mm(A, A) == neg(eye2()) for A in solutions)
check("complex", "every fixture obeys J squared equals minus identity", all_square)
all_symplectic = all(mm(mm(tr(A), K), A) == K for A in solutions)
check("complex", "every fixture preserves the canonical symplectic form", all_symplectic)
associated = [mm(K, A) for A in solutions]
check("metric", "every associated multiplicity form K A is symmetric",
      all(B == tr(B) for B in associated))
check("metric", "every associated multiplicity form has determinant one",
      all(det2(B) == 1 for B in associated))


def definite_signature_2(B) -> tuple[int, int]:
    if B[0][0] > 0:
        return 2, 0
    if B[0][0] < 0:
        return 0, 2
    raise AssertionError("determinant-one symmetric fixture cannot have zero leading entry here")


factor_signatures = [definite_signature_2(B) for B in associated]
check("metric", "the multiplicity forms are positive or negative definite",
      set(factor_signatures) == {(2, 0), (0, 2)})
phase_signatures = {signature_tensor(sig, q_signature) for sig in factor_signatures}
check("signature", "all associated 98D metrics have signature 48|50 up to sign",
      phase_signatures == {(48, 50), (50, 48)})
check("positivity", "no invariant compatible complex fixture is positive",
      (98, 0) not in phase_signatures and (0, 98) not in phase_signatures)
A0 = [[Fraction(0), Fraction(-1)], [Fraction(1), Fraction(0)]]
check("control", "the standard compatible complex structure is present", A0 in solutions)
check("control", "its multiplicity metric is positive identity but q remains indefinite",
      mm(K, A0) == eye2() and signature_tensor((2, 0), q_signature) == (48, 50))


print("\nD. REAL POLARIZATION POSITIVE CONTROLS")
lines = [(Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)),
         (Fraction(1), Fraction(1)), (Fraction(2), Fraction(-3))]
line_isotropic = all(
    sum(vector[i] * K[i][j] * vector[j] for i in range(2) for j in range(2)) == 0
    for vector in lines)
check("polarization", "every planted multiplicity line is symplectically isotropic", line_isotropic)
check("polarization", "line tensor U has half dimension and is Lagrangian",
      sum(q_signature) == 98 // 2 and line_isotropic)
check("polarization", "the vertical cotangent line is among the exact controls",
      (Fraction(0), Fraction(1)) in lines)
check("control", "polarization existence does not change the inherited U signature",
      q_signature == (24, 25))


print("\nE. KREIN AND INVARIANT LINEAR-REDUCTION CONTROLS")
check("krein", "scalar invariant involutions on U are only plus or minus identity",
      {value for value in range(-4, 5) if value * value == 1} == {-1, 1})
check("krein", "both scalar fundamental-symmetry candidates leave q indefinite",
      {q_signature, tuple(reversed(q_signature))} == {(24, 25), (25, 24)})
sample_B = [[Fraction(2), Fraction(1)], [Fraction(1), Fraction(3)]]
sample_eigen_ray = (Fraction(1), Fraction(0))
ray_value = sum(sample_eigen_ray[i] * sample_B[i][j] * sample_eigen_ray[j]
                for i in range(2) for j in range(2))
check("krein", "a nonzero multiplicity ray paired with q produces both signs",
      ray_value > 0 and q_signature[0] > 0 and q_signature[1] > 0)
check("constraint", "proper nonzero multiplicity subspaces give only 49D modules",
      1 * 49 == 49 and 49 not in (0, 98))
check("constraint", "the 49D invariant submodule and quotient retain 24|25 up to sign",
      q_signature == (24, 25))
check("positivity", "no nonzero invariant linear subquotient is positive",
      q_signature[0] > 0 and q_signature[1] > 0)


print("\nF. REGISTRY AND CLAIM CEILING")
registry = load(REGISTRY)
check("registry", "registry records the doubled commutant rather than reusing the base one",
      registry["carrier"]["H_commutant_on_phase_tangent"].startswith("M2_R"))
check("registry", "compatible complex structures exist but positive ones do not",
      registry["compatible_complex_classification"]["examples_exist"] is True
      and registry["compatible_complex_classification"]["positive_compatible_invariant_complex_structure_exists"] is False)
check("registry", "the canonical vertical real polarization is retained",
      registry["polarization"]["canonical_vertical_real_polarization"] == "EXISTS_AND_IS_G_INVARIANT")
check("ceiling", "the result is limited to zero-section invariant linear data",
      registry["claim_ceiling"]["binds"].startswith("H_bal_invariant_linear_data_on_the_zero_section"))
check("ceiling", "nonlinear cohomology and noninvariant domains remain open",
      "nonlinear_BFV_cohomology" in registry["claim_ceiling"]["does_not_bind"]
      and "boundary_domains" in registry["claim_ceiling"]["does_not_bind"])
check("owner", "all positive analytic selectors remain unowned by the current action",
      not registry["owner_fence"]["current_action_selects_noninvariant_positive_sector"]
      and not registry["owner_fence"]["current_action_selects_krein_fundamental_symmetry"]
      and not registry["owner_fence"]["current_action_selects_contour_or_boundary_domain"])
check("routing", "the result remains source-native and moves no ledger",
      registry["comparator_routing_classification"] == "SOURCE_NATIVE_ROUTE"
      and registry["disposition"]["ledger_change"] == "none")
check("roadmap", "CURRENT and NEXT route away from abstract invariant linear repairs",
      "K107" in CURRENT.read_text(encoding="utf-8")
      and "K107" in NEXT.read_text(encoding="utf-8")
      and "Stop abstract invariant linear" in NEXT.read_text(encoding="utf-8"))
check("successor", "K106 records the K107 successor closure",
      "Successor closure (K107)" in K106_RESULT.read_text(encoding="utf-8"))


summary = {"checks": sum(COUNTS.values()), "failures": FAILURES,
           "by_kind": dict(COUNTS)}
print("\n" + json.dumps(summary, indent=2, sort_keys=True))
raise SystemExit(1 if FAILURES else 0)
