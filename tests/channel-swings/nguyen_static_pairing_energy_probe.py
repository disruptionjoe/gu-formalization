#!/usr/bin/env python3
"""Exact static symmetrizer and wave-energy calculation for the K117 horn.

This is a calculation on the declared observed two-field model, not a
construction of native I1B, a GU physical quotient, or loop positivity.
No files are written. The bounded-profile argument is proved in the linked
research note; finite checks here certify its algebraic ingredients.
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
        if isinstance(expr, sp.MatrixBase):
            return all(sp.simplify(entry) == 0 for entry in expr)
        return sp.simplify(expr) == 0

    r, r1, r2 = sp.symbols("r r1 r2", real=True)
    b, c, scale = sp.symbols("b c scale", positive=True)
    beta = sp.symbols("beta", real=True)
    K = sp.Matrix([[r, 1], [1, 0]])
    mass = sp.diag(0, b)
    B = K.inv() * K.diff(r) * r1
    U = -K.inv() * mass

    def dx(expr):
        return expr.diff(r) * r1 + expr.diff(r1) * r2

    # D = -I d_x^2 - B d_x + U. These are coefficients of WD-D^dagger W.
    def adjoint_defects(W):
        first = 2 * dx(W) - B.T * W - W * B
        zeroth = W * U - U.T * W + dx(dx(W)) - dx(B.T * W)
        return sp.simplify(first), sp.simplify(zeroth)

    check("kinetic form stays nonsingular even at r=0", K.det() == -1)
    check("literal first derivative coefficient", B == sp.Matrix([[0, 0], [r1, 0]]))
    check("stable constant-background sign is explicit", U == sp.Matrix([[0, -b], [0, b * r]]))

    # Solve the complete first-order compatibility system, including complex W.
    x, y, z, w = sp.symbols("x y z w", real=True)
    xp, yp, zp, wp = sp.symbols("xp yp zp wp", real=True)
    Wg = sp.Matrix([[x, y + sp.I*z], [y - sp.I*z, w]])
    Wgp = sp.Matrix([[xp, yp + sp.I*zp], [yp - sp.I*zp, wp]])
    equations = 2 * Wgp - B.T * Wg - Wg * B
    solution = sp.solve(list(equations), [xp, yp, zp, wp], dict=True)
    check("complete Hermitian transport system solved", solution == [{xp: r1*y, yp: r1*w/2, zp: 0, wp: 0}])

    a, d, e, f = sp.symbols("a d e f", real=True)
    Wgeneral = sp.Matrix([[a + d*r + e*r*r/4, d + e*r/2 + sp.I*f],
                          [d + e*r/2 - sp.I*f, e]])
    first, zeroth = adjoint_defects(Wgeneral)
    check("integrated four-constant family obeys transport", zero(first))
    check("mass equation forces imaginary part to vanish", zeroth[1, 1] == 2*sp.I*b*f)
    check("general determinant independent of profile", sp.expand(Wgeneral.det()) == a*e-d*d-f*f)
    expected = -a*b + b*e*r*r/4 - e*r2/2
    check("remaining compatibility equation computed", zero(zeroth[0, 1].subs(f, 0) - expected))

    W = scale * sp.Matrix([[c*c + beta*r + r*r/4, beta + r/2],
                           [beta + r/2, 1]])
    profile_ode = b * (r*r - 4*c*c) / 2
    first, zeroth = adjoint_defects(W)
    check("positive-family determinant", zero(W.det() - scale**2 * (c*c-beta*beta)))
    check("positive-family lower minor", W[1, 1] == scale)
    check("profile equation is sufficient for full formal symmetry", zero(first) and zero(zeroth.subs(r2, profile_ode)))
    check("profile equation is necessary in positive family", zero(zeroth[0, 1] - scale*(profile_ode-r2)/2))
    check("changing beta does not repair a bad profile", zero(zeroth.diff(beta)))

    # A non-profile r(x)=1+x violates the full operator identity.
    bad = zeroth.subs({b: 1, c: 1, scale: 1, beta: 0, r: 1, r1: 1, r2: 0})
    check("planted arbitrary moving profile rejected", bad != sp.zeros(2))

    # beta=0, scale=1 suffices whenever any positive member exists.
    F = sp.Matrix([[c, 0], [r/2, 1]])
    inverse = F.inv()
    check("explicit positive factorization", zero(F.T * F - W.subs({scale: 1, beta: 0})))
    transformed_first = F * (-2*dx(inverse) - B*inverse)
    potential = sp.simplify(F * (-dx(dx(inverse)) - B*dx(inverse) + U*inverse))
    check("similarity removes the first derivative", zero(transformed_first))
    expected_potential = sp.Matrix([[b*r/2, -b*c], [-b*c, b*r/2]])
    check("on-profile matrix potential is symmetric", zero(potential.subs(r2, profile_ode)-expected_potential))
    O = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
    diagonal = sp.diag(b*(r/2-c), b*(r/2+c))
    check("constant rotation separates both scalar channels", zero(O.T*expected_potential*O-diagonal))
    channel_weight = sp.simplify(O.T*inverse.T*W*inverse*O)
    check("every positive pairing gives constant positive channel weights", zero(channel_weight-scale*sp.diag(1+beta/c, 1-beta/c)))
    check("positive constant background has nonnegative potentials", diagonal.subs(r, 2*c) == sp.diag(0, 2*b*c))
    check("negative constant background has negative first potential", diagonal.subs(r, -2*c) == sp.diag(-2*b*c, 0))

    energy_integral = r1*r1/2 - b*r**3/6 + 2*b*c*c*r
    check("profile first integral", zero(dx(energy_integral).subs(r2, profile_ode)))

    # Soliton and bound states verified symbolically, without numerical spectra.
    q = sp.symbols("q", real=True)
    k = sp.symbols("k", positive=True)
    rho = 2*c - 6*c/sp.cosh(q)**2
    check("nonconstant exact profile", zero((k*k*sp.diff(rho, q, 2) - b*(rho*rho-4*c*c)/2).subs(b, 2*k*k/c)))
    Vm = sp.simplify((b*(rho/2-c)).subs(b, 2*k*k/c))
    Vp = sp.simplify((b*(rho/2+c)).subs(b, 2*k*k/c))
    check("soliton attractive channel", zero(Vm + 6*k*k/sp.cosh(q)**2))
    check("soliton second channel offset", zero(Vp-Vm-4*k*k))
    ground = 1/sp.cosh(q)**2
    excited = sp.sinh(q)/sp.cosh(q)**2
    for label, psi, ev in [("even", ground, -4*k*k), ("odd", excited, -k*k)]:
        residual = -k*k*sp.diff(psi, q, 2) + Vm*psi - ev*psi
        check(f"exact {label} negative eigenmode", zero(residual))
        check(f"{label} eigenmode decays at both infinities", sp.limit(psi, q, sp.oo) == 0 and sp.limit(psi, q, -sp.oo) == 0)
        check(f"{label} mode is not identically zero", psi.subs(q, 1) != 0)
    check("second channel zero mode", zero(-k*k*sp.diff(ground, q, 2)+Vp*ground))
    check("second channel positive bound mode", zero(-k*k*sp.diff(excited, q, 2)+Vp*excited-3*k*k*excited))

    # A growing wave eigenmode excludes a positive stationary phase-space metric.
    gamma = sp.symbols("gamma", positive=True)
    generator = sp.Matrix([[0, 1], [gamma*gamma, 0]])
    growing = sp.Matrix([1, gamma])
    check("wave growth eigenvalue", generator*growing == gamma*growing)
    m, n, p, ell = sp.symbols("m n p ell", real=True)
    G = sp.Matrix([[m, n+sp.I*ell], [n-sp.I*ell, p]])
    solutions = sp.solve(list(generator.T*G+G*generator), [m, n], dict=True)
    check("all Hermitian phase metrics on the unstable mode solved", solutions == [{m: -gamma*gamma*p, n: 0}])
    check("nondegenerate conserved phase metric is indefinite", zero(G.subs(solutions[0]).det()+gamma*gamma*p*p+ell*ell))
    norm = (growing.T*G*growing)[0]
    check("positive complex phase metrics excluded by growth identity", zero((growing.T*(generator.T*G+G*generator)*growing)[0]-2*gamma*norm))

    # The variational cutoff argument has derivative cost 2/L. Its fixed
    # negative potential contribution -delta beats this at L=4/delta.
    delta = sp.symbols("delta", positive=True)
    check("attractive-channel cutoff bound is strictly negative", sp.simplify(2/(4/delta)-delta) == -delta/2)

    return {
        "result_id": "NGUYEN-STATIC-PAIRING-ENERGY",
        "checks_passed": len(passed),
        "checks": passed,
        "sympy_version": sp.__version__,
        "claim_ceiling": "exact algebra plus analytically proved bounded-profile theorem for the declared static observed two-field model",
        "native_i1b_bridge": "NOT_CONSTRUCTED",
        "physical_gu_positivity": "NOT_ESTABLISHED",
        "profile_equation": "r''=b*(r^2-4*c^2)/2",
        "soliton_negative_eigenvalues": ["-4*k^2", "-k^2"],
        "scope": "b,c>0; whole spatial line; bounded smooth static r; unconstrained two-field wave equation; multiplication symmetrizers",
    }


if __name__ == "__main__":
    print(json.dumps(certify(), indent=2))
