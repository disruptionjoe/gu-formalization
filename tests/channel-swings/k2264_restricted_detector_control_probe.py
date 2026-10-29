#!/usr/bin/env python3
"""Exact finite configuration gaps, edge filters, Lie/shell and resource controls.
No finite sample substitutes for the universal written construction.
"""
import itertools
from fractions import Fraction as F
import sympy as s
FAULTS=['remove_spectator_terms','remove_neutral_coupling','linear_diagonal_only','wrong_modulus','wrong_filter_sign','wrong_completion','wrong_passive_factor','wrong_pulse_area','omit_edge_normalization','omit_hard_wall']
def controls(fault=None):
 out={}
 def ck(k,v):out[k]=bool(v)
 caps=(2,2,2);a=2;vertices=list(itertools.product(*(range(c+1) for c in caps),range(a)));S=3
 def features(z):
  n=z[:-1];l=z[-1]
  if fault=='linear_diagonal_only':return list(n)+[int(l==q) for q in range(a)]
  f=list(n)+[x*x for x in n]
  if fault!='remove_spectator_terms':f += [n[i]*n[j] for i in range(S) for j in range(i+1,S)]
  f += [int(l==q) for q in range(a)]
  if fault!='remove_neutral_coupling':f += [n[i]*int(l==q) for i in range(S) for q in range(a)]
  return f
 edges=[]
 for u in vertices:
  for i in range(S-1):
   for sign in [-1,1]:
    v=list(u);v[i]+=sign;v[i+1]-=sign
    if 0<=v[i]<=caps[i] and 0<=v[i+1]<=caps[i+1]:edges.append((u,tuple(v),i))
  for q in [-1,1]:
   v=(*u[:-1],u[-1]+q)
   if 0<=v[-1]<a:edges.append((u,v,'neutral'))
 diffs=[tuple(y-x for x,y in zip(features(u),features(v))) for u,v,_ in edges]
 ck('directed_feature_differences_unique',len(set(diffs))==len(edges))
 base=17;D={z:sum(base**j*x for j,x in enumerate(features(z))) for z in vertices}
 gaps=[D[v]-D[u] for u,v,_ in edges];lam=max(D.values());M=(2 if fault=='wrong_modulus' else 2*lam+1)
 ck('integer_gaps_nonzero',all(gaps));ck('integer_gaps_unique',len(set(gaps))==len(gaps))
 ck('modular_gaps_unique',len({x%M for x in gaps})==len(gaps))
 ck('feature_count',len(features(vertices[0]))==17)
 # Independently verify each total-charge graph by reachability.
 for charge in range(sum(caps)+1):
  subset={z for z in vertices if sum(z[:-1])==charge};seen={min(subset)}
  while True:
   add={v for u,v,_ in edges if u in seen};new=seen|add
   if new==seen:break
   seen=new
  ck('connected_charge_'+str(charge),seen==subset)
 # Formal root-of-unity average: phase i -> coefficient i on target edge.
 chosen=((1,1,0,0),(2,0,0,0),0);u0,v0,k0=chosen;gap=D[v0]-D[u0]
 def amplitude(u,v):
  removed=next(j for j in range(S) if v[j]<u[j]);added=next(j for j in range(S) if v[j]>u[j])
  return s.sqrt(u[removed]*(u[added]+1))
 ce=amplitude(u0,v0);ck('nonunit_edge_amplitude',ce==s.sqrt(2))
 for idx,(u,v,k) in enumerate(edges):
  if k!=k0:continue
  d=D[v]-D[u]
  if fault=='wrong_filter_sign':coef=s.I*int((d+gap)%M==0)-s.I*int((d-gap)%M==0)
  else:coef=s.I*int((d-gap)%M==0)-s.I*int((d+gap)%M==0)
  coef=coef*amplitude(u,v)/(1 if fault=='omit_edge_normalization' else ce)
  want=s.I if (u,v)==(u0,v0) else -s.I if (u,v)==(v0,u0) else 0
  ck('Fourier_phase_edge_'+str(idx),coef==want)
 # Full local block extension, including states outside the hard wall.
 ladder=s.zeros(4)
 for n in range(1,4 if fault=='omit_hard_wall' else 3):ladder[n-1,n]=s.sqrt(n)
 hop=s.kronecker_product(ladder.H,ladder)+s.kronecker_product(ladder,ladder.H)
 num=s.diag(0,1,2,3);nt=s.kronecker_product(num,s.eye(4))+s.kronecker_product(s.eye(4),num)
 box=s.kronecker_product(s.diag(1,1,1,0),s.diag(1,1,1,0))
 ck('local_extension_number_conservation',nt*hop==hop*nt)
 ck('hard_wall_box_reduces',box*hop==hop*box)
 # SU(3) commutator reachability on an actual path; independent basis count.
 def E(i,j):m=s.zeros(3);m[i,j]=1;return m
 X01=E(0,1)+E(1,0);Y01=s.I*(E(0,1)-E(1,0));X12=E(1,2)+E(2,1);Y12=s.I*(E(1,2)-E(2,1))
 basis=[s.I*x for x in [X01,Y01,X12,Y12]]
 basis += [basis[0]*basis[1]-basis[1]*basis[0],basis[2]*basis[3]-basis[3]*basis[2],basis[0]*basis[2]-basis[2]*basis[0],basis[0]*basis[3]-basis[3]*basis[0]]
 ck('edge_lie_su3_dimension',s.Matrix.hstack(*(s.Matrix(x).reshape(9,1) for x in basis)).rank()==8)
 ck('all_generators_traceless_skew',all(x.trace()==0 and x.H==-x for x in basis))
 # Isometry first column preserved while unprescribed complement adjusts det.
 U=s.Matrix([[s.Rational(3,5),s.Rational(4,5)],[s.Rational(4,5),-s.Rational(3,5)]])
 completed=U if fault=='wrong_completion' else U*s.diag(1,-1)
 ck('completion_preserves_input',completed[:,0]==U[:,0]);ck('completion_special_unitary',completed.H*completed==s.eye(2) and completed.det()==1)
 # Passive two-boson amplitude tested as an actual symmetric tensor lift.
 for p in [s.Rational(0),s.Rational(1,5),s.Rational(1,2),s.Rational(4,5),s.Rational(1)]:
  amp=s.sqrt(2*p*(1-p));prob=(4 if fault=='wrong_passive_factor' else 2)*p*(1-p)
  ck('passive_probability_'+str(p),s.simplify(amp**2-prob)==0);ck('passive_bound_'+str(p),prob<=s.Rational(1,2))
 # Pulse area and smooth joins are integrated/differentiated, not assumed.
 t,T,theta=s.symbols('t T theta',positive=True);h=(1 if fault=='wrong_pulse_area' else 2)*theta/T*s.sin(s.pi*t/T)**2
 ck('pulse_area',s.integrate(h,(t,0,T))==theta)
 ck('pulse_C1_joins',all(s.simplify(f.subs(t,x))==0 for f in [h,s.diff(h,t)] for x in [0,T]))
 # Actual invariant joint state may contain degeneracy coherence, but partial
 # trace contains no local charge coherence. Add asymmetric target as countercontrol.
 rho=s.zeros(4);rho[1,1]=rho[2,2]=s.Rational(1,2);rho[1,2]=rho[2,1]=s.Rational(1,2)
 N=s.diag(0,1,1,2);red=s.Matrix([[sum(rho[2*i+j,2*k+j] for j in range(2)) for k in range(2)] for i in range(2)])
 ck('degenerate_joint_invariance',N*rho==rho*N);ck('battery_marginal_invariance',red*s.diag(0,1)==s.diag(0,1)*red)
 plus=s.ones(2)/2;ck('coherent_stock_not_invariant',plus*s.diag(0,1)!=s.diag(0,1)*plus)
 # Full detector error with rational pi upper bound, not binary statistics.
 Q=15999999;R=5183999998;L=99999999999999
 e=F(1,2000)+F(1,4000)+F(Q+R,L+1)*F(22,7)
 ck('ten_call_compiled_error',10*e+F(2,10000)<F(934,100000))
 dQ=(Q+1)*(Q+2)//2;neutral=2*(dQ+1);H=R+L-1+Q
 ck('actual_input_dimension',dQ==128000008000000)
 ck('actual_neutral_dimension',neutral==256000016000002)
 ck('actual_battery_capacity',H==100005199999995)
 ck('actual_feature_count',2*3+3+neutral+3*neutral==9+4*neutral)
 ck('Lambda_geometric_bound',max(D.values())<=4*(base**len(features(vertices[0]))-1)//(base-1))
 dims=[sum(sum(z[:-1])==n for z in vertices) for n in range(sum(caps)+1)]
 ck('shell_cube_budget',sum(x**3 for x in dims)<=len(vertices)**3)
 return out
RESULT='K2264'
REPORT='lab/process/k2264-restricted-detector-control.json'
DEPS=['explorations/conditional-build/k2264-restricted-detector-control-2026-10-29.md','explorations/conditional-build/k2253-full-instrument-reference-reuse-2026-10-29.md','explorations/conditional-build/k2262-coherent-reference-supply-2026-10-29.md']

def main():
 import argparse,hashlib,json
 from pathlib import Path
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
 root=Path(__file__).resolve().parents[2];checks=controls()
 assert all(checks.values()),[k for k,v in checks.items() if not v]
 faults={}
 for f in FAULTS:
  failed=[k for k,v in controls(f).items() if not v]
  assert failed,('undetected changed input',f)
  faults[f]=failed
 report=dict(result_id=RESULT,checks=checks,fault_failures=faults,evidence_kinds='Finite exact controls only. Universal analytic and control statements are written proofs; report hashes are provenance.',dependency_sha256={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in DEPS},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
 p=root/REPORT
 if args.write:p.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(p.read_text())==report,'report drift'
 print(json.dumps(dict(result=RESULT,controls=len(checks),faults=len(faults))))
if __name__=='__main__':main()
