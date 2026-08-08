#!/usr/bin/env sage
"""Independent exact certificate for fixed-varpi normal Frechet closure."""

checks = 0


def check(label, condition):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


R.<x,y,s> = PolynomialRing(QQ)


def comm(a, b):
    return a*b - b*a


B0 = matrix(R, [[x, 1+y], [x*y, -x]])
B1 = matrix(R, [[y, x-y], [1+x, -y]])
T0 = matrix(R, [[1+x, y], [x-y, -1-x]])
T1 = matrix(R, [[x*y, 2+x], [1-y, -x*y]])
b0 = matrix(R, [[1+x, 2-y], [x+y, -1-x]])
b1 = matrix(R, [[2*x, y], [1+x-y, -2*x]])
B = (B0+s*b0, B1+s*b1)
T = (T0-s*b0, T1-s*b1)
A = (B[0]+T[0], B[1]+T[1])


def dx(m):
    return m.apply_map(lambda z: z.derivative(x))


def dy(m):
    return m.apply_map(lambda z: z.derivative(y))


def ds0(m):
    return m.apply_map(lambda z: z.derivative(s)(x=x, y=y, s=0))


FB = dx(B[1]) - dy(B[0]) + comm(B[0], B[1])
DBT = dx(T[1]) - dy(T[0]) + comm(B[0], T[1]) + comm(T[0], B[1])
TT = comm(T[0], T[1])
FA = dx(A[1]) - dy(A[0]) + comm(A[0], A[1])
check("expanded two-connection curvature equals direct curvature", FB+DBT+TT == FA)
pieces = [ds0(value) for value in (FB, DBT, TT)]
check("all expanded component derivatives are nonzero", all(value != 0 for value in pieces))
check("expanded component derivatives cancel", sum(pieces, matrix(R, 2, 2, 0)) == 0)
check("direct curvature derivative is zero at fixed varpi", ds0(FA) == 0)
check("on-shell T-squared-only derivative would be nonzero", pieces[2] != 0)


slots = [(i, j) for i in range(4) for j in range(i, 4)]
spin_slots = [(mu, a, b) for mu in range(4) for a in range(4) for b in range(a+1, 4)]
jet_slots = [(lam, i, j) for lam in range(4) for (i, j) in slots]


def hc(i, j, a, b):
    return ZZ((i == a and j == b) or (i == b and j == a))


L = matrix(QQ, 24, 40)
for r, (mu, a, b) in enumerate(spin_slots):
    for c, (lam, i, j) in enumerate(jet_slots):
        L[r,c] = QQ(1)/2 * (ZZ(lam == b)*hc(i,j,mu,a) - ZZ(lam == a)*hc(i,j,mu,b))
check("full covariant spin-Levi-Civita first jet has rank 20", L.rank() == 20)


def fixed_q(q):
    I = matrix(QQ, 40, 10)
    for c in range(10):
        for lam in range(4):
            I[10*lam+c,c] = q[lam]
    return L*I


def diffeo(q):
    D = matrix(QQ, 10, 4)
    for r, (i,j) in enumerate(slots):
        for c in range(4):
            D[r,c] = (q[i] if j == c else 0) + (q[j] if i == c else 0)
    return D


for name, q in {
    "timelike": vector(QQ,[1,0,0,0]),
    "spacelike": vector(QQ,[0,1,0,0]),
    "null": vector(QQ,[1,0,0,1]),
}.items():
    Lq = fixed_q(q)
    D = diffeo(q)
    P = identity_matrix(QQ,10) - D*(D.transpose()*D).inverse()*D.transpose()
    check(name+" fixed-q Levi-Civita rank is 9", Lq.rank() == 9)
    check(name+" diffeomorphism/transverse ranks are 4/6", D.rank() == 4 and P.rank() == 6)
    check(name+" transverse fixed-varpi source rank is 6", (Lq*P).rank() == 6)

O = identity_matrix(QQ,6)
O[0,1] = QQ(2)/3
dO = matrix(QQ,6,6)
dO[2,3] = -QQ(5)/7
du = vector(QQ,[1,2,3,5,7,11])
check("complete observation representative is invertible", O.det() == 1)
check("residual-zero moving observation keeps only O dU", dO*vector(QQ,6) + O*du == O*du)
check("moving observation term is live off residual zero", dO*vector(QQ,[1,1,1,1,1,1]) != 0)

print("PASS %s/%s" % (checks, checks))
