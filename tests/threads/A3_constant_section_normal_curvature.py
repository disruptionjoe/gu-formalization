"""THREAD A3 -- constant-section normal-curvature gate for the higher-codim Willmore EL.

Thread A scoped the full higher-codimension Willmore first variation and named the
normal-bundle curvature term R^perp_0 as the one first-variation object not yet
carried by the alpha_W / OQ2-A arc.

This audit computes the Ricci-equation SHAPE-OPERATOR COMMUTATOR piece at the flat
constant section s0(x) = (x, eta) of Y14 = Met(X4). It does not compute the full
ambient-projection contribution to R^perp_0, so it does not close the first variation.
It proves the narrow fact needed for the next step:

    the constant-section shape operators do not commute.

Therefore the normal-bundle curvature term cannot be dropped by codimension-one
intuition. The full first variation must carry this commutator piece and then test
whether the ambient R^Y projection cancels, reinforces, or rotates it.

Run: python tests/threads/A3_constant_section_normal_curvature.py
"""
from __future__ import annotations

import sympy as sp

FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


DIM = 4
eta = sp.diag(-1, 1, 1, 1)
eta_inv = eta
pairs = [(a, b) for a in range(DIM) for b in range(a, DIM)]


def sym2(metric, i, j, k, l):
    return sp.Rational(1, 2) * (metric[i, k] * metric[j, l] + metric[i, l] * metric[j, k])


def B0(mu, nu, a, b):
    """Constant-section vertical SFF from ii-s-coordinate-formula sec 6.1.

    B^V_0{}_{mu nu,ab}
      = -1/2(eta_{a(mu} eta_{nu)b} - 1/2 eta_{ab} eta_{mu nu}).
    """
    return -sp.Rational(1, 2) * (
        sym2(eta, a, b, mu, nu) - sp.Rational(1, 2) * eta[a, b] * eta[mu, nu]
    )


def shape_operator(a, b):
    """Shape operator A_(ab)^i_j = eta^{ik} B0(k,j,ab), with lower normal label (ab)."""
    return sp.Matrix(
        DIM,
        DIM,
        lambda i, j: sp.simplify(sum(eta_inv[i, k] * B0(k, j, a, b) for k in range(DIM))),
    )


def lower_first_tangent(mat):
    """Lower the raised first tangent index: C_ij = eta_iell C^ell_j."""
    return sp.Matrix(
        DIM,
        DIM,
        lambda i, j: sp.simplify(sum(eta[i, ell] * mat[ell, j] for ell in range(DIM))),
    )


def commutator_piece(alpha, beta):
    """Ricci-equation extrinsic piece with tangent indices lowered.

    C_{ij;alpha beta} = eta_{i ell} ([A_alpha, A_beta])^ell_j.
    """
    a, b = alpha
    c, d = beta
    comm = shape_operator(a, b) * shape_operator(c, d) - shape_operator(c, d) * shape_operator(a, b)
    return lower_first_tangent(sp.simplify(comm))


zero = sp.zeros(DIM, DIM)

print("[A3] constant-section normal-curvature commutator audit\n")

# Basic background check: this is the same non-totally-geodesic section Thread A/B use.
nonzero_B0 = any(
    sp.simplify(B0(mu, nu, a, b)) != 0
    for mu in range(DIM)
    for nu in range(DIM)
    for a in range(DIM)
    for b in range(DIM)
)
check("constant-section B0 is nonzero (Met(X4) constant slice is not totally geodesic)", nonzero_B0)

H0 = sp.Matrix(
    DIM,
    DIM,
    lambda a, b: sp.simplify(
        sum(eta_inv[mu, nu] * B0(mu, nu, a, b) for mu in range(DIM) for nu in range(DIM))
    ),
)
H0_expected = sp.Rational(1, 2) * eta
check("mean curvature H0_ab = (1/2) eta_ab, the same O(M^0) background Thread A/B isolate",
      H0 == H0_expected)

# Compute all ordered commutators in the symmetric-pair normal labels.
nonzero = []
antisym_normal = True
antisym_tangent = True
for alpha in pairs:
    for beta in pairs:
        Cab = commutator_piece(alpha, beta)
        Cba = commutator_piece(beta, alpha)
        if sp.simplify(Cab + Cba) != zero:
            antisym_normal = False
        if sp.simplify(Cab + Cab.T) != zero:
            antisym_tangent = False
        if Cab != zero:
            nonzero.append((alpha, beta, Cab))

check("shape-operator commutators are antisymmetric in normal labels", antisym_normal)
check("lowered commutator tensors are antisymmetric in tangent indices", antisym_tangent)
check("normal-curvature commutator piece is NONZERO: 48 ordered normal-label commutators fire",
      len(nonzero) == 48,
      f"observed {len(nonzero)} nonzero ordered commutators out of {len(pairs) ** 2}")

# A minimal witness: diagonal normal (00) and off-diagonal normal (01) fail to commute.
witness = commutator_piece((0, 0), (0, 1))
expected_witness = sp.Matrix(
    [
        [0, sp.Rational(1, 8), 0, 0],
        [sp.Rational(-1, 8), 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
)
print("    witness C_{ij;(00)(01)} = eta_iell [A_(00), A_(01)]^ell_j:")
print(witness)
check("explicit witness [A_(00), A_(01)] is nonzero and equals the exact rational matrix",
      witness == expected_witness)

# The commutator is O(M^0): no perturbation, mass, target count, or observational input enters.
symbols_used = set()
for _, _, Cab in nonzero:
    for entry in Cab:
        symbols_used |= entry.free_symbols
check("commutator piece is an O(M^0) background object with no fitted parameter symbols",
      symbols_used == set(),
      f"free symbols observed: {sorted(str(s) for s in symbols_used)}")

print("\n[verdict]")
print("  The constant-section shape operators in codimension 10 do NOT commute. The Ricci-equation")
print("  commutator piece of R^perp_0 is already nonzero at O(M^0), before Schwarzschild, theta,")
print("  DESI, 24, 8, or any source-action target enters. This is the concrete normal-bundle")
print("  curvature obstruction Thread A named: the higher-codim Willmore first variation must carry")
print("  the R^perp term and cannot use codimension-one intuition that silently drops it.")
print()
print("  Honest scope: this computes only the shape-operator commutator piece. The full R^perp_0")
print("  still requires adding the ambient R^Y normal projection and checking whether it cancels,")
print("  reinforces, or rotates the commutator. No claim status, canon verdict, or OQ2-A selection")
print("  changes here.")

if FAIL:
    print(f"\nFAILED: {FAIL}")
    raise SystemExit(1)
print("\nexit 0 = constant-section R^perp commutator piece is nonzero and exact; full ambient assembly remains open.")
