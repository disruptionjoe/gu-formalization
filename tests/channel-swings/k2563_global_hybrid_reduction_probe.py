"""Exact hybrid error identities and actual-law interval controls; universal proof in note."""
from pathlib import Path
from fractions import Fraction as F
import sympy as s
import hashlib,json,sys
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(n,v):
 checks[n]=bool(v)
 if not v:raise AssertionError(n)
def ct(n,v):
 controls[n]=bool(v)
 if not v:raise AssertionError('contrary: '+n)
x=s.symbols('x',nonnegative=True);g=(1-x)**2/(2*(1+x))
ck('g_derivative',s.simplify(s.diff(g,x)-(s.Rational(1,2)-2/(1+x)**2))==0)
ck('g_second_derivative',s.simplify(s.diff(g,x,2)-4/(1+x)**3)==0)
ck('g_endpoints',g.subs(x,0)==s.Rational(1,2) and g.subs(x,1)==0)
ck('g_Lipschitz_endpoints',s.diff(g,x).subs(x,0)==-s.Rational(3,2) and s.diff(g,x).subs(x,1)==0)
a=s.symbols('a',nonnegative=True)
ck('log_lower_derivative',s.simplify(s.diff(s.log(1+a)-a+a*a/2,a)-a*a/(1+a))==0)
ck('log_upper_derivative',s.simplify(s.diff(a-s.log(1+a),a)-a/(1+a))==0)
S,m,N=s.symbols('S m N',positive=True)
ck('largest_atom_tail_square',s.expand(S*S/(4*N)-m*(S-N*m)-(S-2*N*m)**2/(4*N))==0)
ck('tail_square_equality_fixture',N*(S/(2*N))**2==S*S/(4*N))
ct('arbitrary_retention_breaks_bound',F(2,5)**2>F(1,2)**2/4)
B,e,p0=s.symbols('B e p0',positive=True)
ck('budget_mix_error',s.simplify(1-(B/(B+e)+e*p0/(B+e))-e*(1-p0)/(B+e))==0)
u=s.symbols('u',positive=True);rstar=2/s.sqrt(1+2*u)-1;q=2*s.sqrt(1+2*u)-2-u
ck('continuum_feedback_minimizer',s.simplify(s.diff(g,x).subs(x,rstar)+u)==0)
ck('continuum_feedback_value',s.simplify(g.subs(x,rstar)+u*rstar-q)==0)
ck('continuum_feedback_boundary',q.subs(u,s.Rational(3,2))==s.Rational(1,2) and rstar.subs(u,s.Rational(3,2))==0)
ck('continuum_feedback_origin',q.subs(u,0)==0 and rstar.subs(u,0)==1)
# Rational interval operations, with rigorous atanh-series logarithm tails.
class I:
 def __init__(self,lo,hi=None):self.lo=F(lo);self.hi=F(lo if hi is None else hi)
 def __add__(self,v):v=cv(v);return I(self.lo+v.lo,self.hi+v.hi)
 __radd__=__add__
 def __neg__(self):return I(-self.hi,-self.lo)
 def __sub__(self,v):return self+-cv(v)
 def __rsub__(self,v):return cv(v)+-self
 def __mul__(self,v):
  v=cv(v);z=[self.lo*v.lo,self.lo*v.hi,self.hi*v.lo,self.hi*v.hi];return I(min(z),max(z))
 __rmul__=__mul__
 def __truediv__(self,v):
  v=cv(v);assert not v.lo<=0<=v.hi;return self*I(1/v.hi,1/v.lo)
 def __rtruediv__(self,v):return cv(v)/self
 def __pow__(self,n):
  assert n>=0;out=I(1)
  for _ in range(n):out=out*self
  return out
def cv(x):return x if isinstance(x,I) else I(x)
def log1p(x):
 x=F(x);assert x>=0;t=x/(2+x);M=32
 lo=2*sum((t**(2*k+1)/F(2*k+1) for k in range(M)),F(0))
 return I(lo,lo+2*t**(2*M+1)/(F(2*M+1)*(1-t*t)))
def w(a,b):
 if a==b:return I(0)
 return log1p((b-a)**2/(2*(a+b)*(2-a-b)))
def stage(a,b):
 E=1/(1+a);c=2*E*w(a,b)
 if a==0:return c,I(b/2),I(0)
 r=log1p(a)/b;j=(1-r)**2/(2*(1+r))*a/(1+a)/r
 return c,j,r
fixtures=[(F(0),F(1,2)),(F(1,2),F(1,2)),(F(1,10),F(2,5)),(F(349,2000),F(3,10)),(F(21,5000),F(1,100))]
for i,(a,b) in enumerate(fixtures):
 c,j,r=stage(a,b);d=j-c
 ck('actual_stage_lower_error_'+str(i),d.lo>=-b*b/2)
 ck('actual_stage_upper_error_'+str(i),d.hi<=b*b)
 if a>0:ck('hazard_ratio_bound_'+str(i),r.lo>=0 and r.hi<=1 and (I(a/b)-r).hi<=b/2)
c,j,r=stage(F(1,2),F(1,2));ct('free_atom_continuum_cost_increase',c.lo==c.hi==0 and j.lo>0)
ct('a_over_b_hazard_not_exact',log1p(F(1,2)).hi<F(1,2))
# Actual original 21-stage witness; each suffix is charged by the full prefix.
policy=[(F(349,2000),F(3,10))]+[(F(21,5000),F(1,100))]*20
prefix=F(1);cost=I(0);wrong=I(0)
for a,b in policy:
 prefix/=1+a;cost+=2*prefix*w(a,b);wrong+=2*w(a,b)/(1+a)
ck('hybrid_original_score',sum(b for a,b in policy)==F(1,2))
ck('hybrid_original_dual_lower', (I(prefix)-F(19,10)*cost).lo>F(711020048691,10**12))
ck('hybrid_original_dual_upper', (I(prefix)-F(19,10)*cost).hi<F(711020048692,10**12))
ck('hybrid_budget_lower',cost.lo>F(37866038451,10**12))
ct('omitted_prefix_changes_actual_cost',wrong.lo>cost.hi)
ck('dual_N297_threshold',F(19,160*297)<F(1,2500))
ct('dual_N296_not_threshold',F(19,160*296)>F(1,2500))
ct('N21_not_global_precision',F(19,160*21)>F(1,2500))
Blo=F(37866038451,10**12)
ck('primal_N549_threshold',1/(3*(16*549*Blo+1))<F(1,1000))
ct('primal_N548_lower_bound_not_enough',1/(3*(16*548*Blo+1))>F(1,1000))
# Mesh successor: exact derivative envelopes and precision allocations.
rb,bb=s.symbols('rb bb',nonnegative=True);hh=g.subs(x,rb)/2;zz=bb*(1+rb)/2;ee=bb*hh/(1-zz)
ck('mesh_eta_b_identity',s.simplify(s.diff(ee,bb)-hh/(1-zz)**2)==0)
ck('mesh_eta_r_identity',s.simplify(s.diff(ee,rb)-(bb*s.diff(hh,rb)/(1-zz)+bb*hh*(bb/2)/(1-zz)**2))==0)
ck('mesh_Wr_bound',2*(s.Rational(3,2)+s.Rational(1,4))==s.Rational(7,2))
ck('mesh_atom_r_combination',s.Rational(7,2)+s.Rational(1,2)==4)
lam=F(19,10);nn=594;JJ=51084000;MM=86000;numerr=F(1,23780000)
mesh=(1+4*lam)*(F(nn,2*JJ)+F(1,2*MM));trunc=lam*F(1,4)/(4*nn)
ck('mesh_precision_allocation',mesh==F(1,10000))
ck('two_sided_evaluation_allocation',2*(2*nn+1)*numerr==F(1,10000))
ck('full_precision_width',mesh+trunc+2*(2*nn+1)*numerr<F(1,2500))
ct('literal_ratio_bank_enormous',(MM+1)**nn>10**2700)
# Independent rational interval Euler evaluator and small exhaustive grid.
from math import isqrt,comb

def sqrtI(x,bits=48):
 x=F(x);scale=1<<bits;n=isqrt((x.numerator*scale*scale)//x.denominator)
 return I(F(n,scale),F(n+1,scale))
def qI(u):
 if u>=F(3,2):return I(F(1,2))
 out=2*sqrtI(1+2*u)-2-u
 return I(max(F(0),out.lo),min(F(1,2),out.hi))
def flow(t,x,lam=F(19,10),steps=16):
 x=cv(x)
 if t==0:return x
 h=t/steps;lo=x.lo;hi=x.hi
 for _ in range(steps):
  lo=max(F(0),lo-lam*h*qI(lo/lam).hi)
  hi=min(F(1),hi-lam*h*qI(hi/lam).lo+lam*h*h/4)
 return I(lo,hi)
def atom(b,ratio,x,lam=F(19,10)):
 if b==0:return cv(x)
 a=b*ratio;raw=(cv(x)-2*lam*w(a,b))/(1+a)
 return I(max(F(0),raw.lo),max(F(0),raw.hi))
linear=flow(F(1,2),I(1),F(1,10))
ck('Euler_exact_linear_region_enclosed',linear.lo<=F(39,40)<=linear.hi)
ck('Euler_origin',flow(F(1,2),I(0)).lo==0)
ck('sqrt_bracket_positive_control',sqrtI(F(2)).lo**2<2<sqrtI(F(2)).hi**2)
smallJ=4;smallM=4;delta=F(1,2*smallJ)
base=[flow(k*delta,I(1)) for k in range(smallJ+1)]
vals=[];candidates=0
for k in range(smallJ+1):
 options=[]
 for i in range(k+1):
  for j in range(k-i+1):
   aa=[atom(j*delta,F(m,smallM),base[k-i-j]) for m in range(smallM+1)]
   aa=I(max(v.lo for v in aa),max(v.hi for v in aa))
   options.append(flow(i*delta,aa));candidates+=1
 vals.append(I(max(v.lo for v in options),max(v.hi for v in options)))
ck('small_grid_exhaustive_split_count',candidates==comb(smallJ+3,3))
ck('small_grid_contains_free_baseline',vals[-1].lo>=F(2,3))
ck('small_grid_contains_continuum_lower',vals[-1].lo>=base[-1].lo)
ck('small_grid_interval_order',0<=vals[-1].lo<=vals[-1].hi<=1)
small_grid={'N':1,'J':smallJ,'M':smallM,'score':'1/2','lambda':'19/10','continuum_split_evaluations':candidates,'grid_value_interval':[str(vals[-1].lo),str(vals[-1].hi)],'interpretation':'coarse exhaustive algorithm fixture only; mesh remainder is not a tight optimum'}
paths=['explorations/conditional-build/k2563-global-hybrid-reduction-2026-11-05.md','tests/channel-swings/k2563_global_hybrid_reduction_probe.py','explorations/conditional-build/k2485-constrained-stopping-frontier-2026-11-01.md','explorations/conditional-build/k2495-stopping-order-and-continuum-2026-11-02.md','explorations/conditional-build/k2507-stopping-optimal-hybrid-tail-2026-11-02.md','lab/process/k2561-higher-budget-stopping.json']
report={'result':'K2563','checks':checks,'contrary_controls':controls,'bounds':{'cost_error':'S^2/(4N)','dual_error':'lambda*S^2/(4N)','primal_error':'epsilon*(1-1/(1+S))/(B+epsilon)','dual_297':str(F(19,160*297)),'witness_budget_interval':[str(cost.lo),str(cost.hi)],'certified_mesh_example':{'N':nn,'J':JJ,'M':MM,'component_error':str(numerr)},'small_grid':small_grid},'evidence_kinds':{'exact':'log and generator algebra, square error identity, interval actual-law stage checks, 21-stage prefix calculation, rational precision thresholds','universal':'largest-atom compression, compact hybrid dual, constrained mixtures and feedback recursion proved in note','supporting':'finite interval fixtures test actual law and error bounds; they do not establish universal theorem','reused':'K2483/2485 adaptive reduction and K2495/2507 continuum optimizer','not_claimed':'numerical global V_N, one-atom optimality, original finite attainment or native GU'},'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in paths}}
out=R/'lab/process/k2563-global-hybrid-reduction.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved report consistency'
print('K2563 PASS',len(checks),'exact/supporting groups',len(controls),'contrary controls')
