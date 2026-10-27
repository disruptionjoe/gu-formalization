"""Exact inherited native current; rational extraction, complex projector, real faults."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,argparse,hashlib
import sympy as s
import k2021_common_degree_dual_operator as q
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k2120-inherited-core-current.json'
INPUTS=['lab/process/k1951-coordinated-zero-southeast-principal.json','lab/process/k1967-paired-raw-coefficient-observation.json','tests/channel-swings/k2021_common_degree_dual_operator.py']
def dec(x):return {(i,j):F(v) for i,j,v in x['entries']}
def adj(x):return {(j,i):s.conjugate(v) for (i,j),v in x.items()}
def trace(x):return sum(v for (i,j),v in x.items() if i==j)
def comm(x,y):return q.add((1,q.mul(x,y)),(-1,q.mul(y,x)))
def anti(x,y):return q.add((1,q.mul(x,y)),(1,q.mul(y,x)))
def build(fault=None):
 jc={}; cs=[{} for _ in range(3)]
 for k,b in enumerate(json.loads((ROOT/INPUTS[0]).read_text())['blocks']):
  for (r,c),v in q.mul(dec(b['basis']),dec(b['section'])).items():jc[b['coordinates'][r],4*k+c]=v
  for ell in range(3):cs[ell].update({(4*k+r,4*k+c):v for (r,c),v in dec(b['quotient_generators'][ell]).items()})
 m=dec(json.loads((ROOT/INPUTS[1]).read_text())['scalar']['repair'][0]['M'])
 h=q.H.copy();d=q.raw(0).copy()
 if fault=='injection':jc[min(jc)]*=2
 if fault=='pairing':h[min(h)]*=-1
 if fault=='time-sign':d[min(d)]*=-1
 if fault=='mass':m[min(m)]*=-1
 g=q.mul(q.tr(jc),q.mul(h,jc));fc=q.mul(q.tr(jc),q.mul(h,q.mul(d,jc)))
 mf=q.mul(q.tr(m),q.mul(fc,m));t=q.add((F(140,9),fc),(F(140,9),mf));a=q.add((F(140,27),fc),(F(-140,27),mf))
 v=q.mul(q.mul(cs[0],cs[1]),cs[2]);z=q.mul(a,q.add((-1,v)))
 r={(j^4,j):F(-1 if j>=64 else 1) for j in range(128)}
 if fault=='reflection':r[min(r)]*=-1
 if fault=='odd-normalization':z=q.add((F(1,2),z))
 p=q.add((F(1,4),q.mul(q.add((1,q.I),(s.I,t)),q.add((1,q.I),(1,r)))))
 if fault=='projector-normalization':p=q.add((2,p))
 ck={};check=lambda key,b:ck.__setitem__(key,bool(b))
 check('G-symmetric-neutral-involution',q.tr(g)==g and q.mul(g,g)==q.add((F(121,2450)**2,q.I)) and trace(g)==0)
 check('F-skew',q.tr(fc)==q.add((-1,fc)))
 ff=q.add((-1,q.mul(fc,fc)));check('F-magnitudes',len(ff)==128 and all(i==j for i,j in ff) and list(ff.values()).count(F(81,4900))==64 and list(ff.values()).count(F(81,19600))==64)
 check('mass-skew-square',q.tr(m)==q.add((-1,m)) and q.mul(m,m)==q.add((-1,q.I)))
 for i,c in enumerate(cs):
  check(f'clifford-{i}',q.tr(c)==c and q.mul(c,c)==q.I and not anti(c,m))
  for j in range(i):check(f'anticommuting-{i}-{j}',not anti(c,cs[j]))
  check(f'current-principal-{i}',not comm(fc,c))
 for name,x in [('T',t),('Z',z),('R',r)]:
  for i,c in enumerate(cs+[m]):check(f'{name}-commutes-{i}',not comm(x,c))
 check('T-complex-structure',q.tr(t)==q.add((-1,t)) and q.mul(t,t)==q.add((-1,q.I)))
 check('Z-involution',q.tr(z)==z and q.mul(z,z)==q.I)
 check('R-involution',q.tr(r)==r and q.mul(r,r)==q.I)
 check('commuting-TZR',not comm(t,z) and not comm(t,r) and not anti(r,z))
 check('joint-multiplicities',trace(t)==trace(z)==trace(q.mul(t,z))==0)
 check('F-decomposition',fc==q.add((F(9,280),t),(F(27,280),q.mul(v,z))))
 check('P-projector-rank32',adj(p)==p and q.mul(p,p)==p and trace(p)==32)
 check('P-current',q.mul(p,q.mul(q.add((s.I,fc)),p))==q.add((F(9,280),p)))
 for i,c in enumerate(cs+[m]):check(f'P-reducing-{i}',not comm(p,c))
 check('conjugate-disjoint',not q.mul(p,{ij:s.conjugate(x) for ij,x in p.items()}))
 # A genuine alternative at theta=pi/2: Rtheta=iZR.
 rr=q.add((s.I,q.mul(z,r)));pp=q.add((F(1,4),q.mul(q.add((1,q.I),(s.I,t)),q.add((1,q.I),(1,rr)))))
 check('alternative-projector',adj(pp)==pp and q.mul(pp,pp)==pp and trace(pp)==32 and pp!=p and q.mul(pp,q.mul(q.add((s.I,fc)),pp))==q.add((F(9,280),pp)))
 return ck
FAULTS=['injection','pairing','time-sign','mass','reflection','odd-normalization','projector-normalization']
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
 clean=build();assert all(clean.values()),[k for k,v in clean.items() if not v]
 caught={}
 for fault in FAULTS:
  bad=build(fault);fail=[k for k,v in bad.items() if not v];assert fail,fault;caught[fault]=fail
  print('[FAIL detected]',fault,fail[0])
 result=dict(result_id='K2120',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',exact_checks=clean,fault_failures=caught,pairing_inertia=[64,64],current_inertia=[64,64],maximal_massive_complex_dimension=32,current_on_projector='9/280',scope='Fixed simultaneous C1,C2,C3,M invariant subspaces; strict positive compressed iF. Proof of maximality and domain is in note, not inferred from probe.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in INPUTS})
 if args.write:OUT.write_text(json.dumps(result,indent=2)+'\n')
 else:assert result==json.loads(OUT.read_text())
 print('PASS K2120',len(clean),'exact checks;',len(caught),'genuine faults')
if __name__=='__main__':main()
