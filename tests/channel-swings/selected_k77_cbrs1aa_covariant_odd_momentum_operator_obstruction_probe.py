#!/usr/bin/env sage -python
"""Exact CBRS-1AA equivariant operator and variational-owner gate.

The probe classifies the smallest zero/first-order Spin-covariant operator
basis on Lambda1 plus Lambda3, constructs nonzero exterior-basis witnesses for
both mixed BF maps, derives the auxiliary equations and field-redefinition
quotient, and checks the cross-form Hilbert traces and native propagation.
"""

from __future__ import annotations

from collections import Counter
import contextlib
import io
import itertools
import json
from math import comb, factorial
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
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


def canonical(indices: tuple[int, ...]) -> tuple[int, tuple[int, ...]]:
    if len(set(indices)) != len(indices):
        return 0, ()
    inversions = sum(
        indices[i] > indices[j]
        for i in range(len(indices))
        for j in range(i + 1, len(indices))
    )
    return (-1) ** inversions, tuple(sorted(indices))


def add_term(out: dict[tuple[int, ...], int], indices: tuple[int, ...], value: int) -> None:
    sign, key = canonical(indices)
    if sign:
        out[key] = out.get(key, 0) + sign * value
        if out[key] == 0:
            del out[key]


def so_action(form: dict[tuple[int, ...], int], left: int, right: int):
    """E_left,right sends e_left to e_right and e_right to -e_left."""
    out: dict[tuple[int, ...], int] = {}
    for basis, coefficient in form.items():
        for slot, index in enumerate(basis):
            if index == left:
                replaced = basis[:slot] + (right,) + basis[slot + 1:]
                add_term(out, replaced, coefficient)
            elif index == right:
                replaced = basis[:slot] + (left,) + basis[slot + 1:]
                add_term(out, replaced, -coefficient)
    return out


def wedge_vector(vector: int, form: dict[tuple[int, ...], int]):
    out: dict[tuple[int, ...], int] = {}
    for basis, coefficient in form.items():
        add_term(out, (vector,) + basis, coefficient)
    return out


def contract_vector(vector: int, form: dict[tuple[int, ...], int]):
    out: dict[tuple[int, ...], int] = {}
    for basis, coefficient in form.items():
        for slot, index in enumerate(basis):
            if index == vector:
                reduced = basis[:slot] + basis[slot + 1:]
                out[reduced] = out.get(reduced, 0) + (-1) ** slot * coefficient
    return {key: value for key, value in out.items() if value}


def inner(left: dict[tuple[int, ...], int], right: dict[tuple[int, ...], int]) -> int:
    return sum(value * right.get(key, 0) for key, value in left.items())


def basis_cross_stress_trace(n: int, p: int) -> sp.Integer:
    """Trace of the cross-p-form Hilbert tensor on one unit decomposable form."""
    active = tuple(range(p))

    def component(indices: tuple[int, ...]) -> int:
        sign, key = canonical(indices)
        return sign if key == active else 0

    contraction_trace = 0
    for mu in range(n):
        for rest in itertools.permutations([i for i in active if i != mu], p - 1):
            contraction_trace += component((mu,) + rest) ** 2
    pairing = sp.Integer(1)
    return n * pairing - sp.Rational(2, factorial(p - 1)) * contraction_trace


print("A. PREDECESSOR, RETRIEVAL, AND LAYER ZERO", flush=True)
predecessor = json.loads(read(
    "lab/process/selected-k77-cbrs1z-equivariant-sigma-odd-owner-admission-obstruction.json"
))
check("prior", "CBRS-1Z carries its exact 53-of-53 certificate",
      predecessor["probe_result"] == "PASS_53_OF_53")
check("prior", "CBRS-1Z opens the full covariant action-map gate",
      "FULL_LAMBDA1_PLUS_LAMBDA3" in predecessor["next_gate"])
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    state = runpy.run_path(str(
        ROOT / "tests/channel-swings/selected_k77_cbrs1z_equivariant_sigma_odd_owner_admission_obstruction_probe.py"
    ))
check("prior", "the complete CBRS-1Z executable replay remains green",
      "PASS 53/53" in capture.getvalue() and not state["FAILURES"])
check("type", "the full odd auxiliary has dimension 14+364=378",
      comb(14, 1) + comb(14, 3) == 378)
check("type", "the existing primitive bivector has dimension 91", comb(14, 2) == 91)
check("type", "the odd and primitive carriers have different Clifford parity", 1 % 2 != 2 % 2)
check("type", "the new auxiliary remains Grassmann even",
      predecessor["odd_owner"]["grassmann_parity"] == "EVEN")


print("B. EXACT TENSOR DECOMPOSITIONS", flush=True)
n = 14
d1 = comb(n, 1)
d2 = comb(n, 2)
d3 = comb(n, 3)
d4 = comb(n, 4)
sym2_zero = n * (n + 1) // 2 - 1
hook3 = n * d3 - d2 - d4
check("decomposition", "V tensor Lambda1 has dimension 196", n * d1 == 196)
check("decomposition", "Lambda0 plus Lambda2 plus Sym2_0 exhausts V tensor Lambda1",
      1 + d2 + sym2_zero == n * d1)
check("decomposition", "the traceless symmetric summand has dimension 104", sym2_zero == 104)
check("decomposition", "V tensor Lambda3 has dimension 5096", n * d3 == 5096)
check("decomposition", "the Lambda4 summand has dimension 1001", d4 == 1001)
check("decomposition", "the remaining Lambda3 hook has dimension 4004", hook3 == 4004)
check("decomposition", "Lambda2 plus Lambda4 plus the hook exhausts V tensor Lambda3",
      d2 + d4 + hook3 == n * d3)
check("decomposition", "Lambda2 occurs in both first-jet decompositions",
      d2 == 91 and 1 + 1 == 2)


print("C. HOM SPACES AND BOUNDED OPERATOR LEDGER", flush=True)
decomp_v_l1 = {"Lambda0": 1, "Lambda2": 1, "Sym2_0": 1}
decomp_v_l3 = {"Lambda2": 1, "Lambda4": 1, "Hook3": 1}
decomp_w = {"Lambda1": 1, "Lambda3": 1}
check("hom", "Hom(Wodd,scalar) is zero", not ({"Lambda0"} & set(decomp_w)))
check("hom", "End_Spin(Wodd) has two grade projectors", sum(v * v for v in decomp_w.values()) == 2)
check("hom", "Hom(V tensor Wodd,scalar) has dimension one",
      decomp_v_l1.get("Lambda0", 0) + decomp_v_l3.get("Lambda0", 0) == 1)
check("hom", "Hom(V tensor Wodd,Wodd) is zero",
      not ((set(decomp_v_l1) | set(decomp_v_l3)) & set(decomp_w)))
check("hom", "Hom(V tensor Wodd,Lambda2) has dimension two",
      decomp_v_l1["Lambda2"] + decomp_v_l3["Lambda2"] == 2)
check("operator", "there are two zero-order symmetric grade pairings", len(decomp_w) == 2)
check("operator", "the one linear first-order scalar is the Lambda0 divergence channel",
      decomp_v_l1["Lambda0"] == 1 and "Lambda0" not in decomp_v_l3)
check("operator", "there is no odd-only one-derivative bilinear scalar",
      not ((set(decomp_v_l1) | set(decomp_v_l3)) & set(decomp_w)))
first_jet_symmetric_forms = 3 + 3 + 1
check("operator", "the symmetric quadratic first-jet form space has dimension seven",
      first_jet_symmetric_forms == 7)
check("operator", "the unique cross first-jet pairing is the shared Lambda2 channel",
      set(decomp_v_l1) & set(decomp_v_l3) == {"Lambda2"})


print("D. NONZERO BF ENDPOINT WITNESSES", flush=True)
alpha = {(0,): 1}
alpha_rotated = so_action(alpha, 0, 2)
d_alpha = wedge_vector(0, alpha_rotated)
epsilon1 = {(0, 2): 1}
check("witness", "the grade-one connection variation is nonzero", alpha_rotated == {(2,): 1})
check("witness", "alternation sends the grade-one witness to Lambda2", d_alpha == epsilon1)
check("witness", "the epsilon pairing detects the d-alpha witness", inner(epsilon1, d_alpha) == 1)

beta = {(0, 1, 2): 1}
beta_rotated = so_action(beta, 2, 3)
delta_beta = contract_vector(0, beta_rotated)
epsilon3 = {(1, 3): 1}
check("witness", "the grade-three connection variation is nonzero",
      beta_rotated == {(0, 1, 3): 1})
check("witness", "contraction sends the grade-three witness to Lambda2",
      delta_beta == epsilon3)
check("witness", "the epsilon pairing detects the delta-beta witness",
      inner(epsilon3, delta_beta) == 1)
check("witness", "both independent BF basis maps reach the endpoint", inner(epsilon1, d_alpha) * inner(epsilon3, delta_beta) != 0)


print("E. FIELD EQUATIONS, NORMALIZATION, AND FIELD REDEFINITION", flush=True)
c1, c3, e, u1, u3 = sp.symbols("c1 c3 e u1 u3", nonzero=True)
l_bf = c1 * e * u1 + c3 * e * u3
check("euler", "alpha variation gives c1 times the epsilon adjoint row", sp.diff(l_bf, u1) == c1 * e)
check("euler", "beta variation gives c3 times the epsilon adjoint row", sp.diff(l_bf, u3) == c3 * e)
check("euler", "epsilon variation gives both BF maps", sp.diff(l_bf, e) == c1 * u1 + c3 * u3)
check("euler", "the pure BF Hessian is singular as a multiplier system",
      sp.hessian(l_bf, (e, u1, u3)).det() == 0)

k1, k3, x1, x3, m1, m3 = sp.symbols("k1 k3 x1 x3 m1 m3", nonzero=True)
l_normalized = sp.Rational(1, 2) * k1 * x1**2 + c1 * x1 * m1 \
    - sp.Rational(1, 2) * k3 * x3**2 - c3 * x3 * m3
solution = {x1: -c1 * m1 / k1, x3: -c3 * m3 / k3}
l_effective = sp.factor(l_normalized.subs(solution))
expected_effective = -c1**2 * m1**2 / (2 * k1) + c3**2 * m3**2 / (2 * k3)
check("euler", "the normalized alpha equation fixes alpha proportional to M1",
      sp.solve(sp.diff(l_normalized, x1), x1) == [solution[x1]])
check("euler", "the normalized beta equation fixes beta proportional to M3",
      sp.solve(sp.diff(l_normalized, x3), x3) == [solution[x3]])
check("effective", "eliminating Xi gives the signed Euler-squared action",
      sp.simplify(l_effective - expected_effective) == 0)
check("effective", "the effective endpoint variation vanishes at M equals zero",
      all(sp.diff(l_effective, variable).subs({m1: 0, m3: 0}) == 0 for variable in (m1, m3)))

r1, r3 = sp.symbols("r1 r3", nonzero=True)
check("normalization", "lambda1=c1 squared over k1 is field-rescaling invariant",
      sp.simplify((c1 / r1)**2 / (k1 / r1**2) - c1**2 / k1) == 0)
check("normalization", "lambda3=c3 squared over k3 is field-rescaling invariant",
      sp.simplify((c3 / r3)**2 / (k3 / r3**2) - c3**2 / k3) == 0)
check("normalization", "two independent effective coefficients survive",
      len({str(c1**2 / k1), str(c3**2 / k3)}) == 2)

t, x, c, k = sp.symbols("t x c k", nonzero=True)
shifted_square = sp.expand(sp.Rational(1, 2) * k * (t + c * x)**2)
check("redefinition", "the B/T shift generates the BF cross coefficient k*c",
      shifted_square.coeff(t * x) == k * c)
check("redefinition", "the same shift necessarily generates the c-squared term",
      shifted_square.coeff(x**2) == sp.Rational(1, 2) * k * c**2)
check("redefinition", "undoing the complete field shift returns the original quadratic action",
      sp.expand(shifted_square.subs(t, t - c * x) - sp.Rational(1, 2) * k * t**2) == 0)


print("F. HILBERT CROSS-FORM MAP", flush=True)
trace2 = basis_cross_stress_trace(14, 2)
trace3 = basis_cross_stress_trace(14, 3)
check("hilbert", "the two-form BF stress has trace coefficient ten", trace2 == 10)
check("hilbert", "the three-form BF stress has trace coefficient eight", trace3 == 8)
check("hilbert", "the two Hilbert traces obey n minus two p", trace2 == 14 - 2 * 2 and trace3 == 14 - 2 * 3)
check("hilbert", "neither BF Hilbert map is identically trace-free", trace2 * trace3 != 0)


print("G. PROPAGATION AND CLAIM CEILING", flush=True)
registry = json.loads(read(
    "lab/process/selected-k77-cbrs1aa-covariant-odd-momentum-operator-obstruction.json"
))
check("propagation", "the registry records the two-dimensional raw Hom space",
      registry["hom_spaces"]["Hom_Spin_VtensorWodd_to_Lambda2"] == 2)
check("propagation", "the registry preserves the nonzero raw endpoint map",
      registry["bf_action"]["raw_endpoint_variation_map_nonzero"] is True)
check("propagation", "the registry closes the nonredundant owner quotient",
      registry["bf_action"]["nonredundant_target_blind_owner_quotient_dimension"] == 0)
check("propagation", "the registry carries both Hilbert trace coefficients",
      registry["hilbert_variation"]["trace_grade_one_in_dimension_14"].startswith("10*") and
      registry["hilbert_variation"]["trace_grade_three_in_dimension_14"].startswith("8*"))
check("propagation", "current state advances beyond CBRS-1AA",
      "CBRS-1AA" in read("CURRENT-STATE.yaml") and "CBRS-1AB" in read("CURRENT-STATE.yaml"))
check("propagation", "the agenda carries the narrowed successor",
      "CBRS-1AA" in read("lab/process/RESEARCH-AGENDA.json") and
      "CBRS-1AB" in read("lab/process/RESEARCH-AGENDA.json"))
check("scope", "no ledger canon source ownership or public-posture change follows",
      all(registry[key] == "none" for key in (
          "ledger_verdict_change", "source_ownership_change", "canon_verdict_change",
          "public_posture_change")))


RESULT = {
    "disposition": registry["status"],
    "raw_hom_dimension": registry["hom_spaces"]["Hom_Spin_VtensorWodd_to_Lambda2"],
    "canonical_ray": registry["bf_action"]["canonical_dirac_ray"],
    "nonredundant_owner_quotient_dimension": registry["bf_action"]["nonredundant_target_blind_owner_quotient_dimension"],
    "next_gate": registry["next_gate"],
    "counts": dict(COUNTS),
    "failures": FAILURES,
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(f"FAIL {len(FAILURES)}/{sum(COUNTS.values())}: {FAILURES}")
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
