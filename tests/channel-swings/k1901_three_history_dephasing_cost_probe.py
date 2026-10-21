"""Separate exact derivation and hostile probes; no producer import."""
from pathlib import Path
import copy,hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
COUNT=0
def check(ok,name):
    global COUNT
    assert bool(ok),name
    COUNT+=1
def eq(a,b,name):check(s.simplify(a-b)==0,name)
def mat(a,b,name):check((a-b).applyfunc(s.simplify)==s.zeros(*a.shape),name)
def reject(fn,label):
    try:fn()
    except AssertionError:return label
    raise AssertionError('fault survived: '+label)
def pinned(d):
    expected=hashlib.sha256((ROOT/'explorations/conditional-build/k1900-sharp-phase-noise-cost-2026-10-21.md').read_bytes()).hexdigest()
    check(d['dependency_sha256']==expected,'dependency pin')

def algebra(weight=s.Rational(1,3),rotation=2):
    # Independent roots from quadratic, not the producer matrix.
    w=(-1+s.I*s.sqrt(3))/2
    angles=s.Matrix([0,rotation*s.pi/3,-rotation*s.pi/3])
    eq(weight*sum(angles[j]**2 for j in range(3)),8*s.pi**2/27,'root triple cost')
    eq(3*weight,1,'square-unitary row probability')
    eq(1+w+w**2,0,'equilateral closure')
    eq(s.re(w),-s.Rational(1,2),'unit triangle necessity')
    alpha=s.symbols('alpha',real=True)
    for shift in [-2*s.pi/3,0,2*s.pi/3]:
        # Same principal cell after cyclic relabeling; direct quadratic minimum.
        q=sum((alpha+z)**2 for z in [0,2*s.pi/3,-2*s.pi/3])/3
        eq(s.diff(q,alpha),2*alpha,'cell minimizer derivative')
    for j in [1,2]:eq(s.expand_complex((1+w**j+w**(2*j))/3),0,'nonadjacent coherence')
    eq(s.Rational(8,27)-s.Rational(1,4),s.Rational(5,108),'strict absolute cost gap')
def reporting(d):
    eq(s.sympify(d['phase_second_moment']),8*s.pi**2/27,'report variance')
    eq(s.sympify(d['unrestricted_ratio']),s.Rational(32,27),'report ratio')
    eq(s.sympify(d['energy_factor']),4*s.pi/27,'report energy')
if __name__=='__main__':
    d=json.loads((ROOT/'lab/process/k1901-three-history-dephasing-cost.json').read_text());algebra();n=COUNT;reporting(d);pinned(d)
    faults=[reject(lambda:algebra(weight=s.Rational(1,2)),'unequal probability input'),reject(lambda:algebra(rotation=1),'wrong phase angle')]
    bad=copy.deepcopy(d);bad['unrestricted_ratio']='1';faults.append(reject(lambda:reporting(bad),'report ratio'))
    badpin=copy.deepcopy(d);badpin['dependency_sha256']='0'*64;faults.append(reject(lambda:pinned(badpin),'dependency pin'))
    print(json.dumps({'baseline_math_checks':n,'faults_rejected':faults}))
