#!/usr/bin/env python3
"""Exact finite controls; continuum/operator claims use the companion written proof."""
import sympy as s
ID='K2268'
NOTE='explorations/conditional-build/k2268-observation-regularity-cosmology-2026-10-29.md'
REPORT='lab/process/k2268-observation-regularity-cosmology.json'
DEPS=['explorations/conditional-build/k2266-windowed-cosmology-test-2026-10-29.md']


def verify(m):
    out={}
    def eq(k,a,b=0):out[k]=s.simplify(a-b)==0
    def yes(k,a):out[k]=bool(a)
    x,t,h,L=s.symbols('x t h L',positive=True)
    y=1+L*x*x/2;p=1+L*h*x/2
    eq('interpolation_sharp_midpoint',(p-y).subs(x,h/2),L*h*h/s.Integer(m.get('interp_den',8)))
    eq('derivative_sharp_endpoint',(s.diff(p-y,x)).subs(x,0),L*h/s.Integer(m.get('deriv_den',2)))
    S=s.Matrix([[1,-s.Rational(1,2)],[-s.Rational(1,2),1]]);ell=s.Matrix([-1,1]);e=S*ell
    eq('ellipsoid_member',(e.T*S.inv()*e)[0],3)
    var=3*(S[0,0]+S[1,1]-m.get('cross',2)*S[0,1])
    eq('correlated_support_saturation',(ell.dot(e))**2,var)
    hh=s.Rational(1,10);noise=s.Rational(1,100);slope=(noise-(-noise))/hh
    eq('secant_noise_amplification',slope,2*noise/(hh**m.get('noise_power',1)))
    knots=[s.Integer(1),s.Rational(3,2),s.Integer(2)];values=[1+z*z for z in knots];slopes=[(values[j+1]-values[j])/(knots[j+1]-knots[j]) for j in range(2)];yes('piecewise_not_C1',slopes[0]!=slopes[1])
    w=(x-1)**2*(2-x)**2;y0=1+x**3;g=(x-1)**2*(2-x)**3/s.Integer(100)
    integ=lambda f:s.integrate(s.expand(f),(x,1,2))
    for j in range(3):
        ww=x**j*w;c=x*x*ww
        eq('weak_energy_cancellation_'+str(j),integ(c*((s.diff(y0+g,x))**2-s.diff(y0,x)**2)),integ(-m.get('integration_cross',2)*s.diff(c*s.diff(y0,x),x)*g+c*s.diff(g,x)**2))
    wt=t*t*(1-t)**2
    eq('window_sup_factor',s.Rational(1,16)-wt,(t-s.Rational(1,2))**2*(s.Rational(1,2)+2*t-2*t*t)/2)
    # Exact extrema of w0'' and elementary factor form of w0'.
    eq('window_derivative_factor',s.diff(wt,t),2*t*(1-t)*(1-2*t))
    for pt,expected in [(0,2),(s.Rational(1,2),-1),(1,2)]:eq('second_derivative_'+str(pt),s.diff(wt,t,2).subs(t,pt),expected)
    # Triangle bounds for x^j w0 on [1,2], j=0,1,2.
    for j in range(3):
        b0=s.Rational(2**j,16)
        b1=(s.Rational(j*2**max(j-1,0),16) if j else 0)+s.Rational(2**j,2)
        b2=(s.Rational(j*(j-1)*2**max(j-2,0),16) if j>=2 else 0)+(j*2**max(j-1,0) if j else 0)+2**(j+1)
        yes('window0_bound_'+str(j),b0<=s.Rational(1,4));yes('window1_bound_'+str(j),b1<=s.Rational(9,4));yes('window2_bound_'+str(j),b2<=s.Rational(97,8))
    eq('ell_bound',4*s.Rational(97,8)+12*s.Rational(9,4)+4*s.Rational(1,4),s.Rational(153,2))
    eq('cross_energy_bound',12*8/s.Integer(4)+3*16*s.Rational(9,4),132)
    eq('aggregate_constant',s.Rational(45,2)*132+90*s.Rational(153,2)+300/s.Integer(4),9930)
    v=s.Matrix([649,-870,287])/1806
    ws=[w,x*w,x*x*w];q=s.Matrix([integ(ww*s.Rational(81,4)*x**6) for ww in ws]);A=s.Matrix([3*integ(ww*y0) for ww in ws]);B=s.Matrix([-integ(ww)/2 for ww in ws])
    eq('shared_r_cancel',v.dot(B));eq('shared_a_center_cancel',v.dot(A));eq('unit_l1',sum(abs(z) for z in v),1)
    margin=v.dot(q);eq('margin',margin,s.Rational(205767,24104080))
    step=s.Rational(1,2000);eta=s.Rational(m.get('eta_num',1),10**8);eps0=3*step*step+eta;eps1=12*step+2*eta/step
    bound=9930*eps0+s.Rational(45,4)*eps1*eps1
    yes('actual_rejection_consumer',bound<margin)
    if not m: eq('displayed_bound',bound,s.Rational(3978609,500000000))
    yes('positive_domain',2-eps0>0);yes('M10_valid',9+eps0<10);yes('nonempty_curvature_witness',max(s.diff(y0,x,2).subs(x,z) for z in [1,2])<=12)
    # Whole-domain F: y=1+x², p through endpoints, curvature L=2 on [1,2].
    pp=3*x-1;ss=3;ee0=s.Rational(1,4);ee1=1;fbar=100-12*pp+3*x*ss
    yes('F_whole_cell_certificate',min(fbar.subs(x,z) for z in [1,2])>12*ee0+6*ee1)
    eq('actual_F_expression',100-12*(1+x*x)+3*x*2*x,88-6*x*x)
    # Finite samples leave nonzero interior bumps; no membership assertion.
    bump=x*x*(1-x)**2
    eq('hidden_bump_left',bump.subs(x,0));eq('hidden_bump_right',bump.subs(x,1));yes('hidden_bump_nonzero',bump.subs(x,s.Rational(1,2))>0)
    return out

FAULTS={'too_small_value_bound': {'interp_den': 16}, 'too_small_derivative_bound': {'deriv_den': 4}, 'lost_covariance': {'cross': 0}, 'lost_noise_amplification': {'noise_power': 0}, 'wrong_energy_cross': {'integration_cross': 1}, 'overlarge_noise': {'eta_num': 100}}

def main():
    import argparse,hashlib,json
    from pathlib import Path
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
    checks=verify({});bad=[k for k,v in checks.items() if not v]
    if bad: raise AssertionError('BASELINE FAIL: '+str(bad))
    caught={}
    for name,change in FAULTS.items():
        result=verify(change)
        failures=[k for k,v in result.items() if not v]
        if not failures: raise AssertionError('UNDETECTED: '+name)
        caught[name]=failures
    root=Path(__file__).resolve().parents[2]
    paths=[NOTE,str(Path(__file__).resolve().relative_to(root))]+DEPS
    hashes={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in paths}
    report=dict(result_id=ID,status='internally_reviewed_conditional_mathematics',evidence_kind='finite_exact_symbolic_and_matrix_controls_plus_genuine_changed_input_faults',checks=len(checks),faults=len(caught),fault_failures=caught,sha256=hashes,ceiling='Finite checks supplement written proofs; no empirical, source, novelty, Lean or remote-CI certification.')
    dest=root/REPORT
    if args.write:dest.write_text(json.dumps(report,indent=2)+'\n')
    else:
        old=json.loads(dest.read_text());assert old==report,'stale report: reproduce with --write after review'
    print(ID, 'PASS',len(checks),'exact finite controls;',len(caught),'genuine faults; hashes current')
if __name__=='__main__':main()
