"""Exact sharp actual-memory preparation bounds and conditional decoder consumers."""
from pathlib import Path
import json,hashlib,sys
import sympy as s
from flint import arb,ctx
ctx.prec=256
ROOT=Path(__file__).resolve().parents[2]
checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ctrl(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
q=s.symbols('q',positive=True);x=s.symbols('x',real=True);y=s.symbols('y',positive=True)
f=(q+s.sqrt(4*q-3*q*q))/2
ck('sharp_root_equation',s.simplify(f*f-q*f-q*(1-q))==0)
ck('concavity_exact',s.simplify(s.diff(f,q,2)+2/(4*q-3*q*q)**s.Rational(3,2))==0)
ck('endpoints',f.subs(q,0)==0 and f.subs(q,1)==1)
g=(1+y-s.sqrt(1+2*y-3*y*y))/2
ck('inverse_quadratic',s.simplify(g*g-(1+y)*g+y*y)==0)
ck('stable_inverse',s.simplify(g-2*y*y/(1+y+s.sqrt(1+2*y-3*y*y)))==0)
# Complete input/reference basis; memory is the final tensor factor.
phi=s.Matrix([1,0,0,1])/s.sqrt(2);phip=s.Matrix([1,0,0,-1])/s.sqrt(2);e0=s.Matrix([1,0]);e1=s.Matrix([0,1]);P=phi*phi.T
v=s.Rational(4,5)*s.kronecker_product(phi,e0)+s.Rational(3,5)*s.kronecker_product(phip,e1);rho=v*v.T
ptrA=s.Matrix(4,4,lambda i,j:sum(rho[2*i+k,2*j+k] for k in range(2)))
ptrM=s.Matrix(2,2,lambda i,j:sum(rho[2*k+i,2*k+j] for k in range(4)))
ck('joint_state_normalized_positive',s.trace(rho)==1 and rho*rho==rho)
ck('joint_infidelity',s.simplify(1-s.trace(P*ptrA))==s.Rational(9,25))
ck('actual_memory_marginal',ptrM==s.diag(s.Rational(16,25),s.Rational(9,25)))
delta=rho-s.kronecker_product(P,ptrM);ev=delta.eigenvals();want={(9+3*s.sqrt(73))/50:1,(9-3*s.sqrt(73))/50:1,-s.Rational(9,25):1,s.Integer(0):5}
ck('original_eight_dimensional_spectrum',ev==want)
actual=(9+3*s.sqrt(73))/50
ck('sharp_bound_attained',s.simplify(actual-f.subs(q,s.Rational(9,25)))==0)
ctrl('free_memory_bound_wrong_for_actual_memory',actual>s.Rational(3,5))
ctrl('linear_infidelity_bound_wrong',actual>s.Rational(9,25))
free=rho-s.kronecker_product(P,e0*e0.T)
ck('free_memory_projection_distance',free.eigenvals()=={s.Rational(3,5):1,-s.Rational(3,5):1,s.Integer(0):6})
# Symbolic 3D effective difference; no sampling-only proof of sharpness.
a=s.symbols('a',real=True);b=s.symbols('b',real=True)
D=s.Matrix([[a*a-x,a*b,0],[a*b,b*b,0],[0,0,-(1-x)]])
lam=s.symbols('lam');poly=s.expand(D.charpoly(lam).as_expr()).subs(a*a,1-q).subs(b*b,q)
expected=(lam+1-x)*(lam*lam-(1-x)*lam-q*x)
ck('free_memory_characteristic_polynomial',s.simplify(poly-expected)==0)
# Certify monotonicity by (1-x)^2+4qx - (1-x-2q)^2=4q(1-q)>0.
ck('free_memory_minimum_at_projection',s.expand((1-x)**2+4*q*x-(1-x-2*q)**2-4*q*(1-q))==0)
# Exact state with pure A is factorized; marginals alone do not certify this.
I2=s.eye(2)/2;prod=s.kronecker_product(I2,I2)
product_fixture=s.kronecker_product(P,ptrM)
ck('perfect_preparation_product_fixture',s.kronecker_product(P,s.eye(2))*product_fixture==product_fixture and s.Matrix(4,4,lambda i,j:sum(product_fixture[2*i+k,2*j+k] for k in range(2)))==P)
ctrl('input_marginal_does_not_determine_joint_fidelity',s.trace(P*prod)==s.Rational(1,4))
# Conditional selection control: a rare announced bad history has error one.
rare=s.Rational(1,1000)
history=(1-rare)*s.kronecker_product(P,e0*e0.T)+rare*s.kronecker_product(phip*phip.T,e1*e1.T)
observed_infidelity=s.simplify(s.trace(s.kronecker_product(s.eye(4)-P,s.eye(2))*history))
selector=s.kronecker_product(s.eye(4),e1*e1.T);selected=selector*history*selector/rare
conditional_infidelity=s.simplify(s.trace(s.kronecker_product(s.eye(4)-P,s.eye(2))*selected))
ctrl('unconditional_fidelity_does_not_bound_selected_history',observed_infidelity==rare and s.trace(selected)==1 and conditional_infidelity==1)
ck('conditional_average_allowance_example',s.Rational(3,4)*f.subs(q,0)+s.Rational(1,4)*f.subs(q,1)==s.Rational(1,4))
ck('Jensen_example',f.subs(q,s.Rational(1,4))>s.Rational(1,4))
# Exact two-use memory countercontrol; each one-use output is maximally mixed.
shared=s.diag(s.Rational(1,2),0,0,s.Rational(1,2));independent=s.eye(4)/4
ck('two_use_states_CPTP_outputs',s.trace(shared)==s.trace(independent)==1)
ck('identical_one_use_marginals',s.Matrix(2,2,lambda i,j:sum(shared[2*i+k,2*j+k] for k in range(2)))==I2)
ctrl('single_use_does_not_certify_process',sum(abs(z)*m for z,m in (shared-independent).eigenvals().items())/2==s.Rational(1,2))
# Nearly pure memory cannot use the fixed-pure-reference bound for both actual marginals.
qmem=s.Rational(1,25);vmem=s.Matrix([s.sqrt(1-qmem),0,0,s.sqrt(qmem)]);rm=vmem*vmem.T
marg=s.diag(1-qmem,qmem);dm=rm-s.kronecker_product(marg,marg)
memdist=s.simplify(sum(abs(z)*mul for z,mul in dm.eigenvals().items())/2)
ck('actual_marginal_product_schmidt_distance',s.simplify(memdist-qmem*(1-qmem)-s.sqrt(qmem*(1-qmem)))==0)
ctrl('pure_memory_reference_is_not_actual_marginal',memdist>f.subs(q,qmem))
ck('corrected_near_pure_memory_allowance',memdist<f.subs(q,qmem)+s.sqrt(qmem))
# A stochastic full reset produces a product including any retained reference.
reset_kraus=[s.kronecker_product(s.eye(4),e0*e.T) for e in [e0,e1]]
ck('reset_Kraus_trace_preserving',sum((k.T*k for k in reset_kraus),s.zeros(8))==s.eye(8))
reset=sum((k*rho*k.T for k in reset_kraus),s.zeros(8))
ck('exact_reset_decouples_correlated_input',reset==s.kronecker_product(ptrA,e0*e0.T))
ck('telescoping_error_example',sum([s.Rational(1,100)+s.Rational(1,200)]*4)==s.Rational(3,50))
# Rigorous budget consumers. Numbers are sufficient, prospective and use an upper C.
Cb=2*(1+arb(2).sqrt()/arb('0.0522306').sqrt());lg=arb(60).log();budgets=[]
for name,C,n in [('bad_previous',Cb,9000000),('good_previous',arb(2),170000),('bad_expanded',Cb,20000000)]:
 margin=(arb('0.01')/C)**2-lg/n
 ck(name+'_positive_margin',margin>0 and margin<1)
 ep=2*margin**2/(1+margin+(1+2*margin-3*margin**2).sqrt())
 # Choose a conservative simple input epsilon below the allowed enclosure.
 trial=arb('1e-16') if name=='bad_previous' else (arb('1e-13') if name=='good_previous' else arb('1e-14'))
 ck(name+'_selected_joint_infidelity_sufficient',trial<ep)
 ft=(trial+(4*trial-3*trial**2).sqrt())/2
 ck(name+'_distance_with_correlated_preparation',C*(lg/n+ft).sqrt()<arb('0.01'))
 budgets.append({'branch':name,'n':n,'C_upper_enclosure':str(C),'probability_margin':str(margin),'joint_infidelity_threshold':str(ep),'tested_sufficient_epsilon':str(trial)})
ctrl('bad_fixed_floor_not_removed_by_samples',Cb*((arb('1e-10')+(4*arb('1e-10')-3*arb('1e-10')**2).sqrt())/2).sqrt()>arb('0.01'))
deps=['lab/process/k2428-exact-recovery-uniqueness.json','lab/process/k2430-adaptive-decoder-certification.json','tests/channel-swings/k2430_adaptive_decoder_certification_probe.py']
prior=json.loads((ROOT/deps[1]).read_text());ck('prior_dependency_hashes',all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==v for p,v in prior['dependencies'].items()))
report={'result_id':'K2432','scope':'Sharp finite-dimensional actual-memory preparation decoupling; adaptive tested-average and explicitly uniform deployment consumers only; no measured calibration or GU recovery.','checks':checks,'controls':controls,'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},'actual_memory_bound':'(q+sqrt(4q-3q^2))/2','free_memory_bound':'sqrt(q)','sharp_fixture':{'q':'9/25','eigenvalues':['(9+3sqrt(73))/50','(9-3sqrt(73))/50','-9/25'],'distance':'(9+3sqrt(73))/50'},'budgets':budgets,'evidence_kinds':{'exact_algebra':'symbolic identities, exact spectra, CPTP state controls','rigorous_numerics':'Arb 256-bit sufficient preparation budgets','universal_proof':'purification, rank-one secular inequality, monotonic inverse, conditional contraction and uniform telescoping in note','not_supplied':'physical conditional fidelity, readout, full reset or deployment transfer evidence'}}
path=ROOT/'lab/process/k2432-bell-preparation-memory-decoupling.json'
if '--check' in sys.argv:ck('no_write_report_reproduction',json.loads(path.read_text())==report)
else:path.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2432',len(report['checks']),'checks',len(controls),'controls PASS')
print(json.dumps(budgets,indent=2))
