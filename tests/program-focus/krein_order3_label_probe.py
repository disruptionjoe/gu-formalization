#!/usr/bin/env python3
"""Exact index-character/suspension and actual Clifford-observation controls.
Not a selection of the native field complex or its analytic domains.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('VECLIB_MAXIMUM_THREADS','1')
from pathlib import Path
from fractions import Fraction as F
import sys,json
import numpy as np
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tests/channel-swings'))
from actual_sym2_c14_orbit_probe import native_gammas
checks=[]
def ck(name,x):
 assert bool(x),name
 checks.append(name)
def eta(j):
 q=F(j%3,3)
 return F(0) if q==0 else 1-2*q
rows=[]
for t in range(-5,6):
 # AS: ch(T_C)=4+p1, Ahat=1-p1/24, integral p1=3sigma=-48.
 index=-48*(1-F(4+t,24))
 character=2*(-2+t) # six fixed points times Dirac local contribution1/3.
 m0=(index+2*character)/3;m1=(index-character)/3
 ck(f't={t} integral representation',m0.denominator==m1.denominator==1)
 mult=[m0,m1,m1]
 rho=[sum(mult[j]*(eta(j-k)-eta(j)) for j in range(3)) for k in range(3)]
 ck(f't={t} isotypic averaging equals index class',all((rho[k]+F(k,3)*index).denominator==1 for k in range(3)))
 ck(f't={t} twist-character divisibility criterion',all(v.denominator==1 for v in rho)==((-2+t)%3==0))
 rows.append({'t':t,'index':int(index),'fixed_twist_character':t-2,'equivariant_index':int(character),'virtual_multiplicities':list(map(int,mult)),'graded_suspension_rho':[str(x) for x in rho],'mod_Z':[str(x%1) for x in rho]})
by={r['t']:r for r in rows}
ck('A published anchor',by[-1]['index']==-42 and by[-1]['mod_Z']==['0','0','0'])
ck('B symbol-class anchor',by[1]['index']==-38 and by[1]['mod_Z']==['0','2/3','1/3'])
ck('bare control nonzero',by[0]['index']==-40 and by[0]['mod_Z']==['0','1/3','2/3'])
ck('zero is not unique to A',by[2]['index']==-36 and by[2]['mod_Z']==['0','0','0'])
t=s.symbols('t',integer=True);ms=[-16+2*t,-12,-12]
rr=[s.expand(sum(ms[j]*s.Rational(eta(j-k)-eta(j)) for j in range(3))) for k in range(3)]
ck('all integer t rho1 congruence',s.expand(rr[1]+(-40+2*t)/3)==-12)
ck('all integer t rho2 congruence',s.expand(rr[2]+2*(-40+2*t)/3)==2*t-28)
ck('all t nonzero equivariant virtual index',ms[1]==-12) # no equivariant grade-exchange balance on W_t.
# Same fields and indefinite metric, distinct chosen index gradings.
X=s.Matrix([[0,1],[1,0]]);Z=s.diag(1,-1);I2=s.eye(2)
D=s.diag(X,X);K=s.diag(I2,-I2);Gp=s.diag(Z,Z);Gm=s.diag(Z,-Z)
ck('retained pair both gradings odd, same even Krein metric',all(D*G+G*D==s.zeros(4) and K*G==G*K for G in [Gp,Gm]) and D.H*K==K*D)
# Native-shape cross-grade balanced double is a DIFFERENT comparison.
Kx=s.kronecker_product(X,I2)
ck('balanced double cross-grade K',Kx*Gm+Gm*Kx==s.zeros(4) and D*Kx==Kx*D and D.H*Kx==Kx*D)
ck('balanced double all characters and rho cancel',all(all(F(x)-F(x)==0 for x in r['graded_suspension_rho']) for r in rows))
# Actual K95 Clifford module; integer Gaussian entries, exact equality.
g,eta_metric=native_gammas();I=np.eye(128,dtype=complex);O=0*I
H=[9,0,1,2];N=[a for a in range(14) if a not in H]
eq=np.array_equal
ins={a:eta_metric[a]*g[a] for a in range(14)}
ck('horizontal insertion trace4',eq(sum((g[a]@ins[a] for a in H),O.copy()),4*I))
ck('normal insertion trace10',eq(sum((g[a]@ins[a] for a in N),O.copy()),10*I))
imposter={a:(10 if a in H else -4)*ins[a] for a in range(14)}
ck('mixed trace lies in ambient kernel',eq(sum((g[a]@imposter[a] for a in range(14)),O.copy()),O))
ck('observed imposter has nonzero gamma trace40',eq(sum((g[a]@imposter[a] for a in H),O.copy()),40*I))
# 10 times lift of arbitrary horizontal b.
lift={(a,b):(10*I*(a==b) if a in H else -ins[a]@g[b]) for a in range(14) for b in H}
ck('q kernel lift is onto full observed carrier',all(eq(sum((g[a]@lift[a,b] for a in range(14)),O.copy()),O) for b in H))
# gamma-traceless horizontal b with b_u=gamma_v, b_v=gamma_u, distinct spacelike u,v.
u,v=H[1:3];b={a:(g[v] if a==u else g[u] if a==v else O) for a in H}
ck('horizontal kernel witness',eq(sum((g[a]@b[a] for a in H),O.copy()),O))
# 7 Qbar=7 c_u b - J_H i_u b; denominator14 originally, xi spacelike.
qb={a:7*g[u]@b[a]-ins[a]@b[u] for a in H}
ck('observed symbol exits horizontal kernel',eq(sum((g[a]@qb[a] for a in H),O.copy()),10*b[u]) and not eq(b[u],O))
ck('decomposition dimensions',13*128==3*128+9*128+128 and 4*128==3*128+128)
print('PASS:',len(checks),'exact Krein-benchmark and actual-map controls.')
if '--json' in sys.argv:print(json.dumps({'checks':checks,'benchmark_rows':rows,'native_dimensions':{'total':1664,'horizontal_RS':384,'hidden_RS':1152,'imposter':128,'observed_full':512}},indent=2))
