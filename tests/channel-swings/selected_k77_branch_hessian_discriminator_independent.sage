#!/usr/bin/env sage
"""Independent QQ(sqrt(3)) audit of the K77 branch-Hessian shortcut."""

K.<r> = QuadraticField(3)
R.<b,t> = PolynomialRing(K)
checks = []


def check(label, condition):
    ok = bool(condition)
    checks.append(ok)
    print(("PASS" if ok else "FAIL") + " " + label)


metric_trace = 624*(b^2 + b*t + t^2/3) + t
I1 = 7*t*metric_trace
U = 312*(b+t)^2 + t
points = (
    (1/208-r/312, -1/104+r/208),
    (1/208+r/312, -1/104-r/208),
)
expected_hessians = (
    matrix(K, [[-84+42*r, -42+14*r], [-42+14*r, -28+14*r]]),
    matrix(K, [[-84-42*r, -42-14*r], [-42-14*r, -28-14*r]]),
)

Ib = I1.derivative(b)
It = I1.derivative(t)
H = matrix(R, [[Ib.derivative(b), Ib.derivative(t)],
               [It.derivative(b), It.derivative(t)]])
Ub = U.derivative(b)
Ut = U.derivative(t)

source_i1 = []
source_i2 = []
for index, (b0, t0) in enumerate(points):
    gradient = vector(K, [Ib(b0, t0), It(b0, t0)])
    hessian = H.apply_map(lambda value: value(b0, t0))
    check("branch %d is t-stationary but not B-stationary" % (index+1),
          gradient[1] == 0 and gradient[0] != 0)
    check("branch %d exact reconstruction Hessian" % (index+1),
          hessian == expected_hessians[index])

    # Under b=b0+x+c*x^2, the xx coefficient gains 2*c*dI/db.
    c0 = -hessian.det()/(2*gradient[0]*hessian[1,1])
    changed = matrix(K, hessian)
    changed[0,0] += 2*c0*gradient[0]
    check("branch %d noncritical Hessian rank is coordinate-variable" % (index+1),
          c0 != 0 and changed.det() == 0)

    source_i1.append(hessian[1,1])
    du = vector(K, [Ub(b0, t0), Ut(b0, t0)])
    h2 = du.column()*du.row()
    source_i2.append(h2[1,1])
    check("branch %d residual-square Hessian has rank one" % (index+1),
          U(b0, t0) == 0 and h2.rank() == 1 and h2.det() == 0)

check("naive reconstruction determinants have opposite signs",
      expected_hessians[0].det() < 0 and expected_hessians[1].det() > 0)
check("source I1 restrictions are both negative",
      source_i1 == [14*(r-2), -14*(r+2)]
      and all(value < 0 for value in source_i1))
check("source I1 fixed-coordinate ratio is positive nonunit",
      source_i1[0]/source_i1[1] == 7-4*r
      and source_i1[0]/source_i1[1] > 0
      and source_i1[0]/source_i1[1] != 1)
check("source residual-square restrictions are positive conjugates",
      source_i2 == [7-4*r, 7+4*r]
      and all(value > 0 for value in source_i2))

# Plants reject the two tempting overclaims directly.
check("PLANT Galois conjugacy does not preserve real sign ordering",
      (7-4*r) > 0 and (7+4*r) > 0 and (3-2*r) < 0 and (3+2*r) > 0)
check("PLANT noncritical reconstruction Hessian is not a Morse selector",
      all(Ib(p[0], p[1]) != 0 for p in points))
check("PLANT neither scalar source action picks one branch by rank or inertia",
      all(value < 0 for value in source_i1)
      and all(value > 0 for value in source_i2))

if not all(checks):
    raise SystemExit("independent branch-Hessian audit failed")
print("PASS %d/%d" % (len(checks), len(checks)))
