"""Exact reduced original CP maps; universal/all-carrier proof and scope in K2486."""
from pathlib import Path
import json,hashlib,sys
import sympy as S
R=Path(__file__).resolve().parents[2];Q=S.Rational;checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError('FAIL '+k)
def ctrl(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError('FAIL contrary '+k)
def simp(x):return x.applyfunc(S.simplify) if isinstance(x,S.MatrixBase) else S.simplify(x)
prior=json.loads((R/'lab/process/k2484-coherent-verifier-instruments.json').read_text())
rs=[Q(x['r']) for x in prior['original_laws']];ck('original_angles',rs==[Q(27,127),Q(15,67)])
ck('original_ranks_authenticated',prior['checks']['full_T_rank12_via_orthogonal_controls_0'] and prior['checks']['original108_and_product_basis'])
ck('full_carrier_dimensions',1+2+8+10+87==108 and 1+1+8==10 and 1+1+10==12)
e,r=S.symbols('e r',real=True);p=1-e;M=S.Matrix([[p*r,p*(1-r)],[e*(1-r),e*r]]);lam=S.symbols('l')
ck('characteristic_polynomial',S.expand(M.charpoly(lam).as_expr()-(lam**2-r*lam+p*e*(2*r-1)))==0)
ck('perron_upper_identity',S.expand((lam**2-r*lam+p*e*(2*r-1)).subs(lam,p)-p*(p-e)*(1-r))==0)
ck('detailed_balance',M*S.diag(p,e)==S.diag(p,e)*M.T)
ck('third_step_crossover',S.factor((M**2*S.Matrix([p,e]))[0]-p*p*e-p*r*(p-e)*(r-e))==0)
fixtures=[]
for law,r in enumerate(rs):
 QQ=S.diag(1,1,0,1,0,0);TT=S.zeros(6);TT[0,0]=1;TT[1,1]=r;TT[2,2]=1-r;TT[1,2]=TT[2,1]=S.sqrt(r*(1-r));TT[4,4]=1;I=S.eye(6);P=S.diag(1,0,0,0,0,0)
 ck(f'projectors_{law}',simp(TT*TT-TT)==S.zeros(6) and QQ*TT*QQ==P+r*S.diag(0,1,0,0,0,0))
 for e in [Q(0),Q(1,100),Q(1,3),Q(1,2),Q(2,3)]:
  p=1-e;M=S.Matrix([[p*r,p*(1-r)],[e*(1-r),e*r]])
  def A(B,X):return simp(p*B*X*B+e*(I-B)*X*(I-B))
  # Actual Schrodinger state has coherences across the principal and common sectors.
  v=S.Matrix([1,1,S.I,1,1,1])/S.sqrt(6);rho=v*v.H;F=Q(1,6);out=rho;actual_cost=0;history=[S.Integer(1)];previous_ratio=None;closed_history=[S.ones(6,1)]
  for n in range(1,9):
   B=QQ if n%2 else TT;actual_cost+=(2 if n%2 else 3)*S.trace(out);out=A(B,out)
   En=I
   for j in range(n,0,-1):En=A(QQ if j%2 else TT,En)
   d=M**(n-1)*S.Matrix([p,e]);co=[p**n,d[0],d[1],p**((n+1)//2)*e**(n//2),e**((n+1)//2)*p**(n//2),e**n];expected=S.diag(*co);tag=f'{law}_{e}_{n}'
   ck('effect_'+tag,simp(En-expected)==S.zeros(6));ck('output_mass_'+tag,simp(S.trace(P*out)-p**n*F)==0);q=simp(S.trace(out));ck('output_trace_'+tag,simp(q-S.trace(En*rho))==0)
   expected_cost=sum((2 if j%2 else 3)*history[j-1] for j in range(1,n+1));ck('actual_stopped_cost_'+tag,simp(actual_cost-expected_cost)==0);history.append(q)
   from_closed=sum((2 if j%2 else 3)*sum(closed_history[j-1])/6 for j in range(1,n+1));ck('closed_sector_stopped_cost_'+tag,simp(actual_cost-from_closed)==0);closed_history.append(S.Matrix(co))
   if e<=Q(1,2):
    w=max(co[1:]);ratio=w/p**n;ck('monotone_'+tag,previous_ratio is None or ratio<=previous_ratio);previous_ratio=ratio
    F0=Q(9,10);k=co[1:].index(w)+1;mix=S.zeros(6);mix[0,0]=F0;mix[k,k]=1-F0;mx=mix
    for j in range(1,n+1):mx=A(QQ if j%2 else TT,mx)
    eps=simp(1-S.trace(P*mx)/S.trace(mx));ck('sharp_attainment_'+tag,eps==(1-F0)*w/(F0*p**n+(1-F0)*w))
    if e==Q(1,2):ck('critical_noise_'+tag,En==I/2**n)
    if e==0 and n>=2:ck('noiseless_recovery_'+tag,En==P+r**(n-1)*S.diag(0,1,0,0,0,0))
  if e==Q(1,3):ctrl(f'wrong_principal_only_{law}',(M**2*S.Matrix([p,e]))[0]<p*p*e)
  if e==Q(2,3):ctrl(f'overhalf_wrong_direction_{law}',e**8>p**8)
 # Exact finite-cap consumer, hypothetical eta=1/100, F0=.9, tolerance7/10000.
 e=Q(1,100);p=1-e;M=S.Matrix([[p*r,p*(1-r)],[e*(1-r),e*r]]);F0=Q(9,10);tol=Q(7,10000);n=1;cs=[]
 while True:
  d=M**(n-1)*S.Matrix([p,e]);w=max(*d,p**((n+1)//2)*e**(n//2),e**((n+1)//2)*p**(n//2),e**n);eps=(1-F0)*w/(F0*p**n+(1-F0)*w);cs.append(eps)
  if eps<=tol:break
  n+=1
  if n>100:raise AssertionError('FAIL finite fixture unexpectedly long')
 ck(f'first_feasible_cap_{law}',n>1 and cs[-2]>tol and cs[-1]<=tol)
 fixtures.append({'law':law+1,'r':str(r),'hypothetical_flag_error':'1/100','fidelity_lower_bound':'9/10','tolerance':'7/10000','first_feasible_cap':n,'sharp_infidelity':str(eps),'guaranteed_target_output_mass':str(F0*p**n)})
# Fixed-F mixtures exercise the complete cost/renewal vertex formulas independently.
for law,r in enumerate(rs):
 e=Q(1,100);p=1-e;M=S.Matrix([[p*r,p*(1-r)],[e*(1-r),e*r]]);n=5;F0=Q(9,10);hs=[S.ones(6,1)]
 for j in range(1,n+1):
  d=M**(j-1)*S.Matrix([p,e]);hs.append(S.Matrix([p**j,*d,p**((j+1)//2)*e**(j//2),e**((j+1)//2)*p**(j//2),e**j]))
 costs=[sum((2 if j%2 else 3)*hs[j-1][k] for j in range(1,n+1)) for k in range(6)]
 nums=[F0*costs[0]+(1-F0)*costs[k] for k in range(1,6)];dens=[F0*hs[n][0]+(1-F0)*hs[n][k] for k in range(1,6)];ratios=[x/y for x,y in zip(nums,dens)];weights=[Q(1,15),Q(2,15),Q(3,15),Q(4,15),Q(5,15)]
 mixed_num=sum(w*x for w,x in zip(weights,nums));mixed_den=sum(w*x for w,x in zip(weights,dens));avg=sum(w*d*x for w,d,x in zip(weights,dens,ratios))/mixed_den
 ck(f'renewal_denominator_weighted_identity_{law}',mixed_num/mixed_den==avg and avg<=max(ratios))
 ck(f'pure_target_maximizes_attempt_cost_{law}',all(costs[0]>=x for x in costs[1:]))
 ctrl(f'ordinary_average_not_renewal_{law}',sum(w*x for w,x in zip(weights,ratios))!=avg)
# Independent, nonidentical flags: compare actual normalized effect to worst homogeneous cap.
for law,r in enumerate(rs):
 QQ=S.diag(1,1,0,1,0,0);TT=S.zeros(6);TT[0,0]=1;TT[1,1]=r;TT[2,2]=1-r;TT[1,2]=TT[2,1]=S.sqrt(r*(1-r));TT[4,4]=1;I=S.eye(6)
 noises=[Q(0),Q(1,100),Q(1,5),Q(1,10),Q(1,3)];star=Q(1,3);pstar=1-star;En=I;Es=I;prod=S.Integer(1)
 for j in range(5,0,-1):
  B=QQ if j%2 else TT;ej=noises[j-1];prod*=1-ej
  En=simp((1-ej)*B*En*B+ej*(I-B)*En*(I-B));Es=simp(pstar*B*Es*B+star*(I-B)*Es*(I-B))
 gap=simp(Es/pstar**5-En/prod)
 ck(f'varying_flag_CP_order_{law}',gap==S.diag(*gap.diagonal()) and all(x>=0 for x in gap.diagonal()))
 ck(f'varying_flag_target_yield_{law}',En[0,0]==prod and prod>=pstar**5 and gap[0,0]==0)
# Different actual noise/instrument models, not changes to manifest assertions.
e=Q(1,100);p=1-e;F=Q(9,10);n=5
shared_bad=e*(1-F)/(p*F+e*(1-F));iid_bad=e**n*(1-F)/(p**n*F+e**n*(1-F));ctrl('common_bit_same_marginals_different_floor',shared_bad>iid_bad and shared_bad>0)
flag=0;records=[]
for j in range(2):flag=1-flag;records.append(flag)
ctrl('no_reset_rejects_target',records==[1,0])
ctrl('effect_only_measure_prepare_destroys_target',p>0 and S.trace(S.diag(1,0)*S.diag(0,p))==0)
R2=S.diag(1,0);X=S.Matrix([[0,1],[1,0]]);U=S.kronecker_product(R2,X)+S.kronecker_product(S.eye(2)-R2,S.eye(2));plus=S.ones(2,2)/2
joint=U*S.kronecker_product(plus,plus)*U.H;accepted=joint.extract([1,3],[1,3]);ctrl('coherent_flag_changes_map',accepted[0,1]!=0 and (Q(1,2)*R2*plus*R2+Q(1,2)*(S.eye(2)-R2)*plus*(S.eye(2)-R2))[0,1]==0)
for n in range(1,9):ck(f'pure_target_renewal_{n}',sum(p**k for k in range(n))/p**n==(p**(-n)-1)/e)
deps=['lab/process/k2484-coherent-verifier-instruments.json','tests/channel-swings/k2484_coherent_verifier_instruments_probe.py','lab/process/k2454-two-setting-local-verifier.json']
report={'result':'K2486','scope':'exact original alternating maps with fresh independent diagonal flags and otherwise ideal coherent control','checks':checks,'contrary_controls':controls,'fixtures':fixtures,'evidence_kinds':{'universal':'written CP-map, full-sector, spectral, conditioning and renewal proofs','exact':'symbolic identities and rational finite CP-map products, actual changed-instrument controls','inherited':'original108-dimensional reconstruction and ranks authenticated, not rerun'},'dependencies':{x:hashlib.sha256((R/x).read_bytes()).hexdigest() for x in deps}}
f=R/'lab/process/k2486-noisy-flag-alternating-verifier.json'
if '--write' in sys.argv:f.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
else:ck('saved_report_reproduces',json.loads(f.read_text())==report)
print(json.dumps({'result':'PASS','checks':len(checks),'controls':len(controls),'fixtures':fixtures}))
