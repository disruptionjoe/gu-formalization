"""Exact raw witnesses for curved conservative connections on the fixed core."""
from pathlib import Path
import argparse,hashlib,json
from sage.all import QQ,identity_matrix
from k1953_spin_connection_stable_mass import setup
from k1836_k77_differential_dirac_quotient import enc
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k1961-curved-core-connections.json'

def produce():
 g,As,J,L,C,H=setup();I=identity_matrix(QQ,128,sparse=True);I15=identity_matrix(QQ,15,sparse=True)
 rotations=[];checks=0
 for a,b in [(1,2),(2,3),(1,3)]:
  QJ=I15.tensor_product(g[a]*g[b])*J
  QJ[128*a:128*(a+1),:]+=2*J[128*b:128*(b+1),:]
  QJ[128*b:128*(b+1),:]-=2*J[128*a:128*(a+1),:]
  R=L*QJ
  assert QJ==J*R,'actual tensor action preserves raw core'
  assert R*R==-I and H*R+R.transpose()*H==0,'positive skew complex rotation'
  for A,c in zip(As,C):
   assert A*QJ==J*c*R and c*R==R*c,'observed derivative connection placement'
  rotations.append(R);checks+=8
 R,S,T=rotations
 assert R*S==T and S*R==-T and T*T==-I,'nonabelian quaternion relations';checks+=3
 # A1=R,A2=S: F12=[R,S]=2T, faithful curvature; zero-order V=-C1 R-C2 S.
 F=R*S-S*R;V=-C[0]*R-C[1]*S
 assert F.rank()==128 and F*F==-4*I,'nonzero full-rank curvature'
 assert H*V+V.transpose()*H==0,'conservative curved potential'
 assert any(V*c+c*V!=0 for c in C),'connection is not an anticommuting Dirac mass';checks+=3
 # Real rational Cayley rotations give a finite noncommuting loop witness.
 U=(3*I+4*R)/5;W=(3*I+4*S)/5
 assert U.transpose()*H*U==H and W.transpose()*H*W==H,'finite energy rotations'
 K=U*W*(3*I-4*R)/5*(3*I-4*S)/5
 assert K!=I and K.transpose()*H*K==H,'nontrivial Wilson commutator';checks+=2
 inputs=['lab/process/k1951-coordinated-zero-southeast-principal.json','lab/process/k1959-full-direction-even-connection.json']
 return dict(result_id='K1961',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',exact_controls=checks,labels=[[1,2],[2,3],[1,3]],rotations=[enc(x) for x in rotations],curvature_rank=128,wilson_commutator_trace=str(K.trace()),inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs},scope='Conditional fixed raw core; nonzero curvature is not source-selected interaction or a physical mass.')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();v=produce()
 if a.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
 else:assert v==json.loads(OUT.read_text()),'report mismatch'
 print('PASS K1961',v['exact_controls'],'exact controls',flush=True)
