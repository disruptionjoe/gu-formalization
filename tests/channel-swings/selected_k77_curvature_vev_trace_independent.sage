#!/usr/bin/env sage
"""Independent QQ certificate for the K77 scalar-curvature-jet branch."""


COUNTS = {"exact": 0, "control": 0, "planted": 0}
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(("PASS" if ok else "FAIL") + " [" + kind + "] " + label)
    if not ok:
        FAILURES.append(label)


R = PolynomialRing(QQ, names=("b", "t", "r"))
b, t, r = R.gens()
L = 7*t*(624*b^2 + 624*b*t + 208*t^2 + t + 624*r)
e_b = 2*b + t
raw = 312*(b+t)^2 + t + 312*r
metric = 624*b^2 + 624*b*t + 208*t^2 + t + 624*r

b_star = QQ(1)/208
t_star = -QQ(1)/104
r_star = QQ(1)/129792
point = {b: b_star, t: t_star, r: r_star}

check("exact", "independent nonzero branch solves reduced B equation", e_b.subs(point) == 0)
check("exact", "independent nonzero branch solves raw residual", raw.subs(point) == 0)
check("exact", "independent nonzero branch solves metric trace", metric.subs(point) == 0)
check("exact", "independent complete action density vanishes", L.subs(point) == 0)

J = matrix(QQ, [
    [e_b.derivative(x).subs(point) for x in (b, t, r)],
    [raw.derivative(x).subs(point) for x in (b, t, r)],
    [metric.derivative(x).subs(point) for x in (b, t, r)],
])
check("exact", "independent constraint Jacobian has rank three", J.rank() == 3)
check("exact", "independent constraint determinant is nonzero", J.det() != 0)

base = 7*t*(624*b^2 + 624*b*t + 208*t^2 + t)
curvature = 4368*r*t
check("exact", "independent base action is plus seven over 21632",
      base.subs(point) == QQ(7)/21632)
check("exact", "independent curvature action is minus seven over 21632",
      curvature.subs(point) == -QQ(7)/21632)
check("exact", "independent two contributions cancel", (base + curvature).subs(point) == 0)

reduced_raw = raw.subs(b=-t/2)
r_on_raw = -(t^2/4 + t/312)
check("exact", "independent solved curvature value satisfies the reduced raw equation",
      reduced_raw.subs(r=r_on_raw) == 0)
reduced_metric = metric.subs(b=-t/2).subs(r=r_on_raw)
check("exact", "independent saturated elimination is minus t times 104t plus one",
      reduced_metric == -t*(104*t+1))
check("exact", "independent unique nonzero root is minus one over 104",
      reduced_metric.subs(t=t_star) == 0 and 104*t_star + 1 == 0)

check("control", "the r-zero predecessor is not metric critical",
      metric.subs({b: QQ(1)/156, t: -QQ(1)/78, r: 0}) != 0)
check("control", "the T-zero family remains distinct from the VEV horn",
      raw.subs({t: 0, r: -b^2}) == 0 and L.subs({t: 0, r: -b^2}) == 0)
check("planted", "PLANT the curvature value is solved rather than set to zero", r_star != 0)
check("planted", "PLANT zero total action does not mean each contribution vanishes",
      base.subs(point) != 0 and curvature.subs(point) != 0)

print("BRANCH=(1/208,-1/104,1/129792)")
print("ACTION_SPLIT=(7/21632,-7/21632)")
print("JACOBIAN_DET=" + str(J.det()))
print("CHECKS=" + " ".join(kind + ":" + str(COUNTS[kind]) for kind in sorted(COUNTS)))
if FAILURES:
    raise RuntimeError("FAILURES: " + "; ".join(FAILURES))
print("PASS " + str(sum(COUNTS.values())) + "/" + str(sum(COUNTS.values())))
