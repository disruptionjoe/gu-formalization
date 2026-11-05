"""K2545 exact original-law cubic identities and genuine contrary controls.
Universal stage-count uniformity and near-critical inference are proved in the note.
"""
from pathlib import Path
import hashlib,json,sys
import sympy as s
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(bank,name,v):
 bank[name]=bool(v)
 if not bank[name]:raise AssertionError('FAIL '+name)
def eq(name,a,b=0):ck(checks,name,s.simplify(a-b)==0)
r,b,lam=s.symbols('r b lam',real=True); rt=2*s.sqrt(3)-3;lt=4*s.sqrt(3)/3
al=(1-r)**2/(4*(1+r));be=(1+r)/2;cc=be-al;q=al*be-al**2/2;t=al*be**2-al**2*be+al**3/3;f=r+2*lam*al
ratio=1+(b-r*b)**2/(2*(b+r*b)*(2-b-r*b))
eq('exact_original_log_argument',ratio,(1-cc*b)/(1-be*b))
for n,coef in [(1,al),(2,q),(3,t)]:eq('log_coefficient_'+str(n),(be**n-cc**n)/n,coef)
eq('log_tail_geometric_constant',1/(4*(1-s.Rational(1,4))),s.Rational(1,3))
eq('f_strong_convexity_formula',s.diff(f,r,2),4*lam/(1+r)**3)
M0=2/(1+r)**2-s.Rational(1,2)
eq('M0_leading_derivative',-2*s.diff(al,r),M0);eq('stationarity_link',s.diff(f,r),1-lam*M0)
eq('critical_stationarity',s.diff(f,r).subs({r:rt,lam:lt}))
# Exact ORIGINAL derivative including the continuation value; w and derivative remain independent.
a,WW,Wa,Y,Prev=s.symbols('a w w_a suffix prefix')
deriv=Prev*(-2*lam*Wa*(1+a)-Y+2*lam*WW)/(1+a)**2
eq('original_stage_derivative',deriv,Prev/(1+a)**2*(lam*(2*WW-2*(1+a)*Wa)-Y))
ck(checks,'uniform_M_error_constant',s.Rational(2,3)+s.Rational(3,2)+2*s.Rational(5,4)*s.Rational(7,3)==8<16)
ck(checks,'uniform_localization_constant',32+2/lt+s.Rational(4,3)<35)
ck(checks,'uniform_endpoint_margins_at_1e3',s.Rational(3,2)*lt-16*lt/1000>1 and 1-(1+2*lt/3)/1000>0)
ck(checks,'localized_ratios_stay_interior',0<rt-s.Rational(36,1000)<rt+s.Rational(36,1000)<1)
eq('original_remainder_constant',2*(1+s.Rational(1,2)+s.Rational(1,3)+s.Rational(1,3)),s.Rational(13,3))
A=s.simplify(f.subs({r:rt,lam:lt}));F=s.simplify(s.diff(f,r,2).subs({r:rt,lam:lt}));Bp=s.simplify(s.diff(r*r+2*lam*al*r-2*lam*q,r).subs({r:rt,lam:lt}))
eq('critical_A',A,3-4*s.sqrt(3)/3);eq('critical_B',rt*A/2,5*s.sqrt(3)-s.Rational(17,2));eq('critical_F',F,s.Rational(3,2)+5*s.sqrt(3)/6);eq('critical_Bprime',Bp,s.Rational(1,4)+7*s.sqrt(3)/12)
x=s.symbols('x1:4',nonnegative=True);rs=s.symbols('r1:4',real=True);acts=[xi*ri for xi,ri in zip(x,rs)]
def h2(vals):return (sum(vals)**2+sum(v*v for v in vals))/2
def h3(vals):return (sum(vals)**3+3*sum(vals)*sum(v*v for v in vals)+2*sum(v**3 for v in vals))/6
Q=h2(acts)+2*lam*sum(al.subs(r,rs[i])*x[i]*sum(acts[:i+1])-q.subs(r,rs[i])*x[i]**2 for i in range(3))
C=-h3(acts)-2*lam*sum(t.subs(r,rs[i])*x[i]**3-q.subs(r,rs[i])*x[i]**2*sum(acts[:i+1])+al.subs(r,rs[i])*x[i]*h2(acts[:i+1]) for i in range(3))
# Independently multiply the original prefix products and logarithmic series.
prefix=[s.Integer(1),s.Integer(0),s.Integer(0),s.Integer(0)];cost3=0
for ri,xi,ai in zip(rs,x,acts):
 factor=[s.Integer(1),-ai,ai**2,-ai**3]
 prefix=[s.expand(sum(prefix[j]*factor[k-j] for j in range(k+1))) for k in range(4)]
 wcoeff=[0,al.subs(r,ri)*xi,q.subs(r,ri)*xi**2,t.subs(r,ri)*xi**3]
 cost3+=sum(prefix[j]*wcoeff[3-j] for j in range(4))
eq('independent_original_prefix_cubic',prefix[3]-2*lam*cost3,C)
sub={**dict.fromkeys(rs,rt),lam:lt};common=s.simplify(C.subs(sub));ell=[A*sum(x[i:])+(Bp-A)*x[i] for i in range(3)]
for i in range(3):eq('ordered_ratio_gradient_'+str(i),s.diff(Q,rs[i]).subs(sub),x[i]*ell[i])
eq('critical_common_quadratic',Q.subs(sub),rt*A*sum(x)**2/2)
opt=s.expand(common+sum(x[i]*ell[i]**2/(2*F) for i in range(3)))
C1=-s.Rational(1097,16)+5707*s.sqrt(3)/144;c3=(7619*s.sqrt(3)-13185)/144;cL=(249*s.sqrt(3)-431)/2;d=(1643*s.sqrt(3)-2841)/144
s3=sum(v**3 for v in x);L=sum(x[i]**2*x[j] for i in range(3) for j in range(i+1,3));RR=sum(x[i]*x[j]**2 for i in range(3) for j in range(i+1,3));TT=x[0]*x[1]*x[2]
formula=C1*sum(x)**3+c3*(s3-sum(x)**3)+cL*L
# Coefficient-type checks prove the homogeneous identity, rather than sampled partitions.
pol=s.Poly(s.expand(opt-formula),*x)
for mon,coef in pol.terms():eq('cubic_monomial_'+''.join(map(str,mon)),coef)
eq('cubic_partition_identity',sum(x)**3-s3,3*(L+RR)+6*TT)
eq('critical_gap_constant',c3-cL/3,d)
for name,u,v,w in [('c3',7619,13185,303258),('cL',249,431,242),('d',1643,2841,27066)]:ck(checks,'exact_positive_'+name,3*u*u-v*v==w>0)
u,z=s.symbols('u z',real=True)
eq('weighted_square_completion',z*u-F*u*u/2,z*z/(2*F)-F*(u-z/F)**2/2)
# Recover both original two-stage ordered coefficients independently.
th=s.symbols('theta',positive=True);v=1-th;c0=(13185-7619*s.sqrt(3))/48;c1=(2841-1643*s.sqrt(3))/48
sub2={x[0]:th,x[1]:v,x[2]:0};gap=s.simplify(formula.subs(sub2)-C1)
eq('prior_two_stage_gap',gap,th*v*(c0*v+c1*th))
eq('single_stage_ratio_gain',opt.subs({x[0]:1,x[1]:0,x[2]:0})-common.subs({x[0]:1,x[1]:0,x[2]:0}),Bp*Bp/(2*F))
# Moving multiplier: differentiate H along the stationary ratio curve.
LR=2*(1+r)**2/((1-r)*(r+3));HH=(3*r+1)*(r*r+6*r-3)/(8*(r+3));Hp=s.simplify((s.diff(HH,r)/s.diff(LR,r)).subs(r,rt))
eq('critical_H_lambda_derivative',Hp,(141-81*s.sqrt(3))/8)
mu0=s.simplify(c1/(2*Hp));eq('nearcritical_boundary',mu0,s.Rational(37,66)-257*s.sqrt(3)/396)
ck(checks,'nearcritical_H_positive',141**2-3*81**2>0)
Delta=c3*(s3-sum(x)**3)+cL*L
pairs=sum(x[i]*x[j] for i in range(3) for j in range(i+1,3))
eq('homogeneous_nearcritical_sharp_bound_identity',Delta-c1*sum(x)*pairs,-cL*RR+(2*c0-3*c1)*TT)
ck(checks,'triple_bound_exact_negative',3*10309**2-17847**2==311034>0)
mu=-1;D=s.simplify(gap-mu*Hp*(1-th*th-v*v));witness=s.simplify(D.subs(th,s.Rational(3,4)))
eq('nearcritical_genuine_two_stage_witness',witness,(7119-4109*s.sqrt(3))/256)
ck(checks,'nearcritical_witness_positive',7119**2-3*4109**2>0)
ck(controls,'omitted_ratio_optimization_changes_value',Bp*Bp/(2*F)>0)
ck(controls,'order_changes_value',s.simplify(gap.subs(th,s.Rational(1,3))-gap.subs(th,s.Rational(2,3)))==s.simplify(-2*cL/27) and cL>0)
score=s.symbols('S',positive=True)
eq('collapsing_split_first_defect',1-score**3-(1-score)**3,3*score*(1-score))
ck(controls,'no_uniform_nontrivial_cubic_gap',s.limit(gap,th,0)==0 and s.limit(gap,th,1)==0)
ck(controls,'mixture_only_expected_concentration',s.simplify(score*(1-2*s.Rational(1,2)**3))==3*score/4)
ck(controls,'subcritical_witness_not_overwritten',s.Rational(128,57)<lt and HH.subs(r,s.Rational(5,11))<0)
# Deleting prefix cost removes a nonzero cubic term on an actual two-stage law.
wrong=-h3(acts)-2*lam*sum(t.subs(r,rs[i])*x[i]**3 for i in range(3))
ck(controls,'deleted_prefix_weights_detected',s.simplify((C-wrong).subs({**dict.fromkeys(rs,s.Rational(1,2)),x[0]:s.Rational(1,3),x[1]:s.Rational(2,3),x[2]:0,lam:2}))!=0)
ck(controls,'moving_subcritical_multiplier_has_actual_positive_coefficient',witness>0 and mu<mu0)
ck(controls,'zero_stage_constructive_ratio_is_finite',all(not el.has(1/x[i]) for i,el in enumerate(ell)))
paths=['explorations/conditional-build/k2545-critical-stopping-aggregation-2026-11-04.md',str(Path(__file__).relative_to(R)),'explorations/conditional-build/k2517-small-score-stopping-transition-2026-11-02.md','explorations/conditional-build/k2485-constrained-stopping-frontier-2026-11-01.md']
report={'result':'K2545','exact_algebra':checks,'contrary_controls':controls,'coefficients':{k:str(v) for k,v in dict(A=A,B=rt*A/2,C_one=C1,c3=c3,cL=cL,d=d,Hprime=Hp,mu0=mu0,nearcritical_witness=witness).items()},'scope':'uniform original-law critical cubic and moving-multiplier asymptotics; proofs in note; no exact finite-score global optimum','dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in paths}}
p=R/'lab/process/k2545-critical-stopping-aggregation.json'
if '--write' in sys.argv:p.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(p.read_text())==report,'saved report mismatch'
print('K2545',len(checks),'exact algebra groups',len(controls),'contrary controls')
