"""K2516 exact effect, minimax and resource controls; default verifies saved report."""
from pathlib import Path
import hashlib,json,sys
import sympy as s
R=Path(__file__).resolve().parents[2]
checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not checks[k]:raise AssertionError(k)
def ct(k,v):
 controls[k]=bool(v)
 if not controls[k]:raise AssertionError(k)
a,b,t,e,r,z=s.symbols('a b t e r z',real=True)
f=(a-b+s.sqrt((a-b)**2+4*b))/2
ck('sharp_characteristic',s.simplify(f*f-(a-b)*f-b)==0)
ck('acceptance_square',s.expand((2*e-a+b)**2-((a-b)**2+4*b)-4*(e*e-e*(a-b)-b))==0)
P=s.diag(1,0);I=s.eye(2)
fixtures=[]
for av,bv in [(s.Rational(x,4),s.Rational(y,4)) for x in range(5) for y in range(5)]:
 c=s.sqrt(min((1-av)*bv,av*(1-bv)));A=s.Matrix([[1-av,c],[c,bv]]);D=A-P
 ff=(abs(av-bv)+s.sqrt((av-bv)**2+4*min(av,bv)))/2
 key=str(av)+'_'+str(bv)
 ck('PSD_A_'+key,A.det()>=0 and A[0,0]>=0 and A[1,1]>=0)
 ck('PSD_IminusA_'+key,(I-A).det()>=0 and (I-A)[0,0]>=0 and (I-A)[1,1]>=0)
 ev=list(D.eigenvals());ck('sharp_norm_'+key,s.simplify(max(abs(x) for x in ev)-ff)==0)
 ck('old_bound_'+key,ff<=s.sqrt(max(av,bv)))
 fixtures.append({'a':str(av),'b':str(bv),'norm':str(ff)})
A=s.Matrix([[s.Rational(3,4),s.Rational(1,4)],[s.Rational(1,4),s.Rational(1,12)]])
v=s.Matrix([3,1])/s.sqrt(10);u=s.Matrix([-1,3])/s.sqrt(10);ep=s.Matrix([1,0]);em=s.Matrix([0,1])
Ks=[s.sqrt(s.Rational(5,6))*ep*v.T,s.sqrt(s.Rational(1,6))*em*v.T,em*u.T]
ck('actual_CPTP_Kraus_complete',sum((K.H*K for K in Ks),s.zeros(2))==I)
ck('actual_channel_effect',sum((K.H*P*K for K in Ks),s.zeros(2))==A)
Z=s.diag(1,s.I);ck('complex_phase_spectrum',s.simplify((Z*A*Z.H-P).charpoly().as_expr()-(A-P).charpoly().as_expr())==0)
large=s.diag(A,1,0,0,0);largeP=s.diag(1,0,1,0,0,0)
ck('higher_rank_embedding',(large-largeP).rank()==2)
ck('rank_two_wrong_trace',s.trace(largeP*(s.eye(6)-large)*largeP)==s.Rational(1,4))
ck('rank_four_wrong_trace',s.trace((s.eye(6)-largeP)*large*(s.eye(6)-largeP))==s.Rational(1,12))
small,big=s.symbols('small big',positive=True);DD=small*(1-e)+big*e;qr=small*(1-e)/DD;qs=big*e/DD;tau=e*e/DD
ck('label_normalization',s.factor(qr+qs-1)==0)
ck('balanced_minimax_vertex',s.factor(e*e*(qr/small+qs/big)-tau)==0)
ck('large_sector_axis_vertex',s.factor(e*qs/big-tau)==0)
ck('small_sector_axis_gap',s.factor(e*qr/small-tau-e*(1-2*e)/DD)==0)
q=s.symbols('q');ck('balanced_increases_with_q',s.diff(e*e*(q/small+(1-q)/big),q)==e*e*(1/small-1/big))
ck('large_axis_decreases',s.diff(e*(1-q)/big,q)==-e/big)
ck('nonlinear_domination_other_half',s.expand((1-e)*a+e*b-((1-e)*b+e*a)-(1-2*e)*(a-b))==0)
# Full tolerance extension uses the sum bound from D^2 <= B and effect positivity.
ck('large_tolerance_axis_equalization',s.factor(e*(small/(small+big))/small-e/(small+big))==0)
ck('large_tolerance_balanced_gap',s.factor(e*e*2/(small+big)-e/(small+big)-e*(2*e-1)/(small+big))==0)
for eps in [s.Rational(1,100),s.Rational(1,4),s.Rational(1,2)]:
 for aa,bb in [(eps,0),(eps*eps,eps*eps),(0,eps)]:
  ck('boundary_'+str((eps,aa,bb)),s.simplify((abs(aa-bb)+s.sqrt((aa-bb)**2+4*min(aa,bb)))/2-eps)==0)
k=2;eps=s.Rational(1,10**6);ell=eps
WQ=10*k/eps**2+88*k/eps;WT=12*k/eps**2+84*k/eps;WL=108*k/ell;W=WQ+WT+WL
old=216*k/eps**2+108*k/ell
ck('resource_weight',W==44000560000000)
ck('zero_count_sufficient',5*W==220002800000000)
ck('same_carrier_old_weight',old==432000216000000)
ck('improvement_over_9_8',old/W>s.Rational(49,5))
ck('outer_mix_normalized',WQ/W+WT/W+WL/W==1)
err=512*(2*eps)+1024*s.sqrt(ell*eps)+ell
ck('record_bound',err==s.Rational(2049,10**6))
ck('postselection_consumer',s.factor(err/(s.Rational(1,2)-err))==s.Rational(2049,497951)<s.Rational(1,200))
# Contrary mathematical controls, after the complete clean baseline.
rot=s.Matrix([[s.Rational(99,100),s.sqrt(99)/100],[s.sqrt(99)/100,s.Rational(1,100)]])
ct('coherent_linear_error_false',max(abs(x) for x in (rot-P).eigenvals())==s.Rational(1,10)>s.Rational(1,100))
reset=s.diag(1,s.Rational(1,4));ct('one_endpoint_nonunitary_invisible',reset[0,0]==1 and (reset-P).norm(2)==s.Rational(1,4))
ct('asymmetric_old_bound_strict',s.Rational(1,4)<s.sqrt(s.Rational(1,4)))
true_norm=max(abs(v) for v in (large-largeP).eigenvals())
wrong_square_bound=max(s.trace(largeP*(s.eye(6)-large)*largeP)/2,s.trace((s.eye(6)-largeP)*large*(s.eye(6)-largeP))/4)
ct('rank_factor_required',true_norm**2>wrong_square_bound==s.Rational(1,8))
bad=s.Matrix([[1,1],[1,0]]);ct('omit_effect_positivity_invalid',bad.det()<0 and (I-bad).det()<0)
# Uniform label weights are not optimal for unequal ranks at small tolerance.
r0,s0,e0=2,10,s.Rational(1,10);optimal=e0**2/(r0*(1-e0)+s0*e0)
wrong=min(e0/(2*r0),e0/(2*s0),e0**2*(s.Rational(1,2)/r0+s.Rational(1,2)/s0))
ct('arbitrary_labels_lose_minimax',wrong<optimal)
ct('systematic_floor_not_removed_by_samples',s.Rational(2,1)/W>1/W)
axis_effect=s.diag(1-e0,0)
ct('pooled_gate_not_necessary',max(abs(v) for v in (axis_effect-P).eigenvals())==e0 and (1-e0)*e0>e0**2)
ct('average_not_history_uniform',s.Rational(1,100)*1+s.Rational(99,100)*0<s.Rational(1,50) and 1>s.Rational(1,50))
paths=['explorations/conditional-build/k2516-asymmetric-effect-calibration-2026-11-02.md','tests/channel-swings/k2516_asymmetric_effect_calibration_probe.py','explorations/conditional-build/k2504-verifier-sector-calibration-2026-11-02.md','explorations/conditional-build/k2514-structured-spectator-calibration-2026-11-02.md']
report={'result':'K2516','scope':'exact finite controls and scalar identities; universal compression/minimax proof in note','checks':checks,'contrary_controls':controls,'sharp_fixtures':fixtures,'weight':str(W),'zero_count_n':str(5*W),'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in paths}}
p=R/'lab/process/k2516-asymmetric-effect-calibration.json'
if '--write' in sys.argv:p.write_text(json.dumps(report,indent=2)+'\n')
else:ck('saved_report_consistency',json.loads(p.read_text())==report)
print('K2516 PASS',len(checks),'checks',len(controls),'contrary controls')
