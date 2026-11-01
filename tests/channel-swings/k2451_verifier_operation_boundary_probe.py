"""Original purified instruments, fully local edge tests and rational gap bounds."""
from pathlib import Path
from itertools import product
from fractions import Fraction as F
import sympy as s
from flint import arb,ctx
import ast,json,hashlib,sys
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
edges=[(0,1),(0,2)]+[(2,j) for j in range(3,10)]
def cut(edge):
 graph={i:[] for i in range(10)}
 for x,y in edges:
  if (x,y)==edge:continue
  graph[x].append(y);graph[y].append(x)
 seen={edge[0]};todo=list(seen)
 while todo:
  for z in graph[todo.pop()]:
   if z not in seen:seen.add(z);todo.append(z)
 return seen
ck('tree_connected_and9edges',len(edges)==9 and all(0<len(cut(e))<10 for e in edges))
# Reconstruct actual local measurement effect in the whole edge cube, not only asserted pair block.
def edge_effect(i,j,mu):
 aa,bb=strings[i],strings[j];diff=[k for k in range(4) if aa[k]!=bb[k]];last=3 if 3 in diff else 2;others=[k for k in diff if k!=last]
 cube=list(product(*[[aa[k]] if aa[k]==bb[k] else [aa[k],bb[k]] for k in range(4)]));dim=len(cube);E=s.zeros(dim)
 for signs in product([1,-1],repeat=len(others)):
  parity=1
  for sg in signs:parity*=sg
  v=s.zeros(dim,1)
  for index,point in enumerate(cube):
   a=1
   for k,sg in zip(others,signs):a*= (1 if point[k]==aa[k] else sg)/s.sqrt(2)
   a*=s.sqrt(mu[i]) if point[last]==aa[last] else parity*s.sqrt(mu[j])
   v[index]=a/s.sqrt(mu[i]+mu[j])
  E+=v*v.H
 return cube,simp(E)
fixtures=[]
for law,(mean,w,l) in enumerate(zip(means,weights,norms)):
 axis=mean/l;vp=s.Matrix([s.sqrt((1+axis[1])/2),axis[0]/s.sqrt(2*(1+axis[1]))]);vm=s.Matrix([-vp[1],vp[0]]);eig={1:vp,-1:vm};O=s.Matrix.hstack(vp,vm)
 ck('real_basis_'+str(law),simp(O.T*O)==I)
 ck('Bell_rotation_'+str(law),simp(s.kronecker_product(O.T,O.T)*phi)==phi)
 mu=[(1-w)/2,(1-w)/2];reduced=s.zeros(12)
 for a,(z,ss,hh) in enumerate(product([1,-1],repeat=3),start=1):
  lam=w*((1+ss*l)/2)*((1+Q(hh,2))/2)/2;mu.append(lam)
  K=s.sqrt(2*lam)*eig[hh*ss]*eig[z*ss].H
  vec=s.Matrix([K[b,r] for r,b in product(range(2),repeat=2)])/s.sqrt(2)
  native=simp(s.kronecker_product(O.T,O.T)*vec);f,rb,bb,env=strings[a+1]
  expected=s.zeros(4,1);expected[2*rb+bb]=s.sqrt(lam)
  ck(f'original_rotated_string_{law}_{a}',native==expected)
  reduced[4*f:4*f+4,4*f:4*f+4]+=vec*vec.H
 reduced[0:4,0:4]=(1-w)*Phi
 ck('actual_original_instrument_'+str(law),simp(reduced)==s.diag(*instrument(mean,w,l)))
 ck('weights_positive_'+str(law),all(x>0 for x in mu) and sum(mu)==1)
 gap_candidates=[]
 for edge in edges:
  i,j=edge;cube,E=edge_effect(i,j,mu);inds=[k for k,x in enumerate(strings) if x in cube]
  ck(f'cube_has_two_{law}_{edge}',inds==sorted([i,j]))
  v=s.zeros(len(cube),1);eta=s.zeros(len(cube),1);ix=cube.index(strings[i]);jx=cube.index(strings[j]);v[ix]=s.sqrt(mu[i]);v[jx]=s.sqrt(mu[j]);eta[ix]=s.sqrt(mu[j]);eta[jx]=-s.sqrt(mu[i])
  ck(f'edge_completeness_{law}_{edge}',simp(E*v)==v)
  ck(f'edge_rejection_{law}_{edge}',simp(E*eta)==s.zeros(len(cube),1))
  ck(f'edge_positive_projector_{law}_{edge}',simp(E*E)==E and E==E.H)
  # Exact expectation after wrong destructive readout, target coherence removed.
  wrong=s.simplify((mu[i]*E[ix,ix]+mu[j]*E[jx,jx])/(mu[i]+mu[j]))
  ctrl(f'destructive_filter_fails_{law}_{edge}',wrong<1)
  A=sum(mu[k] for k in cut(edge));conductance=mu[i]*mu[j]/(mu[i]+mu[j]);gap_candidates.append(s.cancel(conductance/(54*A*(1-A))))
  # Deleted edge yields a second zero-energy component vector.
  C=cut(edge);witness=[s.sqrt(mu[k]) if k in C else 0 for k in range(10)]
  ctrl(f'deleted_edge_degenerate_{law}_{edge}',all(s.simplify(s.sqrt(mu[y])*witness[x]-s.sqrt(mu[x])*witness[y])==0 for x,y in edges if (x,y)!=edge) and 0<A<1)
 gap=min(gap_candidates);expected=[Q(85,10071),Q(221,27783)][law]
 ck('exact_gap_bound_'+str(law),gap==expected and gap_candidates.index(gap)==1)
 cube,E=edge_effect(1,2,mu);v=s.Matrix([sum(s.sqrt(mu[k]) for k,x in enumerate(strings) if x==pt) for pt in cube]);defect=s.simplify((v.H*(s.eye(len(cube))-E)*v)[0])
 ctrl('third_support_cube_fails_'+str(law),len([x for x in strings if x in cube])==3 and defect>0)
 # Bell partial transpose negative witness for every original Fourier phase at good flag.
 pt=Q(1,2)*s.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])*(1-w);anti=s.Matrix([0,1,-1,0])/s.sqrt(2)
 ctrl('conditional_effect_not_separable_'+str(law),s.simplify((anti.H*pt*anti)[0])==-(1-w)/2<0)
 # Perfect flag/environment-block-diagonal effect necessarily preserves nonzero orthogonal components.
 ck('flag_components3_'+str(law),len({p[0] for p in strings})==3)
 ck('environment_components9_'+str(law),len({p[3] for p in strings})==9)
 # Same positive calibration assumptions, fair sampling comparison of alternative effects.
 def budget(nu):
  nu=arb(int(nu.p))/int(nu.q);delta=arb('1e-8');beta=arb('1e-8');kap=arb('1e-6');q=arb(1)/4;C=2;tau=arb('.01');c=(2-delta).log()/(1-delta);den=nu*((tau-kap/q)/C)**2-delta-beta;ck(f'positive_budget_{law}_{nu}',den>0);N=int((arb(20).log()/(c*den)).upper().ceil().unique_fmpz());allow=lambda n:C*((delta+beta+arb(20).log()/(c*n))/nu).sqrt()+kap/q
  ck(f'budget_ceiling_{law}_{nu}',allow(N)<=tau);ctrl(f'budget_predecessor_{law}_{nu}',allow(N-1)>tau)
  return N,str(allow(N))
 NN,allow=budget(gap);oldN,_=budget(Q(1,2));ctrl('local_sampling_cost_'+str(law),NN>oldN)
 fixtures.append({'law':law+1,'weights':list(map(str,mu)),'gap_lower_bound':str(gap),'local_actual_uses':NN,'original_two_setting_uses':oldN,'prospective_allowance':allow,'bad_cube_loss':str(defect)})
deps=[str(Path(__file__).relative_to(ROOT)),'explorations/conditional-build/k2451-verifier-operation-boundary-2026-11-01.md','tests/channel-swings/k2439_minimal_flagged_tomography_probe.py','tests/channel-swings/k2419_positive_visibility_dual_probe.py','lab/process/k2447-coherent-program-verification.json','explorations/conditional-build/k2450-route-leakage-certificate-2026-11-01.md']
report={'result_id':'K2451','checks':checks,'controls':controls,'original_laws':fixtures,'tree_edges':[list(e) for e in edges],'evidence_kinds':{'universal':'written local implementation, graph gap and separability/coherence boundaries','finite_exact':'original rotations/reduction, whole cube effects, contrary controls, rational cut bounds','prospective':'Arb256 budgets not measured performance'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2451-verifier-operation-boundary.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2451',len(checks),'checks',len(controls),'controls PASS')
