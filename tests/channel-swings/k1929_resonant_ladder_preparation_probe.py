"""Separate exhaustive graph oracle plus real input/report/pin mutations."""
from pathlib import Path
from fractions import Fraction as F
import importlib.util,json,hashlib,itertools
ROOT=Path(__file__).resolve().parents[2]
P=Path(__file__).with_name('k1929_resonant_ladder_preparation.py')
spec=importlib.util.spec_from_file_location('producer',P);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

def independent():
    count=0
    for d in range(3,11):
        for t in (F(1,2),F(2,3)):
            best=F(0);best_bits=None
            for bits in itertools.product((0,1),repeat=d):
                if bits[0] or bits[-1] or any(bits[j]+bits[j+1]>1 for j in range(d-1)):continue
                weight=sum(t**j for j in range(d) if bits[j])
                if weight>best:best=weight;best_bits=bits
            expected=tuple(int(j%2==1 and j<d-1) for j in range(d))
            assert best_bits==expected,'exhaustive unique maximum';count+=1
            assert best/sum(t**j for j in range(d))==m.mass_formula(d,t),'independent enumeration/formula';count+=1
    # Exact rational coherent catalyst: its diagonal support remains the same.
    # sigma on levels1,3 = [[4/5,2/5],[2/5,1/5]] is pure and positive.
    assert F(4,5)*F(1,5)-F(2,5)**2==0;count+=1
    # Each bath sector singles out a different A energy inside a fixed shell.
    assert m.feasible([1,3],list(map(F,range(5))));count+=1
    return count

def verify_report(data):
    assert data==m.report(),'report equality/pin'

if __name__=='__main__':
    checks=independent();clean=m.calculate();data=json.loads((ROOT/'lab/process/k1929-resonant-ladder-preparation.json').read_text());verify_report(data)
    print('BASELINE PASS',checks,'independent exact checks')
    caught=[]
    for fault in ('endpoint','weight'):
        try:m.calculate(fault)
        except AssertionError as e:print('DETECTED mathematical input',fault,str(e));caught.append(fault)
        else:raise AssertionError('missed '+fault)
    for field in ('example_mass','script_sha256'):
        bad=dict(data);bad[field]='corrupted'
        try:verify_report(bad)
        except AssertionError as e:print('DETECTED reporting/pin',field,str(e));caught.append(field)
        else:raise AssertionError('missed '+field)
    assert len(caught)==4
    print('PASS',checks,'independent exact checks;2math/1report/1pin faults')
