#!/usr/bin/env python3
from pathlib import Path
import argparse,hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def check(out,name,value): out[name]=bool(value)
RESULT='K2153';REPORT='k2153-diagonal-detector-energy.json'
DEPS=['lab/process/k2151-optimal-local-mode-discrimination.json','explorations/conditional-build/k2153-diagonal-detector-energy-2026-10-27.md']
EVIDENCE='Written countable-instrument annihilator/form-domain proof, Cauchy-Schwarz minimization and summation by parts; finite exact controls are separate.'
FAULTS=['annihilator_sign','missing_z','single_population','linear_amplitudes','discard_complement','erase_phase','wrong_signal','classical_coin']
def controls(fault=None):
    out={};z=s.Rational(1,4);t=s.Rational(9,25);N=z/(1-z);Es=10
    v=[s.Matrix([1,0]),s.Matrix([s.sqrt(1-t),s.sqrt(t)]),s.Matrix([0,1])]
    if fault=='linear_amplitudes':v[1]=s.Matrix([1-t,t])
    if fault=='discard_complement':v=[s.Matrix([0,x[1]]) for x in v]
    for n,x in enumerate(v):check(out,f'complete_n{n}',x.dot(x)==1)
    for a in range(2):
        for n in range(3):
            f0=v[min(n,2)][a];f1=v[min(n+1,2)][a]
            sch0=s.sqrt(1-z)*z**s.Rational(n,2)*f0
            sch1=s.sqrt(1-z)*z**s.Rational(n+1,2)*f1
            amp=s.sqrt(n+1)*(s.sqrt(N+1)*sch1+(-1 if fault!='annihilator_sign' else 1)*s.sqrt(N)*sch0)
            want=s.sqrt(n+1)*z**s.Rational(n+1,2)*(f1-f0)
            check(out,f'annihilator_a{a}_n{n}',s.simplify(amp-want)==0)
    energy=Es*sum((n+1)*z**(n if fault=='missing_z' else n+1)*(v[n+1]-v[n]).dot(v[n+1]-v[n]) for n in range(2))
    if fault=='single_population':energy/=2
    soft=2*Es*(z*(1-s.sqrt(1-t))+2*z*z*(1-s.sqrt(t)))
    mix=2*Es*(t*z+(1-t)*2*z*z)
    check(out,'exact_soft_energy',energy==soft==2)
    check(out,'strict_classical_excess',mix==s.Rational(17,5) and mix>soft)
    alpha=t*(1-z)*z+z*z;eta=t*(1-z)**2+z*(2-z)
    if fault=='wrong_signal':eta=alpha
    delta=(1-z)*sum((n+1)*z**n*(v[n+1][1]**2-v[n][1]**2) for n in range(2))
    check(out,'fixed_signal_contrast',alpha==s.Rational(13,100) and eta==s.Rational(16,25) and eta-alpha==delta)
    check(out,'contrast_energy_bound',energy>=z*Es*delta**2==s.Rational(2601,4000))
    zz=s.symbols('z',positive=True);geom=s.diff(zz/(1-zz),zz)
    check(out,'infinite_geometric_weight',s.simplify(geom-1/(1-zz)**2)==0)
    phase=lambda n:1 if fault=='erase_phase' else (-1)**n
    check(out,'identical_effects_different_channel',all(phase(n)**2==1 for n in range(4)) and (phase(1)-phase(0))**2==4)
    # Actual Kraus overlap kernels on occupations 0,1,2; coin labels retained then forgotten.
    softkernel=s.Matrix(3,3,lambda i,j:v[i].dot(v[j]))
    hard1=[0,1,1];hard2=[0,0,1]
    mixkernel=s.Matrix(3,3,lambda i,j:t*int(hard1[i]==hard1[j])+(1-t)*int(hard2[i]==hard2[j]))
    chosen=mixkernel if fault=='classical_coin' else softkernel
    check(out,'soft_channel_coherence',chosen[0,1]==s.Rational(4,5) and chosen[1,2]==s.Rational(3,5))
    check(out,'coin_channel_coherence',mixkernel[0,1]==s.Rational(16,25) and mixkernel[1,2]==s.Rational(9,25))
    check(out,'fixed_effects_preserved',all(v[n][1]**2==t*hard1[n]+(1-t)*hard2[n] and v[n][0]**2==t*(1-hard1[n])+(1-t)*(1-hard2[n]) for n in range(3)))
    for n in range(2):check(out,f'projection_distance_n{n}',(v[n+1][1]**2-v[n][1]**2)**2<=(v[n+1]-v[n]).dot(v[n+1]-v[n]))
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
    baseline=controls();bad=[k for k,v in baseline.items() if not v]
    if bad: raise AssertionError('BASELINE FAIL: '+str(bad))
    caught={}
    for fault in FAULTS:
        failed=[k for k,v in controls(fault).items() if not v]
        if not failed: raise AssertionError('UNDETECTED '+fault)
        caught[fault]=failed
    report={'result_id':RESULT,'status':'conditional_exact_controls','exact_checks':baseline,'fault_failures':caught,'dependency_sha256':{x:hashlib.sha256((ROOT/x).read_bytes()).hexdigest() for x in DEPS},'probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'universal_evidence':EVIDENCE}
    if RESULT=='K2154': report['numerical_evidence']=dynamics()
    if args.write: (ROOT/'lab/process'/REPORT).write_text(json.dumps(report,indent=2)+'\n')
    else: assert json.loads((ROOT/'lab/process'/REPORT).read_text())==report,'stored report differs'
    print(json.dumps({'result':RESULT,'exact_checks':len(baseline),'faults_rejected':len(caught),'numerical_checks':report.get('numerical_evidence',{}).get('checks',{})},indent=2))
if __name__=='__main__': main()
