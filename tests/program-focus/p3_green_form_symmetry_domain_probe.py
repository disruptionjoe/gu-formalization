#!/usr/bin/env python3
"""Finite Green-form controls; analytic transfer is separately cited/proved."""
from pathlib import Path
import hashlib
import json
import sys
import sympy as s

ROOT=Path(__file__).resolve().parents[2]
checks,controls=[],[]
def ck(name,p):
    assert bool(p),name
    checks.append(name)
def reject(name,p):
    assert not bool(p),name
    controls.append(name)
def graph(U):return s.Matrix.vstack(s.eye(U.cols),U)
def iso(c,L):return L.H*c*L==s.zeros(L.cols)
def invariant(J,L):return s.Matrix.hstack(L,J*L.conjugate()).rank()==L.rank()
def exchange(n,e):return s.BlockMatrix([[s.zeros(n),e*s.eye(n)],[s.eye(n),s.zeros(n)]]).as_explicit()
def normal(n):return s.diag(s.I*s.eye(n),-s.I*s.eye(n))

c=normal(1); J=exchange(1,-1)
ck('quaternionic_square',J*J.conjugate()==-s.eye(2))
ck('antiunitary',J.H*J==s.eye(2))
ck('commuting_c_antilinear',J*c.conjugate()==c*J)
ck('exchanges_c_eigenspaces',(J*s.eye(2)[:,0])[0]==0)
L=graph(s.eye(1))
ck('n1_lagrangian',iso(c,L) and L.rank()==1)
reject('n1_lagrangian_is_quaternionic_invariant',invariant(J,L))
a,b=s.symbols('a b',real=True);u=a+s.I*b
# Direct membership determinant for every complex graph scalar, not samples.
det=s.simplify(s.Matrix.hstack(s.Matrix([1,u]),J*s.Matrix([1,u]).conjugate()).det())
ck('all_scalar_graphs_membership_obstruction',det==1+a*a+b*b)
reject('whole_symmetry_space_is_isotropic',iso(c,s.eye(2)))
E=s.Matrix([[0,-1],[1,0]]); c4=normal(2);J4=exchange(2,-1);L4=graph(E)
ck('even_repair_skew_unitary',E.T==-E and E.H*E==s.eye(2))
ck('even_repair_isotropic',iso(c4,L4))
ck('even_repair_half_dimension',L4.rank()==2)
ck('even_repair_invariant',invariant(J4,L4))
ck('even_repair_orthogonal_c_complement',L4.H*c4*L4==s.zeros(2) and s.Matrix.hstack(L4,c4*L4).rank()==4)
reject('all_even_lagrangians_invariant',invariant(J4,graph(s.eye(2))))
for n in (1,2,3):
    Jr=exchange(n,1);cr=normal(n);Lr=graph(s.eye(n))
    ck(f'real_exchange_graph_{n}',iso(cr,Lr) and invariant(Jr,Lr))
Jp=s.diag(E,E)
ck('preserving_quaternionic_square',Jp*Jp.conjugate()==-s.eye(4))
ck('preserving_quaternionic_anticommutes_c',Jp*c4.conjugate()==-c4*Jp)
ck('preserving_quaternionic_graph',iso(c4,graph(s.eye(2))) and invariant(Jp,graph(s.eye(2))))
cu=s.diag(s.I,s.I,s.I,-s.I)
ck('unequal_real_case_anticommutes',cu.conjugate()==-cu)
ck('unequal_eigenspace_dimensions',len((cu-s.I*s.eye(4)).nullspace())==3 and len((cu+s.I*s.eye(4)).nullspace())==1)
Lu=s.Matrix([1,0,0,1]); orth=(Lu.H*cu).nullspace()
ck('unbalanced_even_total_has_isotropic_line',iso(cu,Lu))
ck('unbalanced_green_orthogonal_dimension',len(orth)==3)
reject('isotropic_line_is_green_lagrangian',len(orth)==Lu.rank())
# A nontrivial finite representation sees equal modules, not just dimension.
h=s.diag(1,-1);H=s.diag(h,h);U0=s.eye(2);U1=s.diag(1,-1)
L0,L1=graph(U0),graph(U1)
ck('two_distinct_admissible_real_graphs',iso(c4,L0) and iso(c4,L1) and L0!=L1)
ck('same_projected_representation',H*L0==L0*h and H*L1==L1*h)
intersection=4-s.Matrix.hstack(L0,L1).rank()
ck('actual_nontrivial_graph_intersection',intersection==1)
ck('relative_quotient_dimensions_equal',L0.rank()-intersection==L1.rank()-intersection==1)
# Compact linear symmetry must commute with c for V+ to carry its representation.
swap=exchange(2,1)
reject('arbitrary_symmetry_preserves_vplus',swap*c4==c4*swap)
# A whole periodic family passes pointwise but its unitary graph has monodromy.
t=s.symbols('t',real=True); phase=s.exp(s.I*t)
Jt=s.diag(1,phase); ct=normal(1);ut=s.exp(s.I*t/2);Lt=graph(s.Matrix([[ut]]))
ck('family_antiunitarity',s.simplify(Jt.H*Jt)==s.eye(2))
ck('family_real_square',s.simplify(Jt*Jt.conjugate())==s.eye(2))
ck('family_preserving_sign',s.simplify(Jt*ct.conjugate()+ct*Jt)==s.zeros(2))
ck('local_family_graph_isotropic',s.simplify(Lt.H*ct*Lt)==s.zeros(1))
ck('local_family_graph_invariant',s.simplify(Jt*Lt.conjugate()-Lt)==s.zeros(2,1))
ck('background_family_periodic',Jt.subs(t,0)==Jt.subs(t,2*s.pi))
ck('local_graph_endpoint_sign',ut.subs(t,2*s.pi)==-ut.subs(t,0))
reject('local_graph_is_periodic_domain',s.Matrix.hstack(Lt.subs(t,0),Lt.subs(t,2*s.pi)).rank()==1)
ck('full_circle_phase_winding',s.simplify(s.diff(phase,t)/phase)==s.I)

payload=dict(artifact='P3_GREEN_FORM_SYMMETRY_DOMAIN',program_target='P3xsymmetry',tier='T2',claim_effect='none',finite_supporting_checks=checks,contrary_controls=controls,counts=dict(supporting=len(checks),contrary=len(controls)),proof='Written all-dimension graph classification; analytic boundary transfer uses Baer-Ballmann Thm3.12/Remarks3.13 with stated hypotheses.',scope='Fixed positive-Hilbert Dirac boundary subclass; no GU realization, graded index, physical count or global family selection.',probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
report=ROOT/'lab/process/p3-green-form-symmetry-domain.json'
if __name__=='__main__':
    if '--write' in sys.argv:report.write_text(json.dumps(payload,indent=2)+'\n')
    else:assert json.loads(report.read_text())==payload,'evidence replay mismatch'
    print(json.dumps(dict(status='pass',counts=payload['counts'])))
