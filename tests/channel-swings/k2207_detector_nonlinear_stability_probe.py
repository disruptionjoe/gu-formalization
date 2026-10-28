#!/usr/bin/env python3
"""Exact nonlinear identities and a rational all-tail certificate consumer."""
import sys
sys.dont_write_bytecode=True
from fractions import Fraction as F
from pathlib import Path
import argparse,hashlib,json
import sympy as S
sys.path.insert(0,str(Path(__file__).resolve().parent))
from k2168_finite_budget_moment_envelope_probe import IV,squeeze,sqrtq
from k2204_detector_infinite_stability_certificate_probe import roots,z,p,q,form,branch_moments
ROOT=Path(__file__).resolve().parents[2]
C=F(40,3)
def aa(s):return F(41,6)*s*s+F(3,2)/(s*s)
def ap(s):return F(41,3)*s-3/(s*s*s)
def app(s):return F(41,3)+9/(s*s*s*s)
def gradT(n,j):
    return (n*roots(n-1)[j]/roots(n)[j] if n else 0)+(n+1)*roots(n+1)[j]/(4*roots(n)[j])
def controls(fault=None):
    out={}
    def ck(k,v):out[k]=bool(v)
    a,b,u,v,t=S.symbols('a b u v t',positive=True)
    edge=S.sqrt((a+t*u)*(b+t*v))
    claimed=(u*b-v*a)**2/((2 if fault=='edge_factor' else 4)*((a+t*u)*(b+t*v))**S.Rational(3,2))
    ck('exact_directional_edge',S.simplify(-S.diff(edge,t,2)-claimed)==0)
    s=S.symbols('s',positive=True);A=S.Rational(41,6)*s*s+S.Rational(3,2)/s**2
    ck('squeeze_second_derivative',S.simplify(S.diff(A,s,2)-S.Rational(41,3)-9/s**4)==0)
    ck('squeeze_elasticity',S.simplify(s*S.diff(A,s,2)-S.diff(A,s)-(6 if fault=='elasticity_factor' else 12)/s**3)==0)
    ck('squeeze_third_derivative',S.diff(A,s,3)==-36/s**5)
    r=S.symbols('r',nonnegative=True);g=(1+r)/(1-r)**3-1
    ck('g_derivative_identity',S.simplify(S.diff(g,r)-(4+2*r)/(1-r)**4)==0)
    ck('uniform_g_constant',F(128,9)<15)
    ck('uniform_h_constant',F(6400,729)<9)
    eta=S.symbols('eta',positive=True)
    ck('schur_lower_margin',S.expand((1-eta/2)**2-(1-eta))==eta**2/4)
    ck('reoptimized_radius_identity',S.simplify(2*(eta/180)/(1-eta/180)/(eta/60)-120/(180-eta))==0)
    ck('reoptimized_radius_endpoint',F(120,179)<1)
    # Original nonlinear edge with exact square-root endpoints.
    za,zb,wa,wb=F(1),F(4),F(81,1600),F(161,1600)
    R=(za+3*zb)/2;Rw=(wa+3*wb)/2;T=F(2);Tnew=F(3321,1600)
    ck('rational_edge_endpoint_root',Tnew*Tnew==(za+wa)*(zb+wb))
    DT=T/2*(wa/za+wb/zb);FF=T/4*(wa/za-wb/zb)**2
    ss,tt=F(1),F(1,100)
    E0=aa(ss)*R-C*ss*T;E1=aa(ss+tt)*(R+Rw)-C*(ss+tt)*Tnew
    linear=aa(ss)*Rw-C*ss*DT+(ap(ss)*R-C*T)*tt
    Q=C*ss*FF;d=R*app(ss);score=ap(ss)*Rw-C*DT
    rem=E1-E0-linear-(Q+(0 if fault=='omit_mixed_score' else 2*score*tt)+d*tt*tt)/2
    delta=max(abs(wa/za),abs(wb/zb));eps=abs(tt/ss)
    gg=(1+eps)/(1-delta)**3-1;hh=F(4,3)*eps/(1-eps)**5+delta/(1-eps)**4
    ck('actual_nonlinear_edge_remainder',2*abs(rem)<=gg*Q+hh*d*tt*tt)
    # Actual predecessor rational profile and fresh squeeze brackets from its
    # certified moment formula; no replay of the unchanged Galerkin bank.
    sq=[]
    for j in range(2):
        rr,tm=branch_moments(j);sq.append(squeeze(C*tm/rr))
    ck('actual_squeeze_lower',all(s.a>F(4,5) for s in sq))
    ck('actual_D_upper',F(5,6)*(F(41,3)+9*F(5,4)**4)<30)
    inherited=json.loads((ROOT/'lab/process/k2204-detector-infinite-stability-certificate.json').read_text())
    cert=inherited['full_tail_fixture']
    margin=F(cert['released_rational_margins']['schur_lower_greater_than_identity_multiple'])
    if fault=='inherited_margin':margin=F(1)
    ck('inherited_certificate_stable',cert['decision']=='STABLE')
    ck('actual_eta_from_inherited_margin',margin>=F(1,5)*30)
    ck('inherited_dependency_bytes',all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in inherited['dependency_sha256'].items()) and inherited['probe_sha256']==hashlib.sha256((ROOT/'tests/channel-swings/k2204_detector_infinite_stability_certificate_probe.py').read_bytes()).hexdigest())
    expected=(F(25,68),F(5,34),F(799,650),F(51,26))
    actual=(gradT(0,0),gradT(0,1),gradT(1,0),gradT(1,1))
    ck('actual_profile_gradients',actual==expected)
    H=[]
    for n in [0,1]:
        H.append((F(n)+F(1,2))*(aa(sq[0])-aa(sq[1]))-C*(sq[0]*gradT(n,0)-sq[1]*gradT(n,1)))
    direction=(2,-1) if fault=='contrast_direction' else (2,1)
    ck('actual_descent_constraint',q(0)*direction[0]+q(1)*direction[1]==0)
    derivative=2*H[0]+H[1]
    ck('actual_nonstationarity_certificate',derivative.a>F(2))
    step=F(1,100000);direction_v=[-2*step,-step,F(0)]
    cap=max(abs(direction_v[n])/min(z(n,0),z(n,1)) for n in [0,1])
    ck('actual_descent_step_inside_relative_radius',cap<=F(1,900))
    change=IV(0)
    for j in range(2):
        wv=[v*(1 if j==0 else -1) for v in direction_v]
        dr=sum((F(n)+F(1,2))*v for n,v in enumerate(wv))
        dt=IV(0)
        for n in [0,1]:
            before=p(n)*roots(n)[j]*roots(n+1)[j]/2
            after=sqrtq((z(n,j)+wv[n])*(z(n+1,j)+wv[n+1]))
            dt+=(n+1)*(after-before)
        change+=aa(sq[j])*dr-C*sq[j]*dt
    ck('actual_feasible_finite_energy_descent',change.b<0)
    linear=IV(0) if fault=='discard_first_variation' else -step*derivative
    qform=form(direction_v,direction_v,sq)
    ck('actual_nonlinear_tangent_bound',(change-linear-qform/40).a>=0)

    spikes=[]
    for N in [8,16,32]:
        vv=[F(0)]*(N+1);vv[N]=2*z(N,1);vv[0]=2*q(N)*z(N,1)
        if fault=='tail_spike_repair':vv[0]=-vv[0]
        ck('tail_spike_constraint_'+str(N),sum(q(n)*v for n,v in enumerate(vv))==0)
        ck('tail_spike_crosses_cap_'+str(N),z(N,0)+vv[N]>p(N))
        spikes.append(form(vv,vv,[F(1),F(1)]))
    ck('actual_tail_spike_Q_shrinks',spikes[0]>spikes[1]>spikes[2]>0)
    ck('actual_tail_spike_Q_small',spikes[-1]<F(1,10**30))
    return out,dict(squeezes=[s.pair() for s in sq],descent_derivative=derivative.pair(),finite_descent_energy=change.pair(),finite_step=str(step),cap_norm=str(cap),tail_spike_Q=[str(x) for x in spikes],eta='1/5',joint_radius='1/300',reduced_radius='1/900',growth_coefficient='1/40',is_stationary=False)

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--write',action='store_true');args=pa.parse_args()
    cs,fixture=controls();assert all(cs.values()),[k for k,v in cs.items() if not v]
    faults={}
    for f in ['edge_factor','elasticity_factor','omit_mixed_score','contrast_direction','discard_first_variation','tail_spike_repair','inherited_margin']:
        bad=[k for k,v in controls(f)[0].items() if not v];assert bad,('undetected',f);faults[f]=bad
    deps=['explorations/conditional-build/k2207-detector-nonlinear-stability-2026-10-28.md','explorations/conditional-build/k2204-detector-infinite-stability-certificate-2026-10-28.md','lab/process/k2204-detector-infinite-stability-certificate.json','tests/channel-swings/k2204_detector_infinite_stability_certificate_probe.py','tests/channel-swings/k2168_finite_budget_moment_envelope_probe.py']
    report=dict(result_id='K2207',status='nonlinear_tangent_model_and_conditional_local_minimum',checks=cs,fault_failures=faults,actual_fixture=fixture,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),evidence_kinds='Universal all-tail directional remainder proof; symbolic identities; rational nonlinear edge; inherited K2204 Schur certificate reused; fresh rigorous squeeze/gradient and tail-spike controls. Actual fixture is nonstationary, so no local-minimum or optimizer claim.')
    dst=ROOT/'lab/process/k2207-detector-nonlinear-stability.json'
    if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(dst.read_text())==report,'report drift'
    print(json.dumps(dict(result='K2207',controls=len(cs),faults=len(faults),gradient_interval_display=[float(F(x)) for x in fixture['descent_derivative']])) )
if __name__=='__main__':main()
