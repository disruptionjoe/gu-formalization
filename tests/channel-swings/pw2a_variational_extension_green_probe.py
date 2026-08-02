#!/usr/bin/env python3
"""PW2A exact independent-B variational and two-layer Green comparator.

This is deliberately a structural comparator.  It verifies the complete
chain-rule adjoint and higher-derivative Green identity for a split
``(B,T)->(B+K,T-K)`` with ``K=K(B,j1T)``.  It does not identify the scalar
fixture with the literal Y^14 action or prove gauge naturality of native K.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
RESULT = ROOT / "lab/process/pw2a-source-legal-moving-reduction-lift.json"
REGISTRY = ROOT / "lab/process/pw2a-action-extension-experiment-registry.json"


class DuplicateKeyError(ValueError):
    pass


def unique_object(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise DuplicateKeyError(key)
        out[key] = value
    return out


def load(path: Path):
    return json.loads(path.read_text(), object_pairs_hook=unique_object)


EXACT = 0
TYPE = 0
PLANTED = 0


def exact(name: str, condition: bool) -> None:
    global EXACT
    if not condition:
        raise AssertionError(f"exact check failed: {name}")
    EXACT += 1


def type_level(name: str, condition: bool) -> None:
    global TYPE
    if not condition:
        raise AssertionError(f"type/registry check failed: {name}")
    TYPE += 1


def planted(name: str, false_claim: bool) -> None:
    global PLANTED
    if false_claim:
        raise AssertionError(f"planted false claim unexpectedly passed: {name}")
    PLANTED += 1


def main() -> None:
    result = load(RESULT)
    registry = load(REGISTRY)
    type_level("result status", result["status"] == "PW2A_ABSTRACT_LOCAL_COMOVING_GAUGE_LIFT_PASS")
    type_level("registry status", registry["status"] == "PW2A_STRUCTURAL_VARIATIONAL_EXTENSION_CERTIFICATE")
    type_level("Euler scope structural", registry["scope"]["literal_native_action"] == "NOT_EVALUATED")
    type_level("root extension Ward not evaluated", registry["ward_certificate"]["root_extension_status"] == "NOT_EVALUATED")
    type_level("two Green layers required", registry["green_certificate"]["layers"] == 2)
    type_level("independent B charged", registry["field_debit"]["independent_B"] == "CONNECTION_SIZED_FUNCTIONAL_FIELD")
    type_level("datum not charged", registry["field_debit"]["P1_P2_P3"] == "UNCHANGED_AND_UNUSED")

    # Root first-order action in independent hat variables.  The rational
    # coefficients echo the source transgression grammar without claiming
    # that this scalar polynomial is the native Shiab action.
    hb0, hb1, hb2 = sp.symbols("hb0 hb1 hb2")
    ht0, ht1, ht2 = sp.symbols("ht0 ht1 ht2")
    root_lagrangian = (
        ht0 * (hb1 + sp.Rational(1, 2) * ht1 + sp.Rational(1, 3) * ht0**2)
        + sp.Rational(1, 2) * ht0**2
        + hb0 * ht0
        + sp.Rational(1, 2) * hb1**2
    )

    def d_hat(expr):
        return sp.expand(
            sp.diff(expr, hb0) * hb1
            + sp.diff(expr, hb1) * hb2
            + sp.diff(expr, ht0) * ht1
            + sp.diff(expr, ht1) * ht2
        )

    e_hb = sp.expand(sp.diff(root_lagrangian, hb0) - d_hat(sp.diff(root_lagrangian, hb1)))
    e_ht = sp.expand(sp.diff(root_lagrangian, ht0) - d_hat(sp.diff(root_lagrangian, ht1)))
    exact("root B Euler is live", e_hb != 0)
    exact("root T Euler is live", e_ht != 0)
    exact("root split response is live", sp.expand(e_hb - e_ht) != 0)

    # Pull back along K=z0*T+z1*D T.  The action becomes a second-order
    # density in T and therefore has an order-four Euler expression.
    t = sp.symbols("t0:5")
    b = sp.symbols("b0:4")
    eta = sp.symbols("eta0:3")
    beta = sp.symbols("beta0:2")
    zb, z0, z1 = sp.Integer(3), sp.Integer(2), sp.Integer(-1)

    def total(expr):
        out = 0
        for sequence in (t, b, eta, beta):
            for left, right in zip(sequence[:-1], sequence[1:]):
                out += sp.diff(expr, left) * right
        return sp.expand(out)

    k0 = zb * b[0] + z0 * t[0] + z1 * t[1]
    k1 = zb * b[1] + z0 * t[1] + z1 * t[2]
    k2 = zb * b[2] + z0 * t[2] + z1 * t[3]
    substitutions = {
        hb0: b[0] + k0,
        hb1: b[1] + k1,
        hb2: b[2] + k2,
        ht0: t[0] - k0,
        ht1: t[1] - k1,
        ht2: t[2] - k2,
    }
    pulled = sp.expand(root_lagrangian.subs(substitutions))
    exact("pulled action owns second T jet", sp.diff(pulled, t[2]) != 0)
    exact("pulled action owns first B jet", sp.diff(pulled, b[1]) != 0)

    e_t = sp.expand(
        sp.diff(pulled, t[0])
        - total(sp.diff(pulled, t[1]))
        + total(total(sp.diff(pulled, t[2])))
    )
    e_b = sp.expand(sp.diff(pulled, b[0]) - total(sp.diff(pulled, b[1])))
    exact("T Euler reaches fourth jet", sp.diff(e_t, t[4]) != 0)
    exact("B Euler reaches second jet", sp.diff(e_b, b[2]) != 0)

    # Chain-rule/formal-adjoint certificate.  R_K=E_hatB-E_hatT and
    # (D_B K)^!R=zb R and (D_T K)^!R=z0 R-D(z1 R).
    e_hb_sub = sp.expand(e_hb.subs(substitutions))
    e_ht_sub = sp.expand(e_ht.subs(substitutions))
    r_k = sp.expand(e_hb_sub - e_ht_sub)
    predicted_t = sp.expand(e_ht_sub + z0 * r_k - total(z1 * r_k))
    predicted_b = sp.expand(e_hb_sub + zb * r_k)
    exact("pulled B Euler includes live K adjoint", sp.expand(e_b - predicted_b) == 0)
    exact("B-dependent K return is live", zb * r_k != 0)
    exact("pulled T Euler equals adjoint chain", sp.expand(e_t - predicted_t) == 0)
    exact("adjoint derivative term is live", total(z1 * r_k) != 0)
    planted("jet partial is the Euler covector", sp.diff(pulled, t[0]) == e_t)
    planted("drop formal-adjoint derivative", sp.expand(e_t - (e_ht_sub + z0 * r_k)) == 0)
    planted("drop B-dependent K return", sp.expand(e_b - e_hb_sub) == 0)

    # A derivative-affine control removes the quadratic (D Bhat)^2 term.
    # Its fourth-jet coefficient vanishes in this exact fixture.  Therefore
    # fourth order is attainable in the polynomial control, not forced for
    # Weinstein's derivative-affine first action.
    affine_root = sp.expand(root_lagrangian - sp.Rational(1, 2) * hb1**2)
    affine_pulled = sp.expand(affine_root.subs(substitutions))
    affine_e_t = sp.expand(
        sp.diff(affine_pulled, t[0])
        - total(sp.diff(affine_pulled, t[1]))
        + total(total(sp.diff(affine_pulled, t[2])))
    )
    exact("derivative-affine fourth-jet coefficient cancels", sp.diff(affine_e_t, t[4]) == 0)
    exact("derivative-affine action remains nontrivial", affine_e_t != 0)
    planted("written first action is proved fourth order", sp.diff(affine_e_t, t[4]) != 0)

    # Full second-order first-variation identity with both Green layers.
    p1 = sp.diff(pulled, t[2])
    p0 = sp.expand(sp.diff(pulled, t[1]) - total(p1))
    q0 = sp.diff(pulled, b[1])
    theta = sp.expand(p0 * eta[0] + p1 * eta[1] + q0 * beta[0])
    direct_variation = sp.expand(
        sum(sp.diff(pulled, t[index]) * eta[index] for index in range(3))
        + sum(sp.diff(pulled, b[index]) * beta[index] for index in range(2))
    )
    bulk_plus_boundary = sp.expand(e_t * eta[0] + e_b * beta[0] + total(theta))
    exact("twice-integrated Green identity", sp.expand(direct_variation - bulk_plus_boundary) == 0)
    exact("lower Green layer live", p0 != 0)
    exact("higher Green layer live", p1 != 0)
    exact("higher layer multiplies D variation", sp.diff(theta, eta[1]) == p1)
    planted("one Green layer is complete", sp.expand(direct_variation - (e_t * eta[0] + e_b * beta[0] + total(p0 * eta[0] + q0 * beta[0]))) == 0)
    planted("boundary-free Euler identity", sp.expand(direct_variation - (e_t * eta[0] + e_b * beta[0])) == 0)

    # A non-vacuous coupled Ward comparator.  For q=D t+b, delta t=-chi
    # and delta b=D chi.  Neither Euler contraction vanishes separately, but
    # the coupled Noether identity does.
    ward_lagrangian = sp.Rational(1, 2) * (t[1] + b[0]) ** 2
    ward_e_b = sp.diff(ward_lagrangian, b[0])
    ward_e_t = -total(sp.diff(ward_lagrangian, t[1]))
    ward_b_bulk = -total(ward_e_b)
    ward_t_bulk = -ward_e_t
    exact("Ward B contraction live", ward_b_bulk != 0)
    exact("Ward T contraction live", ward_t_bulk != 0)
    exact("coupled Ward cancellation", sp.expand(ward_b_bulk + ward_t_bulk) == 0)
    planted("isolated B equation is conserved", ward_b_bulk == 0)
    planted("isolated T equation is conserved", ward_t_bulk == 0)

    # The chosen structural K is intentionally not gauge-natural under this
    # shift symmetry.  Hence the comparator certifies the form of the Ward
    # burden but cannot promote the literal native Ward identity.
    chi0, chi1 = sp.symbols("chi0 chi1")
    delta_k = sp.expand(z0 * (-chi0) + z1 * (-chi1))
    exact("structural K gauge-naturality burden is live", delta_k != 0)
    planted("structural K proves native Ward identity", delta_k == 0)

    # Route accounting and source boundary are live assertions.
    type_level("independent B not source selected", result["route_comparison"][2]["source_grade"] == "REPOSITORY_EXTENSION_NOT_SOURCE_SELECTED")
    type_level("constraint surplus deferred", result["constraint_surplus"] == "UNCOMPUTED_PENDING_LITERAL_PORT_AND_GAUGE_BV_QUOTIENT")
    type_level("physical Ward not promoted", result["ward_status"] == "ROOT_EXTENSION_WARD_NOT_EVALUATED__SEPARATE_STRUCTURAL_WARD_COMPARATOR_PASS")
    planted("independent B adds no field freedom", registry["field_debit"]["independent_B"] == "NO_NEW_FIELD")
    planted("P3 owns the Green inverse", registry["field_debit"]["P1_P2_P3"] != "UNCHANGED_AND_UNUSED")

    total_count = EXACT + TYPE + PLANTED
    print(f"PW2A variational extension: {EXACT} algebraic exact + {TYPE} type/registry + {PLANTED} planted = {total_count} PASS")
    print("RESULT: the independent-B rival has an exact structural Euler/adjoint/two-Green-layer certificate")
    print("BOUNDARY: native K naturality, moving owners, literal coefficients, BV quotient, and analytic domain remain open")


if __name__ == "__main__":
    main()
