"""Separate bath-label implementation and actual-data mathematical faults."""
from fractions import Fraction as Q
from pathlib import Path
import json,hashlib,copy
ROOT=Path(__file__).resolve().parents[2]

def direct(s,p,t):
    Z=1+t+t*t+t*t*t;mass=dict(zip(s,p));retained=Q(0)
    for x,px in mass.items():
        retention=Q(0)
        for b in range(4):
            incoming=[mass[y]*t**c/Z for y in mass for c in range(4) if y+c==x+b and y!=x]
            retention+=max([px*t**b/Z]+incoming)/2
        # The shell formula caps total incoming retention at the original population.
        retained+=min(px,retention)
    return 1-retained

def check_merger(row):
    t,w=Q(row['t']),Q(row['w']);n=row['n'];x=3+Q(1,n)
    old=direct([Q(1),x+1],[w,1-w],t);new=direct([Q(1),Q(4)],[w,1-w],t)
    assert old==Q(row['old']) and new==Q(row['limit']) and new<=old, 'return/resonance mismatch'

def physical(a,s,p):
    assert len(a)==len(set(a)) and all(y-x>=1 for x,y in zip(a,a[1:])), 'gap failure'
    assert sum(p)==1 and all(x>=0 for x in p), 'normalization failure'
    assert set(s)<=set(a), 'support absent'
    for energy in {x+b for x in s for b in range(4)}:
        input_positions={(x,b) for x in s for b in range(4) if x+b==energy}
        physical_positions={(x,b) for x in a for b in range(4) if x+b==energy}
        assert len(physical_positions)>=2*len(input_positions), 'rank failure'

def main():
    d=json.loads((ROOT/'lab/process/k2010-countable-thermal-attainment.json').read_text());checks=0
    for r in d['resonance_mergers']:check_merger(r);checks+=1
    for r in d['geometric_limits']:
        t,z=Q(r['t']),Q(r['r']);k=r['k'];s=[Q(2*i+1) for i in range(k)];p=[(1-z)*z**i/(1-z**k) for i in range(k)]
        assert direct(s,p,t)==Q(r['finite']), 'geometric return';checks+=1
    for r in d['escaping_energy']:
        n=r['n'];q=Q(1,n);assert Q(r['mean'])==(1-q)+(n+4)*q
        assert Q(r['l1_to_limit'])==abs((1-q)-1)+abs(q);checks+=1
    for r in d['strict_tail_margins']:
        assert Q(r['coefficient'])==Q(3,20)*Q(r['energy'])-Q(113,100)>0;checks+=1
    for r in d['positive_price_transfers']:
        lam=Q(r['price']);N=r['N'];x=Q(r['remote_offset']);q=Q(r['tail']);p=[(1-q)*Q(2,5),(1-q)*Q(3,5),q]
        support=[Q(1),Q(3),x+1];mean=sum(z*v for z,v in zip(support,p));B=Q(1,2)+lam
        before=direct(support,p,Q(1,2))+lam*mean;after=direct([Q(1),Q(3)],[Q(2,5),Q(3,5)],Q(1,2))+lam*Q(11,5)
        assert before==Q(r['before'])<=B and after==Q(r['after']) and N>1+1/lam
        assert after-before<=Q(r['difference_upper'])<0 and r['dimension_bound']==2*N+7
        physical(list(map(Q,range(5)))+[x,x+1,x+2],support,p);checks+=1
    a=list(map(Q,range(6)));s=[Q(1),Q(4)];p=[Q(1,2)]*2;physical(a,s,p);checks+=1
    # No positive gap: a genuinely non-tight sequence in a bounded energy window.
    for n in (10,30,100):
        values=[Q(i,n) for i in range(n)];assert sum(values)/n<1
        assert Q(n-3,n)>Q(1,2);checks+=1
    for path,h in d['inputs'].items():assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==h
    faults=[]
    def reject(name,fn):
        try:fn()
        except AssertionError as e:faults.append((name,str(e)));return
        raise AssertionError('undetected mathematical fault '+name)
    reject('colliding spectrum',lambda:physical([Q(0),Q(1),Q(2),Q(2),Q(3),Q(4)],s,p))
    reject('lost completion',lambda:physical(a[:-1],s,p))
    reject('lost tail normalization',lambda:physical(a,s,[Q(1,2),Q(1,3)]))
    bad=copy.deepcopy(d['resonance_mergers'][0]);bad['limit']=str(Q(bad['limit'])+Q(1,100))
    reject('frozen wrong limit return',lambda:check_merger(bad))
    print('PASS K2010 probe',checks,'arithmetic groups;',len(faults),'mathematical faults;',len(d['inputs']),'provenance hashes')
    for name,reason in faults:print('DETECTED',name,reason)
if __name__=='__main__':main()
