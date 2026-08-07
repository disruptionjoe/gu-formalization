#!/usr/bin/env python3
"""PW2 exact derivative reconciliation and complete order-two rank gate."""

from __future__ import annotations

import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/pw2-action-graph-experiment-registry.json"


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


@dataclass(frozen=True)
class Dual:
    value: Fraction
    tangent: Fraction

    def __add__(self, other):
        other = promote(other)
        return Dual(self.value + other.value, self.tangent + other.tangent)

    __radd__ = __add__

    def __neg__(self):
        return Dual(-self.value, -self.tangent)

    def __sub__(self, other):
        return self + (-promote(other))

    def __rsub__(self, other):
        return promote(other) - self

    def __mul__(self, other):
        other = promote(other)
        return Dual(self.value * other.value, self.tangent * other.value + self.value * other.tangent)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = promote(other)
        return Dual(
            self.value / other.value,
            (self.tangent * other.value - self.value * other.tangent) / (other.value * other.value),
        )


def promote(value):
    if isinstance(value, Dual):
        return value
    return Dual(Fraction(value), Fraction(0))


def action_graph(t, tx, txx, b, bx, r):
    """Frozen scalar graph with K depending on the full first jet.

    It mirrors only the polynomial dependency shape of the written
    transgression action.  It is not identified with the native Shiab action.
    """

    z0 = 1 + r
    z1 = 2 - r
    k = z0 * t + z1 * tx
    kx = z0 * tx + z1 * txx
    bhat = b + k
    bhat_x = bx + kx
    that = t - k
    that_x = tx - kx
    kappa = Fraction(5, 3)
    return that * (bhat_x + Fraction(1, 2) * that_x + Fraction(1, 3) * that * that) + Fraction(1, 2) * kappa * that * that


exact_checks = 0
planted_checks = 0


def exact(name, condition):
    global exact_checks
    if not condition:
        raise AssertionError(f"exact check failed: {name}")
    exact_checks += 1


def planted(name, false_claim):
    global planted_checks
    if false_claim:
        raise AssertionError(f"planted false claim unexpectedly passed: {name}")
    planted_checks += 1


def main():
    registry = load(REGISTRY)
    exact("registry status", registry["status"] == "PW2_EXACT_DERIVATIVE_AND_RANK_CERTIFICATE")
    exact("heuristic boundary", registry["selector_role"] == "SCHEDULING_ONLY_NO_SCIENTIFIC_VERDICT")
    exact("qualification frozen", registry["qualification_policy"]["post_reveal_refit"] == "INVALIDATES_BANK")

    # Independent exact forward AD versus a SymPy derivative of the same
    # frozen graph.  These are six jet-coordinate partials; they are not an
    # Euler/Green packet until the txx variation is integrated twice.
    base = [Fraction(2), Fraction(-1), Fraction(3), Fraction(1), Fraction(4), Fraction(1)]
    direction = [Fraction(1), Fraction(2), Fraction(-2), Fraction(3), Fraction(-1), Fraction(1)]
    dual_args = [Dual(value, tangent) for value, tangent in zip(base, direction)]
    dual_result = action_graph(*dual_args)

    names = sp.symbols("t tx txx b bx r")
    symbolic = action_graph(*names)
    symbolic_directional = sum(sp.diff(symbolic, variable) * tangent for variable, tangent in zip(names, direction))
    substitutions = dict(zip(names, map(sp.Rational, base)))
    exact("AD action value", dual_result.value == Fraction(symbolic.subs(substitutions)))
    exact("AD first variation", dual_result.tangent == Fraction(symbolic_directional.subs(substitutions)))
    for index, variable in enumerate(names):
        one_hot = [Fraction(0)] * len(base)
        one_hot[index] = Fraction(1)
        packet = action_graph(*(Dual(value, tangent) for value, tangent in zip(base, one_hot)))
        expected = sp.diff(symbolic, variable).subs(substitutions)
        exact(f"owner derivative {variable}", packet.tangent == Fraction(expected))

    # K really uses the full first jet: suppressing txx changes the action
    # derivative while t and exterior-style lower data are held fixed.
    full_value = action_graph(*base)
    dropped_txx = action_graph(base[0], base[1], Fraction(0), base[3], base[4], base[5])
    exact("second jet return is live after differentiating K", full_value != dropped_txx)
    planted("abbreviated graph equals full graph", full_value == dropped_txx)

    # Exact composition of A=A2 D^2+A1 D+A0 and Z=Z1 D+Z0.
    x = sp.symbols("x")
    r = sp.symbols("r")
    a2 = sp.Matrix([[1, r], [0, 0]])
    a1 = sp.Matrix([[0, -1], [0, 0]])
    a0 = sp.zeros(2)
    z1 = sp.Matrix([[-r, 0], [1, 0]])
    z0 = sp.Matrix([[3 - r, 0], [0, 0]])
    dz1 = z1.diff(r)
    dz0 = z0.diff(r)
    ddz1 = dz1.diff(r)
    ddz0 = dz0.diff(r)

    c3 = sp.simplify(a2 * z1)
    c2_terms = {
        "2A2_dZ1": sp.simplify(2 * a2 * dz1),
        "A2_Z0": sp.simplify(a2 * z0),
        "A1_Z1": sp.simplify(a1 * z1),
    }
    c2 = sp.simplify(sum(c2_terms.values(), sp.zeros(2)))
    c1 = sp.simplify(a2 * (ddz1 + 2 * dz0) + a1 * (dz1 + z0) + a0 * z1)
    c0 = sp.simplify(a2 * ddz0 + a1 * dz0 + a0 * z0)
    exact("order three cancels", c3 == sp.zeros(2))
    exact("all C2 terms live", all(term != sp.zeros(2) for term in c2_terms.values()))
    exact("complete C2", c2 == sp.Matrix([[-r, 0], [0, 0]]))

    f0 = sp.Function("f0")(r)
    f1 = sp.Function("f1")(r)
    f = sp.Matrix([f0, f1])
    zf = z1 * f.diff(r) + z0 * f
    composed = sp.simplify(a2 * zf.diff(r, 2) + a1 * zf.diff(r) + a0 * zf)
    assembled = sp.simplify(c3 * f.diff(r, 3) + c2 * f.diff(r, 2) + c1 * f.diff(r) + c0 * f)
    exact("Leibniz composition", sp.simplify(composed - assembled) == sp.zeros(2, 1))

    # At r=0 the abbreviated A2 Z0 block has rank one but the complete C2
    # vanishes through the derivative and A1Z1 returns.
    abbreviated = c2_terms["A2_Z0"]
    exact("abbreviated block nonzero at exception", abbreviated.subs(r, 0).rank() == 1)
    exact("complete block zero at exception", c2.subs(r, 0).rank() == 0)
    planted("A2Z0 determines complete rank", abbreviated.subs(r, 0).rank() == c2.subs(r, 0).rank())
    planted("omit 2A2dZ1", sp.simplify(c2 - c2_terms["2A2_dZ1"]) == c2)
    planted("omit A1Z1", sp.simplify(c2 - c2_terms["A1_Z1"]) == c2)

    # Fraction-free generic rank certificate: the 1x1 pivot minor is -r;
    # every 2x2 minor vanishes.  Hence rank=1 on D(r), rank=0 on V(r).
    pivot_minor = sp.factor(c2[0, 0])
    determinant = sp.factor(c2.det())
    exact("pivot polynomial", pivot_minor == -r)
    exact("rank upper bound", determinant == 0)
    exact("generic sample rank", all(c2.subs(r, value).rank() == 1 for value in (-3, -1, 1, 2, 5)))
    exact("exceptional sample rank", c2.subs(r, 0).rank() == 0)
    planted("finite samples prove genericity", registry["rank_certificate"]["basis"] == "SAMPLES_ONLY")
    planted("exception mislabeled generic", 0 in registry["qualification_policy"]["generic_points"])

    # Moving coefficient identity.  Since A2 Z1=0 identically,
    # (dA2)Z1 + A2(dZ1)=0; freezing A2 would silently lose the first term.
    moving_a2 = sp.simplify(a2.diff(r) * z1)
    moving_z1 = sp.simplify(a2 * dz1)
    exact("moving coefficient product rule", sp.simplify(moving_a2 + moving_z1) == sp.zeros(2))
    exact("moving coefficient term live", moving_a2 != sp.zeros(2) and moving_z1 != sp.zeros(2))
    planted("fixed A2 preserves product rule", moving_z1 == sp.zeros(2))

    # The registry must keep discovery, qualification, and theorem distinct.
    exact("discovery not evidence", registry["discovery_bank"]["evidence_grade"] == "HEURISTIC_SCHEDULING")
    exact("exact certificate required", registry["rank_certificate"]["basis"] == "PIVOT_MINOR_PLUS_VANISHING_MAXIMAL_MINORS")
    exact("native promotion stopped", registry["native_promotion"] == "STOPPED_BY_SOURCE_DOMAIN_AND_ACTIVE_PORT")
    planted("ML gives truth probability", registry["selector_role"] != "SCHEDULING_ONLY_NO_SCIENTIFIC_VERDICT")

    print(f"PW2 derivative/rank gate: {exact_checks} exact + {planted_checks} planted = {exact_checks + planted_checks} PASS")


if __name__ == "__main__":
    main()
