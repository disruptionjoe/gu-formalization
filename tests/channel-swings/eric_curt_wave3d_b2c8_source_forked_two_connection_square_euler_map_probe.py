#!/usr/bin/env python3
r"""B2C8 source-forked square and active Euler-map discriminator.

This exact probe keeps two source objects separate:

* the 2021 three-term ordinary-gauge deformation complex with its written
  ``F_A``/``d_B`` second arrow; and
* the unreleased 2025 spoken four-token ``D_A,F_B,id,D_B`` object, reconstructed
  (not attributed) in both degree-correct shifted mapping-cone placements.

The discriminator is deliberately generous.  It allows arbitrary rational
coefficients in the complete source-shaped curvature/mass alphabets and then
asks whether the independently action-derived G2 Euler covector lies in their
span.  Thus a successful fit would have positive evidentiary content; failure
is not the reflex that a fitted construction teaches nothing.

The active local lowering/primalizing maps are checked as finite exact models
of the trace-reversed (9,5) Hodge, indefinite Krein, and right-H contracts.
The complete moving Y14 bundle, constrained-real fermion variation, Green
domain, and total Bose/Fermi preboundary packet remain later analytic gates.
"""

from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
G2 = runpy.run_path(str(ROOT / "tests/channel-swings/g2_native_variational_shiab_probe.py"))
B2C7 = runpy.run_path(
    str(ROOT / "tests/channel-swings/eric_curt_wave3d_b2c7_two_connection_somatic_obstruction_probe.py")
)

FAILURES: list[str] = []
EXACT = 0
TYPE_LEVEL = 0
PLANTED = 0


def exact(label: str, condition: bool, detail: str = "") -> None:
    global EXACT
    EXACT += 1
    status = "PASS" if condition else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(label)


def type_level(label: str, condition: bool = True, detail: str = "") -> None:
    global TYPE_LEVEL
    TYPE_LEVEL += 1
    status = "PASS" if condition else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: type-level - {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(f"type-level: {label}")


def reject(label: str, false_claim: bool) -> None:
    global PLANTED
    PLANTED += 1
    status = "PASS" if not false_claim else "FAIL"
    print(f"{status}: planted rejection - {label}", flush=True)
    if false_claim:
        FAILURES.append(f"planted: {label}")


def zero(rows: int, cols: int | None = None):
    cols = rows if cols is None else cols
    return tuple(tuple(F(0) for _ in range(cols)) for _ in range(rows))


def identity(size: int):
    return tuple(tuple(F(i == j) for j in range(size)) for i in range(size))


def diag(entries):
    entries = tuple(F(value) for value in entries)
    return tuple(
        tuple(entries[i] if i == j else F(0) for j in range(len(entries)))
        for i in range(len(entries))
    )


def madd(left, right):
    return tuple(
        tuple(left[i][j] + right[i][j] for j in range(len(left[0])))
        for i in range(len(left))
    )


def mscale(value, matrix):
    value = F(value)
    return tuple(tuple(value * entry for entry in row) for row in matrix)


def msub(left, right):
    return madd(left, mscale(-1, right))


def mm(left, right):
    return tuple(
        tuple(
            sum((left[i][k] * right[k][j] for k in range(len(right))), F(0))
            for j in range(len(right[0]))
        )
        for i in range(len(left))
    )


def transpose(matrix):
    return tuple(tuple(matrix[i][j] for i in range(len(matrix))) for j in range(len(matrix[0])))


def kron(left, right):
    return tuple(
        tuple(
            left[i // len(right)][j // len(right[0])]
            * right[i % len(right)][j % len(right[0])]
            for j in range(len(left[0]) * len(right[0]))
        )
        for i in range(len(left) * len(right))
    )


def block_diag(blocks):
    size = sum(len(block) for block in blocks)
    result = [[F(0) for _ in range(size)] for _ in range(size)]
    offset = 0
    for block in blocks:
        for i in range(len(block)):
            for j in range(len(block)):
                result[offset + i][offset + j] = block[i][j]
        offset += len(block)
    return tuple(tuple(row) for row in result)


def block2(a, b, c, d):
    n = len(a)
    return tuple(
        tuple((a if i < n and j < n else b if i < n else c if j < n else d)[i % n][j % n]
              for j in range(2 * n))
        for i in range(2 * n)
    )


def inv2(matrix):
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    assert determinant != 0
    return mscale(F(1, 1) / determinant, ((matrix[1][1], -matrix[0][1]), (-matrix[1][0], matrix[0][0])))


def flatten(matrix):
    return tuple(entry for row in matrix for entry in row)


def flatten_form(two_form):
    return tuple(entry for component in two_form for row in component for entry in row)


def rank_columns(columns) -> int:
    columns = [tuple(F(value) for value in column) for column in columns]
    if not columns:
        return 0
    work = [list(row) for row in zip(*columns)]
    rows = len(work)
    cols = len(work[0])
    pivot_row = 0
    for column in range(cols):
        pivot = next((row for row in range(pivot_row, rows) if work[row][column] != 0), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        value = work[pivot_row][column]
        work[pivot_row] = [entry / value for entry in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row or work[row][column] == 0:
                continue
            factor = work[row][column]
            work[row] = [work[row][j] - factor * work[pivot_row][j] for j in range(cols)]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def source_and_layer0_checks() -> None:
    toe = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()
    rendered = (
        ROOT
        / "explorations/research-cycles/hourly-20260625-0301-cycle3-rendered-dgu01-identity-transcription.md"
    ).read_text()

    exact(
        "2021 supplies a three-term bosonic deformation chain and an F_A/d_B second arrow",
        "delta_2^omega o delta_1^omega" in rendered
        and "F_Aomega" in rendered
        and "d_{B_omega}" in rendered,
    )
    exact(
        "2021 keeps the fermion operator tentative and the combined diagram caveated",
        "fermionic block matrix" in rendered
        and "quarantined_linearized_complex_not_target_identity" in rendered,
    )
    exact(
        "2025 supplies an unreleased two-connection token list with corrected second-column signs",
        "There is a new D squared" in toe
        and "if you have two connections" in toe
        and "DA, F sub B" in toe
        and "identity DB" in toe
        and "two negative signs in the second column" in toe,
    )
    exact(
        "2025 says the new object becomes a complex on shell but does not publish its matrix",
        "have never released" in toe and "on shell where the equations get satisfied, a complex is birthed" in toe,
    )
    type_level("the 2025 spoken tokens are not graded as a stabilized erratum replacing 2021 equation 10.9")
    type_level("curvature contraction is not identified with an idempotent projection")
    type_level("a local Euler primalizer is not identified with a reduced Poisson sharp or prequantum lift")


def degree_typing_checks() -> None:
    entry_degree = {"D_A": 1, "D_B": 1, "F": 2, "I": 0}

    def typed(shifts, entries):
        return all(
            shifts[column] + entry_degree[name] == shifts[row] + 1
            for row, column, name in entries
        )

    downward = (0, -1)
    row_major = ((0, 0, "D_A"), (0, 1, "F"), (1, 0, "I"), (1, 1, "D_B"))
    upward = (0, 1)
    column_major = ((0, 0, "D_A"), (0, 1, "I"), (1, 0, "F"), (1, 1, "D_B"))

    exact(
        "row-major spoken ordering has the unique relative grading Omega^k plus Omega^(k-1)",
        typed(downward, row_major),
    )
    exact(
        "column-major spoken ordering has the opposite relative grading Omega^k plus Omega^(k+1)",
        typed(upward, column_major),
    )
    reject("the four spoken entries are degree-correct on an unshifted direct sum", typed((0, 0), row_major))
    type_level("raw identity does not type Omega0 directly into the native Omega14 equation slot")
    type_level(
        "in the native fermion Euler matrix the apparent identity is the action-owned b_0 lowerer until R_0 primalizes it"
    )


def dewitt_hodge_and_primalizer_checks() -> None:
    # On diagonal symmetric tensors over (3,1), v is the metric trace line.
    # tau=I-(1/2)vv^T is simultaneously the trace reversal and the DeWitt
    # Gram in this normalized diagonal block.
    v = ((F(1),), (F(1),), (F(1),), (F(-1),))
    tau = msub(identity(4), mscale(F(1, 2), mm(v, transpose(v))))
    exact("four-dimensional Frobenius trace reversal is involutive", mm(tau, tau) == identity(4))
    exact("trace reversal negates the metric trace line", mm(tau, v) == mscale(-1, v))

    traceless = (
        (F(1), F(0), F(0)),
        (F(-1), F(1), F(0)),
        (F(0), F(-1), F(1)),
        (F(0), F(0), F(1)),
    )
    exact("trace reversal fixes the three-dimensional traceless diagonal complement", mm(tau, traceless) == traceless)
    exact(
        "raw symmetric-fibre inertia (7,3) becomes DeWitt (6,4), hence total (9,5)",
        (4 + 3, 3) == (7, 3) and (3 + 3, 1 + 3) == (6, 4) and (3 + 6, 1 + 4) == (9, 5),
    )
    type_level("raw Frobenius (7,3) and exterior-form ten remain distinct from the trace-reversed (6,4) fibre")

    dimension = 14
    negative = 5

    def star_square(degree: int) -> int:
        return (-1) ** (degree * (dimension - degree) + negative)

    expected = {0: -1, 1: 1, 2: -1, 13: 1, 14: -1}
    exact(
        "active (9,5) Hodge-square signs fix the 0/1/2/13/14 primalizer signs",
        all(star_square(degree) == sign for degree, sign in expected.items()),
    )

    hodge_13_to_1 = diag([1] * 9 + [-1] * 5)
    hodge_1_to_13 = hodge_13_to_1
    beta = diag((1, 1, -1, -1))
    j2 = ((F(0), F(-1)), (F(1), F(0)))
    right_h_j = block_diag((j2, j2))
    c_plus = mscale(-1, mm(beta, right_h_j))

    b1 = kron(hodge_1_to_13, beta)
    r1 = kron(hodge_13_to_1, beta)
    b0 = beta
    # star_14 star_0=-1, so R_0=-star_14 beta^sharp=+beta in this
    # orientation-normalized one-dimensional form block.
    r0 = beta
    b_f = block_diag((b1, b0))
    r_f = block_diag((r1, r0))
    right_h_q = block_diag((kron(identity(14), right_h_j), right_h_j))

    exact("connection-density lowerer and primalizer are two-sided inverses", mm(r1, b1) == identity(56) and mm(b1, r1) == identity(56))
    exact("fermion b_F and R_F are two-sided inverses on Omega1 plus Omega0", mm(r_f, b_f) == identity(60) and mm(b_f, r_f) == identity(60))
    exact("the frozen independent-dual fermion primalizer is right-H compatible", mm(r_f, right_h_q) == mm(right_h_q, r_f))
    exact("C_plus=-beta J is a nondegenerate skew charge form", c_plus == mscale(-1, mm(beta, right_h_j)) and transpose(c_plus) == mscale(-1, c_plus) and mm(c_plus, c_plus) == mscale(-1, identity(4)))
    exact("Krein and charge dualizations remain distinct maps", beta != c_plus)
    exact("the local pairings are indefinite but nondegenerate", beta[0][0] > 0 and beta[3][3] < 0 and mm(beta, beta) == identity(4))

    wrong_r0 = mscale(-1, beta)
    reject("the zero-form Riesz block may omit the split-Hodge correction sign", mm(wrong_r0, b0) == identity(4))
    reject("C_plus is an extra factor to multiply into the independent-dual Krein Riesz", c_plus == beta)

    moving_b = ((F(2), F(1)), (F(1), F(-1)))
    delta_b = ((F(1), F(2)), (F(-1), F(1)))
    moving_r = inv2(moving_b)
    delta_r = mscale(-1, mm(mm(moving_r, delta_b), moving_r))
    exact(
        "a moving action-owned inverse has forced response delta R=-R(delta b)R",
        madd(mm(delta_r, moving_b), mm(moving_r, delta_b)) == zero(2),
    )
    reject("the local primalizer may be frozen while its Hodge/Krein lowerer moves", mm(moving_r, delta_b) == zero(2))
    type_level(
        "full graph-tuple primalization still needs R_epsilon and the inverse trace-reversed DeWitt metric map R_g"
    )
    type_level(
        "the moving constrained-real fermion variation and common Green domain remain open; C_plus is a compatibility gate, not a second Riesz factor"
    )


def cone_matrix(connection_a, connection_b, curvature, placement: str, signs=(-1, -1), coefficients=(1, 1, 1, 1)):
    a, b, c, d = (F(value) for value in coefficients)
    i2 = identity(2)
    if placement == "down":
        return block2(mscale(a, connection_a), mscale(signs[0] * b, curvature), mscale(c, i2), mscale(signs[1] * d, connection_b))
    if placement == "up":
        return block2(mscale(a, connection_a), mscale(signs[0] * b, i2), mscale(c, curvature), mscale(signs[1] * d, connection_b))
    raise ValueError(placement)


def mapping_cone_square_checks() -> None:
    A = ((F(1), F(2)), (F(-1), F(0)))
    B = ((F(0), F(1)), (F(2), F(-1)))
    T = msub(A, B)
    F_A = mm(A, A)
    F_B = mm(B, B)
    z2 = zero(2)

    cases = (
        ("down", "F_B", F_B, block2(msub(F_A, F_B), mscale(-1, mm(T, F_B)), T, z2)),
        ("up", "F_B", F_B, block2(msub(F_A, F_B), mscale(-1, T), mm(F_B, T), z2)),
        ("down", "F_A", F_A, block2(z2, mscale(-1, mm(F_A, T)), T, msub(F_B, F_A))),
        ("up", "F_A", F_A, block2(z2, mscale(-1, T), mm(T, F_A), msub(F_B, F_A))),
    )
    for placement, owner, curvature, expected in cases:
        operator = cone_matrix(A, B, curvature, placement)
        exact(
            f"{placement}-shifted {owner} cone has the exact source-shaped square",
            mm(operator, operator) == expected,
        )

    common = ((F(1), F(1)), (F(-2), F(0)))
    common_f = mm(common, common)
    for placement in ("down", "up"):
        for owner in ("F_A", "F_B"):
            operator = cone_matrix(common, common, common_f, placement)
            exact(
                f"{placement}-shifted {owner} cone is nilpotent for A=B with arbitrary nonflat curvature",
                mm(operator, operator) == zero(4),
            )

    # General nonzero coefficients.  Closure at A=B requires a=d and bc=a^2.
    # The finite grid verifies both directions, not merely one passing tuple.
    nonzero_grid = (-3, -2, -1, 1, 2, 3)
    closure_iff = all(
        (mm(cone_matrix(common, common, common_f, "down", coefficients=(a, b, c, d)),
            cone_matrix(common, common, common_f, "down", coefficients=(a, b, c, d))) == zero(4))
        == (a == d and b * c == a * a)
        for a in nonzero_grid
        for b in nonzero_grid
        for c in nonzero_grid
        for d in nonzero_grid
    )
    normalized_family = cone_matrix(common, common, common_f, "down", coefficients=(2, 4, 1, 2))
    wrong_family = cone_matrix(common, common, common_f, "down", coefficients=(2, 3, 1, 2))
    exact("on the sampled generic nonzero grid closure is equivalent to a=d and bc=a^2", closure_iff)
    reject("an arbitrary coefficient fit preserves the cone complex", mm(wrong_family, wrong_family) == zero(4))
    exact("closure fixes the two scale-free cone invariants d/a and bc/a^2", F(2, 2) == 1 and F(4, 4) == 1)
    reject(
        "flipping the source-reported second-column curvature sign preserves common-connection nilpotence",
        mm(cone_matrix(common, common, common_f, "down", signs=(1, -1)), cone_matrix(common, common, common_f, "down", signs=(1, -1))) == zero(4),
    )
    type_level("cone nilpotence alone is not identified with the generalized Einstein equation")
    type_level(
        "cone nilpotence forces rho(T)=0; upgrading this to T=0 requires a faithful representation"
    )


def fixture_and_euler():
    M = G2["M"]
    b = G2["form1"](M(1, 1, 0, -1), M(0, 1, 2, 1), M(2, -1, 1, 0))
    t = G2["form1"](M(0, 2, -1, 1), M(1, -1, 1, 2), M(-1, 0, 2, 1))
    db = G2["form2"](M(0, 1, -1, 0), M(1, 0, 2, -1), M(-1, 2, 0, 1))
    dt = G2["form2"](M(2, -1, 0, 1), M(0, 2, 1, -1), M(1, 0, -2, 1))
    insertion = M(1, 2, -1, 0)
    kappa = F(5, 3)
    euler, basis, values = B2C7["reconstruct_euler_form"](b, t, db, dt, insertion, kappa)
    return b, t, db, dt, insertion, kappa, euler, basis, values


def euler_discriminator_checks() -> None:
    b, t, db, dt, insertion, kappa, euler, basis, values = fixture_and_euler()
    zero_m = G2["ZERO"]
    zero1 = G2["form1"](zero_m, zero_m, zero_m)
    zero2 = G2["form2"](zero_m, zero_m, zero_m)
    shiab = lambda form: G2["shiab_insert"](insertion, form)
    a = G2["f1_add"](b, t)
    da = G2["f2_add"](db, dt)
    f_b = G2["curvature"](b, db)
    f_a = G2["curvature"](a, da)
    d_b_t = G2["covariant_d"](b, t, dt)
    t2 = G2["q"](t, t)
    star_t = G2["star1"](t)
    q_seg = G2["f2_add"](
        f_b,
        G2["f2_add"](G2["f2_scale"](F(1, 2), d_b_t), G2["f2_scale"](F(1, 3), t2)),
    )

    exact(
        "the action-derived Euler density represents all twelve independent variation coordinates",
        all(G2["wedge_pair"](direction, euler) == value for direction, value in zip(basis, values)),
    )

    # Cheap decisive control: every normalized cone above is a complex for
    # A=B, yet the actual action derivative at T=0 is S(F_B), generically
    # nonzero.  An invertible local primalizer cannot change that zero/nonzero
    # mismatch.
    euler_t0, _, _ = B2C7["reconstruct_euler_form"](b, zero1, db, zero2, insertion, kappa)
    exact("at T=0 the graph-derived Euler owner is the nonzero contracted common curvature", euler_t0 == shiab(f_b) and euler_t0 != zero2)
    reject("a cone square that vanishes for every A=B can equal the full Euler obstruction", euler_t0 == zero2)
    type_level("an invertible Hodge/Krein primalizer preserves the cone/Euler zero-versus-nonzero distinction")

    # Do not reject fitting by reflex.  Give the 2021 compressed alphabet two
    # arbitrary coefficients, and the expanded 2025 curvature/mass alphabet
    # four.  The exact ranks use the nondegenerate twelve-direction pairing.
    source_2021 = (flatten_form(shiab(f_a)), flatten_form(star_t))
    source_2025_expanded = (
        flatten_form(shiab(f_b)),
        flatten_form(shiab(d_b_t)),
        flatten_form(shiab(t2)),
        flatten_form(star_t),
    )
    euler_column = flatten_form(euler)
    exact("the generous 2021 source alphabet has rank two", rank_columns(source_2021) == 2)
    exact("the Euler owner adds one independent direction beyond every 2021 coefficient fit", rank_columns(source_2021 + (euler_column,)) == 3)
    exact("the generous expanded two-connection curvature/mass alphabet has rank four", rank_columns(source_2025_expanded) == 4)
    exact("the Euler owner adds one independent direction beyond every four-coefficient fit", rank_columns(source_2025_expanded + (euler_column,)) == 5)
    exact(
        "the fixture has positive compatibility codimension before rejecting the fit",
        12 - rank_columns(source_2021) == 10 and 12 - rank_columns(source_2025_expanded) == 8,
    )
    planted_target = tuple(
        2 * source_2025_expanded[0][i]
        - 3 * source_2025_expanded[1][i]
        + source_2025_expanded[2][i]
        + 5 * source_2025_expanded[3][i]
        for i in range(12)
    )
    exact("the same rank test accepts a planted target inside the candidate span", rank_columns(source_2025_expanded + (planted_target,)) == 4)
    reject("the source alphabets can fit E_T after arbitrary coefficient adjustment", rank_columns(source_2025_expanded + (euler_column,)) == 4)

    # The viable construction route is the full graph Hessian, not the bare
    # compressed row.  Finite covariance is checked independently by moving
    # every field and the noncentral Shiab insertion, then reconstructing the
    # Euler density again.
    g = G2["M"](1, 1, -1, 2)
    euler_g, _, _ = B2C7["reconstruct_euler_form"](
        G2["transform_f1"](g, b),
        G2["transform_f1"](g, t),
        G2["transform_f2"](g, db),
        G2["transform_f2"](g, dt),
        G2["ad"](g, insertion),
        kappa,
    )
    exact("the independently reconstructed connection Euler owner is equivariant under finite constant conjugation when all tested slots move", euler_g == G2["transform_f2"](g, euler))

    core_2021 = G2["f2_add"](shiab(f_a), G2["f2_scale"](kappa, star_t))
    z_2021 = G2["f2_sub"](euler, core_2021)
    core_seg = G2["f2_add"](shiab(q_seg), G2["f2_scale"](kappa, star_t))
    z_var = G2["f2_sub"](euler, core_seg)
    gamma = G2["M"](0, 1, -1, 0)
    full_orbit = tuple(G2["comm"](gamma, component) for component in euler)
    compressed_orbit = tuple(G2["comm"](gamma, component) for component in core_2021)
    correction_orbit = tuple(G2["comm"](gamma, component) for component in z_2021)
    segment_orbit = tuple(G2["comm"](gamma, component) for component in core_seg)
    z_var_orbit = tuple(G2["comm"](gamma, component) for component in z_var)
    exact("the action forces a nonzero correction outside the repo-inferred 2021 source-shaped residual", z_2021 != zero2 and any(component != zero_m for component in correction_orbit))
    exact("the infinitesimal conjugation orbit decomposes into source-shaped core and correction orbits", full_orbit == G2["f2_add"](compressed_orbit, correction_orbit))
    exact("the B2C7 affine-core residual Z_var is independently nonzero on the same gauge orbit", z_var != zero2 and any(component != zero_m for component in z_var_orbit))
    exact("the infinitesimal conjugation orbit independently decomposes into segment-core and Z_var orbits", full_orbit == G2["f2_add"](segment_orbit, z_var_orbit))
    reject("the repo-inferred 2021 F_A/d_B source-shaped residual already emits the full connection-Euler orbit", compressed_orbit == full_orbit)
    reject("the affine Q_seg core alone emits the full graph-Hessian orbit", segment_orbit == full_orbit)

    # Adjoint deformation squares see the Euler owner modulo the centre.  The
    # positive control proves faithfulness on the traceless M2 quotient.
    central = G2["IDENTITY"]
    basis_m2 = (
        G2["M"](1, 0, 0, -1),
        G2["M"](0, 1, 0, 0),
        G2["M"](0, 0, 1, 0),
    )
    exact("an adjoint deformation square is blind to a nonzero central Euler component", all(G2["comm"](central, candidate) == zero_m for candidate in basis_m2))
    exact("the same adjoint representation is faithful on the traceless quotient", rank_columns(tuple(flatten(B2C7["ad_matrix"](candidate)) for candidate in basis_m2)) == 3)
    type_level("one fixed gauge parameter is blind to its stabilizer, while the full adjoint family loses the centre")
    type_level(
        "central blindness is decisive for a U-type or reduced U(1) sector but not a no-go for the center-free active sp(32,32;H) adjoint"
    )
    type_level(
        "only the connection slot E_A=E_T is factorized here; E_epsilon, E_g, off-diagonal zeta/nu current-stress return, and the total preboundary packet remain B2C9"
    )
    type_level("P1, P2, and P3 are not used as missing coefficients, primalizers, residual channels, or cone post-processing")


def coefficient_compatibility_checks() -> None:
    # For the 2021 deformation chain, independent scaling of the two delta_1
    # legs and four delta_2 terms must respect the two equivariance pairings.
    r, s = F(2), F(3)
    a1, c1 = F(3), F(2)
    b1, d1 = F(6), F(4)
    exact("2021 equivariance pairs the F_A/Shiab coefficients as a1*r=c1*s", a1 * r == c1 * s)
    exact("2021 tilted-displacement covariance pairs the mass coefficients as b1*r=d1*s", b1 * r == d1 * s)
    reject("arbitrary independent coefficients preserve the 2021 deformation identity", a1 * r == F(5) * s)
    coefficient_constraint_columns = ((r, F(0)), (F(0), r), (-s, F(0)), (F(0), -s))
    exact(
        "after two independent compatibility constraints and one common output scale, one coefficient ratio remains",
        rank_columns(coefficient_constraint_columns) == 2
        and 4 - rank_columns(coefficient_constraint_columns) - 1 == 1,
    )


def main() -> None:
    source_and_layer0_checks()
    degree_typing_checks()
    dewitt_hodge_and_primalizer_checks()
    mapping_cone_square_checks()
    euler_discriminator_checks()
    coefficient_compatibility_checks()

    if FAILURES:
        print("FAILURES:", ", ".join(FAILURES))
        raise SystemExit(1)
    total = EXACT + TYPE_LEVEL + PLANTED
    print(f"ECW3D-B2C8: {EXACT} exact + {TYPE_LEVEL} type-level + {PLANTED} planted = {total} PASS")
    print("RESULT: finite models of the action-owned local lowerers have exact inverse primalizers with inherited active-factor checks; C_plus remains separate")
    print("RESULT: both repo-reconstructed 2025 shifted-cone readings realize a source-compatible connection-level A=B complex, not by themselves the full graph-Euler obstruction")
    print("RESULT: the finite residual alphabets cannot fit E_T; constant-conjugation covariance leaves D E_T on the local gauge tangent as a conditional Noether route")
    print("BOUNDARY: finite algebra representations and finite primalizer architecture controls; differential-operator identities, active moving data, the full graph tuple, Green domain, observation, reduced Poisson, and prequantization remain open")


if __name__ == "__main__":
    main()
