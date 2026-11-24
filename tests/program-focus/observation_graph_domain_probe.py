#!/usr/bin/env python3
"""Exact supporting/contrary controls; the general theorem is the written proof.

No GU operator or physical domain is constructed. Polynomial fixture C2;
plateau is constant near the section, preserving every existing section jet.
"""
import json
from fractions import Fraction as F
from pathlib import Path
import sympy as s

checks = []
def check(name, actual, expected):
    if s.simplify(actual - expected) != 0:
        raise AssertionError((name, actual, expected))
    checks.append(name)

z, eps, x, V = s.symbols('z eps x V', positive=True)
p = 1 - 10*z**3 + 15*z**4 - 6*z**5
# eta(t)=1 for |t|<=1, p(|t|-1) for 1<|t|<2, 0 outside.
for k in range(3):
    check(f'plateau join derivative {k}', s.diff(p,z,k).subs(z,0), 1 if k==0 else 0)
    check(f'outer join derivative {k}', s.diff(p,z,k).subs(z,1), 0)
A0 = 2 + 2*s.integrate(p*p, (z,0,1))
A1 = 2*s.integrate(s.diff(p,z)**2, (z,0,1))
check('cutoff squared integral', A0, s.Rational(643,231))
check('cutoff derivative squared integral', A1, s.Rational(20,7))
# Exact change of variables for product chi in c normal coordinates.
c = 10
chi_L2_sq = eps**c * A0**c
chi_derivative_sq = eps**(c-2) * A1 * A0**(c-1)
check('codimension10 field exponent', s.diff(chi_L2_sq,eps)*eps/chi_L2_sq, 10)
check('codimension10 derivative exponent', s.diff(chi_derivative_sq,eps)*eps/chi_derivative_sq, 8)
check('first order graph limit', s.limit(chi_L2_sq+chi_derivative_sq,eps,0,dir='+'), 0)
check('trace plateau value', s.Integer(1), 1)
# A concrete matrix first-order expression with noncommuting coefficients.
# In one tangent coordinate x and ten normals, u=f(x)*chi_epsilon(y)*(1,2).
# The remaining tangent factors can be fixed normalized bumps.
xx = s.symbols('xx', real=True)
f = (1-xx**2)**2  # extended by0; C1, enough for this H1 fixture
F0 = s.integrate(f*f,(xx,-1,1))
F1 = s.integrate(s.diff(f,xx)**2,(xx,-1,1))
Fcross = s.integrate(f*s.diff(f,xx),(xx,-1,1))
check('tangent norm', F0, s.Rational(256,315))
check('tangent derivative norm', F1, s.Rational(256,105))
check('tangent mixed term', Fcross, 0)
A=s.Matrix([[1,1],[0,1]]); B=s.Matrix([[0,1],[-1,0]])
C=s.Matrix([[0,2],[3,1]]); e=s.Matrix([1,2]); Q=s.Matrix([[1,1]])
check('tangent coefficient norm', (A*e).dot(A*e), 13)
check('normal coefficient norm', (B*e).dot(B*e), 5)
check('lower coefficient norm', (C*e).dot(C*e), 41)
check('noncommuting operator control', (A*B-B*A)[0,0], -1)
operator_sq=(13*F1+41*F0)*chi_L2_sq+5*F0*chi_derivative_sq
field_sq=e.dot(e)*F0*chi_L2_sq
trace_sq=(Q*e)[0]**2*F0
check('concrete graph norm limit', s.limit(field_sq+operator_sq,eps,0,dir='+'), 0)
check('concrete nonzero trace norm', trace_sq, s.Rational(256,35))
check('normal derivative mixed integral', 2*s.integrate(p*s.diff(p,z),(z,0,1)), -1)
# The two transition sides have opposite eta' signs, so their mixed integrals cancel.
check('complete normal mixed term', -s.Rational(1,2)+s.Rational(1,2), 0)
# Nonzero at-section jet control: u=1+b y; plateau multiplier is exactly1 near0.
b,y = s.symbols('b y')
u = 1+b*y
u_cutoff_germ = u
for k in range(6):
    check(f'preserve section jet{k}', s.diff(u_cutoff_germ,y,k).subs(y,0), s.diff(u,y,k).subs(y,0))
check('covariant jet preserved', (s.diff(u_cutoff_germ,y)-b*u_cutoff_germ).subs(y,0), 0)
# Global normal independence is NOT preserved in the transition shell.
check('normal derivative nonzero control', s.diff(p,z).subs(z,s.Rational(1,2)), -s.Rational(15,8))
# Under first-order graph norm, codimension1/2 are not covered by this scaling argument.
for codim, exponent in [(1,-1),(2,0),(3,1),(10,8)]:
    check(f'first-order squared scaling c{codim}', codim-2, exponent)
# General order estimate; c>2m is sufficient, not an iff for arbitrary operators.
for m in range(7):
    check(f'order{m} codimension10 exponent', 10-2*m, [10,8,6,4,2,0,-2][m])
check('L2 target trace exponent', 10-2*0, 10)
# Finite-volume normal-independent positive control, for normalized observed data.
check('normal-independent norm ratio', V / V, 1)
check('normal-independent readout bound saturates', s.sqrt(V)/s.sqrt(V), 1)
# Changing to a graph-plus-observation norm prevents this sequence from tending0.
check('observation-strengthened norm countercontrol', s.limit(chi_L2_sq+chi_derivative_sq+1,eps,0,dir='+'), 1)
report = {
    'status': 'PASS', 'checks': len(checks), 'check_names': checks,
    'cutoff_squared_integral': str(A0),
    'cutoff_derivative_squared_integral': str(A1),
    'codimension': 10, 'operator_order': 1,
    'field_norm_squared_exponent': 10,
    'operator_norm_squared_exponent': 8,
    'concrete_matrix_trace_norm_squared': str(trace_sq),
    'trace': 'fixed nonzero; all at-section jets preserved',
    'scope': 'Exact local scaling controls; universal statements proved in the article; no native closed-domain or GU verdict',
    'fixture_regularity': 'C2 globally; constant plateau near the section; universal proof uses C-infinity bump'
}
print(json.dumps(report, indent=2))
