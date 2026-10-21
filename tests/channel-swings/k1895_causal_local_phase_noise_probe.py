#!/usr/bin/env python3
"""Independent bit-occupation and channel-composition checks, with real fault catches."""
import hashlib,json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def checks(fault=None):
    out={}
    def ck(n,b):out[n]=bool(b)
    cs=[]
    for j in range(4):
        a=s.zeros(16)
        for n in range(16):
            bits=[(n>>(3-k))&1 for k in range(4)]
            if bits[j]:a[n-(1<<(3-j)),n]=(-1)**sum(bits[:j])
        cs.append(a)
    occupations=[((n>>2)&1)+(n&1) for n in range(16)]
    phases=[s.I**n for n in occupations]
    if fault=='nonunitary':phases[0]=2
    V=s.diag(*phases)
    K=lambda x:(V*x*V.H+V.H*x*V)/2-(0 if fault=='missing_loss' else 1)*x
    ck('unital',K(s.eye(16))==s.zeros(16))
    A=cs[0].H*cs[1];B=cs[2].H*cs[3]
    if fault=='nonlocal_hop':A=cs[0].H*cs[2]
    ck('even_observable_decay',K(A)==-A)
    ck('relative_pair_coherence_fixed',K(A*B.H)==s.zeros(16))
    q,r=s.symbols('q r',real=True)
    def weights(q):return [(1+q)**2/4,(1-q*q)/4,(1-q)**2/4,(1-q*q)/4]
    for j in range(4):
        convolution=sum(weights(q)[k]*weights(r)[(j-k)%4] for k in range(4))
        ck('semigroup_convolution_'+str(j),s.expand(convolution-weights(q*r)[j])==0)
    for i in range(16):
        for j in range(16):
            exponent=occupations[i]-occupations[j]
            multiplier=sum(weights(q)[k]*s.I**(k*exponent) for k in range(4))
            expected=[1,q,q*q,q][exponent%4]
            ck(f'matrix_unit_{i}_{j}',s.simplify(multiplier-expected)==0)
    d=json.loads((ROOT/'lab/process/k1895-causal-local-phase-noise.json').read_text())
    if fault=='report':d['causal_speed']='1'
    ck('report_speed',d['causal_speed']=='1/24')
    if fault=='pin':d['inputs'][next(iter(d['inputs']))]='wrong'
    for p,h in d['inputs'].items():ck('pin_'+p,hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h)
    return out
if __name__=='__main__':
    base=checks();assert all(base.values()),'FAIL baseline '+str([k for k,v in base.items() if not v])
    print('PASS baseline',len(base)-4,'exact finite/channel checks; 1 report + 3 pins')
    for f in ['nonunitary','missing_loss','nonlocal_hop','report','pin']:
        bad=[k for k,v in checks(f).items() if not v]
        assert bad,'FAIL mutant survived '+f
        print('CAUGHT',f,'FAIL',bad[0])
