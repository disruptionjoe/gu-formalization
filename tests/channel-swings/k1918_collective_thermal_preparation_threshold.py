#!/usr/bin/env python3
"""Exact thermal shell selection; no numerical asymptotic claim from samples."""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import json,hashlib,argparse
ROOT=Path(__file__).resolve().parents[2];REPORT=ROOT/'lab/process/k1918-collective-thermal-preparation-threshold.json'
def shell(N,q):
    assert N>=1 and 0<=q<=Q(2,3)
    s=3**N//2**N;used=0;mass=Q(0)
    for j in range(N+1):
        n=comb(N,j)*2**j;take=min(n,s-used);mass+=take*(q/2)**j*(1-q)**(N-j);used+=take
        if used==s:return mass,j,take,n
    raise AssertionError('insufficient shell count')
def entropy_compare(num,den):
    # exp(den*(f(num/den)-log(3/2))) compared with 1.
    return (den**den*2**(num+den),num**num*(den-num)**(den-num)*3**den)
def payload():
    checks=[]
    def test(ok,label):assert ok,label;checks.append(label)
    for N in [1,2,3,5,10,30]:
        p,*_=shell(N,Q(2,3));test(p==Q(3**N//2**N,3**N),'flat '+str(N))
        p,*_=shell(N,Q(0));test(p==1,'pure '+str(N))
    test(shell(1,Q(1,21))[0]==Q(20,21),'one cell')
    test(shell(2,Q(1,21))[0]==Q(410,441),'two cells partial shell')
    lo=entropy_compare(1,10);hi=entropy_compare(11,100)
    test(lo[0]<lo[1],'rstar >1/10');test(hi[0]>hi[1],'rstar <11/100')
    p,m,t,n=shell(300,Q(1,21));e=1-p
    test(e<Q(1,10000),'finite collective error below1e-4')
    test(e/(1-e)<Q(1,9999),'finite total relative entropy upper')
    test(Q(300,21)>14,'independent total relative entropy lower')
    for N in [1,2,5,20]:
        q=Q(1,3);mass,*_=shell(N,q);purity=(1-q)**2+q*q/2
        test(mass*mass<=(3**N//2**N)*purity**N,'Holder alpha2 '+str(N))
    dep='explorations/conditional-build/k1916-bath-preparation-resource-limits-2026-10-21.md'
    return {'result_id':'K1918','status':'active_research','evidence_kind':'analytic spectral/CLT/type proof plus exact finite Fraction controls',
      'mathematical_controls':checks,'dependencies':{dep:hashlib.sha256((ROOT/dep).read_bytes()).hexdigest()},
      'finite_example':{'N':300,'q':'1/21','cut_shell':m,'last_shell_selected':str(t),'last_shell_size':str(n),'mass':str(p),'error':str(e),'error_decimal_for_orientation':float(e),'certified_error_upper':'1/10000','certified_D_upper':'1/9999','independent_D_lower':'300/21'},
      'critical':{'rate':'log(d/k)','entropy_equal_rate_mass_limit':'1/2','entropy_equal_rate_D_limit':'log(2)','qutrit_rstar_bounds':['1/10','11/100']},
      'scope':'faithful finite product spectra, extreme channel and unrestricted collective endpoint unitaries; no locality or work protocol',
      'not_claimed':['sharp fixed-spectrum diamond optimum','local construction','finite-rate exact preparation','native GU','novelty','formal proof']}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();r=payload()
    if a.write:REPORT.write_text(json.dumps(r,indent=2)+'\n')
    else:assert json.loads(REPORT.read_text())==r,'report consistency'
    print('PASS K1918 exact finite controls:',len(r['mathematical_controls']),'; example error',r['finite_example']['error_decimal_for_orientation'])
