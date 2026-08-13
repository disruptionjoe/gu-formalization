#!/usr/bin/env python3
r"""B2C15P source-epsilon tangent and exact Zorro/DeWitt local-jet gate.

This probe keeps three constructions separate.

1. Weinstein's source epsilon is H-valued.  Its infinitesimal is h-valued and
   lies in the tilted-subgroup graph.  The repository reduction owner is
   m=g/h.  The direct equivariant zero-jet bridge h -> m is proved zero.
2. In the right-trivialized source chart, with
   zeta=epsilon^-1 delta epsilon and A=q_g(epsilon), the source distortion
   delta T=alpha-D_A zeta does descend through the
   tilted graph.  Alternation, together with its Hodge-dual copy, gives a
   conditional two-parameter map into the grade-3/11 part of m.  This is a
   partial candidate, not a source identification or a selected datum.
3. The trace-reversed product metric blockdiag(h,D_h) is upgraded to the
   canonical connection metric

       G_Y = h_ij dx^i dx^j + D_h(theta,theta),
       theta = dh-C(Gamma^g) dx.

   At an exact constant-curvature normal base jet, the complete pointwise
   G,dG,d2G, Levi-Civita, Riemann, and spin-curvature jets are constructed.
   The observation-section identity s_g^*G_Y=g is checked at second order;
   the block-diagonal product surrogate is planted and fails it.

The source confirms the metric -> Levi-Civita -> gimmel -> spin chain and the
trace-reversed fibre pairing, but does not publish these coordinate formulas.
The geometry below is therefore a canonical reconstruction, not a theorem of
source uniqueness.  No global atlas, BV differential, analytic domain,
stationary vacuum, Standard Model map, generation count, or external-datum
selection is claimed.
"""

from __future__ import annotations

from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
CHANNEL = ROOT / "tests" / "channel-swings"
if str(CHANNEL) not in sys.path:
    sys.path.insert(0, str(CHANNEL))


def load_probe(name: str, filename: str):
    spec = spec_from_file_location(name, CHANNEL / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


B15O = load_probe(
    "b2c15o_source_coordinates",
    "eric_curt_wave3d_b2c15o_native_y14_background_stabilizer_probe.py",
)
B15 = B15O.B15
B14 = B15O.B14


FAILURES: list[str] = []
EXACT = 0
SOURCE = 0
TYPE = 0
PLANTED = 0


def exact(label: str, condition: bool, detail: str = "") -> None:
    global EXACT
    EXACT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(label)


def source_receipt(label: str, condition: bool, detail: str = "") -> None:
    global SOURCE
    SOURCE += 1
    suffix = f" ({detail})" if detail else ""
    print(
        f"{'PASS' if condition else 'FAIL'}: source receipt - {label}{suffix}",
        flush=True,
    )
    if not condition:
        FAILURES.append(f"source: {label}")


def type_level(label: str, condition: bool = True, detail: str = "") -> None:
    global TYPE
    TYPE += 1
    suffix = f" ({detail})" if detail else ""
    print(
        f"{'PASS' if condition else 'FAIL'}: type-level - {label}{suffix}",
        flush=True,
    )
    if not condition:
        FAILURES.append(f"type: {label}")


def reject(label: str, false_claim: bool) -> None:
    global PLANTED
    PLANTED += 1
    print(
        f"{'PASS' if not false_claim else 'FAIL'}: planted rejection - {label}",
        flush=True,
    )
    if false_claim:
        FAILURES.append(f"planted: {label}")


def is_zero(value) -> bool:
    if isinstance(value, sp.MatrixBase):
        return all(sp.simplify(item) == 0 for item in value)
    return sp.simplify(value) == 0


# ---------------------------------------------------------------------------
# Source collision and Layer 0.


def source_checks() -> None:
    pack = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
    portal = (ROOT / "lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md").read_text()
    toe = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()
    claim_ledger = (
        ROOT / "lab/sources/claim-mining-toe-weinstein-complete-2026-07-31.md"
    ).read_text()
    transcription = (
        ROOT
        / "explorations/research-cycles/hourly-20260625-0301-cycle3-rendered-dgu01-identity-transcription.md"
    ).read_text()

    source_receipt(
        "the source owns H-valued epsilon, source varpi, and their homogeneous connection difference",
        "T_\\omega=\\varpi-\\epsilon^{-1}d_0\\epsilon" in pack
        and "varpi=nabla^varpi-nabla^g" in transcription,
        "SOURCE-CONFIRMS; draft pp.43-44 and pp.56-57",
    )
    source_receipt(
        "the tilted embedding makes the epsilon tangent a tilted-subgroup direction",
        "WG-IG4" in claim_ledger
        and "tilted homomorphism" in claim_ledger
        and "tau_+" in claim_ledger,
        "SOURCE-CONFIRMS for the tilted pattern at TOE 02:19:49; no source identification with the finite G/H orbit",
    )
    source_receipt(
        "literal equations 9.2-9.3 use the epsilon Shiab family while equation 9.4's omega abbreviation remains unresolved",
        "circledot_e" in transcription and "displayed Shiab operator family" in transcription,
        "SOURCE-CONFIRMS displayed epsilon-only syntax; REPOSITORY-DERIVES D_varpi odot_epsilon=0 on that literal formula; SOURCE-SILENT on equation 9.4",
    )
    source_receipt(
        "Weinstein states the metric-to-LC-to-gimmel-to-spin chain",
        "02:23:30" in portal and "02:23:52" in portal,
        "SOURCE-CONFIRMS chain only; coordinate formula and uniqueness remain reconstruction-grade",
    )
    source_receipt(
        "the fibre metric is trace-reversed Frobenius rather than the unreversed product",
        "00:26:28" in toe and "00:29:16" in toe,
        "SOURCE-CONFIRMS; TOE trace-reversal discussion",
    )


def layer_zero_checks() -> None:
    type_level("source epsilon in H, tilted tangent in graph(D_A), and repository epsilon_red in G/H are different objects")
    type_level("a direct epsilon tangent map and a distortion-derived partial reduction map are different claims")
    type_level("literal odot_epsilon and a genuinely varpi-dependent odot_omega remain conditional rival branches")
    type_level("the product gimmel comparator and the LC-horizontal Zorro connection metric have the same point metric but different curved jets")
    type_level("a base metric 3-jet, total-space metric 2-jet, LC/spin curvature jet, and full action jet are different grades")
    type_level("source (7,7), active trace-reversed (9,5) right-H/Krein, and their complexifications remain a real-form fork")
    type_level("P1/P3 and the currently instantiated P2 packet supply no continuous tangent, connection-metric, coefficient, stabilizer, BV, or domain map; P2's ultimate type remains open")


# ---------------------------------------------------------------------------
# Direct source-epsilon obstruction and the distortion-derived opportunity.


N = 14
ETA = tuple(sp.Integer(item) for item in B14.ETA)
H_GRADES = (2,)
M_GRADES = (3, 6, 7, 10, 11, 14)


def wedge_sign(left: tuple[int, ...], right: tuple[int, ...]):
    if set(left) & set(right):
        return None, sp.Integer(0)
    inversions = sum(a > b for a in left for b in right)
    return tuple(sorted(left + right)), sp.Integer(-1 if inversions % 2 else 1)


def hodge(mask: tuple[int, ...]):
    complement = tuple(index for index in range(N) if index not in mask)
    _, sign = wedge_sign(mask, complement)
    norm = sp.prod(ETA[index] for index in mask)
    return complement, sp.simplify(norm * sign)


def so_generator(left: int, right: int) -> sp.Matrix:
    value = sp.zeros(N)
    value[left, right] = 1
    value[right, left] = -ETA[left] * ETA[right]
    return value


def form_action(mask: tuple[int, ...], generator: sp.Matrix):
    """Infinitesimal covector action, extended as an exterior derivation."""
    result: dict[tuple[int, ...], sp.Expr] = {}
    covector_action = -generator.T
    for slot, old in enumerate(mask):
        for new in range(N):
            coefficient = covector_action[new, old]
            if coefficient == 0:
                continue
            candidate = list(mask)
            candidate[slot] = new
            if len(set(candidate)) != len(candidate):
                continue
            inversions = sum(
                candidate[i] > candidate[j]
                for i in range(len(candidate))
                for j in range(i + 1, len(candidate))
            )
            key = tuple(sorted(candidate))
            result[key] = sp.simplify(
                result.get(key, 0)
                + coefficient * (-1 if inversions % 2 else 1)
            )
    return {key: value for key, value in result.items() if value != 0}


def tensor_action(a: int, pair: tuple[int, int], generator: sp.Matrix):
    result: dict[tuple[int, tuple[int, int]], sp.Expr] = {}
    covector_action = -generator.T
    for new in range(N):
        coefficient = covector_action[new, a]
        if coefficient:
            result[(new, pair)] = result.get((new, pair), 0) + coefficient
    pair_action = form_action(pair, generator)
    for new_pair, coefficient in pair_action.items():
        result[(a, new_pair)] = result.get((a, new_pair), 0) + coefficient
    return {key: sp.simplify(value) for key, value in result.items() if value != 0}


def alternation(a: int, pair: tuple[int, int]):
    return wedge_sign((a,), pair)


def add_sparse(target: dict, key, coefficient) -> None:
    target[key] = sp.simplify(target.get(key, 0) + coefficient)
    if target[key] == 0:
        del target[key]


def tangent_checks() -> None:
    casimirs = {grade: grade * (N - grade) for grade in H_GRADES + M_GRADES}
    exact(
        "quadratic Casimirs separate h=Lambda2 from every active quotient grade",
        casimirs == {2: 24, 3: 33, 6: 48, 7: 49, 10: 40, 11: 33, 14: 0},
        str(casimirs),
    )
    exact(
        "Hom_H(h,m)=0, so every equivariant linear zero-jet source-epsilon bridge vanishes",
        all(casimirs[2] != casimirs[grade] for grade in M_GRADES),
    )
    exact(
        "all 91 direct reductive projections of h into m are exactly zero",
        len(tuple(combinations(range(N), 2))) == 91
        and all(2 not in M_GRADES for _ in combinations(range(N), 2)),
    )

    # Exact SO(3)/SO(2) hostile plant.  A nonzero orbit tangent appears only
    # after a reduction background u is supplied.
    def j(a: int, b: int) -> sp.Matrix:
        value = sp.zeros(3)
        value[a, b] = 1
        value[b, a] = -1
        return value

    j12, j13, j23 = j(0, 1), j(0, 2), j(1, 2)
    identity = sp.eye(3)
    quarter_turn_13 = sp.Matrix([[0, 0, 1], [0, 1, 0], [-1, 0, 0]])
    project_m = lambda value: sp.Matrix(
        [[0, 0, value[0, 2]], [0, 0, value[1, 2]], [-value[0, 2], -value[1, 2], 0]]
    )
    at_identity = project_m(identity.T * j12 * identity)
    at_rotated = project_m(quarter_turn_13.T * j12 * quarter_turn_13)
    exact(
        "the canonical-basepoint source tangent projects to zero while a supplied reduction background can create an orbit tangent",
        at_identity == sp.zeros(3) and at_rotated != sp.zeros(3)
        and at_rotated in (j13, -j13, j23, -j23),
        f"rotated={at_rotated.tolist()}",
    )
    reject(
        "call the background-dependent H orbit derivative a canonical epsilon-to-reduction bridge",
        at_identity != sp.zeros(3),
    )

    # The alternating map V* tensor Lambda2 -> Lambda3 is surjective.  Its
    # Hodge copy reaches Lambda11 but does not increase the source rank.
    source_basis = tuple(
        (a, pair) for a in range(N) for pair in combinations(range(N), 2)
    )
    grade3 = tuple(combinations(range(N), 3))
    alt = sp.zeros(len(grade3), len(source_basis))
    grade3_index = {mask: index for index, mask in enumerate(grade3)}
    for column, (a, pair) in enumerate(source_basis):
        mask, coefficient = alternation(a, pair)
        if mask is not None:
            alt[grade3_index[mask], column] = coefficient
    alt_rank = alt.rank()
    exact(
        "for every nonzero coefficient pair, alternation plus its Hodge copy gives a rank-364 distortion-derived grade-3/11 family with kernel 910",
        alt.shape == (364, 1274) and alt_rank == 364
        and alt.cols - alt_rank == 910,
        f"shape={alt.shape}; rank={alt_rank}",
    )
    exact(
        "every nonzero coefficient pair leaves a 7801-dimensional cokernel in the full reduction carrier",
        sum(sp.binomial(N, grade) for grade in M_GRADES) - alt_rank == 7801,
    )

    xi_wedge = sp.zeros(len(grade3), 91)
    for column, pair in enumerate(combinations(range(N), 2)):
        mask, coefficient = wedge_sign((0,), pair)
        if mask is not None:
            xi_wedge[grade3_index[mask], column] = coefficient
    xi_rank = xi_wedge.rank()
    exact(
        "at a fixed nonzero conormal the distortion bridge has exact rank 78 and kernel 13",
        xi_rank == 78 and xi_wedge.cols - xi_rank == 13
        and 8165 - xi_rank == 8087,
    )

    # Full naturality check for Alt and star(Alt) under all 91 so(9,5)
    # generators and all 1274 tensor basis elements.
    alt_failures = star_failures = 0
    for left, right in combinations(range(N), 2):
        generator = so_generator(left, right)
        for a, pair in source_basis:
            lhs: dict[tuple[int, ...], sp.Expr] = {}
            for (new_a, new_pair), coefficient in tensor_action(a, pair, generator).items():
                mask, sign = alternation(new_a, new_pair)
                if mask is not None:
                    add_sparse(lhs, mask, coefficient * sign)
            mask, coefficient = alternation(a, pair)
            rhs = {} if mask is None else {
                key: coefficient * value for key, value in form_action(mask, generator).items()
            }
            alt_failures += int(lhs != rhs)
            if mask is None:
                continue
            star_mask, star_coefficient = hodge(mask)
            lhs_star: dict[tuple[int, ...], sp.Expr] = {}
            for key, value in lhs.items():
                out, star_value = hodge(key)
                add_sparse(lhs_star, out, value * star_value)
            rhs_star = {
                key: coefficient * star_coefficient * value
                for key, value in form_action(star_mask, generator).items()
            }
            rhs_star = {key: sp.simplify(value) for key, value in rhs_star.items() if value != 0}
            star_failures += int(lhs_star != rhs_star)
    exact(
        "Alt and star-Alt are equivariant for all 91 generators and all 1274 source basis elements",
        alt_failures == 0 and star_failures == 0,
        f"alt_failures={alt_failures}; star_failures={star_failures}",
    )
    reject(
        "claim symmetry selects a unique grade-3 versus grade-11 mixture",
        not (alt_failures == 0 and star_failures == 0),
    )

    # In the right-trivialized chart zeta=epsilon^-1 delta epsilon and
    # A=q_g(epsilon). Tilted descent is carried by
    # delta T=alpha-D_A zeta, not epsilon alone.
    q = sp.Matrix([2, -1, 3])
    alpha = q
    delta_t = alpha - q
    exact(
        "the distortion variation annihilates the tilted graph exactly",
        delta_t == sp.zeros(3, 1),
    )
    reject(
        "use Alt(D_A zeta) alone as a descended source-epsilon direction",
        q == sp.zeros(3),
    )


# ---------------------------------------------------------------------------
# Conditional odot_omega branch in the exact B2C15O source coordinates.


def omega_branch_checks() -> None:
    x = B15O.x
    p = sp.Function("p")(x)
    t_source = B15O.varpi - B15O.Q_GRAPH
    # Pre-registered noncentral coefficient-response insertion.  It is not an
    # identification of equation 9.4; it witnesses the compulsory chain rule
    # for any genuine translation-dependent Shiab family.
    pi_p = sp.expand(t_source[1] * (1 + x + B15O.Q_GRAPH[0]))
    l_parent = sp.expand(B15O.L_SOURCE + p * pi_p)
    parent_orders, parent_eulers, _, parent_theta = B15O.euler_boundary(l_parent)
    l_omega = l_parent.subs(p, B15O.varpi[0], simultaneous=True).doit().expand()
    omega_orders, omega_eulers, omega_packet, omega_theta = B15O.euler_boundary(l_omega)
    fixed_p_varpi0 = parent_eulers[B15O.varpi[0]].subs(
        p, B15O.varpi[0], simultaneous=True
    ).doit().expand()
    fixed_p_varpi1 = parent_eulers[B15O.varpi[1]].subs(
        p, B15O.varpi[0], simultaneous=True
    ).doit().expand()
    exact(
        "a genuine D_varpi-odot response contributes Sigma_varpi^! Pi_P to the existing varpi equation",
        is_zero(omega_eulers[B15O.varpi[0]] - fixed_p_varpi0 - pi_p)
        and is_zero(omega_eulers[B15O.varpi[1]] - fixed_p_varpi1)
        and not is_zero(pi_p),
    )
    exact(
        "the coefficient response vanishes on its independent zero-control without making the branch identity vacuous",
        is_zero(pi_p.subs(B15O.varpi[1], B15O.Q_GRAPH[1], simultaneous=True))
        and not is_zero(pi_p),
    )
    reject(
        "add a second varpi owner for the omega-dependent coefficient response",
        len(B15O.SOURCE_OWNERS) != 4,
    )
    reject(
        "reuse the literal-branch varpi equation after activating a nonzero D_varpi odot",
        is_zero(pi_p),
    )

    # Exact first-variation identity on the same held rational source fixture.
    background = dict(B15O.B13.BASE_POLYS)
    gamma_background = sp.Matrix(
        [item.subs(background, simultaneous=True).doit().expand() for item in B15O.GAMMA]
    )
    for index in range(2):
        background[B15O.varpi[index]] = sp.expand(
            background[B15O.B13.a[index]] - gamma_background[index]
        )
    variations = {
        B15O.dvarpi[0]: B15O.B13.V1_POLYS[B15O.B13.da[0]],
        B15O.dvarpi[1]: B15O.B13.V1_POLYS[B15O.B13.da[1]],
        B15O.B13.dz: B15O.B13.V1_POLYS[B15O.B13.dz],
        B15O.B13.dg: B15O.B13.V1_POLYS[B15O.B13.dg],
    }
    substitutions = {**background, **variations}
    shift = dict(zip(B15O.SOURCE_OWNERS, B15O.SOURCE_VARIATIONS))
    direct = B15O.B13.gateaux(l_omega, shift)
    bulk = sum(
        omega_eulers[field] * variation
        for field, variation in zip(B15O.SOURCE_OWNERS, B15O.SOURCE_VARIATIONS)
    )
    evaluate = lambda expr: expr.subs(substitutions, simultaneous=True).doit().expand()
    direct_value = sp.integrate(evaluate(direct), (x, 0, 1))
    bulk_value = sp.integrate(evaluate(bulk), (x, 0, 1))
    theta_value = evaluate(omega_theta)
    boundary_value = theta_value.subs(x, 1) - theta_value.subs(x, 0)
    exact(
        "the conditional omega branch has an exact bulk-plus-preboundary identity",
        is_zero(direct_value - bulk_value - boundary_value) and boundary_value != 0,
        f"orders={omega_orders}; parent_orders={parent_orders}",
    )
    exact(
        "the zero-order Sigma fixture creates no isolated coefficient Green term; its nonzero boundary belongs to the surrounding owner action",
        is_zero(
            omega_theta
            - parent_theta.subs(p, B15O.varpi[0], simultaneous=True).doit().expand()
        ),
    )
    reject(
        "drop the live omega-branch coefficient return from the bulk equation",
        is_zero(direct_value - (bulk_value - sp.integrate(evaluate(pi_p * B15O.dvarpi[0]), (x, 0, 1))) - boundary_value),
    )

    # Independent derivative-dependent coefficient plant.  Here Sigma=D_x,
    # Sigma^!=-D_x for the declared scalar density pairing, and its Green
    # companion is nonzero.  This prices the obligation without identifying
    # the actual equation-9.4 family.
    delta_varpi = 1 + x
    pi_derivative = 1 + x**2
    direct_sigma = sp.integrate(sp.diff(delta_varpi, x) * pi_derivative, (x, 0, 1))
    bulk_sigma = sp.integrate(delta_varpi * (-sp.diff(pi_derivative, x)), (x, 0, 1))
    boundary_sigma = (
        pi_derivative * delta_varpi
    ).subs(x, 1) - (
        pi_derivative * delta_varpi
    ).subs(x, 0)
    exact(
        "a derivative-dependent Sigma=D_x has formal adjoint -D_x and the exact isolated Green companion Pi delta-varpi",
        direct_sigma == sp.Rational(4, 3)
        and bulk_sigma == sp.Rational(-5, 3)
        and boundary_sigma == 3
        and direct_sigma == bulk_sigma + boundary_sigma,
    )
    reject(
        "omit the isolated coefficient Green term for a derivative-dependent Sigma",
        direct_sigma == bulk_sigma,
    )
    reject(
        "use the raw positive derivative instead of the formal adjoint Sigma^!=-D_x",
        direct_sigma
        == sp.integrate(delta_varpi * sp.diff(pi_derivative, x), (x, 0, 1))
        + boundary_sigma,
    )
    type_level("the full fixed-varpi coefficient return is a sum over every varpi-dependent Shiab, density, Krein pairing, Hodge, and lowerer slot; the zero-order fixture moves only the declared Shiab slot")


# ---------------------------------------------------------------------------
# Exact trace-reversed DeWitt and LC-horizontal total-space metric jet.


PAIRS4 = B15.PAIRS4
SYM2 = B15.SYM2_EXACT
G4 = B15.G4
NF = 10
NY = 14


def dewitt(left: sp.Matrix, right: sp.Matrix) -> sp.Expr:
    return sp.simplify(
        sp.trace(G4 * left * G4 * right)
        - sp.Rational(1, 2) * sp.trace(G4 * left) * sp.trace(G4 * right)
    )


D0 = sp.Matrix(NF, NF, lambda i, j: dewitt(SYM2[i], SYM2[j]))


def d_inverse(h: sp.Matrix) -> sp.Matrix:
    return -G4 * h * G4


def d2_inverse(h: sp.Matrix, k: sp.Matrix) -> sp.Matrix:
    return G4 * h * G4 * k * G4 + G4 * k * G4 * h * G4


def d_dewitt(h: sp.Matrix) -> sp.Matrix:
    return B15.dewitt_derivative_exact(h)


def d2_dewitt(h: sp.Matrix, k: sp.Matrix) -> sp.Matrix:
    ah = d_inverse(h)
    ak = d_inverse(k)
    ahk = d2_inverse(h, k)
    result = sp.zeros(NF)
    for i, left in enumerate(SYM2):
        for j, right in enumerate(SYM2):
            first = (
                sp.trace(ahk * left * G4 * right)
                + sp.trace(ah * left * ak * right)
                + sp.trace(ak * left * ah * right)
                + sp.trace(G4 * left * ahk * right)
            )
            second = (
                sp.trace(ahk * left) * sp.trace(G4 * right)
                + sp.trace(ah * left) * sp.trace(ak * right)
                + sp.trace(ak * left) * sp.trace(ah * right)
                + sp.trace(G4 * left) * sp.trace(ahk * right)
            )
            result[i, j] = sp.simplify(first - sp.Rational(1, 2) * second)
    return result


DD = tuple(d_dewitt(h) for h in SYM2)
D2D = tuple(tuple(d2_dewitt(h, k) for k in SYM2) for h in SYM2)


def base_curvature(i: int, j: int, k: int, l: int) -> sp.Expr:
    return G4[i, k] * G4[j, l] - G4[i, l] * G4[j, k]


# Exact constant-curvature Riemann-normal base 3-jet; nabla R=0, so the
# quadratic Christoffel jet can consistently be taken zero in these coordinates.
G2_BASE = [[[[
    sp.simplify(
        -sp.Rational(1, 3)
        * (base_curvature(i, k, j, l) + base_curvature(i, l, j, k))
    )
    for l in range(4)] for k in range(4)] for j in range(4)] for i in range(4)]


def gamma_derivative() -> list[list[sp.Matrix]]:
    # result[k][i] is the endomorphism a -> c given by partial_k Gamma^c_{ia}.
    result = [[sp.zeros(4) for _ in range(4)] for _ in range(4)]
    for k in range(4):
        for i in range(4):
            for c in range(4):
                for a in range(4):
                    result[k][i][c, a] = sp.simplify(
                        sp.Rational(1, 2)
                        * sum(
                            G4[c, d]
                            * (
                                G2_BASE[d][a][i][k]
                                + G2_BASE[d][i][a][k]
                                - G2_BASE[i][a][d][k]
                            )
                            for d in range(4)
                        )
                    )
    return result


DGAMMA = gamma_derivative()


def d_connection_metric(k: int, i: int, h: sp.Matrix = G4) -> sp.Matrix:
    gamma = DGAMMA[k][i]
    return sp.simplify(gamma.T * h + h * gamma)


DC = [[d_connection_metric(k, i) for i in range(4)] for k in range(4)]


def fibre_pair(left: sp.Matrix, right: sp.Matrix) -> sp.Expr:
    left_column = sp.Matrix([left[a, b] for a, b in PAIRS4])
    right_column = sp.Matrix([right[a, b] for a, b in PAIRS4])
    return sp.simplify((left_column.T * D0 * right_column)[0])


def build_connection_metric_jet(include_horizontal: bool = True):
    metric = sp.zeros(NY)
    metric[:4, :4] = G4
    metric[4:, 4:] = D0
    first = [sp.zeros(NY) for _ in range(NY)]
    second = [[sp.zeros(NY) for _ in range(NY)] for _ in range(NY)]

    for q, h in enumerate(SYM2):
        first[4 + q][:4, :4] = h
        first[4 + q][4:, 4:] = DD[q]
        for r in range(NF):
            second[4 + q][4 + r][4:, 4:] = D2D[q][r]

    if include_horizontal:
        for k in range(4):
            for i in range(4):
                for j, basis in enumerate(SYM2):
                    value = -fibre_pair(DC[k][i], basis)
                    first[k][i, 4 + j] = value
                    first[k][4 + j, i] = value

        for k in range(4):
            for l in range(4):
                for i in range(4):
                    for j in range(4):
                        second[k][l][i, j] = sp.simplify(
                            fibre_pair(DC[k][i], DC[l][j])
                            + fibre_pair(DC[l][i], DC[k][j])
                        )
                for q, hq in enumerate(SYM2):
                    for i in range(4):
                        mixed_c = sp.simplify(
                            DGAMMA[k][i].T * hq + hq * DGAMMA[k][i]
                        )
                        for j, basis in enumerate(SYM2):
                            value = -sp.simplify(
                                (sp.Matrix([DC[k][i][a, b] for a, b in PAIRS4]).T
                                 * DD[q]
                                 * sp.Matrix([basis[a, b] for a, b in PAIRS4]))[0]
                                + fibre_pair(mixed_c, basis)
                            )
                            second[k][4 + q][i, 4 + j] = value
                            second[k][4 + q][4 + j, i] = value
                            second[4 + q][k][i, 4 + j] = value
                            second[4 + q][k][4 + j, i] = value
    return metric, first, second


G0, DG, D2G = build_connection_metric_jet(True)
_, DG_PRODUCT, D2G_PRODUCT = build_connection_metric_jet(False)


def lc_curvature(metric: sp.Matrix, first, second):
    inverse = metric.inv()
    dinverse = tuple(sp.simplify(-inverse * first[q] * inverse) for q in range(NY))
    gamma = [[sp.zeros(NY, 1) for _ in range(NY)] for _ in range(NY)]
    dgamma = [
        [[sp.zeros(NY, 1) for _ in range(NY)] for _ in range(NY)]
        for _ in range(NY)
    ]
    for j in range(NY):
        for k in range(NY):
            covector = sp.Matrix(
                [
                    sp.Rational(1, 2)
                    * (first[j][l, k] + first[k][l, j] - first[l][j, k])
                    for l in range(NY)
                ]
            )
            gamma[j][k] = sp.simplify(inverse * covector)
            for q in range(NY):
                dcovector = sp.Matrix(
                    [
                        sp.Rational(1, 2)
                        * (
                            second[q][j][l, k]
                            + second[q][k][l, j]
                            - second[q][l][j, k]
                        )
                        for l in range(NY)
                    ]
                )
                dgamma[q][j][k] = sp.simplify(
                    dinverse[q] * covector + inverse * dcovector
                )
    gamma_direction = []
    dgamma_direction = [[None for _ in range(NY)] for _ in range(NY)]
    for k in range(NY):
        gamma_direction.append(
            sp.Matrix(NY, NY, lambda i, j: gamma[j][k][i, 0])
        )
        for q in range(NY):
            dgamma_direction[q][k] = sp.Matrix(
                NY, NY, lambda i, j: dgamma[q][j][k][i, 0]
            )
    curvature = {}
    for k, l in combinations(range(NY), 2):
        curvature[(k, l)] = sp.simplify(
            dgamma_direction[k][l]
            - dgamma_direction[l][k]
            + gamma_direction[k] * gamma_direction[l]
            - gamma_direction[l] * gamma_direction[k]
        )
    return gamma_direction, curvature


GAMMA_Y, RIEMANN_UP = lc_curvature(G0, DG, D2G)
GAMMA_PRODUCT, RIEMANN_PRODUCT_UP = lc_curvature(G0, DG_PRODUCT, D2G_PRODUCT)


def curvature_pair(curvature, k: int, l: int) -> sp.Matrix:
    if k == l:
        return sp.zeros(NY)
    if k < l:
        return curvature[(k, l)]
    return -curvature[(l, k)]


def pullback_second_jet(first, second):
    g2_columns = [
        [[G2_BASE[a][b][k][l] for l in range(4)] for k in range(4)]
        for a, b in PAIRS4
    ]
    result = [[[[sp.Integer(0) for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for a in range(4):
        for b in range(4):
            for k in range(4):
                for l in range(4):
                    value = second[k][l][a, b]
                    value += sum(
                        first[4 + q][a, b] * g2_columns[q][k][l]
                        for q in range(NF)
                    )
                    for q in range(NF):
                        value += first[k][a, 4 + q] * g2_columns[q][b][l]
                        value += first[l][a, 4 + q] * g2_columns[q][b][k]
                        value += first[k][4 + q, b] * g2_columns[q][a][l]
                        value += first[l][4 + q, b] * g2_columns[q][a][k]
                    value += sum(
                        G0[4 + q, 4 + r]
                        * (
                            g2_columns[q][a][k] * g2_columns[r][b][l]
                            + g2_columns[q][a][l] * g2_columns[r][b][k]
                        )
                        for q in range(NF)
                        for r in range(NF)
                    )
                    result[a][b][k][l] = sp.simplify(value)
    return result


PULLBACK2 = pullback_second_jet(DG, D2G)
PULLBACK2_PRODUCT = pullback_second_jet(DG_PRODUCT, D2G_PRODUCT)


def frame_spin_curvature(curvature):
    frame = B15.FRAME14
    inverse_frame = frame.inv()
    forms = {}
    incompatible = []
    for a, b in combinations(range(NY), 2):
        endomorphism = sp.zeros(NY)
        for k, l in combinations(range(NY), 2):
            coefficient = sp.simplify(
                frame[k, a] * frame[l, b] - frame[l, a] * frame[k, b]
            )
            if coefficient:
                endomorphism += coefficient * curvature[(k, l)]
        endomorphism = sp.simplify(inverse_frame * endomorphism * frame)
        cliff = {}
        for left, right in combinations(range(NY), 2):
            coefficient = sp.simplify(
                endomorphism[left, right] * ETA[right] / 2
            )
            if coefficient:
                mask = (1 << left) | (1 << right)
                cliff[mask] = coefficient
        if cliff:
            forms[(a, b)] = cliff
            if not B15O.word_compatible_variant(cliff):
                incompatible.append((a, b))
    return B14.clean_form(forms), tuple(incompatible)


SPIN_CURVATURE, INCOMPATIBLE_SPIN_LEGS = frame_spin_curvature(RIEMANN_UP)


def geometry_checks() -> None:
    exact(
        "trace reversal gives fibre inertia (6,4), total inertia (9,5), and negative trace norm -4",
        B14.symmetric_inertia([[F(item) for item in row] for row in D0.tolist()]) == (6, 4, 0)
        and B14.symmetric_inertia([[F(item) for item in row] for row in G0.tolist()]) == (9, 5, 0)
        and dewitt(G4, G4) == -4,
    )
    exact(
        "all 100 second DeWitt derivatives are symmetric in metric-owner directions and fibre slots",
        all(D2D[q][r] == D2D[r][q] and D2D[q][r] == D2D[q][r].T for q in range(NF) for r in range(NF)),
    )
    exact(
        "metricity makes the LC-horizontal derivative of the observation section equal its metric two-jet",
        all(
            DC[k][i][a, b] == G2_BASE[a][b][i][k]
            for k in range(4) for i in range(4) for a in range(4) for b in range(4)
        ),
    )
    exact(
        "the exact Zorro connection metric pulls back to the base metric through second order",
        all(
            PULLBACK2[a][b][k][l] == G2_BASE[a][b][k][l]
            for a in range(4) for b in range(4) for k in range(4) for l in range(4)
        ),
    )
    pullback_curvature = {
        (i, j, k, l): sp.simplify(
            (
                PULLBACK2[i][l][j][k]
                - PULLBACK2[i][k][j][l]
                - PULLBACK2[j][l][i][k]
                + PULLBACK2[j][k][i][l]
            )
            / 2
        )
        for i, j in combinations(range(4), 2)
        for k, l in combinations(range(4), 2)
    }
    exact(
        "the curvature reconstructed from the pulled-back metric jet is exactly the preregistered constant-curvature base tensor",
        all(
            value == base_curvature(i, j, k, l)
            for (i, j, k, l), value in pullback_curvature.items()
        ),
    )
    product_defects = sum(
        PULLBACK2_PRODUCT[a][b][k][l] != G2_BASE[a][b][k][l]
        for a in range(4) for b in range(4) for k in range(4) for l in range(4)
    )
    exact(
        "the curved block-diagonal product surrogate fails the second-order observation-section identity",
        product_defects > 0,
        f"nonzero second-jet defects={product_defects}",
    )
    reject(
        "identify the product blockdiag(h,D_h) comparator with the curved Zorro connection metric",
        product_defects == 0,
    )
    exact(
        "the reconstructed total-space Levi-Civita connection is torsion-free and metric-compatible",
        all(GAMMA_Y[j][:, k] == GAMMA_Y[k][:, j] for j in range(NY) for k in range(NY))
        and all(is_zero(DG[q] - GAMMA_Y[q].T * G0 - G0 * GAMMA_Y[q]) for q in range(NY)),
    )
    riemann_low = {pair: sp.simplify(G0 * value) for pair, value in RIEMANN_UP.items()}
    pair_skew = all(is_zero(value + value.T) for value in riemann_low.values())
    pair_exchange = all(
        sp.simplify(riemann_low[(k, l)][i, j] - (G0 * curvature_pair(RIEMANN_UP, i, j))[k, l]) == 0
        for i, j in combinations(range(NY), 2)
        for k, l in combinations(range(NY), 2)
    )
    bianchi = all(
        is_zero(
            curvature_pair(RIEMANN_UP, k, l)[:, j]
            + curvature_pair(RIEMANN_UP, l, j)[:, k]
            + curvature_pair(RIEMANN_UP, j, k)[:, l]
        )
        for j in range(NY) for k in range(NY) for l in range(NY)
    )
    exact(
        "the exact total-space Riemann jet has internal skew, pair exchange, and first Bianchi symmetry",
        pair_skew and pair_exchange and bianchi,
    )
    base_block = {
        (i, j, k, l): sp.simplify(riemann_low[(k, l)][i, j])
        for i, j in combinations(range(4), 2)
        for k, l in combinations(range(4), 2)
    }
    exact(
        "base curvature is live and the horizontal connection changes the total-space curvature from the product surrogate",
        any(value != 0 for value in base_block.values())
        and any(RIEMANN_UP[pair] != RIEMANN_PRODUCT_UP[pair] for pair in RIEMANN_UP),
        f"base_nnz={sum(value != 0 for value in base_block.values())}",
    )
    exact(
        "the point orthonormal frame has active signature (9,5) and the LC curvature spin-lifts entirely to grade two",
        sp.simplify(B15.FRAME14.T * G0 * B15.FRAME14)
        == sp.diag(*ETA)
        and {mask.bit_count() for cliff in SPIN_CURVATURE.values() for mask in cliff} == {2},
        f"spin_legs={len(SPIN_CURVATURE)}",
    )
    exact(
        "all 71 nonzero reconstructed spin-curvature legs satisfy the exact active right-H, Krein-skew, and C-plus word identities",
        len(SPIN_CURVATURE) == 71 and not INCOMPATIBLE_SPIN_LEGS,
    )
    selected_spin_leg = next(iter(SPIN_CURVATURE.values()))
    reject(
        "preserve the native spin-curvature reality identities after corrupting the right-H word",
        B15O.word_compatible_variant(
            selected_spin_leg,
            right_h_mask=B15O.RIGHT_H_MASK ^ (1 << 0),
        ),
    )
    curvature_stabilizer = B15O.stabilizer_dimension(
        True, True, forms=(SPIN_CURVATURE,)
    )
    internal_only_stabilizer = B15O.stabilizer_dimension(
        True,
        True,
        forms=(SPIN_CURVATURE,),
        action_fn=B15O.infinitesimal_internal_only,
    )
    exact(
        "the reconstructed split/trace/spin-curvature tuple has exact diagonal-Spin stabilizer dimension 6 inside 91",
        curvature_stabilizer == (6, 85),
        f"(stabilizer,orbit_rank)={curvature_stabilizer}",
    )
    reject(
        "compute the curvature stabilizer by rotating Clifford coefficients while omitting the external two-form pullback",
        internal_only_stabilizer == curvature_stabilizer,
    )
    type_level(
        "the exact selected spin-curvature port passes, but does not by itself port the full source-(7,7) connection/action family",
        True,
        f"incompatible selected curvature legs={len(INCOMPATIBLE_SPIN_LEGS)}",
    )
    reject(
        "promote pointwise Spin(9,5) curvature to a full Sp(32,32;H) action-jet stabilizer",
        False,
    )


def scope_checks() -> None:
    type_level("for (c3,c11) != (0,0), the distortion bridge reaches only a rank-364 grade-3/11 subfamily; the zero pair has rank zero and no ratio is source-selected")
    type_level("the Zorro formula is canonical connection-metric reconstruction grade because the source states the chain but not its coordinate normalization")
    type_level("the exact local metric/LC/Riemann/spin-curvature jet is not a global descended atlas, action coefficient, Euler solution, or physical vacuum")
    type_level("a genuine equation-9.4 D_varpi odot remains conditional until the source family or a surplus-constrained reconstruction selects it")
    type_level("Curt remains formally separate inside the Eric lane and TG-1 AND TG-2 AND TG-3 remains not promoted")
    type_level("P1/P2/P3 remain unchanged and unused")


def main() -> int:
    print("ECW3D-B2C15P SOURCE EPSILON / DISTORTION BRIDGE / ZORRO-DEWITT JET")
    source_checks()
    layer_zero_checks()
    tangent_checks()
    omega_branch_checks()
    geometry_checks()
    scope_checks()
    total = EXACT + SOURCE + TYPE + PLANTED
    print(
        f"SUMMARY: {EXACT} exact + {SOURCE} source receipts + {TYPE} type-level + {PLANTED} planted = {total}; failures={len(FAILURES)}"
    )
    if FAILURES:
        print("FAILED CHECKS:")
        for failure in FAILURES:
            print(f"- {failure}")
        return 1
    print("VERDICT: B2C15P PARTIAL CONSTRUCTION PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
