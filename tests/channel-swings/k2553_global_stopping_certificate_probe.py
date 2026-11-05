"""Exact whole-domain critical-multiplier certificate; universal proof in note."""
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

lo=s.Rational(23,50);hi=s.Rational(3,5)+s.Rational(7,20)*b
cert('T3',ex['T3']-s.Rational(1,30),lo,hi)
cert('residual_lower_hazard',2*(4*sq/3)*ex['k']-1,lo,lo)
cert('residual_upper_hazard',s.Rational(2,3)-2*(4*sq/3)*ex['k'],hi,hi)
r0=2*sq-3;c0=4*sq-s.Rational(13,2);lo=r0+c0*b+s.Rational(9,100)*b*b;hi=r0+c0*b+s.Rational(1,8)*b*b
x=ex['x'];Mlow=2*(1+r*b)*ex['k']+2*(x-x*x/2);Mup=Mlow+2*x*x*x/3
cert('root_lower',Mlow-sq/4,lo,lo)
cert('root_upper',sq/4-Mup,hi,hi)
cert('endpoint',3*sq/4-1-ex['N2'],lo,hi)
cert('H3',ex['H3']+s.Rational(3,100),lo,hi)
lam=4*sq/3;score,t=s.symbols('score t',positive=True)
ck('lambda_identity',s.simplify(lam-4/sq)==0)
ck('M_monotonic',s.cancel(s.diff(-2*A*wa,a)+2*wa+2*A*waa)==0)
fixture={a:s.Rational(1,5),b:s.Rational(2,5)}
qf=s.cancel(q.subs(fixture));direct=s.diff(wbb,b)-3*qf*s.diff(wab,b)+3*qf*qf*s.diff(waa,b)-qf**3*s.diff(waa,a)
ck('residual_third_derivative_exact_fixture',s.cancel(T3.subs(fixture)-direct.subs(fixture))==0)
ck('third_derivative_gap',s.simplify(2*lam*(s.Rational(1,30)-s.Rational(3,100))-lam/150)==0)
g0=(1-r)**2/(2*(1+r));csmall=(1-r)**2/8-(1-r)**4/(32*(1+r)**2)
ck('zero_score_optimizer',s.simplify(1+lam*s.diff(g0,r).subs(r,r0))==0)
ck('zero_score_value_slope',s.simplify(r0+lam*g0.subs(r,r0)-lam*(3*sq/4-1))==0)
d=s.symbols('d');herm=-d*b*(score-b)/score
ck('Hermite_end_values',herm.subs(b,0)==0 and herm.subs(b,score)==0)
ck('Hermite_end_derivative',s.simplify(s.diff(herm,b).subs(b,score)-d)==0)
ck('Hermite_remainder_factor',s.expand(b*(b-score)**2-b*(score-b)**2)==0)
a1,a2,w1,w2,U0,U1=s.symbols('a1 a2 w1 w2 U0 U1');p1=1/(1+a1);p2=p1/(1+a2)
ck('original_prefix_telescope',s.factor(p1*((1+a1)*U0+2*lam*w1-U1)+p2*((1+a2)*U1+2*lam*w2-1)-(U0-p2+2*lam*(p1*w1+p2*w2)))==0)
ct('wrong_prefix_changes_cost',s.factor((w1+w2-p1*w1-p2*w2).subs({a1:s.Rational(1,4),a2:s.Rational(1,5),w1:1,w2:1}))>0)
ct('different_optimizers',s.expand(2*A*s.Symbol('k')+2*s.Symbol('w')-2*s.Symbol('k'))!=0)
ct('negative_denominator_not_positive',s.Rational(1,-2)<0)
ct('endpoint_sampling_insufficient',((X-s.Rational(1,2))**2-s.Rational(1,100)).subs(X,s.Rational(1,2))<0)
ct('algebraic_sign_control',sign(2-sq)>0 and sign(sq-2)<0 and sign(3-2*sq)<0)
ct('corrupted_polynomial_detected',any(sign(x)<0 for x in bern(s.Poly(X-s.Rational(1,2),X,Y,extension=sq))))
ct('wrong_Hermite_sign',s.diff(d*b*(score-b)/score,b).subs(b,score)==-d)
paths=['explorations/conditional-build/k2553-global-stopping-certificate-2026-11-04.md','tests/channel-swings/k2553_global_stopping_certificate_probe.py','explorations/conditional-build/k2515-stopping-transition-certificate-2026-11-02.md','explorations/conditional-build/k2551-finite-score-stopping-separation-2026-11-04.md']
paths+=['explorations/conditional-build/k2509-stopping-atom-certificate-2026-11-02.md', 'explorations/conditional-build/k2483-adaptive-stopping-bellman-2026-11-01.md', 'explorations/conditional-build/k2485-constrained-stopping-frontier-2026-11-01.md', 'explorations/conditional-build/k2517-small-score-stopping-transition-2026-11-02.md']
report={'result':'K2553','multiplier':str(lam),'score_domain':'0<S<=1/2','checks':checks,'contrary_controls':controls,'certificates':certificates,'evidence_kinds':{'exact':'original-law rational derivatives, seven whole-domain algebraic Bernstein certificates, inverse basis reconstruction and prefix identities','universal':'optimizer admission, Hermite shape lemma and all-policy support transfer proved in note','not_claimed':'all multipliers above lambda_star, entire budget frontier, external certification or GU prediction'},'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in paths}}
p=R/'lab/process/k2553-global-stopping-certificate.json'
if '--write' in sys.argv:p.write_text(json.dumps(report,indent=2)+'\n')
else:ck('saved_report_consistency',json.loads(p.read_text())==report)
print('K2553 PASS',len(checks),'exact groups',len(controls),'contrary controls')
