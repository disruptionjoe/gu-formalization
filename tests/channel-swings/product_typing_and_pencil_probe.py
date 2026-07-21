#!/usr/bin/env python3
"""Decisive product-typing and resolvent-pencil checks.

The diagonal-boundary source uses a categorical Cartesian product.  This
probe verifies its finite universal-property fixture, the exact direct-sum
resolvent identities at bounded-operator grade, the ordering in the
single-carrier pencil factorization, and the failure of the previously used
shared-factor coupled surrogate.

The probe is a certificate for typing and algebra.  It does not prove the
remaining uniform invertibility estimate for the infinite-dimensional pencil.
"""
from __future__ import annotations

import itertools
import os
import sys

import numpy as np
import scipy.linalg as la
import scipy.sparse as sp
import scipy.sparse.linalg as spla


RESULTS: list[tuple[str, str, bool]] = []
RNG = np.random.default_rng(20260720)


def check(tag: str, name: str, ok: bool, detail: str = "") -> bool:
    RESULTS.append((tag, name, bool(ok)))
    suffix = f"   ({detail})" if detail else ""
    print(f"[{tag}] {'PASS' if ok else 'FAIL'}  {name}{suffix}", flush=True)
    return bool(ok)


def opnorm(matrix: np.ndarray) -> float:
    return float(np.linalg.norm(matrix, 2))


print("=== PART A: the source product is Cartesian ===", flush=True)

# The literal Z/2-set product used by the L1 fixture.
B = (+1, -1)
BxB = tuple((x, y) for x in B for y in B)
equivariant_maps = (
    {+1: +1, -1: -1},
    {+1: -1, -1: +1},
)
fixture_ok = True
for f in equivariant_maps:
    for g in equivariant_maps:
        candidates = []
        for values in itertools.product(BxB, repeat=len(B)):
            h = dict(zip(B, values))
            if all(h[x][0] == f[x] and h[x][1] == g[x] for x in B):
                candidates.append(h)
        fixture_ok &= len(candidates) == 1
        h = candidates[0]
        fixture_ok &= all(h[-x] == (-h[x][0], -h[x][1]) for x in B)
check(
    "E",
    "source fixture product B x B has the Cartesian universal property and "
    "componentwise Z/2 action",
    fixture_ok,
)

# The finite-dimensional linear/Krein realization of the same universal
# property is the direct sum, not the tensor product.
nx, na, nb = 3, 2, 4
f = RNG.standard_normal((na, nx))
g = RNG.standard_normal((nb, nx))
pair = np.vstack((f, g))
p_a = np.hstack((np.eye(na), np.zeros((na, nb))))
p_b = np.hstack((np.zeros((nb, na)), np.eye(nb)))
linear_universal = np.allclose(p_a @ pair, f) and np.allclose(p_b @ pair, g)
check(
    "E",
    "bounded linear product is H_A direct-sum H_B: the unique pairing map "
    "has the required projections",
    linear_universal,
)

u = np.diag([1.0, -1.0])
u_prod = la.block_diag(u, u)
diagonal = np.vstack((np.eye(2), np.eye(2)))
diag_ok = np.allclose(u_prod @ diagonal, diagonal @ u)
check(
    "E",
    "the Cartesian diagonal Delta(v)=(v,v) is bounded and equivariant under "
    "the componentwise deck action",
    diag_ok and abs(opnorm(diagonal) - np.sqrt(2.0)) < 1e-12,
    f"||Delta||={opnorm(diagonal):.6f}",
)


print("\n=== PART B: direct-sum Krein and resolvent identities ===", flush=True)

def krein_self_adjoint(k: np.ndarray, seed_shift: int) -> np.ndarray:
    rng = np.random.default_rng(20260720 + seed_shift)
    raw = rng.standard_normal(k.shape) + 1j * rng.standard_normal(k.shape)
    hermitian = 0.5 * (raw + raw.conj().T)
    return k @ hermitian


k_a = np.diag([1.0, -1.0])
k_b = np.diag([1.0, 1.0, -1.0])
a = krein_self_adjoint(k_a, 1)
b = krein_self_adjoint(k_b, 2)
k_prod = la.block_diag(k_a, k_b)
n_prod = la.block_diag(a, b)
krein_defect = opnorm(k_prod @ n_prod @ k_prod - n_prod.conj().T)
check(
    "E",
    "finite Krein product uses K_A direct-sum K_B and preserves "
    "K-self-adjointness",
    krein_defect < 1e-12,
    f"defect={krein_defect:.2e}",
)

z = 0.37 + 1.21j
r_a = np.linalg.inv(a - z * np.eye(a.shape[0]))
r_b = np.linalg.inv(b - z * np.eye(b.shape[0]))
r_prod = np.linalg.inv(n_prod - z * np.eye(n_prod.shape[0]))
r_expected = la.block_diag(r_a, r_b)
res_defect = opnorm(r_prod - r_expected)
norm_defect = abs(opnorm(r_prod) - max(opnorm(r_a), opnorm(r_b)))
check(
    "E",
    "Cartesian-product resolvent is the direct sum and its norm is the "
    "maximum of the factor norms",
    res_defect < 1e-12 and norm_defect < 1e-12,
    f"identity={res_defect:.2e} norm={norm_defect:.2e}",
)

w_a = np.diag([0.7, 1.1])
w_b = np.diag([0.6, 0.9, 1.2])
w_prod = la.block_diag(w_a, w_b)
wr_a, wr_b = w_a @ r_a @ w_a, w_b @ r_b @ w_b
wr_prod = w_prod @ r_prod @ w_prod
weighted_defect = abs(opnorm(wr_prod) - max(opnorm(wr_a), opnorm(wr_b)))
check(
    "E",
    "the weighted Krein-Mourre resolvent norm obeys the same maximum law",
    weighted_defect < 1e-12,
    f"defect={weighted_defect:.2e}",
)

a2, b2 = a + 0.03 * np.eye(2), b - 0.02 * np.eye(3)
dr_a = r_a - np.linalg.inv(a2 - z * np.eye(2))
dr_b = r_b - np.linalg.inv(b2 - z * np.eye(3))
dr_prod = r_prod - np.linalg.inv(
    la.block_diag(a2, b2) - z * np.eye(n_prod.shape[0])
)
cauchy_defect = abs(opnorm(dr_prod) - max(opnorm(dr_a), opnorm(dr_b)))
check(
    "E",
    "norm-resolvent Cauchy differences are product-stable algebraically",
    cauchy_defect < 1e-12,
    f"defect={cauchy_defect:.2e}",
)

tower = la.block_diag(a, a, a)
tower_r = np.linalg.inv(tower - z * np.eye(tower.shape[0]))
check(
    "E",
    "finite Cartesian powers introduce no carrier-count growth in the "
    "resolvent operator norm",
    abs(opnorm(tower_r) - opnorm(r_a)) < 1e-12,
)


print("\n=== PART C: exact single-carrier pencil reduction ===", flush=True)

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import uniformity_execution_probe as U  # noqa: E402

ops = U.build_ops(U.A_DN, U.T_OP, U.S_LO, U.S_HI, 9)
delta = 0.3
z_pencil = 1.0j
c_values = np.sqrt(ops["qs"].astype(complex) + 1j * delta)
c_op = sp.diags(np.repeat(c_values, 256), format="csr")
c_inv = sp.diags(np.repeat(1.0 / c_values, 256), format="csr")
a_op = ops["M_op"].tocsr()
n_delta = U.scale_cols(a_op, 1.0 / c_values)
identity = sp.identity(n_delta.shape[0], format="csr", dtype=complex)
pencil = (a_op - z_pencil * c_op).tocsr()
factor_defect_matrix = (n_delta - z_pencil * identity - pencil @ c_inv).tocoo()
factor_defect = (
    float(np.max(np.abs(factor_defect_matrix.data)))
    if factor_defect_matrix.nnz
    else 0.0
)
rhs = RNG.standard_normal(n_delta.shape[0]) + 1j * RNG.standard_normal(
    n_delta.shape[0]
)
direct = spla.spsolve(n_delta - z_pencil * identity, rhs)
factored = c_op @ spla.spsolve(pencil, rhs)
solve_defect = float(np.linalg.norm(direct - factored) / np.linalg.norm(direct))
check(
    "E",
    "ordering check: N_delta-z=(A-z C_delta) C_delta^-1 and "
    "R_delta=C_delta(A-z C_delta)^-1 on the actual collar build",
    factor_defect < 1e-10 and solve_defect < 1e-9,
    f"matrix={factor_defect:.2e} solve={solve_defect:.2e}",
)

c0 = np.sqrt(ops["qs"].astype(complex) + 0j)
sqrt_ratios = []
for d in (0.3, 0.15, 0.075, 0.0375):
    cd = np.sqrt(ops["qs"].astype(complex) + 1j * d)
    sqrt_ratios.append(float(np.max(np.abs(cd - c0)) / np.sqrt(d)))
check(
    "E",
    "C_delta approaches C_0 uniformly at the wall with the expected "
    "O(sqrt(delta)) modulus",
    max(sqrt_ratios) < 2.0,
    f"ratios={[round(x, 4) for x in sqrt_ratios]}",
)

# A point-sampling grid that places the wall exactly on a node changes the
# continuum multiplication operator in a decisive way.  The continuum C_0
# can vanish on a measure-zero set while remaining injective on L2; the
# sampled C_0,N has a literal kernel.  Even with an invertible limiting pencil,
# C_0,N P_0,N^-1 is then noninjective and cannot be the resolvent of a densely
# defined operator (every operator resolvent is injective).
c0_wall_node = np.diag([1.0, 0.0, 1.0]).astype(complex)
p0_invertible = np.array(
    [[2.0, 0.2, 0.0], [0.0, 1.5, 0.1], [0.1, 0.0, 1.0]],
    dtype=complex,
)
r0_sampled = c0_wall_node @ np.linalg.inv(p0_invertible)
check(
    "F",
    "an exact wall-on-node discretization creates a noninjective limiting "
    "map, so its fixed-grid delta-to-zero limit is not an ordinary operator "
    "resolvent",
    np.linalg.matrix_rank(c0_wall_node) == 2
    and np.linalg.matrix_rank(r0_sampled) == 2,
    f"rank(C0)={np.linalg.matrix_rank(c0_wall_node)} "
    f"rank(R0)={np.linalg.matrix_rank(r0_sampled)}",
)


print("\n=== PART D: the prior coupled surrogate is wrong-type ===", flush=True)

shared_defects = []
commutators = []
for s in (U.S_STAR - 0.15, U.S_STAR, U.S_STAR + 0.12):
    def symbol(t: float):
        d = U.cvec(U.xi_of(t, U.ray(U.A_DN, float(s))))
        cs, _ct, p, _t, q = U.sec_parts(d)
        return (U.K_S @ cs / np.sqrt(p)) @ d, q

    ma, qa = symbol(U.T_OP)
    mb, qb = symbol(U.T2)
    shared = np.kron(ma, U.TAU1) + np.kron(mb, U.TAU3)
    target = (qa + qb) * np.eye(shared.shape[0], dtype=complex)
    commutators.append(opnorm(ma @ mb - mb @ ma))
    shared_defects.append(opnorm(shared @ shared - target))

wrong_type_detected = min(shared_defects) > 1.0 and np.allclose(
    shared_defects, commutators, rtol=1e-10, atol=1e-10
)
check(
    "F",
    "the shared-factor graded surrogate is not the categorical product and "
    "fails M2^2=(q_A+q_B)I by its nonzero commutator",
    wrong_type_detected,
    f"defects={[round(x, 4) for x in shared_defects]}",
)

d = 128
cartesian_dim = 2 * d
graded_tensor_dim = 2 * d * d
check(
    "F",
    "the exact graded tensor is a separate monoidal carrier, not the finite "
    "linear categorical product (dimension sum versus tensor dimension)",
    cartesian_dim != graded_tensor_dim,
    f"Cartesian={cartesian_dim} graded_tensor={graded_tensor_dim}",
)


all_ok = all(ok for _tag, _name, ok in RESULTS)
ne = sum(1 for tag, _name, _ok in RESULTS if tag == "E")
nf = sum(1 for tag, _name, _ok in RESULTS if tag == "F")
print("\n" + "=" * 78, flush=True)
if all_ok:
    print(
        "OUTCOME -> P-CARTESIAN: the Lawvere product lifts as a Krein "
        "direct sum; product norm-resolvent uniformity is algebraic once "
        "the per-object pencil is uniformly invertible. The coupled "
        "emergent-wall construction is a separate monoidal question.",
        flush=True,
    )
print(
    f"HEADLINE: {ne} [E] + {nf} [F] = {ne + nf}   "
    f"{'ALL PASS' if all_ok else 'FAILURES PRESENT'}",
    flush=True,
)
sys.exit(0 if all_ok else 1)
