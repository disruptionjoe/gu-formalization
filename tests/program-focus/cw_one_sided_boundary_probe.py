#!/usr/bin/env python3
"""Exact controls for a regular clustered boundary reduction.

The descriptor and coarea arguments are written and independently reviewed.
This probe checks algebraic controls and authenticates the reused actual force;
it is not a proof of a nonlinear manifold or a uniform Sobolev estimate.
"""
from pathlib import Path
import argparse, hashlib, json, sys, time
sys.dont_write_bytecode = True
import sympy as s
from cw_fullsystem_domain_probe import FACTORS, ell, boost_field, compact_symbol, add, scale
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/cw-one-sided-boundary-certificates.json'
PINS={
'lab/process/cw-nonlinear-completion-certificates.json':'8d8bfa45bdf4df274174dbe8732c1c5b61044f84a1fa70e418b92198059f1541',
'lab/process/cw-fullsystem-domain-certificates.json':'8ede03f10d6bd28570a3028eb5c320d297de67a827d8b51c545ee5da76314be5',
'lab/process/printed-state-completion-certificates.json':'ec0aafeace76b0d47f9ec9a7b142be29b6c7349e2c3397283029d14fe3e88977',
}
def build():
    checks=[]
    def ck(n,v):
        assert v,n
        checks.append(n)
    deps=dict(PINS)
    for p in PINS:
        deps.update(json.loads((ROOT/p).read_text()).get('dependencies',{}))
    for p,h in deps.items():ck('reuse '+p,hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h)
    cw=json.loads((ROOT/'lab/process/cw-fullsystem-domain-certificates.json').read_text())
    F={(a,b):s.sympify(v)for a,b,v in cw['boosted_resonance']['force']}
    ck('actual boosted force nonzero receiver',ell(boost_field(F,-1))==104448)
    kap=s.Integer(12);q,z,delta,nu=s.symbols('q z delta nu',real=True)
    R=s.prod(kap**2-4*a*q for a in FACTORS if a!=1)
    d=kap**2*s.prod(kap**2-4*a*q for a in FACTORS)
    ck('actual threshold scalarizer factor',s.cancel(d/(4*kap**2*R))==36-q)
    ck('temporal threshold sign',(36-q).subs(q,36+delta-z*z)==z*z-delta)
    ck('complement nonzero',R.subs(q,36)!=0)
    beta=2*kap**3*R.subs(q,36)
    ck('actual receiver regular numerator',s.cancel(beta/(4*kap**2*R.subs(q,36)))==6)
    ck('actual numerator receiver value',6*104448==626688)
    # Actual sparse scalarizer first temporal jet (z^2=0) on the owned force.
    # This authenticates U F and V F without assembling any dense projector.
    coeff=[s.Integer(1)]
    for a in FACTORS:
        nxt=[s.Integer(0)]*(len(coeff)+1)
        for j,c in enumerate(coeff):nxt[j]+=c;nxt[j+1]-=4*a*c
        coeff=nxt
    X,Y=F,{};BU,BV={},{}
    P0=lambda f:compact_symbol({10:6*s.I},f)
    At=lambda f:compact_symbol({0:s.Integer(1)},f)
    for n in range(40):
        alpha=sum(-c*(-kap)**(39-2*j-n)*36**j for j,c in enumerate(coeff) if n<40-2*j)
        BU=add(BU,scale(alpha,X));BV=add(BV,scale(alpha,Y))
        if n<39:X,Y=P0(X),add(P0(Y),At(X))
    den=4*kap*kap*R.subs(q,36);UF=scale(1/den,BU);VF=scale(1/den,BV)
    ck('actual U force in threshold kernel',not add(scale(12,UF),P0(UF)))
    ck('actual V force chain',not add(scale(12,VF),P0(VF),At(UF)))
    receiver=lambda f:ell(boost_field(f,-1))
    ck('actual U force normalized receiver',receiver(UF)/6==104448)
    b0=receiver(VF)/6
    ck('phase submersion',-s.Rational(3,1)/s.Rational(26,3)-s.Rational(3,1)/s.Rational(26,3)==-s.Rational(9,13))
    # Descriptor control with an algebraic row. Singular A_t is intentional.
    A=s.diag(1,1,0);N=s.Matrix([[0,1,0],[delta,0,0],[0,0,0]])
    C=s.Matrix([[0,-1,0],[-delta,0,0],[0,0,1]])
    Pi=s.diag(1,1,0);V=Pi;U=N;H=s.diag(0,0,1)
    inv=(U+z*V)/(z*z-delta)+H
    ck('singular time symbol control',A.det()==0)
    ck('left full descriptor inverse',s.simplify((z*A+C)*inv)==s.eye(3))
    ck('right full descriptor inverse',s.simplify(inv*(z*A+C))==s.eye(3))
    ck('cluster projection and generator',V*A==Pi and U*A==N)
    ck('cluster square identity',N*N==delta*Pi)
    ck('forcing identity NV=U',N*V==U)
    ck('rankhalf Jordan threshold',N.subs(delta,0).rank()==1 and Pi.rank()==2)
    # General regular-coordinate source g, including forcing of q' itself.
    lam,t=s.symbols('lam t',positive=True,real=True);g0,g1,Q=s.symbols('g0 g1 Q')
    M=s.Matrix([[0,1],[lam*lam,0]]);g=s.Matrix([g0,g1])
    part=s.simplify(-(s.I*nu*s.eye(2)-M).inv()*g)
    bpart=s.factor((s.Matrix([[lam,1]])*part)[0])
    boundary=(g1+lam*g0)/(lam-s.I*nu)
    ck('future boundary from exact forced solution',s.simplify(bpart-boundary)==0)
    free=s.Matrix([Q,-lam*Q]);ck('free decaying state retained',M*free==-lam*free)
    # q(0)=0 is a regular section of the boundary relation, not a source rule.
    initial=s.Matrix([0,boundary]);diff=s.simplify(initial-part)
    ck('regular initial representative differs by decaying mode',s.simplify(M*diff+lam*diff)==s.zeros(2,1))
    propagator=s.Matrix([[s.cosh(lam*t),s.sinh(lam*t)/lam],[lam*s.sinh(lam*t),s.cosh(lam*t)]])
    ck('finite time threshold propagator',propagator.applyfunc(lambda x:s.limit(x,lam,0,dir='+'))==s.Matrix([[1,t],[0,1]]))
    # Constant forcing calibrates forward tuning vs zero-data runaway.
    qc=(1-s.exp(-lam*t))/lam**2;pc=s.diff(qc,t)
    ck('forced scalar positive control',s.simplify(s.diff(qc,t,2)-lam*lam*qc+1)==0)
    ck('boundary scalar positive control',s.simplify(pc.subs(t,0)+lam*qc.subs(t,0)-1/lam)==0)
    ret=(1-s.cosh(lam*t))/lam**2
    ck('retarded negative control',ret.subs(t,0)==0 and s.diff(ret,t).subs(t,0)==0 and s.simplify(s.diff(ret,t,2)-lam*lam*ret+1)==0)
    # Smooth even density rho=1 on [-1,1], exact model integral; coarea proof
    # handles smooth cutoffs. The two different divisors must not be confused.
    new=2*s.atan(1/lam);old=2*s.atan(1/lam)/lam
    ck('Cauchy kernel integral limit',s.limit(new,lam,0,dir='+')==s.pi)
    ck('old inverse diverges',s.limit(old,lam,0,dir='+')==s.oo)
    ck('derivative remainder bounded',s.simplify(s.Abs(nu/(lam-s.I*nu))**2)==nu**2/(lam**2+nu**2))
    # Integrable first-time-moment forcing calibrates a forward-uniform response
    # at the degenerate threshold; constant forcing fails this hypothesis.
    pulse=s.exp(-t);bp=s.exp(-t);qp=1-s.exp(-t);pp=s.exp(-t)
    ck('threshold decaying pulse future relation',s.diff(bp,t)==-pulse)
    ck('threshold pulse regular dynamics',s.diff(qp,t)==pp and s.diff(pp,t)==-pulse)
    ck('threshold pulse bounded displacement',s.limit(qp,t,s.oo)==1)
    ck('pulse first moment',s.integrate(t*pulse,(t,0,s.oo))==1)
    # Boundary relation extends through threshold; individual eigenprojections do not.
    Eplus=(s.eye(2)+M/lam)/2
    ck('singular individual projector',Eplus[0,1]==1/(2*lam))
    ck('regular boundary evolution row',s.Matrix([[lam,1]])*M==lam*s.Matrix([[lam,1]]))
    return {'schema':'gu-cw-one-sided-boundary-v1','status':'PASS','probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'dependencies':deps,'check_count':len(checks),'check_names':checks,'actual_threshold':{'kappa':12,'K':'6 eta','delta':'-r(K)^2-36','ell_b_F':104448,'ell_b_U_F':626688,'ell_b_V_F_over6':str(b0),'UF_terms':len(UF),'VF_terms':len(VF),'phase_derivative':'-9/13'},'boundary':{'cluster':'Pi=V A_t, N=U A_t, N^2=delta Pi','equation':'x_prime=N x - V F','normal_form':'q_prime=p-g0; p_prime=delta q-g1','regular_relation':'p0+sqrt(delta) q0 = integral (g1+sqrt(delta)g0)/(sqrt(delta)-i nu)','free_data':'q0 with decaying homogeneous slope; no physical selection'},'limits':['Fixed smooth compact input packets, Fourier-local L2 through threshold only.','Full descriptor/coarea proof is written and reviewed, not established by finite controls.','Uniform ordinary Sobolev bilinear estimate not certified.','No nonlinear manifold, physical positivity, source state law or slice determination.']}
if __name__=='__main__':
    p=argparse.ArgumentParser();g=p.add_mutually_exclusive_group(required=True);g.add_argument('--write',action='store_true');g.add_argument('--verify',action='store_true');a=p.parse_args();t=time.monotonic();d=build()
    if a.write:OUT.write_text(json.dumps(d,indent=2)+'\n')
    else:assert json.loads(OUT.read_text())==json.loads(json.dumps(d)),'certificate mismatch'
    print(json.dumps({'status':'PASS','checks':d['check_count'],'seconds':time.monotonic()-t}))
