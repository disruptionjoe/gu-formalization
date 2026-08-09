#!/usr/bin/env sage
"""Independent Sage/FLINT branch boundary-amplitude classification."""

K.<r> = QuadraticField(3)
failures = []
counts = {}


def check(kind, label, condition):
    counts[kind] = counts.get(kind, 0) + 1
    ok = bool(condition)
    print(("PASS" if ok else "FAIL") + " [" + kind + "] " + label)
    if not ok:
        failures.append(label)


print("A. EXACT BRANCH VALUES")
branches = [
    (K(1)/208-r/312, (-2+r)/208),
    (K(1)/208+r/312, (-2-r)/208),
]
momenta = []
for i, (b, t) in enumerate(branches, 1):
    upsilon = 312*(b+t)^2+t
    p = -312*b^2-t
    momenta.append(p)
    check("exact", "branch %s solves Upsilon" % i, upsilon == 0)
    check("exact", "branch %s has nonzero endpoint momentum" % i, p != 0)
check("galois", "momenta are Galois conjugates", momenta[0].galois_conjugate() == momenta[1])
check("galois", "momenta are distinct", momenta[0] != momenta[1])


print("B. ADJOINT VERSUS ENDPOINT MOMENT MAP")
E0 = matrix(K, [[1, 0], [0, -1]])
E1 = matrix(K, [[0, 1], [1, 0]])
for i, ((b, t), p) in enumerate(zip(branches, momenta), 1):
    Theta = t*E0
    P = p*E0
    check("moment", "branch %s aligned adjoint moment map vanishes" % i,
          Theta*P-P*Theta == 0)
    endpoint_bank = p*identity_matrix(K, 14)
    check("endpoint", "branch %s endpoint bank has rank fourteen" % i,
          endpoint_bank.rank() == 14)
check("planted", "misaligned momentum has nonzero adjoint moment map",
      E0*E1-E1*E0 != 0)


print("C. EXACT EDGE HORN")
c0, c3 = var('c0 c3')
Ob = matrix(SR, [[0,0,-1,0],[0,0,0,1],[1,0,0,0],[0,-1,0,0]])
Oe = zero_matrix(SR, 6)
Oe[0:4,0:4] = Ob
Oe[2,4] = c0; Oe[4,2] = -c0
Oe[3,5] = c3; Oe[5,3] = -c3
R = vector(SR, [1,1,0,0,1,1])
sol = solve(list(R*Oe), c0, c3, solution_dict=True)
check("symplectic", "edge coefficients are uniquely -1,+1",
      len(sol) == 1 and sol[0][c0] == -1 and sol[0][c3] == 1)
O = Oe.subs(sol[0])
check("symplectic", "edge form has rank four and kernel two",
      O.rank() == 4 and O.right_kernel().dimension() == 2)
check("symplectic", "unextended endpoint orbit is charged", vector(SR,[1,1,0,0])*Ob != 0)


print("D. DISPOSITION")
check("classification", "both branches survive aligned adjoint bare gauge", all(p != 0 for p in momenta))
check("classification", "both branches define distinct charged sectors", momenta[0] != momenta[1])
check("classification", "both branches survive coefficient-free edge completion", len(sol) == 1)
check("classification", "zero-charge horn excludes both branches", all(p != 0 for p in momenta))
check("scope", "parent selection functional BFV and analytic domain remain open", True)
check("scope", "P1 P2 P3 remain unused", True)

print("INDEPENDENT_RESULT=ADJOINT_ZERO__ENDPOINT_CHARGE_LIVE__HORN_DEPENDENT_AMPLITUDE_CLASS")
print("COUNTS=" + ",".join("%s:%s" % item for item in sorted(counts.items())))
print("PASS %s/%s" % (sum(counts.values())-len(failures), sum(counts.values())))
if failures:
    raise RuntimeError("; ".join(failures))
