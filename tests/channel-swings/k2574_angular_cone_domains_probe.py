#!/usr/bin/env python3
"""Exact identities and supporting controls; universal derivations are in the note."""
import argparse,json,hashlib
from pathlib import Path
from fractions import Fraction as F
import sympy as s
root=Path(__file__).resolve().parents[2]
parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args()
checks=[];controls=[]
def ck(name,condition):
    assert bool(condition),'FAIL '+name
    checks.append(name)
def ct(name,condition):
    assert bool(condition),'FAIL contrary '+name
    controls.append(name)

c=s.Rational(120691003,77168);A=c+s.Rational(35,4)
z=s.symbols('z',nonnegative=True);V=A*z-s.Rational(3,4)*z/(1+z)
ck('actual_potential_derivative',s.factor(s.diff(V,z)-(A-s.Rational(3,4)/(1+z)**2))==0)
ck('positive_potential_derivative_lower',A-s.Rational(3,4)>0)
V0=V.subs(z,1);D=V.subs(z,4)
ck('near_potential',V0==s.Rational(121337285,77168))
ck('far_potential',D==s.Rational(606773239,96460))
ck('potential_monotone_endpoint',0<V0<D)
j=s.symbols('j',nonnegative=True)
def positive_coeffs(poly):return all(x>=0 for x in s.Poly(s.expand(poly),j).all_coeffs())
# Symbolic shifts prove these WHOLE polynomial families, not sampled frequencies.
ell=j+2;n=2*ell;L=ell*(ell+2)
ck('entire_elliptic_family',positive_coeffs(5*n*n-8*L))
n=j+46;ell=4*n;L=ell*(ell+2)
ck('entire_oscillatory_family',positive_coeffs(L/4-n*n-D))
L=s.Integer(200*202)
ck('actual_200_1_oscillatory_cone',1+D<L/4)
Tv=(L*s.Rational(3,10)+D-V0)/(L/4)
ck('actual_200_1_energy_exponent',Tv==s.Rational(6496787331,3896984000)<2)
jj=j+40;P0=s.Rational(7,2)*jj**2-5*jj+V0;Pd=-4*jj**2-8*jj+D
ck('whole_turning_family_near_positive',positive_coeffs(P0) and P0.subs(j,0)>0)
ck('whole_turning_family_far_negative',positive_coeffs(-Pd) and (-Pd).subs(j,0)>0)
ct('all_angular_positive_potential_false',Pd.subs(j,0)<0)
ck('variation_uniform_constant',4*s.Rational(3,10)+1==s.Rational(11,5))
# Energy derivative under the actual equation, with complex quadratures.
u,v,up,vp,q,qp=s.symbols('u v up vp q qp',real=True)
Edot=2*up*(-q*u)+2*vp*(-q*v)+qp*(u*u+v*v)+2*q*(u*up+v*vp)
ck('energy_derivative_identity',s.expand(Edot-qp*(u*u+v*v))==0)
ct('constant_energy_false_for_variable_potential',Edot.subs({u:1,v:0,up:0,vp:0,q:2,qp:1})==1)
fluxdot=(-q*v)*u+vp*up-(-q*u)*v-up*vp
ck('conserved_complex_flux',s.expand(fluxdot)==0)
k=s.symbols('k',positive=True)
E=up**2+vp**2+k*k*(u*u+v*v);flux=vp*u-up*v
fp=(up-k*v)**2+(vp+k*u)**2
fm=(up+k*v)**2+(vp-k*u)**2
ck('near_impedance_flux',s.expand(fp-E-2*k*flux)==0)
ck('far_impedance_flux',s.expand(fm-E+2*k*flux)==0)
ck('same_orientation_does_not_cancel_flux',s.expand(fp+fp-2*E-4*k*flux)==0)
x=s.symbols('x',real=True);wave=s.exp(-s.I*k*x)
ck('oscillatory_control_solves_ode',s.simplify(s.diff(wave,x,2)+k*k*wave)==0)
ct('wrong_same_sign_impedance_has_kernel',s.simplify(s.diff(wave,x)+s.I*k*wave)==0 and wave.subs(x,0)==1)
ct('correct_far_sign_detects_kernel',s.simplify(s.diff(wave,x)-s.I*k*wave)==-2*s.I*k*wave)
# Independent real Dirichlet resonance does not defeat the Cauchy estimate.
y=s.sin(k*x)
ck('resonance_near_value',y.subs(x,0)==0)
ck('resonance_far_value',s.simplify(y.subs(x,s.pi/k))==0)
ct('resonant_normal_datum_not_zero',s.diff(y,x).subs(x,0)==k)
ck('oscillatory_energy_fixture',s.simplify(s.diff(y,x)**2+k*k*y*y)==k*k)
# Positive comparison fixture and a matrix of actual boundary amplitudes.
B=s.sinh(k*(1-x))/s.sinh(k);T=s.sinh(k*x)/s.sinh(k)
ck('positive_comparison_equation',s.simplify(s.diff(B,x,2)-k*k*B)==0)
ck('positive_comparison_endpoints',B.subs(x,0)==1 and B.subs(x,1)==0 and T.subs(x,0)==0 and T.subs(x,1)==1)
ck('positive_basis_wronskian',s.simplify(B*s.diff(T,x)-s.diff(B,x)*T-k/s.sinh(k))==0)
ct('unrestricted_positive_cauchy_growth',s.sinh(10*s.log(2))>500)
# Fixed coordinate conversion has a genuine nonzero determinant, not identity.
J,Jt,st,n=s.symbols('J Jt st n',positive=True)
jet=s.Matrix([[J,0],[st*Jt/n,st*J]])
ck('physical_coordinate_jet_adapter',s.factor(jet.det())==st*J**2)
ct('drop_J_derivative_changes_jet',jet[1,0]!=0)
# Full-angular analytic consumer uses a POSITIVE auxiliary norm, not q energy.
r=s.symbols('r',real=True)
mat=s.Matrix([[0,1],[r,0]])
ck('full_angular_matrix_singular_squares',mat.T*mat==s.diag(r*r,1))
nf,Lf=s.symbols('nf Lf',nonnegative=True)
ck('full_angular_positive_potential_margin',s.expand((1+nf**2+Lf+D)-(nf**2+D))==1+Lf)
ck('full_angular_negative_potential_margin',s.expand((1+nf**2+Lf+D)-Lf)==1+nf**2+D)
nu,dd=s.symbols('nu dd',nonnegative=True)
ck('analytic_radius_separates_fixed_potential',s.expand((nu+s.sqrt(dd))**2-(nu**2+dd))==2*nu*s.sqrt(dd))
ct('turning_mode_not_omitted_by_positive_impedance',P0.subs(j,0)>0 and Pd.subs(j,0)<0 and 1+D>0)
ck('balanced_endpoint_auxiliary_flux',s.expand(fp+fm-2*E)==0)
# Endpoint identity and matrix bound are distinct from asserting an optimal rate.
ct('q_weight_not_positive_on_turning_near_end',(-P0).subs(j,0)<0)
# A genuine barrier/well comparison defeats unweighted interior control.
zbar=s.symbols('zbar',positive=True);edge=s.pi/(4*k)
inside=s.cos(k*x);outside=s.exp(-k*(x-edge))/s.sqrt(2)
ck('barrier_well_value_match',s.simplify(inside.subs(x,edge)-outside.subs(x,edge))==0)
ck('barrier_well_derivative_match',s.simplify(s.diff(inside,x).subs(x,edge)-s.diff(outside,x).subs(x,edge))==0)
ck('barrier_well_inside_equation',s.simplify(s.diff(inside,x,2)+k*k*inside)==0)
ck('barrier_well_outside_equation',s.simplify(s.diff(outside,x,2)-k*k*outside)==0)
boundary_norm2=s.simplify(2*(outside**2+s.diff(outside,x)**2/k**2).subs(x,edge+zbar))
ck('barrier_well_control_norm',s.simplify(boundary_norm2-2*s.exp(-2*k*zbar))==0)
ct('endpoint_flux_not_uniform_interior_bound',s.simplify(boundary_norm2.subs({k:10,zbar:s.log(2)}))==s.Rational(1,524288))
report={'result':'K2574','evidence_kind':'exact polynomial-family and energy/flux identities plus finite comparison and adverse controls; comparison/domain proofs in note','checks':checks,'contrary_controls':controls,'actual_constants':{'c':str(c),'A':str(A),'V0':str(V0),'D':str(D),'theta200_variation_upper':str(Tv)},'ceiling':'two disjoint Sobolev cones and all-angular analytic impedance preparation; no general Sobolev inverse or physical selection'}

refs=['k2572-boundary-preparation-robustness']
report['provenance']={'explorations/conditional-build/'+f+'-2026-11-05.md':hashlib.sha256((root/('explorations/conditional-build/'+f+'-2026-11-05.md')).read_bytes()).hexdigest() for f in refs}
out=root/'lab/process/k2574-angular-cone-domains.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved report mismatch'
print(json.dumps({'result':'K2574','checks':len(checks),'controls':len(controls),'status':'pass'}))
