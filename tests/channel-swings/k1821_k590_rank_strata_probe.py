#!/usr/bin/env python3
"""Independent small-complex controls plus explicit artifact mutation rejection."""
import copy
import itertools
import json
from pathlib import Path
import k1821_k590_rank_strata as m


def main():
    data=json.loads(m.ARTIFACT.read_text());m.validate(data) # clean before mutations
    # Exhaust all two-arrow 1->2->1 complexes over GF(2), without rank routine.
    count=0; profiles=set()
    for h in itertools.product((0,1),repeat=2):
        for l in itertools.product((0,1),repeat=2):
            if sum(x*y for x,y in zip(h,l))%2:continue
            rh,rl=int(any(h)),int(any(l));u,v=1-rh,1-rl
            actual=[1-rh,2-rh-rl,1-rl]
            assert actual==m.stratum(1,1,u,v)['homology']
            profiles.add(tuple(actual));count+=1
    assert count==10 and profiles=={(0,0,0),(0,1,1),(1,1,0),(1,2,1)}
    # Rank normal forms for every deficit in 2->5->3, including the zero maps.
    for u,v in itertools.product(range(3),range(4)):
        h=[[int(i==j and j<2-u) for j in range(2)] for i in range(5)]
        l=[[int(j==2+i and i<3-v) for j in range(5)] for i in range(3)]
        assert m.homology(h,l)==[u,u+v,v]
        # Independent standard half-sum-squares dimension formula.
        actual_dim=(2**2+5**2+3**2-u*u-(u+v)**2-v*v)//2
        row=m.stratum(2,3,u,v);assert row['dimension']==actual_dim
        assert row['codimension']==u*u+u*v+v*v
    # Planted nonzero composition and boundary-leaking perturbation.
    high,low,d,p,w,ps=m.representative(1)
    bad=copy.deepcopy(d);bad[0][0]=1
    try:m.homology(high,bad)
    except ValueError as e:assert 'composition' in str(e)
    else:raise AssertionError('accepted non-complex')
    bad=copy.deepcopy(d);bad[0][5]+=1
    assert not m.zero(m.subtract(m.mul(ps[2],bad),m.mul(bad,ps[1])))
    # Endomorphism P genuinely uses two independent M and E directions.
    assert m.rank([w[:3],w[3:]])==2
    assert data['extra_relation_control']['homology']==[0,0,1]
    # Independent Euler check: repaired dimensions 4-9+6=1.
    assert sum((-1)**i*x for i,x in enumerate([4,9,6]))==1
    # These are reporting mutations, separate from the constructions above.
    mutations=[('homology',lambda x:x['full_size_rank_one_endpoint'].update(homology=[0,0,1])),
      ('rank',lambda x:x.update(operator_schmidt_rank=1)),
      ('pairing',lambda x:x['pairing_controls'][1].update(representative_norm='2')),
      ('source',lambda x:x['claim_boundary'].update(source_action_selected=True)),
      ('codimension',lambda x:x['full_strata'][3].update(codimension=2)),
      ('ownership',lambda x:x['factorwise_algebra'].update(rank_one_loss_in_algebra=True))]
    for label,change in mutations:
        bad=copy.deepcopy(data);change(bad)
        try:m.validate(bad)
        except ValueError as e:
            assert 'artifact differs' in str(e);print('REJECTED:',label)
        else:raise AssertionError('missed '+label)
    print('PASS: 10 finite-field complexes, 12 rational normal forms, two planted failures, entanglement; six reporting mutations')

if __name__=='__main__':main()
