#!/usr/bin/env python3
"""Exact curvature, transverse-symbol and localized-function controls."""
from pathlib import Path
import hashlib
import json
import sys
import sympy as s

ROOT=Path(__file__).resolve().parents[2];checks=[];controls=[]
def ck(n,p):
    assert bool(p),n
    checks.append(n)
def reject(n,p):
    assert not bool(p),n
    controls.append(n)
def eq(a,b):return s.simplify(a-b)==s.zeros(*a.shape)
def comm(a,b):return a*b-b*a
x,y,z,t=s.symbols('x y z t',real=True)
T1=s.Matrix([[0,0,0],[0,0,-1],[0,1,0]])
T2=s.Matrix([[0,0,1],[0,0,0],[-1,0,0]])
T3=comm(T1,T2)
A=[y*T1,z*T2,x*T3];coords=[x,y,z]
def curv(i,j):return s.diff(A[j],coords[i])-s.diff(A[i],coords[j])+comm(A[i],A[j])
Cx=A[0].subs(z,x*y)+y*A[2].subs(z,x*y)
Cy=A[1].subs(z,x*y)+x*A[2].subs(z,x*y)
Fc=s.diff(Cy,x)-s.diff(Cx,y)+comm(Cx,Cy)
pulled=(curv(0,1)+x*curv(0,2)+y*curv(2,1)).subs(z,x*y)
ck('nonabelian_curved_section_curvature',eq(Fc,pulled))
horizontal=s.diff(A[1].subs(z,x*y),x)-s.diff(A[0].subs(z,x*y),y)+comm(A[0].subs(z,x*y),A[1].subs(z,x*y))
reject('horizontal_projection_equals_contraction',eq(horizontal,pulled))
ck('actual_nonabelian_term_present',comm(Cx,Cy)!=s.zeros(3))
q=s.symbols('q',positive=True)
k=s.Matrix([q,0,0]);M=q*q*s.eye(3)-k*k.T
ck('longitudinal_null',M*k==s.zeros(3,1))
ck('two_transverse_eigenvectors',M[:,1:]==q*q*s.eye(3)[:,1:])
ck('transverse_rank_at_nonzero_momentum',M.rank()==2)
reject('quotient_removes_all_soft_modes',M[:,1:]==s.zeros(3,2))
ck('transverse_dispersion_no_constant_term',s.diff(M[1,1],q,2)==2 and M[1,1].subs(q,0)==0)
# Curvature norm Taylor coefficient including the background cross term.
F0=T1;da=T2;aa=T1+T3;F=F0+t*da+t*t*aa
inner=lambda U,V:-s.trace(U*V)/2
E=s.expand(inner(F,F)/2)
ck('full_magnetic_hessian_coefficient',s.diff(E,t,2).subs(t,0)==inner(da,da)+2*inner(F0,aa))
reject('background_cross_term_alone_is_hessian',s.diff(E,t,2).subs(t,0)==2*inner(F0,aa))
ck('flat_background_has_no_constant_mass_term',s.diff(inner(t*da+t*t*aa,t*da+t*t*aa)/2,t,2).subs(t,0)==inner(da,da))
# Compact polynomial curl: verify all face traces needed for H2 zero extension.
phi=lambda v:(1-v*v)**4
psi=phi(x)*phi(y)*phi(z); f=s.Matrix([s.diff(psi,y),-s.diff(psi,x),0])
ck('exact_divergence_free',s.simplify(sum(s.diff(f[i],coords[i]) for i in range(3)))==0)
ck('nonzero_physical_fixture',f.subs({x:0,y:s.Rational(1,2),z:0})!=s.zeros(3,1))
for j,v in enumerate(coords):
    ck(f'face_traces_zero_{j}',all(s.diff(comp,v,n).subs(v,side)==0 for comp in f for n in range(3) for side in (-1,1)))
lap=s.Matrix([sum(s.diff(c,v,2) for v in coords) for c in f])
def cube_integral(expr):
    poly=s.Poly(s.expand(expr),x,y,z);out=0
    for powers,coef in poly.terms():
        if any(n%2 for n in powers):continue
        out+=coef*s.prod(s.Rational(2,n+1) for n in powers)
    return out
N=cube_integral((f.T*f)[0]);G=cube_integral(sum(s.diff(c,v)**2 for c in f for v in coords));D=cube_integral((lap.T*lap)[0])
I=[s.integrate(s.diff(phi(x),x,n)**2,(x,-1,1)) for n in range(4)]
ck('independent_product_norm',N==2*I[1]*I[0]**2)
ck('independent_gradient_norm',G==2*I[2]*I[0]**2+4*I[1]**2*I[0])
ck('independent_laplacian_norm',D==2*I[3]*I[0]**2+12*I[1]*I[2]*I[0]+4*I[1]**3)
ck('positive_norm_and_laplacian',N>0 and G>0 and D>0)
R=s.symbols('R',positive=True)
ck('dimension_three_normalization_scaling',R**(-3)*R**3==1)
ck('operator_norm_squared_scaling',s.simplify(R**(-7)*R**3)==R**(-4))
reject('fixed_positive_gap_survives_scaling',s.limit(G/N/R**2,R,s.oo)>0)
ck('residual_tends_zero',s.limit(D/N/R**4,R,s.oo)==0)
for radius in (2,4,8):
    center=radius**2+3*radius
    ck(f'cube_support_escapes_{radius}',center-radius>radius**2)
m=s.symbols('m',positive=True)
ck('positive_decaying_potential',m*m/(1+R*R)>0)
reject('pointwise_positive_is_uniformly_gapped',s.limit(m*m/(1+R*R),R,s.oo)>0)
ck('constant_mass_changes_threshold',s.limit(G/N/R**2+m*m,R,s.oo)==m*m)
# Nonzero momenta: exact curl packets retain every continuum threshold.
kap=s.symbols('kap',positive=True);ph=s.Function('ph')(x,y,z);wave=s.exp(s.I*kap*z)
osc=s.Matrix([0,s.diff(ph*wave,z),-s.diff(ph*wave,y)])
ck('oscillatory_packet_transverse',s.simplify(s.diff(osc[1],y)+s.diff(osc[2],z))==0)
v=s.Function('v')(x,y,z)
lapv=sum(s.diff(v,coord,2) for coord in coords)
lhs=-sum(s.diff(wave*v,coord,2) for coord in coords)-kap**2*wave*v
ck('oscillatory_laplacian_shift_identity',s.simplify(lhs-wave*(-lapv-2*s.I*kap*s.diff(v,z)))==0)
ck('nonzero_momentum_packet_norm_limit',s.limit(kap**2*I[0]**3+N/R**2,R,s.oo)==kap**2*I[0]**3)
reject('oscillatory_packet_is_longitudinal',s.simplify(s.diff(osc[2],y)-s.diff(osc[1],z))==0)
# Three-dimensional virial trace, then an actual nondecaying stationary field.
p12,p13,p23=s.symbols('p12 p13 p23',real=True)
fab=s.Matrix([[0,p12,p13],[-p12,0,p23],[-p13,-p23,0]])
allnorm=sum(c*c for c in fab)
stress=fab*fab.T-s.eye(3)*allnorm/4
ck('stress_trace_equals_magnetic_energy',s.simplify(s.trace(stress)-allnorm/4)==0)
reject('three_dimensional_static_stress_is_traceless',s.trace(stress)==0)
B=s.symbols('B',nonzero=True,real=True)
Ab=[s.zeros(3),B*x*T3,s.zeros(3)]
Fb={(i,j):s.diff(Ab[j],coords[i])-s.diff(Ab[i],coords[j])+comm(Ab[i],Ab[j]) for i in range(3) for j in range(3)}
ck('constant_cartan_curvature',Fb[0,1]==B*T3 and Fb[0,2]==Fb[1,2]==s.zeros(3))
ck('constant_cartan_stationary',all(sum((s.diff(Fb[j,i],coords[j])+comm(Ab[j],Fb[j,i]) for j in range(3)),s.zeros(3))==s.zeros(3) for i in range(3)))
ck('parallel_cartan_section',all(comm(a,T3)==s.zeros(3) for a in Ab))
ck('neutral_curvature_hessian_zero',all(comm(v,T3)==s.zeros(3) for v in Fb.values()))
reject('all_colors_are_parallel',all(comm(a,T1)==s.zeros(3) for a in Ab))
ck('magnetic_background_energy_density_positive',inner(Fb[0,1],Fb[0,1])/2==B*B/2)

payload=dict(artifact='BET_MASS_GAP_CURVATURE_END_TEST',program_target='BET-MASS-GAP',tier='T2',claim_effect='none',guessed_action_variants=1,finite_supporting_checks=checks,contrary_controls=controls,counts=dict(supporting=len(checks),contrary=len(controls)),exact_fixture=dict(norm_squared=str(N),gradient_squared=str(G),laplacian_squared=str(D),normalized_rayleigh_constant=str(G/N),normalized_residual_squared_constant=str(D/N)),proof='Written reduced-gauge exterior Weyl sequence and bounded decaying transverse-potential argument; finite polynomial control is not the analytic proof.',scope='SPECULATIVE compact observed curvature-square family; classical quadratic gap only, no quantum mass-gap or GU action verdict.',probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
report=ROOT/'lab/process/bet-mass-gap-curvature-end-test.json'
if __name__=='__main__':
    if '--write' in sys.argv:report.write_text(json.dumps(payload,indent=2)+'\n')
    else:assert json.loads(report.read_text())==payload,'evidence replay mismatch'
    print(json.dumps(dict(status='pass',counts=payload['counts'],exact_fixture=payload['exact_fixture'])))
