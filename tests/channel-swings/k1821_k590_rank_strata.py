#!/usr/bin/env python3
"""Finite rank-stratum specialization and exact nonfactorized controls.

No scientific producer is imported. Universal claims are proved in the linked
note; finite matrices test the construction and the boundaries of that proof.
"""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / 'lab/process/k1821-k590-rank-strata.json'

def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]

def transpose(a):
    return list(map(list, zip(*a)))

def mul(a, b):
    return [[sum((x*y for x,y in zip(row,col)),F(0)) for col in zip(*b)] for row in a]

def rank(a):
    a = [[F(x) for x in row] for row in a]
    r = 0
    for j in range(len(a[0])):
        p = next((i for i in range(r,len(a)) if a[i][j]),None)
        if p is None: continue
        a[r],a[p] = a[p],a[r]
        v=a[r][j]; a[r]=[x/v for x in a[r]]
        for i in range(len(a)):
            if i != r:
                v=a[i][j];a[i]=[x-v*y for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r

def subtract(a,b):
    return [[x-y for x,y in zip(ar,br)] for ar,br in zip(a,b)]

def zero(a):
    return not any(x for row in a for x in row)

def homology(high,low):
    if not zero(mul(low,high)):
        raise ValueError('composition is nonzero')
    a,b,c=len(high[0]),len(high),len(low)
    r2,r1=rank(high),rank(low)
    return [a-r2,b-r2-r1,c-r1]

def stratum(a,c,u,v):
    if not (0<=u<=a and 0<=v<=c):raise ValueError('invalid deficits')
    b=a+c;r2=a-u;r1=c-v
    dimension=r2*(a+b-r2)+r1*(b-r2+c-r1)
    return {'deficits':[u,v],'ranks':[r2,r1],'homology':[u,u+v,v],
            'dimension':dimension,'codimension':a*b+c*c-dimension}

def representative(s):
    # H=R, M=R^2, E=R^3; E_out=span(e0,e1), E_in=span(e2).
    high=[[F(i==j) for j in range(3)] for i in range(9)]
    low=[[F(j==i+3) for j in range(9)] for i in range(6)]
    w=[F(1),F(0),F(0),F(0),F(1),F(0)]
    p=[[x*y/2 for y in w] for x in w]
    reduced=mul([[x-F(s)*y for x,y in zip(ar,br)] for ar,br in zip(eye(6),p)],low)
    projectors=[[[F(i==j and i%3<2) for j in range(n)] for i in range(n)] for n in (3,9,6)]
    return high,low,reduced,p,w,projectors

def compute():
    controls=[]
    for s in ('0','1/2','1','2'):
        high,low,d,p,w,ps=representative(s)
        controls.append({'s':s,'homology':homology(high,d),'high_rank':rank(high),
                         'low_rank':rank(d),'both_projector_squares':zero(subtract(mul(ps[1],high),mul(high,ps[0]))) and zero(subtract(mul(ps[2],d),mul(d,ps[1]))),
                         'perturbation_rank':rank(subtract(d,low))})
    high,low,d,p,w,ps=representative(1)
    # Realignment of P in End(R^2) tensor End(R^3), operator Schmidt rank.
    realigned=[[p[3*i+k][3*j+l] for k in range(3) for l in range(3)] for i in range(2) for j in range(2)]
    pairing=[]
    for sign in (1,-1,0):
        g=[[sign*x for x in row] for row in p]
        pairing.append({'sign':sign,'annihilates_image':zero(mul(g,d)),
                        'representative_norm':str(mul([w],mul(g,[[x] for x in w]))[0][0])})
    # Add the missing relation: its image is the surviving middle cycle.
    lifted_cycle=[F(0)]*3+w
    repaired_high=[row+[lifted_cycle[i]] for i,row in enumerate(high)]
    repaired_homology=homology(repaired_high,d)
    inputs=['k590-k77-corrected-carrier-completion-squares.json','k446-k77-compatible-nilpotent-cohomology-obstruction.json']
    # Some old artifacts use a different file stem; K590 is the indispensable pin.
    pins={name:hashlib.sha256((ROOT/'lab/process'/name).read_bytes()).hexdigest() for name in inputs if (ROOT/'lab/process'/name).exists()}
    return {'schema_version':'1.0','claim_id':'K1821','status':'active_research',
        'target_claim':'NONE-NOT-A-KILL','classification':'INTERNAL_STRUCTURAL_ONLY',
        'input_sha256':pins,'dimensions':[10752,46592,35840],
        'full_strata':[stratum(10752,35840,u,v) for u,v in [(0,0),(0,1),(1,0),(1,1),(0,70),(21,0)]],
        'one_projector_half_dimensions':[5376,23296,17920],
        'formula':{'homology':'(u,u+v,v)','codimension':'u^2+u*v+v^2',
                   'boundary_split':'independent outgoing/incoming strata; dimensions and codimensions add'},
        'representative_controls':controls,'entangled_projector_rank':rank(p),
        'operator_schmidt_rank':rank(realigned),'pairing_controls':pairing,
        'full_size_rank_one_endpoint':{'ranks':[10752,35839],'homology':[0,1,1]},
        'extra_relation_control':{'dimensions':[4,9,6],'homology':repaired_homology,
                                  'source_action_selected':False,'changes_carrier':True},
        'factorwise_algebra':{'spectral_multiplicities':[192,192,64,64],
                             'rank_divisor':64,'rank_one_loss_in_algebra':False,
                             'conditional_on_declared_spectral_decomposition':True,
                             'real_lift_independently_proved':False},
        'claim_boundary':{'source_action_selected':False,'functional_domain_proved':False,
                          'physical_cohomology':False,'physical_positivity':False,'ledger_changed':False,
                          'novel_general_theorem':False}}

def validate(data):
    expected=compute()
    if data!=expected:raise ValueError('artifact differs from exact construction')
    if data['operator_schmidt_rank']!=4:raise ValueError('nonfactorization control failed')
    for row in data['representative_controls']:
        expected_h=[0,1,1] if row['s']=='1' else [0,0,0]
        if row['homology']!=expected_h or not row['both_projector_squares']:
            raise ValueError('rank-loss control failed')
    return True

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args()
    data=compute();validate(data)
    if args.write:ARTIFACT.write_text(json.dumps(data,indent=2)+'\n')
    else:validate(json.loads(ARTIFACT.read_text()))
    print('PASS: exact rank strata, nonfactorized endpoint and quotient-form controls')

if __name__=='__main__':main()
