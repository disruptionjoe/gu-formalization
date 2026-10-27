"""Exact finite equation controls for the written full graph connection theorem.
Finite controls are not a raw-class classification or continuum PDE proof.
"""
from pathlib import Path
import json, argparse, hashlib
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def compute(fault=None):
 I=s.I; z=s.zeros; eye=s.eye
 sx=s.Matrix([[0,1],[1,0]]); sy=s.Matrix([[0,-I],[I,0]]); sz=s.diag(1,-1)
 C=[s.kronecker_product(sx,eye(2)),s.kronecker_product(sz,sx),s.kronecker_product(sz,sz)]
 M=-I*s.kronecker_product(sz,sy); W=I*C[0]*C[1]*C[2]
 # Three-dimensional multiplicity example embedded in the eight-dimensional native chart.
 n=3; X=z(n);X[0,1]=1;X[1,0]=-1; Z=z(n);Z[1,2]=1;Z[2,1]=-1
 a=s.Rational(9,280); lift=lambda b:s.kronecker_product(eye(4),b)
 B=s.diag(s.Rational(3,4),0,0); D=s.diag(0,s.Rational(3,5),0)
 A=s.diag(s.Rational(5,4),s.Rational(4,5),1)
 Y=s.Matrix.vstack(lift(eye(n)),lift(A),lift(B),lift(D)); q=4*n
 T=s.diag(*([1]*(2*q)+[-1]*(2*q))); ZZ=s.diag(*([1]*q+[-1]*q+[1]*q+[-1]*q)); WW=s.diag(*([s.kronecker_product(W,eye(n))]*4))
 S=a*T+3*a*WW*ZZ; h=Y.conjugate().T*S*Y; hi=h.inv()
 # Left unitary rotation of A supplies a noncommuting tangent at a nontrivial graph.
 dY=s.Matrix.vstack(z(q),lift(X*A),z(q),z(q)); dh=dY.conjugate().T*S*Y+Y.conjugate().T*S*dY
 G=hi*Y.conjugate().T*S*dY
 if fault=='omit_metric_inverse':G=Y.conjugate().T*S*dY
 PS=Y*hi*Y.conjugate().T*S; R=dY-Y*G
 comm=lambda u,v:u*v-v*u
 checks={
 'Cl4_principal_and_mass':all(c*c==eye(4) and c.conjugate().T==c and c*M+M*c==z(4) for c in C) and M.conjugate().T==-M,
 'W_square_and_mass_anticommutator':W*W==eye(4) and W*M+M*W==z(4),
 'graph_current':h==2*a*lift(eye(n)-D.conjugate().T*D),
 'S_projection':PS*PS==PS and PS.conjugate().T*S==S*PS,
 'metric_compatibility':dh==G.conjugate().T*h+h*G,
 'horizontal_remainder':Y.conjugate().T*S*R==z(q),
 'principal_connection_commutes':all(comm(G,s.kronecker_product(c,eye(n)))==z(q) for c in C),
 'mass_current':h*lift(eye(n))*s.kronecker_product(M,eye(n))+s.kronecker_product(M.conjugate().T,eye(n))*h==z(q),
 }
 # Connection curvature on U(8) slice from Maurer-Cartan at origin.
 lam=(eye(4)-3*W)/2
 if fault=='replace_pairing_coefficient':lam=(eye(4)-2*W)/2
 F=s.kronecker_product(lam*lam-lam,comm(X,Z))
 checks['nonabelian_curvature']=F==2*s.kronecker_product(eye(4),comm(X,Z)) and F!=z(q)
 checks['scalar_curve_flat_control']=s.kronecker_product(lam*lam-lam,comm(X,X))==z(q)
 # Nonconstant h=2a diag(1-c^2,1,1), c=3/5, dc=1: flat metric connection.
 c=s.Rational(3,5); hh=2*a*s.diag(1-c*c,1,1); dhh=-4*a*s.diag(c,0,0); flat=s.diag(-c/(1-c*c),0,0)
 if fault=='zero_variable_metric_connection':flat=z(n)
 checks['variable_metric_flat_connection']=dhh==flat.conjugate().T*hh+hh*flat
 # Finite Hermitian extension identity, general injective X and prescribed N.
 XX=s.Matrix([[1,0],[0,1],[1,1]]); H=s.diag(1,-1,1); LL=(XX.T*XX).inv()*XX.T
 QQ=s.Matrix([[2,I,0],[-I,3,1],[0,1,-1]]); NN=H*QQ*XX; cc=XX.T*H*NN
 full=H*NN*LL+LL.T*NN.conjugate().T*H-LL.T*cc*LL
 if fault=='omit_extension_subtraction':full+=LL.T*cc*LL
 K=H*full
 checks['hermitian_extension']=H*K==K.conjugate().T*H and K*XX==NN
 return {k:bool(v) for k,v in checks.items()}
def main():
 checks=compute();assert all(checks.values()),checks
 faults={}
 for f in ['omit_metric_inverse','replace_pairing_coefficient','zero_variable_metric_connection','omit_extension_subtraction']:
  failed=[k for k,v in compute(f).items() if not v];assert failed,f;faults[f]=failed
 report={'schema_version':'1.0','status':'conditional_exact_equation_controls','exact_checks':checks,'fault_failures':faults,'universal_evidence':'Written full graph connection, curvature, domain and extension proofs; finite tests do not prove all-family raw compatibility.','native_bridge':'K2132 fullCl4 multiplicity decomposition, inherited S=a t+3a W Z; 3x3 controls embed in native multiplicity8.'}
 report['probe_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
 report['native_bridge_sha256']=hashlib.sha256((ROOT/'explorations/conditional-build/k2132-conserving-positive-sector-classification-2026-10-27.md').read_bytes()).hexdigest()
 parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args()
 p=ROOT/'lab/process/k2135-full-graph-current-connection.json'
 if args.write:p.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(p.read_text())==report,'stored evidence differs'
 print('PASS',len(checks),'exact equation controls;',len(faults),'input/equation faults')
if __name__=='__main__':main()
