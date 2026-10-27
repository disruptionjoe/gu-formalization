from pathlib import Path
import json,argparse,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parents[2]

OUT='k2138-graph-holonomy-mass-transport.json'
DEPS=['explorations/conditional-build/k2132-conserving-positive-sector-classification-2026-10-27.md','explorations/conditional-build/k2135-full-graph-current-connection-2026-10-27.md']
EVIDENCE='Finite exact unitary-equivalent Clifford, curvature and span controls. Universal multiplicity8 holonomy and mass statements follow from the arbitrary-K written proof, not finite witness extrapolation.'
FAULTS=['wrong_pairing_coefficient','drop_adjoint','one_curvature_plane_only','drop_mass_average','average_curvature_only']
def compute(fault=None):
 I=s.I; eye=s.eye; z=s.zeros; kron=s.kronecker_product
 sx=s.Matrix([[0,1],[1,0]]);sy=s.Matrix([[0,-I],[I,0]]);sz=s.diag(1,-1)
 cs=[kron(sx,eye(2)),kron(sz,sx),kron(sz,sz)];M=-I*kron(sz,sy);W=I*cs[0]*cs[1]*cs[2]
 comm=lambda x,y:x*y-y*x
 q=8;n=2; lift=lambda A:kron(eye(4),A);WL=kron(W,eye(n));ML=kron(M,eye(n));a=s.Rational(9,280)
 coeff=2 if fault=='wrong_pairing_coefficient' else 3
 S=s.diag(*[a*(t*eye(q)+coeff*zz*WL) for t,zz in [(1,1),(1,-1),(-1,1),(-1,-1)]])
 Y=s.Matrix.vstack(eye(q),eye(q),z(q),z(q));h=Y.conjugate().T*S*Y;P=Y*h.inv()*Y.conjugate().T*S
 def curvature(slot,K):
  b1=eye(q);b2=lift(K/2);d1=s.Matrix.vstack(*[b1 if j==slot else z(q) for j in range(4)]);d2=s.Matrix.vstack(*[b2 if j==slot else z(q) for j in range(4)])
  adj=lambda A:A.T if fault=='drop_adjoint' else A.conjugate().T
  return h.inv()*(adj(d1)*S*(eye(4*q)-P)*d2-adj(d2)*S*(eye(4*q)-P)*d1)
 Ks=[I*eye(2),I*sz,I*sx,I*sy];FsB=[curvature(2,K) for K in Ks];FsC=[curvature(3,K) for K in Ks]
 expectedB=lambda K:kron((-eye(4)+3*W)/2,K)
 expectedC=lambda K:kron((-eye(4)-3*W)/2,K)
 bank=[FsB[0],FsC[0]]
 if fault=='one_curvature_plane_only':bank=[FsB[0],FsB[0]]
 def coefficient(F,w):
  spin=s.Matrix(4,4,lambda i,j:F[i*n,j*n]/I)
  Pw=(eye(4)+w*W)/2
  return s.simplify(s.trace(Pw*spin)/s.trace(Pw))
 coefficient_span=s.Matrix([[coefficient(F,w) for F in bank] for w in [1,-1]])
 tau=lambda A:ML.inv()*A*ML
 averaged=[(F+tau(F))/2 for F in FsB]
 K=I*sz;theta=kron(eye(4),K);G=kron((eye(4)-3*W)/2,K);Gm=(G+tau(G))/2
 if fault=='drop_mass_average':Gm=G
 X=I*sx;Z=I*sz;wedge=comm(X,Z);L=(eye(4)-3*W)/2
 F=kron(L*L-L,wedge);D=-3*W/2
 Fm=(F+tau(F))/2-kron(D*D,wedge)
 if fault=='average_curvature_only':Fm=(F+tau(F))/2
 symbolic=s.Matrix(4,4,s.symbols('x:16'))
 principal_equations=list(s.Matrix.vstack(*[comm(symbolic,c).reshape(16,1) for c in cs]));mat,_=s.linear_eq_to_matrix(principal_equations,list(symbolic))
 joint,_=s.linear_eq_to_matrix(principal_equations+list(comm(symbolic,M)),list(symbolic))
 checks={
 'Clifford_and_unitary_mass':all(c*c==eye(4) and c.conjugate().T==c and c*M+M*c==z(4) for c in cs) and M.conjugate().T*M==eye(4),
 'native_graph_metric_at_base':h==2*a*eye(q),
 'projection_base':P*P==P and P.conjugate().T*S==S*P,
 'full_B_curvature':all(F==expectedB(K) for F,K in zip(FsB,Ks)),
 'full_C_curvature':all(F==expectedC(K) for F,K in zip(FsC,Ks)),
 'two_plane_coefficient_span':coefficient_span.det()==-3,
 'multiplicity_two_curvature_span':s.Matrix.hstack(*[F.reshape(q*q,1) for F in FsB+FsC]).rank()==8,
 'principal_and_joint_commutants':16-mat.rank()==2 and 16-joint.rank()==1,
 'mass_conjugation_involution':tau(tau(G))==G,
 'canonical_mass_not_parallel':comm(G,ML)!=z(q),
 'mass_average_parallel':comm(Gm,ML)==z(q) and Gm==theta/2,
 'averaged_B_curvature':all(F==-lift(K)/2 for F,K in zip(averaged,Ks)),
 'mass_slice_curvature_subtraction':Fm==-kron(eye(4),wedge)/4 and Fm!=z(q),
 }
 return {k:bool(v) for k,v in checks.items()}

def main():
 checks=compute();assert all(checks.values()),checks
 failures={}
 for fault in FAULTS:
  failed=[k for k,v in compute(fault).items() if not v]
  assert failed,('FAULT NOT DETECTED',fault)
  failures[fault]=failed
 report={'schema_version':'1.0','status':'conditional_exact_controls','exact_checks':checks,'fault_failures':failures,'universal_evidence':EVIDENCE,'probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'dependency_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in DEPS}}
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();path=ROOT/'lab/process'/OUT
 if args.write:path.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(path.read_text())==report,'stored evidence differs; investigate before intentional refresh'
 print(json.dumps({'checks':len(checks),'faults':len(failures),'all_pass':all(checks.values()),'fault_failures':failures}))
if __name__=='__main__':main()
