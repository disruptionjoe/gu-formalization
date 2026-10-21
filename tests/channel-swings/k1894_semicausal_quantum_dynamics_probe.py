#!/usr/bin/env python3
"""Independent Schrödinger superoperator/partial-trace audit of cascade and faults."""
import copy,hashlib,json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2];REPORT=ROOT/'lab/process/k1894-semicausal-quantum-dynamics.json'
def decode(d):
    M=s.zeros(d['rows'],d['columns'])
    for i,j,v in d['entries']:M[i,j]=s.sympify(v)
    return M
def ptr(r):return s.Matrix(2,2,lambda i,j:r[2*i,2*j]+r[2*i+1,2*j+1])
def D(H,L,r):return -s.I*(H*r-r*H)+L*r*L.H-(L.H*L*r+r*L.H*L)/2
def z(M):return all(s.simplify(x)==0 for x in M)
def check(d,fault=None):
    count=0
    def ck(name,b):
        nonlocal count
        if not b:raise AssertionError('FAIL '+name)
        count+=1
    H=decode(d['cascade']['H']);L=decode(d['cascade']['L']);lo=s.Matrix([[0,1],[0,0]]);I=s.eye(2)
    if fault=='reverse_H':H=-H
    if fault=='omit_H':H=s.zeros(4)
    if fault=='wrong_jump':L=s.kronecker_product(I,lo)
    ck('Hermitian',H.H==H)
    for i in range(4):
        for j in range(4):
            r=s.zeros(4);r[i,j]=1
            ck(f'all_state_dual_{i}_{j}',z(ptr(D(H,L,r))-D(s.zeros(2),lo,ptr(r))))
            ck(f'trace_preservation_{i}_{j}',s.trace(D(H,L,r))==0)
    # Correlated Bell density is also covered, but is an explicit operational control.
    v=s.Matrix([1,0,0,1]);rho=v*v.H/2
    ck('correlated_state',ptr(D(H,L,rho))==D(s.zeros(2),lo,ptr(rho)))
    # Exact derivative recursion: hidden excitation transfer first appears at order t².
    r=s.zeros(4);r[2,2]=1;d1=D(H,L,r);d2=D(H,L,d1)
    ck('forward_transfer_second_order',d1[1,1]+d1[3,3]==0 and d2[1,1]+d2[3,3]==2)
    ck('visible_first_order',d1[2,2]+d1[3,3]==-1)
    # No-signalling to visible holds for all hidden states, not only ground or stationarity.
    for j in [0,1]:
        r=s.zeros(4);r[j,j]=1;ck('no_reverse_signal_'+str(j),ptr(D(H,L,r))==s.zeros(2))
    t=s.symbols('t',positive=True);rho=s.zeros(4);rho[0,0]=1-(1+t*t)*s.exp(-t);rho[1,1]=t*t*s.exp(-t);rho[2,2]=s.exp(-t);rho[1,2]=rho[2,1]=-t*s.exp(-t)
    ck('ODE_independent',z(s.diff(rho,t)-D(H,L,rho)))
    pt=s.Matrix(4,4,lambda i,j:rho[2*(i//2)+j%2,2*(j//2)+i%2])
    ck('NPT_minor',s.simplify(pt.extract([0,3],[0,3]).det())==-t*t*s.exp(-2*t))
    ck('reported_population',s.simplify(s.sympify(d['cascade']['hidden_excitation'],locals={'t':t})-rho[1,1])==0)
    # Build encoded CAR bilinears from bit occupations rather than producer kron.
    def a(k):
        m=s.zeros(16)
        for j in range(16):
            bits=[(j>>(3-i))&1 for i in range(4)]
            if bits[k]:m[j^(1<<(3-k)),j]=(-1)**sum(bits[:k])
        return m
    cs=[a(k) for k in range(4)];A=cs[0].H*cs[1];B=cs[2].H*cs[3];Lf=A+B;Hf=(B.H*A-A.H*B)/(2*s.I);U=decode(d['fermionic_encoding'])
    if fault=='odd_instead_of_even':Lf=cs[0]+cs[2]
    ck('encoding_isometry',U.H*U==s.eye(4));ck('fermion_parity_correct',Lf*U==U*L and Lf.H*U==U*L.H and Hf*U==U*H)
    nf=cs[0].H*cs[0];ng=cs[1].H*cs[1];jump=cs[0].H*cs[1]
    if fault=='reverse_spatial_jump':jump=jump.H
    rate=jump.H*nf*jump-(jump.H*jump*nf+nf*jump.H*jump)/2
    ck('remote_pair_rate',rate==ng*(s.eye(16)-nf) and rate[0,0]==0 and rate[6,6]==1)
    # Carré identity independent on a nonnormal X, with hidden/visible cross terms.
    xx=s.Matrix([[0,1],[0,1]]);X=s.kronecker_product(xx,I)
    def G(Y):return s.I*(H*Y-Y*H)+L.H*Y*L-(L.H*L*Y+Y*L.H*L)/2
    c=L*X-X*L;ck('positive_dissipation_identity',z(G(X.H*X)-G(X.H)*X-X.H*G(X)-c.H*c))
    for p,h in d['inputs'].items():ck('input_pin',hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h)
    return count
if __name__=='__main__':
    d=json.loads(REPORT.read_text());n=check(d);print('PASS K1894 independent',n-3,'exact algebra/ODE checks; 1 population report; 2 pins')
    for f in ['reverse_H','omit_H','wrong_jump','odd_instead_of_even','reverse_spatial_jump','population_report','input_pin']:
        x=copy.deepcopy(d)
        if f=='population_report':x['cascade']['hidden_excitation']='t*exp(-t)'
        if f=='input_pin':x['inputs'][next(iter(x['inputs']))]='0'*64
        try:check(x,f)
        except AssertionError as e:
            assert str(e).startswith('FAIL ');print('CAUGHT',f,str(e))
        else:raise AssertionError('FAIL undetected '+f)
    print('PASS mutations: 5 mathematical generator/encoding/locality faults; 1 report; 1 pin')
