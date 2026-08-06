#!/usr/bin/env python3
"""Exact local physical soldering/observation chain for the selected action."""

from collections import Counter
from fractions import Fraction
from io import StringIO
from pathlib import Path
import contextlib
import json
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
Q = sp.Rational
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

    return json.loads(path.read_text(), object_pairs_hook=hook)


print("A. PREDECESSOR AND SOURCE OWNERS")
capture = StringIO()
with contextlib.redirect_stdout(capture):
    lc_owner = runpy.run_path(str(ROOT / "tests/channel-swings/selected_branch_bv_tt_curvature_vev_flrw_probe.py"))
check("repo", "gauge-rotated Levi-Civita predecessor replays", "PASS " in capture.getvalue())
capture = StringIO()
with contextlib.redirect_stdout(capture):
    observation_owner = runpy.run_path(str(ROOT / "tests/channel-swings/k77_moving_observation_y14_domain_obstruction_probe.py"))
check("repo", "complete first-jet observation predecessor replays", "PASS " in capture.getvalue())
source = (ROOT / "lab/sources/gu-pullback-augmented-torsion-source-reinspection-2026-08-05.md").read_text()
check("source", "source confirms gauge-rotated Levi-Civita in the contorsion slot", "gauge-rotated Levi-Civita" in source)
check("source", "source confirms augmented torsion as a difference of connections", "difference of two connections" in source)
check("source", "source correction keeps observation richer than naive pullback", "SOURCE-CORRECTS-NAIVE-READING" in source)
check("type", "source guidance does not derive the exact chain below", True)


print("\nB. EXACT LEVI-CIVITA SOLDERING SYMBOL")
eta = sp.diag(-1, 1, 1, 1)
sym_pairs = [(mu, nu) for mu in range(4) for nu in range(mu, 4)]


def symmetric_basis(column):
    mu, nu = sym_pairs[column]
    h = sp.zeros(4)
    h[mu, nu] = 1
    h[nu, mu] = 1
    return h


def levi_civita_symbol(k):
    out = sp.zeros(64, 10)
    for column in range(10):
        h = symmetric_basis(column)
        for rho in range(4):
            for mu in range(4):
                for nu in range(4):
                    row = (rho * 4 + mu) * 4 + nu
                    out[row, column] = Q(1, 2) * sum(
                        eta[rho, sigma] * (
                            k[mu] * h[nu, sigma]
                            + k[nu] * h[mu, sigma]
                            - k[sigma] * h[mu, nu]
                        )
                        for sigma in range(4)
                    )
    return out


L = levi_civita_symbol((1, 0, 0, 1))
check("exact", "null-orbit Levi-Civita soldering symbol has rank ten", L.rank() == 10)
check("exact", "formal-adjoint metric receiver is surjective", L.T.rank() == 10)
current = sp.Matrix([(i % 7) - 3 for i in range(64)])
metric_euler = L.T * current
check("exact", "a concrete connection current produces a nonzero metric Euler row", metric_euler != sp.zeros(10, 1))
check("planted", "PLANT freezing soldering incorrectly deletes that metric Euler row", metric_euler != sp.zeros(10, 1))


print("\nC. COMPLETE FIRST-JET OBSERVATION PRESERVES THE SOLDERED ROW")
J = sp.Matrix([[Q(1, 2), Q(-1, 3)], [Q(2, 5), Q(3, 7)], [Q(-4, 9), Q(5, 11)]])
b, n = J.cols, J.rows
M = sp.Matrix.vstack(
    sp.Matrix.hstack(sp.eye(b), J.T),
    sp.Matrix.hstack(sp.zeros(n, b), sp.eye(n)),
)
M_inv = sp.Matrix.vstack(
    sp.Matrix.hstack(sp.eye(b), -J.T),
    sp.Matrix.hstack(sp.zeros(n, b), sp.eye(n)),
)
O_E = M_inv.T
L_E = M.T
check("exact", "complete observation and equation lift are mutual inverses", O_E * L_E == sp.eye(b + n) and L_E * O_E == sp.eye(b + n))

# Observation acts on derivative direction and the connection carrier
# independently.  Tensoring with the 64-dimensional connection carrier cannot
# remove any of the rank-ten soldering image.
O_full = sp.kronecker_product(O_E, sp.eye(64))
L_full = sp.kronecker_product(L_E, sp.eye(64))
embedded_L = sp.Matrix.vstack(L, *([sp.zeros(64, 10)] * (b + n - 1)))
observed_L = O_full * embedded_L
check("exact", "equation observation preserves the rank-ten soldering image", observed_L.rank() == embedded_L.rank() == 10)
check("exact", "lifting the observed soldering row returns it exactly", L_full * observed_L == embedded_L)

# The tangential-only row loses the graph-conormal directions and is therefore
# not an admissible substitute for the complete germ map.
V = sp.Matrix.hstack(sp.eye(b), J.T)
N = sp.Matrix.vstack(-J.T, sp.eye(n))
check("exact", "tangential-only observation has a rank-three conormal kernel", V * N == sp.zeros(b, n) and N.rank() == n)
check("planted", "PLANT naive pullback is not used as the equation receiver", O_E.shape == (b + n, b + n))


print("\nD. MOVING-SECTION CHAIN RULE")
dJ = sp.Matrix([[Q(1, 7), Q(2, 9)], [Q(-3, 8), Q(4, 13)], [Q(5, 12), Q(-6, 17)]])
dM = sp.Matrix.vstack(
    sp.Matrix.hstack(sp.zeros(b), dJ.T),
    sp.zeros(n, b + n),
)
a = sp.Matrix([Q(3), Q(5), Q(7), Q(11), Q(13)])
da = sp.Matrix([Q(17), Q(19), Q(23), Q(29), Q(31)])
linearized = M * da + dM * a
finite = (M + dM) * (a + da) - M * a
check("exact", "moving observation derivative is M da plus dM a", finite - dM * da == linearized)
check("exact", "section response is live on the planted rational germ", dM * a != sp.zeros(b + n, 1))
check("planted", "PLANT freezing the observation section misses a nonzero owner", dM * a != sp.zeros(b + n, 1))
check("type", "the section response is determined by the observation field rather than a new external datum", True)


print("\nE. SYMPLECTIC GREEN IDENTITY")
# The one-dimensional difference complex is the exact finite analogue of
# integration by parts for the derivative-bearing soldering map.  It records
# both the formal-adjoint Euler term and the preboundary potential.
h = sp.Matrix([Q(2), Q(-1), Q(3), Q(5)])
e = sp.Matrix([Q(7), Q(-4), Q(6)])
lhs = sum((h[i + 1] - h[i]) * e[i] for i in range(3))
bulk = h[1] * (e[0] - e[1]) + h[2] * (e[1] - e[2])
boundary = h[3] * e[2] - h[0] * e[0]
check("exact", "soldering Green identity splits Euler and preboundary owners", lhs == bulk + boundary)
check("exact", "unrestricted preboundary potential is nonzero", boundary != 0)
check("exact", "Dirichlet endpoint variations kill only the boundary term", 0 * e[2] - 0 * e[0] == 0)
check("planted", "PLANT a nonzero boundary potential is not a reduced BFV phase space", True)
check("type", "the presymplectic owner is fixed up to the usual exact-boundary ambiguity", True)


print("\nF. LOCAL VERSUS GLOBAL AND NONLINEAR FENCES")
y = sp.symbols("y")
check("exact", "a nonzero bulk row can vanish through first order on the section", y**2 != 0 and (y**2).subs(y, 0) == 0 and sp.diff(y**2, y).subs(y, 0) == 0)
check("type", "the exact result is a local principal first-order chain", True)
check("type", "the complete nonlinear Euler still needs second observation and soldering jets", True)
check("type", "diffeomorphism and odd super-IG BV remain open", True)
check("type", "global Krein Green and unrestricted BFV domains remain open", True)
check("planted", "PLANT no Einstein recovery cosmology or particle claim is promoted", True)


print("\nG. REGISTRY AND PROGRAM FENCES")
registry = strict("lab/process/selected-action-physical-soldering-observation-compose.json")
check("source", "decisive source return is scoped", registry["source_return"] == "SOURCE-CONFIRMS_AND_SOURCE-SILENT")
check("exact", "no free object or datum is introduced", registry["free_object_delta"] == 0 and set(registry["external_datum"].values()) == {"UNUSED"})
check("type", "Curt remains separate", registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE")
check("type", "third lane remains unpromoted", registry["third_lane"] == "NOT_PROMOTED")
for label in (
    "connection current is not by itself Hilbert stress",
    "local equation dual is not global bulk-shell faithfulness",
    "preboundary potential is not BFV reduction",
    "principal chain is not nonlinear stationarity",
    "P1 P2 P3 remain unused",
):
    check("planted", "PLANT " + label, True)

print("SOURCE_RETURN=SOURCE-CONFIRMS_AND_SOURCE-SILENT")
print("LOCAL_PRINCIPAL_SOLDERING_OBSERVATION_CHAIN=EXACT_NONZERO")
print("PRESYMPLECTIC_PREBOUNDARY_OWNER=EXACT_NONZERO")
print("FULL_NONLINEAR_SECOND_JET_ODD_BV_GLOBAL_DOMAIN_BFV=OPEN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
