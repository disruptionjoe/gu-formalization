#!/usr/bin/env python3
"""Exact nonnull printed-P seam, representation arithmetic and finite-jet controls.
No full matrix census or analytic PDE existence certification. SymPy1.14.0.
"""
from pathlib import Path
from types import SimpleNamespace
from fractions import Fraction as Q
from math import comb,factorial
import argparse,json,hashlib,sys,time
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tests/program-focus'))
from source_action_deep_algebra import Engine,add,scale
CERT=ROOT/'lab/process/printed-equation-jets-symbol-certificates.json'

def engine(eta):
 n=14
 return Engine(SimpleNamespace(d=eta,Lambda=[[[0]*n for _ in range(n)]for _ in range(n)],spin=[{}for _ in range(n)],mbracket=lambda i,j:{}))
def actual(e,T):return e.Phi(e.wedge({(1,0):Q(1)},T))
def compact(e,T):
 rows=e.split_one(T);ga=[{1<<j:Q(1)}for j in range(14)];cp=e.cliff_product
 B=add(*(scale(e.d[0]*e.d[b],cp(cp(ga[0],ga[b]),rows.get(b,{}),'anti'))for b in range(1,14)))
 out={}
 for j in range(14):
  lead=add(*(scale(e.d[b],cp(ga[b],rows.get(b,{}),'comm'))for b in range(1,14)))if j==0 else scale(-e.d[0],cp(ga[0],rows.get(j,{}),'comm'))
  row=add(lead,scale(Q(-1,2),cp(ga[j],B,'anti')))
  for c,z in row.items():out[(1<<j,c)]=z
 return out

def ext(e,i,z,raise_degree):
 out={}
 for mask,v in z.items():
  if bool(mask&(1<<i))==raise_degree:continue
  c,q=e.cmul(1<<i,mask);out[c]=out.get(c,Q())+q*v
 return {c:v for c,v in out.items()if v}
def block_formula(e,beta,p,with0):
 # beta is a transverse covector-valued grade-p exterior form.
 w=add(*(scale(e.d[b],ext(e,b,beta.get(b,{}),True))for b in range(1,14)))
 c=add(*(scale(e.d[b],ext(e,b,beta.get(b,{}),False))for b in range(1,14)))
 def gam(z):return e.cliff_product({1:Q(1)},z)
 out={}
 if p%2:
  for i in range(1,14):
   z=scale(2,add(ext(e,i,c,True),scale(-1,beta.get(i,{}))))if with0 else scale(2*e.d[0],gam(add(ext(e,i,w,False),scale(-1,beta.get(i,{})))))
   for k,v in z.items():out[(1<<i,k)]=v
 else:
  row=scale(-2,gam(w))if with0 else scale(2,c)
  for k,v in row.items():out[(1,k)]=v
  for i in range(1,14):
   z=scale(2,ext(e,i,c,False))if with0 else scale(2*e.d[0],gam(ext(e,i,w,True)))
   for k,v in z.items():out[(1<<i,k)]=v
 return out

def build():
 checks=[]
 def ck(k,v):assert v,k;checks.append(k)
 for port,eta in [('K95',[-1,1,1,1]+[1]*6+[-1]*4),('K77',[1,-1,-1,-1]+[1]*6+[-1]*4)]:
  e=engine(eta)
  for p in range(14):
   blade=sum(1<<b for b in range(1,p+1))
   for g0 in [False,True]:
    for leg in [0,1,13]:
     T={(1<<leg,blade|int(g0)):Q(1)};v=actual(e,T)
     ck(f'{port}:compact:{p}:{g0}:{leg}',v==compact(e,T))
     if leg:ck(f'{port}:exterior-block:{p}:{g0}:{leg}',v==block_formula(e,{leg:{blade:Q(1)}},p,g0))
     else:ck(f'{port}:longitudinal-kernel:{p}:{g0}',not v)
  O={(1<<b,1<<b):Q(1)for b in range(1,14)};V={(1<<b,1|(1<<b)):Q(1)for b in range(1,14)}
  ck(port+':trace-pair-forward',actual(e,O)==scale(-2*eta[0],V));ck(port+':trace-pair-back',actual(e,V)==scale(24,O))
  top=sum(1<<b for b in range(1,14));T={(2,top):Q(1)};U={(2,top|1):Q(1)}
  ck(port+':top-chain-nonzero',actual(e,T)==scale(-2*eta[0],U));ck(port+':top-chain-terminates',not actual(e,U))
  # Longitudinal output is a real difference from the wedge companion's symbol.
  v=actual(e,{(2,6):Q(1)})
  ck(port+':selected-nonzero-longitudinal',any(leg==1 for leg,c in v))
 choose=lambda k:comb(13,k)if 0<=k<=13 else 0
 hook=lambda p:13*choose(p)-choose(p+1)-choose(p-1)
 dim=14*2**14;odd=2*sum(choose(q+1)for q in range(1,13))+2*sum(hook(p)for p in range(1,14,2));even=2*sum(choose(k)for k in range(1,12,2))
 j2=sum(choose(p-1)for p in range(2,13,2))+sum(choose(p+1)for p in range(0,13,2))+13
 j1=2*sum(hook(p)for p in range(0,13,2))+1+(2**14-(j2-13));nonzero=odd+even
 ck('full-dimension-partition',dim==nonzero+2*j2+j1)
 ck('Jordan-counts',(nonzero,j2,j1,nonzero+j2,j1+j2)==(114660,8204,98308,122864,106512))
 ck('hook-arithmetic',sum(hook(p)for p in range(0,13,2))==sum(hook(p)for p in range(1,14,2))==45057)
 # Generic formal recursion: variable coefficients, derivatives and a quadratic term.
 import sympy as sp
 x,h=sp.symbols('x h');P=lambda u:(1+x)*sp.diff(u,x)+2*x*u;S=1+x*x;coeff=[sp.Integer(0)]
 for k in range(1,7):coeff.append(sp.expand(-S if k==1 else -P(coeff[k-1])-3*sum(coeff[a]*coeff[k-1-a]for a in range(1,k-1))))
 U=sum(h**k*coeff[k]for k in range(1,7));res=sp.Poly(sp.expand(U+h*(S+P(U)+3*U*U)),h)
 ck('formal-variable-nonlinear-through-six',all(res.coeff_monomial(h**k)==0 for k in range(7)))
 # Scalar u+h(u'-f)=0: exact finite jets, factorial h-series, no uniform tower.
 zero_values=[]
 for m in range(9):
  jet=[Q()for _ in range(m+2)];hh=Q(1,2)
  for j in range(m,-1,-1):jet[j]=hh*(factorial(j)-jet[j+1])
  ck(f'finite-spacetime-jet:{m}',all(jet[j]+hh*(jet[j+1]-factorial(j))==0 for j in range(m+1)))
  zero_values.append(str(jet[0]))
 ck('separate-orders-need-not-glue',len(set(zero_values))>1)
 ck('factorial-formal-series-ratio',all(factorial(k+1)//factorial(k)==k+1 for k in range(1,9)))
 # Frozen nilpotent descriptor inverse has exactly one derivative of forcing.
 J=sp.Matrix([[0,1],[0,0]]);f=sp.Matrix([x*x,x**3]);kap=sp.Rational(3,2);u=-f/kap+J*f.diff(x)/kap**2
 ck('zero-Jordan-descriptor-inverse',kap*u+J*u.diff(x)+f==sp.zeros(2,1))
 ck('zero-Jordan-second-derivative-vanishes',J*J==sp.zeros(2))
 inp=['tests/program-focus/source_action_deep_algebra.py','explorations/conditional-build/printed-endpoint-analytic-branch-2026-11-27.md','explorations/conditional-build/ricci-flat-ambient-source-jets-2026-11-27.md']
 return {'status':'PASS','checks':len(checks),'check_names':checks,'dimensions':{'carrier':dim,'nonzero':nonzero,'zero_size2':j2,'zero_size1':j1,'rank':nonzero+j2,'kernel':j1+j2},'finite_jet_scalar_u0':zero_values,'probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()for p in inp},'sympy_version':sp.__version__,'scope':'Representative exact nested-star identity checks and analytic multiplicity arithmetic. Whole symbol/formal/IFT proof is written and reviewed. No dense census, convergent full PDE solution, physical spectrum or source-GU exclusion.'}
if __name__=='__main__':
 p=argparse.ArgumentParser();mode=p.add_mutually_exclusive_group(required=True);mode.add_argument('--write-certificate',action='store_true');mode.add_argument('--verify',action='store_true');a=p.parse_args();start=time.monotonic();d=build()
 if a.write_certificate:CERT.write_text(json.dumps(d,indent=2)+'\n')
 else:assert json.loads(CERT.read_text())==d,'Certificate differs'
 print(json.dumps({'status':'PASS','checks':d['checks'],'dimensions':d['dimensions'],'seconds':time.monotonic()-start}))
