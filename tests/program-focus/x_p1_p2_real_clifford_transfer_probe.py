"""Exact dyadic controls on RB3's 128-complex-dimensional K95 fixture.

No tolerance: every matrix entry and arithmetic result is a small Gaussian
integer or dyadic rational, exactly representable in binary64. Each dot product
has only128 terms. Universal classification is proved in the companion note.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('VECLIB_MAXIMUM_THREADS','1')
from pathlib import Path
import sys,json
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'channel-swings'))
from actual_sym2_c14_orbit_probe import native_gammas
checks=[]; contrary=[]
def check(name,value,negative=False):
    assert bool(value),name
    (contrary if negative else checks).append(name)
def eq(a,b):return np.array_equal(a,b)
def run():
    checks.clear();contrary.clear()
    gs,eta=native_gammas();I=np.eye(128,dtype=complex);Z=np.zeros_like(I)
    def prod(ids):
        a=I.copy()
        for i in ids:a=a@gs[i]
        return a
    K=prod(range(9));J=prod([1,3,5,7,10,12]);O=prod(range(14))
    check('all196 Clifford anticommutators',all(eq(gs[i]@gs[j]+gs[j]@gs[i],2*eta[i]*I if i==j else Z) for i in range(14) for j in range(14)))
    check('K Hermitian involution with balanced64plus64',eq(K.conj().T,K) and eq(K@K,I) and np.trace(K)==0)
    check('J quaternionic and unitary',eq(J@J.conj(),-I) and eq(J.conj().T@J,I))
    check('J commutes all Clifford generators antilinearly',all(eq(J@g.conj(),g@J) for g in gs))
    check('gamma K selfadjoints',all(eq(g.conj().T@K,K@g) for g in gs))
    check('volume involution and Hermitian',eq(O@O,I) and eq(O.conj().T,O))
    check('volume K skew and quaternionic linear',eq(O.conj().T@K,-K@O) and eq(O@J,J@O.conj()))
    g=(5*I+3*O)/4;h=(5*I-3*O)/4
    check('actual gauge inverse',eq(g@h,I))
    check('actual gauge K unitary',eq(g.conj().T@K@g,K))
    check('actual gauge quaternionic linear',eq(g@J,J@g.conj()))
    check('actual gauge preserves volume',eq(g@O,O@g))
    check('all14 quotient arrows use inverse action',all(eq(x@g,h@x) for x in gs))
    check('same target action fails',any(not eq(x@g,g@x) for x in gs),True)
    moved=[g@x@h for x in gs]
    check('all14 moved arrows equal g squared times old',all(eq(y,g@g@x) for x,y in zip(gs,moved)))
    check('all14 moved inclusion blocks use inverse squared',all(eq(y,x@h@h) for x,y in zip(gs,moved)))
    check('all196 projector numerator blocks unchanged',all(eq(moved[i]@moved[j],gs[i]@gs[j]) for i in range(14) for j in range(14)))
    check('all14 plane motions have grade13 component',all(eq(y,(17*x+15*O@x)/8) for x,y in zip(gs,moved)))
    check('grade13 directions trace orthogonal to original plane',all(np.trace(gs[j].conj().T@O@gs[i])==0 for i in range(14) for j in range(14)))
    check('plane motion is nonzero despite fixed projector',all(not eq(x,y) for x,y in zip(gs,moved)),True)
    check('inert-vector J square rejects hyperbolic ratio',eq((g@J)@(g@J).conj(),-g@g) and not eq(g@g,I),True)
    C0=gs[0]@J;C1=C0@g.conj();rs=[1]+[-1]*13
    check('reflected coflips share square minus one',eq(C0@C0.conj(),-I) and eq(C1@C1.conj(),-I))
    check('reflected coflips K antiunitary not sign reversing',eq(C0.conj().T@K@C0,K.conj()) and eq(C1.conj().T@K@C1,K.conj()))
    check('C0 reflected diagram equation all14',all(eq(r*x@C0,C0@x.conj()) for r,x in zip(rs,gs)))
    H1=C0@h.conj()
    check('C1 reflected kernel quotient all14',all(eq(r*x@C1,H1@x.conj()) for r,x in zip(rs,gs)))
    check('C1 same mirror arrow fails all14',all(not eq(r*x@C1,C1@x.conj()) for r,x in zip(rs,gs)),True)
    H0=eta[0]*gs[0]@C0@gs[0].conj();H1=eta[1]*gs[1]@C0@gs[1].conj()
    check('omitting reflection gives incompatible quotient maps',eq(H0,C0) and eq(H1,-C0) and not eq(H0,H1),True)
    rotor=gs[0]@gs[1];ri=-rotor
    check('Spin rotor is native group element',eq(rotor@ri,I) and eq(rotor.conj().T@K@rotor,K) and eq(rotor@J,J@rotor.conj()))
    rotated=[rotor@x@ri for x in gs]
    check('Spin rotor preserves original Clifford plane',all(eq(y,(-1 if i<2 else 1)*gs[i]) for i,y in enumerate(rotated)))
    check('plane preservation need not fix vector-slot projector',not eq(rotated[0]@rotated[2],gs[0]@gs[2]),True)
    bad=2*I
    check('commutant alone does not imply K unitarity',all(eq(x@bad,bad@x) for x in gs) and not eq(bad.conj().T@K@bad,K),True)
    return dict(schema_version='1.0',artifact='x-p1-p2-real-clifford-transfer',supporting_checks=checks,contrary_controls=contrary,claim_effect='none',proof_scope='Exact dyadic128-complex native K95 controls; universal real-form classification is a separate written proof, not Lean or physical certification.')
if __name__=='__main__':
    data=run();p=Path(__file__).resolve().parents[2]/'lab/process/x-p1-p2-real-clifford-transfer.json'
    if '--write' in sys.argv:p.write_text(json.dumps(data,indent=2)+'\n')
    else:assert json.loads(p.read_text())==data
    print(f"{len(checks)} supporting checks; {len(contrary)} contrary controls")
