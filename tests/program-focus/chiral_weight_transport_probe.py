#!/usr/bin/env python3
"""Exact reduced Clifford controls for the universal written proof, not GU validation.
The Euclidean complex n4/h1/m3 representation tests ordered algebra only;
native n14/m10 source, pairing and domain membership are not inferred from it.
"""
import json
from pathlib import Path
import sympy as s

I=s.I; eye=s.eye(4); zero=s.zeros(4,1)
pa=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)]
g=[s.kronecker_product(pa[0],s.eye(2)),s.kronecker_product(pa[1],s.eye(2)),s.kronecker_product(pa[2],pa[0]),s.kronecker_product(pa[2],pa[1])]
omega=s.simplify(g[0]*g[1]*g[2]*g[3]);P=(eye+omega)/2;M=(eye-omega)/2
# n4 volume squares+1; all gamma are Hermitian in this reduced comparator.
checks={}
def ok(name, condition):
    checks[name]=bool(condition)
    if not condition:raise AssertionError(name)
def simp(x):return s.simplify(x)
def eq(a,b):return simp(a-b)==s.zeros(*a.shape)
def total(xs):return sum(xs,s.zeros(*xs[0].shape))
def gamma(z):return total([g[i]*z[i] for i in range(4)])
def weighted(A,z):return [A*x for x in z]
def q(z,nu):return s.Matrix.vstack(z[0],gamma(z),nu)
def symbol(k,z,nu,A,C,G,E):
    gaz=gamma(weighted(A,z));gcz=gamma(weighted(C,z))
    out=[g[k]*A*z[i]-(gaz if i==k else zero)+g[i]*(C*z[k]-g[k]*gcz)+(nu if i==k else zero) for i in range(4)]
    return out,G*z[k]+g[k]*E*nu
basis=[s.eye(4)[:,j] for j in range(4)]
hidden=[]
for r in [1,2]:
 for psi in basis:
  z=[zero.copy() for _ in range(4)];z[r]=psi;z[3]=-g[3]*g[r]*psi;hidden.append(z)
ok('Clifford relations',all(eq(g[i]*g[j]+g[j]*g[i],(2 if i==j else 0)*eye) for i in range(4) for j in range(4)))
ok('chirality and faithful hidden basis',eq(omega**2,eye) and all(eq(gamma(z),zero) for z in hidden))
A=2*P+3*M; C=5*P+7*M;G=11*P+13*M;E=17*P+19*M
barA=2*M+3*P;barC=5*M+7*P;L=2*A+4*C
K=[I*g[i]+s.Rational(i+1,3)*g[(i+1)%4]*g[(i+2)%4] for i in range(4)]
ok('full-unitary chirality-mixing control',all(eq(k.H,-k) for k in K) and any(not eq(k*omega,omega*k) for k in K))
for j,z in enumerate(hidden):
 outs=[symbol(i,weighted(K[i],z),zero,A,C,G,E) for i in range(4)]
 actual=q([total([o[0][r] for o in outs]) for r in range(4)],total([o[1] for o in outs]))
 S=total([K[r]*z[r] for r in range(1,4)]);R=[total([g[r]*K[i]*z[r] for r in range(1,4)]) for i in range(4)];W=total([g[i]*R[i] for i in range(4)])
 predicted=s.Matrix.vstack(-barA*R[0]+barC*g[0]*(S-W),L*(S-W),G*S)
 ok(f'ordered complete lower rows {j}',eq(actual,predicted))
 if j==0:ok('wrong unswapped coefficient rejected',not eq(actual,s.Matrix.vstack(-A*R[0]+C*g[0]*(S-W),L*(S-W),G*S)))
# Actual wedge C=-A,G=-I. Scalar input SE cannot affect hidden principal data.
C=-A;G=-eye
for j,z in enumerate(hidden):
 out,nu=symbol(0,z,zero,A,C,G,E)
 ok(f'actual wedge principal quotient {j}',eq(q(out,nu),s.zeros(12,1)))
cols=[]
for j in range(20):
 v=s.eye(20)[:,j];out,nu=symbol(0,[v[4*r:4*r+4,:] for r in range(4)],v[16:20,:],A,C,G,E);cols.append(s.Matrix.vstack(*out,nu))
Dt=s.Matrix.hstack(*cols);Dti=Dt.inv()
ok('actual time symbol invertible with asymmetric weights',eq(Dt*Dti,s.eye(20)))
for j,z in enumerate(hidden):
 v=Dti*s.Matrix.vstack(*z,zero);ok(f'inverse time preserves hidden {j}',eq(q([v[4*r:4*r+4,:] for r in range(4)],v[16:20,:]),s.zeros(12,1)))
# Mean curvature along first normal, and all owned density cases.
H=[1,0,0];cH=g[1];L=2*A+4*C;barA=2*M+3*P;barC=-barA
for b in [s.Rational(0),s.Rational(1),s.Rational(2)]:
 v=1-b;cV=v*cH
 # F=iI and U0=i gamma0 are nonzero allowed homogeneous freedoms.
 KK=[s.Rational(1,2)*g[0]*cH+I*g[0]]+[g[r]*cV-(v if r==1 else 0)*eye+I*g[r] for r in range(1,4)]
 ok(f'paired unitary connection b={b}',all(eq(k.H,-k) for k in KK))
 residual=[]
 for z in hidden:
  outs=[symbol(i,weighted(KK[i],z),zero,A,C,G,E) for i in range(4)]
  actual=q([total([o[0][r] for o in outs]) for r in range(4)],total([o[1] for o in outs]))
  w=z[1];Gh=g[0]*w
  LC=s.Matrix.vstack(-barA*Gh-barC*g[0]*w,-L*w,-G*w)
  density=s.Matrix.vstack(zero,zero,G*(b*w))
  residual.append(simp(actual+LC+density))
 ok(f'density exact survivor iff b=H ({b})',all(x==s.zeros(12,1) for x in residual)==(b==1))
# Same copied arrows permit a nonunitary cancellation: changing the actual
# adjoint would change this control. It is not a source solution.
KK=[s.Rational(1,2)*g[0]*cH]+[-s.Rational(1,2)*g[r]*cH+(2 if r==1 else 0)*eye for r in range(1,4)]
ok('nonunitary paired escape is outside U',any(not eq(k.H,-k) for k in KK))
for j,z in enumerate(hidden):
 outs=[symbol(i,weighted(KK[i],z),zero,A,C,G,E) for i in range(4)]
 actual=q([total([o[0][r] for o in outs]) for r in range(4)],total([o[1] for o in outs]))
 w=z[1];LC=s.Matrix.vstack(-barA*g[0]*w-barC*g[0]*w,-L*w,-G*w)
 ok(f'nonunitary copied-arrow positive control {j}',eq(actual+LC,s.zeros(12,1)))
# Nonzero traceless II with h2/m2: H=0, so the particular Spin solution works.
KK=[s.Rational(1,2)*g[0]*g[2],-s.Rational(1,2)*g[1]*g[2],s.zeros(4),s.zeros(4)]
for j,psi in enumerate(basis):
 z=[zero,zero,psi,-g[3]*g[2]*psi]
 outs=[symbol(i,weighted(KK[i],z),zero,A,C,G,E) for i in range(4)]
 oz=[total([o[0][r] for o in outs]) for r in range(4)]
 actual=s.Matrix.vstack(oz[0],oz[1],gamma(oz),total([o[1] for o in outs]))
 LC=s.Matrix.vstack(-barA*g[0]*psi,barA*g[1]*psi,zero,zero)
 ok(f'mean-zero nonzero-traceless-II survivor {j}',eq(actual+LC,s.zeros(16,1)))
# Indefinite coordinate control: eta-on-row and eta-on-column agree only
# with simultaneous form-slot and observation transport.
eta=[1,-1,1,1];gg=[g[0],I*g[1],g[2],g[3]]
FF=s.diag(*[x for sign in eta for x in [sign]*4],1,1,1,1)
for k in range(4):
 raw=s.zeros(20);cov=s.zeros(20)
 for a in range(4):
  for bb in range(4):
   if len({a,k,bb})==3:
    raw[4*a:4*a+4,4*bb:4*bb+4]=eta[a]*gg[a]*gg[k]*gg[bb]*A
    cov[4*a:4*a+4,4*bb:4*bb+4]=eta[bb]*gg[a]*gg[k]*gg[bb]*A
 raw[4*k:4*k+4,16:20]=eye;cov[4*k:4*k+4,16:20]=eta[k]*eye
 raw[16:20,4*k:4*k+4]=-eta[k]*eye;cov[16:20,4*k:4*k+4]=-eye
 raw[16:20,16:20]=gg[k]*E;cov[16:20,16:20]=gg[k]*E
 ok(f'indefinite slot-coordinate identity {k}',eq(FF*raw*FF,cov))
qr=s.zeros(12,20);qc=s.zeros(12,20);qr[0:4,0:4]=eye;qc[0:4,0:4]=eye
qr[8:12,16:20]=eye;qc[8:12,16:20]=eye
for r in range(4):qr[4:8,4*r:4*r+4]=gg[r];qc[4:8,4*r:4*r+4]=eta[r]*gg[r]
ok('observation transported in coordinate identity',eq(qc*FF,qr))
ok('wrong fixed raw gamma-trace rejected',not eq(qr*FF,qr))
# Null-vector evaluation control: complex v=e1+i e2 has zero quadratic norm.
v=[1,I,0];cv=g[1]+I*g[2]
ok('null normal retained',eq(cv*cv,s.zeros(4)))
ok('evaluation faithful at null control',any(not eq(z[1]+I*z[2],zero) for z in hidden))
# Source n14 reciprocal signs stay a separate coefficient convention control.
wp,wm=s.Rational(2),s.Rational(3);lp,lm=s.Rational(11,12)/wm,s.Rational(11,12)/wp
ok('K77 crossed relations',12*wp*lm==11 and 12*wm*lp==11)
ok('K95 sign is not interchangeable',12*wp*(-lm)!=11 and 12*wm*(-lp)!=11)
# Abstract n10 row core, including negative density control.
for w,b in [(2,2),(2,0),(2,3)]:
 S=w-b;WH=-w;WN=-16*S;T=WH+WN
 ok(f'n10 arithmetic consistency {w,b}',(S-T==w)==(b==w))
print(json.dumps({'status':'pass','checks':len(checks),'scope':__doc__,'results':checks},indent=2))
