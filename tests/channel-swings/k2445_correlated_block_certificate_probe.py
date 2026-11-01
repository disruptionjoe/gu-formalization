from pathlib import Path
from itertools import product,combinations
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
src=ROOT/'tests/channel-swings/k2439_minimal_flagged_tomography_probe.py'
I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1);phi=s.Matrix([1,0,0,1])/s.sqrt(2);Phi=phi*phi.H
for node in ast.parse(src.read_text()).body:
 if isinstance(node,ast.FunctionDef) and node.name in {'simp','ptr','choi','psd','dist','law_data','instrument'}:exec(compile(ast.Module(body=[node],type_ignores=[]),str(src),'exec'),globals())

# Basis completeness, including genuinely classical flags.
for n in [2,3]:
 basis=[]
 for i in range(n):
  f=s.zeros(n);f[i,i]=1;basis.append(f)
 for i,j in combinations(range(n),2):
  f=s.zeros(n);f[i,j]=f[j,i]=1/s.sqrt(2);basis.append(f)
  f=s.zeros(n);f[i,j]=s.I/s.sqrt(2);f[j,i]=-s.I/s.sqrt(2);basis.append(f)
 S=s.zeros(n*n)
 for i,j in product(range(n),repeat=2):S[n*i+j,n*j+i]=1
 ck(f'basis_orthonormal_{n}',all(s.trace(f*g)==int(i==j) for i,f in enumerate(basis) for j,g in enumerate(basis)))
 ck(f'basis_swap_{n}',sum((s.kronecker_product(f,f) for f in basis),s.zeros(n*n))==S)
 ck(f'basis_square_{n}',sum((f*f for f in basis),s.zeros(n))==n*s.eye(n))
def reduced(rho,keep,n,m):
 rest=[i for i in range(m) if i not in keep];out=s.zeros(n**len(keep))
 for a,b in product(product(range(n),repeat=len(keep)),repeat=2):
  va=vb=0
  for x in a:va=va*n+x
  for x in b:vb=vb*n+x
  for tail in product(range(n),repeat=len(rest)):
   ia=[0]*m;ib=[0]*m
   for i,x,y in zip(keep,a,b):ia[i]=x;ib[i]=y
   for i,x in zip(rest,tail):ia[i]=ib[i]=x
   aa=bb=0
   for x,y in zip(ia,ib):aa=aa*n+x;bb=bb*n+y
   out[va,vb]+=rho[aa,bb]
 return simp(out)
swap=s.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
sing=s.Matrix([0,1,-1,0])/s.sqrt(2);v=s.kronecker_product(sing,sing);rho=v*v.H
bar=sum((reduced(rho,[i],2,4) for i in range(4)),s.zeros(2))/4
pair=sum((reduced(rho,[i,j],2,4) for i,j in product(range(4),repeat=2) if i!=j),s.zeros(4))/12
sig=s.diag(1,0);score=swap-s.kronecker_product(sig,I)-s.kronecker_product(I,sig)+s.eye(4)
h=s.trace(score*pair);loss=s.trace((bar-sig)**2)
ck('four_qubit_uniform_marginal',bar==I/2)
ck('four_qubit_swap_mean_zero',s.trace(swap*pair)==0)
ck('sharp_quantum_floor',h==0 and loss==Q(1,2)==Q(2,1)/3-Q(1,2)/3)
ctrl('zero_pair_score_not_zero_error',h==0 and loss>0)
ctrl('single_pair_not_uniform_pair',reduced(rho,[0,1],2,4)!=pair)
# Nonexchangeable complex product and entangled W-state fixtures.
chi=s.Matrix([Q(3,5),4*s.I/5]);w=s.Matrix([0,1,1,0,1,0,0,0])/s.sqrt(3)
for k,rr in enumerate([s.kronecker_product(chi*chi.H,s.diag(1,0),I/2),w*w.H]):
 m=3;bb=sum((reduced(rr,[i],2,m) for i in range(m)),s.zeros(2))/m;oo=sum((reduced(rr,[i,j],2,m) for i,j in product(range(m),repeat=2) if i!=j),s.zeros(4))/(m*(m-1));p=s.trace(bb*bb);sw=s.trace(swap*oo)
 ck(f'collective_variance_fixture_{k}',m*2+m*(m-1)*sw-m*m*p>=0)
 ck(f'stronger_loss_fixture_{k}',s.trace((bb-sig)**2)<=s.trace(score*oo)+(2-p)/(m-1))
# Original laws: balanced independent factors and positively correlated m-party affine lift.
means,weights,norms=law_data();H=s.diag(s.zeros(4),s.kronecker_product(Z,Y),s.zeros(4));original=[]
for k,args in enumerate(zip(means,weights,norms)):
 B=instrument(*args);sig12=s.diag(*B);mu=min(1-args[1],args[1]*(1-args[2])/16);t=Q(1,10**5);m=4
 ck(f'original_CP_TP_{k}',all(psd(b) for b in B) and sum((ptr(b) for b in B),s.zeros(2))==I/2)
 ck(f'original_balanced_both_signs_{k}',psd(B[1]+t*s.kronecker_product(Z,Y)) and psd(B[1]-t*s.kronecker_product(Z,Y)))
 ck(f'original_affine_mblock_positive_bound_{k}',m*t/mu<1)
 ck(f'original_tangent_tensor_constraints_{k}',s.trace(H)==0 and ptr(s.kronecker_product(Z,Y))==s.zeros(2) and s.trace(H*H)==4)
 signs=[1,1,-1,-1];hbal=sum(s.trace((sig12+i*t*H)*(sig12+j*t*H)) for a,i in enumerate(signs) for b,j in enumerate(signs) if a!=b)/(m*(m-1))-s.trace(sig12*sig12)
 ck(f'original_balanced_pair_score_{k}',s.simplify(hbal)==-4*t*t/(m-1))
 ctrl(f'original_labelled_vs_unlabelled_{k}',sum(signs)==0 and dist(t*H)==2*t>0)
 h_aff=s.trace(sig12*sig12)+2*t*s.trace(sig12*H)-2*s.trace(sig12*(sig12+t*H))+s.trace(sig12*sig12)
 ck(f'original_affine_score_and_loss_{k}',s.simplify(h_aff)==0 and s.trace((t*H)**2)==4*t*t)
 for sign in [-1,1]:
  eff=(s.eye(12)+sign*H)/2
  ck(f'index_consumer_valid_effect_{k}_{sign}',psd(eff) and psd(s.eye(12)-eff))
  ctrl(f'index_dependent_consumer_breaks_average_{k}_{sign}',s.trace(eff*(sign*t*H))==2*t>0)
 ck(f'original_correlated_zero_score_floor_{k}',4*t*t<=(12-Q(1,12))/(m-1))
 original.append({'law':k,'m':m,'positive_affine_factor':str(1-m*t/mu),'affine_score':'0','affine_true_loss':str(4*t*t),'balanced_score':str(hbal),'labelled_distance':str(2*t)})
# Explicit block-algebra basis identity, including original full12 carrier.
for sizes in [[2,2],[4,4,4]]:
 dim=sum(sizes);basis=[];offset=0
 for block in sizes:
  for i in range(block):
   f=s.SparseMatrix(dim,dim,{(offset+i,offset+i):1});basis.append(f)
  for i,j in combinations(range(block),2):
   basis.append(s.SparseMatrix(dim,dim,{(offset+i,offset+j):1/s.sqrt(2),(offset+j,offset+i):1/s.sqrt(2)}))
   basis.append(s.SparseMatrix(dim,dim,{(offset+i,offset+j):s.I/s.sqrt(2),(offset+j,offset+i):-s.I/s.sqrt(2)}))
  offset+=block
 cas=sum((f*f for f in basis),s.zeros(dim));want=s.diag(*[k for k in sizes for _ in range(k)])
 ck('flag_actual_Casimir_'+str(sizes),cas==want)
 ck('flag_basis_orthonormal_'+str(sizes),all(s.trace(f*g)==int(i==j) for i,f in enumerate(basis) for j,g in enumerate(basis)))
 labels=[z for z,k in enumerate(sizes) for _ in range(k)]
 target=s.SparseMatrix(dim*dim,dim*dim,{(dim*i+j,dim*j+i):1 for i,j in product(range(dim),repeat=2) if labels[i]==labels[j]})
 actual=sum((s.kronecker_product(f,f) for f in basis),s.SparseMatrix(dim*dim,dim*dim,{}))
 ck('flag_actual_compressed_swap_'+str(sizes),actual==target)
 ck('flag_bound_'+str(sizes),max(sizes)-Q(1,dim)<dim-Q(1,dim))
# Diagonal flag marginals alone do not prove joint dephasing invariance.
flagv=s.Matrix([0,1,1,0])/s.sqrt(2);flagrho=flagv*flagv.H;compressed=s.diag(1,0,0,1)
ck('coherent_flag_diagonal_marginal',reduced(flagrho,[0],2,2)==I/2)
ctrl('marginal_flags_do_not_license_compression',s.trace(swap*flagrho)==1 and s.trace(compressed*flagrho)==0)
# Negative h is essential in the martingale.
for pi,h in product([Q(1,4),Q(1,2),Q(3,4)],[-2,Q(-1,5),0,Q(3,7),2]):
 a=(1-pi)/pi;events=[(pi*(1+h/2)/2,2*a),(pi*(1-h/2)/2,-2*a),(1-pi,-h)]
 ck(f'negative_score_route_mean_{pi}_{h}',sum(p*z for p,z in events)==0)
 ck(f'route_variance_{pi}_{h}',sum(p*z*z for p,z in events)<=4*pi*a*a+4*(1-pi))
 ck(f'route_range_{pi}_{h}',all(abs(z)<=max(2*a,2) for p,z in events if p))
ctrl('loss_cannot_center_score_martingale',Q(1,2)*0-Q(1,2)*Q(1,2)!=0)
ctrl('revealed_route_invalid',Q(1,2)*0-Q(1,2)*1!=0)
n=10**12;m=10**8;L=(arb(2)*n*(n+1)/arb('.05')).log();rad=((8*n*L).sqrt()+4*L/3)/(n//2);full=arb(143)/(12*(m-1));flag=arb(47)/(12*(m-1));Qfull=rad+full;Qflag=rad+flag
errfull=(12*Qfull).sqrt();errflag=(12*Qflag).sqrt()
ck('prospective_budgets',0<errflag<errfull<arb('.04'))
ck('full_floor_one_percent_block_size',Q(143,1430000)==Q(1,10000))
ck('flag_floor_one_percent_block_size',Q(47,470000)==Q(1,10000))
evidence={'exact_original':original,'sharp_floor':'unrestricted four-qubit two-singlet state; not flagged causal sharpness','prospective':{'blocks':n,'members_per_block':m,'total_emitted':m*n,'N':12,'used_blocks_assumed':n//2,'alpha':'.05','statistical_radius':str(rad),'unrestricted_output_allowance':str(errfull),'classical_flag_output_allowance':str(errflag),'status':'zero empirical score and ideal operations; no measurements'},'universal':'written collective variance, block algebra refinement and hidden-route martingale','ceilings':'unlabelled mean marginal; no individual distances, final-transcript or joint-use certificate'}

deps=['tests/channel-swings/k2445_correlated_block_certificate_probe.py', 'explorations/conditional-build/k2445-correlated-block-certificate-2026-11-01.md', 'tests/channel-swings/k2439_minimal_flagged_tomography_probe.py', 'lab/process/k2442-replicated-process-distance.json', 'lab/process/k2444-sharp-heralded-transfer.json']
report={'result_id':'K2445','checks':checks,'controls':controls,'evidence':evidence,'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2445-correlated-block-certificate.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('k2445-correlated-block-certificate',len(checks),'checks',len(controls),'controls PASS')
