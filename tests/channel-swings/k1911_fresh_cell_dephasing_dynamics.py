"""Exact finite identities for K1911; uniform process claims are proved in the note."""
from pathlib import Path
import argparse
import hashlib
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[2]
N = 0

def check(ok, label):
    global N
    assert bool(ok), label
    N += 1

def equal(a, b, label):
    check(s.simplify(s.expand_complex(a-b)) == 0, label)

def matrix(a, b, label):
    check((a-b).applyfunc(s.expand_complex).applyfunc(s.simplify) == s.zeros(*a.shape), label)

def calculate(phase=-1, event_scale=1):
    global N
    N = 0
    a = 1/s.sqrt(2)
    E = s.Matrix([[1, 0, a, a], [0, 1, a, phase*s.I*a]])
    C = E.T*E.conjugate()
    equal(C[2,3], (1+s.I)/2, 'target complex orientation')
    h = s.symbols('h', positive=True)
    # Rational parameter h=sin(theta)^2, use positive c,s for exact unitaries.
    u, v = s.Rational(3,5), s.Rational(4,5)
    vac = s.Matrix([1,0,0]); I = s.eye(3)
    F = []
    for j in range(4):
        e = s.Matrix([0, E[0,j], E[1,j]])
        K = s.I*(e*vac.T-vac*e.conjugate().T)
        matrix(K.conjugate().T, K, 'Hermitian cell generator')
        matrix(K**3, K, 'minimal polynomial gives exponential')
        U = I+(u-1)*(K**2)-s.I*v*K
        matrix(U.conjugate().T*U, I, 'exact cell unitary')
        f = u*vac+event_scale*v*e
        matrix(U*vac, f, 'actual rotated vacuum')
        F.append(f)
        equal((f.conjugate().T*s.diag(0,1,1)*f)[0], v*v, 'cell excitation')
    FF = s.Matrix.hstack(*F)
    matrix(FF.T*FF.conjugate(), u*u*s.ones(4)+v*v*C, 'cell Gram channel')
    D = (1-h)*s.ones(4)+h*C
    equal(D[:3,:3].det(), h*h*(1-h)*(3-2*s.sqrt(2)), 'strict rank-three minor')
    equal(D.det(), 0, 'rank upper bound')
    check(C.rank() == 2, 'event endpoint rank')
    p = [s.Rational(1,4)]*4
    mean = E*s.Matrix(p)
    equal(1-(mean.conjugate().T*mean)[0], (11-3*s.sqrt(2))/16, 'minimum energy flux slope')
    # Binomial vs Poisson: exact coefficient identities, independent of a norm claim.
    z = s.symbols('z')
    for n in [1,2,3,5]:
        equal(sum(s.binomial(n,k)*(1-h)**(n-k)*h**k*z**k for k in range(n+1)), (1-h+h*z)**n, 'binomial channel composition')
    x = s.symbols('x', real=True)
    equal((s.exp(-x)-1+x)+x*(1-s.exp(-x))+(1-s.exp(-x)*(1+x)), 2*x*(1-s.exp(-x)), 'one-step l1 distance')
    margin = s.Rational(1,176000)-s.Rational(1,110)**2/15
    equal(margin, s.Rational(1,5808000), 'finite fifteen-cell separation')
    check(margin > 0, 'positive certified margin')
    return {'cell_dimension':3, 'step_correlation':'(1-h)*J+h*C', 'diamond_error':'2*t*h',
            'fifteen_cell_h':'1/1650', 'fifteen_cell_trace_distance_margin':str(margin),
            'simple_energy_flux_over_gap':1, 'uniform_optimized_energy_flux_over_gap':'(11-3*sqrt(2))/16',
            'control_scaling':'h^(-1/2); prefactor not optimized', 'math_checks':N}

def pins():
    return {str(p):hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in [
        'explorations/conditional-build/k1909-poisson-phase-classification-2026-10-21.md',
        'explorations/conditional-build/k1910-minimal-dephasing-bath-energy-2026-10-21.md']}

if __name__ == '__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--write-report',action='store_true');args=parser.parse_args()
    report=calculate();report['dependency_sha256']=pins()
    if args.write_report:
        (ROOT/'lab/process/k1911-fresh-cell-dephasing-dynamics.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report))
