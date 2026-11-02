"""K2509 whole-domain exact Bernstein certificate; --write saves, default replays.
Universal transfer is the written Bellman proof; finite controls are separate.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import hashlib,json,sys
import sympy as s
from flint import arb,ctx
ctx.prec=192
ROOT=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ct(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
def aa(x):return arb(x.numerator)/x.denominator
a,b,r,X,Y=s.symbols('a b r X Y');D=2*(a+b)*(2-a-b);N=D+(b-a)**2;x=(b-a)**2/D;A=1+a
wa=s.cancel(s.diff(N,a)/N-s.diff(D,a)/D);wb=s.cancel(s.diff(N,b)/N-s.diff(D,b)/D)
waa=s.diff(wa,a);wab=s.diff(wa,b);wbb=s.diff(wb,b)
FF=s.factor((2*((wab-wb/A)**2-wbb*waa)/(A*(-2*A*wa+2*x)*waa)).subs(a,r*b))
num,den=s.fraction(s.factor(FF-s.Rational(47,100)))
def bern(poly):
 P=s.Poly(poly.subs({r:s.Rational(31,39)+s.Rational(8,39)*X,b:Y/2}),X,Y);nx,ny=P.degree_list();terms=P.terms();vals=[]
 for i in range(nx+1):
  for j in range(ny+1):
   vals.append(sum(c*s.Rational(comb(i,k),comb(nx,k))*s.Rational(comb(j,l),comb(ny,l)) for (k,l),c in terms if k<=i and l<=j))
 return {'degree':[nx,ny],'coefficients':[str(v) for v in vals],'minimum':str(min(vals))},vals
cert,vals=bern(num)
ck('numerator_degree',cert['degree']==[11,8]);ck('numerator_count',len(vals)==108)
for i,v in enumerate(vals):ck(f'positive_numerator_Bernstein_{i}',v>0)
ck('numerator_minimum',min(vals)==s.Rational(260694488634812372,904489565021289))
constant,factors=s.factor_list(den);ck('denominator_positive_constant',constant==100);factorcert=[]
for j,(f,power) in enumerate(factors):
 c,v=bern(f);c['power']=int(power);c['polynomial']=str(f);factorcert.append(c)
 for i,z in enumerate(v):ck(f'positive_denominator_{j}_{i}',z>0)
ck('denominator_factors',sorted((tuple(c['degree']),c['power'],c['minimum']) for c in factorcert)==[((1,1),3,'1'),((3,2),1,'687364/59319'),((5,3),1,'8')])
corner=s.cancel(FF.subs({r:1,b:s.Rational(1,2)}));ck('continuous_free_corner',corner==s.Rational(16,27));ct('overstated_curvature_refuted',corner<1)
ct('lambda8_decoupled_template_insufficient',FF.subs({r:s.Rational(7,9),b:s.Rational(1,2)})<s.Rational(1,2)<s.Rational(129,256))
q=(X-s.Rational(1,2))**2-s.Rational(1,100)
ct('endpoint_sampling_not_certificate',q.subs(X,0)>0 and q.subs(X,1)>0 and q.subs(X,s.Rational(1,2))<0)
nx,ny=cert['degree'];reconstructed=sum(vals[i*(ny+1)]*comb(nx,i)*X**i*(1-X)**(nx-i) for i in range(nx+1))
ck('Bernstein_basis_reconstruction_boundary',s.Poly(reconstructed-num.subs({r:s.Rational(31,39)+s.Rational(8,39)*X,b:0}),X).is_zero)
bad=num-num.subs({r:s.Rational(31,39),b:0})-1;badcert,badvals=bern(bad)
ct('corrupt_polynomial_rejected',badvals[0]==-1 and not all(v>0 for v in badvals))
u,de=s.symbols('u delta',positive=True);M0=4-2*u;L=M0+de**2*u;kexpr=2*de/L*(1+de*(1-u)/(2-u))
ck('original_hazard_derivative',s.factor((-wa).subs({a:u*(1-de)/2,b:u*(1+de)/2},simultaneous=True)-kexpr)==0)
fuu=s.diff(s.log(L/M0),u,2)
ck('radial_second_derivative',s.factor(fuu-4*de**2*(2*L+(2-de**2)*M0)/(M0**2*L**2))==0)
ck('radial_upper_numerator',s.factor(4*L-(2*L+(2-de**2)*M0))==4*de**2)
ck('L_over_M0_identity',s.factor(L/M0-1-de**2*u/M0)==0)
zz=s.symbols('z');schur=wbb-wab**2/waa
ck('Schur_completion',s.factor(zz**2*waa+2*zz*wab+wbb-schur-waa*(zz+wab/waa)**2)==0)
lam=F(35,4);rad=4/lam*(1+1/(2*lam*lam));kap=F(47,100)-rad
ck('rational_curvature_gap',rad==F(19728,42875) and kap==F(1693,171500)>0);ck('ratio_rectangle',(lam-1)/(lam+1)==F(31,39))
ck('M_derivative',s.factor(s.diff(-2*A*wa,a)+2*wa+2*A*waa)==0)
ap=-wab/waa+wb/(A*waa)
ck('U_second_derivative',s.factor(-2*(wbb+wab*ap)/A+2*wb*ap/A**2-2/A*((wab-wb/A)**2/waa-wbb))==0)
a1,a2,w1,w2,u0,u1,u2=s.symbols('a1 a2 w1 w2 u0 u1 u2');la=s.symbols('lambda');P1=1/(1+a1);P2=P1/(1+a2);cost=2*(P1*w1+P2*w2)
E1=(1+a1)*u0+2*la*w1-u1;E2=(1+a2)*u1+2*la*w2-u2
ck('original_weighted_telescoping',s.factor(P1*E1+P2*E2-(u0+la*cost-P2*u2))==0)
wrong=(u0+2*la*(w1+w2)-P2*u2)-(P1*E1+P2*E2)
ct('unweighted_cost_refuted',wrong.subs({a1:s.Rational(1,4),a2:s.Rational(1,5),w1:1,w2:2,la:1,u0:1,u1:1,u2:1})!=0)
for scores in [(F(1,2),),(F(1,4),F(1,4)),(F(1,3),F(1,12),F(1,12))]:
 S=sum(scores);cross=sum(z*sum(scores[i+1:]) for i,z in enumerate(scores))
 ck('score_pair_identity_'+str(scores),cross==(S*S-sum(z*z for z in scores))/2)
 if len(scores)>1:ck('strict_multistage_gap_'+str(scores),cross>0)
d0=F(77,2000);AA=F(3,2)-d0;xx=d0*d0/(2*(1-d0*d0));clo=2*xx/(AA*(1+xx));mup=4*AA*d0/((1-d0*d0)*(2-d0*d0))+2*xx
ck('budget_lower_witness',clo-F(1,1000)==F(349330467,23366669533000)>0)
ck('multiplier_upper_witness',F(4,35)-mup==F(5632989533,372503683452145)>0)
dlo=F(48439958028934968344008499723887,1267650600228229401496703205376000);dhi=F(3027497376808435521500531232743,79228162514264337593543950336000)
def C(d):
 dd=aa(d);return 2*(1+dd*dd/(2*(1-dd*dd))).log()/(arb(3)/2-dd)
ck('root_admissibility',0<dlo<dhi<d0<F(1,2));ck('certified_lower_cost',C(dlo)<arb(1)/1000);ck('certified_upper_cost',C(dhi)>arb(1)/1000)
plo=F(684093908424485444843251472880883,10**33);phi=F(684093908424485444843251472880884,10**33)
ck('exact_probability_enclosure',plo<1/(F(3,2)-dlo)<1/(F(3,2)-dhi)<phi);ck('strict_improvement_previous_witness',plo>F(5000,7309))
policy=[(F(1934773,5905227),F(49,100)),(F(15007,7000000),F(1,200)),(F(105176,49105049),F(1,200))]
def logbr(xx,n):return sum((-1)**(k+1)*xx**k/k for k in range(1,n+1))
P=F(1);lo=hi=F(0)
for ai,bi in policy:
 ck('competing_atom_'+str(ai),0<=ai<=bi<=F(1,2));P/=1+ai;xx=(bi-ai)**2/(2*(ai+bi)*(2-ai-bi));lo+=2*P*logbr(xx,8);hi+=2*P*logbr(xx,9)
ck('competing_original_success',P==F(3,4) and sum(bi for ai,bi in policy)==F(1,2));ct('no_all_budget_one_stage_inference',hi<F(417,19600) and lo>F(1,1000))
report={'result':'K2509','scope':'original law global one-stage support for lambda>=35/4 and 0<S<=1/2; exact budget1/1000','evidence_kind':'exact rational whole-domain Bernstein certificate, written Bellman transfer, exact finite controls and Arb192 root sign enclosures','checks':checks,'contrary_controls':controls,'curvature_certificate':{'r_domain':['31/39','1'],'b_domain':['0','1/2'],'rational_function':str(FF),'numerator':cert,'denominator_constant':str(constant),'denominator_factors':factorcert},'budget_certificate':{'d_lower':str(dlo),'d_upper':str(dhi),'p_lower':str(plo),'p_upper':str(phi),'cost_lower_endpoint':str(C(dlo)),'cost_upper_endpoint':str(C(dhi)),'kappa':str(kap)},'dependencies':{}}
for path in [Path(__file__),ROOT/'explorations/conditional-build/k2509-stopping-atom-certificate-2026-11-02.md',ROOT/'explorations/conditional-build/k2485-constrained-stopping-frontier-2026-11-01.md',ROOT/'explorations/conditional-build/k2491-analytic-stopping-certificate-2026-11-02.md',ROOT/'explorations/conditional-build/k2507-stopping-optimal-hybrid-tail-2026-11-02.md']:
 report['dependencies'][str(path.relative_to(ROOT))]=hashlib.sha256(path.read_bytes()).hexdigest()
out=ROOT/'lab/process/k2509-stopping-atom-certificate.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,indent=2)+'\n')
else:ck('saved_report_matches_reproduction',json.loads(out.read_text())==report)
print(f'K2509 PASS: {len(checks)} exact/certified checks; {len(controls)} contrary controls')
