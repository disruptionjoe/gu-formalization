"""Original mixed tensors and adjoint; no finite rank extrapolation."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict,Counter
from itertools import combinations,combinations_with_replacement
from math import factorial,prod,comb
import ast,json,hashlib,sys
ROOT=Path(__file__).resolve().parents[2]
p37=ROOT/'tests/channel-swings/k2437_augmented_compatibility_adjoint_probe.py';t37=p37.read_text()
exec(compile(t37[:t37.index('for deg in range(8):')],str(p37),'exec'),globals())
inherited=dict(checks);checks={};controls={}
for node in ast.parse(t37).body:
 if isinstance(node,ast.FunctionDef) and node.name in {'coeff','jp','ja'}:exec(compile(ast.Module(body=[node],type_ignores=[]),str(p37),'exec'),globals())
ck('bank1239',len(rep)==161 and len(linear)==112 and 7*len(rep)+len(linear)==1239)
ck('original_witness',all(inherited.values()))
def ambient(hh):
 aa=[jlinear(hh,covs[r]) for r in range(14)];bb={}
 for r in range(14):
  for ss in range(14):
   for t in range(7):
    v=-sum(F(eta[i]*eta[j],2)*av*bv*fp(KE[t],hh,i,j) for i,av in covs[r].items() for j,bv in covs[ss].items())
    if v:bb[r,ss,t]=ff(v)
 return aa,bb
def dout(hh,P):
 out={}
 for r in range(14):
  for ij,v in symbol(hh,covs[r]).items():out[ij]=pa((1,out.get(ij,{})),(ff(v),der(P,r)))
 return {k:v for k,v in out.items() if v}
def adj(hh,Q,p,d,co):return pa(*[(ff(v),mulvar(Q.get(ij,{}),r)) for r in range(14) for ij,v in symbol(hh,covs[r]).items()],(field(4)/d,ja(p,co)))
def epair(A,B):return sum(fisher(v,B.get(k,{})) for k,v in A.items())
def norm(P,d):return fisher(P,P)/factorial(d)
miss_w=miss_order=False
nonzero_pairings=0
for j,hh in enumerate([rep[0],rep[32],rep[55],h]):
 co=ambient(hh)
 for m in [(0,1,7,8),(1,2,2,7),(0,7,7,8),(2,2,8,9)]:
  P={m:field(1)};D=dout(hh,P);p=jp(P,co);Q=D;U=adj(hh,Q,p,4,co)
  nonzero_pairings+=bool(D or p)
  ck(f'duality_{j}_{m}',epair(D,Q)+fisher(p,p)==fisher(P,U))
  ck(f'boundary_duality_{j}_{m}',fisher(P,U)==fisher({m[1:]:field(1)},der(U,m[0])))
  restricted=([co[0][r] if r<7 else 0 for r in range(14)],{k:v for k,v in co[1].items() if k[0]<7 and k[1]<7})
  miss_w |= jp(P,co)!=jp(P,restricted);miss_order |= ja(p,co)!=ja(p,co,True)
ck('nonvacuous_pairing_coverage',nonzero_pairings>=12)
ctrl('omitted_W_detected',miss_w);ctrl('reversed_scalar_adjoint_detected',miss_order)
co=ambient(h);P={(1,1,2):field(1)};p=jp(P,co);assert p
ck('actual4_over_d',field(4)/3*fisher(p,p)==fisher(P,adj(h,{},p,3,co)))
ctrl('omitted4_over_d_detected',fisher(p,p)!=fisher(P,adj(h,{},p,3,co)))
outer=False
for j in [0,20,21,55,111]:
 tag,bank=linear[j];f={(0,7):field(2),(1,8):field(-1)};D={};p={};cos={}
 for t,hh in bank.items():
  cos[t]=ambient(hh);pp=mulvar(f,t)
  for ij,q in dout(hh,pp).items():D[ij]=pa((1,D.get(ij,{})),(1,q))
  p=pa((1,p),(1,jp(pp,cos[t])))
 Q=D;V=pa(*[(1,der(adj(hh,Q,p,3,cos[t]),t)) for t,hh in bank.items()])
 ck('linear_duality_'+str(j),epair(D,Q)+field(4)/3*fisher(p,p)==fisher(f,V))
 wrong=pa(*[(1,adj(hh,{ij:der(q,t) for ij,q in Q.items()},der(p,t),3,cos[t])) for t,hh in bank.items()]);outer |= wrong!=V
ctrl('outer_derivative_required',outer)
found=None
for ij in combinations([1,3,10,11,12,13],2):
 if any(symbol(hh,covs[r]).get(ij,0) for hh in rep for r in range(7)):continue
 hits=[(j,r) for j,hh in enumerate(rep) for r in range(7,14) if symbol(hh,covs[r]).get(ij,0)]
 if not hits:continue
 Q={ij:{(7,7):field(1)}};Us=[adj(hh,Q,{},3,([],{})) for hh in rep]
 if not all(not der(U,i) for U in Us for i in range(7)):continue
 detect=[]
 for j,(tag,bank) in enumerate(linear):
  V=pa(*[(1,der(adj(hh,Q,{},3,([],{})),t)) for t,hh in bank.items()])
  if V:detect.append(j)
 if detect:found={'ij':list(ij),'constant_W_hit':list(hits[0]),'linear_detection':detect[0]};break
ctrl('unprojected_boundary_is_wrong',found is not None);ck('rotation_restores_test',found is not None and linear[found['linear_detection']][0][0]=='rotation')
for d in [1,2,3,5,8]:
 P={tuple([0]*d):field(2),tuple([7]*d):field(3)}
 if d>1:P[tuple([1]+[8]*(d-1))]=root2
 proj={m:v for m,v in P.items() if any(i<7 for i in m)}
 ds=sum(norm(der(P,i),d-1) for i in range(7));ex=d*sum(sum(i<7 for i in m)*v*v*prod(factorial(a) for a in Counter(m).values())/factorial(d) for m,v in P.items())
 ck('norm_identity_'+str(d),ds==ex);ck('norm_bounds_'+str(d),d*norm(proj,d)<=ds<=d*d*norm(proj,d))
 inv={m:v/sum(i<7 for i in m) for m,v in proj.items()};pieces=[der(inv,i) for i in range(7)]
 ck('ideal_synthesis_'+str(d),pa(*[(1,mulvar(pp,i)) for i,pp in enumerate(pieces)])==proj)
 total=sum(norm(pp,d-1) for pp in pieces);ck('synthesis_norm_'+str(d),norm(proj,d)<=total<=d*norm(proj,d))
def pm(P,Q):return pa(*[(v*w,{tuple(sorted(m+n)):field(1)}) for m,v in P.items() for n,w in Q.items()])
xis=[{(r,):ff(covs[r].get(i,0)) for r in range(14) if covs[r].get(i,0)} for i in range(14)]
bfull={(i,j):pa(((1 if i==j else 2)*eta[i]*eta[j],pm(xis[i],xis[j]))) for i in range(14) for j in range(i,14)}
tau={(i,i):{(7,7):field(eta[i])} for i in range(14)}
for j,hh in enumerate([rep[0],rep[32],rep[55],h]):
 ck('trace_adjoint_'+str(j),not adj(hh,tau,{},3,([],{})));ck('double_divergence_adjoint_'+str(j),not adj(hh,bfull,{},3,([],{})))
# Comparator: (1-x d_z)^(-1) z^n has x^n coefficient n!, though homogeneous kernels vanish.
for n0 in [3,5,8]:
 V={tuple([0]*j+[7]*(n0-j)):field(factorial(n0))/factorial(n0-j) for j in range(n0+1)}
 ck('factorial_comparator_'+str(n0),pa((1,V),(-1,mulvar(der(V,7),0)))=={tuple([7]*n0):field(1)} and V[tuple([0]*n0)]==factorial(n0))
ctrl('kernel_not_uniform_bound',factorial(8)>2**8)
deps=[str(Path(__file__).relative_to(ROOT)),'explorations/conditional-build/k2449-full-mixed-boundary-adjoint-2026-11-01.md','tests/channel-swings/k2437_augmented_compatibility_adjoint_probe.py','tests/channel-swings/k2425_frame_euler_module_probe.py','lab/process/k2437-augmented-compatibility-adjoint.json']
report={'result_id':'K2449','checks':checks,'controls':controls,'boundary_fixture':found,'evidence_kinds':{'universal':'written exact adjoint, descending kernel proof, norm identities and singular-value implication','finite_exact':'original tensor dualities and nonzero omission controls','ceiling':'no uniform quotient estimate or nonlinear convergence'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2449-full-mixed-boundary-adjoint.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2449',len(checks),'checks',len(controls),'controls PASS')
