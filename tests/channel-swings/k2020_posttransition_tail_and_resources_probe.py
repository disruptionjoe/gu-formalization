"""Separate bath-label / shell-rank replay and actual physical fault injections."""
from fractions import Fraction as Q
from pathlib import Path
from copy import deepcopy
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
def direct(s,p,t):
    b=[t**j/sum(t**k for k in range(4)) for j in range(4)]
    return sum(max(Q(0),v-sum(max(w*b[k] for y,w in zip(s,p) for k in range(4) if y+k==x+j)/2 for j in range(4))) for x,v in zip(s,p))
def shell(a,s):
    return all(sum(x+b==e for x in a for b in range(4))>=2*sum(x+b==e for x in s for b in range(4)) for e in {x+b for x in s for b in range(4)})
def formula(d,E):
    a=Q(6,5);b=Q(11,5);c=Q(113,91)
    if E<=a:return Q(63,100)-Q(3,20)*E
    if E<=c:return Q(9,20)-Q(9,76)*(E-a)
    lefts=[Q(81,182)-Q(66,455)/(Q(436,455)+d)*(E-c),Q(81,182)-Q(477,2912)/(Q(825,728)+d)*(E-c)]
    rights=[Q(3,10)+Q(3,20)/(1-d)*(b-E),Q(3,10)+(b-E)/4]
    return min(lefts+rights)
def witness(w):
    a=list(map(Q,w['spectrum']));s=list(map(Q,w['support']));p=list(map(Q,w['populations']));d=Q(w['delta']);E=Q(w['energy'])
    assert sum(p)==1 and min(p)>=0 and sum(x*y for x,y in zip(s,p))==E
    assert shell(a,[x for x,y in zip(s,p) if y]);assert len(a)==w['dimension'] and len(set(a))==len(a) and min(y-x for x,y in zip(a,a[1:]))>=d
    r=direct(s,p,Q(1,2));assert r==Q(w['return_value'])==formula(d,E)
    assert Q(w['kappa'])==(9-E)/10-r>=Q(33,100)
    assert Q(w['bath_TV_gap_radius'])==(r-Q(63,100)+Q(3,20)*E)/2>0

def run():
    z=json.loads((ROOT/'lab/process/k2020-posttransition-tail-and-resources.json').read_text())
    for r in z['zero_loss_deletions']:
        s=list(map(Q,r['support']));p=list(map(Q,r['populations']));t=Q(r['t']);q=sum(y for x,y in zip(s,p) if x>r['cutoff']);low=[y if x<=r['cutoff'] else Q(0) for x,y in zip(s,p)]
        assert sum(low)==1-q and direct(s,low,t)<=direct(s,p,t)
    for row in z['terminal_breakpoint_controls']:
        t=Q(row['t']);gap=row['gap'];p=Q(row['p']);incoming=Q(row['incoming']);weights=[t**k/sum(t**j for j in range(4)) for k in range(4)];L=sum(weights[:4-gap]);H=sum(weights[gap:]);vals=[]
        for u in map(Q,row['u']):
            incoming_to_predecessor=max(L*u-H*p,0);incoming_to_terminal=max(H*p-L*u,0)
            vals.append(max(p-incoming-incoming_to_predecessor,0)+max(u-incoming_to_terminal,0))
        assert vals==list(map(Q,row['twice_local_return'])) and all(x<=y for x,y in zip(vals,vals[1:]))
    for w in z['globally_optimal_witnesses']:witness(w)
    for r in z['secant_consumers']:
        d,E,q,x,low,kap=[Q(r[k]) for k in ['delta','energy','tail_mass','retained_budget','lower_return','kappa']]
        assert x==(E-9*q)/(1-q) and low==(1-q)*formula(d,x)
        assert low>=formula(d,E)+kap*q
    # Independent exact slope floor and sharp zero-loss witness.
    assert Q(477,4756)>Q(1,10)
    assert direct([Q(1),Q(3)],[Q(9,10),Q(1,10)],Q(1,2))==direct([Q(1)],[Q(9,10)],Q(1,2))==Q(9,20)
    faults=[]
    baseline=next(w for w in z['globally_optimal_witnesses'] if w['kind']=='CD-fourteen')
    witness(baseline)
    for name in ['normalization','completion','return','energy','wide_spacing']:
        w=deepcopy(baseline)
        if name=='normalization':w['populations'][0]=str(Q(w['populations'][0])+Q(1,100))
        elif name=='completion':w['spectrum']=w['support'];w['dimension']=len(w['spectrum'])
        elif name=='return':w['return_value']=str(Q(w['return_value'])-Q(1,100))
        elif name=='energy':w['energy']=str(Q(w['energy'])-Q(1,100))
        else:w['delta']='3/5'
        try:witness(w)
        except AssertionError:faults.append(name)
        else:raise AssertionError('accepted '+name)
    # The normalized version is false: erasing mass then renormalizing gives1/2>9/20.
    assert direct([Q(1)],[Q(1)],Q(1,2))>Q(9,20)
    for p,h in z['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    print('PASS K2020 separate',len(z['zero_loss_deletions']),'deletions',len(z['terminal_breakpoint_controls']),'terminal programs',len(z['globally_optimal_witnesses']),'physical optima',len(z['secant_consumers']),'consumers;',len(faults),'actual physical faults;',len(z['inputs']),'provenance hashes')
if __name__=='__main__':run()
