#!/usr/bin/env python3
"""K2150 exact hypothesis controls, not a native full-rank replay."""
from pathlib import Path
import json, hashlib, argparse
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
RESULT='K2150';REPORT='k2150-raw-mobile-locus-regularity.json'
DEPS=['lab/process/k2141-full-graph-raw-tangent.json','lab/process/k2144-raw-neighborhood-rank-budget.json','lab/process/k2147-moving-raw-kernel-prolongation.json']
EVIDENCE='Written fixed-annihilator/Gronwall and rank-stratum proof; finite exact abstract controls do not classify the native exceptional locus.'
FAULTS=['target_column','singular_sign','radial_factor','wrong_dimension','closed_locus']
def check(out,name,condition): out[name]=bool(condition)
def controls(fault=None):
    out={};rank=lambda F,T:F.row_join(T).rank()-F.rank()
    for z,w,expected in [(0,0,1),(1,0,0),(0,1,1),(1,1,1),(-1,0,0)]:
        F=s.Matrix([z,0]);T=s.Matrix([1,0 if fault=='target_column' else w])
        check(out,f'rank_{z}_{w}',rank(F,T)==expected)
    mobile=lambda z,w:rank(s.Matrix([z,0]),s.Matrix([1,w]))<1
    limitmobile=mobile(0,0) if fault!='closed_locus' else mobile(s.Rational(1,100),0)
    check(out,'nonclosed_limit',mobile(1,0) and not limitmobile)
    x=s.symbols('x',positive=True);z=s.exp(-1/x**2);c=(2 if fault=='singular_sign' else -2)/x**3
    check(out,'flat_departure_equation',s.simplify(z*c+s.diff(z,x))==0)
    check(out,'flat_first_three_jets',all(s.limit(s.diff(z,x,k),x,0,dir='+')==0 for k in range(4)))
    check(out,'singular_path_cost',s.integrate(2/x**3,(x,0,1))==s.oo)
    check(out,'integrable_unbounded_control',s.integrate(1/s.sqrt(x),(x,0,1))==2)
    xs=s.symbols('x0:4',real=True);r2=sum(t*t for t in xs);c=s.Matrix([(-1 if fault=='radial_factor' else -2)*t/r2 for t in xs]);grad=s.Matrix([s.diff(r2,t) for t in xs])
    check(out,'radial_equation',s.simplify(r2*c+grad)==s.zeros(4,1))
    check(out,'radial_norm',s.simplify((c.T*c)[0]-4/r2)==0)
    dim=3 if fault=='wrong_dimension' else 4
    check(out,'ambient_p3_finite',s.integrate(x**(dim-1-3),(x,0,1))==1)
    check(out,'ambient_p4_diverges',s.integrate(x**(dim-1-4),(x,0,1))==s.oo)
    check(out,'radial_path_diverges',s.integrate(2/x,(x,0,1))==s.oo)
    check(out,'punctured_nonconstant',s.diff(s.exp(x),x)-s.exp(x)==0)
    F=s.Matrix([[1,0],[0,0],[0,0]]);T=s.Matrix([[1,0],[1,0],[0,1]]);L=s.diag(0,1,1)
    check(out,'quotient_injective',(L*F)==s.zeros(3,2) and (L*T).rank()==2 and rank(F,T)==2)
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
