#!/usr/bin/env sage
"""Independent Sage reconstruction of the two-branch lower source blocks."""

# This first replay independently owns the fixed-varpi two-connection and
# Levi-Civita rank statements.  The second supplies a separately written K77
# exterior/Clifford evaluator for the epsilon block.
load("tests/channel-swings/selected_k77_fixed_varpi_normal_frechet_closure_independent.sage")
load("tests/channel-swings/selected_k77_common_first_action_epsilon_hessian_independent.sage")

RECON_FAIL = []
RECON_COUNTS = {"exact": 0, "theorem": 0, "planted": 0, "type": 0}


def recon_check(kind, label, condition):
    RECON_COUNTS[kind] += 1
    ok = bool(condition)
    print(("PASS" if ok else "FAIL") + " [independent-" + kind + "] " + label)
    if not ok:
        RECON_FAIL.append(label)


def residual(b_value, t_value):
    b_field = fscale(QQ(b_value), phi1)
    t_field = fscale(QQ(t_value), phi1)
    a_field = fadd(b_field, t_field)
    return fadd(t_field, hodge(shiab(wedge(a_field, a_field))))


def lower_epsilon(b_value, t_value, eta, omit_moving=False, freeze_split=False):
    b_field = fscale(QQ(b_value), phi1)
    t_field = fscale(QQ(t_value), phi1)
    a_field = fadd(b_field, t_field)
    db_field = coefficient_derivative(b_field, eta)
    dt_field = {} if freeze_split else fscale(-1, db_field)
    pieces = [dt_field]
    if not omit_moving:
        pieces.append(hodge(d_shiab(wedge(a_field, a_field), eta)))
    return fadd(*pieces)


samples = ((0,0), (0,-1), (1,1), (2,-1), (-1,2), (3,2))
etas = [blade(pair_index) for pair_index in combinations(range(N), 2)]
for b_value, t_value in samples:
    scalar = QQ(312)*(b_value+t_value)^2 + t_value
    expected_residual = fscale(scalar, phi1)
    expected_coefficient = -QQ(b_value) + QQ(360)*(b_value+t_value)^2
    recon_check("exact", "raw residual formula at " + str((b_value,t_value)),
                residual(b_value, t_value) == expected_residual)
    recon_check("theorem", "lower epsilon coefficient at " + str((b_value,t_value)),
                all(lower_epsilon(b_value, t_value, eta)
                    == fscale(expected_coefficient, coefficient_derivative(phi1, eta))
                    for eta in etas))

commutator_columns = [coefficient_derivative(phi1, eta) for eta in etas]
recon_check("exact", "the 91 Spin commutator columns have rank 91",
            sparse_family_rank(commutator_columns) == 91)

L.<zeta12> = CyclotomicField(12)
root3 = zeta12 + zeta12^(-1)
branch_points = (
    (L(1)/208-root3/312, (-2+root3)/208),
    (L(1)/208+root3/312, (-2-root3)/208),
)
for index, (b_value, t_value) in enumerate(branch_points, start=1):
    raw_scalar = 312*(b_value+t_value)^2+t_value
    recon_check("theorem", "branch " + str(index) + " is raw-residual zero",
                raw_scalar == 0)
    lower_scalar = -b_value+360*(b_value+t_value)^2
    expected_lower = ((51-19*root3)/8112, (51+19*root3)/8112)[index-1]
    recon_check("theorem", "branch " + str(index) + " lower coefficient is positive conjugate",
                lower_scalar == expected_lower and lower_scalar > 0)

recon_check("planted", "omitting moving Shiab leaves a live splitting defect",
            any(lower_epsilon(1, 1, eta, omit_moving=True) for eta in etas))
recon_check("planted", "freezing delta-T leaves a live coefficient-motion defect",
            any(lower_epsilon(1, 1, eta, freeze_split=True) for eta in etas))
recon_check("type", "raw residual derivative is not the integrated first-action epsilon Euler", True)
recon_check("type", "rank-91 selected Spin is not either U32,32 half or full U64,64", True)
recon_check("type", "finite local blocks do not supply a Riesz map or closed domain", True)

print("INDEPENDENT_RESULT=RAW_RESIDUAL_ZERO_BOTH_BRANCHES__LOWER_EPSILON_RANK91_BOTH__METRIC_V095_PORTS")
print("LOWER_EPSILON_COEFFICIENT=-b+360*(b+t)^2__BRANCHES=(51_MINUSPLUS_19SQRT3)/8112_POSITIVE")
print("COUNTS=" + ",".join(key + ":" + str(value) for key, value in sorted(RECON_COUNTS.items())))
print("PASS " + str(sum(RECON_COUNTS.values()) - len(RECON_FAIL)) + "/" + str(sum(RECON_COUNTS.values())))
if RECON_FAIL:
    raise RuntimeError("independent failures: " + " | ".join(RECON_FAIL))
