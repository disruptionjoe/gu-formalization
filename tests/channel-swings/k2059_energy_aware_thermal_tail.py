"""Exact packing/energy-tail certificates; no floating solver in reproduction."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,argparse
ROOT=Path(__file__).resolve().parents[2]
K={1:F(7,29),2:F(1,9),3:F(1,23)}
C={1:F(29,135),2:F(9,50),3:F(23,90)}
A={1:F(14,55),2:F(1,8),3:F(3,55)}
REF='lab/process/k2045-third-thermal-spacing-phase.json'
PIN='6641419ca109d3cbbcd21014913ed22a710f9b1c2249974ba0bb593b9591a637'
def allowed(s):
 r=s[-1]-s[-2] if len(s)>1 else 4
 return [d for d in K if s[-1]+d>=12 and r+d>=4]
def beta(s):return max([F(0)]+[A[d] for d in allowed(s)])
def shift(s):return max(1,s[-2]+1) if len(s)>1 else 1
def hull(points):
 out=[]
 for p in sorted(set(points)):
  if out and p[0]==out[-1][0]:continue
  while len(out)>1:
   a,b=out[-2:]
   if (b[0]-a[0])*(p[1]-b[1])-(b[1]-a[1])*(p[0]-b[0])<=0:out.pop()
   else:break
  out.append(p)
 return out

def bellman(a,t,L=32):
 assert t>0 and a<=t*(L+1)
 g={}
 for n in range(L,11,-1):
  for d in K:g[n,d]=max([F(0)]+[a-t*n+K[e]*g.get((n+e,e),F(0)) for e in K if d+e>=4])
 return g

def policy(a,t,L=32):
 # A candidate chooses an affine piece; exact verification later checks the
 # resulting maximum, so this is not an optimizer completeness assumption.
 g={};pol={}
 for n in range(L,11,-1):
  for d in K:
   candidates=[(F(0),F(0))]+[(1+K[e]*g.get((n+e,e),(0,0))[0],F(n)+K[e]*g.get((n+e,e),(0,0))[1]) for e in K if d+e>=4]
   g[n,d]=max(candidates,key=lambda v:v[0]*a-v[1]*t)
 return g

def reachable(s,L):
 reach={(s[-1]+d,d) for d in allowed(s)}
 for n in range(12,L+1):
  for d in K:
   if (n,d) in reach:reach.update((n+e,e) for e in K if d+e>=4 and n+e<=L)
 return reach

def solve_energy(bank,ci,vi,seed,active):
 L=64;g=policy(*map(F,seed),L);s=bank[ci]['s'];v=bank[ci]['vertices'][vi];p=F(v['p'][-1]);e=F(v['energy']);r=F(v['value'])
 d=max(allowed(s),key=lambda d:K[d]*(g[s[-1]+d,d][0]*F(seed[0])-g[s[-1]+d,d][1]*F(seed[1])))
 B,D=g[s[-1]+d,d];aa=1+p*K[d]*B;tt=e+p*K[d]*D
 u,w=g[active];det=aa*(-w)-u*(-tt);price=C[active[1]]
 a=(r*(-w)-price*(-tt))/det;t=(aa*price-u*r)/det
 gg=bellman(a,t,L);ell=shift(s);hh=bellman(a-t*ell,t,L);reach=reachable(s,L)
 assert gg[active]==price
 assert a-t*e+p*max([F(0)]+[K[j]*gg.get((s[-1]+j,j),F(0)) for j in allowed(s)])==r
 assert all(gg[n,j]<=C[j] for n,j in reach)
 assert all(x<=C[j] for (n,j),x in hh.items())
 assert all(a-t*(n+ell)+K[j]*hh.get((n+j,j),F(0))<=F(1,2) for n in range(12,L+1) for j in K)
 return dict(kind='energy',a=str(a),s=str(-t),shift=ell,cutoff=L,contact=[ci,vi],active_cost=list(active),bellman=[[n,d,str(x)] for (n,d),x in sorted(gg.items())],high_bellman=[[n,d,str(x)] for (n,d),x in sorted(hh.items())])

def witness():
 import sympy as sy
 q=sy.Rational;N=10;bits=[0,1,1,1,0,0,0,0,1];T=sy.zeros(N);T[0,0]=q(2,5);T[-1,-1]=q(1,10)
 for i,b in enumerate(bits):
  col=i if b else i+1;w=q(1,5) if b else q(4,5);T[i,col]+=w/2;T[i+1,col]+=w/2
 M=sy.eye(N)-T;roots=[1,8];E=sy.Symbol('E');out={}
 for infinite in [False,True]:
  A=M.copy();mass=[sy.S(1)]*N;en=[sy.Integer(2*i+1) for i in range(N)]
  if infinite:mass[-1]+=q(1,8);en[-1]+=q(85,32)
  A[1,:]=sy.Matrix([mass]);A[8,:]=sy.Matrix([en]);rhs=sy.zeros(N,1);rhs[1]=1;rhs[8]=E;p=A.inv()*rhs;rr=sy.simplify(sum(M*p));vec=p.subs(E,q(5,2))
  for ee in [q(249,100),q(251,100)]:
   pp=p.subs(E,ee);dd=M*pp
   assert min(pp)>0 and min(dd)>=0
   assert all((pp[i+1]-pp[i]/4)*(1 if b else -1)<=0 for i,b in enumerate(bits))
  out['countable' if infinite else 'finite21']=dict(population=list(map(str,vec)),value=str(rr.subs(E,q(5,2))),line=[str(rr.subs(E,0)),str(sy.diff(rr,E))],population_affine=[[str(x.subs(E,0)),str(sy.diff(x,E))] for x in p])
 out.update(support=list(range(1,20,2)),finite_spectrum=list(range(21)),tail_ratio='1/9',tail_mass_factor='1/8',tail_energy_factor='85/32',interval=['249/100','251/100'],orientations=bits)
 return out

def produce():
 assert hashlib.sha256((ROOT/REF).read_bytes()).hexdigest()==PIN
 bank=json.loads((ROOT/REF).read_text())['bank'];best=[None]*len(bank);E=F(5,2)
 for eta in map(F,['0','1/25','2/25','3/25','4/25']):
  vals=[[(F(v['energy']),F(v['value'])-eta*beta(c['s'])*F(v['p'][-1])) for v in c['vertices']] for c in bank]
  hh=hull([v for vs in vals for v in vs]+[(F(12),eta)])
  for i,(c,vs) in enumerate(zip(bank,vals)):
   ell=shift(c['s']);h=hull(vs+[(e+ell,r) for e,r in hh]+[(F(12),eta)])
   for (x,y),(z,w) in zip(h,h[1:]):
    sl=(w-y)/(z-x);a=y-sl*x
    if sl<0:
     rec=(a+sl*E,a,sl,eta,ell)
     if best[i] is None or rec>best[i]:best[i]=rec
 assignments=[dict(kind='uniform',a=str(a),s=str(s),eta=str(eta),shift=ell) for _,a,s,eta,ell in best]
 packing_lower=min(x[0] for x in best)
 for ci,vi,seed,active in [(188,57,['3055794/10000000','1098712/100000000'],(13,2)),(164,26,['3033527/10000000','1005984/100000000'],(14,2)),(187,35,['3056698/10000000','1099395/100000000'],(13,2)),(236,57,['2999613/10000000','861300/100000000'],(16,2)),(212,26,['3084075/10000000','1211490/100000000'],(12,2))]:
  assignments[ci]=solve_energy(bank,ci,vi,seed,active)

 lower,ci=min((F(v['a'])+E*F(v['s']),i) for i,v in enumerate(assignments));al=F(assignments[ci]['a']);sl=F(assignments[ci]['s'])
 left=F(91135,37292);right=F(77294135,28446113)
 for v in assignments:
  da=F(v['a'])-al;ds=F(v['s'])-sl
  if ds>0:left=max(left,-da/ds)
  elif ds<0:right=min(right,-da/ds)
  else:assert da>=0
 assert left<E<right and lower>F(243396,878731)
 upper=witness();up=F(upper['countable']['value'])
 return dict(scope='conditional finite/countable thermal model only',bank_ref=REF,bank_sha256=PIN,energy=str(E),packing_only_lower=str(packing_lower),lower=str(lower),lower_line=[str(al),str(sl)],bottleneck=ci,interval=[str(left),str(right)],upper=str(up),upper_witness=upper,width=str(up-lower),gain=str(lower-F(243396,878731)),assignments=assignments,inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['explorations/conditional-build/k2057-gap-aware-thermal-erasure-2026-10-25.md','explorations/conditional-build/k2029-multicomponent-thermal-placement-2026-10-24.md','explorations/conditional-build/k1934-nonuniform-four-level-catalyst-optimization-2026-10-22.md','explorations/conditional-build/k2049-wide-spacing-packing-2026-10-25.md','explorations/conditional-build/k2054-quantitative-terminal-erasure-2026-10-25.md']})
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');args=p.parse_args();d=produce();dest=ROOT/'lab/process/k2059-energy-aware-thermal-tail.json'
 if args.write:dest.write_text(json.dumps(d,indent=2)+'\n')
 else:assert json.loads(dest.read_text())==d
 print('PASS',len(d['assignments']),'assignments; lower',d['lower'],'=',float(F(d['lower'])),'interval',d['interval'],'packing-only',d['packing_only_lower'])
