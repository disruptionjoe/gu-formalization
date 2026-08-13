# Independent Sage/QQ replay of the local epsilon endpoint direct-sum gate.

Q = QQ

# Two continuum endpoint evaluations are independent at tangent/collar grade.
R.<t,eta0,eta3,e0,e2,p0,p2> = PolynomialRing(Q)
eta = (1-t)*eta0 + t*eta3
assert eta(t=0) == eta0
assert eta(t=1) == eta3
assert matrix(Q, [[1,0],[0,1]]).rank() == 2
green = eta3*e2 - eta0*e0
edge = -p0*eta0 + p2*eta3
assert green(e0=p0,e2=p2) == edge

def endpoint_copy(x, p, u):
    PR = PolynomialRing(Q, 12, names=["x%d"%i for i in range(4)] + ["p%d"%i for i in range(4)] + ["u%d"%i for i in range(4)])
    v = PR.gens()
    F = PR.fraction_field()
    X = matrix(F, 2, 2, v[0:4])
    P = matrix(F, 2, 2, v[4:8])
    U = matrix(F, 2, 2, v[8:12])
    outputs = list((X*U.inverse()).list()) + list((P*U.transpose()).list())
    J = matrix(F, [[f.derivative(z) for z in v] for f in outputs])
    vals = list(x.list()) + list(p.list()) + list(u.list())
    ev = {v[i]: vals[i] for i in range(12)}
    J0 = matrix(Q, [[entry.subs(ev) for entry in row] for row in J.rows()])
    Ocan = block_matrix(Q, [[zero_matrix(Q,4), -identity_matrix(Q,4)], [identity_matrix(Q,4), zero_matrix(Q,4)]])
    O = J0.transpose()*Ocan*J0
    cols = []
    for a in range(2):
        for b in range(2):
            E = zero_matrix(Q,2)
            E[a,b] = 1
            cols.append(vector(Q, list((x*E).list()) + list((-p*E.transpose()).list()) + list((u*E).list())))
    G = matrix(Q, 12, 4, lambda i,j: cols[j][i])
    return J0,O,G

x0 = matrix(Q, [[2,1],[1,1]])
p0m = matrix(Q, [[3,-1],[2,4]])
u0 = matrix(Q, [[1,2],[1,3]])
x3 = matrix(Q, [[3,1],[2,1]])
p3m = matrix(Q, [[1,2],[-1,3]])
u3 = matrix(Q, [[2,1],[1,1]])
J0,O0,G0 = endpoint_copy(x0,p0m,u0)
J3,O3,G3 = endpoint_copy(x3,p3m,u3)
J = block_diagonal_matrix(J0,J3)
O = block_diagonal_matrix(O0,-O3)
G = block_diagonal_matrix(G0,G3)
assert J.rank() == 16
assert O.rank() == 16
assert O.right_kernel().dimension() == 8
assert G.rank() == 8
assert O*G == zero_matrix(Q,24,8)

# Scalar one-normal model and tenfold direct sum.
Js = matrix(Q, [[1,0,0,0,-1,0],[0,1,0,0,0,-1],[0,0,1,0,0,0],[0,0,0,1,0,0]])
Or = matrix(Q, [[0,0,-1,0],[0,0,0,1],[1,0,0,0],[0,-1,0,0]])
Os = Js.transpose()*Or*Js
Gs = matrix(Q, [[1,0],[0,1],[0,0],[0,0],[1,0],[0,1]])
assert Os.rank() == 4
assert Os.right_kernel().dimension() == 2
assert Os*Gs == zero_matrix(Q,6,2)
weights = [Q(-5),Q(-4),Q(-3),Q(-2),Q(-1),Q(1),Q(2),Q(3),Q(4),Q(5)]
Oall = block_diagonal_matrix(*[w*Os for w in weights])
assert Oall.nrows() == 60
assert Oall.rank() == 40
assert Oall.right_kernel().dimension() == 20

print("PASS independent Sage/QQ epsilon endpoint direct-sum replay")
