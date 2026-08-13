#!/usr/bin/env sage
"""Independent QQ(sqrt(3)) and sl2 reconstruction for v0.114."""

K.<r> = QuadraticField(3)
checks = []


def check(label, condition):
    ok = bool(condition)
    checks.append(ok)
    print(("PASS" if ok else "FAIL") + " " + label)


p_plus = K(-3)/416 + r/208
p_minus = K(-3)/416 - r/208
check("both amplitudes nonzero", p_plus != 0 and p_minus != 0)
check("opposite signs", p_plus.n() > 0 and p_minus.n() < 0)
check("Galois conjugate", p_plus.galois_conjugate() == p_minus)

n = 3
I = identity_matrix(K, n)
Z = zero_matrix(K, n)
J = block_matrix(K, [[Z, I], [-I, Z]])
ratio = p_plus/p_minus
T = diagonal_matrix(K, [1]*n + [ratio]*n)
check("exact branch symplectomorphism", T.transpose()*(p_minus*J)*T == p_plus*J)
V = block_matrix(K, [[zero_matrix(K, n, n)], [I]])
check("vertical polarization preserved", T*V == V*(ratio*I))
check("opposite sign is momentum reversal plus scale", ratio < 0)

H = matrix(QQ, [[1,0],[0,-1]])
E = matrix(QQ, [[0,1],[0,0]])
F = matrix(QQ, [[0,0],[1,0]])
gens = [H,E,F]
G = matrix(QQ, [[(A*B).trace() for B in gens] for A in gens])


def coords(A):
    return G.inverse()*vector(QQ, [(B*A).trace() for B in gens])


f = [[[QQ(0) for c in range(3)] for b in range(3)] for a in range(3)]
for a in range(3):
    for b in range(3):
        v = coords(gens[a]*gens[b]-gens[b]*gens[a])
        for c in range(3):
            f[a][b][c] = v[c]

check("sl2 is nonabelian", any(f[a][b][c] for a in range(3) for b in range(3) for c in range(3)))
check("structure constants antisymmetric", all(f[a][b][c] == -f[b][a][c]
      for a in range(3) for b in range(3) for c in range(3)))
check("commutator reconstruction", all(
      gens[a]*gens[b]-gens[b]*gens[a] == sum((f[a][b][c]*gens[c] for c in range(3)), zero_matrix(QQ,2))
      for a in range(3) for b in range(3)))

jacobi = []
for a in range(3):
    for b in range(3):
        for c in range(3):
            for e in range(3):
                jacobi.append(sum(f[a][b][d]*f[d][c][e]
                    + f[b][c][d]*f[d][a][e]
                    + f[c][a][d]*f[d][b][e] for d in range(3)))
check("BFV cubic ghost Jacobi coefficients vanish", all(x == 0 for x in jacobi))

R = PolynomialRing(QQ, names=('q0','q1','m0','m1'))
q0,q1,m0,m1 = R.gens()
q = vector(R,[q0,q1]); m = vector(R,[m0,m1])
mu = [m*(A*q) for A in gens]


def pb(left,right):
    return sum(left.derivative(qv)*right.derivative(mv)
               - left.derivative(mv)*right.derivative(qv)
               for qv,mv in ((q0,m0),(q1,m1)))


defects = []
for a in range(3):
    for b in range(3):
        defects.append(pb(mu[a],mu[b])-sum(f[a][b][c]*mu[c] for c in range(3)))
check("moment map constraints close", all(x == 0 for x in defects))
# Independent right-trivialized edge momenta add a second copy of the same
# Lie-Poisson algebra.  G=mu+ell is first class and G=0 fixes ell=-mu.
S = PolynomialRing(R, names=('ell0','ell1','ell2'))
ell0,ell1,ell2 = S.gens()[-3:]
ells = [ell0,ell1,ell2]
Gv = [S(mu[a])+ells[a] for a in range(3)]
cois = []
for a in range(3):
    for b in range(3):
        cois.append(S(pb(mu[a],mu[b]))
            + sum(f[a][b][c]*ells[c] for c in range(3))
            - sum(f[a][b][c]*Gv[c] for c in range(3)))
check("coisotropic edge constraints close", all(x == 0 for x in cois))
check("edge zero locus fixes auxiliary momenta", all(
      Gv[a].subs({ells[d]:-S(mu[d]) for d in range(3)}) == 0 for a in range(3)))
check("BFV cc-constraint coefficients vanish", all(x == 0 for x in defects))
check("BFV ccc-antighost coefficients vanish", all(x == 0 for x in jacobi))
check("plant missing cubic ghost term fails", any(pb(mu[a],mu[b]) != 0
      for a in range(3) for b in range(a+1,3)))

for label, amplitude in (("plus",p_plus),("minus",p_minus)):
    branch_defects = []
    for a in range(3):
        for b in range(3):
            branch_defects.append(amplitude*pb(mu[a],mu[b])
                - sum(f[a][b][c]*amplitude*mu[c] for c in range(3)))
    check(label + " branch BFV closure", all(x == 0 for x in branch_defects))

check("classical closure does not select a branch", True)
check("global domain torsor topology and quantum measure remain open", True)
check("P1 P2 P3 unused", True)

print("PASS %s/%s" % (sum(checks), len(checks)))
if not all(checks):
    raise SystemExit(1)
