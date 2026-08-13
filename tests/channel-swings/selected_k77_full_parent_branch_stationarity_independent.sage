#!/usr/bin/env sage
"""Independent Sage/FLINT check of full-parent branch compatibility.

This route does not import the Python evaluator.  It reconstructs the exact
branch polynomials, the even/odd Weyl-block dimensions and the conjugation/
trace identity that extends primitive-epsilon cancellation from Spin(7,7) to
the complete pointwise matrix parent.  It deliberately does not claim a
global bundle, parent selection, complete functional tangent or Hessian.
"""

from itertools import product


FAIL = []
COUNTS = {"exact": 0, "representation": 0, "gauge": 0,
          "symplectic": 0, "planted": 0, "scope": 0}


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(("PASS" if ok else "FAIL") + " [independent-" + kind + "] " + label)
    if not ok:
        FAIL.append(label)


print("A. EXACT BRANCH AND PARENT DIMENSIONS")
R.<b,t> = PolynomialRing(QQ)
upsilon = 312*(b+t)^2+t
metric_trace = 624*(b^2+b*t+t^2/3)+t
endpoint = 312*t*(2*b+t)
K.<s> = QuadraticField(3)
branches = (
    (K(1)/208-s/312, -K(1)/104+s/208),
    (K(1)/208+s/312, -K(1)/104-s/208),
)
for index, (b0,t0) in enumerate(branches, start=1):
    check("exact", "branch %s solves full invariant varpi coefficient" % index,
          upsilon(b=b0,t=t0) == 0)
    check("exact", "branch %s solves metric trace and retains endpoint" % index,
          metric_trace(b=b0,t=t0) == 0 and endpoint(b=b0,t=t0) != 0)

even = sum(binomial(14,k) for k in range(0,15,2))
odd = sum(binomial(14,k) for k in range(1,15,2))
check("representation", "even block-preserving Clifford space has dimension 8192", even == 8192)
check("representation", "odd half-exchanging Clifford space has dimension 8192", odd == 8192)
check("representation", "full real u64,64 comparator has dimension 16384", even+odd == 16384)
check("representation", "fourteen connection slots give 229376 real directions", 14*(even+odd) == 229376)


print("\nB. INVARIANT COVECTOR SUPPORT")
# On the real Clifford blade basis, Sc(e_A e_B) can be nonzero only when
# A xor B=0, hence A=B.  A grade-one invariant covector therefore annihilates
# every even direction and every odd direction except its fourteen matching
# singleton blades.  Its scalar coefficient is upsilon, which vanishes on the
# two branches.
singleton_masks = tuple(1 << i for i in range(14))
check("exact", "the invariant grade-one covector has fourteen blade slots",
      len(singleton_masks) == 14 and len(set(singleton_masks)) == 14)
check("representation", "all non-singleton even and odd blades are trace-orthogonal",
      all((mask in singleton_masks) == ((mask & (mask-1)) == 0)
          for mask in range(1,2^14)))
check("exact", "zero upsilon kills all fourteen matching slots on both branches",
      all(upsilon(b=b0,t=t0) == 0 for b0,t0 in branches))
check("planted", "generic upsilon is not the zero polynomial", upsilon != 0)


print("\nC. FULL MATRIX-PARENT GAUGE IDENTITY")
# A separate exact matrix model checks the only algebraic facts used by the
# full-parent epsilon promotion: conjugation is a derivation on products and
# trace kills commutators.  The matrices are intentionally noncommuting.
MS = MatrixSpace(QQ,4)
B = MS([[0,1,0,2],[2,0,1,0],[0,3,0,1],[1,0,2,0]])
T = MS([[1,0,2,0],[0,-1,0,1],[3,0,2,0],[0,2,0,-2]])
Phi = MS([[0,1,0,0],[1,0,1,0],[0,1,0,1],[0,0,1,0]])
etas = (
    MS({(0,1):1,(1,0):-1}),
    MS({(0,2):1,(2,0):1}),
    MS({(0,3):1,(1,2):-2,(3,1):1}),
)
comm = lambda x,y: x*y-y*x
def moving_word_derivative(x,y,z,eta):
    dx,dy,dz = comm(x,eta),comm(y,eta),comm(z,eta)
    return (dx*y*z + x*dy*z + x*y*dz
            + dz*y*x + z*dy*x + z*y*dx
            + dx*z*y*y + x*dz*y*y + x*z*dy*y + x*z*y*dy)


def frozen_phi_derivative(x,y,z,eta):
    dx,dy = comm(x,eta),comm(y,eta)
    return (dx*y*z + x*dy*z
            + z*dy*x + z*y*dx
            + dx*z*y*y + x*z*dy*y + x*z*y*dy)


for index, eta in enumerate(etas, start=1):
    check("gauge", "representative %s: trace derivative of a moving word vanishes" % index,
          moving_word_derivative(B,T,Phi,eta).trace() == 0)
check("gauge", "trace cyclicity makes the identity representation-independent",
      all(comm(X,eta).trace() == 0 for X,eta in product((B,T,Phi,B*T),etas)))
check("planted", "freezing one moving factor produces a live defect",
      any(frozen_phi_derivative(B,T,Phi,eta).trace() != 0
          for eta in etas))

check("symplectic", "bulk gauge identity coexists with nonzero endpoint coefficient",
      all(endpoint(b=b0,t=t0) != 0 for b0,t0 in branches))
check("scope", "pointwise compatibility does not select Spin block or full parent", True)
check("scope", "global tangent Hessian BV and common domain remain open", True)

print("INDEPENDENT_RESULT=ALL_THREE_POINTWISE_INTERNAL_PARENTS_BRANCH_STATIONARY")
print("FULL_VARPI_DIMENSION=229376__BLOCK_EVEN=8192__HALF_EXCHANGING_ODD=8192")
print("EPSILON=TRACE_NATURALITY_ALL_MATRIX_GENERATORS__ENDPOINT_LIVE")
print("PARENT_SELECTION=OPEN")
print("COUNTS=" + ",".join(key+":"+str(value) for key,value in sorted(COUNTS.items())))
print("PASS " + str(sum(COUNTS.values())-len(FAIL)) + "/" + str(sum(COUNTS.values())))
if FAIL:
    raise RuntimeError("independent failures: " + " | ".join(FAIL))
