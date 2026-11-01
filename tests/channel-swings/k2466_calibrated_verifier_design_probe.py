"""Complete original block algebra and calibrated cost optimization, Arb256."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,sys
from flint import arb,ctx
ctx.prec=256
ROOT=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ctrl(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
def ar(v):
 v=F(v);return arb(v.numerator)/v.denominator
rp='lab/process/k2457-local-verifier-phase-design.json';data=json.loads((ROOT/rp).read_text())
ck('original_block_dependencies',all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in data['dependencies'].items()))
results=[];consumer=[];finite_designs=[]
for li,law in enumerate(data['original_laws']):
 tag=str(li);a=ar(F(law['a']));h=1/(2*(1+a));AA=h*(h+4)
 vals=[]
 for row in law['blocks']:
  t0=ar(F(row['trace']));d0=ar(F(row['det']));vals.append((t0+(t0*t0-4*d0).sqrt())/2)
 ell=vals[0];imax=0
 for j,v in enumerate(vals[1:],1):
  if v>ell:ell=v;imax=j
 row=law['blocks'][imax];target=[('3927/3302','569/1651'),('761/670','213/670')][li]
 ck('maximum_original_trace_det_'+tag,(row['trace'],row['det'])==target)
 for j,v in enumerate(vals):
  ck('all30_block_max_'+tag+'_'+str(j),v<ell or (law['blocks'][j]['trace'],law['blocks'][j]['det'])==target)
 ck('crossover_regime_'+tag,1-h<ell<1)
 qx=(ell-h)/(ell*ell+h*ell-h)
 def DD(q):return 1-6*h*q+AA*q*q
 def gg(q):return (1-h*q+DD(q).sqrt())/2
 def gp(q):return (-h+(-6*h+2*AA*q)/(2*DD(q).sqrt()))/2
 ck('crossover_original_'+tag,(gg(qx)-qx*ell).contains(0) and 0<qx<1)
 ck('strict_sqrt_convexity_'+tag,4*AA-36*h*h>0)
 qold=(3+(a/(1+a)).sqrt())/(4+h)
 ck('predecessor_optimum_left_'+tag,qold<qx)
 # All examples normalize by e^2: b's below are beta/e^2, so result is R/e^2.
 designs=[('common',F(1,2500),F(1,2500),F(2),F(2)),('unequal',F(1,50),F(2,25),F(2),F(2)),('crossover',F(1,5),F(0),F(2),F(2)),('cheap_T',F(0),F(0),F(100),F(1)),('no_margin',F(9,10),F(9,10),F(2),F(2))]
 for name,bQ,bT,kQ,kT in designs:
  k0=ar(kQ);k1=ar(kT-kQ);b0=ar(bQ);b1=ar(bT-bQ);uu=arb(1)/2-b0;vv=h/2-b1;ww=arb(1)/2
  LL=vv*k0-k1*uu;rr=-3*h*k1-AA*k0;ss=k1+3*h*k0
  def efficiency(q,zero_only=False):
   lam=gg(q)
   if not zero_only and q*ell>lam:lam=q*ell
   return (1-lam-b0-b1*q)/(k0+k1*q)
  def dh(q):return LL+ww*(rr*q+ss)/DD(q).sqrt()
  qa=LL*LL*AA-ww*ww*rr*rr;qb=-6*h*LL*LL-2*ww*ww*rr*ss;qc=LL*LL-ww*ww*ss*ss
  ck('nondegenerate_quadratic_'+tag+'_'+name,not qa.contains(0))
  discr=qb*qb-4*qa*qc
  roots=[]
  if discr>0:
   for sign in [-1,1]:
    q=(-qb+sign*discr.sqrt())/(2*qa)
    if 0<q<1 and LL*(rr*q+ss)<0:
     ck('unsquared_exact_sign_'+tag+'_'+name+'_'+str(sign),LL*(rr*q+ss)<0)
     ck('root_reproduction_'+tag+'_'+name+'_'+str(sign),(LL*DD(q).sqrt()+ww*(rr*q+ss)).contains(0))
     roots.append(q)
  candidates=[('Q',arb(0)),('crossover',qx),('T',arb(1))]+[('stationary',q) for q in roots if q<qx]
  cand=[(label,q,efficiency(q)) for label,q in candidates];best=cand[0]
  for row0 in cand[1:]:
   if row0[2]>best[2]:best=row0
  label,qstar,theta=best;stamp=tag+'_'+name
  for label0,q0,r0 in cand:ck('candidate_bound_'+stamp+'_'+label0,r0<theta or (r0-theta).contains(0))
  if label=='stationary':ck('unsquared_stationary_'+stamp,dh(qstar).contains(0))
  if name=='common':ck('old_equal_error_optimum_'+tag,(qstar-qold).contains(0))
  if name=='crossover':
   ck('crossover_selected_'+tag,label=='crossover')
   bad=next(q for q in roots if q>qx)
   ctrl('zero_block_only_overclaims_'+tag,efficiency(bad,True)>theta and efficiency(bad)<theta)
  if name=='cheap_T':ck('endpoint_selected_'+tag,label=='T')
  if name=='no_margin':ck('no_positive_margin_'+tag,theta<0)
  # Grid points are contrary/finiteness controls, NOT evidence for global optimality.
  for j in [0,1,5,10,15,19,20]:
   qr=ar(F(j,20));v0=efficiency(qr)
   ck('finite_original_comparison_'+stamp+'_'+str(j),v0<theta or (v0-theta).contains(0))
  if name=='unequal':
   ctrl('common_beta_weight_is_wrong_'+tag,efficiency(qold)<theta)
   # Unique active original zero-block eigenvector gives unequal-error dual.
   p0=1-qstar;g0=gg(qstar);m00=p0+qstar*a/(1+a);m01=qstar*(a/2).sqrt()/(1+a);m11=qstar/(2*(1+a));vx=m01;vy=g0-m00;norm=vx*vx+vy*vy
   xQ=vx*vx/norm;xT=(a/(1+a)*vx*vx+2*(a/2).sqrt()/(1+a)*vx*vy+vy*vy/(2*(1+a)))/norm
   ck('unique_bottleneck_'+tag,qstar*ell<g0 and p0<g0)
   ck('dual_Q_'+tag,((1-xQ-b0)/k0-theta).contains(0))
   ck('dual_T_'+tag,((1-xT-ar(bT))/ar(kT)-theta).contains(0))
   betaE=ar(F(1,100));crit=(1-betaE)/theta
   for factor in [F(3,4),F(1),F(5,4)]:
    added=(1-betaE)/(crit*ar(factor));difference=added-theta
    ck('sharp_unrestricted_threshold_'+tag+'_'+str(factor),difference>0 if factor<1 else (difference.contains(0) if factor==1 else difference<0))
   # Real output units: beta_j=e² times normalized errors; same bound premises.
   e=F(2499,500000);cal=ar(e*e)*(b0+b1*qstar);nu=1-g0;margin=ar(e*e)*nu-cal
   c=arb(2).log();Ls=c-ar(F(1,2));gam=(1+Ls)**2/(2*Ls);num=arb(20).log()+gam*ar(F(1,1000000));nreal=num/(c*margin);N=int(nreal.upper().ceil().unique_fmpz())
   ck('composed_use_rounding_'+tag,N>=nreal and N-1<nreal)
   ck('composed_positive_success_'+tag,ar(F(1,4))-(2*((num/(c*N)+cal)/nu).sqrt()+ar(F(1,1000000)))>0)
   cost=ar(N)*(k0+k1*qstar)
   consumer.append({'law':law['a'],'uses':N,'expected_cost':str(cost),'calibration':str(cal),'gap':str(nu),'normalized_efficiency':str(theta),'threshold_cost_for_error_e2_over100':str(crit)})
  results.append({'law':law['a'],'design':name,'bQ_over_e2':str(bQ),'bT_over_e2':str(bT),'kQ':str(kQ),'kT':str(kT),'chosen':label,'T_weight':str(qstar),'R_over_e2':str(theta),'crossover':str(qx),'ell':str(ell),'candidate_count':len(cand)})
 # Released exact finite-count optimization on the SAME two original carriers.
 # Rational confidence-to-margin constant100; normalized branch errors and costs supplied.
 b0=ar(F(1,50));b1=ar(F(3,50));k0=arb(2);k1=arb(1);budget=100
 uu=arb(1)/2-b0;vv=h/2-b1;ww=arb(1)/2
 LL=vv*k0-k1*uu;rr=-3*h*k1-AA*k0;ss=k1+3*h*k0
 qa=LL*LL*AA-ww*ww*rr*rr;qb=-6*h*LL*LL-2*ww*ww*rr*ss;qc=LL*LL-ww*ww*ss*ss
 discr=qb*qb-4*qa*qc;cont_roots=[]
 for sign in [-1,1]:
  q=(-qb+sign*discr.sqrt())/(2*qa)
  if 0<q<qx and LL*(rr*q+ss)<0:cont_roots.append(q)
 ck('finite_continuous_interior_'+tag,len(cont_roots)==1)
 qcont=cont_roots[0]
 def margin(q):
  gval=gg(q)
  if q*ell>gval:gval=q*ell
  return 1-gval-b0-b1*q
 incumbent_n=int((arb(budget)/margin(qcont)).upper().ceil().unique_fmpz())
 incumbent=arb(incumbent_n)*(k0+k1*qcont)
 # Conservatively enumerate from1. kmin=2 proves counts above floor(incumbent/2) cannot win.
 nmax=int((incumbent/2).upper().floor().unique_fmpz());best=(incumbent,incumbent_n,qcont,'continuous_weight');feasible=0;finite_candidates=[best];branches_certified=True
 for N in range(1,nmax+1):
  th=arb(budget)/N;ends=[]
  for label,q in [('Q',arb(0)),('cross',qx),('T',arb(1))]:
   branches_certified &= not (margin(q)-th).contains(0)
   if margin(q)>th:ends.append((q,label))
  # Exact zero-branch equality: positive RHS removes the square-root sign ambiguity.
  aa=4*vv*vv-AA;bb=8*(uu-th)*vv+6*h;cc0=4*(uu-th)**2-1;ds=bb*bb-4*aa*cc0
  branches_certified &= not ds.contains(0) and not aa.contains(0)
  if ds>0:
   for sign in [-1,1]:
    q=(-bb+sign*ds.sqrt())/(2*aa)
    branches_certified &= all(not z.contains(0) for z in (q,q-qx,uu-th+vv*q))
    if 0<q<qx and 2*(uu-th+vv*q)>0:
     ck('finite_root_sign_'+tag+'_'+str(N)+'_'+str(sign),2*(uu-th+vv*q)>0)
     ends.append((q,'zero_equality'))
  qr=(1-b0-th)/(ell+b1)
  branches_certified &= not (ell+b1).contains(0) and not (qr-qx).contains(0) and not (qr-1).contains(0)
  if qx<qr<1:ends.append((qr,'nonzero_equality'))
  if not ends:continue
  feasible+=1
  # Increasing positive cost selects the smallest feasible q.
  q,label=ends[0]
  for q2,label2 in ends[1:]:
   branches_certified &= not (q2-q).contains(0)
   if q2<q:q,label=q2,label2
  cost=arb(N)*(k0+k1*q)
  finite_candidates.append((cost,N,q,label))
  if cost<best[0]:best=(cost,N,q,label)
 cost,N,q,label=best
 ck('finite_candidate_branches_decided_'+tag,branches_certified)
 ck('finite_all_counts_certified_'+tag,all(c0>cost or (n0==N and lab0==label) for c0,n0,q0,lab0 in finite_candidates))
 ck('finite_integer_cost_improves_'+tag,cost<incumbent)
 ctrl('continuous_weight_not_finite_winner_'+tag,q<qcont and cost<incumbent)
 ck('finite_solution_equality_branch_'+tag,label=='zero_equality')
 ck('finite_boundary_reproduction_'+tag,(margin(q)-arb(budget)/N).contains(0))
 ck('finite_no_smaller_count_at_same_weight_'+tag,margin(q)<arb(budget)/(N-1))
 ck('finite_tail_exhaustion_'+tag,arb(nmax+1)*2>incumbent)
 finite_designs.append({'law':law['a'],'normalized_budget':budget,'errors':['1/50','2/25'],'costs':[2,3],'continuous_weight':str(qcont),'continuous_weight_rounded_count':incumbent_n,'continuous_weight_cost':str(incumbent),'finite_optimal_count':N,'finite_optimal_T_weight':str(q),'finite_expected_cost':str(cost),'counts_exhausted':nmax,'feasible_counts':feasible,'exact_endpoint':'positive-sign zero-block quadratic with margin=100/N'})
# Actual covariance-independent cost reweighting bijection on a finite simplex.
p=[F(1,4),F(1,3),F(5,12)];costs=[F(2),F(3),F(7)];den=sum(x*y for x,y in zip(p,costs));x=[pj*kj/den for pj,kj in zip(p,costs)];back=[xx/kk/sum(y/k for y,k in zip(x,costs)) for xx,kk in zip(x,costs)]
ck('cost_simplex_bijection',sum(x)==1 and back==p)
tail=sum(F(1,2**j) for j in range(3,15))+F(1,2**14)
ck('geometric_cost_tail',tail==F(1,4))
ctrl('mean_not_deterministic_cost',tail>0)
# Actual Bell projector has partial-transpose eigenvalue -1/2, so is not a product effect.
import sympy as sp
Pbell=sp.Matrix([[1,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,1]])/2
PT=sp.zeros(4)
for i in range(2):
 for j in range(2):
  for k in range(2):
   for l in range(2):PT[2*i+l,2*k+j]=Pbell[2*i+j,2*k+l]
ctrl('unrestricted_projector_can_be_nonlocal',min(PT.eigenvals())<0)
note='explorations/conditional-build/k2466-calibrated-verifier-design-2026-11-01.md';deps=[note,str(Path(__file__).relative_to(ROOT)),rp,'explorations/conditional-build/k2463-local-verifier-calibration-2026-11-01.md','lab/process/k2465-sharp-leakage-compensator.json']
report={'result_id':'K2466','checks':checks,'controls':controls,'original_full_carrier_designs':results,'prospective_original_consumers':consumer,'finite_count_designs':finite_designs,'evidence_kinds':{'universal':'exact piecewise-spectrum algebraic optimizer and calibrated effect-cost minimax dual','finite':'all30 original blocks per law and rigorous algebraic candidate comparison','ceiling':'continuous and finite sufficient expected-cost objectives; no measured device or universal local optimum'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2466-calibrated-verifier-design.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2466',len(checks),'checks',len(controls),'controls PASS');print(json.dumps(consumer))
