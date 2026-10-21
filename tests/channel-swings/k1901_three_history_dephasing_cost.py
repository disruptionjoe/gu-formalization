"""Exact finite controls; analytic scope is in the linked research note."""
from pathlib import Path
import argparse, hashlib, json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
COUNT=0
def check(ok, name):
    global COUNT
    assert bool(ok), name
    COUNT+=1
def eq(a,b,name): check(s.simplify(a-b)==0,name)
def mat(a,b,name): check((a-b).applyfunc(s.simplify)==s.zeros(*a.shape),name)
def pin(path): return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()

def calculate(step=2):
    global COUNT
    COUNT=0
    w=(-1+s.I*s.sqrt(3))/2
    F=s.Matrix([[1,1,1],[1,w,w**2],[1,w**2,w**4]])
    mat(F.conjugate().T*F,3*s.eye(3),'equilateral Fourier orthogonality')
    for j in range(3): eq(sum(abs(F[j,k])**2 for k in range(3))/3,1,'row probability')
    alpha=s.symbols('alpha',real=True)
    phases=[alpha,alpha+step*s.pi/3,alpha-step*s.pi/3]
    variance=s.expand(sum(x*x for x in phases)/3)
    eq(variance,alpha**2+8*s.pi**2/27,'wrapped cell exact objective')
    eq(s.diff(variance,alpha,2),2,'strict minimizer')
    histories=s.Matrix([[0,0,0],[0,2*s.pi/3,4*s.pi/3],[0,-2*s.pi/3,-4*s.pi/3]])
    for j in [0,1]: eq(sum((histories[h,j+1]-histories[h,j])**2 for h in range(3))/3,8*s.pi**2/27,'adjacent cost')
    eq((8*s.pi**2/27)/(s.pi**2/4),s.Rational(32,27),'history penalty')
    c,g1,g2=s.symbols('c g1 g2',positive=True)
    energy=c/(2*s.pi)*s.Rational(8,27)*s.pi**2*(1/g1+1/g2)
    eq(energy,4*c*s.pi/27*(1/g1+1/g2),'energy normalization')
    return {'phase_second_moment':'8*pi**2/27','energy_factor':'4*pi/27','unrestricted_ratio':'32/27','probabilities':['1/3']*3,'math_checks':COUNT}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write-report',action='store_true');args=ap.parse_args()
    result=calculate();result['dependency_sha256']=pin('explorations/conditional-build/k1900-sharp-phase-noise-cost-2026-10-21.md')
    if args.write_report: (ROOT/'lab/process/k1901-three-history-dephasing-cost.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
