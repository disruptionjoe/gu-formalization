#!/usr/bin/env python3
"""Exact finite tensor collision channels, fresh/reused faults and Choi mass."""
import sympy as s
from fractions import Fraction as F
from math import comb
from k2256_causal_fresh_resource_reset_probe import trace_keep,embed
FAULTS=['missing_even_phase','wrong_temperature','same_cell','correlated_stock','missing_reference_multiplicity','wrong_heat_observable']
def controls(fault=None):
    out={}
    def ck(k,v):out[k]=bool(v)
    simp=lambda M:M.applyfunc(s.simplify)
    p=s.Rational(1,5);tau=s.diag(1-p,p);don=tau if fault!='wrong_temperature' else s.diag(s.Rational(3,4),s.Rational(1,4))
    c=s.Rational(1,2);ss=s.sqrt(3)/2;phase=c-s.I*ss
    U=s.diag(1,1,1,phase**2);U[1,1]=U[2,2]=phase*c;U[1,2]=U[2,1]=phase*s.I*ss
    if fault=='missing_even_phase':U[3,3]=1
    ck('collision_unitary',simp(U.H*U)==s.eye(4));N=s.diag(0,1,1,2);ck('charge_conserved',U*N==N*U)
    def direct(E):return simp(trace_keep(U*s.kronecker_product(E,don)*U.H,[0],2))
    def formula(E,L):
        a=(c+s.I*ss)**L*c**L;q=p*s.trace(E)+c**(2*L)*(E[1,1]-p*s.trace(E))
        return simp(s.Matrix([[s.trace(E)-q,a*E[0,1]],[s.conjugate(a)*E[1,0],q]]))
    for i in range(2):
      for j in range(2):
        E=s.zeros(2);E[i,j]=1
        for L in [1,2,3]:
          z=E
          for _ in range(L):z=direct(z)
          ck('matrix_unit_'+str((i,j,L)),simp(z-formula(E,L))==s.zeros(2))
    excited=s.diag(0,1);vac=s.diag(1,0)
    ck('one_collision_population',direct(excited)[1,1]==s.Rational(2,5))
    two=simp(trace_keep(U*U*s.kronecker_product(excited,don)*U.H*U.H,[0],2))
    fresh=direct(direct(excited));actual=two if fault=='same_cell' else fresh
    ck('two_fresh_population',actual[1,1]==s.Rational(1,4))
    ck('same_cell_counterexample',two[1,1]-fresh[1,1]==s.Rational(3,20))
    # Entangled donor/reference exact two-fresh-cell network, input B,R,E1,E2.
    bell=s.Matrix([1,0,0,1])/s.sqrt(2);rho=bell*bell.H
    stock=s.kronecker_product(don,don) if fault!='correlated_stock' else s.diag(1-p,0,0,p)
    W=embed(U,[0,3],4)*embed(U,[0,2],4)
    got=simp(trace_keep(W*s.kronecker_product(rho,stock)*W.H,[0,1],4));expected=s.zeros(4)
    for i in range(2):
      for j in range(2):
        E=s.zeros(2);E[i,j]=1;expected+=s.kronecker_product(formula(E,2),E)/2
    ck('entangled_network_formula',simp(got-expected)==s.zeros(4))
    # Two service outputs around one exact renewal expose correlations invisible to a donor marginal.
    FF=s.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,-1]])
    circuit=embed(FF,[1,2],4)*embed(FF,[2,3],4)*embed(FF,[0,2],4)
    initial=s.kronecker_product(vac,vac,stock)
    history=trace_keep(circuit*initial*circuit.H,[0,1],4)
    ck('renewed_two_output_history',history==s.kronecker_product(tau,tau))
    correlated_initial=s.kronecker_product(vac,vac,s.diag(1-p,0,0,p))
    correlated_history=trace_keep(circuit*correlated_initial*circuit.H,[0,1],4)
    ck('actual_correlated_error',sum(abs(correlated_history[i,i]-s.kronecker_product(tau,tau)[i,i]) for i in range(4))/2==s.Rational(8,25))
    delta=simp(got-s.kronecker_product(tau,s.eye(2)/2))
    # Exact eigenvalues of the actual4-by4 Hermitian difference.
    d=s.Rational(1,8)+s.Rational(4,5)/16
    dist=s.simplify(sum(abs(ev)*m for ev,m in delta.eigenvals().items())/2)
    ck('entangled_complete_bound',bool(dist<=d))
    for qq in [s.Rational(0),s.Rational(1,3),s.Rational(1)]:
        inp=s.diag(1-qq,qq);z=simp(U*s.kronecker_product(inp,tau)*U.H)
        bath_number=s.diag(0,-1 if fault=='wrong_heat_observable' else 1)
        qe=s.trace((trace_keep(z,[1],2)-tau)*bath_number)
        heat=(1-c*c)*(qq-p)
        ck('bath_charge_change_'+str(qq),s.simplify(qe-heat)==0)
        ck('total_charge_'+str(qq),s.trace(z*N)==qq+p)
    rr=F(1,2**20);dd=rr/2+F(4,5)*rr*rr
    ck('renewal_999_budget',999*dd<F(477,10**6));ck('total_service_budget',999*dd+F(2,10000)<F(677,10**6))
    ck('finite_stock_count',999*20+1==19981);ck('finite_contact_count',999*20+1000==20980)
    # Independently enumerate normalized Choi eigenvalues and compare binomial levels.
    for K in range(1,6):
      n=2**K
      for pp in [F(1,5),F(1,2),F(4,5)]:
        spec=sorted([pp**j*(1-pp)**(K-j)/n for bits in range(n) for j in [bits.bit_count()] for _ in range(n)],reverse=True)
        mult=n if fault!='missing_reference_multiplicity' else 1
        levels=sorted([(pp**j*(1-pp)**(K-j)/n,mult*comb(K,j)) for j in range(K+1)],reverse=True)
        replay=[v for v,m in levels for _ in range(m)]
        ck('Choi_spectrum_'+str((K,pp)),spec==replay and sum(spec)==1)
        for eps in [F(0),F(1,4),F(1,2)]:
          total=F(0);count=0
          for val in spec:
            if total>=1-eps:break
            total+=val;count+=1
          ck('support_threshold_'+str((K,pp,eps)),sum(spec[:count])>=1-eps and (not count or sum(spec[:count-1])<1-eps))
          ck('max_eigen_bound_'+str((K,pp,eps)),count>=(1-eps)*(2/max(pp,1-pp))**K)
          if eps==0:ck('exact_rank_'+str((K,pp)),count==4**K)
        if pp==F(1,2):ck('one_fewer_qubit_floor_'+str(K),1-sum(spec[:4**(K-1)])==F(3,4))
    # Large finite consumer uses only11 binomial levels, never a million-entry spectrum.
    K=10;pp=F(1,5);target=F(99,100);mass=F(0);count=0;last=None
    for j in range(K+1):
        val=pp**j*(1-pp)**(K-j)/2**K;m=2**K*comb(K,j)
        need=(target-mass)/val;take=min(m,max(0,need.__ceil__()))
        mass+=take*val;count+=take;last=val
        if mass>=target:break
    ck('ten_call_smooth_rank',count==617857 and j==5)
    ck('ten_call_exact_mass',mass==F(9900000256,10**10) and mass-last==F(9899999232,10**10))
    ck('ten_call_dimension',786**2<count<=787**2)
    for K in [1,2,5,10]:
        weights=[F(comb(K,j))*pp**j*(1-pp)**(K-j) for j in range(K+1)]
        mean=sum(F(j)*w for j,w in enumerate(weights));var=sum((F(j)-mean)**2*w for j,w in enumerate(weights))
        ck('information_variance_'+str(K),4*var==F(16*K,25))
    return out

RESULT='K2259'
REPORT='lab/process/k2259-microscopic-donor-renewal.json'
DEPS=['explorations/conditional-build/k2259-microscopic-donor-renewal-2026-10-29.md', 'tests/channel-swings/k2256_causal_fresh_resource_reset_probe.py', 'explorations/conditional-build/k2256-causal-fresh-resource-reset-2026-10-29.md', 'explorations/conditional-build/k2249-finite-density-chain-reset-2026-10-29.md']
EVIDENCE='Finite exact algebra and rational controls; changed mathematical/resource inputs must fail unchanged checks. Universal proofs and report hashes are separate evidence.'

def main():
    import argparse,hashlib,json
    from pathlib import Path
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args()
    root=Path(__file__).resolve().parents[2];checks=controls()
    assert all(checks.values()),[k for k,v in checks.items() if not v]
    faults={}
    for f in FAULTS:
        bad=[k for k,v in controls(f).items() if not v];assert bad,('undetected input fault',f);faults[f]=bad
    report=dict(result_id=RESULT,checks=checks,fault_failures=faults,evidence_kinds=EVIDENCE,dependency_sha256={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in DEPS},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    p=root/REPORT
    if a.write:p.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(p.read_text())==report,'report drift'
    print(json.dumps(dict(result=RESULT,controls=len(checks),faults=len(faults))))
if __name__=='__main__':main()
