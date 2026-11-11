"""Native dyadic K95 and exact symbolic connection controls; no floating tolerance.
Universal completeness is a written proof using the previously proved stabilizer.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('VECLIB_MAXIMUM_THREADS','1')
from pathlib import Path
import sys,json,hashlib
import numpy as np
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tests/channel-swings'))
from actual_sym2_c14_orbit_probe import native_gammas
NOTE='explorations/conditional-build/x-p1-p2-projector-connection-2026-11-11.md'
REPORT='lab/process/x-p1-p2-projector-connection.json'
checks=[]
def ck(name,value,kind='exact_supporting'):
    assert bool(value),name
    checks.append(dict(name=name,kind=kind))
def eq(a,b):return np.array_equal(a,b)
def run():
    checks.clear();gs,eta=native_gammas();I=np.eye(128,dtype=complex)
    def prod(ids):
        a=I.copy()
        for i in ids:a=a@gs[i]
        return a
    K=prod(range(9));J=prod([1,3,5,7,10,12]);O=prod(range(14));Z=0*I
    ck('native Omega square and K-skew',eq(O@O,I) and eq(O.conj().T@K+K@O,Z))
    ck('native Omega quaternionic-linear',eq(O@J,J@O.conj()))
    ck('all14 odd connection defects nonzero',all(eq(O@g-g@O,2*O@g) and not eq(O@g,Z) for g in gs))
    ck('all196 even projector blocks parallel',all(eq(O@(a@b),(a@b)@O) for a in gs for b in gs))
    ck('opposite-charge quotient makes all14 Gamma arrows parallel',all(eq(-O@g-g@O,Z) for g in gs))
    ck('opposite-charge inclusion makes all14 j arrows parallel',all(eq(O@g+g@O,Z) for g in gs))
    ck('same-charge Gamma fails despite parallel projector',any(not eq(O@g-g@O,Z) for g in gs),'exact_contrary')
    ck('opposite charges fail insertion',not eq(O-(-O),Z),'exact_contrary')
    ck('central real identity fails K compatibility',not eq(I.conj().T@K+K@I,Z),'exact_contrary')
    ck('central imaginary identity fails J compatibility',not eq(1j*I@J,J@(1j*I).conj()),'exact_contrary')
    C0=gs[0]@J
    ck('reflected C0 anticommutes volume antilinearly',eq(C0@O.conj(),-O@C0))
    ck('reflected C0 squared minus1',eq(C0@C0.conj(),-I))
    ck('parallel inert J need not imply parallel reflected C0',eq(O@J-J@O.conj(),Z) and not eq(O@C0-C0@O.conj(),Z),'exact_contrary')
    # Exact two-chiral-block calculation encodes the full native Omega algebra.
    x,y=s.symbols('x y',real=True);a=s.Function('a',positive=True)(x)
    ob=s.diag(1,-1);kb=s.Matrix([[0,1],[1,0]]);gb=s.diag(a,1/a)
    ck('residual gauge connection law',s.simplify(s.diff(gb,x)*gb.inv()-s.diff(a,x)/a*ob)==s.zeros(2))
    f=x*y;t=s.Function('t')(x);b=s.Function('b')(x)
    ck('exact beta=df has zero curvature',s.diff(s.diff(f,y),x)-s.diff(s.diff(f,x),y)==0)
    ck('nonclosed beta=xdy retains curvature',s.diff(x,x)-s.diff(0,y)==1,'exact_contrary')
    cb=s.Matrix([[0,1],[-1,0]]);ct=s.diag(s.exp(t),s.exp(-t))*cb
    ck('all coflip calibrations preserve square',s.simplify(ct*ct)==-s.eye(2))
    ck('coflip parallel differential dt+2beta',s.simplify(s.diff(ct,x)+b*(ob*ct-ct*ob)-(s.diff(t,x)+2*b)*ob*ct)==s.zeros(2))
    gm=s.diag(s.exp(2*t),s.exp(-2*t))*s.Matrix([[0,1],[1,0]])
    ck('Clifford arrow parallel differential2(dt+beta)',s.simplify(s.diff(gm,x)+b*(ob*gm-gm*ob)-2*(s.diff(t,x)+b)*ob*gm)==s.zeros(2))
    ck('nonzero exact connection original arrows nonparallel',s.simplify((s.diff(gm,x)+b*(ob*gm-gm*ob)).subs({t:0,s.diff(t,x):0,b:1}))!=s.zeros(2),'exact_contrary')
    # Period2pi circle beta=dtheta: exact nontrivial real holonomy.
    period=s.integrate(s.Integer(1),(x,0,2*s.pi))
    ck('circle closed form has nonzero period',period==2*s.pi)
    ck('circle real holonomy is not periodic-unitary ambiguity',s.exp(-period)!=1,'exact_contrary')
    ck('factor-two calibration has same zero-period condition',2*period!=0)
    deps=[NOTE,'tests/channel-swings/actual_sym2_c14_orbit_probe.py','explorations/conditional-build/x-p1-p2-real-clifford-transfer-2026-11-11.md',str(Path(__file__).relative_to(ROOT))]
    return dict(schema_version='1.0',artifact='x-p1-p2-projector-connection',checks=checks,hashes={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},proof_scope='Universal connection/global classification in companion proof; exact finite controls and symbolic identities only, no Lean or physical certification.',claim_effect='none')
if __name__=='__main__':
    data=run();p=ROOT/REPORT
    if '--write' in sys.argv:p.write_text(json.dumps(data,indent=2)+'\n')
    else:assert json.loads(p.read_text())==data
    print(json.dumps({k:sum(x['kind']==k for x in checks) for k in sorted({x['kind'] for x in checks})}))
