"""Separate Pauli/derivative checks and actual formula corruptions, not theorem assertions."""
import sympy as s
X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1);I=s.eye(2);zero=s.zeros(2)
r,m,v=s.symbols('r m v',positive=True);E=s.sqrt(r*r+m*m);P=(I+(r*X+m*Z)/E)/2;pd=s.diff(P,m)*v
K=-v*r*Y/(2*E**2)
def check_tracking(K):
 if s.simplify(K*P-P*K-s.I*pd)!=zero:raise AssertionError('FAIL tracking equation')
def check_tail(tail):
 R=s.symbols('R',positive=True)
 if s.simplify(s.diff(tail,R)+s.exp(-m*R)*(m*R+1))!=0:raise AssertionError('FAIL radial tail')
check_tracking(K)
assert s.simplify(K*K-v*v*r*r/(4*E**4)*I)==zero
assert s.simplify(s.diff(P,m)- (r*r*Z-m*r*X)/(2*E**3))==zero
# A rotation gives the same correction independently of the commutator construction.
t=s.symbols('t',real=True);Rot=s.cos(t/2)*I-s.I*s.sin(t/2)*Y
assert s.simplify(Rot*Z*Rot.H-s.cos(t)*Z-s.sin(t)*X)==zero
assert s.simplify(s.I*s.diff(Rot,t)*Rot.H-Y/2)==zero
assert s.simplify(s.diff(s.atan(r/m),m)+r/(m*m+r*r))==0
R=s.symbols('R',positive=True);tail=s.exp(-m*R)*(R+2/m);check_tail(tail)
# Verify the derivative entering the uniform adiabatic estimate with independent chain rule.
a=s.symbols('a',real=True);g=-r*v/(4*E**3);dg=s.diff(g,m)*v+s.diff(g,v)*a
assert s.simplify(dg-(-r*a/(4*E**3)+3*r*m*v*v/(4*E**5)))==0
faults=[]
for name,fn in [('wrong sign',lambda:check_tracking(-K)),('missing half',lambda:check_tracking(2*K)),('wrong denominator',lambda:check_tracking(-v*r*Y/(2*E))),('missing second tail term',lambda:check_tail(s.exp(-m*R)*(R+1/m)))]:
 try:fn()
 except AssertionError as e:
  assert str(e).startswith('FAIL ');faults.append(name)
 else:raise AssertionError('undetected mathematical fault '+name)
print('PASS 8 exact Pauli/derivative controls; rejected',len(faults),'formula faults:',faults)
