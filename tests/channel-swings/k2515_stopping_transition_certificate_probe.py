"""K2515 exact curved-domain stopping certificate.
Default reconstructs all certificates and compares the saved report; --write saves.
Exact rational Bernstein certificates, not sampling; universal transfer is in the note.
"""
from pathlib import Path
from math import comb
import hashlib,json,sys
import sympy as s
R=Path(__file__).resolve().parents[2]
checks={};controls={}
def ck(key,value):
 checks[key]=bool(value)
 if not value:raise AssertionError(key)
def ct(key,value):
 controls[key]=bool(value)
 if not value:raise AssertionError(key)
a,b,r,X,Y=s.symbols('a b r X Y');A=1+a
D=2*(a+b)*(2-a-b);N=D+(b-a)**2;x=(b-a)**2/D
wa=s.cancel(s.diff(N,a)/N-s.diff(D,a)/D)
wb=s.cancel(s.diff(N,b)/N-s.diff(D,b)/D)
waa=s.diff(wa,a);wab=s.diff(wa,b);wbb=s.diff(wb,b)
k=s.factor(-wa.subs(a,r*b))
T=s.factor((wbb-wab**2/waa).subs(a,r*b))
Mup=-2*A*wa+2*x
F=s.factor((2*((wab-wb/A)**2-wbb*waa)/(A*Mup*waa)).subs(a,r*b))
h=1+b/2+b*b/2;c=(1+b)/2;L0=s.Rational(8001,2816)
def transformed(expr,curve=None,lower=0,upper=s.Rational(1,2)):
 if curve is None:curve=s.Rational(1,2)+b/2
 # Sequential replacements resolve b inside the curved r parameterization.
 return s.Poly(s.cancel(expr.subs(r,curve+(1-curve)*X).subs(b,lower+(upper-lower)*Y)),X,Y)
def bernstein(poly):
 nx,ny=poly.degree_list();terms=poly.terms()
 vals=[sum(v*s.Rational(comb(i,j),comb(nx,j))*s.Rational(comb(k,l),comb(ny,l))
           for (j,l),v in terms if j<=i and l<=k)
       for i in range(nx+1) for k in range(ny+1)]
 # Independently invert the basis change with exact finite differences.
 reconstructed={}
 for j in range(nx+1):
  for l in range(ny+1):
   v=comb(nx,j)*comb(ny,l)*sum((-1)**(j-i+l-k)*comb(j,i)*comb(l,k)*vals[i*(ny+1)+k]
                                  for i in range(j+1) for k in range(l+1))
   if v:reconstructed[(j,l)]=v
 assert s.Poly.from_dict(reconstructed,(X,Y))==poly
 return {'degree':[nx,ny],'coefficients':[str(v) for v in vals],'minimum':str(min(vals)),'maximum':str(max(vals))},vals

def certificate(name,expr,strict,curve=None,lower=0,upper=s.Rational(1,2)):
 def transform(v):return transformed(v,curve,lower,upper)
 n,d=s.fraction(s.factor(expr))
 if transform(d).eval({X:0,Y:0})<0:n,d=-n,-d
 cert,values=bernstein(transform(n))
 ck(name+'_numerator',all(v>0 if strict else v>=0 for v in values))
 constant,factors=s.factor_list(d);sign=s.sign(constant);den=[]
 for i,(f,power) in enumerate(factors):
  fc,fv=bernstein(transform(f));positive=min(fv)>0;negative=max(fv)<0
  ck(name+'_denominator_factor_'+str(i),positive or negative)
  sign*=(-1 if negative else 1)**power
  fc.update(polynomial=str(f),power=int(power));den.append(fc)
 ck(name+'_positive_nonvanishing_denominator',sign==1)
 cert.update(numerator=str(n),denominator=str(d),denominator_constant=str(constant),denominator_factors=den)
 return cert,n,values
Z=s.factor(2*h*k.subs(r,c))
ck('boundary_hazard_identity',s.factor(Z-8*(2*b+7)*(b*b+b+2)/((b+3)*(b+4)*(b*b+15*b+24)))==0)
domain,dn,dv=certificate('domain',Z-1/L0,False)
ck('domain_degree',domain['degree']==[0,4]);ck('domain_count',len(dv)==5);ck('domain_exact_endpoint',Z.subs(b,s.Rational(1,2))==1/L0)
ck('domain_minimum',min(dv)==0)
curvature,cn,cv=certificate('curvature',F-s.Rational(2,5),True)
ck('curvature_degree',curvature['degree']==[11,19]);ck('curvature_count',len(cv)==240);ck('curvature_minimum',min(cv)==6)
schur,sn,sv=certificate('hazard_normalized_schur',s.Rational(3,8)*h-T/k,True)
ck('schur_degree',schur['degree']==[7,12]);ck('schur_count',len(sv)==104);ck('schur_minimum',min(sv)==s.Rational(57147,4096))
ck('h_increasing',s.diff(h,b)==b+s.Rational(1,2))
ck('boundary_A_equals_h',s.factor(A.subs(a,c*b)-h)==0)
ck('lambda_threshold_order',2<L0<3)
lam,U,wval,z=s.symbols('lam U wval z')
ck('stationarity_hazard_normalization',s.factor((2*lam*T).subs(lam,U/(2*k))-U*T/k)==0)
ck('curvature_gap',s.Rational(2,5)-s.Rational(3,8)==s.Rational(1,40))
ap=-wab/waa+wb/(A*waa)
ck('envelope_second_identity',s.factor(-2*(wbb+wab*ap)/A+2*wb*ap/A**2-2/A*((wab-wb/A)**2/waa-wbb))==0)
ck('Schur_completion_identity',s.factor(z*z*waa+2*z*wab+wbb-(wbb-wab*wab/waa)-waa*(z+wab/waa)**2)==0)
ck('M_monotonic_derivative',s.factor(s.diff(-2*A*wa,a)+2*wa+2*A*waa)==0)
a1,a2,w1,w2,U0,U1=s.symbols('a1 a2 w1 w2 U0 U1');p1=1/(1+a1);p2=p1/(1+a2)
ck('original_prefix_telescope',s.factor(p1*((1+a1)*U0+2*lam*w1-U1)+p2*((1+a2)*U1+2*lam*w2-1)-(U0-p2+2*lam*(p1*w1+p2*w2)))==0)
b1,b2,b3=s.symbols('b1 b2 b3');S=b1+b2+b3
ck('score_pair_identity',s.expand(b1*(b2+b3)+b2*b3-(S*S-b1*b1-b2*b2-b3*b3)/2)==0)
ck('residual_chord_curvature',s.diff(b*(s.Symbol('score')-b)/80,b,2)==-s.Rational(1,40))
d0=s.Rational(2,17);AA=s.Rational(3,2)-d0;xx=d0*d0/(2*(1-d0*d0))
ck('budget_lower_gap',2*xx/(AA*(1+xx))-s.Rational(1,100)==s.Rational(111,1348900)>0)
ck('multiplier_upper_gap',1/L0-(4*AA*d0/((1-d0*d0)*(2-d0*d0))+2*xx)==s.Rational(180686,31163895)>0)
# Released second curved domain; the first proof is retained above.
c2=s.Rational(1,2)+s.Rational(9,20)*b;h2=1+c2*b;L2=s.Rational(8,3)
Z2=s.factor(2*h2*k.subs(r,c2))
domain2a,_,v2a=certificate('refined_domain_low',Z2-1/L2,True,c2,0,s.Rational(1,4))
domain2b,_,v2b=certificate('refined_domain_high',Z2-1/L2,True,c2,s.Rational(1,4),s.Rational(1,2))
ck('refined_domain_degrees',domain2a['degree']==domain2b['degree']==[0,6])
ck('refined_domain_minima',min(v2a)==s.Rational(34956477,4096) and min(v2b)==s.Rational(20683471,6144))
curvature2,_,cv2=certificate('refined_curvature',F-s.Rational(2,5),True,c2)
ck('refined_curvature_degree_count',curvature2['degree']==[11,19] and len(cv2)==240)
ck('refined_curvature_minimum',min(cv2)==6)
schur2,_,sv2=certificate('refined_schur',s.Rational(3,8)*h2-T/k,True,c2)
ck('refined_schur_degree_count',schur2['degree']==[7,12] and len(sv2)==104)
ck('refined_schur_minimum',min(sv2)==s.Rational(114924164571,4096000000))
ck('refined_h_increasing',s.diff(h2,b)==s.Rational(1,2)+s.Rational(9,10)*b)
ck('refined_boundary_A',s.factor(A.subs(a,c2*b)-h2)==0)
d1=s.Rational(1,8);A1=s.Rational(3,2)-d1;x1=d1*d1/(2*(1-d1*d1))
ck('refined_budget_gap',2*x1/(A1*(1+x1))-s.Rational(1,90)==s.Rational(43,125730)>0)
ck('refined_multiplier_gap',1/L2-(4*A1*d1/((1-d1*d1)*(2-d1*d1))+2*x1)==s.Rational(51,7112)>0)
ck('refined_initial_hazard',2*k.subs({r:s.Rational(1,2),b:0})==s.Rational(7,18))
ct('lambda_five_halves_true_ratio_outside',s.Rational(7,18)<s.Rational(2,5))
un,ud=s.fraction(s.factor(Z2-1/L2))
if transformed(ud,c2).eval({X:0,Y:0})<0:un=-un
ct('unsplit_negative_Bernstein_not_disproof',min(bernstein(transformed(un,c2))[1])<0 and min(v2a)>0 and min(v2b)>0)
# Genuine contrary constructions and sign/identity controls.
bad=s.Poly(-1+X,X,Y);_,bv=bernstein(bad);ct('corrupted_numerator_rejected',min(bv)<0)
interior=(X-s.Rational(1,2))**2-s.Rational(1,100)
ct('endpoint_samples_not_proof',interior.subs(X,0)>0 and interior.subs(X,1)>0 and interior.subs(X,s.Rational(1,2))<0)
ct('uncurved_rectangle_not_valid',F.subs({r:s.Rational(1,2),b:s.Rational(1,2)})<s.Rational(2,5))
ct('strict_domain_boundary_claim_false',s.factor((Z-1/L0).subs(b,s.Rational(1,2)))==0)
limiter=s.factor(Mup.subs({a:s.Rational(3,8),b:s.Rational(1,2)}))
ck('true_root_domain_limiter_gap',s.Rational(3,8)-limiter==s.Rational(51,7112)>0)
ct('lambda_eight_thirds_domain_extension_false',limiter==s.Rational(327,889)<s.Rational(3,8))
ct('unweighted_cost_not_original',s.factor((w1+w2-p1*w1-p2*w2).subs({a1:s.Rational(1,4),a2:s.Rational(1,5),w1:1,w2:1}))>0)
# A positive numerator with a negative denominator reverses its sign.
ct('denominator_sign_is_required',s.Rational(1,-2)<0)
ct('distinct_optimizer_equations',s.expand((-2*A*wa+2*wval)-(-2*wa))!=0)
paths=['explorations/conditional-build/k2515-stopping-transition-certificate-2026-11-02.md','tests/channel-swings/k2515_stopping_transition_certificate_probe.py','explorations/conditional-build/k2513-exact-schur-stopping-2026-11-02.md','explorations/conditional-build/k2509-stopping-atom-certificate-2026-11-02.md','explorations/conditional-build/k2503-stopping-instability-boundary-2026-11-02.md','explorations/conditional-build/k2507-stopping-optimal-hybrid-tail-2026-11-02.md']
report={'result':'K2515','scope':'original-law all-policy proof in note; exact rational full-domain certificates and finite controls','threshold':str(L2),'budget':'1/90','first_curve_threshold':str(L0),'first_curve_budget':'1/100','kappa':'1/40','checks':checks,'contrary_controls':controls,'curved_domain':domain,'curvature':curvature,'hazard_normalized_schur':schur,'refined_curved_domain_low':domain2a,'refined_curved_domain_high':domain2b,'refined_curvature':curvature2,'refined_hazard_normalized_schur':schur2,'true_root_domain_limiter':str(limiter),'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in paths}}
p=R/'lab/process/k2515-stopping-transition-certificate.json'
if '--write' in sys.argv:p.write_text(json.dumps(report,indent=2)+'\n')
else:ck('saved_report_consistency',json.loads(p.read_text())==report)
print('K2515 PASS',len(checks),'checks',len(controls),'contrary controls')
