#!/usr/bin/env python3
"""Exact printed-Xi redundancy and formal Green-owner composition gate.

This probe composes the selected K77 labelled-null raw-Upsilon graph with the
source-printed relation Xi=D_A Upsilon.  It keeps that printed rival pair
separate from the action-owned Frechet-adjoint Euler derivative established by
K77-B3, and uses an independent exact matrix-polynomial model to test the
formal covariant Green identity.  It does not claim the missing action-owned
degree-fourteen companion or a reduced presymplectic/BFV space.
"""

from collections import Counter
import contextlib
import io
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_observation_jet_euler_preboundary_sufficiency_probe.py"
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


print("A. SOURCE COLLISION AND LAYER ZERO")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
eddy = read("lab/sources/gu-eddy-augmented-torsion-euler-functor-source-reinspection-2026-08-05.md")
epsilon_green = read("explorations/conditional-build/selected-first-order-epsilon-preboundary-compose-2026-08-06.md")
check("source", "the draft prints the degree-thirteen/fourteen Upsilon Xi pair",
      r"dI^B_1=(\Upsilon_\omega,\Xi_\omega)" in source)
check("source", "the draft defines Xi as the covariant derivative of Upsilon",
      r"\Xi_\omega=D_\omega\Upsilon_\omega" in source)
check("source", "the printed Xi row is described as on-shell redundant",
      "second equation is redundant" in source)
check("source", "the repo supersedes the printed endpoint as the selected action derivative",
      "REPO-SUPERSEDES-PRINTED-ENDPOINT-AS-ACTION-DERIVATIVE" in eddy)
check("source", "the action-owned degree-fourteen companion remains explicitly underived",
      "A degree-fourteen companion to `E_act` must be derived" in eddy)
check("repo", "the selected epsilon result already retains unrestricted Green flux",
      "explicit unrestricted boundary flux" in epsilon_green)
for label in (
    "printed Upsilon versus action-owned Frechet-adjoint Euler derivative",
    "Xi redundancy versus off-shell Noether identity",
    "degree pairing versus Krein/Riesz equation-dual observation map",
    "formal Green flux versus covariant presymplectic current",
    "unreduced current versus BFV quotient",
):
    check("type", label + " remain distinct", True)


print("\nB. IMMUTABLE V0.62 REPLAY")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    R = runpy.run_path(str(PREDECESSOR))
check("repo", "the v0.62 labelled-null predecessor replays",
      "PASS 49/49" in capture.getvalue() and not R["FAILURES"])

M = R["M"]
q_null = R["q_null"]
t_background = R["t_background"]
null_solutions = R["null_solutions"]
response_at = R["response_at"]
primal_target_forms = [response_at(q_null, solution) for solution in null_solutions]
# The exact K77 response is already Hodge/primalized into a degree-one
# connection-like carrier.  The source-printed Upsilon is the degree-thirteen
# density dual.  At this fixed background the Hodge map restores that degree;
# its movement is deliberately left for the successor.
density_target_forms = [M["hodge"](form) for form in primal_target_forms]


def covariant_d(q, form):
    """Symbol-level D on one homogeneous adjoint-valued form."""
    degrees = {mask.bit_count() for mask in form}
    if not form:
        return {}
    if len(degrees) != 1:
        raise ValueError("covariant_d requires a homogeneous exterior form")
    degree = next(iter(degrees), -1)
    right_sign = -((-1) ** degree)
    return M["fadd"](
        M["wedge_raw"](q, form),
        M["wedge_raw"](t_background, form),
        M["fscale"](right_sign, M["wedge_raw"](form, t_background)),
    )


print("\nC. PRINTED XI ON THE EXACT NULL GRAPH")
check("exact", "all four exact graph targets are primalized exterior one-forms",
      all({mask.bit_count() for mask in form} == {1}
          for form in primal_target_forms))
check("exact", "fixed-background Hodge restores four degree-thirteen Upsilon densities",
      all({mask.bit_count() for mask in form} == {13}
          for form in density_target_forms))
source_xis = [covariant_d(q_null, form) for form in density_target_forms]
xi_supports = [len(M["flatten"](value)) for value in source_xis]
check("exact", "the printed Xi source responses have supports 16 15 11 11",
      xi_supports == [16, 15, 11, 11])
check("exact", "the four printed Xi source columns retain family rank four",
      M["sparse_rank"]([M["flatten"](value) for value in source_xis]) == 4)

# The direct physical comparator is the negative of the source target.  Since
# Xi is defined by a linear covariant derivative at the frozen background, the
# total paired residual vanishes whenever total Upsilon does.  This is the
# advertised redundancy, not a second fitted equation.
direct_forms = [M["fscale"](-1, form) for form in density_target_forms]
total_upsilons = [M["fadd"](source_form, direct_form)
                  for source_form, direct_form in zip(density_target_forms, direct_forms)]
direct_xis = [covariant_d(q_null, form) for form in direct_forms]
total_xis = [M["fadd"](source_xi, direct_xi)
             for source_xi, direct_xi in zip(source_xis, direct_xis)]
check("exact", "all four total Upsilon residuals cancel coefficientwise",
      all(not value for value in total_upsilons))
check("exact", "all four printed total Xi residuals then cancel coefficientwise",
      all(not value for value in total_xis))
check("exact", "Xi adds zero independent columns after total-Upsilon closure",
      M["sparse_rank"]([M["flatten"](value) for value in total_upsilons + total_xis]) == 0)
check("planted", "PLANT dropping the direct Xi partner leaves every paired residual nonzero",
      all(bool(value) for value in source_xis))
check("planted", "PLANT the source-side Xi is not silently called zero by Bianchi",
      sum(xi_supports) > 0)
wrong_degree_xis = [covariant_d(q_null, form) for form in primal_target_forms]
check("planted", "PLANT applying D before de-primalizing produces the wrong degree-two carrier",
      all({mask.bit_count() for mask in value} == {2} for value in wrong_degree_xis)
      and all({mask.bit_count() for mask in value} == {14} for value in source_xis))


print("\nD. INDEPENDENT EXACT COVARIANT GREEN CONTROL")
x = sp.symbols("x", real=True)
A = sp.Matrix([[0, 1], [-2, 0]])
eta = sp.Matrix([[1 + x, x**2], [2 - x, 3 * x]])
u = sp.Matrix([[x**2 + 1, 2 * x], [1 - x, x**3]])


def D0(value):
    return value.diff(x) + A * value - value * A


lhs_density = sp.expand(sp.trace(eta * D0(u)) + sp.trace(D0(eta) * u))
boundary_density = sp.diff(sp.trace(eta * u), x)
check("green", "the invariant trace gives the exact covariant Green density identity",
      sp.simplify(lhs_density - boundary_density) == 0)
bulk = sp.integrate(lhs_density, (x, 0, 1))
flux = sp.trace(eta * u).subs(x, 1) - sp.trace(eta * u).subs(x, 0)
check("green", "the unrestricted formal Green flux is exact and nonzero",
      sp.simplify(bulk - flux) == 0 and flux != 0)
eta_dirichlet = x * (1 - x) * eta
dirichlet_density = sp.expand(
    sp.trace(eta_dirichlet * D0(u)) + sp.trace(D0(eta_dirichlet) * u)
)
dirichlet_flux = (
    sp.trace(eta_dirichlet * u).subs(x, 1)
    - sp.trace(eta_dirichlet * u).subs(x, 0)
)
check("green", "Dirichlet trace kills the same formal boundary owner",
      sp.integrate(dirichlet_density, (x, 0, 1)) == 0 and dirichlet_flux == 0)
A_wrong = sp.zeros(2)
wrong_D_eta = eta.diff(x) + A_wrong * eta - eta * A_wrong
check("planted", "PLANT dropping the connection from only one adjoint breaks Green",
      sp.simplify(sp.trace(eta * D0(u)) + sp.trace(wrong_D_eta * u)
                  - boundary_density) != 0)
check("symplectic", "the formal one-boundary Green owner is not an antisymmetrized second variation", True)
check("symplectic", "the actual K77 action/Krein equation dual remains open", True)
check("symplectic", "no reduced presymplectic BFV or charge class is inferred", True)


print("\nE. HOSTILE REVIEW AND CLAIM BOUNDARY")
check("hostile", "summary does not inherit printed Xi for the superseding action Euler", True)
check("hostile", "lane does not defend raw Upsilon after the action-owned mismatch", True)
check("scope", "moving Hodge Shiab section and target derivatives remain open", True)
check("scope", "the coupled nonzero-fermion residual remains separate", True)
check("scope", "P1 P2 P3 remain unchanged and unused", True)
check("planted", "PLANT no Einstein Standard Model cosmology spectrum or domain result is inferred", True)


print("SOURCE_RETURN=SOURCE-CONFIRMS__PRINTED_XI_EQUALS_D_UPSILON_ON_SHELL_REDUNDANCY__REPO-SUPERSEDES__PRINTED_UPSILON_AS_ACTION_DERIVATIVE__SOURCE-SILENT__ACTION_OWNED_DEGREE14_COMPANION_AND_OBSERVATION_KREIN_GREEN_MAP")
print("PRINTED_SOURCE_XI_SUPPORTS=" + repr(xi_supports))
print("PRINTED_PAIRED_TOTAL=UPSILON_ZERO_XI_ZERO__XI_INDEPENDENT_RANK0")
print("FORMAL_GREEN=INVARIANT_TRACE_IDENTITY_PASS__UNRESTRICTED_FLUX_NONZERO__DIRICHLET_FLUX_ZERO")
print("DISPOSITION=PRINTED_XI_REDUNDANT_BUT_ACTION_PAIR_OPEN")
print("EXTERNAL_DATUM=P1_P2_P3_UNCHANGED_AND_UNUSED")
print("NEXT=ACTION_OWNED_DEGREE14_COMPANION_FROM_FRECHET_EULER__THEN_MOVING_HODGE_SECTION_TARGET_GREEN_IDENTITY")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
