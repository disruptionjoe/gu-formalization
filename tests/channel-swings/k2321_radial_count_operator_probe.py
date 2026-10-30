"""Exact fixtures for the fixed-cone count operator; continuum proof in note."""
from pathlib import Path
import json,hashlib,sys
import sympy as s
ROOT=Path(__file__).resolve().parents[2]

def evaluate(fault=None):
    checks={}
    def ck(n,v):checks[n]=bool(v)
    e=s.symbols('e');P,Q,n,V,b,chi=s.symbols('P Q n V b chi',real=True)
    det=1+e*(P-3*Q);ut=1-e*P
    flux=s.expand(det*((1+e*n)*ut+(1 if fault!='reverse_flux_velocity' else -1)*e*V)).coeff(e,1)
    ck('current_flux',s.expand(flux-(n-3*Q+V))==0)
    frame=flux.subs({n:n-3*b*chi,Q:P-b*chi},simultaneous=True)
    ck('frame_cancellation',s.expand(frame-(n-3*P+V))==0)
    ck('lapse_cancels',s.diff(flux,P)==0)
    r,th,ph=s.symbols('r th ph',positive=True);d=s.Function('d')(r,th,ph)
    smap=r+e*d
    mat=s.Matrix([smap,th,ph]).jacobian([r,th,ph]);jac=smap**2/r**2*mat.det()
    ck('angular_triangular_det',s.expand(mat.det()-(1+e*s.diff(d,r)))==0)
    ck('radial_area',s.expand(jac).coeff(e,1)==s.diff(d,r)+2*d/r)
    power=s.Integer(2);disp=r*r
    # Exact density ratio at displaced coordinate; p=2 fixture is algebraic.
    area=(r+e*disp)**(0 if fault=='omit_area' else 2)/r**(0 if fault=='omit_area' else 2)
    sel=1 if fault=='omit_selection' else r**power/(r+e*disp)**power
    contrast=s.diff(sel/(area*(1+e*s.diff(disp,r))),e).subs(e,0)
    ck('selected_count_fixture',s.simplify(contrast+(power+4)*r)==0)
    post=s.diff(1/( ((r+e*disp)/r)**2*(1+e*s.diff(disp,r))),e).subs(e,0)
    ck('post_map_selection',s.simplify(post+4*r)==0)
    t,t0=s.symbols('t t0');field=t*r
    cone=(s.diff(field,r) if fault=='partial_only' else s.diff(field,r)-s.diff(field,t)).subs(t,t0-r)
    ck('cone_chain_rule',s.simplify(cone-(t0-2*r))==0)
    k,mu,c=s.symbols('k mu c',real=True);radial=s.I*mu*c*s.exp(s.I*k*r*mu)
    principal=s.expand((-1 if fault!='reverse_rsd' else 1)*s.diff(radial,r)/s.exp(s.I*k*r*mu))
    ck('fourier_rsd_sign',s.simplify(principal-k*c*mu**2)==0)
    # Actual healthy designer background, no quadratic-F substitution.
    x,A,p=s.symbols('x A p',positive=True);F=1-A*x**(-p)
    H=x**s.Rational(3,2)*(1-A*(1+p/2)*x**(-p))/F**s.Rational(3,2)
    u=-s.sqrt(s.Rational(3,2))*A*p*x**(s.Rational(3,2)-p)/F**s.Rational(3,2)
    beta=(1 if fault=='wrong_beta' else -1)/s.sqrt(6)
    h=s.simplify(H+beta*u)
    ck('jordan_expansion',s.simplify(h-x**s.Rational(3,2)/s.sqrt(F))==0)
    ck('conformal_expansion',s.simplify(s.sqrt(F)*h/x-s.sqrt(x))==0)
    delta=s.symbols('delta',positive=True);cc=s.symbols('cc',positive=True)
    v=s.Matrix([s.Rational(1,3),s.Rational(2,3),s.Rational(2,3)]);Am=delta*s.eye(3)+cc*v*v.T
    ck('unit_radial',v.dot(v)==1)
    ck('radial_eigen',Am*v==(delta+cc)*v)
    tangent=s.Matrix([-2,1,0]);ck('tangent_eigen',Am*tangent==delta*tangent)
    lam=s.symbols('lam');ck('principal_charpoly',s.factor(Am.charpoly(lam).as_expr())==(lam-delta)**2*(lam-delta-cc) or s.expand(Am.charpoly(lam).as_expr()-(lam-delta)**2*(lam-delta-cc))==0)
    ck('wrong_sign_degeneracy',(delta*s.eye(3)-delta*v*v.T).det()==0)
    # Radial specialization of the exact double divergence, including lower terms.
    dd=s.Function('delta')(r);cx=s.Function('c')(r);w=s.Function('w')(r)
    direct=-s.diff(dd*w,r,2)-2*s.diff(dd*w,r)/r-s.diff(cx*w,r,2)-4*s.diff(cx*w,r)/r-2*cx*w/r**2
    bb=s.diff(dd,r)+s.diff(cx,r)+2*cx/r
    split=-s.diff(r*r*((dd+cx)*s.diff(w,r)+bb*w),r)/r**2
    ck('elliptic_divergence_split',s.simplify(direct-split)==0)
    taper=(r-1)*(2-r)
    ck('taper_endpoints',taper.subs(r,1)==taper.subs(r,2)==0)
    ck('taper_energy',s.integrate(s.diff(taper,r)**2,(r,1,2))==s.Rational(1,3))
    ck('positive_taper',taper.subs(r,s.Rational(3,2))>0)
    ww=(r-1)**2*(2-r)**2;zz=1+r
    forward=-s.diff(zz,r)-(2+power)*zz/r
    adj=s.diff(ww,r)-(0 if fault=='wrong_noise_adjoint' else power)*ww/r
    ck('noise_adjoint',s.integrate(r*r*ww*forward,(r,1,2))==s.integrate(r*r*adj*zz,(r,1,2)))
    ck('displacement_noise_nonzero',s.integrate(r*r*adj*adj,(r,1,2))>0)
    ss,tau=s.symbols('ss tau',positive=True);response=s.Rational(3,4)*(1-ss**2)
    ck('response_normalized',s.integrate(response,(ss,-1,1))==1)
    ck('response_noise',s.integrate(response**2,(ss,-1,1))==s.Rational(3,5))
    ck('response_scaling',s.integrate((s.Rational(3,4)*(1-(ss/tau)**2)/tau)**2,(ss,-tau,tau))==s.Rational(3,5)/tau)
    # Finite shared-seed covariance; not continuum certification.
    D=s.Matrix([[1,2,0],[2,-1,1]]);R=s.Matrix([[2,1,1],[-1,3,0]]);cov=s.diag(1,2,3)
    B=D+R;full=B*cov*B.T
    supplied=D*cov*D.T+R*cov*R.T if fault=='independent_fake_seeds' else full
    ck('shared_covariance',supplied==s.Matrix([[30,18],[18,12]]))
    ck('covariance_positive',full.det()>0 and full[0,0]>0)
    ck('cross_terms_matter',full!=D*cov*D.T+R*cov*R.T)
    return checks
base=evaluate();assert all(base.values()),[n for n,v in base.items() if not v]
faults={}
for f in ['reverse_flux_velocity','omit_area','omit_selection','partial_only','reverse_rsd','wrong_beta','wrong_noise_adjoint','independent_fake_seeds']:
    out=evaluate(f);bad=[n for n,v in out.items() if not v];assert bad,'undetected '+f;faults[f]=bad
stem='k2321-radial-count-operator';deps=[f'explorations/conditional-build/{stem}-2026-10-30.md',str(Path(__file__).relative_to(ROOT))]+[f'explorations/conditional-build/{x}-2026-10-30.md' for x in ['k2319-lightcone-density-readout','k2311-uniform-constrained-dust-evolution','k2308-inhomogeneous-constrained-dust-transfer','k2305-regular-constrained-matter-transfer']]
data=dict(schema_version='1.0',result_id='K2321',checks=len(base),check_names=list(base),mutation_failed_checks=faults,evidence_kind='exact symbolic identities and finite covariance controls; continuum elliptic/Gaussian domain proof is in note',dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},details={'current':'n_J-3*Psi_J+V_r=n-3*Phi+V_r','principal':'k*(delta+c*mu**2), delta>0,c>0','domain':'zero-extended compact-annular window H1(R3)','scope':'fixed coordinate cone, Doppler radial map; not full relativistic observed counts'})
out=ROOT/'lab/process'/f'{stem}.json'
if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==data
print(json.dumps({'result':'K2321','exact':len(base),'faults':len(faults)}))
