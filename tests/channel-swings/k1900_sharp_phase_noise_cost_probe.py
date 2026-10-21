from pathlib import Path
import json,hashlib,sys,copy
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def ck(b,label):
    if not b:raise AssertionError('[FAIL] '+label)
def eq(a,b,label):ck(s.simplify(a-b)==0,label)
def mat(d):
    a=s.zeros(d['rows'],d['columns'])
    for i,j,v in d['entries']:a[i,j]=s.Rational(v)
    return a
REPORT='lab/process/k1900-sharp-phase-noise-cost.json'
PIN='lab/process/k1898-stochastic-pulse-energy-coherence.json'
def phase_channel(probabilities):
    # Direct phase factors, without the producer exponential formula.
    factors=[s.Matrix([1,s.I,-1]),s.Matrix([1,s.I,1]),s.Matrix([1,-s.I,1]),s.Matrix([1,-s.I,-1])]
    gram=sum((p*v*v.H for p,v in zip(probabilities,factors)),s.zeros(3))
    ck(gram==s.eye(3),'independent neutral coherence matrix')
    return gram
def audit(d):
    p=list(map(s.Rational,d['optimal_increment_probabilities']));G=phase_channel(p)
    ck(G==s.Matrix(d['three_mode_gram']),'reported Gram matrix')
    C=d['coefficients'];eq(s.sympify(C['three_history_ratio']),s.Rational(32,27),'history control ratio')
    # Direct kinetic cost for sampled piecewise linear profiles, slopes +/-pi/2 over unit gaps.
    cost=sum(pi*((s.pi/2)**2+(s.pi/2)**2) for pi in p)/(2*s.pi)
    eq(cost,2*s.sympify(C['three_mode_factor'])*s.pi,'independent two-ramp energy')
    eq(s.sympify(C['one_channel_factor'])*(s.pi/2)**2/s.pi,s.sympify(C['three_mode_factor'])*s.pi,'single-ramp energy')
    ck(d['source_pins'][PIN]==sha(PIN),'dependency pin')
def scalar_control(sign=-1):
    t,c,z=s.symbols('t c z',real=True);g=30*t*t*(1-t)**2
    left=s.diff(g,t)*(z-2*c*t)**3+sign*6*c*g*(z-2*c*t)**2
    eq(s.integrate(left,(t,0,1)),0,'scalar unused channel cancellation')
def global_controls():
    # Support quadratic at theta=pi/2, plus nonprincipal wrapped-phase controls.
    for v in [0,s.pi/6,s.pi/2,s.pi,2*s.pi,3*s.pi,10*s.pi]:
        gap=s.cos(v)-(s.pi/4-v*v/s.pi)
        ck(gap.evalf()>-1e-30,'global-support sample '+str(v))
    # These sampled inequalities are controls; the analytic convex proof is in the note.
    x=s.symbols('x',positive=True)
    eq(s.diff(s.sin(x)-x*s.cos(x),x),x*s.sin(x),'global convexity proof ingredient')
    # Fourier energy crossing in one rank-two direction.
    k,q=s.symbols('k q',positive=True)
    eq(2/(2*s.pi)*s.integrate(q,(q,0,k)),k*k/(2*s.pi),'independent one-direction energy factor')
    # Fixed endpoints 0 and pi/2, tail endpoints all zero; exact finite-element energy.
    L=s.symbols('L',positive=True)
    energy=(s.pi/2)**2+(s.pi/2)**2/L
    eq(s.limit(energy,L,s.oo),s.pi**2/4,'tail recovery')
    # Independent polynomial characteristic integration, no imported producer formula.
    t,c,z=s.symbols('t c z',real=True);g=30*t*t*(1-t)**2
    eq(s.integrate(g,(t,0,1)),1,'normalized temporal control')
    right=s.diff(g,t)*z**3-6*c*g*z*z
    left=s.diff(g,t)*(z-2*c*t)**3-6*c*g*(z-2*c*t)**2
    eq(s.integrate(right,(t,0,1)),-6*c*z*z,'scalar desired phase integral')
    eq(s.integrate(left,(t,0,1)),0,'scalar unused channel cancellation')
    return 7

def reject(fn,label):
    try:fn()
    except AssertionError as e:ck('[FAIL]' in str(e),'assertion failure');print('CAUGHT',label,str(e))
    else:raise AssertionError('[FAIL] survived '+label)
if __name__=='__main__':
    d=json.loads((ROOT/REPORT).read_text());audit(d);global_controls();scalar_control();print('BASELINE PASS K1900 probe')
    reject(lambda:scalar_control(sign=1),'wrong scalar characteristic sign')
    reject(lambda:phase_channel([s.Rational(1,2),0,0,s.Rational(1,2)]),'common binary signs')
    reject(lambda:phase_channel([s.Rational(1,3)]*3+[0]),'three-history deletion')
    for key,val in [('one_channel_factor','1'),('three_mode_factor','1/4'),('three_history_ratio','16/9')]:
        q=copy.deepcopy(d);q['coefficients'][key]=val;reject(lambda:audit(q),key)
    q=copy.deepcopy(d);q['source_pins'][PIN]='0'*64;reject(lambda:audit(q),'pin')
    print('PASS K1900 probe: exact phase/Fourier/ramp controls and 7 numerical support checks; 3 input, 3 report and 1 pin faults')
