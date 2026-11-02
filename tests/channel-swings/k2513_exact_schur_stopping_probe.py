"""K2513 exact Schur stopping certificate. Default compares saved report; --write saves.
Only exact symbolic/rational certificates; no sampled theorem assertions.
"""
from pathlib import Path
from math import comb
import hashlib,json,sys
import sympy as s
R=Path(__file__).resolve().parents[2]
checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ct(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
a,b,r,X,Y=s.symbols('a b r X Y');D=2*(a+b)*(2-a-b);N=D+(b-a)**2;x=(b-a)**2/D;A=1+a
wa=s.cancel(s.diff(N,a)/N-s.diff(D,a)/D);wb=s.cancel(s.diff(N,b)/N-s.diff(D,b)/D)
waa=s.diff(wa,a);wab=s.diff(wa,b);wbb=s.diff(wb,b)
k=s.factor(-wa.subs(a,r*b));Q=s.factor(((wbb-wab**2/waa)/wa**2).subs(a,r*b))
F=s.factor((2*((wab-wb/A)**2-wbb*waa)/(A*(-2*A*wa+2*x)*waa)).subs(a,r*b))
sub={r:s.Rational(5,8)+3*X/8,b:Y/2}
def bern(poly,substitution):
 p=s.Poly(poly.subs(substitution,simultaneous=True),X,Y);nx,ny=p.degree_list();terms=p.terms()
 vals=[sum(c*s.Rational(comb(i,h),comb(nx,h))*s.Rational(comb(j,l),comb(ny,l)) for (h,l),c in terms if h<=i and l<=j) for i in range(nx+1) for j in range(ny+1)]
 reconstructed=sum(vals[i*(ny+1)+j]*comb(nx,i)*X**i*(1-X)**(nx-i)*comb(ny,j)*Y**j*(1-Y)**(ny-j) for i in range(nx+1) for j in range(ny+1))
 assert s.Poly(reconstructed-p.as_expr(),X,Y).is_zero
 return {'degree':[nx,ny],'coefficients':[str(v) for v in vals],'minimum':str(min(vals)),'maximum':str(max(vals))},vals
def certificate(name,expr,substitution,strict=False):
 n,d=s.fraction(s.factor(expr)); origin={X:0,Y:0}
 if d.subs(substitution,simultaneous=True).subs(origin)<0:n,d=-n,-d
 cert,vals=bern(n,substitution)
 ck(name+'_numerator',all(v>0 if strict else v>=0 for v in vals))
 constant,factors=s.factor_list(d);sign=s.sign(constant);ds=[]
 for i,(f,power) in enumerate(factors):
  fc,fv=bern(f,substitution); positive=min(fv)>0;negative=max(fv)<0
  ck(name+'_denominator_'+str(i),positive or negative)
  sign*=(-1 if negative else 1)**power
  fc.update(polynomial=str(f),power=int(power));ds.append(fc)
 ck(name+'_denominator_sign',sign==1)
 cert.update(denominator_constant=str(constant),denominator_factors=ds)
 return cert,n,vals
ratio,_,_=certificate('hazard_ratio',2*k-(2/(1+r)**2-s.Rational(1,2)),sub)
ck('ratio_degree',ratio['degree']==[5,2]);ck('ratio_boundary_gap',s.Rational(87,338)-s.Rational(1,4)==s.Rational(5,676)>0)
schur,sn,sv=certificate('schur',4-14*(1-2*b)*k-Q,sub)
ck('schur_degree',schur['degree']==[14,7]);ck('schur_count',len(sv)==120);ck('schur_minimum',min(sv)==0)
curvature,cn,cv=certificate('curvature',F-s.Rational(7,10)/(1+b)**3,sub,True)
ck('curvature_degree',curvature['degree']==[11,8]);ck('curvature_count',len(cv)==108);ck('curvature_minimum',min(cv)==s.Rational(10543,64))
score,v,lam,h,z=s.symbols('score v lam h z',positive=True)
B=2*v**2/lam-s.Rational(7,2)*(1-2*b)*v**3/lam**2
ck('stationary_substitution',s.factor((2*lam*(4*z*z-14*(1-2*b)*z**3)).subs(z,v/(2*lam))-B)==0)
ck('k_monotonic_derivative',s.factor(s.diff(4*z*z-14*h*z**3,z)-2*z*(4-21*h*z))==0)
ck('lambda_derivative',s.factor(s.diff(B,lam)-v**2*(-2*lam+7*(1-2*b)*v)/lam**3)==0)
ratioB=s.expand(B*(1+score-b)**3)
ck('b_ratio_derivative',s.factor(s.diff(ratioB,b)-v**2*(1+score-b)**2/lam**2*(v*(s.Rational(35,2)+7*score-28*b)-6*lam))==0)
ck('score_ratio_log_derivative',s.factor(s.diff(3*s.log(1+score)-2*s.log(1+5*score/8),score)-(s.Rational(7,4)+5*score/8)/((1+score)*(1+5*score/8)))==0)
cap=ratioB.subs({b:0,score:s.Rational(1,2),v:s.Rational(16,21),lam:4})
ck('ratio_maximum',cap==s.Rational(32,49));kap=s.Rational(92,6615)
ck('uniform_kappa',(s.Rational(7,10)-cap)*s.Rational(8,27)==kap)
tri,_,_=certificate('coupled',s.Rational(7,10)/(1+score-b)**3-B.subs({lam:4,v:1/(1+5*score/8)}),{b:X*Y/2,score:Y/2},True)
ck('triangular_degree',tri['degree']==[4,4])
ap=-wab/waa+wb/(A*waa)
ck('envelope_second',s.factor(-2*(wbb+wab*ap)/A+2*wb*ap/A**2-2/A*((wab-wb/A)**2/waa-wbb))==0)
ck('schur_completion',s.factor(z*z*waa+2*z*wab+wbb-(wbb-wab**2/waa)-waa*(z+wab/waa)**2)==0)
a1,a2,w1,w2,U0,U1=s.symbols('a1 a2 w1 w2 U0 U1');p1=1/(1+a1);p2=p1/(1+a2)
ck('original_survival_telescope',s.factor(p1*((1+a1)*U0+2*lam*w1-U1)+p2*((1+a2)*U1+2*lam*w2-1)-(U0-p2+2*lam*(p1*w1+p2*w2)))==0)
d0=s.Rational(21,250);AA=s.Rational(3,2)-d0;xx=d0*d0/(2*(1-d0*d0))
ck('budget_gap',2*xx/(AA*(1+xx))-s.Rational(1,200)==s.Rational(1019,1469796200)>0)
ck('multiplier_gap',s.Rational(1,4)-(4*AA*d0/((1-d0*d0)*(2-d0*d0))+2*xx)==s.Rational(76284905,30920027924)>0)
# Contrary controls: corruption, endpoint sampling, invalid extension, wrong weights.
bad=cn-cn.subs({r:s.Rational(5,8),b:0})-1;_,bv=bern(bad,sub);ct('corrupt_numerator_rejected',bv[0]==-1)
poly=(X-s.Rational(1,2))**2-s.Rational(1,100);ct('endpoint_sampling_insufficient',poly.subs(X,0)>0 and poly.subs(X,1)>0 and poly.subs(X,s.Rational(1,2))<0)
ct('strict_schur_boundary_false',s.factor((4-14*(1-2*b)*k-Q).subs(r,1))==0)
ct('unweighted_cost_wrong',s.factor(w1+w2-p1*w1-p2*w2)!=0)
# An exact method limiter: at lambda3 the true b0 ratio is below 5/9,
# but this defect bound already fails at 5/9. It cannot be extended wholesale.
lim=s.factor((4-14*(1-2*b)*k-Q).subs({r:s.Rational(5,9),b:0}))
ct('lambda3_defect_extension_false',lim<0)
ck('lambda3_ratio_admitted',2*k.subs({r:s.Rational(5,9),b:0})==s.Rational(16,49)<s.Rational(1,3))
ct('old_lambda4_template_false',s.Rational(49,75)<s.Rational(675,676))
paths=['explorations/conditional-build/k2513-exact-schur-stopping-2026-11-02.md','tests/channel-swings/k2513_exact_schur_stopping_probe.py','explorations/conditional-build/k2511-coupled-stopping-certificate-2026-11-02.md','explorations/conditional-build/k2503-stopping-instability-boundary-2026-11-02.md','explorations/conditional-build/k2507-stopping-optimal-hybrid-tail-2026-11-02.md']
report={'result':'K2513','scope':'exact rational whole-domain certificates; all-policy transfer in note','checks':checks,'contrary_controls':controls,'hazard_ratio':ratio,'schur_defect':schur,'curvature':curvature,'coupled':tri,'kappa':str(kap),'budget':'1/200','method_limiter':str(lim),'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in paths}}
p=R/'lab/process/k2513-exact-schur-stopping.json'
if '--write' in sys.argv:p.write_text(json.dumps(report,indent=2)+'\n')
else:ck('saved_report_consistency',json.loads(p.read_text())==report)
print('K2513 PASS',len(checks),'checks',len(controls),'contrary controls')
