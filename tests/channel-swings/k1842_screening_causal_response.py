#!/usr/bin/env python3
"""Exact identities; continuum support theorem is proved in the research note."""
from pathlib import Path
import json, hashlib
import sympy as s
ROOT=Path(__file__).resolve().parents[2]

def produce():
    checks={}
    def ck(name, condition):
        checks[name]=bool(condition)
        assert condition,name
    t,z,mu,gamma,c,k,f=s.symbols('t z mu gamma c k f', positive=True)
    n=5; one=s.ones(n,1); Pi=one*one.T/n; Q=s.eye(n)-Pi
    ck('projector',Q*Q==Q);ck('constant_annihilation',Q*one==s.zeros(n,1));ck('mean_constraint',one.T*Q==s.zeros(1,n))
    diff=s.Matrix([[1,-1,0,0,0]])
    ck('difference_readout',diff*Q==diff)
    h=s.Matrix([1,-1,2,-3,1]);ck('zero_mean_intervention',Q*h==h)
    remote=s.Matrix([0,0,0,0,1]);ck('remote_algebraic_response',(Q*remote)[0]==-s.Rational(1,5))
    eta=t**2*(1-t)**2
    u=s.integrate((t-z)*eta.subs(t,z),(z,0,t))
    ck('retarded_zero_mode_ode',s.simplify(s.diff(u,t,2)-eta)==0)
    ck('zero_data',u.subs(t,0)==0 and s.diff(u,t).subs(t,0)==0)
    ck('pulse_response',u.subs(t,1)==s.Rational(1,60))
    chi=f*(1-(1+mu*t)*s.exp(-mu*t))
    ck('critical_damping',s.simplify(s.diff(chi,t,2)+2*mu*s.diff(chi,t)+mu**2*chi-mu**2*f)==0)
    ck('auxiliary_zero_data',chi.subs(t,0)==0 and s.diff(chi,t).subs(t,0)==0)
    residual=f-chi
    ck('late_forcing',s.limit(residual,t,s.oo)==0)
    ck('velocity_memory',s.integrate(residual,(t,0,s.oo))==2*f/mu)
    N=z**2+gamma*z+c**2*k**2;qc=N/(N+mu**2)
    ck('not_projection',s.simplify(qc**2-qc+mu**2*N/(N+mu**2)**2)==0)
    ck('dc_zero',qc.subs({z:0,k:0})==0)
    ck('high_frequency_pass',s.limit(qc,z,s.oo)==1)
    ck('static_spatial_response',s.simplify(qc.subs(z,0)-c**2*k**2/(c**2*k**2+mu**2))==0)
    q=s.Symbol('q')
    ck('exact_projection_roots',set(s.solve(q*q-q,q))=={0,1})
    return {'artifact':'K1842','scope':'conditional_scalar_response_only','mathematical_checks':checks,
            'analytic_proof':'explorations/conditional-build/k1842-screening-causal-response-2026-10-20.md',
            'continuum_support_proved_by':'finite propagation plus positive zero-mode integral, not finite matrix',
            'source_owned':False,'all_nonlocal_theories_excluded':False,'causal_repair_exact_projector':False,
            'causal_repair_erases_history':False,'ledger_changes':False}
if __name__=='__main__':
    out=produce();path=ROOT/'lab/process/k1842-screening-causal-response.json'
    path.write_text(json.dumps(out,indent=2)+'\n');print('K1842 exact groups:',len(out['mathematical_checks']))
