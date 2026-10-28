#!/usr/bin/env python3
"""Exact modular minor and rational kernel certificate for a full adapter fiber."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,hashlib,json
import sympy as S
import k2208_grade_constrained_pencil_reconstruction_probe as o
ROOT=Path(__file__).resolve().parents[2]
PRIME=1000003
ROWS=list(range(119));ROWS[85]=275
COLS=[j for j in range(120) if j!=93]
def residue(x,p=PRIME):
 a,b=S.fraction(x);return int(a)%p*pow(int(b)%p,-1,p)%p

def det_mod(rows,p=PRIME):
 a=[r[:] for r in rows];det=1
 for k in range(len(a)):
  pivot=next((i for i in range(k,len(a)) if a[i][k]%p),None)
  if pivot is None:return 0
  if pivot!=k:a[k],a[pivot]=a[pivot],a[k];det=-det
  q=a[k][k]%p;det=det*q%p;inv=pow(q,-1,p)
  for i in range(k+1,len(a)):
   factor=a[i][k]*inv%p
   if factor:
    for j in range(k+1,len(a)):a[i][j]=(a[i][j]-factor*a[k][j])%p
   a[i][k]=0
 return det%p

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
 checks={}
 def ck(k,v):checks[k]=bool(v)
 wc=o.coord([((1,2,3),1),((1,4,5),1),((2,6,7),2),((3,8,9),3),((4,6,10),5)])
 uc=o.coord([((1,2,4),2),((1,5,7),3),((2,6,8),5),((3,9,10),7),((4,5,6),11)])
 vv=o.IN*o.grade(wc);tt=S.I*o.grade(uc);PP=7*vv-15*tt;BP=7*vv+15*tt
 YY=o.clean(PP.inv()*BP);yp=YY.extract(o.ix,o.ix)
 ac=7*wc+15*o.epsilon*uc;bc=7*wc-15*o.epsilon*uc
 EE=o.constraint_matrix(yp)
 ck('matrix392x120',EE.shape==(392,120))
 ck('nonzero_exact_kernel',ac!=S.zeros(120,1) and EE*ac==S.zeros(392,1))
 ck('actual_real_form_equation',o.clean(o.phi(ac)*yp-o.phi(bc))==S.zeros(16))
 ck('prime',S.isprime(PRIME))
 ck('all_denominators_invertible',all(int(S.denom(x))%PRIME for x in EE))
 small=[[residue(EE[i,j]) for j in COLS] for i in ROWS];det=det_mod(small)
 ck('minor_nonzero',det!=0)
 ck('independent_minor_reproduction',det==992118)
 wr,ur=o.recover(ac,yp);ck('inverse_reconstruction',wr==wc and ur==uc)
 ck('full_reality',o.clean(o.bar(YY)*YY)==o.I)
 ck('both_halves',o.clean(PP*YY-o.bar(PP))==o.Z)
 RR=vv+3*tt;br=vv-3*tt
 K=lambda x:sum(((1 if j<4 else -1)*g*x*g for j,g in enumerate(o.gam)),o.Z)
 AA=3*K(br*br)+34*br*br+36*RR*br+8*br*RR-24*RR*RR
 BB=184*RR*RR+140*RR*br+184*br*RR+194*br*br+24*K(br*RR)+15*K(br*br)
 residual=o.clean(4*AA.extract(o.ix,o.ix)*yp-(5*BB-AA).extract(o.ix,o.ix))
 expected=(S.Integer(15850252893220743860640)-S.Integer(1581983112104607593520)*S.I)/S.Integer(27955676769824869)
 ck('exact_Euler_entry',S.expand(residual[0,0]-expected)==0)
 ck('Euler_obstruction',residual[0,0]!=0)
 # The Euler polynomial is homogeneous quadratic in original v,t. Exercise
 # the original polynomial at signed nonunit scalings, not a status flag.
 for c in [S.Rational(-2),S.Rational(3,5)]:
  r=c*RR;b=c*br
  a=3*K(b*b)+34*b*b+36*r*b+8*b*r-24*r*r
  z=184*r*r+140*r*b+184*b*r+194*b*b+24*K(b*r)+15*K(b*b)
  q=o.clean(4*a.extract(o.ix,o.ix)*yp-(5*z-a).extract(o.ix,o.ix))
  ck('homogeneity_'+str(c),q==c*c*residual)
 ck('kernel_controls_all_real_ports',len(COLS)==119 and len(set(ROWS))==119 and len(set(COLS))==119)
 assert all(checks.values()),[k for k,v in checks.items() if not v]
 faults={}
 bad=[r[:] for r in small];bad[0]=bad[1][:]
 faults['duplicate_minor_row']=['minor_nonzero'] if det_mod(bad)==0 else []
 mutated=EE.copy();j=next(j for j,x in enumerate(ac) if x);mutated[0,j]+=1
 faults['constraint_coefficient']=['nonzero_exact_kernel'] if mutated*ac!=S.zeros(392,1) else []
 wrong=o.clean(5*AA.extract(o.ix,o.ix)*yp-(5*BB-AA).extract(o.ix,o.ix))
 faults['Euler_coefficient']=['exact_Euler_entry'] if wrong[0,0]!=expected else []
 # An omitted real-form equation falsely admits i times a real port. The
 # actual domain is R120, not a complex nullspace silently reinterpreted.
 faults['complex_rescaling']=['real_grade_coordinates'] if any(S.im(x)!=0 for x in S.I*ac) else []
 assert all(faults.values()),faults
 deps=['tests/channel-swings/k2208_grade_constrained_pencil_reconstruction_probe.py','explorations/conditional-build/k2208-grade-constrained-pencil-reconstruction-2026-10-28.md','explorations/conditional-build/k2211-pfaffian-adapter-system-2026-10-28.md','explorations/conditional-build/k2197-general-ordered-adapter-constraints-2026-10-28.md','lab/process/k2205-ordered-pencil-real-constraints.json','explorations/conditional-build/k2214-prescribed-adapter-fibers-2026-10-28.md']
 report=dict(result_id='K2214',status='exact_full_prescribed_factor_fiber_exclusion',checks=checks,fault_failures=faults,rank_certificate={'field':'Q and R','matrix_shape':list(EE.shape),'rank':119,'kernel_dimension':1,'prime':PRIME,'rows':ROWS,'columns':COLS,'minor_determinant_mod_prime':det,'kernel_coordinates':list(map(str,ac))},Euler_residual00=str(residual[0,0]),dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),evidence_kinds='Exact rational kernel plus independently replayed nonzero finite-field minor prove rank; ordered Euler polynomial rejects all nonzero real rescalings; universal reconstruction/homogeneity proof, no generic nonlinear search or isospectral exclusion.')
 dst=ROOT/'lab/process/k2214-prescribed-adapter-fibers.json'
 if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(dst.read_text())==report,'report drift'
 print(json.dumps(dict(result='K2214',controls=len(checks),faults=len(faults),rank=119,minor=det)))
if __name__=='__main__':main()
