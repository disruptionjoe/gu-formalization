#!/usr/bin/env python3
"""Exact orbit stabilizer and original-row covariance controls."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from itertools import combinations
from fractions import Fraction as F
import argparse,hashlib,json
import k2169_invertible_pencil_full_descent_probe as o
from k2214_prescribed_adapter_fibers_probe import det_mod
ROOT=Path(__file__).resolve().parents[2]
rows=[26,33,29,37,4,3,13,12,16,61,8,1,10,11,41,40,14,9,2,39,20,5,6,7,103,21,22,23,67,25,42,49,18,19,38,96,58,59,60,55,56,57,176,84,83]
def blade(t):return o.blade([o.N[i-1] for i in t])
def fixture(terms):return o.add(*(o.scale(blade(t),F(c)) for t,c in terms))
w=fixture([((1,2,3),1),((1,4,5),1),((2,6,7),2),((3,8,9),3),((4,6,10),5)])
u=fixture([((1,2,4),2),((1,5,7),3),((2,6,8),5),((3,9,10),7),((4,5,6),11)])
def conj(g,gi,x):return o.mm(o.mm(g,x),gi)
def coeff(x,b):
 m,c=next(iter(b.items()));return x.get(m,F(0))/c
def polynomial(v,t,fault=None):
 R=o.add(v,o.scale(t,3));b=o.bar(R)
 K=lambda x:o.add(*(o.scale(o.mm(o.mm(o.G[j],x),o.G[j]),o.ETA[j]) for j in o.N))
 A=o.add(o.scale(K(o.mm(b,b)),3),o.scale(o.mm(b,b),34),o.scale(o.mm(R,b),35 if fault=='Euler_coefficient' else 36),o.scale(o.mm(b,R),8),o.scale(o.mm(R,R),-24))
 B=o.add(o.scale(o.mm(R,R),184),o.scale(o.mm(R,b),140),o.scale(o.mm(b,R),184),o.scale(o.mm(b,b),194),o.scale(K(o.mm(b,R)),24),o.scale(K(o.mm(b,b)),15))
 return A,B
def original(v,t):
 R=o.add(v,o.scale(t,3));P=o.add(o.scale(v,7),o.scale(t,-15));pi=o.inv(P)
 T={j:o.scale(o.mm(pi,o.port(R)[j]),-o.ETA[j]) for j in o.N};z=o.add(v,t)
 q={j:o.RR(T,*o.C(o.port(z),*o.kernel(T,j)))[1] for j in o.N}
 return T,q
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();checks={};faults={}
 def ck(k,v):checks[k]=bool(v)
 triples=[blade(t) for t in combinations(range(1,11),3)];biv=[blade(t) for t in combinations(range(1,11),2)]
 columns=[[coeff(o.comm(b,x),t) for x in [w,u] for t in triples] for b in biv]
 mat=[[int(c[i]) for c in columns] for i in range(240)];minor=[mat[i] for i in rows]
 determinant=det_mod(minor)
 ck('rank45_minor',determinant==893116)
 ck('scalar_square_invariants',o.mm(w,w).get(0)==-38 and o.mm(u,u).get(0)==-208)
 v=o.mm(blade(range(1,11)),w);t=o.mm(o.OM,u);A,B=polynomial(v,t)
 g=o.scale(o.add(o.scale(o.I,3),o.scale(blade((1,2)),4)),F(1,5));gi=o.scale(o.add(o.scale(o.I,3),o.scale(blade((1,2)),-4)),F(1,5))
 h=o.scale(o.add(o.scale(o.I,5),o.scale(blade((1,5)),3)),F(1,4));hi=o.scale(o.add(o.scale(o.I,5),o.scale(blade((1,5)),-3)),F(1,4))
 # Original full raw row controls on an independent smaller invertible fixture;
 # no nonlinear solving or rerun of the unchanged K2214 rank certificate.
 vs=o.add(blade(range(1,8)),o.scale(blade(range(4,11)),F(2,3)))
 us=o.add(o.scale(blade((2,3,4)),F(1,5)),o.scale(blade((6,7,8)),F(2,7)));ts=o.mm(o.OM,us)
 T,q=original(vs,ts)
 for label,gg,ii in [('rotation',g,gi),('boost',h,hi),('product',o.mm(h,g),o.mm(gi,hi))]:
  ad=lambda x:conj(gg,ii,x)
  ck(label+'_inverse',o.mm(gg,ii)==o.I and o.mm(ii,gg)==o.I)
  ck(label+'_real_volume',o.bar(gg)==gg and ad(blade(range(1,11)))==blade(range(1,11)))
  L=[[coeff(ad(o.G[j]),o.G[i]) for j in o.N] for i in o.N]
  ck(label+'_vector_grade',all(all(m.bit_count()==1 for m in ad(o.G[j])) for j in o.N))
  ck(label+'_metric',all(sum(o.ETA[o.N[k]]*L[k][i]*L[k][j] for k in range(10))==o.ETA[o.N[i]]*int(i==j) for i in range(10) for j in range(10)))
  ck(label+'_real_grades',all(m.bit_count()==3 for x in [w,u] for m in ad(x)))
  aa,bb=polynomial(ad(v),ad(t));ck(label+'_ordered_Euler_covariance',aa==ad(A) and bb==ad(B))
  Tp,qp=original(ad(vs),ad(ts))
  for a,j in enumerate(o.N):
   ck(f'{label}_original_adapter_{a}',Tp[j]==o.add(*(o.scale(ad(T[k]),L[a][b]) for b,k in enumerate(o.N))))
   ck(f'{label}_original_row_{a}',qp[j]==o.add(*(o.scale(ad(q[k]),L[a][b]) for b,k in enumerate(o.N))))
  if label=='rotation':
   bad=not all(qp[j]==o.add(*(o.scale(ad(q[k]),L[b][a]) for b,k in enumerate(o.N))) for a,j in enumerate(o.N))
   faults['inverse_row_transport']=['original_row_covariance'] if bad else []
 for c in [F(-2),F(3,5)]:
  aa,bb=polynomial(o.scale(v,c),o.scale(t,c));ck('quadratic_'+str(c),aa==o.scale(A,c*c) and bb==o.scale(B,c*c))
 badg=o.add(o.I,o.scale(blade((1,2,3,4)),F(1,2)));badi=o.inv(badg)
 ck('arbitrary_even_similarity_rejected',any(any(m.bit_count()!=1 for m in conj(badg,badi,o.G[j])) for j in o.N))
 ck('original_fixture_is_nonsolution',any(q.values()))
 assert all(checks.values()),[k for k,v in checks.items() if not v]
 bad=minor[:];bad[0]=bad[1];faults['duplicate_minor_row']=['rank45_minor'] if det_mod(bad)==0 else []
 aa,bb=polynomial(v,t,'Euler_coefficient');faults['Euler_coefficient']=['ordered_Euler_input'] if aa!=A else []
 # Corrupt the metric that the actual boost must preserve.
 wrong=[1]*10;Lg=[[coeff(conj(h,hi,o.G[j]),o.G[i]) for j in o.N] for i in o.N]
 faults['normal_metric']=['boost_metric'] if any(sum(wrong[k]*Lg[k][i]*Lg[k][j] for k in range(10))!=int(i==j) for i in range(10) for j in range(10)) else []
 assert all(faults.values()),faults
 deps=['tests/channel-swings/k2169_invertible_pencil_full_descent_probe.py','tests/channel-swings/k2214_prescribed_adapter_fibers_probe.py','lab/process/k2214-prescribed-adapter-fibers.json','explorations/conditional-build/k2214-prescribed-adapter-fibers-2026-10-28.md','explorations/conditional-build/k2217-spin-orbit-adapter-exclusion-2026-10-28.md']
 report=dict(result_id='K2217',status='conditional_Spin_orbit_excluded',controls=len(checks),checks=checks,fault_failures=faults,minor={'prime':1000003,'rows':rows,'determinant':determinant},factor_orbit_dimension=45,port_cone_dimension=46,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),evidence_kinds='Universal covariance and fiber theorem; fresh exact stabilizer minor and actual polynomial controls; original all-ten rows on independent invertible fixture; unchanged K2214 fiber certificate reused.')
 dst=ROOT/'lab/process/k2217-spin-orbit-adapter-exclusion.json'
 if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(dst.read_text())==report
 print(json.dumps(dict(result='K2217',controls=len(checks),faults=faults,minor=determinant)))
if __name__=='__main__':main()
