#!/usr/bin/env python3
"""Exact Clifford/form controls; continuum gap proved in the accompanying note."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,hashlib,json
import sympy as s
import k2212_mass_connection_algebra_probe as old
ROOT=Path(__file__).resolve().parents[2]
X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1)
I=s.eye(4);zero=s.zeros(4);M=s.kronecker_product(X,s.eye(2));S=s.kronecker_product(Z,s.eye(2))
C=[s.kronecker_product(Z,p) for p in [X,Y,Z]]
def controls(fault=None):
 c={}
 def ck(k,v):c[k]=bool(v)
 ck('mass_involution',M*M==I and M.H==M)
 ck('S_involution',S*S==I and S.H==S)
 ck('mass_S_anticommutator',M*S+S*M==zero)
 for j,a in enumerate(C):
  ck('Clifford_'+str(j),a*a==I and a.H==a and a*M+M*a==zero and a*S==S*a)
  for k,b in enumerate(C):ck(f'Clifford_pair_{j}_{k}',a*b+b*a==2*int(j==k)*I)
 # Actual faithful Cl77 generators, not only a small representation.
 mm,add,sc=old.mul,old.add,old.scale
 mass=sc(old.P[0],-s.I);ax=sc(old.Q,-s.I)
 for j in old.O[1:]:
  a=old.C[j]
  ck('native_anticommutation_'+str(j),add(mm(mass,a),mm(a,mass))==old.Z)
 ck('native_mass_square',mm(mass,mass)==old.I)
 # Correlated coefficients: inf(m)-sup(b)=-97, yet inf(m-|b|)=2.
 pairs=[(3,1),(102,100)]
 ck('correlated_gap',min(m-b for m,b in pairs)==2 and min(m for m,b in pairs)-max(b for m,b in pairs)<0)
 for n,(m,b) in enumerate(pairs):
  V=17*S+m*M+b*S*C[0]
  form=(M*V+V*M)/2
  ck('pointwise_form_'+str(n),form==m*I+b*M*S*C[0])
  ck('pointwise_eigenvalues_'+str(n),set(form.eigenvals())=={m-b,m+b})
 # Exact finite periodic derivative with nonconstant potentials, no derivative penalty.
 D=s.zeros(12)
 for j in range(3):
  k=(j+1)%3
  D[j*4:(j+1)*4,k*4:(k+1)*4]=-s.I*C[0]
  D[k*4:(k+1)*4,j*4:(j+1)*4]=s.I*C[0]
 MM=s.diag(M,M,M);potential=s.diag(3*M+S,102*M+100*S*C[0]-7*S,5*M+3*S*C[1])
 H=D+potential
 if fault=='commuting_contamination':H+=s.diag(9*I,9*I,9*I)
 form=(MM*H+H*MM)/2-2*s.eye(12)
 ck('finite_Hermitian',H==H.H)
 ck('finite_correlated_gap_form',form.is_positive_semidefinite is True)
 # A genuine scalar contamination defeats the claimed universal bound.
 ck('scalar_contamination_counterexample',(M+I).det()==0)
 U=(3*I+4*s.I*C[0])/5;Ud=U.H;k=s.Integer(2)
 dU=s.I*k*C[0]*U;dUd=-s.I*k*Ud*C[0]
 A=[s.expand(U*a*Ud) for a in C]
 correction=-s.I*U*C[0]*dUd
 if fault=='frame_sign':correction=-correction
 ck('static_frame_derivative',correction==-k*I)
 ck('frame_unitary',U*Ud==I)
 ck('divergence_free_twist',dU*C[0]*Ud+U*C[0]*dUd==zero)
 massU=U*M*Ud
 for j,a in enumerate(A):ck('frozen_mass_'+str(j),a*massU+massU*a==zero)
 # Frozen-symbol gap 1, global shifted spectrum includes zero when k=2.
 p=s.sqrt(3);h=p*C[0]+M+2*I
 ck('shifted_spectrum_zero',s.simplify(h.det())==0 and (p*C[0]+M)**2==4*I)
 K=s.I*C[0]*M;proj=(I+K)/2
 if fault=='wall_projector':proj=(I-K)/2
 ck('wall_normal_equation',(s.I*C[0]+M)*proj==zero)
 ck('wall_tangent_preservation',all(a*proj==proj*a for a in C[1:]))
 x,a=s.symbols('x a',real=True);f=s.cosh(x)**(-a)
 ck('inherited_wall_profile',s.simplify(s.diff(f,x)+a*s.tanh(x)*f)==0)
 for sign in [-1,1]:
  fp=s.exp(-a*sign*x)
  ck('step_wall_'+str(sign),s.diff(fp,x)+a*sign*fp==0)
 ck('step_wall_continuity',s.exp(-a*x).subs(x,0)==s.exp(a*x).subs(x,0))
 return c
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
 c=controls();assert all(c.values()),[k for k,v in c.items() if not v]
 faults={}
 for f in ['commuting_contamination','frame_sign','wall_projector']:
  bad=[k for k,v in controls(f).items() if not v];assert bad,('undetected',f);faults[f]=bad
 deps=['tests/channel-swings/k2212_mass_connection_algebra_probe.py','explorations/conditional-build/k2212-mass-connection-algebra-2026-10-28.md','explorations/conditional-build/k1967-paired-raw-coefficient-observation-2026-10-22.md','explorations/conditional-build/k2215-variable-mass-gap-2026-10-28.md']
 report=dict(result_id='K2215',status='conditional_variable_gap_and_frame_boundary',checks=c,controls=len(c),fault_failures=faults,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),evidence_kinds='Universal Hilbert-space proof; exact Clifford and finite form controls; inherited wall mechanism; explicit moving-symbol counterexample. No physical source selection.')
 dst=ROOT/'lab/process/k2215-variable-mass-gap.json'
 if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(dst.read_text())==report
 print(json.dumps(dict(result='K2215',controls=len(c),faults=faults)))
if __name__=='__main__':main()
