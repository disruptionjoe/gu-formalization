"""K2511 exact whole-rectangle certificate and original-law controls.
--write saves report; default reproduces. No floating point theorem assertions.
"""
from pathlib import Path
from math import comb
import hashlib,json,sys
import sympy as s
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ct(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
a,b,r,X,Y=s.symbols('a b r X Y');D=2*(a+b)*(2-a-b);N=D+(b-a)**2;x=(b-a)**2/D;A=1+a
wa=s.cancel(s.diff(N,a)/N-s.diff(D,a)/D);wb=s.cancel(s.diff(N,b)/N-s.diff(D,b)/D)
waa=s.diff(wa,a);wab=s.diff(wa,b);wbb=s.diff(wb,b)
F=s.factor((2*((wab-wb/A)**2-wbb*waa)/(A*(-2*A*wa+2*x)*waa)).subs(a,r*b))
num,den=s.fraction(s.factor(F-s.Rational(4,5)/(1+b)**3))
def bern(poly):
 p=s.Poly(poly.subs({r:s.Rational(2,3)+X/3,b:Y/2}),X,Y);nx,ny=p.degree_list();terms=p.terms()
 vals=[sum(c*s.Rational(comb(i,k),comb(nx,k))*s.Rational(comb(j,l),comb(ny,l)) for (k,l),c in terms if k<=i and l<=j) for i in range(nx+1) for j in range(ny+1)]
 return {'degree':[nx,ny],'coefficients':[str(v) for v in vals],'minimum':str(min(vals))},vals
cert,vals=bern(num);ck('numerator_degree',cert['degree']==[11,8]);ck('numerator_count',len(vals)==108);ck('numerator_minimum',min(vals)==s.Integer(160))
for i,v in enumerate(vals):ck('numerator_positive_'+str(i),v>0)
constant,factors=s.factor_list(den);ck('positive_denominator_constant',constant>0);factorcert=[]
for j,(f,power) in enumerate(factors):
 c,v=bern(f);c.update(power=int(power),polynomial=str(f));factorcert.append(c)
 for i,z in enumerate(v):ck(f'denominator_{j}_{i}_positive',z>0)
# Reconstruct the entire Bernstein polynomial, not only one boundary.
nx,ny=cert['degree'];reconstructed=sum(vals[i*(ny+1)+j]*comb(nx,i)*X**i*(1-X)**(nx-i)*comb(ny,j)*Y**j*(1-Y)**(ny-j) for i in range(nx+1) for j in range(ny+1))
ck('full_Bernstein_reconstruction',s.Poly(reconstructed-num.subs({r:s.Rational(2,3)+X/3,b:Y/2}),X,Y).is_zero)
# A genuine corrupted numerator must lose its certificate.
bad=num-num.subs({r:s.Rational(2,3),b:0})-1;_,badvals=bern(bad)
ct('corrupt_numerator_rejected',badvals[0]==-1)
q=(X-s.Rational(1,2))**2-s.Rational(1,100)
ct('endpoint_sampling_insufficient',q.subs(X,0)>0 and q.subs(X,1)>0 and q.subs(X,s.Rational(1,2))<0)
ct('old_decoupled_lambda8_failure_retained',F.subs({r:s.Rational(7,9),b:s.Rational(1,2)})<s.Rational(1,2)<s.Rational(129,256))
u,delta,lam,y=s.symbols('u delta lam y',positive=True);M0=4-2*u;L=M0+delta**2*u
kexpr=2*delta/L*(1+delta*(1-u)/(2-u))
ck('hazard_identity',s.factor((-wa).subs({a:u*(1-delta)/2,b:u*(1+delta)/2},simultaneous=True)-kexpr)==0)
fuu=s.diff(s.log(L/M0),u,2)
ck('radial_derivative',s.factor(fuu-4*delta**2*(2*L+(2-delta**2)*M0)/(M0**2*L**2))==0)
ck('radial_numerator_gap',s.factor(4*L-(2*L+(2-delta**2)*M0))==4*delta**2)
score,v=s.symbols('score v',positive=True)
B=2*v**2/(lam*(1-b))*(1+v**2*b/(2*lam**2*(1-b)))
ck('score_bound_substitution',s.factor((8*v**2/lam*(1/M0+v**2*u/(lam**2*M0**2))).subs(u,2*b)-B)==0)
A0=2*lam**2-v**2;ratio=v**2*(A0*y+v**2)*(y+score)**3/(lam**3*y**2)
ck('ratio_identity',s.factor(B.subs(b,1-y)*(score+y)**3-ratio)==0)
ck('ratio_derivative',s.factor(s.diff(ratio,y)-v**2*(y+score)**2/(lam**3*y**3)*(A0*y*(2*y-score)+v**2*(y-2*score)))==0)
ck('ratio_endpoint',s.factor(ratio.subs(y,1)-2*v**2*(1+score)**3/lam)==0)
ck('score_log_derivative',s.factor(s.diff(3*s.log(1+score)-2*s.log(1+2*score/3),score)-(3-s.Rational(4,3)+2*score/3)/((1+score)*(1+2*score/3)))==0)
ck('ratio_maximum',(2*v**2*(1+score)**3/lam).subs({lam:5,score:s.Rational(1,2),v:s.Rational(3,4)})==s.Rational(243,320))
kap=s.Rational(13,1080);ck('uniform_gap',(s.Rational(4,5)-s.Rational(243,320))*s.Rational(8,27)==kap)
ck('ratio_range',(s.Integer(5)-1)/(s.Integer(5)+1)==s.Rational(2,3))
# Independent full triangular check of the refined scalar curvature comparison.
Bn=B.subs({lam:5,v:1/(1+2*score/3)})
tn,td=s.fraction(s.factor(s.Rational(4,5)/(1+score-b)**3-Bn))
if td.subs({b:0,score:0})<0:tn,td=-tn,-td
Ptri=s.Poly(tn.subs({b:X*Y/2,score:Y/2},simultaneous=True),X,Y);nt,mt=Ptri.degree_list();tt=Ptri.terms()
tv=[sum(c*s.Rational(comb(i,k),comb(nt,k))*s.Rational(comb(j,l),comb(mt,l)) for (k,l),c in tt if k<=i and l<=j) for i in range(nt+1) for j in range(mt+1)]
ck('triangular_degree',(nt,mt)==(4,6));ck('triangular_minimum',min(tv)==1300)
for i,z in enumerate(tv):ck('triangular_positive_'+str(i),z>0)
ck('triangular_denominator',s.factor(td-125*(1-b)**2*(2*score+3)**4*(1+score-b)**3)==0)
tri={'degree':[nt,mt],'coefficients':[str(z) for z in tv],'minimum':str(min(tv))}
# Envelope derivative and Schur identities, independent of a numerical optimizer.
ap=-wab/waa+wb/(A*waa)
ck('envelope_second',s.factor(-2*(wbb+wab*ap)/A+2*wb*ap/A**2-2/A*((wab-wb/A)**2/waa-wbb))==0)
z=s.symbols('z');schur=wbb-wab**2/waa
ck('Schur_completion',s.factor(z*z*waa+2*z*wab+wbb-schur-waa*(z+wab/waa)**2)==0)
a1,a2,w1,w2,U0,U1=s.symbols('a1 a2 w1 w2 U0 U1');p1=1/(1+a1);p2=p1/(1+a2)
e1=(1+a1)*U0+2*lam*w1-U1;e2=(1+a2)*U1+2*lam*w2-1
ck('original_survival_telescope',s.factor(p1*e1+p2*e2-(U0-p2+lam*2*(p1*w1+p2*w2)))==0)
ct('unweighted_cost_wrong',s.factor(2*(w1+w2)-2*(p1*w1+p2*w2))!=0)
d0=s.Rational(27,400);AA=s.Rational(3,2)-d0;xx=d0*d0/(2*(1-d0*d0))
g1=2*xx/(AA*(1+xx))-s.Rational(1,315);g2=s.Rational(1,5)-(4*AA*d0/((1-d0*d0)*(2-d0*d0))+2*xx)
ck('budget_lower_gap',g1==s.Rational(255239,19208939715)>0)
ck('multiplier_upper_gap',g2==s.Rational(179668646,254253057205)>0)
corner=(3*r**3+31*r*r+r-3)/(4*(r+3));ck('corner_limit',s.factor(F.subs(b,0)-corner)==0)
f0=(4*lam**3-6*lam**2-4*lam+3)/((2*lam+1)*(lam+1)**2)
ck('corner_lambda',s.factor(corner.subs(r,(lam-1)/(lam+1))-f0)==0)
cap=27*(lam+1)**2/(lam*(3*lam+1)**2)
P=36*lam**6-84*lam**5-311*lam**4-435*lam**3-364*lam**2-159*lam-27
ck('template_polynomial',s.factor(f0-cap-P/(lam*(lam+1)**2*(2*lam+1)*(3*lam+1)**2))==0)
ck('template_root_lower',P.subs(lam,s.Rational(47,10))==s.Rational(-1291774767,125000)<0)
ck('template_root_upper',P.subs(lam,s.Rational(24,5))==s.Rational(60779781,15625)>0)
coeff=s.Poly(P,lam).all_coeffs();ck('one_positive_sign_change',coeff[0]>0 and all(z<0 for z in coeff[1:]))
ct('lambda9over2_template_impossible',f0.subs(lam,s.Rational(9,2))==s.Rational(456,605)<s.Rational(726,841)==cap.subs(lam,s.Rational(9,2)))
ct('discarded_lambda6_template_failure',f0.subs(lam,6)==s.Rational(627,637)<s.Rational(9,8))
ct('too_large_curvature_constant',corner.subs(r,s.Rational(2,3))<s.Rational(17,20))
paths=['explorations/conditional-build/k2511-coupled-stopping-certificate-2026-11-02.md','tests/channel-swings/k2511_coupled_stopping_certificate_probe.py','explorations/conditional-build/k2509-stopping-atom-certificate-2026-11-02.md','explorations/conditional-build/k2503-stopping-instability-boundary-2026-11-02.md','explorations/conditional-build/k2507-stopping-optimal-hybrid-tail-2026-11-02.md']
report={'result':'K2511','scope':'whole-domain rational Bernstein certificate; exact derivative and rational consumer checks; adaptive transfer proved in note','checks':checks,'contrary_controls':controls,'numerator':cert,'denominator_constant':str(constant),'denominator_factors':factorcert,'kappa':str(kap),'budget':'1/315','triangular_certificate':tri,'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in paths}}
p=R/'lab/process/k2511-coupled-stopping-certificate.json'
if '--write' in sys.argv:p.write_text(json.dumps(report,indent=2)+'\n')
else:ck('saved_report_consistency',json.loads(p.read_text())==report)
print('K2511 PASS',len(checks),'checks',len(controls),'contrary controls')
