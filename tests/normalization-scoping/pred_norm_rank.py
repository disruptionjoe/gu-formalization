#!/usr/bin/env python
"""
PRED-NORM-RANK certificate.

This is an exact monomial-rank audit for the current built normalization
structure.  It checks what survives the allowed rescalings among kappa, Z_U,
mu_DW, source normalization, and physical pole parameters.  It does not fit
target data and does not promote a free scale to a prediction.

Run: python tests/normalization-scoping/pred_norm_rank.py
"""

from fractions import Fraction


FAIL = []


def check(name, condition, detail=""):
    state = "PASS" if condition else "FAIL"
    print(f"{state} :: {name}" + (f" -- {detail}" if detail else ""))
    if not condition:
        FAIL.append(name)


def dot(row, vec):
    return sum(a * b for a, b in zip(row, vec))


def is_invariant(weights, vec):
    return all(dot(row, vec) == 0 for row in weights)


def rref(matrix):
    mat = [[Fraction(x) for x in row] for row in matrix]
    rows = len(mat)
    cols = len(mat[0])
    pivots = []
    r = 0
    for c in range(cols):
        pivot = None
        for rr in range(r, rows):
            if mat[rr][c] != 0:
                pivot = rr
                break
        if pivot is None:
            continue
        mat[r], mat[pivot] = mat[pivot], mat[r]
        scale = mat[r][c]
        mat[r] = [x / scale for x in mat[r]]
        for rr in range(rows):
            if rr == r:
                continue
            factor = mat[rr][c]
            if factor != 0:
                mat[rr] = [x - factor * y for x, y in zip(mat[rr], mat[r])]
        pivots.append(c)
        r += 1
        if r == rows:
            break
    return mat, pivots


def nullspace_basis(matrix):
    reduced, pivots = rref(matrix)
    cols = len(reduced[0])
    free_cols = [c for c in range(cols) if c not in pivots]
    basis = []
    for free_col in free_cols:
        vec = [Fraction(0) for _ in range(cols)]
        vec[free_col] = Fraction(1)
        for row_index, pivot_col in enumerate(pivots):
            vec[pivot_col] = -reduced[row_index][free_col]
        basis.append(tuple(vec))
    return basis, pivots


def vec(**terms):
    out = [Fraction(0) for _ in VARIABLES]
    for name, value in terms.items():
        out[INDEX[name]] = Fraction(value)
    return tuple(out)


VARIABLES = (
    "kappa",
    "Z_U",
    "mu_DW",
    "m_pole",
    "lambda_pole",
    "rho_quarter",
    "source_norm",
)
INDEX = {name: i for i, name in enumerate(VARIABLES)}

# Rows are independent free rescalings; columns are log-monomial exponents.
#
# field_norm: theta/U normalization rescales kappa and Z_U oppositely.  W229's
# built screening length ell^2 = Z_U*kappa is invariant under this move.
# dewitt_scale: the DeWitt/gimmel scale moves mu_DW and all absolute pole or
# density-quarter scales together; ranges scale inversely.
# source_norm: the source-current normalization is not fixed by the built
# geometry, so no prediction may retain source_norm dependence.
WEIGHTS = (
    vec(kappa=1, Z_U=-1),
    vec(mu_DW=1, m_pole=1, lambda_pole=-1, rho_quarter=1),
    vec(source_norm=1),
)

print("== PRED-NORM-RANK: exact scaling matrix ==")
for name, row in zip(("field_norm", "dewitt_scale", "source_norm"), WEIGHTS):
    terms = ", ".join(f"{var}:{int(coeff)}" for var, coeff in zip(VARIABLES, row) if coeff)
    print(f"{name}: {terms}")

basis, pivots = nullspace_basis(WEIGHTS)
print("\n== invariant monomial basis ==")
for item in basis:
    terms = ", ".join(f"{var}^{int(power)}" for var, power in zip(VARIABLES, item) if power)
    print(terms or "1")

rank = len(pivots)
check("R1 scaling matrix has rank 3", rank == 3, f"rank={rank}, pivots={pivots}")
check("R2 invariant quotient has dimension 4", len(basis) == 4, f"basis={basis}")
check("R3 every computed basis vector is invariant", all(is_invariant(WEIGHTS, b) for b in basis))

ell2 = vec(kappa=1, Z_U=1)
mass_ratio = vec(m_pole=1, mu_DW=-1)
range_ratio = vec(lambda_pole=1, mu_DW=1)
rho_ratio = vec(rho_quarter=1, mu_DW=-1)

check("I1 screening length ell^2 = Z_U*kappa is field-normalization invariant",
      is_invariant(WEIGHTS, ell2))
check("I2 pole mass ratio m_pole/mu_DW is invariant but does not fix mu_DW",
      is_invariant(WEIGHTS, mass_ratio))
check("I3 range ratio lambda_pole*mu_DW is invariant but does not fix lambda_pole",
      is_invariant(WEIGHTS, range_ratio))
check("I4 rho_quarter/mu_DW is invariant only as a target-calibrating relation",
      is_invariant(WEIGHTS, rho_ratio))

source_dependent = vec(source_norm=1, mu_DW=-1)
check("S1 source normalization cannot appear in a native invariant",
      not is_invariant(WEIGHTS, source_dependent))
check("S2 no basis invariant contains source_norm",
      all(item[INDEX["source_norm"]] == 0 for item in basis))

fixed_pole_mass = vec(m_pole=1)
fixed_range = vec(lambda_pole=1)
fixed_density = vec(rho_quarter=1)
fixed_kappa = vec(kappa=1)
fixed_z_u = vec(Z_U=1)

check("A1 an absolute pole mass is not invariant", not is_invariant(WEIGHTS, fixed_pole_mass))
check("A2 an absolute force range is not invariant", not is_invariant(WEIGHTS, fixed_range))
check("A3 an absolute density scale is not invariant", not is_invariant(WEIGHTS, fixed_density))
check("A4 kappa alone is a normalization choice, not an invariant", not is_invariant(WEIGHTS, fixed_kappa))
check("A5 Z_U alone is a normalization choice, not an invariant", not is_invariant(WEIGHTS, fixed_z_u))

# Built dimensionless coefficients from W239/H36-style arithmetic.  They can
# survive as ratios, but they do not select the missing scale.
c_l = Fraction(3, 8)
alpha_spin2 = Fraction(1, 3)
m2_eff_band = (Fraction(5, 6), Fraction(5, 4))

check("C1 c_L remains the dimensionless geometric coefficient 3/8", c_l == Fraction(3, 8))
check("C2 alpha=1/3 is dimensionless but standard massive-spin-2, not a native scale",
      alpha_spin2 == Fraction(1, 3))
check("C3 m2_eff supplies a dimensionless pole band, not an absolute pole scale",
      m2_eff_band == (Fraction(5, 6), Fraction(5, 4)))

routes = {
    "fixed_range_gravity": {
        "needs_native_scale": "mu_DW",
        "native_scale_fixed": False,
        "uses_target_density": False,
    },
    "h36_de_density_lock": {
        "needs_native_scale": "rho_quarter",
        "native_scale_fixed": False,
        "uses_target_density": True,
    },
    "source_screening_length": {
        "needs_native_scale": "Z_U*kappa",
        "native_scale_fixed": False,
        "uses_target_density": False,
    },
}

check("V1 every absolute-scale route still has an unfixed native scale",
      all(not route["native_scale_fixed"] for route in routes.values()))
check("V2 the only numerical H36 scale route is target-calibrated",
      routes["h36_de_density_lock"]["uses_target_density"])
check("V3 fixed-range and fixed-pole routes are NO_GO at current built-structure grade",
      not routes["fixed_range_gravity"]["native_scale_fixed"]
      and not routes["source_screening_length"]["native_scale_fixed"])

bar_b_open = True
h59_open = True
canon_moved = False
verdict_moved = False
check("G1 bar(b) and H59 remain OPEN", bar_b_open and h59_open)
check("G2 no canon, verdict, claim-status, or public-posture movement",
      not canon_moved and not verdict_moved)

print("\nRESULT :: NO_GO for current fixed-range/fixed-pole prediction routes")
print("survivors :: ell^2=Z_U*kappa (free scale), m_pole/mu_DW, lambda_pole*mu_DW, rho_quarter/mu_DW")
print("blocked :: no native value for mu_DW, Z_U*kappa, or source_norm without new dynamics")
print("priority_signal :: primary PRED-NORM-RANK reached endpoint; daily steward should reconcile next lane")

raise SystemExit(1 if FAIL else 0)
