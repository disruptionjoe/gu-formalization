"""Independent integral, geometric-sum, and spectral proof controls for K2001."""
from fractions import Fraction as F
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k2001-geometric-pulse-rank-bounds.json').read_text())
x,y,k,al=s.symbols('x y k al', real=True, nonzero=True)
checks=0
# Integrate actual Gram kernel separately on y<x and y>x, not a sampled sign grid.
def integral(f,beta=None):
    b=al if beta is None else beta
    return s.simplify(s.integrate((b*(1-x+y)+(1-al)*x*y)*f,(y,-1,x))/2+s.integrate((b*(1-y+x)+(1-al)*x*y)*f,(y,x,1))/2)
cos_result=integral(s.cos(k*y));sin_result=integral(s.sin(k*y))
cos_expected=al*(s.cos(k*x)-s.cos(k))/k**2
sin_expected=al*s.sin(k*x)/k**2+x*((1-al)*s.sin(k)-k*s.cos(k))/k**2
assert s.simplify(cos_result-cos_expected)==0;checks+=1
assert s.simplify(sin_result-sin_expected)==0;checks+=1
# Actual ramp sign-product integrates to 1-|x-y|; diagonal trace includes middle.
z=s.symbols('z',real=True)
assert s.simplify((s.integrate(1,(z,-1,x))-s.integrate(1,(z,x,y))+s.integrate(1,(z,y,1)))/2-(1-y+x))==0;checks+=1
assert s.integrate((al+(1-al)*x*x)/2,(x,-1,1))==(1+2*al)/3;checks+=1
# Independent finite sections sum geometric errors, including both triangles.
for n in [2,3,5,9,17,33]:
    rho=F(1,768);kap=F(1,16)
    B=[[F(3,2)*kap*rho**(j-i) if j>=i else F(3,2)*kap*rho**(i-j-1) for j in range(n)] for i in range(n)]
    # Use rational 1/27 upper bound for sqrt(rho); do not import producer helpers.
    E=[[F(1,16)*rho**(n-1-i)*F(1,27)**(n-1-j) if j>=i else F(1,16)*rho**(n-1-j)*F(1,27)**(n-1-i) for j in range(n)] for i in range(n)]
    for M,bound in [(B,F(144,767)),(E,F(27,208))]:
        assert max(map(sum,M))<=bound
        assert max(sum(M[i][j] for i in range(n)) for j in range(n))<=bound;checks+=2
    U=s.Matrix(n,n,lambda i,j:1 if j>=i else 0);V=s.eye(n)
    for i in range(n-1):V[i,i+1]=-1
    assert U*V==s.eye(n);checks+=1
for c in D['certificates']:
    r=c['rank'];rho=F(1,768);a=F(1,4)*rho**(r+1)
    assert F(c['residual_squared_lower_bound'])==4*(F(1,48)/16)**2*a**3
    assert F(c['strong_error_squared_lower_bound'])==4*F(3,10)**2*a*a/48;checks+=2
# Analytic eigenfunction identities for actual alpha and independent rational controls.
for av in [F(1,3),F(3,8),F(1,2),F(1,1)]:
    for n in range(5):
        kv=(s.Rational(1,2)+n)*s.pi
        assert s.simplify(cos_result.subs({al:s.Rational(av.numerator,av.denominator),k:kv})-s.Rational(av.numerator,av.denominator)*s.cos(kv*x)/kv**2)==0;checks+=1
# Genuine corrupted mathematical inputs, baseline already green.
def require_zero(expr):
    if s.simplify(expr)!=0:raise AssertionError('MATHEMATICAL_MISMATCH')
mutants=[('lost ramp measure',lambda:require_zero(integral(s.cos(k*y),2*al)-cos_expected)),('wrong Robin coefficient',lambda:require_zero(sin_result-(al*s.sin(k*x)/k**2+x*((1+al)*s.sin(k)-k*s.cos(k))/k**2))),('normalization factor',lambda:require_zero(2*cos_result-cos_expected)),('incorrect triangular inverse',lambda:require_zero((s.Matrix([[1,1],[0,1]])*s.Matrix([[1,1],[0,1]])-s.eye(2))[0,1]))]
for name,test in mutants:
    try:test()
    except AssertionError as e:
        assert str(e)=='MATHEMATICAL_MISMATCH';print('DETECTED',name)
    else:raise AssertionError('MISSED '+name)
print('PASS K2001 independent:',checks,'exact integral/geometric/inverse controls;',len(mutants),'mathematical mutations')
