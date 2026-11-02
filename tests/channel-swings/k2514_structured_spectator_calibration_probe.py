"""Exact finite controls for K2514; universal theorems are proved in its note.
Default compares the saved report; --write creates it after owner admission.
Full Q/T retains a noncommuting principal block; active common-eigen planes
are only reducing parts of that carrier. No physical data are simulated.
"""
from pathlib import Path
import hashlib
import json
import sys
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
checks={}; controls={}
def ck(name,value):
    checks[name]=bool(value)
    if not value: raise AssertionError(name)
def ct(name,value):
    controls[name]=bool(value)
    if not value: raise AssertionError(name)
def eq(a,b):
    if isinstance(a,s.MatrixBase): return (a-b).applyfunc(s.simplify)==s.zeros(a.rows,a.cols)
    return s.simplify(a-b)==0
def ket(n,j): return s.eye(n)[:,j]
def outer(v): return v*v.conjugate().T
def kr(a,b): return s.kronecker_product(a,b)
def rot(c,z): return s.Matrix([[c,-z],[z,c]])
r=s.Rational
I2=s.eye(2); P=s.diag(1,0)
phase=r(3,5)+s.I*r(4,5)
blocks=[s.diag(s.I,1)*rot(r(3,5),r(4,5))*s.diag(1,phase),
        s.diag(phase,s.I)*rot(r(12,13),r(5,13))*s.diag(-1,1)]
ps=[r(16,25),r(25,169)]
for j,(U,p) in enumerate(zip(blocks,ps)):
    ck('complex_unitary_'+str(j),eq(U.conjugate().T*U,I2))
    ck('endpoint_transfer_'+str(j),eq(abs(U[1,0])**2,p))
    ck('reverse_transfer_'+str(j),eq(abs(U[0,1])**2,p))
    D=U.conjugate().T*P*U-P
    ck('complex_defect_square_'+str(j),eq(D*D,p*I2))
    ct('wrong_probability_not_linear_norm_'+str(j),p**2<p)


# Structurally faithful 8D fixture; principal parameter9/25 is not the original
# C108 block. The note proves full-carrier transfer by reducing subspaces.
I8=s.eye(8)
Q=s.diag(1,0,1,0,1,0,1,0)
T=s.diag(0,1,0,1,0,1,0,0)
T[6:8,6:8]=s.Matrix([[9,12],[12,16]])/25
ck('Q_projector',Q*Q==Q)
ck('T_projector',T*T==T)
ct('original_type_noncommuting_block',Q*T!=T*Q)

def layer(pairs,bs):
    U=s.eye(8)
    for (a,b),B in zip(pairs,bs):
        for x,k in enumerate([a,b]):
            for y,l in enumerate([a,b]): U[k,l]=B[x,y]
    return U
pairs1=[(0,1),(2,3)];pairs2=[(0,3),(2,1)]
U1=layer(pairs1,blocks);U2=layer(pairs2,list(reversed(blocks)))
for name,U,pairs,bps in [('first',U1,pairs1,ps),('second',U2,pairs2,list(reversed(ps)))]:
    ck(name+'_full_unitary',eq(U.conjugate().T*U,I8))
    ck(name+'_principal_block_retained',U[6:8,6:8]==I2)
    Dsquare=s.zeros(8)
    for (a,b),p in zip(pairs,bps):
        Dsquare[a,a]=p;Dsquare[b,b]=p
        for label,F in [('Q',Q),('T',T)]:
            wrong=I8-F if F[a,a]==1 else F
            prob=(ket(8,a).T*U.conjugate().T*wrong*U*ket(8,a))[0]
            ck(name+'_'+label+'_single_read_'+str(a),eq(prob,p))
    for label,F in [('Q',Q),('T',T)]:
        D=U.conjugate().T*F*U-F
        ck(name+'_'+label+'_full_defect_square',eq(D*D,Dsquare))
ct('layers_need_not_commute',not eq(U1*U2,U2*U1))

# Complete retained qutrit implementation, including dangerous outside block.
I3=s.eye(3);p0,p1,p2=[outer(ket(3,j)) for j in range(3)]
Z=s.eye(8);Z[0:2,0:2]=s.Matrix([[0,1],[1,0]])
C1=kr(I8,p0)+kr(U1,p1)+kr(Z,p2)
C2=kr(I8,p0)+kr(U2,p1)+kr(Z,p2)
Bm=s.Matrix([[1,0,0],[0,r(3,5),-r(4,5)],[0,r(4,5),r(3,5)]])
Wm=s.Matrix([[r(12,13),-r(5,13),0],[r(5,13),r(12,13),0],[0,0,1]])
V=kr(I8,Wm*Bm)*C2*C1
S=kr(I8,p0+p1);I24=s.eye(24);Uall=U2*U1
ck('complete_gap_unitary',eq(V.conjugate().T*V,I24))
for name,F in [('Q',Q),('T',T)]:
    ck('full_supported_effect_'+name,eq(S*V.conjugate().T*kr(F,I3)*V*S,kr(F,p0)+kr(Uall.conjugate().T*F*Uall,p1)))
ck('full_leakage_identity',eq(S*V.conjugate().T*(I24-S)*V*S,r(16,25)*kr(I8,p1)))
ck('leakage_single_read',eq((kr(ket(8,0),ket(3,1)).T*kr(I8,Bm.T)*(I24-S)*kr(I8,Bm)*kr(ket(8,0),ket(3,1)))[0],r(16,25)))

# Coherent accumulation and cancellation are actual gate changes.
c,z=r(99,101),r(20,101)
R=rot(c,z);RR=R*R
D=RR.T*P*RR-P
ck('aligned_composition_exact',eq(D*D,(2*c*z)**2*I2))
ct('max_layer_bound_fails',(2*c*z)**2>z**2)
ct('root_sum_square_fails',(2*c*z)**2>2*z**2)
ck('opposite_rotations_cancel',R.T*R==I2)
ct('positive_data_can_cancel',z**2>0 and R.T*R==I2)

# A listed spectator is found; original first plane alone misses it.
Spec=layer([(2,3)],[rot(r(3,5),r(4,5))])
ck('listed_spectator_detected',(ket(8,2).T*Spec.T*(I8-Q)*Spec*ket(8,2))[0]==r(16,25))
ct('first_plane_only_misses_spectator',(ket(8,0).T*Spec.T*(I8-Q)*Spec*ket(8,0))[0]==0)
Unknown=layer([(4,5)],[s.Matrix([[0,1],[1,0]])])
ct('unlisted_coupling_passes_selected_inputs',all((ket(8,k).T*Unknown.T*(I8-Q)*Unknown*ket(8,k))[0]==0 for k in [0,2]))
ct('unlisted_coupling_has_unit_error',(ket(8,4).T*(Unknown.T*Q*Unknown-Q)*ket(8,4))[0]==-1)
K0=s.Matrix([[1,0],[0,0]]);K1=s.Matrix([[0,1],[0,0]])
ck('one_way_reset_CPTP',K0.T*K0+K1.T*K1==I2)
A=K0.T*P*K0+K1.T*P*K1
ct('nonunitary_endpoint_inference_fails',A==I2 and (ket(2,0).T*(I2-A)*ket(2,0))[0]==0 and (ket(2,1).T*(A-P)*ket(2,1))[0]==1)

# Symbolic derivatives underlying simplex convexity; sign is proved on [0,pi/4].
x=s.symbols('x',real=True)
ck('sin_square_first_derivative',s.trigsimp(s.diff(s.sin(x)**2,x)-s.sin(2*x))==0)
ck('sin_square_second_derivative',s.trigsimp(s.diff(s.sin(x)**2,x,2)-2*s.cos(2*x))==0)
# Exact unequal-multiplicity optimizer: m=(1,4), tau=1/25.
ms=[1,4];tau=r(1,25)
sins=[r(1,5),r(2,5)];coss=[2*s.sqrt(6)/5,s.sqrt(21)/5]
sin2=[2*a*b for a,b in zip(sins,coss)]
Zweight=sum(m/v for m,v in zip(ms,sin2))
ws=[(1/v)/Zweight for v in sin2]
ck('unequal_optimizer_normalization',eq(sum(m*w for m,w in zip(ms,ws)),1))
ck('unequal_optimizer_stationarity',eq(ws[0]*sin2[0],ws[1]*sin2[1]))
ck('unequal_optimizer_threshold',eq(sum(w*a*a for w,a in zip(ws,sins)),tau))
ck('unequal_layer_angles_by_m',all(a*a==m*tau for m,a in zip(ms,sins)))
# arcsin(1/5)<1/4 and arcsin(2/5)<1/2 via sin y>=y-y^3/6;
# hence total<3/4<pi/4. Universal argument is not a finite fixture.
ck('unequal_angle_simplex_bound',r(1,4)-r(1,4)**3/6>r(1,5) and r(1,2)-r(1,2)**3/6>r(2,5))
sinA=sins[0]*coss[1]+coss[0]*sins[1]
ck('unequal_boundary_endpoint_more_costly',bool(s.simplify(ws[1]*sinA**2-tau)>0))
qgroups=[[r(1,5)],[r(1,10),r(1,10),r(1,10),r(1,2)]]
ck('nonoptimal_label_distribution',sum(sum(q) for q in qgroups)==1 and all(q>0 for row in qgroups for q in row))
qmins=[min(q) for q in qgroups]
ct('nonoptimal_label_design_lower_threshold',sum(m*q for m,q in zip(ms,qmins))==r(3,5)<1)
# Equal-multiplicity direct pooling has factor L improvement over rectangular.
for L in [1,2,3,7]:
    m=3; tprob=r(1,10000)
    direct=m/tprob;rect=L*m/tprob
    ck('direct_rectangular_factor_'+str(L),rect==L*direct)

# Outer detection weights balance the effect and leakage failure thresholds.
b=r(1,100);tau_small=r(1,2000);Wsmall=1/tau_small+1/b
qE=(1/tau_small)/Wsmall;qB=(1/b)/Wsmall
ck('outer_probabilities',qE+qB==1)
ck('outer_equal_failure_threshold',qE*tau_small==qB*b==1/Wsmall)
ct('outer_unbalanced_worse',min(r(1,2)*tau_small,r(1,2)*b)<1/Wsmall)

# Rational consumer; no synthetic successful calibration transcript.
eps=ell=r(1,10**6);ss=r(1,4000000);tau_cons=ss**2/2;bcons=r(1,4000000)
W=1/tau_cons+1/bcons
ck('effect_center_conservative',2*ss==eps/2)
ck('effect_drift_margin',2*ss+2*r(1,4000000)==eps)
ck('support_drift_margin',s.sqrt(bcons)+r(1,2000)==s.sqrt(ell))
ck('new_pooled_weight',W==32000004000000)
ck('rectangular_effect_weight',2/tau_cons==64000000000000)
ck('sufficient_zero_count',5*W==160000020000000)
ck('log100_less_than5',sum(r(5)**k/s.factorial(k) for k in range(7))>100)
ct('bias_floor_rejects',1/W-2/W<0)
E=1024*eps+1024*s.sqrt(eps*ell)+ell
ck('complete_record_consumer',E==r(2049,10**6))
ck('postselection_consumer',E/(r(1,2)-E)==r(2049,497951)<r(1,200))

paths=[
'explorations/conditional-build/k2514-structured-spectator-calibration-2026-11-02.md',
 'tests/channel-swings/k2514_structured_spectator_calibration_probe.py',
 'explorations/conditional-build/k2512-finite-memory-implementation-2026-11-02.md',
 'explorations/conditional-build/k2504-verifier-sector-calibration-2026-11-02.md',
 'explorations/conditional-build/k2484-coherent-verifier-instruments-2026-11-01.md',
 'explorations/conditional-build/k2506-calibration-deployment-transfer-2026-11-02.md']
report={'result':'K2514','scope':'exact complex finite gate fixtures and resource arithmetic; whole-class and minimax proofs in note',
'checks':checks,'contrary_controls':controls,
'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
'consumer':{'layers':2,'active_planes_per_layer':2,'pooled_weight':str(W),'sufficient_zero_count':str(5*W),'confidence_failure':'1/100','record_error':str(E),'postselection_error':str(E/(r(1,2)-E))}}
report_path=ROOT/'lab/process/k2514-structured-spectator-calibration.json'
if '--write' in sys.argv: report_path.write_text(json.dumps(report,indent=2)+'\n')
else: ck('saved_report_consistency',json.loads(report_path.read_text())==report)
print('K2514 PASS',len(checks),'checks',len(controls),'contrary controls')
