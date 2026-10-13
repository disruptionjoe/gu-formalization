#!/usr/bin/env python3
"""Arb whole-line finite-channel comparison and singular chart control for K1749.

The compact integral is enclosed by interval Taylor quadrature.  The two
unbounded tails are not sampled: a closed Gaussian moment bound encloses
them.  All transcendental operations use the repository-pinned
``python-flint==0.9.0`` backend.
"""
from __future__ import annotations

import json
from fractions import Fraction as Q
from pathlib import Path

from flint import arb, ctx, fmpq

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1749-arb-finite-channel-boundary.json"

ctx.dps = 100
ctx.threads = 1

Q_SMALL = Q(1, 1024)
S = Q(1, 32)
COMPACT_RADIUS = Q(11)
CELL_HALF_WIDTH = Q(1, 16)
TAYLOR_ORDER = 12


def aq(x: Q | int) -> arb:
    x = Q(x)
    return arb(fmpq(x.numerator, x.denominator))


def ball_q(lo: Q, hi: Q) -> arb:
    lo, hi = Q(lo), Q(hi)
    return arb(fmpq((lo + hi).numerator, (lo + hi).denominator),
               fmpq((hi - lo).numerator, (hi - lo).denominator)) / 2


def isolate_root() -> tuple[Q, Q]:
    """Isolate the unique positive K1744 cubic root by exact bisection."""
    poly = lambda u: 17*u**3 - 38*u**2 + 84*u - 24
    lo, hi = Q("0.327013679166041"), Q("0.327013679166043")
    assert poly(lo) < 0 < poly(hi)
    assert 76**2 - 4*51*84 < 0
    for _ in range(180):
        mid = (lo + hi) / 2
        if poly(mid) < 0:
            lo = mid
        else:
            hi = mid
    return lo, hi


class D:
    """First derivative jet in the chart variables (p,a)."""
    def __init__(self, v, dp=0, da=0):
        self.v, self.dp, self.da = arb(v), arb(dp), arb(da)

    @staticmethod
    def lift(x):
        return x if isinstance(x, D) else D(x)

    def __add__(self, other):
        other = self.lift(other)
        return D(self.v + other.v, self.dp + other.dp, self.da + other.da)

    __radd__ = __add__

    def __neg__(self):
        return D(-self.v, -self.dp, -self.da)

    def __sub__(self, other):
        return self + (-self.lift(other))

    def __rsub__(self, other):
        return self.lift(other) - self

    def __mul__(self, other):
        other = self.lift(other)
        return D(self.v*other.v,
                 self.dp*other.v + self.v*other.dp,
                 self.da*other.v + self.v*other.da)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.lift(other)
        return D(self.v/other.v,
                 (self.dp*other.v-self.v*other.dp)/other.v**2,
                 (self.da*other.v-self.v*other.da)/other.v**2)

    def __rtruediv__(self, other):
        return self.lift(other) / self

    def __pow__(self, n):
        if n == 0:
            return D(1)
        return D(self.v**n, n*self.v**(n-1)*self.dp,
                 n*self.v**(n-1)*self.da)


def chart_invariants(pv: arb, av: arb):
    p, a = D(pv, 1, 0), D(av, 0, 1)
    b = (1-p*a)/(1-p)
    moment = lambda n: p*a**n + (1-p)*b**n
    m4, m6, m8 = moment(2), moment(3), moment(4)
    u = 3-m4
    k6 = m6-15*m4+30
    h8 = m8-28*m6+210*m4-315
    return b, u, k6, h8/u**2


def channels():
    """Re-derive the two K1744 sections from the exact cubic/formulas."""
    ulo, uhi = isolate_root()
    root = ball_q(ulo, uhi)
    sigma = 2*(6-7*root)/(2-root)
    product = sigma-(3-root)
    discriminant = sigma**2-4*product
    a0 = (sigma-discriminant.sqrt())/2
    b0 = (sigma+discriminant.sqrt())/2
    p0 = (b0-1)/(b0-a0)
    _, _, k6, x = chart_invariants(p0, a0)
    jac = k6.dp*x.da-k6.da*x.dp
    c = aq(Q(35, 3))*root*root.sqrt()
    P = c*x.da/jac
    A = -c*x.dp/jac
    direction_a = a0*(b0-a0)
    beta = c/(k6.dp+k6.da*direction_a)
    selected = (p0+aq(S)*P, a0+aq(S)*A)
    fixed = (p0+aq(S)*beta, a0+aq(S)*beta*direction_a)

    def finish(name, pair):
        p, a = pair
        b, u, _, _ = chart_invariants(p, a)
        t = (aq(Q_SMALL)/u.v).sqrt()
        return {"name": name, "p": p, "a": a, "b": b.v,
                "u": u.v, "t": t, "v": 1-t}

    return finish("selected_k1738_linear", selected), finish("k1728_fixed_radii_linear", fixed), root


class T:
    """Truncated Taylor series with Arb coefficient balls."""
    def __init__(self, coeffs):
        self.c = [arb(x) for x in coeffs]

    @property
    def n(self):
        return len(self.c)

    @staticmethod
    def lift(x, n):
        if isinstance(x, T):
            assert x.n == n
            return x
        return T([x] + [0]*(n-1))

    def __add__(self, other):
        other = self.lift(other, self.n)
        return T([self.c[i]+other.c[i] for i in range(self.n)])

    __radd__ = __add__

    def __neg__(self):
        return T([-x for x in self.c])

    def __sub__(self, other):
        return self + (-self.lift(other, self.n))

    def __rsub__(self, other):
        return self.lift(other, self.n) - self

    def __mul__(self, other):
        other = self.lift(other, self.n)
        return T([sum((self.c[k]*other.c[j-k] for k in range(j+1)), arb(0))
                  for j in range(self.n)])

    __rmul__ = __mul__

    def reciprocal(self):
        out = [1/self.c[0]]
        for j in range(1, self.n):
            out.append(-sum((self.c[k]*out[j-k] for k in range(1, j+1)), arb(0))/self.c[0])
        return T(out)

    def __truediv__(self, other):
        return self * self.lift(other, self.n).reciprocal()

    def __rtruediv__(self, other):
        return self.lift(other, self.n) / self

    def __pow__(self, n):
        out = T.lift(1, self.n)
        base = self
        while n:
            if n & 1:
                out = out*base
            base = base*base
            n //= 2
        return out

    def exp(self):
        out = [self.c[0].exp()]
        for j in range(1, self.n):
            out.append(sum((aq(k)*self.c[k]*out[j-k] for k in range(1, j+1)), arb(0))/aq(j))
        return T(out)

    def sinh(self):
        return (self.exp()-(-self).exp())/2

    def cosh(self):
        return (self.exp()+(-self).exp())/2


def fisher_integrand(y: T, channel) -> T:
    """Positive-denominator Fisher density with respect to dy."""
    p, a, b, t, v = (channel[k] for k in ("p", "a", "b", "t", "v"))
    ra, rb, rt = a.sqrt(), b.sqrt(), t.sqrt()
    ca, cb = rt*ra/v, rt*rb/v
    wa = p*(-t*a/(2*v)).exp()
    wb = (1-p)*(-t*b/(2*v)).exp()
    d = wa*(ca*y).cosh()+wb*(cb*y).cosh()
    # This assertion is exercised both at midpoint balls and over each entire
    # Taylor-remainder cell.  Division is therefore never performed through
    # an interval that merely appears positive at a sampled point.
    assert d.c[0] > 0
    n = wa*ra*(ca*y).sinh()+wb*rb*(cb*y).sinh()
    residual = n-rt*y*d
    gaussian = (-(y*y)/(2*v)).exp()
    prefactor = t/(v**2*v.sqrt()*(2*arb.pi()).sqrt())
    return prefactor*gaussian*residual**2/d


def compact_integral(selected, fixed):
    h = CELL_HALF_WIDTH
    cells = int(COMPACT_RADIUS/h)
    total = arb(0)
    max_remainder = arb(0)
    for index in range(-cells, cells):
        midpoint = (Q(index)+Q(1, 2))*h
        local_half = h/2
        point = T([aq(midpoint), 1]+[0]*(TAYLOR_ORDER-1))
        point_diff = fisher_integrand(point, fixed)-fisher_integrand(point, selected)
        polynomial = arb(0)
        for degree in range(0, TAYLOR_ORDER, 2):
            polynomial += point_diff.c[degree]*aq(2*local_half**(degree+1)/Q(degree+1))

        interval_y = T([ball_q(midpoint-local_half, midpoint+local_half), 1]+[0]*(TAYLOR_ORDER-1))
        interval_diff = fisher_integrand(interval_y, fixed)-fisher_integrand(interval_y, selected)
        remainder_radius = (abs(interval_diff.c[TAYLOR_ORDER-1])
                            * aq(2*local_half**TAYLOR_ORDER/Q(TAYLOR_ORDER))).upper()
        remainder = arb(0, remainder_radius)
        total += polynomial+remainder
        if abs(remainder).upper() > max_remainder.upper():
            max_remainder = abs(remainder)
    return total, max_remainder, 2*cells


def tail_bound(channel) -> arb:
    """Two-sided analytic bound outside |y|<=COMPACT_RADIUS."""
    t, v, b = channel["t"], channel["v"], channel["b"]
    rmax = b.sqrt()
    mu = t.sqrt()*rmax
    ell = (aq(COMPACT_RADIUS)-mu)/v.sqrt()
    assert ell > 0
    normal_density = (-ell**2/2).exp()/(2*arb.pi()).sqrt()
    aa = rmax*(1+t)
    bb = (t*v).sqrt()
    gaussian_moment = 2*normal_density*(aa**2/ell+2*aa*bb+bb**2*(ell+1/ell))
    return t/v**2*gaussian_moment


def boundary_chart(selected):
    """Exact u=q chart: t=1, v=0, hence a discrete non-density."""
    p = selected["p"]
    a_singular = 1-((2-aq(Q_SMALL))*(1-p)/p).sqrt()
    b, u, _, _ = chart_invariants(p, a_singular)
    return {
        "p": p,
        "a": a_singular,
        "b": b.v,
        "u_minus_q": u.v-aq(Q_SMALL),
        "t": arb(1),
        "v": arb(0),
    }


def enc(x: arb) -> str:
    return x.str(45, radius=True, more=True)


def compute():
    selected, fixed, root = channels()
    for channel in (selected, fixed):
        assert channel["p"] > 0 and 1-channel["p"] > 0
        assert channel["a"] > 0 and 1-channel["a"] > 0
        assert channel["b"] > 1 and channel["u"] > aq(Q_SMALL)
        assert channel["t"] > 0 and channel["t"] < 1 and channel["v"] > 0
    compact, max_cell_remainder, cells = compact_integral(selected, fixed)
    selected_tail, fixed_tail = tail_bound(selected), tail_bound(fixed)
    tail = selected_tail+fixed_tail
    whole = compact+arb(0, tail.upper())
    boundary = boundary_chart(selected)
    assert whole > 0
    assert boundary["a"] > 0 and 1-boundary["a"] > 0 and boundary["b"] > 1
    assert boundary["u_minus_q"].contains(0)
    assert boundary["t"] == 1 and boundary["v"] == 0
    return {
        "root": enc(root),
        "q": "1/1024",
        "compact_radius": "11",
        "cell_half_width": "1/16",
        "taylor_order": TAYLOR_ORDER,
        "compact_cell_count": cells,
        "selected": {k: enc(v) for k, v in selected.items() if k != "name"},
        "fixed": {k: enc(v) for k, v in fixed.items() if k != "name"},
        "compact_gap_fixed_minus_selected": enc(compact),
        "selected_tail_upper": enc(selected_tail),
        "fixed_tail_upper": enc(fixed_tail),
        "combined_tail_upper": enc(tail),
        "whole_line_gap_fixed_minus_selected": enc(whole),
        "maximum_cell_remainder": enc(max_cell_remainder),
        "boundary": {k: enc(v) for k, v in boundary.items()},
    }


def validate():
    data = json.loads(ARTIFACT.read_text())
    got = compute()
    cert = data["arb_certificate"]
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1749"),
        ("backend", data["backend"] == "python-flint==0.9.0"),
        ("positive denominator", "strictly positive" in data["method"]["positive_denominator_form"]),
        ("compact Taylor", "Taylor" in data["method"]["compact_enclosure"]),
        ("analytic tails", "Gaussian" in data["method"]["tail_enclosure"]),
    ]
    for key in ("q", "compact_radius", "cell_half_width", "taylor_order", "compact_cell_count"):
        checks.append((f"parameter {key}", cert[key] == got[key]))
    for key in ("root", "compact_gap_fixed_minus_selected", "selected_tail_upper",
                "fixed_tail_upper", "combined_tail_upper", "whole_line_gap_fixed_minus_selected",
                "maximum_cell_remainder"):
        checks.append((f"containment {key}", arb(cert[key]).contains(arb(got[key]))))
    for channel in ("selected", "fixed", "boundary"):
        for key, value in got[channel].items():
            checks.append((f"containment {channel}.{key}", arb(cert[channel][key]).contains(arb(value))))
    gap = arb(cert["whole_line_gap_fixed_minus_selected"])
    checks += [
        ("strict finite ordering", gap > 0),
        ("boundary u=q", arb(cert["boundary"]["u_minus_q"]).contains(0)),
        ("boundary t=1", arb(cert["boundary"]["t"]) == 1),
        ("boundary v=0", arb(cert["boundary"]["v"]) == 0),
        ("singular chart separate", data["singular_boundary_chart"]["fisher_status"] == "+infinity (extended-value convention)"),
        ("not global", not data["decision"]["global_two_radius_optimizer_proved"]),
        ("not all seed", not data["decision"]["all_seed_optimizer_proved"]),
        ("protected", not data["decision"]["source_or_physical_status_change"]),
    ]
    for index, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {index:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    validate()
