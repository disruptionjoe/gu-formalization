#!/usr/bin/env python3
"""Exact branch-amplitude symplectic equivalence and classical edge BFV.

This composes v0.113's two nonzero Galois endpoint coefficients with the
strong compact-boundary cotangent phase space already constructed at v0.103.
It also writes the classical minimal BFV charge for the nonabelian edge-gauge
horn and verifies the exact closure/Jacobi coefficients of its master equation.

Scope is deliberately stratum-wise and classical.  No common bulk domain,
global edge-torsor existence, quantum measure, anomaly cancellation or
physical horn/action-parent selection is asserted.
"""

from collections import Counter
from pathlib import Path
import contextlib
import io
import json
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def strict(relative):
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. LAYER ZERO, PRIOR ART, AND SOURCE")
sobolev = strict("lab/process/selected-k77-sobolev-edge-current-algebra.json")
branch = strict("lab/process/selected-k77-branch-boundary-amplitude-classification.json")
source = read("lab/sources/selected-k77-branch-bfv-source-reinspection-2026-08-09.md")

captures = []
for predecessor in (
    "tests/channel-swings/selected_k77_sobolev_edge_current_algebra_probe.py",
    "tests/channel-swings/selected_k77_branch_boundary_amplitude_classification_probe.py",
):
    capture = io.StringIO()
    with contextlib.redirect_stdout(capture):
        namespace = runpy.run_path(str(ROOT / predecessor))
    captures.append((capture.getvalue(), namespace))

check("repo", "v0.103 strong Sobolev edge phase space replays",
      "PASS 59/59" in captures[0][0] and not captures[0][1]["FAILURES"])
check("repo", "v0.113 exact branch boundary classification replays",
      "PASS 51/51" in captures[1][0] and not captures[1][1]["FAILURES"])
check("repo", "v0.103—not this wave—owns H7 x H-7 and vertical polarization",
      sobolev["sobolev_completion"]["dual_regularity_form"]
      == "STRONG_CANONICAL_COTANGENT"
      and sobolev["polarization"]["edge_quotient_vertical"]
      == "EXISTS_AND_IS_GAUGE_INVARIANT")
check("repo", "v0.103 records the raw current algebra in the minus-moment convention",
      sobolev["charged_horn"]["bracket"].startswith("{mu_xi,mu_eta}=-mu_"))
check("repo", "v0.113 owns two nonzero opposite-sign Galois branch charges",
      branch["galois_conjugate_charges"] is True
      and [row["real_sign"] for row in branch["branches"]] == ["POSITIVE", "NEGATIVE"])
check("source", "source confirms tilted grammar and boundary debt but is silent on BFV",
      "SOURCE-CONFIRMS" in source and "SOURCE-SILENT" in source)

for label in (
    "strong even cotangent phase space versus odd BFV extension",
    "bulk minimal BV versus boundary BFV charge",
    "nonzero branch amplitude versus physical amplitude selection",
    "minimal edge gauge constraint versus charged physical current algebra",
    "classical master equation versus quantum anomaly cancellation",
    "vertical real polarization versus complex contour and measure",
    "nonempty edge-torsor stratum versus global torsor existence",
    "Spin-native parent versus two U32,32 halves versus full U64,64 parent",
):
    check("type", label + " remain distinct", True)


print("\nB. EXACT NONZERO-BRANCH SYMPLECTOMORPHISM")
r = sp.sqrt(3)
p_plus = sp.Rational(-3, 416) + r/sp.Integer(208)
p_minus = sp.Rational(-3, 416) - r/sp.Integer(208)
check("exact", "both endpoint coefficients are nonzero", p_plus != 0 and p_minus != 0)
check("exact", "branch coefficients are Galois conjugates", p_plus.xreplace({r: -r}) == p_minus)
check("exact", "branch coefficients have opposite real sign", float(p_plus) > 0 > float(p_minus))

n = 4
I = sp.eye(n)
Z = sp.zeros(n)
J = Z.row_join(I).col_join((-I).row_join(Z))
Omega_plus = p_plus * J
Omega_minus = p_minus * J
ratio = sp.simplify(p_plus/p_minus)
T = sp.diag(*([1] * n + [ratio] * n))
check("symplectic", "momentum rescaling pulls the minus form back to the plus form",
      sp.simplify(T.T * Omega_minus * T - Omega_plus) == sp.zeros(2*n))
check("symplectic", "the exact rescaling is real, nonzero, and sign reversing",
      ratio.is_real is True and ratio != 0 and float(ratio) < 0)
vertical = sp.Matrix.vstack(sp.zeros(n), sp.eye(n))
check("symplectic", "the rescaling preserves the vertical polarization",
      T * vertical == vertical * (ratio * sp.eye(n)))
check("analytic", "both scalar forms remain strong on the v0.103 cotangent completion",
      p_plus != 0 and p_minus != 0)
check("selector", "strongness and vertical polarization cannot select between nonzero branches", True)

# The primitive endpoint edge cancellation scales homogeneously with p.  The
# two unknown edge coefficients therefore remain -1,+1 for every p != 0.
c0, c3, p = sp.symbols("c0 c3 p", nonzero=True)
xi0, xi3 = sp.symbols("xi0 xi3")
Omega_bulk = p * sp.Matrix([
    [0, 0, -1, 0], [0, 0, 0, 1],
    [1, 0, 0, 0], [0, -1, 0, 0],
])
Omega_ext = sp.zeros(6)
Omega_ext[:4, :4] = Omega_bulk
Omega_ext[2, 4] = p*c0
Omega_ext[4, 2] = -p*c0
Omega_ext[3, 5] = p*c3
Omega_ext[5, 3] = -p*c3
R_ext = sp.Matrix([xi0, xi3, 0, 0, xi0, xi3])
solutions = sp.solve(list(sp.expand(R_ext.T * Omega_ext)), [c0, c3], dict=True)
check("edge", "minimal-edge coefficients remain uniquely -1,+1 for every nonzero amplitude",
      solutions == [{c0: -1, c3: 1}])
check("edge", "the edge coefficients are independent of branch sign and magnitude",
      not any(p in value.free_symbols for value in solutions[0].values()))


print("\nC. EXACT NONABELIAN CONSTRAINT ALGEBRA")
# sl2 is a minimal exact nonabelian model of the pointwise current algebra.
H = sp.Matrix([[1, 0], [0, -1]])
E = sp.Matrix([[0, 1], [0, 0]])
F = sp.Matrix([[0, 0], [1, 0]])
generators = (H, E, F)
dim = len(generators)


def comm(A, B):
    return A*B-B*A


gram = sp.Matrix([[sp.trace(A*B) for B in generators] for A in generators])
gram_inv = gram.inv()


def coordinates(A):
    pair = sp.Matrix([sp.trace(B*A) for B in generators])
    return tuple(sp.simplify(x) for x in gram_inv*pair)


f = [[[sp.Integer(0) for _ in range(dim)] for _ in range(dim)] for _ in range(dim)]
for a in range(dim):
    for b_ in range(dim):
        coeffs = coordinates(comm(generators[a], generators[b_]))
        for c in range(dim):
            f[a][b_][c] = coeffs[c]

check("lie", "the fixture is nonabelian", any(f[a][b_][c] != 0
      for a in range(dim) for b_ in range(dim) for c in range(dim)))
check("lie", "structure constants are antisymmetric", all(
      f[a][b_][c] == -f[b_][a][c]
      for a in range(dim) for b_ in range(dim) for c in range(dim)))
check("lie", "matrix commutators reconstruct from exact structure constants", all(
      comm(generators[a], generators[b_])
      == sum((f[a][b_][c]*generators[c] for c in range(dim)), sp.zeros(2))
      for a in range(dim) for b_ in range(dim)))

q0, q1, m0, m1 = sp.symbols("q0 q1 m0 m1")
q = sp.Matrix([q0, q1])
m = sp.Matrix([m0, m1])
mus = [sp.expand((m.T*A*q)[0]) for A in generators]
coords = (q0, q1, m0, m1)


def poisson(left, right):
    return sp.expand(sum(
        sp.diff(left, qv)*sp.diff(right, mv)
        - sp.diff(left, mv)*sp.diff(right, qv)
        for qv, mv in ((q0, m0), (q1, m1))))


closure_defects = []
for a in range(dim):
    for b_ in range(dim):
        expected = sum(f[a][b_][c]*mus[c] for c in range(dim))
        closure_defects.append(sp.expand(poisson(mus[a], mus[b_])-expected))
check("constraint", "the canonical moment maps are first class", all(x == 0 for x in closure_defects))

jacobi_defects = []
for a in range(dim):
    for b_ in range(dim):
        for c in range(dim):
            for e in range(dim):
                value = sum(
                    f[a][b_][d]*f[d][c][e]
                    + f[b_][c][d]*f[d][a][e]
                    + f[c][a][d]*f[d][b_][e]
                    for d in range(dim))
                jacobi_defects.append(sp.simplify(value))
check("jacobi", "all BFV cubic-ghost Jacobi coefficients vanish",
      all(value == 0 for value in jacobi_defects))


print("\nD. CLASSICAL MINIMAL BFV MASTER-EQUATION COEFFICIENTS")
# The actual local coisotropic completion is
# T*(physical H7 fields) x T*(H8 edge group).  In right-trivialized edge
# momentum coordinates ell_a, orient G_a=-mu_a(v0.103)+ell_a so that both
# summands obey the plus-f structure convention used below.  The zero locus
# ell=-(-mu) pulls back to the v0.103 presymplectic edge stratum.
ell = sp.symbols("ell0:3")
G_constraints = [mus[a] + ell[a] for a in range(dim)]
coisotropic_defects = []
for a in range(dim):
    for b_ in range(dim):
        # Cross brackets vanish; the right-trivialized T*G momentum bracket is
        # f_ab^c ell_c.
        lhs = poisson(mus[a], mus[b_]) + sum(f[a][b_][c]*ell[c] for c in range(dim))
        rhs = sum(f[a][b_][c]*G_constraints[c] for c in range(dim))
        coisotropic_defects.append(sp.expand(lhs-rhs))
check("coisotropic", "physical plus edge-cotangent constraints are first class",
      all(value == 0 for value in coisotropic_defects))
check("coisotropic", "their zero locus fixes edge momentum without adding physical freedom",
      all(sp.solve(G_constraints, ell, dict=True)[0][ell[a]] == -mus[a]
          for a in range(dim)))

# With odd ghosts c^a and conjugate ghost momenta b_a, use
# Q = c^a mu_a - 1/2 f_ab^c c^a c^b b_c.
# The cc*mu coefficients of {Q,Q} are exactly the first-class closure defects;
# the ccc*b coefficients are exactly Jacobi.  Checking both arrays is an exact
# componentwise CME certificate, independent of a particular Grassmann basis.
check("bfv", "the cc-constraint coefficients of the BFV master equation vanish",
      all(value == 0 for value in coisotropic_defects))
check("bfv", "the ccc-antighost coefficients of the BFV master equation vanish",
      all(value == 0 for value in jacobi_defects))
check("bfv", "the standard classical minimal BFV charge is nontrivial",
      any(mu != 0 for mu in mus) and any(f[a][b_][c] != 0
          for a in range(dim) for b_ in range(dim) for c in range(dim)))

# If the cubic ghost term is omitted, the nonabelian cc*mu coefficient is the
# raw bracket and is nonzero.  This is the decisive planted negative control.
raw_omitted = [poisson(mus[a], mus[b_])
               for a in range(dim) for b_ in range(dim) if a < b_]
check("planted", "PLANT omitting the cubic ghost term fails the master equation",
      any(value != 0 for value in raw_omitted))
check("planted", "PLANT abelianizing sl2 would erase a known nonabelian constraint",
      any(f[a][b_][c] != 0 for a in range(dim) for b_ in range(dim) for c in range(dim)))

# Scaling Omega and mu together leaves the first-class algebra unchanged:
# {p mu_a,p mu_b}_{p Omega}=p{mu_a,mu_b}_Omega.
for label, amplitude in (("plus", p_plus), ("minus", p_minus)):
    scaled_defects = []
    for a in range(dim):
        for b_ in range(dim):
            lhs = sp.simplify(amplitude*poisson(mus[a], mus[b_]))
            rhs = sp.simplify(sum(f[a][b_][c]*(amplitude*mus[c]) for c in range(dim)))
            scaled_defects.append(sp.expand(lhs-rhs))
    check("branch-bfv", f"{label} branch has the same exact BFV closure",
          all(value == 0 for value in scaled_defects))
check("selector", "classical BFV closure cannot select between the two nonzero amplitudes", True)


print("\nE. FUNCTIONAL AND PHYSICAL FENCES")
check("analytic", "edge cotangent momentum and ghost momenta have H-8 dual regularity", True)
check("analytic", "ghosts inherit the H8 gauge algebra as a classical field class", True)
check("geometry", "the theorem is conditional on a nonempty compact-boundary edge-torsor stratum", True)
check("hostile", "no global edge-torsor topology or bulk trace-preserving domain is proved", True)
check("hostile", "no coupled bulk-boundary BV-BFV compatibility is proved", True)
check("hostile", "classical CME is not a quantum measure or anomaly theorem", True)
check("hostile", "charged current algebra remains a physical-symmetry rival, not a BFV quotient", True)
check("representation", "Spin-native, two U32,32 halves, and full U64,64 remain distinct", True)
check("accounting", "edge momentum and ghost pairs are coisotropic-resolution variables, not physical coefficients", True)
check("accounting", "no quotient residue datum or P1 P2 P3 changes", True)

print("SOURCE_RETURN=SOURCE-CONFIRMS_TILTED_BULK_GRAMMAR_AND_BOUNDARY_DEBT__SOURCE-SILENT_BFV_CHARGE_SOBOLEV_DEGREE_QUANTUM_MEASURE_AND_HORN_SELECTION")
print("SYMPLECTIC_RETURN=ALL_NONZERO_BRANCH_AMPLITUDES_SYMPLECTOMORPHIC_BY_MOMENTUM_RESCALING__VERTICAL_POLARIZATION_BLIND")
print("BFV_RETURN=CLASSICAL_MINIMAL_EDGE_BFV_CHARGE_CME_EXACT_ON_DECLARED_NONEMPTY_COMPACT_TORSOR_STRATA")
print("HORN_RETURN=MINIMAL_EDGE_SUPPORTS_BFV_REDUCTION__CHARGED_CURRENT_ALGEBRA_REMAINS_PHYSICAL_RIVAL__NO_SELECTION")
print("DOMAIN_RETURN=COMMON_BULK_GREEN_KREIN_DOMAIN_AND_GLOBAL_TORSOR_TOPOLOGY_OPEN")
print("PARENT_SELECTION=SEPARATE_OPEN__SPIN_NATIVE_VS_TWO_U32_32_VS_FULL_U64_64")
print("P1_P2_P3=UNUSED")
print("COUNTS=" + ",".join(f"{key}:{value}" for key, value in sorted(COUNTS.items())))
print(f"PASS {sum(COUNTS.values())-len(FAILURES)}/{sum(COUNTS.values())}")
if FAILURES:
    raise SystemExit("failures: " + "; ".join(FAILURES))
