"""Independent bath-label and planar-vertex controls for K1943."""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import hashlib,json
import k1943_arbitrary_preparation_catalyst_energy as main

ROOT=Path(__file__).resolve().parents[2]
def spectral_rate(t,S,p):
    """Direct bath-state output assignment; never calls the edge-rate routine."""
    q=[t**b/sum(t**j for j in range(4)) for b in range(4)]
    at_half={s:F(0) for s in S};at_one=at_half.copy();total=F(0)
    for e in sorted({s+b for s in S for b in range(4)}):
        entries=[(p[i]*q[b],s) for i,s in enumerate(S) for b in range(4) if s+b==e]
        assert len(entries)<=2,'physical rank allowance'
        entries.sort(reverse=True)
        if len(entries)==1:
            w,s=entries[0];at_half[s]+=w/2;at_one[s]+=w
        else:
            (w,s),(v,u)=entries;at_half[s]+=w/2;at_half[u]+=w/2;at_one[s]+=w
        total+=sum(w for w,s in entries)
    assert total==1,'bath probability'
    # All returned mass outside S is positive. Half trace norm is the total
    # positive deficit on S, even when a site gains more than its input.
    returns=[sum(max(F(0),p[i]-out[s]) for i,s in enumerate(S)) for out in [at_half,at_one]]
    assert returns[1]<=returns[0],'all-input endpoint domination'
    return max(returns)

def planar_optimum(t,S,E):
    """Enumerate all break-line vertices in p0,p1; p2=1-p0-p1."""
    assert len(S)==3
    best=F(1);counts=0
    def lin(w):return (w[0]-w[2],w[1]-w[2],w[2])
    for orientation in product((-1,1),repeat=2):
        # line a*p0+b*p1+c=0. Include simplex, energy, max switches and deficits.
        lines=[(F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(1),F(1),F(-1)),(F(S[0]-S[2]),F(S[1]-S[2]),F(S[2])-E)]
        inc=[[F(0)]*3 for _ in range(3)];edge=[]
        Z=sum(t**b for b in range(4))
        for i,sgn in enumerate(orientation):
            d=S[i+1]-S[i];L=sum(t**b for b in range(4-d))/Z;H=t**d*L
            w=[F(0)]*3;w[i]=H;w[i+1]=-L;edge.append(w);lines.append(lin(w))
            receiver=i+1 if sgn==1 else i
            inc[receiver]=[a+sgn*b for a,b in zip(inc[receiver],w)]
        for i in range(3):lines.append(lin([F(int(i==j))-inc[i][j] for j in range(3)]))
        for (a,b,c),(d,e,f) in combinations(lines,2):
            det=a*e-b*d
            if not det:continue
            x=(b*f-c*e)/det;y=(c*d-a*f)/det;p=[x,y,1-x-y]
            if min(p)<0 or sum(s*w for s,w in zip(S,p))>E:continue
            if any(sgn*sum(u*v for u,v in zip(w,p))<0 for sgn,w in zip(orientation,edge)):continue
            best=min(best,spectral_rate(t,S,p));counts+=1
    return best,counts

def check_report(r):
    assert r['source_sha256']==hashlib.sha256(Path(main.__file__).read_bytes()).hexdigest(),'source pin'
    assert r['claim']=='K1943','report identity'

def run():
    r=json.loads(main.REPORT.read_text());check_report(r);count=0
    for S in [[1,3,5],[2,3,6],[1,4,5],[1,3,7]]:
        for t in [F(1,2),F(3,4)]:
            for a in range(1,6):
                for b in range(1,7-a):
                    p=[F(a,7),F(b,7),F(7-a-b,7)]
                    assert spectral_rate(t,S,p)==main.rate(t,S,p)[0],'independent shell-rate agreement';count+=1
                    energy=sum(s*w for s,w in zip(S,p))
                    low=[i for i,s in enumerate(S) if 1<=s<2]
                    delta=1-sum(p[i] for i in low)
                    assert delta<=energy-1,'excess-energy tail bound'
                    assert spectral_rate(t,S,p)>=F(1,2)-delta>=F(3,2)-energy,'low-energy population return bound';count+=2
    for case in r['energy_cases']:
        if len(case['support'])!=3:continue
        value,k=planar_optimum(F(case['t']),case['support'],F(case['energy_budget']))
        assert value==F(case['optimum']),'independent planar optimum';count+=k+1
    for eta in [F(1,1000),F(1,100),F(1,10)]:
        S=[1,3,5];p=[1-eta,eta,F(0)];energy=1+2*eta
        bound=F(3,2)-energy
        assert bound>0 and spectral_rate(F(1,2),S,p)>=bound,'nonvacuous near-threshold energy bound';count+=1
    ex=r['shifted_example'];S=list(map(F,ex['support']));p=list(map(F,ex['weights']))
    assert spectral_rate(F(1,2),S,p)==F(ex['return_cost']),'fractional component witness';count+=1
    for ex in r['physical_mixtures']:
        S=list(map(F,ex['support']));p=list(map(F,ex['weights']))
        assert spectral_rate(F(ex['t']),S,p)==F(ex['return_cost']),'independent physical mixture'
        assert sum(e*w for e,w in zip(S,p))<=F(ex['E']),'independent mixture energy';count+=2
    # Truncation test on actual returns, with normalized lower-energy support.
    for t in [F(1,3),F(1,2),F(3,4)]:
        S=[1,3,5,7];p=[F(1,10),F(1,5),F(3,10),F(2,5)];old=spectral_rate(t,S,p)
        for keep in range(1,4):
            delta=sum(p[keep:]);new=[v/(1-delta) for v in p[:keep]]
            assert spectral_rate(t,S[:keep],new)<=old+2*delta,'cutoff return continuity'
            assert sum(s*w for s,w in zip(S,new))<=sum(s*w for s,w in zip(S,p)),'truncation energy';count+=2
            cutoff=F(S[keep-1]);energy=sum(s*w for s,w in zip(S,p))
            if cutoff>1:
                assert delta<=(energy-1)/(cutoff-1),'centered cutoff mass bound';count+=1
    # Baseline above is green before any fault is considered.
    faults=[]
    S=[1,3,5];p=[F(1,2),F(1,3),F(1,6)]
    try:assert main.rate(F(1,2),S,p,'normalization')[0]==spectral_rate(F(1,2),S,p),'corrupt return normalization'
    except AssertionError as exc:faults.append(str(exc))
    for fault in ['energy','dual']:
        case=r['energy_cases'][0];cert=next(c for c in case['cells'] if not c.get('infeasible'))
        try:main.verify_cell(F(case['t']),case['support'],F(case['energy_budget']),cert,fault)
        except AssertionError as exc:faults.append(str(exc))
    try:main.mixture_verify(r['convexified_cutoffs'][0],'mix_dual')
    except AssertionError as exc:faults.append(str(exc))
    assert len(faults)==4,'all mathematical faults detected by assertions'
    consistency=[]
    for field,value in [('claim','K0'),('source_sha256','0'*64)]:
        bad=dict(r);bad[field]=value
        try:check_report(bad)
        except AssertionError as exc:consistency.append(str(exc))
    assert len(consistency)==2,'report/pin controls'
    print('PASS',count,'independent exact controls; mathematical faults:',faults,'consistency:',consistency)
if __name__=='__main__':run()
