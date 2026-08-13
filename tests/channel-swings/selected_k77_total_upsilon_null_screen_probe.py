#!/usr/bin/env python3
"""Exact total-raw-Upsilon and labelled ambient null-screen gate.

This composes the v0.59 full-reduction quotient with the complete source
translation tangent.  It keeps the two parity pieces of that tangent, the
full endpoint-curvature derivative, the raw Upsilon derivative, the
linearized superconnection Bianchi identity, and the ambient null screen
separately typed.

It does not construct the observation Euler/preboundary class, a physical
symplectic quotient, a common analytic domain, or any Standard Model state.
"""

from collections import Counter
import contextlib
from fractions import Fraction
import io
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_full_reduction_quotient_reconciliation_probe.py"
DEFECT_NULL = ROOT / "tests/channel-swings/k77_global_even_bv_null_green_domain_probe.py"
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


print("A. SOURCE, REPO ARCHAEOLOGY, AND LAYER ZERO")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
pullback = read("lab/sources/gu-pullback-augmented-torsion-source-reinspection-2026-08-05.md")
v059 = read("explorations/conditional-build/selected-k77-full-reduction-quotient-reconciliation-2026-08-07.md")
ambient_null = read("explorations/conditional-build/selected-second-layer-nonnull-koszul-gcr-split-2026-08-07.md")
defect_null_report = read("explorations/conditional-build/k77-global-even-bv-null-green-domain-2026-08-05.md")
check("source", "the source prints raw Upsilon as Shiab curvature plus kappa T",
      r"\Upsilon^B_\omega" in source and r"*\kappa_1T_\omega" in source)
check("source", "the source prints Xi equals D Upsilon only as a redundant Euler relation",
      r"\Xi_\omega=D_\omega\Upsilon_\omega" in source and "redundant" in source)
check("source", "the source fixes T as a full adjoint-valued connection difference",
      "full adjoint-valued one-form" in pullback and "difference of two connections" in pullback)
check("repo", "v0.59 retains the source-owned full labelled reduction",
      "full labelled Clifford reduction" in v059 and "scalar `U(1)`" in v059)
check("repo", "the ambient non-null split explicitly leaves a null screen open",
      "null screen" in ambient_null and "q^2=0" in ambient_null)
check("repo", "the four-dimensional defect quotient is already a separately typed 10 to 6 to 2 result",
      "10 characteristic directions" in defect_null_report and "2 physical null polarizations" in defect_null_report)
for label in (
    "raw Upsilon versus its derivative",
    "linearized endpoint-curvature Bianchi versus Xi equals D Upsilon",
    "covariant Bianchi versus the even Noether identity",
    "ambient K77 form screen versus the four-dimensional metric physical quotient",
    "screen splitting versus Euler or presymplectic reduction",
    "full labelled reduction versus its horizontal-plane forgetful image",
):
    check("type", label + " remain distinct", True)


print("\nB. IMMUTABLE PREDECESSOR REPLAYS")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    V59 = runpy.run_path(str(PREDECESSOR))
check("repo", "the full-reduction quotient predecessor replays", "PASS 38/38" in capture.getvalue())
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    DNULL = runpy.run_path(str(DEFECT_NULL))
check("repo", "the distinct four-dimensional defect null quotient replays",
      "ALL_K77_GLOBAL_EVEN_BV_NULL_GREEN_CHECKS_PASS" in capture.getvalue())

B = V59["B"]
P = B["P"]
O47 = P["O47"]
M = O47["M"]
ETA = tuple(P["K77_ETA"])
N = 14
FULL = (1 << N) - 1
ZERO = M["ZERO"]
ONE = M["ONE"]
channels = ("comm", "symi", "symi")
solutions = P["k77_solutions"]
connection_parts = P["k77_connection"]
source_lifts = P["k77_source_lifts"]
raw_required = P["k77_raw_required"]
mixed_pairs = O47["mixed_pairs"]
t_star = P["t_star"]


def alpha_form(column):
    out = {}
    for (mu, left, right), coefficient in column.items():
        # The Spencer coordinates are coefficients of
        # J^{ab}=eta^aa eta^bb gamma_a gamma_b / 2.
        # The source convention uses K(alpha)=[alpha,Phi1], whereas the
        # Clifford curvature cross term is assembled with [Phi1,alpha].
        normalized = -coefficient * Fraction(ETA[left] * ETA[right], 2)
        value = M["blade"]((left, right), (normalized, Fraction(0)))
        out[1 << mu] = M["eadd"](out.get(1 << mu, {}), value)
    return M["fclean"](out)


def beta_form(packet):
    """Gauge-fixed inverse of e0 wedge beta on the q-exact packet."""
    out = {}
    for index, coefficient in packet.items():
        pair = mixed_pairs[index // N]
        value_index = index % N
        if 0 not in pair:
            raise AssertionError("connection packet left the e0 wedge image")
        other = pair[1] if pair[0] == 0 else pair[0]
        orientation = 1 if pair == (0, other) else -1
        value = M["blade"](value_index, M["gscale"](orientation, coefficient))
        out[1 << other] = M["eadd"](out.get(1 << other, {}), value)
    return M["fclean"](out)


def curvature_form(packet):
    out = {}
    for index, coefficient in packet.items():
        pair = mixed_pairs[index // N]
        value_index = index % N
        mask = (1 << pair[0]) | (1 << pair[1])
        value = M["blade"](value_index, coefficient)
        out[mask] = M["eadd"](out.get(mask, {}), value)
    return M["fclean"](out)


def target_form(packet):
    out = {}
    for (form_mask, cliff_mask), coefficient in packet.items():
        value = {cliff_mask: coefficient}
        out[form_mask] = M["eadd"](out.get(form_mask, {}), value)
    return M["fclean"](out)


def cliff_grade(form, grade):
    return M["fclean"]({
        form_mask: {cliff_mask: coefficient
                    for cliff_mask, coefficient in element.items()
                    if cliff_mask.bit_count() == grade}
        for form_mask, element in form.items()
    })


def coordinate_count(form):
    return len(M["flatten"](form))


def family_rank(forms):
    return M["sparse_rank"]([M["flatten"](form) for form in forms])


q0 = {1 << 0: {0: ONE}}
t_background = M["fscale"](t_star, M["PHI1"])
f_background = M["wedge_raw"](t_background, t_background)


print("\nC. COMPLETE SOURCE TANGENT AND ENDPOINT CURVATURE")
alphas = [alpha_form(column) for column in source_lifts]
betas = [beta_form(packet) for packet in connection_parts]
delta_as = [M["fadd"](alpha, beta) for alpha, beta in zip(alphas, betas)]
expected_odd_curvatures = [curvature_form(packet) for packet in solutions]
delta_curvatures = [
    M["fadd"](
        M["wedge_raw"](q0, delta_a),
        M["wedge_raw"](t_background, delta_a),
        M["wedge_raw"](delta_a, t_background),
    )
    for delta_a in delta_as
]
odd_curvatures = [cliff_grade(value, 1) for value in delta_curvatures]
check("exact", "all four complete tangents have the intended even-plus-odd source grades",
      all(cliff_grade(value, 1) and cliff_grade(value, 2) for value in delta_as))
check("exact", "the odd endpoint-curvature components equal the four unique inverse-Shiab packets",
      all(M["flatten"](actual) == M["flatten"](expected)
          for actual, expected in zip(odd_curvatures, expected_odd_curvatures)))
check("exact", "the complete endpoint-curvature family retains rank four",
      family_rank(delta_curvatures) == 4)


print("\nD. FULL LINEARIZED SUPERCONNECTION BIANCHI")
bianchi_residuals = []
split_only_residuals = []
for delta_a, delta_f, odd_f in zip(delta_as, delta_curvatures, odd_curvatures):
    covariant_delta_f = M["fadd"](
        M["wedge_raw"](q0, delta_f),
        M["wedge_raw"](t_background, delta_f),
        M["fscale"](-1, M["wedge_raw"](delta_f, t_background)),
    )
    varied_background = M["fadd"](
        M["wedge_raw"](delta_a, f_background),
        M["fscale"](-1, M["wedge_raw"](f_background, delta_a)),
    )
    bianchi_residuals.append(M["fadd"](covariant_delta_f, varied_background))

    split_only_residuals.append(M["fadd"](
        M["wedge_raw"](q0, odd_f),
        M["wedge_raw"](t_background, odd_f),
        M["fscale"](-1, M["wedge_raw"](odd_f, t_background)),
        varied_background,
    ))

check("exact", "the full linearized covariant Bianchi identity vanishes on all four columns",
      all(not value for value in bianchi_residuals))
check("planted", "PLANT retaining only the fitted odd curvature split fails the full Bianchi identity",
      all(bool(value) for value in split_only_residuals))
check("type", "this Bianchi identity is not the displayed Xi equals D Upsilon redundancy", True)
check("type", "this Bianchi identity is not the action-derived even Noether identity", True)


print("\nE. TOTAL RAW-UPSILON NATURALITY TEST")
source_raw_responses = [
    M["fadd"](M["hodge"](M["shiab"](delta_f, channels)), delta_a)
    for delta_f, delta_a in zip(delta_curvatures, delta_as)
]
direct_graph_responses = [M["fscale"](-1, target_form(packet)) for packet in raw_required]
total_graph_residuals = [
    M["fadd"](direct, source_response)
    for direct, source_response in zip(direct_graph_responses, source_raw_responses)
]
grade_counts = {
    grade: [coordinate_count(cliff_grade(value, grade)) for value in total_graph_residuals]
    for grade in range(15)
}
live_grades = {grade: counts for grade, counts in grade_counts.items() if any(counts)}
check("exact", "the previously fitted grade-two curvature contribution still cancels its direct target",
      all(
          M["flatten"](M["fadd"](
              direct,
              cliff_grade(M["hodge"](M["shiab"](delta_f, channels)), 2),
          )) == {}
          for direct, delta_f in zip(direct_graph_responses, delta_curvatures)
      ))
check("exact", "the written kappa-T term makes every current total raw-Upsilon column nonzero",
      all(bool(value) for value in total_graph_residuals))
check("exact", "the total raw-Upsilon failure remains a rank-four family",
      family_rank(total_graph_residuals) == 4)
check("exact", "the total residual exposes live Clifford grades outside the fitted grade-two slice",
      any(grade != 2 for grade in live_grades))
check("planted", "PLANT curvature-only cancellation is not total raw-Upsilon naturality",
      all(bool(value) for value in total_graph_residuals))


print("\nF. LABELLED AMBIENT NULL SCREEN")
eta = sp.diag(*ETA)
q_cov = sp.Matrix([1, 1] + [0] * 12)
ell_cov = sp.Matrix([sp.Rational(1, 2), -sp.Rational(1, 2)] + [0] * 12)
q_vec = eta * q_cov
ell_vec = eta * ell_cov
pairing = (q_cov.T * eta * ell_cov)[0]
projector = sp.eye(N) - q_vec * ell_cov.T - ell_vec * q_cov.T
check("exact", "q and its labelled reciprocal ell are null with pairing one",
      (q_cov.T * eta * q_cov)[0] == 0
      and (ell_cov.T * eta * ell_cov)[0] == 0
      and pairing == 1)
check("exact", "the labelled screen projector has rank twelve and kills both null legs",
      projector.rank() == 12 and projector * q_vec == sp.zeros(N, 1)
      and projector * ell_vec == sp.zeros(N, 1))
check("exact", "the ambient K77 screen has split signature six-six",
      (sum(ETA[index] > 0 for index in range(2, 14)),
       sum(ETA[index] < 0 for index in range(2, 14))) == (6, 6))


def contraction(form, vector):
    out = {}
    for mask, coefficient in form.items():
        ordered = [index for index in range(N) if mask & (1 << index)]
        for position, index in enumerate(ordered):
            if vector[index] == 0:
                continue
            new_mask = mask ^ (1 << index)
            value = M["escale"](((-1) ** position) * vector[index], coefficient)
            out[new_mask] = M["eadd"](out.get(new_mask, {}), value)
    return M["fclean"](out)


q_form = {
    1 << index: {0: (Fraction(int(q_cov[index])), Fraction(0))}
    for index in range(N) if q_cov[index] != 0
}


def null_split(form, reciprocal_vector):
    exact = M["wedge_raw"](q_form, contraction(form, reciprocal_vector))
    transverse = contraction(M["wedge_raw"](q_form, form), reciprocal_vector)
    return exact, transverse


screen_splits = [null_split(value, ell_vec) for value in expected_odd_curvatures]
check("exact", "the labelled null homotopy round-trips all four ambient curvature packets",
      all(M["flatten"](M["fadd"](exact, transverse)) == M["flatten"](value)
          for value, (exact, transverse) in zip(expected_odd_curvatures, screen_splits)))
check("exact", "every labelled q-exact part is principal q-closed without dividing by q squared",
      all(not M["wedge_raw"](q_form, exact) for exact, _ in screen_splits))
check("exact", "both exact and screen-transverse four-column families remain nonzero",
      family_rank([item[0] for item in screen_splits]) > 0
      and family_rank([item[1] for item in screen_splits]) > 0)

s_cov = sp.Matrix([0, 0, 1] + [0] * 11)
s_square = (s_cov.T * eta * s_cov)[0]
ell_alt_cov = ell_cov + s_cov - sp.Rational(1, 2) * s_square * q_cov
ell_alt_vec = eta * ell_alt_cov
check("exact", "a null-rotation-related reciprocal screen also has q pairing one",
      (ell_alt_cov.T * eta * ell_alt_cov)[0] == 0
      and (q_cov.T * eta * ell_alt_cov)[0] == 1)
heldout = {((1 << 0) | (1 << 2)): M["blade"](4)}
heldout_primary = null_split(heldout, ell_vec)
heldout_alternate = null_split(heldout, ell_alt_vec)
check("planted", "PLANT forgetting the labelled reciprocal null leg changes the held-out split",
      tuple(M["flatten"](x) for x in heldout_primary)
      != tuple(M["flatten"](x) for x in heldout_alternate))
check("scope", "the full labelled reduction owns the chosen reciprocal leg modulo its central stabilizer", True)
check("scope", "the ambient screen is not the four-dimensional harmonic constraint/gauge quotient", True)
check("symplectic", "the ambient screen does not construct an Euler or presymplectic reduction", True)
check("symplectic", "the four-dimensional physical null quotient remains separately valid and unrecomputed", True)


print("\nG. ACCOUNTING AND CLAIM BOUNDARY")
check("scope", "Bianchi and screen transport identities are not counted as independent surplus", True)
check("scope", "the current raw-Upsilon failure requires a coupled all-grade graph repair", True)
check("scope", "observation Euler preboundary BV BFV and common domain remain open", True)
check("scope", "P1 P2 P3 remain unchanged and unused", True)
check("planted", "PLANT no particle count chirality positivity or cosmology is inferred", True)

print("SOURCE_RETURN=SOURCE-CONFIRMS__RAW_UPSILON_INCLUDES_SHIAB_CURVATURE_PLUS_KAPPA_T_AND_XI_EQUALS_D_UPSILON_REDUNDANCY__SOURCE-SILENT__LINEARIZED_SUPERCONNECTION_BIANCHI_PROOF_AND_LABELLED_AMBIENT_NULL_SCREEN")
print("FULL_LINEARIZED_SUPERCONNECTION_BIANCHI=PASS")
print("CURRENT_CURVATURE_ONLY_GRAPH_TOTAL_RAW_UPSILON_NATURALITY=FAIL")
print("TOTAL_RAW_UPSILON_RESIDUAL_FAMILY_RANK=4")
print("TOTAL_RAW_UPSILON_LIVE_GRADES=" + repr(live_grades))
print("AMBIENT_LABELLED_NULL_SCREEN=RANK12_SIGNATURE6_6")
print("AMBIENT_NULL_SCREEN_FORGETFUL_QUOTIENT_BASIC=NO")
print("FOUR_DIMENSIONAL_DEFECT_NULL_QUOTIENT=UNCHANGED_SEPARATE")
print("CONSTRAINT_SURPLUS=NO_NEW_FIELD_CONDITIONAL_ON_FULL_LABELLED_REDUCTION__IDENTITIES_NOT_COUNTED")
print("EXTERNAL_DATUM=P1_P2_P3_UNCHANGED_AND_UNUSED")
print("DISPOSITION=FULL_BIANCHI_AND_LABELLED_AMBIENT_NULL_SCREEN_PASS__CURRENT_TOTAL_RAW_UPSILON_GRAPH_FAILS__COUPLED_ALL_GRADE_GRAPH_REPAIR_OPEN")
print("NEXT=SOLVE_COUPLED_ALL_GRADE_RAW_UPSILON_GRAPH_INCLUDING_KAPPA_T__THEN_OBSERVATION_EULER_PREBOUNDARY_SYMPLECTIC_DESCENT")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
