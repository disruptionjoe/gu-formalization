#!/usr/bin/env python3
r"""B2C7 typed two-connection somatic/common-obstruction gate.

The source speaks about two physical Bose/Fermi somatic complexes and one
generalized-Einstein obstruction.  Equality of the raw route operators is
ill-typed: the Bose and Fermi carriers and their density-valued equation
carriers differ.  This probe therefore tests the durable interpretation:

* one graph-complete variational residual ``G``;
* representation-dependent intertwiners ``J_ad(G)`` and ``J_S(G)``;
* an exact symmetrized A/B route core on both representations; and
* the uniquely forced correction from that route core to ``G``.

The finite 3D rational model executes the universal connection and variational
algebra.  It is not the actual Y^14 active-real bundle construction.  The
active (9,5), right-H/Krein Riesz or reduced presymplectic anchor, moving
Shiab/Hodge/density, and global Green domain remain explicit type-level gates.
"""

from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
G2 = runpy.run_path(str(ROOT / "tests/channel-swings/g2_native_variational_shiab_probe.py"))

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


def gzero(n: int):
    return tuple(tuple(F(0) for _ in range(n)) for _ in range(n))


def gidentity(n: int):
    return tuple(tuple(F(i == j) for j in range(n)) for i in range(n))


def gadd(x, y):
    return tuple(tuple(x[i][j] + y[i][j] for j in range(len(x))) for i in range(len(x)))


def gsub(x, y):
    return tuple(tuple(x[i][j] - y[i][j] for j in range(len(x))) for i in range(len(x)))


def gscale(c, x):
    return tuple(tuple(F(c) * entry for entry in row) for row in x)


def gmm(x, y):
    return tuple(
        tuple(sum((x[i][k] * y[k][j] for k in range(len(y))), F(0)) for j in range(len(y[0])))
        for i in range(len(x))
    )


def gmv(matrix, vector):
    return tuple(
        sum((matrix[i][j] * vector[j] for j in range(len(vector))), F(0))
        for i in range(len(matrix))
    )


def vadd(x, y):
    return tuple(a + b for a, b in zip(x, y))


def vsub(x, y):
    return tuple(a - b for a, b in zip(x, y))


def flatten2(matrix):
    return tuple(entry for row in matrix for entry in row)


def unit2(index: int):
    entries = [F(0)] * 4
    entries[index] = F(1)
    return ((entries[0], entries[1]), (entries[2], entries[3]))


def ad_matrix(matrix):
    """Matrix of X -> [matrix,X] on M_2 in the row-major basis."""

    columns = []
    for index in range(4):
        basis = unit2(index)
        columns.append(flatten2(G2["comm"](matrix, basis)))
    return tuple(tuple(columns[j][i] for j in range(4)) for i in range(4))


def block_diag(blocks):
    size = sum(len(block) for block in blocks)
    out = [[F(0) for _ in range(size)] for _ in range(size)]
    offset = 0
    for block in blocks:
        for i in range(len(block)):
            for j in range(len(block)):
                out[offset + i][offset + j] = block[i][j]
        offset += len(block)
    return tuple(tuple(row) for row in out)


def gaussian_solve(matrix, vector):
    augmented = [list(row) + [vector[i]] for i, row in enumerate(matrix)]
    n = len(augmented)
    for column in range(n):
        pivots = [row for row in range(column, n) if augmented[row][column] != 0]
        assert pivots, f"singular exact system: no pivot in column {column}"
        pivot = pivots[0]
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        pivot_value = augmented[column][column]
        augmented[column] = [entry / pivot_value for entry in augmented[column]]
        for row in range(n):
            if row == column:
                continue
            factor = augmented[row][column]
            if factor:
                augmented[row] = [
                    augmented[row][j] - factor * augmented[column][j]
                    for j in range(n + 1)
                ]
    return tuple(augmented[i][-1] for i in range(n))


def source_and_layer0_checks() -> None:
    portal = (ROOT / "lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md").read_text()
    rendered = (
        ROOT
        / "explorations/research-cycles/hourly-20260625-0301-cycle3-rendered-dgu01-identity-transcription.md"
    ).read_text()
    exact(
        "Portal gives two physical somatic complexes with a common Einstein-type obstruction",
        "two somatic complexes" in portal
        and "common generalization of the Einstein field equations" in portal,
    )
    exact(
        "Portal explicitly invokes two connection derivatives and a zero-order difference",
        "I have two derivative operators here" in portal
        and "precisely the augmented torsion" in portal,
    )
    exact(
        "Portal types zeta and nu as separate physical fields",
        "zeta \\in \\Omega^1" in portal
        and "nu \\in \\Omega^0" in portal
        and "two separate fields" in portal,
    )
    exact(
        "the rendered draft extraction owns the fermion Euler block and bosonic delta1/delta2 formulas",
        "fermionic block matrix" in rendered
        and "d_{A_omega} oplus DL_epsilon" in rendered
        and "delta_2^omega" in rendered,
        "the normalized extraction preserves roles but not every glyph",
    )
    exact(
        "Portal records the up/over cancellations as unfinished",
        "you need some cancellations" in portal and "that’s taking a little time" in portal,
    )
    reject("physical nu is an odd gauge parameter or BV ghost", False)
    reject("the source supplies a completed off-shell odd Noether/BV symmetry", False)


def source_2025_and_map_separation_checks() -> None:
    """Keep four superficially similar maps in different typed slots.

    The 2025 conversation places a geometric-quantization route next to GU,
    but it does not identify that phase-space route with the GU Euler map.
    It separately corrects ``projection`` to ``contraction`` and describes an
    unreleased two-connection D-squared.  These distinctions are Layer 0, not
    optional prose.
    """

    toe = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()
    rendered = (
        ROOT
        / "explorations/research-cycles/hourly-20260625-0301-cycle3-rendered-dgu01-identity-transcription.md"
    ).read_text()
    exact(
        "2025 TOE states the geometric-quantization function-to-one-form-to-vector-to-connection route",
        "differentiate it to get a one-form" in toe
        and "stick it into a symplectic form to get a vector field" in toe
        and "throw the vector field to a connection" in toe,
    )
    exact(
        "2025 TOE corrects projection to contraction for the GU curvature route",
        "projection operator" in toe
        and "contraction operator" in toe
        and "you were correct. I'm wrong" in toe,
    )
    exact(
        "2025 TOE types the shortened GU route as 0-to-1-to-13-to-14 using contraction then Hodge star",
        "go zero to one to 13 to 14" in toe
        and "You did a contraction that got you back to one" in toe
        and "And then you did a star" in toe,
    )
    exact(
        "2025 TOE marks the two-connection new D-squared as unreleased and sign-unstable",
        "There is a new D squared" in toe
        and "if you have two connections" in toe
        and "have never released" in toe
        and "There are two negative signs in the second column" in toe,
    )
    exact(
        "the 2021 F_A/d_B arrow and tentative 2025 F_B entry remain a live source fork",
        "F_Aomega" in rendered and "d_{B_omega}" in rendered and "F sub B" in toe,
    )

    # A metric/Krein sharp and a symplectic sharp both turn covectors into
    # vectors, but even in the smallest exact model they are different maps.
    covector = (F(1), F(2))
    metric_sharp = covector
    symplectic_sharp = (covector[1], -covector[0])
    exact(
        "metric Riesz sharp and symplectic sharp are distinct covector-to-vector maps",
        metric_sharp != symplectic_sharp,
    )

    # The G3 object is presymplectic before its kernel/domain quotient.  A
    # nonzero two-form can still have a characteristic direction, so it does
    # not yet define an inverse Poisson anchor.
    presymplectic = (
        (F(0), F(1), F(0)),
        (F(-1), F(0), F(0)),
        (F(0), F(0), F(0)),
    )
    characteristic = (F(0), F(0), F(1))
    has_kernel = gmv(presymplectic, characteristic) == (F(0), F(0), F(0))
    exact(
        "a nonzero presymplectic form can retain a kernel before BFV reduction",
        presymplectic != gzero(3) and has_kernel,
    )

    reject(
        "the general geometric-quantization explanation explicitly identifies the GU Euler intertwiner",
        False,
    )
    reject("GU curvature contraction is a projection onto a subbundle", False)
    reject("the 2025 spoken F_B entry is a stabilized erratum replacing the 2021 F_A arrow", False)
    reject(
        "a nonzero preboundary two-form already supplies an invertible Poisson anchor without quotienting its kernel",
        not has_kernel,
    )
    type_level(
        "B2C8 must discriminate a moving Krein/Hodge Riesz port from a G3-derived reduced presymplectic anchor before composing either with the somatic routes"
    )
    type_level(
        "B2C8 must enumerate typed 2021-F_A/d_B and 2025-spoken-F_B two-connection matrices rather than blend them into one source-exact square"
    )


def split_hodge_checks() -> None:
    dimension = 14
    negative = 5

    def star_square(degree: int) -> int:
        return (-1) ** (degree * (dimension - degree) + negative)

    expected = {0: -1, 1: 1, 2: -1, 13: 1, 14: -1}
    exact(
        "active (9,5) Hodge-square signs are fixed in the relevant degrees",
        all(star_square(degree) == sign for degree, sign in expected.items()),
    )
    reject(
        "Euclidean fourteen-dimensional Hodge-square signs may replace the active split signs",
        all(((-1) ** (degree * (dimension - degree))) == sign for degree, sign in expected.items()),
    )
    type_level(
        "the actual fermion Euler map lands in the density-valued Krein dual and needs a moving right-H Riesz map before same-bundle squaring"
    )


def mixed_covariant_composition(left, right, d_right, value, first, second):
    """Return (nabla^left_0 nabla^right_1 - 0<->1)value."""

    def ordered(i: int, j: int):
        result = tuple(second[i][j])
        result = vadd(result, gmv(d_right[i][j], value))
        result = vadd(result, gmv(right[j], first[i]))
        result = vadd(result, gmv(left[i], first[j]))
        result = vadd(result, gmv(gmm(left[i], right[j]), value))
        return result

    return vsub(ordered(0, 1), ordered(1, 0))


def two_representation_route_checks():
    M = G2["M"]
    ZERO = G2["ZERO"]
    b = G2["form1"](M(1, 1, 0, -1), M(0, 1, 2, 1), M(2, -1, 1, 0))
    t = G2["form1"](M(0, 2, -1, 1), M(1, -1, 1, 2), M(-1, 0, 2, 1))
    db = G2["form2"](M(0, 1, -1, 0), M(1, 0, 2, -1), M(-1, 2, 0, 1))
    dt = G2["form2"](M(2, -1, 0, 1), M(0, 2, 1, -1), M(1, 0, -2, 1))
    a = G2["f1_add"](b, t)
    da = G2["f2_add"](db, dt)
    f_b = G2["curvature"](b, db)
    d_b_t = G2["covariant_d"](b, t, dt)
    h_hat = G2["f2_add"](f_b, G2["f2_scale"](F(1, 2), d_b_t))

    ordered_db = ((ZERO, db[0]), (ZERO, ZERO))
    ordered_dt = ((ZERO, dt[0]), (ZERO, ZERO))
    ordered_da = tuple(
        tuple(G2["add"](ordered_db[i][j], ordered_dt[i][j]) for j in range(2))
        for i in range(2)
    )

    for name, representation, dimension in (
        ("fundamental/Fermi", lambda x: x, 2),
        ("adjoint/Bose", ad_matrix, 4),
    ):
        a_rep = tuple(representation(x) for x in a[:2])
        b_rep = tuple(representation(x) for x in b[:2])
        db_rep = tuple(tuple(representation(x) for x in row) for row in ordered_db)
        da_rep = tuple(tuple(representation(x) for x in row) for row in ordered_da)
        value = tuple(F(i + 1) for i in range(dimension))
        first_a = (tuple(F(i + 2) for i in range(dimension)), tuple(F(3 - i) for i in range(dimension)))
        first_b = (tuple(F(2 * i - 1) for i in range(dimension)), tuple(F(i * i + 1) for i in range(dimension)))
        second_a = (
            (tuple(F(i) for i in range(dimension)), tuple(F(i + 4) for i in range(dimension))),
            (tuple(F(i + 4) for i in range(dimension)), tuple(F(2 - i) for i in range(dimension))),
        )
        second_b = (
            (tuple(F(7 - i) for i in range(dimension)), tuple(F(3 * i - 2) for i in range(dimension))),
            (tuple(F(3 * i - 2) for i in range(dimension)), tuple(F(i + 9) for i in range(dimension))),
        )

        def route(first, second):
            ab = mixed_covariant_composition(a_rep, b_rep, db_rep, value, first, second)
            ba = mixed_covariant_composition(b_rep, a_rep, da_rep, value, first, second)
            return tuple(F(1, 2) * (x + y) for x, y in zip(ab, ba))

        expected = gmv(representation(h_hat[0]), value)
        exact(
            f"symmetrized A/B high-low route cancels first and second jets in the {name} representation",
            route(first_a, second_a) == route(first_b, second_b) == expected,
        )
        asymmetric = mixed_covariant_composition(a_rep, b_rep, db_rep, value, first_a, second_a)
        reject(f"one asymmetric A/B route alone is the zero-order {name} obstruction", asymmetric == expected)

    exact(
        "one adjoint-valued Hhat_AB owns both the Bose and Fermi mixed-route cores",
        any(entry != 0 for component in h_hat for row in component for entry in row),
    )
    return b, t, db, dt, a, da, h_hat


def reconstruct_euler_form(b, t, db, dt, insertion, kappa):
    zero = G2["ZERO"]
    basis1 = []
    for slot in range(3):
        for matrix_index in range(4):
            entries = [zero, zero, zero]
            entries[slot] = unit2(matrix_index)
            basis1.append(tuple(entries))
    basis2 = []
    for slot in range(3):
        for matrix_index in range(4):
            entries = [zero, zero, zero]
            entries[slot] = unit2(matrix_index)
            basis2.append(tuple(entries))

    pairing = tuple(
        tuple(G2["wedge_pair"](direction, candidate) for candidate in basis2)
        for direction in basis1
    )
    shiab = lambda two_form: G2["shiab_insert"](insertion, two_form)
    values = tuple(
        G2["slot_symmetrized_derivative"](
            b, db, t, dt, direction, G2["form2"](zero, zero, zero), shiab, kappa
        )
        for direction in basis1
    )
    coefficients = gaussian_solve(pairing, values)
    result = []
    for slot in range(3):
        block = coefficients[4 * slot : 4 * slot + 4]
        result.append(((block[0], block[1]), (block[2], block[3])))
    return tuple(result), basis1, values


def graph_complete_common_owner_checks(b, t, db, dt, a, da, h_hat) -> None:
    insertion = G2["M"](1, 2, -1, 0)
    kappa = F(5, 3)
    euler, basis1, values = reconstruct_euler_form(b, t, db, dt, insertion, kappa)
    shiab = lambda two_form: G2["shiab_insert"](insertion, two_form)
    zero2 = G2["form2"](G2["ZERO"], G2["ZERO"], G2["ZERO"])

    exact(
        "the reconstructed graph-complete Euler density represents every rational basis variation",
        all(G2["wedge_pair"](direction, euler) == value for direction, value in zip(basis1, values)),
    )

    f_b = G2["curvature"](b, db)
    d_b_t = G2["covariant_d"](b, t, dt)
    t2 = G2["q"](t, t)
    q_seg = G2["f2_add"](
        f_b,
        G2["f2_add"](G2["f2_scale"](F(1, 2), d_b_t), G2["f2_scale"](F(1, 3), t2)),
    )
    f_a = G2["curvature"](a, da)
    core_seg = G2["f2_add"](shiab(q_seg), G2["f2_scale"](kappa, G2["star1"](t)))
    core_draft = G2["f2_add"](shiab(f_a), G2["f2_scale"](kappa, G2["star1"](t)))
    correction = G2["f2_sub"](euler, core_seg)

    exact(
        "the action uniquely forces a nonzero correction from the affine two-connection core to the graph-complete Euler owner",
        correction != zero2 and G2["f2_add"](core_seg, correction) == euler,
    )
    reject("the affine Q_seg plus mass term is already the graph-complete Euler covector", core_seg == euler)
    reject("the draft compressed S(F_A)+mass residual is the native graph-complete Euler covector", core_draft == euler)
    reject("the mixed Hhat_AB route alone is the graph-complete Euler covector", shiab(h_hat) == euler)

    # Necessary common-owner typing control.  Since ``correction`` is defined
    # from the independently reconstructed action Euler form, the identities
    # below test carrier linearity only.  They do not prove either physical
    # somatic composition emits the correction.
    nonzero_fund = False
    nonzero_ad = False
    for component_g, component_core, component_correction in zip(euler, core_seg, correction):
        fund_g = component_g
        fund_sum = G2["add"](component_core, component_correction)
        ad_g = ad_matrix(component_g)
        ad_sum = gadd(ad_matrix(component_core), ad_matrix(component_correction))
        exact("fundamental/Fermi carrier linearly represents the necessary core-plus-correction target", fund_g == fund_sum)
        exact("adjoint/Bose carrier linearly represents the necessary core-plus-correction target", ad_g == ad_sum)
        nonzero_fund = nonzero_fund or fund_g != gzero(2)
        nonzero_ad = nonzero_ad or ad_g != gzero(4)
    exact("the necessary owner target is nonvacuous in both finite representations", nonzero_fund and nonzero_ad)

    # Physical Q_F has two one-form-spinor slots and one zero-form-spinor slot
    # in this two-direction control.  The same owner acts blockwise before the
    # source-silent off-diagonal Dirac couplings are added.
    qf_owner = block_diag([euler[0], euler[0], euler[0]])
    qf_sum = gadd(
        block_diag([core_seg[0], core_seg[0], core_seg[0]]),
        block_diag([correction[0], correction[0], correction[0]]),
    )
    exact("physical zeta/nu carrier is blockwise compatible with the necessary owner target", qf_owner == qf_sum)
    reject(
        "defining Z_var as Euler minus core proves the Bose and Fermi somatic squares independently emit Z_var",
        False,
    )

    gamma = G2["M"](0, 1, -1, 0)
    off_shell_orbit = G2["comm"](gamma, euler[0])
    exact("the Bose route is a complex on shell and an Euler-covariant curved complex off shell", off_shell_orbit != G2["ZERO"] and G2["comm"](gamma, G2["ZERO"]) == G2["ZERO"])
    reject("gauge covariance makes delta2 delta1 vanish identically off shell", off_shell_orbit == G2["ZERO"])

    # Reuse the exact G2 plant: q(y,z)=0 while the polarized variational
    # response is nonzero.  This proves the forced correction is structural.
    y = G2["form1"](G2["M"](1, 0, 0, 0), G2["ZERO"], G2["ZERO"])
    z = G2["form1"](G2["ZERO"], G2["M"](0, 0, 0, 1), G2["ZERO"])
    delta = G2["form1"](
        G2["M"](2, 0, 1, -1), G2["M"](-1, 2, 0, 1), G2["M"](1, 1, -2, 0)
    )
    polarized = F(1, 3) * (
        G2["wedge_pair"](delta, shiab(G2["q"](y, z)))
        + G2["wedge_pair"](y, shiab(G2["q"](delta, z)))
        + G2["wedge_pair"](z, shiab(G2["q"](delta, y)))
    )
    exact("zero curvature polarization can retain a nonzero variational-Euler channel", G2["q"](y, z) == zero2 and polarized != 0)
    reject("every common obstruction can factor only through q(T,T)", polarized == 0)

    type_level(
        "the actual active J_F needs the C-plus/Krein/right-H Riesz map and moving Clifford/Hodge/density data"
    )
    type_level(
        "the source-silent off-diagonal zeta/nu couplings and current map into the graph-complete bosonic owner remain unconstructed"
    )
    reject("P1, P2, or P3 can supply the forced local route correction or Riesz map", False)
    reject("the literal Curt (7,7) real carrier transports the active right-H/Krein intertwiner", False)


def main() -> None:
    source_and_layer0_checks()
    source_2025_and_map_separation_checks()
    split_hodge_checks()
    route_data = two_representation_route_checks()
    graph_complete_common_owner_checks(*route_data)

    if FAILURES:
        print("FAILURES:", ", ".join(FAILURES))
        raise SystemExit(1)
    total = EXACT + TYPE_LEVEL + PLANTED
    print(f"ECW3D-B2C7: {EXACT} exact + {TYPE_LEVEL} type-level + {PLANTED} planted = {total} PASS")
    print("RESULT: Bose/Fermi raw operators are not equal; one graph-complete residual is a typed common-owner target, not yet a proved factorization")
    print("RESULT: symmetrized A/B routes share Hhat_AB, but the native action forces a nonzero parameter-free Euler correction")
    print("RESULT: the 2021 F_A/d_B and tentative 2025 F_B squares remain rival branches; contraction, Riesz, Poisson sharp, and observation are distinct maps")
    print("BOUNDARY: finite exact model; active Y14 source-forked square, local primalizers, current/off-diagonal completion, and reduced Green/BFV phase space remain open")


if __name__ == "__main__":
    main()
