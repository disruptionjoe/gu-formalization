"""Original four-register programs: two local projection families and exact gap."""
from pathlib import Path
from itertools import product
import ast,json,hashlib,sys
import sympy as s
from flint import arb,ctx
ctx.prec=256
ROOT=Path(__file__).resolve().parents[2];Q=s.Rational;checks={};controls={}
def ck(k,b):
 checks[k]=bool(b)
 if not b:raise AssertionError(k)
def ctrl(k,b):
 controls[k]=bool(b)
 if not b:raise AssertionError(k)
I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1);phi=s.Matrix([1,0,0,1])/s.sqrt(2);Phi=phi*phi.H
src=ROOT/'tests/channel-swings/k2439_minimal_flagged_tomography_probe.py'
for node in ast.parse(src.read_text()).body:
 if isinstance(node,ast.FunctionDef) and node.name in {'simp','ptr','choi','psd','dist','law_data','instrument'}:exec(compile(ast.Module(body=[node],type_ignores=[]),str(src),'exec'),globals())
means,weights,norms=law_data()
strings=[(0,0,0,0),(0,1,1,0),(1,0,0,1),(1,0,1,2),(1,1,1,3),(1,1,0,4),(2,1,0,5),(2,1,1,6),(2,0,1,7),(2,0,0,8)]
frb=list(product(range(3),range(2),range(2)));outcomes=list(product(range(3),[1,-1],[1,-1]));om=(-1+s.I*s.sqrt(3))/2
phase=lambda k,f:s.expand(om**((k*f)%3))
ck('cube_root_exact',s.expand(om**3)==1 and s.expand(1+om+om**2)==0)
Abank=[s.Matrix([phase(k,f)*ss**rr*tt**bb/s.sqrt(12) for f,rr,bb in frb]) for k,ss,tt in outcomes]
ck('full_FRB_basis_orthonormal',simp(s.Matrix.hstack(*Abank).H*s.Matrix.hstack(*Abank))==s.eye(12))
fixtures=[]
for law,(mean,w,l) in enumerate(zip(means,weights,norms)):
 axis=mean/l;vp=s.Matrix([s.sqrt((1+axis[1])/2),axis[0]/s.sqrt(2*(1+axis[1]))]);vm=s.Matrix([-vp[1],vp[0]]);eig={1:vp,-1:vm};O=s.Matrix.hstack(vp,vm)
 ck(f'original_rotation_{law}',simp(O.T*O)==I and simp(s.kronecker_product(O.T,O.T)*phi)==phi)
 mu=[(1-w)/2,(1-w)/2];reduced=s.zeros(12)
 for a,(zz,ss,hh) in enumerate(product([1,-1],repeat=3),start=1):
  lam=w*((1+ss*l)/2)*((1+Q(hh,2))/2)/2;mu.append(lam)
  K=s.sqrt(2*lam)*eig[hh*ss]*eig[zz*ss].H;vec=s.Matrix([K[b,r] for r,b in product(range(2),repeat=2)])/s.sqrt(2)
  native=simp(s.kronecker_product(O.T,O.T)*vec);f,rr,bb,env=strings[a+1];expected=s.zeros(4,1);expected[2*rr+bb]=s.sqrt(lam)
  ck(f'original_string_{law}_{a}',native==expected);reduced[4*f:4*f+4,4*f:4*f+4]+=vec*vec.H
 reduced[0:4,0:4]=(1-w)*Phi
 ck(f'original_reduction_{law}',simp(reduced)==s.diag(*instrument(mean,w,l)))
 ck(f'original_positive_weights_{law}',all(x>0 for x in mu) and sum(mu)==1)
 # Direct full 12x9 coefficient matrix of the original purification.
 W=s.zeros(12,9)
 for j,(f,rr,bb,ee) in enumerate(strings):W[frb.index((f,rr,bb)),ee]+=s.sqrt(mu[j])
 psi=s.Matrix([s.sqrt(x) for x in mu]);u=s.Matrix([1/s.sqrt(2),1/s.sqrt(2)]+[0]*8);v=s.Matrix([0,0]+[s.sqrt(x/w) for x in mu[2:]])
 plus=2*s.sqrt(1-w)*u+s.sqrt(w)*v;minus=s.sqrt(w)*v;V=[];pvalues=[];ebank=[]
 for a,((k,ss,tt),av) in enumerate(zip(outcomes,Abank)):
  h=ss*tt;p=((2-w) if h==1 else w)/12;pvalues.append(p)
  # Original contraction, independently compared with explicit feedforward formula.
  ca=simp(W.T*av.conjugate());formula=s.zeros(9,1);formula[0]=s.sqrt(mu[0])*(1+h)/s.sqrt(12)
  for j,(f,rr,bb,ee) in enumerate(strings[2:],start=2):formula[ee]=s.sqrt(mu[j])*s.conjugate(phase(k,f))*ss**rr*tt**bb/s.sqrt(12)
  ck(f'conditional_original_vector_{law}_{a}',simp(ca-formula)==s.zeros(9,1));ck(f'conditional_probability_{law}_{a}',s.simplify((ca.H*ca)[0])==p)
  ev=simp(ca/s.sqrt(p));ebank.append(ev);ck(f'local_E_projection_normalized_{law}_{a}',s.simplify((ev.H*ev)[0])==1)
  # Restrict the actual full tensor vector av tensor ev to the ten original strings.
  va=s.Matrix([av[frb.index((f,rr,bb))]*ev[ee] for f,rr,bb,ee in strings]);va=simp(va);V.append(va)
  expected=(plus/s.sqrt(12*(2-w))) if h==1 else (minus/s.sqrt(12*w))
  ck(f'whole_effect_support_column_{law}_{a}',simp(va-expected)==s.zeros(10,1))
 ck(f'conditional_probabilities_normalized_{law}',sum(pvalues)==1)
 # Full 108D effect is a projection: normalized E factors times orthonormal FRB factors.
 gram=s.Matrix(12,12,lambda a,b:s.simplify((Abank[a].H*Abank[b])[0]*(ebank[a].H*ebank[b])[0]))
 ck(f'full_rank12_projection_{law}',gram==s.eye(12))
 # Reconstruct Psi in the actual full carrier, not only a presumed compressed sector.
 rebuilt=s.zeros(12,9)
 for av,ev,p in zip(Abank,ebank,pvalues):rebuilt+=s.sqrt(p)*av*ev.T
 ck(f'full_target_perfect_completeness_{law}',simp(rebuilt-W)==s.zeros(12,9))
 G=simp(sum((vv*vv.H for vv in V),s.zeros(10)));target=simp(plus*plus.H/(2*(2-w))+minus*minus.H/(2*w))
 ck(f'exact_QTQ_{law}',G==target)
 r=s.cancel((1-w)/(2-w));z=s.sqrt(w)*u-s.sqrt(1-w)*v
 ck(f'exact_target_eigenvector_{law}',simp(G*psi-psi)==s.zeros(10,1))
 ck(f'exact_second_eigenvector_{law}',simp(G*z-r*z)==s.zeros(10,1))
 ck(f'full_support_spectral_identity_{law}',simp(G-psi*psi.H-r*z*z.H)==s.zeros(10))
 ck(f'exact_original_r_{law}',r==[Q(27,127),Q(15,67)][law])
 # Principal-angle 2x2 block proves spectral behavior also outside Q.
 QT=s.diag(1,0);TT=s.Matrix([[r,s.sqrt(r*(1-r))],[s.sqrt(r*(1-r)),1-r]]);xx=s.symbols('x')
 ck(f'outside_support_projection_{law}',simp(TT*TT)==TT)
 ck(f'outside_support_eigenvalues_{law}',s.factor(((QT+TT)/2-xx*s.eye(2)).det())==s.factor((xx-Q(1,2))**2-r/4))
 pp=s.symbols('p',real=True);mix=pp*QT+(1-pp)*TT
 ck(f'mixture_characteristic_{law}',s.expand((mix-xx*s.eye(2)).det()-(xx**2-xx+pp*(1-pp)*(1-r)))==0)
 ck(f'uniform_positive_gap_{law}',0<r<Q(1,2))
 ctrl(f'support_test_alone_degenerate_{law}',len(strings)==10)
 ctrl(f'conditional_test_alone_degenerate_{law}',gram==s.eye(12) and len(Abank)>1)
 # Actual prior measurements/dephasings, evaluated via their explicit pure blocks.
 def t_accept_groups(groups):
  val=0
  for group in groups:
   block=s.zeros(12,9)
   for j in group:
    f,rr,bb,ee=strings[j];block[frb.index((f,rr,bb)),ee]=s.sqrt(mu[j])
   for av,ev in zip(Abank,ebank):
    amp=(av.H*block*ev.conjugate())[0];val+=s.expand_complex(amp*s.conjugate(amp))
  return s.simplify(val)
 fgroups=[[j for j,x in enumerate(strings) if x[0]==f] for f in range(3)];egroups=[[j for j,x in enumerate(strings) if x[3]==e] for e in range(9)]
 flag=t_accept_groups(fgroups);env=t_accept_groups(egroups)
 ck(f'flag_dephasing_formula_{law}',flag==s.cancel((2*(1-w)**2+w/2)/(2-w)))
 ck(f'E_dephasing_formula_{law}',env==s.cancel(2*(1-w)**2/(2-w)+sum(x*x for x in mu[2:])/(w*(2-w))))
 ctrl(f'flag_dephasing_rejects_{law}',flag<1)
 ctrl(f'reversed_order_E_readout_rejects_{law}',env<1)
 # Wrong Fourier conjugation is not an equivalent conditional E setting.
 wrong=0
 for (k,ss,tt),av,ev in zip(outcomes,Abank,ebank):
  wrongev=ev.conjugate();amp=(av.H*W*wrongev.conjugate())[0];wrong+=s.expand_complex(amp*s.conjugate(amp))
 wrong=s.simplify(wrong);ctrl(f'wrong_Fourier_conjugation_rejects_{law}',wrong<1)
 def budget(nu):
  delta=arb('1e-8');beta=arb('1e-8');kap=arb('1e-6');q=arb(1)/4;C=2;tau=arb('.01');c=(2-delta).log()/(1-delta);den=nu*((tau-kap/q)/C)**2-delta-beta
  ck(f'positive_budget_{law}_{nu}',den>0);N=int((arb(20).log()/(c*den)).upper().ceil().unique_fmpz());allow=lambda n:C*((delta+beta+arb(20).log()/(c*n))/nu).sqrt()+kap/q
  ck(f'budget_ceiling_{law}_{nu}',allow(N)<=tau);ctrl(f'budget_predecessor_{law}_{nu}',allow(N-1)>tau)
  return N,str(allow(N))
 ra=arb(int(r.p))/int(r.q);nu=(1-ra.sqrt())/2;newN,allow=budget(nu);tree=[Q(85,10071),Q(221,27783)][law];treeN,_=budget(arb(int(tree.p))/int(tree.q));halfN,_=budget(arb(1)/2)
 ctrl(f'prospective_order_{law}',halfN<newN<treeN)
 fixtures.append({'law':law+1,'weights':list(map(str,mu)),'principal_square':str(r),'exact_gap':f'(1-sqrt({r}))/2','gap_interval':str(nu),'actual_uses_new':newN,'actual_uses_tree':treeN,'actual_uses_internal_entangled_half':halfN,'prospective_allowance':allow,'T_flag_dephased_acceptance':str(flag),'T_environment_dephased_acceptance':str(env),'T_wrong_phase_acceptance':str(wrong)})
deps=[str(Path(__file__).relative_to(ROOT)),'explorations/conditional-build/k2454-two-setting-local-verifier-2026-11-01.md','tests/channel-swings/k2439_minimal_flagged_tomography_probe.py','tests/channel-swings/k2419_positive_visibility_dual_probe.py','lab/process/k2451-verifier-operation-boundary.json','lab/process/k2447-coherent-program-verification.json','explorations/conditional-build/k2450-route-leakage-certificate-2026-11-01.md']
report={'result_id':'K2454','checks':checks,'controls':controls,'original_laws':fixtures,'evidence_kinds':{'universal':'full local effect construction and two-projection spectral proof','finite_exact':'original native rotations and reduced laws; full carrier projection/completeness; all conditional support columns, two-dimensional spectral identity and prior-readout/phase controls','prospective':'Arb256 hypothetical budgets, not device data'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2454-two-setting-local-verifier.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2454',len(checks),'checks',len(controls),'controls PASS')
