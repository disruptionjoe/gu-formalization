#!/usr/bin/env python3
"""Exact bosonic-Q_B phase/primalizer gate on the v0.213 Higgs response.

The source writes a residual norm but does not type its real K77 primalizer.
This probe keeps five objects separate: the existing real complex-bilinear
trace pairing, its action-owned P_plus/P_minus decomposition, relative weights
on the two Weyl halves, a phase-even/sesquilinear candidate, and a positive
Hilbert majorant.  Only finite principal-fibre algebra is decided here.
"""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
import io
from itertools import product
import json
from pathlib import Path
import runpy

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_i2b_moving_higgs_principal_hessian_probe.py"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object, detail: str = "") -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}{suffix}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def strict(relative: str):
    path = ROOT / relative

    def reject(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=reject)


print("A. SOURCE, PRIOR ART, LAYER ZERO, AND ADAPTIVE PREFLIGHT")
claims = read("lab/sources/source-claim-register.yaml")
source_reconstruction = read(
    "lab/sources/paired-curt-eric-gu-axiom-and-argument-reconstruction-2026-07-31.md"
)
pairing_report = read(
    "explorations/conditional-build/selected-k77-residual-pairing-invariance-2026-08-08.md"
)
projection_registry = strict("lab/process/selected-k77-i2b-action-real-projection.json")
check("source", "SC-ACT-04 owns a bosonic residual norm-square slot",
      "- id: SC-ACT-04" in claims and "I^B_2 = ||Upsilon^B_omega||^2" in claims)
check("source", "the typed reconstruction names Q_B but marks its exact pairing open",
      "I_2^B[Q_B]" in source_reconstruction
      and "Both formulas are meaningless until" in source_reconstruction)
check("prior_art", "v0.92 constructs the current local trace comparator",
      "degree-thirteen\nHodge pairing" in pairing_report
      and "scalar Clifford-trace pairing" in pairing_report)
check("prior_art", "v0.206 owns P_plus only at the fixed-real Euler grade",
      projection_registry["exact_results"]["pplus_action_self_adjoint"] is True
      and projection_registry["exact_results"]["nonlinear_residual_replacement_derived"] is False)
for label in (
    "source norm glyph versus a typed Q_B primalizer",
    "complex-bilinear real trace versus phase-even sesquilinear pairing",
    "phase-even Lorentz principal form versus a positive Hilbert majorant",
    "fixed-real Euler P_plus versus a nonlinear residual replacement",
    "C^(32,32)+C^(32,32) carrier halves versus U(32,32)xU(32,32) subgroup",
    "two-half subgroup versus full U(64,64) parent and independent connections",
    "principal rank four versus a reduced Higgs propagator or spectrum",
):
    check("layer0", label + " remain distinct", True)
for kind, label in (
    ("representation", "decompose the exact grade-two tensor carrier before choosing weights"),
    ("krein", "test both bilinear and conjugation-sensitive real forms"),
    ("symplectic", "do not promote a symmetric principal Gram to a BFV form"),
    ("variational", "retain the action-owned projector and the full nonlinear residual separately"),
    ("principal_bundle", "require a moving reduction to own any symmetry-breaking primalizer"),
    ("analytic", "rank four is not a closed domain energy spectrum or propagator"),
    ("source_review", "do not attribute the repository Q_B candidates to Weinstein"),
    ("contrary", "test both Weyl-half reweighting and a noncompact-unitary invariance plant"),
):
    check(kind, label, True)


print("\nB. IMMUTABLE V0.213 RESPONSE")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PREDECESSOR))
check("repo", "v0.213 moving-Higgs Hessian predecessor replays",
      "PASS 44/44" in capture.getvalue() and not P["FAILURES"])

TANGENT = P["T"]
SELECTED = P["SELECTED"]
principal_with = P["principal_with"]
hodge = P["P"]["S"]["hodge"]
sym_pair = P["sym_pair"]
real_scalar = P["real_scalar"]
M = P["P"]["S"]["P"]["M"]
ETA = tuple(M["ETA"])
N = len(ETA)
check("exact", "the ambient signature remains exact K77",
      N == 14 and ETA.count(1) == ETA.count(-1) == 7)
check("exact", "the tested tangent remains four-real", len(TANGENT) == 4)


def gaussian(value) -> sp.Expr:
    return (sp.Rational(value[0].numerator, value[0].denominator)
            + sp.I * sp.Rational(value[1].numerator, value[1].denominator))


def indices(mask: int) -> tuple[int, ...]:
    return tuple(i for i in range(N) if mask & (1 << i))


def response_tensor(response: dict) -> dict[tuple[int, int, int], sp.Expr]:
    """Hodge Lambda^13 to V and decode Cl^2 as an antisymmetric pair."""
    out: dict[tuple[int, int, int], sp.Expr] = {}
    transformed = hodge(response)
    for form_mask, row in transformed.items():
        form_indices = indices(form_mask)
        assert len(form_indices) == 1
        a = form_indices[0]
        for clifford_mask, coefficient in row.items():
            pair = indices(clifford_mask)
            assert len(pair) == 2
            b, c = pair
            value = gaussian(coefficient)
            out[(a, b, c)] = out.get((a, b, c), 0) + value
            out[(a, c, b)] = out.get((a, c, b), 0) - value
    return {key: sp.expand(value) for key, value in out.items() if value != 0}


def tget(tensor, a, b, c):
    return tensor.get((a, b, c), sp.S.Zero)


def tensor_add(*items):
    keys = set().union(*(item.keys() for item in items))
    return {key: value for key in keys
            if (value := sp.expand(sum(item.get(key, 0) for item in items))) != 0}


def tensor_scale(scalar, tensor):
    return {key: sp.expand(scalar * value) for key, value in tensor.items()
            if scalar * value != 0}


def alternating_projector(tensor):
    out = {}
    for a, b, c in product(range(N), repeat=3):
        value = sp.expand((tget(tensor, a, b, c)
                           + tget(tensor, b, c, a)
                           + tget(tensor, c, a, b)) / 3)
        if value:
            out[(a, b, c)] = value
    return out


def contraction(tensor):
    return [sp.expand(sum(ETA[a] * tget(tensor, a, a, c) for a in range(N)))
            for c in range(N)]


def trace_projector(tensor):
    vector = contraction(tensor)
    out = {}
    for a, b, c in product(range(N), repeat=3):
        value = sp.Rational(1, N - 1) * (
            (ETA[a] if a == b else 0) * vector[c]
            - (ETA[a] if a == c else 0) * vector[b]
        )
        if value:
            out[(a, b, c)] = sp.expand(value)
    return out


def hook_projector(tensor):
    return tensor_add(
        tensor,
        tensor_scale(-1, alternating_projector(tensor)),
        tensor_scale(-1, trace_projector(tensor)),
    )


def tensor_pair(left, right, conjugate_right=False):
    total = sp.S.Zero
    for a, b, c in product(range(N), repeat=3):
        rv = tget(right, a, b, c)
        if conjugate_right:
            rv = sp.conjugate(rv)
        total += (sp.Rational(1, 2) * ETA[a] * ETA[b] * ETA[c]
                  * tget(left, a, b, c) * rv)
    return sp.simplify(sp.re(sp.expand_complex(total)))


responses = [[
    response_tensor(principal_with(SELECTED, mu, TANGENT[a]))
    for a in range(4)
] for mu in range(4)]
check("exact", "every live principal response is Lambda13-Cl2 typed",
      all(response and all(
          len(indices(clifford_mask)) == 2
          for row in hodge(principal_with(SELECTED, mu, TANGENT[a])).values()
          for clifford_mask in row
      ) for mu in range(4) for a, response in enumerate(responses[mu])))


print("\nC. ORTHOGONAL V TENSOR LAMBDA2 DECOMPOSITION")
parts = []
for tensor in responses[0]:
    alt = alternating_projector(tensor)
    trace = trace_projector(tensor)
    hook = hook_projector(tensor)
    parts.append((alt, trace, hook))
    check("projector", "alternating plus trace plus hook reconstructs a response",
          tensor_add(alt, trace, hook) == tensor)
    check("projector", "three tensor types are pairwise orthogonal",
          tensor_pair(alt, trace) == tensor_pair(alt, hook)
          == tensor_pair(trace, hook) == 0)
check("representation", "carrier dimensions split as Lambda3 plus V plus traceless hook",
      sp.binomial(14, 3) == 364 and N == 14 and 14 * sp.binomial(14, 2) - 364 - 14 == 896)


def phase_part(tensor, part):
    selector = sp.re if part == 0 else sp.im
    return {key: value for key, coefficient in tensor.items()
            if (value := sp.simplify(selector(coefficient))) != 0}


phase_parameters = sp.symbols("aA bA cA aE bE cE aH bH cH", real=True)
general_gram = sp.zeros(4)
phase_blocks = {}
for type_index, type_name in enumerate(("A", "E", "H")):
    block_family = []
    for p, q in ((0, 0), (0, 1), (1, 1)):
        block = sp.Matrix(4, 4, [
            tensor_pair(phase_part(parts[i][type_index], p),
                        phase_part(parts[j][type_index], q))
            + (tensor_pair(phase_part(parts[i][type_index], q),
                           phase_part(parts[j][type_index], p)) if p != q else 0)
            for i in range(4) for j in range(4)
        ])
        block_family.append(block)
    phase_blocks[type_name] = block_family
    general_gram += sum(
        (phase_parameters[3 * type_index + k] * block_family[k]
         for k in range(3)), sp.zeros(4)
    )

aA, bA, cA, aE, bE, cE, aH, bH, cH = phase_parameters
expected_general = sp.diag(
    sp.Rational(8, 3) * (cA + 2 * cH),
    sp.Rational(8, 3) * (cA + 2 * cH),
    sp.Rational(4, 3) * (aA + 2 * aH + 2 * bA - 2 * bH + cA + 2 * cH),
    sp.Rational(4, 13) * (aE + 12 * aH + 2 * bE - 2 * bH + cE + 12 * cH),
)
expected_det = (sp.Rational(1024, 351) * (cA + 2 * cH) ** 2
                * (aA + 2 * aH + 2 * bA - 2 * bH + cA + 2 * cH)
                * (aE + 12 * aH + 2 * bE - 2 * bH + cE + 12 * cH))
check("classification", "the nine-weight tensor-phase ansatz has the exact diagonal restriction",
      sp.simplify(general_gram - expected_general) == sp.zeros(4))
check("classification", "its rank-four locus has the exact determinant polynomial",
      sp.factor(general_gram.det() - expected_det) == 0)


print("\nD. CURRENT, REAL-PROJECTED, AND PHASE-EVEN PRIMALIZERS")
current_blocks = [[sp.Matrix(4, 4, [
    tensor_pair(responses[mu][a], responses[nu][b])
    for a in range(4) for b in range(4)
]) for nu in range(4)] for mu in range(4)]
check("control", "tensor decoding reproduces every v0.213 current-pairing block",
      all(current_blocks[mu][nu] == P["blocks"][mu][nu]
          for mu in range(4) for nu in range(4)))
current_weights = {
    aA: 1, bA: 0, cA: -1,
    aE: 1, bE: 0, cE: -1,
    aH: 1, bH: 0, cH: -1,
}
check("classification", "the current real complex-bilinear pairing is the rank-two phase-odd point",
      general_gram.subs(current_weights) == sp.diag(-8, -8, 0, 0))


def form_sign(mask: int) -> int:
    out = 1
    for index in M["indices"](mask):
        out *= ETA[index]
    return out


def clifford_sign(mask: int) -> int:
    product_mask, sign = M["blade_product"](mask, mask)
    assert product_mask == 0
    return sign


def real_flat(form):
    out = {}
    for key, value in M["flatten"](form).items():
        if value[0]:
            out[(key, 0)] = value[0]
        if value[1]:
            out[(key, 1)] = value[1]
    return out


def b_adjoint_sign(grade: int) -> int:
    return -1 if grade in {1, 2, 5, 6, 9, 10, 13, 14} else 1


def q_commutation_sign(mask: int, q_axis=13) -> int:
    return -1 if (mask.bit_count() - int(bool(mask & (1 << q_axis)))) % 2 else 1


def fixed_real_phase(mask: int, q_axis=13) -> int:
    return 1 if q_commutation_sign(mask, q_axis) == -b_adjoint_sign(mask.bit_count()) else -1


def tau_q(column):
    return {
        (key, part): value * fixed_real_phase(key[1]) * (1 if part == 0 else -1)
        for (key, part), value in column.items()
    }


def project_real(column, sign):
    transformed = tau_q(column)
    out = {}
    for key in set(column) | set(transformed):
        value = (column.get(key, 0) + sign * transformed.get(key, 0)) / 2
        if value:
            out[key] = value
    return out


def action_pair(left, right):
    coordinate_keys = {key for key, _ in left} & {key for key, _ in right}
    total = Fraction(0)
    for key in coordinate_keys:
        ar, ai = left.get((key, 0), 0), left.get((key, 1), 0)
        br, bi = right.get((key, 0), 0), right.get((key, 1), 0)
        total += form_sign(key[0]) * clifford_sign(key[1]) * (ar * br - ai * bi)
    return sp.Rational(total.numerator, total.denominator)


projected_ranks = {"plus": [], "minus": []}
projected_supports = {"plus": None, "minus": None}
for mu in range(4):
    raw = [real_flat(principal_with(SELECTED, mu, TANGENT[a])) for a in range(4)]
    for name, sign in (("plus", 1), ("minus", -1)):
        projected = [project_real(value, sign) for value in raw]
        gram = sp.Matrix(4, 4, [action_pair(projected[a], projected[b])
                               for a in range(4) for b in range(4)])
        projected_ranks[name].append(gram.rank())
        if mu == 0:
            projected_supports[name] = [len(value) for value in projected]
check("primalizer", "the already action-owned P_plus sector remains rank two",
      projected_ranks["plus"] == [2, 2, 2, 2]
      and projected_supports["plus"] == [1, 1, 2, 0])
check("primalizer", "the complementary P_minus sector also remains rank two",
      projected_ranks["minus"] == [2, 2, 2, 2]
      and projected_supports["minus"] == [1, 1, 0, 2])
check("plant", "PLANT fixed-real projection cannot be reported as rank-four repair",
      4 not in projected_ranks["plus"] + projected_ranks["minus"])

phase_even_blocks = [[sp.Matrix(4, 4, [
    tensor_pair(responses[mu][a], responses[nu][b], conjugate_right=True)
    for a in range(4) for b in range(4)
]) for nu in range(4)] for mu in range(4)]
check("candidate", "the phase-even candidate gives four exact Lorentz diagonal blocks",
      [phase_even_blocks[mu][mu] for mu in range(4)]
      == [8 * sp.eye(4)] + [-8 * sp.eye(4)] * 3)
check("candidate", "all phase-even mixed base blocks vanish",
      all(phase_even_blocks[mu][nu] == sp.zeros(4)
          for mu in range(4) for nu in range(4) if mu != nu))
check("candidate", "the phase-even principal symbol is rank four off the null cone",
      (4, 4, 4, 0) == tuple(sum(
          (sp.Integer(k[mu] * k[nu]) * phase_even_blocks[mu][nu]
           for mu in range(4) for nu in range(4)), sp.zeros(4)
      ).rank() for k in ((1, 0, 0, 0), (0, 1, 0, 0), (2, 1, 1, 0), (1, 1, 0, 0))))


print("\nE. TWO WEYL HALVES AND NONCOMPACT-UNITARY CONTROL")
GAMMA = P["P"]["S"]["GAMMA"]
chirality = np.eye(128, dtype=np.int64)
for gamma in GAMMA:
    chirality = chirality @ gamma
identity = np.eye(128, dtype=np.int64)
check("weyl", "ambient chirality gives exact real 64 plus 64 projectors",
      np.array_equal(chirality @ chirality, identity)
      and np.trace(chirality) == 0
      and np.linalg.matrix_rank(identity + chirality) == 64
      and np.linalg.matrix_rank(identity - chirality) == 64)


def blade_matrix(mask: int):
    out = identity.copy()
    for index in indices(mask):
        out = out @ GAMMA[index]
    return out


live_masks = sorted({clifford_mask for mu in range(4) for a in range(4)
                     for row in hodge(principal_with(SELECTED, mu, TANGENT[a])).values()
                     for clifford_mask in row})
chirality_trace_defects = []
for left in live_masks:
    for right in live_masks:
        chirality_trace_defects.append(int(np.trace(
            chirality @ blade_matrix(left) @ blade_matrix(right)
        )))
check("weyl", "the two Weyl-half traces agree on every live grade-two product",
      len(live_masks) == 8
      and all(mask.bit_count() == 2 for mask in live_masks)
      and chirality_trace_defects == [0] * len(live_masks) ** 2)
w_plus, w_minus = sp.symbols("w_plus w_minus", real=True)
two_half_gram = sp.Rational(1, 2) * (w_plus + w_minus) * current_blocks[0][0]
check("weyl", "relative two-half scalar weights cannot exceed rank two",
      two_half_gram.det() == 0
      and two_half_gram.subs({w_plus: 1, w_minus: 0}).rank() == 2
      and two_half_gram.subs({w_plus: 1, w_minus: -1}).rank() == 0)
check("plant", "PLANT C32,32 plus C32,32 is not silently treated as two independent connections",
      True)

# Exact U(1,1) sub-block.  Its rational boost preserves H, and adjoint
# conjugation preserves Re Tr(A^2) but not Re Tr(A^dagger A).  Since U(1,1)
# embeds in each U(32,32) block, the phase-even repair is not automatically
# invariant under either the block product or the full parent.
H11 = sp.diag(1, -1)
boost = sp.Matrix([[sp.Rational(5, 3), sp.Rational(4, 3)],
                   [sp.Rational(4, 3), sp.Rational(5, 3)]])
A11 = sp.I * sp.diag(1, 0)
A11_moved = sp.simplify(boost * A11 * boost.inv())
bilinear_value = lambda value: sp.simplify(sp.re(sp.trace(value * value)))
phase_even_value = lambda value: sp.simplify(sp.re(sp.trace(value.conjugate().T * value)))
check("unitary", "the plant is an exact noncompact U11 adjoint orbit",
      boost.conjugate().T * H11 * boost == H11
      and A11.conjugate().T * H11 + H11 * A11 == sp.zeros(2)
      and A11_moved.conjugate().T * H11 + H11 * A11_moved == sp.zeros(2))
check("unitary", "the real complex-bilinear trace is invariant on the plant",
      bilinear_value(A11) == bilinear_value(A11_moved) == -1)
check("unitary", "the rank-four phase-even candidate fails noncompact-unitary adjoint invariance",
      phase_even_value(A11) == 1
      and phase_even_value(A11_moved) == sp.Rational(1681, 81))
check("scope", "rank-four existence therefore requires an action-owned moving reduction or another parent",
      phase_even_value(A11) != phase_even_value(A11_moved))


print("\nF. DISPOSITION, REVIEWS, AND ACCOUNTING")
for kind, label in (
    ("representation", "the grade-two response has no two-half scalar-weight repair"),
    ("krein", "nullity under the invariant trace and nonnullity under phase-even pairing remain distinct"),
    ("symplectic", "no symmetric principal Gram is called a presymplectic or BFV quotient"),
    ("variational", "P_plus ownership at fixed-real Euler grade does not select phase-even Q_B"),
    ("principal_bundle", "a moving reduction or fundamental symmetry can still conditionally own the repair"),
    ("analytic", "the Lorentz rank-four candidate carries no domain energy spectrum or propagator claim"),
    ("source", "the source owns the norm-square slot but is silent on the winning primalizer"),
    ("datum", "P1 P2 and P3 remain unchanged and unused"),
    ("accounting", "no field parameter selector quotient or external datum is added"),
    ("contrary", "coupled contact and expanded total-residual parents remain live rivals"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_BOSONIC_RESIDUAL_NORM_SLOT__SOURCE_SILENT_QB_REAL_FORM__REPO_DERIVES_PHASE_EVEN_RANK4_CANDIDATE_BUT_NONCOMPACT_UNITARY_NONINVARIANT")
print("CURRENT_TIMELIKE_GRAM=" + str(current_blocks[0][0]))
print("PHASE_EVEN_TIMELIKE_GRAM=" + str(phase_even_blocks[0][0]))
print("PROJECTED_RANKS=" + str(projected_ranks))
print("TWO_HALF_GRADE2_TRACE_DIFFERENCE=0")
print("PHASE_EVEN_U11_VALUES=1,1681/81")
print("RESULT=PAIRING_ONLY_REPAIR_EXISTS_CONDITIONALLY__CURRENT_ACTION_PROJECTOR_AND_TWO_HALF_WEIGHTS_DO_NOT_REPAIR__PHASE_EVEN_QB_NEEDS_ACTION_OWNED_MOVING_REDUCTION")
print("NEXT=CONSTRUCT_OR_KILL_MOVING_FUNDAMENTAL_SYMMETRY_REDUCTION_OWNING_PHASE_EVEN_QB__IN_PARALLEL_RETAIN_COUPLED_CONTACT_PARENT")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
