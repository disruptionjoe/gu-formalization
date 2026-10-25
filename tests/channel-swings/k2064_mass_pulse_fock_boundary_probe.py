"""Independent Pauli overlaps and derivative-based fault discrimination."""
import sympy as s
X=s.Matrix([[0,1],[1,0]]);Z=s.diag(1,-1);I=s.eye(2);zero=s.zeros(2);count=0
for r,a,b in [(s.Rational(3),s.Rational(4),s.Rational(12)),(s.Rational(0),s.Rational(1),s.Rational(2)),(s.Rational(5),s.Rational(12),s.Rational(12))]:
 P=(I+(r*X+a*Z)/s.sqrt(r*r+a*a))/2;Q=(I+(r*X+b*Z)/s.sqrt(r*r+b*b))/2;nu=(1-(r*r+a*b)/s.sqrt((r*r+a*a)*(r*r+b*b)))/2
 assert s.simplify((P-Q)**2-nu*I)==zero;count+=1
r,m,v,a,j=s.symbols('r m v a j',positive=True);E=s.sqrt(r*r+m*m)
def dt(q):return s.diff(q,m)*v+s.diff(q,v)*a+s.diff(q,a)*j
f=-r*v/(2*E**2);g=f/(2*E);h=dt(g)/(2*E)
expected=-r*j/(8*E**4)+r*(10*m*v*a+3*v**3)/(8*E**6)-18*r*m*m*v**3/(8*E**8)
def derivative_test(expr):
 if s.simplify(dt(h)-expr)!=0:raise AssertionError('FAIL second integration derivative')
derivative_test(expected);count+=1
# Independent series, using inverse radius, for the free-sea mismatch.
x,ma,mb=s.symbols('x ma mb',positive=True);nu=(1-(1+ma*mb*x*x)/(s.sqrt(1+ma*ma*x*x)*s.sqrt(1+mb*mb*x*x)))/2
series=s.expand(s.series(nu,x,0,3).removeO()).coeff(x,2)
def UV_test(coef):
 if s.simplify(series-coef)!=0:raise AssertionError('FAIL projection UV coefficient')
UV_test((ma-mb)**2/4);count+=1
# Restore the exact rectangular mixing formula independently with Pauli projectors.
r0=s.Integer(1);mu=s.Integer(1);shift=s.Integer(1);H0=X+Z;H1=X+2*Z;P=(I+H0/s.sqrt(2))/2;U=-s.I*H1/s.sqrt(5);B=(I-P)*U*P
assert s.simplify(B.H*B-P/10)==zero;count+=1
faults=[]
for name,fun in [('missing feedback derivative term',lambda:derivative_test(expected-3*r*v**3/(8*E**6))),('wrong mass cross coefficient',lambda:derivative_test(expected-2*r*m*v*a/(8*E**6))),('wrong final sign',lambda:derivative_test(expected+36*r*m*m*v**3/(8*E**8))),('doubled sea overlap',lambda:UV_test((ma-mb)**2/2)),('wrong equal mass cancellation',lambda:UV_test((ma+mb)**2/4))]:
 try:fun()
 except AssertionError as e:
  assert str(e).startswith('FAIL ');faults.append(name)
 else:raise AssertionError('undetected mathematical fault '+name)
print('PASS',count,'independent Pauli/series/derivative controls; rejected',len(faults),'formula faults:',faults)
