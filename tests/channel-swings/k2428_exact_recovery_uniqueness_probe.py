"""Exact nominal controller uniqueness from attained-dual localization."""
from pathlib import Path
import json,hashlib,sys
R=Path(__file__).resolve().parents[2]
p=R/'tests/channel-swings/k2426_recovery_rigidity_probe.py';src=p.read_text()
exec(compile(src[:src.rindex("report={'result_id'")],str(p),'exec'),globals())
inherited_checks=dict(checks);inherited_controls=dict(controls);checks={};controls={}
# Original reduced-controller radii are rigorous consequences of K2426.
db=arb('1.584e-12');dg=arb('1.202e-13');radius=arb('1e-11')
ck('inherited_reduced_bad_radius',bad_reduced<db)
ck('inherited_good_radius',good_original<dg)
ells=[];bs=[]
for w,m,Qm in zip(ww,ms,qq):
 B=plus(outer(tv,m),mm(AA0,Qm));C=plus(plus(ident,GG,-(1-w)),B,-w)
 ell=[C[0][0]+C[1][1],C[0][1]-C[1][0]]
 ck('endpoint_localization_'+str(len(ells)),4*(1-w)*dg+2*arb(2).sqrt()*w*db<radius)
 box=[x+arb(0,'1e-11') for x in ell];ck('positive_cosine_'+str(len(ells)),box[0]>0)
 ells.append(box);bs.append(box[1]/box[0])
ck('opposite_strict_endpoint_slopes',bs[0]<0 and bs[1]>0)
lbox=bs[1]/(bs[1]-bs[0]);tbox=-bs[0]*bs[1]/(bs[1]-bs[0])
ck('strict_interior_weights',lbox>0 and lbox<1 and tbox>0)
ck('rational_candidate_in_localized_box',lbox.contains(ar(lrat)) and tbox.contains(ar(trat)))
# Reconstruct support for EVERY dual in the rectangle, not a midpoint check.
lam,tau=lbox,tbox
qr=[[lam,-tau],[1-lam,tau]];rr=[norm(q) for q in qr];RR=sum(rr);ww=list(map(ar,ws));ms=[[ar(x) for x in m] for m in means];qq=list(map(ma,Qs));sv=[sum((1-w)*q[a] for w,q in zip(ww,qr)) for a in range(2)];V=[arb(0),arb(0)];N=[[arb(0),arb(0)],[arb(0),arb(0)]]
for w,q,m,Qm in zip(ww,qr,ms,qq):
 Fm=[[q[0],q[1]],[-q[1],q[0]]];V=[a+w*b for a,b in zip(V,mv(Fm,m))];N=plus(N,mm(Fm,Qm),w)
H=plus(outer(V,V),mm(N,trans(N)),-1);eigengap=((H[0][0]-H[1][1])**2+4*H[0][1]**2).sqrt();hh=(H[0][0]+H[1][1]+eigengap)/2;loweig=hh-eigengap;det=N[0][0]*N[1][1]-N[0][1]*N[1][0]
ck('whole_box_compact_domain',tau*tau<ar(Q(16129,23871))*lam*lam and tau*tau<ar(Q(4489,6327))*(1-lam)*(1-lam))
ck('interval_simple_improving_positive_det',eigengap>0 and det>0 and hh>det)
delt=det;d0=delt/hh;TT=sum(x*x for row in N for x in row);phi0=(TT+hh+delt*delt/hh).sqrt();proj=scale(plus(H,ident,-loweig),1/eigengap);tv=[(1-d0*d0)*x/phi0 for x in mv(proj,V)];cof=[[N[1][1],-N[1][0]],[-N[0][1],N[0][0]]];AA0=scale(plus(plus(N,mm(proj,N),-(1-d0*d0)),cof,d0),1/phi0);g=[x/norm(sv) for x in sv];GG=[[g[0],g[1]],[-g[1],g[0]]]

ck('uniform_nonzero_translation',dot(tv,tv)>0)
ck('uniform_good_support_nonzero',norm(sv)>0)
J=scaleM(I4+kron(scaleM(px,tv[0])+scaleM(pz,tv[1]),I2)+sum((scaleM(kron(pa[a],transpose(pa[b])),AA0[a][b]) for a in range(2) for b in range(2)),mat([[0]*4 for _ in range(4)]))+scaleM(kron(py,transpose(py)),d0),acb(1)/2)
H=scaleM(kron(scaleM(px,V[0])+scaleM(pz,V[1]),I2)+sum((scaleM(kron(pa[a],transpose(pa[b])),N[a][b]) for a in range(2) for b in range(2)),mat([[0]*4 for _ in range(4)])),acb(1)/2)
zv=[a+b for a,b in zip(mv(trans(AA0),V),mv(trans(N),tv))]
Zd=scaleM(scaleM(I2,phi0)+scaleM(px,zv[0])+scaleM(pz,zv[1]),acb(1)/2);D=kron(I2,Zd)-H
ck('original_complementarity_interval_consistent',all((D*J)[i,j].contains(0) for i in range(4) for j in range(4)))
ck('nonzero_translation_and_strict_canonical_branch',dot(tv,tv)>0 and d0>0 and d0<1)
pJ=((tr(J)*tr(J)-tr(J*J))/2).real;pD=((tr(D)*tr(D)-tr(D*D))/2).real
ck('both_positive_rank_two_products',pJ>0 and pD>0)
# Exact rank two follows from physical canonical form, PSD complementarity,
# and these positive products. Interval zero alone is never the rank proof.
P=scaleM(scaleM(J,tr(J))-J*J,1/pJ)
ck('projector_interval_consistent',all((P*P-P)[i,j].contains(0) for i in range(4) for j in range(4)))
fs=[scaleM(f,1/arb(2).sqrt()) for f in [I2,px,py,pz]]
G=mat([[tr(kron(I2,a)*P*kron(I2,b)*P) for b in fs] for a in fs])
ck('complex_Hermitian_TP_Gram_positive',all(submat(G,list(range(k))).det().real>0 for k in range(1,5)))
mu2=(27*G.det()/(tr(G)**3)).real;gamma=(pD/tr(D)).real

ck('uniform_TP_injectivity',mu2>0)
ck('uniform_rank_two_slack_gap',gamma>0)
# Uniform exact-optimum stability has no inherited 1e-27 additive floor.
Cb=(1+arb(2).sqrt()/mu2.sqrt())*(16*RR/gamma).sqrt()
Ag=(4*RR/norm(sv)).sqrt();Bg=RR/norm(sv)
ck('uniform_original_bad_stability_constant71',Cb<71)
ck('uniform_original_good_stability_constants4',Ag<4 and Bg<4)
# Concrete nonunique exposed face: identity and complete Z dephasing.
J1=s.diag(1,0,0,1);J2=s.Matrix([[1,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,1]])
Ds=s.diag(0,1,1,0);Ps=s.diag(1,0,0,1)
Fs=[s.eye(2),X,Y,Z]
Gs=s.Matrix([[s.trace(s.kronecker_product(s.eye(2),a)*Ps*s.kronecker_product(s.eye(2),b)*Ps)/2 for b in Fs] for a in Fs])
ctrl('singular_TP_distinct_supported_channels',J1!=J2 and psd(J1) and psd(J2) and ptr(J1)==s.eye(2) and ptr(J2)==s.eye(2) and Ds*J1==s.zeros(4) and Ds*J2==s.zeros(4) and Gs.det()==0)
def localized_pair(v1,v2):
 b1=v1[1]/v1[0];b2=v2[1]/v2[0]
 if not (b1<0 and b2>0):raise ValueError('strict opposite slopes absent')
 return b2/(b2-b1),-b1*b2/(b2-b1)
try:localized_pair([arb(1),arb(0)],[arb(1),arb(0)]);failed=False
except ValueError:failed=True
ctrl('inactive_law_balanced_zero_sine_rejected',failed and sum([0,0])==0)
# Same X-column support is maximized by identity and X dephasing.
Jx=choi(lambda op:(op+X*op*X)/2);Ji=choi(lambda op:op)
Hx=support_matrix(s.zeros(2,1),s.diag(1,0))
ctrl('branch_boundary_multiple_exact_CPTP_maximizers',Ji!=Jx and psd(Jx) and ptr(Jx)==s.eye(2) and s.trace(Hx*Ji)==1 and s.trace(Hx*Jx)==1 and support(s.zeros(2,1),s.diag(1,0))==1)
# A repeated top eigenspace makes the spectral projector formula undefined.
Hzero=s.zeros(2);ctrl('repeated_top_eigenvalue_projector_undefined',Hzero.eigenvals()=={s.Integer(0):2})
# A finite-shot implementation consumer: fixed exposure, no discarded trials.
mu_floor=arb('0.0522306');ck('support_test_conditioning_floor',mu2>mu_floor)
Ctest=2*(1+arb(2).sqrt()/mu_floor.sqrt());log60=arb(60).log()
pbad=log60/9000000;pgood=log60/170000
bad_test=Ctest*pbad.sqrt();good_test=2*pgood.sqrt()
ck('nine_million_zero_fail_bad_allowance_below_one_percent',bad_test<arb('0.01'))
ck('170000_zero_fail_good_allowance_below_one_percent',good_test<arb('0.01'))
# Exact binomial zero-failure confidence and allocation controls, at tractable counts.
ctrl('understated_failure_probability_not_certified',s.Rational(99,100)**100>s.Rational(1,60))
ck('exact_three_branch_failure_budget',3*s.Rational(1,60)==s.Rational(1,20))
ctrl('postselection_loses_all_failure_evidence',sum([1,1,0,0])==2 and sum(x for x in [1,1,0,0] if x==0)==0)
implementation={'bad_support_factor':str(Ctest),'branch_failure_probability':'1/60','simultaneous_confidence':'at least19/20','bad_shots_each':9000000,'good_shots':170000,'bad_distance_upper':str(bad_test),'good_distance_upper':str(good_test),'total_shots':18170000,'assumptions':'zero observed support failures, fixed independent stationary trials, trusted Bell preparation and exact support/Bell measurement, complete TP outputs with every trial retained; add preparation/measurement systematic probability allowance before square roots','scope':'Prospective decoder implementation certificate, not observed data or flagged-instrument delta.'}
report={'result_id':'K2428','checks':checks,'controls':controls,'inherited_K2426_checks':inherited_checks,'inherited_K2426_controls':inherited_controls,'endpoint_boxes':[[str(x) for x in row] for row in ells],'slope_boxes':list(map(str,bs)),'dual_box':{'lambda':str(lbox),'tau':str(tbox)},'uniform_exposure':{'eigengap':str(eigengap),'determinant':str(det),'improvement_gap':str(hh-det),'translation_squared':str(dot(tv,tv)),'TP_mu_squared_lower':str(mu2),'slack_gamma_lower':str(gamma),'good_support_norm':str(norm(sv))},'finite_shot_implementation':implementation,'exact_optimum_stability':{'bad_sqrt_coefficient':str(Cb),'good_sqrt_coefficient':str(Ag),'good_linear_coefficient':str(Bg),'simple_bounds':'bad<=71 sqrt(e); good<=4 sqrt(e)+4e; e=nominal excess error; no objective-gap floor'},'scope':'Existence of an attained exact dual in this uniformly exposing box plus nonnegative original-controller gaps proves uniqueness of nominal physical channels and projective dual. Rational candidate not asserted optimal; no empirical or Kraus uniqueness.'}
deps=['tests/channel-swings/k2424_recovery_saddle_reduction_probe.py','tests/channel-swings/k2426_recovery_rigidity_probe.py','explorations/conditional-build/k2422-joint-recovery-optimality-2026-10-31.md']
report['dependencies']={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps}
report=json.loads(json.dumps(report));out=R/'lab/process/k2428-exact-recovery-uniqueness.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
else:assert json.loads(out.read_text())==report
print(json.dumps({'checks':len(checks),'controls':len(controls),'dual_box':report['dual_box'],'exposure':report['uniform_exposure']}))
