#!/usr/bin/env python3
"""Exact algebra only; variational/domain proof is in the K1850 note."""
from pathlib import Path
import hashlib
import json
import sympy as s

R = Path(__file__).resolve().parents[2]
path = R / 'lab/process/k1850-metric-screening-ensembles.json'
r = json.loads(path.read_text())
checks = {}
def ck(label, value):
    assert bool(value), label
    checks[label] = True

def zero(expr):
    return s.factor(expr) == 0

l, rho, C, v, f, alpha, beta, A, dl, dA = s.symbols(
    'l rho C v f alpha beta A dl dA', real=True)
K, c, Phi, x = s.symbols('K c Phi x', positive=True)
coef = {k: s.Rational(q) for k, q in r['action_coefficients'].items()}
L = coef['matter_vacuum']*rho*v + coef['multiplier']*l*v + coef['top_form']*(alpha*l+beta)*f
ck('matter vacuum volume sign', s.diff(L, rho) == -v)
ck('multiplier Euler volume sign', s.diff(L, l) == -v+alpha*f)
ck('metric volume derivative', s.diff(L, v) == -(rho+l))
shifted = L.subs({rho: rho+C, l: l-C}, simultaneous=True)
ck('affine full action shift', zero(shifted-L+alpha*C*f))
ck('affine shifted multiplier equation', zero(s.diff(shifted-L, l)))
ck('affine shifted metric equation', zero(s.diff(shifted-L, v)))
ck('nonzero affine slope fixture', s.Rational(r['affine']['alpha']) != 0)
ck('action flux coefficient fixture', s.Rational(r['affine']['shift_action_flux_factor']) == -s.Rational(r['affine']['alpha']))
# Nonlinear countercontrol: multiplier derivative of the shift is -C F.
L2 = -(rho+l)*v + l*l*f/2
D2 = s.expand(L2.subs({rho: rho+C, l: l-C}, simultaneous=True)-L2)
ck('nonlinear action shift', zero(D2-(-l*C+C*C/2)*f))
ck('nonlinear multiplier response', s.diff(D2,l) == -C*f)
ck('nonlinear auxiliary mismatch', s.expand((l-C)*f-l*f) == -C*f)
# Classification differential condition and a discrete-only periodic control.
a0,a1,a2,a3=s.symbols('a0 a1 a2 a3')
sigma=a0+a1*l+a2*l*l+a3*l**3
translation=s.Poly(s.expand(s.diff(sigma,l).subs(l,l-C)-s.diff(sigma,l)),l,C)
ck('polynomial all shift classification', s.solve(translation.coeffs(),(a2,a3),dict=True)==[{a2:0,a3:0}])
ck('isolated shift periodic control', s.simplify((2+s.cos(l-2*s.pi))-(2+s.cos(l)))==0)
ck('periodic control not affine', s.diff(2+s.cos(l),l)!=0)
# Boundary variation of -sigma(lambda) A cancels sigma delta A.
boundary=(alpha*l+beta)*dA+s.diff(-(alpha*l+beta)*A,A)*dA+s.diff(-(alpha*l+beta)*A,l)*dl
ck('Legendre boundary term', s.expand(boundary)==-alpha*A*dl)
ck('fixed multiplier does not admit shift', (l-C)-l == -C)
dim=r['geometry']['dimension'];ric=s.Rational(r['geometry']['ricci_factor']);scalar=s.Rational(r['geometry']['scalar_factor'])
ck('four dimensional trace', dim==4 and scalar==dim*ric)
ck('round sphere Einstein factor', ric-scalar/2 == -3)
ck('constant curvature vacuum trace', zero(scalar/x-4*(3*K/x)/K))
ck('fixed lambda curvature derivative', s.diff(4*(l+rho)/K,rho)==4/K)
ck('sphere volume coefficient', s.sympify(r['geometry']['sphere_volume_factor'])==8*s.pi**2/3)
# Affine sphere, parameterized by its exact volume relation.
flux_aff=c*x*x/alpha
lambda_aff=3*K/x-rho
ck('affine sphere volume equation', zero(c*x*x-alpha*flux_aff))
ck('affine sphere metric equation', zero(lambda_aff+rho-3*K/x))
ck('affine sphere shift leaves metric equation', zero((lambda_aff-C)+(rho+C)-3*K/x))
ck('affine radius inversion', zero((alpha*flux_aff/c)-x*x))
# Nonlinear sphere: implicit equation and its differentiated response.
q=rho*x+(c/Phi)*x**3-3*K
slope=-x/(rho+3*c*x*x/Phi)
curvature_slope=12/(x*(rho+3*c*x*x/Phi))
ck('nonlinear implicit differentiation', zero(s.diff(q,rho)+s.diff(q,x)*slope))
ck('nonlinear curvature chain rule', zero(s.diff(12/x,x)*slope-curvature_slope))
ck('nonlinear monotonic polynomial derivative', s.diff(q,x)==rho+3*c*x*x/Phi)
ck('nonlinear positive derivative at nonnegative rho', s.diff(q,x).subs(rho,0).is_positive)
rc={k:s.Rational(q) for k,q in r['rational_control'].items()}
subs={x:rc['s'],c:rc['c'],K:rc['K'],rho:rc['rho'],Phi:rc['nonlinear_flux']}
ck('rational nonlinear stationary equation', q.subs(subs)==0)
ck('rational nonlinear multiplier', rc['lambda']==rc['c']*rc['s']**2/rc['nonlinear_flux'])
ck('rational nonlinear radius response', slope.subs(subs)==rc['nonlinear_ds_drho'])
ck('rational nonlinear curvature response', curvature_slope.subs(subs)==rc['nonlinear_dR_drho'])
ck('rational affine volume fixture', rc['c']*rc['s']**2==s.Rational(r['affine']['alpha'])*rc['affine_flux'])
ck('rational Einstein vacuum fixture', rc['lambda']+rc['rho']==3*rc['K']/rc['s'])
for dep in r['dependencies']:
    ck('dependency '+dep['path'],hashlib.sha256((R/dep['path']).read_bytes()).hexdigest()==dep['sha256'])
r['exact_algebra_checks']=checks
path.write_text(json.dumps(r,indent=2)+'\n')
print('K1850 exact algebra groups',len(checks))
