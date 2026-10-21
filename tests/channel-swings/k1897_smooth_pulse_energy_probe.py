from pathlib import Path
import sys,json,hashlib,copy
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
PIN='lab/process/k1896-local-phase-vacuum-boundary.json'
REPORT=ROOT/'lab/process/k1897-smooth-pulse-energy.json'
def sha(p): return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def check(b,label):
    if not b: raise AssertionError('[FAIL] '+label)
def eq(a,b,label): check(s.simplify(a-b)==0,label)

def audit(d):
    c=d['coefficients']; ep,em,a=s.symbols('ep em a',positive=True)
    D=s.diag(ep,-em);Q=s.diag(1,-1);A=s.Matrix([[0,a],[a,0]]);E=s.diag(ep,em)
    C=Q*A-A*Q;X=-(E.inv()*C+C*E.inv())/c['normal_form_denominator']
    got=(Q*(A+D*X-X*D)-(A+D*X-X*D)*Q)[0,1]
    expected=-a*(ep-em)**2/(2*ep*em)
    eq(got,expected,'normal-form offdiagonal residual')
    Xexact=s.Matrix([[0,-a/(ep+em)],[a/(ep+em),0]])
    check((A+D*Xexact-Xexact*D).applyfunc(s.simplify)==s.zeros(2),'direct Sylvester cancellation')
    # Direct occupation probabilities, without producer trace construction.
    expected_energy=(s.Rational(4,5)**2)*(2+5)
    eq(s.sympify(c['rational_unitary_energy']),expected_energy,'occupation energy')
    raw_comm_norm=4*expected_energy
    eq(raw_comm_norm*s.sympify(c['commutator_energy_factor']),expected_energy,'weight factor')
    threshold=s.sympify(c['strict_threshold_offset'])
    eq(2+2*s.Rational(1,2)-2*(s.Rational(1,2)+threshold),-1,'radial borderline')
    check(c['energy_iteration_order']>s.Rational(1,2)+threshold,'strict energy order')
    check(c['dimension']==3,'dimension contract')
    eq(s.cos(s.sympify(c['plateau_visibility_phase'])),c['plateau_visibility'],'plateau phase visibility')
    check(d['source_pins'][PIN]==sha(PIN),'dependency pin')
    return 8

def main():
    d=json.loads(REPORT.read_text());n=audit(d)
    faults=[('normal_form_denominator',4),('commutator_energy_factor','1/2'),('energy_iteration_order',2),('rational_unitary_energy','56/25'),('plateau_visibility_phase','pi')]
    for key,val in faults:
        x=copy.deepcopy(d);x['coefficients'][key]=val
        try:audit(x)
        except AssertionError as e: check('[FAIL]' in str(e),'not crash');print('CAUGHT',key,str(e))
        else:raise AssertionError('[FAIL] survived '+key)
    x=copy.deepcopy(d);x['source_pins'][PIN]='0'*64
    try:audit(x)
    except AssertionError as e:check('[FAIL] dependency pin' in str(e),'pin catch');print('CAUGHT pin')
    else:raise AssertionError('[FAIL] pin survived')
    print('PASS K1897 probe:',n,'exact controls + pin; 4 math + 1 report + 1 pin faults caught')
if __name__=='__main__':main()
