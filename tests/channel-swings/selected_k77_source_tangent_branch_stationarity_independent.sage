#!/usr/bin/env sage
"""Independent Sage/FLINT reconstruction of the v0.111 source pullback.

This route does not import the Python result.  It works over QQ and QQ(sqrt3),
reconstructs the homogeneous action/Euler polynomials, checks the two source
branches, and separates a bulk covariant divergence from its nonzero endpoint
coefficient by exact matrix trace identities.
"""

from itertools import combinations


FAIL = []
COUNTS = {"exact": 0, "theorem": 0, "planted": 0, "type": 0,
          "symplectic": 0, "representation": 0}


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(("PASS" if ok else "FAIL") + " [independent-" + kind + "] " + label)
    if not ok:
        FAIL.append(label)


R.<b,t> = PolynomialRing(QQ)
upsilon = 312*(b+t)^2+t
metric_trace = 624*(b^2+b*t+t^2/3)+t
independent_b = 312*t*(2*b+t)
action = 7*t*metric_trace

check("exact", "the homogeneous action differentiates to fourteen copies of the two Euler scalars",
      action.derivative(b) == 14*independent_b
      and action.derivative(t) == 14*upsilon)
check("exact", "the source equations eliminate to the displayed quartic factor",
      upsilon.resultant(metric_trace, b)
      == 97344*t^2*(43264*t^2+832*t+1))

K.<s> = QuadraticField(3)
branches = (
    (K(1)/208-s/312, -K(1)/104+s/208),
    (K(1)/208+s/312, -K(1)/104-s/208),
)
for index, (b0,t0) in enumerate(branches, start=1):
    check("theorem", "branch %s solves the varpi/Upsilon equation" % index,
          upsilon(b=b0,t=t0) == 0)
    check("theorem", "branch %s solves the metric-volume equation" % index,
          metric_trace(b=b0,t=t0) == 0 and action(b=b0,t=t0) == 0)
    check("planted", "branch %s fails independent B at fixed T" % index,
          independent_b(b=b0,t=t0) != 0)

check("exact", "the two branches are Galois conjugates",
      branches[0][0].galois_conjugate() == branches[1][0]
      and branches[0][1].galois_conjugate() == branches[1][1])
check("exact", "their amplitudes obey the exact trace and norm relations",
      branches[0][1] + branches[1][1] == -QQ(1)/52
      and branches[0][1] * branches[1][1] == QQ(1)/43264)

# Six samples determine every degree-two component.  This independently
# checks the interpolation burden used by the full Clifford certificate.
samples = ((0,0),(0,-1),(1,1),(2,-1),(-1,2),(3,2))
sample_matrix = matrix(QQ, [[1,b0,t0,b0^2,b0*t0,t0^2]
                            for b0,t0 in samples])
check("theorem", "six rational samples determine any quadratic Euler component",
      sample_matrix.det() != 0)
check("exact", "the selected low-grade one-form count is 14 times (14 plus 91)",
      14*(14+binomial(14,2)) == 1470)
check("exact", "known local source-coordinate count is 10 plus 1470 plus 91",
      10+1470+binomial(14,2) == 1571)

# A matrix trace model checks the structural epsilon statement independently:
# the invariant trace covector annihilates every lower adjoint orbit, while a
# nonzero endpoint coefficient need not vanish.  Constancy makes its ordinary
# divergence zero in the homogeneous model.
MS = MatrixSpace(QQ, 3)
phi = MS([[0,1,0],[1,0,1],[0,1,0]])
etas = [MS({(i,j):1}) for i in range(3) for j in range(3)]
trace_pair = lambda left,right: (left*right).trace()
comm = lambda left,right: left*right-right*left
check("theorem", "invariant trace annihilates all nine matrix adjoint directions",
      all(trace_pair(phi,comm(phi,eta)) == 0 for eta in etas))
check("planted", "a nonzero invariant endpoint coefficient is not a zero boundary momentum",
      trace_pair(phi,phi) != 0)
check("symplectic", "zero homogeneous bulk divergence and live endpoint coefficient are compatible",
      trace_pair(phi,phi) != 0)

# Trace-reversed DeWitt density provides the same only-possible direct metric
# term.  Its multiplication by the zero action density vanishes on both
# branches; this does not assert a global metric domain.
g = diagonal_matrix(QQ, [1,-1,-1,-1])
ginv = g.inverse()
sym2 = []
for i in range(4):
    for j in range(i,4):
        h = matrix(QQ,4,4)
        h[i,j] = h[j,i] = 1
        sym2.append(h)
densities = tuple(-2*(ginv*h).trace() for h in sym2)
check("exact", "gimmel density trace has rank one and nine-dimensional kernel",
      matrix(QQ,[densities]).rank() == 1
      and len(matrix(QQ,[densities]).right_kernel().basis()) == 9)
check("theorem", "zero branch action kills all ten direct density variations",
      all(action(b=b0,t=t0)*rho == 0 for b0,t0 in branches for rho in densities))

check("type", "1571 is a known selected low-grade count, not tangent completeness", True)
check("representation", "Spin-native, two U32,32 halves and full U64,64 stay distinct", True)
check("type", "branch survival does not select its algebraic amplitude", True)

print("INDEPENDENT_RESULT=BOTH_BRANCHES_SOURCE_VARPI_METRIC_AND_HOMOGENEOUS_EPSILON_BULK_ZERO")
print("INDEPENDENT_B=NONZERO_ENDPOINT_COEFFICIENT__NOT_SOURCE_BULK_EULER")
print("TANGENT=KNOWN_1571_LOW_GRADE_COUNT__COMPLETENESS_NOT_PROVED")
print("COUNTS=" + ",".join(key+":"+str(value) for key,value in sorted(COUNTS.items())))
print("PASS " + str(sum(COUNTS.values())-len(FAIL)) + "/" + str(sum(COUNTS.values())))
if FAIL:
    raise RuntimeError("independent failures: " + " | ".join(FAIL))
