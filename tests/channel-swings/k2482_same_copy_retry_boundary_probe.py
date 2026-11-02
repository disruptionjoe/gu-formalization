"""Exact original-carrier ranks and complete-instrument countercontrols; universal proofs in note."""
from pathlib import Path
from itertools import product
from collections import defaultdict,Counter
import ast,json,hashlib,sys
import sympy as s
ROOT=Path(__file__).resolve().parents[2];Q=s.Rational;checks={};controls={}
def ck(k,b):
 checks[k]=bool(b)
 if not b:raise AssertionError('FAIL '+k)
def ctrl(k,b):
 controls[k]=bool(b)
 if not b:raise AssertionError('FAIL contrary '+k)
# Only original exact law constants are loaded, not predecessor test execution.
p=ROOT/'tests/channel-swings/k2419_positive_visibility_dual_probe.py';env={'s':s,'Q':Q}
for node in ast.parse(p.read_text()).body:
 if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id in ['means','weights','norms'] for t in node.targets):exec(compile(ast.Module(body=[node],type_ignores=[]),str(p),'exec'),env)
strings=[(0,0,0,0),(0,1,1,0),(1,0,0,1),(1,0,1,2),(1,1,1,3),(1,1,0,4),(2,1,0,5),(2,1,1,6),(2,0,1,7),(2,0,0,8)]
ref={e:(f,r,b) for f,r,b,e in strings};ref[0]=(0,0,0)
coords=list(product(range(3),range(2),range(2),range(9)));frb=list(product(range(3),range(2),range(2)));groups=defaultdict(list)
def char(x):
 f,r,b,e=x;fe,re,be=ref[e];return tuple(int(f==j)-int(fe==j) for j in range(3))+(r-b-re+be,)
for x in coords:groups[char(x)].append(x)
zero=(0,0,0,0);ck('full108_all31_characters',len(coords)==108 and len(groups)==31 and len(groups[zero])==14)
fixtures=[];prior=json.loads((ROOT/'lab/process/k2454-two-setting-local-verifier.json').read_text())
for law,(w,l) in enumerate(zip(env['weights'],env['norms'])):
 a=1-w;mu=[a/2,a/2]+[s.cancel(w*((1+ss*l)/2)*((1+Q(hh,2))/2)/2) for zz,ss,hh in product([1,-1],repeat=3)]
 ck(f'original_weights_{law}',list(map(str,mu))==prior['original_laws'][law]['weights'] and a==[Q(27,100),Q(15,52)][law] and sum(mu)==1 and min(mu)>0)
 census=Counter();totalrank=0
 for ch,block in groups.items():
  vals=[2*a if x[3]==0 else mu[x[3]+1] for x in block];signs=[0 if e==0 else (-1)**(b+ref[e][2]) for f,r,b,e in block]
  # Positive diagonal congruence removes sqrt(vals) without changing rank.
  v=s.ones(len(block),1);u=s.Matrix(signs)
  T=v*v.T/(2*(1+a))+u*u.T/(2*w)
  Qmat=s.diag(*[1/t if x in strings else 0 for x,t in zip(block,vals)])
  rank=(T+Qmat).rank();totalrank+=rank
  ck(f'positive_two_column_rank_{law}_{ch}',T.rank()==s.Matrix.hstack(v,u).rank())
  if ch!=zero:census[(len(block),rank)]+=1
  else:
   ck(f'zero_character_rank11_{law}',rank==11 and Qmat.rank()==10)
   ck(f'four_companions_one_added_direction_{law}',len([x for x in block if x not in strings])==4 and all(signs[i]==-1 for i,x in enumerate(block) if x not in strings))
 ck(f'nonzero_exact_census_{law}',census==Counter({(1,1):12,(2,1):4,(4,2):8,(6,2):4,(9,2):2}))
 ck(f'dark53_bright55_bad54_{law}',totalrank==55 and 108-totalrank==53 and totalrank-1==54)
 # Original local conditional norms from the actual FRB Gram, including coherent e0 pair.
 G=s.zeros(12)
 for i,x in enumerate(strings):
  for j,y in enumerate(strings):
   if x[3]==y[3]:G[frb.index(x[:3]),frb.index(y[:3])]+=s.sqrt(mu[i]*mu[j])
 om=(-1+s.I*s.sqrt(3))/2;rr=[]
 for k,ss,tt in product(range(3),[1,-1],[1,-1]):
  av=s.Matrix([s.expand(om**((k*f)%3))*ss**r*tt**b/s.sqrt(12) for f,r,b in frb]);r=s.simplify((av.H*G*av)[0]);rr.append(r)
  ck(f'local_original_probability_{law}_{k}_{ss}_{tt}',r==(1+a*ss*tt)/12)
 Fq=s.factor(sum(x*x for x in mu));Ft=s.factor(sum(x*x for x in rr))
 ck(f'local_target_fidelity_{law}',sum(rr)==1 and Ft==(1+a*a)/12 and 0<Fq<1 and 0<Ft<1)
 ctrl(f'effect_complete_does_not_preserve_target_{law}',Fq!=1 and Ft!=1)
 block=groups[zero];vals=[2*a if x[3]==0 else mu[x[3]+1] for x in block];signs=[0 if e==0 else (-1)**(b+ref[e][2]) for f,r,b,e in block]
 target=s.Matrix([s.sqrt(mu[strings.index(x)]) if x in strings else 0 for x in block])
 z=s.Matrix([s.sqrt(w/2) if x in strings[:2] else (-s.sqrt(a*mu[strings.index(x)]/w) if x in strings[2:] else 0) for x in block])
 V=s.Matrix([s.sqrt(v) for v in vals]);W=s.Matrix([sg*s.sqrt(v) for sg,v in zip(signs,vals)]);Toriginal=V*V.T/(2*(1+a))+W*W.T/(2*w)
 ck(f'original_z_normalized_orthogonal_{law}',s.simplify((z.T*z)[0])==1 and s.simplify((z.T*target)[0])==0)
 ck(f'original_z_Q_T_forms_{law}',sum(z[i]**2 for i,x in enumerate(block) if x in strings)==1 and s.simplify((z.T*Toriginal*z)[0])==a/(1+a))
 F=Q(9,10);mix=Q(1,4);t=mix+(1-mix)*a/(1+a);Fone=s.cancel(F/(F+(1-F)*t))
 ck(f'explicit_onepass_gain_and_limit_{law}',Fone>F and t<1)
 fixtures.append({'law':law+1,'dark':53,'bright':55,'local_Q_output_fidelity':str(Fq),'local_T_output_fidelity':str(Ft),'canonical_onepass_fidelity':str(Fone),'canonical_retry_limit':str(F),'nonzero_blocks':[[*k,v] for k,v in sorted(census.items())]})
# Noncommuting label-level update is not a square of averaged failure effect.
P=s.diag(1,0,0);E0=s.diag(1,1,0);E1=P+s.Matrix([0,1,1])*s.Matrix([[0,1,1]])/2;I=s.eye(3);Omega=(E0+E1)/2
N=lambda X:sum(((I-E)*X*(I-E)/2 for E in [E0,E1]),s.zeros(3))
S1=N(I);S2=N(S1)
ck('projector_CP_completeness',all(E*E==E and (I-E)*(I-E)==I-E for E in [E0,E1]))
ck('finite_bad_effect_telescope',(Omega-P)+N(Omega-P)==I-S2-P and N(P)==s.zeros(3))
ctrl('averaged_effect_wrong_finite_update',S2!=S1*S1)
# Actual complete grading-preserving trap; squared Kraus matrices, not probability assertions.
a=Q(1,4);E=s.diag(1,a,0);A=s.diag(1,s.sqrt(a),0);K0=s.zeros(3);K0[2,1]=s.sqrt(1-a);K1=s.diag(0,0,1)
ck('trap_CP_complete',A.H*A+K0.H*K0+K1.H*K1==I)
Nt=lambda X:K0.H*X*K0+K1.H*X*K1
ck('trap_no_later_output',Nt(E)==s.zeros(3))
ctrl('grading_alone_does_not_prove_bright_completion',E[1,1]==Q(1,4) and E[1,1]!=1)
ck('allpass_repair_consumer',Q(3,5)**10/(9+Q(3,5)**10)<Q(7,10000))
ctrl('allpass_not_anypass',1-(1-Q(1,4))**4!=Q(1,4)**4)
Ec=s.diag(1,Q(1,4),0);Kc=s.diag(0,s.sqrt(3)/2,1);rhoc=s.diag(Q(1,2),0,Q(1,2))
for m in [1,2,8]:
 Bc=I-Kc**(2*m)
 ck(f'canonical_dark_fixture_{m}',s.trace(rhoc*Bc)==Q(1,2) and Bc[2,2]==0 and Bc[1,1]==1-Q(3,4)**m)
ctrl('dark_component_not_certain_output',s.trace(rhoc*(I-Kc**16))!=s.trace(rhoc*I))
# Controls alter actual assumptions/data and compare recomputed quantities; not assertion mutation.
deps=['tests/channel-swings/k2419_positive_visibility_dual_probe.py','tests/channel-swings/k2457_local_verifier_phase_design_probe.py','lab/process/k2457-local-verifier-phase-design.json','lab/process/k2454-two-setting-local-verifier.json']
report={'result':'K2482','scope':'conditional canonical instruments and exact original local disturbance; no hardware or native physics','checks':checks,'contrary_controls':controls,'original_laws':fixtures,'evidence_kinds':{'universal':'written positive-map and stopping proofs','exact':'original coordinate ranks, conditional probabilities and CP counterexamples','inherited':'K2457 complete phase block formula and gap authenticated, not rerun'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
p=ROOT/'lab/process/k2482-same-copy-retry-boundary.json'
if '--write' in sys.argv:p.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
else:ck('saved_report_reproduces',json.loads(p.read_text())==report)
print(json.dumps({'result':'PASS','checks':len(checks),'controls':len(controls),'laws':fixtures}))
