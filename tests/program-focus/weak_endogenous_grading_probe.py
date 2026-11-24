#!/usr/bin/env python3
"""Exact independent controls for the fixed-object weak/Lorentz closure theorem.

The general theorem is proved in the companion article. These checks certify
its source-built rational geometry, the separating Casimir, a genuine weak
quaternionic triple, and countercontrols. No spectral/domain/physical claim.
"""
import argparse
import importlib.util
import json
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[2])
ap.add_argument('--output', type=Path)
ap.add_argument('--mutate', choices=['drop-trace-motion', 'drop-boosts'])
args = ap.parse_args()
p = args.repo / 'tests/channel-swings/joe_directed_sa1_soldered_ad_selector.py'
spec = importlib.util.spec_from_file_location('sa1_geometry', p)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
# Parent helpers parse their own legacy mutations; isolate this probe's controls.
m.MUT = ''
checks = []
def check(name, ok, kind='support'):
    checks.append({'name':name, 'pass':bool(ok), 'kind':kind})
def neg(A): return [[-x for x in r] for r in A]
def scale(A, a): return [[a*x for x in r] for r in A]
def add(A, B): return m.matadd(A, B)
def mat(v): return [v[i:i+10] for i in range(0,100,10)]
def independent(ms):
    rows, _ = m.rref([m.flat(A) for A in ms])
    return [mat(v) for v in rows]
G = m.dewitt(F(1,2))
T,D = m.adapted_congruence(G)
red, piv = m.rref([r + [F(i==j) for j in range(10)] for i,r in enumerate(T)])
Ti = [r[10:] for r in red]
delta = [m.matmul(Ti,m.matmul(m.rho_sym(X),T)) for X in m.so13_basis()]
check('lambda-half adapted inertia is six positive four negative',
      sum(D[i][i]>0 for i in range(10))==6 and sum(D[i][i]<0 for i in range(10))==4)
check('trace is negative and fixed by endogenous Lorentz',
      D[9][9]==-4 and all(A[i][9]==0 for A in delta for i in range(10)))
check('all induced Lorentz generators preserve actual vertical form', all(m.preserves(A,D) for A in delta))
check('negative block has norms -2,-2,-2,-4', [D[i][i] for i in range(6,10)]==[-2,-2,-2,-4])
# Exact Q(sqrt2) pairs (K,M) stand for K+sqrt(2) M. In the normal
# coordinates, the orthonormal quaternionic basis has last vector trace/sqrt2.
L = [
 [[0,-1,0,0],[1,0,0,0],[0,0,0,-1],[0,0,1,0]],
 [[0,0,-1,0],[0,0,0,1],[1,0,0,0],[0,-1,0,0]],
 [[0,0,0,-1],[0,0,-1,0],[0,1,0,0],[1,0,0,0]],
]
weak=[]
for l in L:
    K,M=m.zeros(10,10),m.zeros(10,10)
    for i in range(4):
        for j in range(4):
            if i==3 or j==3:
                M[i+6][j+6]=F(l[i][j],2) if i==3 else F(l[i][j])
            else: K[i+6][j+6]=F(l[i][j])
    if args.mutate=='drop-trace-motion': M=m.zeros(10,10)
    weak.append((K,M))
def pairadd(a,b): return add(a[0],b[0]), add(a[1],b[1])
def pairscale(a,c): return scale(a[0],c),scale(a[1],c)
def pairmul(a,b):
    return (add(m.matmul(a[0],b[0]),scale(m.matmul(a[1],b[1]),F(2))),
            add(m.matmul(a[0],b[1]),m.matmul(a[1],b[0])))
def pairbracket(a,b): return pairadd(pairmul(a,b),pairscale(pairmul(b,a),F(-1)))
Pneg=m.zeros(10,10)
for i in range(6,10): Pneg[i][i]=F(1)
Z=m.zeros(10,10)
check('actual weak generators preserve the six-plus-four metric',
      all(m.preserves(K,D) and m.preserves(M,D) for K,M in weak))
check('each weak generator squares to minus negative-plane projector',
      all(pairmul(w,w)==(neg(Pneg),Z) for w in weak))
check('quaternionic weak su2 brackets',
      all(pairbracket(weak[i],weak[j])==pairscale(weak[k],F(2)) for i,j,k in [(0,1,2),(1,2,0),(2,0,1)]))
check('every nonzero displayed weak generator moves the negative trace',
      all(any(M[i][9] for i in range(9)) for K,M in weak))
# C=2 sum_i(ad Boost_i^2-ad Rotation_i^2). Its eigenvalues are
# m(m+2)+n(n+2) on doubled sl2 weights (m,n).
def C(A):
    result=m.zeros(10,10)
    for i,X in enumerate(delta):
        if args.mutate=='drop-boosts' and i<3: continue
        result=add(result,scale(m.bracket(X,m.bracket(X,A)),F(2 if i<3 else -2)))
    return result
def project_U(A):
    return scale(add(add(C(C(A)),scale(C(A),F(-40))),scale(A,F(256))),F(-1,128))
check('separating Casimir extracts exactly trace-moving weak component',
      all(m.is_zero(project_U(K)) and project_U(M)==M for K,M in weak))
seed=weak[0][1]
orbit=independent([seed])
rounds=[len(orbit)]
while orbit:
    nxt=independent(orbit+[m.bracket(X,A) for X in delta for A in orbit])
    rounds.append(len(nxt))
    if len(nxt)==len(orbit): break
    orbit=nxt
check('Lorentz orbit of extracted trace motion spans all nine directions',len(orbit)==9)
trace_stabilizer=independent([m.bracket(A,B) for A,B in combinations(orbit,2)])
check('trace-motion brackets span entire so(6,3) stabilizer',len(trace_stabilizer)==36)
check('all bracket directions fix trace',all(A[i][9]==0 for A in trace_stabilizer for i in range(10)))
check('trace motion plus brackets give all so(6,4)',len(independent(orbit+trace_stabilizer))==45)
# Symbolic representation decomposition independently separates the module.
def character(a,b): return Counter((i,j) for i in range(a,-a-1,-2) for j in range(b,-b-1,-2))
U=character(2,2)
weights=list(U.elements())
wedge=Counter((a[0]+b[0],a[1]+b[1]) for a,b in combinations(weights,2))
expected=Counter()
for a,b in [(2,4),(2,0),(4,2),(0,2)]: expected.update(character(a,b))
check('wedge-square traceless-nine branching has no (2,2)',wedge==expected)
check('Casimir eigenvalues separate nine from trace stabilizer',
      {a*(a+2)+b*(b+2) for a,b in [(2,4),(2,0),(4,2),(0,2)]}=={8,32} and 2*(2*(2+2))==16)
# Moving tensor covariance does not mean fixed-object commutation.
Jcart=add(m.eye(10),scale(Pneg,F(-2)))
check('CONTROL chosen Cartan grading commutes with fixed weak',
      all(m.is_zero(m.bracket(Jcart,K)) and m.is_zero(m.bracket(Jcart,M)) for K,M in weak),'countercontrol')
check('CONTROL same Cartan grading does not commute with endogenous boosts',
      all(not m.is_zero(m.bracket(Jcart,X)) for X in delta[:3]),'countercontrol')
check('CONTROL endogenous Lorentz alone has dimension six',len(independent(delta))==6,'countercontrol')
# Every actual commutator stays inside so(D), giving an upper bound 45.
check('all generated matrices remain metric-skew',
      all(m.preserves(A,D) for A in orbit+trace_stabilizer))
result={'status':'PASS' if all(c['pass'] for c in checks) else 'FAIL',
        'checks':checks,'passed':sum(c['pass'] for c in checks),'total':len(checks),
        'orbit_ranks':rounds,'trace_motion_rank':len(orbit),
        'trace_stabilizer_rank':len(trace_stabilizer),'normal_closure_rank':len(independent(orbit+trace_stabilizer)),
        'claim_ceiling':'Fixed-object common equivariance only; no selected native physical grading, domain or family index.'}
if args.output:
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
for c in checks: print(('PASS' if c['pass'] else 'FAIL')+' '+c['name'])
print(json.dumps({k:v for k,v in result.items() if k!='checks'}))
raise SystemExit(0 if result['status']=='PASS' else 1)
