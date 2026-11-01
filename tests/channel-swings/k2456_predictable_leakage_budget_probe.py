"""Exact adaptive histories and interval consumers; universal proof is in the note."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import hashlib,json,sys
from flint import arb,ctx
ctx.prec=256
ROOT=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,b):
 checks[k]=bool(b)
 if not b:raise AssertionError(k)
def ctrl(k,b):
 controls[k]=bool(b)
 if not b:raise AssertionError(k)
def A(x):
 x=F(x);return arb(x.numerator)/x.denominator
def parameters(a,b,eta,pi):
 d=max(F(0),b-a);q=a+(1-eta)*d;delta=eta*d;h=b-delta
 v=(a-q)**2/(q*(1-q)) if 0<q<1 else F(0)
 assert q>=h and 0<=h<=1-delta and ((0<q<1) or q==a)
 return q,delta,h,v,1+pi*v
# Exact scalar inequalities over genuine endpoint and interior configurations.
for i,(a,b,eta,pi) in enumerate(product([F(0),F(1,4),F(1,2),F(1)],[F(0),F(1,3),F(1)],[F(1,3),F(1,2)],[F(1,3),F(1,2)])):
 q,de,h,v,D=parameters(a,b,eta,pi);L=1-de
 ck('conditional_second_moment_'+str(i), (1-pi)+pi*(a*a/q+(1-a)**2/(1-q))==D if 0<q<1 else D==1)
 c=(1+A(pi*F(3,4)*L/(1-pi))).log()/A(L)
 actual=A(1-pi)*(c*A(h)/2).exp()+A(pi*((1-a)+a/F(2)))
 # Equality configurations handled exactly; interval comparisons are strict otherwise.
 ck('actual_multiplier_'+str(i),actual/(A(D).sqrt())<1 if a!=b or 0<b<1 else actual.contains(1) or actual<1)
 ck('residual_cost_bound_'+str(i),de*de<=eta**2*v/(4*(1-eta)**2))
 if a>=b:ck('harmless_cost_'+str(i),q==a and de==v==0)
q,de,h,v,D=parameters(F(0),F(1),F(1,2),F(1,2))
ck('endpoint_support_safe',q==F(1,2) and v==1 and de==F(1,2))
actual_pass=1-F(0);old_reference_pass=1-F(1);new_reference_pass=1-q
ctrl('unsmoothed_endpoint_support_fails',actual_pass>0 and old_reference_pass==0 and new_reference_pass>0)
ctrl('omitted_moment_budget_fails',(A(F(3,2)).sqrt()+1)/2>1)
# If one also drops residual delta, the corrected proposed multiplier fails.
ctrl('omitted_residual_fails',(A(F(3,2))+1)/(2*A(F(3,2)).sqrt())>1)
ctrl('persistent_budget_not_bounded',D**20>D**10>1)
# Full adaptive tree: b endpoints make squared e-process multipliers rational.
alpha=F(3,4);depthmax=7;nodes=0;mass=F(0);cross=F(0);maxmean=[arb(0) for _ in range(depthmax+1)];crosses=0
stack=[(0,F(1),F(1),0,0,False,F(1),F(0),F(0))]
while stack:
 n,prob,S,uses,fails,hit,prodD,sumv,sumdelta=stack.pop();nodes+=1
 maxmean[n]+=A(prob)*A(S).sqrt()
 if n==depthmax:
  mass+=prob
  if hit:cross+=prob;crosses+=1
  continue
 pi=F(1,2) if (uses+fails)%2==0 else F(1,3)
 eta=F(1,2);b=F(1) if (n+uses)%3 else F(0);a=[F(0),F(1,4),F(1,2),F(1)][(2*uses+fails+n)%4]
 q,de,h,v,D=parameters(a,b,eta,pi)
 ec=1+pi*F(3,4)*(1-de)/(1-pi) if b==1 else F(1)
 # m_Q expectation directly on this actual history, before any path propagation.
 ck('auxiliary_chord_node_'+str(nodes),(1-pi)*ec+pi*(1-q+q/F(4))<=1)
 for probbranch,mult,used,fail in [(1-pi,ec/D,1,0),(pi*(1-a),1/D,0,0),(pi*a,F(1,4)/D,0,1)]:
  if not probbranch:continue
  ns=S*mult;np=prob*probbranch;pd=prodD*D;sv=sumv+v;sd=sumdelta+used*de
  # Varying pi has no constant-pi corollary; use pi_min=1/3 here.
  ck('product_budget_node_'+str(nodes)+'_'+str(used)+'_'+str(fail),pd>=1+F(1,3)*sv)
  stack.append((n+1,np,ns,uses+used,fails+fail,hit or ns>=1/alpha**2,pd,sv,sd))
ck('adaptive_total_mass',mass==1)
ck('nonvacuous_crossing',0<cross<=alpha and crosses>0)
for n in range(1,depthmax+1):ck('adaptive_mean_nonincrease_'+str(n),(maxmean[n]-maxmean[n-1]).contains(0) if n==1 else maxmean[n]<maxmean[n-1])
# Transparent exact endpoint values for zero-failure process; failure is absorbing.
failed=F(1)
for multiplier in (F(3,2),F(0),F(13,7),F(7,3),F(5,2)):
 failed*=multiplier
ck('zero_failure_absorbing',failed==0)
reset=F(1)
for multiplier in (F(13,7),F(7,3),F(5,2)):reset*=multiplier
ctrl('forbidden_reset_false_crossing',failed<1/alpha**2 and reset>1/alpha**2)
# Original prospective K2454 consumers with outward-rounded Arb arithmetic.
fixtures=[]
for law,r in enumerate([F(27,127),F(15,67)],1):
 nu=(1-A(r).sqrt())/2;B=arb('1e-6');aa=((B.exp()-1)*2).sqrt()/2
 H=(B+2*arb(20).log())/arb(2).log();tau=arb('.01');kap=arb('1e-6');beta=arb('1e-8');den=nu*((tau-4*kap)/2)**2-beta
 ck('consumer_positive_'+str(law),den>0)
 root=((aa+(aa*aa+4*den*H).sqrt())/(2*den))**2
 N=int(root.upper().ceil().unique_fmpz())
 def allowance(n):return 2*((aa/arb(n).sqrt()+H/n+beta)/nu).sqrt()+4*kap
 ck('consumer_target_'+str(law),allowance(N)<=tau)
 ck('consumer_positive_actual_success_'+str(law),((aa/arb(N).sqrt()+H/N+beta)/nu).sqrt()/2+kap<arb(1)/4)
 ctrl('consumer_previous_count_'+str(law),allowance(N-1)>tau)
 fixtures.append({'law':law,'gap':str(nu),'actual_uses':N,'allowance':str(allowance(N)),'B':'1e-6','cost_kind':'prospective externally supplied all-prefix bound'})
# Report identities pin only the actual consumed source/claims, no predecessor replay.
deps=[str(Path(__file__).relative_to(ROOT)),'explorations/conditional-build/k2456-predictable-leakage-budget-2026-11-01.md','explorations/conditional-build/k2453-use-reference-information-budget-2026-11-01.md','explorations/conditional-build/k2450-route-leakage-certificate-2026-11-01.md','lab/process/k2454-two-setting-local-verifier.json']
report={'result_id':'K2456','checks':checks,'controls':controls,'adaptive_tree':{'depth':depthmax,'nodes':nodes,'crossing_probability':str(cross),'alpha':str(alpha),'crossing_leaves':crosses},'prospective_consumers':fixtures,'evidence_kinds':{'universal':'written one-step conditional Cauchy-Schwarz, chord and actual-use cost conversion','finite':'exact adaptive rational tree with real crossing event and endpoint/cost controls','prospective':'Arb256 hypothetical consumer; no measured data'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2456-predictable-leakage-budget.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2456',len(checks),'checks',len(controls),'controls PASS',fixtures)
