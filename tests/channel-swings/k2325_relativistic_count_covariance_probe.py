"""Exact kinematic and covariance controls; continuum proof is in K2325."""
from pathlib import Path
import sympy as s
import json,hashlib,sys
ROOT=Path(__file__).resolve().parents[2]
def evaluate(fault=None):
 c={}
 def ck(n,x): c[n]=bool(x)
 ep,Psi,Phi,dn,V=s.symbols('ep Psi Phi dn V',real=True)
 # First order determinant and lapse normalization independently assembled.
 sq=(1+ep*(Phi-3*Psi));u=(1-ep*Phi)
 if fault=='lapse_sign':u=1+ep*Phi
 ck('current_lapse_cancels',s.expand(s.diff(sq*u*(1+ep*dn),ep).subs(ep,0)-(dn-3*Psi))==0)
 ck('spatial_flux_sign',s.det(s.Matrix([[1,-ep*V],[1,1]])).diff(ep)==V)
 r=s.symbols('r',positive=True);dr=s.Function('dr')(r)
 jac=(r+ep*dr)**2/r**2*(1+ep*s.diff(dr,r))
 ck('radial_jacobian',s.simplify(s.diff(jac,ep).subs(ep,0)-(s.diff(dr,r)+2*dr/r))==0)
 Z,I,H,Hdot=s.symbols('Z I H Hdot',nonzero=True)
 disp=-(Z/H)+I if fault!='redshift_sign' else Z/H+I
 ck('null_displacement',s.expand(disp+Z/H-I)==0)
 # Cone derivative includes H derivative -Hdot and both potential derivatives.
 Pr,Pt,Qr,Qt,Vr,Vt,Wt=s.symbols('Pr Pt Qr Qt Vr Vt Wt')
 DZ=-Pr+Pt+Vr-Vt-(Pt+Qt)
 ck('cone_redshift_euler',s.expand(DZ.subs(Vt,-H*V-Pr)-(Vr+H*V-Qt))==0)
 DH=-Hdot if fault!='spatial_cone_mix' else Hdot
 Ddisp=-(Vr+H*V-Qt)/H+Z*DH/H**2+Phi+Psi
 full=dn-3*Psi+V+Ddisp+2*disp/r
 target=dn-Vr/H+Qt/H+Phi-2*Psi-(Hdot/H**2+2/(r*H))*Z+2*I/r
 ck('expanded_count',s.simplify(full-target)==0)
 w=s.Function('w')(r);E=s.Function('E')(r)
 lhs=r**2*w*(s.diff(E,r)+2*E/r)
 rhs=s.diff(r**2*w*E,r)-r**2*s.diff(w,r)*E
 if fault=='adjoint_extra_area':rhs-=2*r*w*E
 ck('radial_adjoint',s.simplify(lhs-rhs)==0)
 mu=s.symbols('mu',real=True);Y=s.legendre(2,mu)
 aberr=-(1-mu**2) if fault!='aberration_sign' else 1-mu**2
 ck('aberration_divergence',s.diff(aberr,mu)==2*mu)
 ck('quadrupole_monopole_zero',s.integrate(Y,(mu,-1,1))==0)
 ck('quadrupole_dipole_zero',s.integrate(mu*Y,(mu,-1,1))==0)
 ck('quadrupole_norm',s.integrate(2*s.pi*5/(4*s.pi)*Y**2,(mu,-1,1))==1)
 F=30*(r-1)**2*(2-r)**2
 ck('annular_fixture_H1',all(s.diff(F,r,j).subs(r,b)==0 for j in [0,1] for b in [1,2]))
 ck('fixture_mass',s.integrate(F,(r,1,2))==1)
 # Source-integrated time-delay weight is bounded, lens retains a 1/s pole.
 z=s.symbols('z',positive=True);M=s.integrate(F,(r,1,2));L=s.integrate(F/r,(r,1,2))
 lens=M/z-L;bounded=-s.integrate(r**2*s.diff(F/r**2,r),(r,1,2))
 ck('lens_singular_moment',s.limit(z*lens,z,0)==1)
 ck('delay_weight_bounded',s.limit(z*bounded,z,0)==0)
 x=s.symbols('x',positive=True)
 ck('foreground_remainder_L2',s.integrate(s.log(x)**2/x**2,(x,1,s.oo))==2)
 ck('cross_variance_sublinear',s.limit(s.sqrt(x)/x,x,s.oo)==0)
 # Strict tail thresholds use actual radial powers, plus explicit boundary tests.
 power_shift=0 if fault!='drop_radial_measure' else -2
 for label,power,threshold in [('lens',0,s.Rational(1,2)),('kinetic',2,s.Rational(3,2)),('density',4,s.Rational(5,2))]:
  q=threshold+s.Rational(1,2)
  ck(label+'_finite',s.integrate(x**(power+power_shift-2*q),(x,1,s.oo))==1)
  q=threshold
  ck(label+'_borderline',s.integrate(x**(power+power_shift-2*q),(x,1,s.oo)) is s.oo)
 ck('finite_energy_rough_density',s.integrate(x**-2,(x,1,s.oo))==1 and s.integrate(1,(x,1,s.oo)) is s.oo)
 ck('positive_density_coefficient',s.Rational(2,3)>0)
 k=s.symbols('k',positive=True);P=(1+k*k)**-3
 ck('colored_positive',P.is_positive)
 ck('colored_kinetic',s.integrate(k**2*P,(k,0,s.oo))==s.pi/16)
 ck('colored_density',s.integrate(k**4*P,(k,0,s.oo))==3*s.pi/16)
 # Full seed covariance keeps cross terms, not independent field noises.
 B=s.Matrix([[1,2],[2,1]]);G=s.Matrix([[2,-1],[1,3]]);Q=s.diag(2,3)
 actual=(B+G)*Q*(B+G).T if fault!='split_seed' else B*Q*B.T+G*Q*G.T
 ck('shared_covariance',actual==s.Matrix([[21,30],[30,66]]))
 ck('positive_covariance',actual.det()>0)
 return c
base=evaluate();assert all(base.values()),[k for k,v in base.items() if not v]
faults={}
for f in ['lapse_sign','redshift_sign','spatial_cone_mix','adjoint_extra_area','aberration_sign','drop_radial_measure','split_seed']:
 bad=[k for k,v in evaluate(f).items() if not v];assert bad,'undetected '+f;faults[f]=bad
stem='k2325-relativistic-count-covariance';deps=[f'explorations/conditional-build/{stem}-2026-10-30.md',str(Path(__file__).relative_to(ROOT))]+[f'explorations/conditional-build/{v}-2026-10-30.md' for v in ['k2323-born-lensing-observer-domain','k2321-radial-count-operator','k2311-uniform-constrained-dust-evolution']]
out=dict(schema_version='1.0',result_id='K2325',checks=len(base),check_names=list(base),mutation_failed_checks=faults,evidence_kind='exact symbolic current, cone, adjoint, harmonic, spectral-power and finite covariance controls; uniform continuum statements rely on written proofs',dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},details={'scope':'volume-limited conserved dust with supplied Jordan null photons and seed','quadrupole_tail':'-8pi p(0) M2 Y20/k plus L2','covariance_thresholds':{'quadrupole_q':'1/2','kinetic_q':'3/2','point_density_q':'5/2'},'strict_thresholds':True,'native_GU_credit':False})
p=ROOT/'lab/process'/f'{stem}.json'
if '--write' in sys.argv:p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
else:assert json.loads(p.read_text())==out
print(json.dumps({'result':'K2325','exact':len(base),'faults':faults}))
