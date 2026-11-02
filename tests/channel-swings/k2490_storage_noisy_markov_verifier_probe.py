"""Exact finite controls for the conditional storage/Markov theorem; prose owns universal proof."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,sys
import sympy as S
R=Path(__file__).resolve().parents[2]
dims=[1,1,1,8,10,87];checks={};controls={}
def ck(k,x):
 checks[k]=bool(x)
 if not x:raise AssertionError(k)
def ct(k,x):
 controls[k]=bool(x)
 if not x:raise AssertionError('contrary '+k)
def Hpower(u,v,m):
 if not (0<u<v<1 and isinstance(m,int) and m>=1):raise ValueError('Markov domain')
 t=(1-u-v)**m;eta=u/(u+v);um=eta*(1-t);vm=(1-eta)*(1-t)
 return [[1-um,um],[vm,1-vm]]
def masks(j,e):
 z=[1,1,0,int(j%2==1),int(j%2==0),0]
 return [1-x if e else x for x in z]
def sequence(weights,r,u,v,m,delta,n):
 if len(weights)!=6 or min(weights)<0 or sum(weights)!=1 or not 0<r<1 or not 0<=delta<=1 or not isinstance(n,int) or n<1:raise ValueError('state/control domain')
 H=Hpower(u,v,m);pi=[v/(u+v),u/(u+v)]
 x=[[pi[e]*weights[k]*masks(1,e)[k] for k in range(6)] for e in range(2)]
 out=[]
 for j in range(1,n+1):
  out.append((sum(map(sum,x)),sum(z[0] for z in x)))
  if j==n:break
  xx=[]
  for c in range(2):
   y=[sum(H[e][c]*x[e][k] for e in range(2)) for k in range(6)];q=sum(y)
   o=y[:];o[1]=r*y[1]+(1-r)*y[2];o[2]=(1-r)*y[1]+r*y[2]
   xx.append([masks(j+1,c)[k]*((1-delta)*o[k]+delta*F(dims[k],108)*q) for k in range(6)])
  x=xx
 return out
def vertices(F0):
 p=[F(1)]+[F(0)]*5;vs=[p]
 for k in range(1,6):
  x=[F(0)]*6;x[0]=F0;x[k]=1-F0;vs.append(x)
 return vs
def design(r,u,v,m,e,F0,nmax=24):
 delta=1-(1-e)**m;seq=[sequence(x,r,u,v,m,delta,nmax) for x in vertices(F0)]
 rows=[]
 for n in range(1,nmax+1):
  errs=[1-s[n-1][1]/s[n-1][0] for s in seq]
  # prep1, test1, each underlying memory transition price1/10.
  costs=[(1+sum([F(1)]+[z[0] for z in s[:n-1]])+F(m,10)*sum(z[0] for z in s[:n-1]))/s[n-1][0] for s in seq]
  rows.append({'n':n,'worst_error':str(max(errs)),'worst_renewal_cost':str(max(costs))})
 return rows
# Independent fixed-basis selective CP oracle; aggregated multiplicities are explicit.
r=F(27,127);u=F(1,5);v=F(7,10);delta=F(1,100);m=2
q=S.diag(1,1,0,1,0,0);t=S.diag(1,0,0,0,1,0);t[1,1]=S.Rational(r.numerator,r.denominator);t[2,2]=1-t[1,1];t[1,2]=t[2,1]=S.sqrt(t[1,1]*(1-t[1,1]));I=S.eye(6);reset=S.diag(*dims)/108
H=Hpower(u,v,m);pi=[v/(u+v),u/(u+v)]
def sq(x):return S.Rational(x.numerator,x.denominator)
def oracle(rho,n,reset_override=None,return_state=False):
 reset_used=reset if reset_override is None else reset_override
 states=[sq(pi[e])*(q if e==0 else I-q)*rho*(q if e==0 else I-q) for e in range(2)];out=[]
 for j in range(1,n+1):
  z=sum(states,S.zeros(6));out.append((S.simplify(S.trace(z)),S.simplify(z[0,0])))
  if j==n:break
  proj=t if j%2==1 else q;new=[]
  for c in range(2):
   y=sum([sq(H[e][c])*states[e] for e in range(2)],S.zeros(6));z=(1-sq(delta))*y+sq(delta)*S.trace(y)*reset_used;P=proj if c==0 else I-proj
   new.append((P*z*P).applyfunc(S.simplify))
  states=new
 return sum(states,S.zeros(6)) if return_state else out
for k in range(6):
 x=[F(0)]*6;x[k]=1;seq=sequence(x,r,u,v,m,delta,3);o=oracle(S.diag(*x),3)
 ck('CP_sector_'+str(k),all(S.simplify(sq(a)-b)==0 for row,rr in zip(seq,o) for a,b in zip(row,rr)))
rho=S.zeros(6);rho[0,0]=S.Rational(9,10);rho[1,1]=rho[2,2]=rho[1,2]=rho[2,1]=S.Rational(1,20)
ck('coherent_theta_oracle',all(S.simplify(sq(a)-b)==0 for row,rr in zip(sequence([F(9,10),F(1,20),F(1,20),0,0,0],r,u,v,m,delta,3),oracle(rho,3)) for a,b in zip(row,rr)))
ck('multiplicities',sum(dims)==108 and sum(dims[k]*masks(1,0)[k] for k in range(6))==10 and sum(dims[k]*masks(2,0)[k] for k in range(6))==12)
ct('six_dimensional_reset_wrong',oracle(S.diag(1,0,0,0,0,0),2,reset_override=I/6)!=oracle(S.diag(1,0,0,0,0,0),2))
for rr in [F(27,127),F(15,67)]:
 for gap in [1,2,4]:
  for dd in [F(0),F(1,1000),F(1)]:
   for ix,x in enumerate(vertices(F(9,10))):
    seq=sequence(x,rr,u,v,gap,dd,8);hh=Hpower(u,v,gap)
    for j,(prob,target) in enumerate(seq,1):
     ck(f'positive_{rr}_{gap}_{dd}_{ix}_{j}',0<=target<=prob<=1)
     if j>1:
      rank=10 if j%2 else 12;L=max(hh[0][0],hh[1][0]);B=dd*((rank-1)*L+(108-rank)*(1-L))/108;G=(1-dd+dd/108)*L
      bound=B/(B+G) if B+G else F(0)
      ck(f'floor_{rr}_{gap}_{dd}_{ix}_{j}',1-target/prob>=bound)
    if dd==0 and ix==0:ck(f'ideal_target_{rr}_{gap}',all(z==prob for prob,z in seq))
# Independent K2488 closed effect, including every original sector.
for rr in [F(27,127),F(15,67)]:
 for gap in [1,2]:
  hh=Hpower(u,v,gap);uu=hh[0][1];vv=hh[1][0];aa=1-uu;bb=1-vv;pi0=vv/(uu+vv);pi1=1-pi0
  for n in range(1,9):
   z0=z1=F(1)
   for _ in range(n-1):z0,z1=aa*rr*z0+uu*(1-rr)*z1,vv*(1-rr)*z0+bb*rr*z1
   coeff=[pi0*aa**(n-1),pi0*z0,pi1*z1,pi0*uu**(n//2)*vv**((n-1)//2),pi1*vv**(n//2)*uu**((n-1)//2),pi1*bb**(n-1)]
   for k in range(6):
    x=[F(0)]*6;x[k]=1;qq,tt=sequence(x,rr,u,v,gap,F(0),n)[-1]
    ck(f'K2488_recovery_{rr}_{gap}_{n}_{k}',qq==coeff[k] and tt==(coeff[0] if k==0 else 0))

# Hidden noise on all gaps jointly can leave a noiseless accepted subensemble; not the fresh law.
pure=[F(1),0,0,0,0,0];ee=F(1,100);ss0=sequence(pure,r,u,v,2,F(0),3);ss1=sequence(pure,r,u,v,2,F(1),3);fresh=sequence(pure,r,u,v,2,ee,3);common=[tuple((1-ee)*a+ee*b for a,b in zip(x,y)) for x,y in zip(ss0,ss1)]
ck('common_storage_same_single_gap',common[1]==fresh[1])
ct('common_storage_bit_not_fresh',common[2]!=fresh[2])
Ptar=S.diag(1,0,0,0,0,0);state=oracle(S.diag(1,0,0,0,0,0),3,return_state=True);filtered=Ptar*state*Ptar
ct('final_rank_one_escapes_floor',S.trace(filtered)>0 and S.simplify(filtered[0,0]/S.trace(filtered))==1)
ct('n1_no_storage_floor',sequence([F(1),0,0,0,0,0],r,u,v,1,F(1),1)[0][0]==sequence([F(1),0,0,0,0,0],r,u,v,1,F(1),1)[0][1])
# Pure target, delta1: final normalized output fidelity follows rank and hidden weights, not input F.
H=Hpower(u,v,2);first=sequence([F(1),0,0,0,0,0],r,u,v,2,F(1),2);L=H[0][0]
ck('complete_reset_closed_form',first[1][1]/first[1][0]==L/(12*L+96*(1-L)))
# Convexity consumer: ratios of affine positive maps are denominator-weighted vertex ratios.
vtx=vertices(F(9,10));mix=[sum(x[k] for x in vtx)/6 for k in range(6)];seqs=[sequence(x,r,u,v,2,F(1,1000),8) for x in vtx];mm=sequence(mix,r,u,v,2,F(1,1000),8)
ck('vertex_fractional_bound',all(min(z[j][1]/z[j][0] for z in seqs)<=mm[j][1]/mm[j][0]<=max(z[j][1]/z[j][0] for z in seqs) for j in range(8)))
fixtures={}
for eps in [F(1,100000),F(1,1000)]:
 for gap in [1,2,4]:
  rows=design(F(27,127),F(1,2),F(3,4),gap,eps,F(9,10));feasible=[x for x in rows if F(x['worst_error'])<=F(1,100)]
  best=min(feasible,key=lambda x:F(x['worst_renewal_cost'])) if feasible else None
  fixtures[str(eps)+'_gap'+str(gap)]={'per_transition_noise':str(eps),'gap':gap,'delta_gap':str(1-(1-eps)**gap),'best_within_caps1_24':best,'rows':rows}
ct('spacing_changes_storage',1-(1-F(1,1000))**2>F(1,1000))
# Invalid declared laws fail before computation.
for name,args in [('negative_delta',([F(1),0,0,0,0,0],r,u,v,1,F(-1,10),2)),('zero_cap',([F(1),0,0,0,0,0],r,u,v,1,F(0),0))]:
 try:sequence(*args);ok=False
 except ValueError:ok=True
 ct(name,ok)
deps=['lab/process/k2488-markov-flag-filtering.json','lab/process/k2484-coherent-verifier-instruments.json']
report={'result':'K2490','checks':checks,'contrary_controls':controls,'fixtures':fixtures,'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps},'evidence_kinds':{'universal':'written linear transfer, last-noise floor and vertex arguments','exact_finite':'rational transfer, symbolic CP oracle, cap design','not_claimed':'native GU, measured device or unrestricted gap optimality; computation scans caps1_24, written cost monotonicity proves global earliest-cap optimality for each fixed gap'}}
p=R/'lab/process/k2490-storage-noisy-markov-verifier.json'
if '--write' in sys.argv:p.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
else:ck('saved_reproduction',json.loads(p.read_text())==report)
print(json.dumps({'result':'PASS','checks':len(checks),'controls':len(controls),'designs':{k:v['best_within_caps1_24'] for k,v in fixtures.items()}},default=str))
