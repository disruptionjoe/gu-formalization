#!/usr/bin/env python3
"""K2232 exact finite controls. Universal proofs are in the note, not sampled here."""
from fractions import Fraction as F
import json

FAULTS=['coherence-decay-rate', 'upward-detailed-balance-rate', 'finite-time-exact-renewal', 'omitted-final-gap-lowering', 'reservoir-heat-sign', 'unequal-contact-gaps', 'double-swap-pulse-area', 'fresh-entry-coupling-bound-on-correlated-state']

def run(fault=None):
    checks=[]
    def check(value, name=None):
        checks.append((name or f"exact-control-{len(checks)+1:03d}", bool(value)))

    def zeros(n): return [[F(0) for _ in range(n)] for _ in range(n)]
    def ident(n): return [[F(i==j) for j in range(n)] for i in range(n)]
    def add(a,b): return [[x+y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
    def scale(a,c): return [[c*x for x in ar] for ar in a]
    def trans(a): return list(map(list,zip(*a)))
    def mul(a,b): return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0)) for j in range(len(b[0]))] for i in range(len(a))]
    def kron(a,b): return [[a[i//len(b)][j//len(b)]*b[i%len(b)][j%len(b)] for j in range(len(a)*len(b))] for i in range(len(a)*len(b))]
    def unit(n,i,j):
        a=zeros(n);a[i][j]=F(1);return a

    def gad(x,p,s,coherence_fault=False):
        """Apply to first qubit, with arbitrary r-dimensional reference blocks."""
        r=len(x)//2;y=zeros(2*r)
        if fault=="upward-detailed-balance-rate": p=p/(2-p)
        if fault=="finite-time-exact-renewal": s=F(0)
        coherence_fault=coherence_fault or fault=="coherence-decay-rate"
        eta=s*s
        for i in range(r):
            for j in range(r):
                a,b,c,d=x[i][j],x[i][j+r],x[i+r][j],x[i+r][j+r]
                y[i][j]=(1-p)*(a+d)+eta*(p*a-(1-p)*d)
                y[i+r][j+r]=p*(a+d)-eta*(p*a-(1-p)*d)
                y[i][j+r]=(eta if coherence_fault else s)*b
                y[i+r][j]=(eta if coherence_fault else s)*c
        return y

    def replace(x,p): return gad(x,p,F(0))
    def kraus(p_sqrt=F(3,5),q_sqrt=F(4,5),s=F(3,5),z=F(4,5)):
        return [scale([[1,0],[0,s]],q_sqrt),scale([[0,z],[0,0]],q_sqrt),
                scale([[s,0],[0,1]],p_sqrt),scale([[0,0],[z,0]],p_sqrt)]

    p=F(9,25);s=F(3,5);ks=kraus()
    completeness=zeros(2)
    for k in ks: completeness=add(completeness,mul(trans(k),k))
    check(completeness==ident(2))
    for r in (1,2):
        for i in range(2*r):
            for j in range(2*r):
                x=unit(2*r,i,j);y=zeros(2*r)
                for k in ks:
                    kr=kron(k,ident(r));y=add(y,mul(mul(kr,x),trans(kr)))
                check(y==gad(x,p,s))
                check(gad(gad(x,p,F(2,3)),p,F(3,5))==gad(x,p,F(2,5)))
                check(replace(gad(x,p,s),p)==replace(x,p))
                check(gad(replace(x,p),p,s)==replace(x,p))
    # Fixed Gibbs state and exact upward/downward detailed-balance identity.
    tau=[[1-p,0],[0,p]]
    check(gad(tau,p,s)==tau)
    up=p/2 if fault=="upward-detailed-balance-rate" else p;down=1-p
    check((1-p)*up==p*down)
    # Finite correlated Bell input; output reference marginal unchanged and final
    # replacement removes its correlations, whereas marginal thermalization alone does not.
    bell=scale([[1,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,1]],F(1,2))
    y=gad(bell,p,s)
    for i in range(2):
        for j in range(2): check(y[i][j]+y[i+2][j+2]==F(i==j,2))
    check(replace(bell,p)==kron(tau,scale(ident(2),F(1,2))))
    check(y!=replace(bell,p))
    # Gibbs marginal correlated diagonal bank/reference example at p=1/2.
    cc=scale([[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]],F(1,2))
    check(cc!=replace(cc,F(1,2)))
    # Exact SWAP projector, equal-gap commutator and population exchange.
    perm=[0,2,1,3];S=[[F(perm[j]==i) for j in range(4)] for i in range(4)]
    P=scale(add(ident(4),scale(S,-1)),F(1,2))
    U=ident(4) if fault=="double-swap-pulse-area" else add(ident(4),scale(P,-2))
    check(mul(P,P)==P);check(U==S, "swap-area-endpoint")
    N=[[F(i==j)*(i//2+(2 if fault=="unequal-contact-gaps" else 1)*(i%2)) for j in range(4)] for i in range(4)]
    check(mul(N,S)==mul(S,N))
    for a in range(2):
        for b in range(2):
            x=kron(unit(2,a,b),tau);out=mul(mul(U,x),trans(U))
            ptr=[[sum(out[2*i+k][2*j+k] for k in range(2)) for j in range(2)] for i in range(2)]
            check(ptr==(tau if a==b else zeros(2)))
    # Analytic smooth schedule has area f(1)-f(0)=1. Exercise polynomial C1
    # alternative f=3u²-2u³: exact integral f'=1 and endpoint f'=0; no assertion
    # that this polynomial is the note's C-infinity schedule.
    coeff=[F(0),F(6),F(-6)]
    check(sum(c/F(i+1) for i,c in enumerate(coeff))==1)
    check(sum(coeff)==0);check(coeff[0]==0)
    # Same-bank recurrence at rational gaps: energy identity does not depend on
    # those gaps being dimensionless Gibbs logarithms, only fixed endpoint energies.
    def cycle(w,bank,gaps,ps,eta,drop_final=False,heat_sign=1,instant=False):
        drop_final=drop_final or fault=="omitted-final-gap-lowering"
        heat_sign=-1 if fault=="reservoir-heat-sign" else heat_sign
        work=w*gaps[0]+sum(bank[j-1]*(gaps[j]-gaps[j-1]) for j in range(1,len(bank)))
        if not drop_final: work-=bank[-1]*gaps[-1]
        spent=[w]+bank[:-1]
        renewed=[pj+(0 if instant else eta)*(a-pj) for a,pj in zip(spent,ps)]
        heat=heat_sign*sum(e*(a-b) for e,a,b in zip(gaps,spent,renewed))
        dE=sum(e*(a-b) for e,a,b in zip(gaps,renewed,bank))
        return work,heat,dE,renewed
    ps=[F(1,3),F(1,5),F(1,9)];gaps=[F(1),F(2),F(3)];eta=F(1,16)
    bank=ps[:];wt=qt=F(0);energy0=sum(e*b for e,b in zip(gaps,bank))
    for w in (F(2,5),F(1,7),F(3,4),F(1,2)):
        work,heat,dE,bank=cycle(w,bank,gaps,ps,eta)
        check(work==heat+dE);wt+=work;qt+=heat
    check(wt==qt+sum(e*b for e,b in zip(gaps,bank))-energy0)
    # General work observable spectral range and trace-distance dual bound data.
    x0=F(1);xm=F(3)
    coefficients=[F(1),F(1),-F(3)]
    vals=[sum(c*((mask>>j)&1) for j,c in enumerate(coefficients)) for mask in range(8)]
    check(max(vals)-min(vals)==2*xm-x0)
    # Large consumer is exact rational arithmetic; no 2^1701 matrix is formed.
    Ncells=1701;eta=F(1,2**100);s=F(1,2**50)
    eps=Ncells*(s/2+eta)
    q=F(3*100**1700,3*100**1700+7*101**1700)
    check(eps<F(7554,10**16))
    check(q<F(1930581,10**14))
    check(1000*(q+eps)<F(19306566,10**12))
    xmax_upper=F(17762861,10**6)
    check(2*xmax_upper*eps<F(2684,10**14))
    check(eps*Ncells*xmax_upper<F(2283,10**11))

    # Independent negative countercontrols retain their baseline meaning.
    unequal=[[F(i==j)*(i//2+2*(i%2)) for j in range(4)] for i in range(4)]
    check(mul(unequal,S)!=mul(S,unequal), "unequal-gap-countercontrol")
    check(mul(mul(ident(4),unit(4,2,2)),ident(4))!=mul(mul(S,unit(4,2,2)),S), "double-area-countercontrol")
    singlet=scale([[0,0,0,0],[0,1,-1,0],[0,-1,1,0],[0,0,0,0]],F(1,2))
    value=sum(mul(add(ident(4),scale(S,-1)),singlet)[i][i] for i in range(4))
    check(value<=2, "correlated-coupling-exchange-bound")
    check(value==2, "singlet-coupling-expectation")
    product_entry=kron([[F(1,3),0],[0,F(2,3)]],tau)
    contact_entry=singlet if fault=="fresh-entry-coupling-bound-on-correlated-state" else product_entry
    contact_mean=sum(mul(add(ident(4),scale(S,-1)),contact_entry)[i][i] for i in range(4))
    check(contact_mean<=1, "fresh-product-entry-coupling-exchange-bound")
    return checks



def main():
    import argparse, hashlib, json
    from pathlib import Path
    parser=argparse.ArgumentParser()
    parser.add_argument('--write',action='store_true')
    parser.add_argument('--controls-only',action='store_true')
    args=parser.parse_args()
    baseline=run()
    bad=[name for name,ok in baseline if not ok]
    if bad:
        raise AssertionError('FAIL baseline: '+repr(bad))
    detected={}
    for fault in FAULTS:
        # Exceptions propagate as errors; they never count as detection.
        checks=run(fault)
        failed=[name for name,ok in checks if not ok]
        if not failed:
            raise AssertionError('FAIL mutation escaped: '+fault)
        detected[fault]=failed
    root=Path(__file__).resolve().parents[2]
    deps=['explorations/conditional-build/k2228-continuum-energy-form-detector-control-2026-10-28.md', 'explorations/conditional-build/k2229-finite-step-thermal-reset-work-2026-10-28.md', 'explorations/conditional-build/k2232-smooth-reset-and-thermal-renewal-2026-10-29.md']
    target=root/'lab/process/k2232-smooth-reset-and-thermal-renewal.json'
    report=dict(result='K2232',controls=[dict(name=n,passed=ok) for n,ok in baseline],faults=detected,
        evidence_kind='exact finite arithmetic/Clifford controls; universal proof is in the note',
        probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        dependency_sha256={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in deps})
    if not args.controls_only:
        if args.write: target.write_text(json.dumps(report,indent=2)+'\n')
        elif json.loads(target.read_text())!=report:
            raise AssertionError('FAIL stale certificate')
    print(json.dumps(dict(result='K2232',controls=len(baseline),faults={k:len(v) for k,v in detected.items()})))

if __name__=='__main__': main()
