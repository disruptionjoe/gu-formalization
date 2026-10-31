#!/usr/bin/env python3
"""Exact checks for the supplied K2389 joint clock instrument; no hardware claim."""
import argparse
import hashlib
import json
from pathlib import Path
import sympy as s

I=s.eye(2)
X=s.Matrix([[0,1],[1,0]])
Y=s.Matrix([[0,-s.I],[s.I,0]])
Z=s.diag(1,-1)
P=[I,X,Y,Z]
theta=s.symbols('theta',real=True)
nu,w=s.symbols('nu w',real=True)
n=s.cos(theta)*X-s.sin(theta)*Y
A=(I+nu*n)/2
checks={}
controls={}

def eq(name,a,b):
    if isinstance(a,s.MatrixBase) or isinstance(b,s.MatrixBase):
        ok=all(s.simplify(v)==0 for v in (a-b))
    else:
        ok=s.simplify(a-b)==0
    checks[name]=bool(ok)
    assert ok,name

def mean(M):
    return M.applyfunc(lambda v:s.simplify(s.integrate(s.expand_trig(v),(theta,0,2*s.pi))/(2*s.pi)))

def scalar_mean(v):
    return s.simplify(s.integrate(s.expand_trig(v),(theta,0,2*s.pi))/(2*s.pi))

# Occupation is bit blind, controls preserve it, loss lowers it by one.
N=s.diag(1,1,0)
x=s.Matrix([[0,1,0],[1,0,0],[0,0,0]])
z=s.diag(1,-1,0)
eq('number_commutes_x',N*x-x*N,s.zeros(3))
eq('number_commutes_z',N*z-z*N,s.zeros(3))
for b in (0,1):
    L=s.zeros(3);L[2,b]=1
    eq('loss_lowering_'+str(b),N*L-L*N,-L)
    eq('loss_norm_'+str(b),(L.T*L)[b,b],1)
Nrail=s.diag(1,0,0)
controls['single_rail_is_not_bit_blind']=bool(Nrail*x-x*N != s.zeros(3))

# The sign follows the declared Hamiltonian -g N Z (not guessed).
R=s.cos(theta/2)*I+s.I*s.sin(theta/2)*Z
plus=s.Matrix([1,1])/s.sqrt(2)
A0=R*plus*plus.T*R.conjugate().T
eq('clock_hamiltonian_sign',A0,(I+n)/2)
eq('clock_dephasing_channel',(1+nu)/2*A0+(1-nu)/2*Z*A0*Z,A)
eq('clock_trace',s.trace(A),1)
eq('clock_determinant',A.det(),(1-nu**2)/4)
eq('clock_mean',mean(A),I/2)

# Complete map on ALL matrix units, retaining coherences.
for j in range(2):
  for k in range(2):
    E=s.zeros(2);E[j,k]=1
    coherent=s.zeros(2)
    uncorrected=s.zeros(2)
    classical=s.zeros(2)
    for sign in (1,-1):
      B=(I+sign*n)/2
      J=w*mean(s.trace(B*E)*A)
      target=w/4*(s.trace(E)*I+sign*nu/2*(s.trace(X*E)*X+s.trace(Y*E)*Y))
      eq(f'joint_instrument_E{j}{k}_s{sign}',J,target)
      correction=I if sign==1 else Z
      coherent+=correction*J*correction
      uncorrected+=J
      for y in (1,-1):
        Ey=(I+y*X)/2
        weight=w*scalar_mean(s.trace(B*E)*s.trace(Ey*A))
        classical+=weight*(I+sign*y*X)/2
    expected_coh=w/2*(s.trace(E)*I+nu/2*(s.trace(X*E)*X+s.trace(Y*E)*Y))
    expected_cl=w/2*(s.trace(E)*I+nu/2*s.trace(X*E)*X)
    eq(f'coherent_recovery_E{j}{k}',coherent,expected_coh)
    eq(f'classical_recovery_E{j}{k}',classical,expected_cl)
    eq(f'omit_controlled_sign_E{j}{k}',uncorrected,w*s.trace(E)*I/2)

# Exact gate circuit promised by the seven-extra-gate recovery budget.
H=(X+Z)/s.sqrt(2)
CX=s.Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
CXrev=s.Matrix([[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]])
CZ=s.diag(1,1,1,-1)
SW=s.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
eq('controlled_z_three_gate_synthesis',s.kronecker_product(I,H)*CX*s.kronecker_product(I,H),CZ)
eq('swap_three_gate_synthesis',CX*CXrev*CX,SW)
Ug=SW*CZ*s.kronecker_product(H,I)
for j in range(2):
  for k in range(2):
    E=s.zeros(2);E[j,k]=1
    joint=s.zeros(4)
    for sign in (1,-1):
      J=w/4*(s.trace(E)*I+sign*nu/2*(s.trace(X*E)*X+s.trace(Y*E)*Y))
      joint+=s.kronecker_product((I+sign*X)/2,J)
    out=Ug*joint*Ug.conjugate().T
    reduced=s.Matrix(2,2,lambda a,b:sum(out[2*a+c,2*b+c] for c in range(2)))
    target=w/2*(s.trace(E)*I+nu/2*(s.trace(X*E)*X+s.trace(Y*E)*Y))
    eq(f'seven_gate_output_E{j}{k}',reduced,target)

# Independent Pauli decomposition gives CP and exact Bell-complement distance.
qco=[(1+nu)/4,s.Rational(1,4),s.Rational(1,4),(1-nu)/4]
qcl=[(1+nu/2)/4,(1+nu/2)/4,(1-nu/2)/4,(1-nu/2)/4]
for name,q in [('coherent',qco),('classical',qcl)]:
  eq(name+'_pauli_normalization',sum(q),1)
  eq(name+'_complete_error',1-((1-w)+w*q[0]),w*(3-(nu if name=='coherent' else nu/2))/4)
  for a,Q in enumerate([X,Y,Z]):
    channel=sum((qv*Pv*Q*Pv for qv,Pv in zip(q,P)),s.zeros(2))
    factors=[nu/2,nu/2,0] if name=='coherent' else [nu/2,0,0]
    eq(name+'_pauli_axis_'+str(a),channel,factors[a]*Q)
  for nv in [0,s.Rational(1,3),s.Rational(1,2),1]:
    assert all(v.subs(nu,nv)>=0 for v in q)
    checks[name+'_pauli_positive_'+str(nv)]=True

# General clock effect moments, independently integrated.
alpha,bx,by,bz=s.symbols('alpha bx by bz',real=True)
Ey=(alpha*I+bx*X+by*Y+bz*Z)/2
kernel=s.trace(Ey*A)
eq('general_effect_probability',scalar_mean(w*kernel),w*alpha/2)
eq('general_effect_xmoment',scalar_mean(w*kernel*s.cos(theta)),w*nu*bx/4)
eq('general_effect_ymoment',scalar_mean(-w*kernel*s.sin(theta)),w*nu*by/4)
eq('general_effect_zmoment',scalar_mean(w*kernel*0),0)
for m in [0,2,3,-2]:
    Am=(I+nu*(s.cos(m*theta)*X-s.sin(m*theta)*Y))/2
    eq('alias_x_'+str(m),mean(s.cos(theta)*Am),s.zeros(2))
    eq('alias_y_'+str(m),mean(s.sin(theta)*Am),s.zeros(2))
controls['extra_winding_loses_first_harmonic']=True
controls['omitting_sign_control_depolarizes']=True
controls['coherent_access_changes_classical_bound']=bool((w*(3-nu/2)/4-w*(3-nu)/4).subs({w:s.Rational(1,4),nu:1})>0)

# Nonuniform angle laws: general moments cancel after sign correction.
mx,my,aa,bb=s.symbols('mx my aa bb',real=True)
Mplane=s.Matrix([[aa,bb],[bb,1-aa]])
for j in range(2):
  for k in range(2):
    E=s.zeros(2);E[j,k]=1
    rx,ry=s.trace(X*E),s.trace(Y*E)
    tr=s.trace(E)
    corrected=s.zeros(2)
    for sign in (1,-1):
      J=w/4*((tr+sign*(mx*rx+my*ry))*I+nu*((mx*tr+sign*(aa*rx+bb*ry))*X+(my*tr+sign*(bb*rx+(1-aa)*ry))*Y))
      C=I if sign==1 else Z
      corrected+=C*J*C
    target=w/2*(tr*I+nu*((aa*rx+bb*ry)*X+(bb*rx+(1-aa)*ry)*Y))
    eq(f'nonuniform_mean_cancels_E{j}{k}',corrected,target)

# Finite atomic angle law uses rational unit axes, with nonzero cross moment.
axes=[s.Matrix([1,0]),s.Matrix([s.Rational(3,5),s.Rational(4,5)]),s.Matrix([0,-1])]
weights=[s.Rational(1,5),s.Rational(3,10),s.Rational(1,2)]
Mm=sum((a*(v*v.T) for a,v in zip(weights,axes)),s.zeros(2))
mm=sum((a*v for a,v in zip(weights,axes)),s.zeros(2,1))
eq('atomic_moment_trace',s.trace(Mm),1)
checks['atomic_moment_cross_nonzero']=bool(Mm[0,1]!=0)
checks['atomic_moment_positive']=bool(Mm[0,0]>0 and Mm.det()>0)
for j in range(2):
  for k in range(2):
    E=s.zeros(2);E[j,k]=1
    # Independently form the measure/prepare instrument for each atomic angle.
    output=s.zeros(2)
    averaged_dephasing=s.zeros(2)
    for mass,v in zip(weights,axes):
      Q=v[0]*X+v[1]*Y
      Ap=(I+nu*Q)/2
      averaged_dephasing+=mass*((1-nu)*s.trace(E)*I/2+nu*(E+Q*E*Q)/2)
      for sign in (1,-1):
        J=mass*s.trace((I+sign*Q)/2*E)*Ap
        C=I if sign==1 else Z
        output+=C*J*C
    eq(f'atomic_pointer_equals_dephasing_mixture_E{j}{k}',output,averaged_dephasing)
# A constant axis makes the noisy general bound nonoptimal: retain survivor.
# This is the actual constant-axis survivor channel on all matrix units.
constant_choi=s.zeros(4)
for j in range(2):
  for k in range(2):
    E=s.zeros(2);E[j,k]=1
    survivor=sum((s.trace((I+sgn*X)/2*E)*(I+sgn*X)/2 for sgn in (1,-1)),s.zeros(2))
    eq(f'constant_axis_survivor_dephasing_E{j}{k}',survivor,(E+X*E*X)/2)
    constant_choi+=s.kronecker_product(E,survivor)/2
bell=s.Matrix([1,0,0,1])/s.sqrt(2)
constant_error=1-(bell.T*constant_choi*bell)[0]
eq('constant_axis_survivor_bell_error',constant_error,s.Rational(1,2))
controls['nonuniform_noisy_optimum_cannot_be_transferred']=bool(constant_error<1-qco[0].subs(nu,0))

# Exact survivor law under a shaped, nonuniform clock pulse parameter.
u=s.symbols('u',nonnegative=True)
p,q=s.symbols('p q',positive=True)
# A simple smooth phase path s(u)=3u²-2u³ on [0,1].
S=3*u**2-2*u**3
eta=1-q*S
rate=q*s.diff(S,u)/eta
eq('shaped_survival_equation',s.diff(eta,u),-rate*eta)
eq('second_loss_measure',p*rate*eta,p*q*s.diff(S,u))
eq('total_two_loss_probability',s.integrate(p*rate*eta,(u,0,1)),p*q)
eq('shape_zero_start',s.diff(S,u).subs(u,0),0)
eq('shape_zero_end',s.diff(S,u).subs(u,1),0)
# Triangle/trapezoid area and continuous boundary.
G,V=s.symbols('G V',positive=True)
eq('triangle_area',s.sqrt(s.pi/V)*s.sqrt(s.pi*V),s.pi)
eq('trapezoid_area',G*(s.pi/G-G/V)+G**2/V,s.pi)
area=s.symbols('area',positive=True)
eq('pulse_boundary',2*s.sqrt(area/V).subs(area,G**2/V),(area/G+G/V).subs(area,G**2/V))

# Complete noise fixture and strict certified gains, with all good branches.
d=s.symbols('d',real=True)
e0=3*w/4
for name,e in [('classical',w*(3-nu/2)/4),('coherent',w*(3-nu)/4)]:
  gain=e0-e
  actual=d*e+(1-d)*s.Rational(3,4)
  eq(name+'_complete_cost_difference',actual-e0,(1-d)*3*(1-w)/4-d*gain)
  fixture=actual.subs({w:s.Rational(1,4),nu:s.Rational(1,2),d:s.Rational(99,100)})
  assert fixture<s.Rational(3,16)
  checks[name+'_noisy_fixture_improves']=True
  bad=actual.subs({w:s.Rational(1,4),nu:1,d:s.Rational(1,2)})
  controls[name+'_good_branch_cost_can_erase_gain']=bool(bad>s.Rational(3,16))

# Pauli Parseval identity behind arbitrary-CPTP decoder Bell bound.
a,b,c,e=s.symbols('a b c e',real=True)
M=s.Matrix([[a,b],[c,e]])
eq('pauli_parseval_real_matrix',sum(s.trace(M*Q)*s.conjugate(s.trace(M*Q)) for Q in P),2*s.trace(M.T*M))
# Aligned-mean all-CPTP optimization: exact Choi boundary and scalar optimizer.
al_c,al_d=s.symbols('al_c al_d',real=True)
al_x=al_c*al_d
al_t2=(1-al_c**2)*(1-al_d**2)
eq('aligned_Choi_plus_boundary',(1+al_x)**2-al_t2-(al_c+al_d)**2,0)
eq('aligned_Choi_minus_boundary',(1-al_x)**2-al_t2-(al_c-al_d)**2,0)
al_a,al_A,al_B,al_D=s.symbols('al_a al_A al_B al_D',positive=True)
al_z=s.symbols('al_z',real=True)
al_g=al_B*al_z+s.sqrt(al_a**2-al_D*al_z**2)
eq('aligned_objective_derivative',s.diff(al_g,al_z),al_B-al_D*al_z/s.sqrt(al_a**2-al_D*al_z**2))
eq('aligned_objective_concavity',s.diff(al_g,al_z,2),-al_a**2*al_D/(al_a**2-al_D*al_z**2)**s.Rational(3,2))
al_cs=al_a*al_B/s.sqrt(al_D*(al_D+al_B**2))
eq('aligned_stationary_point',s.diff(al_g,al_z).subs(al_z,al_cs),0)
eq('aligned_interior_value',al_g.subs(al_z,al_cs),al_a*s.sqrt((al_D+al_B**2)/al_D))
eq('aligned_interior_domain_numerator',(al_D*(al_D+al_B**2)-al_a**2*al_B**2).subs(al_a**2,al_D+al_A**2),al_D**2-al_A**2*al_B**2)
eq('aligned_threshold_continuity_squared',(al_a**2*(1+al_B**2/al_D)).subs({al_a**2:al_A*(al_A+al_B),al_D:al_A*al_B}),(al_A+al_B)**2)
# Explicit optimal decoder parameters; impose the stated D=a²-A² identity.
al_den=s.sqrt(al_D*(al_D+al_B**2))
al_t=(al_D**2-al_A**2*al_B**2)/(al_D*al_den)
al_x=al_a*al_A*al_B**2/(al_D*al_den)
al_y=al_a*al_B/al_den
al_zz=al_A*al_B/al_D
eq('aligned_optimizer_x_yz',al_x,al_y*al_zz)
eq('aligned_optimizer_translation',s.cancel(al_t**2-(1-al_y**2)*(1-al_zz**2)).subs(al_a**2,al_D+al_A**2),0)
eq('aligned_optimizer_gain',al_a*al_t+al_A*al_x+al_B*al_y,al_a*s.sqrt((al_D+al_B**2)/al_D))

# An actual two-Kraus decoder, including trace preservation and all Bloch axes.
al_alpha,al_beta,al_u,al_v=s.symbols('al_alpha al_beta al_u al_v',real=True)
al_K0=s.diag(s.cos(al_alpha),s.cos(al_beta))
al_K1=s.Matrix([[0,s.sin(al_beta)],[s.sin(al_alpha),0]])
def al_apply(Q):
    return al_K0*Q*al_K0.T+al_K1*Q*al_K1.T
al_tz=s.cos(al_alpha)**2-s.cos(al_beta)**2
al_lz=s.cos(al_alpha)**2+s.cos(al_beta)**2-1
eq('aligned_Kraus_trace_preserving',al_K0.T*al_K0+al_K1.T*al_K1,I)
eq('aligned_Kraus_translation',al_apply(I),I+al_tz*Z)
eq('aligned_Kraus_X',al_apply(X),s.cos(al_alpha-al_beta)*X)
eq('aligned_Kraus_Y',al_apply(Y),s.cos(al_alpha+al_beta)*Y)
eq('aligned_Kraus_Z',al_apply(Z),al_lz*Z)
al_angles={al_alpha:(al_v-al_u)/2,al_beta:(al_v+al_u)/2}
eq('aligned_Kraus_angle_translation',al_tz.subs(al_angles),s.sin(al_u)*s.sin(al_v))
eq('aligned_Kraus_angle_parallel',al_lz.subs(al_angles),s.cos(al_u)*s.cos(al_v))
# Direct Stinespring columns from the two commuting Pauli-product pulses.
al_P=s.kronecker_product(X,Y);al_Q=s.kronecker_product(Y,X)
eq('aligned_dilation_generators_commute',al_P*al_Q-al_Q*al_P,s.zeros(4))
al_U=(s.cos(al_v/2)*s.eye(4)-s.I*s.sin(al_v/2)*al_P)*(s.cos(al_u/2)*s.eye(4)+s.I*s.sin(al_u/2)*al_Q)
for anc,K in [(0,al_K0),(1,al_K1)]:
    induced=s.Matrix(2,2,lambda row,col:al_U[2*row+anc,2*col])
    eq('aligned_dilation_K'+str(anc),induced,K.subs(al_angles))

# Complete sign-paired channel on every matrix unit, with the correct order.
al_mean,al_lam,al_vis,al_tx,al_xx,al_yy,al_zz=s.symbols('al_mean al_lam al_vis al_tx al_xx al_yy al_zz',real=True)
def al_decoder(Q):
    tr=s.trace(Q)
    return (tr*I+(al_tx*tr+al_xx*s.trace(X*Q))*X+al_yy*s.trace(Y*Q)*Y+al_zz*s.trace(Z*Q)*Z)/2

def al_joint(Q,sign):
    tr=s.trace(Q);rx=s.trace(X*Q);ry=s.trace(Y*Q)
    return ((tr+sign*al_mean*rx)*I+al_vis*(al_mean*tr+sign*al_lam*rx)*X+sign*al_vis*(1-al_lam)*ry*Y)/4
for j in range(2):
  for k in range(2):
    E=s.zeros(2);E[j,k]=1
    recovered=al_decoder(al_joint(E,1))+Z*al_decoder(al_joint(E,-1))*Z
    target=(s.trace(E)*I+(al_mean*al_tx+al_vis*al_lam*al_xx)*s.trace(X*E)*X+al_vis*(1-al_lam)*al_yy*s.trace(Y*E)*Y)/2
    eq(f'aligned_complete_recovery_E{j}{k}',recovered,target)
wrong_order=al_decoder(al_joint(I/2,1))+al_decoder(Z*al_joint(I/2,-1)*Z)
eq('aligned_wrong_order_translation',wrong_order,(I+al_tx*X)/2)
controls['nonunital_decoder_requires_correct_sign_order']=bool((wrong_order-I/2).subs(al_tx,4/(3*s.sqrt(3)))!=s.zeros(2))

# Exact interior fixture and endpoints, not a numerical optimum search.
def al_gain(av,lv,nv):
    if av**2<=nv**2*lv:return nv
    AA=nv*lv;BB=nv*(1-lv)
    return s.simplify(av*s.sqrt(1+BB**2/(av**2-AA**2)))
for name,av,lv,nv,expected in [
 ('interior',s.Rational(1,2),s.Rational(1,2),s.Rational(1,2),1/s.sqrt(3)),
 ('zero_visibility',s.Rational(1,2),s.Rational(1,2),s.Integer(0),s.Rational(1,2)),
 ('zero_mean',s.Integer(0),s.Rational(2,3),s.Rational(3,4),s.Rational(3,4)),
 ('zero_all',s.Integer(0),s.Integer(0),s.Integer(0),s.Integer(0)),
 ('zero_lambda',s.Integer(0),s.Integer(0),s.Rational(1,2),s.Rational(1,2)),
 ('antipodal_bias',s.Rational(3,4),s.Integer(1),s.Rational(1,2),s.Rational(3,4)),
 ('antipodal_visibility',s.Rational(1,4),s.Integer(1),s.Rational(3,4),s.Rational(3,4)),
 ('threshold',s.Rational(1,4),s.Rational(1,4),s.Rational(1,2),s.Rational(1,2))]:
    eq('aligned_gain_'+name,al_gain(av,lv,nv),expected)
fx_t=4/(3*s.sqrt(3));fx_x=1/(3*s.sqrt(3));fx_y=1/s.sqrt(3);fx_z=s.Rational(1,3)
eq('aligned_fixture_CP_plus',(1+fx_x)**2-fx_t**2-(fx_y+fx_z)**2,0)
eq('aligned_fixture_CP_minus',(1-fx_x)**2-fx_t**2-(fx_y-fx_z)**2,0)
checks['aligned_fixture_CP_diagonals']=bool(1-fx_x>fx_t)
fx_g=s.Rational(1,2)*fx_t+s.Rational(1,4)*fx_x+s.Rational(1,4)*fx_y
eq('aligned_fixture_gain',fx_g,1/s.sqrt(3))
controls['interior_recovery_beats_ignore_pointer_and_robust_decoder']=bool(fx_g>s.Rational(1,2))
# Physical moment fixture: +X mass1/2 and +-Y masses1/4.
fx_axes=[s.Matrix([1,0]),s.Matrix([0,1]),s.Matrix([0,-1])]
fx_weights=[s.Rational(1,2),s.Rational(1,4),s.Rational(1,4)]
fx_mean=sum((prob*axis for prob,axis in zip(fx_weights,fx_axes)),s.zeros(2,1))
fx_moment=sum((prob*axis*axis.T for prob,axis in zip(fx_weights,fx_axes)),s.zeros(2))
eq('aligned_fixture_mean',fx_mean,s.Matrix([s.Rational(1,2),0]))
eq('aligned_fixture_second_moment',fx_moment,s.eye(2)/2)
# Explicit Pauli channel for the attained fixture gives exact Bell complement.
fx_d1=s.Rational(1,2)*fx_t+s.Rational(1,4)*fx_x
fx_d2=s.Rational(1,4)*fx_y
fx_pauli=[(1+fx_d1+fx_d2)/4,(1+fx_d1-fx_d2)/4,(1-fx_d1+fx_d2)/4,(1-fx_d1-fx_d2)/4]
eq('aligned_fixture_pauli_sum',sum(fx_pauli),1)
checks['aligned_fixture_pauli_positive']=bool(all(value>=0 for value in fx_pauli))
eq('aligned_fixture_complete_error',w*(1-fx_pauli[0]),w*(3-1/s.sqrt(3))/4)

# Explicit cyclic basis bridge from the Kraus Z-axis convention to the theorem.
al_W=(I-s.I*(X+Y+Z))/2
al_Wd=al_W.conjugate().T
eq('aligned_cyclic_rotation_unitary',al_W*al_Wd,I)
for name,Pin,Pout in [('X',X,Y),('Y',Y,Z),('Z',Z,X)]:
    eq('aligned_cyclic_rotation_'+name,al_W*Pin*al_Wd,Pout)
eq('aligned_physical_Kraus_translation',al_W*al_apply(I)*al_Wd,I+al_tz*X)

assert all(checks.values())
assert all(controls.values())
report={'result_id':'K2389','checks':len(checks),'check_names':checks,
        'changed_input_or_inference_controls':controls,
        'scope':'Exact supplied finite-channel instruments, analytic all-CPTP optima and conditional costs; no measured apparatus or GU bridge.'}
root=Path(__file__).resolve().parents[2]
report['dependencies']={}
for f in ['lab/process/k2380-complete-erasure-recovery.json','lab/process/k2383-driven-erasure-recovery.json','lab/process/k2386-finite-timing-recovery.json']:
    path=root/f
    report['dependencies'][f]=hashlib.sha256(path.read_bytes()).hexdigest()
parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args()
encoded=json.dumps(report,indent=2,sort_keys=True)+'\n'
if args.output:Path(args.output).write_text(encoded)
else:print(encoded)
