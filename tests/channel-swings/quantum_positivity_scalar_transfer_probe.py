#!/usr/bin/env python3
"""Exact transfer diagnostics for arXiv:2608.12210v1; no GU bridge asserted.

Checks coefficient matching, momentum conservation, the displayed auxiliary
elimination, and a counterexample to inferring sector closure from pullback.
It performs no loop integral and writes no files.
"""

import json

import sympy as sp


def certify():
    passed = []

    def check(label, condition):
        if not bool(condition):
            raise AssertionError(label)
        passed.append(label)

    def zero(expr):
        return sp.simplify(expr) == 0

    a = sp.symbols("a", real=True, nonzero=True)
    b, c, Q, X, lam, l3, l4 = sp.symbols("b c Q X lambda lambda3 lambda4", real=True)
    action = a*Q**2 + b*Q*X + c*X**2
    residue = sp.expand(action - a*(Q+b*X/(2*a))**2)
    check("complete square residue equals discriminant", zero(residue-(4*a*c-b*b)*X*X/(4*a)))
    normalized = action.subs({a: -sp.Rational(1, 2), b: l3, c: l4})
    ps = normalized.subs({l3: -lam, l4: -lam*lam/2})
    check("paper perfect-square normalization", zero(ps+(Q+lam*X)**2/2))
    check("off-relation quartic term is retained", zero(residue.subs({a: -sp.Rational(1, 2), b: -lam, c: -lam*lam/2+1})-X*X))
    beta3, beta4 = sp.symbols("beta3 beta4", real=True)
    flow = beta3*sp.diff(l4+l3*l3/2, l3)+beta4*sp.diff(l4+l3*l3/2, l4)
    check("RG relation requires tangency", flow == beta4+l3*beta3)

    # Invariants p^2=P, q^2=R, p.q=S; p3=-p-q. No signature assumed.
    P, R, S, eps = sp.symbols("P R S epsilon", real=True)
    V3 = S*(P+R+2*S)+(-P-S)*R+(-R-S)*P
    check("momentum-conserving cubic Gram cancellation", zero(V3-2*(S*S-P*R)))
    check("a soft cubic leg starts at quadratic order", zero(V3.subs({P: eps*eps*P, S: eps*S}, simultaneous=True)-eps*eps*V3))

    # The auxiliary field is algebraic after integration by parts. g,Omega != 0.
    g, omega = sp.symbols("g Omega", real=True, nonzero=True)
    upsilon, box_omega = sp.symbols("Upsilon BoxOmega", real=True)
    auxiliary = -upsilon*box_omega-g*omega*omega*upsilon*upsilon/6
    stationary = sp.solve(sp.diff(auxiliary, upsilon), upsilon)
    check("auxiliary equation has stated unique solution", stationary == [-3*box_omega/(g*omega*omega)])
    effective = sp.simplify(auxiliary.subs(upsilon, stationary[0]))
    check("elimination yields three over two g", zero(effective-3*box_omega*box_omega/(2*g*omega*omega)))
    printed = box_omega*box_omega/(2*g*omega*omega)
    check("displayed coefficient differs by exactly factor three", zero(effective-3*printed))
    # Box(exp(lambda*sigma))/exp(lambda*sigma)=lambda*(Q+lambda*X).
    # This auxiliary substitution is restricted to lambda != 0, since g != 0.
    reduced = effective.subs(box_omega, omega*lam*(Q+lam*X)).subs(g, -3*lam*lam)
    check("derived normalization matches the scalar action", zero(reduced-ps))
    reduced_printed = printed.subs(box_omega, omega*lam*(Q+lam*X)).subs(g, -3*lam*lam)
    check("printed normalization gives one third of scalar action", zero(3*reduced_printed-ps))

    # A finite-dimensional potential control demonstrates precisely why a
    # restricted action says nothing about the omitted normal equation.
    # Q,X are independent jet placeholders here, not fields being varied.
    z, h = sp.symbols("z h", real=True)
    parent = ps+z*h+z*z/2
    check("restricted action can pass coefficient matching", zero(parent.subs(z, 0)-ps))
    check("same restricted action can have a nonzero normal equation", sp.diff(parent, z).subs(z, 0) == h)
    check("closure control vanishes only with its extra condition", sp.diff(parent, z).subs({z: 0, h: 0}) == 0)

    return {
        "result_id": "QUANTUM-POSITIVITY-SCALAR-TRANSFER",
        "source": "arXiv:2608.12210v1",
        "checks_passed": len(passed),
        "checks": passed,
        "sympy_version": sp.__version__,
        "assumptions": "a!=0; auxiliary elimination g!=0 and Omega!=0; auxiliary exponential substitution lambda!=0; polynomial PS identity also valid at lambda=0",
        "claim_ceiling": "exact displayed-equation diagnostics and a finite-dimensional closure countercontrol; no loop calculation or native GU sector constructed",
    }


if __name__ == "__main__":
    print(json.dumps(certify(), indent=2))
