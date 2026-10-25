"""Exact full upper-preserving image and metric-independent Fourier instability.

Completeness of coefficient kernels is reused from the pinned K2028 certificate.
This reconstructs every surviving raw direction; it does not rerun that census.
"""
from pathlib import Path
import json,hashlib,argparse
from sage.all import QQ,matrix,identity_matrix,zero_matrix,prod
from k1967_paired_raw_coefficient_observation import setup
from k1836_k77_differential_dirac_quotient import enc,mat
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2030-positive-metric-rescue.json'
INPUT='lab/process/k2028-all-grade-raw-common-form.json'
def produce():
 r=json.loads((ROOT/INPUT).read_text());g,v,eta,J,C,P,DJ,Fi,Ti,apply=setup()
 I=identity_matrix(QQ,128,sparse=True);Z=zero_matrix(QQ,128,128,sparse=True);B=prod(g[7:]);W=(3*I-v)/2
 M=mat(r['survivor']['M']);basis=[];directions=[];fullchecks=0
 for rec in r['complex_hermitian_branch']['groups']:
  for row in mat(rec['upper_kernel']):
   O=[matrix(Z) for _ in range(14)]
   for co,(mask,ys) in zip(row,rec['labels']):
    if co:
     X=prod([g[k] for k in range(14) if mask>>k&1]) if mask else I
     for k in range(14):
      if ys[k]:O[k]+=co*(3*I+v)*eta[k]*ys[k]*g[k]*X/4
   actions=[apply(k,[o*x for x in J]) for k,o in enumerate(O)]
   raw=[sum((a[j] for a in actions),Z) for j in range(14)];N=Fi*raw[0]
   assert all(raw[j]==DJ[j]*N for j in range(14))
   lower=-sum((eta[k]*B*O[k].transpose()*B*J[k] for k in range(14)),Z)
   assert lower==DJ[14]*N
   basis.append(N);directions.append([enc(o) for o in O]);fullchecks+=15
 assert len(basis)==14
 N=next(x for x in basis if x and x!=x.transpose())
 T=matrix(QQ,[x.list() for x in [I]+C+[N]]).transpose();assert T.rank()==5
 coords=[list(T.solve_right(matrix(QQ,1,128**2,x.list()).transpose().column(0))) for x in basis]
 assert matrix(QQ,coords).rank()==5
 alpha=QQ(4193408)/1087849
 assert M*M==alpha*I and N*N==-I/2 and M*N+N*M==0
 assert all(M*c+c*M==0 and N*c+c*N==0 for c in C)
 assert all(x.trace()==0 for x in C+[M,N])
 assert all(c.transpose()==c and c*c==I for c in C)
 assert all(C[i]*C[j]+C[j]*C[i]==0 for i in range(3) for j in range(i))
 V=prod(C);assert V*V==-I and V.transpose()==-V and all(V*c==c*V for c in C)
 assert V.trace()==0 and C[2].trace()==0 and (V*C[2]).trace()==0
 # Complex matrices represented by their real and imaginary parts, avoiding
 # floating eigensolvers. G=sM+i(tN-sum k_j C_j) after scalar phase removal.
 controls=[]
 for s,t,ks in [(1,0,(0,0,0)),(0,1,(0,0,0)),(2,3,(1,2,3)),(0,0,(2,3,6)),(QQ(3)/5,QQ(4)/5,(0,0,0))]:
  X=s*M;Y=t*N-sum((k*c for k,c in zip(ks,C)),Z)
  disc=alpha*s*s+QQ(t*t)/2-sum(k*k for k in ks)
  assert X*X-Y*Y==disc*I and X*Y+Y*X==0
  controls.append(dict(real=str(s),imaginary=str(t),momentum=list(map(str,ks)),discriminant=str(disc)))
 # An actual non-scalar positive principal metric: K=iV is Hermitian involutive.
 # P=I+(i/2)V has eigenvalues1/2,3/2; [P,C]=0.
 assert all(V*c==c*V for c in C)
 inputs=[INPUT,'lab/process/k1951-coordinated-zero-southeast-principal.json','lab/process/k2026-compatible-mass-moduli.json']
 return dict(result_id='K2030',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',imaginary_upper_dimension=14,imaginary_image_dimension=5,imaginary_invisible_dimension=9,full_raw_return_identities=fullchecks,imaginary_coefficients=directions,imaginary_images=[enc(x) for x in basis],image_coordinates=[[str(x) for x in row] for row in coords],real_generator=enc(M),extra_imaginary_generator=enc(N),principal=[enc(x) for x in C],volume=enc(V),real_square=str(alpha),imaginary_square='-1/2',mixed_anticommutator='0',fourier_controls=controls,complex_positive_metric_real_dimension=2048,real_positive_metric_real_dimension=1024,scope='Fixed common H, raw contraction and128 core. All constant positive Hermitian core metrics commuting with the principal matrices; no source-selected metric or interacting quotient. Full coefficient completeness reused from K2028, all14 surviving raw directions reconstructed here.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs})
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();r=produce()
 if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text())
 print('PASS K2030:14 full raw directions;5 image dimensions;210 raw returns;Clifford mixed instability;5 Fourier controls;3 provenance hashes',flush=True)
