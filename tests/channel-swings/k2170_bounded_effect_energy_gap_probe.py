#!/usr/bin/env python3
"""Fraction-only finite-budget certificates and independent symbolic controls."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import sympy as S
from k2168_finite_budget_moment_envelope_probe import IV,ll,sqrtq
ROOT=Path(__file__).resolve().parents[2];N=F(1,3);Z=F(1,4);DELTA=F(1,2);C=F(40,3);QLOW=F(2,3)
def rho(w,delta=DELTA):return (N*w+N*delta)/((N+1)*w+N*delta)
def epsilon(a,b,L,delta=DELTA,fault=None):
 low,high=rho(b,delta),rho(a,delta)
 U=Z**L/a;V=low**L
 if fault=='wrong_tail':U=Z**(L+1)/a
 if U>=V:return F(0)
 return a*(1-high)**2*(V-U)**2/(16*(V+U-2*U*V))
def controls(fault=None):
 out={};ck=lambda n,x:out.__setitem__(n,bool(x));n,r=S.symbols('n r',positive=True)
 vals=[F(2,5),F(1,4),F(1,3),F(1,7)];rr=F(3,5)
 w=sum(t*t for t in vals);m=sum(i*t*t for i,t in enumerate(vals));T=sum((i+1)*vals[i]*vals[i+1] for i in range(len(vals)-1))
 residual=sum((i+1)*((vals[i+1] if i+1<len(vals) else 0)-rr*vals[i])**2 for i in range(len(vals)))
 if fault=='shift_orientation':residual=sum((i+1)*(vals[i] -rr*(vals[i+1] if i+1<len(vals) else 0))**2 for i in range(len(vals)))
 ck('weighted_shift_residual_finite_identity',residual==m+rr*rr*(m+w)-2*rr*T)
 # Infinite geometric sums evaluated symbolically, with n=J+1+k for tail.
 z=S.symbols('z',positive=True);J=S.symbols('J',integer=True,positive=True)
 tail=(1-z)*z**(J+1)/(1-z)**2
 if fault=='tail_off_by_one':tail*=z
 ck('exact_tail_moment_excess',S.simplify(tail-z/(1-z)*z**J)==0)
 # SS*=I for backward shift: inspect an interior finite compression, excluding last boundary.
 k=7;B=S.zeros(k,k)
 for i in range(k-1):B[i,i+1]=1
 A=B-S.Rational(3,5)*S.eye(k)
 product=A*A.T if fault!='shift_adjoint_order' else A.T*A
 expected=S.Rational(34,25)*S.eye(k)-S.Rational(3,5)*(B+B.T)
 ck('backward_shift_BBstar_identity_interior',product[:k-1,:k-1]==expected[:k-1,:k-1])
 # Exact zero-defect geometric control and threshold branch from geometric tails.
 rr=S.Rational(1,2);gg=S.sqrt(1-rr**2)*rr**n
 ck('geometric_kernel',S.simplify(gg.subs(n,n+1)-rr*gg)==0)
 w1=F(1,4);m1=N;t1=F(7,24)
 # sqrt(z) sum_(n>=1) (n+1)p_n = sqrt(z)*(N+1-p0).
 ck('threshold_actual_T',F(1,2)*(N+1-F(3,4))==t1)
 eta=sqrtq(m1*(m1+w1))-t1
 ck('threshold_deficit_dominates_uniform',eta.a>epsilon(F(1,8),F(1,2),6,fault=fault))
 lo=F(1,8);hi=F(1,2);U=Z**6/lo;V=rho(hi)**6
 ck('uniform_fixture_parameters',(rho(lo),rho(hi),U,V)==(F(5,8),F(2,5),F(1,512),F(64,15625)))
 margin=C*QLOW*epsilon(lo,hi,6,fault=fault)
 ck('exact_uniform_margin',margin==F(5997601,806912000000))
 q=F(3,4) if fault=='unjustified_squeeze' else QLOW
 ck('fourth_root_lower_certificate',q**4<F(9,41))
 # Cap-fidelity relaxed optimizer with r=3/4,z=1/4,t=1/2,K=3.
 R=F(9,16);t2=F(1,4);K=3;ww=t2*(1-R**K)+Z**K
 ck('cap_crossing_neighbors',t2*(1-R)*R**(K-1)<=(1-Z)*Z**(K-1) and t2*(1-R)*R**K>=(1-Z)*Z**K)
 direct_head=sum(S.sqrt(S.Rational(t2))*(1-S.Rational(R))*S.Rational(R)**i for i in range(K))
 tail_overlap=S.sqrt((1-S.Rational(Z))*(1-S.Rational(R)))*(S.sqrt(S.Rational(Z*R)))**K/(1-S.sqrt(S.Rational(Z*R)))
 formula=S.sqrt(S.Rational(ww-Z**K)/(1-S.Rational(R)**K))*(1-S.Rational(R)**K)+tail_overlap
 if fault=='cap_tail_denominator':formula=direct_head+tail_overlap*(1-S.sqrt(S.Rational(Z*R)))
 ck('exact_cap_overlap_geometric_tail',S.simplify(direct_head+tail_overlap-formula)==0)
 ck('cap_norm_exact',ww==sum(t2*(1-R)*R**i for i in range(K))+Z**K)
 return out
FAULTS=['shift_orientation','tail_off_by_one','shift_adjoint_order','wrong_tail','unjustified_squeeze','cap_tail_denominator']
def certificates(count=64):
 a,b=F(1,8),F(1,2);rows=[]
 for j in range(count):
  left=a+(b-a)*F(j,count);right=a+(b-a)*F(j+1,count);mid=(left+right)/2
  value,slope=ll(DELTA,mid)
  tangent=(value+slope*IV(left-mid,right-mid)).a
  choices=[(epsilon(left,right,L),L) for L in range(1,19)];eps,L=max(choices)
  bound=tangent+C*QLOW*eps
  rows.append(dict(left=str(left),right=str(right),tail_L=L,epsilon=str(eps),moment_lower=str(tangent),energy_lower=str(bound)))
 assert F(rows[0]['left'])==a and F(rows[-1]['right'])==b
 assert all(F(x['right'])==F(y['left']) for x,y in zip(rows,rows[1:]))
 lower=min(F(x['energy_lower']) for x in rows)
 assert lower>F('0.54324604')
 return dict(delta=str(DELTA),scope='exact contrast only; no monotonicity of actual optimum assumed',bins=rows,energy_lower=str(lower))
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();checks=controls();assert all(checks.values()),checks
 faults={}
 for f in FAULTS:
  bad=[n for n,p in controls(f).items() if not p];assert bad,('undetected',f);faults[f]=bad
 cert=certificates();margin=C*QLOW*epsilon(F(1,8),F(1,2),6)
 threshold=F('0.5423370097')+margin
 assert threshold>F('0.54234444248')
 deps=['explorations/conditional-build/k2170-bounded-effect-energy-gap-2026-10-27.md','tests/channel-swings/k2168_finite_budget_moment_envelope_probe.py','lab/process/k2168-finite-budget-moment-envelope.json','explorations/conditional-build/k2162-feedback-detector-frontier-2026-10-27.md']
 report=dict(result_id='K2170',status='conditional_exact_controls',checks=checks,fault_failures=faults,uniform_threshold=dict(delta_at_least='1/2',added_energy_lower=str(margin),energy_lower=str(threshold)),probability_partition=cert,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Independently reviewed shift-gap, cap-fidelity, uniform threshold and energy proofs; symbolic controls and rational covering certificates are not a detector optimizer or apparatus-cost theorem.')
 dest=ROOT/'lab/process/k2170-bounded-effect-energy-gap.json'
 if args.write:dest.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(dest.read_text())==report
 print(json.dumps(dict(result='K2170',checks=len(checks),faults=faults,uniform_threshold_display=float(threshold),partition_lower_display=float(F(cert['energy_lower'])))))
if __name__=='__main__':main()
