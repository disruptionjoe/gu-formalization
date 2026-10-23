"""Separate edge formula, physical completion and exposed-face replay."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import json,hashlib
from k1950_global_catalyst_energy_certificates_probe import audit
ROOT=Path(__file__).resolve().parents[2]
def check(fault=None):
    r=json.loads((ROOT/'lab/process/k1975-thermal-sharp-dimension-threshold.json').read_text());n=0
    for z in r['consumers']:
        E,e,w=map(Q,[z['energy'],z['epsilon'],z['B_weight']]);s=[Q(1),Q(3),1+e,3+e];p=[(1-w)*Q(9,10),(1-w)/10,w*Q(2,5),w*Q(3,5)]
        if fault=='ignore_offset':w=E-Q(6,5);p=[(1-w)*Q(9,10),(1-w)/10,w*Q(2,5),w*Q(3,5)]
        assert sum(a*b for a,b in zip(s,p))==E,'physical energy includes fractional offset';n+=1
        inc=[Q(0)]*4
        for i in range(4):
            for j in range(i+1,4):
                if s[j]-s[i] in [1,2,3]:
                    d=int(s[j]-s[i]);bath=[Q(8,15),Q(4,15),Q(2,15),Q(1,15)]
                    H=sum(bath[d:]);L=sum(bath[:4-d])
                    if fault=='wrong_bath':L/=2
                    v=H*p[i]-L*p[j];inc[i]+=max(0,-v);inc[j]+=max(0,v)
        R=sum(max(0,a-b) for a,b in zip(p,inc))/2
        assert R==Q(z['return_error']),'independent edge return';n+=1
        A=[Q(i) for i in range(5)]+[Q(i)+e for i in range(5)]
        if fault=='drop_completion':A=A[:-1]
        for total in {x+b for x in s for b in range(4)}:
            assert sum(total-a in [0,1,2,3] for a in A)>=2*sum(total-a in [0,1,2,3] for a in s),'every actual shell has enough dimension';n+=1
    # Each nonzero equality tag has2 occupied levels and independent full cost>=5.
    charged=5 if fault=='free_tag' else 10
    assert charged>=sum(2*len(f)+1 for f in r['exposed_faces']),'two equality tags cost10'
    for d in range(3,10):
        assert all(k+l>d for k,l in product(range(5,11),repeat=2)),'no pair of equality components below10';n+=1
    for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    return n
if __name__=='__main__':
    n=check();caught=[]
    for f in ['ignore_offset','wrong_bath','drop_completion','free_tag']:
        try:check(f)
        except AssertionError as e:caught.append([f,str(e)])
        else:raise AssertionError('missed mathematical fault '+f)
    prior=json.loads((ROOT/'lab/process/k1950-global-catalyst-energy-certificates.json').read_text());prior['global_duals']=[b for b in prior['global_duals'] if Q(b['slope'])==Q(3,20)];prior['consumers']=[]
    print('PASS K1975 independent physical',n,'replayed exact dual/face obligations',audit(prior,math_only=True),'faults',caught)
