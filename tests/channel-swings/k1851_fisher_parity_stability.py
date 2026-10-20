#!/usr/bin/env python3
"""Exact algebra for the half-line Stein certificate; continuum proof is in K1851."""
from pathlib import Path
import hashlib
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "lab/process/k1851-fisher-parity-stability.json"
r = json.loads(PATH.read_text())
checks = {}


def ck(name, value):
    assert bool(value), name
    checks[name] = True


x, y = s.symbols("x y", real=True)
a, b, d, c, e = map(s.Rational, r["score"])
N = a + b*y + d*y*y
D = 1 + c*y + e*y*y
slope = s.Rational(r["compact_slope"])
radius = s.Rational(r["tail_radius"])
factor = s.Rational(r["stein_factor"])
upper_poly = s.Poly(N-slope*D, y)
upper_coefficients = [upper_poly.nth(j) for j in range(3)]
tail_poly = s.Poly(s.expand(N.subs(y, y+radius**2)-D.subs(y, y+radius**2)), y)
ck("positive denominator", c > 0 and e > 0)
ck("compact upper monotonic coefficients", all(v > 0 for v in upper_coefficients[1:]))
ck("compact upper endpoint negative", upper_poly.eval(1) < 0)
ck("compact upper exact coefficients", list(map(str, upper_coefficients)) == r["compact_upper_polynomial"])
ck("N increasing on nonnegative line", b > 0 and d > 0)
ck("N positive at one", N.subs(y, 1) > 0)
ck("translated tail coefficients positive", all(v > 0 for v in tail_poly.all_coeffs()))
ck("translated tail exact coefficients", [str(tail_poly.nth(j)) for j in range(3)] == r["translated_tail_polynomial"])
ck("compact and tail constants", slope == s.Rational(1, 2) and radius == s.Rational(3, 2))
exponent = slope/2
ck("geometric exponential majorant", 0 < exponent < 1 and 1/(1-exponent) == factor)
ck("middle tail below Stein factor", radius-1+1/radius < factor)
ck("exterior tail below Stein factor", 1/radius < factor)
A, B, C = map(s.Rational, r["minorant"])
L, U, delta = map(s.Rational, [r["lower"], r["upper"], r["score_budget"]])
ck("fixed moment dual value", L == A+B+2*C)
ck("positive exact score budget", 0 < delta == U-L)
ck("reference bound squared", factor**2*delta == s.Rational(r["reference_tv_bound_squared"]))
ck("pair bound squared", 4*factor**2*delta == s.Rational(r["optimizer_tv_bound_squared"]))
ck("reference display threshold", factor**2*delta < s.Rational(47, 1000)**2)
ck("optimizer display threshold", 4*factor**2*delta < s.Rational(93, 1000)**2 < s.Rational(1, 10)**2)
ck("rational square-root majorant", delta < s.Rational(r["score_sqrt_upper"])**2)
ck("rational pair bound", 2*factor*s.Rational(r["score_sqrt_upper"]) == s.Rational(r["optimizer_tv_rational_upper"]))
budget = s.Rational(r["moment_error_budget"])
ck("moment error budget", delta+budget == s.Rational(1, 25)**2)
ck("moment error TV target", factor*(s.Rational(1, 25)+s.Rational(r["score_sqrt_upper"])) == s.Rational(1, 10))
ck("moment penalty signs", B > 0 and C < 0 and list(map(str, [B, -C])) == r["moment_penalties"])
ck("asymmetry budget", s.Rational(r["asymmetry_budget"])+s.Rational(r["optimizer_tv_rational_upper"]) == s.Rational(1, 10))
info, e2, e4, remainder, J = s.symbols("info e2 e4 remainder J")
ck("moment residual signs", s.expand((info-A-B*(1+e2)-C*(2+e4))-(info-L-B*e2-C*e4)) == 0)
u, up, f, fp, gg = s.symbols("u up f fp gg")
ck("weak Stein integration sign", s.expand((fp-gg*f)*u*u+f*(2*up+gg*u)*u-fp*u*u-2*f*u*up) == 0)
p, q, dp, dq = s.symbols("p q dp dq", positive=True)
deficit = (dp*dp/p+dq*dq/q)/2-(dp+dq)**2/(2*(p+q))
ck("Fisher convexity exact deficit", s.factor(deficit-(q*dp-p*dq)**2/(2*p*q*(p+q))) == 0)
aa, bb, kk, Fval, Dval = s.symbols("aa bb kk Fval Dval")
ck("all parity fixed moment form", s.expand((Fval+Dval+aa+bb*kk)-(Fval+aa+bb*kk)) == Dval)
for dep in r["dependencies"]:
    ck("dependency "+dep["path"], hashlib.sha256((ROOT/dep["path"]).read_bytes()).hexdigest() == dep["sha256"])
base = json.loads((ROOT/r["dependencies"][1]["path"]).read_text())
ck("same pinned score and minorant", r["score"] == base["certificate"]["score"] and r["minorant"] == base["certificate"]["minorant"])
ck("same pinned value bounds", r["lower"] == base["lower"] and r["upper"] == base["upper"])
r["mathematical_checks"] = checks
PATH.write_text(json.dumps(r, indent=2)+"\n")
print("K1851 exact groups", len(checks))
