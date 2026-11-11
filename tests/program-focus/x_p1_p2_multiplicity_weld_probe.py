#!/usr/bin/env python3
"""Exact native multiplicity census and commutants, not a class-C action test."""
from pathlib import Path
import hashlib
import importlib.util
import json
import sys
import sympy as s

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT/'tests/shiab_b5_observer_symbol_multiplicity_matrix.py'
spec = importlib.util.spec_from_file_location('native_multiplicity',SOURCE)
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)
checks, controls = [], []
def ck(name, test):
    assert bool(test), name
    checks.append(name)
def reject(name, test):
    assert not bool(test), name
    controls.append(name)

names=list(m.TYPES)
mult={n:sum(slot.h_type==n for slot in m.SLOTS) for n in names}
arrows=[(i,j) for i in names for j in names if m.symbol_multiplicity(m.TYPES[i],m.TYPES[j])==1]
ck('twelve_isotypic_types',len(names)==12)
ck('four_triples_eight_singles',sorted(mult.values())==[1]*8+[3]*4)
ck('twenty_native_slots',sum(mult.values())==20)
ck('forty_type_arrows',len(arrows)==40)
ck('136_scalar_cells',sum(mult[i]*mult[j] for i,j in arrows)==136)
variables=[]
X={}
for n in names:
    v=s.symbols('x_'+n+':'+str(mult[n]**2))
    variables.extend(v)
    X[n]=s.Matrix(mult[n],mult[n],v)
ck('44_endomorphism_variables',len(variables)==44)
A={(i,j):s.ones(mult[j],mult[i]) for i,j in arrows}
eq=[]
for i,j in arrows: eq.extend(X[j]*A[i,j]-A[i,j]*X[i])
M,_=s.linear_eq_to_matrix(eq,variables)
ck('native_symbol_commutant_rank27',M.shape==(136,44) and M.rank()==27)
ck('native_symbol_commutant_dimension17',len(M.nullspace())==17)
# Verify the analytic 1+4*4 decomposition by constructing its basis independently.
basis=[{n:s.eye(mult[n]) for n in names}]
for n in names:
    if mult[n]!=3: continue
    Q=s.Matrix([[1,1,1],[1,-1,0],[1,0,-1]])
    ck('bright_dark_basis_'+n,Q.det()!=0 and s.ones(1,3)*Q[:,1:]==s.zeros(1,2))
    for a in range(2):
        for b in range(2):
            E=s.zeros(3); E[a+1,b+1]=1
            T={k:s.zeros(mult[k]) for k in names};T[n]=Q*E*Q.inv();basis.append(T)
ck('seventeen_constructed_commuting_maps',all(T[j]*A[i,j]==A[i,j]*T[i] for T in basis for i,j in arrows))
flat=lambda T:s.Matrix([v for n in names for v in list(T[n])])
ck('constructed_commutant_basis_independent',s.Matrix.hstack(*map(flat,basis)).rank()==17)
extra=[]
for n in names:
    if mult[n]==3:
        E=s.zeros(3);E[0,1]=1
        F=E.T
        extra.extend(X[n]*E-E*X[n]);extra.extend(X[n]*F-F*X[n])
N,_=s.linear_eq_to_matrix(eq+extra,variables)
ck('augmented_commutant_rank43',N.rank()==43)
ck('augmented_commutant_scalar',N.nullspace()==[flat({n:s.eye(mult[n]) for n in names})])
# Native support connectivity is a premise of the coefficient-uniform proof.
nodes=[(n,k) for n in names for k in range(mult[n])]
adj={v:set() for v in nodes}
for i,j in arrows:
    for a in range(mult[i]):
        for b in range(mult[j]):adj[i,a].add((j,b));adj[j,b].add((i,a))
seen={nodes[0]};todo=list(seen)
while todo:
    for v in adj[todo.pop()]-seen:seen.add(v);todo.append(v)
ck('full_scalar_support_connected',len(seen)==20)
P={n:(s.Matrix([[0,1,0],[1,0,0],[0,0,1]]) if mult[n]==3 else s.eye(1)) for n in names}
ck('mixing_control_intertwines_all_arrows',all(P[j]*A[i,j]==A[i,j]*P[i] for i,j in arrows))
ck('mixing_control_square_one',all(P[n]*P[n].conjugate()==s.eye(mult[n]) for n in names))
ck('mixing_control_positive_gram_isometry',all(P[n].H*P[n]==s.eye(mult[n]) for n in names))
ck('mirror_types_preserve_multiplicity',all(mult[n]==mult[m.TYPES[n].mirror] for n in names))
ck('mirror_arrows_exist',all((m.TYPES[i].mirror,m.TYPES[j].mirror) in A for i,j in arrows))
ck('mixing_control_mirror_balanced',all(P[n]==P[m.TYPES[n].mirror] for n in names))
E=s.zeros(3);E[0,1]=1
reject('mixing_control_preserves_extended_gamma',P['Lp']*E==E*P['Lp'])
reject('connected_support_forces_scalar_without_gamma',M.rank()==43)
reject('nonzero_intertwiner_is_invertible',s.diag(1,0).det()!=0)
# Mixing can solve an intertwiner problem that the diagonal ansatz cannot.
H=s.diag(2,3);G=s.diag(3,2);S=s.Matrix([[0,1],[1,0]])
ck('nondiagonal_intertwiner_exists',S*H==G*S and S.det()!=0)
a,b=s.symbols('a b');diag=s.diag(a,b)
ck('diagonal_intertwiner_only_zero',s.solve(list(diag*H-G*diag),(a,b))=={a:0,b:0})
reject('invertible_intertwiner_forces_prescribed_square', (2*S)*(2*S).conjugate()==s.eye(2))
J=s.Matrix([[0,-1],[1,0]])
ck('intertwiner_square_can_be_negative',J*J.conjugate()==-s.eye(2))
# Pairing-adjoint identity, including a genuine wrong-pairing control.
K=s.diag(1,-1);Pform=s.diag(2,-3);T=K.inv()*Pform
op=s.Matrix([[0,1],[-1,0]])
ck('K_adjoint_selfadjoint_control',K.inv()*op.H*K==op)
reject('distinct_hermitian_pairings_need_not_share_adjoint',Pform.inv()*op.H*Pform==op)
ck('pairing_ratio_records_failed_commutation',T*op!=op*T)
x=s.symbols('x',nonnegative=True)
w=s.exp(x);f=x*s.exp(-2*x);g=x*s.exp(-3*x)
lhs=s.integrate(w*s.diff(f,x)*g,(x,0,s.oo))
rhs=s.integrate(w*f*(-s.diff(g,x)-g),(x,0,s.oo))
wrong=s.integrate(w*f*(-s.diff(g,x)),(x,0,s.oo))
ck('weighted_formal_adjoint_green_identity',lhs==rhs)
reject('pointwise_pairing_rescaling_preserves_formal_adjoint',lhs==wrong)
# Complete sparse-stratum successor: quotient the named-map diagonal variables.
def vertex(n,k): return (n,0 if mult[n]==3 and k<2 else k)
vertices=sorted({vertex(n,k) for n,k in nodes})
ck('sixteen_named_map_variables',len(vertices)==16)
parent={v:v for v in vertices}
def find(v):
    while parent[v]!=v:v=parent[v]
    return v
chosen=[]
for i,j in arrows:
    for a in range(mult[i]):
        for b in range(mult[j]):
            u,v=find(vertex(i,a)),find(vertex(j,b))
            if u!=v:parent[u]=v;chosen.append((i,j,b,a))
ck('native_sparse_spanning_tree_found',len(chosen)==15)
def sparse_rank(cells):
    matrices={e:s.zeros(*A[e].shape) for e in arrows}
    for i,j,b,a in cells:matrices[i,j][b,a]=1
    equations=list(extra)
    for i,j in arrows:equations.extend(X[j]*matrices[i,j]-matrices[i,j]*X[i])
    matrix,_=s.linear_eq_to_matrix(equations,variables)
    return matrix.rank()
ck('sparse_connected_rank43',sparse_rank(chosen)==43)
ck('sparse_two_component_rank42',sparse_rank(chosen[:-1])==42)
ck('zero_symbol_named_map_rank28',sparse_rank([])==28)
reject('nonzero_support_required_for_scalar_rigidity',sparse_rank(chosen[:-1])==43)
exchange=s.Matrix([[0,1],[1,0]])
scales=s.diag(2,s.Rational(1,2))
coflip=exchange*scales
ck('exchanged_components_same_square_nonunit_scales',coflip*coflip.conjugate()==s.eye(2))
reject('same_square_forces_each_component_unit_phase',scales.H*scales==s.eye(2))
bad=exchange*s.diag(2,2)
reject('arbitrary_exchanged_component_scales_preserve_square',bad*bad.conjugate()==s.eye(2))
payload={'artifact':'X_P1_P2_MULTIPLICITY_WELD','program_target':'X-P1-P2','tier':'T2',
 'claim_effect':'none','native_dimensions':{'types':12,'slots':20,'arrows':40,'cells':136,'variables':44,'symbol_rank':27,'augmented_rank':43,'merged_vertices':16,'sparse_tree_rank':43,'sparse_two_component_rank':42,'zero_symbol_rank':28},
 'supporting_checks':checks,'contrary_controls':controls,'counts':{'supporting':len(checks),'contrary':len(controls)},
 'universal_proof':'Commutation with E01/E10 diagonalizes provenance commutant; nonzero scalar cells and connected support force one scalar. Every sparse pattern has C^c commutant on the merged sixteen-variable support graph. Samples do not prove this statement.',
 'scope':'H-symbol coefficient category with fixed extended Gamma/j; existence, full covariance, action membership and domain transfer remain open.',
 'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
report=ROOT/'lab/process/x-p1-p2-multiplicity-weld.json'
if __name__=='__main__':
    if '--write' in sys.argv:report.write_text(json.dumps(payload,indent=2)+'\n')
    else:assert json.loads(report.read_text())==payload,'evidence replay mismatch'
    print(json.dumps({'counts':payload['counts'],'status':'pass','native':payload['native_dimensions']}))
