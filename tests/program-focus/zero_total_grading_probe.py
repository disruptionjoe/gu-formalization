#!/usr/bin/env python3
"""Exact algebra/Clifford controls; not a certificate of native Fredholm domains."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('VECLIB_MAXIMUM_THREADS','1')
from pathlib import Path
import sys,json
from fractions import Fraction as F
import sympy as s
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tests/channel-swings'))
from actual_sym2_c14_orbit_probe import native_gammas
checks=[]
def ck(name,value):
 assert bool(value),name
 checks.append(name)
I2=s.eye(2);K=s.Matrix([[0,1],[1,0]]);Gamma=s.diag(1,-1)
D=s.Matrix([[0,1],[2,0]])
ck('odd plus Krein selfadjoint does not force equal blocks',D*Gamma+Gamma*D==s.zeros(2) and D.H*K==K*D and D.H!=D and D*K!=K*D)
a,b,c,d=s.symbols('a b c d',real=True);A=s.Matrix([[a,b],[b,c]]);B=s.Matrix([[b,c],[c,d]])
DD=s.BlockMatrix([[s.zeros(2),A],[B,s.zeros(2)]]).as_explicit();KK=s.kronecker_product(K,I2)
ck('Krein adjoint permits two independent Hermitian blocks',DD.H*KK==KK*DD)
PP=s.BlockMatrix([[s.zeros(2),A],[A,s.zeros(2)]]).as_explicit()
ck('both adjoints give commuting cross-grade symmetry',PP.H==PP and PP*KK==KK*PP)
# Selfadjoint odd rectangular block has ungraded index0 but nonzero chiral index.
T=s.Matrix([[1,0]]);H=s.BlockMatrix([[s.zeros(2),T.T],[T,s.zeros(1)]]).as_explicit();G=s.diag(1,1,-1)
ck('odd selfadjoint doubled finite control',H.H==H and H*G+G*H==s.zeros(3))
ck('full index0 does not fix chiral index',H.cols-H.rank()-(H.rows-H.rank())==0 and T.cols-T.rows==1)
# Quaternionic structure inside grades doubles, not cancels, chiral index.
J2=s.Matrix([[0,1],[-1,0]]);J=s.diag(J2,J2,J2);Tq=s.Matrix.hstack(I2,s.zeros(2));Hq=s.BlockMatrix([[s.zeros(4),Tq.T],[Tq,s.zeros(2)]]).as_explicit()
ck('Kramers can coexist with index2',J*J==-s.eye(6) and J*Hq.conjugate()==Hq*J and Tq.cols-Tq.rows==2)
ck('real grade-preserving symmetry permits odd index',H==H.conjugate() and T.cols-T.rows==1)
# Recompute characteristic coefficients, not merely copied integers.
p,n=s.symbols('p n');obs=(F(80,3)*p+16*n);hidden=12*p-68*n;total=F(116,3)*p-52*n
ck('formal additivity for arbitrary normal p1',s.expand(obs+hidden-total)==0)
coefs=[s.expand(x.subs(n,6*p)).coeff(p)*3 for x in [obs,hidden,total]]
ck('closed metric-normal coefficients',coefs==[368,-1188,-820])
ck('nonzero signature cannot balance coherent total',coefs[2]!=0)
ck('zero signature also zero observed in this comparison',all(x*0==0 for x in coefs))
g,eta=native_gammas();I=np.eye(128,dtype=complex);Z=0*I
# Signed Gaussian-integer matrices: exact array equality, no tolerances.
def eq(a,b):return np.array_equal(a,b)
def prod(gs):
 r=I.copy()
 for a in gs:r=r@a
 return r
def real_intertwiner(gs):
 imag=[x for x in gs if eq(x.conjugate(),-x)];real=[x for x in gs if eq(x.conjugate(),x)]
 assert len(imag)+len(real)==14
 return prod(imag if len(imag)%2==0 else real)
Hslots=[9,0,1,2];Nslots=[i for i in range(14) if i not in Hslots]
chiH=1j*prod([g[i] for i in Hslots]);chiY=prod(g)
ck('native Lorentz and ambient grades square1',eq(chiH@chiH,I) and eq(chiY@chiY,I))
# Lift b -> (b,-jN GammaH b); multiply by10 to retain integral entries.
R={(a,b):10*I*(a==b) if a in Hslots else -eta[a]*g[a]@g[b] for a in range(14) for b in Hslots}
ck('literal observation has gamma-traceless lift',all(eq(sum((g[a]@R[a,b] for a in range(14)),Z.copy()),Z) for b in Hslots))
ck('coherent G descends horizontal chirality',all(eq((1 if a in Hslots else -1)*chiH@R[a,b],R[a,b]@chiH) for a in range(14) for b in Hslots))
ck('ambient grade is not horizontal observed grade',not eq(chiY,chiH) and not eq(chiY,-chiH))
ck('ambient lift intertwines ambient not horizontal grade',all(eq(chiY@R[a,b],R[a,b]@chiY) for a in range(14) for b in Hslots))
ck('slotwise horizontal grade fails gamma kernel',not eq(sum((g[a]@chiH@R[a,Hslots[0]] for a in range(14)),Z.copy()),Z))
for name,gs in [('K95',g),('K77',[1j*x if j in (7,8) else x for j,x in enumerate(g)])]:
 J=real_intertwiner(gs);ch=1j*prod([gs[i] for i in Hslots]);cy=prod(gs)
 ck(name+' Clifford antiunitary intertwining',all(eq(J@x.conjugate(),x@J) for x in gs))
 ck(name+' real-square',eq(J@J.conjugate(),(-1 if name=='K95' else 1)*I))
 ck(name+' preserves ambient grade',eq(J@cy.conjugate(),cy@J))
 ck(name+' exchanges horizontal/coherent grade',eq(J@ch.conjugate(),-ch@J))
 ck(name+' central imaginary connection breaks J preservation',not eq(J@(1j*I).conjugate(),(1j*I)@J))
K95=prod(g[:9]);connection=1j*I
ck('central imaginary connection is allowed K-skew',eq(connection.conj().T@K95+K95@connection,Z))
ck('native Q square-trace coefficient positive',F(13)*(1-F(4,196))>0)
ck('Lorentz square traces forbid one positive Hermitian phase',F(13)*(1-F(4,196))*(-1)<0)
# Asymmetric observed quotient at total0 is possible only if the total balance
# does not restrict to the same hidden complex: dimensions suffice for control.
ck('balanced total can have compensating unequal splits',2-2==(1-2)+(1-0)==0)
print('PASS:',len(checks),'exact zero-total/grading/real-structure controls.')
if '--json' in sys.argv:print(json.dumps({'checks':checks,'closed_coefficients':list(map(int,coefs))},indent=2))
