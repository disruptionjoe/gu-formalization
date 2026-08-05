#!/usr/bin/env sage
"""Independent exact Sage certificate for the pole split and nonlinear branches."""

R.<z, kappa, alpha, h, v, tau> = PolynomialRing(QQ)
J = matrix(R, [[alpha*z, z], [z, kappa]])
assert J.det() == z*(alpha*kappa-z)
assert J.adjugate()[0, 0] == kappa

# Schur elimination at polynomial level.
assert alpha*z - z^2/kappa - z*(alpha*kappa-z)/kappa == 0

S.<a> = PolynomialRing(QQ)
p = a^4 - 2*a^3 + 2*a^2 - 6*a + 1
assert gcd(p, p.derivative()) == 1
assert len(p.roots(AA, multiplicities=False)) == 2
roots = sorted(p.roots(AA, multiplicities=False))
assert QQ(1)/6 < roots[0] < QQ(1)/5
assert QQ(2) < roots[1] < QQ(9)/4

F.<x, y, q> = PolynomialRing(QQ)
action = 2*(x*y*q + x*y + x*q + x + y*q + y + q) + x^2/2 - y^2/2 + q^2
grad = vector(F, [action.derivative(u) for u in (x, y, q)])
H = matrix(F, [[grad[i].derivative(u) for u in (x, y, q)] for i in range(3)])
assert H.is_symmetric()
assert H[0,0] == 1 and H[1,1] == -1
assert grad(x=0, y=0, q=-1) == vector(QQ, [0,0,0])

# Elimination certificate: a=2(q+1), and p(a)=0 gives both nonabelian roots.
K = FractionField(S)
xa = -a*(1+a)/(1+a^2)
ya = a*(1-a)/(1+a^2)
qa = a/2 - 1
for expression in grad[:2]:
    assert K(expression(x=xa, y=ya, q=qa)) == 0
assert K(grad[2](x=xa, y=ya, q=qa)) == K(a*p/(1+a^2)^2)
cubic_num = S((xa*ya*qa).numerator())
assert p.resultant(cubic_num) == 9

det_branch = K(H.det()(x=xa, y=ya, q=qa))
num = S(det_branch.numerator())
assert p.resultant(num) == -5439488

print("PASS independent Sage/AA certificate")
print("TT_DETERMINANT=z*(alpha*kappa-z)")
print("QUARTIC_REAL_ROOTS=2")
print("NONABELIAN_BRANCHES=2")
print("HESSIAN=NONDEGENERATE_INDEFINITE")
