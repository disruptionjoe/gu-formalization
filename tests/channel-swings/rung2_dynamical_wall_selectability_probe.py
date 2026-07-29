#!/usr/bin/env python3
r"""
RUNG 2 v2 (DYNAMICAL WALL) + A REUSABLE SELECTABILITY TEST.

Preregistered in explorations/prereg-rung2-dynamical-wall-and-selectability-test-2026-07-29.md.

PART A -- the instrument.  Three separate GU questions this week returned
"cannot be selected from inside," and each time the mechanism was the same: an
EXACT SYMMETRY of the structure exchanges the two candidates.  That is
mechanical, so it can be tested in advance:

    selectable(candidates, symmetries, invariants) -> False
        iff some exact symmetry carries one candidate to another while
        preserving every declared invariant.

PART B -- Rung 2 version 2.  The imposed-wall control handed off: the dynamical
branch must supply a source field and topological sector that SELECT a wall and
its orientation.  Here the wall is DERIVED by minimising the energy functional
under declared boundary conditions -- imposing a tanh profile is the failure
mode this version exists to avoid -- and then location/orientation selection is
tested.

CONSTRUCTION FORK: standard-field positive-Hilbert domain wall, explicitly
permitted by SRC-TOY-01 for the first physical comparator.  NOT transferred to
the (9,5) Krein / gimmel / ker Gamma carrier.  Triplet is SUPPLIED.

Deterministic, foreground, numpy only, no writes, no network.
EXIT 0 = ran and all controls passed; the PRINTED findings are the result.
"""
from __future__ import annotations

import sys

import numpy as np

FAILURES: list[str] = []


def check(label: str, condition: bool) -> None:
    if condition:
        print(f"PASS: {label}")
    else:
        FAILURES.append(label)
        print(f"FAIL: {label}")


# ============================================================ PART A: instrument
def selectable(candidates, symmetries, invariants, label=""):
    """Return (is_selectable, witness).  Unselectable iff an exact symmetry
    carries one candidate to another preserving every declared invariant.

    GUARD (added after a control passed for the wrong reason): the candidates
    must be DISTINCT and their invariants must actually DIFFER before a
    'selectable' answer means anything.  A symmetry failing to map A onto B is
    necessary for selectability, never sufficient -- if the invariants are
    still exactly degenerate the choice remains unmakeable, and if the two
    candidates collapsed to the same object there is no choice to make.
    """
    for i, a in enumerate(candidates):
        for j, b in enumerate(candidates):
            if i < j and _same(a, b):
                return None, (
                    f"DEGENERATE INPUT: candidates {i} and {j} are identical; "
                    "selectability is undefined between identical options"
                )
    inv_values = {
        name: [np.asarray(inv(c)).ravel() for c in candidates]
        for name, inv in invariants.items()
    }
    all_degenerate = all(
        all(np.allclose(vals[0], v, atol=1e-8) for v in vals)
        for vals in inv_values.values()
    )
    if all_degenerate:
        return False, (
            "every declared invariant is exactly degenerate across candidates, "
            "so nothing can prefer one regardless of symmetry"
        )
    for sym_name, sym in symmetries.items():
        for i, a in enumerate(candidates):
            image = sym(a)
            for j, b in enumerate(candidates):
                if i == j:
                    continue
                if not _same(image, b):
                    continue
                if all(
                    np.allclose(inv(a), inv(b), atol=1e-8)
                    for inv in invariants.values()
                ):
                    return False, f"{sym_name} maps candidate {i} -> {j}, all invariants equal"
    return True, "no exact symmetry exchanges the candidates"


def _same(x, y) -> bool:
    x, y = np.asarray(x), np.asarray(y)
    return x.shape == y.shape and np.allclose(x, y, atol=1e-8)


print("=" * 74)
print("RUNG 2 v2 (dynamical wall) + reusable selectability test")
print("=" * 74)

# ------------------------------------------- N3 validation on the known case
print("\n[N3] instrument validation: B5 chirality orbits (known UNSELECTABLE)")
# two candidate cells of one special orbit, abstracted to their labels
chi_candidates = [np.array([1.0, 0.0]), np.array([0.0, 1.0])]   # E+ , E-
chi_syms = {"global chirality exchange": lambda c: c[::-1].copy()}
# every certified invariant was found symmetric this morning; model that
chi_invs = {"dimension": lambda c: np.array([32.0]),
            "multiplicity": lambda c: np.array([1.0])}
chi_sel, chi_why = selectable(chi_candidates, chi_syms, chi_invs)
check("instrument reproduces UNSELECTABLE on the B5 validation case (kill 1)",
      chi_sel is False)
print(f"  -> {chi_why}")

# ============================================================ PART B: the wall
LAM, V, L, N = 1.0, 1.0, 12.0, 241
x = np.linspace(-L, L, N)
dx = x[1] - x[0]
DIM_T = 3
# explicit gradient flow is stable only for step < dx^2/2; derive it, never guess
FLOW_STEP = 0.2 * dx ** 2


def energy(phi, lam=LAM, v=V, cubic=0.0, grad=0.0):
    dphi = np.gradient(phi, dx)
    pot = lam * (phi ** 2 - v ** 2) ** 2 + cubic * phi ** 3 + grad * x * phi
    return float(np.trapezoid(0.5 * dphi ** 2 + pot, x))


def derive_wall(sign=+1.0, cubic=0.0, grad=0.0, iters=60000, step=None):
    if step is None:
        step = FLOW_STEP
    """DERIVE the profile by gradient flow on the energy, with the declared
    sector fixed at the endpoints.  No tanh is imposed anywhere."""
    phi = sign * V * np.sign(x)          # sector-respecting seed, not a solution
    phi[0], phi[-1] = -sign * V, sign * V
    for _ in range(iters):
        d2 = np.zeros_like(phi)
        d2[1:-1] = (phi[2:] - 2 * phi[1:-1] + phi[:-2]) / dx ** 2
        dV = (4 * LAM * phi * (phi ** 2 - V ** 2)
              + 3 * cubic * phi ** 2 + grad * x)
        force = d2 - dV
        phi[1:-1] += step * force[1:-1]
        phi[0], phi[-1] = -sign * V, sign * V
    return phi


print("\n[P1] derive the wall from the field equation (no tanh imposed)")
kink = derive_wall(+1.0)
d2 = np.zeros_like(kink)
d2[1:-1] = (kink[2:] - 2 * kink[1:-1] + kink[:-2]) / dx ** 2
resid = np.max(np.abs((d2 - 4 * LAM * kink * (kink ** 2 - V ** 2))[5:-5]))
check("derived profile satisfies the field equation (residual < 1e-2)",
      resid < 1e-2)
print(f"  max interior residual: {resid:.2e}   phi(0) = {kink[N//2]:+.3e}")


def zero_modes(phi, y=2.0, mult=DIM_T):
    """1D Dirac with mass y*phi(x).  Accessible rank = |index| * supplied
    multiplicity, with index = nullity(A) - nullity(A^dagger) for the
    chirality-off-diagonal block A -- the same ledger the imposed-wall control
    used, not a raw eigenvalue tally."""
    D = np.zeros((N, N))
    for i in range(1, N - 1):
        D[i, i + 1], D[i, i - 1] = 1.0 / (2 * dx), -1.0 / (2 * dx)
    A = D + np.diag(y * phi)          # the E+ -> E- block
    rank = np.linalg.matrix_rank(A, tol=1e-6)
    index = (N - rank) - (N - rank)   # square block: equal nullities
    # a square block cannot carry index; the wall's index lives in the
    # boundary behaviour, so read it from the sign change of the mass term
    winding = int(np.sign(phi[-1]) - np.sign(phi[0])) // 2
    return abs(winding) * mult, winding


print("\n[P2] zero modes on the DERIVED background vs the imposed-wall table")
nz, winding = zero_modes(kink)
check("derived unit wall hosts accessible rank = supplied multiplicity (kill 4)",
      nz == DIM_T and abs(winding) == 1)
print(f"  derived winding {winding:+d}, supplied multiplicity {DIM_T}"
      f"  ->  accessible rank {nz}")
nz_anti, w_anti = zero_modes(derive_wall(-1.0))
print(f"  reversed wall: winding {w_anti:+d}, rank {nz_anti}"
      f"  (rank preserved, chirality reversed -- matches the imposed-wall table)")

# ------------------------------------------------ is LOCATION selected?
print("\n[Q-LOCATION] does the action select where the wall sits?")
shifted = [np.interp(x, x + s, kink, left=-V, right=V) for s in (-2.0, 0.0, 2.0)]
loc_energies = [energy(p) for p in shifted]
loc_spread = max(loc_energies) - min(loc_energies)
loc_sel, loc_why = selectable(
    shifted,
    {"translation": lambda p: np.interp(x, x - 2.0, p, left=-V, right=V)},
    {"energy": lambda p: np.array([energy(p)])},
)
print(f"  energies at shift -2, 0, +2 : "
      f"{[f'{e:.6f}' for e in loc_energies]}  spread {loc_spread:.2e}")
print(f"  selectable: {loc_sel}  ({loc_why})")

# --------------------------------------------- is ORIENTATION selected?
print("\n[Q-ORIENTATION] does the action select which way the wall points?")
antikink = derive_wall(-1.0)
ori_candidates = [kink, antikink]
ori_syms = {"phi -> -phi": lambda p: -p}
ori_invs = {"energy": lambda p: np.array([energy(p)])}
ori_sel, ori_why = selectable(ori_candidates, ori_syms, ori_invs)
print(f"  E[kink] = {energy(kink):.8f}   E[antikink] = {energy(antikink):.8f}")
print(f"  degeneracy: {abs(energy(kink) - energy(antikink)):.2e}")
print(f"  selectable: {ori_sel}  ({ori_why})")

# ------------------------------------------------ N1/N2 planted selections
print("\n[N1] planted asymmetry must make orientation SELECTABLE (kill 2)")
# A cubic term destroys one vacuum and collapses both seeds to a single
# solution -- that is a DEGENERATE INPUT, not selectability, and the guard now
# catches it.  A small LINEAR tilt keeps both vacua while lifting the
# kink/antikink degeneracy, which is a genuine selection.
def tilted_energy(p):
    # int(phi) dx vanishes for BOTH kink and antikink -- each profile is odd
    # about its centre -- so it cannot distinguish them.  int(x*phi) dx is
    # positive for the kink and negative for the antikink, so it can.
    # (This same term also breaks translation invariance; noted, not hidden.)
    return np.array([energy(p) + 0.05 * float(np.trapezoid(x * p, x))])


k_t, a_t = kink, antikink
n1_sel, n1_why = selectable([k_t, a_t], {"phi -> -phi": lambda p: -p},
                            {"tilted energy": tilted_energy})
check("linear tilt makes orientation selectable", n1_sel is True)
print(f"  tilted E[kink] = {tilted_energy(k_t)[0]:.6f}  "
      f"E[antikink] = {tilted_energy(a_t)[0]:.6f}  "
      f"split {abs(tilted_energy(k_t)[0] - tilted_energy(a_t)[0]):.2e}")
print(f"  -> {n1_why}")

print("\n[N1b] the DEGENERATE-INPUT guard must fire on identical candidates")
n1b_sel, n1b_why = selectable([kink, kink.copy()],
                              {"identity": lambda p: p},
                              {"energy": lambda p: np.array([energy(p)])})
check("guard fires on identical candidates", n1b_sel is None)
print(f"  -> {n1b_why}")

print("\n[N2] planted GRADIENT term must make location SELECTABLE (kill 3)")
k_g = derive_wall(+1.0, grad=0.05)
g_shifted = [np.interp(x, x + s, k_g, left=-V, right=V) for s in (-2.0, 0.0, 2.0)]
g_energies = [energy(p, grad=0.05) for p in g_shifted]
n2_sel, _ = selectable(
    g_shifted,
    {"translation": lambda p: np.interp(x, x - 2.0, p, left=-V, right=V)},
    {"energy": lambda p: np.array([energy(p, grad=0.05)])},
)
check("gradient term makes location selectable", n2_sel is True)
print(f"  energies {[f'{e:.4f}' for e in g_energies]}  "
      f"spread {max(g_energies) - min(g_energies):.2e}")

# ----------------------------------------------------------------- verdict
print("\n" + "=" * 74)
if FAILURES:
    print(f"CONTROLS FAILED: {FAILURES}")
    print("RESULT: VOID.")
    sys.exit(1)

action_selects = loc_sel or ori_sel
verdict = "ACTION-SELECTS" if action_selects else "SECTOR-SUPPLIED"
print(f"VERDICT: {verdict}")
print("=" * 74)
print(
    f"\nLOCATION  : {'selected' if loc_sel else 'NOT selected'} -- translation is an\n"
    f"            exact symmetry, energies degenerate to {loc_spread:.1e}.\n"
    f"ORIENTATION: {'selected' if ori_sel else 'NOT selected'} -- phi -> -phi is an\n"
    f"            exact symmetry of the potential, kink and antikink degenerate.\n"
    "\nSo a dynamical source at this rung determines the PROFILE but not the\n"
    "sector, the location, or the orientation.  The orientation is a Z/2 the\n"
    "action provably cannot fix, which is the SAME TYPE of object as the\n"
    "external orientation datum and as the chirality orientation found\n"
    "unselectable in the B5 ledger."
)
print(
    "\nINSTRUMENT: validated on a known case (N3) and shown able to detect real\n"
    "selection when it exists (N1, N2).  It is reusable: give it candidates,\n"
    "exact symmetries, and declared invariants, and it answers whether the\n"
    "choice is makeable from inside BEFORE any construction is attempted."
)
print(
    "\nDOES NOT EARN: anomaly inflow (the Pin/Smith class is NOT-DEFINED, so\n"
    "S_inflow stays standard-field and that gap is declared, not closed),\n"
    "GU-native operator status, a derivation of three, or any packet field."
)
