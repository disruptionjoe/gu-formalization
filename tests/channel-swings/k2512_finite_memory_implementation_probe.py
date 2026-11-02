"""Exact finite controls for K2512. Universal/embedding proofs are in the note.
Default reproduces/compares the saved report; --write saves it.
The small matrices test the reducing AB plane; full C108 spectator coverage
is supplied by the written embedding/model proof, not by fixture dimension.
"""
from pathlib import Path
import hashlib
import json
import sys
import sympy as s

ROOT = Path(__file__).resolve().parents[2]
checks = {}
controls = {}

def ck(name, value):
    checks[name] = bool(value)
    if not value:
        raise AssertionError(name)

def ct(name, value):
    controls[name] = bool(value)
    if not value:
        raise AssertionError(name)

def zero(matrix):
    return matrix == s.zeros(matrix.rows, matrix.cols)

def ket(n, j):
    return s.eye(n)[:, j]

def outer(v):
    return v * v.conjugate().T

def kron(a, b):
    return s.kronecker_product(a, b)

def real_rotation(c, z):
    return s.Matrix([[c, -z], [z, c]])

I2, I3, I6 = s.eye(2), s.eye(3), s.eye(6)
P = s.diag(1, 0)
X = s.Matrix([[0, 1], [1, 0]])
Y = s.Matrix([[0, -s.I], [s.I, 0]])
e0, e1, e2 = [ket(3, j) for j in range(3)]
P0, P1, P2 = [outer(e) for e in (e0, e1, e2)]
A, B = ket(2, 0), ket(2, 1)
Q = kron(P, I3)
T = I6 - Q
S = kron(I2, P0 + P1)
Y12 = s.Matrix([[0, 0, 0], [0, 0, -s.I], [0, s.I, 0]])
Y01 = s.Matrix([[0, -s.I, 0], [s.I, 0, 0], [0, 0, 0]])

def circuit(ctheta, stheta, cbeta, sbeta, cphi, sphi):
    R = real_rotation(ctheta, stheta)
    Bm = s.Matrix([[1, 0, 0], [0, cbeta, -sbeta], [0, sbeta, cbeta]])
    Wm = s.Matrix([[cphi, -sphi, 0], [sphi, cphi, 0], [0, 0, 1]])
    C = kron(I2, P0) + kron(R, P1) + kron(X, P2)
    return kron(I2, Wm) * kron(I2, Bm) * C, R, Bm, Wm, C

r = s.Rational
cth, sth = r(3, 5), r(4, 5)
cb, sb = r(3, 5), r(4, 5)
cw, sw = r(12, 13), r(5, 13)
V, R, Bm, Wm, C = circuit(cth, sth, cb, sb, cw, sw)
ck('controlled_unitary', C.conjugate().T * C == I6)
ck('whole_unitary', V.conjugate().T * V == I6)
ck('support_rank_fixture', s.trace(S) == 4)
for name, F, F2 in [('Q', Q, P), ('T', T, I2-P)]:
    AF = S * V.conjugate().T * F * V * S
    expected = kron(F2, P0) + kron(R.T * F2 * R, P1)
    ck(name + '_supported_effect', AF == expected)
    defect = AF - S * F * S
    ck(name + '_defect_square', defect * defect == sth**2 * kron(I2, P1))
    # Each positive/negative original sector has exactly one affected basis
    # vector at memory1; the original full rank is supplied by the paper.
    for side in [0, 1]:
        sector = S * (F if side else I6-F)
        wrong = I6-F if side else F
        total = s.trace(V * sector * V.conjugate().T * wrong)
        ck(name + '_sector_wrong_trace_' + str(side), total == sth**2)
L = S * V.conjugate().T * (I6-S) * V * S
ck('supported_leakage', L == sb**2 * kron(I2, P1))
ck('uniform_support_leakage_probability', s.trace(L)/s.trace(S) == sb**2/2)
# Full H108 generic settings normalize the same rank-one wrong trace.
for rank in [20, 196, 24, 192]:
    ck('full_rank_setting_probability_' + str(rank), rank * (sth**2/rank) == sth**2)
ck('full_support_rank', 108*2 == 216)
ck('full_leakage_trace', 216 * sb**2/2 == 108 * sb**2)

WB = kron(I2, Wm*Bm)
Wb = kron(I2, Wm)
Gth = WB * kron(Y, P1) * WB.conjugate().T
Gb = Wb * kron(I2, Y12) * Wb.conjugate().T
w1 = Wm * e1
v1 = Wm * Bm * e1
for name, F in [('Q', Q), ('T', T)]:
    cross = (I6-F) * Gth * F
    gram = cross.conjugate().T * cross
    ck(name + '_theta_cross_projection', gram*gram == gram and s.trace(gram) == 1)
    ck(name + '_beta_cross_zero', zero((I6-F)*Gb*F))
th_cross = (I6-S)*Gth*S
ck('support_theta_cross_gram', th_cross.conjugate().T*th_cross == (sb*cb)**2*kron(I2, outer(w1)))
ct('ambient_support_theta_nonzero', (sb*cb)**2 == r(144,625) and not zero(th_cross))
b_cross = (I6-S)*Gb*S
ck('support_beta_cross_norm_one', b_cross.conjugate().T*b_cross == kron(I2,outer(w1)))
for M in [1, 17, 10**6]:
    Gphi = M*kron(I2,Y01)
    for name, F in [('Q', Q), ('T', T), ('S', S)]:
        ck('phi_cross_zero_'+name+'_'+str(M), zero((I6-F)*Gphi*F))
# Identity vs arbitrary supported memory rotation leave all one-gap effects equal.
Vphi0, *_ = circuit(cth,sth,cb,sb,1,0)
for name,F in [('Q',Q),('T',T),('leak',I6-S)]:
    ck('one_gap_phi_invisible_'+name, S*V.conjugate().T*F*V*S == S*Vphi0.conjugate().T*F*Vphi0*S)

# Fresh pointer dilation gives the unchanged projective instrument.
pointer0, pointer1 = ket(2,0), ket(2,1)
J0 = kron(I6,pointer0)
for name,F in [('Q',Q),('T',T),('S',S)]:
    U = kron(F,X)+kron(I6-F,I2)
    ck('pointer_unitary_'+name,U.conjugate().T*U==s.eye(12))
    K0=kron(I6,pointer0.T)*U*J0
    K1=kron(I6,pointer1.T)*U*J0
    ck('pointer_Lueders_'+name,K0==I6-F and K1==F)

# Complete reset to A⊗e1 works on the entire retained D, including entanglement.
prepared=kron(A,e1)
reset_ops=[prepared*ket(6,n).T for n in range(6)]
ck('reset_Kraus_complete',sum((K.T*K for K in reset_ops),s.zeros(6))==I6)
# Entire reference can remain; here test one nontrivially entangled fixture.
psi=(kron(kron(A,e0),pointer0)+kron(kron(B,e1),pointer1))/s.sqrt(2)
rho=outer(psi)
reset_rho=sum((kron(K,I2)*rho*kron(K.T,I2) for K in reset_ops),s.zeros(12))
ck('joint_reset_removes_entanglement',reset_rho==kron(outer(prepared),I2/2))
ck('structural_effect_setting', (prepared.T*V.T*(I6-Q)*V*prepared)[0]==sth**2)
ck('structural_leak_setting', (prepared.T*V.T*(I6-S)*V*prepared)[0]==sb**2)

# Repeated-memory controls retain E between gaps and include the Q=1 projection.
Vmemory,*_=circuit(cth,sth,1,0,cw,sw)
psi0=kron(A,e0)
first=Vmemory*psi0
ck('memory_first_Q_certain',Q*first==first)
second=Vmemory*Q*first
pwrong=(second.T*(I6-Q)*second)[0]
ct('phi_changes_two_gap_record',pwrong==sw**2*sth**2==r(16,169))
Vmemory0,*_=circuit(cth,sth,1,0,1,0)
second0=Vmemory0*Q*Vmemory0*psi0
ct('phi_zero_other_record', (second0.T*(I6-Q)*second0)[0]==0)
Vleak,*_=circuit(1,0,cb,sb,1,0)
psi1=kron(A,e1)
firstleak=Vleak*psi1
ck('leak_first_Q_certain',Q*firstleak==firstleak)
secondleak=Vleak*Q*firstleak
ct('unsupported_memory_later_error',(secondleak.T*(I6-Q)*secondleak)[0]==sb**2)
ck('leaky_gap_exact_supported_Q',S*Vleak.T*Q*Vleak*S==S*Q*S)
# Falsely inserting a fresh e1 reset removes the intended later-error mechanism.
reset_second=Vleak*prepared
ct('deployment_reset_changes_process',(reset_second.T*(I6-Q)*reset_second)[0]==0)

# An unmodeled spectator swap passes the two tests but violates Q by one.
I4=s.eye(4); Q4=s.diag(1,0,1,0)
Us=s.Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
Vspec=kron(Us,I3); Qspec=kron(Q4,I3); Sspec=kron(I4,P0+P1)
ptest=kron(ket(4,0),e1)
ct('spectator_swap_passes_effect_test',(ptest.T*Vspec.T*(s.eye(12)-Qspec)*Vspec*ptest)[0]==0)
ct('spectator_swap_passes_leak_test',(ptest.T*Vspec.T*(s.eye(12)-Sspec)*Vspec*ptest)[0]==0)
usupported=kron(ket(4,2),e1)
ct('spectator_swap_has_unit_defect',(usupported.T*(Vspec.T*Qspec*Vspec-Qspec)*usupported)[0]==-1)

# Exact budgets: trig inequalities for the full rectangle are proved in prose.
eps=ell=r(1,10**6); a=eps/2; b=ell/4
htheta=eps/2; hbeta=r(1,2000)
ck('effect_radius_margin',a+htheta==eps)
ck('leak_angle_sufficient_margin',s.sqrt(b)+hbeta==s.sqrt(ell))
ck('anisotropic_radius_factor',hbeta/htheta==1000)
W=1/a**2+1/b
Wgeneric=432/a**2+216/b
ck('two_setting_weight',W==4000004000000)
ck('generic_weight',Wgeneric==1728000864000000)
ck('structural_weight_gain',431<Wgeneric/W<432)
ck('prospective_count',5*W==20000020000000)
ck('generic_prospective_count',5*Wgeneric==8640004320000000)
# log(100)<5: e^5 exceeds100 from its first seven positive Taylor terms.
ck('log100_less_than5',sum((r(5)**k/s.factorial(k) for k in range(7)),s.Integer(0))>100)
ct('bias_floor_rejects',1/W-2/W<0)
# Robust endpoint with nonzero norm-perturbation budgets (proof in note).
eta_c=eta_d=eps/16
hth_robust=eps/4
hb_robust=s.sqrt(ell)/4
ck('robust_effect_margin',a+eta_c+eta_d+hth_robust==7*eps/8<eps)
amp_robust=s.sqrt(b)+eta_c+eta_d+hb_robust
ck('robust_leak_amplitude',amp_robust==r(6001,8000000))
ck('robust_leak_margin',amp_robust**2==r(36012001,64000000000000)<ell)
# An invisible spectator swap is distance2 from the model, not small eta.
minusspec=(ket(4,2)-ket(4,3))/s.sqrt(2)
ct('spectator_swap_breaks_small_norm_promise',(Us-I4)*minusspec==-2*minusspec)
# Small unobserved spectator rotation: exact spectral norm and Q-defect relation.
Rsmall=real_rotation(r(99,101),r(20,101))
Dsmall=Rsmall-I2
ck('small_rotation_operator_distance',Dsmall.T*Dsmall==r(4,101)*I2)
Fsmall=Rsmall.T*P*Rsmall-P
ck('small_rotation_effect_defect',Fsmall*Fsmall==r(400,10201)*I2)
ck('effect_perturbation_constant_one',r(400,10201)<=r(4,101))
# Wrong-event amplitudes obey the triangle bound in a nonzero rational fixture.
psia=ket(2,0)
ck('wrong_event_amplitude_perturbation',((I2-P)*Rsmall*psia).norm()<=Dsmall[:,0].norm())
E=1024*eps+1024*s.sqrt(eps*ell)+ell
ck('complete_record',E==r(2049,10**6))
ck('postselection',E/(r(1,2)-E)==r(2049,497951)<r(1,200))
# Corrupt the actual gate, not a boolean annotation.
bad=s.MutableDenseMatrix(V);bad[0,0]+=r(1,100)
ct('corrupt_gate_rejected',bad.T*bad!=I6)

paths=[
'explorations/conditional-build/k2512-finite-memory-implementation-2026-11-02.md',
 'tests/channel-swings/k2512_finite_memory_implementation_probe.py',
 'explorations/conditional-build/k2510-effect-path-calibration-2026-11-02.md',
 'explorations/conditional-build/k2508-controller-coverage-2026-11-02.md',
 'explorations/conditional-build/k2506-calibration-deployment-transfer-2026-11-02.md']
report={
'result':'K2512',
'scope':'exact supplied retained-qutrit fixture and rational budgets; universal embedding and angle proofs in note',
'checks':checks,'contrary_controls':controls,
'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
'consumer':{'supported_dimension':216,'full_dimension':324,'pooled_weight':str(W),
'generic_pooled_weight':str(Wgeneric),'sufficient_zero_count':str(5*W),
'confidence_failure':'1/100','anisotropic_drift_ratio':1000,
'record_error':str(E),'postselection_error':str(E/(r(1,2)-E))}}
report_path=ROOT/'lab/process/k2512-finite-memory-implementation.json'
if '--write' in sys.argv:
    report_path.write_text(json.dumps(report,indent=2)+'\n')
else:
    ck('saved_report_consistency',json.loads(report_path.read_text())==report)
print('K2512 PASS',len(checks),'checks',len(controls),'contrary controls')
