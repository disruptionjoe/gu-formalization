"""Exact optical-window controls. Infinite-domain theorems are written in the note."""
from pathlib import Path
import sympy as s
import json, hashlib, sys
ROOT = Path(__file__).resolve().parents[2]
r,k,u,c,tau = s.symbols('r k u c tau', positive=True)
x=s.symbols('x',real=True)
g=(r-1)*(2-r)

def evaluate(fault=None):
    checks={}
    def check(name,value): checks[name]=bool(value)
    # Direct angular quadrature for an actual plane wave.
    for q in [1,2,3]:
        direct=s.integrate(s.exp(s.I*q*x),(x,-1,1))/2
        oracle=s.sin(q)/q
        if fault=='wrong_solid_angle': direct*=2
        check('normalized_shell_'+str(q),s.simplify(s.expand_complex(direct)-oracle)==0)
    F=r*g # delta=1 test input, not a claimed background solution.
    candidate_g=F/(r**(2 if fault=='wrong_radial_jacobian' else 1))
    check('radial_transfer_jacobian',s.simplify(candidate_g-g)==0)
    check('radial_zero_traces',g.subs(r,1)==0 and g.subs(r,2)==0)
    energy=s.integrate(s.diff(g,r)**2,(r,1,2))
    check('positive_taper_energy',energy==s.Rational(1,3))
    check('positive_selection_mass',s.integrate(F,(r,1,2))==s.Rational(1,4))
    for q in [1,2,3]:
        B=s.integrate(g*s.sin(q*r),(r,1,2))
        byparts=s.integrate(s.diff(g,r)*s.cos(q*r),(r,1,2))/q
        check('sine_derivative_identity_'+str(q),s.simplify(B-byparts)==0)
    # Zero extension's distributional derivative, using a concrete test function.
    phi=r*r
    actual=-s.integrate(s.diff(phi,r),(r,1,2))
    predicted=(0 if fault=='omit_endpoint_jumps' else phi.subs(r,1)-phi.subs(r,2))
    check('top_hat_boundary_distribution',actual==predicted)
    q=g/r
    check('all_sky_radial_energy',s.simplify(s.integrate(r*r*s.diff(q,r)**2,(r,1,2))-energy)==0)
    # Spherical zonal smooth mask: angular integration from area element 2pi du.
    A=(1+c*x)/(4*s.pi)
    norm=2*s.pi*s.integrate(A*A,(x,-1,1))
    grad=2*s.pi*s.integrate((1-x*x)*s.diff(A,x)**2,(x,-1,1))
    check('angular_normalization',2*s.pi*s.integrate(A,(x,-1,1))==1)
    check('angular_l2_norm',s.simplify(norm-(1+c*c/3)/(4*s.pi))==0)
    candidate_grad=0 if fault=='ignore_angular_gradient' else grad
    check('angular_gradient_energy',s.simplify(candidate_grad-c*c/(6*s.pi))==0)
    check('schur_coulomb_integral',2*s.pi*s.integrate(1/s.sqrt(2-2*x),(x,-1,1))==4*s.pi)
    # A sharp hemisphere has nonzero weak jump even where its classical derivative vanishes.
    test=1-x*x
    jump=-s.integrate(s.diff(test,x),(x,0,1))
    check('hemisphere_jump',jump==1)
    # Exact compact response normalization and dilation; no probabilistic simulation.
    chi=s.Rational(15,16)*(1-x*x)**2
    C=s.integrate(chi*chi,(x,-1,1))
    check('temporal_response_mass',s.integrate(chi,(x,-1,1))==1)
    check('temporal_l2_constant',C==s.Rational(5,7))
    for scale in [s.Rational(1,2),s.Rational(1,3),s.Rational(2,3)]:
        amplitude=1 if fault=='missing_temporal_normalization' else 1/scale
        dilated=amplitude*chi.subs(x,x/scale)
        check('response_scaling_'+str(scale),s.integrate(dilated*dilated,(x,-scale,scale))==C/scale)
    # Noise spatial Jacobian is F^2/r^2 after dt d3x integration.
    noise_radial=s.integrate(F*F/r**(0 if fault=='missing_noise_volume_jacobian' else 2),(r,1,2))
    check('noise_radial_cost',noise_radial==s.Rational(1,30))
    check('full_sky_noise_cost',s.simplify(C*s.Rational(1,30)/(4*s.pi)-1/(168*s.pi))==0)
    # Smearing a quadratic smooth growth verifies separate signal smoothing; toy input only.
    t=s.symbols('t',real=True)
    averaged=s.integrate(chi*(t+tau*x)**2,(x,-1,1))
    check('smearing_changes_signal',s.simplify(averaged-t*t-tau*tau/7)==0)
    # Exact continuity identity behind a derivative remainder bound.
    beta,m,P,pv,slow=s.symbols('beta m P pv slow',real=True)
    qv=slow+beta*pv; pi=pv+( -2 if fault=="wrong_frame_derivative" else 2)*beta*m*P
    njdot=qv+3*P-3*beta*pi
    check('density_derivative_identity',s.expand(njdot-(slow-2*beta*pv+3*(1-2*beta*beta*m)*P))==0)
    check('healthy_beta_coefficient',s.simplify((3*(1-2*beta*beta*m)).subs(m,1/(6*beta*beta)))==2)
    moment=s.integrate(x*chi,(x,0,1))*2
    check('response_absolute_first_moment',moment==s.Rational(5,16))
    # Exact normalized taper Euler equation and equality case; delta=1 fixture only.
    sol=(-r**3+(8 if fault=="wrong_taper_coefficient" else 7)*r-6)/6
    Z=s.integrate(r*sol,(r,1,2))
    check('optimal_taper_euler',-s.diff(sol,r,2)==r)
    check('optimal_taper_boundary',sol.subs(r,1)==0 and sol.subs(r,2)==0)
    check('optimal_taper_green_energy',s.integrate(s.diff(sol,r)**2,(r,1,2))==Z)
    check('optimal_taper_normalized',s.integrate(r*sol/Z,(r,1,2))==1)
    check('optimal_taper_equality',s.integrate(s.diff(sol/Z,r)**2,(r,1,2))==1/Z)
    check('optimal_taper_positive',s.simplify(sol+(r-2)*(r-1)*(r+3)/6)==0)
    return checks

baseline=evaluate()
assert all(baseline.values()),[n for n,v in baseline.items() if not v]
faults={}
for name in ['wrong_solid_angle','wrong_radial_jacobian','omit_endpoint_jumps','ignore_angular_gradient','missing_temporal_normalization','missing_noise_volume_jacobian','wrong_frame_derivative','wrong_taper_coefficient']:
    result=evaluate(name)
    faults[name]=[n for n,v in result.items() if not v]
    assert faults[name], 'undetected fault '+name
stem='k2319-lightcone-density-readout'
deps=[f'explorations/conditional-build/{stem}-2026-10-30.md',str(Path(__file__).relative_to(ROOT)),'explorations/conditional-build/k2311-uniform-constrained-dust-evolution-2026-10-30.md','explorations/conditional-build/k2314-windowed-dust-observables-2026-10-30.md','explorations/conditional-build/k2317-spacetime-dust-windows-2026-10-30.md','explorations/conditional-build/k2308-inhomogeneous-constrained-dust-transfer-2026-10-30.md']
data=dict(schema_version='1.0',result_id='K2319',checks=len(baseline),check_names=list(baseline),mutation_failed_checks=faults,evidence_kind='exact symbolic shell, radial/angle weak derivative and noise-dilation controls; continuum iff and dominated-convergence proofs in note; no sampled convergence certification',dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},details={'uncut_leading_taper_variance':'2*pi**2/3','coordinate_white_noise_full_sky_fixture':'sigma**2/(168*pi*tau)','spectrum':'supplied continuum; bounded IR-cut white UV'})
out=ROOT/'lab/process'/f'{stem}.json'
if '--write' in sys.argv: out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
else: assert json.loads(out.read_text())==data
print(json.dumps({'result':'K2319','checks':len(baseline),'faults':len(faults)}))
