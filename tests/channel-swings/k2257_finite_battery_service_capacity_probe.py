#!/usr/bin/env python3
"""Exact infinite-law tails via two independent finite coefficient algorithms."""
from fractions import Fraction as F
from math import comb
FAULTS=['wrong_weight','wrong_ratio','ceil_threshold','drop_geometric_tail','uncounted_charge','wrong_variance']
def convolution(K,h,ps):
    a=[F(1)]+[F(0)]*h
    for _ in range(K):a=[sum(a[j]*ps[s-j] for j in range(s+1)) for s in range(h+1)]
    return a
def controls(fault=None):
    out={}
    def ck(k,v):out[k]=bool(v)
    p0=F(337,625);r=F(16,25);a=F(162,625);q=F(288,625)
    if fault=='wrong_weight':a=F(161,625)
    if fault=='wrong_ratio':r=F(15,25)
    ck('infinite_law_normalization',p0+a*r/(1-r)==1)
    ck('nonzero_probability',a*r/(1-r)==q)
    mu=2*a*r/(1-r)**2;second=4*a*r*(1+r)/(1-r)**3
    variance=second-mu*mu
    if fault=='wrong_variance':variance=second
    ck('mean',mu==F(64,25));ck('variance',variance==F(94336,5625))
    ck('pgf_half',p0+a*r*F(1,2)/(1-r*F(1,2))==F(281,425))
    for K in [1,2,3,5,10]:
        for H in [0,1,2,3,8,9,20]:
            h=H//2 if fault!='ceil_threshold' else (H+1)//2
            ps=[p0]+[a*r**j for j in range(1,h+1)]
            if fault=='drop_geometric_tail':ps=[x/sum(ps) for x in ps]
            direct=convolution(K,h,ps);hh=H//2
            mix=[p0**K]+[sum(F(comb(K,x)*comb(s-1,x-1))*p0**(K-x)*q**x*(1-r)**x*r**(s-x) for x in range(1,min(K,s)+1)) for s in range(1,hh+1)]
            tail=1-sum(direct);mtail=1-sum(mix)
            ck('independent_tail_'+str((K,H)),tail==mtail)
            ck('tail_nonzero_'+str((K,H)),tail>0)
            if K==1:ck('single_call_tail_'+str(H),tail==q*r**hh)
            if H==0:ck('zero_budget_tail_'+str(K),tail==1-p0**K)
            lower=1-F(2)**hh*F(281,425)**K
            ck('chernoff_valid_'+str((K,H)),mtail>=lower)
    ck('100_calls_20_charge',F(2)**10*F(281,425)**100<F(1,10**14))
    # For epsilon=.01, squared deficit of H=2546 exceeds allowable Cantelli deficit.
    ck('integer_capacity_2547', (F(64,25)*1000-2546)**2>F(94336,5625)*1000/F(99))
    # Exact charge-shell control: vacuum inputs, charged outputs and residual battery.
    for H in [0,1,2,3,8]:
        outcomes=[(2*j,H-2*j) for j in range(H//2+1)]
        if fault=='uncounted_charge':outcomes.append((H+2,0))
        ck('conserving_support_'+str(H),all(n+b==H and b>=0 and n<=H for n,b in outcomes))
    for J in [1,2,5,20]:
        explicit=sum(F(2*j)*a*r**j for j in range(1,J))+2*J*a*r**J/(1-r)
        ck('bounded_witness_'+str(J),explicit==F(64,25)*(1-r**J))
    ck('zero_nonzero_partition',F(337,625)+F(288,625)==1)
    return out

RESULT='K2257'
REPORT='lab/process/k2257-finite-battery-service-capacity.json'
DEPS=['explorations/conditional-build/k2257-finite-battery-service-capacity-2026-10-29.md', 'explorations/conditional-build/k2253-full-instrument-reference-reuse-2026-10-29.md']
EVIDENCE="Finite exact algebra, changed-input faults and rational resource controls; universal proofs are written separately. Hashes check reporting integrity."

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
