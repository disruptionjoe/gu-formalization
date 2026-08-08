#!/usr/bin/env sage
"""Independent Sage/QQ replay of the normal mixed-Hessian packet."""

R.<s> = PolynomialRing(QQ)

C0 = matrix(QQ, [[0,1,2],[-2,1,0],[1,-1,1]])
T0 = matrix(QQ, [[1,0,-1],[2,-1,1],[0,1,2]])
L0 = matrix(QQ, [[1,1,0],[0,2,-1],[1,0,1]])
R0 = matrix(QQ, [[2,0,1],[-1,1,0],[0,1,1]])
Cn = matrix(QQ, [[1,-1,0],[0,2,1],[-2,0,1]])
Tn = matrix(QQ, [[0,2,1],[-1,1,0],[2,0,-1]])
Ln = matrix(QQ, [[1,0,-1],[2,-1,1],[0,1,1]])
Rn = matrix(QQ, [[0,1,1],[-1,2,0],[1,0,-1]])
Gn = matrix(QQ, [[2,1,0],[1,-1,1],[0,1,3]])
Hn = matrix(QQ, [[1,-1,0],[-1,2,1],[0,1,-2]])
kappa = QQ(5)/7
rho_n = QQ(2)/5


def path_average(c, t):
    return c*c + (c*t+t*c)/2 + t*t/3


def gradient(functional):
    out = matrix(R, 3, 3)
    for row in range(3):
        for col in range(3):
            unit = matrix(QQ, 3, 3)
            unit[row,col] = 1
            out[col,row] = functional(unit)
    return out


def objects(active):
    C = matrix(R, C0) + (s*matrix(R,Cn) if "C" in active else 0)
    T = matrix(R, T0) + (s*matrix(R,Tn) if "T" in active else 0)
    L = matrix(R, L0) + (s*matrix(R,Ln) if "L" in active else 0)
    RR = matrix(R, R0) + (s*matrix(R,Rn) if "R" in active else 0)
    G = identity_matrix(R,3) + (s*matrix(R,Gn) if "G" in active else 0)
    H = identity_matrix(R,3) + (s*matrix(R,Hn) if "H" in active else 0)
    rho = R(1) + (s*rho_n if "rho" in active else 0)
    P = path_average(C,T)
    S = lambda value: L*value*RR
    def dc(direction):
        d = matrix(R,direction)
        dP = d*C+C*d+(d*T+T*d)/2
        return rho*(T*G*S(dP)).trace()
    def dt(direction):
        d = matrix(R,direction)
        dP = (C*d+d*C)/2+(d*T+T*d)/3
        mass = kappa*(d*H*T+T*H*d).trace()/2
        return rho*(d*G*S(P)+T*G*S(dP)).trace()+mass
    return C,T,rho,G,L,RR,H,P,S,dc,dt,gradient(dc),gradient(dt)


def d0(value):
    return matrix(QQ, value.nrows(), value.ncols(),
                  [entry.derivative(s)(0) for entry in value.list()])


owners = {"C","T","rho","G","L","R","H"}
full = objects(owners)
ECn = d0(full[-2])
ETn = d0(full[-1])
expected_c = matrix(QQ, [[36,QQ(457)/5,50],[QQ(21)/2,-QQ(1)/2,QQ(263)/5],[QQ(351)/10,QQ(406)/5,QQ(447)/10]])
expected_t = matrix(QQ, [[QQ(109)/15,QQ(5849)/105,QQ(788)/35],[QQ(94)/7,QQ(8467)/210,QQ(15361)/210],[QQ(2159)/35,QQ(8833)/105,QQ(6679)/105]])
assert ECn == expected_c
assert ETn == expected_t

parts_c = zero_matrix(QQ,3)
parts_t = zero_matrix(QQ,3)
for owner in sorted(owners):
    partial = objects({owner})
    pc, pt = d0(partial[-2]), d0(partial[-1])
    assert pc != 0 or pt != 0
    parts_c += pc
    parts_t += pt
assert parts_c == ECn and parts_t == ETn

# Direct mixed derivative checks on a held-out direction.
hc = matrix(QQ, [[2,-1,0],[1,0,3],[-2,1,1]])
ht = matrix(QQ, [[0,1,-2],[2,1,0],[1,-1,3]])
assert full[9](hc).derivative(s)(0) == (hc*ECn).trace()
assert full[10](ht).derivative(s)(0) == (ht*ETn).trace()

C,T,rho,G,L,RR,H,P,S = full[:9]
endpoint = (C+T)*(C+T)
upsilon = rho*G*S(endpoint)+kappa*H*T
upsilon_n = d0(upsilon)
assert upsilon_n != ETn and upsilon_n != 0

print("SAGE_QQ_NORMAL_EULER_JET=PASS")
print("E_C_NORMAL_RANK=%s" % ECn.rank())
print("E_T_NORMAL_RANK=%s" % ETn.rank())
print("SEVEN_OWNER_SUM=PASS")
print("MIXED_HESSIAN_HELDOUTS=PASS")
print("PRINTED_RESIDUAL_TRANSFER=REJECTED")
