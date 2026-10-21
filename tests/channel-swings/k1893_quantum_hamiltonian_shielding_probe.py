#!/usr/bin/env python3
"""Independent occupation-basis and matrix-unit check, with actual faulty interactions."""
import copy,hashlib,itertools,json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2];REPORT=ROOT/'lab/process/k1893-quantum-hamiltonian-shielding.json'
def annihilator(k,n=4):
    M=s.zeros(2**n)
    for j in range(2**n):
        bits=[(j>>(n-1-i))&1 for i in range(n)]
        if bits[k]:M[j^(1<<(n-1-k)),j]=(-1)**sum(bits[:k])
    return M
def mat(d):
    M=s.zeros(d['rows'],d['columns'])
    for i,j,v in d['entries']:M[i,j]=s.sympify(v)
    return M
def check(d,fault=None):
    count=0
    def ck(name,b):
        nonlocal count
        if not b:raise AssertionError('FAIL '+name)
        count+=1
    a=[annihilator(k) for k in range(4)];N=[x.H*x for x in a];I=s.eye(16);pv=(I-2*N[0])*(I-2*N[1]);pt=pv*(I-2*N[2])*(I-2*N[3])
    W=mat(d['witnesses']['hidden_quartic']);C=mat(d['witnesses']['parity_controlled_quartic']);leak=mat(d['witnesses']['density_leak_commutator'])
    if fault=='visible_contamination':W+=N[0]
    if fault=='number_for_parity':C=N[0]*N[2]*N[3]
    if fault=='erase_leak':leak=s.zeros(16)
    ck('quartic_actual',W==N[2]*N[3]);ck('parity_actual',C==pv*N[2]*N[3])
    ck('leak_actual',leak==(N[0]*N[2])*(a[0].H*a[1])-(a[0].H*a[1])*(N[0]*N[2]) and leak!=s.zeros(16))
    units=[];even=[]
    for i in range(4):
        for j in range(4):
            E=s.zeros(4);E[i,j]=1;M=s.kronecker_product(E,s.eye(4));units.append(M)
            if i.bit_count()%2==j.bit_count()%2:even.append(M)
            ck(f'quartic_full_{i}_{j}',W*M==M*W)
            if i.bit_count()%2==j.bit_count()%2:ck(f'parity_even_{i}_{j}',C*M==M*C)
    ck('parity_breaks_full',any(C*x!=x*C for x in units))
    P=[s.eye(2),s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)];dims=dict(full=0,even=0,full_total_even=0,even_total_even=0)
    for inds in itertools.product(range(4),repeat=4):
        M=s.kronecker_product(*(P[k] for k in inds));f=all(M*x==x*M for x in units);e=all(M*x==x*M for x in even);p=M*pt==pt*M
        dims['full']+=f;dims['even']+=e;dims['full_total_even']+=f and p;dims['even_total_even']+=e and p
    ck('report_dimensions',d['dimensions']==dims)
    ck('quartic_degree',s.trace(W)==4 and W*W==W and W*a[2]-a[2]*W==-a[2]*N[3])
    for p,h in d['inputs'].items():ck('input_pin',hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h)
    return count
if __name__=='__main__':
    d=json.loads(REPORT.read_text());n=check(d);print('PASS K1893 independent',n-2,'finite algebra checks; 1 dimensions report and 1 pin')
    caught=[]
    for f in ['visible_contamination','number_for_parity','erase_leak','dimension_report','input_pin']:
        x=copy.deepcopy(d)
        if f=='dimension_report':x['dimensions']['even']=16
        if f=='input_pin':x['inputs'][next(iter(x['inputs']))]='0'*64
        try:check(x,f)
        except AssertionError as e:
            assert str(e).startswith('FAIL '),str(e);caught.append(f);print('CAUGHT',f,str(e))
        else:raise AssertionError('FAIL undetected '+f)
    print('PASS mutations: 3 mathematical interaction/reference faults; 1 report; 1 pin')
