"""Exact whole-domain decreasing-generator certificate; universal proof in K2559."""
from pathlib import Path
import sympy as s
from math import comb
import hashlib,json,sys,time
R=Path(__file__).resolve().parents[2]
checks={};controls={};certificates={}
def ck(k,x):
 checks[k]=bool(x)
 if not x:raise AssertionError(k)
def ct(k,x):
 controls[k]=bool(x)
 if not x:raise AssertionError('contrary '+k)
a,b,r=s.symbols('a b r');A=1+a;D=2*(a+b)*(2-a-b);N=D+(b-a)**2
wa=s.cancel(s.diff(N,a)/N-s.diff(D,a)/D);wb=s.cancel(s.diff(N,b)/N-s.diff(D,b)/D)
waa=s.diff(wa,a);wab=s.diff(wa,b);wbb=s.diff(wb,b);q=wab/waa
T=s.cancel(wbb-wab**2/waa);T3=s.factor(s.diff(T,b)-q*s.diff(T,a));v=wab-wb/A;H=s.cancel((v*v/waa-wbb)/A);H3=s.factor(s.diff(H,b)-v/waa*s.diff(H,a))
sq=s.sqrt(3);X,Y=s.symbols('X Y');st=time.time()
ex={'k':s.factor(-wa.subs(a,r*b)),'T3':s.factor(T3.subs(a,r*b)),'H3':s.factor(H3.subs(a,r*b)),'x':s.factor(((b-a)**2/D).subs(a,r*b)),'N2':s.factor((2*wb).subs(a,r*b))}

def sign(v):
 v=s.expand(v);aa=v.coeff(sq,0);bb=v.coeff(sq,1)
 if bb==0:return s.sign(aa)
 if aa==0:return s.sign(bb)
 if s.sign(aa)==s.sign(bb):return s.sign(aa)
 d=s.sign(aa*aa-3*bb*bb);return s.sign(aa)*d

def polytransform(expr,lo,hi,bl=0,bh=s.Rational(1,2)):
 p=s.Poly(expr,r,b,extension=sq); xx=s.Poly(X,X,Y,extension=sq); yy=s.Poly(bl+(bh-bl)*Y,X,Y,extension=sq)
 low=s.Poly(lo.subs(b,bl+(bh-bl)*Y) if hasattr(lo,'subs') else lo,X,Y,extension=sq);high=s.Poly(hi.subs(b,bl+(bh-bl)*Y) if hasattr(hi,'subs') else hi,X,Y,extension=sq);rr=low+(high-low)*xx
 rp=[s.Poly(1,X,Y,extension=sq)];bp=[rp[0]]
 for i in range(p.degree(r)):rp.append(rp[-1]*rr)
 for j in range(p.degree(b)):bp.append(bp[-1]*yy)
 out=s.Poly(0,X,Y,extension=sq)
 for (i,j),c in p.terms():out+=rp[i]*bp[j]*c
 return out

def bern(poly):
 n,m=poly.degree_list();cs=dict(poly.terms());row={}
 # Tensor transform in two passes.
 for i in range(n+1):
  for l in range(m+1):
   row[i,l]=sum(cs.get((j,l),0)*s.Rational(comb(i,j),comb(n,j)) for j in range(i+1))
 vals=[]
 for i in range(n+1):
  for k in range(m+1):vals.append(s.expand(sum(row[i,l]*s.Rational(comb(k,l),comb(m,l)) for l in range(k+1))))
 # Inverse basis transformation by forward differences, independently of the sums above.
 field=s.QQ.algebraic_field(sq)
 grid=[[field.from_sympy(vals[i*(m+1)+k]) for k in range(m+1)] for i in range(n+1)]
 rows=[]
 for row in grid:
  diff=row[:]; coeff=[]
  for l in range(m+1):
   coeff.append(diff[0]*comb(m,l));diff=[diff[j+1]-diff[j] for j in range(len(diff)-1)]
  rows.append(coeff)
 recovered={}
 for l in range(m+1):
  diff=[rows[i][l] for i in range(n+1)]
  for j in range(n+1):
   value=diff[0]*comb(n,j)
   if value:recovered[j,l]=field.to_sympy(value)
   diff=[diff[k+1]-diff[k] for k in range(len(diff)-1)]
 assert s.Poly(s.Poly.from_dict(recovered,(X,Y),extension=sq).as_expr()-poly.as_expr(),X,Y,extension=sq).is_zero
 return vals

def cert(name,expr,lo,hi,bl=0,bh=s.Rational(1,2)):
 n,d=s.fraction(s.factor(expr));cn,cd=polytransform(n,lo,hi,bl,bh),polytransform(d,lo,hi,bl,bh)
 # Point sign only selects orientation; whole denominator independently checked below.
 if sign(cd.eval({X:0,Y:0}))<0:cn,cd=-cn,-cd
 vs=bern(cn);ds=bern(cd)
 ok=all(sign(v)>=0 for v in vs) and all(sign(v)>0 for v in ds)
 ck(name+'_whole_domain',ok)
 certificates[name]={'domain':{'r_lower':str(lo),'r_upper':str(hi),'b_lower':str(bl),'b_upper':str(bh)},'numerator_degree':list(cn.degree_list()),'denominator_degree':list(cd.degree_list()),'numerator_coefficients':len(vs),'denominator_coefficients':len(ds),'zero_numerator_coefficients':sum(sign(v)==0 for v in vs),'coefficient_digest':hashlib.sha256(('\n'.join(map(str,vs))+'\nDEN\n'+'\n'.join(map(str,ds))).encode()).hexdigest(),'independent_basis_reconstruction':True}
 print(name,'PASS',flush=True)
 return ok

# Generator monotonicity on every subcritical output root.
Kflow=s.factor((wbb-wab**2/waa+wb*wab/(A*waa)).subs(a,r*b))
lo=2*sq-3+(4*sq-s.Rational(13,2))*b+s.Rational(9,100)*b*b
cert('negative_flow_generator',-Kflow,lo,s.Integer(1))
# Strictness: after removing the exact zero at r=1 the transformed numerator
# is positive in the interior (the boundary s=0,r=r0 is allowed to vanish).
num,den=s.fraction(s.factor(-Kflow/(1-r)))
np=polytransform(num,lo,s.Integer(1));dp=polytransform(den,lo,s.Integer(1))
if sign(dp.eval({X:0,Y:0}))<0:np,dp=-np,-dp
ns,ds=bern(np),bern(dp)
ck('strict_generator_numerator_nonnegative_coefficients',all(sign(v)>=0 for v in ns))
ck('strict_generator_numerator_not_zero',any(sign(v)>0 for v in ns))
ck('strict_generator_denominator_positive',all(sign(v)>0 for v in ds))
nn,mm=np.degree_list();zero_positions=[[i,j] for i in range(nn+1) for j in range(mm+1) if sign(ns[i*(mm+1)+j])==0]
ck('strict_upper_score_edge',any(sign(ns[i*(mm+1)+mm])>0 for i in range(nn+1)))
ck('strict_lower_ribbon_upper_score_corner',sign(ns[mm])>0)
ck('strict_lower_ribbon_edge',any(sign(ns[j])>0 for j in range(1,mm+1)))
score,step,action=s.symbols('score step action');tail=score-step
ck('zero_budget_original_slack',s.cancel(((1+action)/(1+score)-1/(1+tail))/2-step*tail/(2*(1+score)*(1+tail))-(action-step)/(2*(1+score)))==0)
ct('zero_budget_partial_action_has_loss',s.cancel((step*tail/(2*(1+score)*(1+tail))).subs({score:s.Rational(1,2),step:s.Rational(1,4)}))>0)
# Independent implicit differentiation of output-root equation M=v.
M=-2*A*wa+2*s.log(N/D)
ck('output_root_derivative_a',s.cancel(s.diff(M,a)+2*A*waa)==0)
ck('output_root_derivative_b',s.cancel(s.diff(M,b)-(-2*A*wab+2*wb))==0)
aprime=s.cancel((wb-A*wab)/(A*waa))
ck('constant_output_generator_derivative',s.cancel((wbb+wab*aprime).subs(a,r*b)-Kflow)==0)
v0=s.symbols('v0',nonnegative=True);r0=2/s.sqrt(1+2*v0)-1
g0=(1-r)**2/(2*(1+r));k0=(1-r)*(r+3)/(4*(1+r)**2)
ck('zero_score_output_root',s.simplify(2*k0.subs(r,r0)-v0)==0)
wb0=s.limit(wb.subs(a,r*b),b,0)
ck('continuous_initial_generator',s.simplify(2*wb0.subs(r,r0)-(2*s.sqrt(1+2*v0)-2-v0))==0)
ck('critical_zero_score_threshold',s.simplify((r*r+6*r-3).subs(r,2*sq-3))==0)
ct('global_all_root_generator_sign_false',s.cancel(Kflow.subs({r:s.Rational(1,4),b:s.Rational(1,10)}))>0)
ct('input_and_output_roots_distinct',s.cancel((M-(-2*wa)).diff(a))!=0)
# Constrained frontier derivatives with original one-stage prefix.
w=s.log(N/D);cost=2*w/A;prob=1/A
ck('cost_strict_derivative_identity',s.cancel(s.diff(cost,a)+M/A**2)==0)
ck('frontier_slope',s.cancel(s.diff(prob,a)/s.diff(cost,a)-1/M)==0)
ck('frontier_second_derivative',s.cancel((s.diff(1/M,a)/s.diff(cost,a))+2*A**3*waa/M**3)==0)
ct('wrong_expected_cost_prefix',s.cancel(s.diff(2*w,a)-s.diff(cost,a))!=0)
# Gaussian rational exact fixtures independently differentiate original log law.
for j,(aa,bb) in enumerate([(s.Rational(1,4),s.Rational(2,5)),(s.Rational(2,5),s.Rational(1,2))]):
 original=s.log(1+(b-a)**2/(2*(a+b)*(2-a-b)))
 d2aa=s.diff(original,a,2);d2ab=s.diff(original,a,b);d2bb=s.diff(original,b,2)
 expected=d2bb-d2ab*d2ab/d2aa+s.diff(original,b)*d2ab/((1+a)*d2aa)
 ck('original_law_generator_fixture_'+str(j),s.cancel(expected.subs({a:aa,b:bb})-Kflow.subs({r:aa/bb,b:bb}))==0)
ct('omitted_output_chain_term_rejected',s.cancel((Kflow-T.subs(a,r*b)).subs({r:s.Rational(4,5),b:s.Rational(1,4)}))!=0)
S,dd=s.symbols('S dd',positive=True);hh=1+S
Dend=s.expand(D.subs({a:S-dd,b:S},simultaneous=True))
ck('small_budget_original_denominator',s.expand(Dend-(8*S*(1-S)+4*(2*S-1)*dd-2*dd**2))==0)
# Log(1+x)=x+O(x^2), x=O(delta^2), so this rational calculation
# rigorously owns coefficients through degree three.
cseries=s.series(2*dd**2/(Dend*(hh-dd)),dd,0,4).removeO()
c2=1/(4*hh*S*(1-S));c3=c2*(1/hh-(2*S-1)/(2*S*(1-S)))
ck('small_budget_second_coefficient',s.cancel(cseries.coeff(dd,2)-c2)==0)
ck('small_budget_third_coefficient',s.cancel(cseries.coeff(dd,3)-c3)==0)
A2=4*hh*S*(1-S);B2=4*S*S-S-1
ck('small_budget_inverse_linear_square',s.cancel(A2*c2-1)==0)
ck('small_budget_inverse_quadratic',s.cancel(2*c2*B2+c3*A2)==0)
ck('true_frontier_budget_coefficient',s.cancel(B2/hh**2+A2/hh**3-(3*S-1)/hh**2)==0)
ct('omitted_prefix_changes_small_budget_cubic',s.cancel(c3-(c3-c2/hh))!=0)
paths=['explorations/conditional-build/k2559-parametric-stopping-concavity-2026-11-05.md','tests/channel-swings/k2559_parametric_stopping_concavity_probe.py','explorations/conditional-build/k2553-global-stopping-certificate-2026-11-04.md','lab/process/k2553-global-stopping-certificate.json','explorations/conditional-build/k2557-parametric-stopping-support-2026-11-05.md','explorations/conditional-build/k2509-stopping-atom-certificate-2026-11-02.md']
report={'result':'K2559','multiplier_domain':'all finite lambda>=4/sqrt(3)','score_domain':'0<S<=1/2','checks':checks,'contrary_controls':controls,'certificates':certificates,'strictness':{'factored_zero':'1-r','nonnegative_numerator_coefficients':len(ns),'positive_numerator_coefficients':sum(1 for v in ns if sign(v)>0),'positive_denominator_coefficients':len(ds),'factored_numerator_degree':list(np.degree_list()),'zero_positions':zero_positions},'evidence_kinds':{'exact':'new two-variable algebraic Bernstein generator certificate with independent basis reconstruction; implicit root and original-law cost derivatives','universal':'nonautonomous scalar-flow comparison, full-policy Bellman transfer, rigidity and constrained-frontier proof in note','not_claimed':'residual concavity in theta, full higher-budget frontier, physical law, external certification or GU prediction'},'dependencies':{x:hashlib.sha256((R/x).read_bytes()).hexdigest() for x in paths}}
out=R/'lab/process/k2559-parametric-stopping-concavity.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved_report_consistency'
print('K2559 PASS',len(checks),'exact groups',len(controls),'contrary controls')
