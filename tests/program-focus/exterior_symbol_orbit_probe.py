#!/usr/bin/env python3
"""Exact structural symbol controls; no source/domain inference."""
import sympy as S
n=14
J=S.Matrix([[0,1],[-1,0]])
X=S.Matrix([[0,1],[1,0]])
Z=S.diag(1,-1)
I=S.eye(2)
gamma=[S.kronecker_product(J,I),S.kronecker_product(X,I),
       S.kronecker_product(Z,X),S.kronecker_product(Z,Z)]
Id=S.eye(4); Zero=S.zeros(4)
JH=S.Matrix.vstack(-gamma[0],*gamma[1:])

def D(i,b,v,M):
    cx=gamma[i]; eta=-1 if i==0 else 1
    ins=S.Matrix.vstack(*[Id if j==i else Zero for j in range(4)])
    contraction=S.Matrix.hstack(*[eta*Id if j==i else Zero for j in range(4)])
    Q=S.diag(*([cx]*4))-S.Rational(2,n)*JH*contraction
    U=ins-JH*cx/n
    return S.Matrix.vstack(
        S.Matrix.hstack(Q,*[x*U for x in b]),
        S.Matrix.hstack(S.Matrix.vstack(*[x*contraction for x in v]),
                        S.kronecker_product(M,cx)))

b=S.Matrix([[1,0]])
for v,expected in [(S.Matrix([0,0]),4),(S.Matrix([0,1]),4),
                   (S.Matrix([-S.Rational(12,49),0]),0)]:
    M=S.eye(2)+S.Rational(13,12)*v*b
    E=-D(0,list(b),v,M).inv()*D(1,list(b),v,M)
    N=E*E-S.eye(24)
    assert N*N==S.zeros(24)
    assert N.rank()==expected

# Exact symbolic Schur/orbit identity; compact matrices, no full1920 job.
import json, importlib.util
from pathlib import Path
n0=S.symbols('n',nonzero=True)
a,c,e,f,g,h,s=S.symbols('a c e f g h s')
be=(n0-2)/n0;rho=(n0-1)/n0;kap=(n0-1)/(n0-2)
L=2*a+n0*c;F=a+(n0-1)*c;Q0=a+(n0-2)*c;T=g+h;Z0=e*F-a*(n0-2)*f
B=S.Matrix([[-a*be,e]]);C=S.Matrix([L,g]);M=S.Matrix([[-rho*L,e+n0*f],[g/n0+h,s]])
K=(M-kap/a*C*B).applyfunc(S.simplify)
expectedK=S.Matrix([[0,-n0*Z0/(a*(n0-2))],[T,s-kap*g*e/a]])
assert (K-expectedK).applyfunc(S.factor)==S.zeros(2)
assert S.factor(K.det()-n0*Z0*T/(a*(n0-2)))==0
mu=(B/a*K.inv()*C)[0]
poly=a*L*s+e*(g*Q0+h*(Q0+a))+a*f*((4-n0)*g+4*h)
assert S.factor(mu+4*(n0-2)/n0**2+(n0-2)**2*poly/(n0**2*T*Z0))==0
checks=3

def coeffs(vals):
    av,cv,ev,fv,gv,hv,sv=map(S.sympify,vals)
    bv=S.Matrix([[-av*S.Rational(12,14),ev]])
    vv=S.Matrix([2*av+14*cv,gv])
    mv=S.Matrix([[-S.Rational(13,14)*vv[0],ev+14*fv],[gv/14+hv,sv]])
    def mat(i):
        cx=gamma[i];eta=-1 if i==0 else 1
        ins=S.Matrix.vstack(*[Id if j==i else Zero for j in range(4)])
        con=S.Matrix.hstack(*[eta*Id if j==i else Zero for j in range(4)])
        q=S.diag(*([cx]*4))-S.Rational(2,14)*JH*con
        u=ins-JH*cx/14
        return S.Matrix.vstack(S.Matrix.hstack(av*q,*[x*u for x in bv]),S.Matrix.hstack(S.Matrix.vstack(*[x*con for x in vv]),S.kronecker_product(mv,cx)))
    pp=S.factor(poly.subs(dict(zip([n0,a,c,e,f,g,h,s],[14,*map(S.sympify,vals)]))))
    reg=av*(gv+hv)*(ev*(av+13*cv)-12*av*fv)
    return mat,pp,reg,bv,vv,mv
cases=[('generic',(1,0,1,1,1,1,0)),('Fzero',(1,-S.Rational(1,13),1,1,1,1,0)),('Lzero',(1,-S.Rational(1,7),1,0,1,1,0)),('Czero',(1,-S.Rational(1,7),1,0,0,1,0)),('semisimple',(1,0,1,0,1,0,-S.Rational(1,2))),('asingular',(0,1,1,0,1,0,0)),('Tsingular',(1,0,1,0,1,-1,0)),('Zsingular',(1,0,12,1,1,0,0))]
case_results=[]
equivalent_generic_checked=False
def pair_frame(b,v):
    mu=(b*v)[0]
    if mu!=0:return S.Matrix.hstack(v/mu,S.Matrix([-b[1],b[0]]))
    if v!=S.zeros(2,1):return S.Matrix.hstack(S.Matrix([1/b[0],0]),v)
    return S.Matrix.hstack(S.Matrix([1/b[0],0]),S.Matrix([-b[1],b[0]]))
for name,vals in cases:
 mat,pp,reg,bv,vv,mv=coeffs(vals);dt=mat(0);rr=dt.rank();assert (rr==24)==(reg!=0);checks+=1
 if reg!=0:
  Es=[-dt.inv()*mat(j) for j in [1,2,3]]
  for E in Es:
   N=E*E-S.eye(24);assert N*N==S.zeros(24);assert N.rank()==(0 if pp==0 else 4);checks+=2
  kv=mv-S.Rational(13,12)/vals[0]*vv*bv
  left=S.diag(S.eye(16)/vals[0],S.kronecker_product(kv.inv(),Id));bn=bv/vals[0];vn=kv.inv()*vv;mn=S.eye(2)+S.Rational(13,12)*vn*bn
  for j in range(4):assert left*mat(j)==D(j,list(bn),vn,mn);checks+=1
  if vn!=S.zeros(2,1):
   muv=(bn*vn)[0];sv=(-49*muv-48)/72
   old,_,_,bo,vo,mo=coeffs((1,0,1,0,1,0,sv));ko=mo-S.Rational(13,12)*vo*bo;vno=ko.inv()*vo;mno=S.eye(2)+S.Rational(13,12)*vno*bo
   pf=pair_frame(bn,vn);po=pair_frame(bo,vno)
   lf=S.diag(S.eye(16),S.kronecker_product(pf.inv(),Id));rf=S.diag(S.eye(16),S.kronecker_product(pf,Id))
   lo=S.diag(S.eye(16),S.kronecker_product(po.inv(),Id));ro=S.diag(S.eye(16),S.kronecker_product(po,Id))
   for j in range(4):assert lf*D(j,list(bn),vn,mn)*rf==lo*D(j,list(bo),vno,mno)*ro;checks+=1
   if name=='generic':equivalent_generic_checked=True
  if pp==0:
   for i in range(3):
    for j in range(i):assert Es[i]*Es[j]+Es[j]*Es[i]==S.zeros(24);checks+=1
   products=[S.eye(24)]
   for E in Es:products += [p*E for p in products[:]]
   H=sum([p.conjugate().T*p for p in products],S.zeros(24))
   for E in Es:assert H*E==E.conjugate().T*H;checks+=1
 case_results.append({'case':name,'time_rank':rr,'P':str(pp)})
# Observation decoder must move under a nontrivial scalar/trace shear.
Pf=S.Matrix([[1,1],[0,1]]);field=S.diag(S.eye(16),S.kronecker_product(Pf,Id))
O=S.Matrix.vstack(S.Matrix.hstack(S.eye(16),JH/14,S.zeros(16,4)),S.Matrix.hstack(S.zeros(4,16),S.zeros(4),Id))
assert O*field!=O;checks+=1
# The wrong auxiliary half-spinor weight changes the semisimplicity predicate.
assert coeffs((1,0,1,0,1,0,-S.Rational(1,2)))[1]==0
assert coeffs((1,0,2,0,1,0,-S.Rational(1,2)))[1]!=0;checks+=1

# Full n14 null visibility via exact Clifford blades and a constructive basis map.
p=Path(__file__).with_name('source_natural_symbol_class_probe.py');spec=importlib.util.spec_from_file_location('cl',p);cl=importlib.util.module_from_spec(spec);spec.loader.exec_module(cl)
from fractions import Fraction as Fr
for positive,negative in [(7,7),(9,5)]:
 eta=[1,1,1,-1]+[1]*(positive-3)+[-1]*(negative-1);neg=positive+1
 gam=[{1<<j:Fr(1)} for j in range(14)]
 ell=cl.add(gam[4],gam[neg]);dual=cl.scale(cl.add(gam[4],cl.scale(gam[neg],-1)),Fr(1,4))
 pr=cl.cmul(ell,dual,eta)
 assert not cl.cmul(ell,ell,eta);assert not cl.cmul(ell,pr,eta);assert cl.cmul(pr,pr,eta)==pr;assert pr[0]==Fr(1,2);checks+=4
 # Domain parameters u1,u2,u3; each diagonal pr has trace64.
 bmap={}
 for j in range(1,4):
  bmap[j,j-1]=pr
  bmap[0,j-1]=cl.scale(cl.cmul(cl.cmul(gam[0],gam[j],eta),pr,eta),-eta[0])
 for q in range(3):
  tr={}
  for j in range(4):tr=cl.add(tr,cl.cmul(gam[j],bmap.get((j,q),{}),eta))
  assert not tr;checks+=1
 entries1=cl.symbols(eta,4);entries2=cl.symbols(eta,neg)
 for s1,s2 in zip(entries1,entries2):
  sym=cl.add(s1,s2)
  for out in range(15):
   for q in range(3):
    ans={}
    for (row,col,blade),coef in sym.items():
     if row==out and (col,q) in bmap:ans=cl.add(ans,cl.cmul({blade:coef},bmap[col,q],eta))
    assert not ans
  checks+=1
 # Literal horizontal observation leaves three independent pr diagonal outputs.
 assert all(bmap[j,j-1]==pr for j in range(1,4));checks+=1
# Named deliberately false alternatives rejected by exact countercontrols.
mutants={'all_cross_arrows_new':equivalent_generic_checked,'fixed_readout_under_mixing':O*field!=O,'wrong_input_half':coeffs((1,0,2,0,1,0,-S.Rational(1,2)))[1]!=0,'all_null_modes_invisible':bool(bmap[1,0])}
assert all(mutants.values())
print(json.dumps({'checks':checks,'normal_form_initial_controls':3,'cases':case_results,'mutants_rejected':list(mutants),'null_visible_bound':192,'null_signatures':['K77','K95'],'scope':'principal algebra only; no admitted singular-state or physical domain'},indent=2))
