#!/usr/bin/env python3
"""Exact transport countercontrols; general orbit proof lives in the note."""
from pathlib import Path
import hashlib
import json
import sys
import sympy as s

ROOT = Path(__file__).resolve().parents[2]
checks, controls = [], []
def ck(name, predicate):
    assert bool(predicate), name
    checks.append(name)
def reject(name, predicate):
    assert not bool(predicate), name
    controls.append(name)
def zero(a):
    return s.simplify(a) == s.zeros(*a.shape)

I=s.eye(2); Z=s.zeros(2)
C1=s.diag(1,-1); C2=s.Matrix([[0,1],[1,0]])
Gamma=s.Matrix.hstack(C1,C2); j=Gamma.T/2
g=s.Matrix([[1,1],[0,1]]); R=s.diag(g,g)
Gp=g*Gamma*R.inv(); jp=R*j*g.inv()
ck('normalized_trace_inclusion',Gamma*j==I)
ck('transported_trace_inclusion',Gp*jp==I)
reject('moving_trace_equals_fixed_trace',Gp==Gamma)
P=s.eye(4)-j*Gamma; Pp=s.eye(4)-jp*Gp
ck('kernel_projector_idempotent',P*P==P)
ck('kernel_projector_rank',P.rank()==2)
ck('transported_projector',Pp==R*P*R.inv())
ck('transported_kernel',Gp*R*P==s.zeros(2,4))
reject('same_kernel_automatically_preserved',Gamma*R*P==s.zeros(2,4))
F=s.diag(g,R); T=s.diag(I,-s.eye(4))
Gext=s.zeros(6);Gext[:2,2:]=Gamma
jext=s.zeros(6);jext[2:,:2]=j
ck('form_degree_sign_covariant',T*F==F*T)
ck('trace_sign_anticommutator',T*Gext+Gext*T==s.zeros(6))
ck('inclusion_sign_anticommutator',T*jext+jext*T==s.zeros(6))
reject('covariant_sign_is_trace_morphism',T*Gext==Gext*T)
D=Gext+jext
reject('covariant_sign_is_same_symbol_symmetry',T*D==D*T)
# A split isotropy representation can carry nonscalar equivariant maps.
h=s.diag(-1,-1,1); A=s.diag(2,3,5)
ck('isotropy_map',A*h==h*A)
k=s.Matrix([[1,0,1],[0,1,0],[0,0,1]])
reject('isotropy_implies_full_group_commutant',A*k==k*A)
ck('orbit_representative_independence',k*h*A*(k*h).inv()==k*A*k.inv())
J0=s.eye(3); ck('isotropy_antilinear',J0*h.conjugate()==h*J0)
u=k*J0*k.conjugate().inv()
ck('transported_antilinear_square',u*u.conjugate()==s.eye(3))
K=s.eye(6); W=s.diag(2,2,3,3,3,3)
Kg=F.inv().H*K*F.inv(); Wg=F.inv().H*W*F.inv()
ck('density_dual_ratio_transport',Kg.inv()*Wg==F*(K.inv()*W)*F.inv())
ck('density_dual_pairing_invariance',F.H*Wg*F==W)
reject('pairing_covariance_implies_arrow_adjoint_equality',W.inv()*D.H*W==K.inv()*D.H*K)
reject('naive_conjugation_is_density_dual',F*W*F.inv()==Wg)
x=s.symbols('x',real=True)
Rx=s.Matrix([[1,x],[0,1]]); Ac=s.Matrix([[1,2],[0,-1]]); Q=s.Matrix([[0,1],[1,0]])
Ax=Rx*Ac*Rx.inv()-s.diff(Rx,x)*Rx.inv(); Qx=Rx*Q*Rx.inv()
ck('full_covariant_derivative_transport',zero(s.diff(Qx,x)+Ax*Qx-Qx*Ax-Rx*(Ac*Q-Q*Ac)*Rx.inv()))
wrong=Rx*Ac*Rx.inv()
reject('omit_connection_inhomogeneous_term',zero(s.diff(Qx,x)+wrong*Qx-Qx*wrong-Rx*(Ac*Q-Q*Ac)*Rx.inv()))
v=s.Matrix([x,x*x]); vp=Rx*v
ck('actual_section_covariance',zero(s.diff(vp,x)+Ax*vp-Rx*(s.diff(v,x)+Ac*v)))
# Square and isometry do not rescue missing diagram compatibility.
G3=s.zeros(3);G3[0,1]=1;j3=G3.T;T3=s.diag(1,-1,1)
for aa in (-1,1):
    for bb in (-1,1):
        H3=s.diag(aa,aa,bb)
        ck(f'actual_stabilizer_{aa}_{bb}',H3*G3==G3*H3 and H3*j3==j3*H3 and H3.H*H3==s.eye(3) and T3*H3.conjugate()==H3*T3)
ck('coflip_square_and_isometry',T3*T3.conjugate()==s.eye(3) and T3.H*T3==s.eye(3))
reject('coflip_covariance_square_isometry_force_arrows',T3*G3.conjugate()==G3*T3)
S3=s.Matrix([[1,1,0],[0,1,0],[0,0,1]]);Ts=S3*T3*S3.inv();Ks=S3.inv().H*S3.inv();Gs=S3*G3*S3.inv()
ck('moving_coflip_square_and_metric',Ts*Ts.conjugate()==s.eye(3) and Ts.H*Ks*Ts==Ks)
reject('moving_coflip_becomes_diagram_morphism',Ts*Gs.conjugate()==Gs*Ts)
reject('moving_coflip_preserves_frozen_metric',Ts.H*Ts==s.eye(3))

payload=dict(artifact='X_P1_P2_MOVING_GAUGE_NATURALITY',program_target='X-P1-P2',tier='T2',claim_effect='none',finite_supporting_checks=checks,contrary_controls=controls,counts=dict(supporting=len(checks),contrary=len(controls)),proof='Written orbit-isotropy, diagram-morphism and density-dual proofs; finite probes are controls only.',scope='Declared associated-bundle category; no class-C action or source-certified full extension.',probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
report=ROOT/'lab/process/x-p1-p2-moving-gauge-naturality.json'
if __name__=='__main__':
    if '--write' in sys.argv:report.write_text(json.dumps(payload,indent=2)+'\n')
    else:assert json.loads(report.read_text())==payload,'evidence replay mismatch'
    print(json.dumps(dict(status='pass',counts=payload['counts'])))
