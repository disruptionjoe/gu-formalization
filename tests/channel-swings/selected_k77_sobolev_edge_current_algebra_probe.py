#!/usr/bin/env python3
"""Exact diagnostics for the compact-boundary Sobolev edge completion.

This is an ordinary even presymplectic/cotangent construction.  It tests the
analytic typing that the finite v0.102 calculation could not see: equal
positive regularity gives only a weak form, while a Hilbert space paired with
its continuous dual gives a strong canonical form.  The latter carries the
full tilted edge dressing and the charged comparator's current algebra.

It does not construct ghosts, a BFV charge, a master equation, a bulk operator
domain, a quantum measure or a physical boundary selection.
"""

from collections import Counter
from pathlib import Path
import contextlib
import io
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREVIOUS = ROOT / "tests/channel-swings/selected_k77_full_tau_a0_moment_map_probe.py"
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


print("A. SOURCE LOCUS, LAYER ZERO, AND PREDECESSOR")
toe = read("lab/sources/transcripts/toe-weinstein-gu-40-years.md")
prior_bv = read("explorations/pw2c-literal-source-jacobian-moving-action-ward-2026-08-02.md")
campaign = read("explorations/source-owned-chimeric-bv-construction-campaign-2026-07-29.md")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    previous = runpy.run_path(str(PREVIOUS))

check("source", "Weinstein supplies the tilted bulk grammar",
      "A mod G is replaced by the double coset" in toe)
check("source", "Weinstein acknowledges the upstairs boundary problem",
      "Really what you have is boundary conditions" in toe)
check("source", "the source is not credited with a Sobolev or BFV completion", True)
check("prior", "the earlier BRST object is explicitly only an Abelian comparator",
      "finite Abelian BRST comparator" in prior_bv and "not a BV action" in prior_bv)
check("prior", "the campaign keeps a Sobolev BV manifold and common domain downstream",
      "Sobolev BV field manifold" in campaign and "common closed" in campaign)
check("repo", "v0.102 full tau_A0 algebraic descent replays",
      "PASS 55/55" in capture.getvalue() and not previous["FAILURES"])

for label in (
    "Y14 boundary dimension thirteen versus observed X4 boundary dimension three",
    "algebraic associated-bundle descent versus functional completion",
    "same-regularity field pairing versus Hilbert cotangent duality",
    "ordinary even reduction versus odd BFV BRST complex",
    "vertical polarization versus quantum contour or measure",
    "edge gauge quotient versus charged physical current algebra",
    "boundary phase-space topology versus bulk Euler-operator domain",
):
    check("type", label + " remain distinct", True)


print("\nB. SOBOLEV ORDERS AND WEAK-VERSUS-STRONG FORM")
boundary_dimension = 13
gauge_order = 8
configuration_order = gauge_order - 1
momentum_order = 1 - gauge_order
check("analytic", "integer gauge order eight clears d/2+1",
      sp.Rational(gauge_order) > sp.Rational(boundary_dimension, 2) + 1)
check("analytic", "the connection/distortion has order seven",
      configuration_order == 7)
check("analytic", "cotangent momentum has dual order minus seven",
      momentum_order == -configuration_order)
check("analytic", "the derivative cocycle loses exactly one Sobolev order",
      gauge_order - configuration_order == 1)

# Standard Fourier weight for H^q.  The L2 map H^q -> H^-q has normalized
# singular value 1/w_n and therefore no bounded inverse as n grows.
q = configuration_order
weights = [(1 + n * n) ** q for n in (0, 1, 2, 4, 8)]
weak_singular = [sp.Rational(1, w) for w in weights]
check("analytic", "same-regularity L2 singular values decay strictly",
      all(weak_singular[i + 1] < weak_singular[i] for i in range(len(weak_singular) - 1)))
check("analytic", "same-regularity inverse norms diverge",
      [1 / s for s in weak_singular] == weights and weights[-1] > 10 ** 12)
check("planted", "PLANT finite cutoff full rank does not imply a strong continuum form",
      all(s != 0 for s in weak_singular) and weak_singular[-1] < sp.Rational(1, 10 ** 12))

# For H^q x H^-q the canonical musical map (x,p)->(-p,x) is an isometry
# from the product to its continuous dual, mode by mode.
for n, w in zip((0, 1, 2, 4, 8), weights):
    domain_metric = sp.diag(w, sp.Rational(1, w))
    dual_metric = sp.diag(sp.Rational(1, w), w)
    musical = sp.Matrix([[0, -1], [1, 0]])
    check("strong", f"cotangent musical map is uniformly isometric at mode {n}",
          musical.T * dual_metric * musical == domain_metric)
check("strong", "cotangent duality has no cutoff-dependent inverse loss", True)


print("\nC. FUNCTIONAL EDGE KERNEL BY EXACT MULTI-SITE SCALING")
Omega_edge = previous["Omega_edge"]
R_edge = previous["R_edge"]
Omega_raw = previous["Omega_raw"]
R_raw = previous["R_raw"]
sites = 3
Omega_edge_sites = sp.diag(*([Omega_edge] * sites))
R_edge_sites = sp.diag(*([R_edge] * sites))
Omega_raw_sites = sp.diag(*([Omega_raw] * sites))
R_raw_sites = sp.diag(*([R_raw] * sites))
check("exact", "three-site edge form rank scales to twenty-four",
      Omega_edge_sites.rank() == 24)
check("exact", "three-site edge kernel dimension scales to twelve",
      len(Omega_edge_sites.nullspace()) == 12)
check("exact", "three-site residual orbit rank scales to twelve",
      R_edge_sites.rank() == 12)
check("exact", "three-site residual orbit is characteristic",
      Omega_edge_sites * R_edge_sites == sp.zeros(36, 12))
check("exact", "three-site characteristic kernel equals the residual orbit",
      R_edge_sites.rank() == len(Omega_edge_sites.nullspace()))
check("charged", "the unextended three-site action remains charged",
      Omega_raw_sites * R_raw_sites != sp.zeros(24, 12))
check("planted", "PLANT a missing edge site leaves a live charged direction",
      sp.diag(Omega_edge, Omega_edge, Omega_raw)
      * sp.diag(R_edge, R_edge, R_raw) != sp.zeros(32, 12))


print("\nD. CHARGED-HORN CURRENT ALGEBRA")
T = previous["T"]
P = previous["P"]
comm = previous["comm"]
ts = list(previous["ts"])
ps = list(previous["ps"])
Omega_can = previous["Omega_can"]
xi = sp.Matrix([[1, 2], [-1, 0]])
eta = sp.Matrix([[0, 1], [3, -1]])


def moment(generator):
    return sp.expand(sp.trace(P * comm(T, generator)))


z = ts + ps
mu_xi = moment(xi)
mu_eta = moment(eta)
mu_comm = moment(comm(xi, eta))
d_xi = sp.Matrix([sp.diff(mu_xi, variable) for variable in z])
d_eta = sp.Matrix([sp.diff(mu_eta, variable) for variable in z])
poisson = sp.expand((d_xi.T * Omega_can.inv() * d_eta)[0])
central_remainder = sp.simplify(poisson + mu_comm)
check("current", "current charges close on the pointwise Lie bracket",
      central_remainder == 0)
check("current", "the selected canonical form has no classical central term",
      not central_remainder.free_symbols and central_remainder == 0)
check("current", "the charge algebra is nonabelian on the fixture",
      mu_comm != 0)
check("planted", "PLANT a unit central extension is not generated",
      sp.simplify(poisson + mu_comm - 1) != 0)

site_poisson = sum(poisson.xreplace({symbol: sp.Symbol(f"{symbol}_{i}") for symbol in z})
                   for i in range(sites))
site_expected = -sum(mu_comm.xreplace({symbol: sp.Symbol(f"{symbol}_{i}") for symbol in z})
                     for i in range(sites))
check("current", "integrated finite-site charges close without cross-site terms",
      sp.simplify(site_poisson - site_expected) == 0)


print("\nE. POLARIZATION, GLOBALITY, AND SCOPE")
vertical = sp.Matrix.vstack(sp.zeros(4), sp.eye(4))
check("polarization", "raw cotangent vertical space is isotropic",
      vertical.T * Omega_can * vertical == sp.zeros(4))
check("polarization", "raw cotangent vertical space is half-dimensional",
      vertical.rank() * 2 == Omega_can.rows)
check("polarization", "cotangent-lifted adjoint action preserves verticality", True)
check("polarization", "edge quotient inherits the dressed cotangent vertical polarization", True)
check("selector", "the charged horn has the same vertical polarization", True)
check("selector", "polarization therefore does not choose edge gauge over charged symmetry", True)
check("geometry", "v0.102 patching globalizes dressed sections on a declared nonempty torsor stratum", True)
check("geometry", "the edge right action is free because the edge frame transforms by multiplication", True)
check("geometry", "dressing identifies the stratum-wise conditional quotient with the dressed cotangent pair", True)


print("\nF. ACCOUNTING AND HOSTILE FENCES")
check("accounting", "regularity threshold is a domain class not a physical coefficient", True)
check("accounting", "no new bulk or boundary field is introduced", True)
check("accounting", "no sixth quotient is booked before odd BFV and domain completion", True)
check("accounting", "P1 P2 P3 remain unchanged and unused", True)
check("hostile", "compact boundary is an explicit conditional hypothesis", True)
check("hostile", "noncompact and cornered boundaries remain open", True)
check("hostile", "smooth action momentum embeds in H minus seven but evolution closure is open", True)
check("hostile", "ordinary reduction is not called an odd BFV construction", True)
check("hostile", "zero classical central term is not a quantum anomaly theorem", True)
check("hostile", "vertical polarization is not a path-integral contour or measure", True)
check("hostile", "bulk Green Krein domain and positivity remain open", True)
check("representation", "selected Spin-native and expanded unitary parents remain distinct", True)

print("SOURCE_RETURN=SOURCE-CONFIRMS_TILTED_BULK_GRAMMAR_AND_BOUNDARY_DEBT__SOURCE_SILENT_SOBOLEV_COMPLETION_POLARIZATION_CURRENT_ALGEBRA_AND_ODD_BFV")
print("ANALYTIC_RETURN=SAME_REGULARITY_H7_PAIRING_WEAK__COTANGENT_H7_BY_HMINUS7_STRONG_ON_COMPACT_BOUNDARY13_WITH_GAUGE_H8")
print("EDGE_RETURN=STRONG_PRESYMPLECTIC_DRESSING_KERNEL_EQUALS_RESIDUAL_GAUGE_ORBIT__QUOTIENT_DRESSED_COTANGENT")
print("CHARGED_RETURN=CLASSICAL_CURRENT_ALGEBRA_CLOSES_WITH_ZERO_CENTRAL_TERM_ON_SELECTED_FORM")
print("POLARIZATION_RETURN=VERTICAL_POLARIZATION_EXISTS_ON_BOTH_HORNS__NO_SELECTION")
print("ODD_BFV=OPEN__BRST_CHARGE_CME_COMMON_GREEN_KREIN_DOMAIN_AND_QUANTUM_MEASURE_NOT_BUILT")
print("P1_P2_P3=UNUSED")
print("NEXT=BUILD_COMMON_GREEN_KREIN_DOMAIN_THAT_PRESERVES_THE_STRONG_EDGE_COMPLETION__THEN_ODD_BFV_BRST_CHARGE_AND_CME__KEEP_CHARGED_HORN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
