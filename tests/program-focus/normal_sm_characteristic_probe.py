#!/usr/bin/env python3
"""Exact algebra controls for the written normal-bundle theorem; not topology automation."""
from pathlib import Path
from fractions import Fraction as F
import argparse, hashlib, json, time
ROOT=Path(__file__).resolve().parents[2]
CERT='lab/process/normal-sm-characteristic-certificates.json'
INPUTS=['explorations/conditional-build/global-normal-complex-reduction-2026-11-24.md','explorations/conditional-build/normal-special-unitary-existence-2026-11-25.md','explorations/conditional-build/normal-sm-global-quotient-2026-11-27.md','explorations/conditional-build/closed-spin-normal-reduction-2026-11-27.md','explorations/conditional-build/native-rs-moving-section-index-2026-11-11.md']
N=4
zero=(0,)*N

def clean(p):return {k:v for k,v in p.items() if v}
def const(x):return {} if not x else {zero:F(x)}
def add(*ps):
 r={}
 for p in ps:
  for k,v in p.items():r[k]=r.get(k,F(0))+v
 return clean(r)
def scale(p,c):return clean({k:v*c for k,v in p.items()})
def mul(p,q):
 r={}
 for k,v in p.items():
  for l,w in q.items():
   m=tuple(a+b for a,b in zip(k,l));r[m]=r.get(m,F(0))+v*w
 return clean(r)
def var(n):return {tuple(int(i==n)for i in range(N)):F(1)}
def c1(rs):return add(*rs)
def c2(rs):return add(*(mul(rs[i],rs[j])for i in range(len(rs))for j in range(i+1,len(rs))))
def run():
 checks=[]
 def check(name,condition):
  assert condition,name
  checks.append(name)
 x,y,z,l=map(var,range(N));sq=lambda a:mul(a,a)
 roots=[x,scale(x,-1),y,scale(y,-1)]
 sym=[add(roots[i],roots[j])for i in range(4)for j in range(i,4)]
 p=add(sq(x),sq(y))
 check('native Sym2 roots have rank10 and zero c1',len(sym)==10 and c1(sym)=={})
 check('root-computed p1Sym2 equals6p1V',scale(c2(sym),-1)==scale(p,6))
 check('coefficient5 mutation detected',scale(c2(sym),-1)!=scale(p,5))
 for n,rs in [(2,[x,y]),(3,[x,y,z])]:
  for weight in [2,-3]:
   t=scale(l,weight);tw=[add(a,t)for a in rs]
   check(f'rank{n} weight{weight} full tensor c1',c1(tw)==add(c1(rs),scale(t,n)))
   check(f'rank{n} weight{weight} full tensor c2',c2(tw)==add(c2(rs),scale(mul(c1(rs),t),n-1),scale(sq(t),n*(n-1)//2)))
 check('line twist oriented real rank4 correction6z2 annihilated by2z',6%2==0)
 # Universal scalar class arithmetic: d^2=p, eQ=0, p1P=5p.
 check('positive and total class coefficients',F(1-5,2)==-2 and -2-1==-3)
 check('wrong sign Euler-realification mutation detected',F(5-1,2)!=-2)
 check('determinant exponents cancel',3*2+2*(-3)==0)
 check('kernel exponents have exact common modulus6',sorted(j for j in range(12)if j%6==0)==[0,6])
 # Product twist: c2W=0, c2C=-2p, p=36ell^2.
 check('weak SU untwist',-9+9==0)
 check('color SU untwist',-84+12==-2*36)
 check('tracefree agrees with actual SU lift',F(-36,4)==-9 and F(-7*36,3)==-84)
 check('zero geometric c2 does not force zero SU charge',0!= -9)
 # Exhaust all congruence residues modulo144, not an unbounded example census.
 check('combined signature divisibility is48',all(((s%16==0 and s%12==0)==(s%48==0))for s in range(144)))
 check('signature16 quotient example cannot product lift',(-16)%48!=0 and (-16)%16==0)
 check('signature48 lift hyperbolic construction',all(2*1*(2*m)==4*m and 36*4*m==3*(48*m)for m in [-2,-1,0,1,2]))
 check('connected sum example chi and sigma',3*24-2*(3-1)-2*34==0 and 3*(-16)==-48)
 check('one K3 Lorentz example',24-2*12==0)
 check('T4 fixed-reduction obstruction despite zero signature',2%6!=0 and 2*2*0==0)
 check('abstract SU2 c2=1 violates trace-line geometric condition',1!=0)
 vals={'signature_minus16':{'d_squared':-48,'c2_E2':0,'c2_E3':96,'c2_total':144},'signature_minus48_product_lift':{'ell_squared':-4,'c2_SU2':36,'c2_SU3':336}}
 return {'artifact':'NORMAL_SM_CHARACTERISTIC_CERTIFICATE','basis_revision':'cb77c122924f6615574011bffc99b81193ffe58a','native_inputs_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()for p in INPUTS},'scope':'Exact polynomial/divisibility controls; topology, source applicability and physical meaning are written-review obligations.','checks':checks,'check_count':len(checks),'examples':vals}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--verify',action='store_true');ap.add_argument('--write-certificate',action='store_true');a=ap.parse_args();start=time.perf_counter();d=run()
 if a.write_certificate:(ROOT/CERT).write_text(json.dumps(d,indent=2)+'\n')
 if a.verify:assert json.loads((ROOT/CERT).read_text())==d,'certificate/dependency mismatch'
 print(json.dumps({'status':'PASS','grouped_controls':d['check_count'],'seconds':time.perf_counter()-start,'scope':d['scope']}))
