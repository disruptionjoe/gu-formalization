"""Original full-carrier phase pinching, exact block bounds and design controls."""
from pathlib import Path
from itertools import product
from collections import defaultdict
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
ref={e:(f,r,b) for f,r,b,e in strings};ref[0]=(0,0,0)
coords=list(product(range(3),range(2),range(2),range(9)));frb=list(product(range(3),range(2),range(2)));groups=defaultdict(list)
def character(x):
 f,r,b,e=x;fe,re,be=ref[e];return tuple(int(f==j)-int(fe==j) for j in range(3))+(r-b-re+be,)
for x in coords:groups[character(x)].append(x)
zero=(0,0,0,0)
ck('full_dimension',len(coords)==108 and sum(map(len,groups.values()))==108)
ck('character_blocks',len(groups)==31 and len(groups[zero])==14)
ck('no_modular_aliases',len({tuple(z%3 for z in c[:3])+(c[3]%5,) for c in groups})==31)
ck('target_fixed',all(character(x)==zero for x in strings))
ctrl('support_is_not_zero_character',len(groups[zero])>len(strings))
om=(-1+s.I*s.sqrt(3))/2
phase=lambda k,f:s.expand(om**((k*f)%3))
outcomes=list(product(range(3),[1,-1],[1,-1]));Abank=[s.Matrix([phase(k,f)*ss**r*tt**b/s.sqrt(12) for f,r,b in frb]) for k,ss,tt in outcomes]
ck('full_local_basis_orthonormal',simp(s.Matrix.hstack(*Abank).H*s.Matrix.hstack(*Abank))==s.eye(12))
fixtures=[]
for law,(mean,w,l) in enumerate(zip(means,weights,norms)):
 a=1-w;mu=[a/2,a/2]
 for zz,ss,hh in product([1,-1],repeat=3):mu.append(s.cancel(w*((1+ss*l)/2)*((1+Q(hh,2))/2)/2))
 prior=json.loads((ROOT/'lab/process/k2454-two-setting-local-verifier.json').read_text())['original_laws'][law]
 ck(f'original_weights_{law}',list(map(str,mu))==prior['weights'] and a==[Q(27,100),Q(15,52)][law])
 W=s.zeros(12,9)
 for j,(f,r,b,e) in enumerate(strings):W[frb.index((f,r,b)),e]+=s.sqrt(mu[j])
 # Independent original conditional vectors for all local outcomes.
 cas=[simp(W.T*av.conjugate()) for av in Abank]
 for j,((k,ss,tt),ca) in enumerate(zip(outcomes,cas)):
  ck(f'original_conditional_norm_{law}_{j}',s.simplify((ca.H*ca)[0])==(1+a*ss*tt)/12)
 # Direct full tensor columns restricted to each character must be collinear
 # with the proposed V/W, with the correct phase and normalized magnitude.
 blockrows=[]
 for gi,(char,block) in enumerate(sorted(groups.items())):
  vals=[2*a if x[3]==0 else mu[x[3]+1] for x in block]
  signs=[0 if e==0 else (-1)**(b+ref[e][2]) for f,r,b,e in block]
  V=s.Matrix([s.sqrt(t) for t in vals]);WV=s.Matrix([sg*s.sqrt(t) for sg,t in zip(signs,vals)])
  for j,((k,ss,tt),av,ca) in enumerate(zip(outcomes,Abank,cas)):
   target=V if ss*tt==1 else WV
   raw=s.Matrix([s.expand(av[frb.index((f,r,b))]*ca[e]) for f,r,b,e in block])
   nz=next((i for i,v in enumerate(target) if v!=0),None)
   if nz is None:ok=all(s.simplify(z)==0 for z in raw)
   else:
    ratio=s.simplify(raw[nz]/target[nz]);ok=all(s.simplify(raw[i]-ratio*target[i])==0 for i in range(len(block))) and s.simplify(ratio*s.conjugate(ratio))==Q(1,144)
   ck(f'full_original_block_column_{law}_{gi}_{j}',ok)
  av=sum(vals);bv=sum(t for t,sg in zip(vals,signs) if sg);cv=sum(t*sg for t,sg in zip(vals,signs));trace=s.cancel(av/(2*(1+a))+bv/(2*w));det=s.cancel((av*bv-cv*cv)/(4*w*(1+a)))
  if char!=zero:
   slack=s.cancel(Q(16,25)-Q(4,5)*trace+det)
   ck(f'nonzero_block_spectral_bound_{law}_{gi}',trace<=Q(8,5) and slack>=0)
   blockrows.append({'character':list(char),'dimension':len(block),'trace':str(trace),'det':str(det),'slack':str(slack)})
  else:
   # Exact target and orthogonal complement matrix test through rational congruence.
   # Divide rows/columns by sqrt(vals), retaining all four companion coordinates.
   Pco=s.Matrix([Q(1,2) if x in strings[:2] else (1 if x in strings[2:] else 0) for x in block])
   qq=s.diag(*[Q(1,1)/t if x in strings else 0 for x,t in zip(block,vals)])
   matrix=s.ones(len(block))/(2*(1+a))+s.Matrix(signs)*s.Matrix(signs).T/(2*w)
   O=qq/4+3*matrix/4
   target=s.Matrix([Pco[i]*vals[i] for i in range(len(block))])
   ck(f'full_target_eigenvector_{law}',O*target==Pco)
   slack=Q(3,5)*s.diag(*[1/t for t in vals])+Q(2,5)*Pco*Pco.T-O
   # Exact LDL-style semidefinite elimination with zero-row pivot handling.
   def rational_psd(M):
    M=s.Matrix(M)
    while M.rows:
     if any(M[i,i]<0 for i in range(M.rows)):return False
     if any(M[i,i]==0 and any(M[i,j]!=0 for j in range(M.cols)) for i in range(M.rows)):return False
     nz=next((i for i in range(M.rows) if M[i,i]>0),None)
     if nz is None:return True
     ix=[i for i in range(M.rows) if i!=nz];v=M.extract(ix,[nz]);M=M.extract(ix,ix)-v*v.T/M[nz,nz]
    return True
   ck(f'full_zero_character_PSD_{law}',rational_psd(slack))
   ctrl(f'half_gap_fails_actual_zero_block_{law}',not rational_psd(Q(1,2)*s.diag(*[1/t for t in vals])+Q(1,2)*Pco*Pco.T-O))
  # All coordinates and exact weights, not a fitted abstract projection.
 maxtrace=max(s.Rational(r['trace']) for r in blockrows);minslack=min(s.Rational(r['slack']) for r in blockrows)
 ck(f'nonzero_block_extrema_{law}',(maxtrace,minslack)==[(Q(3927,3302),Q(1371,41275)),(Q(761,670),Q(33,670))][law])
 ck(f'equal_bad_parity_mass_{law}',sum(mu[j] for j,x in enumerate(strings) if j>=2 and x[1]==x[2])==w/2)
 p=s.symbols('p',real=True);B=s.Matrix([[p+(1-p)*a/(1+a),(1-p)*s.sqrt(a/2)/(1+a)],[(1-p)*s.sqrt(a/2)/(1+a),(1-p)/(2*(1+a))]])
 ck(f'universal_half_gap_determinant_{law}',s.factor((s.eye(2)/2-B).det()-(p-2*p*p-a)/(4*(1+a)))==0)
 ctrl(f'no_diagonal_twirl_half_gap_{law}',a>Q(1,8))
 x=s.symbols('x');rtheta=a*(1-a*x)/(1-a*a*x)
 ck(f'phase_derivative_{law}',s.factor(s.diff(rtheta,x)+a*a*(1-a)/(1-a*a*x)**2)==0)
 ck(f'phase_minimum_{law}',s.cancel(rtheta.subs(x,1))==a/(1+a))
 ctrl(f'quadrature_phase_worse_{law}',rtheta.subs(x,0)>rtheta.subs(x,1))
 # Independently reconstruct compressed Q T_theta Q from equatorial basis,
 # using rational unit phases to avoid numerical spectral inference.
 for ctheta,stheta in [(Q(1),Q(0)),(Q(0),Q(1)),(Q(3,5),Q(4,5))]:
  zphase=ctheta+s.I*stheta;trace=0
  for parity in (1,-1):
   den=1+a*parity*ctheta
   # Sum of actual ten support coordinate squared amplitudes for six columns.
   trace+=Q(1,2)*(a*(2+2*parity*ctheta)+w)/den
  ck(f'phase_trace_formula_{law}_{ctheta}',s.cancel(trace-1-rtheta.subs(x,ctheta**2))==0)
 # Omitting E compensation while applying F phase changes the target overlap.
 badF=om;overlap=a+w*badF
 ctrl(f'omitted_E_compensation_changes_target_{law}',s.simplify(overlap*s.conjugate(overlap))<1)
 fixtures.append({'law':law+1,'a':str(a),'blocks':blockrows,'max_nonzero_trace':str(maxtrace),'min_nonzero_slack':str(minslack),'certified_gap':'2/5'})
# Same prospective consumer for both originals, using the common certified gap.
nu=arb(2)/5;alpha=arb(20).log();kap=arb('1e-6');beta=arb('1e-8');delta=arb('1e-8');tau=arb('.01')
c=(2-delta).log()/(1-delta);D=nu*((tau-4*kap)/2)**2-delta-beta
N=int((alpha/(c*D)).upper().ceil().unique_fmpz())
def bound50(n):return 2*((delta+beta+alpha/(c*n))/nu).sqrt()+4*kap
ck('K2450_consumer',bound50(N)<=tau)
ctrl('K2450_previous_count',bound50(N-1)>tau)
ck('K2450_positive_actual_success',((delta+beta+alpha/(c*N))/nu).sqrt()/2+kap<arb(1)/4)
B=arb('1e-6');A=((B.exp()-1)*2).sqrt()/2;H=(B+2*alpha)/arb(2).log();D6=nu*((tau-4*kap)/2)**2-beta
N6=int((((A+(A*A+4*D6*H).sqrt())/(2*D6))**2).upper().ceil().unique_fmpz())
def bound56(n):return 2*((A/arb(n).sqrt()+H/n+beta)/nu).sqrt()+4*kap
ck('K2456_consumer',bound56(N6)<=tau)
ctrl('K2456_previous_count',bound56(N6-1)>tau)
ck('K2456_positive_actual_success',((A/arb(N6).sqrt()+H/N6+beta)/nu).sqrt()/2+kap<arb(1)/4)
deps=[str(Path(__file__).relative_to(ROOT)),'explorations/conditional-build/k2457-local-verifier-phase-design-2026-11-01.md','tests/channel-swings/k2439_minimal_flagged_tomography_probe.py','tests/channel-swings/k2419_positive_visibility_dual_probe.py','lab/process/k2454-two-setting-local-verifier.json','explorations/conditional-build/k2456-predictable-leakage-budget-2026-11-01.md','explorations/conditional-build/k2450-route-leakage-certificate-2026-11-01.md']
report={'result_id':'K2457','checks':checks,'controls':controls,'original_laws':fixtures,'prospective':{'K2450_actual_uses':N,'K2456_actual_uses':N6,'K2450_allowance':str(bound50(N)),'K2456_allowance':str(bound56(N6))},'evidence_kinds':{'universal':'written finite character pinching, fixed-basis optimum and invariant companion obstruction','exact_original':'all108 coordinates;372 original columns per law; all31 blocks and rational full-zero-block PSD','prospective':'Arb256 hypothetical actual-use counts; no hardware data'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2457-local-verifier-phase-design.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2457',len(checks),'checks',len(controls),'controls PASS',report['prospective'])
