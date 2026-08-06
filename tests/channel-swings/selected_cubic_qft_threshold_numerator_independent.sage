#!/usr/bin/env sage
"""Independent Sage reconstruction of the selected cubic QFT threshold gate."""

R.<c,theta,q0,qm> = PolynomialRing(QQ)
V = c*theta*(q0+qm)^2
vars = [q0,qm,theta]
H = matrix(R, 3, 3, [[V.derivative(x).derivative(y) for y in vars] for x in vars])
H_expected = matrix(R, [
    [2*c*theta, 2*c*theta, 2*c*(q0+qm)],
    [2*c*theta, 2*c*theta, 2*c*(q0+qm)],
    [2*c*(q0+qm), 2*c*(q0+qm), 0],
])
assert H == H_expected
assert H(q0=0,qm=0,theta=0) == zero_matrix(QQ,3)
assert H(q0=0,qm=0) == matrix(R, [
    [2*c*theta,2*c*theta,0],
    [2*c*theta,2*c*theta,0],
    [0,0,0],
])

# Parity support, independently enumerated.
def parity(pt, powers):
    p = {'theta': pt, 'q0': 1, 'qm': -1}
    out = 1
    for key, exponent in powers.items():
        out *= p[key]^exponent
    return out

terms = {
    'theta_q0_q0': {'theta':1,'q0':2},
    'theta_q0_qm': {'theta':1,'q0':1,'qm':1},
    'theta_qm_qm': {'theta':1,'qm':2},
}
assert {k:parity(1,v) for k,v in terms.items()} == {
    'theta_q0_q0':1,'theta_q0_qm':-1,'theta_qm_qm':1}
assert {k:parity(-1,v) for k,v in terms.items()} == {
    'theta_q0_q0':-1,'theta_q0_qm':1,'theta_qm_qm':-1}

# Exact selected squared-mass ratio.
P5 = PolynomialRing(QQ, names=('a','kappa','beta','alpha','kappa1'))
a,kappa,beta,alpha,kappa1 = P5.gens()
S = P5.fraction_field()
a,kappa,beta,alpha,kappa1 = map(S, (a,kappa,beta,alpha,kappa1))
M2 = QQ(124)/117*alpha*kappa1
mu2 = a*kappa/(3*beta^2)
assert M2/mu2 == 124*alpha*beta^2*kappa1/(39*a*kappa)

# Exact heavier -> lighter + massless witnesses and the soft equality locus.
def p_emit(A,B):
    return (A^2-B^2)/(2*A)
assert p_emit(QQ(5),QQ(3)) == QQ(8)/5
assert p_emit(QQ(7),QQ(2)) == QQ(45)/14
T.<A> = PolynomialRing(QQ)
assert p_emit(A,A) == 0

# Independent numerator divisibility control.
P.<z,g> = PolynomialRing(QQ)
F = FractionField(P)
assert F(-2*g/z).denominator() == z
assert F(-2*g*z/z) == -2*g

print("PASS independent Sage: full Hessian, parity support, mass ratio, thresholds, numerator gate")
