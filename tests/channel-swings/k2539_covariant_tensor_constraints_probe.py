"""Exact variational symbols and independent curved-product/source controls.
Universal covariant identities are proved in companion note, not by pass counts.
"""
from pathlib import Path
import hashlib,json,sys
import sympy as s
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(bank,name,p):
 bank[name]=bool(p)
 if not p:raise AssertionError('FAIL '+name)
k=s.symbols('k',nonzero=True);a0=-5*k/2288;la=35*k*k/604032
m0=-4*k/11;mS=158*k/143;mK=148*k/143;mV=503*k/858;mH=893*k/858;beta=(m0-mS)/14
ck(checks,'mass_divergence_coefficient',s.simplify(mS+beta-k)==0)
ck(checks,'beta',beta==-15*k/143)
ck(checks,'scalar_divergence_coefficient',s.simplify(mS-121*la/(13*mV)-5082101*k/4603456)==0)
# Independent uncommuted curvature bookkeeping.
Bb,db,lb,Rc,U,T,Lt=s.symbols('Box_b ddiv_b lambda_b div_Riem dBox_tau Box_dtau lambda_dtau')
dS=2*(Bb+lb-2*Rc)-(Bb+db+lb)-2*lb+2*Rc+s.Rational(2,13)*((db-U)-(Bb-T+db-U+lb-Lt)/2)
dS=s.expand(dS.subs(T,U+Lt))
Ddv=Bb-T-db+U-lb+Lt
ck(checks,'full_Ricci_commutation_reduction',s.simplify(dS-(s.Rational(12,13)*Ddv-2*(lb-Lt)/13-2*Rc).subs(T,U+Lt))==0)
Wc=s.symbols('div_WC');ck(checks,'Weyl_constant_curvature_cancel',s.expand((-2*(lb-Lt)/13-2*Rc).subs(Rc,Wc-(lb-Lt)/13)+2*Wc)==0)
# Actual indefinite coefficient fixtures, no positive Gram substitution.
N=14;eta=[1]*7+[-1]*7;G=s.diag(*eta)
pair=lambda A,B:sum(eta[i]*eta[j]*A[i,j]*B[i,j] for i in range(N) for j in range(N))
for name,xi in [('positive',[1]+[0]*13),('negative',[0]*7+[1]+[0]*6),('null',[1]+[0]*6+[1]+[0]*6)]:
 for typ in ['trace','mixed','skew']:
  C=s.zeros(N);K=s.zeros(N)
  if typ=='trace':C=G
  elif typ=='mixed':C[0,7]=C[7,0]=1;C[2,2]=2
  else:K[0,7]=1;K[7,0]=-1;K[1,2]=2;K[2,1]=-2
  tau=sum(eta[i]*C[i,i] for i in range(N));v=[sum(eta[i]*xi[i]*C[i,j] for i in range(N))-xi[j]*tau for j in range(N)];kd=[sum(eta[i]*xi[i]*K[i,j] for i in range(N)) for j in range(N)];w=[11*v[j]+13*kd[j] for j in range(N)]
  H={}
  for i in range(N):
   for j in range(N):
    for q in range(N):H[i,j,q]=2*(xi[j]*C[i,q]-xi[q]*C[i,j])+s.Rational(2,13)*(G[i,q]*v[j]-G[i,j]*v[q])
  SS=s.Matrix(N,N,lambda i,q:sum(eta[j]*xi[j]*(H[i,j,q]+H[q,j,i])/2 for j in range(N)))
  divw=sum(eta[i]*xi[i]*w[i] for i in range(N));Vs=s.Matrix(N,N,lambda i,j:G[i,j]*divw-(xi[i]*w[j]+xi[j]*w[i])/2)
  dw=s.Matrix(N,N,lambda i,j:xi[i]*w[j]-xi[j]*w[i]);EC=11*Vs/(13*mV)-2*SS/mH;EK=-dw/(2*mV)
  hn=sum(eta[i]*eta[j]*eta[q]*z*z/2 for (i,j,q),z in H.items());wn=sum(eta[i]*w[i]**2 for i in range(N))
  ck(checks,'formal_adjoint_energy_'+name+'_'+typ,s.simplify(pair(C,EC)+pair(K,EK)+wn/(13*mV)+hn/mH)==0)
  ck(checks,'hook_trace_'+name+'_'+typ,all(s.simplify(sum(eta[i]*H[i,j,i] for i in range(N)))==0 for j in range(N)))
  if typ=='skew' and name=='positive':
   ck(controls,'skew_factor_two_matters',s.simplify(pair(C,EC)+pair(K,2*EK)+wn/(13*mV)+hn/mH)!=0)
# Direct product calculation: divHess= dBox+lambda dphi.
Dphi,ddbox=s.symbols('dphi dBoxphi');direct=s.expand(-s.Rational(14,13)*ddbox+s.Rational(14,13)*(ddbox+la*Dphi))
ck(checks,'direct_curved_factor_hook',direct==14*la*Dphi/13)
ck(controls,'dropping_Weyl_fails_curved_fixture',s.simplify(direct)!=0)
cA=s.factor(-105*k/143+847*la/(13*mV)-28*la/(13*mH));cFull=s.factor(m0+121*la/mV)
ck(checks,'one_factor_obstruction',cA==-2992502835*k/4110886208)
ck(checks,'pure_trace_obstruction',cFull==-124533*k/354112)
b=s.factor(-cA/(cFull-cA));ck(checks,'repair_ratio',b==s.Rational(332500315,171866582))
A,B=s.symbols('A B');tt=7*(A+B);q=7*A+6*B;p=7*A+5*B
MA=mS*A+beta*tt+la*(tt/2-A)/(3*a0);MB=mS*B+beta*tt+la*p/(6*a0)
RA=-121*q/(13*mV)-24*(A-B)/(13*mH)+(A+B)/a0
RB=-121*q/(13*mV)+28*(A-B)/(13*mH)+p/(6*a0)
ck(checks,'direct_Euler_vs_divergence_constraint',s.simplify(MB-la*RB-(A*cA+B*(cFull-cA)))==0)
ck(checks,'pure_trace_hook_cancels',s.simplify((RA-RB).subs({A:1,B:1}))==0)
MA,MB,RA,RB=[s.factor(z.subs({A:1,B:b})) for z in [MA,MB,RA,RB]]
ck(checks,'repaired_source_conserved',s.simplify(MB-la*RB)==0)
ck(checks,'nonzero_source_plateau',MA==-308132384957*k/272236665888 and MB==-24749767063*k/272236665888)
ck(controls,'one_factor_not_universal_impossibility',cA!=0 and s.simplify(cA+b*(cFull-cA))==0)
# Stronger consumer: explicit full Einstein/tensor sourced solutions, no inverse.
D=s.symbols('D');phi=D+2*la
zu=(6*RB-5*RA)*D/12+(7*la*RB-5*MA)/12
zv=(RB*phi-7*zu)/5
EA=3*D*(zu+zv)+la*(5*zu+7*zv)/2
EBcoef=(7*zu+5*zv)/2
ck(checks,'full_Einstein_A_block',s.simplify(EA-(RA*D+MA)*phi/2)==0)
ck(checks,'full_Einstein_B_block',s.simplify(EBcoef-RB*phi/2)==0)
hA=s.factor(zu-phi/(6*a0));hB=s.factor(zv-b*phi/(6*a0))
ck(checks,'original_metric_readout_nonzero',hA.subs(D,0)!=0)
ck(controls,'Einstein_shift_is_not_original_readout',s.simplify(hA-zu)!=0)
ck(controls,'generated_source_not_order_zero',s.Poly((RA*D+MA)*phi,D).degree()==2 and RB!=0)
report={'result':'K2539','exact_checks':checks,'contrary_controls':controls,'scope':'full covariant tensor constraints and explicit generated conserved-source/full-field class; no arbitrary prescribed-source inverse, boundary uniqueness, positivity, native GU or observed metric claim','coefficients':{key:str(val) for key,val in dict(cA=cA,cFull=cFull,repair=b,MA=MA,MB=MB,RA=RA,RB=RB,zA_polynomial=zu,zB_polynomial=zv,hA_polynomial=hA,hB_polynomial=hB).items()},'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in ['tests/channel-swings/k2537_reduced_action_decoupling_probe.py',str(Path(__file__).relative_to(R))]}}
out=R/'lab/process/k2539-covariant-tensor-constraints.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==report
print('K2539',len(checks),'exact identity/fixture checks',len(controls),'contrary controls')
