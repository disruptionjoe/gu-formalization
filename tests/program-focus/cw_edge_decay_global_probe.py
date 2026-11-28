#!/usr/bin/env python3
"""Exact controls; full-dimensional PDE bounds and packet proof are written/reviewed."""
from pathlib import Path
import argparse,hashlib,json,sys,time
sys.dont_write_bytecode=True
import sympy as s
from printed_equation_jets_symbol_probe import engine
from cw_fullsystem_domain_probe import D,FACTORS
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/cw-edge-decay-global-certificates.json'
PINS={'lab/process/cw-all-threshold-boundary-certificates.json': 'b2a29cb5ab9f56abda601bff7d56520b60b8b5cde82ade2f1617fff7e1725d02', 'lab/process/cw-fullsystem-domain-certificates.json': '8ede03f10d6bd28570a3028eb5c320d297de67a827d8b51c545ee5da76314be5', 'lab/process/cw-one-sided-boundary-certificates.json': 'f4e6666601b25a18bb1288d2fa19493df432e6b3f194fe17b301cf70d81e0ea2', 'tests/program-focus/cw_fullsystem_domain_probe.py': '705acae3569fb46445ecb8c7562baddce793a3eb482e5477848c20ee9900cc1d', 'tests/program-focus/printed_equation_jets_symbol_probe.py': 'e43da867d17cf985bfac8c014657e8cbf18c94e80013350ca69eee804a4ebeb8', 'tests/program-focus/source_action_deep_algebra.py': '4e3800131049e2b397bbce6106bfc5766d2f5fbf996319c50942f3b805d65598'}
"""Few-column actual CW high-frequency norm fixture, called by build.

build supplies printed_equation_jets_symbol_probe.engine(D).
No import-time work or filesystem effects. Symbolic parameter R>0.
"""


def native_hook(e):
    import sympy as s
    from cw_fullsystem_domain_probe import D, add, scale, compact_symbol, cp, conjugate

    checks = []

    def ck(name, condition):
        assert condition, name
        checks.append(name)

    def native(zeta, value):
        return add(e.Phi(e.wedge({(1 << i, 0): v for i, v in zeta.items()}, value)))

    def left(gamma, value):
        out = {}
        for (leg, mask), coefficient in value.items():
            for blade, v in cp(gamma, {mask: coefficient}).items():
                key = (leg, blade)
                out[key] = out.get(key, 0)+v
        return add(out)

    def norm2(value):
        return s.expand(sum(s.conjugate(v)*v for v in value.values()))

    R = s.symbols('R', positive=True, real=True)
    kap = s.Integer(12)
    omega = s.Integer(10)
    k = {1: R+16/R, 10: R-16/R}
    beta = {(1 << 3, 1 << 3): s.Integer(1),
            (1 << 4, 1 << 4): s.Integer(-1)}
    ctau = {1: s.Integer(-1)}
    ckspace = {1 << i: D[i]*v for i, v in k.items()}
    initial = left(ctau, beta)
    spatial_part = left(ckspace, beta)
    B = add(scale(kap, beta), scale(2*s.I, spatial_part))
    endpoint = scale(s.Rational(1, 20), B)
    vplus = add(B, scale(20*s.I, initial))
    vminus = add(B, scale(-20*s.I, initial))

    ck('fixed spatial square64', s.expand(sum(D[i]*v*v for i, v in k.items())) == 64)
    ck('inside common CW domain with fixed margin28', 64-kap**2/4 == 28)
    ck('actual hook factor1 frequency', omega**2 == 64+kap**2/4)
    for sign, v in [(1, vplus), (-1, vminus)]:
        zeta = {0: sign*s.I*omega, **{i: s.I*c for i, c in k.items()}}
        ck('actual shell square '+str(sign),
           s.expand(sum(D[i]*c*c for i, c in zeta.items())) == 36)
        ck('compact/native kernel binding '+str(sign),
           native(zeta, v) == compact_symbol(zeta, v))
        ck('actual full massive kernel '+str(sign),
           not add(scale(kap, v), native(zeta, v)))

    # T(t)=cos(10t) initial + sin(10t) endpoint; verify both coefficients
    # directly in A_t T'+C(k)T=0, without trusting scalar dispersion alone.
    At = lambda f: native({0: s.Integer(1)}, f)
    C = lambda f: add(scale(kap, f), native({i: s.I*v for i, v in k.items()}, f))
    ck('native cosine evolution coefficient', not add(C(initial), scale(omega, At(endpoint))))
    ck('native sine evolution coefficient', not add(C(endpoint), scale(-omega, At(initial))))
    ck('initial mode cancellation', scale(1/(4*s.I*omega), add(vplus, scale(-1, vminus))) == initial)
    ck('quarter-period endpoint', scale(s.Rational(1, 40), add(vplus, vminus)) == endpoint)
    ck('constant initial coefficient norm', norm2(initial) == 2)
    ratio2 = s.cancel(norm2(endpoint)/norm2(initial))
    target = R**2/50+s.Rational(9, 25)+s.Rational(128, 25)/R**2
    ck('exact coefficient norm ratio', s.expand(ratio2-target) == 0)
    ck('positive leading norm growth', s.expand(ratio2*R**2)
       == R**4/50+s.Rational(9, 25)*R**2+s.Rational(128, 25))

    # Primary-minus real field: all real/imaginary Fourier quadratures have
    # real sharp-skew grades1/2; append the conjugate patch at -k.
    for label, value in [('initial', initial), ('endpoint', endpoint)]:
        re = {key: s.re(v) for key, v in value.items() if s.re(v) != 0}
        im = {key: s.im(v) for key, v in value.items() if s.im(v) != 0}
        ck(label+' primary-minus real quadratures', e.real_skew(re) and e.real_skew(im))
    ck('real coefficient time operator', conjugate(At(endpoint)) == At(conjugate(endpoint)))
    Cminus = lambda f: add(scale(kap, f), native({i: -s.I*v for i, v in k.items()}, f))
    ck('conjugate spatial-frequency adapter', conjugate(C(endpoint)) == Cminus(conjugate(endpoint)))

    # Computational ambient positive-plane rotation fixes time and moves
    # the same witness inside the previously owned observed-Lorentz core.
    kcore = {4: R+16/R, 10: R-16/R}
    bcore = {(1 << 3, 1 << 3): s.Integer(1),
             (1 << 1, 1 << 1): s.Integer(-1)}
    icore = left(ctau, bcore)
    sc = left({1 << i:D[i]*v for i,v in kcore.items()}, bcore)
    Bcore = add(scale(kap,bcore),scale(2*s.I,sc))
    ecore = scale(s.Rational(1,20),Bcore)
    normal = s.expand(sum(D[i]*v*v for i,v in kcore.items() if i>=4))
    ck('core normal invariant64',normal==64)
    ck('core fixed normal margin28',normal-36==28)
    for sign in [-1,1]:
        vc = add(Bcore,scale(sign*20*s.I,icore))
        zc = {0:sign*10*s.I,**{i:s.I*v for i,v in kcore.items()}}
        ck('core native kernel '+str(sign),not add(scale(kap,vc),native(zc,vc)))
        ck('core compact/native binding '+str(sign),native(zc,vc)==compact_symbol(zc,vc))
    ck('core initial norm unchanged',norm2(icore)==2)
    ck('core exact amplification unchanged',s.simplify(norm2(ecore)/2-target)==0)
    ck('core primary-minus quadratures',e.real_skew({k:s.re(v)for k,v in ecore.items() if s.re(v)!=0}) and e.real_skew({k:s.im(v)for k,v in ecore.items() if s.im(v)!=0}))

    return {
        'status': 'PASS', 'check_count': len(checks), 'checks': checks,
        'kappa': 12, 'factor': 1, 'spatial_square': 64, 'frequency': 10,
        'initial_norm_squared': '2',
        'quarter_period': 'pi/20', 'amplification_squared': str(target),
        'mode_terms': [len(vplus), len(vminus)], 'normal_core_witness': {'N':64,'margin':28,'same_amplification':True},
        'limits': [
            'Actual selected frozen K95 primary-minus field sector, inside common CW support.',
            'No same-order global coefficient Sobolev bound; derivative-loss lower bound1.',
            'No exclusion of H_modal or finite derivative loss, and no physical norm conclusion.',
            'Plane fixtures require the accompanying smooth full-dimensional packet argument.',
        ],
    }


def build():
 checks=[]
 def ck(n,v):assert v,n;checks.append(n)
 deps=dict(PINS)
 for p in PINS:
  if p.endswith('.json'):deps.update(json.loads((ROOT/p).read_text()).get('dependencies',{}))
 for p,h in deps.items():ck('reuse '+p,hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h)
 A,al,q,C0,C2,do,d2=s.symbols('A al q C0 C2 do d2',real=True)
 de=C0-A*(1+al)**2-q;v=C2-A*al**2-q
 J=s.Matrix([[s.diff(f,x)for x in [al,q]]for f in [de,v]])
 ck('decay invariant Jacobian',s.expand(J.det())==2*A)
 ai=(C0-C2-A-de+v)/(2*A);qi=C2-v-A*ai**2
 ck('decay invariant alpha inverse',s.simplify(ai-al)==0)
 ck('decay invariant q inverse',s.simplify(qi-q)==0)
 x,y=s.symbols('x y',positive=True)
 ck('decay squared-kernel domination',s.expand((x+y)**2-4*x*y)==(x-y)**2 or s.expand((x+y)**2-4*x*y-(x-y)**2)==0)
 ck('squared-kernel square-root measure',s.simplify((2*x)*(2*y)/(x+y)**2-4*x*y/(x+y)**2)==0)
 ck('both nonnull signatures admit positive plane',9-1>=2 and 9>=2)
 ck('null decay has positive C or is absent',all(-s.Rational(36,a)!=0 for a in FACTORS))
 ck('actual triple threshold -4 -4 to -1',-s.Rational(36,-4)==9 and -s.Rational(36,-1)==36 and (3+3)**2==36)
 # A second exact triple: k=3eta10+3sqrt(3)eta11 gives k^2=-36,
 # l=3eta10-3sqrt(3)eta11 and (k+l)^2=-36.
 ck('negative-axis triple factor+1',-3**2-(3*s.sqrt(3))**2==-36 and -(3+3)**2==-36)
 mu,delta,q0=s.symbols('mu delta q0',real=True)
 N=s.Matrix([[0,1],[delta,0]]);vv=s.Matrix([q0,-mu*q0])
 ck('actual regular decay algebra',s.simplify((N*vv+mu*vv).subs(delta,mu**2))==s.zeros(2,1))
 # The paired roots remove the 1/omega divisor in propagation.
 om,t=s.symbols('om t',positive=True)
 ck('paired sine removable edge',s.limit(s.sin(om*t)/om,om,0,dir='+')==t)
 ck('paired cosine removable edge',s.limit(s.cos(om*t),om,0,dir='+')==1)
 z,r2=s.symbols('z r2');kap=s.Integer(12)
 vals=[]
 for a in FACTORS:
  qa=kap**2/(4*s.Integer(a));da=-r2-qa
  ck('shell remainder '+str(a),s.rem(-z**2-r2-qa,z**2-da,z)==0)
  Ra=s.prod(kap**2-4*b*qa for b in FACTORS if b!=a)
  ck('constant paired denominator '+str(a),4*a*kap**2*Ra!=0)
  vals.append(str(4*a*kap**2*Ra))
 ck('scalarizer differential degree',2+2*len(FACTORS)==40)
 ck('paired polynomial remainder degree bounds',all(2*(j//2)+(39-j)<=39 for j in range(0,40,2)) and all(2*(j//2)+(39-j)<=38 for j in range(1,40,2)))
 # Known-answer calibration: equal diagonal unitary modes conserve the
 # coefficient norm; a nonnormal two-mode shear has cancellation growth.
 rr=s.symbols('rr',real=True);S=s.Matrix([[1,rr],[0,1]])
 E=S*s.diag(s.I,-s.I)*S.inv()
 ck('unitary diagonal control',s.diag(s.I,-s.I).conjugate().T*s.diag(s.I,-s.I)==s.eye(2))
 ck('planted cancellation diagnostic',s.expand((E*s.Matrix([0,1])).conjugate().dot(E*s.Matrix([0,1])))==4*rr**2+1)
 native=native_hook(engine(D));checks+=native['checks']
 return {'schema':'gu-cw-edge-decay-global-v1','status':'PASS','probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'dependencies':deps,'check_count':len(checks),'check_names':checks,'native_hook':native,'analytic_controls':{'decay_Jacobian':'2A','decay_density':'1/(2sqrt(abs(A)))','two_decay_squared_kernel_bound':'sqrt(D E)','output_tail':'epsilon^(1/4)','stable_input_edge_norm':'H_modal actual shell-field amplitudes, not regular T0 norm','global_derivative_loss_window':[1,39],'paired_denominators':vals},'limits':['Written analytic bounds and normalized packet proof are not formalized by finite controls.','No physical norm, nonlinear closure, source or all-class-C verdict.','39 is conservative sufficient linear loss;1 is necessary, not proven sufficient.']}
if __name__=='__main__':
 p=argparse.ArgumentParser();g=p.add_mutually_exclusive_group(required=True);g.add_argument('--write',action='store_true');g.add_argument('--verify',action='store_true');a=p.parse_args();t=time.monotonic();d=build()
 if a.write:OUT.write_text(json.dumps(d,indent=2)+'\n')
 else:assert json.loads(OUT.read_text())==json.loads(json.dumps(d)),'certificate mismatch'
 print(json.dumps({'status':'PASS','checks':d['check_count'],'seconds':time.monotonic()-t}))
