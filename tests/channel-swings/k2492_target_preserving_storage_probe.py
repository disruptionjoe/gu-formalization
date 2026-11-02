"""Exact conditional reset-to-target verifier; no hardware or GU credit."""
from pathlib import Path
from fractions import Fraction as F
import sympy as S
import json, hashlib, sys
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,x):
 checks[k]=bool(x)
 if not x:raise AssertionError('FAIL '+k)
def ct(k,x):
 controls[k]=bool(x)
 if not x:raise AssertionError('FAIL contrary '+k)
def masks(j,e):
 x=[1,1,0,int(j%2==1),int(j%2==0),0]
 return [1-z if e else z for z in x]
def sequence(w,r,u,v,gamma,n):
 if len(w)!=6 or min(w)<0 or sum(w)!=1 or not 0<r<1 or not 0<u<v<1 or not 0<=gamma<=1 or not isinstance(n,int) or n<1:raise ValueError('domain')
 pi=[v/(u+v),u/(u+v)];H=[[1-u,u],[v,1-v]]
 x=[[pi[e]*w[k]*masks(1,e)[k] for k in range(6)] for e in range(2)];out=[]
 for j in range(1,n+1):
  out.append({'q':sum(map(sum,x)),'t':x[0][0],'b0':sum(x[0][1:]),'b1':sum(x[1][1:])})
  if j==n:break
  new=[]
  for c in range(2):
   y=[sum(H[e][c]*x[e][k] for e in range(2)) for k in range(6)];o=y[:];o[1]=r*y[1]+(1-r)*y[2];o[2]=(1-r)*y[1]+r*y[2]
   z=[(1-gamma)*a for a in o];z[0]+=gamma*sum(y);new.append([masks(j+1,c)[k]*z[k] for k in range(6)])
  x=new
 return out
def vertices(f):
 vs=[[F(1),0,0,0,0,0]]
 for k in range(1,6):
  w=[F(0)]*6;w[0]=f;w[k]=1-f;vs.append(w)
 return vs
def rat(x):return S.Rational(x.numerator,x.denominator)
# Independent fixed-basis CP oracle, retaining coherent entries before first test.
r=F(27,127);u=F(1,2);v=F(8,9);gamma=F(1,4);a=1-u;h=1-gamma
Q=S.diag(1,1,0,1,0,0);T=S.diag(1,0,0,0,1,0);T[1,1]=rat(r);T[2,2]=1-rat(r);T[1,2]=T[2,1]=S.sqrt(rat(r)*(1-rat(r)));P=S.diag(1,0,0,0,0,0);I=S.eye(6)
H=[[1-u,u],[v,1-v]];pi=[v/(u+v),u/(u+v)]
def oracle(rho,g,n,swap=False,dephase=False):
 st=[rat(pi[e])*(Q if e==0 else I-Q)*rho*(Q if e==0 else I-Q) for e in range(2)];out=[]
 U=S.eye(6);U[3,3]=U[4,4]=0;U[3,4]=U[4,3]=1
 for j in range(1,n+1):
  z=sum(st,S.zeros(6));out.append((S.simplify(S.trace(z)),S.simplify(z[0,0])))
  if j==n:break
  proj=T if j%2 else Q;new=[]
  for c in range(2):
   y=sum([rat(H[e][c])*st[e] for e in range(2)],S.zeros(6))
   if swap:z=U*y*U.T
   elif dephase:z=P*y*P+(I-P)*y*(I-P)
   else:z=(1-rat(g))*y+rat(g)*S.trace(y)*P
   B=proj if c==0 else I-proj;new.append((B*z*B).applyfunc(S.simplify))
  st=new
 return out
for k in range(6):
 w=[F(0)]*6;w[k]=1
 for gg in [F(0),gamma,F(1)]:
  seq=sequence(w,r,u,v,gg,4);exact=oracle(S.diag(*w),gg,4)
  ck(f'CP_{k}_{gg}',all(rat(z['q'])==o[0] and rat(z['t'])==o[1] for z,o in zip(seq,exact)))
rho=S.zeros(6);rho[0,0]=S.Rational(9,10);rho[1,1]=rho[2,2]=rho[1,2]=rho[2,1]=S.Rational(1,20)
seq=sequence([F(9,10),F(1,20),F(1,20),0,0,0],r,u,v,gamma,4)
ck('coherent_CP',all(rat(z['q'])==o[0] and rat(z['t'])==o[1] for z,o in zip(seq,oracle(rho,gamma,4))))
ck('dephasing_trace_invariant',oracle(rho,F(0),4)==oracle(rho,F(0),4,dephase=True))
wrong=oracle(S.diag(S.Rational(9,10),0,0,S.Rational(1,10),0,0),F(0),6,swap=True)
ct('P_fixed_unitary_defeats_filter',all(t/q==S.Rational(9,10) for q,t in wrong))
for rr in [F(27,127),F(15,67)]:
 for gg in [F(1,8),F(1,4),F(1,2)]:
  for k,w in enumerate(vertices(F(9,10))):
   ss=sequence(w,rr,u,v,gg,12);zero=sequence(w,rr,u,v,F(0),12)
   ck(f'bad_factor_{rr}_{gg}_{k}',all(z['b0']+z['b1']==(1-gg)**j*(z0['b0']+z0['b1']) for j,(z,z0) in enumerate(zip(ss,zero))))
   ck(f'target_injection_{rr}_{gg}_{k}',all(ss[j+1]['t']==a*ss[j]['t']+gg*(a*ss[j]['b0']+v*ss[j]['b1']) for j in range(11)))
   ck(f'monotone_survival_{rr}_{gg}_{k}',all(0<ss[j+1]['q']<=ss[j]['q'] for j in range(11)))
# Critical exact A/B parity ratios and subcritical affine recurrence.
for gg in [F(1,8),F(1,4),F(1,2)]:
 hh=1-gg;D=hh*hh*u*v;w=vertices(F(9,10))[3];ss=sequence(w,r,u,v,gg,15)
 for k in range(7):
  x=ss[2*k]['t']/(ss[2*k]['q']-ss[2*k]['t']);y=ss[2*k+2]['t']/(ss[2*k+2]['q']-ss[2*k+2]['t'])
  ck(f'A_recurrence_{gg}_{k}',y==a*a/D*x+gg*(a*a+hh*u*v)/D)
 if D>a*a:
  R1=gg*(a*a+hh*u*v)/(D-a*a);R2=gg*a*v*(1+hh)/(D-a*a)
  ck('floor_A_constants',R1==F(23,26) and R2==F(15,13))
 if D==a*a:
  for k in range(7):
   Aseq=ss;Bseq=sequence(vertices(F(9,10))[4],r,u,v,gg,15)
   ck('critical_A_odd_'+str(k),1-Aseq[2*k]['t']/Aseq[2*k]['q']==1/(10+F(7,12)*k))
   ck('critical_B_odd_'+str(k),1-Bseq[2*k]['t']/Bseq[2*k]['q']==1/(17+F(7,9)*k))
   ck('critical_A_even_'+str(k),1-Aseq[2*k+1]['t']/Aseq[2*k+1]['q']==1/(F(40,3)+F(7,9)*k))
   ck('critical_B_even_'+str(k),1-Bseq[2*k+1]['t']/Bseq[2*k+1]['q']==1/(F(40,3)+F(7,12)*k))
# Independent forced eigenmode check for the new principal-plane floor.
aa,bb=rat(a),rat(1-v);rr=rat(r);uu,vv=rat(u),rat(v);gg=S.Rational(1,100);hh=1-gg
lam=(rr*(aa+bb)+S.sqrt(rr**2*(aa-bb)**2+4*uu*vv*(1-rr)**2))/2
zz=(lam-aa*rr)/(vv*(1-rr));ell=hh*lam
M=S.Matrix([[aa,gg*aa,gg*vv],[0,hh*aa*rr,hh*vv*(1-rr)],[0,hh*uu*(1-rr),hh*bb*rr]])
vec=S.Matrix([gg*(aa+vv*zz)/(ell-aa),1,zz])
ck('principal_supercritical_branch',ell>aa)
ck('principal_forced_eigenmode',all(S.simplify(x)==0 for x in M*vec-ell*vec))
ck('principal_ratio_normalization',S.simplify(vec[0]/sum(vec)-1/(1+(ell-aa)*(1+zz)/(gg*(aa+vv*zz))))==0)
# Frozen reset bit agrees at a single gap, changes the full temporal law.
w=vertices(F(9,10))[3];s0=sequence(w,r,u,v,F(0),5);s1=sequence(w,r,u,v,F(1),5);fresh=sequence(w,r,u,v,gamma,5)
frozen=[{k:(1-gamma)*z[k]+gamma*y[k] for k in z} for z,y in zip(s0,s1)]
ck('same_one_gap_marginal',frozen[1]==fresh[1]);ct('frozen_reset_not_fresh',frozen[2]!=fresh[2])
ct('pure_target_exception',all(z['q']==z['t'] for z in sequence([F(1),0,0,0,0,0],r,u,v,F(1,8),8)))
ct('full_reset_prepares_target',all(z['q']==z['t'] for z in s1[1:]))
# Finite exact cap consumer: prep/test/pump each price1, independent restart.
fixtures=[]
for gg in [F(1,8),F(1,4),F(1,2)]:
 allseq=[sequence(w,r,u,v,gg,60) for w in vertices(F(9,10))];rows=[]
 for n in range(1,61):
  errors=[1*z[n-1]['q']-z[n-1]['t'] for z in allseq];errors=[ee/z[n-1]['q'] for ee,z in zip(errors,allseq)]
  costs=[(2+2*sum(x['q'] for x in z[:n-1]))/z[n-1]['q'] for z in allseq]
  rows.append({'cap':n,'worst_error':str(max(errors)),'worst_renewal_cost':str(max(costs))})
 feasible=[z for z in rows if F(z['worst_error'])<=F(1,20)];best=feasible[0] if feasible else None
 if gg==F(1,4):ck('critical_first_feasible_26',best is not None and best['cap']==26)
 fixtures.append({'gamma':str(gg),'tolerance':'1/20','first_feasible_through60':best,'rows':rows})
ct('critical_requires_nonstrict_threshold',h*h*u*v==a*a and fixtures[1]['first_feasible_through60'] is not None)
for bad in [F(-1,10),F(11,10)]:
 try:sequence(w,r,u,v,bad,2);ok=False
 except ValueError:ok=True
 ct('invalid_gamma_'+str(bad),ok)
deps=['lab/process/k2490-storage-noisy-markov-verifier.json','lab/process/k2488-markov-flag-filtering.json']
report={'result':'K2492','checks':checks,'contrary_controls':controls,'fixtures':fixtures,'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps},'evidence_kinds':{'universal':'written spectral threshold, resonance, full-memory counterexample and ratio-vertex arguments','exact_finite':'rational sector recursion versus symbolic CP oracle, recurrence and charged caps','not_claimed':'measured storage, target preparation availability, arbitrary P-fixing channels or native GU physics'}}
pth=R/'lab/process/k2492-target-preserving-storage.json'
if '--write' in sys.argv:pth.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
else:ck('saved_reproduction',json.loads(pth.read_text())==report)
print(json.dumps({'result':'PASS','checks':len(checks),'controls':len(controls),'designs':[{k:v for k,v in z.items() if k!='rows'} for z in fixtures]}))
