"""Separate signed-bit reconstruction; actual coefficient fault checks."""
from pathlib import Path
import json,hashlib,copy
from sage.all import QQ,matrix,identity_matrix,zero_matrix,block_matrix
from k1959_full_direction_even_connection_probe import setup
from k1951_coordinated_zero_southeast_principal_probe import mat
ROOT=Path(__file__).resolve().parents[2]
v=json.loads((ROOT/'lab/process/k1961-curved-core-connections.json').read_text())
g,D,Di,J,L=setup();I=identity_matrix(QQ,128,sparse=True);I15=identity_matrix(QQ,15,sparse=True)
rows=json.loads((ROOT/'lab/process/k1951-coordinated-zero-southeast-principal.json').read_text())['blocks']
H=block_matrix([[mat(rows[i]['quotient_energy']) if i==j else zero_matrix(QQ,4,4) for j in range(32)] for i in range(32)],sparse=True)
As=[Di*D(k) for k in [7,8,9]];C=[L*A*J for A in As]
def check(fault=None):
 rotations=[]
 for ix,(a,b) in enumerate([(1,2),(2,3),(1,3)]):
  gen=g[a]*g[b]
  if fault=='reverse_generator' and ix==0:gen=g[b]*g[a]
  QJ=I15.tensor_product(gen)*J
  factor=1 if fault=='half_vector_action' and ix==0 else 2
  QJ[128*a:128*(a+1),:]+=factor*J[128*b:128*(b+1),:]
  QJ[128*b:128*(b+1),:]-=factor*J[128*a:128*(a+1),:]
  R=L*QJ
  assert QJ==J*R,'raw invariance'
  assert R==mat(v['rotations'][ix]),'independent actual generator'
  assert R*R==-I and H*R+R.transpose()*H==0,'rotation and energy'
  for A,c in zip(As,C):assert A*QJ==J*c*R and c*R==R*c,'raw spatial placement'
  rotations.append(R)
 R,S,T=rotations
 if fault=='commuting_replacement':S=R
 assert R*S==T and S*R==-T,'actual nonabelian bracket'
 V=-C[0]*R-C[1]*S
 if fault=='energy_symmetric_term':V+=I
 assert H*V+V.transpose()*H==0,'skew curved potential'
 assert V*V==-2*I+2*C[0]*C[1]*T,'curved homogeneous dispersion at zero momentum'
 assert V.rank()==64,'curvature does not imply a full gap'
 for c in C:assert c*c==I and H*c==c.transpose()*H,'speed one principal system'
 assert all(C[i]*C[j]+C[j]*C[i]==0 for i in range(3) for j in range(i+1,3)),'full characteristic sphere'
 U=(3*I+4*R)/5;W=(3*I+4*S)/5;K=U*W*(3*I-4*R)/5*(3*I-4*S)/5
 assert K!=I and str(K.trace())==v['wilson_commutator_trace'],'finite loop'
 return 30
print('PASS independent K1961',check(),'matrix identities')
for fault in ['reverse_generator','half_vector_action','commuting_replacement','energy_symmetric_term']:
 try:check(fault)
 except AssertionError as e:print('CAUGHT mathematical input',fault,str(e))
 else:raise AssertionError('undetected fault '+fault)
assert v['result_id']=='K1961'
for p,h in v['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'dependency pin'
print('PASS pins and report identity; no analytic domain theorem inferred from counts')
