#!/usr/bin/env python3
"""Exact symbol-support and variational-pairing controls, not a class-C action certificate."""
import argparse,hashlib,importlib.util,json,sys
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('weld_symbol_matrix',ROOT/'tests/shiab_b5_observer_symbol_multiplicity_matrix.py')
m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
checks=[];controls=[]
def ck(n,v):
    assert bool(v),n
    checks.append(n)
def ct(n,v):
    assert bool(v),n
    controls.append(n)
vertices=[v.name for v in m.SLOTS];mirror={v.name:v.mirror for v in m.SLOTS}
mult={(a.name,b.name):m.symbol_multiplicity(m.TYPES[a.h_type],m.TYPES[b.h_type]) for a in m.SLOTS for b in m.SLOTS}
cells={e for e,n in mult.items() if n};edges={tuple(sorted(e)) for e in cells}
ck('actual_slots_and_directed_cells',len(vertices)==20 and len(cells)==136)
ck('Schur_cells_zero_or_one',set(mult.values())=={0,1})
ck('transpose_closed_support',all((b,a) in cells for a,b in cells))
ck('mirror_closed_support',all((mirror[a],mirror[b]) in cells for a,b in cells))
ck('no_self_loops',all(a!=b for a,b in edges))
def components(edge_set):
    unseen=set(vertices);parts=[]
    while unseen:
        seed=min(unseen);part={seed};todo=[seed];unseen.remove(seed)
        while todo:
            a=todo.pop()
            neighbors={y if x==a else x for x,y in edge_set if a in (x,y)}
            for b in neighbors & unseen:unseen.remove(b);part.add(b);todo.append(b)
        parts.append(sorted(part))
    return parts
parts=components(edges);bridges=[e for e in sorted(edges) if len(components(edges-{e}))>len(parts)]
ck('full_support_connected',len(parts)==1)
ck('undirected_cycle_rank',len(edges)==68 and len(edges)-len(vertices)+len(parts)==49)
ck('no_single_bridge',bridges==[])
e=('S:E+:L16+','S:E-:R16+');et=e[::-1];me=(mirror[e[0]],mirror[e[1]]);met=me[::-1]
ck('actual_four_cell_orbit_distinct',len({e,et,me,met})==4 and {e,et,me,met}<=cells)
a={edge:s.Integer(1) for edge in cells};a[e]=a[et]=s.Integer(2)
ck('counterprofile_all_cells_nonzero',all(x!=0 for x in a.values()))
ck('counterprofile_transpose_weights_equal',all(a[(x,y)]==a[(y,x)] for x,y in cells))
lam={edge:a[(mirror[edge[0]],mirror[edge[1]])]/a[edge] for edge in cells}
ct('two_cycle_not_flat',lam[e]*lam[et]==s.Rational(1,4))
constraint=s.Matrix([[-1,2],[2,-1]])
ct('two_cycle_forces_zero_phases',constraint.det()==-3 and constraint.rank()==2)
ct('connected_support_does_not_imply_coflip_compatibility',len(parts)==1 and lam[e]!=1)
# Positive family retains mirror balance; no assertion that it is a full physical action.
balanced={edge:s.Integer(1+sum(ord(c) for c in min(edge,(mirror[edge[0]],mirror[edge[1]]))[0])%7) for edge in cells}
ck('mirror_balanced_positive_family',all(balanced[edge]==balanced[(mirror[edge[0]],mirror[edge[1]])] for edge in cells))
ck('global_phase_solves_balanced_family',all(balanced[edge]-balanced[(mirror[edge[0]],mirror[edge[1]])]==0 for edge in cells))
# A coflip involution also identifies mirror phases; build that augmented graph.
pair={e[0],mirror[e[0]]}
cut={edge for edge in edges if (edge[0] in pair)==(edge[1] in pair)}
mirror_edges={tuple(sorted((v,mirror[v]))) for v in vertices}
augmented=components(cut|mirror_edges)
ck('planted_degenerate_support_two_mirror_components',len(augmented)==2)
ct('disconnected_balance_allows_relative_sign',all((1 if x in pair else -1)==(1 if y in pair else -1) for x,y in cut|mirror_edges))
# Constant slot twists cannot change an already central endpoint mismatch.
C0=s.eye(2);C1=-s.eye(2);phase=s.diag(1,-1)
ck('constant_slot_twist_preserves_central_return',(phase*C0).inv()*(phase*C1)==-s.eye(2))
# Formal first-order adjoint: A∂ is P-self-adjoint iff AᵀP+PA=0.
K=s.diag(1,-1);P=s.diag(1,-2);J=s.Matrix([[0,1],[-1,0]]);A=P.inv()*J
ck('density_dual_first_order_skew_coefficient',J.T==-J)
ck('action_pairing_formal_symmetry',A.T*P+P*A==s.zeros(2))
ct('K_pairing_formal_symmetry_fails',A.T*K+K*A==s.Matrix([[0,s.Rational(1,2)],[s.Rational(1,2),0]]))
ck('identified_pairing_control', (K.inv()*J).T*K+K*(K.inv()*J)==s.zeros(2))
refs=['tests/shiab_b5_observer_symbol_multiplicity_matrix.py','tests/channel-swings/full20_dewitt_loop_transport_probe.py','explorations/b5-curved-coflip-green-transport-2026-08-20.md']
report={'target':'X-P1-P2','status':'constrained','checks':checks,'controls':controls,'graph':{'vertices':len(vertices),'directed_cells':len(cells),'undirected_edges':len(edges),'components':len(parts),'cycle_rank':49,'bridges':bridges},'counterprofile':{'twice_weight_cells':[e,et],'mirror_cells':[me,met],'cycle_product':'1/4','phase_constraint_determinant':'-3'},'pairing_control':{'P':str(P),'K':str(K),'A':str(A),'K_defect':str(A.T*K+K*A)},'provenance':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in refs},'evidence_kind':'exact native multiplicities/support, rational coefficient and pairing controls; inherited geometric coflip identities not recomputed','ceiling':'scalar-slot-phase ansatz only; counterprofiles not certified class-C actions; no datum floor or source verdict'}
report=json.loads(json.dumps(report))  # canonical JSON arrays for tuple-valued cell labels
p=ROOT/'lab/process/x-p1-p2-weld-scope.json';ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
if args.write:p.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(p.read_text())==report
print(json.dumps({'checks':len(checks),'controls':len(controls),'graph':report['graph'],'status':'pass'}))
