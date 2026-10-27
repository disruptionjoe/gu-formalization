#!/usr/bin/env python3
"""K2152 exact finite invariant-sector controls; theorem is all Fock."""
from pathlib import Path
import json,hashlib,argparse,itertools,math
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
RESULT='K2152';REPORT='k2152-finite-chain-threshold-detector.json'
DEPS=['explorations/conditional-build/k2145-parity-causal-duration-2026-10-27.md','lab/process/k2151-optimal-local-mode-discrimination.json']
EVIDENCE='Written all-Fock conjugation and quadratic-form proof. Exact invariant total-number<=2 checks include a reference, and are not a continuum or uniform-regulator certificate.'
FAULTS=['gather_order','gather_sign','omit_undo','parity_for_threshold','off_by_one','zero_point']
def check(out,name,condition):out[name]=bool(condition)
def lift(O,basis):
    x=s.symbols('x0:3');cols=[]
    for ns in basis:
        poly=s.Poly(s.expand(s.prod(sum(O[i,j]*x[i] for i in range(3))**ns[j] for j in range(3))),*x)
        norm=s.sqrt(s.prod(s.factorial(n) for n in ns))
        cols.append(s.Matrix([poly.coeff_monomial(s.prod(x[i]**ms[i] for i in range(3)))*s.sqrt(s.prod(s.factorial(m) for m in ms))/norm for ms in basis]))
    return s.Matrix.hstack(*cols)
def controls(fault=None):
    out={};c=s.Rational(3,5);d=s.Rational(4,5);R12=s.Matrix([[c,d,0],[-d,c,0],[0,0,1]]);R23=s.Matrix([[1,0,0],[0,c,d],[0,-d,c]])
    if fault=='gather_sign':R23[2,1]=d
    O=R23*R12 if fault=='gather_order' else R12*R23;f=s.Matrix([c,c*d,d*d])
    check(out,'adjacent_orthogonality',O.T*O==s.eye(3));check(out,'actual_gather',O*f==s.Matrix([1,0,0]))
    basis=sorted([v for v in itertools.product(range(3),repeat=3) if sum(v)<=2],key=lambda v:(sum(v),v));B=lift(O,basis);dim=len(basis)
    check(out,'fock_lift_unitary',s.simplify(B.T*B)==s.eye(dim))
    number=s.diag(*[sum(v) for v in basis]);check(out,'number_conserved',B*number==number*B)
    A=[]
    for j in range(3):
        a=s.zeros(dim)
        for col,v in enumerate(basis):
            if v[j]:w=list(v);w[j]-=1;a[basis.index(tuple(w)),col]=s.sqrt(v[j])
        A.append(a)
    bf=sum((f[j]*A[j] for j in range(3)),s.zeros(dim));nf=bf.T*bf
    check(out,'mode_number_conjugation',s.simplify(B.T*s.diag(*[v[0] for v in basis])*B-nf)==s.zeros(dim))
    # Threshold2 polynomial is exact only on this invariant total<=2 control.
    target=s.simplify(nf*(nf-s.eye(dim))/2)
    selector=lambda n:int(n>=2)
    if fault=='parity_for_threshold':selector=lambda n:n%2
    if fault=='off_by_one':selector=lambda n:int(n>2)
    P=s.diag(*[selector(v[0]) for v in basis]);undo=s.eye(dim) if fault=='omit_undo' else B.T
    K0=s.simplify(undo*(s.eye(dim)-P)*B);K1=s.simplify(-s.I*undo*P*B)
    check(out,'complete_Kraus',s.simplify(K0.conjugate().T*K0+K1.conjugate().T*K1)==s.eye(dim))
    check(out,'threshold_effect',s.simplify(K1.conjugate().T*K1-target)==s.zeros(dim))
    check(out,'full_instrument_undo',K0==s.eye(dim)-target and K1==-s.I*target)
    # Superposition of vacuum/ref0 and a nontrivial two-particle mode/ref1.
    vacuum=s.zeros(dim,1);vacuum[basis.index((0,0,0))]=1;two=(bf.T*bf.T*vacuum)/s.sqrt(2)
    psi=(s.kronecker_product(vacuum,s.Matrix([1,0]))+s.kronecker_product(two,s.Matrix([0,1])))/s.sqrt(2);rho=psi*psi.T
    def branch(K):L=s.kronecker_product(K,s.eye(2));return s.simplify(L*rho*L.conjugate().T)
    check(out,'reference_complete_record',branch(K0)==branch(s.eye(dim)-target) and branch(K1)==branch(target))
    W=s.Matrix([[5,4,0],[4,5,0],[0,0,4]]);nu=s.Integer(3);Z=s.trace(W)/2;C=s.Integer(3);D=s.Integer(27)
    positive=lambda M:all(ev>=0 for ev in M.eigenvals())
    check(out,'first_energy_form',positive(C*s.eye(3)-s.eye(3)/nu) and positive(C*W**2-nu*s.eye(3)))
    check(out,'second_energy_form',positive(D*s.eye(3)/nu-s.eye(3)) and positive(D*nu*s.eye(3)-W**2))
    Nvac=s.trace(W/nu+nu*W.inv()-2*s.eye(3))/4
    check(out,'vacuum_site_number',Nvac==s.Rational(11,16))
    energy=s.simplify(s.trace(O*W*O.T+W**2*O*W.inv()*O.T)/4-Z)
    budget=0 if fault=='zero_point' else D*(Nvac+s.Rational(3,2))-Z
    check(out,'vacuum_energy_budget',0<energy<=budget)
    check(out,'general_energy_bound_vacuum',energy<=D*C*Z-Z)
    return out
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
    baseline=controls();bad=[k for k,v in baseline.items() if not v]
    if bad: raise AssertionError('BASELINE FAIL: '+str(bad))
    caught={}
    for fault in FAULTS:
        result=controls(fault);failed=[k for k,v in result.items() if not v]
        if not failed: raise AssertionError('UNDETECTED '+fault)
        caught[fault]=failed
    report={'result_id':RESULT,'status':'conditional_exact_controls','exact_checks':baseline,'fault_failures':caught,'dependency_sha256':{x:hashlib.sha256((ROOT/x).read_bytes()).hexdigest() for x in DEPS},'probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'universal_evidence':EVIDENCE}
    if args.write: (ROOT/'lab/process'/REPORT).write_text(json.dumps(report,indent=2)+'\n')
    else:
        assert json.loads((ROOT/'lab/process'/REPORT).read_text())==report, 'stored report differs from current proof controls or dependencies'
    print(json.dumps({'result':RESULT,'exact_checks':len(baseline),'faults_rejected':len(caught),'failures':caught},indent=2))
if __name__=='__main__': main()
