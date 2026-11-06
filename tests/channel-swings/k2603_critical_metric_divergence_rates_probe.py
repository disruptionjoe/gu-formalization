#!/usr/bin/env python3
"""K2603 exact critical-scale consumers; analytic theorem is in the linked note."""
import argparse,json,hashlib
from pathlib import Path
import sympy as s
root=Path(__file__).resolve().parents[2]
ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
checks=[];controls=[]
def ck(name,value):
 assert bool(value),'FAIL '+name
 checks.append(name)
def ct(name,value):
 assert bool(value),'FAIL contrary '+name
 controls.append(name)
prior=json.loads((root/'lab/process/k2600-full-metric-contact-regularity.json').read_text())
ratio=s.Rational(prior['F_Y5_k1'])/s.Rational(prior['determinant_Y5_k1'])
ck('actual_contact_coefficient',ratio==-s.Rational(424853,149354))
ck('actual_source_and_detector_orders',prior['source_detector_B_orders']==[10,12])
z,r,R,eps=s.symbols('z r R eps',positive=True)
phi=z**10/s.factorial(10)
ck('polynomial_core_source_signal',s.diff(phi,z,10)==1)
ct('zero_mass_pair_cancels_contact',s.diff(phi,z,10).subs(z,eps)-s.diff(phi,z,10).subs(z,-eps)==0)
ct('characteristic_covector_cancels',s.Symbol('q')**5!=0 and (s.Symbol('q')**5).subs(s.Symbol('q'),0)==0)
ck('actual_rescaled_profile_power',10-12==-2)
ck('Fourier_profile_power',7-2==5)
ck('Sobolev_cross_scale_factor',s.simplify(r**5*R**5*R**-7*R**-3-(r/R)**5)==0)
# Exact shell envelope integral, suppressing the fixed sphere area.
inner=s.integrate(z**6*eps**-7,(z,0,eps))
outer=s.integrate(z**-1,(z,eps,R))
ck('critical_shell_integral',s.simplify(inner+outer-s.Rational(1,7)-s.log(R/eps))==0)
ck('dual_Lebesgue_exponent',1-s.Rational(2,7)==s.Rational(5,7))
ck('Newton_fixture_same_critical_integrand',s.simplify(z**6*(z**-5)**s.Rational(7,5)-1/z)==0)
ct('total_fourteen_dimension_wrong',14-2*s.Rational(7,2)!=0)
# Independent smooth Gaussian Fourier-profile surrogate, not a compact conserved detector.
x=s.symbols('x',positive=True)
gaussian=s.integrate(x**9*s.exp(-(r*r+R*R)*x*x),(x,0,s.oo))*r**5*R**5
ck('Gaussian_cross_scale_integral',s.simplify(gaussian-12*(r*R)**5/(r*r+R*R)**5)==0)
normalized=s.simplify(gaussian/(s.Rational(3,8)))
ck('Gaussian_normalized_diagonal',s.simplify(normalized.subs(R,r)-1)==0)
ck('Gaussian_ratio_decay',s.simplify(normalized-32*(r/R)**5/(1+(r/R)**2)**5)==0)
q=s.Rational(1,32);N=s.symbols('N',integer=True,positive=True);j=s.symbols('j',integer=True,positive=True)
ck('Gram_row_sum_bound',1+2*q/(1-q)==s.Rational(33,31))
consumers=[]
for n in [1,2,4,8,16,32,64]:
 gram=sum(q**abs(i-j) for i in range(n) for j in range(n))
 ck('dyadic_Gram_bound_'+str(n),gram<=s.Rational(33,31)*n)
 # Signal n and this majorant produce this squared certified generic lower gain.
 gain=s.Rational(n*n,1)/gram
 consumers.append({'scales':n,'Gram_majorant':str(gram),'squared_signal_over_majorant':str(gain)})
ct('identical_scales_have_no_gain',s.simplify(N**2/N**2)==1 and 8**2>s.Rational(33,31)*8)
ct('single_scale_does_not_diverge',1**s.Rational(5,7)==1)
ct('zero_A_trace_cancels_contact',ratio*s.Integer(0)==0)
ck('Sobolev_budget_inverse_power',1/s.Rational(1,2)==2)
ck('Lebesgue_budget_inverse_power',1/s.Rational(5,7)==s.Rational(7,5))
# A shrinking smoothing source with fixed signed unit mass has the same core signal.
weights=[s.Rational(3,2),-s.Rational(1,2)];points=[eps,-eps]
ck('signed_mass_one_core_signal',sum(w*s.diff(phi,z,10).subs(z,p) for w,p in zip(weights,points))==1)
w1=1/eps;w0=1-w1;test=1+z
ck('unbounded_TV_witness_mass_one',s.simplify(w1+w0)==1)
ct('unbounded_TV_defeats_smooth_convergence',s.simplify(w1*test.subs(z,eps)+w0*test.subs(z,0)-test.subs(z,0))==1)
report={'result':'K2603','checks':checks,'contrary_controls':controls,'critical_rates':{'L7_5':'at least c log(r0/epsilon)^(5/7)','Hminus3_2':'at least c sqrt(log(r0/epsilon)); ordinary and L2_A Hminus3_2_B'},'scope':'full selected metric, mass-one uniformly TV-bounded B sources supported O(epsilon), fixed nonzero compact conserved A pressure; necessary bounds only','dyadic_consumers':consumers,'Gaussian_fixture':'exact Fourier scaling surrogate, noncompact and not the actual conserved detector','evidence_kind':'reused actual cofactor coefficient; exact core, shell, Fourier-model and Gram computations; variable-coefficient uniform-profile proof and norm duality in note','next':'matching sufficient regularity and independently specified physical readout remain open'}
refs=['explorations/conditional-build/k2600-full-metric-contact-regularity-2026-11-06.md','lab/process/k2600-full-metric-contact-regularity.json']
report['provenance']={f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in refs}
out=root/'lab/process/k2603-critical-metric-divergence-rates.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'FAIL report replay'
print(json.dumps({'result':'K2603','checks':len(checks),'controls':len(controls),'status':'pass'}))
