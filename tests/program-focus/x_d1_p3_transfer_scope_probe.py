#!/usr/bin/env python3
"""Exact finite support for X-D1-P3; no topological or physical-index certification."""
import argparse
import json
from fractions import Fraction as Q
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[2]
checks, controls = [], []
def check(name, proposition):
    assert proposition, name
    checks.append(name)
def control(name, proposition):
    assert proposition, name
    controls.append(name)
def mul(a, b):
    return (a[0]*b[0]+a[1]*b[1], a[0]*b[1]+a[1]*b[0])
ep, em = (Q(1, 2), Q(1, 2)), (Q(1, 2), Q(-1, 2))
check('group_ring_plus_idempotent', mul(ep, ep) == ep)
check('group_ring_minus_idempotent', mul(em, em) == em)
check('group_ring_orthogonal_idempotents', mul(ep, em) == (0, 0))
check('group_ring_idempotents_sum_to_one', tuple(a+b for a,b in zip(ep,em)) == (1,0))
rank = lambda v: sum(v)
character = lambda v: v[0]-v[1]
check('rank_one_pullbacks_identical', rank((1,0)) == rank((0,1)) == 1)
check('holonomy_character_distinct', character((1,0)) == 1 and character((0,1)) == -1)
check('H0_ranks_distinct', (1,0)[0] != (0,1)[0])
a,b,c,d=s.symbols('a b c d',integer=True)
check('character_additive_symbolic', s.expand((a+c)-(b+d)-(a-b)-(c-d)) == 0)
check('invariant_rank_additive_symbolic', s.expand((a+c)-a-c) == 0)
check('tensor_square_sign_is_trivial', mul((0,1),(0,1)) == (1,0))
eta=(-1,1)
check('representation_eta_square', mul(eta,eta) == tuple(-2*x for x in eta))
control('representation_eta_not_additive_two_torsion', tuple(2*x for x in eta) != (0,0))
control('representation_eta_square_not_zero', mul(eta,eta) != (0,0))
check('mod3_character_distinct', character((1,0))%3 != character((0,1))%3)
control('mod2_character_loses_distinction', character((1,0))%2 == character((0,1))%2)

def betti(differentials, p):
    ranks=[0]+[int(x%p != 0) for x in differentials]+[0]
    return [1-ranks[i]-ranks[i+1] for i in range(4)]
u,t=betti([0,2,0],3),betti([2,0,2],3)
check('untwisted_cellular_betti',u==[1,0,0,1])
check('D1_twisted_cellular_betti',t==[0,0,0,0])
control('both_Euler_characteristics_zero',sum((-1)**i*x for i,x in enumerate(u))==sum((-1)**i*x for i,x in enumerate(t))==0)
control('mod2_transfer_hypothesis_fails',betti([0,2,0],2)==[1,1,1,1])
check('two_inverse_mod3',2*2%3==1)
check('all_addHom_Z2_Z3_generator_images_zero',[x for x in range(3) if 2*x%3==0]==[0])
control('Z4_additive_target_retains_two_torsion',[x for x in range(4) if 2*x%4==0]==[0,2])
# Quaternion q times a pure imaginary u; verify universal polynomial identities.
w,x,y,z,i,j,k=s.symbols('w x y z i j k',real=True)
q=s.Matrix([w,x,y,z]);qu=s.Matrix([-x*i-y*j-z*k,w*i+y*k-z*j,w*j+z*i-x*k,w*k+x*j-y*i])
check('quaternion_product_orthogonal_to_q',s.expand(q.dot(qu))==0)
check('quaternion_product_norm',s.expand(qu.dot(qu)-q.dot(q)*(i*i+j*j+k*k))==0)
check('sign_change_on_q_matches_line_tensor',qu.subs({w:-w,x:-x,y:-y,z:-z},simultaneous=True)==-qu)
S=s.Matrix([[a,b,c],[b,d,i],[c,i,j]])
check('minus_identity_has_trivial_symmetric_square_action',(-s.eye(3))*S*(-s.eye(3))==S)
# Distinguish the finite topological K quotient from the representation ring.
check('topological_eta_relation_implies_two_torsion',s.expand((1+a)**2-1-a*a)==2*a)
control('constant_rank_does_not_determine_character',rank((2,0))==rank((1,1)) and character((2,0))!=character((1,1)))
report={'target':'X-D1-P3','status':'constrained','checks':checks,'controls':controls,
        'counterexample':{'coefficient_ring':'Z_(3); finite probe includes F3 reduction','trivial':{'rank':1,'H0_rank':1,'trace':1},'sign':{'rank':1,'H0_rank':0,'trace':-1}},
        'evidence_kind':'exact finite algebra and symbolic quaternion identities; written topology and K-theory are not machine-certified',
        'claim_ceiling':'no two-data floor, class-C kill, realized index or physical count'}
parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args()
p=ROOT/'lab/process/x-d1-p3-three-local-scope.json'
if args.write:p.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(p.read_text())==report
print(json.dumps({'checks':len(checks),'controls':len(controls),'status':'pass'}))
