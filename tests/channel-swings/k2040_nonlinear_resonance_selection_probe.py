"""Independent exponent census and rational-quadratic-field dynamical controls."""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,copy
ROOT=Path(__file__).resolve().parents[2]
# Q[a], a^2=70-19a. Never round the irrational frequency.
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def mul(x,y):return (x[0]*y[0]+70*x[1]*y[1],x[0]*y[1]+x[1]*y[0]-19*x[1]*y[1])
def scale(n,x):return (n*x[0],n*x[1])
def inv(x):
    c,d=x;den=c*c-19*c*d-70*d*d
    return ((c-19*d)/den,-d/den)
def compositions(total,n):
    if n==1:yield (total,);return
    for x in range(total+1):
        for tail in compositions(total-x,n-1):yield (x,)+tail

def actual_norm_rates(k,z,nu):
    # Direct real derivatives of Re(product z^p conjugate(z)^q).
    p=[max(t,0) for t in k];q=[max(-t,0) for t in k]
    def monomial(pp,qq):
        value=1+0j
        for zz,i,j in zip(z,pp,qq):value*=zz**i*zz.conjugate()**j
        return value
    rates=[]
    for j in range(6):
        dz=dc=0j
        if p[j]:
            pp=p.copy();pp[j]-=1;dz=p[j]*monomial(pp,q)
        if q[j]:
            qq=q.copy();qq[j]-=1;dc=q[j]*monomial(p,qq)
        vx=(dz+dc).real;vy=(1j*(dz-dc)).real
        coeff=2*(-z[j].real*vy+z[j].imag*vx)
        assert coeff==int(coeff)
        rates.append(scale(int(coeff),nu[j]))
    return rates

def verify(r):
    for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'provenance'
    omega=[(Q(1),Q(0)),(Q(2),Q(0)),(Q(0),Q(1)),(Q(0),Q(2)),(Q(19),Q(1)),(Q(38),Q(2))]
    nu=[inv(x) for x in omega]
    for n,w in zip(nu,r['rotation_weights']):assert scale(140,n)==tuple(w),'actual inverse frequency'
    def charge(k):
        out=(Q(0),Q(0))
        for x,n in zip(k,nu):out=add(out,scale(x,n))
        return out
    found=set();counts={}
    for degree in (2,4,6):
        ct=0
        for ex in compositions(degree,12):
            k=tuple(ex[j]-ex[j+6] for j in range(6))
            if charge(k)==(0,0):
                ct+=1
                if any(k):found.add(k)
                if degree<=4:assert not any(k),'quartic phase charge'
        counts[degree]=ct
    assert found==set(map(tuple,r['small_even_resonances'])),'complete even resonance census'
    w6=r['witness6'];w80=r['witness80']
    assert sum(map(abs,w6))==6 and sum(map(abs,w80))==80
    assert charge(w6)==charge(w80)==(0,0),'witness charge'
    # For V=Re(z1^2 conjugate(z2)^4), z1=1+i,z2=1: Im monomial=2.
    rates=[scale(4*k,n) for k,n in zip(w6,nu)]
    assert actual_norm_rates(w6,[1+1j,1+0j,1+0j,1+0j,1+0j,1+0j],nu)==rates
    assert rates[:2]==[(8,0),(-8,0)] and add(*rates[:2])==(0,0),'sector transfer'
    # Degree80 witness at z1=i and other coordinates1: Im monomial=1.
    group=[]
    for j in (0,2,4):group.append(add(scale(2*w80[j],nu[j]),scale(2*w80[j+1],nu[j+1])))
    raw=actual_norm_rates(w80,[1j,1+0j,1+0j,1+0j,1+0j,1+0j],nu)
    assert [add(raw[j],raw[j+1]) for j in (0,2,4)]==group
    assert group==[(19,0),(-19,-1),(0,1)] and add(add(group[0],group[1]),group[2])==(0,0),'paired transfer'
    assert r['first_even_sector_transfer_degree']==6 and r['first_pair_group_transfer_degree']==80,'claimed thresholds'
    # Planted nonresonant even monomial and resonant odd cubic: the filters differ.
    assert charge((1,-1,0,0,0,0))!=(0,0)
    assert charge((1,-2,0,0,0,0))==(0,0)
    assert 25*25<641<26*26,'irrational discriminant'
    return counts
if __name__=='__main__':
    r=json.loads((ROOT/'lab/process/k2040-nonlinear-resonance-selection.json').read_text());print('PASS baseline',verify(r))
    faults=[]
    for label,mut in [('frequency',lambda x:x['rotation_weights'][2].__setitem__(0,39)),('quartic-transfer',lambda x:x.__setitem__('first_even_sector_transfer_degree',4)),('early-group-transfer',lambda x:x.__setitem__('first_pair_group_transfer_degree',78)),('nonresonant-witness',lambda x:x['witness80'].__setitem__(0,8))]:
        bad=copy.deepcopy(r);mut(bad)
        try:verify(bad)
        except AssertionError as e:faults.append(label);print('DETECTED',label,str(e))
        else:raise AssertionError('MISSED '+label)
    print('PASS',len(faults),'actual data/frequency faults')
